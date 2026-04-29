# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the scanners

All scanners are triggered by PowerShell scripts that log to `logs/` and auto-commit results:

```powershell
.\run_fetch_data.ps1          # 4:05 PM — Kite auth + SQLite backfill/delta + manifest commit
.\run_dashboard.ps1           # 4:10 PM — circuit limits dashboard (main.py)
.\run_ema25_zl_scanner.ps1   # 4:25 PM — EMA25 ZL scanner
.\run_momentum_scanner.ps1    # momentum scanner
.\ema-compression-scanner\run_scanner.ps1  # 4:35 PM — EMA compression scanner
```

Run any Python script directly for debugging:

```bash
python fetch_data.py
python ema25_zl_scanner.py
python ema-compression-scanner/screener.py
python dashboard_generator.py
```

Install dependencies:

```bash
pip install requests bs4 python-dateutil yfinance tradingview-screener kiteconnect pyotp pyyaml pandas
```

## Architecture overview

### Data flow (daily, post 4:05 PM IST)

```
run_fetch_data.ps1
  → kite_auth.py          # TOTP login → updates .env KITE_ACCESS_TOKEN
                          # Skipped if token < 16h old (.kite_token_stamp)
  → fetch_data.py         # Kite instruments (filtered) → historical_data() backfill
                          # + quote() delta → .ohlc_data/market.db (SQLite)
                          # → .ohlc_data/data_manifest.csv (git-tracked)

All scanners → ohlc_db.py → .ohlc_data/market.db
```

### Central SQLite DB (`ohlc_db.py`)

`load_ohlc(symbol, lookback=400)` and `load_ohlc_many(symbols, lookback=400)` are the only DB entry points for scanners. Both return DataFrames with **lowercase columns** (`date`, `open`, `high`, `low`, `close`, `volume`) and `date` as a plain column (not index), oldest-first.

Instrument filter in `fetch_data.py`: `exchange=NSE`, `segment=NSE or INDICES`, no `-` in `tradingsymbol`. This excludes SME/BE-series/odd-lot instruments (~2,000–2,500 EQ stocks + indices, vs the raw 9,000+).

**Kite `quote()` field mapping**: `last_price` = today's close; `ohlc.close` = previous day's close. `fetch_data.py` always uses `last_price` for the delta close.

### Scanner pipeline — EMA compression (`ema-compression-scanner/`)

All thresholds live in `settings.yaml`. Pipeline:
1. `indicators.py` — `compute()` adds EMA50/100/200, ATR50, spread metrics; `bollinger_keltner()` adds BB(20,2.0) + KC(20,1.5) + `squeeze_on`; `zl25_stats()` + `rs_line()` are standalone
2. `gate.py` — EMA dual gate (spread < 1.5×ATR50 AND < 3% of EMA200, ≥10 bars); BB squeeze gate (BB inside KC ≥5 bars, width bottom 20%)
3. `scorer.py` — cross-candidate min-max normalization → 0-100 composite score
4. `screener.py` — orchestrates full pipeline, reads from SQLite, writes `ema_compression_latest.md`

### Scanner pipeline — EMA25 ZL (`ema25_zl_scanner.py`)

1. TradingView screener → watchlist (price > EMA25, MCap 1,000–1,00,000 Cr)
2. `load_ohlc(symbol)` → RS gate: daily RS > weekly RS EMA9 AND EMA9 rising
3. ZLEMA25 direction + `zl25_turn_stats()` → days since last turn-up, % gain
4. `bb_kc_squeeze()` → BB(20,2.0,SMA) inside KC(20,1.5,SMA) on last bar
5. Writes `ema25_zl_scans/ema25_zl_scans.md`

### Dashboard (`dashboard_generator.py`)

Reads today's block from 6 markdown files (swing, momentum, weekly-RS, EMA25-ZL, EMA compression, circuit limits), cross-references symbols, builds `dashboard.html` with confluence scoring.

### Circuit limits (`main.py`)

Fetches `nseindia.com/api/eqsurvactions` → parses CSV → generates `index.html` + `NSE_Circuit_Limits.md`. Color code: 🟨 20→10% · 🟥 10→5% · 🟩 5→10% · 🟦 10→20%.

## Key conventions

**ATR**: EMA compression scanner uses SMA ATR (`tr.rolling(period).mean()`) for BB/KC to match TradingView's `ta.sma(ta.tr)`. Wilder EWM is available as `kc_atr_wilder=True` but not the default.

**ZLEMA25**: `2 * EMA(25) - EMA(EMA(25))`. "Rising" = last bar > second-to-last bar.

**RS benchmark**: Kite tradingsymbol `"NIFTY MIDSML 400"` (with spaces). Stored in SQLite like any other symbol.

**Trading-day gap detection**: Use integer position-index differences, not calendar-day differences, to handle NSE holidays correctly.

**Git**: Only `data_manifest.csv` is committed from the data layer. `market.db` is gitignored. Scan output markdown files are committed by their respective PS1 scripts.

## Output files (git-tracked)

| File | Written by |
|------|-----------|
| `NSE_Circuit_Limits.md`, `index.html` | `main.py` |
| `ema25_zl_scans/ema25_zl_scans.md` | `ema25_zl_scanner.py` |
| `ema-compression-scanner/ema_compression_scans/ema_compression_latest.md` | `screener.py` |
| `momentum_scans/momentum_scans.md` | `momentum_scanner.py` |
| `momentum_scans/momentum_rs_weekly_scans.md` | `momentum_rs_weekly_scanner.py` |
| `swing_scans/swing_scans.md` | `swing_scanner.py` |
| `ema_screener_changes.md` | `nse_ema_daily.py` |
| `dashboard.html` | `dashboard_generator.py` |
| `.ohlc_data/data_manifest.csv` | `fetch_data.py` |

## Environment (`.env` inside `ema-compression-scanner/`)

```
KITE_API_KEY=
KITE_API_SECRET=
KITE_ACCESS_TOKEN=      # auto-updated by kite_auth.py
KITE_USER_ID=
KITE_PASSWORD=
KITE_TOTP_SECRET=
```

Stock universe file (gitignored, must be present locally):
`NSE_500cr_15CrNotional10D_50rs_sector_industry.csv`
