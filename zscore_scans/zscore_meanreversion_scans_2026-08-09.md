> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# NSE Z-Score Mean Reversion Scanner (SD3-) - 2026-08-09
*Generated 2026-08-09 11:19 IST*

### Scan definition
| Filter | Value |
|--------|-------|
| Exchange | NSE common equity |
| Price | > Rs 50 |
| Market cap | Rs 1,000 Cr - Rs 5 Lakh Cr |
| Signal | Close is 3+ standard deviations below its 55-bar mean (z = (close - SMA55) / STDEV55) |
| Direction | Oversold only (long / bounce candidates) |
| Zone Age | Consecutive bars continuously at z <= -3 (capped 60d) |
| Turning Up | z rose for the last 3 bars - early reversion tell |
| Float gate | AVOID dropped from scan - SAFE / CAUTION shown under symbol (float_gate.py) |
| Symbol tags | trap - liq (avg10Cr - todayCr) - CMF - DEL% |

---

**Oversold candidates: 3**

### SD3- Oversold Candidates
| Symbol | Z-Score | Zone Age | Turning Up | Close | SMA55 | Dist% | Day Chg | Circuit |
|--------|--------:|---------:|:----------:|------:|------:|------:|--------:|:-------:|
| [POWERGRID](https://in.tradingview.com/chart/?symbol=NSE:POWERGRID)<br><sub>⚠ CAUTION - →264Cr · 480Cr - ↑CMF9d</sub> | -3.23 | 1d |  | 270.90 | 287.00 | -5.6% | -3.85% | 20%  |
| [LICHSGFIN](https://in.tradingview.com/chart/?symbol=NSE:LICHSGFIN)<br><sub>⚠ CAUTION - ↗87Cr · 81Cr - ↓CMF9d</sub> | -3.02 | 6d |  | 504.25 | 543.48 | -7.2% | -0.15% | 20%  |
| [RATNAMANI](https://in.tradingview.com/chart/?symbol=NSE:RATNAMANI)<br><sub>⚠ CAUTION - ↗13Cr · 73Cr - ↓CMF30d</sub> | -3.02 | 1d |  | 2197.60 | 2543.69 | -13.6% | -7.30% | 20%  |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:POWERGRID,NSE:LICHSGFIN,NSE:RATNAMANI
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
