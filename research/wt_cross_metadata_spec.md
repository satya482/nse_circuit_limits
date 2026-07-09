# WaveTrend Scanner — Current-Cross Metadata Embedding
## `spec.md` — Claude Code Implementation Guide

---

## 0. Scope & Constraints

**This spec covers Step 1 only:**
- Add `cross_type`, `wt1_velocity`, `divergence_flag`, `vol_confirm`
  to the existing `wavetrend_scanner.py` output DataFrame
- Zero architectural changes to `run()` interface
- Zero new data fetches — all inputs already available in the existing OHLCV pass
- Zero new dependencies
- Scanner must remain stateless

**Out of scope (covered in separate spec):**
- Historical cycle tracking (trough slope, OB peak slope, sequence score)
- `wt_cycle_tracker.py` nightly batch
- Combined score column
- Any database writes

**Non-negotiable guardrails:**
- `run(universe_df, as_of) -> pd.DataFrame` signature unchanged
- Existing columns unchanged — only additive
- No `datetime.now()` anywhere
- No lookahead bias — all metadata computed using only bars ≤ `as_of`
- Scanner must still complete on 962 stocks within existing runtime budget
- `cross_type = "NO_CROSS"` when no bullcross fired today — never None/NaN

---

## 1. Existing Scanner Context

Current `run()` output includes (minimum):

```python
# Existing columns — DO NOT MODIFY
ticker          str
date            date
cross_rank      int        # +5 BULL_OS_PPV → -3 BEAR_OB
wt1             float
wt2             float
signal          str        # existing signal label
qualifies       bool       # existing gate result
```

New columns to add (all optional-looking but always populated):

```python
# NEW — added by this spec
cross_type      str        # 7-value taxonomy label (see Section 3)
wt1_velocity    float      # rate of wt1 rise over 2 bars
wt2_at_cross    float      # wt2 value at the bar the cross fired
divergence_flag bool       # price lower-low + wt2 higher-low confirmed
vol_confirm     bool       # volume > VOL_RATIO_MIN × EMA20(volume) on cross bar
cross_quality   str        # "HIGH" / "MEDIUM" / "LOW" / "SKIP" (derived, see Section 6)
```

---

## 2. Exact WaveTrend Parameters (Do Not Change)

```python
# Channel parameters — existing, do not modify
WT_N1 = 10           # EMA channel length (ESA)
WT_N2 = 21           # wt1 signal smoothing
WT_SIGNAL = 4        # wt2 = SMA(wt1, 4)

# Zone thresholds — existing
OS_THRESHOLD    = -53    # wt2 < -53 → oversold zone
OB_THRESHOLD    = +53    # wt2 > +53 → overbought zone
OS_DEEP         = -65    # wt2 < -65 → deep oversold (Phoenix condition)

# New constants for this spec
DIV_LOOKBACK        = 10   # bars to search for prior trough for divergence
DIV_PRICE_TOLERANCE = 0.02 # price lower-low must be at least 0.2% lower (avoid flat)
VELOCITY_LOOKBACK   = 2    # bars for wt1 velocity: wt1[t] - wt1[t-2]
VOL_MA_PERIOD       = 20   # EMA period for volume baseline
VOL_RATIO_MIN       = 1.1  # volume must be > 1.1× EMA20 for vol_confirm
FLAT_BOTTOM_BARS    = 3    # minimum bars wt2 stayed in OS before cross (Slingshot)
FLAT_BOTTOM_RANGE   = 8.0  # max wt2 range (high-low) during flat period
SHALLOW_OS_MAX      = -35  # wt2 between -35 and -53 = shallow OS (Grind zone)
```

---

## 3. Cross Detection — Canonical Form

Cross detection must use directional crossover. Never `ta.cross()` equivalent:

```python
def detect_bullcross(wt1: pd.Series, wt2: pd.Series) -> pd.Series:
    """
    Returns boolean Series: True on bars where bullcross fires.
    Fired = wt1 was below wt2 previous bar AND wt1 >= wt2 current bar.
    """
    prev_below = wt1.shift(1) < wt2.shift(1)
    now_above  = wt1 >= wt2
    return prev_below & now_above

def detect_bearcross(wt1: pd.Series, wt2: pd.Series) -> pd.Series:
    """
    Returns boolean Series: True on bars where bearcross fires.
    """
    prev_above = wt1.shift(1) > wt2.shift(1)
    now_below  = wt1 <= wt2
    return prev_above & now_below
```

Both functions must be computed on the full lookback window, not just today.
The full history is needed for divergence detection and flat-bottom detection.

---

## 4. New Metric Definitions

### 4.1 wt2_at_cross

```python
# wt2 value at the exact bar the bullcross fired
# If no bullcross today: wt2_at_cross = wt2[as_of] (current wt2 regardless)
wt2_at_cross = df["wt2"].iloc[-1]
```

### 4.2 wt1_velocity

Rate of wt1 rise. Positive = accelerating upward. Negative = still falling.

```python
def compute_wt1_velocity(wt1: pd.Series, lookback: int = VELOCITY_LOOKBACK) -> float:
    """
    wt1_velocity = wt1[today] - wt1[today - lookback]
    Returns 0.0 if insufficient history.
    """
    if len(wt1) < lookback + 1:
        return 0.0
    return float(wt1.iloc[-1] - wt1.iloc[-(lookback + 1)])
```

### 4.3 divergence_flag

Bullish divergence: within DIV_LOOKBACK bars before today's cross,
find the most recent prior OS trough. Divergence = True if:
- `price_low[today's cross bar] < price_low[prior trough bar]` (price lower low)
- `wt2[today's cross bar] > wt2[prior trough bar]`     (wt2 higher low)

```python
def compute_divergence(
    close:    pd.Series,
    low:      pd.Series,
    wt2:      pd.Series,
    bullcross: pd.Series,
    idx:      int,              # index of today's cross bar in the series
    lookback: int = DIV_LOOKBACK,
    tolerance: float = DIV_PRICE_TOLERANCE,
) -> bool:
    """
    Returns True if bullish divergence confirmed at bar idx.
    
    Prior trough defined as: last bar before idx where bullcross previously
    fired OR the minimum wt2 bar within the lookback window — whichever
    gives a cleaner prior reference.
    
    Use minimum wt2 within lookback as prior trough if no prior cross exists.
    """
    if idx < lookback:
        return False
    
    window_wt2   = wt2.iloc[idx - lookback : idx]
    window_low   = low.iloc[idx - lookback : idx]
    
    prior_trough_idx = window_wt2.idxmin()   # bar with lowest wt2 in window
    
    price_lower_low = low.iloc[idx] < window_low.loc[prior_trough_idx] * (1 - tolerance)
    wt2_higher_low  = wt2.iloc[idx] > window_wt2.loc[prior_trough_idx]
    
    return bool(price_lower_low and wt2_higher_low)
```

### 4.4 vol_confirm

```python
def compute_vol_confirm(
    volume:   pd.Series,
    idx:      int,
    ma_period: int = VOL_MA_PERIOD,
    ratio_min: float = VOL_RATIO_MIN,
) -> bool:
    """
    True if volume[idx] > ratio_min × EMA(volume, ma_period)[idx]
    EMA computed on full series up to idx — no lookahead.
    """
    if idx < ma_period:
        return False
    vol_ema = volume.ewm(span=ma_period, adjust=False).mean()
    return bool(volume.iloc[idx] > ratio_min * vol_ema.iloc[idx])
```

---

## 5. Cross Type Detection — Full Decision Tree

Compute in this exact order. First condition that matches wins.

```python
def classify_cross_type(
    wt1:        pd.Series,
    wt2:        pd.Series,
    close:      pd.Series,
    low:        pd.Series,
    volume:     pd.Series,
    bullcross:  pd.Series,    # full history boolean series
    bearcross:  pd.Series,    # full history boolean series
    idx:        int,          # index of today's cross bar
    rs_rising:  bool,         # RS vs NiftyMidSml400 is rising (pre-computed)
    above_ema50: bool,        # price > EMA50 (pre-computed)
) -> str:
    """
    Returns one of:
    PHOENIX | SLINGSHOT | HIDDEN_STRENGTH | ECHO | 
    GRIND | OB_RECROSS | TRAP_DOOR | NO_CROSS
    """
    
    # Guard — no cross today
    if not bullcross.iloc[idx]:
        return "NO_CROSS"
    
    wt2_now = wt2.iloc[idx]
    
    # --- Rule 1: TRAP_DOOR — check context first, before zone ---
    # Structural context is broken: RS falling AND price below EMA50
    # Catches dangerous false signals regardless of oscillator depth
    if not rs_rising and not above_ema50:
        return "TRAP_DOOR"
    
    # --- Rule 2: OB_RECROSS — cross from overbought territory ---
    if wt2_now > OB_THRESHOLD * 0.5:   # wt2 > +26 at cross = OB side of zero
        return "OB_RECROSS"
    
    # --- Rule 3: GRIND — cross in shallow / near-zero zone ---
    if wt2_now > SHALLOW_OS_MAX:        # wt2 between -35 and 0
        return "GRIND"
    
    # --- Below here: wt2 < -35 (genuinely in OS territory) ---
    
    # --- Rule 4: ECHO — second cross after recent failed cross ---
    # Find most recent prior bullcross within DIV_LOOKBACK * 2 bars
    lookback_window = bullcross.iloc[max(0, idx - DIV_LOOKBACK * 2) : idx]
    prior_crosses   = lookback_window[lookback_window == True]
    
    if len(prior_crosses) >= 1:
        # A prior cross existed and price came back to OS = Echo candidate
        prior_idx   = prior_crosses.index[-1]
        prior_wt2   = wt2.loc[prior_idx]
        
        # Valid Echo: prior cross also from OS zone
        if prior_wt2 < OS_THRESHOLD:
            return "ECHO"
    
    # --- Rule 5: PHOENIX — deep OS + V-bottom (fast reversal) ---
    # Deep: wt2 < -65
    # V-bottom: wt2 was not flat (range > FLAT_BOTTOM_RANGE) in prior FLAT_BOTTOM_BARS
    if wt2_now < OS_DEEP:
        pre_cross_wt2 = wt2.iloc[max(0, idx - FLAT_BOTTOM_BARS) : idx]
        wt2_range     = float(pre_cross_wt2.max() - pre_cross_wt2.min())
        
        if wt2_range > FLAT_BOTTOM_RANGE:    # not flat = V-shape
            return "PHOENIX"
    
    # --- Rule 6: SLINGSHOT — OS zone + flat bottom (extended base) ---
    # wt2 sat in OS for FLAT_BOTTOM_BARS+ bars AND ranged narrowly
    if wt2_now <= OS_THRESHOLD:
        pre_cross_wt2 = wt2.iloc[max(0, idx - FLAT_BOTTOM_BARS) : idx]
        all_in_os     = (pre_cross_wt2 < OS_THRESHOLD).all()
        wt2_range     = float(pre_cross_wt2.max() - pre_cross_wt2.min())
        
        if all_in_os and wt2_range <= FLAT_BOTTOM_RANGE:
            return "SLINGSHOT"
    
    # --- Rule 7: HIDDEN_STRENGTH — OS cross in uptrending stock ---
    # RS rising AND price above EMA50 (already checked above for TRAP_DOOR)
    # Reaches here = rs_rising OR above_ema50 is True
    if rs_rising and above_ema50:
        return "HIDDEN_STRENGTH"
    
    # --- Default: SLINGSHOT if OS but no specific pattern ---
    if wt2_now <= OS_THRESHOLD:
        return "SLINGSHOT"
    
    # Fallback (should not reach here given rules above)
    return "GRIND"
```

---

## 6. cross_quality Derivation

Derived column — combines `cross_type`, `divergence_flag`, `vol_confirm`:

```python
QUALITY_MAP = {
    # (cross_type, divergence_flag, vol_confirm) -> cross_quality
    
    # HIGH — all three align
    ("PHOENIX",         True,  True):  "HIGH",
    ("ECHO",            True,  True):  "HIGH",
    ("SLINGSHOT",       True,  True):  "HIGH",
    
    # HIGH — type alone sufficient for these
    ("PHOENIX",         True,  False): "HIGH",
    ("ECHO",            True,  False): "HIGH",
    ("PHOENIX",         False, True):  "HIGH",
    
    # MEDIUM — type is good, one confirm missing
    ("SLINGSHOT",       True,  False): "MEDIUM",
    ("SLINGSHOT",       False, True):  "MEDIUM",
    ("HIDDEN_STRENGTH", True,  True):  "MEDIUM",
    ("HIDDEN_STRENGTH", True,  False): "MEDIUM",
    ("HIDDEN_STRENGTH", False, True):  "MEDIUM",
    ("ECHO",            False, False): "MEDIUM",
    
    # LOW — cross present but minimal confirmation
    ("SLINGSHOT",       False, False): "LOW",
    ("HIDDEN_STRENGTH", False, False): "LOW",
    ("GRIND",           True,  True):  "LOW",
    
    # SKIP — these types are never actionable
    ("GRIND",           False, False): "SKIP",
    ("GRIND",           True,  False): "SKIP",
    ("GRIND",           False, True):  "SKIP",
    ("OB_RECROSS",      True,  True):  "SKIP",
    ("OB_RECROSS",      False, False): "SKIP",
    ("TRAP_DOOR",       True,  True):  "SKIP",
    ("TRAP_DOOR",       False, False): "SKIP",
    ("NO_CROSS",        False, False): "SKIP",
}

def compute_cross_quality(
    cross_type: str,
    divergence_flag: bool,
    vol_confirm: bool,
) -> str:
    key = (cross_type, divergence_flag, vol_confirm)
    return QUALITY_MAP.get(key, "LOW")   # unlisted combos default to LOW
```

---

## 7. Integration Into run()

Add the following block inside `run()`, after existing WT signal computation,
before the return statement:

```python
def _compute_cross_metadata(
    ticker_df:  pd.DataFrame,    # single-ticker OHLCV + wt1/wt2 columns
    rs_rising:  bool,
    above_ema50: bool,
) -> dict:
    """
    Compute all new metadata fields for one ticker.
    Returns dict with keys matching new output columns.
    Always returns a complete dict — no KeyErrors downstream.
    """
    wt1       = ticker_df["wt1"]
    wt2       = ticker_df["wt2"]
    close     = ticker_df["close"]
    low       = ticker_df["low"]
    volume    = ticker_df["volume"]
    
    bullcross = detect_bullcross(wt1, wt2)
    bearcross = detect_bearcross(wt1, wt2)
    
    idx = len(ticker_df) - 1   # today = last bar
    
    cross_type_val    = classify_cross_type(
                            wt1, wt2, close, low, volume,
                            bullcross, bearcross, idx,
                            rs_rising, above_ema50
                        )
    wt2_at_cross_val  = float(wt2.iloc[idx])
    wt1_velocity_val  = compute_wt1_velocity(wt1)
    divergence_val    = compute_divergence(close, low, wt2, bullcross, idx) \
                        if bullcross.iloc[idx] else False
    vol_confirm_val   = compute_vol_confirm(volume, idx) \
                        if bullcross.iloc[idx] else False
    quality_val       = compute_cross_quality(
                            cross_type_val, divergence_val, vol_confirm_val
                        )
    
    return {
        "cross_type":      cross_type_val,
        "wt2_at_cross":    wt2_at_cross_val,
        "wt1_velocity":    wt1_velocity_val,
        "divergence_flag": divergence_val,
        "vol_confirm":     vol_confirm_val,
        "cross_quality":   quality_val,
    }
```

Call this per-ticker inside the existing loop. Append results to the output row.

---

## 8. Output DataFrame — Final Schema

```python
# Complete output column list after this spec
{
    # Existing (unchanged)
    "ticker":           str,
    "date":             date,
    "cross_rank":       int,       # +5 to -3
    "wt1":              float,
    "wt2":              float,
    "signal":           str,
    "qualifies":        bool,
    
    # New (this spec)
    "cross_type":       str,       # PHOENIX/SLINGSHOT/HIDDEN_STRENGTH/ECHO/
                                   # GRIND/OB_RECROSS/TRAP_DOOR/NO_CROSS
    "wt2_at_cross":     float,     # wt2 value at today's bar (always populated)
    "wt1_velocity":     float,     # wt1[t] - wt1[t-2], positive = rising fast
    "divergence_flag":  bool,      # True = bullish divergence confirmed
    "vol_confirm":      bool,      # True = volume > 1.1× EMA20 on cross bar
    "cross_quality":    str,       # HIGH / MEDIUM / LOW / SKIP
}
```

**Nullability rules:**
- `cross_type` — never null. "NO_CROSS" when no cross today.
- `wt2_at_cross` — never null. Current wt2 value regardless of cross.
- `wt1_velocity` — never null. 0.0 if insufficient history.
- `divergence_flag` — False when no cross today. Never null.
- `vol_confirm` — False when no cross today. Never null.
- `cross_quality` — never null. "SKIP" when no cross or skip type.

---

## 9. Pre-Market Output Sort Order

After this spec, sort output DataFrame by:

```python
# Priority sort: actionable crosses first
QUALITY_ORDER = {"HIGH": 0, "MEDIUM": 1, "LOW": 2, "SKIP": 3}

results_df["_quality_rank"] = results_df["cross_quality"].map(QUALITY_ORDER)

results_df = results_df.sort_values(
    by=["_quality_rank", "cross_rank", "wt1_velocity"],
    ascending=[True, False, False]
).drop(columns=["_quality_rank"])
```

This replaces sorting by `cross_rank` alone. Within the same quality tier,
higher `cross_rank` wins, then higher `wt1_velocity` (faster recoveries first).

---

## 10. Rajan Mehta Output Label

Add a human-readable triage label for the 06:00 scan output:

```python
def format_rajan_label(row: pd.Series) -> str:
    """
    Single-line triage label for pre-market printout.
    Format: [QUALITY] TYPE | rank:+N | vel:+X.X | DIV | VOL
    Example: [HIGH] PHOENIX | rank:+5 | vel:+3.2 | DIV ✓ | VOL ✓
    """
    quality  = row["cross_quality"]
    ctype    = row["cross_type"]
    rank     = row["cross_rank"]
    vel      = row["wt1_velocity"]
    div_str  = "DIV ✓" if row["divergence_flag"] else "DIV ✗"
    vol_str  = "VOL ✓" if row["vol_confirm"]     else "VOL ✗"
    
    rank_str = f"+{rank}" if rank >= 0 else str(rank)
    vel_str  = f"+{vel:.1f}" if vel >= 0 else f"{vel:.1f}"
    
    return f"[{quality}] {ctype} | rank:{rank_str} | vel:{vel_str} | {div_str} | {vol_str}"
```

Console output example at 06:00:
```
APARINDS  [HIGH]   PHOENIX        | rank:+5 | vel:+3.2 | DIV ✓ | VOL ✓
WELCORP   [HIGH]   ECHO           | rank:+5 | vel:+2.8 | DIV ✓ | VOL ✗
RPTECH    [MEDIUM] SLINGSHOT      | rank:+3 | vel:+1.1 | DIV ✓ | VOL ✗
STLTECH   [LOW]    HIDDEN_STRENGTH| rank:+2 | vel:+0.4 | DIV ✗ | VOL ✗
ATLANTAELE[SKIP]   TRAP_DOOR      | rank:+5 | vel:+2.1 | DIV ✓ | VOL ✓
```

Note: ATLANTAELE shows rank+5 but SKIP quality — this is exactly the case
the taxonomy is designed to catch. Cross rank alone would have promoted it.

---

## 11. CLAUDE.md Additions for This Module

```markdown
## WaveTrend Cross Metadata — Constraints

RULES:
- classify_cross_type() must follow the exact 7-rule decision order in spec.
  Do not reorder rules — TRAP_DOOR check before zone checks is intentional.
- cross_type = "NO_CROSS" when bullcross.iloc[-1] is False. Never None/NaN.
- divergence_flag = False (not NaN) when no cross today.
- vol_confirm = False (not NaN) when no cross today.
- wt1_velocity lookback = 2 bars. Do not increase without updating spec.
- OS_DEEP threshold = -65. Do not conflate with OS_THRESHOLD = -53.
- QUALITY_MAP is exhaustive for actionable types. Unlisted combos → "LOW".
- sort order: quality_rank ASC, cross_rank DESC, wt1_velocity DESC.
  This is the pre-market triage order — do not change without explicit instruction.

NEVER:
- Use datetime.now() — all dates from as_of parameter
- Use NaN for cross_type, divergence_flag, vol_confirm, cross_quality
- Change run() signature
- Add new data fetches inside run()
- Compute cycle history here (that is a separate spec / separate module)
```

---

## 12. Acceptance Criteria Checklist

```
[ ] run() completes on 962-stock universe without errors
[ ] All six new columns present in output DataFrame
[ ] cross_type has zero NaN values across all 962 rows
[ ] cross_type = "NO_CROSS" for all rows where no bullcross fired today
[ ] divergence_flag = False (not NaN) for all NO_CROSS rows
[ ] vol_confirm = False (not NaN) for all NO_CROSS rows
[ ] cross_quality = "SKIP" for all TRAP_DOOR rows regardless of other flags
[ ] cross_quality = "SKIP" for all OB_RECROSS rows regardless of other flags
[ ] cross_quality = "SKIP" for all NO_CROSS rows
[ ] PHOENIX only assigned when wt2_at_cross < -65 AND wt2_range > 8.0
[ ] SLINGSHOT only assigned when wt2 was in OS zone for ≥ 3 prior bars
[ ] ECHO only assigned when a prior bullcross existed within 20 bars
[ ] Sort order: all HIGH rows above MEDIUM, MEDIUM above LOW, LOW above SKIP
[ ] Rajan label prints without error for every row
[ ] Unit test: ticker with wt2=-70, V-bottom, rs_rising=True  → PHOENIX
[ ] Unit test: ticker with wt2=-55, flat 4 bars, rs_rising=True → SLINGSHOT  
[ ] Unit test: ticker with wt2=-58, rs_rising=False, above_ema50=False → TRAP_DOOR
[ ] Unit test: ticker with wt2=-20  → GRIND
[ ] Unit test: ticker with wt2=+30  → OB_RECROSS
[ ] Unit test: prior cross 12 bars ago + wt2=-60 now → ECHO
[ ] Unit test: PHOENIX + divergence=True + vol_confirm=True → cross_quality=HIGH
[ ] Unit test: TRAP_DOOR + divergence=True + vol_confirm=True → cross_quality=SKIP
[ ] No datetime.now() calls in module
[ ] Runtime on 962 stocks within 110% of pre-spec baseline runtime
```

---

## 13. Unit Test Stubs

Provide these as `tests/test_wt_cross_metadata.py`:

```python
import pytest
import pandas as pd
import numpy as np

# --- Fixtures: synthetic ticker DataFrames ---

def make_ticker_df(wt1_series, wt2_series, close_series, low_series, vol_series):
    return pd.DataFrame({
        "wt1":    wt1_series,
        "wt2":    wt2_series,
        "close":  close_series,
        "low":    low_series,
        "volume": vol_series,
    })

# --- Cross type tests ---

def test_phoenix_deep_os_v_bottom():
    # wt2 drops to -72 sharply, then crosses up today
    # Expected: PHOENIX
    pass  # Claude Code to implement

def test_slingshot_flat_bottom():
    # wt2 sits at -57, -58, -56, -55 for 4 bars, then crosses up
    # Expected: SLINGSHOT
    pass

def test_trap_door_overrides_deep_os():
    # wt2 = -70 (would be PHOENIX) but rs_rising=False, above_ema50=False
    # Expected: TRAP_DOOR
    pass

def test_echo_prior_cross_detected():
    # Bullcross fired 10 bars ago, wt2 returned to OS, cross fires again today
    # Expected: ECHO
    pass

def test_grind_shallow_os():
    # wt2 = -20 at cross
    # Expected: GRIND
    pass

def test_ob_recross_from_positive_zone():
    # wt2 = +30 at cross
    # Expected: OB_RECROSS
    pass

def test_no_cross_returns_no_cross():
    # wt1 below wt2, no cross today
    # Expected: NO_CROSS
    pass

# --- Quality tests ---

def test_trap_door_always_skip():
    assert compute_cross_quality("TRAP_DOOR", True, True)  == "SKIP"
    assert compute_cross_quality("TRAP_DOOR", False, False) == "SKIP"

def test_ob_recross_always_skip():
    assert compute_cross_quality("OB_RECROSS", True, True)  == "SKIP"
    assert compute_cross_quality("OB_RECROSS", False, False) == "SKIP"

def test_phoenix_div_vol_is_high():
    assert compute_cross_quality("PHOENIX", True, True) == "HIGH"

def test_phoenix_div_no_vol_is_high():
    assert compute_cross_quality("PHOENIX", True, False) == "HIGH"

# --- Nullability tests ---

def test_no_cross_divergence_is_false_not_nan():
    # On a NO_CROSS day, divergence_flag must be False, not NaN
    pass

def test_all_columns_present_in_output():
    # run() on minimal universe returns all 6 new columns
    pass
```

---

*Generated: 2026-07-09 | Version: 1.0 | Step 1 of 4 — Current-Cross Metadata Only*
*Next: wt_cycle_tracker_spec.md (Step 2) — Historical cycle tracking, nightly batch*
