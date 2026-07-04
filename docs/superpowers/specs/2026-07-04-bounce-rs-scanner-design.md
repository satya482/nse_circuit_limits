# Bounce-RS Scanner — Design

**Module:** `scanners/bounce_rs_scanner.py`
**Interface:** `run(universe_df, as_of) -> pd.DataFrame`
**Status:** Design approved, ready for implementation plan
**Date:** 2026-07-04
**Source spec:** `research/bounce_rs_scanner_spec.md` (research draft; this doc supersedes its open questions with decisions)

---

## 1. Purpose

Timing + RS confluence layer: identify NSE stocks with positive relative strength during a breadth (`ratio_5d`) dip, that fire a setup trigger as the dip bounces. Answers: "which Stage-2 stocks should I enter now that the breadth tide is turning?"

---

## 2. Architecture

Single file, three sequential filter layers + a composite score, following the pattern of other root-level scanners (`wt_bullcross_scanner.py`, `ema25_zl_scanner.py`) rather than the split-module pattern used by `ema-compression-scanner/` — scope here doesn't warrant the extra files.

Lives in `scanners/` (not repo root) alongside `scanners/breadth_monitor.py`, since it directly consumes `data/breadth_history.csv` and the breadth regime it produces — same directory groups the regime-dependent scripts.

```
run(universe_df, as_of):
    dip_window = find_dip_bounce(breadth_history_csv, as_of)     # Layer 1
    if dip_window is None:
        log("Bounce-RS: no valid dip-bounce window as of {as_of}")
        return empty DataFrame

    bench_ohlc = load_ohlc_many(["NIFTY MIDSML 400"])

    rows = []
    for symbol in universe_df.symbol:
        ohlc = load_ohlc(symbol, lookback=260)
        if len(ohlc) < 60: continue                              # min-data guard
        if ohlc.date.min() > dip_window.dip_start: continue       # short-history guard

        rs, ema_type = rs_and_ema_check(ohlc, bench_ohlc, dip_window)  # Layer 2
        if ema_type == "C" or rs <= 0: continue

        setup, setup_score = detect_setup(ohlc)                   # Layer 3, always computed

        rows.append({... , score: composite_score(...)})

    return pd.DataFrame(rows).sort_values("score", ascending=False)
```

---

## 3. Layer 1 — Breadth Gate

| Parameter | Value |
|---|---|
| `RATIO_DIP_THRESHOLD` | 0.70 |
| `MIN_DIP_BARS` | 2 |
| `BOUNCE_MIN` | 0.05 |

- Find most recent block of ≥2 consecutive bars with `ratio_5d ≤ 0.70`.
- Skip rows where `total_eligible < 100` (known-broken 2026-06-26 row) before scanning for dip blocks.
- Current bar must be **above** threshold, with `current_ratio_5d - dip_low_ratio ≥ 0.05` (absolute rise, not relative).
- No valid window → empty DataFrame (regime guard, not an error).

---

## 4. Layer 2 — RS Filter

`RS_dip = stock_return_during_dip - benchmark_return_during_dip`, benchmark = `"NIFTY MIDSML 400"` (Kite tradingsymbol, matches repo-wide convention), loaded via `load_ohlc_many`.

**Pass criterion:** `RS_dip > 0`.

**EMA basis: EMA20** (not EMA21, not ZLEMA25 — user decision; EMA20 matches the existing swing-scanner STRONG-condition convention rather than introducing a new indicator or overloading ZLEMA25, which is an entry-timing indicator, not a dip-hold floor).

| Type | Condition | Action |
|---|---|---|
| A | Held above EMA20 throughout dip window | Accept — strongest |
| B | Dipped below EMA20 but close > EMA20 today | Accept — reclaiming |
| C | Broke below EMA50 at any point during dip | Skip |

Dip window alignment: if a stock's OHLCV history starts after `dip_start`, **skip the stock** (not a truncated window) — a partial-window RS_dip isn't comparable to full-window RS_dip elsewhere in the ranking, and would corrupt score ordering (see §8 test).

---

## 5. Layer 3 — Setup Trigger

Computed for every stock that survives Layers 1+2, including `NONE` — rows are always emitted (not hard-filtered), since Layer 1+2 passers with no trigger yet are useful for watchlist building (per spec).

| Setup | Condition | Score |
|---|---|---|
| Pocket Pivot | vol > max down-vol day in prior 10 bars (`POCKET_PIVOT_LB=10`); close ≥ EMA10×0.99 | 3 |
| NR7 + Inside Bar | today's range = smallest of last 7 bars AND inside bar | 3 |
| NR7 alone | today's range = smallest of last 7 bars | 2 |
| Inside Bar alone | today's high < yesterday's high AND today's low > yesterday's low | 1 |
| None | no trigger | 0 |

Pocket Pivot definition confirmed as-is: "volume > max down-volume day" and "volume > any down-volume day" are mathematically equivalent — spec wording was just unclear, no logic change needed.

---

## 6. Composite Score

```
score = min(RS_dip% , 10)               # RS quality: 0–10 pts, capped
      + (3 if ema_type == 'A' else 1)   # EMA hold quality: 1 or 3 pts
      + min(bounce_magnitude * 5, 5)    # Breadth bounce: proportional, capped at 5
      + setup_score                     # Setup trigger: 0–3 pts
```

Weights unchanged from spec draft (RS-dominant); rebalancing deferred until a historical backtest exists (§9, already High priority backlog item) rather than guessed now. Bounce term is now explicitly capped at 5 to prevent a large ratio swing (e.g. 0.70→1.4+) from dwarfing RS/EMA/setup contributions.

---

## 7. Data Dependencies

- OHLCV: **`ohlc_db.load_ohlc()` / `load_ohlc_many()` only** — no raw SQL, no yfinance, no direct table access. Resolves spec's "confirm table name" questions: there is no raw table access in this codebase's scanner layer, only the `ohlc_db.py` API.
- Breadth: `data/breadth_history.csv`, columns confirmed present: `date, universe_tag, total_eligible, ratio_5d, ratio_10d` (verified against actual file).
- Benchmark symbol confirmed: `"NIFTY MIDSML 400"` (verified against `wt_bullcross_scanner.py:59`).

---

## 8. Output Schema

Unchanged from spec:

| Column | Type | Description |
|---|---|---|
| `symbol` | str | NSE ticker |
| `rs_during_dip_%` | float | Outperformance vs benchmark during dip |
| `ema_type` | str | A / B |
| `setup` | str | POCKET_PIVOT / NR7_IB / NR7 / INSIDE_BAR / NONE |
| `dip_low_ratio` | float | Lowest ratio_5d in dip block |
| `ratio_5d_now` | float | Current ratio_5d |
| `bounce_mag` | float | Current ratio - dip low |
| `score` | float | Composite rank score |

---

## 9. Integration Points

Unchanged from spec §7: regime guard (empty df when out of regime), position-sizing override table (EMA type × setup → risk fraction), breadth-monitor sync table (ratio_5d level → sizing multiplier).

---

## 10. Guard Rails (unchanged from spec §10)

Look-ahead bias (dip_end ≤ as_of strictly), IST-aware timestamps, benchmark-missing → NaN → excluded with warning, circuit-frozen cross-reference, minimum 60-bar data guard.

---

## 11. Tests (unchanged from spec §8)

`test_no_bounce_returns_empty`, `test_rs_filter_removes_underperformers`, `test_ema_type_c_excluded`, `test_pocket_pivot_detection`, `test_score_ordering`, `test_broken_breadth_row_handled`.

---

## 12. Deferred to v2 (unchanged from spec §9)

RS percentile rank (High), Three-Weeks Tight detection (Medium), WaveTrend OS cross-reference (Medium), dip-depth-vs-recovery-speed (Low), alert integration (Low), historical backtest (High — also the vehicle for revisiting score weights and RATIO_DIP_THRESHOLD/MIN_DIP_BARS calibration).

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
