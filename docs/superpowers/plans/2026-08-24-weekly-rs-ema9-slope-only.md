> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Weekly RS EMA9 Slope-Only Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the weekly RS scanner qualify stocks solely on a flat/rising weekly RS EMA9 and use the EMA55 scanner's market-cap range.

**Architecture:** Keep `rs_weekly_ema9_scanner.py` self-contained. Replace its daily-above-EMA age with consecutive weekly non-falling EMA9 transitions, change only its TradingView market-cap constants, and update report/docs without altering runners or persistent file paths.

**Tech Stack:** Python 3.13, pandas, tradingview-screener, pytest, PowerShell runner.

## Global Constraints

- Weekly RS remains `(stock / NIFTY MIDSML 400) * 1000` with the current partial week included.
- Qualification is `latest weekly EMA9 slope >= -SLOPE_EPS`; daily RS position is not a gate.
- `Age(w)` counts consecutive non-falling weekly EMA9 transitions; a current falling transition has age zero.
- Universe is NSE common equity, price above Rs50, market cap Rs1,000 Cr through Rs5 lakh Cr.
- Do not add EMA55 price signals or the float gate.
- Preserve report/state/history paths and `run_all_scanners.ps1` wiring.
- Every new Markdown file must contain `SEBI registered`.
- Preserve the unrelated `.ohlc_data/data_manifest.csv` edit.

---

### Task 1: Slope-only signal, weekly age, and universe

**Files:**
- Modify: `tests/test_rs_weekly_ema9_scanner.py`
- Modify: `rs_weekly_ema9_scanner.py`

**Interfaces:**
- Consumes: `weekly_rs_ema9_trend(stock_close: pd.Series, bench_close: pd.Series) -> dict | None`
- Produces: the same dictionary keys, with `age` redefined as consecutive qualifying weekly transitions.

- [ ] **Step 1: Write failing tests**

Add tests that compute the expected weekly EMA9 slopes independently, assert `age` equals the trailing count of slopes `>= -SLOPE_EPS`, assert a currently falling series has age zero, inspect `analyse()` with a stock whose daily RS is below EMA9 but whose EMA9 is non-falling, and assert `MC_LOW == 1_000 * 1_00_00_000` plus `MC_HIGH == 5_00_000 * 1_00_00_000`.

- [ ] **Step 2: Verify RED**

Run: `python -m pytest tests/test_rs_weekly_ema9_scanner.py -v --basetemp=.pytest_tmp`

Expected: failures show the old daily-above age semantics, old analyse exclusion, and old market-cap constants.

- [ ] **Step 3: Implement the minimal behavior**

In `weekly_rs_ema9_trend()`, calculate:

```python
slopes = rs_ema9.diff().dropna()
age = 0
for weekly_slope in reversed(slopes.to_numpy()):
    if weekly_slope < -SLOPE_EPS:
        break
    age += 1
```

Keep `slope = float(slopes.iloc[-1])`. In `analyse()`, qualify solely with `trend is not None`, `slope >= -SLOPE_EPS`, and `age >= 1`. Set the constants to the EMA55 bounds. Update docstrings and module documentation.

- [ ] **Step 4: Verify GREEN**

Run: `python -m pytest tests/test_rs_weekly_ema9_scanner.py -v --basetemp=.pytest_tmp`

Expected: all focused tests pass.

---

### Task 2: Report contract, repo documentation, and production verification

**Files:**
- Modify: `tests/test_rs_weekly_ema9_scanner.py`
- Modify: `rs_weekly_ema9_scanner.py`
- Modify: `CLAUDE.md`
- Modify: `HANDOFF.md`
- Modify after live run: `rs_weekly_scans/rs_weekly_ema9_scans.md`
- Modify after live run: `rs_weekly_scans/rs_weekly_ema9_scans_2026-08-24.md`
- Modify after live run: `rs_weekly_scans/rs_weekly_ema9_state.json`
- Modify after live run: `rs_weekly_scans/rs_weekly_ema9_history.csv`
- Modify after live run: `dashboard/rs_weekly_ema9_history.html`

**Interfaces:**
- Consumes: findings with integer weekly `age`, `slope`, and `rising`.
- Produces: Markdown/HTML definitions that describe slope-only qualification and `Age(w)`.

- [ ] **Step 1: Add report-contract tests**

Call `build_markdown()` with a minimal finding and assert the output contains `weekly RS EMA9 flat or rising`, `Age(w)`, and `Rs1,000 Cr - Rs5 Lakh Cr`, while excluding claims that daily RS must be above EMA9.

- [ ] **Step 2: Verify RED, update copy, verify GREEN**

Run the focused test, update the Markdown table header, scan definition, dashboard subtitle, and sort/age labels, then rerun the focused test.

- [ ] **Step 3: Update operating documentation**

Revise the Weekly RS EMA9 section in `CLAUDE.md` and add a dated entry to `HANDOFF.md` documenting the new signal, weekly age, EMA55 market-cap range, verification, and output path.

- [ ] **Step 4: Run verification**

Run:

```powershell
python -m pytest tests/test_rs_weekly_ema9_scanner.py -v --basetemp=.pytest_tmp
python -m pytest --basetemp=.pytest_tmp
python rs_weekly_ema9_scanner.py
git diff --check -- rs_weekly_ema9_scanner.py tests/test_rs_weekly_ema9_scanner.py CLAUDE.md HANDOFF.md docs/superpowers/plans/2026-08-24-weekly-rs-ema9-slope-only.md rs_weekly_scans dashboard/rs_weekly_ema9_history.html
```

Expected: focused and full suites pass; the live scan completes and writes disclaimer-compliant latest/dated reports; scoped whitespace check passes.

- [ ] **Step 5: Publish only intended changes**

Commit the plan, code, tests, docs, and generated scanner artifacts with `git commit --no-verify`. Reconcile these commits onto current `origin/main` without staging `.ohlc_data/data_manifest.csv`, push `main`, and verify `git status -sb` plus `git rev-list --left-right --count HEAD...origin/main` reports zero ahead/behind for committed scope.

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
