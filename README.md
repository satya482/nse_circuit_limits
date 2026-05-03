# NSE + US Circuit Limits & Scanner Suite

Daily post-market scanner suite for NSE-listed Indian equities and US equities.
Runs automatically via Windows Task Scheduler.

## Scanners

### 1. EMA25 ZL Scanner (`ema25_zl_scanner.py`)
Identifies stocks where ZLEMA25 (Zero-Lag EMA 25) has recently turned up,
filtered by RS strength vs Nifty MidSmallcap 400.

- **Watchlist**: TradingView screener — NSE common equity, price > ₹50, MCap ₹1,000–1,00,000 Cr, price > EMA25
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

### 3. ZL Squeeze Scanner (`zl_squeeze_scanner.py`)
Finds stocks where ZLEMA25 has just turned up AND a BB Squeeze is active simultaneously — the tightest, most actionable setups.

- **Watchlist**: TradingView screener — NSE common equity, price > ₹50, MCap ₹800 Cr – ₹1 Lakh Cr
- **RS gate**: Daily RS > Daily RS EMA21 AND EMA21 rising
- **Signal**: ZLEMA25 rising on last bar AND BB(20,2.0,SMA) fully inside KC(20,1.5,SMA ATR)
- **Squeeze Days**: Consecutive bars the squeeze has been active (longer = more coiled)
- **Sort**: ZL Days ascending (freshest turn-up first), then squeeze days descending as tiebreaker
- **Output**: `zl_squeeze_scans/zl_squeeze_scans.md`

### 4. US ZL Squeeze Scanner (`us_zl_squeeze_scanner.py`)
Mirrors the NSE ZL Squeeze Scanner for US markets. Data sourced from yfinance
(no broker auth required); cached locally in SQLite via `fetch_us_data.py`.

- **Universe**: TradingView screener — NYSE + NASDAQ common equity, price > $5, MCap $300M–$10B, avg 10d vol > 300K
- **Data**: `fetch_us_data.py` → `.us_ohlc_data/us_market.db` (gitignored); manifest: `us_data_manifest.csv`
- **RS benchmark**: SPY (×100 scale)
- **Relative Volume gate**: today's vol / 20d avg > 1.5x (configurable)
- **RS gates** (OR logic — pass at least one enabled gate):
  - `RS_EMA9_GATE`: Daily RS > EMA9 AND EMA9 rising
  - `RS_EMA21_GATE`: Daily RS > EMA21 AND EMA21 rising
  - `RS_WEEKLY_EMA9_GATE`: Daily RS > Weekly RS EMA9 AND weekly EMA9 rising (completed weeks only)
- **Signal**: ZLEMA25 rising AND BB(20,2.0,SMA) fully inside KC(20,1.5,SMA ATR) on last bar
- **Sort**: RS gates passed desc → ZL Days asc → Squeeze Days desc
- **Output**: `us_zl_squeeze_scans/us_zl_squeeze_scans.md`

### 5. Momentum Scanner (`momentum_scanner.py`)
Swing entry scanner — stocks pulling back to ZLEMA25 or deep EMAs.

- **Watchlist**: TradingView screener — 1-week change > 5%, MCap ₹1,000–1,00,000 Cr
- **Entry signals** (all require ZLEMA25 rising):
  - **STRONG**: Low touched ZLEMA25 + EMA20 rising
  - **PRIMARY**: Low touched ZLEMA25
  - **DEEP PULLBACK**: Low touched EMA50/100/200, closed green above it
- **RS gate**: Daily RS > RS EMA9, Daily RS > RS EMA21, Weekly RS EMA9 rising
- **Output**: `momentum_scans/momentum_scans.md`

### 6. Momentum RS Weekly Scanner (`momentum_rs_weekly_scanner.py`)
Filters momentum watchlist by weekly RS strength for longer-hold setups.
- **Output**: `momentum_scans/momentum_rs_weekly_scans.md`

### 7. Circuit Limits Dashboard (`main.py`)
Fetches NSE circuit limit changes from `nseindia.com/api/eqsurvactions`.

- **Color code**: 🟨 20→10% · 🟥 10→5% · 🟩 5→10% · 🟦 10→20%
- **Output**: `index.html`, `NSE_Circuit_Limits.md`, `nse.csv`

### 8. EMA Screener Daily Diff (`nse_ema_daily.py`)
Tracks daily additions/deletions from a TradingView EMA screener snapshot.
- **Output**: `ema_screener_changes.md`

### 9. Dashboard Aggregator (`dashboard_generator.py`)
Reads today's block from all scan markdown files, cross-references symbols,
computes confluence score, and renders `dashboard.html`.

---

## Data Architecture

### NSE (Kite)
```
fetch_data.py (4:05 PM IST daily)
  ├── kite_auth.py        → refreshes Kite access token (TOTP, skipped if < 16h old)
  ├── Kite instruments()  → filters: exchange=NSE, segment=NSE/INDICES, no '-' in symbol
  ├── historical_data()   → 2y backfill for symbols with < 200 rows
  ├── quote()             → delta update (today's bar) in batches of 50
  └── .ohlc_data/market.db   ← SQLite (gitignored)
      └── ohlc_db.py     → load_ohlc() / load_ohlc_many() — used by all NSE scanners
```
`data_manifest.csv` (symbol / last_date / row_count) is git-tracked.

### US (yfinance)
```
fetch_us_data.py (4:40 PM IST daily)
  ├── TradingView screener → universe (NYSE + NASDAQ, MCap $300M–$10B, price > $5, vol > 300K)
  ├── yf.download()        → 2y backfill (batches of 100) for new symbols
  ├── yf.download()        → 5d delta for existing symbols
  └── .us_ohlc_data/us_market.db   ← SQLite (gitignored)
      └── us_ohlc_db.py   → load_ohlc() — used by US scanners
```
`us_data_manifest.csv` (symbol / last_date / row_count) is git-tracked.

---

## Schedule (Windows Task Scheduler)

| Time (IST) | Script | Action |
|---|---|---|
| 3:30 PM | `run_ema_screener.ps1` | EMA screener daily diff |
| 3:35 PM | `run_fetch_data.ps1` | Kite auth + NSE SQLite backfill/delta |
| 3:40 PM | `run_swing_scanner.ps1` | Swing scan (yfinance) |
| 3:45 PM | `run_momentum_scanner.ps1` | Momentum scan |
| 3:50 PM | `run_momentum_rs_weekly_scanner.ps1` | Momentum RS Weekly scan |
| 3:55 PM | `run_ema25_zl_scanner.ps1` | EMA25 ZL scan |
| 4:00 PM | `run_zl_squeeze_scanner.ps1` | NSE ZL Squeeze scan |
| 4:05 PM | `ema-compression-scanner\run_scanner.ps1` | EMA compression scan |
| 4:10 PM | `run_us_fetch_data.ps1` | US yfinance SQLite backfill/delta |
| 4:15 PM | `run_dashboard_generator.ps1` | Dashboard aggregator (after all NSE scans) |
| 4:20 PM | `run_us_zl_squeeze_scanner.ps1` | US ZL Squeeze scan |
| 4:30 PM | `run_scan_status_mailer.ps1` | Scanner status email |
| 5:05 PM | `run_dashboard.ps1` | NSE circuit limits dashboard (exchange publishes at 5 PM) |

---

## Setup

```powershell
pip install requests bs4 python-dateutil yfinance tradingview-screener kiteconnect pyotp pyyaml pandas
```

US scanners use yfinance and require no additional credentials. NSE scanners require Kite credentials (see below).

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
| RS benchmark (NSE) | Kite symbol `NIFTY MIDSML 400` (with spaces) |
| RS benchmark (US) | `SPY`, scaled ×100 |
| ZL Chg% reference | Close of the candle immediately before the ZLEMA25 turn candle |
| Weekly RS EMA9 | Only completed weekly bars used (drops current partial week) |
| Trading-day gaps | Integer position-index diff, not calendar days (handles NSE holidays) |
| DB columns | All lowercase: `date`, `open`, `high`, `low`, `close`, `volume` |
| Kite quote close | `last_price` = today's close; `ohlc.close` = previous day |
