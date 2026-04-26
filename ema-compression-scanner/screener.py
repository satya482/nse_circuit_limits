#!/usr/bin/env python3
"""
EMA Compression Scanner — main entry point.
Scans NSE universe for stocks where EMA50/100/200 are tightly coiled
(spread < 1.5×ATR50 AND spread < 3% of EMA200) for ≥10 consecutive days.
Enriches each result with ZLEMA25 stats (direction, days since turn, chg%).
"""

import sys
import time
import yaml
from datetime import datetime
from pathlib import Path

import indicators
import gate
import scorer
from data_loader import load_env, get_kite, load_instruments, load_universe, fetch_all

BASE_DIR = Path(__file__).parent
ENV_FILE = BASE_DIR / ".env"
SETTINGS_FILE = BASE_DIR / "settings.yaml"


def tv_link(symbol: str) -> str:
    return f"[{symbol}](https://www.tradingview.com/chart/?symbol=NSE:{symbol})"


def fmt_price(p) -> str:
    return f"₹{p:,.1f}"


def _vol_ratio(f: dict) -> str:
    vol_ma50 = f["last"]["vol_ma50"]
    if vol_ma50 > 0:
        return f"{f['recent_vol'] / vol_ma50:.2f}"
    return "—"


def _zl_dir(zl_rising: bool) -> str:
    return "↑" if zl_rising else "↓"


def build_markdown(findings: list[dict], scanned: int, elapsed: float, today: str) -> str:
    rising = sorted([f for f in findings if f["zl_rising"]], key=lambda x: x["zl_days"])
    watch  = [f for f in findings if not f["zl_rising"]]

    lines = [
        f"# EMA Compression Scan — {today}",
        "",
        f"**Scanned:** {scanned} &nbsp;|&nbsp; "
        f"**Compressed (≥10d):** {len(findings)} &nbsp;|&nbsp; "
        f"**ZL Rising:** {len(rising)} &nbsp;|&nbsp; "
        f"**Run time:** {elapsed:.0f}s",
        "",
    ]

    if not findings:
        lines.append("_No compressed stocks found today._")
        return "\n".join(lines)

    # ── Section 1: Compression + ZL Rising (highest conviction) ──────────────────
    lines += [
        "## Compression + ZL Rising",
        "",
        "_Stocks that are compressed AND have ZLEMA25 turning up — coil + momentum flip._",
        "",
    ]

    if rising:
        hdr = "| # | Symbol | Close | EMA200 | Sprd/ATR | Sprd% | Comp Days | Score | ZL Days | ZL Chg% | VolRatio |"
        sep = "|---|--------|-------|--------|----------|-------|-----------|-------|---------|---------|---------|"
        lines += [hdr, sep]
        for i, f in enumerate(rising, 1):
            last = f["last"]
            zl_days_str = f"{f['zl_days']}d+" if f["zl_days"] >= 60 else f"{f['zl_days']}d"
            chg_str = f"+{f['zl_chg']:.1f}%" if f["zl_chg"] >= 0 else f"{f['zl_chg']:.1f}%"
            lines.append(
                f"| {i} | {tv_link(f['symbol'])} "
                f"| {fmt_price(last['close'])} "
                f"| {fmt_price(last['ema200'])} "
                f"| {last['spread_atr_ratio']:.2f} "
                f"| {last['spread_pct']:.2f}% "
                f"| {f['duration']}d "
                f"| **{f['score']}** "
                f"| {zl_days_str} "
                f"| {chg_str} "
                f"| {_vol_ratio(f)} |"
            )
    else:
        lines.append("_None today._")

    # ── Section 2: Full compression table ────────────────────────────────────────
    lines += [
        "",
        "---",
        "",
        "## All Compressed Stocks",
        "",
        "| # | Symbol | Close | EMA50 | EMA100 | EMA200 | Sprd/ATR | Sprd% | Comp Days | Score | ZL | ZL Days | ZL Chg% | VolRatio |",
        "|---|--------|-------|-------|--------|--------|----------|-------|-----------|-------|----|---------|---------|---------|",
    ]

    for i, f in enumerate(findings, 1):
        last = f["last"]
        zl_days_str = f"{f['zl_days']}d+" if f["zl_days"] >= 60 else f"{f['zl_days']}d"
        chg_str = f"+{f['zl_chg']:.1f}%" if f["zl_chg"] >= 0 else f"{f['zl_chg']:.1f}%"
        lines.append(
            f"| {i} | {tv_link(f['symbol'])} "
            f"| {fmt_price(last['close'])} "
            f"| {fmt_price(last['ema50'])} "
            f"| {fmt_price(last['ema100'])} "
            f"| {fmt_price(last['ema200'])} "
            f"| {last['spread_atr_ratio']:.2f} "
            f"| {last['spread_pct']:.2f}% "
            f"| {f['duration']}d "
            f"| **{f['score']}** "
            f"| {_zl_dir(f['zl_rising'])} "
            f"| {zl_days_str} "
            f"| {chg_str} "
            f"| {_vol_ratio(f)} |"
        )

    # ── Section 3: Score components ───────────────────────────────────────────────
    lines += [
        "",
        "---",
        "",
        "### Score components (tightness / duration / vol-contraction / trend / proximity)",
        "",
        "| Symbol | Tight | Dur | VolCtx | Trend | Prox |",
        "|--------|-------|-----|--------|-------|------|",
    ]
    for f in findings:
        c = f["components"]
        lines.append(
            f"| {tv_link(f['symbol'])} "
            f"| {c['tightness']} "
            f"| {c['duration']} "
            f"| {c['vol_contraction']} "
            f"| {c['trend']} "
            f"| {c['proximity']} |"
        )

    lines += ["", f"_Generated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} IST_"]
    return "\n".join(lines)


def run():
    t0 = time.time()
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] EMA Compression Scanner starting...")

    with open(SETTINGS_FILE, encoding="utf-8") as f:
        settings = yaml.safe_load(f)

    cache_dir = BASE_DIR / settings["cache_dir"]
    output_dir = BASE_DIR / settings["output_dir"]
    cache_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    env = load_env(ENV_FILE)
    kite = get_kite(env)
    print(f"  Kite connected.")

    print(f"  Loading instruments...")
    instruments = load_instruments(kite, cache_dir)

    universe = load_universe(settings["universe_csv"])
    print(f"  Universe: {len(universe)} symbols")

    print(f"  Fetching OHLCV (delta cache)...")
    all_data = fetch_all(
        kite, universe, instruments, cache_dir,
        lookback_days=settings["lookback_days"]
    )

    print(f"  Scanning {len(all_data)} stocks...")
    findings = []
    for sym, df_raw in all_data.items():
        try:
            df = indicators.compute(df_raw)
            qualifies, duration = gate.passes(df, settings)
            if not qualifies:
                continue
            total_score, components = scorer.score(df, duration, settings)
            zl_rising, zl_days, zl_chg = indicators.zl25_stats(df_raw)
            last = df.iloc[-1]
            comp_start = max(0, len(df) - duration)
            recent_vol = df["volume"].iloc[comp_start:].mean()
            findings.append({
                "symbol":     sym,
                "score":      total_score,
                "duration":   duration,
                "last":       last,
                "components": components,
                "recent_vol": recent_vol,
                "zl_rising":  zl_rising,
                "zl_days":    zl_days,
                "zl_chg":     zl_chg,
            })
        except Exception as e:
            print(f"    WARN {sym}: {e}", file=sys.stderr)

    findings.sort(key=lambda x: x["score"], reverse=True)

    elapsed = time.time() - t0
    md = build_markdown(findings, len(all_data), elapsed, today)

    out_file = output_dir / f"ema_compression_{today}.txt"
    out_file.write_text(md, encoding="utf-8")

    rising_count = sum(1 for f in findings if f["zl_rising"])
    print(f"  [{len(findings)} compressed, {rising_count} ZL rising] -> {out_file}")

    latest = output_dir / "ema_compression_latest.md"
    latest.write_text(md, encoding="utf-8")

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Done in {elapsed:.0f}s.")


if __name__ == "__main__":
    run()