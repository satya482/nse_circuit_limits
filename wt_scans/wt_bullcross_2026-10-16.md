> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-10-16
*Generated 2026-10-16 15:47 IST*

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

**Total bull crosses today: 66** · 28 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:JTLIND,NSE:WPIL,NSE:KANSAINER,NSE:AIIL,NSE:RSL,NSE:HBLENGINE,NSE:SOLARA,NSE:THANGAMAYL,NSE:SAMBHV,NSE:SIGMAADV,NSE:GAIL,NSE:SARDAEN,NSE:TMCV,NSE:ITC,NSE:CRISIL,NSE:GULFOILLUB,NSE:SURYODAY,NSE:INDPRUD,NSE:LINDEINDIA,NSE:RPGLIFE,NSE:VSTTILLERS,NSE:CMRGREEN,NSE:MAHLIFE,NSE:COALINDIA,NSE:CASTROLIND,NSE:INDGN,NSE:JUNIPER,NSE:GILLETTE,NSE:JKCEMENT,NSE:DBL,NSE:MOL,NSE:MUNJALAU,NSE:GEOJITFSL,NSE:SHRIPISTON,NSE:JMFINANCIL,NSE:PARADEEP,NSE:PPLPHARMA,NSE:VINCOFE,NSE:PFOCUS,NSE:DOLPHIN,NSE:KAPSTON,NSE:IRMENERGY,NSE:JSWSTEEL,NSE:MEDPLUS,NSE:HCG,NSE:RICOAUTO,NSE:RAYMONDLSL,NSE:BETA,NSE:SCHAEFFLER,NSE:GANESHHOU,NSE:GKENERGY,NSE:LINCOLN,NSE:MRF,NSE:BPCL,NSE:ADANIPOWER,NSE:SHK,NSE:BRIGHOTEL,NSE:GSFC,NSE:PINELABS,NSE:NDRAUTO,NSE:JINDALSTEL,NSE:ULTRAMAR,NSE:OBEROIRLTY,NSE:NOCIL,NSE:METROPOLIS,NSE:EPIGRAL
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (41)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [JTLIND](https://in.tradingview.com/chart/?symbol=NSE:JTLIND)<br><sub>📶W9 · ↓CMF6d · DEL54%(T-1)</sub> | ✓ SAFE | ERW steel pipes manufacturer for infrastructure construction projects | ⚡ BULL_ANY_PPV | 94 | 🔄76 | ↑1.023 | ↑1d | SQ·PV | +4.7% | -24.98/-30.47 | +4.69% | 20% |
| [WPIL](https://in.tradingview.com/chart/?symbol=NSE:WPIL)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Pumps and pumping systems for water industrial applications | ⚡ BULL_ANY_PPV | 94 | 🔄50 | ↑1.023 | ↑1d | SQ·PV | +3.8% | -22.43/-29.76 | +3.81% | 20% |
| [KANSAINER](https://in.tradingview.com/chart/?symbol=NSE:KANSAINER)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION | Paint manufacturer industrial coatings decorative segment India | ⚡ BULL_ANY_PPV | 94 | 🔄27 | ↑1.022 | ↑1d | SQ·PV | +3.5% | -20.96/-27.6 | +3.49% | 20% |
| [AIIL](https://in.tradingview.com/chart/?symbol=NSE:AIIL)<br><sub>📶W9 · W↑5d · ↑CMF25d</sub> | ⚠ CAUTION | NBFC providing investment loans advances securities financing | ⚡ BULL_ANY_PPV | 89 | 🔄54 | ↑1.037 | ↑1d | SQ·PV | +5.5% | 18.52/11.68 | +5.52% | 20% |
| [RSL](https://in.tradingview.com/chart/?symbol=NSE:RSL)<br><sub>📶W9 · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | Stainless steel bars billets rods domestic international markets | ⚡ BULL_ANY_PPV | 54 | 🔄50 | ↑1.029 | ↑1d | PV | +4.9% | -15.72/-21.61 | +4.87% | 20% |
| [HBLENGINE](https://in.tradingview.com/chart/?symbol=NSE:HBLENGINE)<br><sub>📶W9 · W↑30d · RVOL27x · ↑CMF0d</sub> | ✓ SAFE | Batteries, e-mobility systems, specialized engineering products | ⚡ BULL_ANY_PPV | 49 | 🔄65 | ↑1.108 | ↑1d | PV | +17.4% | -10.14/-16.38 | +17.35% | 20% |
| [SOLARA](https://in.tradingview.com/chart/?symbol=NSE:SOLARA)<br><sub>📶W9 · 🚀SS·22x · ↓CMF9d</sub> | ✓ SAFE | Active pharmaceutical ingredients manufacturing, CRAMS, global pharma supply | ⚡ BULL_ANY_PPV | 49 | 🔄83 | ↑1.036 | ↑1d | PV | +7.5% | -25.6/-31.88 | +7.52% | 20% |
| [THANGAMAYL](https://in.tradingview.com/chart/?symbol=NSE:THANGAMAYL)<br><sub>📶W9 · ↑CMF19d</sub> | ✓ SAFE | Gold silver diamond jewellery retail Tamil Nadu consumer | ⚡ BULL_ANY_PPV | 49 | 🔄87 | ↑1.037 | ↑1d | PV | +5.6% | -26.85/-36.0 | +5.61% | 10% 🟩 |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>📶W9 · W↑80d · 🚀SS · ↑CMF20d</sub> | ✓ SAFE | ERW steel pipes, tubes, structural hollow sections manufacturer | ⚡ BULL_ANY_PPV | 40 | ↑92 | ↑1.056 | ↑21d | SQ·PV | +33.6% | 54.36/49.89 | +5.23% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄54 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [SARDAEN](https://in.tradingview.com/chart/?symbol=NSE:SARDAEN)<br><sub>📶W9 · ↓CMF7d · 🎯SLING</sub> | ⚠ CAUTION | Steel ferroalloys power producer Chhattisgarh integrated | 🟡 BULL_OS_L2 | 80 | 🔄41 | ↑1.003 | ↓32d | SQ | -0.5% | -49.44/-54.01 | +1.03% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄21 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [CRISIL](https://in.tradingview.com/chart/?symbol=NSE:CRISIL)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION | Credit ratings research risk advisory financial markets | 📈 BULL_ANY_MID | 99 | 🔄52 | ↑1.015 | ↑1d | SQ | +3.3% | -22.26/-29.79 | +3.28% | 20% |
| [GULFOILLUB](https://in.tradingview.com/chart/?symbol=NSE:GULFOILLUB)<br><sub>📶W9 · 🚀SS · ↑CMF14d</sub> | ✓ SAFE | Automotive lubricants manufacturing distribution Indian commercial vehicles | 📈 BULL_ANY_MID | 99 | 🔄60 | ↑1.010 | ↑1d | SQ | +2.3% | -18.14/-19.94 | +2.34% | 20% |
| [SURYODAY](https://in.tradingview.com/chart/?symbol=NSE:SURYODAY)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Microfinance bank lending unbanked underserved retail borrowers | 📈 BULL_ANY_MID | 99 | 🔄42 | ↑1.001 | ↑1d | SQ | +0.7% | -12.79/-13.14 | +0.73% | 20% |
| [INDPRUD](https://in.tradingview.com/chart/?symbol=NSE:INDPRUD)<br><sub>📶W9 · 🚀SS · ↓CMF2d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.011 | ↑1d | SQ | +2.0% | 5.14/2.33 | +2.01% | 20% |
| [LINDEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LINDEINDIA)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Industrial medical gases cryogenic plants manufacturing India | 📈 BULL_ANY_MID | 94 | 🔄40 | ↑1.018 | ↑1d | SQ | +3.4% | -39.77/-46.67 | +3.42% | 20% |
| [RPGLIFE](https://in.tradingview.com/chart/?symbol=NSE:RPGLIFE)<br><sub>📶W9 · ↑CMF17d</sub> | ✓ SAFE | Pharmaceutical formulations and APIs for domestic international markets | 📈 BULL_ANY_MID | 94 | 🔄76 | ↑1.029 | ↑1d | SQ | +5.6% | -3.82/-5.45 | +5.59% | 20% |
| [VSTTILLERS](https://in.tradingview.com/chart/?symbol=NSE:VSTTILLERS)<br><sub>📶W9 · W↑20d · 🚀SS · ↓CMF1d</sub> | ✓ SAFE | Power tillers and compact tractors for Indian farmers | 📈 BULL_ANY_MID | 92 | 🔄25 | ↑0.998 | ↓3d | SQ | +0.5% | -14.78/-14.95 | +0.55% | 20% |
| [CMRGREEN](https://in.tradingview.com/chart/?symbol=NSE:CMRGREEN)<br><sub>📶W9 · ↑CMF3d</sub> | ✓ SAFE | Recycled aluminium zinc alloys ingots automotive casting | 📈 BULL_ANY_MID | 91 | 🔄50 | ↑1.001 | ↓9d | SQ | -0.6% | -27.47/-27.76 | +0.88% | 20% |
| [MAHLIFE](https://in.tradingview.com/chart/?symbol=NSE:MAHLIFE)<br><sub>📶W9 · ↑CMF5d</sub> | ⚠ CAUTION | Residential and industrial real estate development across India | 📈 BULL_ANY_MID | 85 | 🔄46 | ↑1.003 | ↓15d | SQ | -1.9% | -52.85/-52.96 | +2.03% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑53 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [CASTROLIND](https://in.tradingview.com/chart/?symbol=NSE:CASTROLIND)<br><sub>📶W9 · ↑CMF20d</sub> | ✓ SAFE | Automotive and industrial lubricants manufacturer serving India | 📈 BULL_ANY_MID | 69 | ↑64 | ↑1.006 | ↑1d | SQ | +0.9% | 13.11/12.91 | +0.89% | 20% |
| [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN)<br><sub>📶W9 · ↓CMF14d</sub> | ✓ SAFE | Digital commercialization services for global pharma companies | 📈 BULL_ANY_MID | 69 | ↑77 | ↑1.010 | ↑1d | SQ | +1.6% | -4.72/-9.57 | +1.63% | 20% |
| [JUNIPER](https://in.tradingview.com/chart/?symbol=NSE:JUNIPER)<br><sub>📶W9 · W↑55d · ↓CMF6d</sub> | ⚠ CAUTION | Luxury hotel ownership management Hyatt partnership India portfolio | 📈 BULL_ANY_MID | 68 | ↑52 | ↑1.007 | ↑2d | SQ | +1.5% | -8.62/-14.29 | +0.35% | 20% |
| [GILLETTE](https://in.tradingview.com/chart/?symbol=NSE:GILLETTE)<br><sub>📶W9 · W↑5d · ↑CMF19d</sub> | ⚠ CAUTION | Razor blades shaving cream oral care FMCG grooming | 📈 BULL_ANY_MID | 63 | ↑31 | ↑1.018 | ↑2d | SQ | +3.1% | -11.27/-19.11 | +1.90% | 20% |
| [JKCEMENT](https://in.tradingview.com/chart/?symbol=NSE:JKCEMENT)<br><sub>📶W9 · ↑CMF7d</sub> | ⚠ CAUTION | Cement manufacturing construction materials India domestic markets | 📈 BULL_ANY_MID | 62 | ↑19 | ↑1.000 | ↓8d | SQ | -0.8% | -31.75/-36.77 | +0.37% | 20% |
| [DBL](https://in.tradingview.com/chart/?symbol=NSE:DBL)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Highway and bridge construction, roads infrastructure sector | 📈 BULL_ANY_MID | 59 | 🔄36 | ↑1.010 | ↑1d | — | +2.8% | -37.38/-39.76 | +2.76% | 20% |
| [MOL](https://in.tradingview.com/chart/?symbol=NSE:MOL)<br><sub>📶W9 · 🚀SS · ↓CMF19d</sub> | ✓ SAFE | Agrochemicals and pigments manufacturer for farms and coatings | 📈 BULL_ANY_MID | 54 | 🔄52 | ↑1.023 | ↑1d | — | +5.3% | -16.4/-20.44 | +5.29% | 20% |
| [MUNJALAU](https://in.tradingview.com/chart/?symbol=NSE:MUNJALAU)<br><sub>📶W9 · ↑CMF12d · ⚠️TRAP</sub> | ✓ SAFE | Two-wheeler four-wheeler auto components manufacturer | 📈 BULL_ANY_MID | 52 | ↓74 | ↑0.995 | ↓13d | SQ | -2.9% | -35.68/-35.76 | -0.05% | 20% |
| [GEOJITFSL](https://in.tradingview.com/chart/?symbol=NSE:GEOJITFSL)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Stock broking and portfolio management for retail investors | 📈 BULL_ANY_MID | 51 | 🔄56 | ↑1.005 | ↓9d | — | +0.5% | -35.85/-37.86 | +1.71% | 20% |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Pistons rings valves manufacturer automotive OEM export | 📈 BULL_ANY_MID | 49 | 🔄85 | ↑1.046 | ↑1d | — | +6.7% | -15.51/-23.71 | +6.68% | 20% |
| [JMFINANCIL](https://in.tradingview.com/chart/?symbol=NSE:JMFINANCIL)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Investment banking mortgage lending distressed credit asset management | 📈 BULL_ANY_MID | 47 | 🔄32 | ↑1.003 | ↓13d | — | -3.5% | -46.04/-48.67 | +1.73% | 20% |
| [PARADEEP](https://in.tradingview.com/chart/?symbol=NSE:PARADEEP)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Phosphate fertilizer manufacturer for Indian agriculture sector | 📈 BULL_ANY_MID | 46 | 🔄55 | ↑0.996 | ↓9d | — | -4.2% | -43.97/-45.27 | +0.86% | 20% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>📶W9 · 🚀SS · ↓CMF17d · DEL75%(T-1)</sub> | ✓ SAFE | CDMO and critical care generics pharma manufacturing | 📈 BULL_ANY_MID | 40 | 🔄71 | ↑1.001 | ↓20d | — | -5.0% | -50.85/-52.67 | +1.92% | 20% |
| [VINCOFE](https://in.tradingview.com/chart/?symbol=NSE:VINCOFE)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Instant coffee chicory manufacturing export beverages | 📈 BULL_ANY_MID | 40 | ↓77 | ↓0.995 | ↓22d | SQ | +5.9% | 2.42/1.7 | -0.71% | 20% |
| [PFOCUS](https://in.tradingview.com/chart/?symbol=NSE:PFOCUS)<br><sub>📶W9 · 🚀SS · ↓CMF11d</sub> | ✓ SAFE | VFX animation post-production services for film television | 📈 BULL_ANY_MID | 35 | 🔄73 | ↑1.016 | ↓32d | — | +3.5% | -28.73/-32.02 | +4.63% | 20% |
| [DOLPHIN](https://in.tradingview.com/chart/?symbol=NSE:DOLPHIN)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Underwater services marine operations offshore oil gas construction | 📈 BULL_ANY_MID | 24 | ↑94 | ↑1.016 | ↑1d | — | +2.3% | -10.34/-12.94 | +2.26% | 20% 🟦 |
| [KAPSTON](https://in.tradingview.com/chart/?symbol=NSE:KAPSTON)<br><sub>📶W9 · ↓CMF15d</sub> | ✓ SAFE | Security guarding and facility management staffing services | 📈 BULL_ANY_MID | 2 | ↑97 | ↓1.000 | ↓18d | — | -5.5% | -40.17/-43.34 | -0.64% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:JTLIND,NSE:WPIL,NSE:KANSAINER,NSE:AIIL,NSE:RSL,NSE:HBLENGINE,NSE:SOLARA,NSE:THANGAMAYL,NSE:SAMBHV,NSE:SIGMAADV,NSE:GAIL,NSE:SARDAEN,NSE:TMCV,NSE:ITC,NSE:CRISIL,NSE:GULFOILLUB,NSE:SURYODAY,NSE:INDPRUD,NSE:LINDEINDIA,NSE:RPGLIFE,NSE:VSTTILLERS,NSE:CMRGREEN,NSE:MAHLIFE,NSE:COALINDIA,NSE:CASTROLIND,NSE:INDGN,NSE:JUNIPER,NSE:GILLETTE,NSE:JKCEMENT,NSE:DBL,NSE:MOL,NSE:MUNJALAU,NSE:GEOJITFSL,NSE:SHRIPISTON,NSE:JMFINANCIL,NSE:PARADEEP,NSE:PPLPHARMA,NSE:VINCOFE,NSE:PFOCUS,NSE:DOLPHIN,NSE:KAPSTON
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (47)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [JTLIND](https://in.tradingview.com/chart/?symbol=NSE:JTLIND)<br><sub>📶W9 · ↓CMF6d · DEL54%(T-1)</sub> | ✓ SAFE | ERW steel pipes manufacturer for infrastructure construction projects | ⚡ BULL_ANY_PPV | 94 | 🔄76 | ↑1.023 | ↑1d | SQ·PV | +4.7% | -24.98/-30.47 | +4.69% | 20% |
| [WPIL](https://in.tradingview.com/chart/?symbol=NSE:WPIL)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Pumps and pumping systems for water industrial applications | ⚡ BULL_ANY_PPV | 94 | 🔄50 | ↑1.023 | ↑1d | SQ·PV | +3.8% | -22.43/-29.76 | +3.81% | 20% |
| [KANSAINER](https://in.tradingview.com/chart/?symbol=NSE:KANSAINER)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION | Paint manufacturer industrial coatings decorative segment India | ⚡ BULL_ANY_PPV | 94 | 🔄27 | ↑1.022 | ↑1d | SQ·PV | +3.5% | -20.96/-27.6 | +3.49% | 20% |
| [AIIL](https://in.tradingview.com/chart/?symbol=NSE:AIIL)<br><sub>📶W9 · W↑5d · ↑CMF25d</sub> | ⚠ CAUTION | NBFC providing investment loans advances securities financing | ⚡ BULL_ANY_PPV | 89 | 🔄54 | ↑1.037 | ↑1d | SQ·PV | +5.5% | 18.52/11.68 | +5.52% | 20% |
| [RSL](https://in.tradingview.com/chart/?symbol=NSE:RSL)<br><sub>📶W9 · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | Stainless steel bars billets rods domestic international markets | ⚡ BULL_ANY_PPV | 54 | 🔄50 | ↑1.029 | ↑1d | PV | +4.9% | -15.72/-21.61 | +4.87% | 20% |
| [HBLENGINE](https://in.tradingview.com/chart/?symbol=NSE:HBLENGINE)<br><sub>📶W9 · W↑30d · RVOL27x · ↑CMF0d</sub> | ✓ SAFE | Batteries, e-mobility systems, specialized engineering products | ⚡ BULL_ANY_PPV | 49 | 🔄65 | ↑1.108 | ↑1d | PV | +17.4% | -10.14/-16.38 | +17.35% | 20% |
| [SOLARA](https://in.tradingview.com/chart/?symbol=NSE:SOLARA)<br><sub>📶W9 · 🚀SS·22x · ↓CMF9d</sub> | ✓ SAFE | Active pharmaceutical ingredients manufacturing, CRAMS, global pharma supply | ⚡ BULL_ANY_PPV | 49 | 🔄83 | ↑1.036 | ↑1d | PV | +7.5% | -25.6/-31.88 | +7.52% | 20% |
| [THANGAMAYL](https://in.tradingview.com/chart/?symbol=NSE:THANGAMAYL)<br><sub>📶W9 · ↑CMF19d</sub> | ✓ SAFE | Gold silver diamond jewellery retail Tamil Nadu consumer | ⚡ BULL_ANY_PPV | 49 | 🔄87 | ↑1.037 | ↑1d | PV | +5.6% | -26.85/-36.0 | +5.61% | 10% 🟩 |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>📶W9 · W↑80d · 🚀SS · ↑CMF20d</sub> | ✓ SAFE | ERW steel pipes, tubes, structural hollow sections manufacturer | ⚡ BULL_ANY_PPV | 40 | ↑92 | ↑1.056 | ↑21d | SQ·PV | +33.6% | 54.36/49.89 | +5.23% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄54 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [SARDAEN](https://in.tradingview.com/chart/?symbol=NSE:SARDAEN)<br><sub>📶W9 · ↓CMF7d · 🎯SLING</sub> | ⚠ CAUTION | Steel ferroalloys power producer Chhattisgarh integrated | 🟡 BULL_OS_L2 | 80 | 🔄41 | ↑1.003 | ↓32d | SQ | -0.5% | -49.44/-54.01 | +1.03% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄21 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [CRISIL](https://in.tradingview.com/chart/?symbol=NSE:CRISIL)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION | Credit ratings research risk advisory financial markets | 📈 BULL_ANY_MID | 99 | 🔄52 | ↑1.015 | ↑1d | SQ | +3.3% | -22.26/-29.79 | +3.28% | 20% |
| [GULFOILLUB](https://in.tradingview.com/chart/?symbol=NSE:GULFOILLUB)<br><sub>📶W9 · 🚀SS · ↑CMF14d</sub> | ✓ SAFE | Automotive lubricants manufacturing distribution Indian commercial vehicles | 📈 BULL_ANY_MID | 99 | 🔄60 | ↑1.010 | ↑1d | SQ | +2.3% | -18.14/-19.94 | +2.34% | 20% |
| [SURYODAY](https://in.tradingview.com/chart/?symbol=NSE:SURYODAY)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Microfinance bank lending unbanked underserved retail borrowers | 📈 BULL_ANY_MID | 99 | 🔄42 | ↑1.001 | ↑1d | SQ | +0.7% | -12.79/-13.14 | +0.73% | 20% |
| [INDPRUD](https://in.tradingview.com/chart/?symbol=NSE:INDPRUD)<br><sub>📶W9 · 🚀SS · ↓CMF2d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.011 | ↑1d | SQ | +2.0% | 5.14/2.33 | +2.01% | 20% |
| [LINDEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LINDEINDIA)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Industrial medical gases cryogenic plants manufacturing India | 📈 BULL_ANY_MID | 94 | 🔄40 | ↑1.018 | ↑1d | SQ | +3.4% | -39.77/-46.67 | +3.42% | 20% |
| [RPGLIFE](https://in.tradingview.com/chart/?symbol=NSE:RPGLIFE)<br><sub>📶W9 · ↑CMF17d</sub> | ✓ SAFE | Pharmaceutical formulations and APIs for domestic international markets | 📈 BULL_ANY_MID | 94 | 🔄76 | ↑1.029 | ↑1d | SQ | +5.6% | -3.82/-5.45 | +5.59% | 20% |
| [VSTTILLERS](https://in.tradingview.com/chart/?symbol=NSE:VSTTILLERS)<br><sub>📶W9 · W↑20d · 🚀SS · ↓CMF1d</sub> | ✓ SAFE | Power tillers and compact tractors for Indian farmers | 📈 BULL_ANY_MID | 92 | 🔄25 | ↑0.998 | ↓3d | SQ | +0.5% | -14.78/-14.95 | +0.55% | 20% |
| [CMRGREEN](https://in.tradingview.com/chart/?symbol=NSE:CMRGREEN)<br><sub>📶W9 · ↑CMF3d</sub> | ✓ SAFE | Recycled aluminium zinc alloys ingots automotive casting | 📈 BULL_ANY_MID | 91 | 🔄50 | ↑1.001 | ↓9d | SQ | -0.6% | -27.47/-27.76 | +0.88% | 20% |
| [MAHLIFE](https://in.tradingview.com/chart/?symbol=NSE:MAHLIFE)<br><sub>📶W9 · ↑CMF5d</sub> | ⚠ CAUTION | Residential and industrial real estate development across India | 📈 BULL_ANY_MID | 85 | 🔄46 | ↑1.003 | ↓15d | SQ | -1.9% | -52.85/-52.96 | +2.03% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑53 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [CASTROLIND](https://in.tradingview.com/chart/?symbol=NSE:CASTROLIND)<br><sub>📶W9 · ↑CMF20d</sub> | ✓ SAFE | Automotive and industrial lubricants manufacturer serving India | 📈 BULL_ANY_MID | 69 | ↑64 | ↑1.006 | ↑1d | SQ | +0.9% | 13.11/12.91 | +0.89% | 20% |
| [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN)<br><sub>📶W9 · ↓CMF14d</sub> | ✓ SAFE | Digital commercialization services for global pharma companies | 📈 BULL_ANY_MID | 69 | ↑77 | ↑1.010 | ↑1d | SQ | +1.6% | -4.72/-9.57 | +1.63% | 20% |
| [JUNIPER](https://in.tradingview.com/chart/?symbol=NSE:JUNIPER)<br><sub>📶W9 · W↑55d · ↓CMF6d</sub> | ⚠ CAUTION | Luxury hotel ownership management Hyatt partnership India portfolio | 📈 BULL_ANY_MID | 68 | ↑52 | ↑1.007 | ↑2d | SQ | +1.5% | -8.62/-14.29 | +0.35% | 20% |
| [GILLETTE](https://in.tradingview.com/chart/?symbol=NSE:GILLETTE)<br><sub>📶W9 · W↑5d · ↑CMF19d</sub> | ⚠ CAUTION | Razor blades shaving cream oral care FMCG grooming | 📈 BULL_ANY_MID | 63 | ↑31 | ↑1.018 | ↑2d | SQ | +3.1% | -11.27/-19.11 | +1.90% | 20% |
| [JKCEMENT](https://in.tradingview.com/chart/?symbol=NSE:JKCEMENT)<br><sub>📶W9 · ↑CMF7d</sub> | ⚠ CAUTION | Cement manufacturing construction materials India domestic markets | 📈 BULL_ANY_MID | 62 | ↑19 | ↑1.000 | ↓8d | SQ | -0.8% | -31.75/-36.77 | +0.37% | 20% |
| [DBL](https://in.tradingview.com/chart/?symbol=NSE:DBL)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Highway and bridge construction, roads infrastructure sector | 📈 BULL_ANY_MID | 59 | 🔄36 | ↑1.010 | ↑1d | — | +2.8% | -37.38/-39.76 | +2.76% | 20% |
| [MOL](https://in.tradingview.com/chart/?symbol=NSE:MOL)<br><sub>📶W9 · 🚀SS · ↓CMF19d</sub> | ✓ SAFE | Agrochemicals and pigments manufacturer for farms and coatings | 📈 BULL_ANY_MID | 54 | 🔄52 | ↑1.023 | ↑1d | — | +5.3% | -16.4/-20.44 | +5.29% | 20% |
| [GEOJITFSL](https://in.tradingview.com/chart/?symbol=NSE:GEOJITFSL)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Stock broking and portfolio management for retail investors | 📈 BULL_ANY_MID | 51 | 🔄56 | ↑1.005 | ↓9d | — | +0.5% | -35.85/-37.86 | +1.71% | 20% |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Pistons rings valves manufacturer automotive OEM export | 📈 BULL_ANY_MID | 49 | 🔄85 | ↑1.046 | ↑1d | — | +6.7% | -15.51/-23.71 | +6.68% | 20% |
| [JMFINANCIL](https://in.tradingview.com/chart/?symbol=NSE:JMFINANCIL)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Investment banking mortgage lending distressed credit asset management | 📈 BULL_ANY_MID | 47 | 🔄32 | ↑1.003 | ↓13d | — | -3.5% | -46.04/-48.67 | +1.73% | 20% |
| [PARADEEP](https://in.tradingview.com/chart/?symbol=NSE:PARADEEP)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Phosphate fertilizer manufacturer for Indian agriculture sector | 📈 BULL_ANY_MID | 46 | 🔄55 | ↑0.996 | ↓9d | — | -4.2% | -43.97/-45.27 | +0.86% | 20% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>📶W9 · 🚀SS · ↓CMF17d · DEL75%(T-1)</sub> | ✓ SAFE | CDMO and critical care generics pharma manufacturing | 📈 BULL_ANY_MID | 40 | 🔄71 | ↑1.001 | ↓20d | — | -5.0% | -50.85/-52.67 | +1.92% | 20% |
| [PFOCUS](https://in.tradingview.com/chart/?symbol=NSE:PFOCUS)<br><sub>📶W9 · 🚀SS · ↓CMF11d</sub> | ✓ SAFE | VFX animation post-production services for film television | 📈 BULL_ANY_MID | 35 | 🔄73 | ↑1.016 | ↓32d | — | +3.5% | -28.73/-32.02 | +4.63% | 20% |
| [DOLPHIN](https://in.tradingview.com/chart/?symbol=NSE:DOLPHIN)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Underwater services marine operations offshore oil gas construction | 📈 BULL_ANY_MID | 24 | ↑94 | ↑1.016 | ↑1d | — | +2.3% | -10.34/-12.94 | +2.26% | 20% 🟦 |
| [KAPSTON](https://in.tradingview.com/chart/?symbol=NSE:KAPSTON)<br><sub>📶W9 · ↓CMF15d</sub> | ✓ SAFE | Security guarding and facility management staffing services | 📈 BULL_ANY_MID | 2 | ↑97 | ↓1.000 | ↓18d | — | -5.5% | -40.17/-43.34 | -0.64% | 20% |
| [IRMENERGY](https://in.tradingview.com/chart/?symbol=NSE:IRMENERGY)<br><sub>🚀SS · ↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Natural gas distribution networks serving residential commercial industrial | 🟢 BULL_OVERSOLD | 80 | 🔄42 | ↑1.001 | ↓30d | SQ | -8.3% | -59.48/-60.5 | +3.10% | 20% 🟦 |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 42 | 🔄51 | ↑0.992 | ↓13d | — | -5.3% | -64.43/-65.64 | +2.00% | 20% |
| [MRF](https://in.tradingview.com/chart/?symbol=NSE:MRF)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Tyre manufacturer for cars trucks two-wheelers tractors | 🟡 BULL_OS_L2 | 75 | 🔄30 | ↑1.000 | ↓35d | SQ | -7.0% | -52.75/-54.82 | +0.57% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 41 | 🔄36 | ↑1.001 | ↓19d | — | -4.4% | -53.92/-57.54 | +1.19% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 22 | ↑66 | ↑1.004 | ↓8d | — | -0.3% | -53.58/-59.08 | +0.30% | 20% |
| [SHK](https://in.tradingview.com/chart/?symbol=NSE:SHK)<br><sub>🚀SS · ↑CMF0d</sub> | ✓ SAFE | Fragrances flavors aroma chemicals FMCG personal care food beverage | 📈 BULL_ANY_MID | 99 | 🔄32 | ↑1.006 | ↑1d | SQ | +2.4% | -31.51/-32.91 | +2.37% | 20% |
| [BRIGHOTEL](https://in.tradingview.com/chart/?symbol=NSE:BRIGHOTEL)<br><sub>↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 82 | 🔄22 | ↑1.000 | ↓13d | SQ | -0.5% | -39.57/-40.8 | +0.65% | 20% |
| [GSFC](https://in.tradingview.com/chart/?symbol=NSE:GSFC)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Fertilizers and industrial chemicals manufacturer for agriculture | 📈 BULL_ANY_MID | 51 | 🔄30 | ↑1.003 | ↓9d | — | +1.1% | -44.93/-46.79 | +1.53% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:JTLIND,NSE:WPIL,NSE:KANSAINER,NSE:AIIL,NSE:RSL,NSE:HBLENGINE,NSE:SOLARA,NSE:THANGAMAYL,NSE:SAMBHV,NSE:SIGMAADV,NSE:GAIL,NSE:SARDAEN,NSE:TMCV,NSE:ITC,NSE:CRISIL,NSE:GULFOILLUB,NSE:SURYODAY,NSE:INDPRUD,NSE:LINDEINDIA,NSE:RPGLIFE,NSE:VSTTILLERS,NSE:CMRGREEN,NSE:MAHLIFE,NSE:COALINDIA,NSE:CASTROLIND,NSE:INDGN,NSE:JUNIPER,NSE:GILLETTE,NSE:JKCEMENT,NSE:DBL,NSE:MOL,NSE:GEOJITFSL,NSE:SHRIPISTON,NSE:JMFINANCIL,NSE:PARADEEP,NSE:PPLPHARMA,NSE:PFOCUS,NSE:DOLPHIN,NSE:KAPSTON,NSE:IRMENERGY,NSE:JSWSTEEL,NSE:MRF,NSE:BPCL,NSE:ADANIPOWER,NSE:SHK,NSE:BRIGHOTEL,NSE:GSFC
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (28)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [JTLIND](https://in.tradingview.com/chart/?symbol=NSE:JTLIND)<br><sub>📶W9 · ↓CMF6d · DEL54%(T-1)</sub> | ✓ SAFE | ERW steel pipes manufacturer for infrastructure construction projects | ⚡ BULL_ANY_PPV | 94 | 🔄76 | ↑1.023 | ↑1d | SQ·PV | +4.7% | -24.98/-30.47 | +4.69% | 20% |
| [WPIL](https://in.tradingview.com/chart/?symbol=NSE:WPIL)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Pumps and pumping systems for water industrial applications | ⚡ BULL_ANY_PPV | 94 | 🔄50 | ↑1.023 | ↑1d | SQ·PV | +3.8% | -22.43/-29.76 | +3.81% | 20% |
| [KANSAINER](https://in.tradingview.com/chart/?symbol=NSE:KANSAINER)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION | Paint manufacturer industrial coatings decorative segment India | ⚡ BULL_ANY_PPV | 94 | 🔄27 | ↑1.022 | ↑1d | SQ·PV | +3.5% | -20.96/-27.6 | +3.49% | 20% |
| [AIIL](https://in.tradingview.com/chart/?symbol=NSE:AIIL)<br><sub>📶W9 · W↑5d · ↑CMF25d</sub> | ⚠ CAUTION | NBFC providing investment loans advances securities financing | ⚡ BULL_ANY_PPV | 89 | 🔄54 | ↑1.037 | ↑1d | SQ·PV | +5.5% | 18.52/11.68 | +5.52% | 20% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>📶W9 · W↑80d · 🚀SS · ↑CMF20d</sub> | ✓ SAFE | ERW steel pipes, tubes, structural hollow sections manufacturer | ⚡ BULL_ANY_PPV | 40 | ↑92 | ↑1.056 | ↑21d | SQ·PV | +33.6% | 54.36/49.89 | +5.23% | 20% |
| [SARDAEN](https://in.tradingview.com/chart/?symbol=NSE:SARDAEN)<br><sub>📶W9 · ↓CMF7d · 🎯SLING</sub> | ⚠ CAUTION | Steel ferroalloys power producer Chhattisgarh integrated | 🟡 BULL_OS_L2 | 80 | 🔄41 | ↑1.003 | ↓32d | SQ | -0.5% | -49.44/-54.01 | +1.03% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄21 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [CRISIL](https://in.tradingview.com/chart/?symbol=NSE:CRISIL)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION | Credit ratings research risk advisory financial markets | 📈 BULL_ANY_MID | 99 | 🔄52 | ↑1.015 | ↑1d | SQ | +3.3% | -22.26/-29.79 | +3.28% | 20% |
| [GULFOILLUB](https://in.tradingview.com/chart/?symbol=NSE:GULFOILLUB)<br><sub>📶W9 · 🚀SS · ↑CMF14d</sub> | ✓ SAFE | Automotive lubricants manufacturing distribution Indian commercial vehicles | 📈 BULL_ANY_MID | 99 | 🔄60 | ↑1.010 | ↑1d | SQ | +2.3% | -18.14/-19.94 | +2.34% | 20% |
| [SURYODAY](https://in.tradingview.com/chart/?symbol=NSE:SURYODAY)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Microfinance bank lending unbanked underserved retail borrowers | 📈 BULL_ANY_MID | 99 | 🔄42 | ↑1.001 | ↑1d | SQ | +0.7% | -12.79/-13.14 | +0.73% | 20% |
| [INDPRUD](https://in.tradingview.com/chart/?symbol=NSE:INDPRUD)<br><sub>📶W9 · 🚀SS · ↓CMF2d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.011 | ↑1d | SQ | +2.0% | 5.14/2.33 | +2.01% | 20% |
| [LINDEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LINDEINDIA)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Industrial medical gases cryogenic plants manufacturing India | 📈 BULL_ANY_MID | 94 | 🔄40 | ↑1.018 | ↑1d | SQ | +3.4% | -39.77/-46.67 | +3.42% | 20% |
| [RPGLIFE](https://in.tradingview.com/chart/?symbol=NSE:RPGLIFE)<br><sub>📶W9 · ↑CMF17d</sub> | ✓ SAFE | Pharmaceutical formulations and APIs for domestic international markets | 📈 BULL_ANY_MID | 94 | 🔄76 | ↑1.029 | ↑1d | SQ | +5.6% | -3.82/-5.45 | +5.59% | 20% |
| [VSTTILLERS](https://in.tradingview.com/chart/?symbol=NSE:VSTTILLERS)<br><sub>📶W9 · W↑20d · 🚀SS · ↓CMF1d</sub> | ✓ SAFE | Power tillers and compact tractors for Indian farmers | 📈 BULL_ANY_MID | 92 | 🔄25 | ↑0.998 | ↓3d | SQ | +0.5% | -14.78/-14.95 | +0.55% | 20% |
| [CMRGREEN](https://in.tradingview.com/chart/?symbol=NSE:CMRGREEN)<br><sub>📶W9 · ↑CMF3d</sub> | ✓ SAFE | Recycled aluminium zinc alloys ingots automotive casting | 📈 BULL_ANY_MID | 91 | 🔄50 | ↑1.001 | ↓9d | SQ | -0.6% | -27.47/-27.76 | +0.88% | 20% |
| [MAHLIFE](https://in.tradingview.com/chart/?symbol=NSE:MAHLIFE)<br><sub>📶W9 · ↑CMF5d</sub> | ⚠ CAUTION | Residential and industrial real estate development across India | 📈 BULL_ANY_MID | 85 | 🔄46 | ↑1.003 | ↓15d | SQ | -1.9% | -52.85/-52.96 | +2.03% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑53 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [CASTROLIND](https://in.tradingview.com/chart/?symbol=NSE:CASTROLIND)<br><sub>📶W9 · ↑CMF20d</sub> | ✓ SAFE | Automotive and industrial lubricants manufacturer serving India | 📈 BULL_ANY_MID | 69 | ↑64 | ↑1.006 | ↑1d | SQ | +0.9% | 13.11/12.91 | +0.89% | 20% |
| [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN)<br><sub>📶W9 · ↓CMF14d</sub> | ✓ SAFE | Digital commercialization services for global pharma companies | 📈 BULL_ANY_MID | 69 | ↑77 | ↑1.010 | ↑1d | SQ | +1.6% | -4.72/-9.57 | +1.63% | 20% |
| [JUNIPER](https://in.tradingview.com/chart/?symbol=NSE:JUNIPER)<br><sub>📶W9 · W↑55d · ↓CMF6d</sub> | ⚠ CAUTION | Luxury hotel ownership management Hyatt partnership India portfolio | 📈 BULL_ANY_MID | 68 | ↑52 | ↑1.007 | ↑2d | SQ | +1.5% | -8.62/-14.29 | +0.35% | 20% |
| [GILLETTE](https://in.tradingview.com/chart/?symbol=NSE:GILLETTE)<br><sub>📶W9 · W↑5d · ↑CMF19d</sub> | ⚠ CAUTION | Razor blades shaving cream oral care FMCG grooming | 📈 BULL_ANY_MID | 63 | ↑31 | ↑1.018 | ↑2d | SQ | +3.1% | -11.27/-19.11 | +1.90% | 20% |
| [JKCEMENT](https://in.tradingview.com/chart/?symbol=NSE:JKCEMENT)<br><sub>📶W9 · ↑CMF7d</sub> | ⚠ CAUTION | Cement manufacturing construction materials India domestic markets | 📈 BULL_ANY_MID | 62 | ↑19 | ↑1.000 | ↓8d | SQ | -0.8% | -31.75/-36.77 | +0.37% | 20% |
| [MUNJALAU](https://in.tradingview.com/chart/?symbol=NSE:MUNJALAU)<br><sub>📶W9 · ↑CMF12d · ⚠️TRAP</sub> | ✓ SAFE | Two-wheeler four-wheeler auto components manufacturer | 📈 BULL_ANY_MID | 52 | ↓74 | ↑0.995 | ↓13d | SQ | -2.9% | -35.68/-35.76 | -0.05% | 20% |
| [VINCOFE](https://in.tradingview.com/chart/?symbol=NSE:VINCOFE)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Instant coffee chicory manufacturing export beverages | 📈 BULL_ANY_MID | 40 | ↓77 | ↓0.995 | ↓22d | SQ | +5.9% | 2.42/1.7 | -0.71% | 20% |
| [IRMENERGY](https://in.tradingview.com/chart/?symbol=NSE:IRMENERGY)<br><sub>🚀SS · ↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Natural gas distribution networks serving residential commercial industrial | 🟢 BULL_OVERSOLD | 80 | 🔄42 | ↑1.001 | ↓30d | SQ | -8.3% | -59.48/-60.5 | +3.10% | 20% 🟦 |
| [MRF](https://in.tradingview.com/chart/?symbol=NSE:MRF)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Tyre manufacturer for cars trucks two-wheelers tractors | 🟡 BULL_OS_L2 | 75 | 🔄30 | ↑1.000 | ↓35d | SQ | -7.0% | -52.75/-54.82 | +0.57% | 20% |
| [SHK](https://in.tradingview.com/chart/?symbol=NSE:SHK)<br><sub>🚀SS · ↑CMF0d</sub> | ✓ SAFE | Fragrances flavors aroma chemicals FMCG personal care food beverage | 📈 BULL_ANY_MID | 99 | 🔄32 | ↑1.006 | ↑1d | SQ | +2.4% | -31.51/-32.91 | +2.37% | 20% |
| [BRIGHOTEL](https://in.tradingview.com/chart/?symbol=NSE:BRIGHOTEL)<br><sub>↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 82 | 🔄22 | ↑1.000 | ↓13d | SQ | -0.5% | -39.57/-40.8 | +0.65% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:JTLIND,NSE:WPIL,NSE:KANSAINER,NSE:AIIL,NSE:SAMBHV,NSE:SARDAEN,NSE:ITC,NSE:CRISIL,NSE:GULFOILLUB,NSE:SURYODAY,NSE:INDPRUD,NSE:LINDEINDIA,NSE:RPGLIFE,NSE:VSTTILLERS,NSE:CMRGREEN,NSE:MAHLIFE,NSE:COALINDIA,NSE:CASTROLIND,NSE:INDGN,NSE:JUNIPER,NSE:GILLETTE,NSE:JKCEMENT,NSE:MUNJALAU,NSE:VINCOFE,NSE:IRMENERGY,NSE:MRF,NSE:SHK,NSE:BRIGHOTEL
```

---

### 🔥 MAJOR — PPV confirmed (5)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [RSL](https://in.tradingview.com/chart/?symbol=NSE:RSL)<br><sub>📶W9 · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | Stainless steel bars billets rods domestic international markets | ⚡ BULL_ANY_PPV | 54 | 🔄50 | ↑1.029 | ↑1d | PV | +4.9% | -15.72/-21.61 | +4.87% | 20% |
| [HBLENGINE](https://in.tradingview.com/chart/?symbol=NSE:HBLENGINE)<br><sub>📶W9 · W↑30d · RVOL27x · ↑CMF0d</sub> | ✓ SAFE | Batteries, e-mobility systems, specialized engineering products | ⚡ BULL_ANY_PPV | 49 | 🔄65 | ↑1.108 | ↑1d | PV | +17.4% | -10.14/-16.38 | +17.35% | 20% |
| [SOLARA](https://in.tradingview.com/chart/?symbol=NSE:SOLARA)<br><sub>📶W9 · 🚀SS·22x · ↓CMF9d</sub> | ✓ SAFE | Active pharmaceutical ingredients manufacturing, CRAMS, global pharma supply | ⚡ BULL_ANY_PPV | 49 | 🔄83 | ↑1.036 | ↑1d | PV | +7.5% | -25.6/-31.88 | +7.52% | 20% |
| [THANGAMAYL](https://in.tradingview.com/chart/?symbol=NSE:THANGAMAYL)<br><sub>📶W9 · ↑CMF19d</sub> | ✓ SAFE | Gold silver diamond jewellery retail Tamil Nadu consumer | ⚡ BULL_ANY_PPV | 49 | 🔄87 | ↑1.037 | ↑1d | PV | +5.6% | -26.85/-36.0 | +5.61% | 10% 🟩 |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:RSL,NSE:HBLENGINE,NSE:SOLARA,NSE:THANGAMAYL,NSE:SIGMAADV
```

### 🟢 OVERSOLD — reversal from −53/−60 (14)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄54 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 42 | 🔄51 | ↑0.992 | ↓13d | — | -5.3% | -64.43/-65.64 | +2.00% | 20% |
| [MEDPLUS](https://in.tradingview.com/chart/?symbol=NSE:MEDPLUS)<br><sub>↓CMF17d · DEL95%(T-1) · ⚠️TRAP</sub> | ⚠ CAUTION | Retail pharmacy chain with diagnostic centers nationwide | 🟢 BULL_OVERSOLD | 14 | ↓13 | ↑0.978 | ↓11d | — | -6.5% | -78.85/-78.89 | -0.11% | 20% |
| [HCG](https://in.tradingview.com/chart/?symbol=NSE:HCG)<br><sub>↓CMF5d · ⚠️TRAP</sub> | ⚠ CAUTION | Oncology hospital network, fertility services, India | 🟢 BULL_OVERSOLD | 11 | ↓35 | ↑0.961 | ↓14d | — | -14.9% | -68.81/-70.78 | -0.31% | 20% |
| [RICOAUTO](https://in.tradingview.com/chart/?symbol=NSE:RICOAUTO)<br><sub>↓CMF9d · 🎯SLING</sub> | ✓ SAFE | Precision aluminum ferrous auto components two four wheeler | 🟢 BULL_OVERSOLD | 8 | ↓53 | ↑0.987 | ↓17d | — | -10.2% | -60.9/-61.75 | +2.16% | 20% |
| [RAYMONDLSL](https://in.tradingview.com/chart/?symbol=NSE:RAYMONDLSL)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Branded formal casual ethnic apparel textiles vertical integration | 🟢 BULL_OVERSOLD | 7 | ↓3 | ↑0.967 | ↓18d | — | -12.0% | -63.9/-64.37 | +0.56% | 20% |
| [BETA](https://in.tradingview.com/chart/?symbol=NSE:BETA)<br><sub>↓CMF3d · 🔥PHX</sub> | ✓ SAFE | Oncology drug manufacturer for cancer treatment domestic export | 🟢 BULL_OVERSOLD | 7 | ↓54 | ↑0.967 | ↓18d | — | -15.3% | -74.65/-76.19 | +1.60% | 20% |
| [SCHAEFFLER](https://in.tradingview.com/chart/?symbol=NSE:SCHAEFFLER)<br><sub>↓CMF5d · 🎯SLING</sub> | ⚠ CAUTION | Bearings and drivetrain components for automotive and industry | 🟢 BULL_OVERSOLD | 5 | ↓34 | ↑0.987 | ↓22d | — | -5.9% | -59.35/-60.88 | +0.66% | 20% |
| [GANESHHOU](https://in.tradingview.com/chart/?symbol=NSE:GANESHHOU)<br><sub>🚀SS · ↓CMF26d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Residential real estate development Ahmedabad Gujarat region | 🟢 BULL_OVERSOLD | 5 | ↓33 | ↑0.993 | ↓47d | — | -9.9% | -59.35/-60.52 | +1.59% | 20% |
| [GKENERGY](https://in.tradingview.com/chart/?symbol=NSE:GKENERGY)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Solar pump EPC services for Indian agriculture | 🟢 BULL_OVERSOLD | 0 | ↓7 | ↓0.966 | ↓20d | — | -10.3% | -63.12/-63.92 | -1.28% | 20% |
| [LINCOLN](https://in.tradingview.com/chart/?symbol=NSE:LINCOLN)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Injectable antibiotics and cardiac drugs manufacturer | 🟢 BULL_OVERSOLD | 0 | ↓52 | ↓0.979 | ↓34d | — | -10.1% | -60.77/-61.68 | -1.91% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 41 | 🔄36 | ↑1.001 | ↓19d | — | -4.4% | -53.92/-57.54 | +1.19% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 22 | ↑66 | ↑1.004 | ↓8d | — | -0.3% | -53.58/-59.08 | +0.30% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GAIL,NSE:TMCV,NSE:JSWSTEEL,NSE:MEDPLUS,NSE:HCG,NSE:RICOAUTO,NSE:RAYMONDLSL,NSE:BETA,NSE:SCHAEFFLER,NSE:GANESHHOU,NSE:GKENERGY,NSE:LINCOLN,NSE:BPCL,NSE:ADANIPOWER
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (19)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [DBL](https://in.tradingview.com/chart/?symbol=NSE:DBL)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Highway and bridge construction, roads infrastructure sector | 📈 BULL_ANY_MID | 59 | 🔄36 | ↑1.010 | ↑1d | — | +2.8% | -37.38/-39.76 | +2.76% | 20% |
| [MOL](https://in.tradingview.com/chart/?symbol=NSE:MOL)<br><sub>📶W9 · 🚀SS · ↓CMF19d</sub> | ✓ SAFE | Agrochemicals and pigments manufacturer for farms and coatings | 📈 BULL_ANY_MID | 54 | 🔄52 | ↑1.023 | ↑1d | — | +5.3% | -16.4/-20.44 | +5.29% | 20% |
| [GEOJITFSL](https://in.tradingview.com/chart/?symbol=NSE:GEOJITFSL)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Stock broking and portfolio management for retail investors | 📈 BULL_ANY_MID | 51 | 🔄56 | ↑1.005 | ↓9d | — | +0.5% | -35.85/-37.86 | +1.71% | 20% |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Pistons rings valves manufacturer automotive OEM export | 📈 BULL_ANY_MID | 49 | 🔄85 | ↑1.046 | ↑1d | — | +6.7% | -15.51/-23.71 | +6.68% | 20% |
| [JMFINANCIL](https://in.tradingview.com/chart/?symbol=NSE:JMFINANCIL)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Investment banking mortgage lending distressed credit asset management | 📈 BULL_ANY_MID | 47 | 🔄32 | ↑1.003 | ↓13d | — | -3.5% | -46.04/-48.67 | +1.73% | 20% |
| [PARADEEP](https://in.tradingview.com/chart/?symbol=NSE:PARADEEP)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Phosphate fertilizer manufacturer for Indian agriculture sector | 📈 BULL_ANY_MID | 46 | 🔄55 | ↑0.996 | ↓9d | — | -4.2% | -43.97/-45.27 | +0.86% | 20% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>📶W9 · 🚀SS · ↓CMF17d · DEL75%(T-1)</sub> | ✓ SAFE | CDMO and critical care generics pharma manufacturing | 📈 BULL_ANY_MID | 40 | 🔄71 | ↑1.001 | ↓20d | — | -5.0% | -50.85/-52.67 | +1.92% | 20% |
| [PFOCUS](https://in.tradingview.com/chart/?symbol=NSE:PFOCUS)<br><sub>📶W9 · 🚀SS · ↓CMF11d</sub> | ✓ SAFE | VFX animation post-production services for film television | 📈 BULL_ANY_MID | 35 | 🔄73 | ↑1.016 | ↓32d | — | +3.5% | -28.73/-32.02 | +4.63% | 20% |
| [DOLPHIN](https://in.tradingview.com/chart/?symbol=NSE:DOLPHIN)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Underwater services marine operations offshore oil gas construction | 📈 BULL_ANY_MID | 24 | ↑94 | ↑1.016 | ↑1d | — | +2.3% | -10.34/-12.94 | +2.26% | 20% 🟦 |
| [KAPSTON](https://in.tradingview.com/chart/?symbol=NSE:KAPSTON)<br><sub>📶W9 · ↓CMF15d</sub> | ✓ SAFE | Security guarding and facility management staffing services | 📈 BULL_ANY_MID | 2 | ↑97 | ↓1.000 | ↓18d | — | -5.5% | -40.17/-43.34 | -0.64% | 20% |
| [GSFC](https://in.tradingview.com/chart/?symbol=NSE:GSFC)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Fertilizers and industrial chemicals manufacturer for agriculture | 📈 BULL_ANY_MID | 51 | 🔄30 | ↑1.003 | ↓9d | — | +1.1% | -44.93/-46.79 | +1.53% | 20% |
| [PINELABS](https://in.tradingview.com/chart/?symbol=NSE:PINELABS)<br><sub>↓CMF5d · ⚠️TRAP</sub> | ✓ SAFE | Payment processing and POS solutions for Indian merchants | 📈 BULL_ANY_MID | 12 | ↓50 | ↓0.982 | ↓8d | — | -4.5% | -23.86/-23.96 | -1.47% | 20% |
| [NDRAUTO](https://in.tradingview.com/chart/?symbol=NSE:NDRAUTO)<br><sub>↓CMF2d</sub> | ⚠ CAUTION | Automotive seat frames trims supplier passenger vehicles OEM | 📈 BULL_ANY_MID | 11 | ↓25 | ↑0.995 | ↓14d | — | -4.4% | -42.09/-42.17 | +1.44% | 20% |
| [JINDALSTEL](https://in.tradingview.com/chart/?symbol=NSE:JINDALSTEL)<br><sub>↓CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 8 | ↓47 | ↑0.982 | ↓17d | — | -8.9% | -51.85/-52.67 | +0.08% | 20% |
| [ULTRAMAR](https://in.tradingview.com/chart/?symbol=NSE:ULTRAMAR)<br><sub>↓CMF12d</sub> | ✓ SAFE | Inorganic pigments surfactants manufacturer serving paints textiles | 📈 BULL_ANY_MID | 8 | ↓50 | ↑0.990 | ↓17d | — | -6.8% | -49.08/-49.16 | +0.75% | 20% |
| [OBEROIRLTY](https://in.tradingview.com/chart/?symbol=NSE:OBEROIRLTY)<br><sub>↓CMF0d · ⚠️TRAP</sub> | ✓ SAFE | Premium residential and commercial property developer Mumbai | 📈 BULL_ANY_MID | 5 | ↓48 | ↑0.991 | ↓20d | — | -4.6% | -40.8/-40.95 | -0.11% | 20% |
| [NOCIL](https://in.tradingview.com/chart/?symbol=NSE:NOCIL)<br><sub>↓CMF7d · DEL64%(T-1)</sub> | ✓ SAFE | Rubber chemicals manufacturer for tire and industrial processing | 📈 BULL_ANY_MID | 5 | ↓55 | ↑0.993 | ↓38d | — | +1.1% | -27.78/-27.8 | +1.38% | 20% |
| [METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS)<br><sub>🚀SS · ↓CMF13d</sub> | ⚠ CAUTION | Diagnostic pathology labs urban semi-urban India Africa Middle East | 📈 BULL_ANY_MID | 5 | ↓59 | ↑0.992 | ↓22d | — | -8.7% | -47.47/-48.24 | +2.38% | 20% |
| [EPIGRAL](https://in.tradingview.com/chart/?symbol=NSE:EPIGRAL)<br><sub>↓CMF19d · ÷DIV</sub> | ⚠ CAUTION | Chlor-alkali and specialty chemicals for industrial applications | 📈 BULL_ANY_MID | 5 | ↓14 | ↑0.994 | ↓42d | — | -8.0% | -50.41/-51.19 | +1.99% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:DBL,NSE:MOL,NSE:GEOJITFSL,NSE:SHRIPISTON,NSE:JMFINANCIL,NSE:PARADEEP,NSE:PPLPHARMA,NSE:PFOCUS,NSE:DOLPHIN,NSE:KAPSTON,NSE:GSFC,NSE:PINELABS,NSE:NDRAUTO,NSE:JINDALSTEL,NSE:ULTRAMAR,NSE:OBEROIRLTY,NSE:NOCIL,NSE:METROPOLIS,NSE:EPIGRAL
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
