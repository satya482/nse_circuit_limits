# RS Leadership Scanner — Design Spec
**Date:** 2026-07-13

## Overview

Standalone daily scanner mirroring `pine_scripts/Satya RS Relative Leadership.txt`. Fires when a
stock's Relative Performance % (vs NIFTY MIDSML 400) is non-negative AND its EMA of that
oscillator is rising — on the bar the two conditions first align together ("combined cross").

Source of truth: the .txt Pine file as exported (not the TradingView Style-tab screenshot, which
shows saved input values and a 3-color Performance EMA scheme not present in the exported code).
Two interpretive gaps are called out explicitly below since they could not be verified against the
live indicator.

## Parameters (screenshot-saved values, not the .txt's coded defaults)

| Param | Value | Pine input name |
|-------|-------|------------------|
| `rs_ema_long_len` | 9 | RS EMA Length |
| `rs_ema_short_len` | 5 | Short RS EMA |
| `perf_lookback` | 9 | Relative Performance Lookback |
| `perf_smooth` | 5 | Performance Smoothing |
| Benchmark trend filter | **not applied** | (screenshot has it checked; user chose to skip for this scanner) |

Benchmark: `NIFTY MIDSML 400` (Kite tradingsymbol, matches repo convention).

## Architecture

```
rs_leadership_scanner.py
│
├── Stage 1 — TV Screener (reuse rs_highline_scanner.get_watchlist() filters)
│     NSE common equity, price > 20, 1W change > 3%,
│     MCap 800Cr-5L Cr, close > EMA10, close > EMA20,
│     10D avg notional > 20Cr/day
│
├── Stage 2 — load_ohlc_many() + NIFTY MIDSML 400 bench
│
├── Stage 3 — _rs_leadership_signal(df, bench)
│     Combined cross: (rel_perf>=0 AND rel_perf_ema rising) today,
│     NOT both true yesterday
│
└── Stage 4 — Context enrichment + markdown output
      leadershipScore (0-5), RS state, ZLEMA25 direction, squeeze, circuit badge, liq/cmf/deliv tags
```

## Signal Logic

```python
def _rs_leadership_signal(df, bench) -> tuple[bool, float, float]:
    """(signal, rel_perf_today, rel_perf_ema_today)"""
    stock_close = df.set_index("date")["close"].astype(float)
    bench_aligned = bench.reindex(stock_close.index)
    valid = bench_aligned.notna()
    if valid.sum() < PERF_LOOKBACK + PERF_SMOOTH + 2:
        return False, nan, nan

    sc = stock_close[valid]
    bc = bench_aligned[valid]

    stock_ret = sc / sc.shift(PERF_LOOKBACK)
    bench_ret = bc / bc.shift(PERF_LOOKBACK)
    rel_perf = ((stock_ret / bench_ret) - 1) * 100
    rel_perf_ema = rel_perf.ewm(span=PERF_SMOOTH, adjust=False).mean()

    perf_positive = rel_perf >= 0
    ema_rising = rel_perf_ema > rel_perf_ema.shift(1)

    combined_today = bool(perf_positive.iloc[-1] and ema_rising.iloc[-1])
    combined_yesterday = bool(perf_positive.iloc[-2] and ema_rising.iloc[-2])
    signal = combined_today and not combined_yesterday

    return signal, round(rel_perf.iloc[-1], 2), round(rel_perf_ema.iloc[-1], 2)
```

**Interpretive gaps (flagged, not silently assumed):**
1. "Performance EMA blue/uptrend" — no boolean for this exists in the .txt; derived as
   `rel_perf_ema[0] > rel_perf_ema[-1]`, mirroring the file's own `rsEmaRising` pattern for `rsEma21`.
2. Screenshot parameter values (9/5/9/5) used instead of .txt coded defaults (21/9/21/5) — these
   are two different configurations of the same indicator; only one can be live at a time.

**Key invariant:** combined cross fires once per alignment, not every day both conditions hold —
consistent with `strongLeadership`'s cross pattern already in the .txt (`score>=4 and score[1]<4`).

## Context Columns (rich, reusing existing helpers)

- `leadershipScore` (0-5): `rsAboveEma + shortRsBullish + rsEmaRising + outperforming + performanceRising`,
  computed with `rs_ema_long`/`rs_ema_short` as defined above.
- RS state: strong / weak / transition — reuse `_rs_state()` pattern from `rs_highline_scanner.py`,
  parameterized on `rs_ema_long_len=9` instead of the hardcoded `span=9` there (same value, coincidence).
- ZLEMA25 direction: reuse `_zlema()` from `rs_highline_scanner.py`.
- Squeeze flag: reuse `_bb_kc_squeeze()` from `rs_highline_scanner.py`.
- Circuit badge, `liq_tag`, `cmf_tag`, `deliv_tag`: reuse from `ohlc_db.py` / `rs_highline_scanner.py`
  patterns, same as every other scanner in this repo.

## TV Screener Filters

Identical to `rs_highline_scanner.get_watchlist()`:

| Filter | Column | Value |
|--------|--------|-------|
| Exchange | `exchange` | `== "NSE"` |
| Type | `type`, `typespecs` | `stock`, `has(["common"])` |
| Price | `close` | `> 20` |
| 1W change | `Perf.W` | `> 3` |
| Market cap | `market_cap_basic` | `between(8e9, 5e12)` |
| Price > EMA10 | `EMA10` | `col("close") > col("EMA10")` |
| Price > EMA20 | `EMA20` | `col("close") > col("EMA20")` |
| Notional 10D | `Value.Traded` | `> 200e6` |

No local ATR gate (unlike rs_highline) — not part of the Pine source being mirrored.

## Output Schema

Markdown table sorted by `leadershipScore` desc, then `rel_perf` desc.

| Column | Description |
|--------|-------------|
| Symbol + circuit badge | nse.csv circuit limit emoji |
| Name | `get_names()` |
| Close | Last close |
| 1D% | `(close[-1]/close[-2]-1)*100` |
| RelPerf% | `rel_perf` at signal bar |
| PerfEMA | `rel_perf_ema` at signal bar |
| Score | `leadershipScore` 0-5 |
| RS | strong / **transition** / weak |
| ZL | ZLEMA25 ↑ or ↓ |
| Sqz | BB-KC squeeze flag |
| Liq | `liq_tag()` |

Section header:
```
## RS Leadership — YYYY-MM-DD
N signals from M candidates
```

Zero results → `*No signals.*` (never empty file). SEBI header/footer on every file, per repo convention.

## Files

| File | Purpose |
|------|---------|
| `rs_leadership_scanner.py` | Main scanner |
| `rs_leadership_scans/rs_leadership_latest.md` | Always-overwritten latest |
| `rs_leadership_scans/rs_leadership_YYYY-MM-DD.md` | Dated archive |
| `run_rs_leadership_scanner.ps1` | PS1 runner, logs to `logs/` |

## Schedule & Integration

- **Run after:** `run_fetch_data.ps1` (needs fresh SQLite OHLC)
- **Suggested time:** 4:30 PM IST (parallel slot with `rs_highline`, no dependency between them)
- **Auto-commit:** both output files, message `[scan YYYY-MM-DD] rs-leadership: N signals`
- **`run_all_scanners.ps1`:** add to sequence
- **`CLAUDE.md`:** add row to run table and output files table (repo convention — never skip)
- **No dashboard integration** in this phase. Future: confluence with WT/squeeze in
  `wt_squeeze_dashboard.py`, same as `rs_highline` is flagged for.

## Helper Reuse

- `load_ohlc_many`, `get_names`, `liq_tag`, `cmf_tag`, `deliv_tag` — imported from `ohlc_db`
- `SEBI_MD_HEADER`, `SEBI_MD_FOOTER` — imported from `disclaimer`
- `_ema`, `_zlema`, `_bb_kc_squeeze` — copied from `rs_highline_scanner.py` (private helpers, same
  pattern as existing scanners — no shared indicators module in this repo yet)
- `_rs_state`-style logic — copied and reparameterized from `rs_highline_scanner.py`
- Bench symbol: `"NIFTY MIDSML 400"` (matches existing convention)
- TV screener filters — copied verbatim from `rs_highline_scanner.get_watchlist()`

## Testing

Repo has `tests/test_rs_weekly_ema9_scanner.py` as the pattern for scanner unit tests (pure-function
signal logic, no network/DB). Mirror it: `tests/test_rs_leadership_scanner.py` covering
`_rs_leadership_signal()` against constructed DataFrames — combined-cross fires exactly once,
does not fire on days both conditions already held, does not fire when only one condition is true.
