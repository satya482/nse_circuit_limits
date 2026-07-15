#!/usr/bin/env python3
"""
NSE EMA25 ZL Scanner
Run after 4:20 PM IST on trading days (after run_fetch_data.ps1 completes).

Watchlist filters (TradingView):
  - NSE common equity
  - Price > 50 INR
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

import sys
import os
import csv
import json
from datetime import datetime

import pandas as pd
from tradingview_screener import Query, col

from ohlc_db import load_ohlc, get_names, liq_tag, cmf_tag, deliv_tag
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER
from float_gate import float_metrics, passes_hard_gate, trap_label

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "ema25_zl_scans")
_LABELS_FILE = os.path.join(REPO_DIR, "tools", "stock_labels.json")
_LABELS: dict = (
    json.loads(open(_LABELS_FILE, encoding="utf-8").read())
    if os.path.exists(_LABELS_FILE)
    else {}
)
TODAY = datetime.now().strftime("%Y-%m-%d")
MD_FILE = os.path.join(SCANS_DIR, "ema25_zl_scans.md")

MC_LOW = 1_000 * 1_00_00_000  # 1000 Cr  = 10B INR
MC_HIGH = 1_00_000 * 1_00_00_000  # 1L Cr    = 1T INR
ZL_TURN_CAP = 60
FILTER_1W_CHANGE = False  # True = require 1-week price change > 5%
FILTER_PRICE_EMA25 = False  # True = require price > EMA25 (off by default: squeeze builds before reclaim)
RS_MODE = "daily_ema21"  # "daily_ema21" | "weekly_ema9"


# ── Indicators ────────────────────────────────────────────────────────────────
def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def zlema(s: pd.Series, n: int) -> pd.Series:
    e = ema(s, n)
    return 2 * e - ema(e, n)


def _atr_wilder(
    high: pd.Series, low: pd.Series, close: pd.Series, period: int
) -> pd.Series:
    tr = pd.concat(
        [
            high - low,
            (high - close.shift(1)).abs(),
            (low - close.shift(1)).abs(),
        ],
        axis=1,
    ).max(axis=1)
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
    bb_std = c.rolling(20).std()
    bb_upper = bb_basis + 2.0 * bb_std
    bb_lower = bb_basis - 2.0 * bb_std

    kc_basis = c.rolling(20).mean()
    kc_atr = (
        _atr_wilder(h, l, c, 20)
        if kc_atr_wilder
        else (
            pd.concat([h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1)
            .max(axis=1)
            .rolling(20)
            .mean()
        )
    )
    kc_upper = kc_basis + 1.5 * kc_atr
    kc_lower = kc_basis - 1.5 * kc_atr

    return bool(
        bb_upper.iloc[-1] < kc_upper.iloc[-1] and bb_lower.iloc[-1] > kc_lower.iloc[-1]
    )


def zl25_turn_stats(zl25: pd.Series, closes: pd.Series) -> tuple[int, float]:
    n = len(zl25)
    limit = max(2, n - ZL_TURN_CAP)
    for i in range(n - 1, limit - 1, -1):
        if zl25.iloc[i] > zl25.iloc[i - 1] and zl25.iloc[i - 1] <= zl25.iloc[i - 2]:
            bars = (n - 1) - i + 1
            pct = (closes.iloc[-1] / closes.iloc[i - 1] - 1) * 100
            return bars, round(pct, 2)
    cap_idx = max(0, n - ZL_TURN_CAP)
    return ZL_TURN_CAP, round((closes.iloc[-1] / closes.iloc[cap_idx] - 1) * 100, 2)


RVOL_FLAG = 8.0  # matches wt_bullcross_scanner.py / Strong Start RVOL Dashboard.pine
SS_LOWMULT = 0.995  # day low must hold >= prev close x this (Pine parity)


def _rvol_ss(df: pd.DataFrame) -> tuple[float, bool]:
    """RVOL = today's volume / prior-20d avg volume; SS = gapped up and held.
    Mirrors wt_bullcross_scanner._rvol_ss() (Pine parity source there)."""
    vol = df["volume"].astype(float)
    avg_vol = vol.iloc[-21:-1].mean()
    rvol = float(vol.iloc[-1] / avg_vol) if avg_vol > 0 else 0.0
    today_open = float(df["open"].iloc[-1])
    today_low = float(df["low"].iloc[-1])
    prev_close = float(df["close"].iloc[-2])
    strong_start = today_open > prev_close and today_low >= prev_close * SS_LOWMULT
    return rvol, strong_start


# ── Watchlist ──────────────────────────────────────────────────────────────────
def get_watchlist() -> tuple[list[str], dict[str, float]]:
    """Returns (symbols, float_map) where float_map = {symbol: float_shares}.
    Symbols with no TV float data are absent from float_map (gate then skipped)."""
    filters = [
        col("exchange") == "NSE",
        col("type") == "stock",
        col("typespecs").has(["common"]),
        col("close") > 50,
        col("market_cap_basic").between(MC_LOW, MC_HIGH),
    ]
    if FILTER_PRICE_EMA25:
        filters.append(col("close") > col("EMA25"))
    if FILTER_1W_CHANGE:
        filters.append(col("Perf.W") > 5)

    _, df = (
        Query()
        .set_markets("india")
        .select("name", "close", "EMA25", "Perf.W", "float_shares_outstanding")
        .where(*filters)
        .limit(500)
        .get_scanner_data()
    )
    float_map = {
        row["name"]: float(row["float_shares_outstanding"])
        for _, row in df.iterrows()
        if pd.notna(row.get("float_shares_outstanding"))
        and row["float_shares_outstanding"] > 0
    }
    return df["name"].tolist(), float_map


# ── Circuit limits ─────────────────────────────────────────────────────────────
_CIRCUIT_EMOJI = {
    ("20", "10"): "🟨",
    ("10", "5"): "🟥",
    ("5", "10"): "🟩",
    ("10", "20"): "🟦",
}
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
                to = row.get("TO", "")
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
def _weekly_rs_gate(rs: pd.Series, c_rs: pd.Series, idx_rs: pd.Series) -> bool:
    """Daily RS Line > Weekly RS EMA9 AND Weekly RS EMA9 rising.
    Mirrors wt_bullcross_scanner._rs_weekly_gate() — kept in sync per CLAUDE.md."""
    weekly_c = c_rs.resample("W").last().dropna()
    weekly_idx = idx_rs.resample("W").last().dropna()
    wk_common = weekly_c.index.intersection(weekly_idx.index)
    if len(wk_common) < 12:
        return False
    wk_rs = (weekly_c.loc[wk_common] / weekly_idx.loc[wk_common]) * 1000
    wk_rs_e9 = ema(wk_rs, 9)
    return bool(
        rs.iloc[-1] > wk_rs_e9.iloc[-1] and wk_rs_e9.iloc[-1] > wk_rs_e9.iloc[-2]
    )


def _rs_gate(rs: pd.Series, c_rs: pd.Series, idx_rs: pd.Series) -> bool:
    """Return True if the stock passes the active RS filter (RS_MODE)."""
    if RS_MODE == "weekly_ema9":
        return _weekly_rs_gate(rs, c_rs, idx_rs)
    else:  # daily_ema21
        if len(rs) < 22:
            return False
        rs_e21 = ema(rs, 21)
        return bool(rs.iloc[-1] > rs_e21.iloc[-1] and rs_e21.iloc[-1] > rs_e21.iloc[-2])


# ── Stock analysis ─────────────────────────────────────────────────────────────
def analyse(symbol: str, index_s: pd.Series, float_shares: float = 0) -> dict | None:
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

        c_rs = c.loc[common]
        idx_rs = index_s.loc[common]
        rs = (c_rs / idx_rs) * 1000

        if not _rs_gate(rs, c_rs, idx_rs):
            return None

        fm = float_metrics(raw["close"], raw["volume"], float_shares or None)
        if not passes_hard_gate(fm):
            return None

        # ZLEMA25
        zl25 = zlema(c, 25)
        zl_rising = zl25.iloc[-1] > zl25.iloc[-2]

        curr_close = c.iloc[-1]
        prev_close = c.iloc[-2]
        day_chg = (curr_close - prev_close) / prev_close * 100

        zl_days, zl_pct = zl25_turn_stats(zl25, c)
        rvol, strong_start = _rvol_ss(raw)

        return {
            "symbol": symbol,
            "close": curr_close,
            "day_chg": day_chg,
            "zl_rising": zl_rising,
            "zl_days": zl_days,
            "zl_pct": zl_pct,
            "squeeze": bb_kc_squeeze(raw),
            "trap": trap_label(fm),
            "rs_weekly_gate": _weekly_rs_gate(rs, c_rs, idx_rs),
            "rvol": round(rvol, 2),
            "strong_start": strong_start,
            "liq_tag": liq_tag(raw),
            "cmf_tag": cmf_tag(raw),
            "deliv_tag": deliv_tag(symbol),
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
| Price | > ₹50 |
| 1-week change | {w1} |
| Market cap | ₹1,000 Cr – ₹1 Lakh Cr |
| Price vs EMA25 | {ema25} |
| RS filter | {rs_label} |
| ZL Days / ZL Chg% | Days since ZLEMA25 last turned up · % price change since that bar (capped {cap}d) |
| Squeeze | ✓ = BB(20,2.0,SMA) fully inside KC(20,1.5,SMA) on last bar |
| Float gate | ⛔ AVOID dropped from scan · ✓ SAFE / ⚠ CAUTION shown under symbol (float_gate.py) |
| Symbol tags | trap · liq (↗avg10Cr·todayCr) · 📶W9 weekly-RS gate · 🚀SS/RVOL{rvol_flag:.0f}x · CMF · DEL% |

---
""".format(
    cap=ZL_TURN_CAP,
    rvol_flag=RVOL_FLAG,
    rs_label=_RS_FILTER_LABEL.get(RS_MODE, RS_MODE),
    w1="> 5%" if FILTER_1W_CHANGE else "off",
    ema25="Price > EMA25" if FILTER_PRICE_EMA25 else "off",
)


def _table_rows(
    findings: list[dict],
    circuit: dict[str, tuple],
    names: dict[str, str],
) -> list[str]:
    rows = []
    for f in findings:
        sym = f["symbol"]
        cl, em = circuit.get(sym, ("20%", ""))
        tv = f"https://in.tradingview.com/chart/?symbol=NSE:{sym}"
        zl_d = (
            f"{f['zl_days']}d+" if f["zl_days"] >= ZL_TURN_CAP else f"{f['zl_days']}d"
        )
        zl_p = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
        ds = "+" if f["day_chg"] >= 0 else ""
        sqz = "✓" if f.get("squeeze") else "—"
        lbl_cell = _LABELS.get(sym, "")
        extras = []
        trap = f.get("trap", "")
        if trap and trap != "n/a":
            extras.append(trap)
        if f.get("liq_tag"):
            extras.append(f["liq_tag"])
        if f.get("rs_weekly_gate"):
            extras.append("📶W9")
        rvol, ss = f.get("rvol", 0.0), f.get("strong_start", False)
        if ss and rvol >= RVOL_FLAG:
            extras.append(f"🚀SS·{rvol:.0f}x")
        elif ss:
            extras.append("🚀SS")
        elif rvol >= RVOL_FLAG:
            extras.append(f"RVOL{rvol:.0f}x")
        if f.get("cmf_tag"):
            extras.append(f["cmf_tag"])
        if f.get("deliv_tag"):
            extras.append(f["deliv_tag"])
        sym_cell = f"[{sym}]({tv})" + (f"<br><sub>{' · '.join(extras)}</sub>" if extras else "")
        rows.append(
            f"| {sym_cell} "
            f"| {zl_d} "
            f"| {zl_p} "
            f"| {lbl_cell} "
            f"| {ds}{f['day_chg']:.2f}% "
            f"| {f['close']:.2f} "
            f"| {sqz} "
            f"| {cl} {em} |"
        )
    return rows


def build_markdown(
    findings: list[dict], circuit: dict[str, tuple], names: dict[str, str] | None = None
) -> str:
    names = names or {}
    rising = sorted([f for f in findings if f["zl_rising"]], key=lambda x: x["zl_days"])
    watch = sorted(
        [f for f in findings if not f["zl_rising"]], key=lambda x: x["zl_days"]
    )

    hdr = [
        "| Symbol | ZL Days | ZL Chg% | Label | Day Chg | Close | Squeeze | Circuit |",
        "|--------|--------:|--------:|-------|--------:|------:|:-------:|:-------:|",
    ]

    # Single TV-importable watchlist: ###NAME entries become colored sections in TradingView
    buckets = [
        ("1 DAY", 1, 1),
        ("2 DAYS", 2, 2),
        ("3 DAYS", 3, 3),
        ("4-5 DAYS", 4, 5),
        ("6-10 DAYS", 6, 10),
        ("11-15 DAYS", 11, 15),
        ("15 DAYS+", 16, 10**9),
    ]
    wl_parts = []
    for label, lo, hi in buckets:
        syms = [f["symbol"] for f in rising if lo <= f["zl_days"] <= hi]
        if syms:
            wl_parts.append(f"###{label}," + ",".join(f"NSE:{s}" for s in syms))
    if watch:
        wl_parts.append("###WATCH," + ",".join(f"NSE:{f['symbol']}" for f in watch))

    lines = [
        f"# NSE EMA25 ZL Scan — {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        STATIC_HEADER,
        f"**ZLEMA25 Rising: {len(rising)}** &nbsp;|&nbsp; **ZLEMA25 Watch: {len(watch)}**",
        "",
        "**TradingView watchlist** *(sectioned by ZL days since turn-up — paste into TV import)*",
        "```",
        ",".join(wl_parts),
        "```",
        "",
        "### ZLEMA25 Rising",
    ]
    if rising:
        lines += hdr + _table_rows(rising, circuit, names)
        lines += ["", "```", ",".join(f"NSE:{f['symbol']}" for f in rising), "```"]
    else:
        lines.append("*No ZLEMA25 rising stocks today.*")

    lines += ["", "### ZLEMA25 Watch *(pullback / flat)*"]
    if watch:
        lines += hdr + _table_rows(watch, circuit, names)
        lines += ["", "```", ",".join(f"NSE:{f['symbol']}" for f in watch), "```"]
    else:
        lines.append("*No ZLEMA25 watch stocks today.*")

    lines += ["", "### TradingView Watchlists *(by ZL days since turn-up)*"]
    buckets = [
        ("1 day", 1, 1),
        ("2 days", 2, 2),
        ("3 days", 3, 3),
        ("4-5 days", 4, 5),
        ("6-10 days", 6, 10),
        ("11-15 days", 11, 15),
        ("15 days+", 16, 10**9),
    ]
    for label, lo, hi in buckets:
        syms = [f["symbol"] for f in rising if lo <= f["zl_days"] <= hi]
        if not syms:
            continue
        lines += [
            "",
            f"**{label}** ({len(syms)})",
            "```",
            ",".join(f"NSE:{s}" for s in syms),
            "```",
        ]

    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


# ── Console output ─────────────────────────────────────────────────────────────
def print_results(findings: list[dict]) -> None:
    rising = [f for f in findings if f["zl_rising"]]
    watch = [f for f in findings if not f["zl_rising"]]

    print(f"\n{'='*70}")
    print(f"  NSE EMA25 ZL Scanner  |  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  ZLEMA25 Rising: {len(rising)}   ZLEMA25 Watch: {len(watch)}")
    print(f"{'='*70}")

    if rising:
        print("\n  ── ZLEMA25 Rising (top 15 by ZL Chg%) ──")
        for f in rising[:15]:
            ds = "+" if f["day_chg"] >= 0 else ""
            zp = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
            zd = (
                f"{f['zl_days']}d+"
                if f["zl_days"] >= ZL_TURN_CAP
                else f"{f['zl_days']}d"
            )
            print(
                f"  {f['symbol']:<18}  {f['close']:>9.2f}  day:{ds}{f['day_chg']:.1f}%  zl:{zd} {zp}"
            )

    if watch:
        print(f"\n  ── ZLEMA25 Watch ({len(watch)} stocks) ──")
        for f in watch[:10]:
            ds = "+" if f["day_chg"] >= 0 else ""
            zp = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
            print(
                f"  {f['symbol']:<18}  {f['close']:>9.2f}  day:{ds}{f['day_chg']:.1f}%  zl:{f['zl_days']}d {zp}"
            )
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
    print(
        f"  Index data: {len(index_s)} days  (latest: {index_s.index[-1].date()}  {index_s.iloc[-1]:.2f})"
    )

    print("\nFetching NSE circuit limits...")
    circuit = get_circuit_limits()
    print(f"  Circuit data: {len(circuit)} stocks with recent limit changes")

    print("\nFetching live watchlist from TradingView screener...")
    watchlist, float_map = get_watchlist()
    print(
        f"  Watchlist: {len(watchlist)} stocks  |  float data for {len(float_map)}  |  Scanning...\n"
    )

    findings = []
    for i, sym in enumerate(watchlist, 1):
        print(f"  {sym:<20} ({i}/{len(watchlist)})   ", end="\r")
        result = analyse(sym, index_s, float_shares=float_map.get(sym, 0))
        if result:
            findings.append(result)

    print_results(findings)

    dated_file = os.path.join(SCANS_DIR, f"ema25_zl_scans_{TODAY}.md")
    names = get_names([f["symbol"] for f in findings])
    md = build_markdown(findings, circuit, names)
    with open(MD_FILE, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(dated_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"\n  Saved -> {MD_FILE}")
    print(f"  Saved -> {dated_file}")


if __name__ == "__main__":
    main()
