#!/usr/bin/env python3
"""
Float Trap Gate — NSE swing trading liquidity screen.

Prevents entry into stocks where exit risk is unacceptable due to thin free float.
Import and call from any scanner:

    from float_gate import float_metrics, passes_hard_gate, trap_label

Data contract:
  close_series  : pd.Series of close prices, at least 20 bars, any index
  volume_series : pd.Series of volume counts, same index as close_series
  float_shares  : float | None — absolute share count from TV screener
                  (float_shares_outstanding field).
                  If None / zero: gate is skipped (no data ≠ bad stock).

Thresholds (shared across all scanners — tune here):
  FF_MCAP_GREEN  ≥ 300 Cr   yellow ≥ 150 Cr   red < 150 Cr
  FF_TURN_GREEN  ≥ 0.5%     yellow ≥ 0.3%     red < 0.3%
  FT_20_YELLOW   < 1.0×     (1 danger pt)
"""

from __future__ import annotations

import pandas as pd

FF_MCAP_GREEN = 300.0  # Cr
FF_MCAP_YELLOW = 150.0  # Cr  ← hard gate floor
FF_TURN_GREEN = 0.5  # %
FF_TURN_YELLOW = 0.3  # %   ← hard gate floor
FT_20_YELLOW = 1.0  # ×


def float_metrics(
    close_series: pd.Series,
    volume_series: pd.Series,
    float_shares: float | None,
) -> dict | None:
    """
    Compute free-float tradability metrics from price/volume history.

    Returns dict:
      ff_mcap_cr   : free-float market cap in ₹ Crores
      ff_turn_pct  : avg 20-day daily traded value as % of free-float value
      ft_20d       : times the full float changed hands over last 20 sessions
      avg20_val    : avg 20-day daily traded value in ₹ (for exit-days calc upstream)

    Returns None when float_shares is missing/zero — caller treats as no-data,
    not as a failure. Convention: passes_hard_gate(None) == True.
    """
    if not float_shares or float_shares <= 0:
        return None
    if len(close_series) < 20:
        return None

    close = close_series.astype(float)
    volume = volume_series.astype(float)

    latest_close = float(close.iloc[-1])
    ff_mcap_cr = float_shares * latest_close / 1e7  # 1 Cr = 1e7 INR

    daily_val = close * volume
    avg20_val = float(daily_val.tail(20).mean())
    avg20_vol = float(volume.tail(20).mean())

    ff_mcap_inr = ff_mcap_cr * 1e7
    ff_turn_pct = (avg20_val / ff_mcap_inr * 100) if ff_mcap_inr > 0 else 0.0
    ft_20d = (avg20_vol * 20) / float_shares if float_shares > 0 else 0.0

    return {
        "ff_mcap_cr": round(ff_mcap_cr, 0),
        "ff_turn_pct": round(ff_turn_pct, 3),
        "ft_20d": round(ft_20d, 2),
        "avg20_val": round(avg20_val, 0),
    }


def trap_score(m: dict | None) -> tuple[int, str]:
    """
    Returns (pts, verdict).
    verdict: 'SAFE' | 'CAUTION' | 'AVOID' | 'NO DATA'
    pts ≥ 5 = AVOID, 3-4 = CAUTION, < 3 = SAFE.

    Scoring:
      FF MCAP < yellow → 2 pts  |  < green → 1 pt
      FF Turn < yellow → 2 pts  |  < green → 1 pt  (most important — double-weighted)
      Float×20d < 1×  → 1 pt
    Max = 5 pts from MCAP+TURN alone, so an illiquid thin-float stock hits AVOID immediately.
    """
    if m is None:
        return 0, "NO DATA"

    pts = 0
    pts += (
        2
        if m["ff_mcap_cr"] < FF_MCAP_YELLOW
        else (1 if m["ff_mcap_cr"] < FF_MCAP_GREEN else 0)
    )
    pts += (
        2
        if m["ff_turn_pct"] < FF_TURN_YELLOW
        else (1 if m["ff_turn_pct"] < FF_TURN_GREEN else 0)
    )
    pts += 1 if m["ft_20d"] < FT_20_YELLOW else 0

    if pts >= 5:
        return pts, "AVOID"
    if pts >= 3:
        return pts, "CAUTION"
    return pts, "SAFE"


def passes_hard_gate(m: dict | None) -> bool:
    """
    Hard filter: returns False only when verdict == 'AVOID'.
    Returns True when m is None (no float data — don't penalise missing data).

    Usage in scanner loop:
        fm = float_metrics(close_s, vol_s, float_shares)
        if not passes_hard_gate(fm):
            continue
    """
    if m is None:
        return True
    _, verdict = trap_score(m)
    return verdict != "AVOID"


def trap_label(m: dict | None) -> str:
    """
    Short string for a markdown table cell.
    Examples: '✓ SAFE'  '⚠ CAUTION'  '⛔ AVOID'  'n/a'
    """
    if m is None:
        return "n/a"
    _, verdict = trap_score(m)
    icon = {"SAFE": "✓", "CAUTION": "⚠", "AVOID": "⛔"}.get(verdict, "?")
    return f"{icon} {verdict}"
