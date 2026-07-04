# NSE Delivery % Conviction Marker Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fetch NSE full-bhavcopy delivery% (`DELIV_PER`, EQ series only) daily, store in a new `delivery` table in `market.db`, and surface it as a spike marker (`DEL68%(T-1)`) on the Symbol column of the same 5 scanners that carry the CMF marker. Same-day backfill patches today's already-written scanner outputs (both `.md` and dependent `.html` dashboards) since delivery data always lands after those scanners already ran.

**Architecture:** `fetch_delivery.py` downloads/parses NSE bhavcopy and upserts into `delivery`. `ohlc_db.py` gets three new functions (`load_delivery`, `deliv_spike`, `deliv_tag`) mirroring the existing `cmf_days`/`cmf_tag` pair. `backfill_delivery_markers.py` idempotently patches today's already-written scanner `.md` files' Symbol cells, then re-runs the 3 HTML dashboard generators so HTML reflects it same-day. `run_fetch_delivery.ps1` chains fetch → backfill → git commit/push, scheduled ~6:15 PM IST. The 5 scanners get `deliv_tag(symbol)` wired into their Symbol cell permanently, alongside the existing `cmf_tag(df)` call, so every future run (starting tomorrow) picks it up automatically.

**Tech Stack:** Python (pandas, sqlite3, requests), pytest, PowerShell.

## Global Constraints

- No look-ahead bias: `deliv_spike`'s baseline must be computed from the prior N days only, strictly excluding today's row — from `backtesting-integrity.md`.
- `ohlc_db.py` is the only data entry point scanners import from — new delivery functions live there, scanners never touch the `delivery` table directly — from `scanner-conventions.md`.
- Never hand-edit generated output files — `backfill_delivery_markers.py` patches `.md` files programmatically, idempotently, never by hand — from `scanner-conventions.md`.
- Both dated + latest files must reflect the same state — backfill patches both, in the same run — from `scanner-conventions.md`.
- Never commit `market.db` — the new `delivery` table lives inside it like `ohlc`, no separate commit needed — from `CLAUDE.md`.
- This repo commits with `--no-verify` (pre-commit hooks disabled) — from `CLAUDE.md`.
- No Pine Script work — TradingView has no NSE deliverable-qty data feed, confirmed out of scope in the design spec.

---

## Task 1: Core functions in `ohlc_db.py`

**Files:**
- Modify: `ohlc_db.py` (add three functions after `cmf_tag()`, i.e. after line 258)
- Test: `tests/test_delivery.py` (new)

**Interfaces:**
- Produces: `load_delivery(symbol: str, lookback: int = 60, db_path: Path = DB_PATH) -> pd.DataFrame | None`, `deliv_spike(df: pd.DataFrame, n: int = 20, mult: float = 1.5) -> tuple[float, float] | None`, `deliv_tag(symbol: str, n: int = 20, mult: float = 1.5, db_path: Path = DB_PATH) -> str` — all imported by name from `ohlc_db` in Tasks 5–9.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_delivery.py`:

```python
import pandas as pd

import ohlc_db
from ohlc_db import deliv_spike, deliv_tag


def _synthetic_delivery_df(baseline_pct: float, today_pct: float, n: int = 20) -> pd.DataFrame:
    dates = pd.date_range("2026-01-01", periods=n + 1, freq="D")
    pcts = [baseline_pct] * n + [today_pct]
    return pd.DataFrame({"date": dates, "deliv_pct": pcts})


def test_deliv_spike_detects_spike_above_baseline():
    df = _synthetic_delivery_df(baseline_pct=20.0, today_pct=40.0)
    assert deliv_spike(df, n=20, mult=1.5) == (40.0, 20.0)


def test_deliv_spike_no_spike_below_multiplier():
    df = _synthetic_delivery_df(baseline_pct=20.0, today_pct=25.0)
    assert deliv_spike(df, n=20, mult=1.5) is None


def test_deliv_spike_excludes_today_from_baseline():
    """Baseline must use the prior n days only -- mutating today's value
    alone must never change the baseline (no look-ahead)."""
    df = _synthetic_delivery_df(baseline_pct=20.0, today_pct=40.0)
    _, baseline_a = deliv_spike(df, n=20, mult=1.5)
    df.loc[df.index[-1], "deliv_pct"] = 90.0
    _, baseline_b = deliv_spike(df, n=20, mult=1.5)
    assert baseline_a == baseline_b == 20.0


def test_deliv_spike_insufficient_rows_returns_none():
    df = _synthetic_delivery_df(baseline_pct=20.0, today_pct=40.0, n=5)
    assert deliv_spike(df, n=20, mult=1.5) is None


def test_deliv_tag_formats_spike(monkeypatch):
    df = _synthetic_delivery_df(baseline_pct=20.0, today_pct=68.0)
    monkeypatch.setattr(ohlc_db, "load_delivery", lambda symbol, lookback=21, db_path=None: df)
    assert deliv_tag("TEST") == "DEL68%(T-1)"


def test_deliv_tag_empty_when_no_spike(monkeypatch):
    df = _synthetic_delivery_df(baseline_pct=20.0, today_pct=22.0)
    monkeypatch.setattr(ohlc_db, "load_delivery", lambda symbol, lookback=21, db_path=None: df)
    assert deliv_tag("TEST") == ""


def test_deliv_tag_empty_when_no_data(monkeypatch):
    monkeypatch.setattr(ohlc_db, "load_delivery", lambda symbol, lookback=21, db_path=None: None)
    assert deliv_tag("TEST") == ""
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_delivery.py -v`
Expected: FAIL with `ImportError: cannot import name 'deliv_spike' from 'ohlc_db'`

- [ ] **Step 3: Implement `load_delivery`, `deliv_spike`, `deliv_tag`**

Insert immediately after `cmf_tag()` (after the line that closes it, currently line 258):

```python
DELIV_SPIKE_N = 20  # baseline window, trading days
DELIV_SPIKE_MULT = 1.5  # today must exceed baseline * mult to count as spike


def load_delivery(symbol: str, lookback: int = 60, db_path: Path = DB_PATH) -> pd.DataFrame | None:
    """Return (date, deliv_pct) for one symbol from the `delivery` table, oldest-first.
    None if symbol/table missing or DB error -- delivery data lags scanner runs by
    design, so 'no data yet' is expected, not an error state."""
    con = _connect(db_path)
    if con is None:
        return None
    try:
        df = pd.read_sql(
            "SELECT date, deliv_pct FROM delivery WHERE symbol=? ORDER BY date DESC LIMIT ?",
            con,
            params=(symbol, lookback),
        )
        if df.empty:
            return None
        df["date"] = pd.to_datetime(df["date"])
        return df.iloc[::-1].reset_index(drop=True)
    except Exception:
        return None
    finally:
        con.close()


def deliv_spike(
    df: pd.DataFrame, n: int = DELIV_SPIKE_N, mult: float = DELIV_SPIKE_MULT
) -> tuple[float, float] | None:
    """Returns (today_pct, baseline_pct) when today's deliv_pct exceeds the rolling
    mean of the PRIOR n days by `mult`. Baseline strictly excludes today's row --
    no look-ahead. None if no spike or fewer than n+1 rows."""
    if df is None or len(df) < n + 1:
        return None
    pct = df["deliv_pct"].astype(float)
    today_pct = float(pct.iloc[-1])
    baseline_pct = float(pct.iloc[-(n + 1) : -1].mean())
    if today_pct <= baseline_pct * mult:
        return None
    return today_pct, baseline_pct


def deliv_tag(
    symbol: str,
    n: int = DELIV_SPIKE_N,
    mult: float = DELIV_SPIKE_MULT,
    db_path: Path = DB_PATH,
) -> str:
    """'' if no spike / insufficient data. 'DEL{today_pct:.0f}%(T-1)' if spike.
    Binary flag, NOT always-on (unlike cmf_tag) -- only appears on genuine spike
    days. '(T-1)' is always accurate: bhavcopy for day T publishes after this
    scanner's run, so the latest row in `delivery` is always at least 1 trading
    day behind."""
    try:
        df = load_delivery(symbol, lookback=n + 1, db_path=db_path)
        result = deliv_spike(df, n=n, mult=mult)
        if result is None:
            return ""
        today_pct, _ = result
        return f"DEL{today_pct:.0f}%(T-1)"
    except Exception:
        return ""
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_delivery.py -v`
Expected: 7 passed

- [ ] **Step 5: Commit**

```bash
git add ohlc_db.py tests/test_delivery.py
git commit --no-verify -m "feat: add delivery% spike helper (load_delivery, deliv_spike, deliv_tag)"
```

---

## Task 2: `fetch_delivery.py`

**Files:**
- Create: `fetch_delivery.py`
- Test: `tests/test_fetch_delivery.py` (new)

**Interfaces:**
- Produces: `parse_bhavcopy_csv(csv_text: str) -> pd.DataFrame` (columns: `symbol, ttl_trd_qty, deliv_qty, deliv_pct`), `upsert_delivery(rows: pd.DataFrame, d: date, db_path: Path = DB_PATH) -> int`. Both are pure/DB-local helpers, not consumed by other tasks (Task 3's backfill reads via `ohlc_db.load_delivery`, not directly from this file).

- [ ] **Step 1: Write the failing tests**

Create `tests/test_fetch_delivery.py`:

```python
import sqlite3
from datetime import date

from fetch_delivery import parse_bhavcopy_csv, upsert_delivery


_SAMPLE_CSV = """SYMBOL ,SERIES ,DATE1 ,PREV_CLOSE ,OPEN_PRICE ,HIGH_PRICE ,LOW_PRICE ,LAST_PRICE ,CLOSE_PRICE ,AVG_PRICE ,TTL_TRD_QNTY ,TURNOVER_LACS ,NO_OF_TRADES ,DELIV_QTY ,DELIV_PER 
RELIANCE ,EQ ,04-JUL-2026 ,1500.00 ,1505.00 ,1520.00 ,1498.00 ,1510.00 ,1510.00 ,1508.50 ,1000000 ,15085.00 ,50000 ,650000 ,65.00 
TATASTEEL ,EQ ,04-JUL-2026 ,140.00 ,141.00 ,143.00 ,139.00 ,142.00 ,142.00 ,141.50 ,5000000 ,7075.00 ,80000 ,1500000 ,30.00 
IDEA ,BE ,04-JUL-2026 ,10.00 ,10.10 ,10.50 ,9.90 ,10.20 ,10.20 ,10.15 ,20000000 ,2030.00 ,10000 ,4000000 ,20.00 
"""


def test_parse_bhavcopy_csv_filters_eq_series_only():
    df = parse_bhavcopy_csv(_SAMPLE_CSV)
    assert set(df["symbol"]) == {"RELIANCE", "TATASTEEL"}


def test_parse_bhavcopy_csv_strips_whitespace_and_parses_numeric():
    df = parse_bhavcopy_csv(_SAMPLE_CSV)
    row = df[df["symbol"] == "RELIANCE"].iloc[0]
    assert row["deliv_pct"] == 65.0
    assert row["ttl_trd_qty"] == 1000000
    assert row["deliv_qty"] == 650000


def test_upsert_delivery_writes_and_replaces(tmp_path):
    db_path = tmp_path / "test_market.db"
    df = parse_bhavcopy_csv(_SAMPLE_CSV)
    d = date(2026, 7, 4)

    n = upsert_delivery(df, d, db_path=db_path)
    assert n == 2

    con = sqlite3.connect(db_path)
    row = con.execute(
        "SELECT deliv_pct FROM delivery WHERE symbol=? AND date=?",
        ("RELIANCE", "2026-07-04"),
    ).fetchone()
    con.close()
    assert row == (65.0,)

    n2 = upsert_delivery(df, d, db_path=db_path)
    assert n2 == 2
    con = sqlite3.connect(db_path)
    count = con.execute("SELECT COUNT(*) FROM delivery").fetchone()[0]
    con.close()
    assert count == 2
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_fetch_delivery.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'fetch_delivery'`

- [ ] **Step 3: Implement `fetch_delivery.py`**

Create `fetch_delivery.py`:

```python
#!/usr/bin/env python3
"""Fetch NSE full bhavcopy delivery% (DELIV_PER) for EQ-series stocks.
Upserts into market.db `delivery` table. Run ~6:15 PM IST via
run_fetch_delivery.ps1, after NSE publishes the day's bhavcopy."""

import sqlite3
import sys
from datetime import date
from io import StringIO
from pathlib import Path

import pandas as pd
import requests

DB_PATH = Path(__file__).parent / ".ohlc_data" / "market.db"

_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"


def fetch_bhavcopy_csv(d: date) -> str:
    """Download raw bhavcopy CSV text for date d. Raises on non-200/network error."""
    url = (
        "https://nsearchives.nseindia.com/products/content/"
        f"sec_bhavdata_full_{d.strftime('%d%m%Y')}.csv"
    )
    session = requests.Session()
    session.headers.update({"User-Agent": _USER_AGENT})
    session.get("https://www.nseindia.com", timeout=10)  # cookie warm-up
    resp = session.get(url, timeout=15)
    resp.raise_for_status()
    return resp.text


def parse_bhavcopy_csv(csv_text: str) -> pd.DataFrame:
    """Parse bhavcopy CSV text -> DataFrame(symbol, ttl_trd_qty, deliv_qty, deliv_pct),
    EQ series only. NSE bhavcopy pads both header names and string values with
    whitespace -- strip both."""
    df = pd.read_csv(StringIO(csv_text))
    df.columns = [c.strip() for c in df.columns]
    df["SERIES"] = df["SERIES"].str.strip()
    df = df[df["SERIES"] == "EQ"].copy()
    df["SYMBOL"] = df["SYMBOL"].str.strip()
    out = pd.DataFrame(
        {
            "symbol": df["SYMBOL"],
            "ttl_trd_qty": pd.to_numeric(df["TTL_TRD_QNTY"], errors="coerce"),
            "deliv_qty": pd.to_numeric(df["DELIV_QTY"], errors="coerce"),
            "deliv_pct": pd.to_numeric(df["DELIV_PER"], errors="coerce"),
        }
    )
    return out.dropna(subset=["symbol"]).reset_index(drop=True)


def upsert_delivery(rows: pd.DataFrame, d: date, db_path: Path = DB_PATH) -> int:
    """Upsert rows into the `delivery` table for date d. Creates the table on
    first run. Returns row count written."""
    con = sqlite3.connect(db_path)
    try:
        con.execute(
            "CREATE TABLE IF NOT EXISTS delivery ("
            "symbol TEXT, date DATE, ttl_trd_qty INTEGER, deliv_qty INTEGER, deliv_pct REAL, "
            "PRIMARY KEY (symbol, date))"
        )
        date_str = d.isoformat()
        con.executemany(
            "INSERT OR REPLACE INTO delivery (symbol, date, ttl_trd_qty, deliv_qty, deliv_pct) "
            "VALUES (?, ?, ?, ?, ?)",
            [
                (r.symbol, date_str, int(r.ttl_trd_qty), int(r.deliv_qty), float(r.deliv_pct))
                for r in rows.itertuples()
            ],
        )
        con.commit()
        return len(rows)
    finally:
        con.close()


def main() -> None:
    d = date.today()
    try:
        csv_text = fetch_bhavcopy_csv(d)
    except Exception as e:
        print(f"fetch_delivery: bhavcopy fetch failed for {d.isoformat()}: {e}", file=sys.stderr)
        sys.exit(1)
    rows = parse_bhavcopy_csv(csv_text)
    n = upsert_delivery(rows, d)
    print(f"fetch_delivery: wrote {n} EQ rows for {d.isoformat()}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_fetch_delivery.py -v`
Expected: 3 passed

- [ ] **Step 5: Commit**

```bash
git add fetch_delivery.py tests/test_fetch_delivery.py
git commit --no-verify -m "feat: add fetch_delivery.py -- NSE bhavcopy delivery% fetch/parse/upsert"
```

---

## Task 3: `backfill_delivery_markers.py`

**Files:**
- Create: `backfill_delivery_markers.py`
- Test: `tests/test_backfill_delivery_markers.py` (new)

**Interfaces:**
- Consumes: `deliv_tag(symbol) -> str` from Task 1 (used as the default tagger in `main()`; tests inject a fake tagger).
- Produces: `patch_symbol_line(line: str, tagger) -> str`, `patch_md_file(path: Path, tagger) -> int` -- not consumed elsewhere, but `main()` (this task) is invoked directly by `run_fetch_delivery.ps1` in Task 4.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_backfill_delivery_markers.py`:

```python
from backfill_delivery_markers import patch_md_file, patch_symbol_line


def _tagger(spikes):
    return lambda symbol: spikes.get(symbol, "")


def test_patch_symbol_line_adds_tag_no_existing_sub():
    line = "| [RELIANCE](https://tv.example/RELIANCE) | 3d | +1.2% |\n"
    out = patch_symbol_line(line, _tagger({"RELIANCE": "DEL68%(T-1)"}))
    assert out.startswith(
        "| [RELIANCE](https://tv.example/RELIANCE)<br><sub>DEL68%(T-1)</sub>"
    )


def test_patch_symbol_line_appends_to_existing_sub():
    line = "| [RELIANCE](https://tv.example/RELIANCE)<br><sub>↑CMF3d</sub> | 3d |\n"
    out = patch_symbol_line(line, _tagger({"RELIANCE": "DEL68%(T-1)"}))
    assert "<sub>↑CMF3d · DEL68%(T-1)</sub>" in out


def test_patch_symbol_line_idempotent_rerun():
    line = "| [RELIANCE](https://tv.example/RELIANCE) | 3d |\n"
    tagger = _tagger({"RELIANCE": "DEL68%(T-1)"})
    once = patch_symbol_line(line, tagger)
    twice = patch_symbol_line(once, tagger)
    assert once == twice


def test_patch_symbol_line_removes_stale_tag_when_no_longer_spiking():
    line = "| [RELIANCE](https://tv.example/RELIANCE)<br><sub>DEL68%(T-1)</sub> | 3d |\n"
    out = patch_symbol_line(line, _tagger({}))
    assert "DEL" not in out
    assert "<sub>" not in out


def test_patch_symbol_line_handles_rs_highline_extra_bracket():
    line = "| [RELIANCE](https://tv.example/RELIANCE) [20% ] | 150.00 |\n"
    out = patch_symbol_line(line, _tagger({"RELIANCE": "DEL68%(T-1)"}))
    assert out.startswith(
        "| [RELIANCE](https://tv.example/RELIANCE) [20% ]<br><sub>DEL68%(T-1)</sub>"
    )


def test_patch_symbol_line_ignores_non_data_rows():
    header = "| Symbol | Days |\n"
    assert patch_symbol_line(header, _tagger({"RELIANCE": "DEL68%(T-1)"})) == header


def test_patch_md_file_idempotent(tmp_path):
    p = tmp_path / "sample.md"
    p.write_text("| [RELIANCE](https://tv.example/RELIANCE) | 3d |\n", encoding="utf-8")
    tagger = _tagger({"RELIANCE": "DEL68%(T-1)"})

    n1 = patch_md_file(p, tagger)
    content_once = p.read_text(encoding="utf-8")
    n2 = patch_md_file(p, tagger)
    content_twice = p.read_text(encoding="utf-8")

    assert n1 == 1
    assert n2 == 0
    assert content_once == content_twice
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_backfill_delivery_markers.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'backfill_delivery_markers'`

- [ ] **Step 3: Implement `backfill_delivery_markers.py`**

Create `backfill_delivery_markers.py`:

```python
#!/usr/bin/env python3
"""Same-day backfill: patch today's already-written scanner .md Symbol cells
with the delivery% spike marker (fetch_delivery.py runs after those scanners
already produced today's output), then re-run the HTML dashboard generators
so HTML reflects it same-day too. Idempotent -- safe to re-run."""

import re
import sqlite3
import subprocess
import sys
from datetime import date
from pathlib import Path

from ohlc_db import DB_PATH, deliv_tag

BASE = Path(__file__).parent

_SYM_RE = re.compile(r"^\|\s*\[([A-Z0-9&\-]+)\]\(")
_SUB_RE = re.compile(r"<br><sub>(.*?)</sub>")
_DEL_TOKEN_RE = re.compile(r"DEL\d+%\(T-1\)")

SCANNER_MD_FILES = [
    ("wt_scans", "wt_bullcross_{date}.md", "wt_bullcross_latest.md"),
    ("ema25_zl_scans", "ema25_zl_scans_{date}.md", "ema25_zl_scans.md"),
    ("weekly_zl_scans", "weekly_zl_scans_{date}.md", "weekly_zl_scans.md"),
    ("trend_scans", "trend_scan_{date}.md", "trend_scan_latest.md"),
    ("rs_highline_scans", "rs_highline_{date}.md", "rs_highline_latest.md"),
]

HTML_GENERATORS = ["wt_squeeze_dashboard.py", "dashboard_generator.py", "trend_dashboard.py"]


def _strip_del_token(sub_content: str) -> str:
    parts = [p for p in sub_content.split(" · ") if p and not _DEL_TOKEN_RE.fullmatch(p)]
    return " · ".join(parts)


def patch_symbol_line(line: str, tagger) -> str:
    """Idempotently add/replace/remove the DEL{pct}%(T-1) token in a scanner
    markdown row's Symbol cell. Returns the line unchanged if it's not a data
    row (no leading '| [SYMBOL](')."""
    m = _SYM_RE.match(line)
    if not m:
        return line
    symbol = m.group(1)
    tag = tagger(symbol)

    sub_match = _SUB_RE.search(line)
    if sub_match:
        existing = _strip_del_token(sub_match.group(1))
        tokens = [t for t in existing.split(" · ") if t]
        if tag:
            tokens.append(tag)
        new_sub_content = " · ".join(tokens)
        if new_sub_content:
            return line[: sub_match.start()] + f"<br><sub>{new_sub_content}</sub>" + line[sub_match.end() :]
        return line[: sub_match.start()] + line[sub_match.end() :]

    if not tag:
        return line
    insert_at = line.index(")", m.end()) + 1
    rest = line[insert_at:]
    extra_bracket = re.match(r"^\s?\[[^\]]*\]", rest)
    if extra_bracket:
        insert_at += extra_bracket.end()
    return line[:insert_at] + f"<br><sub>{tag}</sub>" + line[insert_at:]


def patch_md_file(path: Path, tagger) -> int:
    """Patch every data row's Symbol cell in-place. Returns count of changed rows."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    changed = 0
    new_lines = []
    for line in lines:
        patched = patch_symbol_line(line, tagger)
        if patched != line:
            changed += 1
        new_lines.append(patched)
    path.write_text("".join(new_lines), encoding="utf-8")
    return changed


def _has_todays_delivery_data(today: str) -> bool:
    try:
        con = sqlite3.connect(DB_PATH)
        row = con.execute("SELECT 1 FROM delivery WHERE date=? LIMIT 1", (today,)).fetchone()
        con.close()
        return row is not None
    except Exception:
        return False


def main() -> None:
    today = date.today().isoformat()
    if not _has_todays_delivery_data(today):
        print("backfill_delivery_markers: no delivery data for today, skipping")
        return

    total = 0
    for dirname, dated_tmpl, latest_name in SCANNER_MD_FILES:
        for name in (dated_tmpl.format(date=today), latest_name):
            path = BASE / dirname / name
            if path.exists():
                total += patch_md_file(path, deliv_tag)
    print(f"backfill_delivery_markers: patched {total} rows")

    for script in HTML_GENERATORS:
        subprocess.run([sys.executable, str(BASE / script)], check=True)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_backfill_delivery_markers.py -v`
Expected: 7 passed

- [ ] **Step 5: Commit**

```bash
git add backfill_delivery_markers.py tests/test_backfill_delivery_markers.py
git commit --no-verify -m "feat: add backfill_delivery_markers.py -- same-day scanner .md/.html patch"
```

---

## Task 4: `run_fetch_delivery.ps1` + `CLAUDE.md` run table

**Files:**
- Create: `run_fetch_delivery.ps1`
- Modify: `CLAUDE.md` (add to "Running the scanners" list)

**Interfaces:**
- Consumes: `fetch_delivery.py` (Task 2) and `backfill_delivery_markers.py` (Task 3) as subprocesses.

- [ ] **Step 1: Create the runner script**

Create `run_fetch_delivery.ps1`, matching `run_rs_highline_scanner.ps1`'s structure exactly:

```powershell
$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\fetch_delivery_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== FETCH_DELIVERY START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\fetch_delivery.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\backfill_delivery_markers.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
$scanDate = Get-Date -Format "yyyy-MM-dd"
& git -C C:\Users\satya\nse_circuit_limits add wt_scans/ ema25_zl_scans/ weekly_zl_scans/ trend_scans/ rs_highline_scans/ wt_squeeze_dashboard.html dashboard.html trend_dashboard.html 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "[scan $scanDate] delivery backfill: symbol markers updated" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "--- Done ---"

# To register the scheduled task (run once as admin):
# schtasks /create /tn "NSE_FetchDelivery" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_fetch_delivery.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 18:15 /f
```

- [ ] **Step 2: Add to `CLAUDE.md` run table**

Find this line in the "Running the scanners" PowerShell block:
```
.\run_rs_highline_scanner.ps1    # 4:30 PM — RS high-line cross scanner
```
Add immediately after it:
```
.\run_fetch_delivery.ps1        # 6:15 PM — NSE bhavcopy delivery% fetch + same-day marker backfill
```

- [ ] **Step 3: Commit**

```bash
git add run_fetch_delivery.ps1 CLAUDE.md
git commit --no-verify -m "feat: add run_fetch_delivery.ps1 runner, document in CLAUDE.md"
```

---

## Task 5: Wire into `wt_bullcross_scanner.py`

**Files:**
- Modify: `wt_bullcross_scanner.py:35` (import), `:382` (finding dict), `:436-437` (`_row` extras)

**Interfaces:**
- Consumes: `deliv_tag(symbol: str) -> str` from Task 1.

- [ ] **Step 1: Import `deliv_tag`**

Current line 35:
```python
from ohlc_db import load_ohlc_many, get_names, liq_tag, cmf_tag
```
Change to:
```python
from ohlc_db import load_ohlc_many, get_names, liq_tag, cmf_tag, deliv_tag
```

- [ ] **Step 2: Store `deliv_tag` in the finding dict**

Current lines 381-382:
```python
            "liq_tag": liq_tag(df_raw),
            "cmf_tag": cmf_tag(df_raw),
```
Change to:
```python
            "liq_tag": liq_tag(df_raw),
            "cmf_tag": cmf_tag(df_raw),
            "deliv_tag": deliv_tag(symbol),
```

- [ ] **Step 3: Append marker to the Symbol cell extras**

Current (lines 436-437):
```python
    if f.get("cmf_tag"):
        extras.append(f["cmf_tag"])
    sym_cell = f"[{sym}]({tv})" + (
```
Change to:
```python
    if f.get("cmf_tag"):
        extras.append(f["cmf_tag"])
    if f.get("deliv_tag"):
        extras.append(f["deliv_tag"])
    sym_cell = f"[{sym}]({tv})" + (
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
    'cmf_tag': '', 'deliv_tag': 'DEL68%(T-1)',
}
row = _row(f, {})
assert 'DEL68%(T-1)' in row, row
print('OK:', row)
"
```
Expected: prints `OK: | [TEST](...)<br><sub>DEL68%(T-1)</sub> | ...` (no traceback)

- [ ] **Step 5: Commit**

```bash
git add wt_bullcross_scanner.py
git commit --no-verify -m "feat: add delivery% marker to wt_bullcross_scanner Symbol column"
```

---

## Task 6: Wire into `ema25_zl_scanner.py`

**Files:**
- Modify: `ema25_zl_scanner.py:34` (import), `:258` (finding dict), `:308-309` (`_table_rows`)

**Interfaces:**
- Consumes: `deliv_tag` from Task 1.

- [ ] **Step 1: Import `deliv_tag`**

Current line 34:
```python
from ohlc_db import load_ohlc, get_names, liq_tag, cmf_tag
```
Change to:
```python
from ohlc_db import load_ohlc, get_names, liq_tag, cmf_tag, deliv_tag
```

- [ ] **Step 2: Store `deliv_tag` in the finding dict**

Current lines 257-258:
```python
            "liq_tag": liq_tag(raw),
            "cmf_tag": cmf_tag(raw),
```
Change to:
```python
            "liq_tag": liq_tag(raw),
            "cmf_tag": cmf_tag(raw),
            "deliv_tag": deliv_tag(symbol),
```

- [ ] **Step 3: Append to the Symbol subline**

Current (lines 308-309):
```python
        cmf = f.get("cmf_tag", "")
        sym_cell = f"[{sym}]({tv})" + (f"<br><sub>{cmf}</sub>" if cmf else "")
```
Change to:
```python
        extras = [t for t in (f.get("cmf_tag", ""), f.get("deliv_tag", "")) if t]
        sym_cell = f"[{sym}]({tv})" + (f"<br><sub>{' · '.join(extras)}</sub>" if extras else "")
```

- [ ] **Step 4: Smoke-check the row output**

Run:
```bash
python -c "
from ema25_zl_scanner import _table_rows
f = {
    'symbol': 'TEST', 'zl_days': 3, 'zl_pct': 1.2, 'day_chg': 0.4,
    'squeeze': False, 'close': 123.45, 'cmf_tag': '', 'deliv_tag': 'DEL68%(T-1)',
}
rows = _table_rows([f], {})
assert any('DEL68%(T-1)' in r for r in rows), rows
print('OK:', rows[-1])
"
```
Expected: prints `OK: | [TEST](...)<br><sub>DEL68%(T-1)</sub> | ...` (no traceback)

- [ ] **Step 5: Commit**

```bash
git add ema25_zl_scanner.py
git commit --no-verify -m "feat: add delivery% marker to ema25_zl_scanner Symbol column"
```

---

## Task 7: Wire into `weekly_zl_scanner.py`

**Files:**
- Modify: `weekly_zl_scanner.py:28` (import), `:244-245` (finding dict), `:302-303` (`_table_rows`)

**Interfaces:**
- Consumes: `deliv_tag` from Task 1.

- [ ] **Step 1: Import `deliv_tag`**

Current line 28:
```python
from ohlc_db import load_ohlc, get_names, liq_tag, cmf_tag
```
Change to:
```python
from ohlc_db import load_ohlc, get_names, liq_tag, cmf_tag, deliv_tag
```

- [ ] **Step 2: Store `deliv_tag` in the finding dict**

Current lines 244-245:
```python
            "liq_tag": liq_tag(daily),
            "cmf_tag": cmf_tag(daily),
```
Change to:
```python
            "liq_tag": liq_tag(daily),
            "cmf_tag": cmf_tag(daily),
            "deliv_tag": deliv_tag(symbol),
```

- [ ] **Step 3: Append to the Symbol subline**

Current (lines 302-303):
```python
        cmf = f.get("cmf_tag", "")
        sym_cell = f"[{sym}]({tv})" + (f"<br><sub>{cmf}</sub>" if cmf else "")
```
Change to:
```python
        extras = [t for t in (f.get("cmf_tag", ""), f.get("deliv_tag", "")) if t]
        sym_cell = f"[{sym}]({tv})" + (f"<br><sub>{' · '.join(extras)}</sub>" if extras else "")
```

- [ ] **Step 4: Smoke-check the row output**

Run:
```bash
python -c "
from weekly_zl_scanner import _table_rows
f = {
    'symbol': 'TEST', 'zl_weeks': 2, 'zl_pct': 1.1, 'day_chg': 0.3,
    'sqz_weeks': 0, 'sqz_on': False, 'price_vs_zl': 'TOUCH',
    'consec_weeks': 4, 'close': 200.0, 'cmf_tag': '', 'deliv_tag': 'DEL68%(T-1)',
}
rows = _table_rows([f], {})
assert any('DEL68%(T-1)' in r for r in rows), rows
print('OK:', rows[-1])
"
```
Expected: prints `OK: | [TEST](...)<br><sub>DEL68%(T-1)</sub> | ...` (no traceback)

- [ ] **Step 5: Commit**

```bash
git add weekly_zl_scanner.py
git commit --no-verify -m "feat: add delivery% marker to weekly_zl_scanner Symbol column"
```

---

## Task 8: Wire into `trend_scanner.py`

**Files:**
- Modify: `trend_scanner.py:35` (import), `:413-414` (finding dict), `:455-456` (`_row`)

**Interfaces:**
- Consumes: `deliv_tag` from Task 1.

- [ ] **Step 1: Import `deliv_tag`**

Current line 35:
```python
from ohlc_db import load_ohlc_many, get_names, liq_tag, cmf_tag
```
Change to:
```python
from ohlc_db import load_ohlc_many, get_names, liq_tag, cmf_tag, deliv_tag
```

- [ ] **Step 2: Store `deliv_tag` in the finding dict**

Current lines 413-414:
```python
            "liq_tag": liq_tag(df_raw),
            "cmf_tag": cmf_tag(df_raw),
```
Change to:
```python
            "liq_tag": liq_tag(df_raw),
            "cmf_tag": cmf_tag(df_raw),
            "deliv_tag": deliv_tag(symbol),
```

- [ ] **Step 3: Append to the Symbol subline**

Current (lines 455-456):
```python
    cmf = f.get("cmf_tag", "")
    sym_cell = f"[{sym}]({tv})" + (f"<br><sub>{cmf}</sub>" if cmf else "")
```
Change to:
```python
    extras = [t for t in (f.get("cmf_tag", ""), f.get("deliv_tag", "")) if t]
    sym_cell = f"[{sym}]({tv})" + (f"<br><sub>{' · '.join(extras)}</sub>" if extras else "")
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
    'cmf_tag': '', 'deliv_tag': 'DEL68%(T-1)',
}
row = _row(f, {})
assert 'DEL68%(T-1)' in row, row
print('OK:', row)
"
```
Expected: prints `OK: | [TEST](...)<br><sub>DEL68%(T-1)</sub> | ...` (no traceback)

- [ ] **Step 5: Commit**

```bash
git add trend_scanner.py
git commit --no-verify -m "feat: add delivery% marker to trend_scanner Symbol column"
```

---

## Task 9: Wire into `rs_highline_scanner.py`

**Files:**
- Modify: `rs_highline_scanner.py:19` (import), `:325-326` (finding dict), `:357-358` (`_row`)

**Interfaces:**
- Consumes: `deliv_tag` from Task 1.

- [ ] **Step 1: Import `deliv_tag`**

Current line 19:
```python
from ohlc_db import load_ohlc_many, get_names, liq_tag, cmf_tag
```
Change to:
```python
from ohlc_db import load_ohlc_many, get_names, liq_tag, cmf_tag, deliv_tag
```

- [ ] **Step 2: Store `deliv_tag` in the finding dict**

Current lines 325-326:
```python
            "liq_tag": liq_tag(df),
            "cmf_tag": cmf_tag(df),
```
Change to:
```python
            "liq_tag": liq_tag(df),
            "cmf_tag": cmf_tag(df),
            "deliv_tag": deliv_tag(symbol),
```

- [ ] **Step 3: Append to the Symbol subline**

Current (lines 357-358):
```python
    cmf = f.get("cmf_tag", "")
    sym_cell = f"[{sym}]({tv}) [{circuit_cell}]" + (f"<br><sub>{cmf}</sub>" if cmf else "")
```
Change to:
```python
    extras = [t for t in (f.get("cmf_tag", ""), f.get("deliv_tag", "")) if t]
    sym_cell = f"[{sym}]({tv}) [{circuit_cell}]" + (f"<br><sub>{' · '.join(extras)}</sub>" if extras else "")
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
    'earliness': 55.0, 'liq_tag': '→₹12Cr · ₹10Cr',
    'cmf_tag': '', 'deliv_tag': 'DEL68%(T-1)',
}
row = _row(f, {}, {})
assert 'DEL68%(T-1)' in row, row
print('OK:', row)
"
```
Expected: prints `OK: | [TEST](...) [20% ]<br><sub>DEL68%(T-1)</sub> | ...` (no traceback)

- [ ] **Step 5: Commit**

```bash
git add rs_highline_scanner.py
git commit --no-verify -m "feat: add delivery% marker to rs_highline_scanner Symbol column"
```

---

## Spec Coverage Check

- `delivery` table schema, NSE bhavcopy source, EQ-series filter → Task 2
- `load_delivery`/`deliv_spike`/`deliv_tag`, relative-spike-vs-baseline logic, no-look-ahead baseline → Task 1
- `fetch_delivery.py` + `run_fetch_delivery.ps1` scheduled ~6:15 PM → Tasks 2, 4
- Same-day backfill of already-written `.md` + re-run of 3 HTML generators, idempotent patching → Task 3
- Permanent wiring into all 5 scanners' Symbol cell → Tasks 5–9
- `CLAUDE.md` run table updated → Task 4
- Error handling (fetch failure ≠ fatal, skip-if-no-data, never partial file) → Tasks 2 Step 3 (`main` exit 1 on fetch failure), Task 3 Step 3 (`_has_todays_delivery_data` guard)
- No Pine Script changes → confirmed, no such task added
