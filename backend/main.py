from fastapi import FastAPI
from market_data import get_market_data
from sentiment import analyze_sentiment
from ai_model import predict
from logger import log_message
from security import check_api_key