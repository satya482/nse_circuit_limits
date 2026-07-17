> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# NIFTY 50 ZLEMA25 Trend Scanner Design

## Goal

Add a dedicated daily scanner that classifies the current NIFTY 50 constituents by ZLEMA25 direction, reports the age of each active direction, and presents uptrends and downtrends separately with the youngest trends first.

The scanner must follow the established `ema25_zl_scanner.py` report conventions without changing that scanner's existing broad-market workflow.

## Scope

The complete setup includes:

- `nifty50_zlema25_scanner.py` as a dedicated root-level scanner.
- A cached NIFTY 50 constituent file under `data/`.
- A PowerShell runner consistent with the repository's scheduled scanner runners.
- Registration in `run_all_scanners.ps1` after the daily OHLC refresh.
- A generated Markdown report under a dedicated scan-output directory.
- Focused tests for direction changes, age calculation, bucketing, sorting, report structure, and universe fallback.
- Updated operating notes in `HANDOFF.md` and `CLAUDE.md` where appropriate.

It does not add trading signals, entry/exit recommendations, alerts, dashboards, backtests, or non-NIFTY-50 symbols.

## Architecture

### Constituents

At runtime, the scanner attempts to download the official NSE NIFTY 50 constituent CSV. A successful response is validated before replacing the cached file: it must contain a recognized symbol column, yield a plausible constituent count, and contain unique non-empty NSE symbols.

If the refresh fails or validation rejects the response, the scanner uses the last valid cached CSV. If neither source yields a valid universe, the run fails clearly instead of silently scanning a partial or unrelated universe.

The cache makes scheduled runs resilient while allowing index rebalances to flow into later scans automatically.

### Market data

For every constituent, daily OHLCV is loaded through `ohlc_db.py`. The scanner requires enough history to form ZLEMA25 and determine the current trend age. A symbol with missing or insufficient history is listed in a skipped-symbol summary; it is not silently assigned a direction.

The scanner does not apply the broad scanner's market-cap, price, RS, liquidity, or float-trap exclusion gates. Every NIFTY 50 constituent with sufficient local data is classified.

### Indicator and direction

ZLEMA25 uses the repository's existing formula:

```text
EMA1 = EMA(close, 25)
ZLEMA25 = 2 * EMA1 - EMA(EMA1, 25)
```

Direction is based on the daily ZLEMA25 slope:

- Uptrend: current ZLEMA25 is greater than the previous bar's ZLEMA25.
- Downtrend: current ZLEMA25 is less than the previous bar's ZLEMA25.
- Flat: exact equality. Flat values are reported separately in the run summary and are not forced into either trend table.

An uptrend starts when the slope changes from non-positive to positive. A downtrend starts when the slope changes from non-negative to negative.

### Trend age and change

Age is the number of consecutive daily trading bars in the current direction, including the first direction-change bar. A new trend therefore has age `1d`.

Age is derived from available OHLC rows, not calendar days. Calculation scans backward through the current same-direction slope run. Unlike the existing broad scanner's capped lookback, the scanner should report the full age available in local history; only display bucketing groups older trends together.

Trend change percentage uses the close immediately before the direction-change candle as the base, matching the established ZLEMA uptrend convention:

```text
(latest close / close before trend start - 1) * 100
```

## Report

The output is `nifty50_zlema25_scans/nifty50_zlema25_scans.md` and includes the repository's standard Markdown SEBI header and footer.

The report contains scan time, universe source, requested/analysed/skipped/flat counts, indicator definition, and two tables:

1. `ZLEMA25 Uptrend Start and Age`
2. `ZLEMA25 Downtrend Start and Age`

Both tables are sorted by ascending age and then symbol. They follow the useful density of `ema25_zl_scanner.py`, with these columns:

| Column | Meaning |
|---|---|
| Symbol | TradingView-linked NSE symbol plus available informational tags |
| ZL Age | Consecutive trading bars in the current direction |
| ZL Chg% | Price change since the direction started |
| Label | Existing stock label, when available |
| Day Chg | Latest daily close change |
| Close | Latest close |
| Squeeze | Existing BB/KC squeeze status |
| Circuit | Existing circuit-limit display |

Informational tags may be shown when locally available, but none may exclude a constituent.

### Age buckets and TradingView watchlists

Uptrend and downtrend sections each use the established buckets:

- `1 DAY`
- `2 DAYS`
- `3 DAYS`
- `4-5 DAYS`
- `6-10 DAYS`
- `11-15 DAYS`
- `15 DAYS+`

Each direction gets a TradingView-importable sectioned watchlist and individual per-bucket copy blocks. Empty buckets are omitted. Symbols within a bucket are alphabetical for deterministic output.

## Runner and workflow integration

The PowerShell runner follows existing production conventions:

- Use the configured Python executable.
- Write dated logs under `logs/`.
- Return a non-zero exit code on scanner failure.
- Stage and publish only the dedicated generated-output directory, consistent with existing scanner runners.

`run_all_scanners.ps1` invokes the new scanner after `FetchData`, near the existing `EMA25_ZL` job, so it reads the refreshed local OHLC database.

No live fetch or scheduled-task registration is performed as part of unit tests.

## Error handling

- Reject malformed or implausibly small constituent downloads and preserve the prior cache.
- Fail the run if no valid current or cached universe exists.
- Continue past individual symbols with missing/insufficient OHLC data and summarize them.
- Surface unexpected calculation or report-generation failures with the symbol and a non-zero process exit.
- Write the final report atomically so a failed run cannot leave a partially written Markdown file.

## Verification

Focused tests will cover:

- ZLEMA25 parity with `ema25_zl_scanner.py`.
- First uptrend and downtrend bars have age `1d`.
- Ongoing direction increments age correctly.
- Up/down reversals reset age.
- Flat slope is excluded from both tables.
- Percentage change uses the close before the trend-start bar.
- Boundary values map to the expected age buckets.
- Both tables sort by age and symbol.
- Both direction watchlists use the required bucket sections.
- Valid remote constituents update the cache; invalid/unavailable remote data uses the cache.
- The report contains the required `SEBI registered` disclaimer text.

After focused tests, validation includes `git diff --check` and a local scanner run against the existing OHLC database. Network refresh behavior may be tested separately when network access is available; fallback behavior remains deterministic in tests.

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
