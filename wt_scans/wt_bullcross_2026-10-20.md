> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-10-20
*Generated 2026-10-20 15:45 IST*

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

**Total bull crosses today: 41** · 12 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV,NSE:GAIL,NSE:TMCV,NSE:THEJO,NSE:ITC,NSE:COALINDIA,NSE:LLOYDSENGG,NSE:EIHAHOTELS,NSE:DISAQ,NSE:VRLLOG,NSE:VADILALIND,NSE:CUB,NSE:GARFIBRES,NSE:TMB,NSE:GODREJAGRO,NSE:BEML,NSE:SSWL,NSE:IRMENERGY,NSE:JSWSTEEL,NSE:TIMKEN,NSE:MEDPLUS,NSE:XPROINDIA,NSE:TITAGARH,NSE:MOSCHIP,NSE:WINDLAS,NSE:RAMCOCEM,NSE:VIMTALABS,NSE:SENORES,NSE:BPCL,NSE:ADANIPOWER,NSE:DIVGIITTS,NSE:JUBLFOOD,NSE:RUBICON,NSE:KNRCON,NSE:SAPPHIRE,NSE:BUILDPRO,NSE:JINDALSTEL,NSE:MFSL,NSE:DATAPATTNS,NSE:NEPHROPLUS,NSE:TSFINV
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (17)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄56 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [THEJO](https://in.tradingview.com/chart/?symbol=NSE:THEJO)<br><sub>📶W9 · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Bulk material handling, mineral processing, corrosion protection equipment | 🟡 BULL_OS_L2 | 10 | ↑69 | ↑0.999 | ↓15d | — | -4.2% | -52.58/-55.81 | +0.00% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄22 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑54 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>📶W9 · W↑17d · ↑CMF17d</sub> | ✓ SAFE | Heavy equipment manufacturing for oil gas power plants | 📈 BULL_ANY_MID | 62 | ↑90 | ↑0.996 | ↓3d | SQ | +3.0% | 6.85/6.21 | +0.00% | 20% |
| [EIHAHOTELS](https://in.tradingview.com/chart/?symbol=NSE:EIHAHOTELS)<br><sub>📶W9 · 🚀SS · ↓CMF1d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 62 | ↑30 | ↑0.992 | ↓3d | SQ | +0.2% | -21.26/-21.64 | +0.00% | 20% |
| [DISAQ](https://in.tradingview.com/chart/?symbol=NSE:DISAQ)<br><sub>📶W9 · ↓CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 59 | 🔄50 | ↑1.014 | ↑1d | — | +2.6% | -38.38/-39.62 | +2.64% | 20% |
| [VRLLOG](https://in.tradingview.com/chart/?symbol=NSE:VRLLOG)<br><sub>📶W9 · ↓CMF17d</sub> | ⚠ CAUTION | Full truck load transport, LTL, bus operations, logistics | 📈 BULL_ANY_MID | 58 | ↑73 | ↓1.004 | ↑2d | SQ | +2.3% | -25.67/-26.25 | +0.00% | 20% |
| [VADILALIND](https://in.tradingview.com/chart/?symbol=NSE:VADILALIND)<br><sub>📶W9 · ↓CMF20d · ⚠️TRAP</sub> | ⚠ CAUTION | Ice cream and frozen desserts manufacturer, Indian consumer market | 📈 BULL_ANY_MID | 58 | ↑86 | ↑0.996 | ↓7d | SQ | -0.1% | -30.9/-32.06 | +0.00% | 20% |
| [CUB](https://in.tradingview.com/chart/?symbol=NSE:CUB)<br><sub>📶W9 · W↑42d · ↑CMF0d</sub> | ⚠ CAUTION | Private bank serving SMEs, MSMEs, retail customers South India | 📈 BULL_ANY_MID | 57 | ↑47 | ↓1.011 | ↑3d | SQ | +3.4% | 11.07/8.1 | +0.00% | 20% |
| [GARFIBRES](https://in.tradingview.com/chart/?symbol=NSE:GARFIBRES)<br><sub>📶W9 · ↑CMF1d · ⚠️TRAP</sub> | ⚠ CAUTION | Technical textiles and ropes for agriculture aquaculture infrastructure | 📈 BULL_ANY_MID | 45 | ↑69 | ↑0.998 | ↓23d | SQ | -4.2% | -35.54/-36.33 | +0.00% | 20% |
| [TMB](https://in.tradingview.com/chart/?symbol=NSE:TMB)<br><sub>📶W9 · ↓CMF16d · ⚠️TRAP</sub> | ⚠ CAUTION | Regional private bank serving retail agriculture MSME segments | 📈 BULL_ANY_MID | 40 | ↑88 | ↓1.001 | ↓20d | SQ | -1.7% | -38.04/-38.45 | +0.00% | 20% |
| [GODREJAGRO](https://in.tradingview.com/chart/?symbol=NSE:GODREJAGRO)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Animal feed, oil palm, crop protection for farmers | 📈 BULL_ANY_MID | 40 | ↑67 | ↓1.002 | ↓20d | SQ | -3.0% | -27.19/-31.17 | +0.00% | 20% |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML)<br><sub>📶W9 · 🚀SS · ↓CMF2d · ⚠️TRAP</sub> | ✓ SAFE | Heavy equipment manufacturing for mining construction defense railways | 📈 BULL_ANY_MID | 20 | ↑66 | ↑0.991 | ↓5d | — | -2.0% | -21.71/-22.32 | +0.00% | 20% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>📶W9 · ↑CMF11d</sub> | ✓ SAFE | Steel and alloy wheel rims manufacturer for automobiles | 📈 BULL_ANY_MID | 0 | ↑96 | ↓1.005 | ↑23d | — | +18.3% | 43.89/42.7 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV,NSE:GAIL,NSE:TMCV,NSE:THEJO,NSE:ITC,NSE:COALINDIA,NSE:LLOYDSENGG,NSE:EIHAHOTELS,NSE:DISAQ,NSE:VRLLOG,NSE:VADILALIND,NSE:CUB,NSE:GARFIBRES,NSE:TMB,NSE:GODREJAGRO,NSE:BEML,NSE:SSWL
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (20)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄56 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [THEJO](https://in.tradingview.com/chart/?symbol=NSE:THEJO)<br><sub>📶W9 · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Bulk material handling, mineral processing, corrosion protection equipment | 🟡 BULL_OS_L2 | 10 | ↑69 | ↑0.999 | ↓15d | — | -4.2% | -52.58/-55.81 | +0.00% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄22 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑54 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>📶W9 · W↑17d · ↑CMF17d</sub> | ✓ SAFE | Heavy equipment manufacturing for oil gas power plants | 📈 BULL_ANY_MID | 62 | ↑90 | ↑0.996 | ↓3d | SQ | +3.0% | 6.85/6.21 | +0.00% | 20% |
| [EIHAHOTELS](https://in.tradingview.com/chart/?symbol=NSE:EIHAHOTELS)<br><sub>📶W9 · 🚀SS · ↓CMF1d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 62 | ↑30 | ↑0.992 | ↓3d | SQ | +0.2% | -21.26/-21.64 | +0.00% | 20% |
| [DISAQ](https://in.tradingview.com/chart/?symbol=NSE:DISAQ)<br><sub>📶W9 · ↓CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 59 | 🔄50 | ↑1.014 | ↑1d | — | +2.6% | -38.38/-39.62 | +2.64% | 20% |
| [VRLLOG](https://in.tradingview.com/chart/?symbol=NSE:VRLLOG)<br><sub>📶W9 · ↓CMF17d</sub> | ⚠ CAUTION | Full truck load transport, LTL, bus operations, logistics | 📈 BULL_ANY_MID | 58 | ↑73 | ↓1.004 | ↑2d | SQ | +2.3% | -25.67/-26.25 | +0.00% | 20% |
| [VADILALIND](https://in.tradingview.com/chart/?symbol=NSE:VADILALIND)<br><sub>📶W9 · ↓CMF20d · ⚠️TRAP</sub> | ⚠ CAUTION | Ice cream and frozen desserts manufacturer, Indian consumer market | 📈 BULL_ANY_MID | 58 | ↑86 | ↑0.996 | ↓7d | SQ | -0.1% | -30.9/-32.06 | +0.00% | 20% |
| [CUB](https://in.tradingview.com/chart/?symbol=NSE:CUB)<br><sub>📶W9 · W↑42d · ↑CMF0d</sub> | ⚠ CAUTION | Private bank serving SMEs, MSMEs, retail customers South India | 📈 BULL_ANY_MID | 57 | ↑47 | ↓1.011 | ↑3d | SQ | +3.4% | 11.07/8.1 | +0.00% | 20% |
| [GARFIBRES](https://in.tradingview.com/chart/?symbol=NSE:GARFIBRES)<br><sub>📶W9 · ↑CMF1d · ⚠️TRAP</sub> | ⚠ CAUTION | Technical textiles and ropes for agriculture aquaculture infrastructure | 📈 BULL_ANY_MID | 45 | ↑69 | ↑0.998 | ↓23d | SQ | -4.2% | -35.54/-36.33 | +0.00% | 20% |
| [TMB](https://in.tradingview.com/chart/?symbol=NSE:TMB)<br><sub>📶W9 · ↓CMF16d · ⚠️TRAP</sub> | ⚠ CAUTION | Regional private bank serving retail agriculture MSME segments | 📈 BULL_ANY_MID | 40 | ↑88 | ↓1.001 | ↓20d | SQ | -1.7% | -38.04/-38.45 | +0.00% | 20% |
| [GODREJAGRO](https://in.tradingview.com/chart/?symbol=NSE:GODREJAGRO)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Animal feed, oil palm, crop protection for farmers | 📈 BULL_ANY_MID | 40 | ↑67 | ↓1.002 | ↓20d | SQ | -3.0% | -27.19/-31.17 | +0.00% | 20% |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML)<br><sub>📶W9 · 🚀SS · ↓CMF2d · ⚠️TRAP</sub> | ✓ SAFE | Heavy equipment manufacturing for mining construction defense railways | 📈 BULL_ANY_MID | 20 | ↑66 | ↑0.991 | ↓5d | — | -2.0% | -21.71/-22.32 | +0.00% | 20% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>📶W9 · ↑CMF11d</sub> | ✓ SAFE | Steel and alloy wheel rims manufacturer for automobiles | 📈 BULL_ANY_MID | 0 | ↑96 | ↓1.005 | ↑23d | — | +18.3% | 43.89/42.7 | +0.00% | 20% |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 42 | 🔄52 | ↑0.992 | ↓13d | — | -5.3% | -64.43/-65.64 | +2.00% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 41 | 🔄37 | ↑1.001 | ↓19d | — | -4.4% | -53.92/-57.54 | +1.19% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 22 | ↑67 | ↑1.004 | ↓8d | — | -0.3% | -53.58/-59.08 | +0.30% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV,NSE:GAIL,NSE:TMCV,NSE:THEJO,NSE:ITC,NSE:COALINDIA,NSE:LLOYDSENGG,NSE:EIHAHOTELS,NSE:DISAQ,NSE:VRLLOG,NSE:VADILALIND,NSE:CUB,NSE:GARFIBRES,NSE:TMB,NSE:GODREJAGRO,NSE:BEML,NSE:SSWL,NSE:JSWSTEEL,NSE:BPCL,NSE:ADANIPOWER
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (12)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>📶W9 · W↑18d · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 99 | 🔄22 | ↑1.001 | ↑1d | SQ | +0.4% | -22.92/-25.88 | +0.42% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>📶W9 · 🚀SS · ↑CMF13d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↑54 | ↑1.003 | ↑1d | SQ | +0.2% | -10.03/-10.31 | +0.20% | 20% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>📶W9 · W↑17d · ↑CMF17d</sub> | ✓ SAFE | Heavy equipment manufacturing for oil gas power plants | 📈 BULL_ANY_MID | 62 | ↑90 | ↑0.996 | ↓3d | SQ | +3.0% | 6.85/6.21 | +0.00% | 20% |
| [EIHAHOTELS](https://in.tradingview.com/chart/?symbol=NSE:EIHAHOTELS)<br><sub>📶W9 · 🚀SS · ↓CMF1d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 62 | ↑30 | ↑0.992 | ↓3d | SQ | +0.2% | -21.26/-21.64 | +0.00% | 20% |
| [VRLLOG](https://in.tradingview.com/chart/?symbol=NSE:VRLLOG)<br><sub>📶W9 · ↓CMF17d</sub> | ⚠ CAUTION | Full truck load transport, LTL, bus operations, logistics | 📈 BULL_ANY_MID | 58 | ↑73 | ↓1.004 | ↑2d | SQ | +2.3% | -25.67/-26.25 | +0.00% | 20% |
| [VADILALIND](https://in.tradingview.com/chart/?symbol=NSE:VADILALIND)<br><sub>📶W9 · ↓CMF20d · ⚠️TRAP</sub> | ⚠ CAUTION | Ice cream and frozen desserts manufacturer, Indian consumer market | 📈 BULL_ANY_MID | 58 | ↑86 | ↑0.996 | ↓7d | SQ | -0.1% | -30.9/-32.06 | +0.00% | 20% |
| [CUB](https://in.tradingview.com/chart/?symbol=NSE:CUB)<br><sub>📶W9 · W↑42d · ↑CMF0d</sub> | ⚠ CAUTION | Private bank serving SMEs, MSMEs, retail customers South India | 📈 BULL_ANY_MID | 57 | ↑47 | ↓1.011 | ↑3d | SQ | +3.4% | 11.07/8.1 | +0.00% | 20% |
| [GARFIBRES](https://in.tradingview.com/chart/?symbol=NSE:GARFIBRES)<br><sub>📶W9 · ↑CMF1d · ⚠️TRAP</sub> | ⚠ CAUTION | Technical textiles and ropes for agriculture aquaculture infrastructure | 📈 BULL_ANY_MID | 45 | ↑69 | ↑0.998 | ↓23d | SQ | -4.2% | -35.54/-36.33 | +0.00% | 20% |
| [TMB](https://in.tradingview.com/chart/?symbol=NSE:TMB)<br><sub>📶W9 · ↓CMF16d · ⚠️TRAP</sub> | ⚠ CAUTION | Regional private bank serving retail agriculture MSME segments | 📈 BULL_ANY_MID | 40 | ↑88 | ↓1.001 | ↓20d | SQ | -1.7% | -38.04/-38.45 | +0.00% | 20% |
| [GODREJAGRO](https://in.tradingview.com/chart/?symbol=NSE:GODREJAGRO)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Animal feed, oil palm, crop protection for farmers | 📈 BULL_ANY_MID | 40 | ↑67 | ↓1.002 | ↓20d | SQ | -3.0% | -27.19/-31.17 | +0.00% | 20% |
| [IRMENERGY](https://in.tradingview.com/chart/?symbol=NSE:IRMENERGY)<br><sub>↓CMF30d · ⚠️TRAP · ÷DIV</sub> | ⚠ CAUTION | Natural gas distribution networks serving residential commercial industrial | 🟢 BULL_OVERSOLD | 45 | ↓37 | ↑0.983 | ↓32d | SQ | -10.6% | -60.14/-60.47 | +0.00% | 20% 🟦 |
| [SENORES](https://in.tradingview.com/chart/?symbol=NSE:SENORES)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Complex generics manufacturer specialty pharma therapies India | 🟡 BULL_OS_L2 | 54 | ↓81 | ↑0.966 | ↓11d | SQ | -5.1% | -58.8/-58.91 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ITC,NSE:COALINDIA,NSE:LLOYDSENGG,NSE:EIHAHOTELS,NSE:VRLLOG,NSE:VADILALIND,NSE:CUB,NSE:GARFIBRES,NSE:TMB,NSE:GODREJAGRO,NSE:IRMENERGY,NSE:SENORES
```

---

### 🔥 MAJOR — PPV confirmed (1)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SIGMAADV
```

### 🟢 OVERSOLD — reversal from −53/−60 (19)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>📶W9 · ↓CMF10d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 52 | 🔄56 | ↑1.002 | ↓8d | — | +1.2% | -59.19/-61.65 | +1.23% | 20% |
| [TMCV](https://in.tradingview.com/chart/?symbol=NSE:TMCV)<br><sub>📶W9 · ↑CMF17d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 45 | 🔄50 | ↑1.005 | ↓15d | — | -3.9% | -52.33/-55.73 | +1.88% | 20% |
| [THEJO](https://in.tradingview.com/chart/?symbol=NSE:THEJO)<br><sub>📶W9 · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Bulk material handling, mineral processing, corrosion protection equipment | 🟡 BULL_OS_L2 | 10 | ↑69 | ↑0.999 | ↓15d | — | -4.2% | -52.58/-55.81 | +0.00% | 20% |
| [JSWSTEEL](https://in.tradingview.com/chart/?symbol=NSE:JSWSTEEL)<br><sub>↑CMF0d · 🔥PHX</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 42 | 🔄52 | ↑0.992 | ↓13d | — | -5.3% | -64.43/-65.64 | +2.00% | 20% |
| [TIMKEN](https://in.tradingview.com/chart/?symbol=NSE:TIMKEN)<br><sub>↑CMF2d · ⚠️TRAP</sub> | ⚠ CAUTION | Tapered roller bearings manufacturing industrial motion transmission | 🟢 BULL_OVERSOLD | 14 | ↓37 | ↑0.975 | ↓11d | — | -8.7% | -61.71/-61.83 | +0.00% | 20% |
| [MEDPLUS](https://in.tradingview.com/chart/?symbol=NSE:MEDPLUS)<br><sub>↓CMF19d · ⚠️TRAP</sub> | ⚠ CAUTION | Retail pharmacy chain with diagnostic centers nationwide | 🟢 BULL_OVERSOLD | 12 | ↓10 | ↑0.971 | ↓13d | — | -8.4% | -79.35/-79.39 | +0.00% | 20% |
| [XPROINDIA](https://in.tradingview.com/chart/?symbol=NSE:XPROINDIA)<br><sub>↓CMF14d · ⚠️TRAP</sub> | ✓ SAFE | Polymer films and sheets for packaging and industrial applications | 🟢 BULL_OVERSOLD | 5 | ↓25 | ↑0.965 | ↓35d | — | -12.4% | -64.62/-66.3 | +0.00% | 20% |
| [TITAGARH](https://in.tradingview.com/chart/?symbol=NSE:TITAGARH)<br><sub>🚀SS · ↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Rail wagons coaches metro trains manufacturing | 🟢 BULL_OVERSOLD | 5 | ↓36 | ↑0.973 | ↓20d | — | -11.3% | -66.65/-67.05 | +0.00% | 20% |
| [MOSCHIP](https://in.tradingview.com/chart/?symbol=NSE:MOSCHIP)<br><sub>🚀SS · ↓CMF18d · ⚠️TRAP</sub> | ✓ SAFE | Fabless chipmaker, ASICs, mixed-signal IP for defense consumer automotive | 🟢 BULL_OVERSOLD | 5 | ↓19 | ↑0.972 | ↓23d | — | -12.4% | -66.66/-67.12 | +0.00% | 20% |
| [WINDLAS](https://in.tradingview.com/chart/?symbol=NSE:WINDLAS)<br><sub>↓CMF14d · ⚠️TRAP</sub> | ✓ SAFE | Oral solid liquid pharma formulations CDMO manufacturing | 🟢 BULL_OVERSOLD | 5 | ↓63 | ↑0.959 | ↓24d | — | -15.7% | -61.11/-61.2 | +0.00% | 20% |
| [RAMCOCEM](https://in.tradingview.com/chart/?symbol=NSE:RAMCOCEM)<br><sub>🚀SS · ↑CMF18d · ⚠️TRAP</sub> | ⚠ CAUTION | Cement producer, RMC, dry mortar for construction | 🟢 BULL_OVERSOLD | 5 | ↓15 | ↑0.978 | ↓22d | — | -9.5% | -62.87/-63.64 | +0.00% | 20% |
| [VIMTALABS](https://in.tradingview.com/chart/?symbol=NSE:VIMTALABS)<br><sub>🚀SS · ↓CMF30d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE | Contract research testing pharma biotech chemicals | 🟢 BULL_OVERSOLD | 5 | ↓38 | ↑0.949 | ↓32d | — | -20.6% | -72.65/-72.79 | +0.00% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>↑CMF1d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 41 | 🔄37 | ↑1.001 | ↓19d | — | -4.4% | -53.92/-57.54 | +1.19% | 20% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 22 | ↑67 | ↑1.004 | ↓8d | — | -0.3% | -53.58/-59.08 | +0.30% | 20% |
| [DIVGIITTS](https://in.tradingview.com/chart/?symbol=NSE:DIVGIITTS)<br><sub>🚀SS · ↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Automotive drivetrain components, transfer cases, all-terrain vehicles | 🟡 BULL_OS_L2 | 8 | ↓82 | ↑0.951 | ↓17d | — | -18.2% | -53.89/-54.56 | +0.00% | 20% |
| [JUBLFOOD](https://in.tradingview.com/chart/?symbol=NSE:JUBLFOOD)<br><sub>🚀SS · ↓CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Domino's Pizza franchise operator serving Indian quick-service restaurant market | 🟡 BULL_OS_L2 | 7 | ↓28 | ↑0.972 | ↓18d | — | -13.7% | -58.02/-58.04 | +0.00% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>↑CMF2d · ⚠️TRAP</sub> | ✓ SAFE | Complex generics and specialty formulations for global pharma | 🟡 BULL_OS_L2 | 5 | ↓50 | ↑0.975 | ↓28d | — | -16.9% | -57.05/-57.74 | +0.00% | 20% |
| [KNRCON](https://in.tradingview.com/chart/?symbol=NSE:KNRCON)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Roads highways bridges irrigation EPC contractor | 🟡 BULL_OS_L2 | 5 | ↓20 | ↑0.989 | ↓23d | — | -7.7% | -55.72/-56.5 | +0.00% | 20% |
| [SAPPHIRE](https://in.tradingview.com/chart/?symbol=NSE:SAPPHIRE)<br><sub>↓CMF16d · ⚠️TRAP</sub> | ⚠ CAUTION | KFC Pizza Hut franchisee quick service restaurants India | 🟡 BULL_OS_L2 | 5 | ↓53 | ↑0.976 | ↓24d | — | -12.1% | -54.66/-55.24 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GAIL,NSE:TMCV,NSE:THEJO,NSE:JSWSTEEL,NSE:TIMKEN,NSE:MEDPLUS,NSE:XPROINDIA,NSE:TITAGARH,NSE:MOSCHIP,NSE:WINDLAS,NSE:RAMCOCEM,NSE:VIMTALABS,NSE:BPCL,NSE:ADANIPOWER,NSE:DIVGIITTS,NSE:JUBLFOOD,NSE:RUBICON,NSE:KNRCON,NSE:SAPPHIRE
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (9)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [DISAQ](https://in.tradingview.com/chart/?symbol=NSE:DISAQ)<br><sub>📶W9 · ↓CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 59 | 🔄50 | ↑1.014 | ↑1d | — | +2.6% | -38.38/-39.62 | +2.64% | 20% |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML)<br><sub>📶W9 · 🚀SS · ↓CMF2d · ⚠️TRAP</sub> | ✓ SAFE | Heavy equipment manufacturing for mining construction defense railways | 📈 BULL_ANY_MID | 20 | ↑66 | ↑0.991 | ↓5d | — | -2.0% | -21.71/-22.32 | +0.00% | 20% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>📶W9 · ↑CMF11d</sub> | ✓ SAFE | Steel and alloy wheel rims manufacturer for automobiles | 📈 BULL_ANY_MID | 0 | ↑96 | ↓1.005 | ↑23d | — | +18.3% | 43.89/42.7 | +0.00% | 20% |
| [BUILDPRO](https://in.tradingview.com/chart/?symbol=NSE:BUILDPRO)<br><sub>↓CMF0d · ⚠️TRAP</sub> | ✓ SAFE | Building materials retail distribution southern western India | 📈 BULL_ANY_MID | 14 | ↓50 | ↑0.503 | ↓11d | — | -82.1% | -52.57/-52.95 | -6.73% | 20% |
| [JINDALSTEL](https://in.tradingview.com/chart/?symbol=NSE:JINDALSTEL)<br><sub>↓CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 8 | ↓48 | ↑0.982 | ↓17d | — | -8.9% | -51.85/-52.67 | +0.08% | 20% |
| [MFSL](https://in.tradingview.com/chart/?symbol=NSE:MFSL)<br><sub>↑CMF18d · ⚠️TRAP</sub> | ✓ SAFE | Life insurance distribution and investment holding company | 📈 BULL_ANY_MID | 5 | ↓18 | ↑0.979 | ↓24d | — | -13.9% | -52.2/-52.37 | +0.00% | 20% |
| [DATAPATTNS](https://in.tradingview.com/chart/?symbol=NSE:DATAPATTNS)<br><sub>↓CMF10d · ⚠️TRAP</sub> | ✓ SAFE | Defense aerospace electronics systems manufacturer for military platforms | 📈 BULL_ANY_MID | 5 | ↓78 | ↑0.985 | ↓31d | — | -11.7% | -51.59/-51.86 | +0.00% | 20% |
| [NEPHROPLUS](https://in.tradingview.com/chart/?symbol=NSE:NEPHROPLUS)<br><sub>↓CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Dialysis clinics network serving kidney failure patients India | 📈 BULL_ANY_MID | 5 | ↓50 | ↑0.981 | ↓33d | — | -11.1% | -41.35/-41.48 | +0.00% | 20% |
| [TSFINV](https://in.tradingview.com/chart/?symbol=NSE:TSFINV)<br><sub>🚀SS · ↓CMF8d · ⚠️TRAP</sub> | ⚠ CAUTION | NBFC lending and investment financing services | 📈 BULL_ANY_MID | 5 | ↓29 | ↑0.986 | ↓31d | — | -1.5% | -30.63/-31.48 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:DISAQ,NSE:BEML,NSE:SSWL,NSE:BUILDPRO,NSE:JINDALSTEL,NSE:MFSL,NSE:DATAPATTNS,NSE:NEPHROPLUS,NSE:TSFINV
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
