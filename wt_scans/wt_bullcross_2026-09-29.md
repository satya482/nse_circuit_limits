> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-09-29
*Generated 2026-09-29 15:46 IST*

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

**Total bull crosses today: 60** · 31 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LANDMARK,NSE:SJS,NSE:GLAND,NSE:SKYGOLD,NSE:DOLLAR,NSE:AZAD,NSE:KIRLOSENG,NSE:INDOCO,NSE:UNICHEMLAB,NSE:KMEW,NSE:FERMENTA,NSE:KIRLOSBROS,NSE:SENORES,NSE:APOLLOTYRE,NSE:CHENNPETRO,NSE:ELLEN,NSE:EIHOTEL,NSE:ELECTCAST,NSE:ASTRAMICRO,NSE:DPABHUSHAN,NSE:PGHL,NSE:AXISCADES,NSE:SIGMAADV,NSE:ALLDIGI,NSE:PASHUPATI,NSE:INDPRUD,NSE:UJJIVANSFB,NSE:AJANTPHARM,NSE:PANAMAPET,NSE:SUPRAJIT,NSE:DIFFNKG,NSE:VIDHIING,NSE:FINEORG,NSE:CUPID,NSE:NINSYS,NSE:MEESHO,NSE:ARSSBL,NSE:GPTINFRA,NSE:PRAKASH,NSE:AEROFLEX,NSE:JAYNECOIND,NSE:NEOGEN,NSE:SETL,NSE:SURAKSHA,NSE:GRASIM,NSE:WELCORP,NSE:CARERATING,NSE:VESUVIUS,NSE:TDPOWERSYS,NSE:HONAUT,NSE:FRACTAL,NSE:KANSAINER,NSE:GRINFRA,NSE:ABLBL,NSE:BHARATWIRE,NSE:SPANDANA,NSE:SANDHAR,NSE:KERNEX,NSE:AGIIL,NSE:CMPDI
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (47)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [LANDMARK](https://in.tradingview.com/chart/?symbol=NSE:LANDMARK)<br><sub>📶W9 · 🚀SS·238x · ↓CMF1d</sub> | ✓ SAFE | Premium multi-brand auto retail, luxury car dealerships | ⚡ BULL_ANY_PPV | 87 | 🔄54 | ↑0.992 | ↓8d | SQ·PV | -1.0% | -18.02/-18.72 | +2.33% | 20% |
| [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS)<br><sub>📶W9 · 🚀SS · ↑CMF4d</sub> | ✓ SAFE | Decorative graphics manufacturing for automotive consumer electronics appliances | ⚡ BULL_ANY_PPV | 87 | 🔄79 | ↑1.000 | ↓8d | SQ·PV | +1.9% | -34.11/-34.34 | +2.13% | 20% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Generic injectables manufacturer for global regulated markets | ⚡ BULL_ANY_PPV | 64 | ↑89 | ↑1.022 | ↑1d | SQ·PV | +3.2% | 19.88/14.52 | +3.24% | 20% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>📶W9 · 🚀SS · ↓CMF10d</sub> | ✓ SAFE | Gold jewelry manufacturer selling to retail jewelers B2B | ⚡ BULL_ANY_PPV | 64 | ↑98 | ↑1.026 | ↑1d | SQ·PV | +3.0% | 7.45/-0.22 | +3.00% | 20% |
| [DOLLAR](https://in.tradingview.com/chart/?symbol=NSE:DOLLAR)<br><sub>📶W9 · W↑17d · ↑CMF9d</sub> | ✓ SAFE | Knitted innerwear and casual apparel manufacturer for mass market | ⚡ BULL_ANY_PPV | 64 | ↑38 | ↑1.029 | ↑1d | SQ·PV | +4.0% | 13.68/8.58 | +3.99% | 20% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>📶W9 · 🚀SS·16x · ↑CMF0d</sub> | ✓ SAFE | Precision aerospace defense turbine components for global OEMs | ⚡ BULL_ANY_PPV | 59 | ↑92 | ↑1.055 | ↑1d | SQ·PV | +7.0% | 2.73/-10.49 | +7.01% | 20% |
| [KIRLOSENG](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSENG)<br><sub>📶W9 · W↑2d · RVOL13x · ↑CMF30d</sub> | ✓ SAFE | Diesel engines, gensets, pump sets for power | ⚡ BULL_ANY_PPV | 59 | ↑93 | ↑1.093 | ↑1d | SQ·PV | +12.2% | 20.43/11.04 | +12.18% | 20% |
| [INDOCO](https://in.tradingview.com/chart/?symbol=NSE:INDOCO)<br><sub>📶W9 · W↑22d · 🚀SS·11x · ↑CMF23d · DEL57%(T-1)</sub> | ✓ SAFE | Pharmaceutical manufacturer oral drugs dermatology gastrointestinal India | ⚡ BULL_ANY_PPV | 59 | ↑67 | ↑1.055 | ↑1d | SQ·PV | +8.1% | 24.82/17.29 | +8.07% | 20% |
| [UNICHEMLAB](https://in.tradingview.com/chart/?symbol=NSE:UNICHEMLAB)<br><sub>📶W9 · W↑2d · RVOL39x · ↓CMF15d</sub> | ✓ SAFE | Generic drugs, APIs, contract manufacturing for pharma | ⚡ BULL_ANY_PPV | 59 | ↑83 | ↑1.034 | ↑1d | SQ·PV | +6.0% | 21.84/17.62 | +5.97% | 20% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>📶W9 · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Dredging, marine craft repair, maritime infrastructure engineering | ⚡ BULL_ANY_PPV | 59 | ↑94 | ↑1.049 | ↑1d | SQ·PV | +6.5% | 20.4/17.29 | +6.53% | 20% |
| [FERMENTA](https://in.tradingview.com/chart/?symbol=NSE:FERMENTA)<br><sub>📶W9 · 🚀SS·16x · ↑CMF1d</sub> | ✓ SAFE | Vitamin D3 and enzyme APIs for pharma, nutraceuticals | ⚡ BULL_ANY_PPV | 58 | ↑50 | ↑1.112 | ↑2d | SQ·PV | +16.1% | 5.22/-10.32 | +10.82% | 20% |
| [KIRLOSBROS](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSBROS)<br><sub>📶W9 · RVOL16x · ↓CMF16d · ÷DIV</sub> | ⚠ CAUTION | Pumps and fluid systems for water, power, irrigation | ⚡ BULL_ANY_PPV | 49 | 🔄58 | ↑1.033 | ↑1d | PV | +6.7% | -39.51/-48.07 | +6.70% | 20% |
| [SENORES](https://in.tradingview.com/chart/?symbol=NSE:SENORES)<br><sub>📶W9 · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Complex generics manufacturer specialty pharma therapies India | ⚡ BULL_ANY_PPV | 43 | 🔄89 | ↑1.012 | ↓17d | PV | -1.7% | -44.53/-47.29 | +3.84% | 20% |
| [APOLLOTYRE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOTYRE)<br><sub>📶W9 · RVOL8x · ↓CMF29d · 🎯SLING</sub> | ⚠ CAUTION | Radial tyres for cars trucks farm vehicles | ⚡ BULL_ANY_PPV | 40 | 🔄30 | ↑1.005 | ↓21d | PV | -7.3% | -54.81/-58.1 | +4.40% | 20% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>📶W9 · ↑CMF9d</sub> | ✓ SAFE | Refines crude oil, produces petroleum products, lubricants | ⚡ BULL_ANY_PPV | 29 | ↑89 | ↑1.014 | ↑1d | PV | +2.0% | -0.73/-1.24 | +2.05% | 20% |
| [ELLEN](https://in.tradingview.com/chart/?symbol=NSE:ELLEN)<br><sub>📶W9 · W↑42d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Industrial oxygen nitrogen gases bulk packaged eastern southern India | ⚡ BULL_ANY_PPV | 29 | ↑80 | ↑1.014 | ↑1d | PV | +2.9% | 42.55/41.77 | +2.87% | 20% |
| [EIHOTEL](https://in.tradingview.com/chart/?symbol=NSE:EIHOTEL)<br><sub>📶W9 · W↑7d · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION | Luxury hotels, resorts, flight catering operations | ⚡ BULL_ANY_PPV | 29 | ↑30 | ↑1.011 | ↑1d | PV | +2.3% | -2.36/-3.01 | +2.29% | 20% |
| [ELECTCAST](https://in.tradingview.com/chart/?symbol=NSE:ELECTCAST)<br><sub>📶W9 · RVOL10x · ↑CMF0d</sub> | ✓ SAFE | Ductile iron pipes fittings water infrastructure manufacturing | ⚡ BULL_ANY_PPV | 24 | ↑40 | ↑1.029 | ↑1d | PV | +5.8% | -27.03/-30.56 | +5.78% | 20% |
| [ASTRAMICRO](https://in.tradingview.com/chart/?symbol=NSE:ASTRAMICRO)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | RF microwave modules defense space telecom systems | ⚡ BULL_ANY_PPV | 24 | ↑83 | ↑1.015 | ↑1d | PV | +3.9% | -39.22/-42.91 | +3.93% | 20% |
| [DPABHUSHAN](https://in.tradingview.com/chart/?symbol=NSE:DPABHUSHAN)<br><sub>📶W9 · W↑7d · RVOL45x · ↑CMF0d</sub> | ✓ SAFE | Gold diamond platinum silver jewellery retail manufacturing Central India | ⚡ BULL_ANY_PPV | 19 | ↑88 | ↑1.145 | ↑1d | PV | +20.0% | 12.87/2.57 | +20.00% | 20% |
| [PGHL](https://in.tradingview.com/chart/?symbol=NSE:PGHL)<br><sub>📶W9 · 🚀SS·12x · ↓CMF30d</sub> | ⚠ CAUTION | Vitamins minerals supplements pharmaceuticals consumer health | ⚡ BULL_ANY_PPV | 19 | ↑46 | ↑1.037 | ↑1d | PV | +5.5% | -32.15/-43.75 | +5.49% | 20% |
| [AXISCADES](https://in.tradingview.com/chart/?symbol=NSE:AXISCADES)<br><sub>📶W9 · W↑22d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Engineering design services automotive aerospace defense OEMs | ⚡ BULL_ANY_PPV | 11 | ↑81 | ↑1.089 | ↑9d | PV | +22.7% | 60.3/56.75 | +10.00% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [ALLDIGI](https://in.tradingview.com/chart/?symbol=NSE:ALLDIGI)<br><sub>📶W9 · ↓CMF21d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 48 | ↑38 | ↑0.993 | ↓17d | SQ | -3.7% | -66.27/-68.48 | -0.01% | 20% |
| [PASHUPATI](https://in.tradingview.com/chart/?symbol=NSE:PASHUPATI)<br><sub>📶W9 · W↑2d · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 89 | 🔄63 | ↑1.130 | ↑1d | SQ | +20.0% | -31.4/-44.71 | +19.99% | 20% |
| [INDPRUD](https://in.tradingview.com/chart/?symbol=NSE:INDPRUD)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 89 | 🔄50 | ↑1.033 | ↑1d | SQ | +6.4% | -22.19/-23.77 | +6.43% | 20% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>📶W9 · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Microfinance bank serving low-income retail borrowers India | 📈 BULL_ANY_MID | 69 | ↑74 | ↑1.011 | ↑1d | SQ | +3.4% | -34.79/-35.75 | +3.44% | 20% |
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Branded generic pharmaceuticals formulations across India Asia Africa | 📈 BULL_ANY_MID | 69 | ↑75 | ↑1.005 | ↑1d | SQ | +0.9% | 5.64/3.68 | +0.92% | 20% |
| [PANAMAPET](https://in.tradingview.com/chart/?symbol=NSE:PANAMAPET)<br><sub>📶W9 · ↑CMF4d</sub> | ✓ SAFE | Specialty petroleum products for pharma, cosmetics, rubber | 📈 BULL_ANY_MID | 69 | ↑88 | ↑1.011 | ↑1d | SQ | +2.8% | -5.85/-6.68 | +2.81% | 10% 🟨 |
| [SUPRAJIT](https://in.tradingview.com/chart/?symbol=NSE:SUPRAJIT)<br><sub>📶W9 · ↓CMF6d</sub> | ⚠ CAUTION | Automotive cables, halogen lamps, mechanical components manufacturer | 📈 BULL_ANY_MID | 69 | ↑56 | ↑1.009 | ↑1d | SQ | +1.8% | -25.94/-26.85 | +1.76% | 20% |
| [DIFFNKG](https://in.tradingview.com/chart/?symbol=NSE:DIFFNKG)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Welding consumables, wear plates, heavy machinery manufacturing | 📈 BULL_ANY_MID | 63 | ↑77 | ↑1.018 | ↑2d | SQ | +4.1% | -7.16/-8.32 | +0.90% | 20% |
| [VIDHIING](https://in.tradingview.com/chart/?symbol=NSE:VIDHIING)<br><sub>📶W9 · W↑62d · ↑CMF25d</sub> | ⚠ CAUTION | Food grade colors manufacturer serving F&B pharma confectionery | 📈 BULL_ANY_MID | 63 | ↑67 | ↑1.022 | ↑2d | SQ | +4.0% | 30.23/29.19 | +1.53% | 20% |
| [FINEORG](https://in.tradingview.com/chart/?symbol=NSE:FINEORG)<br><sub>📶W9 · ↑CMF10d</sub> | ⚠ CAUTION | Oleochemical specialty additives food plastics cosmetics coatings | 📈 BULL_ANY_MID | 60 | ↑62 | ↑1.002 | ↓10d | SQ | -0.3% | -24.31/-25.13 | +0.31% | 20% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>📶W9 · ↑CMF4d</sub> | ✓ SAFE | Condoms lubricants IVD kits sexual wellness global | 📈 BULL_ANY_MID | 59 | ↑99 | ↑1.057 | ↑1d | SQ | +8.9% | -12.75/-22.36 | +8.88% | 20% |
| [NINSYS](https://in.tradingview.com/chart/?symbol=NSE:NINSYS)<br><sub>📶W9 · ↓CMF18d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 59 | ↑85 | ↑1.031 | ↑1d | SQ | +4.4% | -9.62/-22.67 | +4.39% | 5% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · W↑30d · ↑CMF30d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.025 | ↑2d | SQ | +6.1% | 49.69/48.04 | -0.06% | 20% 🟦 |
| [ARSSBL](https://in.tradingview.com/chart/?symbol=NSE:ARSSBL)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Equity derivatives broker with MTF and financial advisory services | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.001 | ↑2d | SQ | +0.7% | -20.33/-22.09 | -0.03% | 20% |
| [GPTINFRA](https://in.tradingview.com/chart/?symbol=NSE:GPTINFRA)<br><sub>📶W9 · W↑7d · ↓CMF20d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↑47 | ↓1.004 | ↑3d | SQ | +1.9% | 14.21/13.67 | -0.47% | 20% |
| [PRAKASH](https://in.tradingview.com/chart/?symbol=NSE:PRAKASH)<br><sub>📶W9 · ↓CMF13d · ÷DIV</sub> | ✓ SAFE | Steel manufacturing, mining, power generation integrated producer | 📈 BULL_ANY_MID | 54 | 🔄22 | ↑1.018 | ↑1d | — | +5.1% | -50.1/-52.89 | +5.13% | 20% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Stainless steel corrugated hoses assemblies fittings industrial applications | 📈 BULL_ANY_MID | 24 | ↑97 | ↑1.029 | ↑1d | — | +5.1% | 9.27/8.84 | +5.10% | 10% 🟨 |
| [JAYNECOIND](https://in.tradingview.com/chart/?symbol=NSE:JAYNECOIND)<br><sub>📶W9 · ↓CMF9d</sub> | ✓ SAFE | Ferrous castings, steel alloys, integrated mining to foundry | 📈 BULL_ANY_MID | 24 | ↑63 | ↑1.027 | ↑1d | — | +5.3% | -18.63/-20.21 | +5.32% | 20% 🟦 |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>📶W9 · W↑17d · ↑CMF10d</sub> | ✓ SAFE | Bromine lithium specialty chemicals pharma agri-chem | 📈 BULL_ANY_MID | 22 | ↑92 | ↑1.024 | ↑3d | — | +4.7% | 45.61/43.42 | +1.63% | 20% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Glass-lined reactors and process equipment for pharma chemicals | 📈 BULL_ANY_MID | 18 | ↑98 | ↑1.035 | ↑2d | — | +6.6% | 28.53/26.06 | +1.49% | 5% 🟥 |
| [SURAKSHA](https://in.tradingview.com/chart/?symbol=NSE:SURAKSHA)<br><sub>📶W9 · W↑37d · ↑CMF30d</sub> | ✓ SAFE | Pathology radiology diagnostic centers East India healthcare | 📈 BULL_ANY_MID | 17 | ↑81 | ↑1.026 | ↑8d | — | +7.9% | 38.28/38.09 | +2.31% | 20% |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 14 | ↑61 | ↑0.998 | ↓11d | — | -3.2% | -35.97/-36.7 | +0.74% | 20% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Large-diameter pipes, steel products, infrastructure | 📈 BULL_ANY_MID | 12 | ↑99 | ↑1.044 | ↑8d | — | +15.5% | 48.33/47.81 | +3.73% | 20% |
| [CARERATING](https://in.tradingview.com/chart/?symbol=NSE:CARERATING)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Credit rating agency for corporate debt securities | 📈 BULL_ANY_MID | 6 | ↑53 | ↑0.999 | ↓19d | — | -2.7% | -38.66/-38.83 | +0.58% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LANDMARK,NSE:SJS,NSE:GLAND,NSE:SKYGOLD,NSE:DOLLAR,NSE:AZAD,NSE:KIRLOSENG,NSE:INDOCO,NSE:UNICHEMLAB,NSE:KMEW,NSE:FERMENTA,NSE:KIRLOSBROS,NSE:SENORES,NSE:APOLLOTYRE,NSE:CHENNPETRO,NSE:ELLEN,NSE:EIHOTEL,NSE:ELECTCAST,NSE:ASTRAMICRO,NSE:DPABHUSHAN,NSE:PGHL,NSE:AXISCADES,NSE:SIGMAADV,NSE:ALLDIGI,NSE:PASHUPATI,NSE:INDPRUD,NSE:UJJIVANSFB,NSE:AJANTPHARM,NSE:PANAMAPET,NSE:SUPRAJIT,NSE:DIFFNKG,NSE:VIDHIING,NSE:FINEORG,NSE:CUPID,NSE:NINSYS,NSE:MEESHO,NSE:ARSSBL,NSE:GPTINFRA,NSE:PRAKASH,NSE:AEROFLEX,NSE:JAYNECOIND,NSE:NEOGEN,NSE:SETL,NSE:SURAKSHA,NSE:GRASIM,NSE:WELCORP,NSE:CARERATING
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (59)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [LANDMARK](https://in.tradingview.com/chart/?symbol=NSE:LANDMARK)<br><sub>📶W9 · 🚀SS·238x · ↓CMF1d</sub> | ✓ SAFE | Premium multi-brand auto retail, luxury car dealerships | ⚡ BULL_ANY_PPV | 87 | 🔄54 | ↑0.992 | ↓8d | SQ·PV | -1.0% | -18.02/-18.72 | +2.33% | 20% |
| [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS)<br><sub>📶W9 · 🚀SS · ↑CMF4d</sub> | ✓ SAFE | Decorative graphics manufacturing for automotive consumer electronics appliances | ⚡ BULL_ANY_PPV | 87 | 🔄79 | ↑1.000 | ↓8d | SQ·PV | +1.9% | -34.11/-34.34 | +2.13% | 20% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Generic injectables manufacturer for global regulated markets | ⚡ BULL_ANY_PPV | 64 | ↑89 | ↑1.022 | ↑1d | SQ·PV | +3.2% | 19.88/14.52 | +3.24% | 20% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>📶W9 · 🚀SS · ↓CMF10d</sub> | ✓ SAFE | Gold jewelry manufacturer selling to retail jewelers B2B | ⚡ BULL_ANY_PPV | 64 | ↑98 | ↑1.026 | ↑1d | SQ·PV | +3.0% | 7.45/-0.22 | +3.00% | 20% |
| [DOLLAR](https://in.tradingview.com/chart/?symbol=NSE:DOLLAR)<br><sub>📶W9 · W↑17d · ↑CMF9d</sub> | ✓ SAFE | Knitted innerwear and casual apparel manufacturer for mass market | ⚡ BULL_ANY_PPV | 64 | ↑38 | ↑1.029 | ↑1d | SQ·PV | +4.0% | 13.68/8.58 | +3.99% | 20% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>📶W9 · 🚀SS·16x · ↑CMF0d</sub> | ✓ SAFE | Precision aerospace defense turbine components for global OEMs | ⚡ BULL_ANY_PPV | 59 | ↑92 | ↑1.055 | ↑1d | SQ·PV | +7.0% | 2.73/-10.49 | +7.01% | 20% |
| [KIRLOSENG](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSENG)<br><sub>📶W9 · W↑2d · RVOL13x · ↑CMF30d</sub> | ✓ SAFE | Diesel engines, gensets, pump sets for power | ⚡ BULL_ANY_PPV | 59 | ↑93 | ↑1.093 | ↑1d | SQ·PV | +12.2% | 20.43/11.04 | +12.18% | 20% |
| [INDOCO](https://in.tradingview.com/chart/?symbol=NSE:INDOCO)<br><sub>📶W9 · W↑22d · 🚀SS·11x · ↑CMF23d · DEL57%(T-1)</sub> | ✓ SAFE | Pharmaceutical manufacturer oral drugs dermatology gastrointestinal India | ⚡ BULL_ANY_PPV | 59 | ↑67 | ↑1.055 | ↑1d | SQ·PV | +8.1% | 24.82/17.29 | +8.07% | 20% |
| [UNICHEMLAB](https://in.tradingview.com/chart/?symbol=NSE:UNICHEMLAB)<br><sub>📶W9 · W↑2d · RVOL39x · ↓CMF15d</sub> | ✓ SAFE | Generic drugs, APIs, contract manufacturing for pharma | ⚡ BULL_ANY_PPV | 59 | ↑83 | ↑1.034 | ↑1d | SQ·PV | +6.0% | 21.84/17.62 | +5.97% | 20% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>📶W9 · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Dredging, marine craft repair, maritime infrastructure engineering | ⚡ BULL_ANY_PPV | 59 | ↑94 | ↑1.049 | ↑1d | SQ·PV | +6.5% | 20.4/17.29 | +6.53% | 20% |
| [FERMENTA](https://in.tradingview.com/chart/?symbol=NSE:FERMENTA)<br><sub>📶W9 · 🚀SS·16x · ↑CMF1d</sub> | ✓ SAFE | Vitamin D3 and enzyme APIs for pharma, nutraceuticals | ⚡ BULL_ANY_PPV | 58 | ↑50 | ↑1.112 | ↑2d | SQ·PV | +16.1% | 5.22/-10.32 | +10.82% | 20% |
| [KIRLOSBROS](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSBROS)<br><sub>📶W9 · RVOL16x · ↓CMF16d · ÷DIV</sub> | ⚠ CAUTION | Pumps and fluid systems for water, power, irrigation | ⚡ BULL_ANY_PPV | 49 | 🔄58 | ↑1.033 | ↑1d | PV | +6.7% | -39.51/-48.07 | +6.70% | 20% |
| [SENORES](https://in.tradingview.com/chart/?symbol=NSE:SENORES)<br><sub>📶W9 · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Complex generics manufacturer specialty pharma therapies India | ⚡ BULL_ANY_PPV | 43 | 🔄89 | ↑1.012 | ↓17d | PV | -1.7% | -44.53/-47.29 | +3.84% | 20% |
| [APOLLOTYRE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOTYRE)<br><sub>📶W9 · RVOL8x · ↓CMF29d · 🎯SLING</sub> | ⚠ CAUTION | Radial tyres for cars trucks farm vehicles | ⚡ BULL_ANY_PPV | 40 | 🔄30 | ↑1.005 | ↓21d | PV | -7.3% | -54.81/-58.1 | +4.40% | 20% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>📶W9 · ↑CMF9d</sub> | ✓ SAFE | Refines crude oil, produces petroleum products, lubricants | ⚡ BULL_ANY_PPV | 29 | ↑89 | ↑1.014 | ↑1d | PV | +2.0% | -0.73/-1.24 | +2.05% | 20% |
| [ELLEN](https://in.tradingview.com/chart/?symbol=NSE:ELLEN)<br><sub>📶W9 · W↑42d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Industrial oxygen nitrogen gases bulk packaged eastern southern India | ⚡ BULL_ANY_PPV | 29 | ↑80 | ↑1.014 | ↑1d | PV | +2.9% | 42.55/41.77 | +2.87% | 20% |
| [EIHOTEL](https://in.tradingview.com/chart/?symbol=NSE:EIHOTEL)<br><sub>📶W9 · W↑7d · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION | Luxury hotels, resorts, flight catering operations | ⚡ BULL_ANY_PPV | 29 | ↑30 | ↑1.011 | ↑1d | PV | +2.3% | -2.36/-3.01 | +2.29% | 20% |
| [ELECTCAST](https://in.tradingview.com/chart/?symbol=NSE:ELECTCAST)<br><sub>📶W9 · RVOL10x · ↑CMF0d</sub> | ✓ SAFE | Ductile iron pipes fittings water infrastructure manufacturing | ⚡ BULL_ANY_PPV | 24 | ↑40 | ↑1.029 | ↑1d | PV | +5.8% | -27.03/-30.56 | +5.78% | 20% |
| [ASTRAMICRO](https://in.tradingview.com/chart/?symbol=NSE:ASTRAMICRO)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | RF microwave modules defense space telecom systems | ⚡ BULL_ANY_PPV | 24 | ↑83 | ↑1.015 | ↑1d | PV | +3.9% | -39.22/-42.91 | +3.93% | 20% |
| [DPABHUSHAN](https://in.tradingview.com/chart/?symbol=NSE:DPABHUSHAN)<br><sub>📶W9 · W↑7d · RVOL45x · ↑CMF0d</sub> | ✓ SAFE | Gold diamond platinum silver jewellery retail manufacturing Central India | ⚡ BULL_ANY_PPV | 19 | ↑88 | ↑1.145 | ↑1d | PV | +20.0% | 12.87/2.57 | +20.00% | 20% |
| [PGHL](https://in.tradingview.com/chart/?symbol=NSE:PGHL)<br><sub>📶W9 · 🚀SS·12x · ↓CMF30d</sub> | ⚠ CAUTION | Vitamins minerals supplements pharmaceuticals consumer health | ⚡ BULL_ANY_PPV | 19 | ↑46 | ↑1.037 | ↑1d | PV | +5.5% | -32.15/-43.75 | +5.49% | 20% |
| [AXISCADES](https://in.tradingview.com/chart/?symbol=NSE:AXISCADES)<br><sub>📶W9 · W↑22d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Engineering design services automotive aerospace defense OEMs | ⚡ BULL_ANY_PPV | 11 | ↑81 | ↑1.089 | ↑9d | PV | +22.7% | 60.3/56.75 | +10.00% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [ALLDIGI](https://in.tradingview.com/chart/?symbol=NSE:ALLDIGI)<br><sub>📶W9 · ↓CMF21d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 48 | ↑38 | ↑0.993 | ↓17d | SQ | -3.7% | -66.27/-68.48 | -0.01% | 20% |
| [PASHUPATI](https://in.tradingview.com/chart/?symbol=NSE:PASHUPATI)<br><sub>📶W9 · W↑2d · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 89 | 🔄63 | ↑1.130 | ↑1d | SQ | +20.0% | -31.4/-44.71 | +19.99% | 20% |
| [INDPRUD](https://in.tradingview.com/chart/?symbol=NSE:INDPRUD)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 89 | 🔄50 | ↑1.033 | ↑1d | SQ | +6.4% | -22.19/-23.77 | +6.43% | 20% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>📶W9 · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Microfinance bank serving low-income retail borrowers India | 📈 BULL_ANY_MID | 69 | ↑74 | ↑1.011 | ↑1d | SQ | +3.4% | -34.79/-35.75 | +3.44% | 20% |
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Branded generic pharmaceuticals formulations across India Asia Africa | 📈 BULL_ANY_MID | 69 | ↑75 | ↑1.005 | ↑1d | SQ | +0.9% | 5.64/3.68 | +0.92% | 20% |
| [PANAMAPET](https://in.tradingview.com/chart/?symbol=NSE:PANAMAPET)<br><sub>📶W9 · ↑CMF4d</sub> | ✓ SAFE | Specialty petroleum products for pharma, cosmetics, rubber | 📈 BULL_ANY_MID | 69 | ↑88 | ↑1.011 | ↑1d | SQ | +2.8% | -5.85/-6.68 | +2.81% | 10% 🟨 |
| [SUPRAJIT](https://in.tradingview.com/chart/?symbol=NSE:SUPRAJIT)<br><sub>📶W9 · ↓CMF6d</sub> | ⚠ CAUTION | Automotive cables, halogen lamps, mechanical components manufacturer | 📈 BULL_ANY_MID | 69 | ↑56 | ↑1.009 | ↑1d | SQ | +1.8% | -25.94/-26.85 | +1.76% | 20% |
| [DIFFNKG](https://in.tradingview.com/chart/?symbol=NSE:DIFFNKG)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Welding consumables, wear plates, heavy machinery manufacturing | 📈 BULL_ANY_MID | 63 | ↑77 | ↑1.018 | ↑2d | SQ | +4.1% | -7.16/-8.32 | +0.90% | 20% |
| [VIDHIING](https://in.tradingview.com/chart/?symbol=NSE:VIDHIING)<br><sub>📶W9 · W↑62d · ↑CMF25d</sub> | ⚠ CAUTION | Food grade colors manufacturer serving F&B pharma confectionery | 📈 BULL_ANY_MID | 63 | ↑67 | ↑1.022 | ↑2d | SQ | +4.0% | 30.23/29.19 | +1.53% | 20% |
| [FINEORG](https://in.tradingview.com/chart/?symbol=NSE:FINEORG)<br><sub>📶W9 · ↑CMF10d</sub> | ⚠ CAUTION | Oleochemical specialty additives food plastics cosmetics coatings | 📈 BULL_ANY_MID | 60 | ↑62 | ↑1.002 | ↓10d | SQ | -0.3% | -24.31/-25.13 | +0.31% | 20% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>📶W9 · ↑CMF4d</sub> | ✓ SAFE | Condoms lubricants IVD kits sexual wellness global | 📈 BULL_ANY_MID | 59 | ↑99 | ↑1.057 | ↑1d | SQ | +8.9% | -12.75/-22.36 | +8.88% | 20% |
| [NINSYS](https://in.tradingview.com/chart/?symbol=NSE:NINSYS)<br><sub>📶W9 · ↓CMF18d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 59 | ↑85 | ↑1.031 | ↑1d | SQ | +4.4% | -9.62/-22.67 | +4.39% | 5% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · W↑30d · ↑CMF30d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.025 | ↑2d | SQ | +6.1% | 49.69/48.04 | -0.06% | 20% 🟦 |
| [ARSSBL](https://in.tradingview.com/chart/?symbol=NSE:ARSSBL)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Equity derivatives broker with MTF and financial advisory services | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.001 | ↑2d | SQ | +0.7% | -20.33/-22.09 | -0.03% | 20% |
| [GPTINFRA](https://in.tradingview.com/chart/?symbol=NSE:GPTINFRA)<br><sub>📶W9 · W↑7d · ↓CMF20d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↑47 | ↓1.004 | ↑3d | SQ | +1.9% | 14.21/13.67 | -0.47% | 20% |
| [PRAKASH](https://in.tradingview.com/chart/?symbol=NSE:PRAKASH)<br><sub>📶W9 · ↓CMF13d · ÷DIV</sub> | ✓ SAFE | Steel manufacturing, mining, power generation integrated producer | 📈 BULL_ANY_MID | 54 | 🔄22 | ↑1.018 | ↑1d | — | +5.1% | -50.1/-52.89 | +5.13% | 20% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Stainless steel corrugated hoses assemblies fittings industrial applications | 📈 BULL_ANY_MID | 24 | ↑97 | ↑1.029 | ↑1d | — | +5.1% | 9.27/8.84 | +5.10% | 10% 🟨 |
| [JAYNECOIND](https://in.tradingview.com/chart/?symbol=NSE:JAYNECOIND)<br><sub>📶W9 · ↓CMF9d</sub> | ✓ SAFE | Ferrous castings, steel alloys, integrated mining to foundry | 📈 BULL_ANY_MID | 24 | ↑63 | ↑1.027 | ↑1d | — | +5.3% | -18.63/-20.21 | +5.32% | 20% 🟦 |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>📶W9 · W↑17d · ↑CMF10d</sub> | ✓ SAFE | Bromine lithium specialty chemicals pharma agri-chem | 📈 BULL_ANY_MID | 22 | ↑92 | ↑1.024 | ↑3d | — | +4.7% | 45.61/43.42 | +1.63% | 20% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Glass-lined reactors and process equipment for pharma chemicals | 📈 BULL_ANY_MID | 18 | ↑98 | ↑1.035 | ↑2d | — | +6.6% | 28.53/26.06 | +1.49% | 5% 🟥 |
| [SURAKSHA](https://in.tradingview.com/chart/?symbol=NSE:SURAKSHA)<br><sub>📶W9 · W↑37d · ↑CMF30d</sub> | ✓ SAFE | Pathology radiology diagnostic centers East India healthcare | 📈 BULL_ANY_MID | 17 | ↑81 | ↑1.026 | ↑8d | — | +7.9% | 38.28/38.09 | +2.31% | 20% |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 14 | ↑61 | ↑0.998 | ↓11d | — | -3.2% | -35.97/-36.7 | +0.74% | 20% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Large-diameter pipes, steel products, infrastructure | 📈 BULL_ANY_MID | 12 | ↑99 | ↑1.044 | ↑8d | — | +15.5% | 48.33/47.81 | +3.73% | 20% |
| [CARERATING](https://in.tradingview.com/chart/?symbol=NSE:CARERATING)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Credit rating agency for corporate debt securities | 📈 BULL_ANY_MID | 6 | ↑53 | ↑0.999 | ↓19d | — | -2.7% | -38.66/-38.83 | +0.58% | 20% |
| [VESUVIUS](https://in.tradingview.com/chart/?symbol=NSE:VESUVIUS)<br><sub>🚀SS·39x · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Refractory ceramics for steel foundry molten metal flows | 🔥 BULL_OS_PPV | 59 | 🔄18 | ↑1.008 | ↑1d | PV | +3.8% | -54.42/-62.11 | +3.84% | 20% |
| [TDPOWERSYS](https://in.tradingview.com/chart/?symbol=NSE:TDPOWERSYS)<br><sub>↑CMF0d · ÷DIV</sub> | ✓ SAFE | AC generators and motors for power generation applications | ⚡ BULL_ANY_PPV | 89 | 🔄40 | ↑1.030 | ↑1d | SQ·PV | +7.7% | -17.39/-18.96 | +7.67% | 20% |
| [HONAUT](https://in.tradingview.com/chart/?symbol=NSE:HONAUT)<br><sub>RVOL9x · ↓CMF30d</sub> | ⚠ CAUTION | Industrial automation control systems for manufacturing plants | ⚡ BULL_ANY_PPV | 57 | ↑46 | ↑0.995 | ↓8d | SQ·PV | +0.2% | -46.4/-50.81 | +0.37% | 20% |
| [FRACTAL](https://in.tradingview.com/chart/?symbol=NSE:FRACTAL)<br><sub>↓CMF11d</sub> | ✓ SAFE | AI analytics solutions for global Fortune 500 enterprises | ⚡ BULL_ANY_PPV | 8 | ↑50 | ↑0.992 | ↓17d | PV | -8.4% | -47.75/-48.05 | +1.02% | 20% |
| [KANSAINER](https://in.tradingview.com/chart/?symbol=NSE:KANSAINER)<br><sub>↑CMF0d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Industrial and decorative paints manufacturer for buildings and industry | 🟢 BULL_OVERSOLD | 35 | 🔄19 | ↑0.995 | ↓28d | — | -10.0% | -61.58/-62.15 | +2.17% | 20% |
| [GRINFRA](https://in.tradingview.com/chart/?symbol=NSE:GRINFRA)<br><sub>↓CMF16d · 🎯SLING</sub> | ⚠ CAUTION | Road EPC contractor, highways and railways infrastructure | 🟢 BULL_OVERSOLD | 35 | 🔄19 | ↑0.996 | ↓26d | — | -7.2% | -63.05/-63.75 | +2.12% | 20% |
| [BHARATWIRE](https://in.tradingview.com/chart/?symbol=NSE:BHARATWIRE)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Steel wire ropes manufacturing for industrial rigging applications | 🟡 BULL_OS_L2 | 45 | ↑32 | ↑0.992 | ↓40d | SQ | -16.6% | -59.06/-59.67 | +0.50% | 20% |
| [SPANDANA](https://in.tradingview.com/chart/?symbol=NSE:SPANDANA)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Microloans to low-income women entrepreneurs, rural semi-urban areas | 🟡 BULL_OS_L2 | 15 | ↑25 | ↓0.992 | ↓5d | — | -0.3% | -52.75/-54.8 | -0.74% | 20% |
| [SANDHAR](https://in.tradingview.com/chart/?symbol=NSE:SANDHAR)<br><sub>↓CMF23d · 🎯SLING</sub> | ✓ SAFE | Automotive safety locks and components for four-wheelers | 🟡 BULL_OS_L2 | 5 | ↑54 | ↑0.991 | ↓33d | — | -5.3% | -55.4/-56.08 | +1.07% | 20% |
| [KERNEX](https://in.tradingview.com/chart/?symbol=NSE:KERNEX)<br><sub>↑CMF0d</sub> | ✓ SAFE | Railway safety systems and collision avoidance software manufacturer | 📈 BULL_ANY_MID | 69 | ↑76 | ↑1.011 | ↑1d | SQ | +1.8% | -22.55/-24.59 | +1.77% | 20% |
| [AGIIL](https://in.tradingview.com/chart/?symbol=NSE:AGIIL)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Real estate development and construction services Punjab region | 📈 BULL_ANY_MID | 58 | ↑29 | ↓0.984 | ↓2d | SQ | +0.1% | -49.35/-50.56 | -2.49% | 20% |
| [CMPDI](https://in.tradingview.com/chart/?symbol=NSE:CMPDI)<br><sub>↓CMF13d · ÷DIV</sub> | ✓ SAFE | Coal mine planning design consultancy subsidiary CIL | 📈 BULL_ANY_MID | 42 | 🔄50 | ↑1.006 | ↓18d | — | -4.7% | -46.36/-48.36 | +3.92% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LANDMARK,NSE:SJS,NSE:GLAND,NSE:SKYGOLD,NSE:DOLLAR,NSE:AZAD,NSE:KIRLOSENG,NSE:INDOCO,NSE:UNICHEMLAB,NSE:KMEW,NSE:FERMENTA,NSE:KIRLOSBROS,NSE:SENORES,NSE:APOLLOTYRE,NSE:CHENNPETRO,NSE:ELLEN,NSE:EIHOTEL,NSE:ELECTCAST,NSE:ASTRAMICRO,NSE:DPABHUSHAN,NSE:PGHL,NSE:AXISCADES,NSE:SIGMAADV,NSE:ALLDIGI,NSE:PASHUPATI,NSE:INDPRUD,NSE:UJJIVANSFB,NSE:AJANTPHARM,NSE:PANAMAPET,NSE:SUPRAJIT,NSE:DIFFNKG,NSE:VIDHIING,NSE:FINEORG,NSE:CUPID,NSE:NINSYS,NSE:MEESHO,NSE:ARSSBL,NSE:GPTINFRA,NSE:PRAKASH,NSE:AEROFLEX,NSE:JAYNECOIND,NSE:NEOGEN,NSE:SETL,NSE:SURAKSHA,NSE:GRASIM,NSE:WELCORP,NSE:CARERATING,NSE:VESUVIUS,NSE:TDPOWERSYS,NSE:HONAUT,NSE:FRACTAL,NSE:KANSAINER,NSE:GRINFRA,NSE:BHARATWIRE,NSE:SPANDANA,NSE:SANDHAR,NSE:KERNEX,NSE:AGIIL,NSE:CMPDI
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (31)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [LANDMARK](https://in.tradingview.com/chart/?symbol=NSE:LANDMARK)<br><sub>📶W9 · 🚀SS·238x · ↓CMF1d</sub> | ✓ SAFE | Premium multi-brand auto retail, luxury car dealerships | ⚡ BULL_ANY_PPV | 87 | 🔄54 | ↑0.992 | ↓8d | SQ·PV | -1.0% | -18.02/-18.72 | +2.33% | 20% |
| [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS)<br><sub>📶W9 · 🚀SS · ↑CMF4d</sub> | ✓ SAFE | Decorative graphics manufacturing for automotive consumer electronics appliances | ⚡ BULL_ANY_PPV | 87 | 🔄79 | ↑1.000 | ↓8d | SQ·PV | +1.9% | -34.11/-34.34 | +2.13% | 20% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Generic injectables manufacturer for global regulated markets | ⚡ BULL_ANY_PPV | 64 | ↑89 | ↑1.022 | ↑1d | SQ·PV | +3.2% | 19.88/14.52 | +3.24% | 20% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>📶W9 · 🚀SS · ↓CMF10d</sub> | ✓ SAFE | Gold jewelry manufacturer selling to retail jewelers B2B | ⚡ BULL_ANY_PPV | 64 | ↑98 | ↑1.026 | ↑1d | SQ·PV | +3.0% | 7.45/-0.22 | +3.00% | 20% |
| [DOLLAR](https://in.tradingview.com/chart/?symbol=NSE:DOLLAR)<br><sub>📶W9 · W↑17d · ↑CMF9d</sub> | ✓ SAFE | Knitted innerwear and casual apparel manufacturer for mass market | ⚡ BULL_ANY_PPV | 64 | ↑38 | ↑1.029 | ↑1d | SQ·PV | +4.0% | 13.68/8.58 | +3.99% | 20% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>📶W9 · 🚀SS·16x · ↑CMF0d</sub> | ✓ SAFE | Precision aerospace defense turbine components for global OEMs | ⚡ BULL_ANY_PPV | 59 | ↑92 | ↑1.055 | ↑1d | SQ·PV | +7.0% | 2.73/-10.49 | +7.01% | 20% |
| [KIRLOSENG](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSENG)<br><sub>📶W9 · W↑2d · RVOL13x · ↑CMF30d</sub> | ✓ SAFE | Diesel engines, gensets, pump sets for power | ⚡ BULL_ANY_PPV | 59 | ↑93 | ↑1.093 | ↑1d | SQ·PV | +12.2% | 20.43/11.04 | +12.18% | 20% |
| [INDOCO](https://in.tradingview.com/chart/?symbol=NSE:INDOCO)<br><sub>📶W9 · W↑22d · 🚀SS·11x · ↑CMF23d · DEL57%(T-1)</sub> | ✓ SAFE | Pharmaceutical manufacturer oral drugs dermatology gastrointestinal India | ⚡ BULL_ANY_PPV | 59 | ↑67 | ↑1.055 | ↑1d | SQ·PV | +8.1% | 24.82/17.29 | +8.07% | 20% |
| [UNICHEMLAB](https://in.tradingview.com/chart/?symbol=NSE:UNICHEMLAB)<br><sub>📶W9 · W↑2d · RVOL39x · ↓CMF15d</sub> | ✓ SAFE | Generic drugs, APIs, contract manufacturing for pharma | ⚡ BULL_ANY_PPV | 59 | ↑83 | ↑1.034 | ↑1d | SQ·PV | +6.0% | 21.84/17.62 | +5.97% | 20% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>📶W9 · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Dredging, marine craft repair, maritime infrastructure engineering | ⚡ BULL_ANY_PPV | 59 | ↑94 | ↑1.049 | ↑1d | SQ·PV | +6.5% | 20.4/17.29 | +6.53% | 20% |
| [FERMENTA](https://in.tradingview.com/chart/?symbol=NSE:FERMENTA)<br><sub>📶W9 · 🚀SS·16x · ↑CMF1d</sub> | ✓ SAFE | Vitamin D3 and enzyme APIs for pharma, nutraceuticals | ⚡ BULL_ANY_PPV | 58 | ↑50 | ↑1.112 | ↑2d | SQ·PV | +16.1% | 5.22/-10.32 | +10.82% | 20% |
| [ALLDIGI](https://in.tradingview.com/chart/?symbol=NSE:ALLDIGI)<br><sub>📶W9 · ↓CMF21d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 48 | ↑38 | ↑0.993 | ↓17d | SQ | -3.7% | -66.27/-68.48 | -0.01% | 20% |
| [PASHUPATI](https://in.tradingview.com/chart/?symbol=NSE:PASHUPATI)<br><sub>📶W9 · W↑2d · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 89 | 🔄63 | ↑1.130 | ↑1d | SQ | +20.0% | -31.4/-44.71 | +19.99% | 20% |
| [INDPRUD](https://in.tradingview.com/chart/?symbol=NSE:INDPRUD)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 89 | 🔄50 | ↑1.033 | ↑1d | SQ | +6.4% | -22.19/-23.77 | +6.43% | 20% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>📶W9 · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Microfinance bank serving low-income retail borrowers India | 📈 BULL_ANY_MID | 69 | ↑74 | ↑1.011 | ↑1d | SQ | +3.4% | -34.79/-35.75 | +3.44% | 20% |
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Branded generic pharmaceuticals formulations across India Asia Africa | 📈 BULL_ANY_MID | 69 | ↑75 | ↑1.005 | ↑1d | SQ | +0.9% | 5.64/3.68 | +0.92% | 20% |
| [PANAMAPET](https://in.tradingview.com/chart/?symbol=NSE:PANAMAPET)<br><sub>📶W9 · ↑CMF4d</sub> | ✓ SAFE | Specialty petroleum products for pharma, cosmetics, rubber | 📈 BULL_ANY_MID | 69 | ↑88 | ↑1.011 | ↑1d | SQ | +2.8% | -5.85/-6.68 | +2.81% | 10% 🟨 |
| [SUPRAJIT](https://in.tradingview.com/chart/?symbol=NSE:SUPRAJIT)<br><sub>📶W9 · ↓CMF6d</sub> | ⚠ CAUTION | Automotive cables, halogen lamps, mechanical components manufacturer | 📈 BULL_ANY_MID | 69 | ↑56 | ↑1.009 | ↑1d | SQ | +1.8% | -25.94/-26.85 | +1.76% | 20% |
| [DIFFNKG](https://in.tradingview.com/chart/?symbol=NSE:DIFFNKG)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Welding consumables, wear plates, heavy machinery manufacturing | 📈 BULL_ANY_MID | 63 | ↑77 | ↑1.018 | ↑2d | SQ | +4.1% | -7.16/-8.32 | +0.90% | 20% |
| [VIDHIING](https://in.tradingview.com/chart/?symbol=NSE:VIDHIING)<br><sub>📶W9 · W↑62d · ↑CMF25d</sub> | ⚠ CAUTION | Food grade colors manufacturer serving F&B pharma confectionery | 📈 BULL_ANY_MID | 63 | ↑67 | ↑1.022 | ↑2d | SQ | +4.0% | 30.23/29.19 | +1.53% | 20% |
| [FINEORG](https://in.tradingview.com/chart/?symbol=NSE:FINEORG)<br><sub>📶W9 · ↑CMF10d</sub> | ⚠ CAUTION | Oleochemical specialty additives food plastics cosmetics coatings | 📈 BULL_ANY_MID | 60 | ↑62 | ↑1.002 | ↓10d | SQ | -0.3% | -24.31/-25.13 | +0.31% | 20% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>📶W9 · ↑CMF4d</sub> | ✓ SAFE | Condoms lubricants IVD kits sexual wellness global | 📈 BULL_ANY_MID | 59 | ↑99 | ↑1.057 | ↑1d | SQ | +8.9% | -12.75/-22.36 | +8.88% | 20% |
| [NINSYS](https://in.tradingview.com/chart/?symbol=NSE:NINSYS)<br><sub>📶W9 · ↓CMF18d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 59 | ↑85 | ↑1.031 | ↑1d | SQ | +4.4% | -9.62/-22.67 | +4.39% | 5% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · W↑30d · ↑CMF30d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.025 | ↑2d | SQ | +6.1% | 49.69/48.04 | -0.06% | 20% 🟦 |
| [ARSSBL](https://in.tradingview.com/chart/?symbol=NSE:ARSSBL)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Equity derivatives broker with MTF and financial advisory services | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.001 | ↑2d | SQ | +0.7% | -20.33/-22.09 | -0.03% | 20% |
| [GPTINFRA](https://in.tradingview.com/chart/?symbol=NSE:GPTINFRA)<br><sub>📶W9 · W↑7d · ↓CMF20d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↑47 | ↓1.004 | ↑3d | SQ | +1.9% | 14.21/13.67 | -0.47% | 20% |
| [TDPOWERSYS](https://in.tradingview.com/chart/?symbol=NSE:TDPOWERSYS)<br><sub>↑CMF0d · ÷DIV</sub> | ✓ SAFE | AC generators and motors for power generation applications | ⚡ BULL_ANY_PPV | 89 | 🔄40 | ↑1.030 | ↑1d | SQ·PV | +7.7% | -17.39/-18.96 | +7.67% | 20% |
| [HONAUT](https://in.tradingview.com/chart/?symbol=NSE:HONAUT)<br><sub>RVOL9x · ↓CMF30d</sub> | ⚠ CAUTION | Industrial automation control systems for manufacturing plants | ⚡ BULL_ANY_PPV | 57 | ↑46 | ↑0.995 | ↓8d | SQ·PV | +0.2% | -46.4/-50.81 | +0.37% | 20% |
| [BHARATWIRE](https://in.tradingview.com/chart/?symbol=NSE:BHARATWIRE)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Steel wire ropes manufacturing for industrial rigging applications | 🟡 BULL_OS_L2 | 45 | ↑32 | ↑0.992 | ↓40d | SQ | -16.6% | -59.06/-59.67 | +0.50% | 20% |
| [KERNEX](https://in.tradingview.com/chart/?symbol=NSE:KERNEX)<br><sub>↑CMF0d</sub> | ✓ SAFE | Railway safety systems and collision avoidance software manufacturer | 📈 BULL_ANY_MID | 69 | ↑76 | ↑1.011 | ↑1d | SQ | +1.8% | -22.55/-24.59 | +1.77% | 20% |
| [AGIIL](https://in.tradingview.com/chart/?symbol=NSE:AGIIL)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Real estate development and construction services Punjab region | 📈 BULL_ANY_MID | 58 | ↑29 | ↓0.984 | ↓2d | SQ | +0.1% | -49.35/-50.56 | -2.49% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LANDMARK,NSE:SJS,NSE:GLAND,NSE:SKYGOLD,NSE:DOLLAR,NSE:AZAD,NSE:KIRLOSENG,NSE:INDOCO,NSE:UNICHEMLAB,NSE:KMEW,NSE:FERMENTA,NSE:ALLDIGI,NSE:PASHUPATI,NSE:INDPRUD,NSE:UJJIVANSFB,NSE:AJANTPHARM,NSE:PANAMAPET,NSE:SUPRAJIT,NSE:DIFFNKG,NSE:VIDHIING,NSE:FINEORG,NSE:CUPID,NSE:NINSYS,NSE:MEESHO,NSE:ARSSBL,NSE:GPTINFRA,NSE:TDPOWERSYS,NSE:HONAUT,NSE:BHARATWIRE,NSE:KERNEX,NSE:AGIIL
```

---

### 🔥 MAJOR — PPV confirmed (14)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [KIRLOSBROS](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSBROS)<br><sub>📶W9 · RVOL16x · ↓CMF16d · ÷DIV</sub> | ⚠ CAUTION | Pumps and fluid systems for water, power, irrigation | ⚡ BULL_ANY_PPV | 49 | 🔄58 | ↑1.033 | ↑1d | PV | +6.7% | -39.51/-48.07 | +6.70% | 20% |
| [SENORES](https://in.tradingview.com/chart/?symbol=NSE:SENORES)<br><sub>📶W9 · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Complex generics manufacturer specialty pharma therapies India | ⚡ BULL_ANY_PPV | 43 | 🔄89 | ↑1.012 | ↓17d | PV | -1.7% | -44.53/-47.29 | +3.84% | 20% |
| [APOLLOTYRE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOTYRE)<br><sub>📶W9 · RVOL8x · ↓CMF29d · 🎯SLING</sub> | ⚠ CAUTION | Radial tyres for cars trucks farm vehicles | ⚡ BULL_ANY_PPV | 40 | 🔄30 | ↑1.005 | ↓21d | PV | -7.3% | -54.81/-58.1 | +4.40% | 20% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>📶W9 · ↑CMF9d</sub> | ✓ SAFE | Refines crude oil, produces petroleum products, lubricants | ⚡ BULL_ANY_PPV | 29 | ↑89 | ↑1.014 | ↑1d | PV | +2.0% | -0.73/-1.24 | +2.05% | 20% |
| [ELLEN](https://in.tradingview.com/chart/?symbol=NSE:ELLEN)<br><sub>📶W9 · W↑42d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Industrial oxygen nitrogen gases bulk packaged eastern southern India | ⚡ BULL_ANY_PPV | 29 | ↑80 | ↑1.014 | ↑1d | PV | +2.9% | 42.55/41.77 | +2.87% | 20% |
| [EIHOTEL](https://in.tradingview.com/chart/?symbol=NSE:EIHOTEL)<br><sub>📶W9 · W↑7d · 🚀SS · ↑CMF7d</sub> | ⚠ CAUTION | Luxury hotels, resorts, flight catering operations | ⚡ BULL_ANY_PPV | 29 | ↑30 | ↑1.011 | ↑1d | PV | +2.3% | -2.36/-3.01 | +2.29% | 20% |
| [ELECTCAST](https://in.tradingview.com/chart/?symbol=NSE:ELECTCAST)<br><sub>📶W9 · RVOL10x · ↑CMF0d</sub> | ✓ SAFE | Ductile iron pipes fittings water infrastructure manufacturing | ⚡ BULL_ANY_PPV | 24 | ↑40 | ↑1.029 | ↑1d | PV | +5.8% | -27.03/-30.56 | +5.78% | 20% |
| [ASTRAMICRO](https://in.tradingview.com/chart/?symbol=NSE:ASTRAMICRO)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | RF microwave modules defense space telecom systems | ⚡ BULL_ANY_PPV | 24 | ↑83 | ↑1.015 | ↑1d | PV | +3.9% | -39.22/-42.91 | +3.93% | 20% |
| [DPABHUSHAN](https://in.tradingview.com/chart/?symbol=NSE:DPABHUSHAN)<br><sub>📶W9 · W↑7d · RVOL45x · ↑CMF0d</sub> | ✓ SAFE | Gold diamond platinum silver jewellery retail manufacturing Central India | ⚡ BULL_ANY_PPV | 19 | ↑88 | ↑1.145 | ↑1d | PV | +20.0% | 12.87/2.57 | +20.00% | 20% |
| [PGHL](https://in.tradingview.com/chart/?symbol=NSE:PGHL)<br><sub>📶W9 · 🚀SS·12x · ↓CMF30d</sub> | ⚠ CAUTION | Vitamins minerals supplements pharmaceuticals consumer health | ⚡ BULL_ANY_PPV | 19 | ↑46 | ↑1.037 | ↑1d | PV | +5.5% | -32.15/-43.75 | +5.49% | 20% |
| [AXISCADES](https://in.tradingview.com/chart/?symbol=NSE:AXISCADES)<br><sub>📶W9 · W↑22d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Engineering design services automotive aerospace defense OEMs | ⚡ BULL_ANY_PPV | 11 | ↑81 | ↑1.089 | ↑9d | PV | +22.7% | 60.3/56.75 | +10.00% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [VESUVIUS](https://in.tradingview.com/chart/?symbol=NSE:VESUVIUS)<br><sub>🚀SS·39x · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Refractory ceramics for steel foundry molten metal flows | 🔥 BULL_OS_PPV | 59 | 🔄18 | ↑1.008 | ↑1d | PV | +3.8% | -54.42/-62.11 | +3.84% | 20% |
| [FRACTAL](https://in.tradingview.com/chart/?symbol=NSE:FRACTAL)<br><sub>↓CMF11d</sub> | ✓ SAFE | AI analytics solutions for global Fortune 500 enterprises | ⚡ BULL_ANY_PPV | 8 | ↑50 | ↑0.992 | ↓17d | PV | -8.4% | -47.75/-48.05 | +1.02% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:KIRLOSBROS,NSE:SENORES,NSE:APOLLOTYRE,NSE:CHENNPETRO,NSE:ELLEN,NSE:EIHOTEL,NSE:ELECTCAST,NSE:ASTRAMICRO,NSE:DPABHUSHAN,NSE:PGHL,NSE:AXISCADES,NSE:SIGMAADV,NSE:VESUVIUS,NSE:FRACTAL
```

### 🟢 OVERSOLD — reversal from −53/−60 (5)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [KANSAINER](https://in.tradingview.com/chart/?symbol=NSE:KANSAINER)<br><sub>↑CMF0d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Industrial and decorative paints manufacturer for buildings and industry | 🟢 BULL_OVERSOLD | 35 | 🔄19 | ↑0.995 | ↓28d | — | -10.0% | -61.58/-62.15 | +2.17% | 20% |
| [GRINFRA](https://in.tradingview.com/chart/?symbol=NSE:GRINFRA)<br><sub>↓CMF16d · 🎯SLING</sub> | ⚠ CAUTION | Road EPC contractor, highways and railways infrastructure | 🟢 BULL_OVERSOLD | 35 | 🔄19 | ↑0.996 | ↓26d | — | -7.2% | -63.05/-63.75 | +2.12% | 20% |
| [ABLBL](https://in.tradingview.com/chart/?symbol=NSE:ABLBL)<br><sub>RVOL52x · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Premium western apparel brands, Indian retail consumer market | 🟢 BULL_OVERSOLD | 5 | ↓4 | ↑0.967 | ↓42d | — | -18.7% | -70.9/-71.28 | -0.25% | 20% |
| [SPANDANA](https://in.tradingview.com/chart/?symbol=NSE:SPANDANA)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Microloans to low-income women entrepreneurs, rural semi-urban areas | 🟡 BULL_OS_L2 | 15 | ↑25 | ↓0.992 | ↓5d | — | -0.3% | -52.75/-54.8 | -0.74% | 20% |
| [SANDHAR](https://in.tradingview.com/chart/?symbol=NSE:SANDHAR)<br><sub>↓CMF23d · 🎯SLING</sub> | ✓ SAFE | Automotive safety locks and components for four-wheelers | 🟡 BULL_OS_L2 | 5 | ↑54 | ↑0.991 | ↓33d | — | -5.3% | -55.4/-56.08 | +1.07% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:KANSAINER,NSE:GRINFRA,NSE:ABLBL,NSE:SPANDANA,NSE:SANDHAR
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (10)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PRAKASH](https://in.tradingview.com/chart/?symbol=NSE:PRAKASH)<br><sub>📶W9 · ↓CMF13d · ÷DIV</sub> | ✓ SAFE | Steel manufacturing, mining, power generation integrated producer | 📈 BULL_ANY_MID | 54 | 🔄22 | ↑1.018 | ↑1d | — | +5.1% | -50.1/-52.89 | +5.13% | 20% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Stainless steel corrugated hoses assemblies fittings industrial applications | 📈 BULL_ANY_MID | 24 | ↑97 | ↑1.029 | ↑1d | — | +5.1% | 9.27/8.84 | +5.10% | 10% 🟨 |
| [JAYNECOIND](https://in.tradingview.com/chart/?symbol=NSE:JAYNECOIND)<br><sub>📶W9 · ↓CMF9d</sub> | ✓ SAFE | Ferrous castings, steel alloys, integrated mining to foundry | 📈 BULL_ANY_MID | 24 | ↑63 | ↑1.027 | ↑1d | — | +5.3% | -18.63/-20.21 | +5.32% | 20% 🟦 |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>📶W9 · W↑17d · ↑CMF10d</sub> | ✓ SAFE | Bromine lithium specialty chemicals pharma agri-chem | 📈 BULL_ANY_MID | 22 | ↑92 | ↑1.024 | ↑3d | — | +4.7% | 45.61/43.42 | +1.63% | 20% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Glass-lined reactors and process equipment for pharma chemicals | 📈 BULL_ANY_MID | 18 | ↑98 | ↑1.035 | ↑2d | — | +6.6% | 28.53/26.06 | +1.49% | 5% 🟥 |
| [SURAKSHA](https://in.tradingview.com/chart/?symbol=NSE:SURAKSHA)<br><sub>📶W9 · W↑37d · ↑CMF30d</sub> | ✓ SAFE | Pathology radiology diagnostic centers East India healthcare | 📈 BULL_ANY_MID | 17 | ↑81 | ↑1.026 | ↑8d | — | +7.9% | 38.28/38.09 | +2.31% | 20% |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 14 | ↑61 | ↑0.998 | ↓11d | — | -3.2% | -35.97/-36.7 | +0.74% | 20% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Large-diameter pipes, steel products, infrastructure | 📈 BULL_ANY_MID | 12 | ↑99 | ↑1.044 | ↑8d | — | +15.5% | 48.33/47.81 | +3.73% | 20% |
| [CARERATING](https://in.tradingview.com/chart/?symbol=NSE:CARERATING)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Credit rating agency for corporate debt securities | 📈 BULL_ANY_MID | 6 | ↑53 | ↑0.999 | ↓19d | — | -2.7% | -38.66/-38.83 | +0.58% | 20% |
| [CMPDI](https://in.tradingview.com/chart/?symbol=NSE:CMPDI)<br><sub>↓CMF13d · ÷DIV</sub> | ✓ SAFE | Coal mine planning design consultancy subsidiary CIL | 📈 BULL_ANY_MID | 42 | 🔄50 | ↑1.006 | ↓18d | — | -4.7% | -46.36/-48.36 | +3.92% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:PRAKASH,NSE:AEROFLEX,NSE:JAYNECOIND,NSE:NEOGEN,NSE:SETL,NSE:SURAKSHA,NSE:GRASIM,NSE:WELCORP,NSE:CARERATING,NSE:CMPDI
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
