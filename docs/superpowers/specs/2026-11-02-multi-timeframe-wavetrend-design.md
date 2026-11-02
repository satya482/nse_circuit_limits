> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Multi-timeframe WaveTrend: approved design and usage

Approved in chat on 2026-11-02. Script: `pine_scripts/Satya_WT_Multi_Timeframe.pine`.

Paste the complete script into TradingView Pine Editor, save, and select Add to chart.
Use intraday or 1-day charts. Weekly, monthly, and multi-day charts are rejected.

## Behavior

- HLC3 WaveTrend: channel EMA10, average EMA21, WT2 SMA4; shared adjustable lengths.
- Daily, weekly, monthly WT1/WT2 calculated in their own source timeframes.
- Developing mode by default; closed-only mode uses the previous completed source
  candle, available at the beginning of the next period, without backdating.
- Developing higher-timeframe values/crosses can change before candle close and
  after reload. Historical bars cannot reconstruct every live intraperiod change.
- Daily blue, weekly orange, monthly purple by default. Direction color mode uses
  original WT1 green/red and WT2 blue/orange. Width distinguishes timeframes;
  WT1 is thicker than WT2. Source-period slopes determine direction colors.
- Reference levels: all (0, +60/+53/-60/-53), zero only, or hidden.
- Three translucent WT1-minus-WT2 areas and three cross-marker sets can be hidden.
  D circles, W diamonds, M squares; bullish green and bearish red.
- Repeated mapped source crosses generate one chart-bar pulse when first available.
  A developing cross can disappear or recur before source candle close.
- Optional price-candle coloring from Daily (default), Weekly, or Monthly crosses:
  bullish white, bearish yellow. It operates independently of plot visibility.
- No alerts, Pocket Pivot, or background shading.

## Implementation and validation plan

1. Create a separate Pine v6 file; preserve existing indicators and unrelated edits.
2. Calculate WT, prior source values, crosses, and source timestamps together.
3. Request current tuples with lookahead off; closed tuples offset all elements
   by one source candle and use lookahead on.
4. Wire display settings, six lines, three areas, three marker sets, and barcolor.
5. Review request offsets and source-context calculations; check whitespace and
   simulate repeated mapped cross pulses, including consecutive source periods.
6. TradingView acceptance: compile; compare each pair against the original on D/W/M
   with identical lengths; test on 15-minute and 1-day charts; toggle both candle
   modes and color modes; check all reference settings, visibility, and candle
   source choices. Closed crosses appear when the next source period begins.

Local checks do not compile or execute Pine. TradingView compilation, visual
comparison, and live/replay behavior remain manual acceptance checks.

Official reference: https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
