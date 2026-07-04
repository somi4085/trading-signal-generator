import yfinance as yf
import pandas as pd
from datetime import datetime
from config import Config

class MarketDataFetcher:

    def __init__(self):
        self.years = Config.MARKET_DATA_YEARS

    def get_stock_data(self, ticker: str):
        start_date = datetime.now() - pd.DateOffset(years=self.years)
        data = yf.download(ticker, start=start_date, progress=False, auto_adjust=True)
        return data
    
