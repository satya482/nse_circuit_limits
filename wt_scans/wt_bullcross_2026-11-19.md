> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-11-19
*Generated 2026-11-19 15:48 IST*

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

**Total bull crosses today: 61** · 22 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:PWL,NSE:BLKASHYAP,NSE:TINNARUBR,NSE:CROMPTON,NSE:LTFOODS,NSE:ENDURANCE,NSE:TVSHLTD,NSE:GABRIEL,NSE:JTEKTINDIA,NSE:SIMPLEXINF,NSE:ADVENZYMES,NSE:HESTERBIO,NSE:SIGMAADV,NSE:MARINE,NSE:UBL,NSE:SYSTMTXC,NSE:HITECH,NSE:JKCEMENT,NSE:VGUARD,NSE:TATACONSUM,NSE:NINSYS,NSE:STARHEALTH,NSE:BALAJITELE,NSE:ASKAUTOLTD,NSE:AMBUJACEM,NSE:SUNTECK,NSE:UPL,NSE:ETHOSLTD,NSE:ORIENTCEM,NSE:EICHERMOT,NSE:MINDACORP,NSE:DLINKINDIA,NSE:ASHAPURMIN,NSE:TATATECH,NSE:IPL,NSE:AMBER,NSE:ASHIKAG,NSE:TEAMLEASE,NSE:PNCINFRA,NSE:BAJAJELEC,NSE:HNDFDS,NSE:SIGNPOST,NSE:SOMANYCERA,NSE:COHANCE,NSE:MAHSCOOTER,NSE:SKFINDUS,NSE:MMP,NSE:SHAILY,NSE:SYRMA,NSE:SRF,NSE:HATSUN,NSE:VIDHIING,NSE:KAJARIACER,NSE:EIHAHOTELS,NSE:CARTRADE,NSE:SAGCEM,NSE:KRN,NSE:NRBBEARING,NSE:CYIENT,NSE:VADILALIND,NSE:AMRUTANJAN
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (31)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PWL](https://in.tradingview.com/chart/?symbol=NSE:PWL)<br><sub>📶W9 · W↑4d · 🚀SS·8x · ↓CMF10d</sub> | ✓ SAFE | Online test prep and upskilling courses for competitive exams | ⚡ BULL_ANY_PPV | 89 | 🔄75 | ↑1.043 | ↑1d | SQ·PV | +6.3% | 18.63/5.87 | +6.31% | 20% |
| [BLKASHYAP](https://in.tradingview.com/chart/?symbol=NSE:BLKASHYAP)<br><sub>📶W9 · W↑8d · RVOL141x · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | High-rise building construction EPC for residential commercial | ⚡ BULL_ANY_PPV | 89 | 🔄74 | ↑1.081 | ↑1d | SQ·PV | +12.1% | 3.29/-0.12 | +12.14% | 20% |
| [TINNARUBR](https://in.tradingview.com/chart/?symbol=NSE:TINNARUBR)<br><sub>📶W9 · W↑4d · 🚀SS·46x · ↑CMF0d</sub> | ✓ SAFE | Waste tyre recycling into crumb rubber and steel | ⚡ BULL_ANY_PPV | 49 | 🔄73 | ↑1.139 | ↑1d | PV | +19.6% | 6.88/0.21 | +19.63% | 20% |
| [CROMPTON](https://in.tradingview.com/chart/?symbol=NSE:CROMPTON)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Fans, lighting, water pumps, home electrical appliances | ⚡ BULL_ANY_PPV | 49 | 🔄21 | ↑1.037 | ↑1d | PV | +6.1% | 11.09/11.0 | +6.13% | 20% |
| [LTFOODS](https://in.tradingview.com/chart/?symbol=NSE:LTFOODS)<br><sub>📶W9 · W↑8d · 🚀SS·76x · ↓CMF0d</sub> | ✓ SAFE | Rice and rice products FMCG global consumer foods | ⚡ BULL_ANY_PPV | 37 | 🔄62 | ↑1.037 | ↑13d | PV | +11.5% | 30.27/24.5 | +4.65% | 20% |
| [ENDURANCE](https://in.tradingview.com/chart/?symbol=NSE:ENDURANCE)<br><sub>📶W9 · W↑8d · ↑CMF6d</sub> | ⚠ CAUTION | Aluminium castings, suspension, braking systems for automobiles | ⚡ BULL_ANY_PPV | 36 | 🔄41 | ↑1.034 | ↑14d | PV | +14.1% | 23.04/20.94 | +4.93% | 20% |
| [TVSHLTD](https://in.tradingview.com/chart/?symbol=NSE:TVSHLTD)<br><sub>📶W9 · W↑14d · ↑CMF15d</sub> | ⚠ CAUTION | Aluminum die castings automotive components manufacturing India | ⚡ BULL_ANY_PPV | 17 | ↑48 | ↑1.064 | ↑3d | PV | +10.6% | 25.65/21.49 | +7.47% | 5% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>📶W9 · W↑8d · ★ · ↑CMF5d</sub> | ✓ SAFE | Shock absorbers and struts for two-wheeler and four-wheeler OEMs | ⚡ BULL_ANY_PPV | 14 | ↑91 | ↑1.057 | ↑6d | PV | +12.6% | 40.6/37.13 | +6.30% | 20% |
| [JTEKTINDIA](https://in.tradingview.com/chart/?symbol=NSE:JTEKTINDIA)<br><sub>📶W9 · W↑14d · ↓CMF12d</sub> | ⚠ CAUTION | Steering systems and driveline components for automobiles | ⚡ BULL_ANY_PPV | 11 | ↑39 | ↑1.021 | ↑14d | PV | +12.1% | 30.69/30.49 | +2.25% | 20% |
| [SIMPLEXINF](https://in.tradingview.com/chart/?symbol=NSE:SIMPLEXINF)<br><sub>📶W9 · W↑29d · ↑CMF24d</sub> | ✓ SAFE | Civil construction contractor for infrastructure projects | ⚡ BULL_ANY_PPV | 7 | ↑82 | ↑1.040 | ↑13d | PV | +17.3% | 51.48/50.78 | +1.19% | 20% |
| [ADVENZYMES](https://in.tradingview.com/chart/?symbol=NSE:ADVENZYMES)<br><sub>📶W9 · W↑14d · ↑CMF5d</sub> | ✓ SAFE | Enzyme manufacturing, pharmaceuticals, food, industrial applications | ⚡ BULL_ANY_PPV | 4 | ↑40 | ↑1.045 | ↑16d | PV | +14.1% | 32.6/26.54 | +5.43% | 20% |
| [HESTERBIO](https://in.tradingview.com/chart/?symbol=NSE:HESTERBIO)<br><sub>📶W9 · W↑14d · ↓CMF12d</sub> | ⚠ CAUTION | Poultry livestock vaccines manufacturer animal healthcare sector | ⚡ BULL_ANY_PPV | 2 | ↑80 | ↓1.010 | ↑18d | PV | +14.3% | 29.85/25.55 | +0.17% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE)<br><sub>📶W9 · ↓CMF13d</sub> | n/a | Electrical automation solar solutions marine industrial sectors | 📈 BULL_ANY_MID | 94 | 🔄95 | ↑1.015 | ↑1d | SQ | +2.6% | -2.34/-3.15 | +2.60% | 20% |
| [UBL](https://in.tradingview.com/chart/?symbol=NSE:UBL)<br><sub>📶W9 · W↑19d · ↓CMF30d</sub> | ✓ SAFE | Beer manufacturer, India domestic market, Kingfisher brand leader | 📈 BULL_ANY_MID | 57 | ↑28 | ↑1.042 | ↑3d | SQ | +6.3% | 31.22/21.86 | +3.97% | 20% |
| [SYSTMTXC](https://in.tradingview.com/chart/?symbol=NSE:SYSTMTXC)<br><sub>📶W9 · W↑51d · ↓CMF20d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 53 | ↑68 | ↑1.018 | ↑12d | SQ | +7.5% | 47.39/46.26 | +1.64% | 5% |
| [HITECH](https://in.tradingview.com/chart/?symbol=NSE:HITECH)<br><sub>📶W9 · W↑14d · ↓CMF26d</sub> | ✓ SAFE | ERW steel pipes tubes construction automotive infrastructure | 📈 BULL_ANY_MID | 44 | 🔄25 | ↑1.011 | ↑16d | — | +18.5% | 17.4/17.17 | +1.64% | 20% |
| [JKCEMENT](https://in.tradingview.com/chart/?symbol=NSE:JKCEMENT)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF15d</sub> | ⚠ CAUTION | Cement manufacturing construction materials India domestic markets | 📈 BULL_ANY_MID | 41 | 🔄52 | ↑1.023 | ↑14d | — | +11.2% | 39.13/38.47 | +3.27% | 20% |
| [VGUARD](https://in.tradingview.com/chart/?symbol=NSE:VGUARD)<br><sub>📶W9 · W↑8d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | Voltage stabilizers, surge protectors, home appliances manufacturer | 📈 BULL_ANY_MID | 39 | 🔄39 | ↑1.022 | ↑16d | — | +15.1% | 22.87/22.77 | +2.95% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄55 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [NINSYS](https://in.tradingview.com/chart/?symbol=NSE:NINSYS)<br><sub>📶W9 · W↑34d · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 28 | ↑98 | ↑1.012 | ↑2d | — | +2.2% | 23.2/22.75 | +0.71% | 20% |
| [STARHEALTH](https://in.tradingview.com/chart/?symbol=NSE:STARHEALTH)<br><sub>📶W9 · W↑8d · ↓CMF13d</sub> | ✓ SAFE | Health insurance provider, retail customers, India | 📈 BULL_ANY_MID | 23 | ↑68 | ↑1.017 | ↑2d | — | +3.5% | 18.36/17.67 | +1.58% | 20% |
| [BALAJITELE](https://in.tradingview.com/chart/?symbol=NSE:BALAJITELE)<br><sub>📶W9 · W↑8d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | TV serials films digital content production entertainment | 📈 BULL_ANY_MID | 18 | ↑53 | ↑1.041 | ↑2d | — | +7.1% | 32.28/31.83 | +3.20% | 20% |
| [ASKAUTOLTD](https://in.tradingview.com/chart/?symbol=NSE:ASKAUTOLTD)<br><sub>📶W9 · W↑8d · ↑CMF10d</sub> | ✓ SAFE | Two-wheeler braking systems manufacturer India | 📈 BULL_ANY_MID | 14 | ↑85 | ↑1.018 | ↑11d | — | +10.6% | 37.11/36.69 | +1.69% | 20% |
| [AMBUJACEM](https://in.tradingview.com/chart/?symbol=NSE:AMBUJACEM)<br><sub>📶W9 · W↑19d · 🚀SS · ↓CMF17d</sub> | ✓ SAFE | Cement manufacturer, construction materials, infrastructure demand | 📈 BULL_ANY_MID | 11 | ↑24 | ↑1.028 | ↑14d | — | +14.0% | 37.7/34.93 | +3.12% | 20% |
| [SUNTECK](https://in.tradingview.com/chart/?symbol=NSE:SUNTECK)<br><sub>📶W9 · W↑19d · ↓CMF0d</sub> | ✓ SAFE | Luxury residential developer MMR premium apartments commercial | 📈 BULL_ANY_MID | 9 | ↑36 | ↑1.025 | ↑16d | — | +15.1% | 53.03/52.98 | +0.63% | 20% |
| [UPL](https://in.tradingview.com/chart/?symbol=NSE:UPL)<br><sub>📶W9 · W↑19d · ↑CMF17d</sub> | ✓ SAFE | Agrochemicals pesticides seeds fertilizers global agribusiness | 📈 BULL_ANY_MID | 8 | ↑26 | ↑1.033 | ↑12d | — | +10.0% | 46.46/44.3 | +3.22% | 20% |
| [ETHOSLTD](https://in.tradingview.com/chart/?symbol=NSE:ETHOSLTD)<br><sub>📶W9 · W↑8d · ↑CMF11d</sub> | ✓ SAFE | Luxury watch retail, multi-brand, Indian affluent consumers | 📈 BULL_ANY_MID | 6 | ↑62 | ↓1.013 | ↑14d | — | +11.6% | 33.04/29.87 | -1.00% | 20% |
| [ORIENTCEM](https://in.tradingview.com/chart/?symbol=NSE:ORIENTCEM)<br><sub>📶W9 · W↑19d · ↑CMF12d</sub> | ✓ SAFE | Cement manufacturing for construction infrastructure projects | 📈 BULL_ANY_MID | 6 | ↑31 | ↑1.034 | ↑14d | — | +14.6% | 44.75/42.35 | +3.70% | 20% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>📶W9 · W↑11d · ↑CMF13d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓60 | ↓1.007 | ↑15d | — | +7.0% | 46.27/45.57 | -0.67% | 20% |
| [MINDACORP](https://in.tradingview.com/chart/?symbol=NSE:MINDACORP)<br><sub>📶W9 · W↑8d · ↑CMF15d</sub> | ✓ SAFE | Automotive components mechatronics electronics OEM supplier | 📈 BULL_ANY_MID | 3 | ↑77 | ↑1.055 | ↑17d | — | +23.5% | 37.73/34.45 | +5.46% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:PWL,NSE:BLKASHYAP,NSE:TINNARUBR,NSE:CROMPTON,NSE:LTFOODS,NSE:ENDURANCE,NSE:TVSHLTD,NSE:GABRIEL,NSE:JTEKTINDIA,NSE:SIMPLEXINF,NSE:ADVENZYMES,NSE:HESTERBIO,NSE:SIGMAADV,NSE:MARINE,NSE:UBL,NSE:SYSTMTXC,NSE:HITECH,NSE:JKCEMENT,NSE:VGUARD,NSE:TATACONSUM,NSE:NINSYS,NSE:STARHEALTH,NSE:BALAJITELE,NSE:ASKAUTOLTD,NSE:AMBUJACEM,NSE:SUNTECK,NSE:UPL,NSE:ETHOSLTD,NSE:ORIENTCEM,NSE:EICHERMOT,NSE:MINDACORP
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (52)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PWL](https://in.tradingview.com/chart/?symbol=NSE:PWL)<br><sub>📶W9 · W↑4d · 🚀SS·8x · ↓CMF10d</sub> | ✓ SAFE | Online test prep and upskilling courses for competitive exams | ⚡ BULL_ANY_PPV | 89 | 🔄75 | ↑1.043 | ↑1d | SQ·PV | +6.3% | 18.63/5.87 | +6.31% | 20% |
| [BLKASHYAP](https://in.tradingview.com/chart/?symbol=NSE:BLKASHYAP)<br><sub>📶W9 · W↑8d · RVOL141x · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | High-rise building construction EPC for residential commercial | ⚡ BULL_ANY_PPV | 89 | 🔄74 | ↑1.081 | ↑1d | SQ·PV | +12.1% | 3.29/-0.12 | +12.14% | 20% |
| [TINNARUBR](https://in.tradingview.com/chart/?symbol=NSE:TINNARUBR)<br><sub>📶W9 · W↑4d · 🚀SS·46x · ↑CMF0d</sub> | ✓ SAFE | Waste tyre recycling into crumb rubber and steel | ⚡ BULL_ANY_PPV | 49 | 🔄73 | ↑1.139 | ↑1d | PV | +19.6% | 6.88/0.21 | +19.63% | 20% |
| [CROMPTON](https://in.tradingview.com/chart/?symbol=NSE:CROMPTON)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Fans, lighting, water pumps, home electrical appliances | ⚡ BULL_ANY_PPV | 49 | 🔄21 | ↑1.037 | ↑1d | PV | +6.1% | 11.09/11.0 | +6.13% | 20% |
| [LTFOODS](https://in.tradingview.com/chart/?symbol=NSE:LTFOODS)<br><sub>📶W9 · W↑8d · 🚀SS·76x · ↓CMF0d</sub> | ✓ SAFE | Rice and rice products FMCG global consumer foods | ⚡ BULL_ANY_PPV | 37 | 🔄62 | ↑1.037 | ↑13d | PV | +11.5% | 30.27/24.5 | +4.65% | 20% |
| [ENDURANCE](https://in.tradingview.com/chart/?symbol=NSE:ENDURANCE)<br><sub>📶W9 · W↑8d · ↑CMF6d</sub> | ⚠ CAUTION | Aluminium castings, suspension, braking systems for automobiles | ⚡ BULL_ANY_PPV | 36 | 🔄41 | ↑1.034 | ↑14d | PV | +14.1% | 23.04/20.94 | +4.93% | 20% |
| [TVSHLTD](https://in.tradingview.com/chart/?symbol=NSE:TVSHLTD)<br><sub>📶W9 · W↑14d · ↑CMF15d</sub> | ⚠ CAUTION | Aluminum die castings automotive components manufacturing India | ⚡ BULL_ANY_PPV | 17 | ↑48 | ↑1.064 | ↑3d | PV | +10.6% | 25.65/21.49 | +7.47% | 5% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>📶W9 · W↑8d · ★ · ↑CMF5d</sub> | ✓ SAFE | Shock absorbers and struts for two-wheeler and four-wheeler OEMs | ⚡ BULL_ANY_PPV | 14 | ↑91 | ↑1.057 | ↑6d | PV | +12.6% | 40.6/37.13 | +6.30% | 20% |
| [JTEKTINDIA](https://in.tradingview.com/chart/?symbol=NSE:JTEKTINDIA)<br><sub>📶W9 · W↑14d · ↓CMF12d</sub> | ⚠ CAUTION | Steering systems and driveline components for automobiles | ⚡ BULL_ANY_PPV | 11 | ↑39 | ↑1.021 | ↑14d | PV | +12.1% | 30.69/30.49 | +2.25% | 20% |
| [SIMPLEXINF](https://in.tradingview.com/chart/?symbol=NSE:SIMPLEXINF)<br><sub>📶W9 · W↑29d · ↑CMF24d</sub> | ✓ SAFE | Civil construction contractor for infrastructure projects | ⚡ BULL_ANY_PPV | 7 | ↑82 | ↑1.040 | ↑13d | PV | +17.3% | 51.48/50.78 | +1.19% | 20% |
| [ADVENZYMES](https://in.tradingview.com/chart/?symbol=NSE:ADVENZYMES)<br><sub>📶W9 · W↑14d · ↑CMF5d</sub> | ✓ SAFE | Enzyme manufacturing, pharmaceuticals, food, industrial applications | ⚡ BULL_ANY_PPV | 4 | ↑40 | ↑1.045 | ↑16d | PV | +14.1% | 32.6/26.54 | +5.43% | 20% |
| [HESTERBIO](https://in.tradingview.com/chart/?symbol=NSE:HESTERBIO)<br><sub>📶W9 · W↑14d · ↓CMF12d</sub> | ⚠ CAUTION | Poultry livestock vaccines manufacturer animal healthcare sector | ⚡ BULL_ANY_PPV | 2 | ↑80 | ↓1.010 | ↑18d | PV | +14.3% | 29.85/25.55 | +0.17% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE)<br><sub>📶W9 · ↓CMF13d</sub> | n/a | Electrical automation solar solutions marine industrial sectors | 📈 BULL_ANY_MID | 94 | 🔄95 | ↑1.015 | ↑1d | SQ | +2.6% | -2.34/-3.15 | +2.60% | 20% |
| [UBL](https://in.tradingview.com/chart/?symbol=NSE:UBL)<br><sub>📶W9 · W↑19d · ↓CMF30d</sub> | ✓ SAFE | Beer manufacturer, India domestic market, Kingfisher brand leader | 📈 BULL_ANY_MID | 57 | ↑28 | ↑1.042 | ↑3d | SQ | +6.3% | 31.22/21.86 | +3.97% | 20% |
| [SYSTMTXC](https://in.tradingview.com/chart/?symbol=NSE:SYSTMTXC)<br><sub>📶W9 · W↑51d · ↓CMF20d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 53 | ↑68 | ↑1.018 | ↑12d | SQ | +7.5% | 47.39/46.26 | +1.64% | 5% |
| [HITECH](https://in.tradingview.com/chart/?symbol=NSE:HITECH)<br><sub>📶W9 · W↑14d · ↓CMF26d</sub> | ✓ SAFE | ERW steel pipes tubes construction automotive infrastructure | 📈 BULL_ANY_MID | 44 | 🔄25 | ↑1.011 | ↑16d | — | +18.5% | 17.4/17.17 | +1.64% | 20% |
| [JKCEMENT](https://in.tradingview.com/chart/?symbol=NSE:JKCEMENT)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF15d</sub> | ⚠ CAUTION | Cement manufacturing construction materials India domestic markets | 📈 BULL_ANY_MID | 41 | 🔄52 | ↑1.023 | ↑14d | — | +11.2% | 39.13/38.47 | +3.27% | 20% |
| [VGUARD](https://in.tradingview.com/chart/?symbol=NSE:VGUARD)<br><sub>📶W9 · W↑8d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | Voltage stabilizers, surge protectors, home appliances manufacturer | 📈 BULL_ANY_MID | 39 | 🔄39 | ↑1.022 | ↑16d | — | +15.1% | 22.87/22.77 | +2.95% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄55 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [NINSYS](https://in.tradingview.com/chart/?symbol=NSE:NINSYS)<br><sub>📶W9 · W↑34d · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 28 | ↑98 | ↑1.012 | ↑2d | — | +2.2% | 23.2/22.75 | +0.71% | 20% |
| [STARHEALTH](https://in.tradingview.com/chart/?symbol=NSE:STARHEALTH)<br><sub>📶W9 · W↑8d · ↓CMF13d</sub> | ✓ SAFE | Health insurance provider, retail customers, India | 📈 BULL_ANY_MID | 23 | ↑68 | ↑1.017 | ↑2d | — | +3.5% | 18.36/17.67 | +1.58% | 20% |
| [BALAJITELE](https://in.tradingview.com/chart/?symbol=NSE:BALAJITELE)<br><sub>📶W9 · W↑8d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | TV serials films digital content production entertainment | 📈 BULL_ANY_MID | 18 | ↑53 | ↑1.041 | ↑2d | — | +7.1% | 32.28/31.83 | +3.20% | 20% |
| [ASKAUTOLTD](https://in.tradingview.com/chart/?symbol=NSE:ASKAUTOLTD)<br><sub>📶W9 · W↑8d · ↑CMF10d</sub> | ✓ SAFE | Two-wheeler braking systems manufacturer India | 📈 BULL_ANY_MID | 14 | ↑85 | ↑1.018 | ↑11d | — | +10.6% | 37.11/36.69 | +1.69% | 20% |
| [AMBUJACEM](https://in.tradingview.com/chart/?symbol=NSE:AMBUJACEM)<br><sub>📶W9 · W↑19d · 🚀SS · ↓CMF17d</sub> | ✓ SAFE | Cement manufacturer, construction materials, infrastructure demand | 📈 BULL_ANY_MID | 11 | ↑24 | ↑1.028 | ↑14d | — | +14.0% | 37.7/34.93 | +3.12% | 20% |
| [SUNTECK](https://in.tradingview.com/chart/?symbol=NSE:SUNTECK)<br><sub>📶W9 · W↑19d · ↓CMF0d</sub> | ✓ SAFE | Luxury residential developer MMR premium apartments commercial | 📈 BULL_ANY_MID | 9 | ↑36 | ↑1.025 | ↑16d | — | +15.1% | 53.03/52.98 | +0.63% | 20% |
| [UPL](https://in.tradingview.com/chart/?symbol=NSE:UPL)<br><sub>📶W9 · W↑19d · ↑CMF17d</sub> | ✓ SAFE | Agrochemicals pesticides seeds fertilizers global agribusiness | 📈 BULL_ANY_MID | 8 | ↑26 | ↑1.033 | ↑12d | — | +10.0% | 46.46/44.3 | +3.22% | 20% |
| [ETHOSLTD](https://in.tradingview.com/chart/?symbol=NSE:ETHOSLTD)<br><sub>📶W9 · W↑8d · ↑CMF11d</sub> | ✓ SAFE | Luxury watch retail, multi-brand, Indian affluent consumers | 📈 BULL_ANY_MID | 6 | ↑62 | ↓1.013 | ↑14d | — | +11.6% | 33.04/29.87 | -1.00% | 20% |
| [ORIENTCEM](https://in.tradingview.com/chart/?symbol=NSE:ORIENTCEM)<br><sub>📶W9 · W↑19d · ↑CMF12d</sub> | ✓ SAFE | Cement manufacturing for construction infrastructure projects | 📈 BULL_ANY_MID | 6 | ↑31 | ↑1.034 | ↑14d | — | +14.6% | 44.75/42.35 | +3.70% | 20% |
| [MINDACORP](https://in.tradingview.com/chart/?symbol=NSE:MINDACORP)<br><sub>📶W9 · W↑8d · ↑CMF15d</sub> | ✓ SAFE | Automotive components mechatronics electronics OEM supplier | 📈 BULL_ANY_MID | 3 | ↑77 | ↑1.055 | ↑17d | — | +23.5% | 37.73/34.45 | +5.46% | 20% |
| [DLINKINDIA](https://in.tradingview.com/chart/?symbol=NSE:DLINKINDIA)<br><sub>W↑4d · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Networking equipment distribution, consumer and enterprise markets | ⚡ BULL_ANY_PPV | 99 | 🔄40 | ↑1.012 | ↑1d | SQ·PV | +3.0% | 3.7/3.29 | +2.99% | 20% |
| [ASHAPURMIN](https://in.tradingview.com/chart/?symbol=NSE:ASHAPURMIN)<br><sub>↑CMF0d · ÷DIV</sub> | ✓ SAFE | Bauxite mining processing distribution industrial minerals global | ⚡ BULL_ANY_PPV | 94 | 🔄4 | ↑1.026 | ↑1d | SQ·PV | +5.4% | -44.04/-50.23 | +5.41% | 20% |
| [TATATECH](https://in.tradingview.com/chart/?symbol=NSE:TATATECH)<br><sub>RVOL17x · ↑CMF0d</sub> | ✓ SAFE | Engineering services, product development, automotive manufacturing sector | ⚡ BULL_ANY_PPV | 89 | 🔄52 | ↑1.046 | ↑1d | SQ·PV | +7.2% | -10.31/-16.64 | +7.16% | 20% |
| [IPL](https://in.tradingview.com/chart/?symbol=NSE:IPL)<br><sub>W↑4d · RVOL230x · ↑CMF0d</sub> | ✓ SAFE | Agrochemical manufacturer crop protection pesticides farming | ⚡ BULL_ANY_PPV | 89 | 🔄14 | ↑1.049 | ↑1d | SQ·PV | +8.1% | -14.93/-22.36 | +8.05% | 20% |
| [AMBER](https://in.tradingview.com/chart/?symbol=NSE:AMBER)<br><sub>W↑8d · 🚀SS · ↑CMF4d · ÷DIV</sub> | ✓ SAFE | Room air conditioner manufacturing and electronics contract services provider | ⚡ BULL_ANY_PPV | 49 | 🔄34 | ↑1.050 | ↑1d | PV | +7.4% | -2.24/-7.83 | +7.38% | 20% |
| [ASHIKAG](https://in.tradingview.com/chart/?symbol=NSE:ASHIKAG)<br><sub>🚀SS · ↓CMF28d · 🎯SLING</sub> | ⚠ CAUTION | NBFC credit financing and securities broking platform | 🟢 BULL_OVERSOLD | 94 | 🔄50 | ↑1.017 | ↑1d | SQ | +5.6% | -57.59/-60.53 | +5.56% | 20% |
| [PNCINFRA](https://in.tradingview.com/chart/?symbol=NSE:PNCINFRA)<br><sub>W↑4d · ↓CMF26d</sub> | ✓ SAFE | Highway and water infrastructure construction contractor | 📈 BULL_ANY_MID | 99 | 🔄2 | ↑1.008 | ↑1d | SQ | +2.1% | -30.67/-34.21 | +2.07% | 20% |
| [BAJAJELEC](https://in.tradingview.com/chart/?symbol=NSE:BAJAJELEC)<br><sub>↓CMF30d</sub> | ✓ SAFE | Electrical appliances fans lighting wiring for homes | 📈 BULL_ANY_MID | 99 | 🔄10 | ↑1.011 | ↑1d | SQ | +1.9% | -13.71/-17.26 | +1.85% | 20% |
| [HNDFDS](https://in.tradingview.com/chart/?symbol=NSE:HNDFDS)<br><sub>↑CMF30d · ÷DIV</sub> | ⚠ CAUTION | Contract manufacturer FMCG food home care beverages | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.009 | ↑1d | SQ | +2.7% | -39.58/-41.08 | +2.68% | 20% |
| [SIGNPOST](https://in.tradingview.com/chart/?symbol=NSE:SIGNPOST)<br><sub>↓CMF30d · ÷DIV</sub> | ✓ SAFE | DOOH advertising networks buses metros transit spaces | 📈 BULL_ANY_MID | 94 | 🔄31 | ↑1.016 | ↑1d | SQ | +3.8% | -42.06/-43.88 | +3.83% | 20% |
| [SOMANYCERA](https://in.tradingview.com/chart/?symbol=NSE:SOMANYCERA)<br><sub>↓CMF10d · ⚠️TRAP</sub> | ✓ SAFE | Ceramic tiles sanitaryware bath fittings residential commercial construction | 📈 BULL_ANY_MID | 69 | ↑73 | ↑1.009 | ↑1d | SQ | +0.7% | -42.22/-48.8 | +0.66% | 20% |
| [COHANCE](https://in.tradingview.com/chart/?symbol=NSE:COHANCE)<br><sub>↑CMF8d</sub> | ✓ SAFE | Pharmaceutical CDMO development manufacturing APIs formulations specialty chemicals | 📈 BULL_ANY_MID | 68 | ↑67 | ↑1.008 | ↑2d | SQ | +1.7% | 4.73/4.67 | +0.67% | 20% |
| [MAHSCOOTER](https://in.tradingview.com/chart/?symbol=NSE:MAHSCOOTER)<br><sub>↑CMF1d · ⚠️TRAP</sub> | ⚠ CAUTION | Dies, jigs, fixtures, die casting automotive components manufacturer | 📈 BULL_ANY_MID | 68 | ↑32 | ↑1.007 | ↑2d | SQ | +1.2% | -15.81/-21.86 | +0.82% | 5% |
| [SKFINDUS](https://in.tradingview.com/chart/?symbol=NSE:SKFINDUS)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Bearings seals lubrication systems industrial machinery | 📈 BULL_ANY_MID | 63 | ↑50 | ↑1.027 | ↑2d | SQ | +5.2% | -10.06/-15.48 | +3.01% | 20% |
| [MMP](https://in.tradingview.com/chart/?symbol=NSE:MMP)<br><sub>★ · ↓CMF13d</sub> | ✓ SAFE | Aluminium powder manufacturer for industrial coatings paints | 📈 BULL_ANY_MID | 63 | ↑94 | ↑1.018 | ↑2d | SQ | +3.1% | -5.41/-9.29 | +1.23% | 20% |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY)<br><sub>↓CMF12d</sub> | ✓ SAFE | Precision plastic injection molded components for automotive OEMs | 📈 BULL_ANY_MID | 60 | ↑77 | ↑1.010 | ↑10d | SQ | +5.3% | 15.67/15.56 | +0.99% | 20% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>↓CMF14d</sub> | ✓ SAFE | Electronics manufacturing, product design, assembly, testing services | 📈 BULL_ANY_MID | 54 | 🔄92 | ↑1.017 | ↑1d | — | +2.9% | -34.67/-37.73 | +2.85% | -% |
| [SRF](https://in.tradingview.com/chart/?symbol=NSE:SRF)<br><sub>W↑8d · 🚀SS · ↑CMF20d</sub> | ⚠ CAUTION | Technical textiles, films, chemicals for automotive, industrial, packaging | 📈 BULL_ANY_MID | 54 | 🔄41 | ↑1.018 | ↑1d | — | +2.8% | 18.38/16.79 | +2.82% | 20% |
| [HATSUN](https://in.tradingview.com/chart/?symbol=NSE:HATSUN)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Dairy milk products manufacturing and processing company | 📈 BULL_ANY_MID | 54 | 🔄67 | ↑1.016 | ↑1d | — | +2.5% | -12.91/-16.46 | +2.48% | 20% |
| [KAJARIACER](https://in.tradingview.com/chart/?symbol=NSE:KAJARIACER)<br><sub>W↑4d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Ceramic and vitrified tiles manufacturer for construction | 📈 BULL_ANY_MID | 53 | 🔄67 | ↑1.015 | ↑2d | — | +2.9% | 1.74/0.27 | +1.93% | 20% |
| [SAGCEM](https://in.tradingview.com/chart/?symbol=NSE:SAGCEM)<br><sub>W↑14d · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Cement manufacturing, South and Central India construction | 📈 BULL_ANY_MID | 17 | ↑9 | ↑1.008 | ↑13d | — | +11.8% | 10.57/9.61 | +0.51% | 20% |
| [AMRUTANJAN](https://in.tradingview.com/chart/?symbol=NSE:AMRUTANJAN)<br><sub>W↑14d · ↓CMF22d</sub> | ⚠ CAUTION | Ayurvedic balm pain relief and OTC consumer healthcare products | 📈 BULL_ANY_MID | 7 | ↑34 | ↓1.010 | ↑13d | — | +4.2% | 19.71/16.45 | +0.13% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:PWL,NSE:BLKASHYAP,NSE:TINNARUBR,NSE:CROMPTON,NSE:LTFOODS,NSE:ENDURANCE,NSE:TVSHLTD,NSE:GABRIEL,NSE:JTEKTINDIA,NSE:SIMPLEXINF,NSE:ADVENZYMES,NSE:HESTERBIO,NSE:SIGMAADV,NSE:MARINE,NSE:UBL,NSE:SYSTMTXC,NSE:HITECH,NSE:JKCEMENT,NSE:VGUARD,NSE:TATACONSUM,NSE:NINSYS,NSE:STARHEALTH,NSE:BALAJITELE,NSE:ASKAUTOLTD,NSE:AMBUJACEM,NSE:SUNTECK,NSE:UPL,NSE:ETHOSLTD,NSE:ORIENTCEM,NSE:MINDACORP,NSE:DLINKINDIA,NSE:ASHAPURMIN,NSE:TATATECH,NSE:IPL,NSE:AMBER,NSE:ASHIKAG,NSE:PNCINFRA,NSE:BAJAJELEC,NSE:HNDFDS,NSE:SIGNPOST,NSE:SOMANYCERA,NSE:COHANCE,NSE:MAHSCOOTER,NSE:SKFINDUS,NSE:MMP,NSE:SHAILY,NSE:SYRMA,NSE:SRF,NSE:HATSUN,NSE:KAJARIACER,NSE:SAGCEM,NSE:AMRUTANJAN
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (22)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PWL](https://in.tradingview.com/chart/?symbol=NSE:PWL)<br><sub>📶W9 · W↑4d · 🚀SS·8x · ↓CMF10d</sub> | ✓ SAFE | Online test prep and upskilling courses for competitive exams | ⚡ BULL_ANY_PPV | 89 | 🔄75 | ↑1.043 | ↑1d | SQ·PV | +6.3% | 18.63/5.87 | +6.31% | 20% |
| [BLKASHYAP](https://in.tradingview.com/chart/?symbol=NSE:BLKASHYAP)<br><sub>📶W9 · W↑8d · RVOL141x · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | High-rise building construction EPC for residential commercial | ⚡ BULL_ANY_PPV | 89 | 🔄74 | ↑1.081 | ↑1d | SQ·PV | +12.1% | 3.29/-0.12 | +12.14% | 20% |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE)<br><sub>📶W9 · ↓CMF13d</sub> | n/a | Electrical automation solar solutions marine industrial sectors | 📈 BULL_ANY_MID | 94 | 🔄95 | ↑1.015 | ↑1d | SQ | +2.6% | -2.34/-3.15 | +2.60% | 20% |
| [UBL](https://in.tradingview.com/chart/?symbol=NSE:UBL)<br><sub>📶W9 · W↑19d · ↓CMF30d</sub> | ✓ SAFE | Beer manufacturer, India domestic market, Kingfisher brand leader | 📈 BULL_ANY_MID | 57 | ↑28 | ↑1.042 | ↑3d | SQ | +6.3% | 31.22/21.86 | +3.97% | 20% |
| [SYSTMTXC](https://in.tradingview.com/chart/?symbol=NSE:SYSTMTXC)<br><sub>📶W9 · W↑51d · ↓CMF20d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 53 | ↑68 | ↑1.018 | ↑12d | SQ | +7.5% | 47.39/46.26 | +1.64% | 5% |
| [DLINKINDIA](https://in.tradingview.com/chart/?symbol=NSE:DLINKINDIA)<br><sub>W↑4d · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Networking equipment distribution, consumer and enterprise markets | ⚡ BULL_ANY_PPV | 99 | 🔄40 | ↑1.012 | ↑1d | SQ·PV | +3.0% | 3.7/3.29 | +2.99% | 20% |
| [ASHAPURMIN](https://in.tradingview.com/chart/?symbol=NSE:ASHAPURMIN)<br><sub>↑CMF0d · ÷DIV</sub> | ✓ SAFE | Bauxite mining processing distribution industrial minerals global | ⚡ BULL_ANY_PPV | 94 | 🔄4 | ↑1.026 | ↑1d | SQ·PV | +5.4% | -44.04/-50.23 | +5.41% | 20% |
| [TATATECH](https://in.tradingview.com/chart/?symbol=NSE:TATATECH)<br><sub>RVOL17x · ↑CMF0d</sub> | ✓ SAFE | Engineering services, product development, automotive manufacturing sector | ⚡ BULL_ANY_PPV | 89 | 🔄52 | ↑1.046 | ↑1d | SQ·PV | +7.2% | -10.31/-16.64 | +7.16% | 20% |
| [IPL](https://in.tradingview.com/chart/?symbol=NSE:IPL)<br><sub>W↑4d · RVOL230x · ↑CMF0d</sub> | ✓ SAFE | Agrochemical manufacturer crop protection pesticides farming | ⚡ BULL_ANY_PPV | 89 | 🔄14 | ↑1.049 | ↑1d | SQ·PV | +8.1% | -14.93/-22.36 | +8.05% | 20% |
| [ASHIKAG](https://in.tradingview.com/chart/?symbol=NSE:ASHIKAG)<br><sub>🚀SS · ↓CMF28d · 🎯SLING</sub> | ⚠ CAUTION | NBFC credit financing and securities broking platform | 🟢 BULL_OVERSOLD | 94 | 🔄50 | ↑1.017 | ↑1d | SQ | +5.6% | -57.59/-60.53 | +5.56% | 20% |
| [PNCINFRA](https://in.tradingview.com/chart/?symbol=NSE:PNCINFRA)<br><sub>W↑4d · ↓CMF26d</sub> | ✓ SAFE | Highway and water infrastructure construction contractor | 📈 BULL_ANY_MID | 99 | 🔄2 | ↑1.008 | ↑1d | SQ | +2.1% | -30.67/-34.21 | +2.07% | 20% |
| [BAJAJELEC](https://in.tradingview.com/chart/?symbol=NSE:BAJAJELEC)<br><sub>↓CMF30d</sub> | ✓ SAFE | Electrical appliances fans lighting wiring for homes | 📈 BULL_ANY_MID | 99 | 🔄10 | ↑1.011 | ↑1d | SQ | +1.9% | -13.71/-17.26 | +1.85% | 20% |
| [HNDFDS](https://in.tradingview.com/chart/?symbol=NSE:HNDFDS)<br><sub>↑CMF30d · ÷DIV</sub> | ⚠ CAUTION | Contract manufacturer FMCG food home care beverages | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.009 | ↑1d | SQ | +2.7% | -39.58/-41.08 | +2.68% | 20% |
| [SIGNPOST](https://in.tradingview.com/chart/?symbol=NSE:SIGNPOST)<br><sub>↓CMF30d · ÷DIV</sub> | ✓ SAFE | DOOH advertising networks buses metros transit spaces | 📈 BULL_ANY_MID | 94 | 🔄31 | ↑1.016 | ↑1d | SQ | +3.8% | -42.06/-43.88 | +3.83% | 20% |
| [SOMANYCERA](https://in.tradingview.com/chart/?symbol=NSE:SOMANYCERA)<br><sub>↓CMF10d · ⚠️TRAP</sub> | ✓ SAFE | Ceramic tiles sanitaryware bath fittings residential commercial construction | 📈 BULL_ANY_MID | 69 | ↑73 | ↑1.009 | ↑1d | SQ | +0.7% | -42.22/-48.8 | +0.66% | 20% |
| [COHANCE](https://in.tradingview.com/chart/?symbol=NSE:COHANCE)<br><sub>↑CMF8d</sub> | ✓ SAFE | Pharmaceutical CDMO development manufacturing APIs formulations specialty chemicals | 📈 BULL_ANY_MID | 68 | ↑67 | ↑1.008 | ↑2d | SQ | +1.7% | 4.73/4.67 | +0.67% | 20% |
| [MAHSCOOTER](https://in.tradingview.com/chart/?symbol=NSE:MAHSCOOTER)<br><sub>↑CMF1d · ⚠️TRAP</sub> | ⚠ CAUTION | Dies, jigs, fixtures, die casting automotive components manufacturer | 📈 BULL_ANY_MID | 68 | ↑32 | ↑1.007 | ↑2d | SQ | +1.2% | -15.81/-21.86 | +0.82% | 5% |
| [SKFINDUS](https://in.tradingview.com/chart/?symbol=NSE:SKFINDUS)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Bearings seals lubrication systems industrial machinery | 📈 BULL_ANY_MID | 63 | ↑50 | ↑1.027 | ↑2d | SQ | +5.2% | -10.06/-15.48 | +3.01% | 20% |
| [MMP](https://in.tradingview.com/chart/?symbol=NSE:MMP)<br><sub>★ · ↓CMF13d</sub> | ✓ SAFE | Aluminium powder manufacturer for industrial coatings paints | 📈 BULL_ANY_MID | 63 | ↑94 | ↑1.018 | ↑2d | SQ | +3.1% | -5.41/-9.29 | +1.23% | 20% |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY)<br><sub>↓CMF12d</sub> | ✓ SAFE | Precision plastic injection molded components for automotive OEMs | 📈 BULL_ANY_MID | 60 | ↑77 | ↑1.010 | ↑10d | SQ | +5.3% | 15.67/15.56 | +0.99% | 20% |
| [VIDHIING](https://in.tradingview.com/chart/?symbol=NSE:VIDHIING)<br><sub>🚀SS · ↓CMF19d · ⚠️TRAP · ÷DIV</sub> | ⚠ CAUTION | Food grade colors manufacturer serving F&B pharma confectionery | 📈 BULL_ANY_MID | 54 | ↓39 | ↑0.996 | ↓11d | SQ | -3.3% | -47.99/-48.05 | +0.74% | 20% |
| [EIHAHOTELS](https://in.tradingview.com/chart/?symbol=NSE:EIHAHOTELS)<br><sub>W↑8d · ↓CMF17d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 52 | ↓34 | ↓1.000 | ↑8d | SQ | +2.0% | 11.25/11.18 | -0.72% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:PWL,NSE:BLKASHYAP,NSE:MARINE,NSE:UBL,NSE:SYSTMTXC,NSE:DLINKINDIA,NSE:ASHAPURMIN,NSE:TATATECH,NSE:IPL,NSE:ASHIKAG,NSE:PNCINFRA,NSE:BAJAJELEC,NSE:HNDFDS,NSE:SIGNPOST,NSE:SOMANYCERA,NSE:COHANCE,NSE:MAHSCOOTER,NSE:SKFINDUS,NSE:MMP,NSE:SHAILY,NSE:VIDHIING,NSE:EIHAHOTELS
```

---

### 🔥 MAJOR — PPV confirmed (12)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [TINNARUBR](https://in.tradingview.com/chart/?symbol=NSE:TINNARUBR)<br><sub>📶W9 · W↑4d · 🚀SS·46x · ↑CMF0d</sub> | ✓ SAFE | Waste tyre recycling into crumb rubber and steel | ⚡ BULL_ANY_PPV | 49 | 🔄73 | ↑1.139 | ↑1d | PV | +19.6% | 6.88/0.21 | +19.63% | 20% |
| [CROMPTON](https://in.tradingview.com/chart/?symbol=NSE:CROMPTON)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Fans, lighting, water pumps, home electrical appliances | ⚡ BULL_ANY_PPV | 49 | 🔄21 | ↑1.037 | ↑1d | PV | +6.1% | 11.09/11.0 | +6.13% | 20% |
| [LTFOODS](https://in.tradingview.com/chart/?symbol=NSE:LTFOODS)<br><sub>📶W9 · W↑8d · 🚀SS·76x · ↓CMF0d</sub> | ✓ SAFE | Rice and rice products FMCG global consumer foods | ⚡ BULL_ANY_PPV | 37 | 🔄62 | ↑1.037 | ↑13d | PV | +11.5% | 30.27/24.5 | +4.65% | 20% |
| [ENDURANCE](https://in.tradingview.com/chart/?symbol=NSE:ENDURANCE)<br><sub>📶W9 · W↑8d · ↑CMF6d</sub> | ⚠ CAUTION | Aluminium castings, suspension, braking systems for automobiles | ⚡ BULL_ANY_PPV | 36 | 🔄41 | ↑1.034 | ↑14d | PV | +14.1% | 23.04/20.94 | +4.93% | 20% |
| [TVSHLTD](https://in.tradingview.com/chart/?symbol=NSE:TVSHLTD)<br><sub>📶W9 · W↑14d · ↑CMF15d</sub> | ⚠ CAUTION | Aluminum die castings automotive components manufacturing India | ⚡ BULL_ANY_PPV | 17 | ↑48 | ↑1.064 | ↑3d | PV | +10.6% | 25.65/21.49 | +7.47% | 5% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>📶W9 · W↑8d · ★ · ↑CMF5d</sub> | ✓ SAFE | Shock absorbers and struts for two-wheeler and four-wheeler OEMs | ⚡ BULL_ANY_PPV | 14 | ↑91 | ↑1.057 | ↑6d | PV | +12.6% | 40.6/37.13 | +6.30% | 20% |
| [JTEKTINDIA](https://in.tradingview.com/chart/?symbol=NSE:JTEKTINDIA)<br><sub>📶W9 · W↑14d · ↓CMF12d</sub> | ⚠ CAUTION | Steering systems and driveline components for automobiles | ⚡ BULL_ANY_PPV | 11 | ↑39 | ↑1.021 | ↑14d | PV | +12.1% | 30.69/30.49 | +2.25% | 20% |
| [SIMPLEXINF](https://in.tradingview.com/chart/?symbol=NSE:SIMPLEXINF)<br><sub>📶W9 · W↑29d · ↑CMF24d</sub> | ✓ SAFE | Civil construction contractor for infrastructure projects | ⚡ BULL_ANY_PPV | 7 | ↑82 | ↑1.040 | ↑13d | PV | +17.3% | 51.48/50.78 | +1.19% | 20% |
| [ADVENZYMES](https://in.tradingview.com/chart/?symbol=NSE:ADVENZYMES)<br><sub>📶W9 · W↑14d · ↑CMF5d</sub> | ✓ SAFE | Enzyme manufacturing, pharmaceuticals, food, industrial applications | ⚡ BULL_ANY_PPV | 4 | ↑40 | ↑1.045 | ↑16d | PV | +14.1% | 32.6/26.54 | +5.43% | 20% |
| [HESTERBIO](https://in.tradingview.com/chart/?symbol=NSE:HESTERBIO)<br><sub>📶W9 · W↑14d · ↓CMF12d</sub> | ⚠ CAUTION | Poultry livestock vaccines manufacturer animal healthcare sector | ⚡ BULL_ANY_PPV | 2 | ↑80 | ↓1.010 | ↑18d | PV | +14.3% | 29.85/25.55 | +0.17% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [AMBER](https://in.tradingview.com/chart/?symbol=NSE:AMBER)<br><sub>W↑8d · 🚀SS · ↑CMF4d · ÷DIV</sub> | ✓ SAFE | Room air conditioner manufacturing and electronics contract services provider | ⚡ BULL_ANY_PPV | 49 | 🔄34 | ↑1.050 | ↑1d | PV | +7.4% | -2.24/-7.83 | +7.38% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:TINNARUBR,NSE:CROMPTON,NSE:LTFOODS,NSE:ENDURANCE,NSE:TVSHLTD,NSE:GABRIEL,NSE:JTEKTINDIA,NSE:SIMPLEXINF,NSE:ADVENZYMES,NSE:HESTERBIO,NSE:SIGMAADV,NSE:AMBER
```

### 🟢 OVERSOLD — reversal from −53/−60 (1)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [TEAMLEASE](https://in.tradingview.com/chart/?symbol=NSE:TEAMLEASE)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Staffing recruitment payroll HR services employer solutions | 🟡 BULL_OS_L2 | 13 | ↓7 | ↑0.995 | ↓12d | — | -7.9% | -54.86/-56.7 | +1.77% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:TEAMLEASE
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (26)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [HITECH](https://in.tradingview.com/chart/?symbol=NSE:HITECH)<br><sub>📶W9 · W↑14d · ↓CMF26d</sub> | ✓ SAFE | ERW steel pipes tubes construction automotive infrastructure | 📈 BULL_ANY_MID | 44 | 🔄25 | ↑1.011 | ↑16d | — | +18.5% | 17.4/17.17 | +1.64% | 20% |
| [JKCEMENT](https://in.tradingview.com/chart/?symbol=NSE:JKCEMENT)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF15d</sub> | ⚠ CAUTION | Cement manufacturing construction materials India domestic markets | 📈 BULL_ANY_MID | 41 | 🔄52 | ↑1.023 | ↑14d | — | +11.2% | 39.13/38.47 | +3.27% | 20% |
| [VGUARD](https://in.tradingview.com/chart/?symbol=NSE:VGUARD)<br><sub>📶W9 · W↑8d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | Voltage stabilizers, surge protectors, home appliances manufacturer | 📈 BULL_ANY_MID | 39 | 🔄39 | ↑1.022 | ↑16d | — | +15.1% | 22.87/22.77 | +2.95% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄55 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [NINSYS](https://in.tradingview.com/chart/?symbol=NSE:NINSYS)<br><sub>📶W9 · W↑34d · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 28 | ↑98 | ↑1.012 | ↑2d | — | +2.2% | 23.2/22.75 | +0.71% | 20% |
| [STARHEALTH](https://in.tradingview.com/chart/?symbol=NSE:STARHEALTH)<br><sub>📶W9 · W↑8d · ↓CMF13d</sub> | ✓ SAFE | Health insurance provider, retail customers, India | 📈 BULL_ANY_MID | 23 | ↑68 | ↑1.017 | ↑2d | — | +3.5% | 18.36/17.67 | +1.58% | 20% |
| [BALAJITELE](https://in.tradingview.com/chart/?symbol=NSE:BALAJITELE)<br><sub>📶W9 · W↑8d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | TV serials films digital content production entertainment | 📈 BULL_ANY_MID | 18 | ↑53 | ↑1.041 | ↑2d | — | +7.1% | 32.28/31.83 | +3.20% | 20% |
| [ASKAUTOLTD](https://in.tradingview.com/chart/?symbol=NSE:ASKAUTOLTD)<br><sub>📶W9 · W↑8d · ↑CMF10d</sub> | ✓ SAFE | Two-wheeler braking systems manufacturer India | 📈 BULL_ANY_MID | 14 | ↑85 | ↑1.018 | ↑11d | — | +10.6% | 37.11/36.69 | +1.69% | 20% |
| [AMBUJACEM](https://in.tradingview.com/chart/?symbol=NSE:AMBUJACEM)<br><sub>📶W9 · W↑19d · 🚀SS · ↓CMF17d</sub> | ✓ SAFE | Cement manufacturer, construction materials, infrastructure demand | 📈 BULL_ANY_MID | 11 | ↑24 | ↑1.028 | ↑14d | — | +14.0% | 37.7/34.93 | +3.12% | 20% |
| [SUNTECK](https://in.tradingview.com/chart/?symbol=NSE:SUNTECK)<br><sub>📶W9 · W↑19d · ↓CMF0d</sub> | ✓ SAFE | Luxury residential developer MMR premium apartments commercial | 📈 BULL_ANY_MID | 9 | ↑36 | ↑1.025 | ↑16d | — | +15.1% | 53.03/52.98 | +0.63% | 20% |
| [UPL](https://in.tradingview.com/chart/?symbol=NSE:UPL)<br><sub>📶W9 · W↑19d · ↑CMF17d</sub> | ✓ SAFE | Agrochemicals pesticides seeds fertilizers global agribusiness | 📈 BULL_ANY_MID | 8 | ↑26 | ↑1.033 | ↑12d | — | +10.0% | 46.46/44.3 | +3.22% | 20% |
| [ETHOSLTD](https://in.tradingview.com/chart/?symbol=NSE:ETHOSLTD)<br><sub>📶W9 · W↑8d · ↑CMF11d</sub> | ✓ SAFE | Luxury watch retail, multi-brand, Indian affluent consumers | 📈 BULL_ANY_MID | 6 | ↑62 | ↓1.013 | ↑14d | — | +11.6% | 33.04/29.87 | -1.00% | 20% |
| [ORIENTCEM](https://in.tradingview.com/chart/?symbol=NSE:ORIENTCEM)<br><sub>📶W9 · W↑19d · ↑CMF12d</sub> | ✓ SAFE | Cement manufacturing for construction infrastructure projects | 📈 BULL_ANY_MID | 6 | ↑31 | ↑1.034 | ↑14d | — | +14.6% | 44.75/42.35 | +3.70% | 20% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>📶W9 · W↑11d · ↑CMF13d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓60 | ↓1.007 | ↑15d | — | +7.0% | 46.27/45.57 | -0.67% | 20% |
| [MINDACORP](https://in.tradingview.com/chart/?symbol=NSE:MINDACORP)<br><sub>📶W9 · W↑8d · ↑CMF15d</sub> | ✓ SAFE | Automotive components mechatronics electronics OEM supplier | 📈 BULL_ANY_MID | 3 | ↑77 | ↑1.055 | ↑17d | — | +23.5% | 37.73/34.45 | +5.46% | 20% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>↓CMF14d</sub> | ✓ SAFE | Electronics manufacturing, product design, assembly, testing services | 📈 BULL_ANY_MID | 54 | 🔄92 | ↑1.017 | ↑1d | — | +2.9% | -34.67/-37.73 | +2.85% | -% |
| [SRF](https://in.tradingview.com/chart/?symbol=NSE:SRF)<br><sub>W↑8d · 🚀SS · ↑CMF20d</sub> | ⚠ CAUTION | Technical textiles, films, chemicals for automotive, industrial, packaging | 📈 BULL_ANY_MID | 54 | 🔄41 | ↑1.018 | ↑1d | — | +2.8% | 18.38/16.79 | +2.82% | 20% |
| [HATSUN](https://in.tradingview.com/chart/?symbol=NSE:HATSUN)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Dairy milk products manufacturing and processing company | 📈 BULL_ANY_MID | 54 | 🔄67 | ↑1.016 | ↑1d | — | +2.5% | -12.91/-16.46 | +2.48% | 20% |
| [KAJARIACER](https://in.tradingview.com/chart/?symbol=NSE:KAJARIACER)<br><sub>W↑4d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Ceramic and vitrified tiles manufacturer for construction | 📈 BULL_ANY_MID | 53 | 🔄67 | ↑1.015 | ↑2d | — | +2.9% | 1.74/0.27 | +1.93% | 20% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>↓CMF16d · ⚠️TRAP</sub> | ✓ SAFE | Used car marketplace and financing platform India | 📈 BULL_ANY_MID | 29 | ↓67 | ↑1.002 | ↑1d | — | +0.5% | -10.17/-11.68 | +0.50% | 20% |
| [SAGCEM](https://in.tradingview.com/chart/?symbol=NSE:SAGCEM)<br><sub>W↑14d · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Cement manufacturing, South and Central India construction | 📈 BULL_ANY_MID | 17 | ↑9 | ↑1.008 | ↑13d | — | +11.8% | 10.57/9.61 | +0.51% | 20% |
| [KRN](https://in.tradingview.com/chart/?symbol=NSE:KRN)<br><sub>🚀SS · ↑CMF5d · ÷DIV</sub> | ✓ SAFE | Heat exchanger manufacturer HVAC refrigeration OEM supplier | 📈 BULL_ANY_MID | 14 | ↓38 | ↑1.001 | ↓16d | — | -15.5% | -45.2/-45.24 | +4.73% | 5% 🟥 |
| [NRBBEARING](https://in.tradingview.com/chart/?symbol=NSE:NRBBEARING)<br><sub>🚀SS · ↓CMF24d</sub> | ✓ SAFE | Needle roller bearings manufacturer automotive industrial applications | 📈 BULL_ANY_MID | 13 | ↓80 | ↑0.996 | ↓12d | — | -6.9% | -45.0/-46.53 | +2.05% | 20% |
| [CYIENT](https://in.tradingview.com/chart/?symbol=NSE:CYIENT)<br><sub>↓CMF15d</sub> | ✓ SAFE | Engineering services, design, manufacturing digital transformation | 📈 BULL_ANY_MID | 10 | ↓71 | ↑1.005 | ↓20d | — | -2.9% | -32.08/-32.2 | +2.26% | 20% |
| [VADILALIND](https://in.tradingview.com/chart/?symbol=NSE:VADILALIND)<br><sub>↑CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Ice cream and frozen desserts manufacturer, Indian consumer market | 📈 BULL_ANY_MID | 7 | ↓83 | ↑1.000 | ↓18d | — | +1.7% | -38.93/-39.46 | +0.74% | 20% |
| [AMRUTANJAN](https://in.tradingview.com/chart/?symbol=NSE:AMRUTANJAN)<br><sub>W↑14d · ↓CMF22d</sub> | ⚠ CAUTION | Ayurvedic balm pain relief and OTC consumer healthcare products | 📈 BULL_ANY_MID | 7 | ↑34 | ↓1.010 | ↑13d | — | +4.2% | 19.71/16.45 | +0.13% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:HITECH,NSE:JKCEMENT,NSE:VGUARD,NSE:TATACONSUM,NSE:NINSYS,NSE:STARHEALTH,NSE:BALAJITELE,NSE:ASKAUTOLTD,NSE:AMBUJACEM,NSE:SUNTECK,NSE:UPL,NSE:ETHOSLTD,NSE:ORIENTCEM,NSE:EICHERMOT,NSE:MINDACORP,NSE:SYRMA,NSE:SRF,NSE:HATSUN,NSE:KAJARIACER,NSE:CARTRADE,NSE:SAGCEM,NSE:KRN,NSE:NRBBEARING,NSE:CYIENT,NSE:VADILALIND,NSE:AMRUTANJAN
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
