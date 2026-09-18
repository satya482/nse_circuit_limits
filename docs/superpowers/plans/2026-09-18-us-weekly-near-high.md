> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# US Weekly Near-High Implementation Plan

**Goal:** Build the approved weekly page and integrate with NSE_AllScanners.
**Architecture:** US generator selects and aggregates, shared renderer displays;
PowerShell orchestrator schedules after existing US refresh.
**Tech:** Python/pandas, TradingView, us_ohlc_db, Lightweight Charts, PowerShell.

- [x] Tests first: aggregation, partial weeks, 52-week high, strict EMA40,
  bucket boundaries, stale stocks, SPY RS and weekly renderer settings.
  Run `python -m pytest tests/test_us_near_52w_high_chart_dashboard.py -v`.
- [x] Implement `to_weekly(df)`, `select_weekly(ohlc_map, as_of)`,
  `get_universe()` and `main()` in us_near_52w_high_chart_dashboard.py.
  Aggregate open:first/high:max/low:min/close:last/volume:sum. Selection:
  `high.tail(52).max()` and `close.ewm(span=40, adjust=False).mean()`.
- [x] Add shared renderer `rs_for_all_exchanges=False`, `weekly=False`,
  `subtitle=''` options. Weekly high period 52; view 24 months; week labels
  and TradingView interval W. Daily defaults unchanged.
- [x] Add run_us_near_52w_high_chart_dashboard.ps1; wire after successful
  US_FetchData. Fix native Python exit propagation in the fetch runner.
- [x] Focused/full pytest, PowerShell parser, real generation, browser availability checked (no connected browser),
  git diff --check; update HANDOFF.md. Preserve unrelated working changes.

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
