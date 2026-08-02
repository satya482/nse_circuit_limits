# Minervini Trend Template Scanner — Design

Date: 2026-08-02

## Purpose

New scanner implementing Mark Minervini's Trend Template: a strict, all-must-pass
gate identifying stocks in a confirmed Stage 2 uptrend. Adds to the existing
scanner suite as a distinct signal source (dashboard-crossable via symbol overlap
with other scans, same as wt_bullcross / rs_leadership / consolidation).

## File layout

- `minervini_trend_scanner.py` — root-level, new file
- `minervini_scans/` — output dir
  - `minervini_trend_latest.md`
  - `minervini_trend_YYYY-MM-DD.md`
- `run_minervini_trend_scanner.ps1` — PowerShell runner, logs to `logs/`

## Universe

Reuses `ema25_zl_scanner.get_watchlist()` — no new TradingView query. Same filter
as `ema55_cross_scanner.py`:
- NSE common equity
- MCap ₹1,000 Cr – ₹5 Lakh Cr
- price > ₹50
- Float hard-gate applied (`float_gate.passes_hard_gate`) — illiquid/trap names
  dropped before scoring, consistent with `ema25_zl_scanner.py` / `ema55_cross_scanner.py`.

## Data

`ohlc_db.load_ohlc(symbol, lookback=400)` per symbol (400 daily bars covers the
252-trading-day 52-week window plus SMA200 warmup with margin). Benchmark
`NIFTY MIDSML 400` loaded once via `load_ohlc_many([BENCH_SYM])`, same as other
RS-gated scanners.

## Criteria (strict AND-gate — all must pass)

All computed off daily close (`close = df["close"].astype(float)`), SMA = plain
rolling mean (`close.rolling(n).mean()`), consistent with repo's SMA convention
(EMA compression scanner uses SMA for BB/KC; this scanner uses SMA per Minervini's
original template, not EMA).

1. `close[-1] > SMA150[-1]`
2. `close[-1] > SMA200[-1]`
3. `SMA150[-1] > SMA200[-1]`
4. SMA200 trending up at least 1 month: `SMA200[-1] > SMA200[-21]` (21 trading
   days back — approximates 1 calendar month, matches `ZL_TURN_CAP`-style
   trading-day convention used elsewhere in repo, not calendar days)
5. `SMA50[-1] > SMA150[-1] AND SMA50[-1] > SMA200[-1]`
6. `close[-1] > SMA50[-1]`
7. `close[-1] >= 1.30 * min(close[-252:])` — at least 30% above 52-week low
8. `close[-1] >= 0.75 * max(close[-252:])` — within 25% of 52-week high
9. RS strength: `_weekly_rs_gate(rs, c_rs, idx_rs)` — reused verbatim from
   `ema25_zl_scanner.py` (daily RS line > weekly RS EMA9 AND weekly RS EMA9
   rising week-over-week; `rs = close/NIFTY_MIDSML_400 * 1000`). This is a
   deliberate substitution for IBD's percentile RS Rating (>=70) — repo has no
   percentile-rank infrastructure; RS-vs-benchmark trend gate is the existing,
   proven proxy used across `ema25_zl_scanner.py`, `wt_bullcross_scanner.py`,
   `rs_weekly_ema9_scanner.py`.

Symbol needs minimum ~260 bars of history to be evaluated (252 for 52wk window +
buffer); shorter history = skip, not fail.

A stock qualifies only if all 9 checks are true. No partial/scored output —
binary qualify list per explicit user decision (matches Minervini's original
template intent: a stock either is or isn't in a confirmed Stage 2 uptrend).

## Output

`minervini_scans/minervini_trend_latest.md` + dated
`minervini_scans/minervini_trend_YYYY-MM-DD.md`, written atomically together.
SEBI disclaimer (`disclaimer.SEBI_MD_HEADER` / `SEBI_MD_FOOTER`) prepended/appended.

Table columns:

| Symbol | Close | %off 52wk-high | %above 52wk-low | SMA stack | RS gate | Day chg% |
|--------|-------|-----------------|-------------------|-----------|---------|----------|

- Symbol: `[SYM](tradingview link)`, same link format as other scanners
- SMA stack: ✓ (always ✓ since all 9 criteria are gate conditions — column exists
  for scanability/consistency with other scanners' tag columns)
- RS gate: 📶 (always shown, same reasoning)
- Sorted by `%off 52wk-high` ascending (closest to high = freshest breakout
  candidate, sorted first)

If zero qualifiers: write `*No signals.*` section, not an empty file (per
`backtesting-integrity.md` scanner output integrity rule).

## Scheduling

New `run_minervini_trend_scanner.ps1`, structurally mirrors
`run_ema55_cross_scanner.ps1` (kite auth check → python script → git add/commit
→ push, logs to `logs/`). Suggested slot: 4:30 PM group, after the RS-gated
scanners (`run_rs_leadership_scanner.ps1`, `run_rs_highline_scanner.ps1`) since
it shares the same RS gate function and benchmark load pattern — no dependency
on delivery% data, so no ordering constraint there.

CLAUDE.md updates required:
- Add to root run-scripts table (after `run_rs_leadership_scanner.ps1` line)
- Add `### Scanner pipeline — Minervini Trend Template` architecture section
- Add output file row to the "Output files (git-tracked)" table

## Out of scope

- Percentile RS Rating (IBD-style, requires cross-sectional ranking
  infrastructure not yet in repo) — explicitly deferred, RS-vs-benchmark trend
  gate substituted per design decision above.
- Dashboard integration (cross-referencing with `dashboard_generator.py`) — not
  requested, can follow as a separate task once this scanner has run and its
  output format is confirmed against real data.
- Scored/partial-pass variant — explicitly rejected in favor of strict gate.

## Addendum (2026-08-02): Age + additions/deletions

Added after the first live run, same design session.

**Age** — consecutive trading days ALL 9 checks (8 SMA/52wk + RS gate) have
held true together, walking backward from today. Computed by vectorizing the
per-bar check math (`_checks_series()`, `_sma_pass_series()`,
`_rs_pass_series()`) across the full close history instead of just
`.iloc[-1]`, then doing the same backward-walk-count loop
`rs_weekly_ema9_scanner.weekly_rs_ema9_trend()` uses for its own age field.
No state file needed — self-contained per run. Capped at `AGE_CAP = 400` bars
(matches `load_ohlc()`'s default lookback, so age can never claim more history
than was actually loaded). `trend_template_checks()` is now implemented as
`{k: bool(v.iloc[-1]) for k, v in _checks_series(close).items()}` so the
single-day and whole-history code paths can't drift apart.

**Additions/deletions** — new `minervini_scans/minervini_trend_state.json`
persists today's qualifying symbol set (mirrors
`rs_weekly_ema9_scanner.py`'s `load_previous()`/`save_current()`). Rendered as
one table with two side-by-side columns (`| Additions | Deletions |`) at the
top of the output file, right after the generated-timestamp line and before
the scan-definition table. Shorter column blank-padded; both-empty shows
`*(none)* | *(none)*` rather than omitting the table.

Output table gained one column: `Age` (right after `%above 52wk-low`).

**2026-08-02, later same day:** sort order changed from `%off 52wk-high`
descending to `Age` ascending (newest entries into the trend first) —
explicit user request.
