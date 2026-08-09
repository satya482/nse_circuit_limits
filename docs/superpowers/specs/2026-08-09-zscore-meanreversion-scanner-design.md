# Z-Score Mean Reversion Scanner — Design

## Purpose
Flag oversold candidates (long/bounce setups) that are 3+ standard deviations below their
mean close — same math as `pine_scripts/Satya Z-Score Probability Indicator.txt`, ported to
the daily scanner pipeline for candidate discovery.

## Scope
Oversold only (z <= -3). Overbought/short candidates out of scope for this scanner.

## Formula (Python <-> Pine parity)
Mirrors the Pine indicator's Z-Score calc, lookback changed from Pine default 75 to 55:

```
sma55 = close.rolling(55, min_periods=55).mean()
sd55  = close.rolling(55, min_periods=55).std()
z     = (close - sma55) / sd55
```

Pine equivalent: `z = (close - ta.sma(close, 55)) / ta.stdev(close, 55)`.

## Universe
Reuse `ema25_zl_scanner.get_watchlist()` — same broad NSE common-equity list (MCap
1,000 Cr - 5 Lakh Cr, price > 50) and float hard-gate used by `ema55_cross_scanner.py`.
No new TradingView query.

## Gate
`Z_THRESHOLD = -3.0` (module-level const, tunable). Keep symbol if `z.iloc[-1] <= Z_THRESHOLD`.

## Per-candidate fields
- `z` — current z-score
- `close`, `sma55`
- `dist_pct` — % distance from close to sma55 (the mean-reversion target)
- `day_chg` — % change vs previous close
- `turning_up` — bool, z rising for the last 3 bars (`ta.rising(z, 3)` equivalent) — early
  reversion tell, mirrors the Pine indicator's `rising = ta.rising(z_sma, 3)`
- `zone_days` — bars continuously at z <= -3 (backward scan, capped 60, same pattern as
  `ema55_cross_scanner.ema55_cross_stats`)
- Standard tags: `trap` (float_gate), `liq_tag`, `cmf_tag`, `deliv_tag` (all from `ohlc_db.py`
  / `float_gate.py`, same as every other scanner)

## Sort & output
Sort by `z` ascending (most extreme first). Table columns: Symbol | Z-Score | Zone Age |
Close | SMA55 | Dist% | Day Chg | Turning Up | Circuit.

Files: `zscore_scans/zscore_meanreversion_scans.md` (undated, always overwritten) +
`zscore_scans/zscore_meanreversion_scans_YYYY-MM-DD.md` (dated), matching
`ema55_cross_scanner.py`'s two-file pattern. Both include SEBI header/footer via
`disclaimer.py`.

## Not included
- No PS1 runner / scheduling — user hasn't asked to wire this into the daily pipeline yet.
- No overbought/short side.
- No dashboard integration.

## Minimum viable test
`min periods=55` warmup guard (skip symbol if `len(raw) < 55`, mirrors other scanners'
lookback-ratio guards) plus one `__main__`/assert-based self-check on `zscore()` /
`zone_days()` against a hand-built series with a known z-score and a known zone length.
