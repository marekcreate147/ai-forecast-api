from prophet import Prophet
import pandas as pd
from datetime import timedelta

def generate_forecast(history_dict):
    df = pd.DataFrame([
        {"ds": date, "y": qty} for date, qty in history_dict.items()
    ])
    df["ds"] = pd.to_datetime(df["ds"])
    df = df.sort_values("ds")

    model = Prophet(daily_seasonality=True)
    model.fit(df)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    forecast_future = forecast_future.copy()  # <-- Šita eilutė
    forecast_future["yhat"] = forecast_future["yhat"].apply(lambda x: max(x, 0))  # <--- FIX čia

    forecast_sum = round(forecast_future["yhat"].sum())

    forecast_per_day = {
        row["ds"].strftime("%Y-%m-%d"): round(row["yhat"], 2)
        for _, row in forecast_future.iterrows()
    }

    return forecast_sum, forecast_per_day
