# CMF Zero-Cross Symbol Marker Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a Chaikin Money Flow (CMF) zero-line-cross recency marker (`↑CMF3d` / `↓CMF7d`) to the Symbol column of every scanner that already computes `liq_tag()`, plus a companion Pine v6 chart indicator.

**Architecture:** One shared pair of functions (`cmf_days`, `cmf_tag`) added to `ohlc_db.py` next to `liq_tag()`. Each of the 5 scanners already calls `liq_tag(df)` once per symbol inside its per-stock analysis function and stores the result in the finding dict — `cmf_tag(df)` is called alongside it the same way. Each scanner's markdown row-builder then reads `f["cmf_tag"]` and appends it into the Symbol cell.

**Tech Stack:** Python (pandas, numpy), Pine Script v6.

## Global Constraints

- `@version=6` mandatory in the new Pine file, full header comment block (what it does, companion pairing, alert format) — from `pine-script-conventions.md`.
- No float equality anywhere — use `>`/`<=` boundary comparisons or `ta.crossover`/`ta.crossunder` in Pine, never `== 0.0` — from `pine-script-conventions.md`.
- No look-ahead bias: CMF at bar N uses only bars `0..N` (rolling window ending at current bar) — from `backtesting-integrity.md`.
- `ohlc_db.py` is the only data entry point for scanners — no new CSV/API reads — from `scanner-conventions.md`.
- Signal rank numbers (WaveTrend etc.) are an external contract — this feature does not touch any rank constant, so N/A here, but no task may renumber one incidentally.

---

## Task 1: CMF core functions in `ohlc_db.py`

**Files:**
- Modify: `ohlc_db.py` (add `import numpy as np` near top; add two functions after `liq_tag()`, i.e. after line 203)
- Test: `tests/test_cmf.py` (new)

**Interfaces:**
- Produces: `cmf_days(df: pd.DataFrame, n: int = 20, cap: int = 30) -> tuple[bool, int] | None` and `cmf_tag(df: pd.DataFrame, n: int = 20, cap: int = 30) -> str` — both imported by name from `ohlc_db` in Tasks 2–6.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_cmf.py`:

```python
import pandas as pd

from ohlc_db import cmf_days, cmf_tag


def _synthetic_cross_df() -> pd.DataFrame:
    """6 bars with MFM=-1 (close=low) then 6 bars with MFM=+1 (close=high).
    Constant volume=100 makes CMF(n=5) equal the rolling average of MFM,
    giving a deterministic zero-cross 3 bars before the last bar.
    """
    rows = []
    for _ in range(6):
        rows.append({"open": 100.0, "high": 110.0, "low": 100.0, "close": 100.0, "volume": 100.0})
    for _ in range(6):
        rows.append({"open": 110.0, "high": 110.0, "low": 100.0, "close": 110.0, "volume": 100.0})
    return pd.DataFrame(rows)


def test_cmf_days_detects_zero_cross():
    df = _synthetic_cross_df()
    assert cmf_days(df, n=5, cap=30) == (True, 3)


def test_cmf_tag_formats_marker():
    df = _synthetic_cross_df()
    assert cmf_tag(df, n=5, cap=30) == "↑CMF3d"


def test_cmf_days_zero_range_bar_no_crash():
    rows = [
        {"open": 100.0, "high": 100.0, "low": 100.0, "close": 100.0, "volume": 100.0}
        for _ in range(10)
    ]
    df = pd.DataFrame(rows)
    result = cmf_days(df, n=5, cap=30)
    assert result is not None
    positive, days = result
    assert isinstance(positive, bool)
    assert isinstance(days, int)


def test_cmf_days_insufficient_bars_returns_none():
    rows = [
        {"open": 100.0, "high": 110.0, "low": 100.0, "close": 105.0, "volume": 100.0}
        for _ in range(3)
    ]
    df = pd.DataFrame(rows)
    assert cmf_days(df, n=20, cap=30) is None
    assert cmf_tag(df, n=20, cap=30) == ""
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_cmf.py -v`
Expected: FAIL with `ImportError: cannot import name 'cmf_days' from 'ohlc_db'`

- [ ] **Step 3: Add `import numpy as np` to `ohlc_db.py`**

Current top of file (line 14-17):
```python
import sqlite3
from pathlib import Path

import pandas as pd
```

Change to:
```python
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd
```

- [ ] **Step 4: Implement `cmf_days` and `cmf_tag`**

Insert immediately after `liq_tag()` (after the line `        return ""` that closes it, currently line 203):

```python
def cmf_days(df: pd.DataFrame, n: int = 20, cap: int = 30) -> tuple[bool, int] | None:
    """Chaikin Money Flow zero-line-cross recency.
    Returns (cmf_positive, bars_since_zero_cross), bars_ago capped at `cap`.
    None if fewer than n + 2 bars.
    No float equality: cross = sign flip via > / <= boundary, mirrors
    zl25_stats()'s bars-ago scan pattern.
    """
    if len(df) < n + 2:
        return None

    high = df["high"].astype(float)
    low = df["low"].astype(float)
    close = df["close"].astype(float)
    volume = df["volume"].astype(float)

    range_ = high - low
    mfm = np.where(range_ > 0, ((close - low) - (high - close)) / range_, 0.0)
    mfv = pd.Series(mfm, index=df.index) * volume

    cmf = (
        mfv.rolling(n, min_periods=n).sum()
        / volume.rolling(n, min_periods=n).sum()
    ).dropna().reset_index(drop=True)

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


def cmf_tag(df: pd.DataFrame, n: int = 20, cap: int = 30) -> str:
    """Formats cmf_days() -> '↑CMF{d}d' / '↓CMF{d}d'. '' on None or error."""
    try:
        result = cmf_days(df, n=n, cap=cap)
        if result is None:
            return ""
        positive, days = result
        arrow = "↑" if positive else "↓"
        return f"{arrow}CMF{days}d"
    except Exception:
        return ""
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `pytest tests/test_cmf.py -v`
Expected: 4 passed

- [ ] **Step 6: Commit**

```bash
git add ohlc_db.py tests/test_cmf.py
git commit -m "feat: add CMF zero-cross recency helper (cmf_days, cmf_tag)"
```

---

## Task 2: Wire into `wt_bullcross_scanner.py`

**Files:**
- Modify: `wt_bullcross_scanner.py:35` (import), `:381` (finding dict), `:421-436` (`_row` extras)

**Interfaces:**
- Consumes: `cmf_tag(df: pd.DataFrame, n=20, cap=30) -> str` from Task 1.

- [ ] **Step 1: Import `cmf_tag`**

Current line 35:
```python
from ohlc_db import load_ohlc_many, get_names, liq_tag
```
Change to:
```python
from ohlc_db import load_ohlc_many, get_names, liq_tag, cmf_tag
```

- [ ] **Step 2: Store `cmf_tag` in the finding dict**

Current line 381:
```python
            "liq_tag": liq_tag(df_raw),
```
Change to:
```python
            "liq_tag": liq_tag(df_raw),
            "cmf_tag": cmf_tag(df_raw),
```

- [ ] **Step 3: Append marker to the Symbol cell extras**

Current (lines 421-436):
```python
    extras = []
    if f.get("rs_weekly_gate"):
        extras.append("📶W9")
    if f.get("weekly_zone"):
        extras.append(f"W↑{f['weekly_zone_days']}d")
    rvol, ss = f.get("rvol", 0.0), f.get("strong_start", False)
    if ss and rvol >= RVOL_FLAG:
        extras.append(f"🚀SS·{rvol:.0f}x")
    elif ss:
        extras.append("🚀SS")
    elif rvol >= RVOL_FLAG:
        extras.append(f"RVOL{rvol:.0f}x")
    if trend_syms and sym in trend_syms:
        extras.append("★")
    sym_cell = f"[{sym}]({tv})" + (
        "<br><sub>" + " · ".join(extras) + "</sub>" if extras else ""
    )
```
Change to (adds `cmf_tag` append right before the `sym_cell` assembly):
```python
    extras = []
    if f.get("rs_weekly_gate"):
        extras.append("📶W9")
    if f.get("weekly_zone"):
        extras.append(f"W↑{f['weekly_zone_days']}d")
    rvol, ss = f.get("rvol", 0.0), f.get("strong_start", False)
    if ss and rvol >= RVOL_FLAG:
        extras.append(f"🚀SS·{rvol:.0f}x")
    elif ss:
        extras.append("🚀SS")
    elif rvol >= RVOL_FLAG:
        extras.append(f"RVOL{rvol:.0f}x")
    if trend_syms and sym in trend_syms:
        extras.append("★")
    if f.get("cmf_tag"):
        extras.append(f["cmf_tag"])
    sym_cell = f"[{sym}]({tv})" + (
        "<br><sub>" + " · ".join(extras) + "</sub>" if extras else ""
    )
```

- [ ] **Step 4: Smoke-check the row output**

Run:
```bash
python -c "
from wt_bullcross_scanner import _row
f = {
    'symbol': 'TEST', 'zl_days': 3, 'zl_rising': True, 'zl_pct': 1.5,
    'day_chg': 0.5, 'squeeze': False, 'wt_is_ppv': False,
    'wt1': 10.0, 'wt2': 5.0, 'wt_rank': 1, 'wt_signal': 'BULL_ANY',
    'cmf_tag': '↑CMF3d',
}
row = _row(f, {})
assert '↑CMF3d' in row, row
print('OK:', row)
"
```
Expected: prints `OK: | [TEST](...)<br><sub>↑CMF3d</sub> | ...` (no traceback)

- [ ] **Step 5: Commit**

```bash
git add wt_bullcross_scanner.py
git commit -m "feat: add CMF marker to wt_bullcross_scanner Symbol column"
```

---

## Task 3: Wire into `ema25_zl_scanner.py`

**Files:**
- Modify: `ema25_zl_scanner.py:34` (import), `:257` (finding dict), `:307-316` (`_table_rows`)

**Interfaces:**
- Consumes: `cmf_tag` from Task 1.

- [ ] **Step 1: Import `cmf_tag`**

Current line 34:
```python
from ohlc_db import load_ohlc, get_names, liq_tag
```
Change to:
```python
from ohlc_db import load_ohlc, get_names, liq_tag, cmf_tag
```

- [ ] **Step 2: Store `cmf_tag` in the finding dict**

Current line 257:
```python
            "liq_tag": liq_tag(raw),
```
Change to:
```python
            "liq_tag": liq_tag(raw),
            "cmf_tag": cmf_tag(raw),
```

- [ ] **Step 3: Add Symbol subline**

Current (lines 307-316):
```python
        rows.append(
            f"| [{sym}]({tv}) "
            f"| {zl_d} "
            f"| {zl_p} "
            f"| {lbl_cell} "
            f"| {ds}{f['day_chg']:.2f}% "
            f"| {f['close']:.2f} "
            f"| {sqz} "
            f"| {cl} {em} |"
        )
```
Change to:
```python
        cmf = f.get("cmf_tag", "")
        sym_cell = f"[{sym}]({tv})" + (f"<br><sub>{cmf}</sub>" if cmf else "")
        rows.append(
            f"| {sym_cell} "
            f"| {zl_d} "
            f"| {zl_p} "
            f"| {lbl_cell} "
            f"| {ds}{f['day_chg']:.2f}% "
            f"| {f['close']:.2f} "
            f"| {sqz} "
            f"| {cl} {em} |"
        )
```

- [ ] **Step 4: Smoke-check the row output**

Run:
```bash
python -c "
from ema25_zl_scanner import _table_rows
f = {
    'symbol': 'TEST', 'zl_days': 3, 'zl_pct': 1.2, 'day_chg': 0.4,
    'squeeze': False, 'close': 123.45, 'cmf_tag': '↑CMF3d',
}
rows = _table_rows([f], {})
assert any('↑CMF3d' in r for r in rows), rows
print('OK:', rows[-1])
"
```
Expected: prints `OK: | [TEST](...)<br><sub>↑CMF3d</sub> | ...` (no traceback)

- [ ] **Step 5: Commit**

```bash
git add ema25_zl_scanner.py
git commit -m "feat: add CMF marker to ema25_zl_scanner Symbol column"
```

---

## Task 4: Wire into `weekly_zl_scanner.py`

**Files:**
- Modify: `weekly_zl_scanner.py` (import line, `:244` finding dict, `:301-312` `_table_rows`)

**Interfaces:**
- Consumes: `cmf_tag` from Task 1.

- [ ] **Step 1: Import `cmf_tag`**

Find the existing `from ohlc_db import ... liq_tag` line and add `cmf_tag` to it (same pattern as Task 2/3).

- [ ] **Step 2: Store `cmf_tag` in the finding dict**

Current line 244:
```python
            "liq_tag": liq_tag(daily),
```
Change to:
```python
            "liq_tag": liq_tag(daily),
            "cmf_tag": cmf_tag(daily),
```

- [ ] **Step 3: Add Symbol subline**

Current (lines 301-312):
```python
        rows.append(
            f"| [{sym}]({tv}) "
            f"| {_meta} "
            f"| {f['consec_weeks']}w "
            f"| {pvz} "
            f"| {zl_w} "
            f"| {zl_p} "
            f"| {ds}{f['day_chg']:.2f}% "
            f"| {f['close']:.2f} "
            f"| {sqz} "
            f"| {cl} {em} |"
        )
```
Change to:
```python
        cmf = f.get("cmf_tag", "")
        sym_cell = f"[{sym}]({tv})" + (f"<br><sub>{cmf}</sub>" if cmf else "")
        rows.append(
            f"| {sym_cell} "
            f"| {_meta} "
            f"| {f['consec_weeks']}w "
            f"| {pvz} "
            f"| {zl_w} "
            f"| {zl_p} "
            f"| {ds}{f['day_chg']:.2f}% "
            f"| {f['close']:.2f} "
            f"| {sqz} "
            f"| {cl} {em} |"
        )
```

- [ ] **Step 4: Smoke-check the row output**

Run:
```bash
python -c "
from weekly_zl_scanner import _table_rows
f = {
    'symbol': 'TEST', 'zl_weeks': 2, 'zl_pct': 1.1, 'day_chg': 0.3,
    'sqz_weeks': 0, 'sqz_on': False, 'price_vs_zl': 'TOUCH',
    'consec_weeks': 4, 'close': 200.0, 'cmf_tag': '↑CMF3d',
}
rows = _table_rows([f], {})
assert any('↑CMF3d' in r for r in rows), rows
print('OK:', rows[-1])
"
```
Expected: prints `OK: | [TEST](...)<br><sub>↑CMF3d</sub> | ...` (no traceback)

- [ ] **Step 5: Commit**

```bash
git add weekly_zl_scanner.py
git commit -m "feat: add CMF marker to weekly_zl_scanner Symbol column"
```

---

## Task 5: Wire into `trend_scanner.py`

**Files:**
- Modify: `trend_scanner.py` (import line, `:413` finding dict, `:454-470` `_row`)

**Interfaces:**
- Consumes: `cmf_tag` from Task 1.

- [ ] **Step 1: Import `cmf_tag`**

Find the existing `from ohlc_db import ... liq_tag` line and add `cmf_tag` to it.

- [ ] **Step 2: Store `cmf_tag` in the finding dict**

Current line 413:
```python
            "liq_tag": liq_tag(df_raw),
```
Change to:
```python
            "liq_tag": liq_tag(df_raw),
            "cmf_tag": cmf_tag(df_raw),
```

- [ ] **Step 3: Add Symbol subline**

Current (lines 454-470):
```python
    return (
        f"| [{sym}]({tv}) "
        f"| {f.get('trap', 'n/a')} "
        f"| {lbl_cell} "
        f"| {sig_emoji} {label} "
        f"| {f['score']:.0f} "
        f"| {rs_cell} "
        f"| {cavgc_arrow}{f['cavgc']:.3f} "
        f"| {f['leader_pct']:.0f}% "
        f"| {abv_low} "
        f"| {tt_cell} "
        f"| {vol_cell} "
        f"| ↑{zl_d} "
        f"| {zl_p} "
        f"| {ds}{f['day_chg']:.2f}% "
        f"| {cl} {em} |"
    )
```
Change to:
```python
    cmf = f.get("cmf_tag", "")
    sym_cell = f"[{sym}]({tv})" + (f"<br><sub>{cmf}</sub>" if cmf else "")
    return (
        f"| {sym_cell} "
        f"| {f.get('trap', 'n/a')} "
        f"| {lbl_cell} "
        f"| {sig_emoji} {label} "
        f"| {f['score']:.0f} "
        f"| {rs_cell} "
        f"| {cavgc_arrow}{f['cavgc']:.3f} "
        f"| {f['leader_pct']:.0f}% "
        f"| {abv_low} "
        f"| {tt_cell} "
        f"| {vol_cell} "
        f"| ↑{zl_d} "
        f"| {zl_p} "
        f"| {ds}{f['day_chg']:.2f}% "
        f"| {cl} {em} |"
    )
```

- [ ] **Step 4: Smoke-check the row output**

Run:
```bash
python -c "
from trend_scanner import _row
f = {
    'symbol': 'TEST', 'entries': [('TEST_TAG', 'Test Label', 0)],
    'rs_state': 'strong', 'rs_pct': 60.0, 'cavgc_rising': True, 'cavgc': 1.01,
    'zl_days': 3, 'zl_pct': 1.0, 'day_chg': 0.5,
    'vol_dryup': False, 'vol_ratio': 1.2, 'tt_score': 5,
    'sma200_up': True, 'pct_above_low': 10.0, 'score': 70.0, 'leader_pct': 80.0,
    'cmf_tag': '↑CMF3d',
}
row = _row(f, {})
assert '↑CMF3d' in row, row
print('OK:', row)
"
```
Expected: prints `OK: | [TEST](...)<br><sub>↑CMF3d</sub> | ...` (no traceback)

- [ ] **Step 5: Commit**

```bash
git add trend_scanner.py
git commit -m "feat: add CMF marker to trend_scanner Symbol column"
```

---

## Task 6: Wire into `rs_highline_scanner.py`

**Files:**
- Modify: `rs_highline_scanner.py` (import line, `:325` finding dict, `:357-372` `_row`)

**Interfaces:**
- Consumes: `cmf_tag` from Task 1.

- [ ] **Step 1: Import `cmf_tag`**

Find the existing `from ohlc_db import ... liq_tag` line and add `cmf_tag` to it.

- [ ] **Step 2: Store `cmf_tag` in the finding dict**

Current line 325:
```python
            "liq_tag": liq_tag(df),
```
Change to:
```python
            "liq_tag": liq_tag(df),
            "cmf_tag": cmf_tag(df),
```

- [ ] **Step 3: Add Symbol subline**

Current (lines 357-372):
```python
    return (
        f"| [{sym}]({tv}) [{circuit_cell}] "
        f"| {name_cell} "
        f"| {f['close']:.2f} "
        f"| {ds}{f['day_chg']:.2f}% "
        f"| {f['rs_high']:.2f} "
        f"| +{f['pct_above']:.2f}% "
        f"| {rs_icon} "
        f"| {zl_cell} "
        f"| {f['zl_days']}d "
        f"| {zl_p} "
        f"| {sqz} "
        f"| {f['atr_pct']:.1f}% "
        f"| {f['earliness']:.0f} "
        f"| {f['liq_tag']} |"
    )
```
Change to:
```python
    cmf = f.get("cmf_tag", "")
    sym_cell = f"[{sym}]({tv}) [{circuit_cell}]" + (f"<br><sub>{cmf}</sub>" if cmf else "")
    return (
        f"| {sym_cell} "
        f"| {name_cell} "
        f"| {f['close']:.2f} "
        f"| {ds}{f['day_chg']:.2f}% "
        f"| {f['rs_high']:.2f} "
        f"| +{f['pct_above']:.2f}% "
        f"| {rs_icon} "
        f"| {zl_cell} "
        f"| {f['zl_days']}d "
        f"| {zl_p} "
        f"| {sqz} "
        f"| {f['atr_pct']:.1f}% "
        f"| {f['earliness']:.0f} "
        f"| {f['liq_tag']} |"
    )
```

- [ ] **Step 4: Smoke-check the row output**

Run:
```bash
python -c "
from rs_highline_scanner import _row
f = {
    'symbol': 'TEST', 'zl_rising': True, 'zl_days': 3, 'zl_pct': 1.0,
    'day_chg': 0.5, 'rs_state': 'strong', 'squeeze': False,
    'close': 150.0, 'rs_high': 145.0, 'pct_above': 3.4, 'atr_pct': 4.2,
    'earliness': 55.0, 'liq_tag': '→₹12Cr · ₹10Cr', 'cmf_tag': '↑CMF3d',
}
row = _row(f, {}, {})
assert '↑CMF3d' in row, row
print('OK:', row)
"
```
Expected: prints `OK: | [TEST](...) [20% ]<br><sub>↑CMF3d</sub> | ...` (no traceback)

- [ ] **Step 5: Commit**

```bash
git add rs_highline_scanner.py
git commit -m "feat: add CMF marker to rs_highline_scanner Symbol column"
```

---

## Task 7: Pine v6 companion indicator

**Files:**
- Create: `pine_scripts/CMF_ZeroCross.pine`

**Interfaces:**
- None (standalone chart indicator, no Python coupling beyond matching formula/logic per parity convention).

- [ ] **Step 1: Write the indicator**

Create `pine_scripts/CMF_ZeroCross.pine`:

```pinescript
//@version=6
indicator("CMF Zero-Cross", shorttitle="CMF0", overlay=false)
// Chaikin Money Flow (CMF) zero-line cross indicator.
// Standalone oscillator pane — no companion overlay indicator.
// Alert message format: CMF_ZERO_CROSS|{{ticker}}|bull|TF:{{interval}}  (or |bear|)
// Python counterpart: ohlc_db.cmf_days() / cmf_tag() — same formula, same
// zero-cross recency logic. Mirror any parameter change both places.

cmfLen = input.int(20, "CMF Length", minval = 1)

rangeVal = high - low
mfm = rangeVal > 0 ? ((close - low) - (high - close)) / rangeVal : 0.0
mfv = mfm * volume

cmfLine = math.sum(mfv, cmfLen) / math.sum(volume, cmfLen)

zero = 0.0
bullCross = ta.crossover(cmfLine, zero)
bearCross = ta.crossunder(cmfLine, zero)

var int barsSinceCross = 0
crossedNow = bullCross or bearCross
barsSinceCross := crossedNow ? 0 : barsSinceCross + 1

plot(cmfLine, "CMF", color = cmfLine >= 0 ? color.green : color.red, linewidth = 2)
hline(0, "Zero Line", color = color.gray)

if barstate.islast
    label.new(
         bar_index, cmfLine,
         text = (cmfLine >= 0 ? "↑CMF" : "↓CMF") + str.tostring(barsSinceCross) + "d",
         color = cmfLine >= 0 ? color.green : color.red,
         style = label.style_label_left,
         textcolor = color.white)

alertcondition(bullCross, "CMF Bull Cross", "CMF_ZERO_CROSS|{{ticker}}|bull|TF:{{interval}}")
alertcondition(bearCross, "CMF Bear Cross", "CMF_ZERO_CROSS|{{ticker}}|bear|TF:{{interval}}")
```

- [ ] **Step 2: Verify in TradingView Pine Editor**

Paste into TradingView Pine Editor, click "Add to chart" on any NSE symbol.
Expected: no compile errors, oscillator pane appears below price, green/red line crossing zero, label at the last bar shows `↑CMFNd` or `↓CMFNd`.

- [ ] **Step 3: Commit**

```bash
git add pine_scripts/CMF_ZeroCross.pine
git commit -m "feat: add CMF zero-cross Pine v6 indicator"
```

---

## Spec Coverage Check

- CMF formula + div-by-zero guard → Task 1
- `cmf_days`/`cmf_tag` in `ohlc_db.py`, `liq_tag()`-style contract → Task 1
- Wiring into all 5 scanners' Symbol cell → Tasks 2–6
- Pine v6 companion, parity, alert format → Task 7
- Test coverage (`tests/test_cmf.py`) → Task 1, Step 1
- No schedule/PS1/CLAUDE.md changes → confirmed, no such task added
