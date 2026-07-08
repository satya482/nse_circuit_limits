> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-07-08
*Generated 2026-07-08 15:43 IST*

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
| RS-Confirmed table | Separate table below, rs_state ≠ weak — informational only, all signals still listed in category tables |
| 📶W9 in Symbol | Daily RS > Weekly RS EMA9 AND Weekly RS EMA9 rising (same gate as ema25_zl_scanner RS_MODE=weekly_ema9) — highest sort priority in every table |

---

**Total bull crosses today: 42** · 15 inside active squeeze

```
NSE:EMBDL,NSE:OAL,NSE:SJS,NSE:SILVERTUC,NSE:RAMRAT,NSE:JINDRILL,NSE:INDOCO,NSE:HIKAL,NSE:BHAGCHEM,NSE:RATNAVEER,NSE:SANGAMIND,NSE:ZYDUSLIFE,NSE:SENCO,NSE:DOLPHIN,NSE:HCLTECH,NSE:UEL,NSE:LTM,NSE:KPITTECH,NSE:TATASTEEL,NSE:JINDALSTEL,NSE:PRABHA,NSE:INFY,NSE:PASHUPATI,NSE:DIVISLAB,NSE:RHIM,NSE:TORNTPOWER,NSE:MAHASTEEL,NSE:TATACONSUM,NSE:POWERGRID,NSE:MUTHOOTFIN,NSE:INDIAMART,NSE:ITC,NSE:BEL,NSE:TECHM,NSE:MAZDOCK,NSE:BPCL,NSE:TATACHEM,NSE:VBL,NSE:WIPRO,NSE:HINDALCO,NSE:COALINDIA,NSE:E2E
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (12)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [EMBDL](https://in.tradingview.com/chart/?symbol=NSE:EMBDL)<br><sub>📶W9 · W↑54d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Residential and commercial real estate development urban markets | ⚡ BULL_ANY_PPV | 99 | 🔄24 | ↑1.010 | ↑1d | SQ·PV | +2.2% | 16.17/15.75 | +2.22% | 10% 🟨 |
| [OAL](https://in.tradingview.com/chart/?symbol=NSE:OAL)<br><sub>📶W9 · W↑66d · 🚀SS·10x · ↓CMF20d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 89 | 🔄69 | ↑1.052 | ↑1d | SQ·PV | +6.3% | -8.2/-17.82 | +6.31% | 20% |
| [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS)<br><sub>📶W9 · W↑61d · ↓CMF25d</sub> | ⚠ CAUTION | Decorative graphics manufacturing for automotive industrial sectors | ⚡ BULL_ANY_PPV | 62 | ↑89 | ↑1.007 | ↑8d | SQ·PV | +3.5% | 44.14/43.65 | +0.37% | 20% |
| [SILVERTUC](https://in.tradingview.com/chart/?symbol=NSE:SILVERTUC)<br><sub>📶W9 · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Software development and digital transformation IT services | ⚡ BULL_ANY_PPV | 54 | 🔄98 | ↑1.023 | ↑1d | PV | +3.6% | -5.51/-8.33 | +3.62% | 20% |
| [RAMRAT](https://in.tradingview.com/chart/?symbol=NSE:RAMRAT)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Enameled copper wires manufacturing electrical equipment sector | ⚡ BULL_ANY_PPV | 54 | 🔄83 | ↑1.016 | ↑1d | PV | +2.1% | 9.8/3.84 | +2.15% | 20% |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>📶W9 · 🚀SS·130x · ↑CMF0d</sub> | ✓ SAFE | Offshore jack-up rigs drilling services oil gas sector | ⚡ BULL_ANY_PPV | 49 | 🔄58 | ↑1.068 | ↑1d | PV | +11.3% | -39.14/-49.64 | +11.26% | 20% |
| [INDOCO](https://in.tradingview.com/chart/?symbol=NSE:INDOCO)<br><sub>📶W9 · W↑23d · ↑CMF19d</sub> | ✓ SAFE | Pharmaceutical manufacturer oral drugs dermatology gastrointestinal India | ⚡ BULL_ANY_PPV | 40 | ↑49 | ↑1.035 | ↑20d | SQ·PV | +21.1% | 45.58/42.29 | +3.13% | 20% |
| [HIKAL](https://in.tradingview.com/chart/?symbol=NSE:HIKAL)<br><sub>📶W9 · W↑18d · RVOL28x · ↓CMF1d</sub> | ✓ SAFE | APIs and specialty chemicals for pharma, crop protection | ⚡ BULL_ANY_PPV | 35 | 🔄51 | ↑1.044 | ↑15d | PV | +20.4% | 43.34/41.19 | +5.23% | 20% |
| [BHAGCHEM](https://in.tradingview.com/chart/?symbol=NSE:BHAGCHEM)<br><sub>📶W9 · W↑66d · ↑CMF13d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 5 | ↑76 | ↑1.025 | ↑22d | PV | +24.0% | 47.23/45.86 | +2.18% | 20% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · W↑18d · ↓CMF9d</sub> | ✓ SAFE | Stainless steel washers tubes pipes solar mounting industrial | 📈 BULL_ANY_MID | 59 | 🔄75 | ↑1.010 | ↑1d | — | +1.5% | 6.42/4.07 | +1.52% | 20% |
| [SANGAMIND](https://in.tradingview.com/chart/?symbol=NSE:SANGAMIND)<br><sub>📶W9 · W↑61d · ↓CMF30d</sub> | ✓ SAFE | PV yarn denim seamless garments textile manufacturer | 📈 BULL_ANY_MID | 53 | ↑77 | ↓1.005 | ↑7d | SQ | +3.1% | 46.76/44.93 | -0.63% | 20% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>📶W9 · W↑56d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | Pharmaceuticals: generics, branded drugs, consumer wellness products | 📈 BULL_ANY_MID | 49 | 🔄74 | ↑1.031 | ↑1d | — | +3.9% | 44.71/41.57 | +3.92% | 20% |

```
NSE:EMBDL,NSE:OAL,NSE:SJS,NSE:SILVERTUC,NSE:RAMRAT,NSE:JINDRILL,NSE:INDOCO,NSE:HIKAL,NSE:BHAGCHEM,NSE:RATNAVEER,NSE:SANGAMIND,NSE:ZYDUSLIFE
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (26)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [EMBDL](https://in.tradingview.com/chart/?symbol=NSE:EMBDL)<br><sub>📶W9 · W↑54d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Residential and commercial real estate development urban markets | ⚡ BULL_ANY_PPV | 99 | 🔄24 | ↑1.010 | ↑1d | SQ·PV | +2.2% | 16.17/15.75 | +2.22% | 10% 🟨 |
| [OAL](https://in.tradingview.com/chart/?symbol=NSE:OAL)<br><sub>📶W9 · W↑66d · 🚀SS·10x · ↓CMF20d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 89 | 🔄69 | ↑1.052 | ↑1d | SQ·PV | +6.3% | -8.2/-17.82 | +6.31% | 20% |
| [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS)<br><sub>📶W9 · W↑61d · ↓CMF25d</sub> | ⚠ CAUTION | Decorative graphics manufacturing for automotive industrial sectors | ⚡ BULL_ANY_PPV | 62 | ↑89 | ↑1.007 | ↑8d | SQ·PV | +3.5% | 44.14/43.65 | +0.37% | 20% |
| [SILVERTUC](https://in.tradingview.com/chart/?symbol=NSE:SILVERTUC)<br><sub>📶W9 · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Software development and digital transformation IT services | ⚡ BULL_ANY_PPV | 54 | 🔄98 | ↑1.023 | ↑1d | PV | +3.6% | -5.51/-8.33 | +3.62% | 20% |
| [RAMRAT](https://in.tradingview.com/chart/?symbol=NSE:RAMRAT)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Enameled copper wires manufacturing electrical equipment sector | ⚡ BULL_ANY_PPV | 54 | 🔄83 | ↑1.016 | ↑1d | PV | +2.1% | 9.8/3.84 | +2.15% | 20% |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>📶W9 · 🚀SS·130x · ↑CMF0d</sub> | ✓ SAFE | Offshore jack-up rigs drilling services oil gas sector | ⚡ BULL_ANY_PPV | 49 | 🔄58 | ↑1.068 | ↑1d | PV | +11.3% | -39.14/-49.64 | +11.26% | 20% |
| [INDOCO](https://in.tradingview.com/chart/?symbol=NSE:INDOCO)<br><sub>📶W9 · W↑23d · ↑CMF19d</sub> | ✓ SAFE | Pharmaceutical manufacturer oral drugs dermatology gastrointestinal India | ⚡ BULL_ANY_PPV | 40 | ↑49 | ↑1.035 | ↑20d | SQ·PV | +21.1% | 45.58/42.29 | +3.13% | 20% |
| [HIKAL](https://in.tradingview.com/chart/?symbol=NSE:HIKAL)<br><sub>📶W9 · W↑18d · RVOL28x · ↓CMF1d</sub> | ✓ SAFE | APIs and specialty chemicals for pharma, crop protection | ⚡ BULL_ANY_PPV | 35 | 🔄51 | ↑1.044 | ↑15d | PV | +20.4% | 43.34/41.19 | +5.23% | 20% |
| [BHAGCHEM](https://in.tradingview.com/chart/?symbol=NSE:BHAGCHEM)<br><sub>📶W9 · W↑66d · ↑CMF13d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 5 | ↑76 | ↑1.025 | ↑22d | PV | +24.0% | 47.23/45.86 | +2.18% | 20% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · W↑18d · ↓CMF9d</sub> | ✓ SAFE | Stainless steel washers tubes pipes solar mounting industrial | 📈 BULL_ANY_MID | 59 | 🔄75 | ↑1.010 | ↑1d | — | +1.5% | 6.42/4.07 | +1.52% | 20% |
| [SANGAMIND](https://in.tradingview.com/chart/?symbol=NSE:SANGAMIND)<br><sub>📶W9 · W↑61d · ↓CMF30d</sub> | ✓ SAFE | PV yarn denim seamless garments textile manufacturer | 📈 BULL_ANY_MID | 53 | ↑77 | ↓1.005 | ↑7d | SQ | +3.1% | 46.76/44.93 | -0.63% | 20% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>📶W9 · W↑56d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | Pharmaceuticals: generics, branded drugs, consumer wellness products | 📈 BULL_ANY_MID | 49 | 🔄74 | ↑1.031 | ↑1d | — | +3.9% | 44.71/41.57 | +3.92% | 20% |
| [SENCO](https://in.tradingview.com/chart/?symbol=NSE:SENCO)<br><sub>↓CMF20d</sub> | ✓ SAFE | Gold diamond silver jewelry retail Eastern India | ⚡ BULL_ANY_PPV | 99 | 🔄44 | ↑1.006 | ↑1d | SQ·PV | +1.4% | -22.79/-28.1 | +1.38% | 20% |
| [DOLPHIN](https://in.tradingview.com/chart/?symbol=NSE:DOLPHIN)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 94 | 🔄21 | ↑1.020 | ↑1d | SQ·PV | +6.1% | -52.72/-57.7 | +6.07% | 20% |
| [HCLTECH](https://in.tradingview.com/chart/?symbol=NSE:HCLTECH)<br><sub>🚀SS · ↑CMF10d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 49 | 🔄3 | ↑1.033 | ↑1d | PV | +5.7% | -42.54/-49.08 | +5.74% | 20% |
| [LTM](https://in.tradingview.com/chart/?symbol=NSE:LTM)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 47 | 🔄3 | ↑1.007 | ↓13d | — | -3.6% | -56.4/-61.13 | +2.08% | 20% |
| [PRABHA](https://in.tradingview.com/chart/?symbol=NSE:PRABHA)<br><sub>↓CMF30d</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 71 | 🔄7 | ↓0.995 | ↓19d | SQ | -3.1% | -54.74/-57.91 | -0.31% | 20% 🟦 |
| [PASHUPATI](https://in.tradingview.com/chart/?symbol=NSE:PASHUPATI)<br><sub>↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄62 | ↑1.004 | ↑1d | SQ | +0.6% | -21.81/-23.6 | +0.57% | 20% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>W↑56d · 🚀SS · ↓CMF4d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 98 | 🔄55 | ↑1.013 | ↑2d | SQ | +3.2% | 2.18/-1.42 | +1.13% | 20% |
| [RHIM](https://in.tradingview.com/chart/?symbol=NSE:RHIM)<br><sub>W↑8d · ↓CMF4d</sub> | ✓ SAFE | Refractory materials for steel furnaces above 1200°C | 📈 BULL_ANY_MID | 94 | 🔄25 | ↑1.015 | ↑6d | SQ | +6.2% | 14.43/10.94 | +1.60% | 20% |
| [TORNTPOWER](https://in.tradingview.com/chart/?symbol=NSE:TORNTPOWER)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Power generation transmission distribution utility Gujarat Maharashtra | 📈 BULL_ANY_MID | 85 | 🔄47 | ↑1.001 | ↓15d | SQ | -0.5% | -39.56/-39.91 | +0.09% | 20% |
| [MAHASTEEL](https://in.tradingview.com/chart/?symbol=NSE:MAHASTEEL)<br><sub>↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 80 | 🔄86 | ↑1.001 | ↓33d | SQ | -1.1% | -38.26/-40.16 | +1.79% | 20% |
| [MUTHOOTFIN](https://in.tradingview.com/chart/?symbol=NSE:MUTHOOTFIN)<br><sub>🚀SS · ↓CMF1d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 51 | 🔄30 | ↑1.005 | ↓9d | — | -2.4% | -40.8/-42.17 | +3.40% | 20% |
| [INDIAMART](https://in.tradingview.com/chart/?symbol=NSE:INDIAMART)<br><sub>↓CMF12d</sub> | ✓ SAFE | B2B marketplace connecting MSMEs suppliers buyers online | 📈 BULL_ANY_MID | 31 | 🔄13 | ↓0.990 | ↓19d | — | -3.3% | -32.62/-33.76 | -1.10% | 20% |
| [MAZDOCK](https://in.tradingview.com/chart/?symbol=NSE:MAZDOCK)<br><sub>W↑7d · ↓CMF30d</sub> | ✓ SAFE | Defense warships submarines naval shipbuilding PSU | 📈 BULL_ANY_MID | 23 | ↑38 | ↑1.017 | ↑2d | — | +3.6% | 10.55/8.39 | +1.43% | 20% |
| [TATACHEM](https://in.tradingview.com/chart/?symbol=NSE:TATACHEM)<br><sub>↓CMF30d</sub> | ✓ SAFE | Soda ash, salt, specialty chemicals manufacturer, global exports | 📈 BULL_ANY_MID | 18 | ↑29 | ↓0.998 | ↓2d | — | +2.0% | -36.42/-39.87 | -1.14% | 20% |

```
NSE:EMBDL,NSE:OAL,NSE:SJS,NSE:SILVERTUC,NSE:RAMRAT,NSE:JINDRILL,NSE:INDOCO,NSE:HIKAL,NSE:BHAGCHEM,NSE:RATNAVEER,NSE:SANGAMIND,NSE:ZYDUSLIFE,NSE:SENCO,NSE:DOLPHIN,NSE:HCLTECH,NSE:LTM,NSE:PRABHA,NSE:PASHUPATI,NSE:DIVISLAB,NSE:RHIM,NSE:TORNTPOWER,NSE:MAHASTEEL,NSE:MUTHOOTFIN,NSE:INDIAMART,NSE:MAZDOCK,NSE:TATACHEM
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (15)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [EMBDL](https://in.tradingview.com/chart/?symbol=NSE:EMBDL)<br><sub>📶W9 · W↑54d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Residential and commercial real estate development urban markets | ⚡ BULL_ANY_PPV | 99 | 🔄24 | ↑1.010 | ↑1d | SQ·PV | +2.2% | 16.17/15.75 | +2.22% | 10% 🟨 |
| [OAL](https://in.tradingview.com/chart/?symbol=NSE:OAL)<br><sub>📶W9 · W↑66d · 🚀SS·10x · ↓CMF20d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 89 | 🔄69 | ↑1.052 | ↑1d | SQ·PV | +6.3% | -8.2/-17.82 | +6.31% | 20% |
| [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS)<br><sub>📶W9 · W↑61d · ↓CMF25d</sub> | ⚠ CAUTION | Decorative graphics manufacturing for automotive industrial sectors | ⚡ BULL_ANY_PPV | 62 | ↑89 | ↑1.007 | ↑8d | SQ·PV | +3.5% | 44.14/43.65 | +0.37% | 20% |
| [INDOCO](https://in.tradingview.com/chart/?symbol=NSE:INDOCO)<br><sub>📶W9 · W↑23d · ↑CMF19d</sub> | ✓ SAFE | Pharmaceutical manufacturer oral drugs dermatology gastrointestinal India | ⚡ BULL_ANY_PPV | 40 | ↑49 | ↑1.035 | ↑20d | SQ·PV | +21.1% | 45.58/42.29 | +3.13% | 20% |
| [SANGAMIND](https://in.tradingview.com/chart/?symbol=NSE:SANGAMIND)<br><sub>📶W9 · W↑61d · ↓CMF30d</sub> | ✓ SAFE | PV yarn denim seamless garments textile manufacturer | 📈 BULL_ANY_MID | 53 | ↑77 | ↓1.005 | ↑7d | SQ | +3.1% | 46.76/44.93 | -0.63% | 20% |
| [SENCO](https://in.tradingview.com/chart/?symbol=NSE:SENCO)<br><sub>↓CMF20d</sub> | ✓ SAFE | Gold diamond silver jewelry retail Eastern India | ⚡ BULL_ANY_PPV | 99 | 🔄44 | ↑1.006 | ↑1d | SQ·PV | +1.4% | -22.79/-28.1 | +1.38% | 20% |
| [DOLPHIN](https://in.tradingview.com/chart/?symbol=NSE:DOLPHIN)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 94 | 🔄21 | ↑1.020 | ↑1d | SQ·PV | +6.1% | -52.72/-57.7 | +6.07% | 20% |
| [PRABHA](https://in.tradingview.com/chart/?symbol=NSE:PRABHA)<br><sub>↓CMF30d</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 71 | 🔄7 | ↓0.995 | ↓19d | SQ | -3.1% | -54.74/-57.91 | -0.31% | 20% 🟦 |
| [PASHUPATI](https://in.tradingview.com/chart/?symbol=NSE:PASHUPATI)<br><sub>↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄62 | ↑1.004 | ↑1d | SQ | +0.6% | -21.81/-23.6 | +0.57% | 20% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>W↑56d · 🚀SS · ↓CMF4d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 98 | 🔄55 | ↑1.013 | ↑2d | SQ | +3.2% | 2.18/-1.42 | +1.13% | 20% |
| [RHIM](https://in.tradingview.com/chart/?symbol=NSE:RHIM)<br><sub>W↑8d · ↓CMF4d</sub> | ✓ SAFE | Refractory materials for steel furnaces above 1200°C | 📈 BULL_ANY_MID | 94 | 🔄25 | ↑1.015 | ↑6d | SQ | +6.2% | 14.43/10.94 | +1.60% | 20% |
| [TORNTPOWER](https://in.tradingview.com/chart/?symbol=NSE:TORNTPOWER)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Power generation transmission distribution utility Gujarat Maharashtra | 📈 BULL_ANY_MID | 85 | 🔄47 | ↑1.001 | ↓15d | SQ | -0.5% | -39.56/-39.91 | +0.09% | 20% |
| [MAHASTEEL](https://in.tradingview.com/chart/?symbol=NSE:MAHASTEEL)<br><sub>↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 80 | 🔄86 | ↑1.001 | ↓33d | SQ | -1.1% | -38.26/-40.16 | +1.79% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>↓CMF19d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↓37 | ↑1.004 | ↑1d | SQ | +0.4% | -36.31/-41.57 | +0.36% | 20% |
| [POWERGRID](https://in.tradingview.com/chart/?symbol=NSE:POWERGRID)<br><sub>🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↓39 | ↓1.001 | ↑2d | SQ | +0.2% | -10.75/-15.11 | -0.07% | 20% |

```
NSE:EMBDL,NSE:OAL,NSE:SJS,NSE:INDOCO,NSE:SANGAMIND,NSE:SENCO,NSE:DOLPHIN,NSE:PRABHA,NSE:PASHUPATI,NSE:DIVISLAB,NSE:RHIM,NSE:TORNTPOWER,NSE:MAHASTEEL,NSE:TATACONSUM,NSE:POWERGRID
```

---

### 🔥 MAJOR — PPV confirmed (7)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SILVERTUC](https://in.tradingview.com/chart/?symbol=NSE:SILVERTUC)<br><sub>📶W9 · 🚀SS · ↑CMF1d</sub> | ✓ SAFE | Software development and digital transformation IT services | ⚡ BULL_ANY_PPV | 54 | 🔄98 | ↑1.023 | ↑1d | PV | +3.6% | -5.51/-8.33 | +3.62% | 20% |
| [RAMRAT](https://in.tradingview.com/chart/?symbol=NSE:RAMRAT)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Enameled copper wires manufacturing electrical equipment sector | ⚡ BULL_ANY_PPV | 54 | 🔄83 | ↑1.016 | ↑1d | PV | +2.1% | 9.8/3.84 | +2.15% | 20% |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>📶W9 · 🚀SS·130x · ↑CMF0d</sub> | ✓ SAFE | Offshore jack-up rigs drilling services oil gas sector | ⚡ BULL_ANY_PPV | 49 | 🔄58 | ↑1.068 | ↑1d | PV | +11.3% | -39.14/-49.64 | +11.26% | 20% |
| [HIKAL](https://in.tradingview.com/chart/?symbol=NSE:HIKAL)<br><sub>📶W9 · W↑18d · RVOL28x · ↓CMF1d</sub> | ✓ SAFE | APIs and specialty chemicals for pharma, crop protection | ⚡ BULL_ANY_PPV | 35 | 🔄51 | ↑1.044 | ↑15d | PV | +20.4% | 43.34/41.19 | +5.23% | 20% |
| [BHAGCHEM](https://in.tradingview.com/chart/?symbol=NSE:BHAGCHEM)<br><sub>📶W9 · W↑66d · ↑CMF13d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 5 | ↑76 | ↑1.025 | ↑22d | PV | +24.0% | 47.23/45.86 | +2.18% | 20% |
| [HCLTECH](https://in.tradingview.com/chart/?symbol=NSE:HCLTECH)<br><sub>🚀SS · ↑CMF10d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 49 | 🔄3 | ↑1.033 | ↑1d | PV | +5.7% | -42.54/-49.08 | +5.74% | 20% |
| [UEL](https://in.tradingview.com/chart/?symbol=NSE:UEL)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 12 | ↓50 | ↑0.978 | ↓13d | PV | -7.3% | -55.46/-57.66 | +0.35% | 20% 🟦 |

```
NSE:SILVERTUC,NSE:RAMRAT,NSE:JINDRILL,NSE:HIKAL,NSE:BHAGCHEM,NSE:HCLTECH,NSE:UEL
```

### 🟢 OVERSOLD — reversal from −53/−60 (5)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [LTM](https://in.tradingview.com/chart/?symbol=NSE:LTM)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 47 | 🔄3 | ↑1.007 | ↓13d | — | -3.6% | -56.4/-61.13 | +2.08% | 20% |
| [KPITTECH](https://in.tradingview.com/chart/?symbol=NSE:KPITTECH)<br><sub>↓CMF23d</sub> | ✓ SAFE | Automotive embedded software development autonomous vehicles mobility | 🟢 BULL_OVERSOLD | 11 | ↓0 | ↑0.909 | ↓14d | — | -25.6% | -74.23/-75.68 | -1.39% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>🚀SS · ↓CMF8d</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 5 | ↓50 | ↑0.995 | ↓22d | — | -9.7% | -60.32/-63.96 | +1.29% | 20% |
| [JINDALSTEL](https://in.tradingview.com/chart/?symbol=NSE:JINDALSTEL)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 5 | ↓38 | ↑0.982 | ↓35d | — | -15.2% | -70.63/-73.17 | +0.98% | 20% |
| [INFY](https://in.tradingview.com/chart/?symbol=NSE:INFY)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 18 | ↓2 | ↑1.001 | ↓12d | — | -8.4% | -50.54/-55.6 | +0.59% | 20% |

```
NSE:LTM,NSE:KPITTECH,NSE:TATASTEEL,NSE:JINDALSTEL,NSE:INFY
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (15)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>📶W9 · W↑18d · ↓CMF9d</sub> | ✓ SAFE | Stainless steel washers tubes pipes solar mounting industrial | 📈 BULL_ANY_MID | 59 | 🔄75 | ↑1.010 | ↑1d | — | +1.5% | 6.42/4.07 | +1.52% | 20% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>📶W9 · W↑56d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | Pharmaceuticals: generics, branded drugs, consumer wellness products | 📈 BULL_ANY_MID | 49 | 🔄74 | ↑1.031 | ↑1d | — | +3.9% | 44.71/41.57 | +3.92% | 20% |
| [MUTHOOTFIN](https://in.tradingview.com/chart/?symbol=NSE:MUTHOOTFIN)<br><sub>🚀SS · ↓CMF1d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 51 | 🔄30 | ↑1.005 | ↓9d | — | -2.4% | -40.8/-42.17 | +3.40% | 20% |
| [INDIAMART](https://in.tradingview.com/chart/?symbol=NSE:INDIAMART)<br><sub>↓CMF12d</sub> | ✓ SAFE | B2B marketplace connecting MSMEs suppliers buyers online | 📈 BULL_ANY_MID | 31 | 🔄13 | ↓0.990 | ↓19d | — | -3.3% | -32.62/-33.76 | -1.10% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>W↑14d · 🚀SS · ↑CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 27 | ↓7 | ↑1.002 | ↑3d | — | +1.1% | 6.95/5.11 | +0.07% | 20% |
| [BEL](https://in.tradingview.com/chart/?symbol=NSE:BEL)<br><sub>🚀SS · ↓CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 27 | ↓41 | ↑1.006 | ↑3d | — | +1.5% | -0.82/-6.13 | +0.71% | 20% |
| [TECHM](https://in.tradingview.com/chart/?symbol=NSE:TECHM)<br><sub>🚀SS · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 23 | ↓22 | ↑1.004 | ↓7d | — | -0.5% | -41.06/-43.01 | +1.64% | 20% |
| [MAZDOCK](https://in.tradingview.com/chart/?symbol=NSE:MAZDOCK)<br><sub>W↑7d · ↓CMF30d</sub> | ✓ SAFE | Defense warships submarines naval shipbuilding PSU | 📈 BULL_ANY_MID | 23 | ↑38 | ↑1.017 | ↑2d | — | +3.6% | 10.55/8.39 | +1.43% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>W↑14d · ↓CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 18 | ↓34 | ↓1.003 | ↑2d | — | +1.2% | 11.82/9.95 | -0.85% | 20% |
| [TATACHEM](https://in.tradingview.com/chart/?symbol=NSE:TATACHEM)<br><sub>↓CMF30d</sub> | ✓ SAFE | Soda ash, salt, specialty chemicals manufacturer, global exports | 📈 BULL_ANY_MID | 18 | ↑29 | ↓0.998 | ↓2d | — | +2.0% | -36.42/-39.87 | -1.14% | 20% |
| [VBL](https://in.tradingview.com/chart/?symbol=NSE:VBL)<br><sub>🚀SS · ↓CMF10d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 16 | ↓67 | ↑1.004 | ↓14d | — | -1.2% | -13.92/-16.25 | +1.07% | 20% |
| [WIPRO](https://in.tradingview.com/chart/?symbol=NSE:WIPRO)<br><sub>🚀SS · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 10 | ↓4 | ↑1.001 | ↓32d | — | -8.5% | -44.09/-47.74 | +1.03% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>🚀SS · ↓CMF15d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓67 | ↑0.984 | ↓31d | — | -9.0% | -43.92/-44.37 | +0.45% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>🚀SS · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓50 | ↑0.994 | ↓24d | — | -4.0% | -45.22/-45.43 | +0.10% | 20% |
| [E2E](https://in.tradingview.com/chart/?symbol=NSE:E2E)<br><sub>↓CMF11d</sub> | ✓ SAFE | Cloud GPU infrastructure for AI and machine learning applications | 📈 BULL_ANY_MID | 5 | ↓0 | ↑0.905 | ↓37d | — | -87.5% | -21.85/-21.92 | +2.02% | 20% |

```
NSE:RATNAVEER,NSE:ZYDUSLIFE,NSE:MUTHOOTFIN,NSE:INDIAMART,NSE:ITC,NSE:BEL,NSE:TECHM,NSE:MAZDOCK,NSE:BPCL,NSE:TATACHEM,NSE:VBL,NSE:WIPRO,NSE:HINDALCO,NSE:COALINDIA,NSE:E2E
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
