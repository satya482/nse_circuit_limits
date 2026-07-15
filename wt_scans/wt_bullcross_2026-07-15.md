> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-07-15
*Generated 2026-07-15 15:45 IST*

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

**Total bull crosses today: 65** · 29 inside active squeeze

```
NSE:VIMTALABS,NSE:ENDURANCE,NSE:JUBLPHARMA,NSE:RACLGEAR,NSE:FLUOROCHEM,NSE:HIRECT,NSE:HEIDELBERG,NSE:WOCKPHARMA,NSE:GABRIEL,NSE:GHCLTEXTIL,NSE:ATHERENERG,NSE:RATEGAIN,NSE:5PAISA,NSE:AIAENG,NSE:LLOYDSME,NSE:METROPOLIS,NSE:VISHNU,NSE:POLYMED,NSE:MARKSANS,NSE:BLUSPRING,NSE:HONAUT,NSE:INNOVACAP,NSE:ACUTAAS,NSE:BHEL,NSE:UNIMECH,NSE:SHREECEM,NSE:ABCAPITAL,NSE:BAJAJHCARE,NSE:OFSS,NSE:WELENT,NSE:JLHL,NSE:MADRASFERT,NSE:KEC,NSE:JKLAKSHMI,NSE:TRITURBINE,NSE:SOLEX,NSE:PRSMJOHNSN,NSE:COALINDIA,NSE:POLICYBZR,NSE:KPIGREEN,NSE:IGIL,NSE:FIEMIND,NSE:BALMLAWRIE,NSE:ANDHRAPAP,NSE:AUTOAXLES,NSE:UBL,NSE:GANDHITUBE,NSE:ORIENTCEM,NSE:ICICIGI,NSE:GMDCLTD,NSE:PNB,NSE:AMBUJACEM,NSE:ALICON,NSE:SEAMECLTD,NSE:UNIONBANK,NSE:IGPL,NSE:GOCOLORS,NSE:HDFCLIFE,NSE:IRCON,NSE:TMPV,NSE:PIIND,NSE:ONEPOINT,NSE:SCI,NSE:ASTEC,NSE:TEAMLEASE
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (31)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [VIMTALABS](https://in.tradingview.com/chart/?symbol=NSE:VIMTALABS)<br><sub>📶W9 · W↑71d · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Contract testing and research services for pharma and chemicals | ⚡ BULL_ANY_PPV | 94 | 🔄60 | ↑1.016 | ↑1d | SQ·PV | +3.6% | 6.0/5.57 | +3.56% | 20% |
| [ENDURANCE](https://in.tradingview.com/chart/?symbol=NSE:ENDURANCE)<br><sub>📶W9 · W↑66d · ↑CMF1d</sub> | ✓ SAFE | Aluminum castings, suspension, braking systems for automakers | ⚡ BULL_ANY_PPV | 88 | 🔄56 | ↑1.022 | ↑7d | SQ·PV | +3.7% | 31.96/27.7 | +2.43% | 20% |
| [JUBLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:JUBLPHARMA)<br><sub>📶W9 · W↑78d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Radiopharmaceuticals, allergy immunotherapy, pharma contract manufacturing | ⚡ BULL_ANY_PPV | 87 | 🔄44 | ↑1.047 | ↑3d | SQ·PV | +6.7% | 20.19/1.77 | +5.54% | 20% |
| [RACLGEAR](https://in.tradingview.com/chart/?symbol=NSE:RACLGEAR)<br><sub>📶W9 · W↑18d · ↓CMF22d</sub> | ✓ SAFE | Automotive gears and precision components for global OEMs | ⚡ BULL_ANY_PPV | 63 | ↑70 | ↑1.025 | ↑2d | SQ·PV | +4.2% | -1.59/-8.47 | +1.93% | 20% 🟦 |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>📶W9 · W↑71d · ↑CMF30d</sub> | ✓ SAFE | PTFE fluorochemicals manufacturer specialty chemicals sector | ⚡ BULL_ANY_PPV | 56 | ↑74 | ↑1.046 | ↑4d | SQ·PV | +6.9% | 43.25/33.45 | +5.29% | 20% |
| [HIRECT](https://in.tradingview.com/chart/?symbol=NSE:HIRECT)<br><sub>📶W9 · RVOL15x · ↑CMF0d</sub> | ✓ SAFE | Power electronics converters rectifiers railway locomotive traction systems | ⚡ BULL_ANY_PPV | 49 | 🔄95 | ↑1.148 | ↑1d | PV | +19.9% | -16.3/-28.41 | +19.88% | 20% |
| [HEIDELBERG](https://in.tradingview.com/chart/?symbol=NSE:HEIDELBERG)<br><sub>📶W9 · W↑13d · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 45 | 🔄25 | ↑1.026 | ↑10d | PV | +6.2% | 44.05/39.51 | +2.88% | 20% |
| [WOCKPHARMA](https://in.tradingview.com/chart/?symbol=NSE:WOCKPHARMA)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Pharma manufacturing: injectables, orals, topicals, biopharmaceuticals globally | ⚡ BULL_ANY_PPV | 40 | 🔄82 | ↑1.008 | ↓25d | PV | +3.1% | -36.88/-39.15 | +2.13% | 20% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>📶W9 · W↑23d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Shock absorbers struts two wheeler four wheeler OEM aftermarket | ⚡ BULL_ANY_PPV | 30 | 🔄81 | ↑1.069 | ↑23d | PV | +30.2% | 46.15/38.84 | +8.48% | 20% |
| [GHCLTEXTIL](https://in.tradingview.com/chart/?symbol=NSE:GHCLTEXTIL)<br><sub>📶W9 · W↑13d · ★ · ↑CMF9d</sub> | ✓ SAFE | Bleached fabric and specialty chemicals textile manufacturer | ⚡ BULL_ANY_PPV | 7 | ↑86 | ↑1.047 | ↑13d | PV | +21.3% | 62.97/62.97 | +4.04% | 20% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>📶W9 · W↑13d · 🚀SS · ★ · ↑CMF12d</sub> | ✓ SAFE | Electric scooters, batteries, charging infrastructure, premium segment | ⚡ BULL_ANY_PPV | 5 | ↑99 | ↑1.090 | ↑15d | PV | +30.9% | 65.09/63.65 | +7.87% | 20% |
| [RATEGAIN](https://in.tradingview.com/chart/?symbol=NSE:RATEGAIN)<br><sub>📶W9 · W↑71d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | Travel SaaS platform, revenue management, global hotels | ⚡ BULL_ANY_PPV | 0 | ↑96 | ↑1.041 | ↑60d+ | PV | +70.2% | 62.96/62.15 | +2.62% | 20% |
| [5PAISA](https://in.tradingview.com/chart/?symbol=NSE:5PAISA)<br><sub>📶W9 · W↑23d · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Digital discount brokerage platform for equity derivatives commodity trading | ⚡ BULL_ANY_PPV | 0 | ↑65 | ↑1.044 | ↑23d | PV | +26.2% | 52.5/47.37 | +1.53% | 20% |
| [AIAENG](https://in.tradingview.com/chart/?symbol=NSE:AIAENG)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | High-chromium grinding media and liners for cement mining | 📈 BULL_ANY_MID | 99 | 🔄83 | ↑1.014 | ↑1d | SQ | +1.4% | 13.28/10.17 | +1.44% | 20% |
| [LLOYDSME](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSME)<br><sub>📶W9 · 🚀SS · ↓CMF14d</sub> | ✓ SAFE | Iron ore mining, sponge iron production, power generation | 📈 BULL_ANY_MID | 94 | 🔄78 | ↑1.022 | ↑1d | SQ | +3.1% | 6.52/1.69 | +3.12% | 20% |
| [METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS)<br><sub>📶W9 · W↑66d · 🚀SS · ↓CMF20d</sub> | ⚠ CAUTION | Diagnostic pathology labs clinical testing centers urban India | 📈 BULL_ANY_MID | 90 | 🔄73 | ↑1.020 | ↑5d | SQ | +4.1% | 49.73/46.67 | +2.23% | 20% |
| [VISHNU](https://in.tradingview.com/chart/?symbol=NSE:VISHNU)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Chromium Barium chemicals manufacturer serving industrial applications | 📈 BULL_ANY_MID | 63 | ↑72 | ↑1.027 | ↑2d | SQ | +4.0% | 6.97/-0.97 | +2.20% | 20% |
| [POLYMED](https://in.tradingview.com/chart/?symbol=NSE:POLYMED)<br><sub>📶W9 · W↑23d · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Plastic medical disposables manufacturer exporting surgical devices globally | 📈 BULL_ANY_MID | 60 | ↑43 | ↑1.029 | ↑5d | SQ | +6.3% | 31.78/29.2 | +3.08% | 20% |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS)<br><sub>📶W9 · W↑71d · ↓CMF16d</sub> | ✓ SAFE | Generic pharmaceutical formulations for regulated global markets | 📈 BULL_ANY_MID | 59 | ↑91 | ↑1.025 | ↑6d | SQ | +5.6% | 56.58/54.94 | +1.77% | 20% |
| [BLUSPRING](https://in.tradingview.com/chart/?symbol=NSE:BLUSPRING)<br><sub>📶W9 · W↑78d · ↓CMF0d</sub> | ✓ SAFE | I don't have specific information about Bluspring Enterprises Ltd's operations | 📈 BULL_ANY_MID | 56 | ↑95 | ↑1.034 | ↑4d | SQ | +9.4% | 38.04/37.1 | +3.10% | 10% 🟨 |
| [HONAUT](https://in.tradingview.com/chart/?symbol=NSE:HONAUT)<br><sub>📶W9 · W↑66d · 🚀SS · ↓CMF19d</sub> | ⚠ CAUTION | Industrial automation controls systems manufacturing | 📈 BULL_ANY_MID | 54 | 🔄66 | ↑1.026 | ↑1d | — | +3.9% | 17.63/17.0 | +3.89% | 20% |
| [INNOVACAP](https://in.tradingview.com/chart/?symbol=NSE:INNOVACAP)<br><sub>📶W9 · W↑88d · ★ · ↓CMF11d</sub> | ✓ SAFE | Tablet manufacturing pharmaceuticals India generic drugs | 📈 BULL_ANY_MID | 53 | ↑81 | ↓1.009 | ↑7d | SQ | +3.9% | 59.76/59.25 | -0.21% | 20% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Specialty chemicals manufacturer serving pharmaceutical intermediates globally | 📈 BULL_ANY_MID | 52 | 🔄99 | ↑1.021 | ↑3d | — | +4.3% | 37.38/36.79 | +2.52% | 20% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄91 | ↑1.037 | ↑1d | — | +3.4% | -7.35/-13.15 | +3.43% | 20% |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH)<br><sub>📶W9 · W↑66d · 🚀SS · ↓CMF10d</sub> | ✓ SAFE | Precision aerospace components and tooling manufacturer | 📈 BULL_ANY_MID | 48 | ↑76 | ↓1.020 | ↑12d | SQ | +10.6% | 47.13/44.37 | +0.34% | 10% 🟩 |
| [SHREECEM](https://in.tradingview.com/chart/?symbol=NSE:SHREECEM)<br><sub>📶W9 · W↑23d · 🚀SS · ↓CMF5d</sub> | ⚠ CAUTION | Cement manufacturing, building materials, construction sector | 📈 BULL_ANY_MID | 35 | 🔄38 | ↑1.022 | ↑23d | — | +11.4% | 44.14/43.8 | +2.45% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑63d · ↑CMF16d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.020 | ↑3d | — | +5.4% | 47.71/46.67 | -0.44% | 20% |
| [BAJAJHCARE](https://in.tradingview.com/chart/?symbol=NSE:BAJAJHCARE)<br><sub>📶W9 · W↑23d · ↑CMF12d</sub> | ✓ SAFE | APIs and formulations manufacturer for global pharma markets | 📈 BULL_ANY_MID | 7 | ↑23 | ↑1.054 | ↑13d | — | +19.6% | 51.44/48.0 | +4.60% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Banking software solutions for financial institutions | 📈 BULL_ANY_MID | 5 | ↑90 | ↑1.055 | ↑15d | — | +20.9% | 50.17/48.27 | +4.64% | 20% |
| [WELENT](https://in.tradingview.com/chart/?symbol=NSE:WELENT)<br><sub>📶W9 · W↑66d · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Infrastructure developer: highways, water systems, oil pipelines | 📈 BULL_ANY_MID | 5 | ↑80 | ↑1.025 | ↑37d | — | +25.0% | 63.31/62.78 | +1.16% | 20% |
| [JLHL](https://in.tradingview.com/chart/?symbol=NSE:JLHL)<br><sub>📶W9 · W↑66d · 🚀SS · ↑CMF11d</sub> | ⚠ CAUTION | Multi-specialty hospital chain serving Mumbai and western India | 📈 BULL_ANY_MID | 5 | ↑60 | ↑1.027 | ↑23d | — | +14.0% | 67.67/66.56 | +1.10% | 20% |

```
NSE:VIMTALABS,NSE:ENDURANCE,NSE:JUBLPHARMA,NSE:RACLGEAR,NSE:FLUOROCHEM,NSE:HIRECT,NSE:HEIDELBERG,NSE:WOCKPHARMA,NSE:GABRIEL,NSE:GHCLTEXTIL,NSE:ATHERENERG,NSE:RATEGAIN,NSE:5PAISA,NSE:AIAENG,NSE:LLOYDSME,NSE:METROPOLIS,NSE:VISHNU,NSE:POLYMED,NSE:MARKSANS,NSE:BLUSPRING,NSE:HONAUT,NSE:INNOVACAP,NSE:ACUTAAS,NSE:BHEL,NSE:UNIMECH,NSE:SHREECEM,NSE:ABCAPITAL,NSE:BAJAJHCARE,NSE:OFSS,NSE:WELENT,NSE:JLHL
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (49)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [VIMTALABS](https://in.tradingview.com/chart/?symbol=NSE:VIMTALABS)<br><sub>📶W9 · W↑71d · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Contract testing and research services for pharma and chemicals | ⚡ BULL_ANY_PPV | 94 | 🔄60 | ↑1.016 | ↑1d | SQ·PV | +3.6% | 6.0/5.57 | +3.56% | 20% |
| [ENDURANCE](https://in.tradingview.com/chart/?symbol=NSE:ENDURANCE)<br><sub>📶W9 · W↑66d · ↑CMF1d</sub> | ✓ SAFE | Aluminum castings, suspension, braking systems for automakers | ⚡ BULL_ANY_PPV | 88 | 🔄56 | ↑1.022 | ↑7d | SQ·PV | +3.7% | 31.96/27.7 | +2.43% | 20% |
| [JUBLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:JUBLPHARMA)<br><sub>📶W9 · W↑78d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Radiopharmaceuticals, allergy immunotherapy, pharma contract manufacturing | ⚡ BULL_ANY_PPV | 87 | 🔄44 | ↑1.047 | ↑3d | SQ·PV | +6.7% | 20.19/1.77 | +5.54% | 20% |
| [RACLGEAR](https://in.tradingview.com/chart/?symbol=NSE:RACLGEAR)<br><sub>📶W9 · W↑18d · ↓CMF22d</sub> | ✓ SAFE | Automotive gears and precision components for global OEMs | ⚡ BULL_ANY_PPV | 63 | ↑70 | ↑1.025 | ↑2d | SQ·PV | +4.2% | -1.59/-8.47 | +1.93% | 20% 🟦 |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>📶W9 · W↑71d · ↑CMF30d</sub> | ✓ SAFE | PTFE fluorochemicals manufacturer specialty chemicals sector | ⚡ BULL_ANY_PPV | 56 | ↑74 | ↑1.046 | ↑4d | SQ·PV | +6.9% | 43.25/33.45 | +5.29% | 20% |
| [HIRECT](https://in.tradingview.com/chart/?symbol=NSE:HIRECT)<br><sub>📶W9 · RVOL15x · ↑CMF0d</sub> | ✓ SAFE | Power electronics converters rectifiers railway locomotive traction systems | ⚡ BULL_ANY_PPV | 49 | 🔄95 | ↑1.148 | ↑1d | PV | +19.9% | -16.3/-28.41 | +19.88% | 20% |
| [HEIDELBERG](https://in.tradingview.com/chart/?symbol=NSE:HEIDELBERG)<br><sub>📶W9 · W↑13d · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 45 | 🔄25 | ↑1.026 | ↑10d | PV | +6.2% | 44.05/39.51 | +2.88% | 20% |
| [WOCKPHARMA](https://in.tradingview.com/chart/?symbol=NSE:WOCKPHARMA)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Pharma manufacturing: injectables, orals, topicals, biopharmaceuticals globally | ⚡ BULL_ANY_PPV | 40 | 🔄82 | ↑1.008 | ↓25d | PV | +3.1% | -36.88/-39.15 | +2.13% | 20% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>📶W9 · W↑23d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Shock absorbers struts two wheeler four wheeler OEM aftermarket | ⚡ BULL_ANY_PPV | 30 | 🔄81 | ↑1.069 | ↑23d | PV | +30.2% | 46.15/38.84 | +8.48% | 20% |
| [GHCLTEXTIL](https://in.tradingview.com/chart/?symbol=NSE:GHCLTEXTIL)<br><sub>📶W9 · W↑13d · ★ · ↑CMF9d</sub> | ✓ SAFE | Bleached fabric and specialty chemicals textile manufacturer | ⚡ BULL_ANY_PPV | 7 | ↑86 | ↑1.047 | ↑13d | PV | +21.3% | 62.97/62.97 | +4.04% | 20% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>📶W9 · W↑13d · 🚀SS · ★ · ↑CMF12d</sub> | ✓ SAFE | Electric scooters, batteries, charging infrastructure, premium segment | ⚡ BULL_ANY_PPV | 5 | ↑99 | ↑1.090 | ↑15d | PV | +30.9% | 65.09/63.65 | +7.87% | 20% |
| [RATEGAIN](https://in.tradingview.com/chart/?symbol=NSE:RATEGAIN)<br><sub>📶W9 · W↑71d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | Travel SaaS platform, revenue management, global hotels | ⚡ BULL_ANY_PPV | 0 | ↑96 | ↑1.041 | ↑60d+ | PV | +70.2% | 62.96/62.15 | +2.62% | 20% |
| [5PAISA](https://in.tradingview.com/chart/?symbol=NSE:5PAISA)<br><sub>📶W9 · W↑23d · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Digital discount brokerage platform for equity derivatives commodity trading | ⚡ BULL_ANY_PPV | 0 | ↑65 | ↑1.044 | ↑23d | PV | +26.2% | 52.5/47.37 | +1.53% | 20% |
| [AIAENG](https://in.tradingview.com/chart/?symbol=NSE:AIAENG)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | High-chromium grinding media and liners for cement mining | 📈 BULL_ANY_MID | 99 | 🔄83 | ↑1.014 | ↑1d | SQ | +1.4% | 13.28/10.17 | +1.44% | 20% |
| [LLOYDSME](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSME)<br><sub>📶W9 · 🚀SS · ↓CMF14d</sub> | ✓ SAFE | Iron ore mining, sponge iron production, power generation | 📈 BULL_ANY_MID | 94 | 🔄78 | ↑1.022 | ↑1d | SQ | +3.1% | 6.52/1.69 | +3.12% | 20% |
| [METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS)<br><sub>📶W9 · W↑66d · 🚀SS · ↓CMF20d</sub> | ⚠ CAUTION | Diagnostic pathology labs clinical testing centers urban India | 📈 BULL_ANY_MID | 90 | 🔄73 | ↑1.020 | ↑5d | SQ | +4.1% | 49.73/46.67 | +2.23% | 20% |
| [VISHNU](https://in.tradingview.com/chart/?symbol=NSE:VISHNU)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Chromium Barium chemicals manufacturer serving industrial applications | 📈 BULL_ANY_MID | 63 | ↑72 | ↑1.027 | ↑2d | SQ | +4.0% | 6.97/-0.97 | +2.20% | 20% |
| [POLYMED](https://in.tradingview.com/chart/?symbol=NSE:POLYMED)<br><sub>📶W9 · W↑23d · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Plastic medical disposables manufacturer exporting surgical devices globally | 📈 BULL_ANY_MID | 60 | ↑43 | ↑1.029 | ↑5d | SQ | +6.3% | 31.78/29.2 | +3.08% | 20% |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS)<br><sub>📶W9 · W↑71d · ↓CMF16d</sub> | ✓ SAFE | Generic pharmaceutical formulations for regulated global markets | 📈 BULL_ANY_MID | 59 | ↑91 | ↑1.025 | ↑6d | SQ | +5.6% | 56.58/54.94 | +1.77% | 20% |
| [BLUSPRING](https://in.tradingview.com/chart/?symbol=NSE:BLUSPRING)<br><sub>📶W9 · W↑78d · ↓CMF0d</sub> | ✓ SAFE | I don't have specific information about Bluspring Enterprises Ltd's operations | 📈 BULL_ANY_MID | 56 | ↑95 | ↑1.034 | ↑4d | SQ | +9.4% | 38.04/37.1 | +3.10% | 10% 🟨 |
| [HONAUT](https://in.tradingview.com/chart/?symbol=NSE:HONAUT)<br><sub>📶W9 · W↑66d · 🚀SS · ↓CMF19d</sub> | ⚠ CAUTION | Industrial automation controls systems manufacturing | 📈 BULL_ANY_MID | 54 | 🔄66 | ↑1.026 | ↑1d | — | +3.9% | 17.63/17.0 | +3.89% | 20% |
| [INNOVACAP](https://in.tradingview.com/chart/?symbol=NSE:INNOVACAP)<br><sub>📶W9 · W↑88d · ★ · ↓CMF11d</sub> | ✓ SAFE | Tablet manufacturing pharmaceuticals India generic drugs | 📈 BULL_ANY_MID | 53 | ↑81 | ↓1.009 | ↑7d | SQ | +3.9% | 59.76/59.25 | -0.21% | 20% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Specialty chemicals manufacturer serving pharmaceutical intermediates globally | 📈 BULL_ANY_MID | 52 | 🔄99 | ↑1.021 | ↑3d | — | +4.3% | 37.38/36.79 | +2.52% | 20% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄91 | ↑1.037 | ↑1d | — | +3.4% | -7.35/-13.15 | +3.43% | 20% |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH)<br><sub>📶W9 · W↑66d · 🚀SS · ↓CMF10d</sub> | ✓ SAFE | Precision aerospace components and tooling manufacturer | 📈 BULL_ANY_MID | 48 | ↑76 | ↓1.020 | ↑12d | SQ | +10.6% | 47.13/44.37 | +0.34% | 10% 🟩 |
| [SHREECEM](https://in.tradingview.com/chart/?symbol=NSE:SHREECEM)<br><sub>📶W9 · W↑23d · 🚀SS · ↓CMF5d</sub> | ⚠ CAUTION | Cement manufacturing, building materials, construction sector | 📈 BULL_ANY_MID | 35 | 🔄38 | ↑1.022 | ↑23d | — | +11.4% | 44.14/43.8 | +2.45% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑63d · ↑CMF16d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.020 | ↑3d | — | +5.4% | 47.71/46.67 | -0.44% | 20% |
| [BAJAJHCARE](https://in.tradingview.com/chart/?symbol=NSE:BAJAJHCARE)<br><sub>📶W9 · W↑23d · ↑CMF12d</sub> | ✓ SAFE | APIs and formulations manufacturer for global pharma markets | 📈 BULL_ANY_MID | 7 | ↑23 | ↑1.054 | ↑13d | — | +19.6% | 51.44/48.0 | +4.60% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Banking software solutions for financial institutions | 📈 BULL_ANY_MID | 5 | ↑90 | ↑1.055 | ↑15d | — | +20.9% | 50.17/48.27 | +4.64% | 20% |
| [WELENT](https://in.tradingview.com/chart/?symbol=NSE:WELENT)<br><sub>📶W9 · W↑66d · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Infrastructure developer: highways, water systems, oil pipelines | 📈 BULL_ANY_MID | 5 | ↑80 | ↑1.025 | ↑37d | — | +25.0% | 63.31/62.78 | +1.16% | 20% |
| [JLHL](https://in.tradingview.com/chart/?symbol=NSE:JLHL)<br><sub>📶W9 · W↑66d · 🚀SS · ↑CMF11d</sub> | ⚠ CAUTION | Multi-specialty hospital chain serving Mumbai and western India | 📈 BULL_ANY_MID | 5 | ↑60 | ↑1.027 | ↑23d | — | +14.0% | 67.67/66.56 | +1.10% | 20% |
| [MADRASFERT](https://in.tradingview.com/chart/?symbol=NSE:MADRASFERT)<br><sub>W↑3d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 94 | 🔄20 | ↑1.024 | ↑1d | SQ·PV | +4.4% | -18.24/-22.93 | +4.37% | 20% |
| [KEC](https://in.tradingview.com/chart/?symbol=NSE:KEC)<br><sub>🚀SS · ↓CMF12d</sub> | ✓ SAFE | Power transmission EPC, railways, infrastructure projects globally | ⚡ BULL_ANY_PPV | 59 | 🔄3 | ↑1.009 | ↑1d | PV | +3.6% | -28.35/-29.9 | +3.59% | 20% |
| [JKLAKSHMI](https://in.tradingview.com/chart/?symbol=NSE:JKLAKSHMI)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Cement manufacturer serving construction infrastructure projects India | ⚡ BULL_ANY_PPV | 59 | 🔄4 | ↑1.011 | ↑1d | PV | +3.1% | -51.81/-57.49 | +3.12% | 20% |
| [TRITURBINE](https://in.tradingview.com/chart/?symbol=NSE:TRITURBINE)<br><sub>🚀SS · ↑CMF0d</sub> | ✓ SAFE | Steam turbines for industrial power generation under 100MW | ⚡ BULL_ANY_PPV | 47 | 🔄73 | ↑1.011 | ↓13d | PV | -4.5% | -45.51/-47.0 | +5.20% | 20% |
| [POLICYBZR](https://in.tradingview.com/chart/?symbol=NSE:POLICYBZR)<br><sub>🚀SS · ↑CMF10d</sub> | ✓ SAFE | Insurance and lending digital marketplace aggregator | 📈 BULL_ANY_MID | 99 | 🔄32 | ↑1.009 | ↑1d | SQ | +2.8% | -13.63/-14.34 | +2.80% | 20% |
| [KPIGREEN](https://in.tradingview.com/chart/?symbol=NSE:KPIGREEN)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Solar wind hybrid power generation utility scale projects | 📈 BULL_ANY_MID | 99 | 🔄18 | ↑1.008 | ↑1d | SQ | +1.4% | -9.88/-15.77 | +1.38% | 20% |
| [IGIL](https://in.tradingview.com/chart/?symbol=NSE:IGIL)<br><sub>🚀SS · ↓CMF19d</sub> | ✓ SAFE | Diamond gemstone jewelry certification grading laboratory services | 📈 BULL_ANY_MID | 99 | 🔄41 | ↑1.012 | ↑1d | SQ | +2.8% | -37.62/-41.79 | +2.75% | 20% |
| [FIEMIND](https://in.tradingview.com/chart/?symbol=NSE:FIEMIND)<br><sub>↓CMF10d</sub> | ⚠ CAUTION | Automotive lighting and mirrors for vehicle manufacturers | 📈 BULL_ANY_MID | 99 | 🔄56 | ↑1.010 | ↑1d | SQ | +2.0% | -28.95/-33.8 | +2.00% | 20% |
| [BALMLAWRIE](https://in.tradingview.com/chart/?symbol=NSE:BALMLAWRIE)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Industrial oils lubricants specialty chemicals trading logistics | 📈 BULL_ANY_MID | 99 | 🔄36 | ↑1.007 | ↑1d | SQ | +2.2% | -20.09/-21.93 | +2.19% | 20% |
| [ANDHRAPAP](https://in.tradingview.com/chart/?symbol=NSE:ANDHRAPAP)<br><sub>🚀SS · ↓CMF8d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄17 | ↑1.007 | ↑1d | SQ | +1.5% | -26.41/-31.0 | +1.53% | 20% |
| [AUTOAXLES](https://in.tradingview.com/chart/?symbol=NSE:AUTOAXLES)<br><sub>W↑18d · 🚀SS · ↓CMF3d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄41 | ↑1.018 | ↑1d | SQ | +2.4% | 15.82/10.91 | +2.42% | 20% |
| [UBL](https://in.tradingview.com/chart/?symbol=NSE:UBL)<br><sub>W↑23d · 🚀SS · ↓CMF11d</sub> | ⚠ CAUTION | Beer manufacturer, India, consumer discretionary beverages | 📈 BULL_ANY_MID | 68 | ↑11 | ↑1.010 | ↑2d | SQ | +1.7% | 8.07/3.17 | +0.64% | 20% |
| [GANDHITUBE](https://in.tradingview.com/chart/?symbol=NSE:GANDHITUBE)<br><sub>W↑8d · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 67 | ↑53 | ↑1.010 | ↑3d | SQ | +1.9% | 34.45/28.38 | +0.54% | 20% |
| [ICICIGI](https://in.tradingview.com/chart/?symbol=NSE:ICICIGI)<br><sub>W↑23d · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION | General insurance motor health property casualty India | 📈 BULL_ANY_MID | 59 | 🔄31 | ↑1.010 | ↑1d | — | +1.5% | 5.63/5.1 | +1.48% | 20% |
| [GMDCLTD](https://in.tradingview.com/chart/?symbol=NSE:GMDCLTD)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Lignite mining and power generation Gujarat state | 📈 BULL_ANY_MID | 59 | 🔄50 | ↑1.007 | ↑1d | — | +1.7% | -32.43/-36.04 | +1.72% | 20% |
| [PNB](https://in.tradingview.com/chart/?symbol=NSE:PNB)<br><sub>W↑25d · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | 🔄25 | ↑1.012 | ↑2d | — | +2.9% | -19.58/-24.31 | +0.94% | 20% |
| [UNIONBANK](https://in.tradingview.com/chart/?symbol=NSE:UNIONBANK)<br><sub>↑CMF1d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄50 | ↑1.036 | ↑1d | — | +3.7% | -21.82/-27.26 | +3.73% | 20% |
| [GOCOLORS](https://in.tradingview.com/chart/?symbol=NSE:GOCOLORS)<br><sub>↓CMF18d</sub> | ✓ SAFE | Women's bottom-wear retail, branded leggings and trousers | 📈 BULL_ANY_MID | 37 | 🔄13 | ↑1.015 | ↓18d | — | +0.3% | -20.46/-22.0 | +3.57% | 20% |

```
NSE:VIMTALABS,NSE:ENDURANCE,NSE:JUBLPHARMA,NSE:RACLGEAR,NSE:FLUOROCHEM,NSE:HIRECT,NSE:HEIDELBERG,NSE:WOCKPHARMA,NSE:GABRIEL,NSE:GHCLTEXTIL,NSE:ATHERENERG,NSE:RATEGAIN,NSE:5PAISA,NSE:AIAENG,NSE:LLOYDSME,NSE:METROPOLIS,NSE:VISHNU,NSE:POLYMED,NSE:MARKSANS,NSE:BLUSPRING,NSE:HONAUT,NSE:INNOVACAP,NSE:ACUTAAS,NSE:BHEL,NSE:UNIMECH,NSE:SHREECEM,NSE:ABCAPITAL,NSE:BAJAJHCARE,NSE:OFSS,NSE:WELENT,NSE:JLHL,NSE:MADRASFERT,NSE:KEC,NSE:JKLAKSHMI,NSE:TRITURBINE,NSE:POLICYBZR,NSE:KPIGREEN,NSE:IGIL,NSE:FIEMIND,NSE:BALMLAWRIE,NSE:ANDHRAPAP,NSE:AUTOAXLES,NSE:UBL,NSE:GANDHITUBE,NSE:ICICIGI,NSE:GMDCLTD,NSE:PNB,NSE:UNIONBANK,NSE:GOCOLORS
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (29)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [VIMTALABS](https://in.tradingview.com/chart/?symbol=NSE:VIMTALABS)<br><sub>📶W9 · W↑71d · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Contract testing and research services for pharma and chemicals | ⚡ BULL_ANY_PPV | 94 | 🔄60 | ↑1.016 | ↑1d | SQ·PV | +3.6% | 6.0/5.57 | +3.56% | 20% |
| [ENDURANCE](https://in.tradingview.com/chart/?symbol=NSE:ENDURANCE)<br><sub>📶W9 · W↑66d · ↑CMF1d</sub> | ✓ SAFE | Aluminum castings, suspension, braking systems for automakers | ⚡ BULL_ANY_PPV | 88 | 🔄56 | ↑1.022 | ↑7d | SQ·PV | +3.7% | 31.96/27.7 | +2.43% | 20% |
| [JUBLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:JUBLPHARMA)<br><sub>📶W9 · W↑78d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Radiopharmaceuticals, allergy immunotherapy, pharma contract manufacturing | ⚡ BULL_ANY_PPV | 87 | 🔄44 | ↑1.047 | ↑3d | SQ·PV | +6.7% | 20.19/1.77 | +5.54% | 20% |
| [RACLGEAR](https://in.tradingview.com/chart/?symbol=NSE:RACLGEAR)<br><sub>📶W9 · W↑18d · ↓CMF22d</sub> | ✓ SAFE | Automotive gears and precision components for global OEMs | ⚡ BULL_ANY_PPV | 63 | ↑70 | ↑1.025 | ↑2d | SQ·PV | +4.2% | -1.59/-8.47 | +1.93% | 20% 🟦 |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>📶W9 · W↑71d · ↑CMF30d</sub> | ✓ SAFE | PTFE fluorochemicals manufacturer specialty chemicals sector | ⚡ BULL_ANY_PPV | 56 | ↑74 | ↑1.046 | ↑4d | SQ·PV | +6.9% | 43.25/33.45 | +5.29% | 20% |
| [AIAENG](https://in.tradingview.com/chart/?symbol=NSE:AIAENG)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | High-chromium grinding media and liners for cement mining | 📈 BULL_ANY_MID | 99 | 🔄83 | ↑1.014 | ↑1d | SQ | +1.4% | 13.28/10.17 | +1.44% | 20% |
| [LLOYDSME](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSME)<br><sub>📶W9 · 🚀SS · ↓CMF14d</sub> | ✓ SAFE | Iron ore mining, sponge iron production, power generation | 📈 BULL_ANY_MID | 94 | 🔄78 | ↑1.022 | ↑1d | SQ | +3.1% | 6.52/1.69 | +3.12% | 20% |
| [METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS)<br><sub>📶W9 · W↑66d · 🚀SS · ↓CMF20d</sub> | ⚠ CAUTION | Diagnostic pathology labs clinical testing centers urban India | 📈 BULL_ANY_MID | 90 | 🔄73 | ↑1.020 | ↑5d | SQ | +4.1% | 49.73/46.67 | +2.23% | 20% |
| [VISHNU](https://in.tradingview.com/chart/?symbol=NSE:VISHNU)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Chromium Barium chemicals manufacturer serving industrial applications | 📈 BULL_ANY_MID | 63 | ↑72 | ↑1.027 | ↑2d | SQ | +4.0% | 6.97/-0.97 | +2.20% | 20% |
| [POLYMED](https://in.tradingview.com/chart/?symbol=NSE:POLYMED)<br><sub>📶W9 · W↑23d · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Plastic medical disposables manufacturer exporting surgical devices globally | 📈 BULL_ANY_MID | 60 | ↑43 | ↑1.029 | ↑5d | SQ | +6.3% | 31.78/29.2 | +3.08% | 20% |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS)<br><sub>📶W9 · W↑71d · ↓CMF16d</sub> | ✓ SAFE | Generic pharmaceutical formulations for regulated global markets | 📈 BULL_ANY_MID | 59 | ↑91 | ↑1.025 | ↑6d | SQ | +5.6% | 56.58/54.94 | +1.77% | 20% |
| [BLUSPRING](https://in.tradingview.com/chart/?symbol=NSE:BLUSPRING)<br><sub>📶W9 · W↑78d · ↓CMF0d</sub> | ✓ SAFE | I don't have specific information about Bluspring Enterprises Ltd's operations | 📈 BULL_ANY_MID | 56 | ↑95 | ↑1.034 | ↑4d | SQ | +9.4% | 38.04/37.1 | +3.10% | 10% 🟨 |
| [INNOVACAP](https://in.tradingview.com/chart/?symbol=NSE:INNOVACAP)<br><sub>📶W9 · W↑88d · ★ · ↓CMF11d</sub> | ✓ SAFE | Tablet manufacturing pharmaceuticals India generic drugs | 📈 BULL_ANY_MID | 53 | ↑81 | ↓1.009 | ↑7d | SQ | +3.9% | 59.76/59.25 | -0.21% | 20% |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH)<br><sub>📶W9 · W↑66d · 🚀SS · ↓CMF10d</sub> | ✓ SAFE | Precision aerospace components and tooling manufacturer | 📈 BULL_ANY_MID | 48 | ↑76 | ↓1.020 | ↑12d | SQ | +10.6% | 47.13/44.37 | +0.34% | 10% 🟩 |
| [MADRASFERT](https://in.tradingview.com/chart/?symbol=NSE:MADRASFERT)<br><sub>W↑3d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 94 | 🔄20 | ↑1.024 | ↑1d | SQ·PV | +4.4% | -18.24/-22.93 | +4.37% | 20% |
| [POLICYBZR](https://in.tradingview.com/chart/?symbol=NSE:POLICYBZR)<br><sub>🚀SS · ↑CMF10d</sub> | ✓ SAFE | Insurance and lending digital marketplace aggregator | 📈 BULL_ANY_MID | 99 | 🔄32 | ↑1.009 | ↑1d | SQ | +2.8% | -13.63/-14.34 | +2.80% | 20% |
| [KPIGREEN](https://in.tradingview.com/chart/?symbol=NSE:KPIGREEN)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Solar wind hybrid power generation utility scale projects | 📈 BULL_ANY_MID | 99 | 🔄18 | ↑1.008 | ↑1d | SQ | +1.4% | -9.88/-15.77 | +1.38% | 20% |
| [IGIL](https://in.tradingview.com/chart/?symbol=NSE:IGIL)<br><sub>🚀SS · ↓CMF19d</sub> | ✓ SAFE | Diamond gemstone jewelry certification grading laboratory services | 📈 BULL_ANY_MID | 99 | 🔄41 | ↑1.012 | ↑1d | SQ | +2.8% | -37.62/-41.79 | +2.75% | 20% |
| [FIEMIND](https://in.tradingview.com/chart/?symbol=NSE:FIEMIND)<br><sub>↓CMF10d</sub> | ⚠ CAUTION | Automotive lighting and mirrors for vehicle manufacturers | 📈 BULL_ANY_MID | 99 | 🔄56 | ↑1.010 | ↑1d | SQ | +2.0% | -28.95/-33.8 | +2.00% | 20% |
| [BALMLAWRIE](https://in.tradingview.com/chart/?symbol=NSE:BALMLAWRIE)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Industrial oils lubricants specialty chemicals trading logistics | 📈 BULL_ANY_MID | 99 | 🔄36 | ↑1.007 | ↑1d | SQ | +2.2% | -20.09/-21.93 | +2.19% | 20% |
| [ANDHRAPAP](https://in.tradingview.com/chart/?symbol=NSE:ANDHRAPAP)<br><sub>🚀SS · ↓CMF8d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄17 | ↑1.007 | ↑1d | SQ | +1.5% | -26.41/-31.0 | +1.53% | 20% |
| [AUTOAXLES](https://in.tradingview.com/chart/?symbol=NSE:AUTOAXLES)<br><sub>W↑18d · 🚀SS · ↓CMF3d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄41 | ↑1.018 | ↑1d | SQ | +2.4% | 15.82/10.91 | +2.42% | 20% |
| [UBL](https://in.tradingview.com/chart/?symbol=NSE:UBL)<br><sub>W↑23d · 🚀SS · ↓CMF11d</sub> | ⚠ CAUTION | Beer manufacturer, India, consumer discretionary beverages | 📈 BULL_ANY_MID | 68 | ↑11 | ↑1.010 | ↑2d | SQ | +1.7% | 8.07/3.17 | +0.64% | 20% |
| [GANDHITUBE](https://in.tradingview.com/chart/?symbol=NSE:GANDHITUBE)<br><sub>W↑8d · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 67 | ↑53 | ↑1.010 | ↑3d | SQ | +1.9% | 34.45/28.38 | +0.54% | 20% |
| [ORIENTCEM](https://in.tradingview.com/chart/?symbol=NSE:ORIENTCEM)<br><sub>W↑13d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Cement manufacturing and distribution for construction sector | 📈 BULL_ANY_MID | 66 | ↓6 | ↑1.004 | ↑4d | SQ | +1.3% | 9.45/9.04 | +0.67% | 20% |
| [AMBUJACEM](https://in.tradingview.com/chart/?symbol=NSE:AMBUJACEM)<br><sub>W↑15d · ↑CMF5d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↓10 | ↓1.004 | ↑3d | SQ | +2.7% | 15.62/14.01 | -0.88% | 20% |
| [ALICON](https://in.tradingview.com/chart/?symbol=NSE:ALICON)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 53 | ↓10 | ↓0.995 | ↓7d | SQ | -1.7% | -41.78/-43.24 | -0.52% | 20% |
| [SEAMECLTD](https://in.tradingview.com/chart/?symbol=NSE:SEAMECLTD)<br><sub>↑CMF0d · ⚠️TRAP</sub> | ✓ SAFE | Offshore drilling equipment rental and marine services | 📈 BULL_ANY_MID | 50 | ↓82 | ↑0.996 | ↓15d | SQ | -1.2% | -20.44/-22.73 | +0.23% | 20% |
| [IGPL](https://in.tradingview.com/chart/?symbol=NSE:IGPL)<br><sub>↓CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 44 | ↓49 | ↓1.000 | ↓16d | SQ | -1.4% | -11.1/-11.42 | -0.29% | 20% |

```
NSE:VIMTALABS,NSE:ENDURANCE,NSE:JUBLPHARMA,NSE:RACLGEAR,NSE:FLUOROCHEM,NSE:AIAENG,NSE:LLOYDSME,NSE:METROPOLIS,NSE:VISHNU,NSE:POLYMED,NSE:MARKSANS,NSE:BLUSPRING,NSE:INNOVACAP,NSE:UNIMECH,NSE:MADRASFERT,NSE:POLICYBZR,NSE:KPIGREEN,NSE:IGIL,NSE:FIEMIND,NSE:BALMLAWRIE,NSE:ANDHRAPAP,NSE:AUTOAXLES,NSE:UBL,NSE:GANDHITUBE,NSE:ORIENTCEM,NSE:AMBUJACEM,NSE:ALICON,NSE:SEAMECLTD,NSE:IGPL
```

---

### 🔥 MAJOR — PPV confirmed (11)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [HIRECT](https://in.tradingview.com/chart/?symbol=NSE:HIRECT)<br><sub>📶W9 · RVOL15x · ↑CMF0d</sub> | ✓ SAFE | Power electronics converters rectifiers railway locomotive traction systems | ⚡ BULL_ANY_PPV | 49 | 🔄95 | ↑1.148 | ↑1d | PV | +19.9% | -16.3/-28.41 | +19.88% | 20% |
| [HEIDELBERG](https://in.tradingview.com/chart/?symbol=NSE:HEIDELBERG)<br><sub>📶W9 · W↑13d · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 45 | 🔄25 | ↑1.026 | ↑10d | PV | +6.2% | 44.05/39.51 | +2.88% | 20% |
| [WOCKPHARMA](https://in.tradingview.com/chart/?symbol=NSE:WOCKPHARMA)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Pharma manufacturing: injectables, orals, topicals, biopharmaceuticals globally | ⚡ BULL_ANY_PPV | 40 | 🔄82 | ↑1.008 | ↓25d | PV | +3.1% | -36.88/-39.15 | +2.13% | 20% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>📶W9 · W↑23d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Shock absorbers struts two wheeler four wheeler OEM aftermarket | ⚡ BULL_ANY_PPV | 30 | 🔄81 | ↑1.069 | ↑23d | PV | +30.2% | 46.15/38.84 | +8.48% | 20% |
| [GHCLTEXTIL](https://in.tradingview.com/chart/?symbol=NSE:GHCLTEXTIL)<br><sub>📶W9 · W↑13d · ★ · ↑CMF9d</sub> | ✓ SAFE | Bleached fabric and specialty chemicals textile manufacturer | ⚡ BULL_ANY_PPV | 7 | ↑86 | ↑1.047 | ↑13d | PV | +21.3% | 62.97/62.97 | +4.04% | 20% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>📶W9 · W↑13d · 🚀SS · ★ · ↑CMF12d</sub> | ✓ SAFE | Electric scooters, batteries, charging infrastructure, premium segment | ⚡ BULL_ANY_PPV | 5 | ↑99 | ↑1.090 | ↑15d | PV | +30.9% | 65.09/63.65 | +7.87% | 20% |
| [RATEGAIN](https://in.tradingview.com/chart/?symbol=NSE:RATEGAIN)<br><sub>📶W9 · W↑71d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | Travel SaaS platform, revenue management, global hotels | ⚡ BULL_ANY_PPV | 0 | ↑96 | ↑1.041 | ↑60d+ | PV | +70.2% | 62.96/62.15 | +2.62% | 20% |
| [5PAISA](https://in.tradingview.com/chart/?symbol=NSE:5PAISA)<br><sub>📶W9 · W↑23d · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Digital discount brokerage platform for equity derivatives commodity trading | ⚡ BULL_ANY_PPV | 0 | ↑65 | ↑1.044 | ↑23d | PV | +26.2% | 52.5/47.37 | +1.53% | 20% |
| [KEC](https://in.tradingview.com/chart/?symbol=NSE:KEC)<br><sub>🚀SS · ↓CMF12d</sub> | ✓ SAFE | Power transmission EPC, railways, infrastructure projects globally | ⚡ BULL_ANY_PPV | 59 | 🔄3 | ↑1.009 | ↑1d | PV | +3.6% | -28.35/-29.9 | +3.59% | 20% |
| [JKLAKSHMI](https://in.tradingview.com/chart/?symbol=NSE:JKLAKSHMI)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Cement manufacturer serving construction infrastructure projects India | ⚡ BULL_ANY_PPV | 59 | 🔄4 | ↑1.011 | ↑1d | PV | +3.1% | -51.81/-57.49 | +3.12% | 20% |
| [TRITURBINE](https://in.tradingview.com/chart/?symbol=NSE:TRITURBINE)<br><sub>🚀SS · ↑CMF0d</sub> | ✓ SAFE | Steam turbines for industrial power generation under 100MW | ⚡ BULL_ANY_PPV | 47 | 🔄73 | ↑1.011 | ↓13d | PV | -4.5% | -45.51/-47.0 | +5.20% | 20% |

```
NSE:HIRECT,NSE:HEIDELBERG,NSE:WOCKPHARMA,NSE:GABRIEL,NSE:GHCLTEXTIL,NSE:ATHERENERG,NSE:RATEGAIN,NSE:5PAISA,NSE:KEC,NSE:JKLAKSHMI,NSE:TRITURBINE
```

### 🟢 OVERSOLD — reversal from −53/−60 (3)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SOLEX](https://in.tradingview.com/chart/?symbol=NSE:SOLEX)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Solar module manufacturing and EPC services provider | 🟡 BULL_OS_L2 | 13 | ↓5 | ↑0.975 | ↓12d | — | -9.7% | -57.06/-57.25 | -0.18% | 20% |
| [PRSMJOHNSN](https://in.tradingview.com/chart/?symbol=NSE:PRSMJOHNSN)<br><sub>🚀SS · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Cement tiles sanitaryware ready-mixed concrete construction materials | 🟡 BULL_OS_L2 | 7 | ↓9 | ↑0.989 | ↓18d | — | -5.8% | -58.39/-59.02 | +0.30% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>↓CMF9d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 5 | ↓52 | ↑0.994 | ↓30d | — | -5.9% | -54.87/-55.01 | +0.38% | 20% |

```
NSE:SOLEX,NSE:PRSMJOHNSN,NSE:COALINDIA
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (22)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [HONAUT](https://in.tradingview.com/chart/?symbol=NSE:HONAUT)<br><sub>📶W9 · W↑66d · 🚀SS · ↓CMF19d</sub> | ⚠ CAUTION | Industrial automation controls systems manufacturing | 📈 BULL_ANY_MID | 54 | 🔄66 | ↑1.026 | ↑1d | — | +3.9% | 17.63/17.0 | +3.89% | 20% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Specialty chemicals manufacturer serving pharmaceutical intermediates globally | 📈 BULL_ANY_MID | 52 | 🔄99 | ↑1.021 | ↑3d | — | +4.3% | 37.38/36.79 | +2.52% | 20% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄91 | ↑1.037 | ↑1d | — | +3.4% | -7.35/-13.15 | +3.43% | 20% |
| [SHREECEM](https://in.tradingview.com/chart/?symbol=NSE:SHREECEM)<br><sub>📶W9 · W↑23d · 🚀SS · ↓CMF5d</sub> | ⚠ CAUTION | Cement manufacturing, building materials, construction sector | 📈 BULL_ANY_MID | 35 | 🔄38 | ↑1.022 | ↑23d | — | +11.4% | 44.14/43.8 | +2.45% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑63d · ↑CMF16d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.020 | ↑3d | — | +5.4% | 47.71/46.67 | -0.44% | 20% |
| [BAJAJHCARE](https://in.tradingview.com/chart/?symbol=NSE:BAJAJHCARE)<br><sub>📶W9 · W↑23d · ↑CMF12d</sub> | ✓ SAFE | APIs and formulations manufacturer for global pharma markets | 📈 BULL_ANY_MID | 7 | ↑23 | ↑1.054 | ↑13d | — | +19.6% | 51.44/48.0 | +4.60% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Banking software solutions for financial institutions | 📈 BULL_ANY_MID | 5 | ↑90 | ↑1.055 | ↑15d | — | +20.9% | 50.17/48.27 | +4.64% | 20% |
| [WELENT](https://in.tradingview.com/chart/?symbol=NSE:WELENT)<br><sub>📶W9 · W↑66d · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Infrastructure developer: highways, water systems, oil pipelines | 📈 BULL_ANY_MID | 5 | ↑80 | ↑1.025 | ↑37d | — | +25.0% | 63.31/62.78 | +1.16% | 20% |
| [JLHL](https://in.tradingview.com/chart/?symbol=NSE:JLHL)<br><sub>📶W9 · W↑66d · 🚀SS · ↑CMF11d</sub> | ⚠ CAUTION | Multi-specialty hospital chain serving Mumbai and western India | 📈 BULL_ANY_MID | 5 | ↑60 | ↑1.027 | ↑23d | — | +14.0% | 67.67/66.56 | +1.10% | 20% |
| [ICICIGI](https://in.tradingview.com/chart/?symbol=NSE:ICICIGI)<br><sub>W↑23d · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION | General insurance motor health property casualty India | 📈 BULL_ANY_MID | 59 | 🔄31 | ↑1.010 | ↑1d | — | +1.5% | 5.63/5.1 | +1.48% | 20% |
| [GMDCLTD](https://in.tradingview.com/chart/?symbol=NSE:GMDCLTD)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Lignite mining and power generation Gujarat state | 📈 BULL_ANY_MID | 59 | 🔄50 | ↑1.007 | ↑1d | — | +1.7% | -32.43/-36.04 | +1.72% | 20% |
| [PNB](https://in.tradingview.com/chart/?symbol=NSE:PNB)<br><sub>W↑25d · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | 🔄25 | ↑1.012 | ↑2d | — | +2.9% | -19.58/-24.31 | +0.94% | 20% |
| [UNIONBANK](https://in.tradingview.com/chart/?symbol=NSE:UNIONBANK)<br><sub>↑CMF1d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄50 | ↑1.036 | ↑1d | — | +3.7% | -21.82/-27.26 | +3.73% | 20% |
| [GOCOLORS](https://in.tradingview.com/chart/?symbol=NSE:GOCOLORS)<br><sub>↓CMF18d</sub> | ✓ SAFE | Women's bottom-wear retail, branded leggings and trousers | 📈 BULL_ANY_MID | 37 | 🔄13 | ↑1.015 | ↓18d | — | +0.3% | -20.46/-22.0 | +3.57% | 20% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>W↑1d · ↓CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 29 | ↓8 | ↑1.008 | ↑1d | — | +1.0% | -31.34/-34.03 | +1.02% | 20% |
| [IRCON](https://in.tradingview.com/chart/?symbol=NSE:IRCON)<br><sub>↓CMF30d</sub> | ✓ SAFE | Railway infrastructure construction, government contracts focus | 📈 BULL_ANY_MID | 14 | ↓5 | ↑0.992 | ↓11d | — | -0.8% | -47.13/-48.12 | +0.69% | 20% |
| [TMPV](https://in.tradingview.com/chart/?symbol=NSE:TMPV)<br><sub>↓CMF17d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 10 | ↓16 | ↑1.001 | ↓21d | — | -8.6% | -43.02/-44.0 | +1.64% | 20% |
| [PIIND](https://in.tradingview.com/chart/?symbol=NSE:PIIND)<br><sub>🚀SS · ↓CMF6d · ÷DIV</sub> | ⚠ CAUTION | Agro-chemicals and custom synthesis manufacturing for global clients | 📈 BULL_ANY_MID | 10 | ↓5 | ↑1.005 | ↓24d | — | -6.5% | -47.87/-48.24 | +3.24% | 20% |
| [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT)<br><sub>↑CMF1d · ⚠️TRAP</sub> | ✓ SAFE | BPM services for customer support and back-office operations globally | 📈 BULL_ANY_MID | 9 | ↓52 | ↓0.989 | ↓11d | — | -3.1% | -37.4/-38.78 | -1.70% | 20% |
| [SCI](https://in.tradingview.com/chart/?symbol=NSE:SCI)<br><sub>↓CMF30d</sub> | ✓ SAFE | Cargo vessel operations, maritime transport, international-domestic routes | 📈 BULL_ANY_MID | 5 | ↓70 | ↑0.993 | ↓23d | — | -3.2% | -40.8/-42.02 | +0.86% | 20% |
| [ASTEC](https://in.tradingview.com/chart/?symbol=NSE:ASTEC)<br><sub>↓CMF22d · ⚠️TRAP</sub> | ✓ SAFE | Pharmaceutical APIs and active ingredients for global markets | 📈 BULL_ANY_MID | 5 | ↓25 | ↑0.984 | ↓22d | — | -10.5% | -44.84/-45.74 | +0.04% | 20% |
| [TEAMLEASE](https://in.tradingview.com/chart/?symbol=NSE:TEAMLEASE)<br><sub>W↑78d · 🚀SS · ↓CMF5d</sub> | ✓ SAFE | Staffing solutions and workforce management for Indian enterprises | 📈 BULL_ANY_MID | 5 | ↓29 | ↑0.999 | ↓60d+ | — | +13.2% | -9.5/-9.88 | +0.30% | 20% |

```
NSE:HONAUT,NSE:ACUTAAS,NSE:BHEL,NSE:SHREECEM,NSE:ABCAPITAL,NSE:BAJAJHCARE,NSE:OFSS,NSE:WELENT,NSE:JLHL,NSE:ICICIGI,NSE:GMDCLTD,NSE:PNB,NSE:UNIONBANK,NSE:GOCOLORS,NSE:HDFCLIFE,NSE:IRCON,NSE:TMPV,NSE:PIIND,NSE:ONEPOINT,NSE:SCI,NSE:ASTEC,NSE:TEAMLEASE
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
