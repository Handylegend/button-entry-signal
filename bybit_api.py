import requests
import time

BASE_URL = "https://api.bybit.com"


def safe_request(url, params=None, retries=3):
    for i in range(retries):
        try:
            res = requests.get(url, params=params, timeout=10)

            # 状态码检查
            if res.status_code != 200:
                time.sleep(1)
                continue

            # 尝试解析JSON
            data = res.json()

            # Bybit接口成功标志
            if data.get("retCode") != 0:
                time.sleep(1)
                continue

            return data["result"]

        except Exception as e:
            time.sleep(1)

    return None


def get_tickers():
    url = f"{BASE_URL}/v5/market/tickers"
    params = {"category": "linear"}

    result = safe_request(url, params)
    return result["list"] if result else []


def get_kline(symbol, limit=50):
    url = f"{BASE_URL}/v5/market/kline"
    params = {
        "category": "linear",
        "symbol": symbol,
        "interval": "240",
        "limit": limit
    }

    result = safe_request(url, params)
    return result["list"] if result else []


def get_open_interest(symbol):
    url = f"{BASE_URL}/v5/market/open-interest"
    params = {
        "category": "linear",
        "symbol": symbol,
        "interval": "5min",
        "limit": 50
    }

    result = safe_request(url, params)
    return result["list"] if result else []
