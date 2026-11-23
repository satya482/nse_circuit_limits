> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-11-23
*Generated 2026-11-23 15:48 IST*

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

**Total bull crosses today: 73** · 33 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ACMESOLAR,NSE:PGHL,NSE:SAMBHV,NSE:LALPATHLAB,NSE:ITI,NSE:INSECTICID,NSE:CANFINHOME,NSE:SWSOLAR,NSE:HITECH,NSE:SUDEEPPHRM,NSE:STEL,NSE:REGAAL,NSE:SIGMAADV,NSE:PTCIL,NSE:5PAISA,NSE:CHOICEIN,NSE:PGHH,NSE:ONESOURCE,NSE:SURYAROSNI,NSE:PENIND,NSE:MPHASIS,NSE:TATAELXSI,NSE:STARHEALTH,NSE:TATACONSUM,NSE:ANTHEM,NSE:EICHERMOT,NSE:AKCAPIT,NSE:SYNGENE,NSE:JSWCEMENT,NSE:ORIENTHOT,NSE:TCIEXP,NSE:BENGALASM,NSE:KUSUMGAR,NSE:JSLL,NSE:INDIAGLYCO,NSE:VMM,NSE:JTLIND,NSE:POLICYBZR,NSE:LATENTVIEW,NSE:RISHABH,NSE:POCL,NSE:RRKABEL,NSE:UNIVCABLES,NSE:NAUKRI,NSE:HUBTOWN,NSE:3BBLACKBIO,NSE:AFCONS,NSE:SEDEMAC,NSE:SAATVIKGL,NSE:IDEAFORGE,NSE:ELANTAS,NSE:GEOJITFSL,NSE:ABBOTINDIA,NSE:DBL,NSE:AVADHSUGAR,NSE:IRMENERGY,NSE:VENTIVE,NSE:PTC,NSE:MOIL,NSE:GUJENERGY,NSE:EIHAHOTELS,NSE:DEEPINDS,NSE:NRAIL,NSE:SANGHVIMOV,NSE:CHENNPETRO,NSE:SUPRAJIT,NSE:SULA,NSE:SBICARD,NSE:LANDMARK,NSE:M&MFIN,NSE:APARINDS,NSE:ECLERX,NSE:HEXT
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (30)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>📶W9 · 🚀SS · ↓CMF26d</sub> | ✓ SAFE | Solar and wind power plants for Indian utilities | ⚡ BULL_ANY_PPV | 99 | 🔄91 | ↑1.006 | ↑1d | SQ·PV | +1.5% | -5.75/-7.68 | +1.53% | 20% |
| [PGHL](https://in.tradingview.com/chart/?symbol=NSE:PGHL)<br><sub>📶W9 · W↑16d · 🚀SS · ↑CMF18d</sub> | ⚠ CAUTION | Vitamins minerals supplements pharmaceuticals consumer health | ⚡ BULL_ANY_PPV | 93 | 🔄58 | ↑1.018 | ↑2d | SQ·PV | +3.4% | 10.56/6.64 | +2.42% | 20% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>📶W9 · 🚀SS·11x · ↑CMF0d</sub> | ✓ SAFE | ERW steel pipes, tubes, structural hollow sections manufacturer | ⚡ BULL_ANY_PPV | 89 | 🔄96 | ↑1.072 | ↑1d | SQ·PV | +11.9% | 6.23/1.78 | +11.92% | 20% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>📶W9 · W↑10d · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Diagnostic lab network pathology testing healthcare services | ⚡ BULL_ANY_PPV | 63 | ↑83 | ↑1.024 | ↑2d | SQ·PV | +3.9% | 30.47/25.43 | +1.72% | 20% |
| [ITI](https://in.tradingview.com/chart/?symbol=NSE:ITI)<br><sub>📶W9 · W↑16d · 🚀SS·14x · ↑CMF15d</sub> | ✓ SAFE | Telecom equipment manufacturing, cables, defense electronics | ⚡ BULL_ANY_PPV | 49 | 🔄48 | ↑1.085 | ↑1d | PV | +12.4% | 16.45/9.51 | +12.41% | 20% |
| [INSECTICID](https://in.tradingview.com/chart/?symbol=NSE:INSECTICID)<br><sub>📶W9 · W↑6d · ↑CMF4d · ÷DIV</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 49 | 🔄36 | ↑1.042 | ↑1d | PV | +6.1% | -8.89/-16.67 | +6.12% | 20% |
| [CANFINHOME](https://in.tradingview.com/chart/?symbol=NSE:CANFINHOME)<br><sub>📶W9 · W↑16d · 🚀SS · ↑CMF20d</sub> | ⚠ CAUTION | Housing loans for affordable home buyers salaried middle class | ⚡ BULL_ANY_PPV | 42 | 🔄45 | ↑1.029 | ↑13d | PV | +9.8% | 48.07/45.41 | +3.30% | 20% |
| [SWSOLAR](https://in.tradingview.com/chart/?symbol=NSE:SWSOLAR)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF2d</sub> | ✓ SAFE | Solar EPC contractor, develops utility-scale projects globally | ⚡ BULL_ANY_PPV | 41 | 🔄14 | ↑1.030 | ↑14d | PV | +14.2% | 15.68/12.39 | +4.41% | 20% |
| [HITECH](https://in.tradingview.com/chart/?symbol=NSE:HITECH)<br><sub>📶W9 · W↑16d · 🚀SS·31x · ↑CMF1d</sub> | ✓ SAFE | ERW steel pipes tubes construction automotive infrastructure | ⚡ BULL_ANY_PPV | 32 | 🔄59 | ↑1.107 | ↑18d | PV | +33.0% | 33.83/21.18 | +13.51% | 20% |
| [SUDEEPPHRM](https://in.tradingview.com/chart/?symbol=NSE:SUDEEPPHRM)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Calcium phosphate excipients pharma food nutrition | ⚡ BULL_ANY_PPV | 31 | 🔄50 | ↑1.041 | ↑19d | PV | +22.3% | 37.34/32.74 | +4.91% | 10% 🟩 |
| [STEL](https://in.tradingview.com/chart/?symbol=NSE:STEL)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF8d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 10 | ↑83 | ↑1.055 | ↑10d | PV | +25.2% | 41.77/39.89 | +4.00% | 20% |
| [REGAAL](https://in.tradingview.com/chart/?symbol=NSE:REGAAL)<br><sub>📶W9 · W↑26d · ↓CMF24d</sub> | ✓ SAFE | Maize starch processor serving food beverage pharmaceutical industries | ⚡ BULL_ANY_PPV | 7 | ↑84 | ↓1.047 | ↑13d | PV | +15.6% | 58.1/55.63 | +1.02% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Precision metal components aerospace defense oil-gas marine | 📈 BULL_ANY_MID | 99 | 🔄87 | ↑1.012 | ↑1d | SQ | +1.3% | -10.84/-15.14 | +1.26% | 20% |
| [5PAISA](https://in.tradingview.com/chart/?symbol=NSE:5PAISA)<br><sub>📶W9 · W↑10d · ↑CMF3d</sub> | ⚠ CAUTION | Digital discount brokerage for equities, derivatives, commodities trading | 📈 BULL_ANY_MID | 95 | 🔄56 | ↑1.013 | ↑5d | SQ | +3.4% | 22.75/22.46 | +1.84% | 20% |
| [CHOICEIN](https://in.tradingview.com/chart/?symbol=NSE:CHOICEIN)<br><sub>📶W9 · W↑10d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Stockbroking wealth management MSME lending insurance distribution financial services | 📈 BULL_ANY_MID | 94 | 🔄54 | ↑1.022 | ↑1d | SQ | +2.7% | -10.0/-14.88 | +2.71% | 20% |
| [PGHH](https://in.tradingview.com/chart/?symbol=NSE:PGHH)<br><sub>📶W9 · W↑31d · 🚀SS · ↓CMF15d</sub> | ⚠ CAUTION | Feminine hygiene pads, health products, Indian consumer market | 📈 BULL_ANY_MID | 93 | 🔄8 | ↑1.026 | ↑2d | SQ | +4.1% | 12.27/4.19 | +2.65% | 20% |
| [ONESOURCE](https://in.tradingview.com/chart/?symbol=NSE:ONESOURCE)<br><sub>📶W9 · W↑16d · ↑CMF20d</sub> | ✓ SAFE | Specialty pharma CDMO injectable biologics contract manufacturing | 📈 BULL_ANY_MID | 70 | 🔄63 | ↓1.003 | ↑20d | SQ | +14.6% | 18.11/17.86 | -0.47% | 20% |
| [SURYAROSNI](https://in.tradingview.com/chart/?symbol=NSE:SURYAROSNI)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF2d</sub> | ✓ SAFE | Steel pipes, GI products, lighting fixtures for infrastructure | 📈 BULL_ANY_MID | 63 | ↑40 | ↑1.018 | ↑2d | SQ | +3.1% | 15.71/10.93 | +1.27% | 20% |
| [PENIND](https://in.tradingview.com/chart/?symbol=NSE:PENIND)<br><sub>📶W9 · W↑1d · ↓CMF30d</sub> | ✓ SAFE | Steel structures, hydraulics, warehousing for infrastructure mobility energy | 📈 BULL_ANY_MID | 63 | ↑58 | ↑1.024 | ↑2d | SQ | +3.9% | 6.12/-0.04 | +1.17% | 20% |
| [MPHASIS](https://in.tradingview.com/chart/?symbol=NSE:MPHASIS)<br><sub>📶W9 · 🚀SS · ↓CMF11d</sub> | ✓ SAFE | IT services, cloud and cognitive transformation, enterprise clients | 📈 BULL_ANY_MID | 59 | 🔄60 | ↑1.013 | ↑1d | — | +2.0% | -21.48/-24.49 | +2.00% | 20% |
| [TATAELXSI](https://in.tradingview.com/chart/?symbol=NSE:TATAELXSI)<br><sub>📶W9 · W↑31d · ↓CMF0d</sub> | ✓ SAFE | Design engineering services for automotive media healthcare | 📈 BULL_ANY_MID | 58 | ↑39 | ↓1.009 | ↑2d | SQ | +2.6% | 8.67/4.26 | -0.72% | 20% |
| [STARHEALTH](https://in.tradingview.com/chart/?symbol=NSE:STARHEALTH)<br><sub>📶W9 · W↑10d · ↓CMF15d · ÷DIV</sub> | ✓ SAFE | Health insurance provider, retail customers, India | 📈 BULL_ANY_MID | 56 | 🔄67 | ↑1.008 | ↑4d | — | +2.7% | 16.86/16.85 | +1.45% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄55 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>📶W9 · W↑10d · ★ · ↑CMF21d</sub> | ✓ SAFE | Contract research development manufacturing biotech pharma | 📈 BULL_ANY_MID | 9 | ↑84 | ↑1.026 | ↑16d | — | +15.5% | 40.1/36.89 | +0.66% | 20% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>📶W9 · W↑11d · ↑CMF13d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓60 | ↓1.007 | ↑15d | — | +7.0% | 46.27/45.57 | -0.67% | 20% |
| [AKCAPIT](https://in.tradingview.com/chart/?symbol=NSE:AKCAPIT)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 4 | ↑50 | ↑1.065 | ↑16d | — | +21.2% | 72.5/71.67 | +4.52% | 20% |
| [SYNGENE](https://in.tradingview.com/chart/?symbol=NSE:SYNGENE)<br><sub>📶W9 · W↑31d · ↑CMF30d</sub> | ✓ SAFE | Contract research development manufacturing pharma biotech | 📈 BULL_ANY_MID | 1 | ↑48 | ↓1.014 | ↑19d | — | +21.1% | 46.49/44.75 | -1.78% | 20% |
| [JSWCEMENT](https://in.tradingview.com/chart/?symbol=NSE:JSWCEMENT)<br><sub>📶W9 · W↑21d · ↑CMF25d</sub> | ✓ SAFE | Green cement manufacturer for infrastructure construction projects | 📈 BULL_ANY_MID | 0 | ↑57 | ↓1.010 | ↑29d | — | +11.4% | 52.39/52.38 | -0.58% | 20% |
| [ORIENTHOT](https://in.tradingview.com/chart/?symbol=NSE:ORIENTHOT)<br><sub>📶W9 · W↑31d · ↑CMF29d</sub> | ✓ SAFE | Taj-branded luxury hotel operator serving Southern India tourism | 📈 BULL_ANY_MID | 0 | ↑95 | ↓1.024 | ↑30d | — | +29.4% | 60.68/60.24 | +0.03% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ACMESOLAR,NSE:PGHL,NSE:SAMBHV,NSE:LALPATHLAB,NSE:ITI,NSE:INSECTICID,NSE:CANFINHOME,NSE:SWSOLAR,NSE:HITECH,NSE:SUDEEPPHRM,NSE:STEL,NSE:REGAAL,NSE:SIGMAADV,NSE:PTCIL,NSE:5PAISA,NSE:CHOICEIN,NSE:PGHH,NSE:ONESOURCE,NSE:SURYAROSNI,NSE:PENIND,NSE:MPHASIS,NSE:TATAELXSI,NSE:STARHEALTH,NSE:TATACONSUM,NSE:ANTHEM,NSE:EICHERMOT,NSE:AKCAPIT,NSE:SYNGENE,NSE:JSWCEMENT,NSE:ORIENTHOT
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (56)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>📶W9 · 🚀SS · ↓CMF26d</sub> | ✓ SAFE | Solar and wind power plants for Indian utilities | ⚡ BULL_ANY_PPV | 99 | 🔄91 | ↑1.006 | ↑1d | SQ·PV | +1.5% | -5.75/-7.68 | +1.53% | 20% |
| [PGHL](https://in.tradingview.com/chart/?symbol=NSE:PGHL)<br><sub>📶W9 · W↑16d · 🚀SS · ↑CMF18d</sub> | ⚠ CAUTION | Vitamins minerals supplements pharmaceuticals consumer health | ⚡ BULL_ANY_PPV | 93 | 🔄58 | ↑1.018 | ↑2d | SQ·PV | +3.4% | 10.56/6.64 | +2.42% | 20% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>📶W9 · 🚀SS·11x · ↑CMF0d</sub> | ✓ SAFE | ERW steel pipes, tubes, structural hollow sections manufacturer | ⚡ BULL_ANY_PPV | 89 | 🔄96 | ↑1.072 | ↑1d | SQ·PV | +11.9% | 6.23/1.78 | +11.92% | 20% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>📶W9 · W↑10d · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Diagnostic lab network pathology testing healthcare services | ⚡ BULL_ANY_PPV | 63 | ↑83 | ↑1.024 | ↑2d | SQ·PV | +3.9% | 30.47/25.43 | +1.72% | 20% |
| [ITI](https://in.tradingview.com/chart/?symbol=NSE:ITI)<br><sub>📶W9 · W↑16d · 🚀SS·14x · ↑CMF15d</sub> | ✓ SAFE | Telecom equipment manufacturing, cables, defense electronics | ⚡ BULL_ANY_PPV | 49 | 🔄48 | ↑1.085 | ↑1d | PV | +12.4% | 16.45/9.51 | +12.41% | 20% |
| [INSECTICID](https://in.tradingview.com/chart/?symbol=NSE:INSECTICID)<br><sub>📶W9 · W↑6d · ↑CMF4d · ÷DIV</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 49 | 🔄36 | ↑1.042 | ↑1d | PV | +6.1% | -8.89/-16.67 | +6.12% | 20% |
| [CANFINHOME](https://in.tradingview.com/chart/?symbol=NSE:CANFINHOME)<br><sub>📶W9 · W↑16d · 🚀SS · ↑CMF20d</sub> | ⚠ CAUTION | Housing loans for affordable home buyers salaried middle class | ⚡ BULL_ANY_PPV | 42 | 🔄45 | ↑1.029 | ↑13d | PV | +9.8% | 48.07/45.41 | +3.30% | 20% |
| [SWSOLAR](https://in.tradingview.com/chart/?symbol=NSE:SWSOLAR)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF2d</sub> | ✓ SAFE | Solar EPC contractor, develops utility-scale projects globally | ⚡ BULL_ANY_PPV | 41 | 🔄14 | ↑1.030 | ↑14d | PV | +14.2% | 15.68/12.39 | +4.41% | 20% |
| [HITECH](https://in.tradingview.com/chart/?symbol=NSE:HITECH)<br><sub>📶W9 · W↑16d · 🚀SS·31x · ↑CMF1d</sub> | ✓ SAFE | ERW steel pipes tubes construction automotive infrastructure | ⚡ BULL_ANY_PPV | 32 | 🔄59 | ↑1.107 | ↑18d | PV | +33.0% | 33.83/21.18 | +13.51% | 20% |
| [SUDEEPPHRM](https://in.tradingview.com/chart/?symbol=NSE:SUDEEPPHRM)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Calcium phosphate excipients pharma food nutrition | ⚡ BULL_ANY_PPV | 31 | 🔄50 | ↑1.041 | ↑19d | PV | +22.3% | 37.34/32.74 | +4.91% | 10% 🟩 |
| [STEL](https://in.tradingview.com/chart/?symbol=NSE:STEL)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF8d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 10 | ↑83 | ↑1.055 | ↑10d | PV | +25.2% | 41.77/39.89 | +4.00% | 20% |
| [REGAAL](https://in.tradingview.com/chart/?symbol=NSE:REGAAL)<br><sub>📶W9 · W↑26d · ↓CMF24d</sub> | ✓ SAFE | Maize starch processor serving food beverage pharmaceutical industries | ⚡ BULL_ANY_PPV | 7 | ↑84 | ↓1.047 | ↑13d | PV | +15.6% | 58.1/55.63 | +1.02% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Precision metal components aerospace defense oil-gas marine | 📈 BULL_ANY_MID | 99 | 🔄87 | ↑1.012 | ↑1d | SQ | +1.3% | -10.84/-15.14 | +1.26% | 20% |
| [5PAISA](https://in.tradingview.com/chart/?symbol=NSE:5PAISA)<br><sub>📶W9 · W↑10d · ↑CMF3d</sub> | ⚠ CAUTION | Digital discount brokerage for equities, derivatives, commodities trading | 📈 BULL_ANY_MID | 95 | 🔄56 | ↑1.013 | ↑5d | SQ | +3.4% | 22.75/22.46 | +1.84% | 20% |
| [CHOICEIN](https://in.tradingview.com/chart/?symbol=NSE:CHOICEIN)<br><sub>📶W9 · W↑10d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Stockbroking wealth management MSME lending insurance distribution financial services | 📈 BULL_ANY_MID | 94 | 🔄54 | ↑1.022 | ↑1d | SQ | +2.7% | -10.0/-14.88 | +2.71% | 20% |
| [PGHH](https://in.tradingview.com/chart/?symbol=NSE:PGHH)<br><sub>📶W9 · W↑31d · 🚀SS · ↓CMF15d</sub> | ⚠ CAUTION | Feminine hygiene pads, health products, Indian consumer market | 📈 BULL_ANY_MID | 93 | 🔄8 | ↑1.026 | ↑2d | SQ | +4.1% | 12.27/4.19 | +2.65% | 20% |
| [ONESOURCE](https://in.tradingview.com/chart/?symbol=NSE:ONESOURCE)<br><sub>📶W9 · W↑16d · ↑CMF20d</sub> | ✓ SAFE | Specialty pharma CDMO injectable biologics contract manufacturing | 📈 BULL_ANY_MID | 70 | 🔄63 | ↓1.003 | ↑20d | SQ | +14.6% | 18.11/17.86 | -0.47% | 20% |
| [SURYAROSNI](https://in.tradingview.com/chart/?symbol=NSE:SURYAROSNI)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF2d</sub> | ✓ SAFE | Steel pipes, GI products, lighting fixtures for infrastructure | 📈 BULL_ANY_MID | 63 | ↑40 | ↑1.018 | ↑2d | SQ | +3.1% | 15.71/10.93 | +1.27% | 20% |
| [PENIND](https://in.tradingview.com/chart/?symbol=NSE:PENIND)<br><sub>📶W9 · W↑1d · ↓CMF30d</sub> | ✓ SAFE | Steel structures, hydraulics, warehousing for infrastructure mobility energy | 📈 BULL_ANY_MID | 63 | ↑58 | ↑1.024 | ↑2d | SQ | +3.9% | 6.12/-0.04 | +1.17% | 20% |
| [MPHASIS](https://in.tradingview.com/chart/?symbol=NSE:MPHASIS)<br><sub>📶W9 · 🚀SS · ↓CMF11d</sub> | ✓ SAFE | IT services, cloud and cognitive transformation, enterprise clients | 📈 BULL_ANY_MID | 59 | 🔄60 | ↑1.013 | ↑1d | — | +2.0% | -21.48/-24.49 | +2.00% | 20% |
| [TATAELXSI](https://in.tradingview.com/chart/?symbol=NSE:TATAELXSI)<br><sub>📶W9 · W↑31d · ↓CMF0d</sub> | ✓ SAFE | Design engineering services for automotive media healthcare | 📈 BULL_ANY_MID | 58 | ↑39 | ↓1.009 | ↑2d | SQ | +2.6% | 8.67/4.26 | -0.72% | 20% |
| [STARHEALTH](https://in.tradingview.com/chart/?symbol=NSE:STARHEALTH)<br><sub>📶W9 · W↑10d · ↓CMF15d · ÷DIV</sub> | ✓ SAFE | Health insurance provider, retail customers, India | 📈 BULL_ANY_MID | 56 | 🔄67 | ↑1.008 | ↑4d | — | +2.7% | 16.86/16.85 | +1.45% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄55 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>📶W9 · W↑10d · ★ · ↑CMF21d</sub> | ✓ SAFE | Contract research development manufacturing biotech pharma | 📈 BULL_ANY_MID | 9 | ↑84 | ↑1.026 | ↑16d | — | +15.5% | 40.1/36.89 | +0.66% | 20% |
| [AKCAPIT](https://in.tradingview.com/chart/?symbol=NSE:AKCAPIT)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 4 | ↑50 | ↑1.065 | ↑16d | — | +21.2% | 72.5/71.67 | +4.52% | 20% |
| [SYNGENE](https://in.tradingview.com/chart/?symbol=NSE:SYNGENE)<br><sub>📶W9 · W↑31d · ↑CMF30d</sub> | ✓ SAFE | Contract research development manufacturing pharma biotech | 📈 BULL_ANY_MID | 1 | ↑48 | ↓1.014 | ↑19d | — | +21.1% | 46.49/44.75 | -1.78% | 20% |
| [JSWCEMENT](https://in.tradingview.com/chart/?symbol=NSE:JSWCEMENT)<br><sub>📶W9 · W↑21d · ↑CMF25d</sub> | ✓ SAFE | Green cement manufacturer for infrastructure construction projects | 📈 BULL_ANY_MID | 0 | ↑57 | ↓1.010 | ↑29d | — | +11.4% | 52.39/52.38 | -0.58% | 20% |
| [ORIENTHOT](https://in.tradingview.com/chart/?symbol=NSE:ORIENTHOT)<br><sub>📶W9 · W↑31d · ↑CMF29d</sub> | ✓ SAFE | Taj-branded luxury hotel operator serving Southern India tourism | 📈 BULL_ANY_MID | 0 | ↑95 | ↓1.024 | ↑30d | — | +29.4% | 60.68/60.24 | +0.03% | 20% |
| [TCIEXP](https://in.tradingview.com/chart/?symbol=NSE:TCIEXP)<br><sub>W↑10d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Express logistics, multi-modal cargo delivery, B2B | ⚡ BULL_ANY_PPV | 99 | 🔄31 | ↑1.007 | ↑1d | SQ·PV | +2.3% | -12.14/-13.26 | +2.27% | 20% |
| [BENGALASM](https://in.tradingview.com/chart/?symbol=NSE:BENGALASM)<br><sub>↓CMF13d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄50 | ↑1.014 | ↑1d | SQ·PV | +2.5% | -38.79/-43.8 | +2.48% | 20% |
| [KUSUMGAR](https://in.tradingview.com/chart/?symbol=NSE:KUSUMGAR)<br><sub>↓CMF12d</sub> | ✓ SAFE | Synthetic fabric manufacturer, polyamide polyester polyurethane, high-performance applications | ⚡ BULL_ANY_PPV | 86 | 🔄50 | ↑1.006 | ↓14d | SQ·PV | -2.5% | -43.06/-45.24 | +1.09% | 20% |
| [JSLL](https://in.tradingview.com/chart/?symbol=NSE:JSLL)<br><sub>W↑10d · 🚀SS·24x · ↑CMF5d · ÷DIV</sub> | ✓ SAFE | Ayurvedic hospital networks, inpatient outpatient wellness services | ⚡ BULL_ANY_PPV | 59 | 🔄1 | ↑1.011 | ↑1d | PV | +7.3% | -43.83/-47.16 | +7.33% | 20% |
| [INDIAGLYCO](https://in.tradingview.com/chart/?symbol=NSE:INDIAGLYCO)<br><sub>RVOL17x · ↑CMF30d</sub> | ✓ SAFE | Bio-based chemicals, glycols, industrial specialty polymers globally | ⚡ BULL_ANY_PPV | 54 | 🔄0 | ↑1.023 | ↑1d | PV | +11.5% | -51.1/-51.14 | +11.54% | 20% |
| [VMM](https://in.tradingview.com/chart/?symbol=NSE:VMM)<br><sub>W↑10d · 🚀SS · ↑CMF12d · ÷DIV</sub> | ⚠ CAUTION | Value hypermarket chain serving middle-income Indian consumers | ⚡ BULL_ANY_PPV | 54 | 🔄14 | ↑1.015 | ↑1d | PV | +2.7% | -2.63/-2.77 | +2.74% | 20% |
| [POLICYBZR](https://in.tradingview.com/chart/?symbol=NSE:POLICYBZR)<br><sub>W↑1d · 🚀SS · ↑CMF6d</sub> | ✓ SAFE | Online insurance and lending marketplace aggregator platform | ⚡ BULL_ANY_PPV | 41 | 🔄2 | ↑1.050 | ↑9d | PV | +14.2% | 10.38/5.17 | +6.48% | 20% |
| [NAUKRI](https://in.tradingview.com/chart/?symbol=NSE:NAUKRI)<br><sub>🚀SS · ↑CMF12d</sub> | ✓ SAFE | Online classifieds: recruitment, real estate, matrimony, education | 📈 BULL_ANY_MID | 99 | 🔄56 | ↑1.008 | ↑1d | SQ | +0.8% | -40.86/-50.38 | +0.83% | 20% |
| [HUBTOWN](https://in.tradingview.com/chart/?symbol=NSE:HUBTOWN)<br><sub>W↑21d · 🚀SS · ↓CMF17d</sub> | ✓ SAFE | Mumbai real estate developer residential commercial projects MMR | 📈 BULL_ANY_MID | 99 | 🔄19 | ↑1.001 | ↑1d | SQ | +2.1% | -3.02/-4.89 | +2.09% | 20% |
| [3BBLACKBIO](https://in.tradingview.com/chart/?symbol=NSE:3BBLACKBIO)<br><sub>↑CMF0d</sub> | ✓ SAFE | Molecular diagnostic kits, PCR reagents, agrochemicals | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.014 | ↑1d | SQ | +2.2% | -18.47/-21.52 | +2.20% | 20% |
| [AFCONS](https://in.tradingview.com/chart/?symbol=NSE:AFCONS)<br><sub>W↑10d · ↓CMF26d</sub> | ✓ SAFE | EPC contractor offshore structures pipelines power plants | 📈 BULL_ANY_MID | 98 | 🔄4 | ↑1.007 | ↑2d | SQ | +1.8% | -11.37/-12.93 | +0.65% | 20% |
| [SEDEMAC](https://in.tradingview.com/chart/?symbol=NSE:SEDEMAC)<br><sub>🚀SS · ↑CMF14d</sub> | ✓ SAFE | Engine control electronics for automotive and off-highway vehicles | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.019 | ↑1d | SQ | +2.9% | -17.12/-23.4 | +2.90% | 20% |
| [SAATVIKGL](https://in.tradingview.com/chart/?symbol=NSE:SAATVIKGL)<br><sub>W↑1d · ↑CMF1d</sub> | ⚠ CAUTION | Solar modules manufacturing, EPC, renewable energy | 📈 BULL_ANY_MID | 94 | 🔄21 | ↑1.017 | ↑1d | SQ | +2.4% | -41.92/-49.17 | +2.43% | 20% |
| [IDEAFORGE](https://in.tradingview.com/chart/?symbol=NSE:IDEAFORGE)<br><sub>W↑6d · 🚀SS · ↓CMF10d</sub> | ✓ SAFE | Drone manufacturer for defense and civilian applications | 📈 BULL_ANY_MID | 93 | 🔄76 | ↑1.020 | ↑2d | SQ | +3.7% | 1.45/-2.02 | +2.00% | 10% 🟩 |
| [ELANTAS](https://in.tradingview.com/chart/?symbol=NSE:ELANTAS)<br><sub>↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 80 | 🔄50 | ↑1.001 | ↓30d | SQ | -11.8% | -46.51/-46.85 | +2.09% | 20% |
| [GEOJITFSL](https://in.tradingview.com/chart/?symbol=NSE:GEOJITFSL)<br><sub>↓CMF2d</sub> | ⚠ CAUTION | Stock broking and portfolio management for retail investors | 📈 BULL_ANY_MID | 59 | 🔄51 | ↑1.011 | ↑1d | — | +2.4% | 6.01/5.96 | +2.40% | 20% |
| [ABBOTINDIA](https://in.tradingview.com/chart/?symbol=NSE:ABBOTINDIA)<br><sub>W↑10d · ↓CMF26d · ⚠️TRAP</sub> | ⚠ CAUTION | Pharmaceuticals and nutritional products for Indian healthcare markets | 📈 BULL_ANY_MID | 58 | ↑47 | ↓1.001 | ↑2d | SQ | +1.7% | -5.64/-9.02 | -1.51% | 20% |
| [DBL](https://in.tradingview.com/chart/?symbol=NSE:DBL)<br><sub>W↑10d · ↓CMF1d · ⚠️TRAP</sub> | ✓ SAFE | Highway and bridge construction, roads infrastructure sector | 📈 BULL_ANY_MID | 58 | ↑41 | ↓1.004 | ↑2d | SQ | +3.1% | 9.96/7.53 | -1.07% | 20% |
| [IRMENERGY](https://in.tradingview.com/chart/?symbol=NSE:IRMENERGY)<br><sub>W↑6d · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | Natural gas distribution networks serving residential commercial industrial | 📈 BULL_ANY_MID | 58 | 🔄43 | ↑1.013 | ↑2d | — | +2.3% | 0.61/-1.49 | +2.04% | 20% 🟦 |
| [GUJENERGY](https://in.tradingview.com/chart/?symbol=NSE:GUJENERGY)<br><sub>W↑16d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Piped natural gas distribution to households and industries | 📈 BULL_ANY_MID | 52 | 🔄6 | ↑1.015 | ↑3d | — | +3.3% | 12.76/9.06 | +1.63% | 20% |
| [EIHAHOTELS](https://in.tradingview.com/chart/?symbol=NSE:EIHAHOTELS)<br><sub>W↑10d · ↓CMF19d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 50 | ↑39 | ↓1.008 | ↑10d | SQ | +3.3% | 22.23/13.81 | -0.14% | 20% |
| [SANGHVIMOV](https://in.tradingview.com/chart/?symbol=NSE:SANGHVIMOV)<br><sub>W↑1d · ↓CMF30d</sub> | ✓ SAFE | Heavy crane rentals for industrial construction projects | 📈 BULL_ANY_MID | 42 | 🔄65 | ↑1.016 | ↑13d | — | +9.0% | 14.28/12.98 | +1.25% | 20% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>↓CMF2d · DEL40%(T-1)</sub> | ✓ SAFE | Refines crude oil, produces petroleum products, lubricants | 📈 BULL_ANY_MID | 40 | 🔄87 | ↑1.004 | ↓23d | — | +0.4% | -24.21/-24.75 | +1.24% | 20% |
| [SUPRAJIT](https://in.tradingview.com/chart/?symbol=NSE:SUPRAJIT)<br><sub>↓CMF8d</sub> | ⚠ CAUTION | Automotive cables, halogen lamps, mechanical components manufacturer | 📈 BULL_ANY_MID | 40 | 🔄49 | ↑1.000 | ↓20d | — | +0.5% | -33.46/-34.41 | +1.01% | 20% |
| [SULA](https://in.tradingview.com/chart/?symbol=NSE:SULA)<br><sub>W↑16d · ↑CMF1d</sub> | ✓ SAFE | Grape wine production, tourism, domestic premium beverage market | 📈 BULL_ANY_MID | 18 | ↑20 | ↓1.006 | ↑2d | — | +3.0% | 12.36/11.93 | -0.44% | 20% |
| [SBICARD](https://in.tradingview.com/chart/?symbol=NSE:SBICARD)<br><sub>W↑10d · ↑CMF12d</sub> | ✓ SAFE | Credit card issuer, consumer lending, retail banking sector | 📈 BULL_ANY_MID | 17 | ↑17 | ↓1.003 | ↑3d | — | +2.4% | 6.39/4.15 | -0.71% | 20% |
| [M&MFIN](https://in.tradingview.com/chart/?symbol=NSE:M&MFIN)<br><sub>↓CMF4d</sub> | ✓ SAFE | Rural tractor auto vehicle financing NBFC farm | 📈 BULL_ANY_MID | 7 | ↑14 | ↓1.006 | ↑13d | — | +6.2% | 2.55/0.23 | -0.50% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ACMESOLAR,NSE:PGHL,NSE:SAMBHV,NSE:LALPATHLAB,NSE:ITI,NSE:INSECTICID,NSE:CANFINHOME,NSE:SWSOLAR,NSE:HITECH,NSE:SUDEEPPHRM,NSE:STEL,NSE:REGAAL,NSE:SIGMAADV,NSE:PTCIL,NSE:5PAISA,NSE:CHOICEIN,NSE:PGHH,NSE:ONESOURCE,NSE:SURYAROSNI,NSE:PENIND,NSE:MPHASIS,NSE:TATAELXSI,NSE:STARHEALTH,NSE:TATACONSUM,NSE:ANTHEM,NSE:AKCAPIT,NSE:SYNGENE,NSE:JSWCEMENT,NSE:ORIENTHOT,NSE:TCIEXP,NSE:BENGALASM,NSE:KUSUMGAR,NSE:JSLL,NSE:INDIAGLYCO,NSE:VMM,NSE:POLICYBZR,NSE:NAUKRI,NSE:HUBTOWN,NSE:3BBLACKBIO,NSE:AFCONS,NSE:SEDEMAC,NSE:SAATVIKGL,NSE:IDEAFORGE,NSE:ELANTAS,NSE:GEOJITFSL,NSE:ABBOTINDIA,NSE:DBL,NSE:IRMENERGY,NSE:GUJENERGY,NSE:EIHAHOTELS,NSE:SANGHVIMOV,NSE:CHENNPETRO,NSE:SUPRAJIT,NSE:SULA,NSE:SBICARD,NSE:M&MFIN
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (33)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>📶W9 · 🚀SS · ↓CMF26d</sub> | ✓ SAFE | Solar and wind power plants for Indian utilities | ⚡ BULL_ANY_PPV | 99 | 🔄91 | ↑1.006 | ↑1d | SQ·PV | +1.5% | -5.75/-7.68 | +1.53% | 20% |
| [PGHL](https://in.tradingview.com/chart/?symbol=NSE:PGHL)<br><sub>📶W9 · W↑16d · 🚀SS · ↑CMF18d</sub> | ⚠ CAUTION | Vitamins minerals supplements pharmaceuticals consumer health | ⚡ BULL_ANY_PPV | 93 | 🔄58 | ↑1.018 | ↑2d | SQ·PV | +3.4% | 10.56/6.64 | +2.42% | 20% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>📶W9 · 🚀SS·11x · ↑CMF0d</sub> | ✓ SAFE | ERW steel pipes, tubes, structural hollow sections manufacturer | ⚡ BULL_ANY_PPV | 89 | 🔄96 | ↑1.072 | ↑1d | SQ·PV | +11.9% | 6.23/1.78 | +11.92% | 20% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>📶W9 · W↑10d · 🚀SS · ↓CMF0d</sub> | ✓ SAFE | Diagnostic lab network pathology testing healthcare services | ⚡ BULL_ANY_PPV | 63 | ↑83 | ↑1.024 | ↑2d | SQ·PV | +3.9% | 30.47/25.43 | +1.72% | 20% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>📶W9 · ↑CMF0d</sub> | ✓ SAFE | Precision metal components aerospace defense oil-gas marine | 📈 BULL_ANY_MID | 99 | 🔄87 | ↑1.012 | ↑1d | SQ | +1.3% | -10.84/-15.14 | +1.26% | 20% |
| [5PAISA](https://in.tradingview.com/chart/?symbol=NSE:5PAISA)<br><sub>📶W9 · W↑10d · ↑CMF3d</sub> | ⚠ CAUTION | Digital discount brokerage for equities, derivatives, commodities trading | 📈 BULL_ANY_MID | 95 | 🔄56 | ↑1.013 | ↑5d | SQ | +3.4% | 22.75/22.46 | +1.84% | 20% |
| [CHOICEIN](https://in.tradingview.com/chart/?symbol=NSE:CHOICEIN)<br><sub>📶W9 · W↑10d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Stockbroking wealth management MSME lending insurance distribution financial services | 📈 BULL_ANY_MID | 94 | 🔄54 | ↑1.022 | ↑1d | SQ | +2.7% | -10.0/-14.88 | +2.71% | 20% |
| [PGHH](https://in.tradingview.com/chart/?symbol=NSE:PGHH)<br><sub>📶W9 · W↑31d · 🚀SS · ↓CMF15d</sub> | ⚠ CAUTION | Feminine hygiene pads, health products, Indian consumer market | 📈 BULL_ANY_MID | 93 | 🔄8 | ↑1.026 | ↑2d | SQ | +4.1% | 12.27/4.19 | +2.65% | 20% |
| [ONESOURCE](https://in.tradingview.com/chart/?symbol=NSE:ONESOURCE)<br><sub>📶W9 · W↑16d · ↑CMF20d</sub> | ✓ SAFE | Specialty pharma CDMO injectable biologics contract manufacturing | 📈 BULL_ANY_MID | 70 | 🔄63 | ↓1.003 | ↑20d | SQ | +14.6% | 18.11/17.86 | -0.47% | 20% |
| [SURYAROSNI](https://in.tradingview.com/chart/?symbol=NSE:SURYAROSNI)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF2d</sub> | ✓ SAFE | Steel pipes, GI products, lighting fixtures for infrastructure | 📈 BULL_ANY_MID | 63 | ↑40 | ↑1.018 | ↑2d | SQ | +3.1% | 15.71/10.93 | +1.27% | 20% |
| [PENIND](https://in.tradingview.com/chart/?symbol=NSE:PENIND)<br><sub>📶W9 · W↑1d · ↓CMF30d</sub> | ✓ SAFE | Steel structures, hydraulics, warehousing for infrastructure mobility energy | 📈 BULL_ANY_MID | 63 | ↑58 | ↑1.024 | ↑2d | SQ | +3.9% | 6.12/-0.04 | +1.17% | 20% |
| [TATAELXSI](https://in.tradingview.com/chart/?symbol=NSE:TATAELXSI)<br><sub>📶W9 · W↑31d · ↓CMF0d</sub> | ✓ SAFE | Design engineering services for automotive media healthcare | 📈 BULL_ANY_MID | 58 | ↑39 | ↓1.009 | ↑2d | SQ | +2.6% | 8.67/4.26 | -0.72% | 20% |
| [TCIEXP](https://in.tradingview.com/chart/?symbol=NSE:TCIEXP)<br><sub>W↑10d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Express logistics, multi-modal cargo delivery, B2B | ⚡ BULL_ANY_PPV | 99 | 🔄31 | ↑1.007 | ↑1d | SQ·PV | +2.3% | -12.14/-13.26 | +2.27% | 20% |
| [BENGALASM](https://in.tradingview.com/chart/?symbol=NSE:BENGALASM)<br><sub>↓CMF13d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 99 | 🔄50 | ↑1.014 | ↑1d | SQ·PV | +2.5% | -38.79/-43.8 | +2.48% | 20% |
| [KUSUMGAR](https://in.tradingview.com/chart/?symbol=NSE:KUSUMGAR)<br><sub>↓CMF12d</sub> | ✓ SAFE | Synthetic fabric manufacturer, polyamide polyester polyurethane, high-performance applications | ⚡ BULL_ANY_PPV | 86 | 🔄50 | ↑1.006 | ↓14d | SQ·PV | -2.5% | -43.06/-45.24 | +1.09% | 20% |
| [JTLIND](https://in.tradingview.com/chart/?symbol=NSE:JTLIND)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | ERW steel pipes manufacturer for infrastructure construction projects | ⚡ BULL_ANY_PPV | 54 | ↓66 | ↑0.996 | ↓11d | SQ·PV | -0.3% | -26.77/-32.78 | +1.10% | 20% |
| [NAUKRI](https://in.tradingview.com/chart/?symbol=NSE:NAUKRI)<br><sub>🚀SS · ↑CMF12d</sub> | ✓ SAFE | Online classifieds: recruitment, real estate, matrimony, education | 📈 BULL_ANY_MID | 99 | 🔄56 | ↑1.008 | ↑1d | SQ | +0.8% | -40.86/-50.38 | +0.83% | 20% |
| [HUBTOWN](https://in.tradingview.com/chart/?symbol=NSE:HUBTOWN)<br><sub>W↑21d · 🚀SS · ↓CMF17d</sub> | ✓ SAFE | Mumbai real estate developer residential commercial projects MMR | 📈 BULL_ANY_MID | 99 | 🔄19 | ↑1.001 | ↑1d | SQ | +2.1% | -3.02/-4.89 | +2.09% | 20% |
| [3BBLACKBIO](https://in.tradingview.com/chart/?symbol=NSE:3BBLACKBIO)<br><sub>↑CMF0d</sub> | ✓ SAFE | Molecular diagnostic kits, PCR reagents, agrochemicals | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.014 | ↑1d | SQ | +2.2% | -18.47/-21.52 | +2.20% | 20% |
| [AFCONS](https://in.tradingview.com/chart/?symbol=NSE:AFCONS)<br><sub>W↑10d · ↓CMF26d</sub> | ✓ SAFE | EPC contractor offshore structures pipelines power plants | 📈 BULL_ANY_MID | 98 | 🔄4 | ↑1.007 | ↑2d | SQ | +1.8% | -11.37/-12.93 | +0.65% | 20% |
| [SEDEMAC](https://in.tradingview.com/chart/?symbol=NSE:SEDEMAC)<br><sub>🚀SS · ↑CMF14d</sub> | ✓ SAFE | Engine control electronics for automotive and off-highway vehicles | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.019 | ↑1d | SQ | +2.9% | -17.12/-23.4 | +2.90% | 20% |
| [SAATVIKGL](https://in.tradingview.com/chart/?symbol=NSE:SAATVIKGL)<br><sub>W↑1d · ↑CMF1d</sub> | ⚠ CAUTION | Solar modules manufacturing, EPC, renewable energy | 📈 BULL_ANY_MID | 94 | 🔄21 | ↑1.017 | ↑1d | SQ | +2.4% | -41.92/-49.17 | +2.43% | 20% |
| [IDEAFORGE](https://in.tradingview.com/chart/?symbol=NSE:IDEAFORGE)<br><sub>W↑6d · 🚀SS · ↓CMF10d</sub> | ✓ SAFE | Drone manufacturer for defense and civilian applications | 📈 BULL_ANY_MID | 93 | 🔄76 | ↑1.020 | ↑2d | SQ | +3.7% | 1.45/-2.02 | +2.00% | 10% 🟩 |
| [ELANTAS](https://in.tradingview.com/chart/?symbol=NSE:ELANTAS)<br><sub>↑CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 80 | 🔄50 | ↑1.001 | ↓30d | SQ | -11.8% | -46.51/-46.85 | +2.09% | 20% |
| [ABBOTINDIA](https://in.tradingview.com/chart/?symbol=NSE:ABBOTINDIA)<br><sub>W↑10d · ↓CMF26d · ⚠️TRAP</sub> | ⚠ CAUTION | Pharmaceuticals and nutritional products for Indian healthcare markets | 📈 BULL_ANY_MID | 58 | ↑47 | ↓1.001 | ↑2d | SQ | +1.7% | -5.64/-9.02 | -1.51% | 20% |
| [DBL](https://in.tradingview.com/chart/?symbol=NSE:DBL)<br><sub>W↑10d · ↓CMF1d · ⚠️TRAP</sub> | ✓ SAFE | Highway and bridge construction, roads infrastructure sector | 📈 BULL_ANY_MID | 58 | ↑41 | ↓1.004 | ↑2d | SQ | +3.1% | 9.96/7.53 | -1.07% | 20% |
| [AVADHSUGAR](https://in.tradingview.com/chart/?symbol=NSE:AVADHSUGAR)<br><sub>★ · ↓CMF13d</sub> | ✓ SAFE | Sugar cane processing, ethanol, power generation | 📈 BULL_ANY_MID | 58 | ↓97 | ↓0.999 | ↓2d | SQ | -0.8% | -14.1/-14.74 | -0.86% | 20% 🟦 |
| [VENTIVE](https://in.tradingview.com/chart/?symbol=NSE:VENTIVE)<br><sub>W↑10d · ↓CMF1d</sub> | ⚠ CAUTION | Luxury hotel owner operator developer India resorts | 📈 BULL_ANY_MID | 56 | ↓21 | ↓0.999 | ↑4d | SQ | +0.5% | -10.44/-12.65 | -0.41% | 20% |
| [PTC](https://in.tradingview.com/chart/?symbol=NSE:PTC)<br><sub>W↑1d · ↓CMF21d · ÷DIV</sub> | ✓ SAFE | Power trading platform connecting generators utilities consumers | 📈 BULL_ANY_MID | 54 | ↓19 | ↑0.995 | ↓11d | SQ | -1.6% | -41.55/-43.55 | +0.00% | 20% |
| [MOIL](https://in.tradingview.com/chart/?symbol=NSE:MOIL)<br><sub>W↑10d · ↓CMF30d · ÷DIV</sub> | ✓ SAFE | Manganese ore mining, largest Indian producer, steel sector | 📈 BULL_ANY_MID | 54 | ↓8 | ↑0.995 | ↓11d | SQ | -0.6% | -39.19/-39.45 | -0.09% | 20% |
| [EIHAHOTELS](https://in.tradingview.com/chart/?symbol=NSE:EIHAHOTELS)<br><sub>W↑10d · ↓CMF19d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 50 | ↑39 | ↓1.008 | ↑10d | SQ | +3.3% | 22.23/13.81 | -0.14% | 20% |
| [DEEPINDS](https://in.tradingview.com/chart/?symbol=NSE:DEEPINDS)<br><sub>↓CMF21d · ÷DIV</sub> | ✓ SAFE | Oil gas compression drilling workover services provider | 📈 BULL_ANY_MID | 45 | ↓85 | ↑0.992 | ↓30d | SQ | -16.3% | -48.89/-49.88 | -0.12% | 20% |
| [NRAIL](https://in.tradingview.com/chart/?symbol=NSE:NRAIL)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 44 | ↓89 | ↓0.978 | ↓16d | SQ | -4.0% | -38.31/-38.48 | -3.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ACMESOLAR,NSE:PGHL,NSE:SAMBHV,NSE:LALPATHLAB,NSE:PTCIL,NSE:5PAISA,NSE:CHOICEIN,NSE:PGHH,NSE:ONESOURCE,NSE:SURYAROSNI,NSE:PENIND,NSE:TATAELXSI,NSE:TCIEXP,NSE:BENGALASM,NSE:KUSUMGAR,NSE:JTLIND,NSE:NAUKRI,NSE:HUBTOWN,NSE:3BBLACKBIO,NSE:AFCONS,NSE:SEDEMAC,NSE:SAATVIKGL,NSE:IDEAFORGE,NSE:ELANTAS,NSE:ABBOTINDIA,NSE:DBL,NSE:AVADHSUGAR,NSE:VENTIVE,NSE:PTC,NSE:MOIL,NSE:EIHAHOTELS,NSE:DEEPINDS,NSE:NRAIL
```

---

### 🔥 MAJOR — PPV confirmed (13)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ITI](https://in.tradingview.com/chart/?symbol=NSE:ITI)<br><sub>📶W9 · W↑16d · 🚀SS·14x · ↑CMF15d</sub> | ✓ SAFE | Telecom equipment manufacturing, cables, defense electronics | ⚡ BULL_ANY_PPV | 49 | 🔄48 | ↑1.085 | ↑1d | PV | +12.4% | 16.45/9.51 | +12.41% | 20% |
| [INSECTICID](https://in.tradingview.com/chart/?symbol=NSE:INSECTICID)<br><sub>📶W9 · W↑6d · ↑CMF4d · ÷DIV</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 49 | 🔄36 | ↑1.042 | ↑1d | PV | +6.1% | -8.89/-16.67 | +6.12% | 20% |
| [CANFINHOME](https://in.tradingview.com/chart/?symbol=NSE:CANFINHOME)<br><sub>📶W9 · W↑16d · 🚀SS · ↑CMF20d</sub> | ⚠ CAUTION | Housing loans for affordable home buyers salaried middle class | ⚡ BULL_ANY_PPV | 42 | 🔄45 | ↑1.029 | ↑13d | PV | +9.8% | 48.07/45.41 | +3.30% | 20% |
| [SWSOLAR](https://in.tradingview.com/chart/?symbol=NSE:SWSOLAR)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF2d</sub> | ✓ SAFE | Solar EPC contractor, develops utility-scale projects globally | ⚡ BULL_ANY_PPV | 41 | 🔄14 | ↑1.030 | ↑14d | PV | +14.2% | 15.68/12.39 | +4.41% | 20% |
| [HITECH](https://in.tradingview.com/chart/?symbol=NSE:HITECH)<br><sub>📶W9 · W↑16d · 🚀SS·31x · ↑CMF1d</sub> | ✓ SAFE | ERW steel pipes tubes construction automotive infrastructure | ⚡ BULL_ANY_PPV | 32 | 🔄59 | ↑1.107 | ↑18d | PV | +33.0% | 33.83/21.18 | +13.51% | 20% |
| [SUDEEPPHRM](https://in.tradingview.com/chart/?symbol=NSE:SUDEEPPHRM)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Calcium phosphate excipients pharma food nutrition | ⚡ BULL_ANY_PPV | 31 | 🔄50 | ↑1.041 | ↑19d | PV | +22.3% | 37.34/32.74 | +4.91% | 10% 🟩 |
| [STEL](https://in.tradingview.com/chart/?symbol=NSE:STEL)<br><sub>📶W9 · W↑10d · 🚀SS · ↑CMF8d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 10 | ↑83 | ↑1.055 | ↑10d | PV | +25.2% | 41.77/39.89 | +4.00% | 20% |
| [REGAAL](https://in.tradingview.com/chart/?symbol=NSE:REGAAL)<br><sub>📶W9 · W↑26d · ↓CMF24d</sub> | ✓ SAFE | Maize starch processor serving food beverage pharmaceutical industries | ⚡ BULL_ANY_PPV | 7 | ↑84 | ↓1.047 | ↑13d | PV | +15.6% | 58.1/55.63 | +1.02% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [JSLL](https://in.tradingview.com/chart/?symbol=NSE:JSLL)<br><sub>W↑10d · 🚀SS·24x · ↑CMF5d · ÷DIV</sub> | ✓ SAFE | Ayurvedic hospital networks, inpatient outpatient wellness services | ⚡ BULL_ANY_PPV | 59 | 🔄1 | ↑1.011 | ↑1d | PV | +7.3% | -43.83/-47.16 | +7.33% | 20% |
| [INDIAGLYCO](https://in.tradingview.com/chart/?symbol=NSE:INDIAGLYCO)<br><sub>RVOL17x · ↑CMF30d</sub> | ✓ SAFE | Bio-based chemicals, glycols, industrial specialty polymers globally | ⚡ BULL_ANY_PPV | 54 | 🔄0 | ↑1.023 | ↑1d | PV | +11.5% | -51.1/-51.14 | +11.54% | 20% |
| [VMM](https://in.tradingview.com/chart/?symbol=NSE:VMM)<br><sub>W↑10d · 🚀SS · ↑CMF12d · ÷DIV</sub> | ⚠ CAUTION | Value hypermarket chain serving middle-income Indian consumers | ⚡ BULL_ANY_PPV | 54 | 🔄14 | ↑1.015 | ↑1d | PV | +2.7% | -2.63/-2.77 | +2.74% | 20% |
| [POLICYBZR](https://in.tradingview.com/chart/?symbol=NSE:POLICYBZR)<br><sub>W↑1d · 🚀SS · ↑CMF6d</sub> | ✓ SAFE | Online insurance and lending marketplace aggregator platform | ⚡ BULL_ANY_PPV | 41 | 🔄2 | ↑1.050 | ↑9d | PV | +14.2% | 10.38/5.17 | +6.48% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ITI,NSE:INSECTICID,NSE:CANFINHOME,NSE:SWSOLAR,NSE:HITECH,NSE:SUDEEPPHRM,NSE:STEL,NSE:REGAAL,NSE:SIGMAADV,NSE:JSLL,NSE:INDIAGLYCO,NSE:VMM,NSE:POLICYBZR
```

### 🟢 OVERSOLD — reversal from −53/−60 (5)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [LATENTVIEW](https://in.tradingview.com/chart/?symbol=NSE:LATENTVIEW)<br><sub>W↑1d · 🚀SS · ↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Data analytics consulting, marketing optimization, enterprise clients | 🟡 BULL_OS_L2 | 17 | ↓2 | ↑0.988 | ↓8d | — | -6.5% | -55.92/-56.68 | +2.17% | 20% |
| [RISHABH](https://in.tradingview.com/chart/?symbol=NSE:RISHABH)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Electrical meters, automation instruments, industrial measurement solutions | 🟡 BULL_OS_L2 | 11 | ↓75 | ↓0.983 | ↓9d | — | -3.5% | -54.22/-56.66 | -2.02% | 20% |
| [POCL](https://in.tradingview.com/chart/?symbol=NSE:POCL)<br><sub>W↑6d · ↑CMF6d · ⚠️TRAP · ÷DIV</sub> | ✓ SAFE | Lead copper aluminum recycling non-ferrous metals manufacturer | 🟡 BULL_OS_L2 | 9 | ↓1 | ↓0.973 | ↓11d | — | -6.5% | -55.22/-55.62 | -1.31% | 20% |
| [RRKABEL](https://in.tradingview.com/chart/?symbol=NSE:RRKABEL)<br><sub>↓CMF17d · 🎯SLING</sub> | ✓ SAFE | Copper wires cables for residential commercial industrial infrastructure | 🟡 BULL_OS_L2 | 5 | ↓42 | ↑0.967 | ↓40d | — | -25.9% | -54.18/-54.25 | +0.69% | 20% |
| [UNIVCABLES](https://in.tradingview.com/chart/?symbol=NSE:UNIVCABLES)<br><sub>↓CMF16d · DEL83%(T-1) · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Electrical power cables manufacturing for infrastructure distribution networks | 🟡 BULL_OS_L2 | 5 | ↓65 | ↑0.984 | ↓29d | — | -25.4% | -53.47/-54.63 | +2.26% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LATENTVIEW,NSE:RISHABH,NSE:POCL,NSE:RRKABEL,NSE:UNIVCABLES
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (22)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MPHASIS](https://in.tradingview.com/chart/?symbol=NSE:MPHASIS)<br><sub>📶W9 · 🚀SS · ↓CMF11d</sub> | ✓ SAFE | IT services, cloud and cognitive transformation, enterprise clients | 📈 BULL_ANY_MID | 59 | 🔄60 | ↑1.013 | ↑1d | — | +2.0% | -21.48/-24.49 | +2.00% | 20% |
| [STARHEALTH](https://in.tradingview.com/chart/?symbol=NSE:STARHEALTH)<br><sub>📶W9 · W↑10d · ↓CMF15d · ÷DIV</sub> | ✓ SAFE | Health insurance provider, retail customers, India | 📈 BULL_ANY_MID | 56 | 🔄67 | ↑1.008 | ↑4d | — | +2.7% | 16.86/16.85 | +1.45% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄55 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>📶W9 · W↑10d · ★ · ↑CMF21d</sub> | ✓ SAFE | Contract research development manufacturing biotech pharma | 📈 BULL_ANY_MID | 9 | ↑84 | ↑1.026 | ↑16d | — | +15.5% | 40.1/36.89 | +0.66% | 20% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>📶W9 · W↑11d · ↑CMF13d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓60 | ↓1.007 | ↑15d | — | +7.0% | 46.27/45.57 | -0.67% | 20% |
| [AKCAPIT](https://in.tradingview.com/chart/?symbol=NSE:AKCAPIT)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 4 | ↑50 | ↑1.065 | ↑16d | — | +21.2% | 72.5/71.67 | +4.52% | 20% |
| [SYNGENE](https://in.tradingview.com/chart/?symbol=NSE:SYNGENE)<br><sub>📶W9 · W↑31d · ↑CMF30d</sub> | ✓ SAFE | Contract research development manufacturing pharma biotech | 📈 BULL_ANY_MID | 1 | ↑48 | ↓1.014 | ↑19d | — | +21.1% | 46.49/44.75 | -1.78% | 20% |
| [JSWCEMENT](https://in.tradingview.com/chart/?symbol=NSE:JSWCEMENT)<br><sub>📶W9 · W↑21d · ↑CMF25d</sub> | ✓ SAFE | Green cement manufacturer for infrastructure construction projects | 📈 BULL_ANY_MID | 0 | ↑57 | ↓1.010 | ↑29d | — | +11.4% | 52.39/52.38 | -0.58% | 20% |
| [ORIENTHOT](https://in.tradingview.com/chart/?symbol=NSE:ORIENTHOT)<br><sub>📶W9 · W↑31d · ↑CMF29d</sub> | ✓ SAFE | Taj-branded luxury hotel operator serving Southern India tourism | 📈 BULL_ANY_MID | 0 | ↑95 | ↓1.024 | ↑30d | — | +29.4% | 60.68/60.24 | +0.03% | 20% |
| [GEOJITFSL](https://in.tradingview.com/chart/?symbol=NSE:GEOJITFSL)<br><sub>↓CMF2d</sub> | ⚠ CAUTION | Stock broking and portfolio management for retail investors | 📈 BULL_ANY_MID | 59 | 🔄51 | ↑1.011 | ↑1d | — | +2.4% | 6.01/5.96 | +2.40% | 20% |
| [IRMENERGY](https://in.tradingview.com/chart/?symbol=NSE:IRMENERGY)<br><sub>W↑6d · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | Natural gas distribution networks serving residential commercial industrial | 📈 BULL_ANY_MID | 58 | 🔄43 | ↑1.013 | ↑2d | — | +2.3% | 0.61/-1.49 | +2.04% | 20% 🟦 |
| [GUJENERGY](https://in.tradingview.com/chart/?symbol=NSE:GUJENERGY)<br><sub>W↑16d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Piped natural gas distribution to households and industries | 📈 BULL_ANY_MID | 52 | 🔄6 | ↑1.015 | ↑3d | — | +3.3% | 12.76/9.06 | +1.63% | 20% |
| [SANGHVIMOV](https://in.tradingview.com/chart/?symbol=NSE:SANGHVIMOV)<br><sub>W↑1d · ↓CMF30d</sub> | ✓ SAFE | Heavy crane rentals for industrial construction projects | 📈 BULL_ANY_MID | 42 | 🔄65 | ↑1.016 | ↑13d | — | +9.0% | 14.28/12.98 | +1.25% | 20% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>↓CMF2d · DEL40%(T-1)</sub> | ✓ SAFE | Refines crude oil, produces petroleum products, lubricants | 📈 BULL_ANY_MID | 40 | 🔄87 | ↑1.004 | ↓23d | — | +0.4% | -24.21/-24.75 | +1.24% | 20% |
| [SUPRAJIT](https://in.tradingview.com/chart/?symbol=NSE:SUPRAJIT)<br><sub>↓CMF8d</sub> | ⚠ CAUTION | Automotive cables, halogen lamps, mechanical components manufacturer | 📈 BULL_ANY_MID | 40 | 🔄49 | ↑1.000 | ↓20d | — | +0.5% | -33.46/-34.41 | +1.01% | 20% |
| [SULA](https://in.tradingview.com/chart/?symbol=NSE:SULA)<br><sub>W↑16d · ↑CMF1d</sub> | ✓ SAFE | Grape wine production, tourism, domestic premium beverage market | 📈 BULL_ANY_MID | 18 | ↑20 | ↓1.006 | ↑2d | — | +3.0% | 12.36/11.93 | -0.44% | 20% |
| [SBICARD](https://in.tradingview.com/chart/?symbol=NSE:SBICARD)<br><sub>W↑10d · ↑CMF12d</sub> | ✓ SAFE | Credit card issuer, consumer lending, retail banking sector | 📈 BULL_ANY_MID | 17 | ↑17 | ↓1.003 | ↑3d | — | +2.4% | 6.39/4.15 | -0.71% | 20% |
| [LANDMARK](https://in.tradingview.com/chart/?symbol=NSE:LANDMARK)<br><sub>W↑10d · ↑CMF1d · ⚠️TRAP</sub> | ✓ SAFE | Premium multi-brand auto retail, luxury car dealerships | 📈 BULL_ANY_MID | 17 | ↓58 | ↓1.000 | ↑3d | — | +2.5% | 4.3/3.05 | -0.84% | 20% |
| [M&MFIN](https://in.tradingview.com/chart/?symbol=NSE:M&MFIN)<br><sub>↓CMF4d</sub> | ✓ SAFE | Rural tractor auto vehicle financing NBFC farm | 📈 BULL_ANY_MID | 7 | ↑14 | ↓1.006 | ↑13d | — | +6.2% | 2.55/0.23 | -0.50% | 20% |
| [APARINDS](https://in.tradingview.com/chart/?symbol=NSE:APARINDS)<br><sub>↓CMF0d · ⚠️TRAP</sub> | ✓ SAFE | Power cables, transformers oils, specialty chemicals globally | 📈 BULL_ANY_MID | 6 | ↓72 | ↓0.982 | ↓14d | — | -8.6% | -45.96/-47.21 | -1.08% | 20% |
| [ECLERX](https://in.tradingview.com/chart/?symbol=NSE:ECLERX)<br><sub>🚀SS · ↓CMF17d · ÷DIV</sub> | ✓ SAFE | Legal document processing, BPM automation, financial services outsourcing | 📈 BULL_ANY_MID | 5 | ↓18 | ↑0.989 | ↓30d | — | -18.9% | -52.21/-52.41 | +3.94% | 20% |
| [HEXT](https://in.tradingview.com/chart/?symbol=NSE:HEXT)<br><sub>🚀SS · ↓CMF10d</sub> | ✓ SAFE | IT services, digital transformation, automation, enterprise clients | 📈 BULL_ANY_MID | 5 | ↓28 | ↑0.984 | ↓35d | — | -2.4% | -35.91/-36.76 | -0.19% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MPHASIS,NSE:STARHEALTH,NSE:TATACONSUM,NSE:ANTHEM,NSE:EICHERMOT,NSE:AKCAPIT,NSE:SYNGENE,NSE:JSWCEMENT,NSE:ORIENTHOT,NSE:GEOJITFSL,NSE:IRMENERGY,NSE:GUJENERGY,NSE:SANGHVIMOV,NSE:CHENNPETRO,NSE:SUPRAJIT,NSE:SULA,NSE:SBICARD,NSE:LANDMARK,NSE:M&MFIN,NSE:APARINDS,NSE:ECLERX,NSE:HEXT
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
