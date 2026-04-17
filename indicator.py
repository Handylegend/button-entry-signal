import pandas as pd
import ta

def calc_indicators(kline):
    df = pd.DataFrame(kline, columns=[
        "time","open","high","low","close","volume","turnover"
    ])

    df["close"] = df["close"].astype(float)

    rsi = ta.momentum.RSIIndicator(df["close"]).rsi().iloc[-1]

    return {
        "rsi": rsi
    }
