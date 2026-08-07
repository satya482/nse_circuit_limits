> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-08-07
*Generated 2026-08-07 15:45 IST*

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

**Total bull crosses today: 45** · 15 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,###WATCHLIST,NSE:MANORAMA,NSE:LLOYDSENGG,NSE:AKUMS,NSE:DIGITIDE,NSE:PGEL,NSE:PWL,NSE:SUNDROP,NSE:SAIPARENT,NSE:MEDANTA,NSE:TFCILTD,NSE:WEL,NSE:LLOYDSENT,NSE:SUMICHEM,NSE:GOODLUCK,NSE:OFSS,NSE:WENDT,NSE:BECTORFOOD,NSE:GANDHAR,NSE:NESTLEIND,NSE:UFLEX,NSE:TMB,NSE:SMSPHARMA,NSE:BEML,NSE:EMBDL,NSE:MBEL,NSE:TATACHEM,NSE:NUCLEUS,NSE:ASTEC,NSE:VBL,NSE:POWERINDIA,NSE:HGS,NSE:GODREJCP,NSE:GRSE,NSE:GMRP&UI,NSE:V2RETAIL,NSE:CMPDI,NSE:ANANDRATHI,NSE:JSWCEMENT,NSE:ADANIPORTS,NSE:HOMEFIRST,NSE:ZOTA,NSE:OMAXE,NSE:PURVA,NSE:ASIANTILES,NSE:ERIS
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (21)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MANORAMA](https://in.tradingview.com/chart/?symbol=NSE:MANORAMA)<br><sub>📶W9 · W↑50d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Specialty fats, butters from tree seeds, chocolate cosmetics | ⚡ BULL_ANY_PPV | 98 | 🔄72 | ↑1.009 | ↑2d | SQ·PV | +1.8% | 35.92/32.73 | +0.76% | 20% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>📶W9 · W↑88d · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | Heavy equipment manufacturing for oil gas power plants | ⚡ BULL_ANY_PPV | 89 | 🔄91 | ↑1.059 | ↑1d | SQ·PV | +9.5% | 48.0/42.69 | +9.52% | 20% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ✓ SAFE | CDMO formulation development manufacturing pharmaceuticals India exports | ⚡ BULL_ANY_PPV | 89 | 🔄87 | ↑1.035 | ↑1d | SQ·PV | +5.3% | 14.01/10.6 | +5.27% | 20% |
| [DIGITIDE](https://in.tradingview.com/chart/?symbol=NSE:DIGITIDE)<br><sub>📶W9 · W↑40d · ↓CMF4d</sub> | ✓ SAFE | AI-driven digital transformation, BPM, enterprise services | ⚡ BULL_ANY_PPV | 89 | 🔄13 | ↑1.031 | ↑1d | SQ·PV | +4.7% | 1.77/-3.89 | +4.69% | 20% |
| [PGEL](https://in.tradingview.com/chart/?symbol=NSE:PGEL)<br><sub>📶W9 · W↑40d · ↑CMF0d</sub> | ✓ SAFE | Electronics manufacturing plastic molding appliances consumer goods | ⚡ BULL_ANY_PPV | 82 | 🔄62 | ↑1.035 | ↑8d | SQ·PV | +7.7% | 40.84/39.08 | +3.43% | 20% |
| [PWL](https://in.tradingview.com/chart/?symbol=NSE:PWL)<br><sub>📶W9 · 🚀SS · ↓CMF22d</sub> | ✓ SAFE | Online coaching JEE NEET UPSC exam preparation edtech | ⚡ BULL_ANY_PPV | 54 | 🔄50 | ↑1.025 | ↑1d | PV | +4.5% | -17.14/-21.53 | +4.47% | 20% |
| [SUNDROP](https://in.tradingview.com/chart/?symbol=NSE:SUNDROP)<br><sub>📶W9 · W↑15d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 54 | 🔄33 | ↑1.017 | ↑1d | PV | +2.6% | 31.68/26.19 | +2.56% | 20% |
| [SAIPARENT](https://in.tradingview.com/chart/?symbol=NSE:SAIPARENT)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Injectable pharmaceuticals manufacturer for hospitals and clinics | ⚡ BULL_ANY_PPV | 49 | 🔄50 | ↑1.050 | ↑1d | PV | +6.5% | -32.91/-40.28 | +6.46% | 20% |
| [MEDANTA](https://in.tradingview.com/chart/?symbol=NSE:MEDANTA)<br><sub>📶W9 · W↑83d · 🚀SS · ↑CMF10d</sub> | ⚠ CAUTION | Private tertiary care hospitals, cardiology, North East India | ⚡ BULL_ANY_PPV | 10 | ↑72 | ↑1.024 | ↑15d | PV | +10.5% | 68.78/67.66 | +0.78% | 20% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>📶W9 · W↑40d · 🚀SS · ↑CMF10d</sub> | ✓ SAFE | Tourism sector lending, hotels resorts restaurants amusement parks | ⚡ BULL_ANY_PPV | 0 | ↑96 | ↑1.118 | ↑20d | PV | +56.3% | 78.67/78.63 | +6.02% | 20% |
| [WEL](https://in.tradingview.com/chart/?symbol=NSE:WEL)<br><sub>📶W9 · W↑74d · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | Ceiling fans, exhaust fans, BLDC fans manufacturer | ⚡ BULL_ANY_PPV | 0 | ↑48 | ↑1.095 | ↑40d | PV | +40.0% | 76.3/75.89 | +7.81% | 20% |
| [LLOYDSENT](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENT)<br><sub>📶W9 · W↑88d · 🚀SS · ↑CMF14d</sub> | ✓ SAFE | Steel trading, engineering solutions, real estate investments | 📈 BULL_ANY_MID | 89 | 🔄74 | ↑1.034 | ↑1d | SQ | +5.1% | 45.76/44.22 | +5.06% | 20% |
| [SUMICHEM](https://in.tradingview.com/chart/?symbol=NSE:SUMICHEM)<br><sub>📶W9 · W↑30d · ↑CMF25d</sub> | ✓ SAFE | Agrochemicals pesticides insecticides herbicides fertilizer crop protection | 📈 BULL_ANY_MID | 63 | ↑61 | ↑1.025 | ↑2d | SQ | +5.0% | 10.54/3.85 | +1.48% | 20% |
| [GOODLUCK](https://in.tradingview.com/chart/?symbol=NSE:GOODLUCK)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Steel pipes, forgings, structural products manufacturing export | 📈 BULL_ANY_MID | 58 | ↓78 | ↓0.995 | ↓2d | SQ | +0.8% | -5.45/-10.21 | -1.65% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄83 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [WENDT](https://in.tradingview.com/chart/?symbol=NSE:WENDT)<br><sub>📶W9 · W↑100d · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | Super abrasives grinding machines precision tooling automotive aerospace | 📈 BULL_ANY_MID | 49 | 🔄53 | ↑1.009 | ↑11d | — | +9.8% | 18.43/17.99 | +1.09% | 20% |
| [BECTORFOOD](https://in.tradingview.com/chart/?symbol=NSE:BECTORFOOD)<br><sub>📶W9 · W↑20d · 🚀SS · ↑CMF14d</sub> | ✓ SAFE | Premium biscuits and packaged bakery products for Indian households | 📈 BULL_ANY_MID | 33 | 🔄42 | ↑1.061 | ↑17d | — | +32.8% | 38.39/34.37 | +6.61% | 20% |
| [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR)<br><sub>📶W9 · W↑83d · ↓CMF9d</sub> | ✓ SAFE | White oils, specialty petroleum products, global manufacturer | 📈 BULL_ANY_MID | 15 | ↑95 | ↓1.030 | ↑5d | — | +8.7% | 38.74/38.2 | -0.10% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 11 | ↑69 | ↓1.011 | ↑9d | — | +5.3% | 52.94/52.13 | +0.00% | 20% |
| [UFLEX](https://in.tradingview.com/chart/?symbol=NSE:UFLEX)<br><sub>📶W9 · W↑83d · ↑CMF12d</sub> | ✓ SAFE | Flexible packaging films, laminates for food beverage | 📈 BULL_ANY_MID | 5 | ↑45 | ↑1.024 | ↑27d | — | +15.7% | 55.85/52.99 | +0.99% | 20% |
| [TMB](https://in.tradingview.com/chart/?symbol=NSE:TMB)<br><sub>📶W9 · W↑25d · ↑CMF9d</sub> | ✓ SAFE | Regional private bank serving retail agriculture MSME segments | 📈 BULL_ANY_MID | 0 | ↑92 | ↓1.022 | ↑22d | — | +16.6% | 57.19/57.16 | +0.29% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,###WATCHLIST,NSE:MANORAMA,NSE:LLOYDSENGG,NSE:AKUMS,NSE:DIGITIDE,NSE:PGEL,NSE:PWL,NSE:SUNDROP,NSE:SAIPARENT,NSE:MEDANTA,NSE:TFCILTD,NSE:WEL,NSE:LLOYDSENT,NSE:SUMICHEM,NSE:GOODLUCK,NSE:OFSS,NSE:WENDT,NSE:BECTORFOOD,NSE:GANDHAR,NSE:NESTLEIND,NSE:UFLEX,NSE:TMB
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (31)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MANORAMA](https://in.tradingview.com/chart/?symbol=NSE:MANORAMA)<br><sub>📶W9 · W↑50d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Specialty fats, butters from tree seeds, chocolate cosmetics | ⚡ BULL_ANY_PPV | 98 | 🔄72 | ↑1.009 | ↑2d | SQ·PV | +1.8% | 35.92/32.73 | +0.76% | 20% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>📶W9 · W↑88d · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | Heavy equipment manufacturing for oil gas power plants | ⚡ BULL_ANY_PPV | 89 | 🔄91 | ↑1.059 | ↑1d | SQ·PV | +9.5% | 48.0/42.69 | +9.52% | 20% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ✓ SAFE | CDMO formulation development manufacturing pharmaceuticals India exports | ⚡ BULL_ANY_PPV | 89 | 🔄87 | ↑1.035 | ↑1d | SQ·PV | +5.3% | 14.01/10.6 | +5.27% | 20% |
| [DIGITIDE](https://in.tradingview.com/chart/?symbol=NSE:DIGITIDE)<br><sub>📶W9 · W↑40d · ↓CMF4d</sub> | ✓ SAFE | AI-driven digital transformation, BPM, enterprise services | ⚡ BULL_ANY_PPV | 89 | 🔄13 | ↑1.031 | ↑1d | SQ·PV | +4.7% | 1.77/-3.89 | +4.69% | 20% |
| [PGEL](https://in.tradingview.com/chart/?symbol=NSE:PGEL)<br><sub>📶W9 · W↑40d · ↑CMF0d</sub> | ✓ SAFE | Electronics manufacturing plastic molding appliances consumer goods | ⚡ BULL_ANY_PPV | 82 | 🔄62 | ↑1.035 | ↑8d | SQ·PV | +7.7% | 40.84/39.08 | +3.43% | 20% |
| [PWL](https://in.tradingview.com/chart/?symbol=NSE:PWL)<br><sub>📶W9 · 🚀SS · ↓CMF22d</sub> | ✓ SAFE | Online coaching JEE NEET UPSC exam preparation edtech | ⚡ BULL_ANY_PPV | 54 | 🔄50 | ↑1.025 | ↑1d | PV | +4.5% | -17.14/-21.53 | +4.47% | 20% |
| [SUNDROP](https://in.tradingview.com/chart/?symbol=NSE:SUNDROP)<br><sub>📶W9 · W↑15d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 54 | 🔄33 | ↑1.017 | ↑1d | PV | +2.6% | 31.68/26.19 | +2.56% | 20% |
| [SAIPARENT](https://in.tradingview.com/chart/?symbol=NSE:SAIPARENT)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Injectable pharmaceuticals manufacturer for hospitals and clinics | ⚡ BULL_ANY_PPV | 49 | 🔄50 | ↑1.050 | ↑1d | PV | +6.5% | -32.91/-40.28 | +6.46% | 20% |
| [MEDANTA](https://in.tradingview.com/chart/?symbol=NSE:MEDANTA)<br><sub>📶W9 · W↑83d · 🚀SS · ↑CMF10d</sub> | ⚠ CAUTION | Private tertiary care hospitals, cardiology, North East India | ⚡ BULL_ANY_PPV | 10 | ↑72 | ↑1.024 | ↑15d | PV | +10.5% | 68.78/67.66 | +0.78% | 20% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>📶W9 · W↑40d · 🚀SS · ↑CMF10d</sub> | ✓ SAFE | Tourism sector lending, hotels resorts restaurants amusement parks | ⚡ BULL_ANY_PPV | 0 | ↑96 | ↑1.118 | ↑20d | PV | +56.3% | 78.67/78.63 | +6.02% | 20% |
| [WEL](https://in.tradingview.com/chart/?symbol=NSE:WEL)<br><sub>📶W9 · W↑74d · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | Ceiling fans, exhaust fans, BLDC fans manufacturer | ⚡ BULL_ANY_PPV | 0 | ↑48 | ↑1.095 | ↑40d | PV | +40.0% | 76.3/75.89 | +7.81% | 20% |
| [LLOYDSENT](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENT)<br><sub>📶W9 · W↑88d · 🚀SS · ↑CMF14d</sub> | ✓ SAFE | Steel trading, engineering solutions, real estate investments | 📈 BULL_ANY_MID | 89 | 🔄74 | ↑1.034 | ↑1d | SQ | +5.1% | 45.76/44.22 | +5.06% | 20% |
| [SUMICHEM](https://in.tradingview.com/chart/?symbol=NSE:SUMICHEM)<br><sub>📶W9 · W↑30d · ↑CMF25d</sub> | ✓ SAFE | Agrochemicals pesticides insecticides herbicides fertilizer crop protection | 📈 BULL_ANY_MID | 63 | ↑61 | ↑1.025 | ↑2d | SQ | +5.0% | 10.54/3.85 | +1.48% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄83 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [WENDT](https://in.tradingview.com/chart/?symbol=NSE:WENDT)<br><sub>📶W9 · W↑100d · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | Super abrasives grinding machines precision tooling automotive aerospace | 📈 BULL_ANY_MID | 49 | 🔄53 | ↑1.009 | ↑11d | — | +9.8% | 18.43/17.99 | +1.09% | 20% |
| [BECTORFOOD](https://in.tradingview.com/chart/?symbol=NSE:BECTORFOOD)<br><sub>📶W9 · W↑20d · 🚀SS · ↑CMF14d</sub> | ✓ SAFE | Premium biscuits and packaged bakery products for Indian households | 📈 BULL_ANY_MID | 33 | 🔄42 | ↑1.061 | ↑17d | — | +32.8% | 38.39/34.37 | +6.61% | 20% |
| [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR)<br><sub>📶W9 · W↑83d · ↓CMF9d</sub> | ✓ SAFE | White oils, specialty petroleum products, global manufacturer | 📈 BULL_ANY_MID | 15 | ↑95 | ↓1.030 | ↑5d | — | +8.7% | 38.74/38.2 | -0.10% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 11 | ↑69 | ↓1.011 | ↑9d | — | +5.3% | 52.94/52.13 | +0.00% | 20% |
| [UFLEX](https://in.tradingview.com/chart/?symbol=NSE:UFLEX)<br><sub>📶W9 · W↑83d · ↑CMF12d</sub> | ✓ SAFE | Flexible packaging films, laminates for food beverage | 📈 BULL_ANY_MID | 5 | ↑45 | ↑1.024 | ↑27d | — | +15.7% | 55.85/52.99 | +0.99% | 20% |
| [TMB](https://in.tradingview.com/chart/?symbol=NSE:TMB)<br><sub>📶W9 · W↑25d · ↑CMF9d</sub> | ✓ SAFE | Regional private bank serving retail agriculture MSME segments | 📈 BULL_ANY_MID | 0 | ↑92 | ↓1.022 | ↑22d | — | +16.6% | 57.19/57.16 | +0.29% | 20% |
| [SMSPHARMA](https://in.tradingview.com/chart/?symbol=NSE:SMSPHARMA)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | API manufacturer for oncology and specialty drugs sector | ⚡ BULL_ANY_PPV | 59 | 🔄73 | ↑1.014 | ↑1d | PV | +5.8% | -46.76/-46.84 | +5.85% | 20% |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML)<br><sub>↑CMF2d</sub> | ✓ SAFE | Heavy equipment mining defense rail coaches manufacturer | ⚡ BULL_ANY_PPV | 54 | 🔄30 | ↑1.026 | ↑1d | PV | +3.6% | -35.33/-38.68 | +3.63% | 20% |
| [EMBDL](https://in.tradingview.com/chart/?symbol=NSE:EMBDL)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Residential and commercial real estate developer urban markets | ⚡ BULL_ANY_PPV | 54 | 🔄5 | ↑1.021 | ↑1d | PV | +3.9% | -30.3/-35.29 | +3.86% | 10% 🟨 |
| [MBEL](https://in.tradingview.com/chart/?symbol=NSE:MBEL)<br><sub>↓CMF30d</sub> | ✓ SAFE | Pre-engineered buildings, steel roofing, industrial structures | ⚡ BULL_ANY_PPV | 40 | 🔄50 | ↑1.009 | ↓21d | PV | -3.8% | -32.18/-32.96 | +3.56% | 20% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>🚀SS · ↑CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄90 | ↑1.009 | ↑1d | SQ | +2.7% | -36.34/-42.32 | +2.74% | 20% |
| [HGS](https://in.tradingview.com/chart/?symbol=NSE:HGS)<br><sub>W↑20d · ↑CMF18d</sub> | ✓ SAFE | Customer experience BPM services, global contact center operations | 📈 BULL_ANY_MID | 99 | 🔄27 | ↑1.008 | ↑1d | SQ | +1.3% | -4.83/-9.57 | +1.26% | 20% |
| [GODREJCP](https://in.tradingview.com/chart/?symbol=NSE:GODREJCP)<br><sub>W↑33d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 98 | 🔄36 | ↑1.008 | ↑2d | SQ | +2.1% | 25.85/25.42 | +1.03% | 20% |
| [CMPDI](https://in.tradingview.com/chart/?symbol=NSE:CMPDI)<br><sub>↓CMF7d</sub> | ✓ SAFE | Coal mine planning design consulting engineering services | 📈 BULL_ANY_MID | 46 | 🔄50 | ↑1.011 | ↓14d | — | -2.0% | -30.08/-33.26 | +2.88% | 20% |
| [ANANDRATHI](https://in.tradingview.com/chart/?symbol=NSE:ANANDRATHI)<br><sub>↓CMF0d</sub> | ⚠ CAUTION | Wealth management advisory for high net worth individuals | 📈 BULL_ANY_MID | 45 | ↑1 | ↑1.019 | ↑30d | SQ | +8.8% | 5.96/-2.35 | +1.45% | 20% |
| [JSWCEMENT](https://in.tradingview.com/chart/?symbol=NSE:JSWCEMENT)<br><sub>↓CMF28d</sub> | ✓ SAFE | Eco-friendly cement manufacturing infrastructure construction projects | 📈 BULL_ANY_MID | 40 | 🔄50 | ↑1.006 | ↓40d | — | +5.4% | -12.22/-14.37 | +1.26% | 20% |
| [ASIANTILES](https://in.tradingview.com/chart/?symbol=NSE:ASIANTILES)<br><sub>W↑10d · ↓CMF7d</sub> | ✓ SAFE | Ceramic tiles bathware surfaces domestic international markets | 📈 BULL_ANY_MID | 8 | ↑14 | ↓1.012 | ↑12d | — | +26.9% | 4.87/2.55 | -1.55% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,###WATCHLIST,NSE:MANORAMA,NSE:LLOYDSENGG,NSE:AKUMS,NSE:DIGITIDE,NSE:PGEL,NSE:PWL,NSE:SUNDROP,NSE:SAIPARENT,NSE:MEDANTA,NSE:TFCILTD,NSE:WEL,NSE:LLOYDSENT,NSE:SUMICHEM,NSE:OFSS,NSE:WENDT,NSE:BECTORFOOD,NSE:GANDHAR,NSE:NESTLEIND,NSE:UFLEX,NSE:TMB,NSE:SMSPHARMA,NSE:BEML,NSE:EMBDL,NSE:MBEL,NSE:POWERINDIA,NSE:HGS,NSE:GODREJCP,NSE:CMPDI,NSE:ANANDRATHI,NSE:JSWCEMENT,NSE:ASIANTILES
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (15)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MANORAMA](https://in.tradingview.com/chart/?symbol=NSE:MANORAMA)<br><sub>📶W9 · W↑50d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Specialty fats, butters from tree seeds, chocolate cosmetics | ⚡ BULL_ANY_PPV | 98 | 🔄72 | ↑1.009 | ↑2d | SQ·PV | +1.8% | 35.92/32.73 | +0.76% | 20% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>📶W9 · W↑88d · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | Heavy equipment manufacturing for oil gas power plants | ⚡ BULL_ANY_PPV | 89 | 🔄91 | ↑1.059 | ↑1d | SQ·PV | +9.5% | 48.0/42.69 | +9.52% | 20% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ✓ SAFE | CDMO formulation development manufacturing pharmaceuticals India exports | ⚡ BULL_ANY_PPV | 89 | 🔄87 | ↑1.035 | ↑1d | SQ·PV | +5.3% | 14.01/10.6 | +5.27% | 20% |
| [DIGITIDE](https://in.tradingview.com/chart/?symbol=NSE:DIGITIDE)<br><sub>📶W9 · W↑40d · ↓CMF4d</sub> | ✓ SAFE | AI-driven digital transformation, BPM, enterprise services | ⚡ BULL_ANY_PPV | 89 | 🔄13 | ↑1.031 | ↑1d | SQ·PV | +4.7% | 1.77/-3.89 | +4.69% | 20% |
| [PGEL](https://in.tradingview.com/chart/?symbol=NSE:PGEL)<br><sub>📶W9 · W↑40d · ↑CMF0d</sub> | ✓ SAFE | Electronics manufacturing plastic molding appliances consumer goods | ⚡ BULL_ANY_PPV | 82 | 🔄62 | ↑1.035 | ↑8d | SQ·PV | +7.7% | 40.84/39.08 | +3.43% | 20% |
| [LLOYDSENT](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENT)<br><sub>📶W9 · W↑88d · 🚀SS · ↑CMF14d</sub> | ✓ SAFE | Steel trading, engineering solutions, real estate investments | 📈 BULL_ANY_MID | 89 | 🔄74 | ↑1.034 | ↑1d | SQ | +5.1% | 45.76/44.22 | +5.06% | 20% |
| [SUMICHEM](https://in.tradingview.com/chart/?symbol=NSE:SUMICHEM)<br><sub>📶W9 · W↑30d · ↑CMF25d</sub> | ✓ SAFE | Agrochemicals pesticides insecticides herbicides fertilizer crop protection | 📈 BULL_ANY_MID | 63 | ↑61 | ↑1.025 | ↑2d | SQ | +5.0% | 10.54/3.85 | +1.48% | 20% |
| [GOODLUCK](https://in.tradingview.com/chart/?symbol=NSE:GOODLUCK)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Steel pipes, forgings, structural products manufacturing export | 📈 BULL_ANY_MID | 58 | ↓78 | ↓0.995 | ↓2d | SQ | +0.8% | -5.45/-10.21 | -1.65% | 20% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>🚀SS · ↑CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄90 | ↑1.009 | ↑1d | SQ | +2.7% | -36.34/-42.32 | +2.74% | 20% |
| [HGS](https://in.tradingview.com/chart/?symbol=NSE:HGS)<br><sub>W↑20d · ↑CMF18d</sub> | ✓ SAFE | Customer experience BPM services, global contact center operations | 📈 BULL_ANY_MID | 99 | 🔄27 | ↑1.008 | ↑1d | SQ | +1.3% | -4.83/-9.57 | +1.26% | 20% |
| [GODREJCP](https://in.tradingview.com/chart/?symbol=NSE:GODREJCP)<br><sub>W↑33d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 98 | 🔄36 | ↑1.008 | ↑2d | SQ | +2.1% | 25.85/25.42 | +1.03% | 20% |
| [GRSE](https://in.tradingview.com/chart/?symbol=NSE:GRSE)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Warship construction for Indian Navy and Coast Guard | 📈 BULL_ANY_MID | 58 | ↓35 | ↓1.006 | ↑2d | SQ | +3.7% | -33.16/-38.56 | -0.02% | 20% |
| [GMRP&UI](https://in.tradingview.com/chart/?symbol=NSE:GMRP&UI)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Power generation, urban infrastructure, transportation services India | 📈 BULL_ANY_MID | 58 | ↓20 | ↓0.999 | ↓2d | SQ | +1.9% | -36.27/-36.92 | -0.35% | 20% |
| [V2RETAIL](https://in.tradingview.com/chart/?symbol=NSE:V2RETAIL)<br><sub>↓CMF30d</sub> | ✓ SAFE | Budget apparel and merchandise for Tier-II Tier-III towns | 📈 BULL_ANY_MID | 50 | ↓46 | ↑1.000 | ↓15d | SQ | -0.8% | -47.37/-47.82 | +0.52% | 20% |
| [ANANDRATHI](https://in.tradingview.com/chart/?symbol=NSE:ANANDRATHI)<br><sub>↓CMF0d</sub> | ⚠ CAUTION | Wealth management advisory for high net worth individuals | 📈 BULL_ANY_MID | 45 | ↑1 | ↑1.019 | ↑30d | SQ | +8.8% | 5.96/-2.35 | +1.45% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,###WATCHLIST,NSE:MANORAMA,NSE:LLOYDSENGG,NSE:AKUMS,NSE:DIGITIDE,NSE:PGEL,NSE:LLOYDSENT,NSE:SUMICHEM,NSE:GOODLUCK,NSE:POWERINDIA,NSE:HGS,NSE:GODREJCP,NSE:GRSE,NSE:GMRP&UI,NSE:V2RETAIL,NSE:ANANDRATHI
```

---

### 🔥 MAJOR — PPV confirmed (11)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PWL](https://in.tradingview.com/chart/?symbol=NSE:PWL)<br><sub>📶W9 · 🚀SS · ↓CMF22d</sub> | ✓ SAFE | Online coaching JEE NEET UPSC exam preparation edtech | ⚡ BULL_ANY_PPV | 54 | 🔄50 | ↑1.025 | ↑1d | PV | +4.5% | -17.14/-21.53 | +4.47% | 20% |
| [SUNDROP](https://in.tradingview.com/chart/?symbol=NSE:SUNDROP)<br><sub>📶W9 · W↑15d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 54 | 🔄33 | ↑1.017 | ↑1d | PV | +2.6% | 31.68/26.19 | +2.56% | 20% |
| [SAIPARENT](https://in.tradingview.com/chart/?symbol=NSE:SAIPARENT)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Injectable pharmaceuticals manufacturer for hospitals and clinics | ⚡ BULL_ANY_PPV | 49 | 🔄50 | ↑1.050 | ↑1d | PV | +6.5% | -32.91/-40.28 | +6.46% | 20% |
| [MEDANTA](https://in.tradingview.com/chart/?symbol=NSE:MEDANTA)<br><sub>📶W9 · W↑83d · 🚀SS · ↑CMF10d</sub> | ⚠ CAUTION | Private tertiary care hospitals, cardiology, North East India | ⚡ BULL_ANY_PPV | 10 | ↑72 | ↑1.024 | ↑15d | PV | +10.5% | 68.78/67.66 | +0.78% | 20% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>📶W9 · W↑40d · 🚀SS · ↑CMF10d</sub> | ✓ SAFE | Tourism sector lending, hotels resorts restaurants amusement parks | ⚡ BULL_ANY_PPV | 0 | ↑96 | ↑1.118 | ↑20d | PV | +56.3% | 78.67/78.63 | +6.02% | 20% |
| [WEL](https://in.tradingview.com/chart/?symbol=NSE:WEL)<br><sub>📶W9 · W↑74d · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | Ceiling fans, exhaust fans, BLDC fans manufacturer | ⚡ BULL_ANY_PPV | 0 | ↑48 | ↑1.095 | ↑40d | PV | +40.0% | 76.3/75.89 | +7.81% | 20% |
| [SMSPHARMA](https://in.tradingview.com/chart/?symbol=NSE:SMSPHARMA)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | API manufacturer for oncology and specialty drugs sector | ⚡ BULL_ANY_PPV | 59 | 🔄73 | ↑1.014 | ↑1d | PV | +5.8% | -46.76/-46.84 | +5.85% | 20% |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML)<br><sub>↑CMF2d</sub> | ✓ SAFE | Heavy equipment mining defense rail coaches manufacturer | ⚡ BULL_ANY_PPV | 54 | 🔄30 | ↑1.026 | ↑1d | PV | +3.6% | -35.33/-38.68 | +3.63% | 20% |
| [EMBDL](https://in.tradingview.com/chart/?symbol=NSE:EMBDL)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Residential and commercial real estate developer urban markets | ⚡ BULL_ANY_PPV | 54 | 🔄5 | ↑1.021 | ↑1d | PV | +3.9% | -30.3/-35.29 | +3.86% | 10% 🟨 |
| [MBEL](https://in.tradingview.com/chart/?symbol=NSE:MBEL)<br><sub>↓CMF30d</sub> | ✓ SAFE | Pre-engineered buildings, steel roofing, industrial structures | ⚡ BULL_ANY_PPV | 40 | 🔄50 | ↑1.009 | ↓21d | PV | -3.8% | -32.18/-32.96 | +3.56% | 20% |
| [TATACHEM](https://in.tradingview.com/chart/?symbol=NSE:TATACHEM)<br><sub>🚀SS·10x · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Alkaline soda ash, salt chemicals, specialty products manufacturer | ⚡ BULL_ANY_PPV | 15 | ↓9 | ↑0.999 | ↓10d | PV | -1.7% | -51.69/-57.43 | +1.55% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,###WATCHLIST,NSE:PWL,NSE:SUNDROP,NSE:SAIPARENT,NSE:MEDANTA,NSE:TFCILTD,NSE:WEL,NSE:SMSPHARMA,NSE:BEML,NSE:EMBDL,NSE:MBEL,NSE:TATACHEM
```

### 🟢 OVERSOLD — reversal from −53/−60 (3)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [NUCLEUS](https://in.tradingview.com/chart/?symbol=NSE:NUCLEUS)<br><sub>↓CMF22d · ⚠️TRAP</sub> | ✓ SAFE | Banking software for retail lending and payments | 🟢 BULL_OVERSOLD | 5 | ↓4 | ↑0.985 | ↓20d | — | -7.2% | -62.83/-64.35 | -0.04% | 20% |
| [ASTEC](https://in.tradingview.com/chart/?symbol=NSE:ASTEC)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Agrochemical active ingredients manufacturer serving domestic and export markets | 🟢 BULL_OVERSOLD | 5 | ↓20 | ↑0.978 | ↓39d | — | -18.7% | -64.22/-64.43 | +0.02% | 20% |
| [VBL](https://in.tradingview.com/chart/?symbol=NSE:VBL)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 5 | ↓22 | ↑0.992 | ↓38d | — | -15.2% | -55.06/-56.28 | +1.38% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,###WATCHLIST,NSE:NUCLEUS,NSE:ASTEC,NSE:VBL
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (16)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄83 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [WENDT](https://in.tradingview.com/chart/?symbol=NSE:WENDT)<br><sub>📶W9 · W↑100d · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | Super abrasives grinding machines precision tooling automotive aerospace | 📈 BULL_ANY_MID | 49 | 🔄53 | ↑1.009 | ↑11d | — | +9.8% | 18.43/17.99 | +1.09% | 20% |
| [BECTORFOOD](https://in.tradingview.com/chart/?symbol=NSE:BECTORFOOD)<br><sub>📶W9 · W↑20d · 🚀SS · ↑CMF14d</sub> | ✓ SAFE | Premium biscuits and packaged bakery products for Indian households | 📈 BULL_ANY_MID | 33 | 🔄42 | ↑1.061 | ↑17d | — | +32.8% | 38.39/34.37 | +6.61% | 20% |
| [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR)<br><sub>📶W9 · W↑83d · ↓CMF9d</sub> | ✓ SAFE | White oils, specialty petroleum products, global manufacturer | 📈 BULL_ANY_MID | 15 | ↑95 | ↓1.030 | ↑5d | — | +8.7% | 38.74/38.2 | -0.10% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 11 | ↑69 | ↓1.011 | ↑9d | — | +5.3% | 52.94/52.13 | +0.00% | 20% |
| [UFLEX](https://in.tradingview.com/chart/?symbol=NSE:UFLEX)<br><sub>📶W9 · W↑83d · ↑CMF12d</sub> | ✓ SAFE | Flexible packaging films, laminates for food beverage | 📈 BULL_ANY_MID | 5 | ↑45 | ↑1.024 | ↑27d | — | +15.7% | 55.85/52.99 | +0.99% | 20% |
| [TMB](https://in.tradingview.com/chart/?symbol=NSE:TMB)<br><sub>📶W9 · W↑25d · ↑CMF9d</sub> | ✓ SAFE | Regional private bank serving retail agriculture MSME segments | 📈 BULL_ANY_MID | 0 | ↑92 | ↓1.022 | ↑22d | — | +16.6% | 57.19/57.16 | +0.29% | 20% |
| [CMPDI](https://in.tradingview.com/chart/?symbol=NSE:CMPDI)<br><sub>↓CMF7d</sub> | ✓ SAFE | Coal mine planning design consulting engineering services | 📈 BULL_ANY_MID | 46 | 🔄50 | ↑1.011 | ↓14d | — | -2.0% | -30.08/-33.26 | +2.88% | 20% |
| [JSWCEMENT](https://in.tradingview.com/chart/?symbol=NSE:JSWCEMENT)<br><sub>↓CMF28d</sub> | ✓ SAFE | Eco-friendly cement manufacturing infrastructure construction projects | 📈 BULL_ANY_MID | 40 | 🔄50 | ↑1.006 | ↓40d | — | +5.4% | -12.22/-14.37 | +1.26% | 20% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>↓CMF23d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 10 | ↓62 | ↑0.984 | ↓15d | — | -7.1% | -51.35/-51.43 | -0.24% | 20% |
| [HOMEFIRST](https://in.tradingview.com/chart/?symbol=NSE:HOMEFIRST)<br><sub>↑CMF1d</sub> | ⚠ CAUTION | Affordable housing loans for first-time homebuyers India | 📈 BULL_ANY_MID | 10 | ↓48 | ↑1.004 | ↓41d | — | +15.9% | -9.36/-10.34 | +0.23% | 20% |
| [ZOTA](https://in.tradingview.com/chart/?symbol=NSE:ZOTA)<br><sub>🚀SS · ↓CMF27d</sub> | ✓ SAFE | Pharma manufacturer: tablets, syrups, ayurveda, OTC products | 📈 BULL_ANY_MID | 10 | ↓40 | ↑1.005 | ↓48d | — | +11.5% | -35.32/-36.7 | +2.27% | 20% |
| [OMAXE](https://in.tradingview.com/chart/?symbol=NSE:OMAXE)<br><sub>W↑35d · ↑CMF3d · DEL60%(T-1)</sub> | ✓ SAFE | Residential commercial retail real estate developer across India | 📈 BULL_ANY_MID | 10 | ↓49 | ↓0.994 | ↓10d | — | -1.4% | -4.87/-6.88 | -1.03% | 20% |
| [PURVA](https://in.tradingview.com/chart/?symbol=NSE:PURVA)<br><sub>🚀SS · ↑CMF19d</sub> | ✓ SAFE | Residential real estate developer metro cities apartments villas | 📈 BULL_ANY_MID | 10 | ↓17 | ↑1.001 | ↓22d | — | -1.1% | -29.94/-30.26 | +1.41% | 20% |
| [ASIANTILES](https://in.tradingview.com/chart/?symbol=NSE:ASIANTILES)<br><sub>W↑10d · ↓CMF7d</sub> | ✓ SAFE | Ceramic tiles bathware surfaces domestic international markets | 📈 BULL_ANY_MID | 8 | ↑14 | ↓1.012 | ↑12d | — | +26.9% | 4.87/2.55 | -1.55% | 20% |
| [ERIS](https://in.tradingview.com/chart/?symbol=NSE:ERIS)<br><sub>↑CMF26d · ⚠️TRAP</sub> | ⚠ CAUTION | Chronic disease pharmaceuticals: cardiology, diabetes, gastroenterology, dermatology | 📈 BULL_ANY_MID | 5 | ↓27 | ↑0.996 | ↓20d | — | -3.4% | -32.28/-33.07 | -0.04% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,###WATCHLIST,NSE:OFSS,NSE:WENDT,NSE:BECTORFOOD,NSE:GANDHAR,NSE:NESTLEIND,NSE:UFLEX,NSE:TMB,NSE:CMPDI,NSE:JSWCEMENT,NSE:ADANIPORTS,NSE:HOMEFIRST,NSE:ZOTA,NSE:OMAXE,NSE:PURVA,NSE:ASIANTILES,NSE:ERIS
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
