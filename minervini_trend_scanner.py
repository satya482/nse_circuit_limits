#!/usr/bin/env python3
"""
Minervini Trend Template Scanner
Run in the 4:30 PM group, after the RS-gated scanners (shares their RS gate
function and benchmark load pattern).

Universe (reused from ema25_zl_scanner.py): NSE common equity,
MCap Rs 1,000 Cr - Rs 5 Lakh Cr, price > Rs 50, float hard-gate applied.

Strict AND-gate, all 9 checks must pass (Mark Minervini's Trend Template):
  1. close > SMA150
  2. close > SMA200
  3. SMA150 > SMA200
  4. SMA200 trending up >= 1 month (SMA200 today > SMA200 21 trading days ago)
  5. SMA50 > SMA150 and SMA50 > SMA200
  6. close > SMA50
  7. close >= 1.30 x 52-week low
  8. close >= 0.75 x 52-week high (within 25% of it)
  9. RS strength: daily RS line > weekly RS EMA9, weekly RS EMA9 rising
     (reused from ema25_zl_scanner._weekly_rs_gate() -- RS Rating proxy,
     see docs/superpowers/specs/2026-08-02-minervini-trend-template-scanner-design.md)

No partial-score output -- binary qualify list.

Data source: .ohlc_data/market.db (populated by fetch_data.py)
Output:      minervini_scans/minervini_trend_latest.md
             minervini_scans/minervini_trend_YYYY-MM-DD.md
"""

import sys
import os
from datetime import datetime

import pandas as pd

import ema25_zl_scanner as base
from ohlc_db import load_ohlc, load_ohlc_many, liq_tag, cmf_tag, deliv_tag
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER
from float_gate import float_metrics, passes_hard_gate, trap_label

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "minervini_scans")
TODAY = datetime.now().strftime("%Y-%m-%d")
MD_LATEST = os.path.join(SCANS_DIR, "minervini_trend_latest.md")
BENCH_SYM = "NIFTY MIDSML 400"
LOOKBACK_52WK = 252
MIN_BARS = 260  # 52wk window + buffer


# ── Trend template criteria ─────────────────────────────────────────────────
def sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def trend_template_checks(close: pd.Series) -> dict:
    """8 SMA/52wk checks (criterion 9 -- RS gate -- is separate, needs the
    benchmark series, see _weekly_rs_gate reuse in analyse())."""
    sma50 = sma(close, 50)
    sma150 = sma(close, 150)
    sma200 = sma(close, 200)
    c = close.iloc[-1]

    window = close.iloc[-LOOKBACK_52WK:]
    wk_low = window.min()
    wk_high = window.max()

    return {
        "above_sma150": bool(c > sma150.iloc[-1]),
        "above_sma200": bool(c > sma200.iloc[-1]),
        "sma150_above_sma200": bool(sma150.iloc[-1] > sma200.iloc[-1]),
        "sma200_trending_up": bool(sma200.iloc[-1] > sma200.iloc[-21]),
        "sma50_above_150_200": bool(
            sma50.iloc[-1] > sma150.iloc[-1] and sma50.iloc[-1] > sma200.iloc[-1]
        ),
        "above_sma50": bool(c > sma50.iloc[-1]),
        "above_52wk_low_30pct": bool(c >= 1.30 * wk_low),
        "within_25pct_of_52wk_high": bool(c >= 0.75 * wk_high),
    }


def passes_trend_template(checks: dict) -> bool:
    return all(checks.values())


# ── Stock analysis ──────────────────────────────────────────────────────────
def analyse(symbol: str, index_s: pd.Series, float_shares: float = 0) -> dict | None:
    try:
        raw = load_ohlc(symbol)
        if raw is None or len(raw) < MIN_BARS:
            return None

        fm = float_metrics(raw["close"], raw["volume"], float_shares or None)
        if not passes_hard_gate(fm):
            return None

        df = raw.set_index("date")
        df.index = pd.to_datetime(df.index)
        c = df["close"].astype(float)

        checks = trend_template_checks(c)
        if not passes_trend_template(checks):
            return None

        common = c.index.intersection(index_s.index)
        if len(common) < 30:
            return None
        c_rs = c.loc[common]
        idx_rs = index_s.loc[common]
        rs = (c_rs / idx_rs) * 1000
        if not base._weekly_rs_gate(rs, c_rs, idx_rs):
            return None

        window = c.iloc[-LOOKBACK_52WK:]
        curr_close = c.iloc[-1]
        prev_close = c.iloc[-2]

        return {
            "symbol": symbol,
            "close": curr_close,
            "day_chg": (curr_close - prev_close) / prev_close * 100,
            "off_high_pct": (curr_close / window.max() - 1) * 100,
            "above_low_pct": (curr_close / window.min() - 1) * 100,
            "trap": trap_label(fm),
            "liq_tag": liq_tag(raw),
            "cmf_tag": cmf_tag(raw),
            "deliv_tag": deliv_tag(symbol),
        }
    except Exception:
        return None


# ── Markdown ─────────────────────────────────────────────────────────────────
STATIC_HEADER = """### Scan definition
| Filter | Value |
|--------|-------|
| Exchange | NSE common equity |
| Price | > Rs 50 |
| Market cap | Rs 1,000 Cr - Rs 5 Lakh Cr |
| Criteria (all must pass) | close > SMA50 > SMA150 > SMA200 stack, SMA200 rising 21d, close within 25% of 52wk high, close >= 30% above 52wk low, RS gate |
| RS gate | Daily RS Line > Weekly RS EMA9, Weekly RS EMA9 rising (RS = close/NIFTY MIDSML 400 x 1000) |
| Float gate | AVOID dropped from scan, SAFE/CAUTION shown under symbol (float_gate.py) |
| Symbol tags | trap - liq (avg10Cr-todayCr) - CMF - DEL% |

---
"""


def _table_rows(findings: list[dict]) -> list[str]:
    rows = []
    for f in findings:
        sym = f["symbol"]
        tv = f"https://in.tradingview.com/chart/?symbol=NSE:{sym}"
        ds = "+" if f["day_chg"] >= 0 else ""
        oh = f"{f['off_high_pct']:.1f}%"
        al = f"+{f['above_low_pct']:.1f}%"
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
        sym_cell = f"[{sym}]({tv})" + (f"<br><sub>{' . '.join(extras)}</sub>" if extras else "")
        rows.append(
            f"| {sym_cell} "
            f"| {f['close']:.2f} "
            f"| {oh} "
            f"| {al} "
            f"| SMA-OK "
            f"| RS-OK "
            f"| {ds}{f['day_chg']:.2f}% |"
        )
    return rows


def build_markdown(findings: list[dict]) -> str:
    rows = sorted(findings, key=lambda x: x["off_high_pct"], reverse=True)

    hdr = [
        "| Symbol | Close | %off 52wk-high | %above 52wk-low | SMA stack | RS gate | Day chg% |",
        "|--------|------:|----------------:|------------------:|:---------:|:-------:|--------:|",
    ]

    lines = [
        f"# Minervini Trend Template Scan - {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        STATIC_HEADER,
        f"**Qualifying: {len(rows)}**",
        "",
        "### Trend Template Qualifiers",
    ]
    if rows:
        lines += hdr + _table_rows(rows)
        lines += ["", "```", ",".join(f"NSE:{f['symbol']}" for f in rows), "```"]
    else:
        lines.append("*No signals.*")

    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nFetching live watchlist from TradingView screener...")
    watchlist, float_map = base.get_watchlist()
    print(f"  Watchlist: {len(watchlist)} stocks | float data for {len(float_map)} | Scanning...\n")

    bench_map = load_ohlc_many([BENCH_SYM])
    bench_df = bench_map.get(BENCH_SYM)
    if bench_df is None:
        print(f"  ERROR: benchmark {BENCH_SYM} not found in DB, aborting.")
        return
    index_s = bench_df.set_index("date")["close"].astype(float)
    index_s.index = pd.to_datetime(index_s.index)

    findings = []
    for i, sym in enumerate(watchlist, 1):
        print(f"  {sym:<20} ({i}/{len(watchlist)})   ", end="\r")
        result = analyse(sym, index_s, float_shares=float_map.get(sym, 0))
        if result:
            findings.append(result)

    print(f"\n  Qualifying: {len(findings)}")

    dated_file = os.path.join(SCANS_DIR, f"minervini_trend_{TODAY}.md")
    md = build_markdown(findings)
    with open(MD_LATEST, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(dated_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  Saved -> {MD_LATEST}")
    print(f"  Saved -> {dated_file}")


if __name__ == "__main__":
    main()
