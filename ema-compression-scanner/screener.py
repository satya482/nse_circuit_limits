#!/usr/bin/env python3
"""
EMA Compression + BB Squeeze Scanner.

Gates (all must pass):
  1. EMA dual gate  — spread < 1.5×ATR50 AND < 3% EMA200 for >=10 consecutive bars
  2. BB squeeze gate — BB(34,2.5) inside KC(34,1.5) for >=5 bars + width bottom 20%
  3. RS hard gate   — weekly RS vs NiftyMidSml400 above EMA9 AND 4-week slope positive

Scoring: 5-component cross-candidate min-max (EMA tightness/duration/vol trend/BB intensity/RS strength).
Output: single merged table sorted by score desc, ZL days asc.
"""

import sys
import time
import yaml
from datetime import datetime
from pathlib import Path

import indicators
import gate
import scorer
from data_loader import load_universe

sys.path.insert(0, str(Path(__file__).parent.parent))
from ohlc_db import load_ohlc, load_ohlc_many

BASE_DIR      = Path(__file__).parent
SETTINGS_FILE = BASE_DIR / "settings.yaml"


def tv_link(symbol: str) -> str:
    return f"[{symbol}](https://www.tradingview.com/chart/?symbol=NSE:{symbol})"


def fmt_price(p) -> str:
    return f"₹{p:,.1f}"


def _zl_dir(zl_rising: bool) -> str:
    return "up" if zl_rising else "dn"


def _zl_days_str(zl_days: int) -> str:
    return f"{zl_days}d+" if zl_days >= 60 else f"{zl_days}d"


def _chg_str(chg: float) -> str:
    return f"+{chg:.1f}%" if chg >= 0 else f"{chg:.1f}%"


def build_markdown(
    candidates: list[dict],
    n_scanned: int,
    n_ema_compressed: int,
    n_bb_squeeze: int,
    elapsed: float,
    today: str,
) -> str:
    n_signals = len(candidates)

    lines = [
        f"# EMA Compression + BB Squeeze — {today}",
        "",
        f"**Scanned:** {n_scanned} &nbsp;|&nbsp; "
        f"**Compressed (>=10d):** {n_ema_compressed} &nbsp;|&nbsp; "
        f"**BB Squeeze:** {n_bb_squeeze} &nbsp;|&nbsp; "
        f"**Signals:** {n_signals} &nbsp;|&nbsp; "
        f"**Run time:** {elapsed:.0f}s",
        "",
    ]

    if not candidates:
        lines.append("_No stocks passed all gates today._")
        lines += ["", f"_Generated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} IST_"]
        return "\n".join(lines)

    hdr = "| # | Symbol | Sector | Close | Comp Days | Sqz Days | ZL | ZL Days | ZL Chg% | Score |"
    sep = "|---|--------|--------|-------|-----------|----------|----|---------|---------|-------|"
    lines += [hdr, sep]

    for i, c in enumerate(candidates, 1):
        last = c["last"]
        lines.append(
            f"| {i} "
            f"| {tv_link(c['symbol'])} "
            f"| {c['sector']} "
            f"| {fmt_price(last['close'])} "
            f"| {c['duration']}d "
            f"| {c['squeeze_days']}d "
            f"| {_zl_dir(c['zl_rising'])} "
            f"| {_zl_days_str(c['zl_days'])} "
            f"| {_chg_str(c['zl_chg'])} "
            f"| **{c['score']}** |"
        )

    lines += [
        "",
        "---",
        "",
        "### Score components (tightness / duration / vol trend / BB intensity / RS strength)",
        "",
        "| Symbol | EMA Tight | Duration | Vol Trend | BB Intens | RS Strength | RS Gap | RS Slope |",
        "|--------|-----------|----------|-----------|-----------|-------------|--------|---------|",
    ]
    for c in candidates:
        comp = c["components"]
        lines.append(
            f"| {tv_link(c['symbol'])} "
            f"| {comp['ema_tightness']} "
            f"| {comp['duration']} "
            f"| {comp['volume_trend']} "
            f"| {comp['bb_intensity']} "
            f"| {comp['rs_strength']} "
            f"| {c['rs_gap']:.4f} "
            f"| {c['rs_slope']:.4f} |"
        )

    lines += [
        "",
        "_Gates: EMA spread < 1.5xATR50 + < 3% EMA200 (>=10 bars) "
        "+ BB(34,2.5) inside KC(34,1.5) (>=5 bars, width bottom 20%) "
        "+ weekly RS vs NiftyMidSml400 above EMA9 + 4-week slope positive_",
        "",
        f"_Generated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} IST_",
    ]
    return "\n".join(lines)


def run():
    t0    = time.time()
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] EMA Compression + BB Squeeze Scanner starting...")

    with open(SETTINGS_FILE, encoding="utf-8") as f:
        settings = yaml.safe_load(f)

    output_dir = BASE_DIR / settings["output_dir"]
    output_dir.mkdir(parents=True, exist_ok=True)

    universe = load_universe(settings["universe_csv"])
    print(f"  Universe: {len(universe)} symbols")
    universe_dict = {s["symbol"]: s for s in universe}

    print("  Loading benchmark (NIFTY MIDSML 400) from DB...")
    benchmark_df = load_ohlc("NIFTY MIDSML 400")
    if benchmark_df is None or len(benchmark_df) < 50:
        print("ERROR: Benchmark not in DB. Run fetch_data.py first.", file=sys.stderr)
        sys.exit(1)
    print(f"  Benchmark: {len(benchmark_df)} bars")

    print("  Loading OHLCV from DB...")
    symbols  = [s["symbol"] for s in universe]
    all_data = load_ohlc_many(symbols, lookback=settings["lookback_days"])

    # ── Phase 1: Compute RS line for all stocks (needed for cross-universe rating) ──
    print(f"  Computing RS ratings for {len(all_data)} stocks...")
    rs_data   = {}   # sym -> (above, slope_ok, rs_gap, rs_slope)
    rs_gaps   = {}   # sym -> rs_gap float (for percentile rank)

    rs_cfg = settings["rs"]
    for sym, df_raw in all_data.items():
        try:
            above, slope_ok, rs_gap, rs_slope = indicators.rs_line(
                df_raw, benchmark_df,
                rs_cfg["ema_period"],
                rs_cfg["slope_lookback_weeks"],
            )
            rs_data[sym]  = (above, slope_ok, rs_gap, rs_slope)
            rs_gaps[sym]  = rs_gap
        except Exception:
            rs_data[sym]  = (False, False, 0.0, 0.0)
            rs_gaps[sym]  = 0.0

    # Percentile rank: fraction of all fetched stocks with rs_gap <= this stock's gap
    all_gap_values = list(rs_gaps.values())
    n_total        = len(all_gap_values)
    rs_ratings     = {
        sym: sum(1 for g in all_gap_values if g <= gap) / n_total
        for sym, gap in rs_gaps.items()
    }

    # ── Phase 2: Apply gates in sequence, collect candidates ─────────────────────
    print(f"  Scanning {len(all_data)} stocks through gates...")

    bb_cfg  = settings["bollinger"]
    kc_cfg  = settings["keltner"]

    n_ema_compressed = 0
    n_bb_squeeze     = 0
    raw_candidates   = []

    for sym, df_raw in all_data.items():
        try:
            df = indicators.compute(df_raw)

            # Gate 1: EMA dual gate
            ema_ok, duration = gate.passes(df, settings)
            if not ema_ok:
                continue
            n_ema_compressed += 1

            # Add BB/KC indicators
            df = indicators.bollinger_keltner(
                df,
                bb_cfg["period"], bb_cfg["std_dev"],
                kc_cfg["period"], kc_cfg["atr_mult"],
            )

            # Gate 2: BB squeeze gate
            squeeze_ok, squeeze_days = gate.bb_squeeze_passes(df, settings)
            if not squeeze_ok:
                continue
            n_bb_squeeze += 1

            # Gate 3: RS hard gate (pre-computed)
            above, slope_ok, rs_gap, rs_slope = rs_data[sym]
            if not (above and slope_ok):
                continue

            zl_rising, zl_days, zl_chg = indicators.zl25_stats(df_raw)
            last       = df.iloc[-1]
            comp_start = max(0, len(df) - duration)

            raw_candidates.append({
                "symbol":       sym,
                "sector":       universe_dict.get(sym, {}).get("sector", ""),
                "df":           df,
                "duration":     duration,
                "squeeze_days": squeeze_days,
                "rs_gap":       rs_gap,
                "rs_slope":     rs_slope,
                "rs_rating":    rs_ratings.get(sym, 0.5),
                "zl_rising":    zl_rising,
                "zl_days":      zl_days,
                "zl_chg":       zl_chg,
                "last":         last,
                "recent_vol":   float(df["volume"].iloc[comp_start:].mean()),
            })

        except Exception as e:
            print(f"    WARN {sym}: {e}", file=sys.stderr)

    # ── Phase 3: Score all candidates together ───────────────────────────────────
    scores = scorer.score_all(raw_candidates, settings)

    # Build score components for display (re-derive from scorer internals via ratio)
    w  = settings["scoring"]
    rw = settings["rs_weights"]
    g  = settings["gate"]

    candidates = []
    for c, total_score in zip(raw_candidates, scores):
        df       = c["df"]
        duration = c["duration"]
        last     = df.iloc[-1]

        spread_atr = float(last.get("spread_atr_ratio", g["ema_spread_atr_ratio"]))
        comp_start = max(0, len(df) - duration)
        recent_vol = float(df["volume"].iloc[comp_start:].mean())
        long_vol   = float(last.get("vol_ma50", 0) or 0)
        vol_ctxt   = round(max(0.0, 1.0 - recent_vol / long_vol) * 100, 1) if long_vol > 0 else 50.0

        bb_pct_rank   = float(last.get("bb_width_pct_rank", 50.0) or 50.0)
        depth_score   = round(min(c["squeeze_days"], 20) / 20 * 100, 1)
        width_score   = round((1.0 - bb_pct_rank / 100) * 100, 1)

        components = {
            "ema_tightness": round(100 / max(spread_atr, 0.01) / (100 / max(g["ema_spread_atr_ratio"], 0.01)) * 100, 1),
            "duration":      round(min(duration, 60) / 60 * 100, 1),
            "volume_trend":  vol_ctxt,
            "bb_intensity":  round((depth_score + width_score) / 2, 1),
            "rs_strength":   round((rw["gap"] * c["rs_gap"] + rw["slope"] * c["rs_slope"]) * 100, 2),
        }

        candidates.append({**c, "score": total_score, "components": components})

    # Sort: score descending, ZL days ascending as tiebreak
    candidates.sort(key=lambda x: (-x["score"], x["zl_days"]))

    elapsed = time.time() - t0
    md = build_markdown(
        candidates, len(all_data),
        n_ema_compressed, n_bb_squeeze,
        elapsed, today,
    )

    out_file = output_dir / f"ema_compression_{today}.txt"
    out_file.write_text(md, encoding="utf-8")

    latest = output_dir / "ema_compression_latest.md"
    latest.write_text(md, encoding="utf-8")

    print(
        f"  [{n_ema_compressed} EMA compressed -> {n_bb_squeeze} BB squeeze -> "
        f"{len(candidates)} signals] -> {out_file}"
    )
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Done in {elapsed:.0f}s.")


if __name__ == "__main__":
    run()