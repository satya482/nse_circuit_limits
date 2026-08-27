> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-08-27
*Generated 2026-08-27 15:50 IST*

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

**Total bull crosses today: 84** · 24 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MOSCHIP,NSE:CRISIL,NSE:BBTC,NSE:INOXINDIA,NSE:WHIRLPOOL,NSE:SIEMENS,NSE:HYUNDAI,NSE:MANINDS,NSE:BIL,NSE:KMEW,NSE:SIGMAADV,NSE:TATACAP,NSE:PRUDENT,NSE:GANDHITUBE,NSE:JINDRILL,NSE:ROSSTECH,NSE:PIXTRANS,NSE:FERMENTA,NSE:SIMPLEXINF,NSE:AETHER,NSE:QPOWER,NSE:UNOMINDA,NSE:STYL,NSE:TECHNVISN,NSE:SYRMA,NSE:ATHERENERG,NSE:CPPLUS,NSE:LODHA,NSE:ASIANENE,NSE:INDSWFTLAB,NSE:RPEL,NSE:SAILIFE,NSE:RUBICON,NSE:RATNAVEER,NSE:GLAND,NSE:ALLTIME,NSE:SCI,NSE:BAJAJHFL,NSE:FIVESTAR,NSE:NELCAST,NSE:HEMIPROP,NSE:AGIIL,NSE:KIRLPNU,NSE:UGROCAP,NSE:COALINDIA,NSE:CEINSYS,NSE:PGHH,NSE:CCL,NSE:GATEWAY,NSE:GREENPANEL,NSE:RESPONIND,NSE:SRF,NSE:TIPSMUSIC,NSE:TCIEXP,NSE:SESHAPAPER,NSE:IMPAL,NSE:BENGALASM,NSE:FRACTAL,NSE:EUREKAFORB,NSE:ARVIND,NSE:APLLTD,NSE:WALCHANNAG,NSE:UTIAMC,NSE:DCAL,NSE:ROTO,NSE:THERMAX,NSE:CAPITALSFB,NSE:REDTAPE,NSE:TRITURBINE,NSE:MANKIND,NSE:SHILCTECH,NSE:SANGAMIND,NSE:ASTRAMICRO,NSE:SUNPHARMA,NSE:SPARC,NSE:PTC,NSE:VSTIND,NSE:IRCTC,NSE:JKCEMENT,NSE:BANCOINDIA,NSE:MAPMYINDIA,NSE:VAIBHAVGBL,NSE:GPTHEALTH,NSE:MUKANDLTD
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (35)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MOSCHIP](https://in.tradingview.com/chart/?symbol=NSE:MOSCHIP)<br><sub>📶W9 · 🚀SS·15x · ↑CMF0d</sub> | ✓ SAFE | Fabless chip design ASICs mixed-signal aerospace defence automotive | ⚡ BULL_ANY_PPV | 89 | 🔄56 | ↑1.049 | ↑1d | SQ·PV | +6.7% | -14.9/-26.71 | +6.72% | 20% |
| [CRISIL](https://in.tradingview.com/chart/?symbol=NSE:CRISIL)<br><sub>📶W9 · W↑54d · ↑CMF26d</sub> | ⚠ CAUTION | Credit ratings analytics research risk advisory services | ⚡ BULL_ANY_PPV | 58 | ↑56 | ↑1.039 | ↑2d | SQ·PV | +5.0% | 43.39/31.26 | +4.21% | 20% |
| [BBTC](https://in.tradingview.com/chart/?symbol=NSE:BBTC)<br><sub>📶W9 · W↑4d · 🚀SS·424x · ↑CMF0d · 🎯SLING</sub> | ✓ SAFE | Teak timber trading, chemicals, textiles, diversified conglomerate | ⚡ BULL_ANY_PPV | 49 | 🔄34 | ↑1.094 | ↑1d | PV | +13.1% | -38.28/-53.95 | +13.14% | 20% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · RVOL31x · ↑CMF1d</sub> | ✓ SAFE | Cryogenic equipment manufacturing for LNG and industrial gases | ⚡ BULL_ANY_PPV | 49 | 🔄95 | ↑1.103 | ↑1d | PV | +13.0% | 3.96/-11.4 | +13.04% | 20% |
| [WHIRLPOOL](https://in.tradingview.com/chart/?symbol=NSE:WHIRLPOOL)<br><sub>📶W9 · W↑4d · 🚀SS·16x · ↑CMF0d</sub> | ✓ SAFE | Washing machines, refrigerators, microwaves for Indian households | ⚡ BULL_ANY_PPV | 49 | 🔄14 | ↑1.069 | ↑1d | PV | +9.0% | -15.68/-29.12 | +9.00% | 20% |
| [SIEMENS](https://in.tradingview.com/chart/?symbol=NSE:SIEMENS)<br><sub>📶W9 · W↑21d · ↑CMF20d · DEL55%(T-1)</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 48 | 🔄74 | ↑1.037 | ↑2d | PV | +5.6% | 36.54/33.96 | +4.54% | 20% |
| [HYUNDAI](https://in.tradingview.com/chart/?symbol=NSE:HYUNDAI)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 5 | ↑47 | ↑1.017 | ↑23d | PV | +15.3% | 45.93/42.54 | +0.87% | 20% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Large-diameter steel pipes oil gas infrastructure export | ⚡ BULL_ANY_PPV | 4 | ↑94 | ↑1.119 | ↑16d | PV | +44.0% | 71.33/70.62 | +9.15% | 20% 🟦 |
| [BIL](https://in.tradingview.com/chart/?symbol=NSE:BIL)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 1 | ↑58 | ↑1.032 | ↑19d | PV | +17.1% | 52.37/49.24 | +3.18% | 20% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>📶W9 · W↑49d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Dredging, marine engineering, ship repair, ports infrastructure | ⚡ BULL_ANY_PPV | 0 | ↑98 | ↑1.079 | ↑25d | PV | +26.8% | 67.09/60.82 | +6.88% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics systems manufacturer for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [TATACAP](https://in.tradingview.com/chart/?symbol=NSE:TATACAP)<br><sub>📶W9 · W↑57d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.013 | ↑1d | SQ | +1.9% | 11.85/8.42 | +1.86% | 20% |
| [PRUDENT](https://in.tradingview.com/chart/?symbol=NSE:PRUDENT)<br><sub>📶W9 · W↑24d · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Mutual funds distribution, wealth management, retail investors | 📈 BULL_ANY_MID | 70 | 🔄81 | ↑1.033 | ↑23d | SQ | +21.0% | 38.42/33.35 | +3.84% | 20% |
| [GANDHITUBE](https://in.tradingview.com/chart/?symbol=NSE:GANDHITUBE)<br><sub>📶W9 · W↑39d · ↑CMF12d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 64 | ↑54 | ↑1.007 | ↑6d | SQ | +1.9% | 31.53/28.77 | +0.18% | 20% |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>📶W9 · W↑34d · ↑CMF11d</sub> | ✓ SAFE | Offshore jack-up drilling rigs for oil and gas exploration | 📈 BULL_ANY_MID | 58 | ↑60 | ↓1.010 | ↑2d | SQ | +2.4% | 26.81/24.62 | -0.30% | 20% |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH)<br><sub>📶W9 · W↑14d · ↓CMF1d · DEL65%(T-1)</sub> | ✓ SAFE | Precision aerospace defense components manufacturing global markets | 📈 BULL_ANY_MID | 58 | ↑84 | ↓1.022 | ↑2d | SQ | +5.0% | 22.57/16.7 | +0.31% | 20% |
| [PIXTRANS](https://in.tradingview.com/chart/?symbol=NSE:PIXTRANS)<br><sub>📶W9 · W↑14d · ↑CMF21d</sub> | ✓ SAFE | V-belts and power transmission components for industrial machinery | 📈 BULL_ANY_MID | 54 | 🔄76 | ↑1.017 | ↑1d | — | +3.0% | -4.37/-4.73 | +2.96% | 20% |
| [FERMENTA](https://in.tradingview.com/chart/?symbol=NSE:FERMENTA)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | Vitamin D3 and enzyme APIs for pharma, nutrition | 📈 BULL_ANY_MID | 54 | 🔄50 | ↑1.028 | ↑1d | — | +4.0% | 8.56/7.27 | +3.95% | 20% |
| [SIMPLEXINF](https://in.tradingview.com/chart/?symbol=NSE:SIMPLEXINF)<br><sub>📶W9 · W↑9d · 🚀SS · ↑CMF13d</sub> | ✓ SAFE | Civil construction contractor for infrastructure projects | 📈 BULL_ANY_MID | 54 | 🔄45 | ↑1.019 | ↑1d | — | +2.9% | 17.9/16.88 | +2.89% | 20% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>📶W9 · ↓CMF11d</sub> | ✓ SAFE | Specialty chemicals for pharma, agro, materials | 📈 BULL_ANY_MID | 45 | ↑96 | ↑1.023 | ↑24d | SQ | +17.5% | 56.51/55.33 | +1.35% | 20% |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER)<br><sub>📶W9 · W↑9d · 🚀SS · ↓CMF12d</sub> | ✓ SAFE | High-voltage electrical equipment manufacturer for power infrastructure | 📈 BULL_ANY_MID | 37 | 🔄97 | ↑1.044 | ↑13d | — | +29.5% | 28.75/26.73 | +5.00% | 5% 🟥 |
| [UNOMINDA](https://in.tradingview.com/chart/?symbol=NSE:UNOMINDA)<br><sub>📶W9 · W↑49d · ↑CMF19d</sub> | ✓ SAFE | Auto parts supplier, OEM components, Indian vehicles | 📈 BULL_ANY_MID | 35 | 🔄53 | ↑1.015 | ↑24d | — | +13.6% | 38.89/38.39 | +1.59% | 20% |
| [STYL](https://in.tradingview.com/chart/?symbol=NSE:STYL)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Secure payment solutions provider for Indian BFSI sector | 📈 BULL_ANY_MID | 28 | ↑50 | ↑1.012 | ↑2d | — | +1.6% | 20.01/17.76 | +0.78% | 20% |
| [TECHNVISN](https://in.tradingview.com/chart/?symbol=NSE:TECHNVISN)<br><sub>📶W9 · ↑CMF25d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 23 | ↑50 | ↑1.025 | ↑2d | — | +7.6% | 9.08/6.82 | +0.70% | 20% 🟦 |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>📶W9 · ↓CMF20d</sub> | ✓ SAFE | Electronics manufacturing, design, assembly, testing for OEM customers | 📈 BULL_ANY_MID | 21 | ↑93 | ↑1.018 | ↑4d | — | +3.8% | 26.5/23.73 | +1.32% | 20% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Electric scooters, batteries, charging network, premium segment | 📈 BULL_ANY_MID | 18 | ↑98 | ↓1.018 | ↑2d | — | +3.9% | 32.92/31.72 | +0.05% | 20% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>📶W9 · ★ · ↓CMF29d</sub> | ✓ SAFE | Video surveillance cameras, DVRs, NVRs, security systems | 📈 BULL_ANY_MID | 18 | ↑97 | ↑1.036 | ↑2d | — | +7.0% | -3.39/-9.05 | +2.82% | 5% 🟥 |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>📶W9 · W↑93d · ↑CMF30d</sub> | ✓ SAFE | Residential and commercial real estate development, Mumbai Pune Bangalore | 📈 BULL_ANY_MID | 18 | ↑70 | ↓1.006 | ↑2d | — | +2.1% | 18.8/16.24 | -0.34% | 20% |
| [ASIANENE](https://in.tradingview.com/chart/?symbol=NSE:ASIANENE)<br><sub>📶W9 · W↑24d · 🚀SS · ↑CMF21d</sub> | ✓ SAFE | Oilfield seismic data acquisition operations maintenance services | 📈 BULL_ANY_MID | 11 | ↑90 | ↑1.071 | ↑9d | — | +31.6% | 62.01/61.62 | +2.96% | 20% |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB)<br><sub>📶W9 · W↑14d · ★ · ↑CMF12d</sub> | ✓ SAFE | Macrolide antibiotics bulk drug manufacturer for global pharma markets | 📈 BULL_ANY_MID | 6 | ↑99 | ↓1.087 | ↑14d | — | +56.8% | 68.3/67.46 | -2.57% | 20% |
| [RPEL](https://in.tradingview.com/chart/?symbol=NSE:RPEL)<br><sub>📶W9 · W↑14d · ★ · ↑CMF10d</sub> | ✓ SAFE | Silica ramming mass and quartz powder for induction furnaces | 📈 BULL_ANY_MID | 6 | ↑98 | ↓1.086 | ↑14d | — | +38.9% | 71.75/71.7 | +0.50% | 20% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Contract research manufacturing pharma biotech molecules | 📈 BULL_ANY_MID | 5 | ↑91 | ↑1.026 | ↑24d | — | +20.7% | 55.03/53.5 | +1.86% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · W↑9d · ↑CMF30d</sub> | ✓ SAFE | Complex generic formulations manufacturing specialty pharmaceuticals | 📈 BULL_ANY_MID | 3 | ↑50 | ↑1.050 | ↑17d | — | +23.5% | 68.52/67.97 | +1.22% | 20% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · W↑24d · 🚀SS · ↑CMF23d</sub> | ✓ SAFE | Stainless steel fasteners tubes pipes solar mounting components | 📈 BULL_ANY_MID | 1 | ↑96 | ↑1.124 | ↑19d | — | +62.6% | 76.22/75.95 | +5.59% | 20% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>📶W9 · W↑19d · ↑CMF15d</sub> | ✓ SAFE | Generic injectable pharmaceuticals manufacturer regulated markets | 📈 BULL_ANY_MID | 0 | ↑88 | ↓1.012 | ↑22d | — | +18.3% | 45.7/45.51 | -1.02% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MOSCHIP,NSE:CRISIL,NSE:BBTC,NSE:INOXINDIA,NSE:WHIRLPOOL,NSE:SIEMENS,NSE:HYUNDAI,NSE:MANINDS,NSE:BIL,NSE:KMEW,NSE:SIGMAADV,NSE:TATACAP,NSE:PRUDENT,NSE:GANDHITUBE,NSE:JINDRILL,NSE:ROSSTECH,NSE:PIXTRANS,NSE:FERMENTA,NSE:SIMPLEXINF,NSE:AETHER,NSE:QPOWER,NSE:UNOMINDA,NSE:STYL,NSE:TECHNVISN,NSE:SYRMA,NSE:ATHERENERG,NSE:CPPLUS,NSE:LODHA,NSE:ASIANENE,NSE:INDSWFTLAB,NSE:RPEL,NSE:SAILIFE,NSE:RUBICON,NSE:RATNAVEER,NSE:GLAND
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (54)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MOSCHIP](https://in.tradingview.com/chart/?symbol=NSE:MOSCHIP)<br><sub>📶W9 · 🚀SS·15x · ↑CMF0d</sub> | ✓ SAFE | Fabless chip design ASICs mixed-signal aerospace defence automotive | ⚡ BULL_ANY_PPV | 89 | 🔄56 | ↑1.049 | ↑1d | SQ·PV | +6.7% | -14.9/-26.71 | +6.72% | 20% |
| [CRISIL](https://in.tradingview.com/chart/?symbol=NSE:CRISIL)<br><sub>📶W9 · W↑54d · ↑CMF26d</sub> | ⚠ CAUTION | Credit ratings analytics research risk advisory services | ⚡ BULL_ANY_PPV | 58 | ↑56 | ↑1.039 | ↑2d | SQ·PV | +5.0% | 43.39/31.26 | +4.21% | 20% |
| [BBTC](https://in.tradingview.com/chart/?symbol=NSE:BBTC)<br><sub>📶W9 · W↑4d · 🚀SS·424x · ↑CMF0d · 🎯SLING</sub> | ✓ SAFE | Teak timber trading, chemicals, textiles, diversified conglomerate | ⚡ BULL_ANY_PPV | 49 | 🔄34 | ↑1.094 | ↑1d | PV | +13.1% | -38.28/-53.95 | +13.14% | 20% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · RVOL31x · ↑CMF1d</sub> | ✓ SAFE | Cryogenic equipment manufacturing for LNG and industrial gases | ⚡ BULL_ANY_PPV | 49 | 🔄95 | ↑1.103 | ↑1d | PV | +13.0% | 3.96/-11.4 | +13.04% | 20% |
| [WHIRLPOOL](https://in.tradingview.com/chart/?symbol=NSE:WHIRLPOOL)<br><sub>📶W9 · W↑4d · 🚀SS·16x · ↑CMF0d</sub> | ✓ SAFE | Washing machines, refrigerators, microwaves for Indian households | ⚡ BULL_ANY_PPV | 49 | 🔄14 | ↑1.069 | ↑1d | PV | +9.0% | -15.68/-29.12 | +9.00% | 20% |
| [SIEMENS](https://in.tradingview.com/chart/?symbol=NSE:SIEMENS)<br><sub>📶W9 · W↑21d · ↑CMF20d · DEL55%(T-1)</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 48 | 🔄74 | ↑1.037 | ↑2d | PV | +5.6% | 36.54/33.96 | +4.54% | 20% |
| [HYUNDAI](https://in.tradingview.com/chart/?symbol=NSE:HYUNDAI)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 5 | ↑47 | ↑1.017 | ↑23d | PV | +15.3% | 45.93/42.54 | +0.87% | 20% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Large-diameter steel pipes oil gas infrastructure export | ⚡ BULL_ANY_PPV | 4 | ↑94 | ↑1.119 | ↑16d | PV | +44.0% | 71.33/70.62 | +9.15% | 20% 🟦 |
| [BIL](https://in.tradingview.com/chart/?symbol=NSE:BIL)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 1 | ↑58 | ↑1.032 | ↑19d | PV | +17.1% | 52.37/49.24 | +3.18% | 20% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>📶W9 · W↑49d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Dredging, marine engineering, ship repair, ports infrastructure | ⚡ BULL_ANY_PPV | 0 | ↑98 | ↑1.079 | ↑25d | PV | +26.8% | 67.09/60.82 | +6.88% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics systems manufacturer for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [TATACAP](https://in.tradingview.com/chart/?symbol=NSE:TATACAP)<br><sub>📶W9 · W↑57d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.013 | ↑1d | SQ | +1.9% | 11.85/8.42 | +1.86% | 20% |
| [PRUDENT](https://in.tradingview.com/chart/?symbol=NSE:PRUDENT)<br><sub>📶W9 · W↑24d · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Mutual funds distribution, wealth management, retail investors | 📈 BULL_ANY_MID | 70 | 🔄81 | ↑1.033 | ↑23d | SQ | +21.0% | 38.42/33.35 | +3.84% | 20% |
| [GANDHITUBE](https://in.tradingview.com/chart/?symbol=NSE:GANDHITUBE)<br><sub>📶W9 · W↑39d · ↑CMF12d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 64 | ↑54 | ↑1.007 | ↑6d | SQ | +1.9% | 31.53/28.77 | +0.18% | 20% |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>📶W9 · W↑34d · ↑CMF11d</sub> | ✓ SAFE | Offshore jack-up drilling rigs for oil and gas exploration | 📈 BULL_ANY_MID | 58 | ↑60 | ↓1.010 | ↑2d | SQ | +2.4% | 26.81/24.62 | -0.30% | 20% |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH)<br><sub>📶W9 · W↑14d · ↓CMF1d · DEL65%(T-1)</sub> | ✓ SAFE | Precision aerospace defense components manufacturing global markets | 📈 BULL_ANY_MID | 58 | ↑84 | ↓1.022 | ↑2d | SQ | +5.0% | 22.57/16.7 | +0.31% | 20% |
| [PIXTRANS](https://in.tradingview.com/chart/?symbol=NSE:PIXTRANS)<br><sub>📶W9 · W↑14d · ↑CMF21d</sub> | ✓ SAFE | V-belts and power transmission components for industrial machinery | 📈 BULL_ANY_MID | 54 | 🔄76 | ↑1.017 | ↑1d | — | +3.0% | -4.37/-4.73 | +2.96% | 20% |
| [FERMENTA](https://in.tradingview.com/chart/?symbol=NSE:FERMENTA)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | Vitamin D3 and enzyme APIs for pharma, nutrition | 📈 BULL_ANY_MID | 54 | 🔄50 | ↑1.028 | ↑1d | — | +4.0% | 8.56/7.27 | +3.95% | 20% |
| [SIMPLEXINF](https://in.tradingview.com/chart/?symbol=NSE:SIMPLEXINF)<br><sub>📶W9 · W↑9d · 🚀SS · ↑CMF13d</sub> | ✓ SAFE | Civil construction contractor for infrastructure projects | 📈 BULL_ANY_MID | 54 | 🔄45 | ↑1.019 | ↑1d | — | +2.9% | 17.9/16.88 | +2.89% | 20% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>📶W9 · ↓CMF11d</sub> | ✓ SAFE | Specialty chemicals for pharma, agro, materials | 📈 BULL_ANY_MID | 45 | ↑96 | ↑1.023 | ↑24d | SQ | +17.5% | 56.51/55.33 | +1.35% | 20% |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER)<br><sub>📶W9 · W↑9d · 🚀SS · ↓CMF12d</sub> | ✓ SAFE | High-voltage electrical equipment manufacturer for power infrastructure | 📈 BULL_ANY_MID | 37 | 🔄97 | ↑1.044 | ↑13d | — | +29.5% | 28.75/26.73 | +5.00% | 5% 🟥 |
| [UNOMINDA](https://in.tradingview.com/chart/?symbol=NSE:UNOMINDA)<br><sub>📶W9 · W↑49d · ↑CMF19d</sub> | ✓ SAFE | Auto parts supplier, OEM components, Indian vehicles | 📈 BULL_ANY_MID | 35 | 🔄53 | ↑1.015 | ↑24d | — | +13.6% | 38.89/38.39 | +1.59% | 20% |
| [STYL](https://in.tradingview.com/chart/?symbol=NSE:STYL)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Secure payment solutions provider for Indian BFSI sector | 📈 BULL_ANY_MID | 28 | ↑50 | ↑1.012 | ↑2d | — | +1.6% | 20.01/17.76 | +0.78% | 20% |
| [TECHNVISN](https://in.tradingview.com/chart/?symbol=NSE:TECHNVISN)<br><sub>📶W9 · ↑CMF25d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 23 | ↑50 | ↑1.025 | ↑2d | — | +7.6% | 9.08/6.82 | +0.70% | 20% 🟦 |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>📶W9 · ↓CMF20d</sub> | ✓ SAFE | Electronics manufacturing, design, assembly, testing for OEM customers | 📈 BULL_ANY_MID | 21 | ↑93 | ↑1.018 | ↑4d | — | +3.8% | 26.5/23.73 | +1.32% | 20% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Electric scooters, batteries, charging network, premium segment | 📈 BULL_ANY_MID | 18 | ↑98 | ↓1.018 | ↑2d | — | +3.9% | 32.92/31.72 | +0.05% | 20% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>📶W9 · ★ · ↓CMF29d</sub> | ✓ SAFE | Video surveillance cameras, DVRs, NVRs, security systems | 📈 BULL_ANY_MID | 18 | ↑97 | ↑1.036 | ↑2d | — | +7.0% | -3.39/-9.05 | +2.82% | 5% 🟥 |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>📶W9 · W↑93d · ↑CMF30d</sub> | ✓ SAFE | Residential and commercial real estate development, Mumbai Pune Bangalore | 📈 BULL_ANY_MID | 18 | ↑70 | ↓1.006 | ↑2d | — | +2.1% | 18.8/16.24 | -0.34% | 20% |
| [ASIANENE](https://in.tradingview.com/chart/?symbol=NSE:ASIANENE)<br><sub>📶W9 · W↑24d · 🚀SS · ↑CMF21d</sub> | ✓ SAFE | Oilfield seismic data acquisition operations maintenance services | 📈 BULL_ANY_MID | 11 | ↑90 | ↑1.071 | ↑9d | — | +31.6% | 62.01/61.62 | +2.96% | 20% |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB)<br><sub>📶W9 · W↑14d · ★ · ↑CMF12d</sub> | ✓ SAFE | Macrolide antibiotics bulk drug manufacturer for global pharma markets | 📈 BULL_ANY_MID | 6 | ↑99 | ↓1.087 | ↑14d | — | +56.8% | 68.3/67.46 | -2.57% | 20% |
| [RPEL](https://in.tradingview.com/chart/?symbol=NSE:RPEL)<br><sub>📶W9 · W↑14d · ★ · ↑CMF10d</sub> | ✓ SAFE | Silica ramming mass and quartz powder for induction furnaces | 📈 BULL_ANY_MID | 6 | ↑98 | ↓1.086 | ↑14d | — | +38.9% | 71.75/71.7 | +0.50% | 20% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Contract research manufacturing pharma biotech molecules | 📈 BULL_ANY_MID | 5 | ↑91 | ↑1.026 | ↑24d | — | +20.7% | 55.03/53.5 | +1.86% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · W↑9d · ↑CMF30d</sub> | ✓ SAFE | Complex generic formulations manufacturing specialty pharmaceuticals | 📈 BULL_ANY_MID | 3 | ↑50 | ↑1.050 | ↑17d | — | +23.5% | 68.52/67.97 | +1.22% | 20% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · W↑24d · 🚀SS · ↑CMF23d</sub> | ✓ SAFE | Stainless steel fasteners tubes pipes solar mounting components | 📈 BULL_ANY_MID | 1 | ↑96 | ↑1.124 | ↑19d | — | +62.6% | 76.22/75.95 | +5.59% | 20% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>📶W9 · W↑19d · ↑CMF15d</sub> | ✓ SAFE | Generic injectable pharmaceuticals manufacturer regulated markets | 📈 BULL_ANY_MID | 0 | ↑88 | ↓1.012 | ↑22d | — | +18.3% | 45.7/45.51 | -1.02% | 20% |
| [SCI](https://in.tradingview.com/chart/?symbol=NSE:SCI)<br><sub>🚀SS · ↓CMF14d</sub> | ✓ SAFE | Ocean freight transport, tankers, bulk carriers, global routes | ⚡ BULL_ANY_PPV | 99 | 🔄63 | ↑1.005 | ↑1d | SQ·PV | +1.4% | -9.42/-10.45 | +1.40% | 20% |
| [BAJAJHFL](https://in.tradingview.com/chart/?symbol=NSE:BAJAJHFL)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Mortgage loans for residential property purchases and refinancing | ⚡ BULL_ANY_PPV | 59 | 🔄24 | ↑1.007 | ↑1d | PV | +1.4% | -32.73/-34.22 | +1.45% | 20% |
| [FIVESTAR](https://in.tradingview.com/chart/?symbol=NSE:FIVESTAR)<br><sub>↑CMF0d · 🎯SLING</sub> | ⚠ CAUTION | Secured business loans for micro-entrepreneurs south india | ⚡ BULL_ANY_PPV | 54 | 🔄57 | ↑1.018 | ↑1d | PV | +3.6% | -51.4/-56.43 | +3.63% | 20% |
| [CCL](https://in.tradingview.com/chart/?symbol=NSE:CCL)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Instant coffee manufacturing and export, global markets | 🟡 BULL_OS_L2 | 40 | 🔄57 | ↑1.002 | ↓22d | — | -6.5% | -55.8/-58.58 | +1.49% | 20% |
| [SRF](https://in.tradingview.com/chart/?symbol=NSE:SRF)<br><sub>🚀SS · ↓CMF26d</sub> | ⚠ CAUTION | Technical textiles, films, chemicals, foils for industrial applications | 📈 BULL_ANY_MID | 99 | 🔄29 | ↑1.005 | ↑1d | SQ | +0.8% | -28.35/-33.91 | +0.85% | 20% |
| [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC)<br><sub>↓CMF5d</sub> | ✓ SAFE | Music content creation, distribution, digital monetization platform | 📈 BULL_ANY_MID | 99 | 🔄58 | ↑1.008 | ↑1d | SQ | +1.5% | -38.87/-41.83 | +1.50% | 20% |
| [TCIEXP](https://in.tradingview.com/chart/?symbol=NSE:TCIEXP)<br><sub>↑CMF10d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄42 | ↑1.015 | ↑1d | SQ | +1.6% | -20.33/-20.93 | +1.55% | 20% |
| [SESHAPAPER](https://in.tradingview.com/chart/?symbol=NSE:SESHAPAPER)<br><sub>↓CMF30d</sub> | ✓ SAFE | Integrated paper and paperboards manufacturer Tamil Nadu facilities | 📈 BULL_ANY_MID | 99 | 🔄24 | ↑1.005 | ↑1d | SQ | +1.2% | -28.05/-28.16 | +1.25% | 20% |
| [IMPAL](https://in.tradingview.com/chart/?symbol=NSE:IMPAL)<br><sub>🚀SS · ↑CMF2d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄52 | ↑1.013 | ↑1d | SQ | +2.4% | -3.07/-10.65 | +2.37% | 20% |
| [BENGALASM](https://in.tradingview.com/chart/?symbol=NSE:BENGALASM)<br><sub>↓CMF16d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.005 | ↑1d | SQ | +0.8% | -31.24/-33.19 | +0.82% | 20% |
| [FRACTAL](https://in.tradingview.com/chart/?symbol=NSE:FRACTAL)<br><sub>↑CMF9d</sub> | ✓ SAFE | AI analytics solutions for Fortune 500 enterprises globally | 📈 BULL_ANY_MID | 87 | 🔄50 | ↑1.010 | ↑13d | SQ | +4.0% | 25.17/24.13 | +1.52% | 20% |
| [EUREKAFORB](https://in.tradingview.com/chart/?symbol=NSE:EUREKAFORB)<br><sub>↓CMF13d</sub> | ⚠ CAUTION | Water purification, vacuum cleaners, air purifiers, consumer durables | 📈 BULL_ANY_MID | 59 | 🔄15 | ↑1.014 | ↑1d | — | +1.8% | -42.36/-47.15 | +1.81% | 20% |
| [APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD)<br><sub>W↑54d · ↓CMF18d</sub> | ⚠ CAUTION | Generic drugs and APIs for global markets | 📈 BULL_ANY_MID | 58 | ↑44 | ↓1.004 | ↑2d | SQ | +2.6% | -3.61/-8.42 | -0.10% | 20% |
| [DCAL](https://in.tradingview.com/chart/?symbol=NSE:DCAL)<br><sub>🚀SS · ↑CMF10d</sub> | ✓ SAFE | Pharmaceutical contract manufacturing and API production | 📈 BULL_ANY_MID | 47 | 🔄10 | ↑1.001 | ↓13d | — | -5.9% | -27.15/-27.3 | +1.11% | 20% |
| [REDTAPE](https://in.tradingview.com/chart/?symbol=NSE:REDTAPE)<br><sub>↓CMF30d</sub> | ✓ SAFE | Footwear apparel accessories omnichannel retail men women kids | 📈 BULL_ANY_MID | 43 | 🔄30 | ↑1.002 | ↓17d | — | -4.8% | -34.0/-34.97 | +1.39% | 20% |
| [TRITURBINE](https://in.tradingview.com/chart/?symbol=NSE:TRITURBINE)<br><sub>🚀SS · ↓CMF7d</sub> | ✓ SAFE | Steam turbines for industrial power generation up to 100MW | 📈 BULL_ANY_MID | 42 | 🔄42 | ↑1.001 | ↓18d | — | -4.6% | -36.08/-39.67 | +1.58% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>↓CMF30d</sub> | ✓ SAFE | Pharma formulations acute chronic diseases consumer health | 📈 BULL_ANY_MID | 40 | 🔄50 | ↑1.006 | ↓21d | — | -3.6% | -34.43/-38.14 | +0.99% | 20% |
| [SHILCTECH](https://in.tradingview.com/chart/?symbol=NSE:SHILCTECH)<br><sub>↓CMF16d</sub> | ✓ SAFE | Transformer manufacturing distribution power industrial electrical equipment | 📈 BULL_ANY_MID | 40 | 🔄50 | ↑1.010 | ↓24d | — | -4.6% | -26.06/-29.36 | +2.45% | 20% |
| [SANGAMIND](https://in.tradingview.com/chart/?symbol=NSE:SANGAMIND)<br><sub>↓CMF13d</sub> | ✓ SAFE | PV yarn denim seamless garments textile manufacturer | 📈 BULL_ANY_MID | 40 | 🔄79 | ↑1.003 | ↓21d | — | -3.2% | -42.79/-43.9 | +1.55% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MOSCHIP,NSE:CRISIL,NSE:BBTC,NSE:INOXINDIA,NSE:WHIRLPOOL,NSE:SIEMENS,NSE:HYUNDAI,NSE:MANINDS,NSE:BIL,NSE:KMEW,NSE:SIGMAADV,NSE:TATACAP,NSE:PRUDENT,NSE:GANDHITUBE,NSE:JINDRILL,NSE:ROSSTECH,NSE:PIXTRANS,NSE:FERMENTA,NSE:SIMPLEXINF,NSE:AETHER,NSE:QPOWER,NSE:UNOMINDA,NSE:STYL,NSE:TECHNVISN,NSE:SYRMA,NSE:ATHERENERG,NSE:CPPLUS,NSE:LODHA,NSE:ASIANENE,NSE:INDSWFTLAB,NSE:RPEL,NSE:SAILIFE,NSE:RUBICON,NSE:RATNAVEER,NSE:GLAND,NSE:SCI,NSE:BAJAJHFL,NSE:FIVESTAR,NSE:CCL,NSE:SRF,NSE:TIPSMUSIC,NSE:TCIEXP,NSE:SESHAPAPER,NSE:IMPAL,NSE:BENGALASM,NSE:FRACTAL,NSE:EUREKAFORB,NSE:APLLTD,NSE:DCAL,NSE:REDTAPE,NSE:TRITURBINE,NSE:MANKIND,NSE:SHILCTECH,NSE:SANGAMIND
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (24)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MOSCHIP](https://in.tradingview.com/chart/?symbol=NSE:MOSCHIP)<br><sub>📶W9 · 🚀SS·15x · ↑CMF0d</sub> | ✓ SAFE | Fabless chip design ASICs mixed-signal aerospace defence automotive | ⚡ BULL_ANY_PPV | 89 | 🔄56 | ↑1.049 | ↑1d | SQ·PV | +6.7% | -14.9/-26.71 | +6.72% | 20% |
| [CRISIL](https://in.tradingview.com/chart/?symbol=NSE:CRISIL)<br><sub>📶W9 · W↑54d · ↑CMF26d</sub> | ⚠ CAUTION | Credit ratings analytics research risk advisory services | ⚡ BULL_ANY_PPV | 58 | ↑56 | ↑1.039 | ↑2d | SQ·PV | +5.0% | 43.39/31.26 | +4.21% | 20% |
| [TATACAP](https://in.tradingview.com/chart/?symbol=NSE:TATACAP)<br><sub>📶W9 · W↑57d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.013 | ↑1d | SQ | +1.9% | 11.85/8.42 | +1.86% | 20% |
| [PRUDENT](https://in.tradingview.com/chart/?symbol=NSE:PRUDENT)<br><sub>📶W9 · W↑24d · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Mutual funds distribution, wealth management, retail investors | 📈 BULL_ANY_MID | 70 | 🔄81 | ↑1.033 | ↑23d | SQ | +21.0% | 38.42/33.35 | +3.84% | 20% |
| [GANDHITUBE](https://in.tradingview.com/chart/?symbol=NSE:GANDHITUBE)<br><sub>📶W9 · W↑39d · ↑CMF12d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 64 | ↑54 | ↑1.007 | ↑6d | SQ | +1.9% | 31.53/28.77 | +0.18% | 20% |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>📶W9 · W↑34d · ↑CMF11d</sub> | ✓ SAFE | Offshore jack-up drilling rigs for oil and gas exploration | 📈 BULL_ANY_MID | 58 | ↑60 | ↓1.010 | ↑2d | SQ | +2.4% | 26.81/24.62 | -0.30% | 20% |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH)<br><sub>📶W9 · W↑14d · ↓CMF1d · DEL65%(T-1)</sub> | ✓ SAFE | Precision aerospace defense components manufacturing global markets | 📈 BULL_ANY_MID | 58 | ↑84 | ↓1.022 | ↑2d | SQ | +5.0% | 22.57/16.7 | +0.31% | 20% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>📶W9 · ↓CMF11d</sub> | ✓ SAFE | Specialty chemicals for pharma, agro, materials | 📈 BULL_ANY_MID | 45 | ↑96 | ↑1.023 | ↑24d | SQ | +17.5% | 56.51/55.33 | +1.35% | 20% |
| [SCI](https://in.tradingview.com/chart/?symbol=NSE:SCI)<br><sub>🚀SS · ↓CMF14d</sub> | ✓ SAFE | Ocean freight transport, tankers, bulk carriers, global routes | ⚡ BULL_ANY_PPV | 99 | 🔄63 | ↑1.005 | ↑1d | SQ·PV | +1.4% | -9.42/-10.45 | +1.40% | 20% |
| [AGIIL](https://in.tradingview.com/chart/?symbol=NSE:AGIIL)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Real estate developer construction residential commercial Punjab | 🟢 BULL_OVERSOLD | 45 | ↓30 | ↑0.990 | ↓46d | SQ | -18.6% | -60.28/-60.3 | +0.31% | 20% |
| [SRF](https://in.tradingview.com/chart/?symbol=NSE:SRF)<br><sub>🚀SS · ↓CMF26d</sub> | ⚠ CAUTION | Technical textiles, films, chemicals, foils for industrial applications | 📈 BULL_ANY_MID | 99 | 🔄29 | ↑1.005 | ↑1d | SQ | +0.8% | -28.35/-33.91 | +0.85% | 20% |
| [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC)<br><sub>↓CMF5d</sub> | ✓ SAFE | Music content creation, distribution, digital monetization platform | 📈 BULL_ANY_MID | 99 | 🔄58 | ↑1.008 | ↑1d | SQ | +1.5% | -38.87/-41.83 | +1.50% | 20% |
| [TCIEXP](https://in.tradingview.com/chart/?symbol=NSE:TCIEXP)<br><sub>↑CMF10d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄42 | ↑1.015 | ↑1d | SQ | +1.6% | -20.33/-20.93 | +1.55% | 20% |
| [SESHAPAPER](https://in.tradingview.com/chart/?symbol=NSE:SESHAPAPER)<br><sub>↓CMF30d</sub> | ✓ SAFE | Integrated paper and paperboards manufacturer Tamil Nadu facilities | 📈 BULL_ANY_MID | 99 | 🔄24 | ↑1.005 | ↑1d | SQ | +1.2% | -28.05/-28.16 | +1.25% | 20% |
| [IMPAL](https://in.tradingview.com/chart/?symbol=NSE:IMPAL)<br><sub>🚀SS · ↑CMF2d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄52 | ↑1.013 | ↑1d | SQ | +2.4% | -3.07/-10.65 | +2.37% | 20% |
| [BENGALASM](https://in.tradingview.com/chart/?symbol=NSE:BENGALASM)<br><sub>↓CMF16d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.005 | ↑1d | SQ | +0.8% | -31.24/-33.19 | +0.82% | 20% |
| [FRACTAL](https://in.tradingview.com/chart/?symbol=NSE:FRACTAL)<br><sub>↑CMF9d</sub> | ✓ SAFE | AI analytics solutions for Fortune 500 enterprises globally | 📈 BULL_ANY_MID | 87 | 🔄50 | ↑1.010 | ↑13d | SQ | +4.0% | 25.17/24.13 | +1.52% | 20% |
| [ARVIND](https://in.tradingview.com/chart/?symbol=NSE:ARVIND)<br><sub>↑CMF10d</sub> | ✓ SAFE | Denim apparel textiles vertically integrated retail cotton | 📈 BULL_ANY_MID | 58 | ↓87 | ↓1.002 | ↓2d | SQ | +0.3% | -4.65/-6.13 | -0.18% | 20% |
| [APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD)<br><sub>W↑54d · ↓CMF18d</sub> | ⚠ CAUTION | Generic drugs and APIs for global markets | 📈 BULL_ANY_MID | 58 | ↑44 | ↓1.004 | ↑2d | SQ | +2.6% | -3.61/-8.42 | -0.10% | 20% |
| [WALCHANNAG](https://in.tradingview.com/chart/?symbol=NSE:WALCHANNAG)<br><sub>↓CMF15d · ÷DIV</sub> | ✓ SAFE | Heavy engineering, defense contractors, nuclear power equipment | 📈 BULL_ANY_MID | 51 | ↓66 | ↑0.994 | ↓14d | SQ | -3.7% | -49.32/-50.32 | +0.60% | 20% |
| [UTIAMC](https://in.tradingview.com/chart/?symbol=NSE:UTIAMC)<br><sub>↓CMF3d · ⚠️TRAP</sub> | ⚠ CAUTION | Mutual fund management, investment schemes, retail investors | 📈 BULL_ANY_MID | 48 | ↓11 | ↓0.995 | ↓12d | SQ | -1.7% | -43.47/-44.33 | -0.72% | 20% |
| [ROTO](https://in.tradingview.com/chart/?symbol=NSE:ROTO)<br><sub>↓CMF14d · ⚠️TRAP</sub> | ✓ SAFE | Progressive cavity pumps for wastewater and sugar industries | 📈 BULL_ANY_MID | 47 | ↓51 | ↓0.991 | ↓13d | SQ | -2.0% | -45.05/-45.58 | -0.75% | 20% |
| [THERMAX](https://in.tradingview.com/chart/?symbol=NSE:THERMAX)<br><sub>🚀SS · ↑CMF19d · ⚠️TRAP</sub> | ✓ SAFE | Boilers, chillers, power plants, pollution control equipment | 📈 BULL_ANY_MID | 45 | ↓54 | ↑0.988 | ↓28d | SQ | -15.9% | -43.68/-43.69 | -0.15% | 20% |
| [CAPITALSFB](https://in.tradingview.com/chart/?symbol=NSE:CAPITALSFB)<br><sub>🚀SS · ↓CMF9d</sub> | ⚠ CAUTION | Retail banking microfinance credit middle-income underserved segments | 📈 BULL_ANY_MID | 45 | ↓46 | ↑0.992 | ↓22d | SQ | -4.2% | -44.68/-48.0 | +0.48% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MOSCHIP,NSE:CRISIL,NSE:TATACAP,NSE:PRUDENT,NSE:GANDHITUBE,NSE:JINDRILL,NSE:ROSSTECH,NSE:AETHER,NSE:SCI,NSE:AGIIL,NSE:SRF,NSE:TIPSMUSIC,NSE:TCIEXP,NSE:SESHAPAPER,NSE:IMPAL,NSE:BENGALASM,NSE:FRACTAL,NSE:ARVIND,NSE:APLLTD,NSE:WALCHANNAG,NSE:UTIAMC,NSE:ROTO,NSE:THERMAX,NSE:CAPITALSFB
```

---

### 🔥 MAJOR — PPV confirmed (14)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [BBTC](https://in.tradingview.com/chart/?symbol=NSE:BBTC)<br><sub>📶W9 · W↑4d · 🚀SS·424x · ↑CMF0d · 🎯SLING</sub> | ✓ SAFE | Teak timber trading, chemicals, textiles, diversified conglomerate | ⚡ BULL_ANY_PPV | 49 | 🔄34 | ↑1.094 | ↑1d | PV | +13.1% | -38.28/-53.95 | +13.14% | 20% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · RVOL31x · ↑CMF1d</sub> | ✓ SAFE | Cryogenic equipment manufacturing for LNG and industrial gases | ⚡ BULL_ANY_PPV | 49 | 🔄95 | ↑1.103 | ↑1d | PV | +13.0% | 3.96/-11.4 | +13.04% | 20% |
| [WHIRLPOOL](https://in.tradingview.com/chart/?symbol=NSE:WHIRLPOOL)<br><sub>📶W9 · W↑4d · 🚀SS·16x · ↑CMF0d</sub> | ✓ SAFE | Washing machines, refrigerators, microwaves for Indian households | ⚡ BULL_ANY_PPV | 49 | 🔄14 | ↑1.069 | ↑1d | PV | +9.0% | -15.68/-29.12 | +9.00% | 20% |
| [SIEMENS](https://in.tradingview.com/chart/?symbol=NSE:SIEMENS)<br><sub>📶W9 · W↑21d · ↑CMF20d · DEL55%(T-1)</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 48 | 🔄74 | ↑1.037 | ↑2d | PV | +5.6% | 36.54/33.96 | +4.54% | 20% |
| [HYUNDAI](https://in.tradingview.com/chart/?symbol=NSE:HYUNDAI)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 5 | ↑47 | ↑1.017 | ↑23d | PV | +15.3% | 45.93/42.54 | +0.87% | 20% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Large-diameter steel pipes oil gas infrastructure export | ⚡ BULL_ANY_PPV | 4 | ↑94 | ↑1.119 | ↑16d | PV | +44.0% | 71.33/70.62 | +9.15% | 20% 🟦 |
| [BIL](https://in.tradingview.com/chart/?symbol=NSE:BIL)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 1 | ↑58 | ↑1.032 | ↑19d | PV | +17.1% | 52.37/49.24 | +3.18% | 20% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>📶W9 · W↑49d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Dredging, marine engineering, ship repair, ports infrastructure | ⚡ BULL_ANY_PPV | 0 | ↑98 | ↑1.079 | ↑25d | PV | +26.8% | 67.09/60.82 | +6.88% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics systems manufacturer for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [ALLTIME](https://in.tradingview.com/chart/?symbol=NSE:ALLTIME)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🔥 BULL_OS_PPV | 5 | ↓9 | ↑0.990 | ↓32d | PV | -11.7% | -62.11/-64.45 | +0.09% | 20% |
| [BAJAJHFL](https://in.tradingview.com/chart/?symbol=NSE:BAJAJHFL)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Mortgage loans for residential property purchases and refinancing | ⚡ BULL_ANY_PPV | 59 | 🔄24 | ↑1.007 | ↑1d | PV | +1.4% | -32.73/-34.22 | +1.45% | 20% |
| [FIVESTAR](https://in.tradingview.com/chart/?symbol=NSE:FIVESTAR)<br><sub>↑CMF0d · 🎯SLING</sub> | ⚠ CAUTION | Secured business loans for micro-entrepreneurs south india | ⚡ BULL_ANY_PPV | 54 | 🔄57 | ↑1.018 | ↑1d | PV | +3.6% | -51.4/-56.43 | +3.63% | 20% |
| [NELCAST](https://in.tradingview.com/chart/?symbol=NSE:NELCAST)<br><sub>↓CMF23d</sub> | ✓ SAFE | Ductile grey iron castings commercial vehicle tractor sectors | ⚡ BULL_ANY_PPV | 10 | ↓20 | ↑0.998 | ↓15d | PV | -6.0% | -47.92/-50.62 | +1.51% | 20% |
| [HEMIPROP](https://in.tradingview.com/chart/?symbol=NSE:HEMIPROP)<br><sub>🚀SS · ↓CMF20d</sub> | ✓ SAFE | Real estate development monetizing surplus PSU land assets | ⚡ BULL_ANY_PPV | 6 | ↓27 | ↑0.995 | ↓19d | PV | -2.8% | -47.06/-49.07 | +0.72% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:BBTC,NSE:INOXINDIA,NSE:WHIRLPOOL,NSE:SIEMENS,NSE:HYUNDAI,NSE:MANINDS,NSE:BIL,NSE:KMEW,NSE:SIGMAADV,NSE:ALLTIME,NSE:BAJAJHFL,NSE:FIVESTAR,NSE:NELCAST,NSE:HEMIPROP
```

### 🟢 OVERSOLD — reversal from −53/−60 (9)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [KIRLPNU](https://in.tradingview.com/chart/?symbol=NSE:KIRLPNU)<br><sub>↑CMF4d · 🎯SLING</sub> | ⚠ CAUTION | Pneumatic compressors, gas compression, industrial engineering solutions | 🟢 BULL_OVERSOLD | 16 | ↓1 | ↑0.794 | ↓9d | — | -51.5% | -60.99/-61.54 | +0.40% | 20% |
| [UGROCAP](https://in.tradingview.com/chart/?symbol=NSE:UGROCAP)<br><sub>🚀SS · ↓CMF18d · 🎯SLING</sub> | ✓ SAFE | MSME lending platform, technology-driven credit scoring | 🟢 BULL_OVERSOLD | 11 | ↓2 | ↑0.979 | ↓14d | — | -8.3% | -62.91/-63.12 | +0.20% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>🚀SS · ↑CMF15d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 5 | ↓37 | ↑0.997 | ↓60d+ | — | -11.4% | -58.82/-63.69 | +0.06% | 20% |
| [CEINSYS](https://in.tradingview.com/chart/?symbol=NSE:CEINSYS)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Geospatial software and enterprise mobility solutions provider | 🟢 BULL_OVERSOLD | 5 | ↓50 | ↑0.961 | ↓35d | — | -20.5% | -70.87/-72.36 | -0.41% | 20% |
| [PGHH](https://in.tradingview.com/chart/?symbol=NSE:PGHH)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Feminine hygiene pads, healthcare products, consumer packaged goods | 🟢 BULL_OVERSOLD | 0 | ↓3 | ↓0.986 | ↓27d | — | -7.6% | -63.4/-64.01 | -0.42% | 20% |
| [CCL](https://in.tradingview.com/chart/?symbol=NSE:CCL)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION | Instant coffee manufacturing and export, global markets | 🟡 BULL_OS_L2 | 40 | 🔄57 | ↑1.002 | ↓22d | — | -6.5% | -55.8/-58.58 | +1.49% | 20% |
| [GATEWAY](https://in.tradingview.com/chart/?symbol=NSE:GATEWAY)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Container depots freight stations inter-modal logistics network | 🟡 BULL_OS_L2 | 11 | ↓24 | ↑0.991 | ↓14d | — | -4.9% | -58.05/-58.6 | +0.58% | 20% |
| [GREENPANEL](https://in.tradingview.com/chart/?symbol=NSE:GREENPANEL)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | MDF and plywood manufacturer for furniture construction | 🟡 BULL_OS_L2 | 6 | ↓3 | ↑0.976 | ↓19d | — | -17.2% | -53.45/-54.73 | +1.22% | 20% |
| [RESPONIND](https://in.tradingview.com/chart/?symbol=NSE:RESPONIND)<br><sub>↓CMF9d · 🎯SLING</sub> | ✓ SAFE | fasteners manufacturing automotive commercial vehicle suppliers | 🟡 BULL_OS_L2 | 5 | ↓8 | ↑0.995 | ↓30d | — | -17.7% | -56.11/-57.25 | +3.37% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:KIRLPNU,NSE:UGROCAP,NSE:COALINDIA,NSE:CEINSYS,NSE:PGHH,NSE:CCL,NSE:GATEWAY,NSE:GREENPANEL,NSE:RESPONIND
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (37)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PIXTRANS](https://in.tradingview.com/chart/?symbol=NSE:PIXTRANS)<br><sub>📶W9 · W↑14d · ↑CMF21d</sub> | ✓ SAFE | V-belts and power transmission components for industrial machinery | 📈 BULL_ANY_MID | 54 | 🔄76 | ↑1.017 | ↑1d | — | +3.0% | -4.37/-4.73 | +2.96% | 20% |
| [FERMENTA](https://in.tradingview.com/chart/?symbol=NSE:FERMENTA)<br><sub>📶W9 · ↓CMF3d</sub> | ✓ SAFE | Vitamin D3 and enzyme APIs for pharma, nutrition | 📈 BULL_ANY_MID | 54 | 🔄50 | ↑1.028 | ↑1d | — | +4.0% | 8.56/7.27 | +3.95% | 20% |
| [SIMPLEXINF](https://in.tradingview.com/chart/?symbol=NSE:SIMPLEXINF)<br><sub>📶W9 · W↑9d · 🚀SS · ↑CMF13d</sub> | ✓ SAFE | Civil construction contractor for infrastructure projects | 📈 BULL_ANY_MID | 54 | 🔄45 | ↑1.019 | ↑1d | — | +2.9% | 17.9/16.88 | +2.89% | 20% |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER)<br><sub>📶W9 · W↑9d · 🚀SS · ↓CMF12d</sub> | ✓ SAFE | High-voltage electrical equipment manufacturer for power infrastructure | 📈 BULL_ANY_MID | 37 | 🔄97 | ↑1.044 | ↑13d | — | +29.5% | 28.75/26.73 | +5.00% | 5% 🟥 |
| [UNOMINDA](https://in.tradingview.com/chart/?symbol=NSE:UNOMINDA)<br><sub>📶W9 · W↑49d · ↑CMF19d</sub> | ✓ SAFE | Auto parts supplier, OEM components, Indian vehicles | 📈 BULL_ANY_MID | 35 | 🔄53 | ↑1.015 | ↑24d | — | +13.6% | 38.89/38.39 | +1.59% | 20% |
| [STYL](https://in.tradingview.com/chart/?symbol=NSE:STYL)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Secure payment solutions provider for Indian BFSI sector | 📈 BULL_ANY_MID | 28 | ↑50 | ↑1.012 | ↑2d | — | +1.6% | 20.01/17.76 | +0.78% | 20% |
| [TECHNVISN](https://in.tradingview.com/chart/?symbol=NSE:TECHNVISN)<br><sub>📶W9 · ↑CMF25d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 23 | ↑50 | ↑1.025 | ↑2d | — | +7.6% | 9.08/6.82 | +0.70% | 20% 🟦 |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>📶W9 · ↓CMF20d</sub> | ✓ SAFE | Electronics manufacturing, design, assembly, testing for OEM customers | 📈 BULL_ANY_MID | 21 | ↑93 | ↑1.018 | ↑4d | — | +3.8% | 26.5/23.73 | +1.32% | 20% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Electric scooters, batteries, charging network, premium segment | 📈 BULL_ANY_MID | 18 | ↑98 | ↓1.018 | ↑2d | — | +3.9% | 32.92/31.72 | +0.05% | 20% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>📶W9 · ★ · ↓CMF29d</sub> | ✓ SAFE | Video surveillance cameras, DVRs, NVRs, security systems | 📈 BULL_ANY_MID | 18 | ↑97 | ↑1.036 | ↑2d | — | +7.0% | -3.39/-9.05 | +2.82% | 5% 🟥 |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>📶W9 · W↑93d · ↑CMF30d</sub> | ✓ SAFE | Residential and commercial real estate development, Mumbai Pune Bangalore | 📈 BULL_ANY_MID | 18 | ↑70 | ↓1.006 | ↑2d | — | +2.1% | 18.8/16.24 | -0.34% | 20% |
| [ASIANENE](https://in.tradingview.com/chart/?symbol=NSE:ASIANENE)<br><sub>📶W9 · W↑24d · 🚀SS · ↑CMF21d</sub> | ✓ SAFE | Oilfield seismic data acquisition operations maintenance services | 📈 BULL_ANY_MID | 11 | ↑90 | ↑1.071 | ↑9d | — | +31.6% | 62.01/61.62 | +2.96% | 20% |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB)<br><sub>📶W9 · W↑14d · ★ · ↑CMF12d</sub> | ✓ SAFE | Macrolide antibiotics bulk drug manufacturer for global pharma markets | 📈 BULL_ANY_MID | 6 | ↑99 | ↓1.087 | ↑14d | — | +56.8% | 68.3/67.46 | -2.57% | 20% |
| [RPEL](https://in.tradingview.com/chart/?symbol=NSE:RPEL)<br><sub>📶W9 · W↑14d · ★ · ↑CMF10d</sub> | ✓ SAFE | Silica ramming mass and quartz powder for induction furnaces | 📈 BULL_ANY_MID | 6 | ↑98 | ↓1.086 | ↑14d | — | +38.9% | 71.75/71.7 | +0.50% | 20% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Contract research manufacturing pharma biotech molecules | 📈 BULL_ANY_MID | 5 | ↑91 | ↑1.026 | ↑24d | — | +20.7% | 55.03/53.5 | +1.86% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · W↑9d · ↑CMF30d</sub> | ✓ SAFE | Complex generic formulations manufacturing specialty pharmaceuticals | 📈 BULL_ANY_MID | 3 | ↑50 | ↑1.050 | ↑17d | — | +23.5% | 68.52/67.97 | +1.22% | 20% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · W↑24d · 🚀SS · ↑CMF23d</sub> | ✓ SAFE | Stainless steel fasteners tubes pipes solar mounting components | 📈 BULL_ANY_MID | 1 | ↑96 | ↑1.124 | ↑19d | — | +62.6% | 76.22/75.95 | +5.59% | 20% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>📶W9 · W↑19d · ↑CMF15d</sub> | ✓ SAFE | Generic injectable pharmaceuticals manufacturer regulated markets | 📈 BULL_ANY_MID | 0 | ↑88 | ↓1.012 | ↑22d | — | +18.3% | 45.7/45.51 | -1.02% | 20% |
| [EUREKAFORB](https://in.tradingview.com/chart/?symbol=NSE:EUREKAFORB)<br><sub>↓CMF13d</sub> | ⚠ CAUTION | Water purification, vacuum cleaners, air purifiers, consumer durables | 📈 BULL_ANY_MID | 59 | 🔄15 | ↑1.014 | ↑1d | — | +1.8% | -42.36/-47.15 | +1.81% | 20% |
| [DCAL](https://in.tradingview.com/chart/?symbol=NSE:DCAL)<br><sub>🚀SS · ↑CMF10d</sub> | ✓ SAFE | Pharmaceutical contract manufacturing and API production | 📈 BULL_ANY_MID | 47 | 🔄10 | ↑1.001 | ↓13d | — | -5.9% | -27.15/-27.3 | +1.11% | 20% |
| [REDTAPE](https://in.tradingview.com/chart/?symbol=NSE:REDTAPE)<br><sub>↓CMF30d</sub> | ✓ SAFE | Footwear apparel accessories omnichannel retail men women kids | 📈 BULL_ANY_MID | 43 | 🔄30 | ↑1.002 | ↓17d | — | -4.8% | -34.0/-34.97 | +1.39% | 20% |
| [TRITURBINE](https://in.tradingview.com/chart/?symbol=NSE:TRITURBINE)<br><sub>🚀SS · ↓CMF7d</sub> | ✓ SAFE | Steam turbines for industrial power generation up to 100MW | 📈 BULL_ANY_MID | 42 | 🔄42 | ↑1.001 | ↓18d | — | -4.6% | -36.08/-39.67 | +1.58% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>↓CMF30d</sub> | ✓ SAFE | Pharma formulations acute chronic diseases consumer health | 📈 BULL_ANY_MID | 40 | 🔄50 | ↑1.006 | ↓21d | — | -3.6% | -34.43/-38.14 | +0.99% | 20% |
| [SHILCTECH](https://in.tradingview.com/chart/?symbol=NSE:SHILCTECH)<br><sub>↓CMF16d</sub> | ✓ SAFE | Transformer manufacturing distribution power industrial electrical equipment | 📈 BULL_ANY_MID | 40 | 🔄50 | ↑1.010 | ↓24d | — | -4.6% | -26.06/-29.36 | +2.45% | 20% |
| [SANGAMIND](https://in.tradingview.com/chart/?symbol=NSE:SANGAMIND)<br><sub>↓CMF13d</sub> | ✓ SAFE | PV yarn denim seamless garments textile manufacturer | 📈 BULL_ANY_MID | 40 | 🔄79 | ↑1.003 | ↓21d | — | -3.2% | -42.79/-43.9 | +1.55% | 20% |
| [ASTRAMICRO](https://in.tradingview.com/chart/?symbol=NSE:ASTRAMICRO)<br><sub>↓CMF20d</sub> | ✓ SAFE | RF Microwave modules defense space telecom systems | 📈 BULL_ANY_MID | 12 | ↓92 | ↓0.992 | ↓8d | — | -1.1% | -29.27/-29.85 | -0.66% | 20% |
| [SUNPHARMA](https://in.tradingview.com/chart/?symbol=NSE:SUNPHARMA)<br><sub>↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 5 | ↓57 | ↑0.999 | ↓48d | — | +6.1% | -33.13/-33.88 | +0.40% | 20% |
| [SPARC](https://in.tradingview.com/chart/?symbol=NSE:SPARC)<br><sub>↓CMF30d · ÷DIV</sub> | ✓ SAFE | Early-stage drug development for global pharmaceutical markets | 📈 BULL_ANY_MID | 5 | ↓75 | ↑0.989 | ↓44d | — | -13.3% | -45.22/-46.76 | +0.32% | 10% 🟨 |
| [PTC](https://in.tradingview.com/chart/?symbol=NSE:PTC)<br><sub>↑CMF18d</sub> | ✓ SAFE | Power trading marketplace connecting generators and distributors | 📈 BULL_ANY_MID | 5 | ↓19 | ↑0.986 | ↓20d | — | -6.6% | -29.12/-29.18 | +0.43% | 20% |
| [VSTIND](https://in.tradingview.com/chart/?symbol=NSE:VSTIND)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Cigarette and tobacco products manufacturer for Indian consumers | 📈 BULL_ANY_MID | 5 | ↓10 | ↑0.992 | ↓41d | — | -18.9% | -52.37/-52.96 | +0.13% | 20% |
| [IRCTC](https://in.tradingview.com/chart/?symbol=NSE:IRCTC)<br><sub>↓CMF5d · ⚠️TRAP</sub> | ✓ SAFE | Railway tickets catering tourism packaged water PSU | 📈 BULL_ANY_MID | 1 | ↓8 | ↓0.993 | ↓19d | — | -0.5% | -34.15/-34.58 | -0.85% | 20% |
| [JKCEMENT](https://in.tradingview.com/chart/?symbol=NSE:JKCEMENT)<br><sub>↓CMF6d · ⚠️TRAP</sub> | ⚠ CAUTION | Cement manufacturer serving construction and infrastructure sectors | 📈 BULL_ANY_MID | 1 | ↓26 | ↓0.992 | ↓19d | — | -3.9% | -45.9/-46.83 | -0.82% | 20% |
| [BANCOINDIA](https://in.tradingview.com/chart/?symbol=NSE:BANCOINDIA)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Engine cooling modules supplier automotive OEMs domestic international | 📈 BULL_ANY_MID | 1 | ↓35 | ↓0.997 | ↓19d | — | -2.1% | -25.34/-26.48 | -0.67% | 20% |
| [MAPMYINDIA](https://in.tradingview.com/chart/?symbol=NSE:MAPMYINDIA)<br><sub>↓CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Digital maps geospatial software location intelligence platform India | 📈 BULL_ANY_MID | 0 | ↓20 | ↓0.983 | ↓26d | — | -6.4% | -28.68/-29.77 | -3.11% | 20% |
| [VAIBHAVGBL](https://in.tradingview.com/chart/?symbol=NSE:VAIBHAVGBL)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Fashion jewelry gemstones direct-to-consumer global TV retail | 📈 BULL_ANY_MID | 0 | ↓34 | ↓0.984 | ↓24d | — | -11.8% | -38.36/-38.76 | -0.63% | 20% |
| [GPTHEALTH](https://in.tradingview.com/chart/?symbol=NSE:GPTHEALTH)<br><sub>↓CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Multispecialty hospital chain secondary tertiary care Eastern India | 📈 BULL_ANY_MID | 0 | ↓49 | ↓0.992 | ↓27d | — | +0.2% | -34.26/-35.25 | -0.43% | 20% |
| [MUKANDLTD](https://in.tradingview.com/chart/?symbol=NSE:MUKANDLTD)<br><sub>↓CMF11d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 0 | ↓41 | ↓0.998 | ↓22d | — | -2.0% | -26.43/-28.33 | -0.56% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:PIXTRANS,NSE:FERMENTA,NSE:SIMPLEXINF,NSE:QPOWER,NSE:UNOMINDA,NSE:STYL,NSE:TECHNVISN,NSE:SYRMA,NSE:ATHERENERG,NSE:CPPLUS,NSE:LODHA,NSE:ASIANENE,NSE:INDSWFTLAB,NSE:RPEL,NSE:SAILIFE,NSE:RUBICON,NSE:RATNAVEER,NSE:GLAND,NSE:EUREKAFORB,NSE:DCAL,NSE:REDTAPE,NSE:TRITURBINE,NSE:MANKIND,NSE:SHILCTECH,NSE:SANGAMIND,NSE:ASTRAMICRO,NSE:SUNPHARMA,NSE:SPARC,NSE:PTC,NSE:VSTIND,NSE:IRCTC,NSE:JKCEMENT,NSE:BANCOINDIA,NSE:MAPMYINDIA,NSE:VAIBHAVGBL,NSE:GPTHEALTH,NSE:MUKANDLTD
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
