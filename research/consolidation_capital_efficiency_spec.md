# Consolidation Tracker + Capital Efficiency System — Full Spec

**Purpose**: Detect mature multi-week consolidations (EMA compression + BB squeeze + volume
exhaustion + RS support), score their quality AND imminence, and deploy capital only when
a break is close — maximizing annualized return per rupee-day deployed.

**Deliverables**: Python scanner modules (universe-wide, EOD) + PineScript companion
(visual + intraday alerts).

---

## 0. Guardrails (Non-Negotiable)

- No look-ahead bias — every indicator at bar `t` uses data through bar `t` only
- IST-aware datetimes everywhere; never naive `datetime.now()`
- No silent API fallbacks — fail loudly on missing data
- Scanner interface: `run(universe_df, as_of) -> pd.DataFrame`
- Universe: canonical 962-stock CSV at `data/universe/nse_universe.csv`
- Minimum 250 bars history required per stock (EMA200 warm-up); skip and log otherwise
- Validate every indicator against TradingView on 2-3 known stocks before universe run

---

## 1. Core Thesis

```
Consolidation = stored energy. Cause doesn't matter (accumulation, digestion,
results-wait, macro pause) — the technical signature is identical:

  Price volatility compresses  → BB squeeze
  EMA 50/100/200 converge      → EMA compression
  Volume declines              → equilibrium
  RS line holds / grinds up    → institutional support underneath

QUALITY answers:   "Is this a good spring?"
IMMINENCE answers: "Is the spring about to release?"
Capital deploys ONLY when both are high. Return metric = annualized return
per rupee-day deployed, not hit rate or move size.
```

---

## 2. Indicator Definitions

### 2.1 EMA Compression (dual gate)

```python
ema_spread      = max(ema50, ema100, ema200) - min(ema50, ema100, ema200)
gate_atr        = (ema_spread / atr50) < 1.5          # ATR50, not ATR14 (EP spike immunity)
gate_pct        = (ema_spread / ema200) < 0.03        # 3%
gate_duration   = both above held >= 10 bars

# Convergence rate → stage classification
spread_norm     = ema_spread / ema200
spread_delta    = spread_norm - spread_norm.shift(5)

STAGE_1_CONVERGING  = spread_delta < -0.001    # deepening, not ready
STAGE_2_COMPRESSED  = abs(spread_delta) <= 0.001   # flatlined — max tension
STAGE_3_DIVERGING   = spread_delta > 0.001     # fanout starting — trigger zone
```

### 2.2 BB Squeeze

```python
# BB(20, 2.0, SMA basis) — TradingView default, validated match
bb_basis  = close.rolling(20).mean()
bb_std    = close.rolling(20).std()
bb_upper  = bb_basis + 2.0 * bb_std
bb_lower  = bb_basis - 2.0 * bb_std
bb_width  = bb_upper - bb_lower

# KC(20, 1.5, SMA basis) — matched period
kc_basis  = close.rolling(20).mean()
kc_upper  = kc_basis + 1.5 * atr20
kc_lower  = kc_basis - 1.5 * atr20

squeeze_on          = (bb_upper < kc_upper) & (bb_lower > kc_lower)
squeeze_bars        = consecutive_true_count(squeeze_on)
bb_width_percentile = rolling_percentile_rank(bb_width, 252)   # 0=tightest ever
gate_squeeze        = squeeze_on for >= 5 bars AND bb_width_percentile <= 20
```

### 2.3 Volume Exhaustion (Phase A/B/C)

```python
vol_ma50        = volume.rolling(50).mean()
vol_percentile  = rolling_percentile_rank(volume.rolling(5).mean(), 252)

PHASE_A = vol declining from elevated post-move levels, still > vol_ma50
PHASE_B = vol at/below vol_ma50, declining week-over-week
PHASE_C = vol_percentile <= 20   # multi-month lows — sellers exhausted

quiet_accum_bar = (volume >= 1.5 * volume.rolling(10).mean()) & \
                  (abs(close/close.shift(1) - 1) < 0.01)   # volume without price move
```

### 2.4 RS Line (Character 1-5)

```python
# Benchmark: NIFTY MIDSML 400 daily close
rs_line   = close / benchmark_close
rs_weekly = rs_line.resample('W-FRI').last()     # IST week close
rs_ema9   = rs_weekly.ewm(span=9, adjust=False).mean()
rs_slope  = rs_weekly.pct_change(4)

CHAR_1_DECLINING   = rs below ema9, falling            → AVOID (bearish resolution)
CHAR_2_FLAT        = rs near ema9, sideways            → neutral
CHAR_3_HOLDING     = rs above ema9, flat               → institutional support
CHAR_4_RISING      = rs higher lows while price flat   → quiet accumulation, HIGH conviction
CHAR_5_RS_BREAKOUT = rs at 52wk high, price in range   → earliest break signal, ACT
```

### 2.5 CMF — Chaikin Money Flow (NEW — accumulation confirmation)

```python
mfm  = ((close - low) - (high - close)) / (high - low)     # money flow multiplier
mfv  = mfm * volume
cmf  = mfv.rolling(20).sum() / volume.rolling(20).sum()

# Role in consolidation context:
cmf > 0 during consolidation          → accumulation under flat price
cmf > 0.10 sustained 10+ bars         → strong institutional bid
cmf rising while price flat           → confirms RS CHAR_4 independently
cmf < -0.05 during consolidation      → distribution — downgrade/delete
cmf_divergence = cmf making higher lows while price makes equal/lower lows
```

CMF is the **volume-weighted twin** of RS character — RS says "outperforming peers",
CMF says "money flowing in at the close". Both firing = strongest accumulation read.

### 2.6 Delivery % — NSE Bhavcopy `DELIV_PER` (NEW — conviction layer)

```python
# Source: NSE bhavcopy daily, DELIV_PER column, stored alongside OHLCV
deliv_ma20        = deliv_per.rolling(20).mean()
deliv_baseline    = deliv_per.rolling(120).median()    # stock's own norm

# Signals during consolidation:
deliv_rising      = deliv_ma20 > deliv_baseline * 1.15   # delivery 15%+ above norm
deliv_spike_quiet = (deliv_per > deliv_baseline * 1.3) & quiet_accum_bar
                    # high-delivery quiet bar = strong hands absorbing supply

# Interpretation matrix:
Low volume + HIGH delivery %  → genuine accumulation (best)
Low volume + low delivery %   → intraday churn, no conviction (neutral)
High volume + HIGH delivery % → institutional positioning (breakout fuel)
High volume + low delivery %  → speculative churn / operator (suspect breakout)
```

Delivery % is NSE-specific edge unavailable to BB/EMA-only systems — it separates
real accumulation from F&O-driven churn. **A breakout on high volume but low
delivery % is a downgrade flag.**

---

## 3. Quality Score (0-100)

Computed for all stocks passing the four gates (2.1 EMA dual gate, 2.2 squeeze gate).

| Component | Weight | Source |
|---|---|---|
| BB squeeze depth | 20 | `(20 - bb_width_percentile) * 1.0`, floor 0 |
| EMA stage | 20 | Stage 1 = 8, Stage 2 = 20, Stage 3 = 0 (quality != imminence) |
| Volume exhaustion | 15 | `(20 - vol_percentile) * 0.75`, floor 0 |
| RS character | 20 | CHAR_1=0, 2=5, 3=12, 4=20, 5=20 |
| CMF accumulation | 15 | cmf>0.10: 15, cmf>0.05: 10, cmf>0: 6, else 0 |
| Delivery % trend | 10 | deliv_rising: 10, at baseline: 5, below: 0 |

```
consolidation_age = consecutive bars where all four core conditions
                    simultaneously true (the "four clocks" running together)
```

---

## 4. Imminence Score (0-100) — Deploy Capital On This

| Component | Weight | Trigger |
|---|---|---|
| Pre-break signal count | 30 | `count(signals below) / 6 * 30` |
| EMA Stage 3 flag | 25 | spread_delta just crossed positive after >= 10 bars negative |
| RS breakout flag | 20 | CHAR_5 — RS 52wk high, price still in range |
| BB breathing | 15 | bb_width_percentile up 2 consecutive bars from < 15 |
| Range position | 10 | close in upper third of consolidation range |

### Pre-break signals (①-⑥, each boolean)

```
① RS line new high, price in range          (5-10 bars early)
② EMA spread_delta turns positive            (5-10 bars early)
③ Quiet accumulation bar — vol 1.5-2x, price flat, HIGH delivery %  (3-5 bars)
④ BB width ticks up 2 consecutive bars       (3-5 bars)
⑤ Higher low within the range                (1-2 bars)
⑥ Upper-wick rejection absorbed near range top (1-2 bars)
```

Signal ③ is upgraded by delivery %: quiet accumulation bar WITHOUT elevated
DELIV_PER counts as 0.5, WITH counts as 1.0.

---

## 5. Tier System (maps to existing 3-tier tracker)

```
TIER 3 COLD:   Quality >= 70, Imminence < 30    → track only, zero capital
TIER 2 WARM:   Quality >= 70, Imminence 30-60   → alerts armed, zero capital
TIER 1 HOT:    Quality >= 70, Imminence >= 60   → capital ready, enter on trigger
DEPLOYED:      breakout confirmed                → position open

Promotion/demotion evaluated daily. Log all transitions to signals.db.
```

### Abandonment (DELETE from watchlist)

```
- RS character drops to 1-2
- consolidation_age > 120 bars (~6 months) — stale
- Volume phase reverses: rising volume, no breakout (distribution)
- CMF < -0.05 sustained 5+ bars
- Quality score falls 15+ points from its peak
- Sector RS breakdown
```

---

## 6. Entry + Time-Stop Rules

### Entry trigger (from TIER 1 only)

```
Breakout bar: close > consolidation range high
  AND volume >= 2x vol_ma50
  AND DELIV_PER >= deliv_baseline          # churn filter — reject low-delivery breakouts
  AND regime throttle allows (Section 8)

Entry: next open OR limit at range-high retest. ORB (15-min high break) if at screen.
Stop:  low of breakout bar, max 1.5x ATR. Fixed ₹15,000 risk sizing.
```

### Time-stop ladder (hard rules)

```
Bar 3:   if close back inside range        → EXIT (failed breakout)
Bar 5:   if pnl < +4%                       → EXIT, redeploy
Bar 10:  if no trend / no EMA fanout        → EXIT at least half
```

Rationale: explosive resolutions work almost immediately. Risk = price distance × time.

### Opportunity-cost monitor (per open position, daily)

```
if position_return < benchmark_return_same_period - 3%   → flag UNDERPERFORMING
if position stalled AND tier1_hot_count >= 2              → flag ROTATE_CAPITAL
```

---

## 7. Catalyst Calendar Overlay

```python
# Per watchlist stock, fetch/store:
days_to_results       # quarterly earnings date (NSE announcements / stockinsights API)
days_to_expiry        # F&O monthly expiry (pinning release)
days_to_index_rebal   # Nifty index rebalance dates

# Capital efficiency rule:
Mature consolidation (Quality 80+) + results in 5-10 days + pre-break signals firing
→ deployment window is NOW; forced resolution within days either direction
→ capital cannot be stuck. Gap risk handled by fixed ₹15k risk sizing.

# EP seasonality: Jan / Apr / Jul / Oct results windows = highest-value scan periods.
```

---

## 8. Regime Throttle (breadth dashboard integration)

Source: existing breadth monitor (`ratio_5d`, SMA200 bands from `data/breadth_history.csv`).

```
GREEN:   ratio_5d >= 1.6, SMA200 band healthy (50-80%)
         → all slots deployable, standard time-stops

NEUTRAL: → max 2-3 slots, time-stop tightened to bar-3 rule only

RED:     ratio_5d <= 0.6 OR SMA200 < 20% falling
         → ZERO deployment. Watchlist-building mode. Tier-3 COLD list grows
           for the regime turn.
```

---

## 9. Slot Architecture

```
5-6 slots total (₹15k risk each).
States: DEPLOYED / ARMED (reserved for named Tier-1 stock, max 2) / FREE.
FREE capital parks in liquid fund (earns ~6-7%, never 0%).
Time-stop exit frees slot immediately; rotate to top HOT candidate.
```

---

## 10. Half-Life Analytics (backtest module, build after live modules)

```python
# For every historical consolidation 2020→present across universe:
record: age_at_breakout, quality_at_breakout, imminence_trajectory,
        pre_break_signal_count, forward_return_20d/60d, max_drawdown,
        breakout_deliv_per, breakout_cmf

# Deliverables:
1. Empirical wait-time distribution conditioned on (quality, imminence, signal count)
   → median_expected_wait per watchlist stock
2. expected_annualized = (hit_rate × avg_move) / (median_wait + avg_hold) × 365
   → THE ranking metric for the watchlist (replaces raw quality sort)
3. Validation of Section 4 weights; Section 6 time-stop thresholds
4. Delivery-%-on-breakout vs 60d forward return — quantify the churn filter edge
```

---

## 10.5 Two-Layer Architecture — Daily Operating Loop

```
LAYER 1 — PYTHON (EOD batch, 4:30 PM IST after bhavcopy)
  962 stocks → 4 gates → Quality + Imminence → Tier assignment
  → results/YYYY-MM-DD-consolidation.csv → git commit
  → answers: WHICH stocks, HOW mature, WHAT rank

LAYER 2 — PINESCRIPT (real-time, market hours, next day)
  Load ONLY Tier 1 + Tier 2 stocks from yesterday's Layer 1 output
  Consolidation panel visible, 6 pre-break alerts armed
  → answers: WHEN to act, visual confirmation

DAILY LOOP:
  T 4:30 PM     Python scan runs, tiers updated, git committed
  T evening     Review output: tier transitions, new HOT entries, abandonments
                Update TradingView watchlist to match Tier 1/2 list
  T+1 9:15 AM   Pine monitoring live on Tier 1/2 only
  T+1 intraday  Pre-break alert fires → check panel → regime throttle check
                → entry per Section 6 (ORB if at screen, else EOD confirm)
  T+1 4:30 PM   Loop repeats; time-stops evaluated on open positions

RULE: Pine never monitors stocks Python hasn't tiered. Python never makes
      intraday decisions. No overlap, no gaps.
```

---

## 11. Python Module Layout

```
scanner/
├── consolidation/
│   ├── indicators.py        # EMA/ATR/BB/KC/CMF/RS/delivery calcs (Section 2)
│   ├── quality.py           # quality score (Section 3)
│   ├── imminence.py         # imminence score + pre-break signals (Section 4)
│   ├── tiers.py             # tier state machine + abandonment (Section 5)
│   ├── tracker.py           # ConsolidationTracker — orchestrates per-stock
│   └── consolidation_scanner.py   # run(universe_df, as_of) -> pd.DataFrame
├── capital/
│   ├── time_stops.py        # Section 6 ladder
│   ├── catalyst_calendar.py # Section 7
│   ├── regime_throttle.py   # Section 8 — reads breadth_history.csv
│   └── slots.py             # Section 9 state
└── research/
    └── half_life_backtest.py   # Section 10

Output columns (daily, sorted by expected_annualized desc, else imminence desc):
symbol | quality | imminence | tier | age_bars | ema_stage | vol_phase |
rs_char | cmf | deliv_trend | prebreak_count | days_to_results |
median_wait_est | regime | action
```

Data additions required:
- NSE bhavcopy `DELIV_PER` ingestion into daily store (join on symbol+date)
- Results calendar table (`data/catalyst_calendar.csv`)
- Consolidation state table in `signals.db` (tier transitions, audit trail)

---

## 12. PineScript Companion (Pine v6)

Runs on Tier 1/2 stocks identified by Python EOD scan. Deliverables:

```
Indicator 1 — Consolidation Panel (oscillator below chart):
  plot quality score + imminence score as two lines
  hline 60 (HOT threshold), hline 80 (imminent)
  bgcolor by EMA stage: blue=converging, green=compressed, orange=diverging
  CMF histogram sub-plot, zero line

Indicator 2 — Pre-break alerts (6 alertconditions, once-per-bar):
  ① RS new high (RS vs NIFTY_MIDSML400 via request.security)
  ② spread_delta crossover 0
  ③ quiet accumulation bar (no delivery % in TV — volume-only version, note limitation)
  ④ BB width up 2 bars from percentile < 15
  ⑤ higher low in range
  ⑥ upper-wick rejection near range top

Alert delivery: webhook → existing parser.
Pine limitations accepted: no delivery %, no cross-stock rank, no persistence —
Python owns those.
```

---

## 13. Build Order

```
Phase 1: consolidation/indicators.py + quality.py     — validate vs TradingView first
Phase 2: imminence.py + tiers.py + scanner            — daily ranked output to git
Phase 3: capital/time_stops.py + regime_throttle.py   — wire breadth dashboard
Phase 4: DELIV_PER ingestion + CMF integration        — upgrade scores
Phase 5: catalyst_calendar.py                         — results dates overlay
Phase 6: PineScript panel + 6 alerts                  — intraday layer
Phase 7: half_life_backtest.py                        — derive expected_annualized,
                                                        re-weight everything empirically
```

Phases 1-3 capture ~70% of the value. Ship those before touching 4-7.

---

## 14. Open Validation Items (flag in backtest, don't assume)

- Stage-2 `spread_delta` tolerance ±0.001 — may need widening on high-ATR stocks
- Imminence >= 60 HOT threshold — arbitrary until Section 10 validates
- Time-stop bar-5 +4% floor — calibrate against NSE breakout follow-through stats
- deliv_baseline 120-bar median — check stability across F&O vs cash-only stocks
- CMF 0.10 "strong" threshold — validate distribution across 962-stock universe
