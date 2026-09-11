> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-09-11
*Generated 2026-09-11 15:45 IST*

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

**Total bull crosses today: 48** · 15 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MAXHEALTH,NSE:KIRLOSIND,NSE:DYNAMATECH,NSE:ABDL,NSE:INDUSTOWER,NSE:AIIL,NSE:AWFIS,NSE:CONCORDBIO,NSE:TVSSCS,NSE:FILATEX,NSE:BLACKBUCK,NSE:INDOCO,NSE:BIRLACABLE,NSE:SIGMAADV,NSE:HINDALCO,NSE:PVRINOX,NSE:TASTYBITE,NSE:PNBHOUSING,NSE:TORNTPHARM,NSE:KPIL,NSE:EIMCOELECO,NSE:HINDZINC,NSE:ADANIENT,NSE:ATHERENERG,NSE:BOSCHLTD,NSE:BIRLANU,NSE:SEDEMAC,NSE:MEESHO,NSE:WAAREEENER,NSE:DRREDDY,NSE:SUNTV,NSE:CUMMINSIND,NSE:VOLTAS,NSE:AURIONPRO,NSE:HINDPETRO,NSE:ICICIGI,NSE:AUTOAXLES,NSE:PROTEAN,NSE:OLECTRA,NSE:ADANIGREEN,NSE:SCHNEIDER,NSE:MASFIN,NSE:JARO,NSE:NINSYS,NSE:RATEGAIN,NSE:CREDITACC,NSE:EQUITASBNK,NSE:ZFCVINDIA
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (28)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MAXHEALTH](https://in.tradingview.com/chart/?symbol=NSE:MAXHEALTH)<br><sub>📶W9 · ↑CMF9d</sub> | ⚠ CAUTION | Tertiary quaternary hospital network Delhi NCR North India | ⚡ BULL_ANY_PPV | 89 | 🔄37 | ↑1.030 | ↑1d | SQ·PV | +4.5% | -32.15/-41.06 | +4.48% | 20% |
| [KIRLOSIND](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSIND)<br><sub>📶W9 · RVOL176x · ↑CMF0d</sub> | ✓ SAFE | Holding company: castings, wind power, real estate investments | ⚡ BULL_ANY_PPV | 89 | 🔄62 | ↑1.033 | ↑1d | SQ·PV | +7.0% | -37.28/-42.15 | +7.03% | 20% |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH)<br><sub>📶W9 · W↑30d · ↑CMF0d</sub> | ✓ SAFE | Aerospace hydraulics pumps and automotive turbochargers manufacturer | ⚡ BULL_ANY_PPV | 59 | ↑81 | ↑1.037 | ↑1d | SQ·PV | +4.8% | 36.95/30.22 | +4.80% | 20% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>📶W9 · W↑5d · ↑CMF25d</sub> | ✓ SAFE | Spirits manufacturer, IMFL exporter, Indian domestic and export markets | ⚡ BULL_ANY_PPV | 58 | ↑62 | ↑1.034 | ↑2d | SQ·PV | +4.7% | -13.87/-26.31 | +3.44% | 10% 🟩 |
| [INDUSTOWER](https://in.tradingview.com/chart/?symbol=NSE:INDUSTOWER)<br><sub>📶W9 · W↑5d · ↑CMF8d</sub> | ✓ SAFE | Telecom tower infrastructure operator serving mobile networks | ⚡ BULL_ANY_PPV | 54 | 🔄33 | ↑1.025 | ↑1d | PV | +4.3% | -30.53/-37.66 | +4.30% | 20% |
| [AIIL](https://in.tradingview.com/chart/?symbol=NSE:AIIL)<br><sub>📶W9 · RVOL15x · ↑CMF0d</sub> | ✓ SAFE | NBFC providing investment loans advances securities financing | ⚡ BULL_ANY_PPV | 54 | 🔄43 | ↑1.029 | ↑1d | PV | +6.3% | -38.03/-42.32 | +6.26% | 20% |
| [AWFIS](https://in.tradingview.com/chart/?symbol=NSE:AWFIS)<br><sub>📶W9 · W↑5d · RVOL82x · ↑CMF0d</sub> | ✓ SAFE | Flexible workspace operator for professionals and corporates | ⚡ BULL_ANY_PPV | 49 | 🔄11 | ↑1.114 | ↑1d | PV | +17.5% | -37.66/-50.77 | +17.47% | 20% |
| [CONCORDBIO](https://in.tradingview.com/chart/?symbol=NSE:CONCORDBIO)<br><sub>📶W9 · W↑108d · ↑CMF3d</sub> | ✓ SAFE | Fermentation APIs immunosuppressants oncology biopharmaceutical manufacturer | ⚡ BULL_ANY_PPV | 24 | ↑57 | ↑1.024 | ↑1d | PV | +3.6% | -2.13/-5.04 | +3.64% | 20% |
| [TVSSCS](https://in.tradingview.com/chart/?symbol=NSE:TVSSCS)<br><sub>📶W9 · ↑CMF14d · ÷DIV</sub> | ✓ SAFE | Supply chain logistics management for automotive and industrial sectors | ⚡ BULL_ANY_PPV | 23 | ↑54 | ↑1.017 | ↑2d | PV | +4.7% | -10.2/-16.04 | +1.37% | 10% 🟩 |
| [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX)<br><sub>📶W9 · RVOL17x · ↑CMF30d</sub> | ✓ SAFE | Polyester yarn and chip manufacturer for textiles | ⚡ BULL_ANY_PPV | 19 | ↑94 | ↑1.111 | ↑1d | PV | +14.6% | -2.49/-14.73 | +14.64% | 20% |
| [BLACKBUCK](https://in.tradingview.com/chart/?symbol=NSE:BLACKBUCK)<br><sub>📶W9 · W↑30d · ↑CMF17d</sub> | ✓ SAFE | Digital trucking platform: loads, payments, telematics, financing | ⚡ BULL_ANY_PPV | 19 | ↑55 | ↑1.060 | ↑1d | PV | +7.2% | 12.39/1.43 | +7.21% | 20% |
| [INDOCO](https://in.tradingview.com/chart/?symbol=NSE:INDOCO)<br><sub>📶W9 · W↑10d · ↑CMF11d</sub> | ✓ SAFE | Pharmaceutical manufacturer oral drugs dermatology gastrointestinal India | ⚡ BULL_ANY_PPV | 18 | ↑61 | ↑1.050 | ↑2d | PV | +13.8% | 37.18/36.83 | +3.45% | 20% |
| [BIRLACABLE](https://in.tradingview.com/chart/?symbol=NSE:BIRLACABLE)<br><sub>📶W9 · W↑30d · ↑CMF30d</sub> | ✓ SAFE | Telecom cables, wires, specialized cables manufacturer | ⚡ BULL_ANY_PPV | 8 | ↑98 | ↑1.115 | ↑12d | PV | +46.6% | 66.97/66.15 | +4.72% | 5% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 91 | 🔄60 | ↑1.003 | ↓9d | SQ | -0.3% | -18.92/-20.04 | +1.17% | 20% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>📶W9 · W↑55d · ↓CMF14d</sub> | ✓ SAFE | Multiplex cinema exhibition chain, entertainment venues | 📈 BULL_ANY_MID | 63 | ↑72 | ↑1.019 | ↑2d | SQ | +5.8% | 16.99/14.58 | +1.29% | 20% |
| [TASTYBITE](https://in.tradingview.com/chart/?symbol=NSE:TASTYBITE)<br><sub>📶W9 · W↑113d · ↑CMF20d</sub> | ✓ SAFE | Ready-to-eat ethnic vegetarian meals packaged food export | 📈 BULL_ANY_MID | 63 | ↑76 | ↑1.024 | ↑2d | SQ | +4.6% | 29.41/21.76 | +0.71% | 20% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>📶W9 · W↑30d · ★ · ↑CMF30d</sub> | ✓ SAFE | Housing loans for retail homebuyers and property | 📈 BULL_ANY_MID | 58 | ↑80 | ↓1.011 | ↑2d | SQ | +3.2% | 20.92/18.82 | -0.01% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑68 | ↓0.997 | ↓2d | SQ | +0.2% | -3.46/-4.79 | -0.71% | 20% |
| [KPIL](https://in.tradingview.com/chart/?symbol=NSE:KPIL)<br><sub>📶W9 · W↑25d · ↓CMF22d</sub> | ⚠ CAUTION | Power transmission EPC projects for utilities and infrastructure | 📈 BULL_ANY_MID | 40 | ↑64 | ↓1.015 | ↑26d | SQ | +10.9% | 44.67/42.44 | +0.26% | 20% |
| [EIMCOELECO](https://in.tradingview.com/chart/?symbol=NSE:EIMCOELECO)<br><sub>📶W9 · W↑65d · ↑CMF20d</sub> | ✓ SAFE | Underground mining equipment manufacturer for coal sector | 📈 BULL_ANY_MID | 40 | ↑85 | ↑1.033 | ↑22d | SQ | +29.6% | 50.62/49.22 | +1.49% | 20% |
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>📶W9 · W↑28d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 28 | ↑64 | ↑1.014 | ↑2d | — | +2.7% | 24.78/23.85 | +1.56% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · ↓CMF7d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 19 | ↑76 | ↑1.039 | ↑1d | — | +5.1% | -9.05/-16.39 | +5.11% | 20% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Premium electric scooters, charging network, urban mobility | 📈 BULL_ANY_MID | 18 | ↑98 | ↓1.027 | ↑2d | — | +4.8% | 46.09/44.45 | -0.14% | 20% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>📶W9 · W↑109d · ↑CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 17 | ↑78 | ↓1.015 | ↑3d | — | +4.4% | 32.49/29.43 | +0.17% | 20% |
| [BIRLANU](https://in.tradingview.com/chart/?symbol=NSE:BIRLANU)<br><sub>📶W9 · ↓CMF5d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 10 | ↑36 | ↑1.003 | ↓30d | — | +8.5% | -26.99/-27.85 | +0.96% | 20% |
| [SEDEMAC](https://in.tradingview.com/chart/?symbol=NSE:SEDEMAC)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE | Engine control electronics for automotive and off-highway vehicles | 📈 BULL_ANY_MID | 7 | ↑50 | ↓0.999 | ↓13d | — | -4.9% | -19.71/-21.04 | -0.50% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · 🚀SS · ↑CMF29d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 0 | ↑50 | ↑1.036 | ↑24d | — | +16.7% | 57.53/55.6 | +3.13% | 20% 🟦 |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MAXHEALTH,NSE:KIRLOSIND,NSE:DYNAMATECH,NSE:ABDL,NSE:INDUSTOWER,NSE:AIIL,NSE:AWFIS,NSE:CONCORDBIO,NSE:TVSSCS,NSE:FILATEX,NSE:BLACKBUCK,NSE:INDOCO,NSE:BIRLACABLE,NSE:SIGMAADV,NSE:HINDALCO,NSE:PVRINOX,NSE:TASTYBITE,NSE:PNBHOUSING,NSE:TORNTPHARM,NSE:KPIL,NSE:EIMCOELECO,NSE:HINDZINC,NSE:ADANIENT,NSE:ATHERENERG,NSE:BOSCHLTD,NSE:BIRLANU,NSE:SEDEMAC,NSE:MEESHO
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (43)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MAXHEALTH](https://in.tradingview.com/chart/?symbol=NSE:MAXHEALTH)<br><sub>📶W9 · ↑CMF9d</sub> | ⚠ CAUTION | Tertiary quaternary hospital network Delhi NCR North India | ⚡ BULL_ANY_PPV | 89 | 🔄37 | ↑1.030 | ↑1d | SQ·PV | +4.5% | -32.15/-41.06 | +4.48% | 20% |
| [KIRLOSIND](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSIND)<br><sub>📶W9 · RVOL176x · ↑CMF0d</sub> | ✓ SAFE | Holding company: castings, wind power, real estate investments | ⚡ BULL_ANY_PPV | 89 | 🔄62 | ↑1.033 | ↑1d | SQ·PV | +7.0% | -37.28/-42.15 | +7.03% | 20% |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH)<br><sub>📶W9 · W↑30d · ↑CMF0d</sub> | ✓ SAFE | Aerospace hydraulics pumps and automotive turbochargers manufacturer | ⚡ BULL_ANY_PPV | 59 | ↑81 | ↑1.037 | ↑1d | SQ·PV | +4.8% | 36.95/30.22 | +4.80% | 20% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>📶W9 · W↑5d · ↑CMF25d</sub> | ✓ SAFE | Spirits manufacturer, IMFL exporter, Indian domestic and export markets | ⚡ BULL_ANY_PPV | 58 | ↑62 | ↑1.034 | ↑2d | SQ·PV | +4.7% | -13.87/-26.31 | +3.44% | 10% 🟩 |
| [INDUSTOWER](https://in.tradingview.com/chart/?symbol=NSE:INDUSTOWER)<br><sub>📶W9 · W↑5d · ↑CMF8d</sub> | ✓ SAFE | Telecom tower infrastructure operator serving mobile networks | ⚡ BULL_ANY_PPV | 54 | 🔄33 | ↑1.025 | ↑1d | PV | +4.3% | -30.53/-37.66 | +4.30% | 20% |
| [AIIL](https://in.tradingview.com/chart/?symbol=NSE:AIIL)<br><sub>📶W9 · RVOL15x · ↑CMF0d</sub> | ✓ SAFE | NBFC providing investment loans advances securities financing | ⚡ BULL_ANY_PPV | 54 | 🔄43 | ↑1.029 | ↑1d | PV | +6.3% | -38.03/-42.32 | +6.26% | 20% |
| [AWFIS](https://in.tradingview.com/chart/?symbol=NSE:AWFIS)<br><sub>📶W9 · W↑5d · RVOL82x · ↑CMF0d</sub> | ✓ SAFE | Flexible workspace operator for professionals and corporates | ⚡ BULL_ANY_PPV | 49 | 🔄11 | ↑1.114 | ↑1d | PV | +17.5% | -37.66/-50.77 | +17.47% | 20% |
| [CONCORDBIO](https://in.tradingview.com/chart/?symbol=NSE:CONCORDBIO)<br><sub>📶W9 · W↑108d · ↑CMF3d</sub> | ✓ SAFE | Fermentation APIs immunosuppressants oncology biopharmaceutical manufacturer | ⚡ BULL_ANY_PPV | 24 | ↑57 | ↑1.024 | ↑1d | PV | +3.6% | -2.13/-5.04 | +3.64% | 20% |
| [TVSSCS](https://in.tradingview.com/chart/?symbol=NSE:TVSSCS)<br><sub>📶W9 · ↑CMF14d · ÷DIV</sub> | ✓ SAFE | Supply chain logistics management for automotive and industrial sectors | ⚡ BULL_ANY_PPV | 23 | ↑54 | ↑1.017 | ↑2d | PV | +4.7% | -10.2/-16.04 | +1.37% | 10% 🟩 |
| [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX)<br><sub>📶W9 · RVOL17x · ↑CMF30d</sub> | ✓ SAFE | Polyester yarn and chip manufacturer for textiles | ⚡ BULL_ANY_PPV | 19 | ↑94 | ↑1.111 | ↑1d | PV | +14.6% | -2.49/-14.73 | +14.64% | 20% |
| [BLACKBUCK](https://in.tradingview.com/chart/?symbol=NSE:BLACKBUCK)<br><sub>📶W9 · W↑30d · ↑CMF17d</sub> | ✓ SAFE | Digital trucking platform: loads, payments, telematics, financing | ⚡ BULL_ANY_PPV | 19 | ↑55 | ↑1.060 | ↑1d | PV | +7.2% | 12.39/1.43 | +7.21% | 20% |
| [INDOCO](https://in.tradingview.com/chart/?symbol=NSE:INDOCO)<br><sub>📶W9 · W↑10d · ↑CMF11d</sub> | ✓ SAFE | Pharmaceutical manufacturer oral drugs dermatology gastrointestinal India | ⚡ BULL_ANY_PPV | 18 | ↑61 | ↑1.050 | ↑2d | PV | +13.8% | 37.18/36.83 | +3.45% | 20% |
| [BIRLACABLE](https://in.tradingview.com/chart/?symbol=NSE:BIRLACABLE)<br><sub>📶W9 · W↑30d · ↑CMF30d</sub> | ✓ SAFE | Telecom cables, wires, specialized cables manufacturer | ⚡ BULL_ANY_PPV | 8 | ↑98 | ↑1.115 | ↑12d | PV | +46.6% | 66.97/66.15 | +4.72% | 5% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 91 | 🔄60 | ↑1.003 | ↓9d | SQ | -0.3% | -18.92/-20.04 | +1.17% | 20% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>📶W9 · W↑55d · ↓CMF14d</sub> | ✓ SAFE | Multiplex cinema exhibition chain, entertainment venues | 📈 BULL_ANY_MID | 63 | ↑72 | ↑1.019 | ↑2d | SQ | +5.8% | 16.99/14.58 | +1.29% | 20% |
| [TASTYBITE](https://in.tradingview.com/chart/?symbol=NSE:TASTYBITE)<br><sub>📶W9 · W↑113d · ↑CMF20d</sub> | ✓ SAFE | Ready-to-eat ethnic vegetarian meals packaged food export | 📈 BULL_ANY_MID | 63 | ↑76 | ↑1.024 | ↑2d | SQ | +4.6% | 29.41/21.76 | +0.71% | 20% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>📶W9 · W↑30d · ★ · ↑CMF30d</sub> | ✓ SAFE | Housing loans for retail homebuyers and property | 📈 BULL_ANY_MID | 58 | ↑80 | ↓1.011 | ↑2d | SQ | +3.2% | 20.92/18.82 | -0.01% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑68 | ↓0.997 | ↓2d | SQ | +0.2% | -3.46/-4.79 | -0.71% | 20% |
| [KPIL](https://in.tradingview.com/chart/?symbol=NSE:KPIL)<br><sub>📶W9 · W↑25d · ↓CMF22d</sub> | ⚠ CAUTION | Power transmission EPC projects for utilities and infrastructure | 📈 BULL_ANY_MID | 40 | ↑64 | ↓1.015 | ↑26d | SQ | +10.9% | 44.67/42.44 | +0.26% | 20% |
| [EIMCOELECO](https://in.tradingview.com/chart/?symbol=NSE:EIMCOELECO)<br><sub>📶W9 · W↑65d · ↑CMF20d</sub> | ✓ SAFE | Underground mining equipment manufacturer for coal sector | 📈 BULL_ANY_MID | 40 | ↑85 | ↑1.033 | ↑22d | SQ | +29.6% | 50.62/49.22 | +1.49% | 20% |
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>📶W9 · W↑28d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 28 | ↑64 | ↑1.014 | ↑2d | — | +2.7% | 24.78/23.85 | +1.56% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · ↓CMF7d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 19 | ↑76 | ↑1.039 | ↑1d | — | +5.1% | -9.05/-16.39 | +5.11% | 20% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Premium electric scooters, charging network, urban mobility | 📈 BULL_ANY_MID | 18 | ↑98 | ↓1.027 | ↑2d | — | +4.8% | 46.09/44.45 | -0.14% | 20% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>📶W9 · W↑109d · ↑CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 17 | ↑78 | ↓1.015 | ↑3d | — | +4.4% | 32.49/29.43 | +0.17% | 20% |
| [BIRLANU](https://in.tradingview.com/chart/?symbol=NSE:BIRLANU)<br><sub>📶W9 · ↓CMF5d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 10 | ↑36 | ↑1.003 | ↓30d | — | +8.5% | -26.99/-27.85 | +0.96% | 20% |
| [SEDEMAC](https://in.tradingview.com/chart/?symbol=NSE:SEDEMAC)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE | Engine control electronics for automotive and off-highway vehicles | 📈 BULL_ANY_MID | 7 | ↑50 | ↓0.999 | ↓13d | — | -4.9% | -19.71/-21.04 | -0.50% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · 🚀SS · ↑CMF29d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 0 | ↑50 | ↑1.036 | ↑24d | — | +16.7% | 57.53/55.6 | +3.13% | 20% 🟦 |
| [WAAREEENER](https://in.tradingview.com/chart/?symbol=NSE:WAAREEENER)<br><sub>↓CMF11d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Solar photovoltaic modules manufacturing renewable energy sector | 🔥 BULL_OS_PPV | 59 | 🔄17 | ↑1.011 | ↑1d | PV | +3.0% | -59.58/-61.27 | +3.02% | 20% |
| [DRREDDY](https://in.tradingview.com/chart/?symbol=NSE:DRREDDY)<br><sub>↑CMF0d</sub> | ⚠ CAUTION | Generics, APIs, biosimilars for global emerging markets | ⚡ BULL_ANY_PPV | 59 | 🔄25 | ↑1.008 | ↑1d | PV | +2.0% | -41.95/-43.92 | +1.97% | 20% |
| [SUNTV](https://in.tradingview.com/chart/?symbol=NSE:SUNTV)<br><sub>RVOL9x · ↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Regional Tamil broadcaster, entertainment content, South India | ⚡ BULL_ANY_PPV | 54 | 🔄20 | ↑1.028 | ↑1d | PV | +4.5% | -46.93/-55.1 | +4.49% | 20% |
| [CUMMINSIND](https://in.tradingview.com/chart/?symbol=NSE:CUMMINSIND)<br><sub>↑CMF1d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 59 | 🔄53 | ↑1.012 | ↑1d | — | +2.7% | -56.42/-62.44 | +2.68% | 20% |
| [VOLTAS](https://in.tradingview.com/chart/?symbol=NSE:VOLTAS)<br><sub>↓CMF24d · 🎯SLING</sub> | ✓ SAFE | AC units, refrigeration, EPC projects, cooling systems | 🟢 BULL_OVERSOLD | 35 | 🔄15 | ↑0.994 | ↓21d | — | -9.7% | -60.89/-63.2 | +0.56% | 20% |
| [AURIONPRO](https://in.tradingview.com/chart/?symbol=NSE:AURIONPRO)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Digital banking platforms payments mobility government sectors | 🟢 BULL_OVERSOLD | 35 | 🔄2 | ↑0.999 | ↓46d | — | -18.5% | -59.45/-60.98 | +1.45% | 20% |
| [AUTOAXLES](https://in.tradingview.com/chart/?symbol=NSE:AUTOAXLES)<br><sub>↓CMF9d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 35 | 🔄32 | ↑0.995 | ↓30d | — | -6.8% | -57.66/-58.45 | +1.21% | 20% |
| [SCHNEIDER](https://in.tradingview.com/chart/?symbol=NSE:SCHNEIDER)<br><sub>↑CMF1d</sub> | ✓ SAFE | Power distribution equipment manufacturing and servicing | 📈 BULL_ANY_MID | 99 | 🔄77 | ↑1.015 | ↑1d | SQ | +2.7% | -20.87/-23.06 | +2.69% | 10% 🟩 |
| [MASFIN](https://in.tradingview.com/chart/?symbol=NSE:MASFIN)<br><sub>↑CMF2d</sub> | ✓ SAFE | Retail NBFC financing MSMEs home loans two-wheelers used cars | 📈 BULL_ANY_MID | 69 | ↑33 | ↑1.004 | ↑1d | SQ | +0.5% | -46.13/-48.6 | +0.51% | 20% |
| [JARO](https://in.tradingview.com/chart/?symbol=NSE:JARO)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Online higher education platform, executive training, career advancement | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.008 | ↑2d | SQ | +3.7% | -25.89/-31.28 | -0.48% | 20% |
| [NINSYS](https://in.tradingview.com/chart/?symbol=NSE:NINSYS)<br><sub>🚀SS · ↓CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 45 | ↑89 | ↑0.999 | ↓60d+ | SQ | +2.3% | -41.2/-42.09 | +0.32% | 5% |
| [RATEGAIN](https://in.tradingview.com/chart/?symbol=NSE:RATEGAIN)<br><sub>↓CMF26d</sub> | ✓ SAFE | Hotel distribution and revenue management software for hospitality | 📈 BULL_ANY_MID | 43 | 🔄77 | ↑1.001 | ↓17d | — | -5.6% | -44.44/-46.17 | +1.36% | 20% |
| [CREDITACC](https://in.tradingview.com/chart/?symbol=NSE:CREDITACC)<br><sub>↓CMF14d</sub> | ✓ SAFE | Microfinance loans for rural women, NBFC sector | 📈 BULL_ANY_MID | 40 | 🔄55 | ↑1.003 | ↓36d | — | -5.3% | -42.54/-43.69 | +1.50% | 20% |
| [EQUITASBNK](https://in.tradingview.com/chart/?symbol=NSE:EQUITASBNK)<br><sub>↓CMF10d</sub> | ⚠ CAUTION | Small finance bank serving underbanked individuals and SMEs | 📈 BULL_ANY_MID | 38 | 🔄63 | ↑0.999 | ↓17d | — | -2.1% | -49.5/-49.64 | +0.72% | 20% |
| [ZFCVINDIA](https://in.tradingview.com/chart/?symbol=NSE:ZFCVINDIA)<br><sub>W↑15d · ↓CMF10d</sub> | ⚠ CAUTION | Braking systems control tech commercial vehicles India | 📈 BULL_ANY_MID | 10 | ↑0 | ↑1.005 | ↑32d | — | +6.6% | -33.84/-35.07 | +0.78% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MAXHEALTH,NSE:KIRLOSIND,NSE:DYNAMATECH,NSE:ABDL,NSE:INDUSTOWER,NSE:AIIL,NSE:AWFIS,NSE:CONCORDBIO,NSE:TVSSCS,NSE:FILATEX,NSE:BLACKBUCK,NSE:INDOCO,NSE:BIRLACABLE,NSE:SIGMAADV,NSE:HINDALCO,NSE:PVRINOX,NSE:TASTYBITE,NSE:PNBHOUSING,NSE:TORNTPHARM,NSE:KPIL,NSE:EIMCOELECO,NSE:HINDZINC,NSE:ADANIENT,NSE:ATHERENERG,NSE:BOSCHLTD,NSE:BIRLANU,NSE:SEDEMAC,NSE:MEESHO,NSE:WAAREEENER,NSE:DRREDDY,NSE:SUNTV,NSE:CUMMINSIND,NSE:VOLTAS,NSE:AURIONPRO,NSE:AUTOAXLES,NSE:SCHNEIDER,NSE:MASFIN,NSE:JARO,NSE:NINSYS,NSE:RATEGAIN,NSE:CREDITACC,NSE:EQUITASBNK,NSE:ZFCVINDIA
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (15)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MAXHEALTH](https://in.tradingview.com/chart/?symbol=NSE:MAXHEALTH)<br><sub>📶W9 · ↑CMF9d</sub> | ⚠ CAUTION | Tertiary quaternary hospital network Delhi NCR North India | ⚡ BULL_ANY_PPV | 89 | 🔄37 | ↑1.030 | ↑1d | SQ·PV | +4.5% | -32.15/-41.06 | +4.48% | 20% |
| [KIRLOSIND](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSIND)<br><sub>📶W9 · RVOL176x · ↑CMF0d</sub> | ✓ SAFE | Holding company: castings, wind power, real estate investments | ⚡ BULL_ANY_PPV | 89 | 🔄62 | ↑1.033 | ↑1d | SQ·PV | +7.0% | -37.28/-42.15 | +7.03% | 20% |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH)<br><sub>📶W9 · W↑30d · ↑CMF0d</sub> | ✓ SAFE | Aerospace hydraulics pumps and automotive turbochargers manufacturer | ⚡ BULL_ANY_PPV | 59 | ↑81 | ↑1.037 | ↑1d | SQ·PV | +4.8% | 36.95/30.22 | +4.80% | 20% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>📶W9 · W↑5d · ↑CMF25d</sub> | ✓ SAFE | Spirits manufacturer, IMFL exporter, Indian domestic and export markets | ⚡ BULL_ANY_PPV | 58 | ↑62 | ↑1.034 | ↑2d | SQ·PV | +4.7% | -13.87/-26.31 | +3.44% | 10% 🟩 |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 91 | 🔄60 | ↑1.003 | ↓9d | SQ | -0.3% | -18.92/-20.04 | +1.17% | 20% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>📶W9 · W↑55d · ↓CMF14d</sub> | ✓ SAFE | Multiplex cinema exhibition chain, entertainment venues | 📈 BULL_ANY_MID | 63 | ↑72 | ↑1.019 | ↑2d | SQ | +5.8% | 16.99/14.58 | +1.29% | 20% |
| [TASTYBITE](https://in.tradingview.com/chart/?symbol=NSE:TASTYBITE)<br><sub>📶W9 · W↑113d · ↑CMF20d</sub> | ✓ SAFE | Ready-to-eat ethnic vegetarian meals packaged food export | 📈 BULL_ANY_MID | 63 | ↑76 | ↑1.024 | ↑2d | SQ | +4.6% | 29.41/21.76 | +0.71% | 20% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>📶W9 · W↑30d · ★ · ↑CMF30d</sub> | ✓ SAFE | Housing loans for retail homebuyers and property | 📈 BULL_ANY_MID | 58 | ↑80 | ↓1.011 | ↑2d | SQ | +3.2% | 20.92/18.82 | -0.01% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑68 | ↓0.997 | ↓2d | SQ | +0.2% | -3.46/-4.79 | -0.71% | 20% |
| [KPIL](https://in.tradingview.com/chart/?symbol=NSE:KPIL)<br><sub>📶W9 · W↑25d · ↓CMF22d</sub> | ⚠ CAUTION | Power transmission EPC projects for utilities and infrastructure | 📈 BULL_ANY_MID | 40 | ↑64 | ↓1.015 | ↑26d | SQ | +10.9% | 44.67/42.44 | +0.26% | 20% |
| [EIMCOELECO](https://in.tradingview.com/chart/?symbol=NSE:EIMCOELECO)<br><sub>📶W9 · W↑65d · ↑CMF20d</sub> | ✓ SAFE | Underground mining equipment manufacturer for coal sector | 📈 BULL_ANY_MID | 40 | ↑85 | ↑1.033 | ↑22d | SQ | +29.6% | 50.62/49.22 | +1.49% | 20% |
| [SCHNEIDER](https://in.tradingview.com/chart/?symbol=NSE:SCHNEIDER)<br><sub>↑CMF1d</sub> | ✓ SAFE | Power distribution equipment manufacturing and servicing | 📈 BULL_ANY_MID | 99 | 🔄77 | ↑1.015 | ↑1d | SQ | +2.7% | -20.87/-23.06 | +2.69% | 10% 🟩 |
| [MASFIN](https://in.tradingview.com/chart/?symbol=NSE:MASFIN)<br><sub>↑CMF2d</sub> | ✓ SAFE | Retail NBFC financing MSMEs home loans two-wheelers used cars | 📈 BULL_ANY_MID | 69 | ↑33 | ↑1.004 | ↑1d | SQ | +0.5% | -46.13/-48.6 | +0.51% | 20% |
| [JARO](https://in.tradingview.com/chart/?symbol=NSE:JARO)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Online higher education platform, executive training, career advancement | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.008 | ↑2d | SQ | +3.7% | -25.89/-31.28 | -0.48% | 20% |
| [NINSYS](https://in.tradingview.com/chart/?symbol=NSE:NINSYS)<br><sub>🚀SS · ↓CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 45 | ↑89 | ↑0.999 | ↓60d+ | SQ | +2.3% | -41.2/-42.09 | +0.32% | 5% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MAXHEALTH,NSE:KIRLOSIND,NSE:DYNAMATECH,NSE:ABDL,NSE:HINDALCO,NSE:PVRINOX,NSE:TASTYBITE,NSE:PNBHOUSING,NSE:TORNTPHARM,NSE:KPIL,NSE:EIMCOELECO,NSE:SCHNEIDER,NSE:MASFIN,NSE:JARO,NSE:NINSYS
```

---

### 🔥 MAJOR — PPV confirmed (13)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [INDUSTOWER](https://in.tradingview.com/chart/?symbol=NSE:INDUSTOWER)<br><sub>📶W9 · W↑5d · ↑CMF8d</sub> | ✓ SAFE | Telecom tower infrastructure operator serving mobile networks | ⚡ BULL_ANY_PPV | 54 | 🔄33 | ↑1.025 | ↑1d | PV | +4.3% | -30.53/-37.66 | +4.30% | 20% |
| [AIIL](https://in.tradingview.com/chart/?symbol=NSE:AIIL)<br><sub>📶W9 · RVOL15x · ↑CMF0d</sub> | ✓ SAFE | NBFC providing investment loans advances securities financing | ⚡ BULL_ANY_PPV | 54 | 🔄43 | ↑1.029 | ↑1d | PV | +6.3% | -38.03/-42.32 | +6.26% | 20% |
| [AWFIS](https://in.tradingview.com/chart/?symbol=NSE:AWFIS)<br><sub>📶W9 · W↑5d · RVOL82x · ↑CMF0d</sub> | ✓ SAFE | Flexible workspace operator for professionals and corporates | ⚡ BULL_ANY_PPV | 49 | 🔄11 | ↑1.114 | ↑1d | PV | +17.5% | -37.66/-50.77 | +17.47% | 20% |
| [CONCORDBIO](https://in.tradingview.com/chart/?symbol=NSE:CONCORDBIO)<br><sub>📶W9 · W↑108d · ↑CMF3d</sub> | ✓ SAFE | Fermentation APIs immunosuppressants oncology biopharmaceutical manufacturer | ⚡ BULL_ANY_PPV | 24 | ↑57 | ↑1.024 | ↑1d | PV | +3.6% | -2.13/-5.04 | +3.64% | 20% |
| [TVSSCS](https://in.tradingview.com/chart/?symbol=NSE:TVSSCS)<br><sub>📶W9 · ↑CMF14d · ÷DIV</sub> | ✓ SAFE | Supply chain logistics management for automotive and industrial sectors | ⚡ BULL_ANY_PPV | 23 | ↑54 | ↑1.017 | ↑2d | PV | +4.7% | -10.2/-16.04 | +1.37% | 10% 🟩 |
| [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX)<br><sub>📶W9 · RVOL17x · ↑CMF30d</sub> | ✓ SAFE | Polyester yarn and chip manufacturer for textiles | ⚡ BULL_ANY_PPV | 19 | ↑94 | ↑1.111 | ↑1d | PV | +14.6% | -2.49/-14.73 | +14.64% | 20% |
| [BLACKBUCK](https://in.tradingview.com/chart/?symbol=NSE:BLACKBUCK)<br><sub>📶W9 · W↑30d · ↑CMF17d</sub> | ✓ SAFE | Digital trucking platform: loads, payments, telematics, financing | ⚡ BULL_ANY_PPV | 19 | ↑55 | ↑1.060 | ↑1d | PV | +7.2% | 12.39/1.43 | +7.21% | 20% |
| [INDOCO](https://in.tradingview.com/chart/?symbol=NSE:INDOCO)<br><sub>📶W9 · W↑10d · ↑CMF11d</sub> | ✓ SAFE | Pharmaceutical manufacturer oral drugs dermatology gastrointestinal India | ⚡ BULL_ANY_PPV | 18 | ↑61 | ↑1.050 | ↑2d | PV | +13.8% | 37.18/36.83 | +3.45% | 20% |
| [BIRLACABLE](https://in.tradingview.com/chart/?symbol=NSE:BIRLACABLE)<br><sub>📶W9 · W↑30d · ↑CMF30d</sub> | ✓ SAFE | Telecom cables, wires, specialized cables manufacturer | ⚡ BULL_ANY_PPV | 8 | ↑98 | ↑1.115 | ↑12d | PV | +46.6% | 66.97/66.15 | +4.72% | 5% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [WAAREEENER](https://in.tradingview.com/chart/?symbol=NSE:WAAREEENER)<br><sub>↓CMF11d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Solar photovoltaic modules manufacturing renewable energy sector | 🔥 BULL_OS_PPV | 59 | 🔄17 | ↑1.011 | ↑1d | PV | +3.0% | -59.58/-61.27 | +3.02% | 20% |
| [DRREDDY](https://in.tradingview.com/chart/?symbol=NSE:DRREDDY)<br><sub>↑CMF0d</sub> | ⚠ CAUTION | Generics, APIs, biosimilars for global emerging markets | ⚡ BULL_ANY_PPV | 59 | 🔄25 | ↑1.008 | ↑1d | PV | +2.0% | -41.95/-43.92 | +1.97% | 20% |
| [SUNTV](https://in.tradingview.com/chart/?symbol=NSE:SUNTV)<br><sub>RVOL9x · ↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Regional Tamil broadcaster, entertainment content, South India | ⚡ BULL_ANY_PPV | 54 | 🔄20 | ↑1.028 | ↑1d | PV | +4.5% | -46.93/-55.1 | +4.49% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:INDUSTOWER,NSE:AIIL,NSE:AWFIS,NSE:CONCORDBIO,NSE:TVSSCS,NSE:FILATEX,NSE:BLACKBUCK,NSE:INDOCO,NSE:BIRLACABLE,NSE:SIGMAADV,NSE:WAAREEENER,NSE:DRREDDY,NSE:SUNTV
```

### 🟢 OVERSOLD — reversal from −53/−60 (9)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CUMMINSIND](https://in.tradingview.com/chart/?symbol=NSE:CUMMINSIND)<br><sub>↑CMF1d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 59 | 🔄53 | ↑1.012 | ↑1d | — | +2.7% | -56.42/-62.44 | +2.68% | 20% |
| [VOLTAS](https://in.tradingview.com/chart/?symbol=NSE:VOLTAS)<br><sub>↓CMF24d · 🎯SLING</sub> | ✓ SAFE | AC units, refrigeration, EPC projects, cooling systems | 🟢 BULL_OVERSOLD | 35 | 🔄15 | ↑0.994 | ↓21d | — | -9.7% | -60.89/-63.2 | +0.56% | 20% |
| [AURIONPRO](https://in.tradingview.com/chart/?symbol=NSE:AURIONPRO)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Digital banking platforms payments mobility government sectors | 🟢 BULL_OVERSOLD | 35 | 🔄2 | ↑0.999 | ↓46d | — | -18.5% | -59.45/-60.98 | +1.45% | 20% |
| [HINDPETRO](https://in.tradingview.com/chart/?symbol=NSE:HINDPETRO)<br><sub>↑CMF9d · 🎯SLING</sub> | ✓ SAFE | Crude oil refining petroleum products marketing hydrocarbons | 🟢 BULL_OVERSOLD | 5 | ↓19 | ↑0.988 | ↓28d | — | -10.1% | -62.08/-62.57 | -0.18% | 20% |
| [ICICIGI](https://in.tradingview.com/chart/?symbol=NSE:ICICIGI)<br><sub>↓CMF16d · ⚠️TRAP</sub> | ✓ SAFE | Motor and health insurance for Indian retail customers | 🟢 BULL_OVERSOLD | 5 | ↓7 | ↑0.970 | ↓28d | — | -11.2% | -76.26/-76.3 | -0.35% | 20% |
| [AUTOAXLES](https://in.tradingview.com/chart/?symbol=NSE:AUTOAXLES)<br><sub>↓CMF9d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 35 | 🔄32 | ↑0.995 | ↓30d | — | -6.8% | -57.66/-58.45 | +1.21% | 20% |
| [PROTEAN](https://in.tradingview.com/chart/?symbol=NSE:PROTEAN)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Digital governance infrastructure software, government services, citizens | 🟡 BULL_OS_L2 | 11 | ↓3 | ↑0.973 | ↓14d | — | -11.3% | -56.25/-56.33 | -0.08% | 20% |
| [OLECTRA](https://in.tradingview.com/chart/?symbol=NSE:OLECTRA)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Electric buses and composite insulators manufacturing transport infrastructure | 🟡 BULL_OS_L2 | 5 | ↓38 | ↑0.982 | ↓28d | — | -10.3% | -59.86/-59.97 | +0.23% | 20% |
| [ADANIGREEN](https://in.tradingview.com/chart/?symbol=NSE:ADANIGREEN)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 0 | ↓62 | ↓0.993 | ↓40d | — | -13.6% | -53.26/-56.27 | -0.93% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CUMMINSIND,NSE:VOLTAS,NSE:AURIONPRO,NSE:HINDPETRO,NSE:ICICIGI,NSE:AUTOAXLES,NSE:PROTEAN,NSE:OLECTRA,NSE:ADANIGREEN
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (11)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>📶W9 · W↑28d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 28 | ↑64 | ↑1.014 | ↑2d | — | +2.7% | 24.78/23.85 | +1.56% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · ↓CMF7d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 19 | ↑76 | ↑1.039 | ↑1d | — | +5.1% | -9.05/-16.39 | +5.11% | 20% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Premium electric scooters, charging network, urban mobility | 📈 BULL_ANY_MID | 18 | ↑98 | ↓1.027 | ↑2d | — | +4.8% | 46.09/44.45 | -0.14% | 20% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>📶W9 · W↑109d · ↑CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 17 | ↑78 | ↓1.015 | ↑3d | — | +4.4% | 32.49/29.43 | +0.17% | 20% |
| [BIRLANU](https://in.tradingview.com/chart/?symbol=NSE:BIRLANU)<br><sub>📶W9 · ↓CMF5d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 10 | ↑36 | ↑1.003 | ↓30d | — | +8.5% | -26.99/-27.85 | +0.96% | 20% |
| [SEDEMAC](https://in.tradingview.com/chart/?symbol=NSE:SEDEMAC)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE | Engine control electronics for automotive and off-highway vehicles | 📈 BULL_ANY_MID | 7 | ↑50 | ↓0.999 | ↓13d | — | -4.9% | -19.71/-21.04 | -0.50% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · 🚀SS · ↑CMF29d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 0 | ↑50 | ↑1.036 | ↑24d | — | +16.7% | 57.53/55.6 | +3.13% | 20% 🟦 |
| [RATEGAIN](https://in.tradingview.com/chart/?symbol=NSE:RATEGAIN)<br><sub>↓CMF26d</sub> | ✓ SAFE | Hotel distribution and revenue management software for hospitality | 📈 BULL_ANY_MID | 43 | 🔄77 | ↑1.001 | ↓17d | — | -5.6% | -44.44/-46.17 | +1.36% | 20% |
| [CREDITACC](https://in.tradingview.com/chart/?symbol=NSE:CREDITACC)<br><sub>↓CMF14d</sub> | ✓ SAFE | Microfinance loans for rural women, NBFC sector | 📈 BULL_ANY_MID | 40 | 🔄55 | ↑1.003 | ↓36d | — | -5.3% | -42.54/-43.69 | +1.50% | 20% |
| [EQUITASBNK](https://in.tradingview.com/chart/?symbol=NSE:EQUITASBNK)<br><sub>↓CMF10d</sub> | ⚠ CAUTION | Small finance bank serving underbanked individuals and SMEs | 📈 BULL_ANY_MID | 38 | 🔄63 | ↑0.999 | ↓17d | — | -2.1% | -49.5/-49.64 | +0.72% | 20% |
| [ZFCVINDIA](https://in.tradingview.com/chart/?symbol=NSE:ZFCVINDIA)<br><sub>W↑15d · ↓CMF10d</sub> | ⚠ CAUTION | Braking systems control tech commercial vehicles India | 📈 BULL_ANY_MID | 10 | ↑0 | ↑1.005 | ↑32d | — | +6.6% | -33.84/-35.07 | +0.78% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:HINDZINC,NSE:ADANIENT,NSE:ATHERENERG,NSE:BOSCHLTD,NSE:BIRLANU,NSE:SEDEMAC,NSE:MEESHO,NSE:RATEGAIN,NSE:CREDITACC,NSE:EQUITASBNK,NSE:ZFCVINDIA
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
