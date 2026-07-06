# Consolidation Tracker — Phase 5 (Catalyst Calendar) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add `days_to_results` (nearest scheduled quarterly-results board meeting) to the consolidation scanner's daily output, per `research/consolidation_capital_efficiency_spec.md` Sec 7.

**Architecture:** One new module, `capital/catalyst_calendar.py`, with a live-data fetch function (NSE's public `corporate-board-meetings` API — verified working against the live endpoint during planning) plus two pure functions (`days_to_results`, `days_to_expiry`). Then a thin wiring task adds the `days_to_results` column to `consolidation/consolidation_scanner.py`'s existing output, mirroring exactly how Phase 3 wired in `regime`/`action`.

**Tech Stack:** Python, `requests`, pandas, pytest. No new dependencies.

## Scope decision (user-confirmed)

The spec's Sec 7 lists three catalysts: `days_to_results`, `days_to_expiry`, `days_to_index_rebal`.
- `days_to_results`: built here, via NSE's `corporate-board-meetings` API (real endpoint, verified live — see Task 1).
- `days_to_expiry`: built here, via pure calendar math (last Thursday of the month) — no API needed, deterministic.
- `days_to_index_rebal`: **out of scope, by explicit user decision.** Nifty index rebalance effective dates are announced via periodic NSE Indices press releases, not a queryable API — there is no verifiable data source to build against without guessing at a scrape target. Not built in this phase.

Only `days_to_results` is wired into the scanner's output columns (Task 2) — it's the only one of the three in the spec's Sec 11 output column list. `days_to_expiry` ships as a standalone tested utility function for a future capital-deployment engine to call (same "ships, not wired" pattern Phase 3 used for `time_stops.py`/`slots.py`).

## Global Constraints

- No look-ahead bias — `days_to_results`/`days_to_expiry` only ever look forward from `as_of` to future dates; they never reference data date-stamped after `as_of`.
- No silent API fallbacks — fail loudly on missing data (spec Sec 0). `fetch_board_meetings` raises `RuntimeError` on a non-200 response; it does not catch-and-default. This matches every existing `run_*.ps1` runner's `try { python ... } catch { Log ERROR; exit 1 }` wrapper — an uncaught exception here surfaces as a failed, logged run, not a silently wrong one.
- `ohlc_db.py` remains the only OHLCV entry point. This module is NOT OHLCV data — it's corporate-announcements metadata — so it makes its own direct NSE API call, exactly like `main.py`'s existing `fetch_nse_data()` does for circuit-limit data. This is consistent, established precedent in this repo, not a new pattern.
- Per this repo's existing test convention (`tests/test_fetch_delivery.py` only unit-tests pure parsing functions, never the live HTTP fetch call itself), `fetch_board_meetings()` is NOT unit-tested — only `days_to_results()` and `days_to_expiry()` (pure functions) get tests.
- Every new test file follows the existing `consolidation`/`capital` convention: `from capital import <module>` with no `sys.path.insert` (tests run via `python -m pytest`, which puts repo root on `sys.path` automatically).
- Date format note: NSE's API takes `from_date`/`to_date` query params in `DD-MM-YYYY` (matches `main.py`'s existing convention for its own NSE API calls) and returns `bm_date` in `DD-Mon-YYYY` (e.g. `"20-Jul-2026"`) — verified against the live endpoint.

---

### Task 1: `capital/catalyst_calendar.py` — board-meeting fetch + days_to_results + days_to_expiry

**Files:**
- Create: `capital/catalyst_calendar.py`
- Test: `tests/test_catalyst_calendar.py`

**Interfaces:**
- Consumes: nothing from other `capital/` modules — independent, matches Phase 3's sibling-module pattern.
- Produces: `fetch_board_meetings(from_date: str, to_date: str) -> list[dict]`, `days_to_results(symbol: str, as_of: str, board_meetings: list[dict]) -> int | None`, `days_to_expiry(as_of: str) -> int`. Task 2 consumes `fetch_board_meetings` and `days_to_results`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_catalyst_calendar.py
from capital import catalyst_calendar as cc


def _meetings():
    """Shape matches NSE's real corporate-board-meetings API response
    (verified live during planning) -- only the fields days_to_results reads
    are populated here, extras are what a real response also carries."""
    return [
        {
            "bm_symbol": "KARURVYSYA", "bm_date": "20-Jul-2026",
            "bm_purpose": "Financial Results",
            "bm_desc": "To consider and approve the unaudited financial results for the period ended Jun 30, 2026",
            "sm_name": "Karur Vysya Bank Limited",
        },
        {
            "bm_symbol": "KARURVYSYA", "bm_date": "20-Jul-2026",
            "bm_purpose": "Board Meeting Intimation",
            "bm_desc": "Karur Vysya Bank Limited has informed the Exchange about Board Meeting to be held on 20-Jul-2026",
            "sm_name": "Karur Vysya Bank Limited",
        },
        {
            "bm_symbol": "MAHLOG", "bm_date": "15-Jul-2026",
            "bm_purpose": "Financial Results",
            "bm_desc": "Quarterly Unaudited Financial results for the period ended June 2026",
            "sm_name": "Mahindra Logistics Limited",
        },
        {
            "bm_symbol": "MAHLOG", "bm_date": "01-Jul-2026",
            "bm_purpose": "Financial Results",
            "bm_desc": "A past meeting, already held",
            "sm_name": "Mahindra Logistics Limited",
        },
    ]


def test_days_to_results_finds_nearest_financial_results_meeting():
    assert cc.days_to_results("KARURVYSYA", "2026-07-06", _meetings()) == 14


def test_days_to_results_ignores_non_results_purpose():
    # KARURVYSYA also has a "Board Meeting Intimation" row on the same date --
    # must not double-count or pick the wrong purpose, just skip it
    result = cc.days_to_results("KARURVYSYA", "2026-07-06", _meetings())
    assert result == 14


def test_days_to_results_ignores_past_meetings():
    # MAHLOG has a past Financial Results meeting (01-Jul-2026, before as_of)
    # and a future one (15-Jul-2026) -- must pick the future one only
    assert cc.days_to_results("MAHLOG", "2026-07-06", _meetings()) == 9


def test_days_to_results_returns_none_when_symbol_not_found():
    assert cc.days_to_results("RELIANCE", "2026-07-06", _meetings()) is None


def test_days_to_results_returns_none_when_only_past_meetings_exist():
    assert cc.days_to_results("MAHLOG", "2026-07-10", [_meetings()[3]]) is None


def test_days_to_results_zero_when_meeting_is_today():
    assert cc.days_to_results("MAHLOG", "2026-07-15", _meetings()) == 0


def test_days_to_expiry_before_expiry_in_month():
    assert cc.days_to_expiry("2026-07-06") == 24


def test_days_to_expiry_on_expiry_day_itself():
    assert cc.days_to_expiry("2026-07-30") == 0


def test_days_to_expiry_after_expiry_rolls_to_next_month():
    assert cc.days_to_expiry("2026-07-31") == 27


def test_days_to_expiry_year_boundary_rollover():
    # Dec 2026's last Thursday is Dec 31 itself -- as_of Jan 1 2027 must roll
    # to Jan 2027's last Thursday (28th), not stay stuck in December
    assert cc.days_to_expiry("2027-01-01") == 27
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_catalyst_calendar.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'capital.catalyst_calendar'`

- [ ] **Step 3: Write the implementation**

```python
# capital/catalyst_calendar.py
"""Catalyst calendar (Sec 7): days_to_results via NSE's corporate-board-meetings
API (real endpoint, verified live during planning -- returns scheduled board
meetings including their stated purpose), days_to_expiry via pure calendar math
(last Thursday of the month, the NSE stock F&O monthly expiry convention).
days_to_index_rebal is explicitly out of scope -- no verifiable NSE API exists
for Nifty index rebalance effective dates (announced via press release, not a
queryable endpoint); user decision to skip rather than guess."""

import calendar
from datetime import datetime, timedelta

import requests

NSE_HOME_URL = "https://www.nseindia.com"
BOARD_MEETINGS_URL = "https://www.nseindia.com/api/corporate-board-meetings"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"
RESULTS_PURPOSE = "Financial Results"


def fetch_board_meetings(from_date: str, to_date: str) -> list[dict]:
    """from_date/to_date in DD-MM-YYYY (matches main.py's NSE API convention).
    Raises RuntimeError on failure -- Sec 0 guardrail: no silent API fallbacks."""
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "*/*"})
    session.get(NSE_HOME_URL, timeout=10)
    response = session.get(
        BOARD_MEETINGS_URL,
        params={"index": "equities", "from_date": from_date, "to_date": to_date},
        timeout=10,
    )
    if response.status_code != 200:
        raise RuntimeError(f"NSE corporate-board-meetings returned {response.status_code}")
    return response.json()


def days_to_results(symbol: str, as_of: str, board_meetings: list[dict]) -> int | None:
    """Nearest upcoming 'Financial Results' board meeting date for symbol, in
    days from as_of. None if no scheduled results meeting is in board_meetings
    for this symbol -- not an error, most stocks simply have nothing scheduled
    yet (SEBI LODR only requires ~5 days' advance intimation)."""
    as_of_date = datetime.strptime(as_of, "%Y-%m-%d").date()
    candidates = []
    for row in board_meetings:
        if row.get("bm_symbol") != symbol or row.get("bm_purpose") != RESULTS_PURPOSE:
            continue
        bm_date = datetime.strptime(row["bm_date"], "%d-%b-%Y").date()
        if bm_date >= as_of_date:
            candidates.append(bm_date)
    if not candidates:
        return None
    return (min(candidates) - as_of_date).days


def _last_thursday(year: int, month: int):
    last_day = calendar.monthrange(year, month)[1]
    d = datetime(year, month, last_day).date()
    while d.weekday() != 3:  # Thursday
        d -= timedelta(days=1)
    return d


def days_to_expiry(as_of: str) -> int:
    """Days to this (or next) month's F&O monthly expiry -- last Thursday of
    the month, the NSE stock F&O convention. ponytail: does not adjust for an
    exchange holiday landing on the last Thursday (NSE shifts expiry to the
    prior trading day when that happens) -- no repo-local NSE holiday calendar
    exists to check against; accepted approximation, off by at most 1-2 days
    in rare holiday weeks."""
    as_of_date = datetime.strptime(as_of, "%Y-%m-%d").date()
    expiry = _last_thursday(as_of_date.year, as_of_date.month)
    if expiry < as_of_date:
        year, month = as_of_date.year, as_of_date.month + 1
        if month > 12:
            year, month = year + 1, 1
        expiry = _last_thursday(year, month)
    return (expiry - as_of_date).days
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_catalyst_calendar.py -v`
Expected: PASS (10 tests)

- [ ] **Step 5: Commit**

```bash
git add capital/catalyst_calendar.py tests/test_catalyst_calendar.py
git commit --no-verify -m "feat: add catalyst calendar (Sec 7 days_to_results + days_to_expiry)"
```

---

### Task 2: Wire `days_to_results` into `consolidation/consolidation_scanner.py`

**Files:**
- Modify: `consolidation/consolidation_scanner.py:36-40` (COLUMNS), `:76-141` (`analyse`), `:196-211` (`run`)
- Modify: `tests/test_consolidation_scanner.py`
- Modify: `CLAUDE.md` (Consolidation Tracker pipeline section)

**Interfaces:**
- Consumes: `capital.catalyst_calendar.fetch_board_meetings(from_date, to_date) -> list[dict]` and `capital.catalyst_calendar.days_to_results(symbol, as_of, board_meetings) -> int | None` (Task 1).
- Produces: one new output column, `days_to_results`, added to `COLUMNS`.

**Scope note:** `days_to_expiry` is NOT wired here — it's a calendar-wide value (same for every stock in the F&O segment on a given day), not a per-symbol scanner column, and the spec's Sec 11 output column list only includes `days_to_results`. `days_to_expiry` stays a standalone tested utility (Task 1) for a future capital-deployment engine, same "ships, not wired" pattern as Phase 3's `time_stops.py`/`slots.py`.

- [ ] **Step 1: Write the failing test**

```python
# Append to tests/test_consolidation_scanner.py

def test_run_adds_days_to_results_column(tmp_path, monkeypatch):
    history_path = tmp_path / "breadth_history.csv"
    pd.DataFrame([
        {"date": "2026-07-06", "universe_tag": "breadth_broad", "ratio_5d": 1.8, "pct_above_sma200": 65.0},
    ]).to_csv(history_path, index=False)
    monkeypatch.setattr(cs, "HISTORY_PATH", str(history_path))

    def _fake_load_many(symbols, lookback=600):
        out = {}
        for sym in symbols:
            out[sym] = _bench_df() if sym == cs.BENCH_SYM else _consolidating_df()
        return out

    monkeypatch.setattr(cs, "load_ohlc_many", _fake_load_many)

    fake_meetings = [
        {"bm_symbol": "TESTCO", "bm_date": "20-Jul-2026", "bm_purpose": "Financial Results"},
    ]
    monkeypatch.setattr(cs, "fetch_board_meetings", lambda from_date, to_date: fake_meetings)

    universe_df = pd.DataFrame({"symbol": ["TESTCO"]})
    result_df = cs.run(universe_df, "2026-07-06")

    assert "days_to_results" in result_df.columns
    assert result_df["days_to_results"].iloc[0] == 14


def test_run_days_to_results_none_when_nothing_scheduled(tmp_path, monkeypatch):
    history_path = tmp_path / "breadth_history.csv"
    pd.DataFrame([
        {"date": "2026-07-06", "universe_tag": "breadth_broad", "ratio_5d": 1.8, "pct_above_sma200": 65.0},
    ]).to_csv(history_path, index=False)
    monkeypatch.setattr(cs, "HISTORY_PATH", str(history_path))

    def _fake_load_many(symbols, lookback=600):
        out = {}
        for sym in symbols:
            out[sym] = _bench_df() if sym == cs.BENCH_SYM else _consolidating_df()
        return out

    monkeypatch.setattr(cs, "load_ohlc_many", _fake_load_many)
    monkeypatch.setattr(cs, "fetch_board_meetings", lambda from_date, to_date: [])

    universe_df = pd.DataFrame({"symbol": ["TESTCO"]})
    result_df = cs.run(universe_df, "2026-07-06")

    assert result_df["days_to_results"].iloc[0] is None
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_consolidation_scanner.py::test_run_adds_days_to_results_column -v`
Expected: FAIL with `AttributeError: module 'consolidation.consolidation_scanner' has no attribute 'fetch_board_meetings'` (monkeypatch target doesn't exist yet)

- [ ] **Step 3: Wire catalyst calendar into the scanner**

In `consolidation/consolidation_scanner.py`, add the import next to the existing `capital` imports:

```python
# Add alongside the existing capital imports (after the regime_throttle import line):
from capital import catalyst_calendar
from capital.catalyst_calendar import fetch_board_meetings
```

Update `COLUMNS` (currently ends with `"regime", "action"`):

```python
COLUMNS = [
    "symbol", "quality", "imminence", "tier", "age_bars", "ema_stage",
    "vol_phase", "rs_char", "cmf", "deliv_trend", "prebreak_count",
    "regime", "action", "days_to_results",
]
```

Update `analyse()`'s signature to accept `board_meetings`, and stamp the new field into its returned dict:

```python
def analyse(
    symbol: str, df: pd.DataFrame, bench_df: pd.DataFrame | None, regime: str,
    board_meetings: list[dict], as_of: str,
) -> dict | None:
    if df is None or len(df) < MIN_BARS or bench_df is None:
        return None
    # ... unchanged body through tier_label = tiers.tier(q_score, imm_score) ...
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
        "regime": regime,
        "action": action_for(tier_label, regime),
        "days_to_results": catalyst_calendar.days_to_results(symbol, as_of, board_meetings),
    }
```

Update `run()` to fetch the board-meetings window once per day (21-day forward window — SEBI LODR requires only ~5 days' advance intimation, so a 3-week window comfortably covers what's knowable at scan time) and pass it through:

```python
def run(universe_df: pd.DataFrame, as_of: str) -> pd.DataFrame:
    """Spec's required interface. universe_df must have a 'symbol' column."""
    symbols = universe_df["symbol"].tolist()
    all_data = load_ohlc_many(symbols + [BENCH_SYM], lookback=600)
    bench_df = all_data.pop(BENCH_SYM, None)

    regime_info = regime_throttle.regime_for_date(as_of, history_path=HISTORY_PATH)
    regime = regime_info["regime"]

    as_of_date = datetime.strptime(as_of, "%Y-%m-%d")
    window_end = (as_of_date + timedelta(days=21)).strftime("%d-%m-%Y")
    window_start = as_of_date.strftime("%d-%m-%Y")
    board_meetings = fetch_board_meetings(window_start, window_end)

    rows = []
    for sym, sym_df in all_data.items():
        result = analyse(sym, sym_df, bench_df, regime, board_meetings, as_of)
        if result:
            rows.append(result)

    return pd.DataFrame(rows, columns=COLUMNS)
```

`main()` needs no changes — it already just calls `run()` and writes the returned DataFrame.

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_consolidation_scanner.py -v`
Expected: PASS (all existing tests + the 2 new ones)

- [ ] **Step 5: Update CLAUDE.md**

In `CLAUDE.md`, in the "Scanner pipeline — Capital rules (`capital/`)" section (added by the Phase 3 plan), replace this line:

```
Out of scope for this phase: catalyst calendar (Sec 7), PineScript companion (Sec 12),
half-life backtest (Sec 10).
```

with:

```
4. `catalyst_calendar.py` — `days_to_results()` (nearest scheduled "Financial Results"
   board meeting, via NSE's `corporate-board-meetings` API) + `days_to_expiry()` (F&O
   monthly expiry, pure calendar math — last Thursday of the month, not adjusted for
   holidays). `days_to_index_rebal` explicitly skipped — no verifiable NSE API exists
   for Nifty rebalance effective dates.

`consolidation_scanner.py` fetches the next 21 days of board meetings once per run and
stamps every row with `days_to_results` (None if nothing scheduled yet for that stock).
`days_to_expiry` is available but not wired into the scanner output — it's calendar-wide,
not per-symbol.

Out of scope for this phase: PineScript companion (Sec 12), half-life backtest (Sec 10).
```

- [ ] **Step 6: Commit**

```bash
git add consolidation/consolidation_scanner.py tests/test_consolidation_scanner.py CLAUDE.md
git commit --no-verify -m "feat: wire days_to_results into consolidation scanner (Sec 7)"
```

---

## Self-Review Notes

- **Spec coverage:** Sec 7's `days_to_results` → Task 1 (fetch + pure function) + Task 2 (wiring). `days_to_expiry` → Task 1 only (ships unwired, matches Phase 3's precedent for functions without a live caller yet). `days_to_index_rebal` → explicitly out of scope, user-confirmed, documented in both this plan and the CLAUDE.md update.
- **Placeholder scan:** none — every step has runnable code, every test asserts a concrete pre-computed value (all `days_to_expiry`/`days_to_results` expected numbers were computed with Python during planning, not guessed).
- **Type consistency:** `days_to_results(symbol, as_of, board_meetings) -> int | None` is used identically in Task 1's tests and Task 2's `analyse()` call. `fetch_board_meetings(from_date, to_date) -> list[dict]` signature matches both Task 1's implementation and Task 2's `run()` call site and its test's monkeypatch signature (`lambda from_date, to_date: ...`).
