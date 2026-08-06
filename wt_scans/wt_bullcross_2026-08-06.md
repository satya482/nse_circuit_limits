> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-08-06
*Generated 2026-08-06 15:44 IST*

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

**Total bull crosses today: 64** · 40 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,###WATCHLIST,NSE:BIOCON,NSE:STOVEKRAFT,NSE:DCBBANK,NSE:ROTO,NSE:AARTIIND,NSE:TTKHLTCARE,NSE:PANAMAPET,NSE:RAMRAT,NSE:CRISIL,NSE:DIVISLAB,NSE:INOXINDIA,NSE:CAPLIPOINT,NSE:SMARTWORKS,NSE:ASIANHOTNR,NSE:INDIQUBE,NSE:GHCLTEXTIL,NSE:INDIGOPNTS,NSE:HLEGLAS,NSE:SHRIRAMFIN,NSE:SANGAMIND,NSE:DLF,NSE:GCSL,NSE:JSWSTEEL,NSE:FUSION,NSE:APOLLOHOSP,NSE:BRITANNIA,NSE:OFSS,NSE:RELTD,NSE:SETL,NSE:STYL,NSE:PARADEEP,NSE:DIXON,NSE:ULTRACEMCO,NSE:LTTS,NSE:AURUM,NSE:EMAMILTD,NSE:SAMMAANCAP,NSE:BLKASHYAP,NSE:PASHUPATI,NSE:REPCOHOME,NSE:TATASTEEL,NSE:VTL,NSE:AXISBANK,NSE:HINDALCO,NSE:POWERINDIA,NSE:AMBUJACEM,NSE:DHANUKA,NSE:KIMS,NSE:POWERMECH,NSE:BALMLAWRIE,NSE:MUTHOOTFIN,NSE:GPTINFRA,NSE:KOVAI,NSE:TCI,NSE:PREMEXPLN,NSE:DBCORP,NSE:NTPCGREEN,NSE:JINDALPOLY,NSE:RAMCOIND,NSE:TMPV,NSE:SHAKTIPUMP,NSE:MSTCLTD,NSE:ACUTAAS,NSE:GRANULES
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (35)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [BIOCON](https://in.tradingview.com/chart/?symbol=NSE:BIOCON)<br><sub>📶W9 · W↑69d · ↑CMF12d</sub> | ✓ SAFE | Biopharmaceutical manufacturing, diabetes oncology immunology therapies | ⚡ BULL_ANY_PPV | 94 | 🔄63 | ↑1.017 | ↑1d | SQ·PV | +2.7% | -2.37/-4.55 | +2.68% | 20% |
| [STOVEKRAFT](https://in.tradingview.com/chart/?symbol=NSE:STOVEKRAFT)<br><sub>📶W9 · 🚀SS·18x · ↓CMF17d</sub> | ✓ SAFE | Kitchen appliances cookware brands retail consumer homes | ⚡ BULL_ANY_PPV | 94 | 🔄86 | ↑1.029 | ↑1d | SQ·PV | +5.8% | 13.3/12.18 | +5.85% | 20% |
| [DCBBANK](https://in.tradingview.com/chart/?symbol=NSE:DCBBANK)<br><sub>📶W9 · W↑39d · ↓CMF9d</sub> | ✓ SAFE | Secured retail lending bank micro-SME agriculture focus | ⚡ BULL_ANY_PPV | 94 | 🔄70 | ↑1.022 | ↑1d | SQ·PV | +3.1% | 29.63/23.98 | +3.07% | 20% |
| [ROTO](https://in.tradingview.com/chart/?symbol=NSE:ROTO)<br><sub>📶W9 · W↑4d · 🚀SS · ↑CMF1d · DEL56%(T-1)</sub> | ✓ SAFE | Progressive cavity pumps for wastewater and sugar industries | ⚡ BULL_ANY_PPV | 94 | 🔄57 | ↑1.024 | ↑1d | SQ·PV | +5.0% | -15.17/-16.24 | +5.00% | 20% |
| [AARTIIND](https://in.tradingview.com/chart/?symbol=NSE:AARTIIND)<br><sub>📶W9 · W↑29d · ↓CMF4d</sub> | ✓ SAFE | Specialty chemicals and intermediates for pharmaceuticals cosmetics | ⚡ BULL_ANY_PPV | 93 | 🔄68 | ↑1.027 | ↑2d | SQ·PV | +4.0% | 14.46/8.96 | +3.14% | 20% |
| [TTKHLTCARE](https://in.tradingview.com/chart/?symbol=NSE:TTKHLTCARE)<br><sub>📶W9 · W↑87d · ↓CMF16d</sub> | ✓ SAFE | Pharmaceuticals, medical devices, consumer healthcare products India | ⚡ BULL_ANY_PPV | 55 | ↑53 | ↑1.048 | ↑5d | SQ·PV | +9.3% | 53.27/47.98 | +4.61% | 20% |
| [PANAMAPET](https://in.tradingview.com/chart/?symbol=NSE:PANAMAPET)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF10d</sub> | ✓ SAFE | Specialty petroleum products manufacturer serves pharma cosmetics rubber textiles | ⚡ BULL_ANY_PPV | 49 | 🔄95 | ↑1.069 | ↑1d | PV | +8.7% | 36.31/30.73 | +8.73% | 10% 🟨 |
| [RAMRAT](https://in.tradingview.com/chart/?symbol=NSE:RAMRAT)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE | Enameled copper wires manufacturing for motors industrial equipment | ⚡ BULL_ANY_PPV | 48 | 🔄83 | ↑1.061 | ↑2d | PV | +8.8% | 47.69/43.71 | +6.94% | 20% |
| [CRISIL](https://in.tradingview.com/chart/?symbol=NSE:CRISIL)<br><sub>📶W9 · W↑39d · ↑CMF11d</sub> | ✓ SAFE | Credit ratings analytics research risk advisory services | ⚡ BULL_ANY_PPV | 5 | ↑43 | ↑1.029 | ↑21d | PV | +17.5% | 47.12/43.16 | +1.68% | 20% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>📶W9 · W↑74d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 0 | ↑76 | ↑1.059 | ↑20d | PV | +19.4% | 64.61/59.48 | +5.25% | 20% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Cryogenic equipment manufacturing for LNG and industrial gases | 📈 BULL_ANY_MID | 99 | 🔄93 | ↑1.010 | ↑1d | SQ | +0.9% | -1.23/-2.65 | +0.87% | 20% |
| [CAPLIPOINT](https://in.tradingview.com/chart/?symbol=NSE:CAPLIPOINT)<br><sub>📶W9 · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | Pharma APIs finished formulations export-oriented Latin America Africa USA | 📈 BULL_ANY_MID | 99 | 🔄85 | ↑1.008 | ↑1d | SQ | +1.7% | 2.69/1.86 | +1.73% | 20% |
| [SMARTWORKS](https://in.tradingview.com/chart/?symbol=NSE:SMARTWORKS)<br><sub>📶W9 · W↑87d · ↓CMF11d</sub> | ✓ SAFE | Managed workspace solutions for enterprises and GCCs | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.015 | ↑1d | SQ | +2.8% | 5.42/1.91 | +2.75% | 20% |
| [ASIANHOTNR](https://in.tradingview.com/chart/?symbol=NSE:ASIANHOTNR)<br><sub>📶W9 · 🚀SS · ↓CMF17d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 93 | 🔄42 | ↑1.029 | ↑2d | SQ | +4.8% | -5.77/-12.21 | +3.05% | 20% |
| [INDIQUBE](https://in.tradingview.com/chart/?symbol=NSE:INDIQUBE)<br><sub>📶W9 · W↑39d · ↑CMF19d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 89 | 🔄38 | ↑1.037 | ↑1d | SQ | +4.6% | 18.7/17.32 | +4.63% | 20% |
| [GHCLTEXTIL](https://in.tradingview.com/chart/?symbol=NSE:GHCLTEXTIL)<br><sub>📶W9 · W↑29d · 🚀SS · ↓CMF5d</sub> | ✓ SAFE | Cotton yarn spinning for apparel manufacturers | 📈 BULL_ANY_MID | 86 | 🔄88 | ↑1.039 | ↑4d | SQ | +5.6% | 43.17/41.82 | +4.38% | 20% |
| [INDIGOPNTS](https://in.tradingview.com/chart/?symbol=NSE:INDIGOPNTS)<br><sub>📶W9 · W↑87d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Decorative paints manufacturer serving residential construction sector | 📈 BULL_ANY_MID | 81 | 🔄62 | ↑1.034 | ↑9d | SQ | +7.6% | 54.0/49.74 | +3.47% | 20% |
| [HLEGLAS](https://in.tradingview.com/chart/?symbol=NSE:HLEGLAS)<br><sub>📶W9 · W↑87d · ↑CMF1d</sub> | ✓ SAFE | Glass-lined equipment for pharma chemical processing | 📈 BULL_ANY_MID | 80 | 🔄66 | ↑1.059 | ↑10d | SQ | +10.2% | 55.22/45.62 | +6.07% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑32d · ↓CMF18d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 67 | ↓81 | ↑1.007 | ↑3d | SQ | +3.9% | 10.9/8.21 | +0.29% | 20% |
| [SANGAMIND](https://in.tradingview.com/chart/?symbol=NSE:SANGAMIND)<br><sub>📶W9 · W↑82d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | PV yarn denim seamless garments textile manufacturer | 📈 BULL_ANY_MID | 64 | ↓82 | ↑1.006 | ↑6d | SQ | +2.8% | 36.92/33.53 | +0.48% | 20% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>📶W9 · W↑79d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 63 | ↑45 | ↑1.018 | ↑2d | SQ | +3.0% | 15.62/11.03 | +1.09% | 20% |
| [GCSL](https://in.tradingview.com/chart/?symbol=NSE:GCSL)<br><sub>📶W9 · 🚀SS · ↓CMF5d · DEL54%(T-1)</sub> | ✓ SAFE | Merchant banking, corporate finance, capital markets advisory | 📈 BULL_ANY_MID | 63 | ↑50 | ↑1.020 | ↑2d | SQ | +4.2% | 35.02/33.07 | +1.26% | 20% 🟦 |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 62 | ↑61 | ↑1.020 | ↑3d | SQ | +2.9% | 12.63/4.94 | +2.41% | 20% |
| [FUSION](https://in.tradingview.com/chart/?symbol=NSE:FUSION)<br><sub>📶W9 · 🚀SS · ↓CMF5d</sub> | ✓ SAFE | Microfinance loans for rural women entrepreneurs | 📈 BULL_ANY_MID | 59 | 🔄68 | ↑1.014 | ↑1d | — | +2.5% | -16.57/-18.51 | +2.51% | 20% |
| [APOLLOHOSP](https://in.tradingview.com/chart/?symbol=NSE:APOLLOHOSP)<br><sub>📶W9 · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↓74 | ↓1.004 | ↑2d | SQ | +0.7% | 38.14/36.38 | +0.01% | 20% |
| [BRITANNIA](https://in.tradingview.com/chart/?symbol=NSE:BRITANNIA)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF22d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 54 | ↑33 | ↑1.019 | ↑11d | SQ | +4.7% | 45.79/38.66 | +0.99% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄83 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [RELTD](https://in.tradingview.com/chart/?symbol=NSE:RELTD)<br><sub>📶W9 · W↑39d · ↓CMF14d · DEL67%(T-1)</sub> | ✓ SAFE | Solar power plants, EV charging, sugar trading conglomerate | 📈 BULL_ANY_MID | 52 | ↓74 | ↓0.996 | ↓8d | SQ | -2.2% | -16.52/-17.11 | -0.89% | 20% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Glass-lined reactors pharmaceuticals chemicals process equipment | 📈 BULL_ANY_MID | 51 | ↓98 | ↓0.996 | ↓9d | SQ | +0.7% | 14.91/14.46 | -1.21% | 5% 🟥 |
| [STYL](https://in.tradingview.com/chart/?symbol=NSE:STYL)<br><sub>📶W9 · ↑CMF29d</sub> | ✓ SAFE | Secure payment solutions provider for Indian BFSI sector | 📈 BULL_ANY_MID | 49 | 🔄50 | ↑1.058 | ↑1d | — | +6.8% | 17.0/11.46 | +6.75% | 20% |
| [PARADEEP](https://in.tradingview.com/chart/?symbol=NSE:PARADEEP)<br><sub>📶W9 · W↑94d · ↑CMF7d</sub> | ✓ SAFE | Phosphatic fertilizers manufacturer for Indian agriculture sector | 📈 BULL_ANY_MID | 47 | 🔄41 | ↑1.018 | ↑8d | — | +10.0% | 23.7/22.14 | +0.97% | 20% |
| [DIXON](https://in.tradingview.com/chart/?symbol=NSE:DIXON)<br><sub>📶W9 · W↑99d · ↑CMF15d</sub> | ✓ SAFE | Electronics manufacturing services for consumer appliances and lighting | 📈 BULL_ANY_MID | 17 | ↑68 | ↓1.009 | ↑3d | — | +2.2% | 43.04/39.75 | -0.77% | 20% |
| [ULTRACEMCO](https://in.tradingview.com/chart/?symbol=NSE:ULTRACEMCO)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 15 | ↑41 | ↑1.010 | ↑15d | — | +5.6% | 51.42/48.64 | +0.28% | 20% |
| [LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS)<br><sub>📶W9 · W↑19d · ↑CMF16d</sub> | ✓ SAFE | Engineering design development testing services global | 📈 BULL_ANY_MID | 8 | ↑24 | ↓1.010 | ↑12d | — | +7.5% | 43.24/42.45 | -0.56% | 20% |
| [AURUM](https://in.tradingview.com/chart/?symbol=NSE:AURUM)<br><sub>📶W9 · ↓CMF15d</sub> | ✓ SAFE | Real estate software platform, rental and sales digitization | 📈 BULL_ANY_MID | 0 | ↓77 | ↓1.002 | ↓40d | — | +22.2% | -12.42/-13.08 | -0.18% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,###WATCHLIST,NSE:BIOCON,NSE:STOVEKRAFT,NSE:DCBBANK,NSE:ROTO,NSE:AARTIIND,NSE:TTKHLTCARE,NSE:PANAMAPET,NSE:RAMRAT,NSE:CRISIL,NSE:DIVISLAB,NSE:INOXINDIA,NSE:CAPLIPOINT,NSE:SMARTWORKS,NSE:ASIANHOTNR,NSE:INDIQUBE,NSE:GHCLTEXTIL,NSE:INDIGOPNTS,NSE:HLEGLAS,NSE:SHRIRAMFIN,NSE:SANGAMIND,NSE:DLF,NSE:GCSL,NSE:JSWSTEEL,NSE:FUSION,NSE:APOLLOHOSP,NSE:BRITANNIA,NSE:OFSS,NSE:RELTD,NSE:SETL,NSE:STYL,NSE:PARADEEP,NSE:DIXON,NSE:ULTRACEMCO,NSE:LTTS,NSE:AURUM
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (37)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [BIOCON](https://in.tradingview.com/chart/?symbol=NSE:BIOCON)<br><sub>📶W9 · W↑69d · ↑CMF12d</sub> | ✓ SAFE | Biopharmaceutical manufacturing, diabetes oncology immunology therapies | ⚡ BULL_ANY_PPV | 94 | 🔄63 | ↑1.017 | ↑1d | SQ·PV | +2.7% | -2.37/-4.55 | +2.68% | 20% |
| [STOVEKRAFT](https://in.tradingview.com/chart/?symbol=NSE:STOVEKRAFT)<br><sub>📶W9 · 🚀SS·18x · ↓CMF17d</sub> | ✓ SAFE | Kitchen appliances cookware brands retail consumer homes | ⚡ BULL_ANY_PPV | 94 | 🔄86 | ↑1.029 | ↑1d | SQ·PV | +5.8% | 13.3/12.18 | +5.85% | 20% |
| [DCBBANK](https://in.tradingview.com/chart/?symbol=NSE:DCBBANK)<br><sub>📶W9 · W↑39d · ↓CMF9d</sub> | ✓ SAFE | Secured retail lending bank micro-SME agriculture focus | ⚡ BULL_ANY_PPV | 94 | 🔄70 | ↑1.022 | ↑1d | SQ·PV | +3.1% | 29.63/23.98 | +3.07% | 20% |
| [ROTO](https://in.tradingview.com/chart/?symbol=NSE:ROTO)<br><sub>📶W9 · W↑4d · 🚀SS · ↑CMF1d · DEL56%(T-1)</sub> | ✓ SAFE | Progressive cavity pumps for wastewater and sugar industries | ⚡ BULL_ANY_PPV | 94 | 🔄57 | ↑1.024 | ↑1d | SQ·PV | +5.0% | -15.17/-16.24 | +5.00% | 20% |
| [AARTIIND](https://in.tradingview.com/chart/?symbol=NSE:AARTIIND)<br><sub>📶W9 · W↑29d · ↓CMF4d</sub> | ✓ SAFE | Specialty chemicals and intermediates for pharmaceuticals cosmetics | ⚡ BULL_ANY_PPV | 93 | 🔄68 | ↑1.027 | ↑2d | SQ·PV | +4.0% | 14.46/8.96 | +3.14% | 20% |
| [TTKHLTCARE](https://in.tradingview.com/chart/?symbol=NSE:TTKHLTCARE)<br><sub>📶W9 · W↑87d · ↓CMF16d</sub> | ✓ SAFE | Pharmaceuticals, medical devices, consumer healthcare products India | ⚡ BULL_ANY_PPV | 55 | ↑53 | ↑1.048 | ↑5d | SQ·PV | +9.3% | 53.27/47.98 | +4.61% | 20% |
| [PANAMAPET](https://in.tradingview.com/chart/?symbol=NSE:PANAMAPET)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF10d</sub> | ✓ SAFE | Specialty petroleum products manufacturer serves pharma cosmetics rubber textiles | ⚡ BULL_ANY_PPV | 49 | 🔄95 | ↑1.069 | ↑1d | PV | +8.7% | 36.31/30.73 | +8.73% | 10% 🟨 |
| [RAMRAT](https://in.tradingview.com/chart/?symbol=NSE:RAMRAT)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE | Enameled copper wires manufacturing for motors industrial equipment | ⚡ BULL_ANY_PPV | 48 | 🔄83 | ↑1.061 | ↑2d | PV | +8.8% | 47.69/43.71 | +6.94% | 20% |
| [CRISIL](https://in.tradingview.com/chart/?symbol=NSE:CRISIL)<br><sub>📶W9 · W↑39d · ↑CMF11d</sub> | ✓ SAFE | Credit ratings analytics research risk advisory services | ⚡ BULL_ANY_PPV | 5 | ↑43 | ↑1.029 | ↑21d | PV | +17.5% | 47.12/43.16 | +1.68% | 20% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>📶W9 · W↑74d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 0 | ↑76 | ↑1.059 | ↑20d | PV | +19.4% | 64.61/59.48 | +5.25% | 20% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Cryogenic equipment manufacturing for LNG and industrial gases | 📈 BULL_ANY_MID | 99 | 🔄93 | ↑1.010 | ↑1d | SQ | +0.9% | -1.23/-2.65 | +0.87% | 20% |
| [CAPLIPOINT](https://in.tradingview.com/chart/?symbol=NSE:CAPLIPOINT)<br><sub>📶W9 · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | Pharma APIs finished formulations export-oriented Latin America Africa USA | 📈 BULL_ANY_MID | 99 | 🔄85 | ↑1.008 | ↑1d | SQ | +1.7% | 2.69/1.86 | +1.73% | 20% |
| [SMARTWORKS](https://in.tradingview.com/chart/?symbol=NSE:SMARTWORKS)<br><sub>📶W9 · W↑87d · ↓CMF11d</sub> | ✓ SAFE | Managed workspace solutions for enterprises and GCCs | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.015 | ↑1d | SQ | +2.8% | 5.42/1.91 | +2.75% | 20% |
| [ASIANHOTNR](https://in.tradingview.com/chart/?symbol=NSE:ASIANHOTNR)<br><sub>📶W9 · 🚀SS · ↓CMF17d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 93 | 🔄42 | ↑1.029 | ↑2d | SQ | +4.8% | -5.77/-12.21 | +3.05% | 20% |
| [INDIQUBE](https://in.tradingview.com/chart/?symbol=NSE:INDIQUBE)<br><sub>📶W9 · W↑39d · ↑CMF19d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 89 | 🔄38 | ↑1.037 | ↑1d | SQ | +4.6% | 18.7/17.32 | +4.63% | 20% |
| [GHCLTEXTIL](https://in.tradingview.com/chart/?symbol=NSE:GHCLTEXTIL)<br><sub>📶W9 · W↑29d · 🚀SS · ↓CMF5d</sub> | ✓ SAFE | Cotton yarn spinning for apparel manufacturers | 📈 BULL_ANY_MID | 86 | 🔄88 | ↑1.039 | ↑4d | SQ | +5.6% | 43.17/41.82 | +4.38% | 20% |
| [INDIGOPNTS](https://in.tradingview.com/chart/?symbol=NSE:INDIGOPNTS)<br><sub>📶W9 · W↑87d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Decorative paints manufacturer serving residential construction sector | 📈 BULL_ANY_MID | 81 | 🔄62 | ↑1.034 | ↑9d | SQ | +7.6% | 54.0/49.74 | +3.47% | 20% |
| [HLEGLAS](https://in.tradingview.com/chart/?symbol=NSE:HLEGLAS)<br><sub>📶W9 · W↑87d · ↑CMF1d</sub> | ✓ SAFE | Glass-lined equipment for pharma chemical processing | 📈 BULL_ANY_MID | 80 | 🔄66 | ↑1.059 | ↑10d | SQ | +10.2% | 55.22/45.62 | +6.07% | 20% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>📶W9 · W↑79d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 63 | ↑45 | ↑1.018 | ↑2d | SQ | +3.0% | 15.62/11.03 | +1.09% | 20% |
| [GCSL](https://in.tradingview.com/chart/?symbol=NSE:GCSL)<br><sub>📶W9 · 🚀SS · ↓CMF5d · DEL54%(T-1)</sub> | ✓ SAFE | Merchant banking, corporate finance, capital markets advisory | 📈 BULL_ANY_MID | 63 | ↑50 | ↑1.020 | ↑2d | SQ | +4.2% | 35.02/33.07 | +1.26% | 20% 🟦 |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 62 | ↑61 | ↑1.020 | ↑3d | SQ | +2.9% | 12.63/4.94 | +2.41% | 20% |
| [FUSION](https://in.tradingview.com/chart/?symbol=NSE:FUSION)<br><sub>📶W9 · 🚀SS · ↓CMF5d</sub> | ✓ SAFE | Microfinance loans for rural women entrepreneurs | 📈 BULL_ANY_MID | 59 | 🔄68 | ↑1.014 | ↑1d | — | +2.5% | -16.57/-18.51 | +2.51% | 20% |
| [BRITANNIA](https://in.tradingview.com/chart/?symbol=NSE:BRITANNIA)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF22d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 54 | ↑33 | ↑1.019 | ↑11d | SQ | +4.7% | 45.79/38.66 | +0.99% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄83 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [STYL](https://in.tradingview.com/chart/?symbol=NSE:STYL)<br><sub>📶W9 · ↑CMF29d</sub> | ✓ SAFE | Secure payment solutions provider for Indian BFSI sector | 📈 BULL_ANY_MID | 49 | 🔄50 | ↑1.058 | ↑1d | — | +6.8% | 17.0/11.46 | +6.75% | 20% |
| [PARADEEP](https://in.tradingview.com/chart/?symbol=NSE:PARADEEP)<br><sub>📶W9 · W↑94d · ↑CMF7d</sub> | ✓ SAFE | Phosphatic fertilizers manufacturer for Indian agriculture sector | 📈 BULL_ANY_MID | 47 | 🔄41 | ↑1.018 | ↑8d | — | +10.0% | 23.7/22.14 | +0.97% | 20% |
| [DIXON](https://in.tradingview.com/chart/?symbol=NSE:DIXON)<br><sub>📶W9 · W↑99d · ↑CMF15d</sub> | ✓ SAFE | Electronics manufacturing services for consumer appliances and lighting | 📈 BULL_ANY_MID | 17 | ↑68 | ↓1.009 | ↑3d | — | +2.2% | 43.04/39.75 | -0.77% | 20% |
| [ULTRACEMCO](https://in.tradingview.com/chart/?symbol=NSE:ULTRACEMCO)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 15 | ↑41 | ↑1.010 | ↑15d | — | +5.6% | 51.42/48.64 | +0.28% | 20% |
| [LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS)<br><sub>📶W9 · W↑19d · ↑CMF16d</sub> | ✓ SAFE | Engineering design development testing services global | 📈 BULL_ANY_MID | 8 | ↑24 | ↓1.010 | ↑12d | — | +7.5% | 43.24/42.45 | -0.56% | 20% |
| [EMAMILTD](https://in.tradingview.com/chart/?symbol=NSE:EMAMILTD)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Personal care, healthcare, FMCG for Indian households | ⚡ BULL_ANY_PPV | 99 | 🔄9 | ↑1.011 | ↑1d | SQ·PV | +1.6% | -27.99/-29.55 | +1.65% | 20% |
| [SAMMAANCAP](https://in.tradingview.com/chart/?symbol=NSE:SAMMAANCAP)<br><sub>↑CMF0d</sub> | ✓ SAFE | NBFC housing finance loans mortgages retail borrowers | ⚡ BULL_ANY_PPV | 94 | 🔄66 | ↑1.027 | ↑1d | SQ·PV | +3.5% | -20.51/-31.11 | +3.52% | 20% |
| [BLKASHYAP](https://in.tradingview.com/chart/?symbol=NSE:BLKASHYAP)<br><sub>🚀SS · ↑CMF18d</sub> | ✓ SAFE | EPC contractor building high-rise residential commercial complexes | ⚡ BULL_ANY_PPV | 54 | 🔄31 | ↑1.022 | ↑1d | PV | +4.5% | -19.45/-22.99 | +4.52% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>🚀SS · ↓CMF26d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 99 | 🔄42 | ↑1.010 | ↑1d | SQ | +2.6% | -48.58/-54.51 | +2.56% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄60 | ↑1.012 | ↑1d | SQ | +3.0% | -40.63/-43.65 | +2.95% | 20% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>🚀SS · ↑CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄90 | ↑1.009 | ↑1d | SQ | +2.7% | -36.34/-42.32 | +2.74% | 20% |
| [AMBUJACEM](https://in.tradingview.com/chart/?symbol=NSE:AMBUJACEM)<br><sub>W↑27d · ↑CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄13 | ↑1.008 | ↑1d | SQ | +2.0% | 0.82/0.46 | +2.00% | 20% |
| [DHANUKA](https://in.tradingview.com/chart/?symbol=NSE:DHANUKA)<br><sub>↑CMF3d</sub> | ✓ SAFE | Herbicides insecticides fungicides manufacturing for Indian farmers | 📈 BULL_ANY_MID | 99 | 🔄12 | ↑1.009 | ↑1d | SQ | +2.1% | -31.85/-35.86 | +2.10% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,###WATCHLIST,NSE:BIOCON,NSE:STOVEKRAFT,NSE:DCBBANK,NSE:ROTO,NSE:AARTIIND,NSE:TTKHLTCARE,NSE:PANAMAPET,NSE:RAMRAT,NSE:CRISIL,NSE:DIVISLAB,NSE:INOXINDIA,NSE:CAPLIPOINT,NSE:SMARTWORKS,NSE:ASIANHOTNR,NSE:INDIQUBE,NSE:GHCLTEXTIL,NSE:INDIGOPNTS,NSE:HLEGLAS,NSE:DLF,NSE:GCSL,NSE:JSWSTEEL,NSE:FUSION,NSE:BRITANNIA,NSE:OFSS,NSE:STYL,NSE:PARADEEP,NSE:DIXON,NSE:ULTRACEMCO,NSE:LTTS,NSE:EMAMILTD,NSE:SAMMAANCAP,NSE:BLKASHYAP,NSE:TATASTEEL,NSE:HINDALCO,NSE:POWERINDIA,NSE:AMBUJACEM,NSE:DHANUKA
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (40)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [BIOCON](https://in.tradingview.com/chart/?symbol=NSE:BIOCON)<br><sub>📶W9 · W↑69d · ↑CMF12d</sub> | ✓ SAFE | Biopharmaceutical manufacturing, diabetes oncology immunology therapies | ⚡ BULL_ANY_PPV | 94 | 🔄63 | ↑1.017 | ↑1d | SQ·PV | +2.7% | -2.37/-4.55 | +2.68% | 20% |
| [STOVEKRAFT](https://in.tradingview.com/chart/?symbol=NSE:STOVEKRAFT)<br><sub>📶W9 · 🚀SS·18x · ↓CMF17d</sub> | ✓ SAFE | Kitchen appliances cookware brands retail consumer homes | ⚡ BULL_ANY_PPV | 94 | 🔄86 | ↑1.029 | ↑1d | SQ·PV | +5.8% | 13.3/12.18 | +5.85% | 20% |
| [DCBBANK](https://in.tradingview.com/chart/?symbol=NSE:DCBBANK)<br><sub>📶W9 · W↑39d · ↓CMF9d</sub> | ✓ SAFE | Secured retail lending bank micro-SME agriculture focus | ⚡ BULL_ANY_PPV | 94 | 🔄70 | ↑1.022 | ↑1d | SQ·PV | +3.1% | 29.63/23.98 | +3.07% | 20% |
| [ROTO](https://in.tradingview.com/chart/?symbol=NSE:ROTO)<br><sub>📶W9 · W↑4d · 🚀SS · ↑CMF1d · DEL56%(T-1)</sub> | ✓ SAFE | Progressive cavity pumps for wastewater and sugar industries | ⚡ BULL_ANY_PPV | 94 | 🔄57 | ↑1.024 | ↑1d | SQ·PV | +5.0% | -15.17/-16.24 | +5.00% | 20% |
| [AARTIIND](https://in.tradingview.com/chart/?symbol=NSE:AARTIIND)<br><sub>📶W9 · W↑29d · ↓CMF4d</sub> | ✓ SAFE | Specialty chemicals and intermediates for pharmaceuticals cosmetics | ⚡ BULL_ANY_PPV | 93 | 🔄68 | ↑1.027 | ↑2d | SQ·PV | +4.0% | 14.46/8.96 | +3.14% | 20% |
| [TTKHLTCARE](https://in.tradingview.com/chart/?symbol=NSE:TTKHLTCARE)<br><sub>📶W9 · W↑87d · ↓CMF16d</sub> | ✓ SAFE | Pharmaceuticals, medical devices, consumer healthcare products India | ⚡ BULL_ANY_PPV | 55 | ↑53 | ↑1.048 | ↑5d | SQ·PV | +9.3% | 53.27/47.98 | +4.61% | 20% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Cryogenic equipment manufacturing for LNG and industrial gases | 📈 BULL_ANY_MID | 99 | 🔄93 | ↑1.010 | ↑1d | SQ | +0.9% | -1.23/-2.65 | +0.87% | 20% |
| [CAPLIPOINT](https://in.tradingview.com/chart/?symbol=NSE:CAPLIPOINT)<br><sub>📶W9 · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | Pharma APIs finished formulations export-oriented Latin America Africa USA | 📈 BULL_ANY_MID | 99 | 🔄85 | ↑1.008 | ↑1d | SQ | +1.7% | 2.69/1.86 | +1.73% | 20% |
| [SMARTWORKS](https://in.tradingview.com/chart/?symbol=NSE:SMARTWORKS)<br><sub>📶W9 · W↑87d · ↓CMF11d</sub> | ✓ SAFE | Managed workspace solutions for enterprises and GCCs | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.015 | ↑1d | SQ | +2.8% | 5.42/1.91 | +2.75% | 20% |
| [ASIANHOTNR](https://in.tradingview.com/chart/?symbol=NSE:ASIANHOTNR)<br><sub>📶W9 · 🚀SS · ↓CMF17d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 93 | 🔄42 | ↑1.029 | ↑2d | SQ | +4.8% | -5.77/-12.21 | +3.05% | 20% |
| [INDIQUBE](https://in.tradingview.com/chart/?symbol=NSE:INDIQUBE)<br><sub>📶W9 · W↑39d · ↑CMF19d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 89 | 🔄38 | ↑1.037 | ↑1d | SQ | +4.6% | 18.7/17.32 | +4.63% | 20% |
| [GHCLTEXTIL](https://in.tradingview.com/chart/?symbol=NSE:GHCLTEXTIL)<br><sub>📶W9 · W↑29d · 🚀SS · ↓CMF5d</sub> | ✓ SAFE | Cotton yarn spinning for apparel manufacturers | 📈 BULL_ANY_MID | 86 | 🔄88 | ↑1.039 | ↑4d | SQ | +5.6% | 43.17/41.82 | +4.38% | 20% |
| [INDIGOPNTS](https://in.tradingview.com/chart/?symbol=NSE:INDIGOPNTS)<br><sub>📶W9 · W↑87d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Decorative paints manufacturer serving residential construction sector | 📈 BULL_ANY_MID | 81 | 🔄62 | ↑1.034 | ↑9d | SQ | +7.6% | 54.0/49.74 | +3.47% | 20% |
| [HLEGLAS](https://in.tradingview.com/chart/?symbol=NSE:HLEGLAS)<br><sub>📶W9 · W↑87d · ↑CMF1d</sub> | ✓ SAFE | Glass-lined equipment for pharma chemical processing | 📈 BULL_ANY_MID | 80 | 🔄66 | ↑1.059 | ↑10d | SQ | +10.2% | 55.22/45.62 | +6.07% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑32d · ↓CMF18d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 67 | ↓81 | ↑1.007 | ↑3d | SQ | +3.9% | 10.9/8.21 | +0.29% | 20% |
| [SANGAMIND](https://in.tradingview.com/chart/?symbol=NSE:SANGAMIND)<br><sub>📶W9 · W↑82d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | PV yarn denim seamless garments textile manufacturer | 📈 BULL_ANY_MID | 64 | ↓82 | ↑1.006 | ↑6d | SQ | +2.8% | 36.92/33.53 | +0.48% | 20% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>📶W9 · W↑79d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 63 | ↑45 | ↑1.018 | ↑2d | SQ | +3.0% | 15.62/11.03 | +1.09% | 20% |
| [GCSL](https://in.tradingview.com/chart/?symbol=NSE:GCSL)<br><sub>📶W9 · 🚀SS · ↓CMF5d · DEL54%(T-1)</sub> | ✓ SAFE | Merchant banking, corporate finance, capital markets advisory | 📈 BULL_ANY_MID | 63 | ↑50 | ↑1.020 | ↑2d | SQ | +4.2% | 35.02/33.07 | +1.26% | 20% 🟦 |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 62 | ↑61 | ↑1.020 | ↑3d | SQ | +2.9% | 12.63/4.94 | +2.41% | 20% |
| [APOLLOHOSP](https://in.tradingview.com/chart/?symbol=NSE:APOLLOHOSP)<br><sub>📶W9 · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↓74 | ↓1.004 | ↑2d | SQ | +0.7% | 38.14/36.38 | +0.01% | 20% |
| [BRITANNIA](https://in.tradingview.com/chart/?symbol=NSE:BRITANNIA)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF22d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 54 | ↑33 | ↑1.019 | ↑11d | SQ | +4.7% | 45.79/38.66 | +0.99% | 20% |
| [RELTD](https://in.tradingview.com/chart/?symbol=NSE:RELTD)<br><sub>📶W9 · W↑39d · ↓CMF14d · DEL67%(T-1)</sub> | ✓ SAFE | Solar power plants, EV charging, sugar trading conglomerate | 📈 BULL_ANY_MID | 52 | ↓74 | ↓0.996 | ↓8d | SQ | -2.2% | -16.52/-17.11 | -0.89% | 20% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Glass-lined reactors pharmaceuticals chemicals process equipment | 📈 BULL_ANY_MID | 51 | ↓98 | ↓0.996 | ↓9d | SQ | +0.7% | 14.91/14.46 | -1.21% | 5% 🟥 |
| [EMAMILTD](https://in.tradingview.com/chart/?symbol=NSE:EMAMILTD)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Personal care, healthcare, FMCG for Indian households | ⚡ BULL_ANY_PPV | 99 | 🔄9 | ↑1.011 | ↑1d | SQ·PV | +1.6% | -27.99/-29.55 | +1.65% | 20% |
| [SAMMAANCAP](https://in.tradingview.com/chart/?symbol=NSE:SAMMAANCAP)<br><sub>↑CMF0d</sub> | ✓ SAFE | NBFC housing finance loans mortgages retail borrowers | ⚡ BULL_ANY_PPV | 94 | 🔄66 | ↑1.027 | ↑1d | SQ·PV | +3.5% | -20.51/-31.11 | +3.52% | 20% |
| [PASHUPATI](https://in.tradingview.com/chart/?symbol=NSE:PASHUPATI)<br><sub>RVOL17x · ↓CMF30d · DEL93%(T-1) · 🎯SLING</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 50 | ↓50 | ↑0.993 | ↓15d | SQ·PV | -2.3% | -56.39/-57.72 | +0.52% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>🚀SS · ↓CMF26d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 99 | 🔄42 | ↑1.010 | ↑1d | SQ | +2.6% | -48.58/-54.51 | +2.56% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄60 | ↑1.012 | ↑1d | SQ | +3.0% | -40.63/-43.65 | +2.95% | 20% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>🚀SS · ↑CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄90 | ↑1.009 | ↑1d | SQ | +2.7% | -36.34/-42.32 | +2.74% | 20% |
| [AMBUJACEM](https://in.tradingview.com/chart/?symbol=NSE:AMBUJACEM)<br><sub>W↑27d · ↑CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄13 | ↑1.008 | ↑1d | SQ | +2.0% | 0.82/0.46 | +2.00% | 20% |
| [DHANUKA](https://in.tradingview.com/chart/?symbol=NSE:DHANUKA)<br><sub>↑CMF3d</sub> | ✓ SAFE | Herbicides insecticides fungicides manufacturing for Indian farmers | 📈 BULL_ANY_MID | 99 | 🔄12 | ↑1.009 | ↑1d | SQ | +2.1% | -31.85/-35.86 | +2.10% | 20% |
| [KIMS](https://in.tradingview.com/chart/?symbol=NSE:KIMS)<br><sub>🚀SS · ↓CMF16d</sub> | ⚠ CAUTION | Multi-specialty hospital chain South India tertiary care | 📈 BULL_ANY_MID | 69 | ↓64 | ↑1.006 | ↑1d | SQ | +0.8% | 11.15/8.82 | +0.80% | 20% |
| [POWERMECH](https://in.tradingview.com/chart/?symbol=NSE:POWERMECH)<br><sub>🚀SS · ↑CMF2d</sub> | ✓ SAFE | EPC contractor boilers turbines power plants infrastructure | 📈 BULL_ANY_MID | 69 | ↓51 | ↑1.005 | ↑1d | SQ | +1.7% | -9.64/-10.65 | +1.71% | 20% |
| [BALMLAWRIE](https://in.tradingview.com/chart/?symbol=NSE:BALMLAWRIE)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | PSU lubricants, packaging, logistics, refinery services | 📈 BULL_ANY_MID | 69 | ↓26 | ↑1.005 | ↑1d | SQ | +0.6% | -38.81/-44.0 | +0.56% | 20% |
| [MUTHOOTFIN](https://in.tradingview.com/chart/?symbol=NSE:MUTHOOTFIN)<br><sub>↓CMF2d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 64 | ↓27 | ↑0.999 | ↑1d | SQ | +0.2% | -22.85/-24.08 | +0.17% | 20% |
| [GPTINFRA](https://in.tradingview.com/chart/?symbol=NSE:GPTINFRA)<br><sub>↓CMF15d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 61 | ↓50 | ↑1.003 | ↓9d | SQ | +1.4% | -28.99/-29.19 | +0.63% | 20% |
| [KOVAI](https://in.tradingview.com/chart/?symbol=NSE:KOVAI)<br><sub>↓CMF12d</sub> | ⚠ CAUTION | Tertiary care hospital pharmacy medical education Coimbatore healthcare | 📈 BULL_ANY_MID | 58 | ↓50 | ↓1.000 | ↓2d | SQ | +0.5% | -11.45/-14.59 | -0.57% | 20% |
| [TCI](https://in.tradingview.com/chart/?symbol=NSE:TCI)<br><sub>W↑4d · ↓CMF5d</sub> | ⚠ CAUTION | Multimodal freight logistics supply chain solutions provider | 📈 BULL_ANY_MID | 58 | ↓19 | ↓1.003 | ↑2d | SQ | +1.4% | -29.99/-32.89 | -0.11% | 20% |
| [PREMEXPLN](https://in.tradingview.com/chart/?symbol=NSE:PREMEXPLN)<br><sub>↓CMF19d</sub> | ✓ SAFE | Explosives propellants detonators defense space mining manufacturing | 📈 BULL_ANY_MID | 50 | ↓83 | ↑1.001 | ↓40d | SQ | +1.5% | -26.85/-28.18 | +0.58% | 20% |
| [DBCORP](https://in.tradingview.com/chart/?symbol=NSE:DBCORP)<br><sub>W↑24d · 🚀SS · ↓CMF30d · DEL66%(T-1)</sub> | ✓ SAFE | Print media, newspapers, advertising, pan-India distribution network | 📈 BULL_ANY_MID | 50 | ↓17 | ↑1.003 | ↑21d | SQ | +6.6% | 23.35/21.47 | +0.22% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,###WATCHLIST,NSE:BIOCON,NSE:STOVEKRAFT,NSE:DCBBANK,NSE:ROTO,NSE:AARTIIND,NSE:TTKHLTCARE,NSE:INOXINDIA,NSE:CAPLIPOINT,NSE:SMARTWORKS,NSE:ASIANHOTNR,NSE:INDIQUBE,NSE:GHCLTEXTIL,NSE:INDIGOPNTS,NSE:HLEGLAS,NSE:SHRIRAMFIN,NSE:SANGAMIND,NSE:DLF,NSE:GCSL,NSE:JSWSTEEL,NSE:APOLLOHOSP,NSE:BRITANNIA,NSE:RELTD,NSE:SETL,NSE:EMAMILTD,NSE:SAMMAANCAP,NSE:PASHUPATI,NSE:TATASTEEL,NSE:HINDALCO,NSE:POWERINDIA,NSE:AMBUJACEM,NSE:DHANUKA,NSE:KIMS,NSE:POWERMECH,NSE:BALMLAWRIE,NSE:MUTHOOTFIN,NSE:GPTINFRA,NSE:KOVAI,NSE:TCI,NSE:PREMEXPLN,NSE:DBCORP
```

---

### 🔥 MAJOR — PPV confirmed (6)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PANAMAPET](https://in.tradingview.com/chart/?symbol=NSE:PANAMAPET)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF10d</sub> | ✓ SAFE | Specialty petroleum products manufacturer serves pharma cosmetics rubber textiles | ⚡ BULL_ANY_PPV | 49 | 🔄95 | ↑1.069 | ↑1d | PV | +8.7% | 36.31/30.73 | +8.73% | 10% 🟨 |
| [RAMRAT](https://in.tradingview.com/chart/?symbol=NSE:RAMRAT)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE | Enameled copper wires manufacturing for motors industrial equipment | ⚡ BULL_ANY_PPV | 48 | 🔄83 | ↑1.061 | ↑2d | PV | +8.8% | 47.69/43.71 | +6.94% | 20% |
| [CRISIL](https://in.tradingview.com/chart/?symbol=NSE:CRISIL)<br><sub>📶W9 · W↑39d · ↑CMF11d</sub> | ✓ SAFE | Credit ratings analytics research risk advisory services | ⚡ BULL_ANY_PPV | 5 | ↑43 | ↑1.029 | ↑21d | PV | +17.5% | 47.12/43.16 | +1.68% | 20% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>📶W9 · W↑74d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 0 | ↑76 | ↑1.059 | ↑20d | PV | +19.4% | 64.61/59.48 | +5.25% | 20% |
| [BLKASHYAP](https://in.tradingview.com/chart/?symbol=NSE:BLKASHYAP)<br><sub>🚀SS · ↑CMF18d</sub> | ✓ SAFE | EPC contractor building high-rise residential commercial complexes | ⚡ BULL_ANY_PPV | 54 | 🔄31 | ↑1.022 | ↑1d | PV | +4.5% | -19.45/-22.99 | +4.52% | 20% |
| [REPCOHOME](https://in.tradingview.com/chart/?symbol=NSE:REPCOHOME)<br><sub>↓CMF10d</sub> | ⚠ CAUTION | Home loans for salaried and self-employed individuals | ⚡ BULL_ANY_PPV | 11 | ↓31 | ↑1.005 | ↓19d | PV | -4.3% | -37.43/-40.94 | +1.39% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,###WATCHLIST,NSE:PANAMAPET,NSE:RAMRAT,NSE:CRISIL,NSE:DIVISLAB,NSE:BLKASHYAP,NSE:REPCOHOME
```

### 🟢 OVERSOLD — reversal from −53/−60 (2)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [VTL](https://in.tradingview.com/chart/?symbol=NSE:VTL)<br><sub>🚀SS · ↓CMF18d · 🎯SLING</sub> | ✓ SAFE | Yarn fabric acrylic fiber garments textiles manufacturer | 🟡 BULL_OS_L2 | 6 | ↓72 | ↑0.995 | ↓19d | — | -5.3% | -51.9/-54.97 | +0.70% | 20% |
| [AXISBANK](https://in.tradingview.com/chart/?symbol=NSE:AXISBANK)<br><sub>↓CMF17d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 5 | ↓43 | ↑0.988 | ↓36d | — | -2.5% | -58.03/-58.94 | +1.01% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,###WATCHLIST,NSE:VTL,NSE:AXISBANK
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (16)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [FUSION](https://in.tradingview.com/chart/?symbol=NSE:FUSION)<br><sub>📶W9 · 🚀SS · ↓CMF5d</sub> | ✓ SAFE | Microfinance loans for rural women entrepreneurs | 📈 BULL_ANY_MID | 59 | 🔄68 | ↑1.014 | ↑1d | — | +2.5% | -16.57/-18.51 | +2.51% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄83 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [STYL](https://in.tradingview.com/chart/?symbol=NSE:STYL)<br><sub>📶W9 · ↑CMF29d</sub> | ✓ SAFE | Secure payment solutions provider for Indian BFSI sector | 📈 BULL_ANY_MID | 49 | 🔄50 | ↑1.058 | ↑1d | — | +6.8% | 17.0/11.46 | +6.75% | 20% |
| [PARADEEP](https://in.tradingview.com/chart/?symbol=NSE:PARADEEP)<br><sub>📶W9 · W↑94d · ↑CMF7d</sub> | ✓ SAFE | Phosphatic fertilizers manufacturer for Indian agriculture sector | 📈 BULL_ANY_MID | 47 | 🔄41 | ↑1.018 | ↑8d | — | +10.0% | 23.7/22.14 | +0.97% | 20% |
| [DIXON](https://in.tradingview.com/chart/?symbol=NSE:DIXON)<br><sub>📶W9 · W↑99d · ↑CMF15d</sub> | ✓ SAFE | Electronics manufacturing services for consumer appliances and lighting | 📈 BULL_ANY_MID | 17 | ↑68 | ↓1.009 | ↑3d | — | +2.2% | 43.04/39.75 | -0.77% | 20% |
| [ULTRACEMCO](https://in.tradingview.com/chart/?symbol=NSE:ULTRACEMCO)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 15 | ↑41 | ↑1.010 | ↑15d | — | +5.6% | 51.42/48.64 | +0.28% | 20% |
| [LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS)<br><sub>📶W9 · W↑19d · ↑CMF16d</sub> | ✓ SAFE | Engineering design development testing services global | 📈 BULL_ANY_MID | 8 | ↑24 | ↓1.010 | ↑12d | — | +7.5% | 43.24/42.45 | -0.56% | 20% |
| [AURUM](https://in.tradingview.com/chart/?symbol=NSE:AURUM)<br><sub>📶W9 · ↓CMF15d</sub> | ✓ SAFE | Real estate software platform, rental and sales digitization | 📈 BULL_ANY_MID | 0 | ↓77 | ↓1.002 | ↓40d | — | +22.2% | -12.42/-13.08 | -0.18% | 20% |
| [NTPCGREEN](https://in.tradingview.com/chart/?symbol=NSE:NTPCGREEN)<br><sub>🚀SS · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Solar and wind power generation projects for utilities | 📈 BULL_ANY_MID | 14 | ↓21 | ↑0.998 | ↓11d | — | +0.0% | -44.26/-45.39 | +0.74% | 20% |
| [JINDALPOLY](https://in.tradingview.com/chart/?symbol=NSE:JINDALPOLY)<br><sub>↓CMF26d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 11 | ↓62 | ↑0.998 | ↓14d | — | -4.0% | -36.76/-38.14 | +1.01% | 20% |
| [RAMCOIND](https://in.tradingview.com/chart/?symbol=NSE:RAMCOIND)<br><sub>↓CMF3d</sub> | ✓ SAFE | Fiber cement sheets, calcium silicate boards, cotton yarn | 📈 BULL_ANY_MID | 10 | ↓61 | ↑1.001 | ↓34d | — | +14.7% | -19.12/-19.15 | +0.94% | 20% |
| [TMPV](https://in.tradingview.com/chart/?symbol=NSE:TMPV)<br><sub>🚀SS · ↓CMF29d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓17 | ↑0.999 | ↓33d | — | -12.4% | -49.04/-51.5 | +1.53% | 20% |
| [SHAKTIPUMP](https://in.tradingview.com/chart/?symbol=NSE:SHAKTIPUMP)<br><sub>🚀SS · ↓CMF23d</sub> | ✓ SAFE | Solar submersible pumps agriculture irrigation water supply | 📈 BULL_ANY_MID | 5 | ↓6 | ↑0.986 | ↓21d | — | -8.6% | -46.83/-46.86 | -0.18% | 20% |
| [MSTCLTD](https://in.tradingview.com/chart/?symbol=NSE:MSTCLTD)<br><sub>🚀SS · ↓CMF17d</sub> | ✓ SAFE | Steel scrap trading, e-commerce, government procurement auctions | 📈 BULL_ANY_MID | 5 | ↓82 | ↑0.996 | ↓53d | — | +40.7% | -25.87/-26.04 | +0.55% | 10% 🟨 |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>↓CMF8d</sub> | ✓ SAFE | Pharmaceutical intermediates and specialty chemicals manufacturer | 📈 BULL_ANY_MID | 1 | ↓95 | ↓0.994 | ↓19d | — | -4.1% | -20.74/-22.12 | -0.68% | 20% |
| [GRANULES](https://in.tradingview.com/chart/?symbol=NSE:GRANULES)<br><sub>↓CMF8d</sub> | ✓ SAFE | APIs, PFIs, finished drugs manufacturing pharma | 📈 BULL_ANY_MID | 0 | ↓88 | ↓0.997 | ↓29d | — | +9.7% | -13.4/-13.62 | -0.76% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,###WATCHLIST,NSE:FUSION,NSE:OFSS,NSE:STYL,NSE:PARADEEP,NSE:DIXON,NSE:ULTRACEMCO,NSE:LTTS,NSE:AURUM,NSE:NTPCGREEN,NSE:JINDALPOLY,NSE:RAMCOIND,NSE:TMPV,NSE:SHAKTIPUMP,NSE:MSTCLTD,NSE:ACUTAAS,NSE:GRANULES
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
