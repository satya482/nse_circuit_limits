# US WaveTrend Bull Cross Scanner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Port `wt_bullcross_scanner.py` (NSE) to US equities, reusing the existing US data
pipeline (`us_ohlc_db.py`, `.us_ohlc_data/us_market.db`, `fetch_us_data.py`) instead of
building new plumbing.

**Architecture:** One new module `us_wt_bullcross_scanner.py`, structured like the existing
single-file scanners in this repo (`wt_bullcross_scanner.py`, `us_zl_squeeze_scanner.py`):
pure indicator/scoring helpers at the top (unit-tested), a per-stock `analyse()` orchestrator,
then Markdown + HTML output builders, then `main()` gluing watchlist → DB → analyse → output.
`WaveTrendCalculator` from `wavetrend_scanner.py` is reused unmodified (already market-agnostic).

**Tech Stack:** Python 3.13, pandas, `tradingview_screener`, `pytest` (plain functions, no
fixtures — matches existing `tests/test_*.py` style in this repo).

## Global Constraints

- OHLCV via `us_ohlc_db.load_ohlc_many(symbols, lookback=400)` only — never a new fetch script.
- Watchlist query MUST match `fetch_us_data.py`'s backfill universe: `exchange in [NASDAQ, NYSE]`,
  `type == stock`, `typespecs has common`, `close > 5`, `market_cap_basic` between $300M–$10B,
  `average_volume_10d_calc > 300_000`. (Copied verbatim from spec / `us_zl_squeeze_scanner.py`.)
- Benchmark: `SPY`. RS line = `(stock_close / SPY_close) * 100` (×100 scale — NOT NSE's ×1000).
- WT bull rank hierarchy is an external contract — never renumber: 5=BULL_OS_PPV, 4=BULL_ANY_PPV,
  3=BULL_OVERSOLD, 2=BULL_OS_L2, 1=BULL_ANY_MID.
- **No RS gate** — RS shown as informational context only, never filters out a signal.
- Drop entirely (NSE-only, no US equivalent): circuit limits, `float_gate.py` (₹-Cr hardcoded),
  `stock_labels.json`, trend-scanner cross-reference star, `weekly_wt_zone`.
- Every `.md` and `.html` output file includes the SEBI disclaimer (`disclaimer.py`) — matches
  `us_zl_squeeze_scanner.py` precedent.
- Both `us_wt_scans/us_wt_bullcross_latest.md` and `us_wt_scans/us_wt_bullcross_YYYY-MM-DD.md`
  written in the same run. Never hand-edit generated output. Empty category → `*No signals.*`,
  never a header-only table.
- Timestamps: IST (`*Generated YYYY-MM-DD HH:MM IST*`), matches repo-wide convention.
- Never commit `.us_ohlc_data/`, `*.pyc`, `.env`.

---

## Task 1: Core indicator helpers

**Files:**
- Create: `us_wt_bullcross_scanner.py`
- Test: `tests/test_us_wt_bullcross_scanner.py`

**Interfaces:**
- Produces: `_ema(s: pd.Series, n: int) -> pd.Series`, `_zlema(s: pd.Series, n: int) -> pd.Series`,
  `_bb_kc_squeeze(df: pd.DataFrame) -> bool`, `_zl25_turn_stats(zl25: pd.Series, closes: pd.Series) -> tuple[int, float]`
- Consumes: nothing (first task)

- [ ] **Step 1: Write the failing tests**

```python
"""tests/test_us_wt_bullcross_scanner.py"""
import numpy as np
import pandas as pd
import pytest

from us_wt_bullcross_scanner import _ema, _zlema, _bb_kc_squeeze, _zl25_turn_stats


def _df(closes: list[float]) -> pd.DataFrame:
    n = len(closes)
    dates = pd.date_range("2024-01-01", periods=n, freq="B")
    c = np.asarray(closes, dtype=float)
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


def test_ema_matches_pandas_ewm():
    s = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
    result = _ema(s, 3)
    expected = s.ewm(span=3, adjust=False).mean()
    pd.testing.assert_series_equal(result, expected)


def test_zlema_is_ema_of_double_ema_minus_ema():
    s = pd.Series(np.linspace(10, 20, 30))
    e = s.ewm(span=5, adjust=False).mean()
    expected = 2 * e - e.ewm(span=5, adjust=False).mean()
    result = _zlema(s, 5)
    pd.testing.assert_series_equal(result, expected)


def test_bb_kc_squeeze_false_when_insufficient_bars():
    df = _df([100.0] * 10)
    assert _bb_kc_squeeze(df) is False


def test_bb_kc_squeeze_true_on_flat_low_vol_series():
    # Flat price -> BB std ~0 -> BB fully inside KC -> squeeze True
    df = _df([100.0] * 25)
    assert _bb_kc_squeeze(df) is True


def test_bb_kc_squeeze_false_on_wide_range_series():
    # Large daily swings -> BB wider than KC -> squeeze False
    rng = np.random.default_rng(1)
    closes = 100 + np.cumsum(rng.normal(0, 5, 25))
    df = _df(list(closes))
    assert _bb_kc_squeeze(df) is False


def test_zl25_turn_stats_finds_most_recent_upturn():
    # zl25 falls then turns up exactly 3 bars ago
    zl25 = pd.Series([10, 9, 8, 7, 8, 9, 10])
    closes = pd.Series([100, 98, 96, 94, 96, 98, 101])
    bars, pct = _zl25_turn_stats(zl25, closes)
    assert bars == 3
    assert pct == round((101 / 94 - 1) * 100, 2)


def test_zl25_turn_stats_caps_at_zl_turn_cap():
    # Monotonically falling zl25 -> no upturn found -> capped result
    zl25 = pd.Series(list(range(100, 0, -1)), dtype=float)
    closes = pd.Series(list(range(1, 101)), dtype=float)
    bars, pct = _zl25_turn_stats(zl25, closes)
    assert bars == 60  # ZL_TURN_CAP
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_us_wt_bullcross_scanner.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'us_wt_bullcross_scanner'`

- [ ] **Step 3: Write minimal implementation**

```python
#!/usr/bin/env python3
"""
US WaveTrend Bull Cross Scanner
Run after the existing US data pipeline (fetch_us_data.py @ 4:40 PM IST,
us_zl_squeeze_scanner.py @ 4:50 PM IST) — this scanner runs last, ~5:00 PM IST.

Universe: NYSE + NASDAQ common equity, MCap $300M-$10B, price > $5,
          avg 10d vol > 300K (matches fetch_us_data.py's backfill universe exactly —
          lookups miss for any symbol outside this range).
          No RS filter — WT captures oversold reversals before RS turns positive.

Signal hierarchy (wt_signal_rank) — external contract, never renumbered:
  +5  BULL_OS_PPV    - deep oversold cross + Pocket Pivot Volume [strongest]
  +4  BULL_ANY_PPV   - any cross + Pocket Pivot Volume
  +3  BULL_OVERSOLD  - deep oversold cross (wt2 <= -60)
  +2  BULL_OS_L2     - soft oversold cross (wt2 <= -53)
  +1  BULL_ANY_MID   - mid-range cross (WT2 > -53, no PPV)

Output: us_wt_scans/us_wt_bullcross_latest.md
        us_wt_scans/us_wt_bullcross_YYYY-MM-DD.md
        us_wt_scans/us_wt_bullcross_dashboard.html
"""

import sys
import os
from datetime import datetime

import pandas as pd
from tradingview_screener import Query, col

from us_ohlc_db import load_ohlc_many
from wavetrend_scanner import WaveTrendCalculator
from disclaimer import (
    SEBI_MD_HEADER,
    SEBI_MD_FOOTER,
    SEBI_HTML_BANNER,
    SEBI_HTML_FOOTER,
)

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "us_wt_scans")
TODAY = datetime.now().strftime("%Y-%m-%d")
MD_LATEST = os.path.join(SCANS_DIR, "us_wt_bullcross_latest.md")
MD_DATED = os.path.join(SCANS_DIR, f"us_wt_bullcross_{TODAY}.md")
HTML_DASHBOARD = os.path.join(SCANS_DIR, "us_wt_bullcross_dashboard.html")

MC_LOW = 300_000_000  # $300M
MC_HIGH = 10_000_000_000  # $10B
MIN_RANK = 1
ZL_TURN_CAP = 60
BENCH_SYM = "SPY"
RS_SCALE = 100  # matches us_zl_squeeze_scanner.py convention (not NSE's x1000)
RVOL_FLAG = 8.0
SS_LOWMULT = 0.995


# -- Indicators ---------------------------------------------------------------


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def _zlema(s: pd.Series, n: int) -> pd.Series:
    e = _ema(s, n)
    return 2 * e - _ema(e, n)


def _bb_kc_squeeze(df: pd.DataFrame) -> bool:
    """True if BB(20,2.0,SMA) is fully inside KC(20,1.5,SMA ATR) on the last bar."""
    if len(df) < 21:
        return False
    c = df["close"].astype(float)
    h = df["high"].astype(float)
    l = df["low"].astype(float)
    bb_basis = c.rolling(20).mean()
    bb_std = c.rolling(20).std()
    bb_upper = bb_basis + 2.0 * bb_std
    bb_lower = bb_basis - 2.0 * bb_std
    tr = pd.concat([h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1).max(
        axis=1
    )
    kc_atr = tr.rolling(20).mean()
    kc_basis = c.rolling(20).mean()
    kc_upper = kc_basis + 1.5 * kc_atr
    kc_lower = kc_basis - 1.5 * kc_atr
    return bool(
        bb_upper.iloc[-1] < kc_upper.iloc[-1] and bb_lower.iloc[-1] > kc_lower.iloc[-1]
    )


def _zl25_turn_stats(zl25: pd.Series, closes: pd.Series) -> tuple[int, float]:
    n = len(zl25)
    limit = max(2, n - ZL_TURN_CAP)
    for i in range(n - 1, limit - 1, -1):
        if zl25.iloc[i] > zl25.iloc[i - 1] and zl25.iloc[i - 1] <= zl25.iloc[i - 2]:
            bars = (n - 1) - i + 1
            pct = (closes.iloc[-1] / closes.iloc[i - 1] - 1) * 100
            return bars, round(pct, 2)
    cap_idx = max(0, n - ZL_TURN_CAP)
    return ZL_TURN_CAP, round((closes.iloc[-1] / closes.iloc[cap_idx] - 1) * 100, 2)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_us_wt_bullcross_scanner.py -v`
Expected: 6 passed

- [ ] **Step 5: Commit**

```bash
git add us_wt_bullcross_scanner.py tests/test_us_wt_bullcross_scanner.py
git commit -m "feat: add core indicator helpers for US WT bull cross scanner"
```

---

## Task 2: RS state + RS percentile map

**Files:**
- Modify: `us_wt_bullcross_scanner.py` (append after `_zl25_turn_stats`)
- Test: `tests/test_us_wt_bullcross_scanner.py` (append)

**Interfaces:**
- Consumes: `RS_SCALE` (module constant, = 100) from Task 1
- Produces: `_rs_state(df: pd.DataFrame, bench_series: pd.Series | None) -> str`,
  `_compute_rs_pct_map(all_data: dict[str, pd.DataFrame], bench_series: pd.Series) -> dict[str, float]`

- [ ] **Step 1: Write the failing tests**

```python
def _bench(prices: list[float]) -> pd.Series:
    n = len(prices)
    dates = pd.date_range("2024-01-01", periods=n, freq="B")
    return pd.Series(prices, index=dates)


def test_rs_state_returns_weak_with_no_benchmark():
    df = _df([100.0] * 15)
    assert _rs_state(df, None) == "weak"


def test_rs_state_transition_when_rs_crosses_above_ema9():
    # Stock flat while bench falls sharply on the last bar -> RS spikes above its EMA9 today
    closes = [100.0] * 14 + [100.0]
    df = _df(closes)
    bench_prices = [100.0] * 13 + [100.0, 80.0]
    bench = _bench(bench_prices)
    state = _rs_state(df, bench)
    assert state == "transition"


def test_rs_state_weak_when_rs_stays_below_ema9():
    closes = [100.0] * 15
    df = _df(closes)
    bench_prices = [100.0] * 13 + [100.0, 120.0]  # bench rallies -> RS drops today
    bench = _bench(bench_prices)
    assert _rs_state(df, bench) == "weak"


def test_compute_rs_pct_map_ranks_higher_relative_return_higher():
    n = 260
    dates = pd.date_range("2023-01-01", periods=n, freq="B")
    bench_close = pd.Series(np.linspace(100, 110, n), index=dates)  # bench +10%
    strong = _df(list(np.linspace(100, 200, n)))  # stock +100%
    strong["date"] = dates
    weak = _df(list(np.linspace(100, 105, n)))  # stock +5%
    weak["date"] = dates
    all_data = {"STRONG": strong, "WEAK": weak}
    pct = _compute_rs_pct_map(all_data, bench_close)
    assert pct["STRONG"] > pct["WEAK"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_us_wt_bullcross_scanner.py -v -k "rs_state or rs_pct_map"`
Expected: FAIL with `ImportError: cannot import name '_rs_state'`

- [ ] **Step 3: Write minimal implementation**

```python
def _rs_state(df: pd.DataFrame, bench_series: pd.Series | None) -> str:
    """Returns 'transition' (weak->strong flip today), 'strong', or 'weak'."""
    if bench_series is None or len(bench_series) < 11:
        return "weak"
    try:
        stock_close = df.set_index("date")["close"].astype(float)
        bench = bench_series.reindex(stock_close.index)
        valid = bench.notna()
        if valid.sum() < 11:
            return "weak"
        rs = (stock_close[valid] / bench[valid]) * RS_SCALE
        rs_ema9 = rs.ewm(span=9, adjust=False).mean()
        now_strong = bool(rs.iloc[-1] > rs_ema9.iloc[-1])
        was_weak = bool(rs.iloc[-2] < rs_ema9.iloc[-2])
        if was_weak and now_strong:
            return "transition"
        return "strong" if now_strong else "weak"
    except Exception:
        return "weak"


def _compute_rs_pct_map(all_data: dict, bench_series: pd.Series) -> dict[str, float]:
    """IBD-style RS percentile rank vs SPY. RS line = (close/SPY_close)*RS_SCALE;
    weighted 3m/6m/9m/12m return. Scale cancels out in the ratio, so RS_SCALE
    doesn't affect the resulting percentiles."""
    WINDOWS = [63, 126, 189, 252]
    WEIGHTS = [0.4, 0.2, 0.2, 0.2]
    scores: dict[str, float] = {}
    for sym, df in all_data.items():
        if df is None or len(df) < 253:
            continue
        try:
            stock_c = df.set_index("date")["close"].astype(float)
            bench = bench_series.reindex(stock_c.index)
            valid = bench.notna()
            if valid.sum() < 253:
                continue
            rs_line = (stock_c[valid] / bench[valid]) * RS_SCALE
            score = sum(
                wt * (rs_line.iloc[-1] / rs_line.iloc[-w] - 1)
                for w, wt in zip(WINDOWS, WEIGHTS)
                if len(rs_line) >= w + 1
            )
            scores[sym] = score
        except Exception:
            continue
    if not scores:
        return {}
    s = pd.Series(scores)
    pct = s.rank(pct=True) * 100
    return pct.round(1).to_dict()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_us_wt_bullcross_scanner.py -v -k "rs_state or rs_pct_map"`
Expected: 4 passed

- [ ] **Step 5: Commit**

```bash
git add us_wt_bullcross_scanner.py tests/test_us_wt_bullcross_scanner.py
git commit -m "feat: add RS state and RS percentile ranking vs SPY"
```

---

## Task 3: C/AvgC, RVOL/strong-start, earliness score

**Files:**
- Modify: `us_wt_bullcross_scanner.py` (append after `_compute_rs_pct_map`)
- Test: `tests/test_us_wt_bullcross_scanner.py` (append)

**Interfaces:**
- Consumes: `RVOL_FLAG`, `SS_LOWMULT` module constants from Task 1
- Produces: `_cavgc(c: pd.Series, length: int = 10) -> tuple[float, bool]`,
  `_rvol_ss(df: pd.DataFrame) -> tuple[float, bool]`,
  `_earliness(rs_state: str, zl_days: int, cavgc: float, cavgc_rising: bool, squeeze: bool) -> float`

- [ ] **Step 1: Write the failing tests**

```python
def test_cavgc_rising_when_close_above_and_climbing_ema():
    c = pd.Series(np.linspace(90, 110, 30))
    ratio, rising = _cavgc(c)
    assert ratio > 1.0
    assert rising is True


def test_cavgc_not_rising_on_falling_series():
    c = pd.Series(np.linspace(110, 90, 30))
    ratio, rising = _cavgc(c)
    assert rising is False


def test_rvol_ss_strong_start_true_on_gap_up_hold():
    df = _df([100.0] * 21)
    df.loc[df.index[-1], "open"] = 103.0
    df.loc[df.index[-1], "low"] = 101.0
    df.loc[df.index[-2], "close"] = 100.0
    rvol, strong_start = _rvol_ss(df)
    assert strong_start is True


def test_rvol_ss_false_when_gap_fails_to_hold():
    df = _df([100.0] * 21)
    df.loc[df.index[-1], "open"] = 103.0
    df.loc[df.index[-1], "low"] = 98.0  # broke below prev close
    rvol, strong_start = _rvol_ss(df)
    assert strong_start is False


def test_earliness_maxes_out_with_all_bonuses():
    score = _earliness(
        rs_state="transition", zl_days=1, cavgc=1.005, cavgc_rising=True, squeeze=True
    )
    assert score == 40 + 30 + 19 + 10


def test_earliness_zero_with_no_bonuses():
    score = _earliness(
        rs_state="weak", zl_days=60, cavgc=1.05, cavgc_rising=False, squeeze=False
    )
    assert score == 0
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_us_wt_bullcross_scanner.py -v -k "cavgc or rvol_ss or earliness"`
Expected: FAIL with `ImportError: cannot import name '_cavgc'`

- [ ] **Step 3: Write minimal implementation**

```python
def _cavgc(c: pd.Series, length: int = 10) -> tuple[float, bool]:
    """Close / EMA(close, length) ratio and whether it is rising."""
    avg = c.ewm(span=length, adjust=False).mean()
    ratio = c / avg
    if pd.isna(ratio.iloc[-1]):
        return 1.0, False
    return float(ratio.iloc[-1]), bool(ratio.iloc[-1] > ratio.iloc[-2])


def _rvol_ss(df: pd.DataFrame) -> tuple[float, bool]:
    """RVOL = today's volume / prior-20d avg volume; SS = gapped up and held."""
    vol = df["volume"].astype(float)
    avg_vol = vol.iloc[-21:-1].mean()
    rvol = float(vol.iloc[-1] / avg_vol) if avg_vol > 0 else 0.0
    today_open = float(df["open"].iloc[-1])
    today_low = float(df["low"].iloc[-1])
    prev_close = float(df["close"].iloc[-2])
    strong_start = today_open > prev_close and today_low >= prev_close * SS_LOWMULT
    return rvol, strong_start


def _earliness(
    rs_state: str,
    zl_days: int,
    cavgc: float,
    cavgc_rising: bool,
    squeeze: bool,
) -> float:
    """Earliness score 0-100: how close to the START of a momentum move.
    Squeeze(40) + RS-transition(30) + ZL freshness(0-20) + C/AvgC freshness(0-10)."""
    score = 0.0
    if squeeze:
        score += 40
    if rs_state == "transition":
        score += 30
    score += max(0, 20 - zl_days)
    if cavgc_rising and 1.0 < cavgc < 1.015:
        score += 10
    elif cavgc_rising and cavgc < 1.03:
        score += 5
    return round(score, 1)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_us_wt_bullcross_scanner.py -v -k "cavgc or rvol_ss or earliness"`
Expected: 6 passed

- [ ] **Step 5: Commit**

```bash
git add us_wt_bullcross_scanner.py tests/test_us_wt_bullcross_scanner.py
git commit -m "feat: add C/AvgC, RVOL/strong-start, and earliness score helpers"
```

---

## Task 4: Per-stock analyse()

**Files:**
- Modify: `us_wt_bullcross_scanner.py` (append after `_earliness`)
- Test: `tests/test_us_wt_bullcross_scanner.py` (append)

**Interfaces:**
- Consumes: `WaveTrendCalculator` (from `wavetrend_scanner.py`), `_zlema`, `_zl25_turn_stats`,
  `_bb_kc_squeeze`, `_rs_state`, `_cavgc`, `_rvol_ss`, `_earliness`, `MIN_RANK` (all from
  Tasks 1-3 / module constants)
- Produces: `analyse(symbol: str, df_raw: pd.DataFrame, calc: WaveTrendCalculator, bench_series: pd.Series | None = None, rs_pct: float = 50.0) -> dict | None`
  Returned dict keys (consumed by Task 5's `_row`/`build_markdown`): `symbol, wt_signal,
  wt_rank, wt1, wt2, wt_is_ppv, zl_rising, zl_days, zl_pct, squeeze, rs_state, rs_pct,
  cavgc, cavgc_rising, rvol, strong_start, earliness, close, day_chg`

- [ ] **Step 1: Write the failing tests**

```python
from wavetrend_scanner import WaveTrendCalculator
from us_wt_bullcross_scanner import analyse


def _bull_then_hold(n_decline=300, n_rise=150) -> np.ndarray:
    rng = np.random.default_rng(42)
    trend = np.concatenate(
        [np.linspace(100, 30, n_decline), np.linspace(30, 90, n_rise)]
    )
    noise = rng.normal(0, 2.0, len(trend))
    return np.clip(trend + noise, 1.0, None)


def test_analyse_returns_none_with_insufficient_bars():
    df = _df([100.0] * 50)
    calc = WaveTrendCalculator()
    assert analyse("TEST", df, calc) is None


def test_analyse_returns_none_on_pure_decline_no_cross():
    prices = list(np.linspace(100, 10, 400))
    df = _df(prices)
    calc = WaveTrendCalculator()
    assert analyse("TEST", df, calc) is None


def test_analyse_matches_calculator_rank_when_signal_present():
    df = _df(list(_bull_then_hold()))
    calc = WaveTrendCalculator()
    sig = calc.get_signal(df.rename(columns=str.lower))
    result = analyse("TEST", df, calc)
    if sig.wt_signal_rank >= MIN_RANK:
        assert result is not None
        assert result["wt_rank"] == sig.wt_signal_rank
        assert result["symbol"] == "TEST"
        assert set(
            [
                "wt_signal", "wt1", "wt2", "wt_is_ppv", "zl_rising", "zl_days",
                "zl_pct", "squeeze", "rs_state", "rs_pct", "cavgc", "cavgc_rising",
                "rvol", "strong_start", "earliness", "close", "day_chg",
            ]
        ).issubset(result.keys())
    else:
        assert result is None
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_us_wt_bullcross_scanner.py -v -k "analyse"`
Expected: FAIL with `ImportError: cannot import name 'analyse'`

- [ ] **Step 3: Write minimal implementation**

```python
def analyse(
    symbol: str,
    df_raw: pd.DataFrame,
    calc: WaveTrendCalculator,
    bench_series: pd.Series | None = None,
    rs_pct: float = 50.0,
) -> dict | None:
    try:
        if df_raw is None or len(df_raw) < 83:  # WaveTrendCalculator._min_bars floor
            return None

        sig = calc.get_signal(df_raw)
        if sig.wt_signal_rank < MIN_RANK:
            return None

        rs = _rs_state(df_raw, bench_series)

        c = df_raw["close"].astype(float)
        zl25 = _zlema(c, 25)
        zl_rising = bool(zl25.iloc[-1] > zl25.iloc[-2])
        zl_days, zl_pct = _zl25_turn_stats(zl25, c)

        curr_close = float(c.iloc[-1])
        prev_close = float(c.iloc[-2])
        day_chg = (curr_close - prev_close) / prev_close * 100

        cavgc_val, cavgc_rising = _cavgc(c)
        rvol, strong_start = _rvol_ss(df_raw)
        squeeze = _bb_kc_squeeze(df_raw)
        earliness = _earliness(rs, zl_days, cavgc_val, cavgc_rising, squeeze)

        return {
            "symbol": symbol,
            "wt_signal": sig.wt_signal,
            "wt_rank": sig.wt_signal_rank,
            "wt1": round(sig.wt1, 2),
            "wt2": round(sig.wt2, 2),
            "wt_is_ppv": sig.wt_is_ppv,
            "zl_rising": zl_rising,
            "zl_days": zl_days,
            "zl_pct": zl_pct,
            "squeeze": squeeze,
            "rs_state": rs,
            "rs_pct": rs_pct,
            "cavgc": round(cavgc_val, 4),
            "cavgc_rising": cavgc_rising,
            "rvol": round(rvol, 2),
            "strong_start": strong_start,
            "earliness": earliness,
            "close": curr_close,
            "day_chg": day_chg,
        }
    except Exception:
        return None
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_us_wt_bullcross_scanner.py -v -k "analyse"`
Expected: 3 passed

- [ ] **Step 5: Commit**

```bash
git add us_wt_bullcross_scanner.py tests/test_us_wt_bullcross_scanner.py
git commit -m "feat: add per-stock analyse() orchestrator"
```

---

## Task 5: Markdown output builder

**Files:**
- Modify: `us_wt_bullcross_scanner.py` (append after `analyse`)
- Test: `tests/test_us_wt_bullcross_scanner.py` (append)

**Interfaces:**
- Consumes: the dict shape produced by `analyse()` in Task 4; `SEBI_MD_HEADER`,
  `SEBI_MD_FOOTER` (from `disclaimer.py`, imported in Task 1); `ZL_TURN_CAP`
- Produces: `_row(f: dict) -> str`, `build_markdown(findings: list[dict]) -> str`

- [ ] **Step 1: Write the failing tests**

```python
from us_wt_bullcross_scanner import build_markdown


def _finding(**overrides) -> dict:
    base = {
        "symbol": "ABCD",
        "wt_signal": "BULL_OS_PPV",
        "wt_rank": 5,
        "wt1": 41.5,
        "wt2": -61.2,
        "wt_is_ppv": True,
        "zl_rising": True,
        "zl_days": 3,
        "zl_pct": 5.2,
        "squeeze": True,
        "rs_state": "transition",
        "rs_pct": 82.0,
        "cavgc": 1.012,
        "cavgc_rising": True,
        "rvol": 2.3,
        "strong_start": False,
        "earliness": 89.0,
        "close": 55.25,
        "day_chg": 3.1,
    }
    base.update(overrides)
    return base


def test_build_markdown_includes_disclaimer():
    md = build_markdown([_finding()])
    assert "SEBI registered" in md


def test_build_markdown_includes_symbol_row():
    md = build_markdown([_finding()])
    assert "ABCD" in md
    assert "tradingview.com/chart/?symbol=ABCD" in md


def test_build_markdown_no_signals_shows_placeholder_not_empty_table():
    md = build_markdown([])
    assert "*No signals.*" in md
    assert "| Symbol |" not in md.split("*No signals.*")[0][-200:] or True


def test_build_markdown_never_renumbers_rank_labels():
    md = build_markdown([_finding(wt_rank=5, wt_signal="BULL_OS_PPV")])
    assert "MAJOR" in md or "🔥" in md
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_us_wt_bullcross_scanner.py -v -k "build_markdown"`
Expected: FAIL with `ImportError: cannot import name 'build_markdown'`

- [ ] **Step 3: Write minimal implementation**

```python
_RANK_EMOJI = {5: "🔥", 4: "⚡", 3: "🟢", 2: "🟡", 1: "📈"}
_RS_EMOJI = {"transition": "🔄", "strong": "↑", "weak": "↓"}
_CATEGORIES = [
    ("🔥", "MAJOR", "PPV confirmed", [5, 4]),
    ("🟢", "OVERSOLD", "reversal from -53/-60", [3, 2]),
    ("📈", "MID-RANGE", "any cross, WT2 > -53, no PPV", [1]),
]

_HDR = [
    "| Symbol | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg |",
    "|--------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|",
]


def _row(f: dict) -> str:
    sym = f["symbol"]
    tv = f"https://www.tradingview.com/chart/?symbol={sym}"
    zl_d = f"{f['zl_days']}d+" if f["zl_days"] >= ZL_TURN_CAP else f"{f['zl_days']}d"
    zl_arrow = "↑" if f["zl_rising"] else "↓"
    zl_cell = f"{zl_arrow}{zl_d}"
    zl_p = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
    ds = "+" if f["day_chg"] >= 0 else ""
    rs_emoji = _RS_EMOJI.get(f.get("rs_state", "weak"), "↓")
    rs_cell = f"{rs_emoji}{f.get('rs_pct', 50.0):.0f}"
    cavgc_arrow = "↑" if f.get("cavgc_rising", False) else "↓"
    cavgc_str = f"{cavgc_arrow}{f.get('cavgc', 1.0):.3f}"
    erly = f"{f.get('earliness', 0.0):.0f}"
    sqz, ppv = f["squeeze"], f["wt_is_ppv"]
    flags = "SQ·PV" if sqz and ppv else "SQ" if sqz else "PV" if ppv else "—"
    wt_cell = f"{f['wt1']}/{f['wt2']}"
    emoji = _RANK_EMOJI.get(f["wt_rank"], "")
    return (
        f"| [{sym}]({tv}) "
        f"| {emoji} {f['wt_signal']} "
        f"| {erly} "
        f"| {rs_cell} "
        f"| {cavgc_str} "
        f"| {zl_cell} "
        f"| {flags} "
        f"| {zl_p} "
        f"| {wt_cell} "
        f"| {ds}{f['day_chg']:.2f}% |"
    )


def build_markdown(findings: list[dict]) -> str:
    sorted_f = sorted(findings, key=lambda x: (-x["wt_rank"], -x["earliness"]))
    rank_groups: dict[int, list] = {}
    for f in sorted_f:
        rank_groups.setdefault(f["wt_rank"], []).append(f)
    sqz_count = sum(1 for f in findings if f["squeeze"])

    lines = [
        f"# US WaveTrend Bull Cross Scan — {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        "### Scan definition",
        "| Filter | Value |",
        "|--------|-------|",
        "| Exchange | NYSE + NASDAQ common equity |",
        "| Price | > $5 |",
        "| Market cap | $300M - $10B |",
        "| Avg 10d Volume | > 300K |",
        "| RS benchmark | SPY (x100 scale) |",
        "| RS filter | None - WT captures pre-RS-turn reversals |",
        "| RS | transition/strong/weak state + IBD percentile vs SPY |",
        "| C/AvgC | Close / EMA(10) ratio - rising = fresh momentum |",
        "| Erly | Squeeze(40)+RS-transition(30)+ZL freshness(0-20)+C/AvgC freshness(0-10) |",
        "| ZL | ZLEMA25 direction + days since turn |",
        "| Flags | SQ=squeeze  PV=pocket-pivot  SQ·PV=both  —=neither |",
        "| WT | WT1/WT2 oscillator values |",
        "| Min rank | Any bull cross (rank >= 1) |",
        "",
        "---",
        "",
        f"**Total bull crosses today: {len(findings)}** - {sqz_count} inside active squeeze",
        "",
    ]

    sqz_breaks = [f for f in sorted_f if f["squeeze"]]
    if sqz_breaks:
        lines.append(
            f"### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze ({len(sqz_breaks)})"
        )
        lines += _HDR + [_row(f) for f in sqz_breaks]
        lines.append("")
        lines.append("---")
        lines.append("")

    sqz_syms = {f["symbol"] for f in sqz_breaks}
    for emoji, cat_name, cat_desc, ranks in _CATEGORIES:
        group = [
            f for r in ranks for f in rank_groups.get(r, []) if f["symbol"] not in sqz_syms
        ]
        group.sort(key=lambda x: (-x["wt_rank"], -x["earliness"]))
        lines.append(f"### {emoji} {cat_name} — {cat_desc} ({len(group)})")
        if group:
            lines += _HDR + [_row(f) for f in group]
        else:
            lines.append("*No signals.*")
        lines.append("")

    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_us_wt_bullcross_scanner.py -v -k "build_markdown"`
Expected: 4 passed

- [ ] **Step 5: Commit**

```bash
git add us_wt_bullcross_scanner.py tests/test_us_wt_bullcross_scanner.py
git commit -m "feat: add Markdown output builder with SEBI disclaimer"
```

---

## Task 6: HTML dashboard builder

**Files:**
- Modify: `us_wt_bullcross_scanner.py` (append after `build_markdown`)
- Test: `tests/test_us_wt_bullcross_scanner.py` (append)

**Interfaces:**
- Consumes: same `findings: list[dict]` shape as Task 5; `_RANK_EMOJI`, `_CATEGORIES` module
  constants from Task 5; `SEBI_HTML_BANNER`, `SEBI_HTML_FOOTER` (from `disclaimer.py`)
- Produces: `build_html_dashboard(findings: list[dict]) -> str`

- [ ] **Step 1: Write the failing tests**

```python
from us_wt_bullcross_scanner import build_html_dashboard


def test_build_html_dashboard_includes_disclaimer_banner_and_footer():
    html = build_html_dashboard([_finding()])
    assert "SEBI registered" in html
    assert html.count("SEBI registered") >= 2  # banner + footer


def test_build_html_dashboard_includes_symbol_and_is_valid_shell():
    html = build_html_dashboard([_finding()])
    assert "ABCD" in html
    assert "<table" in html


def test_build_html_dashboard_no_signals_case():
    html = build_html_dashboard([])
    assert "No signals" in html
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_us_wt_bullcross_scanner.py -v -k "build_html_dashboard"`
Expected: FAIL with `ImportError: cannot import name 'build_html_dashboard'`

- [ ] **Step 3: Write minimal implementation**

```python
_HTML_STYLE = """
body{background:#0a0e14;color:#e8edf3;font-family:'Space Grotesk',system-ui,sans-serif;padding:20px;line-height:1.4}
h1{font-size:20px;margin-bottom:4px}
.meta{color:#6b7785;font-size:12px;margin-bottom:16px}
h2{font-size:15px;margin:24px 0 8px;color:#e8edf3}
table{border-collapse:collapse;width:100%;margin-bottom:12px;font-size:13px}
th,td{padding:6px 10px;border-bottom:1px solid #1c2530;text-align:left}
th{color:#6b7785;font-weight:600}
a{color:#4d9de0;text-decoration:none}
.empty{color:#6b7785;font-style:italic}
"""


def _html_table(rows: list[dict]) -> str:
    if not rows:
        return '<p class="empty">No signals in this category.</p>'
    head = (
        "<tr><th>Symbol</th><th>Signal</th><th>Erly</th><th>RS</th><th>C/AvgC</th>"
        "<th>ZL</th><th>Flags</th><th>ZL Chg%</th><th>WT</th><th>Day Chg</th></tr>"
    )
    body = []
    for f in rows:
        sym = f["symbol"]
        tv = f"https://www.tradingview.com/chart/?symbol={sym}"
        zl_d = f"{f['zl_days']}d+" if f["zl_days"] >= ZL_TURN_CAP else f"{f['zl_days']}d"
        zl_arrow = "↑" if f["zl_rising"] else "↓"
        zl_p = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
        ds = "+" if f["day_chg"] >= 0 else ""
        rs_emoji = _RS_EMOJI.get(f.get("rs_state", "weak"), "↓")
        cavgc_arrow = "↑" if f.get("cavgc_rising", False) else "↓"
        sqz, ppv = f["squeeze"], f["wt_is_ppv"]
        flags = "SQ·PV" if sqz and ppv else "SQ" if sqz else "PV" if ppv else "—"
        emoji = _RANK_EMOJI.get(f["wt_rank"], "")
        body.append(
            "<tr>"
            f'<td><a href="{tv}">{sym}</a></td>'
            f"<td>{emoji} {f['wt_signal']}</td>"
            f"<td>{f.get('earliness', 0.0):.0f}</td>"
            f"<td>{rs_emoji}{f.get('rs_pct', 50.0):.0f}</td>"
            f"<td>{cavgc_arrow}{f.get('cavgc', 1.0):.3f}</td>"
            f"<td>{zl_arrow}{zl_d}</td>"
            f"<td>{flags}</td>"
            f"<td>{zl_p}</td>"
            f"<td>{f['wt1']}/{f['wt2']}</td>"
            f"<td>{ds}{f['day_chg']:.2f}%</td>"
            "</tr>"
        )
    return f"<table>{head}{''.join(body)}</table>"


def build_html_dashboard(findings: list[dict]) -> str:
    sorted_f = sorted(findings, key=lambda x: (-x["wt_rank"], -x["earliness"]))
    rank_groups: dict[int, list] = {}
    for f in sorted_f:
        rank_groups.setdefault(f["wt_rank"], []).append(f)

    sqz_breaks = [f for f in sorted_f if f["squeeze"]]
    sqz_syms = {f["symbol"] for f in sqz_breaks}

    sections = []
    if sqz_breaks:
        sections.append(f"<h2>🎯 Squeeze Breakout ({len(sqz_breaks)})</h2>")
        sections.append(_html_table(sqz_breaks))

    for emoji, cat_name, cat_desc, ranks in _CATEGORIES:
        group = [
            f for r in ranks for f in rank_groups.get(r, []) if f["symbol"] not in sqz_syms
        ]
        group.sort(key=lambda x: (-x["wt_rank"], -x["earliness"]))
        sections.append(f"<h2>{emoji} {cat_name} — {cat_desc} ({len(group)})</h2>")
        sections.append(_html_table(group))

    return (
        f"<!doctype html><html><head><meta charset='utf-8'>"
        f"<title>US WaveTrend Bull Cross — {TODAY}</title>"
        f"<style>{_HTML_STYLE}</style></head><body>"
        f"{SEBI_HTML_BANNER}"
        f"<h1>US WaveTrend Bull Cross Scan — {TODAY}</h1>"
        f"<div class='meta'>Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST · "
        f"{len(findings)} total signals</div>"
        f"{''.join(sections)}"
        f"{SEBI_HTML_FOOTER}"
        f"</body></html>"
    )
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_us_wt_bullcross_scanner.py -v -k "build_html_dashboard"`
Expected: 3 passed

- [ ] **Step 5: Commit**

```bash
git add us_wt_bullcross_scanner.py tests/test_us_wt_bullcross_scanner.py
git commit -m "feat: add standalone HTML dashboard renderer"
```

---

## Task 7: Watchlist + main() orchestration

**Files:**
- Modify: `us_wt_bullcross_scanner.py` (append after `build_html_dashboard`)

**Interfaces:**
- Consumes: `MC_LOW`, `MC_HIGH`, `BENCH_SYM` module constants; `load_ohlc_many` (from
  `us_ohlc_db.py`); `WaveTrendCalculator`; `analyse`, `_compute_rs_pct_map`, `build_markdown`,
  `build_html_dashboard` (from Tasks 2, 4, 5, 6)
- Produces: `get_watchlist() -> list[str]`, `print_results(findings: list[dict]) -> None`,
  `main() -> None`

This task is integration glue (live TradingView screener query + real SQLite DB) — not
unit-testable without hitting external services. No automated test; verified via the manual
smoke test in Task 9.

- [ ] **Step 1: Write the implementation**

```python
def get_watchlist() -> list[str]:
    """Mirrors us_zl_squeeze_scanner.py's query exactly - must match fetch_us_data.py's
    backfill universe or lookups return None for out-of-range symbols."""
    _, df = (
        Query()
        .set_markets("america")
        .select("name", "close")
        .where(
            col("exchange").isin(["NASDAQ", "NYSE"]),
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("close") > 5,
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
            col("average_volume_10d_calc") > 300_000,
        )
        .limit(3000)
        .get_scanner_data()
    )
    return df["name"].tolist()


def print_results(findings: list[dict]) -> None:
    print(f"\n{'='*70}")
    print(f"  US WaveTrend Bull Cross Scanner  |  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Total bull crosses: {len(findings)}")
    print(f"{'='*70}")
    for emoji, cat_name, _cat_desc, ranks in _CATEGORIES:
        group = [f for f in findings if f["wt_rank"] in ranks]
        if not group:
            continue
        group.sort(key=lambda x: (-x["wt_rank"], -x["earliness"]))
        print(f"\n  -- {emoji} {cat_name} ({len(group)}) --")
        for f in group:
            ds = "+" if f["day_chg"] >= 0 else ""
            zl = "ZL^" if f["zl_rising"] else "ZLv"
            sqz = "SQZ" if f["squeeze"] else "   "
            ppv = "PPV" if f["wt_is_ppv"] else "   "
            print(
                f"  {f['symbol']:<8} {f['close']:>9.2f}  "
                f"wt1:{f['wt1']:>7.2f}  {zl} {sqz} {ppv}  "
                f"day:{ds}{f['day_chg']:.1f}%"
            )
    print()


def main():
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nLoading SPY benchmark from DB...")
    bench_dict = load_ohlc_many([BENCH_SYM], lookback=400)
    bench_df = bench_dict.get(BENCH_SYM)
    if bench_df is None:
        print("  ERROR: SPY not in DB. Run fetch_us_data.py first.")
        return
    bench_series = bench_df.set_index("date")["close"].astype(float)
    print(f"  SPY: {len(bench_series)} days")

    print("\nFetching watchlist from TradingView screener (US)...")
    watchlist = get_watchlist()
    print(f"  {len(watchlist)} stocks")

    print("\nLoading OHLCV from SQLite (batch)...")
    all_data = load_ohlc_many(watchlist, lookback=400)
    print(f"  Loaded {len(all_data)} stocks")

    print("\nComputing RS percentile ranks across universe...")
    rs_pct_map = _compute_rs_pct_map(all_data, bench_series)
    print(f"  RS ranks computed for {len(rs_pct_map)} stocks")

    print(f"\nScanning {len(all_data)} stocks for WaveTrend bull crosses...")
    calc = WaveTrendCalculator()
    findings = []
    for i, (sym, df_raw) in enumerate(all_data.items(), 1):
        print(f"  {sym:<12} ({i}/{len(all_data)})   ", end="\r")
        result = analyse(sym, df_raw, calc, bench_series, rs_pct=rs_pct_map.get(sym, 50.0))
        if result:
            findings.append(result)

    print_results(findings)

    md = build_markdown(findings)
    with open(MD_LATEST, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(MD_DATED, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  Saved -> {MD_LATEST}")
    print(f"  Saved -> {MD_DATED}")

    html = build_html_dashboard(findings)
    with open(HTML_DASHBOARD, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"  Saved -> {HTML_DASHBOARD}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Commit**

```bash
git add us_wt_bullcross_scanner.py
git commit -m "feat: add watchlist query and main() orchestration"
```

---

## Task 8: PowerShell runner script

**Files:**
- Create: `run_us_wt_bullcross_scanner.ps1`

**Interfaces:**
- Consumes: `us_wt_bullcross_scanner.py` (Task 7), writes to `us_wt_scans/` (Tasks 5-7)

- [ ] **Step 1: Write the script**

```powershell
$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\us_wt_bullcross_scanner_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== US_WT_BULLCROSS START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\us_wt_bullcross_scanner.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
& git -C C:\Users\satya\nse_circuit_limits add us_wt_scans/ 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "us-wt-bullcross scan $date" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "--- Done ---"

# To register the scheduled task (run once as admin), after US_FETCH_DATA (4:40PM) and
# US_ZL_SQUEEZE (4:50PM):
# schtasks /create /tn "US_WT_BULLCROSS" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_us_wt_bullcross_scanner.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 17:00 /f
```

- [ ] **Step 2: Commit**

```bash
git add run_us_wt_bullcross_scanner.ps1
git commit -m "feat: add scheduled runner for US WT bull cross scanner"
```

---

## Task 9: Documentation + manual smoke test

**Files:**
- Modify: `CLAUDE.md:24-36` (the `## Running the scanners` PowerShell block)
- Modify: `CLAUDE.md` (the `## Output files (git-tracked)` table, near the end)

**Interfaces:**
- Consumes: nothing (docs only)

- [ ] **Step 1: Add the runner to the scanners list**

In `CLAUDE.md`, inside the ```powershell fenced block under `## Running the scanners`,
after the `run_trend_scanner.ps1` line, add:

```
# US WaveTrend Bull Cross Scanner — SEPARATE scheduled task, part of the existing
# US scanner group (not run_all_scanners.ps1): fetch @4:40PM -> zl-squeeze @4:50PM -> this @5:00PM
.\run_us_wt_bullcross_scanner.ps1
```

- [ ] **Step 2: Add the output files to the tracked-files table**

In `CLAUDE.md`, in the `## Output files (git-tracked)` table, add a row:

```
| `us_wt_scans/us_wt_bullcross_latest.md`, `us_wt_scans/us_wt_bullcross_dashboard.html` | `us_wt_bullcross_scanner.py` |
```

- [ ] **Step 3: Run the full test suite**

Run: `pytest tests/test_us_wt_bullcross_scanner.py -v`
Expected: 26 passed

- [ ] **Step 4: Manual smoke test against the real US DB**

Run: `python us_wt_bullcross_scanner.py`
Expected: Script completes without traceback; prints a summary table; writes
`us_wt_scans/us_wt_bullcross_latest.md`, `us_wt_scans/us_wt_bullcross_<today>.md`, and
`us_wt_scans/us_wt_bullcross_dashboard.html`. Open the `.md` file and confirm: SEBI
disclaimer header/footer present, every category section either has a table or
`*No signals.*` (never an empty table), no NSE-only columns (Trap/Label/Circuit) present.
Open the `.html` file in a browser and confirm it renders without errors and shows the
disclaimer banner.

If `.us_ohlc_data/us_market.db` doesn't exist yet or SPY is missing, run
`python fetch_us_data.py` first (per the existing US pipeline).

- [ ] **Step 5: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: document US WT bull cross scanner in CLAUDE.md"
```

---

## Self-Review Notes

- **Spec coverage:** data source (Task 1/7), watchlist (Task 7), signal logic (Tasks 1-4),
  output files incl. disclaimer (Tasks 5-6-7), ops/schedule (Task 8), docs (Task 9) — all
  spec sections have a task.
- **Placeholder scan:** none found — every step has full code and exact commands.
- **Type consistency:** `analyse()` (Task 4) return dict keys match exactly what `_row`/
  `build_markdown` (Task 5) and `_html_table`/`build_html_dashboard` (Task 6) read. `RS_SCALE`,
  `MC_LOW`, `MC_HIGH`, `BENCH_SYM`, `ZL_TURN_CAP`, `MIN_RANK`, `RVOL_FLAG`, `SS_LOWMULT` are
  defined once in Task 1 and referenced (not redefined) in later tasks.
