> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-11-16
*Generated 2026-11-16 16:23 IST*

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

**Total bull crosses today: 23** · 5 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MARSONS,NSE:KPRMILL,NSE:SIGMAADV,NSE:GOKEX,NSE:TATACONSUM,NSE:GESHIP,NSE:TCPLPACK,NSE:EICHERMOT,NSE:TATACHEM,NSE:GALLANTT,NSE:FORTIS,NSE:RESPONIND,NSE:HIRECT,NSE:GANESHHOU,NSE:THERMAX,NSE:NSIL,NSE:ANTELOPUS,NSE:WELCORP,NSE:AJANTPHARM,NSE:DEEDEV,NSE:RPSGVENT,NSE:SJS,NSE:APARINDS
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (8)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MARSONS](https://in.tradingview.com/chart/?symbol=NSE:MARSONS)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Power and distribution transformer manufacturer for infrastructure | ⚡ BULL_ANY_PPV | 37 | 🔄50 | ↑1.077 | ↑13d | PV | +33.9% | 43.3/42.54 | +10.78% | 20% |
| [KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL)<br><sub>📶W9 · W↑11d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Yarn, fabric, apparel manufacturing, sugar, ethanol, renewable energy | ⚡ BULL_ANY_PPV | 36 | 🔄76 | ↑1.046 | ↑14d | PV | +16.5% | 32.3/27.97 | +4.54% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GOKEX](https://in.tradingview.com/chart/?symbol=NSE:GOKEX)<br><sub>📶W9 · W↑1d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Apparel manufacturer for global fashion brands and retailers | 📈 BULL_ANY_MID | 49 | 🔄33 | ↑1.037 | ↑1d | — | +5.6% | -3.46/-7.08 | +5.57% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄55 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Crude oil tankers, offshore drilling vessels, shipping services | 📈 BULL_ANY_MID | 23 | ↑76 | ↑1.026 | ↑2d | — | +5.8% | -10.66/-16.09 | +0.98% | 20% |
| [TCPLPACK](https://in.tradingview.com/chart/?symbol=NSE:TCPLPACK)<br><sub>📶W9 · W↑11d · ★ · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 18 | ↑89 | ↓1.012 | ↑2d | — | +3.6% | 33.1/32.34 | -1.07% | 20% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>📶W9 · W↑11d · ↑CMF13d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓60 | ↓1.007 | ↑15d | — | +7.0% | 46.27/45.57 | -0.67% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MARSONS,NSE:KPRMILL,NSE:SIGMAADV,NSE:GOKEX,NSE:TATACONSUM,NSE:GESHIP,NSE:TCPLPACK,NSE:EICHERMOT
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (10)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MARSONS](https://in.tradingview.com/chart/?symbol=NSE:MARSONS)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Power and distribution transformer manufacturer for infrastructure | ⚡ BULL_ANY_PPV | 37 | 🔄50 | ↑1.077 | ↑13d | PV | +33.9% | 43.3/42.54 | +10.78% | 20% |
| [KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL)<br><sub>📶W9 · W↑11d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Yarn, fabric, apparel manufacturing, sugar, ethanol, renewable energy | ⚡ BULL_ANY_PPV | 36 | 🔄76 | ↑1.046 | ↑14d | PV | +16.5% | 32.3/27.97 | +4.54% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GOKEX](https://in.tradingview.com/chart/?symbol=NSE:GOKEX)<br><sub>📶W9 · W↑1d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Apparel manufacturer for global fashion brands and retailers | 📈 BULL_ANY_MID | 49 | 🔄33 | ↑1.037 | ↑1d | — | +5.6% | -3.46/-7.08 | +5.57% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄55 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Crude oil tankers, offshore drilling vessels, shipping services | 📈 BULL_ANY_MID | 23 | ↑76 | ↑1.026 | ↑2d | — | +5.8% | -10.66/-16.09 | +0.98% | 20% |
| [TCPLPACK](https://in.tradingview.com/chart/?symbol=NSE:TCPLPACK)<br><sub>📶W9 · W↑11d · ★ · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 18 | ↑89 | ↓1.012 | ↑2d | — | +3.6% | 33.1/32.34 | -1.07% | 20% |
| [GALLANTT](https://in.tradingview.com/chart/?symbol=NSE:GALLANTT)<br><sub>↓CMF2d</sub> | ✓ SAFE | Integrated steel manufacturing with mining operations eastern India | ⚡ BULL_ANY_PPV | 54 | 🔄35 | ↑1.015 | ↑1d | PV | +3.5% | -25.34/-30.22 | +3.46% | 20% 🟦 |
| [FORTIS](https://in.tradingview.com/chart/?symbol=NSE:FORTIS)<br><sub>W↑11d · ↑CMF10d</sub> | ⚠ CAUTION | Multi-specialty hospitals, diagnostics, quaternary care delivery | ⚡ BULL_ANY_PPV | 48 | 🔄27 | ↑1.036 | ↑2d | PV | +5.7% | 9.0/5.67 | +5.13% | 20% |
| [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS)<br><sub>↓CMF7d</sub> | ✓ SAFE | Decorative graphics manufacturing for automotive consumer electronics appliances | 📈 BULL_ANY_MID | 53 | 🔄57 | ↑1.014 | ↑7d | — | +3.5% | 5.59/3.53 | +1.52% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MARSONS,NSE:KPRMILL,NSE:SIGMAADV,NSE:GOKEX,NSE:TATACONSUM,NSE:GESHIP,NSE:TCPLPACK,NSE:GALLANTT,NSE:FORTIS,NSE:SJS
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (5)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [TATACHEM](https://in.tradingview.com/chart/?symbol=NSE:TATACHEM)<br><sub>W↑5d · ↓CMF30d</sub> | ✓ SAFE | Soda ash alkali chemicals specialty products manufacturer global | ⚡ BULL_ANY_PPV | 68 | ↓29 | ↑1.008 | ↑2d | SQ·PV | +1.4% | -7.15/-12.33 | +1.02% | 20% |
| [GANESHHOU](https://in.tradingview.com/chart/?symbol=NSE:GANESHHOU)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Residential real estate development Ahmedabad Gujarat region | 🟡 BULL_OS_L2 | 69 | ↓21 | ↑1.004 | ↑1d | SQ | +2.3% | -57.15/-59.07 | +2.31% | 20% |
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM)<br><sub>↓CMF30d</sub> | ✓ SAFE | Branded generic pharmaceuticals formulations across India Asia Africa | 📈 BULL_ANY_MID | 69 | ↓69 | ↑1.008 | ↑1d | SQ | +2.3% | -23.73/-24.33 | +2.33% | 20% |
| [DEEDEV](https://in.tradingview.com/chart/?symbol=NSE:DEEDEV)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | High-pressure piping systems for oil gas power | 📈 BULL_ANY_MID | 62 | ↓94 | ↑0.997 | ↓3d | SQ | -0.1% | -25.95/-27.47 | +2.41% | 10% 🟩 |
| [RPSGVENT](https://in.tradingview.com/chart/?symbol=NSE:RPSGVENT)<br><sub>W↑5d · RVOL90x · ↓CMF30d</sub> | ✓ SAFE | Diversified holding company IT services BPM FMCG Ayurveda real estate sports | 📈 BULL_ANY_MID | 56 | ↓56 | ↑0.990 | ↓9d | SQ | +2.2% | 15.15/13.69 | -0.03% | 20% 🟦 |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:TATACHEM,NSE:GANESHHOU,NSE:AJANTPHARM,NSE:DEEDEV,NSE:RPSGVENT
```

---

### 🔥 MAJOR — PPV confirmed (5)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MARSONS](https://in.tradingview.com/chart/?symbol=NSE:MARSONS)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Power and distribution transformer manufacturer for infrastructure | ⚡ BULL_ANY_PPV | 37 | 🔄50 | ↑1.077 | ↑13d | PV | +33.9% | 43.3/42.54 | +10.78% | 20% |
| [KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL)<br><sub>📶W9 · W↑11d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Yarn, fabric, apparel manufacturing, sugar, ethanol, renewable energy | ⚡ BULL_ANY_PPV | 36 | 🔄76 | ↑1.046 | ↑14d | PV | +16.5% | 32.3/27.97 | +4.54% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GALLANTT](https://in.tradingview.com/chart/?symbol=NSE:GALLANTT)<br><sub>↓CMF2d</sub> | ✓ SAFE | Integrated steel manufacturing with mining operations eastern India | ⚡ BULL_ANY_PPV | 54 | 🔄35 | ↑1.015 | ↑1d | PV | +3.5% | -25.34/-30.22 | +3.46% | 20% 🟦 |
| [FORTIS](https://in.tradingview.com/chart/?symbol=NSE:FORTIS)<br><sub>W↑11d · ↑CMF10d</sub> | ⚠ CAUTION | Multi-specialty hospitals, diagnostics, quaternary care delivery | ⚡ BULL_ANY_PPV | 48 | 🔄27 | ↑1.036 | ↑2d | PV | +5.7% | 9.0/5.67 | +5.13% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MARSONS,NSE:KPRMILL,NSE:SIGMAADV,NSE:GALLANTT,NSE:FORTIS
```

### 🟢 OVERSOLD — reversal from −53/−60 (6)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [RESPONIND](https://in.tradingview.com/chart/?symbol=NSE:RESPONIND)<br><sub>↓CMF28d · 🎯SLING</sub> | ✓ SAFE | PVC flooring and polymer products manufacturer for global markets | 🟢 BULL_OVERSOLD | 5 | ↓10 | ↑0.975 | ↓37d | — | -14.9% | -64.08/-64.16 | -0.30% | 20% |
| [HIRECT](https://in.tradingview.com/chart/?symbol=NSE:HIRECT)<br><sub>↓CMF30d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE | Power electronics and traction transformers for Indian railways | 🟢 BULL_OVERSOLD | 0 | ↓40 | ↓0.942 | ↓42d | — | -29.1% | -66.51/-67.34 | -3.92% | 20% |
| [THERMAX](https://in.tradingview.com/chart/?symbol=NSE:THERMAX)<br><sub>↓CMF6d · ⚠️TRAP</sub> | ✓ SAFE | Industrial boilers, cooling systems, power equipment, pollution control | 🟡 BULL_OS_L2 | 16 | ↓9 | ↑0.961 | ↓9d | — | -12.5% | -56.83/-56.88 | -0.63% | 20% |
| [NSIL](https://in.tradingview.com/chart/?symbol=NSE:NSIL)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 15 | ↓27 | ↑0.991 | ↓10d | — | -4.0% | -54.96/-55.26 | +1.98% | 5% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>↑CMF30d · 🎯SLING</sub> | ✓ SAFE | Oil and gas exploration production Indian subcontinent hydrocarbon resources | 🟡 BULL_OS_L2 | 8 | ↓89 | ↑0.991 | ↓17d | — | -11.1% | -55.01/-57.48 | +2.62% | 20% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>↓CMF9d · ⚠️TRAP</sub> | ✓ SAFE | Large-diameter pipes, steel products, infrastructure | 🟡 BULL_OS_L2 | 6 | ↓97 | ↓0.979 | ↓14d | — | -10.7% | -55.44/-56.81 | -0.88% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:RESPONIND,NSE:HIRECT,NSE:THERMAX,NSE:NSIL,NSE:ANTELOPUS,NSE:WELCORP
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (7)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GOKEX](https://in.tradingview.com/chart/?symbol=NSE:GOKEX)<br><sub>📶W9 · W↑1d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Apparel manufacturer for global fashion brands and retailers | 📈 BULL_ANY_MID | 49 | 🔄33 | ↑1.037 | ↑1d | — | +5.6% | -3.46/-7.08 | +5.57% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄55 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Crude oil tankers, offshore drilling vessels, shipping services | 📈 BULL_ANY_MID | 23 | ↑76 | ↑1.026 | ↑2d | — | +5.8% | -10.66/-16.09 | +0.98% | 20% |
| [TCPLPACK](https://in.tradingview.com/chart/?symbol=NSE:TCPLPACK)<br><sub>📶W9 · W↑11d · ★ · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 18 | ↑89 | ↓1.012 | ↑2d | — | +3.6% | 33.1/32.34 | -1.07% | 20% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>📶W9 · W↑11d · ↑CMF13d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓60 | ↓1.007 | ↑15d | — | +7.0% | 46.27/45.57 | -0.67% | 20% |
| [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS)<br><sub>↓CMF7d</sub> | ✓ SAFE | Decorative graphics manufacturing for automotive consumer electronics appliances | 📈 BULL_ANY_MID | 53 | 🔄57 | ↑1.014 | ↑7d | — | +3.5% | 5.59/3.53 | +1.52% | 20% |
| [APARINDS](https://in.tradingview.com/chart/?symbol=NSE:APARINDS)<br><sub>↓CMF23d</sub> | ✓ SAFE | Power cables, transformers oils, specialty chemicals globally | 📈 BULL_ANY_MID | 21 | ↓80 | ↑1.003 | ↓9d | — | -4.5% | -43.11/-45.84 | +1.12% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GOKEX,NSE:TATACONSUM,NSE:GESHIP,NSE:TCPLPACK,NSE:EICHERMOT,NSE:SJS,NSE:APARINDS
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
