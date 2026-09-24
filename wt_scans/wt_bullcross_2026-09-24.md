> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-09-24
*Generated 2026-09-24 15:46 IST*

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

**Total bull crosses today: 57** · 24 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AJAXENGG,NSE:ROTO,NSE:WINDMACHIN,NSE:JAGSNPHARM,NSE:GODREJAGRO,NSE:HDFCLIFE,NSE:SBILIFE,NSE:SEDEMAC,NSE:SIGMAADV,NSE:CIPLA,NSE:KAJARIACER,NSE:SANGAMIND,NSE:ARVIND,NSE:VIPIND,NSE:LALPATHLAB,NSE:SUPRAJIT,NSE:POLYMED,NSE:TATASTEEL,NSE:INDHOTEL,NSE:ASTERDM,NSE:AEROFLEX,NSE:MEESHO,NSE:PNB,NSE:CARTRADE,NSE:TMB,NSE:SHILCTECH,NSE:OMAXE,NSE:TASTYBITE,NSE:BALAMINES,NSE:INDNIPPON,NSE:RAYMOND,NSE:KRBL,NSE:CEIGALL,NSE:GODIGIT,NSE:HGINFRA,NSE:ABREL,NSE:SANOFI,NSE:VTL,NSE:GILLETTE,NSE:GOKEX,NSE:FAZE3Q,NSE:MARUTI,NSE:ASIANPAINT,NSE:BUTTERFLY,NSE:CENTURYPLY,NSE:ADANIENSOL,NSE:NESTLEIND,NSE:IOC,NSE:M&M,NSE:TRENT,NSE:MAZDOCK,NSE:BRITANNIA,NSE:ORIENTTECH,NSE:SAIPARENT,NSE:FMGOETZE,NSE:BPCL,NSE:GENUSPOWER
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (33)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [AJAXENGG](https://in.tradingview.com/chart/?symbol=NSE:AJAXENGG)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 99 | 🔄53 | ↑1.006 | ↑1d | SQ·PV | +1.1% | -11.52/-11.61 | +1.06% | 20% |
| [ROTO](https://in.tradingview.com/chart/?symbol=NSE:ROTO)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Progressive cavity pumps for wastewater and sugar industries | ⚡ BULL_ANY_PPV | 99 | 🔄33 | ↑1.006 | ↑1d | SQ·PV | +1.0% | -36.94/-42.43 | +1.01% | 20% |
| [WINDMACHIN](https://in.tradingview.com/chart/?symbol=NSE:WINDMACHIN)<br><sub>📶W9 · ↑CMF30d</sub> | ⚠ CAUTION | Plastic injection moulding pipe extrusion machinery manufacturer | ⚡ BULL_ANY_PPV | 99 | 🔄57 | ↑1.004 | ↑1d | SQ·PV | +1.9% | -32.06/-34.48 | +1.86% | 20% |
| [JAGSNPHARM](https://in.tradingview.com/chart/?symbol=NSE:JAGSNPHARM)<br><sub>📶W9 · 🚀SS·120x · ↑CMF0d</sub> | ✓ SAFE | Women's health and pain management pharmaceutical manufacturer India | ⚡ BULL_ANY_PPV | 89 | 🔄56 | ↑1.053 | ↑1d | SQ·PV | +8.1% | -21.89/-31.08 | +8.13% | 20% |
| [GODREJAGRO](https://in.tradingview.com/chart/?symbol=NSE:GODREJAGRO)<br><sub>📶W9 · W↑29d · ↓CMF17d</sub> | ✓ SAFE | Animal feed, oil palm, crop protection for farmers | ⚡ BULL_ANY_PPV | 63 | ↑66 | ↑1.021 | ↑2d | SQ·PV | +3.4% | 41.81/36.73 | +0.90% | 20% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>📶W9 · W↑3d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 19 | ↑14 | ↑1.042 | ↑1d | PV | +5.0% | -31.89/-43.91 | +5.05% | 20% |
| [SBILIFE](https://in.tradingview.com/chart/?symbol=NSE:SBILIFE)<br><sub>📶W9 · ↓CMF16d · 🎯SLING</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 19 | ↑36 | ↑1.031 | ↑1d | PV | +4.2% | -50.09/-59.33 | +4.19% | 20% |
| [SEDEMAC](https://in.tradingview.com/chart/?symbol=NSE:SEDEMAC)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Engine control electronics for automotive and off-highway vehicles | ⚡ BULL_ANY_PPV | 13 | ↑50 | ↑1.077 | ↑7d | PV | +13.1% | 26.54/19.32 | +8.23% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [CIPLA](https://in.tradingview.com/chart/?symbol=NSE:CIPLA)<br><sub>📶W9 · 🚀SS · ↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 10 | ↑41 | ↑1.005 | ↓37d | — | -1.7% | -61.96/-65.24 | +1.99% | 20% |
| [KAJARIACER](https://in.tradingview.com/chart/?symbol=NSE:KAJARIACER)<br><sub>📶W9 · ↑CMF23d</sub> | ⚠ CAUTION | Ceramic and vitrified tiles manufacturer for construction | 📈 BULL_ANY_MID | 99 | 🔄61 | ↑1.006 | ↑1d | SQ | +0.4% | -25.43/-29.51 | +0.44% | 20% |
| [SANGAMIND](https://in.tradingview.com/chart/?symbol=NSE:SANGAMIND)<br><sub>📶W9 · ↑CMF13d</sub> | ✓ SAFE | PV yarn denim seamless garments textile manufacturer | 📈 BULL_ANY_MID | 99 | 🔄72 | ↑1.007 | ↑1d | SQ | +1.6% | -17.12/-20.13 | +1.55% | 20% |
| [ARVIND](https://in.tradingview.com/chart/?symbol=NSE:ARVIND)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Textiles denim apparel retail vertically integrated manufacturing | 📈 BULL_ANY_MID | 94 | 🔄86 | ↑1.024 | ↑1d | SQ | +3.2% | -5.44/-6.16 | +3.18% | 20% |
| [VIPIND](https://in.tradingview.com/chart/?symbol=NSE:VIPIND)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Luggage and travel bags manufacturer for domestic and international markets | 📈 BULL_ANY_MID | 94 | 🔄18 | ↑1.003 | ↓6d | SQ | +1.1% | -22.45/-22.64 | +0.69% | 20% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>📶W9 · ↓CMF6d</sub> | ✓ SAFE | Diagnostic lab network pathology testing healthcare services | 📈 BULL_ANY_MID | 93 | 🔄78 | ↑1.021 | ↑2d | SQ | +2.7% | 32.6/20.14 | +1.92% | 20% |
| [SUPRAJIT](https://in.tradingview.com/chart/?symbol=NSE:SUPRAJIT)<br><sub>📶W9 · ↓CMF3d</sub> | ⚠ CAUTION | Automotive cables, halogen lamps, mechanical components manufacturer | 📈 BULL_ANY_MID | 90 | 🔄52 | ↑0.999 | ↓5d | SQ | +0.4% | -27.13/-27.23 | +0.33% | 20% |
| [POLYMED](https://in.tradingview.com/chart/?symbol=NSE:POLYMED)<br><sub>📶W9 · ↓CMF13d</sub> | ✓ SAFE | Surgical disposables and medical devices manufacturer for hospitals | 📈 BULL_ANY_MID | 88 | 🔄51 | ↓0.999 | ↓2d | SQ | +1.0% | -19.24/-26.26 | -0.61% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>📶W9 · ↑CMF27d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 69 | ↑47 | ↑1.011 | ↑1d | SQ | +2.3% | -10.62/-12.03 | +2.27% | 20% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>📶W9 · ↑CMF24d</sub> | ⚠ CAUTION | Luxury and midscale hotel brands across Asia Pacific | 📈 BULL_ANY_MID | 69 | ↑48 | ↑1.008 | ↑1d | SQ | +1.6% | -22.75/-27.38 | +1.64% | 20% |
| [ASTERDM](https://in.tradingview.com/chart/?symbol=NSE:ASTERDM)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Multi-specialty hospitals and clinics, India healthcare | 📈 BULL_ANY_MID | 59 | 🔄62 | ↑1.011 | ↑1d | — | +1.1% | -23.29/-28.36 | +1.13% | 20% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Stainless steel corrugated hoses assemblies fittings industrial applications | 📈 BULL_ANY_MID | 59 | 🔄96 | ↑1.009 | ↑1d | — | +1.2% | 9.75/8.33 | +1.23% | 10% 🟨 |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · W↑30d · ↑CMF30d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.025 | ↑2d | SQ | +6.1% | 49.69/48.04 | -0.06% | 20% 🟦 |
| [PNB](https://in.tradingview.com/chart/?symbol=NSE:PNB)<br><sub>📶W9 · W↑72d · ↓CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | ↑52 | ↓1.004 | ↑2d | SQ | +1.8% | 22.16/15.43 | -0.05% | 20% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Used car marketplace and financing platform India | 📈 BULL_ANY_MID | 58 | ↑76 | ↓1.007 | ↑2d | SQ | +3.3% | -4.77/-7.03 | +0.10% | 20% |
| [TMB](https://in.tradingview.com/chart/?symbol=NSE:TMB)<br><sub>📶W9 · ↑CMF19d</sub> | ⚠ CAUTION | Regional private bank serving retail agriculture MSME segments | 📈 BULL_ANY_MID | 58 | ↑90 | ↓0.993 | ↓2d | SQ | +1.1% | 1.15/-0.52 | -3.02% | 20% |
| [SHILCTECH](https://in.tradingview.com/chart/?symbol=NSE:SHILCTECH)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Distribution and power transformers for industrial electrical systems | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.001 | ↑2d | SQ | +2.3% | -1.6/-4.78 | -1.65% | 20% |
| [OMAXE](https://in.tradingview.com/chart/?symbol=NSE:OMAXE)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Residential commercial real estate developer across Indian cities | 📈 BULL_ANY_MID | 58 | ↓88 | ↓0.987 | ↓2d | SQ | +1.0% | 1.16/1.01 | -4.43% | 20% |
| [TASTYBITE](https://in.tradingview.com/chart/?symbol=NSE:TASTYBITE)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Ready-to-eat ethnic vegetarian meals packaged food export | 📈 BULL_ANY_MID | 58 | ↑72 | ↓0.994 | ↓2d | SQ | +0.8% | 4.97/1.49 | -2.72% | 20% |
| [BALAMINES](https://in.tradingview.com/chart/?symbol=NSE:BALAMINES)<br><sub>📶W9 · ★ · ↓CMF2d</sub> | ✓ SAFE | Aliphatic amines and specialty chemicals manufacturer for industrial applications | 📈 BULL_ANY_MID | 18 | ↑91 | ↓1.003 | ↓2d | — | +4.1% | -12.87/-16.02 | -1.99% | 20% |
| [INDNIPPON](https://in.tradingview.com/chart/?symbol=NSE:INDNIPPON)<br><sub>📶W9 · W↑14d · ↓CMF10d · ÷DIV</sub> | ✓ SAFE | Electronic ignition systems two-wheeler three-wheeler portable engines | 📈 BULL_ANY_MID | 4 | ↑89 | ↑1.043 | ↑16d | — | +23.6% | 26.29/23.41 | +4.38% | 20% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>📶W9 · W↑34d · ↑CMF30d</sub> | ✓ SAFE | Textiles apparel real estate FMCG engineering diversified conglomerate | 📈 BULL_ANY_MID | 1 | ↑99 | ↑1.157 | ↑19d | — | +92.0% | 77.34/77.23 | +8.00% | 20% |
| [KRBL](https://in.tradingview.com/chart/?symbol=NSE:KRBL)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | Basmati rice processing and export for domestic and global markets | 📈 BULL_ANY_MID | 0 | ↑58 | ↓0.991 | ↓39d | — | +13.4% | -21.62/-22.37 | -1.64% | 20% |
| [CEIGALL](https://in.tradingview.com/chart/?symbol=NSE:CEIGALL)<br><sub>📶W9 · W↑14d · ↑CMF13d</sub> | ✓ SAFE | EPC contractor highways bridges tunnels rail infrastructure | 📈 BULL_ANY_MID | 0 | ↑75 | ↓1.008 | ↑24d | — | +21.7% | 45.55/45.47 | -1.62% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AJAXENGG,NSE:ROTO,NSE:WINDMACHIN,NSE:JAGSNPHARM,NSE:GODREJAGRO,NSE:HDFCLIFE,NSE:SBILIFE,NSE:SEDEMAC,NSE:SIGMAADV,NSE:CIPLA,NSE:KAJARIACER,NSE:SANGAMIND,NSE:ARVIND,NSE:VIPIND,NSE:LALPATHLAB,NSE:SUPRAJIT,NSE:POLYMED,NSE:TATASTEEL,NSE:INDHOTEL,NSE:ASTERDM,NSE:AEROFLEX,NSE:MEESHO,NSE:PNB,NSE:CARTRADE,NSE:TMB,NSE:SHILCTECH,NSE:OMAXE,NSE:TASTYBITE,NSE:BALAMINES,NSE:INDNIPPON,NSE:RAYMOND,NSE:KRBL,NSE:CEIGALL
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (44)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [AJAXENGG](https://in.tradingview.com/chart/?symbol=NSE:AJAXENGG)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 99 | 🔄53 | ↑1.006 | ↑1d | SQ·PV | +1.1% | -11.52/-11.61 | +1.06% | 20% |
| [ROTO](https://in.tradingview.com/chart/?symbol=NSE:ROTO)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Progressive cavity pumps for wastewater and sugar industries | ⚡ BULL_ANY_PPV | 99 | 🔄33 | ↑1.006 | ↑1d | SQ·PV | +1.0% | -36.94/-42.43 | +1.01% | 20% |
| [WINDMACHIN](https://in.tradingview.com/chart/?symbol=NSE:WINDMACHIN)<br><sub>📶W9 · ↑CMF30d</sub> | ⚠ CAUTION | Plastic injection moulding pipe extrusion machinery manufacturer | ⚡ BULL_ANY_PPV | 99 | 🔄57 | ↑1.004 | ↑1d | SQ·PV | +1.9% | -32.06/-34.48 | +1.86% | 20% |
| [JAGSNPHARM](https://in.tradingview.com/chart/?symbol=NSE:JAGSNPHARM)<br><sub>📶W9 · 🚀SS·120x · ↑CMF0d</sub> | ✓ SAFE | Women's health and pain management pharmaceutical manufacturer India | ⚡ BULL_ANY_PPV | 89 | 🔄56 | ↑1.053 | ↑1d | SQ·PV | +8.1% | -21.89/-31.08 | +8.13% | 20% |
| [GODREJAGRO](https://in.tradingview.com/chart/?symbol=NSE:GODREJAGRO)<br><sub>📶W9 · W↑29d · ↓CMF17d</sub> | ✓ SAFE | Animal feed, oil palm, crop protection for farmers | ⚡ BULL_ANY_PPV | 63 | ↑66 | ↑1.021 | ↑2d | SQ·PV | +3.4% | 41.81/36.73 | +0.90% | 20% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>📶W9 · W↑3d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 19 | ↑14 | ↑1.042 | ↑1d | PV | +5.0% | -31.89/-43.91 | +5.05% | 20% |
| [SBILIFE](https://in.tradingview.com/chart/?symbol=NSE:SBILIFE)<br><sub>📶W9 · ↓CMF16d · 🎯SLING</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 19 | ↑36 | ↑1.031 | ↑1d | PV | +4.2% | -50.09/-59.33 | +4.19% | 20% |
| [SEDEMAC](https://in.tradingview.com/chart/?symbol=NSE:SEDEMAC)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Engine control electronics for automotive and off-highway vehicles | ⚡ BULL_ANY_PPV | 13 | ↑50 | ↑1.077 | ↑7d | PV | +13.1% | 26.54/19.32 | +8.23% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [CIPLA](https://in.tradingview.com/chart/?symbol=NSE:CIPLA)<br><sub>📶W9 · 🚀SS · ↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 10 | ↑41 | ↑1.005 | ↓37d | — | -1.7% | -61.96/-65.24 | +1.99% | 20% |
| [KAJARIACER](https://in.tradingview.com/chart/?symbol=NSE:KAJARIACER)<br><sub>📶W9 · ↑CMF23d</sub> | ⚠ CAUTION | Ceramic and vitrified tiles manufacturer for construction | 📈 BULL_ANY_MID | 99 | 🔄61 | ↑1.006 | ↑1d | SQ | +0.4% | -25.43/-29.51 | +0.44% | 20% |
| [SANGAMIND](https://in.tradingview.com/chart/?symbol=NSE:SANGAMIND)<br><sub>📶W9 · ↑CMF13d</sub> | ✓ SAFE | PV yarn denim seamless garments textile manufacturer | 📈 BULL_ANY_MID | 99 | 🔄72 | ↑1.007 | ↑1d | SQ | +1.6% | -17.12/-20.13 | +1.55% | 20% |
| [ARVIND](https://in.tradingview.com/chart/?symbol=NSE:ARVIND)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Textiles denim apparel retail vertically integrated manufacturing | 📈 BULL_ANY_MID | 94 | 🔄86 | ↑1.024 | ↑1d | SQ | +3.2% | -5.44/-6.16 | +3.18% | 20% |
| [VIPIND](https://in.tradingview.com/chart/?symbol=NSE:VIPIND)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Luggage and travel bags manufacturer for domestic and international markets | 📈 BULL_ANY_MID | 94 | 🔄18 | ↑1.003 | ↓6d | SQ | +1.1% | -22.45/-22.64 | +0.69% | 20% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>📶W9 · ↓CMF6d</sub> | ✓ SAFE | Diagnostic lab network pathology testing healthcare services | 📈 BULL_ANY_MID | 93 | 🔄78 | ↑1.021 | ↑2d | SQ | +2.7% | 32.6/20.14 | +1.92% | 20% |
| [SUPRAJIT](https://in.tradingview.com/chart/?symbol=NSE:SUPRAJIT)<br><sub>📶W9 · ↓CMF3d</sub> | ⚠ CAUTION | Automotive cables, halogen lamps, mechanical components manufacturer | 📈 BULL_ANY_MID | 90 | 🔄52 | ↑0.999 | ↓5d | SQ | +0.4% | -27.13/-27.23 | +0.33% | 20% |
| [POLYMED](https://in.tradingview.com/chart/?symbol=NSE:POLYMED)<br><sub>📶W9 · ↓CMF13d</sub> | ✓ SAFE | Surgical disposables and medical devices manufacturer for hospitals | 📈 BULL_ANY_MID | 88 | 🔄51 | ↓0.999 | ↓2d | SQ | +1.0% | -19.24/-26.26 | -0.61% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>📶W9 · ↑CMF27d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 69 | ↑47 | ↑1.011 | ↑1d | SQ | +2.3% | -10.62/-12.03 | +2.27% | 20% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>📶W9 · ↑CMF24d</sub> | ⚠ CAUTION | Luxury and midscale hotel brands across Asia Pacific | 📈 BULL_ANY_MID | 69 | ↑48 | ↑1.008 | ↑1d | SQ | +1.6% | -22.75/-27.38 | +1.64% | 20% |
| [ASTERDM](https://in.tradingview.com/chart/?symbol=NSE:ASTERDM)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Multi-specialty hospitals and clinics, India healthcare | 📈 BULL_ANY_MID | 59 | 🔄62 | ↑1.011 | ↑1d | — | +1.1% | -23.29/-28.36 | +1.13% | 20% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Stainless steel corrugated hoses assemblies fittings industrial applications | 📈 BULL_ANY_MID | 59 | 🔄96 | ↑1.009 | ↑1d | — | +1.2% | 9.75/8.33 | +1.23% | 10% 🟨 |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · W↑30d · ↑CMF30d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.025 | ↑2d | SQ | +6.1% | 49.69/48.04 | -0.06% | 20% 🟦 |
| [PNB](https://in.tradingview.com/chart/?symbol=NSE:PNB)<br><sub>📶W9 · W↑72d · ↓CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | ↑52 | ↓1.004 | ↑2d | SQ | +1.8% | 22.16/15.43 | -0.05% | 20% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Used car marketplace and financing platform India | 📈 BULL_ANY_MID | 58 | ↑76 | ↓1.007 | ↑2d | SQ | +3.3% | -4.77/-7.03 | +0.10% | 20% |
| [TMB](https://in.tradingview.com/chart/?symbol=NSE:TMB)<br><sub>📶W9 · ↑CMF19d</sub> | ⚠ CAUTION | Regional private bank serving retail agriculture MSME segments | 📈 BULL_ANY_MID | 58 | ↑90 | ↓0.993 | ↓2d | SQ | +1.1% | 1.15/-0.52 | -3.02% | 20% |
| [SHILCTECH](https://in.tradingview.com/chart/?symbol=NSE:SHILCTECH)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Distribution and power transformers for industrial electrical systems | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.001 | ↑2d | SQ | +2.3% | -1.6/-4.78 | -1.65% | 20% |
| [TASTYBITE](https://in.tradingview.com/chart/?symbol=NSE:TASTYBITE)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Ready-to-eat ethnic vegetarian meals packaged food export | 📈 BULL_ANY_MID | 58 | ↑72 | ↓0.994 | ↓2d | SQ | +0.8% | 4.97/1.49 | -2.72% | 20% |
| [BALAMINES](https://in.tradingview.com/chart/?symbol=NSE:BALAMINES)<br><sub>📶W9 · ★ · ↓CMF2d</sub> | ✓ SAFE | Aliphatic amines and specialty chemicals manufacturer for industrial applications | 📈 BULL_ANY_MID | 18 | ↑91 | ↓1.003 | ↓2d | — | +4.1% | -12.87/-16.02 | -1.99% | 20% |
| [INDNIPPON](https://in.tradingview.com/chart/?symbol=NSE:INDNIPPON)<br><sub>📶W9 · W↑14d · ↓CMF10d · ÷DIV</sub> | ✓ SAFE | Electronic ignition systems two-wheeler three-wheeler portable engines | 📈 BULL_ANY_MID | 4 | ↑89 | ↑1.043 | ↑16d | — | +23.6% | 26.29/23.41 | +4.38% | 20% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>📶W9 · W↑34d · ↑CMF30d</sub> | ✓ SAFE | Textiles apparel real estate FMCG engineering diversified conglomerate | 📈 BULL_ANY_MID | 1 | ↑99 | ↑1.157 | ↑19d | — | +92.0% | 77.34/77.23 | +8.00% | 20% |
| [KRBL](https://in.tradingview.com/chart/?symbol=NSE:KRBL)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | Basmati rice processing and export for domestic and global markets | 📈 BULL_ANY_MID | 0 | ↑58 | ↓0.991 | ↓39d | — | +13.4% | -21.62/-22.37 | -1.64% | 20% |
| [CEIGALL](https://in.tradingview.com/chart/?symbol=NSE:CEIGALL)<br><sub>📶W9 · W↑14d · ↑CMF13d</sub> | ✓ SAFE | EPC contractor highways bridges tunnels rail infrastructure | 📈 BULL_ANY_MID | 0 | ↑75 | ↓1.008 | ↑24d | — | +21.7% | 45.55/45.47 | -1.62% | 20% |
| [GODIGIT](https://in.tradingview.com/chart/?symbol=NSE:GODIGIT)<br><sub>W↑4d · RVOL9x · ↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION | Digital motor health travel property insurance platform | 🔥 BULL_OS_PPV | 59 | 🔄4 | ↑1.008 | ↑1d | PV | +2.2% | -68.04/-72.75 | +2.16% | 20% |
| [HGINFRA](https://in.tradingview.com/chart/?symbol=NSE:HGINFRA)<br><sub>RVOL234x · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Road construction and maintenance EPC contractor | 🔥 BULL_OS_PPV | 54 | 🔄3 | ↑1.015 | ↑1d | PV | +3.9% | -56.88/-66.0 | +3.85% | 20% |
| [SANOFI](https://in.tradingview.com/chart/?symbol=NSE:SANOFI)<br><sub>🚀SS · ↓CMF22d</sub> | ⚠ CAUTION | Pharmaceutical diabetes cardiology CNS medicines India | ⚡ BULL_ANY_PPV | 99 | 🔄13 | ↑1.012 | ↑1d | SQ·PV | +2.6% | -43.64/-51.58 | +2.63% | 20% |
| [VTL](https://in.tradingview.com/chart/?symbol=NSE:VTL)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Yarn fabric acrylic fiber garments textiles manufacturer | ⚡ BULL_ANY_PPV | 50 | 🔄57 | ↑0.998 | ↓5d | PV | +0.4% | -51.18/-58.35 | +0.38% | 20% |
| [GILLETTE](https://in.tradingview.com/chart/?symbol=NSE:GILLETTE)<br><sub>↑CMF3d · 🎯SLING</sub> | ⚠ CAUTION | Razor blades shaving cream oral care FMCG grooming | 🟢 BULL_OVERSOLD | 42 | 🔄23 | ↑0.993 | ↓13d | — | -3.5% | -62.96/-63.6 | +0.35% | 20% |
| [IOC](https://in.tradingview.com/chart/?symbol=NSE:IOC)<br><sub>↑CMF11d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 7 | ↑29 | ↓0.993 | ↓13d | — | -2.2% | -55.32/-55.57 | -0.53% | 20% |
| [TRENT](https://in.tradingview.com/chart/?symbol=NSE:TRENT)<br><sub>↓CMF22d · ⚠️TRAP</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 5 | ↑4 | ↑0.994 | ↓28d | — | -6.9% | -57.9/-58.62 | +0.70% | 20% |
| [BRITANNIA](https://in.tradingview.com/chart/?symbol=NSE:BRITANNIA)<br><sub>↓CMF28d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 5 | ↑23 | ↑0.990 | ↓20d | — | -8.3% | -53.05/-54.83 | -0.02% | 20% |
| [ORIENTTECH](https://in.tradingview.com/chart/?symbol=NSE:ORIENTTECH)<br><sub>↓CMF30d</sub> | ✓ SAFE | IT infrastructure cloud digital transformation solutions | 📈 BULL_ANY_MID | 88 | 🔄20 | ↓0.992 | ↓2d | SQ | +0.1% | -31.07/-32.46 | -1.20% | 20% |
| [SAIPARENT](https://in.tradingview.com/chart/?symbol=NSE:SAIPARENT)<br><sub>↓CMF23d</sub> | ✓ SAFE | Injectables manufacturer for hospitals and healthcare providers | 📈 BULL_ANY_MID | 83 | 🔄50 | ↑0.993 | ↓12d | SQ | -2.2% | -45.71/-46.23 | -0.02% | 20% |
| [FMGOETZE](https://in.tradingview.com/chart/?symbol=NSE:FMGOETZE)<br><sub>↑CMF19d</sub> | ✓ SAFE | Pistons rings valves powertrain components automotive suppliers | 📈 BULL_ANY_MID | 35 | 🔄50 | ↑1.019 | ↓24d | — | -0.8% | -14.28/-16.25 | +3.29% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>🚀SS · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 8 | ↑40 | ↑0.999 | ↓17d | — | -1.8% | -39.89/-40.11 | +1.07% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AJAXENGG,NSE:ROTO,NSE:WINDMACHIN,NSE:JAGSNPHARM,NSE:GODREJAGRO,NSE:HDFCLIFE,NSE:SBILIFE,NSE:SEDEMAC,NSE:SIGMAADV,NSE:CIPLA,NSE:KAJARIACER,NSE:SANGAMIND,NSE:ARVIND,NSE:VIPIND,NSE:LALPATHLAB,NSE:SUPRAJIT,NSE:POLYMED,NSE:TATASTEEL,NSE:INDHOTEL,NSE:ASTERDM,NSE:AEROFLEX,NSE:MEESHO,NSE:PNB,NSE:CARTRADE,NSE:TMB,NSE:SHILCTECH,NSE:TASTYBITE,NSE:BALAMINES,NSE:INDNIPPON,NSE:RAYMOND,NSE:KRBL,NSE:CEIGALL,NSE:GODIGIT,NSE:HGINFRA,NSE:SANOFI,NSE:VTL,NSE:GILLETTE,NSE:IOC,NSE:TRENT,NSE:BRITANNIA,NSE:ORIENTTECH,NSE:SAIPARENT,NSE:FMGOETZE,NSE:BPCL
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (24)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [AJAXENGG](https://in.tradingview.com/chart/?symbol=NSE:AJAXENGG)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 99 | 🔄53 | ↑1.006 | ↑1d | SQ·PV | +1.1% | -11.52/-11.61 | +1.06% | 20% |
| [ROTO](https://in.tradingview.com/chart/?symbol=NSE:ROTO)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Progressive cavity pumps for wastewater and sugar industries | ⚡ BULL_ANY_PPV | 99 | 🔄33 | ↑1.006 | ↑1d | SQ·PV | +1.0% | -36.94/-42.43 | +1.01% | 20% |
| [WINDMACHIN](https://in.tradingview.com/chart/?symbol=NSE:WINDMACHIN)<br><sub>📶W9 · ↑CMF30d</sub> | ⚠ CAUTION | Plastic injection moulding pipe extrusion machinery manufacturer | ⚡ BULL_ANY_PPV | 99 | 🔄57 | ↑1.004 | ↑1d | SQ·PV | +1.9% | -32.06/-34.48 | +1.86% | 20% |
| [JAGSNPHARM](https://in.tradingview.com/chart/?symbol=NSE:JAGSNPHARM)<br><sub>📶W9 · 🚀SS·120x · ↑CMF0d</sub> | ✓ SAFE | Women's health and pain management pharmaceutical manufacturer India | ⚡ BULL_ANY_PPV | 89 | 🔄56 | ↑1.053 | ↑1d | SQ·PV | +8.1% | -21.89/-31.08 | +8.13% | 20% |
| [GODREJAGRO](https://in.tradingview.com/chart/?symbol=NSE:GODREJAGRO)<br><sub>📶W9 · W↑29d · ↓CMF17d</sub> | ✓ SAFE | Animal feed, oil palm, crop protection for farmers | ⚡ BULL_ANY_PPV | 63 | ↑66 | ↑1.021 | ↑2d | SQ·PV | +3.4% | 41.81/36.73 | +0.90% | 20% |
| [KAJARIACER](https://in.tradingview.com/chart/?symbol=NSE:KAJARIACER)<br><sub>📶W9 · ↑CMF23d</sub> | ⚠ CAUTION | Ceramic and vitrified tiles manufacturer for construction | 📈 BULL_ANY_MID | 99 | 🔄61 | ↑1.006 | ↑1d | SQ | +0.4% | -25.43/-29.51 | +0.44% | 20% |
| [SANGAMIND](https://in.tradingview.com/chart/?symbol=NSE:SANGAMIND)<br><sub>📶W9 · ↑CMF13d</sub> | ✓ SAFE | PV yarn denim seamless garments textile manufacturer | 📈 BULL_ANY_MID | 99 | 🔄72 | ↑1.007 | ↑1d | SQ | +1.6% | -17.12/-20.13 | +1.55% | 20% |
| [ARVIND](https://in.tradingview.com/chart/?symbol=NSE:ARVIND)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Textiles denim apparel retail vertically integrated manufacturing | 📈 BULL_ANY_MID | 94 | 🔄86 | ↑1.024 | ↑1d | SQ | +3.2% | -5.44/-6.16 | +3.18% | 20% |
| [VIPIND](https://in.tradingview.com/chart/?symbol=NSE:VIPIND)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Luggage and travel bags manufacturer for domestic and international markets | 📈 BULL_ANY_MID | 94 | 🔄18 | ↑1.003 | ↓6d | SQ | +1.1% | -22.45/-22.64 | +0.69% | 20% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>📶W9 · ↓CMF6d</sub> | ✓ SAFE | Diagnostic lab network pathology testing healthcare services | 📈 BULL_ANY_MID | 93 | 🔄78 | ↑1.021 | ↑2d | SQ | +2.7% | 32.6/20.14 | +1.92% | 20% |
| [SUPRAJIT](https://in.tradingview.com/chart/?symbol=NSE:SUPRAJIT)<br><sub>📶W9 · ↓CMF3d</sub> | ⚠ CAUTION | Automotive cables, halogen lamps, mechanical components manufacturer | 📈 BULL_ANY_MID | 90 | 🔄52 | ↑0.999 | ↓5d | SQ | +0.4% | -27.13/-27.23 | +0.33% | 20% |
| [POLYMED](https://in.tradingview.com/chart/?symbol=NSE:POLYMED)<br><sub>📶W9 · ↓CMF13d</sub> | ✓ SAFE | Surgical disposables and medical devices manufacturer for hospitals | 📈 BULL_ANY_MID | 88 | 🔄51 | ↓0.999 | ↓2d | SQ | +1.0% | -19.24/-26.26 | -0.61% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>📶W9 · ↑CMF27d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 69 | ↑47 | ↑1.011 | ↑1d | SQ | +2.3% | -10.62/-12.03 | +2.27% | 20% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>📶W9 · ↑CMF24d</sub> | ⚠ CAUTION | Luxury and midscale hotel brands across Asia Pacific | 📈 BULL_ANY_MID | 69 | ↑48 | ↑1.008 | ↑1d | SQ | +1.6% | -22.75/-27.38 | +1.64% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · W↑30d · ↑CMF30d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.025 | ↑2d | SQ | +6.1% | 49.69/48.04 | -0.06% | 20% 🟦 |
| [PNB](https://in.tradingview.com/chart/?symbol=NSE:PNB)<br><sub>📶W9 · W↑72d · ↓CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | ↑52 | ↓1.004 | ↑2d | SQ | +1.8% | 22.16/15.43 | -0.05% | 20% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Used car marketplace and financing platform India | 📈 BULL_ANY_MID | 58 | ↑76 | ↓1.007 | ↑2d | SQ | +3.3% | -4.77/-7.03 | +0.10% | 20% |
| [TMB](https://in.tradingview.com/chart/?symbol=NSE:TMB)<br><sub>📶W9 · ↑CMF19d</sub> | ⚠ CAUTION | Regional private bank serving retail agriculture MSME segments | 📈 BULL_ANY_MID | 58 | ↑90 | ↓0.993 | ↓2d | SQ | +1.1% | 1.15/-0.52 | -3.02% | 20% |
| [SHILCTECH](https://in.tradingview.com/chart/?symbol=NSE:SHILCTECH)<br><sub>📶W9 · ↓CMF0d</sub> | ✓ SAFE | Distribution and power transformers for industrial electrical systems | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.001 | ↑2d | SQ | +2.3% | -1.6/-4.78 | -1.65% | 20% |
| [OMAXE](https://in.tradingview.com/chart/?symbol=NSE:OMAXE)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Residential commercial real estate developer across Indian cities | 📈 BULL_ANY_MID | 58 | ↓88 | ↓0.987 | ↓2d | SQ | +1.0% | 1.16/1.01 | -4.43% | 20% |
| [TASTYBITE](https://in.tradingview.com/chart/?symbol=NSE:TASTYBITE)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Ready-to-eat ethnic vegetarian meals packaged food export | 📈 BULL_ANY_MID | 58 | ↑72 | ↓0.994 | ↓2d | SQ | +0.8% | 4.97/1.49 | -2.72% | 20% |
| [SANOFI](https://in.tradingview.com/chart/?symbol=NSE:SANOFI)<br><sub>🚀SS · ↓CMF22d</sub> | ⚠ CAUTION | Pharmaceutical diabetes cardiology CNS medicines India | ⚡ BULL_ANY_PPV | 99 | 🔄13 | ↑1.012 | ↑1d | SQ·PV | +2.6% | -43.64/-51.58 | +2.63% | 20% |
| [ORIENTTECH](https://in.tradingview.com/chart/?symbol=NSE:ORIENTTECH)<br><sub>↓CMF30d</sub> | ✓ SAFE | IT infrastructure cloud digital transformation solutions | 📈 BULL_ANY_MID | 88 | 🔄20 | ↓0.992 | ↓2d | SQ | +0.1% | -31.07/-32.46 | -1.20% | 20% |
| [SAIPARENT](https://in.tradingview.com/chart/?symbol=NSE:SAIPARENT)<br><sub>↓CMF23d</sub> | ✓ SAFE | Injectables manufacturer for hospitals and healthcare providers | 📈 BULL_ANY_MID | 83 | 🔄50 | ↑0.993 | ↓12d | SQ | -2.2% | -45.71/-46.23 | -0.02% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AJAXENGG,NSE:ROTO,NSE:WINDMACHIN,NSE:JAGSNPHARM,NSE:GODREJAGRO,NSE:KAJARIACER,NSE:SANGAMIND,NSE:ARVIND,NSE:VIPIND,NSE:LALPATHLAB,NSE:SUPRAJIT,NSE:POLYMED,NSE:TATASTEEL,NSE:INDHOTEL,NSE:MEESHO,NSE:PNB,NSE:CARTRADE,NSE:TMB,NSE:SHILCTECH,NSE:OMAXE,NSE:TASTYBITE,NSE:SANOFI,NSE:ORIENTTECH,NSE:SAIPARENT
```

---

### 🔥 MAJOR — PPV confirmed (8)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>📶W9 · W↑3d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 19 | ↑14 | ↑1.042 | ↑1d | PV | +5.0% | -31.89/-43.91 | +5.05% | 20% |
| [SBILIFE](https://in.tradingview.com/chart/?symbol=NSE:SBILIFE)<br><sub>📶W9 · ↓CMF16d · 🎯SLING</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 19 | ↑36 | ↑1.031 | ↑1d | PV | +4.2% | -50.09/-59.33 | +4.19% | 20% |
| [SEDEMAC](https://in.tradingview.com/chart/?symbol=NSE:SEDEMAC)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Engine control electronics for automotive and off-highway vehicles | ⚡ BULL_ANY_PPV | 13 | ↑50 | ↑1.077 | ↑7d | PV | +13.1% | 26.54/19.32 | +8.23% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GODIGIT](https://in.tradingview.com/chart/?symbol=NSE:GODIGIT)<br><sub>W↑4d · RVOL9x · ↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION | Digital motor health travel property insurance platform | 🔥 BULL_OS_PPV | 59 | 🔄4 | ↑1.008 | ↑1d | PV | +2.2% | -68.04/-72.75 | +2.16% | 20% |
| [HGINFRA](https://in.tradingview.com/chart/?symbol=NSE:HGINFRA)<br><sub>RVOL234x · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Road construction and maintenance EPC contractor | 🔥 BULL_OS_PPV | 54 | 🔄3 | ↑1.015 | ↑1d | PV | +3.9% | -56.88/-66.0 | +3.85% | 20% |
| [ABREL](https://in.tradingview.com/chart/?symbol=NSE:ABREL)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Residential commercial real estate developer urban projects | 🔥 BULL_OS_PPV | 5 | ↓16 | ↑0.972 | ↓24d | PV | -13.8% | -66.43/-66.67 | +0.45% | 20% |
| [VTL](https://in.tradingview.com/chart/?symbol=NSE:VTL)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Yarn fabric acrylic fiber garments textiles manufacturer | ⚡ BULL_ANY_PPV | 50 | 🔄57 | ↑0.998 | ↓5d | PV | +0.4% | -51.18/-58.35 | +0.38% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:HDFCLIFE,NSE:SBILIFE,NSE:SEDEMAC,NSE:SIGMAADV,NSE:GODIGIT,NSE:HGINFRA,NSE:ABREL,NSE:VTL
```

### 🟢 OVERSOLD — reversal from −53/−60 (15)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CIPLA](https://in.tradingview.com/chart/?symbol=NSE:CIPLA)<br><sub>📶W9 · 🚀SS · ↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 10 | ↑41 | ↑1.005 | ↓37d | — | -1.7% | -61.96/-65.24 | +1.99% | 20% |
| [GILLETTE](https://in.tradingview.com/chart/?symbol=NSE:GILLETTE)<br><sub>↑CMF3d · 🎯SLING</sub> | ⚠ CAUTION | Razor blades shaving cream oral care FMCG grooming | 🟢 BULL_OVERSOLD | 42 | 🔄23 | ↑0.993 | ↓13d | — | -3.5% | -62.96/-63.6 | +0.35% | 20% |
| [GOKEX](https://in.tradingview.com/chart/?symbol=NSE:GOKEX)<br><sub>↓CMF21d · ⚠️TRAP</sub> | ✓ SAFE | Apparel manufacturer for global fashion brands and retailers | 🟢 BULL_OVERSOLD | 10 | ↓24 | ↓0.958 | ↓10d | — | -10.5% | -73.98/-74.71 | -2.45% | 20% 🟦 |
| [FAZE3Q](https://in.tradingview.com/chart/?symbol=NSE:FAZE3Q)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 6 | ↓15 | ↓0.947 | ↓14d | — | -14.6% | -69.54/-70.14 | -3.66% | 20% |
| [MARUTI](https://in.tradingview.com/chart/?symbol=NSE:MARUTI)<br><sub>↓CMF14d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 5 | ↓21 | ↑0.986 | ↓38d | — | -7.9% | -68.17/-68.97 | +1.78% | 20% |
| [ASIANPAINT](https://in.tradingview.com/chart/?symbol=NSE:ASIANPAINT)<br><sub>🚀SS · ↑CMF30d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 5 | ↓34 | ↑0.988 | ↓26d | — | -10.5% | -65.89/-66.6 | +1.32% | 20% |
| [BUTTERFLY](https://in.tradingview.com/chart/?symbol=NSE:BUTTERFLY)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 5 | ↓19 | ↑0.981 | ↓60d+ | — | -20.3% | -63.83/-64.07 | +0.41% | 20% |
| [CENTURYPLY](https://in.tradingview.com/chart/?symbol=NSE:CENTURYPLY)<br><sub>↓CMF30d · ⚠️TRAP · ÷DIV</sub> | ⚠ CAUTION | Plywood laminates MDF boards residential commercial construction | 🟢 BULL_OVERSOLD | 0 | ↓28 | ↓0.975 | ↓26d | — | -7.1% | -69.7/-69.74 | -2.48% | 20% |
| [ADANIENSOL](https://in.tradingview.com/chart/?symbol=NSE:ADANIENSOL)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 10 | ↓75 | ↑0.987 | ↓15d | — | -12.5% | -58.7/-59.55 | +1.85% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>↓CMF11d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 7 | ↓53 | ↓0.988 | ↓13d | — | -5.3% | -57.62/-58.54 | -0.51% | 20% |
| [IOC](https://in.tradingview.com/chart/?symbol=NSE:IOC)<br><sub>↑CMF11d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 7 | ↑29 | ↓0.993 | ↓13d | — | -2.2% | -55.32/-55.57 | -0.53% | 20% |
| [M&M](https://in.tradingview.com/chart/?symbol=NSE:M&M)<br><sub>↓CMF13d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 5 | ↓34 | ↑0.986 | ↓45d | — | +0.1% | -54.94/-55.48 | +0.52% | 20% |
| [TRENT](https://in.tradingview.com/chart/?symbol=NSE:TRENT)<br><sub>↓CMF22d · ⚠️TRAP</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 5 | ↑4 | ↑0.994 | ↓28d | — | -6.9% | -57.9/-58.62 | +0.70% | 20% |
| [MAZDOCK](https://in.tradingview.com/chart/?symbol=NSE:MAZDOCK)<br><sub>↓CMF12d · 🎯SLING</sub> | ✓ SAFE | Defence warships submarines naval military shipbuilding PSU | 🟡 BULL_OS_L2 | 5 | ↓20 | ↑0.974 | ↓39d | — | -5.0% | -54.35/-54.36 | -0.43% | 20% |
| [BRITANNIA](https://in.tradingview.com/chart/?symbol=NSE:BRITANNIA)<br><sub>↓CMF28d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 5 | ↑23 | ↑0.990 | ↓20d | — | -8.3% | -53.05/-54.83 | -0.02% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CIPLA,NSE:GILLETTE,NSE:GOKEX,NSE:FAZE3Q,NSE:MARUTI,NSE:ASIANPAINT,NSE:BUTTERFLY,NSE:CENTURYPLY,NSE:ADANIENSOL,NSE:NESTLEIND,NSE:IOC,NSE:M&M,NSE:TRENT,NSE:MAZDOCK,NSE:BRITANNIA
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (10)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ASTERDM](https://in.tradingview.com/chart/?symbol=NSE:ASTERDM)<br><sub>📶W9 · ↑CMF1d</sub> | ✓ SAFE | Multi-specialty hospitals and clinics, India healthcare | 📈 BULL_ANY_MID | 59 | 🔄62 | ↑1.011 | ↑1d | — | +1.1% | -23.29/-28.36 | +1.13% | 20% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Stainless steel corrugated hoses assemblies fittings industrial applications | 📈 BULL_ANY_MID | 59 | 🔄96 | ↑1.009 | ↑1d | — | +1.2% | 9.75/8.33 | +1.23% | 10% 🟨 |
| [BALAMINES](https://in.tradingview.com/chart/?symbol=NSE:BALAMINES)<br><sub>📶W9 · ★ · ↓CMF2d</sub> | ✓ SAFE | Aliphatic amines and specialty chemicals manufacturer for industrial applications | 📈 BULL_ANY_MID | 18 | ↑91 | ↓1.003 | ↓2d | — | +4.1% | -12.87/-16.02 | -1.99% | 20% |
| [INDNIPPON](https://in.tradingview.com/chart/?symbol=NSE:INDNIPPON)<br><sub>📶W9 · W↑14d · ↓CMF10d · ÷DIV</sub> | ✓ SAFE | Electronic ignition systems two-wheeler three-wheeler portable engines | 📈 BULL_ANY_MID | 4 | ↑89 | ↑1.043 | ↑16d | — | +23.6% | 26.29/23.41 | +4.38% | 20% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>📶W9 · W↑34d · ↑CMF30d</sub> | ✓ SAFE | Textiles apparel real estate FMCG engineering diversified conglomerate | 📈 BULL_ANY_MID | 1 | ↑99 | ↑1.157 | ↑19d | — | +92.0% | 77.34/77.23 | +8.00% | 20% |
| [KRBL](https://in.tradingview.com/chart/?symbol=NSE:KRBL)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | Basmati rice processing and export for domestic and global markets | 📈 BULL_ANY_MID | 0 | ↑58 | ↓0.991 | ↓39d | — | +13.4% | -21.62/-22.37 | -1.64% | 20% |
| [CEIGALL](https://in.tradingview.com/chart/?symbol=NSE:CEIGALL)<br><sub>📶W9 · W↑14d · ↑CMF13d</sub> | ✓ SAFE | EPC contractor highways bridges tunnels rail infrastructure | 📈 BULL_ANY_MID | 0 | ↑75 | ↓1.008 | ↑24d | — | +21.7% | 45.55/45.47 | -1.62% | 20% |
| [FMGOETZE](https://in.tradingview.com/chart/?symbol=NSE:FMGOETZE)<br><sub>↑CMF19d</sub> | ✓ SAFE | Pistons rings valves powertrain components automotive suppliers | 📈 BULL_ANY_MID | 35 | 🔄50 | ↑1.019 | ↓24d | — | -0.8% | -14.28/-16.25 | +3.29% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>🚀SS · ↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 8 | ↑40 | ↑0.999 | ↓17d | — | -1.8% | -39.89/-40.11 | +1.07% | 20% |
| [GENUSPOWER](https://in.tradingview.com/chart/?symbol=NSE:GENUSPOWER)<br><sub>↓CMF5d</sub> | ✓ SAFE | Smart meters and distribution infrastructure for utilities | 📈 BULL_ANY_MID | 3 | ↓54 | ↓0.983 | ↓17d | — | -6.5% | -33.64/-34.33 | -0.57% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ASTERDM,NSE:AEROFLEX,NSE:BALAMINES,NSE:INDNIPPON,NSE:RAYMOND,NSE:KRBL,NSE:CEIGALL,NSE:FMGOETZE,NSE:BPCL,NSE:GENUSPOWER
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
