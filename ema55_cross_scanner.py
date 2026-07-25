#!/usr/bin/env python3
"""
NSE EMA55 Cross Watchlist Scanner
Run after 4:20 PM IST on trading days (after run_fetch_data.ps1 completes).

Watchlist filters (TradingView, reused from ema25_zl_scanner.py):
  - NSE common equity, price > 50 INR, market cap 1,000 Cr - 5 Lakh Cr

Signal (no RS gate — this is a pure price/EMA55 watch trigger):
  - close currently above EMA55
  - close within +10% of EMA55 (drops off once too extended, or once it
    crosses back under — keeps the list to stocks worth watching closely)
  - reports days since EMA55 was last crossed (parity with ema25_zl_scanner's
    zl25_turn_stats — same backward-scan-with-cap pattern, but for a
    close/EMA55 crossover instead of a ZLEMA25 slope turn)

Data source: .ohlc_data/market.db  (populated by fetch_data.py)
Output:      ema55_cross_scans/ema55_cross_scans.md
"""

import sys
import os
from datetime import datetime

import pandas as pd

import ema25_zl_scanner as base
from ohlc_db import load_ohlc, liq_tag, cmf_tag, deliv_tag
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER
from float_gate import float_metrics, passes_hard_gate, trap_label

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "ema55_cross_scans")
TODAY = datetime.now().strftime("%Y-%m-%d")
MD_FILE = os.path.join(SCANS_DIR, "ema55_cross_scans.md")

EMA_PERIOD = 55
BAND_PCT = 10.0  # keep listed while close is within +BAND_PCT% of EMA55
CROSS_CAP = 60  # bars to scan back for the last cross-up before giving up

_AGE_BUCKETS = [
    ("1 DAY", 1, 1),
    ("2 DAYS", 2, 2),
    ("3 DAYS", 3, 3),
    ("4-5 DAYS", 4, 5),
    ("6-10 DAYS", 6, 10),
    ("11-15 DAYS", 11, 15),
    ("15 DAYS+", 16, 10**9),
]


def ema55_cross_stats(close: pd.Series, ema55: pd.Series) -> tuple[int, float]:
    """Bars since close last crossed above ema55, and % price change since
    that bar. Same backward-scan-with-cap shape as ema25_zl_scanner's
    zl25_turn_stats(), just crossover-of-two-series instead of slope-turn."""
    n = len(close)
    limit = max(2, n - CROSS_CAP)
    for i in range(n - 1, limit - 1, -1):
        crossed_up = close.iloc[i] > ema55.iloc[i] and close.iloc[i - 1] <= ema55.iloc[i - 1]
        if crossed_up:
            bars = (n - 1) - i + 1
            pct = (close.iloc[-1] / close.iloc[i - 1] - 1) * 100
            return bars, round(pct, 2)
    cap_idx = max(0, n - CROSS_CAP)
    return CROSS_CAP, round((close.iloc[-1] / close.iloc[cap_idx] - 1) * 100, 2)


def analyse(symbol: str, float_shares: float = 0) -> dict | None:
    try:
        raw = load_ohlc(symbol)
        if raw is None or len(raw) < 130:  # ~2.4x EMA period, matches zlema25 warmup ratio
            return None

        fm = float_metrics(raw["close"], raw["volume"], float_shares or None)
        if not passes_hard_gate(fm):
            return None

        c = raw["close"].astype(float)
        ema55 = base.ema(c, EMA_PERIOD)

        if c.iloc[-1] <= ema55.iloc[-1]:
            return None  # not currently above EMA55

        band_pct = (c.iloc[-1] / ema55.iloc[-1] - 1) * 100
        if band_pct > BAND_PCT:
            return None  # too extended past EMA55 to "monitor closely"

        cross_days, cross_pct = ema55_cross_stats(c, ema55)

        curr_close = c.iloc[-1]
        prev_close = c.iloc[-2]
        day_chg = (curr_close - prev_close) / prev_close * 100

        return {
            "symbol": symbol,
            "close": curr_close,
            "day_chg": day_chg,
            "band_pct": round(band_pct, 2),
            "cross_days": cross_days,
            "cross_pct": cross_pct,
            "trap": trap_label(fm),
            "liq_tag": liq_tag(raw),
            "cmf_tag": cmf_tag(raw),
            "deliv_tag": deliv_tag(symbol),
        }
    except Exception:
        return None


# ── Markdown ───────────────────────────────────────────────────────────────
STATIC_HEADER = f"""### Scan definition
| Filter | Value |
|--------|-------|
| Exchange | NSE common equity |
| Price | > ₹50 |
| Market cap | ₹1,000 Cr – ₹5 Lakh Cr |
| Signal | Close above EMA{EMA_PERIOD} and within +{BAND_PCT:.0f}% of it |
| Cross Age / Chg% | Days since close last crossed above EMA{EMA_PERIOD} (capped {CROSS_CAP}d) · % price change since that bar |
| Float gate | ⛔ AVOID dropped from scan · ✓ SAFE / ⚠ CAUTION shown under symbol (float_gate.py) |
| Symbol tags | trap · liq (↗avg10Cr·todayCr) · CMF · DEL% |

---
"""


def _table_rows(findings: list[dict], circuit: dict[str, tuple]) -> list[str]:
    rows = []
    for f in findings:
        sym = f["symbol"]
        cl, em = circuit.get(sym, ("20%", ""))
        tv = f"https://in.tradingview.com/chart/?symbol=NSE:{sym}"
        cd = f"{f['cross_days']}d+" if f["cross_days"] >= CROSS_CAP else f"{f['cross_days']}d"
        cp = f"+{f['cross_pct']:.1f}%" if f["cross_pct"] >= 0 else f"{f['cross_pct']:.1f}%"
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
        sym_cell = f"[{sym}]({tv})" + (f"<br><sub>{' · '.join(extras)}</sub>" if extras else "")
        rows.append(
            f"| {sym_cell} "
            f"| {cd} "
            f"| {cp} "
            f"| +{f['band_pct']:.1f}% "
            f"| {ds}{f['day_chg']:.2f}% "
            f"| {f['close']:.2f} "
            f"| {cl} {em} |"
        )
    return rows


def build_markdown(findings: list[dict], circuit: dict[str, tuple]) -> str:
    rows = sorted(findings, key=lambda x: (x["cross_days"], x["symbol"]))

    hdr = [
        "| Symbol | Cross Age | Chg% Since Cross | EMA55 Dist | Day Chg | Close | Circuit |",
        "|--------|----------:|------------------:|-----------:|--------:|------:|:-------:|",
    ]

    wl_parts = []
    for label, lo, hi in _AGE_BUCKETS:
        syms = [f["symbol"] for f in rows if lo <= f["cross_days"] <= hi]
        if syms:
            wl_parts.append(f"###{label}," + ",".join(f"NSE:{s}" for s in syms))

    lines = [
        f"# NSE EMA{EMA_PERIOD} Cross Watchlist — {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        STATIC_HEADER,
        f"**On watch: {len(rows)}**",
        "",
        "**TradingView watchlist** *(sectioned by cross age — paste into TV import)*",
        "```",
        ",".join(wl_parts),
        "```",
        "",
        "### EMA55 Cross Watchlist",
    ]
    if rows:
        lines += hdr + _table_rows(rows, circuit)
        lines += ["", "```", ",".join(f"NSE:{f['symbol']}" for f in rows), "```"]
    else:
        lines.append("*No signals.*")

    lines += ["", "### TradingView Watchlists *(by cross age)*"]
    for label, lo, hi in _AGE_BUCKETS:
        syms = [f["symbol"] for f in rows if lo <= f["cross_days"] <= hi]
        if not syms:
            continue
        lines += [
            "",
            f"**{label.lower()}** ({len(syms)})",
            "```",
            ",".join(f"NSE:{s}" for s in syms),
            "```",
        ]

    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


# ── Main ───────────────────────────────────────────────────────────────────
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

    dated_file = os.path.join(SCANS_DIR, f"ema55_cross_scans_{TODAY}.md")
    md = build_markdown(findings, circuit)
    with open(MD_FILE, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(dated_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  Saved -> {MD_FILE}")
    print(f"  Saved -> {dated_file}")


if __name__ == "__main__":
    main()
