#!/usr/bin/env python3
"""
US ZL Squeeze Scanner
Stocks where ZLEMA25 is Rising AND BB Squeeze is ON simultaneously.
Data sourced from local SQLite (populated by fetch_us_data.py).

Universe : NYSE + NASDAQ common equity, MCap $300M–$10B, price > $5,
           avg 10d vol > 300K (screener pre-filter)
RS bench : SPY
RS scale : ×100  (stock_close / SPY_close × 100)
Signal   : ZLEMA25 rising on last bar AND BB(20,2.0,SMA) inside KC(20,1.5,SMA ATR)
Extra    : Relative Volume, Squeeze duration, RS gates

Output   : us_zl_squeeze_scans/us_zl_squeeze_scans.md
"""

import sys, os
from datetime import datetime

import pandas as pd
from tradingview_screener import Query, col

from us_ohlc_db import load_ohlc

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR  = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "us_zl_squeeze_scans")
TODAY     = datetime.now().strftime("%Y-%m-%d")
MD_FILE   = os.path.join(SCANS_DIR, "us_zl_squeeze_scans.md")

MC_LOW  = 300_000_000
MC_HIGH = 10_000_000_000
ZL_TURN_CAP = 60

# ── Gate flags ─────────────────────────────────────────────────────────────────
REL_VOL_GATE        = True   # today vol / 20d avg > 1.5
RS_EMA9_GATE        = True   # daily RS > EMA9 AND EMA9 rising
RS_EMA21_GATE       = True   # daily RS > EMA21 AND EMA21 rising
RS_WEEKLY_EMA9_GATE = True   # daily RS > weekly RS EMA9 AND weekly EMA9 rising

REL_VOL_MIN = 1.5
BENCHMARK   = "SPY"
RS_SCALE    = 100   # ×100 keeps numbers in readable range vs SPY's price level


# ── Indicators ─────────────────────────────────────────────────────────────────
def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()

def zlema(s: pd.Series, n: int) -> pd.Series:
    e = ema(s, n)
    return 2 * e - ema(e, n)

def bb_kc_squeeze_info(df: pd.DataFrame) -> tuple[bool, int]:
    """Returns (squeeze_on, consecutive_bars_in_squeeze) as of the last bar.
    BB(20,2.0,SMA) inside KC(20,1.5,SMA ATR) — matches TradingView defaults."""
    c, h, l = df["close"].astype(float), df["high"].astype(float), df["low"].astype(float)
    if len(c) < 21:
        return False, 0
    # Bollinger Bands
    mid  = c.rolling(20).mean()
    std  = c.rolling(20).std(ddof=0)
    bb_u = mid + 2.0 * std
    bb_l = mid - 2.0 * std
    # Keltner Channel (SMA ATR — matches TradingView ta.sma(ta.tr))
    tr   = pd.concat([h - l,
                      (h - c.shift()).abs(),
                      (l - c.shift()).abs()], axis=1).max(axis=1)
    atr  = tr.rolling(20).mean()
    kc_u = mid + 1.5 * atr
    kc_l = mid - 1.5 * atr
    # Squeeze: BB fully inside KC
    sq   = (bb_u < kc_u) & (bb_l > kc_l)
    if not sq.iloc[-1]:
        return False, 0
    # Count consecutive bars
    count = 0
    for v in reversed(sq.values):
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
            pct  = (closes.iloc[-1] / closes.iloc[i - 1] - 1) * 100
            return bars, round(pct, 2)
    cap_idx = max(0, n - ZL_TURN_CAP - 1)
    return ZL_TURN_CAP, round((closes.iloc[-1] / closes.iloc[max(0, cap_idx - 1)] - 1) * 100, 2)


# ── Watchlist ──────────────────────────────────────────────────────────────────
def get_watchlist() -> list[str]:
    _, df = (
        Query()
        .set_markets("america")
        .select("name", "close")
        .where(
            col("exchange").isin(["NASDAQ", "NYSE"]),
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("close") > 5,
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
            col("average_volume_10d_calc") > 300_000,
        )
        .limit(3000)
        .get_scanner_data()
    )
    return df["name"].tolist()


# ── RS gates ───────────────────────────────────────────────────────────────────
def _rs_gate_ema9(rs: pd.Series) -> bool:
    if len(rs) < 10:
        return False
    e = ema(rs, 9)
    return bool(rs.iloc[-1] > e.iloc[-1] and e.iloc[-1] > e.iloc[-2])

def _rs_gate_ema21(rs: pd.Series) -> bool:
    if len(rs) < 22:
        return False
    e = ema(rs, 21)
    return bool(rs.iloc[-1] > e.iloc[-1] and e.iloc[-1] > e.iloc[-2])

def _rs_gate_weekly_ema9(rs: pd.Series, c_rs: pd.Series, idx_rs: pd.Series) -> bool:
    """Daily RS line > Weekly RS EMA9 AND Weekly RS EMA9 rising.
    Drops the incomplete current week (resample label > last daily date)."""
    wk_c   = c_rs.resample("W").last().dropna()
    wk_idx = idx_rs.resample("W").last().dropna()
    common = wk_c.index.intersection(wk_idx.index)
    if len(common) < 12:
        return False
    wk_rs = (wk_c.loc[common] / wk_idx.loc[common]) * RS_SCALE
    last_daily = rs.index[-1]
    if wk_rs.index[-1] > last_daily:
        wk_rs = wk_rs.iloc[:-1]
    if len(wk_rs) < 11:
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
        v  = df["volume"].astype(float)

        # Relative volume: today / 20d avg (excluding today)
        rel_vol = 0.0
        if len(v) >= 22:
            avg_vol = v.iloc[-21:-1].mean()
            rel_vol = (v.iloc[-1] / avg_vol) if avg_vol > 0 else 0.0
        if REL_VOL_GATE and rel_vol < REL_VOL_MIN:
            return None

        common = c.index.intersection(index_s.index)
        if len(common) < 30:
            return None

        c_rs   = c.loc[common]
        idx_rs = index_s.loc[common]
        rs     = (c_rs / idx_rs) * RS_SCALE

        g_ema9    = _rs_gate_ema9(rs)
        g_ema21   = _rs_gate_ema21(rs)
        g_weekly9 = _rs_gate_weekly_ema9(rs, c_rs, idx_rs)

        any_gate = RS_EMA9_GATE or RS_EMA21_GATE or RS_WEEKLY_EMA9_GATE
        if any_gate:
            enabled_passed = (
                (RS_EMA9_GATE        and g_ema9)    or
                (RS_EMA21_GATE       and g_ema21)   or
                (RS_WEEKLY_EMA9_GATE and g_weekly9)
            )
            if not enabled_passed:
                return None

        rs_passed = []
        if RS_EMA9_GATE        and g_ema9:    rs_passed.append("EMA9")
        if RS_EMA21_GATE       and g_ema21:   rs_passed.append("EMA21")
        if RS_WEEKLY_EMA9_GATE and g_weekly9: rs_passed.append("W-EMA9")

        zl25      = zlema(c, 25)
        zl_rising = bool(zl25.iloc[-1] > zl25.iloc[-2])
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
            "rel_vol":      rel_vol,
            "zl_days":      zl_days,
            "zl_pct":       zl_pct,
            "squeeze_days": squeeze_days,
            "rs_gates":     rs_passed,
            "g_ema9":       g_ema9,
            "g_ema21":      g_ema21,
            "g_weekly9":    g_weekly9,
        }
    except Exception:
        return None


# ── Output ─────────────────────────────────────────────────────────────────────
def _sort_key(f: dict):
    return (-len(f["rs_gates"]), f["zl_days"], -f["squeeze_days"])

def _static_header() -> str:
    rs_parts = []
    if RS_EMA9_GATE:        rs_parts.append("Daily RS > EMA9 · EMA9 rising")
    if RS_EMA21_GATE:       rs_parts.append("Daily RS > EMA21 · EMA21 rising")
    if RS_WEEKLY_EMA9_GATE: rs_parts.append("Daily RS > Weekly RS EMA9 · EMA9 rising")
    rs_label = " OR ".join(rs_parts) if rs_parts else "off (no RS filter)"
    rv_label = f"> {REL_VOL_MIN}x" if REL_VOL_GATE else "off"
    return f"""### Scan definition
| Filter | Value |
|--------|-------|
| Exchange | NYSE + NASDAQ common equity |
| Price | > $5 |
| Market cap | $300M – $10B (small + mid cap) |
| Avg 10d Volume | > 300K |
| Relative Volume | {rv_label} |
| RS benchmark | SPY (×100 scale) |
| RS filter | {rs_label} |
| Signal | ZLEMA25 rising AND BB(20,2.0,SMA) inside KC(20,1.5,SMA ATR) on last bar |
| Squeeze Days | Consecutive bars the squeeze has been active |
| ZL Days / ZL Chg% | Days since ZLEMA25 last turned up · % price change since (capped {ZL_TURN_CAP}d) |

---
"""

def build_markdown(findings: list[dict]) -> str:
    sorted_f = sorted(findings, key=_sort_key)
    T, F = "✓", "—"
    hdr = [
        "| Symbol | Close | Day Chg | Rel Vol | Sqz Days | ZL Days | ZL Chg% | RS_EMA9 | RS_EMA21 | Weekly-RS_EMA9 |",
        "|--------|------:|--------:|--------:|---------:|--------:|--------:|:-------:|:--------:|:--------------:|",
    ]
    rows = []
    for f in sorted_f:
        tv  = f"https://www.tradingview.com/chart/?symbol={f['symbol']}"
        zl_d = f"{f['zl_days']}d+" if f["zl_days"] >= ZL_TURN_CAP else f"{f['zl_days']}d"
        zl_p = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
        ds   = "+" if f["day_chg"] >= 0 else ""
        rv   = f"{f['rel_vol']:.1f}x"
        rows.append(
            f"| [{f['symbol']}]({tv}) "
            f"| {f['close']:.2f} "
            f"| {ds}{f['day_chg']:.2f}% "
            f"| {rv} "
            f"| {f['squeeze_days']}d "
            f"| {zl_d} "
            f"| {zl_p} "
            f"| {T if f['g_ema9']    else F} "
            f"| {T if f['g_ema21']   else F} "
            f"| {T if f['g_weekly9'] else F} |"
        )

    lines = [
        f"# US ZL Squeeze Scan — {TODAY}",
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
    print(f"  US ZL Squeeze Scanner  |  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  ZLEMA25 Rising + Squeeze ON: {len(findings)}")
    print(f"{'='*75}")
    T, F = "✓", "—"
    for f in sorted_f:
        ds  = "+" if f["day_chg"] >= 0 else ""
        zp  = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
        e9  = T if f["g_ema9"]    else F
        e21 = T if f["g_ema21"]   else F
        we9 = T if f["g_weekly9"] else F
        print(f"  {f['symbol']:<8}  {f['close']:>9.2f}  "
              f"day:{ds}{f['day_chg']:.1f}%  rv:{f['rel_vol']:.1f}x  "
              f"sqz:{f['squeeze_days']}d  zl:{f['zl_days']}d {zp}"
              f"  RS_EMA9:{e9} RS_EMA21:{e21} Weekly-RS_EMA9:{we9}")
    print()


# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nLoading SPY from DB...")
    bm_raw = load_ohlc(BENCHMARK)
    if bm_raw is None or bm_raw.empty:
        print("  ERROR: SPY not in DB. Run fetch_us_data.py first.")
        return
    bm_raw = bm_raw.set_index("date")
    bm_raw.index = pd.to_datetime(bm_raw.index)
    index_s = bm_raw["close"].astype(float)
    print(f"  SPY: {len(index_s)} days  (latest: {index_s.index[-1].date()}  ${index_s.iloc[-1]:.2f})")

    print("\nFetching live watchlist from TradingView screener (US)...")
    watchlist = get_watchlist()
    print(f"  Watchlist: {len(watchlist)} stocks  |  Scanning...\n")

    findings = []
    for i, sym in enumerate(watchlist, 1):
        result = analyse(sym, index_s)
        if result:
            findings.append(result)
        if i % 200 == 0:
            print(f"  {i}/{len(watchlist)}  hits so far: {len(findings)}")

    print_results(findings)

    md = build_markdown(findings)
    with open(MD_FILE, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  Saved -> {MD_FILE}")


if __name__ == "__main__":
    main()
