# Institutional Accumulation Intelligence System — Technical Specification

## 1. Goal

Build a local-first NSE swing-trading decision-support system that identifies stocks likely to start a 1–10 day swing move before they become obvious movers.

The system should not simply report stocks that already moved. It should detect developing accumulation, base formation, relative strength improvement, volatility contraction, sector leadership, and breakout readiness.

Primary output: a GitHub Pages HTML dashboard showing prioritized watchlist candidates with evidence, scores, trigger levels, risk levels, and historical analogs.

---

## 2. Core Philosophy

Most scanners detect:
- top gainers
- high volume
- high delivery %
- new highs

This system should detect earlier-stage opportunities:

1. Accumulation begins
2. Base forms
3. Relative strength improves
4. Supply dries up
5. Price approaches resistance
6. Breakout triggers
7. Follow-through is tracked

The system should rank stocks by evidence quality, not by one indicator.

---

## 3. System Architecture

### 3.1 Local Backend

Runs on local machine.

Responsibilities:
- Ingest NSE bhavcopy / delivery data
- Maintain historical OHLCV + delivery database
- Calculate technical metrics
- Calculate accumulation and readiness scores
- Generate static reports
- Push output to GitHub Pages repository

Suggested stack:
- Python
- SQLite
- Pandas / Polars
- Plotly or lightweight HTML charts
- Jinja2 templates
- GitHub Pages for frontend hosting

---

## 4. Data Sources

### 4.1 Required Daily Data

For each stock:

- Date
- Symbol
- Open
- High
- Low
- Close
- Volume
- Delivery quantity
- Delivery percentage
- Previous close
- Series / segment filter

### 4.2 Benchmark Data

Required:
- NIFTYMIDSML400

Optional:
- NIFTY 50
- NIFTY 500
- Sector indices

### 4.3 Optional Fundamental / Static Data

Useful but not mandatory:
- Sector
- Industry
- Free float shares
- Market cap
- Earnings date
- F&O eligibility
- ASM/GSM status

---

## 5. Database Schema

### 5.1 prices

```sql
CREATE TABLE IF NOT EXISTS prices (
    symbol TEXT NOT NULL,
    trade_date DATE NOT NULL,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    prev_close REAL,
    volume INTEGER,
    delivery_qty INTEGER,
    delivery_pct REAL,
    series TEXT,
    PRIMARY KEY (symbol, trade_date)
);
```

### 5.2 symbols

```sql
CREATE TABLE IF NOT EXISTS symbols (
    symbol TEXT PRIMARY KEY,
    name TEXT,
    sector TEXT,
    industry TEXT,
    free_float_shares REAL,
    market_cap REAL,
    active INTEGER DEFAULT 1
);
```

### 5.3 indicators

```sql
CREATE TABLE IF NOT EXISTS indicators (
    symbol TEXT NOT NULL,
    trade_date DATE NOT NULL,
    ema20 REAL,
    ema50 REAL,
    ema200 REAL,
    atr14 REAL,
    atr_pct REAL,
    bb_width REAL,
    rs_line REAL,
    rs_ema21 REAL,
    rs_slope_10 REAL,
    rs_acceleration REAL,
    volume_sma20 REAL,
    delivery_sma5 REAL,
    delivery_sma20 REAL,
    delivery_percentile_252 REAL,
    close_position REAL,
    PRIMARY KEY (symbol, trade_date)
);
```

### 5.4 scores

```sql
CREATE TABLE IF NOT EXISTS scores (
    symbol TEXT NOT NULL,
    trade_date DATE NOT NULL,
    market_regime_score REAL,
    sector_score REAL,
    accumulation_score REAL,
    structure_score REAL,
    strength_score REAL,
    compression_score REAL,
    breakout_readiness_score REAL,
    risk_quality_score REAL,
    total_score REAL,
    grade TEXT,
    stage TEXT,
    PRIMARY KEY (symbol, trade_date)
);
```

### 5.5 setup_events

```sql
CREATE TABLE IF NOT EXISTS setup_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    trade_date DATE NOT NULL,
    event_type TEXT NOT NULL,
    event_strength REAL,
    description TEXT
);
```

---

## 6. Indicator Calculations

### 6.1 Trend Metrics

Calculate:
- EMA20
- EMA50
- EMA200
- Close above EMA20
- Close above EMA50
- Close above EMA200
- EMA20 above EMA50

Trend score example:
- Close > EMA20: +25
- Close > EMA50: +25
- EMA20 > EMA50: +25
- Close > EMA200: +25

---

### 6.2 Relative Strength

Benchmark:
- Default: NIFTYMIDSML400

Formula:

```text
RS Line = Stock Close / Benchmark Close
RS EMA = EMA(RS Line, 21)
RS Slope 10 = linear regression slope of RS Line over 10 sessions
RS Acceleration = current RS slope - previous RS slope
```

Reward:
- RS above RS EMA21
- RS slope positive
- RS making 20-day high before price
- RS acceleration positive

---

### 6.3 Delivery Trend

Calculate:
- Delivery SMA5
- Delivery SMA20
- Delivery percentile over 252 trading days
- Delivery slope over 5 and 20 days
- Count of high-delivery days in last 10 sessions

Important:
Do not rely only on one-day delivery spike.

Delivery trend is stronger when:
- Delivery SMA5 > Delivery SMA20
- Delivery slope is positive
- Multiple days above P80/P90/P95
- Price does not fall despite high delivery

---

### 6.4 Volatility Compression

Calculate:
- ATR14
- ATR percentage = ATR14 / Close
- Bollinger Band width
- 20-day range contraction
- NR7 / narrow range flags

Compression is strong when:
- ATR percentile is near 60-day low
- Bollinger Band width is contracting
- Daily ranges are becoming smaller
- Volume dries up near support or before resistance breakout

---

### 6.5 Base Detection

A stock is in a base when:

Required:
- At least 15 trading days in a bounded range
- Range depth below configurable threshold, for example 8–18%
- Price remains near or above EMA20/EMA50
- No major breakdown

Base quality factors:
- Higher lows
- Resistance tested multiple times
- Pullbacks become smaller
- ATR contracts inside base
- Volume dries up during pullbacks

Suggested fields:
- base_start_date
- base_days
- base_high
- base_low
- resistance_price
- support_price
- distance_to_breakout_pct

---

## 7. Advanced Evidence Engines

## 7.1 Accumulation Engine

Purpose:
Detect institutional accumulation before breakout.

Signals:
- Delivery trend rising
- High delivery days with small price change
- Price holding despite high volume
- Up-volume greater than down-volume
- Down days occur on lower volume
- Closing position near high of candle
- Multiple P90/P95 delivery days inside base

Score: 0–100

Example scoring:
- Delivery SMA5 > SMA20: +15
- Delivery percentile > 90: +15
- 3 or more high-delivery days in last 10: +15
- Price flat or up while delivery rises: +20
- Up-volume/down-volume ratio positive: +15
- Close position above 60% of range: +10
- Low distribution count: +10

---

## 7.2 Smart Money Absorption Score

Purpose:
Find days where supply may have been absorbed.

Strong absorption day:
- Delivery above average
- Volume above average
- Candle spread small
- Close not weak
- Price does not fall much

Formula idea:

```text
Absorption = High Delivery + High Volume + Small Range + Close Resilience
```

Reward:
- High delivery
- Small candle body/range
- Close in upper half
- Low downside movement

Flag:
`ABSORPTION_DAY`

---

## 7.3 Supply Exhaustion Score

Purpose:
Detect when sellers may be drying up.

Signals:
- Lowest volume in 20/30 days
- Lowest ATR in 20/60 days
- Narrow candle
- Price holds support
- No breakdown on weak market day

Flag:
`SUPPLY_DRY_UP`

---

## 7.4 Failed Breakdown Detector

Purpose:
Find shakeout/reclaim patterns.

Condition:
- Price breaks below recent support intraday or by close
- Recovers back into base quickly
- Close returns above support
- Delivery or volume above average

This is a strong institutional footprint.

Flag:
`FAILED_BREAKDOWN_RECLAIM`

Score impact:
High positive if reclaim occurs within 1–3 sessions.

---

## 7.5 Failed Breakout Detector

Purpose:
Avoid traps.

Condition:
- Price breaks above resistance
- Fails to close above resistance
- Long upper wick
- High volume
- Close weak

Flag:
`FAILED_BREAKOUT`

Score impact:
Negative.

---

## 7.6 Resistance Pressure Score

Purpose:
Measure how close a stock is to breaking resistance.

Factors:
- Number of resistance touches
- Closing near resistance
- Pullbacks after each touch become smaller
- Higher lows
- Distance to resistance below 1–3%

Score high when price repeatedly tests resistance without breaking down.

---

## 7.7 Float Rotation

Optional but powerful.

Formula:

```text
Float Rotation % = Sum(delivery_qty over N days) / free_float_shares * 100
```

Useful windows:
- 20 days
- 30 days
- 60 days

High float rotation inside a base may indicate serious accumulation.

Requires free-float data.

---

## 7.8 Volume-at-Price During Base

Purpose:
Identify where volume is concentrated inside the base.

Approximation:
- Divide base price range into buckets
- Allocate daily volume to bucket based on close or typical price
- Identify high-volume zones

Useful outputs:
- Base POC price
- Volume concentration near resistance
- Volume concentration near support

Bullish:
- Heavy volume near upper half of base
- Support volume shelf

---

## 7.9 Sector Synchronization

Purpose:
Improve probability by requiring sector participation.

For each sector:
- % stocks above EMA20
- % stocks with positive RS slope
- % stocks near 20-day high
- Average delivery percentile
- Number of stocks with accumulation score > 70

Sector score should influence stock score.

---

## 7.10 Historical Similarity Engine

Purpose:
Compare today’s setup with past setups.

Feature vector:
- RS slope
- RS acceleration
- Delivery percentile
- Delivery trend slope
- ATR percentile
- BB width percentile
- Distance to resistance
- Base days
- Base depth
- Accumulation score
- Structure score
- Sector score

For each candidate:
- Find historical top N similar setup days
- Show average 5-day forward return
- Average 10-day forward return
- Win rate
- Median drawdown
- Best/worst outcome

Suggested method:
- Normalize features
- Use cosine similarity or Euclidean distance
- Exclude same stock recent overlapping dates
- Use only dates with enough future data

---

## 8. Composite Scoring Model

### 8.1 Main Score

```text
Total Score =
  15% Market Regime
+ 15% Sector Leadership
+ 20% Relative Strength
+ 20% Accumulation
+ 15% Structure / Base Quality
+ 10% Compression
+ 5% Risk Quality
```

Weights should be configurable.

### 8.2 Grades

| Score | Grade |
|---:|---|
| 90–100 | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| <60 | Avoid |

### 8.3 Stages

Each stock should be assigned one stage:

1. Emerging Candidate
2. Accumulation Detected
3. Base Maturing
4. Ready Soon
5. Triggered
6. In Trend
7. Failed / Avoid

---

## 9. Trigger and Risk Model

For each Ready Soon stock, calculate:

### 9.1 Trigger Price

Possible trigger:
- base_high + small buffer
- previous day high + small buffer
- resistance_price + 0.1–0.3%

### 9.2 Invalidation / Stop

Possible stop:
- below breakout day low
- below base support
- below EMA20
- ATR-based stop

### 9.3 Risk Quality

Penalize:
- Stock too extended from EMA20
- Stop distance too wide
- Reward/risk less than 2:1
- Breakout too far above base

---

## 10. Dashboard Requirements

### 10.1 Home Page: Market Radar

Sections:
1. Market Regime
2. Sector Leadership
3. Tomorrow’s Watchlist
4. Ready Soon
5. Triggered Today
6. Failed Breakouts
7. In Trend
8. Historical Similarity Highlights

---

### 10.2 Candidate Table

Columns:
- Rank
- Symbol
- Stage
- Grade
- Total Score
- Accumulation Score
- RS Score
- Structure Score
- Compression Score
- Sector Score
- Delivery Trend
- Delivery Percentile
- Distance to Breakout %
- Trigger Price
- Stop Price
- Risk %
- Base Days
- Sector
- TradingView Link

---

### 10.3 Evidence Matrix

For each stock:

| Evidence | Status |
|---|---|
| Market regime supportive | ✅ / ❌ |
| Sector leader | ✅ / ❌ |
| RS above 21 EMA | ✅ / ❌ |
| RS slope positive | ✅ / ❌ |
| Delivery trend rising | ✅ / ❌ |
| Volatility contracting | ✅ / ❌ |
| Tight base | ✅ / ❌ |
| Resistance pressure | ✅ / ❌ |
| Supply dry-up | ✅ / ❌ |
| No failed breakout | ✅ / ❌ |
| Risk/reward acceptable | ✅ / ❌ |

---

### 10.4 Setup Timeline

Example:

```text
Day -20: Base begins
Day -15: ATR contraction starts
Day -12: RS turns positive
Day -8: Delivery trend rises
Day -5: Third resistance test
Day -2: Supply dry-up
Day 0: Breakout triggered
```

---

### 10.5 Stock Detail Page

For each symbol:
- Price chart
- Delivery trend chart
- RS line chart
- ATR / BB width compression chart
- Base range visualization
- Evidence matrix
- Setup timeline
- Trigger and stop
- Historical similar setups

---

## 11. Report Generation

Output folder:

```text
docs/
  index.html
  sectors.html
  candidates.html
  triggered.html
  failed.html
  stocks/
    SPARC.html
    KPIT.html
  assets/
    style.css
    app.js
```

This folder can be published with GitHub Pages.

---

## 12. CLI Commands

Suggested commands:

```bash
python ingest.py --date 2026-07-09 --file data/bhavcopy.csv
python calculate_indicators.py
python score_setups.py --date 2026-07-09
python generate_reports.py --date 2026-07-09
python publish.py
```

Combined command:

```bash
python run_daily.py --date 2026-07-09
```

---

## 13. Configuration File

Create `config.yaml`.

```yaml
benchmark: NIFTYMIDSML400

base_detection:
  min_days: 15
  max_depth_pct: 18
  near_breakout_pct: 3

scoring_weights:
  market_regime: 15
  sector: 15
  relative_strength: 20
  accumulation: 20
  structure: 15
  compression: 10
  risk_quality: 5

delivery:
  high_percentile: 90
  extreme_percentile: 95
  trend_short_window: 5
  trend_long_window: 20

risk:
  min_reward_risk: 2
  max_stop_pct: 8
  max_extension_from_ema20_pct: 10

similarity:
  lookback_days: 750
  top_n: 10
  forward_return_days:
    - 5
    - 10
```

---

## 14. Quality Checks

The system should warn when:
- Delivery data missing
- Benchmark data missing
- Symbol has fewer than 252 days of history
- Abnormal volume spike due to split/bonus
- Close price is zero/null
- Duplicate data exists
- Free float data is missing

---

## 15. Backtesting Requirements

For every signal type:
- Record signal date
- Entry trigger
- Stop
- 5-day return
- 10-day return
- Max favorable excursion
- Max adverse excursion
- Win rate
- Average return
- Median return
- Failure rate

Backtest separately by:
- Market regime
- Sector score
- Grade
- Stage
- Accumulation score bucket

---

## 16. MVP Scope

Build first:

1. Data ingestion into SQLite
2. EMA, ATR, RS, delivery trend
3. Basic base detection
4. Accumulation score
5. Breakout readiness score
6. GitHub Pages dashboard
7. TradingView links
8. Evidence matrix

Do not start with historical similarity engine. Add it after the basic scanner is stable.

---

## 17. Phase 2 Scope

Add:
- Failed breakdown detector
- Supply dry-up detector
- Failed breakout detector
- Sector synchronization
- Setup timeline
- Risk model
- Stock detail pages

---

## 18. Phase 3 Scope

Add:
- Float rotation
- Volume-at-price during base
- Historical similarity engine
- Backtest analytics
- AI-generated explanation text

---

## 19. Example AI Explanation

For each stock, generate a short explanation:

```text
SPARC is ranked A because RS has been rising for 14 sessions, delivery SMA5 is above delivery SMA20, delivery percentile is above 90 for 4 of the last 10 sessions, ATR is near a 60-day low, and price is only 1.2% below a six-week resistance. Risk is acceptable with a 5.4% stop distance. Similar historical setups showed positive 10-day returns in 68% of cases.
```

---

## 20. Important Notes

This system is not intended to be foolproof. It should improve selection quality by requiring multiple independent evidence layers.

The final trading decision should still include:
- chart review
- market context
- news/earnings check
- risk management
- position sizing

Primary objective:
Reduce 500 charts to 10–30 high-quality candidates before the move becomes obvious.
