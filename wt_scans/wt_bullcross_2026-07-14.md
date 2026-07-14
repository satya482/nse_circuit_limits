> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-07-14
*Generated 2026-07-14 15:46 IST*

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

**Total bull crosses today: 73** · 34 inside active squeeze

```
NSE:BIOCON,NSE:LANDMARK,NSE:PDSL,NSE:EIHAHOTELS,NSE:SILVERTUC,NSE:HARIOMPIPE,NSE:CONCOR,NSE:CARTRADE,NSE:ACMESOLAR,NSE:AURUM,NSE:HSCL,NSE:PRIVISCL,NSE:LLOYDSME,NSE:IDBI,NSE:ERIS,NSE:KRISHIVAL,NSE:TFCILTD,NSE:SKIPPER,NSE:PCBL,NSE:SOMANYCERA,NSE:SUDEEPPHRM,NSE:NITINSPIN,NSE:HIMATSEIDE,NSE:ROLEXRINGS,NSE:PNBGILTS,NSE:BHEL,NSE:UNIVCABLES,NSE:PIRAMALFIN,NSE:GOODYEAR,NSE:RRKABEL,NSE:GARFIBRES,NSE:ABCAPITAL,NSE:OFSS,NSE:CAPLIPOINT,NSE:BLUESTONE,NSE:TTKPRESTIG,NSE:ALIVUS,NSE:SPECTRUM,NSE:HUHTAMAKI,NSE:BASF,NSE:ICEMAKE,NSE:EUREKAFORB,NSE:HINDOILEXP,NSE:SYNGENE,NSE:PRAKASH,NSE:COALINDIA,NSE:FORTIS,NSE:SUNDROP,NSE:SCHAEFFLER,NSE:AVTNPL,NSE:HATSUN,NSE:PNB,NSE:LINDEINDIA,NSE:JPOLYINVST,NSE:AMBUJACEM,NSE:GMMPFAUDLR,NSE:LAXMIDENTL,NSE:SPMLINFRA,NSE:TITAGARH,NSE:UNIONBANK,NSE:ZEEL,NSE:HDFCLIFE,NSE:PINELABS,NSE:JBMA,NSE:HITECH,NSE:GESHIP,NSE:TMPV,NSE:FIRSTCRY,NSE:HONDAPOWER,NSE:NETWEB,NSE:KIOCL,NSE:SASKEN,NSE:SANOFICONR
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (39)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [BIOCON](https://in.tradingview.com/chart/?symbol=NSE:BIOCON)<br><sub>📶W9 · W↑52d · 🚀SS·11x · ↑CMF0d</sub> | ✓ SAFE | Insulin, oncology drugs, biologics manufacturing for chronic diseases | ⚡ BULL_ANY_PPV | 89 | 🔄75 | ↑1.048 | ↑1d | SQ·PV | +6.4% | -0.2/-11.45 | +6.41% | 20% |
| [LANDMARK](https://in.tradingview.com/chart/?symbol=NSE:LANDMARK)<br><sub>📶W9 · W↑32d · RVOL67x · ↑CMF0d</sub> | ✓ SAFE | Premium luxury car dealer multi-brand retail | ⚡ BULL_ANY_PPV | 89 | 🔄51 | ↑1.124 | ↑1d | SQ·PV | +17.4% | 17.7/8.33 | +17.38% | 20% |
| [PDSL](https://in.tradingview.com/chart/?symbol=NSE:PDSL)<br><sub>📶W9 · W↑70d · 🚀SS·35x · ↓CMF1d</sub> | ✓ SAFE | Apparel supply chain, design sourcing, manufacturing services, fashion brands | ⚡ BULL_ANY_PPV | 87 | 🔄70 | ↑1.059 | ↑3d | SQ·PV | +9.3% | 45.86/37.61 | +6.37% | 20% |
| [EIHAHOTELS](https://in.tradingview.com/chart/?symbol=NSE:EIHAHOTELS)<br><sub>📶W9 · W↑22d · ↓CMF30d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 63 | ↑30 | ↑1.020 | ↑2d | SQ·PV | +3.0% | 20.05/14.33 | +0.98% | 20% |
| [SILVERTUC](https://in.tradingview.com/chart/?symbol=NSE:SILVERTUC)<br><sub>📶W9 · 🚀SS · ★ · ↑CMF0d</sub> | ✓ SAFE | Software development and digital transformation IT services | ⚡ BULL_ANY_PPV | 58 | ↑98 | ↑1.048 | ↑2d | SQ·PV | +8.9% | 8.61/1.33 | +3.75% | 20% |
| [HARIOMPIPE](https://in.tradingview.com/chart/?symbol=NSE:HARIOMPIPE)<br><sub>📶W9 · W↑61d · 🚀SS·24x · ↓CMF16d</sub> | ✓ SAFE | Steel pipe and scaffolding systems manufacturer for construction | ⚡ BULL_ANY_PPV | 54 | 🔄58 | ↑1.023 | ↑1d | PV | +4.8% | -26.85/-32.39 | +4.84% | 20% |
| [CONCOR](https://in.tradingview.com/chart/?symbol=NSE:CONCOR)<br><sub>📶W9 · W↑12d · 🚀SS·8x · ↑CMF15d</sub> | ✓ SAFE | Rail container logistics and multimodal freight transport services | ⚡ BULL_ANY_PPV | 49 | 🔄26 | ↑1.045 | ↑1d | PV | +6.3% | 5.97/0.71 | +6.29% | 20% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>📶W9 · W↑52d · ↑CMF27d</sub> | ✓ SAFE | Used car marketplace, financing, dealer-to-consumer platform | ⚡ BULL_ANY_PPV | 40 | ↑90 | ↑1.044 | ↑32d | SQ·PV | +66.8% | 54.8/51.4 | +3.42% | 20% |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>📶W9 · W↑37d · ↑CMF30d</sub> | ✓ SAFE | Solar and wind power projects, utility-scale renewable energy | ⚡ BULL_ANY_PPV | 22 | ↑90 | ↑1.025 | ↑3d | PV | +4.6% | 45.02/43.18 | +1.53% | 20% |
| [AURUM](https://in.tradingview.com/chart/?symbol=NSE:AURUM)<br><sub>📶W9 · W↑65d · 🚀SS · ↑CMF28d</sub> | ✓ SAFE | Real estate digital platform, rentals, sales, property management | ⚡ BULL_ANY_PPV | 0 | ↑85 | ↑1.056 | ↑23d | PV | +31.6% | 61.25/57.05 | +3.37% | 20% |
| [HSCL](https://in.tradingview.com/chart/?symbol=NSE:HSCL)<br><sub>📶W9 · ↓CMF7d · DEL39%</sub> | ✓ SAFE | Coal pitch and carbon materials manufacturer for industrial applications | 📈 BULL_ANY_MID | 99 | 🔄88 | ↑1.013 | ↑1d | SQ | +1.2% | 2.89/-0.57 | +1.25% | 20% |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF23d</sub> | ✓ SAFE | Fragrance and flavor chemical manufacturer for personal care | 📈 BULL_ANY_MID | 96 | 🔄86 | ↑1.013 | ↑4d | SQ | +3.8% | 36.16/32.34 | +1.66% | 20% |
| [LLOYDSME](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSME)<br><sub>📶W9 · 🚀SS · ↓CMF14d</sub> | ✓ SAFE | Iron ore mining, sponge iron production, power generation | 📈 BULL_ANY_MID | 94 | 🔄78 | ↑1.022 | ↑1d | SQ | +3.1% | 6.52/1.69 | +3.12% | 20% |
| [IDBI](https://in.tradingview.com/chart/?symbol=NSE:IDBI)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF19d</sub> | ✓ SAFE | Commercial banking, retail deposits, corporate lending, MSME focus | 📈 BULL_ANY_MID | 88 | 🔄42 | ↑1.032 | ↑2d | SQ | +4.4% | 20.19/11.98 | +2.94% | 20% 🟦 |
| [ERIS](https://in.tradingview.com/chart/?symbol=NSE:ERIS)<br><sub>📶W9 · W↑73d · ↑CMF8d</sub> | ⚠ CAUTION | Chronic disease pharma: cardiology, diabetes, gastro, derma | 📈 BULL_ANY_MID | 88 | 🔄29 | ↓1.010 | ↑2d | SQ | +1.5% | 26.27/19.77 | +0.22% | 20% |
| [KRISHIVAL](https://in.tradingview.com/chart/?symbol=NSE:KRISHIVAL)<br><sub>📶W9 · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 80 | 🔄64 | ↑1.003 | ↓60d+ | SQ | +21.9% | -23.81/-25.0 | +0.66% | 20% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>📶W9 · W↑22d · ↓CMF30d</sub> | ✓ SAFE | Tourism sector financing hotels resorts restaurants amusement parks | 📈 BULL_ANY_MID | 58 | ↑75 | ↓1.032 | ↑2d | SQ | +7.2% | 27.91/22.06 | -0.35% | 20% |
| [SKIPPER](https://in.tradingview.com/chart/?symbol=NSE:SKIPPER)<br><sub>📶W9 · W↑77d · ↓CMF15d</sub> | ✓ SAFE | Steel transmission towers, polymer pipes, infrastructure EPC | 📈 BULL_ANY_MID | 58 | ↓79 | ↓1.004 | ↑2d | SQ | +1.1% | 13.69/12.34 | -0.67% | 20% |
| [PCBL](https://in.tradingview.com/chart/?symbol=NSE:PCBL)<br><sub>📶W9 · W↑70d · ↓CMF19d</sub> | ✓ SAFE | Carbon black manufacturer tire tyre rubber chemicals | 📈 BULL_ANY_MID | 58 | ↑40 | ↓1.014 | ↑2d | SQ | +3.0% | 21.78/17.51 | -1.44% | 20% |
| [SOMANYCERA](https://in.tradingview.com/chart/?symbol=NSE:SOMANYCERA)<br><sub>📶W9 · W↑73d · ↓CMF20d</sub> | ✓ SAFE | Ceramic tiles sanitaryware bath fittings residential commercial construction | 📈 BULL_ANY_MID | 58 | ↑70 | ↓1.019 | ↑2d | SQ | +3.0% | 27.89/21.5 | -0.31% | 20% |
| [SUDEEPPHRM](https://in.tradingview.com/chart/?symbol=NSE:SUDEEPPHRM)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Mineral excipients and calcium phosphates for pharmaceuticals food nutrition | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.011 | ↑2d | SQ | +1.7% | 21.05/18.86 | -0.74% | 20% |
| [NITINSPIN](https://in.tradingview.com/chart/?symbol=NSE:NITINSPIN)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Cotton yarn and fabric manufacturer for apparel | 📈 BULL_ANY_MID | 58 | ↓93 | ↓1.003 | ↓2d | SQ | +2.1% | 13.76/11.14 | -1.53% | 20% |
| [HIMATSEIDE](https://in.tradingview.com/chart/?symbol=NSE:HIMATSEIDE)<br><sub>📶W9 · W↑22d · ↓CMF30d</sub> | ✓ SAFE | Integrated home textiles bedding bath drapes global export | 📈 BULL_ANY_MID | 57 | ↓8 | ↓1.002 | ↑3d | SQ | +2.2% | 20.11/17.18 | -2.05% | 20% |
| [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS)<br><sub>📶W9 · ↑CMF3d</sub> | ✓ SAFE | Forged automotive bearing rings machined components global supplier | 📈 BULL_ANY_MID | 53 | 🔄58 | ↑1.021 | ↑2d | — | +3.9% | 3.6/0.1 | +1.85% | 20% |
| [PNBGILTS](https://in.tradingview.com/chart/?symbol=NSE:PNBGILTS)<br><sub>📶W9 · W↑65d · ↓CMF8d</sub> | ✓ SAFE | Government securities dealer, primary dealer, debt market | 📈 BULL_ANY_MID | 51 | ↓54 | ↓0.997 | ↓9d | SQ | -2.3% | -20.77/-20.96 | -0.94% | 20% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄91 | ↑1.037 | ↑1d | — | +3.4% | -7.35/-13.15 | +3.43% | 20% |
| [UNIVCABLES](https://in.tradingview.com/chart/?symbol=NSE:UNIVCABLES)<br><sub>📶W9 · ↓CMF16d</sub> | ✓ SAFE | Power cables, wires, capacitors for electrical infrastructure | 📈 BULL_ANY_MID | 49 | 🔄94 | ↑1.040 | ↑1d | — | +4.1% | -20.62/-26.65 | +4.11% | 20% |
| [PIRAMALFIN](https://in.tradingview.com/chart/?symbol=NSE:PIRAMALFIN)<br><sub>📶W9 · 🚀SS · ↓CMF1d</sub> | ⚠ CAUTION | NBFC retail mortgage loans property financing India | 📈 BULL_ANY_MID | 47 | 🔄50 | ↓1.005 | ↑3d | — | +2.4% | 45.9/45.85 | -0.09% | 20% |
| [GOODYEAR](https://in.tradingview.com/chart/?symbol=NSE:GOODYEAR)<br><sub>📶W9 · W↑17d · ↓CMF9d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 40 | 🔄50 | ↑1.015 | ↑30d | — | +9.7% | 40.95/40.88 | +0.71% | 20% |
| [RRKABEL](https://in.tradingview.com/chart/?symbol=NSE:RRKABEL)<br><sub>📶W9 · ↓CMF9d</sub> | ✓ SAFE | Wires cables electrical distribution residential commercial industrial | 📈 BULL_ANY_MID | 18 | ↑96 | ↓1.018 | ↑2d | — | +5.4% | 7.41/4.39 | -1.24% | 20% |
| [GARFIBRES](https://in.tradingview.com/chart/?symbol=NSE:GARFIBRES)<br><sub>📶W9 · W↑70d · ↑CMF28d</sub> | ✓ SAFE | Technical textiles and ropes for agriculture aquaculture infrastructure | 📈 BULL_ANY_MID | 18 | ↑56 | ↑1.031 | ↑2d | — | +4.2% | 24.06/15.79 | +2.13% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑63d · ↑CMF16d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.020 | ↑3d | — | +5.4% | 47.71/46.67 | -0.44% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Banking software solutions for financial institutions | 📈 BULL_ANY_MID | 5 | ↑90 | ↑1.055 | ↑15d | — | +20.9% | 50.17/48.27 | +4.64% | 20% |
| [CAPLIPOINT](https://in.tradingview.com/chart/?symbol=NSE:CAPLIPOINT)<br><sub>📶W9 · W↑70d · ↑CMF1d</sub> | ✓ SAFE | Pharmaceutical APIs formulations clinical research global markets | 📈 BULL_ANY_MID | 5 | ↑89 | ↑1.028 | ↑29d | — | +34.8% | 52.99/51.75 | +1.62% | 20% |
| [BLUESTONE](https://in.tradingview.com/chart/?symbol=NSE:BLUESTONE)<br><sub>📶W9 · W↑32d · ↑CMF2d</sub> | ✓ SAFE | Design-led diamond gold jewellery omni-channel retail | 📈 BULL_ANY_MID | 2 | ↑50 | ↑1.053 | ↑18d | — | +20.5% | 62.77/60.26 | +3.14% | 20% |
| [TTKPRESTIG](https://in.tradingview.com/chart/?symbol=NSE:TTKPRESTIG)<br><sub>📶W9 · W↑65d · ↑CMF16d</sub> | ✓ SAFE | Pressure cookers cookware kitchen appliances consumer durables | 📈 BULL_ANY_MID | 2 | ↑72 | ↓1.050 | ↑18d | — | +23.7% | 73.17/71.09 | -0.14% | 20% |
| [ALIVUS](https://in.tradingview.com/chart/?symbol=NSE:ALIVUS)<br><sub>📶W9 · W↑17d · ↓CMF30d</sub> | ✓ SAFE | APIs chronic disease cardiovascular oncology pharma manufacturing | 📈 BULL_ANY_MID | 0 | ↑71 | ↓1.013 | ↑23d | — | +14.2% | 48.77/48.47 | +0.10% | 20% |
| [SPECTRUM](https://in.tradingview.com/chart/?symbol=NSE:SPECTRUM)<br><sub>📶W9 · W↑47d · ↑CMF6d</sub> | ✓ SAFE | Auto electrical components injection moulding ODM manufacturer | 📈 BULL_ANY_MID | 0 | ↑95 | ↓1.044 | ↑20d | — | +28.6% | 61.21/60.09 | +0.34% | 20% |
| [HUHTAMAKI](https://in.tradingview.com/chart/?symbol=NSE:HUHTAMAKI)<br><sub>📶W9 · W↑27d · ↑CMF16d</sub> | ✓ SAFE | Flexible packaging and molded fiber for food consumption | 📈 BULL_ANY_MID | 0 | ↑52 | ↓1.026 | ↑26d | — | +30.1% | 59.43/58.18 | -2.60% | 20% |

```
NSE:BIOCON,NSE:LANDMARK,NSE:PDSL,NSE:EIHAHOTELS,NSE:SILVERTUC,NSE:HARIOMPIPE,NSE:CONCOR,NSE:CARTRADE,NSE:ACMESOLAR,NSE:AURUM,NSE:HSCL,NSE:PRIVISCL,NSE:LLOYDSME,NSE:IDBI,NSE:ERIS,NSE:KRISHIVAL,NSE:TFCILTD,NSE:SKIPPER,NSE:PCBL,NSE:SOMANYCERA,NSE:SUDEEPPHRM,NSE:NITINSPIN,NSE:HIMATSEIDE,NSE:ROLEXRINGS,NSE:PNBGILTS,NSE:BHEL,NSE:UNIVCABLES,NSE:PIRAMALFIN,NSE:GOODYEAR,NSE:RRKABEL,NSE:GARFIBRES,NSE:ABCAPITAL,NSE:OFSS,NSE:CAPLIPOINT,NSE:BLUESTONE,NSE:TTKPRESTIG,NSE:ALIVUS,NSE:SPECTRUM,NSE:HUHTAMAKI
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (50)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [BIOCON](https://in.tradingview.com/chart/?symbol=NSE:BIOCON)<br><sub>📶W9 · W↑52d · 🚀SS·11x · ↑CMF0d</sub> | ✓ SAFE | Insulin, oncology drugs, biologics manufacturing for chronic diseases | ⚡ BULL_ANY_PPV | 89 | 🔄75 | ↑1.048 | ↑1d | SQ·PV | +6.4% | -0.2/-11.45 | +6.41% | 20% |
| [LANDMARK](https://in.tradingview.com/chart/?symbol=NSE:LANDMARK)<br><sub>📶W9 · W↑32d · RVOL67x · ↑CMF0d</sub> | ✓ SAFE | Premium luxury car dealer multi-brand retail | ⚡ BULL_ANY_PPV | 89 | 🔄51 | ↑1.124 | ↑1d | SQ·PV | +17.4% | 17.7/8.33 | +17.38% | 20% |
| [PDSL](https://in.tradingview.com/chart/?symbol=NSE:PDSL)<br><sub>📶W9 · W↑70d · 🚀SS·35x · ↓CMF1d</sub> | ✓ SAFE | Apparel supply chain, design sourcing, manufacturing services, fashion brands | ⚡ BULL_ANY_PPV | 87 | 🔄70 | ↑1.059 | ↑3d | SQ·PV | +9.3% | 45.86/37.61 | +6.37% | 20% |
| [EIHAHOTELS](https://in.tradingview.com/chart/?symbol=NSE:EIHAHOTELS)<br><sub>📶W9 · W↑22d · ↓CMF30d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 63 | ↑30 | ↑1.020 | ↑2d | SQ·PV | +3.0% | 20.05/14.33 | +0.98% | 20% |
| [SILVERTUC](https://in.tradingview.com/chart/?symbol=NSE:SILVERTUC)<br><sub>📶W9 · 🚀SS · ★ · ↑CMF0d</sub> | ✓ SAFE | Software development and digital transformation IT services | ⚡ BULL_ANY_PPV | 58 | ↑98 | ↑1.048 | ↑2d | SQ·PV | +8.9% | 8.61/1.33 | +3.75% | 20% |
| [HARIOMPIPE](https://in.tradingview.com/chart/?symbol=NSE:HARIOMPIPE)<br><sub>📶W9 · W↑61d · 🚀SS·24x · ↓CMF16d</sub> | ✓ SAFE | Steel pipe and scaffolding systems manufacturer for construction | ⚡ BULL_ANY_PPV | 54 | 🔄58 | ↑1.023 | ↑1d | PV | +4.8% | -26.85/-32.39 | +4.84% | 20% |
| [CONCOR](https://in.tradingview.com/chart/?symbol=NSE:CONCOR)<br><sub>📶W9 · W↑12d · 🚀SS·8x · ↑CMF15d</sub> | ✓ SAFE | Rail container logistics and multimodal freight transport services | ⚡ BULL_ANY_PPV | 49 | 🔄26 | ↑1.045 | ↑1d | PV | +6.3% | 5.97/0.71 | +6.29% | 20% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>📶W9 · W↑52d · ↑CMF27d</sub> | ✓ SAFE | Used car marketplace, financing, dealer-to-consumer platform | ⚡ BULL_ANY_PPV | 40 | ↑90 | ↑1.044 | ↑32d | SQ·PV | +66.8% | 54.8/51.4 | +3.42% | 20% |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>📶W9 · W↑37d · ↑CMF30d</sub> | ✓ SAFE | Solar and wind power projects, utility-scale renewable energy | ⚡ BULL_ANY_PPV | 22 | ↑90 | ↑1.025 | ↑3d | PV | +4.6% | 45.02/43.18 | +1.53% | 20% |
| [AURUM](https://in.tradingview.com/chart/?symbol=NSE:AURUM)<br><sub>📶W9 · W↑65d · 🚀SS · ↑CMF28d</sub> | ✓ SAFE | Real estate digital platform, rentals, sales, property management | ⚡ BULL_ANY_PPV | 0 | ↑85 | ↑1.056 | ↑23d | PV | +31.6% | 61.25/57.05 | +3.37% | 20% |
| [HSCL](https://in.tradingview.com/chart/?symbol=NSE:HSCL)<br><sub>📶W9 · ↓CMF7d · DEL39%</sub> | ✓ SAFE | Coal pitch and carbon materials manufacturer for industrial applications | 📈 BULL_ANY_MID | 99 | 🔄88 | ↑1.013 | ↑1d | SQ | +1.2% | 2.89/-0.57 | +1.25% | 20% |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF23d</sub> | ✓ SAFE | Fragrance and flavor chemical manufacturer for personal care | 📈 BULL_ANY_MID | 96 | 🔄86 | ↑1.013 | ↑4d | SQ | +3.8% | 36.16/32.34 | +1.66% | 20% |
| [LLOYDSME](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSME)<br><sub>📶W9 · 🚀SS · ↓CMF14d</sub> | ✓ SAFE | Iron ore mining, sponge iron production, power generation | 📈 BULL_ANY_MID | 94 | 🔄78 | ↑1.022 | ↑1d | SQ | +3.1% | 6.52/1.69 | +3.12% | 20% |
| [IDBI](https://in.tradingview.com/chart/?symbol=NSE:IDBI)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF19d</sub> | ✓ SAFE | Commercial banking, retail deposits, corporate lending, MSME focus | 📈 BULL_ANY_MID | 88 | 🔄42 | ↑1.032 | ↑2d | SQ | +4.4% | 20.19/11.98 | +2.94% | 20% 🟦 |
| [ERIS](https://in.tradingview.com/chart/?symbol=NSE:ERIS)<br><sub>📶W9 · W↑73d · ↑CMF8d</sub> | ⚠ CAUTION | Chronic disease pharma: cardiology, diabetes, gastro, derma | 📈 BULL_ANY_MID | 88 | 🔄29 | ↓1.010 | ↑2d | SQ | +1.5% | 26.27/19.77 | +0.22% | 20% |
| [KRISHIVAL](https://in.tradingview.com/chart/?symbol=NSE:KRISHIVAL)<br><sub>📶W9 · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 80 | 🔄64 | ↑1.003 | ↓60d+ | SQ | +21.9% | -23.81/-25.0 | +0.66% | 20% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>📶W9 · W↑22d · ↓CMF30d</sub> | ✓ SAFE | Tourism sector financing hotels resorts restaurants amusement parks | 📈 BULL_ANY_MID | 58 | ↑75 | ↓1.032 | ↑2d | SQ | +7.2% | 27.91/22.06 | -0.35% | 20% |
| [PCBL](https://in.tradingview.com/chart/?symbol=NSE:PCBL)<br><sub>📶W9 · W↑70d · ↓CMF19d</sub> | ✓ SAFE | Carbon black manufacturer tire tyre rubber chemicals | 📈 BULL_ANY_MID | 58 | ↑40 | ↓1.014 | ↑2d | SQ | +3.0% | 21.78/17.51 | -1.44% | 20% |
| [SOMANYCERA](https://in.tradingview.com/chart/?symbol=NSE:SOMANYCERA)<br><sub>📶W9 · W↑73d · ↓CMF20d</sub> | ✓ SAFE | Ceramic tiles sanitaryware bath fittings residential commercial construction | 📈 BULL_ANY_MID | 58 | ↑70 | ↓1.019 | ↑2d | SQ | +3.0% | 27.89/21.5 | -0.31% | 20% |
| [SUDEEPPHRM](https://in.tradingview.com/chart/?symbol=NSE:SUDEEPPHRM)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Mineral excipients and calcium phosphates for pharmaceuticals food nutrition | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.011 | ↑2d | SQ | +1.7% | 21.05/18.86 | -0.74% | 20% |
| [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS)<br><sub>📶W9 · ↑CMF3d</sub> | ✓ SAFE | Forged automotive bearing rings machined components global supplier | 📈 BULL_ANY_MID | 53 | 🔄58 | ↑1.021 | ↑2d | — | +3.9% | 3.6/0.1 | +1.85% | 20% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄91 | ↑1.037 | ↑1d | — | +3.4% | -7.35/-13.15 | +3.43% | 20% |
| [UNIVCABLES](https://in.tradingview.com/chart/?symbol=NSE:UNIVCABLES)<br><sub>📶W9 · ↓CMF16d</sub> | ✓ SAFE | Power cables, wires, capacitors for electrical infrastructure | 📈 BULL_ANY_MID | 49 | 🔄94 | ↑1.040 | ↑1d | — | +4.1% | -20.62/-26.65 | +4.11% | 20% |
| [PIRAMALFIN](https://in.tradingview.com/chart/?symbol=NSE:PIRAMALFIN)<br><sub>📶W9 · 🚀SS · ↓CMF1d</sub> | ⚠ CAUTION | NBFC retail mortgage loans property financing India | 📈 BULL_ANY_MID | 47 | 🔄50 | ↓1.005 | ↑3d | — | +2.4% | 45.9/45.85 | -0.09% | 20% |
| [GOODYEAR](https://in.tradingview.com/chart/?symbol=NSE:GOODYEAR)<br><sub>📶W9 · W↑17d · ↓CMF9d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 40 | 🔄50 | ↑1.015 | ↑30d | — | +9.7% | 40.95/40.88 | +0.71% | 20% |
| [RRKABEL](https://in.tradingview.com/chart/?symbol=NSE:RRKABEL)<br><sub>📶W9 · ↓CMF9d</sub> | ✓ SAFE | Wires cables electrical distribution residential commercial industrial | 📈 BULL_ANY_MID | 18 | ↑96 | ↓1.018 | ↑2d | — | +5.4% | 7.41/4.39 | -1.24% | 20% |
| [GARFIBRES](https://in.tradingview.com/chart/?symbol=NSE:GARFIBRES)<br><sub>📶W9 · W↑70d · ↑CMF28d</sub> | ✓ SAFE | Technical textiles and ropes for agriculture aquaculture infrastructure | 📈 BULL_ANY_MID | 18 | ↑56 | ↑1.031 | ↑2d | — | +4.2% | 24.06/15.79 | +2.13% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑63d · ↑CMF16d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.020 | ↑3d | — | +5.4% | 47.71/46.67 | -0.44% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Banking software solutions for financial institutions | 📈 BULL_ANY_MID | 5 | ↑90 | ↑1.055 | ↑15d | — | +20.9% | 50.17/48.27 | +4.64% | 20% |
| [CAPLIPOINT](https://in.tradingview.com/chart/?symbol=NSE:CAPLIPOINT)<br><sub>📶W9 · W↑70d · ↑CMF1d</sub> | ✓ SAFE | Pharmaceutical APIs formulations clinical research global markets | 📈 BULL_ANY_MID | 5 | ↑89 | ↑1.028 | ↑29d | — | +34.8% | 52.99/51.75 | +1.62% | 20% |
| [BLUESTONE](https://in.tradingview.com/chart/?symbol=NSE:BLUESTONE)<br><sub>📶W9 · W↑32d · ↑CMF2d</sub> | ✓ SAFE | Design-led diamond gold jewellery omni-channel retail | 📈 BULL_ANY_MID | 2 | ↑50 | ↑1.053 | ↑18d | — | +20.5% | 62.77/60.26 | +3.14% | 20% |
| [TTKPRESTIG](https://in.tradingview.com/chart/?symbol=NSE:TTKPRESTIG)<br><sub>📶W9 · W↑65d · ↑CMF16d</sub> | ✓ SAFE | Pressure cookers cookware kitchen appliances consumer durables | 📈 BULL_ANY_MID | 2 | ↑72 | ↓1.050 | ↑18d | — | +23.7% | 73.17/71.09 | -0.14% | 20% |
| [ALIVUS](https://in.tradingview.com/chart/?symbol=NSE:ALIVUS)<br><sub>📶W9 · W↑17d · ↓CMF30d</sub> | ✓ SAFE | APIs chronic disease cardiovascular oncology pharma manufacturing | 📈 BULL_ANY_MID | 0 | ↑71 | ↓1.013 | ↑23d | — | +14.2% | 48.77/48.47 | +0.10% | 20% |
| [SPECTRUM](https://in.tradingview.com/chart/?symbol=NSE:SPECTRUM)<br><sub>📶W9 · W↑47d · ↑CMF6d</sub> | ✓ SAFE | Auto electrical components injection moulding ODM manufacturer | 📈 BULL_ANY_MID | 0 | ↑95 | ↓1.044 | ↑20d | — | +28.6% | 61.21/60.09 | +0.34% | 20% |
| [HUHTAMAKI](https://in.tradingview.com/chart/?symbol=NSE:HUHTAMAKI)<br><sub>📶W9 · W↑27d · ↑CMF16d</sub> | ✓ SAFE | Flexible packaging and molded fiber for food consumption | 📈 BULL_ANY_MID | 0 | ↑52 | ↓1.026 | ↑26d | — | +30.1% | 59.43/58.18 | -2.60% | 20% |
| [BASF](https://in.tradingview.com/chart/?symbol=NSE:BASF)<br><sub>W↑17d · ↑CMF16d</sub> | ⚠ CAUTION | Chemical manufacturing, catalysts, plastics, agricultural inputs, automotive | ⚡ BULL_ANY_PPV | 99 | 🔄18 | ↑1.015 | ↑1d | SQ·PV | +2.6% | -3.4/-4.27 | +2.57% | 20% |
| [ICEMAKE](https://in.tradingview.com/chart/?symbol=NSE:ICEMAKE)<br><sub>↓CMF15d</sub> | ✓ SAFE | Refrigeration equipment manufacturer for commercial cold storage operations | ⚡ BULL_ANY_PPV | 94 | 🔄46 | ↑1.020 | ↑1d | SQ·PV | +2.8% | -7.55/-11.11 | +2.82% | 20% |
| [EUREKAFORB](https://in.tradingview.com/chart/?symbol=NSE:EUREKAFORB)<br><sub>W↑17d · ↓CMF30d</sub> | ⚠ CAUTION | Water purification systems and vacuum cleaners India | ⚡ BULL_ANY_PPV | 93 | 🔄17 | ↑1.020 | ↑2d | SQ·PV | +3.7% | 0.64/-3.59 | +2.00% | 20% |
| [FORTIS](https://in.tradingview.com/chart/?symbol=NSE:FORTIS)<br><sub>W↑65d · ↓CMF7d</sub> | ✓ SAFE | Hospital chain, diagnostics, multi-specialty tertiary quaternary care | 📈 BULL_ANY_MID | 99 | 🔄60 | ↑1.006 | ↑1d | SQ | +0.7% | -2.15/-4.4 | +0.65% | 20% |
| [SUNDROP](https://in.tradingview.com/chart/?symbol=NSE:SUNDROP)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄22 | ↑1.005 | ↑1d | SQ | +1.0% | -50.01/-52.97 | +1.00% | 20% |
| [SCHAEFFLER](https://in.tradingview.com/chart/?symbol=NSE:SCHAEFFLER)<br><sub>↓CMF15d</sub> | ⚠ CAUTION | Precision bearings, engine systems, automotive and industrial components | 📈 BULL_ANY_MID | 98 | 🔄49 | ↑1.004 | ↑2d | SQ | +1.3% | -17.19/-21.51 | +0.11% | 20% |
| [AVTNPL](https://in.tradingview.com/chart/?symbol=NSE:AVTNPL)<br><sub>W↑70d · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 98 | 🔄58 | ↑1.010 | ↑2d | SQ | +1.8% | -0.03/-8.95 | +0.34% | 20% |
| [HATSUN](https://in.tradingview.com/chart/?symbol=NSE:HATSUN)<br><sub>W↑2d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄42 | ↑1.024 | ↑1d | SQ | +3.5% | -13.98/-25.02 | +3.50% | 20% |
| [PNB](https://in.tradingview.com/chart/?symbol=NSE:PNB)<br><sub>W↑25d · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | 🔄25 | ↑1.012 | ↑2d | — | +2.9% | -19.58/-24.31 | +0.94% | 20% |
| [JPOLYINVST](https://in.tradingview.com/chart/?symbol=NSE:JPOLYINVST)<br><sub>W↑27d · ↓CMF26d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | ↑58 | ↓1.006 | ↑2d | SQ | +1.7% | 7.11/3.06 | -1.08% | 20% |
| [GMMPFAUDLR](https://in.tradingview.com/chart/?symbol=NSE:GMMPFAUDLR)<br><sub>W↑2d · ↓CMF30d</sub> | ⚠ CAUTION | Glass-lined chemical reactors and equipment manufacturing | 📈 BULL_ANY_MID | 54 | 🔄4 | ↑1.017 | ↑1d | — | +1.8% | -31.59/-36.58 | +1.80% | 20% |
| [TITAGARH](https://in.tradingview.com/chart/?symbol=NSE:TITAGARH)<br><sub>↓CMF10d</sub> | ✓ SAFE | Rail coaches wagons metro trains manufacturing | 📈 BULL_ANY_MID | 50 | 🔄53 | ↑1.004 | ↓10d | — | -2.4% | -26.79/-26.96 | +1.11% | 20% |
| [UNIONBANK](https://in.tradingview.com/chart/?symbol=NSE:UNIONBANK)<br><sub>↑CMF1d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄50 | ↑1.036 | ↑1d | — | +3.7% | -21.82/-27.26 | +3.73% | 20% |
| [ZEEL](https://in.tradingview.com/chart/?symbol=NSE:ZEEL)<br><sub>↓CMF3d</sub> | ✓ SAFE | TV channels, streaming, films, music production and distribution | 📈 BULL_ANY_MID | 40 | 🔄57 | ↑1.004 | ↓35d | — | +24.6% | -28.08/-28.12 | +1.77% | 20% |
| [PINELABS](https://in.tradingview.com/chart/?symbol=NSE:PINELABS)<br><sub>↑CMF1d</sub> | ✓ SAFE | POS terminals, payment processing, merchant financing ecosystem | 📈 BULL_ANY_MID | 18 | ↑50 | ↑1.035 | ↑2d | — | +7.9% | -2.6/-8.75 | +0.84% | 20% |

```
NSE:BIOCON,NSE:LANDMARK,NSE:PDSL,NSE:EIHAHOTELS,NSE:SILVERTUC,NSE:HARIOMPIPE,NSE:CONCOR,NSE:CARTRADE,NSE:ACMESOLAR,NSE:AURUM,NSE:HSCL,NSE:PRIVISCL,NSE:LLOYDSME,NSE:IDBI,NSE:ERIS,NSE:KRISHIVAL,NSE:TFCILTD,NSE:PCBL,NSE:SOMANYCERA,NSE:SUDEEPPHRM,NSE:ROLEXRINGS,NSE:BHEL,NSE:UNIVCABLES,NSE:PIRAMALFIN,NSE:GOODYEAR,NSE:RRKABEL,NSE:GARFIBRES,NSE:ABCAPITAL,NSE:OFSS,NSE:CAPLIPOINT,NSE:BLUESTONE,NSE:TTKPRESTIG,NSE:ALIVUS,NSE:SPECTRUM,NSE:HUHTAMAKI,NSE:BASF,NSE:ICEMAKE,NSE:EUREKAFORB,NSE:FORTIS,NSE:SUNDROP,NSE:SCHAEFFLER,NSE:AVTNPL,NSE:HATSUN,NSE:PNB,NSE:JPOLYINVST,NSE:GMMPFAUDLR,NSE:TITAGARH,NSE:UNIONBANK,NSE:ZEEL,NSE:PINELABS
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (34)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [BIOCON](https://in.tradingview.com/chart/?symbol=NSE:BIOCON)<br><sub>📶W9 · W↑52d · 🚀SS·11x · ↑CMF0d</sub> | ✓ SAFE | Insulin, oncology drugs, biologics manufacturing for chronic diseases | ⚡ BULL_ANY_PPV | 89 | 🔄75 | ↑1.048 | ↑1d | SQ·PV | +6.4% | -0.2/-11.45 | +6.41% | 20% |
| [LANDMARK](https://in.tradingview.com/chart/?symbol=NSE:LANDMARK)<br><sub>📶W9 · W↑32d · RVOL67x · ↑CMF0d</sub> | ✓ SAFE | Premium luxury car dealer multi-brand retail | ⚡ BULL_ANY_PPV | 89 | 🔄51 | ↑1.124 | ↑1d | SQ·PV | +17.4% | 17.7/8.33 | +17.38% | 20% |
| [PDSL](https://in.tradingview.com/chart/?symbol=NSE:PDSL)<br><sub>📶W9 · W↑70d · 🚀SS·35x · ↓CMF1d</sub> | ✓ SAFE | Apparel supply chain, design sourcing, manufacturing services, fashion brands | ⚡ BULL_ANY_PPV | 87 | 🔄70 | ↑1.059 | ↑3d | SQ·PV | +9.3% | 45.86/37.61 | +6.37% | 20% |
| [EIHAHOTELS](https://in.tradingview.com/chart/?symbol=NSE:EIHAHOTELS)<br><sub>📶W9 · W↑22d · ↓CMF30d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 63 | ↑30 | ↑1.020 | ↑2d | SQ·PV | +3.0% | 20.05/14.33 | +0.98% | 20% |
| [SILVERTUC](https://in.tradingview.com/chart/?symbol=NSE:SILVERTUC)<br><sub>📶W9 · 🚀SS · ★ · ↑CMF0d</sub> | ✓ SAFE | Software development and digital transformation IT services | ⚡ BULL_ANY_PPV | 58 | ↑98 | ↑1.048 | ↑2d | SQ·PV | +8.9% | 8.61/1.33 | +3.75% | 20% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>📶W9 · W↑52d · ↑CMF27d</sub> | ✓ SAFE | Used car marketplace, financing, dealer-to-consumer platform | ⚡ BULL_ANY_PPV | 40 | ↑90 | ↑1.044 | ↑32d | SQ·PV | +66.8% | 54.8/51.4 | +3.42% | 20% |
| [HSCL](https://in.tradingview.com/chart/?symbol=NSE:HSCL)<br><sub>📶W9 · ↓CMF7d · DEL39%</sub> | ✓ SAFE | Coal pitch and carbon materials manufacturer for industrial applications | 📈 BULL_ANY_MID | 99 | 🔄88 | ↑1.013 | ↑1d | SQ | +1.2% | 2.89/-0.57 | +1.25% | 20% |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF23d</sub> | ✓ SAFE | Fragrance and flavor chemical manufacturer for personal care | 📈 BULL_ANY_MID | 96 | 🔄86 | ↑1.013 | ↑4d | SQ | +3.8% | 36.16/32.34 | +1.66% | 20% |
| [LLOYDSME](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSME)<br><sub>📶W9 · 🚀SS · ↓CMF14d</sub> | ✓ SAFE | Iron ore mining, sponge iron production, power generation | 📈 BULL_ANY_MID | 94 | 🔄78 | ↑1.022 | ↑1d | SQ | +3.1% | 6.52/1.69 | +3.12% | 20% |
| [IDBI](https://in.tradingview.com/chart/?symbol=NSE:IDBI)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF19d</sub> | ✓ SAFE | Commercial banking, retail deposits, corporate lending, MSME focus | 📈 BULL_ANY_MID | 88 | 🔄42 | ↑1.032 | ↑2d | SQ | +4.4% | 20.19/11.98 | +2.94% | 20% 🟦 |
| [ERIS](https://in.tradingview.com/chart/?symbol=NSE:ERIS)<br><sub>📶W9 · W↑73d · ↑CMF8d</sub> | ⚠ CAUTION | Chronic disease pharma: cardiology, diabetes, gastro, derma | 📈 BULL_ANY_MID | 88 | 🔄29 | ↓1.010 | ↑2d | SQ | +1.5% | 26.27/19.77 | +0.22% | 20% |
| [KRISHIVAL](https://in.tradingview.com/chart/?symbol=NSE:KRISHIVAL)<br><sub>📶W9 · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 80 | 🔄64 | ↑1.003 | ↓60d+ | SQ | +21.9% | -23.81/-25.0 | +0.66% | 20% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>📶W9 · W↑22d · ↓CMF30d</sub> | ✓ SAFE | Tourism sector financing hotels resorts restaurants amusement parks | 📈 BULL_ANY_MID | 58 | ↑75 | ↓1.032 | ↑2d | SQ | +7.2% | 27.91/22.06 | -0.35% | 20% |
| [SKIPPER](https://in.tradingview.com/chart/?symbol=NSE:SKIPPER)<br><sub>📶W9 · W↑77d · ↓CMF15d</sub> | ✓ SAFE | Steel transmission towers, polymer pipes, infrastructure EPC | 📈 BULL_ANY_MID | 58 | ↓79 | ↓1.004 | ↑2d | SQ | +1.1% | 13.69/12.34 | -0.67% | 20% |
| [PCBL](https://in.tradingview.com/chart/?symbol=NSE:PCBL)<br><sub>📶W9 · W↑70d · ↓CMF19d</sub> | ✓ SAFE | Carbon black manufacturer tire tyre rubber chemicals | 📈 BULL_ANY_MID | 58 | ↑40 | ↓1.014 | ↑2d | SQ | +3.0% | 21.78/17.51 | -1.44% | 20% |
| [SOMANYCERA](https://in.tradingview.com/chart/?symbol=NSE:SOMANYCERA)<br><sub>📶W9 · W↑73d · ↓CMF20d</sub> | ✓ SAFE | Ceramic tiles sanitaryware bath fittings residential commercial construction | 📈 BULL_ANY_MID | 58 | ↑70 | ↓1.019 | ↑2d | SQ | +3.0% | 27.89/21.5 | -0.31% | 20% |
| [SUDEEPPHRM](https://in.tradingview.com/chart/?symbol=NSE:SUDEEPPHRM)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Mineral excipients and calcium phosphates for pharmaceuticals food nutrition | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.011 | ↑2d | SQ | +1.7% | 21.05/18.86 | -0.74% | 20% |
| [NITINSPIN](https://in.tradingview.com/chart/?symbol=NSE:NITINSPIN)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Cotton yarn and fabric manufacturer for apparel | 📈 BULL_ANY_MID | 58 | ↓93 | ↓1.003 | ↓2d | SQ | +2.1% | 13.76/11.14 | -1.53% | 20% |
| [HIMATSEIDE](https://in.tradingview.com/chart/?symbol=NSE:HIMATSEIDE)<br><sub>📶W9 · W↑22d · ↓CMF30d</sub> | ✓ SAFE | Integrated home textiles bedding bath drapes global export | 📈 BULL_ANY_MID | 57 | ↓8 | ↓1.002 | ↑3d | SQ | +2.2% | 20.11/17.18 | -2.05% | 20% |
| [PNBGILTS](https://in.tradingview.com/chart/?symbol=NSE:PNBGILTS)<br><sub>📶W9 · W↑65d · ↓CMF8d</sub> | ✓ SAFE | Government securities dealer, primary dealer, debt market | 📈 BULL_ANY_MID | 51 | ↓54 | ↓0.997 | ↓9d | SQ | -2.3% | -20.77/-20.96 | -0.94% | 20% |
| [BASF](https://in.tradingview.com/chart/?symbol=NSE:BASF)<br><sub>W↑17d · ↑CMF16d</sub> | ⚠ CAUTION | Chemical manufacturing, catalysts, plastics, agricultural inputs, automotive | ⚡ BULL_ANY_PPV | 99 | 🔄18 | ↑1.015 | ↑1d | SQ·PV | +2.6% | -3.4/-4.27 | +2.57% | 20% |
| [ICEMAKE](https://in.tradingview.com/chart/?symbol=NSE:ICEMAKE)<br><sub>↓CMF15d</sub> | ✓ SAFE | Refrigeration equipment manufacturer for commercial cold storage operations | ⚡ BULL_ANY_PPV | 94 | 🔄46 | ↑1.020 | ↑1d | SQ·PV | +2.8% | -7.55/-11.11 | +2.82% | 20% |
| [EUREKAFORB](https://in.tradingview.com/chart/?symbol=NSE:EUREKAFORB)<br><sub>W↑17d · ↓CMF30d</sub> | ⚠ CAUTION | Water purification systems and vacuum cleaners India | ⚡ BULL_ANY_PPV | 93 | 🔄17 | ↑1.020 | ↑2d | SQ·PV | +3.7% | 0.64/-3.59 | +2.00% | 20% |
| [HINDOILEXP](https://in.tradingview.com/chart/?symbol=NSE:HINDOILEXP)<br><sub>↓CMF30d</sub> | ✓ SAFE | Crude oil natural gas exploration production onshore offshore | ⚡ BULL_ANY_PPV | 45 | ↓37 | ↑0.998 | ↓31d | SQ·PV | -5.4% | -42.46/-43.05 | +1.10% | 20% |
| [FORTIS](https://in.tradingview.com/chart/?symbol=NSE:FORTIS)<br><sub>W↑65d · ↓CMF7d</sub> | ✓ SAFE | Hospital chain, diagnostics, multi-specialty tertiary quaternary care | 📈 BULL_ANY_MID | 99 | 🔄60 | ↑1.006 | ↑1d | SQ | +0.7% | -2.15/-4.4 | +0.65% | 20% |
| [SUNDROP](https://in.tradingview.com/chart/?symbol=NSE:SUNDROP)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄22 | ↑1.005 | ↑1d | SQ | +1.0% | -50.01/-52.97 | +1.00% | 20% |
| [SCHAEFFLER](https://in.tradingview.com/chart/?symbol=NSE:SCHAEFFLER)<br><sub>↓CMF15d</sub> | ⚠ CAUTION | Precision bearings, engine systems, automotive and industrial components | 📈 BULL_ANY_MID | 98 | 🔄49 | ↑1.004 | ↑2d | SQ | +1.3% | -17.19/-21.51 | +0.11% | 20% |
| [AVTNPL](https://in.tradingview.com/chart/?symbol=NSE:AVTNPL)<br><sub>W↑70d · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 98 | 🔄58 | ↑1.010 | ↑2d | SQ | +1.8% | -0.03/-8.95 | +0.34% | 20% |
| [HATSUN](https://in.tradingview.com/chart/?symbol=NSE:HATSUN)<br><sub>W↑2d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄42 | ↑1.024 | ↑1d | SQ | +3.5% | -13.98/-25.02 | +3.50% | 20% |
| [LINDEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LINDEINDIA)<br><sub>↑CMF11d</sub> | ⚠ CAUTION | Industrial medical gases cryogenic plants manufacturing India | 📈 BULL_ANY_MID | 58 | ↓57 | ↓0.998 | ↓2d | SQ | +0.7% | -16.32/-17.69 | -0.46% | 20% |
| [JPOLYINVST](https://in.tradingview.com/chart/?symbol=NSE:JPOLYINVST)<br><sub>W↑27d · ↓CMF26d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | ↑58 | ↓1.006 | ↑2d | SQ | +1.7% | 7.11/3.06 | -1.08% | 20% |
| [AMBUJACEM](https://in.tradingview.com/chart/?symbol=NSE:AMBUJACEM)<br><sub>W↑15d · ↑CMF5d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↓10 | ↓1.004 | ↑3d | SQ | +2.7% | 15.62/14.01 | -0.88% | 20% |
| [LAXMIDENTL](https://in.tradingview.com/chart/?symbol=NSE:LAXMIDENTL)<br><sub>↓CMF30d</sub> | ✓ SAFE | Dental prosthetics crowns bridges dentures manufacturing India | 📈 BULL_ANY_MID | 52 | ↓15 | ↓0.999 | ↓8d | SQ | -1.6% | -25.83/-28.88 | -0.32% | 20% |
| [SPMLINFRA](https://in.tradingview.com/chart/?symbol=NSE:SPMLINFRA)<br><sub>↓CMF30d</sub> | ✓ SAFE | Water infrastructure, treatment plants, municipal sewage systems | 📈 BULL_ANY_MID | 51 | ↓27 | ↓0.992 | ↓9d | SQ | -1.7% | -30.78/-31.0 | -0.33% | 20% |

```
NSE:BIOCON,NSE:LANDMARK,NSE:PDSL,NSE:EIHAHOTELS,NSE:SILVERTUC,NSE:CARTRADE,NSE:HSCL,NSE:PRIVISCL,NSE:LLOYDSME,NSE:IDBI,NSE:ERIS,NSE:KRISHIVAL,NSE:TFCILTD,NSE:SKIPPER,NSE:PCBL,NSE:SOMANYCERA,NSE:SUDEEPPHRM,NSE:NITINSPIN,NSE:HIMATSEIDE,NSE:PNBGILTS,NSE:BASF,NSE:ICEMAKE,NSE:EUREKAFORB,NSE:HINDOILEXP,NSE:FORTIS,NSE:SUNDROP,NSE:SCHAEFFLER,NSE:AVTNPL,NSE:HATSUN,NSE:LINDEINDIA,NSE:JPOLYINVST,NSE:AMBUJACEM,NSE:LAXMIDENTL,NSE:SPMLINFRA
```

---

### 🔥 MAJOR — PPV confirmed (4)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [HARIOMPIPE](https://in.tradingview.com/chart/?symbol=NSE:HARIOMPIPE)<br><sub>📶W9 · W↑61d · 🚀SS·24x · ↓CMF16d</sub> | ✓ SAFE | Steel pipe and scaffolding systems manufacturer for construction | ⚡ BULL_ANY_PPV | 54 | 🔄58 | ↑1.023 | ↑1d | PV | +4.8% | -26.85/-32.39 | +4.84% | 20% |
| [CONCOR](https://in.tradingview.com/chart/?symbol=NSE:CONCOR)<br><sub>📶W9 · W↑12d · 🚀SS·8x · ↑CMF15d</sub> | ✓ SAFE | Rail container logistics and multimodal freight transport services | ⚡ BULL_ANY_PPV | 49 | 🔄26 | ↑1.045 | ↑1d | PV | +6.3% | 5.97/0.71 | +6.29% | 20% |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>📶W9 · W↑37d · ↑CMF30d</sub> | ✓ SAFE | Solar and wind power projects, utility-scale renewable energy | ⚡ BULL_ANY_PPV | 22 | ↑90 | ↑1.025 | ↑3d | PV | +4.6% | 45.02/43.18 | +1.53% | 20% |
| [AURUM](https://in.tradingview.com/chart/?symbol=NSE:AURUM)<br><sub>📶W9 · W↑65d · 🚀SS · ↑CMF28d</sub> | ✓ SAFE | Real estate digital platform, rentals, sales, property management | ⚡ BULL_ANY_PPV | 0 | ↑85 | ↑1.056 | ↑23d | PV | +31.6% | 61.25/57.05 | +3.37% | 20% |

```
NSE:HARIOMPIPE,NSE:CONCOR,NSE:ACMESOLAR,NSE:AURUM
```

### 🟢 OVERSOLD — reversal from −53/−60 (3)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SYNGENE](https://in.tradingview.com/chart/?symbol=NSE:SYNGENE)<br><sub>↓CMF28d · 🎯SLING</sub> | ✓ SAFE | Contract research development manufacturing pharma biotech | 🟢 BULL_OVERSOLD | 5 | ↓5 | ↑0.989 | ↓23d | — | -6.4% | -58.06/-60.7 | -0.21% | 20% |
| [PRAKASH](https://in.tradingview.com/chart/?symbol=NSE:PRAKASH)<br><sub>↓CMF11d · ⚠️TRAP</sub> | ✓ SAFE | Steel manufacturing mining power generation integrated producer | 🟢 BULL_OVERSOLD | 0 | ↓15 | ↓0.970 | ↓22d | — | -9.7% | -61.71/-62.42 | -0.80% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>↓CMF9d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 5 | ↓53 | ↑0.994 | ↓30d | — | -5.9% | -54.87/-55.01 | +0.38% | 20% |

```
NSE:SYNGENE,NSE:PRAKASH,NSE:COALINDIA
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (32)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS)<br><sub>📶W9 · ↑CMF3d</sub> | ✓ SAFE | Forged automotive bearing rings machined components global supplier | 📈 BULL_ANY_MID | 53 | 🔄58 | ↑1.021 | ↑2d | — | +3.9% | 3.6/0.1 | +1.85% | 20% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄91 | ↑1.037 | ↑1d | — | +3.4% | -7.35/-13.15 | +3.43% | 20% |
| [UNIVCABLES](https://in.tradingview.com/chart/?symbol=NSE:UNIVCABLES)<br><sub>📶W9 · ↓CMF16d</sub> | ✓ SAFE | Power cables, wires, capacitors for electrical infrastructure | 📈 BULL_ANY_MID | 49 | 🔄94 | ↑1.040 | ↑1d | — | +4.1% | -20.62/-26.65 | +4.11% | 20% |
| [PIRAMALFIN](https://in.tradingview.com/chart/?symbol=NSE:PIRAMALFIN)<br><sub>📶W9 · 🚀SS · ↓CMF1d</sub> | ⚠ CAUTION | NBFC retail mortgage loans property financing India | 📈 BULL_ANY_MID | 47 | 🔄50 | ↓1.005 | ↑3d | — | +2.4% | 45.9/45.85 | -0.09% | 20% |
| [GOODYEAR](https://in.tradingview.com/chart/?symbol=NSE:GOODYEAR)<br><sub>📶W9 · W↑17d · ↓CMF9d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 40 | 🔄50 | ↑1.015 | ↑30d | — | +9.7% | 40.95/40.88 | +0.71% | 20% |
| [RRKABEL](https://in.tradingview.com/chart/?symbol=NSE:RRKABEL)<br><sub>📶W9 · ↓CMF9d</sub> | ✓ SAFE | Wires cables electrical distribution residential commercial industrial | 📈 BULL_ANY_MID | 18 | ↑96 | ↓1.018 | ↑2d | — | +5.4% | 7.41/4.39 | -1.24% | 20% |
| [GARFIBRES](https://in.tradingview.com/chart/?symbol=NSE:GARFIBRES)<br><sub>📶W9 · W↑70d · ↑CMF28d</sub> | ✓ SAFE | Technical textiles and ropes for agriculture aquaculture infrastructure | 📈 BULL_ANY_MID | 18 | ↑56 | ↑1.031 | ↑2d | — | +4.2% | 24.06/15.79 | +2.13% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑63d · ↑CMF16d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.020 | ↑3d | — | +5.4% | 47.71/46.67 | -0.44% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑75d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Banking software solutions for financial institutions | 📈 BULL_ANY_MID | 5 | ↑90 | ↑1.055 | ↑15d | — | +20.9% | 50.17/48.27 | +4.64% | 20% |
| [CAPLIPOINT](https://in.tradingview.com/chart/?symbol=NSE:CAPLIPOINT)<br><sub>📶W9 · W↑70d · ↑CMF1d</sub> | ✓ SAFE | Pharmaceutical APIs formulations clinical research global markets | 📈 BULL_ANY_MID | 5 | ↑89 | ↑1.028 | ↑29d | — | +34.8% | 52.99/51.75 | +1.62% | 20% |
| [BLUESTONE](https://in.tradingview.com/chart/?symbol=NSE:BLUESTONE)<br><sub>📶W9 · W↑32d · ↑CMF2d</sub> | ✓ SAFE | Design-led diamond gold jewellery omni-channel retail | 📈 BULL_ANY_MID | 2 | ↑50 | ↑1.053 | ↑18d | — | +20.5% | 62.77/60.26 | +3.14% | 20% |
| [TTKPRESTIG](https://in.tradingview.com/chart/?symbol=NSE:TTKPRESTIG)<br><sub>📶W9 · W↑65d · ↑CMF16d</sub> | ✓ SAFE | Pressure cookers cookware kitchen appliances consumer durables | 📈 BULL_ANY_MID | 2 | ↑72 | ↓1.050 | ↑18d | — | +23.7% | 73.17/71.09 | -0.14% | 20% |
| [ALIVUS](https://in.tradingview.com/chart/?symbol=NSE:ALIVUS)<br><sub>📶W9 · W↑17d · ↓CMF30d</sub> | ✓ SAFE | APIs chronic disease cardiovascular oncology pharma manufacturing | 📈 BULL_ANY_MID | 0 | ↑71 | ↓1.013 | ↑23d | — | +14.2% | 48.77/48.47 | +0.10% | 20% |
| [SPECTRUM](https://in.tradingview.com/chart/?symbol=NSE:SPECTRUM)<br><sub>📶W9 · W↑47d · ↑CMF6d</sub> | ✓ SAFE | Auto electrical components injection moulding ODM manufacturer | 📈 BULL_ANY_MID | 0 | ↑95 | ↓1.044 | ↑20d | — | +28.6% | 61.21/60.09 | +0.34% | 20% |
| [HUHTAMAKI](https://in.tradingview.com/chart/?symbol=NSE:HUHTAMAKI)<br><sub>📶W9 · W↑27d · ↑CMF16d</sub> | ✓ SAFE | Flexible packaging and molded fiber for food consumption | 📈 BULL_ANY_MID | 0 | ↑52 | ↓1.026 | ↑26d | — | +30.1% | 59.43/58.18 | -2.60% | 20% |
| [PNB](https://in.tradingview.com/chart/?symbol=NSE:PNB)<br><sub>W↑25d · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | 🔄25 | ↑1.012 | ↑2d | — | +2.9% | -19.58/-24.31 | +0.94% | 20% |
| [GMMPFAUDLR](https://in.tradingview.com/chart/?symbol=NSE:GMMPFAUDLR)<br><sub>W↑2d · ↓CMF30d</sub> | ⚠ CAUTION | Glass-lined chemical reactors and equipment manufacturing | 📈 BULL_ANY_MID | 54 | 🔄4 | ↑1.017 | ↑1d | — | +1.8% | -31.59/-36.58 | +1.80% | 20% |
| [TITAGARH](https://in.tradingview.com/chart/?symbol=NSE:TITAGARH)<br><sub>↓CMF10d</sub> | ✓ SAFE | Rail coaches wagons metro trains manufacturing | 📈 BULL_ANY_MID | 50 | 🔄53 | ↑1.004 | ↓10d | — | -2.4% | -26.79/-26.96 | +1.11% | 20% |
| [UNIONBANK](https://in.tradingview.com/chart/?symbol=NSE:UNIONBANK)<br><sub>↑CMF1d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄50 | ↑1.036 | ↑1d | — | +3.7% | -21.82/-27.26 | +3.73% | 20% |
| [ZEEL](https://in.tradingview.com/chart/?symbol=NSE:ZEEL)<br><sub>↓CMF3d</sub> | ✓ SAFE | TV channels, streaming, films, music production and distribution | 📈 BULL_ANY_MID | 40 | 🔄57 | ↑1.004 | ↓35d | — | +24.6% | -28.08/-28.12 | +1.77% | 20% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>W↑1d · ↓CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 29 | ↓8 | ↑1.008 | ↑1d | — | +1.0% | -31.34/-34.03 | +1.02% | 20% |
| [PINELABS](https://in.tradingview.com/chart/?symbol=NSE:PINELABS)<br><sub>↑CMF1d</sub> | ✓ SAFE | POS terminals, payment processing, merchant financing ecosystem | 📈 BULL_ANY_MID | 18 | ↑50 | ↑1.035 | ↑2d | — | +7.9% | -2.6/-8.75 | +0.84% | 20% |
| [JBMA](https://in.tradingview.com/chart/?symbol=NSE:JBMA)<br><sub>↑CMF8d</sub> | ✓ SAFE | Auto components, buses, electric vehicles, sheet metal manufacturing | 📈 BULL_ANY_MID | 18 | ↓59 | ↓0.997 | ↓2d | — | -0.1% | -4.15/-4.52 | -1.79% | 20% |
| [HITECH](https://in.tradingview.com/chart/?symbol=NSE:HITECH)<br><sub>↓CMF4d · ⚠️TRAP</sub> | ✓ SAFE | ERW steel pipes tubes for construction infrastructure automotive | 📈 BULL_ANY_MID | 18 | ↓24 | ↓0.990 | ↓2d | — | -0.0% | -23.14/-24.76 | -2.47% | 20% |
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP)<br><sub>🚀SS · ↓CMF0d</sub> | ✓ SAFE | Shipping tankers crude oil petroleum products oilfield services | 📈 BULL_ANY_MID | 13 | ↓76 | ↑1.000 | ↓17d | — | -1.3% | -21.99/-24.72 | +1.20% | 20% |
| [TMPV](https://in.tradingview.com/chart/?symbol=NSE:TMPV)<br><sub>↓CMF17d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 10 | ↓15 | ↑1.001 | ↓21d | — | -8.6% | -43.02/-44.0 | +1.64% | 20% |
| [FIRSTCRY](https://in.tradingview.com/chart/?symbol=NSE:FIRSTCRY)<br><sub>↓CMF30d</sub> | ✓ SAFE | Baby kids mother products retailer omnichannel platform | 📈 BULL_ANY_MID | 5 | ↓3 | ↓1.001 | ↓15d | — | -1.1% | -24.1/-27.28 | -0.49% | 20% |
| [HONDAPOWER](https://in.tradingview.com/chart/?symbol=NSE:HONDAPOWER)<br><sub>↓CMF14d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 3 | ↓16 | ↓0.990 | ↓17d | — | -3.0% | -50.39/-51.65 | -1.12% | 20% |
| [NETWEB](https://in.tradingview.com/chart/?symbol=NSE:NETWEB)<br><sub>↓CMF10d</sub> | ✓ SAFE | High-performance computing systems manufacturer for AI and research | 📈 BULL_ANY_MID | 0 | ↓91 | ↓0.999 | ↓23d | — | +4.9% | -20.58/-21.73 | -0.04% | 20% |
| [KIOCL](https://in.tradingview.com/chart/?symbol=NSE:KIOCL)<br><sub>↓CMF24d · ⚠️TRAP</sub> | ✓ SAFE | Iron ore pellets and pig iron manufacturing for steelmakers | 📈 BULL_ANY_MID | 0 | ↓43 | ↓0.988 | ↓23d | — | -1.8% | -39.88/-41.13 | -1.86% | 20% |
| [SASKEN](https://in.tradingview.com/chart/?symbol=NSE:SASKEN)<br><sub>↓CMF14d</sub> | ✓ SAFE | Product engineering, embedded systems, automotive semiconductor clients | 📈 BULL_ANY_MID | 0 | ↓91 | ↓0.977 | ↓21d | — | -4.7% | -27.88/-28.42 | -2.50% | 5% 🟥 |
| [SANOFICONR](https://in.tradingview.com/chart/?symbol=NSE:SANOFICONR)<br><sub>↑CMF1d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 0 | ↓34 | ↓0.995 | ↓22d | — | -1.3% | -39.68/-40.04 | -0.64% | 20% |

```
NSE:ROLEXRINGS,NSE:BHEL,NSE:UNIVCABLES,NSE:PIRAMALFIN,NSE:GOODYEAR,NSE:RRKABEL,NSE:GARFIBRES,NSE:ABCAPITAL,NSE:OFSS,NSE:CAPLIPOINT,NSE:BLUESTONE,NSE:TTKPRESTIG,NSE:ALIVUS,NSE:SPECTRUM,NSE:HUHTAMAKI,NSE:PNB,NSE:GMMPFAUDLR,NSE:TITAGARH,NSE:UNIONBANK,NSE:ZEEL,NSE:HDFCLIFE,NSE:PINELABS,NSE:JBMA,NSE:HITECH,NSE:GESHIP,NSE:TMPV,NSE:FIRSTCRY,NSE:HONDAPOWER,NSE:NETWEB,NSE:KIOCL,NSE:SASKEN,NSE:SANOFICONR
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
