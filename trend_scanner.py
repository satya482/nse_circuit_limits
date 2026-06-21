#!/usr/bin/env python3
"""
Trend Scanner — early entries in leading stocks during pullbacks.
Run after 4:05 PM IST on trading days (after run_fetch_data.ps1).

Universe: NSE common equity, EMA50>EMA100>EMA200,
          close within 30% of 52W high (leader filter),
          RS percentile >= 60 vs NIFTY MIDSML 400

Entry signals (stock pulling back, about to start next leg):
  LEADER_ZL   — ZLEMA25 touch + RS holds + volume dry-up  [strongest]
  ZL_PULLBACK — ZLEMA25 touch + RS holds
  EMA_SUPPORT — bounce from EMA50/100/200 + RS holds + green candle
  ZL_ENTRY    — ZLEMA25 touch (RS pct >= 60, short-term RS transitioning)

Entry score (0-100):
  RS percentile (35) + vol dry-up (20) + 52W proximity (20)
  + RS holds (15) + ZL freshness (10)

Sort: entry_score desc — best early entries float to top

Output: trend_scans/trend_scan_latest.md
        trend_scans/trend_scan_YYYY-MM-DD.md
"""

import csv
import json
import os
import sys
from datetime import datetime

import pandas as pd
from tradingview_screener import Query, col

from ohlc_db import load_ohlc_many
from float_gate import float_metrics, passes_hard_gate, trap_label as _trap_label

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "trend_scans")
_LABELS_FILE = os.path.join(REPO_DIR, "tools", "stock_labels.json")
_LABELS: dict = (
    json.loads(open(_LABELS_FILE, encoding="utf-8").read())
    if os.path.exists(_LABELS_FILE)
    else {}
)
TODAY = datetime.now().strftime("%Y-%m-%d")
MD_LATEST = os.path.join(SCANS_DIR, "trend_scan_latest.md")
MD_DATED = os.path.join(SCANS_DIR, f"trend_scan_{TODAY}.md")

MC_LOW = 800 * 1_00_00_000
MC_HIGH = 1_00_000 * 1_00_00_000
TOUCH_PCT = 0.015
ZL_TURN_CAP = 60
BENCH_SYM = "NIFTY MIDSML 400"
LEADER_MIN = 0.70  # close must be >= 70% of 52W high
RS_PCT_MIN = 60.0  # RS percentile floor vs benchmark
VOL_DRYUP_THRESH = 0.65  # 3-bar avg vol < 65% of 20-day avg


# ── Indicators ─────────────────────────────────────────────────────────────────


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def _zlema(s: pd.Series, n: int) -> pd.Series:
    e = _ema(s, n)
    return 2 * e - _ema(e, n)


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


def _compute_rs_pct_map(all_data: dict, bench_series: pd.Series) -> dict[str, float]:
    """IBD-style RS percentile rank vs NIFTY MIDSML 400 across full universe."""
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
            rs_line = (stock_c[valid] / bench[valid]) * 1000
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


def _rs_state(df: pd.DataFrame, bench_series: pd.Series) -> str:
    """'transition' | 'strong' | 'weak' based on RS line vs EMA9."""
    try:
        stock_c = df.set_index("date")["close"].astype(float)
        bench = bench_series.reindex(stock_c.index)
        valid = bench.notna()
        if valid.sum() < 11:
            return "weak"
        rs = (stock_c[valid] / bench[valid]) * 1000
        rs_ema9 = rs.ewm(span=9, adjust=False).mean()
        now_strong = bool(rs.iloc[-1] > rs_ema9.iloc[-1])
        was_weak = bool(rs.iloc[-2] < rs_ema9.iloc[-2])
        if was_weak and now_strong:
            return "transition"
        return "strong" if now_strong else "weak"
    except Exception:
        return "weak"


def _cavgc(c: pd.Series, length: int = 10) -> tuple[float, bool]:
    """Close / EMA(close, length) ratio and whether it is rising."""
    avg = c.ewm(span=length, adjust=False).mean()
    ratio = c / avg
    if pd.isna(ratio.iloc[-1]):
        return 1.0, False
    return float(ratio.iloc[-1]), bool(ratio.iloc[-1] > ratio.iloc[-2])


def _entry_score(
    rs_pct: float,
    vol_ratio: float,
    leader_ratio: float,
    rs_holds: bool,
    zl_days: int,
) -> float:
    """Entry quality score 0-100. High = early entry in a leading stock."""
    s = rs_pct * 0.35  # 0-35
    s += max(0.0, (1.0 - vol_ratio) * 20)  # 0-20: sellers gone
    s += max(
        0.0, (leader_ratio - LEADER_MIN) / (1.0 - LEADER_MIN) * 20
    )  # 0-20: near high
    if rs_holds:
        s += 15  # RS divergence
    s += max(0, 10 - zl_days)  # 0-10: ZL freshness
    return round(s, 1)


# ── Watchlist ──────────────────────────────────────────────────────────────────


def get_watchlist() -> tuple[list[str], dict[str, float]]:
    """EMA uptrend universe — same MCap/EMA structure as swing scanner."""
    _, df = (
        Query()
        .set_markets("india")
        .select("name", "close", "market_cap_basic", "float_shares_outstanding")
        .where(
            col("exchange") == "NSE",
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("close") > 50,
            col("EMA50") > col("EMA200"),
            col("EMA100") > col("EMA200"),
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
        )
        .limit(1000)
        .get_scanner_data()
    )
    float_map = {
        row["name"]: float(row["float_shares_outstanding"])
        for _, row in df.iterrows()
        if pd.notna(row.get("float_shares_outstanding"))
        and row["float_shares_outstanding"] > 0
    }
    return df["name"].tolist(), float_map


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


# ── Per-stock analysis ─────────────────────────────────────────────────────────


def analyse(
    symbol: str,
    df_raw: pd.DataFrame,
    bench_series: pd.Series,
    rs_pct: float = 0.0,
    float_shares: float = 0,
) -> dict | None:
    try:
        if df_raw is None or len(df_raw) < 252:
            return None

        # RS percentile pre-filter — must be established leader
        if rs_pct < RS_PCT_MIN:
            return None

        fm = float_metrics(df_raw["close"], df_raw["volume"], float_shares or None)
        if not passes_hard_gate(fm):
            return None

        c = df_raw["close"].astype(float)
        lo = df_raw["low"].astype(float)
        op = df_raw["open"].astype(float)
        vol = df_raw["volume"].astype(float)

        # EMA structure: Stage 2 uptrend
        e50 = _ema(c, 50)
        e100 = _ema(c, 100)
        e200 = _ema(c, 200)
        if not (e50.iloc[-1] > e100.iloc[-1] > e200.iloc[-1]):
            return None

        # Leader filter: within 30% of 52W high
        high_52w = c.rolling(252, min_periods=200).max()
        leader_ratio = float(c.iloc[-1] / high_52w.iloc[-1])
        if leader_ratio < LEADER_MIN:
            return None

        # RS state — does RS hold above EMA9 during the pullback?
        rs_st = _rs_state(df_raw, bench_series)
        rs_holds = rs_st in ("strong", "transition")

        # Volume dry-up: 3-bar avg volume < 65% of 20-day avg
        vol_ratio = float(vol.tail(3).mean() / vol.rolling(20).mean().iloc[-1])
        vol_dryup = vol_ratio < VOL_DRYUP_THRESH

        # ZLEMA25 — must be rising
        zl25 = _zlema(c, 25)
        zl_now, zl_prev = zl25.iloc[-1], zl25.iloc[-2]
        if not (zl_now > zl_prev):
            return None

        zl_days, zl_pct = _zl25_turn_stats(zl25, c)
        e20 = _ema(c, 20)
        e20_rising = bool(e20.iloc[-1] > e20.iloc[-2])

        curr_close = float(c.iloc[-1])
        prev_close = float(c.iloc[-2])
        curr_low = float(lo.iloc[-1])
        curr_open = float(op.iloc[-1])
        day_chg = (curr_close - prev_close) / prev_close * 100

        cavgc_val, cavgc_rising = _cavgc(c)

        # ── Entry conditions ──────────────────────────────────────────────────
        entries = []

        prev_above = prev_close > float(zl25.iloc[-2])
        touched_zl = (
            curr_low <= zl_now * (1 + TOUCH_PCT)
            and curr_low >= zl_now * (1 - TOUCH_PCT)
        ) or (curr_low <= zl_now and curr_close >= zl_now)

        if prev_above and touched_zl:
            suffix = " · EMA20 ↑" if e20_rising else ""
            if rs_holds and vol_dryup:
                entries.append(
                    (
                        "LEADER_ZL",
                        f"ZLEMA25 touch · RS holds · vol dry-up{suffix}",
                        zl_now,
                    )
                )
            elif rs_holds:
                entries.append(
                    ("ZL_PULLBACK", f"ZLEMA25 touch · RS holds{suffix}", zl_now)
                )
            else:
                entries.append(
                    ("ZL_ENTRY", f"ZLEMA25 touch · RS transitioning{suffix}", zl_now)
                )

        for level, name in [
            (float(e50.iloc[-1]), "EMA50"),
            (float(e100.iloc[-1]), "EMA100"),
            (float(e200.iloc[-1]), "EMA200"),
        ]:
            touched = curr_low <= level * (1 + TOUCH_PCT)
            bounced = curr_close > level and curr_close > curr_open
            if touched and bounced and rs_holds:
                entries.append(("EMA_SUPPORT", f"Bounce {name} · RS holds", level))

        if not entries:
            return None

        score = _entry_score(rs_pct, vol_ratio, leader_ratio, rs_holds, zl_days)

        return {
            "symbol": symbol,
            "entries": entries,
            "score": score,
            "rs_pct": rs_pct,
            "rs_state": rs_st,
            "cavgc": round(cavgc_val, 4),
            "cavgc_rising": cavgc_rising,
            "leader_pct": round(leader_ratio * 100, 1),
            "vol_ratio": round(vol_ratio, 2),
            "vol_dryup": vol_dryup,
            "zl_days": zl_days,
            "zl_pct": zl_pct,
            "day_chg": day_chg,
            "trap": _trap_label(fm),
        }

    except Exception:
        return None


# ── Markdown output ────────────────────────────────────────────────────────────

_SIG_ORDER = {"LEADER_ZL": 0, "ZL_PULLBACK": 1, "EMA_SUPPORT": 2, "ZL_ENTRY": 3}
_SIG_EMOJI = {
    "LEADER_ZL": "🏆",
    "ZL_PULLBACK": "🟢",
    "EMA_SUPPORT": "🔵",
    "ZL_ENTRY": "📈",
}
_RS_EMOJI = {"transition": "🔄", "strong": "↑", "weak": "↓"}

_HDR = [
    "| Symbol | Trap | Label | Signal | Score | RS | C/AvgC | 52W% | Vol | ZL | ZL Chg% | Day Chg | Circuit |",
    "|--------|:----:|-------|--------|------:|:--:|-------:|-----:|:---:|:--:|--------:|--------:|:-------:|",
]


def _row(f: dict, circuit: dict) -> str:
    sym = f["symbol"]
    tv = f"https://in.tradingview.com/chart/?symbol=NSE:{sym}"
    cl, em = circuit.get(sym, ("20%", ""))
    lbl = _LABELS.get(sym, "")
    tag, label, _ = min(f["entries"], key=lambda e: _SIG_ORDER.get(e[0], 9))
    sig_emoji = _SIG_EMOJI.get(tag, "")
    rs_cell = f"{_RS_EMOJI.get(f['rs_state'], '↓')}{f['rs_pct']:.0f}"
    cavgc_arrow = "↑" if f["cavgc_rising"] else "↓"
    zl_d = f"{f['zl_days']}d+" if f["zl_days"] >= ZL_TURN_CAP else f"{f['zl_days']}d"
    zl_p = f"+{f['zl_pct']:.1f}%" if f["zl_pct"] >= 0 else f"{f['zl_pct']:.1f}%"
    ds = "+" if f["day_chg"] >= 0 else ""
    vol_cell = f"{'🔵' if f['vol_dryup'] else ''}{f['vol_ratio']:.2f}x"
    return (
        f"| [{sym}]({tv}) "
        f"| {f.get('trap', 'n/a')} "
        f"| {lbl} "
        f"| {sig_emoji} {label} "
        f"| {f['score']:.0f} "
        f"| {rs_cell} "
        f"| {cavgc_arrow}{f['cavgc']:.3f} "
        f"| {f['leader_pct']:.0f}% "
        f"| {vol_cell} "
        f"| ↑{zl_d} "
        f"| {zl_p} "
        f"| {ds}{f['day_chg']:.2f}% "
        f"| {cl} {em} |"
    )


def build_markdown(findings: list[dict], circuit: dict) -> str:
    findings.sort(key=lambda x: -x["score"])
    leader_count = sum(
        1 for f in findings if any(e[0] == "LEADER_ZL" for e in f["entries"])
    )

    lines = [
        f"# Trend Scanner — {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        "### Scan definition",
        "| Filter | Value |",
        "|--------|-------|",
        "| EMA structure | EMA50 > EMA100 > EMA200 (Stage 2) |",
        "| Leader filter | Close ≥ 70% of 52W high |",
        "| RS floor | Percentile ≥ 60 vs NIFTY MIDSML 400 |",
        "| ZLEMA25 | Rising required |",
        "| Score | RS%(×0.35) + vol dry-up(20) + 52W proximity(20) + RS holds(15) + ZL fresh(10) |",
        "| Sort | Score desc — early entries in strongest leaders first |",
        "",
        "---",
        "",
        f"**Opportunities: {len(findings)}** · {leader_count} full LEADER_ZL (all 3 conditions)",
        "",
    ]

    for tag, emoji, heading in [
        ("LEADER_ZL", "🏆", "LEADER ZL — ZLEMA25 touch + RS holds + volume dry-up"),
        ("ZL_PULLBACK", "🟢", "ZL PULLBACK — ZLEMA25 touch + RS holds"),
        ("EMA_SUPPORT", "🔵", "EMA SUPPORT — EMA50/100/200 bounce + RS holds"),
        (
            "ZL_ENTRY",
            "📈",
            "ZL ENTRY — ZLEMA25 touch (RS pct ≥ 60, short-term transitioning)",
        ),
    ]:
        # Each stock appears in exactly one group (best signal)
        group = [
            f
            for f in findings
            if min(f["entries"], key=lambda e: _SIG_ORDER.get(e[0], 9))[0] == tag
        ]
        lines.append(f"### {emoji} {heading} ({len(group)})")
        if group:
            lines += _HDR + [_row(f, circuit) for f in group]
        else:
            lines.append("*No signals.*")
        lines.append("")

    return "\n".join(lines)


# ── Console output ─────────────────────────────────────────────────────────────


def print_results(findings: list[dict]) -> None:
    print(f"\n{'='*70}")
    print(f"  Trend Scanner  |  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Opportunities: {len(findings)}")
    print(f"{'='*70}")
    for f in findings[:25]:
        tag = min(f["entries"], key=lambda e: _SIG_ORDER.get(e[0], 9))[0]
        ds = "+" if f["day_chg"] >= 0 else ""
        vol_flag = "VOL🔵" if f["vol_dryup"] else f"vol{f['vol_ratio']:.2f}x"
        print(
            f"  {f['symbol']:<18} score:{f['score']:>5.1f}  "
            f"RS:{f['rs_pct']:>4.0f}%  52W:{f['leader_pct']:>4.0f}%  "
            f"{vol_flag}  [{tag}]  day:{ds}{f['day_chg']:.1f}%"
        )
    print()


# ── Main ───────────────────────────────────────────────────────────────────────


def main():
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nFetching watchlist from TradingView screener...")
    watchlist, float_map = get_watchlist()
    print(f"  {len(watchlist)} stocks  |  float data for {len(float_map)}")

    print("\nLoading OHLCV from SQLite (batch)...")
    all_data = load_ohlc_many(watchlist, lookback=400)
    print(f"  Loaded {len(all_data)} stocks")

    print(f"\nLoading benchmark ({BENCH_SYM})...")
    bench_dict = load_ohlc_many([BENCH_SYM], lookback=400)
    bench_df = bench_dict.get(BENCH_SYM)
    bench_series = (
        bench_df.set_index("date")["close"].astype(float)
        if bench_df is not None
        else None
    )
    if bench_series is None:
        print("  Benchmark NOT FOUND — aborting.")
        return
    print("  Benchmark loaded")

    print("\nComputing RS percentile ranks...")
    rs_pct_map = _compute_rs_pct_map(all_data, bench_series)
    print(f"  {len(rs_pct_map)} stocks ranked")

    print("\nFetching circuit limits...")
    circuit = get_circuit_limits()

    print(f"\nScanning {len(all_data)} stocks...")
    findings = []
    for i, (sym, df_raw) in enumerate(all_data.items(), 1):
        print(f"  {sym:<20} ({i}/{len(all_data)})   ", end="\r")
        result = analyse(
            sym,
            df_raw,
            bench_series,
            rs_pct=rs_pct_map.get(sym, 0.0),
            float_shares=float_map.get(sym, 0),
        )
        if result:
            findings.append(result)

    print_results(findings)

    md = build_markdown(findings, circuit)
    with open(MD_LATEST, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(MD_DATED, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  Saved → {MD_LATEST}")
    print(f"  Saved → {MD_DATED}")


if __name__ == "__main__":
    main()
