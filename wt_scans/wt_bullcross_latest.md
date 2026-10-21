> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-10-21
*Generated 2026-10-21 15:45 IST*

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

**Total bull crosses today: 23** · 8 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:IPCALAB,NSE:EKC,NSE:SIGMAADV,NSE:GAIL,NSE:TMCV,NSE:ITC,NSE:PIRAMALFIN,NSE:KALYANKJIL,NSE:COALINDIA,NSE:TATVA,NSE:METROPOLIS,NSE:BERGEPAINT,NSE:SMARTWORKS,NSE:JSWSTEEL,NSE:UNIPARTS,NSE:SKFINDUS,NSE:GRINFRA,NSE:BPCL,NSE:GUJENERGY,NSE:ERIS,NSE:ADANIPOWER,NSE:AHLUCONT,NSE:JINDALSTEL
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (12)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>📶W9 · ↓CMF27d · 🎯SLING</sub> | ⚠ CAUTION | Pharma APIs formulations branded generics domestic exports | ⚡ BULL_ANY_PPV | 94 | 🔄83 | ↑1.018 | ↑1d | SQ·PV | +5.8% | -56.46/-57.73 | +5.75% | 20% |
| [EKC](https://in.tradingview.com/chart/?symbol=NSE:EKC)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | High-pressure seamless steel cylinders for industrial gases | ⚡ BULL_ANY_PPV | 59 | 🔄40 | ↑1.008 | ↑1d | PV | +2.4% | -32.81/-35.02 | +2.42% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄57 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄22 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [PIRAMALFIN](https://in.tradingview.com/chart/?symbol=NSE:PIRAMALFIN)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION | Housing loans retail customers construction property lending NBFC | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.016 | ↑1d | SQ | +3.6% | -40.44/-45.73 | +3.61% | 20% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Gold and studded jewellery retail across India and Middle East | 📈 BULL_ANY_MID | 87 | 🔄79 | ↑1.000 | ↓8d | SQ | +0.5% | -25.71/-27.61 | +1.03% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑55 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [TATVA](https://in.tradingview.com/chart/?symbol=NSE:TATVA)<br><sub>📶W9 · W↑23d · RVOL9x · ↓CMF0d · ÷DIV</sub> | ✓ SAFE | Specialty chemicals: catalysts, electrolytes, pharma intermediates | 📈 BULL_ANY_MID | 40 | ↑85 | ↓1.000 | ↑26d | SQ | +22.1% | 53.84/53.6 | -0.70% | 20% |
| [METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS)<br><sub>📶W9 · ↓CMF16d</sub> | ⚠ CAUTION | Diagnostic pathology labs urban semi-urban India Africa Middle East | 📈 BULL_ANY_MID | 40 | 🔄65 | ↑1.006 | ↓25d | — | -8.1% | -48.21/-49.04 | +2.79% | 20% |
| [BERGEPAINT](https://in.tradingview.com/chart/?symbol=NSE:BERGEPAINT)<br><sub>📶W9 · W↑3d · ↑CMF10d</sub> | ⚠ CAUTION | Decorative and industrial paints for buildings and factories | 📈 BULL_ANY_MID | 17 | ↑50 | ↑1.010 | ↑13d | — | +5.0% | 24.83/24.81 | +1.11% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:IPCALAB,NSE:EKC,NSE:SIGMAADV,NSE:GAIL,NSE:TMCV,NSE:ITC,NSE:PIRAMALFIN,NSE:KALYANKJIL,NSE:COALINDIA,NSE:TATVA,NSE:METROPOLIS,NSE:BERGEPAINT
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (20)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>📶W9 · ↓CMF27d · 🎯SLING</sub> | ⚠ CAUTION | Pharma APIs formulations branded generics domestic exports | ⚡ BULL_ANY_PPV | 94 | 🔄83 | ↑1.018 | ↑1d | SQ·PV | +5.8% | -56.46/-57.73 | +5.75% | 20% |
| [EKC](https://in.tradingview.com/chart/?symbol=NSE:EKC)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | High-pressure seamless steel cylinders for industrial gases | ⚡ BULL_ANY_PPV | 59 | 🔄40 | ↑1.008 | ↑1d | PV | +2.4% | -32.81/-35.02 | +2.42% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄57 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄22 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [PIRAMALFIN](https://in.tradingview.com/chart/?symbol=NSE:PIRAMALFIN)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION | Housing loans retail customers construction property lending NBFC | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.016 | ↑1d | SQ | +3.6% | -40.44/-45.73 | +3.61% | 20% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Gold and studded jewellery retail across India and Middle East | 📈 BULL_ANY_MID | 87 | 🔄79 | ↑1.000 | ↓8d | SQ | +0.5% | -25.71/-27.61 | +1.03% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑55 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [TATVA](https://in.tradingview.com/chart/?symbol=NSE:TATVA)<br><sub>📶W9 · W↑23d · RVOL9x · ↓CMF0d · ÷DIV</sub> | ✓ SAFE | Specialty chemicals: catalysts, electrolytes, pharma intermediates | 📈 BULL_ANY_MID | 40 | ↑85 | ↓1.000 | ↑26d | SQ | +22.1% | 53.84/53.6 | -0.70% | 20% |
| [METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS)<br><sub>📶W9 · ↓CMF16d</sub> | ⚠ CAUTION | Diagnostic pathology labs urban semi-urban India Africa Middle East | 📈 BULL_ANY_MID | 40 | 🔄65 | ↑1.006 | ↓25d | — | -8.1% | -48.21/-49.04 | +2.79% | 20% |
| [BERGEPAINT](https://in.tradingview.com/chart/?symbol=NSE:BERGEPAINT)<br><sub>📶W9 · W↑3d · ↑CMF10d</sub> | ⚠ CAUTION | Decorative and industrial paints for buildings and factories | 📈 BULL_ANY_MID | 17 | ↑50 | ↑1.010 | ↑13d | — | +5.0% | 24.83/24.81 | +1.11% | 20% |
| [SMARTWORKS](https://in.tradingview.com/chart/?symbol=NSE:SMARTWORKS)<br><sub>↓CMF15d · 🎯SLING</sub> | ✓ SAFE | Managed workspace solutions for enterprises and GCCs | ⚡ BULL_ANY_PPV | 35 | 🔄59 | ↑0.999 | ↓24d | PV | -8.7% | -52.24/-54.61 | +2.22% | 20% |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 42 | 🔄54 | ↑0.992 | ↓13d | — | -5.3% | -64.43/-65.64 | +2.00% | 20% |
| [GRINFRA](https://in.tradingview.com/chart/?symbol=NSE:GRINFRA)<br><sub>↓CMF0d · 🎯SLING · ÷DIV · DEL79%</sub> | ⚠ CAUTION | Road EPC contractor, highways and railways infrastructure | 🟡 BULL_OS_L2 | 58 | ↑25 | ↑0.993 | ↓7d | SQ | -0.6% | -56.03/-57.01 | -0.08% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 41 | 🔄38 | ↑1.001 | ↓19d | — | -4.4% | -53.92/-57.54 | +1.19% | 20% |
| [GUJENERGY](https://in.tradingview.com/chart/?symbol=NSE:GUJENERGY)<br><sub>W↑3d · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Piped natural gas distribution to households and industries | 🟡 BULL_OS_L2 | 35 | 🔄4 | ↑0.994 | ↓36d | — | -12.7% | -54.68/-56.0 | +0.88% | 20% |
| [ERIS](https://in.tradingview.com/chart/?symbol=NSE:ERIS)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Oral branded drugs for chronic diseases, domestic India | 🟡 BULL_OS_L2 | 35 | 🔄18 | ↑0.991 | ↓34d | — | -12.8% | -58.78/-59.92 | +1.42% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 22 | ↑68 | ↑1.004 | ↓8d | — | -0.3% | -53.58/-59.08 | +0.30% | 20% |
| [AHLUCONT](https://in.tradingview.com/chart/?symbol=NSE:AHLUCONT)<br><sub>W↑3d · ↓CMF30d</sub> | ⚠ CAUTION | Engineering contractor, infrastructure, roads, buildings, metro projects | 📈 BULL_ANY_MID | 99 | 🔄3 | ↑1.009 | ↑1d | SQ | +2.2% | -26.23/-27.69 | +2.16% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:IPCALAB,NSE:EKC,NSE:SIGMAADV,NSE:GAIL,NSE:TMCV,NSE:ITC,NSE:PIRAMALFIN,NSE:KALYANKJIL,NSE:COALINDIA,NSE:TATVA,NSE:METROPOLIS,NSE:BERGEPAINT,NSE:SMARTWORKS,NSE:JSWSTEEL,NSE:GRINFRA,NSE:BPCL,NSE:GUJENERGY,NSE:ERIS,NSE:ADANIPOWER,NSE:AHLUCONT
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (8)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>📶W9 · ↓CMF27d · 🎯SLING</sub> | ⚠ CAUTION | Pharma APIs formulations branded generics domestic exports | ⚡ BULL_ANY_PPV | 94 | 🔄83 | ↑1.018 | ↑1d | SQ·PV | +5.8% | -56.46/-57.73 | +5.75% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄22 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [PIRAMALFIN](https://in.tradingview.com/chart/?symbol=NSE:PIRAMALFIN)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION | Housing loans retail customers construction property lending NBFC | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.016 | ↑1d | SQ | +3.6% | -40.44/-45.73 | +3.61% | 20% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Gold and studded jewellery retail across India and Middle East | 📈 BULL_ANY_MID | 87 | 🔄79 | ↑1.000 | ↓8d | SQ | +0.5% | -25.71/-27.61 | +1.03% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑55 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [TATVA](https://in.tradingview.com/chart/?symbol=NSE:TATVA)<br><sub>📶W9 · W↑23d · RVOL9x · ↓CMF0d · ÷DIV</sub> | ✓ SAFE | Specialty chemicals: catalysts, electrolytes, pharma intermediates | 📈 BULL_ANY_MID | 40 | ↑85 | ↓1.000 | ↑26d | SQ | +22.1% | 53.84/53.6 | -0.70% | 20% |
| [GRINFRA](https://in.tradingview.com/chart/?symbol=NSE:GRINFRA)<br><sub>↓CMF0d · 🎯SLING · ÷DIV · DEL79%</sub> | ⚠ CAUTION | Road EPC contractor, highways and railways infrastructure | 🟡 BULL_OS_L2 | 58 | ↑25 | ↑0.993 | ↓7d | SQ | -0.6% | -56.03/-57.01 | -0.08% | 20% |
| [AHLUCONT](https://in.tradingview.com/chart/?symbol=NSE:AHLUCONT)<br><sub>W↑3d · ↓CMF30d</sub> | ⚠ CAUTION | Engineering contractor, infrastructure, roads, buildings, metro projects | 📈 BULL_ANY_MID | 99 | 🔄3 | ↑1.009 | ↑1d | SQ | +2.2% | -26.23/-27.69 | +2.16% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:IPCALAB,NSE:ITC,NSE:PIRAMALFIN,NSE:KALYANKJIL,NSE:COALINDIA,NSE:TATVA,NSE:GRINFRA,NSE:AHLUCONT
```

---

### 🔥 MAJOR — PPV confirmed (3)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [EKC](https://in.tradingview.com/chart/?symbol=NSE:EKC)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | High-pressure seamless steel cylinders for industrial gases | ⚡ BULL_ANY_PPV | 59 | 🔄40 | ↑1.008 | ↑1d | PV | +2.4% | -32.81/-35.02 | +2.42% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [SMARTWORKS](https://in.tradingview.com/chart/?symbol=NSE:SMARTWORKS)<br><sub>↓CMF15d · 🎯SLING</sub> | ✓ SAFE | Managed workspace solutions for enterprises and GCCs | ⚡ BULL_ANY_PPV | 35 | 🔄59 | ↑0.999 | ↓24d | PV | -8.7% | -52.24/-54.61 | +2.22% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:EKC,NSE:SIGMAADV,NSE:SMARTWORKS
```

### 🟢 OVERSOLD — reversal from −53/−60 (9)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄57 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 42 | 🔄54 | ↑0.992 | ↓13d | — | -5.3% | -64.43/-65.64 | +2.00% | 20% |
| [UNIPARTS](https://in.tradingview.com/chart/?symbol=NSE:UNIPARTS)<br><sub>↓CMF17d · 🎯SLING</sub> | ✓ SAFE | Off-highway vehicle components for agriculture construction mining | 🟢 BULL_OVERSOLD | 5 | ↓85 | ↑0.953 | ↓60d+ | — | -4.2% | -68.96/-69.09 | -1.02% | 20% |
| [SKFINDUS](https://in.tradingview.com/chart/?symbol=NSE:SKFINDUS)<br><sub>↓CMF26d · 🎯SLING</sub> | ⚠ CAUTION | Bearings seals lubrication systems industrial machinery | 🟢 BULL_OVERSOLD | 5 | ↓50 | ↑0.970 | ↓21d | — | -11.4% | -61.34/-61.81 | +0.22% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 41 | 🔄38 | ↑1.001 | ↓19d | — | -4.4% | -53.92/-57.54 | +1.19% | 20% |
| [GUJENERGY](https://in.tradingview.com/chart/?symbol=NSE:GUJENERGY)<br><sub>W↑3d · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Piped natural gas distribution to households and industries | 🟡 BULL_OS_L2 | 35 | 🔄4 | ↑0.994 | ↓36d | — | -12.7% | -54.68/-56.0 | +0.88% | 20% |
| [ERIS](https://in.tradingview.com/chart/?symbol=NSE:ERIS)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Oral branded drugs for chronic diseases, domestic India | 🟡 BULL_OS_L2 | 35 | 🔄18 | ↑0.991 | ↓34d | — | -12.8% | -58.78/-59.92 | +1.42% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 22 | ↑68 | ↑1.004 | ↓8d | — | -0.3% | -53.58/-59.08 | +0.30% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GAIL,NSE:TMCV,NSE:JSWSTEEL,NSE:UNIPARTS,NSE:SKFINDUS,NSE:BPCL,NSE:GUJENERGY,NSE:ERIS,NSE:ADANIPOWER
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (3)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS)<br><sub>📶W9 · ↓CMF16d</sub> | ⚠ CAUTION | Diagnostic pathology labs urban semi-urban India Africa Middle East | 📈 BULL_ANY_MID | 40 | 🔄65 | ↑1.006 | ↓25d | — | -8.1% | -48.21/-49.04 | +2.79% | 20% |
| [BERGEPAINT](https://in.tradingview.com/chart/?symbol=NSE:BERGEPAINT)<br><sub>📶W9 · W↑3d · ↑CMF10d</sub> | ⚠ CAUTION | Decorative and industrial paints for buildings and factories | 📈 BULL_ANY_MID | 17 | ↑50 | ↑1.010 | ↑13d | — | +5.0% | 24.83/24.81 | +1.11% | 20% |
| [JINDALSTEL](https://in.tradingview.com/chart/?symbol=NSE:JINDALSTEL)<br><sub>↓CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 8 | ↓50 | ↑0.982 | ↓17d | — | -8.9% | -51.85/-52.67 | +0.08% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:METROPOLIS,NSE:BERGEPAINT,NSE:JINDALSTEL
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
