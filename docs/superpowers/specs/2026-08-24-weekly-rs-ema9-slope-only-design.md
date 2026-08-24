> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Weekly RS EMA9 Slope-Only Scanner Design

## Goal

Change `rs_weekly_ema9_scanner.py` so qualification depends only on the weekly RS EMA9 being flat or rising. The daily RS line no longer needs to be above the weekly RS EMA9.

Use the EMA55 scanner's market-cap range: NSE common equity with price above Rs50 and market cap from Rs1,000 Cr through Rs5 lakh Cr. This change copies only the universe thresholds; it does not add the EMA55 scanner's float gate or price/EMA55 signal.

## Considered approaches

1. Update the weekly RS scanner directly. Replace its above-EMA age calculation with weekly slope age and adjust its existing TradingView universe thresholds. This is the selected approach because it keeps the scanner self-contained and changes only the requested behavior.
2. Reuse Minervini scanner internals. Its RS gate already checks weekly RS EMA9 slope without requiring RS above EMA9, but importing its private helpers would couple two independently scheduled scanners and still require separate age logic.
3. Add configurable legacy and slope-only modes. This preserves both behaviors but adds an unused configuration surface and ambiguous report/state semantics.

## Signal and age

Daily closes remain aligned with `NIFTY MIDSML 400`, resampled weekly, and converted to weekly RS as `(stock / benchmark) * 1000`. EMA9 continues to include the current partial week.

A symbol qualifies when its latest weekly RS EMA9 transition is non-falling within the existing `SLOPE_EPS` tolerance: `current EMA9 - prior EMA9 >= -SLOPE_EPS`. Daily RS position relative to EMA9 is informationally irrelevant and must not exclude the symbol.

`Age(w)` is the number of consecutive weekly EMA9 transitions, ending at the current partial week, that have each been flat or rising within the same tolerance. A newly qualifying transition has age 1. A falling transition has age 0 and is excluded.

The table continues to label a slope greater than `SLOPE_EPS` as `RISING`; a slope inside the tolerance band is `FLAT`. Results remain sorted by age ascending, then symbol.

## Outputs and compatibility

Keep the existing latest and dated Markdown reports, JSON previous-run state, CSV count history, HTML history dashboard, PowerShell runner, and `run_all_scanners.ps1` wiring. Update displayed definitions and labels so none claim that daily RS must be above EMA9 or that age is measured in trading days.

The state file may show a one-time expansion in additions after deployment because the qualification contract and market-cap universe both widen/change. History remains append-only by run date under its existing idempotent behavior.

## Testing

Focused tests will prove:

- A falling daily RS line below weekly EMA9 can still qualify when weekly EMA9 is flat/rising.
- Weekly slope age counts consecutive qualifying weekly transitions and resets to zero on the current falling transition.
- The TradingView market-cap thresholds match the EMA55 range.
- Report text uses slope-only qualification and weekly age terminology.

Run the focused weekly-RS scanner tests first, followed by the full Python test suite. No live scanner run is required unless network and local data access are explicitly used for verification.

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
