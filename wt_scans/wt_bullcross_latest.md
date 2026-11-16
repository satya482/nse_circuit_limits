> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-11-16
*Generated 2026-11-16 09:58 IST*

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

**Total bull crosses today: 44** · 14 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV,NSE:PIDILITIND,NSE:BPCL,NSE:TATASTEEL,NSE:SAIPARENT,NSE:FEDERALBNK,NSE:MEESHO,NSE:PTCIL,NSE:COALINDIA,NSE:GRAPHITE,NSE:FINEORG,NSE:SUNTV,NSE:ONGC,NSE:IGIL,NSE:POLYPLEX,NSE:WPIL,NSE:KRSNAA,NSE:IONEXCHANG,NSE:GANESHHOU,NSE:SHILCTECH,NSE:NSIL,NSE:ALKYLAMINE,NSE:DEEPINDS,NSE:SKFINDIA,NSE:IMPAL,NSE:SEDEMAC,NSE:UEL,NSE:SHAILY,NSE:LUPIN,NSE:ASHIKAG,NSE:JMFINANCIL,NSE:ZOTA,NSE:MONTECARLO,NSE:GALLANTT,NSE:GREENPLY,NSE:SPORTKING,NSE:TTKHLTCARE,NSE:SOTL,NSE:NUCLEUS,NSE:MMP,NSE:HDFCLIFE,NSE:RRKABEL,NSE:MASTEK,NSE:GPTINFRA
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (14)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · ↑CMF2d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 29 | ↑58 | ↑1.012 | ↑1d | — | +1.2% | -51.83/-59.38 | +1.19% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>📶W9 · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄40 | ↑1.008 | ↑1d | SQ | +2.4% | -31.16/-35.83 | +2.40% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄46 | ↑1.028 | ↑1d | SQ | +5.4% | -42.83/-51.21 | +5.43% | 20% |
| [SAIPARENT](https://in.tradingview.com/chart/?symbol=NSE:SAIPARENT)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Injectables manufacturer for hospitals and healthcare providers | 📈 BULL_ANY_MID | 88 | 🔄50 | ↑1.047 | ↑2d | SQ | +8.7% | -15.9/-23.91 | +5.04% | 20% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>📶W9 · W↑11d · ↑CMF15d</sub> | ✓ SAFE | Retail corporate banking Kerala-headquartered private sector bank | 📈 BULL_ANY_MID | 67 | ↓77 | ↑1.012 | ↑3d | SQ | +2.7% | 8.16/7.14 | +1.18% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 64 | ↓50 | ↑1.004 | ↓6d | SQ | +0.4% | -1.58/-2.79 | +0.67% | 20% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Precision metal components aerospace defense oil-gas marine | 📈 BULL_ANY_MID | 64 | ↓90 | ↑1.016 | ↑1d | SQ | +1.7% | 14.14/9.28 | +1.68% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄54 | ↑1.014 | ↑1d | — | +4.5% | -47.75/-50.99 | +4.51% | 20% |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE)<br><sub>📶W9 · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | Graphite electrodes for electric arc furnace steel making | 📈 BULL_ANY_MID | 54 | 🔄71 | ↑1.025 | ↑1d | — | +5.0% | -21.05/-25.42 | +5.02% | 20% |
| [FINEORG](https://in.tradingview.com/chart/?symbol=NSE:FINEORG)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Oleochemical specialty additives food plastics cosmetics coatings | 📈 BULL_ANY_MID | 54 | 🔄73 | ↑1.028 | ↑1d | — | +4.7% | -7.28/-13.83 | +4.70% | 20% |
| [SUNTV](https://in.tradingview.com/chart/?symbol=NSE:SUNTV)<br><sub>📶W9 · W↑36d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Regional Tamil broadcaster, entertainment content, South India | 📈 BULL_ANY_MID | 29 | ↓76 | ↑1.010 | ↑1d | — | +2.4% | -6.45/-6.62 | +2.43% | 20% |
| [ONGC](https://in.tradingview.com/chart/?symbol=NSE:ONGC)<br><sub>📶W9 · W↑6d · 🚀SS · ↑CMF4d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 22 | ↑45 | ↑1.026 | ↑3d | — | +3.7% | 12.73/0.87 | +3.45% | 20% |
| [IGIL](https://in.tradingview.com/chart/?symbol=NSE:IGIL)<br><sub>📶W9 · W↑16d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Diamond gemstone jewelry certification grading India global | 📈 BULL_ANY_MID | 0 | ↑86 | ↑1.067 | ↑20d | — | +38.3% | 61.15/59.94 | +4.76% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV,NSE:PIDILITIND,NSE:BPCL,NSE:TATASTEEL,NSE:SAIPARENT,NSE:FEDERALBNK,NSE:MEESHO,NSE:PTCIL,NSE:COALINDIA,NSE:GRAPHITE,NSE:FINEORG,NSE:SUNTV,NSE:ONGC,NSE:IGIL
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (10)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · ↑CMF2d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 29 | ↑58 | ↑1.012 | ↑1d | — | +1.2% | -51.83/-59.38 | +1.19% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>📶W9 · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄40 | ↑1.008 | ↑1d | SQ | +2.4% | -31.16/-35.83 | +2.40% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄46 | ↑1.028 | ↑1d | SQ | +5.4% | -42.83/-51.21 | +5.43% | 20% |
| [SAIPARENT](https://in.tradingview.com/chart/?symbol=NSE:SAIPARENT)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Injectables manufacturer for hospitals and healthcare providers | 📈 BULL_ANY_MID | 88 | 🔄50 | ↑1.047 | ↑2d | SQ | +8.7% | -15.9/-23.91 | +5.04% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄54 | ↑1.014 | ↑1d | — | +4.5% | -47.75/-50.99 | +4.51% | 20% |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE)<br><sub>📶W9 · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | Graphite electrodes for electric arc furnace steel making | 📈 BULL_ANY_MID | 54 | 🔄71 | ↑1.025 | ↑1d | — | +5.0% | -21.05/-25.42 | +5.02% | 20% |
| [FINEORG](https://in.tradingview.com/chart/?symbol=NSE:FINEORG)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Oleochemical specialty additives food plastics cosmetics coatings | 📈 BULL_ANY_MID | 54 | 🔄73 | ↑1.028 | ↑1d | — | +4.7% | -7.28/-13.83 | +4.70% | 20% |
| [ONGC](https://in.tradingview.com/chart/?symbol=NSE:ONGC)<br><sub>📶W9 · W↑6d · 🚀SS · ↑CMF4d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 22 | ↑45 | ↑1.026 | ↑3d | — | +3.7% | 12.73/0.87 | +3.45% | 20% |
| [IGIL](https://in.tradingview.com/chart/?symbol=NSE:IGIL)<br><sub>📶W9 · W↑16d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Diamond gemstone jewelry certification grading India global | 📈 BULL_ANY_MID | 0 | ↑86 | ↑1.067 | ↑20d | — | +38.3% | 61.15/59.94 | +4.76% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV,NSE:PIDILITIND,NSE:BPCL,NSE:TATASTEEL,NSE:SAIPARENT,NSE:COALINDIA,NSE:GRAPHITE,NSE:FINEORG,NSE:ONGC,NSE:IGIL
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (14)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>📶W9 · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄40 | ↑1.008 | ↑1d | SQ | +2.4% | -31.16/-35.83 | +2.40% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄46 | ↑1.028 | ↑1d | SQ | +5.4% | -42.83/-51.21 | +5.43% | 20% |
| [SAIPARENT](https://in.tradingview.com/chart/?symbol=NSE:SAIPARENT)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Injectables manufacturer for hospitals and healthcare providers | 📈 BULL_ANY_MID | 88 | 🔄50 | ↑1.047 | ↑2d | SQ | +8.7% | -15.9/-23.91 | +5.04% | 20% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>📶W9 · W↑11d · ↑CMF15d</sub> | ✓ SAFE | Retail corporate banking Kerala-headquartered private sector bank | 📈 BULL_ANY_MID | 67 | ↓77 | ↑1.012 | ↑3d | SQ | +2.7% | 8.16/7.14 | +1.18% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 64 | ↓50 | ↑1.004 | ↓6d | SQ | +0.4% | -1.58/-2.79 | +0.67% | 20% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Precision metal components aerospace defense oil-gas marine | 📈 BULL_ANY_MID | 64 | ↓90 | ↑1.016 | ↑1d | SQ | +1.7% | 14.14/9.28 | +1.68% | 20% |
| [GANESHHOU](https://in.tradingview.com/chart/?symbol=NSE:GANESHHOU)<br><sub>🚀SS · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Residential real estate development Ahmedabad Gujarat region | 🟡 BULL_OS_L2 | 57 | ↓23 | ↑0.992 | ↓8d | SQ | -3.8% | -57.33/-58.45 | +0.63% | 20% |
| [SKFINDIA](https://in.tradingview.com/chart/?symbol=NSE:SKFINDIA)<br><sub>W↑1d · 🚀SS · ↓CMF3d</sub> | ⚠ CAUTION | Rolling bearings, seals, lubrication for industrial automotive machinery | 📈 BULL_ANY_MID | 68 | ↓24 | ↑1.013 | ↑2d | SQ | +1.9% | -10.9/-16.62 | +1.54% | 20% |
| [IMPAL](https://in.tradingview.com/chart/?symbol=NSE:IMPAL)<br><sub>↑CMF3d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 68 | ↓49 | ↑1.013 | ↑2d | SQ | +2.2% | -15.6/-23.3 | +0.86% | 20% |
| [SEDEMAC](https://in.tradingview.com/chart/?symbol=NSE:SEDEMAC)<br><sub>↑CMF5d</sub> | ✓ SAFE | Engine control electronics for automotive and off-highway vehicles | 📈 BULL_ANY_MID | 64 | ↓50 | ↑1.004 | ↓6d | SQ | -0.6% | -28.4/-29.29 | +0.63% | 20% |
| [UEL](https://in.tradingview.com/chart/?symbol=NSE:UEL)<br><sub>🚀SS · ↓CMF20d</sub> | ⚠ CAUTION | Solar power generation, EV manufacturing, renewable energy sector | 📈 BULL_ANY_MID | 64 | ↓45 | ↑1.021 | ↑1d | SQ | +4.3% | -12.38/-12.75 | +4.30% | 10% 🟩 |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY)<br><sub>🚀SS · ↓CMF4d</sub> | ✓ SAFE | Precision plastic injection molded components for automotive OEMs | 📈 BULL_ANY_MID | 63 | ↓72 | ↑1.018 | ↑2d | SQ | +3.9% | -13.97/-19.34 | +1.44% | 20% |
| [LUPIN](https://in.tradingview.com/chart/?symbol=NSE:LUPIN)<br><sub>W↑1d · 🚀SS · ↑CMF11d</sub> | ⚠ CAUTION | Branded generics, APIs, biotechnology for global pharma markets | 📈 BULL_ANY_MID | 56 | ↓41 | ↑1.015 | ↑9d | SQ | +3.7% | 10.68/6.47 | +1.86% | 20% |
| [ASHIKAG](https://in.tradingview.com/chart/?symbol=NSE:ASHIKAG)<br><sub>↓CMF21d · ⚠️TRAP</sub> | ⚠ CAUTION | NBFC credit financing and securities broking platform | 📈 BULL_ANY_MID | 55 | ↓50 | ↑0.988 | ↓10d | SQ | -1.9% | -50.5/-51.09 | -0.08% | 5% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:BPCL,NSE:TATASTEEL,NSE:SAIPARENT,NSE:FEDERALBNK,NSE:MEESHO,NSE:PTCIL,NSE:GANESHHOU,NSE:SKFINDIA,NSE:IMPAL,NSE:SEDEMAC,NSE:UEL,NSE:SHAILY,NSE:LUPIN,NSE:ASHIKAG
```

---

### 🔥 MAJOR — PPV confirmed (2)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [POLYPLEX](https://in.tradingview.com/chart/?symbol=NSE:POLYPLEX)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | BOPET and BOPP films for flexible packaging | ⚡ BULL_ANY_PPV | 10 | ↓40 | ↑1.004 | ↓52d | PV | -20.2% | -53.4/-57.3 | +4.91% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV,NSE:POLYPLEX
```

### 🟢 OVERSOLD — reversal from −53/−60 (8)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · ↑CMF2d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 29 | ↑58 | ↑1.012 | ↑1d | — | +1.2% | -51.83/-59.38 | +1.19% | 20% |
| [WPIL](https://in.tradingview.com/chart/?symbol=NSE:WPIL)<br><sub>↓CMF5d · ⚠️TRAP</sub> | ✓ SAFE | Pumps and pumping systems for water industrial applications | 🟢 BULL_OVERSOLD | 12 | ↓50 | ↓0.962 | ↓8d | — | -7.9% | -62.91/-62.98 | -1.29% | 20% |
| [KRSNAA](https://in.tradingview.com/chart/?symbol=NSE:KRSNAA)<br><sub>🚀SS · ↑CMF4d · 🎯SLING</sub> | ✓ SAFE | Diagnostic imaging centers for patients across India | 🟢 BULL_OVERSOLD | 10 | ↓13 | ↑1.003 | ↓30d | — | -7.6% | -59.5/-62.89 | +3.92% | 20% |
| [IONEXCHANG](https://in.tradingview.com/chart/?symbol=NSE:IONEXCHANG)<br><sub>🚀SS · ↑CMF3d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Water treatment systems, industrial effluent, municipal sewage | 🟢 BULL_OVERSOLD | 5 | ↓24 | ↑0.979 | ↓49d | — | -12.5% | -65.4/-65.55 | +5.99% | 20% |
| [SHILCTECH](https://in.tradingview.com/chart/?symbol=NSE:SHILCTECH)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Distribution and power transformers for industrial electrical systems | 🟡 BULL_OS_L2 | 15 | ↓50 | ↑0.999 | ↓10d | — | -1.8% | -53.46/-54.83 | +2.53% | 20% |
| [NSIL](https://in.tradingview.com/chart/?symbol=NSE:NSIL)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 15 | ↓27 | ↑0.991 | ↓10d | — | -4.0% | -54.96/-55.26 | +1.98% | 20% |
| [ALKYLAMINE](https://in.tradingview.com/chart/?symbol=NSE:ALKYLAMINE)<br><sub>🚀SS · ↑CMF0d · 🎯SLING</sub> | ✓ SAFE | Aliphatic amines manufacturer pharma agrochemical water treatment | 🟡 BULL_OS_L2 | 8 | ↓38 | ↑0.995 | ↓17d | — | -11.7% | -55.5/-57.07 | +2.86% | 20% |
| [DEEPINDS](https://in.tradingview.com/chart/?symbol=NSE:DEEPINDS)<br><sub>↓CMF11d · 🎯SLING</sub> | ✓ SAFE | Oil gas compression drilling workover services provider | 🟡 BULL_OS_L2 | 5 | ↓86 | ↑0.987 | ↓20d | — | -14.4% | -53.71/-55.42 | +1.29% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:PIDILITIND,NSE:WPIL,NSE:KRSNAA,NSE:IONEXCHANG,NSE:SHILCTECH,NSE:NSIL,NSE:ALKYLAMINE,NSE:DEEPINDS
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (20)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄54 | ↑1.014 | ↑1d | — | +4.5% | -47.75/-50.99 | +4.51% | 20% |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE)<br><sub>📶W9 · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | Graphite electrodes for electric arc furnace steel making | 📈 BULL_ANY_MID | 54 | 🔄71 | ↑1.025 | ↑1d | — | +5.0% | -21.05/-25.42 | +5.02% | 20% |
| [FINEORG](https://in.tradingview.com/chart/?symbol=NSE:FINEORG)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Oleochemical specialty additives food plastics cosmetics coatings | 📈 BULL_ANY_MID | 54 | 🔄73 | ↑1.028 | ↑1d | — | +4.7% | -7.28/-13.83 | +4.70% | 20% |
| [SUNTV](https://in.tradingview.com/chart/?symbol=NSE:SUNTV)<br><sub>📶W9 · W↑36d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Regional Tamil broadcaster, entertainment content, South India | 📈 BULL_ANY_MID | 29 | ↓76 | ↑1.010 | ↑1d | — | +2.4% | -6.45/-6.62 | +2.43% | 20% |
| [ONGC](https://in.tradingview.com/chart/?symbol=NSE:ONGC)<br><sub>📶W9 · W↑6d · 🚀SS · ↑CMF4d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 22 | ↑45 | ↑1.026 | ↑3d | — | +3.7% | 12.73/0.87 | +3.45% | 20% |
| [IGIL](https://in.tradingview.com/chart/?symbol=NSE:IGIL)<br><sub>📶W9 · W↑16d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Diamond gemstone jewelry certification grading India global | 📈 BULL_ANY_MID | 0 | ↑86 | ↑1.067 | ↑20d | — | +38.3% | 61.15/59.94 | +4.76% | 20% |
| [JMFINANCIL](https://in.tradingview.com/chart/?symbol=NSE:JMFINANCIL)<br><sub>↓CMF16d</sub> | ✓ SAFE | Investment banking mortgage lending distressed credit asset management | 📈 BULL_ANY_MID | 29 | ↓22 | ↑1.007 | ↑1d | — | +1.1% | -43.24/-46.15 | +1.11% | 20% |
| [ZOTA](https://in.tradingview.com/chart/?symbol=NSE:ZOTA)<br><sub>↓CMF3d</sub> | ✓ SAFE | Pharma manufacturer: tablets, syrups, Ayurveda, OTC products | 📈 BULL_ANY_MID | 29 | ↓51 | ↑1.014 | ↑1d | — | +3.5% | -18.75/-19.91 | +3.45% | 20% |
| [MONTECARLO](https://in.tradingview.com/chart/?symbol=NSE:MONTECARLO)<br><sub>🚀SS · ↓CMF11d</sub> | ✓ SAFE | Woolen cotton apparel manufacturer winter wear retail | 📈 BULL_ANY_MID | 29 | ↓35 | ↑1.011 | ↑1d | — | +1.8% | -41.71/-48.25 | +1.80% | 20% |
| [GALLANTT](https://in.tradingview.com/chart/?symbol=NSE:GALLANTT)<br><sub>↑CMF20d</sub> | ✓ SAFE | Integrated steel manufacturing with mining operations eastern India | 📈 BULL_ANY_MID | 22 | ↓34 | ↑1.004 | ↓8d | — | +1.3% | -26.52/-26.88 | +1.80% | 20% 🟦 |
| [GREENPLY](https://in.tradingview.com/chart/?symbol=NSE:GREENPLY)<br><sub>🚀SS · ↓CMF6d</sub> | ✓ SAFE | Plywood MDF doors flooring for residential commercial construction | 📈 BULL_ANY_MID | 17 | ↓55 | ↑0.985 | ↓8d | — | -8.8% | -45.69/-46.23 | +1.35% | 20% |
| [SPORTKING](https://in.tradingview.com/chart/?symbol=NSE:SPORTKING)<br><sub>🚀SS · ↓CMF6d</sub> | ✓ SAFE | Textile yarns and fabrics production for apparel makers | 📈 BULL_ANY_MID | 16 | ↓92 | ↑1.000 | ↓9d | — | -5.2% | -36.35/-37.42 | +1.65% | 20% |
| [TTKHLTCARE](https://in.tradingview.com/chart/?symbol=NSE:TTKHLTCARE)<br><sub>🚀SS · ↓CMF9d · ÷DIV</sub> | ✓ SAFE | Consumer healthcare OTC brands medical devices condom foods | 📈 BULL_ANY_MID | 16 | ↓34 | ↑0.986 | ↓9d | — | -7.1% | -48.65/-48.92 | +1.30% | 20% |
| [SOTL](https://in.tradingview.com/chart/?symbol=NSE:SOTL)<br><sub>↓CMF3d · ⚠️TRAP</sub> | ✓ SAFE | Specialty lubricants transformer oils petroleum refining chemicals | 📈 BULL_ANY_MID | 15 | ↓92 | ↓0.993 | ↓5d | — | +0.5% | -30.14/-30.32 | -0.29% | 20% |
| [NUCLEUS](https://in.tradingview.com/chart/?symbol=NSE:NUCLEUS)<br><sub>🚀SS · ↑CMF0d · ⚠️TRAP</sub> | ⚠ CAUTION | Banking software for retail lending and payments | 📈 BULL_ANY_MID | 15 | ↓12 | ↑0.991 | ↓10d | — | -3.5% | -38.74/-38.98 | +0.56% | 20% |
| [MMP](https://in.tradingview.com/chart/?symbol=NSE:MMP)<br><sub>🚀SS · ↓CMF5d</sub> | ✓ SAFE | Aluminium powder manufacturer for industrial coatings paints | 📈 BULL_ANY_MID | 10 | ↓94 | ↑1.004 | ↓26d | — | -2.1% | -35.35/-36.22 | +3.04% | 20% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>↑CMF25d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 8 | ↓30 | ↓0.991 | ↓12d | — | -4.4% | -34.34/-35.72 | -0.90% | 20% |
| [RRKABEL](https://in.tradingview.com/chart/?symbol=NSE:RRKABEL)<br><sub>🚀SS · ↓CMF7d</sub> | ✓ SAFE | Copper wires cables for residential commercial industrial infrastructure | 📈 BULL_ANY_MID | 5 | ↓62 | ↑0.959 | ↓30d | — | -19.9% | -49.37/-49.97 | +2.52% | 20% |
| [MASTEK](https://in.tradingview.com/chart/?symbol=NSE:MASTEK)<br><sub>↓CMF11d</sub> | ✓ SAFE | Digital engineering, Oracle Cloud, enterprise transformation | 📈 BULL_ANY_MID | 5 | ↓16 | ↑0.994 | ↓26d | — | -3.5% | -21.73/-21.74 | +1.62% | 20% |
| [GPTINFRA](https://in.tradingview.com/chart/?symbol=NSE:GPTINFRA)<br><sub>🚀SS · ↓CMF15d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓53 | ↑1.000 | ↓32d | — | -1.4% | -29.16/-30.48 | +0.97% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:COALINDIA,NSE:GRAPHITE,NSE:FINEORG,NSE:SUNTV,NSE:ONGC,NSE:IGIL,NSE:JMFINANCIL,NSE:ZOTA,NSE:MONTECARLO,NSE:GALLANTT,NSE:GREENPLY,NSE:SPORTKING,NSE:TTKHLTCARE,NSE:SOTL,NSE:NUCLEUS,NSE:MMP,NSE:HDFCLIFE,NSE:RRKABEL,NSE:MASTEK,NSE:GPTINFRA
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
