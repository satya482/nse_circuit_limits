# Weekly WaveTrend Zone Overlay — Design Spec
*2026-07-01*

## Goal

Overlay weekly WaveTrend context onto two surfaces:

1. **Python scanner** — flag stocks in `wt_bullcross_scanner.py` where the current daily bar falls inside an active weekly WT bull-cross zone. Show as `W↑Nd` inside the symbol column link text.
2. **Pine Script** — new `overlay=true` indicator that shades the daily chart background green from the first bar the weekly WT bull cross became visible, until a weekly bear cross ends the zone.

---

## Zone Definition

| Event | Condition |
|-------|-----------|
| **Zone start** | Weekly WT1 crosses above WT2 (`ta.crossover`) |
| **Zone end** | Weekly WT1 crosses below WT2 (`ta.crossunder`) |
| **Cross level** | Configurable: Any (default) / Oversold L2 (wt2 ≤ −53) / Oversold L1 (wt2 ≤ −60) |
| **WT params** | n1=10, n2=21, wt2=SMA(wt1,4) — identical to `Satya_WT_CROSS_LB_v2` |

---

## Python Changes

### 1. `wavetrend_scanner.py` — new function

```python
def weekly_wt_zone(df: pd.DataFrame, n1: int = 10, n2: int = 21) -> tuple[bool, int]:
```

**Input:** daily OHLCV DataFrame from `load_ohlc()` (columns: date, open, high, low, close, volume; date is plain string, oldest-first).

**Algorithm:**
1. Parse `date` column → datetime, set as index.
2. Resample to weekly (`W-FRI`): open=first, high=max, low=min, close=last, volume=sum. Drop NaN rows.
3. Compute weekly WT (same math as `WaveTrendCalculator`):
   - `ap = (high + low + close) / 3`
   - `esa = ap.ewm(span=n1, adjust=False).mean()`
   - `d = |ap - esa|.ewm(span=n1, adjust=False).mean()`
   - `ci = (ap - esa) / (0.015 * d)`
   - `wt1 = ci.ewm(span=n2, adjust=False).mean()`
   - `wt2 = wt1.rolling(4, min_periods=4).mean()`
4. Drop NaN wt2 rows. Need ≥ `n1 + n2 + 10` valid weekly bars (~35 weekly bars = ~175 daily bars).
5. Detect last weekly bull cross: `wt1 > wt2 AND wt1.shift(1) <= wt2.shift(1)`.
6. If no bull cross found → return `(False, 0)`.
7. Detect any weekly bear cross strictly after the last bull cross: `wt1 < wt2 AND wt1.shift(1) >= wt2.shift(1)`. If found → return `(False, 0)`.
8. Count daily bars from `(last_bull_friday − 4 days)` inclusive (Monday of cross week). Return `(True, count)`.

**Edge cases:**
- Insufficient data → `(False, 0)`
- Bull cross on final weekly bar (this week still open, no bear cross) → `(True, days)` — correct, zone active
- Float equality guard: use `<=` not `==` for cross detection (pandas shift-compare, no float equality)

### 2. `wt_bullcross_scanner.py`

**`analyse()` function** — add after `squeeze = _bb_kc_squeeze(df_raw)`:
```python
wz_in, wz_days = weekly_wt_zone(df_raw)
```

Add to return dict:
```python
"weekly_zone": wz_in,
"weekly_zone_days": wz_days,
```

**`_row()` function** — replace sym_label build:
```python
sym_label = sym
if f.get("weekly_zone"):
    sym_label += f" W↑{f['weekly_zone_days']}d"
if trend_syms and sym in trend_syms:
    sym_label += " ★"
```

Output examples:
- `[SJVN W↑12d](link)` — weekly zone active, no trend leader
- `[SJVN W↑12d ★](link)` — both
- `[SJVN ★](link)` — trend leader only, no weekly zone
- `[SJVN](link)` — neither

**Scan definition table** — add one row:
```
| W↑Nd in Symbol | Days in weekly WT bull-cross zone (any cross; ends on weekly bear cross) |
```

**Import:** Update the existing import line at top of scanner:
```python
# before
from wavetrend_scanner import WaveTrendCalculator
# after
from wavetrend_scanner import WaveTrendCalculator, weekly_wt_zone
```

---

## Pine Script — `Satya_WT_Weekly_Zone_Overlay.pine`

**Type:** `overlay=true` companion indicator. Add on daily price chart alongside `Satya_WT_CROSS_LB_v2`.

### Inputs

| Group | Input | Default |
|-------|-------|---------|
| WaveTrend (match v2) | Channel Length `n1` | 10 |
| WaveTrend (match v2) | Average Length `n2` | 21 |
| Zone Filter | Min cross level | `"Any"` (options: Any / Oversold L2 ≤−53 / Oversold L1 ≤−60) |
| Display | Zone background color | `color.new(color.green, 85)` |
| Display | Show zone-start label | `true` |

### Logic

```pine
f_wt() =>
    ap  = hlc3
    esa = ta.ema(ap, n1)
    d   = ta.ema(math.abs(ap - esa), n1)
    ci  = (ap - esa) / (0.015 * d)
    wt1 = ta.ema(ci, n2)
    wt2 = ta.sma(wt1, 4)
    [wt1, wt2]

[wt1_w, wt2_w] = request.security(syminfo.tickerid, "W", f_wt(),
                                   lookahead=barmerge.lookahead_off)

bullCross_w = ta.crossover(wt1_w, wt2_w) and (
    crossLevel == "Any"                ? true :
    crossLevel == "Oversold L2 (≤-53)" ? wt2_w <= -53 :
                                         wt2_w <= -60)
bearCross_w = ta.crossunder(wt1_w, wt2_w)

var bool inZone = false
if bullCross_w
    inZone := true
if bearCross_w
    inZone := false

bgcolor(inZone ? zoneColor : na, title="Weekly WT Bull Zone")

if showLabel and bullCross_w
    label.new(bar_index, high, "W↑",
              style=label.style_label_up,
              color=color.new(color.green, 50),
              textcolor=color.white,
              size=size.small)
```

### Lookahead note

`lookahead_off` (default) means zone shading starts on the **first daily bar of the week AFTER** the weekly bull cross forms — a one-week visual delay. This is the correct safe default.

For exact visual timing (shade from the cross week itself), change to `lookahead=barmerge.lookahead_on`. Acceptable for a display-only overlay; never use `lookahead_on` for signal generation or backtesting.

---

## File Summary

| File | Change |
|------|--------|
| `wavetrend_scanner.py` | Add `weekly_wt_zone()` function |
| `wt_bullcross_scanner.py` | Call `weekly_wt_zone()` in `analyse()`; update `_row()` sym_label; update scan def table |
| `Satya_WT_Weekly_Zone_Overlay.pine` | New file (Downloads folder or repo root) |

No new Python modules. No schema changes to `WaveTrendSignal` dataclass (zone data only needed in scanner output, not in the signal object).

---

## Out of Scope

- Applying weekly zone filter as a hard gate (it's informational only — stocks without a weekly zone still appear in scan)
- Adding weekly zone to other scanners (EMA25-ZL, momentum) — add when needed
- Pine Script alerts for zone start/end — add when needed
