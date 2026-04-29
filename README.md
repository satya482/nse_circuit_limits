# NSE Circuit Limits & Scanner Suite

Daily post-market scanner suite for NSE-listed Indian equities. Runs automatically
after 4:05 PM IST on trading days via Windows Task Scheduler.

## Scanners

### 1. EMA25 ZL Scanner (`ema25_zl_scanner.py`)
Identifies stocks where ZLEMA25 (Zero-Lag EMA 25) has recently turned up,
filtered by RS strength vs Nifty MidSmallcap 400.

- **Watchlist**: TradingView screener — NSE common equity, price > ₹100, MCap ₹1,000–1,00,000 Cr, price > EMA25
- **RS gate**: Daily RS line > Weekly RS EMA9 AND weekly RS EMA9 rising
- **Signals**: ZLEMA25 Rising / Watch (pullback)
- **Extras**: BB(20,2.0,SMA) inside KC(20,1.5,SMA) squeeze flag, days since last ZL turn-up, % gain since
- **Output**: `ema25_zl_scans/ema25_zl_scans.md`

### 2. EMA Compression + BB Squeeze Scanner (`ema-compression-scanner/screener.py`)
Finds stocks where EMA50/100/200 are converging (structural compression) AND
Bollinger Bands are inside Keltner Channels (timing coil). Historically precedes explosive moves.

- **Universe**: ~962 NSE stocks from `NSE_500cr_15CrNotional10D_50rs_sector_industry.csv`
- **Gate 1 — EMA Dual**: spread < 1.5×ATR50 AND < 3% of EMA200 for ≥10 consecutive bars
- **Gate 2 — BB Squeeze**: BB(20,2.0) fully inside KC(20,1.5) for ≥5 bars, BB width in bottom 20% of 52-week range
- **Gate 3 — RS**: Weekly RS vs NiftyMidSml400 above EMA9 AND 4-week slope positive
- **Score**: 0–100 composite (EMA tightness 25% · duration 20% · volume contraction 20% · BB intensity 15% · RS strength 20%)
- **Output**: `ema-compression-scanner/ema_compression_scans/ema_compression_latest.md`

### 3. Momentum Scanner (`momentum_scanner.py`)
Swing entry scanner — stocks pulling back to ZLEMA25 or deep EMAs.

- **Watchlist**: TradingView screener — 1-week change > 5%, MCap ₹1,000–1,00,000 Cr
- **Entry signals** (all require ZLEMA25 rising):
  - **STRONG**: Low touched ZLEMA25 + EMA20 rising
  - **PRIMARY**: Low touched ZLEMA25
  - **DEEP PULLBACK**: Low touched EMA50/100/200, closed green above it
- **RS gate**: Daily RS > RS EMA9, Daily RS > RS EMA21, Weekly RS EMA9 rising
- **Output**: `momentum_scans/momentum_scans.md`

### 4. Momentum RS Weekly Scanner (`momentum_rs_weekly_scanner.py`)
Filters momentum watchlist by weekly RS strength for longer-hold setups.
- **Output**: `momentum_scans/momentum_rs_weekly_scans.md`

### 5. Circuit Limits Dashboard (`main.py`)
Fetches NSE circuit limit changes from `nseindia.com/api/eqsurvactions`.

- **Color code**: 🟨 20→10% · 🟥 10→5% · 🟩 5→10% · 🟦 10→20%
- **Output**: `index.html`, `NSE_Circuit_Limits.md`, `nse.csv`

### 6. EMA Screener Daily Diff (`nse_ema_daily.py`)
Tracks daily additions/deletions from a TradingView EMA screener snapshot.
- **Output**: `ema_screener_changes.md`

### 7. Dashboard Aggregator (`dashboard_generator.py`)
Reads today's block from all scan markdown files, cross-references symbols,
computes confluence score, and renders `dashboard.html`.

---

## Data Architecture

```
fetch_data.py (4:05 PM daily)
  ├── kite_auth.py        → refreshes Kite access token (TOTP, skipped if < 16h old)
  ├── Kite instruments()  → filters: exchange=NSE, segment=NSE/INDICES, no '-' in symbol
  ├── historical_data()   → backfill for symbols with < 200 rows
  ├── quote()             → delta update (today's bar) in batches of 500
  └── .ohlc_data/market.db   ← central SQLite (gitignored)
      └── ohlc_db.py     → load_ohlc() / load_ohlc_many() — used by all scanners
```

`data_manifest.csv` (symbol / last_date / row_count) is the only git-tracked data artifact.

---

## Schedule (Windows Task Scheduler)

| Time (IST) | Script | Action |
|---|---|---|
| 4:05 PM | `run_fetch_data.ps1` | Kite auth + SQLite backfill/delta |
| 4:10 PM | `run_dashboard.ps1` | Circuit limits dashboard |
| 4:25 PM | `run_ema25_zl_scanner.ps1` | EMA25 ZL scan |
| 4:35 PM | `ema-compression-scanner\run_scanner.ps1` | EMA compression scan |
| — | `run_momentum_scanner.ps1` | Momentum scan |

---

## Setup

```powershell
pip install requests bs4 python-dateutil yfinance tradingview-screener kiteconnect pyotp pyyaml pandas
```

Copy and fill in Kite credentials at `ema-compression-scanner/.env`:
```
KITE_API_KEY=
KITE_API_SECRET=
KITE_ACCESS_TOKEN=
KITE_USER_ID=
KITE_PASSWORD=
KITE_TOTP_SECRET=
```

Place `NSE_500cr_15CrNotional10D_50rs_sector_industry.csv` in the repo root (gitignored).

---

## Key Indicator Conventions

| Convention | Detail |
|---|---|
| ATR for KC | SMA ATR (`tr.rolling(n).mean()`) — matches TradingView `ta.sma(ta.tr)` |
| ZLEMA25 | `2×EMA(25) − EMA(EMA(25))` |
| RS benchmark | Kite symbol `NIFTY MIDSML 400` (with spaces) |
| Trading-day gaps | Integer position-index diff, not calendar days (handles NSE holidays) |
| DB columns | All lowercase: `date`, `open`, `high`, `low`, `close`, `volume` |
| Kite quote close | `last_price` = today's close; `ohlc.close` = previous day |
