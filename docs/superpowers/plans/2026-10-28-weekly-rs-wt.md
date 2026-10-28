# Weekly RS EMA21 + WT1 scanner implementation plan

For educational use; consult a SEBI registered investment advisor.

Approved rules: NSE common equities, price > Rs50, market cap Rs1,000 crore to
Rs5 lakh crore; weekly RS EMA21 strictly rising AND weekly WT1 strictly rising.
RS = stock close / NIFTY MIDSML 400 close * 1000. WT uses HLC3, EMA10 channel,
EMA21 smoothing and the existing shared WaveTrendCalculator. Include the current
developing week, updated daily. No 52-week-high, EMA200, float, liquidity, WT zero
line, WT2, or manual-list bypass gates. Return every qualifying stock.

- [x] Write failing tests in tests/test_weekly_rs_wt_scanner.py for weekly OHLC
  aggregation, partial weeks, independent numerical indicator parity, strict
  slopes, below-zero WT recovery, missing/stale/short data, reports and charts.
- [x] Create weekly_rs_wt_scanner.py. Reuse the RS Leaders universe query, local
  ohlc_db access, WaveTrendCalculator, shared chart renderer and disclaimers.
  Require 22 weekly bars (EMA21 period plus previous observation); use all loaded
  history up to 1,500 daily bars. Seed EMA with adjust=False as existing scans do.
  Aggregate OHLCV before computing indicators; label each weekly candle with its
  actual last observed trading date so the header shows the real price date.
  Exclude incomplete stock history relative to benchmark sessions, and invalid
  prices. Preserve outputs on failed universe/benchmark or total data failure;
  write a fresh empty report/dashboard on a valid zero-signal scan.
- [x] Generate weekly_rs_wt_scans/weekly_rs_wt_scans.md and
  dashboard/weekly_rs_wt.html together from one selection, with TradingView block,
  indicator values and slopes, industry-grouped weekly charts, RS and WT panes.
  Fail before output replacement if any qualifying chart cannot be rendered.
- [x] Add run_weekly_rs_wt_scanner.ps1 to run_all_scanners.ps1 after RS_Leaders.
  Propagate Python failures; stage only the two outputs and publish through the
  existing git retry helper. No separate scheduled task or message delivery.
- [x] Run focused tests, shared renderer regressions, PowerShell parser, live
  scanner test run, output parity checks, and full pytest. Update HANDOFF.md.

Architecture: one self-contained scanner module creates both artifacts. Shared
renderer remains unchanged; the weekly frames and benchmark passed to it match
the scanner's calculation history exactly. Original Near-52W scanner is unchanged.

Validation: 19 new tests; 670 full-suite tests pass (five existing pandas warnings).
PowerShell parser passed. Live run through 2026-10-28: 87 qualifiers, report/chart
symbol parity and both positive slopes verified for all records; 38 have WT1
below zero. Embedded JSON, pane array lengths, actual price dates, chart vendor
asset and JavaScript syntax checked. Browser visual inspection unavailable.
