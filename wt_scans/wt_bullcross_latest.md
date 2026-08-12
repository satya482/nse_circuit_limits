> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-08-12
*Generated 2026-08-12 15:49 IST*

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

**Total bull crosses today: 43** · 17 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:TIIL,NSE:PFIZER,NSE:CNL,NSE:FIVESTAR,NSE:MANALIPETC,NSE:IKIO,NSE:HEXT,NSE:CORONA,NSE:FINOPB,NSE:OFSS,NSE:TTKHLTCARE,NSE:QPOWER,NSE:GOKULAGRO,NSE:ABBOTINDIA,NSE:KRN,NSE:QUESS,NSE:ESCORTS,NSE:NESTLEIND,NSE:LENSKART,NSE:NILKAMAL,NSE:SKIPPER,NSE:JUBLCPL,NSE:INDOTHAI,NSE:HUBTOWN,NSE:BBL,NSE:LICHSGFIN,NSE:VBL,NSE:TIPSMUSIC,NSE:GPTINFRA,NSE:GODREJCP,NSE:IGL,NSE:MAHABANK,NSE:SPLPETRO,NSE:MFSL,NSE:IPCALAB,NSE:SAATVIKGL,NSE:GUJENERGY,NSE:IIFLCAPS,NSE:CCL,NSE:SIGNPOST,NSE:ADANIPORTS,NSE:NUVAMA,NSE:JNKINDIA
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (20)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [TIIL](https://in.tradingview.com/chart/?symbol=NSE:TIIL)<br><sub>📶W9 · W↑18d · 🚀SS·18x · ↑CMF0d</sub> | ✓ SAFE | Drum closures, scaffolding systems, textiles manufacturing | ⚡ BULL_ANY_PPV | 40 | 🔄63 | ↑1.078 | ↑10d | PV | +13.1% | 56.15/49.59 | +10.33% | 20% |
| [PFIZER](https://in.tradingview.com/chart/?symbol=NSE:PFIZER)<br><sub>📶W9 · W↑28d · ↑CMF12d</sub> | ⚠ CAUTION | Pharmaceutical manufacturing, vaccines, oncology drugs, India operations | ⚡ BULL_ANY_PPV | 8 | ↑43 | ↑1.028 | ↑17d | PV | +9.6% | 59.86/56.98 | +2.43% | 20% |
| [CNL](https://in.tradingview.com/chart/?symbol=NSE:CNL)<br><sub>📶W9 · W↑82d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | IT and lifestyle products distributor for retailers | ⚡ BULL_ANY_PPV | 0 | ↑97 | ↑1.107 | ↑48d | PV | +91.4% | 71.37/70.09 | +8.22% | 20% |
| [FIVESTAR](https://in.tradingview.com/chart/?symbol=NSE:FIVESTAR)<br><sub>📶W9 · W↑43d · ↑CMF0d</sub> | ✓ SAFE | Secured business loans for micro-entrepreneurs south india | 📈 BULL_ANY_MID | 99 | 🔄60 | ↑1.009 | ↑1d | SQ | +1.5% | 8.4/7.28 | +1.49% | 20% |
| [MANALIPETC](https://in.tradingview.com/chart/?symbol=NSE:MANALIPETC)<br><sub>📶W9 · W↑18d · ↓CMF11d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 93 | 🔄59 | ↑1.026 | ↑2d | SQ | +4.7% | 20.46/15.16 | +2.84% | 20% |
| [IKIO](https://in.tradingview.com/chart/?symbol=NSE:IKIO)<br><sub>📶W9 · W↑91d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | LED lighting ODM, precision electronics, India domestic commercial | 📈 BULL_ANY_MID | 89 | 🔄79 | ↑1.049 | ↑1d | SQ | +5.5% | 2.76/-5.84 | +5.53% | 20% |
| [HEXT](https://in.tradingview.com/chart/?symbol=NSE:HEXT)<br><sub>📶W9 · W↑94d · ↑CMF3d</sub> | ✓ SAFE | IT Services, Digital Transformation, Automation Solutions, Global Enterprises | 📈 BULL_ANY_MID | 69 | ↓37 | ↑1.002 | ↑1d | SQ | +0.3% | 15.29/15.25 | +0.32% | 20% |
| [CORONA](https://in.tradingview.com/chart/?symbol=NSE:CORONA)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Pharma formulations women's health cardiology pain management domestic | 📈 BULL_ANY_MID | 63 | ↑50 | ↑1.016 | ↑2d | SQ | +2.3% | 32.33/31.37 | +0.55% | 20% |
| [FINOPB](https://in.tradingview.com/chart/?symbol=NSE:FINOPB)<br><sub>📶W9 · W↑86d · ↑CMF30d</sub> | ✓ SAFE | Digital payments bank serving underbanked India populations | 📈 BULL_ANY_MID | 58 | ↓26 | ↓1.000 | ↓2d | SQ | +1.8% | -10.8/-12.49 | -1.24% | 20% 🟦 |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄83 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [TTKHLTCARE](https://in.tradingview.com/chart/?symbol=NSE:TTKHLTCARE)<br><sub>📶W9 · W↑91d · ↓CMF20d</sub> | ✓ SAFE | Pharmaceuticals, medical devices, consumer healthcare products India | 📈 BULL_ANY_MID | 51 | ↑61 | ↑1.034 | ↑9d | SQ | +10.2% | 55.08/53.55 | +1.67% | 20% |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER)<br><sub>📶W9 · 🚀SS · ↓CMF1d · DEL61%</sub> | ✓ SAFE | High-voltage electrical equipment manufacturer for power infrastructure | 📈 BULL_ANY_MID | 48 | 🔄98 | ↑1.071 | ↑2d | — | +22.9% | 1.99/-2.65 | +4.45% | 5% 🟥 |
| [GOKULAGRO](https://in.tradingview.com/chart/?symbol=NSE:GOKULAGRO)<br><sub>📶W9 · W↑8d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Edible oils refining, palm soybean sunflower processing, food sector | 📈 BULL_ANY_MID | 39 | 🔄77 | ↑1.042 | ↑11d | — | +12.2% | 39.58/36.32 | +4.68% | 20% |
| [ABBOTINDIA](https://in.tradingview.com/chart/?symbol=NSE:ABBOTINDIA)<br><sub>📶W9 · W↑28d · ↑CMF21d</sub> | ⚠ CAUTION | Pharmaceuticals, diagnostics, nutritional products for India healthcare | 📈 BULL_ANY_MID | 28 | ↑34 | ↑1.009 | ↑2d | — | +2.2% | 15.16/9.85 | +0.43% | 20% |
| [KRN](https://in.tradingview.com/chart/?symbol=NSE:KRN)<br><sub>📶W9 · W↑2d · 🚀SS · ↓CMF2d · DEL57%</sub> | ✓ SAFE | Precision heat exchangers for HVAC refrigeration equipment makers | 📈 BULL_ANY_MID | 18 | ↑94 | ↑1.080 | ↑2d | — | +21.7% | 16.1/9.95 | +3.43% | 5% |
| [QUESS](https://in.tradingview.com/chart/?symbol=NSE:QUESS)<br><sub>📶W9 · W↑91d · ↑CMF30d</sub> | ✓ SAFE | Staffing, payroll outsourcing, workforce management for enterprises | 📈 BULL_ANY_MID | 17 | ↑91 | ↑1.043 | ↑3d | — | +7.4% | 57.19/54.62 | +3.08% | 20% |
| [ESCORTS](https://in.tradingview.com/chart/?symbol=NSE:ESCORTS)<br><sub>📶W9 · W↑38d · 🚀SS · ↑CMF10d</sub> | ✓ SAFE | Tractors, engines, construction equipment, agriculture and infrastructure | 📈 BULL_ANY_MID | 12 | ↑28 | ↑1.015 | ↑13d | — | +7.6% | 52.47/51.27 | +0.61% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 11 | ↑68 | ↓1.011 | ↑9d | — | +5.3% | 52.94/52.13 | +0.00% | 20% |
| [LENSKART](https://in.tradingview.com/chart/?symbol=NSE:LENSKART)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Eyewear design manufacturing retail omnichannel direct consumer | 📈 BULL_ANY_MID | 5 | ↑50 | ↑1.030 | ↑30d | — | +15.9% | 64.3/61.91 | +2.24% | 20% |
| [NILKAMAL](https://in.tradingview.com/chart/?symbol=NSE:NILKAMAL)<br><sub>📶W9 · W↑48d · ↑CMF18d</sub> | ✓ SAFE | Plastic furniture and material handling solutions for residential commercial sectors | 📈 BULL_ANY_MID | 0 | ↑82 | ↓1.045 | ↑30d | — | +47.4% | 60.36/58.71 | -0.50% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:TIIL,NSE:PFIZER,NSE:CNL,NSE:FIVESTAR,NSE:MANALIPETC,NSE:IKIO,NSE:HEXT,NSE:CORONA,NSE:FINOPB,NSE:OFSS,NSE:TTKHLTCARE,NSE:QPOWER,NSE:GOKULAGRO,NSE:ABBOTINDIA,NSE:KRN,NSE:QUESS,NSE:ESCORTS,NSE:NESTLEIND,NSE:LENSKART,NSE:NILKAMAL
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (29)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [TIIL](https://in.tradingview.com/chart/?symbol=NSE:TIIL)<br><sub>📶W9 · W↑18d · 🚀SS·18x · ↑CMF0d</sub> | ✓ SAFE | Drum closures, scaffolding systems, textiles manufacturing | ⚡ BULL_ANY_PPV | 40 | 🔄63 | ↑1.078 | ↑10d | PV | +13.1% | 56.15/49.59 | +10.33% | 20% |
| [PFIZER](https://in.tradingview.com/chart/?symbol=NSE:PFIZER)<br><sub>📶W9 · W↑28d · ↑CMF12d</sub> | ⚠ CAUTION | Pharmaceutical manufacturing, vaccines, oncology drugs, India operations | ⚡ BULL_ANY_PPV | 8 | ↑43 | ↑1.028 | ↑17d | PV | +9.6% | 59.86/56.98 | +2.43% | 20% |
| [CNL](https://in.tradingview.com/chart/?symbol=NSE:CNL)<br><sub>📶W9 · W↑82d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | IT and lifestyle products distributor for retailers | ⚡ BULL_ANY_PPV | 0 | ↑97 | ↑1.107 | ↑48d | PV | +91.4% | 71.37/70.09 | +8.22% | 20% |
| [FIVESTAR](https://in.tradingview.com/chart/?symbol=NSE:FIVESTAR)<br><sub>📶W9 · W↑43d · ↑CMF0d</sub> | ✓ SAFE | Secured business loans for micro-entrepreneurs south india | 📈 BULL_ANY_MID | 99 | 🔄60 | ↑1.009 | ↑1d | SQ | +1.5% | 8.4/7.28 | +1.49% | 20% |
| [MANALIPETC](https://in.tradingview.com/chart/?symbol=NSE:MANALIPETC)<br><sub>📶W9 · W↑18d · ↓CMF11d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 93 | 🔄59 | ↑1.026 | ↑2d | SQ | +4.7% | 20.46/15.16 | +2.84% | 20% |
| [IKIO](https://in.tradingview.com/chart/?symbol=NSE:IKIO)<br><sub>📶W9 · W↑91d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | LED lighting ODM, precision electronics, India domestic commercial | 📈 BULL_ANY_MID | 89 | 🔄79 | ↑1.049 | ↑1d | SQ | +5.5% | 2.76/-5.84 | +5.53% | 20% |
| [CORONA](https://in.tradingview.com/chart/?symbol=NSE:CORONA)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Pharma formulations women's health cardiology pain management domestic | 📈 BULL_ANY_MID | 63 | ↑50 | ↑1.016 | ↑2d | SQ | +2.3% | 32.33/31.37 | +0.55% | 20% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄83 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [TTKHLTCARE](https://in.tradingview.com/chart/?symbol=NSE:TTKHLTCARE)<br><sub>📶W9 · W↑91d · ↓CMF20d</sub> | ✓ SAFE | Pharmaceuticals, medical devices, consumer healthcare products India | 📈 BULL_ANY_MID | 51 | ↑61 | ↑1.034 | ↑9d | SQ | +10.2% | 55.08/53.55 | +1.67% | 20% |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER)<br><sub>📶W9 · 🚀SS · ↓CMF1d · DEL61%</sub> | ✓ SAFE | High-voltage electrical equipment manufacturer for power infrastructure | 📈 BULL_ANY_MID | 48 | 🔄98 | ↑1.071 | ↑2d | — | +22.9% | 1.99/-2.65 | +4.45% | 5% 🟥 |
| [GOKULAGRO](https://in.tradingview.com/chart/?symbol=NSE:GOKULAGRO)<br><sub>📶W9 · W↑8d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Edible oils refining, palm soybean sunflower processing, food sector | 📈 BULL_ANY_MID | 39 | 🔄77 | ↑1.042 | ↑11d | — | +12.2% | 39.58/36.32 | +4.68% | 20% |
| [ABBOTINDIA](https://in.tradingview.com/chart/?symbol=NSE:ABBOTINDIA)<br><sub>📶W9 · W↑28d · ↑CMF21d</sub> | ⚠ CAUTION | Pharmaceuticals, diagnostics, nutritional products for India healthcare | 📈 BULL_ANY_MID | 28 | ↑34 | ↑1.009 | ↑2d | — | +2.2% | 15.16/9.85 | +0.43% | 20% |
| [KRN](https://in.tradingview.com/chart/?symbol=NSE:KRN)<br><sub>📶W9 · W↑2d · 🚀SS · ↓CMF2d · DEL57%</sub> | ✓ SAFE | Precision heat exchangers for HVAC refrigeration equipment makers | 📈 BULL_ANY_MID | 18 | ↑94 | ↑1.080 | ↑2d | — | +21.7% | 16.1/9.95 | +3.43% | 5% |
| [QUESS](https://in.tradingview.com/chart/?symbol=NSE:QUESS)<br><sub>📶W9 · W↑91d · ↑CMF30d</sub> | ✓ SAFE | Staffing, payroll outsourcing, workforce management for enterprises | 📈 BULL_ANY_MID | 17 | ↑91 | ↑1.043 | ↑3d | — | +7.4% | 57.19/54.62 | +3.08% | 20% |
| [ESCORTS](https://in.tradingview.com/chart/?symbol=NSE:ESCORTS)<br><sub>📶W9 · W↑38d · 🚀SS · ↑CMF10d</sub> | ✓ SAFE | Tractors, engines, construction equipment, agriculture and infrastructure | 📈 BULL_ANY_MID | 12 | ↑28 | ↑1.015 | ↑13d | — | +7.6% | 52.47/51.27 | +0.61% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 11 | ↑68 | ↓1.011 | ↑9d | — | +5.3% | 52.94/52.13 | +0.00% | 20% |
| [LENSKART](https://in.tradingview.com/chart/?symbol=NSE:LENSKART)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Eyewear design manufacturing retail omnichannel direct consumer | 📈 BULL_ANY_MID | 5 | ↑50 | ↑1.030 | ↑30d | — | +15.9% | 64.3/61.91 | +2.24% | 20% |
| [NILKAMAL](https://in.tradingview.com/chart/?symbol=NSE:NILKAMAL)<br><sub>📶W9 · W↑48d · ↑CMF18d</sub> | ✓ SAFE | Plastic furniture and material handling solutions for residential commercial sectors | 📈 BULL_ANY_MID | 0 | ↑82 | ↓1.045 | ↑30d | — | +47.4% | 60.36/58.71 | -0.50% | 20% |
| [SKIPPER](https://in.tradingview.com/chart/?symbol=NSE:SKIPPER)<br><sub>↓CMF30d · ÷DIV</sub> | ✓ SAFE | Power transmission towers, polymer pipes, infrastructure projects | ⚡ BULL_ANY_PPV | 94 | 🔄70 | ↑1.016 | ↑1d | SQ·PV | +2.8% | -20.55/-21.04 | +2.77% | 20% |
| [JUBLCPL](https://in.tradingview.com/chart/?symbol=NSE:JUBLCPL)<br><sub>🚀SS·22x · ↓CMF9d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 49 | 🔄37 | ↑1.036 | ↑1d | PV | +4.0% | -12.1/-22.18 | +3.98% | 20% |
| [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC)<br><sub>🚀SS · ↓CMF17d</sub> | ✓ SAFE | Music content creation, distribution, digital monetization platform | 📈 BULL_ANY_MID | 99 | 🔄68 | ↑1.007 | ↑1d | SQ | +0.8% | -20.15/-23.28 | +0.78% | 20% |
| [GPTINFRA](https://in.tradingview.com/chart/?symbol=NSE:GPTINFRA)<br><sub>↑CMF1d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄45 | ↑1.015 | ↑1d | SQ | +2.0% | -25.25/-29.87 | +2.03% | 20% |
| [GODREJCP](https://in.tradingview.com/chart/?symbol=NSE:GODREJCP)<br><sub>W↑33d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 98 | 🔄37 | ↑1.008 | ↑2d | SQ | +2.1% | 25.85/25.42 | +1.03% | 20% |
| [IGL](https://in.tradingview.com/chart/?symbol=NSE:IGL)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Natural gas distribution Delhi NCR transport domestic industrial | 📈 BULL_ANY_MID | 98 | 🔄17 | ↑1.009 | ↑2d | SQ | +1.6% | 1.47/-0.8 | +0.96% | 20% |
| [MAHABANK](https://in.tradingview.com/chart/?symbol=NSE:MAHABANK)<br><sub>↑CMF0d</sub> | ✓ SAFE | Public sector bank retail corporate wholesale lending | 📈 BULL_ANY_MID | 94 | 🔄78 | ↑1.028 | ↑1d | SQ | +3.7% | -31.22/-41.07 | +3.70% | 20% |
| [SPLPETRO](https://in.tradingview.com/chart/?symbol=NSE:SPLPETRO)<br><sub>🚀SS · ↓CMF18d</sub> | ✓ SAFE | Polystyrene and styrenics polymers manufacturer for packaging | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.023 | ↑1d | SQ | +5.9% | -28.65/-28.9 | +5.90% | 20% |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>🚀SS · ↓CMF2d</sub> | ⚠ CAUTION | Pharma APIs finished dosage forms global markets | 📈 BULL_ANY_MID | 59 | 🔄72 | ↑1.012 | ↑1d | — | +1.0% | -18.05/-21.82 | +1.04% | 20% |
| [SAATVIKGL](https://in.tradingview.com/chart/?symbol=NSE:SAATVIKGL)<br><sub>🚀SS · ↓CMF17d</sub> | ✓ SAFE | Solar modules manufacturing, EPC, renewable energy | 📈 BULL_ANY_MID | 59 | 🔄50 | ↑1.012 | ↑1d | — | +2.0% | -37.91/-44.12 | +2.03% | 20% |
| [GUJENERGY](https://in.tradingview.com/chart/?symbol=NSE:GUJENERGY)<br><sub>RVOL8x · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Compressed natural gas distribution to vehicles and households | 📈 BULL_ANY_MID | 58 | ↑2 | ↓1.006 | ↑2d | SQ | +3.4% | -16.48/-26.13 | -0.02% | 5% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:TIIL,NSE:PFIZER,NSE:CNL,NSE:FIVESTAR,NSE:MANALIPETC,NSE:IKIO,NSE:CORONA,NSE:OFSS,NSE:TTKHLTCARE,NSE:QPOWER,NSE:GOKULAGRO,NSE:ABBOTINDIA,NSE:KRN,NSE:QUESS,NSE:ESCORTS,NSE:NESTLEIND,NSE:LENSKART,NSE:NILKAMAL,NSE:SKIPPER,NSE:JUBLCPL,NSE:TIPSMUSIC,NSE:GPTINFRA,NSE:GODREJCP,NSE:IGL,NSE:MAHABANK,NSE:SPLPETRO,NSE:IPCALAB,NSE:SAATVIKGL,NSE:GUJENERGY
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (17)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [FIVESTAR](https://in.tradingview.com/chart/?symbol=NSE:FIVESTAR)<br><sub>📶W9 · W↑43d · ↑CMF0d</sub> | ✓ SAFE | Secured business loans for micro-entrepreneurs south india | 📈 BULL_ANY_MID | 99 | 🔄60 | ↑1.009 | ↑1d | SQ | +1.5% | 8.4/7.28 | +1.49% | 20% |
| [MANALIPETC](https://in.tradingview.com/chart/?symbol=NSE:MANALIPETC)<br><sub>📶W9 · W↑18d · ↓CMF11d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 93 | 🔄59 | ↑1.026 | ↑2d | SQ | +4.7% | 20.46/15.16 | +2.84% | 20% |
| [IKIO](https://in.tradingview.com/chart/?symbol=NSE:IKIO)<br><sub>📶W9 · W↑91d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | LED lighting ODM, precision electronics, India domestic commercial | 📈 BULL_ANY_MID | 89 | 🔄79 | ↑1.049 | ↑1d | SQ | +5.5% | 2.76/-5.84 | +5.53% | 20% |
| [HEXT](https://in.tradingview.com/chart/?symbol=NSE:HEXT)<br><sub>📶W9 · W↑94d · ↑CMF3d</sub> | ✓ SAFE | IT Services, Digital Transformation, Automation Solutions, Global Enterprises | 📈 BULL_ANY_MID | 69 | ↓37 | ↑1.002 | ↑1d | SQ | +0.3% | 15.29/15.25 | +0.32% | 20% |
| [CORONA](https://in.tradingview.com/chart/?symbol=NSE:CORONA)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Pharma formulations women's health cardiology pain management domestic | 📈 BULL_ANY_MID | 63 | ↑50 | ↑1.016 | ↑2d | SQ | +2.3% | 32.33/31.37 | +0.55% | 20% |
| [FINOPB](https://in.tradingview.com/chart/?symbol=NSE:FINOPB)<br><sub>📶W9 · W↑86d · ↑CMF30d</sub> | ✓ SAFE | Digital payments bank serving underbanked India populations | 📈 BULL_ANY_MID | 58 | ↓26 | ↓1.000 | ↓2d | SQ | +1.8% | -10.8/-12.49 | -1.24% | 20% 🟦 |
| [TTKHLTCARE](https://in.tradingview.com/chart/?symbol=NSE:TTKHLTCARE)<br><sub>📶W9 · W↑91d · ↓CMF20d</sub> | ✓ SAFE | Pharmaceuticals, medical devices, consumer healthcare products India | 📈 BULL_ANY_MID | 51 | ↑61 | ↑1.034 | ↑9d | SQ | +10.2% | 55.08/53.55 | +1.67% | 20% |
| [SKIPPER](https://in.tradingview.com/chart/?symbol=NSE:SKIPPER)<br><sub>↓CMF30d · ÷DIV</sub> | ✓ SAFE | Power transmission towers, polymer pipes, infrastructure projects | ⚡ BULL_ANY_PPV | 94 | 🔄70 | ↑1.016 | ↑1d | SQ·PV | +2.8% | -20.55/-21.04 | +2.77% | 20% |
| [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC)<br><sub>🚀SS · ↓CMF17d</sub> | ✓ SAFE | Music content creation, distribution, digital monetization platform | 📈 BULL_ANY_MID | 99 | 🔄68 | ↑1.007 | ↑1d | SQ | +0.8% | -20.15/-23.28 | +0.78% | 20% |
| [GPTINFRA](https://in.tradingview.com/chart/?symbol=NSE:GPTINFRA)<br><sub>↑CMF1d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄45 | ↑1.015 | ↑1d | SQ | +2.0% | -25.25/-29.87 | +2.03% | 20% |
| [GODREJCP](https://in.tradingview.com/chart/?symbol=NSE:GODREJCP)<br><sub>W↑33d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 98 | 🔄37 | ↑1.008 | ↑2d | SQ | +2.1% | 25.85/25.42 | +1.03% | 20% |
| [IGL](https://in.tradingview.com/chart/?symbol=NSE:IGL)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Natural gas distribution Delhi NCR transport domestic industrial | 📈 BULL_ANY_MID | 98 | 🔄17 | ↑1.009 | ↑2d | SQ | +1.6% | 1.47/-0.8 | +0.96% | 20% |
| [MAHABANK](https://in.tradingview.com/chart/?symbol=NSE:MAHABANK)<br><sub>↑CMF0d</sub> | ✓ SAFE | Public sector bank retail corporate wholesale lending | 📈 BULL_ANY_MID | 94 | 🔄78 | ↑1.028 | ↑1d | SQ | +3.7% | -31.22/-41.07 | +3.70% | 20% |
| [SPLPETRO](https://in.tradingview.com/chart/?symbol=NSE:SPLPETRO)<br><sub>🚀SS · ↓CMF18d</sub> | ✓ SAFE | Polystyrene and styrenics polymers manufacturer for packaging | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.023 | ↑1d | SQ | +5.9% | -28.65/-28.9 | +5.90% | 20% |
| [MFSL](https://in.tradingview.com/chart/?symbol=NSE:MFSL)<br><sub>🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Life insurance products, retail and corporate segments | 📈 BULL_ANY_MID | 62 | ↓27 | ↑1.001 | ↓8d | SQ | +1.1% | -40.62/-40.93 | +1.13% | 20% |
| [GUJENERGY](https://in.tradingview.com/chart/?symbol=NSE:GUJENERGY)<br><sub>RVOL8x · ↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION | Compressed natural gas distribution to vehicles and households | 📈 BULL_ANY_MID | 58 | ↑2 | ↓1.006 | ↑2d | SQ | +3.4% | -16.48/-26.13 | -0.02% | 5% |
| [IIFLCAPS](https://in.tradingview.com/chart/?symbol=NSE:IIFLCAPS)<br><sub>↓CMF14d · ⚠️TRAP</sub> | ⚠ CAUTION | Equities broking, wealth management, investment banking for retail | 📈 BULL_ANY_MID | 51 | ↓43 | ↑0.999 | ↓14d | SQ | -1.4% | -43.52/-44.82 | +0.06% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:FIVESTAR,NSE:MANALIPETC,NSE:IKIO,NSE:HEXT,NSE:CORONA,NSE:FINOPB,NSE:TTKHLTCARE,NSE:SKIPPER,NSE:TIPSMUSIC,NSE:GPTINFRA,NSE:GODREJCP,NSE:IGL,NSE:MAHABANK,NSE:SPLPETRO,NSE:MFSL,NSE:GUJENERGY,NSE:IIFLCAPS
```

---

### 🔥 MAJOR — PPV confirmed (4)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [TIIL](https://in.tradingview.com/chart/?symbol=NSE:TIIL)<br><sub>📶W9 · W↑18d · 🚀SS·18x · ↑CMF0d</sub> | ✓ SAFE | Drum closures, scaffolding systems, textiles manufacturing | ⚡ BULL_ANY_PPV | 40 | 🔄63 | ↑1.078 | ↑10d | PV | +13.1% | 56.15/49.59 | +10.33% | 20% |
| [PFIZER](https://in.tradingview.com/chart/?symbol=NSE:PFIZER)<br><sub>📶W9 · W↑28d · ↑CMF12d</sub> | ⚠ CAUTION | Pharmaceutical manufacturing, vaccines, oncology drugs, India operations | ⚡ BULL_ANY_PPV | 8 | ↑43 | ↑1.028 | ↑17d | PV | +9.6% | 59.86/56.98 | +2.43% | 20% |
| [CNL](https://in.tradingview.com/chart/?symbol=NSE:CNL)<br><sub>📶W9 · W↑82d · 🚀SS · ↑CMF22d</sub> | ✓ SAFE | IT and lifestyle products distributor for retailers | ⚡ BULL_ANY_PPV | 0 | ↑97 | ↑1.107 | ↑48d | PV | +91.4% | 71.37/70.09 | +8.22% | 20% |
| [JUBLCPL](https://in.tradingview.com/chart/?symbol=NSE:JUBLCPL)<br><sub>🚀SS·22x · ↓CMF9d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 49 | 🔄37 | ↑1.036 | ↑1d | PV | +4.0% | -12.1/-22.18 | +3.98% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:TIIL,NSE:PFIZER,NSE:CNL,NSE:JUBLCPL
```

### 🟢 OVERSOLD — reversal from −53/−60 (5)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [INDOTHAI](https://in.tradingview.com/chart/?symbol=NSE:INDOTHAI)<br><sub>↓CMF30d · ⚠️TRAP · DEL100%</sub> | ✓ SAFE | Stock broker serving corporates HNIs retail investors | 🟢 BULL_OVERSOLD | 12 | ↓0 | ↑0.676 | ↓13d | — | -60.5% | -78.07/-78.79 | -4.99% | 20% 🟦 |
| [HUBTOWN](https://in.tradingview.com/chart/?symbol=NSE:HUBTOWN)<br><sub>↓CMF15d · ⚠️TRAP</sub> | ✓ SAFE | Residential Commercial real estate MMR Mumbai Thane development | 🟢 BULL_OVERSOLD | 3 | ↓2 | ↓0.974 | ↓17d | — | -10.7% | -64.99/-66.27 | -0.67% | 20% |
| [BBL](https://in.tradingview.com/chart/?symbol=NSE:BBL)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Transformers, motors, drives for industrial manufacturing | 🟢 BULL_OVERSOLD | 0 | ↓10 | ↓0.965 | ↓23d | — | -16.6% | -69.66/-70.85 | -1.14% | 20% |
| [LICHSGFIN](https://in.tradingview.com/chart/?symbol=NSE:LICHSGFIN)<br><sub>↓CMF12d · 🎯SLING</sub> | ⚠ CAUTION | Housing loans for residential property purchase construction | 🟡 BULL_OS_L2 | 14 | ↓24 | ↑0.990 | ↓11d | — | -6.9% | -56.13/-56.19 | +1.20% | 20% |
| [VBL](https://in.tradingview.com/chart/?symbol=NSE:VBL)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 5 | ↓22 | ↑0.992 | ↓38d | — | -15.2% | -55.06/-56.28 | +1.38% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:INDOTHAI,NSE:HUBTOWN,NSE:BBL,NSE:LICHSGFIN,NSE:VBL
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (17)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>📶W9 · W↑90d · 🚀SS · ↑CMF27d</sub> | ✓ SAFE | Banking software solutions for financial institutions globally | 📈 BULL_ANY_MID | 53 | 🔄83 | ↑1.025 | ↑2d | — | +3.7% | 23.03/19.56 | +2.36% | 20% |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER)<br><sub>📶W9 · 🚀SS · ↓CMF1d · DEL61%</sub> | ✓ SAFE | High-voltage electrical equipment manufacturer for power infrastructure | 📈 BULL_ANY_MID | 48 | 🔄98 | ↑1.071 | ↑2d | — | +22.9% | 1.99/-2.65 | +4.45% | 5% 🟥 |
| [GOKULAGRO](https://in.tradingview.com/chart/?symbol=NSE:GOKULAGRO)<br><sub>📶W9 · W↑8d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Edible oils refining, palm soybean sunflower processing, food sector | 📈 BULL_ANY_MID | 39 | 🔄77 | ↑1.042 | ↑11d | — | +12.2% | 39.58/36.32 | +4.68% | 20% |
| [ABBOTINDIA](https://in.tradingview.com/chart/?symbol=NSE:ABBOTINDIA)<br><sub>📶W9 · W↑28d · ↑CMF21d</sub> | ⚠ CAUTION | Pharmaceuticals, diagnostics, nutritional products for India healthcare | 📈 BULL_ANY_MID | 28 | ↑34 | ↑1.009 | ↑2d | — | +2.2% | 15.16/9.85 | +0.43% | 20% |
| [KRN](https://in.tradingview.com/chart/?symbol=NSE:KRN)<br><sub>📶W9 · W↑2d · 🚀SS · ↓CMF2d · DEL57%</sub> | ✓ SAFE | Precision heat exchangers for HVAC refrigeration equipment makers | 📈 BULL_ANY_MID | 18 | ↑94 | ↑1.080 | ↑2d | — | +21.7% | 16.1/9.95 | +3.43% | 5% |
| [QUESS](https://in.tradingview.com/chart/?symbol=NSE:QUESS)<br><sub>📶W9 · W↑91d · ↑CMF30d</sub> | ✓ SAFE | Staffing, payroll outsourcing, workforce management for enterprises | 📈 BULL_ANY_MID | 17 | ↑91 | ↑1.043 | ↑3d | — | +7.4% | 57.19/54.62 | +3.08% | 20% |
| [ESCORTS](https://in.tradingview.com/chart/?symbol=NSE:ESCORTS)<br><sub>📶W9 · W↑38d · 🚀SS · ↑CMF10d</sub> | ✓ SAFE | Tractors, engines, construction equipment, agriculture and infrastructure | 📈 BULL_ANY_MID | 12 | ↑28 | ↑1.015 | ↑13d | — | +7.6% | 52.47/51.27 | +0.61% | 20% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF5d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 11 | ↑68 | ↓1.011 | ↑9d | — | +5.3% | 52.94/52.13 | +0.00% | 20% |
| [LENSKART](https://in.tradingview.com/chart/?symbol=NSE:LENSKART)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Eyewear design manufacturing retail omnichannel direct consumer | 📈 BULL_ANY_MID | 5 | ↑50 | ↑1.030 | ↑30d | — | +15.9% | 64.3/61.91 | +2.24% | 20% |
| [NILKAMAL](https://in.tradingview.com/chart/?symbol=NSE:NILKAMAL)<br><sub>📶W9 · W↑48d · ↑CMF18d</sub> | ✓ SAFE | Plastic furniture and material handling solutions for residential commercial sectors | 📈 BULL_ANY_MID | 0 | ↑82 | ↓1.045 | ↑30d | — | +47.4% | 60.36/58.71 | -0.50% | 20% |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>🚀SS · ↓CMF2d</sub> | ⚠ CAUTION | Pharma APIs finished dosage forms global markets | 📈 BULL_ANY_MID | 59 | 🔄72 | ↑1.012 | ↑1d | — | +1.0% | -18.05/-21.82 | +1.04% | 20% |
| [SAATVIKGL](https://in.tradingview.com/chart/?symbol=NSE:SAATVIKGL)<br><sub>🚀SS · ↓CMF17d</sub> | ✓ SAFE | Solar modules manufacturing, EPC, renewable energy | 📈 BULL_ANY_MID | 59 | 🔄50 | ↑1.012 | ↑1d | — | +2.0% | -37.91/-44.12 | +2.03% | 20% |
| [CCL](https://in.tradingview.com/chart/?symbol=NSE:CCL)<br><sub>🚀SS · ↓CMF27d</sub> | ⚠ CAUTION | Instant coffee manufacturing and export, global markets | 📈 BULL_ANY_MID | 14 | ↓61 | ↑0.995 | ↓11d | — | -4.4% | -45.14/-45.18 | +1.06% | 20% |
| [SIGNPOST](https://in.tradingview.com/chart/?symbol=NSE:SIGNPOST)<br><sub>↓CMF8d · ⚠️TRAP</sub> | ✓ SAFE | Digital advertising displays buses metros transit | 📈 BULL_ANY_MID | 14 | ↓56 | ↑0.973 | ↓11d | — | -11.6% | -43.61/-43.65 | -0.52% | 20% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>↓CMF23d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 10 | ↓61 | ↑0.984 | ↓15d | — | -7.1% | -51.35/-51.43 | -0.24% | 20% |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA)<br><sub>↓CMF11d · ⚠️TRAP</sub> | ✓ SAFE | Wealth advisory, portfolio management, institutional and HNI clients | 📈 BULL_ANY_MID | 3 | ↓71 | ↓0.989 | ↓17d | — | -8.5% | -34.25/-34.78 | -0.59% | 20% |
| [JNKINDIA](https://in.tradingview.com/chart/?symbol=NSE:JNKINDIA)<br><sub>↓CMF25d · ⚠️TRAP</sub> | ✓ SAFE | Heating equipment waste gas management systems oil gas petrochemical | 📈 BULL_ANY_MID | 0 | ↓84 | ↓0.960 | ↓25d | — | -12.4% | -46.64/-47.89 | -2.76% | 20% 🟦 |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:OFSS,NSE:QPOWER,NSE:GOKULAGRO,NSE:ABBOTINDIA,NSE:KRN,NSE:QUESS,NSE:ESCORTS,NSE:NESTLEIND,NSE:LENSKART,NSE:NILKAMAL,NSE:IPCALAB,NSE:SAATVIKGL,NSE:CCL,NSE:SIGNPOST,NSE:ADANIPORTS,NSE:NUVAMA,NSE:JNKINDIA
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
