> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-11-17
*Generated 2026-11-17 15:50 IST*

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

**Total bull crosses today: 48** · 20 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:5PAISA,NSE:FIRSTCRY,NSE:KDDL,NSE:AVTNPL,NSE:ARIS,NSE:WELSPUNLIV,NSE:KITEX,NSE:SIGMAADV,NSE:SHADOWFAX,NSE:ONEPOINT,NSE:AJMERA,NSE:VIJAYA,NSE:BHARTIHEXA,NSE:ARIHANTCAP,NSE:LOTUSDEV,NSE:AYMSYNTEX,NSE:NUVOCO,NSE:ACC,NSE:TATACONSUM,NSE:SALSTEEL,NSE:NH,NSE:EICHERMOT,NSE:SPECTRUM,NSE:LUMAXTECH,NSE:SURAKSHA,NSE:BRIGADE,NSE:KAMAHOLD,NSE:MEDIASSIST,NSE:SHRIPISTON,NSE:UGROCAP,NSE:PGIL,NSE:SUPRIYA,NSE:VIPIND,NSE:GARFIBRES,NSE:NSIL,NSE:RAIN,NSE:AMAGI,NSE:INDPRUD,NSE:DBREALTY,NSE:DODLA,NSE:SHOPERSTOP,NSE:ASHAPURMIN,NSE:NRBBEARING,NSE:SETL,NSE:AWL,NSE:RALLIS,NSE:JUBLCPL,NSE:EMUDHRA
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (25)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [5PAISA](https://in.tradingview.com/chart/?symbol=NSE:5PAISA)<br><sub>📶W9 · W↑6d · ↓CMF2d</sub> | ⚠ CAUTION | Digital discount brokerage for equities, derivatives, commodities trading | ⚡ BULL_ANY_PPV | 94 | 🔄54 | ↑1.028 | ↑1d | SQ·PV | +4.5% | 23.05/21.59 | +4.52% | 20% |
| [FIRSTCRY](https://in.tradingview.com/chart/?symbol=NSE:FIRSTCRY)<br><sub>📶W9 · W↑6d · RVOL124x · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Mothers babies kids products e-commerce retail platform | ⚡ BULL_ANY_PPV | 89 | 🔄13 | ↑1.084 | ↑1d | SQ·PV | +12.8% | -17.51/-30.87 | +12.85% | 20% |
| [KDDL](https://in.tradingview.com/chart/?symbol=NSE:KDDL)<br><sub>📶W9 · W↑6d · 🚀SS·36x · ↑CMF8d</sub> | ✓ SAFE | Watch dials, hands, luxury components manufacturing retail | ⚡ BULL_ANY_PPV | 49 | 🔄94 | ↑1.101 | ↑1d | PV | +16.5% | 43.73/42.57 | +16.52% | 20% |
| [AVTNPL](https://in.tradingview.com/chart/?symbol=NSE:AVTNPL)<br><sub>📶W9 · W↑2d · 🚀SS·12x · ↓CMF7d</sub> | ✓ SAFE | Plant extract manufacturer for food beverage nutrition | ⚡ BULL_ANY_PPV | 49 | 🔄89 | ↑1.036 | ↑1d | PV | +5.6% | 28.23/25.86 | +5.59% | 20% |
| [ARIS](https://in.tradingview.com/chart/?symbol=NSE:ARIS)<br><sub>📶W9 · W↑12d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Digital procurement platform connecting construction material suppliers builders | ⚡ BULL_ANY_PPV | 39 | 🔄72 | ↑1.025 | ↑16d | PV | +11.6% | 42.32/39.29 | +2.11% | 20% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>📶W9 · W↑6d · ↑CMF11d</sub> | ✓ SAFE | Home textiles manufacturer, flooring, global export focus | ⚡ BULL_ANY_PPV | 37 | 🔄97 | ↑1.063 | ↑13d | PV | +25.2% | 37.33/35.52 | +7.92% | 20% |
| [KITEX](https://in.tradingview.com/chart/?symbol=NSE:KITEX)<br><sub>📶W9 · W↑32d · ↑CMF10d</sub> | ✓ SAFE | Organic infant apparel manufacturer export to US Europe | ⚡ BULL_ANY_PPV | 8 | ↑31 | ↑1.048 | ↑12d | PV | +21.5% | 28.39/26.02 | +4.60% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [SHADOWFAX](https://in.tradingview.com/chart/?symbol=NSE:SHADOWFAX)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Digital commerce logistics network, express delivery, asset-light model | 📈 BULL_ANY_MID | 98 | 🔄50 | ↑1.011 | ↑2d | SQ | +2.5% | 26.33/20.64 | +0.50% | 20% |
| [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT)<br><sub>📶W9 · ↑CMF4d</sub> | ✓ SAFE | BPM services: customer care, technical support, back-office processing | 📈 BULL_ANY_MID | 94 | 🔄90 | ↑1.020 | ↑1d | SQ | +1.7% | -0.67/-3.4 | +1.70% | 20% |
| [AJMERA](https://in.tradingview.com/chart/?symbol=NSE:AJMERA)<br><sub>📶W9 · W↑37d · ↑CMF30d</sub> | ✓ SAFE | Luxury and mid-tier residential real estate developer Mumbai focused | 📈 BULL_ANY_MID | 89 | 🔄56 | ↑1.020 | ↑6d | SQ | +4.8% | 39.45/36.19 | +2.43% | 20% |
| [VIJAYA](https://in.tradingview.com/chart/?symbol=NSE:VIJAYA)<br><sub>📶W9 · ↑CMF17d</sub> | ✓ SAFE | Diagnostic imaging and pathology labs, Southern India healthcare | 📈 BULL_ANY_MID | 58 | ↑80 | ↓1.013 | ↑2d | SQ | +4.1% | 15.61/9.69 | -1.35% | 20% |
| [BHARTIHEXA](https://in.tradingview.com/chart/?symbol=NSE:BHARTIHEXA)<br><sub>📶W9 · W↑27d · ↓CMF3d</sub> | ⚠ CAUTION | Mobile telecom operator Rajasthan Northeast circles consumer | 📈 BULL_ANY_MID | 57 | ↓58 | ↓1.004 | ↑3d | SQ | +5.0% | 19.52/15.73 | -2.18% | 20% |
| [ARIHANTCAP](https://in.tradingview.com/chart/?symbol=NSE:ARIHANTCAP)<br><sub>📶W9 · W↑2d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 54 | 🔄82 | ↑1.020 | ↑1d | — | +3.1% | 14.62/13.86 | +3.10% | 20% |
| [LOTUSDEV](https://in.tradingview.com/chart/?symbol=NSE:LOTUSDEV)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Residential redevelopment, ultra-luxury housing, Mumbai metropolitan area | 📈 BULL_ANY_MID | 53 | ↓93 | ↑1.005 | ↓17d | SQ | +3.1% | -10.88/-14.44 | +0.34% | 20% |
| [AYMSYNTEX](https://in.tradingview.com/chart/?symbol=NSE:AYMSYNTEX)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Polyester nylon filament yarn textiles manufacturing | 📈 BULL_ANY_MID | 53 | 🔄86 | ↑1.025 | ↑2d | — | +4.1% | 8.57/3.34 | +2.16% | 20% |
| [NUVOCO](https://in.tradingview.com/chart/?symbol=NSE:NUVOCO)<br><sub>📶W9 · W↑22d · ↓CMF21d</sub> | ⚠ CAUTION | Cement and ready-mix concrete manufacturer East North India | 📈 BULL_ANY_MID | 48 | ↓62 | ↓1.009 | ↑12d | SQ | +7.8% | 37.6/34.55 | +0.03% | 20% |
| [ACC](https://in.tradingview.com/chart/?symbol=NSE:ACC)<br><sub>📶W9 · W↑17d · ↑CMF15d</sub> | ⚠ CAUTION | Cement and ready-mix concrete for construction infrastructure | 📈 BULL_ANY_MID | 44 | 🔄23 | ↑1.021 | ↑11d | — | +8.4% | 32.84/32.81 | +2.07% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄54 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [SALSTEEL](https://in.tradingview.com/chart/?symbol=NSE:SALSTEEL)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Sponge iron and ferroalloys manufacturer serving domestic steel mills | 📈 BULL_ANY_MID | 18 | ↑95 | ↓1.014 | ↑2d | — | +4.9% | 17.13/15.92 | -0.12% | 5% 🟥 |
| [NH](https://in.tradingview.com/chart/?symbol=NSE:NH)<br><sub>📶W9 · W↑12d · ↑CMF15d</sub> | ⚠ CAUTION | Affordable cardiac surgery and multispecialty hospitals across India | 📈 BULL_ANY_MID | 9 | ↑60 | ↑1.020 | ↑16d | — | +14.8% | 32.46/30.44 | +0.65% | 20% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>📶W9 · W↑11d · ↑CMF13d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓60 | ↓1.007 | ↑15d | — | +7.0% | 46.27/45.57 | -0.67% | 20% |
| [SPECTRUM](https://in.tradingview.com/chart/?symbol=NSE:SPECTRUM)<br><sub>📶W9 · W↑6d · ★ · ↑CMF30d</sub> | ✓ SAFE | Injection moulded electrical components OEM for automotive applications | 📈 BULL_ANY_MID | 5 | ↑99 | ↓1.034 | ↑15d | — | +23.8% | 64.96/64.81 | -1.86% | 20% |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH)<br><sub>📶W9 · W↑12d · ★ · ↑CMF16d</sub> | ✓ SAFE | Automotive lamps, plastic parts, chassis for vehicles | 📈 BULL_ANY_MID | 4 | ↑91 | ↑1.060 | ↑16d | — | +30.0% | 50.37/48.69 | +4.10% | 20% |
| [SURAKSHA](https://in.tradingview.com/chart/?symbol=NSE:SURAKSHA)<br><sub>📶W9 · W↑6d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Pathology radiology diagnostic centers East India healthcare | 📈 BULL_ANY_MID | 3 | ↑76 | ↑1.036 | ↑17d | — | +18.1% | 39.03/38.54 | +3.05% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:5PAISA,NSE:FIRSTCRY,NSE:KDDL,NSE:AVTNPL,NSE:ARIS,NSE:WELSPUNLIV,NSE:KITEX,NSE:SIGMAADV,NSE:SHADOWFAX,NSE:ONEPOINT,NSE:AJMERA,NSE:VIJAYA,NSE:BHARTIHEXA,NSE:ARIHANTCAP,NSE:LOTUSDEV,NSE:AYMSYNTEX,NSE:NUVOCO,NSE:ACC,NSE:TATACONSUM,NSE:SALSTEEL,NSE:NH,NSE:EICHERMOT,NSE:SPECTRUM,NSE:LUMAXTECH,NSE:SURAKSHA
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (31)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [5PAISA](https://in.tradingview.com/chart/?symbol=NSE:5PAISA)<br><sub>📶W9 · W↑6d · ↓CMF2d</sub> | ⚠ CAUTION | Digital discount brokerage for equities, derivatives, commodities trading | ⚡ BULL_ANY_PPV | 94 | 🔄54 | ↑1.028 | ↑1d | SQ·PV | +4.5% | 23.05/21.59 | +4.52% | 20% |
| [FIRSTCRY](https://in.tradingview.com/chart/?symbol=NSE:FIRSTCRY)<br><sub>📶W9 · W↑6d · RVOL124x · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Mothers babies kids products e-commerce retail platform | ⚡ BULL_ANY_PPV | 89 | 🔄13 | ↑1.084 | ↑1d | SQ·PV | +12.8% | -17.51/-30.87 | +12.85% | 20% |
| [KDDL](https://in.tradingview.com/chart/?symbol=NSE:KDDL)<br><sub>📶W9 · W↑6d · 🚀SS·36x · ↑CMF8d</sub> | ✓ SAFE | Watch dials, hands, luxury components manufacturing retail | ⚡ BULL_ANY_PPV | 49 | 🔄94 | ↑1.101 | ↑1d | PV | +16.5% | 43.73/42.57 | +16.52% | 20% |
| [AVTNPL](https://in.tradingview.com/chart/?symbol=NSE:AVTNPL)<br><sub>📶W9 · W↑2d · 🚀SS·12x · ↓CMF7d</sub> | ✓ SAFE | Plant extract manufacturer for food beverage nutrition | ⚡ BULL_ANY_PPV | 49 | 🔄89 | ↑1.036 | ↑1d | PV | +5.6% | 28.23/25.86 | +5.59% | 20% |
| [ARIS](https://in.tradingview.com/chart/?symbol=NSE:ARIS)<br><sub>📶W9 · W↑12d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Digital procurement platform connecting construction material suppliers builders | ⚡ BULL_ANY_PPV | 39 | 🔄72 | ↑1.025 | ↑16d | PV | +11.6% | 42.32/39.29 | +2.11% | 20% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>📶W9 · W↑6d · ↑CMF11d</sub> | ✓ SAFE | Home textiles manufacturer, flooring, global export focus | ⚡ BULL_ANY_PPV | 37 | 🔄97 | ↑1.063 | ↑13d | PV | +25.2% | 37.33/35.52 | +7.92% | 20% |
| [KITEX](https://in.tradingview.com/chart/?symbol=NSE:KITEX)<br><sub>📶W9 · W↑32d · ↑CMF10d</sub> | ✓ SAFE | Organic infant apparel manufacturer export to US Europe | ⚡ BULL_ANY_PPV | 8 | ↑31 | ↑1.048 | ↑12d | PV | +21.5% | 28.39/26.02 | +4.60% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [SHADOWFAX](https://in.tradingview.com/chart/?symbol=NSE:SHADOWFAX)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Digital commerce logistics network, express delivery, asset-light model | 📈 BULL_ANY_MID | 98 | 🔄50 | ↑1.011 | ↑2d | SQ | +2.5% | 26.33/20.64 | +0.50% | 20% |
| [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT)<br><sub>📶W9 · ↑CMF4d</sub> | ✓ SAFE | BPM services: customer care, technical support, back-office processing | 📈 BULL_ANY_MID | 94 | 🔄90 | ↑1.020 | ↑1d | SQ | +1.7% | -0.67/-3.4 | +1.70% | 20% |
| [AJMERA](https://in.tradingview.com/chart/?symbol=NSE:AJMERA)<br><sub>📶W9 · W↑37d · ↑CMF30d</sub> | ✓ SAFE | Luxury and mid-tier residential real estate developer Mumbai focused | 📈 BULL_ANY_MID | 89 | 🔄56 | ↑1.020 | ↑6d | SQ | +4.8% | 39.45/36.19 | +2.43% | 20% |
| [VIJAYA](https://in.tradingview.com/chart/?symbol=NSE:VIJAYA)<br><sub>📶W9 · ↑CMF17d</sub> | ✓ SAFE | Diagnostic imaging and pathology labs, Southern India healthcare | 📈 BULL_ANY_MID | 58 | ↑80 | ↓1.013 | ↑2d | SQ | +4.1% | 15.61/9.69 | -1.35% | 20% |
| [ARIHANTCAP](https://in.tradingview.com/chart/?symbol=NSE:ARIHANTCAP)<br><sub>📶W9 · W↑2d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 54 | 🔄82 | ↑1.020 | ↑1d | — | +3.1% | 14.62/13.86 | +3.10% | 20% |
| [AYMSYNTEX](https://in.tradingview.com/chart/?symbol=NSE:AYMSYNTEX)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Polyester nylon filament yarn textiles manufacturing | 📈 BULL_ANY_MID | 53 | 🔄86 | ↑1.025 | ↑2d | — | +4.1% | 8.57/3.34 | +2.16% | 20% |
| [ACC](https://in.tradingview.com/chart/?symbol=NSE:ACC)<br><sub>📶W9 · W↑17d · ↑CMF15d</sub> | ⚠ CAUTION | Cement and ready-mix concrete for construction infrastructure | 📈 BULL_ANY_MID | 44 | 🔄23 | ↑1.021 | ↑11d | — | +8.4% | 32.84/32.81 | +2.07% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄54 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [SALSTEEL](https://in.tradingview.com/chart/?symbol=NSE:SALSTEEL)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Sponge iron and ferroalloys manufacturer serving domestic steel mills | 📈 BULL_ANY_MID | 18 | ↑95 | ↓1.014 | ↑2d | — | +4.9% | 17.13/15.92 | -0.12% | 5% 🟥 |
| [NH](https://in.tradingview.com/chart/?symbol=NSE:NH)<br><sub>📶W9 · W↑12d · ↑CMF15d</sub> | ⚠ CAUTION | Affordable cardiac surgery and multispecialty hospitals across India | 📈 BULL_ANY_MID | 9 | ↑60 | ↑1.020 | ↑16d | — | +14.8% | 32.46/30.44 | +0.65% | 20% |
| [SPECTRUM](https://in.tradingview.com/chart/?symbol=NSE:SPECTRUM)<br><sub>📶W9 · W↑6d · ★ · ↑CMF30d</sub> | ✓ SAFE | Injection moulded electrical components OEM for automotive applications | 📈 BULL_ANY_MID | 5 | ↑99 | ↓1.034 | ↑15d | — | +23.8% | 64.96/64.81 | -1.86% | 20% |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH)<br><sub>📶W9 · W↑12d · ★ · ↑CMF16d</sub> | ✓ SAFE | Automotive lamps, plastic parts, chassis for vehicles | 📈 BULL_ANY_MID | 4 | ↑91 | ↑1.060 | ↑16d | — | +30.0% | 50.37/48.69 | +4.10% | 20% |
| [SURAKSHA](https://in.tradingview.com/chart/?symbol=NSE:SURAKSHA)<br><sub>📶W9 · W↑6d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Pathology radiology diagnostic centers East India healthcare | 📈 BULL_ANY_MID | 3 | ↑76 | ↑1.036 | ↑17d | — | +18.1% | 39.03/38.54 | +3.05% | 20% |
| [BRIGADE](https://in.tradingview.com/chart/?symbol=NSE:BRIGADE)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Residential apartments, office spaces, South India developer | ⚡ BULL_ANY_PPV | 94 | 🔄12 | ↑1.017 | ↑1d | SQ·PV | +3.4% | -8.65/-11.59 | +3.37% | 20% |
| [KAMAHOLD](https://in.tradingview.com/chart/?symbol=NSE:KAMAHOLD)<br><sub>🚀SS·9x · ↑CMF0d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 89 | 🔄50 | ↑1.031 | ↑1d | SQ·PV | +4.1% | -21.13/-33.71 | +4.14% | 5% |
| [UGROCAP](https://in.tradingview.com/chart/?symbol=NSE:UGROCAP)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | MSME lending platform, technology-driven credit scoring | ⚡ BULL_ANY_PPV | 49 | 🔄3 | ↑1.035 | ↑1d | PV | +4.9% | -51.12/-59.56 | +4.86% | 20% |
| [PGIL](https://in.tradingview.com/chart/?symbol=NSE:PGIL)<br><sub>↑CMF14d</sub> | ✓ SAFE | Apparel manufacturer, exports to global fashion brands | ⚡ BULL_ANY_PPV | 43 | 🔄5 | ↑1.027 | ↑12d | PV | +14.7% | 24.14/24.04 | +4.07% | 20% |
| [VIPIND](https://in.tradingview.com/chart/?symbol=NSE:VIPIND)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Luggage and travel bags manufacturer for domestic and international markets | 🟡 BULL_OS_L2 | 54 | 🔄10 | ↑1.024 | ↑1d | — | +4.6% | -52.48/-56.56 | +4.60% | 20% |
| [AMAGI](https://in.tradingview.com/chart/?symbol=NSE:AMAGI)<br><sub>↓CMF28d</sub> | ✓ SAFE | Cloud SaaS platform for broadcast streaming content monetization | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.010 | ↑1d | SQ | +1.3% | -13.97/-15.62 | +1.34% | 20% |
| [INDPRUD](https://in.tradingview.com/chart/?symbol=NSE:INDPRUD)<br><sub>🚀SS · ↓CMF20d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.025 | ↑1d | SQ | +5.8% | -18.67/-23.34 | +5.75% | 20% |
| [DBREALTY](https://in.tradingview.com/chart/?symbol=NSE:DBREALTY)<br><sub>W↑6d · ↓CMF30d</sub> | ✓ SAFE | Residential commercial real estate development Mumbai projects | 📈 BULL_ANY_MID | 90 | 🔄8 | ↑1.029 | ↑5d | SQ | +5.6% | 7.17/3.8 | +3.63% | 10% 🟩 |
| [SHOPERSTOP](https://in.tradingview.com/chart/?symbol=NSE:SHOPERSTOP)<br><sub>↑CMF2d · DEL53%</sub> | ✓ SAFE | Department store operator, fashion beauty retail, urban consumers | 📈 BULL_ANY_MID | 58 | 🔄41 | ↑1.011 | ↑2d | — | +2.3% | 12.18/9.36 | +0.85% | 20% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>↑CMF3d</sub> | ✓ SAFE | Glass-lined reactors and process equipment for pharma chemicals | 📈 BULL_ANY_MID | 44 | 🔄98 | ↑1.007 | ↓16d | — | +4.0% | -19.9/-20.33 | +2.72% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:5PAISA,NSE:FIRSTCRY,NSE:KDDL,NSE:AVTNPL,NSE:ARIS,NSE:WELSPUNLIV,NSE:KITEX,NSE:SIGMAADV,NSE:SHADOWFAX,NSE:ONEPOINT,NSE:AJMERA,NSE:VIJAYA,NSE:ARIHANTCAP,NSE:AYMSYNTEX,NSE:ACC,NSE:TATACONSUM,NSE:SALSTEEL,NSE:NH,NSE:SPECTRUM,NSE:LUMAXTECH,NSE:SURAKSHA,NSE:BRIGADE,NSE:KAMAHOLD,NSE:UGROCAP,NSE:PGIL,NSE:VIPIND,NSE:AMAGI,NSE:INDPRUD,NSE:DBREALTY,NSE:SHOPERSTOP,NSE:SETL
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (20)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [5PAISA](https://in.tradingview.com/chart/?symbol=NSE:5PAISA)<br><sub>📶W9 · W↑6d · ↓CMF2d</sub> | ⚠ CAUTION | Digital discount brokerage for equities, derivatives, commodities trading | ⚡ BULL_ANY_PPV | 94 | 🔄54 | ↑1.028 | ↑1d | SQ·PV | +4.5% | 23.05/21.59 | +4.52% | 20% |
| [FIRSTCRY](https://in.tradingview.com/chart/?symbol=NSE:FIRSTCRY)<br><sub>📶W9 · W↑6d · RVOL124x · ↑CMF0d · ÷DIV</sub> | ✓ SAFE | Mothers babies kids products e-commerce retail platform | ⚡ BULL_ANY_PPV | 89 | 🔄13 | ↑1.084 | ↑1d | SQ·PV | +12.8% | -17.51/-30.87 | +12.85% | 20% |
| [SHADOWFAX](https://in.tradingview.com/chart/?symbol=NSE:SHADOWFAX)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Digital commerce logistics network, express delivery, asset-light model | 📈 BULL_ANY_MID | 98 | 🔄50 | ↑1.011 | ↑2d | SQ | +2.5% | 26.33/20.64 | +0.50% | 20% |
| [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT)<br><sub>📶W9 · ↑CMF4d</sub> | ✓ SAFE | BPM services: customer care, technical support, back-office processing | 📈 BULL_ANY_MID | 94 | 🔄90 | ↑1.020 | ↑1d | SQ | +1.7% | -0.67/-3.4 | +1.70% | 20% |
| [AJMERA](https://in.tradingview.com/chart/?symbol=NSE:AJMERA)<br><sub>📶W9 · W↑37d · ↑CMF30d</sub> | ✓ SAFE | Luxury and mid-tier residential real estate developer Mumbai focused | 📈 BULL_ANY_MID | 89 | 🔄56 | ↑1.020 | ↑6d | SQ | +4.8% | 39.45/36.19 | +2.43% | 20% |
| [VIJAYA](https://in.tradingview.com/chart/?symbol=NSE:VIJAYA)<br><sub>📶W9 · ↑CMF17d</sub> | ✓ SAFE | Diagnostic imaging and pathology labs, Southern India healthcare | 📈 BULL_ANY_MID | 58 | ↑80 | ↓1.013 | ↑2d | SQ | +4.1% | 15.61/9.69 | -1.35% | 20% |
| [BHARTIHEXA](https://in.tradingview.com/chart/?symbol=NSE:BHARTIHEXA)<br><sub>📶W9 · W↑27d · ↓CMF3d</sub> | ⚠ CAUTION | Mobile telecom operator Rajasthan Northeast circles consumer | 📈 BULL_ANY_MID | 57 | ↓58 | ↓1.004 | ↑3d | SQ | +5.0% | 19.52/15.73 | -2.18% | 20% |
| [LOTUSDEV](https://in.tradingview.com/chart/?symbol=NSE:LOTUSDEV)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Residential redevelopment, ultra-luxury housing, Mumbai metropolitan area | 📈 BULL_ANY_MID | 53 | ↓93 | ↑1.005 | ↓17d | SQ | +3.1% | -10.88/-14.44 | +0.34% | 20% |
| [NUVOCO](https://in.tradingview.com/chart/?symbol=NSE:NUVOCO)<br><sub>📶W9 · W↑22d · ↓CMF21d</sub> | ⚠ CAUTION | Cement and ready-mix concrete manufacturer East North India | 📈 BULL_ANY_MID | 48 | ↓62 | ↓1.009 | ↑12d | SQ | +7.8% | 37.6/34.55 | +0.03% | 20% |
| [BRIGADE](https://in.tradingview.com/chart/?symbol=NSE:BRIGADE)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Residential apartments, office spaces, South India developer | ⚡ BULL_ANY_PPV | 94 | 🔄12 | ↑1.017 | ↑1d | SQ·PV | +3.4% | -8.65/-11.59 | +3.37% | 20% |
| [KAMAHOLD](https://in.tradingview.com/chart/?symbol=NSE:KAMAHOLD)<br><sub>🚀SS·9x · ↑CMF0d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 89 | 🔄50 | ↑1.031 | ↑1d | SQ·PV | +4.1% | -21.13/-33.71 | +4.14% | 5% |
| [MEDIASSIST](https://in.tradingview.com/chart/?symbol=NSE:MEDIASSIST)<br><sub>W↑2d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Health claims processing and network management for insurers | ⚡ BULL_ANY_PPV | 69 | ↓7 | ↑1.005 | ↑1d | SQ·PV | +1.5% | -45.89/-49.39 | +1.49% | 20% |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON)<br><sub>🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Pistons rings valves manufacturer automotive OEM export | ⚡ BULL_ANY_PPV | 63 | ↓83 | ↑1.001 | ↓7d | SQ·PV | +1.1% | -26.41/-27.8 | +0.66% | 20% |
| [GARFIBRES](https://in.tradingview.com/chart/?symbol=NSE:GARFIBRES)<br><sub>↓CMF12d · ⚠️TRAP</sub> | ⚠ CAUTION | Technical textiles and ropes for agriculture aquaculture infrastructure | 🟡 BULL_OS_L2 | 50 | ↓56 | ↓0.998 | ↓10d | SQ | -1.4% | -52.13/-55.64 | -0.42% | 20% |
| [AMAGI](https://in.tradingview.com/chart/?symbol=NSE:AMAGI)<br><sub>↓CMF28d</sub> | ✓ SAFE | Cloud SaaS platform for broadcast streaming content monetization | 📈 BULL_ANY_MID | 99 | 🔄50 | ↑1.010 | ↑1d | SQ | +1.3% | -13.97/-15.62 | +1.34% | 20% |
| [INDPRUD](https://in.tradingview.com/chart/?symbol=NSE:INDPRUD)<br><sub>🚀SS · ↓CMF20d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 94 | 🔄50 | ↑1.025 | ↑1d | SQ | +5.8% | -18.67/-23.34 | +5.75% | 20% |
| [DBREALTY](https://in.tradingview.com/chart/?symbol=NSE:DBREALTY)<br><sub>W↑6d · ↓CMF30d</sub> | ✓ SAFE | Residential commercial real estate development Mumbai projects | 📈 BULL_ANY_MID | 90 | 🔄8 | ↑1.029 | ↑5d | SQ | +5.6% | 7.17/3.8 | +3.63% | 10% 🟩 |
| [DODLA](https://in.tradingview.com/chart/?symbol=NSE:DODLA)<br><sub>↓CMF30d · ÷DIV</sub> | ⚠ CAUTION | Milk, curd, ghee processor South India consumer | 📈 BULL_ANY_MID | 58 | ↓23 | ↑1.001 | ↓12d | SQ | -0.2% | -40.94/-42.64 | +0.24% | 20% |
| [ASHAPURMIN](https://in.tradingview.com/chart/?symbol=NSE:ASHAPURMIN)<br><sub>↓CMF30d · ÷DIV</sub> | ✓ SAFE | Bauxite mining processing distribution industrial minerals global | 📈 BULL_ANY_MID | 56 | ↓3 | ↑0.993 | ↓9d | SQ | -4.4% | -51.29/-52.02 | +2.28% | 20% |
| [NRBBEARING](https://in.tradingview.com/chart/?symbol=NSE:NRBBEARING)<br><sub>↓CMF22d · ⚠️TRAP</sub> | ✓ SAFE | Needle roller bearings manufacturer automotive industrial applications | 📈 BULL_ANY_MID | 55 | ↓77 | ↑0.987 | ↓10d | SQ | -7.1% | -46.3/-46.36 | +0.00% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:5PAISA,NSE:FIRSTCRY,NSE:SHADOWFAX,NSE:ONEPOINT,NSE:AJMERA,NSE:VIJAYA,NSE:BHARTIHEXA,NSE:LOTUSDEV,NSE:NUVOCO,NSE:BRIGADE,NSE:KAMAHOLD,NSE:MEDIASSIST,NSE:SHRIPISTON,NSE:GARFIBRES,NSE:AMAGI,NSE:INDPRUD,NSE:DBREALTY,NSE:DODLA,NSE:ASHAPURMIN,NSE:NRBBEARING
```

---

### 🔥 MAJOR — PPV confirmed (8)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [KDDL](https://in.tradingview.com/chart/?symbol=NSE:KDDL)<br><sub>📶W9 · W↑6d · 🚀SS·36x · ↑CMF8d</sub> | ✓ SAFE | Watch dials, hands, luxury components manufacturing retail | ⚡ BULL_ANY_PPV | 49 | 🔄94 | ↑1.101 | ↑1d | PV | +16.5% | 43.73/42.57 | +16.52% | 20% |
| [AVTNPL](https://in.tradingview.com/chart/?symbol=NSE:AVTNPL)<br><sub>📶W9 · W↑2d · 🚀SS·12x · ↓CMF7d</sub> | ✓ SAFE | Plant extract manufacturer for food beverage nutrition | ⚡ BULL_ANY_PPV | 49 | 🔄89 | ↑1.036 | ↑1d | PV | +5.6% | 28.23/25.86 | +5.59% | 20% |
| [ARIS](https://in.tradingview.com/chart/?symbol=NSE:ARIS)<br><sub>📶W9 · W↑12d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Digital procurement platform connecting construction material suppliers builders | ⚡ BULL_ANY_PPV | 39 | 🔄72 | ↑1.025 | ↑16d | PV | +11.6% | 42.32/39.29 | +2.11% | 20% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>📶W9 · W↑6d · ↑CMF11d</sub> | ✓ SAFE | Home textiles manufacturer, flooring, global export focus | ⚡ BULL_ANY_PPV | 37 | 🔄97 | ↑1.063 | ↑13d | PV | +25.2% | 37.33/35.52 | +7.92% | 20% |
| [KITEX](https://in.tradingview.com/chart/?symbol=NSE:KITEX)<br><sub>📶W9 · W↑32d · ↑CMF10d</sub> | ✓ SAFE | Organic infant apparel manufacturer export to US Europe | ⚡ BULL_ANY_PPV | 8 | ↑31 | ↑1.048 | ↑12d | PV | +21.5% | 28.39/26.02 | +4.60% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [UGROCAP](https://in.tradingview.com/chart/?symbol=NSE:UGROCAP)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | MSME lending platform, technology-driven credit scoring | ⚡ BULL_ANY_PPV | 49 | 🔄3 | ↑1.035 | ↑1d | PV | +4.9% | -51.12/-59.56 | +4.86% | 20% |
| [PGIL](https://in.tradingview.com/chart/?symbol=NSE:PGIL)<br><sub>↑CMF14d</sub> | ✓ SAFE | Apparel manufacturer, exports to global fashion brands | ⚡ BULL_ANY_PPV | 43 | 🔄5 | ↑1.027 | ↑12d | PV | +14.7% | 24.14/24.04 | +4.07% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:KDDL,NSE:AVTNPL,NSE:ARIS,NSE:WELSPUNLIV,NSE:KITEX,NSE:SIGMAADV,NSE:UGROCAP,NSE:PGIL
```

### 🟢 OVERSOLD — reversal from −53/−60 (4)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [SUPRIYA](https://in.tradingview.com/chart/?symbol=NSE:SUPRIYA)<br><sub>↓CMF19d · ⚠️TRAP</sub> | ✓ SAFE | API manufacturer, antihistamine analgesic anaesthetic pharma exports | 🟢 BULL_OVERSOLD | 15 | ↓14 | ↑0.915 | ↓10d | — | -25.5% | -65.18/-66.11 | -0.27% | 20% |
| [VIPIND](https://in.tradingview.com/chart/?symbol=NSE:VIPIND)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Luggage and travel bags manufacturer for domestic and international markets | 🟡 BULL_OS_L2 | 54 | 🔄10 | ↑1.024 | ↑1d | — | +4.6% | -52.48/-56.56 | +4.60% | 20% |
| [NSIL](https://in.tradingview.com/chart/?symbol=NSE:NSIL)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION |  | 🟡 BULL_OS_L2 | 15 | ↓25 | ↑0.991 | ↓10d | — | -4.0% | -54.96/-55.26 | +1.98% | 5% |
| [RAIN](https://in.tradingview.com/chart/?symbol=NSE:RAIN)<br><sub>🚀SS · ↓CMF12d · 🎯SLING</sub> | ✓ SAFE | Calcined coke, cement, advanced materials production globally | 🟡 BULL_OS_L2 | 5 | ↓59 | ↑0.963 | ↓28d | — | -21.7% | -56.91/-57.52 | +2.19% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SUPRIYA,NSE:VIPIND,NSE:NSIL,NSE:RAIN
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (16)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ARIHANTCAP](https://in.tradingview.com/chart/?symbol=NSE:ARIHANTCAP)<br><sub>📶W9 · W↑2d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 54 | 🔄82 | ↑1.020 | ↑1d | — | +3.1% | 14.62/13.86 | +3.10% | 20% |
| [AYMSYNTEX](https://in.tradingview.com/chart/?symbol=NSE:AYMSYNTEX)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Polyester nylon filament yarn textiles manufacturing | 📈 BULL_ANY_MID | 53 | 🔄86 | ↑1.025 | ↑2d | — | +4.1% | 8.57/3.34 | +2.16% | 20% |
| [ACC](https://in.tradingview.com/chart/?symbol=NSE:ACC)<br><sub>📶W9 · W↑17d · ↑CMF15d</sub> | ⚠ CAUTION | Cement and ready-mix concrete for construction infrastructure | 📈 BULL_ANY_MID | 44 | 🔄23 | ↑1.021 | ↑11d | — | +8.4% | 32.84/32.81 | +2.07% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄54 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [SALSTEEL](https://in.tradingview.com/chart/?symbol=NSE:SALSTEEL)<br><sub>📶W9 · ↓CMF1d</sub> | ✓ SAFE | Sponge iron and ferroalloys manufacturer serving domestic steel mills | 📈 BULL_ANY_MID | 18 | ↑95 | ↓1.014 | ↑2d | — | +4.9% | 17.13/15.92 | -0.12% | 5% 🟥 |
| [NH](https://in.tradingview.com/chart/?symbol=NSE:NH)<br><sub>📶W9 · W↑12d · ↑CMF15d</sub> | ⚠ CAUTION | Affordable cardiac surgery and multispecialty hospitals across India | 📈 BULL_ANY_MID | 9 | ↑60 | ↑1.020 | ↑16d | — | +14.8% | 32.46/30.44 | +0.65% | 20% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>📶W9 · W↑11d · ↑CMF13d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓60 | ↓1.007 | ↑15d | — | +7.0% | 46.27/45.57 | -0.67% | 20% |
| [SPECTRUM](https://in.tradingview.com/chart/?symbol=NSE:SPECTRUM)<br><sub>📶W9 · W↑6d · ★ · ↑CMF30d</sub> | ✓ SAFE | Injection moulded electrical components OEM for automotive applications | 📈 BULL_ANY_MID | 5 | ↑99 | ↓1.034 | ↑15d | — | +23.8% | 64.96/64.81 | -1.86% | 20% |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH)<br><sub>📶W9 · W↑12d · ★ · ↑CMF16d</sub> | ✓ SAFE | Automotive lamps, plastic parts, chassis for vehicles | 📈 BULL_ANY_MID | 4 | ↑91 | ↑1.060 | ↑16d | — | +30.0% | 50.37/48.69 | +4.10% | 20% |
| [SURAKSHA](https://in.tradingview.com/chart/?symbol=NSE:SURAKSHA)<br><sub>📶W9 · W↑6d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Pathology radiology diagnostic centers East India healthcare | 📈 BULL_ANY_MID | 3 | ↑76 | ↑1.036 | ↑17d | — | +18.1% | 39.03/38.54 | +3.05% | 20% |
| [SHOPERSTOP](https://in.tradingview.com/chart/?symbol=NSE:SHOPERSTOP)<br><sub>↑CMF2d · DEL53%</sub> | ✓ SAFE | Department store operator, fashion beauty retail, urban consumers | 📈 BULL_ANY_MID | 58 | 🔄41 | ↑1.011 | ↑2d | — | +2.3% | 12.18/9.36 | +0.85% | 20% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>↑CMF3d</sub> | ✓ SAFE | Glass-lined reactors and process equipment for pharma chemicals | 📈 BULL_ANY_MID | 44 | 🔄98 | ↑1.007 | ↓16d | — | +4.0% | -19.9/-20.33 | +2.72% | 20% |
| [AWL](https://in.tradingview.com/chart/?symbol=NSE:AWL)<br><sub>🚀SS · ↑CMF0d</sub> | ✓ SAFE | Edible oils wheat flour rice pulses sugar FMCG | 📈 BULL_ANY_MID | 29 | ↓17 | ↑1.008 | ↑1d | — | +1.9% | -34.72/-35.74 | +1.94% | 20% |
| [RALLIS](https://in.tradingview.com/chart/?symbol=NSE:RALLIS)<br><sub>W↑2d · 🚀SS · ↓CMF2d</sub> | ✓ SAFE | Agrochemicals, seeds, crop nutrients for Indian farmers | 📈 BULL_ANY_MID | 29 | ↓13 | ↑1.007 | ↑1d | — | +2.0% | -29.46/-30.24 | +2.02% | 20% |
| [JUBLCPL](https://in.tradingview.com/chart/?symbol=NSE:JUBLCPL)<br><sub>🚀SS · ↑CMF11d</sub> | ⚠ CAUTION | Agri nutrients, polymers, chemicals manufacturer for farms and industry | 📈 BULL_ANY_MID | 8 | ↓29 | ↑1.000 | ↓17d | — | +1.1% | -29.91/-31.21 | +2.09% | 20% |
| [EMUDHRA](https://in.tradingview.com/chart/?symbol=NSE:EMUDHRA)<br><sub>↓CMF24d</sub> | ✓ SAFE | Digital signatures, PKI certificates, enterprise cybersecurity India | 📈 BULL_ANY_MID | 5 | ↓4 | ↑0.991 | ↓31d | — | -40.0% | -37.23/-37.62 | +1.85% | 10% 🟨 |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ARIHANTCAP,NSE:AYMSYNTEX,NSE:ACC,NSE:TATACONSUM,NSE:SALSTEEL,NSE:NH,NSE:EICHERMOT,NSE:SPECTRUM,NSE:LUMAXTECH,NSE:SURAKSHA,NSE:SHOPERSTOP,NSE:SETL,NSE:AWL,NSE:RALLIS,NSE:JUBLCPL,NSE:EMUDHRA
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
