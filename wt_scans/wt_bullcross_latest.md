> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-07-17
*Generated 2026-07-17 15:45 IST*

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

**Total bull crosses today: 55** · 21 inside active squeeze

```
NSE:SERVOTECH,NSE:FEDERALBNK,NSE:RESPONIND,NSE:AIIL,NSE:VAIBHAVGBL,NSE:PNCINFRA,NSE:EXIDEIND,NSE:MPSLTD,NSE:SONACOMS,NSE:LLOYDSME,NSE:KPRMILL,NSE:TIL,NSE:NITCO,NSE:SANOFI,NSE:MANKIND,NSE:AYMSYNTEX,NSE:BHEL,NSE:THEJO,NSE:AEGISLOG,NSE:ABCAPITAL,NSE:OFSS,NSE:FIVESTAR,NSE:AFCONS,NSE:CAMPUS,NSE:TIIL,NSE:COHANCE,NSE:BATAINDIA,NSE:LGHL,NSE:AGIIL,NSE:GOPAL,NSE:SARDAEN,NSE:KANSAINER,NSE:COALINDIA,NSE:SULA,NSE:SAGCEM,NSE:PASHUPATI,NSE:SHAILY,NSE:CREST,NSE:PNB,NSE:WAAREERTL,NSE:AMBUJACEM,NSE:SRM,NSE:TCI,NSE:EXCELINDUS,NSE:POWERINDIA,NSE:UNIONBANK,NSE:SHANTIGOLD,NSE:ENRIN,NSE:ELGIEQUIP,NSE:HDFCLIFE,NSE:WAAREEENER,NSE:INDOTHAI,NSE:KRISHANA,NSE:TMPV,NSE:BERGEPAINT
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (22)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SERVOTECH](https://in.tradingview.com/chart/?symbol=NSE:SERVOTECH)<br><sub>📶W9 · 🚀SS · ↓CMF16d</sub> | ✓ SAFE | EV chargers solar products power electronics manufacturing | ⚡ BULL_ANY_PPV | 94 | 🔄57 | ↑1.016 | ↑1d | SQ·PV | +3.0% | -25.81/-30.84 | +2.95% | 20% 🟦 |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>📶W9 · W↑35d · ↑CMF30d</sub> | ✓ SAFE | Retail corporate banking Kerala-rooted expanding national branch network | ⚡ BULL_ANY_PPV | 49 | 🔄89 | ↑1.052 | ↑1d | PV | +6.9% | 47.35/41.78 | +6.86% | 20% |
| [RESPONIND](https://in.tradingview.com/chart/?symbol=NSE:RESPONIND)<br><sub>📶W9 · W↑68d · RVOL78x · ↑CMF0d</sub> | ✓ SAFE | fasteners manufacturing automotive commercial vehicle suppliers | ⚡ BULL_ANY_PPV | 49 | 🔄79 | ↑1.114 | ↑1d | PV | +15.8% | 14.93/9.39 | +15.75% | 20% |
| [AIIL](https://in.tradingview.com/chart/?symbol=NSE:AIIL)<br><sub>📶W9 · W↑30d · RVOL11x · ↑CMF0d</sub> | ⚠ CAUTION | NBFC lending and securities investment portfolio management | ⚡ BULL_ANY_PPV | 18 | ↑55 | ↑1.088 | ↑2d | PV | +13.8% | -1.23/-17.41 | +9.88% | 20% |
| [VAIBHAVGBL](https://in.tradingview.com/chart/?symbol=NSE:VAIBHAVGBL)<br><sub>📶W9 · W↑68d · ↓CMF30d</sub> | ✓ SAFE | Fashion jewelry and gemstones direct-to-consumer retailer globally | ⚡ BULL_ANY_PPV | 11 | ↑72 | ↑1.043 | ↑9d | PV | +11.8% | 48.19/47.65 | +4.15% | 20% |
| [PNCINFRA](https://in.tradingview.com/chart/?symbol=NSE:PNCINFRA)<br><sub>📶W9 · W↑25d · ↑CMF19d</sub> | ✓ SAFE | Highways bridges airports water infrastructure construction | ⚡ BULL_ANY_PPV | 10 | ↑45 | ↑1.013 | ↑24d | PV | +18.9% | 50.64/50.44 | +0.50% | 20% |
| [EXIDEIND](https://in.tradingview.com/chart/?symbol=NSE:EXIDEIND)<br><sub>📶W9 · W↑73d · ↑CMF11d</sub> | ✓ SAFE | Lead-acid batteries automotive industrial backup power | ⚡ BULL_ANY_PPV | 6 | ↑78 | ↑1.035 | ↑14d | PV | +12.6% | 53.61/52.57 | +3.30% | 20% |
| [MPSLTD](https://in.tradingview.com/chart/?symbol=NSE:MPSLTD)<br><sub>📶W9 · W↑85d · ↓CMF8d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 5 | ↑52 | ↑1.043 | ↑15d | PV | +15.5% | 70.18/68.91 | +1.80% | 20% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>📶W9 · W↑20d · 🚀SS · ★ · ↑CMF11d</sub> | ✓ SAFE | Differential assemblies and gears for electric vehicles | ⚡ BULL_ANY_PPV | 0 | ↑89 | ↑1.048 | ↑24d | PV | +18.2% | 67.64/64.68 | +3.14% | 20% |
| [LLOYDSME](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSME)<br><sub>📶W9 · 🚀SS · ↓CMF14d</sub> | ✓ SAFE | Iron ore mining, sponge iron production, power generation | 📈 BULL_ANY_MID | 94 | 🔄79 | ↑1.022 | ↑1d | SQ | +3.1% | 6.52/1.69 | +3.12% | 20% |
| [KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL)<br><sub>📶W9 · ↓CMF1d · DEL54%</sub> | ✓ SAFE | Vertically integrated textile apparel manufacturer with sugar ethanol | 📈 BULL_ANY_MID | 80 | 🔄73 | ↑1.006 | ↓36d | SQ | +21.6% | 5.79/3.79 | +0.76% | 20% |
| [TIL](https://in.tradingview.com/chart/?symbol=NSE:TIL)<br><sub>📶W9 · W↑25d · ↓CMF2d</sub> | ✓ SAFE | Material handling equipment, cranes, construction machinery | 📈 BULL_ANY_MID | 67 | ↑16 | ↑1.014 | ↑3d | SQ | +3.9% | 26.52/25.38 | +0.36% | 20% |
| [NITCO](https://in.tradingview.com/chart/?symbol=NSE:NITCO)<br><sub>📶W9 · W↑85d · ↓CMF0d</sub> | ✓ SAFE | Tiles marble mosaic manufacturing building construction surfaces | 📈 BULL_ANY_MID | 58 | ↑60 | ↓1.019 | ↑2d | SQ | +6.4% | 8.23/4.66 | -1.30% | 20% |
| [SANOFI](https://in.tradingview.com/chart/?symbol=NSE:SANOFI)<br><sub>📶W9 · W↑30d · ↑CMF0d</sub> | ⚠ CAUTION | Diabetes insulin, cardiology drugs, CNS medications, Indian pharma | 📈 BULL_ANY_MID | 58 | ↑8 | ↓1.006 | ↑2d | SQ | +1.1% | 12.6/11.65 | +0.12% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>📶W9 · W↑65d · ↓CMF6d</sub> | ✓ SAFE | Pharma formulations acute chronic diseases consumer health | 📈 BULL_ANY_MID | 51 | ↑63 | ↑1.009 | ↑19d | SQ | +7.4% | 47.69/43.74 | +0.35% | 20% |
| [AYMSYNTEX](https://in.tradingview.com/chart/?symbol=NSE:AYMSYNTEX)<br><sub>📶W9 · W↑15d · ↓CMF30d</sub> | ✓ SAFE | Polyester nylon filament yarn manufacturer textile sector | 📈 BULL_ANY_MID | 50 | 🔄77 | ↑1.029 | ↑5d | — | +7.4% | 16.23/14.88 | +3.81% | 20% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄91 | ↑1.037 | ↑1d | — | +3.4% | -7.35/-13.15 | +3.43% | 20% |
| [THEJO](https://in.tradingview.com/chart/?symbol=NSE:THEJO)<br><sub>📶W9 · W↑25d · ↓CMF3d</sub> | ⚠ CAUTION | Bulk material handling, mining equipment, core sector infrastructure | 📈 BULL_ANY_MID | 40 | ↑42 | ↓1.002 | ↑25d | SQ | +21.8% | 30.08/29.79 | -1.17% | 20% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>📶W9 · W↑73d · 🚀SS · ↑CMF26d</sub> | ✓ SAFE | Bulk liquid terminals, oil gas chemical logistics India | 📈 BULL_ANY_MID | 17 | ↑97 | ↑1.050 | ↑3d | — | +10.4% | 52.46/51.4 | +3.98% | 10% 🟨 |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑63d · ↑CMF16d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 17 | ↑80 | ↓1.020 | ↑3d | — | +5.4% | 47.71/46.67 | -0.44% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Banking software solutions for financial institutions | 📈 BULL_ANY_MID | 5 | ↑90 | ↑1.055 | ↑15d | — | +20.9% | 50.17/48.27 | +4.64% | 20% |
| [FIVESTAR](https://in.tradingview.com/chart/?symbol=NSE:FIVESTAR)<br><sub>📶W9 · W↑25d · ↑CMF21d</sub> | ✓ SAFE | Secured business loans for micro-entrepreneurs and self-employed | 📈 BULL_ANY_MID | 5 | ↑47 | ↑1.025 | ↑25d | — | +27.0% | 47.2/47.0 | +0.96% | 20% |

```
NSE:SERVOTECH,NSE:FEDERALBNK,NSE:RESPONIND,NSE:AIIL,NSE:VAIBHAVGBL,NSE:PNCINFRA,NSE:EXIDEIND,NSE:MPSLTD,NSE:SONACOMS,NSE:LLOYDSME,NSE:KPRMILL,NSE:TIL,NSE:NITCO,NSE:SANOFI,NSE:MANKIND,NSE:AYMSYNTEX,NSE:BHEL,NSE:THEJO,NSE:AEGISLOG,NSE:ABCAPITAL,NSE:OFSS,NSE:FIVESTAR
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (36)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SERVOTECH](https://in.tradingview.com/chart/?symbol=NSE:SERVOTECH)<br><sub>📶W9 · 🚀SS · ↓CMF16d</sub> | ✓ SAFE | EV chargers solar products power electronics manufacturing | ⚡ BULL_ANY_PPV | 94 | 🔄57 | ↑1.016 | ↑1d | SQ·PV | +3.0% | -25.81/-30.84 | +2.95% | 20% 🟦 |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>📶W9 · W↑35d · ↑CMF30d</sub> | ✓ SAFE | Retail corporate banking Kerala-rooted expanding national branch network | ⚡ BULL_ANY_PPV | 49 | 🔄89 | ↑1.052 | ↑1d | PV | +6.9% | 47.35/41.78 | +6.86% | 20% |
| [RESPONIND](https://in.tradingview.com/chart/?symbol=NSE:RESPONIND)<br><sub>📶W9 · W↑68d · RVOL78x · ↑CMF0d</sub> | ✓ SAFE | fasteners manufacturing automotive commercial vehicle suppliers | ⚡ BULL_ANY_PPV | 49 | 🔄79 | ↑1.114 | ↑1d | PV | +15.8% | 14.93/9.39 | +15.75% | 20% |
| [AIIL](https://in.tradingview.com/chart/?symbol=NSE:AIIL)<br><sub>📶W9 · W↑30d · RVOL11x · ↑CMF0d</sub> | ⚠ CAUTION | NBFC lending and securities investment portfolio management | ⚡ BULL_ANY_PPV | 18 | ↑55 | ↑1.088 | ↑2d | PV | +13.8% | -1.23/-17.41 | +9.88% | 20% |
| [VAIBHAVGBL](https://in.tradingview.com/chart/?symbol=NSE:VAIBHAVGBL)<br><sub>📶W9 · W↑68d · ↓CMF30d</sub> | ✓ SAFE | Fashion jewelry and gemstones direct-to-consumer retailer globally | ⚡ BULL_ANY_PPV | 11 | ↑72 | ↑1.043 | ↑9d | PV | +11.8% | 48.19/47.65 | +4.15% | 20% |
| [PNCINFRA](https://in.tradingview.com/chart/?symbol=NSE:PNCINFRA)<br><sub>📶W9 · W↑25d · ↑CMF19d</sub> | ✓ SAFE | Highways bridges airports water infrastructure construction | ⚡ BULL_ANY_PPV | 10 | ↑45 | ↑1.013 | ↑24d | PV | +18.9% | 50.64/50.44 | +0.50% | 20% |
| [EXIDEIND](https://in.tradingview.com/chart/?symbol=NSE:EXIDEIND)<br><sub>📶W9 · W↑73d · ↑CMF11d</sub> | ✓ SAFE | Lead-acid batteries automotive industrial backup power | ⚡ BULL_ANY_PPV | 6 | ↑78 | ↑1.035 | ↑14d | PV | +12.6% | 53.61/52.57 | +3.30% | 20% |
| [MPSLTD](https://in.tradingview.com/chart/?symbol=NSE:MPSLTD)<br><sub>📶W9 · W↑85d · ↓CMF8d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 5 | ↑52 | ↑1.043 | ↑15d | PV | +15.5% | 70.18/68.91 | +1.80% | 20% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>📶W9 · W↑20d · 🚀SS · ★ · ↑CMF11d</sub> | ✓ SAFE | Differential assemblies and gears for electric vehicles | ⚡ BULL_ANY_PPV | 0 | ↑89 | ↑1.048 | ↑24d | PV | +18.2% | 67.64/64.68 | +3.14% | 20% |
| [LLOYDSME](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSME)<br><sub>📶W9 · 🚀SS · ↓CMF14d</sub> | ✓ SAFE | Iron ore mining, sponge iron production, power generation | 📈 BULL_ANY_MID | 94 | 🔄79 | ↑1.022 | ↑1d | SQ | +3.1% | 6.52/1.69 | +3.12% | 20% |
| [KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL)<br><sub>📶W9 · ↓CMF1d · DEL54%</sub> | ✓ SAFE | Vertically integrated textile apparel manufacturer with sugar ethanol | 📈 BULL_ANY_MID | 80 | 🔄73 | ↑1.006 | ↓36d | SQ | +21.6% | 5.79/3.79 | +0.76% | 20% |
| [TIL](https://in.tradingview.com/chart/?symbol=NSE:TIL)<br><sub>📶W9 · W↑25d · ↓CMF2d</sub> | ✓ SAFE | Material handling equipment, cranes, construction machinery | 📈 BULL_ANY_MID | 67 | ↑16 | ↑1.014 | ↑3d | SQ | +3.9% | 26.52/25.38 | +0.36% | 20% |
| [NITCO](https://in.tradingview.com/chart/?symbol=NSE:NITCO)<br><sub>📶W9 · W↑85d · ↓CMF0d</sub> | ✓ SAFE | Tiles marble mosaic manufacturing building construction surfaces | 📈 BULL_ANY_MID | 58 | ↑60 | ↓1.019 | ↑2d | SQ | +6.4% | 8.23/4.66 | -1.30% | 20% |
| [SANOFI](https://in.tradingview.com/chart/?symbol=NSE:SANOFI)<br><sub>📶W9 · W↑30d · ↑CMF0d</sub> | ⚠ CAUTION | Diabetes insulin, cardiology drugs, CNS medications, Indian pharma | 📈 BULL_ANY_MID | 58 | ↑8 | ↓1.006 | ↑2d | SQ | +1.1% | 12.6/11.65 | +0.12% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>📶W9 · W↑65d · ↓CMF6d</sub> | ✓ SAFE | Pharma formulations acute chronic diseases consumer health | 📈 BULL_ANY_MID | 51 | ↑63 | ↑1.009 | ↑19d | SQ | +7.4% | 47.69/43.74 | +0.35% | 20% |
| [AYMSYNTEX](https://in.tradingview.com/chart/?symbol=NSE:AYMSYNTEX)<br><sub>📶W9 · W↑15d · ↓CMF30d</sub> | ✓ SAFE | Polyester nylon filament yarn manufacturer textile sector | 📈 BULL_ANY_MID | 50 | 🔄77 | ↑1.029 | ↑5d | — | +7.4% | 16.23/14.88 | +3.81% | 20% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄91 | ↑1.037 | ↑1d | — | +3.4% | -7.35/-13.15 | +3.43% | 20% |
| [THEJO](https://in.tradingview.com/chart/?symbol=NSE:THEJO)<br><sub>📶W9 · W↑25d · ↓CMF3d</sub> | ⚠ CAUTION | Bulk material handling, mining equipment, core sector infrastructure | 📈 BULL_ANY_MID | 40 | ↑42 | ↓1.002 | ↑25d | SQ | +21.8% | 30.08/29.79 | -1.17% | 20% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>📶W9 · W↑73d · 🚀SS · ↑CMF26d</sub> | ✓ SAFE | Bulk liquid terminals, oil gas chemical logistics India | 📈 BULL_ANY_MID | 17 | ↑97 | ↑1.050 | ↑3d | — | +10.4% | 52.46/51.4 | +3.98% | 10% 🟨 |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑63d · ↑CMF16d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 17 | ↑80 | ↓1.020 | ↑3d | — | +5.4% | 47.71/46.67 | -0.44% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Banking software solutions for financial institutions | 📈 BULL_ANY_MID | 5 | ↑90 | ↑1.055 | ↑15d | — | +20.9% | 50.17/48.27 | +4.64% | 20% |
| [FIVESTAR](https://in.tradingview.com/chart/?symbol=NSE:FIVESTAR)<br><sub>📶W9 · W↑25d · ↑CMF21d</sub> | ✓ SAFE | Secured business loans for micro-entrepreneurs and self-employed | 📈 BULL_ANY_MID | 5 | ↑47 | ↑1.025 | ↑25d | — | +27.0% | 47.2/47.0 | +0.96% | 20% |
| [AFCONS](https://in.tradingview.com/chart/?symbol=NSE:AFCONS)<br><sub>RVOL75x · ↑CMF0d · 🎯SLING</sub> | ✓ SAFE | Heavy infrastructure EPC contractor offshore pipeline marine | 🔥 BULL_OS_PPV | 43 | 🔄7 | ↑1.003 | ↓17d | PV | -4.3% | -64.37/-66.37 | +5.03% | 20% |
| [CAMPUS](https://in.tradingview.com/chart/?symbol=NSE:CAMPUS)<br><sub>RVOL185x · ↓CMF1d</sub> | ✓ SAFE | Sportswear and casual apparel manufacturer for mass market | ⚡ BULL_ANY_PPV | 94 | 🔄20 | ↑1.024 | ↑1d | SQ·PV | +4.1% | -38.43/-51.18 | +4.11% | 20% |
| [TIIL](https://in.tradingview.com/chart/?symbol=NSE:TIIL)<br><sub>↑CMF15d</sub> | ⚠ CAUTION | Drum closures, scaffolding systems, textiles manufacturing | ⚡ BULL_ANY_PPV | 94 | 🔄50 | ↑1.015 | ↑1d | SQ·PV | +3.4% | -23.29/-27.77 | +3.44% | 20% |
| [BATAINDIA](https://in.tradingview.com/chart/?symbol=NSE:BATAINDIA)<br><sub>↓CMF1d</sub> | ✓ SAFE | Footwear manufacturing and retail for Indian mass market consumers | ⚡ BULL_ANY_PPV | 59 | 🔄4 | ↑1.010 | ↑1d | PV | +2.1% | -23.55/-23.64 | +2.08% | 20% |
| [SARDAEN](https://in.tradingview.com/chart/?symbol=NSE:SARDAEN)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Steel ferroalloys iron ore pellets power producer | 🟡 BULL_OS_L2 | 40 | 🔄37 | ↑1.002 | ↓20d | — | -4.6% | -51.72/-54.31 | +1.10% | 20% |
| [SAGCEM](https://in.tradingview.com/chart/?symbol=NSE:SAGCEM)<br><sub>W↑15d · ↑CMF7d</sub> | ⚠ CAUTION | Cement manufacturing, South and Central India construction | 📈 BULL_ANY_MID | 99 | 🔄18 | ↑1.014 | ↑1d | SQ | +2.4% | 13.72/11.08 | +2.37% | 20% |
| [PASHUPATI](https://in.tradingview.com/chart/?symbol=NSE:PASHUPATI)<br><sub>↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄74 | ↑1.009 | ↑1d | SQ | +1.6% | -15.3/-16.96 | +1.58% | 20% |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY)<br><sub>↓CMF21d</sub> | ✓ SAFE | Precision injection molded plastic components for automotive OEMs | 📈 BULL_ANY_MID | 83 | 🔄90 | ↑1.000 | ↓12d | SQ | -3.8% | -41.57/-41.69 | +1.76% | 20% |
| [CREST](https://in.tradingview.com/chart/?symbol=NSE:CREST)<br><sub>↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 59 | 🔄46 | ↑1.010 | ↑1d | — | +1.7% | -26.81/-29.69 | +1.74% | 20% |
| [PNB](https://in.tradingview.com/chart/?symbol=NSE:PNB)<br><sub>W↑25d · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | 🔄24 | ↑1.012 | ↑2d | — | +2.9% | -19.58/-24.31 | +0.94% | 20% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>🚀SS · ↑CMF4d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄94 | ↑1.031 | ↑1d | — | +4.5% | -28.4/-34.25 | +4.45% | 20% |
| [UNIONBANK](https://in.tradingview.com/chart/?symbol=NSE:UNIONBANK)<br><sub>↑CMF1d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄50 | ↑1.036 | ↑1d | — | +3.7% | -21.82/-27.26 | +3.73% | 20% |
| [ENRIN](https://in.tradingview.com/chart/?symbol=NSE:ENRIN)<br><sub>🚀SS · ↓CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 40 | 🔄73 | ↑1.009 | ↓21d | — | -1.4% | -25.75/-26.7 | +3.26% | 20% |
| [ELGIEQUIP](https://in.tradingview.com/chart/?symbol=NSE:ELGIEQUIP)<br><sub>↓CMF12d</sub> | ⚠ CAUTION | Air compressors automotive equipment manufacturing industrial sector | 📈 BULL_ANY_MID | 40 | 🔄70 | ↑1.000 | ↓15d | — | -3.7% | -40.99/-42.4 | +0.02% | 20% |

```
NSE:SERVOTECH,NSE:FEDERALBNK,NSE:RESPONIND,NSE:AIIL,NSE:VAIBHAVGBL,NSE:PNCINFRA,NSE:EXIDEIND,NSE:MPSLTD,NSE:SONACOMS,NSE:LLOYDSME,NSE:KPRMILL,NSE:TIL,NSE:NITCO,NSE:SANOFI,NSE:MANKIND,NSE:AYMSYNTEX,NSE:BHEL,NSE:THEJO,NSE:AEGISLOG,NSE:ABCAPITAL,NSE:OFSS,NSE:FIVESTAR,NSE:AFCONS,NSE:CAMPUS,NSE:TIIL,NSE:BATAINDIA,NSE:SARDAEN,NSE:SAGCEM,NSE:PASHUPATI,NSE:SHAILY,NSE:CREST,NSE:PNB,NSE:POWERINDIA,NSE:UNIONBANK,NSE:ENRIN,NSE:ELGIEQUIP
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (21)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SERVOTECH](https://in.tradingview.com/chart/?symbol=NSE:SERVOTECH)<br><sub>📶W9 · 🚀SS · ↓CMF16d</sub> | ✓ SAFE | EV chargers solar products power electronics manufacturing | ⚡ BULL_ANY_PPV | 94 | 🔄57 | ↑1.016 | ↑1d | SQ·PV | +3.0% | -25.81/-30.84 | +2.95% | 20% 🟦 |
| [LLOYDSME](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSME)<br><sub>📶W9 · 🚀SS · ↓CMF14d</sub> | ✓ SAFE | Iron ore mining, sponge iron production, power generation | 📈 BULL_ANY_MID | 94 | 🔄79 | ↑1.022 | ↑1d | SQ | +3.1% | 6.52/1.69 | +3.12% | 20% |
| [KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL)<br><sub>📶W9 · ↓CMF1d · DEL54%</sub> | ✓ SAFE | Vertically integrated textile apparel manufacturer with sugar ethanol | 📈 BULL_ANY_MID | 80 | 🔄73 | ↑1.006 | ↓36d | SQ | +21.6% | 5.79/3.79 | +0.76% | 20% |
| [TIL](https://in.tradingview.com/chart/?symbol=NSE:TIL)<br><sub>📶W9 · W↑25d · ↓CMF2d</sub> | ✓ SAFE | Material handling equipment, cranes, construction machinery | 📈 BULL_ANY_MID | 67 | ↑16 | ↑1.014 | ↑3d | SQ | +3.9% | 26.52/25.38 | +0.36% | 20% |
| [NITCO](https://in.tradingview.com/chart/?symbol=NSE:NITCO)<br><sub>📶W9 · W↑85d · ↓CMF0d</sub> | ✓ SAFE | Tiles marble mosaic manufacturing building construction surfaces | 📈 BULL_ANY_MID | 58 | ↑60 | ↓1.019 | ↑2d | SQ | +6.4% | 8.23/4.66 | -1.30% | 20% |
| [SANOFI](https://in.tradingview.com/chart/?symbol=NSE:SANOFI)<br><sub>📶W9 · W↑30d · ↑CMF0d</sub> | ⚠ CAUTION | Diabetes insulin, cardiology drugs, CNS medications, Indian pharma | 📈 BULL_ANY_MID | 58 | ↑8 | ↓1.006 | ↑2d | SQ | +1.1% | 12.6/11.65 | +0.12% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>📶W9 · W↑65d · ↓CMF6d</sub> | ✓ SAFE | Pharma formulations acute chronic diseases consumer health | 📈 BULL_ANY_MID | 51 | ↑63 | ↑1.009 | ↑19d | SQ | +7.4% | 47.69/43.74 | +0.35% | 20% |
| [THEJO](https://in.tradingview.com/chart/?symbol=NSE:THEJO)<br><sub>📶W9 · W↑25d · ↓CMF3d</sub> | ⚠ CAUTION | Bulk material handling, mining equipment, core sector infrastructure | 📈 BULL_ANY_MID | 40 | ↑42 | ↓1.002 | ↑25d | SQ | +21.8% | 30.08/29.79 | -1.17% | 20% |
| [CAMPUS](https://in.tradingview.com/chart/?symbol=NSE:CAMPUS)<br><sub>RVOL185x · ↓CMF1d</sub> | ✓ SAFE | Sportswear and casual apparel manufacturer for mass market | ⚡ BULL_ANY_PPV | 94 | 🔄20 | ↑1.024 | ↑1d | SQ·PV | +4.1% | -38.43/-51.18 | +4.11% | 20% |
| [TIIL](https://in.tradingview.com/chart/?symbol=NSE:TIIL)<br><sub>↑CMF15d</sub> | ⚠ CAUTION | Drum closures, scaffolding systems, textiles manufacturing | ⚡ BULL_ANY_PPV | 94 | 🔄50 | ↑1.015 | ↑1d | SQ·PV | +3.4% | -23.29/-27.77 | +3.44% | 20% |
| [COHANCE](https://in.tradingview.com/chart/?symbol=NSE:COHANCE)<br><sub>W↑147d · ↑CMF18d</sub> | ✓ SAFE | Contract manufacturing for pharmaceutical drug development | ⚡ BULL_ANY_PPV | 59 | ↓18 | ↑0.998 | ↓6d | SQ·PV | +0.4% | -2.94/-3.77 | +0.03% | 20% |
| [LGHL](https://in.tradingview.com/chart/?symbol=NSE:LGHL)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 40 | ↓2 | ↓0.981 | ↓31d | SQ | -10.8% | -71.33/-72.02 | -0.62% | 20% |
| [SAGCEM](https://in.tradingview.com/chart/?symbol=NSE:SAGCEM)<br><sub>W↑15d · ↑CMF7d</sub> | ⚠ CAUTION | Cement manufacturing, South and Central India construction | 📈 BULL_ANY_MID | 99 | 🔄18 | ↑1.014 | ↑1d | SQ | +2.4% | 13.72/11.08 | +2.37% | 20% |
| [PASHUPATI](https://in.tradingview.com/chart/?symbol=NSE:PASHUPATI)<br><sub>↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄74 | ↑1.009 | ↑1d | SQ | +1.6% | -15.3/-16.96 | +1.58% | 20% |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY)<br><sub>↓CMF21d</sub> | ✓ SAFE | Precision injection molded plastic components for automotive OEMs | 📈 BULL_ANY_MID | 83 | 🔄90 | ↑1.000 | ↓12d | SQ | -3.8% | -41.57/-41.69 | +1.76% | 20% |
| [WAAREERTL](https://in.tradingview.com/chart/?symbol=NSE:WAAREERTL)<br><sub>W↑25d · ↓CMF0d</sub> | ✓ SAFE | Solar EPC solutions and renewable power generation systems | 📈 BULL_ANY_MID | 58 | ↓32 | ↓0.998 | ↓2d | SQ | +0.5% | 6.68/6.11 | -0.40% | 20% |
| [AMBUJACEM](https://in.tradingview.com/chart/?symbol=NSE:AMBUJACEM)<br><sub>W↑15d · ↑CMF5d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↓10 | ↓1.004 | ↑3d | SQ | +2.7% | 15.62/14.01 | -0.88% | 20% |
| [SRM](https://in.tradingview.com/chart/?symbol=NSE:SRM)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Road and bridge construction for J&K infrastructure projects | 📈 BULL_ANY_MID | 54 | ↓37 | ↓0.998 | ↓6d | SQ | +3.1% | -18.5/-19.88 | -0.56% | 20% |
| [TCI](https://in.tradingview.com/chart/?symbol=NSE:TCI)<br><sub>W↑35d · ↓CMF12d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 54 | ↓16 | ↓0.999 | ↓6d | SQ | +0.4% | -24.14/-24.29 | -0.19% | 20% |
| [EXCELINDUS](https://in.tradingview.com/chart/?symbol=NSE:EXCELINDUS)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 54 | ↓16 | ↓0.996 | ↓6d | SQ | -0.3% | -37.15/-38.46 | -0.56% | 20% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>↓CMF30d</sub> | ✓ SAFE | Gold casting jewellery design manufacture retail sector | 📈 BULL_ANY_MID | 46 | ↓50 | ↓0.989 | ↓14d | SQ | -4.5% | -47.68/-47.68 | -0.25% | 20% |

```
NSE:SERVOTECH,NSE:LLOYDSME,NSE:KPRMILL,NSE:TIL,NSE:NITCO,NSE:SANOFI,NSE:MANKIND,NSE:THEJO,NSE:CAMPUS,NSE:TIIL,NSE:COHANCE,NSE:LGHL,NSE:SAGCEM,NSE:PASHUPATI,NSE:SHAILY,NSE:WAAREERTL,NSE:AMBUJACEM,NSE:SRM,NSE:TCI,NSE:EXCELINDUS,NSE:SHANTIGOLD
```

---

### 🔥 MAJOR — PPV confirmed (10)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>📶W9 · W↑35d · ↑CMF30d</sub> | ✓ SAFE | Retail corporate banking Kerala-rooted expanding national branch network | ⚡ BULL_ANY_PPV | 49 | 🔄89 | ↑1.052 | ↑1d | PV | +6.9% | 47.35/41.78 | +6.86% | 20% |
| [RESPONIND](https://in.tradingview.com/chart/?symbol=NSE:RESPONIND)<br><sub>📶W9 · W↑68d · RVOL78x · ↑CMF0d</sub> | ✓ SAFE | fasteners manufacturing automotive commercial vehicle suppliers | ⚡ BULL_ANY_PPV | 49 | 🔄79 | ↑1.114 | ↑1d | PV | +15.8% | 14.93/9.39 | +15.75% | 20% |
| [AIIL](https://in.tradingview.com/chart/?symbol=NSE:AIIL)<br><sub>📶W9 · W↑30d · RVOL11x · ↑CMF0d</sub> | ⚠ CAUTION | NBFC lending and securities investment portfolio management | ⚡ BULL_ANY_PPV | 18 | ↑55 | ↑1.088 | ↑2d | PV | +13.8% | -1.23/-17.41 | +9.88% | 20% |
| [VAIBHAVGBL](https://in.tradingview.com/chart/?symbol=NSE:VAIBHAVGBL)<br><sub>📶W9 · W↑68d · ↓CMF30d</sub> | ✓ SAFE | Fashion jewelry and gemstones direct-to-consumer retailer globally | ⚡ BULL_ANY_PPV | 11 | ↑72 | ↑1.043 | ↑9d | PV | +11.8% | 48.19/47.65 | +4.15% | 20% |
| [PNCINFRA](https://in.tradingview.com/chart/?symbol=NSE:PNCINFRA)<br><sub>📶W9 · W↑25d · ↑CMF19d</sub> | ✓ SAFE | Highways bridges airports water infrastructure construction | ⚡ BULL_ANY_PPV | 10 | ↑45 | ↑1.013 | ↑24d | PV | +18.9% | 50.64/50.44 | +0.50% | 20% |
| [EXIDEIND](https://in.tradingview.com/chart/?symbol=NSE:EXIDEIND)<br><sub>📶W9 · W↑73d · ↑CMF11d</sub> | ✓ SAFE | Lead-acid batteries automotive industrial backup power | ⚡ BULL_ANY_PPV | 6 | ↑78 | ↑1.035 | ↑14d | PV | +12.6% | 53.61/52.57 | +3.30% | 20% |
| [MPSLTD](https://in.tradingview.com/chart/?symbol=NSE:MPSLTD)<br><sub>📶W9 · W↑85d · ↓CMF8d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 5 | ↑52 | ↑1.043 | ↑15d | PV | +15.5% | 70.18/68.91 | +1.80% | 20% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>📶W9 · W↑20d · 🚀SS · ★ · ↑CMF11d</sub> | ✓ SAFE | Differential assemblies and gears for electric vehicles | ⚡ BULL_ANY_PPV | 0 | ↑89 | ↑1.048 | ↑24d | PV | +18.2% | 67.64/64.68 | +3.14% | 20% |
| [AFCONS](https://in.tradingview.com/chart/?symbol=NSE:AFCONS)<br><sub>RVOL75x · ↑CMF0d · 🎯SLING</sub> | ✓ SAFE | Heavy infrastructure EPC contractor offshore pipeline marine | 🔥 BULL_OS_PPV | 43 | 🔄7 | ↑1.003 | ↓17d | PV | -4.3% | -64.37/-66.37 | +5.03% | 20% |
| [BATAINDIA](https://in.tradingview.com/chart/?symbol=NSE:BATAINDIA)<br><sub>↓CMF1d</sub> | ✓ SAFE | Footwear manufacturing and retail for Indian mass market consumers | ⚡ BULL_ANY_PPV | 59 | 🔄4 | ↑1.010 | ↑1d | PV | +2.1% | -23.55/-23.64 | +2.08% | 20% |

```
NSE:FEDERALBNK,NSE:RESPONIND,NSE:AIIL,NSE:VAIBHAVGBL,NSE:PNCINFRA,NSE:EXIDEIND,NSE:MPSLTD,NSE:SONACOMS,NSE:AFCONS,NSE:BATAINDIA
```

### 🟢 OVERSOLD — reversal from −53/−60 (6)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [AGIIL](https://in.tradingview.com/chart/?symbol=NSE:AGIIL)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Real estate development and construction projects Punjab region | 🟢 BULL_OVERSOLD | 8 | ↓78 | ↑0.984 | ↓17d | — | -4.9% | -60.92/-61.02 | +0.73% | 20% |
| [GOPAL](https://in.tradingview.com/chart/?symbol=NSE:GOPAL)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Gathiya, ethnic snacks manufacturer, FMCG retail distribution | 🟢 BULL_OVERSOLD | 0 | ↓15 | ↓0.991 | ↓38d | — | -9.3% | -64.04/-67.9 | -0.45% | 20% |
| [SARDAEN](https://in.tradingview.com/chart/?symbol=NSE:SARDAEN)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Steel ferroalloys iron ore pellets power producer | 🟡 BULL_OS_L2 | 40 | 🔄37 | ↑1.002 | ↓20d | — | -4.6% | -51.72/-54.31 | +1.10% | 20% |
| [KANSAINER](https://in.tradingview.com/chart/?symbol=NSE:KANSAINER)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Paint manufacturer for buildings and industrial coatings | 🟡 BULL_OS_L2 | 13 | ↓20 | ↑0.991 | ↓12d | — | -4.2% | -52.87/-54.28 | +0.19% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>↓CMF9d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 5 | ↓51 | ↑0.994 | ↓30d | — | -5.9% | -54.87/-55.01 | +0.38% | 20% |
| [SULA](https://in.tradingview.com/chart/?symbol=NSE:SULA)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Premium grape wine producer, tourism, domestic consumers | 🟡 BULL_OS_L2 | 5 | ↓2 | ↑0.995 | ↓24d | — | -4.1% | -55.47/-56.43 | +0.17% | 20% |

```
NSE:AGIIL,NSE:GOPAL,NSE:SARDAEN,NSE:KANSAINER,NSE:COALINDIA,NSE:SULA
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (18)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [AYMSYNTEX](https://in.tradingview.com/chart/?symbol=NSE:AYMSYNTEX)<br><sub>📶W9 · W↑15d · ↓CMF30d</sub> | ✓ SAFE | Polyester nylon filament yarn manufacturer textile sector | 📈 BULL_ANY_MID | 50 | 🔄77 | ↑1.029 | ↑5d | — | +7.4% | 16.23/14.88 | +3.81% | 20% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄91 | ↑1.037 | ↑1d | — | +3.4% | -7.35/-13.15 | +3.43% | 20% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>📶W9 · W↑73d · 🚀SS · ↑CMF26d</sub> | ✓ SAFE | Bulk liquid terminals, oil gas chemical logistics India | 📈 BULL_ANY_MID | 17 | ↑97 | ↑1.050 | ↑3d | — | +10.4% | 52.46/51.4 | +3.98% | 10% 🟨 |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑63d · ↑CMF16d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 17 | ↑80 | ↓1.020 | ↑3d | — | +5.4% | 47.71/46.67 | -0.44% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Banking software solutions for financial institutions | 📈 BULL_ANY_MID | 5 | ↑90 | ↑1.055 | ↑15d | — | +20.9% | 50.17/48.27 | +4.64% | 20% |
| [FIVESTAR](https://in.tradingview.com/chart/?symbol=NSE:FIVESTAR)<br><sub>📶W9 · W↑25d · ↑CMF21d</sub> | ✓ SAFE | Secured business loans for micro-entrepreneurs and self-employed | 📈 BULL_ANY_MID | 5 | ↑47 | ↑1.025 | ↑25d | — | +27.0% | 47.2/47.0 | +0.96% | 20% |
| [CREST](https://in.tradingview.com/chart/?symbol=NSE:CREST)<br><sub>↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 59 | 🔄46 | ↑1.010 | ↑1d | — | +1.7% | -26.81/-29.69 | +1.74% | 20% |
| [PNB](https://in.tradingview.com/chart/?symbol=NSE:PNB)<br><sub>W↑25d · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | 🔄24 | ↑1.012 | ↑2d | — | +2.9% | -19.58/-24.31 | +0.94% | 20% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>🚀SS · ↑CMF4d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄94 | ↑1.031 | ↑1d | — | +4.5% | -28.4/-34.25 | +4.45% | 20% |
| [UNIONBANK](https://in.tradingview.com/chart/?symbol=NSE:UNIONBANK)<br><sub>↑CMF1d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄50 | ↑1.036 | ↑1d | — | +3.7% | -21.82/-27.26 | +3.73% | 20% |
| [ENRIN](https://in.tradingview.com/chart/?symbol=NSE:ENRIN)<br><sub>🚀SS · ↓CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 40 | 🔄73 | ↑1.009 | ↓21d | — | -1.4% | -25.75/-26.7 | +3.26% | 20% |
| [ELGIEQUIP](https://in.tradingview.com/chart/?symbol=NSE:ELGIEQUIP)<br><sub>↓CMF12d</sub> | ⚠ CAUTION | Air compressors automotive equipment manufacturing industrial sector | 📈 BULL_ANY_MID | 40 | 🔄70 | ↑1.000 | ↓15d | — | -3.7% | -40.99/-42.4 | +0.02% | 20% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>W↑1d · ↓CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 29 | ↓8 | ↑1.008 | ↑1d | — | +1.0% | -31.34/-34.03 | +1.02% | 20% |
| [WAAREEENER](https://in.tradingview.com/chart/?symbol=NSE:WAAREEENER)<br><sub>↓CMF17d</sub> | ✓ SAFE | Solar photovoltaic modules manufacturer, renewable energy sector | 📈 BULL_ANY_MID | 19 | ↓20 | ↑0.994 | ↓6d | — | -0.8% | -50.77/-50.87 | +0.37% | 20% |
| [INDOTHAI](https://in.tradingview.com/chart/?symbol=NSE:INDOTHAI)<br><sub>↓CMF30d</sub> | ✓ SAFE | Brokerage services for equity and derivative trading | 📈 BULL_ANY_MID | 12 | ↓7 | ↑0.993 | ↓13d | — | -3.0% | -31.63/-32.08 | +0.31% | 20% 🟦 |
| [KRISHANA](https://in.tradingview.com/chart/?symbol=NSE:KRISHANA)<br><sub>↑CMF6d</sub> | ✓ SAFE | Phosphatic fertilizers manufacturing for Indian agriculture sector | 📈 BULL_ANY_MID | 12 | ↓0 | ↑0.701 | ↓13d | — | -79.4% | -35.73/-35.94 | +0.14% | 20% |
| [TMPV](https://in.tradingview.com/chart/?symbol=NSE:TMPV)<br><sub>↓CMF17d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 10 | ↓15 | ↑1.001 | ↓21d | — | -8.6% | -43.02/-44.0 | +1.64% | 20% |
| [BERGEPAINT](https://in.tradingview.com/chart/?symbol=NSE:BERGEPAINT)<br><sub>↓CMF0d · ⚠️TRAP</sub> | ⚠ CAUTION | Decorative and industrial paints manufacturer for residential commercial construction | 📈 BULL_ANY_MID | 0 | ↓35 | ↓0.988 | ↓21d | — | -2.2% | -34.71/-35.15 | -0.92% | 20% |

```
NSE:AYMSYNTEX,NSE:BHEL,NSE:AEGISLOG,NSE:ABCAPITAL,NSE:OFSS,NSE:FIVESTAR,NSE:CREST,NSE:PNB,NSE:POWERINDIA,NSE:UNIONBANK,NSE:ENRIN,NSE:ELGIEQUIP,NSE:HDFCLIFE,NSE:WAAREEENER,NSE:INDOTHAI,NSE:KRISHANA,NSE:TMPV,NSE:BERGEPAINT
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
