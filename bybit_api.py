import requests

BASE = "https://api.bybit.com"

def get_tickers():
    url = f"{BASE}/v5/market/tickers?category=linear"
    return requests.get(url).json()["result"]["list"]

def get_oi(symbol):
    url = f"{BASE}/v5/market/open-interest?category=linear&symbol={symbol}&interval=5min"
    data = requests.get(url).json()
    return data["result"]["list"]

def get_kline(symbol):
    url = f"{BASE}/v5/market/kline?category=linear&symbol={symbol}&interval=240&limit=50"
    data = requests.get(url).json()
    return data["result"]["list"]
