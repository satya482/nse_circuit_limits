# WaveTrend Bull Cross ↔ Market Breadth: Correlation Analysis

**Period**: 2026-06-08 → 2026-07-01 (21 trading days)  
**Data sources**: `wt_scans/wt_bullcross_YYYY-MM-DD.md` × `data/breadth_history.csv`  
**Note**: 21 data points — treat as hypothesis generation, not confirmation.

---

## Raw data (per day)

| Date | WT total | rank4 PPV | SQZ | up4 | dn4 | pct50 | net_thrust |
|------|---------|-----------|-----|-----|-----|-------|------------|
| 2026-06-08 |  20 |  7 |  0 |  46 | 252 | 44.5 | −0.086 |
| 2026-06-09 |  36 | 28 | 18 | 238 |  30 | 52.2 | +0.087 |
| 2026-06-10 |  38 | 18 | 14 |  67 | 150 | 44.1 | −0.035 |
| 2026-06-11 |  21 |  7 |  8 |  52 | 127 | 36.7 | −0.031 |
| 2026-06-12 |  83 | 64 | 38 | 439 |  11 | 49.0 | +0.179 |
| 2026-06-15 | 150 |108 | 76 | 282 |  26 | 59.1 | +0.107 |
| 2026-06-16 |  84 | 26 | 42 | 130 |  41 | 60.2 | +0.037 |
| 2026-06-17 |  47 | 12 | 18 | 137 |  32 | 60.8 | +0.044 |
| 2026-06-18 |  53 | 16 | 23 | 134 |  34 | 62.4 | +0.042 |
| 2026-06-19 |  54 | 13 | 21 | 149 |  27 | 61.9 | +0.051 |
| 2026-06-22 |  93 | 37 | 51 | 188 |  26 | 65.0 | +0.068 |
| 2026-06-23 |  41 | 12 | 18 |  61 | 103 | 59.7 | −0.018 |
| 2026-06-24 |  41 | 18 | 15 | 109 |  52 | 59.8 | +0.024 |
| 2026-06-25 |  56 | 39 | 32 |  67 |  97 | 56.0 | −0.013 |
| 2026-06-29 |  64 | 50 | 30 |  83 |  90 | 55.3 | — |
| 2026-06-30 | 105 | 31 | 33 |  72 |  13 | 61.2 | — |
| 2026-07-01 | 150 | 47 | 66 | 106 |  38 | 61.8 | — |

---

## Correlation table

| WT metric | vs up4 | vs dn4 | vs pct50 | vs pct200 | vs net_thrust |
|-----------|--------|--------|----------|-----------|---------------|
| total_crosses | +0.37 | −0.56 | +0.51 | +0.56 | +0.65 |
| rank4 (PPV)   | +0.62 | −0.40 | +0.19 | +0.18 | +0.66 |
| sqz_count     | —     | —     | +0.51 | — | — |

---

## Lead / lag structure

| Offset | r(total_crosses vs pct_above_sma50) |
|--------|--------------------------------------|
| −1d (yesterday's breadth) | **+0.001** |
| same day | **+0.51** |
| +1 day | +0.47 |
| +2 days | +0.46 |

**Interpretation**: WT count is a coincident indicator. Fires *with* strong breadth, not *before* it.
Yesterday's breadth has near-zero predictive value for today's WT count.

---

## High vs low WT days: next-day breadth

| Tier | n | pct50 same | pct50 +1d | up4 +1d | dn4 +1d |
|------|---|-----------|-----------|---------|---------|
| total ≥ 80 | 6 | 59.4% | **60.3%** | 143 | 48 |
| total < 40 | 4 | 44.4% | 45.5% | 199 | 80 |

High-WT days → breadth floor stays elevated next day. Not a further spike, but holds.

---

## Squeeze breakout tier vs breadth

| SQZ tier | n | pct50 same | pct50 +1d | up4 +1d | dn4 +1d |
|----------|---|-----------|-----------|---------|---------|
| low < 10 | 2 | 40.6% | 50.6% | 339 | 21 |
| mid 10–30 | 8 | 57.0% | 55.9% | 105 | 66 |
| hi > 30 | 7 | 58.9% | **59.5%** | 133 | 55 |

Low-SQZ tier: weak same-day breadth but notable next-day bounce (only 2 pts — watch list).

---

## Key findings

1. **WT = coincident breadth indicator**. Not a leading signal. Fires alongside accumulation days.
2. **net_thrust best single metric** (r = +0.65) — both total and rank4 correlate equally.
3. **rank4 PPV quality > raw total count**. r(rank4 vs up4) = +0.62 vs r(total vs up4) = +0.37.
   High PPV count = genuine institutional participation.
4. **sqz_count / total ratio** = quality filter worth tracking.
   High ratio → most crosses inside active squeezes → higher breadth days.
5. **Low SQZ + high WT**: suspect. Crosses fire but breadth weak → chop or midrange noise.

---

## Hypotheses to test with more data (6M+)

- [ ] Does `sqz_count > 40` on day T predict pct50 staying > 60% for 3+ days?
- [ ] Does `rank4_count / total > 0.5` identify genuine accumulation days?
- [ ] `net_thrust > +0.05` AND `sqz > 30` as composite entry filter — does it hold?
- [ ] `total > 100` as overbought warning (market stretched) vs continuation signal?
- [ ] Low-SQZ bounce: confirm n=2 finding with 6M data
- [ ] RS-gate threshold (`rs_state != weak`): does the RS-Confirmed subset outperform the excluded-weak subset
      on forward returns? 2026-07-02 split was 159 confirmed / 54 weak (75/25) on a 213-cross day — need
      forward-return data across more days, not just same-day counts, to know if the gate adds signal or
      just removes noise cosmetically.

---

*Analysis run: 2026-07-01 · Data window: 21 trading days · Scripts: ad-hoc pandas in Claude Code session*
