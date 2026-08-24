import os
import sys

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import rs_weekly_ema9_scanner as m
from rs_weekly_ema9_scanner import weekly_rs_ema9_trend


def _series(n_days: int, start: str, values) -> pd.Series:
    idx = pd.date_range(start, periods=n_days, freq="D")
    return pd.Series(values, index=idx)


def test_rising_rs_gives_positive_slope():
    n = 400
    dates = pd.date_range("2024-01-01", periods=n, freq="D")
    stock = pd.Series([100 + i * 0.5 for i in range(n)], index=dates)  # strong uptrend
    bench = pd.Series([100.0] * n, index=dates)  # flat benchmark
    out = weekly_rs_ema9_trend(stock, bench)
    assert out is not None
    assert out["slope"] > 0
    assert out["rising"] is True
    weekly_rs = (stock.resample("W").last() / bench.resample("W").last()) * 1000
    expected_age = len(weekly_rs.ewm(span=9, adjust=False).mean().diff().dropna())
    assert out["age"] == expected_age


def test_falling_rs_gives_negative_slope():
    n = 400
    dates = pd.date_range("2024-01-01", periods=n, freq="D")
    stock = pd.Series([200 - i * 0.5 for i in range(n)], index=dates)  # downtrend
    bench = pd.Series([100.0] * n, index=dates)
    out = weekly_rs_ema9_trend(stock, bench)
    assert out is not None
    assert out["slope"] < 0
    assert out["rising"] is False
    assert out["age"] == 0


def test_flat_weekly_ema9_has_weekly_age_even_when_daily_rs_is_not_above():
    n = 400
    dates = pd.date_range("2024-01-01", periods=n, freq="D")
    stock = pd.Series([100.0] * n, index=dates)
    bench = pd.Series([100.0] * n, index=dates)

    out = weekly_rs_ema9_trend(stock, bench)

    assert out is not None
    assert out["slope"] == 0.0
    assert out["rising"] is False
    assert out["age"] > 0


def test_analyse_keeps_flat_weekly_ema9_without_daily_rs_above(monkeypatch):
    n = 400
    dates = pd.date_range("2024-01-01", periods=n, freq="D")
    daily = pd.DataFrame({"date": dates, "close": [100.0] * n})
    bench = pd.Series([100.0] * n, index=dates)
    monkeypatch.setattr(m, "load_ohlc", lambda symbol, lookback: daily)
    monkeypatch.setattr(m, "liq_tag", lambda frame: "")

    out = m.analyse("FLATRS", bench)

    assert out is not None
    assert out["rising"] is False
    assert out["age"] > 0


def test_market_cap_range_matches_ema55_scanner():
    assert m.MC_LOW == 1_000 * 1_00_00_000
    assert m.MC_HIGH == 5_00_000 * 1_00_00_000


def test_insufficient_history_returns_none():
    dates = pd.date_range("2024-01-01", periods=20, freq="D")
    stock = pd.Series([100.0] * 20, index=dates)
    bench = pd.Series([100.0] * 20, index=dates)
    assert weekly_rs_ema9_trend(stock, bench) is None


def test_history_upsert_is_idempotent_per_date():
    orig_file = m.HISTORY_FILE
    m.HISTORY_FILE = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "_scratch_history.csv"
    )
    try:
        if os.path.exists(m.HISTORY_FILE):
            os.remove(m.HISTORY_FILE)
        m.update_history("2026-07-10", 500, 500)
        m.update_history("2026-07-11", 520, 30)
        h = m.update_history("2026-07-11", 525, 35)  # re-run same date overwrites, not duplicates
        assert len(h) == 2
        assert int(h[h["date"] == "2026-07-11"]["count"].iloc[0]) == 525
        assert list(h["date"]) == sorted(h["date"])  # sorted ascending
    finally:
        if os.path.exists(m.HISTORY_FILE):
            os.remove(m.HISTORY_FILE)
        m.HISTORY_FILE = orig_file


if __name__ == "__main__":
    test_rising_rs_gives_positive_slope()
    test_falling_rs_gives_negative_slope()
    test_insufficient_history_returns_none()
    test_history_upsert_is_idempotent_per_date()
    print("OK")
