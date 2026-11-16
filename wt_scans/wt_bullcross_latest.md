> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-11-16
*Generated 2026-11-16 10:56 IST*

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

**Total bull crosses today: 21** · 3 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV,NSE:GALLANTT,NSE:KPRMILL,NSE:TCPLPACK,NSE:EICHERMOT,NSE:SUPRIYA,NSE:HIRECT,NSE:THERMAX,NSE:NSIL,NSE:WELCORP,NSE:ANTELOPUS,NSE:AJANTPHARM,NSE:APOLLOPIPE,NSE:DEEDEV,NSE:GOKEX,NSE:FORTIS,NSE:SJS,NSE:GESHIP,NSE:APARINDS,NSE:JUBLCPL,NSE:STAR
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (5)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GALLANTT](https://in.tradingview.com/chart/?symbol=NSE:GALLANTT)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Integrated steel manufacturing with mining operations eastern India | 📈 BULL_ANY_MID | 49 | 🔄42 | ↑1.050 | ↑1d | — | +7.9% | -23.08/-29.66 | +7.87% | 20% 🟦 |
| [KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL)<br><sub>📶W9 · W↑11d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Yarn, fabric, apparel manufacturing, sugar, ethanol, renewable energy | 📈 BULL_ANY_MID | 36 | 🔄74 | ↑1.034 | ↑14d | — | +14.9% | 30.59/27.54 | +3.11% | 20% |
| [TCPLPACK](https://in.tradingview.com/chart/?symbol=NSE:TCPLPACK)<br><sub>📶W9 · W↑11d · ★ · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 18 | ↓89 | ↓1.010 | ↑2d | — | +3.4% | 32.91/32.29 | -1.33% | 20% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>📶W9 · W↑11d · ↑CMF13d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓60 | ↓1.011 | ↑15d | — | +7.5% | 47.36/45.84 | -0.21% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV,NSE:GALLANTT,NSE:KPRMILL,NSE:TCPLPACK,NSE:EICHERMOT
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (6)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GALLANTT](https://in.tradingview.com/chart/?symbol=NSE:GALLANTT)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Integrated steel manufacturing with mining operations eastern India | 📈 BULL_ANY_MID | 49 | 🔄42 | ↑1.050 | ↑1d | — | +7.9% | -23.08/-29.66 | +7.87% | 20% 🟦 |
| [KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL)<br><sub>📶W9 · W↑11d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Yarn, fabric, apparel manufacturing, sugar, ethanol, renewable energy | 📈 BULL_ANY_MID | 36 | 🔄74 | ↑1.034 | ↑14d | — | +14.9% | 30.59/27.54 | +3.11% | 20% |
| [GOKEX](https://in.tradingview.com/chart/?symbol=NSE:GOKEX)<br><sub>W↑1d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | Apparel manufacturer for global fashion brands and retailers | 📈 BULL_ANY_MID | 54 | 🔄30 | ↑1.026 | ↑1d | — | +4.2% | -4.32/-7.29 | +4.19% | 20% |
| [FORTIS](https://in.tradingview.com/chart/?symbol=NSE:FORTIS)<br><sub>W↑11d · ↑CMF10d</sub> | ⚠ CAUTION | Multi-specialty hospitals, diagnostics, quaternary care delivery | 📈 BULL_ANY_MID | 53 | 🔄23 | ↑1.020 | ↑2d | — | +3.7% | 5.84/4.88 | +3.20% | 20% |
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP)<br><sub>↓CMF0d</sub> | ✓ SAFE | Crude oil tankers, offshore drilling vessels, shipping services | 📈 BULL_ANY_MID | 18 | ↑75 | ↓1.017 | ↑2d | — | +4.6% | -11.76/-16.37 | -0.09% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV,NSE:GALLANTT,NSE:KPRMILL,NSE:GOKEX,NSE:FORTIS,NSE:GESHIP
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (3)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM)<br><sub>↓CMF30d</sub> | ✓ SAFE | Branded generic pharmaceuticals formulations across India Asia Africa | 📈 BULL_ANY_MID | 69 | ↓69 | ↑1.011 | ↑1d | SQ | +2.7% | -23.06/-24.16 | +2.73% | 20% |
| [APOLLOPIPE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOPIPE)<br><sub>↑CMF12d</sub> | ✓ SAFE | PVC HDPE pipes agriculture water construction infrastructure | 📈 BULL_ANY_MID | 69 | ↓76 | ↑1.002 | ↑1d | SQ | +0.7% | -22.52/-22.72 | +0.67% | 20% |
| [DEEDEV](https://in.tradingview.com/chart/?symbol=NSE:DEEDEV)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | High-pressure piping systems for oil gas power | 📈 BULL_ANY_MID | 62 | ↓95 | ↑0.999 | ↓3d | SQ | +0.1% | -24.73/-27.16 | +2.60% | 10% 🟩 |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AJANTPHARM,NSE:APOLLOPIPE,NSE:DEEDEV
```

---

### 🔥 MAJOR — PPV confirmed (1)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV
```

### 🟢 OVERSOLD — reversal from −53/−60 (6)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SUPRIYA](https://in.tradingview.com/chart/?symbol=NSE:SUPRIYA)<br><sub>↓CMF18d · ⚠️TRAP</sub> | ✓ SAFE | API manufacturer, antihistamine analgesic anaesthetic pharma exports | 🟢 BULL_OVERSOLD | 16 | ↓15 | ↑0.904 | ↓9d | — | -24.9% | -66.05/-66.14 | -0.99% | 20% |
| [HIRECT](https://in.tradingview.com/chart/?symbol=NSE:HIRECT)<br><sub>↓CMF30d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE | Power electronics and traction transformers for Indian railways | 🟢 BULL_OVERSOLD | 0 | ↓42 | ↓0.954 | ↓42d | — | -28.0% | -65.79/-67.16 | -2.40% | 20% |
| [THERMAX](https://in.tradingview.com/chart/?symbol=NSE:THERMAX)<br><sub>↓CMF6d · ⚠️TRAP</sub> | ✓ SAFE | Industrial boilers, cooling systems, power equipment, pollution control | 🟡 BULL_OS_L2 | 16 | ↓9 | ↑0.960 | ↓9d | — | -12.6% | -56.86/-56.88 | -0.74% | 20% |
| [NSIL](https://in.tradingview.com/chart/?symbol=NSE:NSIL)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 15 | ↓27 | ↑0.991 | ↓10d | — | -4.0% | -54.96/-55.26 | +1.98% | 20% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>↓CMF9d · ⚠️TRAP</sub> | ✓ SAFE | Large-diameter pipes, steel products, infrastructure | 🟡 BULL_OS_L2 | 6 | ↓97 | ↓0.976 | ↓14d | — | -11.0% | -55.55/-56.84 | -1.27% | 20% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>↑CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Oil and gas exploration production Indian subcontinent hydrocarbon resources | 🟡 BULL_OS_L2 | 3 | ↓85 | ↓0.952 | ↓17d | — | -15.2% | -57.1/-58.0 | -2.19% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SUPRIYA,NSE:HIRECT,NSE:THERMAX,NSE:NSIL,NSE:WELCORP,NSE:ANTELOPUS
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (11)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GALLANTT](https://in.tradingview.com/chart/?symbol=NSE:GALLANTT)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Integrated steel manufacturing with mining operations eastern India | 📈 BULL_ANY_MID | 49 | 🔄42 | ↑1.050 | ↑1d | — | +7.9% | -23.08/-29.66 | +7.87% | 20% 🟦 |
| [KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL)<br><sub>📶W9 · W↑11d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Yarn, fabric, apparel manufacturing, sugar, ethanol, renewable energy | 📈 BULL_ANY_MID | 36 | 🔄74 | ↑1.034 | ↑14d | — | +14.9% | 30.59/27.54 | +3.11% | 20% |
| [TCPLPACK](https://in.tradingview.com/chart/?symbol=NSE:TCPLPACK)<br><sub>📶W9 · W↑11d · ★ · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 18 | ↓89 | ↓1.010 | ↑2d | — | +3.4% | 32.91/32.29 | -1.33% | 20% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>📶W9 · W↑11d · ↑CMF13d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓60 | ↓1.011 | ↑15d | — | +7.5% | 47.36/45.84 | -0.21% | 20% |
| [GOKEX](https://in.tradingview.com/chart/?symbol=NSE:GOKEX)<br><sub>W↑1d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | Apparel manufacturer for global fashion brands and retailers | 📈 BULL_ANY_MID | 54 | 🔄30 | ↑1.026 | ↑1d | — | +4.2% | -4.32/-7.29 | +4.19% | 20% |
| [FORTIS](https://in.tradingview.com/chart/?symbol=NSE:FORTIS)<br><sub>W↑11d · ↑CMF10d</sub> | ⚠ CAUTION | Multi-specialty hospitals, diagnostics, quaternary care delivery | 📈 BULL_ANY_MID | 53 | 🔄23 | ↑1.020 | ↑2d | — | +3.7% | 5.84/4.88 | +3.20% | 20% |
| [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS)<br><sub>↓CMF7d</sub> | ✓ SAFE | Decorative graphics manufacturing for automotive consumer electronics appliances | 📈 BULL_ANY_MID | 23 | ↓54 | ↑1.005 | ↑7d | — | +2.3% | 3.67/3.05 | +0.35% | 20% |
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP)<br><sub>↓CMF0d</sub> | ✓ SAFE | Crude oil tankers, offshore drilling vessels, shipping services | 📈 BULL_ANY_MID | 18 | ↑75 | ↓1.017 | ↑2d | — | +4.6% | -11.76/-16.37 | -0.09% | 20% |
| [APARINDS](https://in.tradingview.com/chart/?symbol=NSE:APARINDS)<br><sub>↓CMF23d · ⚠️TRAP</sub> | ✓ SAFE | Power cables, transformers oils, specialty chemicals globally | 📈 BULL_ANY_MID | 11 | ↓78 | ↓0.981 | ↓9d | — | -7.1% | -44.9/-46.29 | -1.66% | 20% |
| [JUBLCPL](https://in.tradingview.com/chart/?symbol=NSE:JUBLCPL)<br><sub>↑CMF10d</sub> | ⚠ CAUTION | Agri nutrients, polymers, chemicals manufacturer for farms and industry | 📈 BULL_ANY_MID | 9 | ↓28 | ↑0.993 | ↓16d | — | +0.7% | -30.75/-30.88 | -0.03% | 20% |
| [STAR](https://in.tradingview.com/chart/?symbol=NSE:STAR)<br><sub>↑CMF14d · ⚠️TRAP</sub> | ✓ SAFE | Niche finished dosage pharma formulations global markets | 📈 BULL_ANY_MID | 5 | ↓57 | ↓0.990 | ↓15d | — | -2.6% | -36.56/-38.07 | -0.82% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GALLANTT,NSE:KPRMILL,NSE:TCPLPACK,NSE:EICHERMOT,NSE:GOKEX,NSE:FORTIS,NSE:SJS,NSE:GESHIP,NSE:APARINDS,NSE:JUBLCPL,NSE:STAR
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
