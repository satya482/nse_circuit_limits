# Multi-period RS Leaders implementation plan

For educational use; consult a SEBI registered investment advisor.

Approved design: NSE common equity, price > Rs50, market cap Rs1,000 crore to
Rs5 lakh crore. Benchmark NIFTY MIDSML 400. Rolling 5/21/63/126 benchmark trading
sessions, ratio-relative returns, per-period percentiles and positive-RS top-decile
leaders. Preserve full rankings and group leaders by number of qualifying periods.

- [x] Add failing numerical and report tests in tests/test_rs_leaders_scanner.py.
- [x] Implement rs_leaders_scanner.py: date-aligned calculations, deterministic
  tie-aware percentiles, short-history N/A, stale-symbol exclusions, Markdown and
  sortable/filterable HTML. Reuse ohlc_db and disclaimer/tv_watchlist helpers.
- [x] Add run_rs_leaders_scanner.ps1 after RS_WeeklyEMA9 in the production runner.
  Propagate scanner failures before staging only this scanner's outputs.
- [x] Run focused tests, local production scanner test run, PowerShell parser,
  broader regression tests and git diff --check. Inspect generated data and HTML.
- [x] Update HANDOFF.md with output paths, method and validation results.

Validation: 12 focused tests and 651 full-suite tests passed; five pre-existing
pandas warnings. PowerShell syntax passed. Two live runs agree on price date
2026-10-28 and 1,266 ranked stocks. Generated HTML controls tested with Node;
browser visual inspection unavailable. User authorized scoped commit/push after
verification. Actual 1,266-row dashboard data and JavaScript controls also passed.

Output: rs_leaders_scans/rs_leaders_latest.md, dashboard/rs_leaders.html, and
rs_leaders_scans/rs_leaders_latest.json (previous-session ranks, keyed by price
date; rerunning a date does not erase rank changes).

No new price fetch or order placement. TradingView supplies current universe;
existing local OHLC supplies returns. Expose data dates, coverage and the fact
that local price history has not been independently corporate-action audited.
No EMA or liquidity inclusion gate. Percentiles use average ties on a 0-100
scale; a singleton gets 100. Missing periods do not count as leadership.
