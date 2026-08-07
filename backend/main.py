from fastapi import FastAPI
from market_data import get_market_data
from sentiment import analyze_sentiment
from ai_model import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Market Predictor"}

@app.get("/predict")
def prediction():
    market = get_market_data()
    sentiment = analyze_sentiment()
    result = predict()

    return {
        "market": market,
        "sentiment": sentiment,
        "prediction": result
    }