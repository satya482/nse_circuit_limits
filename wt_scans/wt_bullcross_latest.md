> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-10-19
*Generated 2026-10-19 15:44 IST*

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

**Total bull crosses today: 37** · 7 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:IXIGO,NSE:RAJRATAN,NSE:J&KBANK,NSE:BANKINDIA,NSE:INDNIPPON,NSE:JAYBARMARU,NSE:SIGMAADV,NSE:GAIL,NSE:TMCV,NSE:KIRLOSBROS,NSE:ITC,NSE:MANAKCOAT,NSE:COALINDIA,NSE:DISAQ,NSE:RATNAVEER,NSE:VENTIVE,NSE:LANDMARK,NSE:CCAVENUE,NSE:POONAWALLA,NSE:PREMEXPLN,NSE:KMEW,NSE:SHANTIGOLD,NSE:SUPRIYA,NSE:NATCOPHARM,NSE:JSWSTEEL,NSE:MOLDTKPAC,NSE:BPCL,NSE:YATRA,NSE:LMW,NSE:ADANIPOWER,NSE:JLHL,NSE:HITECH,NSE:TVSSRICHAK,NSE:BUILDPRO,NSE:BLSE,NSE:JINDALSTEL,NSE:GPTHEALTH
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (23)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [IXIGO](https://in.tradingview.com/chart/?symbol=NSE:IXIGO)<br><sub>📶W9 · 🚀SS·61x · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Rail bus flight hotel booking aggregator platform | 🔥 BULL_OS_PPV | 49 | 🔄8 | ↑1.055 | ↑1d | PV | +8.7% | -53.34/-63.88 | +8.74% | 20% |
| [RAJRATAN](https://in.tradingview.com/chart/?symbol=NSE:RAJRATAN)<br><sub>📶W9 · 🚀SS · ↓CMF1d</sub> | ✓ SAFE | High-carbon steel wire manufacturer for global tire production | ⚡ BULL_ANY_PPV | 99 | 🔄62 | ↑1.004 | ↑1d | SQ·PV | +1.7% | -39.28/-40.64 | +1.72% | 20% |
| [J&KBANK](https://in.tradingview.com/chart/?symbol=NSE:J&KBANK)<br><sub>📶W9 · 🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Retail corporate banking services Jammu Kashmir Ladakh regions | ⚡ BULL_ANY_PPV | 59 | 🔄66 | ↑1.007 | ↑1d | PV | +3.7% | -53.66/-53.88 | +3.74% | 20% |
| [BANKINDIA](https://in.tradingview.com/chart/?symbol=NSE:BANKINDIA)<br><sub>📶W9 · 🚀SS · ↓CMF19d</sub> | ✓ SAFE | Public sector bank retail corporate MSME lending | ⚡ BULL_ANY_PPV | 54 | 🔄46 | ↑1.023 | ↑1d | PV | +3.3% | -20.89/-27.2 | +3.34% | 20% |
| [INDNIPPON](https://in.tradingview.com/chart/?symbol=NSE:INDNIPPON)<br><sub>📶W9 · ↓CMF27d</sub> | ✓ SAFE | Two-wheeler ignition systems manufacturer for automotive sector | ⚡ BULL_ANY_PPV | 54 | 🔄82 | ↑1.017 | ↑1d | PV | +5.2% | -36.15/-37.21 | +5.21% | 20% |
| [JAYBARMARU](https://in.tradingview.com/chart/?symbol=NSE:JAYBARMARU)<br><sub>📶W9 · ↑CMF13d</sub> | ✓ SAFE | Auto parts supplier to Maruti Suzuki passenger vehicles | ⚡ BULL_ANY_PPV | 49 | 🔄75 | ↑1.039 | ↑1d | PV | +7.5% | 0.13/-1.15 | +7.49% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄56 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [KIRLOSBROS](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSBROS)<br><sub>📶W9 · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Pumps and fluid systems for water, power, irrigation | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.001 | ↓15d | — | -1.1% | -53.46/-54.76 | +1.84% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄21 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [MANAKCOAT](https://in.tradingview.com/chart/?symbol=NSE:MANAKCOAT)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF5d</sub> | ✓ SAFE | Pre-painted steel coils and sheets manufacturing for construction | 📈 BULL_ANY_MID | 94 | 🔄59 | ↑1.017 | ↑1d | SQ | +3.4% | 2.37/2.23 | +3.40% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑53 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [DISAQ](https://in.tradingview.com/chart/?symbol=NSE:DISAQ)<br><sub>📶W9 · ↓CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 59 | 🔄50 | ↑1.014 | ↑1d | — | +2.6% | -38.38/-39.62 | +2.64% | 20% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Stainless steel washers tubes pipes solar mounting components | 📈 BULL_ANY_MID | 58 | ↑99 | ↑1.036 | ↑2d | SQ | +6.2% | 35.6/29.66 | +2.16% | 20% |
| [VENTIVE](https://in.tradingview.com/chart/?symbol=NSE:VENTIVE)<br><sub>📶W9 · W↑1d · ↓CMF8d</sub> | ⚠ CAUTION | Luxury hotel owner operator developer India resorts | 📈 BULL_ANY_MID | 58 | ↑25 | ↓1.000 | ↓2d | SQ | +1.4% | -30.21/-32.65 | -0.49% | 20% |
| [LANDMARK](https://in.tradingview.com/chart/?symbol=NSE:LANDMARK)<br><sub>📶W9 · ↓CMF15d</sub> | ✓ SAFE | Premium multi-brand auto retail, luxury car dealerships | 📈 BULL_ANY_MID | 50 | ↑52 | ↑1.005 | ↓22d | SQ | -4.4% | -37.64/-41.24 | +1.02% | 20% |
| [CCAVENUE](https://in.tradingview.com/chart/?symbol=NSE:CCAVENUE)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄100 | ↑3.588 | ↑1d | — | +765.8% | 6.99/-15.88 | +765.77% | 20% |
| [POONAWALLA](https://in.tradingview.com/chart/?symbol=NSE:POONAWALLA)<br><sub>📶W9 · ↓CMF5d</sub> | ✓ SAFE | NBFC consumer loans MSME financing general insurance | 📈 BULL_ANY_MID | 18 | ↑46 | ↓1.002 | ↓2d | — | +1.4% | -21.3/-23.51 | -0.72% | 20% |
| [PREMEXPLN](https://in.tradingview.com/chart/?symbol=NSE:PREMEXPLN)<br><sub>📶W9 · W↑21d · ↑CMF8d</sub> | ✓ SAFE | Explosives propellants detonators defense space mining | 📈 BULL_ANY_MID | 10 | ↑78 | ↑1.006 | ↑30d | — | +4.5% | 60.61/60.15 | +0.21% | 20% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>📶W9 · W↑11d · ↑CMF15d</sub> | ✓ SAFE | Dredging, marine craft repair, maritime infrastructure engineering | 📈 BULL_ANY_MID | 5 | ↑97 | ↓1.027 | ↑15d | — | +15.5% | 58.09/57.87 | -0.11% | 20% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>📶W9 · W↑56d · ↑CMF18d</sub> | ✓ SAFE | Gold casting jewellery design manufacturing retail consumer ornaments | 📈 BULL_ANY_MID | 0 | ↑98 | ↓1.089 | ↑21d | — | +65.0% | 73.54/73.36 | -2.04% | 20% |
| [SUPRIYA](https://in.tradingview.com/chart/?symbol=NSE:SUPRIYA)<br><sub>📶W9 · ↓CMF0d · ⚠️TRAP</sub> | ✓ SAFE | API manufacturer, antihistamine analgesic anaesthetic pharma exports | 📈 BULL_ANY_MID | 0 | ↑74 | ↓0.988 | ↓34d | — | +8.7% | -18.41/-18.65 | -1.44% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:IXIGO,NSE:RAJRATAN,NSE:J&KBANK,NSE:BANKINDIA,NSE:INDNIPPON,NSE:JAYBARMARU,NSE:SIGMAADV,NSE:GAIL,NSE:TMCV,NSE:KIRLOSBROS,NSE:ITC,NSE:MANAKCOAT,NSE:COALINDIA,NSE:DISAQ,NSE:RATNAVEER,NSE:VENTIVE,NSE:LANDMARK,NSE:CCAVENUE,NSE:POONAWALLA,NSE:PREMEXPLN,NSE:KMEW,NSE:SHANTIGOLD,NSE:SUPRIYA
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (31)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [IXIGO](https://in.tradingview.com/chart/?symbol=NSE:IXIGO)<br><sub>📶W9 · 🚀SS·61x · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Rail bus flight hotel booking aggregator platform | 🔥 BULL_OS_PPV | 49 | 🔄8 | ↑1.055 | ↑1d | PV | +8.7% | -53.34/-63.88 | +8.74% | 20% |
| [RAJRATAN](https://in.tradingview.com/chart/?symbol=NSE:RAJRATAN)<br><sub>📶W9 · 🚀SS · ↓CMF1d</sub> | ✓ SAFE | High-carbon steel wire manufacturer for global tire production | ⚡ BULL_ANY_PPV | 99 | 🔄62 | ↑1.004 | ↑1d | SQ·PV | +1.7% | -39.28/-40.64 | +1.72% | 20% |
| [J&KBANK](https://in.tradingview.com/chart/?symbol=NSE:J&KBANK)<br><sub>📶W9 · 🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Retail corporate banking services Jammu Kashmir Ladakh regions | ⚡ BULL_ANY_PPV | 59 | 🔄66 | ↑1.007 | ↑1d | PV | +3.7% | -53.66/-53.88 | +3.74% | 20% |
| [BANKINDIA](https://in.tradingview.com/chart/?symbol=NSE:BANKINDIA)<br><sub>📶W9 · 🚀SS · ↓CMF19d</sub> | ✓ SAFE | Public sector bank retail corporate MSME lending | ⚡ BULL_ANY_PPV | 54 | 🔄46 | ↑1.023 | ↑1d | PV | +3.3% | -20.89/-27.2 | +3.34% | 20% |
| [INDNIPPON](https://in.tradingview.com/chart/?symbol=NSE:INDNIPPON)<br><sub>📶W9 · ↓CMF27d</sub> | ✓ SAFE | Two-wheeler ignition systems manufacturer for automotive sector | ⚡ BULL_ANY_PPV | 54 | 🔄82 | ↑1.017 | ↑1d | PV | +5.2% | -36.15/-37.21 | +5.21% | 20% |
| [JAYBARMARU](https://in.tradingview.com/chart/?symbol=NSE:JAYBARMARU)<br><sub>📶W9 · ↑CMF13d</sub> | ✓ SAFE | Auto parts supplier to Maruti Suzuki passenger vehicles | ⚡ BULL_ANY_PPV | 49 | 🔄75 | ↑1.039 | ↑1d | PV | +7.5% | 0.13/-1.15 | +7.49% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄56 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [KIRLOSBROS](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSBROS)<br><sub>📶W9 · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Pumps and fluid systems for water, power, irrigation | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.001 | ↓15d | — | -1.1% | -53.46/-54.76 | +1.84% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄21 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [MANAKCOAT](https://in.tradingview.com/chart/?symbol=NSE:MANAKCOAT)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF5d</sub> | ✓ SAFE | Pre-painted steel coils and sheets manufacturing for construction | 📈 BULL_ANY_MID | 94 | 🔄59 | ↑1.017 | ↑1d | SQ | +3.4% | 2.37/2.23 | +3.40% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑53 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [DISAQ](https://in.tradingview.com/chart/?symbol=NSE:DISAQ)<br><sub>📶W9 · ↓CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 59 | 🔄50 | ↑1.014 | ↑1d | — | +2.6% | -38.38/-39.62 | +2.64% | 20% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Stainless steel washers tubes pipes solar mounting components | 📈 BULL_ANY_MID | 58 | ↑99 | ↑1.036 | ↑2d | SQ | +6.2% | 35.6/29.66 | +2.16% | 20% |
| [VENTIVE](https://in.tradingview.com/chart/?symbol=NSE:VENTIVE)<br><sub>📶W9 · W↑1d · ↓CMF8d</sub> | ⚠ CAUTION | Luxury hotel owner operator developer India resorts | 📈 BULL_ANY_MID | 58 | ↑25 | ↓1.000 | ↓2d | SQ | +1.4% | -30.21/-32.65 | -0.49% | 20% |
| [LANDMARK](https://in.tradingview.com/chart/?symbol=NSE:LANDMARK)<br><sub>📶W9 · ↓CMF15d</sub> | ✓ SAFE | Premium multi-brand auto retail, luxury car dealerships | 📈 BULL_ANY_MID | 50 | ↑52 | ↑1.005 | ↓22d | SQ | -4.4% | -37.64/-41.24 | +1.02% | 20% |
| [CCAVENUE](https://in.tradingview.com/chart/?symbol=NSE:CCAVENUE)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄100 | ↑3.588 | ↑1d | — | +765.8% | 6.99/-15.88 | +765.77% | 20% |
| [POONAWALLA](https://in.tradingview.com/chart/?symbol=NSE:POONAWALLA)<br><sub>📶W9 · ↓CMF5d</sub> | ✓ SAFE | NBFC consumer loans MSME financing general insurance | 📈 BULL_ANY_MID | 18 | ↑46 | ↓1.002 | ↓2d | — | +1.4% | -21.3/-23.51 | -0.72% | 20% |
| [PREMEXPLN](https://in.tradingview.com/chart/?symbol=NSE:PREMEXPLN)<br><sub>📶W9 · W↑21d · ↑CMF8d</sub> | ✓ SAFE | Explosives propellants detonators defense space mining | 📈 BULL_ANY_MID | 10 | ↑78 | ↑1.006 | ↑30d | — | +4.5% | 60.61/60.15 | +0.21% | 20% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>📶W9 · W↑11d · ↑CMF15d</sub> | ✓ SAFE | Dredging, marine craft repair, maritime infrastructure engineering | 📈 BULL_ANY_MID | 5 | ↑97 | ↓1.027 | ↑15d | — | +15.5% | 58.09/57.87 | -0.11% | 20% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>📶W9 · W↑56d · ↑CMF18d</sub> | ✓ SAFE | Gold casting jewellery design manufacturing retail consumer ornaments | 📈 BULL_ANY_MID | 0 | ↑98 | ↓1.089 | ↑21d | — | +65.0% | 73.54/73.36 | -2.04% | 20% |
| [SUPRIYA](https://in.tradingview.com/chart/?symbol=NSE:SUPRIYA)<br><sub>📶W9 · ↓CMF0d · ⚠️TRAP</sub> | ✓ SAFE | API manufacturer, antihistamine analgesic anaesthetic pharma exports | 📈 BULL_ANY_MID | 0 | ↑74 | ↓0.988 | ↓34d | — | +8.7% | -18.41/-18.65 | -1.44% | 20% |
| [NATCOPHARM](https://in.tradingview.com/chart/?symbol=NSE:NATCOPHARM)<br><sub>↑CMF12d · 🎯SLING</sub> | ✓ SAFE | Generic oncology drugs, complex formulations, global pharma markets | ⚡ BULL_ANY_PPV | 59 | 🔄31 | ↑1.004 | ↑1d | PV | +2.0% | -50.69/-53.34 | +2.01% | 20% |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 42 | 🔄52 | ↑0.992 | ↓13d | — | -5.3% | -64.43/-65.64 | +2.00% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 41 | 🔄36 | ↑1.001 | ↓19d | — | -4.4% | -53.92/-57.54 | +1.19% | 20% |
| [YATRA](https://in.tradingview.com/chart/?symbol=NSE:YATRA)<br><sub>🚀SS · ↓CMF14d · 🎯SLING</sub> | ✓ SAFE | Online travel bookings for leisure and corporate travelers | 🟡 BULL_OS_L2 | 35 | 🔄11 | ↑0.995 | ↓35d | — | -9.0% | -50.57/-53.89 | +0.99% | 20% |
| [LMW](https://in.tradingview.com/chart/?symbol=NSE:LMW)<br><sub>↓CMF27d · 🎯SLING</sub> | ⚠ CAUTION | Textile spinning machinery and CNC machine tools manufacturer | 🟡 BULL_OS_L2 | 35 | 🔄66 | ↑0.999 | ↓33d | — | -13.3% | -54.37/-56.25 | +1.39% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 22 | ↑66 | ↑1.004 | ↓8d | — | -0.3% | -53.58/-59.08 | +0.30% | 20% |
| [HITECH](https://in.tradingview.com/chart/?symbol=NSE:HITECH)<br><sub>🚀SS · ↓CMF3d</sub> | ✓ SAFE | ERW steel pipes tubes construction automotive infrastructure | 📈 BULL_ANY_MID | 45 | 🔄12 | ↑0.997 | ↓10d | — | +1.5% | -47.37/-49.09 | +0.57% | 20% |
| [TVSSRICHAK](https://in.tradingview.com/chart/?symbol=NSE:TVSSRICHAK)<br><sub>↓CMF18d</sub> | ⚠ CAUTION | Two-wheeler three-wheeler off-highway tyres manufacturer exporter | 📈 BULL_ANY_MID | 30 | 🔄69 | ↓0.992 | ↓48d | — | +11.1% | -40.94/-41.1 | -0.40% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:IXIGO,NSE:RAJRATAN,NSE:J&KBANK,NSE:BANKINDIA,NSE:INDNIPPON,NSE:JAYBARMARU,NSE:SIGMAADV,NSE:GAIL,NSE:TMCV,NSE:KIRLOSBROS,NSE:ITC,NSE:MANAKCOAT,NSE:COALINDIA,NSE:DISAQ,NSE:RATNAVEER,NSE:VENTIVE,NSE:LANDMARK,NSE:CCAVENUE,NSE:POONAWALLA,NSE:PREMEXPLN,NSE:KMEW,NSE:SHANTIGOLD,NSE:SUPRIYA,NSE:NATCOPHARM,NSE:JSWSTEEL,NSE:BPCL,NSE:YATRA,NSE:LMW,NSE:ADANIPOWER,NSE:HITECH,NSE:TVSSRICHAK
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (7)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [RAJRATAN](https://in.tradingview.com/chart/?symbol=NSE:RAJRATAN)<br><sub>📶W9 · 🚀SS · ↓CMF1d</sub> | ✓ SAFE | High-carbon steel wire manufacturer for global tire production | ⚡ BULL_ANY_PPV | 99 | 🔄62 | ↑1.004 | ↑1d | SQ·PV | +1.7% | -39.28/-40.64 | +1.72% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄21 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [MANAKCOAT](https://in.tradingview.com/chart/?symbol=NSE:MANAKCOAT)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF5d</sub> | ✓ SAFE | Pre-painted steel coils and sheets manufacturing for construction | 📈 BULL_ANY_MID | 94 | 🔄59 | ↑1.017 | ↑1d | SQ | +3.4% | 2.37/2.23 | +3.40% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑53 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Stainless steel washers tubes pipes solar mounting components | 📈 BULL_ANY_MID | 58 | ↑99 | ↑1.036 | ↑2d | SQ | +6.2% | 35.6/29.66 | +2.16% | 20% |
| [VENTIVE](https://in.tradingview.com/chart/?symbol=NSE:VENTIVE)<br><sub>📶W9 · W↑1d · ↓CMF8d</sub> | ⚠ CAUTION | Luxury hotel owner operator developer India resorts | 📈 BULL_ANY_MID | 58 | ↑25 | ↓1.000 | ↓2d | SQ | +1.4% | -30.21/-32.65 | -0.49% | 20% |
| [LANDMARK](https://in.tradingview.com/chart/?symbol=NSE:LANDMARK)<br><sub>📶W9 · ↓CMF15d</sub> | ✓ SAFE | Premium multi-brand auto retail, luxury car dealerships | 📈 BULL_ANY_MID | 50 | ↑52 | ↑1.005 | ↓22d | SQ | -4.4% | -37.64/-41.24 | +1.02% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:RAJRATAN,NSE:ITC,NSE:MANAKCOAT,NSE:COALINDIA,NSE:RATNAVEER,NSE:VENTIVE,NSE:LANDMARK
```

---

### 🔥 MAJOR — PPV confirmed (7)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [IXIGO](https://in.tradingview.com/chart/?symbol=NSE:IXIGO)<br><sub>📶W9 · 🚀SS·61x · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Rail bus flight hotel booking aggregator platform | 🔥 BULL_OS_PPV | 49 | 🔄8 | ↑1.055 | ↑1d | PV | +8.7% | -53.34/-63.88 | +8.74% | 20% |
| [J&KBANK](https://in.tradingview.com/chart/?symbol=NSE:J&KBANK)<br><sub>📶W9 · 🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Retail corporate banking services Jammu Kashmir Ladakh regions | ⚡ BULL_ANY_PPV | 59 | 🔄66 | ↑1.007 | ↑1d | PV | +3.7% | -53.66/-53.88 | +3.74% | 20% |
| [BANKINDIA](https://in.tradingview.com/chart/?symbol=NSE:BANKINDIA)<br><sub>📶W9 · 🚀SS · ↓CMF19d</sub> | ✓ SAFE | Public sector bank retail corporate MSME lending | ⚡ BULL_ANY_PPV | 54 | 🔄46 | ↑1.023 | ↑1d | PV | +3.3% | -20.89/-27.2 | +3.34% | 20% |
| [INDNIPPON](https://in.tradingview.com/chart/?symbol=NSE:INDNIPPON)<br><sub>📶W9 · ↓CMF27d</sub> | ✓ SAFE | Two-wheeler ignition systems manufacturer for automotive sector | ⚡ BULL_ANY_PPV | 54 | 🔄82 | ↑1.017 | ↑1d | PV | +5.2% | -36.15/-37.21 | +5.21% | 20% |
| [JAYBARMARU](https://in.tradingview.com/chart/?symbol=NSE:JAYBARMARU)<br><sub>📶W9 · ↑CMF13d</sub> | ✓ SAFE | Auto parts supplier to Maruti Suzuki passenger vehicles | ⚡ BULL_ANY_PPV | 49 | 🔄75 | ↑1.039 | ↑1d | PV | +7.5% | 0.13/-1.15 | +7.49% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [NATCOPHARM](https://in.tradingview.com/chart/?symbol=NSE:NATCOPHARM)<br><sub>↑CMF12d · 🎯SLING</sub> | ✓ SAFE | Generic oncology drugs, complex formulations, global pharma markets | ⚡ BULL_ANY_PPV | 59 | 🔄31 | ↑1.004 | ↑1d | PV | +2.0% | -50.69/-53.34 | +2.01% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:IXIGO,NSE:J&KBANK,NSE:BANKINDIA,NSE:INDNIPPON,NSE:JAYBARMARU,NSE:SIGMAADV,NSE:NATCOPHARM
```

### 🟢 OVERSOLD — reversal from −53/−60 (10)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄56 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [KIRLOSBROS](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSBROS)<br><sub>📶W9 · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Pumps and fluid systems for water, power, irrigation | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.001 | ↓15d | — | -1.1% | -53.46/-54.76 | +1.84% | 20% |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 42 | 🔄52 | ↑0.992 | ↓13d | — | -5.3% | -64.43/-65.64 | +2.00% | 20% |
| [MOLDTKPAC](https://in.tradingview.com/chart/?symbol=NSE:MOLDTKPAC)<br><sub>↑CMF1d · ⚠️TRAP</sub> | ⚠ CAUTION | Injection-molded rigid plastic containers for lubricants paints food | 🟢 BULL_OVERSOLD | 14 | ↓1 | ↑0.757 | ↓11d | — | -53.6% | -62.76/-62.98 | -3.32% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 41 | 🔄36 | ↑1.001 | ↓19d | — | -4.4% | -53.92/-57.54 | +1.19% | 20% |
| [YATRA](https://in.tradingview.com/chart/?symbol=NSE:YATRA)<br><sub>🚀SS · ↓CMF14d · 🎯SLING</sub> | ✓ SAFE | Online travel bookings for leisure and corporate travelers | 🟡 BULL_OS_L2 | 35 | 🔄11 | ↑0.995 | ↓35d | — | -9.0% | -50.57/-53.89 | +0.99% | 20% |
| [LMW](https://in.tradingview.com/chart/?symbol=NSE:LMW)<br><sub>↓CMF27d · 🎯SLING</sub> | ⚠ CAUTION | Textile spinning machinery and CNC machine tools manufacturer | 🟡 BULL_OS_L2 | 35 | 🔄66 | ↑0.999 | ↓33d | — | -13.3% | -54.37/-56.25 | +1.39% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 22 | ↑66 | ↑1.004 | ↓8d | — | -0.3% | -53.58/-59.08 | +0.30% | 20% |
| [JLHL](https://in.tradingview.com/chart/?symbol=NSE:JLHL)<br><sub>W↑1d · ↓CMF4d · ⚠️TRAP</sub> | ⚠ CAUTION | Tertiary hospital chain Mumbai west India multi-specialty care | 🟡 BULL_OS_L2 | 18 | ↓0 | ↓0.984 | ↑2d | — | +3.0% | -56.03/-58.38 | -1.28% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GAIL,NSE:TMCV,NSE:KIRLOSBROS,NSE:JSWSTEEL,NSE:MOLDTKPAC,NSE:BPCL,NSE:YATRA,NSE:LMW,NSE:ADANIPOWER,NSE:JLHL
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (13)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [DISAQ](https://in.tradingview.com/chart/?symbol=NSE:DISAQ)<br><sub>📶W9 · ↓CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 59 | 🔄50 | ↑1.014 | ↑1d | — | +2.6% | -38.38/-39.62 | +2.64% | 20% |
| [CCAVENUE](https://in.tradingview.com/chart/?symbol=NSE:CCAVENUE)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄100 | ↑3.588 | ↑1d | — | +765.8% | 6.99/-15.88 | +765.77% | 20% |
| [POONAWALLA](https://in.tradingview.com/chart/?symbol=NSE:POONAWALLA)<br><sub>📶W9 · ↓CMF5d</sub> | ✓ SAFE | NBFC consumer loans MSME financing general insurance | 📈 BULL_ANY_MID | 18 | ↑46 | ↓1.002 | ↓2d | — | +1.4% | -21.3/-23.51 | -0.72% | 20% |
| [PREMEXPLN](https://in.tradingview.com/chart/?symbol=NSE:PREMEXPLN)<br><sub>📶W9 · W↑21d · ↑CMF8d</sub> | ✓ SAFE | Explosives propellants detonators defense space mining | 📈 BULL_ANY_MID | 10 | ↑78 | ↑1.006 | ↑30d | — | +4.5% | 60.61/60.15 | +0.21% | 20% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>📶W9 · W↑11d · ↑CMF15d</sub> | ✓ SAFE | Dredging, marine craft repair, maritime infrastructure engineering | 📈 BULL_ANY_MID | 5 | ↑97 | ↓1.027 | ↑15d | — | +15.5% | 58.09/57.87 | -0.11% | 20% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>📶W9 · W↑56d · ↑CMF18d</sub> | ✓ SAFE | Gold casting jewellery design manufacturing retail consumer ornaments | 📈 BULL_ANY_MID | 0 | ↑98 | ↓1.089 | ↑21d | — | +65.0% | 73.54/73.36 | -2.04% | 20% |
| [SUPRIYA](https://in.tradingview.com/chart/?symbol=NSE:SUPRIYA)<br><sub>📶W9 · ↓CMF0d · ⚠️TRAP</sub> | ✓ SAFE | API manufacturer, antihistamine analgesic anaesthetic pharma exports | 📈 BULL_ANY_MID | 0 | ↑74 | ↓0.988 | ↓34d | — | +8.7% | -18.41/-18.65 | -1.44% | 20% |
| [HITECH](https://in.tradingview.com/chart/?symbol=NSE:HITECH)<br><sub>🚀SS · ↓CMF3d</sub> | ✓ SAFE | ERW steel pipes tubes construction automotive infrastructure | 📈 BULL_ANY_MID | 45 | 🔄12 | ↑0.997 | ↓10d | — | +1.5% | -47.37/-49.09 | +0.57% | 20% |
| [TVSSRICHAK](https://in.tradingview.com/chart/?symbol=NSE:TVSSRICHAK)<br><sub>↓CMF18d</sub> | ⚠ CAUTION | Two-wheeler three-wheeler off-highway tyres manufacturer exporter | 📈 BULL_ANY_MID | 30 | 🔄69 | ↓0.992 | ↓48d | — | +11.1% | -40.94/-41.1 | -0.40% | 20% |
| [BUILDPRO](https://in.tradingview.com/chart/?symbol=NSE:BUILDPRO)<br><sub>↓CMF0d · ⚠️TRAP</sub> | ✓ SAFE | Building materials retail distribution southern western India | 📈 BULL_ANY_MID | 14 | ↓50 | ↑0.503 | ↓11d | — | -82.1% | -52.57/-52.95 | -6.73% | 20% |
| [BLSE](https://in.tradingview.com/chart/?symbol=NSE:BLSE)<br><sub>↓CMF16d · ⚠️TRAP</sub> | ✓ SAFE | Digital governance and banking services rural India | 📈 BULL_ANY_MID | 11 | ↓5 | ↑0.833 | ↓14d | — | -55.4% | -45.59/-45.81 | -2.25% | 20% |
| [JINDALSTEL](https://in.tradingview.com/chart/?symbol=NSE:JINDALSTEL)<br><sub>↓CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 8 | ↓47 | ↑0.982 | ↓17d | — | -8.9% | -51.85/-52.67 | +0.08% | 20% |
| [GPTHEALTH](https://in.tradingview.com/chart/?symbol=NSE:GPTHEALTH)<br><sub>↓CMF11d · ⚠️TRAP</sub> | ✓ SAFE | Multispecialty hospital chain secondary tertiary care Eastern India | 📈 BULL_ANY_MID | 0 | ↓44 | ↓0.974 | ↓33d | — | -7.8% | -48.96/-49.05 | -1.15% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:DISAQ,NSE:CCAVENUE,NSE:POONAWALLA,NSE:PREMEXPLN,NSE:KMEW,NSE:SHANTIGOLD,NSE:SUPRIYA,NSE:HITECH,NSE:TVSSRICHAK,NSE:BUILDPRO,NSE:BLSE,NSE:JINDALSTEL,NSE:GPTHEALTH
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
