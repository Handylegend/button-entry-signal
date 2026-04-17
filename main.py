from bybit_api import *
from indicator import *
from discord_bot import send_message
from datetime import datetime
import time

def calculate_oi_change(oi_list):
    if len(oi_list) < 2:
        return 0

    try:
        oi_now = float(oi_list[0]["openInterest"])
        oi_prev = float(oi_list[-1]["openInterest"])

        if oi_prev == 0:
            return 0

        return (oi_now - oi_prev) / oi_prev * 100
    except:
        return 0


def analyze():
    tickers = get_tickers()
    signals = []

    for t in tickers:
        time.sleep(0.3)
        try:
            symbol = t["symbol"]

            volume_24h = float(t["turnover24h"])
            price_change = float(t["price24hPcnt"]) * 100

            # 基础筛选
            if volume_24h < 1_000_000 or price_change < 5:
                continue

            kline = get_kline(symbol)
            if not kline or len(kline) < 20:
                continue
            indicators = get_indicators(kline)

            oi_data = get_open_interest(symbol)
            if not oi_data or len(oi_data) < 2:
                continue
            oi_change = calculate_oi_change(oi_data)

            score = 0

            if price_change >= 5:
                score += 2

            if oi_change > 0:
                score += 3

            if indicators["volume_change"] > 5:
                score += 1

            if indicators["rsi"] > 50:
                score += 1

            if score >= 4:
                signals.append(
                    f"{symbol} | 涨:{price_change:.2f}% | OI:{oi_change:.2f}% | RSI:{indicators['rsi']:.1f} | Score:{score}"
                )

        except Exception as e:
            continue

    return signals


if __name__ == "__main__":
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    signals = analyze()

    if signals:
        msg = f"🚀 信号更新 ({now})\n" + "\n".join(signals)
    else:
        msg = f"😴 无信号 ({now})"

    send_message(msg)
