> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-09-14
*Generated 2026-09-14 15:45 IST*

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

**Total bull crosses today: 41** · 11 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MAXHEALTH,NSE:INDUSTOWER,NSE:SIGMAADV,NSE:HINDALCO,NSE:MMFL,NSE:TORNTPHARM,NSE:AETHER,NSE:AKUMS,NSE:PRUDENT,NSE:FINKURVE,NSE:HINDZINC,NSE:ADANIENT,NSE:BOSCHLTD,NSE:RPEL,NSE:SJS,NSE:SEDEMAC,NSE:MEESHO,NSE:CUMMINSIND,NSE:TATACHEM,NSE:INDIAMART,NSE:IGIL,NSE:PATANJALI,NSE:ROSSARI,NSE:LUPIN,NSE:UBL,NSE:DEEPAKFERT,NSE:PACEDIGITK,NSE:CAPILLARY,NSE:VSTTILLERS,NSE:BSOFT,NSE:ABBOTINDIA,NSE:PICCADIL,NSE:IGARASHI,NSE:RELTD,NSE:SUNFLAG,NSE:SATIN,NSE:RAMCOIND,NSE:MANAPPURAM,NSE:JBMA,NSE:LLOYDSENGG,NSE:IFBIND
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (17)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MAXHEALTH](https://in.tradingview.com/chart/?symbol=NSE:MAXHEALTH)<br><sub>📶W9 · ↑CMF9d</sub> | ⚠ CAUTION | Tertiary quaternary hospital network Delhi NCR North India | ⚡ BULL_ANY_PPV | 89 | 🔄36 | ↑1.030 | ↑1d | SQ·PV | +4.5% | -32.15/-41.06 | +4.48% | 20% |
| [INDUSTOWER](https://in.tradingview.com/chart/?symbol=NSE:INDUSTOWER)<br><sub>📶W9 · W↑5d · ↑CMF8d</sub> | ✓ SAFE | Telecom tower infrastructure operator serving mobile networks | ⚡ BULL_ANY_PPV | 54 | 🔄32 | ↑1.025 | ↑1d | PV | +4.3% | -30.53/-37.66 | +4.30% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 91 | 🔄61 | ↑1.003 | ↓9d | SQ | -0.3% | -18.92/-20.04 | +1.17% | 20% |
| [MMFL](https://in.tradingview.com/chart/?symbol=NSE:MMFL)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Steel forging components for vehicles and machinery | 📈 BULL_ANY_MID | 62 | ↑91 | ↑1.000 | ↓3d | SQ | +2.4% | 9.2/8.01 | +0.00% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑67 | ↓0.997 | ↓2d | SQ | +0.2% | -3.46/-4.79 | -0.71% | 20% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Specialty chemicals for pharma, agro, materials | 📈 BULL_ANY_MID | 58 | ↑94 | ↓1.014 | ↑2d | SQ | +2.1% | 17.35/14.98 | +0.00% | 20% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Pharma CDMO formulations development manufacturing domestic international markets | 📈 BULL_ANY_MID | 58 | ↑90 | ↓1.019 | ↑2d | SQ | +3.6% | 17.56/15.78 | +0.00% | 20% |
| [PRUDENT](https://in.tradingview.com/chart/?symbol=NSE:PRUDENT)<br><sub>📶W9 · ↓CMF11d</sub> | ⚠ CAUTION | Retail wealth manager distributing mutual funds insurance brokerage | 📈 BULL_ANY_MID | 58 | ↑75 | ↓1.009 | ↑2d | SQ | +2.0% | 6.7/5.77 | +0.00% | 20% |
| [FINKURVE](https://in.tradingview.com/chart/?symbol=NSE:FINKURVE)<br><sub>📶W9 · W↑26d · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.022 | ↑2d | SQ | +8.6% | -7.79/-9.19 | +0.00% | 20% |
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>📶W9 · W↑28d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 28 | ↑64 | ↑1.014 | ↑2d | — | +2.7% | 24.78/23.85 | +1.56% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · ↓CMF7d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 19 | ↑76 | ↑1.039 | ↑1d | — | +5.1% | -9.05/-16.39 | +5.11% | 20% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>📶W9 · W↑109d · ↑CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 17 | ↑78 | ↓1.015 | ↑3d | — | +4.4% | 32.49/29.43 | +0.17% | 20% |
| [RPEL](https://in.tradingview.com/chart/?symbol=NSE:RPEL)<br><sub>📶W9 · W↑26d · ↑CMF22d</sub> | ✓ SAFE | Silica ramming mass manufacturer for induction furnaces | 📈 BULL_ANY_MID | 17 | ↑98 | ↓1.048 | ↑3d | — | +10.4% | 46.34/44.49 | +0.00% | 20% |
| [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS)<br><sub>📶W9 · ↓CMF16d</sub> | ✓ SAFE | Decorative graphics manufacturing for automotive consumer electronics appliances | 📈 BULL_ANY_MID | 12 | ↑81 | ↑0.996 | ↓13d | — | -5.3% | -31.22/-32.55 | +0.00% | 20% |
| [SEDEMAC](https://in.tradingview.com/chart/?symbol=NSE:SEDEMAC)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE | Engine control electronics for automotive and off-highway vehicles | 📈 BULL_ANY_MID | 7 | ↑50 | ↓0.999 | ↓13d | — | -4.9% | -19.71/-21.04 | -0.50% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · 🚀SS · ↑CMF29d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 0 | ↑50 | ↑1.036 | ↑24d | — | +16.7% | 57.53/55.6 | +3.13% | 20% 🟦 |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MAXHEALTH,NSE:INDUSTOWER,NSE:SIGMAADV,NSE:HINDALCO,NSE:MMFL,NSE:TORNTPHARM,NSE:AETHER,NSE:AKUMS,NSE:PRUDENT,NSE:FINKURVE,NSE:HINDZINC,NSE:ADANIENT,NSE:BOSCHLTD,NSE:RPEL,NSE:SJS,NSE:SEDEMAC,NSE:MEESHO
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (28)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MAXHEALTH](https://in.tradingview.com/chart/?symbol=NSE:MAXHEALTH)<br><sub>📶W9 · ↑CMF9d</sub> | ⚠ CAUTION | Tertiary quaternary hospital network Delhi NCR North India | ⚡ BULL_ANY_PPV | 89 | 🔄36 | ↑1.030 | ↑1d | SQ·PV | +4.5% | -32.15/-41.06 | +4.48% | 20% |
| [INDUSTOWER](https://in.tradingview.com/chart/?symbol=NSE:INDUSTOWER)<br><sub>📶W9 · W↑5d · ↑CMF8d</sub> | ✓ SAFE | Telecom tower infrastructure operator serving mobile networks | ⚡ BULL_ANY_PPV | 54 | 🔄32 | ↑1.025 | ↑1d | PV | +4.3% | -30.53/-37.66 | +4.30% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 91 | 🔄61 | ↑1.003 | ↓9d | SQ | -0.3% | -18.92/-20.04 | +1.17% | 20% |
| [MMFL](https://in.tradingview.com/chart/?symbol=NSE:MMFL)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Steel forging components for vehicles and machinery | 📈 BULL_ANY_MID | 62 | ↑91 | ↑1.000 | ↓3d | SQ | +2.4% | 9.2/8.01 | +0.00% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑67 | ↓0.997 | ↓2d | SQ | +0.2% | -3.46/-4.79 | -0.71% | 20% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Specialty chemicals for pharma, agro, materials | 📈 BULL_ANY_MID | 58 | ↑94 | ↓1.014 | ↑2d | SQ | +2.1% | 17.35/14.98 | +0.00% | 20% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Pharma CDMO formulations development manufacturing domestic international markets | 📈 BULL_ANY_MID | 58 | ↑90 | ↓1.019 | ↑2d | SQ | +3.6% | 17.56/15.78 | +0.00% | 20% |
| [PRUDENT](https://in.tradingview.com/chart/?symbol=NSE:PRUDENT)<br><sub>📶W9 · ↓CMF11d</sub> | ⚠ CAUTION | Retail wealth manager distributing mutual funds insurance brokerage | 📈 BULL_ANY_MID | 58 | ↑75 | ↓1.009 | ↑2d | SQ | +2.0% | 6.7/5.77 | +0.00% | 20% |
| [FINKURVE](https://in.tradingview.com/chart/?symbol=NSE:FINKURVE)<br><sub>📶W9 · W↑26d · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.022 | ↑2d | SQ | +8.6% | -7.79/-9.19 | +0.00% | 20% |
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>📶W9 · W↑28d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 28 | ↑64 | ↑1.014 | ↑2d | — | +2.7% | 24.78/23.85 | +1.56% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · ↓CMF7d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 19 | ↑76 | ↑1.039 | ↑1d | — | +5.1% | -9.05/-16.39 | +5.11% | 20% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>📶W9 · W↑109d · ↑CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 17 | ↑78 | ↓1.015 | ↑3d | — | +4.4% | 32.49/29.43 | +0.17% | 20% |
| [RPEL](https://in.tradingview.com/chart/?symbol=NSE:RPEL)<br><sub>📶W9 · W↑26d · ↑CMF22d</sub> | ✓ SAFE | Silica ramming mass manufacturer for induction furnaces | 📈 BULL_ANY_MID | 17 | ↑98 | ↓1.048 | ↑3d | — | +10.4% | 46.34/44.49 | +0.00% | 20% |
| [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS)<br><sub>📶W9 · ↓CMF16d</sub> | ✓ SAFE | Decorative graphics manufacturing for automotive consumer electronics appliances | 📈 BULL_ANY_MID | 12 | ↑81 | ↑0.996 | ↓13d | — | -5.3% | -31.22/-32.55 | +0.00% | 20% |
| [SEDEMAC](https://in.tradingview.com/chart/?symbol=NSE:SEDEMAC)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE | Engine control electronics for automotive and off-highway vehicles | 📈 BULL_ANY_MID | 7 | ↑50 | ↓0.999 | ↓13d | — | -4.9% | -19.71/-21.04 | -0.50% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · 🚀SS · ↑CMF29d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 0 | ↑50 | ↑1.036 | ↑24d | — | +16.7% | 57.53/55.6 | +3.13% | 20% 🟦 |
| [CUMMINSIND](https://in.tradingview.com/chart/?symbol=NSE:CUMMINSIND)<br><sub>↑CMF1d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 59 | 🔄53 | ↑1.012 | ↑1d | — | +2.7% | -56.42/-62.44 | +2.68% | 20% |
| [INDIAMART](https://in.tradingview.com/chart/?symbol=NSE:INDIAMART)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | B2B marketplace connecting MSMEs to suppliers digitally | 🟢 BULL_OVERSOLD | 13 | ↑5 | ↑0.997 | ↓12d | — | -3.4% | -68.39/-68.89 | +0.00% | 20% |
| [PATANJALI](https://in.tradingview.com/chart/?symbol=NSE:PATANJALI)<br><sub>W↑31d · ↑CMF23d · ⚠️TRAP</sub> | ✓ SAFE | Edible oils, soybean processing, consumer cooking oil products | 🟢 BULL_OVERSOLD | 10 | ↑2 | ↑0.996 | ↓15d | — | -2.6% | -62.66/-63.3 | +0.00% | 20% |
| [ABBOTINDIA](https://in.tradingview.com/chart/?symbol=NSE:ABBOTINDIA)<br><sub>↓CMF19d · ⚠️TRAP</sub> | ⚠ CAUTION | Pharmaceuticals and nutritional products for Indian healthcare markets | 🟡 BULL_OS_L2 | 5 | ↑29 | ↑0.994 | ↓25d | — | -7.2% | -58.96/-59.07 | +0.00% | 20% |
| [IGARASHI](https://in.tradingview.com/chart/?symbol=NSE:IGARASHI)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | DC motors manufacturing for global automotive sector | 🟡 BULL_OS_L2 | 5 | ↑51 | ↑0.995 | ↓31d | — | -8.2% | -53.53/-54.2 | +0.00% | 20% |
| [RELTD](https://in.tradingview.com/chart/?symbol=NSE:RELTD)<br><sub>↓CMF23d · ⚠️TRAP</sub> | ⚠ CAUTION | Solar power plants, EV charging, sugar trading conglomerate | 📈 BULL_ANY_MID | 58 | ↑52 | ↑0.996 | ↓7d | SQ | -2.2% | -48.18/-48.7 | +0.00% | 20% |
| [SATIN](https://in.tradingview.com/chart/?symbol=NSE:SATIN)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Microfinance loans for rural underserved borrowers | 📈 BULL_ANY_MID | 45 | ↑75 | ↑0.993 | ↓37d | SQ | -15.4% | -48.75/-51.16 | +0.00% | 20% |
| [RAMCOIND](https://in.tradingview.com/chart/?symbol=NSE:RAMCOIND)<br><sub>↓CMF5d · ⚠️TRAP</sub> | ✓ SAFE | Fiber cement boards, calcium silicate boards, cotton yarn manufacturer | 📈 BULL_ANY_MID | 11 | ↑54 | ↑0.994 | ↓14d | — | -7.6% | -48.82/-49.62 | +0.00% | 20% |
| [JBMA](https://in.tradingview.com/chart/?symbol=NSE:JBMA)<br><sub>↑CMF16d · ⚠️TRAP</sub> | ✓ SAFE | Commercial buses, EV components, sheet metal tooling systems | 📈 BULL_ANY_MID | 8 | ↑45 | ↑1.000 | ↓17d | — | -0.5% | -46.35/-47.46 | +0.00% | 20% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>↓CMF6d · ⚠️TRAP</sub> | ✓ SAFE | Heavy equipment manufacturing for oil gas power plants | 📈 BULL_ANY_MID | 5 | ↑82 | ↑0.994 | ↓20d | — | -9.3% | -52.47/-52.56 | +0.00% | 20% |
| [IFBIND](https://in.tradingview.com/chart/?symbol=NSE:IFBIND)<br><sub>↓CMF10d · ⚠️TRAP</sub> | ✓ SAFE | Washing machines, dryers, automotive parts, engineering | 📈 BULL_ANY_MID | 5 | ↑43 | ↑0.997 | ↓23d | — | -4.2% | -44.6/-44.71 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MAXHEALTH,NSE:INDUSTOWER,NSE:SIGMAADV,NSE:HINDALCO,NSE:MMFL,NSE:TORNTPHARM,NSE:AETHER,NSE:AKUMS,NSE:PRUDENT,NSE:FINKURVE,NSE:HINDZINC,NSE:ADANIENT,NSE:BOSCHLTD,NSE:RPEL,NSE:SJS,NSE:SEDEMAC,NSE:MEESHO,NSE:CUMMINSIND,NSE:INDIAMART,NSE:PATANJALI,NSE:ABBOTINDIA,NSE:IGARASHI,NSE:RELTD,NSE:SATIN,NSE:RAMCOIND,NSE:JBMA,NSE:LLOYDSENGG,NSE:IFBIND
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (11)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MAXHEALTH](https://in.tradingview.com/chart/?symbol=NSE:MAXHEALTH)<br><sub>📶W9 · ↑CMF9d</sub> | ⚠ CAUTION | Tertiary quaternary hospital network Delhi NCR North India | ⚡ BULL_ANY_PPV | 89 | 🔄36 | ↑1.030 | ↑1d | SQ·PV | +4.5% | -32.15/-41.06 | +4.48% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 91 | 🔄61 | ↑1.003 | ↓9d | SQ | -0.3% | -18.92/-20.04 | +1.17% | 20% |
| [MMFL](https://in.tradingview.com/chart/?symbol=NSE:MMFL)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Steel forging components for vehicles and machinery | 📈 BULL_ANY_MID | 62 | ↑91 | ↑1.000 | ↓3d | SQ | +2.4% | 9.2/8.01 | +0.00% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑67 | ↓0.997 | ↓2d | SQ | +0.2% | -3.46/-4.79 | -0.71% | 20% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>📶W9 · ↑CMF2d</sub> | ✓ SAFE | Specialty chemicals for pharma, agro, materials | 📈 BULL_ANY_MID | 58 | ↑94 | ↓1.014 | ↑2d | SQ | +2.1% | 17.35/14.98 | +0.00% | 20% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | Pharma CDMO formulations development manufacturing domestic international markets | 📈 BULL_ANY_MID | 58 | ↑90 | ↓1.019 | ↑2d | SQ | +3.6% | 17.56/15.78 | +0.00% | 20% |
| [PRUDENT](https://in.tradingview.com/chart/?symbol=NSE:PRUDENT)<br><sub>📶W9 · ↓CMF11d</sub> | ⚠ CAUTION | Retail wealth manager distributing mutual funds insurance brokerage | 📈 BULL_ANY_MID | 58 | ↑75 | ↓1.009 | ↑2d | SQ | +2.0% | 6.7/5.77 | +0.00% | 20% |
| [FINKURVE](https://in.tradingview.com/chart/?symbol=NSE:FINKURVE)<br><sub>📶W9 · W↑26d · ↑CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 58 | ↑50 | ↓1.022 | ↑2d | SQ | +8.6% | -7.79/-9.19 | +0.00% | 20% |
| [RELTD](https://in.tradingview.com/chart/?symbol=NSE:RELTD)<br><sub>↓CMF23d · ⚠️TRAP</sub> | ⚠ CAUTION | Solar power plants, EV charging, sugar trading conglomerate | 📈 BULL_ANY_MID | 58 | ↑52 | ↑0.996 | ↓7d | SQ | -2.2% | -48.18/-48.7 | +0.00% | 20% |
| [SUNFLAG](https://in.tradingview.com/chart/?symbol=NSE:SUNFLAG)<br><sub>↓CMF19d · ⚠️TRAP</sub> | ✓ SAFE | Alloy steel producer serving automotive and engineering industries | 📈 BULL_ANY_MID | 45 | ↓71 | ↑0.990 | ↓41d | SQ | -2.2% | -43.58/-44.36 | +0.00% | 10% 🟨 |
| [SATIN](https://in.tradingview.com/chart/?symbol=NSE:SATIN)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Microfinance loans for rural underserved borrowers | 📈 BULL_ANY_MID | 45 | ↑75 | ↑0.993 | ↓37d | SQ | -15.4% | -48.75/-51.16 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MAXHEALTH,NSE:HINDALCO,NSE:MMFL,NSE:TORNTPHARM,NSE:AETHER,NSE:AKUMS,NSE:PRUDENT,NSE:FINKURVE,NSE:RELTD,NSE:SUNFLAG,NSE:SATIN
```

---

### 🔥 MAJOR — PPV confirmed (2)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [INDUSTOWER](https://in.tradingview.com/chart/?symbol=NSE:INDUSTOWER)<br><sub>📶W9 · W↑5d · ↑CMF8d</sub> | ✓ SAFE | Telecom tower infrastructure operator serving mobile networks | ⚡ BULL_ANY_PPV | 54 | 🔄32 | ↑1.025 | ↑1d | PV | +4.3% | -30.53/-37.66 | +4.30% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:INDUSTOWER,NSE:SIGMAADV
```

### 🟢 OVERSOLD — reversal from −53/−60 (16)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CUMMINSIND](https://in.tradingview.com/chart/?symbol=NSE:CUMMINSIND)<br><sub>↑CMF1d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 59 | 🔄53 | ↑1.012 | ↑1d | — | +2.7% | -56.42/-62.44 | +2.68% | 20% |
| [TATACHEM](https://in.tradingview.com/chart/?symbol=NSE:TATACHEM)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Soda ash alkali chemicals specialty products manufacturer global | 🟢 BULL_OVERSOLD | 13 | ↓9 | ↑0.990 | ↓12d | — | -4.9% | -61.3/-62.9 | +0.00% | 20% |
| [INDIAMART](https://in.tradingview.com/chart/?symbol=NSE:INDIAMART)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | B2B marketplace connecting MSMEs to suppliers digitally | 🟢 BULL_OVERSOLD | 13 | ↑5 | ↑0.997 | ↓12d | — | -3.4% | -68.39/-68.89 | +0.00% | 20% |
| [IGIL](https://in.tradingview.com/chart/?symbol=NSE:IGIL)<br><sub>↓CMF11d · ⚠️TRAP</sub> | ✓ SAFE | Diamond gemstone jewelry certification grading India global | 🟢 BULL_OVERSOLD | 11 | ↓28 | ↑0.981 | ↓14d | — | -8.6% | -66.52/-67.07 | +0.00% | 20% |
| [PATANJALI](https://in.tradingview.com/chart/?symbol=NSE:PATANJALI)<br><sub>W↑31d · ↑CMF23d · ⚠️TRAP</sub> | ✓ SAFE | Edible oils, soybean processing, consumer cooking oil products | 🟢 BULL_OVERSOLD | 10 | ↑2 | ↑0.996 | ↓15d | — | -2.6% | -62.66/-63.3 | +0.00% | 20% |
| [ROSSARI](https://in.tradingview.com/chart/?symbol=NSE:ROSSARI)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Specialty chemicals for textiles, home care, personal care | 🟢 BULL_OVERSOLD | 7 | ↓12 | ↑0.972 | ↓18d | — | -10.1% | -70.44/-70.95 | +0.00% | 20% |
| [LUPIN](https://in.tradingview.com/chart/?symbol=NSE:LUPIN)<br><sub>↓CMF16d · ⚠️TRAP</sub> | ✓ SAFE | Branded generics, APIs, biotechnology for global pharma markets | 🟢 BULL_OVERSOLD | 5 | ↓36 | ↑0.990 | ↓33d | — | -12.6% | -59.86/-60.86 | +0.00% | 20% |
| [UBL](https://in.tradingview.com/chart/?symbol=NSE:UBL)<br><sub>↓CMF30d · ⚠️TRAP · DEL93%</sub> | ⚠ CAUTION | Beer manufacturer, India domestic market, Kingfisher brand leader | 🟢 BULL_OVERSOLD | 5 | ↓12 | ↑0.984 | ↓41d | — | -6.2% | -63.57/-63.62 | +0.00% | 20% |
| [DEEPAKFERT](https://in.tradingview.com/chart/?symbol=NSE:DEEPAKFERT)<br><sub>🚀SS · ↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Fertilizers, bulk chemicals, mining solutions for agriculture | 🟢 BULL_OVERSOLD | 5 | ↓45 | ↑0.972 | ↓30d | — | -16.2% | -64.94/-65.07 | +0.00% | 20% |
| [PACEDIGITK](https://in.tradingview.com/chart/?symbol=NSE:PACEDIGITK)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Telecom fiber networks, power systems, energy infrastructure solutions | 🟢 BULL_OVERSOLD | 5 | ↓50 | ↑0.971 | ↓33d | — | -19.9% | -64.4/-64.56 | +0.00% | 20% |
| [CAPILLARY](https://in.tradingview.com/chart/?symbol=NSE:CAPILLARY)<br><sub>↓CMF16d · ⚠️TRAP</sub> | ✓ SAFE | AI loyalty platform SaaS for retail enterprises | 🟢 BULL_OVERSOLD | 5 | ↓50 | ↑0.978 | ↓25d | — | -11.7% | -60.94/-61.09 | +0.00% | 20% |
| [VSTTILLERS](https://in.tradingview.com/chart/?symbol=NSE:VSTTILLERS)<br><sub>🚀SS · ↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Power tillers and compact tractors for Indian farmers | 🟢 BULL_OVERSOLD | 5 | ↓10 | ↑0.978 | ↓23d | — | -9.0% | -65.0/-65.02 | +0.00% | 20% |
| [BSOFT](https://in.tradingview.com/chart/?symbol=NSE:BSOFT)<br><sub>↓CMF27d · ⚠️TRAP</sub> | ✓ SAFE | IT services, digital transformation, cloud computing consulting | 🟡 BULL_OS_L2 | 5 | ↓7 | ↑0.990 | ↓36d | — | -0.3% | -56.2/-56.78 | +0.00% | 20% |
| [ABBOTINDIA](https://in.tradingview.com/chart/?symbol=NSE:ABBOTINDIA)<br><sub>↓CMF19d · ⚠️TRAP</sub> | ⚠ CAUTION | Pharmaceuticals and nutritional products for Indian healthcare markets | 🟡 BULL_OS_L2 | 5 | ↑29 | ↑0.994 | ↓25d | — | -7.2% | -58.96/-59.07 | +0.00% | 20% |
| [PICCADIL](https://in.tradingview.com/chart/?symbol=NSE:PICCADIL)<br><sub>↓CMF10d · ⚠️TRAP</sub> | ✓ SAFE | Sugar production and premium alcoholic spirits distillery | 🟡 BULL_OS_L2 | 5 | ↓45 | ↑0.978 | ↓32d | — | -16.3% | -52.96/-53.35 | +0.00% | 20% |
| [IGARASHI](https://in.tradingview.com/chart/?symbol=NSE:IGARASHI)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | DC motors manufacturing for global automotive sector | 🟡 BULL_OS_L2 | 5 | ↑51 | ↑0.995 | ↓31d | — | -8.2% | -53.53/-54.2 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CUMMINSIND,NSE:TATACHEM,NSE:INDIAMART,NSE:IGIL,NSE:PATANJALI,NSE:ROSSARI,NSE:LUPIN,NSE:UBL,NSE:DEEPAKFERT,NSE:PACEDIGITK,NSE:CAPILLARY,NSE:VSTTILLERS,NSE:BSOFT,NSE:ABBOTINDIA,NSE:PICCADIL,NSE:IGARASHI
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (12)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>📶W9 · W↑28d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 28 | ↑64 | ↑1.014 | ↑2d | — | +2.7% | 24.78/23.85 | +1.56% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · ↓CMF7d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 19 | ↑76 | ↑1.039 | ↑1d | — | +5.1% | -9.05/-16.39 | +5.11% | 20% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>📶W9 · W↑109d · ↑CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 17 | ↑78 | ↓1.015 | ↑3d | — | +4.4% | 32.49/29.43 | +0.17% | 20% |
| [RPEL](https://in.tradingview.com/chart/?symbol=NSE:RPEL)<br><sub>📶W9 · W↑26d · ↑CMF22d</sub> | ✓ SAFE | Silica ramming mass manufacturer for induction furnaces | 📈 BULL_ANY_MID | 17 | ↑98 | ↓1.048 | ↑3d | — | +10.4% | 46.34/44.49 | +0.00% | 20% |
| [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS)<br><sub>📶W9 · ↓CMF16d</sub> | ✓ SAFE | Decorative graphics manufacturing for automotive consumer electronics appliances | 📈 BULL_ANY_MID | 12 | ↑81 | ↑0.996 | ↓13d | — | -5.3% | -31.22/-32.55 | +0.00% | 20% |
| [SEDEMAC](https://in.tradingview.com/chart/?symbol=NSE:SEDEMAC)<br><sub>📶W9 · ↓CMF8d</sub> | ✓ SAFE | Engine control electronics for automotive and off-highway vehicles | 📈 BULL_ANY_MID | 7 | ↑50 | ↓0.999 | ↓13d | — | -4.9% | -19.71/-21.04 | -0.50% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · 🚀SS · ↑CMF29d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 0 | ↑50 | ↑1.036 | ↑24d | — | +16.7% | 57.53/55.6 | +3.13% | 20% 🟦 |
| [RAMCOIND](https://in.tradingview.com/chart/?symbol=NSE:RAMCOIND)<br><sub>↓CMF5d · ⚠️TRAP</sub> | ✓ SAFE | Fiber cement boards, calcium silicate boards, cotton yarn manufacturer | 📈 BULL_ANY_MID | 11 | ↑54 | ↑0.994 | ↓14d | — | -7.6% | -48.82/-49.62 | +0.00% | 20% |
| [MANAPPURAM](https://in.tradingview.com/chart/?symbol=NSE:MANAPPURAM)<br><sub>↓CMF0d · ⚠️TRAP</sub> | ✓ SAFE | Gold loans, NBFC, retail credit, unbanked customers | 📈 BULL_ANY_MID | 8 | ↓61 | ↑0.989 | ↓17d | — | -5.8% | -41.67/-41.86 | +0.00% | 20% |
| [JBMA](https://in.tradingview.com/chart/?symbol=NSE:JBMA)<br><sub>↑CMF16d · ⚠️TRAP</sub> | ✓ SAFE | Commercial buses, EV components, sheet metal tooling systems | 📈 BULL_ANY_MID | 8 | ↑45 | ↑1.000 | ↓17d | — | -0.5% | -46.35/-47.46 | +0.00% | 20% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>↓CMF6d · ⚠️TRAP</sub> | ✓ SAFE | Heavy equipment manufacturing for oil gas power plants | 📈 BULL_ANY_MID | 5 | ↑82 | ↑0.994 | ↓20d | — | -9.3% | -52.47/-52.56 | +0.00% | 20% |
| [IFBIND](https://in.tradingview.com/chart/?symbol=NSE:IFBIND)<br><sub>↓CMF10d · ⚠️TRAP</sub> | ✓ SAFE | Washing machines, dryers, automotive parts, engineering | 📈 BULL_ANY_MID | 5 | ↑43 | ↑0.997 | ↓23d | — | -4.2% | -44.6/-44.71 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:HINDZINC,NSE:ADANIENT,NSE:BOSCHLTD,NSE:RPEL,NSE:SJS,NSE:SEDEMAC,NSE:MEESHO,NSE:RAMCOIND,NSE:MANAPPURAM,NSE:JBMA,NSE:LLOYDSENGG,NSE:IFBIND
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
