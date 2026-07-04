import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    FINBERT_MODEL = "ProsusAI/finbert"
    MARKET_DATA_YEARS = 5
    SECTORS = ["Technology","Finance","Healthcare"]
    SIGNAL_THRESHOLD = 0.7

