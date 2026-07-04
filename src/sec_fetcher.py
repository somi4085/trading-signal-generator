import requests
from config import Config


class SECFetcher:

    def __init__(self):
        self.base_url = "https://data.sec.gov/api/xbrl/companyfacts/"
        self.headers = {"User-Agent":"somisingh@gmail.com"}
        self.ticker_to_cik = {
            "AAPL": "0000320193",
            "MSFT": "0000789019",
            "GOOGL": "0001652044",
            "AMZN": "0001018724"
        }
        

    def get_filling(self, ticker:str):
        url = self.base_url + "CIK" + self.ticker_to_cik.get(ticker, ticker) + ".json"
        response = requests.get(url, headers=self.headers)
        print("Status:", response.status_code)
        print("URL:", url)
        if response.status_code == 200:
            return response.json()
        return {}

    
    def extract_text(self,filling:dict):

        return filling.get("text","")
    
    