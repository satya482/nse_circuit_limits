> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-08-05
*Generated 2026-08-05 15:45 IST*

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

**Total bull crosses today: 91** · 46 inside active squeeze

```
NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,NSE:CLEANMAX,NSE:USHAMART,NSE:GREENLAM,NSE:RGL,NSE:UDS,NSE:APLLTD,NSE:DATAMATICS,NSE:FIEMIND,NSE:SAREGAMA,NSE:HEG,NSE:DIVISLAB,NSE:LODHA,NSE:JGCHEM,NSE:CNL,NSE:CARTRADE,NSE:LMW,NSE:POONAWALLA,NSE:FMGOETZE,NSE:NOVARTIND,NSE:SANGHVIMOV,NSE:SHRIRAMFIN,NSE:DLF,NSE:JSWSTEEL,NSE:APOLLOHOSP,NSE:AZAD,NSE:DEEPAKFERT,NSE:ANTELOPUS,NSE:INDSWFTLAB,NSE:SHREECEM,NSE:KMEW,NSE:BRITANNIA,NSE:CGCL,NSE:5PAISA,NSE:OFSS,NSE:DYCL,NSE:SUVEN,NSE:RUBICON,NSE:BECTORFOOD,NSE:ORCHPHARMA,NSE:TINNARUBR,NSE:INDIAGLYCO,NSE:ULTRACEMCO,NSE:GALAPREC,NSE:TARSONS,NSE:TANLA,NSE:YATRA,NSE:GOCOLORS,NSE:TEAMLEASE,NSE:NIBE,NSE:TATASTEEL,NSE:VHL,NSE:LGHL,NSE:SHARDACROP,NSE:AXISBANK,NSE:AWFIS,NSE:HINDALCO,NSE:AMBUJACEM,NSE:POWERINDIA,NSE:NMDC,NSE:ZAGGLE,NSE:WAKEFIT,NSE:MRF,NSE:HEIDELBERG,NSE:MUTHOOTFIN,NSE:ARVINDFASN,NSE:CHALET,NSE:PRIVISCL,NSE:SRM,NSE:COHANCE,NSE:WHEELS,NSE:SIS,NSE:NPST,NSE:POWERICA,NSE:WELSPUNLIV,NSE:MAYURUNIQ,NSE:SPARC,NSE:GMBREW,NSE:GRAVITA,NSE:PIRAMALFIN,NSE:RAMCOSYS,NSE:SPMLINFRA,NSE:GKENERGY,NSE:CIEINDIA,NSE:PNBGILTS,NSE:BIRLACORPN,NSE:TMPV,NSE:INDIASHLTR,NSE:VSTIND,NSE:GANESHHOU,NSE:EMMVEE,NSE:BAJAJCON
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (45)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CLEANMAX](https://in.tradingview.com/chart/?symbol=NSE:CLEANMAX)<br><sub>📶W9 · ↑CMF7d · ÷DIV</sub> | ⚠ CAUTION | Solar energy solutions for commercial industrial customers | ⚡ BULL_ANY_PPV | 94 | 🔄50 | ↑1.024 | ↑1d | SQ·PV | +4.0% | 12.06/10.55 | +3.98% | 20% |
| [USHAMART](https://in.tradingview.com/chart/?symbol=NSE:USHAMART)<br><sub>📶W9 · W↑28d · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Wire ropes and steel strands for oil, mining, elevators | ⚡ BULL_ANY_PPV | 92 | 🔄73 | ↑1.029 | ↑3d | SQ·PV | +4.9% | 26.85/18.85 | +3.31% | 20% |
| [GREENLAM](https://in.tradingview.com/chart/?symbol=NSE:GREENLAM)<br><sub>📶W9 · W↑3d · 🚀SS·8x · ↑CMF0d</sub> | ✓ SAFE | Laminate sheets and decorative veneers for furniture makers | ⚡ BULL_ANY_PPV | 89 | 🔄64 | ↑1.050 | ↑1d | SQ·PV | +7.7% | 3.79/-5.63 | +7.67% | 20% |
| [RGL](https://in.tradingview.com/chart/?symbol=NSE:RGL)<br><sub>📶W9 · W↑38d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Global recruitment and staffing services provider | ⚡ BULL_ANY_PPV | 89 | 🔄54 | ↑1.048 | ↑1d | SQ·PV | +6.7% | 3.97/0.57 | +6.69% | 20% |
| [UDS](https://in.tradingview.com/chart/?symbol=NSE:UDS)<br><sub>📶W9 · W↑86d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Facilities management and business support services provider | ⚡ BULL_ANY_PPV | 86 | 🔄60 | ↑1.030 | ↑4d | SQ·PV | +6.7% | 58.04/54.96 | +2.75% | 20% |
| [APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD)<br><sub>📶W9 · W↑38d · ↓CMF2d</sub> | ⚠ CAUTION | Generic drugs and APIs for global markets | ⚡ BULL_ANY_PPV | 69 | ↓36 | ↑1.008 | ↑1d | SQ·PV | +1.1% | -2.26/-7.63 | +1.09% | 20% |
| [DATAMATICS](https://in.tradingview.com/chart/?symbol=NSE:DATAMATICS)<br><sub>📶W9 · W↑81d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Digital operations automation for enterprise productivity | ⚡ BULL_ANY_PPV | 48 | 🔄54 | ↑1.041 | ↑2d | PV | +6.3% | 6.27/-4.18 | +4.38% | 20% |
| [FIEMIND](https://in.tradingview.com/chart/?symbol=NSE:FIEMIND)<br><sub>📶W9 · W↑13d · 🚀SS·8x · ↑CMF10d</sub> | ✓ SAFE | Auto lighting and mirrors for two and four wheeler | ⚡ BULL_ANY_PPV | 34 | 🔄72 | ↑1.059 | ↑16d | PV | +12.6% | 41.58/31.95 | +7.46% | 20% |
| [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA)<br><sub>📶W9 · W↑81d · ↑CMF22d</sub> | ✓ SAFE | Music label, films, TV shows, Indian entertainment content IP owner | ⚡ BULL_ANY_PPV | 11 | ↑90 | ↑1.061 | ↑9d | PV | +14.0% | 62.25/56.4 | +2.71% | 20% |
| [HEG](https://in.tradingview.com/chart/?symbol=NSE:HEG)<br><sub>📶W9 · W↑18d · ↑CMF8d</sub> | ✓ SAFE | Graphite electrodes for electric arc furnace steel production | ⚡ BULL_ANY_PPV | 1 | ↑73 | ↑1.047 | ↑19d | PV | +33.4% | 60.39/59.54 | +1.07% | 20% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>📶W9 · W↑74d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 0 | ↑76 | ↑1.059 | ↑20d | PV | +19.4% | 64.61/59.48 | +5.25% | 20% |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Residential and commercial real estate development, Mumbai Pune Bangalore | ⚡ BULL_ANY_PPV | 0 | ↑83 | ↑1.101 | ↑33d | PV | +51.0% | 56.79/51.26 | +9.37% | 20% |
| [JGCHEM](https://in.tradingview.com/chart/?symbol=NSE:JGCHEM)<br><sub>📶W9 · W↑86d · ↑CMF8d</sub> | ✓ SAFE | Zinc oxide manufacturing, chemicals, industrial applications sector | ⚡ BULL_ANY_PPV | 0 | ↑86 | ↑1.084 | ↑22d | PV | +30.6% | 64.85/61.84 | +8.40% | 20% |
| [CNL](https://in.tradingview.com/chart/?symbol=NSE:CNL)<br><sub>📶W9 · W↑81d · 🚀SS · ★ · ↑CMF17d</sub> | ✓ SAFE | IT and lifestyle products distributor for retailers | ⚡ BULL_ANY_PPV | 0 | ↑96 | ↑1.113 | ↑43d | PV | +79.4% | 70.06/66.82 | +7.18% | 20% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>📶W9 · W↑68d · ↓CMF5d</sub> | ✓ SAFE | Online auto marketplace connecting buyers sellers and financiers | 📈 BULL_ANY_MID | 99 | 🔄80 | ↑1.012 | ↑1d | SQ | +1.3% | 15.54/15.27 | +1.31% | 20% |
| [LMW](https://in.tradingview.com/chart/?symbol=NSE:LMW)<br><sub>📶W9 · W↑81d · ↓CMF8d</sub> | ⚠ CAUTION | Textile spinning machinery, CNC tools, heavy castings manufacturer | 📈 BULL_ANY_MID | 99 | 🔄58 | ↑1.013 | ↑1d | SQ | +1.9% | 19.38/16.0 | +1.92% | 20% |
| [POONAWALLA](https://in.tradingview.com/chart/?symbol=NSE:POONAWALLA)<br><sub>📶W9 · W↑38d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | NBFC consumer loans MSME financing general insurance | 📈 BULL_ANY_MID | 94 | 🔄62 | ↑1.019 | ↑1d | SQ | +2.4% | 31.86/26.76 | +2.36% | 20% |
| [FMGOETZE](https://in.tradingview.com/chart/?symbol=NSE:FMGOETZE)<br><sub>📶W9 · W↑38d · ↓CMF12d</sub> | ✓ SAFE | Pistons, rings, valves for domestic and export auto OEMs | 📈 BULL_ANY_MID | 94 | 🔄47 | ↑1.019 | ↑1d | SQ | +3.5% | 19.29/18.56 | +3.49% | 20% |
| [NOVARTIND](https://in.tradingview.com/chart/?symbol=NSE:NOVARTIND)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Pharma import distribution subsidiary treating chronic diseases | 📈 BULL_ANY_MID | 92 | 🔄50 | ↑1.015 | ↑3d | SQ | +6.4% | 28.25/27.48 | +0.80% | 20% |
| [SANGHVIMOV](https://in.tradingview.com/chart/?symbol=NSE:SANGHVIMOV)<br><sub>📶W9 · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Heavy crane rentals for industrial construction projects | 📈 BULL_ANY_MID | 88 | 🔄91 | ↑1.073 | ↑2d | SQ | +8.4% | 15.25/2.1 | +8.13% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑32d · ↓CMF18d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 67 | ↓81 | ↑1.007 | ↑3d | SQ | +3.9% | 10.9/8.21 | +0.29% | 20% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>📶W9 · W↑79d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 63 | ↑45 | ↑1.018 | ↑2d | SQ | +3.0% | 15.62/11.03 | +1.09% | 20% |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 62 | ↑61 | ↑1.020 | ↑3d | SQ | +2.9% | 12.63/4.94 | +2.41% | 20% |
| [APOLLOHOSP](https://in.tradingview.com/chart/?symbol=NSE:APOLLOHOSP)<br><sub>📶W9 · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↓74 | ↓1.004 | ↑2d | SQ | +0.7% | 38.14/36.38 | +0.01% | 20% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>📶W9 · W↑23d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Precision aerospace turbine components for defense energy OEMs | 📈 BULL_ANY_MID | 58 | ↑88 | ↑1.035 | ↑2d | SQ | +6.1% | 21.41/16.76 | +3.05% | 20% |
| [DEEPAKFERT](https://in.tradingview.com/chart/?symbol=NSE:DEEPAKFERT)<br><sub>📶W9 · W↑3d · ↓CMF5d</sub> | ✓ SAFE | Fertilizers, bulk chemicals, mining chemicals, crop nutrition | 📈 BULL_ANY_MID | 58 | ↓77 | ↓1.004 | ↑2d | SQ | +1.2% | 17.88/15.83 | -0.29% | 20% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>📶W9 · ↓CMF7d</sub> | ✓ SAFE | Oil and gas exploration production Indian subcontinent operations | 📈 BULL_ANY_MID | 58 | ↑88 | ↑1.035 | ↑2d | SQ | +4.7% | 19.44/16.08 | +2.43% | 5% 🟥 |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB)<br><sub>📶W9 · ↑CMF12d</sub> | ✓ SAFE | Macrolide antibiotics bulk drug manufacturer for global pharma markets | 📈 BULL_ANY_MID | 58 | ↓98 | ↓1.007 | ↓2d | SQ | +0.8% | 19.22/17.22 | +0.09% | 20% |
| [SHREECEM](https://in.tradingview.com/chart/?symbol=NSE:SHREECEM)<br><sub>📶W9 · W↑38d · ↑CMF7d</sub> | ⚠ CAUTION | Cement manufacturing low-cost producer Northern Eastern Southern regions | 📈 BULL_ANY_MID | 57 | ↓42 | ↓1.006 | ↑3d | SQ | +3.2% | 25.21/18.1 | +0.00% | 20% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>📶W9 · W↑33d · ↑CMF5d</sub> | ✓ SAFE | Dredging, marine engineering, ship repair, ports infrastructure | 📈 BULL_ANY_MID | 56 | ↑96 | ↑1.017 | ↑9d | SQ | +8.6% | 52.45/52.44 | +0.39% | 20% |
| [BRITANNIA](https://in.tradingview.com/chart/?symbol=NSE:BRITANNIA)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF22d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 54 | ↑34 | ↑1.019 | ↑11d | SQ | +4.7% | 45.79/38.66 | +0.99% | 20% |
| [CGCL](https://in.tradingview.com/chart/?symbol=NSE:CGCL)<br><sub>📶W9 · 🚀SS · ↓CMF10d</sub> | ✓ SAFE | NBFC lending MSMEs affordable housing construction finance | 📈 BULL_ANY_MID | 54 | 🔄80 | ↑1.018 | ↑1d | — | +4.2% | -13.58/-14.02 | +4.21% | 20% |
| [5PAISA](https://in.tradingview.com/chart/?symbol=NSE:5PAISA)<br><sub>📶W9 · 🚀SS · ↓CMF23d</sub> | ✓ SAFE | Digital discount brokerage platform for equity derivatives commodity trading | 📈 BULL_ANY_MID | 54 | 🔄62 | ↑1.023 | ↑1d | — | +4.6% | -22.08/-25.28 | +4.62% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄84 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [DYCL](https://in.tradingview.com/chart/?symbol=NSE:DYCL)<br><sub>📶W9 · W↑38d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Power cables for energy infrastructure and industrial applications | 📈 BULL_ANY_MID | 52 | 🔄56 | ↑1.015 | ↑3d | — | +2.6% | 27.28/25.78 | +1.83% | 20% 🟦 |
| [SUVEN](https://in.tradingview.com/chart/?symbol=NSE:SUVEN)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | CNS drug development biotech neurodegenerative disorders focus | 📈 BULL_ANY_MID | 49 | 🔄94 | ↑1.039 | ↑1d | — | +5.4% | -6.21/-9.89 | +5.39% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · 🚀SS · ↑CMF24d</sub> | ✓ SAFE | Complex generic formulations manufacturing specialty pharmaceuticals | 📈 BULL_ANY_MID | 49 | 🔄50 | ↑1.044 | ↑1d | — | +6.0% | 46.1/45.02 | +5.97% | 20% |
| [BECTORFOOD](https://in.tradingview.com/chart/?symbol=NSE:BECTORFOOD)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Premium biscuits and packaged bakery products for Indian households | 📈 BULL_ANY_MID | 40 | 🔄26 | ↑1.022 | ↑15d | — | +25.9% | 33.52/33.17 | +1.35% | 20% |
| [ORCHPHARMA](https://in.tradingview.com/chart/?symbol=NSE:ORCHPHARMA)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Cephalosporin antibiotics API manufacturer serving Indian healthcare | 📈 BULL_ANY_MID | 40 | ↓86 | ↓0.993 | ↓21d | SQ | +7.1% | -2.2/-3.59 | -1.59% | 20% |
| [TINNARUBR](https://in.tradingview.com/chart/?symbol=NSE:TINNARUBR)<br><sub>📶W9 · W↑86d · ↓CMF11d</sub> | ✓ SAFE | Waste tyre recycling into rubber crumb and steel products | 📈 BULL_ANY_MID | 21 | ↑88 | ↑1.026 | ↑4d | — | +8.2% | 53.35/52.69 | +0.61% | 20% |
| [INDIAGLYCO](https://in.tradingview.com/chart/?symbol=NSE:INDIAGLYCO)<br><sub>📶W9 · W↑28d · ↓CMF3d</sub> | ✓ SAFE | Ethylene glycol, specialty chemicals, pharma and industrial sectors | 📈 BULL_ANY_MID | 16 | ↓72 | ↓1.006 | ↑4d | — | +2.4% | 37.53/36.69 | -0.76% | 20% |
| [ULTRACEMCO](https://in.tradingview.com/chart/?symbol=NSE:ULTRACEMCO)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 15 | ↑42 | ↑1.010 | ↑15d | — | +5.6% | 51.42/48.64 | +0.28% | 20% |
| [GALAPREC](https://in.tradingview.com/chart/?symbol=NSE:GALAPREC)<br><sub>📶W9 · 🚀SS · ↓CMF12d</sub> | ✓ SAFE | Precision fasteners and springs for renewable energy | 📈 BULL_ANY_MID | 14 | ↓87 | ↑1.009 | ↓16d | — | -1.3% | -20.9/-23.61 | +1.98% | 20% |
| [TARSONS](https://in.tradingview.com/chart/?symbol=NSE:TARSONS)<br><sub>📶W9 · W↑38d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Plastic labware manufacturer for research and diagnostic labs | 📈 BULL_ANY_MID | 8 | ↑84 | ↑1.035 | ↑12d | — | +16.6% | 52.86/50.32 | +1.19% | 20% |
| [TANLA](https://in.tradingview.com/chart/?symbol=NSE:TANLA)<br><sub>📶W9 · W↑86d · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | CPaaS provider SMS voice OTP enterprise messaging | 📈 BULL_ANY_MID | 1 | ↑60 | ↓1.024 | ↑19d | — | +17.7% | 59.34/58.07 | +0.24% | 20% |

```
NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,NSE:CLEANMAX,NSE:USHAMART,NSE:GREENLAM,NSE:RGL,NSE:UDS,NSE:APLLTD,NSE:DATAMATICS,NSE:FIEMIND,NSE:SAREGAMA,NSE:HEG,NSE:DIVISLAB,NSE:LODHA,NSE:JGCHEM,NSE:CNL,NSE:CARTRADE,NSE:LMW,NSE:POONAWALLA,NSE:FMGOETZE,NSE:NOVARTIND,NSE:SANGHVIMOV,NSE:SHRIRAMFIN,NSE:DLF,NSE:JSWSTEEL,NSE:APOLLOHOSP,NSE:AZAD,NSE:DEEPAKFERT,NSE:ANTELOPUS,NSE:INDSWFTLAB,NSE:SHREECEM,NSE:KMEW,NSE:BRITANNIA,NSE:CGCL,NSE:5PAISA,NSE:OFSS,NSE:DYCL,NSE:SUVEN,NSE:RUBICON,NSE:BECTORFOOD,NSE:ORCHPHARMA,NSE:TINNARUBR,NSE:INDIAGLYCO,NSE:ULTRACEMCO,NSE:GALAPREC,NSE:TARSONS,NSE:TANLA
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (49)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CLEANMAX](https://in.tradingview.com/chart/?symbol=NSE:CLEANMAX)<br><sub>📶W9 · ↑CMF7d · ÷DIV</sub> | ⚠ CAUTION | Solar energy solutions for commercial industrial customers | ⚡ BULL_ANY_PPV | 94 | 🔄50 | ↑1.024 | ↑1d | SQ·PV | +4.0% | 12.06/10.55 | +3.98% | 20% |
| [USHAMART](https://in.tradingview.com/chart/?symbol=NSE:USHAMART)<br><sub>📶W9 · W↑28d · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Wire ropes and steel strands for oil, mining, elevators | ⚡ BULL_ANY_PPV | 92 | 🔄73 | ↑1.029 | ↑3d | SQ·PV | +4.9% | 26.85/18.85 | +3.31% | 20% |
| [GREENLAM](https://in.tradingview.com/chart/?symbol=NSE:GREENLAM)<br><sub>📶W9 · W↑3d · 🚀SS·8x · ↑CMF0d</sub> | ✓ SAFE | Laminate sheets and decorative veneers for furniture makers | ⚡ BULL_ANY_PPV | 89 | 🔄64 | ↑1.050 | ↑1d | SQ·PV | +7.7% | 3.79/-5.63 | +7.67% | 20% |
| [RGL](https://in.tradingview.com/chart/?symbol=NSE:RGL)<br><sub>📶W9 · W↑38d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Global recruitment and staffing services provider | ⚡ BULL_ANY_PPV | 89 | 🔄54 | ↑1.048 | ↑1d | SQ·PV | +6.7% | 3.97/0.57 | +6.69% | 20% |
| [UDS](https://in.tradingview.com/chart/?symbol=NSE:UDS)<br><sub>📶W9 · W↑86d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Facilities management and business support services provider | ⚡ BULL_ANY_PPV | 86 | 🔄60 | ↑1.030 | ↑4d | SQ·PV | +6.7% | 58.04/54.96 | +2.75% | 20% |
| [DATAMATICS](https://in.tradingview.com/chart/?symbol=NSE:DATAMATICS)<br><sub>📶W9 · W↑81d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Digital operations automation for enterprise productivity | ⚡ BULL_ANY_PPV | 48 | 🔄54 | ↑1.041 | ↑2d | PV | +6.3% | 6.27/-4.18 | +4.38% | 20% |
| [FIEMIND](https://in.tradingview.com/chart/?symbol=NSE:FIEMIND)<br><sub>📶W9 · W↑13d · 🚀SS·8x · ↑CMF10d</sub> | ✓ SAFE | Auto lighting and mirrors for two and four wheeler | ⚡ BULL_ANY_PPV | 34 | 🔄72 | ↑1.059 | ↑16d | PV | +12.6% | 41.58/31.95 | +7.46% | 20% |
| [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA)<br><sub>📶W9 · W↑81d · ↑CMF22d</sub> | ✓ SAFE | Music label, films, TV shows, Indian entertainment content IP owner | ⚡ BULL_ANY_PPV | 11 | ↑90 | ↑1.061 | ↑9d | PV | +14.0% | 62.25/56.4 | +2.71% | 20% |
| [HEG](https://in.tradingview.com/chart/?symbol=NSE:HEG)<br><sub>📶W9 · W↑18d · ↑CMF8d</sub> | ✓ SAFE | Graphite electrodes for electric arc furnace steel production | ⚡ BULL_ANY_PPV | 1 | ↑73 | ↑1.047 | ↑19d | PV | +33.4% | 60.39/59.54 | +1.07% | 20% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>📶W9 · W↑74d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 0 | ↑76 | ↑1.059 | ↑20d | PV | +19.4% | 64.61/59.48 | +5.25% | 20% |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Residential and commercial real estate development, Mumbai Pune Bangalore | ⚡ BULL_ANY_PPV | 0 | ↑83 | ↑1.101 | ↑33d | PV | +51.0% | 56.79/51.26 | +9.37% | 20% |
| [JGCHEM](https://in.tradingview.com/chart/?symbol=NSE:JGCHEM)<br><sub>📶W9 · W↑86d · ↑CMF8d</sub> | ✓ SAFE | Zinc oxide manufacturing, chemicals, industrial applications sector | ⚡ BULL_ANY_PPV | 0 | ↑86 | ↑1.084 | ↑22d | PV | +30.6% | 64.85/61.84 | +8.40% | 20% |
| [CNL](https://in.tradingview.com/chart/?symbol=NSE:CNL)<br><sub>📶W9 · W↑81d · 🚀SS · ★ · ↑CMF17d</sub> | ✓ SAFE | IT and lifestyle products distributor for retailers | ⚡ BULL_ANY_PPV | 0 | ↑96 | ↑1.113 | ↑43d | PV | +79.4% | 70.06/66.82 | +7.18% | 20% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>📶W9 · W↑68d · ↓CMF5d</sub> | ✓ SAFE | Online auto marketplace connecting buyers sellers and financiers | 📈 BULL_ANY_MID | 99 | 🔄80 | ↑1.012 | ↑1d | SQ | +1.3% | 15.54/15.27 | +1.31% | 20% |
| [LMW](https://in.tradingview.com/chart/?symbol=NSE:LMW)<br><sub>📶W9 · W↑81d · ↓CMF8d</sub> | ⚠ CAUTION | Textile spinning machinery, CNC tools, heavy castings manufacturer | 📈 BULL_ANY_MID | 99 | 🔄58 | ↑1.013 | ↑1d | SQ | +1.9% | 19.38/16.0 | +1.92% | 20% |
| [POONAWALLA](https://in.tradingview.com/chart/?symbol=NSE:POONAWALLA)<br><sub>📶W9 · W↑38d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | NBFC consumer loans MSME financing general insurance | 📈 BULL_ANY_MID | 94 | 🔄62 | ↑1.019 | ↑1d | SQ | +2.4% | 31.86/26.76 | +2.36% | 20% |
| [FMGOETZE](https://in.tradingview.com/chart/?symbol=NSE:FMGOETZE)<br><sub>📶W9 · W↑38d · ↓CMF12d</sub> | ✓ SAFE | Pistons, rings, valves for domestic and export auto OEMs | 📈 BULL_ANY_MID | 94 | 🔄47 | ↑1.019 | ↑1d | SQ | +3.5% | 19.29/18.56 | +3.49% | 20% |
| [NOVARTIND](https://in.tradingview.com/chart/?symbol=NSE:NOVARTIND)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Pharma import distribution subsidiary treating chronic diseases | 📈 BULL_ANY_MID | 92 | 🔄50 | ↑1.015 | ↑3d | SQ | +6.4% | 28.25/27.48 | +0.80% | 20% |
| [SANGHVIMOV](https://in.tradingview.com/chart/?symbol=NSE:SANGHVIMOV)<br><sub>📶W9 · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Heavy crane rentals for industrial construction projects | 📈 BULL_ANY_MID | 88 | 🔄91 | ↑1.073 | ↑2d | SQ | +8.4% | 15.25/2.1 | +8.13% | 20% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>📶W9 · W↑79d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 63 | ↑45 | ↑1.018 | ↑2d | SQ | +3.0% | 15.62/11.03 | +1.09% | 20% |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 62 | ↑61 | ↑1.020 | ↑3d | SQ | +2.9% | 12.63/4.94 | +2.41% | 20% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>📶W9 · W↑23d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Precision aerospace turbine components for defense energy OEMs | 📈 BULL_ANY_MID | 58 | ↑88 | ↑1.035 | ↑2d | SQ | +6.1% | 21.41/16.76 | +3.05% | 20% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>📶W9 · ↓CMF7d</sub> | ✓ SAFE | Oil and gas exploration production Indian subcontinent operations | 📈 BULL_ANY_MID | 58 | ↑88 | ↑1.035 | ↑2d | SQ | +4.7% | 19.44/16.08 | +2.43% | 5% 🟥 |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>📶W9 · W↑33d · ↑CMF5d</sub> | ✓ SAFE | Dredging, marine engineering, ship repair, ports infrastructure | 📈 BULL_ANY_MID | 56 | ↑96 | ↑1.017 | ↑9d | SQ | +8.6% | 52.45/52.44 | +0.39% | 20% |
| [BRITANNIA](https://in.tradingview.com/chart/?symbol=NSE:BRITANNIA)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF22d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 54 | ↑34 | ↑1.019 | ↑11d | SQ | +4.7% | 45.79/38.66 | +0.99% | 20% |
| [CGCL](https://in.tradingview.com/chart/?symbol=NSE:CGCL)<br><sub>📶W9 · 🚀SS · ↓CMF10d</sub> | ✓ SAFE | NBFC lending MSMEs affordable housing construction finance | 📈 BULL_ANY_MID | 54 | 🔄80 | ↑1.018 | ↑1d | — | +4.2% | -13.58/-14.02 | +4.21% | 20% |
| [5PAISA](https://in.tradingview.com/chart/?symbol=NSE:5PAISA)<br><sub>📶W9 · 🚀SS · ↓CMF23d</sub> | ✓ SAFE | Digital discount brokerage platform for equity derivatives commodity trading | 📈 BULL_ANY_MID | 54 | 🔄62 | ↑1.023 | ↑1d | — | +4.6% | -22.08/-25.28 | +4.62% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄84 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [DYCL](https://in.tradingview.com/chart/?symbol=NSE:DYCL)<br><sub>📶W9 · W↑38d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Power cables for energy infrastructure and industrial applications | 📈 BULL_ANY_MID | 52 | 🔄56 | ↑1.015 | ↑3d | — | +2.6% | 27.28/25.78 | +1.83% | 20% 🟦 |
| [SUVEN](https://in.tradingview.com/chart/?symbol=NSE:SUVEN)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | CNS drug development biotech neurodegenerative disorders focus | 📈 BULL_ANY_MID | 49 | 🔄94 | ↑1.039 | ↑1d | — | +5.4% | -6.21/-9.89 | +5.39% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · 🚀SS · ↑CMF24d</sub> | ✓ SAFE | Complex generic formulations manufacturing specialty pharmaceuticals | 📈 BULL_ANY_MID | 49 | 🔄50 | ↑1.044 | ↑1d | — | +6.0% | 46.1/45.02 | +5.97% | 20% |
| [BECTORFOOD](https://in.tradingview.com/chart/?symbol=NSE:BECTORFOOD)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Premium biscuits and packaged bakery products for Indian households | 📈 BULL_ANY_MID | 40 | 🔄26 | ↑1.022 | ↑15d | — | +25.9% | 33.52/33.17 | +1.35% | 20% |
| [TINNARUBR](https://in.tradingview.com/chart/?symbol=NSE:TINNARUBR)<br><sub>📶W9 · W↑86d · ↓CMF11d</sub> | ✓ SAFE | Waste tyre recycling into rubber crumb and steel products | 📈 BULL_ANY_MID | 21 | ↑88 | ↑1.026 | ↑4d | — | +8.2% | 53.35/52.69 | +0.61% | 20% |
| [ULTRACEMCO](https://in.tradingview.com/chart/?symbol=NSE:ULTRACEMCO)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 15 | ↑42 | ↑1.010 | ↑15d | — | +5.6% | 51.42/48.64 | +0.28% | 20% |
| [TARSONS](https://in.tradingview.com/chart/?symbol=NSE:TARSONS)<br><sub>📶W9 · W↑38d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Plastic labware manufacturer for research and diagnostic labs | 📈 BULL_ANY_MID | 8 | ↑84 | ↑1.035 | ↑12d | — | +16.6% | 52.86/50.32 | +1.19% | 20% |
| [TANLA](https://in.tradingview.com/chart/?symbol=NSE:TANLA)<br><sub>📶W9 · W↑86d · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | CPaaS provider SMS voice OTP enterprise messaging | 📈 BULL_ANY_MID | 1 | ↑60 | ↓1.024 | ↑19d | — | +17.7% | 59.34/58.07 | +0.24% | 20% |
| [YATRA](https://in.tradingview.com/chart/?symbol=NSE:YATRA)<br><sub>W↑43d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Online travel agency for flights hotels bookings | ⚡ BULL_ANY_PPV | 94 | 🔄34 | ↑1.022 | ↑1d | SQ·PV | +3.3% | -16.83/-24.16 | +3.34% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>🚀SS · ↓CMF26d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 99 | 🔄42 | ↑1.010 | ↑1d | SQ | +2.6% | -48.58/-54.51 | +2.56% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄61 | ↑1.012 | ↑1d | SQ | +3.0% | -40.63/-43.65 | +2.95% | 20% |
| [AMBUJACEM](https://in.tradingview.com/chart/?symbol=NSE:AMBUJACEM)<br><sub>W↑27d · ↑CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄14 | ↑1.008 | ↑1d | SQ | +2.0% | 0.82/0.46 | +2.00% | 20% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>🚀SS · ↑CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄90 | ↑1.009 | ↑1d | SQ | +2.7% | -36.34/-42.32 | +2.74% | 20% |
| [NMDC](https://in.tradingview.com/chart/?symbol=NSE:NMDC)<br><sub>🚀SS · ↑CMF0d</sub> | ✓ SAFE | Iron ore mining, diamonds, sponge iron, wind power | 📈 BULL_ANY_MID | 98 | 🔄62 | ↑1.014 | ↑2d | SQ | +2.4% | -2.93/-8.66 | +1.90% | 20% |
| [ZAGGLE](https://in.tradingview.com/chart/?symbol=NSE:ZAGGLE)<br><sub>W↑33d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Corporate spend management platform for SMEs startups | 📈 BULL_ANY_MID | 94 | 🔄2 | ↑1.017 | ↑1d | SQ | +2.6% | -9.02/-16.27 | +2.65% | 20% |
| [WAKEFIT](https://in.tradingview.com/chart/?symbol=NSE:WAKEFIT)<br><sub>🚀SS · ↓CMF9d</sub> | ✓ SAFE | Sleep mattresses, furniture, home goods direct-to-consumer | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.016 | ↑1d | SQ | +2.3% | 7.89/4.9 | +2.31% | 20% |
| [ARVINDFASN](https://in.tradingview.com/chart/?symbol=NSE:ARVINDFASN)<br><sub>🚀SS · ↑CMF2d</sub> | ✓ SAFE | Casual wear denim retail apparel multiple brands | 📈 BULL_ANY_MID | 59 | 🔄28 | ↑1.012 | ↑1d | — | +3.5% | -39.08/-40.83 | +3.46% | 20% |
| [CHALET](https://in.tradingview.com/chart/?symbol=NSE:CHALET)<br><sub>W↑38d · ↑CMF30d</sub> | ⚠ CAUTION | Luxury hotel owner operator major metro locations India | 📈 BULL_ANY_MID | 59 | 🔄39 | ↑1.013 | ↑1d | — | +1.7% | -1.84/-5.99 | +1.70% | 20% |
| [SRM](https://in.tradingview.com/chart/?symbol=NSE:SRM)<br><sub>W↑8d · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Road and bridge construction for J&K infrastructure projects | 📈 BULL_ANY_MID | 58 | ↑46 | ↓1.013 | ↑2d | SQ | +2.9% | 14.41/7.24 | +0.14% | 20% |
| [POWERICA](https://in.tradingview.com/chart/?symbol=NSE:POWERICA)<br><sub>🚀SS · ↓CMF11d</sub> | ✓ SAFE | Diesel generators and wind energy equipment manufacturer | 📈 BULL_ANY_MID | 51 | 🔄50 | ↑1.014 | ↓9d | — | -0.9% | -47.17/-47.91 | +4.82% | 5% 🟥 |
| [SPARC](https://in.tradingview.com/chart/?symbol=NSE:SPARC)<br><sub>🚀SS · ↓CMF18d</sub> | ✓ SAFE | Early-stage drug development for global pharmaceutical markets | 📈 BULL_ANY_MID | 35 | 🔄89 | ↑1.017 | ↓28d | — | -2.9% | -29.93/-31.43 | +5.35% | 10% 🟨 |

```
NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,NSE:CLEANMAX,NSE:USHAMART,NSE:GREENLAM,NSE:RGL,NSE:UDS,NSE:DATAMATICS,NSE:FIEMIND,NSE:SAREGAMA,NSE:HEG,NSE:DIVISLAB,NSE:LODHA,NSE:JGCHEM,NSE:CNL,NSE:CARTRADE,NSE:LMW,NSE:POONAWALLA,NSE:FMGOETZE,NSE:NOVARTIND,NSE:SANGHVIMOV,NSE:DLF,NSE:JSWSTEEL,NSE:AZAD,NSE:ANTELOPUS,NSE:KMEW,NSE:BRITANNIA,NSE:CGCL,NSE:5PAISA,NSE:OFSS,NSE:DYCL,NSE:SUVEN,NSE:RUBICON,NSE:BECTORFOOD,NSE:TINNARUBR,NSE:ULTRACEMCO,NSE:TARSONS,NSE:TANLA,NSE:YATRA,NSE:TATASTEEL,NSE:HINDALCO,NSE:AMBUJACEM,NSE:POWERINDIA,NSE:NMDC,NSE:ZAGGLE,NSE:WAKEFIT,NSE:ARVINDFASN,NSE:CHALET,NSE:SRM,NSE:POWERICA,NSE:SPARC
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (46)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CLEANMAX](https://in.tradingview.com/chart/?symbol=NSE:CLEANMAX)<br><sub>📶W9 · ↑CMF7d · ÷DIV</sub> | ⚠ CAUTION | Solar energy solutions for commercial industrial customers | ⚡ BULL_ANY_PPV | 94 | 🔄50 | ↑1.024 | ↑1d | SQ·PV | +4.0% | 12.06/10.55 | +3.98% | 20% |
| [USHAMART](https://in.tradingview.com/chart/?symbol=NSE:USHAMART)<br><sub>📶W9 · W↑28d · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Wire ropes and steel strands for oil, mining, elevators | ⚡ BULL_ANY_PPV | 92 | 🔄73 | ↑1.029 | ↑3d | SQ·PV | +4.9% | 26.85/18.85 | +3.31% | 20% |
| [GREENLAM](https://in.tradingview.com/chart/?symbol=NSE:GREENLAM)<br><sub>📶W9 · W↑3d · 🚀SS·8x · ↑CMF0d</sub> | ✓ SAFE | Laminate sheets and decorative veneers for furniture makers | ⚡ BULL_ANY_PPV | 89 | 🔄64 | ↑1.050 | ↑1d | SQ·PV | +7.7% | 3.79/-5.63 | +7.67% | 20% |
| [RGL](https://in.tradingview.com/chart/?symbol=NSE:RGL)<br><sub>📶W9 · W↑38d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Global recruitment and staffing services provider | ⚡ BULL_ANY_PPV | 89 | 🔄54 | ↑1.048 | ↑1d | SQ·PV | +6.7% | 3.97/0.57 | +6.69% | 20% |
| [UDS](https://in.tradingview.com/chart/?symbol=NSE:UDS)<br><sub>📶W9 · W↑86d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Facilities management and business support services provider | ⚡ BULL_ANY_PPV | 86 | 🔄60 | ↑1.030 | ↑4d | SQ·PV | +6.7% | 58.04/54.96 | +2.75% | 20% |
| [APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD)<br><sub>📶W9 · W↑38d · ↓CMF2d</sub> | ⚠ CAUTION | Generic drugs and APIs for global markets | ⚡ BULL_ANY_PPV | 69 | ↓36 | ↑1.008 | ↑1d | SQ·PV | +1.1% | -2.26/-7.63 | +1.09% | 20% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>📶W9 · W↑68d · ↓CMF5d</sub> | ✓ SAFE | Online auto marketplace connecting buyers sellers and financiers | 📈 BULL_ANY_MID | 99 | 🔄80 | ↑1.012 | ↑1d | SQ | +1.3% | 15.54/15.27 | +1.31% | 20% |
| [LMW](https://in.tradingview.com/chart/?symbol=NSE:LMW)<br><sub>📶W9 · W↑81d · ↓CMF8d</sub> | ⚠ CAUTION | Textile spinning machinery, CNC tools, heavy castings manufacturer | 📈 BULL_ANY_MID | 99 | 🔄58 | ↑1.013 | ↑1d | SQ | +1.9% | 19.38/16.0 | +1.92% | 20% |
| [POONAWALLA](https://in.tradingview.com/chart/?symbol=NSE:POONAWALLA)<br><sub>📶W9 · W↑38d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | NBFC consumer loans MSME financing general insurance | 📈 BULL_ANY_MID | 94 | 🔄62 | ↑1.019 | ↑1d | SQ | +2.4% | 31.86/26.76 | +2.36% | 20% |
| [FMGOETZE](https://in.tradingview.com/chart/?symbol=NSE:FMGOETZE)<br><sub>📶W9 · W↑38d · ↓CMF12d</sub> | ✓ SAFE | Pistons, rings, valves for domestic and export auto OEMs | 📈 BULL_ANY_MID | 94 | 🔄47 | ↑1.019 | ↑1d | SQ | +3.5% | 19.29/18.56 | +3.49% | 20% |
| [NOVARTIND](https://in.tradingview.com/chart/?symbol=NSE:NOVARTIND)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Pharma import distribution subsidiary treating chronic diseases | 📈 BULL_ANY_MID | 92 | 🔄50 | ↑1.015 | ↑3d | SQ | +6.4% | 28.25/27.48 | +0.80% | 20% |
| [SANGHVIMOV](https://in.tradingview.com/chart/?symbol=NSE:SANGHVIMOV)<br><sub>📶W9 · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Heavy crane rentals for industrial construction projects | 📈 BULL_ANY_MID | 88 | 🔄91 | ↑1.073 | ↑2d | SQ | +8.4% | 15.25/2.1 | +8.13% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑32d · ↓CMF18d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 67 | ↓81 | ↑1.007 | ↑3d | SQ | +3.9% | 10.9/8.21 | +0.29% | 20% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>📶W9 · W↑79d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 63 | ↑45 | ↑1.018 | ↑2d | SQ | +3.0% | 15.62/11.03 | +1.09% | 20% |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 62 | ↑61 | ↑1.020 | ↑3d | SQ | +2.9% | 12.63/4.94 | +2.41% | 20% |
| [APOLLOHOSP](https://in.tradingview.com/chart/?symbol=NSE:APOLLOHOSP)<br><sub>📶W9 · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↓74 | ↓1.004 | ↑2d | SQ | +0.7% | 38.14/36.38 | +0.01% | 20% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>📶W9 · W↑23d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Precision aerospace turbine components for defense energy OEMs | 📈 BULL_ANY_MID | 58 | ↑88 | ↑1.035 | ↑2d | SQ | +6.1% | 21.41/16.76 | +3.05% | 20% |
| [DEEPAKFERT](https://in.tradingview.com/chart/?symbol=NSE:DEEPAKFERT)<br><sub>📶W9 · W↑3d · ↓CMF5d</sub> | ✓ SAFE | Fertilizers, bulk chemicals, mining chemicals, crop nutrition | 📈 BULL_ANY_MID | 58 | ↓77 | ↓1.004 | ↑2d | SQ | +1.2% | 17.88/15.83 | -0.29% | 20% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>📶W9 · ↓CMF7d</sub> | ✓ SAFE | Oil and gas exploration production Indian subcontinent operations | 📈 BULL_ANY_MID | 58 | ↑88 | ↑1.035 | ↑2d | SQ | +4.7% | 19.44/16.08 | +2.43% | 5% 🟥 |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB)<br><sub>📶W9 · ↑CMF12d</sub> | ✓ SAFE | Macrolide antibiotics bulk drug manufacturer for global pharma markets | 📈 BULL_ANY_MID | 58 | ↓98 | ↓1.007 | ↓2d | SQ | +0.8% | 19.22/17.22 | +0.09% | 20% |
| [SHREECEM](https://in.tradingview.com/chart/?symbol=NSE:SHREECEM)<br><sub>📶W9 · W↑38d · ↑CMF7d</sub> | ⚠ CAUTION | Cement manufacturing low-cost producer Northern Eastern Southern regions | 📈 BULL_ANY_MID | 57 | ↓42 | ↓1.006 | ↑3d | SQ | +3.2% | 25.21/18.1 | +0.00% | 20% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>📶W9 · W↑33d · ↑CMF5d</sub> | ✓ SAFE | Dredging, marine engineering, ship repair, ports infrastructure | 📈 BULL_ANY_MID | 56 | ↑96 | ↑1.017 | ↑9d | SQ | +8.6% | 52.45/52.44 | +0.39% | 20% |
| [BRITANNIA](https://in.tradingview.com/chart/?symbol=NSE:BRITANNIA)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF22d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 54 | ↑34 | ↑1.019 | ↑11d | SQ | +4.7% | 45.79/38.66 | +0.99% | 20% |
| [ORCHPHARMA](https://in.tradingview.com/chart/?symbol=NSE:ORCHPHARMA)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Cephalosporin antibiotics API manufacturer serving Indian healthcare | 📈 BULL_ANY_MID | 40 | ↓86 | ↓0.993 | ↓21d | SQ | +7.1% | -2.2/-3.59 | -1.59% | 20% |
| [YATRA](https://in.tradingview.com/chart/?symbol=NSE:YATRA)<br><sub>W↑43d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Online travel agency for flights hotels bookings | ⚡ BULL_ANY_PPV | 94 | 🔄34 | ↑1.022 | ↑1d | SQ·PV | +3.3% | -16.83/-24.16 | +3.34% | 20% |
| [GOCOLORS](https://in.tradingview.com/chart/?symbol=NSE:GOCOLORS)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Women's branded bottoms retailer, design to retail operations | ⚡ BULL_ANY_PPV | 60 | ↓7 | ↑0.990 | ↓5d | SQ·PV | +0.4% | -34.84/-37.47 | +1.34% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>🚀SS · ↓CMF26d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 99 | 🔄42 | ↑1.010 | ↑1d | SQ | +2.6% | -48.58/-54.51 | +2.56% | 20% |
| [VHL](https://in.tradingview.com/chart/?symbol=NSE:VHL)<br><sub>↓CMF14d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 52 | ↓25 | ↑0.999 | ↓13d | SQ | -2.2% | -57.22/-58.41 | +2.09% | 20% |
| [LGHL](https://in.tradingview.com/chart/?symbol=NSE:LGHL)<br><sub>↓CMF30d · ⚠️TRAP · DEL37%</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 45 | ↓4 | ↑0.990 | ↓44d | SQ | -13.3% | -58.45/-59.23 | +0.08% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄61 | ↑1.012 | ↑1d | SQ | +3.0% | -40.63/-43.65 | +2.95% | 20% |
| [AMBUJACEM](https://in.tradingview.com/chart/?symbol=NSE:AMBUJACEM)<br><sub>W↑27d · ↑CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄14 | ↑1.008 | ↑1d | SQ | +2.0% | 0.82/0.46 | +2.00% | 20% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>🚀SS · ↑CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄90 | ↑1.009 | ↑1d | SQ | +2.7% | -36.34/-42.32 | +2.74% | 20% |
| [NMDC](https://in.tradingview.com/chart/?symbol=NSE:NMDC)<br><sub>🚀SS · ↑CMF0d</sub> | ✓ SAFE | Iron ore mining, diamonds, sponge iron, wind power | 📈 BULL_ANY_MID | 98 | 🔄62 | ↑1.014 | ↑2d | SQ | +2.4% | -2.93/-8.66 | +1.90% | 20% |
| [ZAGGLE](https://in.tradingview.com/chart/?symbol=NSE:ZAGGLE)<br><sub>W↑33d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Corporate spend management platform for SMEs startups | 📈 BULL_ANY_MID | 94 | 🔄2 | ↑1.017 | ↑1d | SQ | +2.6% | -9.02/-16.27 | +2.65% | 20% |
| [WAKEFIT](https://in.tradingview.com/chart/?symbol=NSE:WAKEFIT)<br><sub>🚀SS · ↓CMF9d</sub> | ✓ SAFE | Sleep mattresses, furniture, home goods direct-to-consumer | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.016 | ↑1d | SQ | +2.3% | 7.89/4.9 | +2.31% | 20% |
| [MRF](https://in.tradingview.com/chart/?symbol=NSE:MRF)<br><sub>W↑38d · 🚀SS · ↓CMF1d</sub> | ⚠ CAUTION | Tire manufacturer for cars two-wheelers trucks tractors | 📈 BULL_ANY_MID | 69 | ↓36 | ↑1.008 | ↑1d | SQ | +1.2% | 28.27/25.73 | +1.25% | 20% |
| [HEIDELBERG](https://in.tradingview.com/chart/?symbol=NSE:HEIDELBERG)<br><sub>↓CMF2d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↓22 | ↑1.003 | ↑1d | SQ | +0.2% | -13.57/-17.5 | +0.23% | 20% |
| [MUTHOOTFIN](https://in.tradingview.com/chart/?symbol=NSE:MUTHOOTFIN)<br><sub>↓CMF2d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 64 | ↓27 | ↑0.999 | ↑1d | SQ | +0.2% | -22.85/-24.08 | +0.17% | 20% |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL)<br><sub>↓CMF4d</sub> | ✓ SAFE | Fragrance flavor ingredients terpene chemistry global exports | 📈 BULL_ANY_MID | 58 | ↓75 | ↓1.004 | ↑2d | SQ | +1.4% | 8.71/2.96 | -0.34% | 20% |
| [SRM](https://in.tradingview.com/chart/?symbol=NSE:SRM)<br><sub>W↑8d · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Road and bridge construction for J&K infrastructure projects | 📈 BULL_ANY_MID | 58 | ↑46 | ↓1.013 | ↑2d | SQ | +2.9% | 14.41/7.24 | +0.14% | 20% |
| [COHANCE](https://in.tradingview.com/chart/?symbol=NSE:COHANCE)<br><sub>↓CMF11d</sub> | ✓ SAFE | Pharmaceutical contract manufacturing development across drug lifecycle | 📈 BULL_ANY_MID | 57 | ↓6 | ↑1.002 | ↓13d | SQ | -2.8% | -34.93/-36.2 | +1.07% | 20% |
| [WHEELS](https://in.tradingview.com/chart/?symbol=NSE:WHEELS)<br><sub>🚀SS · ↓CMF9d</sub> | ✓ SAFE | Steel aluminum wheels automotive commercial vehicles tractors | 📈 BULL_ANY_MID | 57 | ↓90 | ↑0.999 | ↓8d | SQ | -0.8% | -37.23/-38.29 | +1.48% | 20% |
| [SIS](https://in.tradingview.com/chart/?symbol=NSE:SIS)<br><sub>↓CMF30d</sub> | ✓ SAFE | Manned security, facility management, cash logistics services | 📈 BULL_ANY_MID | 57 | ↓74 | ↑1.001 | ↓13d | SQ | -0.7% | -19.92/-20.1 | +0.12% | 20% |
| [NPST](https://in.tradingview.com/chart/?symbol=NSE:NPST)<br><sub>↓CMF25d</sub> | ✓ SAFE | UPI payments software and real-time transaction processing platform | 📈 BULL_ANY_MID | 55 | ↓59 | ↑1.002 | ↓15d | SQ | -3.8% | -33.9/-35.62 | +1.21% | 10% 🟨 |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>↓CMF5d</sub> | ✓ SAFE | Home textiles, flooring, technical fabrics for global markets | 📈 BULL_ANY_MID | 48 | ↓73 | ↓1.002 | ↓12d | SQ | -1.6% | -36.55/-38.98 | +0.03% | 20% |
| [MAYURUNIQ](https://in.tradingview.com/chart/?symbol=NSE:MAYURUNIQ)<br><sub>↓CMF7d · ⚠️TRAP</sub> | ✓ SAFE | Synthetic leather manufacturer for automotive footwear upholstery | 📈 BULL_ANY_MID | 42 | ↓85 | ↓0.984 | ↓18d | SQ | -7.8% | -36.1/-36.84 | -0.71% | 20% |

```
NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,NSE:CLEANMAX,NSE:USHAMART,NSE:GREENLAM,NSE:RGL,NSE:UDS,NSE:APLLTD,NSE:CARTRADE,NSE:LMW,NSE:POONAWALLA,NSE:FMGOETZE,NSE:NOVARTIND,NSE:SANGHVIMOV,NSE:SHRIRAMFIN,NSE:DLF,NSE:JSWSTEEL,NSE:APOLLOHOSP,NSE:AZAD,NSE:DEEPAKFERT,NSE:ANTELOPUS,NSE:INDSWFTLAB,NSE:SHREECEM,NSE:KMEW,NSE:BRITANNIA,NSE:ORCHPHARMA,NSE:YATRA,NSE:GOCOLORS,NSE:TATASTEEL,NSE:VHL,NSE:LGHL,NSE:HINDALCO,NSE:AMBUJACEM,NSE:POWERINDIA,NSE:NMDC,NSE:ZAGGLE,NSE:WAKEFIT,NSE:MRF,NSE:HEIDELBERG,NSE:MUTHOOTFIN,NSE:PRIVISCL,NSE:SRM,NSE:COHANCE,NSE:WHEELS,NSE:SIS,NSE:NPST,NSE:WELSPUNLIV,NSE:MAYURUNIQ
```

---

### 🔥 MAJOR — PPV confirmed (8)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [DATAMATICS](https://in.tradingview.com/chart/?symbol=NSE:DATAMATICS)<br><sub>📶W9 · W↑81d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Digital operations automation for enterprise productivity | ⚡ BULL_ANY_PPV | 48 | 🔄54 | ↑1.041 | ↑2d | PV | +6.3% | 6.27/-4.18 | +4.38% | 20% |
| [FIEMIND](https://in.tradingview.com/chart/?symbol=NSE:FIEMIND)<br><sub>📶W9 · W↑13d · 🚀SS·8x · ↑CMF10d</sub> | ✓ SAFE | Auto lighting and mirrors for two and four wheeler | ⚡ BULL_ANY_PPV | 34 | 🔄72 | ↑1.059 | ↑16d | PV | +12.6% | 41.58/31.95 | +7.46% | 20% |
| [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA)<br><sub>📶W9 · W↑81d · ↑CMF22d</sub> | ✓ SAFE | Music label, films, TV shows, Indian entertainment content IP owner | ⚡ BULL_ANY_PPV | 11 | ↑90 | ↑1.061 | ↑9d | PV | +14.0% | 62.25/56.4 | +2.71% | 20% |
| [HEG](https://in.tradingview.com/chart/?symbol=NSE:HEG)<br><sub>📶W9 · W↑18d · ↑CMF8d</sub> | ✓ SAFE | Graphite electrodes for electric arc furnace steel production | ⚡ BULL_ANY_PPV | 1 | ↑73 | ↑1.047 | ↑19d | PV | +33.4% | 60.39/59.54 | +1.07% | 20% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>📶W9 · W↑74d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 0 | ↑76 | ↑1.059 | ↑20d | PV | +19.4% | 64.61/59.48 | +5.25% | 20% |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Residential and commercial real estate development, Mumbai Pune Bangalore | ⚡ BULL_ANY_PPV | 0 | ↑83 | ↑1.101 | ↑33d | PV | +51.0% | 56.79/51.26 | +9.37% | 20% |
| [JGCHEM](https://in.tradingview.com/chart/?symbol=NSE:JGCHEM)<br><sub>📶W9 · W↑86d · ↑CMF8d</sub> | ✓ SAFE | Zinc oxide manufacturing, chemicals, industrial applications sector | ⚡ BULL_ANY_PPV | 0 | ↑86 | ↑1.084 | ↑22d | PV | +30.6% | 64.85/61.84 | +8.40% | 20% |
| [CNL](https://in.tradingview.com/chart/?symbol=NSE:CNL)<br><sub>📶W9 · W↑81d · 🚀SS · ★ · ↑CMF17d</sub> | ✓ SAFE | IT and lifestyle products distributor for retailers | ⚡ BULL_ANY_PPV | 0 | ↑96 | ↑1.113 | ↑43d | PV | +79.4% | 70.06/66.82 | +7.18% | 20% |

```
NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,NSE:DATAMATICS,NSE:FIEMIND,NSE:SAREGAMA,NSE:HEG,NSE:DIVISLAB,NSE:LODHA,NSE:JGCHEM,NSE:CNL
```

### 🟢 OVERSOLD — reversal from −53/−60 (5)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [TEAMLEASE](https://in.tradingview.com/chart/?symbol=NSE:TEAMLEASE)<br><sub>↓CMF20d · ⚠️TRAP</sub> | ✓ SAFE | Staffing recruitment payroll HR services employer solutions | 🟢 BULL_OVERSOLD | 6 | ↓11 | ↓0.978 | ↓14d | — | -11.1% | -59.39/-60.01 | -0.75% | 20% |
| [NIBE](https://in.tradingview.com/chart/?symbol=NSE:NIBE)<br><sub>🚀SS · ↓CMF14d · 🎯SLING</sub> | ✓ SAFE | Defense aerospace components manufacturer renewable energy sector | 🟢 BULL_OVERSOLD | 5 | ↓76 | ↑0.983 | ↓39d | — | -2.6% | -61.54/-64.26 | +1.02% | 10% 🟨 |
| [SHARDACROP](https://in.tradingview.com/chart/?symbol=NSE:SHARDACROP)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Generic agrochemical formulations and technical ingredients export | 🟡 BULL_OS_L2 | 12 | ↓5 | ↓0.975 | ↓8d | — | -5.7% | -55.73/-56.11 | -2.11% | 20% |
| [AXISBANK](https://in.tradingview.com/chart/?symbol=NSE:AXISBANK)<br><sub>↓CMF17d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 5 | ↓44 | ↑0.988 | ↓36d | — | -2.5% | -58.03/-58.94 | +1.01% | 20% |
| [AWFIS](https://in.tradingview.com/chart/?symbol=NSE:AWFIS)<br><sub>🚀SS · ↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Flexible workspace provider for enterprises and freelancers | 🟡 BULL_OS_L2 | 5 | ↓1 | ↑0.986 | ↓20d | — | -7.7% | -52.79/-54.32 | +0.79% | 20% |

```
NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,NSE:TEAMLEASE,NSE:NIBE,NSE:SHARDACROP,NSE:AXISBANK,NSE:AWFIS
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (32)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CGCL](https://in.tradingview.com/chart/?symbol=NSE:CGCL)<br><sub>📶W9 · 🚀SS · ↓CMF10d</sub> | ✓ SAFE | NBFC lending MSMEs affordable housing construction finance | 📈 BULL_ANY_MID | 54 | 🔄80 | ↑1.018 | ↑1d | — | +4.2% | -13.58/-14.02 | +4.21% | 20% |
| [5PAISA](https://in.tradingview.com/chart/?symbol=NSE:5PAISA)<br><sub>📶W9 · 🚀SS · ↓CMF23d</sub> | ✓ SAFE | Digital discount brokerage platform for equity derivatives commodity trading | 📈 BULL_ANY_MID | 54 | 🔄62 | ↑1.023 | ↑1d | — | +4.6% | -22.08/-25.28 | +4.62% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄84 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [DYCL](https://in.tradingview.com/chart/?symbol=NSE:DYCL)<br><sub>📶W9 · W↑38d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Power cables for energy infrastructure and industrial applications | 📈 BULL_ANY_MID | 52 | 🔄56 | ↑1.015 | ↑3d | — | +2.6% | 27.28/25.78 | +1.83% | 20% 🟦 |
| [SUVEN](https://in.tradingview.com/chart/?symbol=NSE:SUVEN)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | CNS drug development biotech neurodegenerative disorders focus | 📈 BULL_ANY_MID | 49 | 🔄94 | ↑1.039 | ↑1d | — | +5.4% | -6.21/-9.89 | +5.39% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · 🚀SS · ↑CMF24d</sub> | ✓ SAFE | Complex generic formulations manufacturing specialty pharmaceuticals | 📈 BULL_ANY_MID | 49 | 🔄50 | ↑1.044 | ↑1d | — | +6.0% | 46.1/45.02 | +5.97% | 20% |
| [BECTORFOOD](https://in.tradingview.com/chart/?symbol=NSE:BECTORFOOD)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Premium biscuits and packaged bakery products for Indian households | 📈 BULL_ANY_MID | 40 | 🔄26 | ↑1.022 | ↑15d | — | +25.9% | 33.52/33.17 | +1.35% | 20% |
| [TINNARUBR](https://in.tradingview.com/chart/?symbol=NSE:TINNARUBR)<br><sub>📶W9 · W↑86d · ↓CMF11d</sub> | ✓ SAFE | Waste tyre recycling into rubber crumb and steel products | 📈 BULL_ANY_MID | 21 | ↑88 | ↑1.026 | ↑4d | — | +8.2% | 53.35/52.69 | +0.61% | 20% |
| [INDIAGLYCO](https://in.tradingview.com/chart/?symbol=NSE:INDIAGLYCO)<br><sub>📶W9 · W↑28d · ↓CMF3d</sub> | ✓ SAFE | Ethylene glycol, specialty chemicals, pharma and industrial sectors | 📈 BULL_ANY_MID | 16 | ↓72 | ↓1.006 | ↑4d | — | +2.4% | 37.53/36.69 | -0.76% | 20% |
| [ULTRACEMCO](https://in.tradingview.com/chart/?symbol=NSE:ULTRACEMCO)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 15 | ↑42 | ↑1.010 | ↑15d | — | +5.6% | 51.42/48.64 | +0.28% | 20% |
| [GALAPREC](https://in.tradingview.com/chart/?symbol=NSE:GALAPREC)<br><sub>📶W9 · 🚀SS · ↓CMF12d</sub> | ✓ SAFE | Precision fasteners and springs for renewable energy | 📈 BULL_ANY_MID | 14 | ↓87 | ↑1.009 | ↓16d | — | -1.3% | -20.9/-23.61 | +1.98% | 20% |
| [TARSONS](https://in.tradingview.com/chart/?symbol=NSE:TARSONS)<br><sub>📶W9 · W↑38d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Plastic labware manufacturer for research and diagnostic labs | 📈 BULL_ANY_MID | 8 | ↑84 | ↑1.035 | ↑12d | — | +16.6% | 52.86/50.32 | +1.19% | 20% |
| [TANLA](https://in.tradingview.com/chart/?symbol=NSE:TANLA)<br><sub>📶W9 · W↑86d · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | CPaaS provider SMS voice OTP enterprise messaging | 📈 BULL_ANY_MID | 1 | ↑60 | ↓1.024 | ↑19d | — | +17.7% | 59.34/58.07 | +0.24% | 20% |
| [ARVINDFASN](https://in.tradingview.com/chart/?symbol=NSE:ARVINDFASN)<br><sub>🚀SS · ↑CMF2d</sub> | ✓ SAFE | Casual wear denim retail apparel multiple brands | 📈 BULL_ANY_MID | 59 | 🔄28 | ↑1.012 | ↑1d | — | +3.5% | -39.08/-40.83 | +3.46% | 20% |
| [CHALET](https://in.tradingview.com/chart/?symbol=NSE:CHALET)<br><sub>W↑38d · ↑CMF30d</sub> | ⚠ CAUTION | Luxury hotel owner operator major metro locations India | 📈 BULL_ANY_MID | 59 | 🔄39 | ↑1.013 | ↑1d | — | +1.7% | -1.84/-5.99 | +1.70% | 20% |
| [POWERICA](https://in.tradingview.com/chart/?symbol=NSE:POWERICA)<br><sub>🚀SS · ↓CMF11d</sub> | ✓ SAFE | Diesel generators and wind energy equipment manufacturer | 📈 BULL_ANY_MID | 51 | 🔄50 | ↑1.014 | ↓9d | — | -0.9% | -47.17/-47.91 | +4.82% | 5% 🟥 |
| [SPARC](https://in.tradingview.com/chart/?symbol=NSE:SPARC)<br><sub>🚀SS · ↓CMF18d</sub> | ✓ SAFE | Early-stage drug development for global pharmaceutical markets | 📈 BULL_ANY_MID | 35 | 🔄89 | ↑1.017 | ↓28d | — | -2.9% | -29.93/-31.43 | +5.35% | 10% 🟨 |
| [GMBREW](https://in.tradingview.com/chart/?symbol=NSE:GMBREW)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Country liquor and IMFL manufacturer Maharashtra spirits sector | 📈 BULL_ANY_MID | 29 | ↓37 | ↑1.004 | ↑1d | — | +0.8% | -25.84/-28.59 | +0.83% | 20% |
| [GRAVITA](https://in.tradingview.com/chart/?symbol=NSE:GRAVITA)<br><sub>🚀SS · ↓CMF5d</sub> | ✓ SAFE | Lead and aluminum recycling, non-ferrous metals processing | 📈 BULL_ANY_MID | 22 | ↓33 | ↑1.004 | ↓8d | — | -4.9% | -28.88/-30.89 | +1.82% | 20% |
| [PIRAMALFIN](https://in.tradingview.com/chart/?symbol=NSE:PIRAMALFIN)<br><sub>🚀SS · ↓CMF12d</sub> | ⚠ CAUTION | NBFC retail housing loans property mortgages consumer finance | 📈 BULL_ANY_MID | 17 | ↓50 | ↑1.004 | ↓13d | — | -2.9% | -25.05/-28.33 | +2.99% | 20% |
| [RAMCOSYS](https://in.tradingview.com/chart/?symbol=NSE:RAMCOSYS)<br><sub>🚀SS · ↓CMF7d · DEL51%</sub> | ✓ SAFE | ERP software, HCM, aerospace supply chain management | 📈 BULL_ANY_MID | 14 | ↓88 | ↑0.977 | ↓11d | — | -21.9% | -40.85/-40.94 | +5.00% | 10% 🟨 |
| [SPMLINFRA](https://in.tradingview.com/chart/?symbol=NSE:SPMLINFRA)<br><sub>🚀SS · ↑CMF1d</sub> | ✓ SAFE | Water power EPC projects municipal industrial clients | 📈 BULL_ANY_MID | 14 | ↓22 | ↑1.002 | ↓16d | — | +2.6% | -19.6/-20.4 | +1.20% | 20% |
| [GKENERGY](https://in.tradingview.com/chart/?symbol=NSE:GKENERGY)<br><sub>🚀SS · ↓CMF23d</sub> | ✓ SAFE | Solar agricultural pump systems EPC services PM-KUSUM | 📈 BULL_ANY_MID | 12 | ↓50 | ↑0.990 | ↓13d | — | -4.8% | -50.54/-51.49 | +1.27% | 10% 🟩 |
| [CIEINDIA](https://in.tradingview.com/chart/?symbol=NSE:CIEINDIA)<br><sub>🚀SS · ↓CMF13d</sub> | ✓ SAFE | Automotive components supplier transmissions suspensions global OEM | 📈 BULL_ANY_MID | 10 | ↓30 | ↑0.986 | ↓15d | — | -10.0% | -36.76/-37.17 | +1.08% | 20% |
| [PNBGILTS](https://in.tradingview.com/chart/?symbol=NSE:PNBGILTS)<br><sub>🚀SS · ↑CMF1d</sub> | ✓ SAFE | Government securities dealer, primary dealer, debt market | 📈 BULL_ANY_MID | 10 | ↓49 | ↑0.994 | ↓15d | — | -4.4% | -51.17/-52.39 | +1.16% | 20% |
| [BIRLACORPN](https://in.tradingview.com/chart/?symbol=NSE:BIRLACORPN)<br><sub>🚀SS · ↓CMF24d · ⚠️TRAP</sub> | ✓ SAFE | Cement manufacturing, jute products, construction materials | 📈 BULL_ANY_MID | 9 | ↓6 | ↑0.987 | ↓16d | — | -6.6% | -40.16/-41.62 | +0.08% | 20% |
| [TMPV](https://in.tradingview.com/chart/?symbol=NSE:TMPV)<br><sub>🚀SS · ↓CMF29d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓18 | ↑0.999 | ↓33d | — | -12.4% | -49.04/-51.5 | +1.53% | 20% |
| [INDIASHLTR](https://in.tradingview.com/chart/?symbol=NSE:INDIASHLTR)<br><sub>↓CMF13d · ⚠️TRAP</sub> | ⚠ CAUTION | Housing loans to low income tier 2 3 cities | 📈 BULL_ANY_MID | 5 | ↓16 | ↑0.992 | ↓25d | — | -3.6% | -23.3/-23.48 | +0.04% | 20% |
| [VSTIND](https://in.tradingview.com/chart/?symbol=NSE:VSTIND)<br><sub>🚀SS · ↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Cigarette and tobacco products manufacturer for Indian consumers | 📈 BULL_ANY_MID | 5 | ↓17 | ↑0.985 | ↓25d | — | -14.9% | -44.57/-45.62 | +0.09% | 20% |
| [GANESHHOU](https://in.tradingview.com/chart/?symbol=NSE:GANESHHOU)<br><sub>↓CMF21d</sub> | ✓ SAFE | Residential real estate development Ahmedabad Gujarat region | 📈 BULL_ANY_MID | 5 | ↓48 | ↑0.997 | ↓28d | — | +3.1% | -23.22/-25.56 | +0.03% | 20% |
| [EMMVEE](https://in.tradingview.com/chart/?symbol=NSE:EMMVEE)<br><sub>↑CMF1d</sub> | ✓ SAFE | Solar PV modules and cells manufacturing for energy sector | 📈 BULL_ANY_MID | 4 | ↓50 | ↓1.001 | ↓16d | — | -3.0% | -25.35/-28.34 | -0.11% | 20% |
| [BAJAJCON](https://in.tradingview.com/chart/?symbol=NSE:BAJAJCON)<br><sub>↓CMF17d · ⚠️TRAP</sub> | ✓ SAFE | Hair oils and personal care products for Indian households | 📈 BULL_ANY_MID | 0 | ↓93 | ↓0.985 | ↓28d | — | -8.3% | -23.16/-24.06 | -2.54% | 20% |

```
NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,NSE:CGCL,NSE:5PAISA,NSE:OFSS,NSE:DYCL,NSE:SUVEN,NSE:RUBICON,NSE:BECTORFOOD,NSE:TINNARUBR,NSE:INDIAGLYCO,NSE:ULTRACEMCO,NSE:GALAPREC,NSE:TARSONS,NSE:TANLA,NSE:ARVINDFASN,NSE:CHALET,NSE:POWERICA,NSE:SPARC,NSE:GMBREW,NSE:GRAVITA,NSE:PIRAMALFIN,NSE:RAMCOSYS,NSE:SPMLINFRA,NSE:GKENERGY,NSE:CIEINDIA,NSE:PNBGILTS,NSE:BIRLACORPN,NSE:TMPV,NSE:INDIASHLTR,NSE:VSTIND,NSE:GANESHHOU,NSE:EMMVEE,NSE:BAJAJCON
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
