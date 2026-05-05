#!/usr/bin/env python3
"""
ZL + Squeeze + RS Backtest — generic, any NSE symbol.
Usage:
    python backtest_zl_squeeze.py KRN
    python backtest_zl_squeeze.py KRN --lookback 800

Signal:  First bar in a ZLEMA25 rising episode where ALL three align:
           (1) ZL25 rising
           (2) BB squeeze active  (BB(20,2.0) inside KC(20,1.5,SMA ATR))
           (3) Daily RS > Weekly RS EMA9  AND  Weekly RS EMA9 rising
             RS = (stock_close / NIFTY MIDSML 400) * 1000
Entry:   Next bar open.
Stop:    Entry - 1.5x ATR14 of signal bar.
Exits:   T1 +8% (flag only) -> T2 +18% (full exit)
         | ZL25 flat/down -> exit at close (Trail / Trail-T1)
         | 30-bar time stop.

Output:
  Section 1 — Every ZL rising episode: squeeze dates + RS-pass dates.
  Section 2 — Trade log + summary stats.
  Section 3 — Comparison: trades with RS filter vs without.
"""

import argparse
import sys
sys.stdout.reconfigure(encoding="utf-8")
import pandas as pd
from ohlc_db import load_ohlc

# ── Config ───────────────────────────────────────────────────────────────────
ZL_PERIOD     = 25
BB_PERIOD     = 20;  BB_MULT = 2.0
KC_PERIOD     = 20;  KC_MULT = 1.5
ATR_PERIOD    = 14
ATR_STOP_MULT = 1.5
TARGET1_PCT   = 8.0
TARGET2_PCT   = 18.0
MAX_BARS      = 30
INDEX_SYMBOL  = "NIFTY MIDSML 400"
# ─────────────────────────────────────────────────────────────────────────────


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    c, h, l = df["close"], df["high"], df["low"]

    # ZLEMA25
    ema      = c.ewm(span=ZL_PERIOD, adjust=False).mean()
    df["zl25"] = 2 * ema - ema.ewm(span=ZL_PERIOD, adjust=False).mean()

    # ATR14 (SMA, matches scanner convention)
    tr = pd.concat(
        [h - l, (h - c.shift()).abs(), (l - c.shift()).abs()], axis=1
    ).max(axis=1)
    df["atr14"] = tr.rolling(ATR_PERIOD).mean()

    # BB (20, 2.0, SMA)
    sma20    = c.rolling(BB_PERIOD).mean()
    std20    = c.rolling(BB_PERIOD).std(ddof=0)
    bb_upper = sma20 + BB_MULT * std20
    bb_lower = sma20 - BB_MULT * std20

    # KC (20, 1.5, SMA ATR) — same as zl_squeeze_scanner
    kc_atr   = tr.rolling(KC_PERIOD).mean()
    kc_mid   = c.rolling(KC_PERIOD).mean()
    kc_upper = kc_mid + KC_MULT * kc_atr
    kc_lower = kc_mid - KC_MULT * kc_atr

    # Squeeze: BB strictly inside KC (matches zl_squeeze_scanner)
    df["squeeze"] = (bb_upper < kc_upper) & (bb_lower > kc_lower)

    return df.dropna().reset_index(drop=True)


def compute_rs(df: pd.DataFrame, idx_df: pd.DataFrame) -> pd.DataFrame:
    """
    Add rs_pass column to df.
    rs_pass = True when:
      daily RS > weekly RS EMA9
      AND weekly RS EMA9 rising
      AND weekly RS EMA21 rising
    """
    stock = df.set_index("date")["close"].astype(float)
    idx   = idx_df.set_index("date")["close"].astype(float)

    common = stock.index.intersection(idx.index)
    if len(common) < 30:
        df["rs_pass"] = False
        return df

    rs_daily = (stock.loc[common] / idx.loc[common]) * 1000  # date-indexed

    # Weekly RS: last trading day of each week (Friday anchor)
    weekly_rs = rs_daily.resample("W-FRI").last().dropna()
    if len(weekly_rs) < 23:
        df["rs_pass"] = False
        return df

    wrs_e9      = weekly_rs.ewm(span=9,  adjust=False).mean()
    wrs_e9_prev = wrs_e9.shift(1)

    wrs_e21      = weekly_rs.ewm(span=21, adjust=False).mean()
    wrs_e21_prev = wrs_e21.shift(1)

    # Forward-fill weekly values to every trading day
    wrs_e9_daily       = wrs_e9.reindex(rs_daily.index,       method="ffill")
    wrs_e9_prev_daily  = wrs_e9_prev.reindex(rs_daily.index,  method="ffill")
    wrs_e21_daily      = wrs_e21.reindex(rs_daily.index,      method="ffill")
    wrs_e21_prev_daily = wrs_e21_prev.reindex(rs_daily.index, method="ffill")

    rs_pass = (
        (rs_daily > wrs_e9_daily)
        & (wrs_e9_daily  > wrs_e9_prev_daily)
        & (wrs_e21_daily > wrs_e21_prev_daily)
    )

    rs_df = pd.DataFrame({
        "date":    rs_daily.index,
        "rs_pass": rs_pass.values,
    })
    df = df.merge(rs_df, on="date", how="left")
    df["rs_pass"] = df["rs_pass"].fillna(False).astype(bool)
    return df


def zl_rising_episodes(zl: pd.Series) -> list[tuple[int, int]]:
    """Return (start_idx, end_idx) for every ZL25 rising run."""
    rising = (zl > zl.shift(1)).fillna(False).values
    episodes, in_ep, start = [], False, 0
    for i, r in enumerate(rising):
        if r and not in_ep:
            in_ep, start = True, i
        elif not r and in_ep:
            in_ep = False
            episodes.append((start, i - 1))
    if in_ep:
        episodes.append((start, len(rising) - 1))
    return episodes


def simulate_trade(df: pd.DataFrame, signal_idx: int) -> dict | None:
    entry_idx = signal_idx + 1
    if entry_idx >= len(df):
        return None

    entry = df.at[entry_idx, "open"]
    atr   = df.at[signal_idx, "atr14"]
    stop  = entry - ATR_STOP_MULT * atr
    risk  = entry - stop
    if risk <= 0:
        return None

    t1 = entry * (1 + TARGET1_PCT / 100)
    t2 = entry * (1 + TARGET2_PCT / 100)

    hit_t1      = False
    exit_price  = None
    exit_date   = None
    exit_reason = None
    bars_held   = 0

    for j in range(entry_idx, min(entry_idx + MAX_BARS + 1, len(df))):
        bar = df.iloc[j]
        bars_held = j - entry_idx

        if bar["low"] <= stop:
            exit_price, exit_date, exit_reason = stop, bar["date"], "Stop"
            break

        if not hit_t1 and bar["high"] >= t1:
            hit_t1 = True

        if hit_t1 and bar["high"] >= t2:
            exit_price, exit_date, exit_reason = t2, bar["date"], "T2"
            break

        # Exit: ZL25 flat or down (skip check on entry bar itself)
        if j > entry_idx and df.at[j, "zl25"] <= df.at[j - 1, "zl25"]:
            reason = "Trail-T1" if hit_t1 else "Trail"
            exit_price, exit_date, exit_reason = bar["close"], bar["date"], reason
            break
    else:
        last = df.iloc[min(entry_idx + MAX_BARS, len(df) - 1)]
        exit_price, exit_date, exit_reason = last["close"], last["date"], "TimeStop"
        bars_held = MAX_BARS

    pnl_pct = (exit_price - entry) / entry * 100
    r_mult  = (exit_price - entry) / risk

    return dict(
        signal_date = df.at[signal_idx, "date"],
        entry_date  = df.at[entry_idx, "date"],
        entry       = round(entry, 2),
        stop        = round(stop, 2),
        risk        = round(risk, 2),
        t1          = round(t1, 2),
        t2          = round(t2, 2),
        exit        = round(exit_price, 2),
        exit_date   = exit_date,
        exit_reason = exit_reason,
        pnl_pct     = round(pnl_pct, 2),
        r_mult      = round(r_mult, 2),
        bars        = bars_held,
        hit_t1      = hit_t1,
    )


def run(symbol: str, lookback: int = 600) -> None:
    df = load_ohlc(symbol, lookback=lookback)
    if df is None or len(df) < 60:
        print(f"  No data for {symbol}. Is it in the SQLite DB?")
        sys.exit(1)

    # Load index for RS computation (extra history for weekly EMA warmup)
    idx_df = load_ohlc(INDEX_SYMBOL, lookback=lookback + 100)
    has_rs = idx_df is not None and len(idx_df) >= 30

    df = add_indicators(df)

    if has_rs:
        df = compute_rs(df, idx_df)
    else:
        df["rs_pass"] = False
        print(f"  Warning: {INDEX_SYMBOL} not found in DB — RS filter disabled.\n")

    episodes = zl_rising_episodes(df["zl25"])

    ep_rows        = []
    trades_with_rs = []   # ZL + squeeze + RS
    trades_no_rs   = []   # ZL + squeeze only (no RS gate)

    for ep_start, ep_end in episodes:
        ep_slice  = df.iloc[ep_start : ep_end + 1]
        sqz_mask  = ep_slice["squeeze"]
        sqz_dates = ep_slice.loc[sqz_mask, "date"].tolist()
        sqz_idxs  = ep_slice.loc[sqz_mask].index.tolist()

        # Squeeze + RS passing bars
        sqzrs_mask  = sqz_mask & ep_slice["rs_pass"]
        sqzrs_dates = ep_slice.loc[sqzrs_mask, "date"].tolist()
        sqzrs_idxs  = ep_slice.loc[sqzrs_mask].index.tolist()

        row = dict(
            ep_start_date = df.at[ep_start, "date"],
            ep_end_date   = df.at[ep_end,   "date"],
            ep_bars       = ep_end - ep_start + 1,
            sqz_dates     = sqz_dates,
            sqzrs_dates   = sqzrs_dates,
            signal_rs     = None,   # signal date with RS
            signal_no_rs  = None,   # signal date without RS gate
        )

        # Trade with RS gate: first bar where squeeze AND rs_pass
        if sqzrs_idxs:
            sig = sqzrs_idxs[0]
            row["signal_rs"] = df.at[sig, "date"]
            trade = simulate_trade(df, sig)
            if trade:
                trades_with_rs.append(trade)

        # Trade without RS gate: first squeeze bar (for comparison)
        if sqz_idxs:
            sig_nors = sqz_idxs[0]
            row["signal_no_rs"] = df.at[sig_nors, "date"]
            trade_nors = simulate_trade(df, sig_nors)
            if trade_nors:
                trades_no_rs.append(trade_nors)

        ep_rows.append(row)

    _print_episodes(symbol, ep_rows, has_rs)
    _print_trades(symbol, trades_with_rs, label="With RS filter  (ZL + Squeeze + RS)")
    if has_rs:
        _print_trades(symbol, trades_no_rs,   label="Without RS filter (ZL + Squeeze only)")


# ── Output ────────────────────────────────────────────────────────────────────

def _fmt_date(d) -> str:
    return str(d)[:10] if d is not None else "—"


def _print_episodes(symbol: str, ep_rows: list, has_rs: bool) -> None:
    w = 80
    print(f"\n{'='*w}")
    print(f"  ZL Rising Episodes — {symbol}   ({len(ep_rows)} total)")
    print(f"  Sqz = squeeze bars   SqzRS = squeeze AND RS passing   * = entry signal taken")
    print(f"{'='*w}")
    print(f"  {'Start':12} {'End':12} {'Bars':>5}  {'Sqz':>4} {'SqzRS':>6}  Squeeze dates (while ZL rising)")
    print(f"  {'-'*12} {'-'*12} {'-'*5}  {'-'*4} {'-'*6}  {'-'*38}")

    for r in ep_rows:
        sqz   = r["sqz_dates"]
        sqzrs = r["sqzrs_dates"]
        ns, nr = len(sqz), len(sqzrs)

        if ns:
            shown   = [_fmt_date(d) for d in sqz[:4]]
            sqz_str = ", ".join(shown) + (f"  (+{ns-4} more)" if ns > 4 else "")
        else:
            sqz_str = "—"

        marker = ""
        if r["signal_rs"]:
            marker = "  * RS+Sqz"
        elif r["signal_no_rs"] and has_rs:
            marker = "  * Sqz only (RS fail)"

        print(
            f"  {_fmt_date(r['ep_start_date']):12} {_fmt_date(r['ep_end_date']):12}"
            f" {r['ep_bars']:>5}  {ns:>4} {nr:>6}  {sqz_str}{marker}"
        )


def _trade_summary(trades: list) -> None:
    if not trades:
        print("  No trades.")
        return
    wins   = [t for t in trades if t["pnl_pct"] > 0]
    losses = [t for t in trades if t["pnl_pct"] <= 0]
    r_vals = [t["r_mult"] for t in trades]
    print(f"  Win rate:    {len(wins)}/{len(trades)} = {len(wins)/len(trades)*100:.0f}%")
    if wins:
        print(f"  Avg win:     +{sum(t['pnl_pct'] for t in wins)/len(wins):.1f}%"
              f"   ({sum(t['r_mult'] for t in wins)/len(wins):.2f}R)")
    if losses:
        print(f"  Avg loss:    {sum(t['pnl_pct'] for t in losses)/len(losses):.1f}%"
              f"   ({sum(t['r_mult'] for t in losses)/len(losses):.2f}R)")
    print(f"  Expectancy:  {sum(r_vals)/len(trades):.2f}R per trade")
    print(f"  T1 hit rate: {sum(1 for t in trades if t['hit_t1'])}/{len(trades)}")
    reasons = {}
    for t in trades:
        reasons[t["exit_reason"]] = reasons.get(t["exit_reason"], 0) + 1
    print(f"  Exits:       { {k: v for k, v in sorted(reasons.items())} }")


def _print_trades(symbol: str, trades: list, label: str) -> None:
    w = 80
    print(f"\n{'='*w}")
    n = len(trades)
    wins = sum(1 for t in trades if t["pnl_pct"] > 0)
    print(f"  {label}")
    print(f"  {symbol}   {n} trades  {wins}W / {n-wins}L")
    print(f"{'='*w}")

    if not trades:
        print(f"  No trades.\n")
        return

    print(
        f"  {'Signal':12} {'Entry':12} {'Px':>8} {'Stop':>7}"
        f" {'Exit Px':>8} {'Exit Dt':12} {'P&L%':>7} {'R':>6}  Reason"
    )
    print(
        f"  {'-'*12} {'-'*12} {'-'*8} {'-'*7}"
        f" {'-'*8} {'-'*12} {'-'*7} {'-'*6}  {'-'*14}"
    )
    for t in trades:
        flag    = "W" if t["pnl_pct"] > 0 else "L"
        t1_flag = " [T1]" if t["hit_t1"] else ""
        print(
            f"  {_fmt_date(t['signal_date']):12} {_fmt_date(t['entry_date']):12}"
            f" {t['entry']:>8.2f} {t['stop']:>7.2f}"
            f" {t['exit']:>8.2f} {_fmt_date(t['exit_date']):12}"
            f" {t['pnl_pct']:>+7.1f}% {t['r_mult']:>+6.2f}R"
            f"  {t['exit_reason']}{t1_flag} {flag}"
        )

    print(f"\n  {'─'*44}")
    _trade_summary(trades)
    print(f"  {'─'*44}\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="ZL + Squeeze + RS Backtest — any NSE symbol")
    ap.add_argument("symbol",     help="NSE symbol, e.g. KRN")
    ap.add_argument("--lookback", type=int, default=600, help="bars of history (default 600)")
    args = ap.parse_args()
    run(args.symbol.upper(), args.lookback)
