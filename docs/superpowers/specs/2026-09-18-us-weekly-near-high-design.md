> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# US weekly near-high charts

Approved in conversation: existing US universe; weekly selection and candles;
close strictly above weekly EMA40 and within 30% of the rolling 52-week HIGH;
include partial week; SPY RS; retain chart features; run with NSE_AllScanners.

Universe: NYSE/NASDAQ common stocks, $300M-$10B cap, price > $5, average
10-day volume > 300,000. Current membership, exchange and industry from
TradingView; prices from us_ohlc_db. No NSE float or manual-list gates.

Aggregate OHLCV to Monday-labelled weeks, retaining partial weeks. Require
52 observed weeks; adjust=False EMA40; existing distance buckets and 0.01%
at-high tolerance. All indicators computed on weekly bars. Existing renderer
gets weekly configuration and explicit US benchmark opt-in; daily defaults
unchanged. Weekly view: 24 months, 52-bar high, week-change labels, weekly
TradingView links. EMA40 added to configurable overlays. Indicators requiring
longer history remain unavailable until enough actual bars exist.

Atomic output: dashboard/us_near_52w_high_charts.html, plus auditable markdown
report. Display data date and generation date. Reject missing/stale SPY, empty
universe and total data failure. Freshness uses the latest completed NYSE
session from exchange-calendars, including holidays and early closes. The
52-week high projection advances by weeks on weekly charts. Exclude stocks missing the benchmark session.
Valid zero qualifiers writes a current empty page.

Run immediately after successful US_FetchData in NSE_AllScanners; no separate
task. Check native Python exits and publish only generated outputs using
existing Git helpers. Validate aggregation, boundaries, SPY alignment, failure
paths, daily regressions, PowerShell syntax, real generation and browser UI.

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
