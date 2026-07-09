> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-07-09
*Generated 2026-07-09 20:25 IST*

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

**Total bull crosses today: 68** · 26 inside active squeeze

```
NSE:GIPCL,NSE:JAYKAY,NSE:ARE&M,NSE:ASTERDM,NSE:INNOVACAP,NSE:PREMIERENE,NSE:PGHL,NSE:TVSSCS,NSE:MARKSANS,NSE:ORCHPHARMA,NSE:RAINBOW,NSE:UDS,NSE:TCIEXP,NSE:JINDALSAW,NSE:KALYANKJIL,NSE:GRPLTD,NSE:AGARWALEYE,NSE:GOODLUCK,NSE:STARHEALTH,NSE:CHOICEIN,NSE:AETHER,NSE:EPACKPEB,NSE:NEOGEN,NSE:SIS,NSE:INOXINDIA,NSE:RUBICON,NSE:ZYDUSLIFE,NSE:HAPPYFORGE,NSE:NOVARTIND,NSE:ENTERO,NSE:CCL,NSE:GLAXO,NSE:RELIGARE,NSE:NEULANDLAB,NSE:SPAL,NSE:UJJIVANSFB,NSE:SHILPAMED,NSE:AMAGI,NSE:TATAINVEST,NSE:JKIL,NSE:CARRARO,NSE:HCLTECH,NSE:JYOTHYLAB,NSE:LTM,NSE:TATASTEEL,NSE:JINDALSTEL,NSE:INFY,NSE:SUPREMEIND,NSE:WAAREEENER,NSE:AWFIS,NSE:DIVISLAB,NSE:JSLL,NSE:APOLLOPIPE,NSE:TATACONSUM,NSE:GKSL,NSE:AMBER,NSE:POWERGRID,NSE:MUTHOOTFIN,NSE:VIKRAMSOLR,NSE:BEL,NSE:ITC,NSE:TECHM,NSE:BPCL,NSE:VBL,NSE:WIPRO,NSE:DEEPINDS,NSE:HINDALCO,NSE:COALINDIA
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (38)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GIPCL](https://in.tradingview.com/chart/?symbol=NSE:GIPCL)<br><sub>📶W9 · W↑67d · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | Power generation thermal plants Gujarat state utilities | ⚡ BULL_ANY_PPV | 94 | 🔄44 | ↑1.017 | ↑1d | SQ·PV | +3.6% | -19.33/-21.29 | +3.58% | 20% |
| [JAYKAY](https://in.tradingview.com/chart/?symbol=NSE:JAYKAY)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Additive manufacturing and 3D printing technology services | ⚡ BULL_ANY_PPV | 89 | 🔄50 | ↑1.030 | ↑1d | SQ·PV | +6.2% | -13.44/-13.57 | +6.22% | 20% |
| [ARE&M](https://in.tradingview.com/chart/?symbol=NSE:ARE&M)<br><sub>📶W9 · W↑62d · 🚀SS · ↓CMF13d</sub> | ✓ SAFE | Lead-acid batteries automotive industrial energy storage | ⚡ BULL_ANY_PPV | 64 | ↑45 | ↑1.025 | ↑1d | SQ·PV | +4.1% | 15.06/10.24 | +4.12% | 20% |
| [ASTERDM](https://in.tradingview.com/chart/?symbol=NSE:ASTERDM)<br><sub>📶W9 · 🚀SS · ↓CMF19d</sub> | ⚠ CAUTION | Private multi-specialty hospital chains India GCC markets | ⚡ BULL_ANY_PPV | 64 | ↑76 | ↑1.025 | ↑1d | SQ·PV | +3.5% | 28.66/24.47 | +3.53% | 20% |
| [INNOVACAP](https://in.tradingview.com/chart/?symbol=NSE:INNOVACAP)<br><sub>📶W9 · W↑84d · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | Tablet manufacturing pharmaceuticals India generic drugs | ⚡ BULL_ANY_PPV | 62 | ↑83 | ↑1.022 | ↑3d | SQ·PV | +3.9% | 57.49/51.69 | +0.81% | 20% |
| [PREMIERENE](https://in.tradingview.com/chart/?symbol=NSE:PREMIERENE)<br><sub>📶W9 · W↑108d · 🚀SS · ↓CMF10d</sub> | ✓ SAFE | Solar cells modules manufacturing for rooftop commercial industrial | ⚡ BULL_ANY_PPV | 59 | ↑69 | ↑1.037 | ↑1d | SQ·PV | +4.3% | -13.6/-26.35 | +4.34% | 20% |
| [PGHL](https://in.tradingview.com/chart/?symbol=NSE:PGHL)<br><sub>📶W9 · W↑74d · ↓CMF6d</sub> | ⚠ CAUTION | Vitamins, minerals, supplements, and OTC pharmaceuticals manufacturer | ⚡ BULL_ANY_PPV | 59 | ↑76 | ↑1.041 | ↑1d | SQ·PV | +5.6% | 50.02/46.09 | +5.58% | 20% |
| [TVSSCS](https://in.tradingview.com/chart/?symbol=NSE:TVSSCS)<br><sub>📶W9 · W↑67d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Third-party logistics provider for automotive manufacturers | ⚡ BULL_ANY_PPV | 59 | ↑74 | ↑1.033 | ↑1d | SQ·PV | +4.8% | 43.59/42.62 | +4.82% | 10% 🟩 |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS)<br><sub>📶W9 · W↑67d · 🚀SS · ↓CMF12d</sub> | ✓ SAFE | Generic pharmaceutical formulations for regulated global markets | ⚡ BULL_ANY_PPV | 58 | ↑91 | ↑1.047 | ↑2d | SQ·PV | +6.2% | 51.91/47.69 | +5.26% | 20% |
| [ORCHPHARMA](https://in.tradingview.com/chart/?symbol=NSE:ORCHPHARMA)<br><sub>📶W9 · W↑67d · ↑CMF30d</sub> | ✓ SAFE | Injectables manufacturer serving hospitals and critical care markets | ⚡ BULL_ANY_PPV | 58 | ↑94 | ↑1.074 | ↑2d | SQ·PV | +13.7% | 35.69/27.67 | +4.86% | 20% |
| [RAINBOW](https://in.tradingview.com/chart/?symbol=NSE:RAINBOW)<br><sub>📶W9 · W↑70d · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION | Pediatric obstetrics gynecology hospital chain India | ⚡ BULL_ANY_PPV | 58 | ↑63 | ↑1.030 | ↑2d | SQ·PV | +4.2% | 37.85/31.78 | +3.52% | 20% |
| [UDS](https://in.tradingview.com/chart/?symbol=NSE:UDS)<br><sub>📶W9 · W↑67d · ↓CMF4d</sub> | ✓ SAFE | Facilities management and business support services provider | ⚡ BULL_ANY_PPV | 54 | ↑47 | ↑1.044 | ↑6d | SQ·PV | +8.1% | 55.99/54.86 | +5.49% | 20% |
| [TCIEXP](https://in.tradingview.com/chart/?symbol=NSE:TCIEXP)<br><sub>📶W9 · W↑24d · 🚀SS·11x · ↑CMF11d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 49 | 🔄21 | ↑1.063 | ↑1d | PV | +10.9% | -6.34/-10.4 | +10.93% | 20% |
| [JINDALSAW](https://in.tradingview.com/chart/?symbol=NSE:JINDALSAW)<br><sub>📶W9 · W↑34d · ↑CMF5d</sub> | ✓ SAFE | Submerged arc welded pipes manufacturer for infrastructure | ⚡ BULL_ANY_PPV | 40 | ↑86 | ↑1.039 | ↑20d | SQ·PV | +21.8% | 37.95/34.22 | +4.87% | 20% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>📶W9 · W↑19d · 🚀SS·12x · ↑CMF18d</sub> | ✓ SAFE | Gold jewellery retail across India and Middle East markets | ⚡ BULL_ANY_PPV | 19 | ↑22 | ↑1.142 | ↑1d | PV | +18.4% | 26.29/19.73 | +18.40% | 20% |
| [GRPLTD](https://in.tradingview.com/chart/?symbol=NSE:GRPLTD)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF18d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 18 | ↑31 | ↑1.034 | ↑2d | PV | +6.2% | 20.61/13.61 | +2.30% | 20% |
| [AGARWALEYE](https://in.tradingview.com/chart/?symbol=NSE:AGARWALEYE)<br><sub>📶W9 · W↑14d · ↑CMF0d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 10 | ↑56 | ↑1.018 | ↑15d | PV | +9.2% | 26.87/24.24 | +1.62% | 20% |
| [GOODLUCK](https://in.tradingview.com/chart/?symbol=NSE:GOODLUCK)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | Steel pipes, forgings, tubes for automotive, industrial | ⚡ BULL_ANY_PPV | 3 | ↑86 | ↑1.049 | ↑17d | PV | +18.0% | 49.57/48.41 | +6.62% | 20% |
| [STARHEALTH](https://in.tradingview.com/chart/?symbol=NSE:STARHEALTH)<br><sub>📶W9 · W↑70d · ↑CMF15d</sub> | ✓ SAFE | Health insurance policies, retail individuals, hospitals network | ⚡ BULL_ANY_PPV | 3 | ↑85 | ↑1.031 | ↑17d | PV | +15.6% | 54.31/52.82 | +3.26% | 20% |
| [CHOICEIN](https://in.tradingview.com/chart/?symbol=NSE:CHOICEIN)<br><sub>📶W9 · W↑19d · 🚀SS·9x · ↑CMF7d</sub> | ✓ SAFE | Stockbroking wealth management MSME lending insurance distribution financial services | ⚡ BULL_ANY_PPV | 0 | ↑62 | ↑1.071 | ↑20d | PV | +26.6% | 59.2/57.93 | +7.98% | 20% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF14d</sub> | ✓ SAFE | Specialty chemicals for pharma agrochemical material science | ⚡ BULL_ANY_PPV | 0 | ↑94 | ↑1.087 | ↑27d | PV | +35.2% | 69.16/65.98 | +5.12% | 20% |
| [EPACKPEB](https://in.tradingview.com/chart/?symbol=NSE:EPACKPEB)<br><sub>📶W9 · W↑72d · 🚀SS · ↑CMF19d</sub> | ✓ SAFE | Steel prefab buildings manufacturing construction services India | 📈 BULL_ANY_MID | 89 | 🔄50 | ↑1.049 | ↑1d | SQ | +7.5% | 28.31/27.93 | +7.55% | 20% |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>📶W9 · W↑4d · ↑CMF24d</sub> | ✓ SAFE | Bromine and lithium specialty chemicals for pharma agriculture | 📈 BULL_ANY_MID | 64 | ↑91 | ↑1.027 | ↑1d | SQ | +3.9% | 27.24/25.07 | +3.89% | 20% |
| [SIS](https://in.tradingview.com/chart/?symbol=NSE:SIS)<br><sub>📶W9 · W↑67d · 🚀SS · ↓CMF18d</sub> | ✓ SAFE | Security guarding, facility management, cash logistics operations | 📈 BULL_ANY_MID | 63 | ↑86 | ↑1.019 | ↑2d | SQ | +2.3% | 24.32/19.56 | +1.80% | 20% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF24d</sub> | ✓ SAFE | Cryogenic equipment manufacturer for LNG and industrial gas sectors | 📈 BULL_ANY_MID | 59 | ↑95 | ↑1.057 | ↑1d | SQ | +7.0% | 23.24/20.59 | +6.95% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · ↑CMF5d</sub> | ✓ SAFE | Complex generics and specialty formulations manufacturing pharma | 📈 BULL_ANY_MID | 56 | ↑50 | ↓1.020 | ↑4d | SQ | +7.1% | 38.64/36.15 | -0.49% | 20% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>📶W9 · W↑56d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | Pharmaceuticals: generics, branded drugs, consumer wellness products | 📈 BULL_ANY_MID | 49 | 🔄73 | ↑1.031 | ↑1d | — | +3.9% | 44.71/41.57 | +3.92% | 20% |
| [HAPPYFORGE](https://in.tradingview.com/chart/?symbol=NSE:HAPPYFORGE)<br><sub>📶W9 · W↑14d · ↑CMF13d</sub> | ✓ SAFE | Heavy forged components supplier automotive industrial OEMs | 📈 BULL_ANY_MID | 23 | ↑88 | ↑1.028 | ↑2d | — | +4.6% | 33.06/30.32 | +2.85% | 20% |
| [NOVARTIND](https://in.tradingview.com/chart/?symbol=NSE:NOVARTIND)<br><sub>📶W9 · W↑57d · 🚀SS · ↓CMF10d</sub> | ⚠ CAUTION | Pharmaceutical distribution and wholesale medicines trading India | 📈 BULL_ANY_MID | 15 | ↑50 | ↑1.011 | ↑15d | — | +8.1% | 36.99/36.46 | +0.96% | 20% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>📶W9 · W↑4d · ↑CMF0d</sub> | ⚠ CAUTION | Pharmaceutical surgical products distributor hospitals clinics retail | 📈 BULL_ANY_MID | 13 | ↑50 | ↑1.023 | ↑12d | — | +11.8% | 22.56/22.0 | +3.75% | 20% |
| [CCL](https://in.tradingview.com/chart/?symbol=NSE:CCL)<br><sub>📶W9 · W↑19d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | Instant coffee manufacturing and export global markets | 📈 BULL_ANY_MID | 9 | ↑80 | ↑1.022 | ↑16d | — | +8.5% | 51.92/50.45 | +2.37% | 20% |
| [GLAXO](https://in.tradingview.com/chart/?symbol=NSE:GLAXO)<br><sub>📶W9 · W↑14d · ↑CMF14d</sub> | ✓ SAFE | Pharmaceuticals manufacturing vaccines respiratory gastrointestinal antibiotics India | 📈 BULL_ANY_MID | 7 | ↑27 | ↑1.018 | ↑18d | — | +15.0% | 34.71/32.79 | +1.23% | 20% |
| [RELIGARE](https://in.tradingview.com/chart/?symbol=NSE:RELIGARE)<br><sub>📶W9 · W↑70d · ↑CMF12d</sub> | ✓ SAFE | Financial services: insurance, broking, SME lending | 📈 BULL_ANY_MID | 5 | ↑68 | ↑1.018 | ↑21d | — | +19.0% | 45.27/43.68 | +2.03% | 20% |
| [NEULANDLAB](https://in.tradingview.com/chart/?symbol=NSE:NEULANDLAB)<br><sub>📶W9 · W↑67d · 🚀SS · ★ · ↓CMF2d</sub> | ✓ SAFE | Pharma APIs CDMO services domestic international markets | 📈 BULL_ANY_MID | 4 | ↑87 | ↑1.042 | ↑16d | — | +14.8% | 70.8/70.33 | +3.46% | 20% |
| [SPAL](https://in.tradingview.com/chart/?symbol=NSE:SPAL)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Knitted infant children's apparel manufacturer exporter textile | 📈 BULL_ANY_MID | 1 | ↑94 | ↑1.056 | ↑19d | — | +48.1% | 63.52/63.02 | +1.52% | 20% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Microfinance bank serving unbanked low-income borrowers | 📈 BULL_ANY_MID | 0 | ↑68 | ↑1.044 | ↑20d | — | +17.5% | 56.33/54.51 | +4.95% | 20% |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>📶W9 · W↑108d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Niche APIs formulations contract manufacturing pharma CDMO | 📈 BULL_ANY_MID | 0 | ↑94 | ↑1.045 | ↑49d | — | +53.0% | 64.96/63.59 | +4.53% | 20% |
| [AMAGI](https://in.tradingview.com/chart/?symbol=NSE:AMAGI)<br><sub>📶W9 · ↑CMF23d</sub> | ✓ SAFE | Cloud TV platform for content distribution and monetization | 📈 BULL_ANY_MID | 0 | ↑50 | ↓1.063 | ↑21d | — | +42.5% | 61.37/59.03 | -0.59% | 20% |

```
NSE:GIPCL,NSE:JAYKAY,NSE:ARE&M,NSE:ASTERDM,NSE:INNOVACAP,NSE:PREMIERENE,NSE:PGHL,NSE:TVSSCS,NSE:MARKSANS,NSE:ORCHPHARMA,NSE:RAINBOW,NSE:UDS,NSE:TCIEXP,NSE:JINDALSAW,NSE:KALYANKJIL,NSE:GRPLTD,NSE:AGARWALEYE,NSE:GOODLUCK,NSE:STARHEALTH,NSE:CHOICEIN,NSE:AETHER,NSE:EPACKPEB,NSE:NEOGEN,NSE:SIS,NSE:INOXINDIA,NSE:RUBICON,NSE:ZYDUSLIFE,NSE:HAPPYFORGE,NSE:NOVARTIND,NSE:ENTERO,NSE:CCL,NSE:GLAXO,NSE:RELIGARE,NSE:NEULANDLAB,NSE:SPAL,NSE:UJJIVANSFB,NSE:SHILPAMED,NSE:AMAGI
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (52)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GIPCL](https://in.tradingview.com/chart/?symbol=NSE:GIPCL)<br><sub>📶W9 · W↑67d · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | Power generation thermal plants Gujarat state utilities | ⚡ BULL_ANY_PPV | 94 | 🔄44 | ↑1.017 | ↑1d | SQ·PV | +3.6% | -19.33/-21.29 | +3.58% | 20% |
| [JAYKAY](https://in.tradingview.com/chart/?symbol=NSE:JAYKAY)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Additive manufacturing and 3D printing technology services | ⚡ BULL_ANY_PPV | 89 | 🔄50 | ↑1.030 | ↑1d | SQ·PV | +6.2% | -13.44/-13.57 | +6.22% | 20% |
| [ARE&M](https://in.tradingview.com/chart/?symbol=NSE:ARE&M)<br><sub>📶W9 · W↑62d · 🚀SS · ↓CMF13d</sub> | ✓ SAFE | Lead-acid batteries automotive industrial energy storage | ⚡ BULL_ANY_PPV | 64 | ↑45 | ↑1.025 | ↑1d | SQ·PV | +4.1% | 15.06/10.24 | +4.12% | 20% |
| [ASTERDM](https://in.tradingview.com/chart/?symbol=NSE:ASTERDM)<br><sub>📶W9 · 🚀SS · ↓CMF19d</sub> | ⚠ CAUTION | Private multi-specialty hospital chains India GCC markets | ⚡ BULL_ANY_PPV | 64 | ↑76 | ↑1.025 | ↑1d | SQ·PV | +3.5% | 28.66/24.47 | +3.53% | 20% |
| [INNOVACAP](https://in.tradingview.com/chart/?symbol=NSE:INNOVACAP)<br><sub>📶W9 · W↑84d · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | Tablet manufacturing pharmaceuticals India generic drugs | ⚡ BULL_ANY_PPV | 62 | ↑83 | ↑1.022 | ↑3d | SQ·PV | +3.9% | 57.49/51.69 | +0.81% | 20% |
| [PREMIERENE](https://in.tradingview.com/chart/?symbol=NSE:PREMIERENE)<br><sub>📶W9 · W↑108d · 🚀SS · ↓CMF10d</sub> | ✓ SAFE | Solar cells modules manufacturing for rooftop commercial industrial | ⚡ BULL_ANY_PPV | 59 | ↑69 | ↑1.037 | ↑1d | SQ·PV | +4.3% | -13.6/-26.35 | +4.34% | 20% |
| [PGHL](https://in.tradingview.com/chart/?symbol=NSE:PGHL)<br><sub>📶W9 · W↑74d · ↓CMF6d</sub> | ⚠ CAUTION | Vitamins, minerals, supplements, and OTC pharmaceuticals manufacturer | ⚡ BULL_ANY_PPV | 59 | ↑76 | ↑1.041 | ↑1d | SQ·PV | +5.6% | 50.02/46.09 | +5.58% | 20% |
| [TVSSCS](https://in.tradingview.com/chart/?symbol=NSE:TVSSCS)<br><sub>📶W9 · W↑67d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Third-party logistics provider for automotive manufacturers | ⚡ BULL_ANY_PPV | 59 | ↑74 | ↑1.033 | ↑1d | SQ·PV | +4.8% | 43.59/42.62 | +4.82% | 10% 🟩 |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS)<br><sub>📶W9 · W↑67d · 🚀SS · ↓CMF12d</sub> | ✓ SAFE | Generic pharmaceutical formulations for regulated global markets | ⚡ BULL_ANY_PPV | 58 | ↑91 | ↑1.047 | ↑2d | SQ·PV | +6.2% | 51.91/47.69 | +5.26% | 20% |
| [ORCHPHARMA](https://in.tradingview.com/chart/?symbol=NSE:ORCHPHARMA)<br><sub>📶W9 · W↑67d · ↑CMF30d</sub> | ✓ SAFE | Injectables manufacturer serving hospitals and critical care markets | ⚡ BULL_ANY_PPV | 58 | ↑94 | ↑1.074 | ↑2d | SQ·PV | +13.7% | 35.69/27.67 | +4.86% | 20% |
| [RAINBOW](https://in.tradingview.com/chart/?symbol=NSE:RAINBOW)<br><sub>📶W9 · W↑70d · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION | Pediatric obstetrics gynecology hospital chain India | ⚡ BULL_ANY_PPV | 58 | ↑63 | ↑1.030 | ↑2d | SQ·PV | +4.2% | 37.85/31.78 | +3.52% | 20% |
| [UDS](https://in.tradingview.com/chart/?symbol=NSE:UDS)<br><sub>📶W9 · W↑67d · ↓CMF4d</sub> | ✓ SAFE | Facilities management and business support services provider | ⚡ BULL_ANY_PPV | 54 | ↑47 | ↑1.044 | ↑6d | SQ·PV | +8.1% | 55.99/54.86 | +5.49% | 20% |
| [TCIEXP](https://in.tradingview.com/chart/?symbol=NSE:TCIEXP)<br><sub>📶W9 · W↑24d · 🚀SS·11x · ↑CMF11d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 49 | 🔄21 | ↑1.063 | ↑1d | PV | +10.9% | -6.34/-10.4 | +10.93% | 20% |
| [JINDALSAW](https://in.tradingview.com/chart/?symbol=NSE:JINDALSAW)<br><sub>📶W9 · W↑34d · ↑CMF5d</sub> | ✓ SAFE | Submerged arc welded pipes manufacturer for infrastructure | ⚡ BULL_ANY_PPV | 40 | ↑86 | ↑1.039 | ↑20d | SQ·PV | +21.8% | 37.95/34.22 | +4.87% | 20% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>📶W9 · W↑19d · 🚀SS·12x · ↑CMF18d</sub> | ✓ SAFE | Gold jewellery retail across India and Middle East markets | ⚡ BULL_ANY_PPV | 19 | ↑22 | ↑1.142 | ↑1d | PV | +18.4% | 26.29/19.73 | +18.40% | 20% |
| [GRPLTD](https://in.tradingview.com/chart/?symbol=NSE:GRPLTD)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF18d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 18 | ↑31 | ↑1.034 | ↑2d | PV | +6.2% | 20.61/13.61 | +2.30% | 20% |
| [AGARWALEYE](https://in.tradingview.com/chart/?symbol=NSE:AGARWALEYE)<br><sub>📶W9 · W↑14d · ↑CMF0d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 10 | ↑56 | ↑1.018 | ↑15d | PV | +9.2% | 26.87/24.24 | +1.62% | 20% |
| [GOODLUCK](https://in.tradingview.com/chart/?symbol=NSE:GOODLUCK)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | Steel pipes, forgings, tubes for automotive, industrial | ⚡ BULL_ANY_PPV | 3 | ↑86 | ↑1.049 | ↑17d | PV | +18.0% | 49.57/48.41 | +6.62% | 20% |
| [STARHEALTH](https://in.tradingview.com/chart/?symbol=NSE:STARHEALTH)<br><sub>📶W9 · W↑70d · ↑CMF15d</sub> | ✓ SAFE | Health insurance policies, retail individuals, hospitals network | ⚡ BULL_ANY_PPV | 3 | ↑85 | ↑1.031 | ↑17d | PV | +15.6% | 54.31/52.82 | +3.26% | 20% |
| [CHOICEIN](https://in.tradingview.com/chart/?symbol=NSE:CHOICEIN)<br><sub>📶W9 · W↑19d · 🚀SS·9x · ↑CMF7d</sub> | ✓ SAFE | Stockbroking wealth management MSME lending insurance distribution financial services | ⚡ BULL_ANY_PPV | 0 | ↑62 | ↑1.071 | ↑20d | PV | +26.6% | 59.2/57.93 | +7.98% | 20% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF14d</sub> | ✓ SAFE | Specialty chemicals for pharma agrochemical material science | ⚡ BULL_ANY_PPV | 0 | ↑94 | ↑1.087 | ↑27d | PV | +35.2% | 69.16/65.98 | +5.12% | 20% |
| [EPACKPEB](https://in.tradingview.com/chart/?symbol=NSE:EPACKPEB)<br><sub>📶W9 · W↑72d · 🚀SS · ↑CMF19d</sub> | ✓ SAFE | Steel prefab buildings manufacturing construction services India | 📈 BULL_ANY_MID | 89 | 🔄50 | ↑1.049 | ↑1d | SQ | +7.5% | 28.31/27.93 | +7.55% | 20% |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>📶W9 · W↑4d · ↑CMF24d</sub> | ✓ SAFE | Bromine and lithium specialty chemicals for pharma agriculture | 📈 BULL_ANY_MID | 64 | ↑91 | ↑1.027 | ↑1d | SQ | +3.9% | 27.24/25.07 | +3.89% | 20% |
| [SIS](https://in.tradingview.com/chart/?symbol=NSE:SIS)<br><sub>📶W9 · W↑67d · 🚀SS · ↓CMF18d</sub> | ✓ SAFE | Security guarding, facility management, cash logistics operations | 📈 BULL_ANY_MID | 63 | ↑86 | ↑1.019 | ↑2d | SQ | +2.3% | 24.32/19.56 | +1.80% | 20% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF24d</sub> | ✓ SAFE | Cryogenic equipment manufacturer for LNG and industrial gas sectors | 📈 BULL_ANY_MID | 59 | ↑95 | ↑1.057 | ↑1d | SQ | +7.0% | 23.24/20.59 | +6.95% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · ↑CMF5d</sub> | ✓ SAFE | Complex generics and specialty formulations manufacturing pharma | 📈 BULL_ANY_MID | 56 | ↑50 | ↓1.020 | ↑4d | SQ | +7.1% | 38.64/36.15 | -0.49% | 20% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>📶W9 · W↑56d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | Pharmaceuticals: generics, branded drugs, consumer wellness products | 📈 BULL_ANY_MID | 49 | 🔄73 | ↑1.031 | ↑1d | — | +3.9% | 44.71/41.57 | +3.92% | 20% |
| [HAPPYFORGE](https://in.tradingview.com/chart/?symbol=NSE:HAPPYFORGE)<br><sub>📶W9 · W↑14d · ↑CMF13d</sub> | ✓ SAFE | Heavy forged components supplier automotive industrial OEMs | 📈 BULL_ANY_MID | 23 | ↑88 | ↑1.028 | ↑2d | — | +4.6% | 33.06/30.32 | +2.85% | 20% |
| [NOVARTIND](https://in.tradingview.com/chart/?symbol=NSE:NOVARTIND)<br><sub>📶W9 · W↑57d · 🚀SS · ↓CMF10d</sub> | ⚠ CAUTION | Pharmaceutical distribution and wholesale medicines trading India | 📈 BULL_ANY_MID | 15 | ↑50 | ↑1.011 | ↑15d | — | +8.1% | 36.99/36.46 | +0.96% | 20% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>📶W9 · W↑4d · ↑CMF0d</sub> | ⚠ CAUTION | Pharmaceutical surgical products distributor hospitals clinics retail | 📈 BULL_ANY_MID | 13 | ↑50 | ↑1.023 | ↑12d | — | +11.8% | 22.56/22.0 | +3.75% | 20% |
| [CCL](https://in.tradingview.com/chart/?symbol=NSE:CCL)<br><sub>📶W9 · W↑19d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | Instant coffee manufacturing and export global markets | 📈 BULL_ANY_MID | 9 | ↑80 | ↑1.022 | ↑16d | — | +8.5% | 51.92/50.45 | +2.37% | 20% |
| [GLAXO](https://in.tradingview.com/chart/?symbol=NSE:GLAXO)<br><sub>📶W9 · W↑14d · ↑CMF14d</sub> | ✓ SAFE | Pharmaceuticals manufacturing vaccines respiratory gastrointestinal antibiotics India | 📈 BULL_ANY_MID | 7 | ↑27 | ↑1.018 | ↑18d | — | +15.0% | 34.71/32.79 | +1.23% | 20% |
| [RELIGARE](https://in.tradingview.com/chart/?symbol=NSE:RELIGARE)<br><sub>📶W9 · W↑70d · ↑CMF12d</sub> | ✓ SAFE | Financial services: insurance, broking, SME lending | 📈 BULL_ANY_MID | 5 | ↑68 | ↑1.018 | ↑21d | — | +19.0% | 45.27/43.68 | +2.03% | 20% |
| [NEULANDLAB](https://in.tradingview.com/chart/?symbol=NSE:NEULANDLAB)<br><sub>📶W9 · W↑67d · 🚀SS · ★ · ↓CMF2d</sub> | ✓ SAFE | Pharma APIs CDMO services domestic international markets | 📈 BULL_ANY_MID | 4 | ↑87 | ↑1.042 | ↑16d | — | +14.8% | 70.8/70.33 | +3.46% | 20% |
| [SPAL](https://in.tradingview.com/chart/?symbol=NSE:SPAL)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Knitted infant children's apparel manufacturer exporter textile | 📈 BULL_ANY_MID | 1 | ↑94 | ↑1.056 | ↑19d | — | +48.1% | 63.52/63.02 | +1.52% | 20% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Microfinance bank serving unbanked low-income borrowers | 📈 BULL_ANY_MID | 0 | ↑68 | ↑1.044 | ↑20d | — | +17.5% | 56.33/54.51 | +4.95% | 20% |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>📶W9 · W↑108d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Niche APIs formulations contract manufacturing pharma CDMO | 📈 BULL_ANY_MID | 0 | ↑94 | ↑1.045 | ↑49d | — | +53.0% | 64.96/63.59 | +4.53% | 20% |
| [AMAGI](https://in.tradingview.com/chart/?symbol=NSE:AMAGI)<br><sub>📶W9 · ↑CMF23d</sub> | ✓ SAFE | Cloud TV platform for content distribution and monetization | 📈 BULL_ANY_MID | 0 | ↑50 | ↓1.063 | ↑21d | — | +42.5% | 61.37/59.03 | -0.59% | 20% |
| [TATAINVEST](https://in.tradingview.com/chart/?symbol=NSE:TATAINVEST)<br><sub>🚀SS · ↓CMF9d</sub> | ⚠ CAUTION | Investment company holding equities, debt, mutual funds | ⚡ BULL_ANY_PPV | 64 | ↑33 | ↑1.020 | ↑1d | SQ·PV | +3.3% | -7.98/-15.66 | +3.27% | 20% |
| [JKIL](https://in.tradingview.com/chart/?symbol=NSE:JKIL)<br><sub>W↑14d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | EPC contractor, urban transport infrastructure, roads and metro | ⚡ BULL_ANY_PPV | 59 | 🔄20 | ↑1.014 | ↑1d | PV | +3.7% | -2.03/-3.71 | +3.67% | 20% |
| [CARRARO](https://in.tradingview.com/chart/?symbol=NSE:CARRARO)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Axles transmission systems agriculture construction equipment manufacturer | ⚡ BULL_ANY_PPV | 54 | 🔄66 | ↑1.029 | ↑1d | PV | +7.0% | -7.32/-7.78 | +6.96% | 20% |
| [HCLTECH](https://in.tradingview.com/chart/?symbol=NSE:HCLTECH)<br><sub>🚀SS · ↑CMF10d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 49 | 🔄3 | ↑1.033 | ↑1d | PV | +5.7% | -42.54/-49.08 | +5.74% | 20% |
| [JYOTHYLAB](https://in.tradingview.com/chart/?symbol=NSE:JYOTHYLAB)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Fabric care, dish wash, personal care FMCG brands | ⚡ BULL_ANY_PPV | 49 | 🔄4 | ↑1.035 | ↑1d | PV | +6.6% | -45.69/-52.26 | +6.62% | 20% |
| [LTM](https://in.tradingview.com/chart/?symbol=NSE:LTM)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 47 | 🔄4 | ↑1.007 | ↓13d | — | -3.6% | -56.4/-61.13 | +2.08% | 20% |
| [AWFIS](https://in.tradingview.com/chart/?symbol=NSE:AWFIS)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Flexible workspace operator for entrepreneurs and corporates | 📈 BULL_ANY_MID | 99 | 🔄2 | ↑1.011 | ↑1d | SQ | +2.6% | -11.98/-14.8 | +2.57% | 20% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>W↑56d · 🚀SS · ↓CMF4d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 98 | 🔄55 | ↑1.013 | ↑2d | SQ | +3.2% | 2.18/-1.42 | +1.13% | 20% |
| [JSLL](https://in.tradingview.com/chart/?symbol=NSE:JSLL)<br><sub>🚀SS · ↑CMF1d</sub> | ✓ SAFE | Ayurvedic hospitals and wellness clinics serving Indian patients | 📈 BULL_ANY_MID | 94 | 🔄24 | ↑1.022 | ↑1d | SQ | +5.0% | -36.71/-39.86 | +5.00% | 20% |
| [APOLLOPIPE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOPIPE)<br><sub>↓CMF15d · DEL67%</sub> | ✓ SAFE | PVC pipes infrastructure water management agriculture | 📈 BULL_ANY_MID | 94 | 🔄82 | ↑1.018 | ↑1d | SQ | +4.2% | -40.56/-42.17 | +4.16% | 20% |
| [GKSL](https://in.tradingview.com/chart/?symbol=NSE:GKSL)<br><sub>↓CMF30d</sub> | ✓ SAFE | Kidney transplant dialysis hospital network healthcare | 📈 BULL_ANY_MID | 69 | ↑50 | ↑1.012 | ↑1d | SQ | +1.3% | -4.99/-10.16 | +1.34% | 20% |
| [AMBER](https://in.tradingview.com/chart/?symbol=NSE:AMBER)<br><sub>🚀SS · ↓CMF10d</sub> | ✓ SAFE | AC manufacturing and EMS for consumer appliances | 📈 BULL_ANY_MID | 59 | 🔄52 | ↑1.005 | ↑1d | — | +2.4% | -17.24/-19.21 | +2.38% | 20% |
| [MUTHOOTFIN](https://in.tradingview.com/chart/?symbol=NSE:MUTHOOTFIN)<br><sub>🚀SS · ↓CMF1d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 51 | 🔄30 | ↑1.005 | ↓9d | — | -2.4% | -40.8/-42.17 | +3.40% | 20% |
| [VIKRAMSOLR](https://in.tradingview.com/chart/?symbol=NSE:VIKRAMSOLR)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Solar PV module manufacturer, EPC services, renewable energy sector | 📈 BULL_ANY_MID | 46 | 🔄50 | ↑1.004 | ↓14d | — | -4.4% | -45.2/-45.34 | +5.21% | 20% |

```
NSE:GIPCL,NSE:JAYKAY,NSE:ARE&M,NSE:ASTERDM,NSE:INNOVACAP,NSE:PREMIERENE,NSE:PGHL,NSE:TVSSCS,NSE:MARKSANS,NSE:ORCHPHARMA,NSE:RAINBOW,NSE:UDS,NSE:TCIEXP,NSE:JINDALSAW,NSE:KALYANKJIL,NSE:GRPLTD,NSE:AGARWALEYE,NSE:GOODLUCK,NSE:STARHEALTH,NSE:CHOICEIN,NSE:AETHER,NSE:EPACKPEB,NSE:NEOGEN,NSE:SIS,NSE:INOXINDIA,NSE:RUBICON,NSE:ZYDUSLIFE,NSE:HAPPYFORGE,NSE:NOVARTIND,NSE:ENTERO,NSE:CCL,NSE:GLAXO,NSE:RELIGARE,NSE:NEULANDLAB,NSE:SPAL,NSE:UJJIVANSFB,NSE:SHILPAMED,NSE:AMAGI,NSE:TATAINVEST,NSE:JKIL,NSE:CARRARO,NSE:HCLTECH,NSE:JYOTHYLAB,NSE:LTM,NSE:AWFIS,NSE:DIVISLAB,NSE:JSLL,NSE:APOLLOPIPE,NSE:GKSL,NSE:AMBER,NSE:MUTHOOTFIN,NSE:VIKRAMSOLR
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (26)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [GIPCL](https://in.tradingview.com/chart/?symbol=NSE:GIPCL)<br><sub>📶W9 · W↑67d · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | Power generation thermal plants Gujarat state utilities | ⚡ BULL_ANY_PPV | 94 | 🔄44 | ↑1.017 | ↑1d | SQ·PV | +3.6% | -19.33/-21.29 | +3.58% | 20% |
| [JAYKAY](https://in.tradingview.com/chart/?symbol=NSE:JAYKAY)<br><sub>📶W9 · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Additive manufacturing and 3D printing technology services | ⚡ BULL_ANY_PPV | 89 | 🔄50 | ↑1.030 | ↑1d | SQ·PV | +6.2% | -13.44/-13.57 | +6.22% | 20% |
| [ARE&M](https://in.tradingview.com/chart/?symbol=NSE:ARE&M)<br><sub>📶W9 · W↑62d · 🚀SS · ↓CMF13d</sub> | ✓ SAFE | Lead-acid batteries automotive industrial energy storage | ⚡ BULL_ANY_PPV | 64 | ↑45 | ↑1.025 | ↑1d | SQ·PV | +4.1% | 15.06/10.24 | +4.12% | 20% |
| [ASTERDM](https://in.tradingview.com/chart/?symbol=NSE:ASTERDM)<br><sub>📶W9 · 🚀SS · ↓CMF19d</sub> | ⚠ CAUTION | Private multi-specialty hospital chains India GCC markets | ⚡ BULL_ANY_PPV | 64 | ↑76 | ↑1.025 | ↑1d | SQ·PV | +3.5% | 28.66/24.47 | +3.53% | 20% |
| [INNOVACAP](https://in.tradingview.com/chart/?symbol=NSE:INNOVACAP)<br><sub>📶W9 · W↑84d · 🚀SS · ↓CMF7d</sub> | ✓ SAFE | Tablet manufacturing pharmaceuticals India generic drugs | ⚡ BULL_ANY_PPV | 62 | ↑83 | ↑1.022 | ↑3d | SQ·PV | +3.9% | 57.49/51.69 | +0.81% | 20% |
| [PREMIERENE](https://in.tradingview.com/chart/?symbol=NSE:PREMIERENE)<br><sub>📶W9 · W↑108d · 🚀SS · ↓CMF10d</sub> | ✓ SAFE | Solar cells modules manufacturing for rooftop commercial industrial | ⚡ BULL_ANY_PPV | 59 | ↑69 | ↑1.037 | ↑1d | SQ·PV | +4.3% | -13.6/-26.35 | +4.34% | 20% |
| [PGHL](https://in.tradingview.com/chart/?symbol=NSE:PGHL)<br><sub>📶W9 · W↑74d · ↓CMF6d</sub> | ⚠ CAUTION | Vitamins, minerals, supplements, and OTC pharmaceuticals manufacturer | ⚡ BULL_ANY_PPV | 59 | ↑76 | ↑1.041 | ↑1d | SQ·PV | +5.6% | 50.02/46.09 | +5.58% | 20% |
| [TVSSCS](https://in.tradingview.com/chart/?symbol=NSE:TVSSCS)<br><sub>📶W9 · W↑67d · 🚀SS · ↓CMF4d</sub> | ✓ SAFE | Third-party logistics provider for automotive manufacturers | ⚡ BULL_ANY_PPV | 59 | ↑74 | ↑1.033 | ↑1d | SQ·PV | +4.8% | 43.59/42.62 | +4.82% | 10% 🟩 |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS)<br><sub>📶W9 · W↑67d · 🚀SS · ↓CMF12d</sub> | ✓ SAFE | Generic pharmaceutical formulations for regulated global markets | ⚡ BULL_ANY_PPV | 58 | ↑91 | ↑1.047 | ↑2d | SQ·PV | +6.2% | 51.91/47.69 | +5.26% | 20% |
| [ORCHPHARMA](https://in.tradingview.com/chart/?symbol=NSE:ORCHPHARMA)<br><sub>📶W9 · W↑67d · ↑CMF30d</sub> | ✓ SAFE | Injectables manufacturer serving hospitals and critical care markets | ⚡ BULL_ANY_PPV | 58 | ↑94 | ↑1.074 | ↑2d | SQ·PV | +13.7% | 35.69/27.67 | +4.86% | 20% |
| [RAINBOW](https://in.tradingview.com/chart/?symbol=NSE:RAINBOW)<br><sub>📶W9 · W↑70d · 🚀SS · ↑CMF30d</sub> | ⚠ CAUTION | Pediatric obstetrics gynecology hospital chain India | ⚡ BULL_ANY_PPV | 58 | ↑63 | ↑1.030 | ↑2d | SQ·PV | +4.2% | 37.85/31.78 | +3.52% | 20% |
| [UDS](https://in.tradingview.com/chart/?symbol=NSE:UDS)<br><sub>📶W9 · W↑67d · ↓CMF4d</sub> | ✓ SAFE | Facilities management and business support services provider | ⚡ BULL_ANY_PPV | 54 | ↑47 | ↑1.044 | ↑6d | SQ·PV | +8.1% | 55.99/54.86 | +5.49% | 20% |
| [JINDALSAW](https://in.tradingview.com/chart/?symbol=NSE:JINDALSAW)<br><sub>📶W9 · W↑34d · ↑CMF5d</sub> | ✓ SAFE | Submerged arc welded pipes manufacturer for infrastructure | ⚡ BULL_ANY_PPV | 40 | ↑86 | ↑1.039 | ↑20d | SQ·PV | +21.8% | 37.95/34.22 | +4.87% | 20% |
| [EPACKPEB](https://in.tradingview.com/chart/?symbol=NSE:EPACKPEB)<br><sub>📶W9 · W↑72d · 🚀SS · ↑CMF19d</sub> | ✓ SAFE | Steel prefab buildings manufacturing construction services India | 📈 BULL_ANY_MID | 89 | 🔄50 | ↑1.049 | ↑1d | SQ | +7.5% | 28.31/27.93 | +7.55% | 20% |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>📶W9 · W↑4d · ↑CMF24d</sub> | ✓ SAFE | Bromine and lithium specialty chemicals for pharma agriculture | 📈 BULL_ANY_MID | 64 | ↑91 | ↑1.027 | ↑1d | SQ | +3.9% | 27.24/25.07 | +3.89% | 20% |
| [SIS](https://in.tradingview.com/chart/?symbol=NSE:SIS)<br><sub>📶W9 · W↑67d · 🚀SS · ↓CMF18d</sub> | ✓ SAFE | Security guarding, facility management, cash logistics operations | 📈 BULL_ANY_MID | 63 | ↑86 | ↑1.019 | ↑2d | SQ | +2.3% | 24.32/19.56 | +1.80% | 20% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF24d</sub> | ✓ SAFE | Cryogenic equipment manufacturer for LNG and industrial gas sectors | 📈 BULL_ANY_MID | 59 | ↑95 | ↑1.057 | ↑1d | SQ | +7.0% | 23.24/20.59 | +6.95% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · ↑CMF5d</sub> | ✓ SAFE | Complex generics and specialty formulations manufacturing pharma | 📈 BULL_ANY_MID | 56 | ↑50 | ↓1.020 | ↑4d | SQ | +7.1% | 38.64/36.15 | -0.49% | 20% |
| [TATAINVEST](https://in.tradingview.com/chart/?symbol=NSE:TATAINVEST)<br><sub>🚀SS · ↓CMF9d</sub> | ⚠ CAUTION | Investment company holding equities, debt, mutual funds | ⚡ BULL_ANY_PPV | 64 | ↑33 | ↑1.020 | ↑1d | SQ·PV | +3.3% | -7.98/-15.66 | +3.27% | 20% |
| [AWFIS](https://in.tradingview.com/chart/?symbol=NSE:AWFIS)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Flexible workspace operator for entrepreneurs and corporates | 📈 BULL_ANY_MID | 99 | 🔄2 | ↑1.011 | ↑1d | SQ | +2.6% | -11.98/-14.8 | +2.57% | 20% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>W↑56d · 🚀SS · ↓CMF4d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 98 | 🔄55 | ↑1.013 | ↑2d | SQ | +3.2% | 2.18/-1.42 | +1.13% | 20% |
| [JSLL](https://in.tradingview.com/chart/?symbol=NSE:JSLL)<br><sub>🚀SS · ↑CMF1d</sub> | ✓ SAFE | Ayurvedic hospitals and wellness clinics serving Indian patients | 📈 BULL_ANY_MID | 94 | 🔄24 | ↑1.022 | ↑1d | SQ | +5.0% | -36.71/-39.86 | +5.00% | 20% |
| [APOLLOPIPE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOPIPE)<br><sub>↓CMF15d · DEL67%</sub> | ✓ SAFE | PVC pipes infrastructure water management agriculture | 📈 BULL_ANY_MID | 94 | 🔄82 | ↑1.018 | ↑1d | SQ | +4.2% | -40.56/-42.17 | +4.16% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>↓CMF19d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 69 | ↓38 | ↑1.004 | ↑1d | SQ | +0.4% | -36.31/-41.57 | +0.36% | 20% |
| [GKSL](https://in.tradingview.com/chart/?symbol=NSE:GKSL)<br><sub>↓CMF30d</sub> | ✓ SAFE | Kidney transplant dialysis hospital network healthcare | 📈 BULL_ANY_MID | 69 | ↑50 | ↑1.012 | ↑1d | SQ | +1.3% | -4.99/-10.16 | +1.34% | 20% |
| [POWERGRID](https://in.tradingview.com/chart/?symbol=NSE:POWERGRID)<br><sub>🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↓39 | ↓1.001 | ↑2d | SQ | +0.2% | -10.75/-15.11 | -0.07% | 20% |

```
NSE:GIPCL,NSE:JAYKAY,NSE:ARE&M,NSE:ASTERDM,NSE:INNOVACAP,NSE:PREMIERENE,NSE:PGHL,NSE:TVSSCS,NSE:MARKSANS,NSE:ORCHPHARMA,NSE:RAINBOW,NSE:UDS,NSE:JINDALSAW,NSE:EPACKPEB,NSE:NEOGEN,NSE:SIS,NSE:INOXINDIA,NSE:RUBICON,NSE:TATAINVEST,NSE:AWFIS,NSE:DIVISLAB,NSE:JSLL,NSE:APOLLOPIPE,NSE:TATACONSUM,NSE:GKSL,NSE:POWERGRID
```

---

### 🔥 MAJOR — PPV confirmed (12)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [TCIEXP](https://in.tradingview.com/chart/?symbol=NSE:TCIEXP)<br><sub>📶W9 · W↑24d · 🚀SS·11x · ↑CMF11d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 49 | 🔄21 | ↑1.063 | ↑1d | PV | +10.9% | -6.34/-10.4 | +10.93% | 20% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>📶W9 · W↑19d · 🚀SS·12x · ↑CMF18d</sub> | ✓ SAFE | Gold jewellery retail across India and Middle East markets | ⚡ BULL_ANY_PPV | 19 | ↑22 | ↑1.142 | ↑1d | PV | +18.4% | 26.29/19.73 | +18.40% | 20% |
| [GRPLTD](https://in.tradingview.com/chart/?symbol=NSE:GRPLTD)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF18d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 18 | ↑31 | ↑1.034 | ↑2d | PV | +6.2% | 20.61/13.61 | +2.30% | 20% |
| [AGARWALEYE](https://in.tradingview.com/chart/?symbol=NSE:AGARWALEYE)<br><sub>📶W9 · W↑14d · ↑CMF0d</sub> | ⚠ CAUTION |  | ⚡ BULL_ANY_PPV | 10 | ↑56 | ↑1.018 | ↑15d | PV | +9.2% | 26.87/24.24 | +1.62% | 20% |
| [GOODLUCK](https://in.tradingview.com/chart/?symbol=NSE:GOODLUCK)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | Steel pipes, forgings, tubes for automotive, industrial | ⚡ BULL_ANY_PPV | 3 | ↑86 | ↑1.049 | ↑17d | PV | +18.0% | 49.57/48.41 | +6.62% | 20% |
| [STARHEALTH](https://in.tradingview.com/chart/?symbol=NSE:STARHEALTH)<br><sub>📶W9 · W↑70d · ↑CMF15d</sub> | ✓ SAFE | Health insurance policies, retail individuals, hospitals network | ⚡ BULL_ANY_PPV | 3 | ↑85 | ↑1.031 | ↑17d | PV | +15.6% | 54.31/52.82 | +3.26% | 20% |
| [CHOICEIN](https://in.tradingview.com/chart/?symbol=NSE:CHOICEIN)<br><sub>📶W9 · W↑19d · 🚀SS·9x · ↑CMF7d</sub> | ✓ SAFE | Stockbroking wealth management MSME lending insurance distribution financial services | ⚡ BULL_ANY_PPV | 0 | ↑62 | ↑1.071 | ↑20d | PV | +26.6% | 59.2/57.93 | +7.98% | 20% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>📶W9 · W↑14d · 🚀SS · ↑CMF14d</sub> | ✓ SAFE | Specialty chemicals for pharma agrochemical material science | ⚡ BULL_ANY_PPV | 0 | ↑94 | ↑1.087 | ↑27d | PV | +35.2% | 69.16/65.98 | +5.12% | 20% |
| [JKIL](https://in.tradingview.com/chart/?symbol=NSE:JKIL)<br><sub>W↑14d · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | EPC contractor, urban transport infrastructure, roads and metro | ⚡ BULL_ANY_PPV | 59 | 🔄20 | ↑1.014 | ↑1d | PV | +3.7% | -2.03/-3.71 | +3.67% | 20% |
| [CARRARO](https://in.tradingview.com/chart/?symbol=NSE:CARRARO)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Axles transmission systems agriculture construction equipment manufacturer | ⚡ BULL_ANY_PPV | 54 | 🔄66 | ↑1.029 | ↑1d | PV | +7.0% | -7.32/-7.78 | +6.96% | 20% |
| [HCLTECH](https://in.tradingview.com/chart/?symbol=NSE:HCLTECH)<br><sub>🚀SS · ↑CMF10d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 49 | 🔄3 | ↑1.033 | ↑1d | PV | +5.7% | -42.54/-49.08 | +5.74% | 20% |
| [JYOTHYLAB](https://in.tradingview.com/chart/?symbol=NSE:JYOTHYLAB)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Fabric care, dish wash, personal care FMCG brands | ⚡ BULL_ANY_PPV | 49 | 🔄4 | ↑1.035 | ↑1d | PV | +6.6% | -45.69/-52.26 | +6.62% | 20% |

```
NSE:TCIEXP,NSE:KALYANKJIL,NSE:GRPLTD,NSE:AGARWALEYE,NSE:GOODLUCK,NSE:STARHEALTH,NSE:CHOICEIN,NSE:AETHER,NSE:JKIL,NSE:CARRARO,NSE:HCLTECH,NSE:JYOTHYLAB
```

### 🟢 OVERSOLD — reversal from −53/−60 (6)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [LTM](https://in.tradingview.com/chart/?symbol=NSE:LTM)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 47 | 🔄4 | ↑1.007 | ↓13d | — | -3.6% | -56.4/-61.13 | +2.08% | 20% |
| [TATASTEEL](https://in.tradingview.com/chart/?symbol=NSE:TATASTEEL)<br><sub>🚀SS · ↓CMF8d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 5 | ↓50 | ↑0.995 | ↓22d | — | -9.7% | -60.32/-63.96 | +1.29% | 20% |
| [JINDALSTEL](https://in.tradingview.com/chart/?symbol=NSE:JINDALSTEL)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 5 | ↓38 | ↑0.982 | ↓35d | — | -15.2% | -70.63/-73.17 | +0.98% | 20% |
| [INFY](https://in.tradingview.com/chart/?symbol=NSE:INFY)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE |  | 🟡 BULL_OS_L2 | 18 | ↓2 | ↑1.001 | ↓12d | — | -8.4% | -50.54/-55.6 | +0.59% | 20% |
| [SUPREMEIND](https://in.tradingview.com/chart/?symbol=NSE:SUPREMEIND)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Plastic pipes, packaging, industrial products manufacturer | 🟡 BULL_OS_L2 | 11 | ↓10 | ↑0.990 | ↓14d | — | -8.4% | -54.4/-55.08 | +1.54% | 20% |
| [WAAREEENER](https://in.tradingview.com/chart/?symbol=NSE:WAAREEENER)<br><sub>🚀SS · ↓CMF11d · ⚠️TRAP</sub> | ✓ SAFE | Solar photovoltaic modules manufacturer, renewable energy sector | 🟡 BULL_OS_L2 | 7 | ↓27 | ↑0.991 | ↓18d | — | -6.2% | -55.62/-55.9 | +1.42% | 20% |

```
NSE:LTM,NSE:TATASTEEL,NSE:JINDALSTEL,NSE:INFY,NSE:SUPREMEIND,NSE:WAAREEENER
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (24)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>📶W9 · W↑56d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | Pharmaceuticals: generics, branded drugs, consumer wellness products | 📈 BULL_ANY_MID | 49 | 🔄73 | ↑1.031 | ↑1d | — | +3.9% | 44.71/41.57 | +3.92% | 20% |
| [HAPPYFORGE](https://in.tradingview.com/chart/?symbol=NSE:HAPPYFORGE)<br><sub>📶W9 · W↑14d · ↑CMF13d</sub> | ✓ SAFE | Heavy forged components supplier automotive industrial OEMs | 📈 BULL_ANY_MID | 23 | ↑88 | ↑1.028 | ↑2d | — | +4.6% | 33.06/30.32 | +2.85% | 20% |
| [NOVARTIND](https://in.tradingview.com/chart/?symbol=NSE:NOVARTIND)<br><sub>📶W9 · W↑57d · 🚀SS · ↓CMF10d</sub> | ⚠ CAUTION | Pharmaceutical distribution and wholesale medicines trading India | 📈 BULL_ANY_MID | 15 | ↑50 | ↑1.011 | ↑15d | — | +8.1% | 36.99/36.46 | +0.96% | 20% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>📶W9 · W↑4d · ↑CMF0d</sub> | ⚠ CAUTION | Pharmaceutical surgical products distributor hospitals clinics retail | 📈 BULL_ANY_MID | 13 | ↑50 | ↑1.023 | ↑12d | — | +11.8% | 22.56/22.0 | +3.75% | 20% |
| [CCL](https://in.tradingview.com/chart/?symbol=NSE:CCL)<br><sub>📶W9 · W↑19d · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | Instant coffee manufacturing and export global markets | 📈 BULL_ANY_MID | 9 | ↑80 | ↑1.022 | ↑16d | — | +8.5% | 51.92/50.45 | +2.37% | 20% |
| [GLAXO](https://in.tradingview.com/chart/?symbol=NSE:GLAXO)<br><sub>📶W9 · W↑14d · ↑CMF14d</sub> | ✓ SAFE | Pharmaceuticals manufacturing vaccines respiratory gastrointestinal antibiotics India | 📈 BULL_ANY_MID | 7 | ↑27 | ↑1.018 | ↑18d | — | +15.0% | 34.71/32.79 | +1.23% | 20% |
| [RELIGARE](https://in.tradingview.com/chart/?symbol=NSE:RELIGARE)<br><sub>📶W9 · W↑70d · ↑CMF12d</sub> | ✓ SAFE | Financial services: insurance, broking, SME lending | 📈 BULL_ANY_MID | 5 | ↑68 | ↑1.018 | ↑21d | — | +19.0% | 45.27/43.68 | +2.03% | 20% |
| [NEULANDLAB](https://in.tradingview.com/chart/?symbol=NSE:NEULANDLAB)<br><sub>📶W9 · W↑67d · 🚀SS · ★ · ↓CMF2d</sub> | ✓ SAFE | Pharma APIs CDMO services domestic international markets | 📈 BULL_ANY_MID | 4 | ↑87 | ↑1.042 | ↑16d | — | +14.8% | 70.8/70.33 | +3.46% | 20% |
| [SPAL](https://in.tradingview.com/chart/?symbol=NSE:SPAL)<br><sub>📶W9 · W↑29d · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Knitted infant children's apparel manufacturer exporter textile | 📈 BULL_ANY_MID | 1 | ↑94 | ↑1.056 | ↑19d | — | +48.1% | 63.52/63.02 | +1.52% | 20% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>📶W9 · W↑19d · 🚀SS · ↑CMF18d</sub> | ✓ SAFE | Microfinance bank serving unbanked low-income borrowers | 📈 BULL_ANY_MID | 0 | ↑68 | ↑1.044 | ↑20d | — | +17.5% | 56.33/54.51 | +4.95% | 20% |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>📶W9 · W↑108d · 🚀SS · ↑CMF12d</sub> | ✓ SAFE | Niche APIs formulations contract manufacturing pharma CDMO | 📈 BULL_ANY_MID | 0 | ↑94 | ↑1.045 | ↑49d | — | +53.0% | 64.96/63.59 | +4.53% | 20% |
| [AMAGI](https://in.tradingview.com/chart/?symbol=NSE:AMAGI)<br><sub>📶W9 · ↑CMF23d</sub> | ✓ SAFE | Cloud TV platform for content distribution and monetization | 📈 BULL_ANY_MID | 0 | ↑50 | ↓1.063 | ↑21d | — | +42.5% | 61.37/59.03 | -0.59% | 20% |
| [AMBER](https://in.tradingview.com/chart/?symbol=NSE:AMBER)<br><sub>🚀SS · ↓CMF10d</sub> | ✓ SAFE | AC manufacturing and EMS for consumer appliances | 📈 BULL_ANY_MID | 59 | 🔄52 | ↑1.005 | ↑1d | — | +2.4% | -17.24/-19.21 | +2.38% | 20% |
| [MUTHOOTFIN](https://in.tradingview.com/chart/?symbol=NSE:MUTHOOTFIN)<br><sub>🚀SS · ↓CMF1d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 51 | 🔄30 | ↑1.005 | ↓9d | — | -2.4% | -40.8/-42.17 | +3.40% | 20% |
| [VIKRAMSOLR](https://in.tradingview.com/chart/?symbol=NSE:VIKRAMSOLR)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Solar PV module manufacturer, EPC services, renewable energy sector | 📈 BULL_ANY_MID | 46 | 🔄50 | ↑1.004 | ↓14d | — | -4.4% | -45.2/-45.34 | +5.21% | 20% |
| [BEL](https://in.tradingview.com/chart/?symbol=NSE:BEL)<br><sub>🚀SS · ↓CMF0d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 27 | ↓41 | ↑1.006 | ↑3d | — | +1.5% | -0.82/-6.13 | +0.71% | 20% |
| [ITC](https://in.tradingview.com/chart/?symbol=NSE:ITC)<br><sub>W↑14d · 🚀SS · ↑CMF6d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 27 | ↓7 | ↑1.002 | ↑3d | — | +1.1% | 6.95/5.11 | +0.07% | 20% |
| [TECHM](https://in.tradingview.com/chart/?symbol=NSE:TECHM)<br><sub>🚀SS · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 23 | ↓23 | ↑1.004 | ↓7d | — | -0.5% | -41.06/-43.01 | +1.64% | 20% |
| [BPCL](https://in.tradingview.com/chart/?symbol=NSE:BPCL)<br><sub>W↑14d · ↓CMF5d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 18 | ↓36 | ↓1.003 | ↑2d | — | +1.2% | 11.82/9.95 | -0.85% | 20% |
| [VBL](https://in.tradingview.com/chart/?symbol=NSE:VBL)<br><sub>🚀SS · ↓CMF10d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 16 | ↓67 | ↑1.004 | ↓14d | — | -1.2% | -13.92/-16.25 | +1.07% | 20% |
| [WIPRO](https://in.tradingview.com/chart/?symbol=NSE:WIPRO)<br><sub>🚀SS · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 10 | ↓4 | ↑1.001 | ↓32d | — | -8.5% | -44.09/-47.74 | +1.03% | 20% |
| [DEEPINDS](https://in.tradingview.com/chart/?symbol=NSE:DEEPINDS)<br><sub>🚀SS · ↓CMF8d · ⚠️TRAP</sub> | ✓ SAFE | Offshore drilling services, compression equipment, oil gas operations | 📈 BULL_ANY_MID | 6 | ↓43 | ↑0.989 | ↓19d | — | -8.3% | -48.43/-49.74 | +1.01% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>🚀SS · ↓CMF15d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓67 | ↑0.984 | ↓31d | — | -9.0% | -43.92/-44.37 | +0.45% | 20% |
| [COALINDIA](https://in.tradingview.com/chart/?symbol=NSE:COALINDIA)<br><sub>🚀SS · ↓CMF3d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 5 | ↓50 | ↑0.994 | ↓24d | — | -4.0% | -45.22/-45.43 | +0.10% | 20% |

```
NSE:ZYDUSLIFE,NSE:HAPPYFORGE,NSE:NOVARTIND,NSE:ENTERO,NSE:CCL,NSE:GLAXO,NSE:RELIGARE,NSE:NEULANDLAB,NSE:SPAL,NSE:UJJIVANSFB,NSE:SHILPAMED,NSE:AMAGI,NSE:AMBER,NSE:MUTHOOTFIN,NSE:VIKRAMSOLR,NSE:BEL,NSE:ITC,NSE:TECHM,NSE:BPCL,NSE:VBL,NSE:WIPRO,NSE:DEEPINDS,NSE:HINDALCO,NSE:COALINDIA
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
