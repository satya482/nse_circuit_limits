#!/usr/bin/env python3
"""
NSE Z-Score Mean Reversion Scanner (oversold / long-bounce candidates)
Flags stocks trading 3+ standard deviations below their 55-bar mean close.

Formula mirrors pine_scripts/Satya Z-Score Probability Indicator.txt
(lookback changed from Pine default 75 to 55, per Python<->Pine parity convention):
    z = (close - SMA(close, 55)) / STDEV(close, 55)

Data source: .ohlc_data/market.db  (populated by fetch_data.py)
Output:      zscore_scans/zscore_meanreversion_scans.md
"""

import sys
import os
from datetime import datetime

import pandas as pd

from ohlc_db import load_ohlc, liq_tag, cmf_tag, deliv_tag
from float_gate import float_metrics, passes_hard_gate, trap_label
import ema25_zl_scanner as base
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER
from tv_watchlist import tv_csv

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "zscore_scans")
TODAY = datetime.now().strftime("%Y-%m-%d")
MD_FILE = os.path.join(SCANS_DIR, "zscore_meanreversion_scans.md")


ZSCORE_LEN = 55
Z_THRESHOLD = -3.0
ZONE_CAP = 60  # bars to scan back for zone-age before giving up


def zscore(close: pd.Series, len: int = ZSCORE_LEN) -> pd.Series:
    sma = close.rolling(len, min_periods=len).mean()
    sd = close.rolling(len, min_periods=len).std(ddof=0)
    return (close - sma) / sd


def zscore_zone_days(
    z: pd.Series, threshold: float = Z_THRESHOLD, cap: int = ZONE_CAP
) -> tuple[int, bool]:
    """Consecutive trailing bars with z <= threshold (capped), and whether z has
    risen for the last 3 bars (early reversion tell, mirrors ta.rising(z_sma, 3))."""
    n = len(z)
    if n == 0 or pd.isna(z.iloc[-1]) or z.iloc[-1] > threshold:
        return 0, False
    days = 0
    limit = max(0, n - cap)
    for i in range(n - 1, limit - 1, -1):
        if pd.isna(z.iloc[i]) or z.iloc[i] > threshold:
            break
        days += 1
    turning_up = bool(n >= 3 and z.iloc[-1] > z.iloc[-2] > z.iloc[-3])
    return days, turning_up


def analyse(symbol: str, float_shares: float = 0) -> dict | None:
    try:
        raw = load_ohlc(symbol)
        if raw is None or len(raw) < ZSCORE_LEN:
            return None

        fm = float_metrics(raw["close"], raw["volume"], float_shares or None)
        if not passes_hard_gate(fm):
            return None

        c = raw["close"].astype(float)
        z = zscore(c)

        if pd.isna(z.iloc[-1]) or z.iloc[-1] > Z_THRESHOLD:
            return None  # not oversold

        sma55 = c.rolling(ZSCORE_LEN, min_periods=ZSCORE_LEN).mean().iloc[-1]
        dist_pct = (c.iloc[-1] / sma55 - 1) * 100
        zone_days, turning_up = zscore_zone_days(z)

        curr_close = c.iloc[-1]
        prev_close = c.iloc[-2]
        day_chg = (curr_close - prev_close) / prev_close * 100

        return {
            "symbol": symbol,
            "z": round(z.iloc[-1], 2),
            "close": curr_close,
            "sma55": round(sma55, 2),
            "dist_pct": round(dist_pct, 2),
            "day_chg": day_chg,
            "turning_up": turning_up,
            "zone_days": zone_days,
            "trap": trap_label(fm),
            "liq_tag": liq_tag(raw),
            "cmf_tag": cmf_tag(raw),
            "deliv_tag": deliv_tag(symbol),
        }
    except Exception:
        return None


# -- Markdown -----------------------------------------------------------
STATIC_HEADER = f"""### Scan definition
| Filter | Value |
|--------|-------|
| Exchange | NSE common equity |
| Price | > Rs 50 |
| Market cap | Rs 1,000 Cr - Rs 5 Lakh Cr |
| Signal | Close is {abs(Z_THRESHOLD):.0f}+ standard deviations below its {ZSCORE_LEN}-bar mean (z = (close - SMA{ZSCORE_LEN}) / STDEV{ZSCORE_LEN}) |
| Direction | Oversold only (long / bounce candidates) |
| Zone Age | Consecutive bars continuously at z <= {Z_THRESHOLD:.0f} (capped {ZONE_CAP}d) |
| Turning Up | z rose for the last 3 bars - early reversion tell |
| Float gate | AVOID dropped from scan - SAFE / CAUTION shown under symbol (float_gate.py) |
| Symbol tags | trap - liq (avg10Cr - todayCr) - CMF - DEL% |

---
"""


def _table_rows(findings: list[dict], circuit: dict[str, tuple]) -> list[str]:
    rows = []
    for f in findings:
        sym = f["symbol"]
        cl, em = circuit.get(sym, ("20%", ""))
        tv = f"https://in.tradingview.com/chart/?symbol=NSE:{sym}"
        zd = f"{f['zone_days']}d+" if f["zone_days"] >= ZONE_CAP else f"{f['zone_days']}d"
        ds = "+" if f["day_chg"] >= 0 else ""
        tu = "up" if f["turning_up"] else ""
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
        sym_cell = f"[{sym}]({tv})" + (f"<br><sub>{' - '.join(extras)}</sub>" if extras else "")
        rows.append(
            f"| {sym_cell} "
            f"| {f['z']:.2f} "
            f"| {zd} "
            f"| {tu} "
            f"| {f['close']:.2f} "
            f"| {f['sma55']:.2f} "
            f"| {f['dist_pct']:.1f}% "
            f"| {ds}{f['day_chg']:.2f}% "
            f"| {cl} {em} |"
        )
    return rows


def build_markdown(findings: list[dict], circuit: dict[str, tuple]) -> str:
    rows = sorted(findings, key=lambda x: (x["z"], x["symbol"]))  # most negative (most extreme) first

    hdr = [
        "| Symbol | Z-Score | Zone Age | Turning Up | Close | SMA55 | Dist% | Day Chg | Circuit |",
        "|--------|--------:|---------:|:----------:|------:|------:|------:|--------:|:-------:|",
    ]

    lines = [
        f"# NSE Z-Score Mean Reversion Scanner (SD3-) - {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        STATIC_HEADER,
        f"**Oversold candidates: {len(rows)}**",
        "",
        "### SD3- Oversold Candidates",
    ]
    if rows:
        lines += hdr + _table_rows(rows, circuit)
        lines += ["", "```", tv_csv(f"NSE:{f['symbol']}" for f in rows), "```"]
    else:
        lines.append("*No signals.*")

    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


# -- Main -----------------------------------------------------------------
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

    print(f"\n  Oversold candidates: {len(findings)}")

    dated_file = os.path.join(SCANS_DIR, f"zscore_meanreversion_scans_{TODAY}.md")
    md = build_markdown(findings, circuit)
    with open(MD_FILE, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(dated_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  Saved -> {MD_FILE}")
    print(f"  Saved -> {dated_file}")


if __name__ == "__main__":
    main()
