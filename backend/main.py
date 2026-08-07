from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Market Predictor")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "AI Market Predictor Running"
    }


@app.get("/predict")
def predict():
    return {
        "symbol": "NIFTY",
        "signal": "BUY",
        "confidence": "87%"
    }
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