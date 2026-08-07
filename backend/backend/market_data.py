import random

def get_market_data():
    return {
        "price": random.randint(24000, 26000),
        "volume": random.randint(100000, 500000)
    }
