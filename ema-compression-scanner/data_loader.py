#!/usr/bin/env python3
"""Kite OHLCV fetcher with per-symbol parquet delta cache (CSV fallback for legacy files)."""

import csv
import time
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
from kiteconnect import KiteConnect


def load_env(env_path: Path) -> dict:
    env = {}
    with open(env_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env


def get_kite(env: dict) -> KiteConnect:
    kite = KiteConnect(api_key=env["KITE_API_KEY"])
    kite.set_access_token(env["KITE_ACCESS_TOKEN"])
    return kite


def load_instruments(kite: KiteConnect, cache_dir: Path) -> dict:
    """Return {tradingsymbol: instrument_token} for NSE EQ. Cached daily."""
    today = datetime.now().strftime("%Y-%m-%d")
    cache_file = cache_dir / f"instruments_{today}.csv"

    if not cache_file.exists():
        for old in cache_dir.glob("instruments_*.csv"):
            old.unlink()
        instruments = kite.instruments("NSE")
        df = pd.DataFrame(instruments)
        df.to_csv(cache_file, index=False)
    else:
        df = pd.read_csv(cache_file)

    eq = df[(df["segment"] == "NSE") & (df["instrument_type"] == "EQ")]
    return {row["tradingsymbol"]: int(row["instrument_token"]) for _, row in eq.iterrows()}


def load_benchmark_token(cache_dir: Path) -> int:
    """Return instrument_token for NIFTY MIDSML 400 from today's instruments cache."""
    today = datetime.now().strftime("%Y-%m-%d")
    cache_file = cache_dir / f"instruments_{today}.csv"
    df = pd.read_csv(cache_file)
    row = df[df["tradingsymbol"] == "NIFTY MIDSML 400"]
    if row.empty:
        raise RuntimeError("NIFTY MIDSML 400 not found in instruments cache — check instruments CSV")
    return int(row.iloc[0]["instrument_token"])


def load_universe(csv_path: str) -> list[dict]:
    """Return list of {symbol, name, sector, industry} from universe CSV."""
    rows = []
    with open(csv_path, newline="", encoding="cp1252") as f:
        reader = csv.DictReader(f)
        for row in reader:
            symbol = row.get("NSE Code", "").strip()
            if symbol:
                rows.append({
                    "symbol": symbol,
                    "name": row.get("Stock Name", "").strip(),
                    "sector": row.get("sector_name", "").strip(),
                    "industry": row.get("Industry Name", "").strip(),
                })
    return rows


def _load_cached(parquet_file: Path, csv_file: Path) -> pd.DataFrame | None:
    """Try parquet first (primary), fall back to CSV (legacy)."""
    if parquet_file.exists():
        try:
            df = pd.read_parquet(parquet_file)
            if "date" in df.columns:
                df["date"] = pd.to_datetime(df["date"]).dt.tz_localize(None)
            return df
        except Exception:
            pass
    if csv_file.exists():
        try:
            df = pd.read_csv(csv_file)
            df["date"] = pd.to_datetime(df["date"], utc=True).dt.tz_localize(None)
            return df
        except Exception:
            pass
    return None


def fetch_ohlc(
    kite: KiteConnect,
    instrument_token: int,
    symbol: str,
    cache_dir: Path,
    lookback_days: int = 400,
) -> pd.DataFrame | None:
    """Fetch OHLCV with parquet/CSV dual-read delta cache. Returns DataFrame or None on failure."""
    parquet_file = cache_dir / f"{symbol}.parquet"
    csv_file     = cache_dir / f"{symbol}.csv"
    to_date      = datetime.now().date()

    df_existing = _load_cached(parquet_file, csv_file)

    if df_existing is not None and not df_existing.empty:
        try:
            last_date = df_existing["date"].max().date()
            from_date = last_date + timedelta(days=1)
            if from_date > to_date:
                return df_existing
            new_data = kite.historical_data(instrument_token, from_date, to_date, "day")
            if new_data:
                df_new = pd.DataFrame(new_data)
                df_new["date"] = pd.to_datetime(df_new["date"]).dt.tz_localize(None)
                df_combined = pd.concat([df_existing, df_new], ignore_index=True)
                df_combined.drop_duplicates(subset=["date"], keep="last", inplace=True)
                df_combined.sort_values("date", inplace=True, ignore_index=True)
                df_combined.to_parquet(parquet_file, index=False)
                return df_combined
            return df_existing
        except Exception:
            # API error (e.g. expired token) — return cached data if sufficient
            if len(df_existing) >= 210:
                return df_existing

    from_date = to_date - timedelta(days=lookback_days)
    try:
        data = kite.historical_data(instrument_token, from_date, to_date, "day")
    except Exception:
        return None
    if not data:
        return None
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"]).dt.tz_localize(None)
    df.sort_values("date", inplace=True, ignore_index=True)
    df.to_parquet(parquet_file, index=False)
    return df


def fetch_benchmark(
    kite: KiteConnect,
    cache_dir: Path,
    lookback_days: int = 400,
) -> pd.DataFrame | None:
    """Fetch NiftyMidSml400 OHLCV for RS line calculation."""
    token = load_benchmark_token(cache_dir)
    return fetch_ohlc(kite, token, "NIFTYMIDSML400", cache_dir, lookback_days)


def fetch_all(
    kite: KiteConnect,
    universe: list[dict],
    instruments: dict,
    cache_dir: Path,
    lookback_days: int = 400,
    rate_limit: float = 0.35,
) -> dict[str, pd.DataFrame]:
    """Fetch OHLCV for all universe symbols. Returns {symbol: df}."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    results = {}
    total = len(universe)
    skipped = 0

    for i, stock in enumerate(universe, 1):
        sym = stock["symbol"]
        token = instruments.get(sym)
        if token is None:
            skipped += 1
            continue

        df = fetch_ohlc(kite, token, sym, cache_dir, lookback_days)
        if df is not None and len(df) >= 210:
            results[sym] = df

        if i % 50 == 0:
            print(f"  {i}/{total} fetched, {skipped} skipped...")
        time.sleep(rate_limit)

    print(f"  Done: {len(results)} loaded, {skipped} not in Kite instruments.")
    return results