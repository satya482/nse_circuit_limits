#!/usr/bin/env python3
"""NSE F&O ZLEMA25 scanner with EMA25 ZL gate and report parity.

The symbol source is NSE's ``SECURITIES IN F&O`` universe through
``fno_universe.py``. TradingView supplies the same eligibility and float data
used by ``ema25_zl_scanner.py``; all analysis and enrichment is delegated to
that scanner.
"""

import os
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

import ema25_zl_scanner as broad
from fno_universe import get_fno_symbols
from ohlc_db import get_names, load_ohlc

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "fno_zlema25_scans")
MD_FILE = os.path.join(SCANS_DIR, "fno_zlema25_scans.md")
TODAY = datetime.now().strftime("%Y-%m-%d")
BENCHMARK = "NIFTY MIDSML 400"


def intersect_universe(
    fno_symbols: list[str], eligible_symbols: list[str]
) -> list[str]:
    """Return unique TradingView-eligible F&O symbols in NSE source order."""
    eligible = set(eligible_symbols)
    seen = set()
    intersection = []
    for symbol in fno_symbols:
        if symbol in eligible and symbol not in seen:
            intersection.append(symbol)
            seen.add(symbol)
    return intersection


def _load_benchmark() -> pd.Series:
    raw = load_ohlc(BENCHMARK)
    if raw is None or raw.empty:
        raise RuntimeError(f"Benchmark {BENCHMARK} is unavailable; run fetch_data.py first")
    frame = raw.set_index("date")
    frame.index = pd.to_datetime(frame.index)
    return frame["close"].astype(float)


def main() -> int:
    try:
        os.makedirs(SCANS_DIR, exist_ok=True)

        print("\nLoading NSE F&O universe...")
        fno_symbols = get_fno_symbols()

        print(f"\nLoading {BENCHMARK} from DB...")
        index_s = _load_benchmark()
        print(
            f"  Index data: {len(index_s)} days  "
            f"(latest: {index_s.index[-1].date()}  {index_s.iloc[-1]:.2f})"
        )

        print("\nFetching NSE circuit limits...")
        circuit = broad.get_circuit_limits()

        print("\nFetching EMA25-parity eligibility from TradingView...")
        eligible_symbols, float_map = broad.get_watchlist()
        symbols = intersect_universe(fno_symbols, eligible_symbols)
        print(
            f"  NSE F&O source: {len(fno_symbols)}  |  "
            f"TradingView-eligible: {len(symbols)}  |  Scanning...\n"
        )

        findings = []
        for i, symbol in enumerate(symbols, 1):
            print(f"  {symbol:<20} ({i}/{len(symbols)})   ", end="\r")
            finding = broad.analyse(
                symbol,
                index_s,
                float_shares=float_map.get(symbol, 0),
            )
            if finding:
                findings.append(finding)

        names = get_names([finding["symbol"] for finding in findings])
        report = broad.build_markdown(
            findings,
            circuit,
            names,
            title=f"NSE F&O ZLEMA25 Scan — {TODAY}",
            universe_label="NSE F&O underlyings eligible under broad EMA25 ZL filters",
            directional=True,
            universe_stats=(
                f"{len(fno_symbols)} NSE F&O stocks · "
                f"{len(symbols)} TradingView-eligible"
            ),
        )

        dated_file = os.path.join(SCANS_DIR, f"fno_zlema25_scans_{TODAY}.md")
        Path(MD_FILE).write_text(report, encoding="utf-8", newline="\n")
        Path(dated_file).write_text(report, encoding="utf-8", newline="\n")

        uptrend = sum(finding.get("zl_direction") == "up" for finding in findings)
        downtrend = sum(finding.get("zl_direction") == "down" for finding in findings)
        flat = sum(finding.get("zl_direction") == "flat" for finding in findings)
        print(
            f"\n  Passed gates: {len(findings)}  |  Uptrend: {uptrend}  |  "
            f"Downtrend: {downtrend}  |  Flat: {flat}"
        )
        print(f"  Saved -> {MD_FILE}")
        print(f"  Saved -> {dated_file}")
        return 0
    except Exception as exc:
        print(f"\n  ERROR: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
