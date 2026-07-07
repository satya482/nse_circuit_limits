> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-07-07
*Generated 2026-07-07 15:44 IST*

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
| RS-Confirmed table | Separate table below, rs_state ≠ weak — informational only, all signals still listed in category tables |
| 📶W9 in Symbol | Daily RS > Weekly RS EMA9 AND Weekly RS EMA9 rising (same gate as ema25_zl_scanner RS_MODE=weekly_ema9) — highest sort priority in every table |

---

**Total bull crosses today: 65** · 20 inside active squeeze

```
NSE:JGCHEM,NSE:VINCOFE,NSE:AKUMS,NSE:HLEGLAS,NSE:ASKAUTOLTD,NSE:ITDC,NSE:TBZ,NSE:TATATECH,NSE:AEQUS,NSE:ZENTEC,NSE:IOLCP,NSE:GKENERGY,NSE:RBLBANK,NSE:ENDURANCE,NSE:VAIBHAVGBL,NSE:BANDHANBNK,NSE:TRAVELFOOD,NSE:ZYDUSLIFE,NSE:GROWW,NSE:VADILALIND,NSE:WELCORP,NSE:HEALTHX,NSE:COFORGE,NSE:LLOYDSENGG,NSE:AGI,NSE:GABRIEL,NSE:INDNIPPON,NSE:RAMCOSYS,NSE:JKIL,NSE:HCLTECH,NSE:RSYSTEMS,NSE:LTM,NSE:SIRCA,NSE:TATASTEEL,NSE:TATAELXSI,NSE:JINDALSTEL,NSE:INFY,NSE:ADVENZYMES,NSE:PGHH,NSE:VEEDOL,NSE:DIVISLAB,NSE:VINATIORGA,NSE:ISGEC,NSE:TCI,NSE:GREENPANEL,NSE:BHARTIHEXA,NSE:TATACONSUM,NSE:RATNAMANI,NSE:AMBER,NSE:POWERGRID,NSE:ICICIGI,NSE:BLUEDART,NSE:MUTHOOTFIN,NSE:BUILDPRO,NSE:ITC,NSE:BEL,NSE:TECHM,NSE:MAZDOCK,NSE:BPCL,NSE:HITECH,NSE:VBL,NSE:GICRE,NSE:WIPRO,NSE:HINDALCO,NSE:COALINDIA
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (28)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [JGCHEM](https://in.tradingview.com/chart/?symbol=NSE:JGCHEM)<br><sub>📶W9 · W↑65d · ↓CMF30d</sub> | ✓ SAFE | Zinc oxide manufacturing, 80 grades, industrial chemicals | ⚡ BULL_ANY_PPV | 99 | 🔄66 | ↑1.009 | ↑1d | SQ·PV | +1.9% | -2.05/-4.35 | +1.87% | 20% |
| [VINCOFE](https://in.tradingview.com/chart/?symbol=NSE:VINCOFE)<br><sub>📶W9 · W↑32d · 🚀SS · ↓CMF19d</sub> | ✓ SAFE | Instant coffee chicory production exporter beverage manufacturing | ⚡ BULL_ANY_PPV | 89 | 🔄62 | ↑1.037 | ↑1d | SQ·PV | +5.0% | 20.62/16.0 | +5.05% | 20% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>📶W9 · W↑27d · ↑CMF18d</sub> | ✓ SAFE | CDMO formulations development manufacturing Indian pharma companies | ⚡ BULL_ANY_PPV | 70 | 🔄83 | ↑1.037 | ↑26d | SQ·PV | +23.9% | 56.5/55.95 | +4.05% | 20% |
| [HLEGLAS](https://in.tradingview.com/chart/?symbol=NSE:HLEGLAS)<br><sub>📶W9 · W↑65d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Glass-lined equipment manufacturer pharmaceutical chemical processing | ⚡ BULL_ANY_PPV | 58 | ↑53 | ↑1.044 | ↑2d | SQ·PV | +6.1% | 45.55/39.21 | +4.38% | 20% |
| [ASKAUTOLTD](https://in.tradingview.com/chart/?symbol=NSE:ASKAUTOLTD)<br><sub>📶W9 · W↑17d · ↑CMF0d</sub> | ✓ SAFE | Two-wheeler advanced braking systems manufacturer India | ⚡ BULL_ANY_PPV | 54 | 🔄35 | ↑1.022 | ↑1d | PV | +3.2% | 8.18/5.43 | +3.19% | 20% |
| [ITDC](https://in.tradingview.com/chart/?symbol=NSE:ITDC)<br><sub>📶W9 · W↑65d · 🚀SS·49x · ↑CMF0d</sub> | ✓ SAFE | Tourism infrastructure hotels resorts hospitality sector India | ⚡ BULL_ANY_PPV | 49 | 🔄84 | ↑1.147 | ↑1d | PV | +20.0% | 5.55/-7.85 | +19.99% | 20% 🟦 |
| [TBZ](https://in.tradingview.com/chart/?symbol=NSE:TBZ)<br><sub>📶W9 · W↑32d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Gold diamond jewellery retail weddings occasions ceremonies | ⚡ BULL_ANY_PPV | 49 | 🔄75 | ↑1.039 | ↑1d | PV | +5.6% | 45.51/43.5 | +5.56% | 20% |
| [TATATECH](https://in.tradingview.com/chart/?symbol=NSE:TATATECH)<br><sub>📶W9 · W↑65d · 🚀SS · ↑CMF29d</sub> | ✓ SAFE | Engineering services for automotive manufacturing digital transformation | ⚡ BULL_ANY_PPV | 48 | 🔄68 | ↑1.009 | ↓12d | PV | -2.1% | -18.02/-21.2 | +2.11% | 20% |
| [AEQUS](https://in.tradingview.com/chart/?symbol=NSE:AEQUS)<br><sub>📶W9 · 🚀SS · ↑CMF11d</sub> | ✓ SAFE | Precision aerospace components and consumer product manufacturing | ⚡ BULL_ANY_PPV | 34 | 🔄50 | ↑1.054 | ↑16d | PV | +33.2% | 45.53/45.29 | +5.70% | 20% 🟦 |
| [ZENTEC](https://in.tradingview.com/chart/?symbol=NSE:ZENTEC)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Defense simulation systems and counter-drone solutions manufacturer | ⚡ BULL_ANY_PPV | 18 | ↑76 | ↓1.028 | ↑2d | PV | +6.7% | 15.05/10.92 | +0.57% | 20% |
| [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP)<br><sub>📶W9 · W↑72d · 🚀SS·12x · ↑CMF0d</sub> | ✓ SAFE | Ibuprofen APIs and specialty chemicals manufacturer global export | ⚡ BULL_ANY_PPV | 7 | ↑97 | ↑1.134 | ↑13d | PV | +28.6% | 71.75/66.84 | +14.25% | 20% |
| [GKENERGY](https://in.tradingview.com/chart/?symbol=NSE:GKENERGY)<br><sub>📶W9 · W↑58d · ↓CMF2d</sub> | ✓ SAFE | Solar water pumps, agricultural sector, rural India | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.030 | ↑1d | SQ | +3.4% | 15.98/14.33 | +3.35% | 10% 🟩 |
| [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Private bank retail corporate lending deposit services | 📈 BULL_ANY_MID | 63 | ↑80 | ↑1.022 | ↑2d | SQ | +3.9% | 17.85/16.09 | +1.76% | 20% |
| [ENDURANCE](https://in.tradingview.com/chart/?symbol=NSE:ENDURANCE)<br><sub>📶W9 · W↑60d · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Aluminum castings, suspension, braking systems for automakers | 📈 BULL_ANY_MID | 59 | 🔄48 | ↑1.006 | ↑1d | — | +0.8% | 12.76/12.61 | +0.75% | 20% |
| [VAIBHAVGBL](https://in.tradingview.com/chart/?symbol=NSE:VAIBHAVGBL)<br><sub>📶W9 · W↑60d · ↓CMF30d</sub> | ✓ SAFE | Fashion jewelry and gemstones direct-to-consumer retailer globally | 📈 BULL_ANY_MID | 59 | 🔄52 | ↑1.007 | ↑1d | — | +1.1% | 8.46/5.43 | +1.09% | 20% |
| [BANDHANBNK](https://in.tradingview.com/chart/?symbol=NSE:BANDHANBNK)<br><sub>📶W9 · ↓CMF12d</sub> | ✓ SAFE | Microfinance-focused universal bank serving underbanked retail customers | 📈 BULL_ANY_MID | 58 | ↓78 | ↓1.001 | ↓2d | SQ | +2.2% | -3.26/-7.78 | -1.10% | 20% |
| [TRAVELFOOD](https://in.tradingview.com/chart/?symbol=NSE:TRAVELFOOD)<br><sub>📶W9 · W↑27d · ↑CMF1d</sub> | ✓ SAFE | Food catering services for trains, flights, buses | 📈 BULL_ANY_MID | 58 | 🔄50 | ↑1.011 | ↑2d | — | +2.2% | 29.71/29.36 | +0.73% | 20% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>📶W9 · W↑56d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | Pharmaceuticals: generics, branded drugs, consumer wellness products | 📈 BULL_ANY_MID | 49 | 🔄73 | ↑1.031 | ↑1d | — | +3.9% | 44.71/41.57 | +3.92% | 20% |
| [GROWW](https://in.tradingview.com/chart/?symbol=NSE:GROWW)<br><sub>📶W9 · ↑CMF9d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 22 | ↑50 | ↑1.018 | ↑3d | — | +4.0% | 33.78/30.78 | +1.28% | 20% |
| [VADILALIND](https://in.tradingview.com/chart/?symbol=NSE:VADILALIND)<br><sub>📶W9 · W↑32d · ↑CMF11d</sub> | ✓ SAFE | Ice cream and frozen desserts manufacturer, retail and foodservice | 📈 BULL_ANY_MID | 21 | ↑82 | ↑1.027 | ↑4d | — | +6.7% | 39.66/36.85 | +1.15% | 20% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Large-diameter pipes, steel billets, rebars infrastructure | 📈 BULL_ANY_MID | 18 | ↑96 | ↓1.037 | ↑2d | — | +7.1% | 69.64/68.33 | -0.17% | 20% |
| [HEALTHX](https://in.tradingview.com/chart/?symbol=NSE:HEALTHX)<br><sub>📶W9 · W↑51d · ↓CMF24d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 18 | ↓59 | ↓1.000 | ↑2d | — | +1.1% | 21.16/20.21 | -1.67% | 20% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>📶W9 · W↑68d · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | IT services, digital transformation, global enterprises | 📈 BULL_ANY_MID | 17 | ↑41 | ↑1.031 | ↑3d | — | +5.2% | 27.46/21.97 | +2.31% | 20% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>📶W9 · W↑65d · ↑CMF15d</sub> | ✓ SAFE | Heavy equipment manufacturing for oil gas steel power | 📈 BULL_ANY_MID | 17 | ↓93 | ↓1.002 | ↑3d | — | +2.8% | 39.54/37.19 | -5.30% | 20% |
| [AGI](https://in.tradingview.com/chart/?symbol=NSE:AGI)<br><sub>📶W9 · W↑72d · ↑CMF15d</sub> | ✓ SAFE | Glass containers PET bottles closures beverages pharma | 📈 BULL_ANY_MID | 10 | ↑49 | ↑1.012 | ↑27d | — | +20.2% | 43.13/42.99 | +0.33% | 20% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>📶W9 · W↑17d · ↑CMF12d</sub> | ✓ SAFE | Shock absorbers struts two wheeler four wheeler OEM aftermarket | 📈 BULL_ANY_MID | 3 | ↑78 | ↓1.021 | ↑17d | — | +21.7% | 42.61/41.77 | -0.68% | 20% |
| [INDNIPPON](https://in.tradingview.com/chart/?symbol=NSE:INDNIPPON)<br><sub>📶W9 · W↑60d · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | Electronic ignition systems two-wheeler three-wheeler portable engines | 📈 BULL_ANY_MID | 2 | ↑78 | ↑1.049 | ↑18d | — | +19.5% | 68.38/66.1 | +3.14% | 20% |
| [RAMCOSYS](https://in.tradingview.com/chart/?symbol=NSE:RAMCOSYS)<br><sub>📶W9 · W↑37d · ↑CMF22d</sub> | ✓ SAFE | Cloud ERP software for aviation and manufacturing businesses | 📈 BULL_ANY_MID | 0 | ↑98 | ↓1.123 | ↑33d | — | +124.7% | 77.47/77.21 | +0.06% | 10% 🟨 |

```
NSE:JGCHEM,NSE:VINCOFE,NSE:AKUMS,NSE:HLEGLAS,NSE:ASKAUTOLTD,NSE:ITDC,NSE:TBZ,NSE:TATATECH,NSE:AEQUS,NSE:ZENTEC,NSE:IOLCP,NSE:GKENERGY,NSE:RBLBANK,NSE:ENDURANCE,NSE:VAIBHAVGBL,NSE:BANDHANBNK,NSE:TRAVELFOOD,NSE:ZYDUSLIFE,NSE:GROWW,NSE:VADILALIND,NSE:WELCORP,NSE:HEALTHX,NSE:COFORGE,NSE:LLOYDSENGG,NSE:AGI,NSE:GABRIEL,NSE:INDNIPPON,NSE:RAMCOSYS
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (42)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [JGCHEM](https://in.tradingview.com/chart/?symbol=NSE:JGCHEM)<br><sub>📶W9 · W↑65d · ↓CMF30d</sub> | ✓ SAFE | Zinc oxide manufacturing, 80 grades, industrial chemicals | ⚡ BULL_ANY_PPV | 99 | 🔄66 | ↑1.009 | ↑1d | SQ·PV | +1.9% | -2.05/-4.35 | +1.87% | 20% |
| [VINCOFE](https://in.tradingview.com/chart/?symbol=NSE:VINCOFE)<br><sub>📶W9 · W↑32d · 🚀SS · ↓CMF19d</sub> | ✓ SAFE | Instant coffee chicory production exporter beverage manufacturing | ⚡ BULL_ANY_PPV | 89 | 🔄62 | ↑1.037 | ↑1d | SQ·PV | +5.0% | 20.62/16.0 | +5.05% | 20% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>📶W9 · W↑27d · ↑CMF18d</sub> | ✓ SAFE | CDMO formulations development manufacturing Indian pharma companies | ⚡ BULL_ANY_PPV | 70 | 🔄83 | ↑1.037 | ↑26d | SQ·PV | +23.9% | 56.5/55.95 | +4.05% | 20% |
| [HLEGLAS](https://in.tradingview.com/chart/?symbol=NSE:HLEGLAS)<br><sub>📶W9 · W↑65d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Glass-lined equipment manufacturer pharmaceutical chemical processing | ⚡ BULL_ANY_PPV | 58 | ↑53 | ↑1.044 | ↑2d | SQ·PV | +6.1% | 45.55/39.21 | +4.38% | 20% |
| [ASKAUTOLTD](https://in.tradingview.com/chart/?symbol=NSE:ASKAUTOLTD)<br><sub>📶W9 · W↑17d · ↑CMF0d</sub> | ✓ SAFE | Two-wheeler advanced braking systems manufacturer India | ⚡ BULL_ANY_PPV | 54 | 🔄35 | ↑1.022 | ↑1d | PV | +3.2% | 8.18/5.43 | +3.19% | 20% |
| [ITDC](https://in.tradingview.com/chart/?symbol=NSE:ITDC)<br><sub>📶W9 · W↑65d · 🚀SS·49x · ↑CMF0d</sub> | ✓ SAFE | Tourism infrastructure hotels resorts hospitality sector India | ⚡ BULL_ANY_PPV | 49 | 🔄84 | ↑1.147 | ↑1d | PV | +20.0% | 5.55/-7.85 | +19.99% | 20% 🟦 |
| [TBZ](https://in.tradingview.com/chart/?symbol=NSE:TBZ)<br><sub>📶W9 · W↑32d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Gold diamond jewellery retail weddings occasions ceremonies | ⚡ BULL_ANY_PPV | 49 | 🔄75 | ↑1.039 | ↑1d | PV | +5.6% | 45.51/43.5 | +5.56% | 20% |
| [TATATECH](https://in.tradingview.com/chart/?symbol=NSE:TATATECH)<br><sub>📶W9 · W↑65d · 🚀SS · ↑CMF29d</sub> | ✓ SAFE | Engineering services for automotive manufacturing digital transformation | ⚡ BULL_ANY_PPV | 48 | 🔄68 | ↑1.009 | ↓12d | PV | -2.1% | -18.02/-21.2 | +2.11% | 20% |
| [AEQUS](https://in.tradingview.com/chart/?symbol=NSE:AEQUS)<br><sub>📶W9 · 🚀SS · ↑CMF11d</sub> | ✓ SAFE | Precision aerospace components and consumer product manufacturing | ⚡ BULL_ANY_PPV | 34 | 🔄50 | ↑1.054 | ↑16d | PV | +33.2% | 45.53/45.29 | +5.70% | 20% 🟦 |
| [ZENTEC](https://in.tradingview.com/chart/?symbol=NSE:ZENTEC)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Defense simulation systems and counter-drone solutions manufacturer | ⚡ BULL_ANY_PPV | 18 | ↑76 | ↓1.028 | ↑2d | PV | +6.7% | 15.05/10.92 | +0.57% | 20% |
| [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP)<br><sub>📶W9 · W↑72d · 🚀SS·12x · ↑CMF0d</sub> | ✓ SAFE | Ibuprofen APIs and specialty chemicals manufacturer global export | ⚡ BULL_ANY_PPV | 7 | ↑97 | ↑1.134 | ↑13d | PV | +28.6% | 71.75/66.84 | +14.25% | 20% |
| [GKENERGY](https://in.tradingview.com/chart/?symbol=NSE:GKENERGY)<br><sub>📶W9 · W↑58d · ↓CMF2d</sub> | ✓ SAFE | Solar water pumps, agricultural sector, rural India | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.030 | ↑1d | SQ | +3.4% | 15.98/14.33 | +3.35% | 10% 🟩 |
| [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Private bank retail corporate lending deposit services | 📈 BULL_ANY_MID | 63 | ↑80 | ↑1.022 | ↑2d | SQ | +3.9% | 17.85/16.09 | +1.76% | 20% |
| [ENDURANCE](https://in.tradingview.com/chart/?symbol=NSE:ENDURANCE)<br><sub>📶W9 · W↑60d · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Aluminum castings, suspension, braking systems for automakers | 📈 BULL_ANY_MID | 59 | 🔄48 | ↑1.006 | ↑1d | — | +0.8% | 12.76/12.61 | +0.75% | 20% |
| [VAIBHAVGBL](https://in.tradingview.com/chart/?symbol=NSE:VAIBHAVGBL)<br><sub>📶W9 · W↑60d · ↓CMF30d</sub> | ✓ SAFE | Fashion jewelry and gemstones direct-to-consumer retailer globally | 📈 BULL_ANY_MID | 59 | 🔄52 | ↑1.007 | ↑1d | — | +1.1% | 8.46/5.43 | +1.09% | 20% |
| [TRAVELFOOD](https://in.tradingview.com/chart/?symbol=NSE:TRAVELFOOD)<br><sub>📶W9 · W↑27d · ↑CMF1d</sub> | ✓ SAFE | Food catering services for trains, flights, buses | 📈 BULL_ANY_MID | 58 | 🔄50 | ↑1.011 | ↑2d | — | +2.2% | 29.71/29.36 | +0.73% | 20% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>📶W9 · W↑56d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | Pharmaceuticals: generics, branded drugs, consumer wellness products | 📈 BULL_ANY_MID | 49 | 🔄73 | ↑1.031 | ↑1d | — | +3.9% | 44.71/41.57 | +3.92% | 20% |
| [GROWW](https://in.tradingview.com/chart/?symbol=NSE:GROWW)<br><sub>📶W9 · ↑CMF9d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 22 | ↑50 | ↑1.018 | ↑3d | — | +4.0% | 33.78/30.78 | +1.28% | 20% |
| [VADILALIND](https://in.tradingview.com/chart/?symbol=NSE:VADILALIND)<br><sub>📶W9 · W↑32d · ↑CMF11d</sub> | ✓ SAFE | Ice cream and frozen desserts manufacturer, retail and foodservice | 📈 BULL_ANY_MID | 21 | ↑82 | ↑1.027 | ↑4d | — | +6.7% | 39.66/36.85 | +1.15% | 20% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Large-diameter pipes, steel billets, rebars infrastructure | 📈 BULL_ANY_MID | 18 | ↑96 | ↓1.037 | ↑2d | — | +7.1% | 69.64/68.33 | -0.17% | 20% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>📶W9 · W↑68d · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | IT services, digital transformation, global enterprises | 📈 BULL_ANY_MID | 17 | ↑41 | ↑1.031 | ↑3d | — | +5.2% | 27.46/21.97 | +2.31% | 20% |
| [AGI](https://in.tradingview.com/chart/?symbol=NSE:AGI)<br><sub>📶W9 · W↑72d · ↑CMF15d</sub> | ✓ SAFE | Glass containers PET bottles closures beverages pharma | 📈 BULL_ANY_MID | 10 | ↑49 | ↑1.012 | ↑27d | — | +20.2% | 43.13/42.99 | +0.33% | 20% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>📶W9 · W↑17d · ↑CMF12d</sub> | ✓ SAFE | Shock absorbers struts two wheeler four wheeler OEM aftermarket | 📈 BULL_ANY_MID | 3 | ↑78 | ↓1.021 | ↑17d | — | +21.7% | 42.61/41.77 | -0.68% | 20% |
| [INDNIPPON](https://in.tradingview.com/chart/?symbol=NSE:INDNIPPON)<br><sub>📶W9 · W↑60d · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | Electronic ignition systems two-wheeler three-wheeler portable engines | 📈 BULL_ANY_MID | 2 | ↑78 | ↑1.049 | ↑18d | — | +19.5% | 68.38/66.1 | +3.14% | 20% |
| [RAMCOSYS](https://in.tradingview.com/chart/?symbol=NSE:RAMCOSYS)<br><sub>📶W9 · W↑37d · ↑CMF22d</sub> | ✓ SAFE | Cloud ERP software for aviation and manufacturing businesses | 📈 BULL_ANY_MID | 0 | ↑98 | ↓1.123 | ↑33d | — | +124.7% | 77.47/77.21 | +0.06% | 10% 🟨 |
| [JKIL](https://in.tradingview.com/chart/?symbol=NSE:JKIL)<br><sub>W↑12d · ↓CMF30d</sub> | ⚠ CAUTION | EPC contractor, urban transport infrastructure, roads and metro | ⚡ BULL_ANY_PPV | 54 | 🔄18 | ↑1.019 | ↑1d | PV | +3.0% | 0.59/-3.31 | +3.00% | 20% |
| [HCLTECH](https://in.tradingview.com/chart/?symbol=NSE:HCLTECH)<br><sub>🚀SS · ↑CMF10d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 49 | 🔄3 | ↑1.033 | ↑1d | PV | +5.7% | -42.54/-49.08 | +5.74% | 20% |
| [RSYSTEMS](https://in.tradingview.com/chart/?symbol=NSE:RSYSTEMS)<br><sub>🚀SS·10x · ↓CMF30d</sub> | ✓ SAFE | Product engineering and AI-driven digital transformation services | ⚡ BULL_ANY_PPV | 43 | 🔄1 | ↑1.004 | ↓17d | PV | -5.8% | -53.21/-54.61 | +5.08% | 20% |
| [LTM](https://in.tradingview.com/chart/?symbol=NSE:LTM)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 47 | 🔄3 | ↑1.007 | ↓13d | — | -3.6% | -56.4/-61.13 | +2.08% | 20% |
| [PGHH](https://in.tradingview.com/chart/?symbol=NSE:PGHH)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Feminine hygiene pads, healthcare products, mass market | 📈 BULL_ANY_MID | 99 | 🔄5 | ↑1.003 | ↑1d | SQ | +0.4% | -37.95/-41.1 | +0.42% | 20% |
| [VEEDOL](https://in.tradingview.com/chart/?symbol=NSE:VEEDOL)<br><sub>W↑65d · 🚀SS · ↓CMF22d</sub> | ⚠ CAUTION | Automotive industrial lubricants manufacturing marketing India global | 📈 BULL_ANY_MID | 99 | 🔄27 | ↑1.008 | ↑1d | SQ | +1.2% | 3.88/1.25 | +1.18% | 20% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>W↑56d · 🚀SS · ↓CMF4d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 98 | 🔄55 | ↑1.013 | ↑2d | SQ | +3.2% | 2.18/-1.42 | +1.13% | 20% |
| [VINATIORGA](https://in.tradingview.com/chart/?symbol=NSE:VINATIORGA)<br><sub>W↑56d · ↓CMF30d</sub> | ✓ SAFE | Specialty chemicals and organic intermediates manufacturer for pharma | 📈 BULL_ANY_MID | 98 | 🔄17 | ↑1.013 | ↑2d | SQ | +2.4% | 8.05/5.35 | +0.83% | 20% |
| [ISGEC](https://in.tradingview.com/chart/?symbol=NSE:ISGEC)<br><sub>↑CMF1d · DEL84%(T-1)</sub> | ⚠ CAUTION | Heavy equipment manufacturing for sugar and steel industries | 📈 BULL_ANY_MID | 98 | 🔄34 | ↑1.004 | ↑2d | SQ | +0.8% | -19.15/-21.46 | +0.36% | 20% |
| [TCI](https://in.tradingview.com/chart/?symbol=NSE:TCI)<br><sub>W↑27d · ↓CMF4d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄16 | ↑1.019 | ↑1d | SQ | +2.4% | 2.42/-6.37 | +2.38% | 20% |
| [GREENPANEL](https://in.tradingview.com/chart/?symbol=NSE:GREENPANEL)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | MDF and plywood manufacturer for furniture construction | 📈 BULL_ANY_MID | 94 | 🔄11 | ↑1.021 | ↑1d | SQ | +3.9% | -12.01/-17.05 | +3.93% | 20% |
| [BHARTIHEXA](https://in.tradingview.com/chart/?symbol=NSE:BHARTIHEXA)<br><sub>W↑2d · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | Mobile, fixed-line, broadband services Rajasthan and Northeast circles | 📈 BULL_ANY_MID | 93 | 🔄18 | ↑1.020 | ↑2d | SQ | +3.2% | -19.9/-30.9 | +2.28% | 20% |
| [RATNAMANI](https://in.tradingview.com/chart/?symbol=NSE:RATNAMANI)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Stainless steel seamless welded pipes oil gas petrochemical power | 📈 BULL_ANY_MID | 59 | 🔄54 | ↑1.011 | ↑1d | — | +1.1% | -9.53/-11.85 | +1.07% | 20% |
| [AMBER](https://in.tradingview.com/chart/?symbol=NSE:AMBER)<br><sub>↓CMF8d</sub> | ✓ SAFE | AC manufacturing and EMS for consumer appliances | 📈 BULL_ANY_MID | 58 | 🔄55 | ↑1.006 | ↑2d | — | +1.9% | -17.4/-19.97 | +0.14% | 20% |
| [ICICIGI](https://in.tradingview.com/chart/?symbol=NSE:ICICIGI)<br><sub>W↑17d · ↑CMF1d</sub> | ⚠ CAUTION | General insurance motor health property casualty India | 📈 BULL_ANY_MID | 58 | 🔄30 | ↑1.006 | ↑2d | — | +1.2% | -8.02/-10.47 | +0.50% | 20% |
| [MUTHOOTFIN](https://in.tradingview.com/chart/?symbol=NSE:MUTHOOTFIN)<br><sub>🚀SS · ↓CMF1d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 51 | 🔄30 | ↑1.005 | ↓9d | — | -2.4% | -40.8/-42.17 | +3.40% | 20% |
| [MAZDOCK](https://in.tradingview.com/chart/?symbol=NSE:MAZDOCK)<br><sub>W↑7d · ↓CMF30d</sub> | ✓ SAFE | Defense warships submarines naval shipbuilding PSU | 📈 BULL_ANY_MID | 23 | ↑38 | ↑1.017 | ↑2d | — | +3.6% | 10.55/8.39 | +1.43% | 20% |

```
NSE:JGCHEM,NSE:VINCOFE,NSE:AKUMS,NSE:HLEGLAS,NSE:ASKAUTOLTD,NSE:ITDC,NSE:TBZ,NSE:TATATECH,NSE:AEQUS,NSE:ZENTEC,NSE:IOLCP,NSE:GKENERGY,NSE:RBLBANK,NSE:ENDURANCE,NSE:VAIBHAVGBL,NSE:TRAVELFOOD,NSE:ZYDUSLIFE,NSE:GROWW,NSE:VADILALIND,NSE:WELCORP,NSE:COFORGE,NSE:AGI,NSE:GABRIEL,NSE:INDNIPPON,NSE:RAMCOSYS,NSE:JKIL,NSE:HCLTECH,NSE:RSYSTEMS,NSE:LTM,NSE:PGHH,NSE:VEEDOL,NSE:DIVISLAB,NSE:VINATIORGA,NSE:ISGEC,NSE:TCI,NSE:GREENPANEL,NSE:BHARTIHEXA,NSE:RATNAMANI,NSE:AMBER,NSE:ICICIGI,NSE:MUTHOOTFIN,NSE:MAZDOCK
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (20)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [JGCHEM](https://in.tradingview.com/chart/?symbol=NSE:JGCHEM)<br><sub>📶W9 · W↑65d · ↓CMF30d</sub> | ✓ SAFE | Zinc oxide manufacturing, 80 grades, industrial chemicals | ⚡ BULL_ANY_PPV | 99 | 🔄66 | ↑1.009 | ↑1d | SQ·PV | +1.9% | -2.05/-4.35 | +1.87% | 20% |
| [VINCOFE](https://in.tradingview.com/chart/?symbol=NSE:VINCOFE)<br><sub>📶W9 · W↑32d · 🚀SS · ↓CMF19d</sub> | ✓ SAFE | Instant coffee chicory production exporter beverage manufacturing | ⚡ BULL_ANY_PPV | 89 | 🔄62 | ↑1.037 | ↑1d | SQ·PV | +5.0% | 20.62/16.0 | +5.05% | 20% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>📶W9 · W↑27d · ↑CMF18d</sub> | ✓ SAFE | CDMO formulations development manufacturing Indian pharma companies | ⚡ BULL_ANY_PPV | 70 | 🔄83 | ↑1.037 | ↑26d | SQ·PV | +23.9% | 56.5/55.95 | +4.05% | 20% |
| [HLEGLAS](https://in.tradingview.com/chart/?symbol=NSE:HLEGLAS)<br><sub>📶W9 · W↑65d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Glass-lined equipment manufacturer pharmaceutical chemical processing | ⚡ BULL_ANY_PPV | 58 | ↑53 | ↑1.044 | ↑2d | SQ·PV | +6.1% | 45.55/39.21 | +4.38% | 20% |
| [GKENERGY](https://in.tradingview.com/chart/?symbol=NSE:GKENERGY)<br><sub>📶W9 · W↑58d · ↓CMF2d</sub> | ✓ SAFE | Solar water pumps, agricultural sector, rural India | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.030 | ↑1d | SQ | +3.4% | 15.98/14.33 | +3.35% | 10% 🟩 |
| [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Private bank retail corporate lending deposit services | 📈 BULL_ANY_MID | 63 | ↑80 | ↑1.022 | ↑2d | SQ | +3.9% | 17.85/16.09 | +1.76% | 20% |
| [BANDHANBNK](https://in.tradingview.com/chart/?symbol=NSE:BANDHANBNK)<br><sub>📶W9 · ↓CMF12d</sub> | ✓ SAFE | Microfinance-focused universal bank serving underbanked retail customers | 📈 BULL_ANY_MID | 58 | ↓78 | ↓1.001 | ↓2d | SQ | +2.2% | -3.26/-7.78 | -1.10% | 20% |
| [SIRCA](https://in.tradingview.com/chart/?symbol=NSE:SIRCA)<br><sub>↓CMF30d</sub> | ✓ SAFE | Italian wood coatings and decorative paints manufacturer | 🟢 BULL_OVERSOLD | 43 | ↓24 | ↓0.990 | ↓17d | SQ | -4.2% | -67.81/-68.28 | -0.43% | 20% |
| [PGHH](https://in.tradingview.com/chart/?symbol=NSE:PGHH)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Feminine hygiene pads, healthcare products, mass market | 📈 BULL_ANY_MID | 99 | 🔄5 | ↑1.003 | ↑1d | SQ | +0.4% | -37.95/-41.1 | +0.42% | 20% |
| [VEEDOL](https://in.tradingview.com/chart/?symbol=NSE:VEEDOL)<br><sub>W↑65d · 🚀SS · ↓CMF22d</sub> | ⚠ CAUTION | Automotive industrial lubricants manufacturing marketing India global | 📈 BULL_ANY_MID | 99 | 🔄27 | ↑1.008 | ↑1d | SQ | +1.2% | 3.88/1.25 | +1.18% | 20% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>W↑56d · 🚀SS · ↓CMF4d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 98 | 🔄55 | ↑1.013 | ↑2d | SQ | +3.2% | 2.18/-1.42 | +1.13% | 20% |
| [VINATIORGA](https://in.tradingview.com/chart/?symbol=NSE:VINATIORGA)<br><sub>W↑56d · ↓CMF30d</sub> | ✓ SAFE | Specialty chemicals and organic intermediates manufacturer for pharma | 📈 BULL_ANY_MID | 98 | 🔄17 | ↑1.013 | ↑2d | SQ | +2.4% | 8.05/5.35 | +0.83% | 20% |
| [ISGEC](https://in.tradingview.com/chart/?symbol=NSE:ISGEC)<br><sub>↑CMF1d · DEL84%(T-1)</sub> | ⚠ CAUTION | Heavy equipment manufacturing for sugar and steel industries | 📈 BULL_ANY_MID | 98 | 🔄34 | ↑1.004 | ↑2d | SQ | +0.8% | -19.15/-21.46 | +0.36% | 20% |
| [TCI](https://in.tradingview.com/chart/?symbol=NSE:TCI)<br><sub>W↑27d · ↓CMF4d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄16 | ↑1.019 | ↑1d | SQ | +2.4% | 2.42/-6.37 | +2.38% | 20% |
| [GREENPANEL](https://in.tradingview.com/chart/?symbol=NSE:GREENPANEL)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | MDF and plywood manufacturer for furniture construction | 📈 BULL_ANY_MID | 94 | 🔄11 | ↑1.021 | ↑1d | SQ | +3.9% | -12.01/-17.05 | +3.93% | 20% |
| [BHARTIHEXA](https://in.tradingview.com/chart/?symbol=NSE:BHARTIHEXA)<br><sub>W↑2d · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | Mobile, fixed-line, broadband services Rajasthan and Northeast circles | 📈 BULL_ANY_MID | 93 | 🔄18 | ↑1.020 | ↑2d | SQ | +3.2% | -19.9/-30.9 | +2.28% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>↓CMF19d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↓37 | ↑1.004 | ↑1d | SQ | +0.4% | -36.31/-41.57 | +0.36% | 20% |
| [POWERGRID](https://in.tradingview.com/chart/?symbol=NSE:POWERGRID)<br><sub>🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↓39 | ↓1.001 | ↑2d | SQ | +0.2% | -10.75/-15.11 | -0.07% | 20% |
| [BLUEDART](https://in.tradingview.com/chart/?symbol=NSE:BLUEDART)<br><sub>W↑12d · ↓CMF30d</sub> | ⚠ CAUTION | Domestic express parcel delivery via air and ground network | 📈 BULL_ANY_MID | 58 | ↓15 | ↓0.998 | ↑2d | SQ | +1.0% | 13.64/12.37 | -1.49% | 20% |
| [BUILDPRO](https://in.tradingview.com/chart/?symbol=NSE:BUILDPRO)<br><sub>↑CMF1d</sub> | ✓ SAFE | Building materials retail distribution southern western India | 📈 BULL_ANY_MID | 40 | ↓50 | ↓0.986 | ↓29d | SQ | -4.9% | -42.75/-44.41 | -2.35% | 20% |

```
NSE:JGCHEM,NSE:VINCOFE,NSE:AKUMS,NSE:HLEGLAS,NSE:GKENERGY,NSE:RBLBANK,NSE:BANDHANBNK,NSE:SIRCA,NSE:PGHH,NSE:VEEDOL,NSE:DIVISLAB,NSE:VINATIORGA,NSE:ISGEC,NSE:TCI,NSE:GREENPANEL,NSE:BHARTIHEXA,NSE:TATACONSUM,NSE:POWERGRID,NSE:BLUEDART,NSE:BUILDPRO
```

---

### 🔥 MAJOR — PPV confirmed (10)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ASKAUTOLTD](https://in.tradingview.com/chart/?symbol=NSE:ASKAUTOLTD)<br><sub>📶W9 · W↑17d · ↑CMF0d</sub> | ✓ SAFE | Two-wheeler advanced braking systems manufacturer India | ⚡ BULL_ANY_PPV | 54 | 🔄35 | ↑1.022 | ↑1d | PV | +3.2% | 8.18/5.43 | +3.19% | 20% |
| [ITDC](https://in.tradingview.com/chart/?symbol=NSE:ITDC)<br><sub>📶W9 · W↑65d · 🚀SS·49x · ↑CMF0d</sub> | ✓ SAFE | Tourism infrastructure hotels resorts hospitality sector India | ⚡ BULL_ANY_PPV | 49 | 🔄84 | ↑1.147 | ↑1d | PV | +20.0% | 5.55/-7.85 | +19.99% | 20% 🟦 |
| [TBZ](https://in.tradingview.com/chart/?symbol=NSE:TBZ)<br><sub>📶W9 · W↑32d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Gold diamond jewellery retail weddings occasions ceremonies | ⚡ BULL_ANY_PPV | 49 | 🔄75 | ↑1.039 | ↑1d | PV | +5.6% | 45.51/43.5 | +5.56% | 20% |
| [TATATECH](https://in.tradingview.com/chart/?symbol=NSE:TATATECH)<br><sub>📶W9 · W↑65d · 🚀SS · ↑CMF29d</sub> | ✓ SAFE | Engineering services for automotive manufacturing digital transformation | ⚡ BULL_ANY_PPV | 48 | 🔄68 | ↑1.009 | ↓12d | PV | -2.1% | -18.02/-21.2 | +2.11% | 20% |
| [AEQUS](https://in.tradingview.com/chart/?symbol=NSE:AEQUS)<br><sub>📶W9 · 🚀SS · ↑CMF11d</sub> | ✓ SAFE | Precision aerospace components and consumer product manufacturing | ⚡ BULL_ANY_PPV | 34 | 🔄50 | ↑1.054 | ↑16d | PV | +33.2% | 45.53/45.29 | +5.70% | 20% 🟦 |
| [ZENTEC](https://in.tradingview.com/chart/?symbol=NSE:ZENTEC)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Defense simulation systems and counter-drone solutions manufacturer | ⚡ BULL_ANY_PPV | 18 | ↑76 | ↓1.028 | ↑2d | PV | +6.7% | 15.05/10.92 | +0.57% | 20% |
| [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP)<br><sub>📶W9 · W↑72d · 🚀SS·12x · ↑CMF0d</sub> | ✓ SAFE | Ibuprofen APIs and specialty chemicals manufacturer global export | ⚡ BULL_ANY_PPV | 7 | ↑97 | ↑1.134 | ↑13d | PV | +28.6% | 71.75/66.84 | +14.25% | 20% |
| [JKIL](https://in.tradingview.com/chart/?symbol=NSE:JKIL)<br><sub>W↑12d · ↓CMF30d</sub> | ⚠ CAUTION | EPC contractor, urban transport infrastructure, roads and metro | ⚡ BULL_ANY_PPV | 54 | 🔄18 | ↑1.019 | ↑1d | PV | +3.0% | 0.59/-3.31 | +3.00% | 20% |
| [HCLTECH](https://in.tradingview.com/chart/?symbol=NSE:HCLTECH)<br><sub>🚀SS · ↑CMF10d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 49 | 🔄3 | ↑1.033 | ↑1d | PV | +5.7% | -42.54/-49.08 | +5.74% | 20% |
| [RSYSTEMS](https://in.tradingview.com/chart/?symbol=NSE:RSYSTEMS)<br><sub>🚀SS·10x · ↓CMF30d</sub> | ✓ SAFE | Product engineering and AI-driven digital transformation services | ⚡ BULL_ANY_PPV | 43 | 🔄1 | ↑1.004 | ↓17d | PV | -5.8% | -53.21/-54.61 | +5.08% | 20% |

```
NSE:ASKAUTOLTD,NSE:ITDC,NSE:TBZ,NSE:TATATECH,NSE:AEQUS,NSE:ZENTEC,NSE:IOLCP,NSE:JKIL,NSE:HCLTECH,NSE:RSYSTEMS
```

### 🟢 OVERSOLD — reversal from −53/−60 (6)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [LTM](https://in.tradingview.com/chart/?symbol=NSE:LTM)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 47 | 🔄3 | ↑1.007 | ↓13d | — | -3.6% | -56.4/-61.13 | +2.08% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>🚀SS · ↓CMF8d</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 5 | ↓50 | ↑0.995 | ↓22d | — | -9.7% | -60.32/-63.96 | +1.29% | 20% |
| [TATAELXSI](https://in.tradingview.com/chart/?symbol=NSE:TATAELXSI)<br><sub>🚀SS · ↓CMF5d</sub> | ✓ SAFE | Design engineering services automotive media communications healthcare | 🟢 BULL_OVERSOLD | 5 | ↓2 | ↑0.976 | ↓36d | — | -10.8% | -67.2/-67.77 | +1.33% | 20% |
| [JINDALSTEL](https://in.tradingview.com/chart/?symbol=NSE:JINDALSTEL)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 5 | ↓38 | ↑0.982 | ↓35d | — | -15.2% | -70.63/-73.17 | +0.98% | 20% |
| [INFY](https://in.tradingview.com/chart/?symbol=NSE:INFY)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 18 | ↓2 | ↑1.001 | ↓12d | — | -8.4% | -50.54/-55.6 | +0.59% | 20% |
| [ADVENZYMES](https://in.tradingview.com/chart/?symbol=NSE:ADVENZYMES)<br><sub>↓CMF8d</sub> | ✓ SAFE | Enzyme manufacturing for pharmaceuticals, food, diagnostics | 🟡 BULL_OS_L2 | 8 | ↓48 | ↓0.971 | ↓12d | — | -14.4% | -55.41/-56.79 | -0.82% | 20% |

```
NSE:LTM,NSE:TATASTEEL,NSE:TATAELXSI,NSE:JINDALSTEL,NSE:INFY,NSE:ADVENZYMES
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (29)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ENDURANCE](https://in.tradingview.com/chart/?symbol=NSE:ENDURANCE)<br><sub>📶W9 · W↑60d · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Aluminum castings, suspension, braking systems for automakers | 📈 BULL_ANY_MID | 59 | 🔄48 | ↑1.006 | ↑1d | — | +0.8% | 12.76/12.61 | +0.75% | 20% |
| [VAIBHAVGBL](https://in.tradingview.com/chart/?symbol=NSE:VAIBHAVGBL)<br><sub>📶W9 · W↑60d · ↓CMF30d</sub> | ✓ SAFE | Fashion jewelry and gemstones direct-to-consumer retailer globally | 📈 BULL_ANY_MID | 59 | 🔄52 | ↑1.007 | ↑1d | — | +1.1% | 8.46/5.43 | +1.09% | 20% |
| [TRAVELFOOD](https://in.tradingview.com/chart/?symbol=NSE:TRAVELFOOD)<br><sub>📶W9 · W↑27d · ↑CMF1d</sub> | ✓ SAFE | Food catering services for trains, flights, buses | 📈 BULL_ANY_MID | 58 | 🔄50 | ↑1.011 | ↑2d | — | +2.2% | 29.71/29.36 | +0.73% | 20% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>📶W9 · W↑56d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | Pharmaceuticals: generics, branded drugs, consumer wellness products | 📈 BULL_ANY_MID | 49 | 🔄73 | ↑1.031 | ↑1d | — | +3.9% | 44.71/41.57 | +3.92% | 20% |
| [GROWW](https://in.tradingview.com/chart/?symbol=NSE:GROWW)<br><sub>📶W9 · ↑CMF9d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 22 | ↑50 | ↑1.018 | ↑3d | — | +4.0% | 33.78/30.78 | +1.28% | 20% |
| [VADILALIND](https://in.tradingview.com/chart/?symbol=NSE:VADILALIND)<br><sub>📶W9 · W↑32d · ↑CMF11d</sub> | ✓ SAFE | Ice cream and frozen desserts manufacturer, retail and foodservice | 📈 BULL_ANY_MID | 21 | ↑82 | ↑1.027 | ↑4d | — | +6.7% | 39.66/36.85 | +1.15% | 20% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Large-diameter pipes, steel billets, rebars infrastructure | 📈 BULL_ANY_MID | 18 | ↑96 | ↓1.037 | ↑2d | — | +7.1% | 69.64/68.33 | -0.17% | 20% |
| [HEALTHX](https://in.tradingview.com/chart/?symbol=NSE:HEALTHX)<br><sub>📶W9 · W↑51d · ↓CMF24d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 18 | ↓59 | ↓1.000 | ↑2d | — | +1.1% | 21.16/20.21 | -1.67% | 20% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>📶W9 · W↑68d · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | IT services, digital transformation, global enterprises | 📈 BULL_ANY_MID | 17 | ↑41 | ↑1.031 | ↑3d | — | +5.2% | 27.46/21.97 | +2.31% | 20% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>📶W9 · W↑65d · ↑CMF15d</sub> | ✓ SAFE | Heavy equipment manufacturing for oil gas steel power | 📈 BULL_ANY_MID | 17 | ↓93 | ↓1.002 | ↑3d | — | +2.8% | 39.54/37.19 | -5.30% | 20% |
| [AGI](https://in.tradingview.com/chart/?symbol=NSE:AGI)<br><sub>📶W9 · W↑72d · ↑CMF15d</sub> | ✓ SAFE | Glass containers PET bottles closures beverages pharma | 📈 BULL_ANY_MID | 10 | ↑49 | ↑1.012 | ↑27d | — | +20.2% | 43.13/42.99 | +0.33% | 20% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>📶W9 · W↑17d · ↑CMF12d</sub> | ✓ SAFE | Shock absorbers struts two wheeler four wheeler OEM aftermarket | 📈 BULL_ANY_MID | 3 | ↑78 | ↓1.021 | ↑17d | — | +21.7% | 42.61/41.77 | -0.68% | 20% |
| [INDNIPPON](https://in.tradingview.com/chart/?symbol=NSE:INDNIPPON)<br><sub>📶W9 · W↑60d · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | Electronic ignition systems two-wheeler three-wheeler portable engines | 📈 BULL_ANY_MID | 2 | ↑78 | ↑1.049 | ↑18d | — | +19.5% | 68.38/66.1 | +3.14% | 20% |
| [RAMCOSYS](https://in.tradingview.com/chart/?symbol=NSE:RAMCOSYS)<br><sub>📶W9 · W↑37d · ↑CMF22d</sub> | ✓ SAFE | Cloud ERP software for aviation and manufacturing businesses | 📈 BULL_ANY_MID | 0 | ↑98 | ↓1.123 | ↑33d | — | +124.7% | 77.47/77.21 | +0.06% | 10% 🟨 |
| [RATNAMANI](https://in.tradingview.com/chart/?symbol=NSE:RATNAMANI)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Stainless steel seamless welded pipes oil gas petrochemical power | 📈 BULL_ANY_MID | 59 | 🔄54 | ↑1.011 | ↑1d | — | +1.1% | -9.53/-11.85 | +1.07% | 20% |
| [AMBER](https://in.tradingview.com/chart/?symbol=NSE:AMBER)<br><sub>↓CMF8d</sub> | ✓ SAFE | AC manufacturing and EMS for consumer appliances | 📈 BULL_ANY_MID | 58 | 🔄55 | ↑1.006 | ↑2d | — | +1.9% | -17.4/-19.97 | +0.14% | 20% |
| [ICICIGI](https://in.tradingview.com/chart/?symbol=NSE:ICICIGI)<br><sub>W↑17d · ↑CMF1d</sub> | ⚠ CAUTION | General insurance motor health property casualty India | 📈 BULL_ANY_MID | 58 | 🔄30 | ↑1.006 | ↑2d | — | +1.2% | -8.02/-10.47 | +0.50% | 20% |
| [MUTHOOTFIN](https://in.tradingview.com/chart/?symbol=NSE:MUTHOOTFIN)<br><sub>🚀SS · ↓CMF1d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 51 | 🔄30 | ↑1.005 | ↓9d | — | -2.4% | -40.8/-42.17 | +3.40% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>W↑14d · 🚀SS · ↑CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 27 | ↓7 | ↑1.002 | ↑3d | — | +1.1% | 6.95/5.11 | +0.07% | 20% |
| [BEL](https://in.tradingview.com/chart/?symbol=NSE:BEL)<br><sub>🚀SS · ↓CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 27 | ↓41 | ↑1.006 | ↑3d | — | +1.5% | -0.82/-6.13 | +0.71% | 20% |
| [TECHM](https://in.tradingview.com/chart/?symbol=NSE:TECHM)<br><sub>🚀SS · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 23 | ↓22 | ↑1.004 | ↓7d | — | -0.5% | -41.06/-43.01 | +1.64% | 20% |
| [MAZDOCK](https://in.tradingview.com/chart/?symbol=NSE:MAZDOCK)<br><sub>W↑7d · ↓CMF30d</sub> | ✓ SAFE | Defense warships submarines naval shipbuilding PSU | 📈 BULL_ANY_MID | 23 | ↑38 | ↑1.017 | ↑2d | — | +3.6% | 10.55/8.39 | +1.43% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>W↑14d · ↓CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 18 | ↓35 | ↓1.003 | ↑2d | — | +1.2% | 11.82/9.95 | -0.85% | 20% |
| [HITECH](https://in.tradingview.com/chart/?symbol=NSE:HITECH)<br><sub>W↑65d · ↑CMF1d</sub> | ✓ SAFE | ERW steel pipes tubes for construction infrastructure automotive | 📈 BULL_ANY_MID | 18 | ↓27 | ↓1.001 | ↓2d | — | +0.2% | -5.38/-5.71 | -0.31% | 20% |
| [VBL](https://in.tradingview.com/chart/?symbol=NSE:VBL)<br><sub>🚀SS · ↓CMF10d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 16 | ↓67 | ↑1.004 | ↓14d | — | -1.2% | -13.92/-16.25 | +1.07% | 20% |
| [GICRE](https://in.tradingview.com/chart/?symbol=NSE:GICRE)<br><sub>↓CMF30d</sub> | ✓ SAFE | Reinsurance underwriting for property casualty risks domestically globally | 📈 BULL_ANY_MID | 13 | ↓31 | ↑1.000 | ↓17d | — | -4.4% | -45.14/-45.8 | +0.67% | 20% |
| [WIPRO](https://in.tradingview.com/chart/?symbol=NSE:WIPRO)<br><sub>🚀SS · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 10 | ↓4 | ↑1.001 | ↓32d | — | -8.5% | -44.09/-47.74 | +1.03% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>🚀SS · ↓CMF15d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓68 | ↑0.984 | ↓31d | — | -9.0% | -43.92/-44.37 | +0.45% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>🚀SS · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓50 | ↑0.994 | ↓24d | — | -4.0% | -45.22/-45.43 | +0.10% | 20% |

```
NSE:ENDURANCE,NSE:VAIBHAVGBL,NSE:TRAVELFOOD,NSE:ZYDUSLIFE,NSE:GROWW,NSE:VADILALIND,NSE:WELCORP,NSE:HEALTHX,NSE:COFORGE,NSE:LLOYDSENGG,NSE:AGI,NSE:GABRIEL,NSE:INDNIPPON,NSE:RAMCOSYS,NSE:RATNAMANI,NSE:AMBER,NSE:ICICIGI,NSE:MUTHOOTFIN,NSE:ITC,NSE:BEL,NSE:TECHM,NSE:MAZDOCK,NSE:BPCL,NSE:HITECH,NSE:VBL,NSE:GICRE,NSE:WIPRO,NSE:HINDALCO,NSE:COALINDIA
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
