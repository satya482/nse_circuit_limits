from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from disclaimer import SEBI_MD_FOOTER, SEBI_MD_HEADER
from ohlc_db import load_ohlc

BENCHMARK = "NIFTY MIDSML 400"
ZLEMA_PERIOD = 25
RS_EMA_PERIOD = 9
MIN_DAILY_BARS = 25
MIN_WEEKLY_BARS = 9
TRADE_COLUMNS = [
    "symbol",
    "entry_date",
    "entry_close",
    "exit_date",
    "exit_close",
    "return_pct",
    "holding_trading_days",
    "holding_calendar_days",
    "exit_reason",
]
OPEN_COLUMNS = [
    "symbol",
    "entry_date",
    "entry_close",
    "last_date",
    "last_close",
    "unrealized_return_pct",
    "holding_trading_days",
    "holding_calendar_days",
]
SUMMARY_COLUMNS = [
    "symbol",
    "trades",
    "wins",
    "losses",
    "zeros",
    "win_rate_pct",
    "average_return_pct",
    "median_return_pct",
    "compounded_return_pct",
    "best_return_pct",
    "worst_return_pct",
    "average_holding_days",
]


def zlema(close: pd.Series, period: int = ZLEMA_PERIOD) -> pd.Series:
    first = close.astype(float).ewm(span=period, adjust=False).mean()
    return 2 * first - first.ewm(span=period, adjust=False).mean()


def _walk_forward_weekly_ema(
    daily_rs: pd.Series, period: int = RS_EMA_PERIOD
) -> pd.DataFrame:
    alpha = 2.0 / (period + 1.0)
    current_ema = np.nan
    completed_weeks = 0
    rows = []
    for _, week in daily_rs.groupby(daily_rs.index.to_period("W-SUN"), sort=True):
        prior_ema = current_ema
        for date, value in week.items():
            partial_ema = (
                float(value)
                if pd.isna(prior_ema)
                else alpha * float(value) + (1 - alpha) * prior_ema
            )
            ready = completed_weeks + 1 >= MIN_WEEKLY_BARS and not pd.isna(prior_ema)
            rows.append(
                (
                    date,
                    partial_ema if ready else np.nan,
                    prior_ema if ready else np.nan,
                )
            )
        final_value = float(week.iloc[-1])
        current_ema = (
            final_value
            if pd.isna(prior_ema)
            else alpha * final_value + (1 - alpha) * prior_ema
        )
        completed_weeks += 1
    return pd.DataFrame(
        rows, columns=["date", "weekly_rs_ema9", "prior_week_rs_ema9"]
    ).set_index("date")


def build_indicator_frame(
    stock_df: pd.DataFrame, benchmark_df: pd.DataFrame
) -> pd.DataFrame:
    stock = stock_df[["date", "close"]].copy()
    bench = benchmark_df[["date", "close"]].copy()
    stock["date"] = pd.to_datetime(stock["date"])
    bench["date"] = pd.to_datetime(bench["date"])
    merged = stock.merge(
        bench, on="date", suffixes=("", "_benchmark"), how="inner"
    ).sort_values("date")
    merged = merged.drop_duplicates("date").reset_index(drop=True)
    merged["zlema25"] = zlema(merged["close"])
    merged["daily_rs"] = merged["close"] / merged["close_benchmark"] * 1000.0
    rs = merged.set_index("date")["daily_rs"]
    weekly = _walk_forward_weekly_ema(rs)
    merged = merged.join(weekly, on="date")
    merged["rs_above_ema9"] = merged["daily_rs"] > merged["weekly_rs_ema9"]
    merged["rs_ema9_rising"] = (
        merged["weekly_rs_ema9"] > merged["prior_week_rs_ema9"]
    )
    zl_up = merged["zlema25"] > merged["zlema25"].shift(1)
    zl_was_not_up = merged["zlema25"].shift(1) <= merged["zlema25"].shift(2)
    enough_daily = pd.Series(merged.index >= MIN_DAILY_BARS - 1, index=merged.index)
    merged["entry_signal"] = (
        enough_daily
        & zl_up
        & zl_was_not_up
        & merged["rs_above_ema9"]
        & merged["rs_ema9_rising"]
    )
    return merged[
        [
            "date",
            "close",
            "zlema25",
            "daily_rs",
            "weekly_rs_ema9",
            "prior_week_rs_ema9",
            "rs_above_ema9",
            "rs_ema9_rising",
            "entry_signal",
        ]
    ]


def simulate_stock(
    symbol: str, frame: pd.DataFrame, start: pd.Timestamp, end: pd.Timestamp
) -> tuple[pd.DataFrame, pd.DataFrame]:
    data = frame.loc[frame["date"] <= end].reset_index(drop=True)
    completed = []
    opened = []
    position = None
    for i, row in data.iterrows():
        if position is None:
            if row["date"] >= start and bool(row["entry_signal"]):
                position = {
                    "entry_i": i,
                    "entry_date": row["date"],
                    "entry_close": float(row["close"]),
                }
            continue

        zl_down = bool(row["zlema25"] < data.at[i - 1, "zlema25"])
        rs_stopped = not bool(row["rs_ema9_rising"])
        if zl_down or rs_stopped:
            reason = (
                "ZLEMA_AND_RS"
                if zl_down and rs_stopped
                else ("ZLEMA_DOWN" if zl_down else "RS_NOT_RISING")
            )
            exit_close = float(row["close"])
            completed.append(
                {
                    "symbol": symbol,
                    **position,
                    "exit_date": row["date"],
                    "exit_close": exit_close,
                    "return_pct": (
                        exit_close / position["entry_close"] - 1.0
                    )
                    * 100.0,
                    "holding_trading_days": i - position["entry_i"],
                    "holding_calendar_days": (
                        row["date"] - position["entry_date"]
                    ).days,
                    "exit_reason": reason,
                }
            )
            completed[-1].pop("entry_i")
            position = None

    if position is not None and not data.empty:
        last = data.iloc[-1]
        last_close = float(last["close"])
        opened.append(
            {
                "symbol": symbol,
                "entry_date": position["entry_date"],
                "entry_close": position["entry_close"],
                "last_date": last["date"],
                "last_close": last_close,
                "unrealized_return_pct": (
                    last_close / position["entry_close"] - 1.0
                )
                * 100.0,
                "holding_trading_days": len(data) - 1 - position["entry_i"],
                "holding_calendar_days": (
                    last["date"] - position["entry_date"]
                ).days,
            }
        )
    return (
        pd.DataFrame(completed, columns=TRADE_COLUMNS),
        pd.DataFrame(opened, columns=OPEN_COLUMNS),
    )


def summarize_trades(trades: pd.DataFrame, symbols: list[str]) -> pd.DataFrame:
    rows = []
    for symbol in [*symbols, "COMBINED"]:
        group = trades if symbol == "COMBINED" else trades.loc[trades["symbol"] == symbol]
        n = len(group)
        returns = group["return_pct"].astype(float) if n else pd.Series(dtype=float)
        rows.append(
            {
                "symbol": symbol,
                "trades": n,
                "wins": int((returns > 0).sum()),
                "losses": int((returns < 0).sum()),
                "zeros": int((returns == 0).sum()),
                "win_rate_pct": float((returns > 0).mean() * 100)
                if n
                else np.nan,
                "average_return_pct": float(returns.mean()) if n else np.nan,
                "median_return_pct": float(returns.median()) if n else np.nan,
                "compounded_return_pct": float(
                    ((1 + returns / 100).prod() - 1) * 100
                )
                if n
                else np.nan,
                "best_return_pct": float(returns.max()) if n else np.nan,
                "worst_return_pct": float(returns.min()) if n else np.nan,
                "average_holding_days": float(
                    group["holding_trading_days"].mean()
                )
                if n
                else np.nan,
            }
        )
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)
