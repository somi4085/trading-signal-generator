from sentiment_analyzer import SentimentAnalyzer
from data_fetcher import MarketDataFetcher
from sec_fetcher import SECFetcher
from config import Config


class SignalGenerator:

    def __init__(self):
        self.sentiment = SentimentAnalyzer()
        self.market = MarketDataFetcher()
        self.sec = SECFetcher()

    def generator_signal(self, ticker:str):
        stock_data = self.market.get_stock_data(ticker)
        filings = self.sec.get_filling(ticker)
        text = self.sec.extract_text(filings)
        sentiment = self.sentiment.analyze_batch([text])[0]
        if sentiment["score"] > Config.SIGNAL_THRESHOLD:
            return "BUY"
        else:
            return "SELL"

