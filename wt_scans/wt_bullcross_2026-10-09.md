> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-10-09
*Generated 2026-10-09 15:45 IST*

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

**Total bull crosses today: 64** · 14 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SUNCLAY,NSE:BHARATSE,NSE:AVTNPL,NSE:PACEDIGITK,NSE:BHEL,NSE:CYIENT,NSE:COLPAL,NSE:RSYSTEMS,NSE:NTPCGREEN,NSE:SIGMAADV,NSE:COALINDIA,NSE:IRCTC,NSE:AKCAPIT,NSE:CUB,NSE:CARTRADE,NSE:BAJAJCON,NSE:POLYCAB,NSE:INDPRUD,NSE:ADANIPOWER,NSE:UNITDSPR,NSE:DCBBANK,NSE:CGPOWER,NSE:DLF,NSE:PAYTM,NSE:ETERNAL,NSE:HDFCLIFE,NSE:VBL,NSE:GVT&D,NSE:WELENT,NSE:KEC,NSE:THERMAX,NSE:INTELLECT,NSE:TMPV,NSE:ASTERDM,NSE:INDIANB,NSE:CESC,NSE:NUCLEUS,NSE:DBCORP,NSE:WIPRO,NSE:GKENERGY,NSE:CHOLAFIN,NSE:SBICARD,NSE:GICRE,NSE:RAINBOW,NSE:ABB,NSE:KPITTECH,NSE:NEWGEN,NSE:ERIS,NSE:ROUTE,NSE:SAFARI,NSE:BAJAJELEC,NSE:IFGLEXPOR,NSE:JKLAKSHMI,NSE:JIOFIN,NSE:TATACAP,NSE:SBFC,NSE:JLHL,NSE:NH,NSE:SHREECEM,NSE:MANAPPURAM,NSE:INDIASHLTR,NSE:TVSSRICHAK,NSE:THANGAMAYL,NSE:EMMVEE
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (29)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SUNCLAY](https://in.tradingview.com/chart/?symbol=NSE:SUNCLAY)<br><sub>📶W9 · RVOL46x · ↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION |  | 🔥 BULL_OS_PPV | 49 | 🔄32 | ↑1.035 | ↑1d | PV | +11.2% | -66.16/-69.98 | +11.23% | 20% |
| [BHARATSE](https://in.tradingview.com/chart/?symbol=NSE:BHARATSE)<br><sub>📶W9 · RVOL21x · ↓CMF4d</sub> | ✓ SAFE | Automotive seating systems manufacturer for cars and commercial vehicles | ⚡ BULL_ANY_PPV | 99 | 🔄58 | ↑1.013 | ↑1d | SQ·PV | +4.7% | -40.8/-46.06 | +4.65% | 20% |
| [AVTNPL](https://in.tradingview.com/chart/?symbol=NSE:AVTNPL)<br><sub>📶W9 · RVOL20x · ↑CMF13d</sub> | ✓ SAFE | Plant extract manufacturer for food beverage nutrition | ⚡ BULL_ANY_PPV | 89 | 🔄88 | ↑1.054 | ↑1d | SQ·PV | +10.9% | -0.72/-2.31 | +10.92% | 20% |
| [PACEDIGITK](https://in.tradingview.com/chart/?symbol=NSE:PACEDIGITK)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Telecom fiber networks, power systems, energy infrastructure solutions | ⚡ BULL_ANY_PPV | 69 | ↑28 | ↑1.005 | ↑1d | SQ·PV | +2.0% | 2.17/1.71 | +2.03% | 20% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 64 | ↑89 | ↑1.016 | ↑1d | SQ·PV | +1.6% | -7.84/-16.13 | +1.64% | 20% |
| [CYIENT](https://in.tradingview.com/chart/?symbol=NSE:CYIENT)<br><sub>📶W9 · W↑50d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE | Engineering services, design, manufacturing digital transformation | ⚡ BULL_ANY_PPV | 59 | ↑76 | ↑1.044 | ↑1d | SQ·PV | +6.8% | 50.46/48.58 | +6.83% | 20% |
| [COLPAL](https://in.tradingview.com/chart/?symbol=NSE:COLPAL)<br><sub>📶W9 · 🚀SS·9x · ↑CMF0d</sub> | ✓ SAFE | Toothpaste, toothbrush, mouthwash maker for mass consumers | ⚡ BULL_ANY_PPV | 54 | 🔄36 | ↑1.017 | ↑1d | PV | +4.7% | -34.71/-39.15 | +4.73% | 20% |
| [RSYSTEMS](https://in.tradingview.com/chart/?symbol=NSE:RSYSTEMS)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | Digital product engineering AI solutions for enterprises | ⚡ BULL_ANY_PPV | 49 | 🔄40 | ↑1.065 | ↑1d | PV | +12.9% | 2.2/0.44 | +12.95% | 20% |
| [NTPCGREEN](https://in.tradingview.com/chart/?symbol=NSE:NTPCGREEN)<br><sub>📶W9 · W↑15d · ↑CMF11d</sub> | ✓ SAFE | Solar and wind power projects for grid distribution | ⚡ BULL_ANY_PPV | 23 | ↑49 | ↑1.017 | ↑2d | PV | +4.6% | -7.57/-10.56 | +1.98% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 69 | ↑54 | ↑1.007 | ↑1d | SQ | +1.4% | 24.57/23.53 | +1.38% | 20% |
| [IRCTC](https://in.tradingview.com/chart/?symbol=NSE:IRCTC)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Railway ticketing catering water PSU monopoly | 📈 BULL_ANY_MID | 69 | ↑19 | ↑1.007 | ↑1d | SQ | +2.0% | -42.9/-46.27 | +1.99% | 20% |
| [AKCAPIT](https://in.tradingview.com/chart/?symbol=NSE:AKCAPIT)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑50 | ↑1.014 | ↑1d | SQ | +1.8% | 1.35/-8.45 | +1.79% | 20% |
| [CUB](https://in.tradingview.com/chart/?symbol=NSE:CUB)<br><sub>📶W9 · W↑35d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Private bank serving SMEs, MSMEs, retail customers South India | 📈 BULL_ANY_MID | 64 | ↑53 | ↑1.026 | ↑1d | SQ | +5.2% | -5.85/-8.06 | +5.16% | 20% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>📶W9 · ↓CMF15d · ÷DIV</sub> | ✓ SAFE | Used car marketplace and financing platform India | 📈 BULL_ANY_MID | 64 | ↑77 | ↑1.016 | ↑1d | SQ | +4.0% | -26.22/-27.84 | +3.99% | 20% |
| [BAJAJCON](https://in.tradingview.com/chart/?symbol=NSE:BAJAJCON)<br><sub>📶W9 · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Hair oils, cosmetics, toiletries FMCG consumer products | 📈 BULL_ANY_MID | 64 | ↑86 | ↑1.025 | ↑1d | SQ | +3.6% | -22.63/-30.44 | +3.64% | 20% |
| [POLYCAB](https://in.tradingview.com/chart/?symbol=NSE:POLYCAB)<br><sub>📶W9 · ↑CMF0d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄55 | ↑1.013 | ↑1d | — | +2.0% | -44.27/-49.73 | +1.99% | 20% |
| [INDPRUD](https://in.tradingview.com/chart/?symbol=NSE:INDPRUD)<br><sub>📶W9 · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 55 | ↑50 | ↓1.001 | ↑5d | SQ | +0.8% | 3.27/0.56 | +0.00% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 52 | 🔄71 | ↑1.000 | ↓3d | — | +2.5% | -41.74/-41.75 | +2.49% | 20% |
| [UNITDSPR](https://in.tradingview.com/chart/?symbol=NSE:UNITDSPR)<br><sub>📶W9 · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Whisky rum vodka gin spirits manufacturer India | 📈 BULL_ANY_MID | 47 | 🔄58 | ↑1.005 | ↓13d | — | -2.3% | -48.29/-48.49 | +3.63% | 20% |
| [DCBBANK](https://in.tradingview.com/chart/?symbol=NSE:DCBBANK)<br><sub>📶W9 · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Secured lending to retail, MSME, agricultural sectors | 📈 BULL_ANY_MID | 47 | 🔄76 | ↑1.003 | ↓13d | — | -6.8% | -41.75/-44.38 | +3.68% | 20% |
| [CGPOWER](https://in.tradingview.com/chart/?symbol=NSE:CGPOWER)<br><sub>📶W9 · 🚀SS · ↓CMF5d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 29 | ↑70 | ↑1.005 | ↑1d | — | +0.4% | -12.74/-14.29 | +0.38% | 20% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 29 | ↑58 | ↑1.011 | ↑1d | — | +2.1% | 7.14/4.78 | +2.10% | 20% |
| [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Digital payments, fintech, consumer and merchant ecosystem | 📈 BULL_ANY_MID | 24 | ↑88 | ↑1.016 | ↑1d | — | +2.3% | 2.77/0.98 | +2.30% | 20% |
| [ETERNAL](https://in.tradingview.com/chart/?symbol=NSE:ETERNAL)<br><sub>📶W9 · ↑CMF2d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 18 | ↑70 | ↓1.004 | ↑2d | — | +2.2% | -0.89/-2.27 | -0.36% | 20% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>📶W9 · W↑14d · ↑CMF6d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 18 | ↑22 | ↑1.000 | ↓12d | — | +0.8% | -18.3/-18.75 | +0.02% | 20% |
| [VBL](https://in.tradingview.com/chart/?symbol=NSE:VBL)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF6d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 13 | ↑43 | ↑1.022 | ↑12d | — | +7.0% | 24.78/23.0 | +3.29% | 20% |
| [GVT&D](https://in.tradingview.com/chart/?symbol=NSE:GVT&D)<br><sub>📶W9 · ↓CMF3d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 12 | ↑70 | ↓0.994 | ↓8d | — | -2.5% | -29.77/-29.83 | -0.32% | -% |
| [WELENT](https://in.tradingview.com/chart/?symbol=NSE:WELENT)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE | Infrastructure development roads water pipelines oil gas projects | 📈 BULL_ANY_MID | 7 | ↑87 | ↑0.998 | ↓18d | — | -0.2% | -21.6/-21.67 | +0.48% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SUNCLAY,NSE:BHARATSE,NSE:AVTNPL,NSE:PACEDIGITK,NSE:BHEL,NSE:CYIENT,NSE:COLPAL,NSE:RSYSTEMS,NSE:NTPCGREEN,NSE:SIGMAADV,NSE:COALINDIA,NSE:IRCTC,NSE:AKCAPIT,NSE:CUB,NSE:CARTRADE,NSE:BAJAJCON,NSE:POLYCAB,NSE:INDPRUD,NSE:ADANIPOWER,NSE:UNITDSPR,NSE:DCBBANK,NSE:CGPOWER,NSE:DLF,NSE:PAYTM,NSE:ETERNAL,NSE:HDFCLIFE,NSE:VBL,NSE:GVT&D,NSE:WELENT
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (46)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SUNCLAY](https://in.tradingview.com/chart/?symbol=NSE:SUNCLAY)<br><sub>📶W9 · RVOL46x · ↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION |  | 🔥 BULL_OS_PPV | 49 | 🔄32 | ↑1.035 | ↑1d | PV | +11.2% | -66.16/-69.98 | +11.23% | 20% |
| [BHARATSE](https://in.tradingview.com/chart/?symbol=NSE:BHARATSE)<br><sub>📶W9 · RVOL21x · ↓CMF4d</sub> | ✓ SAFE | Automotive seating systems manufacturer for cars and commercial vehicles | ⚡ BULL_ANY_PPV | 99 | 🔄58 | ↑1.013 | ↑1d | SQ·PV | +4.7% | -40.8/-46.06 | +4.65% | 20% |
| [AVTNPL](https://in.tradingview.com/chart/?symbol=NSE:AVTNPL)<br><sub>📶W9 · RVOL20x · ↑CMF13d</sub> | ✓ SAFE | Plant extract manufacturer for food beverage nutrition | ⚡ BULL_ANY_PPV | 89 | 🔄88 | ↑1.054 | ↑1d | SQ·PV | +10.9% | -0.72/-2.31 | +10.92% | 20% |
| [PACEDIGITK](https://in.tradingview.com/chart/?symbol=NSE:PACEDIGITK)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Telecom fiber networks, power systems, energy infrastructure solutions | ⚡ BULL_ANY_PPV | 69 | ↑28 | ↑1.005 | ↑1d | SQ·PV | +2.0% | 2.17/1.71 | +2.03% | 20% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 64 | ↑89 | ↑1.016 | ↑1d | SQ·PV | +1.6% | -7.84/-16.13 | +1.64% | 20% |
| [CYIENT](https://in.tradingview.com/chart/?symbol=NSE:CYIENT)<br><sub>📶W9 · W↑50d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE | Engineering services, design, manufacturing digital transformation | ⚡ BULL_ANY_PPV | 59 | ↑76 | ↑1.044 | ↑1d | SQ·PV | +6.8% | 50.46/48.58 | +6.83% | 20% |
| [COLPAL](https://in.tradingview.com/chart/?symbol=NSE:COLPAL)<br><sub>📶W9 · 🚀SS·9x · ↑CMF0d</sub> | ✓ SAFE | Toothpaste, toothbrush, mouthwash maker for mass consumers | ⚡ BULL_ANY_PPV | 54 | 🔄36 | ↑1.017 | ↑1d | PV | +4.7% | -34.71/-39.15 | +4.73% | 20% |
| [RSYSTEMS](https://in.tradingview.com/chart/?symbol=NSE:RSYSTEMS)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | Digital product engineering AI solutions for enterprises | ⚡ BULL_ANY_PPV | 49 | 🔄40 | ↑1.065 | ↑1d | PV | +12.9% | 2.2/0.44 | +12.95% | 20% |
| [NTPCGREEN](https://in.tradingview.com/chart/?symbol=NSE:NTPCGREEN)<br><sub>📶W9 · W↑15d · ↑CMF11d</sub> | ✓ SAFE | Solar and wind power projects for grid distribution | ⚡ BULL_ANY_PPV | 23 | ↑49 | ↑1.017 | ↑2d | PV | +4.6% | -7.57/-10.56 | +1.98% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 69 | ↑54 | ↑1.007 | ↑1d | SQ | +1.4% | 24.57/23.53 | +1.38% | 20% |
| [IRCTC](https://in.tradingview.com/chart/?symbol=NSE:IRCTC)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Railway ticketing catering water PSU monopoly | 📈 BULL_ANY_MID | 69 | ↑19 | ↑1.007 | ↑1d | SQ | +2.0% | -42.9/-46.27 | +1.99% | 20% |
| [AKCAPIT](https://in.tradingview.com/chart/?symbol=NSE:AKCAPIT)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑50 | ↑1.014 | ↑1d | SQ | +1.8% | 1.35/-8.45 | +1.79% | 20% |
| [CUB](https://in.tradingview.com/chart/?symbol=NSE:CUB)<br><sub>📶W9 · W↑35d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Private bank serving SMEs, MSMEs, retail customers South India | 📈 BULL_ANY_MID | 64 | ↑53 | ↑1.026 | ↑1d | SQ | +5.2% | -5.85/-8.06 | +5.16% | 20% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>📶W9 · ↓CMF15d · ÷DIV</sub> | ✓ SAFE | Used car marketplace and financing platform India | 📈 BULL_ANY_MID | 64 | ↑77 | ↑1.016 | ↑1d | SQ | +4.0% | -26.22/-27.84 | +3.99% | 20% |
| [BAJAJCON](https://in.tradingview.com/chart/?symbol=NSE:BAJAJCON)<br><sub>📶W9 · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Hair oils, cosmetics, toiletries FMCG consumer products | 📈 BULL_ANY_MID | 64 | ↑86 | ↑1.025 | ↑1d | SQ | +3.6% | -22.63/-30.44 | +3.64% | 20% |
| [POLYCAB](https://in.tradingview.com/chart/?symbol=NSE:POLYCAB)<br><sub>📶W9 · ↑CMF0d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄55 | ↑1.013 | ↑1d | — | +2.0% | -44.27/-49.73 | +1.99% | 20% |
| [INDPRUD](https://in.tradingview.com/chart/?symbol=NSE:INDPRUD)<br><sub>📶W9 · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 55 | ↑50 | ↓1.001 | ↑5d | SQ | +0.8% | 3.27/0.56 | +0.00% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 52 | 🔄71 | ↑1.000 | ↓3d | — | +2.5% | -41.74/-41.75 | +2.49% | 20% |
| [UNITDSPR](https://in.tradingview.com/chart/?symbol=NSE:UNITDSPR)<br><sub>📶W9 · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Whisky rum vodka gin spirits manufacturer India | 📈 BULL_ANY_MID | 47 | 🔄58 | ↑1.005 | ↓13d | — | -2.3% | -48.29/-48.49 | +3.63% | 20% |
| [DCBBANK](https://in.tradingview.com/chart/?symbol=NSE:DCBBANK)<br><sub>📶W9 · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Secured lending to retail, MSME, agricultural sectors | 📈 BULL_ANY_MID | 47 | 🔄76 | ↑1.003 | ↓13d | — | -6.8% | -41.75/-44.38 | +3.68% | 20% |
| [CGPOWER](https://in.tradingview.com/chart/?symbol=NSE:CGPOWER)<br><sub>📶W9 · 🚀SS · ↓CMF5d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 29 | ↑70 | ↑1.005 | ↑1d | — | +0.4% | -12.74/-14.29 | +0.38% | 20% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 29 | ↑58 | ↑1.011 | ↑1d | — | +2.1% | 7.14/4.78 | +2.10% | 20% |
| [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Digital payments, fintech, consumer and merchant ecosystem | 📈 BULL_ANY_MID | 24 | ↑88 | ↑1.016 | ↑1d | — | +2.3% | 2.77/0.98 | +2.30% | 20% |
| [ETERNAL](https://in.tradingview.com/chart/?symbol=NSE:ETERNAL)<br><sub>📶W9 · ↑CMF2d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 18 | ↑70 | ↓1.004 | ↑2d | — | +2.2% | -0.89/-2.27 | -0.36% | 20% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>📶W9 · W↑14d · ↑CMF6d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 18 | ↑22 | ↑1.000 | ↓12d | — | +0.8% | -18.3/-18.75 | +0.02% | 20% |
| [VBL](https://in.tradingview.com/chart/?symbol=NSE:VBL)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF6d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 13 | ↑43 | ↑1.022 | ↑12d | — | +7.0% | 24.78/23.0 | +3.29% | 20% |
| [GVT&D](https://in.tradingview.com/chart/?symbol=NSE:GVT&D)<br><sub>📶W9 · ↓CMF3d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 12 | ↑70 | ↓0.994 | ↓8d | — | -2.5% | -29.77/-29.83 | -0.32% | -% |
| [WELENT](https://in.tradingview.com/chart/?symbol=NSE:WELENT)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE | Infrastructure development roads water pipelines oil gas projects | 📈 BULL_ANY_MID | 7 | ↑87 | ↑0.998 | ↓18d | — | -0.2% | -21.6/-21.67 | +0.48% | 20% |
| [KEC](https://in.tradingview.com/chart/?symbol=NSE:KEC)<br><sub>🚀SS·17x · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Power transmission infrastructure EPC contractor global | 🔥 BULL_OS_PPV | 35 | 🔄2 | ↑0.994 | ↓46d | PV | -22.6% | -70.93/-71.65 | +5.79% | 20% |
| [THERMAX](https://in.tradingview.com/chart/?symbol=NSE:THERMAX)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Industrial boilers, cooling systems, power equipment, pollution control | 🔥 BULL_OS_PPV | 35 | 🔄30 | ↑0.990 | ↓59d | PV | -30.9% | -64.62/-66.82 | +3.77% | 20% |
| [TMPV](https://in.tradingview.com/chart/?symbol=NSE:TMPV)<br><sub>🚀SS · ↓CMF26d · 🔥PHX</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 43 | 🔄15 | ↑0.996 | ↓12d | — | -4.3% | -64.81/-66.76 | +3.13% | 20% |
| [ASTERDM](https://in.tradingview.com/chart/?symbol=NSE:ASTERDM)<br><sub>🚀SS · ↓CMF7d · 🎯SLING</sub> | ✓ SAFE | Multi-specialty hospitals and clinics, India healthcare | 🟢 BULL_OVERSOLD | 43 | 🔄51 | ↑0.995 | ↓12d | — | -7.9% | -62.41/-64.49 | +3.35% | 20% |
| [INDIANB](https://in.tradingview.com/chart/?symbol=NSE:INDIANB)<br><sub>🚀SS · ↓CMF20d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 35 | 🔄55 | ↑0.991 | ↓21d | — | -8.0% | -61.07/-61.42 | +1.99% | 20% |
| [CESC](https://in.tradingview.com/chart/?symbol=NSE:CESC)<br><sub>🚀SS · ↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Electricity generation and distribution utility West Bengal | 🟢 BULL_OVERSOLD | 35 | 🔄19 | ↑0.997 | ↓42d | — | -18.0% | -62.49/-63.28 | +3.50% | 20% |
| [NUCLEUS](https://in.tradingview.com/chart/?symbol=NSE:NUCLEUS)<br><sub>↓CMF15d · 🎯SLING</sub> | ⚠ CAUTION | Banking software for retail lending and payments | 🟢 BULL_OVERSOLD | 35 | 🔄11 | ↑0.993 | ↓40d | — | -9.1% | -64.95/-65.42 | +3.22% | 20% |
| [DBCORP](https://in.tradingview.com/chart/?symbol=NSE:DBCORP)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Print media, newspapers, advertising, pan-India distribution network | 🟢 BULL_OVERSOLD | 35 | 🔄12 | ↑0.996 | ↓60d+ | — | -19.4% | -64.98/-66.42 | +3.32% | 20% |
| [WIPRO](https://in.tradingview.com/chart/?symbol=NSE:WIPRO)<br><sub>🚀SS · ↓CMF4d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 10 | ↑16 | ↑1.000 | ↓25d | — | -8.0% | -59.15/-63.71 | +1.86% | 20% |
| [ABB](https://in.tradingview.com/chart/?symbol=NSE:ABB)<br><sub>↓CMF4d · ⚠️TRAP</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 5 | ↑69 | ↑0.989 | ↓24d | — | -8.3% | -64.83/-66.76 | -0.21% | 20% |
| [SBFC](https://in.tradingview.com/chart/?symbol=NSE:SBFC)<br><sub>↓CMF12d · 🎯SLING</sub> | ✓ SAFE | MSME secured lending, gold loans, underserved borrowers | 🟡 BULL_OS_L2 | 35 | 🔄30 | ↑1.000 | ↓23d | — | -13.3% | -57.63/-59.49 | +3.84% | 20% |
| [JLHL](https://in.tradingview.com/chart/?symbol=NSE:JLHL)<br><sub>↑CMF8d · 🎯SLING</sub> | ⚠ CAUTION | Tertiary hospital chain Mumbai west India multi-specialty care | 🟡 BULL_OS_L2 | 35 | 🔄0 | ↑0.996 | ↑26d | — | -11.9% | -55.75/-56.42 | +3.48% | 20% |
| [SHREECEM](https://in.tradingview.com/chart/?symbol=NSE:SHREECEM)<br><sub>🚀SS · ↓CMF13d</sub> | ✓ SAFE | Cement manufacturer, lowest cost producer, construction materials | 📈 BULL_ANY_MID | 69 | ↑22 | ↑1.003 | ↑1d | SQ | +2.2% | -50.97/-51.72 | +2.22% | 20% |
| [MANAPPURAM](https://in.tradingview.com/chart/?symbol=NSE:MANAPPURAM)<br><sub>🚀SS · ↑CMF0d</sub> | ✓ SAFE | Gold loans, NBFC, retail credit, unbanked customers | 📈 BULL_ANY_MID | 59 | 🔄62 | ↑1.008 | ↑1d | — | +3.5% | -46.52/-47.95 | +3.50% | 20% |
| [INDIASHLTR](https://in.tradingview.com/chart/?symbol=NSE:INDIASHLTR)<br><sub>↑CMF15d · ⚠️TRAP</sub> | ⚠ CAUTION | Housing loans for low income tier 2 3 cities | 📈 BULL_ANY_MID | 52 | ↑15 | ↑0.999 | ↓13d | SQ | -2.8% | -35.24/-39.03 | -0.01% | 20% |
| [TVSSRICHAK](https://in.tradingview.com/chart/?symbol=NSE:TVSSRICHAK)<br><sub>🚀SS · ↓CMF12d</sub> | ⚠ CAUTION | Two-wheeler three-wheeler off-highway tyres manufacturer exporter | 📈 BULL_ANY_MID | 35 | 🔄66 | ↑0.994 | ↓42d | — | +13.1% | -44.97/-45.86 | +2.80% | 20% |
| [THANGAMAYL](https://in.tradingview.com/chart/?symbol=NSE:THANGAMAYL)<br><sub>↑CMF14d</sub> | ✓ SAFE | Gold silver diamond jewellery retail Tamil Nadu consumer | 📈 BULL_ANY_MID | 16 | ↑82 | ↑1.000 | ↓9d | — | -2.4% | -46.74/-48.14 | +1.64% | 10% 🟨 |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SUNCLAY,NSE:BHARATSE,NSE:AVTNPL,NSE:PACEDIGITK,NSE:BHEL,NSE:CYIENT,NSE:COLPAL,NSE:RSYSTEMS,NSE:NTPCGREEN,NSE:SIGMAADV,NSE:COALINDIA,NSE:IRCTC,NSE:AKCAPIT,NSE:CUB,NSE:CARTRADE,NSE:BAJAJCON,NSE:POLYCAB,NSE:INDPRUD,NSE:ADANIPOWER,NSE:UNITDSPR,NSE:DCBBANK,NSE:CGPOWER,NSE:DLF,NSE:PAYTM,NSE:ETERNAL,NSE:HDFCLIFE,NSE:VBL,NSE:GVT&D,NSE:WELENT,NSE:KEC,NSE:THERMAX,NSE:TMPV,NSE:ASTERDM,NSE:INDIANB,NSE:CESC,NSE:NUCLEUS,NSE:DBCORP,NSE:WIPRO,NSE:ABB,NSE:SBFC,NSE:JLHL,NSE:SHREECEM,NSE:MANAPPURAM,NSE:INDIASHLTR,NSE:TVSSRICHAK,NSE:THANGAMAYL
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (14)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [BHARATSE](https://in.tradingview.com/chart/?symbol=NSE:BHARATSE)<br><sub>📶W9 · RVOL21x · ↓CMF4d</sub> | ✓ SAFE | Automotive seating systems manufacturer for cars and commercial vehicles | ⚡ BULL_ANY_PPV | 99 | 🔄58 | ↑1.013 | ↑1d | SQ·PV | +4.7% | -40.8/-46.06 | +4.65% | 20% |
| [AVTNPL](https://in.tradingview.com/chart/?symbol=NSE:AVTNPL)<br><sub>📶W9 · RVOL20x · ↑CMF13d</sub> | ✓ SAFE | Plant extract manufacturer for food beverage nutrition | ⚡ BULL_ANY_PPV | 89 | 🔄88 | ↑1.054 | ↑1d | SQ·PV | +10.9% | -0.72/-2.31 | +10.92% | 20% |
| [PACEDIGITK](https://in.tradingview.com/chart/?symbol=NSE:PACEDIGITK)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Telecom fiber networks, power systems, energy infrastructure solutions | ⚡ BULL_ANY_PPV | 69 | ↑28 | ↑1.005 | ↑1d | SQ·PV | +2.0% | 2.17/1.71 | +2.03% | 20% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 64 | ↑89 | ↑1.016 | ↑1d | SQ·PV | +1.6% | -7.84/-16.13 | +1.64% | 20% |
| [CYIENT](https://in.tradingview.com/chart/?symbol=NSE:CYIENT)<br><sub>📶W9 · W↑50d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE | Engineering services, design, manufacturing digital transformation | ⚡ BULL_ANY_PPV | 59 | ↑76 | ↑1.044 | ↑1d | SQ·PV | +6.8% | 50.46/48.58 | +6.83% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 69 | ↑54 | ↑1.007 | ↑1d | SQ | +1.4% | 24.57/23.53 | +1.38% | 20% |
| [IRCTC](https://in.tradingview.com/chart/?symbol=NSE:IRCTC)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Railway ticketing catering water PSU monopoly | 📈 BULL_ANY_MID | 69 | ↑19 | ↑1.007 | ↑1d | SQ | +2.0% | -42.9/-46.27 | +1.99% | 20% |
| [AKCAPIT](https://in.tradingview.com/chart/?symbol=NSE:AKCAPIT)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑50 | ↑1.014 | ↑1d | SQ | +1.8% | 1.35/-8.45 | +1.79% | 20% |
| [CUB](https://in.tradingview.com/chart/?symbol=NSE:CUB)<br><sub>📶W9 · W↑35d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Private bank serving SMEs, MSMEs, retail customers South India | 📈 BULL_ANY_MID | 64 | ↑53 | ↑1.026 | ↑1d | SQ | +5.2% | -5.85/-8.06 | +5.16% | 20% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>📶W9 · ↓CMF15d · ÷DIV</sub> | ✓ SAFE | Used car marketplace and financing platform India | 📈 BULL_ANY_MID | 64 | ↑77 | ↑1.016 | ↑1d | SQ | +4.0% | -26.22/-27.84 | +3.99% | 20% |
| [BAJAJCON](https://in.tradingview.com/chart/?symbol=NSE:BAJAJCON)<br><sub>📶W9 · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Hair oils, cosmetics, toiletries FMCG consumer products | 📈 BULL_ANY_MID | 64 | ↑86 | ↑1.025 | ↑1d | SQ | +3.6% | -22.63/-30.44 | +3.64% | 20% |
| [INDPRUD](https://in.tradingview.com/chart/?symbol=NSE:INDPRUD)<br><sub>📶W9 · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 55 | ↑50 | ↓1.001 | ↑5d | SQ | +0.8% | 3.27/0.56 | +0.00% | 20% |
| [SHREECEM](https://in.tradingview.com/chart/?symbol=NSE:SHREECEM)<br><sub>🚀SS · ↓CMF13d</sub> | ✓ SAFE | Cement manufacturer, lowest cost producer, construction materials | 📈 BULL_ANY_MID | 69 | ↑22 | ↑1.003 | ↑1d | SQ | +2.2% | -50.97/-51.72 | +2.22% | 20% |
| [INDIASHLTR](https://in.tradingview.com/chart/?symbol=NSE:INDIASHLTR)<br><sub>↑CMF15d · ⚠️TRAP</sub> | ⚠ CAUTION | Housing loans for low income tier 2 3 cities | 📈 BULL_ANY_MID | 52 | ↑15 | ↑0.999 | ↓13d | SQ | -2.8% | -35.24/-39.03 | -0.01% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:BHARATSE,NSE:AVTNPL,NSE:PACEDIGITK,NSE:BHEL,NSE:CYIENT,NSE:COALINDIA,NSE:IRCTC,NSE:AKCAPIT,NSE:CUB,NSE:CARTRADE,NSE:BAJAJCON,NSE:INDPRUD,NSE:SHREECEM,NSE:INDIASHLTR
```

---

### 🔥 MAJOR — PPV confirmed (8)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SUNCLAY](https://in.tradingview.com/chart/?symbol=NSE:SUNCLAY)<br><sub>📶W9 · RVOL46x · ↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION |  | 🔥 BULL_OS_PPV | 49 | 🔄32 | ↑1.035 | ↑1d | PV | +11.2% | -66.16/-69.98 | +11.23% | 20% |
| [COLPAL](https://in.tradingview.com/chart/?symbol=NSE:COLPAL)<br><sub>📶W9 · 🚀SS·9x · ↑CMF0d</sub> | ✓ SAFE | Toothpaste, toothbrush, mouthwash maker for mass consumers | ⚡ BULL_ANY_PPV | 54 | 🔄36 | ↑1.017 | ↑1d | PV | +4.7% | -34.71/-39.15 | +4.73% | 20% |
| [RSYSTEMS](https://in.tradingview.com/chart/?symbol=NSE:RSYSTEMS)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | Digital product engineering AI solutions for enterprises | ⚡ BULL_ANY_PPV | 49 | 🔄40 | ↑1.065 | ↑1d | PV | +12.9% | 2.2/0.44 | +12.95% | 20% |
| [NTPCGREEN](https://in.tradingview.com/chart/?symbol=NSE:NTPCGREEN)<br><sub>📶W9 · W↑15d · ↑CMF11d</sub> | ✓ SAFE | Solar and wind power projects for grid distribution | ⚡ BULL_ANY_PPV | 23 | ↑49 | ↑1.017 | ↑2d | PV | +4.6% | -7.57/-10.56 | +1.98% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [KEC](https://in.tradingview.com/chart/?symbol=NSE:KEC)<br><sub>🚀SS·17x · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Power transmission infrastructure EPC contractor global | 🔥 BULL_OS_PPV | 35 | 🔄2 | ↑0.994 | ↓46d | PV | -22.6% | -70.93/-71.65 | +5.79% | 20% |
| [THERMAX](https://in.tradingview.com/chart/?symbol=NSE:THERMAX)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Industrial boilers, cooling systems, power equipment, pollution control | 🔥 BULL_OS_PPV | 35 | 🔄30 | ↑0.990 | ↓59d | PV | -30.9% | -64.62/-66.82 | +3.77% | 20% |
| [INTELLECT](https://in.tradingview.com/chart/?symbol=NSE:INTELLECT)<br><sub>🚀SS · ↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Cloud fintech software for banks insurance wealth managers | 🔥 BULL_OS_PPV | 12 | ↓7 | ↑0.970 | ↓13d | PV | -9.8% | -75.24/-75.29 | +2.95% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SUNCLAY,NSE:COLPAL,NSE:RSYSTEMS,NSE:NTPCGREEN,NSE:SIGMAADV,NSE:KEC,NSE:THERMAX,NSE:INTELLECT
```

### 🟢 OVERSOLD — reversal from −53/−60 (26)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [TMPV](https://in.tradingview.com/chart/?symbol=NSE:TMPV)<br><sub>🚀SS · ↓CMF26d · 🔥PHX</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 43 | 🔄15 | ↑0.996 | ↓12d | — | -4.3% | -64.81/-66.76 | +3.13% | 20% |
| [ASTERDM](https://in.tradingview.com/chart/?symbol=NSE:ASTERDM)<br><sub>🚀SS · ↓CMF7d · 🎯SLING</sub> | ✓ SAFE | Multi-specialty hospitals and clinics, India healthcare | 🟢 BULL_OVERSOLD | 43 | 🔄51 | ↑0.995 | ↓12d | — | -7.9% | -62.41/-64.49 | +3.35% | 20% |
| [INDIANB](https://in.tradingview.com/chart/?symbol=NSE:INDIANB)<br><sub>🚀SS · ↓CMF20d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 35 | 🔄55 | ↑0.991 | ↓21d | — | -8.0% | -61.07/-61.42 | +1.99% | 20% |
| [CESC](https://in.tradingview.com/chart/?symbol=NSE:CESC)<br><sub>🚀SS · ↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Electricity generation and distribution utility West Bengal | 🟢 BULL_OVERSOLD | 35 | 🔄19 | ↑0.997 | ↓42d | — | -18.0% | -62.49/-63.28 | +3.50% | 20% |
| [NUCLEUS](https://in.tradingview.com/chart/?symbol=NSE:NUCLEUS)<br><sub>↓CMF15d · 🎯SLING</sub> | ⚠ CAUTION | Banking software for retail lending and payments | 🟢 BULL_OVERSOLD | 35 | 🔄11 | ↑0.993 | ↓40d | — | -9.1% | -64.95/-65.42 | +3.22% | 20% |
| [DBCORP](https://in.tradingview.com/chart/?symbol=NSE:DBCORP)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Print media, newspapers, advertising, pan-India distribution network | 🟢 BULL_OVERSOLD | 35 | 🔄12 | ↑0.996 | ↓60d+ | — | -19.4% | -64.98/-66.42 | +3.32% | 20% |
| [WIPRO](https://in.tradingview.com/chart/?symbol=NSE:WIPRO)<br><sub>🚀SS · ↓CMF4d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 10 | ↑16 | ↑1.000 | ↓25d | — | -8.0% | -59.15/-63.71 | +1.86% | 20% |
| [GKENERGY](https://in.tradingview.com/chart/?symbol=NSE:GKENERGY)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Solar pump EPC services for Indian agriculture | 🟢 BULL_OVERSOLD | 10 | ↓16 | ↑0.975 | ↓15d | — | -5.6% | -59.87/-60.04 | -0.08% | 10% 🟩 |
| [CHOLAFIN](https://in.tradingview.com/chart/?symbol=NSE:CHOLAFIN)<br><sub>🚀SS · ↑CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 9 | ↓45 | ↑0.966 | ↓16d | — | -12.3% | -76.91/-77.55 | +1.49% | 20% |
| [SBICARD](https://in.tradingview.com/chart/?symbol=NSE:SBICARD)<br><sub>🚀SS · ↓CMF6d · 🎯SLING</sub> | ✓ SAFE | Credit card issuer, consumer lending, retail banking sector | 🟢 BULL_OVERSOLD | 9 | ↓12 | ↑0.982 | ↓16d | — | -11.8% | -61.07/-61.94 | +2.62% | 20% |
| [GICRE](https://in.tradingview.com/chart/?symbol=NSE:GICRE)<br><sub>🚀SS · ↓CMF5d · 🎯SLING</sub> | ⚠ CAUTION | Reinsurance provider, domestic market leader, risk transfer | 🟢 BULL_OVERSOLD | 9 | ↓24 | ↑0.976 | ↓16d | — | -8.0% | -75.23/-76.04 | +1.13% | 20% |
| [RAINBOW](https://in.tradingview.com/chart/?symbol=NSE:RAINBOW)<br><sub>🚀SS · ↓CMF20d · 🎯SLING</sub> | ✓ SAFE | Pediatric obstetric gynecology hospital chain India | 🟢 BULL_OVERSOLD | 6 | ↓41 | ↑0.971 | ↓19d | — | -13.5% | -67.36/-68.48 | +1.58% | 20% |
| [ABB](https://in.tradingview.com/chart/?symbol=NSE:ABB)<br><sub>↓CMF4d · ⚠️TRAP</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 5 | ↑69 | ↑0.989 | ↓24d | — | -8.3% | -64.83/-66.76 | -0.21% | 20% |
| [KPITTECH](https://in.tradingview.com/chart/?symbol=NSE:KPITTECH)<br><sub>🚀SS · ↓CMF29d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Automotive software, embedded systems, SDV development | 🟢 BULL_OVERSOLD | 5 | ↓2 | ↑0.971 | ↓31d | — | -18.5% | -66.81/-67.03 | +1.70% | 20% |
| [NEWGEN](https://in.tradingview.com/chart/?symbol=NSE:NEWGEN)<br><sub>🚀SS · ↓CMF25d · 🎯SLING</sub> | ✓ SAFE | Digital transformation platform automation software for enterprises | 🟢 BULL_OVERSOLD | 5 | ↓7 | ↑0.978 | ↓31d | — | -14.1% | -67.98/-68.48 | +1.53% | 20% |
| [ERIS](https://in.tradingview.com/chart/?symbol=NSE:ERIS)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Oral branded drugs for chronic diseases, domestic India | 🟢 BULL_OVERSOLD | 5 | ↓15 | ↑0.983 | ↓26d | — | -10.2% | -64.02/-64.9 | +1.35% | 20% |
| [ROUTE](https://in.tradingview.com/chart/?symbol=NSE:ROUTE)<br><sub>🚀SS · ↓CMF30d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE | Cloud messaging platform for enterprises and telecom operators | 🟢 BULL_OVERSOLD | 5 | ↓4 | ↑0.961 | ↓25d | — | -16.9% | -72.64/-72.71 | +0.46% | 20% |
| [SAFARI](https://in.tradingview.com/chart/?symbol=NSE:SAFARI)<br><sub>🚀SS · ↓CMF0d · 🎯SLING</sub> | ⚠ CAUTION | Luggage and travel bags manufacturer for domestic and international consumers | 🟢 BULL_OVERSOLD | 5 | ↓8 | ↑0.972 | ↓21d | — | -12.1% | -77.34/-78.26 | +2.35% | 20% |
| [BAJAJELEC](https://in.tradingview.com/chart/?symbol=NSE:BAJAJELEC)<br><sub>🚀SS · ↓CMF7d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Electrical appliances fans lighting wiring for homes | 🟢 BULL_OVERSOLD | 5 | ↓11 | ↑0.985 | ↓25d | — | -10.0% | -66.0/-66.6 | +2.74% | 20% |
| [IFGLEXPOR](https://in.tradingview.com/chart/?symbol=NSE:IFGLEXPOR)<br><sub>↓CMF13d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 5 | ↓25 | ↑0.972 | ↓23d | — | -8.9% | -65.13/-65.18 | +0.44% | 20% |
| [JKLAKSHMI](https://in.tradingview.com/chart/?symbol=NSE:JKLAKSHMI)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Integrated cement manufacturer serving construction across regions | 🟢 BULL_OVERSOLD | 4 | ↓6 | ↓0.975 | ↓16d | — | -8.4% | -64.17/-64.26 | -0.57% | 20% |
| [JIOFIN](https://in.tradingview.com/chart/?symbol=NSE:JIOFIN)<br><sub>↓CMF28d · ⚠️TRAP</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 0 | ↓22 | ↓0.986 | ↓49d | — | -8.7% | -65.94/-69.33 | -0.71% | 20% |
| [TATACAP](https://in.tradingview.com/chart/?symbol=NSE:TATACAP)<br><sub>↓CMF3d · ⚠️TRAP</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 0 | ↓50 | ↓0.975 | ↓23d | — | -12.2% | -63.82/-64.63 | -0.59% | 20% |
| [SBFC](https://in.tradingview.com/chart/?symbol=NSE:SBFC)<br><sub>↓CMF12d · 🎯SLING</sub> | ✓ SAFE | MSME secured lending, gold loans, underserved borrowers | 🟡 BULL_OS_L2 | 35 | 🔄30 | ↑1.000 | ↓23d | — | -13.3% | -57.63/-59.49 | +3.84% | 20% |
| [JLHL](https://in.tradingview.com/chart/?symbol=NSE:JLHL)<br><sub>↑CMF8d · 🎯SLING</sub> | ⚠ CAUTION | Tertiary hospital chain Mumbai west India multi-specialty care | 🟡 BULL_OS_L2 | 35 | 🔄0 | ↑0.996 | ↑26d | — | -11.9% | -55.75/-56.42 | +3.48% | 20% |
| [NH](https://in.tradingview.com/chart/?symbol=NSE:NH)<br><sub>↓CMF11d · 🎯SLING</sub> | ⚠ CAUTION | Affordable cardiac surgery and multispecialty hospitals across India | 🟡 BULL_OS_L2 | 12 | ↓39 | ↑0.982 | ↓13d | — | -8.7% | -58.14/-58.42 | +1.43% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:TMPV,NSE:ASTERDM,NSE:INDIANB,NSE:CESC,NSE:NUCLEUS,NSE:DBCORP,NSE:WIPRO,NSE:GKENERGY,NSE:CHOLAFIN,NSE:SBICARD,NSE:GICRE,NSE:RAINBOW,NSE:ABB,NSE:KPITTECH,NSE:NEWGEN,NSE:ERIS,NSE:ROUTE,NSE:SAFARI,NSE:BAJAJELEC,NSE:IFGLEXPOR,NSE:JKLAKSHMI,NSE:JIOFIN,NSE:TATACAP,NSE:SBFC,NSE:JLHL,NSE:NH
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (16)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [POLYCAB](https://in.tradingview.com/chart/?symbol=NSE:POLYCAB)<br><sub>📶W9 · ↑CMF0d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄55 | ↑1.013 | ↑1d | — | +2.0% | -44.27/-49.73 | +1.99% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 52 | 🔄71 | ↑1.000 | ↓3d | — | +2.5% | -41.74/-41.75 | +2.49% | 20% |
| [UNITDSPR](https://in.tradingview.com/chart/?symbol=NSE:UNITDSPR)<br><sub>📶W9 · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Whisky rum vodka gin spirits manufacturer India | 📈 BULL_ANY_MID | 47 | 🔄58 | ↑1.005 | ↓13d | — | -2.3% | -48.29/-48.49 | +3.63% | 20% |
| [DCBBANK](https://in.tradingview.com/chart/?symbol=NSE:DCBBANK)<br><sub>📶W9 · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Secured lending to retail, MSME, agricultural sectors | 📈 BULL_ANY_MID | 47 | 🔄76 | ↑1.003 | ↓13d | — | -6.8% | -41.75/-44.38 | +3.68% | 20% |
| [CGPOWER](https://in.tradingview.com/chart/?symbol=NSE:CGPOWER)<br><sub>📶W9 · 🚀SS · ↓CMF5d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 29 | ↑70 | ↑1.005 | ↑1d | — | +0.4% | -12.74/-14.29 | +0.38% | 20% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 29 | ↑58 | ↑1.011 | ↑1d | — | +2.1% | 7.14/4.78 | +2.10% | 20% |
| [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Digital payments, fintech, consumer and merchant ecosystem | 📈 BULL_ANY_MID | 24 | ↑88 | ↑1.016 | ↑1d | — | +2.3% | 2.77/0.98 | +2.30% | 20% |
| [ETERNAL](https://in.tradingview.com/chart/?symbol=NSE:ETERNAL)<br><sub>📶W9 · ↑CMF2d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 18 | ↑70 | ↓1.004 | ↑2d | — | +2.2% | -0.89/-2.27 | -0.36% | 20% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>📶W9 · W↑14d · ↑CMF6d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 18 | ↑22 | ↑1.000 | ↓12d | — | +0.8% | -18.3/-18.75 | +0.02% | 20% |
| [VBL](https://in.tradingview.com/chart/?symbol=NSE:VBL)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF6d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 13 | ↑43 | ↑1.022 | ↑12d | — | +7.0% | 24.78/23.0 | +3.29% | 20% |
| [GVT&D](https://in.tradingview.com/chart/?symbol=NSE:GVT&D)<br><sub>📶W9 · ↓CMF3d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 12 | ↑70 | ↓0.994 | ↓8d | — | -2.5% | -29.77/-29.83 | -0.32% | -% |
| [WELENT](https://in.tradingview.com/chart/?symbol=NSE:WELENT)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE | Infrastructure development roads water pipelines oil gas projects | 📈 BULL_ANY_MID | 7 | ↑87 | ↑0.998 | ↓18d | — | -0.2% | -21.6/-21.67 | +0.48% | 20% |
| [MANAPPURAM](https://in.tradingview.com/chart/?symbol=NSE:MANAPPURAM)<br><sub>🚀SS · ↑CMF0d</sub> | ✓ SAFE | Gold loans, NBFC, retail credit, unbanked customers | 📈 BULL_ANY_MID | 59 | 🔄62 | ↑1.008 | ↑1d | — | +3.5% | -46.52/-47.95 | +3.50% | 20% |
| [TVSSRICHAK](https://in.tradingview.com/chart/?symbol=NSE:TVSSRICHAK)<br><sub>🚀SS · ↓CMF12d</sub> | ⚠ CAUTION | Two-wheeler three-wheeler off-highway tyres manufacturer exporter | 📈 BULL_ANY_MID | 35 | 🔄66 | ↑0.994 | ↓42d | — | +13.1% | -44.97/-45.86 | +2.80% | 20% |
| [THANGAMAYL](https://in.tradingview.com/chart/?symbol=NSE:THANGAMAYL)<br><sub>↑CMF14d</sub> | ✓ SAFE | Gold silver diamond jewellery retail Tamil Nadu consumer | 📈 BULL_ANY_MID | 16 | ↑82 | ↑1.000 | ↓9d | — | -2.4% | -46.74/-48.14 | +1.64% | 10% 🟨 |
| [EMMVEE](https://in.tradingview.com/chart/?symbol=NSE:EMMVEE)<br><sub>↓CMF13d · ⚠️TRAP</sub> | ✓ SAFE | Solar PV modules and cells manufacturer for renewable energy | 📈 BULL_ANY_MID | 5 | ↓50 | ↓0.978 | ↓15d | — | -8.5% | -39.89/-40.03 | -0.65% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:POLYCAB,NSE:ADANIPOWER,NSE:UNITDSPR,NSE:DCBBANK,NSE:CGPOWER,NSE:DLF,NSE:PAYTM,NSE:ETERNAL,NSE:HDFCLIFE,NSE:VBL,NSE:GVT&D,NSE:WELENT,NSE:MANAPPURAM,NSE:TVSSRICHAK,NSE:THANGAMAYL,NSE:EMMVEE
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
