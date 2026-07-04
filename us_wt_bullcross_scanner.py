#!/usr/bin/env python3
"""
US WaveTrend Bull Cross Scanner
Run after the existing US data pipeline (fetch_us_data.py @ 4:40 PM IST,
us_zl_squeeze_scanner.py @ 4:50 PM IST) — this scanner runs last, ~5:00 PM IST.

Universe: NYSE + NASDAQ common equity, MCap $300M-$10B, price > $5,
          avg 10d vol > 300K (matches fetch_us_data.py's backfill universe exactly —
          lookups miss for any symbol outside this range).
          No RS filter — WT captures oversold reversals before RS turns positive.

Signal hierarchy (wt_signal_rank) — external contract, never renumbered:
  +5  BULL_OS_PPV    - deep oversold cross + Pocket Pivot Volume [strongest]
  +4  BULL_ANY_PPV   - any cross + Pocket Pivot Volume
  +3  BULL_OVERSOLD  - deep oversold cross (wt2 <= -60)
  +2  BULL_OS_L2     - soft oversold cross (wt2 <= -53)
  +1  BULL_ANY_MID   - mid-range cross (WT2 > -53, no PPV)

Output: us_wt_scans/us_wt_bullcross_latest.md
        us_wt_scans/us_wt_bullcross_YYYY-MM-DD.md
        us_wt_scans/us_wt_bullcross_dashboard.html
"""

import sys
import os
from datetime import datetime, timezone, timedelta

import pandas as pd

from tradingview_screener import Query, col

from us_ohlc_db import load_ohlc_many
from wavetrend_scanner import WaveTrendCalculator
from disclaimer import (
    SEBI_MD_HEADER,
    SEBI_MD_FOOTER,
    SEBI_HTML_BANNER,
    SEBI_HTML_FOOTER,
)


sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "us_wt_scans")
IST = timezone(timedelta(hours=5, minutes=30))
TODAY = datetime.now(IST).strftime("%Y-%m-%d")
MD_LATEST = os.path.join(SCANS_DIR, "us_wt_bullcross_latest.md")
MD_DATED = os.path.join(SCANS_DIR, f"us_wt_bullcross_{TODAY}.md")
HTML_DASHBOARD = os.path.join(SCANS_DIR, "us_wt_bullcross_dashboard.html")

MC_LOW = 300_000_000  # $300M
MC_HIGH = 10_000_000_000  # $10B
MIN_RANK = 1
ZL_TURN_CAP = 60
BENCH_SYM = "SPY"
RS_SCALE = 100  # matches us_zl_squeeze_scanner.py convention (not NSE's x1000)
RVOL_FLAG = 8.0
SS_LOWMULT = 0.995


# -- Indicators ---------------------------------------------------------------


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


def _zl25_turn_stats(zl25: pd.Series, closes: pd.Series) -> tuple[int, float]:
    n = len(zl25)
    limit = max(2, n - ZL_TURN_CAP)
    for i in range(n - 1, limit - 1, -1):
        if zl25.iloc[i] > zl25.iloc[i - 1] and zl25.iloc[i - 1] <= zl25.iloc[i - 2]:
            bars = (n - 1) - i + 1
            pct = (closes.iloc[-1] / closes.iloc[i - 1] - 1) * 100
            return bars, round(pct, 2)
    cap_idx = max(0, n - ZL_TURN_CAP)
    return ZL_TURN_CAP, round((closes.iloc[-1] / closes.iloc[cap_idx] - 1) * 100, 2)


def _rs_state(df: pd.DataFrame, bench_series: pd.Series | None) -> str:
    """Returns 'transition' (weak->strong flip today), 'strong', or 'weak'."""
    if bench_series is None or len(bench_series) < 11:
        return "weak"
    try:
        stock_close = df.set_index("date")["close"].astype(float)
        bench = bench_series.reindex(stock_close.index)
        valid = bench.notna()
        if valid.sum() < 11:
            return "weak"
        rs = (stock_close[valid] / bench[valid]) * RS_SCALE
        rs_ema9 = rs.ewm(span=9, adjust=False).mean()
        now_strong = bool(rs.iloc[-1] > rs_ema9.iloc[-1])
        was_weak = bool(rs.iloc[-2] < rs_ema9.iloc[-2])
        if was_weak and now_strong:
            return "transition"
        return "strong" if now_strong else "weak"
    except Exception:
        return "weak"


def _compute_rs_pct_map(all_data: dict, bench_series: pd.Series) -> dict[str, float]:
    """IBD-style RS percentile rank vs SPY. RS line = (close/SPY_close)*RS_SCALE;
    weighted 3m/6m/9m/12m return. Scale cancels out in the ratio, so RS_SCALE
    doesn't affect the resulting percentiles."""
    WINDOWS = [63, 126, 189, 252]
    WEIGHTS = [0.4, 0.2, 0.2, 0.2]
    scores: dict[str, float] = {}
    for sym, df in all_data.items():
        if df is None or len(df) < 253:
            continue
        try:
            stock_c = df.set_index("date")["close"].astype(float)
            bench = bench_series.reindex(stock_c.index)
            valid = bench.notna()
            if valid.sum() < 253:
                continue
            rs_line = (stock_c[valid] / bench[valid]) * RS_SCALE
            score = sum(
                wt * (rs_line.iloc[-1] / rs_line.iloc[-w] - 1)
                for w, wt in zip(WINDOWS, WEIGHTS)
                if len(rs_line) >= w + 1
            )
            scores[sym] = score
        except Exception:
            continue
    if not scores:
        return {}
    s = pd.Series(scores)
    pct = s.rank(pct=True) * 100
    return pct.round(1).to_dict()


def _cavgc(c: pd.Series, length: int = 10) -> tuple[float, bool]:
    """Close / EMA(close, length) ratio and whether it is rising."""
    avg = c.ewm(span=length, adjust=False).mean()
    ratio = c / avg
    if pd.isna(ratio.iloc[-1]):
        return 1.0, False
    return float(ratio.iloc[-1]), bool(ratio.iloc[-1] > ratio.iloc[-2])


def _rvol_ss(df: pd.DataFrame) -> tuple[float, bool]:
    """RVOL = today's volume / prior-20d avg volume; SS = gapped up and held."""
    vol = df["volume"].astype(float)
    avg_vol = vol.iloc[-21:-1].mean()
    rvol = float(vol.iloc[-1] / avg_vol) if avg_vol > 0 else 0.0
    today_open = float(df["open"].iloc[-1])
    today_low = float(df["low"].iloc[-1])
    prev_close = float(df["close"].iloc[-2])
    strong_start = today_open > prev_close and today_low >= prev_close * SS_LOWMULT
    return rvol, strong_start


def _earliness(
    rs_state: str,
    zl_days: int,
    cavgc: float,
    cavgc_rising: bool,
    squeeze: bool,
) -> float:
    """Earliness score 0-100: how close to the START of a momentum move.
    Squeeze(40) + RS-transition(30) + ZL freshness(0-20) + C/AvgC freshness(0-10)."""
    score = 0.0
    if squeeze:
        score += 40
    if rs_state == "transition":
        score += 30
    score += max(0, 20 - zl_days)
    if cavgc_rising and 1.0 < cavgc < 1.015:
        score += 10
    elif cavgc_rising and cavgc < 1.03:
        score += 5
    return round(score, 1)


def analyse(
    symbol: str,
    df_raw: pd.DataFrame,
    calc: WaveTrendCalculator,
    bench_series: pd.Series | None = None,
    rs_pct: float = 50.0,
) -> dict | None:
    try:
        if df_raw is None or len(df_raw) < 83:  # WaveTrendCalculator._min_bars floor
            return None

        sig = calc.get_signal(df_raw)
        if sig.wt_signal_rank < MIN_RANK:
            return None

        rs = _rs_state(df_raw, bench_series)

        c = df_raw["close"].astype(float)
        zl25 = _zlema(c, 25)
        zl_rising = bool(zl25.iloc[-1] > zl25.iloc[-2])
        zl_days, zl_pct = _zl25_turn_stats(zl25, c)

        curr_close = float(c.iloc[-1])
        prev_close = float(c.iloc[-2])
        day_chg = (curr_close - prev_close) / prev_close * 100

        cavgc_val, cavgc_rising = _cavgc(c)
        rvol, strong_start = _rvol_ss(df_raw)
        squeeze = _bb_kc_squeeze(df_raw)
        earliness = _earliness(rs, zl_days, cavgc_val, cavgc_rising, squeeze)

        return {
            "symbol": symbol,
            "wt_signal": sig.wt_signal,
            "wt_rank": sig.wt_signal_rank,
            "wt1": round(sig.wt1, 2),
            "wt2": round(sig.wt2, 2),
            "wt_is_ppv": sig.wt_is_ppv,
            "zl_rising": zl_rising,
            "zl_days": zl_days,
            "zl_pct": zl_pct,
            "squeeze": squeeze,
            "rs_state": rs,
            "rs_pct": rs_pct,
            "cavgc": round(cavgc_val, 4),
            "cavgc_rising": cavgc_rising,
            "rvol": round(rvol, 2),
            "strong_start": strong_start,
            "earliness": earliness,
            "close": curr_close,
            "day_chg": day_chg,
        }
    except Exception:
        return None


# -- Markdown output ----------------------------------------------------------


_RANK_EMOJI = {5: "🔥", 4: "⚡", 3: "🟢", 2: "🟡", 1: "📈"}
_RS_EMOJI = {"transition": "🔄", "strong": "↑", "weak": "↓"}
_CATEGORIES = [
    ("🔥", "MAJOR", "PPV confirmed", [5, 4]),
    ("🟢", "OVERSOLD", "reversal from -53/-60", [3, 2]),
    ("📈", "MID-RANGE", "any cross, WT2 > -53, no PPV", [1]),
]

_HDR = [
    "| Symbol | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg |",
    "|--------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|",
]


def _row(f: dict) -> str:
    sym = f["symbol"]
    tv = f"https://www.tradingview.com/chart/?symbol={sym}"
    zl_d = f"{f['zl_days']}d+" if f["zl_days"] >= ZL_TURN_CAP else f"{f['zl_days']}d"
    zl_arrow = "↑" if f["zl_rising"] else "↓"
    zl_cell = f"{zl_arrow}{zl_d}"
    zl_p = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
    ds = "+" if f["day_chg"] >= 0 else ""
    rs_emoji = _RS_EMOJI.get(f.get("rs_state", "weak"), "↓")
    rs_cell = f"{rs_emoji}{f.get('rs_pct', 50.0):.0f}"
    cavgc_arrow = "↑" if f.get("cavgc_rising", False) else "↓"
    cavgc_str = f"{cavgc_arrow}{f.get('cavgc', 1.0):.3f}"
    erly = f"{f.get('earliness', 0.0):.0f}"
    sqz, ppv = f["squeeze"], f["wt_is_ppv"]
    flags = "SQ·PV" if sqz and ppv else "SQ" if sqz else "PV" if ppv else "—"
    wt_cell = f"{f['wt1']}/{f['wt2']}"
    emoji = _RANK_EMOJI.get(f["wt_rank"], "")
    return (
        f"| [{sym}]({tv}) "
        f"| {emoji} {f['wt_signal']} "
        f"| {erly} "
        f"| {rs_cell} "
        f"| {cavgc_str} "
        f"| {zl_cell} "
        f"| {flags} "
        f"| {zl_p} "
        f"| {wt_cell} "
        f"| {ds}{f['day_chg']:.2f}% |"
    )


def build_markdown(findings: list[dict]) -> str:
    sorted_f = sorted(findings, key=lambda x: (-x["wt_rank"], -x["earliness"]))
    rank_groups: dict[int, list] = {}
    for f in sorted_f:
        rank_groups.setdefault(f["wt_rank"], []).append(f)
    sqz_count = sum(1 for f in findings if f["squeeze"])

    lines = [
        f"# US WaveTrend Bull Cross Scan — {TODAY}",
        f"*Generated {datetime.now(IST).strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        "### Scan definition",
        "| Filter | Value |",
        "|--------|-------|",
        "| Exchange | NYSE + NASDAQ common equity |",
        "| Price | > $5 |",
        "| Market cap | $300M - $10B |",
        "| Avg 10d Volume | > 300K |",
        "| RS benchmark | SPY (x100 scale) |",
        "| RS filter | None - WT captures pre-RS-turn reversals |",
        "| RS | transition/strong/weak state + IBD percentile vs SPY |",
        "| C/AvgC | Close / EMA(10) ratio - rising = fresh momentum |",
        "| Erly | Squeeze(40)+RS-transition(30)+ZL freshness(0-20)+C/AvgC freshness(0-10) |",
        "| ZL | ZLEMA25 direction + days since turn |",
        "| Flags | SQ=squeeze  PV=pocket-pivot  SQ·PV=both  —=neither |",
        "| WT | WT1/WT2 oscillator values |",
        "| Min rank | Any bull cross (rank >= 1) |",
        "",
        "---",
        "",
        f"**Total bull crosses today: {len(findings)}** - {sqz_count} inside active squeeze",
        "",
    ]

    sqz_breaks = [f for f in sorted_f if f["squeeze"]]
    if sqz_breaks:
        lines.append(
            f"### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze ({len(sqz_breaks)})"
        )
        lines += _HDR + [_row(f) for f in sqz_breaks]
        lines.append("")
        lines.append("---")
        lines.append("")

    sqz_syms = {f["symbol"] for f in sqz_breaks}
    for emoji, cat_name, cat_desc, ranks in _CATEGORIES:
        group = [
            f
            for r in ranks
            for f in rank_groups.get(r, [])
            if f["symbol"] not in sqz_syms
        ]
        group.sort(key=lambda x: (-x["wt_rank"], -x["earliness"]))
        lines.append(f"### {emoji} {cat_name} — {cat_desc} ({len(group)})")
        if group:
            lines += _HDR + [_row(f) for f in group]
        else:
            lines.append("*No signals.*")
        lines.append("")

    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


# -- HTML output ---------------------------------------------------------------


_HTML_STYLE = """
body{background:#0a0e14;color:#e8edf3;font-family:'Space Grotesk',system-ui,sans-serif;padding:20px;line-height:1.4}
h1{font-size:20px;margin-bottom:4px}
.meta{color:#6b7785;font-size:12px;margin-bottom:16px}
h2{font-size:15px;margin:24px 0 8px;color:#e8edf3}
table{border-collapse:collapse;width:100%;margin-bottom:12px;font-size:13px}
th,td{padding:6px 10px;border-bottom:1px solid #1c2530;text-align:left}
th{color:#6b7785;font-weight:600}
a{color:#4d9de0;text-decoration:none}
.empty{color:#6b7785;font-style:italic}
"""


def _html_table(rows: list[dict]) -> str:
    if not rows:
        return '<p class="empty">No signals in this category.</p>'
    head = (
        "<tr><th>Symbol</th><th>Signal</th><th>Erly</th><th>RS</th><th>C/AvgC</th>"
        "<th>ZL</th><th>Flags</th><th>ZL Chg%</th><th>WT</th><th>Day Chg</th></tr>"
    )
    body = []
    for f in rows:
        sym = f["symbol"]
        tv = f"https://www.tradingview.com/chart/?symbol={sym}"
        zl_d = f"{f['zl_days']}d+" if f["zl_days"] >= ZL_TURN_CAP else f"{f['zl_days']}d"
        zl_arrow = "↑" if f["zl_rising"] else "↓"
        zl_p = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
        ds = "+" if f["day_chg"] >= 0 else ""
        rs_emoji = _RS_EMOJI.get(f.get("rs_state", "weak"), "↓")
        cavgc_arrow = "↑" if f.get("cavgc_rising", False) else "↓"
        sqz, ppv = f["squeeze"], f["wt_is_ppv"]
        flags = "SQ·PV" if sqz and ppv else "SQ" if sqz else "PV" if ppv else "—"
        emoji = _RANK_EMOJI.get(f["wt_rank"], "")
        body.append(
            "<tr>"
            f'<td><a href="{tv}">{sym}</a></td>'
            f"<td>{emoji} {f['wt_signal']}</td>"
            f"<td>{f.get('earliness', 0.0):.0f}</td>"
            f"<td>{rs_emoji}{f.get('rs_pct', 50.0):.0f}</td>"
            f"<td>{cavgc_arrow}{f.get('cavgc', 1.0):.3f}</td>"
            f"<td>{zl_arrow}{zl_d}</td>"
            f"<td>{flags}</td>"
            f"<td>{zl_p}</td>"
            f"<td>{f['wt1']}/{f['wt2']}</td>"
            f"<td>{ds}{f['day_chg']:.2f}%</td>"
            "</tr>"
        )
    return f"<table>{head}{''.join(body)}</table>"


def build_html_dashboard(findings: list[dict]) -> str:
    sorted_f = sorted(findings, key=lambda x: (-x["wt_rank"], -x["earliness"]))
    rank_groups: dict[int, list] = {}
    for f in sorted_f:
        rank_groups.setdefault(f["wt_rank"], []).append(f)

    sqz_breaks = [f for f in sorted_f if f["squeeze"]]
    sqz_syms = {f["symbol"] for f in sqz_breaks}

    sections = []
    if sqz_breaks:
        sections.append(f"<h2>🎯 Squeeze Breakout ({len(sqz_breaks)})</h2>")
        sections.append(_html_table(sqz_breaks))

    for emoji, cat_name, cat_desc, ranks in _CATEGORIES:
        group = [
            f for r in ranks for f in rank_groups.get(r, []) if f["symbol"] not in sqz_syms
        ]
        group.sort(key=lambda x: (-x["wt_rank"], -x["earliness"]))
        sections.append(f"<h2>{emoji} {cat_name} — {cat_desc} ({len(group)})</h2>")
        sections.append(_html_table(group))

    return (
        f"<!doctype html><html><head><meta charset='utf-8'>"
        f"<title>US WaveTrend Bull Cross — {TODAY}</title>"
        f"<style>{_HTML_STYLE}</style></head><body>"
        f"{SEBI_HTML_BANNER}"
        f"<h1>US WaveTrend Bull Cross Scan — {TODAY}</h1>"
        f"<div class='meta'>Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST · "
        f"{len(findings)} total signals</div>"
        f"{''.join(sections)}"
        f"{SEBI_HTML_FOOTER}"
        f"</body></html>"
    )


# -- Watchlist & main ---------------------------------------------------------


def get_watchlist() -> list[str]:
    """Mirrors us_zl_squeeze_scanner.py's query exactly - must match fetch_us_data.py's
    backfill universe or lookups return None for out-of-range symbols."""
    _, df = (
        Query()
        .set_markets("america")
        .select("name", "close")
        .where(
            col("exchange").isin(["NASDAQ", "NYSE"]),
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("close") > 5,
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
            col("average_volume_10d_calc") > 300_000,
        )
        .limit(3000)
        .get_scanner_data()
    )
    return df["name"].tolist()


def print_results(findings: list[dict]) -> None:
    print(f"\n{'='*70}")
    print(f"  US WaveTrend Bull Cross Scanner  |  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Total bull crosses: {len(findings)}")
    print(f"{'='*70}")
    for emoji, cat_name, _cat_desc, ranks in _CATEGORIES:
        group = [f for f in findings if f["wt_rank"] in ranks]
        if not group:
            continue
        group.sort(key=lambda x: (-x["wt_rank"], -x["earliness"]))
        print(f"\n  -- {emoji} {cat_name} ({len(group)}) --")
        for f in group:
            ds = "+" if f["day_chg"] >= 0 else ""
            zl = "ZL^" if f["zl_rising"] else "ZLv"
            sqz = "SQZ" if f["squeeze"] else "   "
            ppv = "PPV" if f["wt_is_ppv"] else "   "
            print(
                f"  {f['symbol']:<8} {f['close']:>9.2f}  "
                f"wt1:{f['wt1']:>7.2f}  {zl} {sqz} {ppv}  "
                f"day:{ds}{f['day_chg']:.1f}%"
            )
    print()


def main():
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nLoading SPY benchmark from DB...")
    bench_dict = load_ohlc_many([BENCH_SYM], lookback=400)
    bench_df = bench_dict.get(BENCH_SYM)
    if bench_df is None:
        print("  ERROR: SPY not in DB. Run fetch_us_data.py first.")
        return
    bench_series = bench_df.set_index("date")["close"].astype(float)
    print(f"  SPY: {len(bench_series)} days")

    print("\nFetching watchlist from TradingView screener (US)...")
    watchlist = get_watchlist()
    print(f"  {len(watchlist)} stocks")

    print("\nLoading OHLCV from SQLite (batch)...")
    all_data = load_ohlc_many(watchlist, lookback=400)
    print(f"  Loaded {len(all_data)} stocks")

    print("\nComputing RS percentile ranks across universe...")
    rs_pct_map = _compute_rs_pct_map(all_data, bench_series)
    print(f"  RS ranks computed for {len(rs_pct_map)} stocks")

    print(f"\nScanning {len(all_data)} stocks for WaveTrend bull crosses...")
    calc = WaveTrendCalculator()
    findings = []
    for i, (sym, df_raw) in enumerate(all_data.items(), 1):
        print(f"  {sym:<12} ({i}/{len(all_data)})   ", end="\r")
        result = analyse(sym, df_raw, calc, bench_series, rs_pct=rs_pct_map.get(sym, 50.0))
        if result:
            findings.append(result)

    print_results(findings)

    md = build_markdown(findings)
    with open(MD_LATEST, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(MD_DATED, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  Saved -> {MD_LATEST}")
    print(f"  Saved -> {MD_DATED}")

    html = build_html_dashboard(findings)
    with open(HTML_DASHBOARD, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"  Saved -> {HTML_DASHBOARD}")


if __name__ == "__main__":
    main()
