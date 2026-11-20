> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-11-20
*Generated 2026-11-20 15:47 IST*

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

**Total bull crosses today: 71** · 20 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:COFORGE,NSE:EIHOTEL,NSE:NH,NSE:JLHL,NSE:PGEL,NSE:ICICIGI,NSE:KRBL,NSE:SHREECEM,NSE:JAYBARMARU,NSE:ASTERDM,NSE:SIGMAADV,NSE:STEELCAS,NSE:RATNAVEER,NSE:AFFLE,NSE:POWERMECH,NSE:CELLO,NSE:TATACONSUM,NSE:RUBICON,NSE:BALKRISIND,NSE:PROTEAN,NSE:FRACTAL,NSE:SMARTWORKS,NSE:SANSERA,NSE:EICHERMOT,NSE:NBCC,NSE:ASIANHOTNR,NSE:V2RETAIL,NSE:OAL,NSE:KIRLOSBROS,NSE:EPACK,NSE:VOLTAMP,NSE:SCHNEIDER,NSE:RPTECH,NSE:PUNJABCHEM,NSE:BHAGCHEM,NSE:3MINDIA,NSE:EMIL,NSE:BHARATFORG,NSE:PARADEEP,NSE:THEJO,NSE:LUPIN,NSE:GRANULES,NSE:TENNIND,NSE:BRIGHOTEL,NSE:NTPCGREEN,NSE:GANDHITUBE,NSE:IRISDOREME,NSE:VOEPL,NSE:EQUITASBNK,NSE:CAPILLARY,NSE:SUVEN,NSE:INDIANHUME,NSE:KALPATARU,NSE:BIRLACORPN,NSE:NESCO,NSE:DOLATALGO,NSE:HSCL,NSE:ACCELYA,NSE:TEXRAIL,NSE:DECNGOLD,NSE:RELIGARE,NSE:RAILTEL,NSE:SUMICHEM,NSE:KAPSTON,NSE:JSWINFRA,NSE:HIKAL,NSE:STARCEMENT,NSE:ASTRAL,NSE:BANARISUG,NSE:RHIM,NSE:RPGLIFE
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (25)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>📶W9 · W↑30d · ↑CMF18d</sub> | ✓ SAFE | IT services, digital transformation, financial and travel sectors | ⚡ BULL_ANY_PPV | 91 | 🔄87 | ↑1.020 | ↑4d | SQ·PV | +3.8% | 39.06/31.58 | +2.24% | 20% |
| [EIHOTEL](https://in.tradingview.com/chart/?symbol=NSE:EIHOTEL)<br><sub>📶W9 · W↑15d · RVOL19x · ↑CMF1d</sub> | ⚠ CAUTION | Luxury hotels, resorts, flight catering operations | ⚡ BULL_ANY_PPV | 35 | 🔄65 | ↑1.063 | ↑15d | PV | +16.7% | 44.52/39.54 | +7.79% | 20% |
| [NH](https://in.tradingview.com/chart/?symbol=NSE:NH)<br><sub>📶W9 · W↑15d · ↑CMF18d</sub> | ⚠ CAUTION | Affordable cardiac surgery and multispecialty hospitals across India | ⚡ BULL_ANY_PPV | 31 | 🔄59 | ↑1.030 | ↑19d | PV | +16.9% | 34.94/32.46 | +3.77% | 20% |
| [JLHL](https://in.tradingview.com/chart/?symbol=NSE:JLHL)<br><sub>📶W9 · W↑25d · RVOL181x · ↑CMF12d</sub> | ✓ SAFE | Tertiary hospital chain Mumbai west India multi-specialty care | ⚡ BULL_ANY_PPV | 30 | 🔄1 | ↑1.093 | ↑26d | PV | +34.0% | 49.87/45.41 | +12.87% | 20% |
| [PGEL](https://in.tradingview.com/chart/?symbol=NSE:PGEL)<br><sub>📶W9 · W↑15d · ↑CMF18d</sub> | ✓ SAFE | Plastic injection moulding electronics manufacturing services provider | ⚡ BULL_ANY_PPV | 18 | ↑64 | ↑1.056 | ↑2d | PV | +9.2% | 31.08/24.44 | +1.81% | 20% |
| [ICICIGI](https://in.tradingview.com/chart/?symbol=NSE:ICICIGI)<br><sub>📶W9 · W↑40d · ↑CMF6d</sub> | ⚠ CAUTION | Motor and health insurance for Indian retail customers | ⚡ BULL_ANY_PPV | 18 | ↑50 | ↑1.033 | ↑2d | PV | +5.4% | 37.89/35.58 | +2.84% | 20% |
| [KRBL](https://in.tradingview.com/chart/?symbol=NSE:KRBL)<br><sub>📶W9 · W↑9d · ↑CMF13d</sub> | ✓ SAFE | Basmati rice processing and export for domestic and global markets | ⚡ BULL_ANY_PPV | 6 | ↑67 | ↑1.038 | ↑14d | PV | +18.7% | 29.58/26.66 | +2.24% | 20% |
| [SHREECEM](https://in.tradingview.com/chart/?symbol=NSE:SHREECEM)<br><sub>📶W9 · W↑20d · ↑CMF19d</sub> | ⚠ CAUTION | Cement manufacturer, lowest cost producer, construction materials | ⚡ BULL_ANY_PPV | 5 | ↑53 | ↑1.023 | ↑29d | PV | +16.5% | 54.94/54.88 | +1.43% | 20% |
| [JAYBARMARU](https://in.tradingview.com/chart/?symbol=NSE:JAYBARMARU)<br><sub>📶W9 · W↑9d · ↓CMF13d</sub> | ✓ SAFE | Auto parts supplier to Maruti Suzuki passenger vehicles | ⚡ BULL_ANY_PPV | 5 | ↑79 | ↑1.039 | ↑15d | PV | +12.6% | 28.74/21.47 | +3.82% | 20% |
| [ASTERDM](https://in.tradingview.com/chart/?symbol=NSE:ASTERDM)<br><sub>📶W9 · W↑9d · ↑CMF4d</sub> | ✓ SAFE | Multi-specialty hospitals and clinics, India healthcare | ⚡ BULL_ANY_PPV | 2 | ↑69 | ↑1.056 | ↑18d | PV | +17.6% | 43.2/38.89 | +5.41% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [STEELCAS](https://in.tradingview.com/chart/?symbol=NSE:STEELCAS)<br><sub>📶W9 · W↑9d · ★ · ↑CMF19d</sub> | ⚠ CAUTION | Steel alloy castings for heavy engineering OEMs | 📈 BULL_ANY_MID | 58 | ↓89 | ↓1.000 | ↑2d | SQ | +3.8% | 23.72/21.82 | -4.50% | 20% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · 🚀SS · ↓CMF0d · DEL59%(T-1)</sub> | ✓ SAFE | Stainless steel washers tubes pipes solar mounting components | 📈 BULL_ANY_MID | 57 | 🔄98 | ↑1.009 | ↑3d | — | +3.1% | 30.35/28.97 | +0.86% | 20% |
| [AFFLE](https://in.tradingview.com/chart/?symbol=NSE:AFFLE)<br><sub>📶W9 · W↑9d · ↑CMF14d</sub> | ✓ SAFE | Mobile ads, consumer intelligence platform, marketing tech | 📈 BULL_ANY_MID | 45 | 🔄53 | ↑1.011 | ↑15d | — | +19.2% | 22.56/22.08 | +0.54% | 20% |
| [POWERMECH](https://in.tradingview.com/chart/?symbol=NSE:POWERMECH)<br><sub>📶W9 · W↑9d · ↓CMF26d · DEL73%(T-1)</sub> | ✓ SAFE | EPC services boilers turbines power plants infrastructure | 📈 BULL_ANY_MID | 42 | 🔄55 | ↑1.020 | ↑13d | — | +9.3% | 22.86/21.93 | +3.07% | 20% |
| [CELLO](https://in.tradingview.com/chart/?symbol=NSE:CELLO)<br><sub>📶W9 · W↑35d · ↑CMF0d</sub> | ✓ SAFE | Writing instruments stationery housewares molded furniture consumer products | 📈 BULL_ANY_MID | 42 | 🔄38 | ↑1.018 | ↑13d | — | +8.1% | 21.19/19.19 | +1.68% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄56 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · W↑9d · ★ · ↑CMF20d</sub> | ✓ SAFE | Complex generics and specialty formulations for global pharma | 📈 BULL_ANY_MID | 18 | ↑96 | ↓1.015 | ↑2d | — | +3.6% | 23.16/20.41 | -0.21% | 20% |
| [BALKRISIND](https://in.tradingview.com/chart/?symbol=NSE:BALKRISIND)<br><sub>📶W9 · W↑15d · ↑CMF21d</sub> | ⚠ CAUTION | Off-highway tires for agriculture construction mining sectors | 📈 BULL_ANY_MID | 10 | ↑58 | ↑1.024 | ↑15d | — | +14.1% | 44.06/43.68 | +1.57% | 20% |
| [PROTEAN](https://in.tradingview.com/chart/?symbol=NSE:PROTEAN)<br><sub>📶W9 · W↑45d · ↑CMF9d</sub> | ✓ SAFE | Digital governance infrastructure software, government services, citizens | 📈 BULL_ANY_MID | 7 | ↑74 | ↓1.025 | ↑13d | — | +15.5% | 40.69/39.46 | -0.91% | 10% 🟨 |
| [FRACTAL](https://in.tradingview.com/chart/?symbol=NSE:FRACTAL)<br><sub>📶W9 · ↑CMF26d</sub> | ✓ SAFE | AI analytics solutions for global Fortune 500 enterprises | 📈 BULL_ANY_MID | 7 | ↑50 | ↓1.018 | ↑13d | — | +16.6% | 35.81/34.37 | -0.38% | 20% |
| [SMARTWORKS](https://in.tradingview.com/chart/?symbol=NSE:SMARTWORKS)<br><sub>📶W9 · W↑9d · ↓CMF30d</sub> | ✓ SAFE | Managed workspace solutions for enterprises and GCCs | 📈 BULL_ANY_MID | 7 | ↑65 | ↑1.020 | ↑18d | — | +10.9% | 35.92/33.75 | +1.06% | 20% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>📶W9 · W↑9d · ↑CMF8d</sub> | ✓ SAFE | Precision forged machined components two-wheeler four-wheeler OEM | 📈 BULL_ANY_MID | 6 | ↑98 | ↑1.038 | ↑14d | — | +15.4% | 46.27/45.65 | +1.64% | 20% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>📶W9 · W↑11d · ↑CMF13d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓61 | ↓1.007 | ↑15d | — | +7.0% | 46.27/45.57 | -0.67% | 20% |
| [NBCC](https://in.tradingview.com/chart/?symbol=NSE:NBCC)<br><sub>📶W9 · W↑15d · ↑CMF12d</sub> | ✓ SAFE | Government construction and engineering for infrastructure projects | 📈 BULL_ANY_MID | 5 | ↑16 | ↓1.013 | ↑15d | — | +14.3% | 17.95/16.51 | +0.13% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:COFORGE,NSE:EIHOTEL,NSE:NH,NSE:JLHL,NSE:PGEL,NSE:ICICIGI,NSE:KRBL,NSE:SHREECEM,NSE:JAYBARMARU,NSE:ASTERDM,NSE:SIGMAADV,NSE:STEELCAS,NSE:RATNAVEER,NSE:AFFLE,NSE:POWERMECH,NSE:CELLO,NSE:TATACONSUM,NSE:RUBICON,NSE:BALKRISIND,NSE:PROTEAN,NSE:FRACTAL,NSE:SMARTWORKS,NSE:SANSERA,NSE:EICHERMOT,NSE:NBCC
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (41)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>📶W9 · W↑30d · ↑CMF18d</sub> | ✓ SAFE | IT services, digital transformation, financial and travel sectors | ⚡ BULL_ANY_PPV | 91 | 🔄87 | ↑1.020 | ↑4d | SQ·PV | +3.8% | 39.06/31.58 | +2.24% | 20% |
| [EIHOTEL](https://in.tradingview.com/chart/?symbol=NSE:EIHOTEL)<br><sub>📶W9 · W↑15d · RVOL19x · ↑CMF1d</sub> | ⚠ CAUTION | Luxury hotels, resorts, flight catering operations | ⚡ BULL_ANY_PPV | 35 | 🔄65 | ↑1.063 | ↑15d | PV | +16.7% | 44.52/39.54 | +7.79% | 20% |
| [NH](https://in.tradingview.com/chart/?symbol=NSE:NH)<br><sub>📶W9 · W↑15d · ↑CMF18d</sub> | ⚠ CAUTION | Affordable cardiac surgery and multispecialty hospitals across India | ⚡ BULL_ANY_PPV | 31 | 🔄59 | ↑1.030 | ↑19d | PV | +16.9% | 34.94/32.46 | +3.77% | 20% |
| [JLHL](https://in.tradingview.com/chart/?symbol=NSE:JLHL)<br><sub>📶W9 · W↑25d · RVOL181x · ↑CMF12d</sub> | ✓ SAFE | Tertiary hospital chain Mumbai west India multi-specialty care | ⚡ BULL_ANY_PPV | 30 | 🔄1 | ↑1.093 | ↑26d | PV | +34.0% | 49.87/45.41 | +12.87% | 20% |
| [PGEL](https://in.tradingview.com/chart/?symbol=NSE:PGEL)<br><sub>📶W9 · W↑15d · ↑CMF18d</sub> | ✓ SAFE | Plastic injection moulding electronics manufacturing services provider | ⚡ BULL_ANY_PPV | 18 | ↑64 | ↑1.056 | ↑2d | PV | +9.2% | 31.08/24.44 | +1.81% | 20% |
| [ICICIGI](https://in.tradingview.com/chart/?symbol=NSE:ICICIGI)<br><sub>📶W9 · W↑40d · ↑CMF6d</sub> | ⚠ CAUTION | Motor and health insurance for Indian retail customers | ⚡ BULL_ANY_PPV | 18 | ↑50 | ↑1.033 | ↑2d | PV | +5.4% | 37.89/35.58 | +2.84% | 20% |
| [KRBL](https://in.tradingview.com/chart/?symbol=NSE:KRBL)<br><sub>📶W9 · W↑9d · ↑CMF13d</sub> | ✓ SAFE | Basmati rice processing and export for domestic and global markets | ⚡ BULL_ANY_PPV | 6 | ↑67 | ↑1.038 | ↑14d | PV | +18.7% | 29.58/26.66 | +2.24% | 20% |
| [SHREECEM](https://in.tradingview.com/chart/?symbol=NSE:SHREECEM)<br><sub>📶W9 · W↑20d · ↑CMF19d</sub> | ⚠ CAUTION | Cement manufacturer, lowest cost producer, construction materials | ⚡ BULL_ANY_PPV | 5 | ↑53 | ↑1.023 | ↑29d | PV | +16.5% | 54.94/54.88 | +1.43% | 20% |
| [JAYBARMARU](https://in.tradingview.com/chart/?symbol=NSE:JAYBARMARU)<br><sub>📶W9 · W↑9d · ↓CMF13d</sub> | ✓ SAFE | Auto parts supplier to Maruti Suzuki passenger vehicles | ⚡ BULL_ANY_PPV | 5 | ↑79 | ↑1.039 | ↑15d | PV | +12.6% | 28.74/21.47 | +3.82% | 20% |
| [ASTERDM](https://in.tradingview.com/chart/?symbol=NSE:ASTERDM)<br><sub>📶W9 · W↑9d · ↑CMF4d</sub> | ✓ SAFE | Multi-specialty hospitals and clinics, India healthcare | ⚡ BULL_ANY_PPV | 2 | ↑69 | ↑1.056 | ↑18d | PV | +17.6% | 43.2/38.89 | +5.41% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · 🚀SS · ↓CMF0d · DEL59%(T-1)</sub> | ✓ SAFE | Stainless steel washers tubes pipes solar mounting components | 📈 BULL_ANY_MID | 57 | 🔄98 | ↑1.009 | ↑3d | — | +3.1% | 30.35/28.97 | +0.86% | 20% |
| [AFFLE](https://in.tradingview.com/chart/?symbol=NSE:AFFLE)<br><sub>📶W9 · W↑9d · ↑CMF14d</sub> | ✓ SAFE | Mobile ads, consumer intelligence platform, marketing tech | 📈 BULL_ANY_MID | 45 | 🔄53 | ↑1.011 | ↑15d | — | +19.2% | 22.56/22.08 | +0.54% | 20% |
| [POWERMECH](https://in.tradingview.com/chart/?symbol=NSE:POWERMECH)<br><sub>📶W9 · W↑9d · ↓CMF26d · DEL73%(T-1)</sub> | ✓ SAFE | EPC services boilers turbines power plants infrastructure | 📈 BULL_ANY_MID | 42 | 🔄55 | ↑1.020 | ↑13d | — | +9.3% | 22.86/21.93 | +3.07% | 20% |
| [CELLO](https://in.tradingview.com/chart/?symbol=NSE:CELLO)<br><sub>📶W9 · W↑35d · ↑CMF0d</sub> | ✓ SAFE | Writing instruments stationery housewares molded furniture consumer products | 📈 BULL_ANY_MID | 42 | 🔄38 | ↑1.018 | ↑13d | — | +8.1% | 21.19/19.19 | +1.68% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄56 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · W↑9d · ★ · ↑CMF20d</sub> | ✓ SAFE | Complex generics and specialty formulations for global pharma | 📈 BULL_ANY_MID | 18 | ↑96 | ↓1.015 | ↑2d | — | +3.6% | 23.16/20.41 | -0.21% | 20% |
| [BALKRISIND](https://in.tradingview.com/chart/?symbol=NSE:BALKRISIND)<br><sub>📶W9 · W↑15d · ↑CMF21d</sub> | ⚠ CAUTION | Off-highway tires for agriculture construction mining sectors | 📈 BULL_ANY_MID | 10 | ↑58 | ↑1.024 | ↑15d | — | +14.1% | 44.06/43.68 | +1.57% | 20% |
| [PROTEAN](https://in.tradingview.com/chart/?symbol=NSE:PROTEAN)<br><sub>📶W9 · W↑45d · ↑CMF9d</sub> | ✓ SAFE | Digital governance infrastructure software, government services, citizens | 📈 BULL_ANY_MID | 7 | ↑74 | ↓1.025 | ↑13d | — | +15.5% | 40.69/39.46 | -0.91% | 10% 🟨 |
| [FRACTAL](https://in.tradingview.com/chart/?symbol=NSE:FRACTAL)<br><sub>📶W9 · ↑CMF26d</sub> | ✓ SAFE | AI analytics solutions for global Fortune 500 enterprises | 📈 BULL_ANY_MID | 7 | ↑50 | ↓1.018 | ↑13d | — | +16.6% | 35.81/34.37 | -0.38% | 20% |
| [SMARTWORKS](https://in.tradingview.com/chart/?symbol=NSE:SMARTWORKS)<br><sub>📶W9 · W↑9d · ↓CMF30d</sub> | ✓ SAFE | Managed workspace solutions for enterprises and GCCs | 📈 BULL_ANY_MID | 7 | ↑65 | ↑1.020 | ↑18d | — | +10.9% | 35.92/33.75 | +1.06% | 20% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>📶W9 · W↑9d · ↑CMF8d</sub> | ✓ SAFE | Precision forged machined components two-wheeler four-wheeler OEM | 📈 BULL_ANY_MID | 6 | ↑98 | ↑1.038 | ↑14d | — | +15.4% | 46.27/45.65 | +1.64% | 20% |
| [NBCC](https://in.tradingview.com/chart/?symbol=NSE:NBCC)<br><sub>📶W9 · W↑15d · ↑CMF12d</sub> | ✓ SAFE | Government construction and engineering for infrastructure projects | 📈 BULL_ANY_MID | 5 | ↑16 | ↓1.013 | ↑15d | — | +14.3% | 17.95/16.51 | +0.13% | 20% |
| [V2RETAIL](https://in.tradingview.com/chart/?symbol=NSE:V2RETAIL)<br><sub>W↑9d · ↑CMF2d · ÷DIV</sub> | ✓ SAFE | Value retail apparel non-apparel Tier II III cities | ⚡ BULL_ANY_PPV | 54 | 🔄7 | ↑1.024 | ↑1d | PV | +3.0% | -18.5/-19.17 | +2.99% | 20% |
| [OAL](https://in.tradingview.com/chart/?symbol=NSE:OAL)<br><sub>RVOL120x · ↑CMF0d · DEL64%(T-1)</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 49 | 🔄94 | ↑1.074 | ↑1d | PV | +20.0% | -43.31/-45.54 | +20.00% | 20% 🟦 |
| [EPACK](https://in.tradingview.com/chart/?symbol=NSE:EPACK)<br><sub>W↑9d · ↑CMF19d</sub> | ✓ SAFE | AC manufacturing ODM, consumer durables, Indian domestic market | ⚡ BULL_ANY_PPV | 18 | ↑7 | ↑1.051 | ↑2d | PV | +14.2% | -31.31/-41.45 | +3.22% | 20% |
| [BHARATFORG](https://in.tradingview.com/chart/?symbol=NSE:BHARATFORG)<br><sub>↑CMF19d</sub> | ✓ SAFE | Forged components for automotive aerospace defence railways | 📈 BULL_ANY_MID | 99 | 🔄48 | ↑1.009 | ↑1d | SQ | +1.2% | -40.07/-41.61 | +1.20% | 20% |
| [PARADEEP](https://in.tradingview.com/chart/?symbol=NSE:PARADEEP)<br><sub>↑CMF17d</sub> | ✓ SAFE | Phosphate fertilizer manufacturer for Indian agriculture sector | 📈 BULL_ANY_MID | 99 | 🔄52 | ↑1.014 | ↑1d | SQ | +3.1% | -8.47/-9.06 | +3.11% | 20% |
| [THEJO](https://in.tradingview.com/chart/?symbol=NSE:THEJO)<br><sub>🚀SS · ↑CMF7d</sub> | ⚠ CAUTION | Bulk material handling, mineral processing, corrosion protection equipment | 📈 BULL_ANY_MID | 99 | 🔄73 | ↑1.014 | ↑1d | SQ | +2.3% | 8.39/5.92 | +2.33% | 20% |
| [LUPIN](https://in.tradingview.com/chart/?symbol=NSE:LUPIN)<br><sub>W↑9d · ↑CMF20d</sub> | ⚠ CAUTION | Branded generics, APIs, biotechnology for global pharma markets | 📈 BULL_ANY_MID | 98 | 🔄40 | ↑1.011 | ↑2d | SQ | +2.1% | 1.09/-2.15 | +0.76% | 20% |
| [GRANULES](https://in.tradingview.com/chart/?symbol=NSE:GRANULES)<br><sub>↑CMF10d</sub> | ✓ SAFE | APIs, formulation intermediates, finished pharma drugs manufacturer | 📈 BULL_ANY_MID | 94 | 🔄79 | ↑1.016 | ↑1d | SQ | +2.7% | -12.39/-15.52 | +2.68% | 20% |
| [TENNIND](https://in.tradingview.com/chart/?symbol=NSE:TENNIND)<br><sub>W↑5d · ↓CMF10d</sub> | ✓ SAFE | Automotive emissions control systems supplier for passenger vehicles | 📈 BULL_ANY_MID | 94 | 🔄21 | ↑1.028 | ↑1d | SQ | +4.3% | -21.19/-24.87 | +4.35% | 20% |
| [BRIGHOTEL](https://in.tradingview.com/chart/?symbol=NSE:BRIGHOTEL)<br><sub>W↑9d · ↑CMF1d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 94 | 🔄30 | ↑1.025 | ↑1d | SQ | +3.7% | 8.74/3.76 | +3.71% | 20% |
| [IRISDOREME](https://in.tradingview.com/chart/?symbol=NSE:IRISDOREME)<br><sub>★ · ↓CMF6d · ⚠️TRAP</sub> | ⚠ CAUTION | Infant children apparel manufacturer integrated production India | 📈 BULL_ANY_MID | 68 | ↑91 | ↑1.009 | ↑2d | SQ | +3.7% | -22.72/-28.7 | +0.35% | 20% |
| [EQUITASBNK](https://in.tradingview.com/chart/?symbol=NSE:EQUITASBNK)<br><sub>↑CMF15d</sub> | ✓ SAFE | Small finance bank serving underbanked individuals and SMEs | 📈 BULL_ANY_MID | 59 | 🔄16 | ↑1.012 | ↑1d | — | +3.0% | -29.3/-30.96 | +2.96% | 20% |
| [CAPILLARY](https://in.tradingview.com/chart/?symbol=NSE:CAPILLARY)<br><sub>↓CMF21d</sub> | ✓ SAFE | AI loyalty platforms serve enterprise retail globally | 📈 BULL_ANY_MID | 59 | 🔄50 | ↑1.012 | ↑1d | — | +2.4% | -33.11/-36.38 | +2.38% | 20% |
| [BIRLACORPN](https://in.tradingview.com/chart/?symbol=NSE:BIRLACORPN)<br><sub>W↑15d · ↑CMF7d</sub> | ⚠ CAUTION | Cement manufacturing, jute goods, steel castings producer | 📈 BULL_ANY_MID | 45 | 🔄23 | ↑1.011 | ↑15d | — | +7.5% | 24.48/21.93 | +0.77% | 20% |
| [NESCO](https://in.tradingview.com/chart/?symbol=NSE:NESCO)<br><sub>W↑9d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | IT parks, exhibitions, industrial machinery manufacturing, Mumbai | 📈 BULL_ANY_MID | 45 | 🔄45 | ↑1.010 | ↑15d | — | +7.4% | 25.43/23.24 | +0.38% | 20% |
| [DOLATALGO](https://in.tradingview.com/chart/?symbol=NSE:DOLATALGO)<br><sub>W↑15d · ↑CMF13d</sub> | ⚠ CAUTION | Algorithmic trading platform and liquidity provision NSE member | 📈 BULL_ANY_MID | 45 | ↑28 | ↓1.017 | ↑15d | SQ | +7.9% | 35.2/33.62 | +0.13% | 20% |
| [TEXRAIL](https://in.tradingview.com/chart/?symbol=NSE:TEXRAIL)<br><sub>W↑5d · ↑CMF1d</sub> | ✓ SAFE | Railway rolling stock manufacturing and hydro-mechanical equipment | 📈 BULL_ANY_MID | 20 | ↑53 | ↑1.014 | ↑10d | — | +6.1% | 22.59/21.98 | +0.37% | 20% |
| [RELIGARE](https://in.tradingview.com/chart/?symbol=NSE:RELIGARE)<br><sub>W↑9d · ↑CMF6d</sub> | ✓ SAFE | Diversified financials: insurance, broking, SME lending platform | 📈 BULL_ANY_MID | 18 | ↑54 | ↓1.012 | ↑2d | — | +3.8% | 13.1/11.39 | -0.38% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:COFORGE,NSE:EIHOTEL,NSE:NH,NSE:JLHL,NSE:PGEL,NSE:ICICIGI,NSE:KRBL,NSE:SHREECEM,NSE:JAYBARMARU,NSE:ASTERDM,NSE:SIGMAADV,NSE:RATNAVEER,NSE:AFFLE,NSE:POWERMECH,NSE:CELLO,NSE:TATACONSUM,NSE:RUBICON,NSE:BALKRISIND,NSE:PROTEAN,NSE:FRACTAL,NSE:SMARTWORKS,NSE:SANSERA,NSE:NBCC,NSE:V2RETAIL,NSE:OAL,NSE:EPACK,NSE:BHARATFORG,NSE:PARADEEP,NSE:THEJO,NSE:LUPIN,NSE:GRANULES,NSE:TENNIND,NSE:BRIGHOTEL,NSE:IRISDOREME,NSE:EQUITASBNK,NSE:CAPILLARY,NSE:BIRLACORPN,NSE:NESCO,NSE:DOLATALGO,NSE:TEXRAIL,NSE:RELIGARE
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (20)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>📶W9 · W↑30d · ↑CMF18d</sub> | ✓ SAFE | IT services, digital transformation, financial and travel sectors | ⚡ BULL_ANY_PPV | 91 | 🔄87 | ↑1.020 | ↑4d | SQ·PV | +3.8% | 39.06/31.58 | +2.24% | 20% |
| [STEELCAS](https://in.tradingview.com/chart/?symbol=NSE:STEELCAS)<br><sub>📶W9 · W↑9d · ★ · ↑CMF19d</sub> | ⚠ CAUTION | Steel alloy castings for heavy engineering OEMs | 📈 BULL_ANY_MID | 58 | ↓89 | ↓1.000 | ↑2d | SQ | +3.8% | 23.72/21.82 | -4.50% | 20% |
| [ASIANHOTNR](https://in.tradingview.com/chart/?symbol=NSE:ASIANHOTNR)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Luxury hotel operations, Delhi, high-end accommodation | ⚡ BULL_ANY_PPV | 69 | ↓56 | ↑1.003 | ↑1d | SQ·PV | +1.8% | -11.25/-11.58 | +1.80% | 20% |
| [VOLTAMP](https://in.tradingview.com/chart/?symbol=NSE:VOLTAMP)<br><sub>↑CMF0d · 🎯SLING</sub> | ✓ SAFE | Power and distribution transformers for industrial infrastructure | 🟢 BULL_OVERSOLD | 54 | ↓60 | ↑1.001 | ↓16d | SQ | -4.4% | -56.75/-60.18 | +0.83% | 20% |
| [3MINDIA](https://in.tradingview.com/chart/?symbol=NSE:3MINDIA)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Science-based diversified products safety industrial healthcare consumer | 🟡 BULL_OS_L2 | 50 | ↓17 | ↑1.000 | ↓46d | SQ | -13.1% | -51.4/-53.69 | +0.91% | 20% |
| [BHARATFORG](https://in.tradingview.com/chart/?symbol=NSE:BHARATFORG)<br><sub>↑CMF19d</sub> | ✓ SAFE | Forged components for automotive aerospace defence railways | 📈 BULL_ANY_MID | 99 | 🔄48 | ↑1.009 | ↑1d | SQ | +1.2% | -40.07/-41.61 | +1.20% | 20% |
| [PARADEEP](https://in.tradingview.com/chart/?symbol=NSE:PARADEEP)<br><sub>↑CMF17d</sub> | ✓ SAFE | Phosphate fertilizer manufacturer for Indian agriculture sector | 📈 BULL_ANY_MID | 99 | 🔄52 | ↑1.014 | ↑1d | SQ | +3.1% | -8.47/-9.06 | +3.11% | 20% |
| [THEJO](https://in.tradingview.com/chart/?symbol=NSE:THEJO)<br><sub>🚀SS · ↑CMF7d</sub> | ⚠ CAUTION | Bulk material handling, mineral processing, corrosion protection equipment | 📈 BULL_ANY_MID | 99 | 🔄73 | ↑1.014 | ↑1d | SQ | +2.3% | 8.39/5.92 | +2.33% | 20% |
| [LUPIN](https://in.tradingview.com/chart/?symbol=NSE:LUPIN)<br><sub>W↑9d · ↑CMF20d</sub> | ⚠ CAUTION | Branded generics, APIs, biotechnology for global pharma markets | 📈 BULL_ANY_MID | 98 | 🔄40 | ↑1.011 | ↑2d | SQ | +2.1% | 1.09/-2.15 | +0.76% | 20% |
| [GRANULES](https://in.tradingview.com/chart/?symbol=NSE:GRANULES)<br><sub>↑CMF10d</sub> | ✓ SAFE | APIs, formulation intermediates, finished pharma drugs manufacturer | 📈 BULL_ANY_MID | 94 | 🔄79 | ↑1.016 | ↑1d | SQ | +2.7% | -12.39/-15.52 | +2.68% | 20% |
| [TENNIND](https://in.tradingview.com/chart/?symbol=NSE:TENNIND)<br><sub>W↑5d · ↓CMF10d</sub> | ✓ SAFE | Automotive emissions control systems supplier for passenger vehicles | 📈 BULL_ANY_MID | 94 | 🔄21 | ↑1.028 | ↑1d | SQ | +4.3% | -21.19/-24.87 | +4.35% | 20% |
| [BRIGHOTEL](https://in.tradingview.com/chart/?symbol=NSE:BRIGHOTEL)<br><sub>W↑9d · ↑CMF1d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 94 | 🔄30 | ↑1.025 | ↑1d | SQ | +3.7% | 8.74/3.76 | +3.71% | 20% |
| [NTPCGREEN](https://in.tradingview.com/chart/?symbol=NSE:NTPCGREEN)<br><sub>↓CMF22d</sub> | ⚠ CAUTION | Solar and wind power projects for grid distribution | 📈 BULL_ANY_MID | 69 | ↓30 | ↑1.004 | ↑1d | SQ | +1.0% | -39.14/-39.96 | +0.96% | 20% |
| [GANDHITUBE](https://in.tradingview.com/chart/?symbol=NSE:GANDHITUBE)<br><sub>↑CMF2d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↓64 | ↑1.005 | ↑1d | SQ | +1.1% | -7.25/-10.02 | +1.08% | 20% |
| [IRISDOREME](https://in.tradingview.com/chart/?symbol=NSE:IRISDOREME)<br><sub>★ · ↓CMF6d · ⚠️TRAP</sub> | ⚠ CAUTION | Infant children apparel manufacturer integrated production India | 📈 BULL_ANY_MID | 68 | ↑91 | ↑1.009 | ↑2d | SQ | +3.7% | -22.72/-28.7 | +0.35% | 20% |
| [VOEPL](https://in.tradingview.com/chart/?symbol=NSE:VOEPL)<br><sub>↓CMF10d</sub> | ✓ SAFE | Optoelectronics OEM manufacturing consumer appliances electronics | 📈 BULL_ANY_MID | 64 | ↓50 | ↑1.003 | ↓6d | SQ | -0.7% | -37.37/-40.02 | +0.47% | 20% |
| [SUVEN](https://in.tradingview.com/chart/?symbol=NSE:SUVEN)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | CNS disorder drug development, clinical stage biotech | 📈 BULL_ANY_MID | 58 | ↓75 | ↓0.990 | ↓2d | SQ | +1.4% | -15.62/-16.47 | -2.71% | 20% |
| [INDIANHUME](https://in.tradingview.com/chart/?symbol=NSE:INDIANHUME)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↓16 | ↓0.995 | ↓2d | SQ | +2.2% | -47.35/-49.5 | -1.26% | 20% |
| [KALPATARU](https://in.tradingview.com/chart/?symbol=NSE:KALPATARU)<br><sub>W↑5d · RVOL17x · ↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Luxury residential real estate developer focused Mumbai MMR | 📈 BULL_ANY_MID | 57 | ↓12 | ↓0.989 | ↓3d | SQ | -1.0% | -5.3/-12.69 | -0.71% | 20% |
| [DOLATALGO](https://in.tradingview.com/chart/?symbol=NSE:DOLATALGO)<br><sub>W↑15d · ↑CMF13d</sub> | ⚠ CAUTION | Algorithmic trading platform and liquidity provision NSE member | 📈 BULL_ANY_MID | 45 | ↑28 | ↓1.017 | ↑15d | SQ | +7.9% | 35.2/33.62 | +0.13% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:COFORGE,NSE:STEELCAS,NSE:ASIANHOTNR,NSE:VOLTAMP,NSE:3MINDIA,NSE:BHARATFORG,NSE:PARADEEP,NSE:THEJO,NSE:LUPIN,NSE:GRANULES,NSE:TENNIND,NSE:BRIGHOTEL,NSE:NTPCGREEN,NSE:GANDHITUBE,NSE:IRISDOREME,NSE:VOEPL,NSE:SUVEN,NSE:INDIANHUME,NSE:KALPATARU,NSE:DOLATALGO
```

---

### 🔥 MAJOR — PPV confirmed (14)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [EIHOTEL](https://in.tradingview.com/chart/?symbol=NSE:EIHOTEL)<br><sub>📶W9 · W↑15d · RVOL19x · ↑CMF1d</sub> | ⚠ CAUTION | Luxury hotels, resorts, flight catering operations | ⚡ BULL_ANY_PPV | 35 | 🔄65 | ↑1.063 | ↑15d | PV | +16.7% | 44.52/39.54 | +7.79% | 20% |
| [NH](https://in.tradingview.com/chart/?symbol=NSE:NH)<br><sub>📶W9 · W↑15d · ↑CMF18d</sub> | ⚠ CAUTION | Affordable cardiac surgery and multispecialty hospitals across India | ⚡ BULL_ANY_PPV | 31 | 🔄59 | ↑1.030 | ↑19d | PV | +16.9% | 34.94/32.46 | +3.77% | 20% |
| [JLHL](https://in.tradingview.com/chart/?symbol=NSE:JLHL)<br><sub>📶W9 · W↑25d · RVOL181x · ↑CMF12d</sub> | ✓ SAFE | Tertiary hospital chain Mumbai west India multi-specialty care | ⚡ BULL_ANY_PPV | 30 | 🔄1 | ↑1.093 | ↑26d | PV | +34.0% | 49.87/45.41 | +12.87% | 20% |
| [PGEL](https://in.tradingview.com/chart/?symbol=NSE:PGEL)<br><sub>📶W9 · W↑15d · ↑CMF18d</sub> | ✓ SAFE | Plastic injection moulding electronics manufacturing services provider | ⚡ BULL_ANY_PPV | 18 | ↑64 | ↑1.056 | ↑2d | PV | +9.2% | 31.08/24.44 | +1.81% | 20% |
| [ICICIGI](https://in.tradingview.com/chart/?symbol=NSE:ICICIGI)<br><sub>📶W9 · W↑40d · ↑CMF6d</sub> | ⚠ CAUTION | Motor and health insurance for Indian retail customers | ⚡ BULL_ANY_PPV | 18 | ↑50 | ↑1.033 | ↑2d | PV | +5.4% | 37.89/35.58 | +2.84% | 20% |
| [KRBL](https://in.tradingview.com/chart/?symbol=NSE:KRBL)<br><sub>📶W9 · W↑9d · ↑CMF13d</sub> | ✓ SAFE | Basmati rice processing and export for domestic and global markets | ⚡ BULL_ANY_PPV | 6 | ↑67 | ↑1.038 | ↑14d | PV | +18.7% | 29.58/26.66 | +2.24% | 20% |
| [SHREECEM](https://in.tradingview.com/chart/?symbol=NSE:SHREECEM)<br><sub>📶W9 · W↑20d · ↑CMF19d</sub> | ⚠ CAUTION | Cement manufacturer, lowest cost producer, construction materials | ⚡ BULL_ANY_PPV | 5 | ↑53 | ↑1.023 | ↑29d | PV | +16.5% | 54.94/54.88 | +1.43% | 20% |
| [JAYBARMARU](https://in.tradingview.com/chart/?symbol=NSE:JAYBARMARU)<br><sub>📶W9 · W↑9d · ↓CMF13d</sub> | ✓ SAFE | Auto parts supplier to Maruti Suzuki passenger vehicles | ⚡ BULL_ANY_PPV | 5 | ↑79 | ↑1.039 | ↑15d | PV | +12.6% | 28.74/21.47 | +3.82% | 20% |
| [ASTERDM](https://in.tradingview.com/chart/?symbol=NSE:ASTERDM)<br><sub>📶W9 · W↑9d · ↑CMF4d</sub> | ✓ SAFE | Multi-specialty hospitals and clinics, India healthcare | ⚡ BULL_ANY_PPV | 2 | ↑69 | ↑1.056 | ↑18d | PV | +17.6% | 43.2/38.89 | +5.41% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [V2RETAIL](https://in.tradingview.com/chart/?symbol=NSE:V2RETAIL)<br><sub>W↑9d · ↑CMF2d · ÷DIV</sub> | ✓ SAFE | Value retail apparel non-apparel Tier II III cities | ⚡ BULL_ANY_PPV | 54 | 🔄7 | ↑1.024 | ↑1d | PV | +3.0% | -18.5/-19.17 | +2.99% | 20% |
| [OAL](https://in.tradingview.com/chart/?symbol=NSE:OAL)<br><sub>RVOL120x · ↑CMF0d · DEL64%(T-1)</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 49 | 🔄94 | ↑1.074 | ↑1d | PV | +20.0% | -43.31/-45.54 | +20.00% | 20% 🟦 |
| [KIRLOSBROS](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSBROS)<br><sub>↑CMF15d</sub> | ✓ SAFE | Pumps and fluid systems for water, power, irrigation | ⚡ BULL_ANY_PPV | 29 | ↓40 | ↑1.004 | ↑1d | PV | +2.3% | -40.61/-40.81 | +2.26% | 20% |
| [EPACK](https://in.tradingview.com/chart/?symbol=NSE:EPACK)<br><sub>W↑9d · ↑CMF19d</sub> | ✓ SAFE | AC manufacturing ODM, consumer durables, Indian domestic market | ⚡ BULL_ANY_PPV | 18 | ↑7 | ↑1.051 | ↑2d | PV | +14.2% | -31.31/-41.45 | +3.22% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:EIHOTEL,NSE:NH,NSE:JLHL,NSE:PGEL,NSE:ICICIGI,NSE:KRBL,NSE:SHREECEM,NSE:JAYBARMARU,NSE:ASTERDM,NSE:SIGMAADV,NSE:V2RETAIL,NSE:OAL,NSE:KIRLOSBROS,NSE:EPACK
```

### 🟢 OVERSOLD — reversal from −53/−60 (5)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SCHNEIDER](https://in.tradingview.com/chart/?symbol=NSE:SCHNEIDER)<br><sub>↓CMF8d · 🎯SLING</sub> | ✓ SAFE | Power distribution equipment manufacturing and servicing | 🟢 BULL_OVERSOLD | 12 | ↓59 | ↑0.999 | ↓13d | — | -8.5% | -62.38/-63.61 | +3.36% | 20% |
| [RPTECH](https://in.tradingview.com/chart/?symbol=NSE:RPTECH)<br><sub>↓CMF10d · ⚠️TRAP</sub> | ✓ SAFE | ICT distributor, IT peripherals, resellers and retailers | 🟢 BULL_OVERSOLD | 12 | ↓89 | ↑0.960 | ↓13d | — | -18.9% | -58.99/-60.46 | +0.15% | 20% |
| [PUNJABCHEM](https://in.tradingview.com/chart/?symbol=NSE:PUNJABCHEM)<br><sub>↓CMF13d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Agrochemicals pesticides fertilizers crop protection chemicals manufacturing | 🟢 BULL_OVERSOLD | 5 | ↓14 | ↑0.992 | ↓41d | — | -15.4% | -61.47/-61.56 | +2.10% | 20% |
| [BHAGCHEM](https://in.tradingview.com/chart/?symbol=NSE:BHAGCHEM)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Agrochemical technicals insecticides fungicides herbicides manufacturer | 🟢 BULL_OVERSOLD | 0 | ↓5 | ↓0.970 | ↓60d+ | — | -35.7% | -62.66/-63.19 | -1.51% | 20% |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL)<br><sub>↓CMF25d · ⚠️TRAP</sub> | ✓ SAFE | Consumer electronics retail chain South India operations | 🟡 BULL_OS_L2 | 5 | ↓60 | ↑0.973 | ↓47d | — | -23.9% | -55.38/-55.97 | -0.50% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SCHNEIDER,NSE:RPTECH,NSE:PUNJABCHEM,NSE:BHAGCHEM,NSE:EMIL
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (32)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · 🚀SS · ↓CMF0d · DEL59%(T-1)</sub> | ✓ SAFE | Stainless steel washers tubes pipes solar mounting components | 📈 BULL_ANY_MID | 57 | 🔄98 | ↑1.009 | ↑3d | — | +3.1% | 30.35/28.97 | +0.86% | 20% |
| [AFFLE](https://in.tradingview.com/chart/?symbol=NSE:AFFLE)<br><sub>📶W9 · W↑9d · ↑CMF14d</sub> | ✓ SAFE | Mobile ads, consumer intelligence platform, marketing tech | 📈 BULL_ANY_MID | 45 | 🔄53 | ↑1.011 | ↑15d | — | +19.2% | 22.56/22.08 | +0.54% | 20% |
| [POWERMECH](https://in.tradingview.com/chart/?symbol=NSE:POWERMECH)<br><sub>📶W9 · W↑9d · ↓CMF26d · DEL73%(T-1)</sub> | ✓ SAFE | EPC services boilers turbines power plants infrastructure | 📈 BULL_ANY_MID | 42 | 🔄55 | ↑1.020 | ↑13d | — | +9.3% | 22.86/21.93 | +3.07% | 20% |
| [CELLO](https://in.tradingview.com/chart/?symbol=NSE:CELLO)<br><sub>📶W9 · W↑35d · ↑CMF0d</sub> | ✓ SAFE | Writing instruments stationery housewares molded furniture consumer products | 📈 BULL_ANY_MID | 42 | 🔄38 | ↑1.018 | ↑13d | — | +8.1% | 21.19/19.19 | +1.68% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄56 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · W↑9d · ★ · ↑CMF20d</sub> | ✓ SAFE | Complex generics and specialty formulations for global pharma | 📈 BULL_ANY_MID | 18 | ↑96 | ↓1.015 | ↑2d | — | +3.6% | 23.16/20.41 | -0.21% | 20% |
| [BALKRISIND](https://in.tradingview.com/chart/?symbol=NSE:BALKRISIND)<br><sub>📶W9 · W↑15d · ↑CMF21d</sub> | ⚠ CAUTION | Off-highway tires for agriculture construction mining sectors | 📈 BULL_ANY_MID | 10 | ↑58 | ↑1.024 | ↑15d | — | +14.1% | 44.06/43.68 | +1.57% | 20% |
| [PROTEAN](https://in.tradingview.com/chart/?symbol=NSE:PROTEAN)<br><sub>📶W9 · W↑45d · ↑CMF9d</sub> | ✓ SAFE | Digital governance infrastructure software, government services, citizens | 📈 BULL_ANY_MID | 7 | ↑74 | ↓1.025 | ↑13d | — | +15.5% | 40.69/39.46 | -0.91% | 10% 🟨 |
| [FRACTAL](https://in.tradingview.com/chart/?symbol=NSE:FRACTAL)<br><sub>📶W9 · ↑CMF26d</sub> | ✓ SAFE | AI analytics solutions for global Fortune 500 enterprises | 📈 BULL_ANY_MID | 7 | ↑50 | ↓1.018 | ↑13d | — | +16.6% | 35.81/34.37 | -0.38% | 20% |
| [SMARTWORKS](https://in.tradingview.com/chart/?symbol=NSE:SMARTWORKS)<br><sub>📶W9 · W↑9d · ↓CMF30d</sub> | ✓ SAFE | Managed workspace solutions for enterprises and GCCs | 📈 BULL_ANY_MID | 7 | ↑65 | ↑1.020 | ↑18d | — | +10.9% | 35.92/33.75 | +1.06% | 20% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>📶W9 · W↑9d · ↑CMF8d</sub> | ✓ SAFE | Precision forged machined components two-wheeler four-wheeler OEM | 📈 BULL_ANY_MID | 6 | ↑98 | ↑1.038 | ↑14d | — | +15.4% | 46.27/45.65 | +1.64% | 20% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>📶W9 · W↑11d · ↑CMF13d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓61 | ↓1.007 | ↑15d | — | +7.0% | 46.27/45.57 | -0.67% | 20% |
| [NBCC](https://in.tradingview.com/chart/?symbol=NSE:NBCC)<br><sub>📶W9 · W↑15d · ↑CMF12d</sub> | ✓ SAFE | Government construction and engineering for infrastructure projects | 📈 BULL_ANY_MID | 5 | ↑16 | ↓1.013 | ↑15d | — | +14.3% | 17.95/16.51 | +0.13% | 20% |
| [EQUITASBNK](https://in.tradingview.com/chart/?symbol=NSE:EQUITASBNK)<br><sub>↑CMF15d</sub> | ✓ SAFE | Small finance bank serving underbanked individuals and SMEs | 📈 BULL_ANY_MID | 59 | 🔄16 | ↑1.012 | ↑1d | — | +3.0% | -29.3/-30.96 | +2.96% | 20% |
| [CAPILLARY](https://in.tradingview.com/chart/?symbol=NSE:CAPILLARY)<br><sub>↓CMF21d</sub> | ✓ SAFE | AI loyalty platforms serve enterprise retail globally | 📈 BULL_ANY_MID | 59 | 🔄50 | ↑1.012 | ↑1d | — | +2.4% | -33.11/-36.38 | +2.38% | 20% |
| [BIRLACORPN](https://in.tradingview.com/chart/?symbol=NSE:BIRLACORPN)<br><sub>W↑15d · ↑CMF7d</sub> | ⚠ CAUTION | Cement manufacturing, jute goods, steel castings producer | 📈 BULL_ANY_MID | 45 | 🔄23 | ↑1.011 | ↑15d | — | +7.5% | 24.48/21.93 | +0.77% | 20% |
| [NESCO](https://in.tradingview.com/chart/?symbol=NSE:NESCO)<br><sub>W↑9d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | IT parks, exhibitions, industrial machinery manufacturing, Mumbai | 📈 BULL_ANY_MID | 45 | 🔄45 | ↑1.010 | ↑15d | — | +7.4% | 25.43/23.24 | +0.38% | 20% |
| [HSCL](https://in.tradingview.com/chart/?symbol=NSE:HSCL)<br><sub>↑CMF2d</sub> | ✓ SAFE | Coal pitch and carbon materials for industrial applications | 📈 BULL_ANY_MID | 29 | ↓57 | ↑1.004 | ↑1d | — | +1.3% | -17.28/-17.89 | +1.26% | 20% |
| [ACCELYA](https://in.tradingview.com/chart/?symbol=NSE:ACCELYA)<br><sub>W↑5d · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Airline software platform for reservations and operations | 📈 BULL_ANY_MID | 22 | ↓22 | ↑1.008 | ↑8d | — | +2.8% | -7.41/-9.2 | +1.26% | 20% |
| [TEXRAIL](https://in.tradingview.com/chart/?symbol=NSE:TEXRAIL)<br><sub>W↑5d · ↑CMF1d</sub> | ✓ SAFE | Railway rolling stock manufacturing and hydro-mechanical equipment | 📈 BULL_ANY_MID | 20 | ↑53 | ↑1.014 | ↑10d | — | +6.1% | 22.59/21.98 | +0.37% | 20% |
| [DECNGOLD](https://in.tradingview.com/chart/?symbol=NSE:DECNGOLD)<br><sub>↑CMF10d · ⚠️TRAP</sub> | ✓ SAFE | Gold exploration and mining transitioning to active production | 📈 BULL_ANY_MID | 18 | ↓50 | ↓1.004 | ↑2d | — | +6.6% | -5.58/-6.21 | -2.16% | 20% |
| [RELIGARE](https://in.tradingview.com/chart/?symbol=NSE:RELIGARE)<br><sub>W↑9d · ↑CMF6d</sub> | ✓ SAFE | Diversified financials: insurance, broking, SME lending platform | 📈 BULL_ANY_MID | 18 | ↑54 | ↓1.012 | ↑2d | — | +3.8% | 13.1/11.39 | -0.38% | 20% |
| [RAILTEL](https://in.tradingview.com/chart/?symbol=NSE:RAILTEL)<br><sub>W↑9d · ↑CMF2d · ⚠️TRAP</sub> | ✓ SAFE | Railway telecom infrastructure and broadband services provider | 📈 BULL_ANY_MID | 18 | ↓15 | ↓1.007 | ↑2d | — | +2.7% | 9.75/9.25 | -0.97% | 20% |
| [SUMICHEM](https://in.tradingview.com/chart/?symbol=NSE:SUMICHEM)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Agrochemicals pesticides insecticides formulations Indian farmers | 📈 BULL_ANY_MID | 18 | ↓5 | ↓0.997 | ↑2d | — | +1.9% | -23.1/-23.97 | -1.00% | 20% |
| [KAPSTON](https://in.tradingview.com/chart/?symbol=NSE:KAPSTON)<br><sub>★ · ↓CMF30d</sub> | ✓ SAFE | Security guarding and facility management staffing services | 📈 BULL_ANY_MID | 18 | ↓96 | ↑1.008 | ↑12d | — | +7.2% | 11.94/11.14 | +0.80% | 20% |
| [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA)<br><sub>W↑5d · ↑CMF12d</sub> | ⚠ CAUTION | Port operations, cargo handling, maritime logistics services | 📈 BULL_ANY_MID | 16 | ↓76 | ↑1.008 | ↑14d | — | +7.8% | 12.47/10.64 | +1.22% | 20% |
| [HIKAL](https://in.tradingview.com/chart/?symbol=NSE:HIKAL)<br><sub>W↑9d · ↓CMF15d</sub> | ✓ SAFE | Specialty chemicals and APIs for pharma crop protection | 📈 BULL_ANY_MID | 16 | ↓66 | ↓1.002 | ↑4d | — | +1.9% | 14.55/13.0 | -0.59% | 20% |
| [STARCEMENT](https://in.tradingview.com/chart/?symbol=NSE:STARCEMENT)<br><sub>W↑15d · ↑CMF17d</sub> | ✓ SAFE | Cement manufacturing North-East India regional construction | 📈 BULL_ANY_MID | 14 | ↓22 | ↑1.006 | ↑16d | — | +7.9% | 13.5/12.65 | +0.40% | 20% |
| [ASTRAL](https://in.tradingview.com/chart/?symbol=NSE:ASTRAL)<br><sub>↓CMF10d · ⚠️TRAP</sub> | ✓ SAFE | Plastic pipes, fittings, tanks, bathware for construction | 📈 BULL_ANY_MID | 11 | ↓15 | ↑0.988 | ↓14d | — | -7.6% | -49.06/-49.62 | -0.14% | 20% |
| [BANARISUG](https://in.tradingview.com/chart/?symbol=NSE:BANARISUG)<br><sub>↑CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 11 | ↓20 | ↑0.991 | ↓14d | — | -1.4% | -34.19/-34.29 | +0.46% | 20% |
| [RHIM](https://in.tradingview.com/chart/?symbol=NSE:RHIM)<br><sub>↓CMF30d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE | Refractory products for steel furnaces above 1200°C | 📈 BULL_ANY_MID | 7 | ↓26 | ↓0.999 | ↓13d | — | -1.2% | -24.99/-25.29 | -0.11% | 20% |
| [RPGLIFE](https://in.tradingview.com/chart/?symbol=NSE:RPGLIFE)<br><sub>↑CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Pharmaceutical formulations and APIs for domestic international markets | 📈 BULL_ANY_MID | 1 | ↓70 | ↓0.987 | ↓19d | — | -8.0% | -38.45/-38.53 | -2.50% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:RATNAVEER,NSE:AFFLE,NSE:POWERMECH,NSE:CELLO,NSE:TATACONSUM,NSE:RUBICON,NSE:BALKRISIND,NSE:PROTEAN,NSE:FRACTAL,NSE:SMARTWORKS,NSE:SANSERA,NSE:EICHERMOT,NSE:NBCC,NSE:EQUITASBNK,NSE:CAPILLARY,NSE:BIRLACORPN,NSE:NESCO,NSE:HSCL,NSE:ACCELYA,NSE:TEXRAIL,NSE:DECNGOLD,NSE:RELIGARE,NSE:RAILTEL,NSE:SUMICHEM,NSE:KAPSTON,NSE:JSWINFRA,NSE:HIKAL,NSE:STARCEMENT,NSE:ASTRAL,NSE:BANARISUG,NSE:RHIM,NSE:RPGLIFE
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
