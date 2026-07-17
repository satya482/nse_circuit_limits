> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# NIFTY 50 ZLEMA25 Trend Scanner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a production-ready daily NIFTY 50 scanner with separate ZLEMA25 uptrend and downtrend tables, full current-trend age, youngest-first sorting, and symmetric age-bucket watchlists.

**Architecture:** Add one dedicated root-level scanner that reuses the existing EMA25 ZL indicator, squeeze, circuit, label, and OHLC helpers without changing the broad-market scanner. It refreshes and validates the official NSE constituent CSV with an atomic cached fallback, calculates strict slope direction and consecutive-bar age for every constituent with sufficient local history, and atomically writes a disclaimer-compliant Markdown report. A focused test module owns the pure contracts; a PowerShell runner and the existing orchestrator provide production execution.

**Tech Stack:** Python 3.13, pandas, requests, `ohlc_db.py`, `ema25_zl_scanner.py`, pytest, PowerShell, Markdown.

## Global Constraints

- Daily ZLEMA25 formula must remain `2 * EMA(close, 25) - EMA(EMA(close, 25), 25)` and match `ema25_zl_scanner.py`.
- Scan only the current NIFTY 50 universe; require exactly 50 unique non-empty symbols when accepting a constituent file.
- Apply no market-cap, price, RS, liquidity, or float-trap exclusion gates.
- Uptrend means strict positive ZLEMA25 slope; downtrend means strict negative slope; exact equality is flat and belongs to neither table.
- Age is consecutive trading bars in the active direction, with the first direction-change bar reported as `1d`.
- Sort each table by ascending age and then symbol.
- Use buckets `1d`, `2d`, `3d`, `4-5d`, `6-10d`, `11-15d`, and `15d+` for both directions.
- Load OHLC through `ohlc_db.py`; do not read SQLite directly.
- Every new Markdown file must contain the string `SEBI registered` and generated reports must use `SEBI_MD_HEADER` and `SEBI_MD_FOOTER`.
- Preserve unrelated shared-worktree changes and update `HANDOFF.md` when implementation is complete.
- Use `git commit --no-verify` for every repository commit.

## File Structure

- Create `nifty50_zlema25_scanner.py`: universe refresh/cache, pure trend calculation, symbol analysis, Markdown rendering, atomic output, and CLI entry point.
- Create `tests/test_nifty50_zlema25_scanner.py`: all scanner contracts with synthetic OHLC and temporary constituent caches; no network or live database access.
- Create `data/nifty50_constituents.csv`: last known valid official NSE constituent response used for first-run fallback.
- Create `run_nifty50_zlema25_scanner.ps1`: dated logging, scanner execution, exit propagation, and generated-output-only Git publication.
- Modify `run_all_scanners.ps1`: invoke the new job beside the existing daily EMA25 ZL job.
- Modify `CLAUDE.md`: document the manual command, scheduled runner, data source, report path, and semantics.
- Modify `HANDOFF.md`: record implementation status, files, verification evidence, and takeover instructions.

---

### Task 1: Constituent refresh and cached fallback

**Files:**
- Create: `nifty50_zlema25_scanner.py`
- Create: `tests/test_nifty50_zlema25_scanner.py`
- Create: `data/nifty50_constituents.csv`

**Interfaces:**
- Consumes: official CSV URL `https://nsearchives.nseindia.com/content/indices/ind_nifty50list.csv`; a `requests`-compatible client exposing `get(url, headers, timeout)`.
- Produces: `parse_constituents_csv(text: str) -> list[str]`; `load_nifty50_constituents(cache_path: Path = CACHE_FILE, http_client=requests) -> tuple[list[str], str]`, where source is `"NSE refresh"` or `"cached CSV"`.

- [ ] **Step 1: Write failing constituent tests**

Add imports and tests that build a 50-row CSV with `Company Name,Industry,Symbol,Series,ISIN Code`, assert normalization and alphabetical output, reject 49/duplicate/blank symbol sets, write a valid remote response atomically to `tmp_path / "nifty50.csv"`, and fall back to that cache when the fake client raises `requests.RequestException`.

```python
import csv
from io import StringIO
from pathlib import Path

import pytest
import requests

import nifty50_zlema25_scanner as scanner


def constituent_csv(symbols: list[str]) -> str:
    out = StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=["Company Name", "Industry", "Symbol", "Series", "ISIN Code"],
        lineterminator="\n",
    )
    writer.writeheader()
    for symbol in symbols:
        writer.writerow({"Company Name": symbol, "Symbol": symbol, "Series": "EQ"})
    return out.getvalue()


def symbols_50() -> list[str]:
    return [f"SYM{i:02d}" for i in range(50)]


def test_parse_constituents_requires_exactly_50_unique_symbols():
    assert scanner.parse_constituents_csv(constituent_csv(reversed(symbols_50()))) == symbols_50()
    with pytest.raises(ValueError, match="exactly 50"):
        scanner.parse_constituents_csv(constituent_csv(symbols_50()[:-1]))
    with pytest.raises(ValueError, match="unique"):
        scanner.parse_constituents_csv(constituent_csv(symbols_50()[:-1] + ["SYM00"]))
    with pytest.raises(ValueError, match="blank"):
        scanner.parse_constituents_csv(constituent_csv(symbols_50()[:-1] + [""]))


def test_remote_refresh_replaces_cache_and_reports_source(tmp_path):
    class Response:
        text = constituent_csv(symbols_50())
        def raise_for_status(self):
            return None
    class Client:
        @staticmethod
        def get(url, headers, timeout):
            return Response()

    cache = tmp_path / "nifty50.csv"
    symbols, source = scanner.load_nifty50_constituents(cache, Client)
    assert symbols == symbols_50()
    assert source == "NSE refresh"
    assert scanner.parse_constituents_csv(cache.read_text(encoding="utf-8")) == symbols_50()


def test_failed_refresh_uses_valid_cache(tmp_path):
    class Client:
        @staticmethod
        def get(url, headers, timeout):
            raise requests.RequestException("offline")

    cache = tmp_path / "nifty50.csv"
    cache.write_text(constituent_csv(symbols_50()), encoding="utf-8")
    assert scanner.load_nifty50_constituents(cache, Client) == (symbols_50(), "cached CSV")


def test_invalid_remote_response_preserves_and_uses_cache(tmp_path):
    class Response:
        text = constituent_csv(symbols_50()[:-1])
        def raise_for_status(self):
            return None
    class Client:
        @staticmethod
        def get(url, headers, timeout):
            return Response()

    cache = tmp_path / "nifty50.csv"
    valid_text = constituent_csv(symbols_50())
    cache.write_text(valid_text, encoding="utf-8")
    assert scanner.load_nifty50_constituents(cache, Client) == (symbols_50(), "cached CSV")
    assert cache.read_text(encoding="utf-8") == valid_text


def test_no_valid_remote_or_cache_fails_clearly(tmp_path):
    class Client:
        @staticmethod
        def get(url, headers, timeout):
            raise requests.RequestException("offline")

    with pytest.raises(RuntimeError, match="no valid NIFTY 50"):
        scanner.load_nifty50_constituents(tmp_path / "missing.csv", Client)
```

- [ ] **Step 2: Run tests and confirm the expected import failure**

Run: `python -m pytest tests/test_nifty50_zlema25_scanner.py -v --basetemp=.pytest_tmp/nifty50_zl_task1`

Expected: collection fails with `ModuleNotFoundError: No module named 'nifty50_zlema25_scanner'`.

- [ ] **Step 3: Implement the validated atomic cache**

Create the scanner module header, constants, imports, and these functions. Use `csv.DictReader`, uppercase trimmed symbols, exact count validation, `Path.with_suffix(".tmp")`, and `os.replace()` only after parsing succeeds.

```python
NSE_CONSTITUENTS_URL = "https://nsearchives.nseindia.com/content/indices/ind_nifty50list.csv"
CACHE_FILE = Path(__file__).resolve().parent / "data" / "nifty50_constituents.csv"
HTTP_HEADERS = {"User-Agent": "Mozilla/5.0"}


def parse_constituents_csv(text: str) -> list[str]:
    rows = list(csv.DictReader(StringIO(text.lstrip("\ufeff"))))
    if not rows or "Symbol" not in rows[0]:
        raise ValueError("constituent CSV is missing Symbol column")
    symbols = [str(row.get("Symbol", "")).strip().upper() for row in rows]
    if any(not symbol for symbol in symbols):
        raise ValueError("constituent CSV contains a blank symbol")
    if len(symbols) != 50:
        raise ValueError(f"constituent CSV must contain exactly 50 symbols, got {len(symbols)}")
    if len(set(symbols)) != 50:
        raise ValueError("constituent CSV symbols must be unique")
    return sorted(symbols)


def load_nifty50_constituents(
    cache_path: Path = CACHE_FILE,
    http_client=requests,
) -> tuple[list[str], str]:
    try:
        response = http_client.get(
            NSE_CONSTITUENTS_URL,
            headers=HTTP_HEADERS,
            timeout=15,
        )
        response.raise_for_status()
        symbols = parse_constituents_csv(response.text)
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = cache_path.with_suffix(cache_path.suffix + ".tmp")
        tmp_path.write_text(response.text, encoding="utf-8", newline="")
        os.replace(tmp_path, cache_path)
        return symbols, "NSE refresh"
    except (requests.RequestException, OSError, ValueError):
        if not cache_path.exists():
            raise RuntimeError("no valid NIFTY 50 constituent source is available")
        try:
            return parse_constituents_csv(cache_path.read_text(encoding="utf-8")), "cached CSV"
        except (OSError, ValueError) as exc:
            raise RuntimeError("no valid NIFTY 50 constituent source is available") from exc
```

Populate `data/nifty50_constituents.csv` through the implemented validated refresh path; do not hand-maintain a second symbol list in Python.

Run:

```powershell
python -c "from nifty50_zlema25_scanner import load_nifty50_constituents; symbols, source = load_nifty50_constituents(); print(len(symbols), source)"
```

Expected with network available: `50 NSE refresh` and a newly written cache that `parse_constituents_csv()` accepts. If network is unavailable and no cache exists yet, fetch the official URL with approved network access and rerun this exact command; do not substitute an unverified third-party list.

- [ ] **Step 4: Run the constituent tests**

Run: `python -m pytest tests/test_nifty50_zlema25_scanner.py -v --basetemp=.pytest_tmp/nifty50_zl_task1`

Expected: 5 tests pass.

- [ ] **Step 5: Commit the constituent layer**

```powershell
git add -- nifty50_zlema25_scanner.py tests/test_nifty50_zlema25_scanner.py data/nifty50_constituents.csv
git commit --no-verify -m "feat: add cached NIFTY50 universe"
```

### Task 2: Direction, age, and symbol analysis

**Files:**
- Modify: `nifty50_zlema25_scanner.py`
- Modify: `tests/test_nifty50_zlema25_scanner.py`

**Interfaces:**
- Consumes: `ema25_zl_scanner.zlema(close, 25)`, `ema25_zl_scanner.bb_kc_squeeze(df)`, `ohlc_db.load_ohlc(symbol)`, `ohlc_db.liq_tag(df)`, `ohlc_db.cmf_tag(df)`, and `ohlc_db.deliv_tag(symbol)`.
- Produces: immutable `TrendStats(direction: Literal["up", "down", "flat"], age: int, change_pct: float, start_position: int | None)`; `trend_stats(zl25: pd.Series, closes: pd.Series) -> TrendStats`; `analyse_symbol(symbol: str) -> dict[str, object]`.

- [ ] **Step 1: Write failing trend-stat tests**

Use explicit ZLEMA sequences so each slope transition is visible. Assert parity separately using real close data.

```python
import pandas as pd
from pandas.testing import assert_series_equal
from ema25_zl_scanner import zlema as broad_zlema


@pytest.mark.parametrize(
    ("zl", "expected_direction", "expected_age", "expected_start"),
    [
        ([10, 9, 10], "up", 1, 2),
        ([10, 9, 10, 11, 12], "up", 3, 2),
        ([10, 11, 10], "down", 1, 2),
        ([10, 11, 10, 9, 8], "down", 3, 2),
        ([10, 11, 11], "flat", 0, None),
    ],
)
def test_trend_stats_direction_age_and_start(zl, expected_direction, expected_age, expected_start):
    series = pd.Series(zl, dtype=float)
    closes = pd.Series([100 + i * 10 for i in range(len(zl))], dtype=float)
    result = scanner.trend_stats(series, closes)
    assert (result.direction, result.age, result.start_position) == (
        expected_direction,
        expected_age,
        expected_start,
    )


def test_trend_change_uses_close_before_start():
    result = scanner.trend_stats(
        pd.Series([10.0, 9.0, 10.0, 11.0]),
        pd.Series([100.0, 110.0, 121.0, 132.0]),
    )
    assert result.change_pct == 20.0


def test_zlema_is_identical_to_broad_scanner():
    close = pd.Series(range(1, 81), dtype=float)
    assert_series_equal(scanner.zlema(close, 25), broad_zlema(close, 25))
```

Add the following symbol-analysis tests. The monotonic synthetic close makes every available ZLEMA slope positive after the first row, so the expected age is deterministic.

```python
def synthetic_ohlc(rows: int = 65) -> pd.DataFrame:
    close = pd.Series([100.0 + i for i in range(rows)])
    return pd.DataFrame({
        "date": pd.date_range("2026-01-01", periods=rows, freq="B"),
        "open": close - 0.25,
        "high": close + 1.0,
        "low": close - 1.0,
        "close": close,
        "volume": 1_000_000,
    })


def test_analyse_symbol_returns_direction_age_prices_and_tags(monkeypatch):
    monkeypatch.setattr(scanner, "load_ohlc", lambda symbol: synthetic_ohlc())
    monkeypatch.setattr(scanner, "bb_kc_squeeze", lambda frame: True)
    monkeypatch.setattr(scanner, "liq_tag", lambda frame: "LIQ")
    monkeypatch.setattr(scanner, "cmf_tag", lambda frame: "CMF")
    monkeypatch.setattr(scanner, "deliv_tag", lambda symbol: "DEL")
    result = scanner.analyse_symbol("TEST")
    assert result["status"] == "analysed"
    assert result["direction"] == "up" and result["zl_age"] == 64
    assert result["close"] == 164.0
    assert (result["liq_tag"], result["cmf_tag"], result["deliv_tag"]) == ("LIQ", "CMF", "DEL")


def test_analyse_symbol_reports_short_history(monkeypatch):
    monkeypatch.setattr(scanner, "load_ohlc", lambda symbol: synthetic_ohlc(59))
    assert scanner.analyse_symbol("SHORT") == {
        "symbol": "SHORT", "status": "skipped", "reason": "fewer than 60 OHLC rows"
    }


def test_analyse_symbol_raises_contextual_error_for_bad_schema(monkeypatch):
    monkeypatch.setattr(scanner, "load_ohlc", lambda symbol: synthetic_ohlc().drop(columns="close"))
    with pytest.raises(RuntimeError, match="BROKEN: analysis failed"):
        scanner.analyse_symbol("BROKEN")
```

- [ ] **Step 2: Run the new tests and confirm missing interface failures**

Run: `python -m pytest tests/test_nifty50_zlema25_scanner.py -v --basetemp=.pytest_tmp/nifty50_zl_task2`

Expected: constituent tests pass; trend tests fail because `TrendStats`, `trend_stats`, and `analyse_symbol` are absent.

- [ ] **Step 3: Implement the pure trend contract**

```python
@dataclass(frozen=True)
class TrendStats:
    direction: Literal["up", "down", "flat"]
    age: int
    change_pct: float
    start_position: int | None


def trend_stats(zl25: pd.Series, closes: pd.Series) -> TrendStats:
    if len(zl25) != len(closes) or len(zl25) < 2:
        raise ValueError("ZLEMA and close series must have equal length >= 2")
    slopes = zl25.astype(float).diff()
    last_slope = float(slopes.iloc[-1])
    if last_slope == 0:
        return TrendStats("flat", 0, 0.0, None)
    direction = "up" if last_slope > 0 else "down"
    age = 0
    for slope in reversed(slopes.iloc[1:].tolist()):
        if (direction == "up" and slope > 0) or (direction == "down" and slope < 0):
            age += 1
        else:
            break
    start_position = len(zl25) - age
    base_position = start_position - 1
    change_pct = round((float(closes.iloc[-1]) / float(closes.iloc[base_position]) - 1) * 100, 2)
    return TrendStats(direction, age, change_pct, start_position)
```

Import `zlema`, `bb_kc_squeeze`, and `get_circuit_limits` from `ema25_zl_scanner.py`; import `load_ohlc`, `liq_tag`, `cmf_tag`, and `deliv_tag` from `ohlc_db.py`. Do not import or call `_rs_gate`, `get_watchlist`, or `float_gate`.

- [ ] **Step 4: Implement deterministic per-symbol analysis**

`analyse_symbol()` returns `{symbol, status, reason}` only for missing/short history and a finding dictionary for analysed data. Require 60 rows and sort by date before calculation. Unexpected schema/calculation failures raise a contextual `RuntimeError`, allowing `main()` to exit non-zero instead of publishing a partial report.

```python
def analyse_symbol(symbol: str) -> dict[str, object]:
    raw = load_ohlc(symbol)
    if raw is None or len(raw) < 60:
        return {"symbol": symbol, "status": "skipped", "reason": "fewer than 60 OHLC rows"}
    try:
        df = raw.sort_values("date").reset_index(drop=True)
        close = df["close"].astype(float)
        stats = trend_stats(zlema(close, 25), close)
        previous_close = float(close.iloc[-2])
        latest_close = float(close.iloc[-1])
        return {
            "symbol": symbol,
            "status": "analysed",
            "direction": stats.direction,
            "zl_age": stats.age,
            "zl_change_pct": stats.change_pct,
            "close": latest_close,
            "day_change_pct": round((latest_close / previous_close - 1) * 100, 2),
            "squeeze": bb_kc_squeeze(df),
            "liq_tag": liq_tag(df),
            "cmf_tag": cmf_tag(df),
            "deliv_tag": deliv_tag(symbol),
        }
    except Exception as exc:
        raise RuntimeError(f"{symbol}: analysis failed: {exc}") from exc
```

- [ ] **Step 5: Run tests and commit the calculation layer**

Run: `python -m pytest tests/test_nifty50_zlema25_scanner.py -v --basetemp=.pytest_tmp/nifty50_zl_task2`

Expected: all Task 1 and Task 2 tests pass.

```powershell
git add -- nifty50_zlema25_scanner.py tests/test_nifty50_zlema25_scanner.py
git commit --no-verify -m "feat: calculate NIFTY50 ZLEMA trend age"
```

### Task 3: Two-table report and symmetric age buckets

**Files:**
- Modify: `nifty50_zlema25_scanner.py`
- Modify: `tests/test_nifty50_zlema25_scanner.py`

**Interfaces:**
- Consumes: analysed finding dictionaries from `analyse_symbol()` and circuit mapping from `get_circuit_limits()`.
- Produces: `age_bucket(age: int) -> str`; `sort_findings(findings: list[dict[str, object]], direction: str) -> list[dict[str, object]]`; `build_markdown(results, circuits, universe_source, generated_at) -> str`; `write_report_atomic(text: str, output_path: Path) -> None`.

- [ ] **Step 1: Write failing bucket, sorting, and report tests**

```python
@pytest.mark.parametrize(
    ("age", "bucket"),
    [(1, "1 DAY"), (2, "2 DAYS"), (3, "3 DAYS"), (4, "4-5 DAYS"),
     (5, "4-5 DAYS"), (6, "6-10 DAYS"), (10, "6-10 DAYS"),
     (11, "11-15 DAYS"), (15, "11-15 DAYS"), (16, "15 DAYS+"), (80, "15 DAYS+")],
)
def test_age_bucket_boundaries(age, bucket):
    assert scanner.age_bucket(age) == bucket


def finding(symbol: str, direction: str, age: int) -> dict[str, object]:
    return {
        "symbol": symbol, "status": "analysed", "direction": direction,
        "zl_age": age, "zl_change_pct": 1.25, "day_change_pct": 0.5,
        "close": 100.0, "squeeze": False, "liq_tag": "", "cmf_tag": "", "deliv_tag": "",
    }


def test_tables_sort_by_age_then_symbol():
    rows = [finding("ZZZ", "up", 2), finding("BBB", "up", 1), finding("AAA", "up", 1)]
    assert [row["symbol"] for row in scanner.sort_findings(rows, "up")] == ["AAA", "BBB", "ZZZ"]


def test_report_has_two_tables_and_symmetric_watchlists():
    results = [finding("UP1", "up", 1), finding("UP4", "up", 4),
               finding("DN1", "down", 1), finding("DN4", "down", 4),
               {"symbol": "FLAT", "status": "analysed", "direction": "flat", "zl_age": 0},
               {"symbol": "SKIP", "status": "skipped", "reason": "short"}]
    report = scanner.build_markdown(results, {}, "cached CSV", "2026-07-17 16:30 IST")
    assert "### ZLEMA25 Uptrend Start and Age" in report
    assert "### ZLEMA25 Downtrend Start and Age" in report
    assert "###UP 1 DAY,NSE:UP1" in report
    assert "###DOWN 1 DAY,NSE:DN1" in report
    assert report.index("NSE:UP1") < report.index("NSE:UP4")
    assert "Analysed: 5" in report and "Skipped: 1" in report and "Flat: 1" in report
    assert "SEBI registered" in report
```

Add an atomic-write test:

```python
def test_write_report_atomic_replaces_target_without_temp_residue(tmp_path):
    output = tmp_path / "report.md"
    output.write_text("old", encoding="utf-8")
    scanner.write_report_atomic("new\n", output)
    assert output.read_text(encoding="utf-8") == "new\n"
    assert not (tmp_path / "report.md.tmp").exists()
```

- [ ] **Step 2: Run the report tests and confirm missing interface failures**

Run: `python -m pytest tests/test_nifty50_zlema25_scanner.py -v --basetemp=.pytest_tmp/nifty50_zl_task3`

Expected: calculation tests pass; report tests fail because the report interfaces are absent.

- [ ] **Step 3: Implement buckets and deterministic sorting**

```python
AGE_BUCKETS = (
    ("1 DAY", 1, 1), ("2 DAYS", 2, 2), ("3 DAYS", 3, 3),
    ("4-5 DAYS", 4, 5), ("6-10 DAYS", 6, 10),
    ("11-15 DAYS", 11, 15), ("15 DAYS+", 16, sys.maxsize),
)


def age_bucket(age: int) -> str:
    for label, low, high in AGE_BUCKETS:
        if low <= age <= high:
            return label
    raise ValueError(f"trend age must be >= 1, got {age}")


def sort_findings(findings: list[dict[str, object]], direction: str) -> list[dict[str, object]]:
    return sorted(
        (row for row in findings if row.get("status") == "analysed" and row.get("direction") == direction),
        key=lambda row: (int(row["zl_age"]), str(row["symbol"])),
    )
```

- [ ] **Step 4: Implement the Markdown renderer and atomic writer**

Build table rows with the exact columns `Symbol | ZL Age | ZL Chg% | Label | Day Chg | Close | Squeeze | Circuit`. Load labels from `tools/stock_labels.json`; show local liquidity/CMF/delivery tags as informational subtext only. Prefix bucket section names with `UP ` or `DOWN ` so a combined TradingView import has unique section names. Include separate per-direction, per-bucket copy blocks and omit empty buckets.

Wrap the assembled body with `SEBI_MD_HEADER` and `SEBI_MD_FOOTER`. Implement atomic output as:

```python
def write_report_atomic(text: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = output_path.with_suffix(output_path.suffix + ".tmp")
    tmp_path.write_text(text, encoding="utf-8", newline="\n")
    os.replace(tmp_path, output_path)
```

- [ ] **Step 5: Run tests and commit the report layer**

Run: `python -m pytest tests/test_nifty50_zlema25_scanner.py -v --basetemp=.pytest_tmp/nifty50_zl_task3`

Expected: all scanner tests pass.

```powershell
git add -- nifty50_zlema25_scanner.py tests/test_nifty50_zlema25_scanner.py
git commit --no-verify -m "feat: report NIFTY50 ZLEMA trend buckets"
```

### Task 4: CLI, production runner, and orchestration

**Files:**
- Modify: `nifty50_zlema25_scanner.py`
- Modify: `tests/test_nifty50_zlema25_scanner.py`
- Create: `run_nifty50_zlema25_scanner.ps1`
- Modify: `run_all_scanners.ps1`

**Interfaces:**
- Consumes: all Task 1-3 interfaces.
- Produces: `run_scan() -> tuple[list[dict[str, object]], str]`; `main() -> int`; output `nifty50_zlema25_scans/nifty50_zlema25_scans.md`; orchestrator job name `NIFTY50_ZLEMA25`.

- [ ] **Step 1: Write failing end-to-end CLI contract tests**

Monkeypatch `load_nifty50_constituents` to return two symbols, `analyse_symbol` to return one up and one down finding, `get_circuit_limits` to return `{}`, and `OUTPUT_FILE` to a temporary path. Assert `main()` returns `0`, writes both tables, and prints analysed/up/down counts. Add a failure test where constituent loading raises `RuntimeError`, asserting `main()` returns `1` and no report is written.

Add source-contract assertions:

```python
def test_runner_and_orchestrator_contracts():
    root = Path(__file__).resolve().parents[1]
    runner = (root / "run_nifty50_zlema25_scanner.ps1").read_text(encoding="utf-8")
    orchestrator = (root / "run_all_scanners.ps1").read_text(encoding="utf-8")
    assert "nifty50_zlema25_scanner.py" in runner
    assert "nifty50_zlema25_scans/" in runner
    assert "commit --no-verify" in runner
    assert 'Run-Scanner "NIFTY50_ZLEMA25"' in orchestrator
```

- [ ] **Step 2: Run tests and confirm CLI/runner failures**

Run: `python -m pytest tests/test_nifty50_zlema25_scanner.py -v --basetemp=.pytest_tmp/nifty50_zl_task4`

Expected: core/report tests pass; CLI and runner-contract tests fail.

- [ ] **Step 3: Implement the CLI**

Define `OUTPUT_FILE = REPO_DIR / "nifty50_zlema25_scans" / "nifty50_zlema25_scans.md"`. `run_scan()` obtains the universe, analyses symbols in alphabetical order, and returns results plus source. `main()` prints each skip reason, obtains circuit limits once, renders/writes the report, prints final counts/path, and returns `1` with a concise error on fatal universe/report failures. End with `raise SystemExit(main())` under the normal module guard.

```python
def run_scan() -> tuple[list[dict[str, object]], str]:
    symbols, source = load_nifty50_constituents()
    return [analyse_symbol(symbol) for symbol in symbols], source


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Add the production PowerShell runner**

Mirror `run_ema25_zl_scanner.ps1`: log to `logs/nifty50_zlema25_scanner_$date.log`, run `C:\Python313\python.exe`, preserve `$LASTEXITCODE`, and stop before Git publication if the scanner fails. On success stage only `nifty50_zlema25_scans/` and `data/nifty50_constituents.csv`, then use `git commit --no-verify -m "nifty50-zlema25 scan $date"` and `git push`. This intentionally permits the validated cache to track index rebalances while avoiding unrelated files.

- [ ] **Step 5: Register the job in the orchestrator**

Immediately after the existing EMA25 job add:

```powershell
Run-Scanner "NIFTY50_ZLEMA25"      "$ROOT\run_nifty50_zlema25_scanner.ps1"
```

- [ ] **Step 6: Run tests and commit production wiring**

Run: `python -m pytest tests/test_nifty50_zlema25_scanner.py -v --basetemp=.pytest_tmp/nifty50_zl_task4`

Expected: all tests pass.

```powershell
git add -- nifty50_zlema25_scanner.py tests/test_nifty50_zlema25_scanner.py run_nifty50_zlema25_scanner.ps1 run_all_scanners.ps1
git commit --no-verify -m "feat: schedule NIFTY50 ZLEMA scanner"
```

### Task 5: Documentation, live local run, and completion evidence

**Files:**
- Modify: `CLAUDE.md`
- Modify: `HANDOFF.md`
- Generate: `nifty50_zlema25_scans/nifty50_zlema25_scans.md`

**Interfaces:**
- Consumes: completed scanner and runner.
- Produces: documented operating contract and verified current report.

- [ ] **Step 1: Document the scanner workflow**

In `CLAUDE.md`, add the manual command `python nifty50_zlema25_scanner.py`, runner `run_nifty50_zlema25_scanner.ps1`, official-refresh/cached-fallback behavior, strict daily ZLEMA25 slope semantics, two table names, age buckets, and report path. Add the runner to the daily workflow list near `run_ema25_zl_scanner.ps1`.

- [ ] **Step 2: Run focused and broader regression tests**

Run:

```powershell
python -m pytest tests/test_nifty50_zlema25_scanner.py -v --basetemp=.pytest_tmp/nifty50_zl_final
python -m pytest tests/test_backtest_daily_zlema25_weekly_rs.py -v --basetemp=.pytest_tmp/nifty50_zl_regression
```

Expected: both commands pass with zero failures.

- [ ] **Step 3: Run the scanner against the local OHLC database**

Run: `python nifty50_zlema25_scanner.py`

Expected: exit code `0`; exactly 50 constituents requested; analysed + skipped equals 50; analysed equals up + down + flat; output exists at `nifty50_zlema25_scans/nifty50_zlema25_scans.md`; both trend headings and `SEBI registered` are present. If network is unavailable, console/report must identify `cached CSV` as the universe source.

- [ ] **Step 4: Inspect the generated report and repository diff**

Run:

```powershell
rg -n "Universe source|Requested:|Analysed:|Skipped:|Flat:|ZLEMA25 Uptrend Start and Age|ZLEMA25 Downtrend Start and Age|###UP |###DOWN |SEBI registered" nifty50_zlema25_scans/nifty50_zlema25_scans.md
git diff --check
git status --short
```

Expected: required report sections are found; `git diff --check` has no output; status contains only task files plus any clearly identified pre-existing user/agent changes.

- [ ] **Step 5: Update the shared handoff**

At the top of `HANDOFF.md`, add a dated entry listing the scanner, cache, runner, orchestration, tests, generated report, actual requested/analysed/skipped/up/down/flat counts, universe source used by the verified run, focused test counts, and rerun command. Preserve all prior handoff entries.

- [ ] **Step 6: Commit documentation and verified output**

```powershell
git add -- CLAUDE.md HANDOFF.md nifty50_zlema25_scans/nifty50_zlema25_scans.md
git commit --no-verify -m "docs: hand off NIFTY50 ZLEMA scanner"
```

- [ ] **Step 7: Final verification from committed state**

Run:

```powershell
python -m pytest tests/test_nifty50_zlema25_scanner.py -v --basetemp=.pytest_tmp/nifty50_zl_committed
git status --short
git log -5 --oneline
```

Expected: focused tests pass; task files are committed; any remaining status entries are explicitly confirmed as unrelated pre-existing work; recent log shows the task's small cohesive commits.

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
