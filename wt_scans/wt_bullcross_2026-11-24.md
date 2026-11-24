> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-11-24
*Generated 2026-11-24 15:49 IST*

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

**Total bull crosses today: 39** · 15 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LGEINDIA,NSE:SIGMAADV,NSE:TATACONSUM,NSE:LINDEINDIA,NSE:CPPLUS,NSE:ABLBL,NSE:NELCAST,NSE:EICHERMOT,NSE:GRWRHITECH,NSE:AKCAPIT,NSE:PRESTIGE,NSE:ATHERENERG,NSE:SHREEJISPG,NSE:CONSOFINVT,NSE:BENGALASM,NSE:KUSUMGAR,NSE:NEWGEN,NSE:ELLEN,NSE:PIIND,NSE:TRUALT,NSE:3BBLACKBIO,NSE:SEDEMAC,NSE:ELANTAS,NSE:SHANTIGEAR,NSE:AJANTPHARM,NSE:ZYDUSWELL,NSE:RAINBOW,NSE:HEIDELBERG,NSE:TEJASNET,NSE:UEL,NSE:SWANCORP,NSE:BAJAJHCARE,NSE:GMMPFAUDLR,NSE:NAVA,NSE:EIDPARRY,NSE:KIRLPNU,NSE:FSL,NSE:IKS,NSE:ATUL
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (14)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [LGEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LGEINDIA)<br><sub>📶W9 · W↑10d · ↓CMF8d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 63 | ↑72 | ↑1.024 | ↑2d | SQ·PV | +3.4% | 16.11/8.84 | +1.97% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄55 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [LINDEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LINDEINDIA)<br><sub>📶W9 · W↑17d · ↑CMF14d</sub> | ⚠ CAUTION | Industrial medical gases cryogenic plants manufacturing India | 📈 BULL_ANY_MID | 18 | ↑67 | ↓1.027 | ↑2d | — | +5.9% | 29.14/28.31 | +0.00% | 20% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>📶W9 · ★ · ↓CMF12d</sub> | ✓ SAFE | CCTV cameras surveillance systems IP networks security | 📈 BULL_ANY_MID | 18 | ↑97 | ↓1.005 | ↑2d | — | +1.2% | 1.64/1.54 | +0.00% | 10% 🟩 |
| [ABLBL](https://in.tradingview.com/chart/?symbol=NSE:ABLBL)<br><sub>📶W9 · W↑22d · ↑CMF12d</sub> | ⚠ CAUTION | Premium western apparel brands, Indian retail consumer market | 📈 BULL_ANY_MID | 18 | ↑14 | ↓1.017 | ↑2d | — | +3.9% | 19.61/16.67 | +0.00% | 20% |
| [NELCAST](https://in.tradingview.com/chart/?symbol=NSE:NELCAST)<br><sub>📶W9 · W↑42d · ↑CMF30d</sub> | ✓ SAFE | Ductile grey iron castings commercial vehicle tractor sectors | 📈 BULL_ANY_MID | 18 | ↑87 | ↓1.023 | ↑2d | — | +4.6% | 7.41/6.09 | +0.00% | 20% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>📶W9 · W↑11d · ↑CMF13d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓61 | ↓1.007 | ↑15d | — | +7.0% | 46.27/45.57 | -0.67% | 20% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>📶W9 · W↑17d · ↑CMF30d</sub> | ✓ SAFE | Specialty polyester films for packaging and industrial applications | 📈 BULL_ANY_MID | 4 | ↑94 | ↓1.015 | ↑16d | — | +13.4% | 47.38/47.18 | +0.00% | 20% |
| [AKCAPIT](https://in.tradingview.com/chart/?symbol=NSE:AKCAPIT)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 4 | ↑50 | ↑1.065 | ↑16d | — | +21.2% | 72.5/71.67 | +4.52% | 20% |
| [PRESTIGE](https://in.tradingview.com/chart/?symbol=NSE:PRESTIGE)<br><sub>📶W9 · W↑17d · ↑CMF16d</sub> | ✓ SAFE | Real estate developer residential commercial retail hospitality warehouses | 📈 BULL_ANY_MID | 1 | ↑72 | ↓1.018 | ↑19d | — | +21.2% | 45.82/45.74 | +0.00% | 20% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>📶W9 · W↑17d · ★ · ↑CMF21d</sub> | ✓ SAFE | Premium electric scooters, charging network, urban mobility | 📈 BULL_ANY_MID | 0 | ↑99 | ↓1.031 | ↑22d | — | +43.4% | 50.7/50.39 | +0.00% | -% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Dry bulk carrier operations maritime logistics shipping services | 📈 BULL_ANY_MID | 0 | ↑98 | ↓1.009 | ↑22d | — | +17.2% | 55.74/55.57 | +0.00% | 20% |
| [CONSOFINVT](https://in.tradingview.com/chart/?symbol=NSE:CONSOFINVT)<br><sub>📶W9 · W↑17d · 🚀SS · ↑CMF18d</sub> | n/a |  | 📈 BULL_ANY_MID | 0 | ↑92 | ↓1.005 | ↑20d | — | +15.3% | 31.38/30.19 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LGEINDIA,NSE:SIGMAADV,NSE:TATACONSUM,NSE:LINDEINDIA,NSE:CPPLUS,NSE:ABLBL,NSE:NELCAST,NSE:EICHERMOT,NSE:GRWRHITECH,NSE:AKCAPIT,NSE:PRESTIGE,NSE:ATHERENERG,NSE:SHREEJISPG,NSE:CONSOFINVT
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (25)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [LGEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LGEINDIA)<br><sub>📶W9 · W↑10d · ↓CMF8d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 63 | ↑72 | ↑1.024 | ↑2d | SQ·PV | +3.4% | 16.11/8.84 | +1.97% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄55 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [LINDEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LINDEINDIA)<br><sub>📶W9 · W↑17d · ↑CMF14d</sub> | ⚠ CAUTION | Industrial medical gases cryogenic plants manufacturing India | 📈 BULL_ANY_MID | 18 | ↑67 | ↓1.027 | ↑2d | — | +5.9% | 29.14/28.31 | +0.00% | 20% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>📶W9 · ★ · ↓CMF12d</sub> | ✓ SAFE | CCTV cameras surveillance systems IP networks security | 📈 BULL_ANY_MID | 18 | ↑97 | ↓1.005 | ↑2d | — | +1.2% | 1.64/1.54 | +0.00% | 10% 🟩 |
| [ABLBL](https://in.tradingview.com/chart/?symbol=NSE:ABLBL)<br><sub>📶W9 · W↑22d · ↑CMF12d</sub> | ⚠ CAUTION | Premium western apparel brands, Indian retail consumer market | 📈 BULL_ANY_MID | 18 | ↑14 | ↓1.017 | ↑2d | — | +3.9% | 19.61/16.67 | +0.00% | 20% |
| [NELCAST](https://in.tradingview.com/chart/?symbol=NSE:NELCAST)<br><sub>📶W9 · W↑42d · ↑CMF30d</sub> | ✓ SAFE | Ductile grey iron castings commercial vehicle tractor sectors | 📈 BULL_ANY_MID | 18 | ↑87 | ↓1.023 | ↑2d | — | +4.6% | 7.41/6.09 | +0.00% | 20% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>📶W9 · W↑17d · ↑CMF30d</sub> | ✓ SAFE | Specialty polyester films for packaging and industrial applications | 📈 BULL_ANY_MID | 4 | ↑94 | ↓1.015 | ↑16d | — | +13.4% | 47.38/47.18 | +0.00% | 20% |
| [AKCAPIT](https://in.tradingview.com/chart/?symbol=NSE:AKCAPIT)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 4 | ↑50 | ↑1.065 | ↑16d | — | +21.2% | 72.5/71.67 | +4.52% | 20% |
| [PRESTIGE](https://in.tradingview.com/chart/?symbol=NSE:PRESTIGE)<br><sub>📶W9 · W↑17d · ↑CMF16d</sub> | ✓ SAFE | Real estate developer residential commercial retail hospitality warehouses | 📈 BULL_ANY_MID | 1 | ↑72 | ↓1.018 | ↑19d | — | +21.2% | 45.82/45.74 | +0.00% | 20% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>📶W9 · W↑17d · ★ · ↑CMF21d</sub> | ✓ SAFE | Premium electric scooters, charging network, urban mobility | 📈 BULL_ANY_MID | 0 | ↑99 | ↓1.031 | ↑22d | — | +43.4% | 50.7/50.39 | +0.00% | -% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Dry bulk carrier operations maritime logistics shipping services | 📈 BULL_ANY_MID | 0 | ↑98 | ↓1.009 | ↑22d | — | +17.2% | 55.74/55.57 | +0.00% | 20% |
| [CONSOFINVT](https://in.tradingview.com/chart/?symbol=NSE:CONSOFINVT)<br><sub>📶W9 · W↑17d · 🚀SS · ↑CMF18d</sub> | n/a |  | 📈 BULL_ANY_MID | 0 | ↑92 | ↓1.005 | ↑20d | — | +15.3% | 31.38/30.19 | +0.00% | 20% |
| [BENGALASM](https://in.tradingview.com/chart/?symbol=NSE:BENGALASM)<br><sub>↓CMF13d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄50 | ↑1.014 | ↑1d | SQ·PV | +2.5% | -38.79/-43.8 | +2.48% | 20% |
| [KUSUMGAR](https://in.tradingview.com/chart/?symbol=NSE:KUSUMGAR)<br><sub>↓CMF12d</sub> | ✓ SAFE | Synthetic fabric manufacturer, polyamide polyester polyurethane, high-performance applications | ⚡ BULL_ANY_PPV | 86 | 🔄50 | ↑1.006 | ↓14d | SQ·PV | -2.5% | -43.06/-45.24 | +1.09% | 20% |
| [3BBLACKBIO](https://in.tradingview.com/chart/?symbol=NSE:3BBLACKBIO)<br><sub>↑CMF0d</sub> | ✓ SAFE | Molecular diagnostic kits, PCR reagents, agrochemicals | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.014 | ↑1d | SQ | +2.2% | -18.47/-21.52 | +2.20% | 20% |
| [SEDEMAC](https://in.tradingview.com/chart/?symbol=NSE:SEDEMAC)<br><sub>🚀SS · ↑CMF14d</sub> | ✓ SAFE | Engine control electronics for automotive and off-highway vehicles | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.019 | ↑1d | SQ | +2.9% | -17.12/-23.4 | +2.90% | 20% |
| [ELANTAS](https://in.tradingview.com/chart/?symbol=NSE:ELANTAS)<br><sub>↑CMF30d · DEL67%</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 80 | 🔄50 | ↑1.001 | ↓30d | SQ | -11.8% | -46.51/-46.85 | +2.09% | 20% |
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Branded generic pharmaceuticals formulations across India Asia Africa | 📈 BULL_ANY_MID | 58 | ↑68 | ↑1.000 | ↓7d | SQ | +0.8% | -32.8/-34.07 | +0.00% | 20% |
| [ZYDUSWELL](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSWELL)<br><sub>↓CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Sugar substitutes glucose powders health wellness FMCG India | 📈 BULL_ANY_MID | 58 | ↑53 | ↓1.005 | ↑2d | SQ | +4.0% | -49.58/-51.39 | +0.00% | 20% |
| [RAINBOW](https://in.tradingview.com/chart/?symbol=NSE:RAINBOW)<br><sub>W↑7d · ↓CMF3d · ⚠️TRAP</sub> | ⚠ CAUTION | Pediatric obstetric gynecology hospital chain India | 📈 BULL_ANY_MID | 57 | ↑42 | ↓1.002 | ↑3d | SQ | +1.9% | 18.93/15.94 | +0.00% | 20% |
| [BAJAJHCARE](https://in.tradingview.com/chart/?symbol=NSE:BAJAJHCARE)<br><sub>↓CMF11d · ⚠️TRAP</sub> | ⚠ CAUTION | API and pharmaceutical formulation manufacturer for global markets | 📈 BULL_ANY_MID | 50 | ↑46 | ↓1.000 | ↑10d | SQ | +1.4% | 6.51/5.86 | +0.00% | 20% |
| [NAVA](https://in.tradingview.com/chart/?symbol=NSE:NAVA)<br><sub>W↑11d · ↑CMF3d</sub> | ✓ SAFE | Ferroalloys manganese producer mining power generation | 📈 BULL_ANY_MID | 17 | ↑49 | ↓1.005 | ↑3d | — | +3.7% | 21.06/19.75 | +0.00% | 20% |
| [EIDPARRY](https://in.tradingview.com/chart/?symbol=NSE:EIDPARRY)<br><sub>W↑7d · ↓CMF27d · ⚠️TRAP</sub> | ⚠ CAUTION | Sugar, nutraceuticals, ethanol, farm inputs producer | 📈 BULL_ANY_MID | 17 | ↑10 | ↓1.002 | ↑3d | — | +1.2% | -9.25/-10.75 | +0.00% | 20% |
| [KIRLPNU](https://in.tradingview.com/chart/?symbol=NSE:KIRLPNU)<br><sub>W↑11d · ↑CMF0d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE | Pneumatic compressors and gas compression systems for industrial sectors | 📈 BULL_ANY_MID | 16 | ↑3 | ↓1.005 | ↑4d | — | +3.1% | 2.19/1.6 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LGEINDIA,NSE:SIGMAADV,NSE:TATACONSUM,NSE:LINDEINDIA,NSE:CPPLUS,NSE:ABLBL,NSE:NELCAST,NSE:GRWRHITECH,NSE:AKCAPIT,NSE:PRESTIGE,NSE:ATHERENERG,NSE:SHREEJISPG,NSE:CONSOFINVT,NSE:BENGALASM,NSE:KUSUMGAR,NSE:3BBLACKBIO,NSE:SEDEMAC,NSE:ELANTAS,NSE:AJANTPHARM,NSE:ZYDUSWELL,NSE:RAINBOW,NSE:BAJAJHCARE,NSE:NAVA,NSE:EIDPARRY,NSE:KIRLPNU
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (15)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [LGEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LGEINDIA)<br><sub>📶W9 · W↑10d · ↓CMF8d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 63 | ↑72 | ↑1.024 | ↑2d | SQ·PV | +3.4% | 16.11/8.84 | +1.97% | 20% |
| [BENGALASM](https://in.tradingview.com/chart/?symbol=NSE:BENGALASM)<br><sub>↓CMF13d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄50 | ↑1.014 | ↑1d | SQ·PV | +2.5% | -38.79/-43.8 | +2.48% | 20% |
| [KUSUMGAR](https://in.tradingview.com/chart/?symbol=NSE:KUSUMGAR)<br><sub>↓CMF12d</sub> | ✓ SAFE | Synthetic fabric manufacturer, polyamide polyester polyurethane, high-performance applications | ⚡ BULL_ANY_PPV | 86 | 🔄50 | ↑1.006 | ↓14d | SQ·PV | -2.5% | -43.06/-45.24 | +1.09% | 20% |
| [3BBLACKBIO](https://in.tradingview.com/chart/?symbol=NSE:3BBLACKBIO)<br><sub>↑CMF0d</sub> | ✓ SAFE | Molecular diagnostic kits, PCR reagents, agrochemicals | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.014 | ↑1d | SQ | +2.2% | -18.47/-21.52 | +2.20% | 20% |
| [SEDEMAC](https://in.tradingview.com/chart/?symbol=NSE:SEDEMAC)<br><sub>🚀SS · ↑CMF14d</sub> | ✓ SAFE | Engine control electronics for automotive and off-highway vehicles | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.019 | ↑1d | SQ | +2.9% | -17.12/-23.4 | +2.90% | 20% |
| [ELANTAS](https://in.tradingview.com/chart/?symbol=NSE:ELANTAS)<br><sub>↑CMF30d · DEL67%</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 80 | 🔄50 | ↑1.001 | ↓30d | SQ | -11.8% | -46.51/-46.85 | +2.09% | 20% |
| [SHANTIGEAR](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGEAR)<br><sub>↑CMF3d · ⚠️TRAP</sub> | ⚠ CAUTION | Precision gears and gearboxes for industrial machinery | 📈 BULL_ANY_MID | 61 | ↓65 | ↑0.996 | ↓4d | SQ | +1.1% | -4.87/-4.92 | +0.00% | 5% 🟥 |
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Branded generic pharmaceuticals formulations across India Asia Africa | 📈 BULL_ANY_MID | 58 | ↑68 | ↑1.000 | ↓7d | SQ | +0.8% | -32.8/-34.07 | +0.00% | 20% |
| [ZYDUSWELL](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSWELL)<br><sub>↓CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Sugar substitutes glucose powders health wellness FMCG India | 📈 BULL_ANY_MID | 58 | ↑53 | ↓1.005 | ↑2d | SQ | +4.0% | -49.58/-51.39 | +0.00% | 20% |
| [RAINBOW](https://in.tradingview.com/chart/?symbol=NSE:RAINBOW)<br><sub>W↑7d · ↓CMF3d · ⚠️TRAP</sub> | ⚠ CAUTION | Pediatric obstetric gynecology hospital chain India | 📈 BULL_ANY_MID | 57 | ↑42 | ↓1.002 | ↑3d | SQ | +1.9% | 18.93/15.94 | +0.00% | 20% |
| [HEIDELBERG](https://in.tradingview.com/chart/?symbol=NSE:HEIDELBERG)<br><sub>W↑7d · ↑CMF14d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 57 | ↓6 | ↑0.995 | ↓8d | SQ | -1.8% | -51.78/-51.99 | +0.00% | 20% |
| [TEJASNET](https://in.tradingview.com/chart/?symbol=NSE:TEJASNET)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Optical and wireless networking equipment for telecom operators | 📈 BULL_ANY_MID | 56 | ↓24 | ↑0.985 | ↓9d | SQ | -4.8% | -49.63/-49.77 | +0.00% | 20% |
| [UEL](https://in.tradingview.com/chart/?symbol=NSE:UEL)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Solar power generation, EV manufacturing, renewable energy sector | 📈 BULL_ANY_MID | 53 | ↓69 | ↑0.984 | ↓12d | SQ | -4.3% | -42.87/-43.02 | +0.00% | 10% 🟩 |
| [SWANCORP](https://in.tradingview.com/chart/?symbol=NSE:SWANCORP)<br><sub>W↑7d · 🚀SS · ↓CMF13d · ⚠️TRAP</sub> | ✓ SAFE | Textiles manufacturing, real estate development, energy sector conglomerate | 📈 BULL_ANY_MID | 51 | ↓3 | ↑0.988 | ↓14d | SQ | -6.0% | -50.29/-50.92 | +0.00% | 20% |
| [BAJAJHCARE](https://in.tradingview.com/chart/?symbol=NSE:BAJAJHCARE)<br><sub>↓CMF11d · ⚠️TRAP</sub> | ⚠ CAUTION | API and pharmaceutical formulation manufacturer for global markets | 📈 BULL_ANY_MID | 50 | ↑46 | ↓1.000 | ↑10d | SQ | +1.4% | 6.51/5.86 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LGEINDIA,NSE:BENGALASM,NSE:KUSUMGAR,NSE:3BBLACKBIO,NSE:SEDEMAC,NSE:ELANTAS,NSE:SHANTIGEAR,NSE:AJANTPHARM,NSE:ZYDUSWELL,NSE:RAINBOW,NSE:HEIDELBERG,NSE:TEJASNET,NSE:UEL,NSE:SWANCORP,NSE:BAJAJHCARE
```

---

### 🔥 MAJOR — PPV confirmed (1)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV
```

### 🟢 OVERSOLD — reversal from −53/−60 (4)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [NEWGEN](https://in.tradingview.com/chart/?symbol=NSE:NEWGEN)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Digital transformation platform automation software for enterprises | 🟢 BULL_OVERSOLD | 5 | ↓5 | ↑0.973 | ↓22d | — | -9.5% | -64.47/-64.92 | +0.00% | 20% |
| [ELLEN](https://in.tradingview.com/chart/?symbol=NSE:ELLEN)<br><sub>↓CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Industrial oxygen nitrogen gases bulk packaged eastern southern India | 🟡 BULL_OS_L2 | 9 | ↓48 | ↑0.994 | ↓16d | — | -11.7% | -53.88/-55.95 | +0.00% | 20% |
| [PIIND](https://in.tradingview.com/chart/?symbol=NSE:PIIND)<br><sub>🚀SS · ↓CMF13d · ⚠️TRAP</sub> | ✓ SAFE | Agrochemicals and custom synthesis manufacturing for global clients | 🟡 BULL_OS_L2 | 8 | ↓1 | ↑0.945 | ↓17d | — | -25.2% | -57.21/-57.53 | +0.00% | 20% |
| [TRUALT](https://in.tradingview.com/chart/?symbol=NSE:TRUALT)<br><sub>↓CMF12d · ⚠️TRAP</sub> | ✓ SAFE | Ethanol and biogas producer, renewable energy, fuel sector | 🟡 BULL_OS_L2 | 5 | ↓8 | ↑0.971 | ↓32d | — | -23.1% | -59.2/-59.77 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:NEWGEN,NSE:ELLEN,NSE:PIIND,NSE:TRUALT
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (19)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄55 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [LINDEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LINDEINDIA)<br><sub>📶W9 · W↑17d · ↑CMF14d</sub> | ⚠ CAUTION | Industrial medical gases cryogenic plants manufacturing India | 📈 BULL_ANY_MID | 18 | ↑67 | ↓1.027 | ↑2d | — | +5.9% | 29.14/28.31 | +0.00% | 20% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>📶W9 · ★ · ↓CMF12d</sub> | ✓ SAFE | CCTV cameras surveillance systems IP networks security | 📈 BULL_ANY_MID | 18 | ↑97 | ↓1.005 | ↑2d | — | +1.2% | 1.64/1.54 | +0.00% | 10% 🟩 |
| [ABLBL](https://in.tradingview.com/chart/?symbol=NSE:ABLBL)<br><sub>📶W9 · W↑22d · ↑CMF12d</sub> | ⚠ CAUTION | Premium western apparel brands, Indian retail consumer market | 📈 BULL_ANY_MID | 18 | ↑14 | ↓1.017 | ↑2d | — | +3.9% | 19.61/16.67 | +0.00% | 20% |
| [NELCAST](https://in.tradingview.com/chart/?symbol=NSE:NELCAST)<br><sub>📶W9 · W↑42d · ↑CMF30d</sub> | ✓ SAFE | Ductile grey iron castings commercial vehicle tractor sectors | 📈 BULL_ANY_MID | 18 | ↑87 | ↓1.023 | ↑2d | — | +4.6% | 7.41/6.09 | +0.00% | 20% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>📶W9 · W↑11d · ↑CMF13d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓61 | ↓1.007 | ↑15d | — | +7.0% | 46.27/45.57 | -0.67% | 20% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>📶W9 · W↑17d · ↑CMF30d</sub> | ✓ SAFE | Specialty polyester films for packaging and industrial applications | 📈 BULL_ANY_MID | 4 | ↑94 | ↓1.015 | ↑16d | — | +13.4% | 47.38/47.18 | +0.00% | 20% |
| [AKCAPIT](https://in.tradingview.com/chart/?symbol=NSE:AKCAPIT)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 4 | ↑50 | ↑1.065 | ↑16d | — | +21.2% | 72.5/71.67 | +4.52% | 20% |
| [PRESTIGE](https://in.tradingview.com/chart/?symbol=NSE:PRESTIGE)<br><sub>📶W9 · W↑17d · ↑CMF16d</sub> | ✓ SAFE | Real estate developer residential commercial retail hospitality warehouses | 📈 BULL_ANY_MID | 1 | ↑72 | ↓1.018 | ↑19d | — | +21.2% | 45.82/45.74 | +0.00% | 20% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>📶W9 · W↑17d · ★ · ↑CMF21d</sub> | ✓ SAFE | Premium electric scooters, charging network, urban mobility | 📈 BULL_ANY_MID | 0 | ↑99 | ↓1.031 | ↑22d | — | +43.4% | 50.7/50.39 | +0.00% | -% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Dry bulk carrier operations maritime logistics shipping services | 📈 BULL_ANY_MID | 0 | ↑98 | ↓1.009 | ↑22d | — | +17.2% | 55.74/55.57 | +0.00% | 20% |
| [CONSOFINVT](https://in.tradingview.com/chart/?symbol=NSE:CONSOFINVT)<br><sub>📶W9 · W↑17d · 🚀SS · ↑CMF18d</sub> | n/a |  | 📈 BULL_ANY_MID | 0 | ↑92 | ↓1.005 | ↑20d | — | +15.3% | 31.38/30.19 | +0.00% | 20% |
| [GMMPFAUDLR](https://in.tradingview.com/chart/?symbol=NSE:GMMPFAUDLR)<br><sub>↓CMF26d · ⚠️TRAP</sub> | ✓ SAFE | Glass-lined equipment, pharma chemicals, corrosion resistance solutions | 📈 BULL_ANY_MID | 17 | ↓82 | ↑0.993 | ↓8d | — | -4.0% | -33.82/-36.03 | +0.00% | 20% |
| [NAVA](https://in.tradingview.com/chart/?symbol=NSE:NAVA)<br><sub>W↑11d · ↑CMF3d</sub> | ✓ SAFE | Ferroalloys manganese producer mining power generation | 📈 BULL_ANY_MID | 17 | ↑49 | ↓1.005 | ↑3d | — | +3.7% | 21.06/19.75 | +0.00% | 20% |
| [EIDPARRY](https://in.tradingview.com/chart/?symbol=NSE:EIDPARRY)<br><sub>W↑7d · ↓CMF27d · ⚠️TRAP</sub> | ⚠ CAUTION | Sugar, nutraceuticals, ethanol, farm inputs producer | 📈 BULL_ANY_MID | 17 | ↑10 | ↓1.002 | ↑3d | — | +1.2% | -9.25/-10.75 | +0.00% | 20% |
| [KIRLPNU](https://in.tradingview.com/chart/?symbol=NSE:KIRLPNU)<br><sub>W↑11d · ↑CMF0d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE | Pneumatic compressors and gas compression systems for industrial sectors | 📈 BULL_ANY_MID | 16 | ↑3 | ↓1.005 | ↑4d | — | +3.1% | 2.19/1.6 | +0.00% | 20% |
| [FSL](https://in.tradingview.com/chart/?symbol=NSE:FSL)<br><sub>↓CMF3d</sub> | ✓ SAFE | BPM services for healthcare insurance banking finance | 📈 BULL_ANY_MID | 12 | ↓65 | ↑0.999 | ↓13d | — | -1.9% | -17.28/-19.26 | +0.00% | 20% |
| [IKS](https://in.tradingview.com/chart/?symbol=NSE:IKS)<br><sub>🚀SS · ↓CMF3d · ⚠️TRAP</sub> | ⚠ CAUTION | Healthcare IT platform optimizing provider revenue operations US | 📈 BULL_ANY_MID | 6 | ↓49 | ↑0.984 | ↓19d | — | -5.3% | -39.52/-40.34 | +0.00% | 20% |
| [ATUL](https://in.tradingview.com/chart/?symbol=NSE:ATUL)<br><sub>🚀SS · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Specialty chemicals for pharma agrochemical and industrial applications | 📈 BULL_ANY_MID | 5 | ↓12 | ↑0.987 | ↓29d | — | -15.7% | -48.79/-48.93 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:TATACONSUM,NSE:LINDEINDIA,NSE:CPPLUS,NSE:ABLBL,NSE:NELCAST,NSE:EICHERMOT,NSE:GRWRHITECH,NSE:AKCAPIT,NSE:PRESTIGE,NSE:ATHERENERG,NSE:SHREEJISPG,NSE:CONSOFINVT,NSE:GMMPFAUDLR,NSE:NAVA,NSE:EIDPARRY,NSE:KIRLPNU,NSE:FSL,NSE:IKS,NSE:ATUL
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
