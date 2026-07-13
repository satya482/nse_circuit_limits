#!/usr/bin/env python3
"""
NSE RS Leadership Scanner
Mirrors pine_scripts/Satya RS Relative Leadership.txt: fires when a stock's
Relative Performance % vs NIFTY MIDSML 400 is non-negative AND its EMA is
rising, on the bar these two conditions first align together (combined cross).
Run after 4:05 PM IST on trading days (after run_fetch_data.ps1).
"""

import sys
import os
import json
from math import nan, isnan
from datetime import datetime, timezone, timedelta

import pandas as pd
from tradingview_screener import Query, col

from ohlc_db import load_ohlc_many, get_names, liq_tag, cmf_tag, deliv_tag
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "rs_leadership_scans")
_LABELS_FILE = os.path.join(REPO_DIR, "tools", "stock_labels.json")

IST = timezone(timedelta(hours=5, minutes=30))
TODAY = datetime.now(IST).strftime("%Y-%m-%d")
MD_LATEST = os.path.join(SCANS_DIR, "rs_leadership_latest.md")
MD_DATED = os.path.join(SCANS_DIR, f"rs_leadership_{TODAY}.md")

MC_LOW = 8_000 * 1_00_00_000  # 8B INR = 800 Cr
MC_HIGH = 5_00_000 * 1_00_00_000  # 5T INR = 5 lakh Cr
BENCH_SYM = "NIFTY MIDSML 400"

RS_EMA_LONG_LEN = 9
RS_EMA_SHORT_LEN = 5
PERF_LOOKBACK = 9
PERF_SMOOTH = 5


def _load_labels() -> dict:
    if not os.path.exists(_LABELS_FILE):
        return {}
    with open(_LABELS_FILE, encoding="utf-8") as fh:
        return json.loads(fh.read())


_LABELS: dict = _load_labels()


# ── Indicators ────────────────────────────────────────────────────────────────


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def _zlema(s: pd.Series, n: int) -> pd.Series:
    e = _ema(s, n)
    return 2 * e - _ema(e, n)


def _bb_kc_squeeze(df: pd.DataFrame) -> bool:
    """True if BB(20,2.0,SMA) is fully inside KC(20,1.5,SMA ATR) on the last bar."""
    if len(df) < 21:
        return False
    c = df["close"].astype(float)
    h = df["high"].astype(float)
    l = df["low"].astype(float)
    bb_basis = c.rolling(20).mean()
    bb_std = c.rolling(20).std()
    bb_upper = bb_basis + 2.0 * bb_std
    bb_lower = bb_basis - 2.0 * bb_std
    tr = pd.concat([h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1).max(
        axis=1
    )
    kc_atr = tr.rolling(20).mean()
    kc_basis = c.rolling(20).mean()
    kc_upper = kc_basis + 1.5 * kc_atr
    kc_lower = kc_basis - 1.5 * kc_atr
    return bool(
        bb_upper.iloc[-1] < kc_upper.iloc[-1] and bb_lower.iloc[-1] > kc_lower.iloc[-1]
    )


# ── Core signal ───────────────────────────────────────────────────────────────


def _rel_perf_series(
    stock_close: pd.Series, bench_close: pd.Series
) -> tuple[pd.Series, pd.Series]:
    """Aligned (rel_perf, rel_perf_ema) over the overlap of the two series."""
    bench_aligned = bench_close.reindex(stock_close.index)
    valid = bench_aligned.notna()
    sc = stock_close[valid]
    bc = bench_aligned[valid]
    stock_ret = sc / sc.shift(PERF_LOOKBACK)
    bench_ret = bc / bc.shift(PERF_LOOKBACK)
    rel_perf = ((stock_ret / bench_ret) - 1) * 100
    rel_perf_ema = rel_perf.ewm(span=PERF_SMOOTH, adjust=False).mean()
    return rel_perf, rel_perf_ema


def _rs_leadership_signal(
    df: pd.DataFrame, bench: pd.Series
) -> tuple[bool, float, float]:
    """
    (signal, rel_perf_today, rel_perf_ema_today)

    signal = combined cross: (rel_perf>=0 AND rel_perf_ema rising) true today,
    NOT both true yesterday. Returns (False, nan, nan) on insufficient data.
    """
    min_bars = PERF_LOOKBACK + PERF_SMOOTH + 3
    if len(df) < min_bars:
        return False, nan, nan

    stock_close = df.set_index("date")["close"].astype(float)
    rel_perf, rel_perf_ema = _rel_perf_series(stock_close, bench)

    valid_count = rel_perf_ema.notna().sum()
    if valid_count < 3:
        return False, nan, nan

    rel_perf = rel_perf.dropna()
    rel_perf_ema = rel_perf_ema.dropna()
    if len(rel_perf) < 2 or len(rel_perf_ema) < 2:
        return False, nan, nan

    perf_positive = rel_perf >= 0
    ema_rising = rel_perf_ema > rel_perf_ema.shift(1)

    if len(ema_rising.dropna()) < 2:
        return False, nan, nan

    combined = perf_positive & ema_rising
    combined = combined.dropna()
    if len(combined) < 2:
        return False, nan, nan

    combined_today = bool(combined.iloc[-1])
    combined_yesterday = bool(combined.iloc[-2])
    signal = combined_today and not combined_yesterday

    return signal, round(float(rel_perf.iloc[-1]), 2), round(float(rel_perf_ema.iloc[-1]), 2)


def _leadership_score(df: pd.DataFrame, bench: pd.Series) -> tuple[int, str]:
    """(score 0-5, rs_state) mirroring the .txt's leadershipScore formula."""
    if len(df) < RS_EMA_LONG_LEN + 3:
        return 0, "weak"

    stock_close = df.set_index("date")["close"].astype(float)
    bench_aligned = bench.reindex(stock_close.index)
    valid = bench_aligned.notna()
    if valid.sum() < RS_EMA_LONG_LEN + 3:
        return 0, "weak"

    sc = stock_close[valid]
    bc = bench_aligned[valid]
    rs_line = (sc / bc) * 1000
    rs_ema_long = _ema(rs_line, RS_EMA_LONG_LEN)
    rs_ema_short = _ema(rs_line, RS_EMA_SHORT_LEN)

    rel_perf, _ = _rel_perf_series(stock_close, bench)
    rel_perf = rel_perf.reindex(rs_line.index)

    rs_above_ema = bool(rs_line.iloc[-1] > rs_ema_long.iloc[-1])
    short_rs_bullish = bool(rs_ema_short.iloc[-1] > rs_ema_long.iloc[-1])
    rs_ema_rising = bool(rs_ema_long.iloc[-1] > rs_ema_long.iloc[-2])
    outperforming = bool(rel_perf.iloc[-1] > 0) if not pd.isna(rel_perf.iloc[-1]) else False
    performance_rising = (
        bool(rel_perf.iloc[-1] > rel_perf.iloc[-2])
        if not pd.isna(rel_perf.iloc[-1]) and not pd.isna(rel_perf.iloc[-2])
        else False
    )

    score = sum(
        [rs_above_ema, short_rs_bullish, rs_ema_rising, outperforming, performance_rising]
    )

    now_strong = rs_above_ema
    was_strong = bool(rs_line.iloc[-2] > rs_ema_long.iloc[-2])
    if now_strong and not was_strong:
        rs_state = "transition"
    elif now_strong:
        rs_state = "strong"
    else:
        rs_state = "weak"

    return score, rs_state


# ── Watchlist ─────────────────────────────────────────────────────────────────


def get_watchlist() -> list[str]:
    """TV screener: NSE common equity passing price/MCap/EMA/notional filters.
    Same filters as rs_highline_scanner.get_watchlist()."""
    _, df = (
        Query()
        .set_markets("india")
        .select("name", "close", "market_cap_basic", "Perf.W")
        .where(
            col("exchange") == "NSE",
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("close") > 20,
            col("Perf.W") > 3,
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
            col("close") > col("EMA10"),
            col("close") > col("EMA20"),
            col("Value.Traded") > 200e6,
        )
        .limit(2000)
        .get_scanner_data()
    )
    return df["name"].tolist()


# ── Circuit limits ────────────────────────────────────────────────────────────

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


def get_circuit_limits() -> dict[str, tuple[str, str]]:
    import csv

    nse_csv = next((p for p in _NSE_CSV_PATHS if os.path.exists(p)), None)
    if not nse_csv:
        return {}
    try:
        latest: dict[str, dict] = {}
        with open(nse_csv, encoding="utf-8-sig") as fh:
            for raw in csv.DictReader(fh):
                row = {k.strip(): v.strip() for k, v in raw.items()}
                sym = row.get("SYMBOL", "")
                dte = row.get("EFFECTIVE DATE", "")
                frm = row.get("FROM", "")
                to = row.get("TO", "")
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


# ── Per-stock analysis ────────────────────────────────────────────────────────


def analyse(symbol: str, df: pd.DataFrame, bench: pd.Series | None) -> dict | None:
    try:
        if df is None or len(df) < 30:
            return None
        if bench is None:
            return None

        signal, rel_perf, rel_perf_ema = _rs_leadership_signal(df, bench)
        if not signal:
            return None

        score, rs_state = _leadership_score(df, bench)

        c = df["close"].astype(float)
        zl25 = _zlema(c, 25)
        zl_rising = bool(zl25.iloc[-1] > zl25.iloc[-2])

        curr_close = float(c.iloc[-1])
        prev_close = float(c.iloc[-2])
        day_chg = (curr_close - prev_close) / prev_close * 100

        squeeze = _bb_kc_squeeze(df)

        return {
            "symbol": symbol,
            "close": curr_close,
            "day_chg": round(day_chg, 2),
            "rel_perf": rel_perf,
            "rel_perf_ema": rel_perf_ema,
            "score": score,
            "rs_state": rs_state,
            "zl_rising": zl_rising,
            "squeeze": squeeze,
            "liq_tag": liq_tag(df),
            "cmf_tag": cmf_tag(df),
            "deliv_tag": deliv_tag(symbol),
        }
    except Exception:
        return None


# ── Markdown output ───────────────────────────────────────────────────────────

_RS_EMOJI = {"transition": "\U0001f504", "strong": "↑", "weak": "↓"}

_HDR = [
    "| Symbol | Name | Close | 1D% | RelPerf% | PerfEMA | Score | RS | ZL | Sqz | Liq |",
    "|--------|------|------:|----:|---------:|--------:|------:|:--:|:--:|:---:|-----|",
]


def _row(f: dict, circuit: dict, names: dict[str, str]) -> str:
    sym = f["symbol"]
    tv = f"https://in.tradingview.com/chart/?symbol=NSE:{sym}"
    cl, em = circuit.get(sym, ("20%", ""))
    circuit_cell = f"{cl} {em}".strip()

    name_cell = _LABELS.get(sym, "")

    zl_arrow = "↑" if f["zl_rising"] else "↓"
    ds = "+" if f["day_chg"] >= 0 else ""
    rp = "+" if f["rel_perf"] >= 0 else ""
    rs_icon = _RS_EMOJI.get(f["rs_state"], "↓")
    sqz = "●" if f["squeeze"] else "—"
    extras = [t for t in (f.get("cmf_tag", ""), f.get("deliv_tag", "")) if t]
    sym_cell = f"[{sym}]({tv}) [{circuit_cell}]" + (
        f"<br><sub>{' · '.join(extras)}</sub>" if extras else ""
    )

    return (
        f"| {sym_cell} "
        f"| {name_cell} "
        f"| {f['close']:.2f} "
        f"| {ds}{f['day_chg']:.2f}% "
        f"| {rp}{f['rel_perf']:.2f}% "
        f"| {f['rel_perf_ema']:.2f} "
        f"| {f['score']}/5 "
        f"| {rs_icon} "
        f"| {zl_arrow} "
        f"| {sqz} "
        f"| {f['liq_tag']} |"
    )


def build_markdown(findings: list[dict], circuit: dict, names: dict[str, str]) -> str:
    sorted_f = sorted(findings, key=lambda x: (-x["score"], -x["rel_perf"]))
    lines = [
        f"## RS Leadership — {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        "### Scan definition",
        "| Filter | Value |",
        "|--------|-------|",
        "| Exchange | NSE common equity |",
        "| Price | > ₹20 |",
        "| 1W change | > 3% |",
        "| Market cap | ₹800 Cr – ₹5 Lakh Cr |",
        "| EMA10 / EMA20 | price above both |",
        "| Notional 10D | > ₹20 Cr/day |",
        "| Signal | Combined cross: RelPerf%>=0 AND its EMA rising, first alignment |",
        "| Params | RS EMA Length=9, Short RS EMA=5, Perf Lookback=9, Perf Smoothing=5 |",
        "| Benchmark | NIFTY MIDSML 400 (no trend filter applied) |",
        "| Sort | Leadership score desc, then RelPerf% desc |",
        "",
        "---",
        "",
        f"**{len(findings)} signal{'s' if len(findings) != 1 else ''} "
        f"— RS leadership combined cross today**",
        "",
        "```",
        ",".join(f"NSE:{f['symbol']}" for f in sorted_f),
        "```",
        "",
    ]

    if sorted_f:
        lines += _HDR + [_row(f, circuit, names) for f in sorted_f]
        lines += ["", "```", ",".join(f"NSE:{f['symbol']}" for f in sorted_f), "```"]
    else:
        lines.append("*No signals.*")

    lines.append("")
    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


# ── Main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nFetching watchlist from TradingView screener...")
    watchlist = get_watchlist()
    print(f"  {len(watchlist)} stocks after screener filters")

    print(f"\nLoading OHLCV + benchmark ({BENCH_SYM}) from SQLite...")
    syms_to_load = watchlist + [BENCH_SYM]
    all_data = load_ohlc_many(syms_to_load, lookback=400)

    bench_df = all_data.pop(BENCH_SYM, None)
    bench_series: pd.Series | None = (
        bench_df.set_index("date")["close"].astype(float)
        if bench_df is not None
        else None
    )
    if bench_series is None:
        print(f"  WARNING: {BENCH_SYM} not in SQLite — RS signal unavailable")

    print(f"  Loaded {len(all_data)} equity stocks")

    print("\nFetching circuit limits...")
    circuit = get_circuit_limits()

    print(f"\nScanning {len(all_data)} stocks...")
    findings: list[dict] = []
    for i, (sym, df_raw) in enumerate(all_data.items(), 1):
        print(f"  {sym:<20} ({i}/{len(all_data)})   ", end="\r")
        result = analyse(sym, df_raw, bench_series)
        if result:
            findings.append(result)
    print()

    print(f"\n  {len(findings)} RS leadership crosses found")

    names = get_names([f["symbol"] for f in findings])
    md = build_markdown(findings, circuit, names)

    with open(MD_LATEST, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(MD_DATED, "w", encoding="utf-8") as fh:
        fh.write(md)

    print(f"  Saved → {MD_LATEST}")
    print(f"  Saved → {MD_DATED}")


if __name__ == "__main__":
    main()
