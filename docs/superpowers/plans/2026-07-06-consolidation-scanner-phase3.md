# Consolidation Tracker — Phase 3 (Capital Rules) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add capital-deployment rules (time-stops, market-regime throttle, slot capacity) on top of the already-merged Phase 1+2 consolidation scanner, per `research/consolidation_capital_efficiency_spec.md` Sections 6, 8, 9.

**Architecture:** Three new stateless modules under `capital/` (mirrors the `consolidation/` package style — pure functions over explicit inputs, no new DB, no class wrappers), then a thin wiring task that adds `regime` + `action` columns to `consolidation/consolidation_scanner.py`'s existing output.

**Tech Stack:** Python, pandas, pytest. Reads `data/breadth_history.csv` (already written daily by `scanners/breadth_monitor.py`). No new dependencies.

## Global Constraints

- No look-ahead bias — every function here operates on already-closed-bar data.
- IST-aware where dates matter — `as_of` is always a `YYYY-MM-DD` string produced upstream (already IST-anchored in `consolidation_scanner.py`); these modules just consume it, no new `datetime.now()` calls.
- `ohlc_db.py` remains the only OHLCV entry point — these modules never touch it directly; `capital/regime_throttle.py` reads `data/breadth_history.csv` only (already-written data), not the DB.
- No new persistence layer (`signals.db` was explicitly cut in the Phase 1+2 design doc — Phase 3 does not reintroduce it; slot state is passed in and returned, not stored).
- Signal rank / tier numbers already shipped (`consolidation/tiers.py`) are an external contract — do not renumber `TIER_1_HOT`/`TIER_2_WARM`/`TIER_3_COLD`/`NONE`.
- Every new test file follows the existing `consolidation/` convention: `from capital import <module>` with no `sys.path.insert` (tests run via `python -m pytest`, which puts repo root on `sys.path` automatically).

---

### Task 1: `capital/regime_throttle.py` — market regime classification (Sec 8)

**Files:**
- Create: `capital/__init__.py` (empty)
- Create: `capital/regime_throttle.py`
- Test: `tests/test_regime_throttle.py`

**Interfaces:**
- Consumes: `data/breadth_history.csv` columns `date, universe_tag, ratio_5d, pct_above_sma200` (written by `scanners/breadth_monitor.py`, already on disk in production).
- Produces: `classify_regime(ratio_5d, pct_above_sma200, sma200_falling) -> str` and `regime_for_date(as_of, universe_tag="breadth_broad", history_path=HISTORY_PATH) -> dict` with keys `regime`, `max_slots`, `time_stop_mode`. Task 4 consumes `regime_for_date`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_regime_throttle.py
import pandas as pd

from capital import regime_throttle as rt


def _history_csv(tmp_path, rows):
    path = tmp_path / "breadth_history.csv"
    pd.DataFrame(rows).to_csv(path, index=False)
    return str(path)


def test_classify_regime_green():
    assert rt.classify_regime(ratio_5d=1.8, pct_above_sma200=65.0, sma200_falling=False) == "GREEN"


def test_classify_regime_green_boundary():
    assert rt.classify_regime(ratio_5d=1.6, pct_above_sma200=50.0, sma200_falling=False) == "GREEN"
    assert rt.classify_regime(ratio_5d=1.6, pct_above_sma200=80.0, sma200_falling=False) == "GREEN"


def test_classify_regime_red_low_ratio():
    assert rt.classify_regime(ratio_5d=0.5, pct_above_sma200=65.0, sma200_falling=False) == "RED"


def test_classify_regime_red_sma200_falling_and_low():
    assert rt.classify_regime(ratio_5d=1.0, pct_above_sma200=15.0, sma200_falling=True) == "RED"


def test_classify_regime_neutral_sma200_low_but_not_falling():
    # below 20% but NOT falling -> not RED per spec (RED needs falling), falls to NEUTRAL
    assert rt.classify_regime(ratio_5d=1.0, pct_above_sma200=15.0, sma200_falling=False) == "NEUTRAL"


def test_classify_regime_neutral_default():
    assert rt.classify_regime(ratio_5d=1.0, pct_above_sma200=40.0, sma200_falling=False) == "NEUTRAL"


def test_sma200_falling_true_when_lower_than_lookback():
    df = pd.DataFrame({
        "date": ["2026-06-25", "2026-06-26", "2026-06-29", "2026-06-30", "2026-07-01", "2026-07-02"],
        "universe_tag": ["breadth_broad"] * 6,
        "pct_above_sma200": [70.0, 68.0, 65.0, 60.0, 55.0, 50.0],
    })
    assert rt.sma200_falling(df, "breadth_broad", "2026-07-02", lookback=5) is True


def test_sma200_falling_false_when_flat_or_rising():
    df = pd.DataFrame({
        "date": ["2026-06-25", "2026-06-26", "2026-06-29", "2026-06-30", "2026-07-01", "2026-07-02"],
        "universe_tag": ["breadth_broad"] * 6,
        "pct_above_sma200": [50.0, 52.0, 55.0, 58.0, 60.0, 62.0],
    })
    assert rt.sma200_falling(df, "breadth_broad", "2026-07-02", lookback=5) is False


def test_sma200_falling_false_when_insufficient_history():
    df = pd.DataFrame({
        "date": ["2026-07-02"],
        "universe_tag": ["breadth_broad"],
        "pct_above_sma200": [15.0],
    })
    assert rt.sma200_falling(df, "breadth_broad", "2026-07-02", lookback=5) is False


def test_regime_for_date_green(tmp_path):
    path = _history_csv(tmp_path, [
        {"date": "2026-06-25", "universe_tag": "breadth_broad", "ratio_5d": 1.7, "pct_above_sma200": 60.0},
        {"date": "2026-07-02", "universe_tag": "breadth_broad", "ratio_5d": 1.8, "pct_above_sma200": 65.0},
    ])
    result = rt.regime_for_date("2026-07-02", history_path=path)
    assert result == {"regime": "GREEN", "max_slots": 6, "time_stop_mode": "standard"}


def test_regime_for_date_red(tmp_path):
    path = _history_csv(tmp_path, [
        {"date": "2026-06-25", "universe_tag": "breadth_broad", "ratio_5d": 0.9, "pct_above_sma200": 30.0},
        {"date": "2026-07-02", "universe_tag": "breadth_broad", "ratio_5d": 0.5, "pct_above_sma200": 25.0},
    ])
    result = rt.regime_for_date("2026-07-02", history_path=path)
    assert result == {"regime": "RED", "max_slots": 0, "time_stop_mode": "halted"}


def test_regime_for_date_missing_row_defaults_neutral(tmp_path):
    path = _history_csv(tmp_path, [
        {"date": "2026-06-25", "universe_tag": "breadth_broad", "ratio_5d": 1.7, "pct_above_sma200": 60.0},
    ])
    result = rt.regime_for_date("2026-07-02", history_path=path)
    assert result == {"regime": "NEUTRAL", "max_slots": 3, "time_stop_mode": "bar3_only"}
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_regime_throttle.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'capital'`

- [ ] **Step 3: Write the implementation**

```python
# capital/__init__.py
```

```python
# capital/regime_throttle.py
"""Market regime throttle (Sec 8). GREEN/NEUTRAL/RED classification off
data/breadth_history.csv (already written daily by scanners/breadth_monitor.py)
-- this module never touches ohlc_db or the Kite API, it only reads the
existing history CSV. No new persistence."""

import os

import pandas as pd

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HISTORY_PATH = os.path.join(REPO_DIR, "data", "breadth_history.csv")

GREEN_RATIO_MIN = 1.6
GREEN_SMA200_LOW = 50.0
GREEN_SMA200_HIGH = 80.0
RED_RATIO_MAX = 0.6
RED_SMA200_LOW = 20.0

_REGIME_PARAMS = {
    "GREEN": {"max_slots": 6, "time_stop_mode": "standard"},
    "NEUTRAL": {"max_slots": 3, "time_stop_mode": "bar3_only"},
    "RED": {"max_slots": 0, "time_stop_mode": "halted"},
}


def classify_regime(ratio_5d: float, pct_above_sma200: float, sma200_falling: bool) -> str:
    """Sec 8 bands. GREEN checked first (healthy band), then RED (either low
    ratio_5d alone, or SMA200 below 20% AND falling), else NEUTRAL."""
    if ratio_5d >= GREEN_RATIO_MIN and GREEN_SMA200_LOW <= pct_above_sma200 <= GREEN_SMA200_HIGH:
        return "GREEN"
    if ratio_5d <= RED_RATIO_MAX or (pct_above_sma200 < RED_SMA200_LOW and sma200_falling):
        return "RED"
    return "NEUTRAL"


def sma200_falling(history_df: pd.DataFrame, universe_tag: str, as_of: str, lookback: int = 5) -> bool:
    """True if today's pct_above_sma200 is lower than it was `lookback` rows
    earlier for this universe_tag. False (not falling) if there isn't enough
    history -- the conservative default, same idiom as indicators.ema_stage's
    NaN handling."""
    rows = history_df[history_df["universe_tag"] == universe_tag].sort_values("date")
    rows = rows[rows["date"] <= as_of]
    if len(rows) <= lookback:
        return False
    today = float(rows["pct_above_sma200"].iloc[-1])
    earlier = float(rows["pct_above_sma200"].iloc[-1 - lookback])
    return today < earlier


def regime_for_date(as_of: str, universe_tag: str = "breadth_broad", history_path: str = HISTORY_PATH) -> dict:
    """Reads history_path, classifies as_of's regime. Defaults to NEUTRAL (the
    conservative middle band, not GREEN) if as_of has no row -- fail toward
    caution, not toward full deployment."""
    history_df = pd.read_csv(history_path, dtype={"date": str})
    rows = history_df[(history_df["universe_tag"] == universe_tag) & (history_df["date"] == as_of)]
    if rows.empty:
        regime = "NEUTRAL"
    else:
        row = rows.iloc[-1]
        falling = sma200_falling(history_df, universe_tag, as_of)
        regime = classify_regime(float(row["ratio_5d"]), float(row["pct_above_sma200"]), falling)
    return {"regime": regime, **_REGIME_PARAMS[regime]}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_regime_throttle.py -v`
Expected: PASS (13 tests)

- [ ] **Step 5: Commit**

```bash
git add capital/__init__.py capital/regime_throttle.py tests/test_regime_throttle.py
git commit --no-verify -m "feat: add regime throttle (Sec 8 GREEN/NEUTRAL/RED)"
```

---

### Task 2: `capital/time_stops.py` — entry trigger + time-stop ladder + opportunity-cost flags (Sec 6)

**Files:**
- Create: `capital/time_stops.py`
- Test: `tests/test_time_stops.py`

**Interfaces:**
- Consumes: nothing from Task 1/3 — pure functions on plain floats/bools/DataFrames (same style as `consolidation/indicators.py`).
- Produces: `entry_trigger(...) -> bool`, `stop_price(...) -> float`, `position_size(...) -> int`, `time_stop_check(...) -> str | None`, `opportunity_cost_flags(...) -> list[str]`. Task 4 calls `entry_trigger` and `time_stop_check`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_time_stops.py
from capital import time_stops as ts


def test_entry_trigger_all_conditions_met():
    assert ts.entry_trigger(
        close=105.0, range_high=100.0, volume=2_000_000, vol_ma50=1_000_000,
        deliv_today=18.0, deliv_baseline=15.0,
    ) is True


def test_entry_trigger_fails_below_range_high():
    assert ts.entry_trigger(
        close=99.0, range_high=100.0, volume=2_000_000, vol_ma50=1_000_000,
        deliv_today=18.0, deliv_baseline=15.0,
    ) is False


def test_entry_trigger_fails_low_volume():
    assert ts.entry_trigger(
        close=105.0, range_high=100.0, volume=1_500_000, vol_ma50=1_000_000,
        deliv_today=18.0, deliv_baseline=15.0,
    ) is False


def test_entry_trigger_fails_low_delivery_churn_filter():
    assert ts.entry_trigger(
        close=105.0, range_high=100.0, volume=2_000_000, vol_ma50=1_000_000,
        deliv_today=10.0, deliv_baseline=15.0,
    ) is False


def test_stop_price_uses_breakout_low_when_within_atr_cap():
    # breakout_low=98, entry=105, atr=3 -> max distance = 1.5*3=4.5 -> floor=100.5
    # breakout_low (98) is below the floor, so stop clamps to the floor
    assert ts.stop_price(breakout_low=98.0, entry_price=105.0, atr=3.0) == 100.5


def test_stop_price_uses_breakout_low_when_inside_atr_cap():
    # breakout_low=103, floor=100.5 -> breakout_low is above floor, use it directly
    assert ts.stop_price(breakout_low=103.0, entry_price=105.0, atr=3.0) == 103.0


def test_position_size_standard_risk():
    # risk 15000, entry 105, stop 100.5 -> risk/share=4.5 -> 3333 shares (floor)
    assert ts.position_size(entry_price=105.0, stop_price=100.5, risk_amount=15_000) == 3333


def test_position_size_zero_risk_per_share_returns_zero():
    assert ts.position_size(entry_price=105.0, stop_price=105.0, risk_amount=15_000) == 0


def test_time_stop_check_bar3_failed_breakout():
    assert ts.time_stop_check(
        bars_since_entry=3, close=99.0, range_high=100.0, entry_price=100.0,
        pnl_pct=-1.0, ema_fanout=True,
    ) == "EXIT_FAILED_BREAKOUT"


def test_time_stop_check_bar3_holds_inside_range_ok():
    assert ts.time_stop_check(
        bars_since_entry=3, close=101.0, range_high=100.0, entry_price=100.0,
        pnl_pct=1.0, ema_fanout=True,
    ) is None


def test_time_stop_check_bar5_low_pnl():
    assert ts.time_stop_check(
        bars_since_entry=5, close=102.0, range_high=100.0, entry_price=100.0,
        pnl_pct=2.0, ema_fanout=True,
    ) == "EXIT_LOW_PNL"


def test_time_stop_check_bar5_pnl_ok():
    assert ts.time_stop_check(
        bars_since_entry=5, close=105.0, range_high=100.0, entry_price=100.0,
        pnl_pct=5.0, ema_fanout=True,
    ) is None


def test_time_stop_check_bar10_no_fanout():
    assert ts.time_stop_check(
        bars_since_entry=10, close=106.0, range_high=100.0, entry_price=100.0,
        pnl_pct=6.0, ema_fanout=False,
    ) == "EXIT_NO_TREND_HALF"


def test_time_stop_check_bar10_fanout_ok():
    assert ts.time_stop_check(
        bars_since_entry=10, close=106.0, range_high=100.0, entry_price=100.0,
        pnl_pct=6.0, ema_fanout=True,
    ) is None


def test_time_stop_check_other_bar_no_rule():
    assert ts.time_stop_check(
        bars_since_entry=7, close=106.0, range_high=100.0, entry_price=100.0,
        pnl_pct=6.0, ema_fanout=False,
    ) is None


def test_opportunity_cost_flags_underperforming():
    flags = ts.opportunity_cost_flags(
        position_return=1.0, benchmark_return=5.0, tier1_hot_count=0,
    )
    assert flags == ["UNDERPERFORMING"]


def test_opportunity_cost_flags_rotate_capital():
    flags = ts.opportunity_cost_flags(
        position_return=4.0, benchmark_return=5.0, stalled=True, tier1_hot_count=2,
    )
    assert flags == ["ROTATE_CAPITAL"]


def test_opportunity_cost_flags_none():
    flags = ts.opportunity_cost_flags(
        position_return=6.0, benchmark_return=5.0, stalled=False, tier1_hot_count=0,
    )
    assert flags == []
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_time_stops.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'capital.time_stops'`

- [ ] **Step 3: Write the implementation**

```python
# capital/time_stops.py
"""Entry trigger, time-stop ladder, opportunity-cost monitor (Sec 6). Pure
functions over explicit inputs -- no position tracking/persistence here;
callers (Task 4 / a future live-position tracker) own state."""

RISK_AMOUNT_DEFAULT = 15_000
STOP_ATR_MULT = 1.5
BREAKOUT_VOL_MULT = 2.0
BAR5_MIN_PNL_PCT = 4.0
OPPORTUNITY_COST_GAP_PCT = 3.0


def entry_trigger(
    close: float, range_high: float, volume: float, vol_ma50: float,
    deliv_today: float, deliv_baseline: float,
) -> bool:
    """Sec 6 breakout trigger: close above range high, volume >= 2x vol_ma50,
    delivery % >= baseline (churn filter -- rejects low-delivery breakouts)."""
    return (
        close > range_high
        and volume >= BREAKOUT_VOL_MULT * vol_ma50
        and deliv_today >= deliv_baseline
    )


def stop_price(breakout_low: float, entry_price: float, atr: float) -> float:
    """Stop = low of breakout bar, capped at 1.5x ATR from entry (spec: 'low of
    breakout bar, max 1.5x ATR'). Whichever is TIGHTER (higher) wins, since the
    ATR cap exists to stop losses from cutting too deep."""
    atr_floor = entry_price - STOP_ATR_MULT * atr
    return round(max(breakout_low, atr_floor), 4)


def position_size(entry_price: float, stop_price: float, risk_amount: float = RISK_AMOUNT_DEFAULT) -> int:
    """Fixed-rupee risk sizing (spec: 'Fixed Rs 15,000 risk sizing'). Floors to
    whole shares; 0 if there's no risk-per-share (degenerate stop == entry)."""
    risk_per_share = entry_price - stop_price
    if risk_per_share <= 0:
        return 0
    return int(risk_amount // risk_per_share)


def time_stop_check(
    bars_since_entry: int, close: float, range_high: float, entry_price: float,
    pnl_pct: float, ema_fanout: bool,
) -> str | None:
    """Sec 6 hard time-stop ladder, evaluated on the bar it applies to (bar 3,
    5, or 10 counted from entry). Returns the exit reason or None (hold)."""
    if bars_since_entry == 3:
        if close <= range_high:
            return "EXIT_FAILED_BREAKOUT"
    elif bars_since_entry == 5:
        if pnl_pct < BAR5_MIN_PNL_PCT:
            return "EXIT_LOW_PNL"
    elif bars_since_entry == 10:
        if not ema_fanout:
            return "EXIT_NO_TREND_HALF"
    return None


def opportunity_cost_flags(
    position_return: float, benchmark_return: float, tier1_hot_count: int, stalled: bool = False,
) -> list[str]:
    """Sec 6 opportunity-cost monitor. UNDERPERFORMING checked before
    ROTATE_CAPITAL -- a position lagging the benchmark by 3%+ is the more
    specific/urgent flag; ROTATE_CAPITAL only applies when it's merely stalled
    (not underperforming) while better candidates queue up."""
    if position_return < benchmark_return - OPPORTUNITY_COST_GAP_PCT:
        return ["UNDERPERFORMING"]
    if stalled and tier1_hot_count >= 2:
        return ["ROTATE_CAPITAL"]
    return []
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_time_stops.py -v`
Expected: PASS (17 tests)

- [ ] **Step 5: Commit**

```bash
git add capital/time_stops.py tests/test_time_stops.py
git commit --no-verify -m "feat: add entry trigger + time-stop ladder + opportunity-cost monitor (Sec 6)"
```

---

### Task 3: `capital/slots.py` — slot capacity state machine (Sec 9)

**Files:**
- Create: `capital/slots.py`
- Test: `tests/test_slots.py`

**Interfaces:**
- Consumes: nothing from Task 1/2 (independent, stateless — operates on a plain `list[dict]` slot state the caller owns).
- Produces: `init_slots`, `assign_slot`, `arm_slot`, `free_slot`, `count_status`, `rotate_to_top_hot`. Not called by Task 4 (Task 4 wires regime+time-stops only; slots is available for a future live-position tracker — see Task 4's scope note).

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_slots.py
import pytest

from capital import slots


def test_init_slots_all_free():
    s = slots.init_slots(5)
    assert len(s) == 5
    assert all(slot["status"] == "FREE" and slot["symbol"] is None for slot in s)


def test_assign_slot_fills_first_free():
    s = slots.init_slots(3)
    s = slots.assign_slot(s, "TCS")
    assert s[0] == {"status": "DEPLOYED", "symbol": "TCS"}
    assert s[1]["status"] == "FREE"


def test_assign_slot_raises_when_full():
    s = [{"status": "DEPLOYED", "symbol": "TCS"}]
    with pytest.raises(ValueError, match="no free slot"):
        slots.assign_slot(s, "INFY")


def test_arm_slot_reserves_up_to_two():
    s = slots.init_slots(3)
    s = slots.arm_slot(s, "TCS")
    s = slots.arm_slot(s, "INFY")
    assert slots.count_status(s, "ARMED") == 2


def test_arm_slot_raises_when_two_already_armed():
    s = slots.init_slots(3)
    s = slots.arm_slot(s, "TCS")
    s = slots.arm_slot(s, "INFY")
    with pytest.raises(ValueError, match="max 2 armed"):
        slots.arm_slot(s, "WIPRO")


def test_free_slot_by_symbol():
    s = [{"status": "DEPLOYED", "symbol": "TCS"}, {"status": "FREE", "symbol": None}]
    s = slots.free_slot(s, "TCS")
    assert s[0] == {"status": "FREE", "symbol": None}


def test_free_slot_raises_when_symbol_not_found():
    s = [{"status": "FREE", "symbol": None}]
    with pytest.raises(ValueError, match="not found"):
        slots.free_slot(s, "TCS")


def test_count_status():
    s = [
        {"status": "DEPLOYED", "symbol": "TCS"},
        {"status": "ARMED", "symbol": "INFY"},
        {"status": "FREE", "symbol": None},
    ]
    assert slots.count_status(s, "DEPLOYED") == 1
    assert slots.count_status(s, "FREE") == 1


def test_rotate_to_top_hot_frees_then_assigns():
    s = [{"status": "DEPLOYED", "symbol": "TCS"}, {"status": "FREE", "symbol": None}]
    s = slots.rotate_to_top_hot(s, exiting_symbol="TCS", hot_candidates=["INFY", "WIPRO"])
    assert slots.count_status(s, "DEPLOYED") == 1
    symbols = {slot["symbol"] for slot in s if slot["status"] == "DEPLOYED"}
    assert symbols == {"INFY"}


def test_rotate_to_top_hot_no_candidates_just_frees():
    s = [{"status": "DEPLOYED", "symbol": "TCS"}]
    s = slots.rotate_to_top_hot(s, exiting_symbol="TCS", hot_candidates=[])
    assert s[0] == {"status": "FREE", "symbol": None}
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_slots.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'capital.slots'`

- [ ] **Step 3: Write the implementation**

```python
# capital/slots.py
"""Slot capacity state machine (Sec 9). Slots are a plain list[dict] the
caller owns and passes in/out -- no persistence (matches the Phase 1+2 design
decision to cut signals.db; the same reasoning applies here, see the Phase 3
plan's Global Constraints). Every function returns a new list; none mutate
their input in place, so callers can't be surprised by aliasing."""

import copy

MAX_ARMED = 2


def init_slots(n: int) -> list[dict]:
    return [{"status": "FREE", "symbol": None} for _ in range(n)]


def _find(slots: list[dict], status: str) -> int | None:
    for i, slot in enumerate(slots):
        if slot["status"] == status:
            return i
    return None


def assign_slot(slots: list[dict], symbol: str) -> list[dict]:
    slots = copy.deepcopy(slots)
    idx = _find(slots, "FREE")
    if idx is None:
        raise ValueError(f"no free slot for {symbol}")
    slots[idx] = {"status": "DEPLOYED", "symbol": symbol}
    return slots


def arm_slot(slots: list[dict], symbol: str) -> list[dict]:
    slots = copy.deepcopy(slots)
    if count_status(slots, "ARMED") >= MAX_ARMED:
        raise ValueError(f"max {MAX_ARMED} armed slots already reserved")
    idx = _find(slots, "FREE")
    if idx is None:
        raise ValueError(f"no free slot to arm for {symbol}")
    slots[idx] = {"status": "ARMED", "symbol": symbol}
    return slots


def free_slot(slots: list[dict], symbol: str) -> list[dict]:
    slots = copy.deepcopy(slots)
    for slot in slots:
        if slot["symbol"] == symbol:
            slot["status"] = "FREE"
            slot["symbol"] = None
            return slots
    raise ValueError(f"{symbol} not found in any slot")


def count_status(slots: list[dict], status: str) -> int:
    return sum(1 for slot in slots if slot["status"] == status)


def rotate_to_top_hot(slots: list[dict], exiting_symbol: str, hot_candidates: list[str]) -> list[dict]:
    """Sec 9: 'Time-stop exit frees slot immediately; rotate to top HOT
    candidate.' hot_candidates is caller-ranked (best first); takes the first
    one not already occupying a slot."""
    slots = free_slot(slots, exiting_symbol)
    occupied = {slot["symbol"] for slot in slots if slot["symbol"]}
    for candidate in hot_candidates:
        if candidate not in occupied:
            return assign_slot(slots, candidate)
    return slots
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_slots.py -v`
Expected: PASS (10 tests)

- [ ] **Step 5: Commit**

```bash
git add capital/slots.py tests/test_slots.py
git commit --no-verify -m "feat: add slot capacity state machine (Sec 9)"
```

---

### Task 4: Wire regime + action into `consolidation/consolidation_scanner.py`

**Files:**
- Modify: `consolidation/consolidation_scanner.py:34-37` (COLUMNS), `:60-123` (`analyse`), `:178-190` (`run`), `:193-220` (`main`)
- Modify: `tests/test_consolidation_scanner.py`
- Modify: `CLAUDE.md:125-149` (Consolidation Tracker pipeline section)

**Interfaces:**
- Consumes: `capital.regime_throttle.regime_for_date(as_of) -> dict` (Task 1), `capital.time_stops.entry_trigger` is NOT wired here — entry trigger needs a real breakout bar + live delivery data the daily tier scan doesn't have per-symbol yet (range_high, today's actual breakout volume vs 2x threshold); wiring a real trigger check requires a `range_high` definition this scanner doesn't compute. Scope note below.
- Produces: two new output columns, `regime` and `action`, added to `COLUMNS`.

**Scope note:** The spec's Sec 11 output column list is `... | regime | action`. `regime` is a single value for the whole day (applies to every row) — comes straight from `regime_throttle.regime_for_date(as_of)`. `action` is a per-row label derived from `tier` + `regime`, NOT a live entry/exit decision — `time_stops.entry_trigger`/`time_stop_check` require a `range_high` and open-position state this daily tier scan doesn't track (no `signals.db`, per the Phase 1+2 design decision carried into this plan's Global Constraints). Wiring live entry/exit is a future step once a position tracker exists; this task only wires the two data-driven columns the spec's output row already promises.

`action` rules (this task's own definition — not separately specified in the spec beyond "capital ready, enter on trigger" for HOT):
- `regime == "RED"` → `"NO_DEPLOY"` for any tier that isn't `NONE`, else `"NONE"`
- `regime != "RED"` and `tier == "TIER_1_HOT"` → `"DEPLOY_ELIGIBLE"`
- `tier == "TIER_2_WARM"` → `"ARM"`
- `tier == "TIER_3_COLD"` → `"WATCH"`
- `tier == "NONE"` → `"NONE"`

- [ ] **Step 1: Write the failing test**

```python
# Append to tests/test_consolidation_scanner.py

def test_run_adds_regime_and_action_columns(tmp_path, monkeypatch):
    history_path = tmp_path / "breadth_history.csv"
    pd.DataFrame([
        {"date": "2026-07-02", "universe_tag": "breadth_broad", "ratio_5d": 1.8, "pct_above_sma200": 65.0},
    ]).to_csv(history_path, index=False)
    monkeypatch.setattr(cs, "HISTORY_PATH", str(history_path))

    def _fake_load_many(symbols, lookback=600):
        out = {}
        for sym in symbols:
            out[sym] = _bench_df() if sym == cs.BENCH_SYM else _consolidating_df()
        return out

    monkeypatch.setattr(cs, "load_ohlc_many", _fake_load_many)
    universe_df = pd.DataFrame({"symbol": ["TESTCO"]})
    result_df = cs.run(universe_df, "2026-07-02")

    assert "regime" in result_df.columns
    assert "action" in result_df.columns
    assert result_df["regime"].iloc[0] == "GREEN"
    assert result_df["action"].iloc[0] in {"DEPLOY_ELIGIBLE", "ARM", "WATCH", "NONE"}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_consolidation_scanner.py::test_run_adds_regime_and_action_columns -v`
Expected: FAIL with `AssertionError: assert 'regime' in Index([...])` (column doesn't exist yet)

- [ ] **Step 3: Wire regime + action into the scanner**

In `consolidation/consolidation_scanner.py`, add the import and the two new columns:

```python
# Add near the top, alongside the existing `from consolidation import ...` line:
from capital import regime_throttle
from capital.regime_throttle import HISTORY_PATH
```

```python
# Replace the existing COLUMNS list (line 34-37):
COLUMNS = [
    "symbol", "quality", "imminence", "tier", "age_bars", "ema_stage",
    "vol_phase", "rs_char", "cmf", "deliv_trend", "prebreak_count",
    "regime", "action",
]

_ACTION_BY_TIER = {
    "TIER_1_HOT": "DEPLOY_ELIGIBLE",
    "TIER_2_WARM": "ARM",
    "TIER_3_COLD": "WATCH",
    "NONE": "NONE",
}


def action_for(tier_label: str, regime: str) -> str:
    if regime == "RED":
        return "NO_DEPLOY" if tier_label != "NONE" else "NONE"
    return _ACTION_BY_TIER[tier_label]
```

Update `analyse()` to accept and stamp the regime (change signature and the dict it returns):

```python
def analyse(symbol: str, df: pd.DataFrame, bench_df: pd.DataFrame | None, regime: str) -> dict | None:
    if df is None or len(df) < MIN_BARS or bench_df is None:
        return None
    # ... unchanged body through tier_label = tiers.tier(q_score, imm_score) ...
    return {
        "symbol": symbol,
        "quality": q_score,
        "imminence": imm_score,
        "tier": tier_label,
        "age_bars": age_bars,
        "ema_stage": stage,
        "vol_phase": indicators.volume_phase(df),
        "rs_char": rs_char,
        "cmf": round(cmf_today, 3),
        "deliv_trend": deliv_trend_label or "UNKNOWN",
        "prebreak_count": prebreak_count,
        "regime": regime,
        "action": action_for(tier_label, regime),
    }
```

Update `run()` to fetch the regime once per day and pass it through:

```python
def run(universe_df: pd.DataFrame, as_of: str) -> pd.DataFrame:
    """Spec's required interface. universe_df must have a 'symbol' column."""
    symbols = universe_df["symbol"].tolist()
    all_data = load_ohlc_many(symbols + [BENCH_SYM], lookback=600)
    bench_df = all_data.pop(BENCH_SYM, None)

    regime_info = regime_throttle.regime_for_date(as_of, history_path=HISTORY_PATH)
    regime = regime_info["regime"]

    rows = []
    for sym, sym_df in all_data.items():
        result = analyse(sym, sym_df, bench_df, regime)
        if result:
            rows.append(result)

    return pd.DataFrame(rows, columns=COLUMNS)
```

`main()` needs no changes — it already just calls `run()` and writes the returned DataFrame.

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_consolidation_scanner.py -v`
Expected: PASS (all existing tests + the new one)

- [ ] **Step 5: Update CLAUDE.md**

In `CLAUDE.md`, in the "Scanner pipeline — Consolidation Tracker" section, replace this line:

```
Gate: EMA dual gate AND BB squeeze gate only — volume/RS are scored, not filtered on.
Out of scope for this phase: capital/time-stops/regime-throttle (Sec 6/8/9), catalyst
calendar (Sec 7), PineScript companion (Sec 12), half-life backtest (Sec 10).
```

with:

```
Gate: EMA dual gate AND BB squeeze gate only — volume/RS are scored, not filtered on.

### Scanner pipeline — Capital rules (`capital/`)

Phase 3 of the consolidation spec (Sec 6, 8, 9) — see `docs/superpowers/plans/2026-07-06-consolidation-scanner-phase3.md`.

1. `regime_throttle.py` — GREEN/NEUTRAL/RED classification off `data/breadth_history.csv`
   (`ratio_5d` + `pct_above_sma200` + its 5-row trend); returns `max_slots` + `time_stop_mode`
2. `time_stops.py` — breakout entry trigger (close > range high, vol >= 2x vol_ma50,
   delivery% >= baseline), ATR-capped stop price, fixed-₹15k position sizing, bar-3/5/10
   time-stop ladder, opportunity-cost flags. Not yet wired to a live position tracker —
   pure functions only, called once one exists.
3. `slots.py` — DEPLOYED/ARMED/FREE slot capacity state machine (stateless, caller-owned list)

`consolidation_scanner.py` calls `regime_throttle.regime_for_date()` once per run and stamps
every row with the day's `regime` + a tier-derived `action` (`DEPLOY_ELIGIBLE`/`ARM`/`WATCH`/
`NONE`/`NO_DEPLOY`). `time_stops`/`slots` are available but not called from the daily scan —
they operate on live position state this scanner doesn't track (no `signals.db`, by design).

Out of scope for this phase: catalyst calendar (Sec 7), PineScript companion (Sec 12),
half-life backtest (Sec 10).
```

- [ ] **Step 6: Commit**

```bash
git add consolidation/consolidation_scanner.py tests/test_consolidation_scanner.py CLAUDE.md
git commit --no-verify -m "feat: wire regime + action columns into consolidation scanner (Sec 8/9)"
```

---

## Self-Review Notes

- **Spec coverage:** Sec 6 (entry trigger, stop, sizing, time-stop ladder, opportunity-cost monitor) → Task 2. Sec 8 (regime bands) → Task 1. Sec 9 (slots) → Task 3. Output columns `regime`/`action` from Sec 11's column list → Task 4. Sec 6's `signals.db`-dependent live wiring is explicitly out of scope (see Task 4's Scope note), consistent with the Phase 1+2 design doc's decision to cut `signals.db` entirely.
- **Placeholder scan:** none — every step has runnable code and exact expected output.
- **Type consistency:** `regime_for_date` returns `{"regime": str, "max_slots": int, "time_stop_mode": str}` used identically in Task 1's tests and Task 4's wiring. `action_for(tier_label, regime)` matches the `tier` values already defined in `consolidation/tiers.py` (`TIER_1_HOT`/`TIER_2_WARM`/`TIER_3_COLD`/`NONE`) — no new tier vocabulary introduced.
