> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-11-18
*Generated 2026-11-18 15:49 IST*

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

**Total bull crosses today: 39** · 13 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GREENLAM,NSE:APOLLOPIPE,NSE:INDIASHLTR,NSE:NDRAUTO,NSE:BBTC,NSE:KPIGREEN,NSE:WEL,NSE:PNBGILTS,NSE:SIGMAADV,NSE:KOLTEPATIL,NSE:TSFINV,NSE:MOBIKWIK,NSE:LMW,NSE:TATACONSUM,NSE:GRWRHITECH,NSE:THELEELA,NSE:TFCILTD,NSE:FORCEMOT,NSE:EICHERMOT,NSE:CEMPRO,NSE:ITCHOTELS,NSE:WESTLIFE,NSE:PVRINOX,NSE:VESUVIUS,NSE:ADVAIT,NSE:ARVINDFASN,NSE:RATEGAIN,NSE:ASHIANA,NSE:RSL,NSE:INSECTICID,NSE:PILANIINVS,NSE:BLSE,NSE:GARUDA,NSE:HCG,NSE:PFOCUS,NSE:DHANUKA,NSE:STOVEKRAFT,NSE:KMEW,NSE:GANECOS
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (23)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GREENLAM](https://in.tradingview.com/chart/?symbol=NSE:GREENLAM)<br><sub>📶W9 · W↑3d · RVOL68x · ↑CMF0d</sub> | ✓ SAFE | Laminate sheets and decorative veneers for furniture makers | ⚡ BULL_ANY_PPV | 89 | 🔄42 | ↑1.077 | ↑1d | SQ·PV | +10.6% | -11.46/-24.31 | +10.61% | 20% |
| [APOLLOPIPE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOPIPE)<br><sub>📶W9 · ↑CMF14d</sub> | ✓ SAFE | PVC HDPE pipes agriculture water construction infrastructure | ⚡ BULL_ANY_PPV | 89 | 🔄85 | ↑1.075 | ↑1d | SQ·PV | +10.5% | -7.61/-21.01 | +10.54% | 20% |
| [INDIASHLTR](https://in.tradingview.com/chart/?symbol=NSE:INDIASHLTR)<br><sub>📶W9 · W↑18d · RVOL12x · ↑CMF0d</sub> | ⚠ CAUTION | Housing loans for low income tier 2 3 cities | ⚡ BULL_ANY_PPV | 88 | 🔄33 | ↑1.047 | ↑2d | SQ·PV | +8.6% | -15.32/-25.97 | +5.30% | 20% |
| [NDRAUTO](https://in.tradingview.com/chart/?symbol=NSE:NDRAUTO)<br><sub>📶W9 · W↑13d · 🚀SS·60x · ↑CMF11d</sub> | ✓ SAFE | Automotive seat frames trims supplier passenger vehicles OEM | ⚡ BULL_ANY_PPV | 48 | 🔄54 | ↑1.055 | ↑2d | PV | +9.1% | 20.66/17.79 | +7.81% | 20% |
| [BBTC](https://in.tradingview.com/chart/?symbol=NSE:BBTC)<br><sub>📶W9 · W↑7d · RVOL13x · ↑CMF5d</sub> | ✓ SAFE | Teak trading, plantations, timber, diversified conglomerate, legacy Indian | ⚡ BULL_ANY_PPV | 37 | 🔄20 | ↑1.032 | ↑13d | PV | +15.1% | 17.59/16.68 | +5.04% | 20% |
| [KPIGREEN](https://in.tradingview.com/chart/?symbol=NSE:KPIGREEN)<br><sub>📶W9 · W↑7d · ↑CMF1d</sub> | ✓ SAFE | Solar wind hybrid power projects independent producer | ⚡ BULL_ANY_PPV | 18 | ↑27 | ↑1.033 | ↑2d | PV | +9.4% | 13.54/11.9 | +1.51% | 20% |
| [WEL](https://in.tradingview.com/chart/?symbol=NSE:WEL)<br><sub>📶W9 · W↑7d · ↑CMF0d</sub> | ⚠ CAUTION | Ceiling fans, exhaust fans, pedestal fans, BLDC motors | ⚡ BULL_ANY_PPV | 18 | ↑2 | ↑1.045 | ↑2d | PV | +9.6% | 21.29/20.31 | +4.43% | 5% 🟥 |
| [PNBGILTS](https://in.tradingview.com/chart/?symbol=NSE:PNBGILTS)<br><sub>📶W9 · W↑13d · ↑CMF15d</sub> | ✓ SAFE | Government securities underwriting and debt market trading | ⚡ BULL_ANY_PPV | 9 | ↑59 | ↑1.027 | ↑16d | PV | +12.4% | 35.77/32.97 | +1.81% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [KOLTEPATIL](https://in.tradingview.com/chart/?symbol=NSE:KOLTEPATIL)<br><sub>📶W9 · W↑23d · ↑CMF8d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 93 | 🔄74 | ↑1.015 | ↑2d | SQ | +3.8% | 11.73/10.7 | +1.65% | 20% |
| [TSFINV](https://in.tradingview.com/chart/?symbol=NSE:TSFINV)<br><sub>📶W9 · W↑7d · ↑CMF5d</sub> | ⚠ CAUTION | NBFC lending and investment financing services | 📈 BULL_ANY_MID | 68 | ↑50 | ↑1.013 | ↑2d | SQ | +2.9% | 31.37/30.68 | +0.58% | 20% |
| [MOBIKWIK](https://in.tradingview.com/chart/?symbol=NSE:MOBIKWIK)<br><sub>📶W9 · W↑33d · ↓CMF11d</sub> | ✓ SAFE | Digital payments wallet and fintech for consumers merchants | 📈 BULL_ANY_MID | 58 | ↑68 | ↓1.006 | ↑2d | SQ | +3.1% | 18.98/17.67 | -1.23% | 20% |
| [LMW](https://in.tradingview.com/chart/?symbol=NSE:LMW)<br><sub>📶W9 · W↑7d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Textile spinning machinery and CNC machine tools manufacturer | 📈 BULL_ANY_MID | 42 | 🔄64 | ↑1.023 | ↑13d | — | +11.4% | 36.73/36.57 | +2.56% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄55 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>📶W9 · W↑13d · ★ · ↑CMF30d</sub> | ✓ SAFE | Specialty polyester films for packaging and industrial applications | 📈 BULL_ANY_MID | 8 | ↑93 | ↓1.020 | ↑12d | — | +12.6% | 48.67/47.65 | -1.57% | 20% |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA)<br><sub>📶W9 · W↑33d · ↑CMF4d</sub> | ✓ SAFE | Luxury hotel chains five-star properties Indian metros | 📈 BULL_ANY_MID | 8 | ↑94 | ↑1.030 | ↑17d | — | +18.2% | 50.88/49.47 | +1.93% | 20% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>📶W9 · 🚀SS · ↑CMF16d</sub> | ✓ SAFE | Tourism sector financing for hotels restaurants amusement parks | 📈 BULL_ANY_MID | 7 | ↑98 | ↑1.027 | ↑18d | — | +15.0% | 55.1/54.59 | +2.12% | 20% |
| [FORCEMOT](https://in.tradingview.com/chart/?symbol=NSE:FORCEMOT)<br><sub>📶W9 · W↑18d · ↑CMF16d</sub> | ✓ SAFE | Commercial vehicles and auto components, light CVs | 📈 BULL_ANY_MID | 6 | ↑66 | ↓1.039 | ↑14d | — | +19.2% | 57.53/57.38 | +0.72% | 20% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>📶W9 · W↑11d · ↑CMF13d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓60 | ↓1.007 | ↑15d | — | +7.0% | 46.27/45.57 | -0.67% | 20% |
| [CEMPRO](https://in.tradingview.com/chart/?symbol=NSE:CEMPRO)<br><sub>📶W9 · W↑13d · ★ · ↑CMF2d</sub> | ✓ SAFE | Heavy civil engineering and infrastructure construction EPC services | 📈 BULL_ANY_MID | 3 | ↑94 | ↓1.028 | ↑17d | — | +19.7% | 39.27/35.32 | +0.16% | 10% 🟩 |
| [ITCHOTELS](https://in.tradingview.com/chart/?symbol=NSE:ITCHOTELS)<br><sub>📶W9 · W↑18d · ↓CMF16d</sub> | ✓ SAFE | Hotel chain, premium and mid-market segments, Indian travelers | 📈 BULL_ANY_MID | 2 | ↑63 | ↓1.014 | ↑18d | — | +13.4% | 50.96/50.34 | -0.37% | 20% |
| [WESTLIFE](https://in.tradingview.com/chart/?symbol=NSE:WESTLIFE)<br><sub>📶W9 · W↑13d · ★ · ↑CMF0d</sub> | ✓ SAFE | McDonald's franchise operator West South India QSR | 📈 BULL_ANY_MID | 2 | ↑85 | ↓1.028 | ↑18d | — | +18.9% | 49.11/48.71 | +0.49% | 20% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>📶W9 · W↑33d · 🚀SS · ★ · ↑CMF4d</sub> | ✓ SAFE | Multiplex cinema exhibition chain, entertainment venues | 📈 BULL_ANY_MID | 0 | ↑95 | ↑1.054 | ↑32d | — | +39.2% | 68.77/67.42 | +2.21% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GREENLAM,NSE:APOLLOPIPE,NSE:INDIASHLTR,NSE:NDRAUTO,NSE:BBTC,NSE:KPIGREEN,NSE:WEL,NSE:PNBGILTS,NSE:SIGMAADV,NSE:KOLTEPATIL,NSE:TSFINV,NSE:MOBIKWIK,NSE:LMW,NSE:TATACONSUM,NSE:GRWRHITECH,NSE:THELEELA,NSE:TFCILTD,NSE:FORCEMOT,NSE:EICHERMOT,NSE:CEMPRO,NSE:ITCHOTELS,NSE:WESTLIFE,NSE:PVRINOX
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (33)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GREENLAM](https://in.tradingview.com/chart/?symbol=NSE:GREENLAM)<br><sub>📶W9 · W↑3d · RVOL68x · ↑CMF0d</sub> | ✓ SAFE | Laminate sheets and decorative veneers for furniture makers | ⚡ BULL_ANY_PPV | 89 | 🔄42 | ↑1.077 | ↑1d | SQ·PV | +10.6% | -11.46/-24.31 | +10.61% | 20% |
| [APOLLOPIPE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOPIPE)<br><sub>📶W9 · ↑CMF14d</sub> | ✓ SAFE | PVC HDPE pipes agriculture water construction infrastructure | ⚡ BULL_ANY_PPV | 89 | 🔄85 | ↑1.075 | ↑1d | SQ·PV | +10.5% | -7.61/-21.01 | +10.54% | 20% |
| [INDIASHLTR](https://in.tradingview.com/chart/?symbol=NSE:INDIASHLTR)<br><sub>📶W9 · W↑18d · RVOL12x · ↑CMF0d</sub> | ⚠ CAUTION | Housing loans for low income tier 2 3 cities | ⚡ BULL_ANY_PPV | 88 | 🔄33 | ↑1.047 | ↑2d | SQ·PV | +8.6% | -15.32/-25.97 | +5.30% | 20% |
| [NDRAUTO](https://in.tradingview.com/chart/?symbol=NSE:NDRAUTO)<br><sub>📶W9 · W↑13d · 🚀SS·60x · ↑CMF11d</sub> | ✓ SAFE | Automotive seat frames trims supplier passenger vehicles OEM | ⚡ BULL_ANY_PPV | 48 | 🔄54 | ↑1.055 | ↑2d | PV | +9.1% | 20.66/17.79 | +7.81% | 20% |
| [BBTC](https://in.tradingview.com/chart/?symbol=NSE:BBTC)<br><sub>📶W9 · W↑7d · RVOL13x · ↑CMF5d</sub> | ✓ SAFE | Teak trading, plantations, timber, diversified conglomerate, legacy Indian | ⚡ BULL_ANY_PPV | 37 | 🔄20 | ↑1.032 | ↑13d | PV | +15.1% | 17.59/16.68 | +5.04% | 20% |
| [KPIGREEN](https://in.tradingview.com/chart/?symbol=NSE:KPIGREEN)<br><sub>📶W9 · W↑7d · ↑CMF1d</sub> | ✓ SAFE | Solar wind hybrid power projects independent producer | ⚡ BULL_ANY_PPV | 18 | ↑27 | ↑1.033 | ↑2d | PV | +9.4% | 13.54/11.9 | +1.51% | 20% |
| [WEL](https://in.tradingview.com/chart/?symbol=NSE:WEL)<br><sub>📶W9 · W↑7d · ↑CMF0d</sub> | ⚠ CAUTION | Ceiling fans, exhaust fans, pedestal fans, BLDC motors | ⚡ BULL_ANY_PPV | 18 | ↑2 | ↑1.045 | ↑2d | PV | +9.6% | 21.29/20.31 | +4.43% | 5% 🟥 |
| [PNBGILTS](https://in.tradingview.com/chart/?symbol=NSE:PNBGILTS)<br><sub>📶W9 · W↑13d · ↑CMF15d</sub> | ✓ SAFE | Government securities underwriting and debt market trading | ⚡ BULL_ANY_PPV | 9 | ↑59 | ↑1.027 | ↑16d | PV | +12.4% | 35.77/32.97 | +1.81% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [KOLTEPATIL](https://in.tradingview.com/chart/?symbol=NSE:KOLTEPATIL)<br><sub>📶W9 · W↑23d · ↑CMF8d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 93 | 🔄74 | ↑1.015 | ↑2d | SQ | +3.8% | 11.73/10.7 | +1.65% | 20% |
| [TSFINV](https://in.tradingview.com/chart/?symbol=NSE:TSFINV)<br><sub>📶W9 · W↑7d · ↑CMF5d</sub> | ⚠ CAUTION | NBFC lending and investment financing services | 📈 BULL_ANY_MID | 68 | ↑50 | ↑1.013 | ↑2d | SQ | +2.9% | 31.37/30.68 | +0.58% | 20% |
| [MOBIKWIK](https://in.tradingview.com/chart/?symbol=NSE:MOBIKWIK)<br><sub>📶W9 · W↑33d · ↓CMF11d</sub> | ✓ SAFE | Digital payments wallet and fintech for consumers merchants | 📈 BULL_ANY_MID | 58 | ↑68 | ↓1.006 | ↑2d | SQ | +3.1% | 18.98/17.67 | -1.23% | 20% |
| [LMW](https://in.tradingview.com/chart/?symbol=NSE:LMW)<br><sub>📶W9 · W↑7d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Textile spinning machinery and CNC machine tools manufacturer | 📈 BULL_ANY_MID | 42 | 🔄64 | ↑1.023 | ↑13d | — | +11.4% | 36.73/36.57 | +2.56% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄55 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>📶W9 · W↑13d · ★ · ↑CMF30d</sub> | ✓ SAFE | Specialty polyester films for packaging and industrial applications | 📈 BULL_ANY_MID | 8 | ↑93 | ↓1.020 | ↑12d | — | +12.6% | 48.67/47.65 | -1.57% | 20% |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA)<br><sub>📶W9 · W↑33d · ↑CMF4d</sub> | ✓ SAFE | Luxury hotel chains five-star properties Indian metros | 📈 BULL_ANY_MID | 8 | ↑94 | ↑1.030 | ↑17d | — | +18.2% | 50.88/49.47 | +1.93% | 20% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>📶W9 · 🚀SS · ↑CMF16d</sub> | ✓ SAFE | Tourism sector financing for hotels restaurants amusement parks | 📈 BULL_ANY_MID | 7 | ↑98 | ↑1.027 | ↑18d | — | +15.0% | 55.1/54.59 | +2.12% | 20% |
| [FORCEMOT](https://in.tradingview.com/chart/?symbol=NSE:FORCEMOT)<br><sub>📶W9 · W↑18d · ↑CMF16d</sub> | ✓ SAFE | Commercial vehicles and auto components, light CVs | 📈 BULL_ANY_MID | 6 | ↑66 | ↓1.039 | ↑14d | — | +19.2% | 57.53/57.38 | +0.72% | 20% |
| [CEMPRO](https://in.tradingview.com/chart/?symbol=NSE:CEMPRO)<br><sub>📶W9 · W↑13d · ★ · ↑CMF2d</sub> | ✓ SAFE | Heavy civil engineering and infrastructure construction EPC services | 📈 BULL_ANY_MID | 3 | ↑94 | ↓1.028 | ↑17d | — | +19.7% | 39.27/35.32 | +0.16% | 10% 🟩 |
| [ITCHOTELS](https://in.tradingview.com/chart/?symbol=NSE:ITCHOTELS)<br><sub>📶W9 · W↑18d · ↓CMF16d</sub> | ✓ SAFE | Hotel chain, premium and mid-market segments, Indian travelers | 📈 BULL_ANY_MID | 2 | ↑63 | ↓1.014 | ↑18d | — | +13.4% | 50.96/50.34 | -0.37% | 20% |
| [WESTLIFE](https://in.tradingview.com/chart/?symbol=NSE:WESTLIFE)<br><sub>📶W9 · W↑13d · ★ · ↑CMF0d</sub> | ✓ SAFE | McDonald's franchise operator West South India QSR | 📈 BULL_ANY_MID | 2 | ↑85 | ↓1.028 | ↑18d | — | +18.9% | 49.11/48.71 | +0.49% | 20% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>📶W9 · W↑33d · 🚀SS · ★ · ↑CMF4d</sub> | ✓ SAFE | Multiplex cinema exhibition chain, entertainment venues | 📈 BULL_ANY_MID | 0 | ↑95 | ↑1.054 | ↑32d | — | +39.2% | 68.77/67.42 | +2.21% | 20% |
| [VESUVIUS](https://in.tradingview.com/chart/?symbol=NSE:VESUVIUS)<br><sub>RVOL286x · ↑CMF0d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Ceramic refractories for steel and foundry molten metal handling | ⚡ BULL_ANY_PPV | 49 | 🔄16 | ↑1.032 | ↑1d | PV | +10.8% | -54.26/-54.71 | +10.81% | 20% |
| [ADVAIT](https://in.tradingview.com/chart/?symbol=NSE:ADVAIT)<br><sub>W↑7d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Power transmission infrastructure and renewable energy solutions | ⚡ BULL_ANY_PPV | 48 | 🔄50 | ↑1.009 | ↑12d | PV | +9.4% | 16.28/13.01 | +1.42% | 20% |
| [ARVINDFASN](https://in.tradingview.com/chart/?symbol=NSE:ARVINDFASN)<br><sub>↓CMF13d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Casual wear denim apparel retailer multiple brands | 🟡 BULL_OS_L2 | 75 | 🔄8 | ↑0.998 | ↓26d | SQ | -13.0% | -55.2/-57.74 | +1.27% | 20% |
| [ASHIANA](https://in.tradingview.com/chart/?symbol=NSE:ASHIANA)<br><sub>↓CMF22d</sub> | ⚠ CAUTION | Senior living housing developer for Indian retirees | 📈 BULL_ANY_MID | 98 | 🔄63 | ↑1.010 | ↑2d | SQ | +1.8% | -8.02/-9.29 | +1.11% | 20% |
| [RSL](https://in.tradingview.com/chart/?symbol=NSE:RSL)<br><sub>↓CMF30d</sub> | ✓ SAFE | Stainless steel bars billets rods domestic international markets | 📈 BULL_ANY_MID | 91 | 🔄50 | ↑1.003 | ↓9d | SQ | -0.7% | -27.06/-30.18 | +0.60% | 20% |
| [INSECTICID](https://in.tradingview.com/chart/?symbol=NSE:INSECTICID)<br><sub>W↑3d · ↑CMF1d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 88 | 🔄24 | ↓1.002 | ↑2d | SQ | +0.8% | -15.39/-17.68 | -0.07% | 20% |
| [PILANIINVS](https://in.tradingview.com/chart/?symbol=NSE:PILANIINVS)<br><sub>W↑12d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 80 | 🔄31 | ↓1.002 | ↑10d | SQ | +3.8% | 14.9/13.77 | -0.00% | 5% |
| [BLSE](https://in.tradingview.com/chart/?symbol=NSE:BLSE)<br><sub>↑CMF2d</sub> | ✓ SAFE | Digital governance and banking services rural India | 📈 BULL_ANY_MID | 68 | ↑2 | ↑1.009 | ↑2d | SQ | +3.1% | -23.92/-28.56 | +0.20% | 20% |
| [GARUDA](https://in.tradingview.com/chart/?symbol=NSE:GARUDA)<br><sub>W↑3d · ↓CMF30d</sub> | ✓ SAFE | EPC contractor for residential commercial infrastructure projects | 📈 BULL_ANY_MID | 59 | 🔄16 | ↑1.007 | ↑1d | — | +1.6% | -6.77/-8.66 | +1.61% | 20% |
| [HCG](https://in.tradingview.com/chart/?symbol=NSE:HCG)<br><sub>↑CMF2d</sub> | ⚠ CAUTION | Oncology hospital network, fertility services, India | 📈 BULL_ANY_MID | 54 | 🔄31 | ↑1.026 | ↑1d | — | +4.1% | -22.15/-25.53 | +4.13% | 20% |
| [DHANUKA](https://in.tradingview.com/chart/?symbol=NSE:DHANUKA)<br><sub>W↑18d · ↑CMF13d</sub> | ✓ SAFE | Herbicides insecticides fungicides manufacturing for Indian farmers | 📈 BULL_ANY_MID | 23 | ↑26 | ↑1.019 | ↑2d | — | +4.6% | 4.88/-0.64 | +0.49% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GREENLAM,NSE:APOLLOPIPE,NSE:INDIASHLTR,NSE:NDRAUTO,NSE:BBTC,NSE:KPIGREEN,NSE:WEL,NSE:PNBGILTS,NSE:SIGMAADV,NSE:KOLTEPATIL,NSE:TSFINV,NSE:MOBIKWIK,NSE:LMW,NSE:TATACONSUM,NSE:GRWRHITECH,NSE:THELEELA,NSE:TFCILTD,NSE:FORCEMOT,NSE:CEMPRO,NSE:ITCHOTELS,NSE:WESTLIFE,NSE:PVRINOX,NSE:VESUVIUS,NSE:ADVAIT,NSE:ARVINDFASN,NSE:ASHIANA,NSE:RSL,NSE:INSECTICID,NSE:PILANIINVS,NSE:BLSE,NSE:GARUDA,NSE:HCG,NSE:DHANUKA
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (13)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GREENLAM](https://in.tradingview.com/chart/?symbol=NSE:GREENLAM)<br><sub>📶W9 · W↑3d · RVOL68x · ↑CMF0d</sub> | ✓ SAFE | Laminate sheets and decorative veneers for furniture makers | ⚡ BULL_ANY_PPV | 89 | 🔄42 | ↑1.077 | ↑1d | SQ·PV | +10.6% | -11.46/-24.31 | +10.61% | 20% |
| [APOLLOPIPE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOPIPE)<br><sub>📶W9 · ↑CMF14d</sub> | ✓ SAFE | PVC HDPE pipes agriculture water construction infrastructure | ⚡ BULL_ANY_PPV | 89 | 🔄85 | ↑1.075 | ↑1d | SQ·PV | +10.5% | -7.61/-21.01 | +10.54% | 20% |
| [INDIASHLTR](https://in.tradingview.com/chart/?symbol=NSE:INDIASHLTR)<br><sub>📶W9 · W↑18d · RVOL12x · ↑CMF0d</sub> | ⚠ CAUTION | Housing loans for low income tier 2 3 cities | ⚡ BULL_ANY_PPV | 88 | 🔄33 | ↑1.047 | ↑2d | SQ·PV | +8.6% | -15.32/-25.97 | +5.30% | 20% |
| [KOLTEPATIL](https://in.tradingview.com/chart/?symbol=NSE:KOLTEPATIL)<br><sub>📶W9 · W↑23d · ↑CMF8d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 93 | 🔄74 | ↑1.015 | ↑2d | SQ | +3.8% | 11.73/10.7 | +1.65% | 20% |
| [TSFINV](https://in.tradingview.com/chart/?symbol=NSE:TSFINV)<br><sub>📶W9 · W↑7d · ↑CMF5d</sub> | ⚠ CAUTION | NBFC lending and investment financing services | 📈 BULL_ANY_MID | 68 | ↑50 | ↑1.013 | ↑2d | SQ | +2.9% | 31.37/30.68 | +0.58% | 20% |
| [MOBIKWIK](https://in.tradingview.com/chart/?symbol=NSE:MOBIKWIK)<br><sub>📶W9 · W↑33d · ↓CMF11d</sub> | ✓ SAFE | Digital payments wallet and fintech for consumers merchants | 📈 BULL_ANY_MID | 58 | ↑68 | ↓1.006 | ↑2d | SQ | +3.1% | 18.98/17.67 | -1.23% | 20% |
| [ARVINDFASN](https://in.tradingview.com/chart/?symbol=NSE:ARVINDFASN)<br><sub>↓CMF13d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Casual wear denim apparel retailer multiple brands | 🟡 BULL_OS_L2 | 75 | 🔄8 | ↑0.998 | ↓26d | SQ | -13.0% | -55.2/-57.74 | +1.27% | 20% |
| [ASHIANA](https://in.tradingview.com/chart/?symbol=NSE:ASHIANA)<br><sub>↓CMF22d</sub> | ⚠ CAUTION | Senior living housing developer for Indian retirees | 📈 BULL_ANY_MID | 98 | 🔄63 | ↑1.010 | ↑2d | SQ | +1.8% | -8.02/-9.29 | +1.11% | 20% |
| [RSL](https://in.tradingview.com/chart/?symbol=NSE:RSL)<br><sub>↓CMF30d</sub> | ✓ SAFE | Stainless steel bars billets rods domestic international markets | 📈 BULL_ANY_MID | 91 | 🔄50 | ↑1.003 | ↓9d | SQ | -0.7% | -27.06/-30.18 | +0.60% | 20% |
| [INSECTICID](https://in.tradingview.com/chart/?symbol=NSE:INSECTICID)<br><sub>W↑3d · ↑CMF1d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 88 | 🔄24 | ↓1.002 | ↑2d | SQ | +0.8% | -15.39/-17.68 | -0.07% | 20% |
| [PILANIINVS](https://in.tradingview.com/chart/?symbol=NSE:PILANIINVS)<br><sub>W↑12d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 80 | 🔄31 | ↓1.002 | ↑10d | SQ | +3.8% | 14.9/13.77 | -0.00% | 5% |
| [BLSE](https://in.tradingview.com/chart/?symbol=NSE:BLSE)<br><sub>↑CMF2d</sub> | ✓ SAFE | Digital governance and banking services rural India | 📈 BULL_ANY_MID | 68 | ↑2 | ↑1.009 | ↑2d | SQ | +3.1% | -23.92/-28.56 | +0.20% | 20% |
| [PFOCUS](https://in.tradingview.com/chart/?symbol=NSE:PFOCUS)<br><sub>↓CMF6d · ⚠️TRAP</sub> | ✓ SAFE | VFX animation post-production services for film television | 📈 BULL_ANY_MID | 48 | ↓71 | ↓0.995 | ↓12d | SQ | -2.0% | -30.4/-30.49 | -1.16% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GREENLAM,NSE:APOLLOPIPE,NSE:INDIASHLTR,NSE:KOLTEPATIL,NSE:TSFINV,NSE:MOBIKWIK,NSE:ARVINDFASN,NSE:ASHIANA,NSE:RSL,NSE:INSECTICID,NSE:PILANIINVS,NSE:BLSE,NSE:PFOCUS
```

---

### 🔥 MAJOR — PPV confirmed (8)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [NDRAUTO](https://in.tradingview.com/chart/?symbol=NSE:NDRAUTO)<br><sub>📶W9 · W↑13d · 🚀SS·60x · ↑CMF11d</sub> | ✓ SAFE | Automotive seat frames trims supplier passenger vehicles OEM | ⚡ BULL_ANY_PPV | 48 | 🔄54 | ↑1.055 | ↑2d | PV | +9.1% | 20.66/17.79 | +7.81% | 20% |
| [BBTC](https://in.tradingview.com/chart/?symbol=NSE:BBTC)<br><sub>📶W9 · W↑7d · RVOL13x · ↑CMF5d</sub> | ✓ SAFE | Teak trading, plantations, timber, diversified conglomerate, legacy Indian | ⚡ BULL_ANY_PPV | 37 | 🔄20 | ↑1.032 | ↑13d | PV | +15.1% | 17.59/16.68 | +5.04% | 20% |
| [KPIGREEN](https://in.tradingview.com/chart/?symbol=NSE:KPIGREEN)<br><sub>📶W9 · W↑7d · ↑CMF1d</sub> | ✓ SAFE | Solar wind hybrid power projects independent producer | ⚡ BULL_ANY_PPV | 18 | ↑27 | ↑1.033 | ↑2d | PV | +9.4% | 13.54/11.9 | +1.51% | 20% |
| [WEL](https://in.tradingview.com/chart/?symbol=NSE:WEL)<br><sub>📶W9 · W↑7d · ↑CMF0d</sub> | ⚠ CAUTION | Ceiling fans, exhaust fans, pedestal fans, BLDC motors | ⚡ BULL_ANY_PPV | 18 | ↑2 | ↑1.045 | ↑2d | PV | +9.6% | 21.29/20.31 | +4.43% | 5% 🟥 |
| [PNBGILTS](https://in.tradingview.com/chart/?symbol=NSE:PNBGILTS)<br><sub>📶W9 · W↑13d · ↑CMF15d</sub> | ✓ SAFE | Government securities underwriting and debt market trading | ⚡ BULL_ANY_PPV | 9 | ↑59 | ↑1.027 | ↑16d | PV | +12.4% | 35.77/32.97 | +1.81% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [VESUVIUS](https://in.tradingview.com/chart/?symbol=NSE:VESUVIUS)<br><sub>RVOL286x · ↑CMF0d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Ceramic refractories for steel and foundry molten metal handling | ⚡ BULL_ANY_PPV | 49 | 🔄16 | ↑1.032 | ↑1d | PV | +10.8% | -54.26/-54.71 | +10.81% | 20% |
| [ADVAIT](https://in.tradingview.com/chart/?symbol=NSE:ADVAIT)<br><sub>W↑7d · 🚀SS · ↓CMF30d</sub> | ✓ SAFE | Power transmission infrastructure and renewable energy solutions | ⚡ BULL_ANY_PPV | 48 | 🔄50 | ↑1.009 | ↑12d | PV | +9.4% | 16.28/13.01 | +1.42% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:NDRAUTO,NSE:BBTC,NSE:KPIGREEN,NSE:WEL,NSE:PNBGILTS,NSE:SIGMAADV,NSE:VESUVIUS,NSE:ADVAIT
```

### 🟢 OVERSOLD — reversal from −53/−60 (1)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [RATEGAIN](https://in.tradingview.com/chart/?symbol=NSE:RATEGAIN)<br><sub>↓CMF25d · ⚠️TRAP</sub> | ✓ SAFE | Hotel distribution and revenue management software for hospitality | 🟡 BULL_OS_L2 | 10 | ↓34 | ↓0.959 | ↓10d | — | -15.1% | -59.23/-59.94 | -1.11% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:RATEGAIN
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (17)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [LMW](https://in.tradingview.com/chart/?symbol=NSE:LMW)<br><sub>📶W9 · W↑7d · 🚀SS · ↑CMF0d</sub> | ⚠ CAUTION | Textile spinning machinery and CNC machine tools manufacturer | 📈 BULL_ANY_MID | 42 | 🔄64 | ↑1.023 | ↑13d | — | +11.4% | 36.73/36.57 | +2.56% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>📶W9 · W↑21d · 🚀SS · ↑CMF17d</sub> | ⚠ CAUTION | Tea, coffee, salt brands for Indian households and global markets | 📈 BULL_ANY_MID | 35 | 🔄55 | ↑1.037 | ↑15d | — | +19.3% | 47.97/47.29 | +3.57% | 20% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>📶W9 · W↑13d · ★ · ↑CMF30d</sub> | ✓ SAFE | Specialty polyester films for packaging and industrial applications | 📈 BULL_ANY_MID | 8 | ↑93 | ↓1.020 | ↑12d | — | +12.6% | 48.67/47.65 | -1.57% | 20% |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA)<br><sub>📶W9 · W↑33d · ↑CMF4d</sub> | ✓ SAFE | Luxury hotel chains five-star properties Indian metros | 📈 BULL_ANY_MID | 8 | ↑94 | ↑1.030 | ↑17d | — | +18.2% | 50.88/49.47 | +1.93% | 20% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>📶W9 · 🚀SS · ↑CMF16d</sub> | ✓ SAFE | Tourism sector financing for hotels restaurants amusement parks | 📈 BULL_ANY_MID | 7 | ↑98 | ↑1.027 | ↑18d | — | +15.0% | 55.1/54.59 | +2.12% | 20% |
| [FORCEMOT](https://in.tradingview.com/chart/?symbol=NSE:FORCEMOT)<br><sub>📶W9 · W↑18d · ↑CMF16d</sub> | ✓ SAFE | Commercial vehicles and auto components, light CVs | 📈 BULL_ANY_MID | 6 | ↑66 | ↓1.039 | ↑14d | — | +19.2% | 57.53/57.38 | +0.72% | 20% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>📶W9 · W↑11d · ↑CMF13d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓60 | ↓1.007 | ↑15d | — | +7.0% | 46.27/45.57 | -0.67% | 20% |
| [CEMPRO](https://in.tradingview.com/chart/?symbol=NSE:CEMPRO)<br><sub>📶W9 · W↑13d · ★ · ↑CMF2d</sub> | ✓ SAFE | Heavy civil engineering and infrastructure construction EPC services | 📈 BULL_ANY_MID | 3 | ↑94 | ↓1.028 | ↑17d | — | +19.7% | 39.27/35.32 | +0.16% | 10% 🟩 |
| [ITCHOTELS](https://in.tradingview.com/chart/?symbol=NSE:ITCHOTELS)<br><sub>📶W9 · W↑18d · ↓CMF16d</sub> | ✓ SAFE | Hotel chain, premium and mid-market segments, Indian travelers | 📈 BULL_ANY_MID | 2 | ↑63 | ↓1.014 | ↑18d | — | +13.4% | 50.96/50.34 | -0.37% | 20% |
| [WESTLIFE](https://in.tradingview.com/chart/?symbol=NSE:WESTLIFE)<br><sub>📶W9 · W↑13d · ★ · ↑CMF0d</sub> | ✓ SAFE | McDonald's franchise operator West South India QSR | 📈 BULL_ANY_MID | 2 | ↑85 | ↓1.028 | ↑18d | — | +18.9% | 49.11/48.71 | +0.49% | 20% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>📶W9 · W↑33d · 🚀SS · ★ · ↑CMF4d</sub> | ✓ SAFE | Multiplex cinema exhibition chain, entertainment venues | 📈 BULL_ANY_MID | 0 | ↑95 | ↑1.054 | ↑32d | — | +39.2% | 68.77/67.42 | +2.21% | 20% |
| [GARUDA](https://in.tradingview.com/chart/?symbol=NSE:GARUDA)<br><sub>W↑3d · ↓CMF30d</sub> | ✓ SAFE | EPC contractor for residential commercial infrastructure projects | 📈 BULL_ANY_MID | 59 | 🔄16 | ↑1.007 | ↑1d | — | +1.6% | -6.77/-8.66 | +1.61% | 20% |
| [HCG](https://in.tradingview.com/chart/?symbol=NSE:HCG)<br><sub>↑CMF2d</sub> | ⚠ CAUTION | Oncology hospital network, fertility services, India | 📈 BULL_ANY_MID | 54 | 🔄31 | ↑1.026 | ↑1d | — | +4.1% | -22.15/-25.53 | +4.13% | 20% |
| [DHANUKA](https://in.tradingview.com/chart/?symbol=NSE:DHANUKA)<br><sub>W↑18d · ↑CMF13d</sub> | ✓ SAFE | Herbicides insecticides fungicides manufacturing for Indian farmers | 📈 BULL_ANY_MID | 23 | ↑26 | ↑1.019 | ↑2d | — | +4.6% | 4.88/-0.64 | +0.49% | 20% |
| [STOVEKRAFT](https://in.tradingview.com/chart/?symbol=NSE:STOVEKRAFT)<br><sub>↓CMF30d</sub> | ✓ SAFE | Kitchen appliances and cookware manufacturing, retail, brands | 📈 BULL_ANY_MID | 14 | ↓78 | ↑0.994 | ↓11d | — | -3.6% | -45.34/-45.43 | +0.77% | 20% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>↑CMF8d</sub> | n/a | Dredging, marine craft repair, maritime infrastructure engineering | 📈 BULL_ANY_MID | 12 | ↓0 | ↑0.655 | ↓13d | — | -76.3% | -44.59/-45.14 | -0.73% | 20% |
| [GANECOS](https://in.tradingview.com/chart/?symbol=NSE:GANECOS)<br><sub>↓CMF24d</sub> | ✓ SAFE | PET waste recycling, polyester fiber manufacturing, textile supply | 📈 BULL_ANY_MID | 7 | ↓43 | ↑0.983 | ↓18d | — | -10.6% | -49.35/-50.5 | +0.48% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LMW,NSE:TATACONSUM,NSE:GRWRHITECH,NSE:THELEELA,NSE:TFCILTD,NSE:FORCEMOT,NSE:EICHERMOT,NSE:CEMPRO,NSE:ITCHOTELS,NSE:WESTLIFE,NSE:PVRINOX,NSE:GARUDA,NSE:HCG,NSE:DHANUKA,NSE:STOVEKRAFT,NSE:KMEW,NSE:GANECOS
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
