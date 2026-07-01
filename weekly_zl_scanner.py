#!/usr/bin/env python3
"""
NSE Weekly ZL Scanner — ZLEMA25 Uptrend Start
Stocks where the weekly ZLEMA25 has just started a new uptrend on the current bar.

Uptrend start condition (both must be true on the current weekly bar):
  ZLEMA25 > ZLEMA25[1]       — this week's ZLEMA25 is higher than last week's (rising now)
  ZLEMA25[2] >= ZLEMA25[1]   — two weeks ago was >= last week (prev bar was flat or falling)

Watchlist: NSE common equity, price > ₹50, MCap ₹800 Cr – ₹1 Lakh Cr
No RS gate (weekly timeframe is already a higher-order filter)

price_vs_zl: TOUCH (±1.5% of weekly ZLEMA25) = pullback entry zone · ABOVE · BELOW
Squeeze column: BB(20,2.0,SMA) inside KC(20,1.5,SMA ATR) — informational, not a gate

Output: weekly_zl_scans/weekly_zl_scans.md  +  weekly_zl_scans/weekly_zl_scans_YYYY-MM-DD.md
"""

import sys
import os
import csv
import json
from datetime import datetime

import pandas as pd
from tradingview_screener import Query, col

from ohlc_db import load_ohlc, get_names, liq_tag
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "weekly_zl_scans")
_LABELS_FILE = os.path.join(REPO_DIR, "tools", "stock_labels.json")
_LABELS: dict = (
    json.loads(open(_LABELS_FILE, encoding="utf-8").read())
    if os.path.exists(_LABELS_FILE)
    else {}
)
TODAY = datetime.now().strftime("%Y-%m-%d")
MD_FILE = os.path.join(SCANS_DIR, "weekly_zl_scans.md")

MC_LOW = 800 * 1_00_00_000  # ₹800 Cr
MC_HIGH = 1_00_000 * 1_00_00_000  # ₹1 Lakh Cr
ZL_TURN_CAP = 52  # weeks (~1 year)
TOUCH_PCT = 0.015  # ±1.5% of ZLEMA25 = "touching" (pullback entry zone)


# ── Indicators ────────────────────────────────────────────────────────────────
def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def zlema(s: pd.Series, n: int) -> pd.Series:
    e = ema(s, n)
    return 2 * e - ema(e, n)


def bb_kc_squeeze_info(df: pd.DataFrame) -> tuple[bool, int]:
    """Returns (squeeze_on, consecutive_bars_in_squeeze) as of the last bar."""
    if len(df) < 21:
        return False, 0
    c = df["close"].astype(float)
    h = df["high"].astype(float)
    l = df["low"].astype(float)

    bb_basis = c.rolling(20).mean()
    bb_upper = bb_basis + 2.0 * c.rolling(20).std()
    bb_lower = bb_basis - 2.0 * c.rolling(20).std()

    tr = pd.concat([h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1).max(
        axis=1
    )
    kc_atr = tr.rolling(20).mean()
    kc_basis = c.rolling(20).mean()
    kc_upper = kc_basis + 1.5 * kc_atr
    kc_lower = kc_basis - 1.5 * kc_atr

    squeeze_series = (bb_upper < kc_upper) & (bb_lower > kc_lower)
    squeeze_now = bool(squeeze_series.iloc[-1])
    if not squeeze_now:
        return False, 0

    count = 0
    for v in reversed(squeeze_series.values):
        if v:
            count += 1
        else:
            break
    return True, count


def zl25_turn_stats(zl25: pd.Series, closes: pd.Series) -> tuple[int, float]:
    n = len(zl25)
    limit = max(2, n - ZL_TURN_CAP)
    for i in range(n - 1, limit - 1, -1):
        if zl25.iloc[i] > zl25.iloc[i - 1] and zl25.iloc[i - 1] <= zl25.iloc[i - 2]:
            bars = (n - 1) - i + 1
            pct = (closes.iloc[-1] / closes.iloc[i - 1] - 1) * 100
            return bars, round(pct, 2)
    cap_idx = max(0, n - ZL_TURN_CAP)
    return ZL_TURN_CAP, round((closes.iloc[-1] / closes.iloc[cap_idx] - 1) * 100, 2)


def zl25_consecutive_rising(zl25: pd.Series) -> int:
    """Count consecutive weekly bars at the tail where ZLEMA25[i] > ZLEMA25[i-1]."""
    count = 0
    for i in range(len(zl25) - 1, 0, -1):
        if zl25.iloc[i] > zl25.iloc[i - 1]:
            count += 1
        else:
            break
    return count


# ── Weekly resampling ─────────────────────────────────────────────────────────
def to_weekly(df: pd.DataFrame) -> pd.DataFrame:
    """Resample daily OHLCV to weekly. Includes partial current week as last bar."""
    d = df.set_index("date")
    d.index = pd.to_datetime(d.index)
    w = (
        d.resample("W")
        .agg(
            open=("open", "first"),
            high=("high", "max"),
            low=("low", "min"),
            close=("close", "last"),
            volume=("volume", "sum"),
        )
        .dropna(subset=["close"])
    )
    return w.reset_index()


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


# ── Stock analysis ─────────────────────────────────────────────────────────────
def analyse(symbol: str) -> dict | None:
    try:
        daily = load_ohlc(symbol, lookback=400)
        if daily is None or len(daily) < 30:
            return None

        wdf = to_weekly(daily)
        if len(wdf) < 22:
            return None

        c = wdf["close"].astype(float)
        zl25 = zlema(c, 25)
        if len(zl25) < 3:
            return None
        # Uptrend start: current bar rising AND previous bar was flat/falling
        if not (zl25.iloc[-1] > zl25.iloc[-2] and zl25.iloc[-3] >= zl25.iloc[-2]):
            return None

        sqz_on, sqz_weeks = bb_kc_squeeze_info(wdf)
        zl_weeks, zl_pct = zl25_turn_stats(zl25, c)
        consec_weeks = zl25_consecutive_rising(zl25)
        wk_zl25_val = float(zl25.iloc[-1])

        daily_c = daily["close"].astype(float)
        curr_close = float(daily_c.iloc[-1])
        day_chg = (
            (curr_close / daily_c.iloc[-2] - 1) * 100 if len(daily_c) >= 2 else 0.0
        )

        ratio = (curr_close - wk_zl25_val) / wk_zl25_val
        if abs(ratio) <= TOUCH_PCT:
            price_vs_zl = "TOUCH"
        elif ratio > TOUCH_PCT:
            price_vs_zl = "ABOVE"
        else:
            price_vs_zl = "BELOW"

        return {
            "symbol": symbol,
            "close": curr_close,
            "day_chg": day_chg,
            "sqz_on": sqz_on,
            "sqz_weeks": sqz_weeks,
            "zl_weeks": zl_weeks,
            "zl_pct": zl_pct,
            "consec_weeks": consec_weeks,
            "wk_zl25_val": wk_zl25_val,
            "price_vs_zl": price_vs_zl,
            "liq_tag": liq_tag(daily),
        }
    except Exception:
        return None


# ── Output ─────────────────────────────────────────────────────────────────────
_PVZ_ORDER = {"TOUCH": 0, "ABOVE": 1, "BELOW": 2}


def _sort_key(f: dict) -> tuple:
    return (_PVZ_ORDER.get(f["price_vs_zl"], 9), -f["consec_weeks"])


def _static_header() -> str:
    return f"""### Scan definition
| Filter | Value |
|--------|-------|
| Exchange | NSE common equity |
| Price | > ₹50 |
| Market cap | ₹800 Cr – ₹1 Lakh Cr |
| Timeframe | Weekly (daily OHLC resampled; current partial week included) |
| RS filter | None (weekly timeframe is already a higher-order filter) |
| Uptrend start | ZLEMA25 > ZLEMA25[1]  AND  ZLEMA25[2] ≥ ZLEMA25[1] — rising this bar after flat/falling prev bar |
| Price vs ZL | TOUCH = within ±{TOUCH_PCT*100:.0f}% of weekly ZLEMA25 (pullback entry zone) · ABOVE · BELOW |
| Consec | Consecutive weekly bars ZLEMA25 has been rising |
| Sqz | Consecutive weekly bars BB(20,2.0,SMA) inside KC(20,1.5,SMA ATR) |
| ZL Weeks / ZL Chg% | Weeks since weekly ZLEMA25 last turned up · % price change since (capped {ZL_TURN_CAP}w) |

---
"""


def _table_rows(
    findings: list[dict],
    circuit: dict[str, tuple],
    names: dict[str, str] | None = None,
) -> list[str]:
    hdr = [
        "| Symbol | Company | Consec | Price vs ZL | ZL Weeks | ZL Chg% | Day Chg | Close | Sqz | Circuit |",
        "|--------|---------|-------:|:-----------:|---------:|--------:|--------:|------:|:---:|:-------:|",
    ]
    rows = []
    for f in sorted(findings, key=_sort_key):
        sym = f["symbol"]
        cl, em = circuit.get(sym, ("20%", ""))
        tv = f"https://in.tradingview.com/chart/?symbol=NSE:{sym}"
        zl_w = (
            f"{f['zl_weeks']}w+"
            if f["zl_weeks"] >= ZL_TURN_CAP
            else f"{f['zl_weeks']}w"
        )
        zl_p = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
        ds = "+" if f["day_chg"] >= 0 else ""
        sqz = f"{f['sqz_weeks']}w" if f["sqz_on"] else "—"
        pvz = f["price_vs_zl"]
        lbl = _LABELS.get(sym, "")
        name_mcap_str = (names or {}).get(sym, "")
        if " · " in name_mcap_str:
            _name_part, _mcap_part = name_mcap_str.split(" · ", 1)
        else:
            _name_part, _mcap_part = name_mcap_str, ""
        liq = f.get("liq_tag", "")
        _mcap_liq = r" \| ".join(p for p in [_mcap_part, liq] if p)
        _label_lines = [p for p in [_name_part, _mcap_liq, lbl] if p]
        _meta = "<br>".join(_label_lines)
        rows.append(
            f"| [{sym}]({tv}) "
            f"| {_meta} "
            f"| {f['consec_weeks']}w "
            f"| {pvz} "
            f"| {zl_w} "
            f"| {zl_p} "
            f"| {ds}{f['day_chg']:.2f}% "
            f"| {f['close']:.2f} "
            f"| {sqz} "
            f"| {cl} {em} |"
        )
    return hdr + rows


def build_markdown(
    findings: list[dict],
    circuit: dict[str, tuple],
    names: dict[str, str] | None = None,
) -> str:
    lines = [
        f"# NSE Weekly ZL Scan — {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        _static_header(),
        f"## UPTREND START — {len(findings)} stocks",
        "",
    ]
    if findings:
        lines += _table_rows(findings, circuit, names)
        lines += ["", "```", ",".join(f"NSE:{f['symbol']}" for f in findings), "```"]
    else:
        lines.append("*No uptrend start signals today.*")

    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


def print_results(findings: list[dict]) -> None:
    print(f"\n{'='*75}")
    print(f"  NSE Weekly ZL Scanner  |  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Uptrend Start signals: {len(findings)}")
    print(f"{'='*75}")
    if findings:
        print()
        for f in sorted(findings, key=_sort_key):
            ds = "+" if f["day_chg"] >= 0 else ""
            zp = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
            sqz = f"sqz:{f['sqz_weeks']}w" if f["sqz_on"] else "sqz:—"
            print(
                f"  {f['symbol']:<18}  {f['close']:>9.2f}  "
                f"consec:{f['consec_weeks']}w  pvz:{f['price_vs_zl']:<5}  "
                f"day:{ds}{f['day_chg']:.1f}%  {sqz}  zl:{f['zl_weeks']}w {zp}"
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

    dated_file = os.path.join(SCANS_DIR, f"weekly_zl_scans_{TODAY}.md")
    names = get_names([f["symbol"] for f in findings])
    md = build_markdown(findings, circuit, names)
    with open(MD_FILE, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(dated_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  Saved -> {MD_FILE}")
    print(f"  Saved -> {dated_file}")


if __name__ == "__main__":
    main()
