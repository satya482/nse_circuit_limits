> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Daily ZLEMA25 With Weekly RS EMA9 Backtest Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and run a repeatable, no-look-ahead backtest that enters daily ZLEMA25 turn-ups under a rising weekly RS EMA9 and exits on the first ZLEMA25 downturn or loss of the weekly RS EMA9 rise.

**Architecture:** A single root-level backtest module follows the repository's flat-script convention while exposing pure indicator, simulation, statistics, and reporting functions for tests. It reads only through `ohlc_db.py`, reconstructs each partial week's EMA9 from information known on each daily date, and writes deterministic CSV plus disclaimer-compliant Markdown outputs.

**Tech Stack:** Python 3, pandas, argparse, pytest, local SQLite through `ohlc_db.py`, shared disclaimer constants from `disclaimer.py`.

## Global Constraints

- Initial symbols: `TRIVENI`, `CARTRADE`, `KIRLOSENG`.
- Inclusive entry period: `2021-08-20` through `2026-07-13`; pre-period data is warm-up only.
- Benchmark: `NIFTY MIDSML 400`.
- Daily ZLEMA25 formula: `2 * EMA(close, 25) - EMA(EMA(close, 25), 25)` using `ewm(span=25, adjust=False)`.
- Entry close: first strict daily ZLEMA25 turn-up with daily RS above weekly RS EMA9 and weekly RS EMA9 strictly rising.
- Exit close: first later daily bar where ZLEMA25 is strictly down or weekly RS EMA9 is no longer strictly rising.
- Daily RS falling below EMA9 after entry is not an exit.
- No network calls, database writes, slippage, brokerage, targets, stops, dividends, position sizing, or overlapping trades per stock.
- Open trades at the end date are reported but excluded from completed-trade statistics.
- Every new Markdown output must contain `SEBI registered` and use `SEBI_MD_HEADER` plus `SEBI_MD_FOOTER` when generated.
- Preserve unrelated changes in `.ohlc_data/data_manifest.csv` and `pine_scripts/Satya RS Relative Leadership.txt`.
- Use `git commit --no-verify` for every commit in this repository.

---

### Task 1: No-Look-Ahead Indicator Frame

**Files:**
- Create: `backtest_daily_zlema25_weekly_rs.py`
- Create: `tests/test_backtest_daily_zlema25_weekly_rs.py`

**Interfaces:**
- Consumes: daily stock and benchmark DataFrames with `date` and `close` columns.
- Produces: `zlema(close: pd.Series, period: int = 25) -> pd.Series` and `build_indicator_frame(stock_df: pd.DataFrame, benchmark_df: pd.DataFrame) -> pd.DataFrame`.
- `build_indicator_frame` returns `date`, `close`, `zlema25`, `daily_rs`, `weekly_rs_ema9`, `prior_week_rs_ema9`, `rs_above_ema9`, `rs_ema9_rising`, and `entry_signal`.

- [ ] **Step 1: Write failing ZLEMA and no-look-ahead tests**

Create synthetic business-day closes and assert the exact formula plus invariance of earlier same-week rows:

```python
import pandas as pd
from pandas.testing import assert_series_equal

import backtest_daily_zlema25_weekly_rs as m


def _ohlc(closes, start="2024-01-01"):
    dates = pd.bdate_range(start, periods=len(closes))
    return pd.DataFrame({"date": dates, "close": closes})


def test_zlema_matches_double_ema_formula():
    close = pd.Series([100.0 + i for i in range(40)])
    ema = close.ewm(span=25, adjust=False).mean()
    expected = 2 * ema - ema.ewm(span=25, adjust=False).mean()
    assert_series_equal(m.zlema(close), expected)


def test_weekly_rs_ema_does_not_look_ahead_within_week():
    stock = _ohlc([100.0 + i for i in range(70)])
    bench = _ohlc([200.0 + i * 0.2 for i in range(70)])
    cutoff = stock.loc[62, "date"]
    early = m.build_indicator_frame(stock.iloc[:63], bench.iloc[:63])
    full = m.build_indicator_frame(stock, bench)
    cols = ["weekly_rs_ema9", "prior_week_rs_ema9", "rs_ema9_rising"]
    pd.testing.assert_frame_equal(
        early.set_index("date")[cols],
        full.loc[full["date"] <= cutoff].set_index("date")[cols],
    )


def test_entry_signal_requires_all_four_conditions():
    stock = _ohlc([100 + i * 0.2 + (2 if i % 9 == 0 else 0) for i in range(90)])
    bench = _ohlc([200 + i * 0.05 for i in range(90)])
    frame = m.build_indicator_frame(stock, bench)
    expected = (
        (frame["zlema25"] > frame["zlema25"].shift(1))
        & (frame["zlema25"].shift(1) <= frame["zlema25"].shift(2))
        & frame["rs_above_ema9"]
        & frame["rs_ema9_rising"]
        & (frame.index >= 24)
    )
    pd.testing.assert_series_equal(frame["entry_signal"], expected, check_names=False)
```

- [ ] **Step 2: Run the focused tests and verify they fail**

Run: `python -m pytest tests/test_backtest_daily_zlema25_weekly_rs.py -v --basetemp=.pytest_tmp`

Expected: collection fails with `ModuleNotFoundError: No module named 'backtest_daily_zlema25_weekly_rs'`.

- [ ] **Step 3: Implement ZLEMA and walk-forward weekly RS EMA9**

Create the module imports/constants and implement the indicator functions. The weekly loop must preserve the previous completed week's EMA state and recompute the current partial observation from that state on every day:

```python
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from disclaimer import SEBI_MD_FOOTER, SEBI_MD_HEADER
from ohlc_db import load_ohlc

BENCHMARK = "NIFTY MIDSML 400"
ZLEMA_PERIOD = 25
RS_EMA_PERIOD = 9
MIN_DAILY_BARS = 25
MIN_WEEKLY_BARS = 9


def zlema(close: pd.Series, period: int = ZLEMA_PERIOD) -> pd.Series:
    first = close.astype(float).ewm(span=period, adjust=False).mean()
    return 2 * first - first.ewm(span=period, adjust=False).mean()


def _walk_forward_weekly_ema(daily_rs: pd.Series, period: int = RS_EMA_PERIOD) -> pd.DataFrame:
    alpha = 2.0 / (period + 1.0)
    current_ema = np.nan
    completed_weeks = 0
    rows = []
    for _, week in daily_rs.groupby(daily_rs.index.to_period("W-SUN"), sort=True):
        prior_ema = current_ema
        for date, value in week.items():
            partial_ema = float(value) if pd.isna(prior_ema) else alpha * float(value) + (1 - alpha) * prior_ema
            ready = completed_weeks + 1 >= MIN_WEEKLY_BARS and not pd.isna(prior_ema)
            rows.append((date, partial_ema if ready else np.nan, prior_ema if ready else np.nan))
        final_value = float(week.iloc[-1])
        current_ema = final_value if pd.isna(prior_ema) else alpha * final_value + (1 - alpha) * prior_ema
        completed_weeks += 1
    return pd.DataFrame(rows, columns=["date", "weekly_rs_ema9", "prior_week_rs_ema9"]).set_index("date")


def build_indicator_frame(stock_df: pd.DataFrame, benchmark_df: pd.DataFrame) -> pd.DataFrame:
    stock = stock_df[["date", "close"]].copy()
    bench = benchmark_df[["date", "close"]].copy()
    stock["date"] = pd.to_datetime(stock["date"])
    bench["date"] = pd.to_datetime(bench["date"])
    merged = stock.merge(bench, on="date", suffixes=("", "_benchmark"), how="inner").sort_values("date")
    merged = merged.drop_duplicates("date").reset_index(drop=True)
    merged["zlema25"] = zlema(merged["close"])
    merged["daily_rs"] = merged["close"] / merged["close_benchmark"] * 1000.0
    rs = merged.set_index("date")["daily_rs"]
    weekly = _walk_forward_weekly_ema(rs)
    merged = merged.join(weekly, on="date")
    merged["rs_above_ema9"] = merged["daily_rs"] > merged["weekly_rs_ema9"]
    merged["rs_ema9_rising"] = merged["weekly_rs_ema9"] > merged["prior_week_rs_ema9"]
    zl_up = merged["zlema25"] > merged["zlema25"].shift(1)
    zl_was_not_up = merged["zlema25"].shift(1) <= merged["zlema25"].shift(2)
    enough_daily = pd.Series(merged.index >= MIN_DAILY_BARS - 1, index=merged.index)
    merged["entry_signal"] = enough_daily & zl_up & zl_was_not_up & merged["rs_above_ema9"] & merged["rs_ema9_rising"]
    return merged[["date", "close", "zlema25", "daily_rs", "weekly_rs_ema9", "prior_week_rs_ema9", "rs_above_ema9", "rs_ema9_rising", "entry_signal"]]
```

- [ ] **Step 4: Run the tests and verify they pass**

Run: `python -m pytest tests/test_backtest_daily_zlema25_weekly_rs.py -v --basetemp=.pytest_tmp`

Expected: both tests pass.

- [ ] **Step 5: Commit the indicator slice**

```powershell
git add -- backtest_daily_zlema25_weekly_rs.py tests/test_backtest_daily_zlema25_weekly_rs.py
git commit --no-verify -m "feat: add no-look-ahead ZLEMA RS indicators"
```

### Task 2: Trade Simulation and Summary Statistics

**Files:**
- Modify: `backtest_daily_zlema25_weekly_rs.py`
- Modify: `tests/test_backtest_daily_zlema25_weekly_rs.py`

**Interfaces:**
- Consumes: the indicator frame produced by `build_indicator_frame`.
- Produces: `simulate_stock(symbol: str, frame: pd.DataFrame, start: pd.Timestamp, end: pd.Timestamp) -> tuple[pd.DataFrame, pd.DataFrame]` and `summarize_trades(trades: pd.DataFrame, symbols: list[str]) -> pd.DataFrame`.
- Completed trade columns: `symbol`, `entry_date`, `entry_close`, `exit_date`, `exit_close`, `return_pct`, `holding_trading_days`, `holding_calendar_days`, `exit_reason`.
- Open trade columns: `symbol`, `entry_date`, `entry_close`, `last_date`, `last_close`, `unrealized_return_pct`, `holding_trading_days`, `holding_calendar_days`.

- [ ] **Step 1: Add failing simulation tests with hand-built indicator frames**

```python
def _signal_frame():
    dates = pd.bdate_range("2024-03-01", periods=6)
    return pd.DataFrame({
        "date": dates,
        "close": [100.0, 102.0, 105.0, 104.0, 103.0, 106.0],
        "zlema25": [100.0, 99.0, 100.0, 101.0, 100.5, 101.0],
        "rs_ema9_rising": [True, True, True, True, True, False],
        "entry_signal": [False, False, True, False, False, False],
    })


def test_simulation_exits_on_first_zlema_down_close():
    completed, opened = m.simulate_stock(
        "TEST", _signal_frame(), pd.Timestamp("2024-03-01"), pd.Timestamp("2024-03-31")
    )
    assert opened.empty
    trade = completed.iloc[0]
    assert trade["entry_close"] == 105.0
    assert trade["exit_close"] == 103.0
    assert trade["exit_reason"] == "ZLEMA_DOWN"
    assert trade["holding_trading_days"] == 2


def test_open_trade_is_not_in_completed_trades():
    frame = _signal_frame().iloc[:4].copy()
    completed, opened = m.simulate_stock(
        "TEST", frame, pd.Timestamp("2024-03-01"), pd.Timestamp("2024-03-31")
    )
    assert completed.empty
    assert len(opened) == 1


def test_simulation_records_rs_only_and_combined_exit_reasons():
    rs_only = _signal_frame()
    rs_only.loc[3, "rs_ema9_rising"] = False
    completed, _ = m.simulate_stock(
        "TEST", rs_only, pd.Timestamp("2024-03-01"), pd.Timestamp("2024-03-31")
    )
    assert completed.iloc[0]["exit_reason"] == "RS_NOT_RISING"

    combined = _signal_frame()
    combined.loc[3, "zlema25"] = 99.0
    combined.loc[3, "rs_ema9_rising"] = False
    completed, _ = m.simulate_stock(
        "TEST", combined, pd.Timestamp("2024-03-01"), pd.Timestamp("2024-03-31")
    )
    assert completed.iloc[0]["exit_reason"] == "ZLEMA_AND_RS"


def test_summary_counts_wins_zeros_and_compounds():
    trades = pd.DataFrame({
        "symbol": ["A", "A", "A"],
        "return_pct": [10.0, -5.0, 0.0],
        "holding_trading_days": [2, 4, 3],
    })
    row = m.summarize_trades(trades, ["A"]).set_index("symbol").loc["A"]
    assert row["wins"] == 1
    assert row["losses"] == 1
    assert row["zeros"] == 1
    assert row["win_rate_pct"] == pytest.approx(100 / 3)
    assert row["compounded_return_pct"] == pytest.approx(4.5)
```

Also import `pytest` at the top of the test file.

- [ ] **Step 2: Run the new tests and verify they fail**

Run: `python -m pytest tests/test_backtest_daily_zlema25_weekly_rs.py -v --basetemp=.pytest_tmp`

Expected: failures report missing `simulate_stock` and `summarize_trades`.

- [ ] **Step 3: Implement deterministic trade simulation**

Add column constants and the simulator. Iterate only through rows up to the inclusive end date, allow entry only on/after start, evaluate exits only on rows after entry, and choose the combined reason when both conditions fail:

```python
TRADE_COLUMNS = ["symbol", "entry_date", "entry_close", "exit_date", "exit_close", "return_pct", "holding_trading_days", "holding_calendar_days", "exit_reason"]
OPEN_COLUMNS = ["symbol", "entry_date", "entry_close", "last_date", "last_close", "unrealized_return_pct", "holding_trading_days", "holding_calendar_days"]


def simulate_stock(symbol, frame, start, end):
    data = frame.loc[frame["date"] <= end].reset_index(drop=True)
    completed, opened, position = [], [], None
    for i, row in data.iterrows():
        if position is None:
            if row["date"] >= start and bool(row["entry_signal"]):
                position = {"entry_i": i, "entry_date": row["date"], "entry_close": float(row["close"])}
            continue
        zl_down = bool(row["zlema25"] < data.at[i - 1, "zlema25"])
        rs_stopped = not bool(row["rs_ema9_rising"])
        if zl_down or rs_stopped:
            reason = "ZLEMA_AND_RS" if zl_down and rs_stopped else ("ZLEMA_DOWN" if zl_down else "RS_NOT_RISING")
            ret = (float(row["close"]) / position["entry_close"] - 1.0) * 100.0
            completed.append({"symbol": symbol, **position, "exit_date": row["date"], "exit_close": float(row["close"]), "return_pct": ret, "holding_trading_days": i - position["entry_i"], "holding_calendar_days": (row["date"] - position["entry_date"]).days, "exit_reason": reason})
            completed[-1].pop("entry_i")
            position = None
    if position is not None and not data.empty:
        last = data.iloc[-1]
        opened.append({"symbol": symbol, "entry_date": position["entry_date"], "entry_close": position["entry_close"], "last_date": last["date"], "last_close": float(last["close"]), "unrealized_return_pct": (float(last["close"]) / position["entry_close"] - 1.0) * 100.0, "holding_trading_days": len(data) - 1 - position["entry_i"], "holding_calendar_days": (last["date"] - position["entry_date"]).days})
    return pd.DataFrame(completed, columns=TRADE_COLUMNS), pd.DataFrame(opened, columns=OPEN_COLUMNS)
```

- [ ] **Step 4: Implement per-stock and combined statistics**

`summarize_trades` must emit one row for every requested symbol plus `COMBINED`. For zero-trade groups, counts are zero and return metrics are `np.nan`. For nonempty groups calculate wins with `return_pct > 0`, losses with `< 0`, zeros with `== 0`, win rate over all completed trades, mean, median, product compounding, extrema, and average holding days.

```python
SUMMARY_COLUMNS = ["symbol", "trades", "wins", "losses", "zeros", "win_rate_pct", "average_return_pct", "median_return_pct", "compounded_return_pct", "best_return_pct", "worst_return_pct", "average_holding_days"]


def summarize_trades(trades, symbols):
    rows = []
    for symbol in [*symbols, "COMBINED"]:
        group = trades if symbol == "COMBINED" else trades.loc[trades["symbol"] == symbol]
        n = len(group)
        returns = group["return_pct"].astype(float) if n else pd.Series(dtype=float)
        rows.append({
            "symbol": symbol, "trades": n,
            "wins": int((returns > 0).sum()), "losses": int((returns < 0).sum()), "zeros": int((returns == 0).sum()),
            "win_rate_pct": float((returns > 0).mean() * 100) if n else np.nan,
            "average_return_pct": float(returns.mean()) if n else np.nan,
            "median_return_pct": float(returns.median()) if n else np.nan,
            "compounded_return_pct": float(((1 + returns / 100).prod() - 1) * 100) if n else np.nan,
            "best_return_pct": float(returns.max()) if n else np.nan,
            "worst_return_pct": float(returns.min()) if n else np.nan,
            "average_holding_days": float(group["holding_trading_days"].mean()) if n else np.nan,
        })
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)
```

- [ ] **Step 5: Run the focused test file**

Run: `python -m pytest tests/test_backtest_daily_zlema25_weekly_rs.py -v --basetemp=.pytest_tmp`

Expected: all indicator, simulation, and statistics tests pass.

- [ ] **Step 6: Commit simulation and statistics**

```powershell
git add -- backtest_daily_zlema25_weekly_rs.py tests/test_backtest_daily_zlema25_weekly_rs.py
git commit --no-verify -m "feat: simulate ZLEMA RS trades"
```

### Task 3: CLI, CSV, and Disclaimer-Compliant Markdown

**Files:**
- Modify: `backtest_daily_zlema25_weekly_rs.py`
- Modify: `tests/test_backtest_daily_zlema25_weekly_rs.py`

**Interfaces:**
- Consumes: `build_indicator_frame`, `simulate_stock`, `summarize_trades`, and `load_ohlc`.
- Produces: `run_backtest(symbols: list[str], start: pd.Timestamp, end: pd.Timestamp) -> dict`, `build_markdown(result: dict) -> str`, `write_outputs(result: dict, output_dir: Path) -> tuple[Path, Path, Path]`, and CLI `main() -> int`.
- Result dictionary keys: `symbols`, `start`, `end`, `trades`, `open_trades`, `summary`, `skipped`.

- [ ] **Step 1: Add failing orchestration and Markdown tests**

Use monkeypatch to avoid SQLite and verify missing-stock reporting, filenames, and disclaimer:

```python
def test_build_markdown_has_disclaimer_and_open_section():
    result = {
        "symbols": ["TEST"], "start": pd.Timestamp("2024-01-01"), "end": pd.Timestamp("2024-12-31"),
        "trades": pd.DataFrame(columns=m.TRADE_COLUMNS),
        "open_trades": pd.DataFrame(columns=m.OPEN_COLUMNS),
        "summary": m.summarize_trades(pd.DataFrame(columns=m.TRADE_COLUMNS), ["TEST"]),
        "skipped": [],
    }
    text = m.build_markdown(result)
    assert "SEBI registered" in text
    assert "Open Trades" in text
    assert "TEST" in text


def test_write_outputs_always_writes_csv_headers(tmp_path):
    result = {
        "symbols": ["TEST"], "start": pd.Timestamp("2024-01-01"), "end": pd.Timestamp("2024-12-31"),
        "trades": pd.DataFrame(columns=m.TRADE_COLUMNS),
        "open_trades": pd.DataFrame(columns=m.OPEN_COLUMNS),
        "summary": m.summarize_trades(pd.DataFrame(columns=m.TRADE_COLUMNS), ["TEST"]),
        "skipped": [],
    }
    trades_path, open_path, report_path = m.write_outputs(result, tmp_path)
    assert trades_path.read_text(encoding="utf-8").startswith("symbol,entry_date")
    assert open_path.read_text(encoding="utf-8").startswith("symbol,entry_date")
    assert "SEBI registered" in report_path.read_text(encoding="utf-8")


def test_run_backtest_rejects_backwards_dates():
    with pytest.raises(ValueError, match="start date"):
        m.run_backtest(["TEST"], pd.Timestamp("2024-02-01"), pd.Timestamp("2024-01-01"))


def test_run_backtest_reports_missing_stock(monkeypatch):
    benchmark = _ohlc([200.0 + i for i in range(80)])
    monkeypatch.setattr(
        m,
        "load_ohlc",
        lambda symbol, lookback=10000: benchmark if symbol == m.BENCHMARK else None,
    )
    result = m.run_backtest(
        ["MISSING"], pd.Timestamp("2024-01-01"), pd.Timestamp("2024-12-31")
    )
    assert result["skipped"] == [{"symbol": "MISSING", "reason": "OHLC data unavailable"}]
```

- [ ] **Step 2: Run the new tests and verify they fail**

Run: `python -m pytest tests/test_backtest_daily_zlema25_weekly_rs.py -v --basetemp=.pytest_tmp`

Expected: failures report missing `build_markdown` and `write_outputs`.

- [ ] **Step 3: Implement orchestration and validation**

`run_backtest` must load the benchmark with `lookback=10000`, raise `ValueError` when it is absent, load each symbol with the same lookback, append `{symbol, reason}` to `skipped` for missing/insufficient data, build/simulate valid symbols, concatenate frames with declared columns, and summarize all requested symbols. Reject `start > end` before loading.

Use this CLI contract:

```python
def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Backtest daily ZLEMA25 turns with weekly RS EMA9")
    parser.add_argument("symbols", nargs="+", help="NSE symbols, for example TRIVENI CARTRADE KIRLOSENG")
    parser.add_argument("--start", required=True, type=pd.Timestamp)
    parser.add_argument("--end", required=True, type=pd.Timestamp)
    parser.add_argument("--output-dir", type=Path, default=Path("backtest_results"))
    return parser.parse_args(argv)
```

- [ ] **Step 4: Implement Markdown and deterministic output writers**

`build_markdown` must concatenate `SEBI_MD_HEADER`, a title and method block, summary table, skipped-symbol section, completed trade table, open-trade table, combined-compounding caveat, and `SEBI_MD_FOOTER`. Format dates as `YYYY-MM-DD`, percentage values with two decimals, and missing metrics as `N/A`. `write_outputs` creates the output directory and writes these exact paths:

```python
trades_path = output_dir / "daily_zlema25_weekly_rs_trades.csv"
open_path = output_dir / "daily_zlema25_weekly_rs_open.csv"
report_path = output_dir / "daily_zlema25_weekly_rs_summary.md"
```

Call `to_csv(index=False, date_format="%Y-%m-%d")` for both CSVs and `report_path.write_text(build_markdown(result), encoding="utf-8")` for Markdown.

`main` parses arguments, uppercases and de-duplicates symbols while retaining order, runs the backtest, writes outputs, prints the three paths plus combined trade count/win rate, and returns zero. Convert validation errors into a concise stderr message and return code 2.

- [ ] **Step 5: Run focused tests and CLI help**

Run: `python -m pytest tests/test_backtest_daily_zlema25_weekly_rs.py -v --basetemp=.pytest_tmp`

Expected: all tests pass.

Run: `python backtest_daily_zlema25_weekly_rs.py --help`

Expected: usage lists positional `symbols` and required `--start`, `--end`.

- [ ] **Step 6: Commit CLI and reporting**

```powershell
git add -- backtest_daily_zlema25_weekly_rs.py tests/test_backtest_daily_zlema25_weekly_rs.py
git commit --no-verify -m "feat: report daily ZLEMA RS backtest"
```

### Task 4: Run the Three-Stock Backtest and Update Handoff

**Files:**
- Create: `backtest_results/daily_zlema25_weekly_rs_trades.csv`
- Create: `backtest_results/daily_zlema25_weekly_rs_open.csv`
- Create: `backtest_results/daily_zlema25_weekly_rs_summary.md`
- Modify: `HANDOFF.md`

**Interfaces:**
- Consumes: the completed CLI from Task 3 and local OHLC data.
- Produces: verified results for TRIVENI, CARTRADE, and KIRLOSENG plus takeover documentation.

- [ ] **Step 1: Recheck shared-worktree state and target diffs**

Run: `git status --short`

Expected: unrelated manifest/Pine modifications may remain; no unreviewed modifications to the backtest files.

Run: `git diff -- HANDOFF.md`

Expected: inspect any concurrent handoff edits before patching; do not overwrite them.

- [ ] **Step 2: Execute the approved backtest**

Run:

```powershell
python backtest_daily_zlema25_weekly_rs.py TRIVENI CARTRADE KIRLOSENG --start 2021-08-20 --end 2026-07-13
```

Expected: exit code 0, three output paths printed, and a combined completed-trade count/win rate.

- [ ] **Step 3: Verify generated files and numerical consistency**

Run:

```powershell
rg -n "SEBI registered|TRIVENI|CARTRADE|KIRLOSENG|COMBINED" backtest_results/daily_zlema25_weekly_rs_summary.md
python -c "import pandas as pd; t=pd.read_csv(r'backtest_results/daily_zlema25_weekly_rs_trades.csv'); o=pd.read_csv(r'backtest_results/daily_zlema25_weekly_rs_open.csv'); assert set(t.symbol).issubset({'TRIVENI','CARTRADE','KIRLOSENG'}); assert (t.return_pct.round(8)==((t.exit_close/t.entry_close-1)*100).round(8)).all(); assert (t.holding_trading_days>=1).all(); print('completed',len(t),'open',len(o),'wins',int((t.return_pct>0).sum()),'win_rate',round((t.return_pct>0).mean()*100,2) if len(t) else 'N/A')"
```

Expected: disclaimer and all summary labels are found; assertions pass; printed counts match the Markdown combined row.

- [ ] **Step 4: Run focused and broader regression tests**

Run: `python -m pytest tests/test_backtest_daily_zlema25_weekly_rs.py -v --basetemp=.pytest_tmp`

Expected: all focused tests pass.

Run: `python -m pytest --basetemp=.pytest_tmp`

Expected: full suite passes. If an unrelated pre-existing failure occurs, capture the exact test/error and confirm the focused suite remains green before handoff.

- [ ] **Step 5: Update `HANDOFF.md` without replacing concurrent content**

Under `Current Worktree State`, add a dated Codex entry containing:

```markdown
Updated 2026-07-13 by Codex, daily ZLEMA25 + weekly RS EMA9 backtest:

- Added `backtest_daily_zlema25_weekly_rs.py`, a no-look-ahead local-OHLC backtest using `NIFTY MIDSML 400` as benchmark.
- Entry: first daily ZLEMA25 turn-up while daily RS is above a rising partial-week RS EMA9. Exit: first daily ZLEMA25 downturn or weekly RS EMA9 no longer rising, at close.
- Initial run covers TRIVENI, CARTRADE, and KIRLOSENG from 2021-08-20 through 2026-07-13.
- Outputs: `backtest_results/daily_zlema25_weekly_rs_trades.csv`, `daily_zlema25_weekly_rs_open.csv`, and disclaimer-compliant `daily_zlema25_weekly_rs_summary.md`.
- Re-run: `python backtest_daily_zlema25_weekly_rs.py TRIVENI CARTRADE KIRLOSENG --start 2021-08-20 --end 2026-07-13`.
```

- [ ] **Step 6: Check final scope and commit only backtest artifacts**

Run: `git diff --check`

Expected: no whitespace errors in files created or modified by this plan.

Run: `git status --short`

Expected: the three generated results and `HANDOFF.md` are the only uncommitted plan files; unrelated manifest/Pine modifications remain unstaged.

```powershell
git add -- HANDOFF.md backtest_results/daily_zlema25_weekly_rs_trades.csv backtest_results/daily_zlema25_weekly_rs_open.csv backtest_results/daily_zlema25_weekly_rs_summary.md
git commit --no-verify -m "docs: record daily ZLEMA RS backtest results"
```

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
