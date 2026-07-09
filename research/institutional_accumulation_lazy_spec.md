> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# SPEC-1 (lazy): Institutional Accumulation — extend, don't rebuild

Full ambition doc: [`institutional_accumulation_intelligence_spec.md`](institutional_accumulation_intelligence_spec.md).
This is the buildable slice: extend `institutional_footprint_scanner.py`, not a new system.

## Why not the full spec

Full spec's §3/§5/§12/§13 propose a new SQLite schema, 5-script CLI, and a standalone GitHub
Pages site. ~70% of the scoring logic it describes (accumulation, delivery trend, RS, market
regime, base/structure, trigger/stop) already exists across `institutional_footprint_scanner.py`,
`consolidation/`, and `capital/`. Net-new signal work is 4 things. Everything else is a rename.

## What's reused (no new code)

| Full spec section | Already built at |
|---|---|
| §6.2 Relative Strength | `institutional_footprint_scanner.analyse_symbol` (`rs_raw_20/50`, `rs_trend`) |
| §6.3 Delivery Trend | `institutional_footprint_scanner.py` (`delivery_percentile`, `delivery_zscore`, `consecutive_high_delivery_days`) |
| §7.1 Accumulation Engine | `calculate_ics()` |
| §8.2/8.3 Grades/Stages | `assign_rating()` / `assign_lifecycle()` |
| §9 Trigger/Risk | `capital/time_stops.py` |
| Market regime (§8.1) | `capital/regime_throttle.py` |
| Base/structure/compression | `consolidation/quality.py`, `imminence.py`, `tiers.py` |
| Earnings gating | `capital/catalyst_calendar.py` |

## What's actually new (build this)

All four land inside `institutional_footprint_scanner.py` — same `row` dict `analyse_symbol()`
already builds, same `calculate_ics()` scoring, same `footprint_latest.md`/`.html`/`.csv` outputs.
No new files except one small sector module.

### 1. Absorption day flag
`row["absorption_day"]`: today's `(high-low)/close` in bottom 20% of its 20-day range AND
`delivery_ratio >= 1.5` AND close in upper half of today's range. Needs `open/high/low` added to
`row` (currently only `close`/`volume` derived — one extra df column read each).

### 2. Failed breakdown reclaim flag
`row["failed_breakdown_reclaim"]`: low broke `close.rolling(20).min()` intraday or by close within
the last 3 bars, and today's close is back above that level. Reuses the same rolling-20 window
`breakout20` already computes on the high side.

### 3. Failed breakout flag
`row["failed_breakout"]`: `breakout20` was true within the last 2 bars, upper wick
`(high-close)/(high-low) > 0.5`, and volume_ratio >= 1.5, but close never held above the breakout
level. Negative score impact in `calculate_ics()`.

### 4. Resistance pressure score
`row["resistance_touches"]`: count of closes within 1.5% of `close.rolling(60).max()` in the last
20 bars, without a close below it by more than the base-depth threshold. Add as a small
`calculate_ics()` bonus (repeated tests without breakdown = building pressure).

### 5. Sector synchronization (one new module: `sector_sync.py`)
Sector comes straight from the same TradingView query `get_universe()` already runs to build
the scan universe (`.select("name", "sector")`) — not the static
`NSE_500cr_15CrNotional10D_50rs_sector_industry.csv`. The CSV join was tried first and only
covered ~69% of the scanned universe (403/1295 rows landed `UNKNOWN`); switching to the live
TradingView field brought that to 0/1295. No new symbols table, no new dependency — same
`tradingview_screener` query already in use, one extra `.select()` column.

One `groupby("sector")` over the scan's own output rows: `% close_gt_ema20`, `% rs_trend == UP`,
`% ics >= 70`. Join back onto each row as `sector_score`. Runs once per scan, after `run()`
produces all rows, before `build_markdown`/`build_html`.

## Output

Extend existing `footprint_latest.md` / `footprint.html` columns with `sector_score`,
`absorption_day`, `failed_breakdown_reclaim`, `failed_breakout`, `resistance_touches`. Dated
`footprint_scans/footprint_YYYY-MM-DD.csv` is already the signal-history store (per existing
Phase 5 note) — that already gives the full spec's §15 backtest raw material for free; no new
`setup_events` table needed to start.

## Deferred — cut from MVP, revisit only when triggered

Mark each with `# ponytail: <reason> <revisit-trigger>` at the point it would land in code, so
`/ponytail-debt` can surface this list later without a separate tracker.

| Item | Why cut | Revisit when |
|---|---|---|
| New SQLite schema (`prices`/`indicators`/`scores`/`setup_events`) | `ohlc_db.py` + dated CSVs already cover this; adding tables is write-amplification for recomputable values | Recomputing indicators from `load_ohlc_many` in a scan run is measurably slow |
| Float Rotation (§7.7) | No free-float data source anywhere in this repo | A free-float feed shows up (fundamentals API, NSE disclosure scrape) |
| Volume-at-Price-in-base (§7.8) | Approximation of an approximation; no evidence it beats existing quality/imminence scores | Backtest on the 4 new signals shows base-quality alone is a weak discriminator |
| Historical Similarity Engine (§7.10) | Needs a real feature-vector history to compare against — none exists yet | After the 4 new signals + sector_score have run for ~3 months of dated CSVs |
| AI-generated explanation (§19) | Example text is a template f-string over fields already computed — no LLM call needed | User actually wants free-text variation, not a fixed template |
| Standalone GitHub Pages site (§10/§11) | `footprint.html` already has the dashboard pattern (dark cards, JS filter) | `footprint.html` gets too cluttered to add the new columns/sections |
| 5-script CLI + `run_daily.py` orchestrator (§12) | Every other scanner here is one script, one run | Some stage genuinely needs independent scheduling (unlikely) |

## Build order

1. ✅ Add `open`/`high`/`low` to `row` in `analyse_symbol()` (prereq for 1-4).
2. ✅ Absorption day + failed breakdown/breakout flags + resistance_touches → `calculate_ics()` bonus/penalty.
3. ✅ `sector_sync.py` — groupby, join `sector_score` onto rows.
4. ✅ Extend `build_markdown`/`build_html` — `Sector`/`Structure` columns, `structure_tag()` mirrors existing `delivery_visual_tag()` compact-tag convention.
5. Existing dated CSV already gives backtest raw material — nothing else to build for that.

MVP complete. 45 tests passing (`tests/test_institutional_footprint.py`, `tests/test_sector_sync.py`).
