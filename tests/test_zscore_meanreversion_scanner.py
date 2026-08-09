import statistics

import pandas as pd
from zscore_meanreversion_scanner import zscore, zscore_zone_days


def test_zscore_matches_pine_formula():
    # 55 flat bars at 100, then a sharp drop that should read close to a real z-score.
    closes = [100.0] * 55 + [80.0]
    s = pd.Series(closes)
    z = zscore(s, len=55)
    # Independent calculation: last 55 closes, population stdev (ddof=0, matching Pine)
    window = closes[-55:]
    sma = sum(window) / len(window)
    sd = statistics.pstdev(window)
    expected = (80.0 - sma) / sd
    assert abs(z.iloc[-1] - expected) < 1e-9
    assert pd.isna(z.iloc[53])  # not enough bars yet (need 55)


def test_zscore_zone_days_counts_consecutive_extreme_bars():
    # z-series: 3 bars at z=-3.5 (extreme), then not extreme before that
    z = pd.Series([-1.0, -1.0, -3.5, -3.2, -3.1])
    days, turning_up = zscore_zone_days(z, threshold=-3.0, cap=60)
    assert days == 3
    # -3.5 -> -3.2 -> -3.1 is rising each bar
    assert turning_up is True


def test_zscore_zone_days_not_turning_up_when_still_falling():
    z = pd.Series([-1.0, -3.0, -3.5, -4.0])
    days, turning_up = zscore_zone_days(z, threshold=-3.0, cap=60)
    assert days == 3
    assert turning_up is False


def test_zscore_zone_days_zero_when_not_currently_extreme():
    z = pd.Series([-3.5, -3.2, -1.0])
    days, turning_up = zscore_zone_days(z, threshold=-3.0, cap=60)
    assert days == 0
    assert turning_up is False


def test_analyse_returns_none_for_insufficient_history(monkeypatch):
    import zscore_meanreversion_scanner as mod

    monkeypatch.setattr(mod, "load_ohlc", lambda symbol: pd.DataFrame({
        "date": ["2026-01-01"] * 10,
        "open": [100.0] * 10, "high": [100.0] * 10,
        "low": [100.0] * 10, "close": [100.0] * 10,
        "volume": [1000] * 10,
    }))
    assert mod.analyse("FOO") is None


def test_analyse_returns_none_when_not_oversold(monkeypatch):
    import zscore_meanreversion_scanner as mod

    flat = pd.DataFrame({
        "date": [f"2026-01-{i:02d}" for i in range(1, 61)],
        "open": [100.0] * 60, "high": [101.0] * 60,
        "low": [99.0] * 60, "close": [100.0] * 60,
        "volume": [100000] * 60,
    })
    monkeypatch.setattr(mod, "load_ohlc", lambda symbol: flat)
    monkeypatch.setattr(mod, "passes_hard_gate", lambda m: True)
    assert mod.analyse("FOO") is None  # flat series -> z is nan/0, never <= -3


def test_analyse_returns_dict_when_oversold(monkeypatch):
    import zscore_meanreversion_scanner as mod

    closes = [100.0] * 55 + [50.0, 51.0, 52.0, 53.0, 54.0]
    df = pd.DataFrame({
        "date": [f"2026-01-{i:02d}" for i in range(1, len(closes) + 1)],
        "open": closes, "high": [c + 1 for c in closes],
        "low": [c - 1 for c in closes], "close": closes,
        "volume": [100000] * len(closes),
    })
    monkeypatch.setattr(mod, "load_ohlc", lambda symbol: df)
    monkeypatch.setattr(mod, "passes_hard_gate", lambda m: True)
    monkeypatch.setattr(mod, "trap_label", lambda m: "n/a")
    monkeypatch.setattr(mod, "liq_tag", lambda df: "")
    monkeypatch.setattr(mod, "cmf_tag", lambda df: "")
    monkeypatch.setattr(mod, "deliv_tag", lambda sym: "")

    result = mod.analyse("FOO")
    assert result is not None
    assert result["symbol"] == "FOO"
    assert result["z"] <= mod.Z_THRESHOLD
    assert result["close"] == 54.0
    assert "dist_pct" in result and "zone_days" in result and "turning_up" in result
