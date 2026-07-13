#!/usr/bin/env python3
"""
NSE Weekly RS EMA9 Trend Scanner — trending universe
Stocks where the weekly RS Line (stock / NIFTY MIDSML 400) is currently above its
weekly EMA9, and that EMA9 is flat or rising (current partial week included, per
to_weekly convention).

Trend condition: weekly RS EMA9 this week >= last week (flat or rising kept, falling excluded)
Above condition: today's daily RS Line > this week's weekly RS EMA9

Age = consecutive trading days daily RS Line has stayed above the weekly RS EMA9
(walks back from today, resets on any day it dipped below).

New entrants = symbols in today's output that weren't in the previous run's output
(state persisted in rs_weekly_ema9_state.json, mirrors nse_ema_daily.py's diff pattern).

Watchlist: NSE common equity, price > Rs50, MCap Rs800 Cr - Rs1 Lakh Cr
(mirrors weekly_zl_scanner.py)

Output: rs_weekly_scans/rs_weekly_ema9_scans.md + rs_weekly_ema9_scans_YYYY-MM-DD.md
sorted by age ascending (newest entries into the trend first).
"""

import sys
import os
import csv
import json
from datetime import datetime

import pandas as pd
from tradingview_screener import Query, col

from ohlc_db import load_ohlc, load_ohlc_many, get_names, liq_tag
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "rs_weekly_scans")
TODAY = datetime.now().strftime("%Y-%m-%d")
MD_FILE = os.path.join(SCANS_DIR, "rs_weekly_ema9_scans.md")
STATE_FILE = os.path.join(SCANS_DIR, "rs_weekly_ema9_state.json")

MC_LOW = 800 * 1_00_00_000  # Rs800 Cr
MC_HIGH = 1_00_000 * 1_00_00_000  # Rs1 Lakh Cr
BENCH_SYM = "NIFTY MIDSML 400"
SLOPE_EPS = 1e-6  # ponytail: avoids float == 0.0 for "flat" classification


def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def weekly_rs_ema9_trend(stock_close: pd.Series, bench_close: pd.Series) -> dict | None:
    """Pure function: weekly RS = stock/bench * 1000, EMA9 of that, slope of last two
    weekly bars, and age = consecutive trading days daily RS has stayed above the
    (daily-forward-filled) weekly EMA9. Returns None if not enough overlapping history,
    else {"rs_ema9": float, "slope": float, "rising": bool, "age": int}."""
    bench = bench_close.reindex(stock_close.index)
    valid = bench.notna() & stock_close.notna()
    if valid.sum() < 70:
        return None
    c_rs, idx_rs = stock_close[valid], bench[valid]
    c_rs.index = pd.to_datetime(c_rs.index)
    idx_rs.index = pd.to_datetime(idx_rs.index)
    daily_rs = (c_rs / idx_rs) * 1000
    wk_c = c_rs.resample("W").last().dropna()
    wk_idx = idx_rs.resample("W").last().dropna()
    common = wk_c.index.intersection(wk_idx.index)
    if len(common) < 10:
        return None
    wk_rs = (wk_c.loc[common] / wk_idx.loc[common]) * 1000
    rs_ema9 = ema(wk_rs, 9)
    if len(rs_ema9) < 2:
        return None
    slope = float(rs_ema9.iloc[-1] - rs_ema9.iloc[-2])

    wk_ema9_daily = rs_ema9.reindex(daily_rs.index, method="ffill")
    above = (daily_rs > wk_ema9_daily) & wk_ema9_daily.notna()
    age = 0
    for v in reversed(above.values):
        if not v:
            break
        age += 1

    return {
        "rs_ema9": float(rs_ema9.iloc[-1]),
        "slope": slope,
        "rising": slope > SLOPE_EPS,
        "age": age,
    }


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


# ── Circuit limits (duplicated from weekly_zl_scanner.py — each scanner is
#    independently runnable, matches existing per-file convention) ─────────────
_CIRCUIT_EMOJI = {
    ("20", "10"): "\U0001f7e8",
    ("10", "5"): "\U0001f7e5",
    ("5", "10"): "\U0001f7e9",
    ("10", "20"): "\U0001f7e6",
}
_NSE_CSV_PATHS = [
    os.path.join(REPO_DIR, "nse.csv"),
    r"C:\Users\satya\.gemini\antigravity\scratch\circuit_dashboard\nse.csv",
]


def get_circuit_limits() -> dict[str, tuple]:
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


# ── Previous-run state (new-entrant diff, mirrors nse_ema_daily.py) ─────────────
def load_previous() -> set:
    if not os.path.exists(STATE_FILE):
        return set()
    try:
        with open(STATE_FILE, encoding="utf-8") as f:
            return set(json.load(f))
    except Exception:
        return set()


def save_current(symbols: list[str]) -> None:
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted(symbols), f, indent=2)


# ── Stock analysis ──────────────────────────────────────────────────────────
def analyse(symbol: str, bench_close: pd.Series) -> dict | None:
    try:
        daily = load_ohlc(symbol, lookback=400)
        if daily is None or len(daily) < 60:
            return None
        stock_close = daily.set_index("date")["close"].astype(float)
        trend = weekly_rs_ema9_trend(stock_close, bench_close)
        # Trending universe: currently above weekly RS EMA9 AND that EMA9 flat/rising
        if trend is None or trend["slope"] < -SLOPE_EPS or trend["age"] < 1:
            return None

        c = daily["close"].astype(float)
        curr_close = float(c.iloc[-1])
        day_chg = (curr_close / c.iloc[-2] - 1) * 100 if len(c) >= 2 else 0.0

        return {
            "symbol": symbol,
            "close": curr_close,
            "day_chg": day_chg,
            "rs_ema9": trend["rs_ema9"],
            "slope": trend["slope"],
            "rising": trend["rising"],
            "age": trend["age"],
            "liq_tag": liq_tag(daily),
        }
    except Exception:
        return None


# ── Output ───────────────────────────────────────────────────────────────────
def build_markdown(findings: list[dict], circuit: dict, names: dict | None = None) -> str:
    sorted_f = sorted(findings, key=lambda f: f["age"])
    new_f = [f for f in sorted_f if f.get("new_entrant")]
    lines = [
        f"# NSE Weekly RS EMA9 Trend Scan — {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        "### Scan definition",
        "| Filter | Value |",
        "|--------|-------|",
        "| Exchange | NSE common equity |",
        "| Price | > Rs50 |",
        "| Market cap | Rs800 Cr - Rs1 Lakh Cr |",
        "| Timeframe | Weekly (daily OHLC resampled; current partial week included) |",
        "| Trend condition | Daily RS Line above weekly RS EMA9 AND that EMA9 flat or rising vs last week |",
        "| RS Line | (stock_close / NIFTY MIDSML 400 close) x 1000 |",
        "| Age | Consecutive trading days RS Line has stayed above the weekly RS EMA9 |",
        "| New | Not present in the previous run's output |",
        "| Sort | Age ascending — newest entries into the trend first |",
        "",
        "---",
        "",
        f"**{len(sorted_f)} stock{'s' if len(sorted_f) != 1 else ''} in trend** "
        f"&nbsp;|&nbsp; **{len(new_f)} new entrant{'s' if len(new_f) != 1 else ''}**",
        "",
        "```",
        ",".join(f"NSE:{f['symbol']}" for f in sorted_f),
        "```",
        "",
    ]
    if new_f:
        lines += [
            f"**New today:** {', '.join(f['symbol'] for f in new_f)}",
            "",
        ]
    if sorted_f:
        lines += [
            "| Symbol | New | Age(d) | Trend | RS EMA9 | Day Chg | Close | Circuit |",
            "|--------|:---:|-------:|:-----:|--------:|--------:|------:|:-------:|",
        ]
        for f in sorted_f:
            sym = f["symbol"]
            cl, em = circuit.get(sym, ("20%", ""))
            tv = f"https://in.tradingview.com/chart/?symbol=NSE:{sym}"
            name_cell = (names or {}).get(sym, "")
            sym_cell = f"[{sym}]({tv})" + (f"<br><sub>{name_cell}</sub>" if name_cell else "")
            trend_tag = "↑ RISING" if f["rising"] else "→ FLAT"
            new_tag = "NEW" if f.get("new_entrant") else ""
            ds = "+" if f["day_chg"] >= 0 else ""
            lines.append(
                f"| {sym_cell} "
                f"| {new_tag} "
                f"| {f['age']}d "
                f"| {trend_tag} "
                f"| {f['rs_ema9']:.2f} "
                f"| {ds}{f['day_chg']:.2f}% "
                f"| {f['close']:.2f} "
                f"| {cl} {em} |"
            )
        lines += ["", "```", ",".join(f"NSE:{f['symbol']}" for f in sorted_f), "```"]
    else:
        lines.append("*No signals.*")

    lines.append("")
    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


def main():
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nFetching NSE circuit limits...")
    circuit = get_circuit_limits()

    print("Fetching live watchlist from TradingView screener...")
    watchlist = get_watchlist()
    print(f"  Watchlist: {len(watchlist)} stocks")

    print(f"Loading benchmark ({BENCH_SYM}) from SQLite...")
    bench_dict = load_ohlc_many([BENCH_SYM], lookback=400)
    bench_df = bench_dict.get(BENCH_SYM)
    if bench_df is None or bench_df.empty:
        print(f"  WARNING: {BENCH_SYM} not in SQLite — aborting")
        return
    bench_close = bench_df.set_index("date")["close"].astype(float)

    previous_syms = load_previous()

    findings = []
    for i, sym in enumerate(watchlist, 1):
        print(f"  {sym:<20} ({i}/{len(watchlist)})   ", end="\r")
        result = analyse(sym, bench_close)
        if result:
            findings.append(result)
    for f in findings:
        f["new_entrant"] = f["symbol"] not in previous_syms
    new_count = sum(1 for f in findings if f["new_entrant"])
    print(f"\n  {len(findings)} stocks trending  |  {new_count} new entrants")

    dated_file = os.path.join(SCANS_DIR, f"rs_weekly_ema9_scans_{TODAY}.md")
    names = get_names([f["symbol"] for f in findings])
    md = build_markdown(findings, circuit, names)
    with open(MD_FILE, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(dated_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    save_current([f["symbol"] for f in findings])
    print(f"  Saved -> {MD_FILE}")
    print(f"  Saved -> {dated_file}")


if __name__ == "__main__":
    main()
