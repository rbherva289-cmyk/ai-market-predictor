from textblob import TextBlob

def analyze(text):
    score = TextBlob(text).sentiment.polarity

    if score > 0:
        return "positive"

    if score < 0:
        return "negative"

    return "neutral"