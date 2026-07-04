#!/usr/bin/env python3
"""
scripts/wt_breadth_backtest.py
================================
Extended-history backtest: daily WaveTrend bull-cross count (universe-wide)
vs market breadth (data/breadth_history.csv), over ~18 months instead of the
21-day sample in research/wt_breadth_correlation.md.

Universe: data/breadth_universe.csv (current snapshot — survivorship-biased,
see caveat in output). OHLC: local SQLite via ohlc_db.load_ohlc_many.

Computes, per day, across the universe:
  total_cross   : count of WT1/WT2 bull crosses (any level) — proxy for rank>=1
  os_cross      : count of bull crosses with wt2 <= -53 (L2 or deeper) — proxy for rank>=2
  sqz_cross     : count of bull crosses firing while BB(20,2,SMA) inside KC(20,1.5,SMA)

PPV (rank 4/5) is NOT recomputed here — Pine's pocket-pivot loop is per-bar,
too expensive to vectorize accurately at this scale. That finding stands from
the existing 21-day study (research/wt_breadth_correlation.md) and is not
re-tested.

Output: data/wt_breadth_backtest.csv (date, total_cross, os_cross, sqz_cross)
        + printed summary stats / correlations / hypothesis checks.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_DIR))

from ohlc_db import load_ohlc_many  # noqa: E402
from wavetrend_scanner import WaveTrendCalculator  # noqa: E402

WINDOW_DAYS = 400  # ~18 months of trading days, plus warmup handled by lookback
LOOKBACK = 500  # bars pulled per symbol (covers window + EMA warmup)


def _squeeze_series(df: pd.DataFrame) -> pd.Series:
    """Vectorized BB(20,2,SMA) inside KC(20,1.5,SMA-ATR) — full history, bool per bar."""
    c = df["close"].astype(float)
    h = df["high"].astype(float)
    l = df["low"].astype(float)
    bb_basis = c.rolling(20).mean()
    bb_std = c.rolling(20).std()
    bb_upper = bb_basis + 2.0 * bb_std
    bb_lower = bb_basis - 2.0 * bb_std
    tr = pd.concat(
        [h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1
    ).max(axis=1)
    kc_atr = tr.rolling(20).mean()
    kc_upper = bb_basis + 1.5 * kc_atr
    kc_lower = bb_basis - 1.5 * kc_atr
    return (bb_upper < kc_upper) & (bb_lower > kc_lower)


def main() -> None:
    out_path = REPO_DIR / "data" / "wt_breadth_backtest.csv"

    if "--reuse" in sys.argv and out_path.exists():
        print(f"Reusing existing {out_path} (--reuse)")
        wt_df = pd.read_csv(out_path, dtype={"date": str})
    else:
        universe = pd.read_csv(REPO_DIR / "data" / "breadth_universe.csv")["symbol"].tolist()
        print(f"Universe: {len(universe)} symbols (current breadth_universe.csv snapshot)")

        print("Loading OHLCV from SQLite (batch)...")
        all_data = load_ohlc_many(universe, lookback=LOOKBACK)
        print(f"  Loaded {len(all_data)} / {len(universe)} symbols")

        calc = WaveTrendCalculator()

        per_date_total: dict[str, int] = {}
        per_date_os: dict[str, int] = {}
        per_date_sqz: dict[str, int] = {}

        n_ok, n_skip = 0, 0
        for i, (sym, df) in enumerate(all_data.items(), 1):
            if i % 250 == 0:
                print(f"  {i}/{len(all_data)}...")
            if df is None or len(df) < calc._min_bars + 5:
                n_skip += 1
                continue
            try:
                hist = calc.get_history(df)  # adds wt1, wt2, cross flags — full series
                sqz = _squeeze_series(df)
                dates = df["date"].values
                bull_any = hist["wt_bull_cross_any"].values
                bull_os = (hist["wt_bull_cross_os"] | hist["wt_bull_cross_os_l2"]).values
                sqz_v = sqz.values

                # Only look at last WINDOW_DAYS bars to bound compute + match research window
                tail_dates = dates[-WINDOW_DAYS:]
                tail_any = bull_any[-WINDOW_DAYS:]
                tail_os = bull_os[-WINDOW_DAYS:]
                tail_sqz = sqz_v[-WINDOW_DAYS:]

                for d, is_any, is_os, is_sqz in zip(tail_dates, tail_any, tail_os, tail_sqz):
                    if not is_any:
                        continue
                    per_date_total[d] = per_date_total.get(d, 0) + 1
                    if is_os:
                        per_date_os[d] = per_date_os.get(d, 0) + 1
                    if is_sqz:
                        per_date_sqz[d] = per_date_sqz.get(d, 0) + 1
                n_ok += 1
            except Exception:
                n_skip += 1
                continue

        print(f"\nProcessed OK: {n_ok}  Skipped (short history / error): {n_skip}")

        wt_df = pd.DataFrame({"date": sorted(per_date_total.keys())})
        wt_df["total_cross"] = wt_df["date"].map(per_date_total).fillna(0).astype(int)
        wt_df["os_cross"] = wt_df["date"].map(per_date_os).fillna(0).astype(int)
        wt_df["sqz_cross"] = wt_df["date"].map(per_date_sqz).fillna(0).astype(int)

        wt_df.to_csv(out_path, index=False)
        print(f"Wrote {len(wt_df)} rows to {out_path}")
        print(wt_df.tail(10).to_string(index=False))

    # ── Merge with breadth history ──────────────────────────────────────────
    breadth = pd.read_csv(REPO_DIR / "data" / "breadth_history.csv", dtype={"date": str})
    breadth = breadth[breadth["total_eligible"] >= 1500].copy()  # drop thin-universe days
    wt_df["date"] = wt_df["date"].astype(str)

    merged = wt_df.merge(breadth, on="date", how="inner").sort_values("date").reset_index(drop=True)
    print(f"\nMerged rows (WT x breadth, total_eligible>=1500): {len(merged)}")
    print(f"Date range: {merged['date'].min()} .. {merged['date'].max()}")

    merged_path = REPO_DIR / "data" / "wt_breadth_backtest_merged.csv"
    merged.to_csv(merged_path, index=False)
    print(f"Wrote merged table to {merged_path}")

    # ── Correlation table ────────────────────────────────────────────────────
    print("\n=== Correlations (Pearson, same-day) ===")
    metrics = ["up4_count", "down4_count", "pct_above_sma50", "pct_above_sma200", "net_thrust"]
    for wt_col in ["total_cross", "os_cross", "sqz_cross"]:
        row = []
        for m in metrics:
            sub = merged[[wt_col, m]].dropna()
            r = sub[wt_col].corr(sub[m]) if len(sub) > 5 else float("nan")
            row.append(f"{m}={r:+.2f}")
        print(f"  {wt_col:<12} " + "  ".join(row))

    # ── Lead/lag structure ──────────────────────────────────────────────────
    print("\n=== Lead/lag: r(total_cross, pct_above_sma50) at offsets ===")
    m2 = merged.set_index("date")[["total_cross", "pct_above_sma50"]].copy()
    for offset in [-3, -2, -1, 0, 1, 2, 3]:
        shifted = m2["pct_above_sma50"].shift(-offset)  # offset days AHEAD of total_cross
        sub = pd.concat([m2["total_cross"], shifted], axis=1).dropna()
        r = sub.iloc[:, 0].corr(sub.iloc[:, 1]) if len(sub) > 5 else float("nan")
        label = f"{offset:+d}d" if offset != 0 else "same day"
        print(f"  {label:>10}: r={r:+.3f}  n={len(sub)}")

    # ── Regime split: high vs low total_cross days -> forward breadth ──────
    print("\n=== High vs low total_cross tiers: forward breadth ===")
    q80 = merged["total_cross"].quantile(0.80)
    q20 = merged["total_cross"].quantile(0.20)
    merged["pct50_fwd1"] = merged["pct_above_sma50"].shift(-1)
    merged["pct50_fwd3"] = merged["pct_above_sma50"].shift(-3)
    merged["pct50_fwd5"] = merged["pct_above_sma50"].shift(-5)
    hi = merged[merged["total_cross"] >= q80]
    lo = merged[merged["total_cross"] <= q20]
    print(f"  total_cross >= {q80:.0f} (n={len(hi)}): "
          f"pct50_same={hi['pct_above_sma50'].mean():.1f}  "
          f"+1d={hi['pct50_fwd1'].mean():.1f}  +3d={hi['pct50_fwd3'].mean():.1f}  +5d={hi['pct50_fwd5'].mean():.1f}")
    print(f"  total_cross <= {q20:.0f} (n={len(lo)}): "
          f"pct50_same={lo['pct_above_sma50'].mean():.1f}  "
          f"+1d={lo['pct50_fwd1'].mean():.1f}  +3d={lo['pct50_fwd3'].mean():.1f}  +5d={lo['pct50_fwd5'].mean():.1f}")

    # ── "Too many crosses" — percentile of recent days ─────────────────────
    print("\n=== Recent total_cross vs full-history percentile ===")
    recent = merged.tail(10)
    dist = merged["total_cross"]
    for _, r in recent.iterrows():
        pct = (dist < r["total_cross"]).mean() * 100
        print(f"  {r['date']}: total_cross={r['total_cross']:>4d}  pctile={pct:>5.1f}%  "
              f"pct50={r['pct_above_sma50']:.1f}  net_thrust={r['net_thrust']}")

    # ── Chop hypothesis: total_cross vs realized whipsaw (up4 & dn4 both elevated) ──
    print("\n=== Chop proxy: total_cross vs min(up4,down4) (both-sided churn) ===")
    merged["chop_proxy"] = merged[["up4_count", "down4_count"]].min(axis=1)
    sub = merged[["total_cross", "chop_proxy"]].dropna()
    r = sub["total_cross"].corr(sub["chop_proxy"])
    print(f"  r(total_cross, min(up4,down4)) = {r:+.3f}  n={len(sub)}")

    # ── total>100 as overbought-warning hypothesis ──────────────────────────
    print("\n=== total_cross > 100 (\"overbought warning\") — forward pct50 change ===")
    merged["pct50_chg_fwd5"] = merged["pct50_fwd5"] - merged["pct_above_sma50"]
    hi100 = merged[merged["total_cross"] > 100]
    rest = merged[merged["total_cross"] <= 100]
    print(f"  total_cross>100 (n={len(hi100)}): mean 5d pct50 change = {hi100['pct50_chg_fwd5'].mean():+.2f}")
    print(f"  total_cross<=100 (n={len(rest)}): mean 5d pct50 change = {rest['pct50_chg_fwd5'].mean():+.2f}")


if __name__ == "__main__":
    main()
