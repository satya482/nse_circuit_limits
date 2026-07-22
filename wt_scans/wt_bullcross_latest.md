> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-07-22
*Generated 2026-07-22 15:44 IST*

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

**Total bull crosses today: 79** · 41 inside active squeeze

```
NSE:PIDILITIND,NSE:EVEREADY,NSE:SHRIRAMFIN,NSE:PRIVISCL,NSE:CRAMC,NSE:MEDANTA,NSE:WAKEFIT,NSE:UFLEX,NSE:COSMOFIRST,NSE:DATAPATTNS,NSE:PNGJL,NSE:TVSHLTD,NSE:SEDEMAC,NSE:RGL,NSE:NEPHROPLUS,NSE:METROPOLIS,NSE:ENTERO,NSE:PNGSREVA,NSE:INDIQUBE,NSE:INDIGO,NSE:MEESHO,NSE:ZENTEC,NSE:SKFINDUS,NSE:NGLFINE,NSE:STEELCAS,NSE:MARICO,NSE:ARTEMISMED,NSE:AVALON,NSE:KERNEX,NSE:MANKIND,NSE:TVSMOTOR,NSE:ABCAPITAL,NSE:NESTLEIND,NSE:HCG,NSE:WESTLIFE,NSE:TARSONS,NSE:SPECTRUM,NSE:VERANDA,NSE:RRKABEL,NSE:EMIL,NSE:ADANIENT,NSE:BALAMINES,NSE:AEGISVOPAK,NSE:POLYPLEX,NSE:TRUALT,NSE:TARC,NSE:GMRP&UI,NSE:ALICON,NSE:GULPOLY,NSE:BAJEL,NSE:PATANJALI,NSE:GPIL,NSE:PGHH,NSE:NTPC,NSE:VMM,NSE:MUTHOOTFIN,NSE:HINDZINC,NSE:PETRONET,NSE:ARFIN,NSE:SHREDIGCEM,NSE:KINGFA,NSE:IGIL,NSE:IMFA,NSE:BANARISUG,NSE:CLSEL,NSE:GAIL,NSE:GRASIM,NSE:HINDCOPPER,NSE:TATASTEEL,NSE:POWERINDIA,NSE:ENRIN,NSE:HONDAPOWER,NSE:WONDERLA,NSE:ADANIPOWER,NSE:GRSE,NSE:PFOCUS,NSE:SAIL,NSE:TIINDIA,NSE:VINDHYATEL
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (44)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · W↑68d · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄61 | ↑1.012 | ↑1d | SQ·PV | +2.0% | 3.64/3.38 | +1.99% | 20% |
| [EVEREADY](https://in.tradingview.com/chart/?symbol=NSE:EVEREADY)<br><sub>📶W9 · W↑71d · ↓CMF7d</sub> | ✓ SAFE | Dry cells batteries flashlights consumer household products | ⚡ BULL_ANY_PPV | 94 | 🔄58 | ↑1.028 | ↑1d | SQ·PV | +3.6% | -19.14/-23.82 | +3.61% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑26d · 🚀SS · ↓CMF12d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 92 | 🔄79 | ↑1.024 | ↑3d | SQ·PV | +3.9% | 17.16/12.64 | +2.75% | 20% |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL)<br><sub>📶W9 · W↑33d · ↑CMF29d</sub> | ✓ SAFE | Fragrance and flavor chemical manufacturer for personal care | ⚡ BULL_ANY_PPV | 90 | 🔄84 | ↑1.002 | ↑10d | SQ·PV | +3.6% | 41.39/39.46 | +0.05% | 20% |
| [CRAMC](https://in.tradingview.com/chart/?symbol=NSE:CRAMC)<br><sub>📶W9 · W↑27d · 🚀SS·88x · ↓CMF0d</sub> | ✓ SAFE | Mutual funds and investment advisory for Indian retail investors | ⚡ BULL_ANY_PPV | 89 | 🔄50 | ↑1.033 | ↑1d | SQ·PV | +5.5% | 37.47/31.51 | +5.47% | 20% |
| [MEDANTA](https://in.tradingview.com/chart/?symbol=NSE:MEDANTA)<br><sub>📶W9 · W↑71d · ↓CMF11d</sub> | ⚠ CAUTION | Multi-specialty tertiary hospitals, cardiology-focused, North-East India | ⚡ BULL_ANY_PPV | 67 | ↑67 | ↑1.014 | ↑3d | SQ·PV | +2.8% | 38.66/32.68 | +0.80% | 20% |
| [WAKEFIT](https://in.tradingview.com/chart/?symbol=NSE:WAKEFIT)<br><sub>📶W9 · 🚀SS·46x · ↑CMF9d</sub> | ✓ SAFE | Sleep mattresses furniture direct-to-consumer e-commerce home | ⚡ BULL_ANY_PPV | 49 | 🔄50 | ↑1.091 | ↑1d | PV | +13.2% | 39.67/35.28 | +13.22% | 20% |
| [UFLEX](https://in.tradingview.com/chart/?symbol=NSE:UFLEX)<br><sub>📶W9 · W↑71d · 🚀SS·283x · ↑CMF0d</sub> | ✓ SAFE | Flexible packaging films, laminates for food beverage | ⚡ BULL_ANY_PPV | 35 | 🔄55 | ↑1.095 | ↑15d | PV | +16.1% | 51.65/39.16 | +11.60% | 20% |
| [COSMOFIRST](https://in.tradingview.com/chart/?symbol=NSE:COSMOFIRST)<br><sub>📶W9 · W↑28d · ↑CMF0d</sub> | ✓ SAFE | Specialty films for packaging lamination labeling applications | ⚡ BULL_ANY_PPV | 30 | 🔄67 | ↑1.036 | ↑27d | PV | +18.3% | 45.67/41.65 | +4.36% | 20% |
| [DATAPATTNS](https://in.tradingview.com/chart/?symbol=NSE:DATAPATTNS)<br><sub>📶W9 · 🚀SS·11x · ↑CMF0d</sub> | ✓ SAFE | Defense aerospace electronics systems design manufacturing | ⚡ BULL_ANY_PPV | 19 | ↑93 | ↑1.107 | ↑1d | PV | +12.7% | -28.55/-39.45 | +12.70% | 20% |
| [PNGJL](https://in.tradingview.com/chart/?symbol=NSE:PNGJL)<br><sub>📶W9 · W↑13d · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | Gold jewelry retail with regional Maharashtra presence | ⚡ BULL_ANY_PPV | 5 | ↑44 | ↑1.066 | ↑15d | PV | +17.9% | 48.81/40.64 | +5.97% | 10% 🟩 |
| [TVSHLTD](https://in.tradingview.com/chart/?symbol=NSE:TVSHLTD)<br><sub>📶W9 · W↑18d · 🚀SS·17x · ↓CMF23d</sub> | ⚠ CAUTION | Aluminum die-castings automotive components manufacturing holding company | ⚡ BULL_ANY_PPV | 0 | ↑62 | ↑1.046 | ↑20d | PV | +11.1% | 49.07/36.63 | +4.29% | 20% |
| [SEDEMAC](https://in.tradingview.com/chart/?symbol=NSE:SEDEMAC)<br><sub>📶W9 · 🚀SS · ↓CMF19d</sub> | ✓ SAFE | Engine control units, mechatronics for automotive and off-highway | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.024 | ↑1d | SQ | +4.2% | -6.38/-9.39 | +4.22% | 20% |
| [RGL](https://in.tradingview.com/chart/?symbol=NSE:RGL)<br><sub>📶W9 · W↑28d · ↓CMF0d</sub> | ✓ SAFE | Global recruitment and staffing services provider | 📈 BULL_ANY_MID | 90 | 🔄56 | ↑1.005 | ↑10d | SQ | +4.0% | 38.24/37.91 | +0.32% | 20% |
| [NEPHROPLUS](https://in.tradingview.com/chart/?symbol=NSE:NEPHROPLUS)<br><sub>📶W9 · ↓CMF16d</sub> | ✓ SAFE | Dialysis treatment centers for kidney disease patients | 📈 BULL_ANY_MID | 89 | 🔄50 | ↑1.046 | ↑1d | SQ | +7.3% | -29.23/-35.58 | +7.35% | 20% |
| [METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS)<br><sub>📶W9 · W↑71d · ↓CMF25d</sub> | ⚠ CAUTION | Diagnostic pathology labs clinical testing centers urban India | 📈 BULL_ANY_MID | 67 | ↑74 | ↑1.009 | ↑3d | SQ | +4.5% | 44.7/44.48 | +0.23% | 20% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>📶W9 · W↑13d · ↑CMF7d</sub> | ⚠ CAUTION | Pharmaceutical surgical products distributor hospitals clinics retail | 📈 BULL_ANY_MID | 63 | ↑52 | ↑1.023 | ↑2d | SQ | +4.2% | 23.33/21.87 | +1.78% | 20% |
| [PNGSREVA](https://in.tradingview.com/chart/?symbol=NSE:PNGSREVA)<br><sub>📶W9 · ↓CMF24d</sub> | ✓ SAFE | Diamond jewellery retail, precious stones, Indian consumers | 📈 BULL_ANY_MID | 63 | ↑50 | ↑1.022 | ↑2d | SQ | +3.2% | 23.24/18.73 | +1.47% | 20% |
| [INDIQUBE](https://in.tradingview.com/chart/?symbol=NSE:INDIQUBE)<br><sub>📶W9 · W↑28d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 63 | ↑50 | ↑1.023 | ↑2d | SQ | +7.0% | 21.09/19.67 | +1.71% | 20% |
| [INDIGO](https://in.tradingview.com/chart/?symbol=NSE:INDIGO)<br><sub>📶W9 · W↑45d · 🚀SS · ↑CMF29d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄49 | ↑1.008 | ↑1d | — | +1.1% | 20.36/20.19 | +1.11% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · ↑CMF9d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers, rural consumers | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.005 | ↑2d | SQ | +2.2% | 16.26/14.13 | -1.01% | 20% 🟦 |
| [ZENTEC](https://in.tradingview.com/chart/?symbol=NSE:ZENTEC)<br><sub>📶W9 · ↓CMF5d</sub> | ✓ SAFE | Defense simulation systems and counter-drone solutions manufacturer | 📈 BULL_ANY_MID | 58 | ↑70 | ↓1.005 | ↓2d | SQ | +3.7% | -7.32/-7.9 | -0.22% | 20% |
| [SKFINDUS](https://in.tradingview.com/chart/?symbol=NSE:SKFINDUS)<br><sub>📶W9 · ↓CMF14d</sub> | ⚠ CAUTION | Rolling bearings seals lubrication industrial machinery | 📈 BULL_ANY_MID | 58 | ↑50 | ↓0.999 | ↓2d | SQ | +2.9% | -1.42/-2.25 | -2.84% | 20% |
| [NGLFINE](https://in.tradingview.com/chart/?symbol=NSE:NGLFINE)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Veterinary APIs, intermediates, animal health pharmaceuticals manufacturer | 📈 BULL_ANY_MID | 58 | ↑98 | ↓1.032 | ↑2d | SQ | +8.2% | 27.66/23.21 | +0.58% | 20% |
| [STEELCAS](https://in.tradingview.com/chart/?symbol=NSE:STEELCAS)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Steel castings manufacturer for heavy industrial equipment OEMs | 📈 BULL_ANY_MID | 58 | ↑81 | ↓1.003 | ↑2d | SQ | +0.5% | 14.8/14.37 | -0.08% | 20% |
| [MARICO](https://in.tradingview.com/chart/?symbol=NSE:MARICO)<br><sub>📶W9 · W↑17d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↑68 | ↓1.010 | ↑3d | SQ | +2.0% | 39.15/35.61 | +0.08% | 20% |
| [ARTEMISMED](https://in.tradingview.com/chart/?symbol=NSE:ARTEMISMED)<br><sub>📶W9 · W↑13d · ↑CMF1d</sub> | ✓ SAFE | Tertiary care hospital operator, multi-specialty, urban healthcare delivery | 📈 BULL_ANY_MID | 57 | ↑68 | ↓1.003 | ↑3d | SQ | +1.5% | 33.31/31.83 | -1.30% | 20% |
| [AVALON](https://in.tradingview.com/chart/?symbol=NSE:AVALON)<br><sub>📶W9 · ↓CMF14d</sub> | ✓ SAFE | Electronics manufacturing services for high-complexity defense telecom products | 📈 BULL_ANY_MID | 55 | ↑97 | ↓1.006 | ↓5d | SQ | +3.8% | 18.97/11.49 | +0.04% | 20% |
| [KERNEX](https://in.tradingview.com/chart/?symbol=NSE:KERNEX)<br><sub>📶W9 · ↑CMF3d</sub> | ✓ SAFE | Railway safety systems and software developer for trains | 📈 BULL_ANY_MID | 54 | 🔄97 | ↑1.021 | ↑1d | — | +3.0% | 10.17/9.92 | +3.01% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>📶W9 · W↑65d · ↓CMF6d</sub> | ✓ SAFE | Pharma formulations acute chronic diseases consumer health | 📈 BULL_ANY_MID | 51 | ↑63 | ↑1.009 | ↑19d | SQ | +7.4% | 47.69/43.74 | +0.35% | 20% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>📶W9 · W↑21d · ↓CMF9d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄61 | ↑1.043 | ↑1d | — | +5.7% | 34.69/30.07 | +5.68% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑69d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 46 | 🔄80 | ↑1.020 | ↑9d | — | +6.3% | 40.54/39.46 | +2.18% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑17d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 28 | ↑66 | ↑1.011 | ↑2d | — | +2.0% | 14.61/10.66 | +0.67% | 20% |
| [HCG](https://in.tradingview.com/chart/?symbol=NSE:HCG)<br><sub>📶W9 · W↑18d · ↓CMF26d</sub> | ✓ SAFE | Cancer treatment network, fertility clinics, diagnostic services | 📈 BULL_ANY_MID | 20 | ↑62 | ↑1.018 | ↑5d | — | +3.7% | 27.48/25.34 | +1.47% | 20% |
| [WESTLIFE](https://in.tradingview.com/chart/?symbol=NSE:WESTLIFE)<br><sub>📶W9 · W↑28d · ↑CMF1d</sub> | ✓ SAFE | McDonald's franchise operator West South India QSR | 📈 BULL_ANY_MID | 18 | ↑29 | ↓1.029 | ↑2d | — | +11.2% | 1.25/-2.83 | -2.31% | 20% |
| [TARSONS](https://in.tradingview.com/chart/?symbol=NSE:TARSONS)<br><sub>📶W9 · W↑28d · ↑CMF26d</sub> | ✓ SAFE | Plastic laboratory consumables and equipment manufacturer India | 📈 BULL_ANY_MID | 18 | ↑80 | ↓1.032 | ↑2d | — | +8.8% | 46.88/46.37 | -1.86% | 20% |
| [SPECTRUM](https://in.tradingview.com/chart/?symbol=NSE:SPECTRUM)<br><sub>📶W9 · W↑53d · ↑CMF12d</sub> | ✓ SAFE | Auto electrical components injection moulding ODM manufacturer | 📈 BULL_ANY_MID | 18 | ↑96 | ↓1.062 | ↑2d | — | +10.5% | 61.0/54.43 | +0.09% | 20% |
| [VERANDA](https://in.tradingview.com/chart/?symbol=NSE:VERANDA)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Hybrid EdTech platform competitive exam prep and professional courses | 📈 BULL_ANY_MID | 18 | ↑73 | ↓1.000 | ↓2d | — | +4.0% | -14.59/-17.36 | -1.84% | 20% |
| [RRKABEL](https://in.tradingview.com/chart/?symbol=NSE:RRKABEL)<br><sub>📶W9 · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Wires cables electrical distribution residential commercial industrial | 📈 BULL_ANY_MID | 17 | ↑96 | ↑1.038 | ↑3d | — | +6.1% | 23.06/15.08 | +3.71% | 20% |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL)<br><sub>📶W9 · W↑23d · ↑CMF23d</sub> | ✓ SAFE | Consumer electronics retail chain South India operations | 📈 BULL_ANY_MID | 17 | ↑70 | ↓1.002 | ↑3d | — | +2.1% | 27.02/26.9 | -1.46% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · W↑73d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 12 | ↑87 | ↓1.008 | ↑8d | — | +3.1% | 48.18/47.9 | -0.10% | 20% |
| [BALAMINES](https://in.tradingview.com/chart/?symbol=NSE:BALAMINES)<br><sub>📶W9 · W↑79d · ↑CMF9d</sub> | ✓ SAFE | Aliphatic amines, derivatives, specialty chemicals manufacturer | 📈 BULL_ANY_MID | 9 | ↑96 | ↓1.030 | ↑11d | — | +15.1% | 43.86/42.16 | +0.58% | 20% |
| [AEGISVOPAK](https://in.tradingview.com/chart/?symbol=NSE:AEGISVOPAK)<br><sub>📶W9 · W↑76d · ↑CMF28d</sub> | ✓ SAFE | LPG liquid storage terminals third party logistics operator | 📈 BULL_ANY_MID | 0 | ↑85 | ↑1.053 | ↑31d | — | +54.2% | 51.81/49.54 | +2.50% | 20% |
| [POLYPLEX](https://in.tradingview.com/chart/?symbol=NSE:POLYPLEX)<br><sub>📶W9 · W↑28d · ↑CMF1d</sub> | ✓ SAFE | BOPET polyester films flexible packaging industrial applications | 📈 BULL_ANY_MID | 0 | ↑73 | ↑1.044 | ↑28d | — | +24.1% | 60.85/60.14 | +4.02% | 20% |

```
NSE:PIDILITIND,NSE:EVEREADY,NSE:SHRIRAMFIN,NSE:PRIVISCL,NSE:CRAMC,NSE:MEDANTA,NSE:WAKEFIT,NSE:UFLEX,NSE:COSMOFIRST,NSE:DATAPATTNS,NSE:PNGJL,NSE:TVSHLTD,NSE:SEDEMAC,NSE:RGL,NSE:NEPHROPLUS,NSE:METROPOLIS,NSE:ENTERO,NSE:PNGSREVA,NSE:INDIQUBE,NSE:INDIGO,NSE:MEESHO,NSE:ZENTEC,NSE:SKFINDUS,NSE:NGLFINE,NSE:STEELCAS,NSE:MARICO,NSE:ARTEMISMED,NSE:AVALON,NSE:KERNEX,NSE:MANKIND,NSE:TVSMOTOR,NSE:ABCAPITAL,NSE:NESTLEIND,NSE:HCG,NSE:WESTLIFE,NSE:TARSONS,NSE:SPECTRUM,NSE:VERANDA,NSE:RRKABEL,NSE:EMIL,NSE:ADANIENT,NSE:BALAMINES,NSE:AEGISVOPAK,NSE:POLYPLEX
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (69)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · W↑68d · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄61 | ↑1.012 | ↑1d | SQ·PV | +2.0% | 3.64/3.38 | +1.99% | 20% |
| [EVEREADY](https://in.tradingview.com/chart/?symbol=NSE:EVEREADY)<br><sub>📶W9 · W↑71d · ↓CMF7d</sub> | ✓ SAFE | Dry cells batteries flashlights consumer household products | ⚡ BULL_ANY_PPV | 94 | 🔄58 | ↑1.028 | ↑1d | SQ·PV | +3.6% | -19.14/-23.82 | +3.61% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑26d · 🚀SS · ↓CMF12d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 92 | 🔄79 | ↑1.024 | ↑3d | SQ·PV | +3.9% | 17.16/12.64 | +2.75% | 20% |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL)<br><sub>📶W9 · W↑33d · ↑CMF29d</sub> | ✓ SAFE | Fragrance and flavor chemical manufacturer for personal care | ⚡ BULL_ANY_PPV | 90 | 🔄84 | ↑1.002 | ↑10d | SQ·PV | +3.6% | 41.39/39.46 | +0.05% | 20% |
| [CRAMC](https://in.tradingview.com/chart/?symbol=NSE:CRAMC)<br><sub>📶W9 · W↑27d · 🚀SS·88x · ↓CMF0d</sub> | ✓ SAFE | Mutual funds and investment advisory for Indian retail investors | ⚡ BULL_ANY_PPV | 89 | 🔄50 | ↑1.033 | ↑1d | SQ·PV | +5.5% | 37.47/31.51 | +5.47% | 20% |
| [MEDANTA](https://in.tradingview.com/chart/?symbol=NSE:MEDANTA)<br><sub>📶W9 · W↑71d · ↓CMF11d</sub> | ⚠ CAUTION | Multi-specialty tertiary hospitals, cardiology-focused, North-East India | ⚡ BULL_ANY_PPV | 67 | ↑67 | ↑1.014 | ↑3d | SQ·PV | +2.8% | 38.66/32.68 | +0.80% | 20% |
| [WAKEFIT](https://in.tradingview.com/chart/?symbol=NSE:WAKEFIT)<br><sub>📶W9 · 🚀SS·46x · ↑CMF9d</sub> | ✓ SAFE | Sleep mattresses furniture direct-to-consumer e-commerce home | ⚡ BULL_ANY_PPV | 49 | 🔄50 | ↑1.091 | ↑1d | PV | +13.2% | 39.67/35.28 | +13.22% | 20% |
| [UFLEX](https://in.tradingview.com/chart/?symbol=NSE:UFLEX)<br><sub>📶W9 · W↑71d · 🚀SS·283x · ↑CMF0d</sub> | ✓ SAFE | Flexible packaging films, laminates for food beverage | ⚡ BULL_ANY_PPV | 35 | 🔄55 | ↑1.095 | ↑15d | PV | +16.1% | 51.65/39.16 | +11.60% | 20% |
| [COSMOFIRST](https://in.tradingview.com/chart/?symbol=NSE:COSMOFIRST)<br><sub>📶W9 · W↑28d · ↑CMF0d</sub> | ✓ SAFE | Specialty films for packaging lamination labeling applications | ⚡ BULL_ANY_PPV | 30 | 🔄67 | ↑1.036 | ↑27d | PV | +18.3% | 45.67/41.65 | +4.36% | 20% |
| [DATAPATTNS](https://in.tradingview.com/chart/?symbol=NSE:DATAPATTNS)<br><sub>📶W9 · 🚀SS·11x · ↑CMF0d</sub> | ✓ SAFE | Defense aerospace electronics systems design manufacturing | ⚡ BULL_ANY_PPV | 19 | ↑93 | ↑1.107 | ↑1d | PV | +12.7% | -28.55/-39.45 | +12.70% | 20% |
| [PNGJL](https://in.tradingview.com/chart/?symbol=NSE:PNGJL)<br><sub>📶W9 · W↑13d · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | Gold jewelry retail with regional Maharashtra presence | ⚡ BULL_ANY_PPV | 5 | ↑44 | ↑1.066 | ↑15d | PV | +17.9% | 48.81/40.64 | +5.97% | 10% 🟩 |
| [TVSHLTD](https://in.tradingview.com/chart/?symbol=NSE:TVSHLTD)<br><sub>📶W9 · W↑18d · 🚀SS·17x · ↓CMF23d</sub> | ⚠ CAUTION | Aluminum die-castings automotive components manufacturing holding company | ⚡ BULL_ANY_PPV | 0 | ↑62 | ↑1.046 | ↑20d | PV | +11.1% | 49.07/36.63 | +4.29% | 20% |
| [SEDEMAC](https://in.tradingview.com/chart/?symbol=NSE:SEDEMAC)<br><sub>📶W9 · 🚀SS · ↓CMF19d</sub> | ✓ SAFE | Engine control units, mechatronics for automotive and off-highway | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.024 | ↑1d | SQ | +4.2% | -6.38/-9.39 | +4.22% | 20% |
| [RGL](https://in.tradingview.com/chart/?symbol=NSE:RGL)<br><sub>📶W9 · W↑28d · ↓CMF0d</sub> | ✓ SAFE | Global recruitment and staffing services provider | 📈 BULL_ANY_MID | 90 | 🔄56 | ↑1.005 | ↑10d | SQ | +4.0% | 38.24/37.91 | +0.32% | 20% |
| [NEPHROPLUS](https://in.tradingview.com/chart/?symbol=NSE:NEPHROPLUS)<br><sub>📶W9 · ↓CMF16d</sub> | ✓ SAFE | Dialysis treatment centers for kidney disease patients | 📈 BULL_ANY_MID | 89 | 🔄50 | ↑1.046 | ↑1d | SQ | +7.3% | -29.23/-35.58 | +7.35% | 20% |
| [METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS)<br><sub>📶W9 · W↑71d · ↓CMF25d</sub> | ⚠ CAUTION | Diagnostic pathology labs clinical testing centers urban India | 📈 BULL_ANY_MID | 67 | ↑74 | ↑1.009 | ↑3d | SQ | +4.5% | 44.7/44.48 | +0.23% | 20% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>📶W9 · W↑13d · ↑CMF7d</sub> | ⚠ CAUTION | Pharmaceutical surgical products distributor hospitals clinics retail | 📈 BULL_ANY_MID | 63 | ↑52 | ↑1.023 | ↑2d | SQ | +4.2% | 23.33/21.87 | +1.78% | 20% |
| [PNGSREVA](https://in.tradingview.com/chart/?symbol=NSE:PNGSREVA)<br><sub>📶W9 · ↓CMF24d</sub> | ✓ SAFE | Diamond jewellery retail, precious stones, Indian consumers | 📈 BULL_ANY_MID | 63 | ↑50 | ↑1.022 | ↑2d | SQ | +3.2% | 23.24/18.73 | +1.47% | 20% |
| [INDIQUBE](https://in.tradingview.com/chart/?symbol=NSE:INDIQUBE)<br><sub>📶W9 · W↑28d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 63 | ↑50 | ↑1.023 | ↑2d | SQ | +7.0% | 21.09/19.67 | +1.71% | 20% |
| [INDIGO](https://in.tradingview.com/chart/?symbol=NSE:INDIGO)<br><sub>📶W9 · W↑45d · 🚀SS · ↑CMF29d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄49 | ↑1.008 | ↑1d | — | +1.1% | 20.36/20.19 | +1.11% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · ↑CMF9d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers, rural consumers | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.005 | ↑2d | SQ | +2.2% | 16.26/14.13 | -1.01% | 20% 🟦 |
| [ZENTEC](https://in.tradingview.com/chart/?symbol=NSE:ZENTEC)<br><sub>📶W9 · ↓CMF5d</sub> | ✓ SAFE | Defense simulation systems and counter-drone solutions manufacturer | 📈 BULL_ANY_MID | 58 | ↑70 | ↓1.005 | ↓2d | SQ | +3.7% | -7.32/-7.9 | -0.22% | 20% |
| [SKFINDUS](https://in.tradingview.com/chart/?symbol=NSE:SKFINDUS)<br><sub>📶W9 · ↓CMF14d</sub> | ⚠ CAUTION | Rolling bearings seals lubrication industrial machinery | 📈 BULL_ANY_MID | 58 | ↑50 | ↓0.999 | ↓2d | SQ | +2.9% | -1.42/-2.25 | -2.84% | 20% |
| [NGLFINE](https://in.tradingview.com/chart/?symbol=NSE:NGLFINE)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Veterinary APIs, intermediates, animal health pharmaceuticals manufacturer | 📈 BULL_ANY_MID | 58 | ↑98 | ↓1.032 | ↑2d | SQ | +8.2% | 27.66/23.21 | +0.58% | 20% |
| [STEELCAS](https://in.tradingview.com/chart/?symbol=NSE:STEELCAS)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Steel castings manufacturer for heavy industrial equipment OEMs | 📈 BULL_ANY_MID | 58 | ↑81 | ↓1.003 | ↑2d | SQ | +0.5% | 14.8/14.37 | -0.08% | 20% |
| [MARICO](https://in.tradingview.com/chart/?symbol=NSE:MARICO)<br><sub>📶W9 · W↑17d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↑68 | ↓1.010 | ↑3d | SQ | +2.0% | 39.15/35.61 | +0.08% | 20% |
| [ARTEMISMED](https://in.tradingview.com/chart/?symbol=NSE:ARTEMISMED)<br><sub>📶W9 · W↑13d · ↑CMF1d</sub> | ✓ SAFE | Tertiary care hospital operator, multi-specialty, urban healthcare delivery | 📈 BULL_ANY_MID | 57 | ↑68 | ↓1.003 | ↑3d | SQ | +1.5% | 33.31/31.83 | -1.30% | 20% |
| [AVALON](https://in.tradingview.com/chart/?symbol=NSE:AVALON)<br><sub>📶W9 · ↓CMF14d</sub> | ✓ SAFE | Electronics manufacturing services for high-complexity defense telecom products | 📈 BULL_ANY_MID | 55 | ↑97 | ↓1.006 | ↓5d | SQ | +3.8% | 18.97/11.49 | +0.04% | 20% |
| [KERNEX](https://in.tradingview.com/chart/?symbol=NSE:KERNEX)<br><sub>📶W9 · ↑CMF3d</sub> | ✓ SAFE | Railway safety systems and software developer for trains | 📈 BULL_ANY_MID | 54 | 🔄97 | ↑1.021 | ↑1d | — | +3.0% | 10.17/9.92 | +3.01% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>📶W9 · W↑65d · ↓CMF6d</sub> | ✓ SAFE | Pharma formulations acute chronic diseases consumer health | 📈 BULL_ANY_MID | 51 | ↑63 | ↑1.009 | ↑19d | SQ | +7.4% | 47.69/43.74 | +0.35% | 20% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>📶W9 · W↑21d · ↓CMF9d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄61 | ↑1.043 | ↑1d | — | +5.7% | 34.69/30.07 | +5.68% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑69d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 46 | 🔄80 | ↑1.020 | ↑9d | — | +6.3% | 40.54/39.46 | +2.18% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑17d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 28 | ↑66 | ↑1.011 | ↑2d | — | +2.0% | 14.61/10.66 | +0.67% | 20% |
| [HCG](https://in.tradingview.com/chart/?symbol=NSE:HCG)<br><sub>📶W9 · W↑18d · ↓CMF26d</sub> | ✓ SAFE | Cancer treatment network, fertility clinics, diagnostic services | 📈 BULL_ANY_MID | 20 | ↑62 | ↑1.018 | ↑5d | — | +3.7% | 27.48/25.34 | +1.47% | 20% |
| [WESTLIFE](https://in.tradingview.com/chart/?symbol=NSE:WESTLIFE)<br><sub>📶W9 · W↑28d · ↑CMF1d</sub> | ✓ SAFE | McDonald's franchise operator West South India QSR | 📈 BULL_ANY_MID | 18 | ↑29 | ↓1.029 | ↑2d | — | +11.2% | 1.25/-2.83 | -2.31% | 20% |
| [TARSONS](https://in.tradingview.com/chart/?symbol=NSE:TARSONS)<br><sub>📶W9 · W↑28d · ↑CMF26d</sub> | ✓ SAFE | Plastic laboratory consumables and equipment manufacturer India | 📈 BULL_ANY_MID | 18 | ↑80 | ↓1.032 | ↑2d | — | +8.8% | 46.88/46.37 | -1.86% | 20% |
| [SPECTRUM](https://in.tradingview.com/chart/?symbol=NSE:SPECTRUM)<br><sub>📶W9 · W↑53d · ↑CMF12d</sub> | ✓ SAFE | Auto electrical components injection moulding ODM manufacturer | 📈 BULL_ANY_MID | 18 | ↑96 | ↓1.062 | ↑2d | — | +10.5% | 61.0/54.43 | +0.09% | 20% |
| [VERANDA](https://in.tradingview.com/chart/?symbol=NSE:VERANDA)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Hybrid EdTech platform competitive exam prep and professional courses | 📈 BULL_ANY_MID | 18 | ↑73 | ↓1.000 | ↓2d | — | +4.0% | -14.59/-17.36 | -1.84% | 20% |
| [RRKABEL](https://in.tradingview.com/chart/?symbol=NSE:RRKABEL)<br><sub>📶W9 · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Wires cables electrical distribution residential commercial industrial | 📈 BULL_ANY_MID | 17 | ↑96 | ↑1.038 | ↑3d | — | +6.1% | 23.06/15.08 | +3.71% | 20% |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL)<br><sub>📶W9 · W↑23d · ↑CMF23d</sub> | ✓ SAFE | Consumer electronics retail chain South India operations | 📈 BULL_ANY_MID | 17 | ↑70 | ↓1.002 | ↑3d | — | +2.1% | 27.02/26.9 | -1.46% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · W↑73d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 12 | ↑87 | ↓1.008 | ↑8d | — | +3.1% | 48.18/47.9 | -0.10% | 20% |
| [BALAMINES](https://in.tradingview.com/chart/?symbol=NSE:BALAMINES)<br><sub>📶W9 · W↑79d · ↑CMF9d</sub> | ✓ SAFE | Aliphatic amines, derivatives, specialty chemicals manufacturer | 📈 BULL_ANY_MID | 9 | ↑96 | ↓1.030 | ↑11d | — | +15.1% | 43.86/42.16 | +0.58% | 20% |
| [AEGISVOPAK](https://in.tradingview.com/chart/?symbol=NSE:AEGISVOPAK)<br><sub>📶W9 · W↑76d · ↑CMF28d</sub> | ✓ SAFE | LPG liquid storage terminals third party logistics operator | 📈 BULL_ANY_MID | 0 | ↑85 | ↑1.053 | ↑31d | — | +54.2% | 51.81/49.54 | +2.50% | 20% |
| [POLYPLEX](https://in.tradingview.com/chart/?symbol=NSE:POLYPLEX)<br><sub>📶W9 · W↑28d · ↑CMF1d</sub> | ✓ SAFE | BOPET polyester films flexible packaging industrial applications | 📈 BULL_ANY_MID | 0 | ↑73 | ↑1.044 | ↑28d | — | +24.1% | 60.85/60.14 | +4.02% | 20% |
| [TRUALT](https://in.tradingview.com/chart/?symbol=NSE:TRUALT)<br><sub>↓CMF14d · 🎯SLING</sub> | ✓ SAFE | Ethanol CBG biogas producer renewable energy sector | 🔥 BULL_OS_PPV | 35 | 🔄50 | ↑0.996 | ↓44d | PV | -7.6% | -59.46/-61.53 | +2.88% | 20% |
| [TARC](https://in.tradingview.com/chart/?symbol=NSE:TARC)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Luxury residential properties Delhi NCR metropolitan region | ⚡ BULL_ANY_PPV | 94 | 🔄8 | ↑1.018 | ↑1d | SQ·PV | +6.3% | -49.09/-52.57 | +6.33% | 20% |
| [GMRP&UI](https://in.tradingview.com/chart/?symbol=NSE:GMRP&UI)<br><sub>↓CMF30d</sub> | ✓ SAFE | Power generation, urban infrastructure, road-rail-port development | ⚡ BULL_ANY_PPV | 94 | 🔄30 | ↑1.022 | ↑1d | SQ·PV | +4.4% | -48.38/-52.46 | +4.41% | 20% |
| [ALICON](https://in.tradingview.com/chart/?symbol=NSE:ALICON)<br><sub>↓CMF30d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 94 | 🔄15 | ↑1.017 | ↑1d | SQ·PV | +3.4% | -40.1/-44.04 | +3.38% | 20% |
| [GULPOLY](https://in.tradingview.com/chart/?symbol=NSE:GULPOLY)<br><sub>RVOL92x · ↓CMF13d</sub> | ✓ SAFE | Polyol chemicals manufacturing for automotive foam applications | ⚡ BULL_ANY_PPV | 87 | 🔄72 | ↑1.012 | ↓13d | SQ·PV | -2.5% | -34.57/-44.05 | +3.37% | 20% |
| [BAJEL](https://in.tradingview.com/chart/?symbol=NSE:BAJEL)<br><sub>RVOL10x · ↓CMF30d</sub> | ✓ SAFE | EPC contractor civil infrastructure roads bridges projects | ⚡ BULL_ANY_PPV | 40 | 🔄41 | ↑1.010 | ↓45d | PV | +4.6% | -47.09/-49.26 | +4.24% | 20% |
| [PGHH](https://in.tradingview.com/chart/?symbol=NSE:PGHH)<br><sub>W↑3d · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Feminine hygiene pads, healthcare products, mass market | 🟡 BULL_OS_L2 | 94 | 🔄5 | ↑1.016 | ↑1d | SQ | +2.6% | -49.05/-56.92 | +2.61% | 20% |
| [MUTHOOTFIN](https://in.tradingview.com/chart/?symbol=NSE:MUTHOOTFIN)<br><sub>🚀SS · ↓CMF3d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄26 | ↑1.015 | ↑1d | SQ | +3.3% | -27.02/-29.52 | +3.27% | 20% |
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄40 | ↑1.012 | ↑1d | SQ | +2.4% | -40.58/-44.61 | +2.36% | 20% |
| [PETRONET](https://in.tradingview.com/chart/?symbol=NSE:PETRONET)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | LNG import regasification terminals serving Indian energy demand | 📈 BULL_ANY_MID | 99 | 🔄44 | ↑1.009 | ↑1d | SQ | +1.1% | -21.78/-26.65 | +1.08% | 20% |
| [ARFIN](https://in.tradingview.com/chart/?symbol=NSE:ARFIN)<br><sub>↓CMF6d</sub> | ✓ SAFE | Aluminium ferroalloys manufacturing trading steel auto sector | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.012 | ↑1d | SQ | +2.3% | -31.45/-34.8 | +2.32% | 20% 🟦 |
| [SHREDIGCEM](https://in.tradingview.com/chart/?symbol=NSE:SHREDIGCEM)<br><sub>↓CMF8d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄30 | ↑1.008 | ↑1d | SQ | +1.9% | -20.32/-21.91 | +1.86% | 20% |
| [KINGFA](https://in.tradingview.com/chart/?symbol=NSE:KINGFA)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Engineering plastics compounds for automotive consumer appliances | 📈 BULL_ANY_MID | 95 | 🔄70 | ↑1.000 | ↓5d | SQ | -0.1% | -18.0/-22.75 | +0.37% | 20% |
| [IGIL](https://in.tradingview.com/chart/?symbol=NSE:IGIL)<br><sub>↓CMF24d</sub> | ✓ SAFE | Diamond gemstone jewelry certification grading laboratory services | 📈 BULL_ANY_MID | 94 | 🔄47 | ↑1.003 | ↓6d | SQ | +1.4% | -33.23/-34.24 | +0.88% | 20% |
| [IMFA](https://in.tradingview.com/chart/?symbol=NSE:IMFA)<br><sub>↓CMF30d</sub> | ✓ SAFE | Ferrochrome producer for stainless steel manufacturing sector | 📈 BULL_ANY_MID | 88 | 🔄77 | ↓1.000 | ↑2d | SQ | +1.7% | -8.43/-9.37 | -0.31% | 20% |
| [BANARISUG](https://in.tradingview.com/chart/?symbol=NSE:BANARISUG)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 86 | 🔄36 | ↑0.999 | ↓9d | SQ | -0.1% | -20.55/-21.19 | +0.05% | 20% |
| [CLSEL](https://in.tradingview.com/chart/?symbol=NSE:CLSEL)<br><sub>↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 85 | 🔄50 | ↑1.008 | ↓15d | SQ | -1.4% | -49.44/-51.19 | +1.06% | 20% |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>🚀SS · ↓CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 68 | ↑67 | ↑1.010 | ↑2d | SQ | +1.9% | 4.33/1.26 | +0.83% | 20% |
| [HINDCOPPER](https://in.tradingview.com/chart/?symbol=NSE:HINDCOPPER)<br><sub>↓CMF30d</sub> | ✓ SAFE | Copper mining processing refining domestic industrial demand | 📈 BULL_ANY_MID | 58 | ↑74 | ↓0.999 | ↓2d | SQ | +1.5% | -41.2/-47.25 | -0.65% | 20% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>🚀SS · ↑CMF4d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄93 | ↑1.031 | ↑1d | — | +4.5% | -28.4/-34.25 | +4.45% | 20% |
| [ENRIN](https://in.tradingview.com/chart/?symbol=NSE:ENRIN)<br><sub>🚀SS · ↓CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 40 | 🔄72 | ↑1.009 | ↓21d | — | -1.4% | -25.75/-26.7 | +3.26% | 20% |
| [HONDAPOWER](https://in.tradingview.com/chart/?symbol=NSE:HONDAPOWER)<br><sub>↓CMF20d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 35 | 🔄20 | ↑0.999 | ↓23d | — | -3.1% | -46.58/-48.05 | +0.73% | 20% |
| [WONDERLA](https://in.tradingview.com/chart/?symbol=NSE:WONDERLA)<br><sub>↓CMF10d</sub> | ⚠ CAUTION | Theme parks and resort hospitality for leisure tourism | 📈 BULL_ANY_MID | 30 | 🔄15 | ↓0.996 | ↓29d | — | +1.3% | -29.91/-30.37 | -0.13% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>🚀SS · ↓CMF19d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 24 | ↑87 | ↑1.005 | ↓6d | — | +2.3% | -31.17/-34.4 | +0.16% | 20% |
| [VINDHYATEL](https://in.tradingview.com/chart/?symbol=NSE:VINDHYATEL)<br><sub>↓CMF20d · ⚠️TRAP</sub> | ✓ SAFE | Telecom cables manufacturing and EPC construction projects | 📈 BULL_ANY_MID | 0 | ↑88 | ↓0.995 | ↓29d | — | -4.4% | -42.65/-46.51 | -2.20% | 20% |

```
NSE:PIDILITIND,NSE:EVEREADY,NSE:SHRIRAMFIN,NSE:PRIVISCL,NSE:CRAMC,NSE:MEDANTA,NSE:WAKEFIT,NSE:UFLEX,NSE:COSMOFIRST,NSE:DATAPATTNS,NSE:PNGJL,NSE:TVSHLTD,NSE:SEDEMAC,NSE:RGL,NSE:NEPHROPLUS,NSE:METROPOLIS,NSE:ENTERO,NSE:PNGSREVA,NSE:INDIQUBE,NSE:INDIGO,NSE:MEESHO,NSE:ZENTEC,NSE:SKFINDUS,NSE:NGLFINE,NSE:STEELCAS,NSE:MARICO,NSE:ARTEMISMED,NSE:AVALON,NSE:KERNEX,NSE:MANKIND,NSE:TVSMOTOR,NSE:ABCAPITAL,NSE:NESTLEIND,NSE:HCG,NSE:WESTLIFE,NSE:TARSONS,NSE:SPECTRUM,NSE:VERANDA,NSE:RRKABEL,NSE:EMIL,NSE:ADANIENT,NSE:BALAMINES,NSE:AEGISVOPAK,NSE:POLYPLEX,NSE:TRUALT,NSE:TARC,NSE:GMRP&UI,NSE:ALICON,NSE:GULPOLY,NSE:BAJEL,NSE:PGHH,NSE:MUTHOOTFIN,NSE:HINDZINC,NSE:PETRONET,NSE:ARFIN,NSE:SHREDIGCEM,NSE:KINGFA,NSE:IGIL,NSE:IMFA,NSE:BANARISUG,NSE:CLSEL,NSE:GRASIM,NSE:HINDCOPPER,NSE:POWERINDIA,NSE:ENRIN,NSE:HONDAPOWER,NSE:WONDERLA,NSE:ADANIPOWER,NSE:VINDHYATEL
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (41)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · W↑68d · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄61 | ↑1.012 | ↑1d | SQ·PV | +2.0% | 3.64/3.38 | +1.99% | 20% |
| [EVEREADY](https://in.tradingview.com/chart/?symbol=NSE:EVEREADY)<br><sub>📶W9 · W↑71d · ↓CMF7d</sub> | ✓ SAFE | Dry cells batteries flashlights consumer household products | ⚡ BULL_ANY_PPV | 94 | 🔄58 | ↑1.028 | ↑1d | SQ·PV | +3.6% | -19.14/-23.82 | +3.61% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑26d · 🚀SS · ↓CMF12d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 92 | 🔄79 | ↑1.024 | ↑3d | SQ·PV | +3.9% | 17.16/12.64 | +2.75% | 20% |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL)<br><sub>📶W9 · W↑33d · ↑CMF29d</sub> | ✓ SAFE | Fragrance and flavor chemical manufacturer for personal care | ⚡ BULL_ANY_PPV | 90 | 🔄84 | ↑1.002 | ↑10d | SQ·PV | +3.6% | 41.39/39.46 | +0.05% | 20% |
| [CRAMC](https://in.tradingview.com/chart/?symbol=NSE:CRAMC)<br><sub>📶W9 · W↑27d · 🚀SS·88x · ↓CMF0d</sub> | ✓ SAFE | Mutual funds and investment advisory for Indian retail investors | ⚡ BULL_ANY_PPV | 89 | 🔄50 | ↑1.033 | ↑1d | SQ·PV | +5.5% | 37.47/31.51 | +5.47% | 20% |
| [MEDANTA](https://in.tradingview.com/chart/?symbol=NSE:MEDANTA)<br><sub>📶W9 · W↑71d · ↓CMF11d</sub> | ⚠ CAUTION | Multi-specialty tertiary hospitals, cardiology-focused, North-East India | ⚡ BULL_ANY_PPV | 67 | ↑67 | ↑1.014 | ↑3d | SQ·PV | +2.8% | 38.66/32.68 | +0.80% | 20% |
| [SEDEMAC](https://in.tradingview.com/chart/?symbol=NSE:SEDEMAC)<br><sub>📶W9 · 🚀SS · ↓CMF19d</sub> | ✓ SAFE | Engine control units, mechatronics for automotive and off-highway | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.024 | ↑1d | SQ | +4.2% | -6.38/-9.39 | +4.22% | 20% |
| [RGL](https://in.tradingview.com/chart/?symbol=NSE:RGL)<br><sub>📶W9 · W↑28d · ↓CMF0d</sub> | ✓ SAFE | Global recruitment and staffing services provider | 📈 BULL_ANY_MID | 90 | 🔄56 | ↑1.005 | ↑10d | SQ | +4.0% | 38.24/37.91 | +0.32% | 20% |
| [NEPHROPLUS](https://in.tradingview.com/chart/?symbol=NSE:NEPHROPLUS)<br><sub>📶W9 · ↓CMF16d</sub> | ✓ SAFE | Dialysis treatment centers for kidney disease patients | 📈 BULL_ANY_MID | 89 | 🔄50 | ↑1.046 | ↑1d | SQ | +7.3% | -29.23/-35.58 | +7.35% | 20% |
| [METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS)<br><sub>📶W9 · W↑71d · ↓CMF25d</sub> | ⚠ CAUTION | Diagnostic pathology labs clinical testing centers urban India | 📈 BULL_ANY_MID | 67 | ↑74 | ↑1.009 | ↑3d | SQ | +4.5% | 44.7/44.48 | +0.23% | 20% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>📶W9 · W↑13d · ↑CMF7d</sub> | ⚠ CAUTION | Pharmaceutical surgical products distributor hospitals clinics retail | 📈 BULL_ANY_MID | 63 | ↑52 | ↑1.023 | ↑2d | SQ | +4.2% | 23.33/21.87 | +1.78% | 20% |
| [PNGSREVA](https://in.tradingview.com/chart/?symbol=NSE:PNGSREVA)<br><sub>📶W9 · ↓CMF24d</sub> | ✓ SAFE | Diamond jewellery retail, precious stones, Indian consumers | 📈 BULL_ANY_MID | 63 | ↑50 | ↑1.022 | ↑2d | SQ | +3.2% | 23.24/18.73 | +1.47% | 20% |
| [INDIQUBE](https://in.tradingview.com/chart/?symbol=NSE:INDIQUBE)<br><sub>📶W9 · W↑28d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 63 | ↑50 | ↑1.023 | ↑2d | SQ | +7.0% | 21.09/19.67 | +1.71% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · ↑CMF9d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers, rural consumers | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.005 | ↑2d | SQ | +2.2% | 16.26/14.13 | -1.01% | 20% 🟦 |
| [ZENTEC](https://in.tradingview.com/chart/?symbol=NSE:ZENTEC)<br><sub>📶W9 · ↓CMF5d</sub> | ✓ SAFE | Defense simulation systems and counter-drone solutions manufacturer | 📈 BULL_ANY_MID | 58 | ↑70 | ↓1.005 | ↓2d | SQ | +3.7% | -7.32/-7.9 | -0.22% | 20% |
| [SKFINDUS](https://in.tradingview.com/chart/?symbol=NSE:SKFINDUS)<br><sub>📶W9 · ↓CMF14d</sub> | ⚠ CAUTION | Rolling bearings seals lubrication industrial machinery | 📈 BULL_ANY_MID | 58 | ↑50 | ↓0.999 | ↓2d | SQ | +2.9% | -1.42/-2.25 | -2.84% | 20% |
| [NGLFINE](https://in.tradingview.com/chart/?symbol=NSE:NGLFINE)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Veterinary APIs, intermediates, animal health pharmaceuticals manufacturer | 📈 BULL_ANY_MID | 58 | ↑98 | ↓1.032 | ↑2d | SQ | +8.2% | 27.66/23.21 | +0.58% | 20% |
| [STEELCAS](https://in.tradingview.com/chart/?symbol=NSE:STEELCAS)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Steel castings manufacturer for heavy industrial equipment OEMs | 📈 BULL_ANY_MID | 58 | ↑81 | ↓1.003 | ↑2d | SQ | +0.5% | 14.8/14.37 | -0.08% | 20% |
| [MARICO](https://in.tradingview.com/chart/?symbol=NSE:MARICO)<br><sub>📶W9 · W↑17d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↑68 | ↓1.010 | ↑3d | SQ | +2.0% | 39.15/35.61 | +0.08% | 20% |
| [ARTEMISMED](https://in.tradingview.com/chart/?symbol=NSE:ARTEMISMED)<br><sub>📶W9 · W↑13d · ↑CMF1d</sub> | ✓ SAFE | Tertiary care hospital operator, multi-specialty, urban healthcare delivery | 📈 BULL_ANY_MID | 57 | ↑68 | ↓1.003 | ↑3d | SQ | +1.5% | 33.31/31.83 | -1.30% | 20% |
| [AVALON](https://in.tradingview.com/chart/?symbol=NSE:AVALON)<br><sub>📶W9 · ↓CMF14d</sub> | ✓ SAFE | Electronics manufacturing services for high-complexity defense telecom products | 📈 BULL_ANY_MID | 55 | ↑97 | ↓1.006 | ↓5d | SQ | +3.8% | 18.97/11.49 | +0.04% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>📶W9 · W↑65d · ↓CMF6d</sub> | ✓ SAFE | Pharma formulations acute chronic diseases consumer health | 📈 BULL_ANY_MID | 51 | ↑63 | ↑1.009 | ↑19d | SQ | +7.4% | 47.69/43.74 | +0.35% | 20% |
| [TARC](https://in.tradingview.com/chart/?symbol=NSE:TARC)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Luxury residential properties Delhi NCR metropolitan region | ⚡ BULL_ANY_PPV | 94 | 🔄8 | ↑1.018 | ↑1d | SQ·PV | +6.3% | -49.09/-52.57 | +6.33% | 20% |
| [GMRP&UI](https://in.tradingview.com/chart/?symbol=NSE:GMRP&UI)<br><sub>↓CMF30d</sub> | ✓ SAFE | Power generation, urban infrastructure, road-rail-port development | ⚡ BULL_ANY_PPV | 94 | 🔄30 | ↑1.022 | ↑1d | SQ·PV | +4.4% | -48.38/-52.46 | +4.41% | 20% |
| [ALICON](https://in.tradingview.com/chart/?symbol=NSE:ALICON)<br><sub>↓CMF30d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 94 | 🔄15 | ↑1.017 | ↑1d | SQ·PV | +3.4% | -40.1/-44.04 | +3.38% | 20% |
| [GULPOLY](https://in.tradingview.com/chart/?symbol=NSE:GULPOLY)<br><sub>RVOL92x · ↓CMF13d</sub> | ✓ SAFE | Polyol chemicals manufacturing for automotive foam applications | ⚡ BULL_ANY_PPV | 87 | 🔄72 | ↑1.012 | ↓13d | SQ·PV | -2.5% | -34.57/-44.05 | +3.37% | 20% |
| [PGHH](https://in.tradingview.com/chart/?symbol=NSE:PGHH)<br><sub>W↑3d · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Feminine hygiene pads, healthcare products, mass market | 🟡 BULL_OS_L2 | 94 | 🔄5 | ↑1.016 | ↑1d | SQ | +2.6% | -49.05/-56.92 | +2.61% | 20% |
| [MUTHOOTFIN](https://in.tradingview.com/chart/?symbol=NSE:MUTHOOTFIN)<br><sub>🚀SS · ↓CMF3d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄26 | ↑1.015 | ↑1d | SQ | +3.3% | -27.02/-29.52 | +3.27% | 20% |
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄40 | ↑1.012 | ↑1d | SQ | +2.4% | -40.58/-44.61 | +2.36% | 20% |
| [PETRONET](https://in.tradingview.com/chart/?symbol=NSE:PETRONET)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | LNG import regasification terminals serving Indian energy demand | 📈 BULL_ANY_MID | 99 | 🔄44 | ↑1.009 | ↑1d | SQ | +1.1% | -21.78/-26.65 | +1.08% | 20% |
| [ARFIN](https://in.tradingview.com/chart/?symbol=NSE:ARFIN)<br><sub>↓CMF6d</sub> | ✓ SAFE | Aluminium ferroalloys manufacturing trading steel auto sector | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.012 | ↑1d | SQ | +2.3% | -31.45/-34.8 | +2.32% | 20% 🟦 |
| [SHREDIGCEM](https://in.tradingview.com/chart/?symbol=NSE:SHREDIGCEM)<br><sub>↓CMF8d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄30 | ↑1.008 | ↑1d | SQ | +1.9% | -20.32/-21.91 | +1.86% | 20% |
| [KINGFA](https://in.tradingview.com/chart/?symbol=NSE:KINGFA)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Engineering plastics compounds for automotive consumer appliances | 📈 BULL_ANY_MID | 95 | 🔄70 | ↑1.000 | ↓5d | SQ | -0.1% | -18.0/-22.75 | +0.37% | 20% |
| [IGIL](https://in.tradingview.com/chart/?symbol=NSE:IGIL)<br><sub>↓CMF24d</sub> | ✓ SAFE | Diamond gemstone jewelry certification grading laboratory services | 📈 BULL_ANY_MID | 94 | 🔄47 | ↑1.003 | ↓6d | SQ | +1.4% | -33.23/-34.24 | +0.88% | 20% |
| [IMFA](https://in.tradingview.com/chart/?symbol=NSE:IMFA)<br><sub>↓CMF30d</sub> | ✓ SAFE | Ferrochrome producer for stainless steel manufacturing sector | 📈 BULL_ANY_MID | 88 | 🔄77 | ↓1.000 | ↑2d | SQ | +1.7% | -8.43/-9.37 | -0.31% | 20% |
| [BANARISUG](https://in.tradingview.com/chart/?symbol=NSE:BANARISUG)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 86 | 🔄36 | ↑0.999 | ↓9d | SQ | -0.1% | -20.55/-21.19 | +0.05% | 20% |
| [CLSEL](https://in.tradingview.com/chart/?symbol=NSE:CLSEL)<br><sub>↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 85 | 🔄50 | ↑1.008 | ↓15d | SQ | -1.4% | -49.44/-51.19 | +1.06% | 20% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>W↑68d · ↓CMF12d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 68 | ↓51 | ↑1.005 | ↑2d | SQ | +1.3% | 0.89/-3.8 | +0.23% | 20% |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>🚀SS · ↓CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 68 | ↑67 | ↑1.010 | ↑2d | SQ | +1.9% | 4.33/1.26 | +0.83% | 20% |
| [HINDCOPPER](https://in.tradingview.com/chart/?symbol=NSE:HINDCOPPER)<br><sub>↓CMF30d</sub> | ✓ SAFE | Copper mining processing refining domestic industrial demand | 📈 BULL_ANY_MID | 58 | ↑74 | ↓0.999 | ↓2d | SQ | +1.5% | -41.2/-47.25 | -0.65% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>↓CMF20d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↓44 | ↑1.000 | ↓8d | SQ | -0.3% | -49.16/-51.32 | +0.48% | 20% |

```
NSE:PIDILITIND,NSE:EVEREADY,NSE:SHRIRAMFIN,NSE:PRIVISCL,NSE:CRAMC,NSE:MEDANTA,NSE:SEDEMAC,NSE:RGL,NSE:NEPHROPLUS,NSE:METROPOLIS,NSE:ENTERO,NSE:PNGSREVA,NSE:INDIQUBE,NSE:MEESHO,NSE:ZENTEC,NSE:SKFINDUS,NSE:NGLFINE,NSE:STEELCAS,NSE:MARICO,NSE:ARTEMISMED,NSE:AVALON,NSE:MANKIND,NSE:TARC,NSE:GMRP&UI,NSE:ALICON,NSE:GULPOLY,NSE:PGHH,NSE:MUTHOOTFIN,NSE:HINDZINC,NSE:PETRONET,NSE:ARFIN,NSE:SHREDIGCEM,NSE:KINGFA,NSE:IGIL,NSE:IMFA,NSE:BANARISUG,NSE:CLSEL,NSE:GAIL,NSE:GRASIM,NSE:HINDCOPPER,NSE:TATASTEEL
```

---

### 🔥 MAJOR — PPV confirmed (8)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [WAKEFIT](https://in.tradingview.com/chart/?symbol=NSE:WAKEFIT)<br><sub>📶W9 · 🚀SS·46x · ↑CMF9d</sub> | ✓ SAFE | Sleep mattresses furniture direct-to-consumer e-commerce home | ⚡ BULL_ANY_PPV | 49 | 🔄50 | ↑1.091 | ↑1d | PV | +13.2% | 39.67/35.28 | +13.22% | 20% |
| [UFLEX](https://in.tradingview.com/chart/?symbol=NSE:UFLEX)<br><sub>📶W9 · W↑71d · 🚀SS·283x · ↑CMF0d</sub> | ✓ SAFE | Flexible packaging films, laminates for food beverage | ⚡ BULL_ANY_PPV | 35 | 🔄55 | ↑1.095 | ↑15d | PV | +16.1% | 51.65/39.16 | +11.60% | 20% |
| [COSMOFIRST](https://in.tradingview.com/chart/?symbol=NSE:COSMOFIRST)<br><sub>📶W9 · W↑28d · ↑CMF0d</sub> | ✓ SAFE | Specialty films for packaging lamination labeling applications | ⚡ BULL_ANY_PPV | 30 | 🔄67 | ↑1.036 | ↑27d | PV | +18.3% | 45.67/41.65 | +4.36% | 20% |
| [DATAPATTNS](https://in.tradingview.com/chart/?symbol=NSE:DATAPATTNS)<br><sub>📶W9 · 🚀SS·11x · ↑CMF0d</sub> | ✓ SAFE | Defense aerospace electronics systems design manufacturing | ⚡ BULL_ANY_PPV | 19 | ↑93 | ↑1.107 | ↑1d | PV | +12.7% | -28.55/-39.45 | +12.70% | 20% |
| [PNGJL](https://in.tradingview.com/chart/?symbol=NSE:PNGJL)<br><sub>📶W9 · W↑13d · 🚀SS · ↓CMF9d</sub> | ✓ SAFE | Gold jewelry retail with regional Maharashtra presence | ⚡ BULL_ANY_PPV | 5 | ↑44 | ↑1.066 | ↑15d | PV | +17.9% | 48.81/40.64 | +5.97% | 10% 🟩 |
| [TVSHLTD](https://in.tradingview.com/chart/?symbol=NSE:TVSHLTD)<br><sub>📶W9 · W↑18d · 🚀SS·17x · ↓CMF23d</sub> | ⚠ CAUTION | Aluminum die-castings automotive components manufacturing holding company | ⚡ BULL_ANY_PPV | 0 | ↑62 | ↑1.046 | ↑20d | PV | +11.1% | 49.07/36.63 | +4.29% | 20% |
| [TRUALT](https://in.tradingview.com/chart/?symbol=NSE:TRUALT)<br><sub>↓CMF14d · 🎯SLING</sub> | ✓ SAFE | Ethanol CBG biogas producer renewable energy sector | 🔥 BULL_OS_PPV | 35 | 🔄50 | ↑0.996 | ↓44d | PV | -7.6% | -59.46/-61.53 | +2.88% | 20% |
| [BAJEL](https://in.tradingview.com/chart/?symbol=NSE:BAJEL)<br><sub>RVOL10x · ↓CMF30d</sub> | ✓ SAFE | EPC contractor civil infrastructure roads bridges projects | ⚡ BULL_ANY_PPV | 40 | 🔄41 | ↑1.010 | ↓45d | PV | +4.6% | -47.09/-49.26 | +4.24% | 20% |

```
NSE:WAKEFIT,NSE:UFLEX,NSE:COSMOFIRST,NSE:DATAPATTNS,NSE:PNGJL,NSE:TVSHLTD,NSE:TRUALT,NSE:BAJEL
```

### 🟢 OVERSOLD — reversal from −53/−60 (4)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PATANJALI](https://in.tradingview.com/chart/?symbol=NSE:PATANJALI)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Edible oils, soybean processing, consumer packaged goods | 🟢 BULL_OVERSOLD | 16 | ↓1 | ↑0.929 | ↓9d | — | -18.5% | -84.86/-86.02 | -1.20% | 20% |
| [GPIL](https://in.tradingview.com/chart/?symbol=NSE:GPIL)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Steel and iron ore pellets, integrated mining to finished products | 🟢 BULL_OVERSOLD | 0 | ↓42 | ↓0.978 | ↓46d | — | -16.4% | -62.66/-63.38 | -1.34% | 20% |
| [NTPC](https://in.tradingview.com/chart/?symbol=NSE:NTPC)<br><sub>↓CMF4d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 29 | ↓35 | ↑1.003 | ↑1d | — | +0.5% | -51.44/-55.81 | +0.45% | 20% |
| [VMM](https://in.tradingview.com/chart/?symbol=NSE:VMM)<br><sub>↓CMF19d · ⚠️TRAP</sub> | ✓ SAFE | Budget hypermarket chain selling apparel groceries electronics home goods | 🟡 BULL_OS_L2 | 11 | ↓16 | ↓0.986 | ↓9d | — | -4.0% | -54.62/-54.78 | -1.34% | 20% |

```
NSE:PATANJALI,NSE:GPIL,NSE:NTPC,NSE:VMM
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (26)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [INDIGO](https://in.tradingview.com/chart/?symbol=NSE:INDIGO)<br><sub>📶W9 · W↑45d · 🚀SS · ↑CMF29d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄49 | ↑1.008 | ↑1d | — | +1.1% | 20.36/20.19 | +1.11% | 20% |
| [KERNEX](https://in.tradingview.com/chart/?symbol=NSE:KERNEX)<br><sub>📶W9 · ↑CMF3d</sub> | ✓ SAFE | Railway safety systems and software developer for trains | 📈 BULL_ANY_MID | 54 | 🔄97 | ↑1.021 | ↑1d | — | +3.0% | 10.17/9.92 | +3.01% | 20% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>📶W9 · W↑21d · ↓CMF9d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄61 | ↑1.043 | ↑1d | — | +5.7% | 34.69/30.07 | +5.68% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑69d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 46 | 🔄80 | ↑1.020 | ↑9d | — | +6.3% | 40.54/39.46 | +2.18% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑17d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 28 | ↑66 | ↑1.011 | ↑2d | — | +2.0% | 14.61/10.66 | +0.67% | 20% |
| [HCG](https://in.tradingview.com/chart/?symbol=NSE:HCG)<br><sub>📶W9 · W↑18d · ↓CMF26d</sub> | ✓ SAFE | Cancer treatment network, fertility clinics, diagnostic services | 📈 BULL_ANY_MID | 20 | ↑62 | ↑1.018 | ↑5d | — | +3.7% | 27.48/25.34 | +1.47% | 20% |
| [WESTLIFE](https://in.tradingview.com/chart/?symbol=NSE:WESTLIFE)<br><sub>📶W9 · W↑28d · ↑CMF1d</sub> | ✓ SAFE | McDonald's franchise operator West South India QSR | 📈 BULL_ANY_MID | 18 | ↑29 | ↓1.029 | ↑2d | — | +11.2% | 1.25/-2.83 | -2.31% | 20% |
| [TARSONS](https://in.tradingview.com/chart/?symbol=NSE:TARSONS)<br><sub>📶W9 · W↑28d · ↑CMF26d</sub> | ✓ SAFE | Plastic laboratory consumables and equipment manufacturer India | 📈 BULL_ANY_MID | 18 | ↑80 | ↓1.032 | ↑2d | — | +8.8% | 46.88/46.37 | -1.86% | 20% |
| [SPECTRUM](https://in.tradingview.com/chart/?symbol=NSE:SPECTRUM)<br><sub>📶W9 · W↑53d · ↑CMF12d</sub> | ✓ SAFE | Auto electrical components injection moulding ODM manufacturer | 📈 BULL_ANY_MID | 18 | ↑96 | ↓1.062 | ↑2d | — | +10.5% | 61.0/54.43 | +0.09% | 20% |
| [VERANDA](https://in.tradingview.com/chart/?symbol=NSE:VERANDA)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Hybrid EdTech platform competitive exam prep and professional courses | 📈 BULL_ANY_MID | 18 | ↑73 | ↓1.000 | ↓2d | — | +4.0% | -14.59/-17.36 | -1.84% | 20% |
| [RRKABEL](https://in.tradingview.com/chart/?symbol=NSE:RRKABEL)<br><sub>📶W9 · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Wires cables electrical distribution residential commercial industrial | 📈 BULL_ANY_MID | 17 | ↑96 | ↑1.038 | ↑3d | — | +6.1% | 23.06/15.08 | +3.71% | 20% |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL)<br><sub>📶W9 · W↑23d · ↑CMF23d</sub> | ✓ SAFE | Consumer electronics retail chain South India operations | 📈 BULL_ANY_MID | 17 | ↑70 | ↓1.002 | ↑3d | — | +2.1% | 27.02/26.9 | -1.46% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · W↑73d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 12 | ↑87 | ↓1.008 | ↑8d | — | +3.1% | 48.18/47.9 | -0.10% | 20% |
| [BALAMINES](https://in.tradingview.com/chart/?symbol=NSE:BALAMINES)<br><sub>📶W9 · W↑79d · ↑CMF9d</sub> | ✓ SAFE | Aliphatic amines, derivatives, specialty chemicals manufacturer | 📈 BULL_ANY_MID | 9 | ↑96 | ↓1.030 | ↑11d | — | +15.1% | 43.86/42.16 | +0.58% | 20% |
| [AEGISVOPAK](https://in.tradingview.com/chart/?symbol=NSE:AEGISVOPAK)<br><sub>📶W9 · W↑76d · ↑CMF28d</sub> | ✓ SAFE | LPG liquid storage terminals third party logistics operator | 📈 BULL_ANY_MID | 0 | ↑85 | ↑1.053 | ↑31d | — | +54.2% | 51.81/49.54 | +2.50% | 20% |
| [POLYPLEX](https://in.tradingview.com/chart/?symbol=NSE:POLYPLEX)<br><sub>📶W9 · W↑28d · ↑CMF1d</sub> | ✓ SAFE | BOPET polyester films flexible packaging industrial applications | 📈 BULL_ANY_MID | 0 | ↑73 | ↑1.044 | ↑28d | — | +24.1% | 60.85/60.14 | +4.02% | 20% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>🚀SS · ↑CMF4d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄93 | ↑1.031 | ↑1d | — | +4.5% | -28.4/-34.25 | +4.45% | 20% |
| [ENRIN](https://in.tradingview.com/chart/?symbol=NSE:ENRIN)<br><sub>🚀SS · ↓CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 40 | 🔄72 | ↑1.009 | ↓21d | — | -1.4% | -25.75/-26.7 | +3.26% | 20% |
| [HONDAPOWER](https://in.tradingview.com/chart/?symbol=NSE:HONDAPOWER)<br><sub>↓CMF20d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 35 | 🔄20 | ↑0.999 | ↓23d | — | -3.1% | -46.58/-48.05 | +0.73% | 20% |
| [WONDERLA](https://in.tradingview.com/chart/?symbol=NSE:WONDERLA)<br><sub>↓CMF10d</sub> | ⚠ CAUTION | Theme parks and resort hospitality for leisure tourism | 📈 BULL_ANY_MID | 30 | 🔄15 | ↓0.996 | ↓29d | — | +1.3% | -29.91/-30.37 | -0.13% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>🚀SS · ↓CMF19d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 24 | ↑87 | ↑1.005 | ↓6d | — | +2.3% | -31.17/-34.4 | +0.16% | 20% |
| [GRSE](https://in.tradingview.com/chart/?symbol=NSE:GRSE)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Naval warship construction and submarine building | 📈 BULL_ANY_MID | 4 | ↓40 | ↓0.990 | ↓16d | — | -3.4% | -40.4/-41.25 | -1.18% | 20% |
| [PFOCUS](https://in.tradingview.com/chart/?symbol=NSE:PFOCUS)<br><sub>↓CMF14d · ⚠️TRAP</sub> | ✓ SAFE | VFX animation post-production services for entertainment | 📈 BULL_ANY_MID | 2 | ↓95 | ↓0.973 | ↓18d | — | -13.1% | -43.83/-43.88 | -1.41% | 5% |
| [SAIL](https://in.tradingview.com/chart/?symbol=NSE:SAIL)<br><sub>↓CMF27d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE | Integrated steel producer, automotive and construction sectors | 📈 BULL_ANY_MID | 0 | ↓59 | ↓0.984 | ↓51d | — | -8.0% | -48.98/-49.2 | -1.27% | 20% |
| [TIINDIA](https://in.tradingview.com/chart/?symbol=NSE:TIINDIA)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Bicycles, tubes, automotive components, industrial applications | 📈 BULL_ANY_MID | 0 | ↓47 | ↓0.992 | ↓29d | — | -2.4% | -38.35/-38.93 | -0.19% | 20% |
| [VINDHYATEL](https://in.tradingview.com/chart/?symbol=NSE:VINDHYATEL)<br><sub>↓CMF20d · ⚠️TRAP</sub> | ✓ SAFE | Telecom cables manufacturing and EPC construction projects | 📈 BULL_ANY_MID | 0 | ↑88 | ↓0.995 | ↓29d | — | -4.4% | -42.65/-46.51 | -2.20% | 20% |

```
NSE:INDIGO,NSE:KERNEX,NSE:TVSMOTOR,NSE:ABCAPITAL,NSE:NESTLEIND,NSE:HCG,NSE:WESTLIFE,NSE:TARSONS,NSE:SPECTRUM,NSE:VERANDA,NSE:RRKABEL,NSE:EMIL,NSE:ADANIENT,NSE:BALAMINES,NSE:AEGISVOPAK,NSE:POLYPLEX,NSE:POWERINDIA,NSE:ENRIN,NSE:HONDAPOWER,NSE:WONDERLA,NSE:ADANIPOWER,NSE:GRSE,NSE:PFOCUS,NSE:SAIL,NSE:TIINDIA,NSE:VINDHYATEL
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
