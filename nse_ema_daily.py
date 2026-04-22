#!/usr/bin/env python3
"""
NSE EMA Screener — daily change tracker.
Criteria : EMA50 > EMA100  AND  EMA100 > EMA200  (full bullish stack)
MCap     : ₹800 Cr – ₹1 Lakh Cr (NSE common equity only)
Output   : ema_screener_changes.md  +  nse_ema_results.json  (state file)
"""

from tradingview_screener import Query, col
from datetime import datetime, timezone, timedelta
import json, os

IST        = timezone(timedelta(hours=5, minutes=30))
DATA_FILE  = "nse_ema_results.json"
MD_FILE    = "ema_screener_changes.md"
MC_LOW     = 800     * 1_00_00_000   # ₹800 Crore  in INR
MC_HIGH    = 1_00_000 * 1_00_00_000  # ₹1 Lakh Crore in INR


def fetch() -> dict[str, float]:
    """Return {symbol: day_change_pct} for stocks passing all criteria."""
    _, df = (
        Query()
        .set_markets("india")
        .select("name", "close", "change")
        .where(
            col("exchange") == "NSE",
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("EMA50")  > col("EMA100"),
            col("EMA100") > col("EMA200"),
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
        )
        .limit(500)
        .get_scanner_data()
    )
    return {row["name"]: round(float(row["change"]), 2) for _, row in df.iterrows()}


def load_previous() -> dict[str, float]:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return {}


def save_current(data: dict) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)


def pct_str(v: float) -> str:
    return f"+{v:.2f}%" if v >= 0 else f"{v:.2f}%"


def build_md(current: dict, previous: dict, today: str) -> str:
    curr_set = set(current)
    prev_set = set(previous)
    additions = sorted(curr_set - prev_set, key=lambda s: current[s],  reverse=True)
    deletions = sorted(prev_set - curr_set, key=lambda s: previous[s], reverse=True)

    lines = [
        f"# NSE EMA Screener — {today}",
        "",
        "_Criteria: EMA50 > EMA100 > EMA200 (full bullish stack) | MCap ₹800 Cr – ₹1 Lakh Cr_",
        "",
        f"**Total stocks in list: {len(current)}** &nbsp;|&nbsp; "
        f"**Additions: {len(additions)}** &nbsp;|&nbsp; "
        f"**Deletions: {len(deletions)}**",
        "",
    ]

    # ── Additions ──────────────────────────────────────────────────────────────
    lines.append(f"## ✅ Additions ({len(additions)})")
    if additions:
        lines += ["| Symbol | Day Change % |", "|--------|:------------:|"]
        for s in additions:
            tv = f"https://in.tradingview.com/chart/?symbol=NSE:{s}"
            lines.append(f"| [{s}]({tv}) | {pct_str(current[s])} |")
    else:
        lines.append("_No new entries today_")
    lines.append("")

    # ── Deletions ──────────────────────────────────────────────────────────────
    lines.append(f"## ❌ Deletions ({len(deletions)})")
    if deletions:
        lines += ["| Symbol | Last Day Change % |", "|--------|:----------------:|"]
        for s in deletions:
            tv = f"https://in.tradingview.com/chart/?symbol=NSE:{s}"
            lines.append(f"| [{s}]({tv}) | {pct_str(previous.get(s, 0.0))} |")
    else:
        lines.append("_No exits today_")
    lines.append("")

    # ── Full current list ──────────────────────────────────────────────────────
    all_stocks = sorted(current, key=lambda s: current[s], reverse=True)
    lines.append(f"## 📋 Full List ({len(all_stocks)})")
    if all_stocks:
        lines += ["| # | Symbol | Day Change % |", "|---|--------|:------------:|"]
        for i, s in enumerate(all_stocks, 1):
            tv = f"https://in.tradingview.com/chart/?symbol=NSE:{s}"
            lines.append(f"| {i} | [{s}]({tv}) | {pct_str(current[s])} |")
    else:
        lines.append("_No stocks currently in list_")
    lines.append("")

    lines += ["---", f"_Updated: {today} 16:00 IST by GitHub Actions_"]
    return "\n".join(lines) + "\n"


def main():
    now_ist = datetime.now(IST)
    today   = now_ist.strftime("%Y-%m-%d")

    print(f"[{now_ist.strftime('%Y-%m-%d %H:%M IST')}] Fetching screener data…")
    current  = fetch()
    previous = load_previous()

    md = build_md(current, previous, today)
    with open(MD_FILE, "w", encoding="utf-8") as f:
        f.write(md)

    save_current(current)

    additions = len(set(current) - set(previous))
    deletions = len(set(previous) - set(current))
    print(f"Done — {len(current)} stocks total | +{additions} additions | -{deletions} deletions")
    print(f"Written: {MD_FILE}, {DATA_FILE}")


if __name__ == "__main__":
    main()
