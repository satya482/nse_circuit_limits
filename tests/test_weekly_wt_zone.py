"""
tests/test_weekly_wt_zone.py
Unit tests for weekly_wt_zone() in wavetrend_scanner.py.
"""

import sys
from pathlib import Path
from datetime import date, timedelta

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent))
from wavetrend_scanner import weekly_wt_zone


def _make_df(prices: list | np.ndarray, start: str = "2020-01-02") -> pd.DataFrame:
    """Synthetic daily OHLCV (weekdays only) from a close-price list."""
    n = len(prices)
    dates = []
    d = date.fromisoformat(start)
    for _ in range(n):
        while d.weekday() >= 5:
            d += timedelta(days=1)
        dates.append(d.isoformat())
        d += timedelta(days=1)
    c = np.asarray(prices, dtype=float)
    return pd.DataFrame(
        {
            "date": dates,
            "open": c * 0.99,
            "high": c * 1.01,
            "low": c * 0.98,
            "close": c,
            "volume": np.ones(n) * 1_000_000,
        }
    )


def _bull_then_hold(n_decline=300, n_rise=150) -> np.ndarray:
    """Steep decline → reversal → hold. Noise ensures real wt1/wt2 divergence."""
    rng = np.random.default_rng(42)
    trend = np.concatenate(
        [
            np.linspace(100, 30, n_decline),
            np.linspace(30, 90, n_rise),
        ]
    )
    noise = rng.normal(0, 2.0, len(trend))
    return np.clip(trend + noise, 1.0, None)


def _bull_then_bear(n_decline=300, n_rise=100, n_decline2=120) -> np.ndarray:
    """Steep decline → reversal → second decline. Bull cross then bear cross."""
    rng = np.random.default_rng(42)
    trend = np.concatenate(
        [
            np.linspace(100, 30, n_decline),
            np.linspace(30, 90, n_rise),
            np.linspace(90, 20, n_decline2),
        ]
    )
    noise = rng.normal(0, 2.0, len(trend))
    return np.clip(trend + noise, 1.0, None)


def test_in_zone_returns_true_with_positive_days():
    """Bull cross with no subsequent bear cross → (True, N>0)."""
    df = _make_df(_bull_then_hold())
    in_zone, days = weekly_wt_zone(df)
    assert in_zone is True
    assert days > 0
    assert days <= 200  # rise portion is 150 bars + EMA lag buffer


def test_bear_cross_after_bull_ends_zone():
    """Bull cross followed by bear cross → (False, 0)."""
    df = _make_df(_bull_then_bear())
    in_zone, days = weekly_wt_zone(df)
    assert in_zone is False
    assert days == 0


def test_no_cross_returns_false():
    """Steep monotone decline — no bull cross ever → (False, 0)."""
    prices = np.linspace(
        100, 10, 400
    )  # pure decline, no noise → wt1 never crosses above wt2
    df = _make_df(prices)
    in_zone, days = weekly_wt_zone(df)
    assert in_zone is False
    assert days == 0


def test_insufficient_data_returns_false():
    """Too few bars to compute weekly WT → (False, 0)."""
    prices = np.linspace(100, 50, 50)  # < 175 daily bars needed
    df = _make_df(prices)
    in_zone, days = weekly_wt_zone(df)
    assert in_zone is False
    assert days == 0


def test_days_count_is_nonnegative_integer():
    """days is always a non-negative int."""
    df = _make_df(_bull_then_hold())
    in_zone, days = weekly_wt_zone(df)
    assert isinstance(days, int)
    assert days >= 0
