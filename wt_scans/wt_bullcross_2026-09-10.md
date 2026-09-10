> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-09-10
*Generated 2026-09-10 15:45 IST*

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

**Total bull crosses today: 72** · 26 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:PGIL,NSE:MAXHEALTH,NSE:KOLTEPATIL,NSE:AARTIDRUGS,NSE:JSWINFRA,NSE:FORCEMOT,NSE:SUPRAJIT,NSE:VSSL,NSE:INOXINDIA,NSE:KSL,NSE:JUNIPER,NSE:MANINDS,NSE:MAHSEAMLES,NSE:SIGMAADV,NSE:HINDALCO,NSE:ALGOQUANT,NSE:ARVINDFASN,NSE:KRSNAA,NSE:KAJARIACER,NSE:FLUOROCHEM,NSE:RKFORGE,NSE:SONACOMS,NSE:TORNTPHARM,NSE:MEDANTA,NSE:DECNGOLD,NSE:APLLTD,NSE:HINDZINC,NSE:CARRARO,NSE:ADANIENT,NSE:UTLSOLAR,NSE:BOSCHLTD,NSE:FEDERALBNK,NSE:KAPSTON,NSE:SETL,NSE:SUDARSCHEM,NSE:GANDHAR,NSE:MEESHO,NSE:ORIENTTECH,NSE:SWSOLAR,NSE:TCC,NSE:POKARNA,NSE:BHARATRAS,NSE:JSLL,NSE:TAJGVK,NSE:ITDC,NSE:TATAINVEST,NSE:DBL,NSE:CUMMINSIND,NSE:JKLAKSHMI,NSE:ROSSARI,NSE:DABUR,NSE:THERMAX,NSE:DEEPAKFERT,NSE:IREDA,NSE:CHOICEIN,NSE:HITECH,NSE:ADANIGREEN,NSE:SUMMITSEC,NSE:BLUESTARCO,NSE:VAIBHAVGBL,NSE:TECHNOE,NSE:SANDUMA,NSE:TIRUMALCHM,NSE:ICEMAKE,NSE:ZAGGLE,NSE:UJJIVANSFB,NSE:GANESHHOU,NSE:NIITMTS,NSE:DATAMATICS,NSE:TDPOWERSYS,NSE:GODREJCP,NSE:JSWENERGY
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (37)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PGIL](https://in.tradingview.com/chart/?symbol=NSE:PGIL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Apparel manufacturer, exports to global fashion brands | ⚡ BULL_ANY_PPV | 94 | 🔄91 | ↑1.020 | ↑1d | SQ·PV | +4.4% | 0.28/-2.09 | +4.41% | 20% |
| [MAXHEALTH](https://in.tradingview.com/chart/?symbol=NSE:MAXHEALTH)<br><sub>📶W9 · ↑CMF9d</sub> | ⚠ CAUTION | Tertiary quaternary hospital network Delhi NCR North India | ⚡ BULL_ANY_PPV | 89 | 🔄37 | ↑1.030 | ↑1d | SQ·PV | +4.5% | -32.15/-41.06 | +4.48% | 20% |
| [KOLTEPATIL](https://in.tradingview.com/chart/?symbol=NSE:KOLTEPATIL)<br><sub>📶W9 · 🚀SS·8x · ↓CMF22d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 69 | ↑68 | ↑1.010 | ↑1d | SQ·PV | +1.9% | -3.75/-9.32 | +1.89% | 20% |
| [AARTIDRUGS](https://in.tradingview.com/chart/?symbol=NSE:AARTIDRUGS)<br><sub>📶W9 · W↑54d · 🚀SS · ↓CMF21d</sub> | ✓ SAFE | API manufacturer, pharma intermediates, specialty chemicals producer | ⚡ BULL_ANY_PPV | 63 | ↑59 | ↑1.028 | ↑2d | SQ·PV | +3.7% | 41.82/37.28 | +3.20% | 20% |
| [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Port operations, cargo handling, maritime logistics services | ⚡ BULL_ANY_PPV | 58 | ↑70 | ↓1.016 | ↑2d | SQ·PV | +3.1% | 5.16/-3.82 | +0.31% | 20% |
| [FORCEMOT](https://in.tradingview.com/chart/?symbol=NSE:FORCEMOT)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Commercial vehicles and auto components, light CVs | ⚡ BULL_ANY_PPV | 54 | 🔄38 | ↑1.027 | ↑1d | PV | +4.7% | -14.5/-20.96 | +4.72% | 20% |
| [SUPRAJIT](https://in.tradingview.com/chart/?symbol=NSE:SUPRAJIT)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Automotive cables, halogen lamps, mechanical components manufacturer | ⚡ BULL_ANY_PPV | 54 | 🔄58 | ↑1.017 | ↑1d | PV | +3.1% | -43.25/-47.32 | +3.06% | 20% |
| [VSSL](https://in.tradingview.com/chart/?symbol=NSE:VSSL)<br><sub>📶W9 · W↑44d · 🚀SS·50x · ↓CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 40 | ↑86 | ↑1.076 | ↑45d | SQ·PV | +45.3% | 59.6/49.53 | +8.06% | 20% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · W↑9d · 🚀SS · ★ · ↑CMF11d</sub> | ✓ SAFE | Cryogenic equipment manufacturer for LNG, industrial gas, scientific applications | ⚡ BULL_ANY_PPV | 9 | ↑93 | ↑1.053 | ↑11d | PV | +19.2% | 50.28/48.45 | +5.05% | 20% |
| [KSL](https://in.tradingview.com/chart/?symbol=NSE:KSL)<br><sub>📶W9 · W↑14d · ↑CMF0d</sub> | ✓ SAFE | Alloy steel long products for precision engineering applications | ⚡ BULL_ANY_PPV | 5 | ↑76 | ↑1.049 | ↑15d | PV | +13.0% | 42.65/40.92 | +6.35% | 20% |
| [JUNIPER](https://in.tradingview.com/chart/?symbol=NSE:JUNIPER)<br><sub>📶W9 · W↑29d · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 2 | ↑46 | ↑1.050 | ↑18d | PV | +18.4% | 51.51/48.91 | +6.55% | 20% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>📶W9 · W↑24d · RVOL9x · ★ · ↑CMF10d</sub> | ✓ SAFE | Large-diameter welded steel pipes, energy infrastructure, global exports | ⚡ BULL_ANY_PPV | 0 | ↑96 | ↑1.105 | ↑26d | PV | +64.4% | 68.1/67.03 | +10.59% | 20% 🟦 |
| [MAHSEAMLES](https://in.tradingview.com/chart/?symbol=NSE:MAHSEAMLES)<br><sub>📶W9 · W↑24d · ↑CMF0d</sub> | ✓ SAFE | Seamless steel pipes tubes ERW renewable power rig | ⚡ BULL_ANY_PPV | 0 | ↑69 | ↑1.064 | ↑28d | PV | +25.3% | 67.52/66.65 | +6.32% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 91 | 🔄61 | ↑1.003 | ↓9d | SQ | -0.3% | -18.92/-20.04 | +1.17% | 20% |
| [ALGOQUANT](https://in.tradingview.com/chart/?symbol=NSE:ALGOQUANT)<br><sub>📶W9 · ↓CMF18d · DEL34%(T-1)</sub> | ✓ SAFE | Algorithmic trading platform for quantitative capital markets | 📈 BULL_ANY_MID | 82 | 🔄50 | ↑0.998 | ↓13d | SQ | -2.5% | -33.3/-37.7 | +0.66% | 20% |
| [ARVINDFASN](https://in.tradingview.com/chart/?symbol=NSE:ARVINDFASN)<br><sub>📶W9 · ↑CMF2d</sub> | ⚠ CAUTION | Casual wear denim retail apparel multiple brands | 📈 BULL_ANY_MID | 69 | ↑36 | ↑1.012 | ↑1d | SQ | +1.6% | -6.08/-7.23 | +1.65% | 20% |
| [KRSNAA](https://in.tradingview.com/chart/?symbol=NSE:KRSNAA)<br><sub>📶W9 · W↑29d · ↑CMF0d</sub> | ✓ SAFE | Diagnostic imaging centers for patients across India | 📈 BULL_ANY_MID | 68 | ↑22 | ↑1.011 | ↑2d | SQ | +3.3% | 3.11/-0.87 | +0.62% | 20% |
| [KAJARIACER](https://in.tradingview.com/chart/?symbol=NSE:KAJARIACER)<br><sub>📶W9 · W↑9d · ↑CMF13d</sub> | ⚠ CAUTION | Ceramic and vitrified tiles manufacturer for construction | 📈 BULL_ANY_MID | 67 | ↑62 | ↑1.005 | ↑3d | SQ | +1.9% | 23.11/21.7 | +0.38% | 20% |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>📶W9 · ↓CMF18d</sub> | ✓ SAFE | PTFE manufacturer, fluorochemicals, industrial polymers globally | 📈 BULL_ANY_MID | 62 | ↑82 | ↑1.020 | ↑3d | SQ | +5.7% | 25.06/17.35 | +0.66% | 20% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>📶W9 · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Forged auto and railway components manufacturer, precision engineering | 📈 BULL_ANY_MID | 60 | ↑77 | ↑1.008 | ↓10d | SQ | +1.4% | -4.46/-4.6 | +0.88% | 20% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>📶W9 · ↑CMF3d</sub> | ✓ SAFE | Differential assemblies and gears for electric vehicles | 📈 BULL_ANY_MID | 59 | ↑90 | ↑1.004 | ↓11d | SQ | +1.1% | -2.82/-6.41 | +0.50% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑67 | ↓0.997 | ↓2d | SQ | +0.2% | -3.46/-4.79 | -0.71% | 20% |
| [MEDANTA](https://in.tradingview.com/chart/?symbol=NSE:MEDANTA)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Private tertiary hospital network cardiology oncology neurosciences | 📈 BULL_ANY_MID | 58 | ↑69 | ↓1.006 | ↑2d | SQ | +2.2% | 19.92/17.82 | -1.41% | 20% |
| [DECNGOLD](https://in.tradingview.com/chart/?symbol=NSE:DECNGOLD)<br><sub>📶W9 · 🚀SS · ↓CMF5d</sub> | ✓ SAFE | Gold exploration and mining transitioning to active production | 📈 BULL_ANY_MID | 54 | 🔄50 | ↑1.016 | ↑1d | — | +3.1% | -5.03/-8.08 | +3.08% | 20% |
| [APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD)<br><sub>📶W9 · 🚀SS · ↓CMF28d</sub> | ⚠ CAUTION | Generics and APIs manufacturer serving global pharma markets | 📈 BULL_ANY_MID | 51 | ↑47 | ↓1.001 | ↓9d | SQ | +0.4% | -10.34/-12.74 | -0.12% | 20% |
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>📶W9 · W↑28d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 28 | ↑64 | ↑1.014 | ↑2d | — | +2.7% | 24.78/23.85 | +1.56% | 20% |
| [CARRARO](https://in.tradingview.com/chart/?symbol=NSE:CARRARO)<br><sub>📶W9 · W↑14d · ↑CMF4d</sub> | ✓ SAFE | Axles transmissions agricultural tractors construction equipment | 📈 BULL_ANY_MID | 21 | ↑58 | ↑1.020 | ↑4d | — | +3.4% | 18.32/13.62 | +2.43% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · ↓CMF7d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 19 | ↑77 | ↑1.039 | ↑1d | — | +5.1% | -9.05/-16.39 | +5.11% | 20% |
| [UTLSOLAR](https://in.tradingview.com/chart/?symbol=NSE:UTLSOLAR)<br><sub>📶W9 · ↑CMF4d</sub> | ✓ SAFE | Solar rooftop systems, on-grid off-grid hybrid | 📈 BULL_ANY_MID | 18 | ↑50 | ↓1.005 | ↓2d | — | +1.7% | 8.38/5.12 | -2.16% | 5% 🟥 |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>📶W9 · W↑109d · ↑CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.015 | ↑3d | — | +4.4% | 32.49/29.43 | +0.17% | 20% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>📶W9 · ↑CMF2d</sub> | ⚠ CAUTION | Retail corporate banking Kerala-headquartered private sector bank | 📈 BULL_ANY_MID | 16 | ↑79 | ↑0.998 | ↓9d | — | +0.5% | -34.43/-35.07 | +0.29% | 20% |
| [KAPSTON](https://in.tradingview.com/chart/?symbol=NSE:KAPSTON)<br><sub>📶W9 · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | Security guarding and facility management staffing services | 📈 BULL_ANY_MID | 10 | ↑99 | ↑1.030 | ↑10d | — | +16.8% | 35.54/35.26 | +3.66% | 20% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | Glass-lined reactors and process equipment for pharma chemicals | 📈 BULL_ANY_MID | 6 | ↑99 | ↑1.126 | ↑14d | — | +49.8% | 80.64/79.69 | +4.99% | 5% 🟥 |
| [SUDARSCHEM](https://in.tradingview.com/chart/?symbol=NSE:SUDARSCHEM)<br><sub>📶W9 · W↑49d · ↑CMF19d</sub> | ✓ SAFE | Organic inorganic pigments chemicals coating paint industries | 📈 BULL_ANY_MID | 5 | ↑78 | ↑1.024 | ↑20d | — | +20.7% | 48.95/48.25 | +0.67% | 20% |
| [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR)<br><sub>📶W9 · 🚀SS · ↑CMF10d</sub> | ✓ SAFE | White oils, specialty petroleum, consumer healthcare applications | 📈 BULL_ANY_MID | 5 | ↑96 | ↑1.027 | ↑21d | — | +14.8% | 62.56/60.73 | +2.05% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · 🚀SS · ↑CMF29d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 0 | ↑50 | ↑1.036 | ↑24d | — | +16.7% | 57.53/55.6 | +3.13% | 20% 🟦 |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:PGIL,NSE:MAXHEALTH,NSE:KOLTEPATIL,NSE:AARTIDRUGS,NSE:JSWINFRA,NSE:FORCEMOT,NSE:SUPRAJIT,NSE:VSSL,NSE:INOXINDIA,NSE:KSL,NSE:JUNIPER,NSE:MANINDS,NSE:MAHSEAMLES,NSE:SIGMAADV,NSE:HINDALCO,NSE:ALGOQUANT,NSE:ARVINDFASN,NSE:KRSNAA,NSE:KAJARIACER,NSE:FLUOROCHEM,NSE:RKFORGE,NSE:SONACOMS,NSE:TORNTPHARM,NSE:MEDANTA,NSE:DECNGOLD,NSE:APLLTD,NSE:HINDZINC,NSE:CARRARO,NSE:ADANIENT,NSE:UTLSOLAR,NSE:BOSCHLTD,NSE:FEDERALBNK,NSE:KAPSTON,NSE:SETL,NSE:SUDARSCHEM,NSE:GANDHAR,NSE:MEESHO
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (57)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PGIL](https://in.tradingview.com/chart/?symbol=NSE:PGIL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Apparel manufacturer, exports to global fashion brands | ⚡ BULL_ANY_PPV | 94 | 🔄91 | ↑1.020 | ↑1d | SQ·PV | +4.4% | 0.28/-2.09 | +4.41% | 20% |
| [MAXHEALTH](https://in.tradingview.com/chart/?symbol=NSE:MAXHEALTH)<br><sub>📶W9 · ↑CMF9d</sub> | ⚠ CAUTION | Tertiary quaternary hospital network Delhi NCR North India | ⚡ BULL_ANY_PPV | 89 | 🔄37 | ↑1.030 | ↑1d | SQ·PV | +4.5% | -32.15/-41.06 | +4.48% | 20% |
| [KOLTEPATIL](https://in.tradingview.com/chart/?symbol=NSE:KOLTEPATIL)<br><sub>📶W9 · 🚀SS·8x · ↓CMF22d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 69 | ↑68 | ↑1.010 | ↑1d | SQ·PV | +1.9% | -3.75/-9.32 | +1.89% | 20% |
| [AARTIDRUGS](https://in.tradingview.com/chart/?symbol=NSE:AARTIDRUGS)<br><sub>📶W9 · W↑54d · 🚀SS · ↓CMF21d</sub> | ✓ SAFE | API manufacturer, pharma intermediates, specialty chemicals producer | ⚡ BULL_ANY_PPV | 63 | ↑59 | ↑1.028 | ↑2d | SQ·PV | +3.7% | 41.82/37.28 | +3.20% | 20% |
| [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Port operations, cargo handling, maritime logistics services | ⚡ BULL_ANY_PPV | 58 | ↑70 | ↓1.016 | ↑2d | SQ·PV | +3.1% | 5.16/-3.82 | +0.31% | 20% |
| [FORCEMOT](https://in.tradingview.com/chart/?symbol=NSE:FORCEMOT)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Commercial vehicles and auto components, light CVs | ⚡ BULL_ANY_PPV | 54 | 🔄38 | ↑1.027 | ↑1d | PV | +4.7% | -14.5/-20.96 | +4.72% | 20% |
| [SUPRAJIT](https://in.tradingview.com/chart/?symbol=NSE:SUPRAJIT)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Automotive cables, halogen lamps, mechanical components manufacturer | ⚡ BULL_ANY_PPV | 54 | 🔄58 | ↑1.017 | ↑1d | PV | +3.1% | -43.25/-47.32 | +3.06% | 20% |
| [VSSL](https://in.tradingview.com/chart/?symbol=NSE:VSSL)<br><sub>📶W9 · W↑44d · 🚀SS·50x · ↓CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 40 | ↑86 | ↑1.076 | ↑45d | SQ·PV | +45.3% | 59.6/49.53 | +8.06% | 20% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · W↑9d · 🚀SS · ★ · ↑CMF11d</sub> | ✓ SAFE | Cryogenic equipment manufacturer for LNG, industrial gas, scientific applications | ⚡ BULL_ANY_PPV | 9 | ↑93 | ↑1.053 | ↑11d | PV | +19.2% | 50.28/48.45 | +5.05% | 20% |
| [KSL](https://in.tradingview.com/chart/?symbol=NSE:KSL)<br><sub>📶W9 · W↑14d · ↑CMF0d</sub> | ✓ SAFE | Alloy steel long products for precision engineering applications | ⚡ BULL_ANY_PPV | 5 | ↑76 | ↑1.049 | ↑15d | PV | +13.0% | 42.65/40.92 | +6.35% | 20% |
| [JUNIPER](https://in.tradingview.com/chart/?symbol=NSE:JUNIPER)<br><sub>📶W9 · W↑29d · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 2 | ↑46 | ↑1.050 | ↑18d | PV | +18.4% | 51.51/48.91 | +6.55% | 20% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>📶W9 · W↑24d · RVOL9x · ★ · ↑CMF10d</sub> | ✓ SAFE | Large-diameter welded steel pipes, energy infrastructure, global exports | ⚡ BULL_ANY_PPV | 0 | ↑96 | ↑1.105 | ↑26d | PV | +64.4% | 68.1/67.03 | +10.59% | 20% 🟦 |
| [MAHSEAMLES](https://in.tradingview.com/chart/?symbol=NSE:MAHSEAMLES)<br><sub>📶W9 · W↑24d · ↑CMF0d</sub> | ✓ SAFE | Seamless steel pipes tubes ERW renewable power rig | ⚡ BULL_ANY_PPV | 0 | ↑69 | ↑1.064 | ↑28d | PV | +25.3% | 67.52/66.65 | +6.32% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 91 | 🔄61 | ↑1.003 | ↓9d | SQ | -0.3% | -18.92/-20.04 | +1.17% | 20% |
| [ALGOQUANT](https://in.tradingview.com/chart/?symbol=NSE:ALGOQUANT)<br><sub>📶W9 · ↓CMF18d · DEL34%(T-1)</sub> | ✓ SAFE | Algorithmic trading platform for quantitative capital markets | 📈 BULL_ANY_MID | 82 | 🔄50 | ↑0.998 | ↓13d | SQ | -2.5% | -33.3/-37.7 | +0.66% | 20% |
| [ARVINDFASN](https://in.tradingview.com/chart/?symbol=NSE:ARVINDFASN)<br><sub>📶W9 · ↑CMF2d</sub> | ⚠ CAUTION | Casual wear denim retail apparel multiple brands | 📈 BULL_ANY_MID | 69 | ↑36 | ↑1.012 | ↑1d | SQ | +1.6% | -6.08/-7.23 | +1.65% | 20% |
| [KRSNAA](https://in.tradingview.com/chart/?symbol=NSE:KRSNAA)<br><sub>📶W9 · W↑29d · ↑CMF0d</sub> | ✓ SAFE | Diagnostic imaging centers for patients across India | 📈 BULL_ANY_MID | 68 | ↑22 | ↑1.011 | ↑2d | SQ | +3.3% | 3.11/-0.87 | +0.62% | 20% |
| [KAJARIACER](https://in.tradingview.com/chart/?symbol=NSE:KAJARIACER)<br><sub>📶W9 · W↑9d · ↑CMF13d</sub> | ⚠ CAUTION | Ceramic and vitrified tiles manufacturer for construction | 📈 BULL_ANY_MID | 67 | ↑62 | ↑1.005 | ↑3d | SQ | +1.9% | 23.11/21.7 | +0.38% | 20% |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>📶W9 · ↓CMF18d</sub> | ✓ SAFE | PTFE manufacturer, fluorochemicals, industrial polymers globally | 📈 BULL_ANY_MID | 62 | ↑82 | ↑1.020 | ↑3d | SQ | +5.7% | 25.06/17.35 | +0.66% | 20% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>📶W9 · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Forged auto and railway components manufacturer, precision engineering | 📈 BULL_ANY_MID | 60 | ↑77 | ↑1.008 | ↓10d | SQ | +1.4% | -4.46/-4.6 | +0.88% | 20% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>📶W9 · ↑CMF3d</sub> | ✓ SAFE | Differential assemblies and gears for electric vehicles | 📈 BULL_ANY_MID | 59 | ↑90 | ↑1.004 | ↓11d | SQ | +1.1% | -2.82/-6.41 | +0.50% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑67 | ↓0.997 | ↓2d | SQ | +0.2% | -3.46/-4.79 | -0.71% | 20% |
| [MEDANTA](https://in.tradingview.com/chart/?symbol=NSE:MEDANTA)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Private tertiary hospital network cardiology oncology neurosciences | 📈 BULL_ANY_MID | 58 | ↑69 | ↓1.006 | ↑2d | SQ | +2.2% | 19.92/17.82 | -1.41% | 20% |
| [DECNGOLD](https://in.tradingview.com/chart/?symbol=NSE:DECNGOLD)<br><sub>📶W9 · 🚀SS · ↓CMF5d</sub> | ✓ SAFE | Gold exploration and mining transitioning to active production | 📈 BULL_ANY_MID | 54 | 🔄50 | ↑1.016 | ↑1d | — | +3.1% | -5.03/-8.08 | +3.08% | 20% |
| [APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD)<br><sub>📶W9 · 🚀SS · ↓CMF28d</sub> | ⚠ CAUTION | Generics and APIs manufacturer serving global pharma markets | 📈 BULL_ANY_MID | 51 | ↑47 | ↓1.001 | ↓9d | SQ | +0.4% | -10.34/-12.74 | -0.12% | 20% |
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>📶W9 · W↑28d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 28 | ↑64 | ↑1.014 | ↑2d | — | +2.7% | 24.78/23.85 | +1.56% | 20% |
| [CARRARO](https://in.tradingview.com/chart/?symbol=NSE:CARRARO)<br><sub>📶W9 · W↑14d · ↑CMF4d</sub> | ✓ SAFE | Axles transmissions agricultural tractors construction equipment | 📈 BULL_ANY_MID | 21 | ↑58 | ↑1.020 | ↑4d | — | +3.4% | 18.32/13.62 | +2.43% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · ↓CMF7d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 19 | ↑77 | ↑1.039 | ↑1d | — | +5.1% | -9.05/-16.39 | +5.11% | 20% |
| [UTLSOLAR](https://in.tradingview.com/chart/?symbol=NSE:UTLSOLAR)<br><sub>📶W9 · ↑CMF4d</sub> | ✓ SAFE | Solar rooftop systems, on-grid off-grid hybrid | 📈 BULL_ANY_MID | 18 | ↑50 | ↓1.005 | ↓2d | — | +1.7% | 8.38/5.12 | -2.16% | 5% 🟥 |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>📶W9 · W↑109d · ↑CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.015 | ↑3d | — | +4.4% | 32.49/29.43 | +0.17% | 20% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>📶W9 · ↑CMF2d</sub> | ⚠ CAUTION | Retail corporate banking Kerala-headquartered private sector bank | 📈 BULL_ANY_MID | 16 | ↑79 | ↑0.998 | ↓9d | — | +0.5% | -34.43/-35.07 | +0.29% | 20% |
| [KAPSTON](https://in.tradingview.com/chart/?symbol=NSE:KAPSTON)<br><sub>📶W9 · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | Security guarding and facility management staffing services | 📈 BULL_ANY_MID | 10 | ↑99 | ↑1.030 | ↑10d | — | +16.8% | 35.54/35.26 | +3.66% | 20% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | Glass-lined reactors and process equipment for pharma chemicals | 📈 BULL_ANY_MID | 6 | ↑99 | ↑1.126 | ↑14d | — | +49.8% | 80.64/79.69 | +4.99% | 5% 🟥 |
| [SUDARSCHEM](https://in.tradingview.com/chart/?symbol=NSE:SUDARSCHEM)<br><sub>📶W9 · W↑49d · ↑CMF19d</sub> | ✓ SAFE | Organic inorganic pigments chemicals coating paint industries | 📈 BULL_ANY_MID | 5 | ↑78 | ↑1.024 | ↑20d | — | +20.7% | 48.95/48.25 | +0.67% | 20% |
| [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR)<br><sub>📶W9 · 🚀SS · ↑CMF10d</sub> | ✓ SAFE | White oils, specialty petroleum, consumer healthcare applications | 📈 BULL_ANY_MID | 5 | ↑96 | ↑1.027 | ↑21d | — | +14.8% | 62.56/60.73 | +2.05% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · 🚀SS · ↑CMF29d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 0 | ↑50 | ↑1.036 | ↑24d | — | +16.7% | 57.53/55.6 | +3.13% | 20% 🟦 |
| [ORIENTTECH](https://in.tradingview.com/chart/?symbol=NSE:ORIENTTECH)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | IT infrastructure cloud digital transformation solutions | 🔥 BULL_OS_PPV | 35 | 🔄16 | ↑0.993 | ↓34d | PV | -9.1% | -59.31/-60.58 | +2.49% | 20% |
| [JSLL](https://in.tradingview.com/chart/?symbol=NSE:JSLL)<br><sub>↓CMF30d</sub> | ✓ SAFE | Ayurvedic hospital networks, inpatient outpatient wellness services | ⚡ BULL_ANY_PPV | 99 | 🔄9 | ↑1.013 | ↑1d | SQ·PV | +2.4% | -18.38/-22.87 | +2.39% | 20% |
| [TAJGVK](https://in.tradingview.com/chart/?symbol=NSE:TAJGVK)<br><sub>↓CMF9d</sub> | ✓ SAFE | Premium hotel operation and management across India | ⚡ BULL_ANY_PPV | 94 | 🔄34 | ↑1.017 | ↑1d | SQ·PV | +3.1% | -41.02/-47.91 | +3.15% | 20% |
| [ITDC](https://in.tradingview.com/chart/?symbol=NSE:ITDC)<br><sub>RVOL90x · ↓CMF21d · DEL41%(T-1) · 🎯SLING</sub> | ✓ SAFE | Hotel operations, tours, catering for domestic tourism sector | ⚡ BULL_ANY_PPV | 54 | 🔄64 | ↑1.022 | ↑1d | PV | +5.5% | -49.25/-58.97 | +5.55% | 20% 🟦 |
| [TATAINVEST](https://in.tradingview.com/chart/?symbol=NSE:TATAINVEST)<br><sub>🚀SS·52x · ↓CMF30d</sub> | ✓ SAFE | NBFC investing in equities, debt, mutual funds | ⚡ BULL_ANY_PPV | 54 | 🔄35 | ↑1.017 | ↑1d | PV | +4.3% | -40.63/-46.9 | +4.26% | 20% |
| [DBL](https://in.tradingview.com/chart/?symbol=NSE:DBL)<br><sub>🚀SS·73x · ↓CMF13d</sub> | ✓ SAFE | Highway and bridge construction, EPC contractor | ⚡ BULL_ANY_PPV | 54 | 🔄26 | ↑1.017 | ↑1d | PV | +3.8% | -35.95/-46.03 | +3.75% | 20% |
| [CUMMINSIND](https://in.tradingview.com/chart/?symbol=NSE:CUMMINSIND)<br><sub>↑CMF1d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 59 | 🔄53 | ↑1.012 | ↑1d | — | +2.7% | -56.42/-62.44 | +2.68% | 20% |
| [IREDA](https://in.tradingview.com/chart/?symbol=NSE:IREDA)<br><sub>↓CMF6d · 🎯SLING</sub> | ✓ SAFE | Renewable energy financing, solar wind projects, India | 🟡 BULL_OS_L2 | 42 | 🔄20 | ↑0.997 | ↓13d | — | -1.8% | -54.19/-55.17 | +1.19% | 20% |
| [CHOICEIN](https://in.tradingview.com/chart/?symbol=NSE:CHOICEIN)<br><sub>↓CMF21d · DEL64%(T-1) · 🎯SLING</sub> | ✓ SAFE | Stockbroking wealth management MSME lending insurance distribution financial services | 🟡 BULL_OS_L2 | 40 | 🔄55 | ↑1.004 | ↓30d | — | -3.5% | -52.43/-54.03 | +2.63% | 20% |
| [HITECH](https://in.tradingview.com/chart/?symbol=NSE:HITECH)<br><sub>↓CMF29d · 🎯SLING</sub> | ✓ SAFE | ERW steel pipes tubes construction automotive infrastructure | 🟡 BULL_OS_L2 | 20 | ↑18 | ↑1.002 | ↓10d | — | -0.7% | -49.38/-54.72 | +0.79% | 20% |
| [SUMMITSEC](https://in.tradingview.com/chart/?symbol=NSE:SUMMITSEC)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄13 | ↑1.010 | ↑1d | SQ | +1.9% | -22.68/-29.91 | +1.90% | 20% |
| [BLUESTARCO](https://in.tradingview.com/chart/?symbol=NSE:BLUESTARCO)<br><sub>↑CMF0d</sub> | ⚠ CAUTION | AC units, refrigeration, MEP projects for commercial facilities | 📈 BULL_ANY_MID | 94 | 🔄17 | ↑1.020 | ↑1d | SQ | +3.9% | -35.47/-38.04 | +3.92% | 20% |
| [VAIBHAVGBL](https://in.tradingview.com/chart/?symbol=NSE:VAIBHAVGBL)<br><sub>↓CMF30d</sub> | ✓ SAFE | Fashion jewelry gemstones lifestyle direct consumer retail | 📈 BULL_ANY_MID | 75 | 🔄27 | ↑0.992 | ↓34d | SQ | -14.3% | -42.75/-43.12 | +0.80% | 20% |
| [TECHNOE](https://in.tradingview.com/chart/?symbol=NSE:TECHNOE)<br><sub>↓CMF21d · ⚠️TRAP</sub> | ✓ SAFE | Power infrastructure EPC transmission distribution generation projects | 📈 BULL_ANY_MID | 58 | ↑14 | ↓0.999 | ↓2d | SQ | +1.4% | -25.31/-31.14 | -0.76% | 20% |
| [TIRUMALCHM](https://in.tradingview.com/chart/?symbol=NSE:TIRUMALCHM)<br><sub>↓CMF30d</sub> | ✓ SAFE | Phthalic anhydride, maleic anhydride producer for coatings plastics | 📈 BULL_ANY_MID | 48 | ↑5 | ↓0.998 | ↓12d | SQ | +0.1% | -15.69/-20.59 | -0.18% | 20% |
| [ZAGGLE](https://in.tradingview.com/chart/?symbol=NSE:ZAGGLE)<br><sub>↑CMF15d</sub> | ✓ SAFE | B2B expense management software, corporate spend cards | 📈 BULL_ANY_MID | 44 | 🔄3 | ↑1.004 | ↓16d | — | -1.1% | -51.9/-52.22 | +3.88% | 20% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>🚀SS · ↓CMF15d</sub> | ✓ SAFE | Microfinance bank serving low-income retail borrowers India | 📈 BULL_ANY_MID | 40 | 🔄74 | ↑1.010 | ↓60d+ | — | +16.1% | -38.07/-40.67 | +3.74% | 20% |
| [GANESHHOU](https://in.tradingview.com/chart/?symbol=NSE:GANESHHOU)<br><sub>↓CMF0d</sub> | ⚠ CAUTION | Residential real estate development Ahmedabad Gujarat region | 📈 BULL_ANY_MID | 40 | 🔄43 | ↑1.002 | ↓21d | — | +1.0% | -34.42/-35.58 | +1.91% | 20% |
| [NIITMTS](https://in.tradingview.com/chart/?symbol=NSE:NIITMTS)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | IT training services corporate upskilling global | 📈 BULL_ANY_MID | 35 | 🔄8 | ↑0.997 | ↓32d | — | -2.8% | -49.89/-50.86 | +1.40% | 20% |
| [DATAMATICS](https://in.tradingview.com/chart/?symbol=NSE:DATAMATICS)<br><sub>↓CMF30d</sub> | ✓ SAFE | Digital operations and BPO services for enterprise automation | 📈 BULL_ANY_MID | 10 | ↑36 | ↑1.008 | ↓28d | — | -5.4% | -46.32/-50.53 | +0.96% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:PGIL,NSE:MAXHEALTH,NSE:KOLTEPATIL,NSE:AARTIDRUGS,NSE:JSWINFRA,NSE:FORCEMOT,NSE:SUPRAJIT,NSE:VSSL,NSE:INOXINDIA,NSE:KSL,NSE:JUNIPER,NSE:MANINDS,NSE:MAHSEAMLES,NSE:SIGMAADV,NSE:HINDALCO,NSE:ALGOQUANT,NSE:ARVINDFASN,NSE:KRSNAA,NSE:KAJARIACER,NSE:FLUOROCHEM,NSE:RKFORGE,NSE:SONACOMS,NSE:TORNTPHARM,NSE:MEDANTA,NSE:DECNGOLD,NSE:APLLTD,NSE:HINDZINC,NSE:CARRARO,NSE:ADANIENT,NSE:UTLSOLAR,NSE:BOSCHLTD,NSE:FEDERALBNK,NSE:KAPSTON,NSE:SETL,NSE:SUDARSCHEM,NSE:GANDHAR,NSE:MEESHO,NSE:ORIENTTECH,NSE:JSLL,NSE:TAJGVK,NSE:ITDC,NSE:TATAINVEST,NSE:DBL,NSE:CUMMINSIND,NSE:IREDA,NSE:CHOICEIN,NSE:HITECH,NSE:SUMMITSEC,NSE:BLUESTARCO,NSE:VAIBHAVGBL,NSE:TECHNOE,NSE:TIRUMALCHM,NSE:ZAGGLE,NSE:UJJIVANSFB,NSE:GANESHHOU,NSE:NIITMTS,NSE:DATAMATICS
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (26)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PGIL](https://in.tradingview.com/chart/?symbol=NSE:PGIL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Apparel manufacturer, exports to global fashion brands | ⚡ BULL_ANY_PPV | 94 | 🔄91 | ↑1.020 | ↑1d | SQ·PV | +4.4% | 0.28/-2.09 | +4.41% | 20% |
| [MAXHEALTH](https://in.tradingview.com/chart/?symbol=NSE:MAXHEALTH)<br><sub>📶W9 · ↑CMF9d</sub> | ⚠ CAUTION | Tertiary quaternary hospital network Delhi NCR North India | ⚡ BULL_ANY_PPV | 89 | 🔄37 | ↑1.030 | ↑1d | SQ·PV | +4.5% | -32.15/-41.06 | +4.48% | 20% |
| [KOLTEPATIL](https://in.tradingview.com/chart/?symbol=NSE:KOLTEPATIL)<br><sub>📶W9 · 🚀SS·8x · ↓CMF22d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 69 | ↑68 | ↑1.010 | ↑1d | SQ·PV | +1.9% | -3.75/-9.32 | +1.89% | 20% |
| [AARTIDRUGS](https://in.tradingview.com/chart/?symbol=NSE:AARTIDRUGS)<br><sub>📶W9 · W↑54d · 🚀SS · ↓CMF21d</sub> | ✓ SAFE | API manufacturer, pharma intermediates, specialty chemicals producer | ⚡ BULL_ANY_PPV | 63 | ↑59 | ↑1.028 | ↑2d | SQ·PV | +3.7% | 41.82/37.28 | +3.20% | 20% |
| [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Port operations, cargo handling, maritime logistics services | ⚡ BULL_ANY_PPV | 58 | ↑70 | ↓1.016 | ↑2d | SQ·PV | +3.1% | 5.16/-3.82 | +0.31% | 20% |
| [VSSL](https://in.tradingview.com/chart/?symbol=NSE:VSSL)<br><sub>📶W9 · W↑44d · 🚀SS·50x · ↓CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 40 | ↑86 | ↑1.076 | ↑45d | SQ·PV | +45.3% | 59.6/49.53 | +8.06% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 91 | 🔄61 | ↑1.003 | ↓9d | SQ | -0.3% | -18.92/-20.04 | +1.17% | 20% |
| [ALGOQUANT](https://in.tradingview.com/chart/?symbol=NSE:ALGOQUANT)<br><sub>📶W9 · ↓CMF18d · DEL34%(T-1)</sub> | ✓ SAFE | Algorithmic trading platform for quantitative capital markets | 📈 BULL_ANY_MID | 82 | 🔄50 | ↑0.998 | ↓13d | SQ | -2.5% | -33.3/-37.7 | +0.66% | 20% |
| [ARVINDFASN](https://in.tradingview.com/chart/?symbol=NSE:ARVINDFASN)<br><sub>📶W9 · ↑CMF2d</sub> | ⚠ CAUTION | Casual wear denim retail apparel multiple brands | 📈 BULL_ANY_MID | 69 | ↑36 | ↑1.012 | ↑1d | SQ | +1.6% | -6.08/-7.23 | +1.65% | 20% |
| [KRSNAA](https://in.tradingview.com/chart/?symbol=NSE:KRSNAA)<br><sub>📶W9 · W↑29d · ↑CMF0d</sub> | ✓ SAFE | Diagnostic imaging centers for patients across India | 📈 BULL_ANY_MID | 68 | ↑22 | ↑1.011 | ↑2d | SQ | +3.3% | 3.11/-0.87 | +0.62% | 20% |
| [KAJARIACER](https://in.tradingview.com/chart/?symbol=NSE:KAJARIACER)<br><sub>📶W9 · W↑9d · ↑CMF13d</sub> | ⚠ CAUTION | Ceramic and vitrified tiles manufacturer for construction | 📈 BULL_ANY_MID | 67 | ↑62 | ↑1.005 | ↑3d | SQ | +1.9% | 23.11/21.7 | +0.38% | 20% |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>📶W9 · ↓CMF18d</sub> | ✓ SAFE | PTFE manufacturer, fluorochemicals, industrial polymers globally | 📈 BULL_ANY_MID | 62 | ↑82 | ↑1.020 | ↑3d | SQ | +5.7% | 25.06/17.35 | +0.66% | 20% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>📶W9 · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Forged auto and railway components manufacturer, precision engineering | 📈 BULL_ANY_MID | 60 | ↑77 | ↑1.008 | ↓10d | SQ | +1.4% | -4.46/-4.6 | +0.88% | 20% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>📶W9 · ↑CMF3d</sub> | ✓ SAFE | Differential assemblies and gears for electric vehicles | 📈 BULL_ANY_MID | 59 | ↑90 | ↑1.004 | ↓11d | SQ | +1.1% | -2.82/-6.41 | +0.50% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑67 | ↓0.997 | ↓2d | SQ | +0.2% | -3.46/-4.79 | -0.71% | 20% |
| [MEDANTA](https://in.tradingview.com/chart/?symbol=NSE:MEDANTA)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Private tertiary hospital network cardiology oncology neurosciences | 📈 BULL_ANY_MID | 58 | ↑69 | ↓1.006 | ↑2d | SQ | +2.2% | 19.92/17.82 | -1.41% | 20% |
| [APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD)<br><sub>📶W9 · 🚀SS · ↓CMF28d</sub> | ⚠ CAUTION | Generics and APIs manufacturer serving global pharma markets | 📈 BULL_ANY_MID | 51 | ↑47 | ↓1.001 | ↓9d | SQ | +0.4% | -10.34/-12.74 | -0.12% | 20% |
| [JSLL](https://in.tradingview.com/chart/?symbol=NSE:JSLL)<br><sub>↓CMF30d</sub> | ✓ SAFE | Ayurvedic hospital networks, inpatient outpatient wellness services | ⚡ BULL_ANY_PPV | 99 | 🔄9 | ↑1.013 | ↑1d | SQ·PV | +2.4% | -18.38/-22.87 | +2.39% | 20% |
| [TAJGVK](https://in.tradingview.com/chart/?symbol=NSE:TAJGVK)<br><sub>↓CMF9d</sub> | ✓ SAFE | Premium hotel operation and management across India | ⚡ BULL_ANY_PPV | 94 | 🔄34 | ↑1.017 | ↑1d | SQ·PV | +3.1% | -41.02/-47.91 | +3.15% | 20% |
| [SUMMITSEC](https://in.tradingview.com/chart/?symbol=NSE:SUMMITSEC)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄13 | ↑1.010 | ↑1d | SQ | +1.9% | -22.68/-29.91 | +1.90% | 20% |
| [BLUESTARCO](https://in.tradingview.com/chart/?symbol=NSE:BLUESTARCO)<br><sub>↑CMF0d</sub> | ⚠ CAUTION | AC units, refrigeration, MEP projects for commercial facilities | 📈 BULL_ANY_MID | 94 | 🔄17 | ↑1.020 | ↑1d | SQ | +3.9% | -35.47/-38.04 | +3.92% | 20% |
| [VAIBHAVGBL](https://in.tradingview.com/chart/?symbol=NSE:VAIBHAVGBL)<br><sub>↓CMF30d</sub> | ✓ SAFE | Fashion jewelry gemstones lifestyle direct consumer retail | 📈 BULL_ANY_MID | 75 | 🔄27 | ↑0.992 | ↓34d | SQ | -14.3% | -42.75/-43.12 | +0.80% | 20% |
| [TECHNOE](https://in.tradingview.com/chart/?symbol=NSE:TECHNOE)<br><sub>↓CMF21d · ⚠️TRAP</sub> | ✓ SAFE | Power infrastructure EPC transmission distribution generation projects | 📈 BULL_ANY_MID | 58 | ↑14 | ↓0.999 | ↓2d | SQ | +1.4% | -25.31/-31.14 | -0.76% | 20% |
| [SANDUMA](https://in.tradingview.com/chart/?symbol=NSE:SANDUMA)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Manganese iron ore mining integrated ferroalloys producer | 📈 BULL_ANY_MID | 58 | ↓44 | ↓0.989 | ↓2d | SQ | +0.1% | -27.47/-27.69 | -2.12% | 20% |
| [TIRUMALCHM](https://in.tradingview.com/chart/?symbol=NSE:TIRUMALCHM)<br><sub>↓CMF30d</sub> | ✓ SAFE | Phthalic anhydride, maleic anhydride producer for coatings plastics | 📈 BULL_ANY_MID | 48 | ↑5 | ↓0.998 | ↓12d | SQ | +0.1% | -15.69/-20.59 | -0.18% | 20% |
| [ICEMAKE](https://in.tradingview.com/chart/?symbol=NSE:ICEMAKE)<br><sub>↓CMF30d</sub> | ✓ SAFE | Refrigeration equipment manufacturer for commercial cold storage operations | 📈 BULL_ANY_MID | 45 | ↓36 | ↑0.992 | ↓22d | SQ | -10.3% | -33.64/-36.5 | +0.30% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:PGIL,NSE:MAXHEALTH,NSE:KOLTEPATIL,NSE:AARTIDRUGS,NSE:JSWINFRA,NSE:VSSL,NSE:HINDALCO,NSE:ALGOQUANT,NSE:ARVINDFASN,NSE:KRSNAA,NSE:KAJARIACER,NSE:FLUOROCHEM,NSE:RKFORGE,NSE:SONACOMS,NSE:TORNTPHARM,NSE:MEDANTA,NSE:APLLTD,NSE:JSLL,NSE:TAJGVK,NSE:SUMMITSEC,NSE:BLUESTARCO,NSE:VAIBHAVGBL,NSE:TECHNOE,NSE:SANDUMA,NSE:TIRUMALCHM,NSE:ICEMAKE
```

---

### 🔥 MAJOR — PPV confirmed (16)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [FORCEMOT](https://in.tradingview.com/chart/?symbol=NSE:FORCEMOT)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Commercial vehicles and auto components, light CVs | ⚡ BULL_ANY_PPV | 54 | 🔄38 | ↑1.027 | ↑1d | PV | +4.7% | -14.5/-20.96 | +4.72% | 20% |
| [SUPRAJIT](https://in.tradingview.com/chart/?symbol=NSE:SUPRAJIT)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Automotive cables, halogen lamps, mechanical components manufacturer | ⚡ BULL_ANY_PPV | 54 | 🔄58 | ↑1.017 | ↑1d | PV | +3.1% | -43.25/-47.32 | +3.06% | 20% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · W↑9d · 🚀SS · ★ · ↑CMF11d</sub> | ✓ SAFE | Cryogenic equipment manufacturer for LNG, industrial gas, scientific applications | ⚡ BULL_ANY_PPV | 9 | ↑93 | ↑1.053 | ↑11d | PV | +19.2% | 50.28/48.45 | +5.05% | 20% |
| [KSL](https://in.tradingview.com/chart/?symbol=NSE:KSL)<br><sub>📶W9 · W↑14d · ↑CMF0d</sub> | ✓ SAFE | Alloy steel long products for precision engineering applications | ⚡ BULL_ANY_PPV | 5 | ↑76 | ↑1.049 | ↑15d | PV | +13.0% | 42.65/40.92 | +6.35% | 20% |
| [JUNIPER](https://in.tradingview.com/chart/?symbol=NSE:JUNIPER)<br><sub>📶W9 · W↑29d · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 2 | ↑46 | ↑1.050 | ↑18d | PV | +18.4% | 51.51/48.91 | +6.55% | 20% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>📶W9 · W↑24d · RVOL9x · ★ · ↑CMF10d</sub> | ✓ SAFE | Large-diameter welded steel pipes, energy infrastructure, global exports | ⚡ BULL_ANY_PPV | 0 | ↑96 | ↑1.105 | ↑26d | PV | +64.4% | 68.1/67.03 | +10.59% | 20% 🟦 |
| [MAHSEAMLES](https://in.tradingview.com/chart/?symbol=NSE:MAHSEAMLES)<br><sub>📶W9 · W↑24d · ↑CMF0d</sub> | ✓ SAFE | Seamless steel pipes tubes ERW renewable power rig | ⚡ BULL_ANY_PPV | 0 | ↑69 | ↑1.064 | ↑28d | PV | +25.3% | 67.52/66.65 | +6.32% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [ORIENTTECH](https://in.tradingview.com/chart/?symbol=NSE:ORIENTTECH)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | IT infrastructure cloud digital transformation solutions | 🔥 BULL_OS_PPV | 35 | 🔄16 | ↑0.993 | ↓34d | PV | -9.1% | -59.31/-60.58 | +2.49% | 20% |
| [SWSOLAR](https://in.tradingview.com/chart/?symbol=NSE:SWSOLAR)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Solar EPC contractor, develops utility-scale projects globally | 🔥 BULL_OS_PPV | 13 | ↓16 | ↑0.978 | ↓12d | PV | -7.3% | -61.41/-62.3 | +0.34% | 20% |
| [TCC](https://in.tradingview.com/chart/?symbol=NSE:TCC)<br><sub>🚀SS·24x · ↑CMF2d · 🔥PHX</sub> | ✓ SAFE | Real estate aggregation, digital infrastructure, consumer ecosystem platform | 🔥 BULL_OS_PPV | 5 | ↓50 | ↑0.472 | ↓28d | PV | -80.6% | -85.81/-87.28 | +7.17% | 20% |
| [POKARNA](https://in.tradingview.com/chart/?symbol=NSE:POKARNA)<br><sub>RVOL24x · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Granite quarrying, processing, engineered quartz surfaces | 🔥 BULL_OS_PPV | 5 | ↓22 | ↑0.956 | ↓23d | PV | -18.6% | -60.01/-60.67 | +0.14% | 20% 🟦 |
| [BHARATRAS](https://in.tradingview.com/chart/?symbol=NSE:BHARATRAS)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🔥 BULL_OS_PPV | 5 | ↓2 | ↑0.978 | ↓29d | PV | -8.8% | -59.16/-61.03 | +0.10% | 20% |
| [ITDC](https://in.tradingview.com/chart/?symbol=NSE:ITDC)<br><sub>RVOL90x · ↓CMF21d · DEL41%(T-1) · 🎯SLING</sub> | ✓ SAFE | Hotel operations, tours, catering for domestic tourism sector | ⚡ BULL_ANY_PPV | 54 | 🔄64 | ↑1.022 | ↑1d | PV | +5.5% | -49.25/-58.97 | +5.55% | 20% 🟦 |
| [TATAINVEST](https://in.tradingview.com/chart/?symbol=NSE:TATAINVEST)<br><sub>🚀SS·52x · ↓CMF30d</sub> | ✓ SAFE | NBFC investing in equities, debt, mutual funds | ⚡ BULL_ANY_PPV | 54 | 🔄35 | ↑1.017 | ↑1d | PV | +4.3% | -40.63/-46.9 | +4.26% | 20% |
| [DBL](https://in.tradingview.com/chart/?symbol=NSE:DBL)<br><sub>🚀SS·73x · ↓CMF13d</sub> | ✓ SAFE | Highway and bridge construction, EPC contractor | ⚡ BULL_ANY_PPV | 54 | 🔄26 | ↑1.017 | ↑1d | PV | +3.8% | -35.95/-46.03 | +3.75% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:FORCEMOT,NSE:SUPRAJIT,NSE:INOXINDIA,NSE:KSL,NSE:JUNIPER,NSE:MANINDS,NSE:MAHSEAMLES,NSE:SIGMAADV,NSE:ORIENTTECH,NSE:SWSOLAR,NSE:TCC,NSE:POKARNA,NSE:BHARATRAS,NSE:ITDC,NSE:TATAINVEST,NSE:DBL
```

### 🟢 OVERSOLD — reversal from −53/−60 (10)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CUMMINSIND](https://in.tradingview.com/chart/?symbol=NSE:CUMMINSIND)<br><sub>↑CMF1d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 59 | 🔄53 | ↑1.012 | ↑1d | — | +2.7% | -56.42/-62.44 | +2.68% | 20% |
| [JKLAKSHMI](https://in.tradingview.com/chart/?symbol=NSE:JKLAKSHMI)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Integrated cement manufacturer serving construction across regions | 🟢 BULL_OVERSOLD | 10 | ↓4 | ↑0.982 | ↓15d | — | -9.3% | -73.86/-74.61 | +1.34% | 20% |
| [ROSSARI](https://in.tradingview.com/chart/?symbol=NSE:ROSSARI)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Specialty chemicals for textiles, home care, personal care | 🟢 BULL_OVERSOLD | 9 | ↓14 | ↑0.966 | ↓16d | — | -9.4% | -70.72/-70.92 | -0.58% | 20% |
| [DABUR](https://in.tradingview.com/chart/?symbol=NSE:DABUR)<br><sub>↓CMF11d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Ayurvedic FMCG, health home care food beverages | 🟢 BULL_OVERSOLD | 5 | ↓8 | ↑0.991 | ↓32d | — | -11.3% | -66.5/-67.61 | +1.32% | 20% |
| [THERMAX](https://in.tradingview.com/chart/?symbol=NSE:THERMAX)<br><sub>↓CMF9d · 🎯SLING</sub> | ✓ SAFE | Industrial boilers, cooling systems, power equipment, pollution control | 🟢 BULL_OVERSOLD | 5 | ↓44 | ↑0.977 | ↓38d | — | -22.6% | -67.95/-70.0 | +0.19% | 20% |
| [DEEPAKFERT](https://in.tradingview.com/chart/?symbol=NSE:DEEPAKFERT)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Fertilizers, bulk chemicals, mining solutions for agriculture | 🟢 BULL_OVERSOLD | 0 | ↓44 | ↓0.970 | ↓28d | — | -15.2% | -64.78/-65.09 | -1.63% | 20% |
| [IREDA](https://in.tradingview.com/chart/?symbol=NSE:IREDA)<br><sub>↓CMF6d · 🎯SLING</sub> | ✓ SAFE | Renewable energy financing, solar wind projects, India | 🟡 BULL_OS_L2 | 42 | 🔄20 | ↑0.997 | ↓13d | — | -1.8% | -54.19/-55.17 | +1.19% | 20% |
| [CHOICEIN](https://in.tradingview.com/chart/?symbol=NSE:CHOICEIN)<br><sub>↓CMF21d · DEL64%(T-1) · 🎯SLING</sub> | ✓ SAFE | Stockbroking wealth management MSME lending insurance distribution financial services | 🟡 BULL_OS_L2 | 40 | 🔄55 | ↑1.004 | ↓30d | — | -3.5% | -52.43/-54.03 | +2.63% | 20% |
| [HITECH](https://in.tradingview.com/chart/?symbol=NSE:HITECH)<br><sub>↓CMF29d · 🎯SLING</sub> | ✓ SAFE | ERW steel pipes tubes construction automotive infrastructure | 🟡 BULL_OS_L2 | 20 | ↑18 | ↑1.002 | ↓10d | — | -0.7% | -49.38/-54.72 | +0.79% | 20% |
| [ADANIGREEN](https://in.tradingview.com/chart/?symbol=NSE:ADANIGREEN)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 0 | ↓62 | ↓0.993 | ↓40d | — | -13.6% | -53.26/-56.27 | -0.93% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CUMMINSIND,NSE:JKLAKSHMI,NSE:ROSSARI,NSE:DABUR,NSE:THERMAX,NSE:DEEPAKFERT,NSE:IREDA,NSE:CHOICEIN,NSE:HITECH,NSE:ADANIGREEN
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (20)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [DECNGOLD](https://in.tradingview.com/chart/?symbol=NSE:DECNGOLD)<br><sub>📶W9 · 🚀SS · ↓CMF5d</sub> | ✓ SAFE | Gold exploration and mining transitioning to active production | 📈 BULL_ANY_MID | 54 | 🔄50 | ↑1.016 | ↑1d | — | +3.1% | -5.03/-8.08 | +3.08% | 20% |
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>📶W9 · W↑28d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 28 | ↑64 | ↑1.014 | ↑2d | — | +2.7% | 24.78/23.85 | +1.56% | 20% |
| [CARRARO](https://in.tradingview.com/chart/?symbol=NSE:CARRARO)<br><sub>📶W9 · W↑14d · ↑CMF4d</sub> | ✓ SAFE | Axles transmissions agricultural tractors construction equipment | 📈 BULL_ANY_MID | 21 | ↑58 | ↑1.020 | ↑4d | — | +3.4% | 18.32/13.62 | +2.43% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · ↓CMF7d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 19 | ↑77 | ↑1.039 | ↑1d | — | +5.1% | -9.05/-16.39 | +5.11% | 20% |
| [UTLSOLAR](https://in.tradingview.com/chart/?symbol=NSE:UTLSOLAR)<br><sub>📶W9 · ↑CMF4d</sub> | ✓ SAFE | Solar rooftop systems, on-grid off-grid hybrid | 📈 BULL_ANY_MID | 18 | ↑50 | ↓1.005 | ↓2d | — | +1.7% | 8.38/5.12 | -2.16% | 5% 🟥 |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>📶W9 · W↑109d · ↑CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.015 | ↑3d | — | +4.4% | 32.49/29.43 | +0.17% | 20% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>📶W9 · ↑CMF2d</sub> | ⚠ CAUTION | Retail corporate banking Kerala-headquartered private sector bank | 📈 BULL_ANY_MID | 16 | ↑79 | ↑0.998 | ↓9d | — | +0.5% | -34.43/-35.07 | +0.29% | 20% |
| [KAPSTON](https://in.tradingview.com/chart/?symbol=NSE:KAPSTON)<br><sub>📶W9 · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | Security guarding and facility management staffing services | 📈 BULL_ANY_MID | 10 | ↑99 | ↑1.030 | ↑10d | — | +16.8% | 35.54/35.26 | +3.66% | 20% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | Glass-lined reactors and process equipment for pharma chemicals | 📈 BULL_ANY_MID | 6 | ↑99 | ↑1.126 | ↑14d | — | +49.8% | 80.64/79.69 | +4.99% | 5% 🟥 |
| [SUDARSCHEM](https://in.tradingview.com/chart/?symbol=NSE:SUDARSCHEM)<br><sub>📶W9 · W↑49d · ↑CMF19d</sub> | ✓ SAFE | Organic inorganic pigments chemicals coating paint industries | 📈 BULL_ANY_MID | 5 | ↑78 | ↑1.024 | ↑20d | — | +20.7% | 48.95/48.25 | +0.67% | 20% |
| [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR)<br><sub>📶W9 · 🚀SS · ↑CMF10d</sub> | ✓ SAFE | White oils, specialty petroleum, consumer healthcare applications | 📈 BULL_ANY_MID | 5 | ↑96 | ↑1.027 | ↑21d | — | +14.8% | 62.56/60.73 | +2.05% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · 🚀SS · ↑CMF29d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 0 | ↑50 | ↑1.036 | ↑24d | — | +16.7% | 57.53/55.6 | +3.13% | 20% 🟦 |
| [ZAGGLE](https://in.tradingview.com/chart/?symbol=NSE:ZAGGLE)<br><sub>↑CMF15d</sub> | ✓ SAFE | B2B expense management software, corporate spend cards | 📈 BULL_ANY_MID | 44 | 🔄3 | ↑1.004 | ↓16d | — | -1.1% | -51.9/-52.22 | +3.88% | 20% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>🚀SS · ↓CMF15d</sub> | ✓ SAFE | Microfinance bank serving low-income retail borrowers India | 📈 BULL_ANY_MID | 40 | 🔄74 | ↑1.010 | ↓60d+ | — | +16.1% | -38.07/-40.67 | +3.74% | 20% |
| [GANESHHOU](https://in.tradingview.com/chart/?symbol=NSE:GANESHHOU)<br><sub>↓CMF0d</sub> | ⚠ CAUTION | Residential real estate development Ahmedabad Gujarat region | 📈 BULL_ANY_MID | 40 | 🔄43 | ↑1.002 | ↓21d | — | +1.0% | -34.42/-35.58 | +1.91% | 20% |
| [NIITMTS](https://in.tradingview.com/chart/?symbol=NSE:NIITMTS)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | IT training services corporate upskilling global | 📈 BULL_ANY_MID | 35 | 🔄8 | ↑0.997 | ↓32d | — | -2.8% | -49.89/-50.86 | +1.40% | 20% |
| [DATAMATICS](https://in.tradingview.com/chart/?symbol=NSE:DATAMATICS)<br><sub>↓CMF30d</sub> | ✓ SAFE | Digital operations and BPO services for enterprise automation | 📈 BULL_ANY_MID | 10 | ↑36 | ↑1.008 | ↓28d | — | -5.4% | -46.32/-50.53 | +0.96% | 20% |
| [TDPOWERSYS](https://in.tradingview.com/chart/?symbol=NSE:TDPOWERSYS)<br><sub>↓CMF1d</sub> | ✓ SAFE | AC generators and motors for power generation applications | 📈 BULL_ANY_MID | 5 | ↓31 | ↑0.961 | ↓28d | — | -31.4% | -21.79/-21.99 | +1.01% | 20% |
| [GODREJCP](https://in.tradingview.com/chart/?symbol=NSE:GODREJCP)<br><sub>↑CMF21d</sub> | ✓ SAFE | Household insecticides, personal care, emerging markets FMCG | 📈 BULL_ANY_MID | 5 | ↓7 | ↑0.983 | ↓23d | — | -17.8% | -52.28/-52.78 | +0.71% | 20% |
| [JSWENERGY](https://in.tradingview.com/chart/?symbol=NSE:JSWENERGY)<br><sub>↓CMF8d · ⚠️TRAP</sub> | ✓ SAFE | Thermal coal renewable power generation utility India | 📈 BULL_ANY_MID | 0 | ↓45 | ↓0.992 | ↓26d | — | -2.4% | -41.63/-41.72 | -0.81% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:DECNGOLD,NSE:HINDZINC,NSE:CARRARO,NSE:ADANIENT,NSE:UTLSOLAR,NSE:BOSCHLTD,NSE:FEDERALBNK,NSE:KAPSTON,NSE:SETL,NSE:SUDARSCHEM,NSE:GANDHAR,NSE:MEESHO,NSE:ZAGGLE,NSE:UJJIVANSFB,NSE:GANESHHOU,NSE:NIITMTS,NSE:DATAMATICS,NSE:TDPOWERSYS,NSE:GODREJCP,NSE:JSWENERGY
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
