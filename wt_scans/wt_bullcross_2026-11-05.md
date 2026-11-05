> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-11-05
*Generated 2026-11-05 15:50 IST*

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

**Total bull crosses today: 109** · 35 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MBEL,NSE:RBA,NSE:DEVYANI,NSE:CANTABIL,NSE:BLUSPRING,NSE:PWL,NSE:TEXINFRA,NSE:PARACABLES,NSE:SIGMAADV,NSE:PIDILITIND,NSE:BPCL,NSE:TATASTEEL,NSE:KARURVYSYA,NSE:5PAISA,NSE:SYSTMTXC,NSE:MEESHO,NSE:SHADOWFAX,NSE:GNA,NSE:BHAGERIA,NSE:COALINDIA,NSE:PTCIL,NSE:WSTCSTPAPR,NSE:SKYGOLD,NSE:BBOX,NSE:NEOGEN,NSE:ONEPOINT,NSE:KOPRAN,NSE:TATAELXSI,NSE:ZENSARTECH,NSE:ONGC,NSE:SHRINGARMS,NSE:TARIL,NSE:SSWL,NSE:CCAVENUE,NSE:SOUTHBANK,NSE:KALPATARU,NSE:SAPPHIRE,NSE:SIGNATURE,NSE:STUDDS,NSE:ASIANHOTNR,NSE:WALCHANNAG,NSE:VMART,NSE:CIEINDIA,NSE:IGL,NSE:TI,NSE:SARDAEN,NSE:VAIBHAVGBL,NSE:UGROCAP,NSE:EQUITASBNK,NSE:SFL,NSE:VINATIORGA,NSE:NOCIL,NSE:VISHNU,NSE:NIITMTS,NSE:BHAGCHEM,NSE:ATULAUTO,NSE:WONDERLA,NSE:ZEEL,NSE:BAJAJELEC,NSE:SENORES,NSE:LINCOLN,NSE:NSIL,NSE:GLOBUSSPR,NSE:VESUVIUS,NSE:AADHARHFC,NSE:BETA,NSE:HEIDELBERG,NSE:NAUKRI,NSE:SUPRIYA,NSE:ICRA,NSE:HUHTAMAKI,NSE:HINDWAREAP,NSE:CRAFTSMAN,NSE:SCHAEFFLER,NSE:CSBBANK,NSE:INNOVACAP,NSE:PARAS,NSE:INDSWFTLAB,NSE:VARROC,NSE:SOLARA,NSE:CYIENTDLM,NSE:RECLTD,NSE:CUB,NSE:KNACK,NSE:RISHABH,NSE:STARHEALTH,NSE:DCBBANK,NSE:BAJAJHCARE,NSE:AURUM,NSE:AETHER,NSE:VINDHYATEL,NSE:GOODLUCK,NSE:EPACK,NSE:LLOYDSENGG,NSE:OMAXE,NSE:PNCINFRA,NSE:WELCORP,NSE:JUSTDIAL,NSE:PNBHOUSING,NSE:FILATEX,NSE:HDFCLIFE,NSE:DCMSHRIRAM,NSE:KSCL,NSE:SIRCA,NSE:AWL,NSE:PAUSHAKLTD,NSE:NIACL,NSE:DHAMPURSUG,NSE:RAMRAT
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (35)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MBEL](https://in.tradingview.com/chart/?symbol=NSE:MBEL)<br><sub>📶W9 · W↑24d · 🚀SS · ↑CMF21d</sub> | ✓ SAFE | Pre-engineered steel buildings and roofing for industrial infrastructure | ⚡ BULL_ANY_PPV | 89 | 🔄39 | ↑1.087 | ↑1d | SQ·PV | +11.8% | 1.56/-8.5 | +11.82% | 20% |
| [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA)<br><sub>📶W9 · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Burger King franchisee operating QSR restaurants India Indonesia | ⚡ BULL_ANY_PPV | 89 | 🔄84 | ↑1.038 | ↑1d | SQ·PV | +5.2% | -18.23/-24.29 | +5.18% | 20% 🟦 |
| [DEVYANI](https://in.tradingview.com/chart/?symbol=NSE:DEVYANI)<br><sub>📶W9 · 🚀SS·8x · ↑CMF0d</sub> | ✓ SAFE | Yum Brands franchisee, QSR operator, KFC Dominos Pizza Hut | ⚡ BULL_ANY_PPV | 89 | 🔄46 | ↑1.066 | ↑1d | SQ·PV | +8.9% | -19.02/-31.25 | +8.87% | 20% |
| [CANTABIL](https://in.tradingview.com/chart/?symbol=NSE:CANTABIL)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF17d</sub> | ✓ SAFE | Apparel design manufacturing retail through exclusive brand stores | ⚡ BULL_ANY_PPV | 88 | 🔄68 | ↑1.033 | ↑2d | SQ·PV | +5.6% | 39.37/35.91 | +3.32% | 20% |
| [BLUSPRING](https://in.tradingview.com/chart/?symbol=NSE:BLUSPRING)<br><sub>📶W9 · 🚀SS · ★ · ↑CMF30d</sub> | ✓ SAFE | Infrastructure management services for commercial facilities operations | ⚡ BULL_ANY_PPV | 58 | ↑98 | ↑1.081 | ↑2d | SQ·PV | +15.8% | 9.24/0.29 | +6.85% | 20% 🟦 |
| [PWL](https://in.tradingview.com/chart/?symbol=NSE:PWL)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Online test prep and upskilling courses for competitive exams | ⚡ BULL_ANY_PPV | 24 | ↓50 | ↑1.020 | ↑1d | PV | +3.8% | 2.21/-4.92 | +3.76% | 20% |
| [TEXINFRA](https://in.tradingview.com/chart/?symbol=NSE:TEXINFRA)<br><sub>📶W9 · 🚀SS · ↑CMF1d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 24 | ↓76 | ↑1.017 | ↑1d | PV | +2.0% | -14.69/-17.9 | +2.02% | 20% |
| [PARACABLES](https://in.tradingview.com/chart/?symbol=NSE:PARACABLES)<br><sub>📶W9 · W↑9d · ↑CMF14d</sub> | ✓ SAFE | Power telecom railway cables manufacturer | ⚡ BULL_ANY_PPV | 17 | ↑87 | ↑1.076 | ↑3d | PV | +12.2% | 27.56/18.35 | +5.88% | 20% 🟦 |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · ↑CMF2d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 29 | ↑57 | ↑1.012 | ↑1d | — | +1.2% | -51.83/-59.38 | +1.19% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>📶W9 · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄39 | ↑1.008 | ↑1d | SQ | +2.4% | -31.16/-35.83 | +2.40% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄46 | ↑1.028 | ↑1d | SQ | +5.4% | -42.83/-51.21 | +5.43% | 20% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>📶W9 · W↑19d · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Private bank retail deposits lending commercial operations | 📈 BULL_ANY_MID | 89 | 🔄79 | ↑1.032 | ↑1d | SQ | +4.8% | 15.63/14.9 | +4.83% | 20% |
| [5PAISA](https://in.tradingview.com/chart/?symbol=NSE:5PAISA)<br><sub>📶W9 · 🚀SS · ↓CMF3d</sub> | ⚠ CAUTION | Digital discount brokerage for equities, derivatives, commodities trading | 📈 BULL_ANY_MID | 89 | 🔄57 | ↑1.032 | ↑1d | SQ | +4.3% | -12.91/-21.9 | +4.28% | 20% |
| [SYSTMTXC](https://in.tradingview.com/chart/?symbol=NSE:SYSTMTXC)<br><sub>📶W9 · W↑41d · ↓CMF10d · DEL85%</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 68 | ↓58 | ↑1.007 | ↑2d | SQ | +3.0% | 17.49/16.3 | +0.30% | 2% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 64 | ↓50 | ↑1.004 | ↓6d | SQ | +0.4% | -1.58/-2.79 | +0.67% | 20% |
| [SHADOWFAX](https://in.tradingview.com/chart/?symbol=NSE:SHADOWFAX)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Digital commerce logistics network, express delivery, asset-light model | 📈 BULL_ANY_MID | 64 | ↓50 | ↑1.026 | ↑1d | SQ | +4.3% | 2.2/-1.45 | +4.32% | 20% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>📶W9 · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Rear axles and drive shafts for commercial vehicles | 📈 BULL_ANY_MID | 64 | ↓87 | ↑1.018 | ↑1d | SQ | +2.0% | -4.99/-9.36 | +1.96% | 20% |
| [BHAGERIA](https://in.tradingview.com/chart/?symbol=NSE:BHAGERIA)<br><sub>📶W9 · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Dye intermediates, specialty dyes, chemicals manufacturer | 📈 BULL_ANY_MID | 64 | ↓98 | ↑1.021 | ↑1d | SQ | +4.3% | 6.31/5.87 | +4.33% | 10% 🟩 |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄54 | ↑1.014 | ↑1d | — | +4.5% | -47.75/-50.99 | +4.51% | 20% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Precision metal components aerospace defense oil-gas marine | 📈 BULL_ANY_MID | 58 | ↓89 | ↓1.003 | ↓2d | SQ | +1.7% | 10.73/7.55 | -0.35% | 20% |
| [WSTCSTPAPR](https://in.tradingview.com/chart/?symbol=NSE:WSTCSTPAPR)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Paper, paperboard, optical fiber cables manufacturing India | 📈 BULL_ANY_MID | 58 | ↓96 | ↓1.017 | ↑2d | SQ | +3.8% | 28.69/25.53 | +0.24% | 20% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>📶W9 · 🚀SS · ↑CMF20d</sub> | ✓ SAFE | Gold jewelry manufacturer selling to retail jewelers B2B | 📈 BULL_ANY_MID | 54 | 🔄98 | ↑1.030 | ↑1d | — | +2.4% | 7.5/5.72 | +2.36% | 20% |
| [BBOX](https://in.tradingview.com/chart/?symbol=NSE:BBOX)<br><sub>📶W9 · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Digital infrastructure integration, managed services, enterprise networks | 📈 BULL_ANY_MID | 49 | 🔄86 | ↑1.040 | ↑1d | — | +6.1% | -11.21/-15.32 | +6.09% | 20% 🟦 |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>📶W9 · 🚀SS · ↓CMF11d</sub> | ✓ SAFE | Bromine lithium specialty chemicals pharma agri-chem | 📈 BULL_ANY_MID | 49 | 🔄92 | ↑1.061 | ↑1d | — | +5.9% | -16.76/-26.67 | +5.91% | 20% |
| [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT)<br><sub>📶W9 · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | BPM services: customer care, technical support, back-office processing | 📈 BULL_ANY_MID | 49 | 🔄91 | ↑1.043 | ↑1d | — | +6.0% | -3.48/-7.15 | +5.96% | 20% |
| [KOPRAN](https://in.tradingview.com/chart/?symbol=NSE:KOPRAN)<br><sub>📶W9 · 🚀SS · ↑CMF2d</sub> | ✓ SAFE | APIs and formulations manufacturer serving global pharma | 📈 BULL_ANY_MID | 49 | 🔄95 | ↑1.046 | ↑1d | — | +6.1% | -27.07/-33.85 | +6.14% | 20% |
| [TATAELXSI](https://in.tradingview.com/chart/?symbol=NSE:TATAELXSI)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF17d</sub> | ✓ SAFE | Design engineering services for automotive media healthcare | 📈 BULL_ANY_MID | 31 | 🔄37 | ↑1.039 | ↑19d | — | +25.2% | 32.97/29.51 | +4.39% | 20% |
| [ZENSARTECH](https://in.tradingview.com/chart/?symbol=NSE:ZENSARTECH)<br><sub>📶W9 · W↑24d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE | Digital solutions and IT services for global enterprises | 📈 BULL_ANY_MID | 30 | 🔄61 | ↑1.068 | ↑25d | — | +30.2% | 61.48/59.84 | +6.14% | 20% |
| [ONGC](https://in.tradingview.com/chart/?symbol=NSE:ONGC)<br><sub>📶W9 · W↑6d · 🚀SS · ↑CMF4d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 22 | ↑45 | ↑1.026 | ↑3d | — | +3.7% | 12.73/0.87 | +3.45% | 20% |
| [SHRINGARMS](https://in.tradingview.com/chart/?symbol=NSE:SHRINGARMS)<br><sub>📶W9 · W↑24d · ↑CMF18d</sub> | ✓ SAFE | Mangalsutra manufacturer, 18k 22k gold, Indian women bridal wear | 📈 BULL_ANY_MID | 18 | ↑90 | ↑1.081 | ↑2d | — | +13.2% | 25.34/19.0 | +7.12% | 10% 🟨 |
| [TARIL](https://in.tradingview.com/chart/?symbol=NSE:TARIL)<br><sub>📶W9 · W↑19d · ↑CMF3d</sub> | ✓ SAFE | Power transformers, furnace transformers, electrical equipment manufacturing | 📈 BULL_ANY_MID | 18 | ↓63 | ↓1.014 | ↑2d | — | +4.7% | 10.38/5.3 | -0.61% | 20% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>📶W9 · W↑49d · ★ · ↑CMF23d</sub> | ✓ SAFE | Steel and alloy wheel rims manufacturer for automobiles | 📈 BULL_ANY_MID | 10 | ↑98 | ↓1.057 | ↑10d | — | +36.0% | 60.35/59.06 | -1.03% | 20% |
| [CCAVENUE](https://in.tradingview.com/chart/?symbol=NSE:CCAVENUE)<br><sub>📶W9 · W↑14d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 6 | ↑100 | ↑1.124 | ↑14d | — | +801.1% | 41.52/41.16 | +5.08% | 20% |
| [SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK)<br><sub>📶W9 · W↑34d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓88 | ↑1.028 | ↑20d | — | +21.4% | 55.64/55.0 | +0.84% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MBEL,NSE:RBA,NSE:DEVYANI,NSE:CANTABIL,NSE:BLUSPRING,NSE:PWL,NSE:TEXINFRA,NSE:PARACABLES,NSE:SIGMAADV,NSE:PIDILITIND,NSE:BPCL,NSE:TATASTEEL,NSE:KARURVYSYA,NSE:5PAISA,NSE:SYSTMTXC,NSE:MEESHO,NSE:SHADOWFAX,NSE:GNA,NSE:BHAGERIA,NSE:COALINDIA,NSE:PTCIL,NSE:WSTCSTPAPR,NSE:SKYGOLD,NSE:BBOX,NSE:NEOGEN,NSE:ONEPOINT,NSE:KOPRAN,NSE:TATAELXSI,NSE:ZENSARTECH,NSE:ONGC,NSE:SHRINGARMS,NSE:TARIL,NSE:SSWL,NSE:CCAVENUE,NSE:SOUTHBANK
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (27)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MBEL](https://in.tradingview.com/chart/?symbol=NSE:MBEL)<br><sub>📶W9 · W↑24d · 🚀SS · ↑CMF21d</sub> | ✓ SAFE | Pre-engineered steel buildings and roofing for industrial infrastructure | ⚡ BULL_ANY_PPV | 89 | 🔄39 | ↑1.087 | ↑1d | SQ·PV | +11.8% | 1.56/-8.5 | +11.82% | 20% |
| [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA)<br><sub>📶W9 · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Burger King franchisee operating QSR restaurants India Indonesia | ⚡ BULL_ANY_PPV | 89 | 🔄84 | ↑1.038 | ↑1d | SQ·PV | +5.2% | -18.23/-24.29 | +5.18% | 20% 🟦 |
| [DEVYANI](https://in.tradingview.com/chart/?symbol=NSE:DEVYANI)<br><sub>📶W9 · 🚀SS·8x · ↑CMF0d</sub> | ✓ SAFE | Yum Brands franchisee, QSR operator, KFC Dominos Pizza Hut | ⚡ BULL_ANY_PPV | 89 | 🔄46 | ↑1.066 | ↑1d | SQ·PV | +8.9% | -19.02/-31.25 | +8.87% | 20% |
| [CANTABIL](https://in.tradingview.com/chart/?symbol=NSE:CANTABIL)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF17d</sub> | ✓ SAFE | Apparel design manufacturing retail through exclusive brand stores | ⚡ BULL_ANY_PPV | 88 | 🔄68 | ↑1.033 | ↑2d | SQ·PV | +5.6% | 39.37/35.91 | +3.32% | 20% |
| [BLUSPRING](https://in.tradingview.com/chart/?symbol=NSE:BLUSPRING)<br><sub>📶W9 · 🚀SS · ★ · ↑CMF30d</sub> | ✓ SAFE | Infrastructure management services for commercial facilities operations | ⚡ BULL_ANY_PPV | 58 | ↑98 | ↑1.081 | ↑2d | SQ·PV | +15.8% | 9.24/0.29 | +6.85% | 20% 🟦 |
| [PARACABLES](https://in.tradingview.com/chart/?symbol=NSE:PARACABLES)<br><sub>📶W9 · W↑9d · ↑CMF14d</sub> | ✓ SAFE | Power telecom railway cables manufacturer | ⚡ BULL_ANY_PPV | 17 | ↑87 | ↑1.076 | ↑3d | PV | +12.2% | 27.56/18.35 | +5.88% | 20% 🟦 |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · ↑CMF2d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 29 | ↑57 | ↑1.012 | ↑1d | — | +1.2% | -51.83/-59.38 | +1.19% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>📶W9 · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄39 | ↑1.008 | ↑1d | SQ | +2.4% | -31.16/-35.83 | +2.40% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄46 | ↑1.028 | ↑1d | SQ | +5.4% | -42.83/-51.21 | +5.43% | 20% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>📶W9 · W↑19d · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Private bank retail deposits lending commercial operations | 📈 BULL_ANY_MID | 89 | 🔄79 | ↑1.032 | ↑1d | SQ | +4.8% | 15.63/14.9 | +4.83% | 20% |
| [5PAISA](https://in.tradingview.com/chart/?symbol=NSE:5PAISA)<br><sub>📶W9 · 🚀SS · ↓CMF3d</sub> | ⚠ CAUTION | Digital discount brokerage for equities, derivatives, commodities trading | 📈 BULL_ANY_MID | 89 | 🔄57 | ↑1.032 | ↑1d | SQ | +4.3% | -12.91/-21.9 | +4.28% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄54 | ↑1.014 | ↑1d | — | +4.5% | -47.75/-50.99 | +4.51% | 20% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>📶W9 · 🚀SS · ↑CMF20d</sub> | ✓ SAFE | Gold jewelry manufacturer selling to retail jewelers B2B | 📈 BULL_ANY_MID | 54 | 🔄98 | ↑1.030 | ↑1d | — | +2.4% | 7.5/5.72 | +2.36% | 20% |
| [BBOX](https://in.tradingview.com/chart/?symbol=NSE:BBOX)<br><sub>📶W9 · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Digital infrastructure integration, managed services, enterprise networks | 📈 BULL_ANY_MID | 49 | 🔄86 | ↑1.040 | ↑1d | — | +6.1% | -11.21/-15.32 | +6.09% | 20% 🟦 |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>📶W9 · 🚀SS · ↓CMF11d</sub> | ✓ SAFE | Bromine lithium specialty chemicals pharma agri-chem | 📈 BULL_ANY_MID | 49 | 🔄92 | ↑1.061 | ↑1d | — | +5.9% | -16.76/-26.67 | +5.91% | 20% |
| [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT)<br><sub>📶W9 · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | BPM services: customer care, technical support, back-office processing | 📈 BULL_ANY_MID | 49 | 🔄91 | ↑1.043 | ↑1d | — | +6.0% | -3.48/-7.15 | +5.96% | 20% |
| [KOPRAN](https://in.tradingview.com/chart/?symbol=NSE:KOPRAN)<br><sub>📶W9 · 🚀SS · ↑CMF2d</sub> | ✓ SAFE | APIs and formulations manufacturer serving global pharma | 📈 BULL_ANY_MID | 49 | 🔄95 | ↑1.046 | ↑1d | — | +6.1% | -27.07/-33.85 | +6.14% | 20% |
| [TATAELXSI](https://in.tradingview.com/chart/?symbol=NSE:TATAELXSI)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF17d</sub> | ✓ SAFE | Design engineering services for automotive media healthcare | 📈 BULL_ANY_MID | 31 | 🔄37 | ↑1.039 | ↑19d | — | +25.2% | 32.97/29.51 | +4.39% | 20% |
| [ZENSARTECH](https://in.tradingview.com/chart/?symbol=NSE:ZENSARTECH)<br><sub>📶W9 · W↑24d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE | Digital solutions and IT services for global enterprises | 📈 BULL_ANY_MID | 30 | 🔄61 | ↑1.068 | ↑25d | — | +30.2% | 61.48/59.84 | +6.14% | 20% |
| [ONGC](https://in.tradingview.com/chart/?symbol=NSE:ONGC)<br><sub>📶W9 · W↑6d · 🚀SS · ↑CMF4d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 22 | ↑45 | ↑1.026 | ↑3d | — | +3.7% | 12.73/0.87 | +3.45% | 20% |
| [SHRINGARMS](https://in.tradingview.com/chart/?symbol=NSE:SHRINGARMS)<br><sub>📶W9 · W↑24d · ↑CMF18d</sub> | ✓ SAFE | Mangalsutra manufacturer, 18k 22k gold, Indian women bridal wear | 📈 BULL_ANY_MID | 18 | ↑90 | ↑1.081 | ↑2d | — | +13.2% | 25.34/19.0 | +7.12% | 10% 🟨 |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>📶W9 · W↑49d · ★ · ↑CMF23d</sub> | ✓ SAFE | Steel and alloy wheel rims manufacturer for automobiles | 📈 BULL_ANY_MID | 10 | ↑98 | ↓1.057 | ↑10d | — | +36.0% | 60.35/59.06 | -1.03% | 20% |
| [CCAVENUE](https://in.tradingview.com/chart/?symbol=NSE:CCAVENUE)<br><sub>📶W9 · W↑14d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 6 | ↑100 | ↑1.124 | ↑14d | — | +801.1% | 41.52/41.16 | +5.08% | 20% |
| [SAPPHIRE](https://in.tradingview.com/chart/?symbol=NSE:SAPPHIRE)<br><sub>🚀SS · ↑CMF8d</sub> | ⚠ CAUTION | KFC Pizza Hut franchisee quick service restaurants India | ⚡ BULL_ANY_PPV | 89 | 🔄45 | ↑1.055 | ↑1d | SQ·PV | +8.6% | -18.39/-28.66 | +8.61% | 20% |
| [ASIANHOTNR](https://in.tradingview.com/chart/?symbol=NSE:ASIANHOTNR)<br><sub>RVOL9x · ↓CMF28d</sub> | ⚠ CAUTION | Luxury hotel operations, Delhi, high-end accommodation | ⚡ BULL_ANY_PPV | 49 | 🔄64 | ↑1.056 | ↑1d | PV | +10.0% | -34.24/-43.51 | +10.02% | 20% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>🚀SS · ↑CMF21d</sub> | ✓ SAFE | Electronics manufacturing design testing mission-critical defense aerospace systems | 📈 BULL_ANY_MID | 49 | 🔄96 | ↑1.045 | ↑1d | — | +8.0% | -19.99/-23.6 | +7.97% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MBEL,NSE:RBA,NSE:DEVYANI,NSE:CANTABIL,NSE:BLUSPRING,NSE:PARACABLES,NSE:SIGMAADV,NSE:PIDILITIND,NSE:BPCL,NSE:TATASTEEL,NSE:KARURVYSYA,NSE:5PAISA,NSE:COALINDIA,NSE:SKYGOLD,NSE:BBOX,NSE:NEOGEN,NSE:ONEPOINT,NSE:KOPRAN,NSE:TATAELXSI,NSE:ZENSARTECH,NSE:ONGC,NSE:SHRINGARMS,NSE:SSWL,NSE:CCAVENUE,NSE:SAPPHIRE,NSE:ASIANHOTNR,NSE:CYIENTDLM
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (35)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MBEL](https://in.tradingview.com/chart/?symbol=NSE:MBEL)<br><sub>📶W9 · W↑24d · 🚀SS · ↑CMF21d</sub> | ✓ SAFE | Pre-engineered steel buildings and roofing for industrial infrastructure | ⚡ BULL_ANY_PPV | 89 | 🔄39 | ↑1.087 | ↑1d | SQ·PV | +11.8% | 1.56/-8.5 | +11.82% | 20% |
| [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA)<br><sub>📶W9 · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Burger King franchisee operating QSR restaurants India Indonesia | ⚡ BULL_ANY_PPV | 89 | 🔄84 | ↑1.038 | ↑1d | SQ·PV | +5.2% | -18.23/-24.29 | +5.18% | 20% 🟦 |
| [DEVYANI](https://in.tradingview.com/chart/?symbol=NSE:DEVYANI)<br><sub>📶W9 · 🚀SS·8x · ↑CMF0d</sub> | ✓ SAFE | Yum Brands franchisee, QSR operator, KFC Dominos Pizza Hut | ⚡ BULL_ANY_PPV | 89 | 🔄46 | ↑1.066 | ↑1d | SQ·PV | +8.9% | -19.02/-31.25 | +8.87% | 20% |
| [CANTABIL](https://in.tradingview.com/chart/?symbol=NSE:CANTABIL)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF17d</sub> | ✓ SAFE | Apparel design manufacturing retail through exclusive brand stores | ⚡ BULL_ANY_PPV | 88 | 🔄68 | ↑1.033 | ↑2d | SQ·PV | +5.6% | 39.37/35.91 | +3.32% | 20% |
| [BLUSPRING](https://in.tradingview.com/chart/?symbol=NSE:BLUSPRING)<br><sub>📶W9 · 🚀SS · ★ · ↑CMF30d</sub> | ✓ SAFE | Infrastructure management services for commercial facilities operations | ⚡ BULL_ANY_PPV | 58 | ↑98 | ↑1.081 | ↑2d | SQ·PV | +15.8% | 9.24/0.29 | +6.85% | 20% 🟦 |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>📶W9 · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄39 | ↑1.008 | ↑1d | SQ | +2.4% | -31.16/-35.83 | +2.40% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄46 | ↑1.028 | ↑1d | SQ | +5.4% | -42.83/-51.21 | +5.43% | 20% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>📶W9 · W↑19d · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Private bank retail deposits lending commercial operations | 📈 BULL_ANY_MID | 89 | 🔄79 | ↑1.032 | ↑1d | SQ | +4.8% | 15.63/14.9 | +4.83% | 20% |
| [5PAISA](https://in.tradingview.com/chart/?symbol=NSE:5PAISA)<br><sub>📶W9 · 🚀SS · ↓CMF3d</sub> | ⚠ CAUTION | Digital discount brokerage for equities, derivatives, commodities trading | 📈 BULL_ANY_MID | 89 | 🔄57 | ↑1.032 | ↑1d | SQ | +4.3% | -12.91/-21.9 | +4.28% | 20% |
| [SYSTMTXC](https://in.tradingview.com/chart/?symbol=NSE:SYSTMTXC)<br><sub>📶W9 · W↑41d · ↓CMF10d · DEL85%</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 68 | ↓58 | ↑1.007 | ↑2d | SQ | +3.0% | 17.49/16.3 | +0.30% | 2% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 64 | ↓50 | ↑1.004 | ↓6d | SQ | +0.4% | -1.58/-2.79 | +0.67% | 20% |
| [SHADOWFAX](https://in.tradingview.com/chart/?symbol=NSE:SHADOWFAX)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Digital commerce logistics network, express delivery, asset-light model | 📈 BULL_ANY_MID | 64 | ↓50 | ↑1.026 | ↑1d | SQ | +4.3% | 2.2/-1.45 | +4.32% | 20% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>📶W9 · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Rear axles and drive shafts for commercial vehicles | 📈 BULL_ANY_MID | 64 | ↓87 | ↑1.018 | ↑1d | SQ | +2.0% | -4.99/-9.36 | +1.96% | 20% |
| [BHAGERIA](https://in.tradingview.com/chart/?symbol=NSE:BHAGERIA)<br><sub>📶W9 · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Dye intermediates, specialty dyes, chemicals manufacturer | 📈 BULL_ANY_MID | 64 | ↓98 | ↑1.021 | ↑1d | SQ | +4.3% | 6.31/5.87 | +4.33% | 10% 🟩 |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Precision metal components aerospace defense oil-gas marine | 📈 BULL_ANY_MID | 58 | ↓89 | ↓1.003 | ↓2d | SQ | +1.7% | 10.73/7.55 | -0.35% | 20% |
| [WSTCSTPAPR](https://in.tradingview.com/chart/?symbol=NSE:WSTCSTPAPR)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Paper, paperboard, optical fiber cables manufacturing India | 📈 BULL_ANY_MID | 58 | ↓96 | ↓1.017 | ↑2d | SQ | +3.8% | 28.69/25.53 | +0.24% | 20% |
| [SAPPHIRE](https://in.tradingview.com/chart/?symbol=NSE:SAPPHIRE)<br><sub>🚀SS · ↑CMF8d</sub> | ⚠ CAUTION | KFC Pizza Hut franchisee quick service restaurants India | ⚡ BULL_ANY_PPV | 89 | 🔄45 | ↑1.055 | ↑1d | SQ·PV | +8.6% | -18.39/-28.66 | +8.61% | 20% |
| [SIGNATURE](https://in.tradingview.com/chart/?symbol=NSE:SIGNATURE)<br><sub>W↑4d · 🚀SS · ↓CMF30d · DEL36%</sub> | ✓ SAFE | Residential real estate developer NCR affordable mid-segment housing | ⚡ BULL_ANY_PPV | 64 | ↓21 | ↑1.028 | ↑1d | SQ·PV | +3.6% | -24.12/-37.93 | +3.61% | 20% |
| [STUDDS](https://in.tradingview.com/chart/?symbol=NSE:STUDDS)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 64 | ↓50 | ↑1.029 | ↑1d | SQ·PV | +4.5% | -32.69/-41.72 | +4.49% | 20% |
| [AADHARHFC](https://in.tradingview.com/chart/?symbol=NSE:AADHARHFC)<br><sub>🚀SS · ↑CMF15d</sub> | ⚠ CAUTION | Low-income housing loans, retail, affordable home buyers | 📈 BULL_ANY_MID | 69 | ↓34 | ↑1.011 | ↑1d | SQ | +1.6% | -41.32/-49.28 | +1.63% | 20% |
| [BETA](https://in.tradingview.com/chart/?symbol=NSE:BETA)<br><sub>🚀SS · ↑CMF10d</sub> | ✓ SAFE | Oncology drug manufacturer for cancer treatment domestic export | 📈 BULL_ANY_MID | 69 | ↓58 | ↑1.011 | ↑1d | SQ | +4.0% | -28.52/-28.67 | +4.02% | 20% |
| [HEIDELBERG](https://in.tradingview.com/chart/?symbol=NSE:HEIDELBERG)<br><sub>🚀SS · ↑CMF1d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↓7 | ↑1.004 | ↑1d | SQ | +2.0% | -42.65/-47.49 | +2.00% | 20% |
| [NAUKRI](https://in.tradingview.com/chart/?symbol=NSE:NAUKRI)<br><sub>🚀SS · ↑CMF0d</sub> | ✓ SAFE | Online classifieds: recruitment, real estate, matrimony, education | 📈 BULL_ANY_MID | 64 | ↓58 | ↑1.018 | ↑1d | SQ | +4.0% | -42.21/-46.75 | +4.02% | 20% |
| [SUPRIYA](https://in.tradingview.com/chart/?symbol=NSE:SUPRIYA)<br><sub>🚀SS · ↓CMF11d · ⚠️TRAP</sub> | ✓ SAFE | API manufacturer, antihistamine analgesic anaesthetic pharma exports | 📈 BULL_ANY_MID | 63 | ↓74 | ↑1.018 | ↑2d | SQ | +4.4% | -20.92/-28.82 | +1.13% | 20% |
| [ICRA](https://in.tradingview.com/chart/?symbol=NSE:ICRA)<br><sub>W↑19d · 🚀SS · ↑CMF8d · ⚠️TRAP</sub> | ⚠ CAUTION | Credit ratings, debt analysis, capital markets participants | 📈 BULL_ANY_MID | 63 | ↓19 | ↑1.016 | ↑2d | SQ | +3.5% | -15.93/-25.83 | +1.27% | 20% |
| [HUHTAMAKI](https://in.tradingview.com/chart/?symbol=NSE:HUHTAMAKI)<br><sub>🚀SS · ↑CMF5d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE | Flexible packaging solutions for food beverage consumer goods | 📈 BULL_ANY_MID | 63 | ↓52 | ↑1.004 | ↓7d | SQ | +14.8% | -34.1/-36.75 | +1.50% | 20% |
| [HINDWAREAP](https://in.tradingview.com/chart/?symbol=NSE:HINDWAREAP)<br><sub>W↑4d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Bathroom fittings, sanitaryware, kitchen products for homes | 📈 BULL_ANY_MID | 63 | ↓5 | ↑1.022 | ↑2d | SQ | +4.1% | -20.33/-30.03 | +2.47% | 20% |
| [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN)<br><sub>↑CMF16d</sub> | ✓ SAFE | Precision auto parts manufacturing for powertrains and aluminum | 📈 BULL_ANY_MID | 62 | ↓83 | ↑1.003 | ↓8d | SQ | -0.3% | -12.15/-15.69 | +0.11% | 20% |
| [SCHAEFFLER](https://in.tradingview.com/chart/?symbol=NSE:SCHAEFFLER)<br><sub>🚀SS · ↓CMF1d</sub> | ⚠ CAUTION | Bearings and drivetrain components for automotive and industry | 📈 BULL_ANY_MID | 62 | ↓31 | ↑1.000 | ↓8d | SQ | +1.3% | -41.42/-44.9 | +1.55% | 20% |
| [CSBBANK](https://in.tradingview.com/chart/?symbol=NSE:CSBBANK)<br><sub>🚀SS · ↓CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Private bank SME retail NRI lending Kerala focus | 📈 BULL_ANY_MID | 62 | ↓22 | ↑1.002 | ↓8d | SQ | -1.3% | -39.42/-42.75 | +0.25% | 20% |
| [INNOVACAP](https://in.tradingview.com/chart/?symbol=NSE:INNOVACAP)<br><sub>↓CMF29d · ⚠️TRAP</sub> | ✓ SAFE | Pharma contract manufacturing research development marketing | 📈 BULL_ANY_MID | 59 | ↓80 | ↓1.009 | ↑1d | SQ | +0.1% | -20.43/-24.77 | +0.15% | 20% |
| [PARAS](https://in.tradingview.com/chart/?symbol=NSE:PARAS)<br><sub>↑CMF1d · ⚠️TRAP</sub> | ✓ SAFE | Defence electronics and space hardware manufacturing for military government | 📈 BULL_ANY_MID | 58 | ↓93 | ↓1.007 | ↑2d | SQ | +4.4% | -24.38/-28.63 | -0.08% | 20% 🟦 |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB)<br><sub>★ · ↓CMF4d</sub> | ✓ SAFE | Pharma company making tablets capsules injectables antibiotics | 📈 BULL_ANY_MID | 58 | ↓99 | ↓0.987 | ↓2d | SQ | +3.8% | -12.6/-13.8 | -3.72% | 20% |
| [VARROC](https://in.tradingview.com/chart/?symbol=NSE:VARROC)<br><sub>🚀SS · ↑CMF11d · ⚠️TRAP</sub> | ✓ SAFE | Automotive electrical components two-wheeler three-wheeler segments | 📈 BULL_ANY_MID | 58 | ↓78 | ↑0.999 | ↓7d | SQ | -2.0% | -37.31/-40.63 | +1.34% | 20% |
| [SOLARA](https://in.tradingview.com/chart/?symbol=NSE:SOLARA)<br><sub>↓CMF23d · ⚠️TRAP</sub> | ✓ SAFE | Active pharmaceutical ingredients manufacturing, CRAMS, global pharma supply | 📈 BULL_ANY_MID | 54 | ↓84 | ↓1.003 | ↓6d | SQ | -1.6% | -25.81/-29.39 | -0.25% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MBEL,NSE:RBA,NSE:DEVYANI,NSE:CANTABIL,NSE:BLUSPRING,NSE:BPCL,NSE:TATASTEEL,NSE:KARURVYSYA,NSE:5PAISA,NSE:SYSTMTXC,NSE:MEESHO,NSE:SHADOWFAX,NSE:GNA,NSE:BHAGERIA,NSE:PTCIL,NSE:WSTCSTPAPR,NSE:SAPPHIRE,NSE:SIGNATURE,NSE:STUDDS,NSE:AADHARHFC,NSE:BETA,NSE:HEIDELBERG,NSE:NAUKRI,NSE:SUPRIYA,NSE:ICRA,NSE:HUHTAMAKI,NSE:HINDWAREAP,NSE:CRAFTSMAN,NSE:SCHAEFFLER,NSE:CSBBANK,NSE:INNOVACAP,NSE:PARAS,NSE:INDSWFTLAB,NSE:VARROC,NSE:SOLARA
```

---

### 🔥 MAJOR — PPV confirmed (8)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PWL](https://in.tradingview.com/chart/?symbol=NSE:PWL)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Online test prep and upskilling courses for competitive exams | ⚡ BULL_ANY_PPV | 24 | ↓50 | ↑1.020 | ↑1d | PV | +3.8% | 2.21/-4.92 | +3.76% | 20% |
| [TEXINFRA](https://in.tradingview.com/chart/?symbol=NSE:TEXINFRA)<br><sub>📶W9 · 🚀SS · ↑CMF1d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 24 | ↓76 | ↑1.017 | ↑1d | PV | +2.0% | -14.69/-17.9 | +2.02% | 20% |
| [PARACABLES](https://in.tradingview.com/chart/?symbol=NSE:PARACABLES)<br><sub>📶W9 · W↑9d · ↑CMF14d</sub> | ✓ SAFE | Power telecom railway cables manufacturer | ⚡ BULL_ANY_PPV | 17 | ↑87 | ↑1.076 | ↑3d | PV | +12.2% | 27.56/18.35 | +5.88% | 20% 🟦 |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [KALPATARU](https://in.tradingview.com/chart/?symbol=NSE:KALPATARU)<br><sub>🚀SS·11x · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Luxury residential real estate developer focused Mumbai MMR | 🔥 BULL_OS_PPV | 29 | ↓11 | ↑1.015 | ↑1d | PV | +3.5% | -52.85/-60.67 | +3.54% | 20% |
| [ASIANHOTNR](https://in.tradingview.com/chart/?symbol=NSE:ASIANHOTNR)<br><sub>RVOL9x · ↓CMF28d</sub> | ⚠ CAUTION | Luxury hotel operations, Delhi, high-end accommodation | ⚡ BULL_ANY_PPV | 49 | 🔄64 | ↑1.056 | ↑1d | PV | +10.0% | -34.24/-43.51 | +10.02% | 20% |
| [WALCHANNAG](https://in.tradingview.com/chart/?symbol=NSE:WALCHANNAG)<br><sub>🚀SS · ↓CMF1d</sub> | ✓ SAFE | Heavy engineering, defense equipment, nuclear power projects | ⚡ BULL_ANY_PPV | 24 | ↓43 | ↑1.026 | ↑1d | PV | +5.1% | -37.22/-41.54 | +5.09% | 20% |
| [VMART](https://in.tradingview.com/chart/?symbol=NSE:VMART)<br><sub>🚀SS · ↓CMF3d</sub> | ⚠ CAUTION | Affordable apparel retail chain serving tier II III IV cities | ⚡ BULL_ANY_PPV | 24 | ↓65 | ↑1.022 | ↑1d | PV | +4.9% | -42.13/-46.52 | +4.86% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:PWL,NSE:TEXINFRA,NSE:PARACABLES,NSE:SIGMAADV,NSE:KALPATARU,NSE:ASIANHOTNR,NSE:WALCHANNAG,NSE:VMART
```

### 🟢 OVERSOLD — reversal from −53/−60 (23)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · ↑CMF2d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 29 | ↑57 | ↑1.012 | ↑1d | — | +1.2% | -51.83/-59.38 | +1.19% | 20% |
| [CIEINDIA](https://in.tradingview.com/chart/?symbol=NSE:CIEINDIA)<br><sub>🚀SS · ↓CMF4d · 🎯SLING</sub> | ⚠ CAUTION | Automotive parts supplier to OEMs globally | 🟢 BULL_OVERSOLD | 29 | ↓24 | ↑1.011 | ↑1d | — | +3.2% | -57.32/-63.23 | +3.25% | 20% |
| [IGL](https://in.tradingview.com/chart/?symbol=NSE:IGL)<br><sub>🚀SS · ↑CMF16d · 🔥PHX</sub> | ⚠ CAUTION | CNG piped gas distribution Delhi NCR sectors | 🟢 BULL_OVERSOLD | 24 | ↓24 | ↑1.015 | ↑1d | — | +2.9% | -58.37/-66.76 | +2.86% | 20% |
| [TI](https://in.tradingview.com/chart/?symbol=NSE:TI)<br><sub>🚀SS · ↑CMF2d · 🎯SLING</sub> | ✓ SAFE | Brandy and spirits manufacturer, dominant South Indian market position | 🟢 BULL_OVERSOLD | 10 | ↓57 | ↑0.997 | ↓15d | — | -11.1% | -58.98/-63.2 | +2.84% | 20% |
| [SARDAEN](https://in.tradingview.com/chart/?symbol=NSE:SARDAEN)<br><sub>🚀SS · ↓CMF21d · 🎯SLING</sub> | ⚠ CAUTION | Steel ferroalloys power producer Chhattisgarh integrated | 🟢 BULL_OVERSOLD | 10 | ↓27 | ↑1.003 | ↓46d | — | -8.6% | -63.49/-69.88 | +1.77% | 20% |
| [VAIBHAVGBL](https://in.tradingview.com/chart/?symbol=NSE:VAIBHAVGBL)<br><sub>🚀SS · ↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Fashion jewelry gemstones lifestyle direct consumer retail | 🟢 BULL_OVERSOLD | 10 | ↓4 | ↑0.953 | ↓15d | — | -20.1% | -65.17/-67.42 | +0.72% | 20% |
| [UGROCAP](https://in.tradingview.com/chart/?symbol=NSE:UGROCAP)<br><sub>🚀SS · ↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | MSME lending platform, technology-driven credit scoring | 🟢 BULL_OVERSOLD | 9 | ↓2 | ↑0.988 | ↓16d | — | -8.8% | -69.91/-73.62 | +1.16% | 20% |
| [EQUITASBNK](https://in.tradingview.com/chart/?symbol=NSE:EQUITASBNK)<br><sub>↑CMF4d · ⚠️TRAP</sub> | ✓ SAFE | Small finance bank serving underbanked individuals and SMEs | 🟢 BULL_OVERSOLD | 8 | ↓15 | ↑0.943 | ↓17d | — | -19.0% | -66.88/-69.3 | -1.19% | 20% |
| [SFL](https://in.tradingview.com/chart/?symbol=NSE:SFL)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Polyurethane foam and mattresses for Indian consumers | 🟢 BULL_OVERSOLD | 5 | ↓22 | ↑0.973 | ↓36d | — | -20.1% | -75.24/-75.58 | +4.32% | 20% |
| [VINATIORGA](https://in.tradingview.com/chart/?symbol=NSE:VINATIORGA)<br><sub>🚀SS · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Specialty chemicals, monomers, antioxidants, polymers manufacturer | 🟢 BULL_OVERSOLD | 5 | ↓5 | ↑0.987 | ↓43d | — | -22.3% | -71.55/-76.4 | +1.07% | 20% |
| [NOCIL](https://in.tradingview.com/chart/?symbol=NSE:NOCIL)<br><sub>↓CMF21d · ⚠️TRAP</sub> | ✓ SAFE | Rubber chemicals manufacturer for tire and industrial processing | 🟢 BULL_OVERSOLD | 5 | ↓22 | ↑0.963 | ↓52d | — | -16.3% | -59.85/-60.51 | +0.12% | 20% |
| [VISHNU](https://in.tradingview.com/chart/?symbol=NSE:VISHNU)<br><sub>🚀SS · ↓CMF27d · ⚠️TRAP</sub> | ✓ SAFE | Chromium barium specialty chemicals global industrial applications | 🟢 BULL_OVERSOLD | 5 | ↓53 | ↑0.978 | ↓23d | — | -16.6% | -63.76/-67.3 | +0.98% | 20% |
| [NIITMTS](https://in.tradingview.com/chart/?symbol=NSE:NIITMTS)<br><sub>↓CMF30d · 🔥PHX</sub> | ⚠ CAUTION | IT training services corporate upskilling global | 🟢 BULL_OVERSOLD | 5 | ↓2 | ↑0.959 | ↓40d | — | -24.6% | -75.68/-75.96 | +1.80% | 20% |
| [BHAGCHEM](https://in.tradingview.com/chart/?symbol=NSE:BHAGCHEM)<br><sub>🚀SS · ↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Agrochemical technicals insecticides fungicides herbicides manufacturer | 🟢 BULL_OVERSOLD | 5 | ↓9 | ↑0.991 | ↓53d | — | -30.4% | -58.83/-61.01 | +1.20% | 20% |
| [ATULAUTO](https://in.tradingview.com/chart/?symbol=NSE:ATULAUTO)<br><sub>🚀SS · ↑CMF3d · 🎯SLING</sub> | ✓ SAFE | Three-wheeler auto-rickshaw manufacturer for last-mile transport | 🟡 BULL_OS_L2 | 23 | ↓24 | ↑1.003 | ↓7d | — | -1.4% | -50.11/-54.21 | +2.66% | 20% |
| [WONDERLA](https://in.tradingview.com/chart/?symbol=NSE:WONDERLA)<br><sub>🚀SS · ↓CMF20d · 🎯SLING</sub> | ✓ SAFE | Theme parks and resorts for family entertainment and tourism | 🟡 BULL_OS_L2 | 20 | ↓46 | ↑0.999 | ↓5d | — | -2.2% | -52.5/-53.51 | +2.26% | 20% |
| [ZEEL](https://in.tradingview.com/chart/?symbol=NSE:ZEEL)<br><sub>↑CMF1d · ⚠️TRAP</sub> | ✓ SAFE | Television channels, digital content, movies, music production | 🟡 BULL_OS_L2 | 18 | ↓6 | ↓1.010 | ↑2d | — | +9.3% | -49.95/-57.12 | -0.66% | 20% |
| [BAJAJELEC](https://in.tradingview.com/chart/?symbol=NSE:BAJAJELEC)<br><sub>🚀SS · ↓CMF26d · ⚠️TRAP</sub> | ✓ SAFE | Electrical appliances fans lighting wiring for homes | 🟡 BULL_OS_L2 | 18 | ↓4 | ↑0.989 | ↓7d | — | -2.8% | -54.18/-56.63 | +0.88% | 20% |
| [SENORES](https://in.tradingview.com/chart/?symbol=NSE:SENORES)<br><sub>🚀SS · ↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Complex generics manufacturer specialty pharma therapies India | 🟡 BULL_OS_L2 | 17 | ↓74 | ↑0.996 | ↓8d | — | -4.6% | -56.24/-58.32 | +4.48% | 20% |
| [LINCOLN](https://in.tradingview.com/chart/?symbol=NSE:LINCOLN)<br><sub>🚀SS · ↓CMF5d · ⚠️TRAP</sub> | ✓ SAFE | Injectable antibiotics and cardiac drugs manufacturer | 🟡 BULL_OS_L2 | 17 | ↓37 | ↑0.989 | ↓8d | — | -3.2% | -52.36/-53.97 | +0.43% | 20% |
| [NSIL](https://in.tradingview.com/chart/?symbol=NSE:NSIL)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 15 | ↓26 | ↑0.991 | ↓10d | — | -4.0% | -54.96/-55.26 | +1.98% | 20% |
| [GLOBUSSPR](https://in.tradingview.com/chart/?symbol=NSE:GLOBUSSPR)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Grain distillery, spirits manufacturing, domestic alcohol market | 🟡 BULL_OS_L2 | 8 | ↓8 | ↑0.995 | ↓17d | — | -12.3% | -56.63/-58.19 | +4.58% | 20% |
| [VESUVIUS](https://in.tradingview.com/chart/?symbol=NSE:VESUVIUS)<br><sub>↓CMF0d · ⚠️TRAP</sub> | ⚠ CAUTION | Ceramic refractories for steel and foundry molten metal handling | 🟡 BULL_OS_L2 | 0 | ↓10 | ↓0.978 | ↓23d | — | -5.5% | -55.89/-58.19 | -0.61% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:PIDILITIND,NSE:CIEINDIA,NSE:IGL,NSE:TI,NSE:SARDAEN,NSE:VAIBHAVGBL,NSE:UGROCAP,NSE:EQUITASBNK,NSE:SFL,NSE:VINATIORGA,NSE:NOCIL,NSE:VISHNU,NSE:NIITMTS,NSE:BHAGCHEM,NSE:ATULAUTO,NSE:WONDERLA,NSE:ZEEL,NSE:BAJAJELEC,NSE:SENORES,NSE:LINCOLN,NSE:NSIL,NSE:GLOBUSSPR,NSE:VESUVIUS
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (43)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄54 | ↑1.014 | ↑1d | — | +4.5% | -47.75/-50.99 | +4.51% | 20% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>📶W9 · 🚀SS · ↑CMF20d</sub> | ✓ SAFE | Gold jewelry manufacturer selling to retail jewelers B2B | 📈 BULL_ANY_MID | 54 | 🔄98 | ↑1.030 | ↑1d | — | +2.4% | 7.5/5.72 | +2.36% | 20% |
| [BBOX](https://in.tradingview.com/chart/?symbol=NSE:BBOX)<br><sub>📶W9 · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Digital infrastructure integration, managed services, enterprise networks | 📈 BULL_ANY_MID | 49 | 🔄86 | ↑1.040 | ↑1d | — | +6.1% | -11.21/-15.32 | +6.09% | 20% 🟦 |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>📶W9 · 🚀SS · ↓CMF11d</sub> | ✓ SAFE | Bromine lithium specialty chemicals pharma agri-chem | 📈 BULL_ANY_MID | 49 | 🔄92 | ↑1.061 | ↑1d | — | +5.9% | -16.76/-26.67 | +5.91% | 20% |
| [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT)<br><sub>📶W9 · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | BPM services: customer care, technical support, back-office processing | 📈 BULL_ANY_MID | 49 | 🔄91 | ↑1.043 | ↑1d | — | +6.0% | -3.48/-7.15 | +5.96% | 20% |
| [KOPRAN](https://in.tradingview.com/chart/?symbol=NSE:KOPRAN)<br><sub>📶W9 · 🚀SS · ↑CMF2d</sub> | ✓ SAFE | APIs and formulations manufacturer serving global pharma | 📈 BULL_ANY_MID | 49 | 🔄95 | ↑1.046 | ↑1d | — | +6.1% | -27.07/-33.85 | +6.14% | 20% |
| [TATAELXSI](https://in.tradingview.com/chart/?symbol=NSE:TATAELXSI)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF17d</sub> | ✓ SAFE | Design engineering services for automotive media healthcare | 📈 BULL_ANY_MID | 31 | 🔄37 | ↑1.039 | ↑19d | — | +25.2% | 32.97/29.51 | +4.39% | 20% |
| [ZENSARTECH](https://in.tradingview.com/chart/?symbol=NSE:ZENSARTECH)<br><sub>📶W9 · W↑24d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE | Digital solutions and IT services for global enterprises | 📈 BULL_ANY_MID | 30 | 🔄61 | ↑1.068 | ↑25d | — | +30.2% | 61.48/59.84 | +6.14% | 20% |
| [ONGC](https://in.tradingview.com/chart/?symbol=NSE:ONGC)<br><sub>📶W9 · W↑6d · 🚀SS · ↑CMF4d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 22 | ↑45 | ↑1.026 | ↑3d | — | +3.7% | 12.73/0.87 | +3.45% | 20% |
| [SHRINGARMS](https://in.tradingview.com/chart/?symbol=NSE:SHRINGARMS)<br><sub>📶W9 · W↑24d · ↑CMF18d</sub> | ✓ SAFE | Mangalsutra manufacturer, 18k 22k gold, Indian women bridal wear | 📈 BULL_ANY_MID | 18 | ↑90 | ↑1.081 | ↑2d | — | +13.2% | 25.34/19.0 | +7.12% | 10% 🟨 |
| [TARIL](https://in.tradingview.com/chart/?symbol=NSE:TARIL)<br><sub>📶W9 · W↑19d · ↑CMF3d</sub> | ✓ SAFE | Power transformers, furnace transformers, electrical equipment manufacturing | 📈 BULL_ANY_MID | 18 | ↓63 | ↓1.014 | ↑2d | — | +4.7% | 10.38/5.3 | -0.61% | 20% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>📶W9 · W↑49d · ★ · ↑CMF23d</sub> | ✓ SAFE | Steel and alloy wheel rims manufacturer for automobiles | 📈 BULL_ANY_MID | 10 | ↑98 | ↓1.057 | ↑10d | — | +36.0% | 60.35/59.06 | -1.03% | 20% |
| [CCAVENUE](https://in.tradingview.com/chart/?symbol=NSE:CCAVENUE)<br><sub>📶W9 · W↑14d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 6 | ↑100 | ↑1.124 | ↑14d | — | +801.1% | 41.52/41.16 | +5.08% | 20% |
| [SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK)<br><sub>📶W9 · W↑34d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓88 | ↑1.028 | ↑20d | — | +21.4% | 55.64/55.0 | +0.84% | 20% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>🚀SS · ↑CMF21d</sub> | ✓ SAFE | Electronics manufacturing design testing mission-critical defense aerospace systems | 📈 BULL_ANY_MID | 49 | 🔄96 | ↑1.045 | ↑1d | — | +8.0% | -19.99/-23.6 | +7.97% | 20% |
| [RECLTD](https://in.tradingview.com/chart/?symbol=NSE:RECLTD)<br><sub>🚀SS · ↑CMF0d</sub> | ✓ SAFE | Power sector financing, generation to distribution infrastructure | 📈 BULL_ANY_MID | 29 | ↓21 | ↑1.014 | ↑1d | — | +3.0% | -43.86/-48.68 | +3.05% | 20% |
| [CUB](https://in.tradingview.com/chart/?symbol=NSE:CUB)<br><sub>🚀SS · ↓CMF6d</sub> | ✓ SAFE | Private bank serving SMEs, MSMEs, retail customers South India | 📈 BULL_ANY_MID | 29 | ↓36 | ↑1.010 | ↑1d | — | +2.4% | -36.15/-37.74 | +2.39% | 20% |
| [KNACK](https://in.tradingview.com/chart/?symbol=NSE:KNACK)<br><sub>🚀SS · ↑CMF21d</sub> | ✓ SAFE | Printed laminated PP bags for food pet food export | 📈 BULL_ANY_MID | 29 | ↓50 | ↑1.013 | ↑1d | — | +4.1% | -21.92/-22.58 | +4.09% | 20% |
| [RISHABH](https://in.tradingview.com/chart/?symbol=NSE:RISHABH)<br><sub>🚀SS · ↓CMF23d</sub> | ✓ SAFE | Electrical meters, automation instruments, industrial measurement solutions | 📈 BULL_ANY_MID | 29 | ↓86 | ↑1.014 | ↑1d | — | +1.8% | -46.02/-51.31 | +1.78% | 20% |
| [STARHEALTH](https://in.tradingview.com/chart/?symbol=NSE:STARHEALTH)<br><sub>🚀SS · ↓CMF3d</sub> | ⚠ CAUTION | Health insurance provider, retail customers, India | 📈 BULL_ANY_MID | 24 | ↓62 | ↑1.019 | ↑1d | — | +2.2% | -40.8/-49.93 | +2.23% | 20% |
| [DCBBANK](https://in.tradingview.com/chart/?symbol=NSE:DCBBANK)<br><sub>🚀SS · ↓CMF13d</sub> | ✓ SAFE | Secured lending to retail, MSME, agricultural sectors | 📈 BULL_ANY_MID | 24 | ↓68 | ↑1.020 | ↑1d | — | +4.8% | -43.78/-47.14 | +4.76% | 20% |
| [BAJAJHCARE](https://in.tradingview.com/chart/?symbol=NSE:BAJAJHCARE)<br><sub>🚀SS · ↑CMF10d</sub> | ✓ SAFE | API and pharmaceutical formulation manufacturer for global markets | 📈 BULL_ANY_MID | 24 | ↓40 | ↑1.020 | ↑1d | — | +3.7% | -29.0/-34.27 | +3.71% | 20% |
| [AURUM](https://in.tradingview.com/chart/?symbol=NSE:AURUM)<br><sub>🚀SS · ↓CMF17d</sub> | ✓ SAFE | Real estate software platform, rental and sales digitization | 📈 BULL_ANY_MID | 24 | ↓71 | ↑1.022 | ↑1d | — | +3.3% | -25.14/-28.92 | +3.30% | 20% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>🚀SS · ↓CMF2d · ⚠️TRAP</sub> | ✓ SAFE | Specialty chemicals for pharma, agro, materials | 📈 BULL_ANY_MID | 23 | ↓90 | ↑1.005 | ↓7d | — | +1.0% | -14.04/-15.49 | +0.75% | 20% |
| [VINDHYATEL](https://in.tradingview.com/chart/?symbol=NSE:VINDHYATEL)<br><sub>↓CMF2d · ⚠️TRAP</sub> | ✓ SAFE | Telecom railway solar cables FRP EPC projects India | 📈 BULL_ANY_MID | 18 | ↓94 | ↓0.987 | ↓2d | — | +2.2% | -16.07/-18.5 | -3.47% | 20% |
| [GOODLUCK](https://in.tradingview.com/chart/?symbol=NSE:GOODLUCK)<br><sub>↑CMF18d · ⚠️TRAP</sub> | ✓ SAFE | Steel pipes forgings structural products engineering export | 📈 BULL_ANY_MID | 18 | ↓0 | ↓1.003 | ↑2d | — | +3.7% | -15.63/-19.6 | -1.59% | 20% |
| [EPACK](https://in.tradingview.com/chart/?symbol=NSE:EPACK)<br><sub>W↑4d · 🚀SS · ↑CMF8d · ⚠️TRAP</sub> | ✓ SAFE | AC manufacturing ODM, consumer durables, Indian domestic market | 📈 BULL_ANY_MID | 18 | ↓3 | ↑0.992 | ↓7d | — | -4.4% | -45.35/-47.46 | +1.00% | 20% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>🚀SS · ↓CMF9d</sub> | ✓ SAFE | Heavy equipment manufacturing for oil gas power plants | 📈 BULL_ANY_MID | 15 | ↓82 | ↑1.005 | ↓15d | — | -6.9% | -42.1/-43.86 | +2.82% | 20% |
| [OMAXE](https://in.tradingview.com/chart/?symbol=NSE:OMAXE)<br><sub>🚀SS · ↓CMF26d · ⚠️TRAP</sub> | ✓ SAFE | Residential commercial real estate developer across Indian cities | 📈 BULL_ANY_MID | 15 | ↓81 | ↑1.000 | ↓15d | — | -7.7% | -41.29/-45.16 | +0.42% | 10% 🟨 |
| [PNCINFRA](https://in.tradingview.com/chart/?symbol=NSE:PNCINFRA)<br><sub>↓CMF16d · ⚠️TRAP</sub> | ✓ SAFE | Highway and water infrastructure construction contractor | 📈 BULL_ANY_MID | 14 | ↓1 | ↑0.986 | ↓11d | — | -7.0% | -48.99/-49.63 | +0.77% | 20% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>↓CMF2d · ⚠️TRAP</sub> | ✓ SAFE | Large-diameter pipes, steel products, infrastructure | 📈 BULL_ANY_MID | 13 | ↓98 | ↓0.988 | ↓7d | — | -3.6% | -43.52/-45.08 | -0.60% | 20% |
| [JUSTDIAL](https://in.tradingview.com/chart/?symbol=NSE:JUSTDIAL)<br><sub>🚀SS · ↓CMF13d</sub> | ✓ SAFE | Local search engine connecting buyers sellers India | 📈 BULL_ANY_MID | 12 | ↓61 | ↑1.002 | ↓18d | — | +4.2% | -9.35/-9.41 | +0.83% | 20% 🟦 |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>↓CMF5d</sub> | ✓ SAFE | Housing loans for retail homebuyers and property | 📈 BULL_ANY_MID | 10 | ↓69 | ↑1.006 | ↓22d | — | -0.2% | -34.54/-36.35 | +1.66% | 20% |
| [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX)<br><sub>🚀SS · ↓CMF2d</sub> | ✓ SAFE | Polyester yarn and chip manufacturer for textiles | 📈 BULL_ANY_MID | 10 | ↓95 | ↑1.006 | ↓40d | — | +23.8% | -39.79/-42.61 | +2.95% | 20% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>↑CMF25d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 8 | ↓29 | ↓0.991 | ↓12d | — | -4.4% | -34.34/-35.72 | -0.90% | 20% |
| [DCMSHRIRAM](https://in.tradingview.com/chart/?symbol=NSE:DCMSHRIRAM)<br><sub>🚀SS · ↓CMF22d · ⚠️TRAP</sub> | ✓ SAFE | Fertilizer, chemicals, cement producer for Indian agriculture | 📈 BULL_ANY_MID | 8 | ↓20 | ↑0.990 | ↓17d | — | -5.6% | -42.02/-43.68 | +0.47% | 20% |
| [KSCL](https://in.tradingview.com/chart/?symbol=NSE:KSCL)<br><sub>↑CMF6d · ⚠️TRAP</sub> | ✓ SAFE | Hybrid seeds for field crops vegetables agriculture | 📈 BULL_ANY_MID | 7 | ↓12 | ↑0.998 | ↓18d | — | -2.6% | -38.22/-41.54 | +0.62% | 20% |
| [SIRCA](https://in.tradingview.com/chart/?symbol=NSE:SIRCA)<br><sub>🚀SS · ↓CMF4d · ⚠️TRAP</sub> | ✓ SAFE | Premium wood coatings and decorative paints manufacturer | 📈 BULL_ANY_MID | 6 | ↓35 | ↑0.998 | ↓19d | — | +2.0% | -15.9/-16.5 | +0.48% | 20% |
| [AWL](https://in.tradingview.com/chart/?symbol=NSE:AWL)<br><sub>🚀SS · ↓CMF9d</sub> | ✓ SAFE | Edible oils wheat flour rice pulses sugar FMCG | 📈 BULL_ANY_MID | 5 | ↓15 | ↑0.996 | ↓23d | — | -4.7% | -47.05/-49.9 | +2.41% | 20% |
| [PAUSHAKLTD](https://in.tradingview.com/chart/?symbol=NSE:PAUSHAKLTD)<br><sub>🚀SS · ↓CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Phosgene derivatives for pharma agrochemical performance chemicals | 📈 BULL_ANY_MID | 5 | ↓50 | ↑0.993 | ↓20d | — | -7.7% | -27.94/-29.83 | +0.53% | 20% |
| [NIACL](https://in.tradingview.com/chart/?symbol=NSE:NIACL)<br><sub>↑CMF18d · ⚠️TRAP</sub> | ✓ SAFE | General insurance underwriting and claims across India | 📈 BULL_ANY_MID | 1 | ↓41 | ↓0.982 | ↓19d | — | -2.3% | -39.7/-40.81 | -1.19% | 20% |
| [DHAMPURSUG](https://in.tradingview.com/chart/?symbol=NSE:DHAMPURSUG)<br><sub>↓CMF4d · ⚠️TRAP</sub> | ✓ SAFE | Sugarcane processing: sugar, ethanol, chemicals, power generation | 📈 BULL_ANY_MID | 0 | ↓80 | ↓0.999 | ↓30d | — | +3.1% | -22.7/-24.78 | -0.47% | 20% |
| [RAMRAT](https://in.tradingview.com/chart/?symbol=NSE:RAMRAT)<br><sub>↓CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Enameled copper wires for electrical equipment manufacturing | 📈 BULL_ANY_MID | 0 | ↓91 | ↓0.984 | ↓36d | — | +0.1% | -36.22/-37.71 | -1.36% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:COALINDIA,NSE:SKYGOLD,NSE:BBOX,NSE:NEOGEN,NSE:ONEPOINT,NSE:KOPRAN,NSE:TATAELXSI,NSE:ZENSARTECH,NSE:ONGC,NSE:SHRINGARMS,NSE:TARIL,NSE:SSWL,NSE:CCAVENUE,NSE:SOUTHBANK,NSE:CYIENTDLM,NSE:RECLTD,NSE:CUB,NSE:KNACK,NSE:RISHABH,NSE:STARHEALTH,NSE:DCBBANK,NSE:BAJAJHCARE,NSE:AURUM,NSE:AETHER,NSE:VINDHYATEL,NSE:GOODLUCK,NSE:EPACK,NSE:LLOYDSENGG,NSE:OMAXE,NSE:PNCINFRA,NSE:WELCORP,NSE:JUSTDIAL,NSE:PNBHOUSING,NSE:FILATEX,NSE:HDFCLIFE,NSE:DCMSHRIRAM,NSE:KSCL,NSE:SIRCA,NSE:AWL,NSE:PAUSHAKLTD,NSE:NIACL,NSE:DHAMPURSUG,NSE:RAMRAT
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
