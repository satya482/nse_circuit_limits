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
