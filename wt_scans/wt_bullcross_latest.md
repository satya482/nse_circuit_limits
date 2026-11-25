> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-11-25
*Generated 2026-11-25 15:47 IST*

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

**Total bull crosses today: 82** · 22 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ARFIN,NSE:LGEINDIA,NSE:DAMCAPITAL,NSE:TORNTPHARM,NSE:JWL,NSE:KOPRAN,NSE:CEATLTD,NSE:KOVAI,NSE:EMAMILTD,NSE:PDSL,NSE:ISGEC,NSE:KALAMANDIR,NSE:LTF,NSE:SIGMAADV,NSE:METROPOLIS,NSE:ZOTA,NSE:NPST,NSE:MOTHERSON,NSE:NYKAA,NSE:LTTS,NSE:RAMCOCEM,NSE:YATRA,NSE:SHRIRAMFIN,NSE:ADANIPORTS,NSE:GRAPHITE,NSE:STARHEALTH,NSE:CORONA,NSE:RAMCOIND,NSE:SBILIFE,NSE:LODHA,NSE:GLENMARK,NSE:GLAND,NSE:RACLGEAR,NSE:APOLLOTYRE,NSE:INDHOTEL,NSE:AGARWALEYE,NSE:GSPCROP,NSE:IMPAL,NSE:UNICHEMLAB,NSE:SHALBY,NSE:MEDPLUS,NSE:MHRIL,NSE:SUNDROP,NSE:PAISALO,NSE:INOXGREEN,NSE:CANHLIFE,NSE:TITAGARH,NSE:YUKEN,NSE:ADFFOODS,NSE:EFCIL,NSE:EVONILE,NSE:JNKINDIA,NSE:THANGAMAYL,NSE:MEDIASSIST,NSE:MUKANDLTD,NSE:STAR,NSE:LTM,NSE:AKUMS,NSE:AADHARHFC,NSE:RALLIS,NSE:DHANUKA,NSE:APCOTEXIND,NSE:RAMCOSYS,NSE:KRN,NSE:SESHAPAPER,NSE:WELENT,NSE:ARMANFIN,NSE:CARRARO,NSE:VIMTALABS,NSE:LXCHEM,NSE:GODIGIT,NSE:MASTEK,NSE:GREENPLY,NSE:BANSALWIRE,NSE:SIEMENS,NSE:ADANIENT,NSE:UJJIVANSFB,NSE:CUMMINSIND,NSE:EBGNG,NSE:ANDHRSUGAR,NSE:JUNIPER,NSE:RPGLIFE
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (36)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ARFIN](https://in.tradingview.com/chart/?symbol=NSE:ARFIN)<br><sub>📶W9 · 🚀SS · ↑CMF4d</sub> | ✓ SAFE | Aluminium ferroalloys manufacturing trading steel auto sector | ⚡ BULL_ANY_PPV | 94 | 🔄85 | ↑1.020 | ↑1d | SQ·PV | +4.0% | -15.85/-17.39 | +3.96% | 20% |
| [LGEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LGEINDIA)<br><sub>📶W9 · W↑10d · ↓CMF8d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 63 | ↑73 | ↑1.024 | ↑2d | SQ·PV | +3.4% | 16.11/8.84 | +1.97% | 20% |
| [DAMCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:DAMCAPITAL)<br><sub>📶W9 · W↑12d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | Investment banking, M&A advisory, capital markets solutions | ⚡ BULL_ANY_PPV | 54 | 🔄43 | ↑1.024 | ↑1d | PV | +3.8% | 30.6/29.6 | +3.79% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · W↑1d · 🚀SS · ↑CMF18d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 53 | 🔄69 | ↑1.016 | ↑2d | PV | +3.3% | 5.92/-0.5 | +1.58% | 20% |
| [JWL](https://in.tradingview.com/chart/?symbol=NSE:JWL)<br><sub>📶W9 · W↑12d · 🚀SS·22x · ↑CMF10d · ÷DIV</sub> | ✓ SAFE | Railway wagons and commercial vehicle load bodies manufacturer | ⚡ BULL_ANY_PPV | 49 | 🔄22 | ↑1.114 | ↑1d | PV | +20.0% | -8.77/-12.8 | +20.00% | 20% |
| [KOPRAN](https://in.tradingview.com/chart/?symbol=NSE:KOPRAN)<br><sub>📶W9 · W↑8d · RVOL28x · ↑CMF9d</sub> | ✓ SAFE | APIs and formulations manufacturer serving global pharma | ⚡ BULL_ANY_PPV | 49 | 🔄97 | ↑1.070 | ↑1d | PV | +9.1% | 18.26/10.75 | +9.11% | 20% |
| [CEATLTD](https://in.tradingview.com/chart/?symbol=NSE:CEATLTD)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | Radial and bias tyres for two-wheelers, cars, trucks | ⚡ BULL_ANY_PPV | 37 | 🔄61 | ↑1.019 | ↑18d | PV | +15.9% | 32.84/28.92 | +2.49% | 20% |
| [KOVAI](https://in.tradingview.com/chart/?symbol=NSE:KOVAI)<br><sub>📶W9 · W↑12d · ↑CMF3d</sub> | ⚠ CAUTION | Tertiary hospital network pharmacy education Coimbatore healthcare | ⚡ BULL_ANY_PPV | 11 | ↑50 | ↑1.029 | ↑14d | PV | +13.7% | 57.58/56.55 | +1.09% | 20% |
| [EMAMILTD](https://in.tradingview.com/chart/?symbol=NSE:EMAMILTD)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF25d</sub> | ✓ SAFE | Personal care healthcare FMCG creams balms oils Indian consumers | ⚡ BULL_ANY_PPV | 7 | ↑63 | ↑1.029 | ↑18d | PV | +18.9% | 53.97/53.01 | +2.60% | 20% |
| [PDSL](https://in.tradingview.com/chart/?symbol=NSE:PDSL)<br><sub>📶W9 · W↑18d · ★ · ↑CMF17d</sub> | ✓ SAFE | Apparel sourcing design manufacturing distribution global fashion supply chain | ⚡ BULL_ANY_PPV | 7 | ↑86 | ↑1.023 | ↑18d | PV | +26.7% | 45.26/44.93 | +1.38% | 20% |
| [ISGEC](https://in.tradingview.com/chart/?symbol=NSE:ISGEC)<br><sub>📶W9 · W↑58d · ↑CMF30d</sub> | ⚠ CAUTION | Heavy machinery manufacturing for sugar industrial plants globally | ⚡ BULL_ANY_PPV | 5 | ↑84 | ↑1.028 | ↑22d | PV | +15.2% | 56.55/53.06 | +2.11% | 20% |
| [KALAMANDIR](https://in.tradingview.com/chart/?symbol=NSE:KALAMANDIR)<br><sub>📶W9 · W↑18d · ↑CMF15d</sub> | ✓ SAFE | Ethnic sarees silk apparel retail South India omni-channel | ⚡ BULL_ANY_PPV | 4 | ↑45 | ↑1.095 | ↑16d | PV | +46.0% | 32.18/25.12 | +10.37% | 20% |
| [LTF](https://in.tradingview.com/chart/?symbol=NSE:LTF)<br><sub>📶W9 · W↑12d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | NBFC retail loans construction equipment infrastructure financing | ⚡ BULL_ANY_PPV | 2 | ↑44 | ↑1.030 | ↑18d | PV | +16.2% | 30.59/24.0 | +3.63% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS)<br><sub>📶W9 · W↑12d · 🚀SS · ↑CMF20d</sub> | ⚠ CAUTION | Diagnostic pathology labs urban semi-urban India Africa Middle East | 📈 BULL_ANY_MID | 99 | 🔄68 | ↑1.003 | ↑1d | SQ | +0.7% | 15.28/13.45 | +0.71% | 20% |
| [ZOTA](https://in.tradingview.com/chart/?symbol=NSE:ZOTA)<br><sub>📶W9 · W↑12d · 🚀SS · ↓CMF1d</sub> | ✓ SAFE | Pharma manufacturer: tablets, syrups, Ayurveda, OTC products | 📈 BULL_ANY_MID | 94 | 🔄73 | ↑1.024 | ↑1d | SQ | +4.1% | 10.21/9.82 | +4.10% | 20% |
| [NPST](https://in.tradingview.com/chart/?symbol=NSE:NPST)<br><sub>📶W9 · W↑8d · ↑CMF15d</sub> | ⚠ CAUTION | UPI payments software provider fintech digital banking | 📈 BULL_ANY_MID | 94 | 🔄81 | ↑1.018 | ↑1d | SQ | +3.1% | -3.55/-8.14 | +3.08% | 20% |
| [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON)<br><sub>📶W9 · W↑10d · ↑CMF15d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↑82 | ↓1.012 | ↑3d | SQ | +5.4% | 30.75/25.66 | -0.46% | 20% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>📶W9 · W↑16d · ↑CMF29d</sub> | ✓ SAFE | Beauty and fashion e-commerce platform for urban consumers | 📈 BULL_ANY_MID | 57 | ↓84 | ↓0.999 | ↑3d | SQ | +1.4% | 38.77/37.43 | -1.92% | 20% |
| [LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS)<br><sub>📶W9 · W↑33d · ↑CMF30d</sub> | ✓ SAFE | Engineering R&D services for automotive semiconductor industrial | 📈 BULL_ANY_MID | 57 | ↑78 | ↓1.001 | ↓3d | SQ | +2.3% | 17.02/14.37 | -1.06% | 20% |
| [RAMCOCEM](https://in.tradingview.com/chart/?symbol=NSE:RAMCOCEM)<br><sub>📶W9 · W↑12d · 🚀SS · ↓CMF2d · ÷DIV</sub> | ⚠ CAUTION | Cement producer, RMC, dry mortar for construction | 📈 BULL_ANY_MID | 44 | 🔄31 | ↑1.013 | ↑16d | — | +11.7% | 17.38/16.68 | +2.17% | 20% |
| [YATRA](https://in.tradingview.com/chart/?symbol=NSE:YATRA)<br><sub>📶W9 · W↑8d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE | Online travel bookings for leisure and corporate travelers | 📈 BULL_ANY_MID | 42 | 🔄11 | ↑1.030 | ↑8d | — | +14.8% | 18.75/17.45 | +4.18% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 40 | 🔄54 | ↑1.026 | ↑15d | — | +15.5% | 22.47/18.61 | +2.46% | 20% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>📶W9 · W↑21d · ↑CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 30 | 🔄80 | ↓1.005 | ↑21d | — | +12.4% | 38.62/37.57 | +0.10% | 20% |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE)<br><sub>📶W9 · W↑8d · ↑CMF15d</sub> | ✓ SAFE | Graphite electrodes for electric arc furnace steel making | 📈 BULL_ANY_MID | 27 | ↑80 | ↑1.015 | ↑3d | — | +3.8% | 25.81/22.41 | +0.58% | 20% |
| [STARHEALTH](https://in.tradingview.com/chart/?symbol=NSE:STARHEALTH)<br><sub>📶W9 · W↑12d · ↑CMF0d</sub> | ⚠ CAUTION | Health insurance provider, retail customers, India | 📈 BULL_ANY_MID | 24 | ↑70 | ↑1.013 | ↑6d | — | +3.6% | 23.31/18.46 | +0.86% | 20% |
| [CORONA](https://in.tradingview.com/chart/?symbol=NSE:CORONA)<br><sub>📶W9 · W↑18d · ↓CMF10d</sub> | ✓ SAFE | Pharma formulations women's health cardiology pain management domestic | 📈 BULL_ANY_MID | 17 | ↑50 | ↑1.033 | ↑3d | — | +5.8% | 16.02/13.35 | +3.37% | 20% |
| [RAMCOIND](https://in.tradingview.com/chart/?symbol=NSE:RAMCOIND)<br><sub>📶W9 · W↑12d · 🚀SS · ↑CMF14d</sub> | ⚠ CAUTION | Fiber cement boards, calcium silicate boards, cotton yarn manufacturer | 📈 BULL_ANY_MID | 12 | ↑57 | ↑1.013 | ↑18d | — | +11.5% | 19.97/16.12 | +1.15% | 20% |
| [SBILIFE](https://in.tradingview.com/chart/?symbol=NSE:SBILIFE)<br><sub>📶W9 · W↑16d · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 5 | ↑48 | ↓1.007 | ↑15d | — | +9.1% | 46.12/45.95 | -1.18% | 20% |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>📶W9 · W↑10d · ↑CMF13d</sub> | ✓ SAFE | Residential and commercial real estate development, Mumbai Pune Bangalore | 📈 BULL_ANY_MID | 5 | ↑70 | ↓1.021 | ↑15d | — | +21.6% | 35.54/34.6 | +0.02% | 20% |
| [GLENMARK](https://in.tradingview.com/chart/?symbol=NSE:GLENMARK)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF17d</sub> | ✓ SAFE | Generics, specialty drugs, OTC pharma, global markets | 📈 BULL_ANY_MID | 5 | ↑84 | ↑1.030 | ↑22d | — | +22.2% | 44.5/42.63 | +2.33% | 20% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Generic injectables manufacturer for global regulated markets | 📈 BULL_ANY_MID | 5 | ↑95 | ↑1.018 | ↑21d | — | +13.1% | 46.2/44.84 | +1.55% | 20% |
| [RACLGEAR](https://in.tradingview.com/chart/?symbol=NSE:RACLGEAR)<br><sub>📶W9 · W↑8d · ↑CMF0d</sub> | ✓ SAFE | Precision automotive gears and components for global OEMs | 📈 BULL_ANY_MID | 4 | ↑81 | ↑1.031 | ↑16d | — | +13.4% | 37.61/36.86 | +3.15% | 20% |
| [APOLLOTYRE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOTYRE)<br><sub>📶W9 · W↑12d · ↓CMF30d</sub> | ⚠ CAUTION | Radial tyres for cars trucks farm vehicles | 📈 BULL_ANY_MID | 3 | ↑52 | ↑1.037 | ↑17d | — | +12.2% | 33.7/26.23 | +3.96% | 20% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>📶W9 · W↑30d · ↑CMF22d</sub> | ✓ SAFE | Luxury and midscale hotel brands across Asia Pacific | 📈 BULL_ANY_MID | 0 | ↑89 | ↓1.020 | ↑29d | — | +27.3% | 57.17/56.79 | -0.66% | 20% |
| [AGARWALEYE](https://in.tradingview.com/chart/?symbol=NSE:AGARWALEYE)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION | Eye care surgery and diagnostics across India Africa | 📈 BULL_ANY_MID | 0 | ↑80 | ↑1.046 | ↑23d | — | +21.6% | 52.74/50.67 | +4.65% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ARFIN,NSE:LGEINDIA,NSE:DAMCAPITAL,NSE:TORNTPHARM,NSE:JWL,NSE:KOPRAN,NSE:CEATLTD,NSE:KOVAI,NSE:EMAMILTD,NSE:PDSL,NSE:ISGEC,NSE:KALAMANDIR,NSE:LTF,NSE:SIGMAADV,NSE:METROPOLIS,NSE:ZOTA,NSE:NPST,NSE:MOTHERSON,NSE:NYKAA,NSE:LTTS,NSE:RAMCOCEM,NSE:YATRA,NSE:SHRIRAMFIN,NSE:ADANIPORTS,NSE:GRAPHITE,NSE:STARHEALTH,NSE:CORONA,NSE:RAMCOIND,NSE:SBILIFE,NSE:LODHA,NSE:GLENMARK,NSE:GLAND,NSE:RACLGEAR,NSE:APOLLOTYRE,NSE:INDHOTEL,NSE:AGARWALEYE
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (63)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ARFIN](https://in.tradingview.com/chart/?symbol=NSE:ARFIN)<br><sub>📶W9 · 🚀SS · ↑CMF4d</sub> | ✓ SAFE | Aluminium ferroalloys manufacturing trading steel auto sector | ⚡ BULL_ANY_PPV | 94 | 🔄85 | ↑1.020 | ↑1d | SQ·PV | +4.0% | -15.85/-17.39 | +3.96% | 20% |
| [LGEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LGEINDIA)<br><sub>📶W9 · W↑10d · ↓CMF8d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 63 | ↑73 | ↑1.024 | ↑2d | SQ·PV | +3.4% | 16.11/8.84 | +1.97% | 20% |
| [DAMCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:DAMCAPITAL)<br><sub>📶W9 · W↑12d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | Investment banking, M&A advisory, capital markets solutions | ⚡ BULL_ANY_PPV | 54 | 🔄43 | ↑1.024 | ↑1d | PV | +3.8% | 30.6/29.6 | +3.79% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · W↑1d · 🚀SS · ↑CMF18d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 53 | 🔄69 | ↑1.016 | ↑2d | PV | +3.3% | 5.92/-0.5 | +1.58% | 20% |
| [JWL](https://in.tradingview.com/chart/?symbol=NSE:JWL)<br><sub>📶W9 · W↑12d · 🚀SS·22x · ↑CMF10d · ÷DIV</sub> | ✓ SAFE | Railway wagons and commercial vehicle load bodies manufacturer | ⚡ BULL_ANY_PPV | 49 | 🔄22 | ↑1.114 | ↑1d | PV | +20.0% | -8.77/-12.8 | +20.00% | 20% |
| [KOPRAN](https://in.tradingview.com/chart/?symbol=NSE:KOPRAN)<br><sub>📶W9 · W↑8d · RVOL28x · ↑CMF9d</sub> | ✓ SAFE | APIs and formulations manufacturer serving global pharma | ⚡ BULL_ANY_PPV | 49 | 🔄97 | ↑1.070 | ↑1d | PV | +9.1% | 18.26/10.75 | +9.11% | 20% |
| [CEATLTD](https://in.tradingview.com/chart/?symbol=NSE:CEATLTD)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | Radial and bias tyres for two-wheelers, cars, trucks | ⚡ BULL_ANY_PPV | 37 | 🔄61 | ↑1.019 | ↑18d | PV | +15.9% | 32.84/28.92 | +2.49% | 20% |
| [KOVAI](https://in.tradingview.com/chart/?symbol=NSE:KOVAI)<br><sub>📶W9 · W↑12d · ↑CMF3d</sub> | ⚠ CAUTION | Tertiary hospital network pharmacy education Coimbatore healthcare | ⚡ BULL_ANY_PPV | 11 | ↑50 | ↑1.029 | ↑14d | PV | +13.7% | 57.58/56.55 | +1.09% | 20% |
| [EMAMILTD](https://in.tradingview.com/chart/?symbol=NSE:EMAMILTD)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF25d</sub> | ✓ SAFE | Personal care healthcare FMCG creams balms oils Indian consumers | ⚡ BULL_ANY_PPV | 7 | ↑63 | ↑1.029 | ↑18d | PV | +18.9% | 53.97/53.01 | +2.60% | 20% |
| [PDSL](https://in.tradingview.com/chart/?symbol=NSE:PDSL)<br><sub>📶W9 · W↑18d · ★ · ↑CMF17d</sub> | ✓ SAFE | Apparel sourcing design manufacturing distribution global fashion supply chain | ⚡ BULL_ANY_PPV | 7 | ↑86 | ↑1.023 | ↑18d | PV | +26.7% | 45.26/44.93 | +1.38% | 20% |
| [ISGEC](https://in.tradingview.com/chart/?symbol=NSE:ISGEC)<br><sub>📶W9 · W↑58d · ↑CMF30d</sub> | ⚠ CAUTION | Heavy machinery manufacturing for sugar industrial plants globally | ⚡ BULL_ANY_PPV | 5 | ↑84 | ↑1.028 | ↑22d | PV | +15.2% | 56.55/53.06 | +2.11% | 20% |
| [KALAMANDIR](https://in.tradingview.com/chart/?symbol=NSE:KALAMANDIR)<br><sub>📶W9 · W↑18d · ↑CMF15d</sub> | ✓ SAFE | Ethnic sarees silk apparel retail South India omni-channel | ⚡ BULL_ANY_PPV | 4 | ↑45 | ↑1.095 | ↑16d | PV | +46.0% | 32.18/25.12 | +10.37% | 20% |
| [LTF](https://in.tradingview.com/chart/?symbol=NSE:LTF)<br><sub>📶W9 · W↑12d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | NBFC retail loans construction equipment infrastructure financing | ⚡ BULL_ANY_PPV | 2 | ↑44 | ↑1.030 | ↑18d | PV | +16.2% | 30.59/24.0 | +3.63% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS)<br><sub>📶W9 · W↑12d · 🚀SS · ↑CMF20d</sub> | ⚠ CAUTION | Diagnostic pathology labs urban semi-urban India Africa Middle East | 📈 BULL_ANY_MID | 99 | 🔄68 | ↑1.003 | ↑1d | SQ | +0.7% | 15.28/13.45 | +0.71% | 20% |
| [ZOTA](https://in.tradingview.com/chart/?symbol=NSE:ZOTA)<br><sub>📶W9 · W↑12d · 🚀SS · ↓CMF1d</sub> | ✓ SAFE | Pharma manufacturer: tablets, syrups, Ayurveda, OTC products | 📈 BULL_ANY_MID | 94 | 🔄73 | ↑1.024 | ↑1d | SQ | +4.1% | 10.21/9.82 | +4.10% | 20% |
| [NPST](https://in.tradingview.com/chart/?symbol=NSE:NPST)<br><sub>📶W9 · W↑8d · ↑CMF15d</sub> | ⚠ CAUTION | UPI payments software provider fintech digital banking | 📈 BULL_ANY_MID | 94 | 🔄81 | ↑1.018 | ↑1d | SQ | +3.1% | -3.55/-8.14 | +3.08% | 20% |
| [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON)<br><sub>📶W9 · W↑10d · ↑CMF15d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↑82 | ↓1.012 | ↑3d | SQ | +5.4% | 30.75/25.66 | -0.46% | 20% |
| [LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS)<br><sub>📶W9 · W↑33d · ↑CMF30d</sub> | ✓ SAFE | Engineering R&D services for automotive semiconductor industrial | 📈 BULL_ANY_MID | 57 | ↑78 | ↓1.001 | ↓3d | SQ | +2.3% | 17.02/14.37 | -1.06% | 20% |
| [RAMCOCEM](https://in.tradingview.com/chart/?symbol=NSE:RAMCOCEM)<br><sub>📶W9 · W↑12d · 🚀SS · ↓CMF2d · ÷DIV</sub> | ⚠ CAUTION | Cement producer, RMC, dry mortar for construction | 📈 BULL_ANY_MID | 44 | 🔄31 | ↑1.013 | ↑16d | — | +11.7% | 17.38/16.68 | +2.17% | 20% |
| [YATRA](https://in.tradingview.com/chart/?symbol=NSE:YATRA)<br><sub>📶W9 · W↑8d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE | Online travel bookings for leisure and corporate travelers | 📈 BULL_ANY_MID | 42 | 🔄11 | ↑1.030 | ↑8d | — | +14.8% | 18.75/17.45 | +4.18% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 40 | 🔄54 | ↑1.026 | ↑15d | — | +15.5% | 22.47/18.61 | +2.46% | 20% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>📶W9 · W↑21d · ↑CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 30 | 🔄80 | ↓1.005 | ↑21d | — | +12.4% | 38.62/37.57 | +0.10% | 20% |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE)<br><sub>📶W9 · W↑8d · ↑CMF15d</sub> | ✓ SAFE | Graphite electrodes for electric arc furnace steel making | 📈 BULL_ANY_MID | 27 | ↑80 | ↑1.015 | ↑3d | — | +3.8% | 25.81/22.41 | +0.58% | 20% |
| [STARHEALTH](https://in.tradingview.com/chart/?symbol=NSE:STARHEALTH)<br><sub>📶W9 · W↑12d · ↑CMF0d</sub> | ⚠ CAUTION | Health insurance provider, retail customers, India | 📈 BULL_ANY_MID | 24 | ↑70 | ↑1.013 | ↑6d | — | +3.6% | 23.31/18.46 | +0.86% | 20% |
| [CORONA](https://in.tradingview.com/chart/?symbol=NSE:CORONA)<br><sub>📶W9 · W↑18d · ↓CMF10d</sub> | ✓ SAFE | Pharma formulations women's health cardiology pain management domestic | 📈 BULL_ANY_MID | 17 | ↑50 | ↑1.033 | ↑3d | — | +5.8% | 16.02/13.35 | +3.37% | 20% |
| [RAMCOIND](https://in.tradingview.com/chart/?symbol=NSE:RAMCOIND)<br><sub>📶W9 · W↑12d · 🚀SS · ↑CMF14d</sub> | ⚠ CAUTION | Fiber cement boards, calcium silicate boards, cotton yarn manufacturer | 📈 BULL_ANY_MID | 12 | ↑57 | ↑1.013 | ↑18d | — | +11.5% | 19.97/16.12 | +1.15% | 20% |
| [SBILIFE](https://in.tradingview.com/chart/?symbol=NSE:SBILIFE)<br><sub>📶W9 · W↑16d · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 5 | ↑48 | ↓1.007 | ↑15d | — | +9.1% | 46.12/45.95 | -1.18% | 20% |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>📶W9 · W↑10d · ↑CMF13d</sub> | ✓ SAFE | Residential and commercial real estate development, Mumbai Pune Bangalore | 📈 BULL_ANY_MID | 5 | ↑70 | ↓1.021 | ↑15d | — | +21.6% | 35.54/34.6 | +0.02% | 20% |
| [GLENMARK](https://in.tradingview.com/chart/?symbol=NSE:GLENMARK)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF17d</sub> | ✓ SAFE | Generics, specialty drugs, OTC pharma, global markets | 📈 BULL_ANY_MID | 5 | ↑84 | ↑1.030 | ↑22d | — | +22.2% | 44.5/42.63 | +2.33% | 20% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Generic injectables manufacturer for global regulated markets | 📈 BULL_ANY_MID | 5 | ↑95 | ↑1.018 | ↑21d | — | +13.1% | 46.2/44.84 | +1.55% | 20% |
| [RACLGEAR](https://in.tradingview.com/chart/?symbol=NSE:RACLGEAR)<br><sub>📶W9 · W↑8d · ↑CMF0d</sub> | ✓ SAFE | Precision automotive gears and components for global OEMs | 📈 BULL_ANY_MID | 4 | ↑81 | ↑1.031 | ↑16d | — | +13.4% | 37.61/36.86 | +3.15% | 20% |
| [APOLLOTYRE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOTYRE)<br><sub>📶W9 · W↑12d · ↓CMF30d</sub> | ⚠ CAUTION | Radial tyres for cars trucks farm vehicles | 📈 BULL_ANY_MID | 3 | ↑52 | ↑1.037 | ↑17d | — | +12.2% | 33.7/26.23 | +3.96% | 20% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>📶W9 · W↑30d · ↑CMF22d</sub> | ✓ SAFE | Luxury and midscale hotel brands across Asia Pacific | 📈 BULL_ANY_MID | 0 | ↑89 | ↓1.020 | ↑29d | — | +27.3% | 57.17/56.79 | -0.66% | 20% |
| [AGARWALEYE](https://in.tradingview.com/chart/?symbol=NSE:AGARWALEYE)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION | Eye care surgery and diagnostics across India Africa | 📈 BULL_ANY_MID | 0 | ↑80 | ↑1.046 | ↑23d | — | +21.6% | 52.74/50.67 | +4.65% | 20% |
| [GSPCROP](https://in.tradingview.com/chart/?symbol=NSE:GSPCROP)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Fungicides insecticides pesticides agrochemicals formulation manufacturing | 🔥 BULL_OS_PPV | 54 | 🔄50 | ↑1.023 | ↑1d | PV | +6.1% | -57.39/-63.31 | +6.14% | 20% |
| [IMPAL](https://in.tradingview.com/chart/?symbol=NSE:IMPAL)<br><sub>W↑3d · ↑CMF0d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄49 | ↑1.012 | ↑1d | SQ·PV | +2.2% | -1.79/-4.75 | +2.16% | 20% |
| [UNICHEMLAB](https://in.tradingview.com/chart/?symbol=NSE:UNICHEMLAB)<br><sub>↓CMF30d</sub> | ✓ SAFE | Generic drugs, APIs, contract manufacturing for pharma | ⚡ BULL_ANY_PPV | 89 | 🔄76 | ↑1.040 | ↑1d | SQ·PV | +7.6% | -43.62/-48.24 | +7.60% | 20% |
| [SHALBY](https://in.tradingview.com/chart/?symbol=NSE:SHALBY)<br><sub>W↑12d · ↓CMF30d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 89 | 🔄9 | ↑1.036 | ↑1d | SQ·PV | +5.0% | -5.49/-16.09 | +5.05% | 20% |
| [MHRIL](https://in.tradingview.com/chart/?symbol=NSE:MHRIL)<br><sub>W↑18d · RVOL40x · ↓CMF25d · ÷DIV</sub> | ✓ SAFE | Vacation ownership memberships family holidays resorts hospitality | ⚡ BULL_ANY_PPV | 59 | 🔄19 | ↑1.003 | ↑1d | PV | +0.8% | 15.76/8.82 | +0.83% | 20% |
| [SUNDROP](https://in.tradingview.com/chart/?symbol=NSE:SUNDROP)<br><sub>↓CMF29d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 59 | 🔄39 | ↑1.008 | ↑1d | PV | +2.9% | -36.96/-37.46 | +2.88% | 20% |
| [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO)<br><sub>🚀SS · ↑CMF10d · 🎯SLING</sub> | ✓ SAFE | Micro-lending NBFC for underbanked rural India income earners | ⚡ BULL_ANY_PPV | 50 | 🔄95 | ↑1.001 | ↓10d | PV | -3.9% | -55.49/-58.73 | +2.27% | 20% |
| [INOXGREEN](https://in.tradingview.com/chart/?symbol=NSE:INOXGREEN)<br><sub>W↑12d · RVOL9x · ↑CMF7d</sub> | ✓ SAFE | Wind turbine operations maintenance services provider India | ⚡ BULL_ANY_PPV | 49 | 🔄3 | ↑1.043 | ↑1d | PV | +9.5% | -32.75/-33.89 | +9.49% | 20% |
| [CANHLIFE](https://in.tradingview.com/chart/?symbol=NSE:CANHLIFE)<br><sub>↑CMF9d</sub> | ⚠ CAUTION | Life insurance through bank distribution channels | ⚡ BULL_ANY_PPV | 49 | 🔄39 | ↑1.040 | ↑1d | PV | +6.8% | -1.3/-4.8 | +6.78% | 20% |
| [TITAGARH](https://in.tradingview.com/chart/?symbol=NSE:TITAGARH)<br><sub>W↑8d · 🚀SS · ↑CMF4d</sub> | ✓ SAFE | Rail wagons coaches metro trains manufacturing | ⚡ BULL_ANY_PPV | 42 | 🔄40 | ↑1.026 | ↑13d | PV | +9.9% | 20.38/17.0 | +3.82% | 20% |
| [MUKANDLTD](https://in.tradingview.com/chart/?symbol=NSE:MUKANDLTD)<br><sub>↓CMF23d · 🎯SLING</sub> | ✓ SAFE | Specialty steel bars, billets, cranes, material handling equipment | 🟡 BULL_OS_L2 | 35 | 🔄58 | ↑0.999 | ↓29d | — | -18.9% | -54.94/-56.91 | +3.02% | 20% |
| [LTM](https://in.tradingview.com/chart/?symbol=NSE:LTM)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄34 | ↑1.008 | ↑1d | SQ | +1.2% | -12.65/-14.88 | +1.17% | 20% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Pharma CDMO formulations development manufacturing domestic international markets | 📈 BULL_ANY_MID | 99 | 🔄89 | ↑1.011 | ↑1d | SQ | +1.5% | -16.29/-21.34 | +1.53% | 20% |
| [AADHARHFC](https://in.tradingview.com/chart/?symbol=NSE:AADHARHFC)<br><sub>↑CMF29d</sub> | ✓ SAFE | Low-income housing loans, retail, affordable home buyers | 📈 BULL_ANY_MID | 99 | 🔄35 | ↑1.005 | ↑1d | SQ | +2.4% | -46.28/-49.2 | +2.36% | 20% |
| [RALLIS](https://in.tradingview.com/chart/?symbol=NSE:RALLIS)<br><sub>W↑8d · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Agrochemicals, seeds, crop nutrients for Indian farmers | 📈 BULL_ANY_MID | 99 | 🔄16 | ↑1.004 | ↑1d | SQ | +1.2% | -36.58/-39.01 | +1.23% | 20% |
| [DHANUKA](https://in.tradingview.com/chart/?symbol=NSE:DHANUKA)<br><sub>W↑23d · ↑CMF18d</sub> | ✓ SAFE | Herbicides insecticides fungicides manufacturing for Indian farmers | 📈 BULL_ANY_MID | 94 | 🔄30 | ↑1.016 | ↑1d | SQ | +2.8% | -2.2/-2.99 | +2.77% | 20% |
| [APCOTEXIND](https://in.tradingview.com/chart/?symbol=NSE:APCOTEXIND)<br><sub>🚀SS · ↓CMF30d · ÷DIV</sub> | ⚠ CAUTION | Synthetic rubber and latex polymers for coatings, adhesives | 📈 BULL_ANY_MID | 75 | 🔄53 | ↑1.000 | ↓29d | SQ | -17.4% | -44.11/-45.67 | +1.42% | 20% |
| [RAMCOSYS](https://in.tradingview.com/chart/?symbol=NSE:RAMCOSYS)<br><sub>↓CMF5d</sub> | ✓ SAFE | ERP software, HCM, aviation, manufacturing, cloud | 📈 BULL_ANY_MID | 67 | ↑64 | ↑1.004 | ↑3d | SQ | +1.1% | 4.34/3.79 | +0.41% | 10% 🟩 |
| [KRN](https://in.tradingview.com/chart/?symbol=NSE:KRN)<br><sub>🚀SS · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Heat exchanger manufacturer HVAC refrigeration OEM supplier | 📈 BULL_ANY_MID | 59 | 🔄29 | ↑1.013 | ↑1d | — | +4.5% | -42.09/-43.96 | +4.52% | 5% 🟥 |
| [SESHAPAPER](https://in.tradingview.com/chart/?symbol=NSE:SESHAPAPER)<br><sub>↑CMF1d</sub> | ⚠ CAUTION | Integrated paper and paperboards manufacturer Tamil Nadu facilities | 📈 BULL_ANY_MID | 59 | 🔄32 | ↑1.001 | ↑1d | — | +0.7% | -18.1/-18.39 | +0.67% | 20% |
| [WELENT](https://in.tradingview.com/chart/?symbol=NSE:WELENT)<br><sub>↓CMF13d</sub> | ✓ SAFE | Infrastructure development roads water pipelines oil gas projects | 📈 BULL_ANY_MID | 56 | 🔄83 | ↑1.007 | ↑4d | — | +2.6% | -1.15/-3.86 | +0.85% | 20% |
| [ARMANFIN](https://in.tradingview.com/chart/?symbol=NSE:ARMANFIN)<br><sub>↑CMF15d</sub> | ✓ SAFE | NBFC loans unorganized sector rural semi-urban India | 📈 BULL_ANY_MID | 54 | 🔄40 | ↑1.023 | ↑1d | — | +4.4% | -6.89/-7.74 | +4.42% | 20% |
| [CARRARO](https://in.tradingview.com/chart/?symbol=NSE:CARRARO)<br><sub>↓CMF20d</sub> | ✓ SAFE | Axles transmissions agricultural tractors construction equipment | 📈 BULL_ANY_MID | 54 | 🔄32 | ↑1.021 | ↑1d | — | +3.3% | -42.6/-48.56 | +3.26% | 20% |
| [VIMTALABS](https://in.tradingview.com/chart/?symbol=NSE:VIMTALABS)<br><sub>↓CMF30d</sub> | ✓ SAFE | Contract research testing pharma biotech chemicals | 📈 BULL_ANY_MID | 47 | 🔄23 | ↑1.003 | ↓13d | — | -2.8% | -49.47/-51.01 | +2.57% | 20% |
| [LXCHEM](https://in.tradingview.com/chart/?symbol=NSE:LXCHEM)<br><sub>🚀SS · ↓CMF25d</sub> | ✓ SAFE | Acetyl intermediates and specialty chemicals manufacturer for pharma | 📈 BULL_ANY_MID | 45 | 🔄49 | ↑1.003 | ↓15d | — | -4.8% | -41.98/-41.98 | +3.55% | 20% |
| [GODIGIT](https://in.tradingview.com/chart/?symbol=NSE:GODIGIT)<br><sub>🚀SS · ↓CMF10d</sub> | ⚠ CAUTION | Digital-first general insurance, motor and health focused | 📈 BULL_ANY_MID | 40 | 🔄18 | ↑1.001 | ↓45d | — | -0.4% | -50.39/-52.98 | +3.00% | 20% |
| [GREENPLY](https://in.tradingview.com/chart/?symbol=NSE:GREENPLY)<br><sub>↓CMF18d · ÷DIV</sub> | ✓ SAFE | Plywood MDF doors flooring for residential commercial construction | 📈 BULL_ANY_MID | 40 | 🔄58 | ↑1.001 | ↓20d | — | -8.8% | -34.53/-34.77 | +1.18% | 20% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>W↑3d · ↓CMF30d</sub> | ✓ SAFE | Microfinance bank serving low-income retail borrowers India | 📈 BULL_ANY_MID | 15 | ↑55 | ↑1.006 | ↑15d | — | +7.1% | 13.57/10.31 | +0.41% | -% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ARFIN,NSE:LGEINDIA,NSE:DAMCAPITAL,NSE:TORNTPHARM,NSE:JWL,NSE:KOPRAN,NSE:CEATLTD,NSE:KOVAI,NSE:EMAMILTD,NSE:PDSL,NSE:ISGEC,NSE:KALAMANDIR,NSE:LTF,NSE:SIGMAADV,NSE:METROPOLIS,NSE:ZOTA,NSE:NPST,NSE:MOTHERSON,NSE:LTTS,NSE:RAMCOCEM,NSE:YATRA,NSE:SHRIRAMFIN,NSE:ADANIPORTS,NSE:GRAPHITE,NSE:STARHEALTH,NSE:CORONA,NSE:RAMCOIND,NSE:SBILIFE,NSE:LODHA,NSE:GLENMARK,NSE:GLAND,NSE:RACLGEAR,NSE:APOLLOTYRE,NSE:INDHOTEL,NSE:AGARWALEYE,NSE:GSPCROP,NSE:IMPAL,NSE:UNICHEMLAB,NSE:SHALBY,NSE:MHRIL,NSE:SUNDROP,NSE:PAISALO,NSE:INOXGREEN,NSE:CANHLIFE,NSE:TITAGARH,NSE:MUKANDLTD,NSE:LTM,NSE:AKUMS,NSE:AADHARHFC,NSE:RALLIS,NSE:DHANUKA,NSE:APCOTEXIND,NSE:RAMCOSYS,NSE:KRN,NSE:SESHAPAPER,NSE:WELENT,NSE:ARMANFIN,NSE:CARRARO,NSE:VIMTALABS,NSE:LXCHEM,NSE:GODIGIT,NSE:GREENPLY,NSE:UJJIVANSFB
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (22)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ARFIN](https://in.tradingview.com/chart/?symbol=NSE:ARFIN)<br><sub>📶W9 · 🚀SS · ↑CMF4d</sub> | ✓ SAFE | Aluminium ferroalloys manufacturing trading steel auto sector | ⚡ BULL_ANY_PPV | 94 | 🔄85 | ↑1.020 | ↑1d | SQ·PV | +4.0% | -15.85/-17.39 | +3.96% | 20% |
| [LGEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LGEINDIA)<br><sub>📶W9 · W↑10d · ↓CMF8d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 63 | ↑73 | ↑1.024 | ↑2d | SQ·PV | +3.4% | 16.11/8.84 | +1.97% | 20% |
| [METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS)<br><sub>📶W9 · W↑12d · 🚀SS · ↑CMF20d</sub> | ⚠ CAUTION | Diagnostic pathology labs urban semi-urban India Africa Middle East | 📈 BULL_ANY_MID | 99 | 🔄68 | ↑1.003 | ↑1d | SQ | +0.7% | 15.28/13.45 | +0.71% | 20% |
| [ZOTA](https://in.tradingview.com/chart/?symbol=NSE:ZOTA)<br><sub>📶W9 · W↑12d · 🚀SS · ↓CMF1d</sub> | ✓ SAFE | Pharma manufacturer: tablets, syrups, Ayurveda, OTC products | 📈 BULL_ANY_MID | 94 | 🔄73 | ↑1.024 | ↑1d | SQ | +4.1% | 10.21/9.82 | +4.10% | 20% |
| [NPST](https://in.tradingview.com/chart/?symbol=NSE:NPST)<br><sub>📶W9 · W↑8d · ↑CMF15d</sub> | ⚠ CAUTION | UPI payments software provider fintech digital banking | 📈 BULL_ANY_MID | 94 | 🔄81 | ↑1.018 | ↑1d | SQ | +3.1% | -3.55/-8.14 | +3.08% | 20% |
| [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON)<br><sub>📶W9 · W↑10d · ↑CMF15d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↑82 | ↓1.012 | ↑3d | SQ | +5.4% | 30.75/25.66 | -0.46% | 20% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>📶W9 · W↑16d · ↑CMF29d</sub> | ✓ SAFE | Beauty and fashion e-commerce platform for urban consumers | 📈 BULL_ANY_MID | 57 | ↓84 | ↓0.999 | ↑3d | SQ | +1.4% | 38.77/37.43 | -1.92% | 20% |
| [LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS)<br><sub>📶W9 · W↑33d · ↑CMF30d</sub> | ✓ SAFE | Engineering R&D services for automotive semiconductor industrial | 📈 BULL_ANY_MID | 57 | ↑78 | ↓1.001 | ↓3d | SQ | +2.3% | 17.02/14.37 | -1.06% | 20% |
| [IMPAL](https://in.tradingview.com/chart/?symbol=NSE:IMPAL)<br><sub>W↑3d · ↑CMF0d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄49 | ↑1.012 | ↑1d | SQ·PV | +2.2% | -1.79/-4.75 | +2.16% | 20% |
| [UNICHEMLAB](https://in.tradingview.com/chart/?symbol=NSE:UNICHEMLAB)<br><sub>↓CMF30d</sub> | ✓ SAFE | Generic drugs, APIs, contract manufacturing for pharma | ⚡ BULL_ANY_PPV | 89 | 🔄76 | ↑1.040 | ↑1d | SQ·PV | +7.6% | -43.62/-48.24 | +7.60% | 20% |
| [SHALBY](https://in.tradingview.com/chart/?symbol=NSE:SHALBY)<br><sub>W↑12d · ↓CMF30d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 89 | 🔄9 | ↑1.036 | ↑1d | SQ·PV | +5.0% | -5.49/-16.09 | +5.05% | 20% |
| [MEDPLUS](https://in.tradingview.com/chart/?symbol=NSE:MEDPLUS)<br><sub>W↑12d · ↑CMF0d</sub> | ✓ SAFE | Retail pharmacy chain with diagnostic centers nationwide | ⚡ BULL_ANY_PPV | 62 | ↓13 | ↑1.000 | ↑3d | SQ·PV | +0.2% | -15.77/-16.91 | +0.12% | 20% |
| [EFCIL](https://in.tradingview.com/chart/?symbol=NSE:EFCIL)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Managed office spaces, integrated building services, corporate real estate | 🟢 BULL_OVERSOLD | 49 | ↓8 | ↓0.997 | ↓11d | SQ | -1.8% | -60.21/-62.52 | -0.24% | 20% |
| [MEDIASSIST](https://in.tradingview.com/chart/?symbol=NSE:MEDIASSIST)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Health claims processing and network management for insurers | 🟡 BULL_OS_L2 | 53 | ↓7 | ↓0.982 | ↓7d | SQ | -2.8% | -54.4/-55.65 | -1.35% | 20% |
| [LTM](https://in.tradingview.com/chart/?symbol=NSE:LTM)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄34 | ↑1.008 | ↑1d | SQ | +1.2% | -12.65/-14.88 | +1.17% | 20% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Pharma CDMO formulations development manufacturing domestic international markets | 📈 BULL_ANY_MID | 99 | 🔄89 | ↑1.011 | ↑1d | SQ | +1.5% | -16.29/-21.34 | +1.53% | 20% |
| [AADHARHFC](https://in.tradingview.com/chart/?symbol=NSE:AADHARHFC)<br><sub>↑CMF29d</sub> | ✓ SAFE | Low-income housing loans, retail, affordable home buyers | 📈 BULL_ANY_MID | 99 | 🔄35 | ↑1.005 | ↑1d | SQ | +2.4% | -46.28/-49.2 | +2.36% | 20% |
| [RALLIS](https://in.tradingview.com/chart/?symbol=NSE:RALLIS)<br><sub>W↑8d · 🚀SS · ↓CMF8d</sub> | ✓ SAFE | Agrochemicals, seeds, crop nutrients for Indian farmers | 📈 BULL_ANY_MID | 99 | 🔄16 | ↑1.004 | ↑1d | SQ | +1.2% | -36.58/-39.01 | +1.23% | 20% |
| [DHANUKA](https://in.tradingview.com/chart/?symbol=NSE:DHANUKA)<br><sub>W↑23d · ↑CMF18d</sub> | ✓ SAFE | Herbicides insecticides fungicides manufacturing for Indian farmers | 📈 BULL_ANY_MID | 94 | 🔄30 | ↑1.016 | ↑1d | SQ | +2.8% | -2.2/-2.99 | +2.77% | 20% |
| [APCOTEXIND](https://in.tradingview.com/chart/?symbol=NSE:APCOTEXIND)<br><sub>🚀SS · ↓CMF30d · ÷DIV</sub> | ⚠ CAUTION | Synthetic rubber and latex polymers for coatings, adhesives | 📈 BULL_ANY_MID | 75 | 🔄53 | ↑1.000 | ↓29d | SQ | -17.4% | -44.11/-45.67 | +1.42% | 20% |
| [RAMCOSYS](https://in.tradingview.com/chart/?symbol=NSE:RAMCOSYS)<br><sub>↓CMF5d</sub> | ✓ SAFE | ERP software, HCM, aviation, manufacturing, cloud | 📈 BULL_ANY_MID | 67 | ↑64 | ↑1.004 | ↑3d | SQ | +1.1% | 4.34/3.79 | +0.41% | 10% 🟩 |
| [MASTEK](https://in.tradingview.com/chart/?symbol=NSE:MASTEK)<br><sub>↓CMF23d · ⚠️TRAP</sub> | ✓ SAFE | Digital engineering, Oracle Cloud, enterprise transformation | 📈 BULL_ANY_MID | 40 | ↓16 | ↓0.987 | ↓38d | SQ | -7.2% | -31.06/-32.0 | -0.67% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ARFIN,NSE:LGEINDIA,NSE:METROPOLIS,NSE:ZOTA,NSE:NPST,NSE:MOTHERSON,NSE:NYKAA,NSE:LTTS,NSE:IMPAL,NSE:UNICHEMLAB,NSE:SHALBY,NSE:MEDPLUS,NSE:EFCIL,NSE:MEDIASSIST,NSE:LTM,NSE:AKUMS,NSE:AADHARHFC,NSE:RALLIS,NSE:DHANUKA,NSE:APCOTEXIND,NSE:RAMCOSYS,NSE:MASTEK
```

---

### 🔥 MAJOR — PPV confirmed (21)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [DAMCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:DAMCAPITAL)<br><sub>📶W9 · W↑12d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | Investment banking, M&A advisory, capital markets solutions | ⚡ BULL_ANY_PPV | 54 | 🔄43 | ↑1.024 | ↑1d | PV | +3.8% | 30.6/29.6 | +3.79% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · W↑1d · 🚀SS · ↑CMF18d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 53 | 🔄69 | ↑1.016 | ↑2d | PV | +3.3% | 5.92/-0.5 | +1.58% | 20% |
| [JWL](https://in.tradingview.com/chart/?symbol=NSE:JWL)<br><sub>📶W9 · W↑12d · 🚀SS·22x · ↑CMF10d · ÷DIV</sub> | ✓ SAFE | Railway wagons and commercial vehicle load bodies manufacturer | ⚡ BULL_ANY_PPV | 49 | 🔄22 | ↑1.114 | ↑1d | PV | +20.0% | -8.77/-12.8 | +20.00% | 20% |
| [KOPRAN](https://in.tradingview.com/chart/?symbol=NSE:KOPRAN)<br><sub>📶W9 · W↑8d · RVOL28x · ↑CMF9d</sub> | ✓ SAFE | APIs and formulations manufacturer serving global pharma | ⚡ BULL_ANY_PPV | 49 | 🔄97 | ↑1.070 | ↑1d | PV | +9.1% | 18.26/10.75 | +9.11% | 20% |
| [CEATLTD](https://in.tradingview.com/chart/?symbol=NSE:CEATLTD)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | Radial and bias tyres for two-wheelers, cars, trucks | ⚡ BULL_ANY_PPV | 37 | 🔄61 | ↑1.019 | ↑18d | PV | +15.9% | 32.84/28.92 | +2.49% | 20% |
| [KOVAI](https://in.tradingview.com/chart/?symbol=NSE:KOVAI)<br><sub>📶W9 · W↑12d · ↑CMF3d</sub> | ⚠ CAUTION | Tertiary hospital network pharmacy education Coimbatore healthcare | ⚡ BULL_ANY_PPV | 11 | ↑50 | ↑1.029 | ↑14d | PV | +13.7% | 57.58/56.55 | +1.09% | 20% |
| [EMAMILTD](https://in.tradingview.com/chart/?symbol=NSE:EMAMILTD)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF25d</sub> | ✓ SAFE | Personal care healthcare FMCG creams balms oils Indian consumers | ⚡ BULL_ANY_PPV | 7 | ↑63 | ↑1.029 | ↑18d | PV | +18.9% | 53.97/53.01 | +2.60% | 20% |
| [PDSL](https://in.tradingview.com/chart/?symbol=NSE:PDSL)<br><sub>📶W9 · W↑18d · ★ · ↑CMF17d</sub> | ✓ SAFE | Apparel sourcing design manufacturing distribution global fashion supply chain | ⚡ BULL_ANY_PPV | 7 | ↑86 | ↑1.023 | ↑18d | PV | +26.7% | 45.26/44.93 | +1.38% | 20% |
| [ISGEC](https://in.tradingview.com/chart/?symbol=NSE:ISGEC)<br><sub>📶W9 · W↑58d · ↑CMF30d</sub> | ⚠ CAUTION | Heavy machinery manufacturing for sugar industrial plants globally | ⚡ BULL_ANY_PPV | 5 | ↑84 | ↑1.028 | ↑22d | PV | +15.2% | 56.55/53.06 | +2.11% | 20% |
| [KALAMANDIR](https://in.tradingview.com/chart/?symbol=NSE:KALAMANDIR)<br><sub>📶W9 · W↑18d · ↑CMF15d</sub> | ✓ SAFE | Ethnic sarees silk apparel retail South India omni-channel | ⚡ BULL_ANY_PPV | 4 | ↑45 | ↑1.095 | ↑16d | PV | +46.0% | 32.18/25.12 | +10.37% | 20% |
| [LTF](https://in.tradingview.com/chart/?symbol=NSE:LTF)<br><sub>📶W9 · W↑12d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | NBFC retail loans construction equipment infrastructure financing | ⚡ BULL_ANY_PPV | 2 | ↑44 | ↑1.030 | ↑18d | PV | +16.2% | 30.59/24.0 | +3.63% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GSPCROP](https://in.tradingview.com/chart/?symbol=NSE:GSPCROP)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Fungicides insecticides pesticides agrochemicals formulation manufacturing | 🔥 BULL_OS_PPV | 54 | 🔄50 | ↑1.023 | ↑1d | PV | +6.1% | -57.39/-63.31 | +6.14% | 20% |
| [MHRIL](https://in.tradingview.com/chart/?symbol=NSE:MHRIL)<br><sub>W↑18d · RVOL40x · ↓CMF25d · ÷DIV</sub> | ✓ SAFE | Vacation ownership memberships family holidays resorts hospitality | ⚡ BULL_ANY_PPV | 59 | 🔄19 | ↑1.003 | ↑1d | PV | +0.8% | 15.76/8.82 | +0.83% | 20% |
| [SUNDROP](https://in.tradingview.com/chart/?symbol=NSE:SUNDROP)<br><sub>↓CMF29d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 59 | 🔄39 | ↑1.008 | ↑1d | PV | +2.9% | -36.96/-37.46 | +2.88% | 20% |
| [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO)<br><sub>🚀SS · ↑CMF10d · 🎯SLING</sub> | ✓ SAFE | Micro-lending NBFC for underbanked rural India income earners | ⚡ BULL_ANY_PPV | 50 | 🔄95 | ↑1.001 | ↓10d | PV | -3.9% | -55.49/-58.73 | +2.27% | 20% |
| [INOXGREEN](https://in.tradingview.com/chart/?symbol=NSE:INOXGREEN)<br><sub>W↑12d · RVOL9x · ↑CMF7d</sub> | ✓ SAFE | Wind turbine operations maintenance services provider India | ⚡ BULL_ANY_PPV | 49 | 🔄3 | ↑1.043 | ↑1d | PV | +9.5% | -32.75/-33.89 | +9.49% | 20% |
| [CANHLIFE](https://in.tradingview.com/chart/?symbol=NSE:CANHLIFE)<br><sub>↑CMF9d</sub> | ⚠ CAUTION | Life insurance through bank distribution channels | ⚡ BULL_ANY_PPV | 49 | 🔄39 | ↑1.040 | ↑1d | PV | +6.8% | -1.3/-4.8 | +6.78% | 20% |
| [TITAGARH](https://in.tradingview.com/chart/?symbol=NSE:TITAGARH)<br><sub>W↑8d · 🚀SS · ↑CMF4d</sub> | ✓ SAFE | Rail wagons coaches metro trains manufacturing | ⚡ BULL_ANY_PPV | 42 | 🔄40 | ↑1.026 | ↑13d | PV | +9.9% | 20.38/17.0 | +3.82% | 20% |
| [YUKEN](https://in.tradingview.com/chart/?symbol=NSE:YUKEN)<br><sub>↓CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 15 | ↓80 | ↑0.988 | ↓10d | PV | -8.1% | -50.07/-52.19 | +4.88% | 20% |
| [ADFFOODS](https://in.tradingview.com/chart/?symbol=NSE:ADFFOODS)<br><sub>🚀SS·22x · ↓CMF20d · 🎯SLING</sub> | ✓ SAFE | Pickles chutneys ready meals export frozen foods | ⚡ BULL_ANY_PPV | 8 | ↓34 | ↑0.972 | ↓17d | PV | -12.5% | -54.43/-55.09 | +2.58% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:DAMCAPITAL,NSE:TORNTPHARM,NSE:JWL,NSE:KOPRAN,NSE:CEATLTD,NSE:KOVAI,NSE:EMAMILTD,NSE:PDSL,NSE:ISGEC,NSE:KALAMANDIR,NSE:LTF,NSE:SIGMAADV,NSE:GSPCROP,NSE:MHRIL,NSE:SUNDROP,NSE:PAISALO,NSE:INOXGREEN,NSE:CANHLIFE,NSE:TITAGARH,NSE:YUKEN,NSE:ADFFOODS
```

### 🟢 OVERSOLD — reversal from −53/−60 (5)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [EVONILE](https://in.tradingview.com/chart/?symbol=NSE:EVONILE)<br><sub>↓CMF0d · ⚠️TRAP</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 13 | ↓50 | ↑0.934 | ↓12d | — | -22.0% | -61.07/-61.82 | -1.19% | 20% |
| [JNKINDIA](https://in.tradingview.com/chart/?symbol=NSE:JNKINDIA)<br><sub>↓CMF21d · 🎯SLING</sub> | ✓ SAFE | EPC contractor, heating equipment, waste gas systems, oil-gas-petrochemical | 🟢 BULL_OVERSOLD | 9 | ↓58 | ↑0.962 | ↓16d | — | -14.9% | -65.99/-66.11 | +0.39% | 20% |
| [THANGAMAYL](https://in.tradingview.com/chart/?symbol=NSE:THANGAMAYL)<br><sub>↓CMF26d · 🎯SLING</sub> | ✓ SAFE | Gold silver diamond jewellery retail Tamil Nadu consumer | 🟢 BULL_OVERSOLD | 5 | ↓29 | ↑0.971 | ↓29d | — | -20.4% | -67.48/-68.01 | +1.87% | 10% 🟩 |
| [MUKANDLTD](https://in.tradingview.com/chart/?symbol=NSE:MUKANDLTD)<br><sub>↓CMF23d · 🎯SLING</sub> | ✓ SAFE | Specialty steel bars, billets, cranes, material handling equipment | 🟡 BULL_OS_L2 | 35 | 🔄58 | ↑0.999 | ↓29d | — | -18.9% | -54.94/-56.91 | +3.02% | 20% |
| [STAR](https://in.tradingview.com/chart/?symbol=NSE:STAR)<br><sub>↑CMF21d · 🎯SLING</sub> | ✓ SAFE | Niche finished dosage pharma formulations global markets | 🟡 BULL_OS_L2 | 5 | ↓56 | ↑0.992 | ↓22d | — | -6.2% | -55.87/-56.02 | +1.54% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:EVONILE,NSE:JNKINDIA,NSE:THANGAMAYL,NSE:MUKANDLTD,NSE:STAR
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (34)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [RAMCOCEM](https://in.tradingview.com/chart/?symbol=NSE:RAMCOCEM)<br><sub>📶W9 · W↑12d · 🚀SS · ↓CMF2d · ÷DIV</sub> | ⚠ CAUTION | Cement producer, RMC, dry mortar for construction | 📈 BULL_ANY_MID | 44 | 🔄31 | ↑1.013 | ↑16d | — | +11.7% | 17.38/16.68 | +2.17% | 20% |
| [YATRA](https://in.tradingview.com/chart/?symbol=NSE:YATRA)<br><sub>📶W9 · W↑8d · 🚀SS · ↑CMF7d</sub> | ✓ SAFE | Online travel bookings for leisure and corporate travelers | 📈 BULL_ANY_MID | 42 | 🔄11 | ↑1.030 | ↑8d | — | +14.8% | 18.75/17.45 | +4.18% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 40 | 🔄54 | ↑1.026 | ↑15d | — | +15.5% | 22.47/18.61 | +2.46% | 20% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>📶W9 · W↑21d · ↑CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 30 | 🔄80 | ↓1.005 | ↑21d | — | +12.4% | 38.62/37.57 | +0.10% | 20% |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE)<br><sub>📶W9 · W↑8d · ↑CMF15d</sub> | ✓ SAFE | Graphite electrodes for electric arc furnace steel making | 📈 BULL_ANY_MID | 27 | ↑80 | ↑1.015 | ↑3d | — | +3.8% | 25.81/22.41 | +0.58% | 20% |
| [STARHEALTH](https://in.tradingview.com/chart/?symbol=NSE:STARHEALTH)<br><sub>📶W9 · W↑12d · ↑CMF0d</sub> | ⚠ CAUTION | Health insurance provider, retail customers, India | 📈 BULL_ANY_MID | 24 | ↑70 | ↑1.013 | ↑6d | — | +3.6% | 23.31/18.46 | +0.86% | 20% |
| [CORONA](https://in.tradingview.com/chart/?symbol=NSE:CORONA)<br><sub>📶W9 · W↑18d · ↓CMF10d</sub> | ✓ SAFE | Pharma formulations women's health cardiology pain management domestic | 📈 BULL_ANY_MID | 17 | ↑50 | ↑1.033 | ↑3d | — | +5.8% | 16.02/13.35 | +3.37% | 20% |
| [RAMCOIND](https://in.tradingview.com/chart/?symbol=NSE:RAMCOIND)<br><sub>📶W9 · W↑12d · 🚀SS · ↑CMF14d</sub> | ⚠ CAUTION | Fiber cement boards, calcium silicate boards, cotton yarn manufacturer | 📈 BULL_ANY_MID | 12 | ↑57 | ↑1.013 | ↑18d | — | +11.5% | 19.97/16.12 | +1.15% | 20% |
| [SBILIFE](https://in.tradingview.com/chart/?symbol=NSE:SBILIFE)<br><sub>📶W9 · W↑16d · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 5 | ↑48 | ↓1.007 | ↑15d | — | +9.1% | 46.12/45.95 | -1.18% | 20% |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>📶W9 · W↑10d · ↑CMF13d</sub> | ✓ SAFE | Residential and commercial real estate development, Mumbai Pune Bangalore | 📈 BULL_ANY_MID | 5 | ↑70 | ↓1.021 | ↑15d | — | +21.6% | 35.54/34.6 | +0.02% | 20% |
| [GLENMARK](https://in.tradingview.com/chart/?symbol=NSE:GLENMARK)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF17d</sub> | ✓ SAFE | Generics, specialty drugs, OTC pharma, global markets | 📈 BULL_ANY_MID | 5 | ↑84 | ↑1.030 | ↑22d | — | +22.2% | 44.5/42.63 | +2.33% | 20% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Generic injectables manufacturer for global regulated markets | 📈 BULL_ANY_MID | 5 | ↑95 | ↑1.018 | ↑21d | — | +13.1% | 46.2/44.84 | +1.55% | 20% |
| [RACLGEAR](https://in.tradingview.com/chart/?symbol=NSE:RACLGEAR)<br><sub>📶W9 · W↑8d · ↑CMF0d</sub> | ✓ SAFE | Precision automotive gears and components for global OEMs | 📈 BULL_ANY_MID | 4 | ↑81 | ↑1.031 | ↑16d | — | +13.4% | 37.61/36.86 | +3.15% | 20% |
| [APOLLOTYRE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOTYRE)<br><sub>📶W9 · W↑12d · ↓CMF30d</sub> | ⚠ CAUTION | Radial tyres for cars trucks farm vehicles | 📈 BULL_ANY_MID | 3 | ↑52 | ↑1.037 | ↑17d | — | +12.2% | 33.7/26.23 | +3.96% | 20% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>📶W9 · W↑30d · ↑CMF22d</sub> | ✓ SAFE | Luxury and midscale hotel brands across Asia Pacific | 📈 BULL_ANY_MID | 0 | ↑89 | ↓1.020 | ↑29d | — | +27.3% | 57.17/56.79 | -0.66% | 20% |
| [AGARWALEYE](https://in.tradingview.com/chart/?symbol=NSE:AGARWALEYE)<br><sub>📶W9 · W↑18d · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION | Eye care surgery and diagnostics across India Africa | 📈 BULL_ANY_MID | 0 | ↑80 | ↑1.046 | ↑23d | — | +21.6% | 52.74/50.67 | +4.65% | 20% |
| [KRN](https://in.tradingview.com/chart/?symbol=NSE:KRN)<br><sub>🚀SS · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Heat exchanger manufacturer HVAC refrigeration OEM supplier | 📈 BULL_ANY_MID | 59 | 🔄29 | ↑1.013 | ↑1d | — | +4.5% | -42.09/-43.96 | +4.52% | 5% 🟥 |
| [SESHAPAPER](https://in.tradingview.com/chart/?symbol=NSE:SESHAPAPER)<br><sub>↑CMF1d</sub> | ⚠ CAUTION | Integrated paper and paperboards manufacturer Tamil Nadu facilities | 📈 BULL_ANY_MID | 59 | 🔄32 | ↑1.001 | ↑1d | — | +0.7% | -18.1/-18.39 | +0.67% | 20% |
| [WELENT](https://in.tradingview.com/chart/?symbol=NSE:WELENT)<br><sub>↓CMF13d</sub> | ✓ SAFE | Infrastructure development roads water pipelines oil gas projects | 📈 BULL_ANY_MID | 56 | 🔄83 | ↑1.007 | ↑4d | — | +2.6% | -1.15/-3.86 | +0.85% | 20% |
| [ARMANFIN](https://in.tradingview.com/chart/?symbol=NSE:ARMANFIN)<br><sub>↑CMF15d</sub> | ✓ SAFE | NBFC loans unorganized sector rural semi-urban India | 📈 BULL_ANY_MID | 54 | 🔄40 | ↑1.023 | ↑1d | — | +4.4% | -6.89/-7.74 | +4.42% | 20% |
| [CARRARO](https://in.tradingview.com/chart/?symbol=NSE:CARRARO)<br><sub>↓CMF20d</sub> | ✓ SAFE | Axles transmissions agricultural tractors construction equipment | 📈 BULL_ANY_MID | 54 | 🔄32 | ↑1.021 | ↑1d | — | +3.3% | -42.6/-48.56 | +3.26% | 20% |
| [VIMTALABS](https://in.tradingview.com/chart/?symbol=NSE:VIMTALABS)<br><sub>↓CMF30d</sub> | ✓ SAFE | Contract research testing pharma biotech chemicals | 📈 BULL_ANY_MID | 47 | 🔄23 | ↑1.003 | ↓13d | — | -2.8% | -49.47/-51.01 | +2.57% | 20% |
| [LXCHEM](https://in.tradingview.com/chart/?symbol=NSE:LXCHEM)<br><sub>🚀SS · ↓CMF25d</sub> | ✓ SAFE | Acetyl intermediates and specialty chemicals manufacturer for pharma | 📈 BULL_ANY_MID | 45 | 🔄49 | ↑1.003 | ↓15d | — | -4.8% | -41.98/-41.98 | +3.55% | 20% |
| [GODIGIT](https://in.tradingview.com/chart/?symbol=NSE:GODIGIT)<br><sub>🚀SS · ↓CMF10d</sub> | ⚠ CAUTION | Digital-first general insurance, motor and health focused | 📈 BULL_ANY_MID | 40 | 🔄18 | ↑1.001 | ↓45d | — | -0.4% | -50.39/-52.98 | +3.00% | 20% |
| [GREENPLY](https://in.tradingview.com/chart/?symbol=NSE:GREENPLY)<br><sub>↓CMF18d · ÷DIV</sub> | ✓ SAFE | Plywood MDF doors flooring for residential commercial construction | 📈 BULL_ANY_MID | 40 | 🔄58 | ↑1.001 | ↓20d | — | -8.8% | -34.53/-34.77 | +1.18% | 20% |
| [BANSALWIRE](https://in.tradingview.com/chart/?symbol=NSE:BANSALWIRE)<br><sub>🚀SS · ↓CMF13d · ÷DIV</sub> | ⚠ CAUTION | Steel and stainless steel wire manufacturer India | 📈 BULL_ANY_MID | 24 | ↓0 | ↑0.973 | ↑1d | — | +2.0% | -31.43/-32.16 | +1.99% | 20% |
| [SIEMENS](https://in.tradingview.com/chart/?symbol=NSE:SIEMENS)<br><sub>W↑6d · 🚀SS · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 17 | ↓53 | ↓1.000 | ↑3d | — | +1.6% | 7.11/5.62 | -0.13% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>W↑6d · ↑CMF13d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 15 | ↓57 | ↓0.994 | ↑5d | — | +0.7% | 11.94/10.94 | -1.15% | 20% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>W↑3d · ↓CMF30d</sub> | ✓ SAFE | Microfinance bank serving low-income retail borrowers India | 📈 BULL_ANY_MID | 15 | ↑55 | ↑1.006 | ↑15d | — | +7.1% | 13.57/10.31 | +0.41% | -% |
| [CUMMINSIND](https://in.tradingview.com/chart/?symbol=NSE:CUMMINSIND)<br><sub>↑CMF11d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 13 | ↓20 | ↓0.975 | ↓7d | — | -4.8% | -50.37/-50.64 | -1.15% | 20% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>🚀SS · ↓CMF28d</sub> | ✓ SAFE | Refurbished laptops desktops electronics retail distribution | 📈 BULL_ANY_MID | 9 | ↓70 | ↑0.944 | ↓16d | — | -28.6% | -50.75/-50.95 | +1.17% | 20% 🟦 |
| [ANDHRSUGAR](https://in.tradingview.com/chart/?symbol=NSE:ANDHRSUGAR)<br><sub>🚀SS · ↑CMF8d</sub> | ✓ SAFE | Sugar, industrial chemicals, fertilizers manufacturing and alcohol | 📈 BULL_ANY_MID | 9 | ↓36 | ↑0.983 | ↓16d | — | -5.9% | -51.56/-51.64 | +0.33% | 20% |
| [JUNIPER](https://in.tradingview.com/chart/?symbol=NSE:JUNIPER)<br><sub>↓CMF0d · ⚠️TRAP</sub> | ⚠ CAUTION | Luxury hotel ownership management Hyatt partnership India portfolio | 📈 BULL_ANY_MID | 5 | ↓37 | ↓0.988 | ↓15d | — | -3.1% | -36.1/-36.55 | -1.12% | 20% |
| [RPGLIFE](https://in.tradingview.com/chart/?symbol=NSE:RPGLIFE)<br><sub>🚀SS · ↑CMF30d</sub> | ✓ SAFE | Pharmaceutical formulations and APIs for domestic international markets | 📈 BULL_ANY_MID | 5 | ↓73 | ↑0.998 | ↓22d | — | -7.8% | -41.41/-41.58 | +1.48% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:RAMCOCEM,NSE:YATRA,NSE:SHRIRAMFIN,NSE:ADANIPORTS,NSE:GRAPHITE,NSE:STARHEALTH,NSE:CORONA,NSE:RAMCOIND,NSE:SBILIFE,NSE:LODHA,NSE:GLENMARK,NSE:GLAND,NSE:RACLGEAR,NSE:APOLLOTYRE,NSE:INDHOTEL,NSE:AGARWALEYE,NSE:KRN,NSE:SESHAPAPER,NSE:WELENT,NSE:ARMANFIN,NSE:CARRARO,NSE:VIMTALABS,NSE:LXCHEM,NSE:GODIGIT,NSE:GREENPLY,NSE:BANSALWIRE,NSE:SIEMENS,NSE:ADANIENT,NSE:UJJIVANSFB,NSE:CUMMINSIND,NSE:EBGNG,NSE:ANDHRSUGAR,NSE:JUNIPER,NSE:RPGLIFE
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
