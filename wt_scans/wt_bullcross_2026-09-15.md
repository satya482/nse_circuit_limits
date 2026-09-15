> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# WaveTrend Bull Cross Scan — 2026-09-15
*Generated 2026-09-15 15:49 IST*

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

**Total bull crosses today: 69** · 23 inside active squeeze

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MAXHEALTH,NSE:BALAJITELE,NSE:COCKERILL,NSE:RPGLIFE,NSE:OPTIEMUS,NSE:JINDALPHOT,NSE:NITTAGELA,NSE:ACMESOLAR,NSE:INDUSTOWER,NSE:FSL,NSE:MPHASIS,NSE:SHOPERSTOP,NSE:EMUDHRA,NSE:JINDALPOLY,NSE:KOPRAN,NSE:HATSUN,NSE:SIGMAADV,NSE:NIVABUPA,NSE:HINDALCO,NSE:CUPID,NSE:APLLTD,NSE:CANTABIL,NSE:KALYANKJIL,NSE:TORNTPHARM,NSE:LUMAXTECH,NSE:RUBICON,NSE:SAFARI,NSE:SANSTAR,NSE:WEWORK,NSE:HINDZINC,NSE:ADANIENT,NSE:BOSCHLTD,NSE:MEESHO,NSE:MANKIND,NSE:TATAELXSI,NSE:ZENSARTECH,NSE:FIRSTCRY,NSE:ALKEM,NSE:FDC,NSE:REDTAPE,NSE:KPITTECH,NSE:CAMS,NSE:SONATSOFTW,NSE:COLPAL,NSE:UGROCAP,NSE:CUMMINSIND,NSE:HEXT,NSE:TTKPRESTIG,NSE:FLAIR,NSE:NATCOPHARM,NSE:LATENTVIEW,NSE:RALLIS,NSE:BRIGHOTEL,NSE:HGS,NSE:TATACONSUM,NSE:GOLDIAM,NSE:SAGCEM,NSE:DELTACORP,NSE:BHARATWIRE,NSE:SANOFI,NSE:GULFOILLUB,NSE:CEATLTD,NSE:IVALUE,NSE:ZOTA,NSE:MASTEK,NSE:INDRAMEDCO,NSE:TENNIND,NSE:BETA,NSE:IZMO
```

### 📶 WEEKLY RS GATE — RS ≥ Weekly RS EMA9 (rising) vs NIFTY MIDSML 400 (33)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MAXHEALTH](https://in.tradingview.com/chart/?symbol=NSE:MAXHEALTH)<br><sub>📶W9 · ↑CMF9d</sub> | ⚠ CAUTION | Tertiary quaternary hospital network Delhi NCR North India | ⚡ BULL_ANY_PPV | 89 | 🔄36 | ↑1.030 | ↑1d | SQ·PV | +4.5% | -32.15/-41.06 | +4.48% | 20% |
| [BALAJITELE](https://in.tradingview.com/chart/?symbol=NSE:BALAJITELE)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF2d</sub> | ✓ SAFE | Hindi TV serials films digital content production streaming | ⚡ BULL_ANY_PPV | 89 | 🔄44 | ↑1.032 | ↑1d | SQ·PV | +5.3% | -1.79/-3.88 | +5.35% | 20% |
| [COCKERILL](https://in.tradingview.com/chart/?symbol=NSE:COCKERILL)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Cold rolling mill equipment for steel manufacturing | ⚡ BULL_ANY_PPV | 69 | ↑50 | ↑1.011 | ↑1d | SQ·PV | +1.2% | -6.66/-14.89 | +1.23% | 10% 🟨 |
| [RPGLIFE](https://in.tradingview.com/chart/?symbol=NSE:RPGLIFE)<br><sub>📶W9 · W↑2d · ↓CMF3d</sub> | ✓ SAFE | Pharmaceutical formulations and active ingredients manufacturer | ⚡ BULL_ANY_PPV | 61 | ↑76 | ↑1.003 | ↑9d | SQ·PV | +6.0% | 19.03/16.87 | +0.75% | 20% |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS)<br><sub>📶W9 · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | Telecom handset distribution manufacturing electronics sector | ⚡ BULL_ANY_PPV | 59 | ↑83 | ↑1.060 | ↑1d | SQ·PV | +6.8% | -9.19/-21.76 | +6.83% | 20% |
| [JINDALPHOT](https://in.tradingview.com/chart/?symbol=NSE:JINDALPHOT)<br><sub>📶W9 · W↑2d · RVOL40x · ↑CMF0d · 🎯SLING</sub> | ⚠ CAUTION | Holding company investing in photography and electronics group | ⚡ BULL_ANY_PPV | 59 | ↑34 | ↑1.066 | ↑1d | SQ·PV | +8.8% | -42.44/-58.03 | +8.77% | 20% |
| [NITTAGELA](https://in.tradingview.com/chart/?symbol=NSE:NITTAGELA)<br><sub>📶W9 · ↓CMF29d</sub> | ⚠ CAUTION | Gelatin and collagen peptides for pharma food supplements | ⚡ BULL_ANY_PPV | 58 | ↑50 | ↑1.024 | ↑7d | SQ·PV | +5.0% | 21.7/16.79 | +2.50% | 20% |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>📶W9 · W↑17d · ↑CMF20d</sub> | ✓ SAFE | Solar and wind power plants for Indian utilities | ⚡ BULL_ANY_PPV | 57 | ↑89 | ↑1.036 | ↑3d | SQ·PV | +5.8% | 38.08/36.87 | +4.50% | 20% |
| [INDUSTOWER](https://in.tradingview.com/chart/?symbol=NSE:INDUSTOWER)<br><sub>📶W9 · W↑5d · ↑CMF8d</sub> | ✓ SAFE | Telecom tower infrastructure operator serving mobile networks | ⚡ BULL_ANY_PPV | 54 | 🔄32 | ↑1.025 | ↑1d | PV | +4.3% | -30.53/-37.66 | +4.30% | 20% |
| [FSL](https://in.tradingview.com/chart/?symbol=NSE:FSL)<br><sub>📶W9 · 🚀SS·42x · ↑CMF0d</sub> | ✓ SAFE | BPM services for healthcare insurance banking finance | ⚡ BULL_ANY_PPV | 49 | 🔄55 | ↑1.084 | ↑1d | PV | +14.4% | -41.61/-50.6 | +14.44% | 20% |
| [MPHASIS](https://in.tradingview.com/chart/?symbol=NSE:MPHASIS)<br><sub>📶W9 · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | IT services, cloud and cognitive transformation, enterprise clients | ⚡ BULL_ANY_PPV | 49 | 🔄43 | ↑1.009 | ↓11d | PV | -2.0% | -32.53/-35.58 | +3.62% | 20% |
| [SHOPERSTOP](https://in.tradingview.com/chart/?symbol=NSE:SHOPERSTOP)<br><sub>📶W9 · RVOL107x · ↓CMF16d</sub> | ✓ SAFE | Department store operator, fashion beauty retail, urban consumers | ⚡ BULL_ANY_PPV | 49 | 🔄52 | ↑1.037 | ↑1d | PV | +6.1% | -20.11/-29.85 | +6.14% | 20% |
| [EMUDHRA](https://in.tradingview.com/chart/?symbol=NSE:EMUDHRA)<br><sub>📶W9 · W↑42d · 🚀SS·10x · ↑CMF27d</sub> | ✓ SAFE | Digital signatures, PKI certificates, enterprise cybersecurity India | ⚡ BULL_ANY_PPV | 49 | 🔄71 | ↑1.129 | ↑1d | PV | +20.0% | -9.81/-17.76 | +20.00% | 20% |
| [JINDALPOLY](https://in.tradingview.com/chart/?symbol=NSE:JINDALPOLY)<br><sub>📶W9 · W↑12d · RVOL16x · ↑CMF10d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 9 | ↑66 | ↑1.078 | ↑11d | PV | +16.9% | 42.52/35.93 | +9.92% | 20% |
| [KOPRAN](https://in.tradingview.com/chart/?symbol=NSE:KOPRAN)<br><sub>📶W9 · W↑17d · RVOL38x · ★ · ↓CMF1d</sub> | ✓ SAFE | APIs and formulations manufacturer serving global pharma | ⚡ BULL_ANY_PPV | 7 | ↑94 | ↑1.071 | ↑13d | PV | +29.7% | 53.17/51.75 | +6.22% | 5% |
| [HATSUN](https://in.tradingview.com/chart/?symbol=NSE:HATSUN)<br><sub>📶W9 · W↑27d · ↑CMF22d</sub> | ⚠ CAUTION | Dairy milk products manufacturing and processing company | ⚡ BULL_ANY_PPV | 1 | ↑85 | ↑1.063 | ↑19d | PV | +37.0% | 65.33/62.47 | +4.13% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [NIVABUPA](https://in.tradingview.com/chart/?symbol=NSE:NIVABUPA)<br><sub>📶W9 · ↑CMF2d · 🎯SLING</sub> | ⚠ CAUTION | Health insurance policies individuals corporates hospitals | 🟡 BULL_OS_L2 | 69 | ↑50 | ↑1.011 | ↑1d | SQ | +2.0% | -49.16/-58.28 | +1.96% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 91 | 🔄61 | ↑1.003 | ↓9d | SQ | -0.3% | -18.92/-20.04 | +1.17% | 20% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Condoms lubricants IVD kits sexual wellness global | 📈 BULL_ANY_MID | 69 | ↑100 | ↑1.015 | ↑1d | SQ | +1.6% | 22.58/16.62 | +1.57% | 20% |
| [APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Generics and APIs manufacturer serving global pharma markets | 📈 BULL_ANY_MID | 69 | ↑54 | ↑1.011 | ↑1d | SQ | +1.7% | -7.09/-11.51 | +1.70% | 20% |
| [CANTABIL](https://in.tradingview.com/chart/?symbol=NSE:CANTABIL)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Apparel design manufacturing retail through exclusive brand stores | 📈 BULL_ANY_MID | 66 | ↑46 | ↑1.001 | ↑4d | SQ | +0.6% | -9.95/-14.15 | +0.04% | 20% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>📶W9 · 🚀SS · ↓CMF22d</sub> | ✓ SAFE | Gold and studded jewellery retail across India and Middle East | 📈 BULL_ANY_MID | 64 | ↑89 | ↑1.002 | ↓6d | SQ | +2.2% | 12.35/11.89 | +0.51% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑68 | ↓0.997 | ↓2d | SQ | +0.2% | -3.46/-4.79 | -0.71% | 20% |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH)<br><sub>📶W9 · W↑32d · ↑CMF2d</sub> | ✓ SAFE | Automotive lamps, plastic parts, chassis for vehicles | 📈 BULL_ANY_MID | 57 | ↑85 | ↓1.006 | ↑3d | SQ | +2.5% | 14.23/11.19 | -0.12% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Complex generics and specialty formulations for global pharma | 📈 BULL_ANY_MID | 57 | ↑50 | ↓1.003 | ↑3d | SQ | +1.4% | 42.35/40.37 | -1.08% | 20% |
| [SAFARI](https://in.tradingview.com/chart/?symbol=NSE:SAFARI)<br><sub>📶W9 · W↑7d · ↑CMF7d</sub> | ⚠ CAUTION | Luggage and travel bags manufacturer for domestic and international consumers | 📈 BULL_ANY_MID | 57 | ↑17 | ↓1.002 | ↑3d | SQ | +2.0% | 20.85/20.24 | -0.82% | 20% |
| [SANSTAR](https://in.tradingview.com/chart/?symbol=NSE:SANSTAR)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Maize starch derivatives food animal nutrition industrial | 📈 BULL_ANY_MID | 57 | ↑64 | ↓1.010 | ↑3d | SQ | +3.1% | 2.2/-5.31 | +0.21% | 20% |
| [WEWORK](https://in.tradingview.com/chart/?symbol=NSE:WEWORK)<br><sub>📶W9 · ↓CMF28d</sub> | ⚠ CAUTION | Flexible office spaces for enterprises, startups, SMEs, India | 📈 BULL_ANY_MID | 50 | ↑50 | ↑1.001 | ↓33d | SQ | -5.2% | -34.02/-35.09 | +0.49% | 20% |
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>📶W9 · W↑28d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 28 | ↑64 | ↑1.014 | ↑2d | — | +2.7% | 24.78/23.85 | +1.56% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · ↓CMF7d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 19 | ↑77 | ↑1.039 | ↑1d | — | +5.1% | -9.05/-16.39 | +5.11% | 20% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>📶W9 · W↑109d · ↑CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.015 | ↑3d | — | +4.4% | 32.49/29.43 | +0.17% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · 🚀SS · ↑CMF29d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 0 | ↑50 | ↑1.036 | ↑24d | — | +16.7% | 57.53/55.6 | +3.13% | 20% 🟦 |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MAXHEALTH,NSE:BALAJITELE,NSE:COCKERILL,NSE:RPGLIFE,NSE:OPTIEMUS,NSE:JINDALPHOT,NSE:NITTAGELA,NSE:ACMESOLAR,NSE:INDUSTOWER,NSE:FSL,NSE:MPHASIS,NSE:SHOPERSTOP,NSE:EMUDHRA,NSE:JINDALPOLY,NSE:KOPRAN,NSE:HATSUN,NSE:SIGMAADV,NSE:NIVABUPA,NSE:HINDALCO,NSE:CUPID,NSE:APLLTD,NSE:CANTABIL,NSE:KALYANKJIL,NSE:TORNTPHARM,NSE:LUMAXTECH,NSE:RUBICON,NSE:SAFARI,NSE:SANSTAR,NSE:WEWORK,NSE:HINDZINC,NSE:ADANIENT,NSE:BOSCHLTD,NSE:MEESHO
```

---

### 📶 RS-CONFIRMED — RS strong (↑) or transitioning (🔄) vs NIFTY MIDSML 400 (64)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MAXHEALTH](https://in.tradingview.com/chart/?symbol=NSE:MAXHEALTH)<br><sub>📶W9 · ↑CMF9d</sub> | ⚠ CAUTION | Tertiary quaternary hospital network Delhi NCR North India | ⚡ BULL_ANY_PPV | 89 | 🔄36 | ↑1.030 | ↑1d | SQ·PV | +4.5% | -32.15/-41.06 | +4.48% | 20% |
| [BALAJITELE](https://in.tradingview.com/chart/?symbol=NSE:BALAJITELE)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF2d</sub> | ✓ SAFE | Hindi TV serials films digital content production streaming | ⚡ BULL_ANY_PPV | 89 | 🔄44 | ↑1.032 | ↑1d | SQ·PV | +5.3% | -1.79/-3.88 | +5.35% | 20% |
| [COCKERILL](https://in.tradingview.com/chart/?symbol=NSE:COCKERILL)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Cold rolling mill equipment for steel manufacturing | ⚡ BULL_ANY_PPV | 69 | ↑50 | ↑1.011 | ↑1d | SQ·PV | +1.2% | -6.66/-14.89 | +1.23% | 10% 🟨 |
| [RPGLIFE](https://in.tradingview.com/chart/?symbol=NSE:RPGLIFE)<br><sub>📶W9 · W↑2d · ↓CMF3d</sub> | ✓ SAFE | Pharmaceutical formulations and active ingredients manufacturer | ⚡ BULL_ANY_PPV | 61 | ↑76 | ↑1.003 | ↑9d | SQ·PV | +6.0% | 19.03/16.87 | +0.75% | 20% |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS)<br><sub>📶W9 · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | Telecom handset distribution manufacturing electronics sector | ⚡ BULL_ANY_PPV | 59 | ↑83 | ↑1.060 | ↑1d | SQ·PV | +6.8% | -9.19/-21.76 | +6.83% | 20% |
| [JINDALPHOT](https://in.tradingview.com/chart/?symbol=NSE:JINDALPHOT)<br><sub>📶W9 · W↑2d · RVOL40x · ↑CMF0d · 🎯SLING</sub> | ⚠ CAUTION | Holding company investing in photography and electronics group | ⚡ BULL_ANY_PPV | 59 | ↑34 | ↑1.066 | ↑1d | SQ·PV | +8.8% | -42.44/-58.03 | +8.77% | 20% |
| [NITTAGELA](https://in.tradingview.com/chart/?symbol=NSE:NITTAGELA)<br><sub>📶W9 · ↓CMF29d</sub> | ⚠ CAUTION | Gelatin and collagen peptides for pharma food supplements | ⚡ BULL_ANY_PPV | 58 | ↑50 | ↑1.024 | ↑7d | SQ·PV | +5.0% | 21.7/16.79 | +2.50% | 20% |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>📶W9 · W↑17d · ↑CMF20d</sub> | ✓ SAFE | Solar and wind power plants for Indian utilities | ⚡ BULL_ANY_PPV | 57 | ↑89 | ↑1.036 | ↑3d | SQ·PV | +5.8% | 38.08/36.87 | +4.50% | 20% |
| [INDUSTOWER](https://in.tradingview.com/chart/?symbol=NSE:INDUSTOWER)<br><sub>📶W9 · W↑5d · ↑CMF8d</sub> | ✓ SAFE | Telecom tower infrastructure operator serving mobile networks | ⚡ BULL_ANY_PPV | 54 | 🔄32 | ↑1.025 | ↑1d | PV | +4.3% | -30.53/-37.66 | +4.30% | 20% |
| [FSL](https://in.tradingview.com/chart/?symbol=NSE:FSL)<br><sub>📶W9 · 🚀SS·42x · ↑CMF0d</sub> | ✓ SAFE | BPM services for healthcare insurance banking finance | ⚡ BULL_ANY_PPV | 49 | 🔄55 | ↑1.084 | ↑1d | PV | +14.4% | -41.61/-50.6 | +14.44% | 20% |
| [MPHASIS](https://in.tradingview.com/chart/?symbol=NSE:MPHASIS)<br><sub>📶W9 · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | IT services, cloud and cognitive transformation, enterprise clients | ⚡ BULL_ANY_PPV | 49 | 🔄43 | ↑1.009 | ↓11d | PV | -2.0% | -32.53/-35.58 | +3.62% | 20% |
| [SHOPERSTOP](https://in.tradingview.com/chart/?symbol=NSE:SHOPERSTOP)<br><sub>📶W9 · RVOL107x · ↓CMF16d</sub> | ✓ SAFE | Department store operator, fashion beauty retail, urban consumers | ⚡ BULL_ANY_PPV | 49 | 🔄52 | ↑1.037 | ↑1d | PV | +6.1% | -20.11/-29.85 | +6.14% | 20% |
| [EMUDHRA](https://in.tradingview.com/chart/?symbol=NSE:EMUDHRA)<br><sub>📶W9 · W↑42d · 🚀SS·10x · ↑CMF27d</sub> | ✓ SAFE | Digital signatures, PKI certificates, enterprise cybersecurity India | ⚡ BULL_ANY_PPV | 49 | 🔄71 | ↑1.129 | ↑1d | PV | +20.0% | -9.81/-17.76 | +20.00% | 20% |
| [JINDALPOLY](https://in.tradingview.com/chart/?symbol=NSE:JINDALPOLY)<br><sub>📶W9 · W↑12d · RVOL16x · ↑CMF10d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 9 | ↑66 | ↑1.078 | ↑11d | PV | +16.9% | 42.52/35.93 | +9.92% | 20% |
| [KOPRAN](https://in.tradingview.com/chart/?symbol=NSE:KOPRAN)<br><sub>📶W9 · W↑17d · RVOL38x · ★ · ↓CMF1d</sub> | ✓ SAFE | APIs and formulations manufacturer serving global pharma | ⚡ BULL_ANY_PPV | 7 | ↑94 | ↑1.071 | ↑13d | PV | +29.7% | 53.17/51.75 | +6.22% | 5% |
| [HATSUN](https://in.tradingview.com/chart/?symbol=NSE:HATSUN)<br><sub>📶W9 · W↑27d · ↑CMF22d</sub> | ⚠ CAUTION | Dairy milk products manufacturing and processing company | ⚡ BULL_ANY_PPV | 1 | ↑85 | ↑1.063 | ↑19d | PV | +37.0% | 65.33/62.47 | +4.13% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [NIVABUPA](https://in.tradingview.com/chart/?symbol=NSE:NIVABUPA)<br><sub>📶W9 · ↑CMF2d · 🎯SLING</sub> | ⚠ CAUTION | Health insurance policies individuals corporates hospitals | 🟡 BULL_OS_L2 | 69 | ↑50 | ↑1.011 | ↑1d | SQ | +2.0% | -49.16/-58.28 | +1.96% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 91 | 🔄61 | ↑1.003 | ↓9d | SQ | -0.3% | -18.92/-20.04 | +1.17% | 20% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Condoms lubricants IVD kits sexual wellness global | 📈 BULL_ANY_MID | 69 | ↑100 | ↑1.015 | ↑1d | SQ | +1.6% | 22.58/16.62 | +1.57% | 20% |
| [APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Generics and APIs manufacturer serving global pharma markets | 📈 BULL_ANY_MID | 69 | ↑54 | ↑1.011 | ↑1d | SQ | +1.7% | -7.09/-11.51 | +1.70% | 20% |
| [CANTABIL](https://in.tradingview.com/chart/?symbol=NSE:CANTABIL)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Apparel design manufacturing retail through exclusive brand stores | 📈 BULL_ANY_MID | 66 | ↑46 | ↑1.001 | ↑4d | SQ | +0.6% | -9.95/-14.15 | +0.04% | 20% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>📶W9 · 🚀SS · ↓CMF22d</sub> | ✓ SAFE | Gold and studded jewellery retail across India and Middle East | 📈 BULL_ANY_MID | 64 | ↑89 | ↑1.002 | ↓6d | SQ | +2.2% | 12.35/11.89 | +0.51% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑68 | ↓0.997 | ↓2d | SQ | +0.2% | -3.46/-4.79 | -0.71% | 20% |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH)<br><sub>📶W9 · W↑32d · ↑CMF2d</sub> | ✓ SAFE | Automotive lamps, plastic parts, chassis for vehicles | 📈 BULL_ANY_MID | 57 | ↑85 | ↓1.006 | ↑3d | SQ | +2.5% | 14.23/11.19 | -0.12% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Complex generics and specialty formulations for global pharma | 📈 BULL_ANY_MID | 57 | ↑50 | ↓1.003 | ↑3d | SQ | +1.4% | 42.35/40.37 | -1.08% | 20% |
| [SAFARI](https://in.tradingview.com/chart/?symbol=NSE:SAFARI)<br><sub>📶W9 · W↑7d · ↑CMF7d</sub> | ⚠ CAUTION | Luggage and travel bags manufacturer for domestic and international consumers | 📈 BULL_ANY_MID | 57 | ↑17 | ↓1.002 | ↑3d | SQ | +2.0% | 20.85/20.24 | -0.82% | 20% |
| [SANSTAR](https://in.tradingview.com/chart/?symbol=NSE:SANSTAR)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Maize starch derivatives food animal nutrition industrial | 📈 BULL_ANY_MID | 57 | ↑64 | ↓1.010 | ↑3d | SQ | +3.1% | 2.2/-5.31 | +0.21% | 20% |
| [WEWORK](https://in.tradingview.com/chart/?symbol=NSE:WEWORK)<br><sub>📶W9 · ↓CMF28d</sub> | ⚠ CAUTION | Flexible office spaces for enterprises, startups, SMEs, India | 📈 BULL_ANY_MID | 50 | ↑50 | ↑1.001 | ↓33d | SQ | -5.2% | -34.02/-35.09 | +0.49% | 20% |
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>📶W9 · W↑28d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 28 | ↑64 | ↑1.014 | ↑2d | — | +2.7% | 24.78/23.85 | +1.56% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · ↓CMF7d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 19 | ↑77 | ↑1.039 | ↑1d | — | +5.1% | -9.05/-16.39 | +5.11% | 20% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>📶W9 · W↑109d · ↑CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.015 | ↑3d | — | +4.4% | 32.49/29.43 | +0.17% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · 🚀SS · ↑CMF29d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 0 | ↑50 | ↑1.036 | ↑24d | — | +16.7% | 57.53/55.6 | +3.13% | 20% 🟦 |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>↑CMF2d · 🎯SLING</sub> | ⚠ CAUTION | Pharma formulations acute chronic diseases consumer healthcare | 🔥 BULL_OS_PPV | 43 | 🔄42 | ↑0.990 | ↓12d | PV | -4.3% | -63.38/-65.27 | +0.02% | 20% |
| [TATAELXSI](https://in.tradingview.com/chart/?symbol=NSE:TATAELXSI)<br><sub>🚀SS · ↓CMF17d · 🎯SLING</sub> | ✓ SAFE | Design engineering services for automotive media healthcare | 🔥 BULL_OS_PPV | 42 | 🔄6 | ↑0.992 | ↓13d | PV | -5.3% | -63.02/-66.29 | +1.68% | 20% |
| [ZENSARTECH](https://in.tradingview.com/chart/?symbol=NSE:ZENSARTECH)<br><sub>🚀SS·60x · ↓CMF26d · 🎯SLING</sub> | ✓ SAFE | Digital solutions and IT services for global enterprises | 🔥 BULL_OS_PPV | 35 | 🔄8 | ↑0.994 | ↓32d | PV | -13.3% | -64.58/-69.77 | +3.52% | 20% |
| [FIRSTCRY](https://in.tradingview.com/chart/?symbol=NSE:FIRSTCRY)<br><sub>RVOL28x · ↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Mothers babies kids products e-commerce retail platform | 🔥 BULL_OS_PPV | 35 | 🔄2 | ↑0.983 | ↓26d | PV | -19.4% | -57.2/-61.69 | +1.60% | 20% |
| [ALKEM](https://in.tradingview.com/chart/?symbol=NSE:ALKEM)<br><sub>🚀SS · ↓CMF4d · 🎯SLING</sub> | ⚠ CAUTION | Pharma manufacturer generic drugs domestic international markets | 🔥 BULL_OS_PPV | 35 | 🔄39 | ↑0.998 | ↓30d | PV | -8.0% | -56.0/-60.49 | +1.44% | 20% |
| [FDC](https://in.tradingview.com/chart/?symbol=NSE:FDC)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Pharma APIs formulations domestic India manufacturing | ⚡ BULL_ANY_PPV | 99 | 🔄24 | ↑1.013 | ↑1d | SQ·PV | +2.4% | -18.7/-22.35 | +2.42% | 20% |
| [REDTAPE](https://in.tradingview.com/chart/?symbol=NSE:REDTAPE)<br><sub>RVOL113x · ↓CMF30d</sub> | ✓ SAFE | Footwear apparel accessories omnichannel retail men women kids | ⚡ BULL_ANY_PPV | 54 | 🔄35 | ↑1.021 | ↑1d | PV | +4.1% | -42.83/-52.01 | +4.11% | 20% |
| [KPITTECH](https://in.tradingview.com/chart/?symbol=NSE:KPITTECH)<br><sub>🚀SS · ↓CMF11d · 🎯SLING</sub> | ✓ SAFE | Automotive software, embedded systems, SDV development | ⚡ BULL_ANY_PPV | 42 | 🔄2 | ↑0.997 | ↓13d | PV | -4.2% | -52.74/-57.1 | +1.67% | 20% |
| [CAMS](https://in.tradingview.com/chart/?symbol=NSE:CAMS)<br><sub>🚀SS · ↑CMF9d · 🎯SLING</sub> | ✓ SAFE | Mutual fund registry, transfer agent, investor servicing platform | ⚡ BULL_ANY_PPV | 42 | 🔄38 | ↑0.989 | ↓13d | PV | -3.2% | -58.18/-59.42 | +0.89% | 20% |
| [SONATSOFTW](https://in.tradingview.com/chart/?symbol=NSE:SONATSOFTW)<br><sub>🚀SS · ↓CMF11d · 🎯SLING</sub> | ✓ SAFE | IT services, cloud modernization, enterprise digital transformation | ⚡ BULL_ANY_PPV | 35 | 🔄33 | ↑1.017 | ↓36d | PV | -4.1% | -53.91/-59.84 | +5.81% | 20% |
| [COLPAL](https://in.tradingview.com/chart/?symbol=NSE:COLPAL)<br><sub>↑CMF0d · 🎯SLING</sub> | ⚠ CAUTION | Toothpaste, toothbrush, mouthwash maker for mass consumers | ⚡ BULL_ANY_PPV | 35 | 🔄23 | ↑0.999 | ↓43d | PV | -9.0% | -52.14/-55.34 | +1.27% | 20% |
| [UGROCAP](https://in.tradingview.com/chart/?symbol=NSE:UGROCAP)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | MSME lending platform, technology-driven credit scoring | 🟢 BULL_OVERSOLD | 70 | 🔄3 | ↓0.986 | ↓27d | SQ | -12.4% | -57.39/-60.09 | -0.45% | 20% |
| [CUMMINSIND](https://in.tradingview.com/chart/?symbol=NSE:CUMMINSIND)<br><sub>↑CMF1d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 59 | 🔄53 | ↑1.012 | ↑1d | — | +2.7% | -56.42/-62.44 | +2.68% | 20% |
| [HEXT](https://in.tradingview.com/chart/?symbol=NSE:HEXT)<br><sub>🚀SS · ↑CMF12d · 🎯SLING</sub> | ✓ SAFE | IT services, digital transformation, automation, enterprise clients | 🟢 BULL_OVERSOLD | 43 | 🔄36 | ↑1.001 | ↓17d | — | -2.8% | -66.27/-69.3 | +4.11% | 20% |
| [TTKPRESTIG](https://in.tradingview.com/chart/?symbol=NSE:TTKPRESTIG)<br><sub>↓CMF15d · 🎯SLING</sub> | ⚠ CAUTION | Pressure cookers, cookware, kitchen appliances for households | 🟢 BULL_OVERSOLD | 40 | 🔄39 | ↑0.979 | ↓15d | — | -9.3% | -61.33/-62.1 | +0.50% | 20% |
| [FLAIR](https://in.tradingview.com/chart/?symbol=NSE:FLAIR)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Ball pen manufacturer for retail consumer stationery market | 🟢 BULL_OVERSOLD | 39 | 🔄9 | ↓0.976 | ↓11d | — | -6.0% | -75.23/-75.76 | -1.00% | 20% |
| [NATCOPHARM](https://in.tradingview.com/chart/?symbol=NSE:NATCOPHARM)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Generic oncology drugs, complex formulations, global pharma markets | 🟢 BULL_OVERSOLD | 35 | 🔄31 | ↑0.989 | ↓24d | — | -10.5% | -60.98/-62.76 | +0.47% | 20% |
| [LATENTVIEW](https://in.tradingview.com/chart/?symbol=NSE:LATENTVIEW)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Data analytics consulting, marketing optimization, enterprise clients | 🟢 BULL_OVERSOLD | 35 | 🔄4 | ↑0.975 | ↓37d | — | -14.6% | -63.79/-65.11 | +0.18% | 20% |
| [RALLIS](https://in.tradingview.com/chart/?symbol=NSE:RALLIS)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Agrochemicals, seeds, crop nutrients for Indian farmers | 🟢 BULL_OVERSOLD | 35 | 🔄9 | ↓0.982 | ↓15d | — | -5.7% | -67.26/-67.48 | -0.58% | 20% |
| [BRIGHOTEL](https://in.tradingview.com/chart/?symbol=NSE:BRIGHOTEL)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 35 | 🔄15 | ↓0.982 | ↓15d | — | -5.4% | -67.84/-68.22 | -0.65% | 20% |
| [HGS](https://in.tradingview.com/chart/?symbol=NSE:HGS)<br><sub>↓CMF25d · 🎯SLING</sub> | ⚠ CAUTION | Customer experience BPM services, global contact center operations | 🟢 BULL_OVERSOLD | 35 | 🔄24 | ↑0.985 | ↓28d | — | -9.8% | -67.54/-68.14 | +0.04% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 30 | 🔄24 | ↓0.981 | ↓24d | — | -7.1% | -68.61/-69.84 | -0.49% | 20% |
| [SANOFI](https://in.tradingview.com/chart/?symbol=NSE:SANOFI)<br><sub>↓CMF15d · 🎯SLING</sub> | ⚠ CAUTION | Pharmaceutical diabetes cardiology CNS medicines India | 🟡 BULL_OS_L2 | 41 | 🔄15 | ↑1.002 | ↓19d | — | -4.3% | -55.31/-58.1 | +1.68% | 20% |
| [GULFOILLUB](https://in.tradingview.com/chart/?symbol=NSE:GULFOILLUB)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Automotive lubricants manufacturing distribution Indian commercial vehicles | 🟡 BULL_OS_L2 | 38 | 🔄43 | ↑0.981 | ↓17d | — | -7.2% | -52.79/-53.01 | -0.32% | 20% |
| [CEATLTD](https://in.tradingview.com/chart/?symbol=NSE:CEATLTD)<br><sub>↓CMF11d · 🎯SLING</sub> | ⚠ CAUTION | Radial and bias tyres for two-wheelers, cars, trucks | 🟡 BULL_OS_L2 | 35 | 🔄38 | ↑0.987 | ↓32d | — | -4.3% | -52.73/-53.79 | +0.12% | 20% |
| [ZOTA](https://in.tradingview.com/chart/?symbol=NSE:ZOTA)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Pharma manufacturer: tablets, syrups, Ayurveda, OTC products | 📈 BULL_ANY_MID | 99 | 🔄13 | ↑1.013 | ↑1d | SQ | +2.4% | -18.62/-22.83 | +2.38% | 20% |
| [MASTEK](https://in.tradingview.com/chart/?symbol=NSE:MASTEK)<br><sub>🚀SS · ↑CMF12d</sub> | ✓ SAFE | Digital engineering, Oracle Cloud, enterprise transformation | 📈 BULL_ANY_MID | 44 | 🔄33 | ↑0.991 | ↓11d | — | -5.5% | -33.85/-34.94 | +1.59% | 20% |
| [INDRAMEDCO](https://in.tradingview.com/chart/?symbol=NSE:INDRAMEDCO)<br><sub>↓CMF30d</sub> | ✓ SAFE | Tertiary care hospital, multi-specialty, Delhi-based healthcare | 📈 BULL_ANY_MID | 39 | 🔄17 | ↑0.993 | ↓16d | — | -4.7% | -49.42/-50.78 | -0.13% | 20% |
| [TENNIND](https://in.tradingview.com/chart/?symbol=NSE:TENNIND)<br><sub>🚀SS · ↑CMF29d</sub> | ✓ SAFE | Automotive emissions control systems supplier for passenger vehicles | 📈 BULL_ANY_MID | 35 | 🔄50 | ↑0.991 | ↓22d | — | -5.3% | -43.81/-44.28 | +1.29% | 20% |
| [BETA](https://in.tradingview.com/chart/?symbol=NSE:BETA)<br><sub>↓CMF30d</sub> | ✓ SAFE | Oncology drug manufacturer for cancer treatment domestic export | 📈 BULL_ANY_MID | 30 | 🔄80 | ↓0.982 | ↓32d | — | -5.7% | -43.29/-44.57 | -0.63% | 20% |
| [IZMO](https://in.tradingview.com/chart/?symbol=NSE:IZMO)<br><sub>↓CMF30d</sub> | ✓ SAFE | Automotive digital retail and marketing technology solutions | 📈 BULL_ANY_MID | 17 | ↑48 | ↓0.992 | ↓3d | — | -0.5% | -6.28/-7.15 | -1.19% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MAXHEALTH,NSE:BALAJITELE,NSE:COCKERILL,NSE:RPGLIFE,NSE:OPTIEMUS,NSE:JINDALPHOT,NSE:NITTAGELA,NSE:ACMESOLAR,NSE:INDUSTOWER,NSE:FSL,NSE:MPHASIS,NSE:SHOPERSTOP,NSE:EMUDHRA,NSE:JINDALPOLY,NSE:KOPRAN,NSE:HATSUN,NSE:SIGMAADV,NSE:NIVABUPA,NSE:HINDALCO,NSE:CUPID,NSE:APLLTD,NSE:CANTABIL,NSE:KALYANKJIL,NSE:TORNTPHARM,NSE:LUMAXTECH,NSE:RUBICON,NSE:SAFARI,NSE:SANSTAR,NSE:WEWORK,NSE:HINDZINC,NSE:ADANIENT,NSE:BOSCHLTD,NSE:MEESHO,NSE:MANKIND,NSE:TATAELXSI,NSE:ZENSARTECH,NSE:FIRSTCRY,NSE:ALKEM,NSE:FDC,NSE:REDTAPE,NSE:KPITTECH,NSE:CAMS,NSE:SONATSOFTW,NSE:COLPAL,NSE:UGROCAP,NSE:CUMMINSIND,NSE:HEXT,NSE:TTKPRESTIG,NSE:FLAIR,NSE:NATCOPHARM,NSE:LATENTVIEW,NSE:RALLIS,NSE:BRIGHOTEL,NSE:HGS,NSE:TATACONSUM,NSE:SANOFI,NSE:GULFOILLUB,NSE:CEATLTD,NSE:ZOTA,NSE:MASTEK,NSE:INDRAMEDCO,NSE:TENNIND,NSE:BETA,NSE:IZMO
```

---

### 🎯 SQUEEZE BREAKOUT — WT cross inside active BB-KC squeeze (23)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [MAXHEALTH](https://in.tradingview.com/chart/?symbol=NSE:MAXHEALTH)<br><sub>📶W9 · ↑CMF9d</sub> | ⚠ CAUTION | Tertiary quaternary hospital network Delhi NCR North India | ⚡ BULL_ANY_PPV | 89 | 🔄36 | ↑1.030 | ↑1d | SQ·PV | +4.5% | -32.15/-41.06 | +4.48% | 20% |
| [BALAJITELE](https://in.tradingview.com/chart/?symbol=NSE:BALAJITELE)<br><sub>📶W9 · W↑27d · 🚀SS · ↑CMF2d</sub> | ✓ SAFE | Hindi TV serials films digital content production streaming | ⚡ BULL_ANY_PPV | 89 | 🔄44 | ↑1.032 | ↑1d | SQ·PV | +5.3% | -1.79/-3.88 | +5.35% | 20% |
| [COCKERILL](https://in.tradingview.com/chart/?symbol=NSE:COCKERILL)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Cold rolling mill equipment for steel manufacturing | ⚡ BULL_ANY_PPV | 69 | ↑50 | ↑1.011 | ↑1d | SQ·PV | +1.2% | -6.66/-14.89 | +1.23% | 10% 🟨 |
| [RPGLIFE](https://in.tradingview.com/chart/?symbol=NSE:RPGLIFE)<br><sub>📶W9 · W↑2d · ↓CMF3d</sub> | ✓ SAFE | Pharmaceutical formulations and active ingredients manufacturer | ⚡ BULL_ANY_PPV | 61 | ↑76 | ↑1.003 | ↑9d | SQ·PV | +6.0% | 19.03/16.87 | +0.75% | 20% |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS)<br><sub>📶W9 · 🚀SS · ↑CMF9d</sub> | ✓ SAFE | Telecom handset distribution manufacturing electronics sector | ⚡ BULL_ANY_PPV | 59 | ↑83 | ↑1.060 | ↑1d | SQ·PV | +6.8% | -9.19/-21.76 | +6.83% | 20% |
| [JINDALPHOT](https://in.tradingview.com/chart/?symbol=NSE:JINDALPHOT)<br><sub>📶W9 · W↑2d · RVOL40x · ↑CMF0d · 🎯SLING</sub> | ⚠ CAUTION | Holding company investing in photography and electronics group | ⚡ BULL_ANY_PPV | 59 | ↑34 | ↑1.066 | ↑1d | SQ·PV | +8.8% | -42.44/-58.03 | +8.77% | 20% |
| [NITTAGELA](https://in.tradingview.com/chart/?symbol=NSE:NITTAGELA)<br><sub>📶W9 · ↓CMF29d</sub> | ⚠ CAUTION | Gelatin and collagen peptides for pharma food supplements | ⚡ BULL_ANY_PPV | 58 | ↑50 | ↑1.024 | ↑7d | SQ·PV | +5.0% | 21.7/16.79 | +2.50% | 20% |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>📶W9 · W↑17d · ↑CMF20d</sub> | ✓ SAFE | Solar and wind power plants for Indian utilities | ⚡ BULL_ANY_PPV | 57 | ↑89 | ↑1.036 | ↑3d | SQ·PV | +5.8% | 38.08/36.87 | +4.50% | 20% |
| [NIVABUPA](https://in.tradingview.com/chart/?symbol=NSE:NIVABUPA)<br><sub>📶W9 · ↑CMF2d · 🎯SLING</sub> | ⚠ CAUTION | Health insurance policies individuals corporates hospitals | 🟡 BULL_OS_L2 | 69 | ↑50 | ↑1.011 | ↑1d | SQ | +2.0% | -49.16/-58.28 | +1.96% | 20% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>📶W9 · 🚀SS · ↓CMF0d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 91 | 🔄61 | ↑1.003 | ↓9d | SQ | -0.3% | -18.92/-20.04 | +1.17% | 20% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>📶W9 · 🚀SS · ↑CMF30d</sub> | ✓ SAFE | Condoms lubricants IVD kits sexual wellness global | 📈 BULL_ANY_MID | 69 | ↑100 | ↑1.015 | ↑1d | SQ | +1.6% | 22.58/16.62 | +1.57% | 20% |
| [APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD)<br><sub>📶W9 · 🚀SS · ↓CMF30d</sub> | ⚠ CAUTION | Generics and APIs manufacturer serving global pharma markets | 📈 BULL_ANY_MID | 69 | ↑54 | ↑1.011 | ↑1d | SQ | +1.7% | -7.09/-11.51 | +1.70% | 20% |
| [CANTABIL](https://in.tradingview.com/chart/?symbol=NSE:CANTABIL)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Apparel design manufacturing retail through exclusive brand stores | 📈 BULL_ANY_MID | 66 | ↑46 | ↑1.001 | ↑4d | SQ | +0.6% | -9.95/-14.15 | +0.04% | 20% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>📶W9 · 🚀SS · ↓CMF22d</sub> | ✓ SAFE | Gold and studded jewellery retail across India and Middle East | 📈 BULL_ANY_MID | 64 | ↑89 | ↑1.002 | ↓6d | SQ | +2.2% | 12.35/11.89 | +0.51% | 20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>📶W9 · ↑CMF11d</sub> | ⚠ CAUTION |  | 📈 BULL_ANY_MID | 58 | ↑68 | ↓0.997 | ↓2d | SQ | +0.2% | -3.46/-4.79 | -0.71% | 20% |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH)<br><sub>📶W9 · W↑32d · ↑CMF2d</sub> | ✓ SAFE | Automotive lamps, plastic parts, chassis for vehicles | 📈 BULL_ANY_MID | 57 | ↑85 | ↓1.006 | ↑3d | SQ | +2.5% | 14.23/11.19 | -0.12% | 20% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>📶W9 · ↑CMF30d</sub> | ✓ SAFE | Complex generics and specialty formulations for global pharma | 📈 BULL_ANY_MID | 57 | ↑50 | ↓1.003 | ↑3d | SQ | +1.4% | 42.35/40.37 | -1.08% | 20% |
| [SAFARI](https://in.tradingview.com/chart/?symbol=NSE:SAFARI)<br><sub>📶W9 · W↑7d · ↑CMF7d</sub> | ⚠ CAUTION | Luggage and travel bags manufacturer for domestic and international consumers | 📈 BULL_ANY_MID | 57 | ↑17 | ↓1.002 | ↑3d | SQ | +2.0% | 20.85/20.24 | -0.82% | 20% |
| [SANSTAR](https://in.tradingview.com/chart/?symbol=NSE:SANSTAR)<br><sub>📶W9 · ↓CMF30d</sub> | ✓ SAFE | Maize starch derivatives food animal nutrition industrial | 📈 BULL_ANY_MID | 57 | ↑64 | ↓1.010 | ↑3d | SQ | +3.1% | 2.2/-5.31 | +0.21% | 20% |
| [WEWORK](https://in.tradingview.com/chart/?symbol=NSE:WEWORK)<br><sub>📶W9 · ↓CMF28d</sub> | ⚠ CAUTION | Flexible office spaces for enterprises, startups, SMEs, India | 📈 BULL_ANY_MID | 50 | ↑50 | ↑1.001 | ↓33d | SQ | -5.2% | -34.02/-35.09 | +0.49% | 20% |
| [FDC](https://in.tradingview.com/chart/?symbol=NSE:FDC)<br><sub>↓CMF30d</sub> | ⚠ CAUTION | Pharma APIs formulations domestic India manufacturing | ⚡ BULL_ANY_PPV | 99 | 🔄24 | ↑1.013 | ↑1d | SQ·PV | +2.4% | -18.7/-22.35 | +2.42% | 20% |
| [UGROCAP](https://in.tradingview.com/chart/?symbol=NSE:UGROCAP)<br><sub>↓CMF30d · 🎯SLING · ÷DIV</sub> | ⚠ CAUTION | MSME lending platform, technology-driven credit scoring | 🟢 BULL_OVERSOLD | 70 | 🔄3 | ↓0.986 | ↓27d | SQ | -12.4% | -57.39/-60.09 | -0.45% | 20% |
| [ZOTA](https://in.tradingview.com/chart/?symbol=NSE:ZOTA)<br><sub>🚀SS · ↓CMF30d</sub> | ✓ SAFE | Pharma manufacturer: tablets, syrups, Ayurveda, OTC products | 📈 BULL_ANY_MID | 99 | 🔄13 | ↑1.013 | ↑1d | SQ | +2.4% | -18.62/-22.83 | +2.38% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MAXHEALTH,NSE:BALAJITELE,NSE:COCKERILL,NSE:RPGLIFE,NSE:OPTIEMUS,NSE:JINDALPHOT,NSE:NITTAGELA,NSE:ACMESOLAR,NSE:NIVABUPA,NSE:HINDALCO,NSE:CUPID,NSE:APLLTD,NSE:CANTABIL,NSE:KALYANKJIL,NSE:TORNTPHARM,NSE:LUMAXTECH,NSE:RUBICON,NSE:SAFARI,NSE:SANSTAR,NSE:WEWORK,NSE:FDC,NSE:UGROCAP,NSE:ZOTA
```

---

### 🔥 MAJOR — PPV confirmed (19)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [INDUSTOWER](https://in.tradingview.com/chart/?symbol=NSE:INDUSTOWER)<br><sub>📶W9 · W↑5d · ↑CMF8d</sub> | ✓ SAFE | Telecom tower infrastructure operator serving mobile networks | ⚡ BULL_ANY_PPV | 54 | 🔄32 | ↑1.025 | ↑1d | PV | +4.3% | -30.53/-37.66 | +4.30% | 20% |
| [FSL](https://in.tradingview.com/chart/?symbol=NSE:FSL)<br><sub>📶W9 · 🚀SS·42x · ↑CMF0d</sub> | ✓ SAFE | BPM services for healthcare insurance banking finance | ⚡ BULL_ANY_PPV | 49 | 🔄55 | ↑1.084 | ↑1d | PV | +14.4% | -41.61/-50.6 | +14.44% | 20% |
| [MPHASIS](https://in.tradingview.com/chart/?symbol=NSE:MPHASIS)<br><sub>📶W9 · 🚀SS · ↓CMF3d</sub> | ✓ SAFE | IT services, cloud and cognitive transformation, enterprise clients | ⚡ BULL_ANY_PPV | 49 | 🔄43 | ↑1.009 | ↓11d | PV | -2.0% | -32.53/-35.58 | +3.62% | 20% |
| [SHOPERSTOP](https://in.tradingview.com/chart/?symbol=NSE:SHOPERSTOP)<br><sub>📶W9 · RVOL107x · ↓CMF16d</sub> | ✓ SAFE | Department store operator, fashion beauty retail, urban consumers | ⚡ BULL_ANY_PPV | 49 | 🔄52 | ↑1.037 | ↑1d | PV | +6.1% | -20.11/-29.85 | +6.14% | 20% |
| [EMUDHRA](https://in.tradingview.com/chart/?symbol=NSE:EMUDHRA)<br><sub>📶W9 · W↑42d · 🚀SS·10x · ↑CMF27d</sub> | ✓ SAFE | Digital signatures, PKI certificates, enterprise cybersecurity India | ⚡ BULL_ANY_PPV | 49 | 🔄71 | ↑1.129 | ↑1d | PV | +20.0% | -9.81/-17.76 | +20.00% | 20% |
| [JINDALPOLY](https://in.tradingview.com/chart/?symbol=NSE:JINDALPOLY)<br><sub>📶W9 · W↑12d · RVOL16x · ↑CMF10d</sub> | ✓ SAFE |  | ⚡ BULL_ANY_PPV | 9 | ↑66 | ↑1.078 | ↑11d | PV | +16.9% | 42.52/35.93 | +9.92% | 20% |
| [KOPRAN](https://in.tradingview.com/chart/?symbol=NSE:KOPRAN)<br><sub>📶W9 · W↑17d · RVOL38x · ★ · ↓CMF1d</sub> | ✓ SAFE | APIs and formulations manufacturer serving global pharma | ⚡ BULL_ANY_PPV | 7 | ↑94 | ↑1.071 | ↑13d | PV | +29.7% | 53.17/51.75 | +6.22% | 5% |
| [HATSUN](https://in.tradingview.com/chart/?symbol=NSE:HATSUN)<br><sub>📶W9 · W↑27d · ↑CMF22d</sub> | ⚠ CAUTION | Dairy milk products manufacturing and processing company | ⚡ BULL_ANY_PPV | 1 | ↑85 | ↑1.063 | ↑19d | PV | +37.0% | 65.33/62.47 | +4.13% | 20% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>📶W9 · W↑59d · 🚀SS · ↑CMF0d</sub> | ✓ SAFE | Aerospace defense electronics manufacturing for global OEMs | ⚡ BULL_ANY_PPV | 0 | ↑100 | ↑1.130 | ↑58d | PV | +387.9% | 70.19/69.53 | +5.00% | 20% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>↑CMF2d · 🎯SLING</sub> | ⚠ CAUTION | Pharma formulations acute chronic diseases consumer healthcare | 🔥 BULL_OS_PPV | 43 | 🔄42 | ↑0.990 | ↓12d | PV | -4.3% | -63.38/-65.27 | +0.02% | 20% |
| [TATAELXSI](https://in.tradingview.com/chart/?symbol=NSE:TATAELXSI)<br><sub>🚀SS · ↓CMF17d · 🎯SLING</sub> | ✓ SAFE | Design engineering services for automotive media healthcare | 🔥 BULL_OS_PPV | 42 | 🔄6 | ↑0.992 | ↓13d | PV | -5.3% | -63.02/-66.29 | +1.68% | 20% |
| [ZENSARTECH](https://in.tradingview.com/chart/?symbol=NSE:ZENSARTECH)<br><sub>🚀SS·60x · ↓CMF26d · 🎯SLING</sub> | ✓ SAFE | Digital solutions and IT services for global enterprises | 🔥 BULL_OS_PPV | 35 | 🔄8 | ↑0.994 | ↓32d | PV | -13.3% | -64.58/-69.77 | +3.52% | 20% |
| [FIRSTCRY](https://in.tradingview.com/chart/?symbol=NSE:FIRSTCRY)<br><sub>RVOL28x · ↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | Mothers babies kids products e-commerce retail platform | 🔥 BULL_OS_PPV | 35 | 🔄2 | ↑0.983 | ↓26d | PV | -19.4% | -57.2/-61.69 | +1.60% | 20% |
| [ALKEM](https://in.tradingview.com/chart/?symbol=NSE:ALKEM)<br><sub>🚀SS · ↓CMF4d · 🎯SLING</sub> | ⚠ CAUTION | Pharma manufacturer generic drugs domestic international markets | 🔥 BULL_OS_PPV | 35 | 🔄39 | ↑0.998 | ↓30d | PV | -8.0% | -56.0/-60.49 | +1.44% | 20% |
| [REDTAPE](https://in.tradingview.com/chart/?symbol=NSE:REDTAPE)<br><sub>RVOL113x · ↓CMF30d</sub> | ✓ SAFE | Footwear apparel accessories omnichannel retail men women kids | ⚡ BULL_ANY_PPV | 54 | 🔄35 | ↑1.021 | ↑1d | PV | +4.1% | -42.83/-52.01 | +4.11% | 20% |
| [KPITTECH](https://in.tradingview.com/chart/?symbol=NSE:KPITTECH)<br><sub>🚀SS · ↓CMF11d · 🎯SLING</sub> | ✓ SAFE | Automotive software, embedded systems, SDV development | ⚡ BULL_ANY_PPV | 42 | 🔄2 | ↑0.997 | ↓13d | PV | -4.2% | -52.74/-57.1 | +1.67% | 20% |
| [CAMS](https://in.tradingview.com/chart/?symbol=NSE:CAMS)<br><sub>🚀SS · ↑CMF9d · 🎯SLING</sub> | ✓ SAFE | Mutual fund registry, transfer agent, investor servicing platform | ⚡ BULL_ANY_PPV | 42 | 🔄38 | ↑0.989 | ↓13d | PV | -3.2% | -58.18/-59.42 | +0.89% | 20% |
| [SONATSOFTW](https://in.tradingview.com/chart/?symbol=NSE:SONATSOFTW)<br><sub>🚀SS · ↓CMF11d · 🎯SLING</sub> | ✓ SAFE | IT services, cloud modernization, enterprise digital transformation | ⚡ BULL_ANY_PPV | 35 | 🔄33 | ↑1.017 | ↓36d | PV | -4.1% | -53.91/-59.84 | +5.81% | 20% |
| [COLPAL](https://in.tradingview.com/chart/?symbol=NSE:COLPAL)<br><sub>↑CMF0d · 🎯SLING</sub> | ⚠ CAUTION | Toothpaste, toothbrush, mouthwash maker for mass consumers | ⚡ BULL_ANY_PPV | 35 | 🔄23 | ↑0.999 | ↓43d | PV | -9.0% | -52.14/-55.34 | +1.27% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:INDUSTOWER,NSE:FSL,NSE:MPHASIS,NSE:SHOPERSTOP,NSE:EMUDHRA,NSE:JINDALPOLY,NSE:KOPRAN,NSE:HATSUN,NSE:SIGMAADV,NSE:MANKIND,NSE:TATAELXSI,NSE:ZENSARTECH,NSE:FIRSTCRY,NSE:ALKEM,NSE:REDTAPE,NSE:KPITTECH,NSE:CAMS,NSE:SONATSOFTW,NSE:COLPAL
```

### 🟢 OVERSOLD — reversal from −53/−60 (18)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [CUMMINSIND](https://in.tradingview.com/chart/?symbol=NSE:CUMMINSIND)<br><sub>↑CMF1d · 🎯SLING</sub> | ✓ SAFE |  | 🟢 BULL_OVERSOLD | 59 | 🔄53 | ↑1.012 | ↑1d | — | +2.7% | -56.42/-62.44 | +2.68% | 20% |
| [HEXT](https://in.tradingview.com/chart/?symbol=NSE:HEXT)<br><sub>🚀SS · ↑CMF12d · 🎯SLING</sub> | ✓ SAFE | IT services, digital transformation, automation, enterprise clients | 🟢 BULL_OVERSOLD | 43 | 🔄36 | ↑1.001 | ↓17d | — | -2.8% | -66.27/-69.3 | +4.11% | 20% |
| [TTKPRESTIG](https://in.tradingview.com/chart/?symbol=NSE:TTKPRESTIG)<br><sub>↓CMF15d · 🎯SLING</sub> | ⚠ CAUTION | Pressure cookers, cookware, kitchen appliances for households | 🟢 BULL_OVERSOLD | 40 | 🔄39 | ↑0.979 | ↓15d | — | -9.3% | -61.33/-62.1 | +0.50% | 20% |
| [FLAIR](https://in.tradingview.com/chart/?symbol=NSE:FLAIR)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Ball pen manufacturer for retail consumer stationery market | 🟢 BULL_OVERSOLD | 39 | 🔄9 | ↓0.976 | ↓11d | — | -6.0% | -75.23/-75.76 | -1.00% | 20% |
| [NATCOPHARM](https://in.tradingview.com/chart/?symbol=NSE:NATCOPHARM)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Generic oncology drugs, complex formulations, global pharma markets | 🟢 BULL_OVERSOLD | 35 | 🔄31 | ↑0.989 | ↓24d | — | -10.5% | -60.98/-62.76 | +0.47% | 20% |
| [LATENTVIEW](https://in.tradingview.com/chart/?symbol=NSE:LATENTVIEW)<br><sub>🚀SS · ↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Data analytics consulting, marketing optimization, enterprise clients | 🟢 BULL_OVERSOLD | 35 | 🔄4 | ↑0.975 | ↓37d | — | -14.6% | -63.79/-65.11 | +0.18% | 20% |
| [RALLIS](https://in.tradingview.com/chart/?symbol=NSE:RALLIS)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Agrochemicals, seeds, crop nutrients for Indian farmers | 🟢 BULL_OVERSOLD | 35 | 🔄9 | ↓0.982 | ↓15d | — | -5.7% | -67.26/-67.48 | -0.58% | 20% |
| [BRIGHOTEL](https://in.tradingview.com/chart/?symbol=NSE:BRIGHOTEL)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 35 | 🔄15 | ↓0.982 | ↓15d | — | -5.4% | -67.84/-68.22 | -0.65% | 20% |
| [HGS](https://in.tradingview.com/chart/?symbol=NSE:HGS)<br><sub>↓CMF25d · 🎯SLING</sub> | ⚠ CAUTION | Customer experience BPM services, global contact center operations | 🟢 BULL_OVERSOLD | 35 | 🔄24 | ↑0.985 | ↓28d | — | -9.8% | -67.54/-68.14 | +0.04% | 20% |
| [TATACONSUM](https://in.tradingview.com/chart/?symbol=NSE:TATACONSUM)<br><sub>↓CMF30d · 🎯SLING</sub> | ⚠ CAUTION |  | 🟢 BULL_OVERSOLD | 30 | 🔄24 | ↓0.981 | ↓24d | — | -7.1% | -68.61/-69.84 | -0.49% | 20% |
| [GOLDIAM](https://in.tradingview.com/chart/?symbol=NSE:GOLDIAM)<br><sub>↓CMF27d · 🎯SLING</sub> | ✓ SAFE | Diamond gold silver jewelry manufacturer exporting globally | 🟢 BULL_OVERSOLD | 5 | ↓13 | ↑0.973 | ↓22d | — | -11.3% | -62.23/-62.72 | -0.26% | 20% |
| [SAGCEM](https://in.tradingview.com/chart/?symbol=NSE:SAGCEM)<br><sub>🚀SS · ↓CMF16d · 🎯SLING</sub> | ⚠ CAUTION | Cement manufacturing, South and Central India construction | 🟢 BULL_OVERSOLD | 5 | ↓5 | ↑0.972 | ↓37d | — | -17.3% | -70.91/-71.56 | +0.38% | 20% |
| [DELTACORP](https://in.tradingview.com/chart/?symbol=NSE:DELTACORP)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Casinos, hotels, online gaming, entertainment | 🟢 BULL_OVERSOLD | 4 | ↓11 | ↓0.972 | ↓16d | — | -8.6% | -68.61/-68.79 | -0.66% | 20% |
| [BHARATWIRE](https://in.tradingview.com/chart/?symbol=NSE:BHARATWIRE)<br><sub>↓CMF30d · ⚠️TRAP</sub> | ✓ SAFE | Steel wire ropes manufacturing for industrial rigging applications | 🟢 BULL_OVERSOLD | 0 | ↓31 | ↓0.962 | ↓30d | — | -16.1% | -64.94/-64.99 | -2.55% | 20% |
| [SANOFI](https://in.tradingview.com/chart/?symbol=NSE:SANOFI)<br><sub>↓CMF15d · 🎯SLING</sub> | ⚠ CAUTION | Pharmaceutical diabetes cardiology CNS medicines India | 🟡 BULL_OS_L2 | 41 | 🔄15 | ↑1.002 | ↓19d | — | -4.3% | -55.31/-58.1 | +1.68% | 20% |
| [GULFOILLUB](https://in.tradingview.com/chart/?symbol=NSE:GULFOILLUB)<br><sub>↓CMF30d · 🎯SLING</sub> | ✓ SAFE | Automotive lubricants manufacturing distribution Indian commercial vehicles | 🟡 BULL_OS_L2 | 38 | 🔄43 | ↑0.981 | ↓17d | — | -7.2% | -52.79/-53.01 | -0.32% | 20% |
| [CEATLTD](https://in.tradingview.com/chart/?symbol=NSE:CEATLTD)<br><sub>↓CMF11d · 🎯SLING</sub> | ⚠ CAUTION | Radial and bias tyres for two-wheelers, cars, trucks | 🟡 BULL_OS_L2 | 35 | 🔄38 | ↑0.987 | ↓32d | — | -4.3% | -52.73/-53.79 | +0.12% | 20% |
| [IVALUE](https://in.tradingview.com/chart/?symbol=NSE:IVALUE)<br><sub>🚀SS · ↓CMF30d · 🎯SLING · ÷DIV</sub> | ✓ SAFE | IT distributor hybrid cloud solutions enterprise security | 🟡 BULL_OS_L2 | 7 | ↓50 | ↑0.970 | ↓18d | — | -19.3% | -55.48/-56.72 | +1.05% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CUMMINSIND,NSE:HEXT,NSE:TTKPRESTIG,NSE:FLAIR,NSE:NATCOPHARM,NSE:LATENTVIEW,NSE:RALLIS,NSE:BRIGHOTEL,NSE:HGS,NSE:TATACONSUM,NSE:GOLDIAM,NSE:SAGCEM,NSE:DELTACORP,NSE:BHARATWIRE,NSE:SANOFI,NSE:GULFOILLUB,NSE:CEATLTD,NSE:IVALUE
```

### 📈 MID-RANGE — any cross, WT2 > −53, no PPV (9)
| Symbol | Trap | Label | Signal | Erly | RS | C/AvgC | ZL | Flags | ZL Chg% | WT | Day Chg | Circuit |
|--------|:----:|-------|--------|-----:|:--:|-------:|:--:|:-----:|--------:|:--:|--------:|:-------:|
| [HINDZINC](https://in.tradingview.com/chart/?symbol=NSE:HINDZINC)<br><sub>📶W9 · W↑28d · ↑CMF14d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 28 | ↑64 | ↑1.014 | ↑2d | — | +2.7% | 24.78/23.85 | +1.56% | 20% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>📶W9 · ↓CMF7d · ÷DIV</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 19 | ↑77 | ↑1.039 | ↑1d | — | +5.1% | -9.05/-16.39 | +5.11% | 20% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>📶W9 · W↑109d · ↑CMF25d</sub> | ✓ SAFE |  | 📈 BULL_ANY_MID | 17 | ↑79 | ↓1.015 | ↑3d | — | +4.4% | 32.49/29.43 | +0.17% | 20% |
| [MEESHO](https://in.tradingview.com/chart/?symbol=NSE:MEESHO)<br><sub>📶W9 · 🚀SS · ↑CMF29d</sub> | ✓ SAFE | Social commerce marketplace connecting small sellers to tier-2 consumers | 📈 BULL_ANY_MID | 0 | ↑50 | ↑1.036 | ↑24d | — | +16.7% | 57.53/55.6 | +3.13% | 20% 🟦 |
| [MASTEK](https://in.tradingview.com/chart/?symbol=NSE:MASTEK)<br><sub>🚀SS · ↑CMF12d</sub> | ✓ SAFE | Digital engineering, Oracle Cloud, enterprise transformation | 📈 BULL_ANY_MID | 44 | 🔄33 | ↑0.991 | ↓11d | — | -5.5% | -33.85/-34.94 | +1.59% | 20% |
| [INDRAMEDCO](https://in.tradingview.com/chart/?symbol=NSE:INDRAMEDCO)<br><sub>↓CMF30d</sub> | ✓ SAFE | Tertiary care hospital, multi-specialty, Delhi-based healthcare | 📈 BULL_ANY_MID | 39 | 🔄17 | ↑0.993 | ↓16d | — | -4.7% | -49.42/-50.78 | -0.13% | 20% |
| [TENNIND](https://in.tradingview.com/chart/?symbol=NSE:TENNIND)<br><sub>🚀SS · ↑CMF29d</sub> | ✓ SAFE | Automotive emissions control systems supplier for passenger vehicles | 📈 BULL_ANY_MID | 35 | 🔄50 | ↑0.991 | ↓22d | — | -5.3% | -43.81/-44.28 | +1.29% | 20% |
| [BETA](https://in.tradingview.com/chart/?symbol=NSE:BETA)<br><sub>↓CMF30d</sub> | ✓ SAFE | Oncology drug manufacturer for cancer treatment domestic export | 📈 BULL_ANY_MID | 30 | 🔄80 | ↓0.982 | ↓32d | — | -5.7% | -43.29/-44.57 | -0.63% | 20% |
| [IZMO](https://in.tradingview.com/chart/?symbol=NSE:IZMO)<br><sub>↓CMF30d</sub> | ✓ SAFE | Automotive digital retail and marketing technology solutions | 📈 BULL_ANY_MID | 17 | ↑48 | ↓0.992 | ↓3d | — | -0.5% | -6.28/-7.15 | -1.19% | 20% |

```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:HINDZINC,NSE:ADANIENT,NSE:BOSCHLTD,NSE:MEESHO,NSE:MASTEK,NSE:INDRAMEDCO,NSE:TENNIND,NSE:BETA,NSE:IZMO
```

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
