import datetime

import pandas as pd

import ohlc_db
from ohlc_db import deliv_spike, deliv_tag


def _synthetic_delivery_df(baseline_pct: float, today_pct: float, n: int = 20) -> pd.DataFrame:
    dates = pd.date_range("2026-01-01", periods=n + 1, freq="D")
    pcts = [baseline_pct] * n + [today_pct]
    return pd.DataFrame({"date": dates, "deliv_pct": pcts})


def test_deliv_spike_detects_spike_above_baseline():
    df = _synthetic_delivery_df(baseline_pct=20.0, today_pct=40.0)
    assert deliv_spike(df, n=20, mult=1.5) == (40.0, 20.0)


def test_deliv_spike_no_spike_below_multiplier():
    df = _synthetic_delivery_df(baseline_pct=20.0, today_pct=25.0)
    assert deliv_spike(df, n=20, mult=1.5) is None


def test_deliv_spike_excludes_today_from_baseline():
    """Baseline must use the prior n days only -- mutating today's value
    alone must never change the baseline (no look-ahead)."""
    df = _synthetic_delivery_df(baseline_pct=20.0, today_pct=40.0)
    _, baseline_a = deliv_spike(df, n=20, mult=1.5)
    df.loc[df.index[-1], "deliv_pct"] = 90.0
    _, baseline_b = deliv_spike(df, n=20, mult=1.5)
    assert baseline_a == baseline_b == 20.0


def test_deliv_spike_insufficient_rows_returns_none():
    df = _synthetic_delivery_df(baseline_pct=20.0, today_pct=40.0, n=5)
    assert deliv_spike(df, n=20, mult=1.5) is None


def test_deliv_tag_formats_spike(monkeypatch):
    df = _synthetic_delivery_df(baseline_pct=20.0, today_pct=68.0)
    monkeypatch.setattr(ohlc_db, "load_delivery", lambda symbol, lookback=21, db_path=None: df)
    assert deliv_tag("TEST") == "DEL68%(T-1)"


def test_deliv_tag_empty_when_no_spike(monkeypatch):
    df = _synthetic_delivery_df(baseline_pct=20.0, today_pct=22.0)
    monkeypatch.setattr(ohlc_db, "load_delivery", lambda symbol, lookback=21, db_path=None: df)
    assert deliv_tag("TEST") == ""


def test_deliv_tag_no_suffix_when_latest_row_is_today(monkeypatch):
    """When backfill_delivery_markers.py runs same-day right after fetch_delivery.py
    writes today's row, the latest delivery date IS today -- no lag, no (T-1)."""
    n = 20
    dates = pd.date_range(end=datetime.date.today().isoformat(), periods=n + 1, freq="D")
    pcts = [20.0] * n + [68.0]
    df = pd.DataFrame({"date": dates, "deliv_pct": pcts})
    monkeypatch.setattr(ohlc_db, "load_delivery", lambda symbol, lookback=21, db_path=None: df)
    assert deliv_tag("TEST") == "DEL68%"


def test_deliv_tag_empty_when_no_data(monkeypatch):
    monkeypatch.setattr(ohlc_db, "load_delivery", lambda symbol, lookback=21, db_path=None: None)
    assert deliv_tag("TEST") == ""
