> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-10-08
*Generated 2026-10-08 15:44 IST*

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

**Total bull crosses today: 40** · 12 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:KOTIC,NSE:BHEL,NSE:LICHSGFIN,NSE:VEDL,NSE:SIGMAADV,NSE:EXCELINDUS,NSE:SRF,NSE:COALINDIA,NSE:POLYCAB,NSE:SHYAMMETL,NSE:ELLEN,NSE:TCPLPACK,NSE:ADANIPOWER,NSE:STYLEBAAZA,NSE:UEL,NSE:CANHLIFE,NSE:DLF,NSE:CGPOWER,NSE:PAYTM,NSE:ETERNAL,NSE:HDFCLIFE,NSE:VBL,NSE:GVT&D,NSE:HINDOILEXP,NSE:ZOTA,NSE:IFCI,NSE:INDIAMART,NSE:TMPV,NSE:INDIANB,NSE:METROBRAND,NSE:WIPRO,NSE:CHOLAFIN,NSE:REPCOHOME,NSE:ABB,NSE:JIOFIN,NSE:TATACAP,NSE:DECNGOLD,NSE:GOODLUCK,NSE:PRECAM,NSE:NIACL
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (25)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [KOTIC](https://in.tradingview.com/chart/?symbol=NSE:KOTIC)<br><sub>📶W9 · RVOL11x · ↓CMF30d · ÷DIV</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 89 | 🔄50 | ↑1.038 | ↑1d | SQ·PV | +6.8% | 18.92/14.02 | +6.83% | 20% 🟦 |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 64 | ↑88 | ↑1.016 | ↑1d | SQ·PV | +1.6% | -7.84/-16.13 | +1.64% | 20% |
| [LICHSGFIN](https://in.tradingview.com/chart/?symbol=NSE:LICHSGFIN)<br><sub>📶W9 · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Residential mortgage loans for home purchase and construction | ⚡ BULL_ANY_PPV | 54 | 🔄54 | ↑1.019 | ↑1d | PV | +4.2% | -21.25/-21.7 | +4.19% | 20% |
| [VEDL](https://in.tradingview.com/chart/?symbol=NSE:VEDL)<br><sub>📶W9 · 🚀SS · ↑CMF19d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 54 | 🔄3 | ↑1.022 | ↑1d | PV | +4.1% | -36.44/-42.32 | +4.14% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [EXCELINDUS](https://in.tradingview.com/chart/?symbol=NSE:EXCELINDUS)<br><sub>📶W9 · ↓CMF16d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 70 | 🔄50 | ↓0.989 | ↓37d | SQ | -6.8% | -54.83/-55.69 | -0.56% | 20% |
| [SRF](https://in.tradingview.com/chart/?symbol=NSE:SRF)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Technical textiles, films, chemicals for automotive, industrial, packaging | 📈 BULL_ANY_MID | 86 | 🔄37 | ↑1.002 | ↓14d | SQ | -1.1% | -41.0/-43.83 | +1.02% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 69 | ↑54 | ↑1.007 | ↑1d | SQ | +1.4% | 24.57/23.53 | +1.38% | 20% |
| [POLYCAB](https://in.tradingview.com/chart/?symbol=NSE:POLYCAB)<br><sub>📶W9 · ↑CMF0d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄54 | ↑1.013 | ↑1d | — | +2.0% | -44.27/-49.73 | +1.99% | 20% |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL)<br><sub>📶W9 · ↓CMF9d</sub> | ✓ SAFE | Steel long products, ferro alloys, pellets, power generation | 📈 BULL_ANY_MID | 58 | ↑74 | ↓1.005 | ↓2d | SQ | +1.2% | -13.16/-15.53 | -0.05% | 20% |
| [ELLEN](https://in.tradingview.com/chart/?symbol=NSE:ELLEN)<br><sub>📶W9 · ↓CMF6d</sub> | ✓ SAFE | Industrial oxygen nitrogen gases bulk packaged eastern southern India | 📈 BULL_ANY_MID | 58 | ↑74 | ↓0.992 | ↓2d | SQ | +0.6% | -0.94/-2.23 | -4.20% | 20% |
| [TCPLPACK](https://in.tradingview.com/chart/?symbol=NSE:TCPLPACK)<br><sub>📶W9 · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 57 | ↑85 | ↓1.001 | ↑3d | SQ | +1.6% | 27.23/22.92 | -0.92% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 52 | 🔄70 | ↑1.000 | ↓3d | — | +2.5% | -41.74/-41.75 | +2.49% | 20% |
| [STYLEBAAZA](https://in.tradingview.com/chart/?symbol=NSE:STYLEBAAZA)<br><sub>📶W9 · ↑CMF2d · ÷DIV</sub> | ✓ SAFE | Value fashion apparel retailer eastern India families | 📈 BULL_ANY_MID | 51 | ↑82 | ↓0.989 | ↓9d | SQ | -0.9% | -23.44/-25.66 | -1.99% | 5% |
| [UEL](https://in.tradingview.com/chart/?symbol=NSE:UEL)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Solar power generation, EV manufacturing, renewable energy sector | 📈 BULL_ANY_MID | 49 | 🔄50 | ↑1.050 | ↑1d | — | +10.0% | -38.4/-43.61 | +10.00% | 20% 🟦 |
| [CANHLIFE](https://in.tradingview.com/chart/?symbol=NSE:CANHLIFE)<br><sub>📶W9 · ↑CMF19d</sub> | ⚠ CAUTION | Life insurance through bank distribution channels | 📈 BULL_ANY_MID | 43 | ↑50 | ↓0.995 | ↓17d | SQ | -4.1% | -51.58/-52.72 | -0.34% | 20% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 29 | ↑57 | ↑1.011 | ↑1d | — | +2.1% | 7.14/4.78 | +2.10% | 20% |
| [CGPOWER](https://in.tradingview.com/chart/?symbol=NSE:CGPOWER)<br><sub>📶W9 · 🚀SS · ↓CMF5d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 29 | ↑69 | ↑1.005 | ↑1d | — | +0.4% | -12.74/-14.29 | +0.38% | 20% |
| [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Digital payments, fintech, consumer and merchant ecosystem | 📈 BULL_ANY_MID | 24 | ↑87 | ↑1.016 | ↑1d | — | +2.3% | 2.77/0.98 | +2.30% | 20% |
| [ETERNAL](https://in.tradingview.com/chart/?symbol=NSE:ETERNAL)<br><sub>📶W9 · ↑CMF2d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 18 | ↑69 | ↓1.004 | ↑2d | — | +2.2% | -0.89/-2.27 | -0.36% | 20% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>📶W9 · W↑14d · ↑CMF6d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 18 | ↑22 | ↑1.000 | ↓12d | — | +0.8% | -18.3/-18.75 | +0.02% | 20% |
| [VBL](https://in.tradingview.com/chart/?symbol=NSE:VBL)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF6d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 13 | ↑42 | ↑1.022 | ↑12d | — | +7.0% | 24.78/23.0 | +3.29% | 20% |
| [GVT&D](https://in.tradingview.com/chart/?symbol=NSE:GVT&D)<br><sub>📶W9 · ↓CMF3d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 12 | ↑70 | ↓0.994 | ↓8d | — | -2.5% | -29.77/-29.83 | -0.32% | -% |
| [HINDOILEXP](https://in.tradingview.com/chart/?symbol=NSE:HINDOILEXP)<br><sub>📶W9 · ↓CMF5d</sub> | ✓ SAFE | Oil gas exploration production onshore offshore India | 📈 BULL_ANY_MID | 3 | ↑66 | ↓0.995 | ↓17d | — | -3.6% | -28.31/-30.76 | -1.44% | 20% |
| [ZOTA](https://in.tradingview.com/chart/?symbol=NSE:ZOTA)<br><sub>📶W9 · W↑14d · ↑CMF1d</sub> | ✓ SAFE | Pharma manufacturer: tablets, syrups, Ayurveda, OTC products | 📈 BULL_ANY_MID | 2 | ↑45 | ↓1.020 | ↑18d | — | +21.6% | 40.56/37.73 | -1.47% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:KOTIC,NSE:BHEL,NSE:LICHSGFIN,NSE:VEDL,NSE:SIGMAADV,NSE:EXCELINDUS,NSE:SRF,NSE:COALINDIA,NSE:POLYCAB,NSE:SHYAMMETL,NSE:ELLEN,NSE:TCPLPACK,NSE:ADANIPOWER,NSE:STYLEBAAZA,NSE:UEL,NSE:CANHLIFE,NSE:DLF,NSE:CGPOWER,NSE:PAYTM,NSE:ETERNAL,NSE:HDFCLIFE,NSE:VBL,NSE:GVT&D,NSE:HINDOILEXP,NSE:ZOTA
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (34)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [KOTIC](https://in.tradingview.com/chart/?symbol=NSE:KOTIC)<br><sub>📶W9 · RVOL11x · ↓CMF30d · ÷DIV</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 89 | 🔄50 | ↑1.038 | ↑1d | SQ·PV | +6.8% | 18.92/14.02 | +6.83% | 20% 🟦 |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 64 | ↑88 | ↑1.016 | ↑1d | SQ·PV | +1.6% | -7.84/-16.13 | +1.64% | 20% |
| [LICHSGFIN](https://in.tradingview.com/chart/?symbol=NSE:LICHSGFIN)<br><sub>📶W9 · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Residential mortgage loans for home purchase and construction | ⚡ BULL_ANY_PPV | 54 | 🔄54 | ↑1.019 | ↑1d | PV | +4.2% | -21.25/-21.7 | +4.19% | 20% |
| [VEDL](https://in.tradingview.com/chart/?symbol=NSE:VEDL)<br><sub>📶W9 · 🚀SS · ↑CMF19d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 54 | 🔄3 | ↑1.022 | ↑1d | PV | +4.1% | -36.44/-42.32 | +4.14% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [EXCELINDUS](https://in.tradingview.com/chart/?symbol=NSE:EXCELINDUS)<br><sub>📶W9 · ↓CMF16d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 70 | 🔄50 | ↓0.989 | ↓37d | SQ | -6.8% | -54.83/-55.69 | -0.56% | 20% |
| [SRF](https://in.tradingview.com/chart/?symbol=NSE:SRF)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Technical textiles, films, chemicals for automotive, industrial, packaging | 📈 BULL_ANY_MID | 86 | 🔄37 | ↑1.002 | ↓14d | SQ | -1.1% | -41.0/-43.83 | +1.02% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 69 | ↑54 | ↑1.007 | ↑1d | SQ | +1.4% | 24.57/23.53 | +1.38% | 20% |
| [POLYCAB](https://in.tradingview.com/chart/?symbol=NSE:POLYCAB)<br><sub>📶W9 · ↑CMF0d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄54 | ↑1.013 | ↑1d | — | +2.0% | -44.27/-49.73 | +1.99% | 20% |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL)<br><sub>📶W9 · ↓CMF9d</sub> | ✓ SAFE | Steel long products, ferro alloys, pellets, power generation | 📈 BULL_ANY_MID | 58 | ↑74 | ↓1.005 | ↓2d | SQ | +1.2% | -13.16/-15.53 | -0.05% | 20% |
| [ELLEN](https://in.tradingview.com/chart/?symbol=NSE:ELLEN)<br><sub>📶W9 · ↓CMF6d</sub> | ✓ SAFE | Industrial oxygen nitrogen gases bulk packaged eastern southern India | 📈 BULL_ANY_MID | 58 | ↑74 | ↓0.992 | ↓2d | SQ | +0.6% | -0.94/-2.23 | -4.20% | 20% |
| [TCPLPACK](https://in.tradingview.com/chart/?symbol=NSE:TCPLPACK)<br><sub>📶W9 · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 57 | ↑85 | ↓1.001 | ↑3d | SQ | +1.6% | 27.23/22.92 | -0.92% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 52 | 🔄70 | ↑1.000 | ↓3d | — | +2.5% | -41.74/-41.75 | +2.49% | 20% |
| [STYLEBAAZA](https://in.tradingview.com/chart/?symbol=NSE:STYLEBAAZA)<br><sub>📶W9 · ↑CMF2d · ÷DIV</sub> | ✓ SAFE | Value fashion apparel retailer eastern India families | 📈 BULL_ANY_MID | 51 | ↑82 | ↓0.989 | ↓9d | SQ | -0.9% | -23.44/-25.66 | -1.99% | 5% |
| [UEL](https://in.tradingview.com/chart/?symbol=NSE:UEL)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Solar power generation, EV manufacturing, renewable energy sector | 📈 BULL_ANY_MID | 49 | 🔄50 | ↑1.050 | ↑1d | — | +10.0% | -38.4/-43.61 | +10.00% | 20% 🟦 |
| [CANHLIFE](https://in.tradingview.com/chart/?symbol=NSE:CANHLIFE)<br><sub>📶W9 · ↑CMF19d</sub> | ⚠ CAUTION | Life insurance through bank distribution channels | 📈 BULL_ANY_MID | 43 | ↑50 | ↓0.995 | ↓17d | SQ | -4.1% | -51.58/-52.72 | -0.34% | 20% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 29 | ↑57 | ↑1.011 | ↑1d | — | +2.1% | 7.14/4.78 | +2.10% | 20% |
| [CGPOWER](https://in.tradingview.com/chart/?symbol=NSE:CGPOWER)<br><sub>📶W9 · 🚀SS · ↓CMF5d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 29 | ↑69 | ↑1.005 | ↑1d | — | +0.4% | -12.74/-14.29 | +0.38% | 20% |
| [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Digital payments, fintech, consumer and merchant ecosystem | 📈 BULL_ANY_MID | 24 | ↑87 | ↑1.016 | ↑1d | — | +2.3% | 2.77/0.98 | +2.30% | 20% |
| [ETERNAL](https://in.tradingview.com/chart/?symbol=NSE:ETERNAL)<br><sub>📶W9 · ↑CMF2d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 18 | ↑69 | ↓1.004 | ↑2d | — | +2.2% | -0.89/-2.27 | -0.36% | 20% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>📶W9 · W↑14d · ↑CMF6d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 18 | ↑22 | ↑1.000 | ↓12d | — | +0.8% | -18.3/-18.75 | +0.02% | 20% |
| [VBL](https://in.tradingview.com/chart/?symbol=NSE:VBL)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF6d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 13 | ↑42 | ↑1.022 | ↑12d | — | +7.0% | 24.78/23.0 | +3.29% | 20% |
| [GVT&D](https://in.tradingview.com/chart/?symbol=NSE:GVT&D)<br><sub>📶W9 · ↓CMF3d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 12 | ↑70 | ↓0.994 | ↓8d | — | -2.5% | -29.77/-29.83 | -0.32% | -% |
| [HINDOILEXP](https://in.tradingview.com/chart/?symbol=NSE:HINDOILEXP)<br><sub>📶W9 · ↓CMF5d</sub> | ✓ SAFE | Oil gas exploration production onshore offshore India | 📈 BULL_ANY_MID | 3 | ↑66 | ↓0.995 | ↓17d | — | -3.6% | -28.31/-30.76 | -1.44% | 20% |
| [ZOTA](https://in.tradingview.com/chart/?symbol=NSE:ZOTA)<br><sub>📶W9 · W↑14d · ↑CMF1d</sub> | ✓ SAFE | Pharma manufacturer: tablets, syrups, Ayurveda, OTC products | 📈 BULL_ANY_MID | 2 | ↑45 | ↓1.020 | ↑18d | — | +21.6% | 40.56/37.73 | -1.47% | 20% |
| [IFCI](https://in.tradingview.com/chart/?symbol=NSE:IFCI)<br><sub>↓CMF22d</sub> | ✓ SAFE | Industrial credit provider long-term financing manufacturing sector loans | ⚡ BULL_ANY_PPV | 35 | 🔄65 | ↑0.978 | ↓41d | PV | -9.6% | -43.43/-43.89 | +3.75% | 20% |
| [INDIAMART](https://in.tradingview.com/chart/?symbol=NSE:INDIAMART)<br><sub>↑CMF0d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | B2B marketplace connecting MSMEs to suppliers digitally | 🟢 BULL_OVERSOLD | 78 | 🔄12 | ↑0.992 | ↓17d | SQ | -3.4% | -62.05/-62.3 | -0.16% | 20% |
| [TMPV](https://in.tradingview.com/chart/?symbol=NSE:TMPV)<br><sub>🚀SS · ↓CMF26d · 🔥PHX</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 43 | 🔄14 | ↑0.996 | ↓12d | — | -4.3% | -64.81/-66.76 | +3.13% | 20% |
| [INDIANB](https://in.tradingview.com/chart/?symbol=NSE:INDIANB)<br><sub>🚀SS · ↓CMF20d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 35 | 🔄54 | ↑0.991 | ↓21d | — | -8.0% | -61.07/-61.42 | +1.99% | 20% |
| [METROBRAND](https://in.tradingview.com/chart/?symbol=NSE:METROBRAND)<br><sub>↑CMF19d · 🎯SLING</sub> | ✓ SAFE | Footwear and accessories retail across price segments | 🟢 BULL_OVERSOLD | 35 | 🔄11 | ↑0.993 | ↓25d | — | -8.2% | -59.17/-62.03 | +1.88% | 20% |
| [WIPRO](https://in.tradingview.com/chart/?symbol=NSE:WIPRO)<br><sub>🚀SS · ↓CMF4d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 10 | ↑15 | ↑1.000 | ↓25d | — | -8.0% | -59.15/-63.71 | +1.86% | 20% |
| [REPCOHOME](https://in.tradingview.com/chart/?symbol=NSE:REPCOHOME)<br><sub>↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION | Housing loans for residential property purchase construction | 🟢 BULL_OVERSOLD | 6 | ↑26 | ↓0.994 | ↓14d | — | -4.9% | -58.37/-62.76 | -0.79% | 20% |
| [ABB](https://in.tradingview.com/chart/?symbol=NSE:ABB)<br><sub>↓CMF4d · ⚠️TRAP</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 5 | ↑68 | ↑0.989 | ↓24d | — | -8.3% | -64.83/-66.76 | -0.21% | 20% |
| [GOODLUCK](https://in.tradingview.com/chart/?symbol=NSE:GOODLUCK)<br><sub>↓CMF9d</sub> | ✓ SAFE | Steel pipes forgings structural products engineering export | 📈 BULL_ANY_MID | 47 | 🔄0 | ↓0.986 | ↑3d | — | +3.1% | -35.42/-36.91 | -1.03% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:KOTIC,NSE:BHEL,NSE:LICHSGFIN,NSE:VEDL,NSE:SIGMAADV,NSE:EXCELINDUS,NSE:SRF,NSE:COALINDIA,NSE:POLYCAB,NSE:SHYAMMETL,NSE:ELLEN,NSE:TCPLPACK,NSE:ADANIPOWER,NSE:STYLEBAAZA,NSE:UEL,NSE:CANHLIFE,NSE:DLF,NSE:CGPOWER,NSE:PAYTM,NSE:ETERNAL,NSE:HDFCLIFE,NSE:VBL,NSE:GVT&D,NSE:HINDOILEXP,NSE:ZOTA,NSE:IFCI,NSE:INDIAMART,NSE:TMPV,NSE:INDIANB,NSE:METROBRAND,NSE:WIPRO,NSE:REPCOHOME,NSE:ABB,NSE:GOODLUCK
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (12)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [KOTIC](https://in.tradingview.com/chart/?symbol=NSE:KOTIC)<br><sub>📶W9 · RVOL11x · ↓CMF30d · ÷DIV</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 89 | 🔄50 | ↑1.038 | ↑1d | SQ·PV | +6.8% | 18.92/14.02 | +6.83% | 20% 🟦 |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 64 | ↑88 | ↑1.016 | ↑1d | SQ·PV | +1.6% | -7.84/-16.13 | +1.64% | 20% |
| [EXCELINDUS](https://in.tradingview.com/chart/?symbol=NSE:EXCELINDUS)<br><sub>📶W9 · ↓CMF16d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 70 | 🔄50 | ↓0.989 | ↓37d | SQ | -6.8% | -54.83/-55.69 | -0.56% | 20% |
| [SRF](https://in.tradingview.com/chart/?symbol=NSE:SRF)<br><sub>📶W9 · ↓CMF30d</sub> | ⚠ CAUTION | Technical textiles, films, chemicals for automotive, industrial, packaging | 📈 BULL_ANY_MID | 86 | 🔄37 | ↑1.002 | ↓14d | SQ | -1.1% | -41.0/-43.83 | +1.02% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF8d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 69 | ↑54 | ↑1.007 | ↑1d | SQ | +1.4% | 24.57/23.53 | +1.38% | 20% |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL)<br><sub>📶W9 · ↓CMF9d</sub> | ✓ SAFE | Steel long products, ferro alloys, pellets, power generation | 📈 BULL_ANY_MID | 58 | ↑74 | ↓1.005 | ↓2d | SQ | +1.2% | -13.16/-15.53 | -0.05% | 20% |
| [ELLEN](https://in.tradingview.com/chart/?symbol=NSE:ELLEN)<br><sub>📶W9 · ↓CMF6d</sub> | ✓ SAFE | Industrial oxygen nitrogen gases bulk packaged eastern southern India | 📈 BULL_ANY_MID | 58 | ↑74 | ↓0.992 | ↓2d | SQ | +0.6% | -0.94/-2.23 | -4.20% | 20% |
| [TCPLPACK](https://in.tradingview.com/chart/?symbol=NSE:TCPLPACK)<br><sub>📶W9 · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 57 | ↑85 | ↓1.001 | ↑3d | SQ | +1.6% | 27.23/22.92 | -0.92% | 20% |
| [STYLEBAAZA](https://in.tradingview.com/chart/?symbol=NSE:STYLEBAAZA)<br><sub>📶W9 · ↑CMF2d · ÷DIV</sub> | ✓ SAFE | Value fashion apparel retailer eastern India families | 📈 BULL_ANY_MID | 51 | ↑82 | ↓0.989 | ↓9d | SQ | -0.9% | -23.44/-25.66 | -1.99% | 5% |
| [CANHLIFE](https://in.tradingview.com/chart/?symbol=NSE:CANHLIFE)<br><sub>📶W9 · ↑CMF19d</sub> | ⚠ CAUTION | Life insurance through bank distribution channels | 📈 BULL_ANY_MID | 43 | ↑50 | ↓0.995 | ↓17d | SQ | -4.1% | -51.58/-52.72 | -0.34% | 20% |
| [INDIAMART](https://in.tradingview.com/chart/?symbol=NSE:INDIAMART)<br><sub>↑CMF0d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | B2B marketplace connecting MSMEs to suppliers digitally | 🟢 BULL_OVERSOLD | 78 | 🔄12 | ↑0.992 | ↓17d | SQ | -3.4% | -62.05/-62.3 | -0.16% | 20% |
| [PRECAM](https://in.tradingview.com/chart/?symbol=NSE:PRECAM)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Camshaft manufacturer for autos tractors locomotives worldwide | 📈 BULL_ANY_MID | 47 | ↓5 | ↓0.971 | ↓13d | SQ | -6.4% | -50.25/-50.45 | -3.45% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:KOTIC,NSE:BHEL,NSE:EXCELINDUS,NSE:SRF,NSE:COALINDIA,NSE:SHYAMMETL,NSE:ELLEN,NSE:TCPLPACK,NSE:STYLEBAAZA,NSE:CANHLIFE,NSE:INDIAMART,NSE:PRECAM
```

---

### 🔥 MAJOR — PPV confirmed (4)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [LICHSGFIN](https://in.tradingview.com/chart/?symbol=NSE:LICHSGFIN)<br><sub>📶W9 · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Residential mortgage loans for home purchase and construction | ⚡ BULL_ANY_PPV | 54 | 🔄54 | ↑1.019 | ↑1d | PV | +4.2% | -21.25/-21.7 | +4.19% | 20% |
| [VEDL](https://in.tradingview.com/chart/?symbol=NSE:VEDL)<br><sub>📶W9 · 🚀SS · ↑CMF19d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 54 | 🔄3 | ↑1.022 | ↑1d | PV | +4.1% | -36.44/-42.32 | +4.14% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [IFCI](https://in.tradingview.com/chart/?symbol=NSE:IFCI)<br><sub>↓CMF22d</sub> | ✓ SAFE | Industrial credit provider long-term financing manufacturing sector loans | ⚡ BULL_ANY_PPV | 35 | 🔄65 | ↑0.978 | ↓41d | PV | -9.6% | -43.43/-43.89 | +3.75% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LICHSGFIN,NSE:VEDL,NSE:SIGMAADV,NSE:IFCI
```

### 🟢 OVERSOLD — reversal from −53/−60 (10)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [TMPV](https://in.tradingview.com/chart/?symbol=NSE:TMPV)<br><sub>🚀SS · ↓CMF26d · 🔥PHX</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 43 | 🔄14 | ↑0.996 | ↓12d | — | -4.3% | -64.81/-66.76 | +3.13% | 20% |
| [INDIANB](https://in.tradingview.com/chart/?symbol=NSE:INDIANB)<br><sub>🚀SS · ↓CMF20d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 35 | 🔄54 | ↑0.991 | ↓21d | — | -8.0% | -61.07/-61.42 | +1.99% | 20% |
| [METROBRAND](https://in.tradingview.com/chart/?symbol=NSE:METROBRAND)<br><sub>↑CMF19d · 🎯SLING</sub> | ✓ SAFE | Footwear and accessories retail across price segments | 🟢 BULL_OVERSOLD | 35 | 🔄11 | ↑0.993 | ↓25d | — | -8.2% | -59.17/-62.03 | +1.88% | 20% |
| [WIPRO](https://in.tradingview.com/chart/?symbol=NSE:WIPRO)<br><sub>🚀SS · ↓CMF4d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 10 | ↑15 | ↑1.000 | ↓25d | — | -8.0% | -59.15/-63.71 | +1.86% | 20% |
| [CHOLAFIN](https://in.tradingview.com/chart/?symbol=NSE:CHOLAFIN)<br><sub>🚀SS · ↑CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 9 | ↓44 | ↑0.966 | ↓16d | — | -12.3% | -76.91/-77.55 | +1.49% | 20% |
| [REPCOHOME](https://in.tradingview.com/chart/?symbol=NSE:REPCOHOME)<br><sub>↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION | Housing loans for residential property purchase construction | 🟢 BULL_OVERSOLD | 6 | ↑26 | ↓0.994 | ↓14d | — | -4.9% | -58.37/-62.76 | -0.79% | 20% |
| [ABB](https://in.tradingview.com/chart/?symbol=NSE:ABB)<br><sub>↓CMF4d · ⚠️TRAP</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 5 | ↑68 | ↑0.989 | ↓24d | — | -8.3% | -64.83/-66.76 | -0.21% | 20% |
| [JIOFIN](https://in.tradingview.com/chart/?symbol=NSE:JIOFIN)<br><sub>↓CMF28d · ⚠️TRAP</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 0 | ↓21 | ↓0.986 | ↓49d | — | -8.7% | -65.94/-69.33 | -0.71% | 20% |
| [TATACAP](https://in.tradingview.com/chart/?symbol=NSE:TATACAP)<br><sub>↓CMF3d · ⚠️TRAP</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 0 | ↓50 | ↓0.975 | ↓23d | — | -12.2% | -63.82/-64.63 | -0.59% | 20% |
| [DECNGOLD](https://in.tradingview.com/chart/?symbol=NSE:DECNGOLD)<br><sub>↓CMF23d · ⚠️TRAP</sub> | ✓ SAFE | Gold exploration and mining transitioning to active production | 🟡 BULL_OS_L2 | 8 | ↓50 | ↓0.950 | ↓12d | — | -12.1% | -53.38/-53.87 | -3.82% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:TMPV,NSE:INDIANB,NSE:METROBRAND,NSE:WIPRO,NSE:CHOLAFIN,NSE:REPCOHOME,NSE:ABB,NSE:JIOFIN,NSE:TATACAP,NSE:DECNGOLD
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (14)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [POLYCAB](https://in.tradingview.com/chart/?symbol=NSE:POLYCAB)<br><sub>📶W9 · ↑CMF0d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 59 | 🔄54 | ↑1.013 | ↑1d | — | +2.0% | -44.27/-49.73 | +1.99% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 52 | 🔄70 | ↑1.000 | ↓3d | — | +2.5% | -41.74/-41.75 | +2.49% | 20% |
| [UEL](https://in.tradingview.com/chart/?symbol=NSE:UEL)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Solar power generation, EV manufacturing, renewable energy sector | 📈 BULL_ANY_MID | 49 | 🔄50 | ↑1.050 | ↑1d | — | +10.0% | -38.4/-43.61 | +10.00% | 20% 🟦 |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>📶W9 · W↑1d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 29 | ↑57 | ↑1.011 | ↑1d | — | +2.1% | 7.14/4.78 | +2.10% | 20% |
| [CGPOWER](https://in.tradingview.com/chart/?symbol=NSE:CGPOWER)<br><sub>📶W9 · 🚀SS · ↓CMF5d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 29 | ↑69 | ↑1.005 | ↑1d | — | +0.4% | -12.74/-14.29 | +0.38% | 20% |
| [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Digital payments, fintech, consumer and merchant ecosystem | 📈 BULL_ANY_MID | 24 | ↑87 | ↑1.016 | ↑1d | — | +2.3% | 2.77/0.98 | +2.30% | 20% |
| [ETERNAL](https://in.tradingview.com/chart/?symbol=NSE:ETERNAL)<br><sub>📶W9 · ↑CMF2d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 18 | ↑69 | ↓1.004 | ↑2d | — | +2.2% | -0.89/-2.27 | -0.36% | 20% |
| [HDFCLIFE](https://in.tradingview.com/chart/?symbol=NSE:HDFCLIFE)<br><sub>📶W9 · W↑14d · ↑CMF6d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 18 | ↑22 | ↑1.000 | ↓12d | — | +0.8% | -18.3/-18.75 | +0.02% | 20% |
| [VBL](https://in.tradingview.com/chart/?symbol=NSE:VBL)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF6d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 13 | ↑42 | ↑1.022 | ↑12d | — | +7.0% | 24.78/23.0 | +3.29% | 20% |
| [GVT&D](https://in.tradingview.com/chart/?symbol=NSE:GVT&D)<br><sub>📶W9 · ↓CMF3d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 12 | ↑70 | ↓0.994 | ↓8d | — | -2.5% | -29.77/-29.83 | -0.32% | -% |
| [HINDOILEXP](https://in.tradingview.com/chart/?symbol=NSE:HINDOILEXP)<br><sub>📶W9 · ↓CMF5d</sub> | ✓ SAFE | Oil gas exploration production onshore offshore India | 📈 BULL_ANY_MID | 3 | ↑66 | ↓0.995 | ↓17d | — | -3.6% | -28.31/-30.76 | -1.44% | 20% |
| [ZOTA](https://in.tradingview.com/chart/?symbol=NSE:ZOTA)<br><sub>📶W9 · W↑14d · ↑CMF1d</sub> | ✓ SAFE | Pharma manufacturer: tablets, syrups, Ayurveda, OTC products | 📈 BULL_ANY_MID | 2 | ↑45 | ↓1.020 | ↑18d | — | +21.6% | 40.56/37.73 | -1.47% | 20% |
| [GOODLUCK](https://in.tradingview.com/chart/?symbol=NSE:GOODLUCK)<br><sub>↓CMF9d</sub> | ✓ SAFE | Steel pipes forgings structural products engineering export | 📈 BULL_ANY_MID | 47 | 🔄0 | ↓0.986 | ↑3d | — | +3.1% | -35.42/-36.91 | -1.03% | 20% |
| [NIACL](https://in.tradingview.com/chart/?symbol=NSE:NIACL)<br><sub>↓CMF4d</sub> | ✓ SAFE | General insurance underwriting and claims across India | 📈 BULL_ANY_MID | 9 | ↓42 | ↑0.958 | ↓16d | — | -14.1% | -48.07/-48.23 | -0.72% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:POLYCAB,NSE:ADANIPOWER,NSE:UEL,NSE:DLF,NSE:CGPOWER,NSE:PAYTM,NSE:ETERNAL,NSE:HDFCLIFE,NSE:VBL,NSE:GVT&D,NSE:HINDOILEXP,NSE:ZOTA,NSE:GOODLUCK,NSE:NIACL
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
