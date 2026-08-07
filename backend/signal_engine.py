def generate_signal(value):

    if value > 2:
        return "BUY"

    if value < -2:
        return "SELL"

    return "HOLD"