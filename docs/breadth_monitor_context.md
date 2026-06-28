# NSE Breadth Monitor — Context Doc for Claude Chat

## What It Is
Regime/timing layer for NSE equity trading. NOT a stock-selection scanner.
Answers: "Is the market environment supportive right now?"

Live dashboard: https://satya482.github.io/nse_circuit_limits/dashboard/breadth.html

## Universe
~2400–2700 NSE common equity stocks (broad market, not just large-cap).
Circuit-frozen stocks excluded (close == prev_close AND volume == 0).
Refreshed weekly via `scripts/refresh_breadth_universe.py`.

## Data Source
SQLite (`market.db`) populated daily by `fetch_data.py` using Kite Connect API.
Backfill: 10 years (2016–present). Updated post 4:05 PM IST on trading days.

---

## Panels & Metrics

### 1. Market Regime Stat Chip (top of page)
Derived from Ratio 5D vs thresholds.
- `THRUST ▲ Nd` (green) = ratio ≥ 1.6 for N consecutive days → strong bull environment
- `CAP ▼ Nd` (red) = ratio ≤ 0.6 for N consecutive days → panic/distribution
- `NEUTRAL` = between thresholds

### 2. % Stocks Above SMA10/20/50/200
What fraction of the ~2400-stock universe trades above each moving average.

| SMA | Timeframe | What it measures |
|-----|-----------|-----------------|
| SMA10 | ~2 weeks | Short-term momentum; most volatile |
| SMA20 | ~1 month | Near-term trend participation |
| SMA50 | ~2.5 months | Intermediate trend health |
| SMA200 | ~10 months | Long-term structural bull/bear |

**Key levels:**
- SMA200 > 80% = broad overbought / market peak risk
- SMA200 50–80% = healthy bull market
- SMA200 20–50% = weakening / selective market
- SMA200 < 20% = broad washout / bottoming zone
- SMA200 < 15% = extreme washout (historically strong buy signal)

SMA10 step-line (enabled by default) = each horizontal step is one trading day.
The day the SMA10 step ticks HIGHER after several down-steps = entry trigger day.

**Hidden by default:** SMA20 and SMA50 (toggle via legend click or Step buttons).

### 3. NIFTY MIDSML 400 — Regime Band Panel
Price line (normalised 0–100) with background coloring:
- **Green bands** = periods when ratio_5d ≥ 1.6 (thrust regime active)
- **Red bands** = periods when ratio_5d ≤ 0.6 (capitulation regime)
- **Dark/neutral** = in-between

Read: green era = smart time to be long; red era = reduce/avoid.
Crossing markers: ▲ green triangle = ratio crossed INTO thrust; ▼ red = crossed INTO cap.

### 4. Daily 4% Movers
Raw daily count of stocks moving ≥+4% (green bars up) and ≤−4% (red bars down).

| Pattern | Interpretation |
|---------|---------------|
| Green spike > 150–200 stocks | Thrust day — broad institutional buying |
| Red spike > 150–200 stocks | Capitulation day — panic selling, potential bottom 2–4 wks later |
| Both bars tiny < 30 | Low conviction, directionless market |
| Green bars shrinking while index rising | Breadth narrowing — rally thinning, warning |

Threshold lines: dashed green at 150/200, dashed red at −150/−200.

### 5. Ratio Oscillator (5D and 10D)
`ratio_Nd = sum(up4 last N days) / sum(dn4 last N days)`

Y-axis clipped to 8 (extreme spikes can reach 30+, but 0–8 range captures normal action).

| Zone | Value | Meaning |
|------|-------|---------|
| Thrust zone | ≥ 1.6 | Buyers 1.6× more than sellers over window — strong uptrend |
| Neutral | 0.6–1.6 | Mixed market |
| Capitulation zone | ≤ 0.6 | Sellers dominating — panic / distribution |

- 5D (solid) = short-term momentum, reactive
- 10D (dashed) = medium-term, smoother
- 5D crossing ABOVE 1.6 from below = thrust signal (buy)
- 5D crossing BELOW 0.6 = warning/exit signal

### 6. Net Thrust Heatmap (last 2 years)
Calendar grid: each cell = (up4 − dn4) for that trading day.
Green = net up-movers dominated. Red = net down-movers dominated.
Gives seasonal/weekly pattern visibility.

---

## Key Thresholds
```
THRUST_THRESHOLD    = 1.6
CAPITULATION_THRESHOLD = 0.6
SMA10 extreme washout  < 20%
SMA200 overbought      > 80%
SMA200 washout         < 20%
SMA200 extreme bottom  < 15%
Daily movers alert     > 150 / < -150
```

---

## Entry Framework (Swing Trading Alignment)

### Highest-quality setup:
1. Nifty panel: **green band** (thrust regime active — ratio_5d ≥ 1.6)
2. SMA10 breadth: dropped to < 30%, now **turning up** (step-line ticks higher)
3. SMA50 breadth: still > 40% (intermediate trend intact)
4. Ratio 5D: still > 0.6 (not in cap regime)

### Reading the turn:
- Enable SMA10 step-line (default ON)
- Wait for SMA10 to stop falling (steps horizontal or start rising)
- Day it ticks higher = entry trigger
- Missed it? SMA10 often reaches 50–60% within a week of turning

### Avoid if:
- Red band on Nifty panel (cap regime) — SMA10 swing low = dead-cat risk
- SMA200 < 20% AND ratio trending down (structural bear, not a pullback)
- Daily 4% bars showing persistent red dominance without green recovery

### Time horizons:
- SMA10 low → recovery: 3–10 days (short swing)
- SMA50 breadth expansion: 2–6 weeks (primary swing)
- SMA200 re-expansion from < 20%: 3–12 months (multi-month base)

---

## Typical Regime Sequence
```
SMA10 drops sharply → ratio approaches 0.6 (near cap)
→ Daily red bars spike (capitulation)
→ Ratio 5D bounces, crosses 1.0, heads toward 1.6
→ SMA10 turns up (entry zone)
→ Ratio crosses 1.6 (thrust confirmed, green band starts)
→ SMA20/50 breadth expands
→ SMA200 breadth rises (if structural)
→ Eventually SMA10 > 70%, SMA200 > 80% = watch for top
```

---

## Files (for code context)
```
scanners/breadth_monitor.py       # All logic: compute + dashboard HTML
data/breadth_history.csv          # 10yr daily breadth rows (2016–present)
data/breadth_universe.csv         # ~2400–2700 NSE symbols
dashboard/breadth.html # Static dashboard (GitHub Pages)
scripts/refresh_breadth_universe.py # Weekly universe refresh
```

## Run
```powershell
.\run_breadth_monitor.ps1          # Daily, post 4:50 PM IST
python scanners/breadth_monitor.py # Direct run (dashboard only, no new data)
python scanners/breadth_monitor.py --backfill  # Recompute full history
```
