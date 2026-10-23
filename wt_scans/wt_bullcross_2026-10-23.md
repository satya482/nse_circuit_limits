> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-10-23
*Generated 2026-10-23 15:46 IST*

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

**Total bull crosses today: 25** · 8 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SSWL,NSE:CHENNPETRO,NSE:KOLTEPATIL,NSE:KIRLFER,NSE:ANTELOPUS,NSE:CYIENT,NSE:JINDALPOLY,NSE:SIGMAADV,NSE:GAIL,NSE:AGARWALEYE,NSE:TMCV,NSE:SAPPHIRE,NSE:ITC,NSE:COALINDIA,NSE:CAPILLARY,NSE:NATCOPHARM,NSE:OMNI,NSE:VIJAYA,NSE:JSWSTEEL,NSE:HCG,NSE:JUBLCPL,NSE:THYROCARE,NSE:BPCL,NSE:ADANIPOWER,NSE:JINDALSTEL
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (18)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>📶W9 · W↑40d · RVOL17x · ↑CMF14d</sub> | ✓ SAFE | Steel and alloy wheel rims manufacturer for automobiles | ⚡ BULL_ANY_PPV | 89 | 🔄98 | ↑1.128 | ↑1d | SQ·PV | +20.0% | 32.49/32.24 | +19.99% | 20% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>📶W9 · ★ · ↑CMF12d</sub> | ✓ SAFE | Refines crude oil, produces petroleum products, lubricants | ⚡ BULL_ANY_PPV | 63 | ↑93 | ↑1.015 | ↑2d | SQ·PV | +2.6% | 0.55/-1.74 | +1.51% | 20% |
| [KOLTEPATIL](https://in.tradingview.com/chart/?symbol=NSE:KOLTEPATIL)<br><sub>📶W9 · W↑5d · ↓CMF10d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 58 | ↑81 | ↑1.059 | ↑2d | SQ·PV | +9.8% | -9.6/-22.09 | +6.24% | 20% |
| [KIRLFER](https://in.tradingview.com/chart/?symbol=NSE:KIRLFER)<br><sub>📶W9 · ↓CMF6d</sub> | ⚠ CAUTION | Pig iron and ferrous castings for automotive engines | ⚡ BULL_ANY_PPV | 51 | ↑50 | ↑0.993 | ↓14d | SQ·PV | -2.8% | -37.5/-38.1 | +0.02% | 20% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Oil and gas exploration production Indian subcontinent hydrocarbon resources | ⚡ BULL_ANY_PPV | 49 | 🔄96 | ↑1.077 | ↑1d | PV | +13.0% | -36.7/-43.03 | +13.00% | 20% |
| [CYIENT](https://in.tradingview.com/chart/?symbol=NSE:CYIENT)<br><sub>📶W9 · W↑60d · 🚀SS·26x · ↑CMF17d</sub> | ✓ SAFE | Engineering services, design, manufacturing digital transformation | ⚡ BULL_ANY_PPV | 19 | ↑89 | ↑1.051 | ↑1d | PV | +7.8% | 58.49/58.17 | +7.81% | 20% |
| [JINDALPOLY](https://in.tradingview.com/chart/?symbol=NSE:JINDALPOLY)<br><sub>📶W9 · W↑5d · 🚀SS·176x · ↑CMF7d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 19 | ↑90 | ↑1.075 | ↑1d | PV | +11.2% | 8.48/2.35 | +11.23% | 20% 🟦 |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄57 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [AGARWALEYE](https://in.tradingview.com/chart/?symbol=NSE:AGARWALEYE)<br><sub>📶W9 · ↑CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Eye care surgery and diagnostics across India Africa | 🟡 BULL_OS_L2 | 63 | ↑62 | ↑1.003 | ↓7d | SQ | +1.3% | -55.42/-58.31 | +1.14% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [SAPPHIRE](https://in.tradingview.com/chart/?symbol=NSE:SAPPHIRE)<br><sub>📶W9 · ↓CMF19d · 🎯SLING</sub> | ✓ SAFE | KFC Pizza Hut franchisee quick service restaurants India | 🟡 BULL_OS_L2 | 5 | ↑55 | ↑0.986 | ↓27d | — | -12.4% | -55.3/-55.31 | -0.17% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄22 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑55 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [CAPILLARY](https://in.tradingview.com/chart/?symbol=NSE:CAPILLARY)<br><sub>📶W9 · W↑25d · ↓CMF1d</sub> | ✓ SAFE | AI loyalty platforms serve enterprise retail globally | 📈 BULL_ANY_MID | 58 | ↑50 | ↑1.040 | ↑2d | SQ | +6.6% | -4.2/-10.56 | +4.32% | 20% |
| [NATCOPHARM](https://in.tradingview.com/chart/?symbol=NSE:NATCOPHARM)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | Generic oncology drugs, complex formulations, global pharma markets | 📈 BULL_ANY_MID | 20 | ↑40 | ↑0.998 | ↓5d | — | +0.9% | -47.68/-47.72 | +0.85% | 20% |
| [OMNI](https://in.tradingview.com/chart/?symbol=NSE:OMNI)<br><sub>📶W9 · ↑CMF3d</sub> | ✓ SAFE | Precision components and automation systems for industrial manufacturers | 📈 BULL_ANY_MID | 18 | ↑50 | ↓1.009 | ↑2d | — | +8.6% | 28.03/24.73 | -6.18% | 20% |
| [VIJAYA](https://in.tradingview.com/chart/?symbol=NSE:VIJAYA)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Diagnostic imaging and pathology labs, Southern India healthcare | 📈 BULL_ANY_MID | 0 | ↑83 | ↓0.998 | ↓27d | — | -3.4% | -49.21/-52.37 | -0.10% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SSWL,NSE:CHENNPETRO,NSE:KOLTEPATIL,NSE:KIRLFER,NSE:ANTELOPUS,NSE:CYIENT,NSE:JINDALPOLY,NSE:SIGMAADV,NSE:GAIL,NSE:AGARWALEYE,NSE:TMCV,NSE:SAPPHIRE,NSE:ITC,NSE:COALINDIA,NSE:CAPILLARY,NSE:NATCOPHARM,NSE:OMNI,NSE:VIJAYA
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (23)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>📶W9 · W↑40d · RVOL17x · ↑CMF14d</sub> | ✓ SAFE | Steel and alloy wheel rims manufacturer for automobiles | ⚡ BULL_ANY_PPV | 89 | 🔄98 | ↑1.128 | ↑1d | SQ·PV | +20.0% | 32.49/32.24 | +19.99% | 20% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>📶W9 · ★ · ↑CMF12d</sub> | ✓ SAFE | Refines crude oil, produces petroleum products, lubricants | ⚡ BULL_ANY_PPV | 63 | ↑93 | ↑1.015 | ↑2d | SQ·PV | +2.6% | 0.55/-1.74 | +1.51% | 20% |
| [KOLTEPATIL](https://in.tradingview.com/chart/?symbol=NSE:KOLTEPATIL)<br><sub>📶W9 · W↑5d · ↓CMF10d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 58 | ↑81 | ↑1.059 | ↑2d | SQ·PV | +9.8% | -9.6/-22.09 | +6.24% | 20% |
| [KIRLFER](https://in.tradingview.com/chart/?symbol=NSE:KIRLFER)<br><sub>📶W9 · ↓CMF6d</sub> | ⚠ CAUTION | Pig iron and ferrous castings for automotive engines | ⚡ BULL_ANY_PPV | 51 | ↑50 | ↑0.993 | ↓14d | SQ·PV | -2.8% | -37.5/-38.1 | +0.02% | 20% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Oil and gas exploration production Indian subcontinent hydrocarbon resources | ⚡ BULL_ANY_PPV | 49 | 🔄96 | ↑1.077 | ↑1d | PV | +13.0% | -36.7/-43.03 | +13.00% | 20% |
| [CYIENT](https://in.tradingview.com/chart/?symbol=NSE:CYIENT)<br><sub>📶W9 · W↑60d · 🚀SS·26x · ↑CMF17d</sub> | ✓ SAFE | Engineering services, design, manufacturing digital transformation | ⚡ BULL_ANY_PPV | 19 | ↑89 | ↑1.051 | ↑1d | PV | +7.8% | 58.49/58.17 | +7.81% | 20% |
| [JINDALPOLY](https://in.tradingview.com/chart/?symbol=NSE:JINDALPOLY)<br><sub>📶W9 · W↑5d · 🚀SS·176x · ↑CMF7d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 19 | ↑90 | ↑1.075 | ↑1d | PV | +11.2% | 8.48/2.35 | +11.23% | 20% 🟦 |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄57 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [AGARWALEYE](https://in.tradingview.com/chart/?symbol=NSE:AGARWALEYE)<br><sub>📶W9 · ↑CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Eye care surgery and diagnostics across India Africa | 🟡 BULL_OS_L2 | 63 | ↑62 | ↑1.003 | ↓7d | SQ | +1.3% | -55.42/-58.31 | +1.14% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [SAPPHIRE](https://in.tradingview.com/chart/?symbol=NSE:SAPPHIRE)<br><sub>📶W9 · ↓CMF19d · 🎯SLING</sub> | ✓ SAFE | KFC Pizza Hut franchisee quick service restaurants India | 🟡 BULL_OS_L2 | 5 | ↑55 | ↑0.986 | ↓27d | — | -12.4% | -55.3/-55.31 | -0.17% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄22 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑55 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [CAPILLARY](https://in.tradingview.com/chart/?symbol=NSE:CAPILLARY)<br><sub>📶W9 · W↑25d · ↓CMF1d</sub> | ✓ SAFE | AI loyalty platforms serve enterprise retail globally | 📈 BULL_ANY_MID | 58 | ↑50 | ↑1.040 | ↑2d | SQ | +6.6% | -4.2/-10.56 | +4.32% | 20% |
| [NATCOPHARM](https://in.tradingview.com/chart/?symbol=NSE:NATCOPHARM)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | Generic oncology drugs, complex formulations, global pharma markets | 📈 BULL_ANY_MID | 20 | ↑40 | ↑0.998 | ↓5d | — | +0.9% | -47.68/-47.72 | +0.85% | 20% |
| [OMNI](https://in.tradingview.com/chart/?symbol=NSE:OMNI)<br><sub>📶W9 · ↑CMF3d</sub> | ✓ SAFE | Precision components and automation systems for industrial manufacturers | 📈 BULL_ANY_MID | 18 | ↑50 | ↓1.009 | ↑2d | — | +8.6% | 28.03/24.73 | -6.18% | 20% |
| [VIJAYA](https://in.tradingview.com/chart/?symbol=NSE:VIJAYA)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Diagnostic imaging and pathology labs, Southern India healthcare | 📈 BULL_ANY_MID | 0 | ↑83 | ↓0.998 | ↓27d | — | -3.4% | -49.21/-52.37 | -0.10% | 20% |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 42 | 🔄54 | ↑0.992 | ↓13d | — | -5.3% | -64.43/-65.64 | +2.00% | 20% |
| [JUBLCPL](https://in.tradingview.com/chart/?symbol=NSE:JUBLCPL)<br><sub>↓CMF19d · 🎯SLING</sub> | ⚠ CAUTION | Agri nutrients, polymers, chemicals manufacturer for farms and industry | 🟢 BULL_OVERSOLD | 5 | ↑57 | ↑0.991 | ↓23d | — | -13.1% | -60.2/-61.28 | +1.36% | 20% |
| [THYROCARE](https://in.tradingview.com/chart/?symbol=NSE:THYROCARE)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Diagnostic labs thyroid tests affordable pathology services | 🟢 BULL_OVERSOLD | 0 | ↑59 | ↓0.964 | ↓25d | — | -16.7% | -65.38/-66.42 | -1.90% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 41 | 🔄38 | ↑1.001 | ↓19d | — | -4.4% | -53.92/-57.54 | +1.19% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 22 | ↑67 | ↑1.004 | ↓8d | — | -0.3% | -53.58/-59.08 | +0.30% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SSWL,NSE:CHENNPETRO,NSE:KOLTEPATIL,NSE:KIRLFER,NSE:ANTELOPUS,NSE:CYIENT,NSE:JINDALPOLY,NSE:SIGMAADV,NSE:GAIL,NSE:AGARWALEYE,NSE:TMCV,NSE:SAPPHIRE,NSE:ITC,NSE:COALINDIA,NSE:CAPILLARY,NSE:NATCOPHARM,NSE:OMNI,NSE:VIJAYA,NSE:JSWSTEEL,NSE:JUBLCPL,NSE:THYROCARE,NSE:BPCL,NSE:ADANIPOWER
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (8)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>📶W9 · W↑40d · RVOL17x · ↑CMF14d</sub> | ✓ SAFE | Steel and alloy wheel rims manufacturer for automobiles | ⚡ BULL_ANY_PPV | 89 | 🔄98 | ↑1.128 | ↑1d | SQ·PV | +20.0% | 32.49/32.24 | +19.99% | 20% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>📶W9 · ★ · ↑CMF12d</sub> | ✓ SAFE | Refines crude oil, produces petroleum products, lubricants | ⚡ BULL_ANY_PPV | 63 | ↑93 | ↑1.015 | ↑2d | SQ·PV | +2.6% | 0.55/-1.74 | +1.51% | 20% |
| [KOLTEPATIL](https://in.tradingview.com/chart/?symbol=NSE:KOLTEPATIL)<br><sub>📶W9 · W↑5d · ↓CMF10d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 58 | ↑81 | ↑1.059 | ↑2d | SQ·PV | +9.8% | -9.6/-22.09 | +6.24% | 20% |
| [KIRLFER](https://in.tradingview.com/chart/?symbol=NSE:KIRLFER)<br><sub>📶W9 · ↓CMF6d</sub> | ⚠ CAUTION | Pig iron and ferrous castings for automotive engines | ⚡ BULL_ANY_PPV | 51 | ↑50 | ↑0.993 | ↓14d | SQ·PV | -2.8% | -37.5/-38.1 | +0.02% | 20% |
| [AGARWALEYE](https://in.tradingview.com/chart/?symbol=NSE:AGARWALEYE)<br><sub>📶W9 · ↑CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Eye care surgery and diagnostics across India Africa | 🟡 BULL_OS_L2 | 63 | ↑62 | ↑1.003 | ↓7d | SQ | +1.3% | -55.42/-58.31 | +1.14% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄22 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑55 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [CAPILLARY](https://in.tradingview.com/chart/?symbol=NSE:CAPILLARY)<br><sub>📶W9 · W↑25d · ↓CMF1d</sub> | ✓ SAFE | AI loyalty platforms serve enterprise retail globally | 📈 BULL_ANY_MID | 58 | ↑50 | ↑1.040 | ↑2d | SQ | +6.6% | -4.2/-10.56 | +4.32% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SSWL,NSE:CHENNPETRO,NSE:KOLTEPATIL,NSE:KIRLFER,NSE:AGARWALEYE,NSE:ITC,NSE:COALINDIA,NSE:CAPILLARY
```

---

### 🔥 MAJOR — PPV confirmed (4)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Oil and gas exploration production Indian subcontinent hydrocarbon resources | ⚡ BULL_ANY_PPV | 49 | 🔄96 | ↑1.077 | ↑1d | PV | +13.0% | -36.7/-43.03 | +13.00% | 20% |
| [CYIENT](https://in.tradingview.com/chart/?symbol=NSE:CYIENT)<br><sub>📶W9 · W↑60d · 🚀SS·26x · ↑CMF17d</sub> | ✓ SAFE | Engineering services, design, manufacturing digital transformation | ⚡ BULL_ANY_PPV | 19 | ↑89 | ↑1.051 | ↑1d | PV | +7.8% | 58.49/58.17 | +7.81% | 20% |
| [JINDALPOLY](https://in.tradingview.com/chart/?symbol=NSE:JINDALPOLY)<br><sub>📶W9 · W↑5d · 🚀SS·176x · ↑CMF7d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 19 | ↑90 | ↑1.075 | ↑1d | PV | +11.2% | 8.48/2.35 | +11.23% | 20% 🟦 |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ANTELOPUS,NSE:CYIENT,NSE:JINDALPOLY,NSE:SIGMAADV
```

### 🟢 OVERSOLD — reversal from −53/−60 (9)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄57 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [SAPPHIRE](https://in.tradingview.com/chart/?symbol=NSE:SAPPHIRE)<br><sub>📶W9 · ↓CMF19d · 🎯SLING</sub> | ✓ SAFE | KFC Pizza Hut franchisee quick service restaurants India | 🟡 BULL_OS_L2 | 5 | ↑55 | ↑0.986 | ↓27d | — | -12.4% | -55.3/-55.31 | -0.17% | 20% |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 42 | 🔄54 | ↑0.992 | ↓13d | — | -5.3% | -64.43/-65.64 | +2.00% | 20% |
| [HCG](https://in.tradingview.com/chart/?symbol=NSE:HCG)<br><sub>↓CMF10d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Oncology hospital network, fertility services, India | 🟢 BULL_OVERSOLD | 6 | ↓34 | ↑0.954 | ↓19d | — | -20.5% | -67.44/-67.54 | -0.18% | 20% |
| [JUBLCPL](https://in.tradingview.com/chart/?symbol=NSE:JUBLCPL)<br><sub>↓CMF19d · 🎯SLING</sub> | ⚠ CAUTION | Agri nutrients, polymers, chemicals manufacturer for farms and industry | 🟢 BULL_OVERSOLD | 5 | ↑57 | ↑0.991 | ↓23d | — | -13.1% | -60.2/-61.28 | +1.36% | 20% |
| [THYROCARE](https://in.tradingview.com/chart/?symbol=NSE:THYROCARE)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Diagnostic labs thyroid tests affordable pathology services | 🟢 BULL_OVERSOLD | 0 | ↑59 | ↓0.964 | ↓25d | — | -16.7% | -65.38/-66.42 | -1.90% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 41 | 🔄38 | ↑1.001 | ↓19d | — | -4.4% | -53.92/-57.54 | +1.19% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 22 | ↑67 | ↑1.004 | ↓8d | — | -0.3% | -53.58/-59.08 | +0.30% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GAIL,NSE:TMCV,NSE:SAPPHIRE,NSE:JSWSTEEL,NSE:HCG,NSE:JUBLCPL,NSE:THYROCARE,NSE:BPCL,NSE:ADANIPOWER
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (4)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [NATCOPHARM](https://in.tradingview.com/chart/?symbol=NSE:NATCOPHARM)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | Generic oncology drugs, complex formulations, global pharma markets | 📈 BULL_ANY_MID | 20 | ↑40 | ↑0.998 | ↓5d | — | +0.9% | -47.68/-47.72 | +0.85% | 20% |
| [OMNI](https://in.tradingview.com/chart/?symbol=NSE:OMNI)<br><sub>📶W9 · ↑CMF3d</sub> | ✓ SAFE | Precision components and automation systems for industrial manufacturers | 📈 BULL_ANY_MID | 18 | ↑50 | ↓1.009 | ↑2d | — | +8.6% | 28.03/24.73 | -6.18% | 20% |
| [VIJAYA](https://in.tradingview.com/chart/?symbol=NSE:VIJAYA)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Diagnostic imaging and pathology labs, Southern India healthcare | 📈 BULL_ANY_MID | 0 | ↑83 | ↓0.998 | ↓27d | — | -3.4% | -49.21/-52.37 | -0.10% | 20% |
| [JINDALSTEL](https://in.tradingview.com/chart/?symbol=NSE:JINDALSTEL)<br><sub>↓CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 8 | ↓50 | ↑0.982 | ↓17d | — | -8.9% | -51.85/-52.67 | +0.08% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:NATCOPHARM,NSE:OMNI,NSE:VIJAYA,NSE:JINDALSTEL
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
