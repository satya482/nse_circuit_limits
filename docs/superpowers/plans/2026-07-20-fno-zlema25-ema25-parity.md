> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# F&O ZLEMA25 EMA25-Scanner Parity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the five-bar F&O turn-event report with an EMA25-parity scanner that applies the broad scanner's eligibility, RS, float, and enrichment logic and reports current ZLEMA25 uptrends and downtrends with direction-specific ages.

**Architecture:** Extend `ema25_zl_scanner.py` with backward-compatible direction-aware turn statistics and optional directional report rendering. Rewrite `fno_zlema25_scanner.py` as a thin adapter that intersects the authoritative NSE F&O list with the broad TradingView eligibility list, reuses shared analysis, and selects the directional report mode.

**Tech Stack:** Python 3.13, pandas, pytest, TradingView Screener, repository OHLC/float/disclaimer helpers, PowerShell.

## Global Constraints

- The authoritative universe remains `fno_universe.get_fno_symbols()` and its NSE `SECURITIES IN F&O` endpoint/cache behavior.
- TradingView eligibility can remove an F&O symbol but can never introduce a non-F&O symbol.
- Preserve the current default behavior and output of `ema25_zl_scanner.py`.
- Uptrend age starts at `1d` on a non-positive-to-positive ZLEMA25 slope change; downtrend age starts at `1d` on a non-negative-to-negative change.
- Directional ages cap at `60d+`; change percentage uses the close immediately before the direction-change candle.
- Exact-flat ZLEMA25 slopes appear only in the Flat summary count.
- Keep existing F&O output paths and PowerShell runner.
- All created Markdown files must contain `SEBI registered`.
- Preserve unrelated changes in the shared worktree.

---

### Task 1: Direction-aware shared EMA25 analysis and reporting

**Files:**
- Modify: `ema25_zl_scanner.py`
- Create: `tests/test_fno_zlema25_scanner.py`

**Interfaces:**
- Produces: `zl25_turn_stats(zl25: pd.Series, closes: pd.Series, direction: str = "up") -> tuple[int, float]`.
- Produces: `analyse(...)` findings with `zl_direction`, `zl_down_days`, and `zl_down_pct` while preserving existing `zl_rising`, `zl_days`, and `zl_pct` fields.
- Produces: backward-compatible `build_markdown(..., *, title: str | None = None, universe_label: str = "NSE common equity", directional: bool = False, universe_stats: str | None = None) -> str`.

- [ ] **Step 1: Write failing direction-stat tests**

Add synthetic-series tests to `tests/test_fno_zlema25_scanner.py`:

```python
import pandas as pd

import ema25_zl_scanner as broad


def test_downtrend_turn_stats_starts_at_one_day_and_uses_pre_turn_close():
    zl25 = pd.Series([3.0, 3.0, 2.0])
    closes = pd.Series([100.0, 110.0, 99.0])

    assert broad.zl25_turn_stats(zl25, closes, direction="down") == (1, -10.0)


def test_downtrend_turn_stats_counts_continuing_bars():
    zl25 = pd.Series([3.0, 3.0, 2.0, 1.0])
    closes = pd.Series([100.0, 110.0, 99.0, 90.0])

    assert broad.zl25_turn_stats(zl25, closes, direction="down") == (2, -18.18)


def test_turn_stats_rejects_unknown_direction():
    with pytest.raises(ValueError, match="direction"):
        broad.zl25_turn_stats(pd.Series([1.0, 2.0, 3.0]), pd.Series([1.0, 2.0, 3.0]), "sideways")
```

- [ ] **Step 2: Run the tests and verify RED**

Run: `python -m pytest tests/test_fno_zlema25_scanner.py -v --basetemp=.pytest_tmp`

Expected: FAIL because `zl25_turn_stats` does not accept `direction`.

- [ ] **Step 3: Generalize turn statistics and enrich findings**

Change `zl25_turn_stats` to validate `direction`, use the existing up-turn condition for `up`, and use `zl25[i] < zl25[i-1] and zl25[i-1] >= zl25[i-2]` for `down`. Preserve the existing cap fallback.

In `analyse`, calculate:

```python
if zl25.iloc[-1] > zl25.iloc[-2]:
    zl_direction = "up"
elif zl25.iloc[-1] < zl25.iloc[-2]:
    zl_direction = "down"
else:
    zl_direction = "flat"

zl_days, zl_pct = zl25_turn_stats(zl25, c, "up")
zl_down_days, zl_down_pct = zl25_turn_stats(zl25, c, "down")
```

Return the three new fields without removing or renaming existing fields.

- [ ] **Step 4: Verify direction-stat GREEN**

Run: `python -m pytest tests/test_fno_zlema25_scanner.py -v --basetemp=.pytest_tmp`

Expected: PASS.

- [ ] **Step 5: Write failing directional-report tests**

Add findings for one uptrend, one downtrend, and one flat symbol. Assert that `directional=True` produces Uptrend and Downtrend tables, `UP 1 DAY` and `DOWN 2 DAYS` TradingView sections, a Flat count of one, the F&O title/universe statistics, and the disclaimer. Also assert that a default call still contains `# NSE EMA25 ZL Scan`, `ZLEMA25 Rising`, and `ZLEMA25 Watch`.

- [ ] **Step 6: Run the report tests and verify RED**

Run: `python -m pytest tests/test_fno_zlema25_scanner.py -v --basetemp=.pytest_tmp`

Expected: FAIL because `build_markdown` has no directional or presentation options.

- [ ] **Step 7: Add backward-compatible report options**

Add keyword-only report options. Build the scan-definition header from `universe_label`. Keep the existing branch byte-for-byte equivalent when `directional=False`.

For `directional=True`:

```python
uptrend = [f for f in findings if f["zl_direction"] == "up"]
downtrend = [
    {**f, "zl_days": f["zl_down_days"], "zl_pct": f["zl_down_pct"]}
    for f in findings
    if f["zl_direction"] == "down"
]
flat_count = sum(f["zl_direction"] == "flat" for f in findings)
```

Sort both lists by `(zl_days, symbol)`. Render symmetric tables and individual age-bucket blocks. Prefix combined TradingView sections with `UP ` and `DOWN ` so labels are unique.

- [ ] **Step 8: Verify shared report GREEN and broad regression behavior**

Run: `python -m pytest tests/test_fno_zlema25_scanner.py tests/test_nifty50_zlema25_scanner.py -v --basetemp=.pytest_tmp`

Expected: PASS, including the default broad-report assertions.

- [ ] **Step 9: Commit the shared capability**

```powershell
git add -- ema25_zl_scanner.py tests/test_fno_zlema25_scanner.py
git commit --no-verify -m "feat: add directional ZLEMA25 reporting"
```

---

### Task 2: Convert the F&O scanner into the parity adapter

**Files:**
- Modify: `fno_zlema25_scanner.py`
- Modify: `tests/test_fno_zlema25_scanner.py`

**Interfaces:**
- Consumes: `fno_universe.get_fno_symbols()`.
- Consumes: shared `get_watchlist`, `analyse`, `get_circuit_limits`, `get_names`, and directional `build_markdown` from `ema25_zl_scanner.py`.
- Produces: `intersect_universe(fno_symbols: list[str], eligible_symbols: list[str]) -> list[str]` preserving F&O order and uniqueness.
- Produces: unchanged latest and dated F&O Markdown paths.

- [ ] **Step 1: Write failing adapter tests**

Add tests that assert:

```python
def test_intersection_preserves_fno_order_and_never_adds_non_fno():
    assert scanner.intersect_universe(
        ["RELIANCE", "INFY", "RELIANCE", "TCS"],
        ["TCS", "NOTFNO", "RELIANCE"],
    ) == ["RELIANCE", "TCS"]
```

Monkeypatch the F&O universe, TradingView eligibility, benchmark loader, shared analyser, circuit loader, names loader, and report writer inputs. Assert only intersected symbols are analysed, each receives its float value, and directional report mode receives F&O title, universe label, and source/eligible counts.

- [ ] **Step 2: Run adapter tests and verify RED**

Run: `python -m pytest tests/test_fno_zlema25_scanner.py -v --basetemp=.pytest_tmp`

Expected: FAIL because the current scanner contains standalone five-bar turn logic and has no intersection adapter.

- [ ] **Step 3: Rewrite the F&O orchestration**

Remove the duplicated EMA/ZLEMA/squeeze/recent-turn/report implementation. Import and reuse the broad scanner capabilities. Implement ordered, unique intersection with an eligibility set.

Load `NIFTY MIDSML 400` through `ohlc_db.load_ohlc`, prepare the dated index series exactly as the broad scanner does, and fail with a non-zero return when it is unavailable. Analyse only intersected symbols, preserving the float lookup.

Call the shared builder with:

```python
build_markdown(
    findings,
    circuit,
    names,
    title=f"NSE F&O ZLEMA25 Scan — {TODAY}",
    universe_label="NSE F&O underlyings eligible under broad EMA25 ZL filters",
    directional=True,
    universe_stats=f"{len(fno_symbols)} NSE F&O stocks · {len(symbols)} TradingView-eligible",
)
```

Write both existing output files only after building the complete report. Make `main()` return `0` on success and non-zero on fatal benchmark/universe/eligibility errors; exit through `raise SystemExit(main())`.

- [ ] **Step 4: Verify adapter GREEN**

Run: `python -m pytest tests/test_fno_zlema25_scanner.py -v --basetemp=.pytest_tmp`

Expected: PASS.

- [ ] **Step 5: Verify the PowerShell runner propagates Python failure**

Add a static test requiring `$LASTEXITCODE` to be checked after Python execution. Update `run_fno_zlema25_scanner.ps1` only if the test proves the current `try/catch` does not enforce this contract.

Run: `python -m pytest tests/test_fno_zlema25_scanner.py -v --basetemp=.pytest_tmp`

Expected: first RED on the current runner, then PASS after adding an explicit non-zero exit check.

- [ ] **Step 6: Commit the F&O adapter**

```powershell
git add -- fno_zlema25_scanner.py run_fno_zlema25_scanner.ps1 tests/test_fno_zlema25_scanner.py
git commit --no-verify -m "feat: align F&O ZLEMA25 scanner"
```

---

### Task 3: Documentation, generated output, and verification

**Files:**
- Modify: `HANDOFF.md`
- Modify: `CLAUDE.md` only if its existing F&O scanner operating notes are now inaccurate.
- Modify: `fno_zlema25_scans/fno_zlema25_scans.md`
- Create: `fno_zlema25_scans/fno_zlema25_scans_YYYY-MM-DD.md` only when the live run succeeds for the current date.

**Interfaces:**
- Consumes: completed parity scanner and production PowerShell contract.
- Produces: current operational handoff and a regenerated report from real local data.

- [ ] **Step 1: Run focused and related tests**

Run: `python -m pytest tests/test_fno_zlema25_scanner.py tests/test_nifty50_zlema25_scanner.py tests/test_backtest_daily_zlema25_weekly_rs.py -v --basetemp=.pytest_tmp`

Expected: all pass.

- [ ] **Step 2: Run the complete test suite**

Run: `python -m pytest --basetemp=.pytest_tmp`

Expected: all pass with no new failures.

- [ ] **Step 3: Parse the PowerShell runner**

Run:

```powershell
$errors = $null
[System.Management.Automation.Language.Parser]::ParseFile(
    (Resolve-Path 'run_fno_zlema25_scanner.ps1'),
    [ref]$null,
    [ref]$errors
) | Out-Null
if ($errors.Count) { $errors | Format-List; exit 1 }
```

Expected: exit 0 with no parse errors.

- [ ] **Step 4: Run the real scanner**

Run: `python fno_zlema25_scanner.py`

Expected: exit 0, current latest/dated reports, F&O-only eligible counts, and populated Uptrend/Downtrend tables. If the TradingView request is blocked by the sandbox, request network escalation and rerun; do not fabricate generated output.

- [ ] **Step 5: Update operating documentation**

Add a dated `HANDOFF.md` entry describing the NSE F&O source, broad eligibility intersection, shared gates/enrichment, current-direction tables, symmetric ages/watchlists, runner behavior, test totals, and live-run counts. Correct any contradictory `CLAUDE.md` scanner description. Preserve both files' SEBI disclaimer.

- [ ] **Step 6: Verify report invariants and worktree quality**

Run:

```powershell
rg -n "SEBI registered|ZLEMA25 Uptrend|ZLEMA25 Downtrend|UP 1 DAY|DOWN 1 DAY" fno_zlema25_scans/fno_zlema25_scans.md
git diff --check
git status --short
```

Expected: disclaimer and directional sections are present, no whitespace errors, and only intended files are modified.

- [ ] **Step 7: Commit the documentation and generated report**

```powershell
git add -- HANDOFF.md CLAUDE.md fno_zlema25_scans/fno_zlema25_scans.md fno_zlema25_scans/fno_zlema25_scans_YYYY-MM-DD.md
git commit --no-verify -m "docs: hand off F&O ZLEMA25 parity"
```

Omit unchanged files and a dated report that was not successfully regenerated.

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
