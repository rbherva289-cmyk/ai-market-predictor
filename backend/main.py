from fastapi import FastAPI
from market_data import get_market_data
from sentiment import analyze_sentiment

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Market Predictor"}

@app.get("/predict")
def predict():
    market = get_market_data()
    sentiment = analyze_sentiment()

    return {
        "market": market,
        "sentiment": sentiment,
        "signal": "BUY"
    }