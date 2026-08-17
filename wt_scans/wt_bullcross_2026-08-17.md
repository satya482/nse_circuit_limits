> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-08-17
*Generated 2026-08-17 17:40 IST*

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

**Total bull crosses today: 81** · 27 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:COHANCE,NSE:JYOTHYLAB,NSE:GRPLTD,NSE:EXPLEOSOL,NSE:RISHABH,NSE:BALRAMCHIN,NSE:UFLEX,NSE:KFINTECH,NSE:COSMOFIRST,NSE:RUBICON,NSE:PTCIL,NSE:SMCGLOBAL,NSE:HARSHA,NSE:AURUM,NSE:INOXINDIA,NSE:DIXON,NSE:RGL,NSE:SAMBHV,NSE:CARTRADE,NSE:APOLLOPIPE,NSE:UDS,NSE:CYIENTDLM,NSE:AFFLE,NSE:BHAGCHEM,NSE:MONARCH,NSE:INDIGO,NSE:DYNAMATECH,NSE:GAEL,NSE:JYOTICNC,NSE:ESCORTS,NSE:POLYPLEX,NSE:ROSSTECH,NSE:SEAMECLTD,NSE:BIL,NSE:SANSERA,NSE:KDDL,NSE:LENSKART,NSE:TBOTEK,NSE:HAVELLS,NSE:BRIGHOTEL,NSE:SPMLINFRA,NSE:ALEMBICLTD,NSE:MASFIN,NSE:TRIVENI,NSE:ASALCBR,NSE:PNBGILTS,NSE:CEINSYS,NSE:AWHCL,NSE:SHANTIGEAR,NSE:GOKEX,NSE:MBEL,NSE:RELIGARE,NSE:AVANTIFEED,NSE:VTL,NSE:EMAMILTD,NSE:BALMLAWRIE,NSE:NTPC,NSE:MRF,NSE:NIITLTD,NSE:INOXWIND,NSE:BFINVEST,NSE:AMBER,NSE:CAPACITE,NSE:APOLLO,NSE:HAWKINCOOK,NSE:PSPPROJECT,NSE:ADANIPORTS,NSE:PHOENIXLTD,NSE:EMMVEE,NSE:GANECOS,NSE:GREENPLY,NSE:KALAMANDIR,NSE:PATANJALI,NSE:MHRIL,NSE:JSWHL,NSE:INTERARCH,NSE:GRAUWEIL,NSE:HINDUNILVR,NSE:SATIN,NSE:SRF,NSE:JLHL
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (39)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [COHANCE](https://in.tradingview.com/chart/?symbol=NSE:COHANCE)<br><sub>📶W9 · W↑6d · ↓CMF19d</sub> | ✓ SAFE | Pharmaceutical contract manufacturing development across drug lifecycle | ⚡ BULL_ANY_PPV | 92 | 🔄28 | ↑1.006 | ↑8d | SQ·PV | +3.6% | 18.44/18.03 | +0.93% | 20% |
| [JYOTHYLAB](https://in.tradingview.com/chart/?symbol=NSE:JYOTHYLAB)<br><sub>📶W9 · W↑26d · ↑CMF3d</sub> | ✓ SAFE | Home care and personal care products for Indian households | ⚡ BULL_ANY_PPV | 89 | 🔄14 | ↑1.047 | ↑1d | SQ·PV | +7.3% | 11.65/9.7 | +7.31% | 20% |
| [GRPLTD](https://in.tradingview.com/chart/?symbol=NSE:GRPLTD)<br><sub>📶W9 · W↑41d · ↓CMF10d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 62 | ↑63 | ↑1.024 | ↑3d | SQ·PV | +3.7% | 22.14/17.39 | +1.98% | 20% |
| [EXPLEOSOL](https://in.tradingview.com/chart/?symbol=NSE:EXPLEOSOL)<br><sub>📶W9 · W↑16d · 🚀SS·48x · ↑CMF0d</sub> | ✓ SAFE | Software testing QA services banking financial sector | ⚡ BULL_ANY_PPV | 49 | 🔄28 | ↑1.097 | ↑1d | PV | +13.1% | 14.35/1.19 | +13.13% | 20% |
| [RISHABH](https://in.tradingview.com/chart/?symbol=NSE:RISHABH)<br><sub>📶W9 · W↑1d · ↑CMF0d</sub> | ✓ SAFE | Electrical meters, automation instruments, industrial manufacturing | ⚡ BULL_ANY_PPV | 49 | 🔄95 | ↑1.051 | ↑1d | PV | +7.1% | 32.36/30.87 | +7.08% | 20% |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>📶W9 · W↑36d · 🚀SS · ↑CMF10d</sub> | ✓ SAFE | Sugar manufacturing, distillery, power cogeneration for domestic consumption | ⚡ BULL_ANY_PPV | 48 | 🔄79 | ↑1.041 | ↑2d | PV | +5.8% | 36.2/33.88 | +4.95% | 20% |
| [UFLEX](https://in.tradingview.com/chart/?symbol=NSE:UFLEX)<br><sub>📶W9 · W↑89d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Flexible packaging films, laminates for food beverage | ⚡ BULL_ANY_PPV | 30 | 🔄77 | ↑1.160 | ↑33d | PV | +38.7% | 74.07/64.29 | +19.99% | 20% |
| [KFINTECH](https://in.tradingview.com/chart/?symbol=NSE:KFINTECH)<br><sub>📶W9 · W↑56d · ↑CMF15d</sub> | ✓ SAFE | Registrar transfer agent digital services capital markets | ⚡ BULL_ANY_PPV | 17 | ↑47 | ↑1.035 | ↑3d | PV | +5.5% | 25.39/17.14 | +3.51% | 20% |
| [COSMOFIRST](https://in.tradingview.com/chart/?symbol=NSE:COSMOFIRST)<br><sub>📶W9 · W↑89d · 🚀SS · ↓CMF11d</sub> | ✓ SAFE | Specialty films for packaging, lamination, labeling applications | ⚡ BULL_ANY_PPV | 13 | ↑68 | ↑1.047 | ↑7d | PV | +10.7% | 62.92/58.76 | +2.82% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · W↑1d · 🚀SS·14x · ↑CMF30d</sub> | ✓ SAFE | Complex generic formulations manufacturing specialty pharmaceuticals | ⚡ BULL_ANY_PPV | 11 | ↑50 | ↑1.104 | ↑9d | PV | +20.6% | 71.94/67.96 | +11.09% | 20% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>📶W9 · W↑26d · 🚀SS·18x · ↑CMF6d</sub> | ✓ SAFE | Precision metal castings aerospace defense oil gas marine | ⚡ BULL_ANY_PPV | 9 | ↑79 | ↑1.079 | ↑11d | PV | +16.1% | 75.87/71.27 | +8.05% | 20% |
| [SMCGLOBAL](https://in.tradingview.com/chart/?symbol=NSE:SMCGLOBAL)<br><sub>📶W9 · W↑51d · ↑CMF30d</sub> | ✓ SAFE | Stock brokerage, derivatives trading, insurance distribution, retail capital markets | 📈 BULL_ANY_MID | 99 | 🔄71 | ↑1.010 | ↑1d | SQ | +1.2% | 18.92/15.09 | +1.20% | 20% |
| [HARSHA](https://in.tradingview.com/chart/?symbol=NSE:HARSHA)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Precision bearing cages, brass steel polyamide components manufacturing | 📈 BULL_ANY_MID | 94 | 🔄53 | ↑1.026 | ↑1d | SQ | +3.2% | -2.29/-8.19 | +3.24% | 20% |
| [AURUM](https://in.tradingview.com/chart/?symbol=NSE:AURUM)<br><sub>📶W9 · 🚀SS · ↓CMF22d</sub> | ✓ SAFE | Real estate software platform, rental and sales digitization | 📈 BULL_ANY_MID | 94 | 🔄81 | ↑1.017 | ↑1d | SQ | +3.9% | 9.05/7.72 | +3.92% | 20% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | Cryogenic equipment manufacturing for LNG and industrial gases | 📈 BULL_ANY_MID | 62 | ↑91 | ↑1.004 | ↓8d | SQ | +0.7% | 5.31/1.5 | +0.40% | 20% |
| [DIXON](https://in.tradingview.com/chart/?symbol=NSE:DIXON)<br><sub>📶W9 · W↑106d · ↑CMF22d</sub> | ✓ SAFE | Electronics manufacturing services for consumer appliances and lighting | 📈 BULL_ANY_MID | 58 | ↓59 | ↓0.999 | ↓2d | SQ | -0.1% | 20.68/20.15 | -0.74% | 20% |
| [RGL](https://in.tradingview.com/chart/?symbol=NSE:RGL)<br><sub>📶W9 · W↑46d · ↓CMF5d</sub> | ✓ SAFE | Global recruitment and staffing services provider | 📈 BULL_ANY_MID | 58 | ↑56 | ↓1.031 | ↑2d | SQ | +9.7% | 0.87/-6.58 | -0.92% | 20% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>📶W9 · W↑36d · ↓CMF13d</sub> | ✓ SAFE | ERW steel pipes tubes structural hollow sections manufacturer | 📈 BULL_ANY_MID | 58 | ↑58 | ↓1.004 | ↑2d | SQ | +2.4% | 14.5/12.34 | -0.97% | 20% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>📶W9 · W↑76d · ↑CMF5d</sub> | ✓ SAFE | Online auto marketplace connecting buyers sellers and financiers | 📈 BULL_ANY_MID | 51 | ↑83 | ↓1.006 | ↓9d | SQ | -0.3% | -7.71/-10.38 | -0.03% | 20% |
| [APOLLOPIPE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOPIPE)<br><sub>📶W9 · W↑11d · ↓CMF7d</sub> | ✓ SAFE | Plastic pipes CPVC UPVC HDPE agriculture construction water | 📈 BULL_ANY_MID | 48 | 🔄85 | ↑1.053 | ↑2d | — | +7.2% | 28.13/23.97 | +6.74% | 20% |
| [UDS](https://in.tradingview.com/chart/?symbol=NSE:UDS)<br><sub>📶W9 · W↑94d · ↑CMF26d</sub> | ✓ SAFE | Facilities management and business support services provider | 📈 BULL_ANY_MID | 48 | ↑64 | ↓1.012 | ↑12d | SQ | +7.9% | 56.93/56.23 | +0.10% | 20% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>📶W9 · W↑106d · ↑CMF30d</sub> | ✓ SAFE | Electronics manufacturing design integration testing subsystems defense aerospace | 📈 BULL_ANY_MID | 40 | ↑96 | ↑1.056 | ↑33d | SQ | +58.9% | 59.94/58.34 | +5.86% | 20% |
| [AFFLE](https://in.tradingview.com/chart/?symbol=NSE:AFFLE)<br><sub>📶W9 · W↑31d · ↑CMF20d</sub> | ✓ SAFE | Mobile advertising platform, consumer intelligence, app monetization | 📈 BULL_ANY_MID | 20 | ↑52 | ↑1.029 | ↑5d | — | +6.9% | 46.35/45.27 | +2.10% | 20% |
| [BHAGCHEM](https://in.tradingview.com/chart/?symbol=NSE:BHAGCHEM)<br><sub>📶W9 · W↑11d · ↓CMF21d</sub> | ✓ SAFE | Agrochemical technicals insecticides fungicides herbicides manufacturer | 📈 BULL_ANY_MID | 18 | ↑68 | ↓1.018 | ↑2d | — | +4.5% | 17.03/12.89 | -0.38% | 20% |
| [MONARCH](https://in.tradingview.com/chart/?symbol=NSE:MONARCH)<br><sub>📶W9 · W↑94d · ↑CMF16d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 18 | ↑76 | ↓1.010 | ↑2d | — | +2.6% | 34.5/34.32 | -0.40% | 20% |
| [INDIGO](https://in.tradingview.com/chart/?symbol=NSE:INDIGO)<br><sub>📶W9 · W↑63d · ↑CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 17 | ↓55 | ↓0.999 | ↓3d | — | +0.6% | 25.43/24.28 | -1.02% | 20% |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH)<br><sub>📶W9 · W↑11d · ↓CMF30d</sub> | ✓ SAFE | Hydraulic pumps, turbochargers for aerospace automotive | 📈 BULL_ANY_MID | 17 | ↑72 | ↓1.018 | ↑3d | — | +4.2% | 33.58/31.45 | -0.58% | 20% |
| [GAEL](https://in.tradingview.com/chart/?symbol=NSE:GAEL)<br><sub>📶W9 · W↑11d · ★ · ↑CMF16d</sub> | ✓ SAFE | Corn starch soya derivatives cotton yarn food pharma | 📈 BULL_ANY_MID | 17 | ↑83 | ↓1.014 | ↑3d | — | +4.5% | 21.87/20.33 | -0.03% | 20% |
| [JYOTICNC](https://in.tradingview.com/chart/?symbol=NSE:JYOTICNC)<br><sub>📶W9 · W↑46d · 🚀SS · ↓CMF18d</sub> | ✓ SAFE | CNC metal-cutting machines for aerospace, defence, automotive | 📈 BULL_ANY_MID | 16 | ↑57 | ↑1.036 | ↑4d | — | +6.6% | 39.66/36.17 | +3.75% | 20% |
| [ESCORTS](https://in.tradingview.com/chart/?symbol=NSE:ESCORTS)<br><sub>📶W9 · W↑41d · 🚀SS · ↑CMF13d</sub> | ✓ SAFE | Tractors, engines, construction equipment, agriculture and infrastructure | 📈 BULL_ANY_MID | 14 | ↑34 | ↑1.012 | ↑16d | — | +7.9% | 51.81/51.19 | +0.64% | 20% |
| [POLYPLEX](https://in.tradingview.com/chart/?symbol=NSE:POLYPLEX)<br><sub>📶W9 · W↑46d · 🚀SS · ↑CMF19d</sub> | ✓ SAFE | BOPET polyester films flexible packaging industrial applications | 📈 BULL_ANY_MID | 10 | ↑78 | ↑1.036 | ↑10d | — | +10.6% | 64.45/64.42 | +2.48% | 20% |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH)<br><sub>📶W9 · W↑6d · ★ · ↑CMF3d</sub> | ✓ SAFE | Precision aerospace defense components manufacturing global markets | 📈 BULL_ANY_MID | 9 | ↑90 | ↑1.038 | ↑11d | — | +16.2% | 30.34/26.53 | +3.30% | 20% |
| [SEAMECLTD](https://in.tradingview.com/chart/?symbol=NSE:SEAMECLTD)<br><sub>📶W9 · W↑11d · 🚀SS · ★ · ↑CMF1d</sub> | ✓ SAFE | Diving support vessels, subsea engineering, offshore oil and gas | 📈 BULL_ANY_MID | 9 | ↑84 | ↑1.026 | ↑16d | — | +11.8% | 45.38/42.92 | +1.25% | 20% |
| [BIL](https://in.tradingview.com/chart/?symbol=NSE:BIL)<br><sub>📶W9 · W↑11d · ↑CMF9d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 9 | ↑54 | ↑1.038 | ↑11d | — | +15.4% | 59.4/58.59 | +2.09% | 20% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>📶W9 · W↑11d · ★ · ↑CMF3d</sub> | ✓ SAFE | Precision forged machined components for auto and industrial | 📈 BULL_ANY_MID | 8 | ↑98 | ↑1.060 | ↑12d | — | +23.7% | 67.24/66.4 | +1.97% | 20% |
| [KDDL](https://in.tradingview.com/chart/?symbol=NSE:KDDL)<br><sub>📶W9 · W↑11d · ↓CMF8d</sub> | ✓ SAFE | Watch dials, hands, luxury components manufacturing retail | 📈 BULL_ANY_MID | 7 | ↑92 | ↑1.071 | ↑13d | — | +30.7% | 58.6/58.07 | +3.93% | 20% |
| [LENSKART](https://in.tradingview.com/chart/?symbol=NSE:LENSKART)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Eyewear design manufacturing retail omnichannel direct consumer | 📈 BULL_ANY_MID | 5 | ↑50 | ↑1.030 | ↑30d | — | +15.9% | 64.3/61.91 | +2.24% | 20% |
| [TBOTEK](https://in.tradingview.com/chart/?symbol=NSE:TBOTEK)<br><sub>📶W9 · W↑61d · ↑CMF0d</sub> | ✓ SAFE | Global travel distribution platform for hotels airlines agents | 📈 BULL_ANY_MID | 4 | ↑76 | ↑1.050 | ↑16d | — | +19.0% | 51.05/47.71 | +4.08% | 20% |
| [HAVELLS](https://in.tradingview.com/chart/?symbol=NSE:HAVELLS)<br><sub>📶W9 · W↑46d · ↑CMF20d</sub> | ✓ SAFE | Electrical goods manufacturing and distribution for households | 📈 BULL_ANY_MID | 0 | ↑35 | ↓1.015 | ↑22d | — | +11.0% | 49.91/47.42 | +0.08% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:COHANCE,NSE:JYOTHYLAB,NSE:GRPLTD,NSE:EXPLEOSOL,NSE:RISHABH,NSE:BALRAMCHIN,NSE:UFLEX,NSE:KFINTECH,NSE:COSMOFIRST,NSE:RUBICON,NSE:PTCIL,NSE:SMCGLOBAL,NSE:HARSHA,NSE:AURUM,NSE:INOXINDIA,NSE:DIXON,NSE:RGL,NSE:SAMBHV,NSE:CARTRADE,NSE:APOLLOPIPE,NSE:UDS,NSE:CYIENTDLM,NSE:AFFLE,NSE:BHAGCHEM,NSE:MONARCH,NSE:INDIGO,NSE:DYNAMATECH,NSE:GAEL,NSE:JYOTICNC,NSE:ESCORTS,NSE:POLYPLEX,NSE:ROSSTECH,NSE:SEAMECLTD,NSE:BIL,NSE:SANSERA,NSE:KDDL,NSE:LENSKART,NSE:TBOTEK,NSE:HAVELLS
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (51)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [COHANCE](https://in.tradingview.com/chart/?symbol=NSE:COHANCE)<br><sub>📶W9 · W↑6d · ↓CMF19d</sub> | ✓ SAFE | Pharmaceutical contract manufacturing development across drug lifecycle | ⚡ BULL_ANY_PPV | 92 | 🔄28 | ↑1.006 | ↑8d | SQ·PV | +3.6% | 18.44/18.03 | +0.93% | 20% |
| [JYOTHYLAB](https://in.tradingview.com/chart/?symbol=NSE:JYOTHYLAB)<br><sub>📶W9 · W↑26d · ↑CMF3d</sub> | ✓ SAFE | Home care and personal care products for Indian households | ⚡ BULL_ANY_PPV | 89 | 🔄14 | ↑1.047 | ↑1d | SQ·PV | +7.3% | 11.65/9.7 | +7.31% | 20% |
| [GRPLTD](https://in.tradingview.com/chart/?symbol=NSE:GRPLTD)<br><sub>📶W9 · W↑41d · ↓CMF10d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 62 | ↑63 | ↑1.024 | ↑3d | SQ·PV | +3.7% | 22.14/17.39 | +1.98% | 20% |
| [EXPLEOSOL](https://in.tradingview.com/chart/?symbol=NSE:EXPLEOSOL)<br><sub>📶W9 · W↑16d · 🚀SS·48x · ↑CMF0d</sub> | ✓ SAFE | Software testing QA services banking financial sector | ⚡ BULL_ANY_PPV | 49 | 🔄28 | ↑1.097 | ↑1d | PV | +13.1% | 14.35/1.19 | +13.13% | 20% |
| [RISHABH](https://in.tradingview.com/chart/?symbol=NSE:RISHABH)<br><sub>📶W9 · W↑1d · ↑CMF0d</sub> | ✓ SAFE | Electrical meters, automation instruments, industrial manufacturing | ⚡ BULL_ANY_PPV | 49 | 🔄95 | ↑1.051 | ↑1d | PV | +7.1% | 32.36/30.87 | +7.08% | 20% |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>📶W9 · W↑36d · 🚀SS · ↑CMF10d</sub> | ✓ SAFE | Sugar manufacturing, distillery, power cogeneration for domestic consumption | ⚡ BULL_ANY_PPV | 48 | 🔄79 | ↑1.041 | ↑2d | PV | +5.8% | 36.2/33.88 | +4.95% | 20% |
| [UFLEX](https://in.tradingview.com/chart/?symbol=NSE:UFLEX)<br><sub>📶W9 · W↑89d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Flexible packaging films, laminates for food beverage | ⚡ BULL_ANY_PPV | 30 | 🔄77 | ↑1.160 | ↑33d | PV | +38.7% | 74.07/64.29 | +19.99% | 20% |
| [KFINTECH](https://in.tradingview.com/chart/?symbol=NSE:KFINTECH)<br><sub>📶W9 · W↑56d · ↑CMF15d</sub> | ✓ SAFE | Registrar transfer agent digital services capital markets | ⚡ BULL_ANY_PPV | 17 | ↑47 | ↑1.035 | ↑3d | PV | +5.5% | 25.39/17.14 | +3.51% | 20% |
| [COSMOFIRST](https://in.tradingview.com/chart/?symbol=NSE:COSMOFIRST)<br><sub>📶W9 · W↑89d · 🚀SS · ↓CMF11d</sub> | ✓ SAFE | Specialty films for packaging, lamination, labeling applications | ⚡ BULL_ANY_PPV | 13 | ↑68 | ↑1.047 | ↑7d | PV | +10.7% | 62.92/58.76 | +2.82% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · W↑1d · 🚀SS·14x · ↑CMF30d</sub> | ✓ SAFE | Complex generic formulations manufacturing specialty pharmaceuticals | ⚡ BULL_ANY_PPV | 11 | ↑50 | ↑1.104 | ↑9d | PV | +20.6% | 71.94/67.96 | +11.09% | 20% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>📶W9 · W↑26d · 🚀SS·18x · ↑CMF6d</sub> | ✓ SAFE | Precision metal castings aerospace defense oil gas marine | ⚡ BULL_ANY_PPV | 9 | ↑79 | ↑1.079 | ↑11d | PV | +16.1% | 75.87/71.27 | +8.05% | 20% |
| [SMCGLOBAL](https://in.tradingview.com/chart/?symbol=NSE:SMCGLOBAL)<br><sub>📶W9 · W↑51d · ↑CMF30d</sub> | ✓ SAFE | Stock brokerage, derivatives trading, insurance distribution, retail capital markets | 📈 BULL_ANY_MID | 99 | 🔄71 | ↑1.010 | ↑1d | SQ | +1.2% | 18.92/15.09 | +1.20% | 20% |
| [HARSHA](https://in.tradingview.com/chart/?symbol=NSE:HARSHA)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Precision bearing cages, brass steel polyamide components manufacturing | 📈 BULL_ANY_MID | 94 | 🔄53 | ↑1.026 | ↑1d | SQ | +3.2% | -2.29/-8.19 | +3.24% | 20% |
| [AURUM](https://in.tradingview.com/chart/?symbol=NSE:AURUM)<br><sub>📶W9 · 🚀SS · ↓CMF22d</sub> | ✓ SAFE | Real estate software platform, rental and sales digitization | 📈 BULL_ANY_MID | 94 | 🔄81 | ↑1.017 | ↑1d | SQ | +3.9% | 9.05/7.72 | +3.92% | 20% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | Cryogenic equipment manufacturing for LNG and industrial gases | 📈 BULL_ANY_MID | 62 | ↑91 | ↑1.004 | ↓8d | SQ | +0.7% | 5.31/1.5 | +0.40% | 20% |
| [RGL](https://in.tradingview.com/chart/?symbol=NSE:RGL)<br><sub>📶W9 · W↑46d · ↓CMF5d</sub> | ✓ SAFE | Global recruitment and staffing services provider | 📈 BULL_ANY_MID | 58 | ↑56 | ↓1.031 | ↑2d | SQ | +9.7% | 0.87/-6.58 | -0.92% | 20% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>📶W9 · W↑36d · ↓CMF13d</sub> | ✓ SAFE | ERW steel pipes tubes structural hollow sections manufacturer | 📈 BULL_ANY_MID | 58 | ↑58 | ↓1.004 | ↑2d | SQ | +2.4% | 14.5/12.34 | -0.97% | 20% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>📶W9 · W↑76d · ↑CMF5d</sub> | ✓ SAFE | Online auto marketplace connecting buyers sellers and financiers | 📈 BULL_ANY_MID | 51 | ↑83 | ↓1.006 | ↓9d | SQ | -0.3% | -7.71/-10.38 | -0.03% | 20% |
| [APOLLOPIPE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOPIPE)<br><sub>📶W9 · W↑11d · ↓CMF7d</sub> | ✓ SAFE | Plastic pipes CPVC UPVC HDPE agriculture construction water | 📈 BULL_ANY_MID | 48 | 🔄85 | ↑1.053 | ↑2d | — | +7.2% | 28.13/23.97 | +6.74% | 20% |
| [UDS](https://in.tradingview.com/chart/?symbol=NSE:UDS)<br><sub>📶W9 · W↑94d · ↑CMF26d</sub> | ✓ SAFE | Facilities management and business support services provider | 📈 BULL_ANY_MID | 48 | ↑64 | ↓1.012 | ↑12d | SQ | +7.9% | 56.93/56.23 | +0.10% | 20% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>📶W9 · W↑106d · ↑CMF30d</sub> | ✓ SAFE | Electronics manufacturing design integration testing subsystems defense aerospace | 📈 BULL_ANY_MID | 40 | ↑96 | ↑1.056 | ↑33d | SQ | +58.9% | 59.94/58.34 | +5.86% | 20% |
| [AFFLE](https://in.tradingview.com/chart/?symbol=NSE:AFFLE)<br><sub>📶W9 · W↑31d · ↑CMF20d</sub> | ✓ SAFE | Mobile advertising platform, consumer intelligence, app monetization | 📈 BULL_ANY_MID | 20 | ↑52 | ↑1.029 | ↑5d | — | +6.9% | 46.35/45.27 | +2.10% | 20% |
| [BHAGCHEM](https://in.tradingview.com/chart/?symbol=NSE:BHAGCHEM)<br><sub>📶W9 · W↑11d · ↓CMF21d</sub> | ✓ SAFE | Agrochemical technicals insecticides fungicides herbicides manufacturer | 📈 BULL_ANY_MID | 18 | ↑68 | ↓1.018 | ↑2d | — | +4.5% | 17.03/12.89 | -0.38% | 20% |
| [MONARCH](https://in.tradingview.com/chart/?symbol=NSE:MONARCH)<br><sub>📶W9 · W↑94d · ↑CMF16d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 18 | ↑76 | ↓1.010 | ↑2d | — | +2.6% | 34.5/34.32 | -0.40% | 20% |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH)<br><sub>📶W9 · W↑11d · ↓CMF30d</sub> | ✓ SAFE | Hydraulic pumps, turbochargers for aerospace automotive | 📈 BULL_ANY_MID | 17 | ↑72 | ↓1.018 | ↑3d | — | +4.2% | 33.58/31.45 | -0.58% | 20% |
| [GAEL](https://in.tradingview.com/chart/?symbol=NSE:GAEL)<br><sub>📶W9 · W↑11d · ★ · ↑CMF16d</sub> | ✓ SAFE | Corn starch soya derivatives cotton yarn food pharma | 📈 BULL_ANY_MID | 17 | ↑83 | ↓1.014 | ↑3d | — | +4.5% | 21.87/20.33 | -0.03% | 20% |
| [JYOTICNC](https://in.tradingview.com/chart/?symbol=NSE:JYOTICNC)<br><sub>📶W9 · W↑46d · 🚀SS · ↓CMF18d</sub> | ✓ SAFE | CNC metal-cutting machines for aerospace, defence, automotive | 📈 BULL_ANY_MID | 16 | ↑57 | ↑1.036 | ↑4d | — | +6.6% | 39.66/36.17 | +3.75% | 20% |
| [ESCORTS](https://in.tradingview.com/chart/?symbol=NSE:ESCORTS)<br><sub>📶W9 · W↑41d · 🚀SS · ↑CMF13d</sub> | ✓ SAFE | Tractors, engines, construction equipment, agriculture and infrastructure | 📈 BULL_ANY_MID | 14 | ↑34 | ↑1.012 | ↑16d | — | +7.9% | 51.81/51.19 | +0.64% | 20% |
| [POLYPLEX](https://in.tradingview.com/chart/?symbol=NSE:POLYPLEX)<br><sub>📶W9 · W↑46d · 🚀SS · ↑CMF19d</sub> | ✓ SAFE | BOPET polyester films flexible packaging industrial applications | 📈 BULL_ANY_MID | 10 | ↑78 | ↑1.036 | ↑10d | — | +10.6% | 64.45/64.42 | +2.48% | 20% |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH)<br><sub>📶W9 · W↑6d · ★ · ↑CMF3d</sub> | ✓ SAFE | Precision aerospace defense components manufacturing global markets | 📈 BULL_ANY_MID | 9 | ↑90 | ↑1.038 | ↑11d | — | +16.2% | 30.34/26.53 | +3.30% | 20% |
| [SEAMECLTD](https://in.tradingview.com/chart/?symbol=NSE:SEAMECLTD)<br><sub>📶W9 · W↑11d · 🚀SS · ★ · ↑CMF1d</sub> | ✓ SAFE | Diving support vessels, subsea engineering, offshore oil and gas | 📈 BULL_ANY_MID | 9 | ↑84 | ↑1.026 | ↑16d | — | +11.8% | 45.38/42.92 | +1.25% | 20% |
| [BIL](https://in.tradingview.com/chart/?symbol=NSE:BIL)<br><sub>📶W9 · W↑11d · ↑CMF9d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 9 | ↑54 | ↑1.038 | ↑11d | — | +15.4% | 59.4/58.59 | +2.09% | 20% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>📶W9 · W↑11d · ★ · ↑CMF3d</sub> | ✓ SAFE | Precision forged machined components for auto and industrial | 📈 BULL_ANY_MID | 8 | ↑98 | ↑1.060 | ↑12d | — | +23.7% | 67.24/66.4 | +1.97% | 20% |
| [KDDL](https://in.tradingview.com/chart/?symbol=NSE:KDDL)<br><sub>📶W9 · W↑11d · ↓CMF8d</sub> | ✓ SAFE | Watch dials, hands, luxury components manufacturing retail | 📈 BULL_ANY_MID | 7 | ↑92 | ↑1.071 | ↑13d | — | +30.7% | 58.6/58.07 | +3.93% | 20% |
| [LENSKART](https://in.tradingview.com/chart/?symbol=NSE:LENSKART)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Eyewear design manufacturing retail omnichannel direct consumer | 📈 BULL_ANY_MID | 5 | ↑50 | ↑1.030 | ↑30d | — | +15.9% | 64.3/61.91 | +2.24% | 20% |
| [TBOTEK](https://in.tradingview.com/chart/?symbol=NSE:TBOTEK)<br><sub>📶W9 · W↑61d · ↑CMF0d</sub> | ✓ SAFE | Global travel distribution platform for hotels airlines agents | 📈 BULL_ANY_MID | 4 | ↑76 | ↑1.050 | ↑16d | — | +19.0% | 51.05/47.71 | +4.08% | 20% |
| [HAVELLS](https://in.tradingview.com/chart/?symbol=NSE:HAVELLS)<br><sub>📶W9 · W↑46d · ↑CMF20d</sub> | ✓ SAFE | Electrical goods manufacturing and distribution for households | 📈 BULL_ANY_MID | 0 | ↑35 | ↓1.015 | ↑22d | — | +11.0% | 49.91/47.42 | +0.08% | 20% |
| [BRIGHOTEL](https://in.tradingview.com/chart/?symbol=NSE:BRIGHOTEL)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄21 | ↑1.014 | ↑1d | SQ·PV | +2.4% | -35.67/-40.43 | +2.36% | 20% |
| [SPMLINFRA](https://in.tradingview.com/chart/?symbol=NSE:SPMLINFRA)<br><sub>↓CMF6d</sub> | ✓ SAFE | Water power EPC projects municipal industrial clients | ⚡ BULL_ANY_PPV | 54 | 🔄25 | ↑1.025 | ↑1d | PV | +3.4% | -34.83/-41.64 | +3.38% | 20% |
| [ALEMBICLTD](https://in.tradingview.com/chart/?symbol=NSE:ALEMBICLTD)<br><sub>↑CMF0d</sub> | ✓ SAFE | Pharmaceutical manufacturer APIs generics India exports | ⚡ BULL_ANY_PPV | 19 | ↑29 | ↑1.036 | ↑1d | PV | +3.8% | -30.01/-38.6 | +3.80% | 20% |
| [GOKEX](https://in.tradingview.com/chart/?symbol=NSE:GOKEX)<br><sub>🚀SS · ↑CMF2d · 🎯SLING</sub> | ✓ SAFE | Apparel manufacturer for global fashion brands and retailers | 🟡 BULL_OS_L2 | 99 | 🔄52 | ↑1.012 | ↑1d | SQ | +2.6% | -48.23/-53.77 | +2.61% | 20% 🟦 |
| [MBEL](https://in.tradingview.com/chart/?symbol=NSE:MBEL)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Pre-engineered buildings, steel roofing, industrial structures | 🟡 BULL_OS_L2 | 40 | 🔄8 | ↑1.013 | ↓27d | — | -8.7% | -49.93/-53.25 | +4.77% | 20% |
| [VTL](https://in.tradingview.com/chart/?symbol=NSE:VTL)<br><sub>↓CMF25d</sub> | ✓ SAFE | Yarn fabric acrylic fiber garments textiles manufacturer | 📈 BULL_ANY_MID | 99 | 🔄71 | ↑1.010 | ↑1d | SQ | +2.5% | -46.67/-49.29 | +2.48% | 20% |
| [MRF](https://in.tradingview.com/chart/?symbol=NSE:MRF)<br><sub>W↑46d · ↓CMF9d</sub> | ⚠ CAUTION | Tire manufacturer for cars two-wheelers trucks tractors | 📈 BULL_ANY_MID | 58 | ↑31 | ↓1.002 | ↑2d | SQ | +1.6% | -1.62/-1.66 | -0.36% | 20% |
| [INOXWIND](https://in.tradingview.com/chart/?symbol=NSE:INOXWIND)<br><sub>🚀SS · ↓CMF30d · ÷DIV</sub> | ✓ SAFE | Wind turbine manufacturing renewable energy utilities corporates | 📈 BULL_ANY_MID | 54 | 🔄2 | ↑1.028 | ↑1d | — | +6.0% | -42.16/-46.88 | +6.05% | 20% |
| [AMBER](https://in.tradingview.com/chart/?symbol=NSE:AMBER)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Room air conditioner manufacturing and design services for brands | 📈 BULL_ANY_MID | 51 | 🔄37 | ↑1.002 | ↓9d | — | -1.8% | -40.03/-45.81 | +0.51% | 20% |
| [PSPPROJECT](https://in.tradingview.com/chart/?symbol=NSE:PSPPROJECT)<br><sub>↓CMF18d</sub> | ✓ SAFE | EPC contractor industrial institutional government residential projects | 📈 BULL_ANY_MID | 44 | 🔄72 | ↑1.003 | ↓16d | — | -8.2% | -45.02/-46.28 | +2.67% | 20% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>↓CMF29d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 40 | 🔄55 | ↑1.004 | ↓21d | — | -7.1% | -50.77/-52.92 | +2.36% | 20% |
| [PHOENIXLTD](https://in.tradingview.com/chart/?symbol=NSE:PHOENIXLTD)<br><sub>↓CMF13d</sub> | ✓ SAFE | Retail malls, office spaces, hospitality mixed-use developments | 📈 BULL_ANY_MID | 40 | 🔄64 | ↑1.005 | ↓47d | — | +11.4% | -36.65/-38.44 | +2.11% | 20% |
| [GANECOS](https://in.tradingview.com/chart/?symbol=NSE:GANECOS)<br><sub>↓CMF9d</sub> | ✓ SAFE | PET waste recycling, polyester fiber production, textile sector | 📈 BULL_ANY_MID | 40 | 🔄54 | ↑1.010 | ↓34d | — | +23.6% | -26.47/-27.32 | +3.83% | 20% 🟦 |
| [GREENPLY](https://in.tradingview.com/chart/?symbol=NSE:GREENPLY)<br><sub>↓CMF30d</sub> | ✓ SAFE | Plywood MDF panels manufacturing building construction interiors | 📈 BULL_ANY_MID | 40 | 🔄56 | ↑1.005 | ↓55d | — | +15.7% | -31.52/-32.98 | +1.90% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:COHANCE,NSE:JYOTHYLAB,NSE:GRPLTD,NSE:EXPLEOSOL,NSE:RISHABH,NSE:BALRAMCHIN,NSE:UFLEX,NSE:KFINTECH,NSE:COSMOFIRST,NSE:RUBICON,NSE:PTCIL,NSE:SMCGLOBAL,NSE:HARSHA,NSE:AURUM,NSE:INOXINDIA,NSE:RGL,NSE:SAMBHV,NSE:CARTRADE,NSE:APOLLOPIPE,NSE:UDS,NSE:CYIENTDLM,NSE:AFFLE,NSE:BHAGCHEM,NSE:MONARCH,NSE:DYNAMATECH,NSE:GAEL,NSE:JYOTICNC,NSE:ESCORTS,NSE:POLYPLEX,NSE:ROSSTECH,NSE:SEAMECLTD,NSE:BIL,NSE:SANSERA,NSE:KDDL,NSE:LENSKART,NSE:TBOTEK,NSE:HAVELLS,NSE:BRIGHOTEL,NSE:SPMLINFRA,NSE:ALEMBICLTD,NSE:GOKEX,NSE:MBEL,NSE:VTL,NSE:MRF,NSE:INOXWIND,NSE:AMBER,NSE:PSPPROJECT,NSE:ADANIPORTS,NSE:PHOENIXLTD,NSE:GANECOS,NSE:GREENPLY
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (27)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [COHANCE](https://in.tradingview.com/chart/?symbol=NSE:COHANCE)<br><sub>📶W9 · W↑6d · ↓CMF19d</sub> | ✓ SAFE | Pharmaceutical contract manufacturing development across drug lifecycle | ⚡ BULL_ANY_PPV | 92 | 🔄28 | ↑1.006 | ↑8d | SQ·PV | +3.6% | 18.44/18.03 | +0.93% | 20% |
| [JYOTHYLAB](https://in.tradingview.com/chart/?symbol=NSE:JYOTHYLAB)<br><sub>📶W9 · W↑26d · ↑CMF3d</sub> | ✓ SAFE | Home care and personal care products for Indian households | ⚡ BULL_ANY_PPV | 89 | 🔄14 | ↑1.047 | ↑1d | SQ·PV | +7.3% | 11.65/9.7 | +7.31% | 20% |
| [GRPLTD](https://in.tradingview.com/chart/?symbol=NSE:GRPLTD)<br><sub>📶W9 · W↑41d · ↓CMF10d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 62 | ↑63 | ↑1.024 | ↑3d | SQ·PV | +3.7% | 22.14/17.39 | +1.98% | 20% |
| [SMCGLOBAL](https://in.tradingview.com/chart/?symbol=NSE:SMCGLOBAL)<br><sub>📶W9 · W↑51d · ↑CMF30d</sub> | ✓ SAFE | Stock brokerage, derivatives trading, insurance distribution, retail capital markets | 📈 BULL_ANY_MID | 99 | 🔄71 | ↑1.010 | ↑1d | SQ | +1.2% | 18.92/15.09 | +1.20% | 20% |
| [HARSHA](https://in.tradingview.com/chart/?symbol=NSE:HARSHA)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Precision bearing cages, brass steel polyamide components manufacturing | 📈 BULL_ANY_MID | 94 | 🔄53 | ↑1.026 | ↑1d | SQ | +3.2% | -2.29/-8.19 | +3.24% | 20% |
| [AURUM](https://in.tradingview.com/chart/?symbol=NSE:AURUM)<br><sub>📶W9 · 🚀SS · ↓CMF22d</sub> | ✓ SAFE | Real estate software platform, rental and sales digitization | 📈 BULL_ANY_MID | 94 | 🔄81 | ↑1.017 | ↑1d | SQ | +3.9% | 9.05/7.72 | +3.92% | 20% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | Cryogenic equipment manufacturing for LNG and industrial gases | 📈 BULL_ANY_MID | 62 | ↑91 | ↑1.004 | ↓8d | SQ | +0.7% | 5.31/1.5 | +0.40% | 20% |
| [DIXON](https://in.tradingview.com/chart/?symbol=NSE:DIXON)<br><sub>📶W9 · W↑106d · ↑CMF22d</sub> | ✓ SAFE | Electronics manufacturing services for consumer appliances and lighting | 📈 BULL_ANY_MID | 58 | ↓59 | ↓0.999 | ↓2d | SQ | -0.1% | 20.68/20.15 | -0.74% | 20% |
| [RGL](https://in.tradingview.com/chart/?symbol=NSE:RGL)<br><sub>📶W9 · W↑46d · ↓CMF5d</sub> | ✓ SAFE | Global recruitment and staffing services provider | 📈 BULL_ANY_MID | 58 | ↑56 | ↓1.031 | ↑2d | SQ | +9.7% | 0.87/-6.58 | -0.92% | 20% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>📶W9 · W↑36d · ↓CMF13d</sub> | ✓ SAFE | ERW steel pipes tubes structural hollow sections manufacturer | 📈 BULL_ANY_MID | 58 | ↑58 | ↓1.004 | ↑2d | SQ | +2.4% | 14.5/12.34 | -0.97% | 20% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>📶W9 · W↑76d · ↑CMF5d</sub> | ✓ SAFE | Online auto marketplace connecting buyers sellers and financiers | 📈 BULL_ANY_MID | 51 | ↑83 | ↓1.006 | ↓9d | SQ | -0.3% | -7.71/-10.38 | -0.03% | 20% |
| [UDS](https://in.tradingview.com/chart/?symbol=NSE:UDS)<br><sub>📶W9 · W↑94d · ↑CMF26d</sub> | ✓ SAFE | Facilities management and business support services provider | 📈 BULL_ANY_MID | 48 | ↑64 | ↓1.012 | ↑12d | SQ | +7.9% | 56.93/56.23 | +0.10% | 20% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>📶W9 · W↑106d · ↑CMF30d</sub> | ✓ SAFE | Electronics manufacturing design integration testing subsystems defense aerospace | 📈 BULL_ANY_MID | 40 | ↑96 | ↑1.056 | ↑33d | SQ | +58.9% | 59.94/58.34 | +5.86% | 20% |
| [BRIGHOTEL](https://in.tradingview.com/chart/?symbol=NSE:BRIGHOTEL)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄21 | ↑1.014 | ↑1d | SQ·PV | +2.4% | -35.67/-40.43 | +2.36% | 20% |
| [GOKEX](https://in.tradingview.com/chart/?symbol=NSE:GOKEX)<br><sub>🚀SS · ↑CMF2d · 🎯SLING</sub> | ✓ SAFE | Apparel manufacturer for global fashion brands and retailers | 🟡 BULL_OS_L2 | 99 | 🔄52 | ↑1.012 | ↑1d | SQ | +2.6% | -48.23/-53.77 | +2.61% | 20% 🟦 |
| [VTL](https://in.tradingview.com/chart/?symbol=NSE:VTL)<br><sub>↓CMF25d</sub> | ✓ SAFE | Yarn fabric acrylic fiber garments textiles manufacturer | 📈 BULL_ANY_MID | 99 | 🔄71 | ↑1.010 | ↑1d | SQ | +2.5% | -46.67/-49.29 | +2.48% | 20% |
| [EMAMILTD](https://in.tradingview.com/chart/?symbol=NSE:EMAMILTD)<br><sub>W↑46d · ↓CMF30d</sub> | ✓ SAFE | Personal care, healthcare, FMCG for Indian households | 📈 BULL_ANY_MID | 62 | ↓13 | ↑1.001 | ↓8d | SQ | +0.5% | -20.62/-22.1 | +0.30% | 20% |
| [BALMLAWRIE](https://in.tradingview.com/chart/?symbol=NSE:BALMLAWRIE)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | PSU lubricants, packaging, logistics, refinery services | 📈 BULL_ANY_MID | 62 | ↓28 | ↑1.001 | ↓8d | SQ | -0.7% | -49.09/-51.12 | +0.67% | 20% |
| [NTPC](https://in.tradingview.com/chart/?symbol=NSE:NTPC)<br><sub>↑CMF7d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↓30 | ↓0.992 | ↓2d | SQ | +0.1% | -49.42/-49.91 | -1.25% | 20% |
| [MRF](https://in.tradingview.com/chart/?symbol=NSE:MRF)<br><sub>W↑46d · ↓CMF9d</sub> | ⚠ CAUTION | Tire manufacturer for cars two-wheelers trucks tractors | 📈 BULL_ANY_MID | 58 | ↑31 | ↓1.002 | ↑2d | SQ | +1.6% | -1.62/-1.66 | -0.36% | 20% |
| [NIITLTD](https://in.tradingview.com/chart/?symbol=NSE:NIITLTD)<br><sub>🚀SS · ↓CMF2d</sub> | ✓ SAFE | Vocational skills training, IT certification, global workforce development | 📈 BULL_ANY_MID | 56 | ↓73 | ↑0.998 | ↓9d | SQ | -0.6% | -18.09/-21.84 | +0.08% | 20% |
| [BFINVEST](https://in.tradingview.com/chart/?symbol=NSE:BFINVEST)<br><sub>W↑6d · ↓CMF1d</sub> | ✓ SAFE | Kalyani Group holding company invests subsidiaries manufacturing | 📈 BULL_ANY_MID | 54 | ↓61 | ↑0.997 | ↓11d | SQ | +2.1% | 3.07/2.23 | +0.18% | 20% |
| [CAPACITE](https://in.tradingview.com/chart/?symbol=NSE:CAPACITE)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | EPC contractor high-rise buildings residential commercial urban infrastructure | 📈 BULL_ANY_MID | 51 | ↓13 | ↓0.993 | ↓9d | SQ | -0.8% | -38.5/-40.29 | -1.23% | 20% |
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO)<br><sub>↑CMF9d · ⚠️TRAP</sub> | ✓ SAFE | Defence electronics design assembly testing aerospace systems | 📈 BULL_ANY_MID | 49 | ↓88 | ↓0.990 | ↓11d | SQ | -0.7% | -17.78/-18.32 | -1.65% | 20% 🟦 |
| [HAWKINCOOK](https://in.tradingview.com/chart/?symbol=NSE:HAWKINCOOK)<br><sub>↓CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 45 | ↓50 | ↑0.999 | ↓57d | SQ | +16.3% | -36.3/-36.87 | +0.00% | 20% |
| [EMMVEE](https://in.tradingview.com/chart/?symbol=NSE:EMMVEE)<br><sub>↓CMF7d</sub> | ✓ SAFE | Solar PV modules and cells manufacturing for energy sector | 📈 BULL_ANY_MID | 40 | ↓50 | ↓0.997 | ↓24d | SQ | -3.9% | -21.13/-22.9 | -0.16% | 20% |
| [KALAMANDIR](https://in.tradingview.com/chart/?symbol=NSE:KALAMANDIR)<br><sub>↓CMF30d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE | Ethnic sarees silk apparel retail South India omni-channel | 📈 BULL_ANY_MID | 40 | ↓2 | ↓0.989 | ↓44d | SQ | -18.4% | -48.73/-50.1 | -1.01% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:COHANCE,NSE:JYOTHYLAB,NSE:GRPLTD,NSE:SMCGLOBAL,NSE:HARSHA,NSE:AURUM,NSE:INOXINDIA,NSE:DIXON,NSE:RGL,NSE:SAMBHV,NSE:CARTRADE,NSE:UDS,NSE:CYIENTDLM,NSE:BRIGHOTEL,NSE:GOKEX,NSE:VTL,NSE:EMAMILTD,NSE:BALMLAWRIE,NSE:NTPC,NSE:MRF,NSE:NIITLTD,NSE:BFINVEST,NSE:CAPACITE,NSE:APOLLO,NSE:HAWKINCOOK,NSE:EMMVEE,NSE:KALAMANDIR
```

---

### 🔥 MAJOR — PPV confirmed (12)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [EXPLEOSOL](https://in.tradingview.com/chart/?symbol=NSE:EXPLEOSOL)<br><sub>📶W9 · W↑16d · 🚀SS·48x · ↑CMF0d</sub> | ✓ SAFE | Software testing QA services banking financial sector | ⚡ BULL_ANY_PPV | 49 | 🔄28 | ↑1.097 | ↑1d | PV | +13.1% | 14.35/1.19 | +13.13% | 20% |
| [RISHABH](https://in.tradingview.com/chart/?symbol=NSE:RISHABH)<br><sub>📶W9 · W↑1d · ↑CMF0d</sub> | ✓ SAFE | Electrical meters, automation instruments, industrial manufacturing | ⚡ BULL_ANY_PPV | 49 | 🔄95 | ↑1.051 | ↑1d | PV | +7.1% | 32.36/30.87 | +7.08% | 20% |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>📶W9 · W↑36d · 🚀SS · ↑CMF10d</sub> | ✓ SAFE | Sugar manufacturing, distillery, power cogeneration for domestic consumption | ⚡ BULL_ANY_PPV | 48 | 🔄79 | ↑1.041 | ↑2d | PV | +5.8% | 36.2/33.88 | +4.95% | 20% |
| [UFLEX](https://in.tradingview.com/chart/?symbol=NSE:UFLEX)<br><sub>📶W9 · W↑89d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Flexible packaging films, laminates for food beverage | ⚡ BULL_ANY_PPV | 30 | 🔄77 | ↑1.160 | ↑33d | PV | +38.7% | 74.07/64.29 | +19.99% | 20% |
| [KFINTECH](https://in.tradingview.com/chart/?symbol=NSE:KFINTECH)<br><sub>📶W9 · W↑56d · ↑CMF15d</sub> | ✓ SAFE | Registrar transfer agent digital services capital markets | ⚡ BULL_ANY_PPV | 17 | ↑47 | ↑1.035 | ↑3d | PV | +5.5% | 25.39/17.14 | +3.51% | 20% |
| [COSMOFIRST](https://in.tradingview.com/chart/?symbol=NSE:COSMOFIRST)<br><sub>📶W9 · W↑89d · 🚀SS · ↓CMF11d</sub> | ✓ SAFE | Specialty films for packaging, lamination, labeling applications | ⚡ BULL_ANY_PPV | 13 | ↑68 | ↑1.047 | ↑7d | PV | +10.7% | 62.92/58.76 | +2.82% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · W↑1d · 🚀SS·14x · ↑CMF30d</sub> | ✓ SAFE | Complex generic formulations manufacturing specialty pharmaceuticals | ⚡ BULL_ANY_PPV | 11 | ↑50 | ↑1.104 | ↑9d | PV | +20.6% | 71.94/67.96 | +11.09% | 20% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>📶W9 · W↑26d · 🚀SS·18x · ↑CMF6d</sub> | ✓ SAFE | Precision metal castings aerospace defense oil gas marine | ⚡ BULL_ANY_PPV | 9 | ↑79 | ↑1.079 | ↑11d | PV | +16.1% | 75.87/71.27 | +8.05% | 20% |
| [SPMLINFRA](https://in.tradingview.com/chart/?symbol=NSE:SPMLINFRA)<br><sub>↓CMF6d</sub> | ✓ SAFE | Water power EPC projects municipal industrial clients | ⚡ BULL_ANY_PPV | 54 | 🔄25 | ↑1.025 | ↑1d | PV | +3.4% | -34.83/-41.64 | +3.38% | 20% |
| [ALEMBICLTD](https://in.tradingview.com/chart/?symbol=NSE:ALEMBICLTD)<br><sub>↑CMF0d</sub> | ✓ SAFE | Pharmaceutical manufacturer APIs generics India exports | ⚡ BULL_ANY_PPV | 19 | ↑29 | ↑1.036 | ↑1d | PV | +3.8% | -30.01/-38.6 | +3.80% | 20% |
| [MASFIN](https://in.tradingview.com/chart/?symbol=NSE:MASFIN)<br><sub>↓CMF11d</sub> | ⚠ CAUTION | Retail financing NBFC for MSMEs and vehicle loans | ⚡ BULL_ANY_PPV | 11 | ↓37 | ↑0.999 | ↓14d | PV | -3.0% | -39.4/-40.01 | +1.26% | 20% |
| [TRIVENI](https://in.tradingview.com/chart/?symbol=NSE:TRIVENI)<br><sub>🚀SS · ↑CMF0d</sub> | ✓ SAFE | Sugar ethanol production, power transmission, water treatment solutions | ⚡ BULL_ANY_PPV | 5 | ↓3 | ↑0.969 | ↓38d | PV | -25.1% | -23.86/-24.06 | +4.96% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:EXPLEOSOL,NSE:RISHABH,NSE:BALRAMCHIN,NSE:UFLEX,NSE:KFINTECH,NSE:COSMOFIRST,NSE:RUBICON,NSE:PTCIL,NSE:SPMLINFRA,NSE:ALEMBICLTD,NSE:MASFIN,NSE:TRIVENI
```

### 🟢 OVERSOLD — reversal from −53/−60 (8)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ASALCBR](https://in.tradingview.com/chart/?symbol=NSE:ASALCBR)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 8 | ↓7 | ↑0.992 | ↓17d | — | -8.8% | -61.38/-62.43 | +2.70% | 20% |
| [PNBGILTS](https://in.tradingview.com/chart/?symbol=NSE:PNBGILTS)<br><sub>↓CMF7d · 🎯SLING</sub> | ✓ SAFE | Government securities dealer, primary dealer, debt market | 🟢 BULL_OVERSOLD | 5 | ↓27 | ↑0.992 | ↓23d | — | -8.3% | -63.71/-63.89 | +1.17% | 20% |
| [CEINSYS](https://in.tradingview.com/chart/?symbol=NSE:CEINSYS)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Geospatial software and enterprise mobility solutions provider | 🟢 BULL_OVERSOLD | 0 | ↓50 | ↓0.966 | ↓27d | — | -13.7% | -65.18/-68.05 | -3.96% | 20% |
| [AWHCL](https://in.tradingview.com/chart/?symbol=NSE:AWHCL)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Waste collection transport processing disposal services | 🟢 BULL_OVERSOLD | 0 | ↓4 | ↓0.957 | ↓27d | — | -15.2% | -73.82/-73.84 | -1.13% | 20% |
| [SHANTIGEAR](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGEAR)<br><sub>↑CMF13d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 0 | ↓10 | ↓0.980 | ↓31d | — | -11.5% | -65.97/-66.23 | -1.03% | 20% |
| [MBEL](https://in.tradingview.com/chart/?symbol=NSE:MBEL)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Pre-engineered buildings, steel roofing, industrial structures | 🟡 BULL_OS_L2 | 40 | 🔄8 | ↑1.013 | ↓27d | — | -8.7% | -49.93/-53.25 | +4.77% | 20% |
| [RELIGARE](https://in.tradingview.com/chart/?symbol=NSE:RELIGARE)<br><sub>↓CMF6d · ⚠️TRAP</sub> | ✓ SAFE | Financial services holding: insurance, broking, SME lending | 🟡 BULL_OS_L2 | 9 | ↓30 | ↓0.969 | ↓11d | — | -8.7% | -53.77/-53.9 | -1.55% | 20% |
| [AVANTIFEED](https://in.tradingview.com/chart/?symbol=NSE:AVANTIFEED)<br><sub>↓CMF12d · 🎯SLING</sub> | ✓ SAFE | Shrimp feed manufacturing and shrimp export processing | 🟡 BULL_OS_L2 | 8 | ↓19 | ↑0.990 | ↓17d | — | -8.7% | -53.11/-53.26 | +1.65% | 20% 🟦 |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ASALCBR,NSE:PNBGILTS,NSE:CEINSYS,NSE:AWHCL,NSE:SHANTIGEAR,NSE:MBEL,NSE:RELIGARE,NSE:AVANTIFEED
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (34)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [APOLLOPIPE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOPIPE)<br><sub>📶W9 · W↑11d · ↓CMF7d</sub> | ✓ SAFE | Plastic pipes CPVC UPVC HDPE agriculture construction water | 📈 BULL_ANY_MID | 48 | 🔄85 | ↑1.053 | ↑2d | — | +7.2% | 28.13/23.97 | +6.74% | 20% |
| [AFFLE](https://in.tradingview.com/chart/?symbol=NSE:AFFLE)<br><sub>📶W9 · W↑31d · ↑CMF20d</sub> | ✓ SAFE | Mobile advertising platform, consumer intelligence, app monetization | 📈 BULL_ANY_MID | 20 | ↑52 | ↑1.029 | ↑5d | — | +6.9% | 46.35/45.27 | +2.10% | 20% |
| [BHAGCHEM](https://in.tradingview.com/chart/?symbol=NSE:BHAGCHEM)<br><sub>📶W9 · W↑11d · ↓CMF21d</sub> | ✓ SAFE | Agrochemical technicals insecticides fungicides herbicides manufacturer | 📈 BULL_ANY_MID | 18 | ↑68 | ↓1.018 | ↑2d | — | +4.5% | 17.03/12.89 | -0.38% | 20% |
| [MONARCH](https://in.tradingview.com/chart/?symbol=NSE:MONARCH)<br><sub>📶W9 · W↑94d · ↑CMF16d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 18 | ↑76 | ↓1.010 | ↑2d | — | +2.6% | 34.5/34.32 | -0.40% | 20% |
| [INDIGO](https://in.tradingview.com/chart/?symbol=NSE:INDIGO)<br><sub>📶W9 · W↑63d · ↑CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 17 | ↓55 | ↓0.999 | ↓3d | — | +0.6% | 25.43/24.28 | -1.02% | 20% |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH)<br><sub>📶W9 · W↑11d · ↓CMF30d</sub> | ✓ SAFE | Hydraulic pumps, turbochargers for aerospace automotive | 📈 BULL_ANY_MID | 17 | ↑72 | ↓1.018 | ↑3d | — | +4.2% | 33.58/31.45 | -0.58% | 20% |
| [GAEL](https://in.tradingview.com/chart/?symbol=NSE:GAEL)<br><sub>📶W9 · W↑11d · ★ · ↑CMF16d</sub> | ✓ SAFE | Corn starch soya derivatives cotton yarn food pharma | 📈 BULL_ANY_MID | 17 | ↑83 | ↓1.014 | ↑3d | — | +4.5% | 21.87/20.33 | -0.03% | 20% |
| [JYOTICNC](https://in.tradingview.com/chart/?symbol=NSE:JYOTICNC)<br><sub>📶W9 · W↑46d · 🚀SS · ↓CMF18d</sub> | ✓ SAFE | CNC metal-cutting machines for aerospace, defence, automotive | 📈 BULL_ANY_MID | 16 | ↑57 | ↑1.036 | ↑4d | — | +6.6% | 39.66/36.17 | +3.75% | 20% |
| [ESCORTS](https://in.tradingview.com/chart/?symbol=NSE:ESCORTS)<br><sub>📶W9 · W↑41d · 🚀SS · ↑CMF13d</sub> | ✓ SAFE | Tractors, engines, construction equipment, agriculture and infrastructure | 📈 BULL_ANY_MID | 14 | ↑34 | ↑1.012 | ↑16d | — | +7.9% | 51.81/51.19 | +0.64% | 20% |
| [POLYPLEX](https://in.tradingview.com/chart/?symbol=NSE:POLYPLEX)<br><sub>📶W9 · W↑46d · 🚀SS · ↑CMF19d</sub> | ✓ SAFE | BOPET polyester films flexible packaging industrial applications | 📈 BULL_ANY_MID | 10 | ↑78 | ↑1.036 | ↑10d | — | +10.6% | 64.45/64.42 | +2.48% | 20% |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH)<br><sub>📶W9 · W↑6d · ★ · ↑CMF3d</sub> | ✓ SAFE | Precision aerospace defense components manufacturing global markets | 📈 BULL_ANY_MID | 9 | ↑90 | ↑1.038 | ↑11d | — | +16.2% | 30.34/26.53 | +3.30% | 20% |
| [SEAMECLTD](https://in.tradingview.com/chart/?symbol=NSE:SEAMECLTD)<br><sub>📶W9 · W↑11d · 🚀SS · ★ · ↑CMF1d</sub> | ✓ SAFE | Diving support vessels, subsea engineering, offshore oil and gas | 📈 BULL_ANY_MID | 9 | ↑84 | ↑1.026 | ↑16d | — | +11.8% | 45.38/42.92 | +1.25% | 20% |
| [BIL](https://in.tradingview.com/chart/?symbol=NSE:BIL)<br><sub>📶W9 · W↑11d · ↑CMF9d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 9 | ↑54 | ↑1.038 | ↑11d | — | +15.4% | 59.4/58.59 | +2.09% | 20% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>📶W9 · W↑11d · ★ · ↑CMF3d</sub> | ✓ SAFE | Precision forged machined components for auto and industrial | 📈 BULL_ANY_MID | 8 | ↑98 | ↑1.060 | ↑12d | — | +23.7% | 67.24/66.4 | +1.97% | 20% |
| [KDDL](https://in.tradingview.com/chart/?symbol=NSE:KDDL)<br><sub>📶W9 · W↑11d · ↓CMF8d</sub> | ✓ SAFE | Watch dials, hands, luxury components manufacturing retail | 📈 BULL_ANY_MID | 7 | ↑92 | ↑1.071 | ↑13d | — | +30.7% | 58.6/58.07 | +3.93% | 20% |
| [LENSKART](https://in.tradingview.com/chart/?symbol=NSE:LENSKART)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Eyewear design manufacturing retail omnichannel direct consumer | 📈 BULL_ANY_MID | 5 | ↑50 | ↑1.030 | ↑30d | — | +15.9% | 64.3/61.91 | +2.24% | 20% |
| [TBOTEK](https://in.tradingview.com/chart/?symbol=NSE:TBOTEK)<br><sub>📶W9 · W↑61d · ↑CMF0d</sub> | ✓ SAFE | Global travel distribution platform for hotels airlines agents | 📈 BULL_ANY_MID | 4 | ↑76 | ↑1.050 | ↑16d | — | +19.0% | 51.05/47.71 | +4.08% | 20% |
| [HAVELLS](https://in.tradingview.com/chart/?symbol=NSE:HAVELLS)<br><sub>📶W9 · W↑46d · ↑CMF20d</sub> | ✓ SAFE | Electrical goods manufacturing and distribution for households | 📈 BULL_ANY_MID | 0 | ↑35 | ↓1.015 | ↑22d | — | +11.0% | 49.91/47.42 | +0.08% | 20% |
| [INOXWIND](https://in.tradingview.com/chart/?symbol=NSE:INOXWIND)<br><sub>🚀SS · ↓CMF30d · ÷DIV</sub> | ✓ SAFE | Wind turbine manufacturing renewable energy utilities corporates | 📈 BULL_ANY_MID | 54 | 🔄2 | ↑1.028 | ↑1d | — | +6.0% | -42.16/-46.88 | +6.05% | 20% |
| [AMBER](https://in.tradingview.com/chart/?symbol=NSE:AMBER)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Room air conditioner manufacturing and design services for brands | 📈 BULL_ANY_MID | 51 | 🔄37 | ↑1.002 | ↓9d | — | -1.8% | -40.03/-45.81 | +0.51% | 20% |
| [PSPPROJECT](https://in.tradingview.com/chart/?symbol=NSE:PSPPROJECT)<br><sub>↓CMF18d</sub> | ✓ SAFE | EPC contractor industrial institutional government residential projects | 📈 BULL_ANY_MID | 44 | 🔄72 | ↑1.003 | ↓16d | — | -8.2% | -45.02/-46.28 | +2.67% | 20% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>↓CMF29d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 40 | 🔄55 | ↑1.004 | ↓21d | — | -7.1% | -50.77/-52.92 | +2.36% | 20% |
| [PHOENIXLTD](https://in.tradingview.com/chart/?symbol=NSE:PHOENIXLTD)<br><sub>↓CMF13d</sub> | ✓ SAFE | Retail malls, office spaces, hospitality mixed-use developments | 📈 BULL_ANY_MID | 40 | 🔄64 | ↑1.005 | ↓47d | — | +11.4% | -36.65/-38.44 | +2.11% | 20% |
| [GANECOS](https://in.tradingview.com/chart/?symbol=NSE:GANECOS)<br><sub>↓CMF9d</sub> | ✓ SAFE | PET waste recycling, polyester fiber production, textile sector | 📈 BULL_ANY_MID | 40 | 🔄54 | ↑1.010 | ↓34d | — | +23.6% | -26.47/-27.32 | +3.83% | 20% 🟦 |
| [GREENPLY](https://in.tradingview.com/chart/?symbol=NSE:GREENPLY)<br><sub>↓CMF30d</sub> | ✓ SAFE | Plywood MDF panels manufacturing building construction interiors | 📈 BULL_ANY_MID | 40 | 🔄56 | ↑1.005 | ↓55d | — | +15.7% | -31.52/-32.98 | +1.90% | 20% |
| [PATANJALI](https://in.tradingview.com/chart/?symbol=NSE:PATANJALI)<br><sub>W↑11d · ↑CMF3d</sub> | ✓ SAFE | Edible oils, soybean processing, FMCG consumer goods | 📈 BULL_ANY_MID | 24 | ↓2 | ↑0.999 | ↑1d | — | +0.5% | -28.74/-29.84 | +0.54% | 20% |
| [MHRIL](https://in.tradingview.com/chart/?symbol=NSE:MHRIL)<br><sub>W↑11d · ↓CMF29d · ⚠️TRAP</sub> | ✓ SAFE | Vacation ownership memberships, resort holidays, Indian leisure travelers | 📈 BULL_ANY_MID | 18 | ↓10 | ↓0.997 | ↓2d | — | +0.5% | -1.64/-2.18 | -0.76% | 20% |
| [JSWHL](https://in.tradingview.com/chart/?symbol=NSE:JSWHL)<br><sub>W↑11d · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Investment holding company financing JSW Group operations | 📈 BULL_ANY_MID | 17 | ↓5 | ↓1.002 | ↑3d | — | +1.9% | 14.65/14.42 | -0.64% | 10% 🟩 |
| [INTERARCH](https://in.tradingview.com/chart/?symbol=NSE:INTERARCH)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Pre-engineered steel structures for warehouses factories | 📈 BULL_ANY_MID | 14 | ↓16 | ↑0.993 | ↓11d | — | -3.9% | -38.65/-38.78 | +0.15% | 20% |
| [GRAUWEIL](https://in.tradingview.com/chart/?symbol=NSE:GRAUWEIL)<br><sub>↓CMF17d</sub> | ⚠ CAUTION | Leather chemicals manufacturing industrial tanneries India | 📈 BULL_ANY_MID | 12 | ↓50 | ↑0.984 | ↓13d | — | -11.1% | -50.96/-51.6 | +0.85% | 20% |
| [HINDUNILVR](https://in.tradingview.com/chart/?symbol=NSE:HINDUNILVR)<br><sub>↓CMF29d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 10 | ↓16 | ↓0.993 | ↓10d | — | -1.4% | -44.84/-45.26 | -0.95% | 20% |
| [SATIN](https://in.tradingview.com/chart/?symbol=NSE:SATIN)<br><sub>↓CMF11d</sub> | ✓ SAFE | Microfinance loans for rural underserved borrowers | 📈 BULL_ANY_MID | 8 | ↓83 | ↑0.995 | ↓17d | — | -10.7% | -40.71/-41.9 | +1.41% | 20% |
| [SRF](https://in.tradingview.com/chart/?symbol=NSE:SRF)<br><sub>↓CMF18d</sub> | ✓ SAFE | Technical textiles, films, chemicals, foils for industrial applications | 📈 BULL_ANY_MID | 5 | ↓30 | ↑1.000 | ↓24d | — | -4.7% | -27.67/-30.26 | +0.38% | 20% |
| [JLHL](https://in.tradingview.com/chart/?symbol=NSE:JLHL)<br><sub>↑CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Tertiary quaternary hospital chain Mumbai western India | 📈 BULL_ANY_MID | 5 | ↓0 | ↑0.883 | ↓46d | — | -76.0% | -23.84/-24.05 | -0.19% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:APOLLOPIPE,NSE:AFFLE,NSE:BHAGCHEM,NSE:MONARCH,NSE:INDIGO,NSE:DYNAMATECH,NSE:GAEL,NSE:JYOTICNC,NSE:ESCORTS,NSE:POLYPLEX,NSE:ROSSTECH,NSE:SEAMECLTD,NSE:BIL,NSE:SANSERA,NSE:KDDL,NSE:LENSKART,NSE:TBOTEK,NSE:HAVELLS,NSE:INOXWIND,NSE:AMBER,NSE:PSPPROJECT,NSE:ADANIPORTS,NSE:PHOENIXLTD,NSE:GANECOS,NSE:GREENPLY,NSE:PATANJALI,NSE:MHRIL,NSE:JSWHL,NSE:INTERARCH,NSE:GRAUWEIL,NSE:HINDUNILVR,NSE:SATIN,NSE:SRF,NSE:JLHL
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
