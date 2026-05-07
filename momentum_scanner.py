#!/usr/bin/env python3
"""
NSE Momentum Scanner  (NSE_AboveWeekEMA5 screen)
Run after 4:10 PM IST on trading days.

Watchlist filters (TradingView):
  - NSE common equity
  - Price > 50 INR
  - 1-week change > 5%
  - Market cap 10B – 1T INR  (≈ 1,000 Cr – 1 Lakh Cr)
  - Price > EMA25

Entry conditions (all require ZLEMA25 rising):
  STRONG        – price touched ZLEMA25 + EMA20 rising
  PRIMARY       – price touched ZLEMA25
  DEEP PULLBACK – low touched EMA50/100/200, closed green above it

RS filter (all 3 must pass):
  - Daily RS Line > RS EMA9
  - Daily RS Line > RS EMA21
  - Weekly RS EMA9 is rising
  RS Line = (stock_close / Nifty MidSmallcap 400) * 1000

Output: momentum_scans/momentum_scans.md — auto-committed and pushed to GitHub
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
SCANS_DIR   = os.path.join(REPO_DIR, "momentum_scans")
INDEX_CACHE = os.path.join(REPO_DIR, ".niftymidsml400_cache.csv")
TODAY       = datetime.now().strftime("%Y-%m-%d")
MD_FILE     = os.path.join(SCANS_DIR, "momentum_scans.md")

MC_LOW      = 1_000  * 1_00_00_000    # ₹1,000 Cr  (~10B INR)
MC_HIGH     = 1_00_000 * 1_00_00_000  # ₹1 Lakh Cr (~1T INR)
TOUCH_PCT    = 0.015
ZL_TURN_CAP  = 60
INDEX_NAME  = "Nifty MidSmallcap 400"
NSE_ARCH    = "https://nsearchives.nseindia.com/content/indices/ind_close_all_{}.csv"


# ── Indicators ────────────────────────────────────────────────────────────────
def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()

def zlema(s: pd.Series, n: int) -> pd.Series:
    e = ema(s, n)
    return 2 * e - ema(e, n)

def zl25_turn_stats(zl25: pd.Series, closes: pd.Series) -> tuple[int, float]:
    n     = len(zl25)
    limit = max(2, n - ZL_TURN_CAP)
    for i in range(n - 1, limit - 1, -1):
        if zl25.iloc[i] > zl25.iloc[i - 1] and zl25.iloc[i - 1] <= zl25.iloc[i - 2]:
            bars = (n - 1) - i
            pct  = (closes.iloc[-1] / closes.iloc[i - 1] - 1) * 100
            return bars, round(pct, 2)
    return ZL_TURN_CAP, round((closes.iloc[-1] / closes.iloc[-(ZL_TURN_CAP + 2)] - 1) * 100, 2)


# ── Nifty MidSmallcap 400 index cache ────────────────────────────────────────
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

    start = date.today() - timedelta(days=months * 31)
    all_weekdays = pd.bdate_range(start, date.today() - timedelta(1))
    cached_dates = set(cached.index.date) if not cached.empty else set()
    missing = [d.date() for d in all_weekdays if d.date() not in cached_dates]

    if missing:
        print(f"  Fetching {len(missing)} days of NIFTY MidSmallcap 400 data...")
        with ThreadPoolExecutor(max_workers=15) as ex:
            results = list(ex.map(_fetch_index_day, missing))
        new_data = {d: c for d, c in (r for r in results if r)}
        if new_data:
            new_s = pd.Series(new_data)
            new_s.index = pd.to_datetime(new_s.index)
            new_s.name = "close"
            cached = pd.concat([cached, new_s]).sort_index().drop_duplicates()
            cached.name = "close"
            cached.to_csv(INDEX_CACHE, header=True)

    return cached.dropna()


# ── Watchlist ─────────────────────────────────────────────────────────────────
def get_watchlist() -> list[str]:
    _, df = (
        Query()
        .set_markets("india")
        .select("name", "close", "EMA25", "Perf.W")
        .where(
            col("exchange") == "NSE",
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("close") > 50,
            col("Perf.W") > 5,
            col("close") > col("EMA25"),
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
        )
        .limit(500)
        .get_scanner_data()
    )
    return df["name"].tolist()


# ── Circuit limits ────────────────────────────────────────────────────────────
_CIRCUIT_EMOJI = {("20","10"): "🟨", ("10","5"): "🟥", ("5","10"): "🟩", ("10","20"): "🟦"}

_NSE_CSV = r"C:\Users\satya\.gemini\antigravity\scratch\circuit_dashboard\nse.csv"

def get_circuit_limits() -> dict[str, tuple[str, str]]:
    """Return {symbol: (current_pct, emoji)} from yesterday's circuit dashboard nse.csv."""
    if not os.path.exists(_NSE_CSV):
        print(f"  [circuit] nse.csv not found at {_NSE_CSV}, skipping.")
        return {}
    try:
        latest: dict[str, dict] = {}
        with open(_NSE_CSV, encoding="utf-8-sig") as fh:
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


# ── Stock analysis ────────────────────────────────────────────────────────────
def analyse(symbol: str, index_s: pd.Series) -> dict | None:
    try:
        df = yf.Ticker(f"{symbol}.NS").history(period="1y")
        if len(df) < 210:
            return None

        c  = df["Close"]
        lo = df["Low"]
        op = df["Open"]

        e20  = ema(c, 20)
        e50  = ema(c, 50)
        e100 = ema(c, 100)
        e200 = ema(c, 200)
        zl25 = zlema(c, 25)

        if not (e50.iloc[-1] > e200.iloc[-1] and e100.iloc[-1] > e200.iloc[-1]):
            return None

        zl_now, zl_prev   = zl25.iloc[-1], zl25.iloc[-2]
        e20_now, e20_prev = e20.iloc[-1],  e20.iloc[-2]
        curr_close = c.iloc[-1]
        prev_close = c.iloc[-2]
        curr_low   = lo.iloc[-1]
        curr_open  = op.iloc[-1]

        zl_rising  = zl_now > zl_prev
        e20_rising = e20_now > e20_prev

        if not zl_rising:
            return None

        # ── RS Line filter ────────────────────────────────────────────────────
        c_norm = c.copy()
        c_norm.index = pd.to_datetime([d.date() for d in c.index])
        common = c_norm.index.intersection(index_s.index)
        if len(common) < 30:
            return None

        c_rs   = c_norm.loc[common]
        idx_rs = index_s.loc[common]

        rs    = (c_rs / idx_rs) * 1000
        rs_e9  = ema(rs, 9)
        rs_e21 = ema(rs, 21)

        rs_above_e9  = rs.iloc[-1] > rs_e9.iloc[-1]
        rs_above_e21 = rs.iloc[-1] > rs_e21.iloc[-1]

        weekly_c   = c_rs.resample("W").last().dropna()
        weekly_idx = idx_rs.resample("W").last().dropna()
        wk_common  = weekly_c.index.intersection(weekly_idx.index)
        if len(wk_common) < 12:
            return None

        wk_rs        = (weekly_c.loc[wk_common] / weekly_idx.loc[wk_common]) * 1000
        wk_rs_e9     = ema(wk_rs, 9)
        wk_rs_rising = wk_rs_e9.iloc[-1] > wk_rs_e9.iloc[-2]

        if not (rs_above_e9 and rs_above_e21 and wk_rs_rising):
            return None

        # ── Entry conditions ──────────────────────────────────────────────────
        entries = []

        was_above  = prev_close > zl_prev
        touched_zl = (
            curr_low <= zl_now * (1 + TOUCH_PCT)
            and curr_low >= zl_now * (1 - TOUCH_PCT)
        ) or (curr_low <= zl_now and curr_close >= zl_now)

        if was_above and touched_zl:
            tag   = "STRONG" if e20_rising else "PRIMARY"
            label = "ZLEMA25 touch + EMA20 rising" if e20_rising else "ZLEMA25 touch"
            entries.append((tag, label, zl_now))

        for level, name in [
            (e50.iloc[-1],  "EMA50"),
            (e100.iloc[-1], "EMA100"),
            (e200.iloc[-1], "EMA200"),
        ]:
            touched = curr_low <= level * (1 + TOUCH_PCT)
            bounced = curr_close > level and curr_close > curr_open
            if touched and bounced:
                entries.append(("DEEP PULLBACK", f"Bounce from {name}", level))

        if not entries:
            return None

        zl_days, zl_pct = zl25_turn_stats(zl25, c)
        return {
            "symbol":  symbol,
            "close":   curr_close,
            "day_chg": (curr_close - prev_close) / prev_close * 100,
            "zl_days": zl_days,
            "zl_pct":  zl_pct,
            "entries": entries,
        }

    except Exception:
        return None


# ── Markdown ──────────────────────────────────────────────────────────────────
TAG_ORDER = {"STRONG": 0, "PRIMARY": 1, "DEEP PULLBACK": 2}

STATIC_FOOTER = """
---

### Signal definitions
| Signal | Condition |
|--------|-----------|
| **STRONG** | ZLEMA25 rising · price touched ZLEMA25 · EMA20 rising |
| **PRIMARY** | ZLEMA25 rising · price touched ZLEMA25 |
| **DEEP PULLBACK** | ZLEMA25 rising · low touched EMA50/100/200 · closed green above it |

### Watchlist filters
- Price > ₹50 · 1-week change > 5% · Price > EMA25
- Market cap ₹1,000 Cr – ₹1 Lakh Cr · NSE common equity

### RS filter (all 3 required)
- RS Line (stock / Nifty MidSmallcap 400 × 1000) above its 9 EMA and 21 EMA (daily)
- Weekly RS EMA9 is rising"""

def build_markdown(findings: list[dict], circuit: dict[str, tuple]) -> str:
    findings.sort(key=lambda x: min(TAG_ORDER.get(e[0], 9) for e in x["entries"]))

    lines = [
        f"# NSE Momentum Scan — {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        f"\n**Entry Opportunities: {len(findings)}**",
        f"*(Price > ₹50 · 1W change > 5% · Price > EMA25 · RS filter)*\n",
        "| Symbol | Signal | Day Change | ZL Days | ZL Chg% | Circuit |",
        "|--------|--------|----------:|--------:|--------:|:-------:|",
    ]

    for f in findings:
        cl, em = circuit.get(f["symbol"], ("20%", ""))
        tv      = f"https://in.tradingview.com/chart/?symbol=NSE:{f['symbol']}"
        zl_d    = f"{f['zl_days']}d+" if f['zl_days'] >= ZL_TURN_CAP else f"{f['zl_days']}d"
        zl_p    = f"+{f['zl_pct']:.1f}%" if f['zl_pct'] >= 0 else f"{f['zl_pct']:.1f}%"
        for tag, label, _ in f["entries"]:
            ds = "+" if f["day_chg"] >= 0 else ""
            lines.append(
                f"| [{f['symbol']}]({tv}) "
                f"| **{tag}** — {label} "
                f"| {ds}{f['day_chg']:.2f}% "
                f"| {zl_d} "
                f"| {zl_p} "
                f"| {cl} {em} |"
            )

    return "\n".join(lines)


# ── Console ───────────────────────────────────────────────────────────────────
def print_results(findings: list[dict]) -> None:
    print(f"\n{'='*70}")
    print(f"  NSE Momentum Scanner  |  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Entry Opportunities (with RS filter): {len(findings)}")
    print(f"{'='*70}")

    if not findings:
        print("  No entry setups found today.")
        return

    for f in findings:
        ds = "+" if f["day_chg"] >= 0 else ""
        print(f"\n  {f['symbol']:<15}  Close: {f['close']:>8.2f}  ({ds}{f['day_chg']:.2f}% day)")
        for tag, label, level in f["entries"]:
            vs = (f["close"] - level) / level * 100
            print(f"    [{tag}]  {label}  Level={level:.2f}  ({vs:+.1f}%)")
        print("    " + "─" * 60)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("\nFetching NIFTY MidSmallcap 400 index history...")
    index_s = get_index_history(months=6)
    print(f"  Index data: {len(index_s)} days  (latest: {index_s.index[-1].date()}  {index_s.iloc[-1]:.2f})")

    print("\nFetching NSE circuit limits...")
    circuit = get_circuit_limits()
    print(f"  Circuit data: {len(circuit)} stocks with recent limit changes")

    print("\nFetching live watchlist from TradingView screener...")
    watchlist = get_watchlist()
    print(f"  Watchlist: {len(watchlist)} stocks  |  Scanning...\n")

    findings = []
    for i, sym in enumerate(watchlist, 1):
        print(f"  {sym:<20} ({i}/{len(watchlist)})   ", end="\r")
        result = analyse(sym, index_s)
        if result:
            findings.append(result)

    print_results(findings)

    os.makedirs(SCANS_DIR, exist_ok=True)
    dated_file = os.path.join(SCANS_DIR, f"momentum_scans_{TODAY}.md")
    md = build_markdown(findings, circuit)
    with open(MD_FILE, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(dated_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"\n  Saved -> {MD_FILE}")
    print(f"  Saved -> {dated_file}")


if __name__ == "__main__":
    main()