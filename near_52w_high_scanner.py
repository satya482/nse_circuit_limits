#!/usr/bin/env python3
"""
NSE Near-52W-High Scanner
Run after 4:20 PM IST on trading days (after run_fetch_data.ps1 completes).

Watchlist filters (TradingView, reused from ema25_zl_scanner.py):
  - NSE common equity, price > 50 INR, market cap 1,000 Cr - 5 Lakh Cr

Signal (single combined gate, no union confluence):
  - close within 30% below the rolling 260-day high (52w high, computed off
    the `high` column -- matches pine_scripts/52w_full_history.pine's
    ta.highest(high,260)), AND close > EMA200
  - rows sitting at/above that 52w high (pct_from_high ~ 0, within
    NEW_HIGH_EPS) are tagged as a new/at 52w high, not filtered separately --
    they're a boundary case of the same band, not an independent criterion

Data source: .ohlc_data/market.db  (populated by fetch_data.py)
Output:      near_52w_high_scans/near_52w_high_scans.md
"""

import sys
import os
from datetime import datetime

import pandas as pd

import ema25_zl_scanner as base
from ohlc_db import load_ohlc, liq_tag, cmf_tag, deliv_tag
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER
from float_gate import float_metrics, passes_hard_gate, trap_label
from tv_watchlist import tv_csv, tv_csv_flat, tv_top_sections

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "near_52w_high_scans")
TODAY = datetime.now().strftime("%Y-%m-%d")
MD_FILE = os.path.join(SCANS_DIR, "near_52w_high_scans.md")

HIGH52W_PERIOD = 260  # daily bars, matches pine's auto-bars daily=260
EMA_PERIOD = 200
BAND_PCT = -30.0  # gate: pct_from_high in [BAND_PCT, 0]
NEW_HIGH_EPS = 0.01
MIN_BARS = 260

_PCT_BUCKETS_ORDER = ["AT/NEW HIGH", "0-10%", "10-20%", "20-30%"]


def high52w_stats(high: pd.Series, close: pd.Series, period: int = HIGH52W_PERIOD) -> tuple[float, float]:
    """Returns (high_52w, pct_from_high) using the latest `period` bars.
    high_52w = rolling max of `high` (not close) -- parity with the pine
    script's ta.highest(high, 260). pct_from_high is always <=0 by
    construction (today's high feeds its own rolling max)."""
    high_52w = high.rolling(period).max().iloc[-1]
    pct_from_high = (close.iloc[-1] - high_52w) / high_52w * 100
    return high_52w, pct_from_high


def is_new_high(pct_from_high: float) -> bool:
    return abs(pct_from_high) < NEW_HIGH_EPS


def passes_gate(pct_from_high: float, close: float, ema200: float) -> bool:
    return BAND_PCT <= pct_from_high <= 0 and close > ema200


def bucket_for(pct_from_high: float) -> str:
    if is_new_high(pct_from_high):
        return "AT/NEW HIGH"
    if pct_from_high >= -10.0:
        return "0-10%"
    if pct_from_high >= -20.0:
        return "10-20%"
    return "20-30%"


def analyse(symbol: str, float_shares: float = 0) -> dict | None:
    try:
        raw = load_ohlc(symbol)
        if raw is None or len(raw) < MIN_BARS:
            return None

        fm = float_metrics(raw["close"], raw["volume"], float_shares or None)
        if not passes_hard_gate(fm):
            return None

        high = raw["high"].astype(float)
        close = raw["close"].astype(float)
        ema200 = base.ema(close, EMA_PERIOD).iloc[-1]

        high_52w, pct_from_high = high52w_stats(high, close)
        if not passes_gate(pct_from_high, close.iloc[-1], ema200):
            return None

        curr_close = close.iloc[-1]
        prev_close = close.iloc[-2]
        day_chg = (curr_close - prev_close) / prev_close * 100

        return {
            "symbol": symbol,
            "close": curr_close,
            "day_chg": day_chg,
            "high_52w": round(high_52w, 2),
            "pct_from_high": round(pct_from_high, 2),
            "ema200": round(ema200, 2),
            "new_high": is_new_high(pct_from_high),
            "bucket": bucket_for(pct_from_high),
            "trap": trap_label(fm),
            "liq_tag": liq_tag(raw),
            "cmf_tag": cmf_tag(raw),
            "deliv_tag": deliv_tag(symbol),
        }
    except Exception:
        return None


# -- Markdown -----------------------------------------------------------------
STATIC_HEADER = f"""### Scan definition
| Filter | Value |
|--------|-------|
| Exchange | NSE common equity |
| Price | > Rs50 |
| Market cap | Rs1,000 Cr - Rs5 Lakh Cr |
| Signal | Close within {BAND_PCT:.0f}% to 0% of rolling {HIGH52W_PERIOD}-bar (52w) high, AND close > EMA{EMA_PERIOD} |
| 52w High | Rolling max of daily HIGH over {HIGH52W_PERIOD} bars (pine parity: ta.highest(high,{HIGH52W_PERIOD})) |
| At/New High | Rows within {NEW_HIGH_EPS}% of the 52w high are tagged, not filtered separately |
| Float gate | AVOID dropped from scan; SAFE / CAUTION shown under symbol (float_gate.py) |
| Symbol tags | trap - liq (avg10Cr-todayCr) - CMF - DEL% |

---
"""


def _table_rows(findings: list[dict], circuit: dict[str, tuple]) -> list[str]:
    rows = []
    for f in findings:
        sym = f["symbol"]
        cl, em = circuit.get(sym, ("20%", ""))
        tv = f"https://in.tradingview.com/chart/?symbol=NSE:{sym}"
        pct = f["pct_from_high"]
        pct_text = ("+" if pct >= 0 else "") + f"{pct:.2f}%"
        ds = "+" if f["day_chg"] >= 0 else ""
        extras = []
        trap = f.get("trap", "")
        if trap and trap != "n/a":
            extras.append(trap)
        if f.get("liq_tag"):
            extras.append(f["liq_tag"])
        if f.get("cmf_tag"):
            extras.append(f["cmf_tag"])
        if f.get("deliv_tag"):
            extras.append(f["deliv_tag"])
        marker = "\U0001F3AF " if f["new_high"] else ""
        sym_cell = f"{marker}[{sym}]({tv})" + (f"<br><sub>{' - '.join(extras)}</sub>" if extras else "")
        rows.append(
            f"| {sym_cell} "
            f"| {pct_text} "
            f"| {f['close']:.2f} "
            f"| {f['high_52w']:.2f} "
            f"| {f['ema200']:.2f} "
            f"| {ds}{f['day_chg']:.2f}% "
            f"| {cl} {em} |"
        )
    return rows


def build_markdown(findings: list[dict], circuit: dict[str, tuple]) -> str:
    rows = sorted(findings, key=lambda x: (-x["pct_from_high"], x["symbol"]))

    hdr = [
        "| Symbol | %From 52wHigh | Close | 52w High | EMA200 | Day Chg | Circuit |",
        "|--------|--------------:|------:|---------:|-------:|--------:|:-------:|",
    ]

    wl_parts = []
    for label in _PCT_BUCKETS_ORDER:
        syms = [f["symbol"] for f in rows if f["bucket"] == label]
        if syms:
            wl_parts.append(f"###{label}," + tv_csv_flat(f"NSE:{s}" for s in syms))

    lines = [
        f"# NSE Near-52W-High Watchlist - {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        STATIC_HEADER,
        f"**On watch: {len(rows)}**",
        "",
        "**TradingView watchlist** *(sectioned by distance from 52w high - paste into TV import)*",
        "```",
        ",".join(tv_top_sections() + wl_parts),
        "```",
        "",
        "### Near-52W-High Watchlist",
    ]
    if rows:
        lines += [
            "*(\U0001F3AF marks stocks at/making a new 52w high)*",
            "",
        ]
        lines += hdr + _table_rows(rows, circuit)
        lines += ["", "```", tv_csv(f"NSE:{f['symbol']}" for f in rows), "```"]
    else:
        lines.append("*No signals.*")

    lines += ["", "### TradingView Watchlists *(by distance from 52w high)*"]
    for label in _PCT_BUCKETS_ORDER:
        syms = [f["symbol"] for f in rows if f["bucket"] == label]
        if not syms:
            continue
        lines += [
            "",
            f"**{label}** ({len(syms)})",
            "```",
            tv_csv(f"NSE:{s}" for s in syms),
            "```",
        ]

    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


# -- Main -----------------------------------------------------------------------
def main():
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nFetching NSE circuit limits...")
    circuit = base.get_circuit_limits()
    print(f"  Circuit data: {len(circuit)} stocks with recent limit changes")

    print("\nFetching live watchlist from TradingView screener...")
    watchlist, float_map = base.get_watchlist()
    print(
        f"  Watchlist: {len(watchlist)} stocks  |  float data for {len(float_map)}  |  Scanning...\n"
    )

    findings = []
    for i, sym in enumerate(watchlist, 1):
        print(f"  {sym:<20} ({i}/{len(watchlist)})   ", end="\r")
        result = analyse(sym, float_shares=float_map.get(sym, 0))
        if result:
            findings.append(result)

    print(f"\n  On watch: {len(findings)}")

    dated_file = os.path.join(SCANS_DIR, f"near_52w_high_scans_{TODAY}.md")
    md = build_markdown(findings, circuit)
    with open(MD_FILE, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(dated_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  Saved -> {MD_FILE}")
    print(f"  Saved -> {dated_file}")


if __name__ == "__main__":
    main()
