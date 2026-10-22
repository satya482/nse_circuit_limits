> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-10-22
*Generated 2026-10-22 15:46 IST*

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

**Total bull crosses today: 27** · 10 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:EFCIL,NSE:MAHLIFE,NSE:SUNTECK,NSE:SIGMAADV,NSE:GAIL,NSE:TMCV,NSE:SAILIFE,NSE:ITC,NSE:COALINDIA,NSE:VADILALIND,NSE:PNBGILTS,NSE:CORONA,NSE:GODREJCP,NSE:TCI,NSE:KPL,NSE:NHPC,NSE:FSL,NSE:PERSISTENT,NSE:GNA,NSE:JSWSTEEL,NSE:TENNIND,NSE:WINDLAS,NSE:HDBFS,NSE:CANHLIFE,NSE:BPCL,NSE:ADANIPOWER,NSE:JINDALSTEL
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (19)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [EFCIL](https://in.tradingview.com/chart/?symbol=NSE:EFCIL)<br><sub>📶W9 · ↓CMF23d · ÷DIV</sub> | ✓ SAFE | Managed office spaces, integrated building services, corporate real estate | ⚡ BULL_ANY_PPV | 94 | 🔄17 | ↑1.028 | ↑1d | SQ·PV | +6.1% | -34.81/-36.78 | +6.11% | 20% |
| [MAHLIFE](https://in.tradingview.com/chart/?symbol=NSE:MAHLIFE)<br><sub>📶W9 · RVOL23x · ↑CMF9d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Residential and industrial real estate development across India | ⚡ BULL_ANY_PPV | 69 | ↑52 | ↑1.012 | ↑1d | SQ·PV | +3.1% | -51.52/-53.04 | +3.10% | 20% |
| [SUNTECK](https://in.tradingview.com/chart/?symbol=NSE:SUNTECK)<br><sub>📶W9 · RVOL205x · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Luxury residential developer MMR premium apartments commercial | ⚡ BULL_ANY_PPV | 59 | ↑21 | ↑1.032 | ↑1d | SQ·PV | +5.3% | -40.69/-49.82 | +5.29% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄57 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>📶W9 · ↓CMF16d · 🎯SLING</sub> | ✓ SAFE | CRDMO drug discovery manufacturing pharma biotech | 🟡 BULL_OS_L2 | 35 | 🔄90 | ↑0.979 | ↓25d | — | -9.7% | -55.6/-56.11 | +0.17% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄22 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑55 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [VADILALIND](https://in.tradingview.com/chart/?symbol=NSE:VADILALIND)<br><sub>📶W9 · ↓CMF22d</sub> | ⚠ CAUTION | Ice cream and frozen desserts manufacturer, Indian consumer market | 📈 BULL_ANY_MID | 69 | ↑89 | ↑1.005 | ↑1d | SQ | +1.8% | -32.98/-33.49 | +1.76% | 20% |
| [PNBGILTS](https://in.tradingview.com/chart/?symbol=NSE:PNBGILTS)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Government securities underwriting and debt market trading | 📈 BULL_ANY_MID | 69 | ↑43 | ↑1.014 | ↑1d | SQ | +3.7% | -31.85/-32.66 | +3.66% | 20% |
| [CORONA](https://in.tradingview.com/chart/?symbol=NSE:CORONA)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Pharma formulations women's health cardiology pain management domestic | 📈 BULL_ANY_MID | 69 | ↑50 | ↑1.007 | ↑1d | SQ | +1.1% | -29.83/-33.93 | +1.13% | 20% |
| [GODREJCP](https://in.tradingview.com/chart/?symbol=NSE:GODREJCP)<br><sub>📶W9 · W↑9d · ↑CMF3d</sub> | ⚠ CAUTION | Household insecticides, personal care, emerging markets FMCG | 📈 BULL_ANY_MID | 68 | ↑14 | ↑1.003 | ↑2d | SQ | +1.6% | -23.35/-24.87 | +0.14% | 20% |
| [TCI](https://in.tradingview.com/chart/?symbol=NSE:TCI)<br><sub>📶W9 · W↑19d · ↓CMF30d</sub> | ✓ SAFE | Multimodal logistics freight transport supply chain solutions | 📈 BULL_ANY_MID | 68 | ↑39 | ↑1.012 | ↑2d | SQ | +1.8% | -0.46/-6.09 | +1.49% | 20% |
| [KPL](https://in.tradingview.com/chart/?symbol=NSE:KPL)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Pharma manufacturer finished dosages domestic international markets | 📈 BULL_ANY_MID | 19 | ↑50 | ↑1.034 | ↑1d | — | +5.5% | -22.73/-26.49 | +5.51% | 20% |
| [NHPC](https://in.tradingview.com/chart/?symbol=NSE:NHPC)<br><sub>📶W9 · ↓CMF4d</sub> | ⚠ CAUTION | Hydroelectric and renewable power generation for utilities | 📈 BULL_ANY_MID | 18 | ↑41 | ↓1.002 | ↓2d | — | +2.4% | -44.41/-49.38 | -0.37% | 20% |
| [FSL](https://in.tradingview.com/chart/?symbol=NSE:FSL)<br><sub>📶W9 · W↑9d · ↓CMF7d</sub> | ✓ SAFE | BPM services for healthcare insurance banking finance | 📈 BULL_ANY_MID | 7 | ↑72 | ↑1.035 | ↑13d | — | +12.4% | 33.61/30.88 | +1.81% | 20% |
| [PERSISTENT](https://in.tradingview.com/chart/?symbol=NSE:PERSISTENT)<br><sub>📶W9 · W↑9d · ↑CMF4d</sub> | ✓ SAFE | Digital engineering services, cloud modernization, enterprise software | 📈 BULL_ANY_MID | 6 | ↑66 | ↓1.001 | ↑14d | — | +7.0% | 33.8/33.43 | -2.01% | 20% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>📶W9 · ↓CMF0d · ⚠️TRAP</sub> | ✓ SAFE | Rear axles and drive shafts for commercial vehicles | 📈 BULL_ANY_MID | 0 | ↑87 | ↓0.986 | ↓25d | — | -1.2% | -31.52/-31.97 | -1.68% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:EFCIL,NSE:MAHLIFE,NSE:SUNTECK,NSE:SIGMAADV,NSE:GAIL,NSE:TMCV,NSE:SAILIFE,NSE:ITC,NSE:COALINDIA,NSE:VADILALIND,NSE:PNBGILTS,NSE:CORONA,NSE:GODREJCP,NSE:TCI,NSE:KPL,NSE:NHPC,NSE:FSL,NSE:PERSISTENT,NSE:GNA
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (24)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [EFCIL](https://in.tradingview.com/chart/?symbol=NSE:EFCIL)<br><sub>📶W9 · ↓CMF23d · ÷DIV</sub> | ✓ SAFE | Managed office spaces, integrated building services, corporate real estate | ⚡ BULL_ANY_PPV | 94 | 🔄17 | ↑1.028 | ↑1d | SQ·PV | +6.1% | -34.81/-36.78 | +6.11% | 20% |
| [MAHLIFE](https://in.tradingview.com/chart/?symbol=NSE:MAHLIFE)<br><sub>📶W9 · RVOL23x · ↑CMF9d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Residential and industrial real estate development across India | ⚡ BULL_ANY_PPV | 69 | ↑52 | ↑1.012 | ↑1d | SQ·PV | +3.1% | -51.52/-53.04 | +3.10% | 20% |
| [SUNTECK](https://in.tradingview.com/chart/?symbol=NSE:SUNTECK)<br><sub>📶W9 · RVOL205x · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Luxury residential developer MMR premium apartments commercial | ⚡ BULL_ANY_PPV | 59 | ↑21 | ↑1.032 | ↑1d | SQ·PV | +5.3% | -40.69/-49.82 | +5.29% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄57 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>📶W9 · ↓CMF16d · 🎯SLING</sub> | ✓ SAFE | CRDMO drug discovery manufacturing pharma biotech | 🟡 BULL_OS_L2 | 35 | 🔄90 | ↑0.979 | ↓25d | — | -9.7% | -55.6/-56.11 | +0.17% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄22 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑55 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [VADILALIND](https://in.tradingview.com/chart/?symbol=NSE:VADILALIND)<br><sub>📶W9 · ↓CMF22d</sub> | ⚠ CAUTION | Ice cream and frozen desserts manufacturer, Indian consumer market | 📈 BULL_ANY_MID | 69 | ↑89 | ↑1.005 | ↑1d | SQ | +1.8% | -32.98/-33.49 | +1.76% | 20% |
| [PNBGILTS](https://in.tradingview.com/chart/?symbol=NSE:PNBGILTS)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Government securities underwriting and debt market trading | 📈 BULL_ANY_MID | 69 | ↑43 | ↑1.014 | ↑1d | SQ | +3.7% | -31.85/-32.66 | +3.66% | 20% |
| [CORONA](https://in.tradingview.com/chart/?symbol=NSE:CORONA)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Pharma formulations women's health cardiology pain management domestic | 📈 BULL_ANY_MID | 69 | ↑50 | ↑1.007 | ↑1d | SQ | +1.1% | -29.83/-33.93 | +1.13% | 20% |
| [GODREJCP](https://in.tradingview.com/chart/?symbol=NSE:GODREJCP)<br><sub>📶W9 · W↑9d · ↑CMF3d</sub> | ⚠ CAUTION | Household insecticides, personal care, emerging markets FMCG | 📈 BULL_ANY_MID | 68 | ↑14 | ↑1.003 | ↑2d | SQ | +1.6% | -23.35/-24.87 | +0.14% | 20% |
| [TCI](https://in.tradingview.com/chart/?symbol=NSE:TCI)<br><sub>📶W9 · W↑19d · ↓CMF30d</sub> | ✓ SAFE | Multimodal logistics freight transport supply chain solutions | 📈 BULL_ANY_MID | 68 | ↑39 | ↑1.012 | ↑2d | SQ | +1.8% | -0.46/-6.09 | +1.49% | 20% |
| [KPL](https://in.tradingview.com/chart/?symbol=NSE:KPL)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Pharma manufacturer finished dosages domestic international markets | 📈 BULL_ANY_MID | 19 | ↑50 | ↑1.034 | ↑1d | — | +5.5% | -22.73/-26.49 | +5.51% | 20% |
| [NHPC](https://in.tradingview.com/chart/?symbol=NSE:NHPC)<br><sub>📶W9 · ↓CMF4d</sub> | ⚠ CAUTION | Hydroelectric and renewable power generation for utilities | 📈 BULL_ANY_MID | 18 | ↑41 | ↓1.002 | ↓2d | — | +2.4% | -44.41/-49.38 | -0.37% | 20% |
| [FSL](https://in.tradingview.com/chart/?symbol=NSE:FSL)<br><sub>📶W9 · W↑9d · ↓CMF7d</sub> | ✓ SAFE | BPM services for healthcare insurance banking finance | 📈 BULL_ANY_MID | 7 | ↑72 | ↑1.035 | ↑13d | — | +12.4% | 33.61/30.88 | +1.81% | 20% |
| [PERSISTENT](https://in.tradingview.com/chart/?symbol=NSE:PERSISTENT)<br><sub>📶W9 · W↑9d · ↑CMF4d</sub> | ✓ SAFE | Digital engineering services, cloud modernization, enterprise software | 📈 BULL_ANY_MID | 6 | ↑66 | ↓1.001 | ↑14d | — | +7.0% | 33.8/33.43 | -2.01% | 20% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>📶W9 · ↓CMF0d · ⚠️TRAP</sub> | ✓ SAFE | Rear axles and drive shafts for commercial vehicles | 📈 BULL_ANY_MID | 0 | ↑87 | ↓0.986 | ↓25d | — | -1.2% | -31.52/-31.97 | -1.68% | 20% |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 42 | 🔄53 | ↑0.992 | ↓13d | — | -5.3% | -64.43/-65.64 | +2.00% | 20% |
| [TENNIND](https://in.tradingview.com/chart/?symbol=NSE:TENNIND)<br><sub>↓CMF25d · 🎯SLING</sub> | ✓ SAFE | Automotive emissions control systems supplier for passenger vehicles | 🟢 BULL_OVERSOLD | 35 | 🔄50 | ↑0.979 | ↓23d | — | -12.4% | -68.31/-68.71 | +0.55% | 20% |
| [WINDLAS](https://in.tradingview.com/chart/?symbol=NSE:WINDLAS)<br><sub>↓CMF16d · 🎯SLING</sub> | ✓ SAFE | Oral solid liquid pharma formulations CDMO manufacturing | 🟢 BULL_OVERSOLD | 35 | 🔄68 | ↑0.971 | ↓26d | — | -16.2% | -60.2/-61.11 | +2.17% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 41 | 🔄38 | ↑1.001 | ↓19d | — | -4.4% | -53.92/-57.54 | +1.19% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 22 | ↑67 | ↑1.004 | ↓8d | — | -0.3% | -53.58/-59.08 | +0.30% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:EFCIL,NSE:MAHLIFE,NSE:SUNTECK,NSE:SIGMAADV,NSE:GAIL,NSE:TMCV,NSE:SAILIFE,NSE:ITC,NSE:COALINDIA,NSE:VADILALIND,NSE:PNBGILTS,NSE:CORONA,NSE:GODREJCP,NSE:TCI,NSE:KPL,NSE:NHPC,NSE:FSL,NSE:PERSISTENT,NSE:GNA,NSE:JSWSTEEL,NSE:TENNIND,NSE:WINDLAS,NSE:BPCL,NSE:ADANIPOWER
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (10)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [EFCIL](https://in.tradingview.com/chart/?symbol=NSE:EFCIL)<br><sub>📶W9 · ↓CMF23d · ÷DIV</sub> | ✓ SAFE | Managed office spaces, integrated building services, corporate real estate | ⚡ BULL_ANY_PPV | 94 | 🔄17 | ↑1.028 | ↑1d | SQ·PV | +6.1% | -34.81/-36.78 | +6.11% | 20% |
| [MAHLIFE](https://in.tradingview.com/chart/?symbol=NSE:MAHLIFE)<br><sub>📶W9 · RVOL23x · ↑CMF9d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | Residential and industrial real estate development across India | ⚡ BULL_ANY_PPV | 69 | ↑52 | ↑1.012 | ↑1d | SQ·PV | +3.1% | -51.52/-53.04 | +3.10% | 20% |
| [SUNTECK](https://in.tradingview.com/chart/?symbol=NSE:SUNTECK)<br><sub>📶W9 · RVOL205x · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Luxury residential developer MMR premium apartments commercial | ⚡ BULL_ANY_PPV | 59 | ↑21 | ↑1.032 | ↑1d | SQ·PV | +5.3% | -40.69/-49.82 | +5.29% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄22 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑55 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [VADILALIND](https://in.tradingview.com/chart/?symbol=NSE:VADILALIND)<br><sub>📶W9 · ↓CMF22d</sub> | ⚠ CAUTION | Ice cream and frozen desserts manufacturer, Indian consumer market | 📈 BULL_ANY_MID | 69 | ↑89 | ↑1.005 | ↑1d | SQ | +1.8% | -32.98/-33.49 | +1.76% | 20% |
| [PNBGILTS](https://in.tradingview.com/chart/?symbol=NSE:PNBGILTS)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Government securities underwriting and debt market trading | 📈 BULL_ANY_MID | 69 | ↑43 | ↑1.014 | ↑1d | SQ | +3.7% | -31.85/-32.66 | +3.66% | 20% |
| [CORONA](https://in.tradingview.com/chart/?symbol=NSE:CORONA)<br><sub>📶W9 · ↑CMF0d</sub> | ⚠ CAUTION | Pharma formulations women's health cardiology pain management domestic | 📈 BULL_ANY_MID | 69 | ↑50 | ↑1.007 | ↑1d | SQ | +1.1% | -29.83/-33.93 | +1.13% | 20% |
| [GODREJCP](https://in.tradingview.com/chart/?symbol=NSE:GODREJCP)<br><sub>📶W9 · W↑9d · ↑CMF3d</sub> | ⚠ CAUTION | Household insecticides, personal care, emerging markets FMCG | 📈 BULL_ANY_MID | 68 | ↑14 | ↑1.003 | ↑2d | SQ | +1.6% | -23.35/-24.87 | +0.14% | 20% |
| [TCI](https://in.tradingview.com/chart/?symbol=NSE:TCI)<br><sub>📶W9 · W↑19d · ↓CMF30d</sub> | ✓ SAFE | Multimodal logistics freight transport supply chain solutions | 📈 BULL_ANY_MID | 68 | ↑39 | ↑1.012 | ↑2d | SQ | +1.8% | -0.46/-6.09 | +1.49% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:EFCIL,NSE:MAHLIFE,NSE:SUNTECK,NSE:ITC,NSE:COALINDIA,NSE:VADILALIND,NSE:PNBGILTS,NSE:CORONA,NSE:GODREJCP,NSE:TCI
```

---

### 🔥 MAJOR — PPV confirmed (1)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV
```

### 🟢 OVERSOLD — reversal from −53/−60 (10)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄57 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>📶W9 · ↓CMF16d · 🎯SLING</sub> | ✓ SAFE | CRDMO drug discovery manufacturing pharma biotech | 🟡 BULL_OS_L2 | 35 | 🔄90 | ↑0.979 | ↓25d | — | -9.7% | -55.6/-56.11 | +0.17% | 20% |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 42 | 🔄53 | ↑0.992 | ↓13d | — | -5.3% | -64.43/-65.64 | +2.00% | 20% |
| [TENNIND](https://in.tradingview.com/chart/?symbol=NSE:TENNIND)<br><sub>↓CMF25d · 🎯SLING</sub> | ✓ SAFE | Automotive emissions control systems supplier for passenger vehicles | 🟢 BULL_OVERSOLD | 35 | 🔄50 | ↑0.979 | ↓23d | — | -12.4% | -68.31/-68.71 | +0.55% | 20% |
| [WINDLAS](https://in.tradingview.com/chart/?symbol=NSE:WINDLAS)<br><sub>↓CMF16d · 🎯SLING</sub> | ✓ SAFE | Oral solid liquid pharma formulations CDMO manufacturing | 🟢 BULL_OVERSOLD | 35 | 🔄68 | ↑0.971 | ↓26d | — | -16.2% | -60.2/-61.11 | +2.17% | 20% |
| [HDBFS](https://in.tradingview.com/chart/?symbol=NSE:HDBFS)<br><sub>↓CMF16d · 🎯SLING</sub> | ✓ SAFE | Vehicle loans and personal finance for underbanked consumers | 🟢 BULL_OVERSOLD | 5 | ↓9 | ↑0.944 | ↓27d | — | -23.3% | -75.88/-77.46 | -0.43% | 20% |
| [CANHLIFE](https://in.tradingview.com/chart/?symbol=NSE:CANHLIFE)<br><sub>↑CMF29d · ⚠️TRAP</sub> | ⚠ CAUTION | Life insurance through bank distribution channels | 🟢 BULL_OVERSOLD | 0 | ↓51 | ↓0.952 | ↓27d | — | -17.1% | -73.5/-73.56 | -1.64% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 41 | 🔄38 | ↑1.001 | ↓19d | — | -4.4% | -53.92/-57.54 | +1.19% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 22 | ↑67 | ↑1.004 | ↓8d | — | -0.3% | -53.58/-59.08 | +0.30% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GAIL,NSE:TMCV,NSE:SAILIFE,NSE:JSWSTEEL,NSE:TENNIND,NSE:WINDLAS,NSE:HDBFS,NSE:CANHLIFE,NSE:BPCL,NSE:ADANIPOWER
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (6)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [KPL](https://in.tradingview.com/chart/?symbol=NSE:KPL)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Pharma manufacturer finished dosages domestic international markets | 📈 BULL_ANY_MID | 19 | ↑50 | ↑1.034 | ↑1d | — | +5.5% | -22.73/-26.49 | +5.51% | 20% |
| [NHPC](https://in.tradingview.com/chart/?symbol=NSE:NHPC)<br><sub>📶W9 · ↓CMF4d</sub> | ⚠ CAUTION | Hydroelectric and renewable power generation for utilities | 📈 BULL_ANY_MID | 18 | ↑41 | ↓1.002 | ↓2d | — | +2.4% | -44.41/-49.38 | -0.37% | 20% |
| [FSL](https://in.tradingview.com/chart/?symbol=NSE:FSL)<br><sub>📶W9 · W↑9d · ↓CMF7d</sub> | ✓ SAFE | BPM services for healthcare insurance banking finance | 📈 BULL_ANY_MID | 7 | ↑72 | ↑1.035 | ↑13d | — | +12.4% | 33.61/30.88 | +1.81% | 20% |
| [PERSISTENT](https://in.tradingview.com/chart/?symbol=NSE:PERSISTENT)<br><sub>📶W9 · W↑9d · ↑CMF4d</sub> | ✓ SAFE | Digital engineering services, cloud modernization, enterprise software | 📈 BULL_ANY_MID | 6 | ↑66 | ↓1.001 | ↑14d | — | +7.0% | 33.8/33.43 | -2.01% | 20% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>📶W9 · ↓CMF0d · ⚠️TRAP</sub> | ✓ SAFE | Rear axles and drive shafts for commercial vehicles | 📈 BULL_ANY_MID | 0 | ↑87 | ↓0.986 | ↓25d | — | -1.2% | -31.52/-31.97 | -1.68% | 20% |
| [JINDALSTEL](https://in.tradingview.com/chart/?symbol=NSE:JINDALSTEL)<br><sub>↓CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 8 | ↓49 | ↑0.982 | ↓17d | — | -8.9% | -51.85/-52.67 | +0.08% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:KPL,NSE:NHPC,NSE:FSL,NSE:PERSISTENT,NSE:GNA,NSE:JINDALSTEL
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
