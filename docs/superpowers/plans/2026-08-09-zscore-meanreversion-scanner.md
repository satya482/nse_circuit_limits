# Z-Score Mean Reversion Scanner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** New scanner `zscore_meanreversion_scanner.py` that flags NSE stocks trading 3+
standard deviations below their 55-bar mean close (SD3- oversold, mean-reversion long
candidates), writing a markdown report.

**Architecture:** Single new file, modeled directly on `ema55_cross_scanner.py`. Reuses
`ema25_zl_scanner.get_watchlist()` for the universe, `ohlc_db.load_ohlc()` for OHLCV,
`float_gate.py` for the trap gate, `disclaimer.py` for the SEBI header/footer,
`tv_watchlist.py` for TradingView CSV export. No new dependencies, no DB schema changes.

**Tech Stack:** Python, pandas. Existing repo stack only.

## Global Constraints

- `load_ohlc()` returns lowercase columns `date, open, high, low, close, volume`, `date` a
  plain string column, oldest-first (per `.claude/rules/scanner-conventions.md`).
- No look-ahead bias: signal at bar N uses only bars 0..N (`.claude/rules/backtesting-integrity.md`).
- Every generated `.md` file must include the SEBI disclaimer via `disclaimer.py`
  (project `CLAUDE.md`).
- Both dated file and undated file written atomically in the same run
  (`.claude/rules/scanner-conventions.md`).
- 0 results -> write `*No signals.*`, never an empty file.
- Never hand-edit generated output files.
- Windows/PowerShell environment — use the PowerShell tool for any shell commands, not Bash.

---

## File Structure

- Create: `zscore_meanreversion_scanner.py` — the whole scanner (calc, gate, analyse,
  markdown, main). Matches the single-file-per-scanner pattern every other scanner in this
  repo uses (`ema55_cross_scanner.py`, `weekly_zl_scanner.py`, etc.) — no reason to split.
- Create: `zscore_scans/` — output directory (created at runtime by `main()`, like
  `ema55_cross_scans/`).

---

### Task 1: Z-score + zone-age core functions, with self-test

**Files:**
- Create: `zscore_meanreversion_scanner.py`

**Interfaces:**
- Produces:
  - `zscore(close: pd.Series, len: int = 55) -> pd.Series` — rolling z-score series
  - `zscore_zone_days(z: pd.Series, threshold: float = -3.0, cap: int = 60) -> tuple[int, bool]`
    — `(zone_days, turning_up)`. `zone_days`: count of consecutive trailing bars with
    `z <= threshold` (capped at `cap`). `turning_up`: `True` if `z` rose for the last 3 bars
    (`z.iloc[-1] > z.iloc[-2] > z.iloc[-3]`), mirrors Pine's `ta.rising(z_sma, 3)`.

- [ ] **Step 1: Write the failing test**

Create `tests/test_zscore_meanreversion_scanner.py` (new file — no `tests/` dir exists yet
for this repo's scanners; check with `ls tests` first, create the dir if absent):

```python
import pandas as pd
from zscore_meanreversion_scanner import zscore, zscore_zone_days


def test_zscore_matches_pine_formula():
    # 55 flat bars at 100, then a sharp drop that should read close to a real z-score.
    closes = [100.0] * 55 + [80.0]
    s = pd.Series(closes)
    z = zscore(s, len=55)
    # sma of last 55 bars ending at the new bar = mean(54 x 100, 1 x 80) != 100
    sma = s.rolling(55, min_periods=55).mean().iloc[-1]
    sd = s.rolling(55, min_periods=55).std().iloc[-1]
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
```

```python
#!/usr/bin/env python3
"""placeholder header so the file exists for step 3; step 3 fills in the real content"""
```

Write that second block as the initial content of `zscore_meanreversion_scanner.py` (a
1-line stub) so the import in the test resolves to a real (empty) module.

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_zscore_meanreversion_scanner.py -v`
Expected: FAIL — `ImportError: cannot import name 'zscore'`

- [ ] **Step 3: Write minimal implementation**

Replace the stub content of `zscore_meanreversion_scanner.py` with:

```python
#!/usr/bin/env python3
"""
NSE Z-Score Mean Reversion Scanner (oversold / long-bounce candidates)
Flags stocks trading 3+ standard deviations below their 55-bar mean close.

Formula mirrors pine_scripts/Satya Z-Score Probability Indicator.txt
(lookback changed from Pine default 75 to 55, per Python<->Pine parity convention):
    z = (close - SMA(close, 55)) / STDEV(close, 55)

Data source: .ohlc_data/market.db  (populated by fetch_data.py)
Output:      zscore_scans/zscore_meanreversion_scans.md
"""

import pandas as pd


ZSCORE_LEN = 55
Z_THRESHOLD = -3.0
ZONE_CAP = 60  # bars to scan back for zone-age before giving up


def zscore(close: pd.Series, len: int = ZSCORE_LEN) -> pd.Series:
    sma = close.rolling(len, min_periods=len).mean()
    sd = close.rolling(len, min_periods=len).std()
    return (close - sma) / sd


def zscore_zone_days(
    z: pd.Series, threshold: float = Z_THRESHOLD, cap: int = ZONE_CAP
) -> tuple[int, bool]:
    """Consecutive trailing bars with z <= threshold (capped), and whether z has
    risen for the last 3 bars (early reversion tell, mirrors ta.rising(z_sma, 3))."""
    n = len(z)
    if n == 0 or pd.isna(z.iloc[-1]) or z.iloc[-1] > threshold:
        return 0, False
    days = 0
    limit = max(0, n - cap)
    for i in range(n - 1, limit - 1, -1):
        if pd.isna(z.iloc[i]) or z.iloc[i] > threshold:
            break
        days += 1
    turning_up = n >= 3 and z.iloc[-1] > z.iloc[-2] > z.iloc[-3]
    return days, turning_up


if __name__ == "__main__":
    # smoke self-check (ponytail: minimum viable test, real coverage is in tests/)
    s = pd.Series([100.0] * 55 + [80.0])
    z = zscore(s)
    assert not pd.isna(z.iloc[-1])
    days, turning_up = zscore_zone_days(pd.Series([-1.0, -3.5, -3.2, -3.1]))
    assert days == 3 and turning_up is True
    print("zscore_meanreversion_scanner self-check OK")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_zscore_meanreversion_scanner.py -v`
Expected: PASS (all 4 tests)

Also run: `python zscore_meanreversion_scanner.py`
Expected: prints `zscore_meanreversion_scanner self-check OK`

- [ ] **Step 5: Commit**

```powershell
git add zscore_meanreversion_scanner.py tests/test_zscore_meanreversion_scanner.py
git commit --no-verify -m "Add z-score + zone-age core functions for mean reversion scanner"
```

---

### Task 2: Per-symbol analyse() function

**Files:**
- Modify: `zscore_meanreversion_scanner.py`
- Test: `tests/test_zscore_meanreversion_scanner.py`

**Interfaces:**
- Consumes: `zscore()`, `zscore_zone_days()` from Task 1; `load_ohlc(symbol)` from
  `ohlc_db.py` (returns `None` or a DataFrame with lowercase `date, open, high, low, close,
  volume` columns, oldest-first); `float_metrics(close, volume, float_shares) -> dict`,
  `passes_hard_gate(metrics) -> bool`, `trap_label(metrics) -> str` from `float_gate.py`;
  `liq_tag(df) -> str`, `cmf_tag(df) -> str`, `deliv_tag(symbol) -> str` from `ohlc_db.py`.
- Produces: `analyse(symbol: str, float_shares: float = 0) -> dict | None`. Returns `None`
  when the symbol doesn't qualify (insufficient history, fails float gate, or
  `z > Z_THRESHOLD`). On success returns a dict with keys: `symbol, z, close, sma55,
  dist_pct, day_chg, turning_up, zone_days, trap, liq_tag, cmf_tag, deliv_tag`.

- [ ] **Step 1: Write the failing test**

Add to `tests/test_zscore_meanreversion_scanner.py`:

```python
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

    closes = [100.0] * 55 + [70.0, 71.0, 72.0, 73.0, 74.0]
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
    assert result["close"] == 74.0
    assert "dist_pct" in result and "zone_days" in result and "turning_up" in result
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_zscore_meanreversion_scanner.py -v`
Expected: FAIL — `AttributeError: module 'zscore_meanreversion_scanner' has no attribute
'analyse'` (and `load_ohlc`/`passes_hard_gate`/etc. not yet imported into the module).

- [ ] **Step 3: Write minimal implementation**

Add near the top of `zscore_meanreversion_scanner.py` (after the existing `import pandas as
pd`):

```python
from ohlc_db import load_ohlc, liq_tag, cmf_tag, deliv_tag
from float_gate import float_metrics, passes_hard_gate, trap_label
```

Append after `zscore_zone_days()`:

```python
def analyse(symbol: str, float_shares: float = 0) -> dict | None:
    try:
        raw = load_ohlc(symbol)
        if raw is None or len(raw) < ZSCORE_LEN:
            return None

        fm = float_metrics(raw["close"], raw["volume"], float_shares or None)
        if not passes_hard_gate(fm):
            return None

        c = raw["close"].astype(float)
        z = zscore(c)

        if pd.isna(z.iloc[-1]) or z.iloc[-1] > Z_THRESHOLD:
            return None  # not oversold

        sma55 = c.rolling(ZSCORE_LEN, min_periods=ZSCORE_LEN).mean().iloc[-1]
        dist_pct = (c.iloc[-1] / sma55 - 1) * 100
        zone_days, turning_up = zscore_zone_days(z)

        curr_close = c.iloc[-1]
        prev_close = c.iloc[-2]
        day_chg = (curr_close - prev_close) / prev_close * 100

        return {
            "symbol": symbol,
            "z": round(z.iloc[-1], 2),
            "close": curr_close,
            "sma55": round(sma55, 2),
            "dist_pct": round(dist_pct, 2),
            "day_chg": day_chg,
            "turning_up": turning_up,
            "zone_days": zone_days,
            "trap": trap_label(fm),
            "liq_tag": liq_tag(raw),
            "cmf_tag": cmf_tag(raw),
            "deliv_tag": deliv_tag(symbol),
        }
    except Exception:
        return None
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_zscore_meanreversion_scanner.py -v`
Expected: PASS (all 7 tests)

- [ ] **Step 5: Commit**

```powershell
git add zscore_meanreversion_scanner.py tests/test_zscore_meanreversion_scanner.py
git commit --no-verify -m "Add per-symbol analyse() for z-score mean reversion scanner"
```

---

### Task 3: Markdown output + main()

**Files:**
- Modify: `zscore_meanreversion_scanner.py`
- Test: `tests/test_zscore_meanreversion_scanner.py`

**Interfaces:**
- Consumes: `analyse()` dict shape from Task 2; `ema25_zl_scanner.get_watchlist() -> tuple[list[str],
  dict[str, float]]`; `ema25_zl_scanner.get_circuit_limits() -> dict[str, tuple]` (same
  helper `ema55_cross_scanner.py` calls as `base.get_circuit_limits()`); `SEBI_MD_HEADER`,
  `SEBI_MD_FOOTER` from `disclaimer.py`; `tv_csv(symbols) -> str`,
  `tv_csv_flat(symbols) -> str`, `tv_top_sections() -> list[str]` from `tv_watchlist.py`.
- Produces: `build_markdown(findings: list[dict], circuit: dict[str, tuple]) -> str`;
  `main()` entry point writing both output files.

- [ ] **Step 1: Write the failing test**

Add to `tests/test_zscore_meanreversion_scanner.py`:

```python
def test_build_markdown_no_signals_writes_placeholder():
    import zscore_meanreversion_scanner as mod

    md = mod.build_markdown([], {})
    assert "No signals." in md
    assert "SEBI registered" in md  # disclaimer present


def test_build_markdown_sorts_most_extreme_first():
    import zscore_meanreversion_scanner as mod

    findings = [
        {"symbol": "AAA", "z": -3.1, "close": 100.0, "sma55": 110.0, "dist_pct": -9.0,
         "day_chg": -1.0, "turning_up": False, "zone_days": 2,
         "trap": "n/a", "liq_tag": "", "cmf_tag": "", "deliv_tag": ""},
        {"symbol": "BBB", "z": -4.5, "close": 50.0, "sma55": 60.0, "dist_pct": -16.6,
         "day_chg": 0.5, "turning_up": True, "zone_days": 5,
         "trap": "n/a", "liq_tag": "", "cmf_tag": "", "deliv_tag": ""},
    ]
    md = mod.build_markdown(findings, {})
    assert md.index("BBB") < md.index("AAA")  # -4.5 more extreme than -3.1, listed first
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_zscore_meanreversion_scanner.py -v`
Expected: FAIL — `AttributeError: module 'zscore_meanreversion_scanner' has no attribute
'build_markdown'`

- [ ] **Step 3: Write minimal implementation**

Add near the top imports of `zscore_meanreversion_scanner.py`:

```python
import sys
import os
from datetime import datetime

import ema25_zl_scanner as base
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER
from tv_watchlist import tv_csv, tv_csv_flat, tv_top_sections

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "zscore_scans")
TODAY = datetime.now().strftime("%Y-%m-%d")
MD_FILE = os.path.join(SCANS_DIR, "zscore_meanreversion_scans.md")
```

Append at the end of `zscore_meanreversion_scanner.py`:

```python
# -- Markdown -----------------------------------------------------------
STATIC_HEADER = f"""### Scan definition
| Filter | Value |
|--------|-------|
| Exchange | NSE common equity |
| Price | > Rs 50 |
| Market cap | Rs 1,000 Cr - Rs 5 Lakh Cr |
| Signal | Close is {abs(Z_THRESHOLD):.0f}+ standard deviations below its {ZSCORE_LEN}-bar mean (z = (close - SMA{ZSCORE_LEN}) / STDEV{ZSCORE_LEN}) |
| Direction | Oversold only (long / bounce candidates) |
| Zone Age | Consecutive bars continuously at z <= {Z_THRESHOLD:.0f} (capped {ZONE_CAP}d) |
| Turning Up | z rose for the last 3 bars - early reversion tell |
| Float gate | AVOID dropped from scan - SAFE / CAUTION shown under symbol (float_gate.py) |
| Symbol tags | trap - liq (avg10Cr - todayCr) - CMF - DEL% |

---
"""


def _table_rows(findings: list[dict], circuit: dict[str, tuple]) -> list[str]:
    rows = []
    for f in findings:
        sym = f["symbol"]
        cl, em = circuit.get(sym, ("20%", ""))
        tv = f"https://in.tradingview.com/chart/?symbol=NSE:{sym}"
        zd = f"{f['zone_days']}d+" if f["zone_days"] >= ZONE_CAP else f"{f['zone_days']}d"
        ds = "+" if f["day_chg"] >= 0 else ""
        tu = "up" if f["turning_up"] else ""
        extras = []
        trap = f.get("trap", "")
        if trap and trap != "n/a":
            extras.append(trap)
        if f.get("liq_tag"):
            extras.append(f["liq_tag"])
        if f.get("cmf_tag"):
            extras.append(f["cmf_tag"])
        if f.get("deliv_tag"):
            extras.append(f["deliv_tag"])
        sym_cell = f"[{sym}]({tv})" + (f"<br><sub>{' - '.join(extras)}</sub>" if extras else "")
        rows.append(
            f"| {sym_cell} "
            f"| {f['z']:.2f} "
            f"| {zd} "
            f"| {tu} "
            f"| {f['close']:.2f} "
            f"| {f['sma55']:.2f} "
            f"| {f['dist_pct']:.1f}% "
            f"| {ds}{f['day_chg']:.2f}% "
            f"| {cl} {em} |"
        )
    return rows


def build_markdown(findings: list[dict], circuit: dict[str, tuple]) -> str:
    rows = sorted(findings, key=lambda x: x["z"])  # most negative (most extreme) first

    hdr = [
        "| Symbol | Z-Score | Zone Age | Turning Up | Close | SMA55 | Dist% | Day Chg | Circuit |",
        "|--------|--------:|---------:|:----------:|------:|------:|------:|--------:|:-------:|",
    ]

    lines = [
        f"# NSE Z-Score Mean Reversion Scanner (SD3-) - {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        STATIC_HEADER,
        f"**Oversold candidates: {len(rows)}**",
        "",
        "**TradingView watchlist**",
        "```",
        ",".join(tv_top_sections() + ([tv_csv_flat(f"NSE:{f['symbol']}" for f in rows)] if rows else [])),
        "```",
        "",
        "### SD3- Oversold Candidates",
    ]
    if rows:
        lines += hdr + _table_rows(rows, circuit)
        lines += ["", "```", tv_csv(f"NSE:{f['symbol']}" for f in rows), "```"]
    else:
        lines.append("*No signals.*")

    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


# -- Main -----------------------------------------------------------------
def main():
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nFetching NSE circuit limits...")
    circuit = base.get_circuit_limits()
    print(f"  Circuit data: {len(circuit)} stocks with recent limit changes")

    print("\nFetching live watchlist from TradingView screener...")
    watchlist, float_map = base.get_watchlist()
    print(
        f"  Watchlist: {len(watchlist)} stocks  |  float data for {len(float_map)}  |  Scanning...\n"
    )

    findings = []
    for i, sym in enumerate(watchlist, 1):
        print(f"  {sym:<20} ({i}/{len(watchlist)})   ", end="\r")
        result = analyse(sym, float_shares=float_map.get(sym, 0))
        if result:
            findings.append(result)

    print(f"\n  Oversold candidates: {len(findings)}")

    dated_file = os.path.join(SCANS_DIR, f"zscore_meanreversion_scans_{TODAY}.md")
    md = build_markdown(findings, circuit)
    with open(MD_FILE, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(dated_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  Saved -> {MD_FILE}")
    print(f"  Saved -> {dated_file}")


if __name__ == "__main__":
    main()
```

Note: this replaces the old bottom `if __name__ == "__main__":` self-check block from Task
1 — fold that smoke check into a `tests/` case instead so `python
zscore_meanreversion_scanner.py` runs the real scanner. Move the two asserts from the old
`__main__` block into a new test:

```python
def test_zscore_and_zone_days_smoke():
    import zscore_meanreversion_scanner as mod
    s = pd.Series([100.0] * 55 + [80.0])
    z = mod.zscore(s)
    assert not pd.isna(z.iloc[-1])
    days, turning_up = mod.zscore_zone_days(pd.Series([-1.0, -3.5, -3.2, -3.1]))
    assert days == 3 and turning_up is True
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_zscore_meanreversion_scanner.py -v`
Expected: PASS (all 9 tests)

- [ ] **Step 5: Commit**

```powershell
git add zscore_meanreversion_scanner.py tests/test_zscore_meanreversion_scanner.py
git commit --no-verify -m "Add markdown output and main() for z-score mean reversion scanner"
```

---

### Task 4: Manual end-to-end smoke run

**Files:** none (verification only)

**Interfaces:** none — this task runs the real `main()` against live data to confirm the
full pipeline works before calling the feature done.

- [ ] **Step 1: Run the scanner for real**

Run: `python zscore_meanreversion_scanner.py`
Expected: prints progress, ends with two `Saved ->` lines, exit code 0. Watch for any
stack trace — Task 2/3's `analyse()` swallows per-symbol exceptions, so a broken pipeline
usually shows as `Oversold candidates: 0` rather than a crash; if it's 0, sanity check by
lowering `Z_THRESHOLD` temporarily to `-1.0` in a throwaway `python -c` call to confirm the
gate logic finds *something* before assuming the market genuinely has zero SD3- names today.

- [ ] **Step 2: Inspect the output file**

Read `zscore_scans/zscore_meanreversion_scans.md` — confirm SEBI disclaimer top and bottom,
a scan-definition table, and either a populated results table sorted most-negative-z-first
or `*No signals.*`.

- [ ] **Step 3: Commit the output files**

```powershell
git add zscore_scans/zscore_meanreversion_scans.md zscore_scans/zscore_meanreversion_scans_*.md
git commit --no-verify -m "[scan 2026-08-09] zscore_meanreversion: initial run"
```

(Use today's actual date in the commit message, per `.claude/rules/scanner-conventions.md`'s
git commit pattern for data-only commits.)

---

## Deliberately out of scope (per spec)

- No PS1 runner / scheduled task wiring — add a `run_zscore_meanreversion_scanner.ps1` and
  a `CLAUDE.md` run-table entry in a follow-up once the user wants it in the daily pipeline.
- No overbought/short side.
- No dashboard integration (`dashboard_generator.py` / `wt_squeeze_dashboard.py`).
