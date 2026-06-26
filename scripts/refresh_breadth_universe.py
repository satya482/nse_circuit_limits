#!/usr/bin/env python3
"""
Weekly manual script — pull NSE EQ instruments from Kite → data/breadth_universe.csv

Run: python scripts/refresh_breadth_universe.py
Requires active Kite token in ema-compression-scanner/.env

Universe: NSE exchange, EQ segment, no '-' in tradingsymbol (excludes SME/BE-series).
Refreshed weekly (Monday AM before market open).
"""

import sys
from datetime import date, timezone, timedelta
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "ema-compression-scanner"))
from data_loader import load_env, get_kite  # noqa: E402

ENV_PATH = ROOT / "ema-compression-scanner" / ".env"
OUT_PATH = ROOT / "data" / "breadth_universe.csv"
IST = timezone(timedelta(hours=5, minutes=30))


def filter_instruments(raw: pd.DataFrame) -> pd.DataFrame:
    """Filter raw Kite instruments to broad NSE EQ universe.
    Returns DataFrame with columns: symbol, instrument_token, name, generated_date.
    """
    today = date.today().isoformat()
    broad = raw[
        (raw["exchange"] == "NSE")
        & (raw["segment"] == "NSE")
        & (raw["instrument_type"] == "EQ")
        & (~raw["tradingsymbol"].str.contains("-", regex=False))
    ][["tradingsymbol", "instrument_token", "name"]].copy()
    broad = broad.rename(columns={"tradingsymbol": "symbol"})
    broad["generated_date"] = today
    return broad.reset_index(drop=True)


def main() -> None:
    env = load_env(ENV_PATH)
    kite = get_kite(env)

    print("Downloading NSE instruments from Kite...")
    raw = pd.DataFrame(kite.instruments("NSE"))

    broad = filter_instruments(raw)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    broad.to_csv(OUT_PATH, index=False)
    print(f"breadth_universe.csv: {len(broad)} symbols -> {OUT_PATH}")


if __name__ == "__main__":
    main()
