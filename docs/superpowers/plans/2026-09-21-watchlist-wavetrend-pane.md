> Educational information only. Consult a SEBI registered investment advisor before making investment decisions.

# Watchlist WaveTrend pane

Add a default-visible, independently toggleable WaveTrend pane below RS on `dashboard/charts.html`. Reuse the existing price-based WaveTrend calculator and `pine_scripts/Satya_All_Panel.pine`: HLC3 input, EMA10 channel/deviation, EMA21 WT1, SMA4 WT2, aqua/orange lines, lime bull crosses and red bear crosses. Show zero and the agreed +/-53 and +/-60 levels. No histogram. All crosses qualify regardless of zone.

Keep shared rendering opt-in so other dashboard callers retain their existing output behavior. Align the pane's dates, visible range and crosshair with the price and RS charts. Missing warmup values remain whitespace. Use the existing responsive pane sizing and non-interactive scrolling behavior.

1. Add focused tests for Pine-equivalent values, crosses, warmup and opt-in rendering; observe expected failures.
2. Add optional WT data and rendering to the shared chart generator; enable both in the TradingView dashboard caller.
3. Exercise generated JavaScript with a chart stub, including levels, markers, range sync and toggle behavior. Run focused and full tests.
4. Regenerate the requested dashboard using current watchlist membership and local OHLC. Verify embedded data and disclaimer, update HANDOFF, review the diff and publish the scoped change.
