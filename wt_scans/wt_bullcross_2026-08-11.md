> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-08-11
*Generated 2026-08-11 15:44 IST*

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

**Total bull crosses today: 67** · 26 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:KAJARIACER,NSE:MRPL,NSE:WINDLAS,NSE:YATRA,NSE:OIL,NSE:PICCADIL,NSE:CHENNPETRO,NSE:ARE&M,NSE:UNICHEMLAB,NSE:GANDHITUBE,NSE:TCPLPACK,NSE:NAUKRI,NSE:IRISDOREME,NSE:SHRIPISTON,NSE:EPL,NSE:BLUSPRING,NSE:SILVERTUC,NSE:HESTERBIO,NSE:NEWGEN,NSE:OFSS,NSE:INDOTECH,NSE:LANDMARK,NSE:SENCO,NSE:MOBIKWIK,NSE:COSMOFIRST,NSE:TINNARUBR,NSE:NESTLEIND,NSE:NEPHROPLUS,NSE:LENSKART,NSE:CYIENTDLM,NSE:DEEDEV,NSE:KSCL,NSE:SCHAEFFLER,NSE:VIKRAN,NSE:GRMOVER,NSE:FUSION,NSE:TEJASNET,NSE:GODAVARIB,NSE:KCP,NSE:KSB,NSE:SAFARI,NSE:VBL,NSE:GODREJCP,NSE:VMM,NSE:FIRSTCRY,NSE:ACCELYA,NSE:CDSL,NSE:HDBFS,NSE:DELHIVERY,NSE:SIGNATURE,NSE:ABDL,NSE:LGBBROSLTD,NSE:SAGCEM,NSE:FEDFINA,NSE:MAYURUNIQ,NSE:INDOSTAR,NSE:SKMEGGPROD,NSE:BALAMINES,NSE:EPIGRAL,NSE:ADFFOODS,NSE:ADANIPORTS,NSE:ONESOURCE,NSE:BORORENEW,NSE:JINDALPOLY,NSE:CIEINDIA,NSE:NINSYS,NSE:NORTHARC
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (31)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [KAJARIACER](https://in.tradingview.com/chart/?symbol=NSE:KAJARIACER)<br><sub>📶W9 · 🚀SS · ↓CMF10d</sub> | ✓ SAFE | Ceramic and vitrified tiles manufacturer for construction | ⚡ BULL_ANY_PPV | 94 | 🔄66 | ↑1.023 | ↑1d | SQ·PV | +3.5% | -26.48/-31.35 | +3.45% | 20% |
| [MRPL](https://in.tradingview.com/chart/?symbol=NSE:MRPL)<br><sub>📶W9 · W↑22d · ↑CMF18d · DEL45%(T-1)</sub> | ✓ SAFE | Crude oil refining, petrochemicals production, domestic fuel supply | ⚡ BULL_ANY_PPV | 89 | 🔄71 | ↑1.066 | ↑1d | SQ·PV | +11.2% | 17.17/16.06 | +11.16% | 20% |
| [WINDLAS](https://in.tradingview.com/chart/?symbol=NSE:WINDLAS)<br><sub>📶W9 · W↑52d · RVOL55x · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Pharma CDMO oral solids liquid formulations contract manufacturing | ⚡ BULL_ANY_PPV | 89 | 🔄64 | ↑1.077 | ↑1d | SQ·PV | +12.3% | 42.73/36.2 | +12.32% | 20% |
| [YATRA](https://in.tradingview.com/chart/?symbol=NSE:YATRA)<br><sub>📶W9 · W↑2d · RVOL12x · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Online travel agency for flights hotels bookings | ⚡ BULL_ANY_PPV | 89 | 🔄47 | ↑1.050 | ↑1d | SQ·PV | +9.4% | -11.93/-13.22 | +9.36% | 20% |
| [OIL](https://in.tradingview.com/chart/?symbol=NSE:OIL)<br><sub>📶W9 · W↑17d · 🚀SS · ↑CMF24d</sub> | ✓ SAFE | Crude oil and natural gas exploration production transportation | ⚡ BULL_ANY_PPV | 58 | ↑38 | ↑1.040 | ↑2d | SQ·PV | +6.2% | 39.29/28.0 | +3.83% | 20% |
| [PICCADIL](https://in.tradingview.com/chart/?symbol=NSE:PICCADIL)<br><sub>📶W9 · W↑32d · ↓CMF1d</sub> | ✓ SAFE | Sugar production and premium spirits for Indian consumers | ⚡ BULL_ANY_PPV | 52 | ↑79 | ↑1.030 | ↑8d | SQ·PV | +8.2% | 47.29/43.11 | +1.23% | 20% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>📶W9 · W↑22d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Crude oil refining, petroleum products, lubricant additives | ⚡ BULL_ANY_PPV | 49 | 🔄93 | ↑1.102 | ↑1d | PV | +15.0% | 45.49/43.76 | +15.00% | 20% |
| [ARE&M](https://in.tradingview.com/chart/?symbol=NSE:ARE&M)<br><sub>📶W9 · W↑85d · 🚀SS·9x · ↑CMF0d</sub> | ✓ SAFE | Lead-acid batteries automotive industrial energy storage | ⚡ BULL_ANY_PPV | 49 | 🔄58 | ↑1.051 | ↑1d | PV | +8.1% | 44.07/43.44 | +8.08% | 20% |
| [UNICHEMLAB](https://in.tradingview.com/chart/?symbol=NSE:UNICHEMLAB)<br><sub>📶W9 · RVOL27x · ↑CMF0d</sub> | ✓ SAFE | Pharma generics APIs contract manufacturing CMO | ⚡ BULL_ANY_PPV | 49 | 🔄85 | ↑1.099 | ↑1d | PV | +13.1% | -13.33/-20.93 | +13.14% | 20% |
| [GANDHITUBE](https://in.tradingview.com/chart/?symbol=NSE:GANDHITUBE)<br><sub>📶W9 · W↑27d · 🚀SS·11x · ↑CMF0d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 30 | 🔄64 | ↑1.043 | ↑22d | PV | +8.9% | 73.64/67.54 | +5.58% | 20% |
| [TCPLPACK](https://in.tradingview.com/chart/?symbol=NSE:TCPLPACK)<br><sub>📶W9 · W↑42d · RVOL9x · ↑CMF11d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 18 | ↑80 | ↑1.118 | ↑2d | PV | +16.7% | 33.18/16.0 | +11.38% | 20% |
| [NAUKRI](https://in.tradingview.com/chart/?symbol=NSE:NAUKRI)<br><sub>📶W9 · W↑97d · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Job portal, real estate classifieds, matrimonial matchmaking platform | ⚡ BULL_ANY_PPV | 0 | ↑75 | ↑1.077 | ↑30d | PV | +40.1% | 60.32/51.8 | +6.08% | 20% |
| [IRISDOREME](https://in.tradingview.com/chart/?symbol=NSE:IRISDOREME)<br><sub>📶W9 · W↑85d · 🚀SS · ★ · ↑CMF30d · DEL68%(T-1)</sub> | ✓ SAFE | Infant children apparel manufacturer integrated production India | ⚡ BULL_ANY_PPV | 0 | ↑94 | ↓1.056 | ↑39d | PV | +56.9% | 74.15/73.89 | +0.99% | 20% |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Pistons rings valves engine components automotive OEMs exporters | 📈 BULL_ANY_MID | 97 | 🔄91 | ↑1.008 | ↑3d | SQ | +2.2% | 48.82/48.64 | +0.19% | 20% |
| [EPL](https://in.tradingview.com/chart/?symbol=NSE:EPL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Laminated plastic tubes for cosmetics pharma food | 📈 BULL_ANY_MID | 94 | 🔄60 | ↑1.023 | ↑1d | SQ | +3.0% | -22.47/-29.7 | +2.97% | 20% |
| [BLUSPRING](https://in.tradingview.com/chart/?symbol=NSE:BLUSPRING)<br><sub>📶W9 · 🚀SS · ↓CMF2d</sub> | ✓ SAFE | Infrastructure services management operations facilities | 📈 BULL_ANY_MID | 89 | 🔄95 | ↑1.035 | ↑1d | SQ | +4.9% | 27.61/24.92 | +4.89% | 10% 🟨 |
| [SILVERTUC](https://in.tradingview.com/chart/?symbol=NSE:SILVERTUC)<br><sub>📶W9 · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | IT services digital transformation e-governance software development | 📈 BULL_ANY_MID | 58 | ↑98 | ↑1.035 | ↑2d | SQ | +5.4% | 26.2/19.44 | +1.64% | 20% |
| [HESTERBIO](https://in.tradingview.com/chart/?symbol=NSE:HESTERBIO)<br><sub>📶W9 · W↑85d · ↓CMF1d</sub> | ✓ SAFE | Poultry livestock vaccines manufacturer animal healthcare sector | 📈 BULL_ANY_MID | 58 | ↑88 | ↓1.011 | ↑2d | SQ | +2.9% | 31.11/27.46 | -0.24% | 20% |
| [NEWGEN](https://in.tradingview.com/chart/?symbol=NSE:NEWGEN)<br><sub>📶W9 · W↑52d · ↓CMF1d · DEL33%(T-1)</sub> | ✓ SAFE | Digital transformation platform: automation, content, communication, low-code | 📈 BULL_ANY_MID | 57 | ↓21 | ↓1.007 | ↑3d | SQ | +2.3% | 34.96/33.95 | -1.44% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄83 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [INDOTECH](https://in.tradingview.com/chart/?symbol=NSE:INDOTECH)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | Power distribution transformers utility industrial renewable energy | 📈 BULL_ANY_MID | 49 | 🔄99 | ↑1.334 | ↑1d | — | +50.8% | 56.69/49.57 | +50.82% | 5% 🟥 |
| [LANDMARK](https://in.tradingview.com/chart/?symbol=NSE:LANDMARK)<br><sub>📶W9 · W↑52d · ↓CMF19d · DEL47%(T-1)</sub> | ✓ SAFE | Premium auto retail, luxury and mass-market vehicles, India | 📈 BULL_ANY_MID | 40 | ↑81 | ↑1.047 | ↑21d | SQ | +35.2% | 52.83/49.78 | +1.85% | 20% |
| [SENCO](https://in.tradingview.com/chart/?symbol=NSE:SENCO)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | Gold diamond silver jewelry retail Eastern India focus | 📈 BULL_ANY_MID | 28 | ↑70 | ↑1.015 | ↑2d | — | +3.2% | 34.64/33.4 | +0.60% | 20% |
| [MOBIKWIK](https://in.tradingview.com/chart/?symbol=NSE:MOBIKWIK)<br><sub>📶W9 · W↑2d · ↓CMF2d</sub> | ✓ SAFE | Digital wallet and payments for consumers merchants | 📈 BULL_ANY_MID | 23 | ↑39 | ↑1.028 | ↑2d | — | +5.9% | -0.59/-5.71 | +2.67% | 20% |
| [COSMOFIRST](https://in.tradingview.com/chart/?symbol=NSE:COSMOFIRST)<br><sub>📶W9 · W↑85d · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | Specialty films for packaging, lamination, labeling applications | 📈 BULL_ANY_MID | 17 | ↑69 | ↓1.030 | ↑3d | — | +6.7% | 61.86/59.65 | +0.34% | 20% |
| [TINNARUBR](https://in.tradingview.com/chart/?symbol=NSE:TINNARUBR)<br><sub>📶W9 · W↑90d · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Waste tyre recycling into rubber crumb and steel products | 📈 BULL_ANY_MID | 17 | ↑88 | ↑1.024 | ↑8d | — | +9.1% | 47.05/46.01 | +1.47% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 11 | ↑68 | ↓1.011 | ↑9d | — | +5.3% | 52.94/52.13 | +0.00% | 20% |
| [NEPHROPLUS](https://in.tradingview.com/chart/?symbol=NSE:NEPHROPLUS)<br><sub>📶W9 · ↑CMF11d</sub> | ✓ SAFE | Dialysis center chain serving kidney disease patients India | 📈 BULL_ANY_MID | 10 | ↑50 | ↑1.030 | ↑15d | — | +13.3% | 34.27/30.79 | +2.44% | 20% |
| [LENSKART](https://in.tradingview.com/chart/?symbol=NSE:LENSKART)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Eyewear design manufacturing retail omnichannel direct consumer | 📈 BULL_ANY_MID | 5 | ↑50 | ↑1.030 | ↑30d | — | +15.9% | 64.3/61.91 | +2.24% | 20% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>📶W9 · W↑102d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Electronics manufacturing design integration testing subsystems defense aerospace | 📈 BULL_ANY_MID | 0 | ↑95 | ↑1.048 | ↑29d | — | +52.7% | 57.62/55.4 | +2.53% | 20% |
| [DEEDEV](https://in.tradingview.com/chart/?symbol=NSE:DEEDEV)<br><sub>📶W9 · W↑65d · 🚀SS · ↑CMF23d</sub> | ✓ SAFE | Process piping systems oil gas power thermal | 📈 BULL_ANY_MID | 0 | ↑99 | ↑1.243 | ↑31d | — | +131.8% | 73.24/67.09 | +30.83% | 5% 🟥 |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:KAJARIACER,NSE:MRPL,NSE:WINDLAS,NSE:YATRA,NSE:OIL,NSE:PICCADIL,NSE:CHENNPETRO,NSE:ARE&M,NSE:UNICHEMLAB,NSE:GANDHITUBE,NSE:TCPLPACK,NSE:NAUKRI,NSE:IRISDOREME,NSE:SHRIPISTON,NSE:EPL,NSE:BLUSPRING,NSE:SILVERTUC,NSE:HESTERBIO,NSE:NEWGEN,NSE:OFSS,NSE:INDOTECH,NSE:LANDMARK,NSE:SENCO,NSE:MOBIKWIK,NSE:COSMOFIRST,NSE:TINNARUBR,NSE:NESTLEIND,NSE:NEPHROPLUS,NSE:LENSKART,NSE:CYIENTDLM,NSE:DEEDEV
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (44)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [KAJARIACER](https://in.tradingview.com/chart/?symbol=NSE:KAJARIACER)<br><sub>📶W9 · 🚀SS · ↓CMF10d</sub> | ✓ SAFE | Ceramic and vitrified tiles manufacturer for construction | ⚡ BULL_ANY_PPV | 94 | 🔄66 | ↑1.023 | ↑1d | SQ·PV | +3.5% | -26.48/-31.35 | +3.45% | 20% |
| [MRPL](https://in.tradingview.com/chart/?symbol=NSE:MRPL)<br><sub>📶W9 · W↑22d · ↑CMF18d · DEL45%(T-1)</sub> | ✓ SAFE | Crude oil refining, petrochemicals production, domestic fuel supply | ⚡ BULL_ANY_PPV | 89 | 🔄71 | ↑1.066 | ↑1d | SQ·PV | +11.2% | 17.17/16.06 | +11.16% | 20% |
| [WINDLAS](https://in.tradingview.com/chart/?symbol=NSE:WINDLAS)<br><sub>📶W9 · W↑52d · RVOL55x · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Pharma CDMO oral solids liquid formulations contract manufacturing | ⚡ BULL_ANY_PPV | 89 | 🔄64 | ↑1.077 | ↑1d | SQ·PV | +12.3% | 42.73/36.2 | +12.32% | 20% |
| [YATRA](https://in.tradingview.com/chart/?symbol=NSE:YATRA)<br><sub>📶W9 · W↑2d · RVOL12x · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Online travel agency for flights hotels bookings | ⚡ BULL_ANY_PPV | 89 | 🔄47 | ↑1.050 | ↑1d | SQ·PV | +9.4% | -11.93/-13.22 | +9.36% | 20% |
| [OIL](https://in.tradingview.com/chart/?symbol=NSE:OIL)<br><sub>📶W9 · W↑17d · 🚀SS · ↑CMF24d</sub> | ✓ SAFE | Crude oil and natural gas exploration production transportation | ⚡ BULL_ANY_PPV | 58 | ↑38 | ↑1.040 | ↑2d | SQ·PV | +6.2% | 39.29/28.0 | +3.83% | 20% |
| [PICCADIL](https://in.tradingview.com/chart/?symbol=NSE:PICCADIL)<br><sub>📶W9 · W↑32d · ↓CMF1d</sub> | ✓ SAFE | Sugar production and premium spirits for Indian consumers | ⚡ BULL_ANY_PPV | 52 | ↑79 | ↑1.030 | ↑8d | SQ·PV | +8.2% | 47.29/43.11 | +1.23% | 20% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>📶W9 · W↑22d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Crude oil refining, petroleum products, lubricant additives | ⚡ BULL_ANY_PPV | 49 | 🔄93 | ↑1.102 | ↑1d | PV | +15.0% | 45.49/43.76 | +15.00% | 20% |
| [ARE&M](https://in.tradingview.com/chart/?symbol=NSE:ARE&M)<br><sub>📶W9 · W↑85d · 🚀SS·9x · ↑CMF0d</sub> | ✓ SAFE | Lead-acid batteries automotive industrial energy storage | ⚡ BULL_ANY_PPV | 49 | 🔄58 | ↑1.051 | ↑1d | PV | +8.1% | 44.07/43.44 | +8.08% | 20% |
| [UNICHEMLAB](https://in.tradingview.com/chart/?symbol=NSE:UNICHEMLAB)<br><sub>📶W9 · RVOL27x · ↑CMF0d</sub> | ✓ SAFE | Pharma generics APIs contract manufacturing CMO | ⚡ BULL_ANY_PPV | 49 | 🔄85 | ↑1.099 | ↑1d | PV | +13.1% | -13.33/-20.93 | +13.14% | 20% |
| [GANDHITUBE](https://in.tradingview.com/chart/?symbol=NSE:GANDHITUBE)<br><sub>📶W9 · W↑27d · 🚀SS·11x · ↑CMF0d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 30 | 🔄64 | ↑1.043 | ↑22d | PV | +8.9% | 73.64/67.54 | +5.58% | 20% |
| [TCPLPACK](https://in.tradingview.com/chart/?symbol=NSE:TCPLPACK)<br><sub>📶W9 · W↑42d · RVOL9x · ↑CMF11d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 18 | ↑80 | ↑1.118 | ↑2d | PV | +16.7% | 33.18/16.0 | +11.38% | 20% |
| [NAUKRI](https://in.tradingview.com/chart/?symbol=NSE:NAUKRI)<br><sub>📶W9 · W↑97d · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Job portal, real estate classifieds, matrimonial matchmaking platform | ⚡ BULL_ANY_PPV | 0 | ↑75 | ↑1.077 | ↑30d | PV | +40.1% | 60.32/51.8 | +6.08% | 20% |
| [IRISDOREME](https://in.tradingview.com/chart/?symbol=NSE:IRISDOREME)<br><sub>📶W9 · W↑85d · 🚀SS · ★ · ↑CMF30d · DEL68%(T-1)</sub> | ✓ SAFE | Infant children apparel manufacturer integrated production India | ⚡ BULL_ANY_PPV | 0 | ↑94 | ↓1.056 | ↑39d | PV | +56.9% | 74.15/73.89 | +0.99% | 20% |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Pistons rings valves engine components automotive OEMs exporters | 📈 BULL_ANY_MID | 97 | 🔄91 | ↑1.008 | ↑3d | SQ | +2.2% | 48.82/48.64 | +0.19% | 20% |
| [EPL](https://in.tradingview.com/chart/?symbol=NSE:EPL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Laminated plastic tubes for cosmetics pharma food | 📈 BULL_ANY_MID | 94 | 🔄60 | ↑1.023 | ↑1d | SQ | +3.0% | -22.47/-29.7 | +2.97% | 20% |
| [BLUSPRING](https://in.tradingview.com/chart/?symbol=NSE:BLUSPRING)<br><sub>📶W9 · 🚀SS · ↓CMF2d</sub> | ✓ SAFE | Infrastructure services management operations facilities | 📈 BULL_ANY_MID | 89 | 🔄95 | ↑1.035 | ↑1d | SQ | +4.9% | 27.61/24.92 | +4.89% | 10% 🟨 |
| [SILVERTUC](https://in.tradingview.com/chart/?symbol=NSE:SILVERTUC)<br><sub>📶W9 · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | IT services digital transformation e-governance software development | 📈 BULL_ANY_MID | 58 | ↑98 | ↑1.035 | ↑2d | SQ | +5.4% | 26.2/19.44 | +1.64% | 20% |
| [HESTERBIO](https://in.tradingview.com/chart/?symbol=NSE:HESTERBIO)<br><sub>📶W9 · W↑85d · ↓CMF1d</sub> | ✓ SAFE | Poultry livestock vaccines manufacturer animal healthcare sector | 📈 BULL_ANY_MID | 58 | ↑88 | ↓1.011 | ↑2d | SQ | +2.9% | 31.11/27.46 | -0.24% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄83 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [INDOTECH](https://in.tradingview.com/chart/?symbol=NSE:INDOTECH)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | Power distribution transformers utility industrial renewable energy | 📈 BULL_ANY_MID | 49 | 🔄99 | ↑1.334 | ↑1d | — | +50.8% | 56.69/49.57 | +50.82% | 5% 🟥 |
| [LANDMARK](https://in.tradingview.com/chart/?symbol=NSE:LANDMARK)<br><sub>📶W9 · W↑52d · ↓CMF19d · DEL47%(T-1)</sub> | ✓ SAFE | Premium auto retail, luxury and mass-market vehicles, India | 📈 BULL_ANY_MID | 40 | ↑81 | ↑1.047 | ↑21d | SQ | +35.2% | 52.83/49.78 | +1.85% | 20% |
| [SENCO](https://in.tradingview.com/chart/?symbol=NSE:SENCO)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | Gold diamond silver jewelry retail Eastern India focus | 📈 BULL_ANY_MID | 28 | ↑70 | ↑1.015 | ↑2d | — | +3.2% | 34.64/33.4 | +0.60% | 20% |
| [MOBIKWIK](https://in.tradingview.com/chart/?symbol=NSE:MOBIKWIK)<br><sub>📶W9 · W↑2d · ↓CMF2d</sub> | ✓ SAFE | Digital wallet and payments for consumers merchants | 📈 BULL_ANY_MID | 23 | ↑39 | ↑1.028 | ↑2d | — | +5.9% | -0.59/-5.71 | +2.67% | 20% |
| [COSMOFIRST](https://in.tradingview.com/chart/?symbol=NSE:COSMOFIRST)<br><sub>📶W9 · W↑85d · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | Specialty films for packaging, lamination, labeling applications | 📈 BULL_ANY_MID | 17 | ↑69 | ↓1.030 | ↑3d | — | +6.7% | 61.86/59.65 | +0.34% | 20% |
| [TINNARUBR](https://in.tradingview.com/chart/?symbol=NSE:TINNARUBR)<br><sub>📶W9 · W↑90d · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Waste tyre recycling into rubber crumb and steel products | 📈 BULL_ANY_MID | 17 | ↑88 | ↑1.024 | ↑8d | — | +9.1% | 47.05/46.01 | +1.47% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 11 | ↑68 | ↓1.011 | ↑9d | — | +5.3% | 52.94/52.13 | +0.00% | 20% |
| [NEPHROPLUS](https://in.tradingview.com/chart/?symbol=NSE:NEPHROPLUS)<br><sub>📶W9 · ↑CMF11d</sub> | ✓ SAFE | Dialysis center chain serving kidney disease patients India | 📈 BULL_ANY_MID | 10 | ↑50 | ↑1.030 | ↑15d | — | +13.3% | 34.27/30.79 | +2.44% | 20% |
| [LENSKART](https://in.tradingview.com/chart/?symbol=NSE:LENSKART)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Eyewear design manufacturing retail omnichannel direct consumer | 📈 BULL_ANY_MID | 5 | ↑50 | ↑1.030 | ↑30d | — | +15.9% | 64.3/61.91 | +2.24% | 20% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>📶W9 · W↑102d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Electronics manufacturing design integration testing subsystems defense aerospace | 📈 BULL_ANY_MID | 0 | ↑95 | ↑1.048 | ↑29d | — | +52.7% | 57.62/55.4 | +2.53% | 20% |
| [DEEDEV](https://in.tradingview.com/chart/?symbol=NSE:DEEDEV)<br><sub>📶W9 · W↑65d · 🚀SS · ↑CMF23d</sub> | ✓ SAFE | Process piping systems oil gas power thermal | 📈 BULL_ANY_MID | 0 | ↑99 | ↑1.243 | ↑31d | — | +131.8% | 73.24/67.09 | +30.83% | 5% 🟥 |
| [KSCL](https://in.tradingview.com/chart/?symbol=NSE:KSCL)<br><sub>↓CMF16d · 🎯SLING</sub> | ✓ SAFE | Hybrid seed research, production, field crops, vegetables | 🔥 BULL_OS_PPV | 59 | 🔄10 | ↑1.014 | ↑1d | PV | +4.7% | -59.37/-63.11 | +4.68% | 20% |
| [SCHAEFFLER](https://in.tradingview.com/chart/?symbol=NSE:SCHAEFFLER)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Precision bearings transmission components automotive industrial manufacturing | ⚡ BULL_ANY_PPV | 94 | 🔄45 | ↑1.015 | ↑1d | SQ·PV | +2.2% | -21.08/-28.58 | +2.17% | 20% |
| [VIKRAN](https://in.tradingview.com/chart/?symbol=NSE:VIKRAN)<br><sub>W↑2d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Power transmission towers and infrastructure EPC projects | ⚡ BULL_ANY_PPV | 93 | 🔄50 | ↑1.017 | ↑2d | SQ·PV | +2.9% | -2.12/-10.33 | +1.57% | 20% |
| [GRMOVER](https://in.tradingview.com/chart/?symbol=NSE:GRMOVER)<br><sub>W↑2d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Basmati rice milling processing exports domestic international markets | ⚡ BULL_ANY_PPV | 82 | 🔄1 | ↑1.031 | ↑8d | SQ·PV | +6.9% | -13.34/-20.55 | +4.02% | 10% 🟨 |
| [FUSION](https://in.tradingview.com/chart/?symbol=NSE:FUSION)<br><sub>🚀SS · ↓CMF8d</sub> | ✓ SAFE | Microfinance loans for rural women entrepreneurs | ⚡ BULL_ANY_PPV | 56 | 🔄68 | ↑1.008 | ↓4d | PV | +1.1% | -15.4/-18.8 | +2.89% | 20% |
| [TEJASNET](https://in.tradingview.com/chart/?symbol=NSE:TEJASNET)<br><sub>🚀SS · ↓CMF23d</sub> | ✓ SAFE | Optical wireless networking products telecom service providers infrastructure | ⚡ BULL_ANY_PPV | 54 | 🔄70 | ↑1.020 | ↑1d | PV | +2.3% | -11.44/-18.99 | +2.32% | 20% 🟦 |
| [GODAVARIB](https://in.tradingview.com/chart/?symbol=NSE:GODAVARIB)<br><sub>🚀SS·81x · ↑CMF0d</sub> | ✓ SAFE | Sugarcane biorefinery making chemicals ethanol power and sugar | ⚡ BULL_ANY_PPV | 49 | 🔄29 | ↑1.051 | ↑1d | PV | +13.9% | -44.31/-44.74 | +13.95% | 20% |
| [GODREJCP](https://in.tradingview.com/chart/?symbol=NSE:GODREJCP)<br><sub>W↑33d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 98 | 🔄37 | ↑1.008 | ↑2d | SQ | +2.1% | 25.85/25.42 | +1.03% | 20% |
| [CDSL](https://in.tradingview.com/chart/?symbol=NSE:CDSL)<br><sub>↓CMF2d</sub> | ✓ SAFE | Electronic securities holding settlement infrastructure depository | 📈 BULL_ANY_MID | 59 | 🔄39 | ↑1.007 | ↑1d | — | +1.1% | -18.22/-19.72 | +1.09% | 20% |
| [HDBFS](https://in.tradingview.com/chart/?symbol=NSE:HDBFS)<br><sub>↓CMF17d</sub> | ⚠ CAUTION | Auto loans and two-wheeler financing for underbanked customers | 📈 BULL_ANY_MID | 59 | 🔄36 | ↑1.014 | ↑1d | — | +2.5% | -37.11/-40.33 | +2.47% | 20% |
| [FEDFINA](https://in.tradingview.com/chart/?symbol=NSE:FEDFINA)<br><sub>↓CMF30d</sub> | ✓ SAFE | MSME gold loans and business credit NBFC | 📈 BULL_ANY_MID | 54 | 🔄56 | ↑1.018 | ↑1d | — | +3.2% | -24.91/-28.84 | +3.16% | 20% |
| [INDOSTAR](https://in.tradingview.com/chart/?symbol=NSE:INDOSTAR)<br><sub>🚀SS · ↓CMF14d</sub> | ✓ SAFE | NBFC lending commercial vehicles SME infrastructure | 📈 BULL_ANY_MID | 48 | 🔄58 | ↑1.013 | ↓12d | — | -4.6% | -26.14/-27.87 | +2.66% | 20% |
| [SKMEGGPROD](https://in.tradingview.com/chart/?symbol=NSE:SKMEGGPROD)<br><sub>🚀SS · ↓CMF9d</sub> | ✓ SAFE | Egg powder processing and export, poultry sector | 📈 BULL_ANY_MID | 41 | 🔄88 | ↑1.028 | ↓14d | — | -16.4% | -34.94/-39.02 | +5.12% | 20% |
| [BALAMINES](https://in.tradingview.com/chart/?symbol=NSE:BALAMINES)<br><sub>🚀SS · ↓CMF6d</sub> | ✓ SAFE | Aliphatic amines specialty chemicals manufacturer for industrial applications | 📈 BULL_ANY_MID | 40 | 🔄89 | ↑1.009 | ↓25d | — | +2.7% | -31.71/-33.06 | +3.79% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:KAJARIACER,NSE:MRPL,NSE:WINDLAS,NSE:YATRA,NSE:OIL,NSE:PICCADIL,NSE:CHENNPETRO,NSE:ARE&M,NSE:UNICHEMLAB,NSE:GANDHITUBE,NSE:TCPLPACK,NSE:NAUKRI,NSE:IRISDOREME,NSE:SHRIPISTON,NSE:EPL,NSE:BLUSPRING,NSE:SILVERTUC,NSE:HESTERBIO,NSE:OFSS,NSE:INDOTECH,NSE:LANDMARK,NSE:SENCO,NSE:MOBIKWIK,NSE:COSMOFIRST,NSE:TINNARUBR,NSE:NESTLEIND,NSE:NEPHROPLUS,NSE:LENSKART,NSE:CYIENTDLM,NSE:DEEDEV,NSE:KSCL,NSE:SCHAEFFLER,NSE:VIKRAN,NSE:GRMOVER,NSE:FUSION,NSE:TEJASNET,NSE:GODAVARIB,NSE:GODREJCP,NSE:CDSL,NSE:HDBFS,NSE:FEDFINA,NSE:INDOSTAR,NSE:SKMEGGPROD,NSE:BALAMINES
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (26)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [KAJARIACER](https://in.tradingview.com/chart/?symbol=NSE:KAJARIACER)<br><sub>📶W9 · 🚀SS · ↓CMF10d</sub> | ✓ SAFE | Ceramic and vitrified tiles manufacturer for construction | ⚡ BULL_ANY_PPV | 94 | 🔄66 | ↑1.023 | ↑1d | SQ·PV | +3.5% | -26.48/-31.35 | +3.45% | 20% |
| [MRPL](https://in.tradingview.com/chart/?symbol=NSE:MRPL)<br><sub>📶W9 · W↑22d · ↑CMF18d · DEL45%(T-1)</sub> | ✓ SAFE | Crude oil refining, petrochemicals production, domestic fuel supply | ⚡ BULL_ANY_PPV | 89 | 🔄71 | ↑1.066 | ↑1d | SQ·PV | +11.2% | 17.17/16.06 | +11.16% | 20% |
| [WINDLAS](https://in.tradingview.com/chart/?symbol=NSE:WINDLAS)<br><sub>📶W9 · W↑52d · RVOL55x · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Pharma CDMO oral solids liquid formulations contract manufacturing | ⚡ BULL_ANY_PPV | 89 | 🔄64 | ↑1.077 | ↑1d | SQ·PV | +12.3% | 42.73/36.2 | +12.32% | 20% |
| [YATRA](https://in.tradingview.com/chart/?symbol=NSE:YATRA)<br><sub>📶W9 · W↑2d · RVOL12x · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Online travel agency for flights hotels bookings | ⚡ BULL_ANY_PPV | 89 | 🔄47 | ↑1.050 | ↑1d | SQ·PV | +9.4% | -11.93/-13.22 | +9.36% | 20% |
| [OIL](https://in.tradingview.com/chart/?symbol=NSE:OIL)<br><sub>📶W9 · W↑17d · 🚀SS · ↑CMF24d</sub> | ✓ SAFE | Crude oil and natural gas exploration production transportation | ⚡ BULL_ANY_PPV | 58 | ↑38 | ↑1.040 | ↑2d | SQ·PV | +6.2% | 39.29/28.0 | +3.83% | 20% |
| [PICCADIL](https://in.tradingview.com/chart/?symbol=NSE:PICCADIL)<br><sub>📶W9 · W↑32d · ↓CMF1d</sub> | ✓ SAFE | Sugar production and premium spirits for Indian consumers | ⚡ BULL_ANY_PPV | 52 | ↑79 | ↑1.030 | ↑8d | SQ·PV | +8.2% | 47.29/43.11 | +1.23% | 20% |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Pistons rings valves engine components automotive OEMs exporters | 📈 BULL_ANY_MID | 97 | 🔄91 | ↑1.008 | ↑3d | SQ | +2.2% | 48.82/48.64 | +0.19% | 20% |
| [EPL](https://in.tradingview.com/chart/?symbol=NSE:EPL)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Laminated plastic tubes for cosmetics pharma food | 📈 BULL_ANY_MID | 94 | 🔄60 | ↑1.023 | ↑1d | SQ | +3.0% | -22.47/-29.7 | +2.97% | 20% |
| [BLUSPRING](https://in.tradingview.com/chart/?symbol=NSE:BLUSPRING)<br><sub>📶W9 · 🚀SS · ↓CMF2d</sub> | ✓ SAFE | Infrastructure services management operations facilities | 📈 BULL_ANY_MID | 89 | 🔄95 | ↑1.035 | ↑1d | SQ | +4.9% | 27.61/24.92 | +4.89% | 10% 🟨 |
| [SILVERTUC](https://in.tradingview.com/chart/?symbol=NSE:SILVERTUC)<br><sub>📶W9 · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | IT services digital transformation e-governance software development | 📈 BULL_ANY_MID | 58 | ↑98 | ↑1.035 | ↑2d | SQ | +5.4% | 26.2/19.44 | +1.64% | 20% |
| [HESTERBIO](https://in.tradingview.com/chart/?symbol=NSE:HESTERBIO)<br><sub>📶W9 · W↑85d · ↓CMF1d</sub> | ✓ SAFE | Poultry livestock vaccines manufacturer animal healthcare sector | 📈 BULL_ANY_MID | 58 | ↑88 | ↓1.011 | ↑2d | SQ | +2.9% | 31.11/27.46 | -0.24% | 20% |
| [NEWGEN](https://in.tradingview.com/chart/?symbol=NSE:NEWGEN)<br><sub>📶W9 · W↑52d · ↓CMF1d · DEL33%(T-1)</sub> | ✓ SAFE | Digital transformation platform: automation, content, communication, low-code | 📈 BULL_ANY_MID | 57 | ↓21 | ↓1.007 | ↑3d | SQ | +2.3% | 34.96/33.95 | -1.44% | 20% |
| [LANDMARK](https://in.tradingview.com/chart/?symbol=NSE:LANDMARK)<br><sub>📶W9 · W↑52d · ↓CMF19d · DEL47%(T-1)</sub> | ✓ SAFE | Premium auto retail, luxury and mass-market vehicles, India | 📈 BULL_ANY_MID | 40 | ↑81 | ↑1.047 | ↑21d | SQ | +35.2% | 52.83/49.78 | +1.85% | 20% |
| [SCHAEFFLER](https://in.tradingview.com/chart/?symbol=NSE:SCHAEFFLER)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Precision bearings transmission components automotive industrial manufacturing | ⚡ BULL_ANY_PPV | 94 | 🔄45 | ↑1.015 | ↑1d | SQ·PV | +2.2% | -21.08/-28.58 | +2.17% | 20% |
| [VIKRAN](https://in.tradingview.com/chart/?symbol=NSE:VIKRAN)<br><sub>W↑2d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Power transmission towers and infrastructure EPC projects | ⚡ BULL_ANY_PPV | 93 | 🔄50 | ↑1.017 | ↑2d | SQ·PV | +2.9% | -2.12/-10.33 | +1.57% | 20% |
| [GRMOVER](https://in.tradingview.com/chart/?symbol=NSE:GRMOVER)<br><sub>W↑2d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Basmati rice milling processing exports domestic international markets | ⚡ BULL_ANY_PPV | 82 | 🔄1 | ↑1.031 | ↑8d | SQ·PV | +6.9% | -13.34/-20.55 | +4.02% | 10% 🟨 |
| [GODREJCP](https://in.tradingview.com/chart/?symbol=NSE:GODREJCP)<br><sub>W↑33d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 98 | 🔄37 | ↑1.008 | ↑2d | SQ | +2.1% | 25.85/25.42 | +1.03% | 20% |
| [VMM](https://in.tradingview.com/chart/?symbol=NSE:VMM)<br><sub>↑CMF0d</sub> | ✓ SAFE | Discount hypermarkets, apparel groceries electronics, middle-income households | 📈 BULL_ANY_MID | 69 | ↓13 | ↑1.004 | ↑1d | SQ | +1.5% | -37.39/-38.16 | +1.52% | 20% |
| [FIRSTCRY](https://in.tradingview.com/chart/?symbol=NSE:FIRSTCRY)<br><sub>W↑7d · ↓CMF30d</sub> | ⚠ CAUTION | Baby kids mothers products online retail platform | 📈 BULL_ANY_MID | 69 | ↓5 | ↑1.002 | ↑1d | SQ | +0.6% | 7.41/7.35 | +0.61% | 20% |
| [ACCELYA](https://in.tradingview.com/chart/?symbol=NSE:ACCELYA)<br><sub>W↑22d · 🚀SS · ↓CMF7d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 67 | ↓30 | ↑1.003 | ↑3d | SQ | +0.8% | 15.35/14.43 | +0.26% | 20% |
| [DELHIVERY](https://in.tradingview.com/chart/?symbol=NSE:DELHIVERY)<br><sub>↑CMF1d · ⚠️TRAP</sub> | ✓ SAFE | Express parcel and freight logistics for ecommerce B2B | 📈 BULL_ANY_MID | 58 | ↓49 | ↓0.999 | ↓2d | SQ | +0.0% | -16.77/-21.34 | -1.02% | 20% |
| [SIGNATURE](https://in.tradingview.com/chart/?symbol=NSE:SIGNATURE)<br><sub>W↑27d · ↓CMF30d</sub> | ✓ SAFE | Residential real estate developer, Gurugram, mid-premium segments | 📈 BULL_ANY_MID | 58 | ↓15 | ↓1.002 | ↑2d | SQ | +1.6% | 16.8/16.54 | -1.18% | 20% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>↑CMF2d</sub> | ✓ SAFE | Spirits manufacturer, IMFL exporter, Indian domestic and export markets | 📈 BULL_ANY_MID | 58 | ↓65 | ↓1.002 | ↓2d | SQ | +3.4% | -20.95/-23.3 | -0.78% | 10% 🟩 |
| [LGBBROSLTD](https://in.tradingview.com/chart/?symbol=NSE:LGBBROSLTD)<br><sub>↓CMF24d · ⚠️TRAP</sub> | ⚠ CAUTION | Transmission chains sprockets metal parts automotive industrial | 📈 BULL_ANY_MID | 58 | ↓35 | ↓1.004 | ↑2d | SQ | +1.7% | -19.17/-22.15 | -0.15% | 20% |
| [SAGCEM](https://in.tradingview.com/chart/?symbol=NSE:SAGCEM)<br><sub>↑CMF24d</sub> | ⚠ CAUTION | Cement manufacturing, South and Central India construction | 📈 BULL_ANY_MID | 58 | ↓18 | ↑1.004 | ↓12d | SQ | -1.4% | -27.44/-28.16 | +1.73% | 20% |
| [MAYURUNIQ](https://in.tradingview.com/chart/?symbol=NSE:MAYURUNIQ)<br><sub>↓CMF11d</sub> | ✓ SAFE | Synthetic leather manufacturer for automotive footwear upholstery | 📈 BULL_ANY_MID | 50 | ↓84 | ↑1.001 | ↓22d | SQ | -6.5% | -38.27/-39.13 | +0.46% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:KAJARIACER,NSE:MRPL,NSE:WINDLAS,NSE:YATRA,NSE:OIL,NSE:PICCADIL,NSE:SHRIPISTON,NSE:EPL,NSE:BLUSPRING,NSE:SILVERTUC,NSE:HESTERBIO,NSE:NEWGEN,NSE:LANDMARK,NSE:SCHAEFFLER,NSE:VIKRAN,NSE:GRMOVER,NSE:GODREJCP,NSE:VMM,NSE:FIRSTCRY,NSE:ACCELYA,NSE:DELHIVERY,NSE:SIGNATURE,NSE:ABDL,NSE:LGBBROSLTD,NSE:SAGCEM,NSE:MAYURUNIQ
```

---

### 🔥 MAJOR — PPV confirmed (11)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>📶W9 · W↑22d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Crude oil refining, petroleum products, lubricant additives | ⚡ BULL_ANY_PPV | 49 | 🔄93 | ↑1.102 | ↑1d | PV | +15.0% | 45.49/43.76 | +15.00% | 20% |
| [ARE&M](https://in.tradingview.com/chart/?symbol=NSE:ARE&M)<br><sub>📶W9 · W↑85d · 🚀SS·9x · ↑CMF0d</sub> | ✓ SAFE | Lead-acid batteries automotive industrial energy storage | ⚡ BULL_ANY_PPV | 49 | 🔄58 | ↑1.051 | ↑1d | PV | +8.1% | 44.07/43.44 | +8.08% | 20% |
| [UNICHEMLAB](https://in.tradingview.com/chart/?symbol=NSE:UNICHEMLAB)<br><sub>📶W9 · RVOL27x · ↑CMF0d</sub> | ✓ SAFE | Pharma generics APIs contract manufacturing CMO | ⚡ BULL_ANY_PPV | 49 | 🔄85 | ↑1.099 | ↑1d | PV | +13.1% | -13.33/-20.93 | +13.14% | 20% |
| [GANDHITUBE](https://in.tradingview.com/chart/?symbol=NSE:GANDHITUBE)<br><sub>📶W9 · W↑27d · 🚀SS·11x · ↑CMF0d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 30 | 🔄64 | ↑1.043 | ↑22d | PV | +8.9% | 73.64/67.54 | +5.58% | 20% |
| [TCPLPACK](https://in.tradingview.com/chart/?symbol=NSE:TCPLPACK)<br><sub>📶W9 · W↑42d · RVOL9x · ↑CMF11d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 18 | ↑80 | ↑1.118 | ↑2d | PV | +16.7% | 33.18/16.0 | +11.38% | 20% |
| [NAUKRI](https://in.tradingview.com/chart/?symbol=NSE:NAUKRI)<br><sub>📶W9 · W↑97d · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Job portal, real estate classifieds, matrimonial matchmaking platform | ⚡ BULL_ANY_PPV | 0 | ↑75 | ↑1.077 | ↑30d | PV | +40.1% | 60.32/51.8 | +6.08% | 20% |
| [IRISDOREME](https://in.tradingview.com/chart/?symbol=NSE:IRISDOREME)<br><sub>📶W9 · W↑85d · 🚀SS · ★ · ↑CMF30d · DEL68%(T-1)</sub> | ✓ SAFE | Infant children apparel manufacturer integrated production India | ⚡ BULL_ANY_PPV | 0 | ↑94 | ↓1.056 | ↑39d | PV | +56.9% | 74.15/73.89 | +0.99% | 20% |
| [KSCL](https://in.tradingview.com/chart/?symbol=NSE:KSCL)<br><sub>↓CMF16d · 🎯SLING</sub> | ✓ SAFE | Hybrid seed research, production, field crops, vegetables | 🔥 BULL_OS_PPV | 59 | 🔄10 | ↑1.014 | ↑1d | PV | +4.7% | -59.37/-63.11 | +4.68% | 20% |
| [FUSION](https://in.tradingview.com/chart/?symbol=NSE:FUSION)<br><sub>🚀SS · ↓CMF8d</sub> | ✓ SAFE | Microfinance loans for rural women entrepreneurs | ⚡ BULL_ANY_PPV | 56 | 🔄68 | ↑1.008 | ↓4d | PV | +1.1% | -15.4/-18.8 | +2.89% | 20% |
| [TEJASNET](https://in.tradingview.com/chart/?symbol=NSE:TEJASNET)<br><sub>🚀SS · ↓CMF23d</sub> | ✓ SAFE | Optical wireless networking products telecom service providers infrastructure | ⚡ BULL_ANY_PPV | 54 | 🔄70 | ↑1.020 | ↑1d | PV | +2.3% | -11.44/-18.99 | +2.32% | 20% 🟦 |
| [GODAVARIB](https://in.tradingview.com/chart/?symbol=NSE:GODAVARIB)<br><sub>🚀SS·81x · ↑CMF0d</sub> | ✓ SAFE | Sugarcane biorefinery making chemicals ethanol power and sugar | ⚡ BULL_ANY_PPV | 49 | 🔄29 | ↑1.051 | ↑1d | PV | +13.9% | -44.31/-44.74 | +13.95% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CHENNPETRO,NSE:ARE&M,NSE:UNICHEMLAB,NSE:GANDHITUBE,NSE:TCPLPACK,NSE:NAUKRI,NSE:IRISDOREME,NSE:KSCL,NSE:FUSION,NSE:TEJASNET,NSE:GODAVARIB
```

### 🟢 OVERSOLD — reversal from −53/−60 (4)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [KCP](https://in.tradingview.com/chart/?symbol=NSE:KCP)<br><sub>↓CMF12d · 🎯SLING</sub> | ⚠ CAUTION | Cement sugar heavy engineering power hospitality conglomerate | 🟢 BULL_OVERSOLD | 10 | ↓11 | ↑0.978 | ↓15d | — | -9.8% | -60.93/-61.71 | +0.04% | 20% |
| [KSB](https://in.tradingview.com/chart/?symbol=NSE:KSB)<br><sub>↓CMF17d · 🎯SLING</sub> | ✓ SAFE | Pumps and valves for power, water, agriculture | 🟢 BULL_OVERSOLD | 5 | ↓43 | ↑0.987 | ↓43d | — | +0.6% | -60.47/-61.86 | +0.99% | 20% |
| [SAFARI](https://in.tradingview.com/chart/?symbol=NSE:SAFARI)<br><sub>↓CMF28d · ⚠️TRAP</sub> | ⚠ CAUTION | Luggage and travel bags manufacturer, domestic and export markets | 🟡 BULL_OS_L2 | 7 | ↓10 | ↑0.986 | ↓18d | — | -7.8% | -54.21/-54.57 | -0.23% | 20% |
| [VBL](https://in.tradingview.com/chart/?symbol=NSE:VBL)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 5 | ↓21 | ↑0.992 | ↓38d | — | -15.2% | -55.06/-56.28 | +1.38% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:KCP,NSE:KSB,NSE:SAFARI,NSE:VBL
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (26)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄83 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [INDOTECH](https://in.tradingview.com/chart/?symbol=NSE:INDOTECH)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | Power distribution transformers utility industrial renewable energy | 📈 BULL_ANY_MID | 49 | 🔄99 | ↑1.334 | ↑1d | — | +50.8% | 56.69/49.57 | +50.82% | 5% 🟥 |
| [SENCO](https://in.tradingview.com/chart/?symbol=NSE:SENCO)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE | Gold diamond silver jewelry retail Eastern India focus | 📈 BULL_ANY_MID | 28 | ↑70 | ↑1.015 | ↑2d | — | +3.2% | 34.64/33.4 | +0.60% | 20% |
| [MOBIKWIK](https://in.tradingview.com/chart/?symbol=NSE:MOBIKWIK)<br><sub>📶W9 · W↑2d · ↓CMF2d</sub> | ✓ SAFE | Digital wallet and payments for consumers merchants | 📈 BULL_ANY_MID | 23 | ↑39 | ↑1.028 | ↑2d | — | +5.9% | -0.59/-5.71 | +2.67% | 20% |
| [COSMOFIRST](https://in.tradingview.com/chart/?symbol=NSE:COSMOFIRST)<br><sub>📶W9 · W↑85d · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | Specialty films for packaging, lamination, labeling applications | 📈 BULL_ANY_MID | 17 | ↑69 | ↓1.030 | ↑3d | — | +6.7% | 61.86/59.65 | +0.34% | 20% |
| [TINNARUBR](https://in.tradingview.com/chart/?symbol=NSE:TINNARUBR)<br><sub>📶W9 · W↑90d · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Waste tyre recycling into rubber crumb and steel products | 📈 BULL_ANY_MID | 17 | ↑88 | ↑1.024 | ↑8d | — | +9.1% | 47.05/46.01 | +1.47% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 11 | ↑68 | ↓1.011 | ↑9d | — | +5.3% | 52.94/52.13 | +0.00% | 20% |
| [NEPHROPLUS](https://in.tradingview.com/chart/?symbol=NSE:NEPHROPLUS)<br><sub>📶W9 · ↑CMF11d</sub> | ✓ SAFE | Dialysis center chain serving kidney disease patients India | 📈 BULL_ANY_MID | 10 | ↑50 | ↑1.030 | ↑15d | — | +13.3% | 34.27/30.79 | +2.44% | 20% |
| [LENSKART](https://in.tradingview.com/chart/?symbol=NSE:LENSKART)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Eyewear design manufacturing retail omnichannel direct consumer | 📈 BULL_ANY_MID | 5 | ↑50 | ↑1.030 | ↑30d | — | +15.9% | 64.3/61.91 | +2.24% | 20% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>📶W9 · W↑102d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Electronics manufacturing design integration testing subsystems defense aerospace | 📈 BULL_ANY_MID | 0 | ↑95 | ↑1.048 | ↑29d | — | +52.7% | 57.62/55.4 | +2.53% | 20% |
| [DEEDEV](https://in.tradingview.com/chart/?symbol=NSE:DEEDEV)<br><sub>📶W9 · W↑65d · 🚀SS · ↑CMF23d</sub> | ✓ SAFE | Process piping systems oil gas power thermal | 📈 BULL_ANY_MID | 0 | ↑99 | ↑1.243 | ↑31d | — | +131.8% | 73.24/67.09 | +30.83% | 5% 🟥 |
| [CDSL](https://in.tradingview.com/chart/?symbol=NSE:CDSL)<br><sub>↓CMF2d</sub> | ✓ SAFE | Electronic securities holding settlement infrastructure depository | 📈 BULL_ANY_MID | 59 | 🔄39 | ↑1.007 | ↑1d | — | +1.1% | -18.22/-19.72 | +1.09% | 20% |
| [HDBFS](https://in.tradingview.com/chart/?symbol=NSE:HDBFS)<br><sub>↓CMF17d</sub> | ⚠ CAUTION | Auto loans and two-wheeler financing for underbanked customers | 📈 BULL_ANY_MID | 59 | 🔄36 | ↑1.014 | ↑1d | — | +2.5% | -37.11/-40.33 | +2.47% | 20% |
| [FEDFINA](https://in.tradingview.com/chart/?symbol=NSE:FEDFINA)<br><sub>↓CMF30d</sub> | ✓ SAFE | MSME gold loans and business credit NBFC | 📈 BULL_ANY_MID | 54 | 🔄56 | ↑1.018 | ↑1d | — | +3.2% | -24.91/-28.84 | +3.16% | 20% |
| [INDOSTAR](https://in.tradingview.com/chart/?symbol=NSE:INDOSTAR)<br><sub>🚀SS · ↓CMF14d</sub> | ✓ SAFE | NBFC lending commercial vehicles SME infrastructure | 📈 BULL_ANY_MID | 48 | 🔄58 | ↑1.013 | ↓12d | — | -4.6% | -26.14/-27.87 | +2.66% | 20% |
| [SKMEGGPROD](https://in.tradingview.com/chart/?symbol=NSE:SKMEGGPROD)<br><sub>🚀SS · ↓CMF9d</sub> | ✓ SAFE | Egg powder processing and export, poultry sector | 📈 BULL_ANY_MID | 41 | 🔄88 | ↑1.028 | ↓14d | — | -16.4% | -34.94/-39.02 | +5.12% | 20% |
| [BALAMINES](https://in.tradingview.com/chart/?symbol=NSE:BALAMINES)<br><sub>🚀SS · ↓CMF6d</sub> | ✓ SAFE | Aliphatic amines specialty chemicals manufacturer for industrial applications | 📈 BULL_ANY_MID | 40 | 🔄89 | ↑1.009 | ↓25d | — | +2.7% | -31.71/-33.06 | +3.79% | 20% |
| [EPIGRAL](https://in.tradingview.com/chart/?symbol=NSE:EPIGRAL)<br><sub>W↑17d · ↑CMF16d · ⚠️TRAP</sub> | ✓ SAFE | Chlor-alkali chemicals, caustic soda, chlorine manufacturing | 📈 BULL_ANY_MID | 18 | ↓10 | ↓0.996 | ↓2d | — | +0.5% | 0.91/0.66 | -1.75% | 20% |
| [ADFFOODS](https://in.tradingview.com/chart/?symbol=NSE:ADFFOODS)<br><sub>↓CMF29d</sub> | ✓ SAFE | Pickles chutneys ready meals export frozen foods | 📈 BULL_ANY_MID | 12 | ↓60 | ↑0.977 | ↓13d | — | -10.5% | -51.87/-52.16 | +0.95% | 20% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>↓CMF23d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 10 | ↓62 | ↑0.984 | ↓15d | — | -7.1% | -51.35/-51.43 | -0.24% | 20% |
| [ONESOURCE](https://in.tradingview.com/chart/?symbol=NSE:ONESOURCE)<br><sub>🚀SS · ↑CMF22d</sub> | ✓ SAFE | Specialty pharma CDMO injectable biologics contract manufacturing | 📈 BULL_ANY_MID | 10 | ↓35 | ↑1.001 | ↓22d | — | -1.7% | -14.95/-15.41 | +1.49% | 20% 🟦 |
| [BORORENEW](https://in.tradingview.com/chart/?symbol=NSE:BORORENEW)<br><sub>↓CMF8d</sub> | ✓ SAFE | Solar panel glass manufacturing India photovoltaic energy | 📈 BULL_ANY_MID | 10 | ↓44 | ↑1.002 | ↓24d | — | -5.4% | -39.97/-40.96 | +2.55% | 20% |
| [JINDALPOLY](https://in.tradingview.com/chart/?symbol=NSE:JINDALPOLY)<br><sub>↓CMF29d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 8 | ↓61 | ↑0.998 | ↓17d | — | -4.5% | -38.11/-38.24 | +0.16% | 20% |
| [CIEINDIA](https://in.tradingview.com/chart/?symbol=NSE:CIEINDIA)<br><sub>🚀SS · ↓CMF17d</sub> | ✓ SAFE | Automotive components supplier transmissions suspensions global OEM | 📈 BULL_ANY_MID | 6 | ↓29 | ↑0.994 | ↓19d | — | -10.4% | -36.32/-37.16 | +0.85% | 20% |
| [NINSYS](https://in.tradingview.com/chart/?symbol=NSE:NINSYS)<br><sub>↓CMF6d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 5 | ↓93 | ↑0.966 | ↓37d | — | +5.9% | -45.71/-45.74 | -0.64% | 5% |
| [NORTHARC](https://in.tradingview.com/chart/?symbol=NSE:NORTHARC)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Non-bank lender financing underserved households and SMEs | 📈 BULL_ANY_MID | 0 | ↓54 | ↓0.989 | ↓24d | — | -4.7% | -37.67/-38.12 | -1.07% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:OFSS,NSE:INDOTECH,NSE:SENCO,NSE:MOBIKWIK,NSE:COSMOFIRST,NSE:TINNARUBR,NSE:NESTLEIND,NSE:NEPHROPLUS,NSE:LENSKART,NSE:CYIENTDLM,NSE:DEEDEV,NSE:CDSL,NSE:HDBFS,NSE:FEDFINA,NSE:INDOSTAR,NSE:SKMEGGPROD,NSE:BALAMINES,NSE:EPIGRAL,NSE:ADFFOODS,NSE:ADANIPORTS,NSE:ONESOURCE,NSE:BORORENEW,NSE:JINDALPOLY,NSE:CIEINDIA,NSE:NINSYS,NSE:NORTHARC
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
