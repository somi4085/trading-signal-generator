import sys
sys.path.append("src")

from fastapi import FastAPI
from signal_generator import SignalGenerator
from backtester import Backtester

app = FastAPI()

signal_generator = SignalGenerator()

@app.get("/signal/{ticker}")
def get_signal(ticker:str):
    signal = signal_generator.generator_signal(ticker)
    return {"ticker":ticker, "signal":signal}

@app.get("/backtest/{ticker}")
def get_backtest(ticker:str):
    backtester = Backtester(ticker)
    signal = signal_generator.generator_signal(ticker)
    results = backtester.run([signal])
    return results
