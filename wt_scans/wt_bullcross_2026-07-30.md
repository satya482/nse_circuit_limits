> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-07-30
*Generated 2026-07-30 15:43 IST*

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

**Total bull crosses today: 85** · 36 inside active squeeze

```
NSE:STEELCAS,NSE:LTFOODS,NSE:MACPOWER,NSE:SYRMA,NSE:KTKBANK,NSE:DIVISLAB,NSE:LODHA,NSE:NAZARA,NSE:BELRISE,NSE:KDDL,NSE:CARERATING,NSE:SHADOWFAX,NSE:KIRLOSBROS,NSE:TAJGVK,NSE:SHRIRAMFIN,NSE:SHRIPISTON,NSE:DLF,NSE:JSWSTEEL,NSE:APOLLOHOSP,NSE:EMIL,NSE:RGL,NSE:EIHOTEL,NSE:AJAXENGG,NSE:NGLFINE,NSE:JSL,NSE:BRITANNIA,NSE:PACEDIGITK,NSE:VMART,NSE:BOROSCI,NSE:OIL,NSE:BLUESTARCO,NSE:PGEL,NSE:BLUEJET,NSE:RELAXO,NSE:CONCORDBIO,NSE:PAYTM,NSE:GNA,NSE:ULTRACEMCO,NSE:VSSL,NSE:KALYANKJIL,NSE:SONACOMS,NSE:DIXON,NSE:ECLERX,NSE:AMAGI,NSE:ICRA,NSE:TCI,NSE:SHARDAMOTR,NSE:IFCI,NSE:GOCOLORS,NSE:DOLLAR,NSE:FORCEMOT,NSE:GODIGIT,NSE:SALZERELEC,NSE:TATASTEEL,NSE:IRCTC,NSE:AMRUTANJAN,NSE:KEC,NSE:AXISBANK,NSE:RIIL,NSE:HINDALCO,NSE:AMBUJACEM,NSE:GMRP&UI,NSE:GRINFRA,NSE:BANARISUG,NSE:MUTHOOTFIN,NSE:HERITGFOOD,NSE:WONDERLA,NSE:NATIONALUM,NSE:ACC,NSE:IGIL,NSE:CASTROLIND,NSE:MADRASFERT,NSE:FORTIS,NSE:CEATLTD,NSE:ANUP,NSE:BHAGCHEM,NSE:DCAL,NSE:POLYCAB,NSE:TITAGARH,NSE:CEIGALL,NSE:TMPV,NSE:KRBL,NSE:SWARAJENG,NSE:DLINKINDIA,NSE:THOMASCOOK
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (44)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [STEELCAS](https://in.tradingview.com/chart/?symbol=NSE:STEELCAS)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Steel castings manufacturer for heavy industrial equipment OEMs | ⚡ BULL_ANY_PPV | 89 | 🔄87 | ↑1.032 | ↑1d | SQ·PV | +4.1% | 19.43/18.44 | +4.14% | 20% |
| [LTFOODS](https://in.tradingview.com/chart/?symbol=NSE:LTFOODS)<br><sub>📶W9 · W↑4d · RVOL18x · ↑CMF5d</sub> | ✓ SAFE | Specialty rice producer rice-based foods global FMCG | ⚡ BULL_ANY_PPV | 88 | 🔄33 | ↑1.042 | ↑2d | SQ·PV | +7.3% | -16.19/-29.31 | +4.89% | 20% |
| [MACPOWER](https://in.tradingview.com/chart/?symbol=NSE:MACPOWER)<br><sub>📶W9 · W↑29d · ↑CMF1d</sub> | ✓ SAFE | CNC turning centers and lathe machines for metal fabrication | ⚡ BULL_ANY_PPV | 58 | ↑92 | ↑1.083 | ↑2d | SQ·PV | +14.3% | 33.98/20.55 | +5.48% | 20% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>📶W9 · 🚀SS·10x · ↓CMF0d</sub> | ✓ SAFE | Electronics manufacturing design assembly testing services | ⚡ BULL_ANY_PPV | 54 | 🔄95 | ↑1.019 | ↑1d | PV | +2.6% | -15.15/-22.05 | +2.56% | 20% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>📶W9 · W↑4d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE | Private bank, retail deposits, MSME lending, treasury operations | ⚡ BULL_ANY_PPV | 35 | 🔄89 | ↑1.037 | ↑15d | PV | +8.5% | 50.51/45.7 | +4.21% | 20% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>📶W9 · W↑74d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 0 | ↑76 | ↑1.059 | ↑20d | PV | +19.4% | 64.61/59.48 | +5.25% | 20% |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Residential and commercial real estate development, Mumbai Pune Bangalore | ⚡ BULL_ANY_PPV | 0 | ↑84 | ↑1.101 | ↑33d | PV | +51.0% | 56.79/51.26 | +9.37% | 20% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>📶W9 · W↑77d · 🚀SS · ↓CMF19d</sub> | ✓ SAFE | Gaming platform, esports, mobile and console games, India and global | 📈 BULL_ANY_MID | 99 | 🔄60 | ↑1.010 | ↑1d | SQ | +1.4% | 15.54/11.87 | +1.45% | 20% |
| [BELRISE](https://in.tradingview.com/chart/?symbol=NSE:BELRISE)<br><sub>📶W9 · ↓CMF17d</sub> | ✓ SAFE | Auto parts maker: chassis, polymers, suspension systems | 📈 BULL_ANY_MID | 99 | 🔄89 | ↑1.006 | ↑1d | SQ | +1.0% | -15.5/-17.62 | +1.01% | 20% |
| [KDDL](https://in.tradingview.com/chart/?symbol=NSE:KDDL)<br><sub>📶W9 · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | Watch dials, hands, precision components manufacturer, luxury retail | 📈 BULL_ANY_MID | 99 | 🔄86 | ↑1.012 | ↑1d | SQ | +2.1% | -7.31/-8.95 | +2.14% | 20% |
| [CARERATING](https://in.tradingview.com/chart/?symbol=NSE:CARERATING)<br><sub>📶W9 · W↑9d · 🚀SS · ↓CMF3d</sub> | ⚠ CAUTION | Credit ratings for corporate debt and bonds | 📈 BULL_ANY_MID | 98 | 🔄53 | ↑1.012 | ↑2d | SQ | +2.1% | 36.64/33.83 | +1.07% | 20% |
| [SHADOWFAX](https://in.tradingview.com/chart/?symbol=NSE:SHADOWFAX)<br><sub>📶W9 · ↑CMF4d</sub> | ✓ SAFE | Fast delivery logistics platform for e-commerce merchants | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.020 | ↑1d | SQ | +2.0% | -15.39/-19.69 | +2.00% | 20% |
| [KIRLOSBROS](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSBROS)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Pumps and fluid management systems for infrastructure and agriculture | 📈 BULL_ANY_MID | 85 | 🔄58 | ↑1.003 | ↓15d | SQ | -1.8% | -22.64/-25.1 | +1.00% | 20% |
| [TAJGVK](https://in.tradingview.com/chart/?symbol=NSE:TAJGVK)<br><sub>📶W9 · W↑49d · ↑CMF17d</sub> | ✓ SAFE | Luxury hotel operations and management, premium hospitality sector | 📈 BULL_ANY_MID | 80 | 🔄44 | ↑1.003 | ↑22d | SQ | +8.7% | 36.81/35.61 | +0.25% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑32d · ↓CMF18d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 67 | ↓81 | ↑1.007 | ↑3d | SQ | +3.9% | 10.9/8.21 | +0.29% | 20% |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON)<br><sub>📶W9 · W↑34d · ↑CMF30d</sub> | ✓ SAFE | Pistons, rings, pins, valves for automobile engines | 📈 BULL_ANY_MID | 67 | ↑93 | ↑1.015 | ↑3d | SQ | +2.3% | 39.77/37.38 | +0.56% | 20% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>📶W9 · W↑79d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 63 | ↑46 | ↑1.018 | ↑2d | SQ | +3.0% | 15.62/11.03 | +1.09% | 20% |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 62 | ↑60 | ↑1.020 | ↑3d | SQ | +2.9% | 12.63/4.94 | +2.41% | 20% |
| [APOLLOHOSP](https://in.tradingview.com/chart/?symbol=NSE:APOLLOHOSP)<br><sub>📶W9 · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↓74 | ↓1.004 | ↑2d | SQ | +0.7% | 38.14/36.38 | +0.01% | 20% |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL)<br><sub>📶W9 · W↑29d · ↓CMF2d</sub> | ✓ SAFE | Consumer electronics retail chain South India operations | 📈 BULL_ANY_MID | 58 | ↓62 | ↓1.001 | ↓2d | SQ | +2.3% | 4.64/1.93 | -1.96% | 20% |
| [RGL](https://in.tradingview.com/chart/?symbol=NSE:RGL)<br><sub>📶W9 · W↑34d · ↓CMF0d</sub> | ✓ SAFE | Global recruitment and staffing services provider | 📈 BULL_ANY_MID | 58 | ↑61 | ↓1.005 | ↑2d | SQ | +2.8% | 14.92/10.89 | -1.25% | 20% |
| [EIHOTEL](https://in.tradingview.com/chart/?symbol=NSE:EIHOTEL)<br><sub>📶W9 · W↑34d · ↓CMF15d</sub> | ⚠ CAUTION | Luxury hotels resorts Oberoi Trident brands hospitality | 📈 BULL_ANY_MID | 58 | ↑37 | ↓1.003 | ↑2d | SQ | +2.0% | 8.85/7.09 | -1.10% | 20% |
| [AJAXENGG](https://in.tradingview.com/chart/?symbol=NSE:AJAXENGG)<br><sub>📶W9 · W↑14d · ↑CMF13d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | 🔄51 | ↑1.008 | ↑2d | — | +1.8% | -0.19/-1.16 | +0.80% | 20% |
| [NGLFINE](https://in.tradingview.com/chart/?symbol=NSE:NGLFINE)<br><sub>📶W9 · ↑CMF6d</sub> | ✓ SAFE | Veterinary APIs, intermediates, animal health pharmaceuticals manufacturer | 📈 BULL_ANY_MID | 57 | ↑98 | ↑1.021 | ↑8d | SQ | +9.0% | 40.9/36.66 | +0.88% | 20% |
| [JSL](https://in.tradingview.com/chart/?symbol=NSE:JSL)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF1d</sub> | ⚠ CAUTION | Stainless steel flat products for automotive construction railways | 📈 BULL_ANY_MID | 56 | 🔄38 | ↑1.013 | ↑4d | — | +3.3% | 34.88/33.3 | +1.27% | 20% |
| [BRITANNIA](https://in.tradingview.com/chart/?symbol=NSE:BRITANNIA)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF22d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 54 | ↑33 | ↑1.019 | ↑11d | SQ | +4.7% | 45.79/38.66 | +0.99% | 20% |
| [PACEDIGITK](https://in.tradingview.com/chart/?symbol=NSE:PACEDIGITK)<br><sub>📶W9 · ↓CMF6d</sub> | ✓ SAFE | Power systems, fiber networks, telecom and energy infrastructure | 📈 BULL_ANY_MID | 54 | 🔄50 | ↑1.015 | ↑1d | — | +2.9% | -22.54/-23.33 | +2.93% | 20% |
| [VMART](https://in.tradingview.com/chart/?symbol=NSE:VMART)<br><sub>📶W9 · ↓CMF11d</sub> | ✓ SAFE | Value fashion retail Tier II-IV cities apparel footwear | 📈 BULL_ANY_MID | 54 | 🔄66 | ↑1.021 | ↑1d | — | +2.2% | -24.08/-26.78 | +2.17% | 20% |
| [BOROSCI](https://in.tradingview.com/chart/?symbol=NSE:BOROSCI)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | Laboratory glassware manufacturer for pharma QC and biotech | 📈 BULL_ANY_MID | 51 | ↓78 | ↓0.994 | ↓9d | SQ | -3.3% | -25.93/-27.59 | -1.10% | 20% |
| [OIL](https://in.tradingview.com/chart/?symbol=NSE:OIL)<br><sub>📶W9 · W↑9d · 🚀SS · ↑CMF16d</sub> | ✓ SAFE | Crude oil and natural gas exploration production transportation | 📈 BULL_ANY_MID | 36 | 🔄44 | ↑1.023 | ↑19d | — | +8.2% | 43.68/42.57 | +2.01% | 20% |
| [BLUESTARCO](https://in.tradingview.com/chart/?symbol=NSE:BLUESTARCO)<br><sub>📶W9 · W↑14d · ↑CMF14d</sub> | ⚠ CAUTION | AC manufacturing, refrigeration, MEP solutions for commercial buildings | 📈 BULL_ANY_MID | 28 | ↑31 | ↑1.013 | ↑2d | — | +2.8% | 1.22/-2.61 | +0.63% | 20% |
| [PGEL](https://in.tradingview.com/chart/?symbol=NSE:PGEL)<br><sub>📶W9 · W↑34d · ↑CMF30d</sub> | ✓ SAFE | EMS plastic moulding consumer electronics appliances manufacturing | 📈 BULL_ANY_MID | 18 | ↑56 | ↓1.030 | ↑2d | — | +4.7% | 31.59/26.34 | +0.09% | 20% |
| [BLUEJET](https://in.tradingview.com/chart/?symbol=NSE:BLUEJET)<br><sub>📶W9 · W↑103d · 🚀SS · ↑CMF24d</sub> | ✓ SAFE | Specialty pharma CDMO, niche chemistry, healthcare ingredients manufacturing | 📈 BULL_ANY_MID | 18 | ↑68 | ↑1.041 | ↑2d | — | +7.1% | 33.77/25.42 | +1.61% | 20% |
| [RELAXO](https://in.tradingview.com/chart/?symbol=NSE:RELAXO)<br><sub>📶W9 · W↑82d · ↑CMF30d</sub> | ✓ SAFE | Mass-market slippers sandals shoes footwear manufacturer | 📈 BULL_ANY_MID | 18 | ↑67 | ↓1.012 | ↑2d | — | +4.1% | 19.79/17.28 | -0.23% | 20% |
| [CONCORDBIO](https://in.tradingview.com/chart/?symbol=NSE:CONCORDBIO)<br><sub>📶W9 · W↑77d · ↓CMF17d</sub> | ✓ SAFE | Fermentation APIs immunosuppressants oncology contract manufacturer | 📈 BULL_ANY_MID | 18 | ↑45 | ↓1.024 | ↑2d | — | +5.9% | -0.96/-9.15 | -0.03% | 20% |
| [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM)<br><sub>📶W9 · W↑29d · ↑CMF22d</sub> | ✓ SAFE | Digital payments, fintech, consumer merchants | 📈 BULL_ANY_MID | 17 | ↑73 | ↓1.018 | ↑3d | — | +3.3% | 31.28/28.54 | +0.19% | 20% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>📶W9 · W↑29d · ↑CMF10d</sub> | ✓ SAFE | Rear axles and drive shafts for commercial vehicles globally | 📈 BULL_ANY_MID | 16 | ↑92 | ↓1.022 | ↑4d | — | +4.7% | 36.66/34.1 | -0.25% | 20% |
| [ULTRACEMCO](https://in.tradingview.com/chart/?symbol=NSE:ULTRACEMCO)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 15 | ↑42 | ↑1.010 | ↑15d | — | +5.6% | 51.42/48.64 | +0.28% | 20% |
| [VSSL](https://in.tradingview.com/chart/?symbol=NSE:VSSL)<br><sub>📶W9 · W↑14d · ↓CMF6d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↑64 | ↓1.005 | ↑15d | — | +11.2% | 31.06/30.75 | -1.98% | 20% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>📶W9 · W↑34d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Gold jewellery retail across India and Middle East markets | 📈 BULL_ANY_MID | 4 | ↑90 | ↓1.084 | ↑16d | — | +69.6% | 63.23/61.76 | +0.95% | 20% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>📶W9 · W↑29d · ↑CMF20d</sub> | ✓ SAFE | Differential assemblies and gears for electric vehicles | 📈 BULL_ANY_MID | 0 | ↑92 | ↑1.061 | ↑33d | — | +28.1% | 67.05/66.57 | +6.00% | 20% |
| [DIXON](https://in.tradingview.com/chart/?symbol=NSE:DIXON)<br><sub>📶W9 · W↑94d · ↑CMF10d</sub> | ✓ SAFE | Consumer electronics contract manufacturing for global brands | 📈 BULL_ANY_MID | 0 | ↑69 | ↓1.024 | ↑21d | — | +19.9% | 49.78/46.48 | +0.44% | 20% |
| [ECLERX](https://in.tradingview.com/chart/?symbol=NSE:ECLERX)<br><sub>📶W9 · W↑24d · ↑CMF19d</sub> | ✓ SAFE | Legal document processing and financial analytics for global enterprises | 📈 BULL_ANY_MID | 0 | ↑57 | ↓1.025 | ↑21d | — | +43.4% | 52.0/51.33 | -2.10% | 20% |
| [AMAGI](https://in.tradingview.com/chart/?symbol=NSE:AMAGI)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Cloud TV platform for content distribution and monetization | 📈 BULL_ANY_MID | 0 | ↑50 | ↑1.059 | ↑36d | — | +63.1% | 68.27/66.52 | +1.54% | 20% |

```
NSE:STEELCAS,NSE:LTFOODS,NSE:MACPOWER,NSE:SYRMA,NSE:KTKBANK,NSE:DIVISLAB,NSE:LODHA,NSE:NAZARA,NSE:BELRISE,NSE:KDDL,NSE:CARERATING,NSE:SHADOWFAX,NSE:KIRLOSBROS,NSE:TAJGVK,NSE:SHRIRAMFIN,NSE:SHRIPISTON,NSE:DLF,NSE:JSWSTEEL,NSE:APOLLOHOSP,NSE:EMIL,NSE:RGL,NSE:EIHOTEL,NSE:AJAXENGG,NSE:NGLFINE,NSE:JSL,NSE:BRITANNIA,NSE:PACEDIGITK,NSE:VMART,NSE:BOROSCI,NSE:OIL,NSE:BLUESTARCO,NSE:PGEL,NSE:BLUEJET,NSE:RELAXO,NSE:CONCORDBIO,NSE:PAYTM,NSE:GNA,NSE:ULTRACEMCO,NSE:VSSL,NSE:KALYANKJIL,NSE:SONACOMS,NSE:DIXON,NSE:ECLERX,NSE:AMAGI
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (59)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [STEELCAS](https://in.tradingview.com/chart/?symbol=NSE:STEELCAS)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Steel castings manufacturer for heavy industrial equipment OEMs | ⚡ BULL_ANY_PPV | 89 | 🔄87 | ↑1.032 | ↑1d | SQ·PV | +4.1% | 19.43/18.44 | +4.14% | 20% |
| [LTFOODS](https://in.tradingview.com/chart/?symbol=NSE:LTFOODS)<br><sub>📶W9 · W↑4d · RVOL18x · ↑CMF5d</sub> | ✓ SAFE | Specialty rice producer rice-based foods global FMCG | ⚡ BULL_ANY_PPV | 88 | 🔄33 | ↑1.042 | ↑2d | SQ·PV | +7.3% | -16.19/-29.31 | +4.89% | 20% |
| [MACPOWER](https://in.tradingview.com/chart/?symbol=NSE:MACPOWER)<br><sub>📶W9 · W↑29d · ↑CMF1d</sub> | ✓ SAFE | CNC turning centers and lathe machines for metal fabrication | ⚡ BULL_ANY_PPV | 58 | ↑92 | ↑1.083 | ↑2d | SQ·PV | +14.3% | 33.98/20.55 | +5.48% | 20% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>📶W9 · 🚀SS·10x · ↓CMF0d</sub> | ✓ SAFE | Electronics manufacturing design assembly testing services | ⚡ BULL_ANY_PPV | 54 | 🔄95 | ↑1.019 | ↑1d | PV | +2.6% | -15.15/-22.05 | +2.56% | 20% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>📶W9 · W↑4d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE | Private bank, retail deposits, MSME lending, treasury operations | ⚡ BULL_ANY_PPV | 35 | 🔄89 | ↑1.037 | ↑15d | PV | +8.5% | 50.51/45.7 | +4.21% | 20% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>📶W9 · W↑74d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 0 | ↑76 | ↑1.059 | ↑20d | PV | +19.4% | 64.61/59.48 | +5.25% | 20% |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Residential and commercial real estate development, Mumbai Pune Bangalore | ⚡ BULL_ANY_PPV | 0 | ↑84 | ↑1.101 | ↑33d | PV | +51.0% | 56.79/51.26 | +9.37% | 20% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>📶W9 · W↑77d · 🚀SS · ↓CMF19d</sub> | ✓ SAFE | Gaming platform, esports, mobile and console games, India and global | 📈 BULL_ANY_MID | 99 | 🔄60 | ↑1.010 | ↑1d | SQ | +1.4% | 15.54/11.87 | +1.45% | 20% |
| [BELRISE](https://in.tradingview.com/chart/?symbol=NSE:BELRISE)<br><sub>📶W9 · ↓CMF17d</sub> | ✓ SAFE | Auto parts maker: chassis, polymers, suspension systems | 📈 BULL_ANY_MID | 99 | 🔄89 | ↑1.006 | ↑1d | SQ | +1.0% | -15.5/-17.62 | +1.01% | 20% |
| [KDDL](https://in.tradingview.com/chart/?symbol=NSE:KDDL)<br><sub>📶W9 · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | Watch dials, hands, precision components manufacturer, luxury retail | 📈 BULL_ANY_MID | 99 | 🔄86 | ↑1.012 | ↑1d | SQ | +2.1% | -7.31/-8.95 | +2.14% | 20% |
| [CARERATING](https://in.tradingview.com/chart/?symbol=NSE:CARERATING)<br><sub>📶W9 · W↑9d · 🚀SS · ↓CMF3d</sub> | ⚠ CAUTION | Credit ratings for corporate debt and bonds | 📈 BULL_ANY_MID | 98 | 🔄53 | ↑1.012 | ↑2d | SQ | +2.1% | 36.64/33.83 | +1.07% | 20% |
| [SHADOWFAX](https://in.tradingview.com/chart/?symbol=NSE:SHADOWFAX)<br><sub>📶W9 · ↑CMF4d</sub> | ✓ SAFE | Fast delivery logistics platform for e-commerce merchants | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.020 | ↑1d | SQ | +2.0% | -15.39/-19.69 | +2.00% | 20% |
| [KIRLOSBROS](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSBROS)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Pumps and fluid management systems for infrastructure and agriculture | 📈 BULL_ANY_MID | 85 | 🔄58 | ↑1.003 | ↓15d | SQ | -1.8% | -22.64/-25.1 | +1.00% | 20% |
| [TAJGVK](https://in.tradingview.com/chart/?symbol=NSE:TAJGVK)<br><sub>📶W9 · W↑49d · ↑CMF17d</sub> | ✓ SAFE | Luxury hotel operations and management, premium hospitality sector | 📈 BULL_ANY_MID | 80 | 🔄44 | ↑1.003 | ↑22d | SQ | +8.7% | 36.81/35.61 | +0.25% | 20% |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON)<br><sub>📶W9 · W↑34d · ↑CMF30d</sub> | ✓ SAFE | Pistons, rings, pins, valves for automobile engines | 📈 BULL_ANY_MID | 67 | ↑93 | ↑1.015 | ↑3d | SQ | +2.3% | 39.77/37.38 | +0.56% | 20% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>📶W9 · W↑79d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 63 | ↑46 | ↑1.018 | ↑2d | SQ | +3.0% | 15.62/11.03 | +1.09% | 20% |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 62 | ↑60 | ↑1.020 | ↑3d | SQ | +2.9% | 12.63/4.94 | +2.41% | 20% |
| [RGL](https://in.tradingview.com/chart/?symbol=NSE:RGL)<br><sub>📶W9 · W↑34d · ↓CMF0d</sub> | ✓ SAFE | Global recruitment and staffing services provider | 📈 BULL_ANY_MID | 58 | ↑61 | ↓1.005 | ↑2d | SQ | +2.8% | 14.92/10.89 | -1.25% | 20% |
| [EIHOTEL](https://in.tradingview.com/chart/?symbol=NSE:EIHOTEL)<br><sub>📶W9 · W↑34d · ↓CMF15d</sub> | ⚠ CAUTION | Luxury hotels resorts Oberoi Trident brands hospitality | 📈 BULL_ANY_MID | 58 | ↑37 | ↓1.003 | ↑2d | SQ | +2.0% | 8.85/7.09 | -1.10% | 20% |
| [AJAXENGG](https://in.tradingview.com/chart/?symbol=NSE:AJAXENGG)<br><sub>📶W9 · W↑14d · ↑CMF13d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | 🔄51 | ↑1.008 | ↑2d | — | +1.8% | -0.19/-1.16 | +0.80% | 20% |
| [NGLFINE](https://in.tradingview.com/chart/?symbol=NSE:NGLFINE)<br><sub>📶W9 · ↑CMF6d</sub> | ✓ SAFE | Veterinary APIs, intermediates, animal health pharmaceuticals manufacturer | 📈 BULL_ANY_MID | 57 | ↑98 | ↑1.021 | ↑8d | SQ | +9.0% | 40.9/36.66 | +0.88% | 20% |
| [JSL](https://in.tradingview.com/chart/?symbol=NSE:JSL)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF1d</sub> | ⚠ CAUTION | Stainless steel flat products for automotive construction railways | 📈 BULL_ANY_MID | 56 | 🔄38 | ↑1.013 | ↑4d | — | +3.3% | 34.88/33.3 | +1.27% | 20% |
| [BRITANNIA](https://in.tradingview.com/chart/?symbol=NSE:BRITANNIA)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF22d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 54 | ↑33 | ↑1.019 | ↑11d | SQ | +4.7% | 45.79/38.66 | +0.99% | 20% |
| [PACEDIGITK](https://in.tradingview.com/chart/?symbol=NSE:PACEDIGITK)<br><sub>📶W9 · ↓CMF6d</sub> | ✓ SAFE | Power systems, fiber networks, telecom and energy infrastructure | 📈 BULL_ANY_MID | 54 | 🔄50 | ↑1.015 | ↑1d | — | +2.9% | -22.54/-23.33 | +2.93% | 20% |
| [VMART](https://in.tradingview.com/chart/?symbol=NSE:VMART)<br><sub>📶W9 · ↓CMF11d</sub> | ✓ SAFE | Value fashion retail Tier II-IV cities apparel footwear | 📈 BULL_ANY_MID | 54 | 🔄66 | ↑1.021 | ↑1d | — | +2.2% | -24.08/-26.78 | +2.17% | 20% |
| [OIL](https://in.tradingview.com/chart/?symbol=NSE:OIL)<br><sub>📶W9 · W↑9d · 🚀SS · ↑CMF16d</sub> | ✓ SAFE | Crude oil and natural gas exploration production transportation | 📈 BULL_ANY_MID | 36 | 🔄44 | ↑1.023 | ↑19d | — | +8.2% | 43.68/42.57 | +2.01% | 20% |
| [BLUESTARCO](https://in.tradingview.com/chart/?symbol=NSE:BLUESTARCO)<br><sub>📶W9 · W↑14d · ↑CMF14d</sub> | ⚠ CAUTION | AC manufacturing, refrigeration, MEP solutions for commercial buildings | 📈 BULL_ANY_MID | 28 | ↑31 | ↑1.013 | ↑2d | — | +2.8% | 1.22/-2.61 | +0.63% | 20% |
| [PGEL](https://in.tradingview.com/chart/?symbol=NSE:PGEL)<br><sub>📶W9 · W↑34d · ↑CMF30d</sub> | ✓ SAFE | EMS plastic moulding consumer electronics appliances manufacturing | 📈 BULL_ANY_MID | 18 | ↑56 | ↓1.030 | ↑2d | — | +4.7% | 31.59/26.34 | +0.09% | 20% |
| [BLUEJET](https://in.tradingview.com/chart/?symbol=NSE:BLUEJET)<br><sub>📶W9 · W↑103d · 🚀SS · ↑CMF24d</sub> | ✓ SAFE | Specialty pharma CDMO, niche chemistry, healthcare ingredients manufacturing | 📈 BULL_ANY_MID | 18 | ↑68 | ↑1.041 | ↑2d | — | +7.1% | 33.77/25.42 | +1.61% | 20% |
| [RELAXO](https://in.tradingview.com/chart/?symbol=NSE:RELAXO)<br><sub>📶W9 · W↑82d · ↑CMF30d</sub> | ✓ SAFE | Mass-market slippers sandals shoes footwear manufacturer | 📈 BULL_ANY_MID | 18 | ↑67 | ↓1.012 | ↑2d | — | +4.1% | 19.79/17.28 | -0.23% | 20% |
| [CONCORDBIO](https://in.tradingview.com/chart/?symbol=NSE:CONCORDBIO)<br><sub>📶W9 · W↑77d · ↓CMF17d</sub> | ✓ SAFE | Fermentation APIs immunosuppressants oncology contract manufacturer | 📈 BULL_ANY_MID | 18 | ↑45 | ↓1.024 | ↑2d | — | +5.9% | -0.96/-9.15 | -0.03% | 20% |
| [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM)<br><sub>📶W9 · W↑29d · ↑CMF22d</sub> | ✓ SAFE | Digital payments, fintech, consumer merchants | 📈 BULL_ANY_MID | 17 | ↑73 | ↓1.018 | ↑3d | — | +3.3% | 31.28/28.54 | +0.19% | 20% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>📶W9 · W↑29d · ↑CMF10d</sub> | ✓ SAFE | Rear axles and drive shafts for commercial vehicles globally | 📈 BULL_ANY_MID | 16 | ↑92 | ↓1.022 | ↑4d | — | +4.7% | 36.66/34.1 | -0.25% | 20% |
| [ULTRACEMCO](https://in.tradingview.com/chart/?symbol=NSE:ULTRACEMCO)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 15 | ↑42 | ↑1.010 | ↑15d | — | +5.6% | 51.42/48.64 | +0.28% | 20% |
| [VSSL](https://in.tradingview.com/chart/?symbol=NSE:VSSL)<br><sub>📶W9 · W↑14d · ↓CMF6d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↑64 | ↓1.005 | ↑15d | — | +11.2% | 31.06/30.75 | -1.98% | 20% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>📶W9 · W↑34d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Gold jewellery retail across India and Middle East markets | 📈 BULL_ANY_MID | 4 | ↑90 | ↓1.084 | ↑16d | — | +69.6% | 63.23/61.76 | +0.95% | 20% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>📶W9 · W↑29d · ↑CMF20d</sub> | ✓ SAFE | Differential assemblies and gears for electric vehicles | 📈 BULL_ANY_MID | 0 | ↑92 | ↑1.061 | ↑33d | — | +28.1% | 67.05/66.57 | +6.00% | 20% |
| [DIXON](https://in.tradingview.com/chart/?symbol=NSE:DIXON)<br><sub>📶W9 · W↑94d · ↑CMF10d</sub> | ✓ SAFE | Consumer electronics contract manufacturing for global brands | 📈 BULL_ANY_MID | 0 | ↑69 | ↓1.024 | ↑21d | — | +19.9% | 49.78/46.48 | +0.44% | 20% |
| [ECLERX](https://in.tradingview.com/chart/?symbol=NSE:ECLERX)<br><sub>📶W9 · W↑24d · ↑CMF19d</sub> | ✓ SAFE | Legal document processing and financial analytics for global enterprises | 📈 BULL_ANY_MID | 0 | ↑57 | ↓1.025 | ↑21d | — | +43.4% | 52.0/51.33 | -2.10% | 20% |
| [AMAGI](https://in.tradingview.com/chart/?symbol=NSE:AMAGI)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Cloud TV platform for content distribution and monetization | 📈 BULL_ANY_MID | 0 | ↑50 | ↑1.059 | ↑36d | — | +63.1% | 68.27/66.52 | +1.54% | 20% |
| [ICRA](https://in.tradingview.com/chart/?symbol=NSE:ICRA)<br><sub>🚀SS · ↓CMF30d · 🔥PHX</sub> | ✓ SAFE | Credit ratings for bonds and debt securities | 🔥 BULL_OS_PPV | 40 | 🔄11 | ↑1.000 | ↓15d | PV | -5.2% | -66.83/-69.83 | +3.09% | 20% |
| [TCI](https://in.tradingview.com/chart/?symbol=NSE:TCI)<br><sub>↓CMF0d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄21 | ↑1.005 | ↑1d | SQ·PV | +1.5% | -36.1/-39.96 | +1.54% | 20% |
| [SHARDAMOTR](https://in.tradingview.com/chart/?symbol=NSE:SHARDAMOTR)<br><sub>W↑24d · RVOL13x · ↓CMF30d</sub> | ⚠ CAUTION | Emission control and suspension auto components manufacturer | ⚡ BULL_ANY_PPV | 59 | 🔄27 | ↑1.012 | ↑1d | PV | +1.4% | -21.56/-28.6 | +1.42% | 20% |
| [IFCI](https://in.tradingview.com/chart/?symbol=NSE:IFCI)<br><sub>↓CMF21d</sub> | ✓ SAFE | Long-term industrial project financing and infrastructure lending | ⚡ BULL_ANY_PPV | 54 | 🔄82 | ↑1.023 | ↑1d | PV | +3.1% | -42.93/-48.49 | +3.11% | 20% |
| [GOCOLORS](https://in.tradingview.com/chart/?symbol=NSE:GOCOLORS)<br><sub>↓CMF29d</sub> | ✓ SAFE | Women's bottom-wear retail, branded leggings and trousers | ⚡ BULL_ANY_PPV | 54 | 🔄19 | ↑1.030 | ↑1d | PV | +6.2% | -40.39/-42.85 | +6.19% | 20% |
| [DOLLAR](https://in.tradingview.com/chart/?symbol=NSE:DOLLAR)<br><sub>↑CMF4d</sub> | ✓ SAFE | Knitted innerwear and casual apparel manufacturer for mass market | ⚡ BULL_ANY_PPV | 54 | 🔄8 | ↑1.029 | ↑1d | PV | +4.3% | -29.69/-36.15 | +4.31% | 20% |
| [FORCEMOT](https://in.tradingview.com/chart/?symbol=NSE:FORCEMOT)<br><sub>↓CMF30d</sub> | ✓ SAFE | Small commercial vehicles, vans, tractors, automotive components | ⚡ BULL_ANY_PPV | 48 | 🔄40 | ↑1.002 | ↓12d | PV | -0.2% | -44.42/-45.06 | +1.64% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>🚀SS · ↓CMF26d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 99 | 🔄42 | ↑1.010 | ↑1d | SQ | +2.6% | -48.58/-54.51 | +2.56% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄60 | ↑1.012 | ↑1d | SQ | +3.0% | -40.63/-43.65 | +2.95% | 20% |
| [AMBUJACEM](https://in.tradingview.com/chart/?symbol=NSE:AMBUJACEM)<br><sub>W↑27d · ↑CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄13 | ↑1.008 | ↑1d | SQ | +2.0% | 0.82/0.46 | +2.00% | 20% |
| [GMRP&UI](https://in.tradingview.com/chart/?symbol=NSE:GMRP&UI)<br><sub>↓CMF30d</sub> | ✓ SAFE | Power generation, urban infrastructure, road-rail-port development | 📈 BULL_ANY_MID | 99 | 🔄25 | ↑1.013 | ↑1d | SQ | +2.7% | -41.16/-43.51 | +2.74% | 20% |
| [GRINFRA](https://in.tradingview.com/chart/?symbol=NSE:GRINFRA)<br><sub>↓CMF7d</sub> | ⚠ CAUTION | Road EPC contractor, highways and railways infrastructure | 📈 BULL_ANY_MID | 99 | 🔄17 | ↑1.007 | ↑1d | SQ | +0.8% | -38.93/-43.16 | +0.75% | 20% |
| [BANARISUG](https://in.tradingview.com/chart/?symbol=NSE:BANARISUG)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄36 | ↑1.004 | ↑1d | SQ | +0.6% | -10.47/-10.59 | +0.62% | 20% |
| [WONDERLA](https://in.tradingview.com/chart/?symbol=NSE:WONDERLA)<br><sub>↓CMF16d</sub> | ⚠ CAUTION | Theme parks and resort hospitality for leisure tourism | 📈 BULL_ANY_MID | 59 | 🔄18 | ↑1.007 | ↑1d | — | +0.8% | -30.82/-34.46 | +0.82% | 20% |
| [NATIONALUM](https://in.tradingview.com/chart/?symbol=NSE:NATIONALUM)<br><sub>↓CMF3d</sub> | ✓ SAFE | Bauxite mining, alumina refining, primary aluminium production | 📈 BULL_ANY_MID | 58 | 🔄70 | ↑1.010 | ↑2d | — | +3.9% | -25.59/-28.16 | +0.86% | 20% |
| [IGIL](https://in.tradingview.com/chart/?symbol=NSE:IGIL)<br><sub>↑CMF0d</sub> | ✓ SAFE | Diamond gemstone jewelry certification grading laboratory services | 📈 BULL_ANY_MID | 58 | ↑41 | ↓1.010 | ↑2d | SQ | +5.1% | -45.21/-51.23 | -0.45% | 20% |
| [CEATLTD](https://in.tradingview.com/chart/?symbol=NSE:CEATLTD)<br><sub>↓CMF1d</sub> | ✓ SAFE | Tyres for cars trucks two-wheelers buses manufacturing | 📈 BULL_ANY_MID | 40 | 🔄44 | ↑1.002 | ↓23d | — | +2.0% | -17.64/-19.11 | +0.88% | 20% |
| [ANUP](https://in.tradingview.com/chart/?symbol=NSE:ANUP)<br><sub>↓CMF11d</sub> | ⚠ CAUTION | Industrial boilers and pressure vessels manufacturing | 📈 BULL_ANY_MID | 40 | 🔄48 | ↑1.009 | ↓34d | — | +13.3% | -30.48/-30.98 | +3.07% | 20% |
| [BHAGCHEM](https://in.tradingview.com/chart/?symbol=NSE:BHAGCHEM)<br><sub>↓CMF9d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 40 | 🔄59 | ↑1.002 | ↓38d | — | +14.6% | -25.45/-26.44 | +0.77% | 20% |

```
NSE:STEELCAS,NSE:LTFOODS,NSE:MACPOWER,NSE:SYRMA,NSE:KTKBANK,NSE:DIVISLAB,NSE:LODHA,NSE:NAZARA,NSE:BELRISE,NSE:KDDL,NSE:CARERATING,NSE:SHADOWFAX,NSE:KIRLOSBROS,NSE:TAJGVK,NSE:SHRIPISTON,NSE:DLF,NSE:JSWSTEEL,NSE:RGL,NSE:EIHOTEL,NSE:AJAXENGG,NSE:NGLFINE,NSE:JSL,NSE:BRITANNIA,NSE:PACEDIGITK,NSE:VMART,NSE:OIL,NSE:BLUESTARCO,NSE:PGEL,NSE:BLUEJET,NSE:RELAXO,NSE:CONCORDBIO,NSE:PAYTM,NSE:GNA,NSE:ULTRACEMCO,NSE:VSSL,NSE:KALYANKJIL,NSE:SONACOMS,NSE:DIXON,NSE:ECLERX,NSE:AMAGI,NSE:ICRA,NSE:TCI,NSE:SHARDAMOTR,NSE:IFCI,NSE:GOCOLORS,NSE:DOLLAR,NSE:FORCEMOT,NSE:TATASTEEL,NSE:HINDALCO,NSE:AMBUJACEM,NSE:GMRP&UI,NSE:GRINFRA,NSE:BANARISUG,NSE:WONDERLA,NSE:NATIONALUM,NSE:IGIL,NSE:CEATLTD,NSE:ANUP,NSE:BHAGCHEM
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (36)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [STEELCAS](https://in.tradingview.com/chart/?symbol=NSE:STEELCAS)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Steel castings manufacturer for heavy industrial equipment OEMs | ⚡ BULL_ANY_PPV | 89 | 🔄87 | ↑1.032 | ↑1d | SQ·PV | +4.1% | 19.43/18.44 | +4.14% | 20% |
| [LTFOODS](https://in.tradingview.com/chart/?symbol=NSE:LTFOODS)<br><sub>📶W9 · W↑4d · RVOL18x · ↑CMF5d</sub> | ✓ SAFE | Specialty rice producer rice-based foods global FMCG | ⚡ BULL_ANY_PPV | 88 | 🔄33 | ↑1.042 | ↑2d | SQ·PV | +7.3% | -16.19/-29.31 | +4.89% | 20% |
| [MACPOWER](https://in.tradingview.com/chart/?symbol=NSE:MACPOWER)<br><sub>📶W9 · W↑29d · ↑CMF1d</sub> | ✓ SAFE | CNC turning centers and lathe machines for metal fabrication | ⚡ BULL_ANY_PPV | 58 | ↑92 | ↑1.083 | ↑2d | SQ·PV | +14.3% | 33.98/20.55 | +5.48% | 20% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>📶W9 · W↑77d · 🚀SS · ↓CMF19d</sub> | ✓ SAFE | Gaming platform, esports, mobile and console games, India and global | 📈 BULL_ANY_MID | 99 | 🔄60 | ↑1.010 | ↑1d | SQ | +1.4% | 15.54/11.87 | +1.45% | 20% |
| [BELRISE](https://in.tradingview.com/chart/?symbol=NSE:BELRISE)<br><sub>📶W9 · ↓CMF17d</sub> | ✓ SAFE | Auto parts maker: chassis, polymers, suspension systems | 📈 BULL_ANY_MID | 99 | 🔄89 | ↑1.006 | ↑1d | SQ | +1.0% | -15.5/-17.62 | +1.01% | 20% |
| [KDDL](https://in.tradingview.com/chart/?symbol=NSE:KDDL)<br><sub>📶W9 · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | Watch dials, hands, precision components manufacturer, luxury retail | 📈 BULL_ANY_MID | 99 | 🔄86 | ↑1.012 | ↑1d | SQ | +2.1% | -7.31/-8.95 | +2.14% | 20% |
| [CARERATING](https://in.tradingview.com/chart/?symbol=NSE:CARERATING)<br><sub>📶W9 · W↑9d · 🚀SS · ↓CMF3d</sub> | ⚠ CAUTION | Credit ratings for corporate debt and bonds | 📈 BULL_ANY_MID | 98 | 🔄53 | ↑1.012 | ↑2d | SQ | +2.1% | 36.64/33.83 | +1.07% | 20% |
| [SHADOWFAX](https://in.tradingview.com/chart/?symbol=NSE:SHADOWFAX)<br><sub>📶W9 · ↑CMF4d</sub> | ✓ SAFE | Fast delivery logistics platform for e-commerce merchants | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.020 | ↑1d | SQ | +2.0% | -15.39/-19.69 | +2.00% | 20% |
| [KIRLOSBROS](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSBROS)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Pumps and fluid management systems for infrastructure and agriculture | 📈 BULL_ANY_MID | 85 | 🔄58 | ↑1.003 | ↓15d | SQ | -1.8% | -22.64/-25.1 | +1.00% | 20% |
| [TAJGVK](https://in.tradingview.com/chart/?symbol=NSE:TAJGVK)<br><sub>📶W9 · W↑49d · ↑CMF17d</sub> | ✓ SAFE | Luxury hotel operations and management, premium hospitality sector | 📈 BULL_ANY_MID | 80 | 🔄44 | ↑1.003 | ↑22d | SQ | +8.7% | 36.81/35.61 | +0.25% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑32d · ↓CMF18d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 67 | ↓81 | ↑1.007 | ↑3d | SQ | +3.9% | 10.9/8.21 | +0.29% | 20% |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON)<br><sub>📶W9 · W↑34d · ↑CMF30d</sub> | ✓ SAFE | Pistons, rings, pins, valves for automobile engines | 📈 BULL_ANY_MID | 67 | ↑93 | ↑1.015 | ↑3d | SQ | +2.3% | 39.77/37.38 | +0.56% | 20% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>📶W9 · W↑79d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 63 | ↑46 | ↑1.018 | ↑2d | SQ | +3.0% | 15.62/11.03 | +1.09% | 20% |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 62 | ↑60 | ↑1.020 | ↑3d | SQ | +2.9% | 12.63/4.94 | +2.41% | 20% |
| [APOLLOHOSP](https://in.tradingview.com/chart/?symbol=NSE:APOLLOHOSP)<br><sub>📶W9 · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↓74 | ↓1.004 | ↑2d | SQ | +0.7% | 38.14/36.38 | +0.01% | 20% |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL)<br><sub>📶W9 · W↑29d · ↓CMF2d</sub> | ✓ SAFE | Consumer electronics retail chain South India operations | 📈 BULL_ANY_MID | 58 | ↓62 | ↓1.001 | ↓2d | SQ | +2.3% | 4.64/1.93 | -1.96% | 20% |
| [RGL](https://in.tradingview.com/chart/?symbol=NSE:RGL)<br><sub>📶W9 · W↑34d · ↓CMF0d</sub> | ✓ SAFE | Global recruitment and staffing services provider | 📈 BULL_ANY_MID | 58 | ↑61 | ↓1.005 | ↑2d | SQ | +2.8% | 14.92/10.89 | -1.25% | 20% |
| [EIHOTEL](https://in.tradingview.com/chart/?symbol=NSE:EIHOTEL)<br><sub>📶W9 · W↑34d · ↓CMF15d</sub> | ⚠ CAUTION | Luxury hotels resorts Oberoi Trident brands hospitality | 📈 BULL_ANY_MID | 58 | ↑37 | ↓1.003 | ↑2d | SQ | +2.0% | 8.85/7.09 | -1.10% | 20% |
| [NGLFINE](https://in.tradingview.com/chart/?symbol=NSE:NGLFINE)<br><sub>📶W9 · ↑CMF6d</sub> | ✓ SAFE | Veterinary APIs, intermediates, animal health pharmaceuticals manufacturer | 📈 BULL_ANY_MID | 57 | ↑98 | ↑1.021 | ↑8d | SQ | +9.0% | 40.9/36.66 | +0.88% | 20% |
| [BRITANNIA](https://in.tradingview.com/chart/?symbol=NSE:BRITANNIA)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF22d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 54 | ↑33 | ↑1.019 | ↑11d | SQ | +4.7% | 45.79/38.66 | +0.99% | 20% |
| [BOROSCI](https://in.tradingview.com/chart/?symbol=NSE:BOROSCI)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | Laboratory glassware manufacturer for pharma QC and biotech | 📈 BULL_ANY_MID | 51 | ↓78 | ↓0.994 | ↓9d | SQ | -3.3% | -25.93/-27.59 | -1.10% | 20% |
| [TCI](https://in.tradingview.com/chart/?symbol=NSE:TCI)<br><sub>↓CMF0d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄21 | ↑1.005 | ↑1d | SQ·PV | +1.5% | -36.1/-39.96 | +1.54% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>🚀SS · ↓CMF26d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 99 | 🔄42 | ↑1.010 | ↑1d | SQ | +2.6% | -48.58/-54.51 | +2.56% | 20% |
| [IRCTC](https://in.tradingview.com/chart/?symbol=NSE:IRCTC)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Railway ticketing catering tourism water beverages | 🟡 BULL_OS_L2 | 50 | ↓5 | ↓0.995 | ↓10d | SQ | -1.4% | -57.73/-59.67 | -0.57% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄60 | ↑1.012 | ↑1d | SQ | +3.0% | -40.63/-43.65 | +2.95% | 20% |
| [AMBUJACEM](https://in.tradingview.com/chart/?symbol=NSE:AMBUJACEM)<br><sub>W↑27d · ↑CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄13 | ↑1.008 | ↑1d | SQ | +2.0% | 0.82/0.46 | +2.00% | 20% |
| [GMRP&UI](https://in.tradingview.com/chart/?symbol=NSE:GMRP&UI)<br><sub>↓CMF30d</sub> | ✓ SAFE | Power generation, urban infrastructure, road-rail-port development | 📈 BULL_ANY_MID | 99 | 🔄25 | ↑1.013 | ↑1d | SQ | +2.7% | -41.16/-43.51 | +2.74% | 20% |
| [GRINFRA](https://in.tradingview.com/chart/?symbol=NSE:GRINFRA)<br><sub>↓CMF7d</sub> | ⚠ CAUTION | Road EPC contractor, highways and railways infrastructure | 📈 BULL_ANY_MID | 99 | 🔄17 | ↑1.007 | ↑1d | SQ | +0.8% | -38.93/-43.16 | +0.75% | 20% |
| [BANARISUG](https://in.tradingview.com/chart/?symbol=NSE:BANARISUG)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄36 | ↑1.004 | ↑1d | SQ | +0.6% | -10.47/-10.59 | +0.62% | 20% |
| [MUTHOOTFIN](https://in.tradingview.com/chart/?symbol=NSE:MUTHOOTFIN)<br><sub>↓CMF2d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 64 | ↓27 | ↑0.999 | ↑1d | SQ | +0.2% | -22.85/-24.08 | +0.17% | 20% |
| [HERITGFOOD](https://in.tradingview.com/chart/?symbol=NSE:HERITGFOOD)<br><sub>W↑29d · 🚀SS · ↑CMF6d</sub> | ✓ SAFE | Dairy products, renewable energy, animal feed manufacturer | 📈 BULL_ANY_MID | 60 | ↓12 | ↑0.999 | ↓5d | SQ | -0.2% | -15.12/-15.23 | +0.20% | 20% |
| [ACC](https://in.tradingview.com/chart/?symbol=NSE:ACC)<br><sub>W↑82d · ↑CMF13d · ⚠️TRAP</sub> | ⚠ CAUTION | Cement manufacturing, ready-mix concrete, infrastructure | 📈 BULL_ANY_MID | 58 | ↓14 | ↓0.998 | ↓2d | SQ | +1.1% | -7.1/-7.81 | -1.04% | 20% |
| [IGIL](https://in.tradingview.com/chart/?symbol=NSE:IGIL)<br><sub>↑CMF0d</sub> | ✓ SAFE | Diamond gemstone jewelry certification grading laboratory services | 📈 BULL_ANY_MID | 58 | ↑41 | ↓1.010 | ↑2d | SQ | +5.1% | -45.21/-51.23 | -0.45% | 20% |
| [CASTROLIND](https://in.tradingview.com/chart/?symbol=NSE:CASTROLIND)<br><sub>W↑9d · ↓CMF30d</sub> | ⚠ CAUTION | Automotive and industrial lubricants manufacturer, bp subsidiary | 📈 BULL_ANY_MID | 58 | ↓38 | ↓1.001 | ↑2d | SQ | +0.4% | 8.55/8.2 | -0.07% | 20% |
| [MADRASFERT](https://in.tradingview.com/chart/?symbol=NSE:MADRASFERT)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 53 | ↓20 | ↑0.996 | ↓12d | SQ | -0.9% | -41.17/-42.02 | +0.27% | 20% |
| [FORTIS](https://in.tradingview.com/chart/?symbol=NSE:FORTIS)<br><sub>↓CMF19d</sub> | ⚠ CAUTION | Hospital chain, diagnostics, multi-specialty tertiary quaternary care | 📈 BULL_ANY_MID | 52 | ↓51 | ↓0.997 | ↓8d | SQ | -0.2% | -30.71/-32.28 | -0.34% | 20% |

```
NSE:STEELCAS,NSE:LTFOODS,NSE:MACPOWER,NSE:NAZARA,NSE:BELRISE,NSE:KDDL,NSE:CARERATING,NSE:SHADOWFAX,NSE:KIRLOSBROS,NSE:TAJGVK,NSE:SHRIRAMFIN,NSE:SHRIPISTON,NSE:DLF,NSE:JSWSTEEL,NSE:APOLLOHOSP,NSE:EMIL,NSE:RGL,NSE:EIHOTEL,NSE:NGLFINE,NSE:BRITANNIA,NSE:BOROSCI,NSE:TCI,NSE:TATASTEEL,NSE:IRCTC,NSE:HINDALCO,NSE:AMBUJACEM,NSE:GMRP&UI,NSE:GRINFRA,NSE:BANARISUG,NSE:MUTHOOTFIN,NSE:HERITGFOOD,NSE:ACC,NSE:IGIL,NSE:CASTROLIND,NSE:MADRASFERT,NSE:FORTIS
```

---

### 🔥 MAJOR — PPV confirmed (10)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>📶W9 · 🚀SS·10x · ↓CMF0d</sub> | ✓ SAFE | Electronics manufacturing design assembly testing services | ⚡ BULL_ANY_PPV | 54 | 🔄95 | ↑1.019 | ↑1d | PV | +2.6% | -15.15/-22.05 | +2.56% | 20% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>📶W9 · W↑4d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE | Private bank, retail deposits, MSME lending, treasury operations | ⚡ BULL_ANY_PPV | 35 | 🔄89 | ↑1.037 | ↑15d | PV | +8.5% | 50.51/45.7 | +4.21% | 20% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>📶W9 · W↑74d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 0 | ↑76 | ↑1.059 | ↑20d | PV | +19.4% | 64.61/59.48 | +5.25% | 20% |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Residential and commercial real estate development, Mumbai Pune Bangalore | ⚡ BULL_ANY_PPV | 0 | ↑84 | ↑1.101 | ↑33d | PV | +51.0% | 56.79/51.26 | +9.37% | 20% |
| [ICRA](https://in.tradingview.com/chart/?symbol=NSE:ICRA)<br><sub>🚀SS · ↓CMF30d · 🔥PHX</sub> | ✓ SAFE | Credit ratings for bonds and debt securities | 🔥 BULL_OS_PPV | 40 | 🔄11 | ↑1.000 | ↓15d | PV | -5.2% | -66.83/-69.83 | +3.09% | 20% |
| [SHARDAMOTR](https://in.tradingview.com/chart/?symbol=NSE:SHARDAMOTR)<br><sub>W↑24d · RVOL13x · ↓CMF30d</sub> | ⚠ CAUTION | Emission control and suspension auto components manufacturer | ⚡ BULL_ANY_PPV | 59 | 🔄27 | ↑1.012 | ↑1d | PV | +1.4% | -21.56/-28.6 | +1.42% | 20% |
| [IFCI](https://in.tradingview.com/chart/?symbol=NSE:IFCI)<br><sub>↓CMF21d</sub> | ✓ SAFE | Long-term industrial project financing and infrastructure lending | ⚡ BULL_ANY_PPV | 54 | 🔄82 | ↑1.023 | ↑1d | PV | +3.1% | -42.93/-48.49 | +3.11% | 20% |
| [GOCOLORS](https://in.tradingview.com/chart/?symbol=NSE:GOCOLORS)<br><sub>↓CMF29d</sub> | ✓ SAFE | Women's bottom-wear retail, branded leggings and trousers | ⚡ BULL_ANY_PPV | 54 | 🔄19 | ↑1.030 | ↑1d | PV | +6.2% | -40.39/-42.85 | +6.19% | 20% |
| [DOLLAR](https://in.tradingview.com/chart/?symbol=NSE:DOLLAR)<br><sub>↑CMF4d</sub> | ✓ SAFE | Knitted innerwear and casual apparel manufacturer for mass market | ⚡ BULL_ANY_PPV | 54 | 🔄8 | ↑1.029 | ↑1d | PV | +4.3% | -29.69/-36.15 | +4.31% | 20% |
| [FORCEMOT](https://in.tradingview.com/chart/?symbol=NSE:FORCEMOT)<br><sub>↓CMF30d</sub> | ✓ SAFE | Small commercial vehicles, vans, tractors, automotive components | ⚡ BULL_ANY_PPV | 48 | 🔄40 | ↑1.002 | ↓12d | PV | -0.2% | -44.42/-45.06 | +1.64% | 20% |

```
NSE:SYRMA,NSE:KTKBANK,NSE:DIVISLAB,NSE:LODHA,NSE:ICRA,NSE:SHARDAMOTR,NSE:IFCI,NSE:GOCOLORS,NSE:DOLLAR,NSE:FORCEMOT
```

### 🟢 OVERSOLD — reversal from −53/−60 (6)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GODIGIT](https://in.tradingview.com/chart/?symbol=NSE:GODIGIT)<br><sub>↓CMF30d · 🔥PHX</sub> | ✓ SAFE | Digital-first general insurance platform motor health travel | 🟢 BULL_OVERSOLD | 10 | ↓5 | ↑0.957 | ↓15d | — | -15.5% | -68.6/-68.98 | +0.71% | 20% |
| [SALZERELEC](https://in.tradingview.com/chart/?symbol=NSE:SALZERELEC)<br><sub>↓CMF22d · 🎯SLING</sub> | ✓ SAFE | Switchgear wires cables energy management industrial electrical solutions | 🟢 BULL_OVERSOLD | 5 | ↓11 | ↑0.986 | ↓33d | — | -10.9% | -60.03/-60.66 | -0.06% | 20% |
| [AMRUTANJAN](https://in.tradingview.com/chart/?symbol=NSE:AMRUTANJAN)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 16 | ↓17 | ↑0.990 | ↓9d | — | -4.1% | -56.46/-57.62 | -0.15% | 20% |
| [KEC](https://in.tradingview.com/chart/?symbol=NSE:KEC)<br><sub>↓CMF23d · ⚠️TRAP</sub> | ✓ SAFE | Power transmission EPC, railways, infrastructure projects globally | 🟡 BULL_OS_L2 | 8 | ↓2 | ↓0.982 | ↓12d | — | -4.3% | -54.0/-55.49 | -1.84% | 20% |
| [AXISBANK](https://in.tradingview.com/chart/?symbol=NSE:AXISBANK)<br><sub>↓CMF17d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 5 | ↓44 | ↑0.988 | ↓36d | — | -2.5% | -58.03/-58.94 | +1.01% | 20% |
| [RIIL](https://in.tradingview.com/chart/?symbol=NSE:RIIL)<br><sub>↓CMF14d · ⚠️TRAP</sub> | ✓ SAFE | Petroleum pipelines, logistics, energy sector infrastructure | 🟡 BULL_OS_L2 | 0 | ↓20 | ↓0.975 | ↓38d | — | -3.4% | -58.4/-58.86 | -1.32% | 20% |

```
NSE:GODIGIT,NSE:SALZERELEC,NSE:AMRUTANJAN,NSE:KEC,NSE:AXISBANK,NSE:RIIL
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (33)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [AJAXENGG](https://in.tradingview.com/chart/?symbol=NSE:AJAXENGG)<br><sub>📶W9 · W↑14d · ↑CMF13d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | 🔄51 | ↑1.008 | ↑2d | — | +1.8% | -0.19/-1.16 | +0.80% | 20% |
| [JSL](https://in.tradingview.com/chart/?symbol=NSE:JSL)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF1d</sub> | ⚠ CAUTION | Stainless steel flat products for automotive construction railways | 📈 BULL_ANY_MID | 56 | 🔄38 | ↑1.013 | ↑4d | — | +3.3% | 34.88/33.3 | +1.27% | 20% |
| [PACEDIGITK](https://in.tradingview.com/chart/?symbol=NSE:PACEDIGITK)<br><sub>📶W9 · ↓CMF6d</sub> | ✓ SAFE | Power systems, fiber networks, telecom and energy infrastructure | 📈 BULL_ANY_MID | 54 | 🔄50 | ↑1.015 | ↑1d | — | +2.9% | -22.54/-23.33 | +2.93% | 20% |
| [VMART](https://in.tradingview.com/chart/?symbol=NSE:VMART)<br><sub>📶W9 · ↓CMF11d</sub> | ✓ SAFE | Value fashion retail Tier II-IV cities apparel footwear | 📈 BULL_ANY_MID | 54 | 🔄66 | ↑1.021 | ↑1d | — | +2.2% | -24.08/-26.78 | +2.17% | 20% |
| [OIL](https://in.tradingview.com/chart/?symbol=NSE:OIL)<br><sub>📶W9 · W↑9d · 🚀SS · ↑CMF16d</sub> | ✓ SAFE | Crude oil and natural gas exploration production transportation | 📈 BULL_ANY_MID | 36 | 🔄44 | ↑1.023 | ↑19d | — | +8.2% | 43.68/42.57 | +2.01% | 20% |
| [BLUESTARCO](https://in.tradingview.com/chart/?symbol=NSE:BLUESTARCO)<br><sub>📶W9 · W↑14d · ↑CMF14d</sub> | ⚠ CAUTION | AC manufacturing, refrigeration, MEP solutions for commercial buildings | 📈 BULL_ANY_MID | 28 | ↑31 | ↑1.013 | ↑2d | — | +2.8% | 1.22/-2.61 | +0.63% | 20% |
| [PGEL](https://in.tradingview.com/chart/?symbol=NSE:PGEL)<br><sub>📶W9 · W↑34d · ↑CMF30d</sub> | ✓ SAFE | EMS plastic moulding consumer electronics appliances manufacturing | 📈 BULL_ANY_MID | 18 | ↑56 | ↓1.030 | ↑2d | — | +4.7% | 31.59/26.34 | +0.09% | 20% |
| [BLUEJET](https://in.tradingview.com/chart/?symbol=NSE:BLUEJET)<br><sub>📶W9 · W↑103d · 🚀SS · ↑CMF24d</sub> | ✓ SAFE | Specialty pharma CDMO, niche chemistry, healthcare ingredients manufacturing | 📈 BULL_ANY_MID | 18 | ↑68 | ↑1.041 | ↑2d | — | +7.1% | 33.77/25.42 | +1.61% | 20% |
| [RELAXO](https://in.tradingview.com/chart/?symbol=NSE:RELAXO)<br><sub>📶W9 · W↑82d · ↑CMF30d</sub> | ✓ SAFE | Mass-market slippers sandals shoes footwear manufacturer | 📈 BULL_ANY_MID | 18 | ↑67 | ↓1.012 | ↑2d | — | +4.1% | 19.79/17.28 | -0.23% | 20% |
| [CONCORDBIO](https://in.tradingview.com/chart/?symbol=NSE:CONCORDBIO)<br><sub>📶W9 · W↑77d · ↓CMF17d</sub> | ✓ SAFE | Fermentation APIs immunosuppressants oncology contract manufacturer | 📈 BULL_ANY_MID | 18 | ↑45 | ↓1.024 | ↑2d | — | +5.9% | -0.96/-9.15 | -0.03% | 20% |
| [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM)<br><sub>📶W9 · W↑29d · ↑CMF22d</sub> | ✓ SAFE | Digital payments, fintech, consumer merchants | 📈 BULL_ANY_MID | 17 | ↑73 | ↓1.018 | ↑3d | — | +3.3% | 31.28/28.54 | +0.19% | 20% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>📶W9 · W↑29d · ↑CMF10d</sub> | ✓ SAFE | Rear axles and drive shafts for commercial vehicles globally | 📈 BULL_ANY_MID | 16 | ↑92 | ↓1.022 | ↑4d | — | +4.7% | 36.66/34.1 | -0.25% | 20% |
| [ULTRACEMCO](https://in.tradingview.com/chart/?symbol=NSE:ULTRACEMCO)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 15 | ↑42 | ↑1.010 | ↑15d | — | +5.6% | 51.42/48.64 | +0.28% | 20% |
| [VSSL](https://in.tradingview.com/chart/?symbol=NSE:VSSL)<br><sub>📶W9 · W↑14d · ↓CMF6d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↑64 | ↓1.005 | ↑15d | — | +11.2% | 31.06/30.75 | -1.98% | 20% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>📶W9 · W↑34d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Gold jewellery retail across India and Middle East markets | 📈 BULL_ANY_MID | 4 | ↑90 | ↓1.084 | ↑16d | — | +69.6% | 63.23/61.76 | +0.95% | 20% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>📶W9 · W↑29d · ↑CMF20d</sub> | ✓ SAFE | Differential assemblies and gears for electric vehicles | 📈 BULL_ANY_MID | 0 | ↑92 | ↑1.061 | ↑33d | — | +28.1% | 67.05/66.57 | +6.00% | 20% |
| [DIXON](https://in.tradingview.com/chart/?symbol=NSE:DIXON)<br><sub>📶W9 · W↑94d · ↑CMF10d</sub> | ✓ SAFE | Consumer electronics contract manufacturing for global brands | 📈 BULL_ANY_MID | 0 | ↑69 | ↓1.024 | ↑21d | — | +19.9% | 49.78/46.48 | +0.44% | 20% |
| [ECLERX](https://in.tradingview.com/chart/?symbol=NSE:ECLERX)<br><sub>📶W9 · W↑24d · ↑CMF19d</sub> | ✓ SAFE | Legal document processing and financial analytics for global enterprises | 📈 BULL_ANY_MID | 0 | ↑57 | ↓1.025 | ↑21d | — | +43.4% | 52.0/51.33 | -2.10% | 20% |
| [AMAGI](https://in.tradingview.com/chart/?symbol=NSE:AMAGI)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Cloud TV platform for content distribution and monetization | 📈 BULL_ANY_MID | 0 | ↑50 | ↑1.059 | ↑36d | — | +63.1% | 68.27/66.52 | +1.54% | 20% |
| [WONDERLA](https://in.tradingview.com/chart/?symbol=NSE:WONDERLA)<br><sub>↓CMF16d</sub> | ⚠ CAUTION | Theme parks and resort hospitality for leisure tourism | 📈 BULL_ANY_MID | 59 | 🔄18 | ↑1.007 | ↑1d | — | +0.8% | -30.82/-34.46 | +0.82% | 20% |
| [NATIONALUM](https://in.tradingview.com/chart/?symbol=NSE:NATIONALUM)<br><sub>↓CMF3d</sub> | ✓ SAFE | Bauxite mining, alumina refining, primary aluminium production | 📈 BULL_ANY_MID | 58 | 🔄70 | ↑1.010 | ↑2d | — | +3.9% | -25.59/-28.16 | +0.86% | 20% |
| [CEATLTD](https://in.tradingview.com/chart/?symbol=NSE:CEATLTD)<br><sub>↓CMF1d</sub> | ✓ SAFE | Tyres for cars trucks two-wheelers buses manufacturing | 📈 BULL_ANY_MID | 40 | 🔄44 | ↑1.002 | ↓23d | — | +2.0% | -17.64/-19.11 | +0.88% | 20% |
| [ANUP](https://in.tradingview.com/chart/?symbol=NSE:ANUP)<br><sub>↓CMF11d</sub> | ⚠ CAUTION | Industrial boilers and pressure vessels manufacturing | 📈 BULL_ANY_MID | 40 | 🔄48 | ↑1.009 | ↓34d | — | +13.3% | -30.48/-30.98 | +3.07% | 20% |
| [BHAGCHEM](https://in.tradingview.com/chart/?symbol=NSE:BHAGCHEM)<br><sub>↓CMF9d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 40 | 🔄59 | ↑1.002 | ↓38d | — | +14.6% | -25.45/-26.44 | +0.77% | 20% |
| [DCAL](https://in.tradingview.com/chart/?symbol=NSE:DCAL)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Pharmaceutical contract manufacturing and API production | 📈 BULL_ANY_MID | 18 | ↓16 | ↓0.994 | ↓2d | — | +1.8% | -15.92/-16.27 | -1.43% | 20% |
| [POLYCAB](https://in.tradingview.com/chart/?symbol=NSE:POLYCAB)<br><sub>↓CMF6d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 12 | ↓77 | ↓0.982 | ↓8d | — | -3.9% | -46.59/-46.91 | -1.62% | 20% |
| [TITAGARH](https://in.tradingview.com/chart/?symbol=NSE:TITAGARH)<br><sub>↓CMF22d · ⚠️TRAP</sub> | ✓ SAFE | Rail coaches wagons metro trains manufacturing | 📈 BULL_ANY_MID | 8 | ↓39 | ↓0.993 | ↓12d | — | -4.0% | -39.39/-41.27 | -1.09% | 20% |
| [CEIGALL](https://in.tradingview.com/chart/?symbol=NSE:CEIGALL)<br><sub>↓CMF30d</sub> | ✓ SAFE | Highway bridges tunnels construction EPC contractor | 📈 BULL_ANY_MID | 7 | ↓70 | ↑0.988 | ↓18d | — | -6.6% | -46.93/-47.88 | +0.34% | 20% |
| [TMPV](https://in.tradingview.com/chart/?symbol=NSE:TMPV)<br><sub>🚀SS · ↓CMF29d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓17 | ↑0.999 | ↓33d | — | -12.4% | -49.04/-51.5 | +1.53% | 20% |
| [KRBL](https://in.tradingview.com/chart/?symbol=NSE:KRBL)<br><sub>↓CMF14d</sub> | ✓ SAFE | Basmati rice production processing export global markets | 📈 BULL_ANY_MID | 5 | ↓35 | ↑0.997 | ↓35d | — | +1.5% | -47.39/-48.4 | +0.60% | 20% |
| [SWARAJENG](https://in.tradingview.com/chart/?symbol=NSE:SWARAJENG)<br><sub>↓CMF8d</sub> | ✓ SAFE | Diesel engines for agricultural tractors, 22-65 HP range | 📈 BULL_ANY_MID | 5 | ↓29 | ↑0.997 | ↓34d | — | -2.6% | -43.89/-45.65 | +1.11% | 20% |
| [DLINKINDIA](https://in.tradingview.com/chart/?symbol=NSE:DLINKINDIA)<br><sub>↓CMF13d</sub> | ✓ SAFE | Networking equipment distribution, consumer and enterprise markets | 📈 BULL_ANY_MID | 5 | ↓49 | ↑0.993 | ↓43d | — | -2.5% | -28.27/-29.05 | +0.83% | 20% |
| [THOMASCOOK](https://in.tradingview.com/chart/?symbol=NSE:THOMASCOOK)<br><sub>↓CMF11d</sub> | ✓ SAFE | Travel agency, tours, forex, hotel bookings, Indians abroad | 📈 BULL_ANY_MID | 0 | ↓12 | ↓0.990 | ↓40d | — | +7.8% | -50.82/-51.08 | -0.51% | 20% |

```
NSE:AJAXENGG,NSE:JSL,NSE:PACEDIGITK,NSE:VMART,NSE:OIL,NSE:BLUESTARCO,NSE:PGEL,NSE:BLUEJET,NSE:RELAXO,NSE:CONCORDBIO,NSE:PAYTM,NSE:GNA,NSE:ULTRACEMCO,NSE:VSSL,NSE:KALYANKJIL,NSE:SONACOMS,NSE:DIXON,NSE:ECLERX,NSE:AMAGI,NSE:WONDERLA,NSE:NATIONALUM,NSE:CEATLTD,NSE:ANUP,NSE:BHAGCHEM,NSE:DCAL,NSE:POLYCAB,NSE:TITAGARH,NSE:CEIGALL,NSE:TMPV,NSE:KRBL,NSE:SWARAJENG,NSE:DLINKINDIA,NSE:THOMASCOOK
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
