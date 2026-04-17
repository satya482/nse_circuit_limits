#!/usr/bin/env python3
"""
NSE Swing Trading Scanner
Run after 4:05 PM IST on trading days.

Entry conditions:
  STRONG       – ZLEMA25 rising + price touched ZLEMA25 + EMA20 rising
  PRIMARY      – ZLEMA25 rising + price touched ZLEMA25
  DEEP PULLBACK– ZLEMA25 rising + price touched EMA50/100/200 and bounced green

Output: swing_scans/YYYY-MM-DD.md  (committed and pushed to GitHub automatically)
"""

import sys
import os
import subprocess
from datetime import datetime
import yfinance as yf
import pandas as pd
from tradingview_screener import Query, col

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR   = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR  = os.path.join(REPO_DIR, "swing_scans")
TODAY      = datetime.now().strftime("%Y-%m-%d")
MD_FILE    = os.path.join(SCANS_DIR, f"{TODAY}.md")

MC_LOW     = 800     * 1_00_00_000
MC_HIGH    = 1_00_000 * 1_00_00_000
TOUCH_PCT  = 0.015


# ── Indicators ────────────────────────────────────────────────────────────────
def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()

def zlema(s: pd.Series, n: int) -> pd.Series:
    e = ema(s, n)
    return 2 * e - ema(e, n)


# ── Watchlist ─────────────────────────────────────────────────────────────────
def get_watchlist() -> list[str]:
    _, df = (
        Query()
        .set_markets("india")
        .select("name", "EMA50", "EMA100", "EMA200")
        .where(
            col("exchange") == "NSE",
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("EMA50")  > col("EMA200"),
            col("EMA100") > col("EMA200"),
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
        )
        .limit(500)
        .get_scanner_data()
    )
    return df["name"].tolist()


# ── Stock analysis ────────────────────────────────────────────────────────────
def analyse(symbol: str) -> dict | None:
    try:
        df = yf.Ticker(f"{symbol}.NS").history(period="2y")
        if len(df) < 210:
            return None

        c  = df["Close"]
        lo = df["Low"]
        op = df["Open"]

        e20  = ema(c, 20)
        e50  = ema(c, 50)
        e100 = ema(c, 100)
        e200 = ema(c, 200)
        zl25 = zlema(c, 25)

        if not (e50.iloc[-1] > e200.iloc[-1] and e100.iloc[-1] > e200.iloc[-1]):
            return None

        zl_now, zl_prev   = zl25.iloc[-1], zl25.iloc[-2]
        e20_now, e20_prev = e20.iloc[-1],  e20.iloc[-2]
        curr_close = c.iloc[-1]
        prev_close = c.iloc[-2]
        curr_low   = lo.iloc[-1]
        curr_open  = op.iloc[-1]

        zl_rising  = zl_now > zl_prev
        e20_rising = e20_now > e20_prev

        if not zl_rising:
            return None

        entries = []

        # Primary / Strong: price touching ZLEMA25 during pullback
        was_above = prev_close > zl_prev
        touched_zl = (
            curr_low <= zl_now * (1 + TOUCH_PCT)
            and curr_low >= zl_now * (1 - TOUCH_PCT)
        ) or (curr_low <= zl_now and curr_close >= zl_now)

        if was_above and touched_zl:
            tag = "STRONG" if e20_rising else "PRIMARY"
            label = "ZLEMA25 touch + EMA20 rising" if e20_rising else "ZLEMA25 touch"
            entries.append((tag, label, zl_now))

        # Deep pullback: bouncing from EMA50 / EMA100 / EMA200
        for level, name in [
            (e50.iloc[-1],  "EMA50"),
            (e100.iloc[-1], "EMA100"),
            (e200.iloc[-1], "EMA200"),
        ]:
            touched = curr_low <= level * (1 + TOUCH_PCT)
            bounced = curr_close > level and curr_close > curr_open
            if touched and bounced:
                entries.append(("DEEP PULLBACK", f"Bounce from {name}", level))

        if not entries:
            return None

        day_chg = (curr_close - prev_close) / prev_close * 100

        return {
            "symbol":  symbol,
            "close":   curr_close,
            "day_chg": day_chg,
            "zlema25": zl_now,
            "ema20":   e20_now,
            "ema50":   e50.iloc[-1],
            "ema100":  e100.iloc[-1],
            "ema200":  e200.iloc[-1],
            "entries": entries,
        }

    except Exception:
        return None


# ── Markdown output ───────────────────────────────────────────────────────────
TAG_ORDER = {"STRONG": 0, "PRIMARY": 1, "DEEP PULLBACK": 2}

def build_markdown(findings: list[dict]) -> str:
    findings.sort(key=lambda x: min(TAG_ORDER.get(e[0], 9) for e in x["entries"]))

    lines = [
        f"# NSE Swing Scan — {TODAY}",
        f"\n**Entry Opportunities: {len(findings)}**\n",
        "| Symbol | Signal | Level (Rs.) | Level vs Close | Day Change |",
        "|--------|--------|------------:|:--------------:|-----------:|",
    ]

    for f in findings:
        for tag, label, level in f["entries"]:
            vs_close = (f["close"] - level) / level * 100
            day_sign = "+" if f["day_chg"] >= 0 else ""
            lvl_sign = "+" if vs_close >= 0 else ""
            lines.append(
                f"| {f['symbol']} | **{tag}** — {label} "
                f"| {level:.2f} "
                f"| {lvl_sign}{vs_close:.1f}% "
                f"| {day_sign}{f['day_chg']:.2f}% |"
            )

    lines += [
        "",
        "---",
        "",
        "### Signal definitions",
        "| Signal | Condition |",
        "|--------|-----------|",
        "| **STRONG** | ZLEMA25 rising · price touched ZLEMA25 · EMA20 rising |",
        "| **PRIMARY** | ZLEMA25 rising · price touched ZLEMA25 |",
        "| **DEEP PULLBACK** | ZLEMA25 rising · low touched EMA50/100/200 · closed green above it |",
        "",
        f"*Generated at {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
    ]

    return "\n".join(lines)


# ── Console output ────────────────────────────────────────────────────────────
def print_results(findings: list[dict]) -> None:
    print(f"\n{'='*65}")
    print(f"  NSE Swing Scanner  |  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Entry Opportunities: {len(findings)}")
    print(f"{'='*65}")

    if not findings:
        print("  No entry setups found today.")
        return

    for f in findings:
        day_sign = "+" if f["day_chg"] >= 0 else ""
        print(f"\n  {f['symbol']:<15}  Close: {f['close']:>8.2f}  ({day_sign}{f['day_chg']:.2f}% day)")
        for tag, label, level in f["entries"]:
            vs = (f["close"] - level) / level * 100
            print(f"    [{tag}]  {label}")
            print(f"             Level {level:.2f}  ({vs:+.1f}% from close)")
        print(f"    EMAs  20={f['ema20']:.1f}  50={f['ema50']:.1f}  "
              f"100={f['ema100']:.1f}  200={f['ema200']:.1f}  ZLEMA25={f['zlema25']:.1f}")
        print("    " + "─" * 55)


# ── Git push ──────────────────────────────────────────────────────────────────
def git_commit_push(md_path: str) -> None:
    rel = os.path.relpath(md_path, REPO_DIR)
    cmds = [
        ["git", "-C", REPO_DIR, "add", rel],
        ["git", "-C", REPO_DIR, "commit", "-m", f"swing scan {TODAY}"],
        ["git", "-C", REPO_DIR, "push"],
    ]
    for cmd in cmds:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0 and "nothing to commit" not in result.stdout:
            print(f"  git warning: {result.stderr.strip()}")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("\nFetching live watchlist from TradingView screener...")
    watchlist = get_watchlist()
    print(f"Watchlist: {len(watchlist)} stocks  |  Scanning...\n")

    findings = []
    for i, sym in enumerate(watchlist, 1):
        print(f"  {sym:<20} ({i}/{len(watchlist)})   ", end="\r")
        result = analyse(sym)
        if result:
            findings.append(result)

    print_results(findings)

    os.makedirs(SCANS_DIR, exist_ok=True)
    md = build_markdown(findings)
    with open(MD_FILE, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"\n  Saved -> {MD_FILE}")

    print("  Committing and pushing to GitHub...")
    git_commit_push(MD_FILE)
    print("  Done.")


if __name__ == "__main__":
    main()
