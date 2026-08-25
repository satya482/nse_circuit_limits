> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-08-25
*Generated 2026-08-25 15:45 IST*

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

**Total bull crosses today: 69** · 19 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:AWL,NSE:FACT,NSE:SIEMENS,NSE:GODREJAGRO,NSE:SETL,NSE:SHILPAMED,NSE:CYIENTDLM,NSE:NEPHROPLUS,NSE:NPST,NSE:ACUTAAS,NSE:ECLERX,NSE:ALGOQUANT,NSE:KALYANKJIL,NSE:INDUSINDBK,NSE:GCSL,NSE:CUB,NSE:AIIL,NSE:CONFIPET,NSE:GANESHHOU,NSE:SHREEJISPG,NSE:LODHA,NSE:LANDMARK,NSE:BDL,NSE:ETHOSLTD,NSE:QUESS,NSE:MOL,NSE:TBOTEK,NSE:SKYGOLD,NSE:RCF,NSE:DELTACORP,NSE:NFL,NSE:BRIGHOTEL,NSE:RAMCOCEM,NSE:ROUTE,NSE:UGROCAP,NSE:STARCEMENT,NSE:METROBRAND,NSE:ABLBL,NSE:COALINDIA,NSE:TORNTPOWER,NSE:EPACK,NSE:SIKA,NSE:SAGCEM,NSE:ICEMAKE,NSE:EIEL,NSE:ORIENTTECH,NSE:HUDCO,NSE:JINDALPOLY,NSE:PARKHOSPS,NSE:LICHSGFIN,NSE:ITCHOTELS,NSE:ICRA,NSE:HAWKINCOOK,NSE:CAPITALSFB,NSE:HDFCAMC,NSE:VENUSPIPES,NSE:LINCOLN,NSE:VOLTAS,NSE:GPTINFRA,NSE:SURYAROSNI,NSE:RAMCOSYS,NSE:HARIOMPIPE,NSE:SANSTAR,NSE:SUNPHARMA,NSE:TTKPRESTIG,NSE:DEEPAKFERT,NSE:NHPC,NSE:JKTYRE
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (29)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>📶W9 · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Spirits manufacturer, IMFL exporter, Indian domestic and export markets | ⚡ BULL_ANY_PPV | 59 | ↑63 | ↑1.036 | ↑1d | SQ·PV | +3.8% | -22.64/-34.57 | +3.78% | 10% 🟩 |
| [AWL](https://in.tradingview.com/chart/?symbol=NSE:AWL)<br><sub>📶W9 · W↑32d · 🚀SS · ↓CMF17d</sub> | ✓ SAFE | Edible oils wheat flour rice pulses sugar FMCG | ⚡ BULL_ANY_PPV | 58 | ↑25 | ↑1.040 | ↑2d | SQ·PV | +6.7% | 12.03/-1.19 | +3.49% | 20% |
| [FACT](https://in.tradingview.com/chart/?symbol=NSE:FACT)<br><sub>📶W9 · 🚀SS·337x · ↑CMF0d</sub> | ✓ SAFE | Nitrogen fertilizer production chemicals agricultural sector south India | ⚡ BULL_ANY_PPV | 49 | 🔄41 | ↑1.080 | ↑1d | PV | +11.7% | -35.53/-49.73 | +11.71% | 20% |
| [SIEMENS](https://in.tradingview.com/chart/?symbol=NSE:SIEMENS)<br><sub>📶W9 · W↑21d · ↑CMF20d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 48 | 🔄74 | ↑1.037 | ↑2d | PV | +5.6% | 36.54/33.96 | +4.54% | 20% |
| [GODREJAGRO](https://in.tradingview.com/chart/?symbol=NSE:GODREJAGRO)<br><sub>📶W9 · W↑7d · RVOL17x · ↑CMF8d</sub> | ✓ SAFE | Animal feed, crop protection, oil palm processing | ⚡ BULL_ANY_PPV | 41 | 🔄39 | ↑1.052 | ↑9d | PV | +10.5% | 26.06/18.3 | +6.52% | 20% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>📶W9 · ↑CMF10d</sub> | ✓ SAFE | Glass-lined reactors pharmaceuticals chemicals process equipment | ⚡ BULL_ANY_PPV | 18 | ↑99 | ↓1.036 | ↑2d | PV | +5.7% | 57.2/56.73 | +0.77% | 5% 🟥 |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>📶W9 · W↑17d · ★ · ↑CMF1d</sub> | ✓ SAFE | Niche APIs formulations contract manufacturing pharma | ⚡ BULL_ANY_PPV | 3 | ↑98 | ↓1.056 | ↑17d | PV | +41.0% | 60.03/59.72 | +0.67% | 20% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>📶W9 · W↑112d · ↑CMF0d</sub> | ✓ SAFE | Electronics manufacturing design integration testing subsystems defense aerospace | ⚡ BULL_ANY_PPV | 0 | ↑98 | ↑1.059 | ↑39d | PV | +65.7% | 61.64/59.11 | +4.55% | 20% |
| [NEPHROPLUS](https://in.tradingview.com/chart/?symbol=NSE:NEPHROPLUS)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Dialysis center chain serving kidney disease patients India | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.009 | ↑1d | SQ | +1.5% | 9.12/8.24 | +1.53% | 20% |
| [NPST](https://in.tradingview.com/chart/?symbol=NSE:NPST)<br><sub>📶W9 · W↑7d · ↑CMF7d</sub> | ✓ SAFE | UPI payments software and real-time transaction processing platform | 📈 BULL_ANY_MID | 99 | 🔄71 | ↑1.014 | ↑1d | SQ | +3.0% | 17.09/16.46 | +2.96% | 10% 🟨 |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Pharmaceutical intermediates and specialty chemicals manufacturer | 📈 BULL_ANY_MID | 94 | 🔄92 | ↑1.024 | ↑1d | SQ | +4.4% | -15.22/-16.21 | +4.42% | 20% |
| [ECLERX](https://in.tradingview.com/chart/?symbol=NSE:ECLERX)<br><sub>📶W9 · W↑42d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | BPM automation analytics for Fortune 2000 financial services retail | 📈 BULL_ANY_MID | 94 | 🔄52 | ↑1.023 | ↑1d | SQ | +3.1% | 4.61/-0.18 | +3.11% | 20% |
| [ALGOQUANT](https://in.tradingview.com/chart/?symbol=NSE:ALGOQUANT)<br><sub>📶W9 · 🚀SS · ↓CMF6d · DEL44%(T-1)</sub> | ✓ SAFE | Algorithmic trading software capital markets quantitative strategies | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.017 | ↑1d | SQ | +2.1% | -8.23/-10.68 | +2.14% | 20% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>📶W9 · W↑52d · ↓CMF7d · DEL28%(T-1)</sub> | ✓ SAFE | Gold jewellery retail, pan-India stores, consumer luxury | 📈 BULL_ANY_MID | 68 | ↑90 | ↑1.014 | ↑2d | SQ | +1.5% | 28.93/23.82 | +0.76% | 20% |
| [INDUSINDBK](https://in.tradingview.com/chart/?symbol=NSE:INDUSINDBK)<br><sub>📶W9 · ↑CMF30d</sub> | ⚠ CAUTION | Private bank vehicle finance microfinance retail lending | 📈 BULL_ANY_MID | 58 | ↓67 | ↓1.000 | ↓2d | SQ | +0.9% | -10.22/-11.04 | -0.33% | 20% |
| [GCSL](https://in.tradingview.com/chart/?symbol=NSE:GCSL)<br><sub>📶W9 · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Merchant banking, corporate finance, capital markets advisory | 📈 BULL_ANY_MID | 58 | ↑50 | ↑1.030 | ↑2d | SQ | +7.0% | 0.48/-5.42 | +2.14% | 20% 🟦 |
| [CUB](https://in.tradingview.com/chart/?symbol=NSE:CUB)<br><sub>📶W9 · W↑2d · 🚀SS · ↓CMF2d</sub> | ✓ SAFE | Private bank serving SMEs, MSMEs, retail customers, South India | 📈 BULL_ANY_MID | 54 | 🔄15 | ↑1.022 | ↑1d | — | +4.4% | 12.72/11.75 | +4.43% | 20% |
| [AIIL](https://in.tradingview.com/chart/?symbol=NSE:AIIL)<br><sub>📶W9 · W↑57d · 🚀SS · ↑CMF23d</sub> | ✓ SAFE | NBFC lending and investment securities portfolio management | 📈 BULL_ANY_MID | 54 | 🔄57 | ↑1.017 | ↑1d | — | +2.1% | 3.16/0.66 | +2.12% | 20% |
| [CONFIPET](https://in.tradingview.com/chart/?symbol=NSE:CONFIPET)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | LPG cylinders manufacturing, bottling plants, auto-LPG dispensing stations | 📈 BULL_ANY_MID | 49 | 🔄94 | ↑1.044 | ↑1d | — | +7.9% | -8.23/-12.07 | +7.92% | 10% 🟨 |
| [GANESHHOU](https://in.tradingview.com/chart/?symbol=NSE:GANESHHOU)<br><sub>📶W9 · W↑7d · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | Residential real estate development Ahmedabad Gujarat region | 📈 BULL_ANY_MID | 46 | 🔄59 | ↑1.027 | ↑9d | — | +9.6% | 20.42/19.55 | +3.78% | 20% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>📶W9 · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Dry bulk ship operator maritime logistics cargo transport | 📈 BULL_ANY_MID | 24 | ↑50 | ↑1.016 | ↑1d | — | +1.6% | 7.34/6.53 | +1.61% | 10% 🟩 |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>📶W9 · W↑93d · ↑CMF30d</sub> | ✓ SAFE | Residential and commercial real estate development, Mumbai Pune Bangalore | 📈 BULL_ANY_MID | 18 | ↑69 | ↓1.006 | ↑2d | — | +2.1% | 18.8/16.24 | -0.34% | 20% |
| [LANDMARK](https://in.tradingview.com/chart/?symbol=NSE:LANDMARK)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Premium auto retail, luxury and mass-market vehicles, India | 📈 BULL_ANY_MID | 18 | ↑69 | ↓1.007 | ↓2d | — | +4.7% | -0.68/-4.39 | -2.46% | 20% |
| [BDL](https://in.tradingview.com/chart/?symbol=NSE:BDL)<br><sub>📶W9 · W↑12d · ↑CMF11d</sub> | ✓ SAFE | Guided missiles and defense systems for Indian Armed Forces | 📈 BULL_ANY_MID | 17 | ↑46 | ↓1.007 | ↑3d | — | +3.3% | 38.7/38.45 | -0.59% | 20% |
| [ETHOSLTD](https://in.tradingview.com/chart/?symbol=NSE:ETHOSLTD)<br><sub>📶W9 · W↑67d · ↓CMF5d</sub> | ✓ SAFE | Premium luxury watch retail, multi-brand, Indian affluent consumers | 📈 BULL_ANY_MID | 13 | ↑63 | ↓1.016 | ↑7d | — | +5.4% | 46.32/45.76 | +0.09% | 20% |
| [QUESS](https://in.tradingview.com/chart/?symbol=NSE:QUESS)<br><sub>📶W9 · W↑100d · ↑CMF30d</sub> | ✓ SAFE | Staffing, payroll outsourcing, workforce management for enterprises | 📈 BULL_ANY_MID | 8 | ↑94 | ↑1.031 | ↑12d | — | +11.6% | 58.12/58.07 | +2.48% | 20% |
| [MOL](https://in.tradingview.com/chart/?symbol=NSE:MOL)<br><sub>📶W9 · W↑27d · ↓CMF19d</sub> | ✓ SAFE | Chemical manufacturer: pigments, agrochemicals, crop nutrition | 📈 BULL_ANY_MID | 8 | ↑55 | ↓1.024 | ↑12d | — | +18.8% | 51.96/51.36 | -2.98% | 20% |
| [TBOTEK](https://in.tradingview.com/chart/?symbol=NSE:TBOTEK)<br><sub>📶W9 · W↑67d · ↑CMF0d</sub> | ✓ SAFE | Global travel distribution platform for hotels airlines agents | 📈 BULL_ANY_MID | 5 | ↑77 | ↑1.028 | ↑22d | — | +20.7% | 57.86/57.73 | +1.27% | 20% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>📶W9 · W↑37d · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Gold jewelry manufacturer supplying retailers and boutiques | 📈 BULL_ANY_MID | 2 | ↑99 | ↑1.067 | ↑18d | — | +32.0% | 61.76/60.5 | +5.55% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:AWL,NSE:FACT,NSE:SIEMENS,NSE:GODREJAGRO,NSE:SETL,NSE:SHILPAMED,NSE:CYIENTDLM,NSE:NEPHROPLUS,NSE:NPST,NSE:ACUTAAS,NSE:ECLERX,NSE:ALGOQUANT,NSE:KALYANKJIL,NSE:INDUSINDBK,NSE:GCSL,NSE:CUB,NSE:AIIL,NSE:CONFIPET,NSE:GANESHHOU,NSE:SHREEJISPG,NSE:LODHA,NSE:LANDMARK,NSE:BDL,NSE:ETHOSLTD,NSE:QUESS,NSE:MOL,NSE:TBOTEK,NSE:SKYGOLD
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (37)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>📶W9 · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Spirits manufacturer, IMFL exporter, Indian domestic and export markets | ⚡ BULL_ANY_PPV | 59 | ↑63 | ↑1.036 | ↑1d | SQ·PV | +3.8% | -22.64/-34.57 | +3.78% | 10% 🟩 |
| [AWL](https://in.tradingview.com/chart/?symbol=NSE:AWL)<br><sub>📶W9 · W↑32d · 🚀SS · ↓CMF17d</sub> | ✓ SAFE | Edible oils wheat flour rice pulses sugar FMCG | ⚡ BULL_ANY_PPV | 58 | ↑25 | ↑1.040 | ↑2d | SQ·PV | +6.7% | 12.03/-1.19 | +3.49% | 20% |
| [FACT](https://in.tradingview.com/chart/?symbol=NSE:FACT)<br><sub>📶W9 · 🚀SS·337x · ↑CMF0d</sub> | ✓ SAFE | Nitrogen fertilizer production chemicals agricultural sector south India | ⚡ BULL_ANY_PPV | 49 | 🔄41 | ↑1.080 | ↑1d | PV | +11.7% | -35.53/-49.73 | +11.71% | 20% |
| [SIEMENS](https://in.tradingview.com/chart/?symbol=NSE:SIEMENS)<br><sub>📶W9 · W↑21d · ↑CMF20d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 48 | 🔄74 | ↑1.037 | ↑2d | PV | +5.6% | 36.54/33.96 | +4.54% | 20% |
| [GODREJAGRO](https://in.tradingview.com/chart/?symbol=NSE:GODREJAGRO)<br><sub>📶W9 · W↑7d · RVOL17x · ↑CMF8d</sub> | ✓ SAFE | Animal feed, crop protection, oil palm processing | ⚡ BULL_ANY_PPV | 41 | 🔄39 | ↑1.052 | ↑9d | PV | +10.5% | 26.06/18.3 | +6.52% | 20% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>📶W9 · ↑CMF10d</sub> | ✓ SAFE | Glass-lined reactors pharmaceuticals chemicals process equipment | ⚡ BULL_ANY_PPV | 18 | ↑99 | ↓1.036 | ↑2d | PV | +5.7% | 57.2/56.73 | +0.77% | 5% 🟥 |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>📶W9 · W↑17d · ★ · ↑CMF1d</sub> | ✓ SAFE | Niche APIs formulations contract manufacturing pharma | ⚡ BULL_ANY_PPV | 3 | ↑98 | ↓1.056 | ↑17d | PV | +41.0% | 60.03/59.72 | +0.67% | 20% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>📶W9 · W↑112d · ↑CMF0d</sub> | ✓ SAFE | Electronics manufacturing design integration testing subsystems defense aerospace | ⚡ BULL_ANY_PPV | 0 | ↑98 | ↑1.059 | ↑39d | PV | +65.7% | 61.64/59.11 | +4.55% | 20% |
| [NEPHROPLUS](https://in.tradingview.com/chart/?symbol=NSE:NEPHROPLUS)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Dialysis center chain serving kidney disease patients India | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.009 | ↑1d | SQ | +1.5% | 9.12/8.24 | +1.53% | 20% |
| [NPST](https://in.tradingview.com/chart/?symbol=NSE:NPST)<br><sub>📶W9 · W↑7d · ↑CMF7d</sub> | ✓ SAFE | UPI payments software and real-time transaction processing platform | 📈 BULL_ANY_MID | 99 | 🔄71 | ↑1.014 | ↑1d | SQ | +3.0% | 17.09/16.46 | +2.96% | 10% 🟨 |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Pharmaceutical intermediates and specialty chemicals manufacturer | 📈 BULL_ANY_MID | 94 | 🔄92 | ↑1.024 | ↑1d | SQ | +4.4% | -15.22/-16.21 | +4.42% | 20% |
| [ECLERX](https://in.tradingview.com/chart/?symbol=NSE:ECLERX)<br><sub>📶W9 · W↑42d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | BPM automation analytics for Fortune 2000 financial services retail | 📈 BULL_ANY_MID | 94 | 🔄52 | ↑1.023 | ↑1d | SQ | +3.1% | 4.61/-0.18 | +3.11% | 20% |
| [ALGOQUANT](https://in.tradingview.com/chart/?symbol=NSE:ALGOQUANT)<br><sub>📶W9 · 🚀SS · ↓CMF6d · DEL44%(T-1)</sub> | ✓ SAFE | Algorithmic trading software capital markets quantitative strategies | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.017 | ↑1d | SQ | +2.1% | -8.23/-10.68 | +2.14% | 20% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>📶W9 · W↑52d · ↓CMF7d · DEL28%(T-1)</sub> | ✓ SAFE | Gold jewellery retail, pan-India stores, consumer luxury | 📈 BULL_ANY_MID | 68 | ↑90 | ↑1.014 | ↑2d | SQ | +1.5% | 28.93/23.82 | +0.76% | 20% |
| [GCSL](https://in.tradingview.com/chart/?symbol=NSE:GCSL)<br><sub>📶W9 · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Merchant banking, corporate finance, capital markets advisory | 📈 BULL_ANY_MID | 58 | ↑50 | ↑1.030 | ↑2d | SQ | +7.0% | 0.48/-5.42 | +2.14% | 20% 🟦 |
| [CUB](https://in.tradingview.com/chart/?symbol=NSE:CUB)<br><sub>📶W9 · W↑2d · 🚀SS · ↓CMF2d</sub> | ✓ SAFE | Private bank serving SMEs, MSMEs, retail customers, South India | 📈 BULL_ANY_MID | 54 | 🔄15 | ↑1.022 | ↑1d | — | +4.4% | 12.72/11.75 | +4.43% | 20% |
| [AIIL](https://in.tradingview.com/chart/?symbol=NSE:AIIL)<br><sub>📶W9 · W↑57d · 🚀SS · ↑CMF23d</sub> | ✓ SAFE | NBFC lending and investment securities portfolio management | 📈 BULL_ANY_MID | 54 | 🔄57 | ↑1.017 | ↑1d | — | +2.1% | 3.16/0.66 | +2.12% | 20% |
| [CONFIPET](https://in.tradingview.com/chart/?symbol=NSE:CONFIPET)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | LPG cylinders manufacturing, bottling plants, auto-LPG dispensing stations | 📈 BULL_ANY_MID | 49 | 🔄94 | ↑1.044 | ↑1d | — | +7.9% | -8.23/-12.07 | +7.92% | 10% 🟨 |
| [GANESHHOU](https://in.tradingview.com/chart/?symbol=NSE:GANESHHOU)<br><sub>📶W9 · W↑7d · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | Residential real estate development Ahmedabad Gujarat region | 📈 BULL_ANY_MID | 46 | 🔄59 | ↑1.027 | ↑9d | — | +9.6% | 20.42/19.55 | +3.78% | 20% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>📶W9 · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Dry bulk ship operator maritime logistics cargo transport | 📈 BULL_ANY_MID | 24 | ↑50 | ↑1.016 | ↑1d | — | +1.6% | 7.34/6.53 | +1.61% | 10% 🟩 |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>📶W9 · W↑93d · ↑CMF30d</sub> | ✓ SAFE | Residential and commercial real estate development, Mumbai Pune Bangalore | 📈 BULL_ANY_MID | 18 | ↑69 | ↓1.006 | ↑2d | — | +2.1% | 18.8/16.24 | -0.34% | 20% |
| [LANDMARK](https://in.tradingview.com/chart/?symbol=NSE:LANDMARK)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Premium auto retail, luxury and mass-market vehicles, India | 📈 BULL_ANY_MID | 18 | ↑69 | ↓1.007 | ↓2d | — | +4.7% | -0.68/-4.39 | -2.46% | 20% |
| [BDL](https://in.tradingview.com/chart/?symbol=NSE:BDL)<br><sub>📶W9 · W↑12d · ↑CMF11d</sub> | ✓ SAFE | Guided missiles and defense systems for Indian Armed Forces | 📈 BULL_ANY_MID | 17 | ↑46 | ↓1.007 | ↑3d | — | +3.3% | 38.7/38.45 | -0.59% | 20% |
| [ETHOSLTD](https://in.tradingview.com/chart/?symbol=NSE:ETHOSLTD)<br><sub>📶W9 · W↑67d · ↓CMF5d</sub> | ✓ SAFE | Premium luxury watch retail, multi-brand, Indian affluent consumers | 📈 BULL_ANY_MID | 13 | ↑63 | ↓1.016 | ↑7d | — | +5.4% | 46.32/45.76 | +0.09% | 20% |
| [QUESS](https://in.tradingview.com/chart/?symbol=NSE:QUESS)<br><sub>📶W9 · W↑100d · ↑CMF30d</sub> | ✓ SAFE | Staffing, payroll outsourcing, workforce management for enterprises | 📈 BULL_ANY_MID | 8 | ↑94 | ↑1.031 | ↑12d | — | +11.6% | 58.12/58.07 | +2.48% | 20% |
| [MOL](https://in.tradingview.com/chart/?symbol=NSE:MOL)<br><sub>📶W9 · W↑27d · ↓CMF19d</sub> | ✓ SAFE | Chemical manufacturer: pigments, agrochemicals, crop nutrition | 📈 BULL_ANY_MID | 8 | ↑55 | ↓1.024 | ↑12d | — | +18.8% | 51.96/51.36 | -2.98% | 20% |
| [TBOTEK](https://in.tradingview.com/chart/?symbol=NSE:TBOTEK)<br><sub>📶W9 · W↑67d · ↑CMF0d</sub> | ✓ SAFE | Global travel distribution platform for hotels airlines agents | 📈 BULL_ANY_MID | 5 | ↑77 | ↑1.028 | ↑22d | — | +20.7% | 57.86/57.73 | +1.27% | 20% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>📶W9 · W↑37d · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Gold jewelry manufacturer supplying retailers and boutiques | 📈 BULL_ANY_MID | 2 | ↑99 | ↑1.067 | ↑18d | — | +32.0% | 61.76/60.5 | +5.55% | 20% |
| [RCF](https://in.tradingview.com/chart/?symbol=NSE:RCF)<br><sub>🚀SS·25x · ↓CMF30d · 🔥PHX</sub> | ✓ SAFE | Fertilizer and industrial chemical manufacturer for agriculture | 🔥 BULL_OS_PPV | 54 | 🔄23 | ↑1.021 | ↑1d | PV | +4.6% | -56.73/-65.23 | +4.57% | 20% |
| [DELTACORP](https://in.tradingview.com/chart/?symbol=NSE:DELTACORP)<br><sub>🚀SS · ↓CMF18d · 🎯SLING</sub> | ✓ SAFE | Casinos, hotels, online gaming, entertainment | 🔥 BULL_OS_PPV | 54 | 🔄14 | ↑1.018 | ↑1d | PV | +4.5% | -55.95/-60.76 | +4.48% | 20% |
| [NFL](https://in.tradingview.com/chart/?symbol=NSE:NFL)<br><sub>W↑2d · 🚀SS·18x · ↓CMF30d</sub> | ✓ SAFE | Urea fertilizer production, agricultural inputs, Indian farming | ⚡ BULL_ANY_PPV | 94 | 🔄18 | ↑1.017 | ↑1d | SQ·PV | +2.3% | -23.14/-34.93 | +2.27% | 20% |
| [JINDALPOLY](https://in.tradingview.com/chart/?symbol=NSE:JINDALPOLY)<br><sub>↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄59 | ↑1.008 | ↑1d | SQ | +1.5% | -6.61/-6.66 | +1.53% | 20% |
| [PARKHOSPS](https://in.tradingview.com/chart/?symbol=NSE:PARKHOSPS)<br><sub>↓CMF30d</sub> | ✓ SAFE | Multi-specialty hospital chain North India tertiary quaternary care | 📈 BULL_ANY_MID | 63 | ↑50 | ↑1.016 | ↑2d | SQ | +3.3% | -24.18/-31.03 | +1.07% | 20% |
| [LICHSGFIN](https://in.tradingview.com/chart/?symbol=NSE:LICHSGFIN)<br><sub>↓CMF21d · ÷DIV</sub> | ✓ SAFE | Housing loans for residential property purchase construction | 📈 BULL_ANY_MID | 59 | 🔄27 | ↑1.008 | ↑1d | — | +3.0% | -46.84/-48.5 | +2.97% | 20% |
| [ITCHOTELS](https://in.tradingview.com/chart/?symbol=NSE:ITCHOTELS)<br><sub>🚀SS · ↓CMF27d</sub> | ⚠ CAUTION | Hotel properties operator across luxury segment brands | 📈 BULL_ANY_MID | 59 | 🔄22 | ↑1.003 | ↑1d | — | +1.0% | -18.79/-20.56 | +1.00% | 20% |
| [ICRA](https://in.tradingview.com/chart/?symbol=NSE:ICRA)<br><sub>W↑12d · 🚀SS · ↑CMF11d</sub> | ✓ SAFE | Credit ratings agency serving Indian capital markets debt securities | 📈 BULL_ANY_MID | 54 | 🔄19 | ↑1.017 | ↑1d | — | +2.8% | -13.76/-17.3 | +2.80% | 20% |
| [LINCOLN](https://in.tradingview.com/chart/?symbol=NSE:LINCOLN)<br><sub>W↑7d · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | Injectable antibiotics and cardiac drugs manufacturer | 📈 BULL_ANY_MID | 44 | 🔄50 | ↑1.009 | ↑16d | — | +6.5% | 28.78/27.67 | +0.97% | 20% 🟦 |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:AWL,NSE:FACT,NSE:SIEMENS,NSE:GODREJAGRO,NSE:SETL,NSE:SHILPAMED,NSE:CYIENTDLM,NSE:NEPHROPLUS,NSE:NPST,NSE:ACUTAAS,NSE:ECLERX,NSE:ALGOQUANT,NSE:KALYANKJIL,NSE:GCSL,NSE:CUB,NSE:AIIL,NSE:CONFIPET,NSE:GANESHHOU,NSE:SHREEJISPG,NSE:LODHA,NSE:LANDMARK,NSE:BDL,NSE:ETHOSLTD,NSE:QUESS,NSE:MOL,NSE:TBOTEK,NSE:SKYGOLD,NSE:RCF,NSE:DELTACORP,NSE:NFL,NSE:JINDALPOLY,NSE:PARKHOSPS,NSE:LICHSGFIN,NSE:ITCHOTELS,NSE:ICRA,NSE:LINCOLN
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (19)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>📶W9 · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Spirits manufacturer, IMFL exporter, Indian domestic and export markets | ⚡ BULL_ANY_PPV | 59 | ↑63 | ↑1.036 | ↑1d | SQ·PV | +3.8% | -22.64/-34.57 | +3.78% | 10% 🟩 |
| [AWL](https://in.tradingview.com/chart/?symbol=NSE:AWL)<br><sub>📶W9 · W↑32d · 🚀SS · ↓CMF17d</sub> | ✓ SAFE | Edible oils wheat flour rice pulses sugar FMCG | ⚡ BULL_ANY_PPV | 58 | ↑25 | ↑1.040 | ↑2d | SQ·PV | +6.7% | 12.03/-1.19 | +3.49% | 20% |
| [NEPHROPLUS](https://in.tradingview.com/chart/?symbol=NSE:NEPHROPLUS)<br><sub>📶W9 · ↓CMF4d</sub> | ✓ SAFE | Dialysis center chain serving kidney disease patients India | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.009 | ↑1d | SQ | +1.5% | 9.12/8.24 | +1.53% | 20% |
| [NPST](https://in.tradingview.com/chart/?symbol=NSE:NPST)<br><sub>📶W9 · W↑7d · ↑CMF7d</sub> | ✓ SAFE | UPI payments software and real-time transaction processing platform | 📈 BULL_ANY_MID | 99 | 🔄71 | ↑1.014 | ↑1d | SQ | +3.0% | 17.09/16.46 | +2.96% | 10% 🟨 |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Pharmaceutical intermediates and specialty chemicals manufacturer | 📈 BULL_ANY_MID | 94 | 🔄92 | ↑1.024 | ↑1d | SQ | +4.4% | -15.22/-16.21 | +4.42% | 20% |
| [ECLERX](https://in.tradingview.com/chart/?symbol=NSE:ECLERX)<br><sub>📶W9 · W↑42d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | BPM automation analytics for Fortune 2000 financial services retail | 📈 BULL_ANY_MID | 94 | 🔄52 | ↑1.023 | ↑1d | SQ | +3.1% | 4.61/-0.18 | +3.11% | 20% |
| [ALGOQUANT](https://in.tradingview.com/chart/?symbol=NSE:ALGOQUANT)<br><sub>📶W9 · 🚀SS · ↓CMF6d · DEL44%(T-1)</sub> | ✓ SAFE | Algorithmic trading software capital markets quantitative strategies | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.017 | ↑1d | SQ | +2.1% | -8.23/-10.68 | +2.14% | 20% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>📶W9 · W↑52d · ↓CMF7d · DEL28%(T-1)</sub> | ✓ SAFE | Gold jewellery retail, pan-India stores, consumer luxury | 📈 BULL_ANY_MID | 68 | ↑90 | ↑1.014 | ↑2d | SQ | +1.5% | 28.93/23.82 | +0.76% | 20% |
| [INDUSINDBK](https://in.tradingview.com/chart/?symbol=NSE:INDUSINDBK)<br><sub>📶W9 · ↑CMF30d</sub> | ⚠ CAUTION | Private bank vehicle finance microfinance retail lending | 📈 BULL_ANY_MID | 58 | ↓67 | ↓1.000 | ↓2d | SQ | +0.9% | -10.22/-11.04 | -0.33% | 20% |
| [GCSL](https://in.tradingview.com/chart/?symbol=NSE:GCSL)<br><sub>📶W9 · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Merchant banking, corporate finance, capital markets advisory | 📈 BULL_ANY_MID | 58 | ↑50 | ↑1.030 | ↑2d | SQ | +7.0% | 0.48/-5.42 | +2.14% | 20% 🟦 |
| [NFL](https://in.tradingview.com/chart/?symbol=NSE:NFL)<br><sub>W↑2d · 🚀SS·18x · ↓CMF30d</sub> | ✓ SAFE | Urea fertilizer production, agricultural inputs, Indian farming | ⚡ BULL_ANY_PPV | 94 | 🔄18 | ↑1.017 | ↑1d | SQ·PV | +2.3% | -23.14/-34.93 | +2.27% | 20% |
| [BRIGHOTEL](https://in.tradingview.com/chart/?symbol=NSE:BRIGHOTEL)<br><sub>RVOL9x · ↓CMF30d · ⚠️TRAP · ÷DIV</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 58 | ↓16 | ↑0.992 | ↓7d | SQ·PV | -0.5% | -26.94/-28.19 | +0.20% | 20% |
| [RAMCOCEM](https://in.tradingview.com/chart/?symbol=NSE:RAMCOCEM)<br><sub>🚀SS · ↓CMF21d</sub> | ⚠ CAUTION | Cement producer, RMC, dry mortar for construction | ⚡ BULL_ANY_PPV | 51 | ↓24 | ↑0.998 | ↓14d | SQ·PV | -1.4% | -21.41/-23.19 | +0.58% | 20% |
| [JINDALPOLY](https://in.tradingview.com/chart/?symbol=NSE:JINDALPOLY)<br><sub>↓CMF30d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 99 | 🔄59 | ↑1.008 | ↑1d | SQ | +1.5% | -6.61/-6.66 | +1.53% | 20% |
| [PARKHOSPS](https://in.tradingview.com/chart/?symbol=NSE:PARKHOSPS)<br><sub>↓CMF30d</sub> | ✓ SAFE | Multi-specialty hospital chain North India tertiary quaternary care | 📈 BULL_ANY_MID | 63 | ↑50 | ↑1.016 | ↑2d | SQ | +3.3% | -24.18/-31.03 | +1.07% | 20% |
| [HAWKINCOOK](https://in.tradingview.com/chart/?symbol=NSE:HAWKINCOOK)<br><sub>↓CMF19d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 50 | ↓50 | ↑1.002 | ↓60d+ | SQ | +11.2% | -46.49/-48.81 | +0.61% | 20% |
| [CAPITALSFB](https://in.tradingview.com/chart/?symbol=NSE:CAPITALSFB)<br><sub>🚀SS · ↓CMF7d</sub> | ⚠ CAUTION | Retail banking microfinance credit middle-income underserved segments | 📈 BULL_ANY_MID | 50 | ↓47 | ↑1.001 | ↓20d | SQ | -2.8% | -47.25/-49.05 | +0.89% | 20% |
| [HDFCAMC](https://in.tradingview.com/chart/?symbol=NSE:HDFCAMC)<br><sub>↓CMF23d · ⚠️TRAP</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 47 | ↓26 | ↓0.996 | ↓13d | SQ | -1.4% | -43.83/-45.68 | -0.45% | 20% |
| [VENUSPIPES](https://in.tradingview.com/chart/?symbol=NSE:VENUSPIPES)<br><sub>🚀SS · ↓CMF26d · ⚠️TRAP</sub> | ✓ SAFE | Stainless steel pipes tubes manufacturing chemicals pharmaceuticals | 📈 BULL_ANY_MID | 45 | ↓71 | ↑0.989 | ↓53d | SQ | +14.7% | -50.09/-51.58 | -0.02% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:AWL,NSE:NEPHROPLUS,NSE:NPST,NSE:ACUTAAS,NSE:ECLERX,NSE:ALGOQUANT,NSE:KALYANKJIL,NSE:INDUSINDBK,NSE:GCSL,NSE:NFL,NSE:BRIGHOTEL,NSE:RAMCOCEM,NSE:JINDALPOLY,NSE:PARKHOSPS,NSE:HAWKINCOOK,NSE:CAPITALSFB,NSE:HDFCAMC,NSE:VENUSPIPES
```

---

### 🔥 MAJOR — PPV confirmed (9)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [FACT](https://in.tradingview.com/chart/?symbol=NSE:FACT)<br><sub>📶W9 · 🚀SS·337x · ↑CMF0d</sub> | ✓ SAFE | Nitrogen fertilizer production chemicals agricultural sector south India | ⚡ BULL_ANY_PPV | 49 | 🔄41 | ↑1.080 | ↑1d | PV | +11.7% | -35.53/-49.73 | +11.71% | 20% |
| [SIEMENS](https://in.tradingview.com/chart/?symbol=NSE:SIEMENS)<br><sub>📶W9 · W↑21d · ↑CMF20d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 48 | 🔄74 | ↑1.037 | ↑2d | PV | +5.6% | 36.54/33.96 | +4.54% | 20% |
| [GODREJAGRO](https://in.tradingview.com/chart/?symbol=NSE:GODREJAGRO)<br><sub>📶W9 · W↑7d · RVOL17x · ↑CMF8d</sub> | ✓ SAFE | Animal feed, crop protection, oil palm processing | ⚡ BULL_ANY_PPV | 41 | 🔄39 | ↑1.052 | ↑9d | PV | +10.5% | 26.06/18.3 | +6.52% | 20% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>📶W9 · ↑CMF10d</sub> | ✓ SAFE | Glass-lined reactors pharmaceuticals chemicals process equipment | ⚡ BULL_ANY_PPV | 18 | ↑99 | ↓1.036 | ↑2d | PV | +5.7% | 57.2/56.73 | +0.77% | 5% 🟥 |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>📶W9 · W↑17d · ★ · ↑CMF1d</sub> | ✓ SAFE | Niche APIs formulations contract manufacturing pharma | ⚡ BULL_ANY_PPV | 3 | ↑98 | ↓1.056 | ↑17d | PV | +41.0% | 60.03/59.72 | +0.67% | 20% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>📶W9 · W↑112d · ↑CMF0d</sub> | ✓ SAFE | Electronics manufacturing design integration testing subsystems defense aerospace | ⚡ BULL_ANY_PPV | 0 | ↑98 | ↑1.059 | ↑39d | PV | +65.7% | 61.64/59.11 | +4.55% | 20% |
| [RCF](https://in.tradingview.com/chart/?symbol=NSE:RCF)<br><sub>🚀SS·25x · ↓CMF30d · 🔥PHX</sub> | ✓ SAFE | Fertilizer and industrial chemical manufacturer for agriculture | 🔥 BULL_OS_PPV | 54 | 🔄23 | ↑1.021 | ↑1d | PV | +4.6% | -56.73/-65.23 | +4.57% | 20% |
| [DELTACORP](https://in.tradingview.com/chart/?symbol=NSE:DELTACORP)<br><sub>🚀SS · ↓CMF18d · 🎯SLING</sub> | ✓ SAFE | Casinos, hotels, online gaming, entertainment | 🔥 BULL_OS_PPV | 54 | 🔄14 | ↑1.018 | ↑1d | PV | +4.5% | -55.95/-60.76 | +4.48% | 20% |
| [ROUTE](https://in.tradingview.com/chart/?symbol=NSE:ROUTE)<br><sub>↓CMF23d</sub> | ✓ SAFE | Cloud messaging platform for enterprises and telecom operators | ⚡ BULL_ANY_PPV | 5 | ↓16 | ↑0.999 | ↓34d | PV | -4.9% | -47.95/-48.21 | +2.91% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:FACT,NSE:SIEMENS,NSE:GODREJAGRO,NSE:SETL,NSE:SHILPAMED,NSE:CYIENTDLM,NSE:RCF,NSE:DELTACORP,NSE:ROUTE
```

### 🟢 OVERSOLD — reversal from −53/−60 (13)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [UGROCAP](https://in.tradingview.com/chart/?symbol=NSE:UGROCAP)<br><sub>↓CMF16d · ⚠️TRAP</sub> | ✓ SAFE | MSME lending platform, technology-driven credit scoring | 🟢 BULL_OVERSOLD | 13 | ↓2 | ↑0.977 | ↓12d | — | -7.4% | -62.94/-63.11 | -0.17% | 20% |
| [STARCEMENT](https://in.tradingview.com/chart/?symbol=NSE:STARCEMENT)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Cement manufacturing and distribution northeast eastern India | 🟢 BULL_OVERSOLD | 10 | ↓12 | ↑0.990 | ↓15d | — | -4.4% | -69.0/-69.86 | -0.01% | 20% |
| [METROBRAND](https://in.tradingview.com/chart/?symbol=NSE:METROBRAND)<br><sub>↓CMF13d · 🎯SLING</sub> | ⚠ CAUTION | Footwear accessories retail branded shoes family segments | 🟢 BULL_OVERSOLD | 9 | ↓13 | ↑0.989 | ↓16d | — | -10.9% | -59.98/-61.29 | +1.34% | 20% |
| [ABLBL](https://in.tradingview.com/chart/?symbol=NSE:ABLBL)<br><sub>🚀SS · ↓CMF11d · 🎯SLING</sub> | ⚠ CAUTION | Premium western apparel brands for urban consumers | 🟢 BULL_OVERSOLD | 8 | ↓4 | ↑0.974 | ↓17d | — | -9.8% | -75.5/-75.67 | +0.36% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>🚀SS · ↑CMF15d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 5 | ↓37 | ↑0.997 | ↓60d+ | — | -11.4% | -58.82/-63.69 | +0.06% | 20% |
| [TORNTPOWER](https://in.tradingview.com/chart/?symbol=NSE:TORNTPOWER)<br><sub>↓CMF15d · ⚠️TRAP</sub> | ⚠ CAUTION | Power generation transmission distribution utility company | 🟢 BULL_OVERSOLD | 5 | ↓20 | ↑0.976 | ↓27d | — | -10.5% | -64.88/-65.53 | -0.19% | 20% |
| [EPACK](https://in.tradingview.com/chart/?symbol=NSE:EPACK)<br><sub>↓CMF13d · ⚠️TRAP</sub> | ✓ SAFE | Room air conditioner ODM manufacturer for Indian consumer market | 🟢 BULL_OVERSOLD | 5 | ↓4 | ↑0.959 | ↓33d | — | -13.2% | -72.04/-72.41 | -0.69% | 20% |
| [SIKA](https://in.tradingview.com/chart/?symbol=NSE:SIKA)<br><sub>↓CMF5d · ⚠️TRAP</sub> | ✓ SAFE | Aerospace defense space automotive engineering systems provider | 🟢 BULL_OVERSOLD | 0 | ↓50 | ↓0.977 | ↓26d | — | -9.6% | -61.05/-61.6 | -1.51% | 20% |
| [SAGCEM](https://in.tradingview.com/chart/?symbol=NSE:SAGCEM)<br><sub>↓CMF1d · ⚠️TRAP</sub> | ⚠ CAUTION | Cement manufacturing, South and Central India construction | 🟢 BULL_OVERSOLD | 0 | ↓9 | ↓0.980 | ↓22d | — | -8.0% | -61.76/-61.9 | -1.17% | 20% |
| [ICEMAKE](https://in.tradingview.com/chart/?symbol=NSE:ICEMAKE)<br><sub>↓CMF20d · ⚠️TRAP</sub> | ✓ SAFE | Refrigeration equipment manufacturer for commercial cold storage operations | 🟡 BULL_OS_L2 | 15 | ↓28 | ↑0.974 | ↓10d | — | -10.5% | -53.05/-53.34 | +0.01% | 20% |
| [EIEL](https://in.tradingview.com/chart/?symbol=NSE:EIEL)<br><sub>↓CMF12d · ⚠️TRAP</sub> | ✓ SAFE | Water treatment plants design construction operations municipalities | 🟡 BULL_OS_L2 | 8 | ↓37 | ↑0.976 | ↓17d | — | -11.5% | -58.33/-58.33 | -0.31% | 20% |
| [ORIENTTECH](https://in.tradingview.com/chart/?symbol=NSE:ORIENTTECH)<br><sub>↓CMF18d · 🎯SLING</sub> | ✓ SAFE | IT infrastructure cloud services digital transformation solutions | 🟡 BULL_OS_L2 | 5 | ↓13 | ↑0.987 | ↓22d | — | -5.2% | -56.03/-57.02 | +0.47% | 20% |
| [HUDCO](https://in.tradingview.com/chart/?symbol=NSE:HUDCO)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Housing finance and urban infrastructure development public sector | 🟡 BULL_OS_L2 | 4 | ↓20 | ↓0.984 | ↓16d | — | -6.6% | -55.34/-55.75 | -0.70% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:UGROCAP,NSE:STARCEMENT,NSE:METROBRAND,NSE:ABLBL,NSE:COALINDIA,NSE:TORNTPOWER,NSE:EPACK,NSE:SIKA,NSE:SAGCEM,NSE:ICEMAKE,NSE:EIEL,NSE:ORIENTTECH,NSE:HUDCO
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (28)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CUB](https://in.tradingview.com/chart/?symbol=NSE:CUB)<br><sub>📶W9 · W↑2d · 🚀SS · ↓CMF2d</sub> | ✓ SAFE | Private bank serving SMEs, MSMEs, retail customers, South India | 📈 BULL_ANY_MID | 54 | 🔄15 | ↑1.022 | ↑1d | — | +4.4% | 12.72/11.75 | +4.43% | 20% |
| [AIIL](https://in.tradingview.com/chart/?symbol=NSE:AIIL)<br><sub>📶W9 · W↑57d · 🚀SS · ↑CMF23d</sub> | ✓ SAFE | NBFC lending and investment securities portfolio management | 📈 BULL_ANY_MID | 54 | 🔄57 | ↑1.017 | ↑1d | — | +2.1% | 3.16/0.66 | +2.12% | 20% |
| [CONFIPET](https://in.tradingview.com/chart/?symbol=NSE:CONFIPET)<br><sub>📶W9 · ↓CMF10d</sub> | ✓ SAFE | LPG cylinders manufacturing, bottling plants, auto-LPG dispensing stations | 📈 BULL_ANY_MID | 49 | 🔄94 | ↑1.044 | ↑1d | — | +7.9% | -8.23/-12.07 | +7.92% | 10% 🟨 |
| [GANESHHOU](https://in.tradingview.com/chart/?symbol=NSE:GANESHHOU)<br><sub>📶W9 · W↑7d · 🚀SS · ↑CMF3d</sub> | ✓ SAFE | Residential real estate development Ahmedabad Gujarat region | 📈 BULL_ANY_MID | 46 | 🔄59 | ↑1.027 | ↑9d | — | +9.6% | 20.42/19.55 | +3.78% | 20% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>📶W9 · 🚀SS · ↓CMF6d</sub> | ✓ SAFE | Dry bulk ship operator maritime logistics cargo transport | 📈 BULL_ANY_MID | 24 | ↑50 | ↑1.016 | ↑1d | — | +1.6% | 7.34/6.53 | +1.61% | 10% 🟩 |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>📶W9 · W↑93d · ↑CMF30d</sub> | ✓ SAFE | Residential and commercial real estate development, Mumbai Pune Bangalore | 📈 BULL_ANY_MID | 18 | ↑69 | ↓1.006 | ↑2d | — | +2.1% | 18.8/16.24 | -0.34% | 20% |
| [LANDMARK](https://in.tradingview.com/chart/?symbol=NSE:LANDMARK)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Premium auto retail, luxury and mass-market vehicles, India | 📈 BULL_ANY_MID | 18 | ↑69 | ↓1.007 | ↓2d | — | +4.7% | -0.68/-4.39 | -2.46% | 20% |
| [BDL](https://in.tradingview.com/chart/?symbol=NSE:BDL)<br><sub>📶W9 · W↑12d · ↑CMF11d</sub> | ✓ SAFE | Guided missiles and defense systems for Indian Armed Forces | 📈 BULL_ANY_MID | 17 | ↑46 | ↓1.007 | ↑3d | — | +3.3% | 38.7/38.45 | -0.59% | 20% |
| [ETHOSLTD](https://in.tradingview.com/chart/?symbol=NSE:ETHOSLTD)<br><sub>📶W9 · W↑67d · ↓CMF5d</sub> | ✓ SAFE | Premium luxury watch retail, multi-brand, Indian affluent consumers | 📈 BULL_ANY_MID | 13 | ↑63 | ↓1.016 | ↑7d | — | +5.4% | 46.32/45.76 | +0.09% | 20% |
| [QUESS](https://in.tradingview.com/chart/?symbol=NSE:QUESS)<br><sub>📶W9 · W↑100d · ↑CMF30d</sub> | ✓ SAFE | Staffing, payroll outsourcing, workforce management for enterprises | 📈 BULL_ANY_MID | 8 | ↑94 | ↑1.031 | ↑12d | — | +11.6% | 58.12/58.07 | +2.48% | 20% |
| [MOL](https://in.tradingview.com/chart/?symbol=NSE:MOL)<br><sub>📶W9 · W↑27d · ↓CMF19d</sub> | ✓ SAFE | Chemical manufacturer: pigments, agrochemicals, crop nutrition | 📈 BULL_ANY_MID | 8 | ↑55 | ↓1.024 | ↑12d | — | +18.8% | 51.96/51.36 | -2.98% | 20% |
| [TBOTEK](https://in.tradingview.com/chart/?symbol=NSE:TBOTEK)<br><sub>📶W9 · W↑67d · ↑CMF0d</sub> | ✓ SAFE | Global travel distribution platform for hotels airlines agents | 📈 BULL_ANY_MID | 5 | ↑77 | ↑1.028 | ↑22d | — | +20.7% | 57.86/57.73 | +1.27% | 20% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>📶W9 · W↑37d · 🚀SS · ↓CMF15d</sub> | ✓ SAFE | Gold jewelry manufacturer supplying retailers and boutiques | 📈 BULL_ANY_MID | 2 | ↑99 | ↑1.067 | ↑18d | — | +32.0% | 61.76/60.5 | +5.55% | 20% |
| [LICHSGFIN](https://in.tradingview.com/chart/?symbol=NSE:LICHSGFIN)<br><sub>↓CMF21d · ÷DIV</sub> | ✓ SAFE | Housing loans for residential property purchase construction | 📈 BULL_ANY_MID | 59 | 🔄27 | ↑1.008 | ↑1d | — | +3.0% | -46.84/-48.5 | +2.97% | 20% |
| [ITCHOTELS](https://in.tradingview.com/chart/?symbol=NSE:ITCHOTELS)<br><sub>🚀SS · ↓CMF27d</sub> | ⚠ CAUTION | Hotel properties operator across luxury segment brands | 📈 BULL_ANY_MID | 59 | 🔄22 | ↑1.003 | ↑1d | — | +1.0% | -18.79/-20.56 | +1.00% | 20% |
| [ICRA](https://in.tradingview.com/chart/?symbol=NSE:ICRA)<br><sub>W↑12d · 🚀SS · ↑CMF11d</sub> | ✓ SAFE | Credit ratings agency serving Indian capital markets debt securities | 📈 BULL_ANY_MID | 54 | 🔄19 | ↑1.017 | ↑1d | — | +2.8% | -13.76/-17.3 | +2.80% | 20% |
| [LINCOLN](https://in.tradingview.com/chart/?symbol=NSE:LINCOLN)<br><sub>W↑7d · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | Injectable antibiotics and cardiac drugs manufacturer | 📈 BULL_ANY_MID | 44 | 🔄50 | ↑1.009 | ↑16d | — | +6.5% | 28.78/27.67 | +0.97% | 20% 🟦 |
| [VOLTAS](https://in.tradingview.com/chart/?symbol=NSE:VOLTAS)<br><sub>↓CMF11d · ⚠️TRAP</sub> | ✓ SAFE | AC manufacturer, refrigeration, EPC projects contractor | 📈 BULL_ANY_MID | 17 | ↓26 | ↑0.992 | ↓8d | — | -3.6% | -50.79/-50.88 | +0.08% | 20% |
| [GPTINFRA](https://in.tradingview.com/chart/?symbol=NSE:GPTINFRA)<br><sub>🚀SS · ↓CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 15 | ↓37 | ↑0.999 | ↓10d | — | -1.9% | -43.34/-44.79 | +0.87% | 20% |
| [SURYAROSNI](https://in.tradingview.com/chart/?symbol=NSE:SURYAROSNI)<br><sub>↓CMF30d</sub> | ✓ SAFE | Steel pipes, GI tubes, lighting fixtures manufacturing | 📈 BULL_ANY_MID | 10 | ↓19 | ↑0.986 | ↓15d | — | -7.5% | -44.4/-44.6 | +0.50% | 20% |
| [RAMCOSYS](https://in.tradingview.com/chart/?symbol=NSE:RAMCOSYS)<br><sub>↓CMF21d · ⚠️TRAP</sub> | ✓ SAFE | ERP software, HCM, aerospace supply chain management | 📈 BULL_ANY_MID | 8 | ↓66 | ↓0.969 | ↓12d | — | -12.5% | -45.84/-46.17 | -2.09% | 10% 🟨 |
| [HARIOMPIPE](https://in.tradingview.com/chart/?symbol=NSE:HARIOMPIPE)<br><sub>↓CMF30d</sub> | ✓ SAFE | Steel pipe and scaffolding systems manufacturer for construction | 📈 BULL_ANY_MID | 8 | ↓19 | ↑0.977 | ↓17d | — | -10.6% | -48.12/-48.4 | +0.26% | 20% |
| [SANSTAR](https://in.tradingview.com/chart/?symbol=NSE:SANSTAR)<br><sub>↓CMF17d</sub> | ✓ SAFE | Maize starch derivatives food animal nutrition industrial | 📈 BULL_ANY_MID | 8 | ↓56 | ↑0.997 | ↓17d | — | -3.4% | -43.41/-43.66 | +1.26% | 20% |
| [SUNPHARMA](https://in.tradingview.com/chart/?symbol=NSE:SUNPHARMA)<br><sub>↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 5 | ↓56 | ↑0.999 | ↓48d | — | +6.1% | -33.13/-33.88 | +0.40% | 20% |
| [TTKPRESTIG](https://in.tradingview.com/chart/?symbol=NSE:TTKPRESTIG)<br><sub>↓CMF0d</sub> | ✓ SAFE | Pressure cookers, cookware, kitchen appliances for households | 📈 BULL_ANY_MID | 5 | ↓45 | ↑0.998 | ↓22d | — | -7.4% | -36.85/-37.74 | +1.30% | 20% |
| [DEEPAKFERT](https://in.tradingview.com/chart/?symbol=NSE:DEEPAKFERT)<br><sub>↓CMF19d · ⚠️TRAP</sub> | ✓ SAFE | Fertilizers, bulk chemicals, mining chemicals, crop nutrition | 📈 BULL_ANY_MID | 4 | ↓58 | ↓0.987 | ↓16d | — | -7.4% | -40.54/-41.29 | -1.09% | 20% |
| [NHPC](https://in.tradingview.com/chart/?symbol=NSE:NHPC)<br><sub>↓CMF21d · ⚠️TRAP</sub> | ⚠ CAUTION | Hydroelectric power generation and renewable energy utilities | 📈 BULL_ANY_MID | 3 | ↓37 | ↓0.998 | ↓17d | — | -2.7% | -39.01/-40.38 | -0.04% | 20% |
| [JKTYRE](https://in.tradingview.com/chart/?symbol=NSE:JKTYRE)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Radial tyres for cars, trucks, two-wheelers | 📈 BULL_ANY_MID | 3 | ↓24 | ↓0.996 | ↓17d | — | -4.8% | -33.36/-35.35 | -0.51% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CUB,NSE:AIIL,NSE:CONFIPET,NSE:GANESHHOU,NSE:SHREEJISPG,NSE:LODHA,NSE:LANDMARK,NSE:BDL,NSE:ETHOSLTD,NSE:QUESS,NSE:MOL,NSE:TBOTEK,NSE:SKYGOLD,NSE:LICHSGFIN,NSE:ITCHOTELS,NSE:ICRA,NSE:LINCOLN,NSE:VOLTAS,NSE:GPTINFRA,NSE:SURYAROSNI,NSE:RAMCOSYS,NSE:HARIOMPIPE,NSE:SANSTAR,NSE:SUNPHARMA,NSE:TTKPRESTIG,NSE:DEEPAKFERT,NSE:NHPC,NSE:JKTYRE
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
