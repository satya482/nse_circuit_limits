# Union Watchlist 30-Day Liquidity Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Apply a fail-open minimum ₹10 crore 30-session average traded-value gate to every tier of the inclusive Union Watchlist without changing standalone scanner results.

**Architecture:** Add pure calculation and source-set filtering helpers to `ema55_cross_scanner.py`, then call the existing batch OHLC loader once after at least two fresh sources have been assembled and before `build_union()`. The EMA55 report will expose excluded and retained-unverified counts outside its TradingView fence; `union_chart_dashboard.py` remains unchanged because it already parses the filtered tier fence.

**Tech Stack:** Python 3, pandas, pytest, Markdown report generation, existing `ohlc_db.load_ohlc_many()` data access.

## Global Constraints

- Formula: `SMA(volume, 30) × latest completed daily close ÷ 10,000,000`.
- The threshold is inclusive: exactly `10.0` crore passes.
- Zero-volume sessions are valid; negative volume, non-positive close, non-finite values, stale data, and fewer than 30 rows are unverified.
- Fail open: retain unverified candidates and list them alphabetically in the Union section.
- Apply the gate before confluence calculation to every Union tier, from `ALL n` through `1 ONLY`.
- Do not alter the standalone EMA55 Cross rows, upstream scanners, or `union_chart_dashboard.py`.
- Do not call OHLC storage when fewer than two source sets are available.
- Use one `ohlc_db.load_ohlc_many(..., lookback=30)` call for all deduplicated candidates.
- Every generated or newly created Markdown/HTML file must contain `SEBI registered`; use the existing disclaimer constants in generators.
- Preserve unrelated `.ohlc_data/data_manifest.csv` and `.superpowers/` worktree changes.

---

## File Map

- Modify `ema55_cross_scanner.py`: calculate liquidity, filter copied source sets, batch-load candidate OHLCV, tier the filtered sets, and render gate status.
- Modify `tests/test_ema55_cross_scanner.py`: unit and report-integration coverage for the formula, fail-open cases, tier recalculation, one-batch-load behavior, and standalone-list isolation.
- Modify `HANDOFF.md`: record the new production rule, test evidence, and whether live artifacts were regenerated.
- Do not modify `union_chart_dashboard.py`: its `parse_union_tiers()` function already reads only the first confluence-tier TradingView fence.

### Task 1: Pure Liquidity Calculation and Source-Set Filter

**Files:**
- Modify: `tests/test_ema55_cross_scanner.py`
- Modify: `ema55_cross_scanner.py` near the Union Watchlist helpers

**Interfaces:**
- Consumes: an oldest-first `pd.DataFrame` with `date`, `close`, and `volume`; `report_date: str`; `source_sets: dict[str, set[str]]`; `ohlc_map: dict[str, pd.DataFrame]`.
- Produces: `average_traded_value_cr(df: pd.DataFrame, report_date: str) -> float | None`.
- Produces: `filter_union_sources(source_sets: dict[str, set[str]], ohlc_map: dict[str, pd.DataFrame], report_date: str, threshold_cr: float = 10.0) -> tuple[dict[str, set[str]], list[str], list[str]]`, returning copied filtered sets, sorted verified exclusions, and sorted retained-unverified symbols.

- [ ] **Step 1: Add a compact OHLC fixture and failing formula-boundary tests**

Add these imports and tests to `tests/test_ema55_cross_scanner.py`:

```python
import math

from ema55_cross_scanner import (
    average_traded_value_cr,
    filter_union_sources,
)


def _liquidity_df(
    *,
    rows: int = 30,
    close: float = 100.0,
    volume: float = 1_000_000.0,
    end: str = TODAY,
) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "date": pd.bdate_range(end=end, periods=rows),
            "close": [close] * rows,
            "volume": [volume] * rows,
        }
    )


def test_average_traded_value_uses_30_session_sma_and_latest_close():
    df = _liquidity_df(close=200.0, volume=50_000.0)
    df.loc[df.index[0], "volume"] = 0.0

    expected = ((29 * 50_000.0) / 30) * 200.0 / 10_000_000
    assert math.isclose(average_traded_value_cr(df, TODAY), expected)


def test_filter_union_sources_includes_exact_ten_crore_and_excludes_below():
    sources = {"EMA55 Cross": {"EXACT", "LOW"}, "Trend": {"EXACT", "LOW"}}
    ohlc = {
        "EXACT": _liquidity_df(close=100.0, volume=1_000_000.0),
        "LOW": _liquidity_df(close=100.0, volume=999_999.0),
    }

    filtered, excluded, unverified = filter_union_sources(sources, ohlc, TODAY)

    assert filtered == {"EMA55 Cross": {"EXACT"}, "Trend": {"EXACT"}}
    assert excluded == ["LOW"]
    assert unverified == []
```

- [ ] **Step 2: Run the new formula tests and verify they fail**

Run:

```powershell
python -m pytest tests/test_ema55_cross_scanner.py -k "average_traded_value or exact_ten_crore" -v
```

Expected: test collection fails because `average_traded_value_cr` and `filter_union_sources` are not defined.

- [ ] **Step 3: Add failing fail-open, validation, non-mutation, and tier tests**

Append:

```python
def test_filter_union_sources_retains_and_sorts_unverified_histories():
    stale = _liquidity_df(end="2000-01-31")
    invalid_close = _liquidity_df()
    invalid_close.loc[invalid_close.index[-1], "close"] = float("nan")
    negative_volume = _liquidity_df()
    negative_volume.loc[negative_volume.index[3], "volume"] = -1
    sources = {
        "EMA55 Cross": {"STALE", "MISSING", "SHORT"},
        "Trend": {"BAD_CLOSE", "BAD_VOLUME"},
    }
    ohlc = {
        "STALE": stale,
        "SHORT": _liquidity_df(rows=29),
        "BAD_CLOSE": invalid_close,
        "BAD_VOLUME": negative_volume,
    }

    filtered, excluded, unverified = filter_union_sources(sources, ohlc, TODAY)

    assert filtered == sources
    assert excluded == []
    assert unverified == ["BAD_CLOSE", "BAD_VOLUME", "MISSING", "SHORT", "STALE"]


def test_filter_union_sources_treats_nonpositive_close_and_nonnumeric_volume_as_unverified():
    zero_close = _liquidity_df(close=0.0)
    bad_volume = _liquidity_df()
    bad_volume.loc[bad_volume.index[0], "volume"] = "unknown"
    sources = {"EMA55 Cross": {"ZERO", "TEXT"}, "Trend": {"ZERO", "TEXT"}}

    filtered, excluded, unverified = filter_union_sources(
        sources, {"ZERO": zero_close, "TEXT": bad_volume}, TODAY
    )

    assert filtered == sources
    assert excluded == []
    assert unverified == ["TEXT", "ZERO"]


def test_filter_union_sources_does_not_mutate_inputs_and_recalculates_tiers():
    sources = {
        "EMA55 Cross": {"LIQUID", "LOW"},
        "EMA25 ZL": {"LIQUID", "LOW", "ONLY"},
        "Trend": {"LIQUID", "ONLY"},
    }
    original = {name: set(symbols) for name, symbols in sources.items()}
    ohlc = {
        "LIQUID": _liquidity_df(),
        "LOW": _liquidity_df(volume=50_000.0),
        "ONLY": _liquidity_df(),
    }

    filtered, excluded, unverified = filter_union_sources(sources, ohlc, TODAY)

    assert sources == original
    assert excluded == ["LOW"]
    assert unverified == []
    assert build_union(filtered) == [
        ("ALL 3", ["LIQUID"]),
        ("2 OF 3", ["ONLY"]),
    ]
```

- [ ] **Step 4: Run the expanded helper tests and verify they fail**

Run:

```powershell
python -m pytest tests/test_ema55_cross_scanner.py -k "filter_union_sources or average_traded_value" -v
```

Expected: FAIL because the helpers are absent.

- [ ] **Step 5: Implement the pure helpers**

Change the OHLC import in `ema55_cross_scanner.py` and add the helpers immediately before `build_union()`:

```python
from ohlc_db import load_ohlc, load_ohlc_many, liq_tag, cmf_tag, deliv_tag

UNION_LIQUIDITY_LOOKBACK = 30
UNION_LIQUIDITY_MIN_CR = 10.0


def average_traded_value_cr(df: pd.DataFrame, report_date: str) -> float | None:
    """Return 30-session average volume times latest close in crore rupees.

    None means the threshold cannot be verified from complete, current, valid data.
    """
    try:
        if df is None or len(df) < UNION_LIQUIDITY_LOOKBACK:
            return None
        bars = df.iloc[-UNION_LIQUIDITY_LOOKBACK:]
        latest_date = pd.to_datetime(bars["date"].iloc[-1], errors="coerce")
        expected_date = pd.to_datetime(report_date, errors="coerce")
        if pd.isna(latest_date) or pd.isna(expected_date):
            return None
        if latest_date.normalize() != expected_date.normalize():
            return None

        close = pd.to_numeric(bars["close"], errors="coerce")
        volume = pd.to_numeric(bars["volume"], errors="coerce")
        latest_close = float(close.iloc[-1])
        if not pd.notna(latest_close) or not math.isfinite(latest_close) or latest_close <= 0:
            return None
        if volume.isna().any() or not np.isfinite(volume.to_numpy(dtype=float)).all():
            return None
        if (volume < 0).any():
            return None
        return float(volume.mean() * latest_close / 10_000_000)
    except Exception:
        return None


def filter_union_sources(
    source_sets: dict[str, set[str]],
    ohlc_map: dict[str, pd.DataFrame],
    report_date: str,
    threshold_cr: float = UNION_LIQUIDITY_MIN_CR,
) -> tuple[dict[str, set[str]], list[str], list[str]]:
    """Filter copied Union source sets, retaining candidates with unverified OHLCV."""
    allowed: set[str] = set()
    excluded: list[str] = []
    unverified: list[str] = []
    candidates = sorted(set().union(*source_sets.values())) if source_sets else []
    for symbol in candidates:
        value_cr = average_traded_value_cr(ohlc_map.get(symbol), report_date)
        if value_cr is None:
            allowed.add(symbol)
            unverified.append(symbol)
        elif value_cr >= threshold_cr:
            allowed.add(symbol)
        else:
            excluded.append(symbol)
    filtered = {name: set(symbols) & allowed for name, symbols in source_sets.items()}
    return filtered, excluded, unverified
```

Also add `import math` and `import numpy as np` beside the existing standard-library and pandas imports. Do not call the database from either helper.

- [ ] **Step 6: Run helper tests**

Run:

```powershell
python -m pytest tests/test_ema55_cross_scanner.py -k "filter_union_sources or average_traded_value" -v
```

Expected: all selected tests PASS.

- [ ] **Step 7: Commit the pure helper slice**

Run:

```powershell
git add ema55_cross_scanner.py tests/test_ema55_cross_scanner.py
git commit --no-verify -m "feat(union): add liquidity gate helpers"
```

Expected: only those two files are committed; `.ohlc_data/data_manifest.csv` and `.superpowers/` remain unstaged.

### Task 2: Report Integration and Fail-Open Status

**Files:**
- Modify: `tests/test_ema55_cross_scanner.py`
- Modify: `ema55_cross_scanner.py` in `build_union_section()` and `build_markdown()`

**Interfaces:**
- Consumes: Task 1's `filter_union_sources(...)` return tuple and the existing `build_union(...)` result.
- Produces: `build_union_section(union_groups, notes, excluded_symbols=None, unverified_symbols=None) -> list[str]` with compatibility defaults.
- Produces: one guarded call to `load_ohlc_many(sorted(candidates), lookback=30)` when `len(source_sets) >= 2`.

- [ ] **Step 1: Add failing rendering tests for the threshold summary and sorted warning**

Append:

```python
def test_union_section_reports_liquidity_exclusions_and_unverified_symbols():
    section = "\n".join(
        build_union_section(
            [("ALL 2", ["LIQUID"])],
            [],
            excluded_symbols=["LOW"],
            unverified_symbols=["BETA", "ALPHA"],
        )
    )

    assert "Avg Volume 30D × latest close ≥ ₹10 Cr" in section
    assert "Excluded below threshold: 1" in section
    assert "Liquidity unverified (retained): ALPHA, BETA" in section
    assert section.index("Liquidity unverified") < section.index("```")
```

- [ ] **Step 2: Add failing integration tests for one batch load and no-load degradation**

Append:

```python
def test_build_markdown_filters_union_with_one_sorted_batch_load(monkeypatch):
    def fake_source(path, skip_labels, name):
        return {"LIQUID", "LOW", "MISSING"}, None

    calls = []

    def fake_many(symbols, lookback):
        calls.append((symbols, lookback))
        return {
            "LIQUID": _liquidity_df(),
            "LOW": _liquidity_df(volume=50_000.0),
        }

    monkeypatch.setattr(scanner, "_load_union_source", fake_source)
    monkeypatch.setattr(scanner, "load_ohlc_many", fake_many)

    report = scanner.build_markdown([], {})

    assert calls == [(["LIQUID", "LOW", "MISSING"], 30)]
    union_block = report.split("### Scan definition", 1)[0]
    assert "NSE:LIQUID" in union_block
    assert "NSE:MISSING" in union_block
    assert "NSE:LOW" not in union_block
    assert "Excluded below threshold: 1" in union_block
    assert "Liquidity unverified (retained): MISSING" in union_block


def test_build_markdown_skips_liquidity_load_with_only_ema55_source(monkeypatch):
    monkeypatch.setattr(scanner, "_load_union_source", lambda *args: (None, "stale"))

    def unexpected_load(*args, **kwargs):
        raise AssertionError("load_ohlc_many must not run for one source")

    monkeypatch.setattr(scanner, "load_ohlc_many", unexpected_load)

    report = scanner.build_markdown([{"symbol": "EMA55ONLY", "cross_days": 1}], {})

    assert "No union data available today" in report
```

For the last fixture, avoid `_table_rows()` requiring a complete finding by monkeypatching it within the test:

```python
    monkeypatch.setattr(scanner, "_table_rows", lambda *args: ["| EMA55ONLY |"])
```

- [ ] **Step 3: Add failing tests for loader failure and standalone EMA55 isolation**

Append:

```python
def test_build_markdown_retains_candidates_when_batch_load_fails(monkeypatch):
    monkeypatch.setattr(
        scanner, "_load_union_source", lambda *args: ({"EMA55SYM", "UPSTREAM"}, None)
    )
    monkeypatch.setattr(
        scanner, "load_ohlc_many", lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("db down"))
    )
    monkeypatch.setattr(scanner, "_table_rows", lambda *args: ["| EMA55SYM |"])
    finding = {"symbol": "EMA55SYM", "cross_days": 1}

    report = scanner.build_markdown([finding], {})
    union_block, standalone = report.split("### Scan definition", 1)

    assert "NSE:EMA55SYM" in union_block
    assert "NSE:UPSTREAM" in union_block
    assert "Liquidity unverified (retained): EMA55SYM, UPSTREAM" in union_block
    assert "EMA55SYM" in standalone


def test_low_liquidity_symbol_is_removed_only_from_union(monkeypatch):
    monkeypatch.setattr(scanner, "_load_union_source", lambda *args: ({"LOW"}, None))
    monkeypatch.setattr(
        scanner,
        "load_ohlc_many",
        lambda *args, **kwargs: {"LOW": _liquidity_df(volume=50_000.0)},
    )
    monkeypatch.setattr(scanner, "_table_rows", lambda *args: ["| LOW |"])
    finding = {"symbol": "LOW", "cross_days": 1}

    report = scanner.build_markdown([finding], {})
    union_block, standalone = report.split("### Scan definition", 1)

    assert "NSE:LOW" not in union_block
    assert "Excluded below threshold: 1" in union_block
    assert "| LOW |" in standalone
    assert "NSE:LOW" in standalone
```

- [ ] **Step 4: Run the new report integration tests and verify they fail**

Run:

```powershell
python -m pytest tests/test_ema55_cross_scanner.py -k "liquidity_exclusions or sorted_batch or skips_liquidity or batch_load_fails or removed_only" -v
```

Expected: FAIL because the report does not yet accept or render liquidity results and does not batch-load Union OHLCV.

- [ ] **Step 5: Render gate status outside the TradingView fence**

Change `build_union_section()` to accept compatibility defaults, normalize ordering, and add the summary before the empty-data/fence branches:

```python
def build_union_section(
    union_groups: list[tuple[str, list[str]]],
    notes: list[str],
    excluded_symbols: list[str] | None = None,
    unverified_symbols: list[str] | None = None,
) -> list[str]:
    excluded_symbols = sorted(excluded_symbols or [])
    unverified_symbols = sorted(unverified_symbols or [])
    lines = [
        "### 🟢 Union Watchlist — EMA25 ZL + EMA55 Cross + Minervini Trend Template + Trend Scanner + Weekly RS EMA9",
        "*(sectioned by confluence — how many of the scanners flagged the symbol today)*",
        "",
    ]
    if notes:
        lines.append(f"*({'; '.join(notes)})*")
        lines.append("")
    lines += [
        f"**Liquidity gate:** Avg Volume 30D × latest close ≥ ₹{UNION_LIQUIDITY_MIN_CR:g} Cr "
        f"· **Excluded below threshold: {len(excluded_symbols)}**",
        "",
    ]
    if unverified_symbols:
        lines += [
            f"⚠️ **Liquidity unverified (retained):** {', '.join(unverified_symbols)}",
            "",
        ]
```

Keep the existing `if not union_groups`, counts, fence, and separator logic after this insertion. Do not put either liquidity line inside a fenced block.

- [ ] **Step 6: Batch-load and filter immediately before tier calculation**

Replace the direct `union_groups = build_union(source_sets)` in `build_markdown()` with:

```python
    excluded_symbols: list[str] = []
    unverified_symbols: list[str] = []
    filtered_source_sets = source_sets
    if len(source_sets) >= 2:
        candidates = sorted(set().union(*source_sets.values()))
        try:
            ohlc_map = load_ohlc_many(candidates, lookback=UNION_LIQUIDITY_LOOKBACK)
        except Exception:
            ohlc_map = {}
        filtered_source_sets, excluded_symbols, unverified_symbols = filter_union_sources(
            source_sets, ohlc_map, TODAY
        )
    union_groups = build_union(filtered_source_sets)
```

Then replace the report call with:

```python
        *build_union_section(
            union_groups,
            union_notes,
            excluded_symbols=excluded_symbols,
            unverified_symbols=unverified_symbols,
        ),
```

The rest of `build_markdown()` must continue using the original `rows` for the standalone table and age-group TradingView blocks. Only its confluence marker may derive from the filtered `union_groups`.

- [ ] **Step 7: Run all focused EMA55 tests**

Run:

```powershell
python -m pytest tests/test_ema55_cross_scanner.py -v
```

Expected: all tests PASS, including pre-existing source freshness and five-tier tests.

- [ ] **Step 8: Verify the dashboard parser still consumes a report with liquidity prose**

Run:

```powershell
python -m pytest tests/test_union_chart_dashboard.py -k "parse_union_tiers or load_todays_union" -v
```

Expected: all selected tests PASS. No dashboard source changes are needed because the summary and warning precede the same first confluence-tier fence.

- [ ] **Step 9: Commit report integration**

Run:

```powershell
git add ema55_cross_scanner.py tests/test_ema55_cross_scanner.py
git commit --no-verify -m "feat(union): enforce liquidity threshold"
```

Expected: only the scanner and its focused test file are committed.

### Task 3: Production Verification and Handoff

**Files:**
- Modify: `HANDOFF.md`
- Conditionally regenerate: `ema55_cross_scans/ema55_cross_scans.md`
- Conditionally regenerate: `ema55_cross_scans/ema55_cross_scans_YYYY-MM-DD.md`
- Conditionally regenerate: `dashboard/union_charts.html`

**Interfaces:**
- Consumes: the completed scanner report contract from Task 2.
- Produces: test evidence and, only when all inputs are current and local credentials/network access are expected, a current Union report and dashboard artifact.

- [ ] **Step 1: Run focused scanner and dashboard suites together**

Run:

```powershell
python -m pytest tests/test_ema55_cross_scanner.py tests/test_union_chart_dashboard.py -v
```

Expected: all focused tests PASS.

- [ ] **Step 2: Run the full repository suite**

Run:

```powershell
python -m pytest
```

Expected: the full suite PASS; record the exact count and any pre-existing warnings for `HANDOFF.md`.

- [ ] **Step 3: Check whether a live generation is safe and meaningful**

Run:

```powershell
rg -n "^# .*2026-08-28" ema25_zl_scans/ema25_zl_scans.md minervini_scans/minervini_trend_latest.md trend_scans/trend_scan_latest.md rs_weekly_scans/rs_weekly_ema9_scans.md
python -c "from ohlc_db import latest_date; print(latest_date())"
```

Expected for a live run: every upstream heading and the database latest date are `2026-08-28`. If inputs are stale or local credentials/network access are not expected, do not run scanners; preserve existing generated artifacts and state the reason in `HANDOFF.md`.

- [ ] **Step 4: If current inputs are available, run the normal EMA55 scanner and dashboard generator**

Run only when Step 3 confirms current data and the user expects live TradingView/NSE access:

```powershell
python ema55_cross_scanner.py
python union_chart_dashboard.py
```

Expected: the EMA55 report is regenerated for `2026-08-28`, the Union section reports its liquidity exclusion count and any unverified retained names, and the dashboard is regenerated from the filtered Union tier fence. Do not refresh unrelated scanners or raw market data.

- [ ] **Step 5: Verify generated artifacts or preservation**

For a live run, execute:

```powershell
rg -n "SEBI registered|Liquidity gate|Excluded below threshold|Liquidity unverified|###(ALL [2-5]|[2-4] OF [2-5]|1 ONLY)" ema55_cross_scans/ema55_cross_scans.md
rg -n "SEBI registered|Union Watchlist Charts" dashboard/union_charts.html
```

Expected: both artifacts contain `SEBI registered`; the report contains the threshold/exclusion summary; any warning is outside the TradingView fence; tier symbols match what the dashboard embeds. If Step 4 was skipped, verify `git diff --name-only` shows no generated artifact changes.

- [ ] **Step 6: Update `HANDOFF.md` with the implementation and evidence**

Add a dated entry at the top of `Current Worktree State` using the actual results:

```markdown
Updated 2026-08-28 by Codex, Union Watchlist 30-day liquidity gate:

- The inclusive Union Watchlist now applies `Avg Volume 30D × latest close >= ₹10 Cr` before confluence tiers are calculated; standalone scanner eligibility and output remain unchanged.
- Missing, stale, short, or invalid OHLCV remains fail-open and is named in the Union warning; verified symbols below the threshold are excluded.
- Verification: record the exact focused-test and full-suite pass counts printed in Steps 1 and 2; `git diff --check` passed.
- State either the generated report/dashboard record counts or the exact stale-input reason that caused the existing artifacts to be preserved.
```

Replace the evidence instructions with the exact observed values. Retain the existing SEBI disclaimer already present in `HANDOFF.md`.

- [ ] **Step 7: Run final repository hygiene checks**

Run:

```powershell
git diff --check
git status --short
git diff --stat
```

Expected: no whitespace errors; only intended code, tests, documentation, and conditionally generated artifacts appear in the task diff. Confirm `.ohlc_data/data_manifest.csv` and `.superpowers/` are still unstaged user changes.

- [ ] **Step 8: Commit documentation and any verified artifacts**

Stage only paths changed by this task, adjusting the generated-file list to match Step 4:

```powershell
git add HANDOFF.md ema55_cross_scans/ema55_cross_scans.md dashboard/union_charts.html
git commit --no-verify -m "docs(union): record liquidity gate rollout"
```

If live generation was skipped, stage only `HANDOFF.md`. If a dated EMA55 report was generated, stage its exact `ema55_cross_scans/ema55_cross_scans_2026-08-28.md` path too. Do not stage `.ohlc_data/data_manifest.csv` or `.superpowers/`.

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
