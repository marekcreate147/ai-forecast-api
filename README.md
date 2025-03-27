# AI Forecast API (Prophet)

FastAPI + Facebook Prophet API for WooCommerce integration.

## Endpoint

POST /forecast

```json
{
  "sku": "SKU-123",
  "history": {
    "2025-03-01": 2,
    "2025-03-02": 0,
    ...
  }
}
```

Response:

```json
{
  "sku": "SKU-123",
  "forecast_sum": 22,
  "forecast_per_day": {
    "2025-03-27": 1.2,
    ...
  }
}
```
