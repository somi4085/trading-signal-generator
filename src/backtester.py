import pandas as pd
import os
import numpy as np
from data_fetcher import MarketDataFetcher


class Backtester:

    def __init__(self, ticker:str):
        self.ticker = ticker
        self.data_fetcher = MarketDataFetcher()

    
    def run(self, signal:list):
        stock_data = self.data_fetcher.get_stock_data(self.ticker)
        stock_data["Signal"] = signal
        stock_data["Returns"] = stock_data["Close"].pct_change()
        stock_data["Strategy_Returns"] = stock_data["Returns"] * stock_data["Signal"]
        total_return = stock_data["Strategy_Returns"].sum()
        sharpe = stock_data["Strategy_Returns"].mean() / stock_data["Strategy_Returns"].std()

        return {
            "total_return": round(float(total_return), 4) if not pd.isna(total_return) else 0.0,
            "sharpe_ratio": round(float(sharpe), 4) if not pd.isna(sharpe) else 0.0
        }
    
