from fastapi import FastAPI
from predictor import predict_market
from signal_engine import generate_signal

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/predict")
def prediction():
    result = predict_market()
    signal = generate_signal(result)
    return {
        "prediction": result,
        "signal": signal
    }