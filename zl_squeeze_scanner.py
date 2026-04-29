#!/usr/bin/env python3
"""
NSE ZL Squeeze Scanner
Stocks where ZLEMA25 is Rising AND BB Squeeze is ON simultaneously.
Run after fetch_data.py completes (shares same SQLite data source).

Watchlist: NSE common equity, price > ₹100, MCap ₹800 Cr – ₹1 Lakh Cr
RS gate:   Daily RS > Daily RS EMA21 AND EMA21 rising
Signal:    ZLEMA25 rising on last bar AND BB(20,2.0,SMA) inside KC(20,1.5,SMA ATR)
Extra:     Squeeze duration — consecutive bars the squeeze has been active

Output: zl_squeeze_scans/zl_squeeze_scans.md
"""

import sys, os, csv
from datetime import datetime

import pandas as pd
from tradingview_screener import Query, col

from ohlc_db import load_ohlc

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR   = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR  = os.path.join(REPO_DIR, "zl_squeeze_scans")
TODAY      = datetime.now().strftime("%Y-%m-%d")
MD_FILE    = os.path.join(SCANS_DIR, "zl_squeeze_scans.md")

MC_LOW      = 800    * 1_00_00_000   # ₹800 Cr
MC_HIGH     = 1_00_000 * 1_00_00_000  # ₹1 Lakh Cr
ZL_TURN_CAP       = 60
RS_EMA21_GATE     = False  # Daily RS > EMA21 AND EMA21 rising
RS_EMA9_GATE      = True   # Daily RS > EMA9  AND EMA9  rising
RS_WEEKLY_EMA9_GATE = True   # Weekly RS > Weekly RS EMA9 AND EMA9 rising

# A stock must pass AT LEAST ONE enabled gate to appear in results.
# If all gates are False, no RS filter is applied.


# ── Indicators ────────────────────────────────────────────────────────────────
def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()

def zlema(s: pd.Series, n: int) -> pd.Series:
    e = ema(s, n)
    return 2 * e - ema(e, n)

def bb_kc_squeeze_info(df: pd.DataFrame) -> tuple[bool, int]:
    """Returns (squeeze_on, consecutive_bars_in_squeeze) as of the last bar.
    squeeze_on=True when BB(20,2.0,SMA) fully inside KC(20,1.5,SMA ATR)."""
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
            bars = (n - 1) - i
            pct  = (closes.iloc[-1] / closes.iloc[i] - 1) * 100
            return bars, round(pct, 2)
    cap_idx = max(0, n - ZL_TURN_CAP - 1)
    return ZL_TURN_CAP, round((closes.iloc[-1] / closes.iloc[cap_idx] - 1) * 100, 2)


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
            col("close") > 100,
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


# ── RS gates ─────────────────────────────────────────────────────────────────
def _rs_gate_ema21(rs: pd.Series) -> bool:
    if len(rs) < 22:
        return False
    e = ema(rs, 21)
    return bool(rs.iloc[-1] > e.iloc[-1] and e.iloc[-1] > e.iloc[-2])

def _rs_gate_ema9(rs: pd.Series) -> bool:
    if len(rs) < 10:
        return False
    e = ema(rs, 9)
    return bool(rs.iloc[-1] > e.iloc[-1] and e.iloc[-1] > e.iloc[-2])

def _rs_gate_weekly_ema9(rs: pd.Series, c_rs: pd.Series, idx_rs: pd.Series) -> bool:
    """Daily RS line > Weekly RS EMA9 AND Weekly RS EMA9 rising.
    Uses only completed weekly bars (drops the current partial week if its
    resample label is beyond the last daily bar date)."""
    wk_c   = c_rs.resample("W").last().dropna()
    wk_idx = idx_rs.resample("W").last().dropna()
    common = wk_c.index.intersection(wk_idx.index)
    if len(common) < 12:
        return False
    wk_rs = (wk_c.loc[common] / wk_idx.loc[common]) * 1000
    # Drop incomplete current week: resample("W") labels the week by its
    # ending Sunday, so the last bar's label is always > last daily date
    # when the week is not yet finished.
    last_daily = rs.index[-1]
    if wk_rs.index[-1] > last_daily:
        wk_rs = wk_rs.iloc[:-1]
    if len(wk_rs) < 11:   # need at least 11 bars to get a stable EMA9 with [-2]
        return False
    e9 = ema(wk_rs, 9)
    return bool(rs.iloc[-1] > e9.iloc[-1] and e9.iloc[-1] > e9.iloc[-2])


# ── Stock analysis ─────────────────────────────────────────────────────────────
def analyse(symbol: str, index_s: pd.Series) -> dict | None:
    try:
        raw = load_ohlc(symbol)
        if raw is None or len(raw) < 60:
            return None

        df = raw.set_index("date")
        df.index = pd.to_datetime(df.index)
        c  = df["close"].astype(float)

        common = c.index.intersection(index_s.index)
        if len(common) < 30:
            return None

        # Always compute all three RS gate results (for display columns)
        c_rs   = c.loc[common]
        idx_rs = index_s.loc[common]
        rs     = (c_rs / idx_rs) * 1000
        g_ema9    = _rs_gate_ema9(rs)
        g_ema21   = _rs_gate_ema21(rs)
        g_weekly9 = _rs_gate_weekly_ema9(rs, c_rs, idx_rs)

        # Filtering: at least one ENABLED gate must pass
        any_gate = RS_EMA21_GATE or RS_EMA9_GATE or RS_WEEKLY_EMA9_GATE
        if any_gate:
            enabled_passed = (
                (RS_EMA9_GATE    and g_ema9)    or
                (RS_EMA21_GATE   and g_ema21)   or
                (RS_WEEKLY_EMA9_GATE and g_weekly9)
            )
            if not enabled_passed:
                return None

        # Track which enabled gates passed (for sort priority)
        rs_passed = []
        if RS_EMA9_GATE    and g_ema9:    rs_passed.append("EMA9")
        if RS_EMA21_GATE   and g_ema21:   rs_passed.append("EMA21")
        if RS_WEEKLY_EMA9_GATE and g_weekly9: rs_passed.append("W-EMA9")

        zl25       = zlema(c, 25)
        zl_rising  = bool(zl25.iloc[-1] > zl25.iloc[-2])
        if not zl_rising:
            return None

        squeeze_on, squeeze_days = bb_kc_squeeze_info(raw)
        if not squeeze_on:
            return None

        zl_days, zl_pct = zl25_turn_stats(zl25, c)
        day_chg = (c.iloc[-1] - c.iloc[-2]) / c.iloc[-2] * 100

        return {
            "symbol":       symbol,
            "close":        c.iloc[-1],
            "day_chg":      day_chg,
            "zl_days":      zl_days,
            "zl_pct":       zl_pct,
            "squeeze_days": squeeze_days,
            "rs_gates":     rs_passed,   # enabled gates passed (for sort priority)
            "g_ema9":       g_ema9,
            "g_ema21":      g_ema21,
            "g_weekly9":    g_weekly9,
        }
    except Exception:
        return None


# ── Output ─────────────────────────────────────────────────────────────────────
def _sort_key(f: dict):
    # More RS gates passed → higher priority; then freshest ZL turn; then longest squeeze
    return (-len(f["rs_gates"]), f["zl_days"], -f["squeeze_days"])

def _static_header() -> str:
    parts = []
    if RS_EMA21_GATE:
        parts.append("Daily RS > EMA21 · EMA21 rising")
    if RS_EMA9_GATE:
        parts.append("Daily RS > EMA9 · EMA9 rising")
    if RS_WEEKLY_EMA9_GATE:
        parts.append("Weekly RS > W-EMA9 · W-EMA9 rising")
    rs_label = " OR ".join(parts) if parts else "off (no RS filter)"
    return f"""### Scan definition
| Filter | Value |
|--------|-------|
| Exchange | NSE common equity |
| Price | > ₹100 |
| Market cap | ₹800 Cr – ₹1 Lakh Cr |
| RS filter | {rs_label} |
| Signal | ZLEMA25 rising AND BB(20,2.0,SMA) inside KC(20,1.5,SMA ATR) on last bar |
| Squeeze Days | Consecutive bars the squeeze has been active |
| ZL Days / ZL Chg% | Days since ZLEMA25 last turned up · % price change since (capped {ZL_TURN_CAP}d) |

---
"""

def build_markdown(findings: list[dict], circuit: dict[str, tuple]) -> str:
    sorted_f = sorted(findings, key=_sort_key)

    T, F = "✓", "—"
    hdr = [
        "| Symbol | Close | Day Chg | Sqz Days | ZL Days | ZL Chg% | RS_EMA9 | RS_EMA21 | Weekly-RS_EMA9 | Circuit |",
        "|--------|------:|--------:|---------:|--------:|--------:|:-------:|:--------:|:--------------:|:-------:|",
    ]
    rows = []
    for f in sorted_f:
        cl, em = circuit.get(f["symbol"], ("20%", ""))
        tv     = f"https://in.tradingview.com/chart/?symbol=NSE:{f['symbol']}"
        zl_d   = f"{f['zl_days']}d+" if f["zl_days"] >= ZL_TURN_CAP else f"{f['zl_days']}d"
        zl_p   = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
        ds     = "+" if f["day_chg"] >= 0 else ""
        rows.append(
            f"| [{f['symbol']}]({tv}) "
            f"| {f['close']:.2f} "
            f"| {ds}{f['day_chg']:.2f}% "
            f"| {f['squeeze_days']}d "
            f"| {zl_d} "
            f"| {zl_p} "
            f"| {T if f['g_ema9'] else F} "
            f"| {T if f['g_ema21'] else F} "
            f"| {T if f['g_weekly9'] else F} "
            f"| {cl} {em} |"
        )

    lines = [
        f"# NSE ZL Squeeze Scan — {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        _static_header(),
        f"**{len(findings)} stocks: ZLEMA25 Rising + Squeeze ON**",
        "",
    ]
    if findings:
        lines += hdr + rows
    else:
        lines.append("*No signals today.*")
    return "\n".join(lines)


def print_results(findings: list[dict]) -> None:
    sorted_f = sorted(findings, key=_sort_key)
    print(f"\n{'='*75}")
    print(f"  NSE ZL Squeeze Scanner  |  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  ZLEMA25 Rising + Squeeze ON: {len(findings)}")
    print(f"{'='*75}")
    T, F = "✓", "—"
    for f in sorted_f:
        ds  = "+" if f["day_chg"] >= 0 else ""
        zp  = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
        e9  = T if f["g_ema9"]    else F
        e21 = T if f["g_ema21"]   else F
        we9 = T if f["g_weekly9"] else F
        print(f"  {f['symbol']:<18}  {f['close']:>9.2f}  "
              f"day:{ds}{f['day_chg']:.1f}%  sqz:{f['squeeze_days']}d  zl:{f['zl_days']}d {zp}"
              f"  RS_EMA9:{e9} RS_EMA21:{e21} Weekly-RS_EMA9:{we9}")
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
