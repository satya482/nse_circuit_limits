> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Repo Handoff

Last reviewed by Codex: 2026-07-07.

This repository is a Windows-first scanner and dashboard suite for NSE and US equities. It is actively maintained by multiple agents, especially Claude Code and Codex. Treat this file as the neutral takeover map; `CLAUDE.md` remains the deeper scanner operations manual.

## Current Worktree State

Observed on 2026-07-07 before this handoff was added:

- Modified: `pine_scripts/Monthly_HL_projection.pine`
  - Existing diff changes the script from current/historical monthly high-low projection lines to monthly close projection lines while keeping boxes.
  - This appears to be in-progress user/Claude work. Do not revert without explicit instruction.
- Untracked: `docs/superpowers/plans/2026-07-07-consolidation-panel-pine.md`
  - Plan for `pine_scripts/Consolidation_Panel.pine`, a Pine v6 visual companion for the consolidation tracker.
- Untracked: `research/consolidation_capital_efficiency_spec.md`
  - Full consolidation and capital-efficiency system spec. It is referenced by `CLAUDE.md` and implementation plans.
- New from this handoff: `AGENTS.md` and `HANDOFF.md`.

Always rerun `git status --short` before making changes because Claude Code may be working in parallel.

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
- Phase 6 Pine work is planned but not complete in the observed worktree:
  - `docs/superpowers/plans/2026-07-07-consolidation-panel-pine.md` defines `pine_scripts/Consolidation_Panel.pine`.
  - Existing Pine companion alert script may already exist; inspect `pine_scripts/` before adding overlapping files.
- Full spec is in `research/consolidation_capital_efficiency_spec.md`, currently untracked at the time of this handoff.

## Quick Takeover Checklist

1. Run `git status --short`.
2. Inspect any file you plan to edit with `git diff -- <file>` first.
3. Confirm whether the task touches generated outputs, scanner logic, runner scripts, or Pine.
4. Run targeted tests for touched Python modules.
5. Update `HANDOFF.md` when adding a new workflow, scheduled runner, package, or active in-progress handoff item.
6. If committing, use `git commit --no-verify`.

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
