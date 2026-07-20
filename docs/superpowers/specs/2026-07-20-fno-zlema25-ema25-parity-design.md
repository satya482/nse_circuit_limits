> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# F&O ZLEMA25 EMA25-Scanner Parity Design

## Goal

Bring `fno_zlema25_scanner.py` to gate, enrichment, and report-density parity with `ema25_zl_scanner.py` while keeping the NSE F&O universe, F&O report paths, and existing PowerShell runner.

The finished scanner will classify eligible NSE F&O stock underlyings into current ZLEMA25 uptrends and downtrends, with direction-specific age and price change for both sides.

## Scope

The change includes:

- Reusing the production analysis, gates, metadata, and Markdown presentation from `ema25_zl_scanner.py`.
- Restricting candidates to the NSE `SECURITIES IN F&O` universe returned by `fno_universe.py`.
- Preserving `fno_zlema25_scans/fno_zlema25_scans.md`, dated snapshots, and `run_fno_zlema25_scanner.ps1`.
- Replacing the existing five-bar event report with current ZLEMA25 Uptrend and Downtrend tables plus symmetric age buckets.
- Adding focused tests and updating `HANDOFF.md`.

The change does not alter the broad `ema25_zl_scanner.py` default output, the NSE F&O universe-fetching policy, scheduled-task registration, or other scanners.

## Architecture

### Reuse boundary

`ema25_zl_scanner.py` remains the source of truth for:

- TradingView eligibility filters and float-share metadata.
- Benchmark-relative-strength calculations and gates.
- Float-trap hard gating and SAFE/CAUTION labels.
- ZLEMA25 calculation and the established turn-age and change-percentage convention.
- BB/KC squeeze, liquidity, weekly-RS, Strong Start/RVOL, CMF, delivery, company-label, and circuit-limit enrichment.
- Table layout and TradingView watchlist bucketing.

The shared analysis and report functions will accept minimal optional direction and presentation values. Existing defaults must reproduce the current broad EMA25 ZL report unchanged. The F&O mode adds direction-aware fields and renders Uptrend and Downtrend rather than changing the broad scanner's Rising and Watch contract.

`fno_zlema25_scanner.py` becomes a thin orchestration adapter. It obtains the authoritative F&O symbols, intersects them with the broad scanner's TradingView-eligible symbols, calls the shared analyser for each remaining symbol, and asks the shared report builder for an F&O-labelled report.

This avoids a second copy of indicator and enrichment logic. No new shared framework or package is introduced.

### Universe and eligibility flow

The candidate flow is:

1. `fno_universe.get_fno_symbols()` fetches or loads NSE `SECURITIES IN F&O` stock underlyings using its existing 30-day cache.
2. `ema25_zl_scanner.get_watchlist()` supplies NSE common-equity eligibility and float-share data using the same TradingView query as the broad scanner.
3. The scanner takes the intersection, preserving the NSE F&O source order. TradingView may exclude an F&O symbol through the shared price or market-cap filters, but it can never add a non-F&O symbol.
4. Each intersected symbol is analysed against the same benchmark and gates as the broad scanner.

The report records the NSE F&O source count and the post-intersection eligible count so exclusions are visible.

### Analysis parity

The F&O scan uses the current `ema25_zl_scanner.py` settings without redefining them:

- Price greater than Rs 50.
- Market capitalization from Rs 1,000 Cr through Rs 5 Lakh Cr.
- One-week price-change gate off.
- Price-above-EMA25 gate off.
- Daily relative-strength line above its rising daily EMA21.
- Float-trap AVOID results excluded.
- At least 60 daily bars and sufficient benchmark overlap.

ZLEMA25 continues to use the repository formula:

```text
EMA1 = EMA(close, 25)
ZLEMA25 = 2 * EMA1 - EMA(EMA1, 25)
```

Results are split by the current ZLEMA25 slope:

- Uptrend: latest ZLEMA25 is greater than the preceding value.
- Downtrend: latest ZLEMA25 is less than the preceding value.
- Flat: latest ZLEMA25 equals the preceding value; reported in the summary count and omitted from both directional tables.

For an uptrend, `ZL Age` searches backward for the latest non-positive-to-positive slope change. For a downtrend, it searches backward for the latest non-negative-to-negative slope change. Age includes the turning bar, so a direction that starts on the latest candle is `1d`.

`ZL Chg%` compares the latest close with the close immediately before that direction's turning candle. Both ages retain the broad scanner's 60-bar cap; when no matching turn exists inside the window, the age displays `60d+` and change uses the oldest close in that window.

The previous independent recent-event lists are removed: every analysed symbol belongs only to its current direction, except an exactly flat slope, which belongs to neither table.

## Report

The latest and dated report files remain:

- `fno_zlema25_scans/fno_zlema25_scans.md`
- `fno_zlema25_scans/fno_zlema25_scans_YYYY-MM-DD.md`

The report uses the standard Markdown SEBI header and footer and identifies the universe as NSE F&O underlyings sourced through `fno_universe.py`.

Its content matches the broad scanner's information density while adding symmetric direction reporting:

- Scan-definition table with all active and inactive gates.
- ZLEMA25 Uptrend, Downtrend, and Flat counts.
- One TradingView-importable watchlist with direction-prefixed sections for `1 DAY`, `2 DAYS`, `3 DAYS`, `4-5 DAYS`, `6-10 DAYS`, `11-15 DAYS`, and `15 DAYS+`.
- Uptrend and Downtrend tables with Symbol, ZL Age, ZL Chg%, Label, Day Chg, Close, Squeeze, and Circuit columns.
- Symbol sub-tags for float-trap status, liquidity, weekly RS EMA9 confirmation, Strong Start/RVOL, CMF, and delivery when available.
- Individual Uptrend and Downtrend watchlist copy blocks by ZLEMA age bucket.

Rows keep the broad scanner's age-first ordering. The shared builder remains responsible for exact formatting so future presentation fixes benefit both reports.

## Error handling and writes

- Failure to obtain an NSE F&O universe follows the existing `fno_universe.py` cache fallback and terminal error behavior.
- Failure to load the benchmark is fatal and produces a non-zero scanner exit.
- TradingView eligibility-query failure is fatal; silently scanning without price, market-cap, or float metadata would violate parity.
- Individual symbol analysis failures follow the broad scanner's current skip behavior.
- Both latest and dated Markdown outputs are written only after the complete report is built.
- The PowerShell runner continues to stop on a non-zero scanner exit and stage only the F&O report outputs.

## Testing and verification

Focused tests will prove:

- The intersection contains only NSE F&O symbols and preserves F&O order.
- Non-F&O TradingView results cannot enter the scan.
- Price/market-cap-ineligible or metadata-missing F&O symbols do not bypass shared eligibility.
- The adapter passes the shared float value and benchmark to the shared analyser.
- A fresh uptrend and fresh downtrend each report age `1d`.
- Ongoing uptrends and downtrends increment their own ages and use the close before their respective turn for `ZL Chg%`.
- Reversals move a symbol into only its new current-direction table and reset age to `1d`.
- Exact flat slopes appear only in the Flat summary count.
- The report uses the F&O title and universe label while rendering Uptrend/Downtrend tables, tags, columns, direction-prefixed sectioned watchlists, and symmetric age buckets.
- The broad builder's default title and universe label remain unchanged.
- Latest and dated report paths remain unchanged.
- Generated Markdown includes the required `SEBI registered` disclaimer.

Implementation follows test-driven development: add focused failing tests, observe the expected failures, make the smallest production changes, and rerun focused tests. Final verification includes the related EMA/F&O tests, the complete pytest suite, PowerShell syntax parsing, `git diff --check`, and a local scanner run when the existing data and network-backed TradingView query are available.

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
