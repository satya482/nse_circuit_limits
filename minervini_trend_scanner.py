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
  9. RS strength: weekly RS EMA9 flat or rising (see _weekly_rs_ema9_gate();
     deliberately does NOT require RS Line above the EMA9, unlike
     ema25_zl_scanner._weekly_rs_gate())

No partial-score output -- binary qualify list.

Age: consecutive trading days ALL 9 checks have held true together, walking
back through OHLC history (no state file needed, see trend_template_age()).

Additions/deletions: today's qualifying symbols diffed against the previous
run's (state persisted in minervini_trend_state.json, mirrors
rs_weekly_ema9_scanner.py's diff pattern) -- shown as a 2-column table at the
top of the output.

Data source: .ohlc_data/market.db (populated by fetch_data.py)
Output:      minervini_scans/minervini_trend_latest.md
             minervini_scans/minervini_trend_YYYY-MM-DD.md
"""

import sys
import os
import json
from datetime import datetime

import pandas as pd

import ema25_zl_scanner as base
from ohlc_db import load_ohlc, load_ohlc_many, liq_tag, cmf_tag, deliv_tag
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER
from float_gate import float_metrics, passes_hard_gate, trap_label
from tv_watchlist import tv_csv, tv_csv_flat, tv_top_sections

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "minervini_scans")
TODAY = datetime.now().strftime("%Y-%m-%d")
MD_LATEST = os.path.join(SCANS_DIR, "minervini_trend_latest.md")
STATE_FILE = os.path.join(SCANS_DIR, "minervini_trend_state.json")
BENCH_SYM = "NIFTY MIDSML 400"
LOOKBACK_52WK = 252
MIN_BARS = 260  # 52wk window + buffer
AGE_CAP = 400  # bars to walk back before giving up (matches load_ohlc's default lookback)

# Wider than ema25_zl_scanner/nifty50_zlema25_scanner's day-granularity _AGE_BUCKETS:
# minervini's 9-check AND-gate age runs weeks-to-months once qualified, not days.
AGE_BUCKETS = [
    ("<2 WEEKS", 0, 10),  # age=0 seen in practice
    ("2-4 WEEKS", 11, 21),
    ("1-2 MONTHS", 22, 42),
    ("2-3 MONTHS", 43, 63),
    ("3-6 MONTHS", 64, 126),
    ("6+ MONTHS", 127, AGE_CAP),
]


# ── Trend template criteria ─────────────────────────────────────────────────
def sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def _checks_series(close: pd.Series) -> dict:
    """Per-bar boolean series for each of the 8 SMA/52wk checks (criterion 9 --
    RS gate -- is separate, see _rs_pass_series). NaN comparisons evaluate
    False, so bars without enough warmup history are naturally excluded.
    Shared by trend_template_checks() (today only) and trend_template_age()
    (whole history) so both use identical logic -- no drift between them."""
    sma50 = sma(close, 50)
    sma150 = sma(close, 150)
    sma200 = sma(close, 200)
    wk_low = close.rolling(LOOKBACK_52WK, min_periods=LOOKBACK_52WK).min()
    wk_high = close.rolling(LOOKBACK_52WK, min_periods=LOOKBACK_52WK).max()

    return {
        "above_sma150": close > sma150,
        "above_sma200": close > sma200,
        "sma150_above_sma200": sma150 > sma200,
        # sma200.iloc[-1] > sma200.iloc[-21] compares today to 20 bars back
        # (iloc[-21] is the 21st-from-last element, i.e. 20 positions before
        # iloc[-1]) -- shift(20) reproduces that same relationship at every bar.
        "sma200_trending_up": sma200 > sma200.shift(20),
        "sma50_above_150_200": (sma50 > sma150) & (sma50 > sma200),
        "above_sma50": close > sma50,
        "above_52wk_low_30pct": close >= 1.30 * wk_low,
        "within_25pct_of_52wk_high": close >= 0.75 * wk_high,
    }


def trend_template_checks(close: pd.Series) -> dict:
    """8 SMA/52wk checks for the last bar only (criterion 9 -- RS gate -- is
    separate, needs the benchmark series, see _weekly_rs_ema9_gate() call in
    analyse())."""
    return {k: bool(v.iloc[-1]) for k, v in _checks_series(close).items()}


def passes_trend_template(checks: dict) -> bool:
    return all(checks.values())


def _sma_pass_series(close: pd.Series) -> pd.Series:
    """AND of all 8 SMA/52wk checks, per bar."""
    series = list(_checks_series(close).values())
    out = series[0]
    for s in series[1:]:
        out = out & s
    return out


def _weekly_rs_ema9_gate(c_rs: pd.Series, idx_rs: pd.Series) -> bool:
    """Weekly RS EMA9 flat or rising vs prior week. Unlike
    ema25_zl_scanner._weekly_rs_gate(), does NOT require daily RS Line above
    the EMA9 -- only the EMA9's own slope."""
    wk_c = c_rs.resample("W").last().dropna()
    wk_idx = idx_rs.resample("W").last().dropna()
    common = wk_c.index.intersection(wk_idx.index)
    if len(common) < 12:
        return False
    wk_rs = (wk_c.loc[common] / wk_idx.loc[common]) * 1000
    wk_rs_e9 = base.ema(wk_rs, 9)
    return bool(wk_rs_e9.iloc[-1] >= wk_rs_e9.iloc[-2])


def _rs_pass_series(c_rs: pd.Series, idx_rs: pd.Series) -> pd.Series:
    """Per-day version of _weekly_rs_ema9_gate(): weekly RS EMA9 flat/rising
    vs prior week (forward-filled to daily). Mirrors
    rs_weekly_ema9_scanner.weekly_rs_ema9_trend()'s daily-alignment approach."""
    daily_rs = (c_rs / idx_rs) * 1000
    wk_c = c_rs.resample("W").last().dropna()
    wk_idx = idx_rs.resample("W").last().dropna()
    common = wk_c.index.intersection(wk_idx.index)
    if len(common) < 12:
        return pd.Series(False, index=daily_rs.index)
    wk_rs = (wk_c.loc[common] / wk_idx.loc[common]) * 1000
    wk_rs_e9 = base.ema(wk_rs, 9)
    wk_flat_or_rising = wk_rs_e9 >= wk_rs_e9.shift(1)

    return (
        wk_flat_or_rising.astype(float)
        .reindex(daily_rs.index, method="ffill")
        .fillna(0.0)
        .astype(bool)
    )


def trend_template_age(close: pd.Series, c_rs: pd.Series, idx_rs: pd.Series) -> int:
    """Consecutive trading days ALL 9 checks (8 SMA/52wk + RS gate) have held
    true, walking backward from today. Same backward-walk shape as
    rs_weekly_ema9_scanner.weekly_rs_ema9_trend()'s age loop, capped at
    AGE_CAP bars."""
    sma_pass = _sma_pass_series(close)
    rs_pass = _rs_pass_series(c_rs, idx_rs)
    combined = sma_pass.reindex(rs_pass.index).fillna(False) & rs_pass

    age = 0
    for v in reversed(combined.values):
        if not v or age >= AGE_CAP:
            break
        age += 1
    return age


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
        if not _weekly_rs_ema9_gate(c_rs, idx_rs):
            return None

        age = trend_template_age(c, c_rs, idx_rs)

        window = c.iloc[-LOOKBACK_52WK:]
        curr_close = c.iloc[-1]
        prev_close = c.iloc[-2]

        return {
            "symbol": symbol,
            "close": curr_close,
            "day_chg": (curr_close - prev_close) / prev_close * 100,
            "off_high_pct": (curr_close / window.max() - 1) * 100,
            "above_low_pct": (curr_close / window.min() - 1) * 100,
            "age": age,
            "trap": trap_label(fm),
            "liq_tag": liq_tag(raw),
            "cmf_tag": cmf_tag(raw),
            "deliv_tag": deliv_tag(symbol),
        }
    except Exception:
        return None


# ── Previous-run state (additions/deletions diff, mirrors
#    rs_weekly_ema9_scanner.py's load_previous/save_current) ───────────────────
def load_previous() -> set:
    if not os.path.exists(STATE_FILE):
        return set()
    try:
        with open(STATE_FILE, encoding="utf-8") as f:
            return set(json.load(f))
    except Exception:
        return set()


def save_current(symbols: list[str]) -> None:
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted(symbols), f, indent=2)


# ── Markdown ─────────────────────────────────────────────────────────────────
STATIC_HEADER = """### Scan definition
| Filter | Value |
|--------|-------|
| Exchange | NSE common equity |
| Price | > Rs 50 |
| Market cap | Rs 1,000 Cr - Rs 5 Lakh Cr |
| Criteria (all must pass) | close > SMA50 > SMA150 > SMA200 stack, SMA200 rising 21d, close within 25% of 52wk high, close >= 30% above 52wk low, RS gate |
| RS gate | Daily RS Line > Weekly RS EMA9, Weekly RS EMA9 rising (RS = close/NIFTY MIDSML 400 x 1000) |
| Age | Consecutive trading days all 9 checks (incl. RS gate) have held true together, capped at {AGE_CAP}d |
| Float gate | AVOID dropped from scan, SAFE/CAUTION shown under symbol (float_gate.py) |
| Symbol tags | trap - liq (avg10Cr-todayCr) - CMF - DEL% |

---
""".format(AGE_CAP=AGE_CAP)


def _diff_table(additions: list[str], deletions: list[str]) -> list[str]:
    """One table, two side-by-side columns: symbols added / dropped vs the
    previous run (state persisted in minervini_trend_state.json)."""
    lines = [
        "### Additions / Deletions vs previous run",
        "| Additions | Deletions |",
        "|-----------|-----------|",
    ]
    n = max(len(additions), len(deletions))
    if n == 0:
        lines.append("| *(none)* | *(none)* |")
    else:
        for i in range(n):
            a = additions[i] if i < len(additions) else ""
            d = deletions[i] if i < len(deletions) else ""
            a_cell = f"[{a}](https://in.tradingview.com/chart/?symbol=NSE:{a})" if a else ""
            d_cell = f"[{d}](https://in.tradingview.com/chart/?symbol=NSE:{d})" if d else ""
            lines.append(f"| {a_cell} | {d_cell} |")
    lines.append("")
    return lines


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
            f"| {f.get('age', 0)}d "
            f"| SMA-OK "
            f"| RS-OK "
            f"| {ds}{f['day_chg']:.2f}% |"
        )
    return rows


def build_markdown(
    findings: list[dict],
    additions: list[str] | None = None,
    deletions: list[str] | None = None,
) -> str:
    rows = sorted(findings, key=lambda x: x.get("age", 0))

    hdr = [
        "| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |",
        "|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|",
    ]

    lines = [
        f"# Minervini Trend Template Scan - {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
    ]
    lines += _diff_table(additions or [], deletions or [])
    lines += [
        STATIC_HEADER,
        f"**Qualifying: {len(rows)}**",
        "",
        "### Trend Template Qualifiers",
    ]
    if rows:
        wl_parts = []
        for label, lo, hi in AGE_BUCKETS:
            syms = sorted(f["symbol"] for f in rows if lo <= f.get("age", 0) <= hi)
            if syms:
                wl_parts.append(f"###{label}," + tv_csv_flat(f"NSE:{s}" for s in syms))
        lines += [
            "",
            "**TradingView watchlist** *(sectioned by trend age — paste into TV import)*",
            "```",
            ",".join(tv_top_sections() + wl_parts),
            "```",
            "",
        ]
        lines += hdr + _table_rows(rows)
        lines += ["", "### By Trend Age"]
        for label, lo, hi in AGE_BUCKETS:
            syms = sorted(f["symbol"] for f in rows if lo <= f.get("age", 0) <= hi)
            if syms:
                lines += [
                    "",
                    f"**{label}** ({len(syms)})",
                    "```",
                    tv_csv(f"NSE:{s}" for s in syms),
                    "```",
                ]
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

    previous_syms = load_previous()

    findings = []
    for i, sym in enumerate(watchlist, 1):
        print(f"  {sym:<20} ({i}/{len(watchlist)})   ", end="\r")
        result = analyse(sym, index_s, float_shares=float_map.get(sym, 0))
        if result:
            findings.append(result)

    current_syms = {f["symbol"] for f in findings}
    additions = sorted(current_syms - previous_syms)
    deletions = sorted(previous_syms - current_syms)
    print(f"\n  Qualifying: {len(findings)}  |  +{len(additions)} additions  -{len(deletions)} deletions")

    dated_file = os.path.join(SCANS_DIR, f"minervini_trend_{TODAY}.md")
    md = build_markdown(findings, additions, deletions)
    with open(MD_LATEST, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(dated_file, "w", encoding="utf-8") as fh:
        fh.write(md)
    save_current(list(current_syms))
    print(f"  Saved -> {MD_LATEST}")
    print(f"  Saved -> {dated_file}")


if __name__ == "__main__":
    main()
