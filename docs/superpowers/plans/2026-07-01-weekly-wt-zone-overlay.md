# Weekly WT Zone Overlay — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Surface weekly WaveTrend bull-cross zone context in the daily WT scanner output and as a Pine Script daily chart background overlay.

**Architecture:** A standalone `weekly_wt_zone(df)` function in `wavetrend_scanner.py` resamples daily OHLCV to weekly, computes WT using the same math as `WaveTrendCalculator`, and returns `(in_zone: bool, days: int)`. The scanner calls it per stock and injects `W↑Nd` into the symbol link text. A separate Pine Script indicator shades the daily chart background using `request.security` weekly WT.

**Tech Stack:** Python 3.11+, pandas, pytest; Pine Script v6.

## Global Constraints

- All Python follows existing codebase patterns: `adjust=False` for EMA, `min_periods=period` for SMA.
- `date` column from `load_ohlc()` is a plain string `YYYY-MM-DD`, not datetime — always convert before resampling.
- Weekly resample key: `W-FRI` (NSE trades Mon–Fri; weekly bar label = Friday of that week).
- Pine Script: `@version=6`. No float equality (`==`). Use `ta.crossover`/`ta.crossunder`.
- No new Python modules — `weekly_wt_zone` goes into `wavetrend_scanner.py`.
- WT params must stay in sync with `Satya_WT_CROSS_LB_v2`: n1=10, n2=21, wt2=SMA(wt1, 4).
- Tests: pytest, no fixtures, no frameworks — plain functions with synthetic DataFrames.

---

### Task 1: `weekly_wt_zone()` — implement and test

**Files:**
- Modify: `wavetrend_scanner.py` (append function after `scan_universe`)
- Create: `tests/test_weekly_wt_zone.py`

**Interfaces:**
- Produces: `weekly_wt_zone(df: pd.DataFrame, n1: int = 10, n2: int = 21) -> tuple[bool, int]`
  - `df`: daily OHLCV with columns `date` (str), `open`, `high`, `low`, `close`, `volume`; oldest-first
  - returns `(True, N)` when current bar is in an active weekly bull-cross zone; `N` = trading days since Monday of the cross week (inclusive)
  - returns `(False, 0)` otherwise

- [ ] **Step 1: Create test file with a helper to build synthetic daily OHLCV**

Create `tests/test_weekly_wt_zone.py`:

```python
"""
tests/test_weekly_wt_zone.py
Unit tests for weekly_wt_zone() in wavetrend_scanner.py.
"""
import sys
from pathlib import Path
from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

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
    return pd.DataFrame({
        "date": dates,
        "open": c * 0.99,
        "high": c * 1.01,
        "low":  c * 0.98,
        "close": c,
        "volume": np.ones(n) * 1_000_000,
    })


def _bull_then_hold(n_decline=300, n_rise=150) -> np.ndarray:
    """Decline → reversal → flat. Reliably produces a weekly bull cross."""
    return np.concatenate([
        np.linspace(100, 40, n_decline),
        np.linspace(40, 90, n_rise),
    ])


def _bull_then_bear(n_decline=300, n_rise=100, n_decline2=120) -> np.ndarray:
    """Decline → reversal → decline again. Bull cross followed by bear cross."""
    return np.concatenate([
        np.linspace(100, 40, n_decline),
        np.linspace(40, 90, n_rise),
        np.linspace(90, 30, n_decline2),
    ])
```

- [ ] **Step 2: Write failing test — in-zone returns True with positive day count**

Append to `tests/test_weekly_wt_zone.py`:

```python
def test_in_zone_returns_true_with_positive_days():
    """Bull cross with no subsequent bear cross → (True, N>0)."""
    df = _make_df(_bull_then_hold())
    in_zone, days = weekly_wt_zone(df)
    assert in_zone is True
    assert days > 0
    assert days <= 160  # rise portion is 150 bars + small EMA lag buffer


def test_bear_cross_after_bull_ends_zone():
    """Bull cross followed by bear cross → (False, 0)."""
    df = _make_df(_bull_then_bear())
    in_zone, days = weekly_wt_zone(df)
    assert in_zone is False
    assert days == 0


def test_no_cross_returns_false():
    """Monotone decline — no bull cross ever → (False, 0)."""
    prices = np.linspace(100, 10, 400)
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
```

- [ ] **Step 3: Run tests to confirm they FAIL**

```
cd c:\Users\satya\nse_circuit_limits
pytest tests/test_weekly_wt_zone.py -v
```

Expected: `ImportError: cannot import name 'weekly_wt_zone'` or `AttributeError`.

- [ ] **Step 4: Find insertion point in `wavetrend_scanner.py`**

Read the bottom of `wavetrend_scanner.py` to find a clean place after `scan_universe`:

```
grep -n "^def \|^class " wavetrend_scanner.py
```

Append `weekly_wt_zone` after the last top-level function.

- [ ] **Step 5: Implement `weekly_wt_zone()` in `wavetrend_scanner.py`**

Append to `wavetrend_scanner.py` (after the last function, before any `if __name__` block):

```python
# ══════════════════════════════════════════════════════════════════════════════
# WEEKLY WT ZONE
# ══════════════════════════════════════════════════════════════════════════════

def weekly_wt_zone(
    df: pd.DataFrame,
    n1: int = 10,
    n2: int = 21,
) -> tuple[bool, int]:
    """
    Detect whether the current daily bar is inside an active weekly WT bull-cross zone.

    Zone starts: first daily bar of the week a weekly bull cross (wt1 crossover wt2) formed.
    Zone ends:   first daily bar of the week a weekly bear cross (wt1 crossunder wt2) formed.
    Cross level: any bull cross (wt1 > wt2, prev wt1 <= prev wt2) — no level filter.

    Parameters
    ----------
    df  : Daily OHLCV DataFrame from load_ohlc(). Columns: date (str YYYY-MM-DD),
          open, high, low, close, volume. Oldest row first.
    n1  : Channel length (EMA period). Default 10 — matches Satya_WT_CROSS_LB_v2.
    n2  : Average length (EMA period). Default 21 — matches Satya_WT_CROSS_LB_v2.

    Returns
    -------
    (in_zone, days_since_cross)
        in_zone          : True if current bar is in an active weekly bull-cross zone.
        days_since_cross : Trading days from Monday of the cross week (inclusive) to today.
                           0 when in_zone is False.
    """
    MIN_WEEKLY = n1 + n2 + 10  # ~41 weekly bars = ~205 daily bars for stable warmup

    # ── 1. Parse dates and resample daily → weekly ──────────────────────────
    daily = df.copy()
    daily["date"] = pd.to_datetime(daily["date"])
    daily = daily.set_index("date").sort_index()

    wk = daily.resample("W-FRI").agg(
        open=("open", "first"),
        high=("high", "max"),
        low=("low", "min"),
        close=("close", "last"),
        volume=("volume", "sum"),
    ).dropna(subset=["close"])

    if len(wk) < MIN_WEEKLY:
        return False, 0

    # ── 2. Compute weekly WaveTrend (same math as WaveTrendCalculator) ──────
    ap  = (wk["high"] + wk["low"] + wk["close"]) / 3
    esa = ap.ewm(span=n1, adjust=False).mean()
    d   = (ap - esa).abs().ewm(span=n1, adjust=False).mean()
    ci  = (ap - esa) / (0.015 * d)
    wt1 = ci.ewm(span=n2, adjust=False).mean()
    wt2 = wt1.rolling(4, min_periods=4).mean()

    # Drop rows where wt2 is NaN (warmup period)
    valid_idx = wt2.dropna().index
    if len(valid_idx) < 3:
        return False, 0

    wt1v = wt1.loc[valid_idx]
    wt2v = wt2.loc[valid_idx]

    # ── 3. Detect weekly crosses ─────────────────────────────────────────────
    bull_cross = (wt1v > wt2v) & (wt1v.shift(1) <= wt2v.shift(1))
    bear_cross = (wt1v < wt2v) & (wt1v.shift(1) >= wt2v.shift(1))

    bull_dates = bull_cross[bull_cross].index
    if len(bull_dates) == 0:
        return False, 0

    last_bull = bull_dates[-1]  # Friday of the cross week (W-FRI label)

    # ── 4. Check no bear cross after the last bull cross ─────────────────────
    bear_after = bear_cross.loc[bear_cross.index > last_bull]
    if bear_after.any():
        return False, 0

    # ── 5. Count daily bars from Monday of the cross week (inclusive) ────────
    # W-FRI label is Friday; Monday of that week = Friday - 4 calendar days.
    cross_week_monday = last_bull - pd.Timedelta(days=4)
    days_in_zone = int((daily.index >= cross_week_monday).sum())

    return True, days_in_zone
```

- [ ] **Step 6: Run tests to confirm they PASS**

```
cd c:\Users\satya\nse_circuit_limits
pytest tests/test_weekly_wt_zone.py -v
```

Expected output:
```
tests/test_weekly_wt_zone.py::test_in_zone_returns_true_with_positive_days PASSED
tests/test_weekly_wt_zone.py::test_bear_cross_after_bull_ends_zone PASSED
tests/test_weekly_wt_zone.py::test_no_cross_returns_false PASSED
tests/test_weekly_wt_zone.py::test_insufficient_data_returns_false PASSED
tests/test_weekly_wt_zone.py::test_days_count_is_nonnegative_integer PASSED
5 passed
```

- [ ] **Step 7: Commit**

```bash
git add wavetrend_scanner.py tests/test_weekly_wt_zone.py
git commit -m "feat: add weekly_wt_zone() to wavetrend_scanner"
git push
```

---

### Task 2: Scanner integration — `wt_bullcross_scanner.py`

**Files:**
- Modify: `wt_bullcross_scanner.py`

**Interfaces:**
- Consumes: `weekly_wt_zone(df: pd.DataFrame, n1: int = 10, n2: int = 21) -> tuple[bool, int]` from Task 1
- Produces: Symbol column entries like `[SJVN W↑12d](link)` when `weekly_zone=True`

- [ ] **Step 1: Update import line**

In `wt_bullcross_scanner.py`, find:
```python
from wavetrend_scanner import WaveTrendCalculator
```
Replace with:
```python
from wavetrend_scanner import WaveTrendCalculator, weekly_wt_zone
```

- [ ] **Step 2: Call `weekly_wt_zone` in `analyse()`**

In `wt_bullcross_scanner.py`, inside `analyse()`, find the line:
```python
        squeeze = _bb_kc_squeeze(df_raw)
```

Add immediately after it:
```python
        wz_in, wz_days = weekly_wt_zone(df_raw)
```

- [ ] **Step 3: Add weekly zone fields to the return dict**

In `analyse()`, find the return dict. Add two fields after `"squeeze": squeeze,`:
```python
            "weekly_zone":      wz_in,
            "weekly_zone_days": wz_days,
```

The full return dict should include (among existing fields):
```python
        return {
            "symbol": symbol,
            # ... existing fields ...
            "squeeze": squeeze,
            "weekly_zone":      wz_in,
            "weekly_zone_days": wz_days,
            "rs_state": rs,
            # ... rest of fields ...
        }
```

- [ ] **Step 4: Update `_row()` to append `W↑Nd` to the symbol label**

In `_row()`, find:
```python
    sym_label = f"{sym} ★" if trend_syms and sym in trend_syms else sym
```

Replace with:
```python
    sym_label = sym
    if f.get("weekly_zone"):
        sym_label += f" W↑{f['weekly_zone_days']}d"
    if trend_syms and sym in trend_syms:
        sym_label += " ★"
```

> Note: `↑` = ↑, `★` = ★. Explicit Unicode escapes prevent encoding issues on Windows.

- [ ] **Step 5: Update scan definition table**

In `build_markdown()`, find the scan definition table lines. Add one row after the `| Min rank |` row:

```python
        "| W↑Nd in Symbol | Days in weekly WT bull-cross zone (any cross; ends on weekly bear cross) |",
```

The definition table block starts with `"### Scan definition"`. The new row goes at the end of the `|--------|-------|` block, before `""` or `"---"`.

- [ ] **Step 6: Smoke-test the scanner output manually**

Run:
```
cd c:\Users\satya\nse_circuit_limits
python wt_bullcross_scanner.py 2>&1 | head -60
```

Check:
- No exceptions
- `W↑Nd` appears in at least some symbol cells (e.g. `[SJVN W↑12d](...)`)
- Symbols without a weekly zone render without `W↑`
- Symbols that are both trend leaders and in weekly zone show both: `[SJVN W↑12d ★](...)`

- [ ] **Step 7: Commit**

```bash
git add wt_bullcross_scanner.py
git commit -m "feat: add weekly WT zone flag W↑Nd to wt_bullcross scanner symbol column"
git push
```

---

### Task 3: Pine Script — `Satya_WT_Weekly_Zone_Overlay.pine`

**Files:**
- Create: `C:\Users\satya\Downloads\WaveTrend\Satya_WT_Weekly_Zone_Overlay.pine`

**Interfaces:**
- Companion to: `Satya_WT_CROSS_LB_v2.pine` (keep n1/n2 params in sync)
- No Python dependencies

- [ ] **Step 1: Create the Pine Script file**

Create `C:\Users\satya\Downloads\WaveTrend\Satya_WT_Weekly_Zone_Overlay.pine`:

```pine
//@version=6
// ============================================================
// Satya WT Weekly Zone Overlay
// Add as a SEPARATE indicator on the daily price chart (overlay=true).
// Replicates weekly WaveTrend via request.security and shades the
// daily chart background when the weekly WT is in an active bull-cross
// zone (weekly wt1 crossed above wt2, no bear cross since).
//
// Zone start: first daily bar AFTER the weekly bull cross candle closes
//             (lookahead_off — no look-ahead bias; one-week visual delay).
// Zone end:   first daily bar after the weekly bear cross candle closes.
//
// To shade from the exact cross week instead (display-only, no backtesting):
//   change lookahead=barmerge.lookahead_off  →  barmerge.lookahead_on
//
// Companion indicator: Satya_WT_CROSS_LB_v2
// Alert message format: "WT_WEEKLY_ZONE|{{ticker}}|zone_start|{{interval}}"
// ============================================================

indicator(
    title     = "Satya WT Weekly Zone Overlay",
    shorttitle= "Satya_WT_WklyZone",
    overlay   = true,
    max_labels_count = 500)

// ════════════════════════════════════════════════════════════
// INPUTS — keep n1/n2 in sync with Satya_WT_CROSS_LB_v2
// ════════════════════════════════════════════════════════════

n1         = input.int(10,  "Channel Length",  minval=1, group="WaveTrend (match v2)")
n2         = input.int(21,  "Average Length",  minval=1, group="WaveTrend (match v2)")

crossLevel = input.string(
    "Any",
    "Min cross level for zone start",
    options=["Any", "Oversold L2 (wt2 ≤ -53)", "Oversold L1 (wt2 ≤ -60)"],
    group="Zone Filter")

zoneColor  = input.color(color.new(color.green, 85), "Zone background color", group="Display")
showLabel  = input.bool(true,  "Show W↑ label on zone start bar",             group="Display")

// ════════════════════════════════════════════════════════════
// WEEKLY WAVETREND via request.security
// ════════════════════════════════════════════════════════════

f_wt() =>
    ap  = hlc3
    esa = ta.ema(ap, n1)
    d   = ta.ema(math.abs(ap - esa), n1)
    ci  = (ap - esa) / (0.015 * d)
    wt1 = ta.ema(ci, n2)
    wt2 = ta.sma(wt1, 4)
    [wt1, wt2]

[wt1_w, wt2_w] = request.security(
    syminfo.tickerid, "W", f_wt(),
    lookahead = barmerge.lookahead_off)

// ════════════════════════════════════════════════════════════
// CROSS CONDITIONS (weekly)
// ════════════════════════════════════════════════════════════

bullCrossAny_w = ta.crossover(wt1_w, wt2_w)
bearCrossAny_w = ta.crossunder(wt1_w, wt2_w)

bullCross_w = switch crossLevel
    "Oversold L1 (wt2 ≤ -60)" => bullCrossAny_w and wt2_w <= -60
    "Oversold L2 (wt2 ≤ -53)" => bullCrossAny_w and wt2_w <= -53
    =>                            bullCrossAny_w

// ════════════════════════════════════════════════════════════
// ZONE STATE
// ════════════════════════════════════════════════════════════

var bool inZone = false
if bullCross_w
    inZone := true
if bearCrossAny_w
    inZone := false

// ════════════════════════════════════════════════════════════
// BACKGROUND + LABEL
// ════════════════════════════════════════════════════════════

bgcolor(inZone ? zoneColor : na, title = "Weekly WT Bull Zone")

if showLabel and bullCross_w
    label.new(
        bar_index, high,
        "W↑",
        style     = label.style_label_up,
        color     = color.new(color.green, 50),
        textcolor = color.white,
        size      = size.small)
```

- [ ] **Step 2: Manual TradingView verification**

Open TradingView on any NSE stock (e.g. HDFCBANK daily chart). Add indicator from file. Verify:

1. Green background shading appears on historical bars where weekly WT was in a bull-cross zone.
2. "W↑" label appears at zone start bars.
3. Shading stops at bars where weekly bear cross occurred.
4. Changing "Min cross level" to "Oversold L1 (wt2 ≤ -60)" reduces the number of zones.
5. Changing `lookahead_off` → `lookahead_on` shifts zone start ~1 week earlier (exact cross week).
6. No Pine Script compilation errors.

- [ ] **Step 3: Commit**

```bash
git add "C:/Users/satya/Downloads/WaveTrend/Satya_WT_Weekly_Zone_Overlay.pine"
```

> Note: Pine files in Downloads are not in the repo. If you want the file tracked, copy it to the repo root or a `pine_scripts/` directory first, then `git add`.

Alternatively, commit a copy into the repo:
```bash
cp "C:/Users/satya/Downloads/WaveTrend/Satya_WT_Weekly_Zone_Overlay.pine" \
   /c/Users/satya/nse_circuit_limits/pine_scripts/Satya_WT_Weekly_Zone_Overlay.pine
git add pine_scripts/Satya_WT_Weekly_Zone_Overlay.pine
git commit -m "feat: Satya WT Weekly Zone Overlay Pine Script indicator"
git push
```

---

## Self-Review Checklist

- [x] `weekly_wt_zone()` fully spec-covered (Task 1)
- [x] Import update explicit (Task 2 Step 1)
- [x] `analyse()` return dict update shown in full context (Task 2 Steps 2–3)
- [x] `_row()` replacement shown with Unicode escapes to avoid Windows encoding issues (Task 2 Step 4)
- [x] Scan def table update shown (Task 2 Step 5)
- [x] Pine Script includes all inputs: n1/n2, crossLevel, zoneColor, showLabel (Task 3)
- [x] Pine Script uses `switch` for crossLevel (cleaner than ternary chain in v6)
- [x] Lookahead tradeoff documented in Pine header comment
- [x] Pine repo tracking path noted (Downloads vs repo)
- [x] No TBD/TODO/placeholders
