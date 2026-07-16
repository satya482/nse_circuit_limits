> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-07-16
*Generated 2026-07-16 15:45 IST*

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

**Total bull crosses today: 82** · 35 inside active squeeze

```
NSE:DEEPAKFERT,NSE:PNBGILTS,NSE:RKFORGE,NSE:ASKAUTOLTD,NSE:BECTORFOOD,NSE:GRINDWELL,NSE:SRF,NSE:EMMVEE,NSE:DIXON,NSE:CYIENTDLM,NSE:SKIPPER,NSE:KIRLFER,NSE:MOLDTKPAC,NSE:HARSHA,NSE:KKCL,NSE:LLOYDSME,NSE:YATHARTH,NSE:PANACEABIO,NSE:JKTYRE,NSE:HFCL,NSE:INOXINDIA,NSE:ACE,NSE:INDIGOPNTS,NSE:TVSSRICHAK,NSE:THYROCARE,NSE:PPLPHARMA,NSE:ALLTIME,NSE:MANKIND,NSE:BHEL,NSE:INGERRAND,NSE:GLAND,NSE:COSMOFIRST,NSE:PGIL,NSE:HLEGLAS,NSE:EIMCOELECO,NSE:FINEORG,NSE:ABCAPITAL,NSE:SWIGGY,NSE:OFSS,NSE:ALKEM,NSE:ADOR,NSE:APLLTD,NSE:KAYNES,NSE:IEX,NSE:GNFC,NSE:WEBELSOLAR,NSE:IPL,NSE:IGL,NSE:SANOFICONR,NSE:GODFRYPHLP,NSE:BLS,NSE:CESC,NSE:SUNTV,NSE:COALINDIA,NSE:HINDPETRO,NSE:LINDEINDIA,NSE:VHL,NSE:BAYERCROP,NSE:CIEINDIA,NSE:JKCEMENT,NSE:CASTROLIND,NSE:FORCEMOT,NSE:ANTHEM,NSE:ANGELONE,NSE:PNB,NSE:LTFOODS,NSE:JSLL,NSE:AMBUJACEM,NSE:JSWDULUX,NSE:POWERINDIA,NSE:UNIONBANK,NSE:UNOMINDA,NSE:ENRIN,NSE:HDFCLIFE,NSE:JAINREC,NSE:INTERARCH,NSE:TVSHLTD,NSE:TMPV,NSE:PRINCEPIPE,NSE:THOMASCOOK,NSE:TIINDIA,NSE:NFL
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (42)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [DEEPAKFERT](https://in.tradingview.com/chart/?symbol=NSE:DEEPAKFERT)<br><sub>📶W9 · W↑89d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Fertilizers, crop nutrition, bulk chemicals, mining sector | ⚡ BULL_ANY_PPV | 94 | 🔄74 | ↑1.026 | ↑1d | SQ·PV | +3.4% | 12.21/8.75 | +3.38% | 20% |
| [PNBGILTS](https://in.tradingview.com/chart/?symbol=NSE:PNBGILTS)<br><sub>📶W9 · W↑67d · ↑CMF0d</sub> | ✓ SAFE | Government securities dealer, primary dealer, debt market | ⚡ BULL_ANY_PPV | 94 | 🔄61 | ↑1.027 | ↑1d | SQ·PV | +4.3% | -12.01/-18.97 | +4.27% | 20% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>📶W9 · W↑4d · 🚀SS·31x · ↑CMF0d</sub> | ✓ SAFE | Precision forged auto, rail, engineering components manufacturer | ⚡ BULL_ANY_PPV | 89 | 🔄55 | ↑1.036 | ↑1d | SQ·PV | +4.7% | -12.41/-20.96 | +4.65% | 20% |
| [ASKAUTOLTD](https://in.tradingview.com/chart/?symbol=NSE:ASKAUTOLTD)<br><sub>📶W9 · W↑24d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Two-wheeler advanced braking systems manufacturer India | ⚡ BULL_ANY_PPV | 52 | ↑48 | ↑1.031 | ↑8d | SQ·PV | +7.0% | 41.35/35.43 | +2.57% | 20% |
| [BECTORFOOD](https://in.tradingview.com/chart/?symbol=NSE:BECTORFOOD)<br><sub>📶W9 · W↑4d · 🚀SS·76x · ↑CMF0d</sub> | ✓ SAFE | Biscuits bakery products FMCG retail consumer branded foods | ⚡ BULL_ANY_PPV | 49 | 🔄14 | ↑1.095 | ↑1d | PV | +13.8% | -30.05/-42.13 | +13.77% | 20% |
| [GRINDWELL](https://in.tradingview.com/chart/?symbol=NSE:GRINDWELL)<br><sub>📶W9 · W↑67d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Grinding wheels, abrasives, ceramics for industrial manufacturing | ⚡ BULL_ANY_PPV | 49 | 🔄90 | ↑1.127 | ↑1d | PV | +16.4% | 9.7/-1.22 | +16.44% | 20% |
| [SRF](https://in.tradingview.com/chart/?symbol=NSE:SRF)<br><sub>📶W9 · W↑63d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Technical textiles, chemicals, films for industrial applications | ⚡ BULL_ANY_PPV | 48 | 🔄48 | ↑1.038 | ↑2d | PV | +5.3% | 36.0/27.31 | +4.10% | 20% |
| [EMMVEE](https://in.tradingview.com/chart/?symbol=NSE:EMMVEE)<br><sub>📶W9 · 🚀SS·9x · ↑CMF0d</sub> | ✓ SAFE | Solar PV modules and cells manufacturing, renewable energy sector | ⚡ BULL_ANY_PPV | 18 | ↑50 | ↑1.063 | ↑2d | PV | +9.1% | 29.84/20.34 | +6.83% | 20% |
| [DIXON](https://in.tradingview.com/chart/?symbol=NSE:DIXON)<br><sub>📶W9 · W↑84d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Consumer electronics contract manufacturing for global brands | ⚡ BULL_ANY_PPV | 9 | ↑65 | ↑1.082 | ↑11d | PV | +21.3% | 67.07/62.79 | +6.27% | 20% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>📶W9 · W↑84d · 🚀SS · ★ · ↑CMF9d</sub> | ✓ SAFE | Electronics manufacturing design integration testing subsystems OEMs | ⚡ BULL_ANY_PPV | 9 | ↑90 | ↑1.101 | ↑11d | PV | +26.4% | 71.75/70.09 | +8.99% | 20% |
| [SKIPPER](https://in.tradingview.com/chart/?symbol=NSE:SKIPPER)<br><sub>📶W9 · W↑79d · ↓CMF17d · ÷DIV</sub> | ✓ SAFE | Steel transmission towers, polymer pipes, infrastructure EPC | 📈 BULL_ANY_MID | 99 | 🔄78 | ↑1.013 | ↑1d | SQ | +2.4% | 13.85/12.82 | +2.37% | 20% |
| [KIRLFER](https://in.tradingview.com/chart/?symbol=NSE:KIRLFER)<br><sub>📶W9 · W↑24d · ↓CMF20d</sub> | ⚠ CAUTION | Pig iron and grey iron castings for automobiles | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.013 | ↑1d | SQ | +2.1% | 2.84/1.65 | +2.14% | 20% |
| [MOLDTKPAC](https://in.tradingview.com/chart/?symbol=NSE:MOLDTKPAC)<br><sub>📶W9 · ↓CMF26d</sub> | ✓ SAFE | Injection-molded plastic containers for automotive lubricants food paints | 📈 BULL_ANY_MID | 99 | 🔄65 | ↑1.015 | ↑1d | SQ | +1.4% | -7.95/-12.54 | +1.44% | 20% |
| [HARSHA](https://in.tradingview.com/chart/?symbol=NSE:HARSHA)<br><sub>📶W9 · W↑72d · ↓CMF30d</sub> | ✓ SAFE | Precision bearing cages, brass steel polyamide components manufacturing | 📈 BULL_ANY_MID | 98 | 🔄57 | ↑1.010 | ↑2d | SQ | +2.6% | 9.54/9.12 | +0.66% | 20% |
| [KKCL](https://in.tradingview.com/chart/?symbol=NSE:KKCL)<br><sub>📶W9 · W↑24d · ↑CMF22d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 98 | 🔄43 | ↑1.010 | ↑2d | SQ | +2.1% | 26.81/24.43 | +0.60% | 20% |
| [LLOYDSME](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSME)<br><sub>📶W9 · 🚀SS · ↓CMF14d</sub> | ✓ SAFE | Iron ore mining, sponge iron production, power generation | 📈 BULL_ANY_MID | 94 | 🔄78 | ↑1.022 | ↑1d | SQ | +3.1% | 6.52/1.69 | +3.12% | 20% |
| [YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Multi-specialty hospital network trauma care Delhi-NCR Madhya Pradesh | 📈 BULL_ANY_MID | 93 | 🔄77 | ↑1.022 | ↑2d | SQ | +3.6% | 8.75/2.44 | +2.14% | 20% |
| [PANACEABIO](https://in.tradingview.com/chart/?symbol=NSE:PANACEABIO)<br><sub>📶W9 · W↑72d · 🚀SS · ↓CMF29d</sub> | ✓ SAFE | Vaccine and pharmaceutical manufacturing biotech company | 📈 BULL_ANY_MID | 89 | 🔄90 | ↑1.033 | ↑1d | SQ | +4.8% | 15.64/11.07 | +4.77% | 10% 🟨 |
| [JKTYRE](https://in.tradingview.com/chart/?symbol=NSE:JKTYRE)<br><sub>📶W9 · W↑19d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Radial tyres for cars, trucks, two-wheelers | 📈 BULL_ANY_MID | 63 | ↑45 | ↑1.028 | ↑2d | SQ | +4.5% | 32.29/25.88 | +1.99% | 20% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>📶W9 · ↑CMF10d</sub> | ✓ SAFE | Optical fiber cables, telecom equipment, defense infrastructure | 📈 BULL_ANY_MID | 58 | ↑100 | ↓1.032 | ↑2d | SQ | +5.5% | 46.16/42.26 | +0.58% | 5% 🟥 |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · ↑CMF29d</sub> | ✓ SAFE | Cryogenic equipment manufacturer for LNG and industrial gas sectors | 📈 BULL_ANY_MID | 58 | ↑93 | ↑1.036 | ↑2d | SQ | +7.7% | 27.78/24.81 | +1.53% | 20% |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE)<br><sub>📶W9 · W↑72d · ↓CMF3d</sub> | ✓ SAFE | Mobile cranes, forklifts, construction equipment manufacturer | 📈 BULL_ANY_MID | 58 | ↑46 | ↓1.014 | ↑2d | SQ | +4.1% | 20.72/18.58 | -0.07% | 20% |
| [INDIGOPNTS](https://in.tradingview.com/chart/?symbol=NSE:INDIGOPNTS)<br><sub>📶W9 · W↑72d · ↑CMF3d</sub> | ✓ SAFE | Decorative paints manufacturer serving residential and commercial construction | 📈 BULL_ANY_MID | 58 | ↑54 | ↓1.008 | ↑2d | SQ | +2.6% | 39.01/36.77 | -1.81% | 20% |
| [TVSSRICHAK](https://in.tradingview.com/chart/?symbol=NSE:TVSSRICHAK)<br><sub>📶W9 · W↑39d · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑63 | ↓1.004 | ↑2d | SQ | +1.4% | 25.19/20.42 | -0.46% | 20% |
| [THYROCARE](https://in.tradingview.com/chart/?symbol=NSE:THYROCARE)<br><sub>📶W9 · ↓CMF17d</sub> | ✓ SAFE | Diagnostic lab tests thyroid endocrine clinical pathology services | 📈 BULL_ANY_MID | 57 | ↓83 | ↓0.995 | ↓3d | SQ | +3.4% | -4.38/-4.99 | -0.57% | 20% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | CDMO services, hospital generics, pharmaceutical manufacturing solutions | 📈 BULL_ANY_MID | 54 | 🔄47 | ↑1.012 | ↑6d | — | +4.0% | 28.4/27.41 | +1.82% | 20% |
| [ALLTIME](https://in.tradingview.com/chart/?symbol=NSE:ALLTIME)<br><sub>📶W9 · W↑24d · 🚀SS · ↓CMF22d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 53 | 🔄50 | ↑1.021 | ↑2d | — | +5.0% | 2.66/-1.43 | +2.17% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>📶W9 · W↑65d · ↓CMF6d</sub> | ✓ SAFE | Pharma formulations acute chronic diseases consumer health | 📈 BULL_ANY_MID | 51 | ↑63 | ↑1.009 | ↑19d | SQ | +7.4% | 47.69/43.74 | +0.35% | 20% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄91 | ↑1.037 | ↑1d | — | +3.4% | -7.35/-13.15 | +3.43% | 20% |
| [INGERRAND](https://in.tradingview.com/chart/?symbol=NSE:INGERRAND)<br><sub>📶W9 · W↑19d · 🚀SS · ↓CMF2d</sub> | ⚠ CAUTION | Air compressors, industrial equipment manufacturing, manufacturing sector | 📈 BULL_ANY_MID | 48 | 🔄75 | ↑1.047 | ↑2d | — | +6.5% | 7.59/-4.53 | +5.58% | 20% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>📶W9 · W↑72d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Generic injectable pharmaceuticals manufacturer regulated markets | 📈 BULL_ANY_MID | 37 | 🔄87 | ↑1.023 | ↑18d | — | +15.7% | 47.0/46.06 | +2.61% | 20% |
| [COSMOFIRST](https://in.tradingview.com/chart/?symbol=NSE:COSMOFIRST)<br><sub>📶W9 · W↑67d · ↑CMF17d</sub> | ✓ SAFE | Specialty films for packaging lamination labeling applications | 📈 BULL_ANY_MID | 35 | 🔄62 | ↑1.024 | ↑23d | — | +15.7% | 42.05/41.78 | +2.33% | 20% |
| [PGIL](https://in.tradingview.com/chart/?symbol=NSE:PGIL)<br><sub>📶W9 · W↑67d · ↑CMF21d</sub> | ✓ SAFE | Apparel manufacturer, exports garments to global fashion brands | 📈 BULL_ANY_MID | 19 | ↑86 | ↑1.018 | ↑6d | — | +5.0% | 43.15/42.22 | +0.49% | 20% |
| [HLEGLAS](https://in.tradingview.com/chart/?symbol=NSE:HLEGLAS)<br><sub>📶W9 · W↑72d · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Glass-lined equipment manufacturer pharmaceutical chemical processing | 📈 BULL_ANY_MID | 18 | ↑62 | ↑1.068 | ↑2d | — | +11.2% | 62.86/60.66 | +4.49% | 20% |
| [EIMCOELECO](https://in.tradingview.com/chart/?symbol=NSE:EIMCOELECO)<br><sub>📶W9 · W↑24d · ↓CMF5d</sub> | ✓ SAFE | Underground mining equipment manufacturer for coal sector | 📈 BULL_ANY_MID | 18 | ↑49 | ↓1.027 | ↑2d | — | +6.0% | 36.62/35.12 | -0.81% | 20% |
| [FINEORG](https://in.tradingview.com/chart/?symbol=NSE:FINEORG)<br><sub>📶W9 · W↑72d · ↓CMF0d</sub> | ⚠ CAUTION | Oleochemical additives for food cosmetics plastics coatings | 📈 BULL_ANY_MID | 18 | ↑55 | ↓1.003 | ↓2d | — | +1.9% | 2.23/0.03 | -0.79% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑63d · ↑CMF16d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.020 | ↑3d | — | +5.4% | 47.71/46.67 | -0.44% | 20% |
| [SWIGGY](https://in.tradingview.com/chart/?symbol=NSE:SWIGGY)<br><sub>📶W9 · W↑24d · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Food delivery and quick commerce marketplace serving Indian consumers | 📈 BULL_ANY_MID | 8 | ↑9 | ↑1.032 | ↑12d | — | +13.3% | 33.16/28.87 | +1.06% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Banking software solutions for financial institutions | 📈 BULL_ANY_MID | 5 | ↑89 | ↑1.055 | ↑15d | — | +20.9% | 50.17/48.27 | +4.64% | 20% |
| [ALKEM](https://in.tradingview.com/chart/?symbol=NSE:ALKEM)<br><sub>📶W9 · W↑14d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Pharma manufacturer: branded generics, APIs, nutraceuticals India | 📈 BULL_ANY_MID | 5 | ↑51 | ↑1.016 | ↑23d | — | +7.0% | 56.54/55.36 | +0.88% | 20% |
| [ADOR](https://in.tradingview.com/chart/?symbol=NSE:ADOR)<br><sub>📶W9 · W↑63d · ↑CMF16d</sub> | ✓ SAFE | Welding equipment and consumables for industrial fabrication | 📈 BULL_ANY_MID | 0 | ↑82 | ↓1.025 | ↑25d | — | +22.0% | 66.25/64.59 | -0.70% | 20% |
| [APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD)<br><sub>📶W9 · W↑24d · ↑CMF13d</sub> | ⚠ CAUTION | Generic drugs and APIs for global markets | 📈 BULL_ANY_MID | 0 | ↑43 | ↓1.015 | ↑23d | — | +13.8% | 58.47/57.44 | -1.21% | 20% |

```
NSE:DEEPAKFERT,NSE:PNBGILTS,NSE:RKFORGE,NSE:ASKAUTOLTD,NSE:BECTORFOOD,NSE:GRINDWELL,NSE:SRF,NSE:EMMVEE,NSE:DIXON,NSE:CYIENTDLM,NSE:SKIPPER,NSE:KIRLFER,NSE:MOLDTKPAC,NSE:HARSHA,NSE:KKCL,NSE:LLOYDSME,NSE:YATHARTH,NSE:PANACEABIO,NSE:JKTYRE,NSE:HFCL,NSE:INOXINDIA,NSE:ACE,NSE:INDIGOPNTS,NSE:TVSSRICHAK,NSE:THYROCARE,NSE:PPLPHARMA,NSE:ALLTIME,NSE:MANKIND,NSE:BHEL,NSE:INGERRAND,NSE:GLAND,NSE:COSMOFIRST,NSE:PGIL,NSE:HLEGLAS,NSE:EIMCOELECO,NSE:FINEORG,NSE:ABCAPITAL,NSE:SWIGGY,NSE:OFSS,NSE:ALKEM,NSE:ADOR,NSE:APLLTD
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (59)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [DEEPAKFERT](https://in.tradingview.com/chart/?symbol=NSE:DEEPAKFERT)<br><sub>📶W9 · W↑89d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Fertilizers, crop nutrition, bulk chemicals, mining sector | ⚡ BULL_ANY_PPV | 94 | 🔄74 | ↑1.026 | ↑1d | SQ·PV | +3.4% | 12.21/8.75 | +3.38% | 20% |
| [PNBGILTS](https://in.tradingview.com/chart/?symbol=NSE:PNBGILTS)<br><sub>📶W9 · W↑67d · ↑CMF0d</sub> | ✓ SAFE | Government securities dealer, primary dealer, debt market | ⚡ BULL_ANY_PPV | 94 | 🔄61 | ↑1.027 | ↑1d | SQ·PV | +4.3% | -12.01/-18.97 | +4.27% | 20% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>📶W9 · W↑4d · 🚀SS·31x · ↑CMF0d</sub> | ✓ SAFE | Precision forged auto, rail, engineering components manufacturer | ⚡ BULL_ANY_PPV | 89 | 🔄55 | ↑1.036 | ↑1d | SQ·PV | +4.7% | -12.41/-20.96 | +4.65% | 20% |
| [ASKAUTOLTD](https://in.tradingview.com/chart/?symbol=NSE:ASKAUTOLTD)<br><sub>📶W9 · W↑24d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Two-wheeler advanced braking systems manufacturer India | ⚡ BULL_ANY_PPV | 52 | ↑48 | ↑1.031 | ↑8d | SQ·PV | +7.0% | 41.35/35.43 | +2.57% | 20% |
| [BECTORFOOD](https://in.tradingview.com/chart/?symbol=NSE:BECTORFOOD)<br><sub>📶W9 · W↑4d · 🚀SS·76x · ↑CMF0d</sub> | ✓ SAFE | Biscuits bakery products FMCG retail consumer branded foods | ⚡ BULL_ANY_PPV | 49 | 🔄14 | ↑1.095 | ↑1d | PV | +13.8% | -30.05/-42.13 | +13.77% | 20% |
| [GRINDWELL](https://in.tradingview.com/chart/?symbol=NSE:GRINDWELL)<br><sub>📶W9 · W↑67d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Grinding wheels, abrasives, ceramics for industrial manufacturing | ⚡ BULL_ANY_PPV | 49 | 🔄90 | ↑1.127 | ↑1d | PV | +16.4% | 9.7/-1.22 | +16.44% | 20% |
| [SRF](https://in.tradingview.com/chart/?symbol=NSE:SRF)<br><sub>📶W9 · W↑63d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Technical textiles, chemicals, films for industrial applications | ⚡ BULL_ANY_PPV | 48 | 🔄48 | ↑1.038 | ↑2d | PV | +5.3% | 36.0/27.31 | +4.10% | 20% |
| [EMMVEE](https://in.tradingview.com/chart/?symbol=NSE:EMMVEE)<br><sub>📶W9 · 🚀SS·9x · ↑CMF0d</sub> | ✓ SAFE | Solar PV modules and cells manufacturing, renewable energy sector | ⚡ BULL_ANY_PPV | 18 | ↑50 | ↑1.063 | ↑2d | PV | +9.1% | 29.84/20.34 | +6.83% | 20% |
| [DIXON](https://in.tradingview.com/chart/?symbol=NSE:DIXON)<br><sub>📶W9 · W↑84d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Consumer electronics contract manufacturing for global brands | ⚡ BULL_ANY_PPV | 9 | ↑65 | ↑1.082 | ↑11d | PV | +21.3% | 67.07/62.79 | +6.27% | 20% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>📶W9 · W↑84d · 🚀SS · ★ · ↑CMF9d</sub> | ✓ SAFE | Electronics manufacturing design integration testing subsystems OEMs | ⚡ BULL_ANY_PPV | 9 | ↑90 | ↑1.101 | ↑11d | PV | +26.4% | 71.75/70.09 | +8.99% | 20% |
| [SKIPPER](https://in.tradingview.com/chart/?symbol=NSE:SKIPPER)<br><sub>📶W9 · W↑79d · ↓CMF17d · ÷DIV</sub> | ✓ SAFE | Steel transmission towers, polymer pipes, infrastructure EPC | 📈 BULL_ANY_MID | 99 | 🔄78 | ↑1.013 | ↑1d | SQ | +2.4% | 13.85/12.82 | +2.37% | 20% |
| [KIRLFER](https://in.tradingview.com/chart/?symbol=NSE:KIRLFER)<br><sub>📶W9 · W↑24d · ↓CMF20d</sub> | ⚠ CAUTION | Pig iron and grey iron castings for automobiles | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.013 | ↑1d | SQ | +2.1% | 2.84/1.65 | +2.14% | 20% |
| [MOLDTKPAC](https://in.tradingview.com/chart/?symbol=NSE:MOLDTKPAC)<br><sub>📶W9 · ↓CMF26d</sub> | ✓ SAFE | Injection-molded plastic containers for automotive lubricants food paints | 📈 BULL_ANY_MID | 99 | 🔄65 | ↑1.015 | ↑1d | SQ | +1.4% | -7.95/-12.54 | +1.44% | 20% |
| [HARSHA](https://in.tradingview.com/chart/?symbol=NSE:HARSHA)<br><sub>📶W9 · W↑72d · ↓CMF30d</sub> | ✓ SAFE | Precision bearing cages, brass steel polyamide components manufacturing | 📈 BULL_ANY_MID | 98 | 🔄57 | ↑1.010 | ↑2d | SQ | +2.6% | 9.54/9.12 | +0.66% | 20% |
| [KKCL](https://in.tradingview.com/chart/?symbol=NSE:KKCL)<br><sub>📶W9 · W↑24d · ↑CMF22d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 98 | 🔄43 | ↑1.010 | ↑2d | SQ | +2.1% | 26.81/24.43 | +0.60% | 20% |
| [LLOYDSME](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSME)<br><sub>📶W9 · 🚀SS · ↓CMF14d</sub> | ✓ SAFE | Iron ore mining, sponge iron production, power generation | 📈 BULL_ANY_MID | 94 | 🔄78 | ↑1.022 | ↑1d | SQ | +3.1% | 6.52/1.69 | +3.12% | 20% |
| [YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Multi-specialty hospital network trauma care Delhi-NCR Madhya Pradesh | 📈 BULL_ANY_MID | 93 | 🔄77 | ↑1.022 | ↑2d | SQ | +3.6% | 8.75/2.44 | +2.14% | 20% |
| [PANACEABIO](https://in.tradingview.com/chart/?symbol=NSE:PANACEABIO)<br><sub>📶W9 · W↑72d · 🚀SS · ↓CMF29d</sub> | ✓ SAFE | Vaccine and pharmaceutical manufacturing biotech company | 📈 BULL_ANY_MID | 89 | 🔄90 | ↑1.033 | ↑1d | SQ | +4.8% | 15.64/11.07 | +4.77% | 10% 🟨 |
| [JKTYRE](https://in.tradingview.com/chart/?symbol=NSE:JKTYRE)<br><sub>📶W9 · W↑19d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Radial tyres for cars, trucks, two-wheelers | 📈 BULL_ANY_MID | 63 | ↑45 | ↑1.028 | ↑2d | SQ | +4.5% | 32.29/25.88 | +1.99% | 20% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>📶W9 · ↑CMF10d</sub> | ✓ SAFE | Optical fiber cables, telecom equipment, defense infrastructure | 📈 BULL_ANY_MID | 58 | ↑100 | ↓1.032 | ↑2d | SQ | +5.5% | 46.16/42.26 | +0.58% | 5% 🟥 |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · ↑CMF29d</sub> | ✓ SAFE | Cryogenic equipment manufacturer for LNG and industrial gas sectors | 📈 BULL_ANY_MID | 58 | ↑93 | ↑1.036 | ↑2d | SQ | +7.7% | 27.78/24.81 | +1.53% | 20% |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE)<br><sub>📶W9 · W↑72d · ↓CMF3d</sub> | ✓ SAFE | Mobile cranes, forklifts, construction equipment manufacturer | 📈 BULL_ANY_MID | 58 | ↑46 | ↓1.014 | ↑2d | SQ | +4.1% | 20.72/18.58 | -0.07% | 20% |
| [INDIGOPNTS](https://in.tradingview.com/chart/?symbol=NSE:INDIGOPNTS)<br><sub>📶W9 · W↑72d · ↑CMF3d</sub> | ✓ SAFE | Decorative paints manufacturer serving residential and commercial construction | 📈 BULL_ANY_MID | 58 | ↑54 | ↓1.008 | ↑2d | SQ | +2.6% | 39.01/36.77 | -1.81% | 20% |
| [TVSSRICHAK](https://in.tradingview.com/chart/?symbol=NSE:TVSSRICHAK)<br><sub>📶W9 · W↑39d · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑63 | ↓1.004 | ↑2d | SQ | +1.4% | 25.19/20.42 | -0.46% | 20% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | CDMO services, hospital generics, pharmaceutical manufacturing solutions | 📈 BULL_ANY_MID | 54 | 🔄47 | ↑1.012 | ↑6d | — | +4.0% | 28.4/27.41 | +1.82% | 20% |
| [ALLTIME](https://in.tradingview.com/chart/?symbol=NSE:ALLTIME)<br><sub>📶W9 · W↑24d · 🚀SS · ↓CMF22d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 53 | 🔄50 | ↑1.021 | ↑2d | — | +5.0% | 2.66/-1.43 | +2.17% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>📶W9 · W↑65d · ↓CMF6d</sub> | ✓ SAFE | Pharma formulations acute chronic diseases consumer health | 📈 BULL_ANY_MID | 51 | ↑63 | ↑1.009 | ↑19d | SQ | +7.4% | 47.69/43.74 | +0.35% | 20% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄91 | ↑1.037 | ↑1d | — | +3.4% | -7.35/-13.15 | +3.43% | 20% |
| [INGERRAND](https://in.tradingview.com/chart/?symbol=NSE:INGERRAND)<br><sub>📶W9 · W↑19d · 🚀SS · ↓CMF2d</sub> | ⚠ CAUTION | Air compressors, industrial equipment manufacturing, manufacturing sector | 📈 BULL_ANY_MID | 48 | 🔄75 | ↑1.047 | ↑2d | — | +6.5% | 7.59/-4.53 | +5.58% | 20% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>📶W9 · W↑72d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Generic injectable pharmaceuticals manufacturer regulated markets | 📈 BULL_ANY_MID | 37 | 🔄87 | ↑1.023 | ↑18d | — | +15.7% | 47.0/46.06 | +2.61% | 20% |
| [COSMOFIRST](https://in.tradingview.com/chart/?symbol=NSE:COSMOFIRST)<br><sub>📶W9 · W↑67d · ↑CMF17d</sub> | ✓ SAFE | Specialty films for packaging lamination labeling applications | 📈 BULL_ANY_MID | 35 | 🔄62 | ↑1.024 | ↑23d | — | +15.7% | 42.05/41.78 | +2.33% | 20% |
| [PGIL](https://in.tradingview.com/chart/?symbol=NSE:PGIL)<br><sub>📶W9 · W↑67d · ↑CMF21d</sub> | ✓ SAFE | Apparel manufacturer, exports garments to global fashion brands | 📈 BULL_ANY_MID | 19 | ↑86 | ↑1.018 | ↑6d | — | +5.0% | 43.15/42.22 | +0.49% | 20% |
| [HLEGLAS](https://in.tradingview.com/chart/?symbol=NSE:HLEGLAS)<br><sub>📶W9 · W↑72d · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Glass-lined equipment manufacturer pharmaceutical chemical processing | 📈 BULL_ANY_MID | 18 | ↑62 | ↑1.068 | ↑2d | — | +11.2% | 62.86/60.66 | +4.49% | 20% |
| [EIMCOELECO](https://in.tradingview.com/chart/?symbol=NSE:EIMCOELECO)<br><sub>📶W9 · W↑24d · ↓CMF5d</sub> | ✓ SAFE | Underground mining equipment manufacturer for coal sector | 📈 BULL_ANY_MID | 18 | ↑49 | ↓1.027 | ↑2d | — | +6.0% | 36.62/35.12 | -0.81% | 20% |
| [FINEORG](https://in.tradingview.com/chart/?symbol=NSE:FINEORG)<br><sub>📶W9 · W↑72d · ↓CMF0d</sub> | ⚠ CAUTION | Oleochemical additives for food cosmetics plastics coatings | 📈 BULL_ANY_MID | 18 | ↑55 | ↓1.003 | ↓2d | — | +1.9% | 2.23/0.03 | -0.79% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑63d · ↑CMF16d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.020 | ↑3d | — | +5.4% | 47.71/46.67 | -0.44% | 20% |
| [SWIGGY](https://in.tradingview.com/chart/?symbol=NSE:SWIGGY)<br><sub>📶W9 · W↑24d · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Food delivery and quick commerce marketplace serving Indian consumers | 📈 BULL_ANY_MID | 8 | ↑9 | ↑1.032 | ↑12d | — | +13.3% | 33.16/28.87 | +1.06% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Banking software solutions for financial institutions | 📈 BULL_ANY_MID | 5 | ↑89 | ↑1.055 | ↑15d | — | +20.9% | 50.17/48.27 | +4.64% | 20% |
| [ALKEM](https://in.tradingview.com/chart/?symbol=NSE:ALKEM)<br><sub>📶W9 · W↑14d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Pharma manufacturer: branded generics, APIs, nutraceuticals India | 📈 BULL_ANY_MID | 5 | ↑51 | ↑1.016 | ↑23d | — | +7.0% | 56.54/55.36 | +0.88% | 20% |
| [ADOR](https://in.tradingview.com/chart/?symbol=NSE:ADOR)<br><sub>📶W9 · W↑63d · ↑CMF16d</sub> | ✓ SAFE | Welding equipment and consumables for industrial fabrication | 📈 BULL_ANY_MID | 0 | ↑82 | ↓1.025 | ↑25d | — | +22.0% | 66.25/64.59 | -0.70% | 20% |
| [APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD)<br><sub>📶W9 · W↑24d · ↑CMF13d</sub> | ⚠ CAUTION | Generic drugs and APIs for global markets | 📈 BULL_ANY_MID | 0 | ↑43 | ↓1.015 | ↑23d | — | +13.8% | 58.47/57.44 | -1.21% | 20% |
| [KAYNES](https://in.tradingview.com/chart/?symbol=NSE:KAYNES)<br><sub>W↑14d · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Electronics manufacturing IoT solutions design engineering | ⚡ BULL_ANY_PPV | 54 | ↑3 | ↑1.034 | ↑6d | SQ·PV | +7.1% | 33.78/26.53 | +3.04% | 20% |
| [IEX](https://in.tradingview.com/chart/?symbol=NSE:IEX)<br><sub>🚀SS · ↑CMF0d</sub> | ✓ SAFE | Electricity trading platform physical delivery certificates | ⚡ BULL_ANY_PPV | 49 | 🔄18 | ↑1.033 | ↑1d | PV | +4.9% | -38.17/-46.62 | +4.92% | 20% |
| [GNFC](https://in.tradingview.com/chart/?symbol=NSE:GNFC)<br><sub>🚀SS · ↓CMF20d</sub> | ✓ SAFE | Urea ammonia fertilizers chemicals industrial farmers | ⚡ BULL_ANY_PPV | 40 | 🔄51 | ↑1.006 | ↓25d | PV | +4.4% | -34.78/-35.52 | +2.90% | 20% |
| [GODFRYPHLP](https://in.tradingview.com/chart/?symbol=NSE:GODFRYPHLP)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Cigarettes and tobacco products for Indian consumers | 🟢 BULL_OVERSOLD | 40 | 🔄16 | ↑1.002 | ↓21d | — | -5.7% | -57.05/-60.67 | +1.76% | 20% |
| [CESC](https://in.tradingview.com/chart/?symbol=NSE:CESC)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Power generation and distribution utility serving eastern India | 🟡 BULL_OS_L2 | 59 | 🔄37 | ↑1.009 | ↑1d | — | +1.5% | -54.33/-58.31 | +1.51% | 20% |
| [HINDPETRO](https://in.tradingview.com/chart/?symbol=NSE:HINDPETRO)<br><sub>W↑63d · 🚀SS · ↓CMF22d</sub> | ✓ SAFE | Crude refining, fuel distribution, petrochemicals for domestic consumers | 📈 BULL_ANY_MID | 99 | 🔄34 | ↑1.012 | ↑1d | SQ | +1.3% | -6.21/-10.34 | +1.27% | 20% |
| [LINDEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LINDEINDIA)<br><sub>🚀SS · ↓CMF1d</sub> | ⚠ CAUTION | Industrial medical gases cryogenic plants manufacturing India | 📈 BULL_ANY_MID | 99 | 🔄57 | ↑1.005 | ↑1d | SQ | +1.4% | -17.67/-18.16 | +1.42% | 20% |
| [VHL](https://in.tradingview.com/chart/?symbol=NSE:VHL)<br><sub>W↑24d · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄39 | ↑1.004 | ↑1d | SQ | +0.5% | 0.14/-0.26 | +0.49% | 20% |
| [BAYERCROP](https://in.tradingview.com/chart/?symbol=NSE:BAYERCROP)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Crop protection chemicals seeds insecticides fungicides herbicides agriculture | 📈 BULL_ANY_MID | 94 | 🔄12 | ↑1.019 | ↑1d | SQ | +2.7% | -36.7/-44.78 | +2.69% | 20% |
| [CIEINDIA](https://in.tradingview.com/chart/?symbol=NSE:CIEINDIA)<br><sub>W↑19d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Automotive components supplier for global OEMs | 📈 BULL_ANY_MID | 94 | 🔄55 | ↑1.017 | ↑1d | SQ | +2.5% | 7.96/3.72 | +2.49% | 20% |
| [JKCEMENT](https://in.tradingview.com/chart/?symbol=NSE:JKCEMENT)<br><sub>W↑19d · 🚀SS · ↓CMF3d</sub> | ⚠ CAUTION | Cement manufacturing for construction and infrastructure applications | 📈 BULL_ANY_MID | 88 | 🔄21 | ↓1.004 | ↑2d | SQ | +1.4% | -0.85/-3.8 | +0.07% | 20% |
| [FORCEMOT](https://in.tradingview.com/chart/?symbol=NSE:FORCEMOT)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Small commercial vehicles, vans, tractors, automotive components | 📈 BULL_ANY_MID | 68 | ↑38 | ↑1.013 | ↑2d | SQ | +4.8% | -12.37/-16.98 | +0.40% | 20% |
| [PNB](https://in.tradingview.com/chart/?symbol=NSE:PNB)<br><sub>W↑25d · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | 🔄24 | ↑1.012 | ↑2d | — | +2.9% | -19.58/-24.31 | +0.94% | 20% |
| [JSWDULUX](https://in.tradingview.com/chart/?symbol=NSE:JSWDULUX)<br><sub>↓CMF14d</sub> | ⚠ CAUTION | Decorative and industrial paints manufacturing for buildings | 📈 BULL_ANY_MID | 54 | 🔄37 | ↑1.016 | ↑1d | — | +4.5% | -31.91/-32.75 | +4.48% | 20% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>🚀SS · ↑CMF4d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄94 | ↑1.031 | ↑1d | — | +4.5% | -28.4/-34.25 | +4.45% | 20% |
| [UNIONBANK](https://in.tradingview.com/chart/?symbol=NSE:UNIONBANK)<br><sub>↑CMF1d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄50 | ↑1.036 | ↑1d | — | +3.7% | -21.82/-27.26 | +3.73% | 20% |
| [UNOMINDA](https://in.tradingview.com/chart/?symbol=NSE:UNOMINDA)<br><sub>W↑19d · ↓CMF6d</sub> | ✓ SAFE | Automotive components supplier to Indian and global OEMs | 📈 BULL_ANY_MID | 49 | ↑42 | ↓1.007 | ↑11d | SQ | +5.7% | 43.74/43.63 | -0.61% | 20% |
| [ENRIN](https://in.tradingview.com/chart/?symbol=NSE:ENRIN)<br><sub>🚀SS · ↓CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 40 | 🔄73 | ↑1.009 | ↓21d | — | -1.4% | -25.75/-26.7 | +3.26% | 20% |

```
NSE:DEEPAKFERT,NSE:PNBGILTS,NSE:RKFORGE,NSE:ASKAUTOLTD,NSE:BECTORFOOD,NSE:GRINDWELL,NSE:SRF,NSE:EMMVEE,NSE:DIXON,NSE:CYIENTDLM,NSE:SKIPPER,NSE:KIRLFER,NSE:MOLDTKPAC,NSE:HARSHA,NSE:KKCL,NSE:LLOYDSME,NSE:YATHARTH,NSE:PANACEABIO,NSE:JKTYRE,NSE:HFCL,NSE:INOXINDIA,NSE:ACE,NSE:INDIGOPNTS,NSE:TVSSRICHAK,NSE:PPLPHARMA,NSE:ALLTIME,NSE:MANKIND,NSE:BHEL,NSE:INGERRAND,NSE:GLAND,NSE:COSMOFIRST,NSE:PGIL,NSE:HLEGLAS,NSE:EIMCOELECO,NSE:FINEORG,NSE:ABCAPITAL,NSE:SWIGGY,NSE:OFSS,NSE:ALKEM,NSE:ADOR,NSE:APLLTD,NSE:KAYNES,NSE:IEX,NSE:GNFC,NSE:GODFRYPHLP,NSE:CESC,NSE:HINDPETRO,NSE:LINDEINDIA,NSE:VHL,NSE:BAYERCROP,NSE:CIEINDIA,NSE:JKCEMENT,NSE:FORCEMOT,NSE:PNB,NSE:JSWDULUX,NSE:POWERINDIA,NSE:UNIONBANK,NSE:UNOMINDA,NSE:ENRIN
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (35)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [DEEPAKFERT](https://in.tradingview.com/chart/?symbol=NSE:DEEPAKFERT)<br><sub>📶W9 · W↑89d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Fertilizers, crop nutrition, bulk chemicals, mining sector | ⚡ BULL_ANY_PPV | 94 | 🔄74 | ↑1.026 | ↑1d | SQ·PV | +3.4% | 12.21/8.75 | +3.38% | 20% |
| [PNBGILTS](https://in.tradingview.com/chart/?symbol=NSE:PNBGILTS)<br><sub>📶W9 · W↑67d · ↑CMF0d</sub> | ✓ SAFE | Government securities dealer, primary dealer, debt market | ⚡ BULL_ANY_PPV | 94 | 🔄61 | ↑1.027 | ↑1d | SQ·PV | +4.3% | -12.01/-18.97 | +4.27% | 20% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>📶W9 · W↑4d · 🚀SS·31x · ↑CMF0d</sub> | ✓ SAFE | Precision forged auto, rail, engineering components manufacturer | ⚡ BULL_ANY_PPV | 89 | 🔄55 | ↑1.036 | ↑1d | SQ·PV | +4.7% | -12.41/-20.96 | +4.65% | 20% |
| [ASKAUTOLTD](https://in.tradingview.com/chart/?symbol=NSE:ASKAUTOLTD)<br><sub>📶W9 · W↑24d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Two-wheeler advanced braking systems manufacturer India | ⚡ BULL_ANY_PPV | 52 | ↑48 | ↑1.031 | ↑8d | SQ·PV | +7.0% | 41.35/35.43 | +2.57% | 20% |
| [SKIPPER](https://in.tradingview.com/chart/?symbol=NSE:SKIPPER)<br><sub>📶W9 · W↑79d · ↓CMF17d · ÷DIV</sub> | ✓ SAFE | Steel transmission towers, polymer pipes, infrastructure EPC | 📈 BULL_ANY_MID | 99 | 🔄78 | ↑1.013 | ↑1d | SQ | +2.4% | 13.85/12.82 | +2.37% | 20% |
| [KIRLFER](https://in.tradingview.com/chart/?symbol=NSE:KIRLFER)<br><sub>📶W9 · W↑24d · ↓CMF20d</sub> | ⚠ CAUTION | Pig iron and grey iron castings for automobiles | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.013 | ↑1d | SQ | +2.1% | 2.84/1.65 | +2.14% | 20% |
| [MOLDTKPAC](https://in.tradingview.com/chart/?symbol=NSE:MOLDTKPAC)<br><sub>📶W9 · ↓CMF26d</sub> | ✓ SAFE | Injection-molded plastic containers for automotive lubricants food paints | 📈 BULL_ANY_MID | 99 | 🔄65 | ↑1.015 | ↑1d | SQ | +1.4% | -7.95/-12.54 | +1.44% | 20% |
| [HARSHA](https://in.tradingview.com/chart/?symbol=NSE:HARSHA)<br><sub>📶W9 · W↑72d · ↓CMF30d</sub> | ✓ SAFE | Precision bearing cages, brass steel polyamide components manufacturing | 📈 BULL_ANY_MID | 98 | 🔄57 | ↑1.010 | ↑2d | SQ | +2.6% | 9.54/9.12 | +0.66% | 20% |
| [KKCL](https://in.tradingview.com/chart/?symbol=NSE:KKCL)<br><sub>📶W9 · W↑24d · ↑CMF22d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 98 | 🔄43 | ↑1.010 | ↑2d | SQ | +2.1% | 26.81/24.43 | +0.60% | 20% |
| [LLOYDSME](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSME)<br><sub>📶W9 · 🚀SS · ↓CMF14d</sub> | ✓ SAFE | Iron ore mining, sponge iron production, power generation | 📈 BULL_ANY_MID | 94 | 🔄78 | ↑1.022 | ↑1d | SQ | +3.1% | 6.52/1.69 | +3.12% | 20% |
| [YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Multi-specialty hospital network trauma care Delhi-NCR Madhya Pradesh | 📈 BULL_ANY_MID | 93 | 🔄77 | ↑1.022 | ↑2d | SQ | +3.6% | 8.75/2.44 | +2.14% | 20% |
| [PANACEABIO](https://in.tradingview.com/chart/?symbol=NSE:PANACEABIO)<br><sub>📶W9 · W↑72d · 🚀SS · ↓CMF29d</sub> | ✓ SAFE | Vaccine and pharmaceutical manufacturing biotech company | 📈 BULL_ANY_MID | 89 | 🔄90 | ↑1.033 | ↑1d | SQ | +4.8% | 15.64/11.07 | +4.77% | 10% 🟨 |
| [JKTYRE](https://in.tradingview.com/chart/?symbol=NSE:JKTYRE)<br><sub>📶W9 · W↑19d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Radial tyres for cars, trucks, two-wheelers | 📈 BULL_ANY_MID | 63 | ↑45 | ↑1.028 | ↑2d | SQ | +4.5% | 32.29/25.88 | +1.99% | 20% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>📶W9 · ↑CMF10d</sub> | ✓ SAFE | Optical fiber cables, telecom equipment, defense infrastructure | 📈 BULL_ANY_MID | 58 | ↑100 | ↓1.032 | ↑2d | SQ | +5.5% | 46.16/42.26 | +0.58% | 5% 🟥 |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · ↑CMF29d</sub> | ✓ SAFE | Cryogenic equipment manufacturer for LNG and industrial gas sectors | 📈 BULL_ANY_MID | 58 | ↑93 | ↑1.036 | ↑2d | SQ | +7.7% | 27.78/24.81 | +1.53% | 20% |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE)<br><sub>📶W9 · W↑72d · ↓CMF3d</sub> | ✓ SAFE | Mobile cranes, forklifts, construction equipment manufacturer | 📈 BULL_ANY_MID | 58 | ↑46 | ↓1.014 | ↑2d | SQ | +4.1% | 20.72/18.58 | -0.07% | 20% |
| [INDIGOPNTS](https://in.tradingview.com/chart/?symbol=NSE:INDIGOPNTS)<br><sub>📶W9 · W↑72d · ↑CMF3d</sub> | ✓ SAFE | Decorative paints manufacturer serving residential and commercial construction | 📈 BULL_ANY_MID | 58 | ↑54 | ↓1.008 | ↑2d | SQ | +2.6% | 39.01/36.77 | -1.81% | 20% |
| [TVSSRICHAK](https://in.tradingview.com/chart/?symbol=NSE:TVSSRICHAK)<br><sub>📶W9 · W↑39d · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑63 | ↓1.004 | ↑2d | SQ | +1.4% | 25.19/20.42 | -0.46% | 20% |
| [THYROCARE](https://in.tradingview.com/chart/?symbol=NSE:THYROCARE)<br><sub>📶W9 · ↓CMF17d</sub> | ✓ SAFE | Diagnostic lab tests thyroid endocrine clinical pathology services | 📈 BULL_ANY_MID | 57 | ↓83 | ↓0.995 | ↓3d | SQ | +3.4% | -4.38/-4.99 | -0.57% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>📶W9 · W↑65d · ↓CMF6d</sub> | ✓ SAFE | Pharma formulations acute chronic diseases consumer health | 📈 BULL_ANY_MID | 51 | ↑63 | ↑1.009 | ↑19d | SQ | +7.4% | 47.69/43.74 | +0.35% | 20% |
| [KAYNES](https://in.tradingview.com/chart/?symbol=NSE:KAYNES)<br><sub>W↑14d · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Electronics manufacturing IoT solutions design engineering | ⚡ BULL_ANY_PPV | 54 | ↑3 | ↑1.034 | ↑6d | SQ·PV | +7.1% | 33.78/26.53 | +3.04% | 20% |
| [HINDPETRO](https://in.tradingview.com/chart/?symbol=NSE:HINDPETRO)<br><sub>W↑63d · 🚀SS · ↓CMF22d</sub> | ✓ SAFE | Crude refining, fuel distribution, petrochemicals for domestic consumers | 📈 BULL_ANY_MID | 99 | 🔄34 | ↑1.012 | ↑1d | SQ | +1.3% | -6.21/-10.34 | +1.27% | 20% |
| [LINDEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LINDEINDIA)<br><sub>🚀SS · ↓CMF1d</sub> | ⚠ CAUTION | Industrial medical gases cryogenic plants manufacturing India | 📈 BULL_ANY_MID | 99 | 🔄57 | ↑1.005 | ↑1d | SQ | +1.4% | -17.67/-18.16 | +1.42% | 20% |
| [VHL](https://in.tradingview.com/chart/?symbol=NSE:VHL)<br><sub>W↑24d · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄39 | ↑1.004 | ↑1d | SQ | +0.5% | 0.14/-0.26 | +0.49% | 20% |
| [BAYERCROP](https://in.tradingview.com/chart/?symbol=NSE:BAYERCROP)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Crop protection chemicals seeds insecticides fungicides herbicides agriculture | 📈 BULL_ANY_MID | 94 | 🔄12 | ↑1.019 | ↑1d | SQ | +2.7% | -36.7/-44.78 | +2.69% | 20% |
| [CIEINDIA](https://in.tradingview.com/chart/?symbol=NSE:CIEINDIA)<br><sub>W↑19d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Automotive components supplier for global OEMs | 📈 BULL_ANY_MID | 94 | 🔄55 | ↑1.017 | ↑1d | SQ | +2.5% | 7.96/3.72 | +2.49% | 20% |
| [JKCEMENT](https://in.tradingview.com/chart/?symbol=NSE:JKCEMENT)<br><sub>W↑19d · 🚀SS · ↓CMF3d</sub> | ⚠ CAUTION | Cement manufacturing for construction and infrastructure applications | 📈 BULL_ANY_MID | 88 | 🔄21 | ↓1.004 | ↑2d | SQ | +1.4% | -0.85/-3.8 | +0.07% | 20% |
| [CASTROLIND](https://in.tradingview.com/chart/?symbol=NSE:CASTROLIND)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Automotive and industrial lubricants manufacturer, bp subsidiary | 📈 BULL_ANY_MID | 69 | ↓36 | ↑1.003 | ↑1d | SQ | +0.4% | -22.08/-24.8 | +0.43% | 20% |
| [FORCEMOT](https://in.tradingview.com/chart/?symbol=NSE:FORCEMOT)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Small commercial vehicles, vans, tractors, automotive components | 📈 BULL_ANY_MID | 68 | ↑38 | ↑1.013 | ↑2d | SQ | +4.8% | -12.37/-16.98 | +0.40% | 20% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Drug development, manufacturing services for pharma companies | 📈 BULL_ANY_MID | 61 | ↓50 | ↑1.003 | ↓9d | SQ | -1.6% | -43.44/-44.69 | +1.09% | 20% |
| [ANGELONE](https://in.tradingview.com/chart/?symbol=NSE:ANGELONE)<br><sub>↓CMF3d</sub> | ✓ SAFE | Retail stock broking, commodities, mobile-first trading app | 📈 BULL_ANY_MID | 58 | ↓77 | ↓0.987 | ↓2d | SQ | +0.4% | 0.69/0.31 | -2.50% | 20% |
| [LTFOODS](https://in.tradingview.com/chart/?symbol=NSE:LTFOODS)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Specialty rice producer rice-based foods global FMCG | 📈 BULL_ANY_MID | 58 | ↓25 | ↓0.998 | ↑2d | SQ | +0.5% | 7.58/7.08 | -1.02% | 20% |
| [JSLL](https://in.tradingview.com/chart/?symbol=NSE:JSLL)<br><sub>↑CMF2d · ⚠️TRAP</sub> | ✓ SAFE | Ayurvedic hospitals and wellness clinics serving Indian patients | 📈 BULL_ANY_MID | 58 | ↓16 | ↓0.998 | ↓2d | SQ | +1.8% | -23.45/-24.63 | -0.61% | 20% |
| [AMBUJACEM](https://in.tradingview.com/chart/?symbol=NSE:AMBUJACEM)<br><sub>W↑15d · ↑CMF5d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↓10 | ↓1.004 | ↑3d | SQ | +2.7% | 15.62/14.01 | -0.88% | 20% |
| [UNOMINDA](https://in.tradingview.com/chart/?symbol=NSE:UNOMINDA)<br><sub>W↑19d · ↓CMF6d</sub> | ✓ SAFE | Automotive components supplier to Indian and global OEMs | 📈 BULL_ANY_MID | 49 | ↑42 | ↓1.007 | ↑11d | SQ | +5.7% | 43.74/43.63 | -0.61% | 20% |

```
NSE:DEEPAKFERT,NSE:PNBGILTS,NSE:RKFORGE,NSE:ASKAUTOLTD,NSE:SKIPPER,NSE:KIRLFER,NSE:MOLDTKPAC,NSE:HARSHA,NSE:KKCL,NSE:LLOYDSME,NSE:YATHARTH,NSE:PANACEABIO,NSE:JKTYRE,NSE:HFCL,NSE:INOXINDIA,NSE:ACE,NSE:INDIGOPNTS,NSE:TVSSRICHAK,NSE:THYROCARE,NSE:MANKIND,NSE:KAYNES,NSE:HINDPETRO,NSE:LINDEINDIA,NSE:VHL,NSE:BAYERCROP,NSE:CIEINDIA,NSE:JKCEMENT,NSE:CASTROLIND,NSE:FORCEMOT,NSE:ANTHEM,NSE:ANGELONE,NSE:LTFOODS,NSE:JSLL,NSE:AMBUJACEM,NSE:UNOMINDA
```

---

### 🔥 MAJOR — PPV confirmed (12)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [BECTORFOOD](https://in.tradingview.com/chart/?symbol=NSE:BECTORFOOD)<br><sub>📶W9 · W↑4d · 🚀SS·76x · ↑CMF0d</sub> | ✓ SAFE | Biscuits bakery products FMCG retail consumer branded foods | ⚡ BULL_ANY_PPV | 49 | 🔄14 | ↑1.095 | ↑1d | PV | +13.8% | -30.05/-42.13 | +13.77% | 20% |
| [GRINDWELL](https://in.tradingview.com/chart/?symbol=NSE:GRINDWELL)<br><sub>📶W9 · W↑67d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Grinding wheels, abrasives, ceramics for industrial manufacturing | ⚡ BULL_ANY_PPV | 49 | 🔄90 | ↑1.127 | ↑1d | PV | +16.4% | 9.7/-1.22 | +16.44% | 20% |
| [SRF](https://in.tradingview.com/chart/?symbol=NSE:SRF)<br><sub>📶W9 · W↑63d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Technical textiles, chemicals, films for industrial applications | ⚡ BULL_ANY_PPV | 48 | 🔄48 | ↑1.038 | ↑2d | PV | +5.3% | 36.0/27.31 | +4.10% | 20% |
| [EMMVEE](https://in.tradingview.com/chart/?symbol=NSE:EMMVEE)<br><sub>📶W9 · 🚀SS·9x · ↑CMF0d</sub> | ✓ SAFE | Solar PV modules and cells manufacturing, renewable energy sector | ⚡ BULL_ANY_PPV | 18 | ↑50 | ↑1.063 | ↑2d | PV | +9.1% | 29.84/20.34 | +6.83% | 20% |
| [DIXON](https://in.tradingview.com/chart/?symbol=NSE:DIXON)<br><sub>📶W9 · W↑84d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Consumer electronics contract manufacturing for global brands | ⚡ BULL_ANY_PPV | 9 | ↑65 | ↑1.082 | ↑11d | PV | +21.3% | 67.07/62.79 | +6.27% | 20% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>📶W9 · W↑84d · 🚀SS · ★ · ↑CMF9d</sub> | ✓ SAFE | Electronics manufacturing design integration testing subsystems OEMs | ⚡ BULL_ANY_PPV | 9 | ↑90 | ↑1.101 | ↑11d | PV | +26.4% | 71.75/70.09 | +8.99% | 20% |
| [IEX](https://in.tradingview.com/chart/?symbol=NSE:IEX)<br><sub>🚀SS · ↑CMF0d</sub> | ✓ SAFE | Electricity trading platform physical delivery certificates | ⚡ BULL_ANY_PPV | 49 | 🔄18 | ↑1.033 | ↑1d | PV | +4.9% | -38.17/-46.62 | +4.92% | 20% |
| [GNFC](https://in.tradingview.com/chart/?symbol=NSE:GNFC)<br><sub>🚀SS · ↓CMF20d</sub> | ✓ SAFE | Urea ammonia fertilizers chemicals industrial farmers | ⚡ BULL_ANY_PPV | 40 | 🔄51 | ↑1.006 | ↓25d | PV | +4.4% | -34.78/-35.52 | +2.90% | 20% |
| [WEBELSOLAR](https://in.tradingview.com/chart/?symbol=NSE:WEBELSOLAR)<br><sub>🚀SS · ↓CMF12d · ÷DIV</sub> | ✓ SAFE | Solar PV cells modules manufacturing renewable energy sector | ⚡ BULL_ANY_PPV | 14 | ↓43 | ↑0.993 | ↓11d | PV | -1.5% | -40.2/-40.98 | +1.13% | 5% 🟥 |
| [IPL](https://in.tradingview.com/chart/?symbol=NSE:IPL)<br><sub>🚀SS·17x · ↓CMF30d</sub> | ✓ SAFE | Agrochemical manufacturer crop protection pesticides farming | ⚡ BULL_ANY_PPV | 13 | ↓21 | ↑0.998 | ↓12d | PV | -3.1% | -31.29/-37.42 | +0.93% | 20% |
| [IGL](https://in.tradingview.com/chart/?symbol=NSE:IGL)<br><sub>↓CMF13d</sub> | ✓ SAFE | Natural gas distribution Delhi NCR transport domestic industrial | ⚡ BULL_ANY_PPV | 5 | ↓10 | ↑0.999 | ↓25d | PV | -4.2% | -33.21/-35.51 | +1.61% | 20% |
| [SANOFICONR](https://in.tradingview.com/chart/?symbol=NSE:SANOFICONR)<br><sub>🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 5 | ↓37 | ↑0.998 | ↓24d | PV | -1.3% | -40.42/-40.55 | +0.77% | 20% |

```
NSE:BECTORFOOD,NSE:GRINDWELL,NSE:SRF,NSE:EMMVEE,NSE:DIXON,NSE:CYIENTDLM,NSE:IEX,NSE:GNFC,NSE:WEBELSOLAR,NSE:IPL,NSE:IGL,NSE:SANOFICONR
```

### 🟢 OVERSOLD — reversal from −53/−60 (5)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GODFRYPHLP](https://in.tradingview.com/chart/?symbol=NSE:GODFRYPHLP)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Cigarettes and tobacco products for Indian consumers | 🟢 BULL_OVERSOLD | 40 | 🔄16 | ↑1.002 | ↓21d | — | -5.7% | -57.05/-60.67 | +1.76% | 20% |
| [BLS](https://in.tradingview.com/chart/?symbol=NSE:BLS)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Visa passport consular services outsourcing government | 🟢 BULL_OVERSOLD | 5 | ↓5 | ↑0.987 | ↓24d | — | -9.2% | -60.83/-63.94 | +0.89% | 20% |
| [CESC](https://in.tradingview.com/chart/?symbol=NSE:CESC)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Power generation and distribution utility serving eastern India | 🟡 BULL_OS_L2 | 59 | 🔄37 | ↑1.009 | ↑1d | — | +1.5% | -54.33/-58.31 | +1.51% | 20% |
| [SUNTV](https://in.tradingview.com/chart/?symbol=NSE:SUNTV)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Regional broadcaster, Tamil Nadu, multi-lingual entertainment channels | 🟡 BULL_OS_L2 | 14 | ↓11 | ↑0.998 | ↓11d | — | -2.0% | -57.79/-58.5 | +1.06% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>↓CMF9d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 5 | ↓51 | ↑0.994 | ↓30d | — | -5.9% | -54.87/-55.01 | +0.38% | 20% |

```
NSE:GODFRYPHLP,NSE:BLS,NSE:CESC,NSE:SUNTV,NSE:COALINDIA
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (30)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | CDMO services, hospital generics, pharmaceutical manufacturing solutions | 📈 BULL_ANY_MID | 54 | 🔄47 | ↑1.012 | ↑6d | — | +4.0% | 28.4/27.41 | +1.82% | 20% |
| [ALLTIME](https://in.tradingview.com/chart/?symbol=NSE:ALLTIME)<br><sub>📶W9 · W↑24d · 🚀SS · ↓CMF22d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 53 | 🔄50 | ↑1.021 | ↑2d | — | +5.0% | 2.66/-1.43 | +2.17% | 20% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄91 | ↑1.037 | ↑1d | — | +3.4% | -7.35/-13.15 | +3.43% | 20% |
| [INGERRAND](https://in.tradingview.com/chart/?symbol=NSE:INGERRAND)<br><sub>📶W9 · W↑19d · 🚀SS · ↓CMF2d</sub> | ⚠ CAUTION | Air compressors, industrial equipment manufacturing, manufacturing sector | 📈 BULL_ANY_MID | 48 | 🔄75 | ↑1.047 | ↑2d | — | +6.5% | 7.59/-4.53 | +5.58% | 20% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>📶W9 · W↑72d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Generic injectable pharmaceuticals manufacturer regulated markets | 📈 BULL_ANY_MID | 37 | 🔄87 | ↑1.023 | ↑18d | — | +15.7% | 47.0/46.06 | +2.61% | 20% |
| [COSMOFIRST](https://in.tradingview.com/chart/?symbol=NSE:COSMOFIRST)<br><sub>📶W9 · W↑67d · ↑CMF17d</sub> | ✓ SAFE | Specialty films for packaging lamination labeling applications | 📈 BULL_ANY_MID | 35 | 🔄62 | ↑1.024 | ↑23d | — | +15.7% | 42.05/41.78 | +2.33% | 20% |
| [PGIL](https://in.tradingview.com/chart/?symbol=NSE:PGIL)<br><sub>📶W9 · W↑67d · ↑CMF21d</sub> | ✓ SAFE | Apparel manufacturer, exports garments to global fashion brands | 📈 BULL_ANY_MID | 19 | ↑86 | ↑1.018 | ↑6d | — | +5.0% | 43.15/42.22 | +0.49% | 20% |
| [HLEGLAS](https://in.tradingview.com/chart/?symbol=NSE:HLEGLAS)<br><sub>📶W9 · W↑72d · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Glass-lined equipment manufacturer pharmaceutical chemical processing | 📈 BULL_ANY_MID | 18 | ↑62 | ↑1.068 | ↑2d | — | +11.2% | 62.86/60.66 | +4.49% | 20% |
| [EIMCOELECO](https://in.tradingview.com/chart/?symbol=NSE:EIMCOELECO)<br><sub>📶W9 · W↑24d · ↓CMF5d</sub> | ✓ SAFE | Underground mining equipment manufacturer for coal sector | 📈 BULL_ANY_MID | 18 | ↑49 | ↓1.027 | ↑2d | — | +6.0% | 36.62/35.12 | -0.81% | 20% |
| [FINEORG](https://in.tradingview.com/chart/?symbol=NSE:FINEORG)<br><sub>📶W9 · W↑72d · ↓CMF0d</sub> | ⚠ CAUTION | Oleochemical additives for food cosmetics plastics coatings | 📈 BULL_ANY_MID | 18 | ↑55 | ↓1.003 | ↓2d | — | +1.9% | 2.23/0.03 | -0.79% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑63d · ↑CMF16d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.020 | ↑3d | — | +5.4% | 47.71/46.67 | -0.44% | 20% |
| [SWIGGY](https://in.tradingview.com/chart/?symbol=NSE:SWIGGY)<br><sub>📶W9 · W↑24d · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Food delivery and quick commerce marketplace serving Indian consumers | 📈 BULL_ANY_MID | 8 | ↑9 | ↑1.032 | ↑12d | — | +13.3% | 33.16/28.87 | +1.06% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Banking software solutions for financial institutions | 📈 BULL_ANY_MID | 5 | ↑89 | ↑1.055 | ↑15d | — | +20.9% | 50.17/48.27 | +4.64% | 20% |
| [ALKEM](https://in.tradingview.com/chart/?symbol=NSE:ALKEM)<br><sub>📶W9 · W↑14d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Pharma manufacturer: branded generics, APIs, nutraceuticals India | 📈 BULL_ANY_MID | 5 | ↑51 | ↑1.016 | ↑23d | — | +7.0% | 56.54/55.36 | +0.88% | 20% |
| [ADOR](https://in.tradingview.com/chart/?symbol=NSE:ADOR)<br><sub>📶W9 · W↑63d · ↑CMF16d</sub> | ✓ SAFE | Welding equipment and consumables for industrial fabrication | 📈 BULL_ANY_MID | 0 | ↑82 | ↓1.025 | ↑25d | — | +22.0% | 66.25/64.59 | -0.70% | 20% |
| [APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD)<br><sub>📶W9 · W↑24d · ↑CMF13d</sub> | ⚠ CAUTION | Generic drugs and APIs for global markets | 📈 BULL_ANY_MID | 0 | ↑43 | ↓1.015 | ↑23d | — | +13.8% | 58.47/57.44 | -1.21% | 20% |
| [PNB](https://in.tradingview.com/chart/?symbol=NSE:PNB)<br><sub>W↑25d · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | 🔄24 | ↑1.012 | ↑2d | — | +2.9% | -19.58/-24.31 | +0.94% | 20% |
| [JSWDULUX](https://in.tradingview.com/chart/?symbol=NSE:JSWDULUX)<br><sub>↓CMF14d</sub> | ⚠ CAUTION | Decorative and industrial paints manufacturing for buildings | 📈 BULL_ANY_MID | 54 | 🔄37 | ↑1.016 | ↑1d | — | +4.5% | -31.91/-32.75 | +4.48% | 20% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>🚀SS · ↑CMF4d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄94 | ↑1.031 | ↑1d | — | +4.5% | -28.4/-34.25 | +4.45% | 20% |
| [UNIONBANK](https://in.tradingview.com/chart/?symbol=NSE:UNIONBANK)<br><sub>↑CMF1d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄50 | ↑1.036 | ↑1d | — | +3.7% | -21.82/-27.26 | +3.73% | 20% |
| [ENRIN](https://in.tradingview.com/chart/?symbol=NSE:ENRIN)<br><sub>🚀SS · ↓CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 40 | 🔄73 | ↑1.009 | ↓21d | — | -1.4% | -25.75/-26.7 | +3.26% | 20% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>W↑1d · ↓CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 29 | ↓8 | ↑1.008 | ↑1d | — | +1.0% | -31.34/-34.03 | +1.02% | 20% |
| [JAINREC](https://in.tradingview.com/chart/?symbol=NSE:JAINREC)<br><sub>↓CMF2d · ⚠️TRAP</sub> | ✓ SAFE | Non-ferrous metal recycling, lead copper aluminium alloys | 📈 BULL_ANY_MID | 18 | ↓50 | ↓0.993 | ↓2d | — | +4.0% | -38.46/-39.92 | -2.35% | 20% 🟦 |
| [INTERARCH](https://in.tradingview.com/chart/?symbol=NSE:INTERARCH)<br><sub>W↑24d · ↓CMF30d</sub> | ✓ SAFE | Prefab structural steel buildings construction commercial industrial | 📈 BULL_ANY_MID | 18 | ↓23 | ↓1.003 | ↑2d | — | +2.0% | -11.98/-15.12 | -0.17% | 20% |
| [TVSHLTD](https://in.tradingview.com/chart/?symbol=NSE:TVSHLTD)<br><sub>W↑14d · 🚀SS · ↓CMF19d · DEL89%(T-1)</sub> | ⚠ CAUTION | Aluminum die-castings automotive components manufacturing holding company | 📈 BULL_ANY_MID | 14 | ↓52 | ↑1.001 | ↑16d | — | +4.9% | 44.22/41.61 | +0.09% | 20% |
| [TMPV](https://in.tradingview.com/chart/?symbol=NSE:TMPV)<br><sub>↓CMF17d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 10 | ↓15 | ↑1.001 | ↓21d | — | -8.6% | -43.02/-44.0 | +1.64% | 20% |
| [PRINCEPIPE](https://in.tradingview.com/chart/?symbol=NSE:PRINCEPIPE)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Plastic pipes fittings polymer processing residential commercial | 📈 BULL_ANY_MID | 6 | ↓31 | ↓0.992 | ↓14d | — | -4.3% | -29.88/-30.25 | -0.98% | 20% |
| [THOMASCOOK](https://in.tradingview.com/chart/?symbol=NSE:THOMASCOOK)<br><sub>W↑39d · 🚀SS · ↓CMF1d</sub> | ✓ SAFE | Travel agency, tours, forex, hotel bookings, Indians abroad | 📈 BULL_ANY_MID | 5 | ↓7 | ↑0.998 | ↓30d | — | +13.0% | -25.39/-27.12 | +0.59% | 20% |
| [TIINDIA](https://in.tradingview.com/chart/?symbol=NSE:TIINDIA)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Bicycles, tubes, automotive components, industrial applications | 📈 BULL_ANY_MID | 0 | ↓51 | ↓0.991 | ↓25d | — | -1.4% | -34.4/-36.02 | -0.24% | 20% |
| [NFL](https://in.tradingview.com/chart/?symbol=NSE:NFL)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Urea fertilizer production, agricultural inputs, Indian farming | 📈 BULL_ANY_MID | 0 | ↓16 | ↓0.994 | ↓24d | — | -2.3% | -39.96/-40.08 | -0.61% | 20% |

```
NSE:PPLPHARMA,NSE:ALLTIME,NSE:BHEL,NSE:INGERRAND,NSE:GLAND,NSE:COSMOFIRST,NSE:PGIL,NSE:HLEGLAS,NSE:EIMCOELECO,NSE:FINEORG,NSE:ABCAPITAL,NSE:SWIGGY,NSE:OFSS,NSE:ALKEM,NSE:ADOR,NSE:APLLTD,NSE:PNB,NSE:JSWDULUX,NSE:POWERINDIA,NSE:UNIONBANK,NSE:ENRIN,NSE:HDFCLIFE,NSE:JAINREC,NSE:INTERARCH,NSE:TVSHLTD,NSE:TMPV,NSE:PRINCEPIPE,NSE:THOMASCOOK,NSE:TIINDIA,NSE:NFL
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
