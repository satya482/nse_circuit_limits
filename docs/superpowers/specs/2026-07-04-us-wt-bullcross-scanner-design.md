# US WaveTrend Bull Cross Scanner — Design

Date: 2026-07-04

## Purpose

Port the existing NSE `wt_bullcross_scanner.py` to US equities (NYSE/NASDAQ), reusing the
US data pipeline that already exists in this repo (`fetch_us_data.py` → `.us_ohlc_data/us_market.db`
→ `us_ohlc_db.py`) rather than building a new one.

## Data source

- OHLCV: `us_ohlc_db.load_ohlc_many(symbols, lookback=400)` — same SQLite DB the existing
  `us_zl_squeeze_scanner.py` reads from. No new fetch script needed; `fetch_us_data.py` already
  backfills/deltas this DB daily at 4:40 PM IST via `run_us_fetch_data.ps1`.
- Watchlist: TradingView screener, US market, **must mirror** the universe `fetch_us_data.py`
  backfills or lookups return `None` for out-of-range symbols:
  - `exchange` in `[NASDAQ, NYSE]`, `type == stock`, `typespecs has common`
  - `close > 5`
  - `market_cap_basic` between $300M and $10B
  - `average_volume_10d_calc > 300,000`
  (Same query as `us_zl_squeeze_scanner.py::get_watchlist()`.)
- Benchmark: `SPY`, already tracked in the DB. RS line = `(stock_close / SPY_close) * 100`
  (×100 scale, matching `us_zl_squeeze_scanner.py` convention — NOT the NSE ×1000 scale).

## Signal logic

Reuse `wavetrend_scanner.WaveTrendCalculator` unmodified — it's already market-agnostic
(operates on any OHLCV DataFrame). Same 5-level bull rank hierarchy as the NSE scanner
(external contract per `scanner-conventions.md`, never renumbered):

| Rank | Signal | Condition |
|---|---|---|
| 5 | BULL_OS_PPV | deep oversold cross (wt2 ≤ −60) + Pocket Pivot Volume |
| 4 | BULL_ANY_PPV | any cross + PPV |
| 3 | BULL_OVERSOLD | deep oversold cross |
| 2 | BULL_OS_L2 | soft oversold cross (wt2 ≤ −53) |
| 1 | BULL_ANY_MID | mid-range cross, no PPV |

**No RS gate** — mirrors the NSE scanner's explicit design choice ("WT captures pre-RS-turn
reversals; filtering on RS would kill the best setups"). RS state/percentile shown as
informational context only.

Per-stock context columns (all reused from NSE scanner logic, all self-contained — no new deps):
- ZLEMA25 direction + days-since-turn + % gain since turn
- BB(20,2.0,SMA) inside KC(20,1.5,SMA ATR) squeeze flag
- RS state (weak/strong/transition) vs SPY + IBD-style percentile rank across the scanned universe
- C/AvgC (close ÷ EMA10) ratio + rising flag
- RVOL (today vol ÷ 20d avg) + "strong start" (gap-up-and-held) flag
- Earliness score (0–100): squeeze(40) + RS-transition(30) + ZL-freshness(0–20) + C/AvgC-freshness(0–10)

Dropped (NSE-only, no US equivalent exists): circuit limits, float-trap gate (`float_gate.py`
is hardcoded to ₹ Crores), `stock_labels.json` labels, trend-scanner cross-reference star.

## Output

- `us_wt_scans/us_wt_bullcross_latest.md` + `us_wt_scans/us_wt_bullcross_YYYY-MM-DD.md`
  (both written same run, per repo convention — never hand-edited)
- `us_wt_scans/us_wt_bullcross_dashboard.html` — standalone dark-theme render of the same
  categorized tables (Squeeze Breakout / Major / Oversold / Mid-range), overwritten each run,
  no dated copy (matches `wt_squeeze_dashboard.html` pattern). No cross-scanner confluence logic.
- Both files include the SEBI disclaimer header/footer (`disclaimer.py`), matching the existing
  precedent set by `us_zl_squeeze_scanner.py` — kept for consistency across US scanner outputs
  in this repo even though the disclaimer text is India-specific.
- Timestamps: IST, per repo-wide backtesting-integrity rule, same as all other scanners
  (`*Generated YYYY-MM-DD HH:MM IST*`).

## Ops

- New `run_us_wt_bullcross_scanner.ps1`, mirroring `run_us_zl_squeeze_scanner.ps1`: logs to
  `logs/us_wt_bullcross_scanner_YYYY-MM-DD.log`, runs the Python script, then
  `git add us_wt_scans/` + commit (`us-wt-bullcross scan YYYY-MM-DD`) + push.
- New standalone scheduled task, not part of `run_all_scanners.ps1` (follows existing US-scanner
  precedent of separate schtasks entries): registered for **5:00 PM IST**, after the existing
  US pipeline (`US_FETCH_DATA` @ 4:40 PM, `US_ZL_SQUEEZE` @ 4:50 PM).
- `CLAUDE.md` run table gets a new row for `run_us_wt_bullcross_scanner.ps1`.

## Error handling

Same pattern as NSE scanner: `analyse()` wraps per-stock computation in try/except, returns
`None` on failure (skip stock, don't crash the run). Missing SPY in DB → scanner logs the
same "run fetch_us_data.py first" error `us_zl_squeeze_scanner.py` already uses and exits early.

## Testing

Smoke test: run the script against the existing populated `.us_ohlc_data/us_market.db`,
confirm both `.md` files write with a disclaimer, non-empty header/table structure, and
`*No signals.*` fallback when a category is empty (never an empty table with only headers).
