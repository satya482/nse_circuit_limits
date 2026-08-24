> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Repo Handoff

Last reviewed by Codex: 2026-07-20.
Last reviewed by Claude Code: 2026-07-15 (see "Current Worktree State" below).

This repository is a Windows-first scanner and dashboard suite for NSE and US equities. It is actively maintained by multiple agents, especially Claude Code and Codex. Treat this file as the neutral takeover map; `CLAUDE.md` remains the deeper scanner operations manual.

## Current Worktree State

Updated 2026-08-24 by Codex, five-source EMA55 union watchlist:

- `ema55_cross_scanner.py` now reads the complete qualifying list from `rs_weekly_scans/rs_weekly_ema9_scans.md` as a fifth equal confluence source alongside EMA25 ZL, EMA55 Cross, Minervini Trend Template, and Trend Scanner.
- The union heading names Weekly RS EMA9 and dynamic tiers now render as `ALL 5` / `4 OF 5` / `3 OF 5` / `2 OF 5` / `1 ONLY` when all sources are fresh; the established stale/missing-source degradation remains unchanged.
- The existing scheduler order already runs `RS_WeeklyEMA9` before `EMA55_Cross`, so no PowerShell change was needed. Current Weekly RS parsing returned all 597 qualifying symbols.
- Verification on 2026-08-24: focused EMA55 tests 14/14, full suite 463/463, and `git diff --check` passed. The tracked EMA55 report was not regenerated because EMA25 ZL, Minervini, and Trend outputs were stale before today's scheduled scans; the next normal pipeline run will write a genuine five-source union.

Updated 2026-08-24 by Codex, weekly RS EMA9 slope-only scanner:

- `rs_weekly_ema9_scanner.py` now qualifies stocks solely when weekly RS EMA9 is flat or rising versus the prior week within `SLOPE_EPS`; daily RS no longer has to be above the weekly EMA9.
- Trend age is now the consecutive number of non-falling weekly EMA9 transitions, reported as `Age(w)`. The current partial week remains included.
- The TradingView universe now matches the EMA55 market-cap range: NSE common equity, price above Rs50, market cap Rs1,000 Cr through Rs5 lakh Cr. EMA55 signal and float gates were not added.
- Existing latest/dated reports, state, history CSV/HTML, PowerShell runner, and `RS_WeeklyEMA9` orchestration entry remain in place.
- Verification on 2026-08-24: focused weekly-RS tests 9/9, full suite 460/460, and a live TradingView/local-OHLC run completed over 1,426 watchlist stocks with 597 qualifying and 46 new entrants.
- Live output: `rs_weekly_scans/rs_weekly_ema9_scans.md` and `rs_weekly_scans/rs_weekly_ema9_scans_2026-08-24.md`.

Updated 2026-07-20 by Codex, NSE F&O ZLEMA25 EMA25-parity scanner:

- Reworked `fno_zlema25_scanner.py` into a thin adapter over `ema25_zl_scanner.py`. The authoritative source remains NSE `SECURITIES IN F&O` through `fno_universe.py`; candidates are intersected with the broad TradingView price/market-cap eligibility list, so non-F&O symbols cannot enter.
- F&O symbols now use the broad scanner's daily RS EMA21 gate, float hard gate, squeeze, SAFE/CAUTION, liquidity, weekly-RS, Strong Start/RVOL, CMF, delivery, labels, and circuit-limit enrichment.
- The report now has exclusive current `ZLEMA25 Uptrend` and `ZLEMA25 Downtrend` tables. Each direction has its own capped 60-bar age and price change from the close before its turn; exact-flat slopes are counted separately. Both directions receive symmetric, direction-prefixed TradingView age buckets.
- `ema25_zl_scanner.py` gained backward-compatible direction-aware turn statistics and optional directional report rendering. Its default broad Rising/Watch report contract remains unchanged.
- `run_fno_zlema25_scanner.ps1` now checks `$LASTEXITCODE` and stops before git publish when Python fails. F&O report writes force LF line endings so tracked output passes `git diff --check` on Windows.
- Live run on 2026-07-20: NSE endpoint returned 404 and the established stale cache fallback supplied 209 F&O symbols; 192 passed TradingView eligibility, 81 passed analysis gates, with 80 uptrends, 1 downtrend (`NUVAMA`, age `3d`), and 0 flat.
- Verification: 9/9 focused F&O tests, 32/32 related NIFTY 50 scanner tests, full suite 401/401, PowerShell parse, live network/local-OHLC scan, and `git diff --check` passed. Design: `docs/superpowers/specs/2026-07-20-fno-zlema25-ema25-parity-design.md`; plan: `docs/superpowers/plans/2026-07-20-fno-zlema25-ema25-parity.md`.

Updated 2026-07-17 by Codex, NIFTY 50 daily ZLEMA25 trend-age scanner:

- Added `nifty50_zlema25_scanner.py`, a dedicated no-exclusion-gate scan of the current NIFTY 50 universe. It refreshes the official NSE constituent CSV, validates exactly 50 unique symbols, and falls back to the atomically cached `data/nifty50_constituents.csv`.
- Daily ZLEMA25 uses the existing `ema25_zl_scanner.py` formula. Strict rising/falling slopes produce separate uptrend/downtrend tables; exact equality is flat. Age is the full consecutive trading-bar run, resets to `1d` at a direction change, and sorts ascending then by symbol.
- Output `nifty50_zlema25_scans/nifty50_zlema25_scans.md` includes separate direction tables plus symmetric `1d`, `2d`, `3d`, `4-5d`, `6-10d`, `11-15d`, and `15d+` TradingView watchlists. Informational liquidity/CMF/delivery, squeeze, labels, and circuit columns never exclude a constituent.
- Added `run_nifty50_zlema25_scanner.ps1` and registered `NIFTY50_ZLEMA25` in `run_all_scanners.ps1` immediately after `EMA25_ZL`. The runner stops on scanner failure and stages only the generated report plus validated constituent cache.
- Added `tests/test_nifty50_zlema25_scanner.py`. Final verification: 32/32 focused scanner tests passed, 15/15 related daily-ZLEMA backtest regression tests passed, all PowerShell files parsed, and `git diff --check` was clean.
- Live local-OHLC run on 2026-07-17 used `NSE refresh`: requested 50, analysed 50, skipped 0, flat 0, uptrend 25, downtrend 25. Rerun with `python nifty50_zlema25_scanner.py` after the normal OHLC refresh.
- Feature commits: `c8b299d`, `a4b531f`, `deaa18e`, `aa8d864`; documentation/report handoff follows in the next commit. Design: `docs/superpowers/specs/2026-07-17-nifty50-zlema25-trend-scanner-design.md`; plan: `docs/superpowers/plans/2026-07-17-nifty50-zlema25-trend-scanner.md`.

Updated 2026-07-16 by Codex, ATR Bible Pine suite takeover:

- Resumed Claude Code's implementation plan at Task 3 after commits `3749514` and `4fff336` completed the overlay calculations, visuals, stop/target lines, and dashboard.
- `pine_scripts/ATR_Bible_Overlay.pine` now has all 7 pipe-format alert conditions with hidden plot placeholders. Circuit-suspect bars suppress ATR-derived stop/target/sizing output, and disabling the dashboard clears its persistent table.
- Added `pine_scripts/ATR_Bible_Panel.pine`: ATR(10)/ATR(50) lines and fill, CR state line and zones, ATR-delta histogram, and current verdict label.
- Added `tests/test_atr_bible_pine.py` for suite structure, alert coverage, overlay/panel input parity, dashboard hiding, and circuit-day trade-math suppression. Focused result: 5/5 passed.
- Added the required SEBI disclaimer to the source spec and implementation plan. Local static review is complete; final Pine syntax and visual behavior still require pasting both scripts into TradingView. The source spec remains untracked until this task is committed.

Updated 2026-07-15 by Claude Code, ZLEMA25 Trend Labels stats box (commit `c523062`):

- `pine_scripts/ZLEMA25_Trend_Labels.pine` — new middle-right stats table: ZLEMA25 + EMA20
  current-uptrend age (bars) and % since trend start; `—` when a line is not rising. EMA20
  stats mirror the ZLEMA25 convention (% base = close of bar before turn-up bar). Vertical
  nudge via "Empty rows above/below" pad inputs (pad cells use `" "` — empty text collapses
  to zero height). Existing labels/barcolor untouched. Pending: user compile/visual check on
  TradingView. Spec: `docs/superpowers/specs/2026-07-15-zlema25-stats-box-design.md`.

Updated 2026-07-15 by Claude Code, EMA25 ZL scanner WT-parity symbol tags:

- `ema25_zl_scanner.py` brought on par with `wt_bullcross_scanner.py` info density:
  - Float trap hard gate (`float_gate.py`): watchlist now selects `float_shares_outstanding`,
    `get_watchlist()` returns `(symbols, float_map)`, ⛔ AVOID stocks dropped from scan.
  - Symbol sub-line extras (order): trap label (✓ SAFE / ⚠ CAUTION, n/a hidden) · `liq_tag`
    (was computed but never rendered — dead data, now shown) · 📶W9 (weekly RS EMA9 gate,
    via new `_weekly_rs_gate()` — extracted from `_rs_gate()`'s weekly branch, mirrors
    `wt_bullcross_scanner._rs_weekly_gate()`) · 🚀SS / RVOL8x (`_rvol_ss()` copied from WT
    scanner, Pine parity) · CMF · DEL% (already there).
  - WT-specific columns NOT ported (cross-type, divergence, weekly WT zone, Erly, RS%, C/AvgC).
  - Scan-definition header documents float gate + tag legend. README scanner entry updated.

Updated 2026-07-14 by Claude Code, ZLEMA25 trend labels Pine:

- `pine_scripts/ZLEMA25_Trend_Labels.pine` — new standalone overlay. ZLEMA25 line + label on every completed uptrend segment (days + % at last rising bar, silver) plus live label for current uptrend (white). % base = close before turn-up candle, same as scanner ZL Chg% reference. `max_labels_count=500`.

Updated 2026-07-14 by Claude Code, EMA25 ZL watchlist buckets:

- `ema25_zl_scanner.py` `build_markdown()`: top-of-page combined block replaced by a single TV-importable watchlist using `###SECTION` separators (TradingView paste format) by ZL days since turn-up: 1d / 2d / 3d / 4-5d / 6-10d / 11-15d / 15d+ plus WATCH. Bottom "TradingView Watchlists" per-bucket copy blocks retained (rising set only; empty buckets skipped). Today's output regenerated. README scanner entry updated.

Updated 2026-07-14 by Claude Code, footprint scanner cwd fix (commit `2fad056`):

- `run_institutional_footprint_scanner.ps1` now does `Set-Location $ROOT` before invoking python. The `NSE_FetchDelivery` scheduled task has no `WorkingDirectory`, so runs since 2026-07-10 started in `C:\Windows\System32` and died on `PermissionError: Access is denied: 'footprint_scans'` (scanner uses repo-relative paths). Last good output was `footprint_scans/footprint_2026-07-09.*`; tonight's 6:15 PM run is the real verification.
- Known-but-unfixed: breadth monitor runs twice daily (AllScanners trailing trigger + unconditional 5:30 PM fallback trigger on `NSE_BreadthMonitor`). Harmless - history upsert is idempotent - just redundant compute.

Updated 2026-07-13 by Codex, daily ZLEMA25 + weekly RS EMA9 backtest:

- Added `backtest_daily_zlema25_weekly_rs.py`, a no-look-ahead local-OHLC backtest using `NIFTY MIDSML 400` as benchmark.
- Entry: first daily ZLEMA25 turn-up while daily RS is above a rising partial-week RS EMA9. Exit: first daily ZLEMA25 downturn or weekly RS EMA9 no longer rising, at close.
- Initial run covers TRIVENI, CARTRADE, and KIRLOSENG from 2021-08-20 through 2026-07-13.
- Actual results: TRIVENI 48 completed trades / 27.08% win rate / -18.37% compounded return; CARTRADE 40 / 25.00% / 22.49%; KIRLOSENG 57 / 36.84% / 350.56%; combined 145 / 30.34% / 350.47%, with one open KIRLOSENG trade excluded from completed-trade statistics. The combined 350.47% compounded figure is a strategy-sequence diagnostic, not a realizable portfolio return, because trades across the three stocks overlap.
- Outputs: `backtest_results/daily_zlema25_weekly_rs_trades.csv`, `daily_zlema25_weekly_rs_open.csv`, and disclaimer-compliant `daily_zlema25_weekly_rs_summary.md`.
- Re-run: `python backtest_daily_zlema25_weekly_rs.py TRIVENI CARTRADE KIRLOSENG --start 2021-08-20 --end 2026-07-13`.
- Verification: CSV arithmetic/holding-period assertions passed; focused tests passed 15/15 and the full suite passed 355/355 on 2026-07-13.

Updated 2026-07-07 by Claude Code, after merging `feat/consolidation-panel-pine` to `main` (pushed to origin, commits `ef160f7`, `4820956`):

- Working tree is clean as of this write — no pending modified/untracked files from this session.
- `pine_scripts/Consolidation_Panel.pine` — **done**. Sec 12 Indicator 1 (Consolidation Tracker Phase 6, second of two Pine companions). Built via subagent-driven-development from `docs/superpowers/plans/2026-07-07-consolidation-panel-pine.md` (2 tasks, both task-reviewed + final whole-branch reviewed, verdict READY TO MERGE, no fixes needed). Companion to the already-existing `pine_scripts/Consolidation_PreBreak_Alerts.pine` (Indicator 2). Both Pine indicators for Sec 12 are now complete.
- The previously-untracked `pine_scripts/Monthly_HL_projection.pine` diff (high/low projection lines → close projection lines), `research/consolidation_capital_efficiency_spec.md`, and `research/nse_institutional_footprint_plan_spec.md` are now committed to `main` (commit `4820956`), along with `AGENTS.md`/`HANDOFF.md` themselves.
- Consolidation spec (`research/consolidation_capital_efficiency_spec.md`) remaining open items: Phase 7 `research/half_life_backtest.py` (not started — no `expected_annualized` ranking metric yet); wiring `capital/time_stops.py`/`capital/slots.py` to live positions (both exist but nothing calls them — needs a `signals.db` position tracker first, doesn't exist by design).

Updated 2026-07-07 by Codex, institutional footprint scanner work:

- `research/nse_institutional_footprint_plan_spec.md` was rewritten from greenfield app to repo-native scanner spec and now includes the required `SEBI registered` disclaimer.
- `institutional_footprint_scanner.py` added as a root-level EOD scanner. It reuses `ohlc_db.py`, `fetch_delivery.py` data, `capital/regime_throttle.py`, and `disclaimer.py`; no new DB/schema/package.
- `tests/test_institutional_footprint.py` added for pure helper/scoring behavior plus injected-data scanner/report behavior.
- Live smoke run generated `institutional_footprint_scans/institutional_footprint_latest.md` and `institutional_footprint_scans/institutional_footprint_2026-07-07.md`. Report is filtered to `ICS >= 55` / non-`IGNORE` rows to avoid universe-sized output.
- Reports include market regime, A/B/C action rank, and deployment action. Not scheduled yet. No PowerShell runner yet. Pending enhancements: optional dashboard integration, optional runner/commit flow, and calibration/backtest of ICS thresholds.
- `fetch_delivery.py` now supports resumable historical delivery backfill with `--from YYYY-MM-DD --to YYYY-MM-DD`, progress tracking in local SQLite table `delivery_backfill_progress`, and `--stats` summaries. Local backfill for `2025-01-01` through `2026-07-07` loaded 383 available trading dates / 857,541 rows; 12 dates returned NSE archive 404s.

Updated 2026-07-07 by Claude Code, institutional footprint scanner follow-up (on top of Codex's MVP above):

- Added `delivery_zscore()` alongside `delivery_percentile()` (same 252-session window, population stdev, `None` when prior window has zero variance); surfaced as `Z+n.n` in the delivery tag.
- Closed the three items Codex left pending: `build_html()` → `dashboard/institutional_footprint.html` (dark cards, vanilla-JS filter, SEBI banner/footer); dated CSV snapshot per run as the Phase-5 signal-history store (no DB table yet, per spec); `run_institutional_footprint_scanner.ps1` added (6:20 PM, after delivery fetch), not yet registered as a scheduled task.
- `CLAUDE.md` updated: run-schedule line, output-files table, architecture section for the scanner.
- Still pending: schtasks registration, ICS threshold calibration/backtest — spec explicitly says wait for real signal quality first.
- Wired `run_institutional_footprint_scanner.ps1` as a trailing step of `run_fetch_delivery.ps1` (needs today's delivery% first), test-run confirmed working end to end. Dashboard file renamed `dashboard/institutional_footprint.html` → `dashboard/footprint.html`.
- Output folder renamed `institutional_footprint_scans/` → `footprint_scans/`, files renamed `institutional_footprint_latest.md`/`institutional_footprint_YYYY-MM-DD.md`/`.csv` → `footprint_latest.md`/`footprint_YYYY-MM-DD.md`/`.csv`. `institutional_footprint_scanner.py` (script name) unchanged.

Always rerun `git status --short` before making changes because Claude Code and Codex may be working in parallel.

## High-Level Architecture

- Root-level Python scripts are scanner entry points and report generators. Many are intentionally flat scripts rather than packages.
- `ohlc_db.py` is the central NSE OHLCV read layer over `.ohlc_data/market.db`.
- `us_ohlc_db.py` is the US OHLCV read layer over `.us_ohlc_data/us_market.db`.
- `fetch_data.py` populates NSE OHLCV through Kite and writes `.ohlc_data/data_manifest.csv`.
- `fetch_us_data.py` populates US OHLCV through yfinance and writes `us_data_manifest.csv`.
- `disclaimer.py` owns mandatory Markdown and HTML disclaimer constants.
- PowerShell `run_*.ps1` files are production runners. They log to `logs/`, often auto-commit outputs, and encode scheduled-task behavior.
- Generated scan outputs live in folders such as `ema25_zl_scans/`, `zl_squeeze_scans/`, `wt_scans/`, `trend_scans/`, `bounce_rs_scans/`, and dashboard HTML files.

## Main Domains

- Circuit limits: `main.py` fetches NSE surveillance action data and writes `index.html`, `NSE_Circuit_Limits.md`, and `nse.csv`.
- NSE data layer: `fetch_data.py` plus `ohlc_db.py`; Kite credentials and token refresh are handled through `ema-compression-scanner/kite_auth.py`.
- US data layer: `fetch_us_data.py` plus `us_ohlc_db.py`; no broker auth, yfinance-based.
- Momentum and ZLEMA scanners: `momentum_scanner.py`, `momentum_rs_weekly_scanner.py`, `ema25_zl_scanner.py`, `weekly_zl_scanner.py`, `zl_squeeze_scanner.py`, `fno_zlema25_scanner.py`.
- WaveTrend and confluence: `wavetrend_scanner.py`, `wt_bullcross_scanner.py`, `wt_squeeze_dashboard.py`, `us_wt_bullcross_scanner.py`, `us_zl_squeeze_scanner.py`.
- Breadth monitor: `scanners/breadth_monitor.py`, `scanners/net_thrust_wavetrend.py`, `scanners/sma200_context.py`, and `data/breadth_history.csv`.
- Bounce-RS: `scanners/bounce_rs_scanner.py` and `run_bounce_rs_scanner.py`; depends on fresh breadth history.
- Consolidation tracker: `consolidation/` contains indicators, quality, imminence, tiers, and daily scanner orchestration.
- Institutional footprint: `institutional_footprint_scanner.py` scores broad NSE accumulation footprint from OHLCV, delivery%, CMF, volume, price structure, and RS; outputs `institutional_footprint_scans/`.
- Capital rules: `capital/` contains regime throttle, slots, time stops, and catalyst calendar utilities.
- Fundamental context and KG: `fundamental_context/`, `kg_company_summary.py`, Telegram ingestion/parser/resolver files, and company/peer tooling under `tools/`.

## Daily Operating Flow

The broad Windows orchestrator is `run_all_scanners.ps1`.

Typical sequence:

1. `run_fetch_data.ps1` refreshes Kite token and NSE OHLCV.
2. NSE scanners run from cached SQLite data.
3. `ema-compression-scanner/run_scanner.ps1` runs the EMA compression scanner.
4. WT, RS high-line, trend, circuit-limit, US fetch, US scanners, dashboards, catalyst bot, and scan status mailer run.
5. `run_all_scanners.ps1` triggers the separate scheduled task `NSE_BreadthMonitor`.
6. `run_breadth_monitor.ps1` runs `fetch_data.py --all`, updates breadth dashboard/history, then runs Bounce-RS and rebuilds WT squeeze dashboard.

`run_consolidation_scanner.ps1` is a separate consolidation tracker scheduled task and commits `results/` plus `consolidation_scans/`.

`fetch_delivery.py` can fetch one date or a resumable historical range:

```powershell
python fetch_delivery.py --date 2026-07-06
python fetch_delivery.py --from 2025-01-01 --to 2026-07-07
python fetch_delivery.py --from 2025-01-01 --to 2026-07-07 --stats
```

It writes `.ohlc_data/market.db` tables `delivery` and `delivery_backfill_progress`; the DB stays local and must not be committed.

`institutional_footprint_scanner.py` is currently manual only:

```powershell
python institutional_footprint_scanner.py
```

It calls TradingView screener for universe selection, reads OHLCV/delivery from local SQLite through `ohlc_db.py`, and writes latest+dated Markdown reports under `institutional_footprint_scans/`.

## Data and Secrets

- Local-only or ignored: `.env`, `.ohlc_data/market.db`, `.us_ohlc_data/us_market.db`, `.company_cache/`, `.telegram_session*`, `.telegram_state.json`, `logs/`, `.claude/`, `.code-index/`.
- The root `.env` exists locally and may contain credentials; do not print or commit it.
- Kite credentials expected by `ema-compression-scanner/kite_auth.py` include `KITE_API_KEY`, `KITE_API_SECRET`, `KITE_ACCESS_TOKEN`, `KITE_USER_ID`, `KITE_PASSWORD`, and `KITE_TOTP_SECRET`.
- Telegram and mail runners may rely on user-level environment variables such as `DISCORD_WEBHOOK_URL` and `GMAIL_APP_PASSWORD`.

## Tests and Quality

- Test suite lives in `tests/`.
- Preferred focused command: `python -m pytest tests/test_<area>.py -v`.
- Full suite command: `python -m pytest`.
- Lint config is `ruff.toml`; ignores `E741`, `E402`, and `E701` intentionally.
- `.pre-commit-config.yaml` exists, but hooks are disabled for this repo. Commits should use `git commit --no-verify`.
- Do not add tests to generated scan output folders. Add tests under `tests/` for pure logic and scanner orchestration behavior.

## Handoff Rules For Any Agent

- Start with `git status --short`.
- Read this file and `CLAUDE.md` before changing scanner behavior.
- Preserve existing generated-output disclaimer behavior. New Markdown or HTML files need the disclaimer.
- Keep changes narrow. Many scanner thresholds are trading-system assumptions; update docs/tests when changing them.
- For new scanners, follow existing patterns:
  - Load OHLCV through `ohlc_db.py` or `us_ohlc_db.py`.
  - Emit dated output plus latest output where established.
  - Add SEBI disclaimer to generated Markdown/HTML.
  - Add a PowerShell runner if it is intended for scheduling.
  - Add focused tests for pure indicator logic and orchestration edges.
- For Pine changes, follow existing plan files under `docs/superpowers/plans/` and validate in TradingView. Local Python tests do not validate Pine syntax.

## Active Roadmap Context

- Consolidation tracker phases 1, 2, 3, and 5 appear implemented:
  - `consolidation/indicators.py`
  - `consolidation/quality.py`
  - `consolidation/imminence.py`
  - `consolidation/tiers.py`
  - `consolidation/consolidation_scanner.py`
  - `capital/regime_throttle.py`
  - `capital/time_stops.py`
  - `capital/slots.py`
  - `capital/catalyst_calendar.py`
- Phase 6 Pine work (Sec 12) is now **complete**: `pine_scripts/Consolidation_Panel.pine` (Indicator 1, merged 2026-07-07) + `pine_scripts/Consolidation_PreBreak_Alerts.pine` (Indicator 2, pre-existing).
- Phase 7 (`research/half_life_backtest.py`) not started.
- `capital/time_stops.py` / `capital/slots.py` exist but are not wired to any live position tracker (no `signals.db` yet, by design — see spec Sec 6/9).
- Full spec is in `research/consolidation_capital_efficiency_spec.md`, now tracked on `main`.

- Institutional footprint scanner MVP exists with regime throttle and A/B/C action rank, but is not production-scheduled. Next useful items: optional HTML/dashboard integration, optional PowerShell runner/commit flow, and calibration/backtest of ICS thresholds.

## Quick Takeover Checklist

1. Run `git status --short`.
2. Inspect any file you plan to edit with `git diff -- <file>` first.
3. Confirm whether the task touches generated outputs, scanner logic, runner scripts, or Pine.
4. Run targeted tests for touched Python modules.
5. Update `HANDOFF.md` when adding a new workflow, scheduled runner, package, or active in-progress handoff item.
6. If committing, use `git commit --no-verify`.

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
