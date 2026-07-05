# tests/test_consolidation_scanner.py
import os
import pandas as pd
import pytest

from consolidation import consolidation_scanner as cs


def _consolidating_df(n: int = 300) -> pd.DataFrame:
    """A genuine volatility CONTRACTION: wider noise (std=0.5) for all but the
    trailing 100 bars, then tight noise (std=0.03) for the trailing 100 --
    passes both the EMA dual gate and the BB squeeze gate.

    A uniform (homoskedastic) noise series was tried first and does NOT
    reliably pass the squeeze gate: bb_width_percentile is a rank among the
    trailing 252 bars, and with constant-variance noise there is no trend for
    today's bar to rank low against -- it lands wherever i.i.d. sampling
    happens to put it (verified: this produced bb_width_percentile ~60, gate
    fails). Only an actual narrowing of realized volatility over time gives a
    low, reliably-low percentile at the tail."""
    import numpy as np
    rng = np.random.default_rng(42)
    early_n = max(0, n - 100)
    tight_n = n - early_n
    noise = np.concatenate([rng.normal(0, 0.5, early_n), rng.normal(0, 0.03, tight_n)])
    close = [100.0 + x for x in noise]
    return pd.DataFrame({
        "date": pd.date_range("2023-06-01", periods=n, freq="B"),
        "open": close, "high": [c + 0.05 for c in close],
        "low": [c - 0.05 for c in close], "close": close,
        "volume": [1_000_000.0] * n,
    })


def _bench_df(n: int = 300) -> pd.DataFrame:
    return pd.DataFrame({
        "date": pd.date_range("2023-06-01", periods=n, freq="B"),
        "open": [100.0] * n, "high": [100.0] * n,
        "low": [100.0] * n, "close": [100.0] * n,
        "volume": [1_000_000.0] * n,
    })


def test_analyse_returns_none_below_minimum_history():
    short_df = _consolidating_df(50)
    result = cs.analyse("TEST", short_df, _bench_df(50))
    assert result is None


def test_analyse_returns_none_without_benchmark():
    result = cs.analyse("TEST", _consolidating_df(), None)
    assert result is None


def test_analyse_returns_expected_columns_on_qualifying_stock(monkeypatch):
    import ohlc_db
    monkeypatch.setattr(ohlc_db, "load_delivery", lambda symbol, lookback=120, db_path=None: None)
    monkeypatch.setattr(ohlc_db, "deliv_spike", lambda df, n=20, mult=1.5: None)
    result = cs.analyse("TEST", _consolidating_df(), _bench_df())
    assert result is not None
    assert set(result.keys()) == set(cs.COLUMNS)
    assert result["tier"] in ("NONE", "TIER_1_HOT", "TIER_2_WARM", "TIER_3_COLD")


def test_find_previous_csv_returns_most_recent_before_as_of(tmp_path, monkeypatch):
    monkeypatch.setattr(cs, "RESULTS_DIR", str(tmp_path))
    (tmp_path / "2026-07-01-consolidation.csv").write_text("symbol,tier\nAAA,TIER_1_HOT\n")
    (tmp_path / "2026-07-03-consolidation.csv").write_text("symbol,tier\nAAA,TIER_2_WARM\n")
    result = cs.find_previous_csv("2026-07-05")
    assert result.endswith("2026-07-03-consolidation.csv")


def test_find_previous_csv_none_when_directory_empty(tmp_path, monkeypatch):
    monkeypatch.setattr(cs, "RESULTS_DIR", str(tmp_path))
    assert cs.find_previous_csv("2026-07-05") is None


def test_compute_transitions_flags_promotion_and_abandonment(tmp_path, monkeypatch):
    monkeypatch.setattr(cs, "RESULTS_DIR", str(tmp_path))
    (tmp_path / "2026-07-03-consolidation.csv").write_text(
        "symbol,tier\nAAA,TIER_3_COLD\nBBB,TIER_2_WARM\n"
    )
    rows = [{"symbol": "AAA", "tier": "TIER_1_HOT"}]
    transitions = cs.compute_transitions(rows, "2026-07-05")
    assert "AAA" in transitions["promoted"]
    assert "BBB" in transitions["abandoned"]


def test_build_markdown_no_signals_writes_placeholder_not_empty():
    md = cs.build_markdown([], "2026-07-05", {"promoted": [], "demoted": [], "abandoned": []})
    assert "No signals" in md
    assert "SEBI registered" in md
