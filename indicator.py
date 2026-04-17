import pandas as pd


def calculate_rsi(close_prices, period=14):
    series = pd.Series(close_prices)

    delta = series.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi.iloc[-1]


def parse_kline(kline):
    df = pd.DataFrame(kline, columns=[
        "time", "open", "high", "low", "close", "volume", "turnover"
    ])

    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)

    return df


def get_indicators(kline):
    df = parse_kline(kline)

    rsi = calculate_rsi(df["close"])

    # 成交量变化（最近 vs 前一根）
    vol_now = df["volume"].iloc[-1]
    vol_prev = df["volume"].iloc[-2]
    vol_change = (vol_now - vol_prev) / vol_prev * 100 if vol_prev != 0 else 0

    return {
        "rsi": rsi,
        "volume_change": vol_change
    }
