#!/usr/bin/env python3
"""
NSE F&O ZLEMA25 Scanner  —  Uptrend Start / Downtrend Start
Run after 4:20 PM IST on trading days (after run_fetch_data.ps1 completes).

Universe:  NSE F&O underlyings (~200 stocks), .fno_cache.csv refreshed monthly
Signal:    ZLEMA25 turned UP  → Uptrend Start   (within FRESH_BARS days)
           ZLEMA25 turned DOWN → Downtrend Start (within FRESH_BARS days)
Output:    fno_zlema25_scans/fno_zlema25_scans.md
           fno_zlema25_scans/fno_zlema25_scans_YYYY-MM-DD.md
"""

import os
import sys
from datetime import datetime

import pandas as pd

from ohlc_db import load_ohlc
from fno_universe import get_fno_symbols

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "fno_zlema25_scans")
MD_FILE = os.path.join(SCANS_DIR, "fno_zlema25_scans.md")
TODAY = datetime.now().strftime("%Y-%m-%d")

FRESH_BARS = 5  # turns within this many bars are shown in output
TURN_CAP = 60  # max lookback when searching for a turn


# ── Indicators ─────────────────────────────────────────────────────────────────


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def _zlema(s: pd.Series, n: int) -> pd.Series:
    e = _ema(s, n)
    return 2 * e - _ema(e, n)


def _bb_kc_squeeze(df: pd.DataFrame) -> bool:
    if len(df) < 21:
        return False
    c = df["close"].astype(float)
    h = df["high"].astype(float)
    l = df["low"].astype(float)
    tr = pd.concat([h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1).max(
        axis=1
    )
    bb_basis = c.rolling(20).mean()
    bb_std = c.rolling(20).std()
    kc_basis = bb_basis
    kc_atr = tr.rolling(20).mean()
    return bool(
        (bb_basis + 2.0 * bb_std).iloc[-1] < (kc_basis + 1.5 * kc_atr).iloc[-1]
        and (bb_basis - 2.0 * bb_std).iloc[-1] > (kc_basis - 1.5 * kc_atr).iloc[-1]
    )


def _last_turn(
    zl25: pd.Series, closes: pd.Series, direction: str
) -> tuple[int, float] | None:
    """
    Scan backwards for the most recent ZLEMA25 turn within TURN_CAP bars.
    direction: 'up'  → turned up  (zl[i] > zl[i-1] and zl[i-1] <= zl[i-2])
               'down' → turned down (zl[i] < zl[i-1] and zl[i-1] >= zl[i-2])
    Returns (bars_ago, pct_change_since_turn) or None.
    bars_ago=1 means the turn happened on today's bar.
    """
    n = len(zl25)
    limit = max(2, n - TURN_CAP)
    for i in range(n - 1, limit - 1, -1):
        if i < 2:
            break
        if direction == "up":
            turned = (
                zl25.iloc[i] > zl25.iloc[i - 1] and zl25.iloc[i - 1] <= zl25.iloc[i - 2]
            )
        else:
            turned = (
                zl25.iloc[i] < zl25.iloc[i - 1] and zl25.iloc[i - 1] >= zl25.iloc[i - 2]
            )
        if turned:
            bars_ago = (n - 1) - i + 1
            pct = (closes.iloc[-1] / closes.iloc[i - 1] - 1) * 100
            return bars_ago, round(pct, 2)
    return None


# ── Per-symbol analysis ────────────────────────────────────────────────────────


def _analyse(symbol: str) -> dict | None:
    try:
        df = load_ohlc(symbol)
        if df is None or len(df) < 60:
            return None

        c = df["close"].astype(float)
        zl25 = _zlema(c, 25)

        up_turn = _last_turn(zl25, c, "up")
        down_turn = _last_turn(zl25, c, "down")

        # Only keep if at least one signal is fresh enough to show
        if (up_turn is None or up_turn[0] > FRESH_BARS) and (
            down_turn is None or down_turn[0] > FRESH_BARS
        ):
            return None

        return {
            "symbol": symbol,
            "close": round(float(c.iloc[-1]), 2),
            "day_chg": round(
                (float(c.iloc[-1]) - float(c.iloc[-2])) / float(c.iloc[-2]) * 100, 2
            ),
            "zl_rising": bool(zl25.iloc[-1] > zl25.iloc[-2]),
            "zl_dist": round(
                (float(c.iloc[-1]) - float(zl25.iloc[-1])) / float(zl25.iloc[-1]) * 100,
                2,
            ),
            "up_turn": up_turn,  # (bars_ago, pct) or None
            "down_turn": down_turn,  # (bars_ago, pct) or None
            "squeeze": _bb_kc_squeeze(df),
        }
    except Exception:
        return None


# ── Markdown builder ───────────────────────────────────────────────────────────

_HDR = [
    "| Symbol | Close | Day% | Turn (bars ago) | % since turn | vs ZL25 | Squeeze |",
    "|--------|------:|-----:|----------------:|-------------:|--------:|:-------:|",
]


def _row(f: dict, turn_key: str) -> str:
    bars_ago, pct_since = f[turn_key]
    tv = f"https://in.tradingview.com/chart/?symbol=NSE:{f['symbol']}"
    ds = "+" if f["day_chg"] >= 0 else ""
    ps = "+" if pct_since >= 0 else ""
    vzl = f"+{f['zl_dist']:.1f}%" if f["zl_dist"] >= 0 else f"{f['zl_dist']:.1f}%"
    sqz = "✓" if f["squeeze"] else "-"
    bell = " 🔔" if bars_ago <= 2 else ""
    return (
        f"| [{f['symbol']}]({tv}){bell} "
        f"| {f['close']:.2f} "
        f"| {ds}{f['day_chg']:.1f}% "
        f"| {bars_ago}d "
        f"| {ps}{pct_since:.1f}% "
        f"| {vzl} "
        f"| {sqz} |"
    )


def _build_md(up_starts: list[dict], dn_starts: list[dict], total_scanned: int) -> str:
    lines = [
        f"# NSE F&O ZLEMA25 Scanner — {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST · {total_scanned} F&O stocks scanned*",
        "",
        "### Scan definition",
        "| | |",
        "|-|-|",
        "| Universe | NSE F&O underlyings (~200 stocks, refreshed monthly) |",
        f"| Signal | ZLEMA25 turn within last **{FRESH_BARS} bars** |",
        "| 🔔 | Turn happened today or yesterday (1–2 bars ago) |",
        "| vs ZL25 | % of close above/below ZLEMA25 level |",
        "| Squeeze | BB(20,2) inside KC(20,1.5) on last bar |",
        "",
        "---",
        "",
        f"## Uptrend Start &nbsp;({len(up_starts)} stocks)",
        f"*ZLEMA25 turned UP within last {FRESH_BARS} bars · sorted freshest first*",
        "",
    ]

    if up_starts:
        lines += _HDR + [_row(f, "up_turn") for f in up_starts]
    else:
        lines.append("*No uptrend starts today.*")

    lines += [
        "",
        "---",
        "",
        f"## Downtrend Start &nbsp;({len(dn_starts)} stocks)",
        f"*ZLEMA25 turned DOWN within last {FRESH_BARS} bars · sorted freshest first*",
        "",
    ]

    if dn_starts:
        lines += _HDR + [_row(f, "down_turn") for f in dn_starts]
    else:
        lines.append("*No downtrend starts today.*")

    return "\n".join(lines)


# ── Console summary ────────────────────────────────────────────────────────────


def _print_summary(up_starts: list[dict], dn_starts: list[dict]) -> None:
    print(f"\n{'='*65}")
    print(f"  NSE F&O ZLEMA25  |  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Uptrend starts : {len(up_starts)}")
    print(f"  Downtrend starts: {len(dn_starts)}")
    print(f"{'='*65}")

    def _fmt(f: dict, key: str) -> str:
        bars, pct = f[key]
        ds = "+" if f["day_chg"] >= 0 else ""
        ps = "+" if pct >= 0 else ""
        new = " <NEW>" if bars <= 2 else ""
        return (
            f"  {f['symbol']:<14} {f['close']:>9.2f}  "
            f"turn:{bars}d  {ps}{pct:.1f}%  day:{ds}{f['day_chg']:.1f}%{new}"
        )

    if up_starts:
        print("\n  -- Uptrend Start --")
        for f in up_starts:
            print(_fmt(f, "up_turn"))

    if dn_starts:
        print("\n  -- Downtrend Start --")
        for f in dn_starts:
            print(_fmt(f, "down_turn"))
    print()


# ── Main ───────────────────────────────────────────────────────────────────────


def main():
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nLoading F&O universe...")
    symbols = get_fno_symbols()

    print(f"\nScanning {len(symbols)} stocks for ZLEMA25 turns...\n")
    results = []
    for i, sym in enumerate(symbols, 1):
        print(f"  {sym:<16} ({i}/{len(symbols)})", end="\r")
        r = _analyse(sym)
        if r:
            results.append(r)

    up_starts = sorted(
        [f for f in results if f["up_turn"] and f["up_turn"][0] <= FRESH_BARS],
        key=lambda x: x["up_turn"][0],
    )
    dn_starts = sorted(
        [f for f in results if f["down_turn"] and f["down_turn"][0] <= FRESH_BARS],
        key=lambda x: x["down_turn"][0],
    )

    _print_summary(up_starts, dn_starts)

    md = _build_md(up_starts, dn_starts, len(symbols))
    dated = os.path.join(SCANS_DIR, f"fno_zlema25_scans_{TODAY}.md")
    for path in (MD_FILE, dated):
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(md)
    print(f"  Saved -> {MD_FILE}")
    print(f"  Saved -> {dated}")


if __name__ == "__main__":
    main()
