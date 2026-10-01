> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-10-01
*Generated 2026-10-01 15:46 IST*

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

**Total bull crosses today: 49** · 16 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CCL,NSE:GOPAL,NSE:INDUSTOWER,NSE:LEMONTREE,NSE:TARIL,NSE:SCHNEIDER,NSE:GKSL,NSE:GREENPLY,NSE:ATLANTAELE,NSE:MPHASIS,NSE:NUVAMA,NSE:PACEDIGITK,NSE:WELSPUNLIV,NSE:KARURVYSYA,NSE:SIGMAADV,NSE:LTTS,NSE:CUB,NSE:SWARAJ,NSE:GPPL,NSE:ICIL,NSE:BIRLACABLE,NSE:EBGNG,NSE:SIS,NSE:TBOTEK,NSE:AEROPLANE,NSE:COFORGE,NSE:IDBI,NSE:UNIMECH,NSE:GRASIM,NSE:MOLDTKPAC,NSE:PERSISTENT,NSE:RATNAVEER,NSE:MONTECARLO,NSE:ROSSTECH,NSE:SASKEN,NSE:AADHARHFC,NSE:VINATIORGA,NSE:TEAMLEASE,NSE:PREMIERENE,NSE:ICRA,NSE:CONCOR,NSE:EQUITASBNK,NSE:TRAVELFOOD,NSE:HONDAPOWER,NSE:INDUSINDBK,NSE:THERMAX,NSE:HEXT,NSE:ARIHANT,NSE:MASTEK
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (34)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CCL](https://in.tradingview.com/chart/?symbol=NSE:CCL)<br><sub>📶W9 · ↑CMF10d · 🎯SLING</sub> | ⚠ CAUTION | Instant coffee manufacturer, global export, beverage | 🔥 BULL_OS_PPV | 59 | 🔄53 | ↑1.013 | ↑1d | PV | +3.6% | -62.07/-65.1 | +3.64% | 20% |
| [GOPAL](https://in.tradingview.com/chart/?symbol=NSE:GOPAL)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Ethnic and western snacks manufacturer serving Indian households | ⚡ BULL_ANY_PPV | 88 | 🔄29 | ↑0.994 | ↓7d | SQ·PV | -1.4% | -27.6/-29.76 | +1.51% | 20% |
| [INDUSTOWER](https://in.tradingview.com/chart/?symbol=NSE:INDUSTOWER)<br><sub>📶W9 · ↓CMF6d</sub> | ✓ SAFE | Telecom tower infrastructure operator serving mobile networks | ⚡ BULL_ANY_PPV | 69 | ↑44 | ↑1.006 | ↑1d | SQ·PV | +0.8% | -20.73/-23.54 | +0.82% | 20% |
| [LEMONTREE](https://in.tradingview.com/chart/?symbol=NSE:LEMONTREE)<br><sub>📶W9 · W↑4d · RVOL15x · ↓CMF30d</sub> | ✓ SAFE | Mid-market hotel chain business leisure travelers India | ⚡ BULL_ANY_PPV | 64 | ↑16 | ↑1.019 | ↑1d | SQ·PV | +3.3% | -17.85/-24.44 | +3.28% | 20% |
| [TARIL](https://in.tradingview.com/chart/?symbol=NSE:TARIL)<br><sub>📶W9 · 🚀SS·69x · ↓CMF30d</sub> | ✓ SAFE | Power transformers, furnace transformers, electrical equipment manufacturing | ⚡ BULL_ANY_PPV | 59 | 🔄21 | ↑1.010 | ↑1d | PV | +4.0% | -43.96/-49.46 | +3.96% | 20% |
| [SCHNEIDER](https://in.tradingview.com/chart/?symbol=NSE:SCHNEIDER)<br><sub>📶W9 · ↑CMF10d</sub> | ✓ SAFE | Power distribution equipment manufacturing and servicing | ⚡ BULL_ANY_PPV | 59 | ↑79 | ↑1.046 | ↑1d | SQ·PV | +6.0% | 7.69/-1.21 | +5.98% | 10% 🟩 |
| [GKSL](https://in.tradingview.com/chart/?symbol=NSE:GKSL)<br><sub>📶W9 · 🚀SS·59x · ↓CMF11d</sub> | ✓ SAFE | Nephrology urology hospital super-specialty services Gujarat | ⚡ BULL_ANY_PPV | 58 | ↑50 | ↑1.086 | ↑2d | SQ·PV | +11.2% | 51.73/40.4 | +9.23% | 20% |
| [GREENPLY](https://in.tradingview.com/chart/?symbol=NSE:GREENPLY)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Plywood MDF doors flooring for residential commercial construction | ⚡ BULL_ANY_PPV | 58 | ↑64 | ↑1.038 | ↑2d | SQ·PV | +8.4% | 4.04/-4.21 | +1.25% | 20% |
| [ATLANTAELE](https://in.tradingview.com/chart/?symbol=NSE:ATLANTAELE)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | High-voltage transformers for power generation transmission distribution | ⚡ BULL_ANY_PPV | 49 | 🔄50 | ↑1.034 | ↑1d | PV | +6.7% | -26.32/-31.06 | +6.74% | 5% 🟥 |
| [MPHASIS](https://in.tradingview.com/chart/?symbol=NSE:MPHASIS)<br><sub>📶W9 · 🚀SS · ↓CMF15d · 🎯SLING</sub> | ✓ SAFE | IT services, cloud and cognitive transformation, enterprise clients | ⚡ BULL_ANY_PPV | 40 | 🔄33 | ↑1.005 | ↓23d | PV | -7.3% | -53.98/-54.44 | +4.45% | 20% |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA)<br><sub>📶W9 · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Wealth management advisory, broking, trading for HNI UHNIs | ⚡ BULL_ANY_PPV | 29 | ↑68 | ↑1.011 | ↑1d | PV | +3.0% | -32.94/-36.83 | +2.96% | 20% |
| [PACEDIGITK](https://in.tradingview.com/chart/?symbol=NSE:PACEDIGITK)<br><sub>📶W9 · 🚀SS·12x · ↓CMF30d</sub> | ✓ SAFE | Telecom fiber networks, power systems, energy infrastructure solutions | ⚡ BULL_ANY_PPV | 24 | ↑50 | ↑1.026 | ↑1d | PV | +4.6% | -9.11/-16.43 | +4.61% | 20% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>📶W9 · W↑34d · ↑CMF14d</sub> | ✓ SAFE | Home textiles manufacturer, flooring, global export focus | ⚡ BULL_ANY_PPV | 8 | ↑95 | ↑1.065 | ↑12d | PV | +18.6% | 65.58/62.9 | +5.21% | 20% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Private bank retail deposits lending commercial operations | ⚡ BULL_ANY_PPV | 5 | ↑76 | ↑1.000 | ↓30d | PV | -2.6% | -42.33/-43.97 | +0.15% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS)<br><sub>📶W9 · ↓CMF3d · 🎯SLING</sub> | ⚠ CAUTION | Engineering R&D services for automotive semiconductor industrial | 🟢 BULL_OVERSOLD | 10 | ↑35 | ↑1.008 | ↓25d | — | -7.6% | -57.11/-61.4 | +1.21% | 20% |
| [CUB](https://in.tradingview.com/chart/?symbol=NSE:CUB)<br><sub>📶W9 · W↑29d · ↓CMF6d</sub> | ⚠ CAUTION | Private bank serving SMEs, MSMEs, retail customers South India | 📈 BULL_ANY_MID | 63 | ↑45 | ↑1.022 | ↑2d | SQ | +7.0% | -14.29/-17.34 | +1.77% | 20% |
| [SWARAJ](https://in.tradingview.com/chart/?symbol=NSE:SWARAJ)<br><sub>📶W9 · W↑42d · 🚀SS · ↓CMF6d</sub> | n/a | Cotton synthetic fabric manufacturer for apparel and textiles | 📈 BULL_ANY_MID | 63 | ↑90 | ↑1.018 | ↑2d | SQ | +2.6% | 48.1/45.36 | +1.22% | 20% |
| [GPPL](https://in.tradingview.com/chart/?symbol=NSE:GPPL)<br><sub>📶W9 · W↑39d · ↓CMF30d</sub> | ✓ SAFE | Container and breakbulk cargo port operations Gujarat coast | 📈 BULL_ANY_MID | 58 | ↑58 | ↓1.014 | ↑2d | SQ | +3.3% | 9.2/0.19 | -0.52% | 20% |
| [ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Bed linen manufacturer, global exports, home textiles | 📈 BULL_ANY_MID | 58 | ↑86 | ↓0.994 | ↓2d | SQ | +2.0% | 19.4/18.9 | -3.64% | 20% 🟦 |
| [BIRLACABLE](https://in.tradingview.com/chart/?symbol=NSE:BIRLACABLE)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Telecom cables, wires, specialized cables manufacturer | 📈 BULL_ANY_MID | 58 | ↑99 | ↓1.030 | ↑2d | SQ | +3.8% | 23.48/21.85 | +0.49% | 5% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>📶W9 · W↑29d · ↓CMF4d</sub> | ✓ SAFE | Refurbished laptops desktops electronics retail distribution | 📈 BULL_ANY_MID | 57 | ↑94 | ↑1.031 | ↑3d | SQ | +4.8% | 39.59/37.33 | +2.61% | 5% 🟥 |
| [SIS](https://in.tradingview.com/chart/?symbol=NSE:SIS)<br><sub>📶W9 · ↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Manned security guarding cash logistics facility management services | 📈 BULL_ANY_MID | 57 | ↑70 | ↓0.992 | ↓3d | SQ | +4.7% | -34.75/-36.7 | -1.49% | 20% |
| [TBOTEK](https://in.tradingview.com/chart/?symbol=NSE:TBOTEK)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | B2B travel booking platform connecting hotels airlines agents | 📈 BULL_ANY_MID | 55 | ↑72 | ↓0.994 | ↓5d | SQ | -0.9% | 1.37/-1.03 | -0.81% | 20% |
| [AEROPLANE](https://in.tradingview.com/chart/?symbol=NSE:AEROPLANE)<br><sub>📶W9 · ↑CMF19d</sub> | ✓ SAFE | Basmati rice processor and exporter for global markets | 📈 BULL_ANY_MID | 50 | ↑50 | ↓1.018 | ↑10d | SQ | +8.3% | 40.19/38.54 | +0.07% | 20% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | IT services, digital transformation, financial and travel sectors | 📈 BULL_ANY_MID | 24 | ↑76 | ↑1.021 | ↑1d | — | +4.4% | -27.0/-30.77 | +4.40% | 20% |
| [IDBI](https://in.tradingview.com/chart/?symbol=NSE:IDBI)<br><sub>📶W9 · ↓CMF17d</sub> | ⚠ CAUTION | Retail corporate MSME lending deposit bank | 📈 BULL_ANY_MID | 19 | ↑53 | ↑1.031 | ↑1d | — | +5.3% | -9.69/-15.62 | +5.32% | 20% 🟦 |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH)<br><sub>📶W9 · W↑122d · ↑CMF17d</sub> | ✓ SAFE | Precision aerospace components, tooling, defense manufacturing | 📈 BULL_ANY_MID | 17 | ↑96 | ↑1.055 | ↑3d | — | +9.7% | 56.37/53.08 | +2.84% | 10% 🟩 |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 14 | ↑60 | ↑0.998 | ↓11d | — | -3.2% | -35.97/-36.7 | +0.74% | 20% |
| [MOLDTKPAC](https://in.tradingview.com/chart/?symbol=NSE:MOLDTKPAC)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Injection-molded rigid plastic containers for lubricants paints food | 📈 BULL_ANY_MID | 13 | ↑51 | ↓0.998 | ↓7d | — | +3.0% | -38.73/-39.61 | -0.26% | 20% |
| [PERSISTENT](https://in.tradingview.com/chart/?symbol=NSE:PERSISTENT)<br><sub>📶W9 · ↓CMF12d</sub> | ✓ SAFE | Digital engineering services, cloud modernization, enterprise software | 📈 BULL_ANY_MID | 10 | ↑55 | ↑1.006 | ↓23d | — | -4.1% | -45.43/-47.83 | +1.67% | 20% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · W↑49d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Stainless steel washers tubes pipes solar mounting components | 📈 BULL_ANY_MID | 9 | ↑98 | ↑1.054 | ↑11d | — | +20.5% | 58.33/57.56 | +4.44% | 20% |
| [MONTECARLO](https://in.tradingview.com/chart/?symbol=NSE:MONTECARLO)<br><sub>📶W9 · ↓CMF17d</sub> | ✓ SAFE | Woolen cotton apparel manufacturer winter wear retail | 📈 BULL_ANY_MID | 9 | ↑34 | ↓0.991 | ↓11d | — | -4.9% | -41.84/-42.43 | -0.87% | 20% |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH)<br><sub>📶W9 · W↑39d · ★ · ↑CMF12d</sub> | ✓ SAFE | Aerospace defense semiconductor precision components manufacturing | 📈 BULL_ANY_MID | 0 | ↑96 | ↓1.062 | ↑27d | — | +44.9% | 69.76/68.64 | +1.27% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CCL,NSE:GOPAL,NSE:INDUSTOWER,NSE:LEMONTREE,NSE:TARIL,NSE:SCHNEIDER,NSE:GKSL,NSE:GREENPLY,NSE:ATLANTAELE,NSE:MPHASIS,NSE:NUVAMA,NSE:PACEDIGITK,NSE:WELSPUNLIV,NSE:KARURVYSYA,NSE:SIGMAADV,NSE:LTTS,NSE:CUB,NSE:SWARAJ,NSE:GPPL,NSE:ICIL,NSE:BIRLACABLE,NSE:EBGNG,NSE:SIS,NSE:TBOTEK,NSE:AEROPLANE,NSE:COFORGE,NSE:IDBI,NSE:UNIMECH,NSE:GRASIM,NSE:MOLDTKPAC,NSE:PERSISTENT,NSE:RATNAVEER,NSE:MONTECARLO,NSE:ROSSTECH
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (47)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CCL](https://in.tradingview.com/chart/?symbol=NSE:CCL)<br><sub>📶W9 · ↑CMF10d · 🎯SLING</sub> | ⚠ CAUTION | Instant coffee manufacturer, global export, beverage | 🔥 BULL_OS_PPV | 59 | 🔄53 | ↑1.013 | ↑1d | PV | +3.6% | -62.07/-65.1 | +3.64% | 20% |
| [GOPAL](https://in.tradingview.com/chart/?symbol=NSE:GOPAL)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Ethnic and western snacks manufacturer serving Indian households | ⚡ BULL_ANY_PPV | 88 | 🔄29 | ↑0.994 | ↓7d | SQ·PV | -1.4% | -27.6/-29.76 | +1.51% | 20% |
| [INDUSTOWER](https://in.tradingview.com/chart/?symbol=NSE:INDUSTOWER)<br><sub>📶W9 · ↓CMF6d</sub> | ✓ SAFE | Telecom tower infrastructure operator serving mobile networks | ⚡ BULL_ANY_PPV | 69 | ↑44 | ↑1.006 | ↑1d | SQ·PV | +0.8% | -20.73/-23.54 | +0.82% | 20% |
| [LEMONTREE](https://in.tradingview.com/chart/?symbol=NSE:LEMONTREE)<br><sub>📶W9 · W↑4d · RVOL15x · ↓CMF30d</sub> | ✓ SAFE | Mid-market hotel chain business leisure travelers India | ⚡ BULL_ANY_PPV | 64 | ↑16 | ↑1.019 | ↑1d | SQ·PV | +3.3% | -17.85/-24.44 | +3.28% | 20% |
| [TARIL](https://in.tradingview.com/chart/?symbol=NSE:TARIL)<br><sub>📶W9 · 🚀SS·69x · ↓CMF30d</sub> | ✓ SAFE | Power transformers, furnace transformers, electrical equipment manufacturing | ⚡ BULL_ANY_PPV | 59 | 🔄21 | ↑1.010 | ↑1d | PV | +4.0% | -43.96/-49.46 | +3.96% | 20% |
| [SCHNEIDER](https://in.tradingview.com/chart/?symbol=NSE:SCHNEIDER)<br><sub>📶W9 · ↑CMF10d</sub> | ✓ SAFE | Power distribution equipment manufacturing and servicing | ⚡ BULL_ANY_PPV | 59 | ↑79 | ↑1.046 | ↑1d | SQ·PV | +6.0% | 7.69/-1.21 | +5.98% | 10% 🟩 |
| [GKSL](https://in.tradingview.com/chart/?symbol=NSE:GKSL)<br><sub>📶W9 · 🚀SS·59x · ↓CMF11d</sub> | ✓ SAFE | Nephrology urology hospital super-specialty services Gujarat | ⚡ BULL_ANY_PPV | 58 | ↑50 | ↑1.086 | ↑2d | SQ·PV | +11.2% | 51.73/40.4 | +9.23% | 20% |
| [GREENPLY](https://in.tradingview.com/chart/?symbol=NSE:GREENPLY)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Plywood MDF doors flooring for residential commercial construction | ⚡ BULL_ANY_PPV | 58 | ↑64 | ↑1.038 | ↑2d | SQ·PV | +8.4% | 4.04/-4.21 | +1.25% | 20% |
| [ATLANTAELE](https://in.tradingview.com/chart/?symbol=NSE:ATLANTAELE)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | High-voltage transformers for power generation transmission distribution | ⚡ BULL_ANY_PPV | 49 | 🔄50 | ↑1.034 | ↑1d | PV | +6.7% | -26.32/-31.06 | +6.74% | 5% 🟥 |
| [MPHASIS](https://in.tradingview.com/chart/?symbol=NSE:MPHASIS)<br><sub>📶W9 · 🚀SS · ↓CMF15d · 🎯SLING</sub> | ✓ SAFE | IT services, cloud and cognitive transformation, enterprise clients | ⚡ BULL_ANY_PPV | 40 | 🔄33 | ↑1.005 | ↓23d | PV | -7.3% | -53.98/-54.44 | +4.45% | 20% |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA)<br><sub>📶W9 · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Wealth management advisory, broking, trading for HNI UHNIs | ⚡ BULL_ANY_PPV | 29 | ↑68 | ↑1.011 | ↑1d | PV | +3.0% | -32.94/-36.83 | +2.96% | 20% |
| [PACEDIGITK](https://in.tradingview.com/chart/?symbol=NSE:PACEDIGITK)<br><sub>📶W9 · 🚀SS·12x · ↓CMF30d</sub> | ✓ SAFE | Telecom fiber networks, power systems, energy infrastructure solutions | ⚡ BULL_ANY_PPV | 24 | ↑50 | ↑1.026 | ↑1d | PV | +4.6% | -9.11/-16.43 | +4.61% | 20% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>📶W9 · W↑34d · ↑CMF14d</sub> | ✓ SAFE | Home textiles manufacturer, flooring, global export focus | ⚡ BULL_ANY_PPV | 8 | ↑95 | ↑1.065 | ↑12d | PV | +18.6% | 65.58/62.9 | +5.21% | 20% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Private bank retail deposits lending commercial operations | ⚡ BULL_ANY_PPV | 5 | ↑76 | ↑1.000 | ↓30d | PV | -2.6% | -42.33/-43.97 | +0.15% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS)<br><sub>📶W9 · ↓CMF3d · 🎯SLING</sub> | ⚠ CAUTION | Engineering R&D services for automotive semiconductor industrial | 🟢 BULL_OVERSOLD | 10 | ↑35 | ↑1.008 | ↓25d | — | -7.6% | -57.11/-61.4 | +1.21% | 20% |
| [CUB](https://in.tradingview.com/chart/?symbol=NSE:CUB)<br><sub>📶W9 · W↑29d · ↓CMF6d</sub> | ⚠ CAUTION | Private bank serving SMEs, MSMEs, retail customers South India | 📈 BULL_ANY_MID | 63 | ↑45 | ↑1.022 | ↑2d | SQ | +7.0% | -14.29/-17.34 | +1.77% | 20% |
| [SWARAJ](https://in.tradingview.com/chart/?symbol=NSE:SWARAJ)<br><sub>📶W9 · W↑42d · 🚀SS · ↓CMF6d</sub> | n/a | Cotton synthetic fabric manufacturer for apparel and textiles | 📈 BULL_ANY_MID | 63 | ↑90 | ↑1.018 | ↑2d | SQ | +2.6% | 48.1/45.36 | +1.22% | 20% |
| [GPPL](https://in.tradingview.com/chart/?symbol=NSE:GPPL)<br><sub>📶W9 · W↑39d · ↓CMF30d</sub> | ✓ SAFE | Container and breakbulk cargo port operations Gujarat coast | 📈 BULL_ANY_MID | 58 | ↑58 | ↓1.014 | ↑2d | SQ | +3.3% | 9.2/0.19 | -0.52% | 20% |
| [ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Bed linen manufacturer, global exports, home textiles | 📈 BULL_ANY_MID | 58 | ↑86 | ↓0.994 | ↓2d | SQ | +2.0% | 19.4/18.9 | -3.64% | 20% 🟦 |
| [BIRLACABLE](https://in.tradingview.com/chart/?symbol=NSE:BIRLACABLE)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Telecom cables, wires, specialized cables manufacturer | 📈 BULL_ANY_MID | 58 | ↑99 | ↓1.030 | ↑2d | SQ | +3.8% | 23.48/21.85 | +0.49% | 5% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>📶W9 · W↑29d · ↓CMF4d</sub> | ✓ SAFE | Refurbished laptops desktops electronics retail distribution | 📈 BULL_ANY_MID | 57 | ↑94 | ↑1.031 | ↑3d | SQ | +4.8% | 39.59/37.33 | +2.61% | 5% 🟥 |
| [SIS](https://in.tradingview.com/chart/?symbol=NSE:SIS)<br><sub>📶W9 · ↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Manned security guarding cash logistics facility management services | 📈 BULL_ANY_MID | 57 | ↑70 | ↓0.992 | ↓3d | SQ | +4.7% | -34.75/-36.7 | -1.49% | 20% |
| [TBOTEK](https://in.tradingview.com/chart/?symbol=NSE:TBOTEK)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | B2B travel booking platform connecting hotels airlines agents | 📈 BULL_ANY_MID | 55 | ↑72 | ↓0.994 | ↓5d | SQ | -0.9% | 1.37/-1.03 | -0.81% | 20% |
| [AEROPLANE](https://in.tradingview.com/chart/?symbol=NSE:AEROPLANE)<br><sub>📶W9 · ↑CMF19d</sub> | ✓ SAFE | Basmati rice processor and exporter for global markets | 📈 BULL_ANY_MID | 50 | ↑50 | ↓1.018 | ↑10d | SQ | +8.3% | 40.19/38.54 | +0.07% | 20% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | IT services, digital transformation, financial and travel sectors | 📈 BULL_ANY_MID | 24 | ↑76 | ↑1.021 | ↑1d | — | +4.4% | -27.0/-30.77 | +4.40% | 20% |
| [IDBI](https://in.tradingview.com/chart/?symbol=NSE:IDBI)<br><sub>📶W9 · ↓CMF17d</sub> | ⚠ CAUTION | Retail corporate MSME lending deposit bank | 📈 BULL_ANY_MID | 19 | ↑53 | ↑1.031 | ↑1d | — | +5.3% | -9.69/-15.62 | +5.32% | 20% 🟦 |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH)<br><sub>📶W9 · W↑122d · ↑CMF17d</sub> | ✓ SAFE | Precision aerospace components, tooling, defense manufacturing | 📈 BULL_ANY_MID | 17 | ↑96 | ↑1.055 | ↑3d | — | +9.7% | 56.37/53.08 | +2.84% | 10% 🟩 |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 14 | ↑60 | ↑0.998 | ↓11d | — | -3.2% | -35.97/-36.7 | +0.74% | 20% |
| [MOLDTKPAC](https://in.tradingview.com/chart/?symbol=NSE:MOLDTKPAC)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Injection-molded rigid plastic containers for lubricants paints food | 📈 BULL_ANY_MID | 13 | ↑51 | ↓0.998 | ↓7d | — | +3.0% | -38.73/-39.61 | -0.26% | 20% |
| [PERSISTENT](https://in.tradingview.com/chart/?symbol=NSE:PERSISTENT)<br><sub>📶W9 · ↓CMF12d</sub> | ✓ SAFE | Digital engineering services, cloud modernization, enterprise software | 📈 BULL_ANY_MID | 10 | ↑55 | ↑1.006 | ↓23d | — | -4.1% | -45.43/-47.83 | +1.67% | 20% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · W↑49d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Stainless steel washers tubes pipes solar mounting components | 📈 BULL_ANY_MID | 9 | ↑98 | ↑1.054 | ↑11d | — | +20.5% | 58.33/57.56 | +4.44% | 20% |
| [MONTECARLO](https://in.tradingview.com/chart/?symbol=NSE:MONTECARLO)<br><sub>📶W9 · ↓CMF17d</sub> | ✓ SAFE | Woolen cotton apparel manufacturer winter wear retail | 📈 BULL_ANY_MID | 9 | ↑34 | ↓0.991 | ↓11d | — | -4.9% | -41.84/-42.43 | -0.87% | 20% |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH)<br><sub>📶W9 · W↑39d · ★ · ↑CMF12d</sub> | ✓ SAFE | Aerospace defense semiconductor precision components manufacturing | 📈 BULL_ANY_MID | 0 | ↑96 | ↓1.062 | ↑27d | — | +44.9% | 69.76/68.64 | +1.27% | 20% |
| [SASKEN](https://in.tradingview.com/chart/?symbol=NSE:SASKEN)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Product engineering, semiconductors, automotive, consumer electronics | 🟢 BULL_OVERSOLD | 53 | 🔄64 | ↑1.006 | ↓7d | — | -2.0% | -58.66/-60.27 | +2.86% | 5% 🟥 |
| [AADHARHFC](https://in.tradingview.com/chart/?symbol=NSE:AADHARHFC)<br><sub>↓CMF4d · 🎯SLING</sub> | ✓ SAFE | Low-income housing loans, retail, affordable home buyers | 🟢 BULL_OVERSOLD | 51 | 🔄30 | ↑1.003 | ↓9d | — | -2.9% | -61.56/-63.08 | +2.84% | 20% 🟦 |
| [VINATIORGA](https://in.tradingview.com/chart/?symbol=NSE:VINATIORGA)<br><sub>↓CMF16d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Specialty chemicals, monomers, antioxidants, polymers manufacturer | 🟢 BULL_OVERSOLD | 42 | 🔄20 | ↑1.000 | ↓18d | — | -7.0% | -65.26/-67.07 | +3.41% | 20% |
| [TEAMLEASE](https://in.tradingview.com/chart/?symbol=NSE:TEAMLEASE)<br><sub>↓CMF18d · 🎯SLING</sub> | ⚠ CAUTION | Staffing recruitment payroll HR services employer solutions | 🟢 BULL_OVERSOLD | 36 | 🔄16 | ↑0.999 | ↓19d | — | -5.7% | -64.23/-64.84 | +2.68% | 20% |
| [PREMIERENE](https://in.tradingview.com/chart/?symbol=NSE:PREMIERENE)<br><sub>↓CMF3d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Solar cells modules manufacturing renewable energy | 🟢 BULL_OVERSOLD | 35 | 🔄34 | ↑0.979 | ↓24d | — | -13.4% | -64.95/-65.01 | +0.91% | 20% |
| [ICRA](https://in.tradingview.com/chart/?symbol=NSE:ICRA)<br><sub>↓CMF23d · 🎯SLING</sub> | ✓ SAFE | Credit ratings, debt analysis, capital markets participants | 🟢 BULL_OVERSOLD | 35 | 🔄9 | ↑0.980 | ↓23d | — | -12.2% | -71.61/-71.63 | +2.04% | 20% |
| [EQUITASBNK](https://in.tradingview.com/chart/?symbol=NSE:EQUITASBNK)<br><sub>↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION | Small finance bank serving underbanked individuals and SMEs | 🟢 BULL_OVERSOLD | 10 | ↑56 | ↓0.986 | ↓10d | — | -5.2% | -66.77/-69.39 | -0.75% | 20% |
| [TRAVELFOOD](https://in.tradingview.com/chart/?symbol=NSE:TRAVELFOOD)<br><sub>↑CMF2d · 🎯SLING</sub> | ⚠ CAUTION | Airport railway highway food beverage QSR operations | 🟢 BULL_OVERSOLD | 5 | ↑41 | ↑0.994 | ↓26d | — | -6.2% | -58.99/-60.02 | +0.65% | 20% |
| [HONDAPOWER](https://in.tradingview.com/chart/?symbol=NSE:HONDAPOWER)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 5 | ↑20 | ↑0.992 | ↓39d | — | -9.9% | -62.12/-62.26 | +0.63% | 20% |
| [THERMAX](https://in.tradingview.com/chart/?symbol=NSE:THERMAX)<br><sub>↓CMF24d · 🎯SLING</sub> | ✓ SAFE | Industrial boilers, cooling systems, power equipment, pollution control | 🟢 BULL_OVERSOLD | 0 | ↑37 | ↓0.979 | ↓53d | — | -28.7% | -65.46/-66.18 | -0.93% | 20% |
| [HEXT](https://in.tradingview.com/chart/?symbol=NSE:HEXT)<br><sub>↓CMF3d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | IT services, digital transformation, automation, enterprise clients | 🟡 BULL_OS_L2 | 9 | ↑23 | ↓0.985 | ↓11d | — | -6.2% | -58.51/-59.48 | -0.74% | 20% |
| [ARIHANT](https://in.tradingview.com/chart/?symbol=NSE:ARIHANT)<br><sub>↑CMF1d</sub> | ⚠ CAUTION | Residential commercial construction developer Chennai region | 📈 BULL_ANY_MID | 56 | ↑50 | ↓0.992 | ↓4d | SQ | -0.1% | -23.58/-24.0 | -0.73% | 20% |
| [MASTEK](https://in.tradingview.com/chart/?symbol=NSE:MASTEK)<br><sub>↓CMF4d</sub> | ✓ SAFE | Digital engineering, Oracle Cloud, enterprise transformation | 📈 BULL_ANY_MID | 0 | ↑28 | ↓0.990 | ↓23d | — | -11.0% | -48.2/-49.79 | -0.46% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CCL,NSE:GOPAL,NSE:INDUSTOWER,NSE:LEMONTREE,NSE:TARIL,NSE:SCHNEIDER,NSE:GKSL,NSE:GREENPLY,NSE:ATLANTAELE,NSE:MPHASIS,NSE:NUVAMA,NSE:PACEDIGITK,NSE:WELSPUNLIV,NSE:KARURVYSYA,NSE:SIGMAADV,NSE:LTTS,NSE:CUB,NSE:SWARAJ,NSE:GPPL,NSE:ICIL,NSE:BIRLACABLE,NSE:EBGNG,NSE:SIS,NSE:TBOTEK,NSE:AEROPLANE,NSE:COFORGE,NSE:IDBI,NSE:UNIMECH,NSE:GRASIM,NSE:MOLDTKPAC,NSE:PERSISTENT,NSE:RATNAVEER,NSE:MONTECARLO,NSE:ROSSTECH,NSE:SASKEN,NSE:AADHARHFC,NSE:VINATIORGA,NSE:TEAMLEASE,NSE:PREMIERENE,NSE:ICRA,NSE:EQUITASBNK,NSE:TRAVELFOOD,NSE:HONDAPOWER,NSE:THERMAX,NSE:HEXT,NSE:ARIHANT,NSE:MASTEK
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (16)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GOPAL](https://in.tradingview.com/chart/?symbol=NSE:GOPAL)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Ethnic and western snacks manufacturer serving Indian households | ⚡ BULL_ANY_PPV | 88 | 🔄29 | ↑0.994 | ↓7d | SQ·PV | -1.4% | -27.6/-29.76 | +1.51% | 20% |
| [INDUSTOWER](https://in.tradingview.com/chart/?symbol=NSE:INDUSTOWER)<br><sub>📶W9 · ↓CMF6d</sub> | ✓ SAFE | Telecom tower infrastructure operator serving mobile networks | ⚡ BULL_ANY_PPV | 69 | ↑44 | ↑1.006 | ↑1d | SQ·PV | +0.8% | -20.73/-23.54 | +0.82% | 20% |
| [LEMONTREE](https://in.tradingview.com/chart/?symbol=NSE:LEMONTREE)<br><sub>📶W9 · W↑4d · RVOL15x · ↓CMF30d</sub> | ✓ SAFE | Mid-market hotel chain business leisure travelers India | ⚡ BULL_ANY_PPV | 64 | ↑16 | ↑1.019 | ↑1d | SQ·PV | +3.3% | -17.85/-24.44 | +3.28% | 20% |
| [SCHNEIDER](https://in.tradingview.com/chart/?symbol=NSE:SCHNEIDER)<br><sub>📶W9 · ↑CMF10d</sub> | ✓ SAFE | Power distribution equipment manufacturing and servicing | ⚡ BULL_ANY_PPV | 59 | ↑79 | ↑1.046 | ↑1d | SQ·PV | +6.0% | 7.69/-1.21 | +5.98% | 10% 🟩 |
| [GKSL](https://in.tradingview.com/chart/?symbol=NSE:GKSL)<br><sub>📶W9 · 🚀SS·59x · ↓CMF11d</sub> | ✓ SAFE | Nephrology urology hospital super-specialty services Gujarat | ⚡ BULL_ANY_PPV | 58 | ↑50 | ↑1.086 | ↑2d | SQ·PV | +11.2% | 51.73/40.4 | +9.23% | 20% |
| [GREENPLY](https://in.tradingview.com/chart/?symbol=NSE:GREENPLY)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Plywood MDF doors flooring for residential commercial construction | ⚡ BULL_ANY_PPV | 58 | ↑64 | ↑1.038 | ↑2d | SQ·PV | +8.4% | 4.04/-4.21 | +1.25% | 20% |
| [CUB](https://in.tradingview.com/chart/?symbol=NSE:CUB)<br><sub>📶W9 · W↑29d · ↓CMF6d</sub> | ⚠ CAUTION | Private bank serving SMEs, MSMEs, retail customers South India | 📈 BULL_ANY_MID | 63 | ↑45 | ↑1.022 | ↑2d | SQ | +7.0% | -14.29/-17.34 | +1.77% | 20% |
| [SWARAJ](https://in.tradingview.com/chart/?symbol=NSE:SWARAJ)<br><sub>📶W9 · W↑42d · 🚀SS · ↓CMF6d</sub> | n/a | Cotton synthetic fabric manufacturer for apparel and textiles | 📈 BULL_ANY_MID | 63 | ↑90 | ↑1.018 | ↑2d | SQ | +2.6% | 48.1/45.36 | +1.22% | 20% |
| [GPPL](https://in.tradingview.com/chart/?symbol=NSE:GPPL)<br><sub>📶W9 · W↑39d · ↓CMF30d</sub> | ✓ SAFE | Container and breakbulk cargo port operations Gujarat coast | 📈 BULL_ANY_MID | 58 | ↑58 | ↓1.014 | ↑2d | SQ | +3.3% | 9.2/0.19 | -0.52% | 20% |
| [ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Bed linen manufacturer, global exports, home textiles | 📈 BULL_ANY_MID | 58 | ↑86 | ↓0.994 | ↓2d | SQ | +2.0% | 19.4/18.9 | -3.64% | 20% 🟦 |
| [BIRLACABLE](https://in.tradingview.com/chart/?symbol=NSE:BIRLACABLE)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Telecom cables, wires, specialized cables manufacturer | 📈 BULL_ANY_MID | 58 | ↑99 | ↓1.030 | ↑2d | SQ | +3.8% | 23.48/21.85 | +0.49% | 5% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>📶W9 · W↑29d · ↓CMF4d</sub> | ✓ SAFE | Refurbished laptops desktops electronics retail distribution | 📈 BULL_ANY_MID | 57 | ↑94 | ↑1.031 | ↑3d | SQ | +4.8% | 39.59/37.33 | +2.61% | 5% 🟥 |
| [SIS](https://in.tradingview.com/chart/?symbol=NSE:SIS)<br><sub>📶W9 · ↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Manned security guarding cash logistics facility management services | 📈 BULL_ANY_MID | 57 | ↑70 | ↓0.992 | ↓3d | SQ | +4.7% | -34.75/-36.7 | -1.49% | 20% |
| [TBOTEK](https://in.tradingview.com/chart/?symbol=NSE:TBOTEK)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | B2B travel booking platform connecting hotels airlines agents | 📈 BULL_ANY_MID | 55 | ↑72 | ↓0.994 | ↓5d | SQ | -0.9% | 1.37/-1.03 | -0.81% | 20% |
| [AEROPLANE](https://in.tradingview.com/chart/?symbol=NSE:AEROPLANE)<br><sub>📶W9 · ↑CMF19d</sub> | ✓ SAFE | Basmati rice processor and exporter for global markets | 📈 BULL_ANY_MID | 50 | ↑50 | ↓1.018 | ↑10d | SQ | +8.3% | 40.19/38.54 | +0.07% | 20% |
| [ARIHANT](https://in.tradingview.com/chart/?symbol=NSE:ARIHANT)<br><sub>↑CMF1d</sub> | ⚠ CAUTION | Residential commercial construction developer Chennai region | 📈 BULL_ANY_MID | 56 | ↑50 | ↓0.992 | ↓4d | SQ | -0.1% | -23.58/-24.0 | -0.73% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GOPAL,NSE:INDUSTOWER,NSE:LEMONTREE,NSE:SCHNEIDER,NSE:GKSL,NSE:GREENPLY,NSE:CUB,NSE:SWARAJ,NSE:GPPL,NSE:ICIL,NSE:BIRLACABLE,NSE:EBGNG,NSE:SIS,NSE:TBOTEK,NSE:AEROPLANE,NSE:ARIHANT
```

---

### 🔥 MAJOR — PPV confirmed (9)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CCL](https://in.tradingview.com/chart/?symbol=NSE:CCL)<br><sub>📶W9 · ↑CMF10d · 🎯SLING</sub> | ⚠ CAUTION | Instant coffee manufacturer, global export, beverage | 🔥 BULL_OS_PPV | 59 | 🔄53 | ↑1.013 | ↑1d | PV | +3.6% | -62.07/-65.1 | +3.64% | 20% |
| [TARIL](https://in.tradingview.com/chart/?symbol=NSE:TARIL)<br><sub>📶W9 · 🚀SS·69x · ↓CMF30d</sub> | ✓ SAFE | Power transformers, furnace transformers, electrical equipment manufacturing | ⚡ BULL_ANY_PPV | 59 | 🔄21 | ↑1.010 | ↑1d | PV | +4.0% | -43.96/-49.46 | +3.96% | 20% |
| [ATLANTAELE](https://in.tradingview.com/chart/?symbol=NSE:ATLANTAELE)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | High-voltage transformers for power generation transmission distribution | ⚡ BULL_ANY_PPV | 49 | 🔄50 | ↑1.034 | ↑1d | PV | +6.7% | -26.32/-31.06 | +6.74% | 5% 🟥 |
| [MPHASIS](https://in.tradingview.com/chart/?symbol=NSE:MPHASIS)<br><sub>📶W9 · 🚀SS · ↓CMF15d · 🎯SLING</sub> | ✓ SAFE | IT services, cloud and cognitive transformation, enterprise clients | ⚡ BULL_ANY_PPV | 40 | 🔄33 | ↑1.005 | ↓23d | PV | -7.3% | -53.98/-54.44 | +4.45% | 20% |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA)<br><sub>📶W9 · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Wealth management advisory, broking, trading for HNI UHNIs | ⚡ BULL_ANY_PPV | 29 | ↑68 | ↑1.011 | ↑1d | PV | +3.0% | -32.94/-36.83 | +2.96% | 20% |
| [PACEDIGITK](https://in.tradingview.com/chart/?symbol=NSE:PACEDIGITK)<br><sub>📶W9 · 🚀SS·12x · ↓CMF30d</sub> | ✓ SAFE | Telecom fiber networks, power systems, energy infrastructure solutions | ⚡ BULL_ANY_PPV | 24 | ↑50 | ↑1.026 | ↑1d | PV | +4.6% | -9.11/-16.43 | +4.61% | 20% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>📶W9 · W↑34d · ↑CMF14d</sub> | ✓ SAFE | Home textiles manufacturer, flooring, global export focus | ⚡ BULL_ANY_PPV | 8 | ↑95 | ↑1.065 | ↑12d | PV | +18.6% | 65.58/62.9 | +5.21% | 20% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Private bank retail deposits lending commercial operations | ⚡ BULL_ANY_PPV | 5 | ↑76 | ↑1.000 | ↓30d | PV | -2.6% | -42.33/-43.97 | +0.15% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CCL,NSE:TARIL,NSE:ATLANTAELE,NSE:MPHASIS,NSE:NUVAMA,NSE:PACEDIGITK,NSE:WELSPUNLIV,NSE:KARURVYSYA,NSE:SIGMAADV
```

### 🟢 OVERSOLD — reversal from −53/−60 (14)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS)<br><sub>📶W9 · ↓CMF3d · 🎯SLING</sub> | ⚠ CAUTION | Engineering R&D services for automotive semiconductor industrial | 🟢 BULL_OVERSOLD | 10 | ↑35 | ↑1.008 | ↓25d | — | -7.6% | -57.11/-61.4 | +1.21% | 20% |
| [SASKEN](https://in.tradingview.com/chart/?symbol=NSE:SASKEN)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Product engineering, semiconductors, automotive, consumer electronics | 🟢 BULL_OVERSOLD | 53 | 🔄64 | ↑1.006 | ↓7d | — | -2.0% | -58.66/-60.27 | +2.86% | 5% 🟥 |
| [AADHARHFC](https://in.tradingview.com/chart/?symbol=NSE:AADHARHFC)<br><sub>↓CMF4d · 🎯SLING</sub> | ✓ SAFE | Low-income housing loans, retail, affordable home buyers | 🟢 BULL_OVERSOLD | 51 | 🔄30 | ↑1.003 | ↓9d | — | -2.9% | -61.56/-63.08 | +2.84% | 20% 🟦 |
| [VINATIORGA](https://in.tradingview.com/chart/?symbol=NSE:VINATIORGA)<br><sub>↓CMF16d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Specialty chemicals, monomers, antioxidants, polymers manufacturer | 🟢 BULL_OVERSOLD | 42 | 🔄20 | ↑1.000 | ↓18d | — | -7.0% | -65.26/-67.07 | +3.41% | 20% |
| [TEAMLEASE](https://in.tradingview.com/chart/?symbol=NSE:TEAMLEASE)<br><sub>↓CMF18d · 🎯SLING</sub> | ⚠ CAUTION | Staffing recruitment payroll HR services employer solutions | 🟢 BULL_OVERSOLD | 36 | 🔄16 | ↑0.999 | ↓19d | — | -5.7% | -64.23/-64.84 | +2.68% | 20% |
| [PREMIERENE](https://in.tradingview.com/chart/?symbol=NSE:PREMIERENE)<br><sub>↓CMF3d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Solar cells modules manufacturing renewable energy | 🟢 BULL_OVERSOLD | 35 | 🔄34 | ↑0.979 | ↓24d | — | -13.4% | -64.95/-65.01 | +0.91% | 20% |
| [ICRA](https://in.tradingview.com/chart/?symbol=NSE:ICRA)<br><sub>↓CMF23d · 🎯SLING</sub> | ✓ SAFE | Credit ratings, debt analysis, capital markets participants | 🟢 BULL_OVERSOLD | 35 | 🔄9 | ↑0.980 | ↓23d | — | -12.2% | -71.61/-71.63 | +2.04% | 20% |
| [CONCOR](https://in.tradingview.com/chart/?symbol=NSE:CONCOR)<br><sub>↓CMF28d · ⚠️TRAP</sub> | ✓ SAFE | Rail container logistics, port management, multimodal freight | 🟢 BULL_OVERSOLD | 10 | ↓34 | ↓0.960 | ↓10d | — | -9.4% | -78.08/-78.3 | -1.23% | 20% |
| [EQUITASBNK](https://in.tradingview.com/chart/?symbol=NSE:EQUITASBNK)<br><sub>↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION | Small finance bank serving underbanked individuals and SMEs | 🟢 BULL_OVERSOLD | 10 | ↑56 | ↓0.986 | ↓10d | — | -5.2% | -66.77/-69.39 | -0.75% | 20% |
| [TRAVELFOOD](https://in.tradingview.com/chart/?symbol=NSE:TRAVELFOOD)<br><sub>↑CMF2d · 🎯SLING</sub> | ⚠ CAUTION | Airport railway highway food beverage QSR operations | 🟢 BULL_OVERSOLD | 5 | ↑41 | ↑0.994 | ↓26d | — | -6.2% | -58.99/-60.02 | +0.65% | 20% |
| [HONDAPOWER](https://in.tradingview.com/chart/?symbol=NSE:HONDAPOWER)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 5 | ↑20 | ↑0.992 | ↓39d | — | -9.9% | -62.12/-62.26 | +0.63% | 20% |
| [INDUSINDBK](https://in.tradingview.com/chart/?symbol=NSE:INDUSINDBK)<br><sub>↓CMF0d · ⚠️TRAP</sub> | ✓ SAFE | Vehicle finance and retail banking for mass market | 🟢 BULL_OVERSOLD | 0 | ↓51 | ↓0.966 | ↓20d | — | -11.7% | -77.27/-77.49 | -1.61% | 20% |
| [THERMAX](https://in.tradingview.com/chart/?symbol=NSE:THERMAX)<br><sub>↓CMF24d · 🎯SLING</sub> | ✓ SAFE | Industrial boilers, cooling systems, power equipment, pollution control | 🟢 BULL_OVERSOLD | 0 | ↑37 | ↓0.979 | ↓53d | — | -28.7% | -65.46/-66.18 | -0.93% | 20% |
| [HEXT](https://in.tradingview.com/chart/?symbol=NSE:HEXT)<br><sub>↓CMF3d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | IT services, digital transformation, automation, enterprise clients | 🟡 BULL_OS_L2 | 9 | ↑23 | ↓0.985 | ↓11d | — | -6.2% | -58.51/-59.48 | -0.74% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LTTS,NSE:SASKEN,NSE:AADHARHFC,NSE:VINATIORGA,NSE:TEAMLEASE,NSE:PREMIERENE,NSE:ICRA,NSE:CONCOR,NSE:EQUITASBNK,NSE:TRAVELFOOD,NSE:HONDAPOWER,NSE:INDUSINDBK,NSE:THERMAX,NSE:HEXT
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (10)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | IT services, digital transformation, financial and travel sectors | 📈 BULL_ANY_MID | 24 | ↑76 | ↑1.021 | ↑1d | — | +4.4% | -27.0/-30.77 | +4.40% | 20% |
| [IDBI](https://in.tradingview.com/chart/?symbol=NSE:IDBI)<br><sub>📶W9 · ↓CMF17d</sub> | ⚠ CAUTION | Retail corporate MSME lending deposit bank | 📈 BULL_ANY_MID | 19 | ↑53 | ↑1.031 | ↑1d | — | +5.3% | -9.69/-15.62 | +5.32% | 20% 🟦 |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH)<br><sub>📶W9 · W↑122d · ↑CMF17d</sub> | ✓ SAFE | Precision aerospace components, tooling, defense manufacturing | 📈 BULL_ANY_MID | 17 | ↑96 | ↑1.055 | ↑3d | — | +9.7% | 56.37/53.08 | +2.84% | 10% 🟩 |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 14 | ↑60 | ↑0.998 | ↓11d | — | -3.2% | -35.97/-36.7 | +0.74% | 20% |
| [MOLDTKPAC](https://in.tradingview.com/chart/?symbol=NSE:MOLDTKPAC)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Injection-molded rigid plastic containers for lubricants paints food | 📈 BULL_ANY_MID | 13 | ↑51 | ↓0.998 | ↓7d | — | +3.0% | -38.73/-39.61 | -0.26% | 20% |
| [PERSISTENT](https://in.tradingview.com/chart/?symbol=NSE:PERSISTENT)<br><sub>📶W9 · ↓CMF12d</sub> | ✓ SAFE | Digital engineering services, cloud modernization, enterprise software | 📈 BULL_ANY_MID | 10 | ↑55 | ↑1.006 | ↓23d | — | -4.1% | -45.43/-47.83 | +1.67% | 20% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · W↑49d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Stainless steel washers tubes pipes solar mounting components | 📈 BULL_ANY_MID | 9 | ↑98 | ↑1.054 | ↑11d | — | +20.5% | 58.33/57.56 | +4.44% | 20% |
| [MONTECARLO](https://in.tradingview.com/chart/?symbol=NSE:MONTECARLO)<br><sub>📶W9 · ↓CMF17d</sub> | ✓ SAFE | Woolen cotton apparel manufacturer winter wear retail | 📈 BULL_ANY_MID | 9 | ↑34 | ↓0.991 | ↓11d | — | -4.9% | -41.84/-42.43 | -0.87% | 20% |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH)<br><sub>📶W9 · W↑39d · ★ · ↑CMF12d</sub> | ✓ SAFE | Aerospace defense semiconductor precision components manufacturing | 📈 BULL_ANY_MID | 0 | ↑96 | ↓1.062 | ↑27d | — | +44.9% | 69.76/68.64 | +1.27% | 20% |
| [MASTEK](https://in.tradingview.com/chart/?symbol=NSE:MASTEK)<br><sub>↓CMF4d</sub> | ✓ SAFE | Digital engineering, Oracle Cloud, enterprise transformation | 📈 BULL_ANY_MID | 0 | ↑28 | ↓0.990 | ↓23d | — | -11.0% | -48.2/-49.79 | -0.46% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:COFORGE,NSE:IDBI,NSE:UNIMECH,NSE:GRASIM,NSE:MOLDTKPAC,NSE:PERSISTENT,NSE:RATNAVEER,NSE:MONTECARLO,NSE:ROSSTECH,NSE:MASTEK
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
