> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-09-02
*Generated 2026-09-02 15:46 IST*

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

**Total bull crosses today: 60** · 22 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MAITHANALL,NSE:DRAGARWQ,NSE:ELANTAS,NSE:INFY,NSE:JAYKAY,NSE:HCLTECH,NSE:CENTENKA,NSE:XPROINDIA,NSE:HYUNDAI,NSE:WINDLAS,NSE:ANTHEM,NSE:CLEAN,NSE:SIGMAADV,NSE:TATACAP,NSE:EIHAHOTELS,NSE:SUNDARMFIN,NSE:THEJO,NSE:PREMEXPLN,NSE:FEDERALBNK,NSE:MRPL,NSE:PANAMAPET,NSE:YATRA,NSE:BEPL,NSE:ARTEMISMED,NSE:NAHARSPING,NSE:INDOSTAR,NSE:AEROPLANE,NSE:MONTECARLO,NSE:63MOONS,NSE:CHENNPETRO,NSE:TARSONS,NSE:DIVGIITTS,NSE:CLSEL,NSE:GUJALKALI,NSE:TINNARUBR,NSE:SEAMECLTD,NSE:TORNTPOWER,NSE:NINSYS,NSE:EMSLIMITED,NSE:DLINKINDIA,NSE:NUVOCO,NSE:ZOTA,NSE:TCC,NSE:PARKHOTELS,NSE:ASTRAZEN,NSE:CREDITACC,NSE:EPACK,NSE:ERIS,NSE:ONGC,NSE:KRISHNADEF,NSE:IONEXCHANG,NSE:SRF,NSE:ACCELYA,NSE:BFINVEST,NSE:VTL,NSE:ROTO,NSE:GUJENERGY,NSE:ASTERDM,NSE:DHANUKA,NSE:HLEGLAS
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (36)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MAITHANALL](https://in.tradingview.com/chart/?symbol=NSE:MAITHANALL)<br><sub>📶W9 · W↑3d · RVOL13x · ↑CMF1d</sub> | ✓ SAFE | Ferro alloys manufacturer for steel industry globally | ⚡ BULL_ANY_PPV | 94 | 🔄46 | ↑1.030 | ↑1d | SQ·PV | +4.8% | 17.61/14.35 | +4.79% | 20% |
| [DRAGARWQ](https://in.tradingview.com/chart/?symbol=NSE:DRAGARWQ)<br><sub>📶W9 · ↑CMF15d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 63 | ↑50 | ↑1.024 | ↑2d | SQ·PV | +3.6% | 22.93/15.03 | +2.24% | 20% |
| [ELANTAS](https://in.tradingview.com/chart/?symbol=NSE:ELANTAS)<br><sub>📶W9 · ↓CMF0d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 62 | ↑50 | ↑1.018 | ↑3d | SQ·PV | +3.1% | 22.46/20.9 | +2.35% | 20% |
| [INFY](https://in.tradingview.com/chart/?symbol=NSE:INFY)<br><sub>📶W9 · W↑37d · ↑CMF3d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 59 | 🔄17 | ↑1.010 | ↑1d | PV | +1.2% | -6.55/-11.02 | +1.22% | 20% |
| [JAYKAY](https://in.tradingview.com/chart/?symbol=NSE:JAYKAY)<br><sub>📶W9 · ↑CMF5d</sub> | ✓ SAFE | 3D printing and additive manufacturing solutions for industrial prototyping | ⚡ BULL_ANY_PPV | 58 | ↑50 | ↑1.060 | ↑2d | SQ·PV | +12.7% | 0.97/-6.26 | +5.49% | 20% |
| [HCLTECH](https://in.tradingview.com/chart/?symbol=NSE:HCLTECH)<br><sub>📶W9 · W↑42d · 🚀SS · ↓CMF4d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 54 | 🔄42 | ↑1.024 | ↑1d | PV | +3.0% | -1.66/-9.73 | +3.04% | 20% |
| [CENTENKA](https://in.tradingview.com/chart/?symbol=NSE:CENTENKA)<br><sub>📶W9 · 🚀SS·199x · ↑CMF0d</sub> | ✓ SAFE | Synthetic yarn manufacturer for textiles and automotive | ⚡ BULL_ANY_PPV | 49 | 🔄77 | ↑1.067 | ↑1d | PV | +10.7% | -23.01/-32.58 | +10.71% | 20% |
| [XPROINDIA](https://in.tradingview.com/chart/?symbol=NSE:XPROINDIA)<br><sub>📶W9 · RVOL16x · ↑CMF0d</sub> | ✓ SAFE | Polymer films and sheets for packaging and industrial applications | ⚡ BULL_ANY_PPV | 49 | 🔄70 | ↑1.098 | ↑1d | PV | +13.2% | 0.91/-11.34 | +13.19% | 20% |
| [HYUNDAI](https://in.tradingview.com/chart/?symbol=NSE:HYUNDAI)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 5 | ↑47 | ↑1.017 | ↑23d | PV | +15.3% | 45.93/42.54 | +0.87% | 20% |
| [WINDLAS](https://in.tradingview.com/chart/?symbol=NSE:WINDLAS)<br><sub>📶W9 · W↑68d · ↑CMF16d</sub> | ✓ SAFE | Oral solid liquid pharma formulations CDMO manufacturing | ⚡ BULL_ANY_PPV | 3 | ↑81 | ↑1.093 | ↑17d | PV | +30.6% | 69.67/65.63 | +8.75% | 20% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>📶W9 · W↑28d · ↑CMF1d</sub> | ✓ SAFE | Contract research development manufacturing biotech pharma | ⚡ BULL_ANY_PPV | 0 | ↑77 | ↑1.033 | ↑28d | PV | +21.4% | 61.12/58.59 | +1.08% | 20% |
| [CLEAN](https://in.tradingview.com/chart/?symbol=NSE:CLEAN)<br><sub>📶W9 · W↑18d · ↑CMF14d</sub> | ✓ SAFE | Specialty chemicals manufacturing, catalytic processes, pharma and industrial | ⚡ BULL_ANY_PPV | 0 | ↑42 | ↑1.037 | ↑23d | PV | +17.6% | 40.06/35.89 | +4.36% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [TATACAP](https://in.tradingview.com/chart/?symbol=NSE:TATACAP)<br><sub>📶W9 · W↑57d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.013 | ↑1d | SQ | +1.9% | 11.85/8.42 | +1.86% | 20% |
| [EIHAHOTELS](https://in.tradingview.com/chart/?symbol=NSE:EIHAHOTELS)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄28 | ↑1.025 | ↑1d | SQ | +5.0% | -13.73/-17.73 | +4.96% | 20% |
| [SUNDARMFIN](https://in.tradingview.com/chart/?symbol=NSE:SUNDARMFIN)<br><sub>📶W9 · W↑53d · ↑CMF1d</sub> | ⚠ CAUTION | Vehicle and equipment finance NBFC retail lending | 📈 BULL_ANY_MID | 69 | ↑41 | ↑1.001 | ↑1d | SQ | +0.4% | 6.37/5.46 | +0.38% | 20% |
| [THEJO](https://in.tradingview.com/chart/?symbol=NSE:THEJO)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | Bulk material handling, mineral processing, corrosion protection equipment | 📈 BULL_ANY_MID | 69 | ↑77 | ↑1.010 | ↑1d | SQ | +1.1% | 6.28/3.73 | +1.12% | 20% |
| [PREMEXPLN](https://in.tradingview.com/chart/?symbol=NSE:PREMEXPLN)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Explosives propellants detonators defense space mining manufacturing | 📈 BULL_ANY_MID | 68 | ↑64 | ↑1.006 | ↑2d | SQ | +0.9% | 19.59/10.3 | +0.73% | 20% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Retail corporate banking Kerala-headquartered private sector bank | 📈 BULL_ANY_MID | 67 | ↑82 | ↑1.005 | ↓3d | SQ | +2.6% | -12.99/-14.33 | +1.17% | 20% |
| [MRPL](https://in.tradingview.com/chart/?symbol=NSE:MRPL)<br><sub>📶W9 · W↑38d · ↓CMF11d</sub> | ✓ SAFE | Crude oil refining, petrochemicals, fuel production for domestic markets | 📈 BULL_ANY_MID | 64 | ↑63 | ↑1.016 | ↑1d | SQ | +2.2% | 1.07/-0.4 | +2.22% | 20% |
| [PANAMAPET](https://in.tradingview.com/chart/?symbol=NSE:PANAMAPET)<br><sub>📶W9 · ↓CMF15d</sub> | ✓ SAFE | Specialty petroleum products for pharma, cosmetics, rubber | 📈 BULL_ANY_MID | 63 | ↑92 | ↑1.017 | ↑2d | SQ | +3.9% | -6.49/-11.78 | +0.55% | 10% 🟨 |
| [YATRA](https://in.tradingview.com/chart/?symbol=NSE:YATRA)<br><sub>📶W9 · W↑18d · ↑CMF16d</sub> | ✓ SAFE | Online travel bookings for leisure and corporate travelers | 📈 BULL_ANY_MID | 58 | ↑28 | ↓1.018 | ↑2d | SQ | +7.3% | -2.17/-3.96 | +0.23% | 20% |
| [BEPL](https://in.tradingview.com/chart/?symbol=NSE:BEPL)<br><sub>📶W9 · ↑CMF7d</sub> | ✓ SAFE | ABS SAN resin manufacturer for automotive consumer goods | 📈 BULL_ANY_MID | 58 | ↑83 | ↓1.020 | ↑2d | SQ | +5.1% | 34.71/33.42 | +0.10% | 20% |
| [ARTEMISMED](https://in.tradingview.com/chart/?symbol=NSE:ARTEMISMED)<br><sub>📶W9 · W↑43d · ↓CMF5d</sub> | ✓ SAFE | Tertiary care hospital operator, multi-specialty healthcare delivery Gurgaon | 📈 BULL_ANY_MID | 58 | ↑78 | ↓1.000 | ↑2d | SQ | +1.0% | 42.4/42.15 | -2.21% | 20% |
| [NAHARSPING](https://in.tradingview.com/chart/?symbol=NSE:NAHARSPING)<br><sub>📶W9 · ↓CMF2d</sub> | ✓ SAFE | Cotton yarn and hosiery knitwear manufacturer exporting globally | 📈 BULL_ANY_MID | 58 | ↑79 | ↓0.999 | ↓2d | SQ | +1.9% | -12.93/-16.31 | -1.54% | 5% |
| [INDOSTAR](https://in.tradingview.com/chart/?symbol=NSE:INDOSTAR)<br><sub>📶W9 · W↑3d · ↓CMF2d</sub> | ✓ SAFE | Commercial vehicle finance NBFC underserved retail markets | 📈 BULL_ANY_MID | 54 | 🔄53 | ↑1.024 | ↑1d | — | +3.6% | 22.26/20.54 | +3.57% | 20% |
| [AEROPLANE](https://in.tradingview.com/chart/?symbol=NSE:AEROPLANE)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Basmati rice processor exporter FMCG packaged food | 📈 BULL_ANY_MID | 45 | 🔄50 | ↑1.006 | ↓15d | — | -2.7% | -32.39/-35.3 | +2.33% | 20% |
| [MONTECARLO](https://in.tradingview.com/chart/?symbol=NSE:MONTECARLO)<br><sub>📶W9 · W↑8d · ↓CMF30d</sub> | ✓ SAFE | Woolen cotton apparel manufacturer winter wear retail | 📈 BULL_ANY_MID | 28 | ↑30 | ↑1.012 | ↑2d | — | +2.6% | 8.0/6.71 | +0.96% | 20% |
| [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS)<br><sub>📶W9 · 🚀SS · ↓CMF3d · DEL55%(T-1)</sub> | ✓ SAFE | Financial software IP, banking and capital markets infrastructure | 📈 BULL_ANY_MID | 24 | ↑63 | ↑1.025 | ↑1d | — | +3.8% | -9.79/-14.7 | +3.81% | 20% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>📶W9 · W↑38d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Refines crude oil, produces petroleum products, lubricants | 📈 BULL_ANY_MID | 22 | ↑88 | ↑1.025 | ↑3d | — | +5.4% | 30.49/28.69 | +1.95% | 20% |
| [TARSONS](https://in.tradingview.com/chart/?symbol=NSE:TARSONS)<br><sub>📶W9 · ↑CMF15d</sub> | ✓ SAFE | Plastic labware manufacturer for research and diagnostic labs | 📈 BULL_ANY_MID | 18 | ↑91 | ↓1.019 | ↑2d | — | +4.1% | 26.26/25.61 | +0.36% | 20% |
| [DIVGIITTS](https://in.tradingview.com/chart/?symbol=NSE:DIVGIITTS)<br><sub>📶W9 · W↑23d · ↑CMF17d</sub> | ✓ SAFE | Automotive drivetrain components, transfer cases, all-terrain vehicles | 📈 BULL_ANY_MID | 17 | ↑95 | ↓1.025 | ↑3d | — | +5.9% | 39.78/37.25 | -1.92% | 20% |
| [CLSEL](https://in.tradingview.com/chart/?symbol=NSE:CLSEL)<br><sub>📶W9 · W↑13d · ↑CMF7d</sub> | ✓ SAFE | Basmati rice milling, packing, exporting for global food markets | 📈 BULL_ANY_MID | 11 | ↑60 | ↓1.010 | ↑9d | — | +8.2% | 33.97/33.43 | -0.33% | 20% |
| [GUJALKALI](https://in.tradingview.com/chart/?symbol=NSE:GUJALKALI)<br><sub>📶W9 · W↑28d · ↑CMF5d</sub> | ✓ SAFE | Caustic soda chlorine chemicals manufacturing industrial applications | 📈 BULL_ANY_MID | 10 | ↑78 | ↓1.013 | ↑10d | — | +7.6% | 43.9/42.8 | +0.21% | 20% |
| [TINNARUBR](https://in.tradingview.com/chart/?symbol=NSE:TINNARUBR)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Waste tyre recycling into crumb rubber and steel | 📈 BULL_ANY_MID | 10 | ↑78 | ↑0.998 | ↓15d | — | -5.9% | -39.78/-41.23 | -0.01% | 20% |
| [SEAMECLTD](https://in.tradingview.com/chart/?symbol=NSE:SEAMECLTD)<br><sub>📶W9 · W↑18d · ★ · ↑CMF13d</sub> | ✓ SAFE | Offshore diving vessels, subsea engineering, oil and gas | 📈 BULL_ANY_MID | 0 | ↑86 | ↑1.044 | ↑28d | — | +24.3% | 59.33/57.2 | +3.39% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MAITHANALL,NSE:DRAGARWQ,NSE:ELANTAS,NSE:INFY,NSE:JAYKAY,NSE:HCLTECH,NSE:CENTENKA,NSE:XPROINDIA,NSE:HYUNDAI,NSE:WINDLAS,NSE:ANTHEM,NSE:CLEAN,NSE:SIGMAADV,NSE:TATACAP,NSE:EIHAHOTELS,NSE:SUNDARMFIN,NSE:THEJO,NSE:PREMEXPLN,NSE:FEDERALBNK,NSE:MRPL,NSE:PANAMAPET,NSE:YATRA,NSE:BEPL,NSE:ARTEMISMED,NSE:NAHARSPING,NSE:INDOSTAR,NSE:AEROPLANE,NSE:MONTECARLO,NSE:63MOONS,NSE:CHENNPETRO,NSE:TARSONS,NSE:DIVGIITTS,NSE:CLSEL,NSE:GUJALKALI,NSE:TINNARUBR,NSE:SEAMECLTD
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (53)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MAITHANALL](https://in.tradingview.com/chart/?symbol=NSE:MAITHANALL)<br><sub>📶W9 · W↑3d · RVOL13x · ↑CMF1d</sub> | ✓ SAFE | Ferro alloys manufacturer for steel industry globally | ⚡ BULL_ANY_PPV | 94 | 🔄46 | ↑1.030 | ↑1d | SQ·PV | +4.8% | 17.61/14.35 | +4.79% | 20% |
| [DRAGARWQ](https://in.tradingview.com/chart/?symbol=NSE:DRAGARWQ)<br><sub>📶W9 · ↑CMF15d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 63 | ↑50 | ↑1.024 | ↑2d | SQ·PV | +3.6% | 22.93/15.03 | +2.24% | 20% |
| [ELANTAS](https://in.tradingview.com/chart/?symbol=NSE:ELANTAS)<br><sub>📶W9 · ↓CMF0d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 62 | ↑50 | ↑1.018 | ↑3d | SQ·PV | +3.1% | 22.46/20.9 | +2.35% | 20% |
| [INFY](https://in.tradingview.com/chart/?symbol=NSE:INFY)<br><sub>📶W9 · W↑37d · ↑CMF3d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 59 | 🔄17 | ↑1.010 | ↑1d | PV | +1.2% | -6.55/-11.02 | +1.22% | 20% |
| [JAYKAY](https://in.tradingview.com/chart/?symbol=NSE:JAYKAY)<br><sub>📶W9 · ↑CMF5d</sub> | ✓ SAFE | 3D printing and additive manufacturing solutions for industrial prototyping | ⚡ BULL_ANY_PPV | 58 | ↑50 | ↑1.060 | ↑2d | SQ·PV | +12.7% | 0.97/-6.26 | +5.49% | 20% |
| [HCLTECH](https://in.tradingview.com/chart/?symbol=NSE:HCLTECH)<br><sub>📶W9 · W↑42d · 🚀SS · ↓CMF4d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 54 | 🔄42 | ↑1.024 | ↑1d | PV | +3.0% | -1.66/-9.73 | +3.04% | 20% |
| [CENTENKA](https://in.tradingview.com/chart/?symbol=NSE:CENTENKA)<br><sub>📶W9 · 🚀SS·199x · ↑CMF0d</sub> | ✓ SAFE | Synthetic yarn manufacturer for textiles and automotive | ⚡ BULL_ANY_PPV | 49 | 🔄77 | ↑1.067 | ↑1d | PV | +10.7% | -23.01/-32.58 | +10.71% | 20% |
| [XPROINDIA](https://in.tradingview.com/chart/?symbol=NSE:XPROINDIA)<br><sub>📶W9 · RVOL16x · ↑CMF0d</sub> | ✓ SAFE | Polymer films and sheets for packaging and industrial applications | ⚡ BULL_ANY_PPV | 49 | 🔄70 | ↑1.098 | ↑1d | PV | +13.2% | 0.91/-11.34 | +13.19% | 20% |
| [HYUNDAI](https://in.tradingview.com/chart/?symbol=NSE:HYUNDAI)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 5 | ↑47 | ↑1.017 | ↑23d | PV | +15.3% | 45.93/42.54 | +0.87% | 20% |
| [WINDLAS](https://in.tradingview.com/chart/?symbol=NSE:WINDLAS)<br><sub>📶W9 · W↑68d · ↑CMF16d</sub> | ✓ SAFE | Oral solid liquid pharma formulations CDMO manufacturing | ⚡ BULL_ANY_PPV | 3 | ↑81 | ↑1.093 | ↑17d | PV | +30.6% | 69.67/65.63 | +8.75% | 20% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>📶W9 · W↑28d · ↑CMF1d</sub> | ✓ SAFE | Contract research development manufacturing biotech pharma | ⚡ BULL_ANY_PPV | 0 | ↑77 | ↑1.033 | ↑28d | PV | +21.4% | 61.12/58.59 | +1.08% | 20% |
| [CLEAN](https://in.tradingview.com/chart/?symbol=NSE:CLEAN)<br><sub>📶W9 · W↑18d · ↑CMF14d</sub> | ✓ SAFE | Specialty chemicals manufacturing, catalytic processes, pharma and industrial | ⚡ BULL_ANY_PPV | 0 | ↑42 | ↑1.037 | ↑23d | PV | +17.6% | 40.06/35.89 | +4.36% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [TATACAP](https://in.tradingview.com/chart/?symbol=NSE:TATACAP)<br><sub>📶W9 · W↑57d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.013 | ↑1d | SQ | +1.9% | 11.85/8.42 | +1.86% | 20% |
| [EIHAHOTELS](https://in.tradingview.com/chart/?symbol=NSE:EIHAHOTELS)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄28 | ↑1.025 | ↑1d | SQ | +5.0% | -13.73/-17.73 | +4.96% | 20% |
| [SUNDARMFIN](https://in.tradingview.com/chart/?symbol=NSE:SUNDARMFIN)<br><sub>📶W9 · W↑53d · ↑CMF1d</sub> | ⚠ CAUTION | Vehicle and equipment finance NBFC retail lending | 📈 BULL_ANY_MID | 69 | ↑41 | ↑1.001 | ↑1d | SQ | +0.4% | 6.37/5.46 | +0.38% | 20% |
| [THEJO](https://in.tradingview.com/chart/?symbol=NSE:THEJO)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | Bulk material handling, mineral processing, corrosion protection equipment | 📈 BULL_ANY_MID | 69 | ↑77 | ↑1.010 | ↑1d | SQ | +1.1% | 6.28/3.73 | +1.12% | 20% |
| [PREMEXPLN](https://in.tradingview.com/chart/?symbol=NSE:PREMEXPLN)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Explosives propellants detonators defense space mining manufacturing | 📈 BULL_ANY_MID | 68 | ↑64 | ↑1.006 | ↑2d | SQ | +0.9% | 19.59/10.3 | +0.73% | 20% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Retail corporate banking Kerala-headquartered private sector bank | 📈 BULL_ANY_MID | 67 | ↑82 | ↑1.005 | ↓3d | SQ | +2.6% | -12.99/-14.33 | +1.17% | 20% |
| [MRPL](https://in.tradingview.com/chart/?symbol=NSE:MRPL)<br><sub>📶W9 · W↑38d · ↓CMF11d</sub> | ✓ SAFE | Crude oil refining, petrochemicals, fuel production for domestic markets | 📈 BULL_ANY_MID | 64 | ↑63 | ↑1.016 | ↑1d | SQ | +2.2% | 1.07/-0.4 | +2.22% | 20% |
| [PANAMAPET](https://in.tradingview.com/chart/?symbol=NSE:PANAMAPET)<br><sub>📶W9 · ↓CMF15d</sub> | ✓ SAFE | Specialty petroleum products for pharma, cosmetics, rubber | 📈 BULL_ANY_MID | 63 | ↑92 | ↑1.017 | ↑2d | SQ | +3.9% | -6.49/-11.78 | +0.55% | 10% 🟨 |
| [YATRA](https://in.tradingview.com/chart/?symbol=NSE:YATRA)<br><sub>📶W9 · W↑18d · ↑CMF16d</sub> | ✓ SAFE | Online travel bookings for leisure and corporate travelers | 📈 BULL_ANY_MID | 58 | ↑28 | ↓1.018 | ↑2d | SQ | +7.3% | -2.17/-3.96 | +0.23% | 20% |
| [BEPL](https://in.tradingview.com/chart/?symbol=NSE:BEPL)<br><sub>📶W9 · ↑CMF7d</sub> | ✓ SAFE | ABS SAN resin manufacturer for automotive consumer goods | 📈 BULL_ANY_MID | 58 | ↑83 | ↓1.020 | ↑2d | SQ | +5.1% | 34.71/33.42 | +0.10% | 20% |
| [ARTEMISMED](https://in.tradingview.com/chart/?symbol=NSE:ARTEMISMED)<br><sub>📶W9 · W↑43d · ↓CMF5d</sub> | ✓ SAFE | Tertiary care hospital operator, multi-specialty healthcare delivery Gurgaon | 📈 BULL_ANY_MID | 58 | ↑78 | ↓1.000 | ↑2d | SQ | +1.0% | 42.4/42.15 | -2.21% | 20% |
| [NAHARSPING](https://in.tradingview.com/chart/?symbol=NSE:NAHARSPING)<br><sub>📶W9 · ↓CMF2d</sub> | ✓ SAFE | Cotton yarn and hosiery knitwear manufacturer exporting globally | 📈 BULL_ANY_MID | 58 | ↑79 | ↓0.999 | ↓2d | SQ | +1.9% | -12.93/-16.31 | -1.54% | 5% |
| [INDOSTAR](https://in.tradingview.com/chart/?symbol=NSE:INDOSTAR)<br><sub>📶W9 · W↑3d · ↓CMF2d</sub> | ✓ SAFE | Commercial vehicle finance NBFC underserved retail markets | 📈 BULL_ANY_MID | 54 | 🔄53 | ↑1.024 | ↑1d | — | +3.6% | 22.26/20.54 | +3.57% | 20% |
| [AEROPLANE](https://in.tradingview.com/chart/?symbol=NSE:AEROPLANE)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Basmati rice processor exporter FMCG packaged food | 📈 BULL_ANY_MID | 45 | 🔄50 | ↑1.006 | ↓15d | — | -2.7% | -32.39/-35.3 | +2.33% | 20% |
| [MONTECARLO](https://in.tradingview.com/chart/?symbol=NSE:MONTECARLO)<br><sub>📶W9 · W↑8d · ↓CMF30d</sub> | ✓ SAFE | Woolen cotton apparel manufacturer winter wear retail | 📈 BULL_ANY_MID | 28 | ↑30 | ↑1.012 | ↑2d | — | +2.6% | 8.0/6.71 | +0.96% | 20% |
| [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS)<br><sub>📶W9 · 🚀SS · ↓CMF3d · DEL55%(T-1)</sub> | ✓ SAFE | Financial software IP, banking and capital markets infrastructure | 📈 BULL_ANY_MID | 24 | ↑63 | ↑1.025 | ↑1d | — | +3.8% | -9.79/-14.7 | +3.81% | 20% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>📶W9 · W↑38d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Refines crude oil, produces petroleum products, lubricants | 📈 BULL_ANY_MID | 22 | ↑88 | ↑1.025 | ↑3d | — | +5.4% | 30.49/28.69 | +1.95% | 20% |
| [TARSONS](https://in.tradingview.com/chart/?symbol=NSE:TARSONS)<br><sub>📶W9 · ↑CMF15d</sub> | ✓ SAFE | Plastic labware manufacturer for research and diagnostic labs | 📈 BULL_ANY_MID | 18 | ↑91 | ↓1.019 | ↑2d | — | +4.1% | 26.26/25.61 | +0.36% | 20% |
| [DIVGIITTS](https://in.tradingview.com/chart/?symbol=NSE:DIVGIITTS)<br><sub>📶W9 · W↑23d · ↑CMF17d</sub> | ✓ SAFE | Automotive drivetrain components, transfer cases, all-terrain vehicles | 📈 BULL_ANY_MID | 17 | ↑95 | ↓1.025 | ↑3d | — | +5.9% | 39.78/37.25 | -1.92% | 20% |
| [CLSEL](https://in.tradingview.com/chart/?symbol=NSE:CLSEL)<br><sub>📶W9 · W↑13d · ↑CMF7d</sub> | ✓ SAFE | Basmati rice milling, packing, exporting for global food markets | 📈 BULL_ANY_MID | 11 | ↑60 | ↓1.010 | ↑9d | — | +8.2% | 33.97/33.43 | -0.33% | 20% |
| [GUJALKALI](https://in.tradingview.com/chart/?symbol=NSE:GUJALKALI)<br><sub>📶W9 · W↑28d · ↑CMF5d</sub> | ✓ SAFE | Caustic soda chlorine chemicals manufacturing industrial applications | 📈 BULL_ANY_MID | 10 | ↑78 | ↓1.013 | ↑10d | — | +7.6% | 43.9/42.8 | +0.21% | 20% |
| [TINNARUBR](https://in.tradingview.com/chart/?symbol=NSE:TINNARUBR)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Waste tyre recycling into crumb rubber and steel | 📈 BULL_ANY_MID | 10 | ↑78 | ↑0.998 | ↓15d | — | -5.9% | -39.78/-41.23 | -0.01% | 20% |
| [SEAMECLTD](https://in.tradingview.com/chart/?symbol=NSE:SEAMECLTD)<br><sub>📶W9 · W↑18d · ★ · ↑CMF13d</sub> | ✓ SAFE | Offshore diving vessels, subsea engineering, oil and gas | 📈 BULL_ANY_MID | 0 | ↑86 | ↑1.044 | ↑28d | — | +24.3% | 59.33/57.2 | +3.39% | 20% |
| [TORNTPOWER](https://in.tradingview.com/chart/?symbol=NSE:TORNTPOWER)<br><sub>↓CMF21d · 🎯SLING</sub> | ⚠ CAUTION | Power generation transmission distribution utility Gujarat Maharashtra | 🔥 BULL_OS_PPV | 40 | 🔄21 | ↑1.004 | ↓33d | PV | -10.2% | -56.48/-60.64 | +2.43% | 20% |
| [NINSYS](https://in.tradingview.com/chart/?symbol=NSE:NINSYS)<br><sub>↑CMF2d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 75 | 🔄90 | ↑0.991 | ↓53d | SQ·PV | +2.3% | -35.17/-37.49 | +0.08% | 5% |
| [EMSLIMITED](https://in.tradingview.com/chart/?symbol=NSE:EMSLIMITED)<br><sub>🚀SS·20x · ↓CMF12d</sub> | ✓ SAFE | Water treatment EPC contractor for municipal urban infrastructure | ⚡ BULL_ANY_PPV | 59 | 🔄54 | ↑1.014 | ↑1d | PV | +3.9% | -27.05/-32.56 | +3.87% | 10% 🟨 |
| [DLINKINDIA](https://in.tradingview.com/chart/?symbol=NSE:DLINKINDIA)<br><sub>↑CMF10d</sub> | ✓ SAFE | Networking equipment distribution, consumer and enterprise markets | ⚡ BULL_ANY_PPV | 54 | 🔄35 | ↑1.016 | ↑1d | PV | +2.7% | -0.79/-3.65 | +2.69% | 20% |
| [NUVOCO](https://in.tradingview.com/chart/?symbol=NSE:NUVOCO)<br><sub>↑CMF0d</sub> | ⚠ CAUTION | Cement and ready-mix concrete manufacturer East North India | ⚡ BULL_ANY_PPV | 29 | ↑32 | ↑1.010 | ↑1d | PV | +1.6% | -39.17/-42.65 | +1.64% | 20% |
| [ZOTA](https://in.tradingview.com/chart/?symbol=NSE:ZOTA)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Pharma manufacturer: tablets, syrups, Ayurveda, OTC products | 🟢 BULL_OVERSOLD | 35 | 🔄12 | ↑0.996 | ↓60d+ | — | -9.9% | -59.69/-60.39 | +4.85% | 20% |
| [TCC](https://in.tradingview.com/chart/?symbol=NSE:TCC)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Real estate aggregation, digital infrastructure, consumer ecosystem platform | 🟢 BULL_OVERSOLD | 35 | 🔄50 | ↑0.987 | ↓22d | — | -19.0% | -62.14/-64.53 | +0.80% | 20% |
| [PARKHOTELS](https://in.tradingview.com/chart/?symbol=NSE:PARKHOTELS)<br><sub>↓CMF23d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 35 | 🔄23 | ↑0.999 | ↓23d | — | -6.8% | -59.64/-61.18 | +1.90% | 20% |
| [ONGC](https://in.tradingview.com/chart/?symbol=NSE:ONGC)<br><sub>🚀SS · ↓CMF23d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 59 | 🔄28 | ↑1.007 | ↑1d | — | +2.0% | -54.15/-58.74 | +2.02% | 20% |
| [IONEXCHANG](https://in.tradingview.com/chart/?symbol=NSE:IONEXCHANG)<br><sub>↓CMF18d</sub> | ✓ SAFE | Water treatment systems, industrial effluent, municipal sewage | 📈 BULL_ANY_MID | 94 | 🔄52 | ↑1.023 | ↑1d | SQ | +3.9% | -35.38/-40.16 | +3.94% | 20% |
| [SRF](https://in.tradingview.com/chart/?symbol=NSE:SRF)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Technical textiles, films, chemicals for automotive, industrial, packaging | 📈 BULL_ANY_MID | 69 | ↑30 | ↑1.003 | ↑1d | SQ | +0.2% | -27.7/-27.87 | +0.25% | 20% |
| [ACCELYA](https://in.tradingview.com/chart/?symbol=NSE:ACCELYA)<br><sub>↓CMF23d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 60 | ↑30 | ↑1.001 | ↓10d | SQ | +0.0% | -35.92/-36.72 | +0.25% | 20% |
| [BFINVEST](https://in.tradingview.com/chart/?symbol=NSE:BFINVEST)<br><sub>↓CMF13d</sub> | ✓ SAFE | Kalyani Group holding company invests subsidiaries manufacturing | 📈 BULL_ANY_MID | 59 | 🔄52 | ↑1.009 | ↑1d | — | +1.9% | -41.34/-43.61 | +1.92% | 20% |
| [ROTO](https://in.tradingview.com/chart/?symbol=NSE:ROTO)<br><sub>↓CMF18d · ⚠️TRAP</sub> | ✓ SAFE | Progressive cavity pumps for wastewater and sugar industries | 📈 BULL_ANY_MID | 58 | ↑43 | ↓0.996 | ↓2d | SQ | +3.1% | -49.88/-51.04 | -1.77% | 20% |
| [GUJENERGY](https://in.tradingview.com/chart/?symbol=NSE:GUJENERGY)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Piped natural gas distribution to households and industries | 📈 BULL_ANY_MID | 54 | 🔄1 | ↑1.016 | ↑1d | — | +3.1% | -43.17/-46.88 | +3.14% | 5% |
| [ASTERDM](https://in.tradingview.com/chart/?symbol=NSE:ASTERDM)<br><sub>↓CMF16d</sub> | ✓ SAFE | Multi-specialty hospitals and clinics, India healthcare | 📈 BULL_ANY_MID | 35 | 🔄57 | ↑0.992 | ↓27d | — | -5.2% | -34.64/-34.64 | +0.28% | 20% |
| [DHANUKA](https://in.tradingview.com/chart/?symbol=NSE:DHANUKA)<br><sub>↑CMF1d</sub> | ⚠ CAUTION | Herbicides insecticides fungicides manufacturing for Indian farmers | 📈 BULL_ANY_MID | 29 | ↑13 | ↑1.006 | ↑1d | — | +0.5% | -46.12/-50.1 | +0.54% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MAITHANALL,NSE:DRAGARWQ,NSE:ELANTAS,NSE:INFY,NSE:JAYKAY,NSE:HCLTECH,NSE:CENTENKA,NSE:XPROINDIA,NSE:HYUNDAI,NSE:WINDLAS,NSE:ANTHEM,NSE:CLEAN,NSE:SIGMAADV,NSE:TATACAP,NSE:EIHAHOTELS,NSE:SUNDARMFIN,NSE:THEJO,NSE:PREMEXPLN,NSE:FEDERALBNK,NSE:MRPL,NSE:PANAMAPET,NSE:YATRA,NSE:BEPL,NSE:ARTEMISMED,NSE:NAHARSPING,NSE:INDOSTAR,NSE:AEROPLANE,NSE:MONTECARLO,NSE:63MOONS,NSE:CHENNPETRO,NSE:TARSONS,NSE:DIVGIITTS,NSE:CLSEL,NSE:GUJALKALI,NSE:TINNARUBR,NSE:SEAMECLTD,NSE:TORNTPOWER,NSE:NINSYS,NSE:EMSLIMITED,NSE:DLINKINDIA,NSE:NUVOCO,NSE:ZOTA,NSE:TCC,NSE:PARKHOTELS,NSE:ONGC,NSE:IONEXCHANG,NSE:SRF,NSE:ACCELYA,NSE:BFINVEST,NSE:ROTO,NSE:GUJENERGY,NSE:ASTERDM,NSE:DHANUKA
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (22)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MAITHANALL](https://in.tradingview.com/chart/?symbol=NSE:MAITHANALL)<br><sub>📶W9 · W↑3d · RVOL13x · ↑CMF1d</sub> | ✓ SAFE | Ferro alloys manufacturer for steel industry globally | ⚡ BULL_ANY_PPV | 94 | 🔄46 | ↑1.030 | ↑1d | SQ·PV | +4.8% | 17.61/14.35 | +4.79% | 20% |
| [DRAGARWQ](https://in.tradingview.com/chart/?symbol=NSE:DRAGARWQ)<br><sub>📶W9 · ↑CMF15d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 63 | ↑50 | ↑1.024 | ↑2d | SQ·PV | +3.6% | 22.93/15.03 | +2.24% | 20% |
| [ELANTAS](https://in.tradingview.com/chart/?symbol=NSE:ELANTAS)<br><sub>📶W9 · ↓CMF0d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 62 | ↑50 | ↑1.018 | ↑3d | SQ·PV | +3.1% | 22.46/20.9 | +2.35% | 20% |
| [JAYKAY](https://in.tradingview.com/chart/?symbol=NSE:JAYKAY)<br><sub>📶W9 · ↑CMF5d</sub> | ✓ SAFE | 3D printing and additive manufacturing solutions for industrial prototyping | ⚡ BULL_ANY_PPV | 58 | ↑50 | ↑1.060 | ↑2d | SQ·PV | +12.7% | 0.97/-6.26 | +5.49% | 20% |
| [TATACAP](https://in.tradingview.com/chart/?symbol=NSE:TATACAP)<br><sub>📶W9 · W↑57d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.013 | ↑1d | SQ | +1.9% | 11.85/8.42 | +1.86% | 20% |
| [EIHAHOTELS](https://in.tradingview.com/chart/?symbol=NSE:EIHAHOTELS)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄28 | ↑1.025 | ↑1d | SQ | +5.0% | -13.73/-17.73 | +4.96% | 20% |
| [SUNDARMFIN](https://in.tradingview.com/chart/?symbol=NSE:SUNDARMFIN)<br><sub>📶W9 · W↑53d · ↑CMF1d</sub> | ⚠ CAUTION | Vehicle and equipment finance NBFC retail lending | 📈 BULL_ANY_MID | 69 | ↑41 | ↑1.001 | ↑1d | SQ | +0.4% | 6.37/5.46 | +0.38% | 20% |
| [THEJO](https://in.tradingview.com/chart/?symbol=NSE:THEJO)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | Bulk material handling, mineral processing, corrosion protection equipment | 📈 BULL_ANY_MID | 69 | ↑77 | ↑1.010 | ↑1d | SQ | +1.1% | 6.28/3.73 | +1.12% | 20% |
| [PREMEXPLN](https://in.tradingview.com/chart/?symbol=NSE:PREMEXPLN)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Explosives propellants detonators defense space mining manufacturing | 📈 BULL_ANY_MID | 68 | ↑64 | ↑1.006 | ↑2d | SQ | +0.9% | 19.59/10.3 | +0.73% | 20% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Retail corporate banking Kerala-headquartered private sector bank | 📈 BULL_ANY_MID | 67 | ↑82 | ↑1.005 | ↓3d | SQ | +2.6% | -12.99/-14.33 | +1.17% | 20% |
| [MRPL](https://in.tradingview.com/chart/?symbol=NSE:MRPL)<br><sub>📶W9 · W↑38d · ↓CMF11d</sub> | ✓ SAFE | Crude oil refining, petrochemicals, fuel production for domestic markets | 📈 BULL_ANY_MID | 64 | ↑63 | ↑1.016 | ↑1d | SQ | +2.2% | 1.07/-0.4 | +2.22% | 20% |
| [PANAMAPET](https://in.tradingview.com/chart/?symbol=NSE:PANAMAPET)<br><sub>📶W9 · ↓CMF15d</sub> | ✓ SAFE | Specialty petroleum products for pharma, cosmetics, rubber | 📈 BULL_ANY_MID | 63 | ↑92 | ↑1.017 | ↑2d | SQ | +3.9% | -6.49/-11.78 | +0.55% | 10% 🟨 |
| [YATRA](https://in.tradingview.com/chart/?symbol=NSE:YATRA)<br><sub>📶W9 · W↑18d · ↑CMF16d</sub> | ✓ SAFE | Online travel bookings for leisure and corporate travelers | 📈 BULL_ANY_MID | 58 | ↑28 | ↓1.018 | ↑2d | SQ | +7.3% | -2.17/-3.96 | +0.23% | 20% |
| [BEPL](https://in.tradingview.com/chart/?symbol=NSE:BEPL)<br><sub>📶W9 · ↑CMF7d</sub> | ✓ SAFE | ABS SAN resin manufacturer for automotive consumer goods | 📈 BULL_ANY_MID | 58 | ↑83 | ↓1.020 | ↑2d | SQ | +5.1% | 34.71/33.42 | +0.10% | 20% |
| [ARTEMISMED](https://in.tradingview.com/chart/?symbol=NSE:ARTEMISMED)<br><sub>📶W9 · W↑43d · ↓CMF5d</sub> | ✓ SAFE | Tertiary care hospital operator, multi-specialty healthcare delivery Gurgaon | 📈 BULL_ANY_MID | 58 | ↑78 | ↓1.000 | ↑2d | SQ | +1.0% | 42.4/42.15 | -2.21% | 20% |
| [NAHARSPING](https://in.tradingview.com/chart/?symbol=NSE:NAHARSPING)<br><sub>📶W9 · ↓CMF2d</sub> | ✓ SAFE | Cotton yarn and hosiery knitwear manufacturer exporting globally | 📈 BULL_ANY_MID | 58 | ↑79 | ↓0.999 | ↓2d | SQ | +1.9% | -12.93/-16.31 | -1.54% | 5% |
| [NINSYS](https://in.tradingview.com/chart/?symbol=NSE:NINSYS)<br><sub>↑CMF2d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 75 | 🔄90 | ↑0.991 | ↓53d | SQ·PV | +2.3% | -35.17/-37.49 | +0.08% | 5% |
| [IONEXCHANG](https://in.tradingview.com/chart/?symbol=NSE:IONEXCHANG)<br><sub>↓CMF18d</sub> | ✓ SAFE | Water treatment systems, industrial effluent, municipal sewage | 📈 BULL_ANY_MID | 94 | 🔄52 | ↑1.023 | ↑1d | SQ | +3.9% | -35.38/-40.16 | +3.94% | 20% |
| [SRF](https://in.tradingview.com/chart/?symbol=NSE:SRF)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Technical textiles, films, chemicals for automotive, industrial, packaging | 📈 BULL_ANY_MID | 69 | ↑30 | ↑1.003 | ↑1d | SQ | +0.2% | -27.7/-27.87 | +0.25% | 20% |
| [ACCELYA](https://in.tradingview.com/chart/?symbol=NSE:ACCELYA)<br><sub>↓CMF23d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 60 | ↑30 | ↑1.001 | ↓10d | SQ | +0.0% | -35.92/-36.72 | +0.25% | 20% |
| [VTL](https://in.tradingview.com/chart/?symbol=NSE:VTL)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Yarn fabric acrylic fiber garments textiles manufacturer | 📈 BULL_ANY_MID | 58 | ↓62 | ↓0.990 | ↓2d | SQ | +2.7% | -32.66/-32.98 | -2.47% | 20% |
| [ROTO](https://in.tradingview.com/chart/?symbol=NSE:ROTO)<br><sub>↓CMF18d · ⚠️TRAP</sub> | ✓ SAFE | Progressive cavity pumps for wastewater and sugar industries | 📈 BULL_ANY_MID | 58 | ↑43 | ↓0.996 | ↓2d | SQ | +3.1% | -49.88/-51.04 | -1.77% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MAITHANALL,NSE:DRAGARWQ,NSE:ELANTAS,NSE:JAYKAY,NSE:TATACAP,NSE:EIHAHOTELS,NSE:SUNDARMFIN,NSE:THEJO,NSE:PREMEXPLN,NSE:FEDERALBNK,NSE:MRPL,NSE:PANAMAPET,NSE:YATRA,NSE:BEPL,NSE:ARTEMISMED,NSE:NAHARSPING,NSE:NINSYS,NSE:IONEXCHANG,NSE:SRF,NSE:ACCELYA,NSE:VTL,NSE:ROTO
```

---

### 🔥 MAJOR — PPV confirmed (13)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [INFY](https://in.tradingview.com/chart/?symbol=NSE:INFY)<br><sub>📶W9 · W↑37d · ↑CMF3d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 59 | 🔄17 | ↑1.010 | ↑1d | PV | +1.2% | -6.55/-11.02 | +1.22% | 20% |
| [HCLTECH](https://in.tradingview.com/chart/?symbol=NSE:HCLTECH)<br><sub>📶W9 · W↑42d · 🚀SS · ↓CMF4d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 54 | 🔄42 | ↑1.024 | ↑1d | PV | +3.0% | -1.66/-9.73 | +3.04% | 20% |
| [CENTENKA](https://in.tradingview.com/chart/?symbol=NSE:CENTENKA)<br><sub>📶W9 · 🚀SS·199x · ↑CMF0d</sub> | ✓ SAFE | Synthetic yarn manufacturer for textiles and automotive | ⚡ BULL_ANY_PPV | 49 | 🔄77 | ↑1.067 | ↑1d | PV | +10.7% | -23.01/-32.58 | +10.71% | 20% |
| [XPROINDIA](https://in.tradingview.com/chart/?symbol=NSE:XPROINDIA)<br><sub>📶W9 · RVOL16x · ↑CMF0d</sub> | ✓ SAFE | Polymer films and sheets for packaging and industrial applications | ⚡ BULL_ANY_PPV | 49 | 🔄70 | ↑1.098 | ↑1d | PV | +13.2% | 0.91/-11.34 | +13.19% | 20% |
| [HYUNDAI](https://in.tradingview.com/chart/?symbol=NSE:HYUNDAI)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 5 | ↑47 | ↑1.017 | ↑23d | PV | +15.3% | 45.93/42.54 | +0.87% | 20% |
| [WINDLAS](https://in.tradingview.com/chart/?symbol=NSE:WINDLAS)<br><sub>📶W9 · W↑68d · ↑CMF16d</sub> | ✓ SAFE | Oral solid liquid pharma formulations CDMO manufacturing | ⚡ BULL_ANY_PPV | 3 | ↑81 | ↑1.093 | ↑17d | PV | +30.6% | 69.67/65.63 | +8.75% | 20% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>📶W9 · W↑28d · ↑CMF1d</sub> | ✓ SAFE | Contract research development manufacturing biotech pharma | ⚡ BULL_ANY_PPV | 0 | ↑77 | ↑1.033 | ↑28d | PV | +21.4% | 61.12/58.59 | +1.08% | 20% |
| [CLEAN](https://in.tradingview.com/chart/?symbol=NSE:CLEAN)<br><sub>📶W9 · W↑18d · ↑CMF14d</sub> | ✓ SAFE | Specialty chemicals manufacturing, catalytic processes, pharma and industrial | ⚡ BULL_ANY_PPV | 0 | ↑42 | ↑1.037 | ↑23d | PV | +17.6% | 40.06/35.89 | +4.36% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [TORNTPOWER](https://in.tradingview.com/chart/?symbol=NSE:TORNTPOWER)<br><sub>↓CMF21d · 🎯SLING</sub> | ⚠ CAUTION | Power generation transmission distribution utility Gujarat Maharashtra | 🔥 BULL_OS_PPV | 40 | 🔄21 | ↑1.004 | ↓33d | PV | -10.2% | -56.48/-60.64 | +2.43% | 20% |
| [EMSLIMITED](https://in.tradingview.com/chart/?symbol=NSE:EMSLIMITED)<br><sub>🚀SS·20x · ↓CMF12d</sub> | ✓ SAFE | Water treatment EPC contractor for municipal urban infrastructure | ⚡ BULL_ANY_PPV | 59 | 🔄54 | ↑1.014 | ↑1d | PV | +3.9% | -27.05/-32.56 | +3.87% | 10% 🟨 |
| [DLINKINDIA](https://in.tradingview.com/chart/?symbol=NSE:DLINKINDIA)<br><sub>↑CMF10d</sub> | ✓ SAFE | Networking equipment distribution, consumer and enterprise markets | ⚡ BULL_ANY_PPV | 54 | 🔄35 | ↑1.016 | ↑1d | PV | +2.7% | -0.79/-3.65 | +2.69% | 20% |
| [NUVOCO](https://in.tradingview.com/chart/?symbol=NSE:NUVOCO)<br><sub>↑CMF0d</sub> | ⚠ CAUTION | Cement and ready-mix concrete manufacturer East North India | ⚡ BULL_ANY_PPV | 29 | ↑32 | ↑1.010 | ↑1d | PV | +1.6% | -39.17/-42.65 | +1.64% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:INFY,NSE:HCLTECH,NSE:CENTENKA,NSE:XPROINDIA,NSE:HYUNDAI,NSE:WINDLAS,NSE:ANTHEM,NSE:CLEAN,NSE:SIGMAADV,NSE:TORNTPOWER,NSE:EMSLIMITED,NSE:DLINKINDIA,NSE:NUVOCO
```

### 🟢 OVERSOLD — reversal from −53/−60 (9)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ZOTA](https://in.tradingview.com/chart/?symbol=NSE:ZOTA)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Pharma manufacturer: tablets, syrups, Ayurveda, OTC products | 🟢 BULL_OVERSOLD | 35 | 🔄12 | ↑0.996 | ↓60d+ | — | -9.9% | -59.69/-60.39 | +4.85% | 20% |
| [TCC](https://in.tradingview.com/chart/?symbol=NSE:TCC)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Real estate aggregation, digital infrastructure, consumer ecosystem platform | 🟢 BULL_OVERSOLD | 35 | 🔄50 | ↑0.987 | ↓22d | — | -19.0% | -62.14/-64.53 | +0.80% | 20% |
| [PARKHOTELS](https://in.tradingview.com/chart/?symbol=NSE:PARKHOTELS)<br><sub>↓CMF23d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 35 | 🔄23 | ↑0.999 | ↓23d | — | -6.8% | -59.64/-61.18 | +1.90% | 20% |
| [ASTRAZEN](https://in.tradingview.com/chart/?symbol=NSE:ASTRAZEN)<br><sub>↓CMF23d · ⚠️TRAP</sub> | ✓ SAFE | Prescription drugs oncology cardiology respiratory diseases India | 🟢 BULL_OVERSOLD | 6 | ↓6 | ↑0.961 | ↓19d | — | -14.9% | -70.79/-70.8 | -0.71% | 20% |
| [CREDITACC](https://in.tradingview.com/chart/?symbol=NSE:CREDITACC)<br><sub>↓CMF7d · 🎯SLING</sub> | ✓ SAFE | Microfinance loans for rural women, NBFC sector | 🟢 BULL_OVERSOLD | 5 | ↓55 | ↑0.983 | ↓29d | — | -6.7% | -62.86/-62.91 | +0.72% | 20% |
| [EPACK](https://in.tradingview.com/chart/?symbol=NSE:EPACK)<br><sub>↓CMF19d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | AC manufacturing ODM, consumer durables, Indian domestic market | 🟢 BULL_OVERSOLD | 5 | ↓3 | ↑0.958 | ↓39d | — | -18.5% | -72.15/-72.26 | -0.10% | 20% |
| [ERIS](https://in.tradingview.com/chart/?symbol=NSE:ERIS)<br><sub>↓CMF5d · ⚠️TRAP · ÷DIV</sub> | ⚠ CAUTION | Oral branded drugs for chronic diseases, domestic India | 🟢 BULL_OVERSOLD | 0 | ↓17 | ↓0.982 | ↓38d | — | -9.9% | -59.92/-60.14 | -0.85% | 20% |
| [ONGC](https://in.tradingview.com/chart/?symbol=NSE:ONGC)<br><sub>🚀SS · ↓CMF23d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 59 | 🔄28 | ↑1.007 | ↑1d | — | +2.0% | -54.15/-58.74 | +2.02% | 20% |
| [KRISHNADEF](https://in.tradingview.com/chart/?symbol=NSE:KRISHNADEF)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Defense equipment and dairy machinery manufacturer, engineering sector | 🟡 BULL_OS_L2 | 5 | ↓48 | ↑0.978 | ↓33d | — | -21.4% | -57.46/-58.35 | +0.57% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ZOTA,NSE:TCC,NSE:PARKHOTELS,NSE:ASTRAZEN,NSE:CREDITACC,NSE:EPACK,NSE:ERIS,NSE:ONGC,NSE:KRISHNADEF
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (16)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [INDOSTAR](https://in.tradingview.com/chart/?symbol=NSE:INDOSTAR)<br><sub>📶W9 · W↑3d · ↓CMF2d</sub> | ✓ SAFE | Commercial vehicle finance NBFC underserved retail markets | 📈 BULL_ANY_MID | 54 | 🔄53 | ↑1.024 | ↑1d | — | +3.6% | 22.26/20.54 | +3.57% | 20% |
| [AEROPLANE](https://in.tradingview.com/chart/?symbol=NSE:AEROPLANE)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Basmati rice processor exporter FMCG packaged food | 📈 BULL_ANY_MID | 45 | 🔄50 | ↑1.006 | ↓15d | — | -2.7% | -32.39/-35.3 | +2.33% | 20% |
| [MONTECARLO](https://in.tradingview.com/chart/?symbol=NSE:MONTECARLO)<br><sub>📶W9 · W↑8d · ↓CMF30d</sub> | ✓ SAFE | Woolen cotton apparel manufacturer winter wear retail | 📈 BULL_ANY_MID | 28 | ↑30 | ↑1.012 | ↑2d | — | +2.6% | 8.0/6.71 | +0.96% | 20% |
| [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS)<br><sub>📶W9 · 🚀SS · ↓CMF3d · DEL55%(T-1)</sub> | ✓ SAFE | Financial software IP, banking and capital markets infrastructure | 📈 BULL_ANY_MID | 24 | ↑63 | ↑1.025 | ↑1d | — | +3.8% | -9.79/-14.7 | +3.81% | 20% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>📶W9 · W↑38d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Refines crude oil, produces petroleum products, lubricants | 📈 BULL_ANY_MID | 22 | ↑88 | ↑1.025 | ↑3d | — | +5.4% | 30.49/28.69 | +1.95% | 20% |
| [TARSONS](https://in.tradingview.com/chart/?symbol=NSE:TARSONS)<br><sub>📶W9 · ↑CMF15d</sub> | ✓ SAFE | Plastic labware manufacturer for research and diagnostic labs | 📈 BULL_ANY_MID | 18 | ↑91 | ↓1.019 | ↑2d | — | +4.1% | 26.26/25.61 | +0.36% | 20% |
| [DIVGIITTS](https://in.tradingview.com/chart/?symbol=NSE:DIVGIITTS)<br><sub>📶W9 · W↑23d · ↑CMF17d</sub> | ✓ SAFE | Automotive drivetrain components, transfer cases, all-terrain vehicles | 📈 BULL_ANY_MID | 17 | ↑95 | ↓1.025 | ↑3d | — | +5.9% | 39.78/37.25 | -1.92% | 20% |
| [CLSEL](https://in.tradingview.com/chart/?symbol=NSE:CLSEL)<br><sub>📶W9 · W↑13d · ↑CMF7d</sub> | ✓ SAFE | Basmati rice milling, packing, exporting for global food markets | 📈 BULL_ANY_MID | 11 | ↑60 | ↓1.010 | ↑9d | — | +8.2% | 33.97/33.43 | -0.33% | 20% |
| [GUJALKALI](https://in.tradingview.com/chart/?symbol=NSE:GUJALKALI)<br><sub>📶W9 · W↑28d · ↑CMF5d</sub> | ✓ SAFE | Caustic soda chlorine chemicals manufacturing industrial applications | 📈 BULL_ANY_MID | 10 | ↑78 | ↓1.013 | ↑10d | — | +7.6% | 43.9/42.8 | +0.21% | 20% |
| [TINNARUBR](https://in.tradingview.com/chart/?symbol=NSE:TINNARUBR)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Waste tyre recycling into crumb rubber and steel | 📈 BULL_ANY_MID | 10 | ↑78 | ↑0.998 | ↓15d | — | -5.9% | -39.78/-41.23 | -0.01% | 20% |
| [SEAMECLTD](https://in.tradingview.com/chart/?symbol=NSE:SEAMECLTD)<br><sub>📶W9 · W↑18d · ★ · ↑CMF13d</sub> | ✓ SAFE | Offshore diving vessels, subsea engineering, oil and gas | 📈 BULL_ANY_MID | 0 | ↑86 | ↑1.044 | ↑28d | — | +24.3% | 59.33/57.2 | +3.39% | 20% |
| [BFINVEST](https://in.tradingview.com/chart/?symbol=NSE:BFINVEST)<br><sub>↓CMF13d</sub> | ✓ SAFE | Kalyani Group holding company invests subsidiaries manufacturing | 📈 BULL_ANY_MID | 59 | 🔄52 | ↑1.009 | ↑1d | — | +1.9% | -41.34/-43.61 | +1.92% | 20% |
| [GUJENERGY](https://in.tradingview.com/chart/?symbol=NSE:GUJENERGY)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Piped natural gas distribution to households and industries | 📈 BULL_ANY_MID | 54 | 🔄1 | ↑1.016 | ↑1d | — | +3.1% | -43.17/-46.88 | +3.14% | 5% |
| [ASTERDM](https://in.tradingview.com/chart/?symbol=NSE:ASTERDM)<br><sub>↓CMF16d</sub> | ✓ SAFE | Multi-specialty hospitals and clinics, India healthcare | 📈 BULL_ANY_MID | 35 | 🔄57 | ↑0.992 | ↓27d | — | -5.2% | -34.64/-34.64 | +0.28% | 20% |
| [DHANUKA](https://in.tradingview.com/chart/?symbol=NSE:DHANUKA)<br><sub>↑CMF1d</sub> | ⚠ CAUTION | Herbicides insecticides fungicides manufacturing for Indian farmers | 📈 BULL_ANY_MID | 29 | ↑13 | ↑1.006 | ↑1d | — | +0.5% | -46.12/-50.1 | +0.54% | 20% |
| [HLEGLAS](https://in.tradingview.com/chart/?symbol=NSE:HLEGLAS)<br><sub>↓CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Glass-lined equipment for pharma chemical processing | 📈 BULL_ANY_MID | 0 | ↓6 | ↓0.982 | ↓29d | — | -23.8% | -23.53/-23.77 | -0.84% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:INDOSTAR,NSE:AEROPLANE,NSE:MONTECARLO,NSE:63MOONS,NSE:CHENNPETRO,NSE:TARSONS,NSE:DIVGIITTS,NSE:CLSEL,NSE:GUJALKALI,NSE:TINNARUBR,NSE:SEAMECLTD,NSE:BFINVEST,NSE:GUJENERGY,NSE:ASTERDM,NSE:DHANUKA,NSE:HLEGLAS
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
