# CMF Zero-Cross Symbol Marker — Design Spec
**Date:** 2026-07-04

## Overview

Chaikin Money Flow (CMF) zero-line cross marker, added to the Symbol column of every scanner that currently computes `liq_tag()`. Shows accumulation/distribution state as a compact recency tag (`↑CMF3d` / `↓CMF7d`), same style as existing `zl_cell` (`↑6d`) pattern.

Companion Pine v6 indicator added for manual chart use, same zero-cross logic (Python↔Pine parity).

---

## CMF Formula

```
range_        = high - low
MFM           = ((close - low) - (high - close)) / range_   [0 if range_ == 0 — no div-by-zero]
MFV           = MFM * volume
CMF(n)        = sum(MFV, n) / sum(volume, n)                 [n = 20]
```

---

## New Functions — `ohlc_db.py`

Placed next to `liq_tag()` (same file, same convention: try/except → `""` on failure).

```python
def cmf_days(df: pd.DataFrame, n: int = 20, cap: int = 30) -> tuple[bool, int] | None:
    """
    Returns (cmf_positive, bars_since_zero_cross), capped at `cap`.
    None if insufficient data (< n + 2 bars).
    Mirrors zl25_stats() bars-ago scan pattern — no float equality,
    manual > / <= comparison (CMF crossing exactly 0.0 is a valid boundary,
    not a case needing math.abs tolerance).
    """

def cmf_tag(df: pd.DataFrame, n: int = 20, cap: int = 30) -> str:
    """Formats cmf_days() → '↑CMF{d}d' / '↓CMF{d}d' / '' on None or error."""
```

**Algorithm (`cmf_days`):**
1. Compute CMF series per formula above.
2. `cmf_positive = cmf.iloc[-1] > 0`
3. Scan backward from last bar for most recent sign change (`cmf.iloc[i] > 0 and cmf.iloc[i-1] <= 0` or inverse `<` / `>=`).
4. `bars_ago = (n_bars - 1) - i`, capped at `cap`.
5. No cross found within cap → return `(cmf_positive, cap)`.

---

## Wiring — Symbol Cell, 5 Files

| File | Current Symbol cell | Change |
|------|---------------------|--------|
| `wt_bullcross_scanner.py` | `extras` list subline (`📶W9` · `W↑Nd` · `🚀SS` · `★`) | Append `cmf_tag(df_raw)` to `extras` |
| `ema25_zl_scanner.py` | flat `[{sym}](tv)` | Add `<br><sub>{cmf}</sub>` subline |
| `weekly_zl_scanner.py` | flat `[{sym}](tv)` | Add `<br><sub>{cmf}</sub>` subline |
| `trend_scanner.py` | flat `[{sym}](tv)` | Add `<br><sub>{cmf}</sub>` subline |
| `rs_highline_scanner.py` | flat `[{sym}](tv) [{circuit_cell}]` | Add `<br><sub>{cmf}</sub>` subline |

`liq_tag()` stays as-is in all 5 (computed, mostly unused inline — out of scope per user decision, no fix bundled).

Each file already computes/has access to the same raw OHLC `df` used for `liq_tag()` — reuse it, no extra `load_ohlc` call.

---

## Pine v6 — `pine_scripts/CMF_ZeroCross.pine`

- `@version=6`, standalone oscillator pane (not overlay)
- Header comment: what it does, no companion overlay, alert format
- `ta.crossover(cmfLine, 0.0)` / `ta.crossunder(cmfLine, 0.0)` — no float equality
- Label at last bar: days since cross (mirrors `cmf_days` bars-ago, manual counting loop from most recent crossover/crossunder `bool` series)
- Alert message: `CMF_ZERO_CROSS|{{ticker}}|bull|TF:{{interval}}` (bull) / `...|bear|...` (bear)

---

## Error Handling

- `high == low` bar (circuit-frozen / illiquid) → MFM = 0, no crash.
- `< n+2` bars total → `cmf_days` returns `None` → `cmf_tag` returns `""` → Symbol cell renders with no CMF subline (or existing extras unaffected in wt_bullcross case).
- Same silent-fail contract as `liq_tag()` — a missing marker is not an error state for the scanner run.

---

## Test — `tests/test_cmf.py`

Pytest, matches repo convention (see `tests/test_weekly_wt_zone.py` for style).

- Synthetic OHLCV series with known engineered zero-cross at a specific bar → assert `cmf_days` bars-ago count and sign.
- All-`high==low` bars (zero range) → assert no exception, `cmf_positive` well-defined (no NaN propagation).
- `< n+2` bars → assert `cmf_days` returns `None`, `cmf_tag` returns `""`.

---

## Files Touched

| File | Change |
|------|--------|
| `ohlc_db.py` | Add `cmf_days()`, `cmf_tag()` |
| `wt_bullcross_scanner.py` | Import `cmf_tag`, append to `extras` |
| `ema25_zl_scanner.py` | Import `cmf_tag`, add subline |
| `weekly_zl_scanner.py` | Import `cmf_tag`, add subline |
| `trend_scanner.py` | Import `cmf_tag`, add subline |
| `rs_highline_scanner.py` | Import `cmf_tag`, add subline |
| `pine_scripts/CMF_ZeroCross.pine` | New file |
| `tests/test_cmf.py` | New file |

No schedule/PS1/CLAUDE.md changes — this is a column addition to existing scanners, not a new scanner.
