> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-08-10
*Generated 2026-08-10 15:46 IST*

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

**Total bull crosses today: 75** · 30 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:HINDOILEXP,NSE:NPST,NSE:GIPCL,NSE:POLYMED,NSE:INDSWFTLAB,NSE:RPEL,NSE:KOVAI,NSE:ENTERO,NSE:TASTYBITE,NSE:PIXTRANS,NSE:MOL,NSE:POLYPLEX,NSE:BALRAMCHIN,NSE:UNIVCABLES,NSE:KAPSTON,NSE:INNOVACAP,NSE:EBGNG,NSE:DALBHARAT,NSE:GNA,NSE:COROMANDEL,NSE:AYE,NSE:KMEW,NSE:HNDFDS,NSE:HCG,NSE:AJANTPHARM,NSE:AARTIDRUGS,NSE:JKPAPER,NSE:HSCL,NSE:OFSS,NSE:SANATHAN,NSE:NEOGEN,NSE:SENORES,NSE:CONCORDBIO,NSE:KROSS,NSE:NESTLEIND,NSE:EMCURE,NSE:LENSKART,NSE:THYROCARE,NSE:TANLA,NSE:SHRIRAMPPS,NSE:JASH,NSE:JUBLPHARMA,NSE:VESUVIUS,NSE:EPACK,NSE:VENUSPIPES,NSE:JARO,NSE:THERMAX,NSE:SERVOTECH,NSE:VBL,NSE:NAVNETEDUL,NSE:POWERINDIA,NSE:GODREJCP,NSE:ELECTHERM,NSE:HONDAPOWER,NSE:CESC,NSE:FORTIS,NSE:ARFIN,NSE:MCX,NSE:CUB,NSE:AAVAS,NSE:FLAIR,NSE:TATACOMM,NSE:DATAPATTNS,NSE:EXPLEOSOL,NSE:KALPATARU,NSE:INDIAMART,NSE:STAR,NSE:ADANIPORTS,NSE:CANFINHOME,NSE:UTIAMC,NSE:IVALUE,NSE:WAAREERTL,NSE:AVANTIFEED,NSE:SOLARA,NSE:SWARAJENG
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (39)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [HINDOILEXP](https://in.tradingview.com/chart/?symbol=NSE:HINDOILEXP)<br><sub>📶W9 · W↑1d · ↑CMF0d</sub> | ✓ SAFE | Crude oil natural gas exploration production onshore offshore | ⚡ BULL_ANY_PPV | 94 | 🔄47 | ↑1.026 | ↑1d | SQ·PV | +5.2% | -7.16/-7.29 | +5.20% | 20% |
| [NPST](https://in.tradingview.com/chart/?symbol=NSE:NPST)<br><sub>📶W9 · ↓CMF28d</sub> | ✓ SAFE | UPI payments software and real-time transaction processing platform | ⚡ BULL_ANY_PPV | 94 | 🔄68 | ↑1.020 | ↑1d | SQ·PV | +4.0% | -29.74/-34.98 | +3.95% | 10% 🟨 |
| [GIPCL](https://in.tradingview.com/chart/?symbol=NSE:GIPCL)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF29d</sub> | ✓ SAFE | Thermal coal power generation 1184MW capacity Gujarat utilities | ⚡ BULL_ANY_PPV | 94 | 🔄46 | ↑1.022 | ↑1d | SQ·PV | +4.3% | -9.95/-10.16 | +4.31% | 20% |
| [POLYMED](https://in.tradingview.com/chart/?symbol=NSE:POLYMED)<br><sub>📶W9 · W↑41d · RVOL10x · ↑CMF0d</sub> | ✓ SAFE | Plastic medical disposables manufacturer serving hospitals globally | ⚡ BULL_ANY_PPV | 89 | 🔄57 | ↑1.036 | ↑1d | SQ·PV | +4.6% | 39.81/34.06 | +4.64% | 20% |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB)<br><sub>📶W9 · 🚀SS · ↓CMF1d</sub> | ✓ SAFE | Macrolide antibiotics bulk drug manufacturer for global pharma markets | ⚡ BULL_ANY_PPV | 89 | 🔄98 | ↑1.032 | ↑1d | SQ·PV | +3.9% | 23.45/18.69 | +3.87% | 20% |
| [RPEL](https://in.tradingview.com/chart/?symbol=NSE:RPEL)<br><sub>📶W9 · ↓CMF7d</sub> | ✓ SAFE | Silica ramming mass and quartz powder for induction furnaces | ⚡ BULL_ANY_PPV | 89 | 🔄95 | ↑1.032 | ↑1d | SQ·PV | +4.6% | -0.19/-7.78 | +4.56% | 20% |
| [KOVAI](https://in.tradingview.com/chart/?symbol=NSE:KOVAI)<br><sub>📶W9 · 🚀SS · ↓CMF14d</sub> | ⚠ CAUTION | Tertiary care hospital pharmacy medical education Coimbatore healthcare | ⚡ BULL_ANY_PPV | 89 | 🔄50 | ↑1.038 | ↑1d | SQ·PV | +5.5% | 5.75/-8.89 | +5.45% | 20% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>📶W9 · W↑26d · 🚀SS·17x · ↓CMF2d</sub> | ✓ SAFE | Pharmaceutical and surgical product distributor serving hospitals | ⚡ BULL_ANY_PPV | 75 | 🔄64 | ↑1.050 | ↑15d | SQ·PV | +10.5% | 59.62/48.31 | +5.83% | 20% |
| [TASTYBITE](https://in.tradingview.com/chart/?symbol=NSE:TASTYBITE)<br><sub>📶W9 · W↑89d · ↑CMF0d</sub> | ✓ SAFE | Ready-to-eat ethnic vegetarian meals packaged foods export | ⚡ BULL_ANY_PPV | 55 | ↑66 | ↑1.025 | ↑10d | SQ·PV | +7.3% | 62.17/61.15 | +1.39% | 20% |
| [PIXTRANS](https://in.tradingview.com/chart/?symbol=NSE:PIXTRANS)<br><sub>📶W9 · W↑1d · 🚀SS·75x · ↑CMF8d</sub> | ✓ SAFE | V-belts and power transmission components for industrial machinery | ⚡ BULL_ANY_PPV | 49 | 🔄83 | ↑1.122 | ↑1d | PV | +15.7% | -8.71/-24.87 | +15.68% | 20% |
| [MOL](https://in.tradingview.com/chart/?symbol=NSE:MOL)<br><sub>📶W9 · W↑16d · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Chemical manufacturer: pigments, agrochemicals, crop nutrition | ⚡ BULL_ANY_PPV | 49 | 🔄30 | ↑1.075 | ↑1d | PV | +11.0% | 17.78/16.56 | +10.97% | 20% |
| [POLYPLEX](https://in.tradingview.com/chart/?symbol=NSE:POLYPLEX)<br><sub>📶W9 · W↑41d · ↑CMF14d</sub> | ✓ SAFE | BOPET polyester films flexible packaging industrial applications | ⚡ BULL_ANY_PPV | 45 | 🔄78 | ↑1.049 | ↑5d | PV | +7.8% | 48.77/41.78 | +5.72% | 20% |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>📶W9 · W↑31d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE | Sugar manufacturing, distillery, power cogeneration for domestic consumption | ⚡ BULL_ANY_PPV | 14 | ↑82 | ↑1.040 | ↑6d | PV | +11.8% | 54.24/52.78 | +3.44% | 20% |
| [UNIVCABLES](https://in.tradingview.com/chart/?symbol=NSE:UNIVCABLES)<br><sub>📶W9 · W↑11d · 🚀SS·14x · ★ · ↑CMF12d</sub> | ✓ SAFE | Electrical cables and power solutions manufacturer for infrastructure | ⚡ BULL_ANY_PPV | 4 | ↑98 | ↑1.185 | ↑16d | PV | +45.1% | 67.18/62.4 | +20.00% | 20% |
| [KAPSTON](https://in.tradingview.com/chart/?symbol=NSE:KAPSTON)<br><sub>📶W9 · W↑36d · 🚀SS · ★ · ↑CMF21d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 0 | ↑99 | ↑1.106 | ↑23d | PV | +59.7% | 76.9/75.55 | +7.63% | 20% |
| [INNOVACAP](https://in.tradingview.com/chart/?symbol=NSE:INNOVACAP)<br><sub>📶W9 · ↓CMF29d</sub> | ⚠ CAUTION | Tablet manufacturing pharmaceuticals India generic drugs | 📈 BULL_ANY_MID | 99 | 🔄69 | ↑1.008 | ↑1d | SQ | +2.3% | -23.06/-26.34 | +2.29% | 20% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>📶W9 · ↓CMF15d</sub> | ✓ SAFE | Refurbished electronics retailer distributor ICT devices consumer segment | 📈 BULL_ANY_MID | 94 | 🔄92 | ↑1.028 | ↑1d | SQ | +5.7% | -32.19/-34.8 | +5.71% | 5% 🟥 |
| [DALBHARAT](https://in.tradingview.com/chart/?symbol=NSE:DALBHARAT)<br><sub>📶W9 · W↑36d · ↑CMF18d</sub> | ✓ SAFE | Cement manufacturer, construction materials, Indian infrastructure demand | 📈 BULL_ANY_MID | 94 | 🔄27 | ↑1.009 | ↑6d | SQ | +2.5% | 32.12/30.63 | +0.96% | 20% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>📶W9 · W↑36d · ↓CMF0d</sub> | ✓ SAFE | Rear axles and shafts for commercial vehicles globally | 📈 BULL_ANY_MID | 91 | 🔄91 | ↑1.020 | ↑4d | SQ | +4.4% | 37.59/37.55 | +2.18% | 20% |
| [COROMANDEL](https://in.tradingview.com/chart/?symbol=NSE:COROMANDEL)<br><sub>📶W9 · W↑46d · ↑CMF16d</sub> | ⚠ CAUTION | Phosphatic fertilizers, crop nutrients, Indian agriculture sector | 📈 BULL_ANY_MID | 90 | 🔄38 | ↑1.011 | ↑10d | SQ | +4.7% | 36.56/36.4 | +1.40% | 20% |
| [AYE](https://in.tradingview.com/chart/?symbol=NSE:AYE)<br><sub>📶W9 · ↑CMF27d</sub> | ✓ SAFE | Micro-enterprise secured lending NBFC working capital loans | 📈 BULL_ANY_MID | 89 | 🔄50 | ↑1.042 | ↑1d | SQ | +4.7% | 4.93/-3.65 | +4.72% | 20% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>📶W9 · W↑36d · ↑CMF8d</sub> | ✓ SAFE | Dredging, marine engineering, ship repair, ports infrastructure | 📈 BULL_ANY_MID | 83 | 🔄97 | ↑1.029 | ↑12d | SQ | +10.9% | 52.21/51.69 | +2.71% | 20% |
| [HNDFDS](https://in.tradingview.com/chart/?symbol=NSE:HNDFDS)<br><sub>📶W9 · W↑96d · 🚀SS · ↑CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 80 | 🔄63 | ↑1.013 | ↑22d | SQ | +6.9% | 43.5/42.21 | +1.63% | 20% |
| [HCG](https://in.tradingview.com/chart/?symbol=NSE:HCG)<br><sub>📶W9 · W↑31d · ↑CMF1d</sub> | ✓ SAFE | Oncology and fertility hospital network across India | 📈 BULL_ANY_MID | 72 | 🔄65 | ↑1.052 | ↑18d | SQ | +10.6% | 48.53/36.03 | +5.89% | 20% |
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM)<br><sub>📶W9 · W↑41d · ↑CMF30d</sub> | ⚠ CAUTION | Branded generics tablets capsules ophthalmology gastroenterology dermatology | 📈 BULL_ANY_MID | 67 | ↑74 | ↑1.011 | ↑3d | SQ | +2.0% | 40.29/38.36 | +0.49% | 20% |
| [AARTIDRUGS](https://in.tradingview.com/chart/?symbol=NSE:AARTIDRUGS)<br><sub>📶W9 · W↑31d · ↑CMF0d</sub> | ✓ SAFE | API manufacturer, pharma intermediates, specialty chemicals producer | 📈 BULL_ANY_MID | 63 | ↑48 | ↑1.019 | ↑2d | SQ | +2.9% | 41.13/34.66 | +1.53% | 20% |
| [JKPAPER](https://in.tradingview.com/chart/?symbol=NSE:JKPAPER)<br><sub>📶W9 · W↑21d · ↓CMF13d</sub> | ✓ SAFE | Paper manufacturer: office, coated, packaging boards | 📈 BULL_ANY_MID | 56 | 🔄57 | ↑1.013 | ↑4d | — | +2.6% | 28.99/28.98 | +1.46% | 20% |
| [HSCL](https://in.tradingview.com/chart/?symbol=NSE:HSCL)<br><sub>📶W9 · 🚀SS · ↑CMF16d</sub> | ✓ SAFE | Coal pitch and advanced carbon materials manufacturer | 📈 BULL_ANY_MID | 54 | 🔄91 | ↑1.019 | ↑1d | — | +2.6% | 32.14/29.95 | +2.58% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄83 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [SANATHAN](https://in.tradingview.com/chart/?symbol=NSE:SANATHAN)<br><sub>📶W9 · W↑41d · ↓CMF3d</sub> | ✓ SAFE | Polyester cotton yarn technical textiles manufacturer exporter | 📈 BULL_ANY_MID | 53 | 🔄52 | ↑1.011 | ↑7d | — | +3.8% | 40.13/39.68 | +0.86% | 20% |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>📶W9 · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | Bromine lithium specialty chemicals pharma agrochemicals engineering | 📈 BULL_ANY_MID | 49 | 🔄88 | ↑1.054 | ↑1d | — | +7.4% | -1.51/-7.24 | +7.43% | 20% |
| [SENORES](https://in.tradingview.com/chart/?symbol=NSE:SENORES)<br><sub>📶W9 · ↓CMF9d</sub> | ✓ SAFE | Complex generics pharma targeting affordable specialty therapeutics | 📈 BULL_ANY_MID | 49 | 🔄95 | ↑1.047 | ↑1d | — | +5.9% | -7.8/-15.68 | +5.93% | 20% |
| [CONCORDBIO](https://in.tradingview.com/chart/?symbol=NSE:CONCORDBIO)<br><sub>📶W9 · W↑84d · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Fermentation APIs immunosuppressants oncology biopharma manufacturer | 📈 BULL_ANY_MID | 41 | 🔄56 | ↑1.034 | ↑9d | — | +13.0% | 31.9/30.61 | +3.96% | 20% |
| [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS)<br><sub>📶W9 · W↑16d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Commercial vehicle axles and tractor components manufacturer | 📈 BULL_ANY_MID | 18 | ↑60 | ↑1.021 | ↑7d | — | +7.0% | 31.05/29.52 | +1.63% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 11 | ↑68 | ↓1.011 | ↑9d | — | +5.3% | 52.94/52.13 | +0.00% | 20% |
| [EMCURE](https://in.tradingview.com/chart/?symbol=NSE:EMCURE)<br><sub>📶W9 · W↑11d · ↓CMF9d</sub> | ✓ SAFE | Oral antibiotics and generics for domestic European markets | 📈 BULL_ANY_MID | 9 | ↑82 | ↑1.023 | ↑16d | — | +11.9% | 54.09/51.88 | +0.85% | 20% |
| [LENSKART](https://in.tradingview.com/chart/?symbol=NSE:LENSKART)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Eyewear design manufacturing retail omnichannel direct consumer | 📈 BULL_ANY_MID | 5 | ↑50 | ↑1.030 | ↑30d | — | +15.9% | 64.3/61.91 | +2.24% | 20% |
| [THYROCARE](https://in.tradingview.com/chart/?symbol=NSE:THYROCARE)<br><sub>📶W9 · W↑16d · ★ · ↓CMF11d</sub> | ✓ SAFE | Thyrocare Technologies Ltd

Diagnostic pathology and radiology services for hospitals | 📈 BULL_ANY_MID | 4 | ↑86 | ↑1.046 | ↑16d | — | +19.5% | 55.34/53.79 | +3.12% | 20% |
| [TANLA](https://in.tradingview.com/chart/?symbol=NSE:TANLA)<br><sub>📶W9 · W↑89d · ↓CMF12d</sub> | ✓ SAFE | CPaaS provider SMS voice OTP enterprise messaging | 📈 BULL_ANY_MID | 0 | ↑66 | ↑1.038 | ↑22d | — | +21.2% | 59.52/58.45 | +3.02% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:HINDOILEXP,NSE:NPST,NSE:GIPCL,NSE:POLYMED,NSE:INDSWFTLAB,NSE:RPEL,NSE:KOVAI,NSE:ENTERO,NSE:TASTYBITE,NSE:PIXTRANS,NSE:MOL,NSE:POLYPLEX,NSE:BALRAMCHIN,NSE:UNIVCABLES,NSE:KAPSTON,NSE:INNOVACAP,NSE:EBGNG,NSE:DALBHARAT,NSE:GNA,NSE:COROMANDEL,NSE:AYE,NSE:KMEW,NSE:HNDFDS,NSE:HCG,NSE:AJANTPHARM,NSE:AARTIDRUGS,NSE:JKPAPER,NSE:HSCL,NSE:OFSS,NSE:SANATHAN,NSE:NEOGEN,NSE:SENORES,NSE:CONCORDBIO,NSE:KROSS,NSE:NESTLEIND,NSE:EMCURE,NSE:LENSKART,NSE:THYROCARE,NSE:TANLA
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (50)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [HINDOILEXP](https://in.tradingview.com/chart/?symbol=NSE:HINDOILEXP)<br><sub>📶W9 · W↑1d · ↑CMF0d</sub> | ✓ SAFE | Crude oil natural gas exploration production onshore offshore | ⚡ BULL_ANY_PPV | 94 | 🔄47 | ↑1.026 | ↑1d | SQ·PV | +5.2% | -7.16/-7.29 | +5.20% | 20% |
| [NPST](https://in.tradingview.com/chart/?symbol=NSE:NPST)<br><sub>📶W9 · ↓CMF28d</sub> | ✓ SAFE | UPI payments software and real-time transaction processing platform | ⚡ BULL_ANY_PPV | 94 | 🔄68 | ↑1.020 | ↑1d | SQ·PV | +4.0% | -29.74/-34.98 | +3.95% | 10% 🟨 |
| [GIPCL](https://in.tradingview.com/chart/?symbol=NSE:GIPCL)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF29d</sub> | ✓ SAFE | Thermal coal power generation 1184MW capacity Gujarat utilities | ⚡ BULL_ANY_PPV | 94 | 🔄46 | ↑1.022 | ↑1d | SQ·PV | +4.3% | -9.95/-10.16 | +4.31% | 20% |
| [POLYMED](https://in.tradingview.com/chart/?symbol=NSE:POLYMED)<br><sub>📶W9 · W↑41d · RVOL10x · ↑CMF0d</sub> | ✓ SAFE | Plastic medical disposables manufacturer serving hospitals globally | ⚡ BULL_ANY_PPV | 89 | 🔄57 | ↑1.036 | ↑1d | SQ·PV | +4.6% | 39.81/34.06 | +4.64% | 20% |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB)<br><sub>📶W9 · 🚀SS · ↓CMF1d</sub> | ✓ SAFE | Macrolide antibiotics bulk drug manufacturer for global pharma markets | ⚡ BULL_ANY_PPV | 89 | 🔄98 | ↑1.032 | ↑1d | SQ·PV | +3.9% | 23.45/18.69 | +3.87% | 20% |
| [RPEL](https://in.tradingview.com/chart/?symbol=NSE:RPEL)<br><sub>📶W9 · ↓CMF7d</sub> | ✓ SAFE | Silica ramming mass and quartz powder for induction furnaces | ⚡ BULL_ANY_PPV | 89 | 🔄95 | ↑1.032 | ↑1d | SQ·PV | +4.6% | -0.19/-7.78 | +4.56% | 20% |
| [KOVAI](https://in.tradingview.com/chart/?symbol=NSE:KOVAI)<br><sub>📶W9 · 🚀SS · ↓CMF14d</sub> | ⚠ CAUTION | Tertiary care hospital pharmacy medical education Coimbatore healthcare | ⚡ BULL_ANY_PPV | 89 | 🔄50 | ↑1.038 | ↑1d | SQ·PV | +5.5% | 5.75/-8.89 | +5.45% | 20% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>📶W9 · W↑26d · 🚀SS·17x · ↓CMF2d</sub> | ✓ SAFE | Pharmaceutical and surgical product distributor serving hospitals | ⚡ BULL_ANY_PPV | 75 | 🔄64 | ↑1.050 | ↑15d | SQ·PV | +10.5% | 59.62/48.31 | +5.83% | 20% |
| [TASTYBITE](https://in.tradingview.com/chart/?symbol=NSE:TASTYBITE)<br><sub>📶W9 · W↑89d · ↑CMF0d</sub> | ✓ SAFE | Ready-to-eat ethnic vegetarian meals packaged foods export | ⚡ BULL_ANY_PPV | 55 | ↑66 | ↑1.025 | ↑10d | SQ·PV | +7.3% | 62.17/61.15 | +1.39% | 20% |
| [PIXTRANS](https://in.tradingview.com/chart/?symbol=NSE:PIXTRANS)<br><sub>📶W9 · W↑1d · 🚀SS·75x · ↑CMF8d</sub> | ✓ SAFE | V-belts and power transmission components for industrial machinery | ⚡ BULL_ANY_PPV | 49 | 🔄83 | ↑1.122 | ↑1d | PV | +15.7% | -8.71/-24.87 | +15.68% | 20% |
| [MOL](https://in.tradingview.com/chart/?symbol=NSE:MOL)<br><sub>📶W9 · W↑16d · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Chemical manufacturer: pigments, agrochemicals, crop nutrition | ⚡ BULL_ANY_PPV | 49 | 🔄30 | ↑1.075 | ↑1d | PV | +11.0% | 17.78/16.56 | +10.97% | 20% |
| [POLYPLEX](https://in.tradingview.com/chart/?symbol=NSE:POLYPLEX)<br><sub>📶W9 · W↑41d · ↑CMF14d</sub> | ✓ SAFE | BOPET polyester films flexible packaging industrial applications | ⚡ BULL_ANY_PPV | 45 | 🔄78 | ↑1.049 | ↑5d | PV | +7.8% | 48.77/41.78 | +5.72% | 20% |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>📶W9 · W↑31d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE | Sugar manufacturing, distillery, power cogeneration for domestic consumption | ⚡ BULL_ANY_PPV | 14 | ↑82 | ↑1.040 | ↑6d | PV | +11.8% | 54.24/52.78 | +3.44% | 20% |
| [UNIVCABLES](https://in.tradingview.com/chart/?symbol=NSE:UNIVCABLES)<br><sub>📶W9 · W↑11d · 🚀SS·14x · ★ · ↑CMF12d</sub> | ✓ SAFE | Electrical cables and power solutions manufacturer for infrastructure | ⚡ BULL_ANY_PPV | 4 | ↑98 | ↑1.185 | ↑16d | PV | +45.1% | 67.18/62.4 | +20.00% | 20% |
| [KAPSTON](https://in.tradingview.com/chart/?symbol=NSE:KAPSTON)<br><sub>📶W9 · W↑36d · 🚀SS · ★ · ↑CMF21d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 0 | ↑99 | ↑1.106 | ↑23d | PV | +59.7% | 76.9/75.55 | +7.63% | 20% |
| [INNOVACAP](https://in.tradingview.com/chart/?symbol=NSE:INNOVACAP)<br><sub>📶W9 · ↓CMF29d</sub> | ⚠ CAUTION | Tablet manufacturing pharmaceuticals India generic drugs | 📈 BULL_ANY_MID | 99 | 🔄69 | ↑1.008 | ↑1d | SQ | +2.3% | -23.06/-26.34 | +2.29% | 20% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>📶W9 · ↓CMF15d</sub> | ✓ SAFE | Refurbished electronics retailer distributor ICT devices consumer segment | 📈 BULL_ANY_MID | 94 | 🔄92 | ↑1.028 | ↑1d | SQ | +5.7% | -32.19/-34.8 | +5.71% | 5% 🟥 |
| [DALBHARAT](https://in.tradingview.com/chart/?symbol=NSE:DALBHARAT)<br><sub>📶W9 · W↑36d · ↑CMF18d</sub> | ✓ SAFE | Cement manufacturer, construction materials, Indian infrastructure demand | 📈 BULL_ANY_MID | 94 | 🔄27 | ↑1.009 | ↑6d | SQ | +2.5% | 32.12/30.63 | +0.96% | 20% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>📶W9 · W↑36d · ↓CMF0d</sub> | ✓ SAFE | Rear axles and shafts for commercial vehicles globally | 📈 BULL_ANY_MID | 91 | 🔄91 | ↑1.020 | ↑4d | SQ | +4.4% | 37.59/37.55 | +2.18% | 20% |
| [COROMANDEL](https://in.tradingview.com/chart/?symbol=NSE:COROMANDEL)<br><sub>📶W9 · W↑46d · ↑CMF16d</sub> | ⚠ CAUTION | Phosphatic fertilizers, crop nutrients, Indian agriculture sector | 📈 BULL_ANY_MID | 90 | 🔄38 | ↑1.011 | ↑10d | SQ | +4.7% | 36.56/36.4 | +1.40% | 20% |
| [AYE](https://in.tradingview.com/chart/?symbol=NSE:AYE)<br><sub>📶W9 · ↑CMF27d</sub> | ✓ SAFE | Micro-enterprise secured lending NBFC working capital loans | 📈 BULL_ANY_MID | 89 | 🔄50 | ↑1.042 | ↑1d | SQ | +4.7% | 4.93/-3.65 | +4.72% | 20% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>📶W9 · W↑36d · ↑CMF8d</sub> | ✓ SAFE | Dredging, marine engineering, ship repair, ports infrastructure | 📈 BULL_ANY_MID | 83 | 🔄97 | ↑1.029 | ↑12d | SQ | +10.9% | 52.21/51.69 | +2.71% | 20% |
| [HNDFDS](https://in.tradingview.com/chart/?symbol=NSE:HNDFDS)<br><sub>📶W9 · W↑96d · 🚀SS · ↑CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 80 | 🔄63 | ↑1.013 | ↑22d | SQ | +6.9% | 43.5/42.21 | +1.63% | 20% |
| [HCG](https://in.tradingview.com/chart/?symbol=NSE:HCG)<br><sub>📶W9 · W↑31d · ↑CMF1d</sub> | ✓ SAFE | Oncology and fertility hospital network across India | 📈 BULL_ANY_MID | 72 | 🔄65 | ↑1.052 | ↑18d | SQ | +10.6% | 48.53/36.03 | +5.89% | 20% |
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM)<br><sub>📶W9 · W↑41d · ↑CMF30d</sub> | ⚠ CAUTION | Branded generics tablets capsules ophthalmology gastroenterology dermatology | 📈 BULL_ANY_MID | 67 | ↑74 | ↑1.011 | ↑3d | SQ | +2.0% | 40.29/38.36 | +0.49% | 20% |
| [AARTIDRUGS](https://in.tradingview.com/chart/?symbol=NSE:AARTIDRUGS)<br><sub>📶W9 · W↑31d · ↑CMF0d</sub> | ✓ SAFE | API manufacturer, pharma intermediates, specialty chemicals producer | 📈 BULL_ANY_MID | 63 | ↑48 | ↑1.019 | ↑2d | SQ | +2.9% | 41.13/34.66 | +1.53% | 20% |
| [JKPAPER](https://in.tradingview.com/chart/?symbol=NSE:JKPAPER)<br><sub>📶W9 · W↑21d · ↓CMF13d</sub> | ✓ SAFE | Paper manufacturer: office, coated, packaging boards | 📈 BULL_ANY_MID | 56 | 🔄57 | ↑1.013 | ↑4d | — | +2.6% | 28.99/28.98 | +1.46% | 20% |
| [HSCL](https://in.tradingview.com/chart/?symbol=NSE:HSCL)<br><sub>📶W9 · 🚀SS · ↑CMF16d</sub> | ✓ SAFE | Coal pitch and advanced carbon materials manufacturer | 📈 BULL_ANY_MID | 54 | 🔄91 | ↑1.019 | ↑1d | — | +2.6% | 32.14/29.95 | +2.58% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄83 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [SANATHAN](https://in.tradingview.com/chart/?symbol=NSE:SANATHAN)<br><sub>📶W9 · W↑41d · ↓CMF3d</sub> | ✓ SAFE | Polyester cotton yarn technical textiles manufacturer exporter | 📈 BULL_ANY_MID | 53 | 🔄52 | ↑1.011 | ↑7d | — | +3.8% | 40.13/39.68 | +0.86% | 20% |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>📶W9 · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | Bromine lithium specialty chemicals pharma agrochemicals engineering | 📈 BULL_ANY_MID | 49 | 🔄88 | ↑1.054 | ↑1d | — | +7.4% | -1.51/-7.24 | +7.43% | 20% |
| [SENORES](https://in.tradingview.com/chart/?symbol=NSE:SENORES)<br><sub>📶W9 · ↓CMF9d</sub> | ✓ SAFE | Complex generics pharma targeting affordable specialty therapeutics | 📈 BULL_ANY_MID | 49 | 🔄95 | ↑1.047 | ↑1d | — | +5.9% | -7.8/-15.68 | +5.93% | 20% |
| [CONCORDBIO](https://in.tradingview.com/chart/?symbol=NSE:CONCORDBIO)<br><sub>📶W9 · W↑84d · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Fermentation APIs immunosuppressants oncology biopharma manufacturer | 📈 BULL_ANY_MID | 41 | 🔄56 | ↑1.034 | ↑9d | — | +13.0% | 31.9/30.61 | +3.96% | 20% |
| [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS)<br><sub>📶W9 · W↑16d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Commercial vehicle axles and tractor components manufacturer | 📈 BULL_ANY_MID | 18 | ↑60 | ↑1.021 | ↑7d | — | +7.0% | 31.05/29.52 | +1.63% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 11 | ↑68 | ↓1.011 | ↑9d | — | +5.3% | 52.94/52.13 | +0.00% | 20% |
| [EMCURE](https://in.tradingview.com/chart/?symbol=NSE:EMCURE)<br><sub>📶W9 · W↑11d · ↓CMF9d</sub> | ✓ SAFE | Oral antibiotics and generics for domestic European markets | 📈 BULL_ANY_MID | 9 | ↑82 | ↑1.023 | ↑16d | — | +11.9% | 54.09/51.88 | +0.85% | 20% |
| [LENSKART](https://in.tradingview.com/chart/?symbol=NSE:LENSKART)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Eyewear design manufacturing retail omnichannel direct consumer | 📈 BULL_ANY_MID | 5 | ↑50 | ↑1.030 | ↑30d | — | +15.9% | 64.3/61.91 | +2.24% | 20% |
| [THYROCARE](https://in.tradingview.com/chart/?symbol=NSE:THYROCARE)<br><sub>📶W9 · W↑16d · ★ · ↓CMF11d</sub> | ✓ SAFE | Thyrocare Technologies Ltd

Diagnostic pathology and radiology services for hospitals | 📈 BULL_ANY_MID | 4 | ↑86 | ↑1.046 | ↑16d | — | +19.5% | 55.34/53.79 | +3.12% | 20% |
| [TANLA](https://in.tradingview.com/chart/?symbol=NSE:TANLA)<br><sub>📶W9 · W↑89d · ↓CMF12d</sub> | ✓ SAFE | CPaaS provider SMS voice OTP enterprise messaging | 📈 BULL_ANY_MID | 0 | ↑66 | ↑1.038 | ↑22d | — | +21.2% | 59.52/58.45 | +3.02% | 20% |
| [SHRIRAMPPS](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMPPS)<br><sub>↓CMF30d</sub> | ✓ SAFE | Residential real estate developer mid-market South India housing | ⚡ BULL_ANY_PPV | 94 | 🔄43 | ↑1.017 | ↑1d | SQ·PV | +2.9% | -31.96/-38.05 | +2.94% | 20% |
| [JASH](https://in.tradingview.com/chart/?symbol=NSE:JASH)<br><sub>↓CMF1d</sub> | ✓ SAFE | Pumps gates valves water wastewater infrastructure equipment manufacturer | ⚡ BULL_ANY_PPV | 59 | 🔄70 | ↑1.010 | ↑1d | PV | +1.7% | -26.93/-31.69 | +1.68% | 20% |
| [JUBLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:JUBLPHARMA)<br><sub>↑CMF1d</sub> | ⚠ CAUTION | Radiopharmaceuticals, immunotherapy, contract pharma manufacturing globally | ⚡ BULL_ANY_PPV | 54 | 🔄25 | ↑1.016 | ↑1d | PV | +3.3% | -33.16/-36.37 | +3.29% | 20% |
| [VESUVIUS](https://in.tradingview.com/chart/?symbol=NSE:VESUVIUS)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Refractory ceramics for steel foundry molten metal flows | ⚡ BULL_ANY_PPV | 54 | 🔄25 | ↑1.022 | ↑1d | PV | +3.1% | -32.2/-39.27 | +3.10% | 20% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>🚀SS · ↑CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄90 | ↑1.009 | ↑1d | SQ | +2.7% | -36.34/-42.32 | +2.74% | 20% |
| [GODREJCP](https://in.tradingview.com/chart/?symbol=NSE:GODREJCP)<br><sub>W↑33d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 98 | 🔄36 | ↑1.008 | ↑2d | SQ | +2.1% | 25.85/25.42 | +1.03% | 20% |
| [ELECTHERM](https://in.tradingview.com/chart/?symbol=NSE:ELECTHERM)<br><sub>↓CMF23d</sub> | ✓ SAFE | Industrial heating equipment manufacturer, process heating sector | 📈 BULL_ANY_MID | 80 | 🔄79 | ↑1.007 | ↓27d | SQ | -6.4% | -34.63/-38.05 | +2.62% | 10% 🟨 |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>↓CMF16d</sub> | ✓ SAFE | Commodity futures trading exchange platform India | 📈 BULL_ANY_MID | 54 | 🔄73 | ↑1.026 | ↑1d | — | +4.6% | -44.2/-51.23 | +4.60% | 20% |
| [CUB](https://in.tradingview.com/chart/?symbol=NSE:CUB)<br><sub>🚀SS · ↓CMF6d</sub> | ✓ SAFE | Private bank serving SMEs, MSMEs, retail customers, South India | 📈 BULL_ANY_MID | 54 | 🔄14 | ↑1.016 | ↑1d | — | +2.1% | -18.23/-22.01 | +2.08% | 20% |
| [AAVAS](https://in.tradingview.com/chart/?symbol=NSE:AAVAS)<br><sub>🚀SS · ↓CMF13d</sub> | ✓ SAFE | Housing loans for rural semi-urban low income customers | 📈 BULL_ANY_MID | 54 | 🔄32 | ↑1.007 | ↓6d | — | +3.2% | -32.45/-34.27 | +2.37% | 20% |
| [EXPLEOSOL](https://in.tradingview.com/chart/?symbol=NSE:EXPLEOSOL)<br><sub>W↑11d · ↓CMF30d</sub> | ✓ SAFE | Software testing QA services banking financial sector | 📈 BULL_ANY_MID | 18 | ↑17 | ↓1.009 | ↑2d | — | +1.8% | 3.95/1.61 | -0.15% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:HINDOILEXP,NSE:NPST,NSE:GIPCL,NSE:POLYMED,NSE:INDSWFTLAB,NSE:RPEL,NSE:KOVAI,NSE:ENTERO,NSE:TASTYBITE,NSE:PIXTRANS,NSE:MOL,NSE:POLYPLEX,NSE:BALRAMCHIN,NSE:UNIVCABLES,NSE:KAPSTON,NSE:INNOVACAP,NSE:EBGNG,NSE:DALBHARAT,NSE:GNA,NSE:COROMANDEL,NSE:AYE,NSE:KMEW,NSE:HNDFDS,NSE:HCG,NSE:AJANTPHARM,NSE:AARTIDRUGS,NSE:JKPAPER,NSE:HSCL,NSE:OFSS,NSE:SANATHAN,NSE:NEOGEN,NSE:SENORES,NSE:CONCORDBIO,NSE:KROSS,NSE:NESTLEIND,NSE:EMCURE,NSE:LENSKART,NSE:THYROCARE,NSE:TANLA,NSE:SHRIRAMPPS,NSE:JASH,NSE:JUBLPHARMA,NSE:VESUVIUS,NSE:POWERINDIA,NSE:GODREJCP,NSE:ELECTHERM,NSE:MCX,NSE:CUB,NSE:AAVAS,NSE:EXPLEOSOL
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (30)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [HINDOILEXP](https://in.tradingview.com/chart/?symbol=NSE:HINDOILEXP)<br><sub>📶W9 · W↑1d · ↑CMF0d</sub> | ✓ SAFE | Crude oil natural gas exploration production onshore offshore | ⚡ BULL_ANY_PPV | 94 | 🔄47 | ↑1.026 | ↑1d | SQ·PV | +5.2% | -7.16/-7.29 | +5.20% | 20% |
| [NPST](https://in.tradingview.com/chart/?symbol=NSE:NPST)<br><sub>📶W9 · ↓CMF28d</sub> | ✓ SAFE | UPI payments software and real-time transaction processing platform | ⚡ BULL_ANY_PPV | 94 | 🔄68 | ↑1.020 | ↑1d | SQ·PV | +4.0% | -29.74/-34.98 | +3.95% | 10% 🟨 |
| [GIPCL](https://in.tradingview.com/chart/?symbol=NSE:GIPCL)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF29d</sub> | ✓ SAFE | Thermal coal power generation 1184MW capacity Gujarat utilities | ⚡ BULL_ANY_PPV | 94 | 🔄46 | ↑1.022 | ↑1d | SQ·PV | +4.3% | -9.95/-10.16 | +4.31% | 20% |
| [POLYMED](https://in.tradingview.com/chart/?symbol=NSE:POLYMED)<br><sub>📶W9 · W↑41d · RVOL10x · ↑CMF0d</sub> | ✓ SAFE | Plastic medical disposables manufacturer serving hospitals globally | ⚡ BULL_ANY_PPV | 89 | 🔄57 | ↑1.036 | ↑1d | SQ·PV | +4.6% | 39.81/34.06 | +4.64% | 20% |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB)<br><sub>📶W9 · 🚀SS · ↓CMF1d</sub> | ✓ SAFE | Macrolide antibiotics bulk drug manufacturer for global pharma markets | ⚡ BULL_ANY_PPV | 89 | 🔄98 | ↑1.032 | ↑1d | SQ·PV | +3.9% | 23.45/18.69 | +3.87% | 20% |
| [RPEL](https://in.tradingview.com/chart/?symbol=NSE:RPEL)<br><sub>📶W9 · ↓CMF7d</sub> | ✓ SAFE | Silica ramming mass and quartz powder for induction furnaces | ⚡ BULL_ANY_PPV | 89 | 🔄95 | ↑1.032 | ↑1d | SQ·PV | +4.6% | -0.19/-7.78 | +4.56% | 20% |
| [KOVAI](https://in.tradingview.com/chart/?symbol=NSE:KOVAI)<br><sub>📶W9 · 🚀SS · ↓CMF14d</sub> | ⚠ CAUTION | Tertiary care hospital pharmacy medical education Coimbatore healthcare | ⚡ BULL_ANY_PPV | 89 | 🔄50 | ↑1.038 | ↑1d | SQ·PV | +5.5% | 5.75/-8.89 | +5.45% | 20% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>📶W9 · W↑26d · 🚀SS·17x · ↓CMF2d</sub> | ✓ SAFE | Pharmaceutical and surgical product distributor serving hospitals | ⚡ BULL_ANY_PPV | 75 | 🔄64 | ↑1.050 | ↑15d | SQ·PV | +10.5% | 59.62/48.31 | +5.83% | 20% |
| [TASTYBITE](https://in.tradingview.com/chart/?symbol=NSE:TASTYBITE)<br><sub>📶W9 · W↑89d · ↑CMF0d</sub> | ✓ SAFE | Ready-to-eat ethnic vegetarian meals packaged foods export | ⚡ BULL_ANY_PPV | 55 | ↑66 | ↑1.025 | ↑10d | SQ·PV | +7.3% | 62.17/61.15 | +1.39% | 20% |
| [INNOVACAP](https://in.tradingview.com/chart/?symbol=NSE:INNOVACAP)<br><sub>📶W9 · ↓CMF29d</sub> | ⚠ CAUTION | Tablet manufacturing pharmaceuticals India generic drugs | 📈 BULL_ANY_MID | 99 | 🔄69 | ↑1.008 | ↑1d | SQ | +2.3% | -23.06/-26.34 | +2.29% | 20% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>📶W9 · ↓CMF15d</sub> | ✓ SAFE | Refurbished electronics retailer distributor ICT devices consumer segment | 📈 BULL_ANY_MID | 94 | 🔄92 | ↑1.028 | ↑1d | SQ | +5.7% | -32.19/-34.8 | +5.71% | 5% 🟥 |
| [DALBHARAT](https://in.tradingview.com/chart/?symbol=NSE:DALBHARAT)<br><sub>📶W9 · W↑36d · ↑CMF18d</sub> | ✓ SAFE | Cement manufacturer, construction materials, Indian infrastructure demand | 📈 BULL_ANY_MID | 94 | 🔄27 | ↑1.009 | ↑6d | SQ | +2.5% | 32.12/30.63 | +0.96% | 20% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>📶W9 · W↑36d · ↓CMF0d</sub> | ✓ SAFE | Rear axles and shafts for commercial vehicles globally | 📈 BULL_ANY_MID | 91 | 🔄91 | ↑1.020 | ↑4d | SQ | +4.4% | 37.59/37.55 | +2.18% | 20% |
| [COROMANDEL](https://in.tradingview.com/chart/?symbol=NSE:COROMANDEL)<br><sub>📶W9 · W↑46d · ↑CMF16d</sub> | ⚠ CAUTION | Phosphatic fertilizers, crop nutrients, Indian agriculture sector | 📈 BULL_ANY_MID | 90 | 🔄38 | ↑1.011 | ↑10d | SQ | +4.7% | 36.56/36.4 | +1.40% | 20% |
| [AYE](https://in.tradingview.com/chart/?symbol=NSE:AYE)<br><sub>📶W9 · ↑CMF27d</sub> | ✓ SAFE | Micro-enterprise secured lending NBFC working capital loans | 📈 BULL_ANY_MID | 89 | 🔄50 | ↑1.042 | ↑1d | SQ | +4.7% | 4.93/-3.65 | +4.72% | 20% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>📶W9 · W↑36d · ↑CMF8d</sub> | ✓ SAFE | Dredging, marine engineering, ship repair, ports infrastructure | 📈 BULL_ANY_MID | 83 | 🔄97 | ↑1.029 | ↑12d | SQ | +10.9% | 52.21/51.69 | +2.71% | 20% |
| [HNDFDS](https://in.tradingview.com/chart/?symbol=NSE:HNDFDS)<br><sub>📶W9 · W↑96d · 🚀SS · ↑CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 80 | 🔄63 | ↑1.013 | ↑22d | SQ | +6.9% | 43.5/42.21 | +1.63% | 20% |
| [HCG](https://in.tradingview.com/chart/?symbol=NSE:HCG)<br><sub>📶W9 · W↑31d · ↑CMF1d</sub> | ✓ SAFE | Oncology and fertility hospital network across India | 📈 BULL_ANY_MID | 72 | 🔄65 | ↑1.052 | ↑18d | SQ | +10.6% | 48.53/36.03 | +5.89% | 20% |
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM)<br><sub>📶W9 · W↑41d · ↑CMF30d</sub> | ⚠ CAUTION | Branded generics tablets capsules ophthalmology gastroenterology dermatology | 📈 BULL_ANY_MID | 67 | ↑74 | ↑1.011 | ↑3d | SQ | +2.0% | 40.29/38.36 | +0.49% | 20% |
| [AARTIDRUGS](https://in.tradingview.com/chart/?symbol=NSE:AARTIDRUGS)<br><sub>📶W9 · W↑31d · ↑CMF0d</sub> | ✓ SAFE | API manufacturer, pharma intermediates, specialty chemicals producer | 📈 BULL_ANY_MID | 63 | ↑48 | ↑1.019 | ↑2d | SQ | +2.9% | 41.13/34.66 | +1.53% | 20% |
| [SHRIRAMPPS](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMPPS)<br><sub>↓CMF30d</sub> | ✓ SAFE | Residential real estate developer mid-market South India housing | ⚡ BULL_ANY_PPV | 94 | 🔄43 | ↑1.017 | ↑1d | SQ·PV | +2.9% | -31.96/-38.05 | +2.94% | 20% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>🚀SS · ↑CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄90 | ↑1.009 | ↑1d | SQ | +2.7% | -36.34/-42.32 | +2.74% | 20% |
| [GODREJCP](https://in.tradingview.com/chart/?symbol=NSE:GODREJCP)<br><sub>W↑33d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 98 | 🔄36 | ↑1.008 | ↑2d | SQ | +2.1% | 25.85/25.42 | +1.03% | 20% |
| [ELECTHERM](https://in.tradingview.com/chart/?symbol=NSE:ELECTHERM)<br><sub>↓CMF23d</sub> | ✓ SAFE | Industrial heating equipment manufacturer, process heating sector | 📈 BULL_ANY_MID | 80 | 🔄79 | ↑1.007 | ↓27d | SQ | -6.4% | -34.63/-38.05 | +2.62% | 10% 🟨 |
| [HONDAPOWER](https://in.tradingview.com/chart/?symbol=NSE:HONDAPOWER)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↓19 | ↑1.002 | ↑1d | SQ | +0.5% | -30.96/-35.19 | +0.53% | 20% |
| [CESC](https://in.tradingview.com/chart/?symbol=NSE:CESC)<br><sub>🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Power generation and distribution, Eastern India utilities | 📈 BULL_ANY_MID | 68 | ↓33 | ↑1.002 | ↑2d | SQ | +1.3% | -13.41/-13.45 | +0.39% | 20% |
| [FORTIS](https://in.tradingview.com/chart/?symbol=NSE:FORTIS)<br><sub>↓CMF26d · ⚠️TRAP</sub> | ⚠ CAUTION | Multi-specialty hospitals, diagnostics, quaternary healthcare services across India | 📈 BULL_ANY_MID | 58 | ↓42 | ↓1.004 | ↑2d | SQ | +2.7% | -35.27/-46.2 | -1.05% | 20% |
| [ARFIN](https://in.tradingview.com/chart/?symbol=NSE:ARFIN)<br><sub>↓CMF9d · ⚠️TRAP</sub> | ✓ SAFE | Aluminium ferroalloys manufacturing trading steel auto sectors | 📈 BULL_ANY_MID | 58 | ↓84 | ↓0.997 | ↓2d | SQ | +0.2% | -18.0/-22.67 | -1.00% | 20% 🟦 |
| [FLAIR](https://in.tradingview.com/chart/?symbol=NSE:FLAIR)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Ball pen manufacturer for retail consumer stationery market | 📈 BULL_ANY_MID | 51 | ↓5 | ↓0.995 | ↓9d | SQ | -1.3% | -35.34/-36.89 | -0.42% | 20% |
| [TATACOMM](https://in.tradingview.com/chart/?symbol=NSE:TATACOMM)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Global telecom services, voice data internet connectivity provider | 📈 BULL_ANY_MID | 40 | ↓48 | ↓0.988 | ↓38d | SQ | -8.4% | -49.01/-49.54 | -0.90% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:HINDOILEXP,NSE:NPST,NSE:GIPCL,NSE:POLYMED,NSE:INDSWFTLAB,NSE:RPEL,NSE:KOVAI,NSE:ENTERO,NSE:TASTYBITE,NSE:INNOVACAP,NSE:EBGNG,NSE:DALBHARAT,NSE:GNA,NSE:COROMANDEL,NSE:AYE,NSE:KMEW,NSE:HNDFDS,NSE:HCG,NSE:AJANTPHARM,NSE:AARTIDRUGS,NSE:SHRIRAMPPS,NSE:POWERINDIA,NSE:GODREJCP,NSE:ELECTHERM,NSE:HONDAPOWER,NSE:CESC,NSE:FORTIS,NSE:ARFIN,NSE:FLAIR,NSE:TATACOMM
```

---

### 🔥 MAJOR — PPV confirmed (11)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PIXTRANS](https://in.tradingview.com/chart/?symbol=NSE:PIXTRANS)<br><sub>📶W9 · W↑1d · 🚀SS·75x · ↑CMF8d</sub> | ✓ SAFE | V-belts and power transmission components for industrial machinery | ⚡ BULL_ANY_PPV | 49 | 🔄83 | ↑1.122 | ↑1d | PV | +15.7% | -8.71/-24.87 | +15.68% | 20% |
| [MOL](https://in.tradingview.com/chart/?symbol=NSE:MOL)<br><sub>📶W9 · W↑16d · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Chemical manufacturer: pigments, agrochemicals, crop nutrition | ⚡ BULL_ANY_PPV | 49 | 🔄30 | ↑1.075 | ↑1d | PV | +11.0% | 17.78/16.56 | +10.97% | 20% |
| [POLYPLEX](https://in.tradingview.com/chart/?symbol=NSE:POLYPLEX)<br><sub>📶W9 · W↑41d · ↑CMF14d</sub> | ✓ SAFE | BOPET polyester films flexible packaging industrial applications | ⚡ BULL_ANY_PPV | 45 | 🔄78 | ↑1.049 | ↑5d | PV | +7.8% | 48.77/41.78 | +5.72% | 20% |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>📶W9 · W↑31d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE | Sugar manufacturing, distillery, power cogeneration for domestic consumption | ⚡ BULL_ANY_PPV | 14 | ↑82 | ↑1.040 | ↑6d | PV | +11.8% | 54.24/52.78 | +3.44% | 20% |
| [UNIVCABLES](https://in.tradingview.com/chart/?symbol=NSE:UNIVCABLES)<br><sub>📶W9 · W↑11d · 🚀SS·14x · ★ · ↑CMF12d</sub> | ✓ SAFE | Electrical cables and power solutions manufacturer for infrastructure | ⚡ BULL_ANY_PPV | 4 | ↑98 | ↑1.185 | ↑16d | PV | +45.1% | 67.18/62.4 | +20.00% | 20% |
| [KAPSTON](https://in.tradingview.com/chart/?symbol=NSE:KAPSTON)<br><sub>📶W9 · W↑36d · 🚀SS · ★ · ↑CMF21d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 0 | ↑99 | ↑1.106 | ↑23d | PV | +59.7% | 76.9/75.55 | +7.63% | 20% |
| [JASH](https://in.tradingview.com/chart/?symbol=NSE:JASH)<br><sub>↓CMF1d</sub> | ✓ SAFE | Pumps gates valves water wastewater infrastructure equipment manufacturer | ⚡ BULL_ANY_PPV | 59 | 🔄70 | ↑1.010 | ↑1d | PV | +1.7% | -26.93/-31.69 | +1.68% | 20% |
| [JUBLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:JUBLPHARMA)<br><sub>↑CMF1d</sub> | ⚠ CAUTION | Radiopharmaceuticals, immunotherapy, contract pharma manufacturing globally | ⚡ BULL_ANY_PPV | 54 | 🔄25 | ↑1.016 | ↑1d | PV | +3.3% | -33.16/-36.37 | +3.29% | 20% |
| [VESUVIUS](https://in.tradingview.com/chart/?symbol=NSE:VESUVIUS)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Refractory ceramics for steel foundry molten metal flows | ⚡ BULL_ANY_PPV | 54 | 🔄25 | ↑1.022 | ↑1d | PV | +3.1% | -32.2/-39.27 | +3.10% | 20% |
| [EPACK](https://in.tradingview.com/chart/?symbol=NSE:EPACK)<br><sub>↓CMF2d</sub> | ✓ SAFE | Room air conditioner ODM manufacturer for Indian consumer market | ⚡ BULL_ANY_PPV | 10 | ↓11 | ↑1.002 | ↓22d | PV | +0.5% | -31.44/-31.78 | +0.78% | 20% |
| [VENUSPIPES](https://in.tradingview.com/chart/?symbol=NSE:VENUSPIPES)<br><sub>↓CMF15d</sub> | ✓ SAFE | Stainless steel pipes tubes manufacturing chemicals pharmaceuticals | ⚡ BULL_ANY_PPV | 5 | ↓78 | ↑0.992 | ↓42d | PV | +19.9% | -38.54/-40.2 | +0.97% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:PIXTRANS,NSE:MOL,NSE:POLYPLEX,NSE:BALRAMCHIN,NSE:UNIVCABLES,NSE:KAPSTON,NSE:JASH,NSE:JUBLPHARMA,NSE:VESUVIUS,NSE:EPACK,NSE:VENUSPIPES
```

### 🟢 OVERSOLD — reversal from −53/−60 (5)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [JARO](https://in.tradingview.com/chart/?symbol=NSE:JARO)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Online higher education platform, executive training, career advancement | 🟢 BULL_OVERSOLD | 5 | ↓50 | ↑0.984 | ↓21d | — | -12.1% | -58.8/-60.32 | -0.31% | 20% |
| [THERMAX](https://in.tradingview.com/chart/?symbol=NSE:THERMAX)<br><sub>↑CMF6d · ⚠️TRAP</sub> | ✓ SAFE | Boilers, chillers, power plants, pollution control equipment | 🟡 BULL_OS_L2 | 10 | ↓62 | ↑0.972 | ↓15d | — | -14.0% | -55.3/-56.09 | -0.19% | 20% |
| [SERVOTECH](https://in.tradingview.com/chart/?symbol=NSE:SERVOTECH)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | EV chargers, solar products, power electronics manufacturer | 🟡 BULL_OS_L2 | 8 | ↓10 | ↑0.973 | ↓17d | — | -12.2% | -55.24/-55.33 | +0.59% | 20% 🟦 |
| [VBL](https://in.tradingview.com/chart/?symbol=NSE:VBL)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 5 | ↓21 | ↑0.992 | ↓38d | — | -15.2% | -55.06/-56.28 | +1.38% | 20% |
| [NAVNETEDUL](https://in.tradingview.com/chart/?symbol=NSE:NAVNETEDUL)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Educational books stationery publisher state boards students | 🟡 BULL_OS_L2 | 4 | ↓18 | ↓0.987 | ↓16d | — | -9.3% | -50.18/-53.01 | -1.38% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:JARO,NSE:THERMAX,NSE:SERVOTECH,NSE:VBL,NSE:NAVNETEDUL
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (29)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [JKPAPER](https://in.tradingview.com/chart/?symbol=NSE:JKPAPER)<br><sub>📶W9 · W↑21d · ↓CMF13d</sub> | ✓ SAFE | Paper manufacturer: office, coated, packaging boards | 📈 BULL_ANY_MID | 56 | 🔄57 | ↑1.013 | ↑4d | — | +2.6% | 28.99/28.98 | +1.46% | 20% |
| [HSCL](https://in.tradingview.com/chart/?symbol=NSE:HSCL)<br><sub>📶W9 · 🚀SS · ↑CMF16d</sub> | ✓ SAFE | Coal pitch and advanced carbon materials manufacturer | 📈 BULL_ANY_MID | 54 | 🔄91 | ↑1.019 | ↑1d | — | +2.6% | 32.14/29.95 | +2.58% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄83 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [SANATHAN](https://in.tradingview.com/chart/?symbol=NSE:SANATHAN)<br><sub>📶W9 · W↑41d · ↓CMF3d</sub> | ✓ SAFE | Polyester cotton yarn technical textiles manufacturer exporter | 📈 BULL_ANY_MID | 53 | 🔄52 | ↑1.011 | ↑7d | — | +3.8% | 40.13/39.68 | +0.86% | 20% |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>📶W9 · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | Bromine lithium specialty chemicals pharma agrochemicals engineering | 📈 BULL_ANY_MID | 49 | 🔄88 | ↑1.054 | ↑1d | — | +7.4% | -1.51/-7.24 | +7.43% | 20% |
| [SENORES](https://in.tradingview.com/chart/?symbol=NSE:SENORES)<br><sub>📶W9 · ↓CMF9d</sub> | ✓ SAFE | Complex generics pharma targeting affordable specialty therapeutics | 📈 BULL_ANY_MID | 49 | 🔄95 | ↑1.047 | ↑1d | — | +5.9% | -7.8/-15.68 | +5.93% | 20% |
| [CONCORDBIO](https://in.tradingview.com/chart/?symbol=NSE:CONCORDBIO)<br><sub>📶W9 · W↑84d · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Fermentation APIs immunosuppressants oncology biopharma manufacturer | 📈 BULL_ANY_MID | 41 | 🔄56 | ↑1.034 | ↑9d | — | +13.0% | 31.9/30.61 | +3.96% | 20% |
| [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS)<br><sub>📶W9 · W↑16d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Commercial vehicle axles and tractor components manufacturer | 📈 BULL_ANY_MID | 18 | ↑60 | ↑1.021 | ↑7d | — | +7.0% | 31.05/29.52 | +1.63% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 11 | ↑68 | ↓1.011 | ↑9d | — | +5.3% | 52.94/52.13 | +0.00% | 20% |
| [EMCURE](https://in.tradingview.com/chart/?symbol=NSE:EMCURE)<br><sub>📶W9 · W↑11d · ↓CMF9d</sub> | ✓ SAFE | Oral antibiotics and generics for domestic European markets | 📈 BULL_ANY_MID | 9 | ↑82 | ↑1.023 | ↑16d | — | +11.9% | 54.09/51.88 | +0.85% | 20% |
| [LENSKART](https://in.tradingview.com/chart/?symbol=NSE:LENSKART)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Eyewear design manufacturing retail omnichannel direct consumer | 📈 BULL_ANY_MID | 5 | ↑50 | ↑1.030 | ↑30d | — | +15.9% | 64.3/61.91 | +2.24% | 20% |
| [THYROCARE](https://in.tradingview.com/chart/?symbol=NSE:THYROCARE)<br><sub>📶W9 · W↑16d · ★ · ↓CMF11d</sub> | ✓ SAFE | Thyrocare Technologies Ltd

Diagnostic pathology and radiology services for hospitals | 📈 BULL_ANY_MID | 4 | ↑86 | ↑1.046 | ↑16d | — | +19.5% | 55.34/53.79 | +3.12% | 20% |
| [TANLA](https://in.tradingview.com/chart/?symbol=NSE:TANLA)<br><sub>📶W9 · W↑89d · ↓CMF12d</sub> | ✓ SAFE | CPaaS provider SMS voice OTP enterprise messaging | 📈 BULL_ANY_MID | 0 | ↑66 | ↑1.038 | ↑22d | — | +21.2% | 59.52/58.45 | +3.02% | 20% |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>↓CMF16d</sub> | ✓ SAFE | Commodity futures trading exchange platform India | 📈 BULL_ANY_MID | 54 | 🔄73 | ↑1.026 | ↑1d | — | +4.6% | -44.2/-51.23 | +4.60% | 20% |
| [CUB](https://in.tradingview.com/chart/?symbol=NSE:CUB)<br><sub>🚀SS · ↓CMF6d</sub> | ✓ SAFE | Private bank serving SMEs, MSMEs, retail customers, South India | 📈 BULL_ANY_MID | 54 | 🔄14 | ↑1.016 | ↑1d | — | +2.1% | -18.23/-22.01 | +2.08% | 20% |
| [AAVAS](https://in.tradingview.com/chart/?symbol=NSE:AAVAS)<br><sub>🚀SS · ↓CMF13d</sub> | ✓ SAFE | Housing loans for rural semi-urban low income customers | 📈 BULL_ANY_MID | 54 | 🔄32 | ↑1.007 | ↓6d | — | +3.2% | -32.45/-34.27 | +2.37% | 20% |
| [DATAPATTNS](https://in.tradingview.com/chart/?symbol=NSE:DATAPATTNS)<br><sub>🚀SS · ↑CMF13d · ÷DIV</sub> | ✓ SAFE | Defense aerospace electronics systems manufacturing | 📈 BULL_ANY_MID | 29 | ↓88 | ↑1.001 | ↑1d | — | +1.1% | -1.59/-1.69 | +1.12% | 20% |
| [EXPLEOSOL](https://in.tradingview.com/chart/?symbol=NSE:EXPLEOSOL)<br><sub>W↑11d · ↓CMF30d</sub> | ✓ SAFE | Software testing QA services banking financial sector | 📈 BULL_ANY_MID | 18 | ↑17 | ↓1.009 | ↑2d | — | +1.8% | 3.95/1.61 | -0.15% | 20% |
| [KALPATARU](https://in.tradingview.com/chart/?symbol=NSE:KALPATARU)<br><sub>W↑1d · ↓CMF20d · ⚠️TRAP</sub> | ✓ SAFE | Luxury residential real estate developer focused Mumbai MMR | 📈 BULL_ANY_MID | 18 | ↓7 | ↓1.003 | ↑2d | — | +1.5% | -9.04/-10.75 | +0.03% | 20% |
| [INDIAMART](https://in.tradingview.com/chart/?symbol=NSE:INDIAMART)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | B2B marketplace connecting MSMEs suppliers buyers online | 📈 BULL_ANY_MID | 14 | ↓6 | ↑1.001 | ↓16d | — | -6.7% | -43.65/-46.38 | +1.58% | 20% |
| [STAR](https://in.tradingview.com/chart/?symbol=NSE:STAR)<br><sub>↓CMF7d · ⚠️TRAP</sub> | ✓ SAFE | Niche pharmaceutical formulations manufacturer, global markets | 📈 BULL_ANY_MID | 11 | ↓46 | ↓0.986 | ↓9d | — | -4.1% | -48.64/-49.4 | -0.48% | 20% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>↓CMF23d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 10 | ↓62 | ↑0.984 | ↓15d | — | -7.1% | -51.35/-51.43 | -0.24% | 20% |
| [CANFINHOME](https://in.tradingview.com/chart/?symbol=NSE:CANFINHOME)<br><sub>↓CMF19d</sub> | ✓ SAFE | Housing finance for first-time middle-income home buyers | 📈 BULL_ANY_MID | 10 | ↓34 | ↑1.002 | ↓30d | — | -2.0% | -34.22/-36.58 | +1.11% | 20% |
| [UTIAMC](https://in.tradingview.com/chart/?symbol=NSE:UTIAMC)<br><sub>🚀SS · ↓CMF12d</sub> | ✓ SAFE | Mutual fund management, investment schemes, retail investors | 📈 BULL_ANY_MID | 10 | ↓9 | ↑1.001 | ↓29d | — | -2.8% | -28.34/-29.12 | +1.25% | 20% |
| [IVALUE](https://in.tradingview.com/chart/?symbol=NSE:IVALUE)<br><sub>↓CMF30d</sub> | ✓ SAFE | Tech distributor, hybrid-cloud solutions, enterprise digital transformation | 📈 BULL_ANY_MID | 10 | ↓50 | ↑1.002 | ↓40d | — | +19.1% | -23.24/-24.09 | +1.81% | 20% |
| [WAAREERTL](https://in.tradingview.com/chart/?symbol=NSE:WAAREERTL)<br><sub>↓CMF12d</sub> | ✓ SAFE | Solar EPC projects, rooftop installations, utility-scale systems | 📈 BULL_ANY_MID | 9 | ↓22 | ↑0.991 | ↓16d | — | -8.8% | -42.28/-42.93 | +0.29% | 20% |
| [AVANTIFEED](https://in.tradingview.com/chart/?symbol=NSE:AVANTIFEED)<br><sub>↓CMF7d · ⚠️TRAP</sub> | ✓ SAFE | Shrimp feed manufacturing and shrimp export processing | 📈 BULL_ANY_MID | 8 | ↓35 | ↓0.986 | ↓12d | — | -5.8% | -43.78/-44.0 | -0.31% | 20% 🟦 |
| [SOLARA](https://in.tradingview.com/chart/?symbol=NSE:SOLARA)<br><sub>↓CMF30d</sub> | ✓ SAFE | API manufacturer, CRAMS provider, pharma sector | 📈 BULL_ANY_MID | 5 | ↓36 | ↑0.998 | ↓21d | — | -9.6% | -42.82/-44.02 | +2.31% | 20% |
| [SWARAJENG](https://in.tradingview.com/chart/?symbol=NSE:SWARAJENG)<br><sub>🚀SS · ↓CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Diesel engines for tractors, 22-65 HP range | 📈 BULL_ANY_MID | 5 | ↓29 | ↑0.998 | ↓41d | — | -2.7% | -31.5/-32.96 | +0.05% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:JKPAPER,NSE:HSCL,NSE:OFSS,NSE:SANATHAN,NSE:NEOGEN,NSE:SENORES,NSE:CONCORDBIO,NSE:KROSS,NSE:NESTLEIND,NSE:EMCURE,NSE:LENSKART,NSE:THYROCARE,NSE:TANLA,NSE:MCX,NSE:CUB,NSE:AAVAS,NSE:DATAPATTNS,NSE:EXPLEOSOL,NSE:KALPATARU,NSE:INDIAMART,NSE:STAR,NSE:ADANIPORTS,NSE:CANFINHOME,NSE:UTIAMC,NSE:IVALUE,NSE:WAAREERTL,NSE:AVANTIFEED,NSE:SOLARA,NSE:SWARAJENG
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
