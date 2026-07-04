# NSE Delivery % Conviction Marker — Design Spec
**Date:** 2026-07-04

## Overview

NSE full bhavcopy publishes deliverable-quantity % (`DELIV_PER`) per EQ-series stock, separately from Kite's OHLCV feed. This data is fetched daily, stored in a new SQLite table, and surfaced as a spike marker (`DEL68%(T-1)`) on the Symbol column of all 5 existing Symbol-marker scanners — same rollout pattern as the recent CMF marker.

Pine Script is explicitly **out of scope**: delivery % is not derivable from OHLCV and TradingView's NSE data feed doesn't carry it, so Pine has no way to compute or fetch it live. Python-side only.

Data is inherently ~1 trading day behind price scanners (bhavcopy for day T publishes ~6:30 PM, after the 4:xx PM scanner runs) — tag string always makes this explicit with a `(T-1)` suffix.

---

## Data Source

NSE full bhavcopy: `https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_DDMMYYYY.csv`

Filter `SERIES == 'EQ'`. Relevant columns: `SYMBOL`, `DATE1`, `TTL_TRD_QNTY`, `DELIV_QTY`, `DELIV_PER`.

---

## New Table — `market.db`

```sql
CREATE TABLE delivery (
  symbol TEXT,
  date DATE,
  ttl_trd_qty INTEGER,
  deliv_qty INTEGER,
  deliv_pct REAL,
  PRIMARY KEY (symbol, date)
)
```

Same DB as `ohlc` table (not a separate file) — one connection point, mirrors existing convention.

---

## New Script — `fetch_delivery.py`

- Reuses `main.py`'s NSE session/`User-Agent` warm-up pattern (archives host may still need a realistic UA; warm-up against `nseindia.com` first if archives 403s without it).
- Downloads today's bhavcopy CSV, filters `SERIES=='EQ'`, strips column whitespace (NSE CSV headers have padding).
- Upserts into `delivery` table (`INSERT OR REPLACE`).
- On fetch failure (404 — bhavcopy not yet published, or blocked): log, exit non-zero. Missing day ≠ fatal — downstream `deliv_tag()` just returns `''` for that date.

## New Runner — `run_fetch_delivery.ps1`

- Scheduled ~6:15 PM IST (after bhavcopy publish, before `NSE_BreadthMonitor` 5:30 PM fallback would already be done — this is later, standalone).
- Logs to `logs/`.
- Chains directly into `backfill_delivery_markers.py` on success.

---

## New Functions — `ohlc_db.py`

Placed next to `cmf_days()` / `cmf_tag()`, same file, same try/except → safe-default convention.

```python
DELIV_SPIKE_N = 20        # baseline window, trading days
DELIV_SPIKE_MULT = 1.5    # today must exceed baseline * mult to count as spike

def load_delivery(symbol: str, lookback: int = 60, db_path: Path = DB_PATH) -> pd.DataFrame | None:
    """Return (date, deliv_pct) from delivery table, oldest-first. None if missing/empty."""

def deliv_spike(df: pd.DataFrame, n: int = DELIV_SPIKE_N, mult: float = DELIV_SPIKE_MULT) -> tuple[float, float] | None:
    """
    Returns (today_pct, baseline_pct). baseline = mean of PRIOR n days,
    STRICTLY excluding today's row (df.iloc[-(n+1):-1]) — no look-ahead.
    Spike condition: today_pct > baseline_pct * mult.
    None if fewer than n+1 rows.
    """

def deliv_tag(symbol: str, n: int = DELIV_SPIKE_N, mult: float = DELIV_SPIKE_MULT) -> str:
    """
    '' if no spike / insufficient data / symbol not in delivery table.
    'DEL{today_pct:.0f}%(T-1)' if spike.
    Binary flag, NOT always-on (unlike cmf_tag) — only appears on genuine spike days,
    keeps Symbol column readable.
    """
```

---

## Wiring — Symbol Cell, 5 Files (same as CMF rollout)

| File | Change |
|------|--------|
| `wt_bullcross_scanner.py` | Append `deliv_tag(symbol)` to `extras` list (alongside `cmf_tag`) |
| `ema25_zl_scanner.py` | Append to existing `<sub>` subline |
| `weekly_zl_scanner.py` | Append to existing `<sub>` subline |
| `trend_scanner.py` | Append to existing `<sub>` subline |
| `rs_highline_scanner.py` | Append to existing `<sub>` subline |

Empty string from `deliv_tag()` → no visual change to existing subline (same silent-omit contract as `cmf_tag`).

This wiring is **permanent** — every future scanner run (starting tomorrow's normal 4:xx PM run) picks up the tag automatically from whatever's latest in the `delivery` table.

---

## New Script — `backfill_delivery_markers.py`

One-time-per-day patch for scanner outputs that already ran today, *before* delivery data existed:

1. For each of the 5 scanners' `_YYYY-MM-DD.md` and `_latest.md`: read file, for each data row find the Symbol cell, strip any existing `DEL{n}%(T-1)` substring (regex, idempotent), look up `deliv_tag(symbol)`, append if non-empty, rewrite file.
2. Skip entirely (leave files untouched) if today's `delivery` table has zero rows — never write a partial/broken file.
3. Re-run the 3 HTML generators (`wt_squeeze_dashboard.py`, `dashboard_generator.py`, `trend_dashboard.py`) so HTML regenerates from the now-patched `.md` files — no separate HTML-patching logic.
4. Git commit: `[scan YYYY-MM-DD] delivery backfill: N symbols tagged`.

Idempotent by construction — re-running same day produces identical output (strip-then-append, not blind append).

---

## Error Handling

- `fetch_delivery.py`: NSE archives may 404 (not yet published) or block bots — non-zero exit, PS1 logs it, doesn't crash other scheduled tasks.
- Missing/failed fetch → `deliv_tag()` returns `''` everywhere → scanners render exactly as they do today (no marker), same "no data ≠ bad stock" philosophy as `float_gate.py`.
- `backfill_delivery_markers.py` never writes an empty or partial file — skips patch step entirely if no data.

---

## Test — `tests/test_delivery.py`

Pytest, mirrors `tests/test_cmf.py`:
- Synthetic `deliv_pct` series with an engineered spike at a known bar → assert `deliv_spike` detects it, assert baseline excludes today's row (no look-ahead: mutate today's value, confirm baseline unchanged).
- No spike (flat series) → assert `None`-equivalent / `deliv_tag` returns `''`.
- `< n+1` rows → assert `deliv_spike` returns `None`.
- Idempotent backfill: run patch function twice on same sample `.md` content, assert byte-identical output.

---

## Files Touched

| File | Change |
|------|--------|
| `market.db` (schema) | New `delivery` table (migration handled by `fetch_delivery.py` on first run, `CREATE TABLE IF NOT EXISTS`) |
| `fetch_delivery.py` | New file |
| `run_fetch_delivery.ps1` | New file |
| `backfill_delivery_markers.py` | New file |
| `ohlc_db.py` | Add `load_delivery()`, `deliv_spike()`, `deliv_tag()` |
| `wt_bullcross_scanner.py` | Import `deliv_tag`, append to `extras` |
| `ema25_zl_scanner.py` | Import `deliv_tag`, append to subline |
| `weekly_zl_scanner.py` | Import `deliv_tag`, append to subline |
| `trend_scanner.py` | Import `deliv_tag`, append to subline |
| `rs_highline_scanner.py` | Import `deliv_tag`, append to subline |
| `tests/test_delivery.py` | New file |
| `CLAUDE.md` | Add `run_fetch_delivery.ps1` to run table (per scanner-conventions.md new-scanner checklist) |

No Pine Script changes — out of scope per design decision above.
