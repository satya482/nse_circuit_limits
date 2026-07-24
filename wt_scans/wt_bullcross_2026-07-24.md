> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-07-24
*Generated 2026-07-24 15:44 IST*

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

**Total bull crosses today: 49** · 20 inside active squeeze

```
NSE:PIDILITIND,NSE:ARVSMART,NSE:DEEPINDS,NSE:SHRIRAMFIN,NSE:LALPATHLAB,NSE:SATIN,NSE:WENDT,NSE:WEL,NSE:SAMHI,NSE:PVRINOX,NSE:TFCILTD,NSE:SANGHVIMOV,NSE:RATNAVEER,NSE:RPTECH,NSE:PRICOLLTD,NSE:INDIGO,NSE:MARICO,NSE:EFCIL,NSE:LMW,NSE:TVSMOTOR,NSE:ABCAPITAL,NSE:ASIANENE,NSE:NESTLEIND,NSE:LTTS,NSE:GULFOILLUB,NSE:ADANIENT,NSE:VIDHIING,NSE:OAL,NSE:AZAD,NSE:DBL,NSE:GAEL,NSE:APARINDS,NSE:SULA,NSE:TATAELXSI,NSE:DSSL,NSE:NTPC,NSE:MUTHOOTFIN,NSE:HINDZINC,NSE:GRASIM,NSE:GAIL,NSE:TATASTEEL,NSE:NDRAUTO,NSE:ICICIGI,NSE:TIMKEN,NSE:STUDDS,NSE:ADANIPOWER,NSE:POLYCAB,NSE:POWERMECH,NSE:MONTECARLO
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (29)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · W↑68d · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄60 | ↑1.012 | ↑1d | SQ·PV | +2.0% | 3.64/3.38 | +1.99% | 20% |
| [ARVSMART](https://in.tradingview.com/chart/?symbol=NSE:ARVSMART)<br><sub>📶W9 · W↑30d · ↓CMF30d</sub> | ⚠ CAUTION | Residential commercial real estate development urban markets India | ⚡ BULL_ANY_PPV | 99 | 🔄48 | ↑1.013 | ↑1d | SQ·PV | +3.0% | -12.82/-16.75 | +3.00% | 20% |
| [DEEPINDS](https://in.tradingview.com/chart/?symbol=NSE:DEEPINDS)<br><sub>📶W9 · ↓CMF19d</sub> | ✓ SAFE | Offshore drilling services, compression equipment, oil gas operations | ⚡ BULL_ANY_PPV | 94 | 🔄60 | ↑1.022 | ↑1d | SQ·PV | +4.4% | 1.65/1.18 | +4.37% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑26d · 🚀SS · ↓CMF12d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 92 | 🔄79 | ↑1.024 | ↑3d | SQ·PV | +3.9% | 17.16/12.64 | +2.75% | 20% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>📶W9 · W↑78d · ↑CMF8d</sub> | ✓ SAFE | Diagnostic testing, pathology labs, consumer healthcare | ⚡ BULL_ANY_PPV | 64 | ↑77 | ↑1.030 | ↑1d | SQ·PV | +4.3% | 35.76/34.53 | +4.27% | 20% |
| [SATIN](https://in.tradingview.com/chart/?symbol=NSE:SATIN)<br><sub>📶W9 · W↑78d · ↑CMF11d</sub> | ✓ SAFE | Microfinance loans for rural semi-urban underserved populations | ⚡ BULL_ANY_PPV | 59 | ↑96 | ↑1.039 | ↑1d | SQ·PV | +4.9% | 36.99/36.4 | +4.92% | 20% |
| [WENDT](https://in.tradingview.com/chart/?symbol=NSE:WENDT)<br><sub>📶W9 · W↑35d · ↑CMF0d</sub> | ✓ SAFE | Precision grinding wheels and machines for auto manufacturing | ⚡ BULL_ANY_PPV | 49 | 🔄53 | ↑1.047 | ↑1d | PV | +8.7% | -22.22/-26.06 | +8.73% | 20% |
| [WEL](https://in.tradingview.com/chart/?symbol=NSE:WEL)<br><sub>📶W9 · W↑64d · ↓CMF30d · ÷DIV</sub> | ✓ SAFE | Electrical wiring devices and switchgear for residential commercial industrial | ⚡ BULL_ANY_PPV | 40 | ↑15 | ↑1.045 | ↑30d | SQ·PV | +15.7% | 34.03/23.9 | +5.71% | 20% |
| [SAMHI](https://in.tradingview.com/chart/?symbol=NSE:SAMHI)<br><sub>📶W9 · W↑45d · ↑CMF1d</sub> | ✓ SAFE | Branded hotel asset ownership management Marriott IHG Hyatt | ⚡ BULL_ANY_PPV | 19 | ↑41 | ↑1.043 | ↑1d | PV | +4.6% | -22.04/-30.84 | +4.59% | 20% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>📶W9 · W↑20d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Multiplex cinema exhibition across India urban entertainment | ⚡ BULL_ANY_PPV | 18 | ↑50 | ↑1.050 | ↑2d | PV | +7.2% | 47.1/37.52 | +5.61% | 20% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>📶W9 · W↑30d · ↑CMF0d</sub> | ✓ SAFE | Tourism sector financing hotels resorts restaurants amusement parks | ⚡ BULL_ANY_PPV | 10 | ↑85 | ↑1.055 | ↑10d | PV | +16.1% | 46.94/46.03 | +6.31% | 20% |
| [SANGHVIMOV](https://in.tradingview.com/chart/?symbol=NSE:SANGHVIMOV)<br><sub>📶W9 · W↑81d · ↑CMF3d</sub> | ✓ SAFE | Heavy crane rental solutions industrial construction logistics | 📈 BULL_ANY_MID | 89 | 🔄92 | ↑1.041 | ↑1d | SQ | +7.0% | 10.15/9.19 | +7.03% | 20% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · ↓CMF21d</sub> | ✓ SAFE | Stainless steel washers tubes pipes solar mounting industrial | 📈 BULL_ANY_MID | 69 | ↑73 | ↑1.004 | ↑1d | SQ | +0.6% | -12.36/-13.5 | +0.64% | 20% |
| [RPTECH](https://in.tradingview.com/chart/?symbol=NSE:RPTECH)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | IT hardware distributor connecting brands resellers retailers | 📈 BULL_ANY_MID | 64 | ↑99 | ↑1.025 | ↑1d | SQ | +2.4% | 14.86/12.48 | +2.40% | 20% |
| [PRICOLLTD](https://in.tradingview.com/chart/?symbol=NSE:PRICOLLTD)<br><sub>📶W9 · W↑25d · ↑CMF18d</sub> | ✓ SAFE | Automotive instrument clusters precision components Tier-1 OEM supplier | 📈 BULL_ANY_MID | 63 | ↑71 | ↑1.017 | ↑2d | SQ | +3.9% | 25.71/21.82 | +0.42% | 20% |
| [INDIGO](https://in.tradingview.com/chart/?symbol=NSE:INDIGO)<br><sub>📶W9 · W↑45d · 🚀SS · ↑CMF29d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄48 | ↑1.008 | ↑1d | — | +1.1% | 20.36/20.19 | +1.11% | 20% |
| [MARICO](https://in.tradingview.com/chart/?symbol=NSE:MARICO)<br><sub>📶W9 · W↑17d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↑69 | ↓1.010 | ↑3d | SQ | +2.0% | 39.15/35.61 | +0.08% | 20% |
| [EFCIL](https://in.tradingview.com/chart/?symbol=NSE:EFCIL)<br><sub>📶W9 · W↑80d · ↑CMF8d</sub> | ✓ SAFE | Managed office spaces and building services provider | 📈 BULL_ANY_MID | 57 | ↑50 | ↓1.012 | ↑3d | SQ | +4.5% | 6.54/1.29 | -0.45% | 20% |
| [LMW](https://in.tradingview.com/chart/?symbol=NSE:LMW)<br><sub>📶W9 · W↑73d · RVOL14x · ↓CMF0d</sub> | ⚠ CAUTION | Textile spinning machinery and CNC machine tools manufacturer | 📈 BULL_ANY_MID | 55 | ↓57 | ↓0.985 | ↓5d | SQ | -1.9% | 16.46/12.76 | -1.07% | 20% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>📶W9 · W↑21d · ↓CMF9d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄60 | ↑1.043 | ↑1d | — | +5.7% | 34.69/30.07 | +5.68% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑69d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 46 | 🔄80 | ↑1.020 | ↑9d | — | +6.3% | 40.54/39.46 | +2.18% | 20% |
| [ASIANENE](https://in.tradingview.com/chart/?symbol=NSE:ASIANENE)<br><sub>📶W9 · ↓CMF28d</sub> | ✓ SAFE | Seismic data acquisition and oilfield operations services | 📈 BULL_ANY_MID | 29 | ↑74 | ↑1.011 | ↑1d | — | +1.4% | 0.02/-0.15 | +1.45% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑17d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 28 | ↑66 | ↑1.011 | ↑2d | — | +2.0% | 14.61/10.66 | +0.67% | 20% |
| [LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS)<br><sub>📶W9 · W↑10d · ↑CMF7d</sub> | ✓ SAFE | Engineering design development testing services global | 📈 BULL_ANY_MID | 22 | ↑22 | ↑1.018 | ↑3d | — | +3.4% | 17.44/14.99 | +1.27% | 20% |
| [GULFOILLUB](https://in.tradingview.com/chart/?symbol=NSE:GULFOILLUB)<br><sub>📶W9 · W↑45d · ↓CMF7d</sub> | ✓ SAFE | Lubricants manufacturer for automobiles and industrial machinery | 📈 BULL_ANY_MID | 18 | ↑33 | ↓0.998 | ↓2d | — | +3.4% | -26.17/-29.1 | -1.93% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · W↑73d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 12 | ↑87 | ↓1.008 | ↑8d | — | +3.1% | 48.18/47.9 | -0.10% | 20% |
| [VIDHIING](https://in.tradingview.com/chart/?symbol=NSE:VIDHIING)<br><sub>📶W9 · W↑15d · ↓CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 9 | ↑35 | ↑1.024 | ↑16d | — | +9.6% | 35.8/33.04 | +2.00% | 20% |
| [OAL](https://in.tradingview.com/chart/?symbol=NSE:OAL)<br><sub>📶W9 · W↑78d · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 7 | ↑72 | ↑1.055 | ↑13d | — | +17.0% | 33.61/29.94 | +5.89% | 20% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>📶W9 · W↑15d · ↑CMF11d · ÷DIV</sub> | ✓ SAFE | Precision aerospace defense turbine components manufacturer | 📈 BULL_ANY_MID | 3 | ↑88 | ↑1.035 | ↑17d | — | +19.1% | 37.63/35.79 | +3.88% | 20% |

```
NSE:PIDILITIND,NSE:ARVSMART,NSE:DEEPINDS,NSE:SHRIRAMFIN,NSE:LALPATHLAB,NSE:SATIN,NSE:WENDT,NSE:WEL,NSE:SAMHI,NSE:PVRINOX,NSE:TFCILTD,NSE:SANGHVIMOV,NSE:RATNAVEER,NSE:RPTECH,NSE:PRICOLLTD,NSE:INDIGO,NSE:MARICO,NSE:EFCIL,NSE:LMW,NSE:TVSMOTOR,NSE:ABCAPITAL,NSE:ASIANENE,NSE:NESTLEIND,NSE:LTTS,NSE:GULFOILLUB,NSE:ADANIENT,NSE:VIDHIING,NSE:OAL,NSE:AZAD
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (43)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · W↑68d · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄60 | ↑1.012 | ↑1d | SQ·PV | +2.0% | 3.64/3.38 | +1.99% | 20% |
| [ARVSMART](https://in.tradingview.com/chart/?symbol=NSE:ARVSMART)<br><sub>📶W9 · W↑30d · ↓CMF30d</sub> | ⚠ CAUTION | Residential commercial real estate development urban markets India | ⚡ BULL_ANY_PPV | 99 | 🔄48 | ↑1.013 | ↑1d | SQ·PV | +3.0% | -12.82/-16.75 | +3.00% | 20% |
| [DEEPINDS](https://in.tradingview.com/chart/?symbol=NSE:DEEPINDS)<br><sub>📶W9 · ↓CMF19d</sub> | ✓ SAFE | Offshore drilling services, compression equipment, oil gas operations | ⚡ BULL_ANY_PPV | 94 | 🔄60 | ↑1.022 | ↑1d | SQ·PV | +4.4% | 1.65/1.18 | +4.37% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑26d · 🚀SS · ↓CMF12d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 92 | 🔄79 | ↑1.024 | ↑3d | SQ·PV | +3.9% | 17.16/12.64 | +2.75% | 20% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>📶W9 · W↑78d · ↑CMF8d</sub> | ✓ SAFE | Diagnostic testing, pathology labs, consumer healthcare | ⚡ BULL_ANY_PPV | 64 | ↑77 | ↑1.030 | ↑1d | SQ·PV | +4.3% | 35.76/34.53 | +4.27% | 20% |
| [SATIN](https://in.tradingview.com/chart/?symbol=NSE:SATIN)<br><sub>📶W9 · W↑78d · ↑CMF11d</sub> | ✓ SAFE | Microfinance loans for rural semi-urban underserved populations | ⚡ BULL_ANY_PPV | 59 | ↑96 | ↑1.039 | ↑1d | SQ·PV | +4.9% | 36.99/36.4 | +4.92% | 20% |
| [WENDT](https://in.tradingview.com/chart/?symbol=NSE:WENDT)<br><sub>📶W9 · W↑35d · ↑CMF0d</sub> | ✓ SAFE | Precision grinding wheels and machines for auto manufacturing | ⚡ BULL_ANY_PPV | 49 | 🔄53 | ↑1.047 | ↑1d | PV | +8.7% | -22.22/-26.06 | +8.73% | 20% |
| [WEL](https://in.tradingview.com/chart/?symbol=NSE:WEL)<br><sub>📶W9 · W↑64d · ↓CMF30d · ÷DIV</sub> | ✓ SAFE | Electrical wiring devices and switchgear for residential commercial industrial | ⚡ BULL_ANY_PPV | 40 | ↑15 | ↑1.045 | ↑30d | SQ·PV | +15.7% | 34.03/23.9 | +5.71% | 20% |
| [SAMHI](https://in.tradingview.com/chart/?symbol=NSE:SAMHI)<br><sub>📶W9 · W↑45d · ↑CMF1d</sub> | ✓ SAFE | Branded hotel asset ownership management Marriott IHG Hyatt | ⚡ BULL_ANY_PPV | 19 | ↑41 | ↑1.043 | ↑1d | PV | +4.6% | -22.04/-30.84 | +4.59% | 20% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>📶W9 · W↑20d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Multiplex cinema exhibition across India urban entertainment | ⚡ BULL_ANY_PPV | 18 | ↑50 | ↑1.050 | ↑2d | PV | +7.2% | 47.1/37.52 | +5.61% | 20% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>📶W9 · W↑30d · ↑CMF0d</sub> | ✓ SAFE | Tourism sector financing hotels resorts restaurants amusement parks | ⚡ BULL_ANY_PPV | 10 | ↑85 | ↑1.055 | ↑10d | PV | +16.1% | 46.94/46.03 | +6.31% | 20% |
| [SANGHVIMOV](https://in.tradingview.com/chart/?symbol=NSE:SANGHVIMOV)<br><sub>📶W9 · W↑81d · ↑CMF3d</sub> | ✓ SAFE | Heavy crane rental solutions industrial construction logistics | 📈 BULL_ANY_MID | 89 | 🔄92 | ↑1.041 | ↑1d | SQ | +7.0% | 10.15/9.19 | +7.03% | 20% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · ↓CMF21d</sub> | ✓ SAFE | Stainless steel washers tubes pipes solar mounting industrial | 📈 BULL_ANY_MID | 69 | ↑73 | ↑1.004 | ↑1d | SQ | +0.6% | -12.36/-13.5 | +0.64% | 20% |
| [RPTECH](https://in.tradingview.com/chart/?symbol=NSE:RPTECH)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | IT hardware distributor connecting brands resellers retailers | 📈 BULL_ANY_MID | 64 | ↑99 | ↑1.025 | ↑1d | SQ | +2.4% | 14.86/12.48 | +2.40% | 20% |
| [PRICOLLTD](https://in.tradingview.com/chart/?symbol=NSE:PRICOLLTD)<br><sub>📶W9 · W↑25d · ↑CMF18d</sub> | ✓ SAFE | Automotive instrument clusters precision components Tier-1 OEM supplier | 📈 BULL_ANY_MID | 63 | ↑71 | ↑1.017 | ↑2d | SQ | +3.9% | 25.71/21.82 | +0.42% | 20% |
| [INDIGO](https://in.tradingview.com/chart/?symbol=NSE:INDIGO)<br><sub>📶W9 · W↑45d · 🚀SS · ↑CMF29d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄48 | ↑1.008 | ↑1d | — | +1.1% | 20.36/20.19 | +1.11% | 20% |
| [MARICO](https://in.tradingview.com/chart/?symbol=NSE:MARICO)<br><sub>📶W9 · W↑17d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↑69 | ↓1.010 | ↑3d | SQ | +2.0% | 39.15/35.61 | +0.08% | 20% |
| [EFCIL](https://in.tradingview.com/chart/?symbol=NSE:EFCIL)<br><sub>📶W9 · W↑80d · ↑CMF8d</sub> | ✓ SAFE | Managed office spaces and building services provider | 📈 BULL_ANY_MID | 57 | ↑50 | ↓1.012 | ↑3d | SQ | +4.5% | 6.54/1.29 | -0.45% | 20% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>📶W9 · W↑21d · ↓CMF9d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄60 | ↑1.043 | ↑1d | — | +5.7% | 34.69/30.07 | +5.68% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑69d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 46 | 🔄80 | ↑1.020 | ↑9d | — | +6.3% | 40.54/39.46 | +2.18% | 20% |
| [ASIANENE](https://in.tradingview.com/chart/?symbol=NSE:ASIANENE)<br><sub>📶W9 · ↓CMF28d</sub> | ✓ SAFE | Seismic data acquisition and oilfield operations services | 📈 BULL_ANY_MID | 29 | ↑74 | ↑1.011 | ↑1d | — | +1.4% | 0.02/-0.15 | +1.45% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑17d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 28 | ↑66 | ↑1.011 | ↑2d | — | +2.0% | 14.61/10.66 | +0.67% | 20% |
| [LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS)<br><sub>📶W9 · W↑10d · ↑CMF7d</sub> | ✓ SAFE | Engineering design development testing services global | 📈 BULL_ANY_MID | 22 | ↑22 | ↑1.018 | ↑3d | — | +3.4% | 17.44/14.99 | +1.27% | 20% |
| [GULFOILLUB](https://in.tradingview.com/chart/?symbol=NSE:GULFOILLUB)<br><sub>📶W9 · W↑45d · ↓CMF7d</sub> | ✓ SAFE | Lubricants manufacturer for automobiles and industrial machinery | 📈 BULL_ANY_MID | 18 | ↑33 | ↓0.998 | ↓2d | — | +3.4% | -26.17/-29.1 | -1.93% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · W↑73d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 12 | ↑87 | ↓1.008 | ↑8d | — | +3.1% | 48.18/47.9 | -0.10% | 20% |
| [VIDHIING](https://in.tradingview.com/chart/?symbol=NSE:VIDHIING)<br><sub>📶W9 · W↑15d · ↓CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 9 | ↑35 | ↑1.024 | ↑16d | — | +9.6% | 35.8/33.04 | +2.00% | 20% |
| [OAL](https://in.tradingview.com/chart/?symbol=NSE:OAL)<br><sub>📶W9 · W↑78d · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 7 | ↑72 | ↑1.055 | ↑13d | — | +17.0% | 33.61/29.94 | +5.89% | 20% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>📶W9 · W↑15d · ↑CMF11d · ÷DIV</sub> | ✓ SAFE | Precision aerospace defense turbine components manufacturer | 📈 BULL_ANY_MID | 3 | ↑88 | ↑1.035 | ↑17d | — | +19.1% | 37.63/35.79 | +3.88% | 20% |
| [DBL](https://in.tradingview.com/chart/?symbol=NSE:DBL)<br><sub>RVOL215x · ↑CMF0d</sub> | ✓ SAFE | Highway and bridge construction for government infrastructure projects | ⚡ BULL_ANY_PPV | 54 | 🔄22 | ↑1.025 | ↑1d | PV | +8.7% | -41.73/-42.82 | +8.65% | 20% |
| [GAEL](https://in.tradingview.com/chart/?symbol=NSE:GAEL)<br><sub>RVOL11x · ↑CMF0d</sub> | ✓ SAFE | Corn starch derivatives soya feed cotton yarn agro-processing | ⚡ BULL_ANY_PPV | 54 | 🔄75 | ↑1.027 | ↑1d | PV | +9.0% | -44.66/-46.07 | +8.98% | 20% |
| [APARINDS](https://in.tradingview.com/chart/?symbol=NSE:APARINDS)<br><sub>↓CMF13d</sub> | ✓ SAFE | Transmission cables, insulators, specialty oils for power | ⚡ BULL_ANY_PPV | 40 | 🔄91 | ↑1.001 | ↓39d | PV | +8.5% | -27.48/-28.0 | +3.47% | 20% |
| [SULA](https://in.tradingview.com/chart/?symbol=NSE:SULA)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Premium grape wine producer, tourism, domestic consumers | ⚡ BULL_ANY_PPV | 5 | ↑3 | ↑1.000 | ↓29d | PV | -4.0% | -48.06/-50.0 | +0.30% | 20% |
| [TATAELXSI](https://in.tradingview.com/chart/?symbol=NSE:TATAELXSI)<br><sub>↓CMF18d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Design engineering services automotive media communications healthcare | 🟢 BULL_OVERSOLD | 50 | 🔄3 | ↑1.002 | ↓10d | — | -4.1% | -60.66/-62.01 | +4.44% | 20% |
| [DSSL](https://in.tradingview.com/chart/?symbol=NSE:DSSL)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | IT infrastructure, system integration, managed services, cloud computing | 🟡 BULL_OS_L2 | 40 | 🔄79 | ↑1.008 | ↓23d | — | -11.5% | -56.73/-58.44 | +4.99% | 5% 🟥 |
| [MUTHOOTFIN](https://in.tradingview.com/chart/?symbol=NSE:MUTHOOTFIN)<br><sub>🚀SS · ↓CMF3d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄26 | ↑1.015 | ↑1d | SQ | +3.3% | -27.02/-29.52 | +3.27% | 20% |
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄39 | ↑1.012 | ↑1d | SQ | +2.4% | -40.58/-44.61 | +2.36% | 20% |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>🚀SS · ↓CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 68 | ↑67 | ↑1.010 | ↑2d | SQ | +1.9% | 4.33/1.26 | +0.83% | 20% |
| [ICICIGI](https://in.tradingview.com/chart/?symbol=NSE:ICICIGI)<br><sub>↑CMF5d</sub> | ✓ SAFE | General insurance motor health property casualty India | 📈 BULL_ANY_MID | 47 | 🔄25 | ↑0.997 | ↓8d | — | -7.1% | -42.75/-42.9 | +2.64% | 20% |
| [TIMKEN](https://in.tradingview.com/chart/?symbol=NSE:TIMKEN)<br><sub>↓CMF27d</sub> | ⚠ CAUTION | Tapered roller bearings industrial motion automotive manufacturing | 📈 BULL_ANY_MID | 35 | 🔄37 | ↑0.994 | ↓26d | — | -12.5% | -48.03/-49.41 | +1.42% | 20% |
| [STUDDS](https://in.tradingview.com/chart/?symbol=NSE:STUDDS)<br><sub>↓CMF12d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 35 | 🔄50 | ↑1.000 | ↓24d | — | -6.1% | -48.33/-49.37 | +1.62% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>🚀SS · ↓CMF19d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 24 | ↑87 | ↑1.005 | ↓6d | — | +2.3% | -31.17/-34.4 | +0.16% | 20% |
| [POWERMECH](https://in.tradingview.com/chart/?symbol=NSE:POWERMECH)<br><sub>↓CMF24d</sub> | ✓ SAFE | EPC contractor boilers turbines generators power infrastructure | 📈 BULL_ANY_MID | 10 | ↑50 | ↑1.006 | ↓34d | — | +4.3% | -38.62/-40.94 | +1.49% | 20% |
| [MONTECARLO](https://in.tradingview.com/chart/?symbol=NSE:MONTECARLO)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 2 | ↑27 | ↓0.997 | ↓18d | — | -2.8% | -34.45/-34.7 | -0.17% | 20% |

```
NSE:PIDILITIND,NSE:ARVSMART,NSE:DEEPINDS,NSE:SHRIRAMFIN,NSE:LALPATHLAB,NSE:SATIN,NSE:WENDT,NSE:WEL,NSE:SAMHI,NSE:PVRINOX,NSE:TFCILTD,NSE:SANGHVIMOV,NSE:RATNAVEER,NSE:RPTECH,NSE:PRICOLLTD,NSE:INDIGO,NSE:MARICO,NSE:EFCIL,NSE:TVSMOTOR,NSE:ABCAPITAL,NSE:ASIANENE,NSE:NESTLEIND,NSE:LTTS,NSE:GULFOILLUB,NSE:ADANIENT,NSE:VIDHIING,NSE:OAL,NSE:AZAD,NSE:DBL,NSE:GAEL,NSE:APARINDS,NSE:SULA,NSE:TATAELXSI,NSE:DSSL,NSE:MUTHOOTFIN,NSE:HINDZINC,NSE:GRASIM,NSE:ICICIGI,NSE:TIMKEN,NSE:STUDDS,NSE:ADANIPOWER,NSE:POWERMECH,NSE:MONTECARLO
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (20)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · W↑68d · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄60 | ↑1.012 | ↑1d | SQ·PV | +2.0% | 3.64/3.38 | +1.99% | 20% |
| [ARVSMART](https://in.tradingview.com/chart/?symbol=NSE:ARVSMART)<br><sub>📶W9 · W↑30d · ↓CMF30d</sub> | ⚠ CAUTION | Residential commercial real estate development urban markets India | ⚡ BULL_ANY_PPV | 99 | 🔄48 | ↑1.013 | ↑1d | SQ·PV | +3.0% | -12.82/-16.75 | +3.00% | 20% |
| [DEEPINDS](https://in.tradingview.com/chart/?symbol=NSE:DEEPINDS)<br><sub>📶W9 · ↓CMF19d</sub> | ✓ SAFE | Offshore drilling services, compression equipment, oil gas operations | ⚡ BULL_ANY_PPV | 94 | 🔄60 | ↑1.022 | ↑1d | SQ·PV | +4.4% | 1.65/1.18 | +4.37% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑26d · 🚀SS · ↓CMF12d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 92 | 🔄79 | ↑1.024 | ↑3d | SQ·PV | +3.9% | 17.16/12.64 | +2.75% | 20% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>📶W9 · W↑78d · ↑CMF8d</sub> | ✓ SAFE | Diagnostic testing, pathology labs, consumer healthcare | ⚡ BULL_ANY_PPV | 64 | ↑77 | ↑1.030 | ↑1d | SQ·PV | +4.3% | 35.76/34.53 | +4.27% | 20% |
| [SATIN](https://in.tradingview.com/chart/?symbol=NSE:SATIN)<br><sub>📶W9 · W↑78d · ↑CMF11d</sub> | ✓ SAFE | Microfinance loans for rural semi-urban underserved populations | ⚡ BULL_ANY_PPV | 59 | ↑96 | ↑1.039 | ↑1d | SQ·PV | +4.9% | 36.99/36.4 | +4.92% | 20% |
| [WEL](https://in.tradingview.com/chart/?symbol=NSE:WEL)<br><sub>📶W9 · W↑64d · ↓CMF30d · ÷DIV</sub> | ✓ SAFE | Electrical wiring devices and switchgear for residential commercial industrial | ⚡ BULL_ANY_PPV | 40 | ↑15 | ↑1.045 | ↑30d | SQ·PV | +15.7% | 34.03/23.9 | +5.71% | 20% |
| [SANGHVIMOV](https://in.tradingview.com/chart/?symbol=NSE:SANGHVIMOV)<br><sub>📶W9 · W↑81d · ↑CMF3d</sub> | ✓ SAFE | Heavy crane rental solutions industrial construction logistics | 📈 BULL_ANY_MID | 89 | 🔄92 | ↑1.041 | ↑1d | SQ | +7.0% | 10.15/9.19 | +7.03% | 20% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · ↓CMF21d</sub> | ✓ SAFE | Stainless steel washers tubes pipes solar mounting industrial | 📈 BULL_ANY_MID | 69 | ↑73 | ↑1.004 | ↑1d | SQ | +0.6% | -12.36/-13.5 | +0.64% | 20% |
| [RPTECH](https://in.tradingview.com/chart/?symbol=NSE:RPTECH)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | IT hardware distributor connecting brands resellers retailers | 📈 BULL_ANY_MID | 64 | ↑99 | ↑1.025 | ↑1d | SQ | +2.4% | 14.86/12.48 | +2.40% | 20% |
| [PRICOLLTD](https://in.tradingview.com/chart/?symbol=NSE:PRICOLLTD)<br><sub>📶W9 · W↑25d · ↑CMF18d</sub> | ✓ SAFE | Automotive instrument clusters precision components Tier-1 OEM supplier | 📈 BULL_ANY_MID | 63 | ↑71 | ↑1.017 | ↑2d | SQ | +3.9% | 25.71/21.82 | +0.42% | 20% |
| [MARICO](https://in.tradingview.com/chart/?symbol=NSE:MARICO)<br><sub>📶W9 · W↑17d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↑69 | ↓1.010 | ↑3d | SQ | +2.0% | 39.15/35.61 | +0.08% | 20% |
| [EFCIL](https://in.tradingview.com/chart/?symbol=NSE:EFCIL)<br><sub>📶W9 · W↑80d · ↑CMF8d</sub> | ✓ SAFE | Managed office spaces and building services provider | 📈 BULL_ANY_MID | 57 | ↑50 | ↓1.012 | ↑3d | SQ | +4.5% | 6.54/1.29 | -0.45% | 20% |
| [LMW](https://in.tradingview.com/chart/?symbol=NSE:LMW)<br><sub>📶W9 · W↑73d · RVOL14x · ↓CMF0d</sub> | ⚠ CAUTION | Textile spinning machinery and CNC machine tools manufacturer | 📈 BULL_ANY_MID | 55 | ↓57 | ↓0.985 | ↓5d | SQ | -1.9% | 16.46/12.76 | -1.07% | 20% |
| [MUTHOOTFIN](https://in.tradingview.com/chart/?symbol=NSE:MUTHOOTFIN)<br><sub>🚀SS · ↓CMF3d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄26 | ↑1.015 | ↑1d | SQ | +3.3% | -27.02/-29.52 | +3.27% | 20% |
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄39 | ↑1.012 | ↑1d | SQ | +2.4% | -40.58/-44.61 | +2.36% | 20% |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>🚀SS · ↓CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 68 | ↑67 | ↑1.010 | ↑2d | SQ | +1.9% | 4.33/1.26 | +0.83% | 20% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>W↑68d · ↓CMF12d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 68 | ↓51 | ↑1.005 | ↑2d | SQ | +1.3% | 0.89/-3.8 | +0.23% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>↓CMF20d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↓43 | ↑1.000 | ↓8d | SQ | -0.3% | -49.16/-51.32 | +0.48% | 20% |
| [NDRAUTO](https://in.tradingview.com/chart/?symbol=NSE:NDRAUTO)<br><sub>↓CMF0d · ⚠️TRAP</sub> | ✓ SAFE | Automotive seat frames trims supplier passenger vehicles OEM | 📈 BULL_ANY_MID | 48 | ↓37 | ↓0.987 | ↓12d | SQ | -3.6% | -20.83/-23.05 | -0.78% | 20% |

```
NSE:PIDILITIND,NSE:ARVSMART,NSE:DEEPINDS,NSE:SHRIRAMFIN,NSE:LALPATHLAB,NSE:SATIN,NSE:WEL,NSE:SANGHVIMOV,NSE:RATNAVEER,NSE:RPTECH,NSE:PRICOLLTD,NSE:MARICO,NSE:EFCIL,NSE:LMW,NSE:MUTHOOTFIN,NSE:HINDZINC,NSE:GRASIM,NSE:GAIL,NSE:TATASTEEL,NSE:NDRAUTO
```

---

### 🔥 MAJOR — PPV confirmed (8)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [WENDT](https://in.tradingview.com/chart/?symbol=NSE:WENDT)<br><sub>📶W9 · W↑35d · ↑CMF0d</sub> | ✓ SAFE | Precision grinding wheels and machines for auto manufacturing | ⚡ BULL_ANY_PPV | 49 | 🔄53 | ↑1.047 | ↑1d | PV | +8.7% | -22.22/-26.06 | +8.73% | 20% |
| [SAMHI](https://in.tradingview.com/chart/?symbol=NSE:SAMHI)<br><sub>📶W9 · W↑45d · ↑CMF1d</sub> | ✓ SAFE | Branded hotel asset ownership management Marriott IHG Hyatt | ⚡ BULL_ANY_PPV | 19 | ↑41 | ↑1.043 | ↑1d | PV | +4.6% | -22.04/-30.84 | +4.59% | 20% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>📶W9 · W↑20d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Multiplex cinema exhibition across India urban entertainment | ⚡ BULL_ANY_PPV | 18 | ↑50 | ↑1.050 | ↑2d | PV | +7.2% | 47.1/37.52 | +5.61% | 20% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>📶W9 · W↑30d · ↑CMF0d</sub> | ✓ SAFE | Tourism sector financing hotels resorts restaurants amusement parks | ⚡ BULL_ANY_PPV | 10 | ↑85 | ↑1.055 | ↑10d | PV | +16.1% | 46.94/46.03 | +6.31% | 20% |
| [DBL](https://in.tradingview.com/chart/?symbol=NSE:DBL)<br><sub>RVOL215x · ↑CMF0d</sub> | ✓ SAFE | Highway and bridge construction for government infrastructure projects | ⚡ BULL_ANY_PPV | 54 | 🔄22 | ↑1.025 | ↑1d | PV | +8.7% | -41.73/-42.82 | +8.65% | 20% |
| [GAEL](https://in.tradingview.com/chart/?symbol=NSE:GAEL)<br><sub>RVOL11x · ↑CMF0d</sub> | ✓ SAFE | Corn starch derivatives soya feed cotton yarn agro-processing | ⚡ BULL_ANY_PPV | 54 | 🔄75 | ↑1.027 | ↑1d | PV | +9.0% | -44.66/-46.07 | +8.98% | 20% |
| [APARINDS](https://in.tradingview.com/chart/?symbol=NSE:APARINDS)<br><sub>↓CMF13d</sub> | ✓ SAFE | Transmission cables, insulators, specialty oils for power | ⚡ BULL_ANY_PPV | 40 | 🔄91 | ↑1.001 | ↓39d | PV | +8.5% | -27.48/-28.0 | +3.47% | 20% |
| [SULA](https://in.tradingview.com/chart/?symbol=NSE:SULA)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Premium grape wine producer, tourism, domestic consumers | ⚡ BULL_ANY_PPV | 5 | ↑3 | ↑1.000 | ↓29d | PV | -4.0% | -48.06/-50.0 | +0.30% | 20% |

```
NSE:WENDT,NSE:SAMHI,NSE:PVRINOX,NSE:TFCILTD,NSE:DBL,NSE:GAEL,NSE:APARINDS,NSE:SULA
```

### 🟢 OVERSOLD — reversal from −53/−60 (3)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [TATAELXSI](https://in.tradingview.com/chart/?symbol=NSE:TATAELXSI)<br><sub>↓CMF18d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Design engineering services automotive media communications healthcare | 🟢 BULL_OVERSOLD | 50 | 🔄3 | ↑1.002 | ↓10d | — | -4.1% | -60.66/-62.01 | +4.44% | 20% |
| [DSSL](https://in.tradingview.com/chart/?symbol=NSE:DSSL)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | IT infrastructure, system integration, managed services, cloud computing | 🟡 BULL_OS_L2 | 40 | 🔄79 | ↑1.008 | ↓23d | — | -11.5% | -56.73/-58.44 | +4.99% | 5% 🟥 |
| [NTPC](https://in.tradingview.com/chart/?symbol=NSE:NTPC)<br><sub>↓CMF4d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 29 | ↓34 | ↑1.003 | ↑1d | — | +0.5% | -51.44/-55.81 | +0.45% | 20% |

```
NSE:TATAELXSI,NSE:DSSL,NSE:NTPC
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (18)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [INDIGO](https://in.tradingview.com/chart/?symbol=NSE:INDIGO)<br><sub>📶W9 · W↑45d · 🚀SS · ↑CMF29d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄48 | ↑1.008 | ↑1d | — | +1.1% | 20.36/20.19 | +1.11% | 20% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>📶W9 · W↑21d · ↓CMF9d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄60 | ↑1.043 | ↑1d | — | +5.7% | 34.69/30.07 | +5.68% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑69d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 46 | 🔄80 | ↑1.020 | ↑9d | — | +6.3% | 40.54/39.46 | +2.18% | 20% |
| [ASIANENE](https://in.tradingview.com/chart/?symbol=NSE:ASIANENE)<br><sub>📶W9 · ↓CMF28d</sub> | ✓ SAFE | Seismic data acquisition and oilfield operations services | 📈 BULL_ANY_MID | 29 | ↑74 | ↑1.011 | ↑1d | — | +1.4% | 0.02/-0.15 | +1.45% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑17d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 28 | ↑66 | ↑1.011 | ↑2d | — | +2.0% | 14.61/10.66 | +0.67% | 20% |
| [LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS)<br><sub>📶W9 · W↑10d · ↑CMF7d</sub> | ✓ SAFE | Engineering design development testing services global | 📈 BULL_ANY_MID | 22 | ↑22 | ↑1.018 | ↑3d | — | +3.4% | 17.44/14.99 | +1.27% | 20% |
| [GULFOILLUB](https://in.tradingview.com/chart/?symbol=NSE:GULFOILLUB)<br><sub>📶W9 · W↑45d · ↓CMF7d</sub> | ✓ SAFE | Lubricants manufacturer for automobiles and industrial machinery | 📈 BULL_ANY_MID | 18 | ↑33 | ↓0.998 | ↓2d | — | +3.4% | -26.17/-29.1 | -1.93% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · W↑73d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 12 | ↑87 | ↓1.008 | ↑8d | — | +3.1% | 48.18/47.9 | -0.10% | 20% |
| [VIDHIING](https://in.tradingview.com/chart/?symbol=NSE:VIDHIING)<br><sub>📶W9 · W↑15d · ↓CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 9 | ↑35 | ↑1.024 | ↑16d | — | +9.6% | 35.8/33.04 | +2.00% | 20% |
| [OAL](https://in.tradingview.com/chart/?symbol=NSE:OAL)<br><sub>📶W9 · W↑78d · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 7 | ↑72 | ↑1.055 | ↑13d | — | +17.0% | 33.61/29.94 | +5.89% | 20% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>📶W9 · W↑15d · ↑CMF11d · ÷DIV</sub> | ✓ SAFE | Precision aerospace defense turbine components manufacturer | 📈 BULL_ANY_MID | 3 | ↑88 | ↑1.035 | ↑17d | — | +19.1% | 37.63/35.79 | +3.88% | 20% |
| [ICICIGI](https://in.tradingview.com/chart/?symbol=NSE:ICICIGI)<br><sub>↑CMF5d</sub> | ✓ SAFE | General insurance motor health property casualty India | 📈 BULL_ANY_MID | 47 | 🔄25 | ↑0.997 | ↓8d | — | -7.1% | -42.75/-42.9 | +2.64% | 20% |
| [TIMKEN](https://in.tradingview.com/chart/?symbol=NSE:TIMKEN)<br><sub>↓CMF27d</sub> | ⚠ CAUTION | Tapered roller bearings industrial motion automotive manufacturing | 📈 BULL_ANY_MID | 35 | 🔄37 | ↑0.994 | ↓26d | — | -12.5% | -48.03/-49.41 | +1.42% | 20% |
| [STUDDS](https://in.tradingview.com/chart/?symbol=NSE:STUDDS)<br><sub>↓CMF12d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 35 | 🔄50 | ↑1.000 | ↓24d | — | -6.1% | -48.33/-49.37 | +1.62% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>🚀SS · ↓CMF19d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 24 | ↑87 | ↑1.005 | ↓6d | — | +2.3% | -31.17/-34.4 | +0.16% | 20% |
| [POLYCAB](https://in.tradingview.com/chart/?symbol=NSE:POLYCAB)<br><sub>↓CMF6d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 12 | ↓75 | ↓0.982 | ↓8d | — | -3.9% | -46.59/-46.91 | -1.62% | 20% |
| [POWERMECH](https://in.tradingview.com/chart/?symbol=NSE:POWERMECH)<br><sub>↓CMF24d</sub> | ✓ SAFE | EPC contractor boilers turbines generators power infrastructure | 📈 BULL_ANY_MID | 10 | ↑50 | ↑1.006 | ↓34d | — | +4.3% | -38.62/-40.94 | +1.49% | 20% |
| [MONTECARLO](https://in.tradingview.com/chart/?symbol=NSE:MONTECARLO)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 2 | ↑27 | ↓0.997 | ↓18d | — | -2.8% | -34.45/-34.7 | -0.17% | 20% |

```
NSE:INDIGO,NSE:TVSMOTOR,NSE:ABCAPITAL,NSE:ASIANENE,NSE:NESTLEIND,NSE:LTTS,NSE:GULFOILLUB,NSE:ADANIENT,NSE:VIDHIING,NSE:OAL,NSE:AZAD,NSE:ICICIGI,NSE:TIMKEN,NSE:STUDDS,NSE:ADANIPOWER,NSE:POLYCAB,NSE:POWERMECH,NSE:MONTECARLO
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
