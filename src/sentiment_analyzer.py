from transformers import pipeline
from config import Config


class SentimentAnalyzer:

    def __init__(self):
        self.model = pipeline("text-classification",model=Config.FINBERT_MODEL)


    def analyze_batch(self, text:list):
        result= self.model(text)

        return [{"label":r["label"], "score":r["score"]} for r in result]
    


