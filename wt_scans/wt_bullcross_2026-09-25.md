> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-09-25
*Generated 2026-09-25 15:45 IST*

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

**Total bull crosses today: 70** · 30 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:BALRAMCHIN,NSE:INTERARCH,NSE:GEOJITFSL,NSE:TNPETRO,NSE:ARTEMISMED,NSE:SHOPERSTOP,NSE:ANDHRSUGAR,NSE:JSWDULUX,NSE:MANINFRA,NSE:SDBL,NSE:AVADHSUGAR,NSE:HDFCLIFE,NSE:SBILIFE,NSE:EMIL,NSE:ANTELOPUS,NSE:SBC,NSE:BHAGERIA,NSE:SIGMAADV,NSE:CIPLA,NSE:STARHEALTH,NSE:ELPROINTL,NSE:PUNJABCHEM,NSE:CUPID,NSE:TATASTEEL,NSE:INDHOTEL,NSE:KCP,NSE:KAYNES,NSE:MEESHO,NSE:PNB,NSE:SKFINDIA,NSE:BLUESTARCO,NSE:CYIENT,NSE:PETRONET,NSE:MMFL,NSE:AGARWALEYE,NSE:IDBI,NSE:NAVINFLUOR,NSE:TNPL,NSE:FCL,NSE:GENESYS,NSE:MVGJL,NSE:MAHLIFE,NSE:GODREJIND,NSE:WAAREEENER,NSE:AVANTIFEED,NSE:GRMOVER,NSE:MARUTI,NSE:ASIANPAINT,NSE:BAYERCROP,NSE:NACLIND,NSE:GRINFRA,NSE:DBCORP,NSE:GRWRHITECH,NSE:VOLTAS,NSE:ADANIENSOL,NSE:IOC,NSE:NESTLEIND,NSE:GUJENERGY,NSE:M&M,NSE:TRENT,NSE:BRITANNIA,NSE:TTKPRESTIG,NSE:TECHNVISN,NSE:IGARASHI,NSE:PASHUPATI,NSE:RECLTD,NSE:LAXMIDENTL,NSE:RESPONIND,NSE:BPCL,NSE:INGERRAND
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (41)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>📶W9 · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | Sugar production, ethanol distillery, power cogeneration for domestic industrial use | ⚡ BULL_ANY_PPV | 99 | 🔄83 | ↑1.015 | ↑1d | SQ·PV | +4.0% | -12.75/-13.75 | +4.00% | 20% |
| [INTERARCH](https://in.tradingview.com/chart/?symbol=NSE:INTERARCH)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Pre-engineered steel buildings manufacturing industrial commercial structures | ⚡ BULL_ANY_PPV | 99 | 🔄20 | ↑1.010 | ↑1d | SQ·PV | +2.5% | -15.86/-16.05 | +2.45% | 20% |
| [GEOJITFSL](https://in.tradingview.com/chart/?symbol=NSE:GEOJITFSL)<br><sub>📶W9 · ↓CMF16d</sub> | ⚠ CAUTION | Stock broking and portfolio management for retail investors | ⚡ BULL_ANY_PPV | 99 | 🔄62 | ↑1.011 | ↑1d | SQ·PV | +3.0% | 3.25/2.86 | +2.96% | 20% |
| [TNPETRO](https://in.tradingview.com/chart/?symbol=NSE:TNPETRO)<br><sub>📶W9 · W↑123d · ↑CMF18d</sub> | ✓ SAFE | Petrochemical intermediates and detergent raw materials manufacturer | ⚡ BULL_ANY_PPV | 94 | 🔄83 | ↑1.029 | ↑1d | SQ·PV | +4.7% | 23.78/21.24 | +4.69% | 20% |
| [ARTEMISMED](https://in.tradingview.com/chart/?symbol=NSE:ARTEMISMED)<br><sub>📶W9 · W↑60d · 🚀SS·50x · ↓CMF0d</sub> | ✓ SAFE | Tertiary care hospital operator, multi-specialty healthcare delivery Gurgaon | ⚡ BULL_ANY_PPV | 89 | 🔄86 | ↑1.050 | ↑1d | SQ·PV | +7.5% | 44.0/37.56 | +7.51% | 20% |
| [SHOPERSTOP](https://in.tradingview.com/chart/?symbol=NSE:SHOPERSTOP)<br><sub>📶W9 · W↑5d · RVOL17x · ↑CMF0d</sub> | ✓ SAFE | Department store operator, fashion beauty retail, urban consumers | ⚡ BULL_ANY_PPV | 89 | 🔄61 | ↑1.067 | ↑1d | SQ·PV | +10.0% | 8.16/2.6 | +10.00% | 20% |
| [ANDHRSUGAR](https://in.tradingview.com/chart/?symbol=NSE:ANDHRSUGAR)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Sugar, industrial chemicals, fertilizers manufacturing and alcohol | ⚡ BULL_ANY_PPV | 82 | 🔄74 | ↑1.004 | ↓18d | SQ·PV | -1.1% | -28.57/-28.69 | +2.61% | 20% |
| [JSWDULUX](https://in.tradingview.com/chart/?symbol=NSE:JSWDULUX)<br><sub>📶W9 · W↑35d · ↓CMF3d</sub> | ⚠ CAUTION | Paints coatings manufacturer automotive industrial decorative | ⚡ BULL_ANY_PPV | 69 | ↑45 | ↑1.014 | ↑1d | SQ·PV | +2.1% | 21.18/17.37 | +2.15% | 20% |
| [MANINFRA](https://in.tradingview.com/chart/?symbol=NSE:MANINFRA)<br><sub>📶W9 · W↑40d · ↑CMF26d</sub> | ✓ SAFE | EPC contractor, ports, residential, commercial real estate development | ⚡ BULL_ANY_PPV | 59 | ↑68 | ↑1.035 | ↑1d | SQ·PV | +4.7% | 27.64/23.24 | +4.65% | 20% |
| [SDBL](https://in.tradingview.com/chart/?symbol=NSE:SDBL)<br><sub>📶W9 · 🚀SS·51x · ↑CMF0d</sub> | ✓ SAFE | Beer and spirits manufacturer for Indian consumer market | ⚡ BULL_ANY_PPV | 49 | 🔄28 | ↑1.069 | ↑1d | PV | +10.6% | -32.49/-45.16 | +10.59% | 20% |
| [AVADHSUGAR](https://in.tradingview.com/chart/?symbol=NSE:AVADHSUGAR)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Sugar cane processing, ethanol, power generation | ⚡ BULL_ANY_PPV | 49 | 🔄95 | ↑1.058 | ↑1d | PV | +10.0% | -15.96/-19.83 | +10.00% | 5% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>📶W9 · W↑3d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 19 | ↑14 | ↑1.042 | ↑1d | PV | +5.0% | -31.89/-43.91 | +5.05% | 20% |
| [SBILIFE](https://in.tradingview.com/chart/?symbol=NSE:SBILIFE)<br><sub>📶W9 · ↓CMF16d · 🎯SLING</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 19 | ↑36 | ↑1.031 | ↑1d | PV | +4.2% | -50.09/-59.33 | +4.19% | 20% |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL)<br><sub>📶W9 · W↑5d · 🚀SS · ↑CMF11d</sub> | ✓ SAFE | Consumer electronics retail chain South India operations | ⚡ BULL_ANY_PPV | 13 | ↑94 | ↑1.049 | ↑7d | PV | +10.7% | 43.75/39.75 | +5.85% | 20% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>📶W9 · W↑20d · ↑CMF17d · ÷DIV</sub> | ✓ SAFE | Oil and gas exploration production Indian subcontinent hydrocarbon resources | ⚡ BULL_ANY_PPV | 2 | ↑98 | ↑1.109 | ↑18d | PV | +59.2% | 47.89/43.77 | +11.56% | 5% 🟥 |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>📶W9 · W↑20d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 0 | ↑94 | ↑1.081 | ↑22d | PV | +32.1% | 55.4/52.91 | +10.44% | 20% |
| [BHAGERIA](https://in.tradingview.com/chart/?symbol=NSE:BHAGERIA)<br><sub>📶W9 · W↑24d · 🚀SS · ★ · ↑CMF23d</sub> | ✓ SAFE | Dye intermediates, specialty dyes, chemicals manufacturer | ⚡ BULL_ANY_PPV | 0 | ↑98 | ↑1.144 | ↑25d | PV | +90.9% | 67.73/65.66 | +9.72% | 5% 🟥 |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [CIPLA](https://in.tradingview.com/chart/?symbol=NSE:CIPLA)<br><sub>📶W9 · 🚀SS · ↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 10 | ↑41 | ↑1.005 | ↓37d | — | -1.7% | -61.96/-65.24 | +1.99% | 20% |
| [STARHEALTH](https://in.tradingview.com/chart/?symbol=NSE:STARHEALTH)<br><sub>📶W9 · ↑CMF1d · 🎯SLING</sub> | ✓ SAFE | Health insurance provider, retail customers, India | 🟡 BULL_OS_L2 | 69 | ↑60 | ↑1.009 | ↑1d | SQ | +1.4% | -46.78/-54.17 | +1.41% | 20% |
| [ELPROINTL](https://in.tradingview.com/chart/?symbol=NSE:ELPROINTL)<br><sub>📶W9 · ↓CMF14d · ⚠️TRAP</sub> | ⚠ CAUTION | Surge arresters manufacturing, real estate development, renewable energy | 🟡 BULL_OS_L2 | 48 | ↑50 | ↓0.996 | ↓12d | SQ | -1.3% | -54.24/-54.87 | -0.12% | 10% 🟨 |
| [PUNJABCHEM](https://in.tradingview.com/chart/?symbol=NSE:PUNJABCHEM)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Agrochemicals pesticides fertilizers crop protection chemicals manufacturing | 📈 BULL_ANY_MID | 99 | 🔄42 | ↑1.007 | ↑1d | SQ | +2.2% | -43.18/-45.37 | +2.23% | 20% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>📶W9 · 🚀SS · ↑CMF2d</sub> | ✓ SAFE | Condoms lubricants IVD kits sexual wellness global | 📈 BULL_ANY_MID | 91 | 🔄99 | ↑1.000 | ↓9d | SQ | -3.6% | -24.06/-26.78 | +1.39% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>📶W9 · ↑CMF27d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 69 | ↑46 | ↑1.011 | ↑1d | SQ | +2.3% | -10.62/-12.03 | +2.27% | 20% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>📶W9 · ↑CMF24d</sub> | ⚠ CAUTION | Luxury and midscale hotel brands across Asia Pacific | 📈 BULL_ANY_MID | 69 | ↑47 | ↑1.008 | ↑1d | SQ | +1.6% | -22.75/-27.38 | +1.64% | 20% |
| [KCP](https://in.tradingview.com/chart/?symbol=NSE:KCP)<br><sub>📶W9 · ↓CMF4d</sub> | ⚠ CAUTION | Cement sugar heavy engineering power hospitality conglomerate | 📈 BULL_ANY_MID | 64 | ↑40 | ↑1.019 | ↑1d | SQ | +2.6% | -31.14/-36.44 | +2.58% | 20% |
| [KAYNES](https://in.tradingview.com/chart/?symbol=NSE:KAYNES)<br><sub>📶W9 · 🚀SS · ↓CMF20d</sub> | ✓ SAFE | Electronics manufacturing, IoT solutions, industrial and consumer products | 📈 BULL_ANY_MID | 59 | ↑36 | ↑1.032 | ↑1d | SQ | +4.0% | -14.83/-21.5 | +4.00% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · W↑30d · ↑CMF30d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.025 | ↑2d | SQ | +6.1% | 49.69/48.04 | -0.06% | 20% 🟦 |
| [PNB](https://in.tradingview.com/chart/?symbol=NSE:PNB)<br><sub>📶W9 · W↑72d · ↓CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | ↑52 | ↓1.004 | ↑2d | SQ | +1.8% | 22.16/15.43 | -0.05% | 20% |
| [SKFINDIA](https://in.tradingview.com/chart/?symbol=NSE:SKFINDIA)<br><sub>📶W9 · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Rolling bearings, seals, lubrication for industrial automotive machinery | 📈 BULL_ANY_MID | 58 | ↑24 | ↓1.004 | ↑2d | SQ | +1.3% | -18.96/-24.31 | -0.14% | 20% |
| [BLUESTARCO](https://in.tradingview.com/chart/?symbol=NSE:BLUESTARCO)<br><sub>📶W9 · W↑10d · ↑CMF11d</sub> | ✓ SAFE | AC units, refrigeration, MEP projects for commercial facilities | 📈 BULL_ANY_MID | 57 | ↑30 | ↑1.021 | ↑8d | SQ | +5.5% | 23.7/21.42 | +2.62% | 20% |
| [CYIENT](https://in.tradingview.com/chart/?symbol=NSE:CYIENT)<br><sub>📶W9 · W↑40d · ↑CMF26d</sub> | ✓ SAFE | Engineering services, product design, manufacturing sector solutions | 📈 BULL_ANY_MID | 54 | 🔄67 | ↑1.020 | ↑1d | — | +3.5% | 17.69/15.56 | +3.49% | 20% |
| [PETRONET](https://in.tradingview.com/chart/?symbol=NSE:PETRONET)<br><sub>📶W9 · ↑CMF2d</sub> | ⚠ CAUTION | LNG import regasification terminals serving Indian gas utilities | 📈 BULL_ANY_MID | 54 | ↑52 | ↓1.001 | ↓6d | SQ | +1.1% | -16.89/-17.51 | -0.03% | 20% |
| [MMFL](https://in.tradingview.com/chart/?symbol=NSE:MMFL)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE | Steel forging components for vehicles and machinery | 📈 BULL_ANY_MID | 53 | ↑91 | ↑1.000 | ↓12d | SQ | -0.1% | -19.7/-20.25 | +0.55% | 20% |
| [AGARWALEYE](https://in.tradingview.com/chart/?symbol=NSE:AGARWALEYE)<br><sub>📶W9 · ↑CMF30d</sub> | ⚠ CAUTION | Eye care surgery and diagnostics across India Africa | 📈 BULL_ANY_MID | 40 | ↑55 | ↓0.999 | ↓21d | SQ | +0.7% | -26.64/-28.84 | -0.42% | 20% |
| [IDBI](https://in.tradingview.com/chart/?symbol=NSE:IDBI)<br><sub>📶W9 · ↓CMF13d</sub> | ⚠ CAUTION | Retail corporate MSME lending deposit bank | 📈 BULL_ANY_MID | 29 | ↑48 | ↑1.010 | ↑1d | — | +2.2% | -20.63/-22.75 | +2.18% | 20% 🟦 |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>📶W9 · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | Specialty fluorochemicals refrigerants organic synthesis pharmaceutical | 📈 BULL_ANY_MID | 29 | ↑84 | ↑1.012 | ↑1d | — | +1.5% | 12.07/8.76 | +1.46% | 20% |
| [TNPL](https://in.tradingview.com/chart/?symbol=NSE:TNPL)<br><sub>📶W9 · W↑15d · ↓CMF6d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 23 | ↑52 | ↑1.020 | ↑2d | — | +5.0% | -10.09/-14.16 | +1.79% | 20% |
| [FCL](https://in.tradingview.com/chart/?symbol=NSE:FCL)<br><sub>📶W9 · W↑35d · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 14 | ↑98 | ↑1.068 | ↑6d | — | +14.1% | 48.53/46.33 | +7.87% | 10% 🟨 |
| [GENESYS](https://in.tradingview.com/chart/?symbol=NSE:GENESYS)<br><sub>📶W9 · W↑15d · 🚀SS · ↑CMF23d</sub> | ✓ SAFE | 3D geospatial data maps digital twins urban infrastructure | 📈 BULL_ANY_MID | 5 | ↑16 | ↑1.018 | ↑24d | — | +60.3% | 32.6/32.51 | +1.06% | 10% 🟨 |
| [MVGJL](https://in.tradingview.com/chart/?symbol=NSE:MVGJL)<br><sub>📶W9 · W↑20d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 1 | ↑84 | ↑1.056 | ↑19d | — | +48.6% | 52.44/52.03 | +4.46% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:BALRAMCHIN,NSE:INTERARCH,NSE:GEOJITFSL,NSE:TNPETRO,NSE:ARTEMISMED,NSE:SHOPERSTOP,NSE:ANDHRSUGAR,NSE:JSWDULUX,NSE:MANINFRA,NSE:SDBL,NSE:AVADHSUGAR,NSE:HDFCLIFE,NSE:SBILIFE,NSE:EMIL,NSE:ANTELOPUS,NSE:SBC,NSE:BHAGERIA,NSE:SIGMAADV,NSE:CIPLA,NSE:STARHEALTH,NSE:ELPROINTL,NSE:PUNJABCHEM,NSE:CUPID,NSE:TATASTEEL,NSE:INDHOTEL,NSE:KCP,NSE:KAYNES,NSE:MEESHO,NSE:PNB,NSE:SKFINDIA,NSE:BLUESTARCO,NSE:CYIENT,NSE:PETRONET,NSE:MMFL,NSE:AGARWALEYE,NSE:IDBI,NSE:NAVINFLUOR,NSE:TNPL,NSE:FCL,NSE:GENESYS,NSE:MVGJL
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (55)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>📶W9 · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | Sugar production, ethanol distillery, power cogeneration for domestic industrial use | ⚡ BULL_ANY_PPV | 99 | 🔄83 | ↑1.015 | ↑1d | SQ·PV | +4.0% | -12.75/-13.75 | +4.00% | 20% |
| [INTERARCH](https://in.tradingview.com/chart/?symbol=NSE:INTERARCH)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Pre-engineered steel buildings manufacturing industrial commercial structures | ⚡ BULL_ANY_PPV | 99 | 🔄20 | ↑1.010 | ↑1d | SQ·PV | +2.5% | -15.86/-16.05 | +2.45% | 20% |
| [GEOJITFSL](https://in.tradingview.com/chart/?symbol=NSE:GEOJITFSL)<br><sub>📶W9 · ↓CMF16d</sub> | ⚠ CAUTION | Stock broking and portfolio management for retail investors | ⚡ BULL_ANY_PPV | 99 | 🔄62 | ↑1.011 | ↑1d | SQ·PV | +3.0% | 3.25/2.86 | +2.96% | 20% |
| [TNPETRO](https://in.tradingview.com/chart/?symbol=NSE:TNPETRO)<br><sub>📶W9 · W↑123d · ↑CMF18d</sub> | ✓ SAFE | Petrochemical intermediates and detergent raw materials manufacturer | ⚡ BULL_ANY_PPV | 94 | 🔄83 | ↑1.029 | ↑1d | SQ·PV | +4.7% | 23.78/21.24 | +4.69% | 20% |
| [ARTEMISMED](https://in.tradingview.com/chart/?symbol=NSE:ARTEMISMED)<br><sub>📶W9 · W↑60d · 🚀SS·50x · ↓CMF0d</sub> | ✓ SAFE | Tertiary care hospital operator, multi-specialty healthcare delivery Gurgaon | ⚡ BULL_ANY_PPV | 89 | 🔄86 | ↑1.050 | ↑1d | SQ·PV | +7.5% | 44.0/37.56 | +7.51% | 20% |
| [SHOPERSTOP](https://in.tradingview.com/chart/?symbol=NSE:SHOPERSTOP)<br><sub>📶W9 · W↑5d · RVOL17x · ↑CMF0d</sub> | ✓ SAFE | Department store operator, fashion beauty retail, urban consumers | ⚡ BULL_ANY_PPV | 89 | 🔄61 | ↑1.067 | ↑1d | SQ·PV | +10.0% | 8.16/2.6 | +10.00% | 20% |
| [ANDHRSUGAR](https://in.tradingview.com/chart/?symbol=NSE:ANDHRSUGAR)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Sugar, industrial chemicals, fertilizers manufacturing and alcohol | ⚡ BULL_ANY_PPV | 82 | 🔄74 | ↑1.004 | ↓18d | SQ·PV | -1.1% | -28.57/-28.69 | +2.61% | 20% |
| [JSWDULUX](https://in.tradingview.com/chart/?symbol=NSE:JSWDULUX)<br><sub>📶W9 · W↑35d · ↓CMF3d</sub> | ⚠ CAUTION | Paints coatings manufacturer automotive industrial decorative | ⚡ BULL_ANY_PPV | 69 | ↑45 | ↑1.014 | ↑1d | SQ·PV | +2.1% | 21.18/17.37 | +2.15% | 20% |
| [MANINFRA](https://in.tradingview.com/chart/?symbol=NSE:MANINFRA)<br><sub>📶W9 · W↑40d · ↑CMF26d</sub> | ✓ SAFE | EPC contractor, ports, residential, commercial real estate development | ⚡ BULL_ANY_PPV | 59 | ↑68 | ↑1.035 | ↑1d | SQ·PV | +4.7% | 27.64/23.24 | +4.65% | 20% |
| [SDBL](https://in.tradingview.com/chart/?symbol=NSE:SDBL)<br><sub>📶W9 · 🚀SS·51x · ↑CMF0d</sub> | ✓ SAFE | Beer and spirits manufacturer for Indian consumer market | ⚡ BULL_ANY_PPV | 49 | 🔄28 | ↑1.069 | ↑1d | PV | +10.6% | -32.49/-45.16 | +10.59% | 20% |
| [AVADHSUGAR](https://in.tradingview.com/chart/?symbol=NSE:AVADHSUGAR)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Sugar cane processing, ethanol, power generation | ⚡ BULL_ANY_PPV | 49 | 🔄95 | ↑1.058 | ↑1d | PV | +10.0% | -15.96/-19.83 | +10.00% | 5% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>📶W9 · W↑3d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 19 | ↑14 | ↑1.042 | ↑1d | PV | +5.0% | -31.89/-43.91 | +5.05% | 20% |
| [SBILIFE](https://in.tradingview.com/chart/?symbol=NSE:SBILIFE)<br><sub>📶W9 · ↓CMF16d · 🎯SLING</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 19 | ↑36 | ↑1.031 | ↑1d | PV | +4.2% | -50.09/-59.33 | +4.19% | 20% |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL)<br><sub>📶W9 · W↑5d · 🚀SS · ↑CMF11d</sub> | ✓ SAFE | Consumer electronics retail chain South India operations | ⚡ BULL_ANY_PPV | 13 | ↑94 | ↑1.049 | ↑7d | PV | +10.7% | 43.75/39.75 | +5.85% | 20% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>📶W9 · W↑20d · ↑CMF17d · ÷DIV</sub> | ✓ SAFE | Oil and gas exploration production Indian subcontinent hydrocarbon resources | ⚡ BULL_ANY_PPV | 2 | ↑98 | ↑1.109 | ↑18d | PV | +59.2% | 47.89/43.77 | +11.56% | 5% 🟥 |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>📶W9 · W↑20d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 0 | ↑94 | ↑1.081 | ↑22d | PV | +32.1% | 55.4/52.91 | +10.44% | 20% |
| [BHAGERIA](https://in.tradingview.com/chart/?symbol=NSE:BHAGERIA)<br><sub>📶W9 · W↑24d · 🚀SS · ★ · ↑CMF23d</sub> | ✓ SAFE | Dye intermediates, specialty dyes, chemicals manufacturer | ⚡ BULL_ANY_PPV | 0 | ↑98 | ↑1.144 | ↑25d | PV | +90.9% | 67.73/65.66 | +9.72% | 5% 🟥 |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [CIPLA](https://in.tradingview.com/chart/?symbol=NSE:CIPLA)<br><sub>📶W9 · 🚀SS · ↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 10 | ↑41 | ↑1.005 | ↓37d | — | -1.7% | -61.96/-65.24 | +1.99% | 20% |
| [STARHEALTH](https://in.tradingview.com/chart/?symbol=NSE:STARHEALTH)<br><sub>📶W9 · ↑CMF1d · 🎯SLING</sub> | ✓ SAFE | Health insurance provider, retail customers, India | 🟡 BULL_OS_L2 | 69 | ↑60 | ↑1.009 | ↑1d | SQ | +1.4% | -46.78/-54.17 | +1.41% | 20% |
| [ELPROINTL](https://in.tradingview.com/chart/?symbol=NSE:ELPROINTL)<br><sub>📶W9 · ↓CMF14d · ⚠️TRAP</sub> | ⚠ CAUTION | Surge arresters manufacturing, real estate development, renewable energy | 🟡 BULL_OS_L2 | 48 | ↑50 | ↓0.996 | ↓12d | SQ | -1.3% | -54.24/-54.87 | -0.12% | 10% 🟨 |
| [PUNJABCHEM](https://in.tradingview.com/chart/?symbol=NSE:PUNJABCHEM)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Agrochemicals pesticides fertilizers crop protection chemicals manufacturing | 📈 BULL_ANY_MID | 99 | 🔄42 | ↑1.007 | ↑1d | SQ | +2.2% | -43.18/-45.37 | +2.23% | 20% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>📶W9 · 🚀SS · ↑CMF2d</sub> | ✓ SAFE | Condoms lubricants IVD kits sexual wellness global | 📈 BULL_ANY_MID | 91 | 🔄99 | ↑1.000 | ↓9d | SQ | -3.6% | -24.06/-26.78 | +1.39% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>📶W9 · ↑CMF27d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 69 | ↑46 | ↑1.011 | ↑1d | SQ | +2.3% | -10.62/-12.03 | +2.27% | 20% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>📶W9 · ↑CMF24d</sub> | ⚠ CAUTION | Luxury and midscale hotel brands across Asia Pacific | 📈 BULL_ANY_MID | 69 | ↑47 | ↑1.008 | ↑1d | SQ | +1.6% | -22.75/-27.38 | +1.64% | 20% |
| [KCP](https://in.tradingview.com/chart/?symbol=NSE:KCP)<br><sub>📶W9 · ↓CMF4d</sub> | ⚠ CAUTION | Cement sugar heavy engineering power hospitality conglomerate | 📈 BULL_ANY_MID | 64 | ↑40 | ↑1.019 | ↑1d | SQ | +2.6% | -31.14/-36.44 | +2.58% | 20% |
| [KAYNES](https://in.tradingview.com/chart/?symbol=NSE:KAYNES)<br><sub>📶W9 · 🚀SS · ↓CMF20d</sub> | ✓ SAFE | Electronics manufacturing, IoT solutions, industrial and consumer products | 📈 BULL_ANY_MID | 59 | ↑36 | ↑1.032 | ↑1d | SQ | +4.0% | -14.83/-21.5 | +4.00% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · W↑30d · ↑CMF30d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.025 | ↑2d | SQ | +6.1% | 49.69/48.04 | -0.06% | 20% 🟦 |
| [PNB](https://in.tradingview.com/chart/?symbol=NSE:PNB)<br><sub>📶W9 · W↑72d · ↓CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | ↑52 | ↓1.004 | ↑2d | SQ | +1.8% | 22.16/15.43 | -0.05% | 20% |
| [SKFINDIA](https://in.tradingview.com/chart/?symbol=NSE:SKFINDIA)<br><sub>📶W9 · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Rolling bearings, seals, lubrication for industrial automotive machinery | 📈 BULL_ANY_MID | 58 | ↑24 | ↓1.004 | ↑2d | SQ | +1.3% | -18.96/-24.31 | -0.14% | 20% |
| [BLUESTARCO](https://in.tradingview.com/chart/?symbol=NSE:BLUESTARCO)<br><sub>📶W9 · W↑10d · ↑CMF11d</sub> | ✓ SAFE | AC units, refrigeration, MEP projects for commercial facilities | 📈 BULL_ANY_MID | 57 | ↑30 | ↑1.021 | ↑8d | SQ | +5.5% | 23.7/21.42 | +2.62% | 20% |
| [CYIENT](https://in.tradingview.com/chart/?symbol=NSE:CYIENT)<br><sub>📶W9 · W↑40d · ↑CMF26d</sub> | ✓ SAFE | Engineering services, product design, manufacturing sector solutions | 📈 BULL_ANY_MID | 54 | 🔄67 | ↑1.020 | ↑1d | — | +3.5% | 17.69/15.56 | +3.49% | 20% |
| [PETRONET](https://in.tradingview.com/chart/?symbol=NSE:PETRONET)<br><sub>📶W9 · ↑CMF2d</sub> | ⚠ CAUTION | LNG import regasification terminals serving Indian gas utilities | 📈 BULL_ANY_MID | 54 | ↑52 | ↓1.001 | ↓6d | SQ | +1.1% | -16.89/-17.51 | -0.03% | 20% |
| [MMFL](https://in.tradingview.com/chart/?symbol=NSE:MMFL)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE | Steel forging components for vehicles and machinery | 📈 BULL_ANY_MID | 53 | ↑91 | ↑1.000 | ↓12d | SQ | -0.1% | -19.7/-20.25 | +0.55% | 20% |
| [AGARWALEYE](https://in.tradingview.com/chart/?symbol=NSE:AGARWALEYE)<br><sub>📶W9 · ↑CMF30d</sub> | ⚠ CAUTION | Eye care surgery and diagnostics across India Africa | 📈 BULL_ANY_MID | 40 | ↑55 | ↓0.999 | ↓21d | SQ | +0.7% | -26.64/-28.84 | -0.42% | 20% |
| [IDBI](https://in.tradingview.com/chart/?symbol=NSE:IDBI)<br><sub>📶W9 · ↓CMF13d</sub> | ⚠ CAUTION | Retail corporate MSME lending deposit bank | 📈 BULL_ANY_MID | 29 | ↑48 | ↑1.010 | ↑1d | — | +2.2% | -20.63/-22.75 | +2.18% | 20% 🟦 |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>📶W9 · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | Specialty fluorochemicals refrigerants organic synthesis pharmaceutical | 📈 BULL_ANY_MID | 29 | ↑84 | ↑1.012 | ↑1d | — | +1.5% | 12.07/8.76 | +1.46% | 20% |
| [TNPL](https://in.tradingview.com/chart/?symbol=NSE:TNPL)<br><sub>📶W9 · W↑15d · ↓CMF6d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 23 | ↑52 | ↑1.020 | ↑2d | — | +5.0% | -10.09/-14.16 | +1.79% | 20% |
| [FCL](https://in.tradingview.com/chart/?symbol=NSE:FCL)<br><sub>📶W9 · W↑35d · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 14 | ↑98 | ↑1.068 | ↑6d | — | +14.1% | 48.53/46.33 | +7.87% | 10% 🟨 |
| [GENESYS](https://in.tradingview.com/chart/?symbol=NSE:GENESYS)<br><sub>📶W9 · W↑15d · 🚀SS · ↑CMF23d</sub> | ✓ SAFE | 3D geospatial data maps digital twins urban infrastructure | 📈 BULL_ANY_MID | 5 | ↑16 | ↑1.018 | ↑24d | — | +60.3% | 32.6/32.51 | +1.06% | 10% 🟨 |
| [MVGJL](https://in.tradingview.com/chart/?symbol=NSE:MVGJL)<br><sub>📶W9 · W↑20d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 1 | ↑84 | ↑1.056 | ↑19d | — | +48.6% | 52.44/52.03 | +4.46% | 20% |
| [MAHLIFE](https://in.tradingview.com/chart/?symbol=NSE:MAHLIFE)<br><sub>↑CMF2d</sub> | ⚠ CAUTION | Residential and industrial real estate development across India | ⚡ BULL_ANY_PPV | 88 | 🔄42 | ↑0.997 | ↓7d | SQ·PV | +3.7% | -33.41/-33.64 | +0.83% | 20% |
| [GODREJIND](https://in.tradingview.com/chart/?symbol=NSE:GODREJIND)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Oleochemicals, real estate, agriculture, chemicals holding company | ⚡ BULL_ANY_PPV | 75 | 🔄51 | ↑0.994 | ↓40d | SQ·PV | -16.1% | -51.47/-54.81 | +0.57% | 20% |
| [WAAREEENER](https://in.tradingview.com/chart/?symbol=NSE:WAAREEENER)<br><sub>🚀SS · ↓CMF21d · 🎯SLING</sub> | ✓ SAFE | Solar photovoltaic modules manufacturing renewable energy sector | 🟢 BULL_OVERSOLD | 44 | 🔄9 | ↑0.991 | ↓11d | — | -2.1% | -66.63/-67.04 | +0.52% | 20% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>↑CMF2d · 🎯SLING</sub> | ✓ SAFE | Specialty polyester films for packaging and industrial applications | 🟡 BULL_OS_L2 | 41 | 🔄91 | ↑1.009 | ↓19d | — | -7.0% | -55.37/-58.02 | +4.69% | 10% 🟨 |
| [VOLTAS](https://in.tradingview.com/chart/?symbol=NSE:VOLTAS)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | AC units, refrigeration, EPC projects, cooling systems | 🟡 BULL_OS_L2 | 35 | 🔄14 | ↑0.990 | ↓31d | — | -13.3% | -58.79/-59.21 | +0.43% | 20% |
| [IOC](https://in.tradingview.com/chart/?symbol=NSE:IOC)<br><sub>↑CMF11d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 7 | ↑29 | ↓0.993 | ↓13d | — | -2.2% | -55.32/-55.57 | -0.53% | 20% |
| [TRENT](https://in.tradingview.com/chart/?symbol=NSE:TRENT)<br><sub>↓CMF22d · ⚠️TRAP</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 5 | ↑4 | ↑0.994 | ↓28d | — | -6.9% | -57.9/-58.62 | +0.70% | 20% |
| [BRITANNIA](https://in.tradingview.com/chart/?symbol=NSE:BRITANNIA)<br><sub>↓CMF28d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 5 | ↑22 | ↑0.990 | ↓20d | — | -8.3% | -53.05/-54.83 | -0.02% | 20% |
| [IGARASHI](https://in.tradingview.com/chart/?symbol=NSE:IGARASHI)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | DC motors manufacturing for global automotive sector | 📈 BULL_ANY_MID | 86 | 🔄44 | ↑0.997 | ↓9d | SQ | +2.0% | -8.6/-9.1 | +1.06% | 20% |
| [PASHUPATI](https://in.tradingview.com/chart/?symbol=NSE:PASHUPATI)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 75 | 🔄34 | ↑0.993 | ↓29d | SQ | -6.0% | -45.76/-46.24 | +0.95% | 20% |
| [RECLTD](https://in.tradingview.com/chart/?symbol=NSE:RECLTD)<br><sub>🚀SS · ↓CMF27d</sub> | ✓ SAFE | Power sector financing, generation to distribution infrastructure | 📈 BULL_ANY_MID | 69 | ↑20 | ↑1.005 | ↑1d | SQ | +1.5% | -44.72/-47.19 | +1.52% | 20% |
| [LAXMIDENTL](https://in.tradingview.com/chart/?symbol=NSE:LAXMIDENTL)<br><sub>↑CMF2d</sub> | ✓ SAFE | Dental prosthetics crowns bridges dentures manufacturing India | 📈 BULL_ANY_MID | 68 | ↑20 | ↑1.009 | ↑2d | SQ | +2.0% | -19.4/-25.86 | +1.03% | 20% |
| [RESPONIND](https://in.tradingview.com/chart/?symbol=NSE:RESPONIND)<br><sub>↓CMF30d · ÷DIV</sub> | ✓ SAFE | PVC flooring and polymer products manufacturer for global markets | 📈 BULL_ANY_MID | 59 | 🔄23 | ↑1.004 | ↑1d | — | +2.0% | -3.86/-6.18 | +2.03% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>🚀SS · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 8 | ↑40 | ↑0.999 | ↓17d | — | -1.8% | -39.89/-40.11 | +1.07% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:BALRAMCHIN,NSE:INTERARCH,NSE:GEOJITFSL,NSE:TNPETRO,NSE:ARTEMISMED,NSE:SHOPERSTOP,NSE:ANDHRSUGAR,NSE:JSWDULUX,NSE:MANINFRA,NSE:SDBL,NSE:AVADHSUGAR,NSE:HDFCLIFE,NSE:SBILIFE,NSE:EMIL,NSE:ANTELOPUS,NSE:SBC,NSE:BHAGERIA,NSE:SIGMAADV,NSE:CIPLA,NSE:STARHEALTH,NSE:ELPROINTL,NSE:PUNJABCHEM,NSE:CUPID,NSE:TATASTEEL,NSE:INDHOTEL,NSE:KCP,NSE:KAYNES,NSE:MEESHO,NSE:PNB,NSE:SKFINDIA,NSE:BLUESTARCO,NSE:CYIENT,NSE:PETRONET,NSE:MMFL,NSE:AGARWALEYE,NSE:IDBI,NSE:NAVINFLUOR,NSE:TNPL,NSE:FCL,NSE:GENESYS,NSE:MVGJL,NSE:MAHLIFE,NSE:GODREJIND,NSE:WAAREEENER,NSE:GRWRHITECH,NSE:VOLTAS,NSE:IOC,NSE:TRENT,NSE:BRITANNIA,NSE:IGARASHI,NSE:PASHUPATI,NSE:RECLTD,NSE:LAXMIDENTL,NSE:RESPONIND,NSE:BPCL
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (30)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>📶W9 · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | Sugar production, ethanol distillery, power cogeneration for domestic industrial use | ⚡ BULL_ANY_PPV | 99 | 🔄83 | ↑1.015 | ↑1d | SQ·PV | +4.0% | -12.75/-13.75 | +4.00% | 20% |
| [INTERARCH](https://in.tradingview.com/chart/?symbol=NSE:INTERARCH)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Pre-engineered steel buildings manufacturing industrial commercial structures | ⚡ BULL_ANY_PPV | 99 | 🔄20 | ↑1.010 | ↑1d | SQ·PV | +2.5% | -15.86/-16.05 | +2.45% | 20% |
| [GEOJITFSL](https://in.tradingview.com/chart/?symbol=NSE:GEOJITFSL)<br><sub>📶W9 · ↓CMF16d</sub> | ⚠ CAUTION | Stock broking and portfolio management for retail investors | ⚡ BULL_ANY_PPV | 99 | 🔄62 | ↑1.011 | ↑1d | SQ·PV | +3.0% | 3.25/2.86 | +2.96% | 20% |
| [TNPETRO](https://in.tradingview.com/chart/?symbol=NSE:TNPETRO)<br><sub>📶W9 · W↑123d · ↑CMF18d</sub> | ✓ SAFE | Petrochemical intermediates and detergent raw materials manufacturer | ⚡ BULL_ANY_PPV | 94 | 🔄83 | ↑1.029 | ↑1d | SQ·PV | +4.7% | 23.78/21.24 | +4.69% | 20% |
| [ARTEMISMED](https://in.tradingview.com/chart/?symbol=NSE:ARTEMISMED)<br><sub>📶W9 · W↑60d · 🚀SS·50x · ↓CMF0d</sub> | ✓ SAFE | Tertiary care hospital operator, multi-specialty healthcare delivery Gurgaon | ⚡ BULL_ANY_PPV | 89 | 🔄86 | ↑1.050 | ↑1d | SQ·PV | +7.5% | 44.0/37.56 | +7.51% | 20% |
| [SHOPERSTOP](https://in.tradingview.com/chart/?symbol=NSE:SHOPERSTOP)<br><sub>📶W9 · W↑5d · RVOL17x · ↑CMF0d</sub> | ✓ SAFE | Department store operator, fashion beauty retail, urban consumers | ⚡ BULL_ANY_PPV | 89 | 🔄61 | ↑1.067 | ↑1d | SQ·PV | +10.0% | 8.16/2.6 | +10.00% | 20% |
| [ANDHRSUGAR](https://in.tradingview.com/chart/?symbol=NSE:ANDHRSUGAR)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Sugar, industrial chemicals, fertilizers manufacturing and alcohol | ⚡ BULL_ANY_PPV | 82 | 🔄74 | ↑1.004 | ↓18d | SQ·PV | -1.1% | -28.57/-28.69 | +2.61% | 20% |
| [JSWDULUX](https://in.tradingview.com/chart/?symbol=NSE:JSWDULUX)<br><sub>📶W9 · W↑35d · ↓CMF3d</sub> | ⚠ CAUTION | Paints coatings manufacturer automotive industrial decorative | ⚡ BULL_ANY_PPV | 69 | ↑45 | ↑1.014 | ↑1d | SQ·PV | +2.1% | 21.18/17.37 | +2.15% | 20% |
| [MANINFRA](https://in.tradingview.com/chart/?symbol=NSE:MANINFRA)<br><sub>📶W9 · W↑40d · ↑CMF26d</sub> | ✓ SAFE | EPC contractor, ports, residential, commercial real estate development | ⚡ BULL_ANY_PPV | 59 | ↑68 | ↑1.035 | ↑1d | SQ·PV | +4.7% | 27.64/23.24 | +4.65% | 20% |
| [STARHEALTH](https://in.tradingview.com/chart/?symbol=NSE:STARHEALTH)<br><sub>📶W9 · ↑CMF1d · 🎯SLING</sub> | ✓ SAFE | Health insurance provider, retail customers, India | 🟡 BULL_OS_L2 | 69 | ↑60 | ↑1.009 | ↑1d | SQ | +1.4% | -46.78/-54.17 | +1.41% | 20% |
| [ELPROINTL](https://in.tradingview.com/chart/?symbol=NSE:ELPROINTL)<br><sub>📶W9 · ↓CMF14d · ⚠️TRAP</sub> | ⚠ CAUTION | Surge arresters manufacturing, real estate development, renewable energy | 🟡 BULL_OS_L2 | 48 | ↑50 | ↓0.996 | ↓12d | SQ | -1.3% | -54.24/-54.87 | -0.12% | 10% 🟨 |
| [PUNJABCHEM](https://in.tradingview.com/chart/?symbol=NSE:PUNJABCHEM)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Agrochemicals pesticides fertilizers crop protection chemicals manufacturing | 📈 BULL_ANY_MID | 99 | 🔄42 | ↑1.007 | ↑1d | SQ | +2.2% | -43.18/-45.37 | +2.23% | 20% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>📶W9 · 🚀SS · ↑CMF2d</sub> | ✓ SAFE | Condoms lubricants IVD kits sexual wellness global | 📈 BULL_ANY_MID | 91 | 🔄99 | ↑1.000 | ↓9d | SQ | -3.6% | -24.06/-26.78 | +1.39% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>📶W9 · ↑CMF27d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 69 | ↑46 | ↑1.011 | ↑1d | SQ | +2.3% | -10.62/-12.03 | +2.27% | 20% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>📶W9 · ↑CMF24d</sub> | ⚠ CAUTION | Luxury and midscale hotel brands across Asia Pacific | 📈 BULL_ANY_MID | 69 | ↑47 | ↑1.008 | ↑1d | SQ | +1.6% | -22.75/-27.38 | +1.64% | 20% |
| [KCP](https://in.tradingview.com/chart/?symbol=NSE:KCP)<br><sub>📶W9 · ↓CMF4d</sub> | ⚠ CAUTION | Cement sugar heavy engineering power hospitality conglomerate | 📈 BULL_ANY_MID | 64 | ↑40 | ↑1.019 | ↑1d | SQ | +2.6% | -31.14/-36.44 | +2.58% | 20% |
| [KAYNES](https://in.tradingview.com/chart/?symbol=NSE:KAYNES)<br><sub>📶W9 · 🚀SS · ↓CMF20d</sub> | ✓ SAFE | Electronics manufacturing, IoT solutions, industrial and consumer products | 📈 BULL_ANY_MID | 59 | ↑36 | ↑1.032 | ↑1d | SQ | +4.0% | -14.83/-21.5 | +4.00% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · W↑30d · ↑CMF30d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.025 | ↑2d | SQ | +6.1% | 49.69/48.04 | -0.06% | 20% 🟦 |
| [PNB](https://in.tradingview.com/chart/?symbol=NSE:PNB)<br><sub>📶W9 · W↑72d · ↓CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | ↑52 | ↓1.004 | ↑2d | SQ | +1.8% | 22.16/15.43 | -0.05% | 20% |
| [SKFINDIA](https://in.tradingview.com/chart/?symbol=NSE:SKFINDIA)<br><sub>📶W9 · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Rolling bearings, seals, lubrication for industrial automotive machinery | 📈 BULL_ANY_MID | 58 | ↑24 | ↓1.004 | ↑2d | SQ | +1.3% | -18.96/-24.31 | -0.14% | 20% |
| [BLUESTARCO](https://in.tradingview.com/chart/?symbol=NSE:BLUESTARCO)<br><sub>📶W9 · W↑10d · ↑CMF11d</sub> | ✓ SAFE | AC units, refrigeration, MEP projects for commercial facilities | 📈 BULL_ANY_MID | 57 | ↑30 | ↑1.021 | ↑8d | SQ | +5.5% | 23.7/21.42 | +2.62% | 20% |
| [PETRONET](https://in.tradingview.com/chart/?symbol=NSE:PETRONET)<br><sub>📶W9 · ↑CMF2d</sub> | ⚠ CAUTION | LNG import regasification terminals serving Indian gas utilities | 📈 BULL_ANY_MID | 54 | ↑52 | ↓1.001 | ↓6d | SQ | +1.1% | -16.89/-17.51 | -0.03% | 20% |
| [MMFL](https://in.tradingview.com/chart/?symbol=NSE:MMFL)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE | Steel forging components for vehicles and machinery | 📈 BULL_ANY_MID | 53 | ↑91 | ↑1.000 | ↓12d | SQ | -0.1% | -19.7/-20.25 | +0.55% | 20% |
| [AGARWALEYE](https://in.tradingview.com/chart/?symbol=NSE:AGARWALEYE)<br><sub>📶W9 · ↑CMF30d</sub> | ⚠ CAUTION | Eye care surgery and diagnostics across India Africa | 📈 BULL_ANY_MID | 40 | ↑55 | ↓0.999 | ↓21d | SQ | +0.7% | -26.64/-28.84 | -0.42% | 20% |
| [MAHLIFE](https://in.tradingview.com/chart/?symbol=NSE:MAHLIFE)<br><sub>↑CMF2d</sub> | ⚠ CAUTION | Residential and industrial real estate development across India | ⚡ BULL_ANY_PPV | 88 | 🔄42 | ↑0.997 | ↓7d | SQ·PV | +3.7% | -33.41/-33.64 | +0.83% | 20% |
| [GODREJIND](https://in.tradingview.com/chart/?symbol=NSE:GODREJIND)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Oleochemicals, real estate, agriculture, chemicals holding company | ⚡ BULL_ANY_PPV | 75 | 🔄51 | ↑0.994 | ↓40d | SQ·PV | -16.1% | -51.47/-54.81 | +0.57% | 20% |
| [IGARASHI](https://in.tradingview.com/chart/?symbol=NSE:IGARASHI)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | DC motors manufacturing for global automotive sector | 📈 BULL_ANY_MID | 86 | 🔄44 | ↑0.997 | ↓9d | SQ | +2.0% | -8.6/-9.1 | +1.06% | 20% |
| [PASHUPATI](https://in.tradingview.com/chart/?symbol=NSE:PASHUPATI)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 75 | 🔄34 | ↑0.993 | ↓29d | SQ | -6.0% | -45.76/-46.24 | +0.95% | 20% |
| [RECLTD](https://in.tradingview.com/chart/?symbol=NSE:RECLTD)<br><sub>🚀SS · ↓CMF27d</sub> | ✓ SAFE | Power sector financing, generation to distribution infrastructure | 📈 BULL_ANY_MID | 69 | ↑20 | ↑1.005 | ↑1d | SQ | +1.5% | -44.72/-47.19 | +1.52% | 20% |
| [LAXMIDENTL](https://in.tradingview.com/chart/?symbol=NSE:LAXMIDENTL)<br><sub>↑CMF2d</sub> | ✓ SAFE | Dental prosthetics crowns bridges dentures manufacturing India | 📈 BULL_ANY_MID | 68 | ↑20 | ↑1.009 | ↑2d | SQ | +2.0% | -19.4/-25.86 | +1.03% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:BALRAMCHIN,NSE:INTERARCH,NSE:GEOJITFSL,NSE:TNPETRO,NSE:ARTEMISMED,NSE:SHOPERSTOP,NSE:ANDHRSUGAR,NSE:JSWDULUX,NSE:MANINFRA,NSE:STARHEALTH,NSE:ELPROINTL,NSE:PUNJABCHEM,NSE:CUPID,NSE:TATASTEEL,NSE:INDHOTEL,NSE:KCP,NSE:KAYNES,NSE:MEESHO,NSE:PNB,NSE:SKFINDIA,NSE:BLUESTARCO,NSE:PETRONET,NSE:MMFL,NSE:AGARWALEYE,NSE:MAHLIFE,NSE:GODREJIND,NSE:IGARASHI,NSE:PASHUPATI,NSE:RECLTD,NSE:LAXMIDENTL
```

---

### 🔥 MAJOR — PPV confirmed (9)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SDBL](https://in.tradingview.com/chart/?symbol=NSE:SDBL)<br><sub>📶W9 · 🚀SS·51x · ↑CMF0d</sub> | ✓ SAFE | Beer and spirits manufacturer for Indian consumer market | ⚡ BULL_ANY_PPV | 49 | 🔄28 | ↑1.069 | ↑1d | PV | +10.6% | -32.49/-45.16 | +10.59% | 20% |
| [AVADHSUGAR](https://in.tradingview.com/chart/?symbol=NSE:AVADHSUGAR)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Sugar cane processing, ethanol, power generation | ⚡ BULL_ANY_PPV | 49 | 🔄95 | ↑1.058 | ↑1d | PV | +10.0% | -15.96/-19.83 | +10.00% | 5% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>📶W9 · W↑3d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 19 | ↑14 | ↑1.042 | ↑1d | PV | +5.0% | -31.89/-43.91 | +5.05% | 20% |
| [SBILIFE](https://in.tradingview.com/chart/?symbol=NSE:SBILIFE)<br><sub>📶W9 · ↓CMF16d · 🎯SLING</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 19 | ↑36 | ↑1.031 | ↑1d | PV | +4.2% | -50.09/-59.33 | +4.19% | 20% |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL)<br><sub>📶W9 · W↑5d · 🚀SS · ↑CMF11d</sub> | ✓ SAFE | Consumer electronics retail chain South India operations | ⚡ BULL_ANY_PPV | 13 | ↑94 | ↑1.049 | ↑7d | PV | +10.7% | 43.75/39.75 | +5.85% | 20% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>📶W9 · W↑20d · ↑CMF17d · ÷DIV</sub> | ✓ SAFE | Oil and gas exploration production Indian subcontinent hydrocarbon resources | ⚡ BULL_ANY_PPV | 2 | ↑98 | ↑1.109 | ↑18d | PV | +59.2% | 47.89/43.77 | +11.56% | 5% 🟥 |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>📶W9 · W↑20d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 0 | ↑94 | ↑1.081 | ↑22d | PV | +32.1% | 55.4/52.91 | +10.44% | 20% |
| [BHAGERIA](https://in.tradingview.com/chart/?symbol=NSE:BHAGERIA)<br><sub>📶W9 · W↑24d · 🚀SS · ★ · ↑CMF23d</sub> | ✓ SAFE | Dye intermediates, specialty dyes, chemicals manufacturer | ⚡ BULL_ANY_PPV | 0 | ↑98 | ↑1.144 | ↑25d | PV | +90.9% | 67.73/65.66 | +9.72% | 5% 🟥 |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SDBL,NSE:AVADHSUGAR,NSE:HDFCLIFE,NSE:SBILIFE,NSE:EMIL,NSE:ANTELOPUS,NSE:SBC,NSE:BHAGERIA,NSE:SIGMAADV
```

### 🟢 OVERSOLD — reversal from −53/−60 (21)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CIPLA](https://in.tradingview.com/chart/?symbol=NSE:CIPLA)<br><sub>📶W9 · 🚀SS · ↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 10 | ↑41 | ↑1.005 | ↓37d | — | -1.7% | -61.96/-65.24 | +1.99% | 20% |
| [WAAREEENER](https://in.tradingview.com/chart/?symbol=NSE:WAAREEENER)<br><sub>🚀SS · ↓CMF21d · 🎯SLING</sub> | ✓ SAFE | Solar photovoltaic modules manufacturing renewable energy sector | 🟢 BULL_OVERSOLD | 44 | 🔄9 | ↑0.991 | ↓11d | — | -2.1% | -66.63/-67.04 | +0.52% | 20% |
| [AVANTIFEED](https://in.tradingview.com/chart/?symbol=NSE:AVANTIFEED)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Shrimp feed manufacturing and shrimp export aquaculture | 🟢 BULL_OVERSOLD | 11 | ↓15 | ↑0.980 | ↓14d | — | -4.2% | -62.65/-63.68 | +0.45% | 20% 🟦 |
| [GRMOVER](https://in.tradingview.com/chart/?symbol=NSE:GRMOVER)<br><sub>↑CMF0d · 🎯SLING</sub> | ✓ SAFE | Basmati rice milling processing domestic export markets | 🟢 BULL_OVERSOLD | 11 | ↓2 | ↑0.985 | ↓14d | — | -6.0% | -62.03/-62.07 | +0.95% | 10% 🟨 |
| [MARUTI](https://in.tradingview.com/chart/?symbol=NSE:MARUTI)<br><sub>↓CMF14d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 5 | ↓21 | ↑0.986 | ↓38d | — | -7.9% | -68.17/-68.97 | +1.78% | 20% |
| [ASIANPAINT](https://in.tradingview.com/chart/?symbol=NSE:ASIANPAINT)<br><sub>🚀SS · ↑CMF30d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 5 | ↓34 | ↑0.988 | ↓26d | — | -10.5% | -65.89/-66.6 | +1.32% | 20% |
| [BAYERCROP](https://in.tradingview.com/chart/?symbol=NSE:BAYERCROP)<br><sub>↓CMF9d · ⚠️TRAP</sub> | ⚠ CAUTION | Crop protection chemicals and seeds for Indian farmers | 🟢 BULL_OVERSOLD | 5 | ↓12 | ↑0.975 | ↓52d | — | -9.6% | -76.13/-76.26 | -0.50% | 20% |
| [NACLIND](https://in.tradingview.com/chart/?symbol=NSE:NACLIND)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Crop protection chemicals, technicals and formulations, Indian and export | 🟢 BULL_OVERSOLD | 5 | ↓5 | ↑0.960 | ↓24d | — | -20.6% | -69.51/-70.57 | +0.24% | 20% 🟦 |
| [GRINFRA](https://in.tradingview.com/chart/?symbol=NSE:GRINFRA)<br><sub>🚀SS · ↓CMF14d · 🎯SLING</sub> | ⚠ CAUTION | Road EPC contractor, highways and railways infrastructure | 🟢 BULL_OVERSOLD | 5 | ↓13 | ↑0.984 | ↓24d | — | -7.6% | -63.19/-63.54 | +0.26% | 20% |
| [DBCORP](https://in.tradingview.com/chart/?symbol=NSE:DBCORP)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Print media, newspapers, advertising, pan-India distribution network | 🟢 BULL_OVERSOLD | 5 | ↓13 | ↑0.984 | ↓57d | — | -8.0% | -65.38/-65.73 | +0.78% | 20% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>↑CMF2d · 🎯SLING</sub> | ✓ SAFE | Specialty polyester films for packaging and industrial applications | 🟡 BULL_OS_L2 | 41 | 🔄91 | ↑1.009 | ↓19d | — | -7.0% | -55.37/-58.02 | +4.69% | 10% 🟨 |
| [VOLTAS](https://in.tradingview.com/chart/?symbol=NSE:VOLTAS)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | AC units, refrigeration, EPC projects, cooling systems | 🟡 BULL_OS_L2 | 35 | 🔄14 | ↑0.990 | ↓31d | — | -13.3% | -58.79/-59.21 | +0.43% | 20% |
| [ADANIENSOL](https://in.tradingview.com/chart/?symbol=NSE:ADANIENSOL)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 10 | ↓74 | ↑0.987 | ↓15d | — | -12.5% | -58.7/-59.55 | +1.85% | 20% |
| [IOC](https://in.tradingview.com/chart/?symbol=NSE:IOC)<br><sub>↑CMF11d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 7 | ↑29 | ↓0.993 | ↓13d | — | -2.2% | -55.32/-55.57 | -0.53% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>↓CMF11d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 7 | ↓53 | ↓0.988 | ↓13d | — | -5.3% | -57.62/-58.54 | -0.51% | 20% |
| [GUJENERGY](https://in.tradingview.com/chart/?symbol=NSE:GUJENERGY)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Piped natural gas distribution to households and industries | 🟡 BULL_OS_L2 | 7 | ↓1 | ↑0.983 | ↓18d | — | -7.2% | -57.23/-57.28 | +0.13% | 5% |
| [M&M](https://in.tradingview.com/chart/?symbol=NSE:M&M)<br><sub>↓CMF13d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 5 | ↓34 | ↑0.986 | ↓45d | — | +0.1% | -54.94/-55.48 | +0.52% | 20% |
| [TRENT](https://in.tradingview.com/chart/?symbol=NSE:TRENT)<br><sub>↓CMF22d · ⚠️TRAP</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 5 | ↑4 | ↑0.994 | ↓28d | — | -6.9% | -57.9/-58.62 | +0.70% | 20% |
| [BRITANNIA](https://in.tradingview.com/chart/?symbol=NSE:BRITANNIA)<br><sub>↓CMF28d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 5 | ↑22 | ↑0.990 | ↓20d | — | -8.3% | -53.05/-54.83 | -0.02% | 20% |
| [TTKPRESTIG](https://in.tradingview.com/chart/?symbol=NSE:TTKPRESTIG)<br><sub>🚀SS · ↓CMF23d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Pressure cookers, cookware, kitchen appliances for households | 🟡 BULL_OS_L2 | 5 | ↓24 | ↑0.989 | ↓23d | — | -11.9% | -58.92/-59.83 | +1.77% | 20% |
| [TECHNVISN](https://in.tradingview.com/chart/?symbol=NSE:TECHNVISN)<br><sub>↓CMF8d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 5 | ↓50 | ↑0.971 | ↓22d | — | -13.0% | -54.45/-55.17 | +1.16% | 20% 🟦 |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CIPLA,NSE:WAAREEENER,NSE:AVANTIFEED,NSE:GRMOVER,NSE:MARUTI,NSE:ASIANPAINT,NSE:BAYERCROP,NSE:NACLIND,NSE:GRINFRA,NSE:DBCORP,NSE:GRWRHITECH,NSE:VOLTAS,NSE:ADANIENSOL,NSE:IOC,NSE:NESTLEIND,NSE:GUJENERGY,NSE:M&M,NSE:TRENT,NSE:BRITANNIA,NSE:TTKPRESTIG,NSE:TECHNVISN
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (10)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CYIENT](https://in.tradingview.com/chart/?symbol=NSE:CYIENT)<br><sub>📶W9 · W↑40d · ↑CMF26d</sub> | ✓ SAFE | Engineering services, product design, manufacturing sector solutions | 📈 BULL_ANY_MID | 54 | 🔄67 | ↑1.020 | ↑1d | — | +3.5% | 17.69/15.56 | +3.49% | 20% |
| [IDBI](https://in.tradingview.com/chart/?symbol=NSE:IDBI)<br><sub>📶W9 · ↓CMF13d</sub> | ⚠ CAUTION | Retail corporate MSME lending deposit bank | 📈 BULL_ANY_MID | 29 | ↑48 | ↑1.010 | ↑1d | — | +2.2% | -20.63/-22.75 | +2.18% | 20% 🟦 |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>📶W9 · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | Specialty fluorochemicals refrigerants organic synthesis pharmaceutical | 📈 BULL_ANY_MID | 29 | ↑84 | ↑1.012 | ↑1d | — | +1.5% | 12.07/8.76 | +1.46% | 20% |
| [TNPL](https://in.tradingview.com/chart/?symbol=NSE:TNPL)<br><sub>📶W9 · W↑15d · ↓CMF6d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 23 | ↑52 | ↑1.020 | ↑2d | — | +5.0% | -10.09/-14.16 | +1.79% | 20% |
| [FCL](https://in.tradingview.com/chart/?symbol=NSE:FCL)<br><sub>📶W9 · W↑35d · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 14 | ↑98 | ↑1.068 | ↑6d | — | +14.1% | 48.53/46.33 | +7.87% | 10% 🟨 |
| [GENESYS](https://in.tradingview.com/chart/?symbol=NSE:GENESYS)<br><sub>📶W9 · W↑15d · 🚀SS · ↑CMF23d</sub> | ✓ SAFE | 3D geospatial data maps digital twins urban infrastructure | 📈 BULL_ANY_MID | 5 | ↑16 | ↑1.018 | ↑24d | — | +60.3% | 32.6/32.51 | +1.06% | 10% 🟨 |
| [MVGJL](https://in.tradingview.com/chart/?symbol=NSE:MVGJL)<br><sub>📶W9 · W↑20d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 1 | ↑84 | ↑1.056 | ↑19d | — | +48.6% | 52.44/52.03 | +4.46% | 20% |
| [RESPONIND](https://in.tradingview.com/chart/?symbol=NSE:RESPONIND)<br><sub>↓CMF30d · ÷DIV</sub> | ✓ SAFE | PVC flooring and polymer products manufacturer for global markets | 📈 BULL_ANY_MID | 59 | 🔄23 | ↑1.004 | ↑1d | — | +2.0% | -3.86/-6.18 | +2.03% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>🚀SS · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 8 | ↑40 | ↑0.999 | ↓17d | — | -1.8% | -39.89/-40.11 | +1.07% | 20% |
| [INGERRAND](https://in.tradingview.com/chart/?symbol=NSE:INGERRAND)<br><sub>↓CMF6d</sub> | ✓ SAFE | Air compressors, power tools, industrial manufacturing sector | 📈 BULL_ANY_MID | 5 | ↓54 | ↑0.986 | ↓32d | — | -1.4% | -39.82/-40.36 | -0.02% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CYIENT,NSE:IDBI,NSE:NAVINFLUOR,NSE:TNPL,NSE:FCL,NSE:GENESYS,NSE:MVGJL,NSE:RESPONIND,NSE:BPCL,NSE:INGERRAND
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
