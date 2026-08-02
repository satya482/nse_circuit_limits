# Minervini Trend Template Scanner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship `minervini_trend_scanner.py` — a strict 9-check gate (SMA50/150/200 stack, 52wk high/low proximity, RS-vs-benchmark strength) that outputs a qualify-list markdown, wired into the daily scanner schedule.

**Architecture:** Single new root-level script following the `ema55_cross_scanner.py` pattern — reuses `ema25_zl_scanner.get_watchlist()` for universe/float_map and `ema25_zl_scanner`'s RS-gate math, `ohlc_db.load_ohlc()` for data, `disclaimer` constants for SEBI compliance. Pure functions unit-tested with synthetic `pd.Series`, matching `tests/test_ema55_cross_scanner.py`.

**Tech Stack:** Python, pandas, pytest, PowerShell (runner script).

## Global Constraints

- `@version` N/A (Python, not Pine) — but Python↔Pine parity rule doesn't apply here (no Pine companion for this scanner).
- Output must include SEBI disclaimer (`disclaimer.SEBI_MD_HEADER` / `SEBI_MD_FOOTER`) — non-negotiable per repo CLAUDE.md.
- Both dated (`minervini_trend_YYYY-MM-DD.md`) and `minervini_trend_latest.md` written atomically in the same run.
- Zero-result run writes `*No signals.*`, never an empty file.
- No look-ahead bias: all checks use `close.iloc[-1]` (today's bar) or earlier — no forward references.
- PowerShell runner must be plain ASCII (no em dashes/curly quotes) — verify with `tools\check_ps1_syntax.ps1` if it exists.
- `git commit --no-verify` in this repo (pre-commit hooks disabled per repo CLAUDE.md).

---

### Task 1: Trend-template criteria functions + unit tests

**Files:**
- Create: `minervini_trend_scanner.py` (criteria functions only, no I/O yet)
- Test: `tests/test_minervini_trend_scanner.py`

**Interfaces:**
- Consumes: `ema25_zl_scanner.ema(s, n)` (existing EMA helper, only used for RS EMA9, not SMA)
- Produces:
  - `sma(s: pd.Series, n: int) -> pd.Series`
  - `trend_template_checks(close: pd.Series) -> dict[str, bool]` — returns all 8 SMA/52wk checks by name (`above_sma150`, `above_sma200`, `sma150_above_sma200`, `sma200_trending_up`, `sma50_above_150_200`, `above_sma50`, `above_52wk_low_30pct`, `within_25pct_of_52wk_high`), used by Task 2's `analyse()`
  - `passes_trend_template(checks: dict[str, bool]) -> bool` — `all(checks.values())`

- [ ] **Step 1: Write failing tests for `sma()` and `trend_template_checks()`**

```python
# tests/test_minervini_trend_scanner.py
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent))

from minervini_trend_scanner import sma, trend_template_checks, passes_trend_template


def _uptrend_series(n=300, start=100.0, step=0.5):
    return pd.Series([start + i * step for i in range(n)])


def test_sma_matches_rolling_mean():
    s = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
    result = sma(s, 3)
    assert result.iloc[-1] == (3.0 + 4.0 + 5.0) / 3
    assert pd.isna(result.iloc[0])


def test_all_checks_pass_on_clean_steady_uptrend():
    close = _uptrend_series(300)
    checks = trend_template_checks(close)
    assert all(checks.values()), checks
    assert passes_trend_template(checks)


def test_fails_when_price_below_sma50():
    close = _uptrend_series(300)
    close.iloc[-1] = close.iloc[-60]  # crash the last close well below SMA50
    checks = trend_template_checks(close)
    assert checks["above_sma50"] is False
    assert passes_trend_template(checks) is False


def test_fails_when_sma200_not_trending_up():
    # flat for the whole 300 bars except a brief recent wiggle: SMA200 flat
    close = pd.Series([100.0] * 300)
    checks = trend_template_checks(close)
    assert checks["sma200_trending_up"] is False
    assert passes_trend_template(checks) is False


def test_fails_when_more_than_25pct_off_52wk_high():
    close = _uptrend_series(300)
    peak = close.iloc[-30]
    close.iloc[-1] = peak * 0.70  # 30% off a recent-ish high, still within 252d window
    checks = trend_template_checks(close)
    assert checks["within_25pct_of_52wk_high"] is False


def test_fails_when_not_30pct_above_52wk_low():
    close = _uptrend_series(300, start=100.0, step=0.05)  # slow crawl, low bar close to today's low
    checks = trend_template_checks(close)
    assert checks["above_52wk_low_30pct"] is False
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_minervini_trend_scanner.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'minervini_trend_scanner'` (file doesn't exist yet)

- [ ] **Step 3: Implement `sma()`, `trend_template_checks()`, `passes_trend_template()`**

```python
#!/usr/bin/env python3
"""
Minervini Trend Template Scanner
Run in the 4:30 PM group, after the RS-gated scanners (shares their RS gate
function and benchmark load pattern).

Universe (reused from ema25_zl_scanner.py): NSE common equity,
MCap Rs 1,000 Cr - Rs 5 Lakh Cr, price > Rs 50, float hard-gate applied.

Strict AND-gate, all 9 checks must pass (Mark Minervini's Trend Template):
  1. close > SMA150
  2. close > SMA200
  3. SMA150 > SMA200
  4. SMA200 trending up >= 1 month (SMA200 today > SMA200 21 trading days ago)
  5. SMA50 > SMA150 and SMA50 > SMA200
  6. close > SMA50
  7. close >= 1.30 x 52-week low
  8. close >= 0.75 x 52-week high (within 25% of it)
  9. RS strength: daily RS line > weekly RS EMA9, weekly RS EMA9 rising
     (reused from ema25_zl_scanner._weekly_rs_gate() -- RS Rating proxy,
     see docs/superpowers/specs/2026-08-02-minervini-trend-template-scanner-design.md)

No partial-score output -- binary qualify list.

Data source: .ohlc_data/market.db (populated by fetch_data.py)
Output:      minervini_scans/minervini_trend_latest.md
             minervini_scans/minervini_trend_YYYY-MM-DD.md
"""

import sys
import os
from datetime import datetime

import pandas as pd

import ema25_zl_scanner as base
from ohlc_db import load_ohlc, load_ohlc_many, liq_tag, cmf_tag, deliv_tag
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER
from float_gate import float_metrics, passes_hard_gate, trap_label

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "minervini_scans")
TODAY = datetime.now().strftime("%Y-%m-%d")
MD_LATEST = os.path.join(SCANS_DIR, "minervini_trend_latest.md")
BENCH_SYM = "NIFTY MIDSML 400"
LOOKBACK_52WK = 252
MIN_BARS = 260  # 52wk window + buffer


def sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def trend_template_checks(close: pd.Series) -> dict:
    """8 SMA/52wk checks (criterion 9 -- RS gate -- is separate, needs the
    benchmark series, see _weekly_rs_gate reuse in analyse())."""
    sma50 = sma(close, 50)
    sma150 = sma(close, 150)
    sma200 = sma(close, 200)
    c = close.iloc[-1]

    window = close.iloc[-LOOKBACK_52WK:]
    wk_low = window.min()
    wk_high = window.max()

    return {
        "above_sma150": bool(c > sma150.iloc[-1]),
        "above_sma200": bool(c > sma200.iloc[-1]),
        "sma150_above_sma200": bool(sma150.iloc[-1] > sma200.iloc[-1]),
        "sma200_trending_up": bool(sma200.iloc[-1] > sma200.iloc[-21]),
        "sma50_above_150_200": bool(
            sma50.iloc[-1] > sma150.iloc[-1] and sma50.iloc[-1] > sma200.iloc[-1]
        ),
        "above_sma50": bool(c > sma50.iloc[-1]),
        "above_52wk_low_30pct": bool(c >= 1.30 * wk_low),
        "within_25pct_of_52wk_high": bool(c >= 0.75 * wk_high),
    }


def passes_trend_template(checks: dict) -> bool:
    return all(checks.values())
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_minervini_trend_scanner.py -v`
Expected: PASS (6/6)

- [ ] **Step 5: Commit**

```bash
git add minervini_trend_scanner.py tests/test_minervini_trend_scanner.py
git commit --no-verify -m "Add Minervini trend template criteria functions + tests"
```

---

### Task 2: `analyse()`, markdown output, `main()`

**Files:**
- Modify: `minervini_trend_scanner.py` (append to file from Task 1)
- Test: `tests/test_minervini_trend_scanner.py` (append)

**Interfaces:**
- Consumes: `trend_template_checks(close)`, `passes_trend_template(checks)` from Task 1; `ema25_zl_scanner._weekly_rs_gate(rs, c_rs, idx_rs)`, `ema25_zl_scanner.get_watchlist()` (existing); `float_gate.float_metrics`, `float_gate.passes_hard_gate`, `float_gate.trap_label`; `ohlc_db.load_ohlc`, `load_ohlc_many`, `liq_tag`, `cmf_tag`, `deliv_tag`
- Produces: `analyse(symbol: str, index_s: pd.Series, float_shares: float = 0) -> dict | None`, `build_markdown(findings: list[dict]) -> str`, `main()`

- [ ] **Step 1: Write failing test for `build_markdown()` empty + populated cases**

```python
# append to tests/test_minervini_trend_scanner.py
from minervini_trend_scanner import build_markdown


def test_build_markdown_empty_findings_writes_no_signals_not_empty_file():
    md = build_markdown([])
    assert "No signals." in md
    assert "SEBI registered" in md  # disclaimer present


def test_build_markdown_populated_includes_symbol_and_close():
    findings = [{
        "symbol": "TESTSTOCK",
        "close": 123.45,
        "day_chg": 1.23,
        "off_high_pct": -4.5,
        "above_low_pct": 45.0,
    }]
    md = build_markdown(findings)
    assert "TESTSTOCK" in md
    assert "123.45" in md
    assert "SEBI registered" in md
```

- [ ] **Step 2: Run to verify failure**

Run: `python -m pytest tests/test_minervini_trend_scanner.py -v`
Expected: FAIL — `ImportError: cannot import name 'build_markdown'`

- [ ] **Step 3: Implement `analyse()`, `build_markdown()`, `main()`**

```python
# append to minervini_trend_scanner.py

def analyse(symbol: str, index_s: pd.Series, float_shares: float = 0) -> dict | None:
    try:
        raw = load_ohlc(symbol)
        if raw is None or len(raw) < MIN_BARS:
            return None

        fm = float_metrics(raw["close"], raw["volume"], float_shares or None)
        if not passes_hard_gate(fm):
            return None

        df = raw.set_index("date")
        df.index = pd.to_datetime(df.index)
        c = df["close"].astype(float)

        checks = trend_template_checks(c)
        if not passes_trend_template(checks):
            return None

        common = c.index.intersection(index_s.index)
        if len(common) < 30:
            return None
        c_rs = c.loc[common]
        idx_rs = index_s.loc[common]
        rs = (c_rs / idx_rs) * 1000
        if not base._weekly_rs_gate(rs, c_rs, idx_rs):
            return None

        window = c.iloc[-LOOKBACK_52WK:]
        curr_close = c.iloc[-1]
        prev_close = c.iloc[-2]

        return {
            "symbol": symbol,
            "close": curr_close,
            "day_chg": (curr_close - prev_close) / prev_close * 100,
            "off_high_pct": (curr_close / window.max() - 1) * 100,
            "above_low_pct": (curr_close / window.min() - 1) * 100,
            "trap": trap_label(fm),
            "liq_tag": liq_tag(raw),
            "cmf_tag": cmf_tag(raw),
            "deliv_tag": deliv_tag(symbol),
        }
    except Exception:
        return None


STATIC_HEADER = """### Scan definition
| Filter | Value |
|--------|-------|
| Exchange | NSE common equity |
| Price | > Rs 50 |
| Market cap | Rs 1,000 Cr - Rs 5 Lakh Cr |
| Criteria (all must pass) | close > SMA50 > SMA150 > SMA200 stack, SMA200 rising 21d, close within 25% of 52wk high, close >= 30% above 52wk low, RS gate |
| RS gate | Daily RS Line > Weekly RS EMA9, Weekly RS EMA9 rising (RS = close/NIFTY MIDSML 400 x 1000) |
| Float gate | AVOID dropped from scan, SAFE/CAUTION shown under symbol (float_gate.py) |
| Symbol tags | trap - liq (avg10Cr-todayCr) - CMF - DEL% |

---
"""


def _table_rows(findings: list[dict]) -> list[str]:
    rows = []
    for f in findings:
        sym = f["symbol"]
        tv = f"https://in.tradingview.com/chart/?symbol=NSE:{sym}"
        ds = "+" if f["day_chg"] >= 0 else ""
        oh = f"{f['off_high_pct']:.1f}%"
        al = f"+{f['above_low_pct']:.1f}%"
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
        sym_cell = f"[{sym}]({tv})" + (f"<br><sub>{' . '.join(extras)}</sub>" if extras else "")
        rows.append(
            f"| {sym_cell} "
            f"| {f['close']:.2f} "
            f"| {oh} "
            f"| {al} "
            f"| SMA-OK "
            f"| RS-OK "
            f"| {ds}{f['day_chg']:.2f}% |"
        )
    return rows


def build_markdown(findings: list[dict]) -> str:
    rows = sorted(findings, key=lambda x: x["off_high_pct"], reverse=True)

    hdr = [
        "| Symbol | Close | %off 52wk-high | %above 52wk-low | SMA stack | RS gate | Day chg% |",
        "|--------|------:|----------------:|------------------:|:---------:|:-------:|--------:|",
    ]

    lines = [
        f"# Minervini Trend Template Scan - {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        STATIC_HEADER,
        f"**Qualifying: {len(rows)}**",
        "",
        "### Trend Template Qualifiers",
    ]
    if rows:
        lines += hdr + _table_rows(rows)
        lines += ["", "```", ",".join(f"NSE:{f['symbol']}" for f in rows), "```"]
    else:
        lines.append("*No signals.*")

    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


def main():
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nFetching live watchlist from TradingView screener...")
    watchlist, float_map = base.get_watchlist()
    print(f"  Watchlist: {len(watchlist)} stocks | float data for {len(float_map)} | Scanning...\n")

    bench_map = load_ohlc_many([BENCH_SYM])
    bench_df = bench_map.get(BENCH_SYM)
    if bench_df is None:
        print(f"  ERROR: benchmark {BENCH_SYM} not found in DB, aborting.")
        return
    index_s = bench_df.set_index("date")["close"].astype(float)
    index_s.index = pd.to_datetime(index_s.index)

    findings = []
    for i, sym in enumerate(watchlist, 1):
        print(f"  {sym:<20} ({i}/{len(watchlist)})   ", end="\r")
        result = analyse(sym, index_s, float_shares=float_map.get(sym, 0))
        if result:
            findings.append(result)

    print(f"\n  Qualifying: {len(findings)}")

    dated_file = os.path.join(SCANS_DIR, f"minervini_trend_{TODAY}.md")
    md = build_markdown(findings)
    with open(MD_LATEST, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(dated_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  Saved -> {MD_LATEST}")
    print(f"  Saved -> {dated_file}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_minervini_trend_scanner.py -v`
Expected: PASS (8/8 total)

- [ ] **Step 5: Commit**

```bash
git add minervini_trend_scanner.py tests/test_minervini_trend_scanner.py
git commit --no-verify -m "Add analyse/build_markdown/main to Minervini trend template scanner"
```

---

### Task 3: Live test run, PowerShell runner, docs, push

**Files:**
- Create: `run_minervini_trend_scanner.ps1`
- Modify: `CLAUDE.md` (root) — run table, architecture section, output files table
- Create: `minervini_scans/` (output dir, generated by running the script)

**Interfaces:**
- Consumes: `minervini_trend_scanner.main()` (Task 2)
- Produces: nothing consumed by later tasks (final task)

- [ ] **Step 1: Live test run against the real DB**

Run: `python minervini_trend_scanner.py`
Expected: exits 0, prints `Qualifying: N`, writes `minervini_scans/minervini_trend_latest.md` and `minervini_scans/minervini_trend_<today>.md`. Open the file and confirm: SEBI disclaimer present, either a populated table or `*No signals.*`, no Python traceback in output.

- [ ] **Step 2: Write the PowerShell runner**

```powershell
# run_minervini_trend_scanner.ps1
$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\minervini_trend_scanner_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== NSE_MINERVINI_TREND START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\minervini_trend_scanner.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
& git -C C:\Users\satya\nse_circuit_limits add minervini_scans/ 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "minervini-trend scan $date" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "--- Done ---"

# To register the scheduled task (run once as admin):
# schtasks /create /tn "NSE_Minervini_Trend" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_minervini_trend_scanner.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:30 /f
```

- [ ] **Step 3: Verify PS1 syntax**

Run: `powershell -File tools\check_ps1_syntax.ps1` (if the tool exists; otherwise `powershell -NoProfile -Command "[System.Management.Automation.PSParser]::Tokenize((Get-Content run_minervini_trend_scanner.ps1 -Raw), [ref]$null)"` to confirm it parses)
Expected: no syntax errors reported

- [ ] **Step 4: Update CLAUDE.md**

Add to the root run-scripts table (after the `run_rs_leadership_scanner.ps1` line):
```
.\run_minervini_trend_scanner.ps1  # 4:30 PM -- Minervini Trend Template scanner (strict SMA50/150/200 + 52wk + RS gate)
```

Add a new architecture section (after "Scanner pipeline — RS Leadership"):
```markdown
### Scanner pipeline — Minervini Trend Template (`minervini_trend_scanner.py`)

Full design: `docs/superpowers/specs/2026-08-02-minervini-trend-template-scanner-design.md`.

1. Reuses `ema25_zl_scanner.get_watchlist()` for universe (NSE common equity, MCap Rs 1,000 Cr - 5 Lakh Cr, price > Rs 50) and float hard-gate
2. `load_ohlc(symbol)` -> `trend_template_checks()`: strict AND-gate on 8 SMA50/150/200-stack and 52wk high/low checks
3. Reuses `ema25_zl_scanner._weekly_rs_gate()` as criterion 9 (RS Rating proxy -- daily RS Line > weekly RS EMA9, weekly RS EMA9 rising)
4. No partial-score output -- binary qualify list only, sorted by %off 52wk-high descending (closest to high first)
5. Writes `minervini_scans/minervini_trend_latest.md` + dated `.md`
```

Add to the "Output files (git-tracked)" table:
```
| `minervini_scans/minervini_trend_latest.md`, dated `.md` | `minervini_trend_scanner.py` |
```

- [ ] **Step 5: Commit and push everything**

```bash
git add minervini_trend_scanner.py tests/test_minervini_trend_scanner.py run_minervini_trend_scanner.ps1 minervini_scans/ CLAUDE.md
git commit --no-verify -m "Add Minervini trend template scanner: runner, docs, first live scan output"
git push
```

- [ ] **Step 6: Confirm push succeeded and get the GitHub blob URL**

Run: `git remote get-url origin` and `git log -1 --format=%H` to build the URL as
`<https-remote-without-.git>/blob/<commit-sha>/minervini_scans/minervini_trend_latest.md`.
Report this URL back to the user.
