> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-07-23
*Generated 2026-07-23 15:44 IST*

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

**Total bull crosses today: 56** · 24 inside active squeeze

```
NSE:PIDILITIND,NSE:SHRIRAMFIN,NSE:MAHLIFE,NSE:WSTCSTPAPR,NSE:CARERATING,NSE:SURYODAY,NSE:NUVAMA,NSE:IGPL,NSE:TANLA,NSE:ROUTE,NSE:UJJIVANSFB,NSE:ANDHRSUGAR,NSE:ASTRAMICRO,NSE:GPTHEALTH,NSE:TASTYBITE,NSE:INDIGO,NSE:ASHAPURMIN,NSE:DOLPHIN,NSE:SANOFI,NSE:MARICO,NSE:JINDRILL,NSE:AEROENTER,NSE:MANKIND,NSE:TVSMOTOR,NSE:ABCAPITAL,NSE:THANGAMAYL,NSE:NESTLEIND,NSE:MACPOWER,NSE:AEGISLOG,NSE:ADANIENT,NSE:AKUMS,NSE:ASIANTILES,NSE:ANDHRAPAP,NSE:NTPCGREEN,NSE:TIRUMALCHM,NSE:SANDUMA,NSE:CRIZAC,NSE:SEAMECLTD,NSE:NTPC,NSE:SKFINDIA,NSE:HINDZINC,NSE:MUTHOOTFIN,NSE:GRASIM,NSE:GAIL,NSE:WEALTH,NSE:JAINREC,NSE:ASIANHOTNR,NSE:TATASTEEL,NSE:POWERINDIA,NSE:AEROFLEX,NSE:ENRIN,NSE:ONEPOINT,NSE:ADANIPOWER,NSE:GOLDIAM,NSE:NETWEB,NSE:PRECWIRE
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (31)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · W↑68d · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄61 | ↑1.012 | ↑1d | SQ·PV | +2.0% | 3.64/3.38 | +1.99% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑26d · 🚀SS · ↓CMF12d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 92 | 🔄79 | ↑1.024 | ↑3d | SQ·PV | +3.9% | 17.16/12.64 | +2.75% | 20% |
| [MAHLIFE](https://in.tradingview.com/chart/?symbol=NSE:MAHLIFE)<br><sub>📶W9 · W↑63d · RVOL19x · ↓CMF0d</sub> | ✓ SAFE | Residential and industrial real estate developer across India | ⚡ BULL_ANY_PPV | 68 | ↑60 | ↑1.012 | ↑2d | SQ·PV | +2.2% | 42.58/35.83 | +0.91% | 20% |
| [WSTCSTPAPR](https://in.tradingview.com/chart/?symbol=NSE:WSTCSTPAPR)<br><sub>📶W9 · W↑19d · ↑CMF1d</sub> | ✓ SAFE | Paper, paperboard, optical fiber producer for packaging and printing | ⚡ BULL_ANY_PPV | 58 | ↑75 | ↑1.048 | ↑2d | SQ·PV | +7.9% | 24.93/12.97 | +2.13% | 20% |
| [CARERATING](https://in.tradingview.com/chart/?symbol=NSE:CARERATING)<br><sub>📶W9 · W↑4d · ↑CMF0d</sub> | ⚠ CAUTION | Credit ratings for corporate debt and bonds | ⚡ BULL_ANY_PPV | 53 | ↑59 | ↑1.030 | ↑7d | SQ·PV | +4.4% | 24.99/15.72 | +3.27% | 20% |
| [SURYODAY](https://in.tradingview.com/chart/?symbol=NSE:SURYODAY)<br><sub>📶W9 · W↑77d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Microfinance bank serving unbanked rural populations credit | ⚡ BULL_ANY_PPV | 49 | 🔄86 | ↑1.046 | ↑1d | PV | +7.2% | 52.7/50.14 | +7.19% | 20% |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA)<br><sub>📶W9 · W↑77d · ↑CMF30d</sub> | ✓ SAFE | Wealth management, advisory, broking for high-net-worth individuals | ⚡ BULL_ANY_PPV | 22 | ↑89 | ↑1.029 | ↑3d | PV | +5.0% | 37.59/37.45 | +3.44% | 20% |
| [IGPL](https://in.tradingview.com/chart/?symbol=NSE:IGPL)<br><sub>📶W9 · ↓CMF13d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 18 | ↑58 | ↑1.036 | ↑2d | PV | +6.6% | -7.74/-20.44 | +3.09% | 20% |
| [TANLA](https://in.tradingview.com/chart/?symbol=NSE:TANLA)<br><sub>📶W9 · W↑77d · 🚀SS·41x · ↓CMF0d</sub> | ✓ SAFE | CPaaS provider SMS messaging enterprise customer communications | ⚡ BULL_ANY_PPV | 10 | ↑63 | ↑1.080 | ↑10d | PV | +18.6% | 66.86/62.84 | +10.13% | 20% |
| [ROUTE](https://in.tradingview.com/chart/?symbol=NSE:ROUTE)<br><sub>📶W9 · W↑89d · 🚀SS·89x · ↓CMF0d</sub> | ✓ SAFE | SMS and messaging platform for enterprises and telecom | ⚡ BULL_ANY_PPV | 9 | ↑34 | ↑1.053 | ↑11d | PV | +12.5% | 57.84/49.46 | +5.89% | 20% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>📶W9 · W↑29d · RVOL9x · ↑CMF28d</sub> | ✓ SAFE | Microfinance bank serving unbanked low-income borrowers | ⚡ BULL_ANY_PPV | 0 | ↑82 | ↑1.053 | ↑30d | PV | +29.1% | 61.95/61.94 | +5.73% | 20% |
| [ANDHRSUGAR](https://in.tradingview.com/chart/?symbol=NSE:ANDHRSUGAR)<br><sub>📶W9 · ↓CMF12d</sub> | ✓ SAFE | Sugar production and refining for domestic consumption | 📈 BULL_ANY_MID | 67 | ↑49 | ↑1.014 | ↑3d | SQ | +4.3% | -0.43/-3.34 | +1.53% | 20% |
| [ASTRAMICRO](https://in.tradingview.com/chart/?symbol=NSE:ASTRAMICRO)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | RF microwave modules defense space telecom systems | 📈 BULL_ANY_MID | 64 | ↑96 | ↑1.016 | ↑1d | SQ | +1.5% | 20.09/17.6 | +1.48% | 20% |
| [GPTHEALTH](https://in.tradingview.com/chart/?symbol=NSE:GPTHEALTH)<br><sub>📶W9 · W↑80d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 63 | ↑64 | ↑1.019 | ↑2d | SQ | +3.8% | 18.34/13.21 | +0.88% | 20% |
| [TASTYBITE](https://in.tradingview.com/chart/?symbol=NSE:TASTYBITE)<br><sub>📶W9 · W↑77d · ↓CMF30d</sub> | ✓ SAFE | Packaged ready-to-eat vegetarian meals for retail and institutional | 📈 BULL_ANY_MID | 62 | ↑71 | ↑1.027 | ↑3d | SQ | +4.5% | 49.82/47.1 | +2.56% | 20% |
| [INDIGO](https://in.tradingview.com/chart/?symbol=NSE:INDIGO)<br><sub>📶W9 · W↑45d · 🚀SS · ↑CMF29d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄49 | ↑1.008 | ↑1d | — | +1.1% | 20.36/20.19 | +1.11% | 20% |
| [ASHAPURMIN](https://in.tradingview.com/chart/?symbol=NSE:ASHAPURMIN)<br><sub>📶W9 · W↑4d · ↓CMF19d</sub> | ✓ SAFE | Bauxite mining processing distribution industrial minerals global | 📈 BULL_ANY_MID | 59 | 🔄61 | ↑1.007 | ↑1d | — | +1.5% | 6.56/6.06 | +1.51% | 20% |
| [DOLPHIN](https://in.tradingview.com/chart/?symbol=NSE:DOLPHIN)<br><sub>📶W9 · W↑4d · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 59 | ↑37 | ↑1.036 | ↑1d | SQ | +4.8% | -8.37/-14.84 | +4.83% | 20% |
| [SANOFI](https://in.tradingview.com/chart/?symbol=NSE:SANOFI)<br><sub>📶W9 · W↑34d · ↑CMF1d</sub> | ⚠ CAUTION | Diabetes insulin, cardiology drugs, CNS medications, Indian pharma | 📈 BULL_ANY_MID | 58 | ↑12 | ↓1.000 | ↑2d | SQ | +0.3% | 14.07/12.82 | -0.44% | 20% |
| [MARICO](https://in.tradingview.com/chart/?symbol=NSE:MARICO)<br><sub>📶W9 · W↑17d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↑69 | ↓1.010 | ↑3d | SQ | +2.0% | 39.15/35.61 | +0.08% | 20% |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>📶W9 · W↑9d · 🚀SS · ↑CMF11d · ÷DIV</sub> | ✓ SAFE | Offshore jack-up rigs drilling services oil gas sector | 📈 BULL_ANY_MID | 54 | 🔄66 | ↑1.024 | ↑1d | — | +3.7% | 5.63/3.81 | +3.69% | 20% |
| [AEROENTER](https://in.tradingview.com/chart/?symbol=NSE:AEROENTER)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Diversified industrial holding company trading manufacturing leasing financing | 📈 BULL_ANY_MID | 54 | 🔄89 | ↑1.020 | ↑1d | — | +6.1% | -15.86/-16.67 | +6.11% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>📶W9 · W↑65d · ↓CMF6d</sub> | ✓ SAFE | Pharma formulations acute chronic diseases consumer health | 📈 BULL_ANY_MID | 51 | ↑63 | ↑1.009 | ↑19d | SQ | +7.4% | 47.69/43.74 | +0.35% | 20% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>📶W9 · W↑21d · ↓CMF9d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄61 | ↑1.043 | ↑1d | — | +5.7% | 34.69/30.07 | +5.68% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑69d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 46 | 🔄80 | ↑1.020 | ↑9d | — | +6.3% | 40.54/39.46 | +2.18% | 20% |
| [THANGAMAYL](https://in.tradingview.com/chart/?symbol=NSE:THANGAMAYL)<br><sub>📶W9 · W↑39d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Gold ornaments silver diamond jewelry retail Tamil Nadu | 📈 BULL_ANY_MID | 40 | ↑99 | ↑1.058 | ↑42d | SQ | +80.6% | 50.68/45.71 | +6.10% | 10% 🟨 |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑17d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 28 | ↑66 | ↑1.011 | ↑2d | — | +2.0% | 14.61/10.66 | +0.67% | 20% |
| [MACPOWER](https://in.tradingview.com/chart/?symbol=NSE:MACPOWER)<br><sub>📶W9 · W↑24d · ↑CMF19d</sub> | ✓ SAFE | CNC turning centers and lathe machines for metal fabrication | 📈 BULL_ANY_MID | 27 | ↑88 | ↑1.012 | ↑3d | — | +3.9% | 21.74/21.43 | +0.92% | 20% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>📶W9 · W↑77d · ↑CMF30d</sub> | ✓ SAFE | Bulk liquid terminals, oil gas chemical logistics India | 📈 BULL_ANY_MID | 13 | ↑98 | ↑1.034 | ↑7d | — | +12.0% | 55.3/55.22 | +1.30% | 10% 🟨 |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · W↑73d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 12 | ↑87 | ↓1.008 | ↑8d | — | +3.1% | 48.18/47.9 | -0.10% | 20% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>📶W9 · W↑39d · ★ · ↑CMF2d</sub> | ✓ SAFE | CDMO formulations development manufacturing Indian pharma companies | 📈 BULL_ANY_MID | 0 | ↑89 | ↓1.021 | ↑38d | — | +32.6% | 59.7/59.7 | -0.06% | 20% |

```
NSE:PIDILITIND,NSE:SHRIRAMFIN,NSE:MAHLIFE,NSE:WSTCSTPAPR,NSE:CARERATING,NSE:SURYODAY,NSE:NUVAMA,NSE:IGPL,NSE:TANLA,NSE:ROUTE,NSE:UJJIVANSFB,NSE:ANDHRSUGAR,NSE:ASTRAMICRO,NSE:GPTHEALTH,NSE:TASTYBITE,NSE:INDIGO,NSE:ASHAPURMIN,NSE:DOLPHIN,NSE:SANOFI,NSE:MARICO,NSE:JINDRILL,NSE:AEROENTER,NSE:MANKIND,NSE:TVSMOTOR,NSE:ABCAPITAL,NSE:THANGAMAYL,NSE:NESTLEIND,NSE:MACPOWER,NSE:AEGISLOG,NSE:ADANIENT,NSE:AKUMS
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (47)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · W↑68d · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄61 | ↑1.012 | ↑1d | SQ·PV | +2.0% | 3.64/3.38 | +1.99% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑26d · 🚀SS · ↓CMF12d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 92 | 🔄79 | ↑1.024 | ↑3d | SQ·PV | +3.9% | 17.16/12.64 | +2.75% | 20% |
| [MAHLIFE](https://in.tradingview.com/chart/?symbol=NSE:MAHLIFE)<br><sub>📶W9 · W↑63d · RVOL19x · ↓CMF0d</sub> | ✓ SAFE | Residential and industrial real estate developer across India | ⚡ BULL_ANY_PPV | 68 | ↑60 | ↑1.012 | ↑2d | SQ·PV | +2.2% | 42.58/35.83 | +0.91% | 20% |
| [WSTCSTPAPR](https://in.tradingview.com/chart/?symbol=NSE:WSTCSTPAPR)<br><sub>📶W9 · W↑19d · ↑CMF1d</sub> | ✓ SAFE | Paper, paperboard, optical fiber producer for packaging and printing | ⚡ BULL_ANY_PPV | 58 | ↑75 | ↑1.048 | ↑2d | SQ·PV | +7.9% | 24.93/12.97 | +2.13% | 20% |
| [CARERATING](https://in.tradingview.com/chart/?symbol=NSE:CARERATING)<br><sub>📶W9 · W↑4d · ↑CMF0d</sub> | ⚠ CAUTION | Credit ratings for corporate debt and bonds | ⚡ BULL_ANY_PPV | 53 | ↑59 | ↑1.030 | ↑7d | SQ·PV | +4.4% | 24.99/15.72 | +3.27% | 20% |
| [SURYODAY](https://in.tradingview.com/chart/?symbol=NSE:SURYODAY)<br><sub>📶W9 · W↑77d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Microfinance bank serving unbanked rural populations credit | ⚡ BULL_ANY_PPV | 49 | 🔄86 | ↑1.046 | ↑1d | PV | +7.2% | 52.7/50.14 | +7.19% | 20% |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA)<br><sub>📶W9 · W↑77d · ↑CMF30d</sub> | ✓ SAFE | Wealth management, advisory, broking for high-net-worth individuals | ⚡ BULL_ANY_PPV | 22 | ↑89 | ↑1.029 | ↑3d | PV | +5.0% | 37.59/37.45 | +3.44% | 20% |
| [IGPL](https://in.tradingview.com/chart/?symbol=NSE:IGPL)<br><sub>📶W9 · ↓CMF13d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 18 | ↑58 | ↑1.036 | ↑2d | PV | +6.6% | -7.74/-20.44 | +3.09% | 20% |
| [TANLA](https://in.tradingview.com/chart/?symbol=NSE:TANLA)<br><sub>📶W9 · W↑77d · 🚀SS·41x · ↓CMF0d</sub> | ✓ SAFE | CPaaS provider SMS messaging enterprise customer communications | ⚡ BULL_ANY_PPV | 10 | ↑63 | ↑1.080 | ↑10d | PV | +18.6% | 66.86/62.84 | +10.13% | 20% |
| [ROUTE](https://in.tradingview.com/chart/?symbol=NSE:ROUTE)<br><sub>📶W9 · W↑89d · 🚀SS·89x · ↓CMF0d</sub> | ✓ SAFE | SMS and messaging platform for enterprises and telecom | ⚡ BULL_ANY_PPV | 9 | ↑34 | ↑1.053 | ↑11d | PV | +12.5% | 57.84/49.46 | +5.89% | 20% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>📶W9 · W↑29d · RVOL9x · ↑CMF28d</sub> | ✓ SAFE | Microfinance bank serving unbanked low-income borrowers | ⚡ BULL_ANY_PPV | 0 | ↑82 | ↑1.053 | ↑30d | PV | +29.1% | 61.95/61.94 | +5.73% | 20% |
| [ANDHRSUGAR](https://in.tradingview.com/chart/?symbol=NSE:ANDHRSUGAR)<br><sub>📶W9 · ↓CMF12d</sub> | ✓ SAFE | Sugar production and refining for domestic consumption | 📈 BULL_ANY_MID | 67 | ↑49 | ↑1.014 | ↑3d | SQ | +4.3% | -0.43/-3.34 | +1.53% | 20% |
| [ASTRAMICRO](https://in.tradingview.com/chart/?symbol=NSE:ASTRAMICRO)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | RF microwave modules defense space telecom systems | 📈 BULL_ANY_MID | 64 | ↑96 | ↑1.016 | ↑1d | SQ | +1.5% | 20.09/17.6 | +1.48% | 20% |
| [GPTHEALTH](https://in.tradingview.com/chart/?symbol=NSE:GPTHEALTH)<br><sub>📶W9 · W↑80d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 63 | ↑64 | ↑1.019 | ↑2d | SQ | +3.8% | 18.34/13.21 | +0.88% | 20% |
| [TASTYBITE](https://in.tradingview.com/chart/?symbol=NSE:TASTYBITE)<br><sub>📶W9 · W↑77d · ↓CMF30d</sub> | ✓ SAFE | Packaged ready-to-eat vegetarian meals for retail and institutional | 📈 BULL_ANY_MID | 62 | ↑71 | ↑1.027 | ↑3d | SQ | +4.5% | 49.82/47.1 | +2.56% | 20% |
| [INDIGO](https://in.tradingview.com/chart/?symbol=NSE:INDIGO)<br><sub>📶W9 · W↑45d · 🚀SS · ↑CMF29d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄49 | ↑1.008 | ↑1d | — | +1.1% | 20.36/20.19 | +1.11% | 20% |
| [ASHAPURMIN](https://in.tradingview.com/chart/?symbol=NSE:ASHAPURMIN)<br><sub>📶W9 · W↑4d · ↓CMF19d</sub> | ✓ SAFE | Bauxite mining processing distribution industrial minerals global | 📈 BULL_ANY_MID | 59 | 🔄61 | ↑1.007 | ↑1d | — | +1.5% | 6.56/6.06 | +1.51% | 20% |
| [DOLPHIN](https://in.tradingview.com/chart/?symbol=NSE:DOLPHIN)<br><sub>📶W9 · W↑4d · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 59 | ↑37 | ↑1.036 | ↑1d | SQ | +4.8% | -8.37/-14.84 | +4.83% | 20% |
| [SANOFI](https://in.tradingview.com/chart/?symbol=NSE:SANOFI)<br><sub>📶W9 · W↑34d · ↑CMF1d</sub> | ⚠ CAUTION | Diabetes insulin, cardiology drugs, CNS medications, Indian pharma | 📈 BULL_ANY_MID | 58 | ↑12 | ↓1.000 | ↑2d | SQ | +0.3% | 14.07/12.82 | -0.44% | 20% |
| [MARICO](https://in.tradingview.com/chart/?symbol=NSE:MARICO)<br><sub>📶W9 · W↑17d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↑69 | ↓1.010 | ↑3d | SQ | +2.0% | 39.15/35.61 | +0.08% | 20% |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>📶W9 · W↑9d · 🚀SS · ↑CMF11d · ÷DIV</sub> | ✓ SAFE | Offshore jack-up rigs drilling services oil gas sector | 📈 BULL_ANY_MID | 54 | 🔄66 | ↑1.024 | ↑1d | — | +3.7% | 5.63/3.81 | +3.69% | 20% |
| [AEROENTER](https://in.tradingview.com/chart/?symbol=NSE:AEROENTER)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Diversified industrial holding company trading manufacturing leasing financing | 📈 BULL_ANY_MID | 54 | 🔄89 | ↑1.020 | ↑1d | — | +6.1% | -15.86/-16.67 | +6.11% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>📶W9 · W↑65d · ↓CMF6d</sub> | ✓ SAFE | Pharma formulations acute chronic diseases consumer health | 📈 BULL_ANY_MID | 51 | ↑63 | ↑1.009 | ↑19d | SQ | +7.4% | 47.69/43.74 | +0.35% | 20% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>📶W9 · W↑21d · ↓CMF9d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄61 | ↑1.043 | ↑1d | — | +5.7% | 34.69/30.07 | +5.68% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑69d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 46 | 🔄80 | ↑1.020 | ↑9d | — | +6.3% | 40.54/39.46 | +2.18% | 20% |
| [THANGAMAYL](https://in.tradingview.com/chart/?symbol=NSE:THANGAMAYL)<br><sub>📶W9 · W↑39d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Gold ornaments silver diamond jewelry retail Tamil Nadu | 📈 BULL_ANY_MID | 40 | ↑99 | ↑1.058 | ↑42d | SQ | +80.6% | 50.68/45.71 | +6.10% | 10% 🟨 |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑17d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 28 | ↑66 | ↑1.011 | ↑2d | — | +2.0% | 14.61/10.66 | +0.67% | 20% |
| [MACPOWER](https://in.tradingview.com/chart/?symbol=NSE:MACPOWER)<br><sub>📶W9 · W↑24d · ↑CMF19d</sub> | ✓ SAFE | CNC turning centers and lathe machines for metal fabrication | 📈 BULL_ANY_MID | 27 | ↑88 | ↑1.012 | ↑3d | — | +3.9% | 21.74/21.43 | +0.92% | 20% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>📶W9 · W↑77d · ↑CMF30d</sub> | ✓ SAFE | Bulk liquid terminals, oil gas chemical logistics India | 📈 BULL_ANY_MID | 13 | ↑98 | ↑1.034 | ↑7d | — | +12.0% | 55.3/55.22 | +1.30% | 10% 🟨 |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · W↑73d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 12 | ↑87 | ↓1.008 | ↑8d | — | +3.1% | 48.18/47.9 | -0.10% | 20% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>📶W9 · W↑39d · ★ · ↑CMF2d</sub> | ✓ SAFE | CDMO formulations development manufacturing Indian pharma companies | 📈 BULL_ANY_MID | 0 | ↑89 | ↓1.021 | ↑38d | — | +32.6% | 59.7/59.7 | -0.06% | 20% |
| [ASIANTILES](https://in.tradingview.com/chart/?symbol=NSE:ASIANTILES)<br><sub>RVOL35x · ↑CMF0d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Ceramic tiles and sanitaryware for residential construction | 🔥 BULL_OS_PPV | 49 | 🔄4 | ↑1.085 | ↑1d | PV | +19.5% | -57.89/-63.85 | +19.48% | 20% |
| [ANDHRAPAP](https://in.tradingview.com/chart/?symbol=NSE:ANDHRAPAP)<br><sub>↓CMF14d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄21 | ↑1.012 | ↑1d | SQ·PV | +2.8% | -33.65/-38.12 | +2.83% | 20% |
| [NTPCGREEN](https://in.tradingview.com/chart/?symbol=NSE:NTPCGREEN)<br><sub>🚀SS·40x · ↑CMF0d · 🎯SLING</sub> | ✓ SAFE | Solar wind power generation utility green energy | ⚡ BULL_ANY_PPV | 49 | 🔄28 | ↑1.039 | ↑1d | PV | +6.5% | -41.54/-53.71 | +6.48% | 20% |
| [TIRUMALCHM](https://in.tradingview.com/chart/?symbol=NSE:TIRUMALCHM)<br><sub>↓CMF10d</sub> | ✓ SAFE | Phthalic anhydride, maleic anhydride, fine chemicals for coatings, plastics | ⚡ BULL_ANY_PPV | 29 | ↑3 | ↑1.008 | ↑1d | PV | +1.2% | -28.35/-32.46 | +1.20% | 20% |
| [SEAMECLTD](https://in.tradingview.com/chart/?symbol=NSE:SEAMECLTD)<br><sub>↓CMF1d · 🎯SLING</sub> | ✓ SAFE | Offshore drilling equipment rental and marine services | 🟡 BULL_OS_L2 | 80 | 🔄83 | ↑1.002 | ↓21d | SQ | -3.1% | -53.28/-53.58 | +2.29% | 20% |
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄40 | ↑1.012 | ↑1d | SQ | +2.4% | -40.58/-44.61 | +2.36% | 20% |
| [MUTHOOTFIN](https://in.tradingview.com/chart/?symbol=NSE:MUTHOOTFIN)<br><sub>🚀SS · ↓CMF3d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄27 | ↑1.015 | ↑1d | SQ | +3.3% | -27.02/-29.52 | +3.27% | 20% |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>🚀SS · ↓CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 68 | ↑67 | ↑1.010 | ↑2d | SQ | +1.9% | 4.33/1.26 | +0.83% | 20% |
| [WEALTH](https://in.tradingview.com/chart/?symbol=NSE:WEALTH)<br><sub>↓CMF2d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 60 | ↑41 | ↑1.002 | ↓10d | SQ | +0.1% | -24.03/-24.04 | +0.55% | 20% |
| [JAINREC](https://in.tradingview.com/chart/?symbol=NSE:JAINREC)<br><sub>↓CMF3d</sub> | ✓ SAFE | Non-ferrous metal recycling, lead copper aluminium alloys | 📈 BULL_ANY_MID | 58 | ↑50 | ↑0.997 | ↓7d | SQ | +2.1% | -44.16/-46.88 | +0.09% | 20% 🟦 |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>🚀SS · ↑CMF4d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄93 | ↑1.031 | ↑1d | — | +4.5% | -28.4/-34.25 | +4.45% | 20% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>↓CMF9d</sub> | ✓ SAFE | Stainless steel corrugated hoses assemblies fittings fluid systems | 📈 BULL_ANY_MID | 43 | 🔄98 | ↑1.008 | ↓17d | — | -10.6% | -30.46/-31.98 | +3.19% | 10% 🟨 |
| [ENRIN](https://in.tradingview.com/chart/?symbol=NSE:ENRIN)<br><sub>🚀SS · ↓CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 40 | 🔄72 | ↑1.009 | ↓21d | — | -1.4% | -25.75/-26.7 | +3.26% | 20% |
| [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT)<br><sub>↑CMF7d</sub> | ✓ SAFE | BPM services for customer support and back-office operations globally | 📈 BULL_ANY_MID | 33 | 🔄58 | ↓0.989 | ↓17d | — | -5.4% | -47.24/-48.18 | -0.31% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>🚀SS · ↓CMF19d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 24 | ↑87 | ↑1.005 | ↓6d | — | +2.3% | -31.17/-34.4 | +0.16% | 20% |
| [NETWEB](https://in.tradingview.com/chart/?symbol=NSE:NETWEB)<br><sub>↓CMF17d · ⚠️TRAP</sub> | ✓ SAFE | High-performance computing systems manufacturer for AI and research | 📈 BULL_ANY_MID | 0 | ↑87 | ↓0.988 | ↓30d | — | +1.2% | -29.72/-30.3 | -1.05% | 20% |

```
NSE:PIDILITIND,NSE:SHRIRAMFIN,NSE:MAHLIFE,NSE:WSTCSTPAPR,NSE:CARERATING,NSE:SURYODAY,NSE:NUVAMA,NSE:IGPL,NSE:TANLA,NSE:ROUTE,NSE:UJJIVANSFB,NSE:ANDHRSUGAR,NSE:ASTRAMICRO,NSE:GPTHEALTH,NSE:TASTYBITE,NSE:INDIGO,NSE:ASHAPURMIN,NSE:DOLPHIN,NSE:SANOFI,NSE:MARICO,NSE:JINDRILL,NSE:AEROENTER,NSE:MANKIND,NSE:TVSMOTOR,NSE:ABCAPITAL,NSE:THANGAMAYL,NSE:NESTLEIND,NSE:MACPOWER,NSE:AEGISLOG,NSE:ADANIENT,NSE:AKUMS,NSE:ASIANTILES,NSE:ANDHRAPAP,NSE:NTPCGREEN,NSE:TIRUMALCHM,NSE:SEAMECLTD,NSE:HINDZINC,NSE:MUTHOOTFIN,NSE:GRASIM,NSE:WEALTH,NSE:JAINREC,NSE:POWERINDIA,NSE:AEROFLEX,NSE:ENRIN,NSE:ONEPOINT,NSE:ADANIPOWER,NSE:NETWEB
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (24)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>📶W9 · W↑68d · 🚀SS · ↓CMF16d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄61 | ↑1.012 | ↑1d | SQ·PV | +2.0% | 3.64/3.38 | +1.99% | 20% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>📶W9 · W↑26d · 🚀SS · ↓CMF12d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 92 | 🔄79 | ↑1.024 | ↑3d | SQ·PV | +3.9% | 17.16/12.64 | +2.75% | 20% |
| [MAHLIFE](https://in.tradingview.com/chart/?symbol=NSE:MAHLIFE)<br><sub>📶W9 · W↑63d · RVOL19x · ↓CMF0d</sub> | ✓ SAFE | Residential and industrial real estate developer across India | ⚡ BULL_ANY_PPV | 68 | ↑60 | ↑1.012 | ↑2d | SQ·PV | +2.2% | 42.58/35.83 | +0.91% | 20% |
| [WSTCSTPAPR](https://in.tradingview.com/chart/?symbol=NSE:WSTCSTPAPR)<br><sub>📶W9 · W↑19d · ↑CMF1d</sub> | ✓ SAFE | Paper, paperboard, optical fiber producer for packaging and printing | ⚡ BULL_ANY_PPV | 58 | ↑75 | ↑1.048 | ↑2d | SQ·PV | +7.9% | 24.93/12.97 | +2.13% | 20% |
| [CARERATING](https://in.tradingview.com/chart/?symbol=NSE:CARERATING)<br><sub>📶W9 · W↑4d · ↑CMF0d</sub> | ⚠ CAUTION | Credit ratings for corporate debt and bonds | ⚡ BULL_ANY_PPV | 53 | ↑59 | ↑1.030 | ↑7d | SQ·PV | +4.4% | 24.99/15.72 | +3.27% | 20% |
| [ANDHRSUGAR](https://in.tradingview.com/chart/?symbol=NSE:ANDHRSUGAR)<br><sub>📶W9 · ↓CMF12d</sub> | ✓ SAFE | Sugar production and refining for domestic consumption | 📈 BULL_ANY_MID | 67 | ↑49 | ↑1.014 | ↑3d | SQ | +4.3% | -0.43/-3.34 | +1.53% | 20% |
| [ASTRAMICRO](https://in.tradingview.com/chart/?symbol=NSE:ASTRAMICRO)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | RF microwave modules defense space telecom systems | 📈 BULL_ANY_MID | 64 | ↑96 | ↑1.016 | ↑1d | SQ | +1.5% | 20.09/17.6 | +1.48% | 20% |
| [GPTHEALTH](https://in.tradingview.com/chart/?symbol=NSE:GPTHEALTH)<br><sub>📶W9 · W↑80d · 🚀SS · ↑CMF15d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 63 | ↑64 | ↑1.019 | ↑2d | SQ | +3.8% | 18.34/13.21 | +0.88% | 20% |
| [TASTYBITE](https://in.tradingview.com/chart/?symbol=NSE:TASTYBITE)<br><sub>📶W9 · W↑77d · ↓CMF30d</sub> | ✓ SAFE | Packaged ready-to-eat vegetarian meals for retail and institutional | 📈 BULL_ANY_MID | 62 | ↑71 | ↑1.027 | ↑3d | SQ | +4.5% | 49.82/47.1 | +2.56% | 20% |
| [DOLPHIN](https://in.tradingview.com/chart/?symbol=NSE:DOLPHIN)<br><sub>📶W9 · W↑4d · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 59 | ↑37 | ↑1.036 | ↑1d | SQ | +4.8% | -8.37/-14.84 | +4.83% | 20% |
| [SANOFI](https://in.tradingview.com/chart/?symbol=NSE:SANOFI)<br><sub>📶W9 · W↑34d · ↑CMF1d</sub> | ⚠ CAUTION | Diabetes insulin, cardiology drugs, CNS medications, Indian pharma | 📈 BULL_ANY_MID | 58 | ↑12 | ↓1.000 | ↑2d | SQ | +0.3% | 14.07/12.82 | -0.44% | 20% |
| [MARICO](https://in.tradingview.com/chart/?symbol=NSE:MARICO)<br><sub>📶W9 · W↑17d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↑69 | ↓1.010 | ↑3d | SQ | +2.0% | 39.15/35.61 | +0.08% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>📶W9 · W↑65d · ↓CMF6d</sub> | ✓ SAFE | Pharma formulations acute chronic diseases consumer health | 📈 BULL_ANY_MID | 51 | ↑63 | ↑1.009 | ↑19d | SQ | +7.4% | 47.69/43.74 | +0.35% | 20% |
| [THANGAMAYL](https://in.tradingview.com/chart/?symbol=NSE:THANGAMAYL)<br><sub>📶W9 · W↑39d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Gold ornaments silver diamond jewelry retail Tamil Nadu | 📈 BULL_ANY_MID | 40 | ↑99 | ↑1.058 | ↑42d | SQ | +80.6% | 50.68/45.71 | +6.10% | 10% 🟨 |
| [ANDHRAPAP](https://in.tradingview.com/chart/?symbol=NSE:ANDHRAPAP)<br><sub>↓CMF14d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄21 | ↑1.012 | ↑1d | SQ·PV | +2.8% | -33.65/-38.12 | +2.83% | 20% |
| [SEAMECLTD](https://in.tradingview.com/chart/?symbol=NSE:SEAMECLTD)<br><sub>↓CMF1d · 🎯SLING</sub> | ✓ SAFE | Offshore drilling equipment rental and marine services | 🟡 BULL_OS_L2 | 80 | 🔄83 | ↑1.002 | ↓21d | SQ | -3.1% | -53.28/-53.58 | +2.29% | 20% |
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄40 | ↑1.012 | ↑1d | SQ | +2.4% | -40.58/-44.61 | +2.36% | 20% |
| [MUTHOOTFIN](https://in.tradingview.com/chart/?symbol=NSE:MUTHOOTFIN)<br><sub>🚀SS · ↓CMF3d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄27 | ↑1.015 | ↑1d | SQ | +3.3% | -27.02/-29.52 | +3.27% | 20% |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>🚀SS · ↓CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 68 | ↑67 | ↑1.010 | ↑2d | SQ | +1.9% | 4.33/1.26 | +0.83% | 20% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>W↑68d · ↓CMF12d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 68 | ↓51 | ↑1.005 | ↑2d | SQ | +1.3% | 0.89/-3.8 | +0.23% | 20% |
| [WEALTH](https://in.tradingview.com/chart/?symbol=NSE:WEALTH)<br><sub>↓CMF2d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 60 | ↑41 | ↑1.002 | ↓10d | SQ | +0.1% | -24.03/-24.04 | +0.55% | 20% |
| [JAINREC](https://in.tradingview.com/chart/?symbol=NSE:JAINREC)<br><sub>↓CMF3d</sub> | ✓ SAFE | Non-ferrous metal recycling, lead copper aluminium alloys | 📈 BULL_ANY_MID | 58 | ↑50 | ↑0.997 | ↓7d | SQ | +2.1% | -44.16/-46.88 | +0.09% | 20% 🟦 |
| [ASIANHOTNR](https://in.tradingview.com/chart/?symbol=NSE:ASIANHOTNR)<br><sub>W↑19d · ↓CMF7d · DEL78%(T-1) · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | ↓28 | ↓0.963 | ↓2d | SQ | -1.2% | -17.35/-20.98 | -5.70% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>↓CMF20d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 57 | ↓44 | ↑1.000 | ↓8d | SQ | -0.3% | -49.16/-51.32 | +0.48% | 20% |

```
NSE:PIDILITIND,NSE:SHRIRAMFIN,NSE:MAHLIFE,NSE:WSTCSTPAPR,NSE:CARERATING,NSE:ANDHRSUGAR,NSE:ASTRAMICRO,NSE:GPTHEALTH,NSE:TASTYBITE,NSE:DOLPHIN,NSE:SANOFI,NSE:MARICO,NSE:MANKIND,NSE:THANGAMAYL,NSE:ANDHRAPAP,NSE:SEAMECLTD,NSE:HINDZINC,NSE:MUTHOOTFIN,NSE:GRASIM,NSE:GAIL,NSE:WEALTH,NSE:JAINREC,NSE:ASIANHOTNR,NSE:TATASTEEL
```

---

### 🔥 MAJOR — PPV confirmed (9)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SURYODAY](https://in.tradingview.com/chart/?symbol=NSE:SURYODAY)<br><sub>📶W9 · W↑77d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Microfinance bank serving unbanked rural populations credit | ⚡ BULL_ANY_PPV | 49 | 🔄86 | ↑1.046 | ↑1d | PV | +7.2% | 52.7/50.14 | +7.19% | 20% |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA)<br><sub>📶W9 · W↑77d · ↑CMF30d</sub> | ✓ SAFE | Wealth management, advisory, broking for high-net-worth individuals | ⚡ BULL_ANY_PPV | 22 | ↑89 | ↑1.029 | ↑3d | PV | +5.0% | 37.59/37.45 | +3.44% | 20% |
| [IGPL](https://in.tradingview.com/chart/?symbol=NSE:IGPL)<br><sub>📶W9 · ↓CMF13d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 18 | ↑58 | ↑1.036 | ↑2d | PV | +6.6% | -7.74/-20.44 | +3.09% | 20% |
| [TANLA](https://in.tradingview.com/chart/?symbol=NSE:TANLA)<br><sub>📶W9 · W↑77d · 🚀SS·41x · ↓CMF0d</sub> | ✓ SAFE | CPaaS provider SMS messaging enterprise customer communications | ⚡ BULL_ANY_PPV | 10 | ↑63 | ↑1.080 | ↑10d | PV | +18.6% | 66.86/62.84 | +10.13% | 20% |
| [ROUTE](https://in.tradingview.com/chart/?symbol=NSE:ROUTE)<br><sub>📶W9 · W↑89d · 🚀SS·89x · ↓CMF0d</sub> | ✓ SAFE | SMS and messaging platform for enterprises and telecom | ⚡ BULL_ANY_PPV | 9 | ↑34 | ↑1.053 | ↑11d | PV | +12.5% | 57.84/49.46 | +5.89% | 20% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>📶W9 · W↑29d · RVOL9x · ↑CMF28d</sub> | ✓ SAFE | Microfinance bank serving unbanked low-income borrowers | ⚡ BULL_ANY_PPV | 0 | ↑82 | ↑1.053 | ↑30d | PV | +29.1% | 61.95/61.94 | +5.73% | 20% |
| [ASIANTILES](https://in.tradingview.com/chart/?symbol=NSE:ASIANTILES)<br><sub>RVOL35x · ↑CMF0d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Ceramic tiles and sanitaryware for residential construction | 🔥 BULL_OS_PPV | 49 | 🔄4 | ↑1.085 | ↑1d | PV | +19.5% | -57.89/-63.85 | +19.48% | 20% |
| [NTPCGREEN](https://in.tradingview.com/chart/?symbol=NSE:NTPCGREEN)<br><sub>🚀SS·40x · ↑CMF0d · 🎯SLING</sub> | ✓ SAFE | Solar wind power generation utility green energy | ⚡ BULL_ANY_PPV | 49 | 🔄28 | ↑1.039 | ↑1d | PV | +6.5% | -41.54/-53.71 | +6.48% | 20% |
| [TIRUMALCHM](https://in.tradingview.com/chart/?symbol=NSE:TIRUMALCHM)<br><sub>↓CMF10d</sub> | ✓ SAFE | Phthalic anhydride, maleic anhydride, fine chemicals for coatings, plastics | ⚡ BULL_ANY_PPV | 29 | ↑3 | ↑1.008 | ↑1d | PV | +1.2% | -28.35/-32.46 | +1.20% | 20% |

```
NSE:SURYODAY,NSE:NUVAMA,NSE:IGPL,NSE:TANLA,NSE:ROUTE,NSE:UJJIVANSFB,NSE:ASIANTILES,NSE:NTPCGREEN,NSE:TIRUMALCHM
```

### 🟢 OVERSOLD — reversal from −53/−60 (4)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SANDUMA](https://in.tradingview.com/chart/?symbol=NSE:SANDUMA)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Manganese iron ore mining ferroalloys steel production | 🟢 BULL_OVERSOLD | 11 | ↓39 | ↑0.983 | ↓14d | — | -7.2% | -60.9/-61.26 | -0.22% | 20% |
| [CRIZAC](https://in.tradingview.com/chart/?symbol=NSE:CRIZAC)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | EdTech international student recruitment platform for universities | 🟢 BULL_OVERSOLD | 5 | ↓5 | ↑0.983 | ↓29d | — | -9.3% | -62.21/-62.5 | +0.73% | 20% |
| [NTPC](https://in.tradingview.com/chart/?symbol=NSE:NTPC)<br><sub>↓CMF4d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 29 | ↓35 | ↑1.003 | ↑1d | — | +0.5% | -51.44/-55.81 | +0.45% | 20% |
| [SKFINDIA](https://in.tradingview.com/chart/?symbol=NSE:SKFINDIA)<br><sub>↓CMF28d · ⚠️TRAP</sub> | ⚠ CAUTION | Bearings seals lubrication automotive industrial machinery | 🟡 BULL_OS_L2 | 0 | ↓5 | ↓0.974 | ↓29d | — | -7.5% | -55.81/-55.97 | -1.97% | 20% |

```
NSE:SANDUMA,NSE:CRIZAC,NSE:NTPC,NSE:SKFINDIA
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (19)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [INDIGO](https://in.tradingview.com/chart/?symbol=NSE:INDIGO)<br><sub>📶W9 · W↑45d · 🚀SS · ↑CMF29d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄49 | ↑1.008 | ↑1d | — | +1.1% | 20.36/20.19 | +1.11% | 20% |
| [ASHAPURMIN](https://in.tradingview.com/chart/?symbol=NSE:ASHAPURMIN)<br><sub>📶W9 · W↑4d · ↓CMF19d</sub> | ✓ SAFE | Bauxite mining processing distribution industrial minerals global | 📈 BULL_ANY_MID | 59 | 🔄61 | ↑1.007 | ↑1d | — | +1.5% | 6.56/6.06 | +1.51% | 20% |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>📶W9 · W↑9d · 🚀SS · ↑CMF11d · ÷DIV</sub> | ✓ SAFE | Offshore jack-up rigs drilling services oil gas sector | 📈 BULL_ANY_MID | 54 | 🔄66 | ↑1.024 | ↑1d | — | +3.7% | 5.63/3.81 | +3.69% | 20% |
| [AEROENTER](https://in.tradingview.com/chart/?symbol=NSE:AEROENTER)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Diversified industrial holding company trading manufacturing leasing financing | 📈 BULL_ANY_MID | 54 | 🔄89 | ↑1.020 | ↑1d | — | +6.1% | -15.86/-16.67 | +6.11% | 20% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>📶W9 · W↑21d · ↓CMF9d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄61 | ↑1.043 | ↑1d | — | +5.7% | 34.69/30.07 | +5.68% | 20% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>📶W9 · W↑69d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | NBFC financing insurance brokerage retail corporate customers | 📈 BULL_ANY_MID | 46 | 🔄80 | ↑1.020 | ↑9d | — | +6.3% | 40.54/39.46 | +2.18% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑17d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 28 | ↑66 | ↑1.011 | ↑2d | — | +2.0% | 14.61/10.66 | +0.67% | 20% |
| [MACPOWER](https://in.tradingview.com/chart/?symbol=NSE:MACPOWER)<br><sub>📶W9 · W↑24d · ↑CMF19d</sub> | ✓ SAFE | CNC turning centers and lathe machines for metal fabrication | 📈 BULL_ANY_MID | 27 | ↑88 | ↑1.012 | ↑3d | — | +3.9% | 21.74/21.43 | +0.92% | 20% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>📶W9 · W↑77d · ↑CMF30d</sub> | ✓ SAFE | Bulk liquid terminals, oil gas chemical logistics India | 📈 BULL_ANY_MID | 13 | ↑98 | ↑1.034 | ↑7d | — | +12.0% | 55.3/55.22 | +1.30% | 10% 🟨 |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · W↑73d · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 12 | ↑87 | ↓1.008 | ↑8d | — | +3.1% | 48.18/47.9 | -0.10% | 20% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>📶W9 · W↑39d · ★ · ↑CMF2d</sub> | ✓ SAFE | CDMO formulations development manufacturing Indian pharma companies | 📈 BULL_ANY_MID | 0 | ↑89 | ↓1.021 | ↑38d | — | +32.6% | 59.7/59.7 | -0.06% | 20% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>🚀SS · ↑CMF4d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 49 | 🔄93 | ↑1.031 | ↑1d | — | +4.5% | -28.4/-34.25 | +4.45% | 20% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>↓CMF9d</sub> | ✓ SAFE | Stainless steel corrugated hoses assemblies fittings fluid systems | 📈 BULL_ANY_MID | 43 | 🔄98 | ↑1.008 | ↓17d | — | -10.6% | -30.46/-31.98 | +3.19% | 10% 🟨 |
| [ENRIN](https://in.tradingview.com/chart/?symbol=NSE:ENRIN)<br><sub>🚀SS · ↓CMF2d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 40 | 🔄72 | ↑1.009 | ↓21d | — | -1.4% | -25.75/-26.7 | +3.26% | 20% |
| [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT)<br><sub>↑CMF7d</sub> | ✓ SAFE | BPM services for customer support and back-office operations globally | 📈 BULL_ANY_MID | 33 | 🔄58 | ↓0.989 | ↓17d | — | -5.4% | -47.24/-48.18 | -0.31% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>🚀SS · ↓CMF19d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 24 | ↑87 | ↑1.005 | ↓6d | — | +2.3% | -31.17/-34.4 | +0.16% | 20% |
| [GOLDIAM](https://in.tradingview.com/chart/?symbol=NSE:GOLDIAM)<br><sub>↑CMF29d</sub> | ✓ SAFE | Diamond gold silver jewelry manufacturer export markets | 📈 BULL_ANY_MID | 10 | ↓43 | ↑0.958 | ↓15d | — | -22.9% | -48.7/-49.76 | +1.51% | 20% |
| [NETWEB](https://in.tradingview.com/chart/?symbol=NSE:NETWEB)<br><sub>↓CMF17d · ⚠️TRAP</sub> | ✓ SAFE | High-performance computing systems manufacturer for AI and research | 📈 BULL_ANY_MID | 0 | ↑87 | ↓0.988 | ↓30d | — | +1.2% | -29.72/-30.3 | -1.05% | 20% |
| [PRECWIRE](https://in.tradingview.com/chart/?symbol=NSE:PRECWIRE)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Enamelled copper wires motors transformers automotive appliances | 📈 BULL_ANY_MID | 0 | ↓90 | ↓0.985 | ↓24d | — | -9.9% | -48.71/-50.76 | -1.17% | 20% |

```
NSE:INDIGO,NSE:ASHAPURMIN,NSE:JINDRILL,NSE:AEROENTER,NSE:TVSMOTOR,NSE:ABCAPITAL,NSE:NESTLEIND,NSE:MACPOWER,NSE:AEGISLOG,NSE:ADANIENT,NSE:AKUMS,NSE:POWERINDIA,NSE:AEROFLEX,NSE:ENRIN,NSE:ONEPOINT,NSE:ADANIPOWER,NSE:GOLDIAM,NSE:NETWEB,NSE:PRECWIRE
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
