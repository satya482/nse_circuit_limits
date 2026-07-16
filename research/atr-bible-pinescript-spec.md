> **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# ATR BIBLE — Pine Script Suite
## Specification v1.0 | Rajan Mehta System | NSE Swing Trading

---

## DESIGN PHILOSOPHY

> *"ATR doesn't tell you direction. It tells you energy. Energy always seeks release."*

This suite has one job: take the ATR Bible framework and put it directly on the chart with zero mental math required. Every ₹ value, every state verdict, every sizing number is auto-calculated and displayed. The trader reads the chart. The script does the arithmetic.

**Human-friendly means:** one glance tells you the CR state. One input (entry price) unlocks stop, targets, and position size. Rajan's verdicts appear in plain English, not raw numbers.

---

## ARCHITECTURE — TWO SCRIPTS, ONE SYSTEM

Pine Script cannot combine a chart overlay and a panel oscillator in a single indicator. The solution is a two-script suite that runs in tandem.

```
┌─────────────────────────────────────────────────────────┐
│  SCRIPT A: ATR_BIBLE_OVERLAY  (overlay = true)          │
│  ─ Candle coloring by CR state                          │
│  ─ Stop line + Entry line + T1/T2/T3 target lines       │
│  ─ ATR noise corridor (optional)                        │
│  ─ Squeeze / exit / distribution signals                │
│  ─ Dashboard table (top-right)                          │
│  ─ NSE flags: [CIRCUIT], [SPEC], [EP WIN]               │
└─────────────────────────────────────────────────────────┘
        │
        │ (same ticker, same timeframe, shared inputs)
        │
┌─────────────────────────────────────────────────────────┐
│  SCRIPT B: ATR_BIBLE_PANEL  (overlay = false)           │
│  ─ ATR(10) line + ATR(50) line + fill between them      │
│  ─ Compression Ratio (CR) line with colored zones       │
│  ─ CR threshold reference lines (0.5, 0.7, 1.0, 1.5, 2.0)│
│  ─ State verdict label (right side, plain English)      │
│  ─ ATR expansion histogram bars                         │
└─────────────────────────────────────────────────────────┘
```

**User setup:** Add Script A to chart. Add Script B below. Both use identical input parameters — user sets them once in each script.

---

## SECTION 1: SHARED INPUTS (identical in both scripts)

These parameters must be set the same in both scripts. Consider grouping them at the top of each script under a labeled section comment.

### Group 1 — ATR Core
| Input ID | Label | Type | Default | Notes |
|---|---|---|---|---|
| `atr_fast` | ATR Fast Period | int | `10` | Tactical ATR for stops and sizing |
| `atr_slow` | ATR Slow Period | int | `50` | Strategic ATR for compression ratio |

### Group 2 — Position Setup
| Input ID | Label | Type | Default | Notes |
|---|---|---|---|---|
| `risk_inr` | Risk Per Trade (₹) | float | `15000` | Fixed ₹ risk per trade |
| `entry_px` | Entry Price (0 = current close) | float | `0` | Set to 0 for live scan mode. Set to actual entry price to lock stop/target lines. |
| `setup_type` | Setup Type | enum | `"1PB"` | Options: VCP / 1PB / GRIND / 3WT / EP |

**Stop multiplier is auto-derived from `setup_type`:**
```
VCP  → 1.0× ATR(10)
3WT  → 1.0× ATR(10)
1PB  → 1.5× ATR(10)
GRIND→ 2.0× ATR(10)
EP   → 2.5× ATR(10)
```

### Group 3 — CR Thresholds (adjustable, not hardcoded)
| Input ID | Label | Type | Default |
|---|---|---|---|
| `cr_extreme` | Extreme Squeeze Level | float | `0.50` |
| `cr_build` | Squeeze Building Level | float | `0.70` |
| `cr_expand` | Expansion Start Level | float | `1.00` |
| `cr_extended` | Expanded Level | float | `1.50` |
| `cr_danger` | Overextended / Danger Level | float | `2.00` |

---

## SECTION 2: SCRIPT A — OVERLAY INPUTS (additional)

### Group 4 — Display Toggles
| Input ID | Label | Type | Default |
|---|---|---|---|
| `show_dashboard` | Show Dashboard Table | bool | `true` |
| `show_stops` | Show Stop Line | bool | `true` |
| `show_targets` | Show T1 / T2 / T3 Lines | bool | `true` |
| `show_atr_corridor` | Show ATR Noise Corridor | bool | `false` |
| `color_candles` | Color Candles by CR State | bool | `true` |
| `show_squeeze_signal` | Mark Squeeze Bars | bool | `true` |
| `show_exit_warn` | Show Exit / Distribution Warnings | bool | `true` |
| `show_nse_flags` | Show NSE Flags (Circuit, Spec, EP Window) | bool | `true` |

### Group 5 — Dashboard Position
| Input ID | Label | Type | Default | Options |
|---|---|---|---|---|
| `dash_pos` | Dashboard Position | enum | `"top_right"` | top_right / top_left / bottom_right |

### Group 6 — Line Persistence
| Input ID | Label | Type | Default |
|---|---|---|---|
| `line_extend_bars` | Extend Lines (bars to the right) | int | `50` |

---

## SECTION 3: CORE CALCULATIONS (both scripts)

### ATR Core
```pine
// True Range
tr = math.max(high - low,
              math.abs(high - close[1]),
              math.abs(low  - close[1]))

// ATR values
atr10 = ta.atr(atr_fast)    // e.g. ta.atr(10)
atr50 = ta.atr(atr_slow)    // e.g. ta.atr(50)

// Compression Ratio — guard against divide-by-zero on early bars
cr = atr50 > 0 ? atr10 / atr50 : na
```

### CR State Machine
Six states. One verdict per bar. No ambiguity.
```pine
cr_state =
    cr < cr_extreme  ? "EXTREME SQUEEZE" :
    cr < cr_build    ? "SQUEEZE BUILDING" :
    cr < cr_expand   ? "NORMAL" :
    cr < cr_extended ? "EXPANDING" :
    cr < cr_danger   ? "EXPANDED" :
    "OVEREXTENDED"
```

### Rajan's Verdict Voice (for labels and dashboard)
Map the technical state to the trading verdict:
```pine
rajan_verdict =
    cr < cr_extreme  ? "COILED. ENTER AT TRIGGER." :
    cr < cr_build    ? "BUILDING. ADD TO WATCHLIST." :
    cr < cr_expand   ? "NORMAL. WAIT." :
    cr < cr_extended ? "BREAKING OUT. CONFIRM VOLUME." :
    cr < cr_danger   ? "LET IT RUN. TRAIL STOP." :
    "DANGER ZONE. REDUCE OR EXIT."
```

### Stop, Target, and Sizing
```pine
// Entry price: 0 = use current close (live scan mode)
ep = entry_px > 0 ? entry_px : close

// Stop multiplier auto-set from setup
stop_mult =
    setup_type == "VCP"   ? 1.0 :
    setup_type == "3WT"   ? 1.0 :
    setup_type == "1PB"   ? 1.5 :
    setup_type == "GRIND" ? 2.0 : 2.5   // EP

// Stop level and stop amount (₹ risk per share)
stop_lvl = ep - (stop_mult * atr10)
stop_amt  = ep - stop_lvl               // ₹ per share

// Target ladder
t1 = ep + (3 * atr10)
t2 = ep + (5 * atr10)
t3 = ep + (8 * atr10)

// R multiples at each target (should read 3.0, 5.0, 8.0)
r_t1 = stop_amt > 0 ? (t1 - ep) / stop_amt : na
r_t2 = stop_amt > 0 ? (t2 - ep) / stop_amt : na
r_t3 = stop_amt > 0 ? (t3 - ep) / stop_amt : na

// Position sizing
shares    = stop_amt > 0 ? math.floor(risk_inr / stop_amt) : 0
pos_value = shares * ep
```

### 3-Star Squeeze Detection
All three conditions must be true simultaneously. This is the highest-conviction setup in the system.
```pine
star1 = cr < cr_extreme                                  // ATR coiled
star2 = volume < ta.sma(volume, 20) * 0.50              // Volume dried up
star3 = high < high[1] and low > low[1]                 // Inside bar

squeeze_3star = star1 and star2 and star3
squeeze_1star = star1 and not squeeze_3star             // Squeeze, but not full signal
```

### Exit / Distribution Signals
```pine
// ATR expansion on a down day — the single most important exit warning
atr_expand_down = (high - low) > (atr10[1] * 1.5) and close < open

// Distribution: 3 consecutive days of ATR expansion + lower closes
dist_3day = atr_expand_down    and atr_expand_down[1]    and atr_expand_down[2]
        and close < close[1]   and close[1] < close[2]
```

### NSE-Specific Flag Detection
```pine
// Circuit suspect: today's range is < 20% of ATR(50) — suggests circuit hit
circuit_suspect = (high - low) < (atr50 * 0.20) and show_nse_flags

// Low liquidity / SPEC suspect: daily notional < ~₹15Cr (approximate)
// volume * close in ₹ — user must confirm actual notional
spec_suspect = (volume * close) < 15_00_00_000 and show_nse_flags

// EP Season: Jan, Apr, Jul, Oct — results season windows
m = month(time)
ep_season = (m == 1 or m == 4 or m == 7 or m == 10) and show_nse_flags
```

---

## SECTION 4: SCRIPT A VISUAL SPEC — OVERLAY

### 4.1 Candle Coloring

Color scheme maps the CR state machine directly to the price bars. One glance → instant state read.

| Condition | Candle Color | Hex | Transparency |
|---|---|---|---|
| 3-Star Squeeze | Bright mint green | `#00FF88` | 0% |
| Extreme Squeeze (1-star) | Green | `#3FB950` | 15% |
| Squeeze Building | Blue | `#58A6FF` | 25% |
| Normal | na (default) | — | — |
| Expanding | Amber | `#D29922` | 25% |
| Expanded | Orange | `#E8A020` | 30% |
| Overextended | Red | `#F85149` | 20% |

```pine
bar_col =
    squeeze_3star         ? color.new(#00FF88, 0)  :
    star1                 ? color.new(#3FB950, 15) :
    cr < cr_build         ? color.new(#58A6FF, 25) :
    cr > cr_danger        ? color.new(#F85149, 20) :
    cr > cr_extended      ? color.new(#E8A020, 30) :
    cr > cr_expand        ? color.new(#D29922, 25) :
    na

barcolor(color_candles ? bar_col : na)
```

### 4.2 Background Highlighting

Subtle, non-distracting. Only fires on high-signal events.

| Condition | Background Color | Transparency |
|---|---|---|
| 3-Star Squeeze bar | Green | 93% |
| ATR expand on down day (exit warning) | Red | 88% |
| Distribution confirmed (3-day) | Deep red | 82% |
| EP Season (Jan/Apr/Jul/Oct) | Faint gold | 96% |

```pine
bgcolor(squeeze_3star   ? color.new(#3FB950, 93) : na)
bgcolor(dist_3day       ? color.new(#F85149, 82) : na, force_overlay=true)
bgcolor(atr_expand_down and not dist_3day ? color.new(#F85149, 88) : na)
bgcolor(ep_season       ? color.new(#D29922, 96) : na)
```

### 4.3 ATR Noise Corridor (optional toggle)

When enabled, plots ±1 ATR(10) bands around close. Shows the noise envelope the stock normally moves within. A breakout beyond this corridor is a genuine structural move.

```pine
upper_corridor = close + atr10
lower_corridor = close - atr10

// Only plot when toggle is on
plot(show_atr_corridor ? upper_corridor : na, "ATR Upper",
     color=color.new(#58A6FF, 70), style=plot.style_line, linewidth=1)
plot(show_atr_corridor ? lower_corridor : na, "ATR Lower",
     color=color.new(#58A6FF, 70), style=plot.style_line, linewidth=1)
```

### 4.4 Stop and Target Lines

Lines are only drawn when `entry_px` is explicitly set (> 0). In live scan mode (entry_px = 0), these lines follow close — showing live sizing but not committing to a trade.

**Approach:** Use `line.new()` with `extend=extend.right` and delete previous bar's line on each new bar (var line approach).

| Line | Color | Style | Label Text |
|---|---|---|---|
| Stop | `#F85149` (red) | Solid, width 2 | `"STOP ₹{stop_lvl} (−₹{stop_amt} / share)"` |
| Entry | `#E6EDF3` (white) | Dashed, width 1 | `"ENTRY ₹{ep} · {setup_type}"` |
| T1 | `#2D6A3F` (dim green) | Dotted, width 1 | `"T1 ₹{t1} · +3R · Sell 50%"` |
| T2 | `#3FB950` (green) | Dashed, width 1 | `"T2 ₹{t2} · +5R · Sell 25%"` |
| T3 | `#7FE09F` (bright green) | Solid, width 2 | `"T3 ₹{t3} · +8R · Trail"` |

Lines extend `line_extend_bars` bars to the right. Labels sit at the right end of each line.

### 4.5 Signals (plotshape)

| Signal | Condition | Shape | Position | Color | Label | Size |
|---|---|---|---|---|---|---|
| 3-Star Squeeze | `squeeze_3star` | `shape.triangleup` | `location.belowbar` | `#00FF88` | `"★★★"` | `size.normal` |
| 1-Star Squeeze | `squeeze_1star` | `shape.triangleup` | `location.belowbar` | `#3FB950` | `"★"` | `size.small` |
| Exit Warning | `atr_expand_down and not dist_3day` | `shape.xcross` | `location.abovebar` | `#F85149` | `"⚠"` | `size.small` |
| Distribution | `dist_3day` | `shape.arrowdown` | `location.abovebar` | `#C03030` | `"DIST"` | `size.normal` |
| Circuit Suspect | `circuit_suspect` | `shape.circle` | `location.abovebar` | `#FF8800` | `"⚡"` | `size.small` |
| SPEC Suspect | `spec_suspect` | `shape.square` | `location.abovebar` | `#FF8800` | `"₹"` | `size.tiny` |
| EP Season Open | `ep_season and not ep_season[1]` | `shape.flag` | `location.top` | `#D29922` | `"EP WIN"` | `size.small` |

### 4.6 Dashboard Table

A `table.new()` with 10 rows × 2 columns. Positioned at `dash_pos` (default: top right). Updates every bar using `table.cell()`.

**Table structure:**

| Row | Column 0 (Label) | Column 1 (Value) | Row Color Condition |
|---|---|---|---|
| 0 | `"ATR BIBLE · {setup_type}"` | `"{ticker}"` | Header — dark bg |
| 1 | `"ATR(10)"` | `"₹{atr10}"` | Default |
| 2 | `"ATR(50)"` | `"₹{atr50}"` | Default |
| 3 | `"CR"` | `"{cr} · {cr_state}"` | Green if squeeze, red if overextended |
| 4 | `"VERDICT"` | `"{rajan_verdict}"` | Matches CR state color |
| 5 | `"STOP (−{stop_mult}×ATR)"` | `"₹{stop_lvl} / Risk ₹{stop_amt}/sh"` | Red bg |
| 6 | `"POSITION SIZE"` | `"{shares} shares · ₹{pos_value}"` | Default |
| 7 | `"T1 (3× ATR)"` | `"₹{t1} · {r_t1}R · Sell 50%"` | Dim green |
| 8 | `"T2 (5× ATR)"` | `"₹{t2} · {r_t2}R · Sell 25%"` | Green |
| 9 | `"T3 (8× ATR)"` | `"₹{t3} · {r_t3}R · Trail"` | Bright green |

**Optional NSE flag rows** (appended below row 9, only if flags detected):

| Condition | Flag Row Text | Color |
|---|---|---|
| `circuit_suspect` | `"⚡ [CIRCUIT] — ATR unreliable today"` | Orange |
| `spec_suspect` | `"[SPEC] — Low notional. Half size."` | Orange |
| `ep_season` | `"[EP WIN] — Results season. Highest EP rate."` | Gold |

**Dashboard color palette:**

| Element | Background | Text |
|---|---|---|
| Header row | `#1C2128` | `#58A6FF` |
| Label column | `#161B22` | `#8B949E` |
| Squeeze value | `#1A4228` | `#3FB950` |
| Overextended value | `#3D1A1A` | `#F85149` |
| Stop row | `#2A1010` | `#F85149` |
| Target rows | `#0D1F10` | `#3FB950` |
| Normal value | `#21262D` | `#E6EDF3` |
| Flag row | `#2A1A00` | `#FF8800` |

---

## SECTION 5: SCRIPT B VISUAL SPEC — PANEL

The panel shows the mechanics of contraction and expansion directly — the ATR lines, the CR, and the zone context. It answers one question: *where are we in the volatility cycle right now?*

### 5.1 ATR Lines + Fill

```pine
atr10_plot = plot(atr10, "ATR(10) Tactical", color=#3FB950, linewidth=2)
atr50_plot = plot(atr50, "ATR(50) Strategic", color=#58A6FF, linewidth=1, style=plot.style_line)

// Fill between them:
// Green fill when ATR10 < ATR50 → contraction (squeeze building)
// Red fill when ATR10 > ATR50  → expansion (trade active or distribution)
fill(atr10_plot, atr50_plot,
     atr10 < atr50
         ? color.new(#3FB950, 85)   // green = squeeze
         : color.new(#F85149, 85))  // red = expansion
```

**Reading the fill:**
- Thin green fill narrowing → squeeze deepening → setup forming
- Green fill disappearing → expansion beginning → trade is live
- Wide red fill → ATR expanded far above baseline → overextended, watch for reversal

### 5.2 CR Line + Threshold Zones

The CR line is the core of the panel. Color changes dynamically with CR state.

```pine
cr_color =
    cr < cr_extreme  ? #3FB950 :   // Bright green — extreme squeeze
    cr < cr_build    ? #58A6FF :   // Blue — building
    cr < cr_expand   ? #484F58 :   // Gray — normal
    cr < cr_extended ? #D29922 :   // Amber — expanding
    cr < cr_danger   ? #E8A020 :   // Orange — expanded
    #F85149                         // Red — overextended

plot(cr, "Compression Ratio", color=cr_color, linewidth=2)
```

**Horizontal reference lines (hline):**

| Level | Label | Color | Line Style |
|---|---|---|---|
| 0.50 | `"Extreme Squeeze"` | `#3FB950` | Dashed |
| 0.70 | `"Squeeze Building"` | `#58A6FF` | Dotted |
| 1.00 | `"Normal"` | `#484F58` | Dotted |
| 1.50 | `"Expanded"` | `#D29922` | Dotted |
| 2.00 | `"Overextended / Danger"` | `#F85149` | Dashed |

**Zone fills between hlines (bgcolor):**

```pine
bgcolor(cr < cr_extreme ? color.new(#3FB950, 90) : na)      // Squeeze zone — green
bgcolor(cr > cr_danger  ? color.new(#F85149, 90) : na)      // Danger zone — red
```

### 5.3 ATR Expansion Histogram

A histogram plot showing how much today's TR exceeds ATR(10). When bars spike above zero, volatility is expanding. When bars hug zero or go negative, volatility is contracting.

```pine
atr_delta = tr - atr10       // Positive = expanding, Negative = contracting

hist_color =
    atr_delta > 0 and close < open ? #F85149 :   // Expanding on down day → EXIT WARNING
    atr_delta > 0                  ? #3FB950 :   // Expanding on up day → healthy
    #484F58                                       // Contracting → squeeze building

plot(atr_delta, "ATR Delta", style=plot.style_histogram,
     color=hist_color, linewidth=2)

hline(0, "Zero", color=#30363D)
```

### 5.4 State Verdict Label (right side of panel)

A `label.new()` placed on the last bar, right side, showing the current verdict in plain English. Updates every bar.

```pine
// Delete previous label, draw new one (var approach)
if barstate.islast
    label.delete(verdict_label)
    verdict_label := label.new(
        bar_index, cr,
        str.format("{0}\nCR: {1,number,#.##}", rajan_verdict, cr),
        style    = label.style_label_left,
        color    = cr < cr_extreme ? color.new(#3FB950, 70) :
                   cr > cr_danger  ? color.new(#F85149, 70) :
                   color.new(#21262D, 70),
        textcolor = #E6EDF3,
        size     = size.small
    )
```

---

## SECTION 6: ALERT CONDITIONS — 7 TOTAL

All alerts fire on `alert.freq_once_per_bar_close` to avoid intrabar noise. Alert messages include ticker, timeframe, and key values.

### Alert 1 — Extreme Squeeze Detected
**Trigger:** `ta.crossunder(cr, cr_extreme)` (CR drops below 0.50)
```
Message: "★ SQUEEZE: {ticker} | CR={cr} dropped below {cr_extreme}.
          ATR(10)=₹{atr10} | Setup={setup_type} | Check chart for entry trigger."
```

### Alert 2 — 3-Star Squeeze (Maximum Conviction)
**Trigger:** `squeeze_3star` (all three conditions met simultaneously)
```
Message: "★★★ 3-STAR SQUEEZE: {ticker} | CR={cr} | Volume={vol}% of avg | Inside bar.
          All three squeeze conditions active. Maximum conviction.
          Stop({setup_type})=₹{stop_lvl} | Shares=₹15K risk → {shares}"
```

### Alert 3 — Expansion Starting (Squeeze Released)
**Trigger:** `ta.crossover(cr, cr_build)` AND `cr[1] < cr_extreme` (CR rising from squeeze)
```
Message: "EXPANSION: {ticker} | CR={cr} rising from squeeze.
          ATR(10)=₹{atr10} | Confirm volume before entry.
          If VCP/3WT structure present — trigger activated."
```

### Alert 4 — Exit Warning (ATR Expand on Down Day)
**Trigger:** `atr_expand_down` AND `not atr_expand_down[1]` (first occurrence)
```
Message: "⚠ EXIT WARNING: {ticker} | ATR expanded {mult}× on a down close.
          Institutional selling possible. Check position.
          Reduce if Phase 1 (pre-T1). Exit immediately if distribution."
```

### Alert 5 — Distribution Confirmed (3-Day)
**Trigger:** `dist_3day` AND `not dist_3day[1]`
```
Message: "⚠⚠ DISTRIBUTION: {ticker} | 3 consecutive days: expanding ATR + lower closes.
          Exit all. Do not average. Do not re-enter same week."
```

### Alert 6 — Overextended (CR Danger Zone)
**Trigger:** `ta.crossover(cr, cr_danger)` (CR crosses above 2.0)
```
Message: "OVEREXTENDED: {ticker} | CR={cr} above {cr_danger}.
          ATR expanded far above baseline. Distribution risk elevated.
          Trail stops to 20-day MA. Reduce position."
```

### Alert 7 — Circuit Suspect
**Trigger:** `circuit_suspect` (first time today's range is < 20% of ATR50)
```
Message: "⚡ [CIRCUIT] SUSPECT: {ticker} | Range={range} vs ATR50={atr50}.
          ATR unreliable. Do not use ATR-based stops today.
          Use prior pivot structure instead."
```

---

## SECTION 7: HUMAN-FRIENDLY DESIGN PRINCIPLES

These principles govern every implementation decision. When in doubt, refer back to these.

### 7.1 Rajan's Voice in Labels
The dashboard and panel labels speak in verdicts, not statistics. The trader reads *"COILED. ENTER AT TRIGGER."* not *"CR: 0.43"*. Raw numbers appear as secondary information only.

### 7.2 Zero Mental Math
Every ₹ value auto-calculates. Entry price input unlocks all downstream values simultaneously: stop level, stop amount per share, shares to buy, position value, T1/T2/T3 prices, and R multiples. The trader reads the dashboard and executes — no calculator required.

### 7.3 Setup-Aware at All Times
The setup dropdown (VCP / 1PB / GRIND / 3WT / EP) is the master switch. Changing the setup automatically changes the stop multiplier, stop level, shares count, and position value displayed. The entire dashboard recalculates in one click.

### 7.4 Candle Color IS the CR State
With `color_candles = true`, the trader never needs to look at the panel to know the CR state. Green candles = squeeze. Blue = building. Amber = expanding. Red = overextended. The price chart itself communicates volatility structure.

### 7.5 Context-Sensitive NSE Flags
The script auto-detects probable circuit conditions and low-liquidity environments from price and volume data — without needing external data. Flags appear as signals on the chart AND as warning rows in the dashboard. The trader is warned automatically, not after the fact.

### 7.6 Separation of Concerns
- Overlay = price decisions (where to buy, where to stop, where to target)
- Panel = volatility structure (what the ATR is doing, where CR sits)

Each script has exactly one job. They are not redundant — they are complementary views of the same system.

### 7.7 Live Scan Mode vs Trade Mode
- `entry_px = 0` → Live scan mode. Lines follow current close. Dashboard shows live sizing. No committed trade.
- `entry_px = {price}` → Trade mode. Lines locked to entry. Dashboard shows exact trade parameters. Lines extend rightward until manually cleared.

This lets the trader run the overlay on a watchlist scan (entry_px = 0 everywhere) and switch to trade mode (set entry_px) only when a trade is taken.

---

## SECTION 8: OUT OF SCOPE (INTENTIONAL)

The following are deliberate exclusions. They belong to other tools in the system.

| Excluded Feature | Reason | Use Instead |
|---|---|---|
| Entry price auto-calculation | → Chart Whisperer | Chart Whisperer (ZLEMA25 pullback) |
| Fundamental / earnings quality | → Vikram Iyer | Vikram Iyer GARP framework |
| Sector / thematic research | → Arnav Kohli | Macro/sector context tool |
| Automated buy/sell execution | Outside Pine scope | Broker API |
| Multi-position simultaneous tracking | Complexity without value | Manual log / journal |
| Backtesting / strategy mode | Separate tool | Pine Strategy script (future spec) |
| DCF / fair value calculation | → Vikram Iyer | Fundamental framework |

---

## SECTION 9: PINE SCRIPT v5 IMPLEMENTATION NOTES

Technical notes for the developer implementing this spec.

### Script Header
```pine
//@version=5
indicator("ATR BIBLE · Overlay [Rajan Mehta]",
          overlay          = true,
          max_lines_count  = 10,
          max_labels_count = 10,
          max_boxes_count  = 5)
```

### Dashboard Table (var pattern)
```pine
// Declare once, update every bar
var table dash = table.new(
    position.top_right, 2, 12,
    bgcolor       = #0D1117,
    border_color  = #30363D,
    border_width  = 1,
    frame_color   = #58A6FF,
    frame_width   = 1
)
// Update cells each bar (not just on barstate.islast — table needs updates)
table.cell(dash, 0, 0, "ATR BIBLE · " + setup_type, ...)
```

### Persistent Lines (var + delete pattern)
```pine
var line stop_line  = na
var line entry_line = na
var line t1_line    = na
var line t2_line    = na
var line t3_line    = na

// Delete previous, draw new — on every bar
line.delete(stop_line)
stop_line := line.new(
    bar_index, stop_lvl,
    bar_index + line_extend_bars, stop_lvl,
    color   = #F85149,
    width   = 2,
    extend  = extend.right
)
// Repeat for entry_line, t1_line, t2_line, t3_line
```

### ₹ Number Formatting
Pine Script does not natively support ₹ symbol formatting. Use string concatenation:
```pine
// Format: "₹1,23,456.78" — Indian numbering requires custom formatting
fmt_inr(v) =>
    str.format("₹{0,number,#,###.##}", v)
    // Note: Indian lakh/crore formatting not natively supported in Pine
    // Use standard comma formatting — sufficient for dashboard display
```

### Edge Cases to Handle
1. `atr50 = 0` on early bars → `cr = na` → hide all CR-dependent plots/labels
2. `stop_amt <= 0` (entry below stop) → `shares = 0`, show "INVALID SETUP" in dashboard
3. `entry_px = 0` and `close = 0` → guard with `nz(close, 0) > 0` check
4. Circuit day: ATR can be near-zero → `circuit_suspect` flag suppresses ATR-based calculations
5. First bar of new session: `close[1]` may reference previous session → standard Pine behavior, no special handling needed

### Performance Notes
- `table.cell()` calls on every bar are acceptable — do NOT gate behind `barstate.islast` for the dashboard (it causes the table to disappear on historical bars)
- Lines: limit to max 10 (`max_lines_count = 10`) — 5 lines used (stop, entry, T1, T2, T3)
- Labels: limit to max 10 (`max_labels_count = 10`) — panel verdict label uses 1
- No expensive loops required — all calculations are vectorized single-bar operations

---

## SECTION 10: FUTURE EXTENSIONS (v2.0 IDEAS)

Not in scope for v1.0. Logged here for the next iteration.

| Feature | Description | Complexity |
|---|---|---|
| Multi-setup display | Show stop/target lines for ALL setups simultaneously (VCP/1PB/EP in different colors) | Medium |
| Squeeze duration counter | Count consecutive bars below cr_extreme and display in dashboard | Low |
| ATR percentile | Show where ATR(10) sits relative to its 252-bar range (0–100%) | Low |
| Delivery % integration | If available via data provider, add delivery % to dashboard | High |
| Trailing stop auto-move | Track trade phases and update stop level automatically | High |
| Strategy (backtest) version | Convert overlay logic to strategy for historical PnL | High |
| Multi-ticker scanner | Output watchlist with CR state for all tickers | Pine limitation — needs external tool |

---

*Spec v1.0 | July 2026 | For NSE Swing Trading System | Rajan Mehta Framework*
*Implementation: Pine Script v5 | TradingView*

---

*Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
