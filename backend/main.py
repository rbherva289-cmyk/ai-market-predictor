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
