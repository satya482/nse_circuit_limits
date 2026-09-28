> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-09-28
*Generated 2026-09-28 15:46 IST*

### Scan definition
| Filter | Value |
|--------|-------|
| Exchange | NSE common equity |
| Price | > ₹50 |
| Market cap | ₹1,000 Cr – ₹5 Lakh Cr |
| Label | Description from stock_labels.json |
| RS filter | None — WT captures pre-RS-turn reversals |
| RS | 🔄/↑/↓ state + IBD percentile vs NIFTY MIDSML 400 — e.g. 🔄82 |
| C/AvgC | Close / EMA(10) ratio — ↑ rising momentum |
| Erly | Squeeze(40)+RS-transition(30)+ZL freshness(0-20)+C/AvgC freshness(0-10) |
| ZL | ZLEMA25 direction + days since turn — e.g. ↑6d |
| Flags | SQ=squeeze  PV=pocket-pivot  SQ·PV=both  —=neither |
| WT | WT1/WT2 oscillator values |
| Sort | Weekly RS gate (📶W9) first → Rank desc → Erly desc |
| Min rank | Any bull cross (rank ≥ 1) |
| W↑Nd in Symbol | Days in weekly WT bull-cross zone (any cross; ends on weekly bear cross) |
| ⚠️TRAP in Symbol | RS falling AND price below EMA50 on the cross bar — structural context broken, treat as suspect |
| 🔥PHX in Symbol | Deep oversold (wt2 < -65) V-bottom cross — fast reversal, not a flat base |
| 🎯SLING in Symbol | Oversold cross off a flat multi-bar base (extended base breakout) |
| ÷DIV in Symbol | Bullish divergence — today's price low undercuts the prior 10-bar OS trough while wt2 makes a higher low |
| RS-Confirmed table | Separate table below, rs_state ≠ weak — informational only, all signals still listed in category tables |
| 📶W9 in Symbol | Daily RS > Weekly RS EMA9 AND Weekly RS EMA9 rising (same gate as ema25_zl_scanner RS_MODE=weekly_ema9) — highest sort priority in every table |

---

**Total bull crosses today: 23** · 7 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GLAXO,NSE:STYLEBAAZA,NSE:INDOBORAX,NSE:RSYSTEMS,NSE:JINDRILL,NSE:SIGMAADV,NSE:MRPL,NSE:MEESHO,NSE:INDIQUBE,NSE:NITTAGELA,NSE:NILKAMAL,NSE:GRASIM,NSE:GNRL,NSE:WHEELS,NSE:SGMART,NSE:TATAELXSI,NSE:ZFCVINDIA,NSE:VINATIORGA,NSE:ZENSARTECH,NSE:TVSHLTD,NSE:LINDEINDIA,NSE:SYMPHONY,NSE:CAMPUS
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (15)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GLAXO](https://in.tradingview.com/chart/?symbol=NSE:GLAXO)<br><sub>📶W9 · ↓CMF8d</sub> | ⚠ CAUTION | Prescription drugs vaccines respiratory gastro oncology pharma | ⚡ BULL_ANY_PPV | 99 | 🔄70 | ↑1.013 | ↑1d | SQ·PV | +2.9% | -9.39/-11.62 | +2.87% | 20% |
| [STYLEBAAZA](https://in.tradingview.com/chart/?symbol=NSE:STYLEBAAZA)<br><sub>📶W9 · W↑36d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Value fashion apparel retailer eastern India families | ⚡ BULL_ANY_PPV | 94 | 🔄80 | ↑1.029 | ↑1d | SQ·PV | +5.0% | -22.36/-26.32 | +4.98% | 5% |
| [INDOBORAX](https://in.tradingview.com/chart/?symbol=NSE:INDOBORAX)<br><sub>📶W9 · RVOL58x · ↑CMF0d</sub> | ✓ SAFE | Boron lithium chemicals manufacturer serving industrial pharmaceutical sectors | ⚡ BULL_ANY_PPV | 54 | 🔄93 | ↑1.021 | ↑1d | PV | +6.1% | -22.41/-22.7 | +6.13% | 20% |
| [RSYSTEMS](https://in.tradingview.com/chart/?symbol=NSE:RSYSTEMS)<br><sub>📶W9 · W↑1d · 🚀SS·368x · ↑CMF0d</sub> | ✓ SAFE | Digital product engineering AI solutions for enterprises | ⚡ BULL_ANY_PPV | 49 | 🔄41 | ↑1.116 | ↑1d | PV | +16.8% | -12.05/-24.26 | +16.80% | 20% |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>📶W9 · RVOL15x · ↑CMF0d</sub> | ✓ SAFE | Offshore jack-up drilling rigs for oil gas exploration | ⚡ BULL_ANY_PPV | 49 | 🔄66 | ↑1.031 | ↑1d | PV | +5.4% | -15.77/-18.85 | +5.40% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [MRPL](https://in.tradingview.com/chart/?symbol=NSE:MRPL)<br><sub>📶W9 · ↓CMF29d</sub> | ✓ SAFE | Crude oil refining, petrochemicals, fuel production for domestic markets | 📈 BULL_ANY_MID | 59 | 🔄68 | ↑1.014 | ↑1d | — | +3.2% | -20.88/-21.69 | +3.16% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · W↑30d · ↑CMF30d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.025 | ↑2d | SQ | +6.1% | 49.69/48.04 | -0.06% | 20% 🟦 |
| [INDIQUBE](https://in.tradingview.com/chart/?symbol=NSE:INDIQUBE)<br><sub>📶W9 · W↑76d · ↑CMF15d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑66 | ↓1.016 | ↑2d | SQ | +2.8% | 10.52/7.54 | +0.25% | 20% |
| [NITTAGELA](https://in.tradingview.com/chart/?symbol=NSE:NITTAGELA)<br><sub>📶W9 · ↑CMF8d</sub> | ⚠ CAUTION | Gelatin and collagen peptides for pharma food supplements | 📈 BULL_ANY_MID | 54 | ↑50 | ↑1.009 | ↑16d | SQ | +7.2% | 37.1/36.72 | +0.41% | 20% |
| [NILKAMAL](https://in.tradingview.com/chart/?symbol=NSE:NILKAMAL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Plastic furniture and material handling solutions for residential commercial sectors | 📈 BULL_ANY_MID | 35 | 🔄88 | ↑0.999 | ↓60d+ | — | +48.1% | -29.99/-30.38 | +1.80% | 20% |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 14 | ↑61 | ↑0.998 | ↓11d | — | -3.2% | -35.97/-36.7 | +0.74% | 20% |
| [GNRL](https://in.tradingview.com/chart/?symbol=NSE:GNRL)<br><sub>📶W9 · ↑CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Oil gas exploration trading natural resources sector | 📈 BULL_ANY_MID | 4 | ↑50 | ↓0.985 | ↓16d | — | -1.0% | -10.8/-18.38 | -1.78% | 20% 🟦 |
| [WHEELS](https://in.tradingview.com/chart/?symbol=NSE:WHEELS)<br><sub>📶W9 · W↑26d · ↑CMF22d</sub> | ✓ SAFE | Steel aluminum wheels automotive commercial tractors mining | 📈 BULL_ANY_MID | 0 | ↑98 | ↓1.056 | ↑32d | — | +71.7% | 59.44/58.98 | +1.19% | 20% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>📶W9 · ↓CMF13d</sub> | ✓ SAFE | Building materials B2B marketplace connecting manufacturers suppliers traders | 📈 BULL_ANY_MID | 0 | ↑91 | ↓0.995 | ↓60d+ | — | +21.0% | -28.48/-29.72 | -0.21% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GLAXO,NSE:STYLEBAAZA,NSE:INDOBORAX,NSE:RSYSTEMS,NSE:JINDRILL,NSE:SIGMAADV,NSE:MRPL,NSE:MEESHO,NSE:INDIQUBE,NSE:NITTAGELA,NSE:NILKAMAL,NSE:GRASIM,NSE:GNRL,NSE:WHEELS,NSE:SGMART
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (21)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GLAXO](https://in.tradingview.com/chart/?symbol=NSE:GLAXO)<br><sub>📶W9 · ↓CMF8d</sub> | ⚠ CAUTION | Prescription drugs vaccines respiratory gastro oncology pharma | ⚡ BULL_ANY_PPV | 99 | 🔄70 | ↑1.013 | ↑1d | SQ·PV | +2.9% | -9.39/-11.62 | +2.87% | 20% |
| [STYLEBAAZA](https://in.tradingview.com/chart/?symbol=NSE:STYLEBAAZA)<br><sub>📶W9 · W↑36d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Value fashion apparel retailer eastern India families | ⚡ BULL_ANY_PPV | 94 | 🔄80 | ↑1.029 | ↑1d | SQ·PV | +5.0% | -22.36/-26.32 | +4.98% | 5% |
| [INDOBORAX](https://in.tradingview.com/chart/?symbol=NSE:INDOBORAX)<br><sub>📶W9 · RVOL58x · ↑CMF0d</sub> | ✓ SAFE | Boron lithium chemicals manufacturer serving industrial pharmaceutical sectors | ⚡ BULL_ANY_PPV | 54 | 🔄93 | ↑1.021 | ↑1d | PV | +6.1% | -22.41/-22.7 | +6.13% | 20% |
| [RSYSTEMS](https://in.tradingview.com/chart/?symbol=NSE:RSYSTEMS)<br><sub>📶W9 · W↑1d · 🚀SS·368x · ↑CMF0d</sub> | ✓ SAFE | Digital product engineering AI solutions for enterprises | ⚡ BULL_ANY_PPV | 49 | 🔄41 | ↑1.116 | ↑1d | PV | +16.8% | -12.05/-24.26 | +16.80% | 20% |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>📶W9 · RVOL15x · ↑CMF0d</sub> | ✓ SAFE | Offshore jack-up drilling rigs for oil gas exploration | ⚡ BULL_ANY_PPV | 49 | 🔄66 | ↑1.031 | ↑1d | PV | +5.4% | -15.77/-18.85 | +5.40% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [MRPL](https://in.tradingview.com/chart/?symbol=NSE:MRPL)<br><sub>📶W9 · ↓CMF29d</sub> | ✓ SAFE | Crude oil refining, petrochemicals, fuel production for domestic markets | 📈 BULL_ANY_MID | 59 | 🔄68 | ↑1.014 | ↑1d | — | +3.2% | -20.88/-21.69 | +3.16% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · W↑30d · ↑CMF30d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.025 | ↑2d | SQ | +6.1% | 49.69/48.04 | -0.06% | 20% 🟦 |
| [INDIQUBE](https://in.tradingview.com/chart/?symbol=NSE:INDIQUBE)<br><sub>📶W9 · W↑76d · ↑CMF15d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑66 | ↓1.016 | ↑2d | SQ | +2.8% | 10.52/7.54 | +0.25% | 20% |
| [NITTAGELA](https://in.tradingview.com/chart/?symbol=NSE:NITTAGELA)<br><sub>📶W9 · ↑CMF8d</sub> | ⚠ CAUTION | Gelatin and collagen peptides for pharma food supplements | 📈 BULL_ANY_MID | 54 | ↑50 | ↑1.009 | ↑16d | SQ | +7.2% | 37.1/36.72 | +0.41% | 20% |
| [NILKAMAL](https://in.tradingview.com/chart/?symbol=NSE:NILKAMAL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Plastic furniture and material handling solutions for residential commercial sectors | 📈 BULL_ANY_MID | 35 | 🔄88 | ↑0.999 | ↓60d+ | — | +48.1% | -29.99/-30.38 | +1.80% | 20% |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 14 | ↑61 | ↑0.998 | ↓11d | — | -3.2% | -35.97/-36.7 | +0.74% | 20% |
| [GNRL](https://in.tradingview.com/chart/?symbol=NSE:GNRL)<br><sub>📶W9 · ↑CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Oil gas exploration trading natural resources sector | 📈 BULL_ANY_MID | 4 | ↑50 | ↓0.985 | ↓16d | — | -1.0% | -10.8/-18.38 | -1.78% | 20% 🟦 |
| [WHEELS](https://in.tradingview.com/chart/?symbol=NSE:WHEELS)<br><sub>📶W9 · W↑26d · ↑CMF22d</sub> | ✓ SAFE | Steel aluminum wheels automotive commercial tractors mining | 📈 BULL_ANY_MID | 0 | ↑98 | ↓1.056 | ↑32d | — | +71.7% | 59.44/58.98 | +1.19% | 20% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>📶W9 · ↓CMF13d</sub> | ✓ SAFE | Building materials B2B marketplace connecting manufacturers suppliers traders | 📈 BULL_ANY_MID | 0 | ↑91 | ↓0.995 | ↓60d+ | — | +21.0% | -28.48/-29.72 | -0.21% | 20% |
| [TATAELXSI](https://in.tradingview.com/chart/?symbol=NSE:TATAELXSI)<br><sub>↓CMF26d · 🎯SLING</sub> | ✓ SAFE | Design engineering services for automotive media healthcare | 🟢 BULL_OVERSOLD | 35 | 🔄4 | ↑0.977 | ↓22d | — | -12.2% | -69.97/-70.81 | +0.13% | 20% |
| [ZENSARTECH](https://in.tradingview.com/chart/?symbol=NSE:ZENSARTECH)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Digital solutions and IT services for global enterprises | 🟡 BULL_OS_L2 | 10 | ↑6 | ↑1.003 | ↓41d | — | -14.0% | -48.1/-54.07 | +0.41% | 20% |
| [TVSHLTD](https://in.tradingview.com/chart/?symbol=NSE:TVSHLTD)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Aluminum die castings automotive components manufacturing India | 🟡 BULL_OS_L2 | 4 | ↑29 | ↓0.981 | ↓16d | — | -7.0% | -55.97/-56.57 | -1.31% | 20% |
| [LINDEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LINDEINDIA)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Industrial medical gases cryogenic plants manufacturing India | 📈 BULL_ANY_MID | 89 | 🔄34 | ↑0.995 | ↓6d | SQ | -0.8% | -34.3/-35.01 | +0.79% | 20% |
| [SYMPHONY](https://in.tradingview.com/chart/?symbol=NSE:SYMPHONY)<br><sub>W↑11d · ↓CMF30d</sub> | ✓ SAFE | Evaporative air coolers for residential commercial industrial markets | 📈 BULL_ANY_MID | 58 | ↑6 | ↓0.996 | ↓2d | SQ | +1.6% | -18.33/-22.65 | -0.48% | 20% |
| [CAMPUS](https://in.tradingview.com/chart/?symbol=NSE:CAMPUS)<br><sub>↑CMF2d</sub> | ✓ SAFE | Sports athleisure footwear manufacturing distribution retail | 📈 BULL_ANY_MID | 37 | 🔄23 | ↑0.996 | ↓18d | — | -4.5% | -51.1/-51.48 | +0.50% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GLAXO,NSE:STYLEBAAZA,NSE:INDOBORAX,NSE:RSYSTEMS,NSE:JINDRILL,NSE:SIGMAADV,NSE:MRPL,NSE:MEESHO,NSE:INDIQUBE,NSE:NITTAGELA,NSE:NILKAMAL,NSE:GRASIM,NSE:GNRL,NSE:WHEELS,NSE:SGMART,NSE:TATAELXSI,NSE:ZENSARTECH,NSE:TVSHLTD,NSE:LINDEINDIA,NSE:SYMPHONY,NSE:CAMPUS
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (7)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GLAXO](https://in.tradingview.com/chart/?symbol=NSE:GLAXO)<br><sub>📶W9 · ↓CMF8d</sub> | ⚠ CAUTION | Prescription drugs vaccines respiratory gastro oncology pharma | ⚡ BULL_ANY_PPV | 99 | 🔄70 | ↑1.013 | ↑1d | SQ·PV | +2.9% | -9.39/-11.62 | +2.87% | 20% |
| [STYLEBAAZA](https://in.tradingview.com/chart/?symbol=NSE:STYLEBAAZA)<br><sub>📶W9 · W↑36d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Value fashion apparel retailer eastern India families | ⚡ BULL_ANY_PPV | 94 | 🔄80 | ↑1.029 | ↑1d | SQ·PV | +5.0% | -22.36/-26.32 | +4.98% | 5% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · W↑30d · ↑CMF30d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.025 | ↑2d | SQ | +6.1% | 49.69/48.04 | -0.06% | 20% 🟦 |
| [INDIQUBE](https://in.tradingview.com/chart/?symbol=NSE:INDIQUBE)<br><sub>📶W9 · W↑76d · ↑CMF15d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑66 | ↓1.016 | ↑2d | SQ | +2.8% | 10.52/7.54 | +0.25% | 20% |
| [NITTAGELA](https://in.tradingview.com/chart/?symbol=NSE:NITTAGELA)<br><sub>📶W9 · ↑CMF8d</sub> | ⚠ CAUTION | Gelatin and collagen peptides for pharma food supplements | 📈 BULL_ANY_MID | 54 | ↑50 | ↑1.009 | ↑16d | SQ | +7.2% | 37.1/36.72 | +0.41% | 20% |
| [LINDEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LINDEINDIA)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Industrial medical gases cryogenic plants manufacturing India | 📈 BULL_ANY_MID | 89 | 🔄34 | ↑0.995 | ↓6d | SQ | -0.8% | -34.3/-35.01 | +0.79% | 20% |
| [SYMPHONY](https://in.tradingview.com/chart/?symbol=NSE:SYMPHONY)<br><sub>W↑11d · ↓CMF30d</sub> | ✓ SAFE | Evaporative air coolers for residential commercial industrial markets | 📈 BULL_ANY_MID | 58 | ↑6 | ↓0.996 | ↓2d | SQ | +1.6% | -18.33/-22.65 | -0.48% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GLAXO,NSE:STYLEBAAZA,NSE:MEESHO,NSE:INDIQUBE,NSE:NITTAGELA,NSE:LINDEINDIA,NSE:SYMPHONY
```

---

### 🔥 MAJOR — PPV confirmed (4)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [INDOBORAX](https://in.tradingview.com/chart/?symbol=NSE:INDOBORAX)<br><sub>📶W9 · RVOL58x · ↑CMF0d</sub> | ✓ SAFE | Boron lithium chemicals manufacturer serving industrial pharmaceutical sectors | ⚡ BULL_ANY_PPV | 54 | 🔄93 | ↑1.021 | ↑1d | PV | +6.1% | -22.41/-22.7 | +6.13% | 20% |
| [RSYSTEMS](https://in.tradingview.com/chart/?symbol=NSE:RSYSTEMS)<br><sub>📶W9 · W↑1d · 🚀SS·368x · ↑CMF0d</sub> | ✓ SAFE | Digital product engineering AI solutions for enterprises | ⚡ BULL_ANY_PPV | 49 | 🔄41 | ↑1.116 | ↑1d | PV | +16.8% | -12.05/-24.26 | +16.80% | 20% |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>📶W9 · RVOL15x · ↑CMF0d</sub> | ✓ SAFE | Offshore jack-up drilling rigs for oil gas exploration | ⚡ BULL_ANY_PPV | 49 | 🔄66 | ↑1.031 | ↑1d | PV | +5.4% | -15.77/-18.85 | +5.40% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:INDOBORAX,NSE:RSYSTEMS,NSE:JINDRILL,NSE:SIGMAADV
```

### 🟢 OVERSOLD — reversal from −53/−60 (5)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [TATAELXSI](https://in.tradingview.com/chart/?symbol=NSE:TATAELXSI)<br><sub>↓CMF26d · 🎯SLING</sub> | ✓ SAFE | Design engineering services for automotive media healthcare | 🟢 BULL_OVERSOLD | 35 | 🔄4 | ↑0.977 | ↓22d | — | -12.2% | -69.97/-70.81 | +0.13% | 20% |
| [ZFCVINDIA](https://in.tradingview.com/chart/?symbol=NSE:ZFCVINDIA)<br><sub>W↑26d · ↑CMF3d · 🎯SLING</sub> | ⚠ CAUTION | Braking systems control tech commercial vehicles India | 🟢 BULL_OVERSOLD | 18 | ↓1 | ↓0.976 | ↓2d | — | -0.5% | -64.63/-65.18 | -0.91% | 20% |
| [VINATIORGA](https://in.tradingview.com/chart/?symbol=NSE:VINATIORGA)<br><sub>↓CMF13d · 🎯SLING</sub> | ⚠ CAUTION | Specialty chemicals, monomers, antioxidants, polymers manufacturer | 🟢 BULL_OVERSOLD | 5 | ↓16 | ↓0.972 | ↓15d | — | -8.3% | -67.42/-67.56 | -1.28% | 20% |
| [ZENSARTECH](https://in.tradingview.com/chart/?symbol=NSE:ZENSARTECH)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Digital solutions and IT services for global enterprises | 🟡 BULL_OS_L2 | 10 | ↑6 | ↑1.003 | ↓41d | — | -14.0% | -48.1/-54.07 | +0.41% | 20% |
| [TVSHLTD](https://in.tradingview.com/chart/?symbol=NSE:TVSHLTD)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Aluminum die castings automotive components manufacturing India | 🟡 BULL_OS_L2 | 4 | ↑29 | ↓0.981 | ↓16d | — | -7.0% | -55.97/-56.57 | -1.31% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:TATAELXSI,NSE:ZFCVINDIA,NSE:VINATIORGA,NSE:ZENSARTECH,NSE:TVSHLTD
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (7)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MRPL](https://in.tradingview.com/chart/?symbol=NSE:MRPL)<br><sub>📶W9 · ↓CMF29d</sub> | ✓ SAFE | Crude oil refining, petrochemicals, fuel production for domestic markets | 📈 BULL_ANY_MID | 59 | 🔄68 | ↑1.014 | ↑1d | — | +3.2% | -20.88/-21.69 | +3.16% | 20% |
| [NILKAMAL](https://in.tradingview.com/chart/?symbol=NSE:NILKAMAL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Plastic furniture and material handling solutions for residential commercial sectors | 📈 BULL_ANY_MID | 35 | 🔄88 | ↑0.999 | ↓60d+ | — | +48.1% | -29.99/-30.38 | +1.80% | 20% |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 14 | ↑61 | ↑0.998 | ↓11d | — | -3.2% | -35.97/-36.7 | +0.74% | 20% |
| [GNRL](https://in.tradingview.com/chart/?symbol=NSE:GNRL)<br><sub>📶W9 · ↑CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Oil gas exploration trading natural resources sector | 📈 BULL_ANY_MID | 4 | ↑50 | ↓0.985 | ↓16d | — | -1.0% | -10.8/-18.38 | -1.78% | 20% 🟦 |
| [WHEELS](https://in.tradingview.com/chart/?symbol=NSE:WHEELS)<br><sub>📶W9 · W↑26d · ↑CMF22d</sub> | ✓ SAFE | Steel aluminum wheels automotive commercial tractors mining | 📈 BULL_ANY_MID | 0 | ↑98 | ↓1.056 | ↑32d | — | +71.7% | 59.44/58.98 | +1.19% | 20% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>📶W9 · ↓CMF13d</sub> | ✓ SAFE | Building materials B2B marketplace connecting manufacturers suppliers traders | 📈 BULL_ANY_MID | 0 | ↑91 | ↓0.995 | ↓60d+ | — | +21.0% | -28.48/-29.72 | -0.21% | 20% |
| [CAMPUS](https://in.tradingview.com/chart/?symbol=NSE:CAMPUS)<br><sub>↑CMF2d</sub> | ✓ SAFE | Sports athleisure footwear manufacturing distribution retail | 📈 BULL_ANY_MID | 37 | 🔄23 | ↑0.996 | ↓18d | — | -4.5% | -51.1/-51.48 | +0.50% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MRPL,NSE:NILKAMAL,NSE:GRASIM,NSE:GNRL,NSE:WHEELS,NSE:SGMART,NSE:CAMPUS
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
