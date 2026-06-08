#!/usr/bin/env python3
"""
WaveTrend Bull Cross Scanner
Run after 4:05 PM IST on trading days (after run_fetch_data.ps1).

Universe: NSE common equity, MCap ₹1,000 Cr – ₹5 Lakh Cr, price > ₹50
          No RS filter — WT captures oversold reversals before RS turns positive.

Signal hierarchy (wt_signal_rank):
  +5  BULL_OS_PPV    — deep oversold cross + Pocket Pivot Volume [strongest]
  +4  BULL_ANY_PPV   — any cross + Pocket Pivot Volume
  +3  BULL_OVERSOLD  — deep oversold cross (wt2 ≤ -60)
  +2  BULL_OS_L2     — soft oversold cross (wt2 ≤ -53)
  +1  BULL_ZERO_CROSS — WT1 crosses above 0 (momentum confirmation)

Context columns:
  ZL    : ZLEMA25 direction (↑ rising / ↓ flat-down)
  Sqz   : BB(20,2.0,SMA) fully inside KC(20,1.5,SMA) on last bar
  PPV   : Pocket Pivot Volume fires

Output: wt_scans/wt_bullcross_latest.md
        wt_scans/wt_bullcross_YYYY-MM-DD.md
"""

import sys, os, csv, json
from datetime import datetime

import pandas as pd
from tradingview_screener import Query, col

from ohlc_db import load_ohlc_many
from wavetrend_scanner import WaveTrendCalculator

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR     = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR    = os.path.join(REPO_DIR, "wt_scans")
_LABELS_FILE = os.path.join(REPO_DIR, "tools", "stock_labels.json")
_LABELS: dict = json.loads(open(_LABELS_FILE, encoding="utf-8").read()) if os.path.exists(_LABELS_FILE) else {}
TODAY        = datetime.now().strftime("%Y-%m-%d")
MD_LATEST    = os.path.join(SCANS_DIR, "wt_bullcross_latest.md")
MD_DATED     = os.path.join(SCANS_DIR, f"wt_bullcross_{TODAY}.md")

MC_LOW   = 1_000   * 1_00_00_000   # 1,000 Cr
MC_HIGH  = 5_00_000 * 1_00_00_000  # 5 Lakh Cr
MIN_RANK = 1
ZL_TURN_CAP = 60


# ── Indicators ────────────────────────────────────────────────────────────────

def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()

def _zlema(s: pd.Series, n: int) -> pd.Series:
    e = _ema(s, n)
    return 2 * e - _ema(e, n)

def _bb_kc_squeeze(df: pd.DataFrame) -> bool:
    """True if BB(20,2.0,SMA) is fully inside KC(20,1.5,SMA ATR) on the last bar."""
    if len(df) < 21:
        return False
    c = df["close"].astype(float)
    h = df["high"].astype(float)
    l = df["low"].astype(float)
    bb_basis = c.rolling(20).mean()
    bb_std   = c.rolling(20).std()
    bb_upper = bb_basis + 2.0 * bb_std
    bb_lower = bb_basis - 2.0 * bb_std
    tr       = pd.concat([h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1).max(axis=1)
    kc_atr   = tr.rolling(20).mean()
    kc_basis = c.rolling(20).mean()
    kc_upper = kc_basis + 1.5 * kc_atr
    kc_lower = kc_basis - 1.5 * kc_atr
    return bool(bb_upper.iloc[-1] < kc_upper.iloc[-1] and bb_lower.iloc[-1] > kc_lower.iloc[-1])

def _zl25_turn_stats(zl25: pd.Series, closes: pd.Series) -> tuple[int, float]:
    n     = len(zl25)
    limit = max(2, n - ZL_TURN_CAP)
    for i in range(n - 1, limit - 1, -1):
        if zl25.iloc[i] > zl25.iloc[i - 1] and zl25.iloc[i - 1] <= zl25.iloc[i - 2]:
            bars = (n - 1) - i + 1
            pct  = (closes.iloc[-1] / closes.iloc[i - 1] - 1) * 100
            return bars, round(pct, 2)
    cap_idx = max(0, n - ZL_TURN_CAP)
    return ZL_TURN_CAP, round((closes.iloc[-1] / closes.iloc[cap_idx] - 1) * 100, 2)


# ── Watchlist ─────────────────────────────────────────────────────────────────

def get_watchlist() -> list[str]:
    """Broad universe — no RS or EMA25 filter (WT captures pre-RS-turn reversals)."""
    _, df = (
        Query()
        .set_markets("india")
        .select("name", "close", "market_cap_basic")
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


# ── Circuit limits ────────────────────────────────────────────────────────────

_CIRCUIT_EMOJI = {("20", "10"): "🟨", ("10", "5"): "🟥", ("5", "10"): "🟩", ("10", "20"): "🟦"}
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
                sym = row.get("SYMBOL", "")
                dte = row.get("EFFECTIVE DATE", "")
                frm = row.get("FROM", "")
                to  = row.get("TO", "")
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


# ── Per-stock analysis ────────────────────────────────────────────────────────

def analyse(symbol: str, df_raw: pd.DataFrame, calc: WaveTrendCalculator) -> dict | None:
    try:
        if df_raw is None or len(df_raw) < 83:   # WaveTrendCalculator._min_bars
            return None

        sig = calc.get_signal(df_raw)
        if sig.wt_signal_rank < MIN_RANK:
            return None

        c    = df_raw["close"].astype(float)
        zl25 = _zlema(c, 25)
        zl_rising = bool(zl25.iloc[-1] > zl25.iloc[-2])
        zl_days, zl_pct = _zl25_turn_stats(zl25, c)

        curr_close = float(c.iloc[-1])
        prev_close = float(c.iloc[-2])
        day_chg    = (curr_close - prev_close) / prev_close * 100

        return {
            "symbol":    symbol,
            "wt_signal": sig.wt_signal,
            "wt_rank":   sig.wt_signal_rank,
            "wt1":       round(sig.wt1, 2),
            "wt2":       round(sig.wt2, 2),
            "wt_is_ppv": sig.wt_is_ppv,
            "zl_rising": zl_rising,
            "zl_days":   zl_days,
            "zl_pct":    zl_pct,
            "squeeze":   _bb_kc_squeeze(df_raw),
            "close":     curr_close,
            "day_chg":   day_chg,
        }
    except Exception:
        return None


# ── Markdown output ───────────────────────────────────────────────────────────

_RANK_EMOJI = {5: "🔥", 4: "⚡", 3: "🟢", 2: "🟡", 1: "📈"}
_RANK_LABEL = {5: "BULL OS+PPV", 4: "BULL ANY+PPV", 3: "BULL OVERSOLD", 2: "BULL OS L2", 1: "ABOVE ZERO LINE"}

_CATEGORIES = [
    ("🔥", "MAJOR",           "PPV confirmed",         [5, 4]),
    ("🟢", "OVERSOLD",        "reversal from −53/−60", [3, 2]),
    ("📈", "ABOVE ZERO LINE", "momentum confirmed",    [1]),
]

_HDR = [
    "| Symbol | Label | Signal | Rank | WT1 | WT2 | ZL | ZL Days | ZL Chg% | Sqz | PPV | Day Chg | Close | Circuit |",
    "|--------|-------|--------|:----:|----:|----:|:--:|--------:|--------:|:---:|:---:|--------:|------:|:-------:|",
]


def _row(f: dict, circuit: dict) -> str:
    sym      = f["symbol"]
    tv       = f"https://in.tradingview.com/chart/?symbol=NSE:{sym}"
    cl, em   = circuit.get(sym, ("20%", ""))
    zl_d     = f"{f['zl_days']}d+" if f["zl_days"] >= ZL_TURN_CAP else f"{f['zl_days']}d"
    zl_p     = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
    ds       = "+" if f["day_chg"] >= 0 else ""
    zl_arrow = "↑" if f["zl_rising"] else "↓"
    sqz      = "✓" if f["squeeze"] else "—"
    ppv      = "✓" if f["wt_is_ppv"] else "—"
    emoji    = _RANK_EMOJI.get(f["wt_rank"], "")
    lbl      = _LABELS.get(sym, "")
    return (
        f"| [{sym}]({tv}) "
        f"| {lbl} "
        f"| {emoji} {f['wt_signal']} "
        f"| {f['wt_rank']} "
        f"| {f['wt1']} "
        f"| {f['wt2']} "
        f"| {zl_arrow} "
        f"| {zl_d} "
        f"| {zl_p} "
        f"| {sqz} "
        f"| {ppv} "
        f"| {ds}{f['day_chg']:.2f}% "
        f"| {f['close']:.2f} "
        f"| {cl} {em} |"
    )


def build_markdown(findings: list[dict], circuit: dict) -> str:
    # Sort: rank desc, then wt1 asc within rank (deeper oversold first)
    sorted_f = sorted(findings, key=lambda x: (-x["wt_rank"], x["wt1"]))

    rank_groups: dict[int, list] = {}
    for f in sorted_f:
        rank_groups.setdefault(f["wt_rank"], []).append(f)

    lines = [
        f"# WaveTrend Bull Cross Scan — {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        "### Scan definition",
        "| Filter | Value |",
        "|--------|-------|",
        "| Exchange | NSE common equity |",
        "| Price | > ₹50 |",
        "| Market cap | ₹1,000 Cr – ₹5 Lakh Cr |",
        "| RS filter | None — WT captures pre-RS-turn reversals |",
        "| Min rank | Any bull cross (rank ≥ 1) |",
        "| Sqz | BB(20,2.0,SMA) inside KC(20,1.5,SMA) on last bar |",
        "",
        "---",
        "",
        f"**Total bull crosses today: {len(findings)}**",
        "",
    ]

    for emoji, cat_name, cat_desc, ranks in _CATEGORIES:
        group = [f for r in ranks for f in rank_groups.get(r, [])]
        group.sort(key=lambda x: (-x["wt_rank"], x["wt1"]))
        lines.append(f"### {emoji} {cat_name} — {cat_desc} ({len(group)})")
        if group:
            lines += _HDR + [_row(f, circuit) for f in group]
        else:
            lines.append("*No signals.*")
        lines.append("")

    return "\n".join(lines)


# ── Console output ─────────────────────────────────────────────────────────────

def print_results(findings: list[dict]) -> None:
    print(f"\n{'='*70}")
    print(f"  WaveTrend Bull Cross Scanner  |  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Total bull crosses: {len(findings)}")
    print(f"{'='*70}")
    for emoji, cat_name, _cat_desc, ranks in _CATEGORIES:
        group = [f for f in findings if f["wt_rank"] in ranks]
        if not group:
            continue
        group.sort(key=lambda x: (-x["wt_rank"], x["wt1"]))
        print(f"\n  ── {emoji} {cat_name} ({len(group)}) ──")
        for f in group:
            ds  = "+" if f["day_chg"] >= 0 else ""
            zl  = "ZL↑" if f["zl_rising"] else "ZL↓"
            sqz = "SQZ" if f["squeeze"] else "   "
            ppv = "PPV" if f["wt_is_ppv"] else "   "
            print(f"  {f['symbol']:<18} {f['close']:>9.2f}  "
                  f"wt1:{f['wt1']:>7.2f}  {zl} {sqz} {ppv}  "
                  f"day:{ds}{f['day_chg']:.1f}%")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nFetching watchlist from TradingView screener...")
    watchlist = get_watchlist()
    print(f"  {len(watchlist)} stocks")

    print("\nLoading OHLCV from SQLite (batch)...")
    all_data = load_ohlc_many(watchlist, lookback=400)
    print(f"  Loaded {len(all_data)} stocks")

    print("\nFetching circuit limits...")
    circuit = get_circuit_limits()

    print(f"\nScanning {len(all_data)} stocks for WaveTrend bull crosses...")
    calc     = WaveTrendCalculator()
    findings = []
    for i, (sym, df_raw) in enumerate(all_data.items(), 1):
        print(f"  {sym:<20} ({i}/{len(all_data)})   ", end="\r")
        result = analyse(sym, df_raw, calc)
        if result:
            findings.append(result)

    print_results(findings)

    md = build_markdown(findings, circuit)
    with open(MD_LATEST, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(MD_DATED, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  Saved → {MD_LATEST}")
    print(f"  Saved → {MD_DATED}")


if __name__ == "__main__":
    main()
