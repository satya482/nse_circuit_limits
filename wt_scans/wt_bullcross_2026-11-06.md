> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-11-06
*Generated 2026-11-06 15:50 IST*

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

**Total bull crosses today: 29** · 6 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV,NSE:PIDILITIND,NSE:BPCL,NSE:TATASTEEL,NSE:MEESHO,NSE:COALINDIA,NSE:BSOFT,NSE:ABDL,NSE:ONGC,NSE:KROSS,NSE:IVALUE,NSE:VENTIVE,NSE:ESCORTS,NSE:LATENTVIEW,NSE:INDIGOPNTS,NSE:PUNJABCHEM,NSE:CLEAN,NSE:KEC,NSE:NSIL,NSE:ECLERX,NSE:PRIVISCL,NSE:KPITTECH,NSE:SHILPAMED,NSE:INDPRUD,NSE:BLACKBUCK,NSE:HDFCLIFE,NSE:EVONILE,NSE:SMCGLOBAL,NSE:POLICYBZR
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (10)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · ↑CMF2d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 29 | ↑58 | ↑1.012 | ↑1d | — | +1.2% | -51.83/-59.38 | +1.19% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>📶W9 · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄40 | ↑1.008 | ↑1d | SQ | +2.4% | -31.16/-35.83 | +2.40% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄46 | ↑1.028 | ↑1d | SQ | +5.4% | -42.83/-51.21 | +5.43% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 64 | ↓50 | ↑1.004 | ↓6d | SQ | +0.4% | -1.58/-2.79 | +0.67% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄54 | ↑1.014 | ↑1d | — | +4.5% | -47.75/-50.99 | +4.51% | 20% |
| [BSOFT](https://in.tradingview.com/chart/?symbol=NSE:BSOFT)<br><sub>📶W9 · W↑20d · ↑CMF18d</sub> | ✓ SAFE | IT services, digital transformation, cloud computing consulting | 📈 BULL_ANY_MID | 31 | 🔄54 | ↑1.043 | ↑19d | — | +23.6% | 52.35/49.24 | +2.13% | 20% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>📶W9 · ↑CMF6d</sub> | ✓ SAFE | Spirits manufacturer, IMFL exporter, Indian domestic and export markets | 📈 BULL_ANY_MID | 29 | ↓83 | ↑1.009 | ↑1d | — | +1.3% | 6.75/4.71 | +1.28% | 20% |
| [ONGC](https://in.tradingview.com/chart/?symbol=NSE:ONGC)<br><sub>📶W9 · W↑6d · 🚀SS · ↑CMF4d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 22 | ↑46 | ↑1.026 | ↑3d | — | +3.7% | 12.73/0.87 | +3.45% | 20% |
| [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS)<br><sub>📶W9 · W↑80d · ↑CMF1d</sub> | ✓ SAFE | Commercial vehicle axle components manufacturer | 📈 BULL_ANY_MID | 17 | ↓94 | ↓1.017 | ↑3d | — | +6.9% | 22.64/20.03 | -1.17% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV,NSE:PIDILITIND,NSE:BPCL,NSE:TATASTEEL,NSE:MEESHO,NSE:COALINDIA,NSE:BSOFT,NSE:ABDL,NSE:ONGC,NSE:KROSS
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (8)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · ↑CMF2d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 29 | ↑58 | ↑1.012 | ↑1d | — | +1.2% | -51.83/-59.38 | +1.19% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>📶W9 · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄40 | ↑1.008 | ↑1d | SQ | +2.4% | -31.16/-35.83 | +2.40% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄46 | ↑1.028 | ↑1d | SQ | +5.4% | -42.83/-51.21 | +5.43% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄54 | ↑1.014 | ↑1d | — | +4.5% | -47.75/-50.99 | +4.51% | 20% |
| [BSOFT](https://in.tradingview.com/chart/?symbol=NSE:BSOFT)<br><sub>📶W9 · W↑20d · ↑CMF18d</sub> | ✓ SAFE | IT services, digital transformation, cloud computing consulting | 📈 BULL_ANY_MID | 31 | 🔄54 | ↑1.043 | ↑19d | — | +23.6% | 52.35/49.24 | +2.13% | 20% |
| [ONGC](https://in.tradingview.com/chart/?symbol=NSE:ONGC)<br><sub>📶W9 · W↑6d · 🚀SS · ↑CMF4d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 22 | ↑46 | ↑1.026 | ↑3d | — | +3.7% | 12.73/0.87 | +3.45% | 20% |
| [IVALUE](https://in.tradingview.com/chart/?symbol=NSE:IVALUE)<br><sub>RVOL51x · ↑CMF0d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | IT distributor hybrid cloud solutions enterprise security | 🔥 BULL_OS_PPV | 49 | 🔄24 | ↑1.077 | ↑1d | PV | +13.7% | -53.88/-62.83 | +13.65% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV,NSE:PIDILITIND,NSE:BPCL,NSE:TATASTEEL,NSE:COALINDIA,NSE:BSOFT,NSE:ONGC,NSE:IVALUE
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (6)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>📶W9 · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄40 | ↑1.008 | ↑1d | SQ | +2.4% | -31.16/-35.83 | +2.40% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄46 | ↑1.028 | ↑1d | SQ | +5.4% | -42.83/-51.21 | +5.43% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 64 | ↓50 | ↑1.004 | ↓6d | SQ | +0.4% | -1.58/-2.79 | +0.67% | 20% |
| [VENTIVE](https://in.tradingview.com/chart/?symbol=NSE:VENTIVE)<br><sub>↓CMF3d · 🎯SLING</sub> | ⚠ CAUTION | Luxury hotel owner operator developer India resorts | 🟢 BULL_OVERSOLD | 59 | ↓20 | ↑1.004 | ↓11d | SQ | -1.2% | -56.5/-60.9 | +1.53% | 20% |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL)<br><sub>↓CMF6d</sub> | ✓ SAFE | Aroma chemicals fragrance ingredients terpenes global export manufacturer | 📈 BULL_ANY_MID | 69 | ↓63 | ↑1.014 | ↑1d | SQ | +2.7% | -29.02/-32.48 | +2.69% | 20% |
| [KPITTECH](https://in.tradingview.com/chart/?symbol=NSE:KPITTECH)<br><sub>W↑20d · ↑CMF15d</sub> | ✓ SAFE | Automotive software, embedded systems, SDV development | 📈 BULL_ANY_MID | 58 | ↓6 | ↓1.014 | ↑2d | SQ | +3.9% | 7.05/2.5 | +0.12% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:BPCL,NSE:TATASTEEL,NSE:MEESHO,NSE:VENTIVE,NSE:PRIVISCL,NSE:KPITTECH
```

---

### 🔥 MAJOR — PPV confirmed (2)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [IVALUE](https://in.tradingview.com/chart/?symbol=NSE:IVALUE)<br><sub>RVOL51x · ↑CMF0d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | IT distributor hybrid cloud solutions enterprise security | 🔥 BULL_OS_PPV | 49 | 🔄24 | ↑1.077 | ↑1d | PV | +13.7% | -53.88/-62.83 | +13.65% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV,NSE:IVALUE
```

### 🟢 OVERSOLD — reversal from −53/−60 (9)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · ↑CMF2d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 29 | ↑58 | ↑1.012 | ↑1d | — | +1.2% | -51.83/-59.38 | +1.19% | 20% |
| [ESCORTS](https://in.tradingview.com/chart/?symbol=NSE:ESCORTS)<br><sub>↓CMF6d · ⚠️TRAP</sub> | ⚠ CAUTION | Agricultural tractors, construction equipment, railway wagons | 🟢 BULL_OVERSOLD | 17 | ↓8 | ↑0.969 | ↓8d | — | -8.0% | -70.89/-71.41 | -0.67% | 20% |
| [LATENTVIEW](https://in.tradingview.com/chart/?symbol=NSE:LATENTVIEW)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Data analytics consulting, marketing optimization, enterprise clients | 🟢 BULL_OVERSOLD | 6 | ↓2 | ↑0.979 | ↓19d | — | -11.6% | -67.94/-70.57 | +1.39% | 20% |
| [INDIGOPNTS](https://in.tradingview.com/chart/?symbol=NSE:INDIGOPNTS)<br><sub>↓CMF27d · 🔥PHX</sub> | ✓ SAFE | Decorative paints manufacturer for residential commercial property sector | 🟢 BULL_OVERSOLD | 5 | ↓25 | ↑0.978 | ↓31d | — | -18.2% | -75.12/-77.48 | +1.54% | 20% |
| [PUNJABCHEM](https://in.tradingview.com/chart/?symbol=NSE:PUNJABCHEM)<br><sub>↓CMF3d · 🎯SLING</sub> | ⚠ CAUTION | Agrochemicals pesticides fertilizers crop protection chemicals manufacturing | 🟢 BULL_OVERSOLD | 5 | ↓18 | ↑0.975 | ↓31d | — | -13.8% | -74.69/-76.07 | +0.08% | 20% |
| [CLEAN](https://in.tradingview.com/chart/?symbol=NSE:CLEAN)<br><sub>↓CMF7d · ⚠️TRAP</sub> | ✓ SAFE | Specialty chemicals manufacturing, catalytic processes, pharma and industrial | 🟢 BULL_OVERSOLD | 2 | ↓19 | ↓0.963 | ↓18d | — | -15.9% | -70.61/-71.99 | -1.44% | 20% |
| [KEC](https://in.tradingview.com/chart/?symbol=NSE:KEC)<br><sub>W↑5d · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Power transmission infrastructure EPC contractor global | 🟡 BULL_OS_L2 | 25 | ↓2 | ↑1.001 | ↓5d | — | +1.1% | -54.42/-58.05 | +1.11% | 20% |
| [NSIL](https://in.tradingview.com/chart/?symbol=NSE:NSIL)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 15 | ↓27 | ↑0.991 | ↓10d | — | -4.0% | -54.96/-55.26 | +1.98% | 20% |
| [ECLERX](https://in.tradingview.com/chart/?symbol=NSE:ECLERX)<br><sub>↓CMF6d · 🎯SLING</sub> | ✓ SAFE | Legal document processing, BPM automation, financial services outsourcing | 🟡 BULL_OS_L2 | 6 | ↓30 | ↑0.962 | ↓19d | — | -14.1% | -55.64/-56.14 | +0.76% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:PIDILITIND,NSE:ESCORTS,NSE:LATENTVIEW,NSE:INDIGOPNTS,NSE:PUNJABCHEM,NSE:CLEAN,NSE:KEC,NSE:NSIL,NSE:ECLERX
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (12)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄54 | ↑1.014 | ↑1d | — | +4.5% | -47.75/-50.99 | +4.51% | 20% |
| [BSOFT](https://in.tradingview.com/chart/?symbol=NSE:BSOFT)<br><sub>📶W9 · W↑20d · ↑CMF18d</sub> | ✓ SAFE | IT services, digital transformation, cloud computing consulting | 📈 BULL_ANY_MID | 31 | 🔄54 | ↑1.043 | ↑19d | — | +23.6% | 52.35/49.24 | +2.13% | 20% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>📶W9 · ↑CMF6d</sub> | ✓ SAFE | Spirits manufacturer, IMFL exporter, Indian domestic and export markets | 📈 BULL_ANY_MID | 29 | ↓83 | ↑1.009 | ↑1d | — | +1.3% | 6.75/4.71 | +1.28% | 20% |
| [ONGC](https://in.tradingview.com/chart/?symbol=NSE:ONGC)<br><sub>📶W9 · W↑6d · 🚀SS · ↑CMF4d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 22 | ↑46 | ↑1.026 | ↑3d | — | +3.7% | 12.73/0.87 | +3.45% | 20% |
| [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS)<br><sub>📶W9 · W↑80d · ↑CMF1d</sub> | ✓ SAFE | Commercial vehicle axle components manufacturer | 📈 BULL_ANY_MID | 17 | ↓94 | ↓1.017 | ↑3d | — | +6.9% | 22.64/20.03 | -1.17% | 20% |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>↓CMF15d</sub> | ✓ SAFE | Niche APIs formulations contract manufacturing pharma | 📈 BULL_ANY_MID | 24 | ↓98 | ↑1.015 | ↑1d | — | +2.2% | -5.21/-8.12 | +2.23% | 20% |
| [INDPRUD](https://in.tradingview.com/chart/?symbol=NSE:INDPRUD)<br><sub>↓CMF15d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 23 | ↓50 | ↑1.020 | ↑2d | — | +6.0% | -28.16/-37.73 | +1.64% | 20% |
| [BLACKBUCK](https://in.tradingview.com/chart/?symbol=NSE:BLACKBUCK)<br><sub>↓CMF20d · ÷DIV</sub> | ✓ SAFE | Digital trucking platform: loads, payments, telematics, financing | 📈 BULL_ANY_MID | 10 | ↓48 | ↑1.008 | ↓23d | — | -6.5% | -51.84/-52.84 | +3.06% | 20% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>↑CMF25d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 8 | ↓29 | ↓0.991 | ↓12d | — | -4.4% | -34.34/-35.72 | -0.90% | 20% |
| [EVONILE](https://in.tradingview.com/chart/?symbol=NSE:EVONILE)<br><sub>↑CMF1d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓50 | ↑1.000 | ↓20d | — | -11.5% | -50.58/-52.84 | +2.71% | 20% |
| [SMCGLOBAL](https://in.tradingview.com/chart/?symbol=NSE:SMCGLOBAL)<br><sub>↓CMF4d · DEL42%</sub> | ✓ SAFE | Stocks, commodities, currencies brokerage, retail and institutional clients | 📈 BULL_ANY_MID | 5 | ↓86 | ↑0.995 | ↓33d | — | +13.8% | -24.35/-25.01 | +0.39% | 20% |
| [POLICYBZR](https://in.tradingview.com/chart/?symbol=NSE:POLICYBZR)<br><sub>↓CMF4d · ⚠️TRAP</sub> | ✓ SAFE | Online insurance and lending marketplace aggregator platform | 📈 BULL_ANY_MID | 0 | ↓2 | ↓0.987 | ↓34d | — | -46.1% | -47.73/-48.76 | -0.51% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:COALINDIA,NSE:BSOFT,NSE:ABDL,NSE:ONGC,NSE:KROSS,NSE:SHILPAMED,NSE:INDPRUD,NSE:BLACKBUCK,NSE:HDFCLIFE,NSE:EVONILE,NSE:SMCGLOBAL,NSE:POLICYBZR
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
