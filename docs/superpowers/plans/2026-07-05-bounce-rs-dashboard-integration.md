# Bounce-RS Dashboard Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Wire the merged `scanners/bounce_rs_scanner.py` into `wt_squeeze_dashboard.html` as a top-of-page table, populated once a day after real breadth data lands (~5:30 PM), visible only when the scanner has signals.

**Architecture:** A new thin scanner script (`run_bounce_rs_scanner.py`) builds a liquid watchlist, calls `scanners.bounce_rs_scanner.run()`, writes markdown (dated + latest). `wt_squeeze_dashboard.py` gains a parser for that markdown and a conditional top section, mirroring its existing `conf_section`/`sqz_section` pattern exactly. `run_breadth_monitor.ps1` gains two trailing steps so the dashboard rebuilds again after today's breadth data is written, since its normal 4:40 PM build happens before that data exists.

**Tech Stack:** pandas, `tradingview_screener` (`Query`/`col`), pytest.

## Global Constraints

- SEBI disclaimer on every generated `.md`: `from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER` — prepend header, append footer. `wt_squeeze_dashboard.html` already has its own banner/footer at the page level; the new section does not need its own disclaimer block.
- IST timestamps: `datetime.now(IST)` where `IST = timezone(timedelta(hours=5, minutes=30))` — matches every existing scanner. Never a naive `datetime.now()`.
- Git: `git commit --no-verify` in this repo (pre-commit hooks disabled/flaky, standing exception per `CLAUDE.md`).
- Output-file discipline (`scanner-conventions.md`): write both a dated file (`bounce_rs_scan_YYYY-MM-DD.md`) and `bounce_rs_scan_latest.md` in the same run; write `*No signals.*` on zero rows, never an empty file.
- `ohlc_db`/data access: the new scanner script does not touch SQLite directly — it only calls `scanners.bounce_rs_scanner.run()`, which already encapsulates all `ohlc_db` access.
- Watchlist filter: NSE common equity, `market_cap_basic` between ₹800 Cr (`800 * 1_00_00_000`) and ₹1 Lakh Cr (`1_00_000 * 1_00_00_000`) — same as `inside_bar_scanner.py::get_watchlist()`.
- `scanners/bounce_rs_scanner.py::run(universe_df, as_of) -> pd.DataFrame` returns columns exactly `["symbol", "rs_during_dip_%", "ema_type", "setup", "dip_low_ratio", "ratio_5d_now", "bounce_mag", "score"]` (`OUTPUT_COLUMNS`), sorted by `score` descending, empty (but column-complete) when no regime.
- Dashboard section placement: topmost, above `{wg_section}` in `wt_squeeze_dashboard.py`'s `build_html()` return string (`wt_squeeze_dashboard.py:550`) — above Trend×WT confluence, above everything.
- Dashboard section visibility: hidden entirely (empty string, no `<div>`) when there are zero rows — matches the existing `if conf_rows:` / `if sqz_rows:` pattern, no permanent placeholder.

---

### Task 1: `run_bounce_rs_scanner.py` — scanner runner script

**Files:**
- Create: `run_bounce_rs_scanner.py`

**Interfaces:**
- Consumes: `scanners.bounce_rs_scanner.run(universe_df: pd.DataFrame, as_of: date) -> pd.DataFrame` (already exists, columns per Global Constraints above).
- Produces: `bounce_rs_scans/bounce_rs_scan_latest.md` and `bounce_rs_scans/bounce_rs_scan_YYYY-MM-DD.md` — later tasks (the dashboard parser) read `bounce_rs_scan_latest.md`.

This script has no new pure logic of its own (all scanning logic already lives in, and is already tested in, `scanners/bounce_rs_scanner.py`) — it is I/O glue (TradingView query, file write), the same shape as `inside_bar_scanner.py`. No unit test file for this task; verification is a live run in Task 7.

- [ ] **Step 1: Write the file**

```python
#!/usr/bin/env python3
"""
Bounce-RS Scanner runner.
Builds a liquid NSE watchlist, calls scanners.bounce_rs_scanner.run(), writes markdown.

Watchlist: NSE common equity, MCap ₹800 Cr – ₹1 Lakh Cr (same filter as inside_bar_scanner.py)
Output:    bounce_rs_scans/bounce_rs_scan_latest.md + bounce_rs_scan_YYYY-MM-DD.md
"""

import os
import sys
from datetime import datetime, timezone, timedelta

import pandas as pd
from tradingview_screener import Query, col

from scanners.bounce_rs_scanner import run
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER

sys.stdout.reconfigure(encoding="utf-8")

IST = timezone(timedelta(hours=5, minutes=30))
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "bounce_rs_scans")

MC_LOW = 800 * 1_00_00_000  # ₹800 Cr
MC_HIGH = 1_00_000 * 1_00_00_000  # ₹1 Lakh Cr


def get_watchlist() -> list[str]:
    _, df = (
        Query()
        .set_markets("india")
        .select("name", "close")
        .where(
            col("exchange") == "NSE",
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
        )
        .limit(2000)
        .get_scanner_data()
    )
    return df["name"].tolist()


def build_markdown(result: pd.DataFrame, today: str, now_str: str) -> str:
    lines = [
        f"# Bounce-RS Scanner — {today}",
        f"*Generated {now_str}*",
        "",
    ]
    if result.empty:
        lines.append("*No signals.*")
    else:
        lines.append(
            "| Symbol | RS Dip% | EMA Type | Setup | Dip Low | Ratio Now | Bounce | Score |"
        )
        lines.append(
            "|--------|--------:|:--------:|-------|--------:|----------:|-------:|------:|"
        )
        for _, r in result.iterrows():
            tv = f"https://in.tradingview.com/chart/?symbol=NSE:{r['symbol']}"
            lines.append(
                f"| [{r['symbol']}]({tv}) "
                f"| {r['rs_during_dip_%']:.2f} "
                f"| {r['ema_type']} "
                f"| {r['setup']} "
                f"| {r['dip_low_ratio']:.2f} "
                f"| {r['ratio_5d_now']:.2f} "
                f"| {r['bounce_mag']:.2f} "
                f"| {r['score']:.2f} |"
            )
    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


def main():
    os.makedirs(SCANS_DIR, exist_ok=True)
    now_ist = datetime.now(IST)
    today = now_ist.strftime("%Y-%m-%d")
    now_str = now_ist.strftime("%Y-%m-%d %H:%M IST")

    print(f"[{now_str}] Bounce-RS Scanner — fetching watchlist...")
    watchlist = get_watchlist()
    print(f"  Watchlist: {len(watchlist)} stocks")

    universe_df = pd.DataFrame({"symbol": watchlist})
    result = run(universe_df, now_ist.date())
    print(f"  Signals: {len(result)}")

    md = build_markdown(result, today, now_str)
    latest_file = os.path.join(SCANS_DIR, "bounce_rs_scan_latest.md")
    dated_file = os.path.join(SCANS_DIR, f"bounce_rs_scan_{today}.md")
    with open(latest_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(dated_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  Saved -> {latest_file}")
    print(f"  Saved -> {dated_file}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Syntax/import check**

Run: `python -c "import ast; ast.parse(open('run_bounce_rs_scanner.py').read())"`
Expected: no output (parses clean).

Run: `python -c "import run_bounce_rs_scanner"` (from repo root)
Expected: no output (imports clean — confirms `from scanners.bounce_rs_scanner import run` and `from disclaimer import ...` resolve).

- [ ] **Step 3: Commit**

```bash
git add run_bounce_rs_scanner.py
git commit --no-verify -m "feat: add Bounce-RS scanner runner script"
```

---

### Task 2: `run_bounce_rs_scanner.ps1` — PowerShell runner

**Files:**
- Create: `run_bounce_rs_scanner.ps1`

**Interfaces:**
- Consumes: `run_bounce_rs_scanner.py` (Task 1).
- Produces: nothing new consumed by later tasks — this is a leaf runner, invoked by Task 5's `run_breadth_monitor.ps1` addition by filename only.

- [ ] **Step 1: Write the file**

```powershell
# run_bounce_rs_scanner.ps1 — Bounce-RS Scanner
# Invoked as a trailing step of run_breadth_monitor.ps1 (~5:30 PM+), after
# today's breadth ratio_5d row has been written to data/breadth_history.csv.
# Logs: logs/bounce_rs_scanner_YYYY-MM-DD.log

$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\bounce_rs_scanner_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== BOUNCE_RS_SCANNER START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\run_bounce_rs_scanner.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
& git -C C:\Users\satya\nse_circuit_limits add bounce_rs_scans 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "[scan $date] bounce_rs: scan run" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "--- Done ---"
```

- [ ] **Step 2: Verify PowerShell syntax**

Run: `powershell -NoProfile -Command "[System.Management.Automation.PSParser]::Tokenize((Get-Content 'run_bounce_rs_scanner.ps1' -Raw), [ref]$null) | Out-Null; Write-Output 'OK'"`
Expected: `OK` (no parse errors).

- [ ] **Step 3: Commit**

```bash
git add run_bounce_rs_scanner.ps1
git commit --no-verify -m "feat: add Bounce-RS scanner PowerShell runner"
```

---

### Task 3: `parse_bounce_rs()` — markdown parser in `wt_squeeze_dashboard.py`

**Files:**
- Modify: `wt_squeeze_dashboard.py`
- Test: `tests/test_wt_squeeze_dashboard_bounce_rs.py`

**Interfaces:**
- Produces: `parse_bounce_rs(content: str) -> list[dict]`. Each dict has keys `symbol, rs_pct, ema_type, setup, dip_low, ratio_now, bounce, score` — all values are the raw string cell content (already-formatted numbers from the markdown, e.g. `"8.23"`, not floats) except `symbol`, which is stripped of its markdown link syntax via the existing `_strip_md_link()` helper (`wt_squeeze_dashboard.py:55`).
- Consumes: nothing from other tasks — pure string-parsing function, no dependency on Task 1's live output.

This is a new test file (no prior test file exists for `wt_squeeze_dashboard.py`) — scoped only to the new parsing logic being added, not retrofitting tests onto the module's pre-existing untested functions.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_wt_squeeze_dashboard_bounce_rs.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from wt_squeeze_dashboard import parse_bounce_rs


def test_parse_bounce_rs_basic():
    md = (
        "# Bounce-RS Scanner — 2026-07-05\n\n"
        "| Symbol | RS Dip% | EMA Type | Setup | Dip Low | Ratio Now | Bounce | Score |\n"
        "|--------|--------:|:--------:|-------|--------:|----------:|-------:|------:|\n"
        "| [SBIN](https://in.tradingview.com/chart/?symbol=NSE:SBIN) | 8.23 | A | POCKET_PIVOT "
        "| 0.55 | 0.85 | 0.30 | 14.50 |\n"
    )
    rows = parse_bounce_rs(md)
    assert len(rows) == 1
    assert rows[0]["symbol"] == "SBIN"
    assert rows[0]["ema_type"] == "A"
    assert rows[0]["setup"] == "POCKET_PIVOT"
    assert rows[0]["score"] == "14.50"


def test_parse_bounce_rs_no_signals_returns_empty():
    md = "# Bounce-RS Scanner — 2026-07-05\n\n*No signals.*\n"
    assert parse_bounce_rs(md) == []


def test_parse_bounce_rs_empty_content_returns_empty():
    assert parse_bounce_rs("") == []


def test_parse_bounce_rs_multiple_rows_preserves_order():
    md = (
        "| Symbol | RS Dip% | EMA Type | Setup | Dip Low | Ratio Now | Bounce | Score |\n"
        "|--------|--------:|:--------:|-------|--------:|----------:|-------:|------:|\n"
        "| [AAA](url) | 10.0 | A | POCKET_PIVOT | 0.5 | 0.9 | 0.4 | 18.0 |\n"
        "| [BBB](url) | 2.0 | B | NONE | 0.6 | 0.8 | 0.2 | 5.0 |\n"
    )
    rows = parse_bounce_rs(md)
    assert [r["symbol"] for r in rows] == ["AAA", "BBB"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_wt_squeeze_dashboard_bounce_rs.py -v`
Expected: FAIL — `ImportError: cannot import name 'parse_bounce_rs'`.

- [ ] **Step 3: Write minimal implementation**

Add to `wt_squeeze_dashboard.py`, after `parse_wt_rows` (near line 95-175, directly following that function):

```python
def parse_bounce_rs(content: str) -> list[dict]:
    """Parse bounce_rs_scan_latest.md's 8-col table. '*No signals.*' or an
    empty file both correctly yield []."""
    rows = []
    for line in content.splitlines():
        ls = line.strip()
        if not ls.startswith("|"):
            continue
        if ls.startswith("|---") or ls.startswith("| ---"):
            continue
        parts = [p.strip() for p in ls.split("|")][1:-1]
        if len(parts) != 8:
            continue
        sym = _strip_md_link(parts[0])
        if not sym or sym == "Symbol":
            continue
        rows.append(
            {
                "symbol": sym,
                "rs_pct": parts[1],
                "ema_type": parts[2],
                "setup": parts[3],
                "dip_low": parts[4],
                "ratio_now": parts[5],
                "bounce": parts[6],
                "score": parts[7],
            }
        )
    return rows
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_wt_squeeze_dashboard_bounce_rs.py -v`
Expected: 4 passed.

- [ ] **Step 5: Commit**

```bash
git add wt_squeeze_dashboard.py tests/test_wt_squeeze_dashboard_bounce_rs.py
git commit --no-verify -m "feat: add Bounce-RS markdown parser to wt_squeeze_dashboard"
```

---

### Task 4: Top-of-dashboard section + `build_html()`/`main()` wiring

**Files:**
- Modify: `wt_squeeze_dashboard.py`
- Modify: `tests/test_wt_squeeze_dashboard_bounce_rs.py`

**Interfaces:**
- Consumes: `parse_bounce_rs(content: str) -> list[dict]` (Task 3, exact dict shape above).
- Produces: `_bounce_rs_section_html(rows: list[dict]) -> str` (empty string when `rows` is empty). Modifies `build_html(today, now_str, wt_rows, trend_info=None, bounce_rs_rows=None)` — new keyword-only-in-practice 5th parameter, defaults to `None`/treated as empty. Modifies `main()` to read `BOUNCE_RS_MD` and pass parsed rows through.

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_wt_squeeze_dashboard_bounce_rs.py`:

```python
from wt_squeeze_dashboard import _bounce_rs_section_html, build_html  # noqa: E402

_SAMPLE_ROW = {
    "symbol": "SBIN",
    "rs_pct": "8.23",
    "ema_type": "A",
    "setup": "POCKET_PIVOT",
    "dip_low": "0.55",
    "ratio_now": "0.85",
    "bounce": "0.30",
    "score": "14.50",
}


def test_bounce_rs_section_hidden_when_empty():
    assert _bounce_rs_section_html([]) == ""


def test_bounce_rs_section_shows_row_when_present():
    html = _bounce_rs_section_html([_SAMPLE_ROW])
    assert "SBIN" in html
    assert "POCKET_PIVOT" in html
    assert "(1 stocks)" in html


def test_build_html_includes_bounce_rs_section_when_rows_present():
    html = build_html(
        "2026-07-05", "2026-07-05 17:35 IST", [], bounce_rs_rows=[_SAMPLE_ROW]
    )
    assert "BOUNCE-RS" in html
    assert "SBIN" in html


def test_build_html_omits_bounce_rs_section_when_no_rows():
    html = build_html("2026-07-05", "2026-07-05 17:35 IST", [])
    assert "BOUNCE-RS" not in html


def test_build_html_bounce_rs_section_appears_before_wt_bar():
    """Topmost placement: bounce-rs section text appears before the stat bar's
    'WT Bull Cross' label, confirming it renders above every other section."""
    html = build_html(
        "2026-07-05", "2026-07-05 17:35 IST", [], bounce_rs_rows=[_SAMPLE_ROW]
    )
    assert html.index("BOUNCE-RS") < html.index("WT Bull Cross")
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_wt_squeeze_dashboard_bounce_rs.py -v`
Expected: FAIL — `ImportError: cannot import name '_bounce_rs_section_html'` (and `build_html` rejects the unexpected `bounce_rs_rows` kwarg once that import succeeds).

- [ ] **Step 3: Write minimal implementation**

Add to `wt_squeeze_dashboard.py`, after `parse_bounce_rs` (Task 3):

```python
_BOUNCE_RS_TABLE_HDR = """    <thead><tr>
      <th>Symbol</th><th>RS Dip%</th><th>EMA Type</th><th>Setup</th>
      <th>Dip Low</th><th>Ratio Now</th><th>Bounce</th><th>Score</th>
    </tr></thead>"""


def _bounce_rs_html_row(r: dict) -> str:
    tv = f"https://in.tradingview.com/chart/?symbol=NSE:{r['symbol']}"
    return (
        f'<tr><td class="sym"><a href="{tv}" target="_blank">{r["symbol"]}</a></td>'
        f'<td class="num">{r["rs_pct"]}</td>'
        f'<td class="mu">{r["ema_type"]}</td>'
        f'<td class="mu">{r["setup"]}</td>'
        f'<td class="num">{r["dip_low"]}</td>'
        f'<td class="num">{r["ratio_now"]}</td>'
        f'<td class="num">{r["bounce"]}</td>'
        f'<td class="num">{r["score"]}</td></tr>'
    )


def _bounce_rs_section_html(rows: list[dict]) -> str:
    """Bounce-RS top-of-dashboard table. Empty string (section hidden entirely)
    when rows is empty — a dip-bounce regime is rare, no permanent placeholder."""
    if not rows:
        return ""
    rows_html = [_bounce_rs_html_row(r) for r in rows]
    return f"""
<div class="section" style="border:1px solid #f97316;border-radius:6px;padding:12px;background:#1a0f00">
  <div class="stitle" style="color:#f97316;border-color:#f97316">
    🔄 BOUNCE-RS — positive RS through breadth dip, bounce confirmed
    <span class="cnt" style="color:#f97316">({len(rows)} stocks)</span>
  </div>
  <table>
{_BOUNCE_RS_TABLE_HDR}
    <tbody>{"".join(rows_html)}</tbody>
  </table>
</div>
"""
```

Modify `build_html`'s signature (`wt_squeeze_dashboard.py:417`):

```python
def build_html(
    today: str,
    now_str: str,
    wt_rows: list,
    trend_info: "dict | None" = None,
    bounce_rs_rows: "list | None" = None,
) -> str:
    trend_info = trend_info or {}
    bounce_rs_section = _bounce_rs_section_html(bounce_rs_rows or [])
```

(This second line goes right after the existing `trend_info = trend_info or {}` line.)

Modify the final return string (`wt_squeeze_dashboard.py:550`) — insert `{bounce_rs_section}` immediately before `{wg_section}`:

```python
{bounce_rs_section}
{wg_section}
{conf_section}
{rs_section}
{sqz_section}
```

Modify `main()` (`wt_squeeze_dashboard.py:583`): add the constant near the other `_MD` constants (`wt_squeeze_dashboard.py:34-35`):

```python
BOUNCE_RS_MD = os.path.join(BASE, "bounce_rs_scans", "bounce_rs_scan_latest.md")
```

and in `main()`, before the `html = build_html(...)` call:

```python
    bounce_rs_rows = parse_bounce_rs(read_file(BOUNCE_RS_MD))
    print(f"  Bounce-RS       : {len(bounce_rs_rows)}")
```

then update the call:

```python
    html = build_html(today, now_str, wt_rows, trend_info, bounce_rs_rows)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_wt_squeeze_dashboard_bounce_rs.py -v`
Expected: 9 passed (4 from Task 3 + 5 new).

- [ ] **Step 5: Commit**

```bash
git add wt_squeeze_dashboard.py tests/test_wt_squeeze_dashboard_bounce_rs.py
git commit --no-verify -m "feat: add Bounce-RS top-of-dashboard section to wt_squeeze_dashboard"
```

---

### Task 5: `run_breadth_monitor.ps1` — trailing steps

**Files:**
- Modify: `run_breadth_monitor.ps1`

**Interfaces:**
- Consumes: `run_bounce_rs_scanner.ps1` (Task 2), `run_wt_squeeze_dashboard.ps1` (pre-existing, unmodified).

- [ ] **Step 1: Add trailing steps**

The current file ends with (verify this is still the exact tail before editing):
```powershell
Log "=== BREADTH_MONITOR DONE ==="

# To register scheduled task (run once as admin):
# schtasks /create /tn "NSE_BreadthMonitor" /tr "powershell.exe -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File C:\Users\satya\nse_circuit_limits\run_breadth_monitor.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 17:30 /f
```

Replace `Log "=== BREADTH_MONITOR DONE ==="` and everything after it with:

```powershell
Log "=== BREADTH_MONITOR DONE ==="

# ── Step 5: Bounce-RS scanner + dashboard rebuild ─────────────────────────────
# Runs here (not at 4:40 PM) because today's ratio_5d row above must exist first.
Log "--- Running Bounce-RS scanner ---"
& "$ROOT\run_bounce_rs_scanner.ps1"
Log "--- Rebuilding WT+Squeeze dashboard with fresh Bounce-RS data ---"
& "$ROOT\run_wt_squeeze_dashboard.ps1"
Log "=== BOUNCE_RS + DASHBOARD REBUILD DONE ==="

# To register scheduled task (run once as admin):
# schtasks /create /tn "NSE_BreadthMonitor" /tr "powershell.exe -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File C:\Users\satya\nse_circuit_limits\run_breadth_monitor.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 17:30 /f
```

- [ ] **Step 2: Verify PowerShell syntax**

Run: `powershell -NoProfile -Command "[System.Management.Automation.PSParser]::Tokenize((Get-Content 'run_breadth_monitor.ps1' -Raw), [ref]$null) | Out-Null; Write-Output 'OK'"`
Expected: `OK`.

- [ ] **Step 3: Commit**

```bash
git add run_breadth_monitor.ps1
git commit --no-verify -m "feat: run Bounce-RS scanner + rebuild dashboard after breadth monitor"
```

---

### Task 6: `CLAUDE.md` documentation

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Add to the run-scripts list**

In the PowerShell run-scripts code block (the one listing `run_fetch_data.ps1`, `run_dashboard.ps1`, etc.), after the `run_breadth_monitor.ps1` line, add:

```
.\run_breadth_monitor.ps1       # fires after AllScanners (or 5:30 PM fallback)
                                 #   -> trailing: run_bounce_rs_scanner.ps1, then re-run_wt_squeeze_dashboard.ps1
```

(Edit the existing `run_breadth_monitor.ps1` line's trailing comment to add the second line shown above — do not duplicate the `.\run_breadth_monitor.ps1` invocation itself.)

- [ ] **Step 2: Add to the Output files (git-tracked) table**

Add a row:

```
| `bounce_rs_scans/bounce_rs_scan_latest.md` | `run_bounce_rs_scanner.py` |
```

- [ ] **Step 3: Note the dashboard's two-build-per-day behavior**

In the "Dashboard — WaveTrend + Squeeze (`wt_squeeze_dashboard.py`)" section, add one line after the existing description:

```
Builds twice daily: 4:40 PM (`run_wt_squeeze_dashboard.ps1`, no Bounce-RS data yet) and again
~5:30-5:35 PM (triggered by `run_breadth_monitor.ps1`'s trailing step, once today's breadth
ratio and Bounce-RS scan are both available).
```

- [ ] **Step 4: Commit**

```bash
git add CLAUDE.md
git commit --no-verify -m "docs: document Bounce-RS scanner runner and two-build dashboard schedule"
```

---

### Task 7: End-to-end live smoke test

**Files:** none created/modified — verification only.

- [ ] **Step 1: Run the full pytest suite**

Run: `pytest tests/ -v`
Expected: all tests pass, including the 9 new tests from Tasks 3-4.

- [ ] **Step 2: Run the scanner live**

Run: `python run_bounce_rs_scanner.py`
Expected: exits 0, prints a watchlist count and a signal count, writes `bounce_rs_scans/bounce_rs_scan_latest.md` and `bounce_rs_scans/bounce_rs_scan_YYYY-MM-DD.md` (today's date). Read the generated file and confirm it has the SEBI disclaimer header/footer and either a populated table or `*No signals.*`.

- [ ] **Step 3: Run the dashboard build live**

Run: `python wt_squeeze_dashboard.py`
Expected: exits 0, prints a `Bounce-RS       : N` line, writes `wt_squeeze_dashboard.html`. Open the file (or grep it) and confirm: if Task 7 Step 2 found 0 signals, the string `BOUNCE-RS` does NOT appear anywhere in the HTML; if it found signals, a `BOUNCE-RS` section appears before the `WT Bull Cross` stat bar label.

- [ ] **Step 4: If Step 2 found 0 signals (the common case), verify the section logic another way**

Since real market conditions rarely have an active dip-bounce regime, Step 3's "section absent" branch is the one actually exercised live. Confirm the "section present" branch works via the unit tests from Task 4 (already passing in Step 1) rather than waiting for a real signal day — this step exists only to record that reasoning, no new command to run.
