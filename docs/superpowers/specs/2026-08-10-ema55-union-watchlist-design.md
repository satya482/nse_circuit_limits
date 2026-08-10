# EMA55 Union Watchlist — Design

Date: 2026-08-10

## Purpose

Three independent scanners each already produce a TradingView-paste watchlist:
`ema25_zl_scanner.py` (RS-gated ZLEMA25 rising), `ema55_cross_scanner.py` (price
crossed above EMA55), `minervini_trend_scanner.py` (strict 9-check Trend Template
AND-gate). A stock flagged by more than one is a stronger signal than one flagged
by a single scanner. Today there is no single copy-paste list showing that overlap
— the user has to eyeball three separate files. This adds one union section, at
the top of `ema55_cross_scans.md`, sectioned by how many of the three scanners
agree on each symbol.

## Why ema55_cross_scanner.py hosts it

`run_all_scanners.ps1` runs these as sequential steps inside one orchestrator
script (not three separate Windows scheduled tasks — there is only one
`NSE_AllScanners` task). Today's order is `EMA25_ZL` (~4:25 PM) → `EMA55_Cross`
(~4:28 PM) → ... → `MinerviniTrend` (~4:30 PM). EMA55 finishes before Minervini
even starts, so it cannot embed a 3-way union today.

**Schedule change**: move the `EMA55_Cross` step in `run_all_scanners.ps1` to run
immediately after `MinerviniTrend`. New relative order: `EMA25_ZL` → (NIFTY50_ZLEMA25,
ZL_Squeeze, InsideBarScanner, WeeklyZL, RS_WeeklyEMA9, EMA_Compression, WT_BullCross,
RS_HighLine, RS_Leadership, MinerviniTrend — unchanged relative order, now run before
EMA55) → `EMA55_Cross`. These are all independent scanners with no cross-dependencies
(confirmed: nothing outside `ema55_cross_scanner.py` itself and its test file
references `ema55_cross_scans.md`), so reordering is safe. Net effect: EMA55_Cross's
own run shifts from ~15:42 to ~15:48 IST; everything currently between it and
Minervini shifts ~5 min earlier. CLAUDE.md's run-order comments and table get
updated to match.

## Union computation

`ema55_cross_scanner.py`, after computing its own `findings` list (already in
memory, no need to re-read its own output file), reads the other two scanners'
**already-written today's output**:

- `ema25_zl_scans/ema25_zl_scans.md`
- `minervini_scans/minervini_trend_latest.md`

For each, extract the symbol set from the file's existing TV-paste block (the
fenced ` ``` ` block already containing `NSE:XXXX,NSE:YYYY,...`), via regex
`NSE:([A-Z0-9&]+)`, excluding `INDEX_WATCHLIST_SYMBOLS` names
(`NIFTYSMLCAP250`, `NIFTYMIDSML400`). This avoids importing either scanner's
internal data structures — ema55 stays decoupled from their implementations,
only depends on the stable "TV block exists in the md" convention already used
by all three.

For EMA25 ZL specifically: only the **Rising** set counts (the "ZLEMA25 Rising"
section, 262 stocks in today's run), not "Watch" (2 stocks, a near-miss edge
case) — consistent with Rising being the actual signal and Watch being
informational only.

**Freshness check**: before parsing, confirm the target file's `# ... — YYYY-MM-DD`
title line matches today's date (`TODAY` constant, same convention already used
by `ema25_zl_scanner`/`minervini_trend_scanner` themselves). If a file is missing
or carries a stale date (scanner didn't run / failed upstream today), that
scanner is dropped from the union entirely for this run, and the union section
header notes which scanner(s) were excluded and why — union still renders for
whatever is available (degrades gracefully, doesn't block ema55's own scan).

## Confluence grouping

```python
def build_union(ema55_symbols: set[str], ema25_symbols: set[str], minervini_symbols: set[str]) -> dict[str, list[str]]:
    all_syms = ema55_symbols | ema25_symbols | minervini_symbols
    groups = {"ALL 3": [], "2 OF 3": [], "1 ONLY": []}
    for s in sorted(all_syms):
        n = (s in ema55_symbols) + (s in ema25_symbols) + (s in minervini_symbols)
        groups["ALL 3" if n == 3 else "2 OF 3" if n == 2 else "1 ONLY"].append(s)
    return groups
```

Empty groups are omitted from the output (e.g. if nothing hits all 3 today, no
`###ALL 3` section is emitted — same "no empty section" pattern the repo already
uses elsewhere, but here it's per-section-omission, not whole-file).

## Output format

New section inserted at the very top of `ema55_cross_scans.md`, right under the
title/generated line, above `### Scan definition`. Reuses `tv_watchlist.tv_csv_flat`
+ `tv_top_sections` exactly as the existing per-scanner blocks do, so the paste
format is identical to what a TradingView user already expects from this repo:

```
# NSE EMA55 Cross Watchlist — 2026-08-10
*Generated 2026-08-10 15:48 IST*

### Union Watchlist — EMA25 ZL + EMA55 Cross + Minervini Trend Template
*(sectioned by confluence — how many of the 3 scanners flagged the symbol today)*

**All 3: 4** &nbsp;|&nbsp; **2 of 3: 31** &nbsp;|&nbsp; **1 only: 340**

```
###INDICES,NSE:NIFTYSMLCAP250,...,###COMMODITIES,MCX:GOLDM1!,...,###ALL 3,NSE:NIFTYSMLCAP250,...,NSE:FOO,NSE:BAR,###2 OF 3,...,###1 ONLY,...
```

---

### Scan definition
...
```

(exact counts illustrative — real numbers come from the day's run)

If any source scanner was excluded for staleness/missing data, a one-line note
replaces the subtitle, e.g.:
`*(Minervini data unavailable for today's union - showing EMA25 ZL + EMA55 Cross only)*`

## Files touched

| File | Change |
|------|--------|
| `run_all_scanners.ps1` | Move `Run-Scanner "EMA55_Cross" ...` line to after `Run-Scanner "MinerviniTrend" ...` |
| `ema55_cross_scanner.py` | Add union-building functions + call from `main()`/`build_markdown()`; prepend union section to output |
| `CLAUDE.md` | Update run-order comments/table for the swapped EMA55/Minervini position; document the new union section under ema55_cross_scanner's pipeline description |

No changes to `ema25_zl_scanner.py` or `minervini_trend_scanner.py` — they are
read-only inputs to this feature.

## Testing

`tests/test_ema55_cross_scanner.py` already exists — add cases for:
- `build_union()` pure-function grouping logic (3 fixed sets, assert group membership)
- Freshness check: mock a stale-dated md file, assert scanner dropped + note appears
- Empty-group omission (no symbols in all 3 → no `###ALL 3` section emitted)

No live OHLC/network dependency needed for these — same pattern as the repo's
other pure-function unit tests (parsing/grouping logic tested directly, scanning
logic tested via `analyse()` fixtures elsewhere in the same test file).
