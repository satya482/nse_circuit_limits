#!/usr/bin/env python3
"""
NSE Z-Score Mean Reversion Scanner (oversold / long-bounce candidates)
Flags stocks trading 3+ standard deviations below their 55-bar mean close.

Formula mirrors pine_scripts/Satya Z-Score Probability Indicator.txt
(lookback changed from Pine default 75 to 55, per Python<->Pine parity convention):
    z = (close - SMA(close, 55)) / STDEV(close, 55)

Data source: .ohlc_data/market.db  (populated by fetch_data.py)
Output:      zscore_scans/zscore_meanreversion_scans.md
"""

import pandas as pd


ZSCORE_LEN = 55
Z_THRESHOLD = -3.0
ZONE_CAP = 60  # bars to scan back for zone-age before giving up


def zscore(close: pd.Series, len: int = ZSCORE_LEN) -> pd.Series:
    sma = close.rolling(len, min_periods=len).mean()
    sd = close.rolling(len, min_periods=len).std()
    return (close - sma) / sd


def zscore_zone_days(
    z: pd.Series, threshold: float = Z_THRESHOLD, cap: int = ZONE_CAP
) -> tuple[int, bool]:
    """Consecutive trailing bars with z <= threshold (capped), and whether z has
    risen for the last 3 bars (early reversion tell, mirrors ta.rising(z_sma, 3))."""
    n = len(z)
    if n == 0 or pd.isna(z.iloc[-1]) or z.iloc[-1] > threshold:
        return 0, False
    days = 0
    limit = max(0, n - cap)
    for i in range(n - 1, limit - 1, -1):
        if pd.isna(z.iloc[i]) or z.iloc[i] > threshold:
            break
        days += 1
    turning_up = bool(n >= 3 and z.iloc[-1] > z.iloc[-2] > z.iloc[-3])
    return days, turning_up


if __name__ == "__main__":
    # smoke self-check (ponytail: minimum viable test, real coverage is in tests/)
    s = pd.Series([100.0] * 55 + [80.0])
    z = zscore(s)
    assert not pd.isna(z.iloc[-1])
    days, turning_up = zscore_zone_days(pd.Series([-1.0, -3.5, -3.2, -3.1]))
    assert days == 3 and turning_up is True
    print("zscore_meanreversion_scanner self-check OK")
