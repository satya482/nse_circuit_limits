> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-10-30
*Generated 2026-10-30 15:50 IST*

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

**Total bull crosses today: 53** · 9 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:WPIL,NSE:GREAVESCOT,NSE:BOROLTD,NSE:MANKIND,NSE:SIGMAADV,NSE:NINSYS,NSE:ELPROINTL,NSE:GVT&D,NSE:FAZE3Q,NSE:RSL,NSE:AKCAPIT,NSE:BIL,NSE:LEMONTREE,NSE:YUKEN,NSE:BALAJITELE,NSE:KARURVYSYA,NSE:GALLANTT,NSE:GRMOVER,NSE:MUFIN,NSE:RAYMOND,NSE:ZYDUSLIFE,NSE:SURYODAY,NSE:LODHA,NSE:JSWDULUX,NSE:WAAREERTL,NSE:ACCELYA,NSE:ICICILIFE,NSE:AFCONS,NSE:IREDA,NSE:AUBANK,NSE:FIVESTAR,NSE:CMRGREEN,NSE:BAJAJCON,NSE:KALYANKJIL,NSE:M&MFIN,NSE:KIRLPNU,NSE:BLIL,NSE:KSB,NSE:KALAMANDIR,NSE:TEAMLEASE,NSE:ORKLAINDIA,NSE:BHARATRAS,NSE:PAGEIND,NSE:NSIL,NSE:3MINDIA,NSE:SMLMAH,NSE:PREMIERENE,NSE:KITEX,NSE:ENRIN,NSE:DEEPINDS,NSE:360ONE,NSE:SCI,NSE:TAALTECH
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (21)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [WPIL](https://in.tradingview.com/chart/?symbol=NSE:WPIL)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Pumps and pumping systems for water industrial applications | ⚡ BULL_ANY_PPV | 59 | 🔄50 | ↑1.014 | ↑1d | PV | +4.5% | -49.91/-52.9 | +4.48% | 20% |
| [GREAVESCOT](https://in.tradingview.com/chart/?symbol=NSE:GREAVESCOT)<br><sub>📶W9 · 🚀SS·24x · ↓CMF5d</sub> | ✓ SAFE | Engines, powertrains, electric vehicles, agricultural and industrial machinery | ⚡ BULL_ANY_PPV | 49 | 🔄71 | ↑1.039 | ↑1d | PV | +6.8% | -41.64/-47.97 | +6.75% | 20% |
| [BOROLTD](https://in.tradingview.com/chart/?symbol=NSE:BOROLTD)<br><sub>📶W9 · 🚀SS·87x · ↑CMF0d</sub> | ✓ SAFE | Laboratory glassware, kitchenware, opalware manufacturer | ⚡ BULL_ANY_PPV | 49 | 🔄75 | ↑1.126 | ↑1d | PV | +20.0% | -31.82/-41.84 | +19.98% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Pharma formulations acute chronic diseases consumer healthcare | ⚡ BULL_ANY_PPV | 19 | ↑68 | ↑1.071 | ↑1d | PV | +8.2% | -23.74/-35.05 | +8.24% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [NINSYS](https://in.tradingview.com/chart/?symbol=NSE:NINSYS)<br><sub>📶W9 · W↑20d · ↑CMF22d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 0 | ↑98 | ↑1.063 | ↑24d | PV | +33.1% | 59.3/56.62 | +4.05% | 20% |
| [ELPROINTL](https://in.tradingview.com/chart/?symbol=NSE:ELPROINTL)<br><sub>📶W9 · 🚀SS · ↑CMF18d · 🎯SLING</sub> | ⚠ CAUTION | Surge arresters manufacturing, real estate development, renewable energy | 🟢 BULL_OVERSOLD | 59 | 🔄50 | ↑1.012 | ↑1d | — | +3.0% | -58.95/-64.28 | +2.97% | 20% 🟦 |
| [GVT&D](https://in.tradingview.com/chart/?symbol=NSE:GVT&D)<br><sub>📶W9 · 🚀SS · ↑CMF1d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 46 | 🔄77 | ↑1.014 | ↓14d | — | -6.2% | -65.3/-71.09 | +5.01% | 20% |
| [FAZE3Q](https://in.tradingview.com/chart/?symbol=NSE:FAZE3Q)<br><sub>📶W9 · ↓CMF7d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 93 | 🔄47 | ↑1.016 | ↑2d | SQ | +3.6% | -23.2/-28.19 | +1.94% | 20% 🟦 |
| [RSL](https://in.tradingview.com/chart/?symbol=NSE:RSL)<br><sub>📶W9 · ↓CMF18d</sub> | ✓ SAFE | Stainless steel bars billets rods domestic international markets | 📈 BULL_ANY_MID | 90 | 🔄50 | ↑1.003 | ↓10d | SQ | -0.8% | -33.83/-34.13 | +1.18% | 20% |
| [AKCAPIT](https://in.tradingview.com/chart/?symbol=NSE:AKCAPIT)<br><sub>📶W9 · 🚀SS · ↑CMF27d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 87 | 🔄50 | ↓0.993 | ↓3d | SQ | +0.3% | -9.38/-10.54 | -0.28% | 20% |
| [BIL](https://in.tradingview.com/chart/?symbol=NSE:BIL)<br><sub>📶W9 · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 70 | 🔄88 | ↓0.994 | ↓20d | SQ | +3.0% | -22.02/-22.36 | -0.64% | 20% |
| [LEMONTREE](https://in.tradingview.com/chart/?symbol=NSE:LEMONTREE)<br><sub>📶W9 · W↑25d · ↓CMF12d</sub> | ✓ SAFE | Mid-market hotel chain business leisure travelers India | 📈 BULL_ANY_MID | 58 | ↑42 | ↓0.997 | ↓2d | SQ | +2.0% | -3.24/-3.33 | -1.86% | 20% |
| [YUKEN](https://in.tradingview.com/chart/?symbol=NSE:YUKEN)<br><sub>📶W9 · ★ · ↓CMF6d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | ↑94 | ↑1.034 | ↑2d | SQ | +5.2% | 0.38/-7.6 | +2.72% | 20% |
| [BALAJITELE](https://in.tradingview.com/chart/?symbol=NSE:BALAJITELE)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | TV serials films digital content production entertainment | 📈 BULL_ANY_MID | 45 | 🔄52 | ↑0.997 | ↓10d | — | -3.7% | -33.13/-33.81 | +0.11% | 20% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>📶W9 · W↑15d · ↓CMF2d</sub> | ✓ SAFE | Private bank retail deposits lending commercial operations | 📈 BULL_ANY_MID | 26 | ↑83 | ↑1.015 | ↑4d | — | +5.5% | 29.17/28.55 | +0.45% | 20% |
| [GALLANTT](https://in.tradingview.com/chart/?symbol=NSE:GALLANTT)<br><sub>📶W9 · W↑15d · ↑CMF14d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE | Integrated steel manufacturing with mining operations eastern India | 📈 BULL_ANY_MID | 18 | ↑49 | ↓0.996 | ↓2d | — | +3.9% | -11.57/-12.69 | -2.44% | 20% 🟦 |
| [GRMOVER](https://in.tradingview.com/chart/?symbol=NSE:GRMOVER)<br><sub>📶W9 · W↑15d · ↑CMF14d</sub> | ✓ SAFE | Basmati rice milling processing domestic export markets | 📈 BULL_ANY_MID | 18 | ↑17 | ↓1.004 | ↑2d | — | +3.6% | 16.2/15.83 | -1.88% | 20% 🟦 |
| [MUFIN](https://in.tradingview.com/chart/?symbol=NSE:MUFIN)<br><sub>📶W9 · ↑CMF1d · DEL54%(T-1)</sub> | ✓ SAFE | EV financing NBFC for electric vehicle ecosystem | 📈 BULL_ANY_MID | 18 | ↑73 | ↓0.998 | ↓2d | — | +1.3% | -9.71/-10.11 | -0.93% | 20% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>📶W9 · ↓CMF2d</sub> | ✓ SAFE | Textiles apparel real estate FMCG engineering diversified conglomerate | 📈 BULL_ANY_MID | 7 | ↑99 | ↓1.003 | ↓13d | — | -5.1% | -23.55/-24.6 | -0.15% | 10% 🟨 |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Pharmaceuticals: generics, branded drugs, consumer wellness products | 📈 BULL_ANY_MID | 0 | ↑78 | ↓0.996 | ↓25d | — | +1.6% | -25.59/-26.34 | -0.86% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:WPIL,NSE:GREAVESCOT,NSE:BOROLTD,NSE:MANKIND,NSE:SIGMAADV,NSE:NINSYS,NSE:ELPROINTL,NSE:GVT&D,NSE:FAZE3Q,NSE:RSL,NSE:AKCAPIT,NSE:BIL,NSE:LEMONTREE,NSE:YUKEN,NSE:BALAJITELE,NSE:KARURVYSYA,NSE:GALLANTT,NSE:GRMOVER,NSE:MUFIN,NSE:RAYMOND,NSE:ZYDUSLIFE
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (27)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [WPIL](https://in.tradingview.com/chart/?symbol=NSE:WPIL)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Pumps and pumping systems for water industrial applications | ⚡ BULL_ANY_PPV | 59 | 🔄50 | ↑1.014 | ↑1d | PV | +4.5% | -49.91/-52.9 | +4.48% | 20% |
| [GREAVESCOT](https://in.tradingview.com/chart/?symbol=NSE:GREAVESCOT)<br><sub>📶W9 · 🚀SS·24x · ↓CMF5d</sub> | ✓ SAFE | Engines, powertrains, electric vehicles, agricultural and industrial machinery | ⚡ BULL_ANY_PPV | 49 | 🔄71 | ↑1.039 | ↑1d | PV | +6.8% | -41.64/-47.97 | +6.75% | 20% |
| [BOROLTD](https://in.tradingview.com/chart/?symbol=NSE:BOROLTD)<br><sub>📶W9 · 🚀SS·87x · ↑CMF0d</sub> | ✓ SAFE | Laboratory glassware, kitchenware, opalware manufacturer | ⚡ BULL_ANY_PPV | 49 | 🔄75 | ↑1.126 | ↑1d | PV | +20.0% | -31.82/-41.84 | +19.98% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Pharma formulations acute chronic diseases consumer healthcare | ⚡ BULL_ANY_PPV | 19 | ↑68 | ↑1.071 | ↑1d | PV | +8.2% | -23.74/-35.05 | +8.24% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [NINSYS](https://in.tradingview.com/chart/?symbol=NSE:NINSYS)<br><sub>📶W9 · W↑20d · ↑CMF22d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 0 | ↑98 | ↑1.063 | ↑24d | PV | +33.1% | 59.3/56.62 | +4.05% | 20% |
| [ELPROINTL](https://in.tradingview.com/chart/?symbol=NSE:ELPROINTL)<br><sub>📶W9 · 🚀SS · ↑CMF18d · 🎯SLING</sub> | ⚠ CAUTION | Surge arresters manufacturing, real estate development, renewable energy | 🟢 BULL_OVERSOLD | 59 | 🔄50 | ↑1.012 | ↑1d | — | +3.0% | -58.95/-64.28 | +2.97% | 20% 🟦 |
| [GVT&D](https://in.tradingview.com/chart/?symbol=NSE:GVT&D)<br><sub>📶W9 · 🚀SS · ↑CMF1d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 46 | 🔄77 | ↑1.014 | ↓14d | — | -6.2% | -65.3/-71.09 | +5.01% | 20% |
| [FAZE3Q](https://in.tradingview.com/chart/?symbol=NSE:FAZE3Q)<br><sub>📶W9 · ↓CMF7d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 93 | 🔄47 | ↑1.016 | ↑2d | SQ | +3.6% | -23.2/-28.19 | +1.94% | 20% 🟦 |
| [RSL](https://in.tradingview.com/chart/?symbol=NSE:RSL)<br><sub>📶W9 · ↓CMF18d</sub> | ✓ SAFE | Stainless steel bars billets rods domestic international markets | 📈 BULL_ANY_MID | 90 | 🔄50 | ↑1.003 | ↓10d | SQ | -0.8% | -33.83/-34.13 | +1.18% | 20% |
| [AKCAPIT](https://in.tradingview.com/chart/?symbol=NSE:AKCAPIT)<br><sub>📶W9 · 🚀SS · ↑CMF27d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 87 | 🔄50 | ↓0.993 | ↓3d | SQ | +0.3% | -9.38/-10.54 | -0.28% | 20% |
| [BIL](https://in.tradingview.com/chart/?symbol=NSE:BIL)<br><sub>📶W9 · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 70 | 🔄88 | ↓0.994 | ↓20d | SQ | +3.0% | -22.02/-22.36 | -0.64% | 20% |
| [LEMONTREE](https://in.tradingview.com/chart/?symbol=NSE:LEMONTREE)<br><sub>📶W9 · W↑25d · ↓CMF12d</sub> | ✓ SAFE | Mid-market hotel chain business leisure travelers India | 📈 BULL_ANY_MID | 58 | ↑42 | ↓0.997 | ↓2d | SQ | +2.0% | -3.24/-3.33 | -1.86% | 20% |
| [YUKEN](https://in.tradingview.com/chart/?symbol=NSE:YUKEN)<br><sub>📶W9 · ★ · ↓CMF6d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | ↑94 | ↑1.034 | ↑2d | SQ | +5.2% | 0.38/-7.6 | +2.72% | 20% |
| [BALAJITELE](https://in.tradingview.com/chart/?symbol=NSE:BALAJITELE)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | TV serials films digital content production entertainment | 📈 BULL_ANY_MID | 45 | 🔄52 | ↑0.997 | ↓10d | — | -3.7% | -33.13/-33.81 | +0.11% | 20% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>📶W9 · W↑15d · ↓CMF2d</sub> | ✓ SAFE | Private bank retail deposits lending commercial operations | 📈 BULL_ANY_MID | 26 | ↑83 | ↑1.015 | ↑4d | — | +5.5% | 29.17/28.55 | +0.45% | 20% |
| [GALLANTT](https://in.tradingview.com/chart/?symbol=NSE:GALLANTT)<br><sub>📶W9 · W↑15d · ↑CMF14d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE | Integrated steel manufacturing with mining operations eastern India | 📈 BULL_ANY_MID | 18 | ↑49 | ↓0.996 | ↓2d | — | +3.9% | -11.57/-12.69 | -2.44% | 20% 🟦 |
| [GRMOVER](https://in.tradingview.com/chart/?symbol=NSE:GRMOVER)<br><sub>📶W9 · W↑15d · ↑CMF14d</sub> | ✓ SAFE | Basmati rice milling processing domestic export markets | 📈 BULL_ANY_MID | 18 | ↑17 | ↓1.004 | ↑2d | — | +3.6% | 16.2/15.83 | -1.88% | 20% 🟦 |
| [MUFIN](https://in.tradingview.com/chart/?symbol=NSE:MUFIN)<br><sub>📶W9 · ↑CMF1d · DEL54%(T-1)</sub> | ✓ SAFE | EV financing NBFC for electric vehicle ecosystem | 📈 BULL_ANY_MID | 18 | ↑73 | ↓0.998 | ↓2d | — | +1.3% | -9.71/-10.11 | -0.93% | 20% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>📶W9 · ↓CMF2d</sub> | ✓ SAFE | Textiles apparel real estate FMCG engineering diversified conglomerate | 📈 BULL_ANY_MID | 7 | ↑99 | ↓1.003 | ↓13d | — | -5.1% | -23.55/-24.6 | -0.15% | 10% 🟨 |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Pharmaceuticals: generics, branded drugs, consumer wellness products | 📈 BULL_ANY_MID | 0 | ↑78 | ↓0.996 | ↓25d | — | +1.6% | -25.59/-26.34 | -0.86% | 20% |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>↓CMF7d · 🎯SLING</sub> | ✓ SAFE | Residential and commercial real estate development, Mumbai Pune Bangalore | 🟢 BULL_OVERSOLD | 35 | 🔄47 | ↑0.989 | ↓23d | — | -11.7% | -69.35/-69.72 | +3.10% | 20% |
| [TEAMLEASE](https://in.tradingview.com/chart/?symbol=NSE:TEAMLEASE)<br><sub>↓CMF30d · DEL88%(T-1) · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Staffing recruitment payroll HR services employer solutions | 🟡 BULL_OS_L2 | 99 | 🔄25 | ↑1.008 | ↑1d | SQ | +3.9% | -51.83/-54.26 | +3.92% | 20% |
| [ORKLAINDIA](https://in.tradingview.com/chart/?symbol=NSE:ORKLAINDIA)<br><sub>↓CMF29d · 🎯SLING</sub> | ✓ SAFE | Spices convenience foods snacks beverages Indian consumer households | 🟡 BULL_OS_L2 | 44 | 🔄50 | ↑0.992 | ↓11d | — | -4.0% | -57.55/-58.31 | -0.12% | 20% |
| [PAGEIND](https://in.tradingview.com/chart/?symbol=NSE:PAGEIND)<br><sub>↑CMF2d · 🎯SLING</sub> | ⚠ CAUTION | Jockey apparel manufacturing, distribution, India South Asia | 🟡 BULL_OS_L2 | 39 | 🔄47 | ↑0.995 | ↓16d | — | -5.3% | -54.16/-56.36 | +1.02% | 20% |
| [PREMIERENE](https://in.tradingview.com/chart/?symbol=NSE:PREMIERENE)<br><sub>↑CMF2d</sub> | ✓ SAFE | Solar cells modules manufacturing renewable energy | 📈 BULL_ANY_MID | 59 | 🔄48 | ↑1.007 | ↑1d | — | +1.3% | -40.88/-44.04 | +1.26% | 20% |
| [ENRIN](https://in.tradingview.com/chart/?symbol=NSE:ENRIN)<br><sub>🚀SS · ↓CMF7d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 36 | 🔄56 | ↑0.990 | ↓19d | — | -10.8% | -50.96/-51.3 | +3.23% | -% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:WPIL,NSE:GREAVESCOT,NSE:BOROLTD,NSE:MANKIND,NSE:SIGMAADV,NSE:NINSYS,NSE:ELPROINTL,NSE:GVT&D,NSE:FAZE3Q,NSE:RSL,NSE:AKCAPIT,NSE:BIL,NSE:LEMONTREE,NSE:YUKEN,NSE:BALAJITELE,NSE:KARURVYSYA,NSE:GALLANTT,NSE:GRMOVER,NSE:MUFIN,NSE:RAYMOND,NSE:ZYDUSLIFE,NSE:LODHA,NSE:TEAMLEASE,NSE:ORKLAINDIA,NSE:PAGEIND,NSE:PREMIERENE,NSE:ENRIN
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (9)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [FAZE3Q](https://in.tradingview.com/chart/?symbol=NSE:FAZE3Q)<br><sub>📶W9 · ↓CMF7d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 93 | 🔄47 | ↑1.016 | ↑2d | SQ | +3.6% | -23.2/-28.19 | +1.94% | 20% 🟦 |
| [RSL](https://in.tradingview.com/chart/?symbol=NSE:RSL)<br><sub>📶W9 · ↓CMF18d</sub> | ✓ SAFE | Stainless steel bars billets rods domestic international markets | 📈 BULL_ANY_MID | 90 | 🔄50 | ↑1.003 | ↓10d | SQ | -0.8% | -33.83/-34.13 | +1.18% | 20% |
| [AKCAPIT](https://in.tradingview.com/chart/?symbol=NSE:AKCAPIT)<br><sub>📶W9 · 🚀SS · ↑CMF27d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 87 | 🔄50 | ↓0.993 | ↓3d | SQ | +0.3% | -9.38/-10.54 | -0.28% | 20% |
| [BIL](https://in.tradingview.com/chart/?symbol=NSE:BIL)<br><sub>📶W9 · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 70 | 🔄88 | ↓0.994 | ↓20d | SQ | +3.0% | -22.02/-22.36 | -0.64% | 20% |
| [LEMONTREE](https://in.tradingview.com/chart/?symbol=NSE:LEMONTREE)<br><sub>📶W9 · W↑25d · ↓CMF12d</sub> | ✓ SAFE | Mid-market hotel chain business leisure travelers India | 📈 BULL_ANY_MID | 58 | ↑42 | ↓0.997 | ↓2d | SQ | +2.0% | -3.24/-3.33 | -1.86% | 20% |
| [YUKEN](https://in.tradingview.com/chart/?symbol=NSE:YUKEN)<br><sub>📶W9 · ★ · ↓CMF6d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | ↑94 | ↑1.034 | ↑2d | SQ | +5.2% | 0.38/-7.6 | +2.72% | 20% |
| [TEAMLEASE](https://in.tradingview.com/chart/?symbol=NSE:TEAMLEASE)<br><sub>↓CMF30d · DEL88%(T-1) · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Staffing recruitment payroll HR services employer solutions | 🟡 BULL_OS_L2 | 99 | 🔄25 | ↑1.008 | ↑1d | SQ | +3.9% | -51.83/-54.26 | +3.92% | 20% |
| [BHARATRAS](https://in.tradingview.com/chart/?symbol=NSE:BHARATRAS)<br><sub>W↑5d · ↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 40 | ↓2 | ↓0.981 | ↓60d+ | SQ | -31.6% | -53.68/-54.07 | -1.20% | 20% |
| [KITEX](https://in.tradingview.com/chart/?symbol=NSE:KITEX)<br><sub>W↑20d · ↓CMF30d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE | Organic infant apparel manufacturer export to US Europe | 📈 BULL_ANY_MID | 47 | ↓9 | ↓0.988 | ↓13d | SQ | -1.9% | -33.0/-34.09 | -1.58% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:FAZE3Q,NSE:RSL,NSE:AKCAPIT,NSE:BIL,NSE:LEMONTREE,NSE:YUKEN,NSE:TEAMLEASE,NSE:BHARATRAS,NSE:KITEX
```

---

### 🔥 MAJOR — PPV confirmed (7)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [WPIL](https://in.tradingview.com/chart/?symbol=NSE:WPIL)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Pumps and pumping systems for water industrial applications | ⚡ BULL_ANY_PPV | 59 | 🔄50 | ↑1.014 | ↑1d | PV | +4.5% | -49.91/-52.9 | +4.48% | 20% |
| [GREAVESCOT](https://in.tradingview.com/chart/?symbol=NSE:GREAVESCOT)<br><sub>📶W9 · 🚀SS·24x · ↓CMF5d</sub> | ✓ SAFE | Engines, powertrains, electric vehicles, agricultural and industrial machinery | ⚡ BULL_ANY_PPV | 49 | 🔄71 | ↑1.039 | ↑1d | PV | +6.8% | -41.64/-47.97 | +6.75% | 20% |
| [BOROLTD](https://in.tradingview.com/chart/?symbol=NSE:BOROLTD)<br><sub>📶W9 · 🚀SS·87x · ↑CMF0d</sub> | ✓ SAFE | Laboratory glassware, kitchenware, opalware manufacturer | ⚡ BULL_ANY_PPV | 49 | 🔄75 | ↑1.126 | ↑1d | PV | +20.0% | -31.82/-41.84 | +19.98% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Pharma formulations acute chronic diseases consumer healthcare | ⚡ BULL_ANY_PPV | 19 | ↑68 | ↑1.071 | ↑1d | PV | +8.2% | -23.74/-35.05 | +8.24% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [NINSYS](https://in.tradingview.com/chart/?symbol=NSE:NINSYS)<br><sub>📶W9 · W↑20d · ↑CMF22d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 0 | ↑98 | ↑1.063 | ↑24d | PV | +33.1% | 59.3/56.62 | +4.05% | 20% |
| [SURYODAY](https://in.tradingview.com/chart/?symbol=NSE:SURYODAY)<br><sub>🚀SS · ↓CMF7d · 🎯SLING</sub> | ✓ SAFE | Microfinance bank lending unbanked underserved retail borrowers | ⚡ BULL_ANY_PPV | 14 | ↓38 | ↑0.985 | ↓11d | PV | -8.3% | -52.02/-55.04 | +1.21% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:WPIL,NSE:GREAVESCOT,NSE:BOROLTD,NSE:MANKIND,NSE:SIGMAADV,NSE:NINSYS,NSE:SURYODAY
```

### 🟢 OVERSOLD — reversal from −53/−60 (24)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ELPROINTL](https://in.tradingview.com/chart/?symbol=NSE:ELPROINTL)<br><sub>📶W9 · 🚀SS · ↑CMF18d · 🎯SLING</sub> | ⚠ CAUTION | Surge arresters manufacturing, real estate development, renewable energy | 🟢 BULL_OVERSOLD | 59 | 🔄50 | ↑1.012 | ↑1d | — | +3.0% | -58.95/-64.28 | +2.97% | 20% 🟦 |
| [GVT&D](https://in.tradingview.com/chart/?symbol=NSE:GVT&D)<br><sub>📶W9 · 🚀SS · ↑CMF1d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 46 | 🔄77 | ↑1.014 | ↓14d | — | -6.2% | -65.3/-71.09 | +5.01% | 20% |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>↓CMF7d · 🎯SLING</sub> | ✓ SAFE | Residential and commercial real estate development, Mumbai Pune Bangalore | 🟢 BULL_OVERSOLD | 35 | 🔄47 | ↑0.989 | ↓23d | — | -11.7% | -69.35/-69.72 | +3.10% | 20% |
| [JSWDULUX](https://in.tradingview.com/chart/?symbol=NSE:JSWDULUX)<br><sub>↓CMF2d · ⚠️TRAP</sub> | n/a | Paints coatings manufacturer automotive industrial decorative | 🟢 BULL_OVERSOLD | 15 | ↓0 | ↑0.277 | ↓10d | — | -91.3% | -63.64/-64.46 | -4.27% | 20% |
| [WAAREERTL](https://in.tradingview.com/chart/?symbol=NSE:WAAREERTL)<br><sub>↓CMF7d · 🎯SLING</sub> | ✓ SAFE | Solar EPC contractor, utility-scale and rooftop projects | 🟢 BULL_OVERSOLD | 14 | ↓10 | ↑0.973 | ↓11d | — | -14.2% | -58.63/-60.9 | +0.32% | 20% |
| [ACCELYA](https://in.tradingview.com/chart/?symbol=NSE:ACCELYA)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Airline software platform for reservations and operations | 🟢 BULL_OVERSOLD | 13 | ↓20 | ↑0.950 | ↓12d | — | -10.4% | -74.61/-75.27 | -1.10% | 20% |
| [ICICILIFE](https://in.tradingview.com/chart/?symbol=NSE:ICICILIFE)<br><sub>↑CMF0d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 11 | ↓13 | ↑0.973 | ↓14d | — | -11.0% | -67.54/-68.44 | -0.47% | 20% |
| [AFCONS](https://in.tradingview.com/chart/?symbol=NSE:AFCONS)<br><sub>↓CMF10d · ⚠️TRAP</sub> | ✓ SAFE | EPC contractor offshore structures pipelines power plants | 🟢 BULL_OVERSOLD | 10 | ↓4 | ↓0.939 | ↓10d | — | -15.7% | -76.1/-76.86 | -2.66% | 20% |
| [IREDA](https://in.tradingview.com/chart/?symbol=NSE:IREDA)<br><sub>↓CMF28d · ⚠️TRAP</sub> | ✓ SAFE | Renewable energy financing, solar wind projects, India | 🟢 BULL_OVERSOLD | 9 | ↓20 | ↓0.974 | ↓11d | — | -8.0% | -63.22/-63.53 | -1.68% | 20% |
| [AUBANK](https://in.tradingview.com/chart/?symbol=NSE:AUBANK)<br><sub>↓CMF5d · ⚠️TRAP</sub> | ✓ SAFE | Small finance bank serving underserved retail borrowers | 🟢 BULL_OVERSOLD | 8 | ↓40 | ↓0.954 | ↓12d | — | -13.6% | -75.68/-77.2 | -1.90% | 20% |
| [FIVESTAR](https://in.tradingview.com/chart/?symbol=NSE:FIVESTAR)<br><sub>↓CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Secured microfinance loans for small business owners and self-employed entrepreneurs | 🟢 BULL_OVERSOLD | 7 | ↓18 | ↓0.905 | ↓13d | — | -21.4% | -81.47/-81.68 | -5.25% | 20% |
| [CMRGREEN](https://in.tradingview.com/chart/?symbol=NSE:CMRGREEN)<br><sub>↓CMF8d · 🎯SLING</sub> | ✓ SAFE | Recycled aluminium zinc alloys ingots automotive casting | 🟢 BULL_OVERSOLD | 7 | ↓50 | ↑0.971 | ↓18d | — | -10.3% | -62.49/-63.29 | -0.38% | 20% |
| [BAJAJCON](https://in.tradingview.com/chart/?symbol=NSE:BAJAJCON)<br><sub>↓CMF19d · ⚠️TRAP</sub> | ✓ SAFE | Hair oils, cosmetics, toiletries FMCG consumer products | 🟢 BULL_OVERSOLD | 6 | ↓44 | ↓0.913 | ↓14d | — | -24.8% | -63.6/-63.99 | -5.24% | 20% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Gold and studded jewellery retail across India and Middle East | 🟢 BULL_OVERSOLD | 5 | ↓70 | ↓0.958 | ↓15d | — | -10.1% | -64.89/-65.5 | -3.30% | 20% |
| [M&MFIN](https://in.tradingview.com/chart/?symbol=NSE:M&MFIN)<br><sub>↑CMF2d · 🎯SLING</sub> | ✓ SAFE | Rural tractor auto vehicle financing NBFC farm | 🟢 BULL_OVERSOLD | 5 | ↓13 | ↑0.940 | ↓60d+ | — | -36.5% | -78.41/-80.03 | -1.17% | 20% |
| [KIRLPNU](https://in.tradingview.com/chart/?symbol=NSE:KIRLPNU)<br><sub>↓CMF11d · ⚠️TRAP</sub> | ✓ SAFE | Pneumatic compressors and gas compression systems for industrial sectors | 🟢 BULL_OVERSOLD | 5 | ↓1 | ↓0.933 | ↓15d | — | -19.3% | -71.95/-72.11 | -3.23% | 20% |
| [BLIL](https://in.tradingview.com/chart/?symbol=NSE:BLIL)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Diversified holding company: logistics, chemicals, packaging, plantations | 🟢 BULL_OVERSOLD | 5 | ↓50 | ↑0.991 | ↓60d+ | — | -12.3% | -60.45/-61.37 | +0.37% | 20% |
| [KSB](https://in.tradingview.com/chart/?symbol=NSE:KSB)<br><sub>↓CMF22d · ⚠️TRAP</sub> | ⚠ CAUTION | Pumps and valves for energy, water, agriculture sectors | 🟢 BULL_OVERSOLD | 1 | ↓32 | ↓0.946 | ↓19d | — | -19.0% | -70.01/-70.91 | -1.67% | 20% |
| [KALAMANDIR](https://in.tradingview.com/chart/?symbol=NSE:KALAMANDIR)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Ethnic sarees silk apparel retail South India omni-channel | 🟢 BULL_OVERSOLD | 1 | ↓2 | ↓0.954 | ↓19d | — | -13.4% | -77.75/-78.07 | -1.10% | 20% |
| [ORKLAINDIA](https://in.tradingview.com/chart/?symbol=NSE:ORKLAINDIA)<br><sub>↓CMF29d · 🎯SLING</sub> | ✓ SAFE | Spices convenience foods snacks beverages Indian consumer households | 🟡 BULL_OS_L2 | 44 | 🔄50 | ↑0.992 | ↓11d | — | -4.0% | -57.55/-58.31 | -0.12% | 20% |
| [PAGEIND](https://in.tradingview.com/chart/?symbol=NSE:PAGEIND)<br><sub>↑CMF2d · 🎯SLING</sub> | ⚠ CAUTION | Jockey apparel manufacturing, distribution, India South Asia | 🟡 BULL_OS_L2 | 39 | 🔄47 | ↑0.995 | ↓16d | — | -5.3% | -54.16/-56.36 | +1.02% | 20% |
| [NSIL](https://in.tradingview.com/chart/?symbol=NSE:NSIL)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 15 | ↓28 | ↑0.991 | ↓10d | — | -4.0% | -54.96/-55.26 | +1.98% | 20% |
| [3MINDIA](https://in.tradingview.com/chart/?symbol=NSE:3MINDIA)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Science-based diversified products safety industrial healthcare consumer | 🟡 BULL_OS_L2 | 5 | ↓40 | ↑0.987 | ↓31d | — | -10.9% | -56.1/-56.59 | +0.24% | 20% |
| [SMLMAH](https://in.tradingview.com/chart/?symbol=NSE:SMLMAH)<br><sub>↓CMF19d · ⚠️TRAP</sub> | ✓ SAFE | Light medium commercial vehicles manufacturing Japan partnership | 🟡 BULL_OS_L2 | 0 | ↓78 | ↓0.931 | ↓32d | — | -20.9% | -57.62/-58.51 | -2.55% | 10% 🟩 |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ELPROINTL,NSE:GVT&D,NSE:LODHA,NSE:JSWDULUX,NSE:WAAREERTL,NSE:ACCELYA,NSE:ICICILIFE,NSE:AFCONS,NSE:IREDA,NSE:AUBANK,NSE:FIVESTAR,NSE:CMRGREEN,NSE:BAJAJCON,NSE:KALYANKJIL,NSE:M&MFIN,NSE:KIRLPNU,NSE:BLIL,NSE:KSB,NSE:KALAMANDIR,NSE:ORKLAINDIA,NSE:PAGEIND,NSE:NSIL,NSE:3MINDIA,NSE:SMLMAH
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (13)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [BALAJITELE](https://in.tradingview.com/chart/?symbol=NSE:BALAJITELE)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | TV serials films digital content production entertainment | 📈 BULL_ANY_MID | 45 | 🔄52 | ↑0.997 | ↓10d | — | -3.7% | -33.13/-33.81 | +0.11% | 20% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>📶W9 · W↑15d · ↓CMF2d</sub> | ✓ SAFE | Private bank retail deposits lending commercial operations | 📈 BULL_ANY_MID | 26 | ↑83 | ↑1.015 | ↑4d | — | +5.5% | 29.17/28.55 | +0.45% | 20% |
| [GALLANTT](https://in.tradingview.com/chart/?symbol=NSE:GALLANTT)<br><sub>📶W9 · W↑15d · ↑CMF14d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE | Integrated steel manufacturing with mining operations eastern India | 📈 BULL_ANY_MID | 18 | ↑49 | ↓0.996 | ↓2d | — | +3.9% | -11.57/-12.69 | -2.44% | 20% 🟦 |
| [GRMOVER](https://in.tradingview.com/chart/?symbol=NSE:GRMOVER)<br><sub>📶W9 · W↑15d · ↑CMF14d</sub> | ✓ SAFE | Basmati rice milling processing domestic export markets | 📈 BULL_ANY_MID | 18 | ↑17 | ↓1.004 | ↑2d | — | +3.6% | 16.2/15.83 | -1.88% | 20% 🟦 |
| [MUFIN](https://in.tradingview.com/chart/?symbol=NSE:MUFIN)<br><sub>📶W9 · ↑CMF1d · DEL54%(T-1)</sub> | ✓ SAFE | EV financing NBFC for electric vehicle ecosystem | 📈 BULL_ANY_MID | 18 | ↑73 | ↓0.998 | ↓2d | — | +1.3% | -9.71/-10.11 | -0.93% | 20% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>📶W9 · ↓CMF2d</sub> | ✓ SAFE | Textiles apparel real estate FMCG engineering diversified conglomerate | 📈 BULL_ANY_MID | 7 | ↑99 | ↓1.003 | ↓13d | — | -5.1% | -23.55/-24.6 | -0.15% | 10% 🟨 |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Pharmaceuticals: generics, branded drugs, consumer wellness products | 📈 BULL_ANY_MID | 0 | ↑78 | ↓0.996 | ↓25d | — | +1.6% | -25.59/-26.34 | -0.86% | 20% |
| [PREMIERENE](https://in.tradingview.com/chart/?symbol=NSE:PREMIERENE)<br><sub>↑CMF2d</sub> | ✓ SAFE | Solar cells modules manufacturing renewable energy | 📈 BULL_ANY_MID | 59 | 🔄48 | ↑1.007 | ↑1d | — | +1.3% | -40.88/-44.04 | +1.26% | 20% |
| [ENRIN](https://in.tradingview.com/chart/?symbol=NSE:ENRIN)<br><sub>🚀SS · ↓CMF7d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 36 | 🔄56 | ↑0.990 | ↓19d | — | -10.8% | -50.96/-51.3 | +3.23% | -% |
| [DEEPINDS](https://in.tradingview.com/chart/?symbol=NSE:DEEPINDS)<br><sub>↓CMF5d · ⚠️TRAP</sub> | ✓ SAFE | Oil gas compression drilling workover services provider | 📈 BULL_ANY_MID | 6 | ↓90 | ↓0.964 | ↓14d | — | -12.1% | -47.92/-48.51 | -3.70% | 20% |
| [360ONE](https://in.tradingview.com/chart/?symbol=NSE:360ONE)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Wealth management and advisory services for ultra-high-net-worth individuals | 📈 BULL_ANY_MID | 5 | ↓39 | ↓0.974 | ↓15d | — | -6.0% | -47.17/-48.56 | -3.69% | 20% |
| [SCI](https://in.tradingview.com/chart/?symbol=NSE:SCI)<br><sub>↑CMF19d · ⚠️TRAP</sub> | ✓ SAFE | Cargo and tanker shipping for domestic and international trade | 📈 BULL_ANY_MID | 5 | ↓43 | ↓0.963 | ↓15d | — | -11.8% | -49.42/-49.79 | -3.74% | 20% |
| [TAALTECH](https://in.tradingview.com/chart/?symbol=NSE:TAALTECH)<br><sub>↑CMF17d · ⚠️TRAP</sub> | ✓ SAFE | Embedded systems and engineering R&D for aerospace | 📈 BULL_ANY_MID | 0 | ↓50 | ↓0.929 | ↓36d | — | -81.2% | -27.08/-27.17 | -2.86% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:BALAJITELE,NSE:KARURVYSYA,NSE:GALLANTT,NSE:GRMOVER,NSE:MUFIN,NSE:RAYMOND,NSE:ZYDUSLIFE,NSE:PREMIERENE,NSE:ENRIN,NSE:DEEPINDS,NSE:360ONE,NSE:SCI,NSE:TAALTECH
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
