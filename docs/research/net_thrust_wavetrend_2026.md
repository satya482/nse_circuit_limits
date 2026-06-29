> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Net-Thrust WaveTrend Oscillator — Research Log
**Date:** 2026-06-28  
**Status:** NO-GO (validation failed all three acceptance criteria)  
**Spec:** `spec_1.md` (retained in downloads; summarised here)  
**Codebase:** `nse_circuit_limits` — branch `main`, commits `71160c4` → `da6cd8c`

---

## 1. Hypothesis

A WaveTrend oscillator computed on *normalised net breadth thrust* (`net_thrust`) rather than on stock price would lead the structural breadth metric `pct_above_sma200` by roughly 5–10 trading days at inflection points — earlier than the existing simple `pct_above_sma10` turn-up rule already in the dashboard.

**What "leading" means here:** When the market sells off hard and then begins recovering, the structural SMA200 metric takes weeks to turn. The hypothesis was that short bursts of aggressive buying (many stocks up ≥4% in one session) would manifest as a WT bull-cross on `net_thrust` *before* the structural picture changed, giving an earlier entry trigger.

---

## 2. Input: net_thrust

```
net_thrust = (up4_count - down4_count) / total_eligible
```

- `up4_count`: stocks closing ≥+4% today  
- `down4_count`: stocks closing ≤-4% today  
- `total_eligible`: total stocks in the broad NSE universe (excludes circuit-frozen)  

Normalised by `total_eligible` to be comparable across history (universe grew from ~1,073 in 2016 to ~2,390 in 2026). Raw count difference (`up4 - down4`) would not be comparable across years.

**Guard:** rows with `total_eligible < 2000` get `NaN`, never computed. This excluded all history before 2024-12-23 (2,105 rows out of 2,478 total).

**Reference values (sanity checks):**

| Date | up4 | dn4 | total | net_thrust |
|------|-----|-----|-------|------------|
| 2026-05-12 | 46 | 658 | 2385 | −0.2566 |
| 2026-06-12 | 439 | 11 | 2393 | +0.1789 |
| 2026-06-22 | 188 | 26 | 2396 | +0.0676 |

The 2026-05-12 value (−0.2566) is the deepest capitulation spike in the usable history.

---

## 3. WaveTrend Parameterisation

Standard WaveTrend formula (same as stock-level scanner, now input-agnostic):

```
esa  = EMA(net_thrust, n1)
d    = EMA(|net_thrust − esa|, n1)
ci   = (net_thrust − esa) / (0.015 × d)
wt1  = EMA(ci, n2)
wt2  = SMA(wt1, 4)          # fixed 4-bar smoothing, not overridable
```

Two channels run in parallel:

| Channel | n1 | n2 | Analogy |
|---------|----|----|---------|
| fast | 5 | 10 | `ratio_5d` (5-day thrust ratio) |
| slow | 10 | 21 | `ratio_10d` (10-day thrust ratio) |

**Low-conviction guard (option a):** on days where `up4 + down4 < 30` (both sides quiet = directionless), replace `net_thrust` with the 60-day trailing rolling median before the WaveTrend calc. This prevents `d` from collapsing to near-zero on quiet days and making `ci` artificially large. Zero low-conviction days existed in the actual 18-month dataset.

**Cross definition:**  
- `BULL_CROSS`: `wt1[t-1] <= wt2[t-1]` AND `wt1[t] > wt2[t]`  
- `BEAR_CROSS`: inverse

---

## 4. Data Coverage — The Core Limitation

| Metric | Value |
|--------|-------|
| Total breadth history rows | 2,478 (2016-06-28 → 2026-06-26) |
| Rows with total_eligible ≥ 2000 | **373** |
| Usable date range | 2024-12-23 → 2026-06-25 |
| Usable span | ~18 months |
| Known bad row excluded | 2026-06-26 (total_eligible = 10) |

**Why only 373 usable rows?**  
The breadth universe crossed 2,000 eligible stocks sometime in late 2024. All earlier history sits below the guard threshold. This is the single most important limitation on every finding below.

---

## 5. Signal Count

After filtering (373 usable days × 2 channels):

| Channel | BULL_CROSS | BEAR_CROSS | Avg gap between crosses |
|---------|-----------|-----------|------------------------|
| Fast (n1=5, n2=10) | 57 | 57 | ~3.3 days |
| Slow (n1=10, n2=21) | 48 | 48 | ~3.9 days |

The fast channel fires a full cross every 3.3 days on average — extremely noisy relative to what a "timing signal" should produce.

---

## 6. SMA200 Structural Context at Each Bull Cross

Breakdown of the 57 fast-channel BULL_CROSS events by SMA200 band and confirm/diverge status:

| Band | Count | Confirm | Diverge | Neutral |
|------|-------|---------|---------|---------|
| weakening (20–50%) | 35 | 13 | 20 | 2 |
| healthy_bull (50–80%) | 12 | 9 | 3 | 0 |
| extreme_bottom (<15%) | 5 | 1 | 4 | 0 |
| washout (15–20%) | 5 | 1 | 3 | 1 |

**Notable pattern:** 67% of bull crosses fired while `sma200_roc_10d < −1.0` (DIVERGENT) — momentum thrust occurring while structural breadth was still declining. Only 24/57 were CONFIRMED (structural breadth also improving at the cross).

Tier distribution:

| Tier | Count | Interpretation |
|------|-------|----------------|
| 1 (extreme_bottom/washout + rising) | 2 | Rare, highest conviction |
| 2 (weakening + rising) | 13 | Standard healthy setup |
| 3 (momentum only) | 42 | Most crosses fell here |
| 4 (overbought) | 0 | None in this period |

---

## 7. Acceptance Criteria Results

### C1 — Does WT lead SMA200 structural inflection?

**Method:** For each fast BULL_CROSS, find the nearest SMA200 local-min-then-rising inflection (rolling 20-bar window local min, followed by ≥3 consecutive non-decreasing bars). Compute calendar-day lag (positive = WT fires before inflection, negative = WT fires after).

**Result:**

| Stat | Value |
|------|-------|
| Crosses with non-NaN lag | 53/57 |
| Median lag | **−10 days** |
| Mean lag | −14.3 days |
| Min lag | −107 days |
| Max lag | +81 days |
| Number of SMA200 inflection events found | ~6 |

**FAIL.** Target: 0–15 positive days. Actual: −10 days (WT fires 10 days *after* the inflection).

**Why:** Only ~6 SMA200 inflection events exist in 18 months. The `lag_to_nearest` function that finds the nearest event in either direction pulls most crosses backward to past inflections. Looking at the raw cross table:
- Early 2025 crosses (Jan–Mar) had positive lags (13, −1, −8, 5, 1 days) — genuinely near a real inflection
- From Apr 2025 onward, lags go deeply negative (−25, −37, −57, −65, −82, −92, −102, −107) because the inflection was the Jan 2025 bottom and there's been no new full cycle since

The algorithm's "nearest" logic is being dominated by a single completed cycle. With 5–10 years of data (multiple full cycles), the distribution would look very different.

### C2 — Does WT beat the existing SMA10 turn-up rule?

**Method:** Compare `|median lag to SMA200 inflection|` for WT bull-crosses vs. for SMA10 turn-up events.

| | Median |abs(median)| Direction |
|--|--------|-----------|-----------|
| Fast WT BULL_CROSS → SMA200 inflection | −10.0 days | 10.0 days | Lagging |
| SMA10 turn-up → SMA200 inflection | −1.0 days | 1.0 days | Lagging |

**FAIL.** WT absolute lag (10 days) is 10× the SMA10 rule's lag (1 day). The simple rule wins.

**Note on C2 implementation:** Initial implementation compared raw values (`-10 < -1`, True), which was a spurious PASS. Fixed to absolute-value comparison before final review.

### C3 — Is the false-cross rate acceptable?

**Chop window:** 2026-05-19 → 2026-06-11  
(SMA10 oscillated 18% → 67% → 46% with no durable trend — labeled chop from dashboard history)

| | Crosses in window | False (reversed <7 cal days) | Rate |
|--|-------------------|------------------------------|------|
| Fast WT | 6 | 6 | **100%** |
| SMA10/ratio_5d baseline | 3 | 1 | **33%** |

**Chop window cross sequence:**
```
2026-05-19  BULL_CROSS  → reversed (BEAR) on 2026-05-26   [7 days] FALSE
2026-05-26  BEAR_CROSS  → reversed (BULL) on 2026-06-02   [7 days] FALSE
2026-06-02  BULL_CROSS  → reversed (BEAR) on 2026-06-08   [6 days] FALSE
2026-06-08  BEAR_CROSS  → reversed (BULL) on 2026-06-09   [1 day]  FALSE
2026-06-09  BULL_CROSS  → reversed (BEAR) on 2026-06-10   [1 day]  FALSE
2026-06-10  BEAR_CROSS  → (chop window ends 06-11)              FALSE
```

**FAIL.** WT is 3× noisier than the existing simple rule during chop.

---

## 8. Why the Fast Channel Fails in Chop

`net_thrust` is statistically closer to white noise than to price. Price has autocorrelation (yesterday's trend partially predicts today's); net thrust does not — each day's movers are mostly independent. 

With n1=5 (5-bar EMA for the channel length), `esa` tracks `net_thrust` almost immediately, making `ci` very sensitive to day-by-day variation. A single day with many advancers (e.g., broad short-covering) creates a spike that crosses `wt2`, then the next session's reversion creates a bear cross. The EMA just isn't long enough to absorb the noise.

The classic McClellan Oscillator uses **19-day / 39-day** EMAs on raw advances-minus-declines. Translated to this framework: n1≈19, n2≈39. The current fast params (5/10) are 3–4× shorter — tuned for price autocorrelation, not breadth-burst statistics.

---

## 9. What Could Work — Future Experiments

### 9.1 Slower parameters
Try n1=15, n2=30 or n1=19, n2=39 (McClellan-equivalent). Hypothesis: fewer crosses in chop, longer hold between signals. The slow channel (n1=10, n2=21) had 48 vs. 57 crosses — already 16% fewer. Extension to 19/39 could reduce to ~30, which would lower the false-cross rate significantly.

### 9.2 More history
The entire analysis rests on 373 trading days. With `total_eligible >= 2000` only available from Dec 2024, there is no way to fix this without lowering the guard or backfilling older data via a different source. The market cap of the NSE broad universe crossed 2,000 names at some point in late 2024; before that the guard correctly excludes the data but kills the analysis.

Options:
- Lower the guard to `total_eligible >= 1500` and check whether normalization holds
- Use a different universe definition (e.g., Nifty 500 fixed basket) that's stable over 5+ years

### 9.3 Alternative input: signed-log-ratio
Spec §12 flags this explicitly. `net_thrust` is dominated by extreme days like 2026-05-12 (−0.2566 on a 658-stock down day). Log-compression:
```
input = sign(up4 - dn4) × log(1 + max(up4, dn4) / max(min(up4, dn4), 1))
```
This compresses the tail and might reduce the false-cross rate on extreme-volatility days specifically.

### 9.4 Tier-filtered signals only
Instead of all bull-crosses, filter to Tier 1 (extreme_bottom/washout + SMA200 rising) and Tier 2 (weakening + CONFIRMED). In this dataset: only 2 Tier-1 events and 13 Tier-2 events. Too sparse to validate, but if more history is available this could be a much cleaner signal set. Tier-1 events are precisely the contrarian-capitulation setup the hypothesis was originally targeting.

### 9.5 Lag metric redesign
The `lag_to_nearest` function picks the absolute-nearest SMA200 inflection in either direction. This produces spuriously negative lags when there's only one cycle in the data. A better metric:
- Only look forward (positive lag = WT leads, ignore backward matches)
- Count what fraction of bull-crosses are followed by a SMA200 inflection within N days
- Compare that hit-rate to the SMA10 rule's hit-rate

### 9.6 Use SMA10 inflection as the target, not SMA200
`pct_above_sma200` takes months to inflect. `pct_above_sma10` inflects in days. The spec's hypothesis was about SMA200 specifically, but a more tractable research question: does WT bull-cross lead the *SMA10* turn-up? The lag_to_sma10_uptick column in the validation CSV already has this — median 0.0, mean 0.2. WT and SMA10 fire on essentially the same day, which means WT is at best a concurrent signal for SMA10, not a leading one.

---

## 10. Key Files

| File | Role |
|------|------|
| `scanners/breadth_monitor.py` | Computes and persists `net_thrust` in the daily pipeline |
| `scanners/net_thrust_wavetrend.py` | Module A: dual-channel WT on net_thrust |
| `scanners/sma200_context.py` | Module B: sma200_band, confirm_or_diverge, breadth_cross_tier |
| `scripts/validate_net_thrust_wavetrend.py` | Module D: full validation harness |
| `data/breadth_history.csv` | Source; `net_thrust` column added, 373 rows populated |
| `data/net_thrust_wavetrend.csv` | Module A output; 746 rows (373 dates × 2 channels) |
| `data/net_thrust_wt_validation.csv` | Module D output; 114 rows; the review artifact |
| `tests/test_net_thrust_wavetrend.py` | 6 spec-mandated unit tests |
| `tests/test_sma200_context.py` | 40 boundary tests for Module B |
| `wavetrend_scanner.py` | Refactored: `calc_from_series(series, n1, n2)` added |

---

## 11. Verdict and Decision

**VERDICT: NO-GO** — dashboard panel (spec §8) not built.

Per spec §7.5: "A clean 'this doesn't help' finding is a useful and complete outcome for this spec, not a failure to fix."

The primary reason the verdict is NO-GO is **data scarcity** (373 trading days, ~6 SMA200 cycles), not necessarily a fundamental flaw in the signal concept. The false-cross rate result (C3) is more damning on its own merits — the fast channel is genuinely too noisy for NSE breadth during chop — but this too could change with slower parameters.

**Revisit conditions:**
1. Breadth history reaches ≥ 5 years of `total_eligible >= 2000` data (estimated: mid-2029 at current pace, or sooner if the guard is relaxed to ≥1500)
2. Grid-search on n1/n2 with the slow-channel parameters (15/30, 19/39)
3. Tier-filtered analysis (Tier 1+2 only) across multiple cycles

**Do not:**
- Build the dashboard panel until C1+C3 pass with at least 5 cycles of history
- Merge the parameterisation change without re-running the harness (`python scripts/validate_net_thrust_wavetrend.py`)

---

## 12. Test Coverage

```
tests/test_net_thrust_wavetrend.py   6 tests  (spec §11)
tests/test_sma200_context.py        40 tests  (Module B boundaries)
tests/test_breadth_monitor.py       21 tests  (pre-existing)
─────────────────────────────────────────────
Total                               67 tests  all passing
```

---

*This document was auto-generated from the implementation session on 2026-06-28. All numerical values are from the actual data files as of that date.*

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
