> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-10-26
*Generated 2026-10-26 15:44 IST*

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

**Total bull crosses today: 67** · 19 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ATHERENERG,NSE:RBA,NSE:ACUTAAS,NSE:ITCHOTELS,NSE:WESTLIFE,NSE:SGMART,NSE:YASHO,NSE:CARBORUNIV,NSE:GNA,NSE:SIGMAADV,NSE:INDIASHLTR,NSE:DRAGARWQ,NSE:SESHAPAPER,NSE:CARRARO,NSE:RUBICON,NSE:EMCURE,NSE:ANURAS,NSE:GRINFRA,NSE:LUPIN,NSE:ANTHEM,NSE:JUBLFOOD,NSE:DEVYANI,NSE:GRANULES,NSE:TTKPRESTIG,NSE:NUVOCO,NSE:MARATHON,NSE:GRWRHITECH,NSE:ACI,NSE:GUFICBIO,NSE:LMW,NSE:MENONBE,NSE:SETL,NSE:SAKAR,NSE:KAYNES,NSE:AJANTPHARM,NSE:JAGSNPHARM,NSE:SURAKSHA,NSE:ICRA,NSE:PRIVISCL,NSE:STAR,NSE:ZYDUSLIFE,NSE:JUBLPHARMA,NSE:SUNCLAY,NSE:RAMKY,NSE:KEC,NSE:TIIL,NSE:TCIEXP,NSE:STYL,NSE:ONESOURCE,NSE:GKENERGY,NSE:SAGCEM,NSE:BANSALWIRE,NSE:KRN,NSE:SENORES,NSE:DEEDEV,NSE:FORTIS,NSE:NEULANDLAB,NSE:TENNIND,NSE:PARKHOSPS,NSE:VIMTALABS,NSE:UNIPARTS,NSE:MMFL,NSE:LINCOLN,NSE:HONAUT,NSE:CANHLIFE,NSE:MAXHEALTH,NSE:CAPLIPOINT
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (42)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>📶W9 · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Premium electric scooters, charging network, urban mobility | ⚡ BULL_ANY_PPV | 89 | 🔄97 | ↑1.075 | ↑1d | SQ·PV | +14.1% | -14.33/-16.67 | +14.13% | -% |
| [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Burger King franchisee operating QSR restaurants India Indonesia | ⚡ BULL_ANY_PPV | 64 | ↑91 | ↑1.019 | ↑1d | SQ·PV | +4.1% | -49.29/-51.51 | +4.14% | 20% 🟦 |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Pharmaceutical intermediates and specialty chemicals manufacturer globally | ⚡ BULL_ANY_PPV | 59 | ↑92 | ↑1.042 | ↑1d | SQ·PV | +6.7% | -1.34/-7.34 | +6.73% | 20% |
| [ITCHOTELS](https://in.tradingview.com/chart/?symbol=NSE:ITCHOTELS)<br><sub>📶W9 · W↑1d · RVOL13x · ↑CMF0d</sub> | ⚠ CAUTION | Hotel chain, premium and mid-market segments, Indian travelers | ⚡ BULL_ANY_PPV | 59 | ↑54 | ↑1.032 | ↑1d | SQ·PV | +5.2% | 6.18/-1.77 | +5.16% | 20% |
| [WESTLIFE](https://in.tradingview.com/chart/?symbol=NSE:WESTLIFE)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | McDonald's franchise operator West South India QSR | ⚡ BULL_ANY_PPV | 59 | ↑80 | ↑1.038 | ↑1d | SQ·PV | +3.5% | -14.74/-20.35 | +3.47% | 20% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>📶W9 · W↑6d · ★ · ↑CMF0d</sub> | ✓ SAFE | Building materials B2B marketplace connecting manufacturers suppliers traders | ⚡ BULL_ANY_PPV | 58 | ↑95 | ↓1.031 | ↑2d | SQ·PV | +5.7% | 35.48/32.57 | +0.36% | 20% |
| [YASHO](https://in.tradingview.com/chart/?symbol=NSE:YASHO)<br><sub>📶W9 · 🚀SS · ↓CMF13d</sub> | ✓ SAFE | Specialty chemicals manufacturer: antioxidants, aroma, rubber additives | ⚡ BULL_ANY_PPV | 49 | 🔄98 | ↑1.033 | ↑1d | PV | +13.2% | -46.54/-48.8 | +13.18% | 20% 🟦 |
| [CARBORUNIV](https://in.tradingview.com/chart/?symbol=NSE:CARBORUNIV)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Abrasives, ceramics, refractories for industrial manufacturing | ⚡ BULL_ANY_PPV | 35 | 🔄81 | ↑1.021 | ↓27d | PV | +4.2% | -39.65/-40.46 | +9.76% | 20% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Rear axles and drive shafts for commercial vehicles | ⚡ BULL_ANY_PPV | 19 | ↑91 | ↑1.038 | ↑1d | PV | +8.1% | -26.67/-30.88 | +8.06% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [INDIASHLTR](https://in.tradingview.com/chart/?symbol=NSE:INDIASHLTR)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF0d · 🎯SLING</sub> | ⚠ CAUTION | Housing loans for low income tier 2 3 cities | 🟢 BULL_OVERSOLD | 69 | ↑25 | ↑1.005 | ↑1d | SQ | +1.5% | -49.93/-60.81 | +1.51% | 20% |
| [DRAGARWQ](https://in.tradingview.com/chart/?symbol=NSE:DRAGARWQ)<br><sub>📶W9 · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 69 | ↑50 | ↑1.012 | ↑1d | SQ | +2.1% | -55.85/-61.07 | +2.11% | 20% |
| [SESHAPAPER](https://in.tradingview.com/chart/?symbol=NSE:SESHAPAPER)<br><sub>📶W9 · 🚀SS · ↓CMF15d · 🎯SLING</sub> | ✓ SAFE | Integrated paper and paperboards manufacturer Tamil Nadu facilities | 🟢 BULL_OVERSOLD | 40 | 🔄42 | ↑1.011 | ↓38d | — | -6.7% | -61.71/-64.15 | +7.97% | 20% |
| [CARRARO](https://in.tradingview.com/chart/?symbol=NSE:CARRARO)<br><sub>📶W9 · ↓CMF5d · 🎯SLING</sub> | ✓ SAFE | Axles transmissions agricultural tractors construction equipment | 🟢 BULL_OVERSOLD | 11 | ↑53 | ↑0.999 | ↓14d | — | -7.0% | -60.71/-60.85 | +3.87% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · ↑CMF1d · 🎯SLING</sub> | ✓ SAFE | Complex generics and specialty formulations for global pharma | 🟢 BULL_OVERSOLD | 10 | ↑95 | ↑1.003 | ↓32d | — | -16.7% | -57.94/-60.39 | +4.63% | 20% |
| [EMCURE](https://in.tradingview.com/chart/?symbol=NSE:EMCURE)<br><sub>📶W9 · ↑CMF1d · ⚠️TRAP</sub> | ✓ SAFE | Pharmaceuticals manufacturing antibiotics contraceptives dermatology global markets | 🟢 BULL_OVERSOLD | 5 | ↑73 | ↑0.988 | ↓20d | — | -7.7% | -61.68/-63.75 | +0.55% | 20% |
| [ANURAS](https://in.tradingview.com/chart/?symbol=NSE:ANURAS)<br><sub>📶W9 · ↑CMF2d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Specialty chemical manufacturing for pharmaceuticals agrochemicals | 🟡 BULL_OS_L2 | 58 | ↑52 | ↑0.998 | ↓7d | SQ | -3.1% | -56.68/-56.83 | +2.08% | 20% |
| [GRINFRA](https://in.tradingview.com/chart/?symbol=NSE:GRINFRA)<br><sub>📶W9 · ↑CMF1d · ⚠️TRAP</sub> | ⚠ CAUTION | Road EPC contractor, highways and railways infrastructure | 🟡 BULL_OS_L2 | 58 | ↑28 | ↓0.998 | ↓2d | SQ | +2.5% | -55.67/-57.69 | -1.10% | 20% |
| [LUPIN](https://in.tradingview.com/chart/?symbol=NSE:LUPIN)<br><sub>📶W9 · ↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION | Branded generics, APIs, biotechnology for global pharma markets | 🟡 BULL_OS_L2 | 29 | ↑40 | ↑1.003 | ↑1d | — | +1.6% | -56.23/-58.15 | +1.61% | 20% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>📶W9 · ↑CMF1d · 🎯SLING</sub> | ✓ SAFE | Contract research development manufacturing biotech pharma | 🟡 BULL_OS_L2 | 14 | ↑77 | ↑0.997 | ↓11d | — | -4.6% | -54.78/-56.83 | +1.16% | 20% |
| [JUBLFOOD](https://in.tradingview.com/chart/?symbol=NSE:JUBLFOOD)<br><sub>📶W9 · ↓CMF19d · 🎯SLING</sub> | ✓ SAFE | Domino's Pizza franchise operator serving Indian quick-service restaurant market | 🟡 BULL_OS_L2 | 10 | ↑41 | ↑1.014 | ↓22d | — | -11.7% | -55.73/-59.1 | +4.68% | 20% |
| [DEVYANI](https://in.tradingview.com/chart/?symbol=NSE:DEVYANI)<br><sub>📶W9 · ↓CMF6d · 🎯SLING · DEL63%</sub> | ⚠ CAUTION | Yum Brands franchisee, QSR operator, KFC Dominos Pizza Hut | 🟡 BULL_OS_L2 | 5 | ↑57 | ↑0.999 | ↓27d | — | -13.3% | -55.03/-57.06 | +2.33% | 20% |
| [GRANULES](https://in.tradingview.com/chart/?symbol=NSE:GRANULES)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | APIs, formulation intermediates, finished pharma drugs manufacturer | 📈 BULL_ANY_MID | 69 | ↑83 | ↑1.009 | ↑1d | SQ | +3.2% | -43.88/-46.06 | +3.25% | 20% |
| [TTKPRESTIG](https://in.tradingview.com/chart/?symbol=NSE:TTKPRESTIG)<br><sub>📶W9 · ↑CMF1d · ⚠️TRAP</sub> | ⚠ CAUTION | Pressure cookers, cookware, kitchen appliances for households | 📈 BULL_ANY_MID | 68 | ↑35 | ↑1.015 | ↑2d | SQ | +3.6% | -25.17/-30.6 | +0.96% | 20% |
| [NUVOCO](https://in.tradingview.com/chart/?symbol=NSE:NUVOCO)<br><sub>📶W9 · W↑6d · ↓CMF5d</sub> | ✓ SAFE | Cement and ready-mix concrete manufacturer East North India | 📈 BULL_ANY_MID | 64 | ↑59 | ↑1.019 | ↑1d | SQ | +3.0% | 13.93/11.47 | +2.98% | 20% |
| [MARATHON](https://in.tradingview.com/chart/?symbol=NSE:MARATHON)<br><sub>📶W9 · ↓CMF23d · ⚠️TRAP</sub> | ✓ SAFE | Luxury residential commercial real estate developer MMR region | 📈 BULL_ANY_MID | 63 | ↑27 | ↑1.002 | ↓7d | SQ | +1.9% | -30.46/-32.25 | +0.07% | 20% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>📶W9 · ★ · ↑CMF23d</sub> | ✓ SAFE | Specialty polyester films for packaging and industrial applications | 📈 BULL_ANY_MID | 58 | ↑94 | ↓1.007 | ↑2d | SQ | +4.8% | 0.09/-3.0 | -0.81% | 20% 🟦 |
| [ACI](https://in.tradingview.com/chart/?symbol=NSE:ACI)<br><sub>📶W9 · W↑11d · ↓CMF6d · ⚠️TRAP</sub> | ✓ SAFE | Bromine, industrial salt, potash specialty chemicals exporter | 📈 BULL_ANY_MID | 58 | ↑22 | ↓0.995 | ↓2d | SQ | +1.7% | -10.35/-11.43 | -2.11% | 20% |
| [GUFICBIO](https://in.tradingview.com/chart/?symbol=NSE:GUFICBIO)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Pharmaceutical APIs and formulations manufacturer for generic drugs | 📈 BULL_ANY_MID | 55 | ↑84 | ↑1.010 | ↓15d | SQ | -2.9% | -52.04/-52.92 | +3.97% | 20% |
| [LMW](https://in.tradingview.com/chart/?symbol=NSE:LMW)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Textile spinning machinery and CNC machine tools manufacturer | 📈 BULL_ANY_MID | 50 | ↑70 | ↑1.003 | ↓38d | SQ | -13.9% | -47.17/-50.98 | +1.37% | 20% |
| [MENONBE](https://in.tradingview.com/chart/?symbol=NSE:MENONBE)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 50 | ↑97 | ↑0.995 | ↓15d | SQ | -5.2% | -51.05/-51.94 | +2.75% | 20% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>📶W9 · 🚀SS · ↓CMF11d</sub> | ✓ SAFE | Glass-lined reactors and process equipment for pharma chemicals | 📈 BULL_ANY_MID | 39 | 🔄98 | ↑0.995 | ↓16d | — | -15.8% | -44.4/-44.85 | +5.00% | 20% |
| [SAKAR](https://in.tradingview.com/chart/?symbol=NSE:SAKAR)<br><sub>📶W9 · ↓CMF16d</sub> | ✓ SAFE | Pharma manufacturing across therapeutic segments Ahmedabad | 📈 BULL_ANY_MID | 35 | 🔄97 | ↑1.018 | ↓40d | — | +12.4% | -47.54/-49.19 | +9.10% | 20% 🟦 |
| [KAYNES](https://in.tradingview.com/chart/?symbol=NSE:KAYNES)<br><sub>📶W9 · ↓CMF30d · ÷DIV</sub> | ✓ SAFE | Electronics manufacturing, IoT solutions, industrial and consumer products | 📈 BULL_ANY_MID | 29 | ↑27 | ↑1.012 | ↑1d | — | +3.7% | -45.46/-48.34 | +3.73% | 20% |
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM)<br><sub>📶W9 · ↓CMF18d</sub> | ⚠ CAUTION | Branded generic pharmaceuticals formulations across India Asia Africa | 📈 BULL_ANY_MID | 29 | ↑79 | ↑1.014 | ↑1d | — | +3.0% | -46.26/-51.92 | +2.96% | 20% |
| [JAGSNPHARM](https://in.tradingview.com/chart/?symbol=NSE:JAGSNPHARM)<br><sub>📶W9 · ↓CMF2d</sub> | ✓ SAFE | Women's health and pain management pharmaceutical manufacturer India | 📈 BULL_ANY_MID | 24 | ↑72 | ↑1.018 | ↑1d | — | +5.3% | -49.86/-52.48 | +5.34% | 20% |
| [SURAKSHA](https://in.tradingview.com/chart/?symbol=NSE:SURAKSHA)<br><sub>📶W9 · ↓CMF3d</sub> | ⚠ CAUTION | Pathology radiology diagnostic centers East India healthcare | 📈 BULL_ANY_MID | 24 | ↑79 | ↑1.026 | ↑1d | — | +4.4% | -45.4/-48.2 | +4.44% | 20% |
| [ICRA](https://in.tradingview.com/chart/?symbol=NSE:ICRA)<br><sub>📶W9 · W↑11d · ↑CMF0d · ⚠️TRAP</sub> | ✓ SAFE | Credit ratings, debt analysis, capital markets participants | 📈 BULL_ANY_MID | 18 | ↑30 | ↑1.003 | ↑12d | — | +4.5% | -0.49/-1.24 | +0.46% | 20% |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | Aroma chemicals fragrance ingredients terpenes global export manufacturer | 📈 BULL_ANY_MID | 10 | ↑69 | ↑1.005 | ↓26d | — | -2.6% | -47.14/-48.42 | +3.26% | 20% |
| [STAR](https://in.tradingview.com/chart/?symbol=NSE:STAR)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE | Niche finished dosage pharma formulations global markets | 📈 BULL_ANY_MID | 5 | ↑74 | ↑0.993 | ↓42d | — | +5.1% | -48.65/-49.02 | +1.80% | 20% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Pharmaceuticals: generics, branded drugs, consumer wellness products | 📈 BULL_ANY_MID | 0 | ↑78 | ↓0.996 | ↓25d | — | +1.6% | -25.59/-26.34 | -0.86% | 20% |
| [JUBLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:JUBLPHARMA)<br><sub>📶W9 · ↓CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Radiopharmaceuticals, allergy therapy, contract pharmaceutical manufacturing | 📈 BULL_ANY_MID | 0 | ↑56 | ↓0.995 | ↓40d | — | +6.2% | -35.11/-35.17 | -0.14% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ATHERENERG,NSE:RBA,NSE:ACUTAAS,NSE:ITCHOTELS,NSE:WESTLIFE,NSE:SGMART,NSE:YASHO,NSE:CARBORUNIV,NSE:GNA,NSE:SIGMAADV,NSE:INDIASHLTR,NSE:DRAGARWQ,NSE:SESHAPAPER,NSE:CARRARO,NSE:RUBICON,NSE:EMCURE,NSE:ANURAS,NSE:GRINFRA,NSE:LUPIN,NSE:ANTHEM,NSE:JUBLFOOD,NSE:DEVYANI,NSE:GRANULES,NSE:TTKPRESTIG,NSE:NUVOCO,NSE:MARATHON,NSE:GRWRHITECH,NSE:ACI,NSE:GUFICBIO,NSE:LMW,NSE:MENONBE,NSE:SETL,NSE:SAKAR,NSE:KAYNES,NSE:AJANTPHARM,NSE:JAGSNPHARM,NSE:SURAKSHA,NSE:ICRA,NSE:PRIVISCL,NSE:STAR,NSE:ZYDUSLIFE,NSE:JUBLPHARMA
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (60)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>📶W9 · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Premium electric scooters, charging network, urban mobility | ⚡ BULL_ANY_PPV | 89 | 🔄97 | ↑1.075 | ↑1d | SQ·PV | +14.1% | -14.33/-16.67 | +14.13% | -% |
| [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Burger King franchisee operating QSR restaurants India Indonesia | ⚡ BULL_ANY_PPV | 64 | ↑91 | ↑1.019 | ↑1d | SQ·PV | +4.1% | -49.29/-51.51 | +4.14% | 20% 🟦 |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Pharmaceutical intermediates and specialty chemicals manufacturer globally | ⚡ BULL_ANY_PPV | 59 | ↑92 | ↑1.042 | ↑1d | SQ·PV | +6.7% | -1.34/-7.34 | +6.73% | 20% |
| [ITCHOTELS](https://in.tradingview.com/chart/?symbol=NSE:ITCHOTELS)<br><sub>📶W9 · W↑1d · RVOL13x · ↑CMF0d</sub> | ⚠ CAUTION | Hotel chain, premium and mid-market segments, Indian travelers | ⚡ BULL_ANY_PPV | 59 | ↑54 | ↑1.032 | ↑1d | SQ·PV | +5.2% | 6.18/-1.77 | +5.16% | 20% |
| [WESTLIFE](https://in.tradingview.com/chart/?symbol=NSE:WESTLIFE)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | McDonald's franchise operator West South India QSR | ⚡ BULL_ANY_PPV | 59 | ↑80 | ↑1.038 | ↑1d | SQ·PV | +3.5% | -14.74/-20.35 | +3.47% | 20% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>📶W9 · W↑6d · ★ · ↑CMF0d</sub> | ✓ SAFE | Building materials B2B marketplace connecting manufacturers suppliers traders | ⚡ BULL_ANY_PPV | 58 | ↑95 | ↓1.031 | ↑2d | SQ·PV | +5.7% | 35.48/32.57 | +0.36% | 20% |
| [YASHO](https://in.tradingview.com/chart/?symbol=NSE:YASHO)<br><sub>📶W9 · 🚀SS · ↓CMF13d</sub> | ✓ SAFE | Specialty chemicals manufacturer: antioxidants, aroma, rubber additives | ⚡ BULL_ANY_PPV | 49 | 🔄98 | ↑1.033 | ↑1d | PV | +13.2% | -46.54/-48.8 | +13.18% | 20% 🟦 |
| [CARBORUNIV](https://in.tradingview.com/chart/?symbol=NSE:CARBORUNIV)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Abrasives, ceramics, refractories for industrial manufacturing | ⚡ BULL_ANY_PPV | 35 | 🔄81 | ↑1.021 | ↓27d | PV | +4.2% | -39.65/-40.46 | +9.76% | 20% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Rear axles and drive shafts for commercial vehicles | ⚡ BULL_ANY_PPV | 19 | ↑91 | ↑1.038 | ↑1d | PV | +8.1% | -26.67/-30.88 | +8.06% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [INDIASHLTR](https://in.tradingview.com/chart/?symbol=NSE:INDIASHLTR)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF0d · 🎯SLING</sub> | ⚠ CAUTION | Housing loans for low income tier 2 3 cities | 🟢 BULL_OVERSOLD | 69 | ↑25 | ↑1.005 | ↑1d | SQ | +1.5% | -49.93/-60.81 | +1.51% | 20% |
| [DRAGARWQ](https://in.tradingview.com/chart/?symbol=NSE:DRAGARWQ)<br><sub>📶W9 · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 69 | ↑50 | ↑1.012 | ↑1d | SQ | +2.1% | -55.85/-61.07 | +2.11% | 20% |
| [SESHAPAPER](https://in.tradingview.com/chart/?symbol=NSE:SESHAPAPER)<br><sub>📶W9 · 🚀SS · ↓CMF15d · 🎯SLING</sub> | ✓ SAFE | Integrated paper and paperboards manufacturer Tamil Nadu facilities | 🟢 BULL_OVERSOLD | 40 | 🔄42 | ↑1.011 | ↓38d | — | -6.7% | -61.71/-64.15 | +7.97% | 20% |
| [CARRARO](https://in.tradingview.com/chart/?symbol=NSE:CARRARO)<br><sub>📶W9 · ↓CMF5d · 🎯SLING</sub> | ✓ SAFE | Axles transmissions agricultural tractors construction equipment | 🟢 BULL_OVERSOLD | 11 | ↑53 | ↑0.999 | ↓14d | — | -7.0% | -60.71/-60.85 | +3.87% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · ↑CMF1d · 🎯SLING</sub> | ✓ SAFE | Complex generics and specialty formulations for global pharma | 🟢 BULL_OVERSOLD | 10 | ↑95 | ↑1.003 | ↓32d | — | -16.7% | -57.94/-60.39 | +4.63% | 20% |
| [EMCURE](https://in.tradingview.com/chart/?symbol=NSE:EMCURE)<br><sub>📶W9 · ↑CMF1d · ⚠️TRAP</sub> | ✓ SAFE | Pharmaceuticals manufacturing antibiotics contraceptives dermatology global markets | 🟢 BULL_OVERSOLD | 5 | ↑73 | ↑0.988 | ↓20d | — | -7.7% | -61.68/-63.75 | +0.55% | 20% |
| [ANURAS](https://in.tradingview.com/chart/?symbol=NSE:ANURAS)<br><sub>📶W9 · ↑CMF2d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Specialty chemical manufacturing for pharmaceuticals agrochemicals | 🟡 BULL_OS_L2 | 58 | ↑52 | ↑0.998 | ↓7d | SQ | -3.1% | -56.68/-56.83 | +2.08% | 20% |
| [GRINFRA](https://in.tradingview.com/chart/?symbol=NSE:GRINFRA)<br><sub>📶W9 · ↑CMF1d · ⚠️TRAP</sub> | ⚠ CAUTION | Road EPC contractor, highways and railways infrastructure | 🟡 BULL_OS_L2 | 58 | ↑28 | ↓0.998 | ↓2d | SQ | +2.5% | -55.67/-57.69 | -1.10% | 20% |
| [LUPIN](https://in.tradingview.com/chart/?symbol=NSE:LUPIN)<br><sub>📶W9 · ↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION | Branded generics, APIs, biotechnology for global pharma markets | 🟡 BULL_OS_L2 | 29 | ↑40 | ↑1.003 | ↑1d | — | +1.6% | -56.23/-58.15 | +1.61% | 20% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>📶W9 · ↑CMF1d · 🎯SLING</sub> | ✓ SAFE | Contract research development manufacturing biotech pharma | 🟡 BULL_OS_L2 | 14 | ↑77 | ↑0.997 | ↓11d | — | -4.6% | -54.78/-56.83 | +1.16% | 20% |
| [JUBLFOOD](https://in.tradingview.com/chart/?symbol=NSE:JUBLFOOD)<br><sub>📶W9 · ↓CMF19d · 🎯SLING</sub> | ✓ SAFE | Domino's Pizza franchise operator serving Indian quick-service restaurant market | 🟡 BULL_OS_L2 | 10 | ↑41 | ↑1.014 | ↓22d | — | -11.7% | -55.73/-59.1 | +4.68% | 20% |
| [DEVYANI](https://in.tradingview.com/chart/?symbol=NSE:DEVYANI)<br><sub>📶W9 · ↓CMF6d · 🎯SLING · DEL63%</sub> | ⚠ CAUTION | Yum Brands franchisee, QSR operator, KFC Dominos Pizza Hut | 🟡 BULL_OS_L2 | 5 | ↑57 | ↑0.999 | ↓27d | — | -13.3% | -55.03/-57.06 | +2.33% | 20% |
| [GRANULES](https://in.tradingview.com/chart/?symbol=NSE:GRANULES)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | APIs, formulation intermediates, finished pharma drugs manufacturer | 📈 BULL_ANY_MID | 69 | ↑83 | ↑1.009 | ↑1d | SQ | +3.2% | -43.88/-46.06 | +3.25% | 20% |
| [TTKPRESTIG](https://in.tradingview.com/chart/?symbol=NSE:TTKPRESTIG)<br><sub>📶W9 · ↑CMF1d · ⚠️TRAP</sub> | ⚠ CAUTION | Pressure cookers, cookware, kitchen appliances for households | 📈 BULL_ANY_MID | 68 | ↑35 | ↑1.015 | ↑2d | SQ | +3.6% | -25.17/-30.6 | +0.96% | 20% |
| [NUVOCO](https://in.tradingview.com/chart/?symbol=NSE:NUVOCO)<br><sub>📶W9 · W↑6d · ↓CMF5d</sub> | ✓ SAFE | Cement and ready-mix concrete manufacturer East North India | 📈 BULL_ANY_MID | 64 | ↑59 | ↑1.019 | ↑1d | SQ | +3.0% | 13.93/11.47 | +2.98% | 20% |
| [MARATHON](https://in.tradingview.com/chart/?symbol=NSE:MARATHON)<br><sub>📶W9 · ↓CMF23d · ⚠️TRAP</sub> | ✓ SAFE | Luxury residential commercial real estate developer MMR region | 📈 BULL_ANY_MID | 63 | ↑27 | ↑1.002 | ↓7d | SQ | +1.9% | -30.46/-32.25 | +0.07% | 20% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>📶W9 · ★ · ↑CMF23d</sub> | ✓ SAFE | Specialty polyester films for packaging and industrial applications | 📈 BULL_ANY_MID | 58 | ↑94 | ↓1.007 | ↑2d | SQ | +4.8% | 0.09/-3.0 | -0.81% | 20% 🟦 |
| [ACI](https://in.tradingview.com/chart/?symbol=NSE:ACI)<br><sub>📶W9 · W↑11d · ↓CMF6d · ⚠️TRAP</sub> | ✓ SAFE | Bromine, industrial salt, potash specialty chemicals exporter | 📈 BULL_ANY_MID | 58 | ↑22 | ↓0.995 | ↓2d | SQ | +1.7% | -10.35/-11.43 | -2.11% | 20% |
| [GUFICBIO](https://in.tradingview.com/chart/?symbol=NSE:GUFICBIO)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Pharmaceutical APIs and formulations manufacturer for generic drugs | 📈 BULL_ANY_MID | 55 | ↑84 | ↑1.010 | ↓15d | SQ | -2.9% | -52.04/-52.92 | +3.97% | 20% |
| [LMW](https://in.tradingview.com/chart/?symbol=NSE:LMW)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Textile spinning machinery and CNC machine tools manufacturer | 📈 BULL_ANY_MID | 50 | ↑70 | ↑1.003 | ↓38d | SQ | -13.9% | -47.17/-50.98 | +1.37% | 20% |
| [MENONBE](https://in.tradingview.com/chart/?symbol=NSE:MENONBE)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 50 | ↑97 | ↑0.995 | ↓15d | SQ | -5.2% | -51.05/-51.94 | +2.75% | 20% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>📶W9 · 🚀SS · ↓CMF11d</sub> | ✓ SAFE | Glass-lined reactors and process equipment for pharma chemicals | 📈 BULL_ANY_MID | 39 | 🔄98 | ↑0.995 | ↓16d | — | -15.8% | -44.4/-44.85 | +5.00% | 20% |
| [SAKAR](https://in.tradingview.com/chart/?symbol=NSE:SAKAR)<br><sub>📶W9 · ↓CMF16d</sub> | ✓ SAFE | Pharma manufacturing across therapeutic segments Ahmedabad | 📈 BULL_ANY_MID | 35 | 🔄97 | ↑1.018 | ↓40d | — | +12.4% | -47.54/-49.19 | +9.10% | 20% 🟦 |
| [KAYNES](https://in.tradingview.com/chart/?symbol=NSE:KAYNES)<br><sub>📶W9 · ↓CMF30d · ÷DIV</sub> | ✓ SAFE | Electronics manufacturing, IoT solutions, industrial and consumer products | 📈 BULL_ANY_MID | 29 | ↑27 | ↑1.012 | ↑1d | — | +3.7% | -45.46/-48.34 | +3.73% | 20% |
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM)<br><sub>📶W9 · ↓CMF18d</sub> | ⚠ CAUTION | Branded generic pharmaceuticals formulations across India Asia Africa | 📈 BULL_ANY_MID | 29 | ↑79 | ↑1.014 | ↑1d | — | +3.0% | -46.26/-51.92 | +2.96% | 20% |
| [JAGSNPHARM](https://in.tradingview.com/chart/?symbol=NSE:JAGSNPHARM)<br><sub>📶W9 · ↓CMF2d</sub> | ✓ SAFE | Women's health and pain management pharmaceutical manufacturer India | 📈 BULL_ANY_MID | 24 | ↑72 | ↑1.018 | ↑1d | — | +5.3% | -49.86/-52.48 | +5.34% | 20% |
| [SURAKSHA](https://in.tradingview.com/chart/?symbol=NSE:SURAKSHA)<br><sub>📶W9 · ↓CMF3d</sub> | ⚠ CAUTION | Pathology radiology diagnostic centers East India healthcare | 📈 BULL_ANY_MID | 24 | ↑79 | ↑1.026 | ↑1d | — | +4.4% | -45.4/-48.2 | +4.44% | 20% |
| [ICRA](https://in.tradingview.com/chart/?symbol=NSE:ICRA)<br><sub>📶W9 · W↑11d · ↑CMF0d · ⚠️TRAP</sub> | ✓ SAFE | Credit ratings, debt analysis, capital markets participants | 📈 BULL_ANY_MID | 18 | ↑30 | ↑1.003 | ↑12d | — | +4.5% | -0.49/-1.24 | +0.46% | 20% |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | Aroma chemicals fragrance ingredients terpenes global export manufacturer | 📈 BULL_ANY_MID | 10 | ↑69 | ↑1.005 | ↓26d | — | -2.6% | -47.14/-48.42 | +3.26% | 20% |
| [STAR](https://in.tradingview.com/chart/?symbol=NSE:STAR)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE | Niche finished dosage pharma formulations global markets | 📈 BULL_ANY_MID | 5 | ↑74 | ↑0.993 | ↓42d | — | +5.1% | -48.65/-49.02 | +1.80% | 20% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Pharmaceuticals: generics, branded drugs, consumer wellness products | 📈 BULL_ANY_MID | 0 | ↑78 | ↓0.996 | ↓25d | — | +1.6% | -25.59/-26.34 | -0.86% | 20% |
| [JUBLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:JUBLPHARMA)<br><sub>📶W9 · ↓CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Radiopharmaceuticals, allergy therapy, contract pharmaceutical manufacturing | 📈 BULL_ANY_MID | 0 | ↑56 | ↓0.995 | ↓40d | — | +6.2% | -35.11/-35.17 | -0.14% | 20% |
| [SUNCLAY](https://in.tradingview.com/chart/?symbol=NSE:SUNCLAY)<br><sub>↑CMF11d · 🎯SLING</sub> | ⚠ CAUTION |  | 🔥 BULL_OS_PPV | 48 | 🔄32 | ↑1.002 | ↓12d | PV | -0.1% | -69.34/-70.64 | +5.34% | 20% |
| [RAMKY](https://in.tradingview.com/chart/?symbol=NSE:RAMKY)<br><sub>W↑1d · 🚀SS · ↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Infrastructure construction, highways, urban development projects | 🔥 BULL_OS_PPV | 40 | 🔄2 | ↑1.006 | ↓53d | PV | -31.9% | -60.79/-61.92 | +7.23% | 20% |
| [KEC](https://in.tradingview.com/chart/?symbol=NSE:KEC)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Power transmission infrastructure EPC contractor global | 🔥 BULL_OS_PPV | 35 | 🔄2 | ↑0.981 | ↓57d | PV | -29.5% | -71.3/-72.9 | +2.76% | 20% |
| [TIIL](https://in.tradingview.com/chart/?symbol=NSE:TIIL)<br><sub>↓CMF30d · 🎯SLING · ÷DIV · DEL83%</sub> | ✓ SAFE | Drum closures, scaffolding systems, textiles, engineering services globally | 🔥 BULL_OS_PPV | 5 | ↑70 | ↑0.988 | ↓32d | PV | -19.6% | -61.98/-63.84 | +1.24% | 20% |
| [TCIEXP](https://in.tradingview.com/chart/?symbol=NSE:TCIEXP)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Express logistics, multi-modal cargo delivery, B2B | ⚡ BULL_ANY_PPV | 5 | ↑32 | ↑0.983 | ↓20d | PV | -5.0% | -50.35/-51.82 | +0.60% | 20% |
| [STYL](https://in.tradingview.com/chart/?symbol=NSE:STYL)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | BFSI payment solutions and communications technology provider | 🟢 BULL_OVERSOLD | 40 | 🔄68 | ↑0.974 | ↓15d | — | -12.6% | -72.88/-74.59 | +1.64% | 20% |
| [ONESOURCE](https://in.tradingview.com/chart/?symbol=NSE:ONESOURCE)<br><sub>↑CMF0d · 🎯SLING</sub> | ✓ SAFE | Specialty pharma CDMO injectable biologics contract manufacturing | 🟢 BULL_OVERSOLD | 35 | 🔄42 | ↑1.000 | ↓20d | — | -10.8% | -60.82/-62.91 | +4.74% | 20% |
| [GKENERGY](https://in.tradingview.com/chart/?symbol=NSE:GKENERGY)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Solar pump EPC services for Indian agriculture | 🟢 BULL_OVERSOLD | 35 | 🔄10 | ↑0.986 | ↓26d | — | -15.7% | -71.3/-71.69 | +7.12% | 20% |
| [SAGCEM](https://in.tradingview.com/chart/?symbol=NSE:SAGCEM)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Cement manufacturing, South and Central India construction | 🟢 BULL_OVERSOLD | 35 | 🔄7 | ↑0.979 | ↓24d | — | -14.2% | -77.36/-78.6 | +2.61% | 20% |
| [SENORES](https://in.tradingview.com/chart/?symbol=NSE:SENORES)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Complex generics manufacturer specialty pharma therapies India | 🟢 BULL_OVERSOLD | 10 | ↑88 | ↑0.991 | ↓15d | — | -5.7% | -66.12/-66.75 | +2.48% | 20% |
| [DEEDEV](https://in.tradingview.com/chart/?symbol=NSE:DEEDEV)<br><sub>↓CMF18d · 🎯SLING</sub> | ✓ SAFE | High-pressure piping systems for oil gas power | 🟢 BULL_OVERSOLD | 6 | ↑94 | ↑0.972 | ↓19d | — | -17.2% | -60.95/-62.81 | +1.13% | 10% 🟩 |
| [FORTIS](https://in.tradingview.com/chart/?symbol=NSE:FORTIS)<br><sub>↓CMF27d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Multi-specialty hospitals, diagnostics, quaternary care delivery | 🟢 BULL_OVERSOLD | 5 | ↑19 | ↑0.994 | ↓25d | — | -17.8% | -62.13/-63.56 | +3.06% | 20% |
| [NEULANDLAB](https://in.tradingview.com/chart/?symbol=NSE:NEULANDLAB)<br><sub>↑CMF1d · ⚠️TRAP</sub> | ✓ SAFE | Pharma APIs and CDMO services for global markets | 🟢 BULL_OVERSOLD | 5 | ↑80 | ↑0.977 | ↓35d | — | -16.7% | -69.37/-70.82 | +1.01% | 20% |
| [TENNIND](https://in.tradingview.com/chart/?symbol=NSE:TENNIND)<br><sub>↓CMF27d · ⚠️TRAP</sub> | ✓ SAFE | Automotive emissions control systems supplier for passenger vehicles | 🟢 BULL_OVERSOLD | 5 | ↑50 | ↑0.977 | ↓25d | — | -13.7% | -68.66/-68.76 | +0.90% | 20% |
| [LINCOLN](https://in.tradingview.com/chart/?symbol=NSE:LINCOLN)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Injectable antibiotics and cardiac drugs manufacturer | 🟢 BULL_OVERSOLD | 5 | ↑58 | ↑0.994 | ↓40d | — | -12.8% | -66.94/-68.09 | +3.23% | 20% |
| [HONAUT](https://in.tradingview.com/chart/?symbol=NSE:HONAUT)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Industrial automation control systems for manufacturing plants | 🟢 BULL_OVERSOLD | 0 | ↑42 | ↓0.984 | ↓27d | — | -7.9% | -68.61/-70.11 | -0.70% | 20% |
| [MAXHEALTH](https://in.tradingview.com/chart/?symbol=NSE:MAXHEALTH)<br><sub>🚀SS · ↓CMF15d · 🎯SLING</sub> | ✓ SAFE | Tertiary quaternary hospital network Delhi NCR North India | 🟡 BULL_OS_L2 | 5 | ↑17 | ↑0.992 | ↓33d | — | -15.9% | -53.0/-54.79 | +2.45% | 20% |
| [CAPLIPOINT](https://in.tradingview.com/chart/?symbol=NSE:CAPLIPOINT)<br><sub>↓CMF17d · 🎯SLING</sub> | ✓ SAFE | Pharma APIs formulations exports Latin America Africa USA | 🟡 BULL_OS_L2 | 5 | ↑75 | ↑0.986 | ↓27d | — | -12.4% | -51.28/-53.03 | +2.34% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ATHERENERG,NSE:RBA,NSE:ACUTAAS,NSE:ITCHOTELS,NSE:WESTLIFE,NSE:SGMART,NSE:YASHO,NSE:CARBORUNIV,NSE:GNA,NSE:SIGMAADV,NSE:INDIASHLTR,NSE:DRAGARWQ,NSE:SESHAPAPER,NSE:CARRARO,NSE:RUBICON,NSE:EMCURE,NSE:ANURAS,NSE:GRINFRA,NSE:LUPIN,NSE:ANTHEM,NSE:JUBLFOOD,NSE:DEVYANI,NSE:GRANULES,NSE:TTKPRESTIG,NSE:NUVOCO,NSE:MARATHON,NSE:GRWRHITECH,NSE:ACI,NSE:GUFICBIO,NSE:LMW,NSE:MENONBE,NSE:SETL,NSE:SAKAR,NSE:KAYNES,NSE:AJANTPHARM,NSE:JAGSNPHARM,NSE:SURAKSHA,NSE:ICRA,NSE:PRIVISCL,NSE:STAR,NSE:ZYDUSLIFE,NSE:JUBLPHARMA,NSE:SUNCLAY,NSE:RAMKY,NSE:KEC,NSE:TIIL,NSE:TCIEXP,NSE:STYL,NSE:ONESOURCE,NSE:GKENERGY,NSE:SAGCEM,NSE:SENORES,NSE:DEEDEV,NSE:FORTIS,NSE:NEULANDLAB,NSE:TENNIND,NSE:LINCOLN,NSE:HONAUT,NSE:MAXHEALTH,NSE:CAPLIPOINT
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (19)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>📶W9 · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Premium electric scooters, charging network, urban mobility | ⚡ BULL_ANY_PPV | 89 | 🔄97 | ↑1.075 | ↑1d | SQ·PV | +14.1% | -14.33/-16.67 | +14.13% | -% |
| [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Burger King franchisee operating QSR restaurants India Indonesia | ⚡ BULL_ANY_PPV | 64 | ↑91 | ↑1.019 | ↑1d | SQ·PV | +4.1% | -49.29/-51.51 | +4.14% | 20% 🟦 |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Pharmaceutical intermediates and specialty chemicals manufacturer globally | ⚡ BULL_ANY_PPV | 59 | ↑92 | ↑1.042 | ↑1d | SQ·PV | +6.7% | -1.34/-7.34 | +6.73% | 20% |
| [ITCHOTELS](https://in.tradingview.com/chart/?symbol=NSE:ITCHOTELS)<br><sub>📶W9 · W↑1d · RVOL13x · ↑CMF0d</sub> | ⚠ CAUTION | Hotel chain, premium and mid-market segments, Indian travelers | ⚡ BULL_ANY_PPV | 59 | ↑54 | ↑1.032 | ↑1d | SQ·PV | +5.2% | 6.18/-1.77 | +5.16% | 20% |
| [WESTLIFE](https://in.tradingview.com/chart/?symbol=NSE:WESTLIFE)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | McDonald's franchise operator West South India QSR | ⚡ BULL_ANY_PPV | 59 | ↑80 | ↑1.038 | ↑1d | SQ·PV | +3.5% | -14.74/-20.35 | +3.47% | 20% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>📶W9 · W↑6d · ★ · ↑CMF0d</sub> | ✓ SAFE | Building materials B2B marketplace connecting manufacturers suppliers traders | ⚡ BULL_ANY_PPV | 58 | ↑95 | ↓1.031 | ↑2d | SQ·PV | +5.7% | 35.48/32.57 | +0.36% | 20% |
| [INDIASHLTR](https://in.tradingview.com/chart/?symbol=NSE:INDIASHLTR)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF0d · 🎯SLING</sub> | ⚠ CAUTION | Housing loans for low income tier 2 3 cities | 🟢 BULL_OVERSOLD | 69 | ↑25 | ↑1.005 | ↑1d | SQ | +1.5% | -49.93/-60.81 | +1.51% | 20% |
| [DRAGARWQ](https://in.tradingview.com/chart/?symbol=NSE:DRAGARWQ)<br><sub>📶W9 · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 69 | ↑50 | ↑1.012 | ↑1d | SQ | +2.1% | -55.85/-61.07 | +2.11% | 20% |
| [ANURAS](https://in.tradingview.com/chart/?symbol=NSE:ANURAS)<br><sub>📶W9 · ↑CMF2d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Specialty chemical manufacturing for pharmaceuticals agrochemicals | 🟡 BULL_OS_L2 | 58 | ↑52 | ↑0.998 | ↓7d | SQ | -3.1% | -56.68/-56.83 | +2.08% | 20% |
| [GRINFRA](https://in.tradingview.com/chart/?symbol=NSE:GRINFRA)<br><sub>📶W9 · ↑CMF1d · ⚠️TRAP</sub> | ⚠ CAUTION | Road EPC contractor, highways and railways infrastructure | 🟡 BULL_OS_L2 | 58 | ↑28 | ↓0.998 | ↓2d | SQ | +2.5% | -55.67/-57.69 | -1.10% | 20% |
| [GRANULES](https://in.tradingview.com/chart/?symbol=NSE:GRANULES)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | APIs, formulation intermediates, finished pharma drugs manufacturer | 📈 BULL_ANY_MID | 69 | ↑83 | ↑1.009 | ↑1d | SQ | +3.2% | -43.88/-46.06 | +3.25% | 20% |
| [TTKPRESTIG](https://in.tradingview.com/chart/?symbol=NSE:TTKPRESTIG)<br><sub>📶W9 · ↑CMF1d · ⚠️TRAP</sub> | ⚠ CAUTION | Pressure cookers, cookware, kitchen appliances for households | 📈 BULL_ANY_MID | 68 | ↑35 | ↑1.015 | ↑2d | SQ | +3.6% | -25.17/-30.6 | +0.96% | 20% |
| [NUVOCO](https://in.tradingview.com/chart/?symbol=NSE:NUVOCO)<br><sub>📶W9 · W↑6d · ↓CMF5d</sub> | ✓ SAFE | Cement and ready-mix concrete manufacturer East North India | 📈 BULL_ANY_MID | 64 | ↑59 | ↑1.019 | ↑1d | SQ | +3.0% | 13.93/11.47 | +2.98% | 20% |
| [MARATHON](https://in.tradingview.com/chart/?symbol=NSE:MARATHON)<br><sub>📶W9 · ↓CMF23d · ⚠️TRAP</sub> | ✓ SAFE | Luxury residential commercial real estate developer MMR region | 📈 BULL_ANY_MID | 63 | ↑27 | ↑1.002 | ↓7d | SQ | +1.9% | -30.46/-32.25 | +0.07% | 20% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>📶W9 · ★ · ↑CMF23d</sub> | ✓ SAFE | Specialty polyester films for packaging and industrial applications | 📈 BULL_ANY_MID | 58 | ↑94 | ↓1.007 | ↑2d | SQ | +4.8% | 0.09/-3.0 | -0.81% | 20% 🟦 |
| [ACI](https://in.tradingview.com/chart/?symbol=NSE:ACI)<br><sub>📶W9 · W↑11d · ↓CMF6d · ⚠️TRAP</sub> | ✓ SAFE | Bromine, industrial salt, potash specialty chemicals exporter | 📈 BULL_ANY_MID | 58 | ↑22 | ↓0.995 | ↓2d | SQ | +1.7% | -10.35/-11.43 | -2.11% | 20% |
| [GUFICBIO](https://in.tradingview.com/chart/?symbol=NSE:GUFICBIO)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Pharmaceutical APIs and formulations manufacturer for generic drugs | 📈 BULL_ANY_MID | 55 | ↑84 | ↑1.010 | ↓15d | SQ | -2.9% | -52.04/-52.92 | +3.97% | 20% |
| [LMW](https://in.tradingview.com/chart/?symbol=NSE:LMW)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Textile spinning machinery and CNC machine tools manufacturer | 📈 BULL_ANY_MID | 50 | ↑70 | ↑1.003 | ↓38d | SQ | -13.9% | -47.17/-50.98 | +1.37% | 20% |
| [MENONBE](https://in.tradingview.com/chart/?symbol=NSE:MENONBE)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 50 | ↑97 | ↑0.995 | ↓15d | SQ | -5.2% | -51.05/-51.94 | +2.75% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ATHERENERG,NSE:RBA,NSE:ACUTAAS,NSE:ITCHOTELS,NSE:WESTLIFE,NSE:SGMART,NSE:INDIASHLTR,NSE:DRAGARWQ,NSE:ANURAS,NSE:GRINFRA,NSE:GRANULES,NSE:TTKPRESTIG,NSE:NUVOCO,NSE:MARATHON,NSE:GRWRHITECH,NSE:ACI,NSE:GUFICBIO,NSE:LMW,NSE:MENONBE
```

---

### 🔥 MAJOR — PPV confirmed (9)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [YASHO](https://in.tradingview.com/chart/?symbol=NSE:YASHO)<br><sub>📶W9 · 🚀SS · ↓CMF13d</sub> | ✓ SAFE | Specialty chemicals manufacturer: antioxidants, aroma, rubber additives | ⚡ BULL_ANY_PPV | 49 | 🔄98 | ↑1.033 | ↑1d | PV | +13.2% | -46.54/-48.8 | +13.18% | 20% 🟦 |
| [CARBORUNIV](https://in.tradingview.com/chart/?symbol=NSE:CARBORUNIV)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Abrasives, ceramics, refractories for industrial manufacturing | ⚡ BULL_ANY_PPV | 35 | 🔄81 | ↑1.021 | ↓27d | PV | +4.2% | -39.65/-40.46 | +9.76% | 20% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Rear axles and drive shafts for commercial vehicles | ⚡ BULL_ANY_PPV | 19 | ↑91 | ↑1.038 | ↑1d | PV | +8.1% | -26.67/-30.88 | +8.06% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [SUNCLAY](https://in.tradingview.com/chart/?symbol=NSE:SUNCLAY)<br><sub>↑CMF11d · 🎯SLING</sub> | ⚠ CAUTION |  | 🔥 BULL_OS_PPV | 48 | 🔄32 | ↑1.002 | ↓12d | PV | -0.1% | -69.34/-70.64 | +5.34% | 20% |
| [RAMKY](https://in.tradingview.com/chart/?symbol=NSE:RAMKY)<br><sub>W↑1d · 🚀SS · ↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Infrastructure construction, highways, urban development projects | 🔥 BULL_OS_PPV | 40 | 🔄2 | ↑1.006 | ↓53d | PV | -31.9% | -60.79/-61.92 | +7.23% | 20% |
| [KEC](https://in.tradingview.com/chart/?symbol=NSE:KEC)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Power transmission infrastructure EPC contractor global | 🔥 BULL_OS_PPV | 35 | 🔄2 | ↑0.981 | ↓57d | PV | -29.5% | -71.3/-72.9 | +2.76% | 20% |
| [TIIL](https://in.tradingview.com/chart/?symbol=NSE:TIIL)<br><sub>↓CMF30d · 🎯SLING · ÷DIV · DEL83%</sub> | ✓ SAFE | Drum closures, scaffolding systems, textiles, engineering services globally | 🔥 BULL_OS_PPV | 5 | ↑70 | ↑0.988 | ↓32d | PV | -19.6% | -61.98/-63.84 | +1.24% | 20% |
| [TCIEXP](https://in.tradingview.com/chart/?symbol=NSE:TCIEXP)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Express logistics, multi-modal cargo delivery, B2B | ⚡ BULL_ANY_PPV | 5 | ↑32 | ↑0.983 | ↓20d | PV | -5.0% | -50.35/-51.82 | +0.60% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:YASHO,NSE:CARBORUNIV,NSE:GNA,NSE:SIGMAADV,NSE:SUNCLAY,NSE:RAMKY,NSE:KEC,NSE:TIIL,NSE:TCIEXP
```

### 🟢 OVERSOLD — reversal from −53/−60 (28)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SESHAPAPER](https://in.tradingview.com/chart/?symbol=NSE:SESHAPAPER)<br><sub>📶W9 · 🚀SS · ↓CMF15d · 🎯SLING</sub> | ✓ SAFE | Integrated paper and paperboards manufacturer Tamil Nadu facilities | 🟢 BULL_OVERSOLD | 40 | 🔄42 | ↑1.011 | ↓38d | — | -6.7% | -61.71/-64.15 | +7.97% | 20% |
| [CARRARO](https://in.tradingview.com/chart/?symbol=NSE:CARRARO)<br><sub>📶W9 · ↓CMF5d · 🎯SLING</sub> | ✓ SAFE | Axles transmissions agricultural tractors construction equipment | 🟢 BULL_OVERSOLD | 11 | ↑53 | ↑0.999 | ↓14d | — | -7.0% | -60.71/-60.85 | +3.87% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · ↑CMF1d · 🎯SLING</sub> | ✓ SAFE | Complex generics and specialty formulations for global pharma | 🟢 BULL_OVERSOLD | 10 | ↑95 | ↑1.003 | ↓32d | — | -16.7% | -57.94/-60.39 | +4.63% | 20% |
| [EMCURE](https://in.tradingview.com/chart/?symbol=NSE:EMCURE)<br><sub>📶W9 · ↑CMF1d · ⚠️TRAP</sub> | ✓ SAFE | Pharmaceuticals manufacturing antibiotics contraceptives dermatology global markets | 🟢 BULL_OVERSOLD | 5 | ↑73 | ↑0.988 | ↓20d | — | -7.7% | -61.68/-63.75 | +0.55% | 20% |
| [LUPIN](https://in.tradingview.com/chart/?symbol=NSE:LUPIN)<br><sub>📶W9 · ↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION | Branded generics, APIs, biotechnology for global pharma markets | 🟡 BULL_OS_L2 | 29 | ↑40 | ↑1.003 | ↑1d | — | +1.6% | -56.23/-58.15 | +1.61% | 20% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>📶W9 · ↑CMF1d · 🎯SLING</sub> | ✓ SAFE | Contract research development manufacturing biotech pharma | 🟡 BULL_OS_L2 | 14 | ↑77 | ↑0.997 | ↓11d | — | -4.6% | -54.78/-56.83 | +1.16% | 20% |
| [JUBLFOOD](https://in.tradingview.com/chart/?symbol=NSE:JUBLFOOD)<br><sub>📶W9 · ↓CMF19d · 🎯SLING</sub> | ✓ SAFE | Domino's Pizza franchise operator serving Indian quick-service restaurant market | 🟡 BULL_OS_L2 | 10 | ↑41 | ↑1.014 | ↓22d | — | -11.7% | -55.73/-59.1 | +4.68% | 20% |
| [DEVYANI](https://in.tradingview.com/chart/?symbol=NSE:DEVYANI)<br><sub>📶W9 · ↓CMF6d · 🎯SLING · DEL63%</sub> | ⚠ CAUTION | Yum Brands franchisee, QSR operator, KFC Dominos Pizza Hut | 🟡 BULL_OS_L2 | 5 | ↑57 | ↑0.999 | ↓27d | — | -13.3% | -55.03/-57.06 | +2.33% | 20% |
| [STYL](https://in.tradingview.com/chart/?symbol=NSE:STYL)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | BFSI payment solutions and communications technology provider | 🟢 BULL_OVERSOLD | 40 | 🔄68 | ↑0.974 | ↓15d | — | -12.6% | -72.88/-74.59 | +1.64% | 20% |
| [ONESOURCE](https://in.tradingview.com/chart/?symbol=NSE:ONESOURCE)<br><sub>↑CMF0d · 🎯SLING</sub> | ✓ SAFE | Specialty pharma CDMO injectable biologics contract manufacturing | 🟢 BULL_OVERSOLD | 35 | 🔄42 | ↑1.000 | ↓20d | — | -10.8% | -60.82/-62.91 | +4.74% | 20% |
| [GKENERGY](https://in.tradingview.com/chart/?symbol=NSE:GKENERGY)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Solar pump EPC services for Indian agriculture | 🟢 BULL_OVERSOLD | 35 | 🔄10 | ↑0.986 | ↓26d | — | -15.7% | -71.3/-71.69 | +7.12% | 20% |
| [SAGCEM](https://in.tradingview.com/chart/?symbol=NSE:SAGCEM)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Cement manufacturing, South and Central India construction | 🟢 BULL_OVERSOLD | 35 | 🔄7 | ↑0.979 | ↓24d | — | -14.2% | -77.36/-78.6 | +2.61% | 20% |
| [BANSALWIRE](https://in.tradingview.com/chart/?symbol=NSE:BANSALWIRE)<br><sub>↓CMF2d · ⚠️TRAP</sub> | ✓ SAFE | Steel and stainless steel wire manufacturer India | 🟢 BULL_OVERSOLD | 14 | ↓0 | ↑0.470 | ↓11d | — | -81.7% | -60.65/-60.92 | -2.77% | 20% 🟦 |
| [KRN](https://in.tradingview.com/chart/?symbol=NSE:KRN)<br><sub>↓CMF29d · 🎯SLING</sub> | ✓ SAFE | Heat exchanger manufacturer HVAC refrigeration OEM supplier | 🟢 BULL_OVERSOLD | 10 | ↓77 | ↑0.934 | ↓15d | — | -23.2% | -68.12/-68.48 | +5.00% | 10% 🟩 |
| [SENORES](https://in.tradingview.com/chart/?symbol=NSE:SENORES)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Complex generics manufacturer specialty pharma therapies India | 🟢 BULL_OVERSOLD | 10 | ↑88 | ↑0.991 | ↓15d | — | -5.7% | -66.12/-66.75 | +2.48% | 20% |
| [DEEDEV](https://in.tradingview.com/chart/?symbol=NSE:DEEDEV)<br><sub>↓CMF18d · 🎯SLING</sub> | ✓ SAFE | High-pressure piping systems for oil gas power | 🟢 BULL_OVERSOLD | 6 | ↑94 | ↑0.972 | ↓19d | — | -17.2% | -60.95/-62.81 | +1.13% | 10% 🟩 |
| [FORTIS](https://in.tradingview.com/chart/?symbol=NSE:FORTIS)<br><sub>↓CMF27d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Multi-specialty hospitals, diagnostics, quaternary care delivery | 🟢 BULL_OVERSOLD | 5 | ↑19 | ↑0.994 | ↓25d | — | -17.8% | -62.13/-63.56 | +3.06% | 20% |
| [NEULANDLAB](https://in.tradingview.com/chart/?symbol=NSE:NEULANDLAB)<br><sub>↑CMF1d · ⚠️TRAP</sub> | ✓ SAFE | Pharma APIs and CDMO services for global markets | 🟢 BULL_OVERSOLD | 5 | ↑80 | ↑0.977 | ↓35d | — | -16.7% | -69.37/-70.82 | +1.01% | 20% |
| [TENNIND](https://in.tradingview.com/chart/?symbol=NSE:TENNIND)<br><sub>↓CMF27d · ⚠️TRAP</sub> | ✓ SAFE | Automotive emissions control systems supplier for passenger vehicles | 🟢 BULL_OVERSOLD | 5 | ↑50 | ↑0.977 | ↓25d | — | -13.7% | -68.66/-68.76 | +0.90% | 20% |
| [PARKHOSPS](https://in.tradingview.com/chart/?symbol=NSE:PARKHOSPS)<br><sub>↓CMF0d · 🎯SLING</sub> | ✓ SAFE | Multi-specialty hospital chain North India tertiary care | 🟢 BULL_OVERSOLD | 5 | ↓50 | ↑0.956 | ↓26d | — | -21.2% | -70.01/-71.04 | +2.12% | 20% |
| [VIMTALABS](https://in.tradingview.com/chart/?symbol=NSE:VIMTALABS)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Contract research testing pharma biotech chemicals | 🟢 BULL_OVERSOLD | 5 | ↓43 | ↑0.969 | ↓36d | — | -23.0% | -73.65/-74.43 | +4.54% | 20% |
| [UNIPARTS](https://in.tradingview.com/chart/?symbol=NSE:UNIPARTS)<br><sub>🚀SS · ↓CMF20d · ⚠️TRAP</sub> | ✓ SAFE | Off-highway vehicle components for agriculture construction mining | 🟢 BULL_OVERSOLD | 5 | ↓85 | ↑0.959 | ↓60d+ | — | -5.6% | -68.13/-68.55 | +0.76% | 20% |
| [MMFL](https://in.tradingview.com/chart/?symbol=NSE:MMFL)<br><sub>↓CMF29d · 🎯SLING</sub> | ✓ SAFE | Steel forging components for vehicles and machinery | 🟢 BULL_OVERSOLD | 5 | ↓75 | ↑0.956 | ↓33d | — | -21.2% | -74.51/-74.91 | +1.31% | 20% |
| [LINCOLN](https://in.tradingview.com/chart/?symbol=NSE:LINCOLN)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Injectable antibiotics and cardiac drugs manufacturer | 🟢 BULL_OVERSOLD | 5 | ↑58 | ↑0.994 | ↓40d | — | -12.8% | -66.94/-68.09 | +3.23% | 20% |
| [HONAUT](https://in.tradingview.com/chart/?symbol=NSE:HONAUT)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Industrial automation control systems for manufacturing plants | 🟢 BULL_OVERSOLD | 0 | ↑42 | ↓0.984 | ↓27d | — | -7.9% | -68.61/-70.11 | -0.70% | 20% |
| [CANHLIFE](https://in.tradingview.com/chart/?symbol=NSE:CANHLIFE)<br><sub>↓CMF0d · ⚠️TRAP</sub> | ⚠ CAUTION | Life insurance through bank distribution channels | 🟢 BULL_OVERSOLD | 0 | ↓41 | ↓0.944 | ↓29d | — | -19.7% | -73.3/-73.56 | -2.28% | 20% |
| [MAXHEALTH](https://in.tradingview.com/chart/?symbol=NSE:MAXHEALTH)<br><sub>🚀SS · ↓CMF15d · 🎯SLING</sub> | ✓ SAFE | Tertiary quaternary hospital network Delhi NCR North India | 🟡 BULL_OS_L2 | 5 | ↑17 | ↑0.992 | ↓33d | — | -15.9% | -53.0/-54.79 | +2.45% | 20% |
| [CAPLIPOINT](https://in.tradingview.com/chart/?symbol=NSE:CAPLIPOINT)<br><sub>↓CMF17d · 🎯SLING</sub> | ✓ SAFE | Pharma APIs formulations exports Latin America Africa USA | 🟡 BULL_OS_L2 | 5 | ↑75 | ↑0.986 | ↓27d | — | -12.4% | -51.28/-53.03 | +2.34% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SESHAPAPER,NSE:CARRARO,NSE:RUBICON,NSE:EMCURE,NSE:LUPIN,NSE:ANTHEM,NSE:JUBLFOOD,NSE:DEVYANI,NSE:STYL,NSE:ONESOURCE,NSE:GKENERGY,NSE:SAGCEM,NSE:BANSALWIRE,NSE:KRN,NSE:SENORES,NSE:DEEDEV,NSE:FORTIS,NSE:NEULANDLAB,NSE:TENNIND,NSE:PARKHOSPS,NSE:VIMTALABS,NSE:UNIPARTS,NSE:MMFL,NSE:LINCOLN,NSE:HONAUT,NSE:CANHLIFE,NSE:MAXHEALTH,NSE:CAPLIPOINT
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (11)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>📶W9 · 🚀SS · ↓CMF11d</sub> | ✓ SAFE | Glass-lined reactors and process equipment for pharma chemicals | 📈 BULL_ANY_MID | 39 | 🔄98 | ↑0.995 | ↓16d | — | -15.8% | -44.4/-44.85 | +5.00% | 20% |
| [SAKAR](https://in.tradingview.com/chart/?symbol=NSE:SAKAR)<br><sub>📶W9 · ↓CMF16d</sub> | ✓ SAFE | Pharma manufacturing across therapeutic segments Ahmedabad | 📈 BULL_ANY_MID | 35 | 🔄97 | ↑1.018 | ↓40d | — | +12.4% | -47.54/-49.19 | +9.10% | 20% 🟦 |
| [KAYNES](https://in.tradingview.com/chart/?symbol=NSE:KAYNES)<br><sub>📶W9 · ↓CMF30d · ÷DIV</sub> | ✓ SAFE | Electronics manufacturing, IoT solutions, industrial and consumer products | 📈 BULL_ANY_MID | 29 | ↑27 | ↑1.012 | ↑1d | — | +3.7% | -45.46/-48.34 | +3.73% | 20% |
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM)<br><sub>📶W9 · ↓CMF18d</sub> | ⚠ CAUTION | Branded generic pharmaceuticals formulations across India Asia Africa | 📈 BULL_ANY_MID | 29 | ↑79 | ↑1.014 | ↑1d | — | +3.0% | -46.26/-51.92 | +2.96% | 20% |
| [JAGSNPHARM](https://in.tradingview.com/chart/?symbol=NSE:JAGSNPHARM)<br><sub>📶W9 · ↓CMF2d</sub> | ✓ SAFE | Women's health and pain management pharmaceutical manufacturer India | 📈 BULL_ANY_MID | 24 | ↑72 | ↑1.018 | ↑1d | — | +5.3% | -49.86/-52.48 | +5.34% | 20% |
| [SURAKSHA](https://in.tradingview.com/chart/?symbol=NSE:SURAKSHA)<br><sub>📶W9 · ↓CMF3d</sub> | ⚠ CAUTION | Pathology radiology diagnostic centers East India healthcare | 📈 BULL_ANY_MID | 24 | ↑79 | ↑1.026 | ↑1d | — | +4.4% | -45.4/-48.2 | +4.44% | 20% |
| [ICRA](https://in.tradingview.com/chart/?symbol=NSE:ICRA)<br><sub>📶W9 · W↑11d · ↑CMF0d · ⚠️TRAP</sub> | ✓ SAFE | Credit ratings, debt analysis, capital markets participants | 📈 BULL_ANY_MID | 18 | ↑30 | ↑1.003 | ↑12d | — | +4.5% | -0.49/-1.24 | +0.46% | 20% |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | Aroma chemicals fragrance ingredients terpenes global export manufacturer | 📈 BULL_ANY_MID | 10 | ↑69 | ↑1.005 | ↓26d | — | -2.6% | -47.14/-48.42 | +3.26% | 20% |
| [STAR](https://in.tradingview.com/chart/?symbol=NSE:STAR)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE | Niche finished dosage pharma formulations global markets | 📈 BULL_ANY_MID | 5 | ↑74 | ↑0.993 | ↓42d | — | +5.1% | -48.65/-49.02 | +1.80% | 20% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Pharmaceuticals: generics, branded drugs, consumer wellness products | 📈 BULL_ANY_MID | 0 | ↑78 | ↓0.996 | ↓25d | — | +1.6% | -25.59/-26.34 | -0.86% | 20% |
| [JUBLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:JUBLPHARMA)<br><sub>📶W9 · ↓CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Radiopharmaceuticals, allergy therapy, contract pharmaceutical manufacturing | 📈 BULL_ANY_MID | 0 | ↑56 | ↓0.995 | ↓40d | — | +6.2% | -35.11/-35.17 | -0.14% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SETL,NSE:SAKAR,NSE:KAYNES,NSE:AJANTPHARM,NSE:JAGSNPHARM,NSE:SURAKSHA,NSE:ICRA,NSE:PRIVISCL,NSE:STAR,NSE:ZYDUSLIFE,NSE:JUBLPHARMA
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
