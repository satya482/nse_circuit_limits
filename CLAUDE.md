# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Git commits — pre-commit hooks disabled

Pre-commit is configured (`.pre-commit-config.yaml`: black, ruff, detect-secrets) but user has
disabled it for this repo — it hangs/is too slow in practice. **Always commit with `git commit --no-verify`
here.** This is an explicit, standing exception to the default "never skip hooks" rule — it applies to
this repo only, not others.

## PowerShell scripts — ASCII only, no em dashes/curly quotes in strings

Windows PowerShell 5.1 reads a `.ps1` file via the system codepage (Windows-1252) unless it has a
UTF-8 BOM. This repo's `.ps1` files are plain UTF-8 **without** a BOM. A non-ASCII character
(em dash `—`, curly quotes, etc.) inside a real string literal gets mis-decoded and corrupts the
tokenizer's quote tracking — the whole script then fails to parse. Failure mode is silent: the
scheduled task just shows `LastTaskResult` non-zero, the script's own log file is never even
created (the parse error happens before the first line runs), and nothing posts to Discord.
Comments (`# ...`) are safe; string literals are not.

- Use plain ASCII (`-`, not `—`) in any string embedded in a `.ps1` file.
- Before committing a `.ps1` change, run `tools\check_ps1_syntax.ps1` — parses every `.ps1` in the
  repo and reports line/column of any syntax error. Catches this class of bug in seconds.
- Root cause + incident: 2026-07-08, both `run_breadth_monitor.ps1` and
  `run_institutional_footprint_scanner.ps1` silently no-op'd for a full day because commit
  `be74fb0` added an em dash to a Discord alert message string in both files.

## SEBI Disclaimer — mandatory on every output file

Every `.md` and `.html` file generated or created in this repo **must** include the SEBI disclaimer.
Use the shared constants from `disclaimer.py`:

```python
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER        # for .md generators
from disclaimer import SEBI_HTML_BANNER, SEBI_HTML_FOOTER     # for HTML generators
```

- **Markdown:** prepend `SEBI_MD_HEADER` at top, append `SEBI_MD_FOOTER` at bottom.
- **HTML:** inject `SEBI_HTML_BANNER` after `<body>` (or top of content), `SEBI_HTML_FOOTER` before `</body>`.
- New scanner or report file → add both. No exceptions.
- Check: if a generated file lacks the disclaimer string `"SEBI registered"`, it is non-compliant.

## Running the scanners

All scanners are triggered by PowerShell scripts that log to `logs/` and auto-commit results:

```powershell
.\run_fetch_data.ps1          # 4:05 PM — Kite auth + SQLite backfill/delta + manifest commit (EQ+indices only)
.\run_dashboard.ps1           # 4:10 PM — circuit limits dashboard (main.py)
.\run_daily_gainers_brief.ps1 # 4:15 PM — daily top-gainers HTML brief
.\run_ema25_zl_scanner.ps1   # 4:25 PM — EMA25 ZL scanner
.\run_nifty50_zlema25_scanner.ps1  # NIFTY 50 daily ZLEMA25 up/down trend age scanner
.\run_momentum_scanner.ps1    # momentum scanner
.\ema-compression-scanner\run_scanner.ps1  # 4:35 PM — EMA compression scanner
.\run_wt_bullcross_scanner.ps1  # 4:30 PM — WaveTrend bull cross scanner
.\run_rs_highline_scanner.ps1    # 4:30 PM — RS high-line cross scanner
.\run_rs_leadership_scanner.ps1  # 4:30 PM — RS leadership combined-cross scanner (RelPerf%+EMA)
.\run_minervini_trend_scanner.ps1  # 4:30 PM — Minervini Trend Template scanner (strict SMA50/150/200 + 52wk + RS gate)
.\run_trend_scanner.ps1         # 4:35 PM — Trend scanner: leaders in pullbacks (must run BEFORE EMA55_Cross, see below)
.\run_ema55_cross_scanner.ps1  # ~4:32 PM — runs AFTER MinerviniTrend and TrendScanner (moved, was 4:28 PM before EMA25/Minervini)
                                 #   so it can build the union watchlist below; close within -10% to +20% of EMA55
.\run_union_chart_dashboard.ps1  # ~4:32 PM -- runs AFTER EMA55_Cross (needs its union watchlist)
                                   #   interactive candlestick+volume charts for every union symbol
.\run_fetch_delivery.ps1        # 6:15 PM — NSE bhavcopy delivery% fetch + same-day marker backfill
                                 #   -> trailing: run_institutional_footprint_scanner.ps1 (needs today's delivery%)
.\run_wt_squeeze_dashboard.ps1  # 4:40 PM — WT + Squeeze combined dashboard (after both above)
.\run_rs_weekly_ema9_scanner.ps1  # runs in NSE_AllScanners, after WeeklyZL — weekly RS EMA9 flat/rising trend list
.\run_consolidation_scanner.ps1  # 4:35 PM — Consolidation Tracker: quality/imminence/tier scan
# US WaveTrend Bull Cross Scanner — SEPARATE scheduled task, part of the existing
# US scanner group (not run_all_scanners.ps1): fetch @4:40PM -> zl-squeeze @4:50PM -> this @5:00PM
.\run_us_wt_bullcross_scanner.ps1

# Breadth Monitor — SEPARATE scheduled task (NSE_BreadthMonitor), NOT part of NSE_AllScanners
# Triggered by run_all_scanners.ps1 via Start-ScheduledTask at end (no wait, separate log)
# Fallback: 5:30 PM scheduled trigger if AllScanners didn't run
# Self-contained: kite_auth + fetch_data.py --all + breadth_monitor.py + commit
.\run_breadth_monitor.ps1       # fires after AllScanners (or 5:30 PM fallback)
                                 #   -> trailing: run_bounce_rs_scanner.ps1, then re-run_wt_squeeze_dashboard.ps1
```

**Weekly (manual, Monday AM before market open):**
```powershell
python scripts/refresh_breadth_universe.py   # Refresh broad NSE EQ universe (~2000 stocks)
```

Run any Python script directly for debugging:

```bash
python fetch_data.py
python ema25_zl_scanner.py
python nifty50_zlema25_scanner.py
python ema-compression-scanner/screener.py
python dashboard_generator.py
python wt_bullcross_scanner.py
python wt_squeeze_dashboard.py
```

Install dependencies:

```bash
pip install requests bs4 python-dateutil yfinance tradingview-screener kiteconnect pyotp pyyaml pandas
```

## Architecture overview

### Data flow (daily, post 4:05 PM IST)

```
run_fetch_data.ps1
  → kite_auth.py          # TOTP login → updates .env KITE_ACCESS_TOKEN
                          # Skipped if token < 16h old (.kite_token_stamp)
  → fetch_data.py         # Kite EQ+indices: historical_data() backfill + quote() delta
                          # → .ohlc_data/market.db (SQLite)
                          # → .ohlc_data/data_manifest.csv (git-tracked)
                          # --all flag: also backfills breadth universe (2500 stocks, weekly)

All scanners → ohlc_db.py → .ohlc_data/market.db
```

### Central SQLite DB (`ohlc_db.py`)

`load_ohlc(symbol, lookback=400)` and `load_ohlc_many(symbols, lookback=400)` are the only DB entry points for scanners. Both return DataFrames with **lowercase columns** (`date`, `open`, `high`, `low`, `close`, `volume`) and `date` as a plain column (not index), oldest-first.

Instrument filter in `fetch_data.py`: `exchange=NSE`, `segment=NSE or INDICES`, no `-` in `tradingsymbol`. This excludes SME/BE-series/odd-lot instruments (~2,000–2,500 EQ stocks + indices, vs the raw 9,000+).

**Kite `quote()` field mapping**: `last_price` = today's close; `ohlc.close` = previous day's close. `fetch_data.py` always uses `last_price` for the delta close.

### Scanner pipeline — EMA compression (`ema-compression-scanner/`)

All thresholds live in `settings.yaml`. Pipeline:
1. `indicators.py` — `compute()` adds EMA50/100/200, ATR50, spread metrics; `bollinger_keltner()` adds BB(20,2.0) + KC(20,1.5) + `squeeze_on`; `zl25_stats()` + `rs_line()` are standalone
2. `gate.py` — EMA dual gate (spread < 1.5×ATR50 AND < 3% of EMA200, ≥10 bars); BB squeeze gate (BB inside KC ≥5 bars, width bottom 20%)
3. `scorer.py` — cross-candidate min-max normalization → 0-100 composite score
4. `screener.py` — orchestrates full pipeline, reads from SQLite, writes `ema_compression_latest.md`

### Scanner pipeline — EMA25 ZL (`ema25_zl_scanner.py`)

1. TradingView screener → watchlist (price > EMA25, MCap 1,000–5,00,000 Cr)
2. `load_ohlc(symbol)` → RS gate: daily RS > weekly RS EMA9 AND EMA9 rising
3. ZLEMA25 direction + `zl25_turn_stats()` → days since last turn-up, % gain
4. `bb_kc_squeeze()` → BB(20,2.0,SMA) inside KC(20,1.5,SMA) on last bar
5. Writes `ema25_zl_scans/ema25_zl_scans.md`

### Scanner pipeline — EMA55 Cross Watchlist (`ema55_cross_scanner.py`)

Pure price/EMA55 watch trigger, no RS gate — reuses `ema25_zl_scanner.get_watchlist()`
(same mcap ₹1,000 Cr–5 Lakh Cr / price > ₹50 universe) and its float hard-gate.

1. Per symbol: EMA55 via `ema25_zl_scanner.ema()`; keep only if `close` is within
   -10% to +20% of EMA55 (below-EMA stocks included as "approaching" watches;
   drops off once too extended above, or once it falls more than 10% under —
   self-pruning watchlist)
2. `ema55_cross_stats()` — bars since close last crossed above EMA55 (capped 60d) +
   % price change since that bar; same backward-scan-with-cap shape as
   `ema25_zl_scanner.zl25_turn_stats()`, just crossover-of-two-series instead of a
   ZLEMA25 slope turn
3. Writes `ema55_cross_scans/ema55_cross_scans.md` (dated + `_latest` equivalent as
   the undated file), sorted by cross age ascending (freshest first)
4. `build_union()` — prepends a "Union Watchlist" section at the top of the md,
   grouping symbols by how many of {EMA25 ZL, EMA55 Cross, Minervini Trend
   Template, Trend Scanner} flagged them today (`ALL 4` / `3 OF 4` / ... /
   `1 ONLY`, empty groups omitted). Reads the other three scanners'
   already-written `_latest.md` files read-only, parsing symbols straight out
   of their existing TV-paste blocks (`_symbols_from_tv_block()`) rather than
   importing their internals — EMA25 ZL's "WATCH" section is excluded
   (near-miss only, not the Rising signal). `_load_union_source()` checks
   each file's title line carries today's date before trusting it; a
   missing/stale source is dropped with a note instead of blocking the
   union. **Requires `run_all_scanners.ps1` to run EMA55_Cross after
   MinerviniTrend and TrendScanner** (both moved there specifically for
   this — see run order above) so all three upstream files exist same-run.

### Scanner pipeline — Union Watchlist Chart Dashboard (`union_chart_dashboard.py`)

Full design: `docs/superpowers/specs/2026-08-20-union-chart-dashboard-design.md`.

1. Reads today's union watchlist symbols + confluence tier straight from
   `ema55_cross_scans/ema55_cross_scans.md`'s union tv-paste block
   (`parse_union_tiers`/`load_todays_union`) — aborts with nothing written
   if that file is missing or not dated today (no stale publish)
2. `load_ohlc_many(symbols, lookback=250)` — only DB entry point, per repo
   convention; symbols with <130 bars skipped (count logged, not silent)
3. `build_chart_data()` — OHLCV per symbol as a plain `[date,o,h,l,c,v]`
   array, no server-side EMA (computed client-side so the live period
   control needs no regenerate)
4. `build_html()` — one self-contained HTML file: vendored
   `lightweight-charts.js`, a global control bar (candle up/down color,
   EMA periods, symbol/tier filter), and a card grid (one chart per
   symbol) that lazy-constructs each chart via `IntersectionObserver` as
   it scrolls into view (required at ~500 symbols to keep first paint fast)
5. Writes `dashboard/union_charts.html`

### Scanner pipeline — NIFTY 50 ZLEMA25 Trend (`nifty50_zlema25_scanner.py`)

1. Refreshes the official NSE NIFTY 50 constituent CSV and atomically caches the validated 50-symbol universe at `data/nifty50_constituents.csv`; uses the cache when NSE is unavailable.
2. `load_ohlc(symbol)` loads daily bars for every constituent with no market-cap, price, RS, liquidity, or float exclusion gate.
3. Reuses the EMA25 ZL formula from `ema25_zl_scanner.py`; strict positive slope is uptrend, strict negative slope is downtrend, and exact equality is flat.
4. Trend age counts consecutive trading bars in the current direction (new direction = `1d`); ZL Chg% uses the close immediately before the turn bar.
5. Writes `nifty50_zlema25_scans/nifty50_zlema25_scans.md` with separate uptrend/downtrend tables sorted youngest-first and symmetric `1d`, `2d`, `3d`, `4-5d`, `6-10d`, `11-15d`, and `15d+` TradingView buckets.

Manual run: `python nifty50_zlema25_scanner.py`. Production runner: `run_nifty50_zlema25_scanner.ps1`; `run_all_scanners.ps1` invokes it immediately after the broad EMA25 ZL scanner.

### Scanner pipeline — Weekly ZL (`weekly_zl_scanner.py`)

1. TradingView screener → watchlist (MCap ₹800 Cr – ₹1 Lakh Cr, no RS gate)
2. `load_ohlc(symbol)` → `to_weekly()` resamples daily OHLC to weekly (partial current week included)
3. Weekly ZLEMA25 (`2×EMA25 − EMA(EMA25)`) — uptrend start: `zl25[-1] > zl25[-2] AND zl25[-3] >= zl25[-2]` (rising this bar, flat/falling previous bar)
4. `zl25_consecutive_rising()` → count consecutive weekly bars ZLEMA25 has been rising
5. `price_vs_zl`: TOUCH (±1.5% of ZLEMA25 level) / ABOVE / BELOW — flags pullback entry zone
6. `bb_kc_squeeze_info()` → squeeze column (informational, not a gate)
7. Writes `weekly_zl_scans/weekly_zl_scans.md`; sorted TOUCH-first, then by `-consec_weeks`

### Scanner pipeline — Weekly RS EMA9 Trend (`rs_weekly_ema9_scanner.py`)

"Trending universe" list — daily RS above weekly RS EMA9 AND that EMA9 flat/rising
(same weekly-resample + EMA9 math as `ema25_zl_scanner.py` RS_MODE=weekly_ema9 /
`wt_bullcross_scanner.py` `_rs_weekly_gate()`, kept in sync per CLAUDE.md Python↔Pine
parity convention).

1. TradingView screener → watchlist (MCap ₹800 Cr – ₹1 Lakh Cr, price > ₹50)
2. `load_ohlc(symbol)` + benchmark (`NIFTY MIDSML 400`) → daily RS Line, weekly RS EMA9
3. Keeps stock if daily RS > weekly RS EMA9 (today) AND weekly RS EMA9 this week ≥ last week
4. `age` = consecutive trading days daily RS has stayed above the weekly RS EMA9
5. `new_entrant` = symbol wasn't in previous run's output (diff vs `rs_weekly_ema9_state.json`,
   mirrors `nse_ema_daily.py`'s diff pattern)
6. Writes `rs_weekly_scans/rs_weekly_ema9_scans.md`; sorted by age ascending (newest first)
7. Appends today's count to `rs_weekly_scans/rs_weekly_ema9_history.csv` (idempotent upsert
   by date) and renders it as `dashboard/rs_weekly_ema9_history.html` (GitHub Pages)

### Scanner pipeline — Consolidation Tracker (`consolidation/`)

Phase 1+2 of `research/consolidation_capital_efficiency_spec.md` (full spec covers 7 phases;
only indicators+quality+imminence+tiers+scanner are built — see
`docs/superpowers/specs/2026-07-05-consolidation-scanner-phase1-2-design.md`).

1. `indicators.py` — EMA compression (Sec 2.1), BB/KC squeeze (Sec 2.2), volume exhaustion
   (Sec 2.3), RS character (Sec 2.4)
2. `quality.py` — 0-100 quality score (Sec 3): BB depth + EMA stage + vol exhaustion +
   RS character + CMF (reuses `ohlc_db.cmf_series()`) + delivery% trend (reuses
   `ohlc_db.load_delivery()`)
3. `imminence.py` — 0-100 imminence score + 6 pre-break signals (Sec 4)
4. `tiers.py` — COLD/WARM/HOT tier lookup + stateless `consolidation_age`/quality-peak-drawdown
   (backward-scan over historical OHLC, no DB) + abandonment checks (Sec 5)
5. `consolidation_scanner.py` — `run(universe_df, as_of) -> pd.DataFrame`; own TradingView
   universe query (mcap 1,000–5,00,000 Cr, price > ₹50, mirrors `wt_bullcross_scanner.py`);
   writes `results/YYYY-MM-DD-consolidation.csv` (Layer 1 → future Pine Layer 2 contract) +
   `consolidation_scans/consolidation_scan_latest.md`

Gate: EMA dual gate AND BB squeeze gate only — volume/RS are scored, not filtered on.

### Scanner pipeline — Capital rules (`capital/`)

Phase 3 of the consolidation spec (Sec 6, 8, 9) — see `docs/superpowers/plans/2026-07-06-consolidation-scanner-phase3.md`.

1. `regime_throttle.py` — GREEN/NEUTRAL/RED classification off `data/breadth_history.csv`
   (`ratio_5d` + `pct_above_sma200` + its 5-row trend); returns `max_slots` + `time_stop_mode`
2. `time_stops.py` — breakout entry trigger (close > range high, vol >= 2x vol_ma50,
   delivery% >= baseline), ATR-capped stop price, fixed-₹15k position sizing, bar-3/5/10
   time-stop ladder, opportunity-cost flags. Not yet wired to a live position tracker —
   pure functions only, called once one exists.
3. `slots.py` — DEPLOYED/ARMED/FREE slot capacity state machine (stateless, caller-owned list)

`consolidation_scanner.py` calls `regime_throttle.regime_for_date()` once per run and stamps
every row with the day's `regime` + a tier-derived `action` (`DEPLOY_ELIGIBLE`/`ARM`/`WATCH`/
`NONE`/`NO_DEPLOY`). `time_stops`/`slots` are available but not called from the daily scan —
they operate on live position state this scanner doesn't track (no `signals.db`, by design).

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

### Scanner pipeline — Institutional Footprint (`institutional_footprint_scanner.py`)

Full spec: `research/nse_institutional_footprint_plan_spec.md`. All 5 phases built.

1. Own TradingView universe query (NSE common equity, mcap ₹1,000 Cr–₹5,00,000 Cr, price > ₹50)
2. Per symbol: `load_ohlc_many()` + `ohlc_db.load_delivery()` → delivery percentile/z-score
   (vs trailing 252-session window), price/volume/CMF/RS indicators
3. `calculate_ics()` → 0-100 Institutional Campaign Score across delivery/volume/price/money-flow/RS
4. `assign_rating()` (ELITE/STRONG/BUILDING/WATCH/IGNORE) + `assign_lifecycle()`
   (DISTRIBUTION > BREAKOUT > MARKUP > BUILDING > SEED) + `assign_trade_action()` (regime-gated)
5. Writes `footprint_scans/footprint_latest.md` + dated `.md`/`.csv`
   (CSV is the Phase 5 signal-history store — no DB table until cross-day queries need one) and
   `dashboard/footprint.html` (dark-mode cards, vanilla-JS symbol/stage filter)

### Daily Gainers Brief (`daily_gainers_brief.py`)

1. Fetches NSE gainers + positive-change value stocks from two NSE API endpoints
2. Combines, deduplicates by symbol, takes top 20 by % change DESC
3. For each stock: enriches via KG (Neo4j BENEFITS_FROM themes + TRIGGERED catalysts) → `.company_cache/` (30d TTL) → screener.in live scrape cascade
4. Assembles `business_text` / `products_text` / `macro_text` directly from raw data (no LLM)
5. Generates responsive HTML with day/night toggle, sortable summary table, per-stock cards with KG pills
6. Writes `daily_brief.html` (root, always overwritten) + `daily_briefs/daily_brief_YYYY-MM-DD.html`
7. `--dry-run` flag prints enriched context, skips HTML write

### Scanner pipeline — WaveTrend Bull Cross (`wt_bullcross_scanner.py`)

1. TradingView screener → broad watchlist (NSE equity, 1,000–1,00,000 Cr, price > ₹50, **no RS filter**)
2. `load_ohlc_many(symbols)` → batch OHLCV load from SQLite
3. `WaveTrendCalculator` (from `wavetrend_scanner.py`) → `wt_signal_rank` per stock
   - Rank 5: BULL_OS_PPV — deep oversold cross (wt2 ≤ −60) + Pocket Pivot Volume
   - Rank 4: BULL_ANY_PPV — any cross + PPV
   - Rank 3: BULL_OVERSOLD — deep oversold cross
   - Rank 2: BULL_OS_L2 — soft oversold cross (wt2 ≤ −53)
   - Rank 1: BULL_ANY — any bull cross (mid-range)
4. Context per stock: ZLEMA25 direction + turn stats, BB-KC squeeze flag
5. Writes `wt_scans/wt_bullcross_latest.md` (grouped by rank, rank desc)

**No RS filter** is intentional: WT oversold signals fire before RS turns positive; filtering on RS would kill the best setups.

### Scanner pipeline — RS Leadership (`rs_leadership_scanner.py`)

Mirrors `pine_scripts/Satya RS Relative Leadership.txt`. Full design:
`docs/superpowers/specs/2026-07-13-rs-leadership-scanner-design.md`.

1. TV screener (same filters as `rs_highline_scanner.get_watchlist()`) -> watchlist
2. `load_ohlc_many()` + NIFTY MIDSML 400 bench
3. `_rs_leadership_signal()` -> combined cross: RelPerf% (9-bar lookback) >= 0
   AND its 5-bar EMA rising, true today, NOT both true yesterday
4. `_leadership_score()` -> 0-5 score + RS state (strong/weak/transition),
   mirrors the .txt's `leadershipScore` formula
5. Writes `rs_leadership_scans/rs_leadership_latest.md`, sorted score desc
   then RelPerf% desc

No benchmark-trend filter applied (explicit deviation from the Pine source's
default-checked `useBenchmarkFilter` input).

### Scanner pipeline — Minervini Trend Template (`minervini_trend_scanner.py`)

Full design: `docs/superpowers/specs/2026-08-02-minervini-trend-template-scanner-design.md`.

1. Reuses `ema25_zl_scanner.get_watchlist()` for universe (NSE common equity, MCap ₹1,000 Cr – ₹5 Lakh Cr, price > ₹50) and float hard-gate
2. `load_ohlc(symbol)` -> `trend_template_checks()`: strict AND-gate on 8 SMA50/150/200-stack and 52wk high/low checks
3. Criterion 9 (RS strength): `minervini_trend_scanner._weekly_rs_ema9_gate()` — weekly RS EMA9 flat or rising; deliberately does NOT require RS Line above the EMA9 (unlike `ema25_zl_scanner._weekly_rs_gate()`)
4. No partial-score output — binary qualify list only, sorted by Age ascending (newest entries into the trend first)
5. `trend_template_age()` -> Age column: consecutive trading days all 9 checks have held true together (vectorized backward walk, no state file)
6. Additions/deletions vs previous run (state in `minervini_scans/minervini_trend_state.json`, mirrors `rs_weekly_ema9_scanner.py`) shown as a 2-column table at the top of the output
7. "By Trend Age" section groups qualifiers into wider buckets than `ema25_zl_scanner`/`nifty50_zlema25_scanner`'s day-granularity `_AGE_BUCKETS` (`<2 WEEKS` / `2-4 WEEKS` / `1-2 MONTHS` / `2-3 MONTHS` / `3-6 MONTHS` / `6+ MONTHS`, see `AGE_BUCKETS` in `minervini_trend_scanner.py`) since the 9-check AND-gate age runs weeks-to-months once qualified, not days — each bucket gets its own TV watchlist copy block
8. Writes `minervini_scans/minervini_trend_latest.md` + dated `.md`

### Scanner pipeline — Breadth Monitor (`scanners/breadth_monitor.py`)

**Regime/timing layer — not a candidate-selection scanner.** Answers "is the market supportive?"
**Runs as separate scheduled task `NSE_BreadthMonitor` at 5:30 PM** (after regular scanners).
`run_breadth_monitor.ps1` is self-contained: kite_auth → `fetch_data.py --all` → breadth_monitor.py → commit.

1. Reads `data/breadth_universe.csv` (broad NSE EQ, ~2,000–2,500 symbols, refreshed weekly)
2. `load_ohlc_many(symbols, lookback=2500)` → 10yr OHLCV from SQLite
3. `compute_daily_breadth(universe_df, as_of, ohlc_map)` — pure function:
   - up4/down4: stocks ≥+4% / ≤-4% (circuit-frozen excluded: close==prev AND vol==0)
   - ratio_5d / ratio_10d: rolling up/down count ratios (thresholds 1.6/0.6 — TODO: validate)
   - up25_quarter / down25_quarter: ≥25% / ≤-25% over 63 trading days
   - pct_above_sma200: plain SMA (circuit-gap distortion: known, deferred v1.1)
   - composite_score: always null (v1 — TODO: backtest weights before enabling)
4. `update_breadth_history()` upsert → `data/breadth_history.csv` keyed (date, universe_tag)
5. `build_dashboard_html()` → `dashboard/breadth.html` (GitHub Pages)

### Dashboard — WaveTrend + Squeeze (`wt_squeeze_dashboard.py`)

Reads two scanner outputs, finds confluence, builds `wt_squeeze_dashboard.html`:
- `wt_scans/wt_bullcross_latest.md` → WT bull cross rows
- `ema-compression-scanner/ema_compression_scans/ema_compression_latest.md` → squeeze rows
- Confluence section (starred ★): stocks appearing in **both** today
- WT section has priority — sorted rank 5→1, deeper oversold first within same rank
- Links back to `dashboard.html`

Builds twice daily: 4:40 PM (`run_wt_squeeze_dashboard.ps1`, no Bounce-RS data yet) and again
~5:30-5:35 PM (triggered by `run_breadth_monitor.ps1`'s trailing step, once today's breadth
ratio and Bounce-RS scan are both available).

### Dashboard (`dashboard_generator.py`)

Reads today's block from 6 markdown files (swing, momentum, weekly-RS, EMA25-ZL, EMA compression, circuit limits), cross-references symbols, builds `dashboard.html` with confluence scoring.

### Circuit limits (`main.py`)

Fetches `nseindia.com/api/eqsurvactions` → parses CSV → generates `index.html` + `NSE_Circuit_Limits.md`. Color code: 🟨 20→10% · 🟥 10→5% · 🟩 5→10% · 🟦 10→20%.

## Key conventions

**ATR**: EMA compression scanner uses SMA ATR (`tr.rolling(period).mean()`) for BB/KC to match TradingView's `ta.sma(ta.tr)`. Wilder EWM is available as `kc_atr_wilder=True` but not the default.

**ZLEMA25**: `2 * EMA(25) - EMA(EMA(25))`. "Rising" = last bar > second-to-last bar.

**RS benchmark**: Kite tradingsymbol `"NIFTY MIDSML 400"` (with spaces). Stored in SQLite like any other symbol.

**Trading-day gap detection**: Use integer position-index differences, not calendar-day differences, to handle NSE holidays correctly.

**Git**: Only `data_manifest.csv` is committed from the data layer. `market.db` is gitignored. Scan output markdown files are committed by their respective PS1 scripts.

## Output files (git-tracked)

| File | Written by |
|------|-----------|
| `NSE_Circuit_Limits.md`, `index.html` | `main.py` |
| `ema25_zl_scans/ema25_zl_scans.md` | `ema25_zl_scanner.py` |
| `ema55_cross_scans/ema55_cross_scans.md` | `ema55_cross_scanner.py` |
| `weekly_zl_scans/weekly_zl_scans.md` | `weekly_zl_scanner.py` |
| `rs_weekly_scans/rs_weekly_ema9_scans.md` | `rs_weekly_ema9_scanner.py` |
| `rs_weekly_scans/rs_weekly_ema9_history.csv`, `dashboard/rs_weekly_ema9_history.html` | `rs_weekly_ema9_scanner.py` |
| `ema-compression-scanner/ema_compression_scans/ema_compression_latest.md` | `screener.py` |
| `momentum_scans/momentum_scans.md` | `momentum_scanner.py` |
| `momentum_scans/momentum_rs_weekly_scans.md` | `momentum_rs_weekly_scanner.py` |
| `wt_scans/wt_bullcross_latest.md`, `wt_scans/wt_bullcross_YYYY-MM-DD.md` | `wt_bullcross_scanner.py` |
| `trend_scans/trend_scan_latest.md`, `trend_scans/trend_scan_YYYY-MM-DD.md` | `trend_scanner.py` |
| `wt_squeeze_dashboard.html` | `wt_squeeze_dashboard.py` |
| `swing_scans/swing_scans.md` | `swing_scanner.py` |
| `ema_screener_changes.md` | `nse_ema_daily.py` |
| `dashboard.html` | `dashboard_generator.py` |
| `daily_brief.html`, `daily_briefs/daily_brief_YYYY-MM-DD.html` | `daily_gainers_brief.py` |
| `.ohlc_data/data_manifest.csv` | `fetch_data.py` |
| `data/breadth_history.csv`, `dashboard/breadth.html` | `scanners/breadth_monitor.py` |
| `rs_highline_scans/rs_highline_latest.md`, `rs_highline_scans/rs_highline_YYYY-MM-DD.md` | `rs_highline_scanner.py` |
| `rs_leadership_scans/rs_leadership_latest.md`, `rs_leadership_scans/rs_leadership_YYYY-MM-DD.md` | `rs_leadership_scanner.py` |
| `minervini_scans/minervini_trend_latest.md`, dated `.md` | `minervini_trend_scanner.py` |
| `us_wt_scans/us_wt_bullcross_latest.md`, `us_wt_scans/us_wt_bullcross_YYYY-MM-DD.md`, `us_wt_scans/us_wt_bullcross_dashboard.html` | `us_wt_bullcross_scanner.py` |
| `bounce_rs_scans/bounce_rs_scan_latest.md` | `run_bounce_rs_scanner.py` |
| `footprint_scans/footprint_latest.md`, dated `.md`/`.csv` | `institutional_footprint_scanner.py` |
| `dashboard/footprint.html` | `institutional_footprint_scanner.py` |
| `dashboard/union_charts.html` | `union_chart_dashboard.py` |

## Environment (`.env` inside `ema-compression-scanner/`)

```
KITE_API_KEY=
KITE_API_SECRET=
KITE_ACCESS_TOKEN=      # auto-updated by kite_auth.py
KITE_USER_ID=
KITE_PASSWORD=
KITE_TOTP_SECRET=
```

Stock universe file (gitignored, must be present locally):
`NSE_500cr_15CrNotional10D_50rs_sector_industry.csv`
