# RS High-Line Cross Scanner — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `rs_highline_scanner.py` — daily standalone scanner that fires when a stock's close crosses above the high of the last bar where its RS line was declining, with full context enrichment (ZL25, RS state, squeeze, earliness, circuit, liq_tag).

**Architecture:** TV screener narrows ~2000 NSE equities to ~400 via price/MCap/EMA/notional filters. OHLC loaded from SQLite via `load_ohlc_many`. Local ATR(14)% gate applied, then `_rs_highline_cross` computes the signal per-stock. Results enriched with context columns and written to two markdown files.

**Tech Stack:** Python 3.13, pandas, tradingview-screener, SQLite (via ohlc_db.py), PowerShell runner.

## Global Constraints

- Python executable: `C:\Python313\python.exe`
- All output `.md` files must include `SEBI_MD_HEADER` / `SEBI_MD_FOOTER` from `disclaimer.py`
- Zero results → write `*No signals.*` section, never empty file
- Write both `rs_highline_latest.md` AND `rs_highline_YYYY-MM-DD.md` in same run
- Git commit message format: `[scan YYYY-MM-DD] rs-highline: N signals`
- Bench symbol: `"NIFTY MIDSML 400"` (with spaces, matches SQLite key)
- `load_ohlc_many` returns `date` as `datetime64` column, oldest-first, lowercase cols
- ATR = Wilder EWM: `tr.ewm(span=14, adjust=False).mean()`
- No yfinance, no external API calls in scanner logic — SQLite only

---

## File Map

| File | Action | Responsibility |
|------|--------|----------------|
| `rs_highline_scanner.py` | Create | Main scanner: screener → OHLC → signal → output |
| `rs_highline_scans/` | Create dir | Output directory |
| `tests/test_rs_highline_scanner.py` | Create | Unit tests for `_rs_highline_cross` |
| `run_rs_highline_scanner.ps1` | Create | PS1 runner, logs to `logs/`, auto-commit |
| `run_all_scanners.ps1` | Modify | Add RS_HighLine after WT_BullCross |
| `CLAUDE.md` | Modify | Add to run table + output files table |

---

## Task 1: Signal Function + Unit Tests

**Files:**
- Create: `rs_highline_scanner.py` (signal function only)
- Create: `tests/test_rs_highline_scanner.py`

**Interfaces:**
- Produces: `_rs_highline_cross(df: pd.DataFrame, bench: pd.Series) -> tuple[bool, float, float]`
  - `df`: DataFrame with cols `date` (datetime64), `high`, `close` — oldest first
  - `bench`: Series indexed by datetime64, values = bench close prices
  - Returns `(signal, latest_rs_high, pct_above)` — signal=False when no crossover

---

- [ ] **Step 1: Create `rs_highline_scanner.py` with signal function**

```python
#!/usr/bin/env python3
"""
NSE RS High-Line Cross Scanner
Fires when close crosses above the high of the last bar where RS line was declining.
RS line = (close / NIFTY MIDSML 400 close) * 1000  — mirrors Pine Script latestRsHigh logic.
Run after 4:05 PM IST on trading days (after run_fetch_data.ps1).
"""

import sys
import os
import csv
import json
from math import nan, isnan
from datetime import datetime

import pandas as pd
from tradingview_screener import Query, col

from ohlc_db import load_ohlc_many, get_names, liq_tag
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR  = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "rs_highline_scans")
_LABELS_FILE = os.path.join(REPO_DIR, "tools", "stock_labels.json")
_LABELS: dict = (
    json.loads(open(_LABELS_FILE, encoding="utf-8").read())
    if os.path.exists(_LABELS_FILE)
    else {}
)
TODAY     = datetime.now().strftime("%Y-%m-%d")
MD_LATEST = os.path.join(SCANS_DIR, "rs_highline_latest.md")
MD_DATED  = os.path.join(SCANS_DIR, f"rs_highline_{TODAY}.md")

MC_LOW      = 8_000 * 1_00_00_000        # 8B INR = 800 Cr
MC_HIGH     = 5_00_000 * 1_00_00_000     # 5T INR = 5 lakh Cr
ATR_PCT_MIN = 3.0                         # ATR(14)/close*100 must exceed this
BENCH_SYM   = "NIFTY MIDSML 400"
ZL_TURN_CAP = 60


# ── Indicators ────────────────────────────────────────────────────────────────

def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def _zlema(s: pd.Series, n: int) -> pd.Series:
    e = _ema(s, n)
    return 2 * e - _ema(e, n)


def _atr_wilder(df: pd.DataFrame, period: int = 14) -> pd.Series:
    h = df["high"].astype(float)
    l = df["low"].astype(float)
    c = df["close"].astype(float)
    tr = pd.concat(
        [h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1
    ).max(axis=1)
    return tr.ewm(span=period, adjust=False).mean()


def _atr_pct(df: pd.DataFrame, period: int = 14) -> float:
    """ATR(period, Wilder EWM) / close[-1] * 100."""
    if len(df) < period + 1:
        return 0.0
    atr = _atr_wilder(df, period)
    close = float(df["close"].iloc[-1])
    if close == 0:
        return 0.0
    return float(atr.iloc[-1] / close * 100)


def _bb_kc_squeeze(df: pd.DataFrame) -> bool:
    """True if BB(20,2.0,SMA) is fully inside KC(20,1.5,SMA ATR) on the last bar."""
    if len(df) < 21:
        return False
    c = df["close"].astype(float)
    h = df["high"].astype(float)
    l = df["low"].astype(float)
    bb_basis = c.rolling(20).mean()
    bb_std   = c.rolling(20).std()
    bb_upper = bb_basis + 2.0 * bb_std
    bb_lower = bb_basis - 2.0 * bb_std
    tr       = pd.concat([h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1).max(axis=1)
    kc_atr   = tr.rolling(20).mean()
    kc_basis = c.rolling(20).mean()
    kc_upper = kc_basis + 1.5 * kc_atr
    kc_lower = kc_basis - 1.5 * kc_atr
    return bool(bb_upper.iloc[-1] < kc_upper.iloc[-1] and bb_lower.iloc[-1] > kc_lower.iloc[-1])


def _zl25_turn_stats(zl25: pd.Series, closes: pd.Series) -> tuple[int, float]:
    n     = len(zl25)
    limit = max(2, n - ZL_TURN_CAP)
    for i in range(n - 1, limit - 1, -1):
        if zl25.iloc[i] > zl25.iloc[i - 1] and zl25.iloc[i - 1] <= zl25.iloc[i - 2]:
            bars = (n - 1) - i + 1
            pct  = (closes.iloc[-1] / closes.iloc[i - 1] - 1) * 100
            return bars, round(pct, 2)
    cap_idx = max(0, n - ZL_TURN_CAP)
    return ZL_TURN_CAP, round((closes.iloc[-1] / closes.iloc[cap_idx] - 1) * 100, 2)


def _rs_state(df: pd.DataFrame, bench: pd.Series | None) -> str:
    """Returns 'transition' (weak→strong flip today), 'strong', or 'weak'."""
    if bench is None or len(bench) < 11:
        return "weak"
    try:
        stock_close = df.set_index("date")["close"].astype(float)
        b           = bench.reindex(stock_close.index)
        valid       = b.notna()
        if valid.sum() < 11:
            return "weak"
        rs      = (stock_close[valid] / b[valid]) * 1000
        rs_ema9 = rs.ewm(span=9, adjust=False).mean()
        now_strong = bool(rs.iloc[-1] > rs_ema9.iloc[-1])
        was_weak   = bool(rs.iloc[-2] < rs_ema9.iloc[-2])
        if was_weak and now_strong:
            return "transition"
        return "strong" if now_strong else "weak"
    except Exception:
        return "weak"


def _cavgc(c: pd.Series, length: int = 10) -> tuple[float, bool]:
    avg   = c.ewm(span=length, adjust=False).mean()
    ratio = c / avg
    if pd.isna(ratio.iloc[-1]):
        return 1.0, False
    return float(ratio.iloc[-1]), bool(ratio.iloc[-1] > ratio.iloc[-2])


def _earliness(rs_state: str, zl_days: int, cavgc: float, cavgc_rising: bool, squeeze: bool) -> float:
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


# ── Core signal ───────────────────────────────────────────────────────────────

def _rs_highline_cross(
    df: pd.DataFrame,
    bench: pd.Series,
) -> tuple[bool, float, float]:
    """
    (signal, latest_rs_high_price, pct_above_rs_high)

    latestRsHigh = high of most recent bar where RS line was declining.
    signal = close[-1] crossed above latestRsHigh (Pine ta.crossover equivalent).
    pct_above: positive when close is above the RS-high level.
    Returns (False, nan, nan) on insufficient data.
    """
    if len(df) < 3:
        return False, nan, nan

    stock_close   = df.set_index("date")["close"].astype(float)
    bench_aligned = bench.reindex(stock_close.index)
    valid         = bench_aligned.notna()
    if valid.sum() < 10:
        return False, nan, nan

    rs_line = (stock_close[valid] / bench_aligned[valid]) * 1000
    highs   = df.set_index("date")["high"].astype(float).reindex(rs_line.index)

    # Scan backwards for most recent RS-declining bar
    latest_rs_high = nan
    for i in range(len(rs_line) - 1, 0, -1):
        if rs_line.iloc[i] < rs_line.iloc[i - 1]:
            latest_rs_high = float(highs.iloc[i])
            break

    if isnan(latest_rs_high):
        return False, nan, nan

    c_today = float(stock_close.iloc[-1])
    c_prev  = float(stock_close.iloc[-2])
    crossed  = c_today > latest_rs_high and c_prev <= latest_rs_high
    pct_above = (c_today / latest_rs_high - 1) * 100
    return crossed, round(latest_rs_high, 2), round(pct_above, 2)
```

- [ ] **Step 2: Create `tests/test_rs_highline_scanner.py`**

```python
"""Unit tests for _rs_highline_cross signal function."""
import pandas as pd
import pytest
from rs_highline_scanner import _rs_highline_cross


def _df(closes: list[float], highs: list[float] | None = None) -> pd.DataFrame:
    n = len(closes)
    dates = pd.date_range("2024-01-01", periods=n, freq="B")
    return pd.DataFrame({
        "date":   dates,
        "open":   closes,
        "high":   highs if highs else [c * 1.02 for c in closes],
        "low":    [c * 0.98 for c in closes],
        "close":  closes,
        "volume": [1_000_000] * n,
    })


def _bench(n: int, val: float = 100.0) -> pd.Series:
    dates = pd.date_range("2024-01-01", periods=n, freq="B")
    return pd.Series([val] * n, index=dates)


def test_basic_crossover():
    """close[-1] crosses above high of last RS-down bar → signal=True."""
    # RS line (bench flat=100): [900,850,920,880,1050]
    # RS declining at i=3 (880<920) → latestRsHigh = high[3] = 92
    # close[-2]=88 ≤ 92, close[-1]=105 > 92 → signal=True
    closes = [90.0, 85.0, 92.0, 88.0, 105.0]
    highs  = [92.0, 88.0, 95.0, 92.0, 108.0]
    signal, rs_high, pct = _rs_highline_cross(_df(closes, highs), _bench(5))
    assert signal is True
    assert rs_high == 92.0
    assert pct > 0


def test_today_rs_down_no_signal():
    """If today is the RS-down bar, latestRsHigh = today's high → close>high impossible."""
    # RS: [900,850,920,880,800] — declining today (i=4: 800<880)
    # latestRsHigh = high[4] = 85, close[-1]=80 → 80>85 is False
    closes = [90.0, 85.0, 92.0, 88.0, 80.0]
    highs  = [92.0, 88.0, 95.0, 92.0, 85.0]
    signal, _, _ = _rs_highline_cross(_df(closes, highs), _bench(5))
    assert signal is False


def test_no_rs_down_bars():
    """RS always rising → no latestRsHigh → no signal."""
    closes = [80.0, 85.0, 90.0, 95.0, 100.0]
    signal, rs_high, _ = _rs_highline_cross(_df(closes), _bench(5))
    assert signal is False
    import math
    assert math.isnan(rs_high)


def test_prev_close_already_above_no_signal():
    """Crossover only fires on the exact cross bar — prev_close must be ≤ rs_high."""
    # RS declining at i=1 → latestRsHigh = high[1] = 88
    # close[-2]=96 > 88, so crossover already happened before → no signal
    closes = [90.0, 85.0, 92.0, 96.0, 105.0]
    highs  = [92.0, 88.0, 95.0, 98.0, 108.0]
    signal, _, _ = _rs_highline_cross(_df(closes, highs), _bench(5))
    assert signal is False


def test_insufficient_data():
    """Fewer than 10 valid bench bars → (False, nan, nan)."""
    import math
    closes = [100.0, 101.0]
    signal, rs_high, pct = _rs_highline_cross(_df(closes), _bench(2))
    assert signal is False
    assert math.isnan(rs_high)


def test_pct_above_positive_on_signal():
    """pct_above is positive when signal fires (close > rs_high)."""
    closes = [90.0, 85.0, 92.0, 88.0, 105.0]
    highs  = [92.0, 88.0, 95.0, 92.0, 108.0]
    signal, rs_high, pct = _rs_highline_cross(_df(closes, highs), _bench(5))
    assert signal is True
    assert pct == round((105.0 / 92.0 - 1) * 100, 2)
```

- [ ] **Step 3: Run tests — expect FAIL (function exists but tests not run yet)**

```
cd c:\Users\satya\nse_circuit_limits
C:\Python313\python.exe -m pytest tests/test_rs_highline_scanner.py -v
```

Expected: All 6 tests PASS (signal function is already in the file from Step 1).

- [ ] **Step 4: Commit**

```
git add rs_highline_scanner.py tests/test_rs_highline_scanner.py
git commit -m "feat(rs-highline): add signal function + unit tests"
git push
```

---

## Task 2: TV Screener + ATR Gate

**Files:**
- Modify: `rs_highline_scanner.py` — add `get_watchlist()` and apply ATR gate in main loop

**Interfaces:**
- Produces: `get_watchlist() -> list[str]` — NSE symbols passing all TV screener filters
- ATR gate applied inline in `main()` after OHLC load: skip stock if `_atr_pct(df) < ATR_PCT_MIN`

---

- [ ] **Step 1: Add `get_watchlist()` to `rs_highline_scanner.py`**

Add after the `_earliness` function, before `_rs_highline_cross`:

```python
# ── Watchlist ─────────────────────────────────────────────────────────────────


def get_watchlist() -> list[str]:
    """TV screener: NSE common equity passing price/MCap/EMA/notional filters."""
    _, df = (
        Query()
        .set_markets("india")
        .select("name", "close", "market_cap_basic", "Perf.W")
        .where(
            col("exchange") == "NSE",
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("close") > 20,
            col("Perf.W") > 3,
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
            col("close") > col("EMA10"),
            col("close") > col("EMA20"),
            col("Value.Traded") > 200e6,
        )
        .limit(2000)
        .get_scanner_data()
    )
    return df["name"].tolist()
```

- [ ] **Step 2: Smoke-test screener (requires internet)**

```
cd c:\Users\satya\nse_circuit_limits
C:\Python313\python.exe -c "from rs_highline_scanner import get_watchlist; w=get_watchlist(); print(f'{len(w)} symbols, first 5: {w[:5]}')"
```

Expected: prints `N symbols, first 5: ['SYMBOL1', ...]` with N > 50.

If `Value.Traded` throws a column error, replace with `col("average_volume_10d_calc") * col("close") > 200e6` and re-test.

- [ ] **Step 3: Commit**

```
git add rs_highline_scanner.py
git commit -m "feat(rs-highline): add TV screener watchlist filter"
git push
```

---

## Task 3: Context Enrichment + analyse()

**Files:**
- Modify: `rs_highline_scanner.py` — add `get_circuit_limits()` and `analyse()`

**Interfaces:**
- Consumes: `_rs_highline_cross(df, bench) -> (bool, float, float)`; all helper functions from Task 1
- Produces: `analyse(symbol, df, bench) -> dict | None`

```python
# dict keys: symbol, signal, rs_high, pct_above, rs_state, zl_rising,
#            zl_days, zl_pct, squeeze, atr_pct, earliness, close, day_chg, liq_tag
```

---

- [ ] **Step 1: Add `get_circuit_limits()` to `rs_highline_scanner.py`**

Add after `get_watchlist()`:

```python
# ── Circuit limits ────────────────────────────────────────────────────────────

_CIRCUIT_EMOJI = {
    ("20", "10"): "🟨",
    ("10", "5"):  "🟥",
    ("5",  "10"): "🟩",
    ("10", "20"): "🟦",
}
_NSE_CSV_PATHS = [
    os.path.join(REPO_DIR, "nse.csv"),
    r"C:\Users\satya\.gemini\antigravity\scratch\circuit_dashboard\nse.csv",
]


def get_circuit_limits() -> dict[str, tuple[str, str]]:
    nse_csv = next((p for p in _NSE_CSV_PATHS if os.path.exists(p)), None)
    if not nse_csv:
        return {}
    try:
        latest: dict[str, dict] = {}
        with open(nse_csv, encoding="utf-8-sig") as fh:
            for raw in csv.DictReader(fh):
                row = {k.strip(): v.strip() for k, v in raw.items()}
                sym = row.get("SYMBOL", "")
                dte = row.get("EFFECTIVE DATE", "")
                frm = row.get("FROM", "")
                to  = row.get("TO", "")
                if not sym or not dte:
                    continue
                try:
                    parsed = datetime.strptime(dte, "%d-%b-%Y")
                except ValueError:
                    continue
                if sym not in latest or parsed > latest[sym]["parsed"]:
                    latest[sym] = {"parsed": parsed, "from": frm, "to": to}
        return {
            sym: (d["to"] + "%", _CIRCUIT_EMOJI.get((d["from"], d["to"]), ""))
            for sym, d in latest.items()
        }
    except Exception:
        return {}
```

- [ ] **Step 2: Add `analyse()` to `rs_highline_scanner.py`**

Add after `get_circuit_limits()`:

```python
# ── Per-stock analysis ────────────────────────────────────────────────────────


def analyse(
    symbol: str,
    df: pd.DataFrame,
    bench: pd.Series | None,
) -> dict | None:
    try:
        if df is None or len(df) < 30:
            return None

        atr_p = _atr_pct(df)
        if atr_p < ATR_PCT_MIN:
            return None

        if bench is None:
            return None

        signal, rs_high, pct_above = _rs_highline_cross(df, bench)
        if not signal:
            return None

        rs = _rs_state(df, bench)
        c  = df["close"].astype(float)
        zl25      = _zlema(c, 25)
        zl_rising = bool(zl25.iloc[-1] > zl25.iloc[-2])
        zl_days, zl_pct = _zl25_turn_stats(zl25, c)

        curr_close = float(c.iloc[-1])
        prev_close = float(c.iloc[-2])
        day_chg    = (curr_close - prev_close) / prev_close * 100

        cavgc_val, cavgc_rising = _cavgc(c)
        squeeze   = _bb_kc_squeeze(df)
        earliness = _earliness(rs, zl_days, cavgc_val, cavgc_rising, squeeze)

        return {
            "symbol":    symbol,
            "close":     curr_close,
            "day_chg":   round(day_chg, 2),
            "rs_high":   rs_high,
            "pct_above": pct_above,
            "rs_state":  rs,
            "zl_rising": zl_rising,
            "zl_days":   zl_days,
            "zl_pct":    zl_pct,
            "squeeze":   squeeze,
            "atr_pct":   round(atr_p, 1),
            "earliness": earliness,
            "liq_tag":   liq_tag(df),
        }
    except Exception:
        return None
```

- [ ] **Step 3: Run existing tests to confirm no regressions**

```
C:\Python313\python.exe -m pytest tests/test_rs_highline_scanner.py -v
```

Expected: 6 PASS.

- [ ] **Step 4: Commit**

```
git add rs_highline_scanner.py
git commit -m "feat(rs-highline): add circuit limits + analyse() context enrichment"
git push
```

---

## Task 4: Markdown Output

**Files:**
- Modify: `rs_highline_scanner.py` — add `_row()`, `_HDR`, `build_markdown()`

**Interfaces:**
- Consumes: `analyse()` dict keys defined in Task 3
- Produces: `build_markdown(findings, circuit, names) -> str` — full markdown string

---

- [ ] **Step 1: Add markdown builder to `rs_highline_scanner.py`**

Add after `analyse()`:

```python
# ── Markdown output ───────────────────────────────────────────────────────────

_RS_EMOJI = {"transition": "🔄", "strong": "↑", "weak": "↓"}

_HDR = [
    "| Symbol | Name | Close | 1D% | RS-High | Above% | RS | ZL | ZL-days | ZL+% | Sqz | ATR% | Early | Liq |",
    "|--------|------|------:|----:|--------:|-------:|:--:|:--:|--------:|-----:|:---:|-----:|------:|-----|",
]


def _row(f: dict, circuit: dict, names: dict[str, str]) -> str:
    sym  = f["symbol"]
    tv   = f"https://in.tradingview.com/chart/?symbol=NSE:{sym}"
    cl, em = circuit.get(sym, ("20%", ""))
    circuit_cell = f"{cl} {em}".strip()

    name_str = names.get(sym, "")
    lbl      = _LABELS.get(sym, "")
    label_parts = [p for p in [name_str, lbl] if p]
    name_cell   = "<br>".join(label_parts)

    zl_arrow = "↑" if f["zl_rising"] else "↓"
    zl_d     = f"{f['zl_days']}d+" if f["zl_days"] >= ZL_TURN_CAP else f"{f['zl_days']}d"
    zl_cell  = f"{zl_arrow}{zl_d}"
    zl_p     = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
    ds       = "+" if f["day_chg"] >= 0 else ""
    rs_icon  = _RS_EMOJI.get(f["rs_state"], "↓")
    sqz      = "●" if f["squeeze"] else "—"

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


def build_markdown(
    findings: list[dict],
    circuit: dict,
    names: dict[str, str],
) -> str:
    sorted_f = sorted(findings, key=lambda x: -x["earliness"])
    lines = [
        f"# RS High-Line Cross — {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        "### Scan definition",
        "| Filter | Value |",
        "|--------|-------|",
        "| Exchange | NSE common equity |",
        "| Price | > ₹20 |",
        "| 1W change | > 3% |",
        "| Market cap | ₹800 Cr – ₹5 Lakh Cr |",
        "| EMA10 / EMA20 | price above both |",
        "| Notional 10D | > ₹20 Cr/day |",
        "| ATR(14)% | > 3% (local, Wilder EWM) |",
        "| Signal | Close crossed above high of last RS-down bar |",
        "| Sort | Earliness score desc (entry closest to move start first) |",
        "",
        "---",
        "",
        f"**{len(findings)} signal{'s' if len(findings) != 1 else ''} "
        f"— RS high-line cross today**",
        "",
    ]

    if sorted_f:
        lines += _HDR + [_row(f, circuit, names) for f in sorted_f]
    else:
        lines.append("*No signals.*")

    lines.append("")
    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER
```

- [ ] **Step 2: Verify markdown builder with synthetic data**

```
C:\Python313\python.exe -c "
from rs_highline_scanner import build_markdown
fake = [{'symbol':'TEST','close':100.0,'day_chg':1.5,'rs_high':95.0,'pct_above':5.26,'rs_state':'strong','zl_rising':True,'zl_days':3,'zl_pct':4.1,'squeeze':False,'atr_pct':3.8,'earliness':25.0,'liq_tag':'→50Cr · 45Cr'}]
md = build_markdown(fake, {}, {})
print(md[:500])
"
```

Expected: prints markdown with header, table row for TEST, SEBI disclaimer.

- [ ] **Step 3: Commit**

```
git add rs_highline_scanner.py
git commit -m "feat(rs-highline): add markdown output builder"
git push
```

---

## Task 5: main() + Output Files

**Files:**
- Modify: `rs_highline_scanner.py` — add `main()` and `__main__` block
- Create: `rs_highline_scans/` directory (via `os.makedirs` in main)

**Interfaces:**
- Consumes: all prior functions
- Produces: `rs_highline_scans/rs_highline_latest.md`, `rs_highline_scans/rs_highline_YYYY-MM-DD.md`

---

- [ ] **Step 1: Add `main()` to `rs_highline_scanner.py`**

Add at the end of the file:

```python
# ── Main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nFetching watchlist from TradingView screener...")
    watchlist = get_watchlist()
    print(f"  {len(watchlist)} stocks after screener filters")

    print(f"\nLoading OHLCV + benchmark ({BENCH_SYM}) from SQLite...")
    syms_to_load = watchlist + [BENCH_SYM]
    all_data = load_ohlc_many(syms_to_load, lookback=400)

    bench_df = all_data.pop(BENCH_SYM, None)
    bench_series: pd.Series | None = (
        bench_df.set_index("date")["close"].astype(float)
        if bench_df is not None
        else None
    )
    if bench_series is None:
        print(f"  WARNING: {BENCH_SYM} not in SQLite — RS signal unavailable")

    print(f"  Loaded {len(all_data)} equity stocks")

    print(f"\nFetching circuit limits...")
    circuit = get_circuit_limits()

    print(f"\nScanning {len(all_data)} stocks...")
    findings: list[dict] = []
    for i, (sym, df_raw) in enumerate(all_data.items(), 1):
        print(f"  {sym:<20} ({i}/{len(all_data)})   ", end="\r")
        result = analyse(sym, df_raw, bench_series)
        if result:
            findings.append(result)
    print()

    print(f"\n  {len(findings)} RS high-line crosses found")

    names = get_names([f["symbol"] for f in findings])
    md    = build_markdown(findings, circuit, names)

    with open(MD_LATEST, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(MD_DATED, "w", encoding="utf-8") as fh:
        fh.write(md)

    print(f"  Saved → {MD_LATEST}")
    print(f"  Saved → {MD_DATED}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run scanner end-to-end (requires SQLite DB populated)**

```
cd c:\Users\satya\nse_circuit_limits
C:\Python313\python.exe rs_highline_scanner.py
```

Expected:
- Prints watchlist count, loaded stocks count, findings count
- Creates `rs_highline_scans/rs_highline_latest.md` and `rs_highline_scans/rs_highline_YYYY-MM-DD.md`
- Files contain SEBI header + either a table or `*No signals.*`

- [ ] **Step 3: Verify both output files exist and have SEBI disclaimer**

```
C:\Python313\python.exe -c "
import os, glob
scans = glob.glob('rs_highline_scans/*.md')
print('Files:', scans)
for f in scans:
    txt = open(f, encoding='utf-8').read()
    print(f, '— SEBI ok:', 'SEBI registered' in txt, '— lines:', txt.count(chr(10)))
"
```

Expected: both files listed, both show `SEBI ok: True`.

- [ ] **Step 4: Commit**

```
git add rs_highline_scanner.py rs_highline_scans/
git commit -m "feat(rs-highline): add main() + end-to-end output"
git push
```

---

## Task 6: PS1 Runner + Integration

**Files:**
- Create: `run_rs_highline_scanner.ps1`
- Modify: `run_all_scanners.ps1` — add RS_HighLine after WT_BullCross
- Modify: `CLAUDE.md` — add to run table + output files table

---

- [ ] **Step 1: Create `run_rs_highline_scanner.ps1`**

```powershell
$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\rs_highline_scanner_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== RS_HIGHLINE_SCANNER START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\rs_highline_scanner.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
$scanDate = Get-Date -Format "yyyy-MM-dd"
& git -C C:\Users\satya\nse_circuit_limits add rs_highline_scans/ 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit -m "[scan $scanDate] rs-highline: scan complete" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "--- Done ---"

# To register the scheduled task (run once as admin):
# schtasks /create /tn "NSE_RS_HighLine" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_rs_highline_scanner.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:30 /f
```

- [ ] **Step 2: Add RS_HighLine to `run_all_scanners.ps1`**

In `run_all_scanners.ps1`, find the line:
```powershell
Run-Scanner "WT_BullCross"         "$ROOT\run_wt_bullcross_scanner.ps1"
```

Add after it:
```powershell
Run-Scanner "RS_HighLine"          "$ROOT\run_rs_highline_scanner.ps1"
```

- [ ] **Step 3: Update `CLAUDE.md` run table**

In the `## Running the scanners` section of `CLAUDE.md`, add:
```
.\run_rs_highline_scanner.ps1    # 4:30 PM — RS high-line cross scanner
```

In the `## Output files (git-tracked)` table, add:
```
| `rs_highline_scans/rs_highline_latest.md`, `rs_highline_scans/rs_highline_YYYY-MM-DD.md` | `rs_highline_scanner.py` |
```

- [ ] **Step 4: Smoke-test PS1 runner**

```powershell
powershell -NonInteractive -ExecutionPolicy Bypass -File C:\Users\satya\nse_circuit_limits\run_rs_highline_scanner.ps1
```

Expected: exits 0, log file created in `logs/`, both scan files updated, git commit+push succeeds.

- [ ] **Step 5: Run full test suite to confirm no regressions**

```
C:\Python313\python.exe -m pytest tests/ -v
```

Expected: all tests PASS including `test_rs_highline_scanner.py`.

- [ ] **Step 6: Commit all integration changes**

```
git add run_rs_highline_scanner.ps1 run_all_scanners.ps1 CLAUDE.md
git commit -m "feat(rs-highline): PS1 runner + run_all_scanners integration + CLAUDE.md"
git push
```

---

## Self-Review

**Spec coverage check:**
- ✅ TV screener: NSE, price>20, 1W>3%, MCap 8B–5T, EMA10/20, notional>200M — Task 2
- ✅ Local ATR(14)>3% gate — Task 3 `analyse()`
- ✅ `_rs_highline_cross` signal — Task 1
- ✅ Full context: ZL25, RS state, squeeze, earliness, circuit, liq_tag — Task 3
- ✅ Both dated + latest output files — Task 5
- ✅ Zero results → `*No signals.*` not empty — Task 4 `build_markdown`
- ✅ SEBI disclaimer on output — Task 4
- ✅ PS1 runner + git commit+push — Task 6
- ✅ `run_all_scanners.ps1` integration — Task 6
- ✅ `CLAUDE.md` update — Task 6

**Type consistency:**
- `analyse()` returns dict with keys consumed verbatim by `_row()` — consistent
- `_rs_highline_cross` returns `(bool, float, float)` — consumed in Task 3 as `signal, rs_high, pct_above`
- `bench: pd.Series` param consistent across `_rs_highline_cross`, `_rs_state`, `analyse`
