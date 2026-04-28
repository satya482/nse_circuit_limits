# EMA Compression Scanner — Project Context

## What This Project Does
Scans a universe of 962 NSE-listed stocks daily to identify EMA compression
setups that historically precede explosive moves. Results are ranked by a
composite score and committed to git daily.

---

## Research Thesis (Read Before Writing Any Code)

### The Setup
Two independent volatility compression signals firing simultaneously:

1. **EMA Compression** — EMA 50, 100, 200 converging (structural reset)
2. **Bollinger Band Squeeze** — BB inside Keltner Channels (timing coil)

When both are true + RS line confirms direction → explosive move (EMA fanout
+ BB bulge) is high probability.

### Phase Model
```
Phase 1: TRENDING     — EMA 50 > 100 > 200, BB wide, price directional
Phase 2: COMPRESSION  — EMAs converging, BB narrowing, volume declining
Phase 3: SQUEEZE PEAK — EMAs ≈ equal, BB inside KC, volume at lows
Phase 4: RELEASE      — EMA fanout, BB bulge, volume 3-5x surge
```

---

## Signal Architecture (Full Pipeline)

```
962 stocks
    ↓
[EMA Dual Gate]         — structural compression confirmed
    ↓
[BB Squeeze Gate]       — timing coil confirmed
    ↓
[RS Directionality]     — direction filter (bullish only)
    ↓
[Composite Score 0-100] — priority ranking
    ↓
Top 10-15 stocks → results/YYYY-MM-DD-signals.csv → git commit
```

---

## Gate Definitions (Exact Thresholds)

### EMA Dual Gate (BOTH must pass)
```python
ema_spread = max(ema50, ema100, ema200) - min(ema50, ema100, ema200)

gate_1 = (ema_spread / atr50) < 1.5          # ATR-normalized
gate_2 = (ema_spread / ema200) < 0.03        # % spread < 3%
gate_3 = compression_duration >= 10           # bars condition held
```

### BB Squeeze Gate
```python
# Bollinger Bands (20, 2.0, SMA basis)
bb_basis = close.rolling(20).mean()                  # SMA basis
bb_std   = close.rolling(20).std()
bb_upper = bb_basis + 2.0 * bb_std
bb_lower = bb_basis - 2.0 * bb_std

# Keltner Channels (20, 1.5, SMA basis — matched to BB period)
kc_basis = close.rolling(20).mean()
kc_upper = kc_basis + 1.5 * atr20
kc_lower = kc_basis - 1.5 * atr20

# Squeeze = BB inside KC
squeeze_on = (bb_upper < kc_upper) and (bb_lower > kc_lower)

gate_4 = squeeze_on for >= 5 bars
gate_5 = bb_width_percentile <= 20  # bottom 20% of 52-week range
```

### RS Directionality Filter
```python
# Benchmark: NiftyMidSml400 index
rs_line = stock_close / niftymidsml400_close

# Weekly RS line vs its EMA 9
rs_weekly = rs_line.resample('W').last()
rs_ema9 = rs_weekly.ewm(span=9).mean()

# Must pass BOTH:
direction_1 = rs_weekly.iloc[-1] > rs_ema9.iloc[-1]   # RS above EMA9
direction_2 = rs_weekly.diff(4).iloc[-1] > 0            # RS slope positive
```

---

## Composite Score (0-100)

Calculated ONLY for stocks that pass all gates above.

| Component | Weight | What It Measures |
|---|---|---|
| EMA Tightness | 25% | How compressed — tighter = higher |
| Compression Duration | 20% | Bars condition held — longer = higher |
| Volume Trend | 20% | Is volume declining? Declining = higher |
| BB Squeeze Intensity | 15% | How deep inside KC are the BBs |
| RS Line Strength | 20% | RS gap above EMA9 + slope + percentile rank |

```python
# RS Score sub-components
rs_score = (
    0.40 * normalize(rs_gap)     +   # RS line above EMA9 by how much
    0.30 * normalize(rs_slope)   +   # RS rising how fast
    0.30 * rs_rating                 # percentile rank vs all 962 stocks
)
```

---

## Data Source

**Zerodha Kite API** (`kiteconnect` Python SDK)

```python
from kiteconnect import KiteConnect
kite = KiteConnect(api_key=os.getenv("KITE_API_KEY"))
kite.set_access_token(os.getenv("KITE_ACCESS_TOKEN"))

# Daily OHLCV fetch
data = kite.historical_data(
    instrument_token=token,
    from_date="2020-01-01",
    to_date=today,
    interval="day"
)
```

### Key Notes on Kite
- Historical data available from ~2010
- Daily candles: `interval="day"`
- Access token expires daily — must refresh each morning
- Instrument token for NiftyMidSml400 must be looked up from instruments master
- Rate limit: ~3 requests/second — implement throttling in data_loader.py

---

## Stock Universe

**File**: `data/universe.csv`  
**Source**: Pre-filtered NSE stocks  
**Count**: ~962 stocks  
**Filters applied**: Market cap > ₹500 Cr, 10-day avg notional > ₹15 Cr, Price > ₹50

**Columns**:
```
Stock Name | NSE Code | ISIN | Industry Name | sector_name | Sector Description
```

**Cross-reference with Kite**: Match via `trading_symbol` (NSE Code) or ISIN
from Kite instruments master.

---

## Project Structure

```
ema-compression-scanner/
│
├── CLAUDE.md                          ← You are here
├── .env                               ← API keys (gitignored)
├── .gitignore
├── requirements.txt
├── run_scanner.py                     ← Single entry point
│
├── config/
│   └── settings.yaml                 ← All thresholds and weights
│
├── data/
│   ├── universe.csv                  ← 962 NSE stocks (gitignored, large)
│   ├── cache/                        ← OHLCV parquet cache (gitignored)
│   └── db/
│       └── signals.db                ← SQLite signal history (gitignored)
│
├── scanner/
│   ├── __init__.py
│   ├── data_loader.py                ← Kite API fetch + cache logic
│   ├── indicators.py                 ← EMA, ATR, BB, KC, RS calculations
│   ├── gate.py                       ← Dual EMA gate + BB squeeze gate
│   ├── scorer.py                     ← Composite score (0-100)
│   └── screener.py                   ← Orchestrates full pipeline
│
├── results/                          ← GIT TRACKED — daily outputs
│   └── YYYY-MM-DD-signals.csv
│
└── notebooks/
    ├── 01_identify_compressions.ipynb
    ├── 02_measure_outcomes.ipynb
    ├── 03_correlation_analysis.ipynb
    └── 04_visual_validation.ipynb
```

---

## Git Strategy

```
COMMIT:   results/*.csv, config/, scanner/*.py, CLAUDE.md
IGNORE:   data/cache/, data/db/, .env, __pycache__
```

Commit message format:
```
scan: YYYY-MM-DD — N signals | top: STOCK1(score), STOCK2(score)
```

---

## Build Order (Follow This Sequence)

```
Step 1: config/settings.yaml          — all thresholds in one place
Step 2: scanner/data_loader.py        — Kite fetch + parquet cache
Step 3: scanner/indicators.py         — EMA, ATR, BB, KC, RS line
Step 4: scanner/gate.py               — dual gate + BB squeeze gate
Step 5: scanner/scorer.py             — composite score
Step 6: scanner/screener.py           — full pipeline orchestration
Step 7: run_scanner.py                — entry point + git commit
Step 8: notebooks/                    — research and backtesting
```

---

## Settings Reference (settings.yaml values)

```yaml
# EMA Dual Gate
ema_atr_threshold: 1.5          # ema_spread / ATR50 < this
ema_pct_threshold: 0.03         # ema_spread / EMA200 < this (3%)
compression_min_bars: 10        # minimum bars gate must hold

# ATR
atr_period: 50                  # ATR50 (not 14 — smooths EP spikes)

# Bollinger Bands
bb_period: 20                   # 4-week lookback — balanced responsiveness
bb_std: 2.0                     # 95.4% price containment — standard
bb_basis: "SMA"                 # SMA basis — TradingView default, widely comparable

# Keltner Channels
kc_period: 20                   # matched to BB period — apples to apples
kc_atr_mult: 1.5                # squeeze threshold — tight, high quality
kc_basis: "SMA"                 # SMA basis consistent with BB

# BB Squeeze Gate
squeeze_min_bars: 5
bb_width_percentile_max: 20     # bottom 20% of 52-week range

# RS Line
rs_benchmark: "NIFTY_MIDSML400" # Kite symbol for NiftyMidSml400
rs_ema_period: 9
rs_ema_timeframe: "weekly"
rs_slope_lookback: 4            # weeks

# Composite Score Weights
score_weights:
  ema_tightness: 0.25
  duration: 0.20
  volume_trend: 0.20
  bb_intensity: 0.15
  rs_strength: 0.20

# RS sub-weights
rs_weights:
  gap: 0.40
  slope: 0.30
  rating: 0.30

# Output
top_n_results: 15               # number of stocks in daily output
results_dir: "results/"
```

---

## Environment Variables (.env)

```
KITE_API_KEY=your_api_key
KITE_API_SECRET=your_api_secret
KITE_ACCESS_TOKEN=your_access_token   # refresh daily
```

---

## Key Decisions and Rationale (Do Not Change Without Discussion)

| Decision | Rationale |
|---|---|
| ATR50 not ATR14 | ATR14 stays elevated after EP moves, masking compression |
| BB(20, 2.0, SMA) | Standard 4-week lookback, 2.0 std = market standard, SMA basis = TradingView default |
| KC(20, 1.5, SMA) | Matched period to BB — consistent lookback window for squeeze comparison |
| NiftyMidSml400 benchmark | Matches actual universe — mid/small cap peer group |
| Weekly RS EMA9 | Smooths daily noise, reduces whipsaws |
| Parquet cache | Fast reads for 962 stocks × 5 years of daily data |
| SQLite for signal history | Zero-dependency, git-friendly audit trail |
| Results to git | Daily signal evolution becomes a trading journal |

---

## Failure Modes to Guard Against in Code

1. **Bear market signals** — add Nifty50 > its own EMA200 as market regime filter
2. **False breakouts** — volume must be 2x+ average on breakout bar
3. **Stale compression** — flag if compression > 18 months (120 weeks)
4. **Newly listed stocks** — minimum 250 bars of history required for EMA200
5. **Data gaps** — handle missing bars gracefully in data_loader.py

---

## Research Questions to Answer in Notebooks

```
Q1: Does longer compression duration → larger post-breakout move?
Q2: Does tighter EMA spread → faster EMA fanout?
Q3: Does BB squeeze duration add to EMA compression signal quality?
Q4: What % of dual-compressed stocks break up vs down?
Q5: Does prior RS strength predict breakout direction?
Q6: Which NSE sectors show this setup most reliably?
```

---

## Indicator Sanity Checks (Validate Against TradingView)

Before running full universe scan, validate each indicator on these stocks:
- Pick 2-3 stocks where you can visually verify on TradingView
- EMA50, EMA100, EMA200 values must match to 2 decimal places
- BB(20, 2.0, SMA basis) upper/lower must match TradingView exactly
- ATR(50) must match
- KC(20, 1.5, SMA basis) must match
- Note: TradingView BB uses SMA basis and rolling std — code must match this exactly
- Only then run on full universe
