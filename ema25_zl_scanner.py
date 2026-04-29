#!/usr/bin/env python3
"""
NSE EMA25 ZL Scanner
Run after 4:20 PM IST on trading days (after run_fetch_data.ps1 completes).

Watchlist filters (TradingView):
  - NSE common equity
  - Price > 100 INR
  - Market cap 10B – 1T INR  (≈ 1,000 Cr – 1 Lakh Cr)
  - Price > EMA25

RS filter — controlled by RS_MODE:
  "daily_ema21" (default): Daily RS Line > Daily RS EMA21 AND Daily RS EMA21 rising
  "weekly_ema9" (optional): Daily RS Line > Weekly RS EMA9 AND Weekly RS EMA9 rising
  RS Line = (stock_close / Nifty MidSmallcap 400) * 1000

For each RS-passing stock:
  - Compute ZLEMA25 direction (rising / flat-down)
  - Compute zl25_turn_stats(): days since last ZLEMA25 turn-up, % gain since

Data source: .ohlc_data/market.db  (populated by fetch_data.py)
Output:      ema25_zl_scans/ema25_zl_scans.md
"""

import sys, os, csv
from datetime import datetime

import pandas as pd
from tradingview_screener import Query, col

from ohlc_db import load_ohlc, DB_PATH

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR    = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR   = os.path.join(REPO_DIR, "ema25_zl_scans")
TODAY       = datetime.now().strftime("%Y-%m-%d")
MD_FILE     = os.path.join(SCANS_DIR, "ema25_zl_scans.md")

MC_LOW      = 1_000     * 1_00_00_000   # 1000 Cr  = 10B INR
MC_HIGH     = 1_00_000  * 1_00_00_000   # 1L Cr    = 1T INR
ZL_TURN_CAP          = 60
FILTER_1W_CHANGE     = False   # True = require 1-week price change > 5%
FILTER_PRICE_EMA25   = False   # True = require price > EMA25 (off by default: squeeze builds before reclaim)
RS_MODE              = "daily_ema21"  # "daily_ema21" | "weekly_ema9"


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

def bb_kc_squeeze(df: pd.DataFrame, kc_atr_wilder: bool = False) -> bool:
    """True if BB(20,2.0,SMA) is fully inside KC(20,1.5,SMA ATR) on the last bar.
    Set kc_atr_wilder=True to use Wilder EWM ATR instead of SMA ATR."""
    if len(df) < 21:
        return False
    c = df["close"].astype(float)
    h = df["high"].astype(float)
    l = df["low"].astype(float)

    bb_basis = c.rolling(20).mean()
    bb_std   = c.rolling(20).std()
    bb_upper = bb_basis + 2.0 * bb_std
    bb_lower = bb_basis - 2.0 * bb_std

    kc_basis = c.rolling(20).mean()
    kc_atr   = _atr_wilder(h, l, c, 20) if kc_atr_wilder else (
        pd.concat([h-l, (h-c.shift(1)).abs(), (l-c.shift(1)).abs()], axis=1).max(axis=1).rolling(20).mean()
    )
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


# ── Watchlist ──────────────────────────────────────────────────────────────────
def get_watchlist() -> list[str]:
    filters = [
        col("exchange") == "NSE",
        col("type") == "stock",
        col("typespecs").has(["common"]),
        col("close") > 100,
        col("market_cap_basic").between(MC_LOW, MC_HIGH),
    ]
    if FILTER_PRICE_EMA25:
        filters.append(col("close") > col("EMA25"))
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


# ── RS gate ────────────────────────────────────────────────────────────────────
def _rs_gate(rs: pd.Series, c_rs: pd.Series, idx_rs: pd.Series) -> bool:
    """Return True if the stock passes the active RS filter (RS_MODE)."""
    if RS_MODE == "weekly_ema9":
        weekly_c   = c_rs.resample("W").last().dropna()
        weekly_idx = idx_rs.resample("W").last().dropna()
        wk_common  = weekly_c.index.intersection(weekly_idx.index)
        if len(wk_common) < 12:
            return False
        wk_rs    = (weekly_c.loc[wk_common] / weekly_idx.loc[wk_common]) * 1000
        wk_rs_e9 = ema(wk_rs, 9)
        return bool(rs.iloc[-1] > wk_rs_e9.iloc[-1] and wk_rs_e9.iloc[-1] > wk_rs_e9.iloc[-2])
    else:  # daily_ema21
        if len(rs) < 22:
            return False
        rs_e21 = ema(rs, 21)
        return bool(rs.iloc[-1] > rs_e21.iloc[-1] and rs_e21.iloc[-1] > rs_e21.iloc[-2])


# ── Stock analysis ─────────────────────────────────────────────────────────────
def analyse(symbol: str, index_s: pd.Series) -> dict | None:
    try:
        raw = load_ohlc(symbol)
        if raw is None or len(raw) < 60:
            return None
        df = raw.set_index("date")
        df.index = pd.to_datetime(df.index)

        c = df["close"].astype(float)

        # Align with index (common trading dates)
        common = c.index.intersection(index_s.index)
        if len(common) < 30:
            return None

        c_rs   = c.loc[common]
        idx_rs = index_s.loc[common]
        rs     = (c_rs / idx_rs) * 1000

        if not _rs_gate(rs, c_rs, idx_rs):
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
            "squeeze":   bb_kc_squeeze(raw),
        }
    except Exception:
        return None


# ── Markdown ───────────────────────────────────────────────────────────────────
_RS_FILTER_LABEL = {
    "daily_ema21": "Daily RS > Daily RS EMA21 · Daily RS EMA21 rising",
    "weekly_ema9": "Daily RS > Weekly RS EMA9 · Weekly RS EMA9 rising",
}

STATIC_HEADER = """### Scan definition
| Filter | Value |
|--------|-------|
| Exchange | NSE common equity |
| Price | > ₹100 |
| 1-week change | {w1} |
| Market cap | ₹1,000 Cr – ₹1 Lakh Cr |
| Price vs EMA25 | {ema25} |
| RS filter | {rs_label} |
| ZL Days / ZL Chg% | Days since ZLEMA25 last turned up · % price change since that bar (capped {cap}d) |
| Squeeze | ✓ = BB(20,2.0,SMA) fully inside KC(20,1.5,SMA) on last bar |

---
""".format(
    cap=ZL_TURN_CAP,
    rs_label=_RS_FILTER_LABEL.get(RS_MODE, RS_MODE),
    w1="> 5%" if FILTER_1W_CHANGE else "off",
    ema25="Price > EMA25" if FILTER_PRICE_EMA25 else "off",
)


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
        STATIC_HEADER,
        f"**ZLEMA25 Rising: {len(rising)}** &nbsp;|&nbsp; **ZLEMA25 Watch: {len(watch)}**",
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
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nLoading NIFTY MidSmallcap 400 from DB...")
    bm_raw = load_ohlc("NIFTY MIDSML 400")
    if bm_raw is None or bm_raw.empty:
        print("  ERROR: Benchmark not in DB. Run fetch_data.py first.")
        return
    bm_raw = bm_raw.set_index("date")
    bm_raw.index = pd.to_datetime(bm_raw.index)
    index_s = bm_raw["close"].astype(float)
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

    existing = ""
    if os.path.exists(MD_FILE):
        with open(MD_FILE, "r", encoding="utf-8") as fh:
            existing = fh.read()
    md = build_markdown(findings, circuit)
    with open(MD_FILE, "w", encoding="utf-8") as fh:
        if existing:
            fh.write(md + "\n\n---\n\n" + existing)
        else:
            fh.write(md)
    print(f"\n  Saved -> {MD_FILE}")


if __name__ == "__main__":
    main()