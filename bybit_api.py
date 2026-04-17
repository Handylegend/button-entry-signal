import requests

BASE_URL = "https://api.bybit.com"


def get_tickers():
    url = f"{BASE_URL}/v5/market/tickers?category=linear"
    res = requests.get(url, timeout=10)
    return res.json()["result"]["list"]


def get_kline(symbol, limit=50):
    url = f"{BASE_URL}/v5/market/kline"
    params = {
        "category": "linear",
        "symbol": symbol,
        "interval": "240",
        "limit": limit
    }
    res = requests.get(url, params=params, timeout=10)
    return res.json()["result"]["list"]


def get_open_interest(symbol):
    url = f"{BASE_URL}/v5/market/open-interest"
    params = {
        "category": "linear",
        "symbol": symbol,
        "interval": "5min",
        "limit": 50
    }
    res = requests.get(url, params=params, timeout=10)
    return res.json()["result"]["list"]
