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

## Extended backtest (2026-07-02) — 571 trading days, 2021-09-27 → 2026-06-29

**Motivation**: 21-day sample above sat entirely inside one rally window (2026-06-08 → 07-01) —
too narrow to separate "WT count tracks a rising market" from "WT count tracks breadth generally."
Recomputed WT bull-cross counts from raw OHLC (`scripts/wt_breadth_backtest.py`) using the full
local SQLite history (`.ohlc_data/market.db`, 2016–2026) against `data/breadth_universe.csv`
(current ~2,700-symbol snapshot — survivorship-biased, see caveats).

**Important — NOT the same metric as `wt_bullcross_latest.md`**: this backtest counts raw
`wt_bull_cross_any` (rank≥1 proxy) across the *unfiltered* breadth universe (no price/mcap/float/RS
gates, no PPV rank 4/5 — PPV's per-bar loop is too expensive to vectorize at this scale). Counts run
~3-5x higher than the live scanner's gated output. **Use this section for correlation direction and
regime behavior, not absolute count thresholds** — those still come from the live scanner's own history.

### Correlation table (Pearson, n=571; Spearman in parens)

| WT metric | vs up4 | vs dn4 | vs pct50 | vs pct200 | vs net_thrust |
|-----------|--------|--------|----------|-----------|---------------|
| total_cross | +0.39 (+0.14) | −0.18 (−0.14) | **−0.17 (−0.19)** | −0.34 (−0.41) | +0.49 (+0.56) |
| os_cross (deep oversold) | +0.33 (−0.01) | −0.08 (+0.02) | **−0.41 (−0.54)** | −0.34 (−0.49) | +0.30 (+0.19) |
| sqz_cross | +0.28 (+0.09) | −0.20 (−0.15) | −0.06 (−0.13) | −0.26 (−0.35) | +0.43 (+0.52) |

**This flips the 21-day finding.** Short-window: total_cross vs pct50 was +0.51. Full history: **−0.17**
(Spearman −0.19, robust to outliers — checked by dropping the single largest spike day, sign holds).
Likely explanation: WT count tracks breadth **momentum** (net_thrust, consistently positive ~+0.5 in
both windows) far more than breadth **level**. The 21-day sample happened to have momentum and level
rising together, hiding this. Over 4.7 years they decouple — count spikes both on capitulation-bounce
days (pct50 in single digits) and on strong broad-rally days (pct50 >75%), which is why the *level*
correlation nets negative: oversold-bounce spikes are more frequent/extreme than rally spikes.

`os_cross` (deep-oversold-only) has the cleanest read: consistently negative vs both pct50 and pct200
(Spearman −0.54 / −0.49). Makes sense structurally — a stock can only fire an oversold bull cross if it
*was* oversold, which is mechanically more common when breadth is weak.

### Lead/lag (r(total_cross, pct_above_sma50) at offset days)

| −3d | −2d | −1d | same day | +1d | +2d | +3d |
|-----|-----|-----|----------|-----|-----|-----|
| −0.293 | −0.303 | −0.250 | −0.173 | −0.155 | −0.147 | −0.140 |

Strongest (most negative) at −2d/−3d: today's cross count correlates most with breadth having been
**weaker 2-3 days ago** — consistent with crosses firing as bounces *after* a breadth dip, not before one.

### Regime split — total_cross tier vs forward breadth

| Tier | n | pct50 same | +1d | +3d | +5d |
|------|---|-----------|-----|-----|-----|
| total_cross ≥ 194 (top quintile) | 115 | 41.5 | 42.2 | 42.2 | 42.2 |
| total_cross ≤ 1 (bottom quintile) | 127 | 56.3 | 55.6 | 55.0 | 54.7 |

High-count days cluster in weak-breadth regimes and **stay** weak for 5 days after — no evidence of a
count spike front-running a breadth recovery on its own.

### Signal composition matters more than raw count

| Composition | n | Fwd-5d pct50 change |
|---|---|---|
| os_frac (os_cross/total) top quartile | 143 | **+3.49** |
| os_frac bottom quartile | 181 | −1.90 |
| sqz_frac (sqz_cross/total) top quartile | 143 | −1.86 |
| sqz_frac bottom quartile | 143 | +0.69 |

A day with a **higher share of deep-oversold crosses** (proper capitulation bounce) leads breadth
*higher* over the next 5 days. A day with a **higher share of squeeze-context crosses** leads breadth
*lower*. This is a genuine reversal of the 21-day study's finding #4 ("sqz_count/total = quality
filter") — flagging that hypothesis as **likely wrong at longer horizon**, not confirming it.
Read with normal caution given no forward-return / trade-level validation yet, only breadth proxy.

### Hypothesis test results (vs the 6M+ backlog from the 21-day study)

| Hypothesis | Verdict |
|---|---|
| `sqz_count > 40` predicts pct50 staying > 60% for 3+ days | **REJECTED** — sqz>40 days: pct50_fwd3=45.3, only 26.3% stayed >60%. sqz≤40 days: pct50_fwd3=48.4, 37.8% stayed >60%. Opposite direction. |
| `net_thrust > +0.05 AND sqz_cross > 30` as composite entry filter | **CONFIRMED** — composite days (n=75): fwd-5d pct50 change +3.62. Rest (n=496): −0.46. Clear positive differential. |
| `total_cross > 100` as overbought warning vs continuation | Leans **overbought-warning**, weakly: total_cross>100 (n=234) → fwd-5d pct50 change −0.25; total_cross≤100 (n=337) → +0.30. Small effect, not decisive. |
| `rank4/total > 0.5` identifies genuine accumulation days | **Not tested** — PPV not recomputed in this backtest (see caveat above). Still open. |
| RS-gate forward-return validation | **Not tested** — needs per-day RS state, out of scope for this pass. Still open. |

### Answering the original question — "too many bullcross signals lately"

Recent raw-universe counts (2026-06-15 → 06-29, `total_cross`, percentile vs full 4.7yr history):

| Date | total_cross | percentile | pct50 | net_thrust |
|------|------------|-----------|-------|------------|
| 2026-06-15 | 757 | 99.8% | 59.1 | +0.107 |
| 2026-06-16 | 264 | 87.6% | 60.2 | +0.037 |
| 2026-06-22 | 135 | 70.2% | 65.0 | +0.068 |
| 2026-06-29 | 81 | 52.5% | 55.3 | — |
| 2026-07-02 | 229 | ~90%+ | — | — |

2026-06-15 is a genuine broad-based event (checked: only 38/757 crosses came from short-history/warmup
symbols — not a data artifact), the single largest spike in 4.7 years. Outside that one day, most of
the "elevated" recent readings sit in the 50th-90th percentile band — elevated but not extreme.

Given the composition finding above: 2026-07-02's os_frac (11/229 = 4.8%) is low and sqz_frac
(100/229 = 43.7%) is high-ish — on the (tentatively reversed) composition read, that combination leans
toward the **weaker** forward-breadth quadrant, not a confirming-accumulation one. Treat as a caution
flag, not a verdict — this composition finding itself just reversed one prior conclusion, so hold it
loosely until re-tested on more data.

**Bottom line**: elevated bullcross counts right now don't cleanly resolve to "healthy accumulation" or
"washout noise" from breadth correlation alone — the strongest, most robust finding across both the
21-day and 571-day windows is that WT count tracks breadth **momentum** (net_thrust, r≈+0.5 in both),
not breadth **level**. If net_thrust is positive alongside high counts, that's the closest thing to a
validated green light (`net_thrust>0.05 AND sqz>30` composite, confirmed above). If net_thrust is flat
or negative, high counts likely reflect scattered bounce attempts, not confirmed follow-through.

### Caveats

- Universe is `breadth_universe.csv`'s **current** ~2,700-symbol snapshot applied retroactively —
  survivorship bias (delisted/renamed symbols not represented in earlier years).
- No PPV (rank 4/5) recomputed — Pine's per-bar pocket-pivot loop wasn't vectorized for this scale.
- `sqz_cross` here means "bull cross fired while squeeze active," not squeeze-breakout timing —
  slightly different framing from the live scanner's SQUEEZE BREAKOUT section.
- Breadth rows with `total_eligible < 1500` dropped (thin-universe days, incl. the known-bad 2026-06-26
  row already flagged in `net_thrust_wavetrend.py`).
- Forward-breadth proxies only — no trade-level forward-return validation. Don't treat any "CONFIRMED"
  row above as a trading rule without that step.

*Scripts: `scripts/wt_breadth_backtest.py` → `data/wt_breadth_backtest.csv`,
`data/wt_breadth_backtest_merged.csv`*

---

*Analysis run: 2026-07-01 (21-day) / 2026-07-02 (571-day extended) · Scripts: ad-hoc pandas in Claude Code session*
