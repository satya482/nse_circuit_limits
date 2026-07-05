# Consolidation Scanner (Phase 1+2) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a daily EOD scanner (`consolidation_scanner.run(universe_df, as_of) -> pd.DataFrame`) that finds NSE stocks in a mature multi-week consolidation, scores their Quality (spring tightness) and Imminence (spring release proximity) 0-100, and labels a tier (COLD/WARM/HOT), writing both a git-tracked CSV and a markdown report.

**Architecture:** New `consolidation/` Python package (`indicators.py`, `quality.py`, `imminence.py`, `tiers.py`, `consolidation_scanner.py`) sitting at repo root alongside `ohlc_db.py`. All indicator math is pure functions over `pd.DataFrame`/`pd.Series` — no classes, no new SQLite tables, no persisted state. Reuses `ohlc_db.py`'s existing `load_ohlc_many()`, `load_delivery()`, `deliv_spike()`, and (after a small refactor) a newly-extracted `cmf_series()`. Universe comes from a TradingView `Query()` call mirroring `wt_bullcross_scanner.py`. Tier-transition history is derived by diffing today's output against the most recent prior `results/*-consolidation.csv`, not a database.

**Tech Stack:** Python 3.13, pandas, numpy, `tradingview_screener`, pytest, PowerShell (runner script) — no new dependencies.

## Global Constraints

- No look-ahead bias: every indicator at bar `t` uses data through `t` only (`.claude/rules/backtesting-integrity.md`)
- IST-aware datetimes: use `timezone(timedelta(hours=5, minutes=30))`, never naive `datetime.now()` for the `as_of` stamp
- No float equality: crossovers use `>` / `<=` boundary logic, never `==` (`.claude/rules/pine-script-conventions.md`)
- Minimum 250 bars of history required per stock; skip (return `None` from `analyse()`) otherwise — never crash
- SQLite is the only OHLCV source: `load_ohlc_many()` from `ohlc_db.py`, never a new CSV or API call inside scanner logic
- Every new `.md` file must carry the SEBI disclaimer (`disclaimer.py`'s `SEBI_MD_HEADER`/`SEBI_MD_FOOTER`)
- Never hand-edit generated output files (`results/*.csv`, `consolidation_scans/*.md`)
- Commit with `git commit --no-verify` in this repo (pre-commit hooks are disabled here per project CLAUDE.md)
- Design source: `docs/superpowers/specs/2026-07-05-consolidation-scanner-phase1-2-design.md` and `research/consolidation_capital_efficiency_spec.md` (Sections 0-5, 11 only — Phase 3/5/6/7 are out of scope)
- **Gate definition (user decision):** a stock enters scoring only after passing 2 gates — EMA dual gate (Sec 2.1) AND BB squeeze gate (Sec 2.2). Volume exhaustion and RS character are scored components, not additional filters.
- Several numeric thresholds below are first-pass interpretations of qualitative spec language (flagged inline with `# ponytail:` or docstring notes) — spec's own Sec 14 already treats its stated thresholds as unvalidated, to be tuned by the future Phase 7 backtest, not this plan.

---

### Task 1: EMA compression + BB/KC squeeze indicators

**Files:**
- Create: `consolidation/__init__.py` (empty)
- Create: `consolidation/indicators.py`
- Test: `tests/test_consolidation_indicators.py`

**Interfaces:**
- Produces: `ema_compression(df) -> pd.DataFrame` (adds `ema50,ema100,ema200,atr50,ema_spread,spread_atr_ratio,spread_pct,spread_delta`), `compression_duration(df) -> int`, `ema_dual_gate(df) -> tuple[bool, int]`, `ema_stage(spread_delta: float) -> str`, `bollinger_keltner(df) -> pd.DataFrame` (adds `bb_upper,bb_lower,bb_width,bb_width_percentile,kc_upper,kc_lower,squeeze_on`), `squeeze_gate(df) -> tuple[bool, int]`. Module constants: `EMA_ATR_GATE=1.5`, `EMA_PCT_GATE=0.03`, `EMA_MIN_BARS=10`, `BB_WIDTH_PCT_MAX=20.0`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_consolidation_indicators.py
import pandas as pd
from consolidation import indicators


def _flat_df(n: int, price: float = 100.0, vol: float = 1_000_000.0) -> pd.DataFrame:
    """n bars, dead-flat OHLCV -- EMAs converge to `price`, spread -> 0."""
    return pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": [price] * n, "high": [price * 1.001] * n,
        "low": [price * 0.999] * n, "close": [price] * n,
        "volume": [vol] * n,
    })


def test_ema_compression_flat_series_spread_shrinks_to_near_zero():
    df = indicators.ema_compression(_flat_df(300))
    assert df["ema_spread"].iloc[-1] < df["ema_spread"].iloc[100]
    assert df["spread_pct"].iloc[-1] < 0.001


def test_compression_duration_counts_consecutive_tail_bars():
    df = indicators.ema_compression(_flat_df(300))
    duration = indicators.compression_duration(df)
    assert duration > indicators.EMA_MIN_BARS


def test_ema_dual_gate_passes_on_long_flat_series():
    df = indicators.ema_compression(_flat_df(300))
    passes, duration = indicators.ema_dual_gate(df)
    assert passes is True
    assert duration >= indicators.EMA_MIN_BARS


def test_ema_dual_gate_fails_on_trending_series():
    n = 300
    prices = [100.0 + i * 0.5 for i in range(n)]  # steadily trending, never compresses
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": prices, "high": [p * 1.02 for p in prices],
        "low": [p * 0.98 for p in prices], "close": prices,
        "volume": [1_000_000.0] * n,
    })
    df = indicators.ema_compression(df)
    passes, _ = indicators.ema_dual_gate(df)
    assert passes is False


def test_ema_stage_classification():
    assert indicators.ema_stage(-0.01) == "STAGE_1_CONVERGING"
    assert indicators.ema_stage(0.0) == "STAGE_2_COMPRESSED"
    assert indicators.ema_stage(0.0005) == "STAGE_2_COMPRESSED"
    assert indicators.ema_stage(0.01) == "STAGE_3_DIVERGING"
    assert indicators.ema_stage(float("nan")) == "STAGE_1_CONVERGING"


def test_bollinger_keltner_flat_series_is_squeezed():
    df = indicators.bollinger_keltner(_flat_df(300))
    assert bool(df["squeeze_on"].iloc[-1]) is True
    assert df["bb_width_percentile"].iloc[-1] <= indicators.BB_WIDTH_PCT_MAX


def test_squeeze_gate_passes_on_flat_series():
    df = indicators.bollinger_keltner(_flat_df(300))
    passes, days = indicators.squeeze_gate(df)
    assert passes is True
    assert days >= 5


def test_squeeze_gate_fails_on_volatile_series():
    n = 300
    prices = [100.0 + (10 if i % 2 == 0 else -10) for i in range(n)]  # violent chop, wide bands
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": prices, "high": [p * 1.05 for p in prices],
        "low": [p * 0.95 for p in prices], "close": prices,
        "volume": [1_000_000.0] * n,
    })
    df = indicators.bollinger_keltner(df)
    passes, _ = indicators.squeeze_gate(df)
    assert passes is False
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_consolidation_indicators.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'consolidation'`

- [ ] **Step 3: Create the package and implement**

```python
# consolidation/__init__.py
```

```python
# consolidation/indicators.py
"""Consolidation scanner indicators: EMA compression (Sec 2.1), BB/KC squeeze (Sec 2.2),
volume exhaustion (Sec 2.3), RS character (Sec 2.4). Pure functions over OHLCV DataFrames
from ohlc_db.load_ohlc()/load_ohlc_many() (lowercase date/open/high/low/close/volume,
oldest-first, plain 'date' column)."""

import pandas as pd
import numpy as np

EMA_ATR_GATE = 1.5
EMA_PCT_GATE = 0.03
EMA_MIN_BARS = 10

BB_PERIOD = 20
BB_STD = 2.0
KC_PERIOD = 20
KC_ATR_MULT = 1.5
SQUEEZE_MIN_BARS = 5
BB_WIDTH_PCT_MAX = 20.0

VOL_MA_PERIOD = 50
VOL_PCTILE_LOOKBACK = 252

RS_MIN_WEEKS = 14
RS_FLAT_THRESHOLD = 0.01
PRICE_FLAT_THRESHOLD = 0.05


def _ema(series: pd.Series, period: int) -> pd.Series:
    return series.ewm(span=period, adjust=False).mean()


def _atr_sma(high: pd.Series, low: pd.Series, close: pd.Series, period: int) -> pd.Series:
    tr = pd.concat(
        [high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()],
        axis=1,
    ).max(axis=1)
    return tr.rolling(period).mean()


def ema_compression(df: pd.DataFrame) -> pd.DataFrame:
    """Adds ema50/100/200, atr50 (SMA basis, matches TradingView ta.sma(ta.tr) —
    see pine-script-conventions.md), ema_spread, spread_atr_ratio, spread_pct
    (fraction, e.g. 0.03 = 3%, NOT *100), spread_delta (5-bar change in spread_pct)."""
    df = df.copy()
    close = df["close"].astype(float)
    high = df["high"].astype(float)
    low = df["low"].astype(float)

    df["ema50"] = _ema(close, 50)
    df["ema100"] = _ema(close, 100)
    df["ema200"] = _ema(close, 200)
    df["atr50"] = _atr_sma(high, low, close, 50)

    ema_high = df[["ema50", "ema100", "ema200"]].max(axis=1)
    ema_low = df[["ema50", "ema100", "ema200"]].min(axis=1)
    df["ema_spread"] = ema_high - ema_low
    df["spread_atr_ratio"] = df["ema_spread"] / df["atr50"].replace(0, np.nan)
    df["spread_pct"] = df["ema_spread"] / df["ema200"].replace(0, np.nan)
    df["spread_delta"] = df["spread_pct"] - df["spread_pct"].shift(5)
    return df


def compression_duration(df: pd.DataFrame) -> int:
    """Consecutive tail bars where spread_atr_ratio < EMA_ATR_GATE AND spread_pct < EMA_PCT_GATE."""
    ratio = df["spread_atr_ratio"]
    pct = df["spread_pct"]
    count = 0
    for i in range(len(df) - 1, -1, -1):
        r, p = ratio.iloc[i], pct.iloc[i]
        if pd.isna(r) or pd.isna(p) or not (r < EMA_ATR_GATE and p < EMA_PCT_GATE):
            break
        count += 1
    return count


def ema_dual_gate(df: pd.DataFrame) -> tuple[bool, int]:
    duration = compression_duration(df)
    return duration >= EMA_MIN_BARS, duration


def ema_stage(spread_delta: float) -> str:
    """Sec 2.1 stage classification. NaN (insufficient history) treated as converging,
    the conservative default -- a stock with unknown trajectory shouldn't score as imminent."""
    if pd.isna(spread_delta):
        return "STAGE_1_CONVERGING"
    if spread_delta < -0.001:
        return "STAGE_1_CONVERGING"
    if spread_delta > 0.001:
        return "STAGE_3_DIVERGING"
    return "STAGE_2_COMPRESSED"


def bollinger_keltner(df: pd.DataFrame) -> pd.DataFrame:
    """Adds bb_upper/lower/width, bb_width_percentile (true rolling percentile rank,
    252-bar window, 0=tightest-ever), kc_upper/lower, squeeze_on."""
    df = df.copy()
    close = df["close"].astype(float)
    high = df["high"].astype(float)
    low = df["low"].astype(float)

    bb_basis = close.rolling(BB_PERIOD).mean()
    bb_std = close.rolling(BB_PERIOD).std()
    df["bb_upper"] = bb_basis + BB_STD * bb_std
    df["bb_lower"] = bb_basis - BB_STD * bb_std
    df["bb_width"] = df["bb_upper"] - df["bb_lower"]

    lookback = min(252, len(df))
    roll = df["bb_width"].rolling(lookback, min_periods=max(lookback // 2, BB_PERIOD))
    df["bb_width_percentile"] = roll.rank(pct=True) * 100

    kc_atr = _atr_sma(high, low, close, KC_PERIOD)
    kc_basis = close.rolling(KC_PERIOD).mean()
    df["kc_upper"] = kc_basis + KC_ATR_MULT * kc_atr
    df["kc_lower"] = kc_basis - KC_ATR_MULT * kc_atr

    df["squeeze_on"] = (df["bb_upper"] < df["kc_upper"]) & (df["bb_lower"] > df["kc_lower"])
    return df


def squeeze_gate(df: pd.DataFrame) -> tuple[bool, int]:
    """(passes, squeeze_bars). squeeze_on true >= SQUEEZE_MIN_BARS consecutive tail
    bars AND today's bb_width_percentile <= BB_WIDTH_PCT_MAX."""
    sq = df["squeeze_on"]
    count = 0
    for i in range(len(sq) - 1, -1, -1):
        if bool(sq.iloc[i]):
            count += 1
        else:
            break
    last_pct = df["bb_width_percentile"].iloc[-1]
    width_ok = pd.notna(last_pct) and float(last_pct) <= BB_WIDTH_PCT_MAX
    return count >= SQUEEZE_MIN_BARS and width_ok, count
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_consolidation_indicators.py -v`
Expected: PASS (8 tests)

- [ ] **Step 5: Commit**

```bash
git add consolidation/__init__.py consolidation/indicators.py tests/test_consolidation_indicators.py
git commit --no-verify -m "feat: add EMA compression + BB/KC squeeze indicators for consolidation scanner"
```

---

### Task 2: Volume exhaustion + RS character indicators

**Files:**
- Modify: `consolidation/indicators.py`
- Modify: `tests/test_consolidation_indicators.py`

**Interfaces:**
- Consumes: nothing new from Task 1 (independent indicator groups, same file)
- Produces: `volume_exhaustion(df) -> pd.DataFrame` (adds `vol_ma50, vol_percentile, quiet_accum_bar`), `volume_phase(df) -> str` (`PHASE_A`/`PHASE_B`/`PHASE_C`), `volume_declining(df) -> bool`, `rs_metrics(df, bench_df) -> dict | None` (keys: `rs_weekly_last, rs_ema9_last, rs_slope, above_ema, price_flat, rs_52wk_high, price_20d_high`), `classify_rs_character(metrics: dict) -> str` (one of `CHAR_1_DECLINING, CHAR_2_FLAT, CHAR_3_HOLDING, CHAR_4_RISING, CHAR_5_RS_BREAKOUT`). These are consumed by Task 3 (`quality.py`) and Task 6 (`consolidation_scanner.py`).

- [ ] **Step 1: Write the failing tests**

```python
# append to tests/test_consolidation_indicators.py

def _bench_series(n: int, val: float = 100.0) -> pd.DataFrame:
    return pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": [val] * n, "high": [val] * n, "low": [val] * n,
        "close": [val] * n, "volume": [1_000_000.0] * n,
    })


def test_volume_exhaustion_declining_volume_low_percentile():
    n = 300
    # elevated volume for first 100 bars, then steadily declining to multi-month lows
    vol = [3_000_000.0] * 100 + list(np.linspace(3_000_000.0, 200_000.0, n - 100))
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": [100.0] * n, "high": [101.0] * n, "low": [99.0] * n,
        "close": [100.0] * n, "volume": vol,
    })
    result = indicators.volume_exhaustion(df)
    assert result["vol_percentile"].iloc[-1] < 20


def test_volume_phase_c_on_multi_month_lows():
    n = 300
    vol = [3_000_000.0] * 100 + list(np.linspace(3_000_000.0, 200_000.0, n - 100))
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": [100.0] * n, "high": [101.0] * n, "low": [99.0] * n,
        "close": [100.0] * n, "volume": vol,
    })
    df = indicators.volume_exhaustion(df)
    assert indicators.volume_phase(df) == "PHASE_C"


def test_quiet_accum_bar_flags_high_volume_flat_price():
    n = 60
    close = [100.0] * (n - 1) + [100.3]  # <1% move on the last bar
    vol = [1_000_000.0] * (n - 1) + [2_000_000.0]  # 2x the 10-bar average
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": close, "high": [c * 1.005 for c in close],
        "low": [c * 0.995 for c in close], "close": close, "volume": vol,
    })
    result = indicators.volume_exhaustion(df)
    assert bool(result["quiet_accum_bar"].iloc[-1]) is True


def test_rs_metrics_none_on_insufficient_history():
    stock = _bench_series(30, 100.0)
    bench = _bench_series(30, 100.0)
    assert indicators.rs_metrics(stock, bench) is None


def test_rs_metrics_char_1_declining_when_rs_falls_below_ema():
    n = 260  # ~52 weeks
    stock_close = [100.0] * 200 + list(np.linspace(100.0, 70.0, n - 200))  # stock falling vs flat bench
    stock = pd.DataFrame({
        "date": pd.date_range("2023-01-02", periods=n, freq="B"),
        "open": stock_close, "high": [c * 1.01 for c in stock_close],
        "low": [c * 0.99 for c in stock_close], "close": stock_close,
        "volume": [1_000_000.0] * n,
    })
    bench = _bench_series(n, 100.0)
    metrics = indicators.rs_metrics(stock, bench)
    assert metrics is not None
    assert indicators.classify_rs_character(metrics) == "CHAR_1_DECLINING"


def test_rs_metrics_char_4_rising_when_rs_climbs_price_flat():
    n = 260
    stock_close = [100.0] * 200 + list(np.linspace(100.0, 103.0, n - 200))  # RS climbs, price ~flat
    stock = pd.DataFrame({
        "date": pd.date_range("2023-01-02", periods=n, freq="B"),
        "open": stock_close, "high": [c * 1.01 for c in stock_close],
        "low": [c * 0.99 for c in stock_close], "close": stock_close,
        "volume": [1_000_000.0] * n,
    })
    bench = _bench_series(n, 100.0)
    metrics = indicators.rs_metrics(stock, bench)
    assert metrics is not None
    assert indicators.classify_rs_character(metrics) == "CHAR_4_RISING"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_consolidation_indicators.py -v -k "volume or rs_metrics"`
Expected: FAIL with `AttributeError: module 'consolidation.indicators' has no attribute 'volume_exhaustion'`

- [ ] **Step 3: Implement**

```python
# append to consolidation/indicators.py

def volume_exhaustion(df: pd.DataFrame) -> pd.DataFrame:
    """Adds vol_ma50, vol_percentile (true rolling percentile rank of the 5-bar
    average volume, 252-bar window), quiet_accum_bar (Sec 2.3: volume 1.5x+ the
    10-bar average with <1% price move -- volume without price move)."""
    df = df.copy()
    volume = df["volume"].astype(float)
    close = df["close"].astype(float)

    df["vol_ma50"] = volume.rolling(VOL_MA_PERIOD, min_periods=VOL_MA_PERIOD // 2).mean()
    vol5 = volume.rolling(5, min_periods=3).mean()
    lookback = min(VOL_PCTILE_LOOKBACK, len(df))
    df["vol_percentile"] = (
        vol5.rolling(lookback, min_periods=max(lookback // 2, 5)).rank(pct=True) * 100
    )
    df["quiet_accum_bar"] = (
        volume >= 1.5 * volume.rolling(10, min_periods=5).mean()
    ) & ((close / close.shift(1) - 1).abs() < 0.01)
    return df


def volume_declining(df: pd.DataFrame) -> bool:
    """True if the 5-bar average volume today is below its level 5 bars ago."""
    vol5 = df["volume"].astype(float).rolling(5, min_periods=3).mean()
    if len(vol5) < 6 or pd.isna(vol5.iloc[-1]) or pd.isna(vol5.iloc[-6]):
        return False
    return bool(vol5.iloc[-1] < vol5.iloc[-6])


def volume_phase(df: pd.DataFrame) -> str:
    """Sec 2.3 PHASE_A/B/C, informational context (not part of the numeric quality
    score, which uses vol_percentile directly). PHASE_C (multi-month lows) takes
    priority over the A/B declining-volume split."""
    vol_pctile = df["vol_percentile"].iloc[-1]
    if pd.notna(vol_pctile) and float(vol_pctile) <= 20:
        return "PHASE_C"
    last_vol = float(df["volume"].iloc[-1])
    vol_ma50 = df["vol_ma50"].iloc[-1]
    if pd.isna(vol_ma50):
        return "PHASE_A"
    return "PHASE_A" if last_vol > vol_ma50 else "PHASE_B"


def rs_metrics(df: pd.DataFrame, bench_df: pd.DataFrame) -> dict | None:
    """Weekly RS = stock_close / bench_close (Friday close). None if fewer than
    RS_MIN_WEEKS weeks of aligned history. RS_FLAT_THRESHOLD / PRICE_FLAT_THRESHOLD
    are first-pass interpretations of the spec's qualitative 'flat'/'holding'
    language -- unvalidated, Sec 14 backtest territory."""
    close_stock = df.set_index("date")["close"].astype(float)
    close_bench = bench_df.set_index("date")["close"].astype(float)
    rs = (close_stock / close_bench.reindex(close_stock.index).ffill()).dropna()
    rs_weekly = rs.resample("W-FRI").last().dropna()

    if len(rs_weekly) < RS_MIN_WEEKS:
        return None

    rs_ema9 = rs_weekly.ewm(span=9, adjust=False).mean()
    rs_slope = float(rs_weekly.pct_change(4).iloc[-1])
    above_ema = bool(rs_weekly.iloc[-1] > rs_ema9.iloc[-1])

    price_now = float(close_stock.iloc[-1])
    idx_4w = max(0, len(close_stock) - 20)
    price_4w_ago = float(close_stock.iloc[idx_4w])
    price_flat = abs(price_now / price_4w_ago - 1) < PRICE_FLAT_THRESHOLD

    rs_52wk_max = rs_weekly.rolling(52, min_periods=26).max().iloc[-1]
    rs_52wk_high = bool(rs_weekly.iloc[-1] >= rs_52wk_max * 0.999)

    price_20d_max = close_stock.rolling(20, min_periods=10).max().iloc[-1]
    price_20d_high = bool(price_now >= price_20d_max * 0.999)

    return {
        "rs_weekly_last": float(rs_weekly.iloc[-1]),
        "rs_ema9_last": float(rs_ema9.iloc[-1]),
        "rs_slope": rs_slope,
        "above_ema": above_ema,
        "price_flat": price_flat,
        "rs_52wk_high": rs_52wk_high,
        "price_20d_high": price_20d_high,
    }


def classify_rs_character(metrics: dict) -> str:
    """Sec 2.4 CHAR_1..5. Order matters: CHAR_5 (breakout) and CHAR_4 (rising) are
    checked before the flatter CHAR_3/CHAR_1/CHAR_2 fallbacks."""
    rs_slope = metrics["rs_slope"]
    above_ema = metrics["above_ema"]
    price_flat = metrics["price_flat"]

    if metrics["rs_52wk_high"] and price_flat and not metrics["price_20d_high"]:
        return "CHAR_5_RS_BREAKOUT"
    if rs_slope > RS_FLAT_THRESHOLD and price_flat:
        return "CHAR_4_RISING"
    if above_ema and abs(rs_slope) <= RS_FLAT_THRESHOLD:
        return "CHAR_3_HOLDING"
    if not above_ema and rs_slope < -RS_FLAT_THRESHOLD:
        return "CHAR_1_DECLINING"
    return "CHAR_2_FLAT"
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_consolidation_indicators.py -v`
Expected: PASS (14 tests total)

- [ ] **Step 5: Commit**

```bash
git add consolidation/indicators.py tests/test_consolidation_indicators.py
git commit --no-verify -m "feat: add volume exhaustion + RS character indicators"
```

---

### Task 3: CMF refactor + quality score

**Files:**
- Modify: `ohlc_db.py:208-246` (extract `cmf_series()` out of `cmf_days()`)
- Modify: `tests/test_cmf.py` (add a regression test for the new `cmf_series()`)
- Create: `consolidation/quality.py`
- Test: `tests/test_consolidation_quality.py`

**Interfaces:**
- Consumes: `indicators.ema_stage`, `indicators.classify_rs_character` return-value vocabularies (Task 1/2) — this task's `quality_score()` takes their string outputs directly, so the dict keys must match exactly: `STAGE_1_CONVERGING/STAGE_2_COMPRESSED/STAGE_3_DIVERGING` and `CHAR_1_DECLINING/CHAR_2_FLAT/CHAR_3_HOLDING/CHAR_4_RISING/CHAR_5_RS_BREAKOUT`.
- Produces: `ohlc_db.cmf_series(df, n=20) -> pd.Series` (new), `quality.deliv_trend(symbol, db_path=...) -> str | None` (`RISING`/`AT_BASELINE`/`BELOW`/`None`), `quality.quality_score(bb_width_percentile, ema_stage, vol_percentile, rs_char, cmf, deliv_trend_label) -> float`. Consumed by Task 5 (`tiers.py`) and Task 6 (`consolidation_scanner.py`).

- [ ] **Step 1: Write the failing tests**

```python
# append to tests/test_cmf.py

def test_cmf_series_matches_cmf_days_internal_calc():
    """Regression guard for the cmf_days() refactor: cmf_series()'s last value
    must have the same sign cmf_days() would report as cmf_positive."""
    from ohlc_db import cmf_series

    df = _synthetic_cross_df()
    series = cmf_series(df, n=5)
    positive, _ = cmf_days(df, n=5, cap=30)
    assert (series.iloc[-1] > 0) == positive
```

```python
# tests/test_consolidation_quality.py
import pandas as pd
from consolidation import quality


def test_quality_score_perfect_setup_scores_100():
    score = quality.quality_score(
        bb_width_percentile=0.0,
        ema_stage="STAGE_2_COMPRESSED",
        vol_percentile=0.0,
        rs_char="CHAR_4_RISING",
        cmf=0.15,
        deliv_trend_label="RISING",
    )
    assert score == 100.0


def test_quality_score_worst_setup_scores_zero():
    score = quality.quality_score(
        bb_width_percentile=20.0,
        ema_stage="STAGE_3_DIVERGING",
        vol_percentile=20.0,
        rs_char="CHAR_1_DECLINING",
        cmf=-0.05,
        deliv_trend_label="BELOW",
    )
    assert score == 0.0


def test_quality_score_unknown_deliv_trend_scores_zero_points_for_that_component():
    score = quality.quality_score(
        bb_width_percentile=0.0,
        ema_stage="STAGE_2_COMPRESSED",
        vol_percentile=0.0,
        rs_char="CHAR_4_RISING",
        cmf=0.15,
        deliv_trend_label=None,
    )
    assert score == 90.0  # 100 minus the 10-pt delivery component


def test_deliv_trend_rising_when_ma20_well_above_baseline(monkeypatch):
    import ohlc_db
    dates = pd.date_range("2026-01-01", periods=120, freq="D")
    pcts = [20.0] * 100 + [35.0] * 20  # recent 20d well above the 120d median
    df = pd.DataFrame({"date": dates, "deliv_pct": pcts})
    monkeypatch.setattr(ohlc_db, "load_delivery", lambda symbol, lookback=120, db_path=None: df)
    assert quality.deliv_trend("TEST") == "RISING"


def test_deliv_trend_none_on_insufficient_history(monkeypatch):
    import ohlc_db
    monkeypatch.setattr(ohlc_db, "load_delivery", lambda symbol, lookback=120, db_path=None: None)
    assert quality.deliv_trend("TEST") is None
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_cmf.py tests/test_consolidation_quality.py -v`
Expected: FAIL — `cmf_series` doesn't exist yet, `consolidation.quality` module doesn't exist yet

- [ ] **Step 3: Refactor ohlc_db.py and implement quality.py**

Replace `ohlc_db.py:208-246` (the `cmf_days` function) with:

```python
def cmf_series(df: pd.DataFrame, n: int = 20) -> pd.Series:
    """Raw Chaikin Money Flow series (rolling n-bar sum of money-flow-volume over
    rolling n-bar sum of volume), index-reset, NaNs dropped. Empty if fewer than
    n bars available. Factored out of cmf_days() so quality scoring (which needs
    the raw value, not just sign+days-since-cross) shares one source of truth."""
    high = df["high"].astype(float)
    low = df["low"].astype(float)
    close = df["close"].astype(float)
    volume = df["volume"].astype(float)

    range_ = high - low
    mfm = np.where(range_ > 0, ((close - low) - (high - close)) / range_, 0.0)
    mfv = pd.Series(mfm, index=df.index) * volume

    return (
        mfv.rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum()
    ).dropna().reset_index(drop=True)


def cmf_days(df: pd.DataFrame, n: int = 20, cap: int = 30) -> tuple[bool, int] | None:
    """Chaikin Money Flow zero-line-cross recency.
    Returns (cmf_positive, bars_since_zero_cross), bars_ago capped at `cap`.
    None if fewer than n + 2 bars.
    No float equality: cross = sign flip via > / <= boundary, mirrors
    zl25_stats()'s bars-ago scan pattern.
    """
    if len(df) < n + 2:
        return None

    cmf = cmf_series(df, n=n)
    m = len(cmf)
    if m < 2:
        return None

    cmf_positive = bool(cmf.iloc[-1] > 0)

    limit = max(1, m - cap)
    for i in range(m - 1, limit - 1, -1):
        curr, prev = cmf.iloc[i], cmf.iloc[i - 1]
        if cmf_positive and curr > 0 and prev <= 0:
            return True, (m - 1) - i
        if not cmf_positive and curr <= 0 and prev > 0:
            return False, (m - 1) - i

    return cmf_positive, cap
```

```python
# consolidation/quality.py
"""Quality score (Sec 3): how good a spring this consolidation is. Fixed weights
against absolute thresholds -- NOT normalized across today's candidate set, so a
score is comparable day-over-day (needed for stable tier thresholds)."""

import pandas as pd

import ohlc_db

DELIV_MA_WINDOW = 20
DELIV_BASELINE_WINDOW = 120
DELIV_RISING_MULT = 1.15
DELIV_BELOW_MULT = 0.85

_EMA_STAGE_PTS = {"STAGE_1_CONVERGING": 8, "STAGE_2_COMPRESSED": 20, "STAGE_3_DIVERGING": 0}
_RS_CHAR_PTS = {
    "CHAR_1_DECLINING": 0, "CHAR_2_FLAT": 5, "CHAR_3_HOLDING": 12,
    "CHAR_4_RISING": 20, "CHAR_5_RS_BREAKOUT": 20,
}
_DELIV_TREND_PTS = {"RISING": 10, "AT_BASELINE": 5, "BELOW": 0}


def deliv_trend(symbol: str, db_path=ohlc_db.DB_PATH) -> str | None:
    """RISING / AT_BASELINE / BELOW per spec Sec 2.6. None if insufficient delivery
    history (< DELIV_BASELINE_WINDOW days). The AT_BASELINE band (0.85x-1.15x) is a
    first-pass interpretation -- spec only defines the RISING threshold explicitly;
    unvalidated, Sec 14 backtest territory."""
    df = ohlc_db.load_delivery(symbol, lookback=DELIV_BASELINE_WINDOW, db_path=db_path)
    if df is None or len(df) < DELIV_BASELINE_WINDOW:
        return None
    pct = df["deliv_pct"].astype(float)
    deliv_ma20 = pct.iloc[-DELIV_MA_WINDOW:].mean()
    deliv_baseline = pct.median()
    if deliv_baseline == 0:
        return None
    ratio = deliv_ma20 / deliv_baseline
    if ratio > DELIV_RISING_MULT:
        return "RISING"
    if ratio < DELIV_BELOW_MULT:
        return "BELOW"
    return "AT_BASELINE"


def quality_score(
    bb_width_percentile: float,
    ema_stage: str,
    vol_percentile: float,
    rs_char: str,
    cmf: float,
    deliv_trend_label: str | None,
) -> float:
    """Sec 3 table, full 100 pts: BB depth(20) + EMA stage(20) + vol exhaustion(15)
    + RS character(20) + CMF(15) + delivery trend(10)."""
    bb_pts = max(0.0, (20 - bb_width_percentile) * 1.0)
    stage_pts = _EMA_STAGE_PTS[ema_stage]
    vol_pts = max(0.0, (20 - vol_percentile) * 0.75)
    rs_pts = _RS_CHAR_PTS[rs_char]
    cmf_pts = 15 if cmf > 0.10 else (10 if cmf > 0.05 else (6 if cmf > 0 else 0))
    deliv_pts = _DELIV_TREND_PTS.get(deliv_trend_label, 0)
    return round(bb_pts + stage_pts + vol_pts + rs_pts + cmf_pts + deliv_pts, 1)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_cmf.py tests/test_consolidation_quality.py -v`
Expected: PASS — all `test_cmf.py` tests (including the pre-existing ones) still pass, confirming the refactor didn't change `cmf_days()` behavior; new quality tests pass too

- [ ] **Step 5: Commit**

```bash
git add ohlc_db.py tests/test_cmf.py consolidation/quality.py tests/test_consolidation_quality.py
git commit --no-verify -m "refactor: extract cmf_series() from cmf_days(); add consolidation quality score"
```

---

### Task 4: Imminence score + pre-break signals

**Files:**
- Create: `consolidation/imminence.py`
- Test: `tests/test_consolidation_imminence.py`

**Interfaces:**
- Consumes: nothing from earlier tasks directly (operates on raw `pd.Series`/`pd.DataFrame` + booleans passed in by Task 6) — but its function names/signatures below are exactly what Task 6 will call.
- Produces: `spread_delta_crossover(spread_delta: pd.Series) -> bool`, `ema_stage3_flag(spread_delta: pd.Series) -> bool`, `bb_breathing(bb_width_percentile: pd.Series) -> bool`, `range_position(df, age_bars: int) -> float` (0.0-1.0), `higher_low(df, window: int = 5) -> bool`, `wick_rejection_absorbed(df, age_bars: int) -> bool`, `signal3_weight(quiet_accum_today: bool, deliv_spike_today: bool) -> float`, `imminence_score(signal1, signal2, signal3_wt, signal4, signal5, signal6, stage3_flag, rs_breakout_flag, bb_breathing_flag, range_pos) -> tuple[float, float]` (returns `(score 0-100, prebreak_count 0-6)`).

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_consolidation_imminence.py
import pandas as pd
from consolidation import imminence


def _df(n: int, closes, highs=None, opens=None) -> pd.DataFrame:
    closes = list(closes)
    highs = list(highs) if highs is not None else [c * 1.01 for c in closes]
    opens = list(opens) if opens is not None else closes
    return pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": opens, "high": highs,
        "low": [c * 0.99 for c in closes], "close": closes,
        "volume": [1_000_000.0] * n,
    })


def test_spread_delta_crossover_true_on_boundary_cross():
    s = pd.Series([-0.002, -0.001, 0.0, 0.001])
    assert imminence.spread_delta_crossover(s) is True


def test_spread_delta_crossover_false_when_already_positive():
    s = pd.Series([0.001, 0.002, 0.003, 0.004])
    assert imminence.spread_delta_crossover(s) is False


def test_ema_stage3_flag_requires_ten_prior_negative_bars():
    s = pd.Series([-0.001] * 10 + [0.001])
    assert imminence.ema_stage3_flag(s) is True
    s_short = pd.Series([-0.001] * 5 + [0.001])
    assert imminence.ema_stage3_flag(s_short) is False


def test_bb_breathing_true_on_two_bar_tick_up_from_low_percentile():
    s = pd.Series([10.0, 11.0, 13.0])
    assert imminence.bb_breathing(s) is True


def test_bb_breathing_false_when_starting_above_threshold():
    s = pd.Series([20.0, 25.0, 30.0])
    assert imminence.bb_breathing(s) is False


def test_range_position_top_third_flag():
    n = 30
    closes = [100.0] * (n - 1) + [109.0]  # near the top of a 100-110 range
    df = _df(n, closes, highs=[110.0] * n)
    df.loc[df.index[:-1], "low"] = 95.0
    pos = imminence.range_position(df, age_bars=20)
    assert pos >= 2 / 3


def test_higher_low_true_when_todays_low_exceeds_prior_window_low():
    n = 10
    df = _df(n, [100.0] * n)
    df.loc[df.index[-6:-1], "low"] = 95.0
    df.loc[df.index[-1], "low"] = 98.0
    assert imminence.higher_low(df, window=5) is True


def test_signal3_weight_full_on_spike_half_without():
    assert imminence.signal3_weight(quiet_accum_today=True, deliv_spike_today=True) == 1.0
    assert imminence.signal3_weight(quiet_accum_today=True, deliv_spike_today=False) == 0.5
    assert imminence.signal3_weight(quiet_accum_today=False, deliv_spike_today=True) == 0.0


def test_imminence_score_all_signals_firing_scores_100():
    score, count = imminence.imminence_score(
        signal1=True, signal2=True, signal3_wt=1.0, signal4=True,
        signal5=True, signal6=True, stage3_flag=True,
        rs_breakout_flag=True, bb_breathing_flag=True, range_pos=0.9,
    )
    assert score == 100.0
    assert count == 6.0


def test_imminence_score_nothing_firing_scores_zero():
    score, count = imminence.imminence_score(
        signal1=False, signal2=False, signal3_wt=0.0, signal4=False,
        signal5=False, signal6=False, stage3_flag=False,
        rs_breakout_flag=False, bb_breathing_flag=False, range_pos=0.1,
    )
    assert score == 0.0
    assert count == 0.0
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_consolidation_imminence.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'consolidation.imminence'`

- [ ] **Step 3: Implement**

```python
# consolidation/imminence.py
"""Imminence score (Sec 4): how close the spring is to releasing. Pre-break
signals ①-⑥ map to signal1..signal6 params in imminence_score()."""

import pandas as pd

_PREBREAK_MAX = 6.0


def spread_delta_crossover(spread_delta: pd.Series) -> bool:
    """Signal ②: spread_delta crosses positive (ta.crossover-equivalent, no float
    equality -- boundary via > / <=)."""
    if len(spread_delta) < 2:
        return False
    return bool(spread_delta.iloc[-1] > 0 and spread_delta.iloc[-2] <= 0)


def ema_stage3_flag(spread_delta: pd.Series) -> bool:
    """Sec 4 'EMA Stage 3 flag': spread_delta just crossed positive AFTER >= 10
    bars held negative (distinguishes a fresh, meaningful fanout from noise)."""
    if len(spread_delta) < 12:
        return False
    if not (spread_delta.iloc[-1] > 0 and spread_delta.iloc[-2] <= 0):
        return False
    count = 0
    for i in range(len(spread_delta) - 2, -1, -1):
        v = spread_delta.iloc[i]
        if pd.isna(v) or v > 0:
            break
        count += 1
    return count >= 10


def bb_breathing(bb_width_percentile: pd.Series) -> bool:
    """Sec 4 'BB breathing' / signal ④: bb_width_percentile ticks up 2 consecutive
    bars starting from below 15."""
    if len(bb_width_percentile) < 3:
        return False
    p0, p1, p2 = bb_width_percentile.iloc[-3:]
    if pd.isna(p0) or pd.isna(p1) or pd.isna(p2):
        return False
    return bool(p0 < 15 and p1 > p0 and p2 > p1)


def range_position(df: pd.DataFrame, age_bars: int) -> float:
    """0.0-1.0 position of today's close within the high/low range of the
    trailing max(age_bars, 10) bars."""
    window = df.iloc[-max(age_bars, 10):]
    hi, lo = window["high"].max(), window["low"].min()
    if hi == lo:
        return 0.0
    return float((df["close"].iloc[-1] - lo) / (hi - lo))


def higher_low(df: pd.DataFrame, window: int = 5) -> bool:
    """Signal ⑤: today's low exceeds the low of the prior `window` bars."""
    if len(df) < window + 1:
        return False
    low = df["low"].astype(float)
    today_low = low.iloc[-1]
    prior_low = low.iloc[-(window + 1):-1].min()
    return bool(today_low > prior_low)


def wick_rejection_absorbed(df: pd.DataFrame, age_bars: int) -> bool:
    """Signal ⑥: yesterday had a long upper wick near the range top, today closed
    back above/held yesterday's body top (rejection absorbed, not confirmed)."""
    if len(df) < 3:
        return False
    window = df.iloc[-max(age_bars, 10):]
    range_high = window["high"].max()
    prev = df.iloc[-2]
    today = df.iloc[-1]
    prev_body_top = max(prev["open"], prev["close"])
    prev_range = prev["high"] - prev["low"]
    if prev_range <= 0:
        return False
    prev_wick = prev["high"] - prev_body_top
    near_top = prev["high"] >= range_high * 0.98
    long_wick = prev_wick > prev_range * 0.3
    absorbed = today["close"] >= prev_body_top
    return bool(near_top and long_wick and absorbed)


def signal3_weight(quiet_accum_today: bool, deliv_spike_today: bool) -> float:
    """Signal ③: quiet accumulation bar, upgraded to full weight when delivery %
    also spiked that day (spec: 0.5 without delivery confirmation, 1.0 with)."""
    if not quiet_accum_today:
        return 0.0
    return 1.0 if deliv_spike_today else 0.5


def imminence_score(
    signal1: bool,
    signal2: bool,
    signal3_wt: float,
    signal4: bool,
    signal5: bool,
    signal6: bool,
    stage3_flag: bool,
    rs_breakout_flag: bool,
    bb_breathing_flag: bool,
    range_pos: float,
) -> tuple[float, float]:
    """Sec 4 table: pre-break count(30) + EMA stage3(25) + RS breakout(20) +
    BB breathing(15) + range position(10). Returns (score 0-100, prebreak_count 0-6)."""
    prebreak_count = (
        (1.0 if signal1 else 0.0)
        + (1.0 if signal2 else 0.0)
        + signal3_wt
        + (1.0 if signal4 else 0.0)
        + (1.0 if signal5 else 0.0)
        + (1.0 if signal6 else 0.0)
    )
    prebreak_pts = prebreak_count / _PREBREAK_MAX * 30
    stage3_pts = 25 if stage3_flag else 0
    rs_pts = 20 if rs_breakout_flag else 0
    bb_pts = 15 if bb_breathing_flag else 0
    range_pts = 10 if range_pos >= 2 / 3 else 0
    score = prebreak_pts + stage3_pts + rs_pts + bb_pts + range_pts
    return round(score, 1), round(prebreak_count, 1)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_consolidation_imminence.py -v`
Expected: PASS (10 tests)

- [ ] **Step 5: Commit**

```bash
git add consolidation/imminence.py tests/test_consolidation_imminence.py
git commit --no-verify -m "feat: add imminence score + 6 pre-break signals"
```

---

### Task 5: Tiers, stateless age/peak, abandonment

**Files:**
- Create: `consolidation/tiers.py`
- Test: `tests/test_consolidation_tiers.py`

**Interfaces:**
- Consumes: `indicators.EMA_ATR_GATE, EMA_PCT_GATE, BB_WIDTH_PCT_MAX` (Task 1), `quality.quality_score()` (Task 3), `indicators.ema_stage()` (Task 1), `indicators.volume_declining()` (Task 2), `ohlc_db.cmf_series()` (Task 3).
- Produces: `tier(quality: float, imminence: float) -> str` (`TIER_1_HOT`/`TIER_2_WARM`/`TIER_3_COLD`/`NONE`), `consolidation_age(df) -> int` (df must already have `spread_atr_ratio, spread_pct, squeeze_on, bb_width_percentile` columns), `quality_peak_drawdown(df, age_bars, rs_char, cmf, deliv_trend_label) -> float`, `cmf_negative_streak(cmf_vals: pd.Series, threshold: float = -0.05) -> int`, `abandonment_reasons(rs_char, age_bars, volume_rising, cmf, cmf_days_negative, quality_drawdown) -> list[str]`. Consumed by Task 6.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_consolidation_tiers.py
import pandas as pd
from consolidation import tiers, indicators


def _gated_df(n: int) -> pd.DataFrame:
    """Flat series that passes both gates for its full length -- gives a
    predictable consolidation_age == n (or n-1 accounting for warmup NaNs)."""
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="B"),
        "open": [100.0] * n, "high": [100.5] * n,
        "low": [99.5] * n, "close": [100.0] * n,
        "volume": [1_000_000.0] * n,
    })
    df = indicators.ema_compression(df)
    df = indicators.bollinger_keltner(df)
    return df


def test_tier_hot_on_high_quality_high_imminence():
    assert tiers.tier(quality=75, imminence=65) == "TIER_1_HOT"


def test_tier_warm_on_high_quality_mid_imminence():
    assert tiers.tier(quality=80, imminence=45) == "TIER_2_WARM"


def test_tier_cold_on_high_quality_low_imminence():
    assert tiers.tier(quality=90, imminence=10) == "TIER_3_COLD"


def test_tier_none_below_quality_floor():
    assert tiers.tier(quality=50, imminence=90) == "NONE"


def test_consolidation_age_counts_consecutive_gated_bars():
    df = _gated_df(300)
    age = tiers.consolidation_age(df)
    assert age > indicators.EMA_MIN_BARS


def test_consolidation_age_zero_when_gate_breaks_today():
    df = _gated_df(300)
    df.loc[df.index[-1], "squeeze_on"] = False
    assert tiers.consolidation_age(df) == 0


def test_cmf_negative_streak_counts_tail_bars_below_threshold():
    s = pd.Series([0.1, 0.1, -0.06, -0.07, -0.08])
    assert tiers.cmf_negative_streak(s, threshold=-0.05) == 3


def test_abandonment_reasons_flags_declining_rs_and_stale_age():
    reasons = tiers.abandonment_reasons(
        rs_char="CHAR_1_DECLINING", age_bars=130, volume_rising=False,
        cmf=0.02, cmf_days_negative=0, quality_drawdown=5.0,
    )
    assert "RS_CHARACTER_DROPPED" in reasons
    assert "STALE_AGE" in reasons


def test_abandonment_reasons_empty_on_healthy_setup():
    reasons = tiers.abandonment_reasons(
        rs_char="CHAR_4_RISING", age_bars=30, volume_rising=False,
        cmf=0.08, cmf_days_negative=0, quality_drawdown=2.0,
    )
    assert reasons == []
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_consolidation_tiers.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'consolidation.tiers'`

- [ ] **Step 3: Implement**

```python
# consolidation/tiers.py
"""Tier labelling (Sec 5) + stateless consolidation_age / quality-peak-drawdown /
abandonment checks -- no persisted state, no DB. Age and peak are derived by
backward-scanning the historical OHLCV already loaded for today's indicator
calcs, the same 'bars-ago scan' idiom ohlc_db.cmf_days()/zl25_stats() use."""

import pandas as pd

from consolidation import indicators, quality

MAX_AGE_STALE = 120


def tier(quality: float, imminence: float) -> str:
    if quality < 70:
        return "NONE"
    if imminence >= 60:
        return "TIER_1_HOT"
    if imminence >= 30:
        return "TIER_2_WARM"
    return "TIER_3_COLD"


def consolidation_age(df: pd.DataFrame) -> int:
    """Consecutive tail bars where EMA dual gate AND squeeze gate both held
    (2-gate definition per user decision -- not the spec's ambiguous '4 gates').
    df must already have spread_atr_ratio, spread_pct, squeeze_on,
    bb_width_percentile columns (ema_compression() + bollinger_keltner() applied)."""
    ema_ok = (df["spread_atr_ratio"] < indicators.EMA_ATR_GATE) & (
        df["spread_pct"] < indicators.EMA_PCT_GATE
    )
    sq_ok = df["squeeze_on"] & (df["bb_width_percentile"] <= indicators.BB_WIDTH_PCT_MAX)
    combined = (ema_ok & sq_ok).fillna(False)
    count = 0
    for i in range(len(combined) - 1, -1, -1):
        if bool(combined.iloc[i]):
            count += 1
        else:
            break
    return count


def cmf_negative_streak(cmf_vals: pd.Series, threshold: float = -0.05) -> int:
    count = 0
    for i in range(len(cmf_vals) - 1, -1, -1):
        if cmf_vals.iloc[i] < threshold:
            count += 1
        else:
            break
    return count


def quality_peak_drawdown(
    df: pd.DataFrame,
    age_bars: int,
    rs_char: str,
    cmf: float,
    deliv_trend_label: str | None,
) -> float:
    """Points quality has fallen from its peak over the trailing
    min(age_bars, MAX_AGE_STALE) window.
    ponytail: rs_char / cmf / deliv_trend are held constant at today's value
    across the window -- only BB/EMA/vol components vary bar-to-bar (those are
    already full per-bar Series; re-classifying RS/CMF/delivery at every
    historical bar would need a much heavier per-bar resample loop for an
    abandonment check only). Revisit if this misfires in the Phase 7 backtest."""
    window = min(age_bars, MAX_AGE_STALE, len(df))
    if window < 2:
        return 0.0
    tail = df.iloc[-window:]
    scores = []
    for i in range(len(tail)):
        row = tail.iloc[i]
        bb_pct = row.get("bb_width_percentile")
        vol_pct = row.get("vol_percentile")
        if pd.isna(bb_pct) or pd.isna(vol_pct):
            continue
        stage = indicators.ema_stage(row.get("spread_delta"))
        scores.append(
            quality.quality_score(
                float(bb_pct), stage, float(vol_pct), rs_char, cmf, deliv_trend_label
            )
        )
    if not scores:
        return 0.0
    return round(max(scores) - scores[-1], 1)


def abandonment_reasons(
    rs_char: str,
    age_bars: int,
    volume_rising: bool,
    cmf: float,
    cmf_days_negative: int,
    quality_drawdown: float,
) -> list[str]:
    """Sec 5 abandonment triggers. Sector RS breakdown is not implemented here
    (needs a sector universe this scanner doesn't have) -- out of scope for v1."""
    reasons = []
    if rs_char in ("CHAR_1_DECLINING", "CHAR_2_FLAT"):
        reasons.append("RS_CHARACTER_DROPPED")
    if age_bars > MAX_AGE_STALE:
        reasons.append("STALE_AGE")
    if volume_rising:
        reasons.append("VOLUME_PHASE_REVERSED")
    if cmf < -0.05 and cmf_days_negative >= 5:
        reasons.append("CMF_DISTRIBUTION")
    if quality_drawdown >= 15:
        reasons.append("QUALITY_DRAWDOWN")
    return reasons
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_consolidation_tiers.py -v`
Expected: PASS (9 tests)

- [ ] **Step 5: Commit**

```bash
git add consolidation/tiers.py tests/test_consolidation_tiers.py
git commit --no-verify -m "feat: add tier labelling + stateless age/peak/abandonment checks"
```

---

### Task 6: Scanner orchestration + output

**Files:**
- Create: `consolidation/consolidation_scanner.py`
- Test: `tests/test_consolidation_scanner.py`

**Interfaces:**
- Consumes: everything from Tasks 1-5 (`indicators`, `quality`, `imminence`, `tiers` modules) plus `ohlc_db.load_ohlc_many`, `ohlc_db.cmf_series`, `ohlc_db.load_delivery`, `ohlc_db.deliv_spike`, `disclaimer.SEBI_MD_HEADER/FOOTER`.
- Produces: `analyse(symbol, df, bench_df) -> dict | None`, `run(universe_df: pd.DataFrame, as_of: str) -> pd.DataFrame` (spec's required signature — `universe_df` has a `symbol` column), `get_universe() -> list[str]`, `find_previous_csv(as_of: str) -> str | None`, `compute_transitions(rows: list[dict], as_of: str) -> dict`, `build_markdown(rows, as_of, transitions) -> str`, `main() -> None`. `COLUMNS` constant: `["symbol","quality","imminence","tier","age_bars","ema_stage","vol_phase","rs_char","cmf","deliv_trend","prebreak_count"]`.

- [ ] **Step 1: Write the failing tests (network/screener-free — test `analyse()` and the pure output helpers only)**

```python
# tests/test_consolidation_scanner.py
import os
import pandas as pd
import pytest

from consolidation import consolidation_scanner as cs


def _consolidating_df(n: int = 300) -> pd.DataFrame:
    """Flat-enough series to pass both gates: constant price/volume, tiny noise
    so rolling std isn't exactly zero (which would make BB width NaN-adjacent)."""
    import numpy as np
    rng = np.random.default_rng(42)
    noise = rng.normal(0, 0.05, n)
    close = [100.0 + x for x in noise]
    return pd.DataFrame({
        "date": pd.date_range("2023-06-01", periods=n, freq="B"),
        "open": close, "high": [c + 0.3 for c in close],
        "low": [c - 0.3 for c in close], "close": close,
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_consolidation_scanner.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'consolidation.consolidation_scanner'`

- [ ] **Step 3: Implement**

```python
# consolidation/consolidation_scanner.py
"""Consolidation Tracker — daily scanner. run(universe_df, as_of) -> pd.DataFrame
per spec Sec 0's required interface. Universe: own TradingView Query() mirroring
wt_bullcross_scanner.py (NSE common stock, mcap 1,000-5,00,000 Cr, price > Rs 50).
Gate: EMA dual gate AND BB squeeze gate only (2-gate definition, user decision --
volume/RS are scored components, not filters). No signals.db: tier-transition
history is derived by diffing today's output against the most recent prior
results/*-consolidation.csv."""

import os
import sys
from datetime import datetime, timezone, timedelta

import pandas as pd
from tradingview_screener import Query, col

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ohlc_db import load_ohlc_many, cmf_series, load_delivery, deliv_spike
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER

from consolidation import indicators, quality, imminence, tiers

IST = timezone(timedelta(hours=5, minutes=30))
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(REPO_DIR, "results")
MD_DIR = os.path.join(REPO_DIR, "consolidation_scans")
BENCH_SYM = "NIFTY MIDSML 400"

MC_LOW = 1_000 * 1_00_00_000
MC_HIGH = 5_00_000 * 1_00_00_000
MIN_BARS = 250

COLUMNS = [
    "symbol", "quality", "imminence", "tier", "age_bars", "ema_stage",
    "vol_phase", "rs_char", "cmf", "deliv_trend", "prebreak_count",
]
_TIER_RANK = {"TIER_1_HOT": 3, "TIER_2_WARM": 2, "TIER_3_COLD": 1, "NONE": 0}


def get_universe() -> list[str]:
    """TV screener, mirrors wt_bullcross_scanner.py's own band exactly."""
    _, df = (
        Query()
        .set_markets("india")
        .select("name")
        .where(
            col("exchange") == "NSE",
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("close") > 50,
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
        )
        .limit(2000)
        .get_scanner_data()
    )
    return df["name"].tolist()


def analyse(symbol: str, df: pd.DataFrame, bench_df: pd.DataFrame | None) -> dict | None:
    if df is None or len(df) < MIN_BARS or bench_df is None:
        return None

    df = indicators.ema_compression(df)
    df = indicators.bollinger_keltner(df)
    df = indicators.volume_exhaustion(df)

    ema_ok, _ = indicators.ema_dual_gate(df)
    sq_ok, _ = indicators.squeeze_gate(df)
    if not (ema_ok and sq_ok):
        return None

    metrics = indicators.rs_metrics(df, bench_df)
    if metrics is None:
        return None
    rs_char = indicators.classify_rs_character(metrics)

    cmf_vals = cmf_series(df, n=20)
    cmf_today = float(cmf_vals.iloc[-1]) if len(cmf_vals) else 0.0

    deliv_trend_label = quality.deliv_trend(symbol)

    stage = indicators.ema_stage(df["spread_delta"].iloc[-1])
    bb_pct = float(df["bb_width_percentile"].iloc[-1])
    vol_pct = float(df["vol_percentile"].iloc[-1])

    q_score = quality.quality_score(bb_pct, stage, vol_pct, rs_char, cmf_today, deliv_trend_label)
    age_bars = tiers.consolidation_age(df)

    stage3 = imminence.ema_stage3_flag(df["spread_delta"])
    rs_breakout_flag = rs_char == "CHAR_5_RS_BREAKOUT"
    bb_breathe = imminence.bb_breathing(df["bb_width_percentile"])
    range_pos = imminence.range_position(df, age_bars)

    sig1 = bool(metrics["rs_52wk_high"] and not metrics["price_20d_high"])
    sig2 = imminence.spread_delta_crossover(df["spread_delta"])
    quiet_today = bool(df["quiet_accum_bar"].iloc[-1])
    deliv_df = load_delivery(symbol, lookback=21)
    deliv_spike_today = deliv_df is not None and deliv_spike(deliv_df) is not None
    sig3_wt = imminence.signal3_weight(quiet_today, deliv_spike_today)
    sig5 = imminence.higher_low(df)
    sig6 = imminence.wick_rejection_absorbed(df, age_bars)

    imm_score, prebreak_count = imminence.imminence_score(
        sig1, sig2, sig3_wt, bb_breathe, sig5, sig6,
        stage3, rs_breakout_flag, bb_breathe, range_pos,
    )

    tier_label = tiers.tier(q_score, imm_score)

    return {
        "symbol": symbol,
        "quality": q_score,
        "imminence": imm_score,
        "tier": tier_label,
        "age_bars": age_bars,
        "ema_stage": stage,
        "vol_phase": indicators.volume_phase(df),
        "rs_char": rs_char,
        "cmf": round(cmf_today, 3),
        "deliv_trend": deliv_trend_label or "UNKNOWN",
        "prebreak_count": prebreak_count,
    }


def find_previous_csv(as_of: str) -> str | None:
    """Most recent results/*-consolidation.csv strictly before as_of. Globbing
    existing files (rather than assuming yesterday's calendar date exists) skips
    weekends/holidays automatically."""
    if not os.path.isdir(RESULTS_DIR):
        return None
    candidates = sorted(
        f for f in os.listdir(RESULTS_DIR)
        if f.endswith("-consolidation.csv") and f[:10] < as_of
    )
    return os.path.join(RESULTS_DIR, candidates[-1]) if candidates else None


def compute_transitions(rows: list[dict], as_of: str) -> dict:
    prev_path = find_previous_csv(as_of)
    prev_tiers = {}
    if prev_path:
        prev_df = pd.read_csv(prev_path)
        prev_tiers = dict(zip(prev_df["symbol"], prev_df["tier"]))

    curr_symbols = {r["symbol"] for r in rows}
    promoted, demoted = [], []
    for r in rows:
        prev_t = prev_tiers.get(r["symbol"])
        if prev_t is None:
            continue
        if _TIER_RANK[r["tier"]] > _TIER_RANK.get(prev_t, 0):
            promoted.append(r["symbol"])
        elif _TIER_RANK[r["tier"]] < _TIER_RANK.get(prev_t, 0):
            demoted.append(r["symbol"])
    abandoned = [sym for sym in prev_tiers if sym not in curr_symbols]
    return {"promoted": promoted, "demoted": demoted, "abandoned": abandoned}


def build_markdown(rows: list[dict], as_of: str, transitions: dict) -> str:
    sorted_rows = sorted(rows, key=lambda r: (-_TIER_RANK[r["tier"]], -r["imminence"]))
    lines = [f"## Consolidation Scan — {as_of}", ""]
    lines.append(f"**Promotions:** {', '.join(transitions['promoted']) or 'none'}")
    lines.append(f"**Demotions:** {', '.join(transitions['demoted']) or 'none'}")
    lines.append(f"**Abandoned:** {', '.join(transitions['abandoned']) or 'none'}")
    lines.append("")
    if sorted_rows:
        lines.append("| " + " | ".join(COLUMNS) + " |")
        lines.append("|" + "---|" * len(COLUMNS))
        for r in sorted_rows:
            lines.append("| " + " | ".join(str(r[c]) for c in COLUMNS) + " |")
    else:
        lines.append("*No signals.*")
    lines.append("")
    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


def run(universe_df: pd.DataFrame, as_of: str) -> pd.DataFrame:
    """Spec's required interface. universe_df must have a 'symbol' column."""
    symbols = universe_df["symbol"].tolist()
    all_data = load_ohlc_many(symbols + [BENCH_SYM], lookback=600)
    bench_df = all_data.pop(BENCH_SYM, None)

    rows = []
    for sym, sym_df in all_data.items():
        result = analyse(sym, sym_df, bench_df)
        if result:
            rows.append(result)

    return pd.DataFrame(rows, columns=COLUMNS)


def main() -> None:
    os.makedirs(RESULTS_DIR, exist_ok=True)
    os.makedirs(MD_DIR, exist_ok=True)
    as_of = datetime.now(IST).strftime("%Y-%m-%d")

    print("Fetching universe from TradingView screener...")
    symbols = get_universe()
    print(f"  {len(symbols)} stocks after screener filters")

    universe_df = pd.DataFrame({"symbol": symbols})
    result_df = run(universe_df, as_of)
    print(f"  {len(result_df)} stocks passed EMA+squeeze gates")

    rows = result_df.to_dict("records")
    transitions = compute_transitions(rows, as_of)

    csv_path = os.path.join(RESULTS_DIR, f"{as_of}-consolidation.csv")
    result_df.to_csv(csv_path, index=False)

    md = build_markdown(rows, as_of, transitions)
    with open(os.path.join(MD_DIR, "consolidation_scan_latest.md"), "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(os.path.join(MD_DIR, f"consolidation_scan_{as_of}.md"), "w", encoding="utf-8") as fh:
        fh.write(md)

    print(f"  Saved -> {csv_path}")
    print("  Saved -> consolidation_scans/consolidation_scan_latest.md")


if __name__ == "__main__":
    main()
```

Note on Step 3's `analyse()`: `sig4` in `imminence_score()` reuses `bb_breathe` directly (spec's signal ④ and the standalone "BB breathing" component are the same underlying condition — see design doc's Section 2 note on intentional overlap in the spec's own composite scoring).

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_consolidation_scanner.py -v`
Expected: PASS (7 tests)

- [ ] **Step 5: Run the full test suite to confirm no regressions**

Run: `pytest tests/ -v`
Expected: PASS (all existing tests + all new consolidation tests)

- [ ] **Step 6: Commit**

```bash
git add consolidation/consolidation_scanner.py tests/test_consolidation_scanner.py
git commit --no-verify -m "feat: add consolidation scanner orchestration + CSV/MD output"
```

---

### Task 7: TradingView validation gate (manual, Sec 0 — non-negotiable)

**Files:**
- Create: `consolidation/validation_notes.md` (records the manual comparison — not a generated artifact, a one-time human checklist result, so it's exempt from the "never hand-edit generated output" rule and does NOT need the SEBI disclaimer since it's an internal dev note, not a user-facing scan output)

This task has no automated test — it is the spec's own Sec 0 requirement ("Validate every indicator against TradingView on 2-3 known stocks before universe run") and must be done by a human comparing live chart values, not by an agent guessing numbers.

- [ ] **Step 1: Pick 2-3 liquid stocks currently mid-consolidation**

Run `python -c "from consolidation.consolidation_scanner import get_universe, analyse; from ohlc_db import load_ohlc_many; syms = get_universe(); data = load_ohlc_many(syms + ['NIFTY MIDSML 400'], lookback=600); bench = data.pop('NIFTY MIDSML 400'); hits = [(s, analyse(s, d, bench)) for s, d in data.items()]; hot = [h for h in hits if h[1]]; print(len(hot)); [print(h[0], h[1]) for h in hot[:5]]"` and note 2-3 symbols that pass both gates.

- [ ] **Step 2: Compare EMA/BB/KC values against TradingView charts**

For each picked symbol, open `https://in.tradingview.com/chart/?symbol=NSE:<SYMBOL>` and add:
- EMA(50), EMA(100), EMA(200) — compare today's plotted values against `df["ema50"/"ema100"/"ema200"].iloc[-1]` from a quick `python -c` printout
- Bollinger Bands (20, 2.0) — compare `bb_upper`/`bb_lower` against the chart's plotted band
- Keltner Channels (20, 1.5, SMA ATR) — TradingView's default KC uses EMA basis, not SMA; when adding the indicator, set basis to SMA to match `bollinger_keltner()`'s SMA-basis KC, or note the expected divergence if left on EMA basis

Record each symbol's comparison (values within ~0.1% tolerance, matching float rounding) in `consolidation/validation_notes.md`.

- [ ] **Step 3: Compare RS line manually**

For each symbol, verify `(stock_close / NIFTY_MIDSML_400_close)` at the latest weekly close matches the direction (rising/falling) visible on a TradingView RS comparison chart (`<SYMBOL>/NIFTY MIDSML 400` ratio chart). Exact scale won't match (spec doesn't fix RS to a particular multiplier here) — only the direction and EMA9 relationship need to agree.

- [ ] **Step 4: Write the validation notes file and commit**

```markdown
# Consolidation Scanner — TradingView Validation Notes

Validated per spec Sec 0 before the first universe run.

## Symbols checked
<!-- fill in during Step 1-3: symbol, date checked, EMA/BB/KC/RS match y/n, notes -->

## Outcome
<!-- PASS / issues found + fixes made -->
```

```bash
git add consolidation/validation_notes.md
git commit --no-verify -m "docs: record TradingView validation of consolidation scanner indicators"
```

---

### Task 8: PowerShell runner + CLAUDE.md integration

**Files:**
- Create: `run_consolidation_scanner.ps1`
- Modify: `CLAUDE.md` (add to the "Running the scanners" list, and add a "Scanner pipeline — Consolidation Tracker" section under Architecture overview)

**Interfaces:**
- Consumes: `consolidation/consolidation_scanner.py`'s `main()` (invoked via `python consolidation\consolidation_scanner.py`, which works because Task 6's file inserts the repo root onto `sys.path` before importing sibling package modules)

- [ ] **Step 1: Create the PowerShell runner**

```powershell
# run_consolidation_scanner.ps1 — Consolidation Tracker (Phase 1+2)
# Run after 4:05 PM IST on trading days (after run_fetch_data.ps1).
# Logs: logs/consolidation_scanner_YYYY-MM-DD.log

$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\consolidation_scanner_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== CONSOLIDATION_SCANNER START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\consolidation\consolidation_scanner.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
& git -C C:\Users\satya\nse_circuit_limits add results consolidation_scans 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "[scan $date] consolidation: scan run" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "--- Done ---"

# To register the scheduled task (run once as admin):
# schtasks /create /tn "NSE_ConsolidationScanner" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_consolidation_scanner.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:35 /f
```

- [ ] **Step 2: Add CLAUDE.md entries**

In the "Running the scanners" PowerShell block, add after the `run_trend_scanner.ps1` line:
```
.\run_consolidation_scanner.ps1  # 4:35 PM — Consolidation Tracker: quality/imminence/tier scan
```

Under "Architecture overview", add a new subsection after "### Scanner pipeline — Weekly ZL (`weekly_zl_scanner.py`)":

```markdown
### Scanner pipeline — Consolidation Tracker (`consolidation/`)

Phase 1+2 of `research/consolidation_capital_efficiency_spec.md` (full spec covers 7 phases;
only indicators+quality+imminence+tiers+scanner are built — see
`docs/superpowers/specs/2026-07-05-consolidation-scanner-phase1-2-design.md`).

1. `indicators.py` — EMA compression (Sec 2.1), BB/KC squeeze (Sec 2.2), volume exhaustion
   (Sec 2.3), RS character (Sec 2.4)
2. `quality.py` — 0-100 quality score (Sec 3): BB depth + EMA stage + vol exhaustion +
   RS character + CMF (reuses `ohlc_db.cmf_series()`) + delivery% trend (reuses
   `ohlc_db.load_delivery()`)
3. `imminence.py` — 0-100 imminence score + 6 pre-break signals (Sec 4)
4. `tiers.py` — COLD/WARM/HOT tier lookup + stateless `consolidation_age`/quality-peak-drawdown
   (backward-scan over historical OHLC, no DB) + abandonment checks (Sec 5)
5. `consolidation_scanner.py` — `run(universe_df, as_of) -> pd.DataFrame`; own TradingView
   universe query (mcap 1,000–5,00,000 Cr, price > ₹50, mirrors `wt_bullcross_scanner.py`);
   writes `results/YYYY-MM-DD-consolidation.csv` (Layer 1 → future Pine Layer 2 contract) +
   `consolidation_scans/consolidation_scan_latest.md`

Gate: EMA dual gate AND BB squeeze gate only — volume/RS are scored, not filtered on.
Out of scope for this phase: capital/time-stops/regime-throttle (Sec 6/8/9), catalyst
calendar (Sec 7), PineScript companion (Sec 12), half-life backtest (Sec 10).
```

- [ ] **Step 3: Commit**

```bash
git add run_consolidation_scanner.ps1 CLAUDE.md
git commit --no-verify -m "chore: add consolidation scanner PS1 runner + CLAUDE.md integration"
```

---

## Self-Review Notes

**Spec coverage:** Sec 2.1(Task1) 2.2(Task1) 2.3(Task2) 2.4(Task2) 2.5(Task3, via `ohlc_db.cmf_series`) 2.6(Task3) 3(Task3) 4(Task4) 5(Task5) 0(Task7, Task6's `MIN_BARS`/no-look-ahead) 11(Task6 columns, trimmed per design doc) — all covered. Sec 6/7/8/9/10/12 confirmed out of scope per the design doc.

**Placeholder scan:** no TBD/TODO; `validation_notes.md`'s template blanks are intentionally filled in by the human executing Task 7's Steps 1-3, not left as plan placeholders.

**Type consistency:** `ema_stage()` vocabulary (`STAGE_1_CONVERGING/STAGE_2_COMPRESSED/STAGE_3_DIVERGING`) and `classify_rs_character()` vocabulary (`CHAR_1..5`) defined in Task 1/2 match the dict keys used in Task 3's `quality_score()` and Task 5's `tiers.py` exactly. `COLUMNS` list defined once in Task 6, reused by `build_markdown()` and asserted against in Task 6's tests.
