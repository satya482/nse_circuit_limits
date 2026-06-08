"""
wavetrend_scanner.py
====================
Python replication of Satya WaveTrend with Crosses [LazyBear] v2 (Fixed)
for use in the daily NSE scanner via Claude Code.

Mirrors Pine Script v2 logic exactly, including all bug fixes:
  1. bullCross  → crossover()  (WT1 crosses ABOVE WT2 only)
  2. bearCross  → crossunder() (WT1 crosses BELOW WT2 only)
  3. Zone check → wt2 (slower line) only, not both wt1 AND wt2

Signal Rank Hierarchy (wt_signal_rank field):
  +5  BULL_OS_PPV      Bull cross in deep oversold + Pocket Pivot Volume (STRONGEST)
  +4  BULL_ANY_PPV     Bull cross (any level) + Pocket Pivot Volume
  +3  BULL_OVERSOLD    Bull cross in deep oversold (L1, -60)
  +2  BULL_OS_L2       Bull cross in soft oversold (L2, -53)
  +1  BULL_ZERO_CROSS  WT1 crosses above 0 (momentum confirmation)
   0  NONE             No signal today
  -1  BEAR_ANY         Bear cross at any level
  -2  BEAR_OB_L2       Bear cross in soft overbought (L2, +53)
  -3  BEAR_OB          Bear cross in deep overbought (L1, +60)

Usage in Claude Code daily scanner:
  from wavetrend_scanner import WaveTrendCalculator, scan_universe

  calc   = WaveTrendCalculator()
  result = scan_universe(universe_dict, calc, min_rank=1)
  # result is a DataFrame sorted by wt_signal_rank desc
  # merge into your existing scanner signal df on 'nse_code'
"""

from __future__ import annotations

import warnings
from dataclasses import dataclass
from typing import Dict, Optional, Tuple

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore", category=RuntimeWarning)


# ══════════════════════════════════════════════════════════════════════════════
# OUTPUT SCHEMA
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class WaveTrendSignal:
    """
    All WaveTrend fields for a single stock on today's date.
    Call .to_dict() to get a flat dict suitable for a DataFrame row.
    """

    # ── Raw oscillator values ─────────────────────────────────────────────────
    wt1:      float = np.nan   # WaveTrend line 1 (faster)
    wt2:      float = np.nan   # WaveTrend line 2 (slower, SMA-4 of wt1)
    wt_diff:  float = np.nan   # wt1 - wt2  (positive = bullish momentum)

    # ── Primary signal (human-readable, scanner display) ─────────────────────
    wt_signal:      str = "NONE"   # e.g. "BULL_OS_PPV"
    wt_signal_rank: int = 0        # -3 to +5, higher = stronger bull

    # ── Zone-specific crosses ─────────────────────────────────────────────────
    wt_bull_cross_os:     bool = False   # WT1 crossover WT2 while wt2 ≤ -60 (L1)
    wt_bull_cross_os_l2:  bool = False   # WT1 crossover WT2 while wt2 ≤ -53 (L2)
    wt_bear_cross_ob:     bool = False   # WT1 crossunder WT2 while wt2 ≥ +60 (L1)
    wt_bear_cross_ob_l2:  bool = False   # WT1 crossunder WT2 while wt2 ≥ +53 (L2)

    # ── Any-level crosses ─────────────────────────────────────────────────────
    wt_bull_cross_any:  bool = False
    wt_bear_cross_any:  bool = False

    # ── Zero-line crosses ─────────────────────────────────────────────────────
    wt_bull_cross_zero: bool = False   # WT1 crosses above 0
    wt_bear_cross_zero: bool = False   # WT1 crosses below 0

    # ── Pocket Pivot Volume ───────────────────────────────────────────────────
    wt_is_ppv:       bool = False   # Pocket Pivot Volume fires today
    wt_bull_ppv:     bool = False   # Bull cross (any) + PPV
    wt_bull_os_ppv:  bool = False   # Bull cross in oversold L1 + PPV (STRONGEST)

    # ── State ─────────────────────────────────────────────────────────────────
    wt_in_oversold:   bool = False   # wt1 ≤ -60
    wt_in_overbought: bool = False   # wt1 ≥ +60

    def to_dict(self) -> dict:
        """Flat dict → merge into scanner signal DataFrame."""
        return {
            "wt1":               round(float(self.wt1), 2)  if not np.isnan(self.wt1) else np.nan,
            "wt2":               round(float(self.wt2), 2)  if not np.isnan(self.wt2) else np.nan,
            "wt_diff":           round(float(self.wt_diff), 2) if not np.isnan(self.wt_diff) else np.nan,
            "wt_signal":         self.wt_signal,
            "wt_signal_rank":    self.wt_signal_rank,
            "wt_bull_cross_os":  self.wt_bull_cross_os,
            "wt_bull_cross_os_l2": self.wt_bull_cross_os_l2,
            "wt_bear_cross_ob":  self.wt_bear_cross_ob,
            "wt_bear_cross_ob_l2": self.wt_bear_cross_ob_l2,
            "wt_bull_cross_any": self.wt_bull_cross_any,
            "wt_bear_cross_any": self.wt_bear_cross_any,
            "wt_bull_cross_zero": self.wt_bull_cross_zero,
            "wt_bear_cross_zero": self.wt_bear_cross_zero,
            "wt_is_ppv":         self.wt_is_ppv,
            "wt_bull_ppv":       self.wt_bull_ppv,
            "wt_bull_os_ppv":    self.wt_bull_os_ppv,
            "wt_in_oversold":    self.wt_in_oversold,
            "wt_in_overbought":  self.wt_in_overbought,
        }


# ══════════════════════════════════════════════════════════════════════════════
# CORE CALCULATOR
# ══════════════════════════════════════════════════════════════════════════════

class WaveTrendCalculator:
    """
    Calculates WaveTrend oscillator + Pocket Pivot Volume signals
    from OHLCV data. All parameters match the Pine Script defaults.

    Parameters
    ----------
    n1          : Channel Length (EMA period for hlc3 smoothing), default 10
    n2          : Average Length (EMA period for CI), default 21
    ob_level1   : Overbought Level 1, default +60
    ob_level2   : Overbought Level 2, default +53
    os_level1   : Oversold Level 1, default -60
    os_level2   : Oversold Level 2, default -53
    pp_len      : Pocket Pivot lookback in trading days, default 10
    vol_ma_len  : Volume MA period (context only), default 50
    """

    def __init__(
        self,
        n1:         int   = 10,
        n2:         int   = 21,
        ob_level1:  float = 60.0,
        ob_level2:  float = 53.0,
        os_level1:  float = -60.0,
        os_level2:  float = -53.0,
        pp_len:     int   = 10,
        vol_ma_len: int   = 50,
    ):
        self.n1         = n1
        self.n2         = n2
        self.ob_level1  = ob_level1
        self.ob_level2  = ob_level2
        self.os_level1  = os_level1
        self.os_level2  = os_level2
        self.pp_len     = pp_len
        self.vol_ma_len = vol_ma_len

        # Minimum bars needed for stable EMA warmup
        # (3× longest period + SMA-4 + headroom)
        self._min_bars = max(self.n1 + self.n2 * 3 + 10, 60)

    # ── EMA / SMA helpers ────────────────────────────────────────────────────

    @staticmethod
    def _ema(series: pd.Series, period: int) -> pd.Series:
        """
        Exponential Moving Average.
        adjust=False mirrors Pine Script ta.ema() (recursive definition).
        """
        return series.ewm(span=period, adjust=False).mean()

    @staticmethod
    def _sma(series: pd.Series, period: int) -> pd.Series:
        """Simple Moving Average. min_periods=period mirrors Pine Script ta.sma()."""
        return series.rolling(window=period, min_periods=period).mean()

    # ── Cross helpers ────────────────────────────────────────────────────────

    @staticmethod
    def _crossover(s1: pd.Series, s2: pd.Series) -> pd.Series:
        """
        s1 crosses ABOVE s2.
        Current:  s1 > s2
        Previous: s1 ≤ s2
        Mirrors ta.crossover(s1, s2).
        """
        return (s1 > s2) & (s1.shift(1) <= s2.shift(1))

    @staticmethod
    def _crossunder(s1: pd.Series, s2: pd.Series) -> pd.Series:
        """
        s1 crosses BELOW s2.
        Current:  s1 < s2
        Previous: s1 ≥ s2
        Mirrors ta.crossunder(s1, s2).
        """
        return (s1 < s2) & (s1.shift(1) >= s2.shift(1))

    # ── WaveTrend calculation ────────────────────────────────────────────────

    def _calc_wavetrend(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Adds wt1, wt2, wt_diff to df.
        Exact Pine Script formula:
            ap  = hlc3
            esa = EMA(ap, n1)
            d   = EMA(|ap - esa|, n1)
            ci  = (ap - esa) / (0.015 * d)
            tci = EMA(ci, n2)
            wt1 = tci
            wt2 = SMA(wt1, 4)
        """
        df = df.copy()
        ap  = (df["high"] + df["low"] + df["close"]) / 3
        esa = self._ema(ap, self.n1)
        d   = self._ema((ap - esa).abs(), self.n1)
        ci  = (ap - esa) / (0.015 * d)
        tci = self._ema(ci, self.n2)

        df["wt1"]    = tci
        df["wt2"]    = self._sma(df["wt1"], 4)
        df["wt_diff"]= df["wt1"] - df["wt2"]
        return df

    # ── Cross signals (full history) ─────────────────────────────────────────

    def _calc_cross_signals(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Adds all cross signal boolean columns for ALL bars.
        Useful for backtesting or historical analysis.
        """
        wt1  = df["wt1"]
        wt2  = df["wt2"]
        zero = pd.Series(0.0, index=wt1.index)

        # ── FIXED: crossover/crossunder with wt2 zone check ──────────────────
        df["wt_bull_cross_os"]    = self._crossover(wt1, wt2) & (wt2 <= self.os_level1)
        df["wt_bull_cross_os_l2"] = self._crossover(wt1, wt2) & (wt2 <= self.os_level2)
        df["wt_bear_cross_ob"]    = self._crossunder(wt1, wt2) & (wt2 >= self.ob_level1)
        df["wt_bear_cross_ob_l2"] = self._crossunder(wt1, wt2) & (wt2 >= self.ob_level2)
        df["wt_bull_cross_any"]   = self._crossover(wt1, wt2)
        df["wt_bear_cross_any"]   = self._crossunder(wt1, wt2)
        df["wt_bull_cross_zero"]  = self._crossover(wt1, zero)
        df["wt_bear_cross_zero"]  = self._crossunder(wt1, zero)

        # State
        df["wt_in_oversold"]   = wt1 <= self.os_level1
        df["wt_in_overbought"] = wt1 >= self.ob_level1

        return df

    # ── Pocket Pivot Volume (last bar only, fast) ────────────────────────────

    def _calc_pocket_pivot_today(
        self,
        close:  np.ndarray,
        volume: np.ndarray,
    ) -> Tuple[bool, float, int]:
        """
        Pocket Pivot Volume for the LAST (today's) bar.
        Mirrors the Pine Script loop EXACTLY:

            for i = 1 to 500
                if seen >= ppLen: break
                if isDown[i]:
                    maxDownVol = max(maxDownVol, volume[i])
                    seen += 1

        Returns
        -------
        is_ppv       : True if PPV signal fires today
        max_down_vol : Highest down-day volume in last pp_len down days
        seen         : Number of down days found (must == pp_len for signal)
        """
        n = len(close)
        if n < 2:
            return False, 0.0, 0

        is_up_today = close[-1] > close[-2]
        today_vol   = volume[-1]

        seen         = 0
        max_down_vol = 0.0

        # Walk backwards from yesterday (i=1 in Pine Script)
        for i in range(1, min(501, n)):
            if seen >= self.pp_len:       # mirrors Pine Script break condition
                break
            bar = n - 1 - i               # absolute index of bar[i]
            if bar < 1:
                break
            is_down = close[bar] < close[bar - 1]
            if is_down:
                max_down_vol = max(max_down_vol, volume[bar])
                seen += 1

        is_ppv = is_up_today and (today_vol > max_down_vol) and (seen == self.pp_len)
        return is_ppv, max_down_vol, seen

    # ── Main entry point: single stock ───────────────────────────────────────

    def get_signal(self, df: pd.DataFrame) -> WaveTrendSignal:
        """
        Get today's WaveTrend signal for a single stock.

        Parameters
        ----------
        df : pd.DataFrame
            OHLCV data. Must have columns (case-insensitive):
                open, high, low, close, volume
            Index: datetime, sorted ascending.
            Recommended: ≥100 bars for stable EMA warmup.

        Returns
        -------
        WaveTrendSignal
            All signal fields. Use .to_dict() to add to scanner DataFrame.
        """
        if df is None or len(df) < self._min_bars:
            return WaveTrendSignal()

        # Normalise column names
        df = df.copy()
        df.columns = [c.lower() for c in df.columns]

        required = {"open", "high", "low", "close", "volume"}
        if not required.issubset(df.columns):
            missing = required - set(df.columns)
            raise ValueError(f"Missing columns: {missing}")

        # ── Calculate WaveTrend ───────────────────────────────────────────────
        df = self._calc_wavetrend(df)
        df = self._calc_cross_signals(df)

        last = df.iloc[-1]

        wt1_val  = float(last["wt1"])
        wt2_val  = float(last["wt2"])
        wt_diff  = float(last["wt_diff"])

        # ── Pocket Pivot (raw arrays for speed) ───────────────────────────────
        is_ppv, _, _ = self._calc_pocket_pivot_today(
            df["close"].values, df["volume"].values
        )

        # ── Read cross flags ──────────────────────────────────────────────────
        bull_os     = bool(last["wt_bull_cross_os"])
        bull_os_l2  = bool(last["wt_bull_cross_os_l2"])
        bear_ob     = bool(last["wt_bear_cross_ob"])
        bear_ob_l2  = bool(last["wt_bear_cross_ob_l2"])
        bull_any    = bool(last["wt_bull_cross_any"])
        bear_any    = bool(last["wt_bear_cross_any"])
        bull_zero   = bool(last["wt_bull_cross_zero"])
        bear_zero   = bool(last["wt_bear_cross_zero"])
        in_os       = bool(last["wt_in_oversold"])
        in_ob       = bool(last["wt_in_overbought"])

        # ── Combined signals ──────────────────────────────────────────────────
        bull_ppv    = bull_any and is_ppv
        bull_os_ppv = bull_os  and is_ppv

        # ── Signal rank (priority ladder) ────────────────────────────────────
        if bull_os_ppv:
            signal, rank = "BULL_OS_PPV",    5
        elif bull_ppv:
            signal, rank = "BULL_ANY_PPV",   4
        elif bull_os:
            signal, rank = "BULL_OVERSOLD",  3
        elif bull_os_l2:
            signal, rank = "BULL_OS_L2",     2
        elif bull_zero:
            signal, rank = "BULL_ZERO_CROSS", 1
        elif bear_ob:
            signal, rank = "BEAR_OB",       -3
        elif bear_ob_l2:
            signal, rank = "BEAR_OB_L2",    -2
        elif bear_any:
            signal, rank = "BEAR_ANY",      -1
        else:
            signal, rank = "NONE",           0

        return WaveTrendSignal(
            wt1=wt1_val,
            wt2=wt2_val,
            wt_diff=wt_diff,
            wt_signal=signal,
            wt_signal_rank=rank,
            wt_bull_cross_os=bull_os,
            wt_bull_cross_os_l2=bull_os_l2,
            wt_bear_cross_ob=bear_ob,
            wt_bear_cross_ob_l2=bear_ob_l2,
            wt_bull_cross_any=bull_any,
            wt_bear_cross_any=bear_any,
            wt_bull_cross_zero=bull_zero,
            wt_bear_cross_zero=bear_zero,
            wt_is_ppv=is_ppv,
            wt_bull_ppv=bull_ppv,
            wt_bull_os_ppv=bull_os_ppv,
            wt_in_oversold=in_os,
            wt_in_overbought=in_ob,
        )

    def get_history(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Get WaveTrend signals for ALL historical bars.
        Useful for backtesting or signal history visualization.

        Returns
        -------
        pd.DataFrame with wt1, wt2, wt_diff, and all cross flag columns.
        PPV column is NOT included here (use get_signal() for last bar PPV).
        """
        df = df.copy()
        df.columns = [c.lower() for c in df.columns]
        df = self._calc_wavetrend(df)
        df = self._calc_cross_signals(df)
        return df


# ══════════════════════════════════════════════════════════════════════════════
# UNIVERSE SCANNER
# ══════════════════════════════════════════════════════════════════════════════

def scan_universe(
    universe:   Dict[str, pd.DataFrame],
    calculator: Optional[WaveTrendCalculator] = None,
    min_rank:   int = 1,
) -> pd.DataFrame:
    """
    Scan all stocks in the 962-stock universe for WaveTrend signals today.

    Parameters
    ----------
    universe   : {nse_code: ohlcv_df}
                 Each DataFrame must have open/high/low/close/volume columns.
    calculator : WaveTrendCalculator instance. Uses default params if None.
    min_rank   : Only return rows where wt_signal_rank >= min_rank.
                 1  = any bull signal
                 3  = oversold crosses only
                 4  = PPV confirmation required
                 5  = deep oversold + PPV (strongest filter)

    Returns
    -------
    pd.DataFrame sorted by wt_signal_rank desc (strongest signal at top).
    Merge with your existing scanner df on 'nse_code'.

    Example
    -------
    >>> from wavetrend_scanner import WaveTrendCalculator, scan_universe
    >>> calc = WaveTrendCalculator()
    >>> wt_df = scan_universe(universe_dict, calc, min_rank=3)
    >>> scanner_df = scanner_df.merge(wt_df, on="nse_code", how="left")
    """
    if calculator is None:
        calculator = WaveTrendCalculator()

    rows = []
    errors = []

    for ticker, df in universe.items():
        try:
            sig = calculator.get_signal(df)
            if sig.wt_signal_rank >= min_rank:
                row = {"nse_code": ticker}
                row.update(sig.to_dict())
                rows.append(row)
        except Exception as exc:
            errors.append((ticker, str(exc)))

    if errors:
        print(f"[WaveTrendScanner] {len(errors)} stocks skipped:")
        for t, e in errors[:10]:
            print(f"  {t}: {e}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")

    if not rows:
        print("[WaveTrendScanner] No signals found at min_rank={min_rank}")
        return pd.DataFrame()

    result = pd.DataFrame(rows)
    result = result.sort_values("wt_signal_rank", ascending=False)
    result = result.reset_index(drop=True)
    return result


# ══════════════════════════════════════════════════════════════════════════════
# WEBHOOK ALERT PARSER
# (optional: parse TradingView webhook messages into the same schema)
# ══════════════════════════════════════════════════════════════════════════════

def parse_alert_message(message: str) -> dict:
    """
    Parse a pipe-delimited TradingView webhook alert message
    into a structured dict.

    Alert message format (set in Pine Script):
        SIGNAL_TYPE|TICKER|Description|TF:timeframe

    Example:
        "BULL_OS_PPV|RELIANCE|Bull WT cross in OVERSOLD zone + PPV|TF:D"

    Returns
    -------
    {
        "signal_type": "BULL_OS_PPV",
        "ticker":      "RELIANCE",
        "description": "Bull WT cross in OVERSOLD zone + PPV",
        "timeframe":   "D",
        "raw":         "BULL_OS_PPV|RELIANCE|..."
    }
    """
    parts = [p.strip() for p in message.split("|")]
    return {
        "signal_type": parts[0] if len(parts) > 0 else "",
        "ticker":      parts[1] if len(parts) > 1 else "",
        "description": parts[2] if len(parts) > 2 else "",
        "timeframe":   parts[3].replace("TF:", "") if len(parts) > 3 else "",
        "raw":         message,
    }


# ══════════════════════════════════════════════════════════════════════════════
# SMOKE TEST
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    """
    Quick smoke test using yfinance.
    Replace with your NSE OHLCV data source in production
    (Kite API / BhavCopy / Breeze / etc.)
    """
    try:
        import yfinance as yf
    except ImportError:
        print("Install yfinance for smoke test: pip install yfinance")
        raise

    calc = WaveTrendCalculator()

    test_tickers = {
        "RELIANCE": "RELIANCE.NS",
        "INFY":     "INFY.NS",
        "HDFCBANK": "HDFCBANK.NS",
    }

    universe = {}
    for nse_code, yf_ticker in test_tickers.items():
        try:
            df = yf.download(yf_ticker, period="1y", interval="1d",
                             auto_adjust=True, progress=False)
            if len(df) > 0:
                df.columns = [c.lower() for c in df.columns]
                universe[nse_code] = df
                print(f"  Loaded {nse_code}: {len(df)} bars")
        except Exception as e:
            print(f"  Failed {nse_code}: {e}")

    print("\n=== Scanning universe (min_rank=1) ===")
    result = scan_universe(universe, calc, min_rank=1)

    if not result.empty:
        display_cols = [
            "nse_code", "wt_signal", "wt_signal_rank",
            "wt1", "wt2", "wt_diff",
            "wt_in_oversold", "wt_is_ppv", "wt_bull_os_ppv"
        ]
        print(result[display_cols].to_string(index=False))
    else:
        print("No signals today.")

    # ── Test alert parser ─────────────────────────────────────────────────────
    print("\n=== Alert Parser Test ===")
    test_msg = "BULL_OS_PPV|RELIANCE|Bull WT cross in OVERSOLD + PPV|TF:D"
    parsed = parse_alert_message(test_msg)
    for k, v in parsed.items():
        print(f"  {k:<15} {v}")
