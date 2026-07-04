# LLM Trading Signal Generator

An AI-powered trading signal generator that extracts alpha signals from SEC filings using FinBERT sentiment analysis and backtests against 5 years of market data.

## Features
- FinBERT sentiment analysis on SEC filings
- Real-time market data fetching via yfinance
- BUY/SELL signal generation based on sentiment score
- Backtesting engine with Sharpe ratio calculation
- REST API built with FastAPI

## Tech Stack
- Python 3.10
- FinBERT (ProsusAI/finbert)
- yfinance
- FastAPI
- SEC EDGAR API
- Pandas & NumPy

## Installation
```bash
git clone https://github.com/yourusername/trading-signal.git
cd trading-signal
pip install -r requirements.txt
```

## Setup
Create a `.env` file: