#!/usr/bin/env python3
"""
NSE Inside Bar / Mini Coil Scanner
Stocks where all bars since a "mother bar" are contained within its high/low range.

Watchlist: NSE common equity, price > ₹50, MCap ₹800 Cr – ₹1 Lakh Cr
Signal:    Find the LONGEST active coil ending today (mother bar up to 20 bars back,
           minimum 2 consecutive inside bars)
Output:    inside_bar_scans/inside_bar_scans.md  +  inside_bar_scans/inside_bar_scans_YYYY-MM-DD.md
"""

import sys
import os
import csv
from datetime import datetime

import pandas as pd
from tradingview_screener import Query, col

from ohlc_db import load_ohlc

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "inside_bar_scans")
TODAY = datetime.now().strftime("%Y-%m-%d")
MD_FILE = os.path.join(SCANS_DIR, "inside_bar_scans.md")

MC_LOW = 800 * 1_00_00_000  # ₹800 Cr
MC_HIGH = 1_00_000 * 1_00_00_000  # ₹1 Lakh Cr
LOOKBACK = 20  # max bars to look back for a mother bar
MIN_INSIDE = 2  # minimum inside bars required


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
        return {}
    try:
        latest: dict[str, dict] = {}
        with open(nse_csv, encoding="utf-8-sig") as fh:
            for raw in csv.DictReader(fh):
                row = {k.strip(): v.strip() for k, v in raw.items()}
                sym, dte = row.get("SYMBOL", ""), row.get("EFFECTIVE DATE", "")
                frm, to = row.get("FROM", ""), row.get("TO", "")
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


# ── Core algorithm ─────────────────────────────────────────────────────────────
def find_coil(df: pd.DataFrame) -> dict | None:
    """
    Find the longest active coil ending at today's bar.
    Scans inside_len from LOOKBACK down to MIN_INSIDE.
    Mother bar is at position -(inside_len+1); all bars since must be inside it.
    Returns the first (longest) match, or None.
    """
    n = len(df)
    for inside_len in range(min(LOOKBACK, n - 2), MIN_INSIDE - 1, -1):
        mother = df.iloc[-(inside_len + 1)]
        mb_high = float(mother["high"])
        mb_low = float(mother["low"])
        inside = df.iloc[-inside_len:]
        if (inside["high"] <= mb_high).all() and (inside["low"] >= mb_low).all():
            return {
                "inside_len": inside_len,
                "mb_high": mb_high,
                "mb_low": mb_low,
                "mb_date": str(mother["date"])[:10],
                "coil_width_pct": round((mb_high - mb_low) / mb_low * 100, 2),
            }
    return None


# ── Per-symbol analysis ────────────────────────────────────────────────────────
def analyse(symbol: str) -> dict | None:
    df = load_ohlc(symbol, lookback=LOOKBACK + 10)
    if df is None or len(df) < MIN_INSIDE + 3:
        return None

    coil = find_coil(df)
    if coil is None:
        return None

    close = float(df["close"].iloc[-1])
    prev = float(df["close"].iloc[-2])
    day_chg = round((close / prev - 1) * 100, 2)

    return {
        "symbol": symbol,
        "close": close,
        "day_chg": day_chg,
        "inside_len": coil["inside_len"],
        "mb_high": coil["mb_high"],
        "mb_low": coil["mb_low"],
        "mb_date": coil["mb_date"],
        "coil_width_pct": coil["coil_width_pct"],
    }


# ── Output ─────────────────────────────────────────────────────────────────────
def _sort_key(f: dict) -> tuple:
    return (-f["inside_len"], f["coil_width_pct"])


def _static_header() -> str:
    return f"""### Scan definition
| Filter | Value |
|--------|-------|
| Exchange | NSE common equity |
| Price | > ₹50 |
| Market cap | ₹800 Cr – ₹1 Lakh Cr |
| Lookback | Last {LOOKBACK} bars |
| Signal | All bars since mother bar are inside its high/low range |
| Min inside bars | {MIN_INSIDE} |
| Inside Bars | Consecutive bars the stock has been coiling |
| Coil Width% | (Mother high − low) / low × 100 — tighter = more compressed |

---
"""


def build_markdown(findings: list[dict], circuit: dict[str, tuple]) -> str:
    sorted_f = sorted(findings, key=_sort_key)

    hdr = [
        "| Symbol | Close | Day Chg% | Inside Bars | MB High | MB Low | Coil Width% | Circuit |",
        "|--------|------:|---------:|:-----------:|--------:|-------:|:-----------:|:-------:|",
    ]
    rows = []
    for f in sorted_f:
        cl, em = circuit.get(f["symbol"], ("20%", ""))
        tv = f"https://in.tradingview.com/chart/?symbol=NSE:{f['symbol']}"
        ds = "+" if f["day_chg"] >= 0 else ""
        rows.append(
            f"| [{f['symbol']}]({tv}) "
            f"| {f['close']:.2f} "
            f"| {ds}{f['day_chg']:.2f}% "
            f"| {f['inside_len']}d "
            f"| {f['mb_high']:.2f} "
            f"| {f['mb_low']:.2f} "
            f"| {f['coil_width_pct']:.2f}% "
            f"| {cl} {em} |"
        )

    lines = [
        f"# NSE Inside Bar / Mini Coil Scan — {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        _static_header(),
        f"**{len(findings)} stocks in Inside Bar / Mini Coil**",
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
    print(
        f"  NSE Inside Bar / Mini Coil Scanner  |  {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    )
    print(f"  Signals: {len(findings)}")
    print(f"{'='*75}")
    for f in sorted_f:
        ds = "+" if f["day_chg"] >= 0 else ""
        print(
            f"  {f['symbol']:<18}  {f['close']:>9.2f}  "
            f"day:{ds}{f['day_chg']:.1f}%  "
            f"inside:{f['inside_len']}d  "
            f"width:{f['coil_width_pct']:.2f}%  "
            f"MB:{f['mb_high']:.2f}/{f['mb_low']:.2f}  "
            f"since:{f['mb_date']}"
        )
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

    dated_file = os.path.join(SCANS_DIR, f"inside_bar_scans_{TODAY}.md")
    md = build_markdown(findings, circuit)
    with open(MD_FILE, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(dated_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  Saved -> {MD_FILE}")
    print(f"  Saved -> {dated_file}")


if __name__ == "__main__":
    main()
