from fastapi import FastAPI
from market_data import get_market_data
from sentiment import analyze_sentiment
from ai_model import predict
from logger import log_message
from security import check_api_key
log_message("Prediction requested")

if not check_api_key():
    return {"error": "Invalid API key"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/predict")
def prediction():
log_message("Prediction requested")

if not check_api_key():
    return {"error": "Invalid API key"}

    log_message("Prediction requested")

    if not check_api_key():
        return {"error": "Invalid API key"}

    return {"signal": "BUY"}