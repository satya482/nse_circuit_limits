# Union Watchlist 30-Day Liquidity Gate — Design

Date: 2026-08-28

## Purpose

Require every verified member of the inclusive Union Watchlist to have at least
₹10 crore of average daily traded value. Apply the rule only to the Union
Watchlist and its chart dashboard; do not change any standalone scanner's
eligibility criteria or output.

## Liquidity Formula

For each union candidate, use the latest 30 completed daily bars:

```text
average_volume_30d = SMA(volume, 30)
average_traded_value_cr = average_volume_30d × latest_close ÷ 10,000,000
```

The symbol passes when `average_traded_value_cr >= 10.0`.

This matches the selected TradingView-style composition: its Average Volume
30D is `ta.sma(volume, 30)`, combined with the current regular-session price.
TradingView documents those fields separately:

- https://www.tradingview.com/support/solutions/43000745917-how-do-we-calculate-average-volume/
- https://www.tradingview.com/support/solutions/43000635853-what-does-price-mean-in-the-screener/

Zero-volume sessions are valid observations and remain in the 30-session SMA.
Exactly ₹10 crore passes because the comparison is inclusive.

## Scope and Ordering

The existing five-source union remains inclusive across:

1. EMA55 Cross;
2. EMA25 ZL;
3. Minervini Trend Template;
4. Trend Scanner;
5. Weekly RS EMA9.

After fresh source files are parsed, collect the deduplicated candidate symbols
and load their OHLCV in one `ohlc_db.load_ohlc_many(..., lookback=30)` call.
Determine the allowed symbol set, intersect every available source set with it,
then call the existing `build_union()`. Confluence counts and tier labels are
therefore calculated only after the liquidity gate.

Do not apply the gate to the standalone EMA55 Cross table/watchlist or modify
any upstream source file. The union chart dashboard automatically inherits the
gate because it parses the Union Watchlist section from the EMA55 report.

## Unverified Data Policy

The user selected fail-open behavior for data that cannot prove or disprove the
threshold. Retain a candidate and list it in a Union-section warning when any of
these conditions applies:

- symbol absent from the OHLC batch result;
- fewer than 30 daily rows;
- latest bar date is not the report date;
- missing, non-numeric, or non-finite latest close or 30-session volume;
- latest close is non-positive or any volume is negative.

Complete valid data below ₹10 crore is not unverified; it is excluded.

The warning lists every retained-unverified symbol alphabetically. The Union
section also reports the number excluded below threshold. These lines stay
outside TradingView fenced blocks so existing report parsers remain unchanged.

## Components

### Liquidity calculation

Add a pure helper in `ema55_cross_scanner.py` that accepts one OHLCV DataFrame
and the report date. It returns the calculated crore value for 30 valid,
current daily bars, or `None` when the data is unverified.

### Source-set filter

Add a pure helper that accepts source sets and the batch OHLC mapping. It
returns:

- source sets intersected with verified passers plus retained-unverified names;
- alphabetically sorted below-threshold exclusions;
- alphabetically sorted retained-unverified symbols.

The helper must not mutate its input source sets.

### Report integration

`build_markdown()` performs the single batch load and applies the filter before
`build_union()`. `build_union_section()` receives liquidity results and renders
the threshold/exclusion summary plus the retained-unverified warning.

If fewer than two fresh sources are available, the existing no-union behavior
remains authoritative and no liquidity load is required.

## Error Handling

An unavailable database or omitted symbols produces an empty OHLC mapping.
Under the selected policy, candidates are retained and named as unverified; the
report generation does not fail. Unexpected per-symbol numeric/data errors are
also treated as unverified rather than aborting the whole scanner.

## Testing

Focused tests will cover:

- 30-session SMA volume multiplied by the latest close;
- exact ₹10 crore inclusion and below-threshold exclusion;
- zero-volume sessions participating in the SMA;
- missing, stale, invalid, and 29-row histories retained as unverified;
- source-set inputs remaining unmodified;
- confluence tiers recalculated after low-liquidity removal;
- alphabetized warning symbols and exclusion counts in the Union section;
- no OHLC batch load when fewer than two source sets can form a union;
- standalone EMA55 Cross rows remaining unaffected.

Run the focused EMA55 tests, the full repository suite, and `git diff --check`.
When current scanner inputs and local OHLCV are available, run the normal EMA55
scanner and Union chart generator, then verify the report/dashboard counts and
required SEBI disclaimers before publishing.

---

*Warning: I am not a SEBI registered investment advisor. All content is for
educational and informational purposes only and does not constitute investment
advice. Please consult a SEBI registered investment advisor before making any
investment decisions. Investments in securities market are subject to market
risks, read all related documents carefully before investing.*
