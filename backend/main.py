from fastapi import FastAPI
from indicators import calculate_rsi
from sentiment import analyze_sentiment

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Market Predictor"}

@app.get("/market")
def market():
    sentiment = analyze_sentiment()

    return {
        "signal": "BUY",
        "rsi": 65,
        "macd": "Bullish",
        "sentiment": sentiment
    }