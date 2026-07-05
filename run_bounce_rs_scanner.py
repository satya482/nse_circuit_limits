#!/usr/bin/env python3
"""
Bounce-RS Scanner runner.
Builds a liquid NSE watchlist, calls scanners.bounce_rs_scanner.run(), writes markdown.

Watchlist: NSE common equity, MCap ₹800 Cr – ₹1 Lakh Cr (same filter as inside_bar_scanner.py)
Output:    bounce_rs_scans/bounce_rs_scan_latest.md + bounce_rs_scan_YYYY-MM-DD.md
"""

import os
import sys
from datetime import datetime, timezone, timedelta

import pandas as pd
from tradingview_screener import Query, col

from scanners.bounce_rs_scanner import run
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER

sys.stdout.reconfigure(encoding="utf-8")

IST = timezone(timedelta(hours=5, minutes=30))
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "bounce_rs_scans")

MC_LOW = 800 * 1_00_00_000  # ₹800 Cr
MC_HIGH = 1_00_000 * 1_00_00_000  # ₹1 Lakh Cr


def get_watchlist() -> list[str]:
    _, df = (
        Query()
        .set_markets("india")
        .select("name", "close")
        .where(
            col("exchange") == "NSE",
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
        )
        .limit(2000)
        .get_scanner_data()
    )
    return df["name"].tolist()


def build_markdown(result: pd.DataFrame, today: str, now_str: str) -> str:
    lines = [
        f"# Bounce-RS Scanner — {today}",
        f"*Generated {now_str}*",
        "",
    ]
    if result.empty:
        lines.append("*No signals.*")
    else:
        lines.append(
            "| Symbol | RS Dip% | EMA Type | Setup | Dip Low | Ratio Now | Bounce | Score |"
        )
        lines.append(
            "|--------|--------:|:--------:|-------|--------:|----------:|-------:|------:|"
        )
        for _, r in result.iterrows():
            tv = f"https://in.tradingview.com/chart/?symbol=NSE:{r['symbol']}"
            lines.append(
                f"| [{r['symbol']}]({tv}) "
                f"| {r['rs_during_dip_%']:.2f} "
                f"| {r['ema_type']} "
                f"| {r['setup']} "
                f"| {r['dip_low_ratio']:.2f} "
                f"| {r['ratio_5d_now']:.2f} "
                f"| {r['bounce_mag']:.2f} "
                f"| {r['score']:.2f} |"
            )
    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


def main():
    os.makedirs(SCANS_DIR, exist_ok=True)
    now_ist = datetime.now(IST)
    today = now_ist.strftime("%Y-%m-%d")
    now_str = now_ist.strftime("%Y-%m-%d %H:%M IST")

    print(f"[{now_str}] Bounce-RS Scanner — fetching watchlist...")
    watchlist = get_watchlist()
    print(f"  Watchlist: {len(watchlist)} stocks")

    universe_df = pd.DataFrame({"symbol": watchlist})
    result = run(universe_df, now_ist.date())
    print(f"  Signals: {len(result)}")

    md = build_markdown(result, today, now_str)
    latest_file = os.path.join(SCANS_DIR, "bounce_rs_scan_latest.md")
    dated_file = os.path.join(SCANS_DIR, f"bounce_rs_scan_{today}.md")
    with open(latest_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(dated_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  Saved -> {latest_file}")
    print(f"  Saved -> {dated_file}")


if __name__ == "__main__":
    main()
