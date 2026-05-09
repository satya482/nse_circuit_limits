#!/usr/bin/env python3
"""
NSE Weekly ZL Squeeze Scanner
Stocks where ZLEMA25 is Rising on WEEKLY bars, optionally with BB Squeeze active.
Uses daily OHLC resampled to weekly; includes the current partial week.

Watchlist: NSE common equity, price > ₹50, MCap ₹800 Cr – ₹1 Lakh Cr
No RS gate (weekly timeframe is already a higher-timeframe filter)
Signal A: Weekly ZLEMA25 rising AND BB(20,2.0,SMA) inside KC(20,1.5,SMA ATR) on last weekly bar
Signal B: Weekly ZLEMA25 rising (no squeeze required — Watch list)

Output: weekly_zl_scans/weekly_zl_scans.md  +  weekly_zl_scans/weekly_zl_scans_YYYY-MM-DD.md
"""

import sys, os, csv
from datetime import datetime

import pandas as pd
from tradingview_screener import Query, col

from ohlc_db import load_ohlc

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR    = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR   = os.path.join(REPO_DIR, "weekly_zl_scans")
TODAY       = datetime.now().strftime("%Y-%m-%d")
MD_FILE     = os.path.join(SCANS_DIR, "weekly_zl_scans.md")

MC_LOW      = 800     * 1_00_00_000   # ₹800 Cr
MC_HIGH     = 1_00_000 * 1_00_00_000  # ₹1 Lakh Cr
ZL_TURN_CAP = 52                      # weeks (~1 year)


# ── Indicators ────────────────────────────────────────────────────────────────
def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()

def zlema(s: pd.Series, n: int) -> pd.Series:
    e = ema(s, n)
    return 2 * e - ema(e, n)

def bb_kc_squeeze_info(df: pd.DataFrame) -> tuple[bool, int]:
    """Returns (squeeze_on, consecutive_bars_in_squeeze) as of the last bar."""
    if len(df) < 21:
        return False, 0
    c = df["close"].astype(float)
    h = df["high"].astype(float)
    l = df["low"].astype(float)

    bb_basis = c.rolling(20).mean()
    bb_upper = bb_basis + 2.0 * c.rolling(20).std()
    bb_lower = bb_basis - 2.0 * c.rolling(20).std()

    tr       = pd.concat([h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1).max(axis=1)
    kc_atr   = tr.rolling(20).mean()
    kc_basis = c.rolling(20).mean()
    kc_upper = kc_basis + 1.5 * kc_atr
    kc_lower = kc_basis - 1.5 * kc_atr

    squeeze_series = (bb_upper < kc_upper) & (bb_lower > kc_lower)
    squeeze_now    = bool(squeeze_series.iloc[-1])
    if not squeeze_now:
        return False, 0

    count = 0
    for v in reversed(squeeze_series.values):
        if v:
            count += 1
        else:
            break
    return True, count

def zl25_turn_stats(zl25: pd.Series, closes: pd.Series) -> tuple[int, float]:
    n     = len(zl25)
    limit = max(2, n - ZL_TURN_CAP)
    for i in range(n - 1, limit - 1, -1):
        if zl25.iloc[i] > zl25.iloc[i - 1] and zl25.iloc[i - 1] <= zl25.iloc[i - 2]:
            bars = (n - 1) - i + 1
            pct  = (closes.iloc[-1] / closes.iloc[i] - 1) * 100
            return bars, round(pct, 2)
    cap_idx = max(0, n - ZL_TURN_CAP)
    return ZL_TURN_CAP, round((closes.iloc[-1] / closes.iloc[cap_idx] - 1) * 100, 2)


# ── Weekly resampling ─────────────────────────────────────────────────────────
def to_weekly(df: pd.DataFrame) -> pd.DataFrame:
    """Resample daily OHLCV to weekly. Includes partial current week as last bar."""
    d = df.set_index("date")
    d.index = pd.to_datetime(d.index)
    w = d.resample("W").agg(
        open=("open", "first"),
        high=("high", "max"),
        low=("low", "min"),
        close=("close", "last"),
        volume=("volume", "sum"),
    ).dropna(subset=["close"])
    return w.reset_index()


# ── Watchlist ──────────────────────────────────────────────────────────────────
def get_watchlist() -> list[str]:
    _, df = (
        Query()
        .set_markets("india")
        .select("name", "close")
        .where(
            col("exchange") == "NSE",
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("close") > 50,
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
        )
        .limit(2000)
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
        return {}
    try:
        latest: dict[str, dict] = {}
        with open(nse_csv, encoding="utf-8-sig") as fh:
            for raw in csv.DictReader(fh):
                row = {k.strip(): v.strip() for k, v in raw.items()}
                sym, dte = row.get("SYMBOL",""), row.get("EFFECTIVE DATE","")
                frm, to  = row.get("FROM",""), row.get("TO","")
                if not sym or not dte:
                    continue
                try:
                    parsed = datetime.strptime(dte, "%d-%b-%Y")
                except ValueError:
                    continue
                if sym not in latest or parsed > latest[sym]["parsed"]:
                    latest[sym] = {"parsed": parsed, "from": frm, "to": to}
        return {sym: (d["to"] + "%", _CIRCUIT_EMOJI.get((d["from"], d["to"]), ""))
                for sym, d in latest.items()}
    except Exception:
        return {}


# ── Stock analysis ─────────────────────────────────────────────────────────────
def analyse(symbol: str) -> dict | None:
    try:
        daily = load_ohlc(symbol, lookback=400)
        if daily is None or len(daily) < 30:
            return None

        wdf = to_weekly(daily)
        if len(wdf) < 22:
            return None

        c    = wdf["close"].astype(float)
        zl25 = zlema(c, 25)
        if not bool(zl25.iloc[-1] > zl25.iloc[-2]):
            return None

        sqz_on, sqz_weeks = bb_kc_squeeze_info(wdf)
        zl_weeks, zl_pct  = zl25_turn_stats(zl25, c)

        daily_c = daily["close"].astype(float)
        day_chg = (daily_c.iloc[-1] / daily_c.iloc[-2] - 1) * 100 if len(daily_c) >= 2 else 0.0

        return {
            "symbol":    symbol,
            "close":     float(daily_c.iloc[-1]),
            "day_chg":   day_chg,
            "sqz_on":    sqz_on,
            "sqz_weeks": sqz_weeks,
            "zl_weeks":  zl_weeks,
            "zl_pct":    zl_pct,
        }
    except Exception:
        return None


# ── Output ─────────────────────────────────────────────────────────────────────
def _sort_key(f: dict) -> tuple:
    return (f["zl_weeks"], -f["sqz_weeks"])

def _static_header() -> str:
    return f"""### Scan definition
| Filter | Value |
|--------|-------|
| Exchange | NSE common equity |
| Price | > ₹50 |
| Market cap | ₹800 Cr – ₹1 Lakh Cr |
| Timeframe | Weekly (daily OHLC resampled; current partial week included) |
| RS filter | None (weekly timeframe is already a higher-order filter) |
| Signal A | Weekly ZLEMA25 rising + BB(20,2.0,SMA) inside KC(20,1.5,SMA ATR) |
| Signal B | Weekly ZLEMA25 rising (Watch — no squeeze required) |
| Sqz Weeks | Consecutive weekly bars the squeeze has been active |
| ZL Weeks / ZL Chg% | Weeks since Weekly ZLEMA25 last turned up · % price change since (capped {ZL_TURN_CAP}w) |

---
"""

def _table_rows(findings: list[dict], circuit: dict[str, tuple]) -> list[str]:
    hdr = [
        "| Symbol | Close | Day Chg% | Sqz Weeks | ZL Weeks | ZL Chg% | Circuit |",
        "|--------|------:|---------:|----------:|---------:|--------:|:-------:|",
    ]
    rows = []
    for f in sorted(findings, key=_sort_key):
        cl, em = circuit.get(f["symbol"], ("20%", ""))
        tv     = f"https://in.tradingview.com/chart/?symbol=NSE:{f['symbol']}"
        zl_w   = f"{f['zl_weeks']}w+" if f["zl_weeks"] >= ZL_TURN_CAP else f"{f['zl_weeks']}w"
        zl_p   = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
        ds     = "+" if f["day_chg"] >= 0 else ""
        sqz    = f"{f['sqz_weeks']}w" if f["sqz_on"] else "—"
        rows.append(
            f"| [{f['symbol']}]({tv}) "
            f"| {f['close']:.2f} "
            f"| {ds}{f['day_chg']:.2f}% "
            f"| {sqz} "
            f"| {zl_w} "
            f"| {zl_p} "
            f"| {cl} {em} |"
        )
    return hdr + rows

def build_markdown(findings: list[dict], circuit: dict[str, tuple]) -> str:
    squeeze = [f for f in findings if f["sqz_on"]]
    watch   = [f for f in findings if not f["sqz_on"]]

    lines = [
        f"# NSE Weekly ZL Scan — {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        _static_header(),
        f"**{len(squeeze)} stocks: Weekly ZLEMA25 Rising + Squeeze ON**",
        "",
    ]
    if squeeze:
        lines += _table_rows(squeeze, circuit)
    else:
        lines.append("*No signals today.*")

    lines += [
        "",
        f"**{len(watch)} stocks: Weekly ZLEMA25 Rising (Watch)**",
        "",
    ]
    if watch:
        lines += _table_rows(watch, circuit)
    else:
        lines.append("*No watch stocks today.*")

    return "\n".join(lines)


def print_results(findings: list[dict]) -> None:
    squeeze = [f for f in findings if f["sqz_on"]]
    watch   = [f for f in findings if not f["sqz_on"]]
    print(f"\n{'='*75}")
    print(f"  NSE Weekly ZL Scanner  |  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Weekly ZLEMA25 Rising + Squeeze ON: {len(squeeze)}")
    print(f"  Weekly ZLEMA25 Rising (Watch):      {len(watch)}")
    print(f"{'='*75}")
    for label, group in [("SQUEEZE ON", squeeze), ("WATCH", watch)]:
        if group:
            print(f"\n  --- {label} ---")
            for f in sorted(group, key=_sort_key):
                ds  = "+" if f["day_chg"] >= 0 else ""
                zp  = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
                sqz = f"sqz:{f['sqz_weeks']}w" if f["sqz_on"] else "sqz:—"
                print(f"  {f['symbol']:<18}  {f['close']:>9.2f}  "
                      f"day:{ds}{f['day_chg']:.1f}%  {sqz}  "
                      f"zl:{f['zl_weeks']}w {zp}")
    print()


# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nFetching NSE circuit limits...")
    circuit = get_circuit_limits()
    print(f"  Circuit data: {len(circuit)} stocks with recent limit changes")

    print("\nFetching live watchlist from TradingView screener...")
    watchlist = get_watchlist()
    print(f"  Watchlist: {len(watchlist)} stocks  |  Scanning...\n")

    findings = []
    for i, sym in enumerate(watchlist, 1):
        print(f"  {sym:<20} ({i}/{len(watchlist)})   ", end="\r")
        result = analyse(sym)
        if result:
            findings.append(result)

    print_results(findings)

    dated_file = os.path.join(SCANS_DIR, f"weekly_zl_scans_{TODAY}.md")
    md = build_markdown(findings, circuit)
    with open(MD_FILE, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(dated_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  Saved -> {MD_FILE}")
    print(f"  Saved -> {dated_file}")


if __name__ == "__main__":
    main()
