# RS High-Line Cross Scanner — Design Spec
**Date:** 2026-06-30

## Overview

Standalone daily scanner that fires when a stock's **close crosses above the high of the last bar where its RS line was declining**. Mirrors the Pine Script `latestRsHigh` crossover alert logic exactly.

RS line = `(close / NIFTY MIDSML 400 close) * 1000`

---

## Architecture

```
rs_highline_scanner.py
│
├── Stage 1 — TV Screener (~2000 → ~400 stocks)
│     NSE common equity, price > 20, 1W change > 3%,
│     MCap 8B–5T INR, close > EMA10, close > EMA20,
│     10D avg notional > 200M INR
│
├── Stage 2 — load_ohlc_many() + NIFTY MIDSML 400 bench
│
├── Stage 3 — Local ATR gate
│     ATR(14, Wilder EWM) / close > 3%
│
├── Stage 4 — _rs_highline_cross(df, bench)
│     Signal: close[-1] > latestRsHigh AND close[-2] <= latestRsHigh
│
└── Stage 5 — Context enrichment + markdown output
      ZL25, RS state, squeeze, earliness, circuit badge, liq_tag
```

---

## Signal Logic

```python
def _rs_highline_cross(df, bench) -> tuple[bool, float, float]:
    """(signal, latest_rs_high_price, pct_above_rs_high)"""
    stock_close = df.set_index("date")["close"].astype(float)
    bench_aligned = bench.reindex(stock_close.index)
    valid = bench_aligned.notna()
    if valid.sum() < 10:
        return False, nan, nan

    rs_line = (stock_close[valid] / bench_aligned[valid]) * 1000
    highs = df.set_index("date")["high"].astype(float).reindex(rs_line.index)

    # Most recent bar where RS was declining
    latest_rs_high = nan
    for i in range(len(rs_line) - 1, 0, -1):
        if rs_line.iloc[i] < rs_line.iloc[i - 1]:
            latest_rs_high = highs.iloc[i]
            break

    if isnan(latest_rs_high):
        return False, nan, nan

    c_today = stock_close.iloc[-1]
    c_prev  = stock_close.iloc[-2]
    crossed = c_today > latest_rs_high and c_prev <= latest_rs_high
    pct_above = (c_today / latest_rs_high - 1) * 100
    return crossed, round(latest_rs_high, 2), round(pct_above, 2)
```

**Key invariants:**
- If today is an RS-down bar → `latestRsHigh = today's high` → `close > high` impossible → signal = False. Matches Pine behaviour.
- No artificial lookback cap — RS-down bar could be 1 or 100+ bars ago.
- `pct_above` positive = close is above breakout level.

---

## TV Screener Filters

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

**Local gate (post OHLC load):**
- ATR(14, Wilder EWM) / close × 100 > 3%

---

## Output Schema

Markdown table sorted by **earliness score descending**.

| Column | Description |
|--------|-------------|
| Symbol + circuit badge | nse.csv circuit limit emoji |
| Name | `get_names()` |
| Close | Last close |
| 1D% | `(close[-1]/close[-2]-1)*100` |
| RS-High | `latest_rs_high` level |
| Above% | `pct_above` |
| RS | strong / **transition** / weak |
| ZL | ZLEMA25 ↑ or ↓ |
| ZL-days / ZL-gain% | `_zl25_turn_stats()` |
| Sqz | BB-KC squeeze flag |
| ATR% | Local Wilder ATR(14)/close*100 |
| Early | Earliness score 0–100 |
| Liq | `liq_tag()` |

Section header:
```
## RS High-Line Cross — YYYY-MM-DD
N signals from M candidates
```

Zero results → `*No signals.*` (never empty file).

---

## Files

| File | Purpose |
|------|---------|
| `rs_highline_scanner.py` | Main scanner |
| `rs_highline_scans/rs_highline_latest.md` | Always-overwritten latest |
| `rs_highline_scans/rs_highline_YYYY-MM-DD.md` | Dated archive |
| `run_rs_highline_scanner.ps1` | PS1 runner, logs to `logs/` |

---

## Schedule & Integration

- **Run after:** `run_fetch_data.ps1` (needs fresh SQLite OHLC)
- **Suggested time:** 4:30 PM IST
- **Auto-commit:** both output files, message `[scan YYYY-MM-DD] rs-highline: N signals`
- **`run_all_scanners.ps1`:** add to sequence
- **`CLAUDE.md`:** add row to run table and output files table
- **No dashboard integration** (standalone). Future: confluence with WT in `wt_squeeze_dashboard.py`.

---

## Helper Reuse

- `load_ohlc_many`, `get_names`, `liq_tag` — imported from `ohlc_db`
- `SEBI_MD_HEADER`, `SEBI_MD_FOOTER` — imported from `disclaimer`
- `_ema`, `_zlema`, `_bb_kc_squeeze`, `_zl25_turn_stats` — copied from `wt_bullcross_scanner` (private helpers, same pattern as existing scanners)
- `_rs_state`, `_earliness` — copied from `wt_bullcross_scanner`
- Bench symbol: `"NIFTY MIDSML 400"` (matches existing convention)
