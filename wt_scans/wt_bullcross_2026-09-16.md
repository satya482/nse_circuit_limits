> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-09-16
*Generated 2026-09-16 15:46 IST*

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

**Total bull crosses today: 41** · 13 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:NPST,NSE:INDUSTOWER,NSE:CSBBANK,NSE:ARROWGREEN,NSE:FOSECOIND,NSE:SIGMAADV,NSE:HINDALCO,NSE:EQUITASBNK,NSE:ECLERX,NSE:ACE,NSE:TORNTPHARM,NSE:GRPLTD,NSE:LALPATHLAB,NSE:AKCAPIT,NSE:PRSMJOHNSN,NSE:HINDZINC,NSE:ADANIENT,NSE:BOSCHLTD,NSE:GPTHEALTH,NSE:CMSINFO,NSE:GODAVARIB,NSE:IPL,NSE:J&KBANK,NSE:SAATVIKGL,NSE:GODREJIND,NSE:EIHOTEL,NSE:TRUALT,NSE:ASTRAZEN,NSE:CUMMINSIND,NSE:ASHIANA,NSE:NTPCGREEN,NSE:TRANSRAILL,NSE:HAVELLS,NSE:PGHL,NSE:CAPITALSFB,NSE:BHARATRAS,NSE:KEI,NSE:SILVERTUC,NSE:ICICIPRULI,NSE:RECLTD,NSE:EXIDEIND
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (19)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [NPST](https://in.tradingview.com/chart/?symbol=NSE:NPST)<br><sub>📶W9 · W↑23d · 🚀SS·63x · ↑CMF0d</sub> | ✓ SAFE | UPI payments software provider fintech digital banking | ⚡ BULL_ANY_PPV | 89 | 🔄78 | ↑1.073 | ↑1d | SQ·PV | +11.9% | 41.63/37.42 | +11.90% | 10% 🟨 |
| [INDUSTOWER](https://in.tradingview.com/chart/?symbol=NSE:INDUSTOWER)<br><sub>📶W9 · W↑5d · ↑CMF8d</sub> | ✓ SAFE | Telecom tower infrastructure operator serving mobile networks | ⚡ BULL_ANY_PPV | 54 | 🔄33 | ↑1.025 | ↑1d | PV | +4.3% | -30.53/-37.66 | +4.30% | 20% |
| [CSBBANK](https://in.tradingview.com/chart/?symbol=NSE:CSBBANK)<br><sub>📶W9 · 🚀SS·16x · ↑CMF0d</sub> | ✓ SAFE | Private bank SME retail NRI lending Kerala focus | ⚡ BULL_ANY_PPV | 49 | 🔄25 | ↑1.042 | ↑1d | PV | +10.9% | -35.39/-38.11 | +10.93% | 20% |
| [ARROWGREEN](https://in.tradingview.com/chart/?symbol=NSE:ARROWGREEN)<br><sub>📶W9 · W↑8d · RVOL10x · ★ · ↑CMF30d</sub> | ✓ SAFE | Water-soluble films, security products, agriculture exports | ⚡ BULL_ANY_PPV | 8 | ↑96 | ↑1.110 | ↑12d | PV | +29.3% | 34.98/29.97 | +8.22% | 5% |
| [FOSECOIND](https://in.tradingview.com/chart/?symbol=NSE:FOSECOIND)<br><sub>📶W9 · W↑33d · RVOL10x · ↑CMF16d</sub> | ✓ SAFE | Foundry chemicals consumables metallurgical casting additives manufacturer | ⚡ BULL_ANY_PPV | 3 | ↑82 | ↑1.089 | ↑17d | PV | +27.8% | 51.25/42.74 | +10.01% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 91 | 🔄61 | ↑1.003 | ↓9d | SQ | -0.3% | -18.92/-20.04 | +1.17% | 20% |
| [EQUITASBNK](https://in.tradingview.com/chart/?symbol=NSE:EQUITASBNK)<br><sub>📶W9 · ↓CMF13d</sub> | ⚠ CAUTION | Small finance bank serving underbanked individuals and SMEs | 📈 BULL_ANY_MID | 69 | ↑68 | ↑1.007 | ↑1d | SQ | +3.0% | -46.11/-48.71 | +3.01% | 20% |
| [ECLERX](https://in.tradingview.com/chart/?symbol=NSE:ECLERX)<br><sub>📶W9 · W↑58d · ↓CMF4d</sub> | ✓ SAFE | Legal document processing, BPM automation, financial services outsourcing | 📈 BULL_ANY_MID | 64 | ↑71 | ↑1.021 | ↑1d | SQ | +3.5% | 9.89/9.35 | +3.50% | 20% |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Mobile cranes, material handling equipment for construction sector | 📈 BULL_ANY_MID | 63 | ↑71 | ↑1.017 | ↑2d | SQ | +1.8% | 5.32/0.96 | +1.55% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑67 | ↓0.997 | ↓2d | SQ | +0.2% | -3.46/-4.79 | -0.71% | 20% |
| [GRPLTD](https://in.tradingview.com/chart/?symbol=NSE:GRPLTD)<br><sub>📶W9 · ↑CMF1d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑57 | ↓0.996 | ↓2d | SQ | +2.8% | -11.65/-12.73 | -3.27% | 20% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>📶W9 · RVOL9x · ↓CMF0d</sub> | ✓ SAFE | Diagnostic lab network pathology testing healthcare services | 📈 BULL_ANY_MID | 54 | ↑77 | ↓0.994 | ↓6d | SQ | -0.9% | 14.76/7.33 | -0.56% | 20% |
| [AKCAPIT](https://in.tradingview.com/chart/?symbol=NSE:AKCAPIT)<br><sub>📶W9 · ↑CMF0d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 54 | ↑50 | ↓0.994 | ↓6d | SQ | -0.7% | -19.31/-20.34 | -0.29% | 20% |
| [PRSMJOHNSN](https://in.tradingview.com/chart/?symbol=NSE:PRSMJOHNSN)<br><sub>📶W9 · W↑23d · ↓CMF30d</sub> | ✓ SAFE | Cement tiles sanitaryware RMC residential commercial construction | 📈 BULL_ANY_MID | 48 | ↑28 | ↑1.015 | ↑17d | SQ | +6.9% | 38.56/38.55 | +2.14% | 20% |
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>📶W9 · W↑28d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 28 | ↑65 | ↑1.014 | ↑2d | — | +2.7% | 24.78/23.85 | +1.56% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · ↓CMF7d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 19 | ↑77 | ↑1.039 | ↑1d | — | +5.1% | -9.05/-16.39 | +5.11% | 20% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>📶W9 · W↑109d · ↑CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.015 | ↑3d | — | +4.4% | 32.49/29.43 | +0.17% | 20% |
| [GPTHEALTH](https://in.tradingview.com/chart/?symbol=NSE:GPTHEALTH)<br><sub>📶W9 · W↑3d · ↑CMF5d</sub> | ✓ SAFE | Multispecialty hospital chain secondary tertiary care Eastern India | 📈 BULL_ANY_MID | 15 | ↑68 | ↑1.024 | ↑10d | — | +8.3% | 27.86/26.42 | +2.41% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:NPST,NSE:INDUSTOWER,NSE:CSBBANK,NSE:ARROWGREEN,NSE:FOSECOIND,NSE:SIGMAADV,NSE:HINDALCO,NSE:EQUITASBNK,NSE:ECLERX,NSE:ACE,NSE:TORNTPHARM,NSE:GRPLTD,NSE:LALPATHLAB,NSE:AKCAPIT,NSE:PRSMJOHNSN,NSE:HINDZINC,NSE:ADANIENT,NSE:BOSCHLTD,NSE:GPTHEALTH
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (37)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [NPST](https://in.tradingview.com/chart/?symbol=NSE:NPST)<br><sub>📶W9 · W↑23d · 🚀SS·63x · ↑CMF0d</sub> | ✓ SAFE | UPI payments software provider fintech digital banking | ⚡ BULL_ANY_PPV | 89 | 🔄78 | ↑1.073 | ↑1d | SQ·PV | +11.9% | 41.63/37.42 | +11.90% | 10% 🟨 |
| [INDUSTOWER](https://in.tradingview.com/chart/?symbol=NSE:INDUSTOWER)<br><sub>📶W9 · W↑5d · ↑CMF8d</sub> | ✓ SAFE | Telecom tower infrastructure operator serving mobile networks | ⚡ BULL_ANY_PPV | 54 | 🔄33 | ↑1.025 | ↑1d | PV | +4.3% | -30.53/-37.66 | +4.30% | 20% |
| [CSBBANK](https://in.tradingview.com/chart/?symbol=NSE:CSBBANK)<br><sub>📶W9 · 🚀SS·16x · ↑CMF0d</sub> | ✓ SAFE | Private bank SME retail NRI lending Kerala focus | ⚡ BULL_ANY_PPV | 49 | 🔄25 | ↑1.042 | ↑1d | PV | +10.9% | -35.39/-38.11 | +10.93% | 20% |
| [ARROWGREEN](https://in.tradingview.com/chart/?symbol=NSE:ARROWGREEN)<br><sub>📶W9 · W↑8d · RVOL10x · ★ · ↑CMF30d</sub> | ✓ SAFE | Water-soluble films, security products, agriculture exports | ⚡ BULL_ANY_PPV | 8 | ↑96 | ↑1.110 | ↑12d | PV | +29.3% | 34.98/29.97 | +8.22% | 5% |
| [FOSECOIND](https://in.tradingview.com/chart/?symbol=NSE:FOSECOIND)<br><sub>📶W9 · W↑33d · RVOL10x · ↑CMF16d</sub> | ✓ SAFE | Foundry chemicals consumables metallurgical casting additives manufacturer | ⚡ BULL_ANY_PPV | 3 | ↑82 | ↑1.089 | ↑17d | PV | +27.8% | 51.25/42.74 | +10.01% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 91 | 🔄61 | ↑1.003 | ↓9d | SQ | -0.3% | -18.92/-20.04 | +1.17% | 20% |
| [EQUITASBNK](https://in.tradingview.com/chart/?symbol=NSE:EQUITASBNK)<br><sub>📶W9 · ↓CMF13d</sub> | ⚠ CAUTION | Small finance bank serving underbanked individuals and SMEs | 📈 BULL_ANY_MID | 69 | ↑68 | ↑1.007 | ↑1d | SQ | +3.0% | -46.11/-48.71 | +3.01% | 20% |
| [ECLERX](https://in.tradingview.com/chart/?symbol=NSE:ECLERX)<br><sub>📶W9 · W↑58d · ↓CMF4d</sub> | ✓ SAFE | Legal document processing, BPM automation, financial services outsourcing | 📈 BULL_ANY_MID | 64 | ↑71 | ↑1.021 | ↑1d | SQ | +3.5% | 9.89/9.35 | +3.50% | 20% |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Mobile cranes, material handling equipment for construction sector | 📈 BULL_ANY_MID | 63 | ↑71 | ↑1.017 | ↑2d | SQ | +1.8% | 5.32/0.96 | +1.55% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑67 | ↓0.997 | ↓2d | SQ | +0.2% | -3.46/-4.79 | -0.71% | 20% |
| [GRPLTD](https://in.tradingview.com/chart/?symbol=NSE:GRPLTD)<br><sub>📶W9 · ↑CMF1d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑57 | ↓0.996 | ↓2d | SQ | +2.8% | -11.65/-12.73 | -3.27% | 20% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>📶W9 · RVOL9x · ↓CMF0d</sub> | ✓ SAFE | Diagnostic lab network pathology testing healthcare services | 📈 BULL_ANY_MID | 54 | ↑77 | ↓0.994 | ↓6d | SQ | -0.9% | 14.76/7.33 | -0.56% | 20% |
| [AKCAPIT](https://in.tradingview.com/chart/?symbol=NSE:AKCAPIT)<br><sub>📶W9 · ↑CMF0d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 54 | ↑50 | ↓0.994 | ↓6d | SQ | -0.7% | -19.31/-20.34 | -0.29% | 20% |
| [PRSMJOHNSN](https://in.tradingview.com/chart/?symbol=NSE:PRSMJOHNSN)<br><sub>📶W9 · W↑23d · ↓CMF30d</sub> | ✓ SAFE | Cement tiles sanitaryware RMC residential commercial construction | 📈 BULL_ANY_MID | 48 | ↑28 | ↑1.015 | ↑17d | SQ | +6.9% | 38.56/38.55 | +2.14% | 20% |
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>📶W9 · W↑28d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 28 | ↑65 | ↑1.014 | ↑2d | — | +2.7% | 24.78/23.85 | +1.56% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · ↓CMF7d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 19 | ↑77 | ↑1.039 | ↑1d | — | +5.1% | -9.05/-16.39 | +5.11% | 20% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>📶W9 · W↑109d · ↑CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.015 | ↑3d | — | +4.4% | 32.49/29.43 | +0.17% | 20% |
| [GPTHEALTH](https://in.tradingview.com/chart/?symbol=NSE:GPTHEALTH)<br><sub>📶W9 · W↑3d · ↑CMF5d</sub> | ✓ SAFE | Multispecialty hospital chain secondary tertiary care Eastern India | 📈 BULL_ANY_MID | 15 | ↑68 | ↑1.024 | ↑10d | — | +8.3% | 27.86/26.42 | +2.41% | 20% |
| [CMSINFO](https://in.tradingview.com/chart/?symbol=NSE:CMSINFO)<br><sub>🚀SS · ↓CMF27d · 🎯SLING</sub> | ✓ SAFE | Cash management, ATM networks, retail banking infrastructure | 🔥 BULL_OS_PPV | 40 | 🔄3 | ↑1.001 | ↓33d | PV | -11.9% | -59.23/-63.52 | +4.25% | 20% |
| [GODAVARIB](https://in.tradingview.com/chart/?symbol=NSE:GODAVARIB)<br><sub>RVOL114x · ↓CMF6d · ÷DIV</sub> | ✓ SAFE | Sugarcane biorefinery making chemicals ethanol power and sugar | ⚡ BULL_ANY_PPV | 92 | 🔄12 | ↑1.003 | ↓8d | SQ·PV | -2.0% | -41.53/-43.68 | +4.55% | 20% |
| [IPL](https://in.tradingview.com/chart/?symbol=NSE:IPL)<br><sub>🚀SS·355x · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Agrochemical manufacturer crop protection pesticides farming | ⚡ BULL_ANY_PPV | 69 | ↑14 | ↑1.015 | ↑1d | SQ·PV | +3.8% | -45.82/-57.52 | +3.84% | 20% |
| [J&KBANK](https://in.tradingview.com/chart/?symbol=NSE:J&KBANK)<br><sub>🚀SS · ↓CMF14d</sub> | ✓ SAFE | Retail corporate banking services Jammu Kashmir Ladakh regions | ⚡ BULL_ANY_PPV | 69 | ↑73 | ↑1.006 | ↑1d | SQ·PV | +2.0% | -42.9/-46.25 | +2.01% | 20% |
| [SAATVIKGL](https://in.tradingview.com/chart/?symbol=NSE:SAATVIKGL)<br><sub>🚀SS·11x · ↓CMF30d</sub> | ✓ SAFE | Solar modules manufacturing, EPC, renewable energy | ⚡ BULL_ANY_PPV | 59 | 🔄50 | ↑1.015 | ↑1d | PV | +6.1% | -41.47/-43.83 | +6.08% | 20% |
| [GODREJIND](https://in.tradingview.com/chart/?symbol=NSE:GODREJIND)<br><sub>↓CMF25d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Oleochemicals, real estate, agriculture, chemicals holding company | ⚡ BULL_ANY_PPV | 40 | 🔄61 | ↑1.001 | ↓33d | PV | -13.7% | -54.05/-56.08 | +2.94% | 20% |
| [EIHOTEL](https://in.tradingview.com/chart/?symbol=NSE:EIHOTEL)<br><sub>🚀SS · ↓CMF28d · ÷DIV</sub> | ⚠ CAUTION | Luxury hotels, resorts, flight catering operations | ⚡ BULL_ANY_PPV | 29 | ↑18 | ↑1.009 | ↑1d | PV | +2.9% | -47.69/-50.97 | +2.92% | 20% |
| [TRUALT](https://in.tradingview.com/chart/?symbol=NSE:TRUALT)<br><sub>↓CMF10d</sub> | ✓ SAFE | Ethanol and biogas producer, renewable energy, fuel sector | ⚡ BULL_ANY_PPV | 10 | ↑50 | ↑1.003 | ↓33d | PV | -0.1% | -40.58/-40.86 | +2.68% | 20% |
| [ASTRAZEN](https://in.tradingview.com/chart/?symbol=NSE:ASTRAZEN)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Prescription drugs oncology cardiology respiratory diseases India | ⚡ BULL_ANY_PPV | 5 | ↑8 | ↑0.981 | ↓29d | PV | -17.0% | -57.7/-58.27 | +0.11% | 20% |
| [CUMMINSIND](https://in.tradingview.com/chart/?symbol=NSE:CUMMINSIND)<br><sub>↑CMF1d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 59 | 🔄54 | ↑1.012 | ↑1d | — | +2.7% | -56.42/-62.44 | +2.68% | 20% |
| [ASHIANA](https://in.tradingview.com/chart/?symbol=NSE:ASHIANA)<br><sub>↓CMF3d · 🎯SLING</sub> | ⚠ CAUTION | Senior living housing developer for Indian retirees | 🟢 BULL_OVERSOLD | 35 | 🔄56 | ↑0.994 | ↓39d | — | -8.2% | -66.38/-67.66 | +1.89% | 20% |
| [NTPCGREEN](https://in.tradingview.com/chart/?symbol=NSE:NTPCGREEN)<br><sub>↓CMF19d · 🎯SLING</sub> | ⚠ CAUTION | Solar and wind power projects for grid distribution | 🟢 BULL_OVERSOLD | 8 | ↑31 | ↑0.998 | ↓17d | — | -4.2% | -68.26/-68.68 | +2.01% | 20% |
| [PGHL](https://in.tradingview.com/chart/?symbol=NSE:PGHL)<br><sub>↓CMF29d · 🎯SLING</sub> | ⚠ CAUTION | Vitamins minerals supplements pharmaceuticals consumer health | 🟢 BULL_OVERSOLD | 5 | ↑39 | ↑0.990 | ↓50d | — | -12.8% | -61.36/-63.69 | +0.96% | 20% |
| [CAPITALSFB](https://in.tradingview.com/chart/?symbol=NSE:CAPITALSFB)<br><sub>🚀SS · ↓CMF23d · 🎯SLING</sub> | ⚠ CAUTION | Retail banking microfinance credit middle-income underserved segments | 🟢 BULL_OVERSOLD | 5 | ↑50 | ↑0.993 | ↓36d | — | -7.8% | -71.22/-71.99 | +1.32% | 20% |
| [BHARATRAS](https://in.tradingview.com/chart/?symbol=NSE:BHARATRAS)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 35 | 🔄2 | ↑0.989 | ↓33d | — | -9.6% | -58.53/-58.75 | +2.52% | 20% |
| [ICICIPRULI](https://in.tradingview.com/chart/?symbol=NSE:ICICIPRULI)<br><sub>🚀SS · ↓CMF6d</sub> | ✓ SAFE | Life insurance policies pensions health coverage retail corporate | 📈 BULL_ANY_MID | 42 | 🔄18 | ↑0.990 | ↓13d | — | -7.1% | -52.21/-52.26 | +2.71% | 20% |
| [RECLTD](https://in.tradingview.com/chart/?symbol=NSE:RECLTD)<br><sub>🚀SS · ↓CMF20d</sub> | ✓ SAFE | Power sector financing, generation to distribution infrastructure | 📈 BULL_ANY_MID | 5 | ↑24 | ↑0.994 | ↓29d | — | -13.5% | -48.35/-48.37 | +1.35% | 20% |
| [EXIDEIND](https://in.tradingview.com/chart/?symbol=NSE:EXIDEIND)<br><sub>↓CMF14d</sub> | ✓ SAFE | Lead-acid batteries automobiles industrial power backup | 📈 BULL_ANY_MID | 5 | ↑67 | ↑0.992 | ↓36d | — | -1.9% | -46.56/-46.89 | +1.54% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:NPST,NSE:INDUSTOWER,NSE:CSBBANK,NSE:ARROWGREEN,NSE:FOSECOIND,NSE:SIGMAADV,NSE:HINDALCO,NSE:EQUITASBNK,NSE:ECLERX,NSE:ACE,NSE:TORNTPHARM,NSE:GRPLTD,NSE:LALPATHLAB,NSE:AKCAPIT,NSE:PRSMJOHNSN,NSE:HINDZINC,NSE:ADANIENT,NSE:BOSCHLTD,NSE:GPTHEALTH,NSE:CMSINFO,NSE:GODAVARIB,NSE:IPL,NSE:J&KBANK,NSE:SAATVIKGL,NSE:GODREJIND,NSE:EIHOTEL,NSE:TRUALT,NSE:ASTRAZEN,NSE:CUMMINSIND,NSE:ASHIANA,NSE:NTPCGREEN,NSE:PGHL,NSE:CAPITALSFB,NSE:BHARATRAS,NSE:ICICIPRULI,NSE:RECLTD,NSE:EXIDEIND
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (13)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [NPST](https://in.tradingview.com/chart/?symbol=NSE:NPST)<br><sub>📶W9 · W↑23d · 🚀SS·63x · ↑CMF0d</sub> | ✓ SAFE | UPI payments software provider fintech digital banking | ⚡ BULL_ANY_PPV | 89 | 🔄78 | ↑1.073 | ↑1d | SQ·PV | +11.9% | 41.63/37.42 | +11.90% | 10% 🟨 |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 91 | 🔄61 | ↑1.003 | ↓9d | SQ | -0.3% | -18.92/-20.04 | +1.17% | 20% |
| [EQUITASBNK](https://in.tradingview.com/chart/?symbol=NSE:EQUITASBNK)<br><sub>📶W9 · ↓CMF13d</sub> | ⚠ CAUTION | Small finance bank serving underbanked individuals and SMEs | 📈 BULL_ANY_MID | 69 | ↑68 | ↑1.007 | ↑1d | SQ | +3.0% | -46.11/-48.71 | +3.01% | 20% |
| [ECLERX](https://in.tradingview.com/chart/?symbol=NSE:ECLERX)<br><sub>📶W9 · W↑58d · ↓CMF4d</sub> | ✓ SAFE | Legal document processing, BPM automation, financial services outsourcing | 📈 BULL_ANY_MID | 64 | ↑71 | ↑1.021 | ↑1d | SQ | +3.5% | 9.89/9.35 | +3.50% | 20% |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Mobile cranes, material handling equipment for construction sector | 📈 BULL_ANY_MID | 63 | ↑71 | ↑1.017 | ↑2d | SQ | +1.8% | 5.32/0.96 | +1.55% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑67 | ↓0.997 | ↓2d | SQ | +0.2% | -3.46/-4.79 | -0.71% | 20% |
| [GRPLTD](https://in.tradingview.com/chart/?symbol=NSE:GRPLTD)<br><sub>📶W9 · ↑CMF1d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑57 | ↓0.996 | ↓2d | SQ | +2.8% | -11.65/-12.73 | -3.27% | 20% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>📶W9 · RVOL9x · ↓CMF0d</sub> | ✓ SAFE | Diagnostic lab network pathology testing healthcare services | 📈 BULL_ANY_MID | 54 | ↑77 | ↓0.994 | ↓6d | SQ | -0.9% | 14.76/7.33 | -0.56% | 20% |
| [AKCAPIT](https://in.tradingview.com/chart/?symbol=NSE:AKCAPIT)<br><sub>📶W9 · ↑CMF0d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 54 | ↑50 | ↓0.994 | ↓6d | SQ | -0.7% | -19.31/-20.34 | -0.29% | 20% |
| [PRSMJOHNSN](https://in.tradingview.com/chart/?symbol=NSE:PRSMJOHNSN)<br><sub>📶W9 · W↑23d · ↓CMF30d</sub> | ✓ SAFE | Cement tiles sanitaryware RMC residential commercial construction | 📈 BULL_ANY_MID | 48 | ↑28 | ↑1.015 | ↑17d | SQ | +6.9% | 38.56/38.55 | +2.14% | 20% |
| [GODAVARIB](https://in.tradingview.com/chart/?symbol=NSE:GODAVARIB)<br><sub>RVOL114x · ↓CMF6d · ÷DIV</sub> | ✓ SAFE | Sugarcane biorefinery making chemicals ethanol power and sugar | ⚡ BULL_ANY_PPV | 92 | 🔄12 | ↑1.003 | ↓8d | SQ·PV | -2.0% | -41.53/-43.68 | +4.55% | 20% |
| [IPL](https://in.tradingview.com/chart/?symbol=NSE:IPL)<br><sub>🚀SS·355x · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Agrochemical manufacturer crop protection pesticides farming | ⚡ BULL_ANY_PPV | 69 | ↑14 | ↑1.015 | ↑1d | SQ·PV | +3.8% | -45.82/-57.52 | +3.84% | 20% |
| [J&KBANK](https://in.tradingview.com/chart/?symbol=NSE:J&KBANK)<br><sub>🚀SS · ↓CMF14d</sub> | ✓ SAFE | Retail corporate banking services Jammu Kashmir Ladakh regions | ⚡ BULL_ANY_PPV | 69 | ↑73 | ↑1.006 | ↑1d | SQ·PV | +2.0% | -42.9/-46.25 | +2.01% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:NPST,NSE:HINDALCO,NSE:EQUITASBNK,NSE:ECLERX,NSE:ACE,NSE:TORNTPHARM,NSE:GRPLTD,NSE:LALPATHLAB,NSE:AKCAPIT,NSE:PRSMJOHNSN,NSE:GODAVARIB,NSE:IPL,NSE:J&KBANK
```

---

### 🔥 MAJOR — PPV confirmed (11)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [INDUSTOWER](https://in.tradingview.com/chart/?symbol=NSE:INDUSTOWER)<br><sub>📶W9 · W↑5d · ↑CMF8d</sub> | ✓ SAFE | Telecom tower infrastructure operator serving mobile networks | ⚡ BULL_ANY_PPV | 54 | 🔄33 | ↑1.025 | ↑1d | PV | +4.3% | -30.53/-37.66 | +4.30% | 20% |
| [CSBBANK](https://in.tradingview.com/chart/?symbol=NSE:CSBBANK)<br><sub>📶W9 · 🚀SS·16x · ↑CMF0d</sub> | ✓ SAFE | Private bank SME retail NRI lending Kerala focus | ⚡ BULL_ANY_PPV | 49 | 🔄25 | ↑1.042 | ↑1d | PV | +10.9% | -35.39/-38.11 | +10.93% | 20% |
| [ARROWGREEN](https://in.tradingview.com/chart/?symbol=NSE:ARROWGREEN)<br><sub>📶W9 · W↑8d · RVOL10x · ★ · ↑CMF30d</sub> | ✓ SAFE | Water-soluble films, security products, agriculture exports | ⚡ BULL_ANY_PPV | 8 | ↑96 | ↑1.110 | ↑12d | PV | +29.3% | 34.98/29.97 | +8.22% | 5% |
| [FOSECOIND](https://in.tradingview.com/chart/?symbol=NSE:FOSECOIND)<br><sub>📶W9 · W↑33d · RVOL10x · ↑CMF16d</sub> | ✓ SAFE | Foundry chemicals consumables metallurgical casting additives manufacturer | ⚡ BULL_ANY_PPV | 3 | ↑82 | ↑1.089 | ↑17d | PV | +27.8% | 51.25/42.74 | +10.01% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [CMSINFO](https://in.tradingview.com/chart/?symbol=NSE:CMSINFO)<br><sub>🚀SS · ↓CMF27d · 🎯SLING</sub> | ✓ SAFE | Cash management, ATM networks, retail banking infrastructure | 🔥 BULL_OS_PPV | 40 | 🔄3 | ↑1.001 | ↓33d | PV | -11.9% | -59.23/-63.52 | +4.25% | 20% |
| [SAATVIKGL](https://in.tradingview.com/chart/?symbol=NSE:SAATVIKGL)<br><sub>🚀SS·11x · ↓CMF30d</sub> | ✓ SAFE | Solar modules manufacturing, EPC, renewable energy | ⚡ BULL_ANY_PPV | 59 | 🔄50 | ↑1.015 | ↑1d | PV | +6.1% | -41.47/-43.83 | +6.08% | 20% |
| [GODREJIND](https://in.tradingview.com/chart/?symbol=NSE:GODREJIND)<br><sub>↓CMF25d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Oleochemicals, real estate, agriculture, chemicals holding company | ⚡ BULL_ANY_PPV | 40 | 🔄61 | ↑1.001 | ↓33d | PV | -13.7% | -54.05/-56.08 | +2.94% | 20% |
| [EIHOTEL](https://in.tradingview.com/chart/?symbol=NSE:EIHOTEL)<br><sub>🚀SS · ↓CMF28d · ÷DIV</sub> | ⚠ CAUTION | Luxury hotels, resorts, flight catering operations | ⚡ BULL_ANY_PPV | 29 | ↑18 | ↑1.009 | ↑1d | PV | +2.9% | -47.69/-50.97 | +2.92% | 20% |
| [TRUALT](https://in.tradingview.com/chart/?symbol=NSE:TRUALT)<br><sub>↓CMF10d</sub> | ✓ SAFE | Ethanol and biogas producer, renewable energy, fuel sector | ⚡ BULL_ANY_PPV | 10 | ↑50 | ↑1.003 | ↓33d | PV | -0.1% | -40.58/-40.86 | +2.68% | 20% |
| [ASTRAZEN](https://in.tradingview.com/chart/?symbol=NSE:ASTRAZEN)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Prescription drugs oncology cardiology respiratory diseases India | ⚡ BULL_ANY_PPV | 5 | ↑8 | ↑0.981 | ↓29d | PV | -17.0% | -57.7/-58.27 | +0.11% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:INDUSTOWER,NSE:CSBBANK,NSE:ARROWGREEN,NSE:FOSECOIND,NSE:SIGMAADV,NSE:CMSINFO,NSE:SAATVIKGL,NSE:GODREJIND,NSE:EIHOTEL,NSE:TRUALT,NSE:ASTRAZEN
```

### 🟢 OVERSOLD — reversal from −53/−60 (10)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CUMMINSIND](https://in.tradingview.com/chart/?symbol=NSE:CUMMINSIND)<br><sub>↑CMF1d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 59 | 🔄54 | ↑1.012 | ↑1d | — | +2.7% | -56.42/-62.44 | +2.68% | 20% |
| [ASHIANA](https://in.tradingview.com/chart/?symbol=NSE:ASHIANA)<br><sub>↓CMF3d · 🎯SLING</sub> | ⚠ CAUTION | Senior living housing developer for Indian retirees | 🟢 BULL_OVERSOLD | 35 | 🔄56 | ↑0.994 | ↓39d | — | -8.2% | -66.38/-67.66 | +1.89% | 20% |
| [NTPCGREEN](https://in.tradingview.com/chart/?symbol=NSE:NTPCGREEN)<br><sub>↓CMF19d · 🎯SLING</sub> | ⚠ CAUTION | Solar and wind power projects for grid distribution | 🟢 BULL_OVERSOLD | 8 | ↑31 | ↑0.998 | ↓17d | — | -4.2% | -68.26/-68.68 | +2.01% | 20% |
| [TRANSRAILL](https://in.tradingview.com/chart/?symbol=NSE:TRANSRAILL)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Transmission poles and power distribution infrastructure EPC | 🟢 BULL_OVERSOLD | 7 | ↓3 | ↑0.974 | ↓18d | — | -11.6% | -66.42/-67.09 | +0.48% | 20% |
| [HAVELLS](https://in.tradingview.com/chart/?symbol=NSE:HAVELLS)<br><sub>🚀SS · ↓CMF8d · 🎯SLING</sub> | ✓ SAFE | Electrical equipment, wiring, switchgear, consumer appliances | 🟢 BULL_OVERSOLD | 5 | ↓16 | ↑0.965 | ↓44d | — | -6.9% | -61.18/-61.24 | +0.27% | 20% |
| [PGHL](https://in.tradingview.com/chart/?symbol=NSE:PGHL)<br><sub>↓CMF29d · 🎯SLING</sub> | ⚠ CAUTION | Vitamins minerals supplements pharmaceuticals consumer health | 🟢 BULL_OVERSOLD | 5 | ↑39 | ↑0.990 | ↓50d | — | -12.8% | -61.36/-63.69 | +0.96% | 20% |
| [CAPITALSFB](https://in.tradingview.com/chart/?symbol=NSE:CAPITALSFB)<br><sub>🚀SS · ↓CMF23d · 🎯SLING</sub> | ⚠ CAUTION | Retail banking microfinance credit middle-income underserved segments | 🟢 BULL_OVERSOLD | 5 | ↑50 | ↑0.993 | ↓36d | — | -7.8% | -71.22/-71.99 | +1.32% | 20% |
| [BHARATRAS](https://in.tradingview.com/chart/?symbol=NSE:BHARATRAS)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 35 | 🔄2 | ↑0.989 | ↓33d | — | -9.6% | -58.53/-58.75 | +2.52% | 20% |
| [KEI](https://in.tradingview.com/chart/?symbol=NSE:KEI)<br><sub>↓CMF8d · 🎯SLING</sub> | ✓ SAFE | Electrical wires cables high-voltage distribution power infrastructure | 🟡 BULL_OS_L2 | 11 | ↓43 | ↑0.952 | ↓14d | — | -18.6% | -55.73/-55.8 | +0.13% | 20% |
| [SILVERTUC](https://in.tradingview.com/chart/?symbol=NSE:SILVERTUC)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | IT services, digital transformation, software development, governance | 🟡 BULL_OS_L2 | 5 | ↓85 | ↑0.967 | ↓28d | — | -21.9% | -58.47/-59.34 | +2.27% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CUMMINSIND,NSE:ASHIANA,NSE:NTPCGREEN,NSE:TRANSRAILL,NSE:HAVELLS,NSE:PGHL,NSE:CAPITALSFB,NSE:BHARATRAS,NSE:KEI,NSE:SILVERTUC
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (7)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>📶W9 · W↑28d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 28 | ↑65 | ↑1.014 | ↑2d | — | +2.7% | 24.78/23.85 | +1.56% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · ↓CMF7d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 19 | ↑77 | ↑1.039 | ↑1d | — | +5.1% | -9.05/-16.39 | +5.11% | 20% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>📶W9 · W↑109d · ↑CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.015 | ↑3d | — | +4.4% | 32.49/29.43 | +0.17% | 20% |
| [GPTHEALTH](https://in.tradingview.com/chart/?symbol=NSE:GPTHEALTH)<br><sub>📶W9 · W↑3d · ↑CMF5d</sub> | ✓ SAFE | Multispecialty hospital chain secondary tertiary care Eastern India | 📈 BULL_ANY_MID | 15 | ↑68 | ↑1.024 | ↑10d | — | +8.3% | 27.86/26.42 | +2.41% | 20% |
| [ICICIPRULI](https://in.tradingview.com/chart/?symbol=NSE:ICICIPRULI)<br><sub>🚀SS · ↓CMF6d</sub> | ✓ SAFE | Life insurance policies pensions health coverage retail corporate | 📈 BULL_ANY_MID | 42 | 🔄18 | ↑0.990 | ↓13d | — | -7.1% | -52.21/-52.26 | +2.71% | 20% |
| [RECLTD](https://in.tradingview.com/chart/?symbol=NSE:RECLTD)<br><sub>🚀SS · ↓CMF20d</sub> | ✓ SAFE | Power sector financing, generation to distribution infrastructure | 📈 BULL_ANY_MID | 5 | ↑24 | ↑0.994 | ↓29d | — | -13.5% | -48.35/-48.37 | +1.35% | 20% |
| [EXIDEIND](https://in.tradingview.com/chart/?symbol=NSE:EXIDEIND)<br><sub>↓CMF14d</sub> | ✓ SAFE | Lead-acid batteries automobiles industrial power backup | 📈 BULL_ANY_MID | 5 | ↑67 | ↑0.992 | ↓36d | — | -1.9% | -46.56/-46.89 | +1.54% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:HINDZINC,NSE:ADANIENT,NSE:BOSCHLTD,NSE:GPTHEALTH,NSE:ICICIPRULI,NSE:RECLTD,NSE:EXIDEIND
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
