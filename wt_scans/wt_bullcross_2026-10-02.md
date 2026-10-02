> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-10-02
*Generated 2026-10-02 15:47 IST*

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

**Total bull crosses today: 33** · 11 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GKSL,NSE:SIGMAADV,NSE:ACCELYA,NSE:GATEWAY,NSE:SWARAJ,NSE:SUDARSCHEM,NSE:AEROPLANE,NSE:BAJAJHFL,NSE:RBA,NSE:INOXINDIA,NSE:AEGISLOG,NSE:GRASIM,NSE:RUBICON,NSE:GANDHITUBE,NSE:KENNAMET,NSE:HLEGLAS,NSE:CHOLAHLDNG,NSE:CREDITACC,NSE:EUREKAFORB,NSE:FUSION,NSE:BAYERCROP,NSE:NACLIND,NSE:SPMLINFRA,NSE:CENTURYPLY,NSE:INFOBEAN,NSE:MIDWESTLTD,NSE:HEIDELBERG,NSE:HGS,NSE:BSOFT,NSE:HINDWAREAP,NSE:ETHOSLTD,NSE:SAGCEM,NSE:IRCTC
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (16)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GKSL](https://in.tradingview.com/chart/?symbol=NSE:GKSL)<br><sub>📶W9 · 🚀SS·59x · ↓CMF11d</sub> | ✓ SAFE | Nephrology urology hospital super-specialty services Gujarat | ⚡ BULL_ANY_PPV | 58 | ↑50 | ↑1.086 | ↑2d | SQ·PV | +11.2% | 51.73/40.4 | +9.23% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [ACCELYA](https://in.tradingview.com/chart/?symbol=NSE:ACCELYA)<br><sub>📶W9 · 🚀SS · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Airline software platform for reservations and operations | 🟢 BULL_OVERSOLD | 57 | ↑38 | ↑0.992 | ↓8d | SQ | -2.2% | -62.42/-67.95 | +0.00% | 20% |
| [GATEWAY](https://in.tradingview.com/chart/?symbol=NSE:GATEWAY)<br><sub>📶W9 · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Container depot and rail freight logistics network | 🟡 BULL_OS_L2 | 45 | ↑32 | ↑0.994 | ↓22d | SQ | -2.3% | -57.25/-57.84 | +0.00% | 20% |
| [SWARAJ](https://in.tradingview.com/chart/?symbol=NSE:SWARAJ)<br><sub>📶W9 · W↑42d · 🚀SS · ↓CMF6d</sub> | n/a | Cotton synthetic fabric manufacturer for apparel and textiles | 📈 BULL_ANY_MID | 63 | ↑90 | ↑1.018 | ↑2d | SQ | +2.6% | 48.1/45.36 | +1.22% | 20% |
| [SUDARSCHEM](https://in.tradingview.com/chart/?symbol=NSE:SUDARSCHEM)<br><sub>📶W9 · ★ · ↑CMF0d</sub> | ✓ SAFE | Organic inorganic pigments colorants paints coatings textiles | 📈 BULL_ANY_MID | 58 | ↑81 | ↓1.014 | ↑2d | SQ | +3.1% | -4.89/-8.05 | +0.00% | 20% |
| [AEROPLANE](https://in.tradingview.com/chart/?symbol=NSE:AEROPLANE)<br><sub>📶W9 · ↑CMF19d</sub> | ✓ SAFE | Basmati rice processor and exporter for global markets | 📈 BULL_ANY_MID | 50 | ↑50 | ↓1.018 | ↑10d | SQ | +8.3% | 40.19/38.54 | +0.07% | 20% |
| [BAJAJHFL](https://in.tradingview.com/chart/?symbol=NSE:BAJAJHFL)<br><sub>📶W9 · ↑CMF5d · ⚠️TRAP</sub> | ⚠ CAUTION | Mortgage loans for home purchases, residential real estate sector | 📈 BULL_ANY_MID | 49 | ↑34 | ↓1.001 | ↓11d | SQ | +0.2% | -42.65/-42.86 | +0.00% | 20% |
| [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Burger King franchisee operating QSR restaurants India Indonesia | 📈 BULL_ANY_MID | 47 | ↑84 | ↑0.993 | ↓18d | SQ | -3.5% | -49.88/-50.82 | +0.00% | 20% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · ★ · ↓CMF6d</sub> | ✓ SAFE | Cryogenic equipment manufacturer for LNG, industrial gas, scientific applications | 📈 BULL_ANY_MID | 18 | ↑92 | ↓1.024 | ↑2d | — | +5.6% | 0.23/-2.74 | +0.00% | 20% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>📶W9 · ★ · ↑CMF19d</sub> | ✓ SAFE | Bulk liquid terminals, LPG, chemical logistics India | 📈 BULL_ANY_MID | 17 | ↑93 | ↓1.020 | ↑3d | — | +7.8% | 16.1/13.19 | +0.00% | 10% 🟨 |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 14 | ↑60 | ↑0.998 | ↓11d | — | -3.2% | -35.97/-36.7 | +0.74% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · ↓CMF10d · ⚠️TRAP</sub> | ✓ SAFE | Complex generics and specialty formulations for global pharma | 📈 BULL_ANY_MID | 9 | ↑50 | ↑0.984 | ↓16d | — | -8.9% | -41.88/-41.91 | +0.00% | 20% |
| [GANDHITUBE](https://in.tradingview.com/chart/?symbol=NSE:GANDHITUBE)<br><sub>📶W9 · W↑10d · ↑CMF16d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 9 | ↑69 | ↓1.018 | ↑11d | — | +9.1% | 43.26/42.95 | +0.00% | 20% |
| [KENNAMET](https://in.tradingview.com/chart/?symbol=NSE:KENNAMET)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Carbide cutting tools and wear solutions for manufacturing | 📈 BULL_ANY_MID | 0 | ↑50 | ↓1.007 | ↓45d | — | +51.6% | -17.31/-18.53 | +0.00% | 20% |
| [HLEGLAS](https://in.tradingview.com/chart/?symbol=NSE:HLEGLAS)<br><sub>📶W9 · W↑15d · ↑CMF12d</sub> | ✓ SAFE | Glass-lined equipment manufacturer for pharma chemicals processing | 📈 BULL_ANY_MID | 0 | ↑67 | ↓1.020 | ↑21d | — | +38.1% | 43.9/43.79 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GKSL,NSE:SIGMAADV,NSE:ACCELYA,NSE:GATEWAY,NSE:SWARAJ,NSE:SUDARSCHEM,NSE:AEROPLANE,NSE:BAJAJHFL,NSE:RBA,NSE:INOXINDIA,NSE:AEGISLOG,NSE:GRASIM,NSE:RUBICON,NSE:GANDHITUBE,NSE:KENNAMET,NSE:HLEGLAS
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (23)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GKSL](https://in.tradingview.com/chart/?symbol=NSE:GKSL)<br><sub>📶W9 · 🚀SS·59x · ↓CMF11d</sub> | ✓ SAFE | Nephrology urology hospital super-specialty services Gujarat | ⚡ BULL_ANY_PPV | 58 | ↑50 | ↑1.086 | ↑2d | SQ·PV | +11.2% | 51.73/40.4 | +9.23% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [ACCELYA](https://in.tradingview.com/chart/?symbol=NSE:ACCELYA)<br><sub>📶W9 · 🚀SS · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Airline software platform for reservations and operations | 🟢 BULL_OVERSOLD | 57 | ↑38 | ↑0.992 | ↓8d | SQ | -2.2% | -62.42/-67.95 | +0.00% | 20% |
| [GATEWAY](https://in.tradingview.com/chart/?symbol=NSE:GATEWAY)<br><sub>📶W9 · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Container depot and rail freight logistics network | 🟡 BULL_OS_L2 | 45 | ↑32 | ↑0.994 | ↓22d | SQ | -2.3% | -57.25/-57.84 | +0.00% | 20% |
| [SWARAJ](https://in.tradingview.com/chart/?symbol=NSE:SWARAJ)<br><sub>📶W9 · W↑42d · 🚀SS · ↓CMF6d</sub> | n/a | Cotton synthetic fabric manufacturer for apparel and textiles | 📈 BULL_ANY_MID | 63 | ↑90 | ↑1.018 | ↑2d | SQ | +2.6% | 48.1/45.36 | +1.22% | 20% |
| [SUDARSCHEM](https://in.tradingview.com/chart/?symbol=NSE:SUDARSCHEM)<br><sub>📶W9 · ★ · ↑CMF0d</sub> | ✓ SAFE | Organic inorganic pigments colorants paints coatings textiles | 📈 BULL_ANY_MID | 58 | ↑81 | ↓1.014 | ↑2d | SQ | +3.1% | -4.89/-8.05 | +0.00% | 20% |
| [AEROPLANE](https://in.tradingview.com/chart/?symbol=NSE:AEROPLANE)<br><sub>📶W9 · ↑CMF19d</sub> | ✓ SAFE | Basmati rice processor and exporter for global markets | 📈 BULL_ANY_MID | 50 | ↑50 | ↓1.018 | ↑10d | SQ | +8.3% | 40.19/38.54 | +0.07% | 20% |
| [BAJAJHFL](https://in.tradingview.com/chart/?symbol=NSE:BAJAJHFL)<br><sub>📶W9 · ↑CMF5d · ⚠️TRAP</sub> | ⚠ CAUTION | Mortgage loans for home purchases, residential real estate sector | 📈 BULL_ANY_MID | 49 | ↑34 | ↓1.001 | ↓11d | SQ | +0.2% | -42.65/-42.86 | +0.00% | 20% |
| [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Burger King franchisee operating QSR restaurants India Indonesia | 📈 BULL_ANY_MID | 47 | ↑84 | ↑0.993 | ↓18d | SQ | -3.5% | -49.88/-50.82 | +0.00% | 20% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · ★ · ↓CMF6d</sub> | ✓ SAFE | Cryogenic equipment manufacturer for LNG, industrial gas, scientific applications | 📈 BULL_ANY_MID | 18 | ↑92 | ↓1.024 | ↑2d | — | +5.6% | 0.23/-2.74 | +0.00% | 20% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>📶W9 · ★ · ↑CMF19d</sub> | ✓ SAFE | Bulk liquid terminals, LPG, chemical logistics India | 📈 BULL_ANY_MID | 17 | ↑93 | ↓1.020 | ↑3d | — | +7.8% | 16.1/13.19 | +0.00% | 10% 🟨 |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 14 | ↑60 | ↑0.998 | ↓11d | — | -3.2% | -35.97/-36.7 | +0.74% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · ↓CMF10d · ⚠️TRAP</sub> | ✓ SAFE | Complex generics and specialty formulations for global pharma | 📈 BULL_ANY_MID | 9 | ↑50 | ↑0.984 | ↓16d | — | -8.9% | -41.88/-41.91 | +0.00% | 20% |
| [GANDHITUBE](https://in.tradingview.com/chart/?symbol=NSE:GANDHITUBE)<br><sub>📶W9 · W↑10d · ↑CMF16d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 9 | ↑69 | ↓1.018 | ↑11d | — | +9.1% | 43.26/42.95 | +0.00% | 20% |
| [KENNAMET](https://in.tradingview.com/chart/?symbol=NSE:KENNAMET)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Carbide cutting tools and wear solutions for manufacturing | 📈 BULL_ANY_MID | 0 | ↑50 | ↓1.007 | ↓45d | — | +51.6% | -17.31/-18.53 | +0.00% | 20% |
| [HLEGLAS](https://in.tradingview.com/chart/?symbol=NSE:HLEGLAS)<br><sub>📶W9 · W↑15d · ↑CMF12d</sub> | ✓ SAFE | Glass-lined equipment manufacturer for pharma chemicals processing | 📈 BULL_ANY_MID | 0 | ↑67 | ↓1.020 | ↑21d | — | +38.1% | 43.9/43.79 | +0.00% | 20% |
| [INFOBEAN](https://in.tradingview.com/chart/?symbol=NSE:INFOBEAN)<br><sub>↓CMF28d · ⚠️TRAP</sub> | ✓ SAFE | AI-driven software engineering, digital transformation, enterprise clients | 🟢 BULL_OVERSOLD | 5 | ↑37 | ↑0.980 | ↓21d | — | -8.9% | -61.49/-63.18 | +0.00% | 20% 🟦 |
| [HGS](https://in.tradingview.com/chart/?symbol=NSE:HGS)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Customer experience BPM services, global contact center operations | 🟢 BULL_OVERSOLD | 5 | ↑26 | ↑0.985 | ↓41d | — | -13.2% | -66.49/-67.05 | +0.00% | 20% |
| [BSOFT](https://in.tradingview.com/chart/?symbol=NSE:BSOFT)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | IT services, digital transformation, cloud computing consulting | 🟡 BULL_OS_L2 | 45 | ↑18 | ↑0.985 | ↓50d | SQ | -4.5% | -56.22/-56.77 | +0.00% | 20% |
| [HINDWAREAP](https://in.tradingview.com/chart/?symbol=NSE:HINDWAREAP)<br><sub>↓CMF29d · ⚠️TRAP · ÷DIV</sub> | ⚠ CAUTION | Bathroom fittings, sanitaryware, kitchen products for homes | 🟡 BULL_OS_L2 | 45 | ↑3 | ↑0.990 | ↓60d+ | SQ | -31.2% | -56.49/-56.97 | +0.00% | 20% |
| [ETHOSLTD](https://in.tradingview.com/chart/?symbol=NSE:ETHOSLTD)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Luxury watch retail, multi-brand, Indian affluent consumers | 🟡 BULL_OS_L2 | 5 | ↑50 | ↑0.988 | ↓35d | — | -7.8% | -53.93/-54.81 | +0.00% | 20% |
| [SAGCEM](https://in.tradingview.com/chart/?symbol=NSE:SAGCEM)<br><sub>↓CMF29d · ⚠️TRAP · ÷DIV</sub> | ⚠ CAUTION | Cement manufacturing, South and Central India construction | 📈 BULL_ANY_MID | 57 | ↑8 | ↑0.999 | ↓8d | SQ | -0.9% | -33.78/-36.87 | +0.00% | 20% |
| [IRCTC](https://in.tradingview.com/chart/?symbol=NSE:IRCTC)<br><sub>↓CMF30d · ⚠️TRAP · ÷DIV</sub> | ⚠ CAUTION | Railway ticketing catering water PSU monopoly | 📈 BULL_ANY_MID | 14 | ↑12 | ↑0.992 | ↓11d | — | -0.6% | -47.59/-48.31 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GKSL,NSE:SIGMAADV,NSE:ACCELYA,NSE:GATEWAY,NSE:SWARAJ,NSE:SUDARSCHEM,NSE:AEROPLANE,NSE:BAJAJHFL,NSE:RBA,NSE:INOXINDIA,NSE:AEGISLOG,NSE:GRASIM,NSE:RUBICON,NSE:GANDHITUBE,NSE:KENNAMET,NSE:HLEGLAS,NSE:INFOBEAN,NSE:HGS,NSE:BSOFT,NSE:HINDWAREAP,NSE:ETHOSLTD,NSE:SAGCEM,NSE:IRCTC
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (11)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GKSL](https://in.tradingview.com/chart/?symbol=NSE:GKSL)<br><sub>📶W9 · 🚀SS·59x · ↓CMF11d</sub> | ✓ SAFE | Nephrology urology hospital super-specialty services Gujarat | ⚡ BULL_ANY_PPV | 58 | ↑50 | ↑1.086 | ↑2d | SQ·PV | +11.2% | 51.73/40.4 | +9.23% | 20% |
| [ACCELYA](https://in.tradingview.com/chart/?symbol=NSE:ACCELYA)<br><sub>📶W9 · 🚀SS · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Airline software platform for reservations and operations | 🟢 BULL_OVERSOLD | 57 | ↑38 | ↑0.992 | ↓8d | SQ | -2.2% | -62.42/-67.95 | +0.00% | 20% |
| [GATEWAY](https://in.tradingview.com/chart/?symbol=NSE:GATEWAY)<br><sub>📶W9 · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Container depot and rail freight logistics network | 🟡 BULL_OS_L2 | 45 | ↑32 | ↑0.994 | ↓22d | SQ | -2.3% | -57.25/-57.84 | +0.00% | 20% |
| [SWARAJ](https://in.tradingview.com/chart/?symbol=NSE:SWARAJ)<br><sub>📶W9 · W↑42d · 🚀SS · ↓CMF6d</sub> | n/a | Cotton synthetic fabric manufacturer for apparel and textiles | 📈 BULL_ANY_MID | 63 | ↑90 | ↑1.018 | ↑2d | SQ | +2.6% | 48.1/45.36 | +1.22% | 20% |
| [SUDARSCHEM](https://in.tradingview.com/chart/?symbol=NSE:SUDARSCHEM)<br><sub>📶W9 · ★ · ↑CMF0d</sub> | ✓ SAFE | Organic inorganic pigments colorants paints coatings textiles | 📈 BULL_ANY_MID | 58 | ↑81 | ↓1.014 | ↑2d | SQ | +3.1% | -4.89/-8.05 | +0.00% | 20% |
| [AEROPLANE](https://in.tradingview.com/chart/?symbol=NSE:AEROPLANE)<br><sub>📶W9 · ↑CMF19d</sub> | ✓ SAFE | Basmati rice processor and exporter for global markets | 📈 BULL_ANY_MID | 50 | ↑50 | ↓1.018 | ↑10d | SQ | +8.3% | 40.19/38.54 | +0.07% | 20% |
| [BAJAJHFL](https://in.tradingview.com/chart/?symbol=NSE:BAJAJHFL)<br><sub>📶W9 · ↑CMF5d · ⚠️TRAP</sub> | ⚠ CAUTION | Mortgage loans for home purchases, residential real estate sector | 📈 BULL_ANY_MID | 49 | ↑34 | ↓1.001 | ↓11d | SQ | +0.2% | -42.65/-42.86 | +0.00% | 20% |
| [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Burger King franchisee operating QSR restaurants India Indonesia | 📈 BULL_ANY_MID | 47 | ↑84 | ↑0.993 | ↓18d | SQ | -3.5% | -49.88/-50.82 | +0.00% | 20% |
| [BSOFT](https://in.tradingview.com/chart/?symbol=NSE:BSOFT)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | IT services, digital transformation, cloud computing consulting | 🟡 BULL_OS_L2 | 45 | ↑18 | ↑0.985 | ↓50d | SQ | -4.5% | -56.22/-56.77 | +0.00% | 20% |
| [HINDWAREAP](https://in.tradingview.com/chart/?symbol=NSE:HINDWAREAP)<br><sub>↓CMF29d · ⚠️TRAP · ÷DIV</sub> | ⚠ CAUTION | Bathroom fittings, sanitaryware, kitchen products for homes | 🟡 BULL_OS_L2 | 45 | ↑3 | ↑0.990 | ↓60d+ | SQ | -31.2% | -56.49/-56.97 | +0.00% | 20% |
| [SAGCEM](https://in.tradingview.com/chart/?symbol=NSE:SAGCEM)<br><sub>↓CMF29d · ⚠️TRAP · ÷DIV</sub> | ⚠ CAUTION | Cement manufacturing, South and Central India construction | 📈 BULL_ANY_MID | 57 | ↑8 | ↑0.999 | ↓8d | SQ | -0.9% | -33.78/-36.87 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GKSL,NSE:ACCELYA,NSE:GATEWAY,NSE:SWARAJ,NSE:SUDARSCHEM,NSE:AEROPLANE,NSE:BAJAJHFL,NSE:RBA,NSE:BSOFT,NSE:HINDWAREAP,NSE:SAGCEM
```

---

### 🔥 MAJOR — PPV confirmed (1)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV
```

### 🟢 OVERSOLD — reversal from −53/−60 (13)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CHOLAHLDNG](https://in.tradingview.com/chart/?symbol=NSE:CHOLAHLDNG)<br><sub>↑CMF20d · ⚠️TRAP</sub> | ⚠ CAUTION | NBFC lending, insurance, investment holding company | 🟢 BULL_OVERSOLD | 6 | ↓11 | ↑0.972 | ↓19d | — | -9.9% | -74.1/-74.42 | +0.00% | 20% |
| [CREDITACC](https://in.tradingview.com/chart/?symbol=NSE:CREDITACC)<br><sub>↓CMF6d · ⚠️TRAP</sub> | ⚠ CAUTION | Microfinance loans for rural women, NBFC sector | 🟢 BULL_OVERSOLD | 5 | ↓32 | ↑0.963 | ↓51d | — | -17.6% | -76.38/-78.19 | +0.00% | 20% |
| [EUREKAFORB](https://in.tradingview.com/chart/?symbol=NSE:EUREKAFORB)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Water purification, vacuum cleaners, air purifiers for households | 🟢 BULL_OVERSOLD | 5 | ↓4 | ↑0.961 | ↓22d | — | -16.7% | -68.6/-69.2 | +0.00% | 20% |
| [FUSION](https://in.tradingview.com/chart/?symbol=NSE:FUSION)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Microfinance loans for rural women entrepreneurs across India | 🟢 BULL_OVERSOLD | 5 | ↓36 | ↑0.970 | ↓21d | — | -14.2% | -64.45/-64.9 | +0.00% | 20% |
| [BAYERCROP](https://in.tradingview.com/chart/?symbol=NSE:BAYERCROP)<br><sub>↓CMF14d · ⚠️TRAP</sub> | ⚠ CAUTION | Crop protection chemicals and seeds for Indian farmers | 🟢 BULL_OVERSOLD | 5 | ↓12 | ↑0.968 | ↓57d | — | -13.6% | -78.21/-78.42 | +0.00% | 20% |
| [NACLIND](https://in.tradingview.com/chart/?symbol=NSE:NACLIND)<br><sub>↓CMF30d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE | Crop protection chemicals, technicals and formulations, Indian and export | 🟢 BULL_OVERSOLD | 5 | ↓3 | ↑0.952 | ↓29d | — | -25.9% | -68.52/-69.07 | +0.00% | 20% 🟦 |
| [SPMLINFRA](https://in.tradingview.com/chart/?symbol=NSE:SPMLINFRA)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Water sewage power EPC infrastructure projects government entities | 🟢 BULL_OVERSOLD | 5 | ↓16 | ↑0.975 | ↓31d | — | -16.5% | -64.25/-64.88 | +0.00% | 20% |
| [CENTURYPLY](https://in.tradingview.com/chart/?symbol=NSE:CENTURYPLY)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Plywood laminates MDF boards residential commercial construction | 🟢 BULL_OVERSOLD | 5 | ↓24 | ↑0.973 | ↓32d | — | -10.8% | -75.37/-76.62 | +0.00% | 20% |
| [INFOBEAN](https://in.tradingview.com/chart/?symbol=NSE:INFOBEAN)<br><sub>↓CMF28d · ⚠️TRAP</sub> | ✓ SAFE | AI-driven software engineering, digital transformation, enterprise clients | 🟢 BULL_OVERSOLD | 5 | ↑37 | ↑0.980 | ↓21d | — | -8.9% | -61.49/-63.18 | +0.00% | 20% 🟦 |
| [MIDWESTLTD](https://in.tradingview.com/chart/?symbol=NSE:MIDWESTLTD)<br><sub>↓CMF30d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE | Granite mining processing export natural stones rare earth | 🟢 BULL_OVERSOLD | 5 | ↓50 | ↑0.973 | ↓58d | — | -30.6% | -69.82/-71.67 | +0.00% | 20% |
| [HEIDELBERG](https://in.tradingview.com/chart/?symbol=NSE:HEIDELBERG)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 5 | ↓10 | ↑0.965 | ↓21d | — | -17.5% | -62.32/-62.92 | +0.00% | 20% |
| [HGS](https://in.tradingview.com/chart/?symbol=NSE:HGS)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Customer experience BPM services, global contact center operations | 🟢 BULL_OVERSOLD | 5 | ↑26 | ↑0.985 | ↓41d | — | -13.2% | -66.49/-67.05 | +0.00% | 20% |
| [ETHOSLTD](https://in.tradingview.com/chart/?symbol=NSE:ETHOSLTD)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Luxury watch retail, multi-brand, Indian affluent consumers | 🟡 BULL_OS_L2 | 5 | ↑50 | ↑0.988 | ↓35d | — | -7.8% | -53.93/-54.81 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CHOLAHLDNG,NSE:CREDITACC,NSE:EUREKAFORB,NSE:FUSION,NSE:BAYERCROP,NSE:NACLIND,NSE:SPMLINFRA,NSE:CENTURYPLY,NSE:INFOBEAN,NSE:MIDWESTLTD,NSE:HEIDELBERG,NSE:HGS,NSE:ETHOSLTD
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (8)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · ★ · ↓CMF6d</sub> | ✓ SAFE | Cryogenic equipment manufacturer for LNG, industrial gas, scientific applications | 📈 BULL_ANY_MID | 18 | ↑92 | ↓1.024 | ↑2d | — | +5.6% | 0.23/-2.74 | +0.00% | 20% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>📶W9 · ★ · ↑CMF19d</sub> | ✓ SAFE | Bulk liquid terminals, LPG, chemical logistics India | 📈 BULL_ANY_MID | 17 | ↑93 | ↓1.020 | ↑3d | — | +7.8% | 16.1/13.19 | +0.00% | 10% 🟨 |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 14 | ↑60 | ↑0.998 | ↓11d | — | -3.2% | -35.97/-36.7 | +0.74% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · ↓CMF10d · ⚠️TRAP</sub> | ✓ SAFE | Complex generics and specialty formulations for global pharma | 📈 BULL_ANY_MID | 9 | ↑50 | ↑0.984 | ↓16d | — | -8.9% | -41.88/-41.91 | +0.00% | 20% |
| [GANDHITUBE](https://in.tradingview.com/chart/?symbol=NSE:GANDHITUBE)<br><sub>📶W9 · W↑10d · ↑CMF16d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 9 | ↑69 | ↓1.018 | ↑11d | — | +9.1% | 43.26/42.95 | +0.00% | 20% |
| [KENNAMET](https://in.tradingview.com/chart/?symbol=NSE:KENNAMET)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Carbide cutting tools and wear solutions for manufacturing | 📈 BULL_ANY_MID | 0 | ↑50 | ↓1.007 | ↓45d | — | +51.6% | -17.31/-18.53 | +0.00% | 20% |
| [HLEGLAS](https://in.tradingview.com/chart/?symbol=NSE:HLEGLAS)<br><sub>📶W9 · W↑15d · ↑CMF12d</sub> | ✓ SAFE | Glass-lined equipment manufacturer for pharma chemicals processing | 📈 BULL_ANY_MID | 0 | ↑67 | ↓1.020 | ↑21d | — | +38.1% | 43.9/43.79 | +0.00% | 20% |
| [IRCTC](https://in.tradingview.com/chart/?symbol=NSE:IRCTC)<br><sub>↓CMF30d · ⚠️TRAP · ÷DIV</sub> | ⚠ CAUTION | Railway ticketing catering water PSU monopoly | 📈 BULL_ANY_MID | 14 | ↑12 | ↑0.992 | ↓11d | — | -0.6% | -47.59/-48.31 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:INOXINDIA,NSE:AEGISLOG,NSE:GRASIM,NSE:RUBICON,NSE:GANDHITUBE,NSE:KENNAMET,NSE:HLEGLAS,NSE:IRCTC
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
