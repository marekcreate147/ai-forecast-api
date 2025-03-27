from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from prophet_model import generate_forecast
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Leisti visus domenus (dev tikslams)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ForecastRequest(BaseModel):
    sku: str
    history: dict  # {'YYYY-MM-DD': qty}

@app.post("/forecast")
def forecast(req: ForecastRequest):
    try:
        forecast_sum, daily = generate_forecast(req.history)
        return {
            "sku": req.sku,
            "forecast_sum": forecast_sum,
            "forecast_per_day": daily
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
