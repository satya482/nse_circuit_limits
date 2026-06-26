# NSE Breadth Monitor — Design Doc
_Date: 2026-06-26_

## Purpose

Bonde/Stockbee-style market breadth monitor for NSE equities. Provides **market timing / regime context** — answers "is the market environment supportive right now?" Replaces the existing `breadth_scanner.py` (% above SMA/EMA only) with a richer thrust/capitulation monitor.

**Separation of concerns:** this is a regime/timing layer, not a candidate-selection scanner. Existing execution scanners (`wt_bullcross_scanner.py`, `ema_compression_scanner.py`, etc.) are unaffected and not cross-referenced here (future integration, explicitly out of scope).

---

## Decisions Resolved

| # | Decision | Resolution |
|---|---|---|
| 1 | Universe | Broad — Kite instruments dump (`exchange=NSE`, `instrument_type=EQ`, excl. SME), ~2,000–2,500 symbols |
| 2 | Ratio thresholds (1.6 / 0.6) | Kept as named constants, flagged TODO: validate against NSE history |
| 3 | Composite score | Ships as `null` in v1 — column present, TODO: backtest weights before enabling |
| 4 | SMA200 circuit-gap correction | Deferred to v1.1, flagged as known limitation |
| 5 | Refresh automation | All local PS1, slots into existing 4:50 PM scanner schedule |
| 6 | History depth | 10 years (~2,500 bars) via Kite historical API backfill (Option A: extends SQLite) |
| 7 | Universe refresh cadence | Weekly (manual, Monday morning before market open) |
| 8 | Calendar heatmap | Implemented in v1 via custom canvas drawing |
| 9 | Migration | Fresh start — old `breadth_scanner.py`, `breadth_scans/breadth_history.csv`, `breadth_chart.html` deleted; SQLite backfill covers full history |

---

## File Layout

```
scanners/
  breadth_monitor.py             # core scanner + dashboard builder
data/
  breadth_universe.csv           # Kite instruments dump, broad NSE EQ (excl. SME)
  breadth_history.csv            # accumulating output, one row per (date, universe_tag)
dashboard/
  nse_breadth_monitor.html       # static Chart.js dashboard, served via GitHub Pages
scripts/
  refresh_breadth_universe.py    # weekly Kite instruments pull → breadth_universe.csv
run_breadth_monitor.ps1          # local PS1 runner, 4:50 PM schedule
```

**Retired (delete after migration):**
- `breadth_scanner.py`
- `breadth_scans/breadth_history.csv`
- `breadth_chart.html`

---

## Data Flow

```
Weekly (manual, Monday):
  scripts/refresh_breadth_universe.py
    → Kite instruments API (exchange=NSE, instrument_type=EQ, excl. '-' symbols)
    → data/breadth_universe.csv  (columns: symbol, exchange, instrument_type, name, generated_date)

Daily 4:50 PM (run_breadth_monitor.ps1):
  data/breadth_universe.csv
    → fetch_data.py (breadth symbols, lookback=2500) → .ohlc_data/market.db
    → scanners/breadth_monitor.py
        compute_daily_breadth(universe_df, as_of=today, ohlc_map)
        update_breadth_history(path, new_row)  → data/breadth_history.csv
        build_dashboard_html(history_df, nifty_df) → dashboard/nse_breadth_monitor.html
    → git add data/breadth_history.csv dashboard/nse_breadth_monitor.html
    → git commit "[scan YYYY-MM-DD] breadth-monitor: <up4>↑ <down4>↓ ratio5d=<x>"
    → git push
```

---

## Architecture

### `scanners/breadth_monitor.py`

```python
def compute_daily_breadth(
    universe_df: pd.DataFrame,
    as_of: date,
    ohlc_map: dict[str, pd.DataFrame]
) -> dict:
    """
    Single-day breadth snapshot. Pure function, no I/O.
    as_of strictly bounds all calculations — never reads closes after as_of.
    Returns dict matching breadth_history.csv schema.
    Regime/timing layer only — not a candidate-selection scanner.
    """

def update_breadth_history(history_path: str, new_row: dict) -> None:
    """
    Upsert new_row into breadth_history.csv keyed on (date, universe_tag).
    Idempotent: re-running same as_of overwrites, never duplicates.
    """

def build_dashboard_html(
    history_df: pd.DataFrame,
    nifty_df: pd.DataFrame
) -> str:
    """
    Builds static HTML dashboard. Data embedded as JSON.
    Returns HTML string; caller writes file.
    """
```

**Interface deviation from other scanners:** this module accumulates a rolling time series rather than emitting per-day candidate lists. Documented in module docstring and CLAUDE.md. Not an inconsistency — deliberate.

**OHLCV access:** exclusively via `ohlc_db.load_ohlc_many(symbols, lookback=2500)`. Never reads CSVs, yfinance, or external APIs directly. Repo convention.

**CLI modes:**
- No flag: runs `as_of=today`, appends/upserts one row to `data/breadth_history.csv`.
- `--backfill`: iterates all trading dates available in SQLite (oldest → newest), upserts a row for each. Used for one-time migration and recovery.

### `scripts/refresh_breadth_universe.py`

Standalone. Requires active Kite token. Filters: `exchange=NSE`, `instrument_type=EQ`, excludes symbols containing `-`. Writes `data/breadth_universe.csv` with `generated_date` header comment for staleness visibility.

### `fetch_data.py` change

After existing 962-stock delta fetch, runs a second pass for breadth universe symbols with `lookback=2500`. Same SQLite DB, same `ohlc_db.py` interface. First run is the one-time 10-year backfill (~28 min at Kite rate limits); subsequent runs are incremental delta.

---

## Core Metrics

### Guardrails (all metrics)
- `as_of` strictly bounds every calculation
- IST timezone explicit on all datetimes (`timezone(timedelta(hours=5, minutes=30))`)
- Circuit-frozen exclusion (v1): stock excluded from up4/down4 if `close == prev_close AND volume == 0`
  - `# TODO: integrate nse_circuit_limits API for precise frozen detection (v1.1)`
- If Kite call fails for a stock/day: log + exclude from denominator. Never substitute stale close silently.

### 4% Daily Movers
```
pct_1d(stock, t) = close[t] / close[t-1] - 1
up4_count(t)     = count(pct_1d >= 0.04, not circuit-frozen)
down4_count(t)   = count(pct_1d <= -0.04, not circuit-frozen)
total_eligible   = count(not circuit-frozen AND has prev_close)
```

### 5d / 10d Ratio
```
ratio_5d(t)  = sum(up4_count, t-4..t)  / max(1, sum(down4_count, t-4..t))
ratio_10d(t) = sum(up4_count, t-9..t)  / max(1, sum(down4_count, t-9..t))
```
Constants in code:
```python
THRUST_THRESHOLD = 1.6        # TODO: validate against NSE history before treating as production signal
CAPITULATION_THRESHOLD = 0.6  # TODO: validate against NSE history before treating as production signal
```

### Quarterly 25%+ Movers
```
pct_63d(stock, t)   = close[t] / close[t-63] - 1
up25_quarter(t)     = count(pct_63d >= 0.25)   # stocks with <63 bars excluded from this calc only
down25_quarter(t)   = count(pct_63d <= -0.25)
```

### % Above SMA200
```
sma200(stock, t)     = mean(close, t-199..t)   # plain SMA, min_periods=200
pct_above_sma200(t)  = above_sma200_count / total_eligible * 100
# Known limitation: circuit-gap days distort plain SMA. Flagged, deferred to v1.1.
```

### Composite Score
```python
composite_score = None  # v1: always null
# TODO v1.1: backtest normalization bounds (ratio_5d distribution, net thrust range)
#            against >=1 year real NSE history before enabling.
#            Mockup weights (0.40/0.40/0.20) and bounds (min(ratio,3)/3, net±600)
#            were arbitrary demo values — do not carry to production.
```

---

## Output Schema

`data/breadth_history.csv` — append/upsert, keyed on `(date, universe_tag)`:

| column | type | notes |
|---|---|---|
| `date` | str `YYYY-MM-DD` | IST trading date |
| `universe_tag` | str | `breadth_broad` (all rows v1) |
| `total_eligible` | int | denominator that day (excl. circuit-frozen) |
| `up4_count` | int | |
| `down4_count` | int | |
| `ratio_5d` | float | |
| `ratio_10d` | float | |
| `up25_quarter` | int | |
| `down25_quarter` | int | |
| `pct_above_sma200` | float | |
| `composite_score` | float, nullable | null in v1 |

**Idempotency:** re-running same `as_of` overwrites that row, never appends duplicate.

---

## Dashboard — `dashboard/nse_breadth_monitor.html`

Static HTML, Chart.js v4 + `chartjs-plugin-annotation` v3, vanilla JS. Data embedded as JSON at build time. Served via GitHub Pages at `satya482.github.io/nse_circuit_limits/dashboard/nse_breadth_monitor.html`.

### Color Tokens
```
Background:  #0a0e14    Panel:   #10151d    Border: #1c2530    Grid: #1a222d
Text:        #e8edf3    Muted:   #6b7785
Bull:        #1fd980    Bear:    #ff5577    Cyan:   #4dd9e8    Amber: #ffb454
```
Fonts: Space Grotesk (display) + JetBrains Mono (data) via Google Fonts CDN.

### 6 Panels (top → bottom, shared x-axis)

1. **Stat strip** — composite score gauge (shows `—` in v1), ratio_5d, today's up4/down4, pct_above_sma200. HTML stat cards, no canvas.
2. **Nifty 50 price** — line chart from SQLite `"NIFTY 50"` symbol, normalized. Triangle annotations: ↑ green at `ratio_5d >= THRUST_THRESHOLD`, ↓ red at `ratio_5d <= CAPITULATION_THRESHOLD`.
3. **Mirrored thrust bars** — `up4_count` green positive, `down4_count` red negative, zero axis shared. Chart.js bar chart.
4. **Ratio oscillator** — `ratio_5d` solid + `ratio_10d` dashed. Shaded annotation bands: ≥1.6 green, ≤0.6 red.
5. **% above SMA200** — line chart, dashed 50% reference line.
6. **Calendar heatmap** — custom canvas drawing. GitHub-style year grid. Each cell = one trading day, color mapped from `up4_count - down4_count` net: red (heavy selling) → neutral (#1c2530) → green (heavy buying).

---

## PS1 Runner

`run_breadth_monitor.ps1` — same pattern as `run_wt_bullcross_scanner.ps1`:
- Logs to `logs/breadth_monitor_YYYY-MM-DD.log`
- Runs `python scanners/breadth_monitor.py`
- Git adds `data/breadth_history.csv dashboard/nse_breadth_monitor.html`
- Commit: `[scan YYYY-MM-DD] breadth-monitor: <up4>↑ <down4>↓ ratio5d=<x.xx>`
- `git push`

Scheduled task: replace existing `NSE_BreadthScanner` schtask entry (same name, new script path), runs 4:50 PM Mon–Fri.

---

## Migration Steps (one-time, in order)

1. Run `scripts/refresh_breadth_universe.py` → `data/breadth_universe.csv`
2. Run extended `fetch_data.py` → fills SQLite with ~10 yr breadth universe history (~28 min)
3. Run `python scanners/breadth_monitor.py --backfill` → writes full `data/breadth_history.csv`
4. Verify `data/breadth_history.csv` row count and spot-check a few dates
5. Delete `breadth_scanner.py`, `breadth_scans/breadth_history.csv`, `breadth_chart.html`
6. Update schtask to point at `run_breadth_monitor.ps1`
7. Add breadth-monitor entry to `CLAUDE.md` run table
8. Add weekly universe refresh note to CLAUDE.md: `# Weekly (manual, Monday AM): python scripts/refresh_breadth_universe.py`

---

## Open TODOs (in code as comments)

- `THRUST_THRESHOLD` / `CAPITULATION_THRESHOLD`: validate against ≥1 yr real NSE breadth history
- Composite score weights: backtest normalization bounds before enabling
- Circuit-frozen detection: integrate `nse_circuit_limits` API (v1.1)
- SMA200 gap-day correction (v1.1)

---

## Acceptance Criteria (from spec §9)

- [ ] No look-ahead: `as_of` row uses only data through that day's close
- [ ] Re-running same `as_of` produces identical row, no duplicates
- [ ] `universe_tag` on every row; `total_eligible` doesn't silently drift from API failures
- [ ] Circuit-frozen stocks excluded from `up4`/`down4`, not counted as flat
- [ ] Ratio thresholds marked TODO, not treated as validated signals
- [ ] Dashboard renders from `data/breadth_history.csv` with no manual data massaging

---

## Out of Scope (v1)

- Composite score (placeholder weights, ships as null)
- SMA200 gap-day correction
- Cross-referencing breadth regime into EP/WaveTrend/compression scanner ranking
- GitHub Actions automation (all local PS1)
