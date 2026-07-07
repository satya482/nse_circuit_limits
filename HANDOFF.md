> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Repo Handoff

Last reviewed by Codex: 2026-07-07.
Last reviewed by Claude Code: 2026-07-07 (see "Current Worktree State" below).

This repository is a Windows-first scanner and dashboard suite for NSE and US equities. It is actively maintained by multiple agents, especially Claude Code and Codex. Treat this file as the neutral takeover map; `CLAUDE.md` remains the deeper scanner operations manual.

## Current Worktree State

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
