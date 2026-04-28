#!/usr/bin/env python3
"""
NSE EMA25 ZL Scanner
Run after 4:20 PM IST on trading days.

Watchlist filters (TradingView):
  - NSE common equity
  - Price > 100 INR
  - 1-week change > 5%
  - Market cap 10B – 1T INR  (≈ 1,000 Cr – 1 Lakh Cr)
  - Price > EMA25

RS filter (both required):
  - Daily RS Line > Weekly RS EMA9
  - Weekly RS EMA9 is rising
  RS Line = (stock_close / Nifty MidSmallcap 400) * 1000

For each RS-passing stock:
  - Compute ZLEMA25 direction (rising / flat-down)
  - Compute zl25_turn_stats(): days since last ZLEMA25 turn-up, % gain since

OHLC cache: .ema25_ohlc_cache/{SYMBOL}.csv  (committed to git, 120-day delta)
Output:     ema25_zl_scans/ema25_zl_scans.md
"""

import sys, os, csv
from datetime import datetime, date, timedelta
from concurrent.futures import ThreadPoolExecutor

import requests
import yfinance as yf
import pandas as pd
from tradingview_screener import Query, col

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR    = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR   = os.path.join(REPO_DIR, "ema25_zl_scans")
CACHE_DIR   = os.path.join(REPO_DIR, ".ema25_ohlc_cache")
INDEX_CACHE = os.path.join(REPO_DIR, ".niftymidsml400_cache.csv")
TODAY       = datetime.now().strftime("%Y-%m-%d")
MD_FILE     = os.path.join(SCANS_DIR, "ema25_zl_scans.md")

MC_LOW      = 1_000     * 1_00_00_000   # 1000 Cr  = 10B INR
MC_HIGH     = 1_00_000  * 1_00_00_000   # 1L Cr    = 1T INR
ZL_TURN_CAP = 60
FILTER_1W_CHANGE = False   # True = require 1-week price change > 5%; False = no filter
CACHE_MAX   = 280   # rows kept per symbol (280 needed for BB width pct rank over 52w)
INDEX_NAME  = "Nifty MidSmallcap 400"
NSE_ARCH    = "https://nsearchives.nseindia.com/content/indices/ind_close_all_{}.csv"


# ── Indicators ────────────────────────────────────────────────────────────────
def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()

def zlema(s: pd.Series, n: int) -> pd.Series:
    e = ema(s, n)
    return 2 * e - ema(e, n)

def _atr_wilder(high: pd.Series, low: pd.Series, close: pd.Series, period: int) -> pd.Series:
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low  - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    return tr.ewm(span=period, adjust=False).mean()

def bb_kc_squeeze(df: pd.DataFrame) -> bool:
    """True if BB(20,2.0,SMA) is fully inside KC(20,1.5,SMA+WilderATR) on the last bar."""
    if len(df) < 21:
        return False
    c = df["Close"].astype(float)
    h = df["High"].astype(float)
    l = df["Low"].astype(float)

    bb_basis = c.rolling(20).mean()
    bb_std   = c.rolling(20).std()
    bb_upper = bb_basis + 2.0 * bb_std
    bb_lower = bb_basis - 2.0 * bb_std

    kc_basis = c.rolling(20).mean()
    kc_atr   = _atr_wilder(h, l, c, 20)
    kc_upper = kc_basis + 1.5 * kc_atr
    kc_lower = kc_basis - 1.5 * kc_atr

    return bool(bb_upper.iloc[-1] < kc_upper.iloc[-1] and bb_lower.iloc[-1] > kc_lower.iloc[-1])

def zl25_turn_stats(zl25: pd.Series, closes: pd.Series) -> tuple[int, float]:
    n     = len(zl25)
    limit = max(2, n - ZL_TURN_CAP)
    for i in range(n - 1, limit - 1, -1):
        if zl25.iloc[i] > zl25.iloc[i - 1] and zl25.iloc[i - 1] <= zl25.iloc[i - 2]:
            bars = (n - 1) - i
            pct  = (closes.iloc[-1] / closes.iloc[i] - 1) * 100
            return bars, round(pct, 2)
    cap_idx = max(0, n - ZL_TURN_CAP - 1)
    return ZL_TURN_CAP, round((closes.iloc[-1] / closes.iloc[cap_idx] - 1) * 100, 2)


# ── OHLC cache (per-symbol CSV, delta-updated) ─────────────────────────────────
def _raw_history(symbol: str, period: str = None, start: str = None) -> pd.DataFrame:
    t = yf.Ticker(f"{symbol}.NS")
    raw = t.history(start=start) if start else t.history(period=period or "6mo")
    if raw.empty:
        return raw
    raw = raw[["Open", "High", "Low", "Close", "Volume"]].copy()
    raw.index = pd.DatetimeIndex([d.date() for d in raw.index])
    raw.index.name = "Date"
    return raw

def get_ohlc(symbol: str) -> pd.DataFrame | None:
    """Return cached + updated OHLC (≥60 bars) or None."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    path = os.path.join(CACHE_DIR, f"{symbol}.csv")

    existing = pd.DataFrame()
    if os.path.exists(path):
        try:
            existing = pd.read_csv(path, index_col=0, parse_dates=True)
        except Exception:
            existing = pd.DataFrame()

    today = date.today()
    if existing.empty:
        df = _raw_history(symbol, period="6mo")
    else:
        last = existing.index[-1].date()
        if last >= today - timedelta(days=1):
            return existing if len(existing) >= 60 else None
        df = _raw_history(symbol, start=(last + timedelta(days=1)).strftime("%Y-%m-%d"))

    if not df.empty:
        combined = pd.concat([existing, df]) if not existing.empty else df
        combined = combined[~combined.index.duplicated(keep="last")].sort_index()
        if len(combined) > CACHE_MAX:
            combined = combined.iloc[-CACHE_MAX:]
        combined.to_csv(path)
        return combined if len(combined) >= 60 else None

    return existing if len(existing) >= 60 else None


# ── Nifty MidSmallcap 400 index cache ─────────────────────────────────────────
def _fetch_index_day(d: date) -> tuple | None:
    url = NSE_ARCH.format(d.strftime("%d%m%Y"))
    try:
        r = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        if not r.ok:
            return None
        for line in r.text.strip().split("\n"):
            if line.startswith(INDEX_NAME):
                parts = line.split(",")
                return (d, float(parts[5]))
    except Exception:
        return None

def get_index_history(months: int = 6) -> pd.Series:
    if os.path.exists(INDEX_CACHE):
        cached = pd.read_csv(INDEX_CACHE, index_col=0, parse_dates=True).squeeze("columns")
    else:
        cached = pd.Series(dtype=float)

    start        = date.today() - timedelta(days=months * 31)
    all_weekdays = pd.bdate_range(start, date.today() - timedelta(1))
    cached_dates = set(cached.index.date) if not cached.empty else set()
    missing      = [d.date() for d in all_weekdays if d.date() not in cached_dates]

    if missing:
        print(f"  Fetching {len(missing)} days of NIFTY MidSmallcap 400 data...")
        with ThreadPoolExecutor(max_workers=15) as ex:
            results = list(ex.map(_fetch_index_day, missing))
        new_data = {d: c for d, c in (r for r in results if r)}
        if new_data:
            new_s = pd.Series(new_data)
            new_s.index = pd.to_datetime(new_s.index)
            new_s.name  = "close"
            cached = pd.concat([cached, new_s]).sort_index().drop_duplicates()
            cached.name = "close"
            cached.to_csv(INDEX_CACHE, header=True)

    return cached.dropna()


# ── Watchlist ──────────────────────────────────────────────────────────────────
def get_watchlist() -> list[str]:
    filters = [
        col("exchange") == "NSE",
        col("type") == "stock",
        col("typespecs").has(["common"]),
        col("close") > 100,
        col("close") > col("EMA25"),
        col("market_cap_basic").between(MC_LOW, MC_HIGH),
    ]
    if FILTER_1W_CHANGE:
        filters.append(col("Perf.W") > 5)

    _, df = (
        Query()
        .set_markets("india")
        .select("name", "close", "EMA25", "Perf.W")
        .where(*filters)
        .limit(500)
        .get_scanner_data()
    )
    return df["name"].tolist()


# ── Circuit limits ─────────────────────────────────────────────────────────────
_CIRCUIT_EMOJI = {("20","10"): "🟨", ("10","5"): "🟥", ("5","10"): "🟩", ("10","20"): "🟦"}
_NSE_CSV_PATHS = [
    os.path.join(REPO_DIR, "nse.csv"),
    r"C:\Users\satya\.gemini\antigravity\scratch\circuit_dashboard\nse.csv",
]

def get_circuit_limits() -> dict[str, tuple[str, str]]:
    nse_csv = next((p for p in _NSE_CSV_PATHS if os.path.exists(p)), None)
    if not nse_csv:
        print("  [circuit] nse.csv not found, skipping.")
        return {}
    try:
        latest: dict[str, dict] = {}
        with open(nse_csv, encoding="utf-8-sig") as fh:
            for raw in csv.DictReader(fh):
                row = {k.strip(): v.strip() for k, v in raw.items()}
                sym = row.get("SYMBOL", "")
                dte = row.get("EFFECTIVE DATE", "")
                frm = row.get("FROM", "")
                to  = row.get("TO",   "")
                if not sym or not dte:
                    continue
                try:
                    parsed = datetime.strptime(dte, "%d-%b-%Y")
                except ValueError:
                    continue
                if sym not in latest or parsed > latest[sym]["parsed"]:
                    latest[sym] = {"parsed": parsed, "from": frm, "to": to}
        return {
            sym: (d["to"] + "%", _CIRCUIT_EMOJI.get((d["from"], d["to"]), ""))
            for sym, d in latest.items()
        }
    except Exception:
        return {}


# ── Stock analysis ─────────────────────────────────────────────────────────────
def analyse(symbol: str, index_s: pd.Series) -> dict | None:
    try:
        df = get_ohlc(symbol)
        if df is None:
            return None

        c = df["Close"]

        # Align with index (common trading dates)
        common = c.index.intersection(index_s.index)
        if len(common) < 30:
            return None

        c_rs   = c.loc[common]
        idx_rs = index_s.loc[common]
        rs     = (c_rs / idx_rs) * 1000

        # Weekly RS EMA9
        weekly_c   = c_rs.resample("W").last().dropna()
        weekly_idx = idx_rs.resample("W").last().dropna()
        wk_common  = weekly_c.index.intersection(weekly_idx.index)
        if len(wk_common) < 12:
            return None

        wk_rs    = (weekly_c.loc[wk_common] / weekly_idx.loc[wk_common]) * 1000
        wk_rs_e9 = ema(wk_rs, 9)

        if not (rs.iloc[-1] > wk_rs_e9.iloc[-1] and wk_rs_e9.iloc[-1] > wk_rs_e9.iloc[-2]):
            return None

        # ZLEMA25
        zl25      = zlema(c, 25)
        zl_rising = zl25.iloc[-1] > zl25.iloc[-2]

        curr_close = c.iloc[-1]
        prev_close = c.iloc[-2]
        day_chg    = (curr_close - prev_close) / prev_close * 100

        zl_days, zl_pct = zl25_turn_stats(zl25, c)

        return {
            "symbol":    symbol,
            "close":     curr_close,
            "day_chg":   day_chg,
            "zl_rising": zl_rising,
            "zl_days":   zl_days,
            "zl_pct":    zl_pct,
            "squeeze":   bb_kc_squeeze(df),
        }
    except Exception:
        return None


# ── Markdown ───────────────────────────────────────────────────────────────────
STATIC_FOOTER = """
---

### Scan definition
| Filter | Value |
|--------|-------|
| Exchange | NSE common equity |
| Price | > ₹100 |
| 1-week change | > 5% |
| Market cap | ₹1,000 Cr – ₹1 Lakh Cr |
| Price vs EMA25 | Price > EMA25 |
| RS filter | Daily RS > Weekly RS EMA9 · Weekly RS EMA9 rising |
| ZL Days / ZL Chg% | Days since ZLEMA25 last turned up · % price change since that bar (capped {cap}d) |
| Squeeze | ✓ = BB(20,2.0,SMA) fully inside KC(20,1.5,SMA) on last bar |
""".format(cap=ZL_TURN_CAP)


def _table_rows(findings: list[dict], circuit: dict[str, tuple]) -> list[str]:
    rows = []
    for f in findings:
        cl, em = circuit.get(f["symbol"], ("20%", ""))
        tv     = f"https://in.tradingview.com/chart/?symbol=NSE:{f['symbol']}"
        zl_d   = f"{f['zl_days']}d+" if f["zl_days"] >= ZL_TURN_CAP else f"{f['zl_days']}d"
        zl_p   = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
        ds     = "+" if f["day_chg"] >= 0 else ""
        sqz    = "✓" if f.get("squeeze") else "—"
        rows.append(
            f"| [{f['symbol']}]({tv}) "
            f"| {f['close']:.2f} "
            f"| {ds}{f['day_chg']:.2f}% "
            f"| {zl_d} "
            f"| {zl_p} "
            f"| {sqz} "
            f"| {cl} {em} |"
        )
    return rows


def build_markdown(findings: list[dict], circuit: dict[str, tuple]) -> str:
    rising = sorted([f for f in findings if     f["zl_rising"]], key=lambda x: x["zl_days"])
    watch  = sorted([f for f in findings if not f["zl_rising"]], key=lambda x: x["zl_days"])

    hdr = [
        "| Symbol | Close | Day Chg | ZL Days | ZL Chg% | Squeeze | Circuit |",
        "|--------|------:|--------:|--------:|--------:|:-------:|:-------:|",
    ]

    lines = [
        f"# NSE EMA25 ZL Scan — {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        f"**ZLEMA25 Rising: {len(rising)}** &nbsp;|&nbsp; **ZLEMA25 Watch: {len(watch)}**",
        "*(Price > ₹100 · 1W > 5% · MCap 10B–1T INR · NSE · Price > EMA25 · Daily RS > Weekly RS EMA9 · Weekly RS EMA9 rising)*",
        "",
        "### ZLEMA25 Rising",
    ]
    if rising:
        lines += hdr + _table_rows(rising, circuit)
    else:
        lines.append("*No ZLEMA25 rising stocks today.*")

    lines += ["", "### ZLEMA25 Watch *(pullback / flat)*"]
    if watch:
        lines += hdr + _table_rows(watch, circuit)
    else:
        lines.append("*No ZLEMA25 watch stocks today.*")

    return "\n".join(lines)


# ── Console output ─────────────────────────────────────────────────────────────
def print_results(findings: list[dict]) -> None:
    rising = [f for f in findings if     f["zl_rising"]]
    watch  = [f for f in findings if not f["zl_rising"]]

    print(f"\n{'='*70}")
    print(f"  NSE EMA25 ZL Scanner  |  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  ZLEMA25 Rising: {len(rising)}   ZLEMA25 Watch: {len(watch)}")
    print(f"{'='*70}")

    if rising:
        print("\n  ── ZLEMA25 Rising (top 15 by ZL Chg%) ──")
        for f in rising[:15]:
            ds  = "+" if f["day_chg"] >= 0 else ""
            zp  = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
            zd  = f"{f['zl_days']}d+" if f["zl_days"] >= ZL_TURN_CAP else f"{f['zl_days']}d"
            print(f"  {f['symbol']:<18}  {f['close']:>9.2f}  day:{ds}{f['day_chg']:.1f}%  zl:{zd} {zp}")

    if watch:
        print(f"\n  ── ZLEMA25 Watch ({len(watch)} stocks) ──")
        for f in watch[:10]:
            ds = "+" if f["day_chg"] >= 0 else ""
            zp = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
            print(f"  {f['symbol']:<18}  {f['close']:>9.2f}  day:{ds}{f['day_chg']:.1f}%  zl:{f['zl_days']}d {zp}")
    print()


# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    os.makedirs(CACHE_DIR, exist_ok=True)
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nFetching NIFTY MidSmallcap 400 index history...")
    index_s = get_index_history(months=6)
    print(f"  Index data: {len(index_s)} days  (latest: {index_s.index[-1].date()}  {index_s.iloc[-1]:.2f})")

    print("\nFetching NSE circuit limits...")
    circuit = get_circuit_limits()
    print(f"  Circuit data: {len(circuit)} stocks with recent limit changes")

    print("\nFetching live watchlist from TradingView screener...")
    watchlist = get_watchlist()
    print(f"  Watchlist: {len(watchlist)} stocks  |  Scanning...\n")

    def _worker(sym):
        return analyse(sym, index_s)

    findings = []
    for i, sym in enumerate(watchlist, 1):
        print(f"  {sym:<20} ({i}/{len(watchlist)})   ", end="\r")
        result = _worker(sym)
        if result:
            findings.append(result)

    print_results(findings)

    existing = ""
    if os.path.exists(MD_FILE):
        with open(MD_FILE, "r", encoding="utf-8") as fh:
            existing = fh.read()
    md = build_markdown(findings, circuit)
    with open(MD_FILE, "w", encoding="utf-8") as fh:
        if existing:
            fh.write(md + "\n\n---\n\n" + existing)
        else:
            fh.write(md + "\n" + STATIC_FOOTER)
    print(f"\n  Saved -> {MD_FILE}")


if __name__ == "__main__":
    main()