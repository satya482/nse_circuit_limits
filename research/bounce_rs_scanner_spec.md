# Bounce-RS Scanner — Spec

**Module:** `scanners/bounce_rs_scanner.py`  
**Interface:** `run(universe_df, as_of) -> pd.DataFrame`  
**Status:** Design complete; implementation pending validation  
**Last updated:** 2026-07-04

---

## 1. Purpose

Identify trending NSE stocks exhibiting positive relative strength (RS) during a `ratio_5d` breadth dip, and firing a setup trigger on or after the bounce. The scanner is a **timing + RS confluence layer** — it answers: *"which Stage 2 stocks should I enter now that the breadth tide is turning?"*

---

## 2. Conceptual Model

```
Breadth dip (ratio_5d ≤ 0.65)
        ↓
Stocks holding above EMA50 despite sell-off   ← RS positive relative to NiftyMidSml400
        ↓
ratio_5d starts bouncing (now > threshold + 0.05)
        ↓
Setup trigger fires on today's bar (NR7 / IB / Pocket Pivot)
        ↓
Scanner emits ranked output → entry list
```

**Key insight:** Stocks that decline less than the benchmark during a breadth dip are showing latent institutional demand. When breadth recovers, these lead first and fastest.

---

## 3. Three-Layer Filter Cascade

### Layer 1 — Breadth Gate (market-level)

| Parameter | Value | Notes |
|---|---|---|
| `RATIO_DIP_THRESHOLD` | 0.65 | ratio_5d ≤ this defines a dip bar |
| `MIN_DIP_BARS` | 2 | dip must persist ≥ N consecutive bars |
| `BOUNCE_MIN` | 0.05 | ratio must have risen ≥ this from dip low |

**Logic:**
- Scan breadth history for the most recent block of ≥ `MIN_DIP_BARS` bars at/below threshold
- Current bar must be **above** threshold (bounce in progress, not still in dip)
- Rise from dip low must be ≥ `BOUNCE_MIN`
- If no valid dip-bounce found → return empty DataFrame (market not in regime)

**Research questions:**
- [ ] Is `0.65` too tight? Check how often ratio stays between 0.6–0.7 vs. clean breaks below 0.6. Consider loosening to `0.70`.
- [ ] `MIN_DIP_BARS = 2` may generate noise on shallow one-day dips. Validate against breadth history CSV — how many 2-day vs 3-day+ dips appear?
- [ ] Should bounce be measured as absolute (current value) or relative to dip low? Current implementation uses `current - dip_low ≥ BOUNCE_MIN`. Alternative: `current / dip_low ≥ 1.08`.

---

### Layer 2 — RS Filter (stock-level)

**Definition:**  
`RS_dip = stock_return_during_dip - benchmark_return_during_dip`

Where:
- `stock_return = close_at_dip_end / close_at_dip_start - 1`
- `benchmark_return` = same calculation for `NIFTY_MIDSML_400`
- Dip window = `[dip_start_date, dip_end_date]` from Layer 1

**Pass criterion:** `RS_dip > 0` (stock fell less than benchmark, or rose while benchmark fell)

**EMA Type classification during dip:**

| Type | Condition | Action |
|---|---|---|
| A | Held above EMA21 throughout dip | Accept — strongest |
| B | Dipped below EMA21 but close > EMA21 today | Accept — reclaiming |
| C | Broke below EMA50 at any point during dip | Skip |

**Research questions:**
- [ ] EMA21 vs ZLEMA25 — current spec uses EMA21 for simplicity. Should Type A/B use ZLEMA25 instead to match the primary entry methodology?
- [ ] RS threshold at `0.0` is binary. Consider tiered scoring: RS > +2% gets bonus points, RS > 0% baseline, RS -1% to 0% borderline.
- [ ] Minimum close price and ATR filter to exclude illiquid stocks that show false RS (stock simply didn't trade during dip days).
- [ ] Dip window alignment: if `dip_start` date is before OHLCV history for that stock, skip or use available window?

---

### Layer 3 — Setup Trigger (stock-level, today's bar)

Three setup types detected on the current bar:

#### Pocket Pivot
- Today's volume > max down-volume day in prior 10 bars (`POCKET_PIVOT_LB = 10`)
- Close ≥ EMA10 × 0.99 (at or near EMA10)
- Score: 3

#### NR7 + Inside Bar (combo)
- Today's range = smallest of last 7 bars (`NR_PERIOD = 7`)
- Today's high < yesterday's high AND today's low > yesterday's low
- Score: 3

#### NR7 alone
- Today's range = smallest of last 7 bars
- Score: 2

#### Inside Bar alone
- Today's high < yesterday's high AND today's low > yesterday's low
- Score: 1

#### None
- Score: 0 — stock passes Layers 1+2 but no compression trigger yet
- Still emit in output but lower rank — useful for watchlist building

**Research questions:**
- [ ] Should scanner emit `NONE` setups at all, or hard-filter to setups only? Options: (a) emit all with flag, (b) emit only if `setup_score > 0`.
- [ ] Pocket Pivot definition: Qullamaggie uses volume > any single down-volume day. Current uses `max`. Validate this is correct.
- [ ] Three-Weeks Tight (3WT) — worth adding. Definition: close within 1.5% of prior two weekly closes. Requires weekly OHLCV or weekly resample from daily.
- [ ] VCP detection is complex (requires multi-week pivot analysis). Out of scope for v1; flag as v2 addition.

---

## 4. Composite Score Formula

```
score = min(RS_dip% × 1.0, 10)    # RS quality:      0–10 pts (capped)
      + (3 if ema_type == 'A' else 1)  # EMA hold quality: 1 or 3 pts
      + bounce_magnitude × 5           # Breadth bounce:   proportional
      + setup_score                    # Setup trigger:    0–3 pts
```

**Research questions:**
- [ ] Weight calibration: RS is currently dominant. Should EMA type have a higher weight (e.g. 5 pts for A vs 2 for B)?
- [ ] Should `bounce_magnitude × 5` be capped? A bounce from 0.6 to 1.4 gives 4.0 pts here — is that proportional to signal quality?
- [ ] Consider adding `ratio_10d > 0.8` as a bonus point (regime confirmation).
- [ ] RS percentile rank within the universe on that dip window may be a more robust metric than raw RS delta.

---

## 5. Data Dependencies

### SQLite (`data/market.db`)

| Table | Columns needed | Notes |
|---|---|---|
| `daily_ohlcv` | symbol, date, open, high, low, close, volume | 260-day lookback default |

**Research questions:**
- [ ] Confirm benchmark symbol string. Possible values: `NIFTY_MIDSML_400`, `NIFTY_MIDSML400`, `^NIFTYMIDSML400`. Query `SELECT DISTINCT symbol FROM daily_ohlcv WHERE symbol LIKE '%MIDSML%'` to confirm.
- [ ] Confirm `daily_ohlcv` table name matches actual schema. May be `ohlcv`, `price_data`, or `eod_prices` depending on Kite ingest script.
- [ ] Volume column: confirm it stores actual traded volume, not notional.

### Breadth CSV (`data/breadth_history.csv`)

| Column | Type | Notes |
|---|---|---|
| `date` | date | daily |
| `ratio_5d` | float | core metric |
| `ratio_10d` | float | regime confirmation |

**Research questions:**
- [ ] Data integrity: 2026-06-26 row is known broken (`total_eligible=10`). Scanner must skip or impute this row. Safest: filter rows where `total_eligible < 100`.
- [ ] CSV vs SQLite: consider moving breadth history into `market.db` for consistency.

---

## 6. Output Schema

| Column | Type | Description |
|---|---|---|
| `symbol` | str | NSE ticker |
| `rs_during_dip_%` | float | Outperformance vs benchmark during dip |
| `ema_type` | str | A / B (C already filtered out) |
| `setup` | str | POCKET_PIVOT / NR7_IB / NR7 / INSIDE_BAR / NONE |
| `dip_low_ratio` | float | Lowest ratio_5d value in dip block |
| `ratio_5d_now` | float | Current ratio_5d |
| `bounce_mag` | float | Current ratio - dip low |
| `score` | float | Composite rank score |

**Downstream consumers:**
- Rajan Mehta (Tape Reader) persona for triage
- Chart Whisperer for ZLEMA25/EMA21 entry confirmation
- WaveTrend scanner cross-reference for OS bullcross confirmation

---

## 7. Integration Points

### Regime Guard

```python
if results.empty:
    # ratio_5d not in bounce regime — do not force entries
    # Log: "Bounce-RS: no valid dip-bounce window as of {as_of}"
```

### Position Sizing Override

When `ema_type == 'A'` and `setup in ['POCKET_PIVOT', 'NR7_IB']`:
- Use ¾ to full position (₹11,250–₹15,000 risk)

When `ema_type == 'B'` or `setup == 'NONE'`:
- Use ½ position (₹7,500 risk) — add second half on ratio_5d crossing 1.0

### Breadth Monitor Sync

| ratio_5d level | Position sizing multiplier |
|---|---|
| 0.65 → 0.80 | 0.5× |
| 0.80 → 1.00 | 0.75× |
| > 1.00 | 1.0× |

---

## 8. Validation Tests to Write

```python
# test_bounce_rs_scanner.py

def test_no_bounce_returns_empty():
    # Inject breadth where ratio_5d is currently IN dip (not bouncing)
    # run() should return empty DataFrame
    pass

def test_rs_filter_removes_underperformers():
    # Stock that fell more than benchmark during dip should be excluded
    pass

def test_ema_type_c_excluded():
    # Stock that broke EMA50 during dip should not appear in output
    pass

def test_pocket_pivot_detection():
    # Construct OHLCV where today's volume > all down-day volumes in prior 10
    pass

def test_score_ordering():
    # Highest RS + Type A + Pocket Pivot should rank above lower combos
    pass

def test_broken_breadth_row_handled():
    # Row with total_eligible=10 should not corrupt dip detection
    pass
```

---

## 9. v2 Enhancements (Backlog)

| Feature | Priority | Notes |
|---|---|---|
| RS percentile rank | High | Rank each stock's dip RS within universe — more robust than raw delta |
| Three-Weeks Tight detection | Medium | Requires weekly resample from daily OHLCV |
| WaveTrend OS confirmation | Medium | Cross-reference `wavetrend_scanner.py` for BULL_OS_PPV on same stock |
| Dip depth vs recovery speed | Low | Stocks recovering faster than the dip-speed may have stronger momentum |
| Alert integration | Low | Kite Connect webhook or Telegram alert when scanner emits on live bar |
| Historical backtest | High | Run scanner as-of each trading day in 2024–2025; measure forward returns at +5/+10/+20 days |

---

## 10. Known Risks / Guard Rails

- **Look-ahead bias:** `dip_end` must use only dates strictly ≤ `as_of`. Never use future closes to define the dip window.
- **Timezone:** All timestamps must be `Asia/Kolkata` tz-aware. Use `IST.localize()` not `tz_convert()` on naive timestamps.
- **Benchmark availability:** If `NIFTY_MIDSML_400` is missing from DB on a date, RS calculation returns `NaN` → stock is excluded. Log a warning.
- **Circuit-frozen stocks:** Stocks frozen in upper/lower circuit may show misleading RS. Cross-reference circuit limit data if available.
- **Minimum data guard:** Skip stocks with < 60 bars of OHLCV history to avoid EMA warm-up errors.
