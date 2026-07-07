> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# SPEC-1: NSE Institutional Footprint Scanner

## Purpose

Build a local end-of-day NSE scanner that highlights possible institutional accumulation using data this repo already stores: OHLCV, delivery percentage, volume, price structure, money flow, and relative strength.

This is not a new app. It is one repo-native scanner/report that reuses the existing market database, runner conventions, and disclaimer constants.

## Existing Repo Assets To Reuse

- `fetch_data.py` populates `.ohlc_data/market.db` with OHLCV.
- `fetch_delivery.py` downloads NSE full bhavcopy delivery data into the existing `delivery` table.
- `ohlc_db.py` is the data access layer:
  - `load_ohlc()` / `load_ohlc_many()`
  - `load_delivery()`
  - `deliv_spike()` / `deliv_tag()`
  - `cmf_series()` / `cmf_tag()`
  - `liq_tag()`
- `disclaimer.py` owns mandatory report disclaimers:
  - `SEBI_MD_HEADER` / `SEBI_MD_FOOTER`
  - `SEBI_HTML_BANNER` / `SEBI_HTML_FOOTER`
- Existing scanner pattern:
  - flat root-level Python scanner
  - output folder with `*_latest.md` and dated `*_YYYY-MM-DD.md`
  - optional PowerShell runner if scheduled
  - focused tests under `tests/`

## Non-Goals

- No new `src/` package.
- No new standalone SQLite database.
- No duplicate bhavcopy importer.
- No React, web server, cloud DB, or intraday data.
- No Plotly or per-stock chart pages in MVP.
- No publish script in MVP; use existing runner/git patterns if scheduling is later added.

## MVP Output

Create:

```text
institutional_footprint_scanner.py
institutional_footprint_scans/institutional_footprint_latest.md
institutional_footprint_scans/institutional_footprint_YYYY-MM-DD.md
tests/test_institutional_footprint.py
```

Optional after MVP:

```text
dashboard/institutional_footprint.html
run_institutional_footprint_scanner.ps1
```

All generated `.md` and `.html` files must include the `SEBI registered` disclaimer string through `disclaimer.py` constants.

## Data Contract

Use existing tables only.

```text
ohlc(symbol, date, open, high, low, close, volume)
delivery(symbol, date, ttl_trd_qty, deliv_qty, deliv_pct)
```

Do not create `daily_prices`, `daily_delivery`, `scores`, or `indicators` tables for MVP. If score history is needed later, prefer CSV outputs first; add a table only after a clear query need exists.

Benchmark:

```text
NIFTY MIDSML 400
```

This must match the symbol already used by existing scanners.

## Universe

MVP should use the same TradingView screener style as `consolidation/consolidation_scanner.py` and `wt_bullcross_scanner.py`:

```text
exchange = NSE
type = stock
typespecs has common
close > 50
market_cap_basic between configured lower/upper bounds
```

Default market-cap band:

```text
Rs 1,000 Cr to Rs 5,00,000 Cr
```

Keep thresholds as module constants in the scanner. Do not add YAML config until a second real consumer needs it.

## Delivery Enhancements

Add pure helper functions in `institutional_footprint_scanner.py` unless they become useful to other scanners; only then move them into `ohlc_db.py`.

### `delivery_sparkline(values, lookback=20)`

- Return exactly 20 Unicode block characters when at least 20 values exist.
- Use only the latest 20 values.
- Normalize within those 20 values.
- Return `""` with fewer than 20 values.
- If all values are equal, return 20 middle blocks.

### `delivery_percentile(values, lookback=252, min_periods=60)`

- Latest value is compared against prior history only.
- Use up to the previous 252 sessions.
- Return rounded integer percentile.
- Return `None` if prior history is shorter than `min_periods`.

### `consecutive_high_delivery_days(values, mult=1.5, baseline_window=20)`

- Count backward from latest row.
- A day qualifies when its delivery percentage is at least `mult` times the prior `baseline_window` average.
- Stop on first non-qualifying day.
- Display only when count is at least 2.

### `delivery_visual_tag(row)`

Compose a compact tag:

```text
DEL68% ▁▂▃▄▅▆▇█... P98 3D
```

Rules:

- Only show the tag when latest delivery is a spike.
- Add sparkline when available.
- Add `P<n>` when percentile is available.
- Add `<n>D` when consecutive high-delivery days >= 2.
- Keep it readable inside existing Markdown table cells.

## Indicators

Compute indicators directly from the loaded OHLCV DataFrame.

Price:

```text
EMA20, EMA50, EMA200
20-day high breakout
52-week high proximity
ATR14 if needed for context
```

Volume:

```text
avg_volume20
volume_ratio20
turnover_cr = close * volume / 1e7
avg_turnover20
turnover_ratio20
```

Money flow:

```text
CMF20 from ohlc_db.cmf_series()
OBV and OBV slope20 only if the first scoring pass needs more separation
```

Relative strength:

```text
20-day, 50-day, 100-day returns versus NIFTY MIDSML 400
cross-sectional RS percentile for today's scanned universe
RS trend: UP / FLAT / DOWN
```

## Institutional Campaign Score

The score is a simple 0-100 point total. It is not a model.

### Delivery Score: 30

| Condition | Points |
|---|---:|
| Latest delivery above prior 20-day average | 6 |
| Delivery ratio >= 1.5 | 6 |
| Delivery percentile >= 90 | 6 |
| Consecutive high-delivery days >= 3 | 6 |
| 20-day delivery slope positive | 6 |

### Volume Score: 20

| Condition | Points |
|---|---:|
| Volume ratio >= 1.5 | 6 |
| Turnover ratio >= 1.5 | 6 |
| Turnover >= Rs 5 Cr | 4 |
| Up day with above-average volume | 4 |

### Price Score: 20

| Condition | Points |
|---|---:|
| Close > EMA20 | 4 |
| Close > EMA50 | 4 |
| Close > EMA200 | 4 |
| 20-day breakout | 4 |
| Within 15% of 52-week high | 4 |

### Money Flow Score: 15

| Condition | Points |
|---|---:|
| CMF20 > 0 | 5 |
| CMF20 > 0.05 | 5 |
| OBV slope20 positive, if implemented; otherwise CMF rising | 5 |

### Relative Strength Score: 15

| Condition | Points |
|---|---:|
| RS percentile >= 90 | 8 |
| RS trend improving | 4 |
| Stock outperforming benchmark over 50 days | 3 |

## Rating

Use compact labels in reports.

```text
ICS >= 95  ELITE
ICS >= 85  STRONG
ICS >= 70  BUILDING
ICS >= 55  WATCH
else       IGNORE
```

## Lifecycle Stage

Use plain ASCII labels in code and reports.

```text
SEED          delivery percentile >= 85 and no breakout
BUILDING      ICS >= 70, delivery slope positive, CMF20 > 0, no breakout
BREAKOUT      20-day breakout, delivery percentile >= 90, volume_ratio20 >= 1.5
MARKUP        close > EMA20 and EMA50, RS percentile >= 90, ICS >= 85
DISTRIBUTION  price down, volume_ratio20 >= 1.5, CMF20 < 0, OBV/CMF weakening
```

When multiple stages match, prefer this order:

```text
DISTRIBUTION > BREAKOUT > MARKUP > BUILDING > SEED
```

## Markdown Report

One Markdown report is enough for MVP.

```text
institutional_footprint_scans/institutional_footprint_latest.md
institutional_footprint_scans/institutional_footprint_YYYY-MM-DD.md
```

Sections:

```text
Fresh Institutional Entries
Elite / Strong Accumulation
Building Positions
Breakouts With Delivery
Distribution Warnings
Watchlist, if a watchlist file already exists later
```

Each row should show:

```text
Symbol
Name / liquidity tag if available
ICS
Rating
Stage
Delivery tag
RS percentile / trend
CMF20
Volume ratio
Turnover
Reason
TradingView link
```

Reason should be generated from the top 2-4 facts, for example:

```text
Delivery P98, 3D high delivery, CMF positive, RS leader
```

## Optional HTML Report

HTML is second phase, not MVP.

If added, use one static file:

```text
dashboard/institutional_footprint.html
```

Requirements:

- Mobile-first cards.
- Dark mode default.
- Vanilla JavaScript search/filter.
- No external runtime.
- Include `SEBI_HTML_BANNER` and `SEBI_HTML_FOOTER`.

Do not add Plotly until the Markdown scanner has proven useful.

## Implementation Plan

### Phase 1: Pure Helpers And Tests

Implement and test:

```text
delivery_sparkline
delivery_percentile
consecutive_high_delivery_days
assign_rating
assign_lifecycle
calculate_ics
```

Focused command:

```powershell
python -m pytest tests/test_institutional_footprint.py -v
```

### Phase 2: Scanner

Implement:

```text
get_universe()
analyse_symbol(symbol, df, bench_df, delivery_df)
run(universe_df, as_of) -> pandas.DataFrame
build_markdown(rows, as_of)
main()
```

Use `load_ohlc_many()` for the universe plus benchmark.

### Phase 3: Report Integration

Write latest and dated Markdown files with SEBI disclaimer constants.

Add a PowerShell runner only if the user wants this scheduled:

```text
run_institutional_footprint_scanner.ps1
```

### Phase 4: HTML Dashboard, Optional

Add only after the Markdown output has useful signal quality.

### Phase 5: Signal Tracking, Optional

Use generated report history or CSV snapshots first. Add a DB table only when repeated queries over historical signals become painful.

## Acceptance Criteria

MVP is complete when:

```text
1. `python institutional_footprint_scanner.py` runs from repo root.
2. It reads OHLCV and delivery data through `ohlc_db.py`.
3. It writes latest and dated Markdown reports.
4. Every generated Markdown report contains `SEBI registered`.
5. ICS is always between 0 and 100.
6. Missing delivery or benchmark data skips the symbol or degrades clearly, without crashing the whole scan.
7. Focused pytest coverage passes.
```

## First Implementation Prompt

```text
Build Phase 1 and Phase 2 of `research/nse_institutional_footprint_plan_spec.md`.

Keep it repo-native:
- one root-level `institutional_footprint_scanner.py`
- one focused `tests/test_institutional_footprint.py`
- reuse `ohlc_db.py`, `fetch_delivery.py`, and `disclaimer.py`
- no new `src/` package
- no new SQLite schema
- no Plotly or HTML yet

Run:
python -m pytest tests/test_institutional_footprint.py -v
```

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
