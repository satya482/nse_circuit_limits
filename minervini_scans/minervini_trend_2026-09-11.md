> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-09-11
*Generated 2026-09-11 15:45 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE) | [AARTIIND](https://in.tradingview.com/chart/?symbol=NSE:AARTIIND) |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG) | [APLAPOLLO](https://in.tradingview.com/chart/?symbol=NSE:APLAPOLLO) |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS) | [CAPLIPOINT](https://in.tradingview.com/chart/?symbol=NSE:CAPLIPOINT) |
| [DEEPINDS](https://in.tradingview.com/chart/?symbol=NSE:DEEPINDS) | [CEIGALL](https://in.tradingview.com/chart/?symbol=NSE:CEIGALL) |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH) | [DYCL](https://in.tradingview.com/chart/?symbol=NSE:DYCL) |
| [EXICOM](https://in.tradingview.com/chart/?symbol=NSE:EXICOM) | [ELGIEQUIP](https://in.tradingview.com/chart/?symbol=NSE:ELGIEQUIP) |
| [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX) | [EMCURE](https://in.tradingview.com/chart/?symbol=NSE:EMCURE) |
| [IONEXCHANG](https://in.tradingview.com/chart/?symbol=NSE:IONEXCHANG) | [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO) |
| [KIRLOSIND](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSIND) | [EPL](https://in.tradingview.com/chart/?symbol=NSE:EPL) |
| [KRN](https://in.tradingview.com/chart/?symbol=NSE:KRN) | [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR) |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH) | [GODREJAGRO](https://in.tradingview.com/chart/?symbol=NSE:GODREJAGRO) |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE) | [ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL) |
| [PRICOLLTD](https://in.tradingview.com/chart/?symbol=NSE:PRICOLLTD) | [IFCI](https://in.tradingview.com/chart/?symbol=NSE:IFCI) |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL) | [JKPAPER](https://in.tradingview.com/chart/?symbol=NSE:JKPAPER) |
| [QUADFUTURE](https://in.tradingview.com/chart/?symbol=NSE:QUADFUTURE) | [JTLIND](https://in.tradingview.com/chart/?symbol=NSE:JTLIND) |
| [RACLGEAR](https://in.tradingview.com/chart/?symbol=NSE:RACLGEAR) | [KINGFA](https://in.tradingview.com/chart/?symbol=NSE:KINGFA) |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL) | [KIRLOSENG](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSENG) |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV) | [KOLTEPATIL](https://in.tradingview.com/chart/?symbol=NSE:KOLTEPATIL) |
| [SOTL](https://in.tradingview.com/chart/?symbol=NSE:SOTL) | [KSL](https://in.tradingview.com/chart/?symbol=NSE:KSL) |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL) | [LUMAXIND](https://in.tradingview.com/chart/?symbol=NSE:LUMAXIND) |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH) | [MANORAMA](https://in.tradingview.com/chart/?symbol=NSE:MANORAMA) |
| [YASHO](https://in.tradingview.com/chart/?symbol=NSE:YASHO) | [MEDANTA](https://in.tradingview.com/chart/?symbol=NSE:MEDANTA) |
|  | [NORTHARC](https://in.tradingview.com/chart/?symbol=NSE:NORTHARC) |
|  | [PGIL](https://in.tradingview.com/chart/?symbol=NSE:PGIL) |
|  | [RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO) |
|  | [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS) |
|  | [SAIL](https://in.tradingview.com/chart/?symbol=NSE:SAIL) |
|  | [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV) |
|  | [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD) |
|  | [SPLPETRO](https://in.tradingview.com/chart/?symbol=NSE:SPLPETRO) |
|  | [STAR](https://in.tradingview.com/chart/?symbol=NSE:STAR) |
|  | [VSSL](https://in.tradingview.com/chart/?symbol=NSE:VSSL) |
|  | [WSTCSTPAPR](https://in.tradingview.com/chart/?symbol=NSE:WSTCSTPAPR) |

### Scan definition
| Filter | Value |
|--------|-------|
| Exchange | NSE common equity |
| Price | > Rs 50 |
| Market cap | Rs 1,000 Cr - Rs 5 Lakh Cr |
| Criteria (all must pass) | close > SMA50 > SMA150 > SMA200 stack, SMA200 rising 21d, close within 25% of 52wk high, close >= 30% above 52wk low, RS gate |
| RS gate | Daily RS Line > Weekly RS EMA9, Weekly RS EMA9 rising (RS = close/NIFTY MIDSML 400 x 1000) |
| Age | Consecutive trading days all 9 checks (incl. RS gate) have held true together, capped at 400d |
| Float gate | AVOID dropped from scan, SAFE/CAUTION shown under symbol (float_gate.py) |
| Symbol tags | trap - liq (avg10Cr-todayCr) - CMF - DEL% |

---

**Qualifying: 147**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABSLAMC,NSE:ACE,NSE:ACUTAAS,NSE:ADANIENT,NSE:ADANIPORTS,NSE:ADANIPOWER,NSE:AEGISLOG,NSE:ANTELOPUS,NSE:APOLLO,NSE:APOLLOHOSP,NSE:BALAMINES,NSE:BHEL,NSE:CGCL,NSE:CGPOWER,NSE:CONFIPET,NSE:CPPLUS,NSE:EDELWEISS,NSE:GRANULES,NSE:GRAPHITE,NSE:GRASIM,NSE:GVT&D,NSE:HINDALCO,NSE:HONASA,NSE:INDNIPPON,NSE:IONEXCHANG,NSE:JAMNAAUTO,NSE:JINDWORLD,NSE:JSWINFRA,NSE:KIRLOSIND,NSE:MAHABANK,NSE:MAHSEAMLES,NSE:MIDHANI,NSE:MOTILALOFS,NSE:NIACL,NSE:NOVARTIND,NSE:PAISALO,NSE:PPLPHARMA,NSE:PRICOLLTD,NSE:PRIVISCL,NSE:PVRINOX,NSE:RAIN,NSE:RBLBANK,NSE:SHREEJISPG,NSE:SKIPPER,NSE:SUDARSCHEM,NSE:TEJASNET,NSE:UNIONBANK,NSE:VARROC,NSE:VENUSPIPES,NSE:WABAG,NSE:WOCKPHARMA,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ACMESOLAR,NSE:AEROFLEX,NSE:BLUESTONE,NSE:BODALCHEM,NSE:CYIENTDLM,NSE:DATAPATTNS,NSE:DEEPINDS,NSE:EBGNG,NSE:EMIL,NSE:ENGINERSIN,NSE:EXICOM,NSE:FILATEX,NSE:FINCABLES,NSE:GLENMARK,NSE:HFCL,NSE:INOXINDIA,NSE:IPCALAB,NSE:JINDRILL,NSE:KRN,NSE:KROSS,NSE:LUMAXTECH,NSE:MANINDS,NSE:MCX,NSE:NEOGEN,NSE:NEULANDLAB,NSE:QPOWER,NSE:QUADFUTURE,NSE:RAYMOND,NSE:RPEL,NSE:WELSPUNLIV,NSE:WHEELS,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ANTHEM,NSE:APARINDS,NSE:AUROPHARMA,NSE:AVALON,NSE:BIRLACABLE,NSE:BOSCHLTD,NSE:CRAFTSMAN,NSE:DIACABS,NSE:DIVISLAB,NSE:DYNAMATECH,NSE:FCL,NSE:FLUOROCHEM,NSE:HEG,NSE:JINDALSAW,NSE:KABRAEXTRU,NSE:KENNAMET,NSE:LALPATHLAB,NSE:MARINE,NSE:MARKSANS,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:NAVINFLUOR,NSE:NETWEB,NSE:NRBBEARING,NSE:PNBHOUSING,NSE:RACLGEAR,NSE:RATNAVEER,NSE:RKFORGE,NSE:SETL,NSE:SHAILY,NSE:SIEMENS,NSE:SIGMAADV,NSE:SMLMAH,NSE:SOLARINDS,NSE:SSWL,NSE:STLTECH,NSE:SYRMA,NSE:TBZ,NSE:TFCILTD,NSE:UNIMECH,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AETHER,NSE:ATHERENERG,NSE:AZAD,NSE:BALRAMCHIN,NSE:CHENNPETRO,NSE:GLAND,NSE:IOLCP,NSE:KARURVYSYA,NSE:KTKBANK,NSE:MTARTECH,NSE:NAZARA,NSE:SHILPAMED,NSE:SOTL,NSE:TITAN,NSE:YASHO,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AKUMS,NSE:CUPID,NSE:LAURUSLABS,NSE:NYKAA,NSE:PARAS,NSE:SAILIFE,NSE:SANSERA,NSE:SKYGOLD,NSE:SONACOMS,NSE:WELCORP
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>✓ SAFE . ↗921Cr · 1631Cr . ↓CMF7d</sub> | 3104.10 | -3.3% | +76.5% | 0d | SMA-OK | RS-OK | +5.11% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>⚠ CAUTION . →294Cr · 318Cr . ↓CMF0d</sub> | 1020.80 | -11.2% | +38.2% | 0d | SMA-OK | RS-OK | +1.17% |
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO)<br><sub>✓ SAFE . ↗306Cr · 327Cr . ↓CMF1d</sub> | 422.25 | -6.2% | +131.8% | 0d | SMA-OK | RS-OK | +2.19% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>✓ SAFE . ↗589Cr · 962Cr . ↑CMF1d</sub> | 1765.20 | -6.3% | +35.4% | 0d | SMA-OK | RS-OK | +3.23% |
| [GVT&D](https://in.tradingview.com/chart/?symbol=NSE:GVT&D)<br><sub>✓ SAFE . ↗550Cr · 503Cr . ↑CMF1d</sub> | 4656.00 | -15.9% | +82.0% | 0d | SMA-OK | RS-OK | -1.98% |
| [KIRLOSIND](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSIND)<br><sub>✓ SAFE . ↗26Cr · 245Cr . ↑CMF0d</sub> | 3828.30 | -11.2% | +54.8% | 0d | SMA-OK | RS-OK | +7.03% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>✓ SAFE . ↗602Cr · 703Cr . ↓CMF30d</sub> | 214.00 | -14.0% | +75.8% | 0d | SMA-OK | RS-OK | +2.69% |
| [APOLLOHOSP](https://in.tradingview.com/chart/?symbol=NSE:APOLLOHOSP)<br><sub>✓ SAFE . ↘252Cr · 323Cr . ↑CMF1d</sub> | 8935.00 | -1.3% | +31.5% | 0d | SMA-OK | RS-OK | +1.10% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>✓ SAFE . →125Cr · 165Cr . ↑CMF4d</sub> | 1353.60 | -4.5% | +130.2% | 0d | SMA-OK | RS-OK | +3.52% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>✓ SAFE . ↗112Cr · 110Cr . ↓CMF0d</sub> | 3383.70 | -8.4% | +156.8% | 0d | SMA-OK | RS-OK | -1.96% |
| [MIDHANI](https://in.tradingview.com/chart/?symbol=NSE:MIDHANI)<br><sub>✓ SAFE . ↗224Cr · 87Cr . ↑CMF21d</sub> | 447.40 | -6.2% | +65.4% | 0d | SMA-OK | RS-OK | -3.44% |
| [JAMNAAUTO](https://in.tradingview.com/chart/?symbol=NSE:JAMNAAUTO)<br><sub>✓ SAFE . ↗30Cr · 85Cr . ↑CMF3d</sub> | 135.46 | -8.6% | +48.5% | 0d | SMA-OK | RS-OK | +2.73% |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL)<br><sub>✓ SAFE . ↗30Cr · 38Cr . ↑CMF0d</sub> | 3556.10 | -5.2% | +52.5% | 0d | SMA-OK | RS-OK | +1.73% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . ↗118Cr · 109Cr . ↓CMF14d</sub> | 1237.10 | -1.4% | +34.7% | 2d | SMA-OK | RS-OK | +1.29% |
| [SUDARSCHEM](https://in.tradingview.com/chart/?symbol=NSE:SUDARSCHEM)<br><sub>✓ SAFE . →59Cr · 39Cr . ↑CMF20d</sub> | 1248.20 | -18.1% | +67.0% | 2d | SMA-OK | RS-OK | -1.78% |
| [WABAG](https://in.tradingview.com/chart/?symbol=NSE:WABAG)<br><sub>✓ SAFE . →201Cr · 508Cr . ↑CMF3d</sub> | 2277.90 | 0.0% | +117.1% | 3d | SMA-OK | RS-OK | +2.99% |
| [CGPOWER](https://in.tradingview.com/chart/?symbol=NSE:CGPOWER)<br><sub>✓ SAFE . ↗281Cr · 312Cr . ↑CMF25d</sub> | 925.30 | -5.2% | +74.4% | 3d | SMA-OK | RS-OK | +1.60% |
| [UNIONBANK](https://in.tradingview.com/chart/?symbol=NSE:UNIONBANK)<br><sub>✓ SAFE . →151Cr · 125Cr . ↓CMF0d</sub> | 182.67 | -9.7% | +44.0% | 3d | SMA-OK | RS-OK | -0.30% |
| [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA)<br><sub>✓ SAFE . ↗85Cr · 101Cr . ↑CMF0d</sub> | 343.15 | -2.3% | +46.5% | 3d | SMA-OK | RS-OK | +0.20% |
| [ABSLAMC](https://in.tradingview.com/chart/?symbol=NSE:ABSLAMC)<br><sub>⚠ CAUTION . ↗31Cr · 64Cr . ↑CMF14d</sub> | 1109.90 | -7.4% | +54.8% | 3d | SMA-OK | RS-OK | +1.97% |
| [MOTILALOFS](https://in.tradingview.com/chart/?symbol=NSE:MOTILALOFS)<br><sub>✓ SAFE . ↘76Cr · 64Cr . ↑CMF15d</sub> | 1026.50 | -5.9% | +63.4% | 3d | SMA-OK | RS-OK | +1.13% |
| [IONEXCHANG](https://in.tradingview.com/chart/?symbol=NSE:IONEXCHANG)<br><sub>✓ SAFE . ↗46Cr · 60Cr . ↑CMF5d</sub> | 445.70 | -4.8% | +40.5% | 3d | SMA-OK | RS-OK | +2.35% |
| [PRICOLLTD](https://in.tradingview.com/chart/?symbol=NSE:PRICOLLTD)<br><sub>✓ SAFE . →30Cr · 58Cr . ↓CMF0d</sub> | 761.40 | -5.6% | +50.2% | 3d | SMA-OK | RS-OK | +2.95% |
| [INDNIPPON](https://in.tradingview.com/chart/?symbol=NSE:INDNIPPON)<br><sub>✓ SAFE . ↗67Cr · 37Cr . ↓CMF1d</sub> | 1358.90 | -0.7% | +100.1% | 3d | SMA-OK | RS-OK | -0.74% |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE)<br><sub>✓ SAFE . ↗524Cr · 328Cr . ↑CMF2d</sub> | 825.80 | -2.2% | +58.2% | 4d | SMA-OK | RS-OK | +0.12% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>✓ SAFE . ↗109Cr · 72Cr . ↑CMF0d</sub> | 211.35 | -6.7% | +58.6% | 4d | SMA-OK | RS-OK | -0.54% |
| [VARROC](https://in.tradingview.com/chart/?symbol=NSE:VARROC)<br><sub>✓ SAFE . ↗45Cr · 42Cr . ↑CMF1d</sub> | 872.00 | -1.4% | +86.6% | 4d | SMA-OK | RS-OK | -1.40% |
| [GRANULES](https://in.tradingview.com/chart/?symbol=NSE:GRANULES)<br><sub>✓ SAFE . ↗181Cr · 714Cr . ↑CMF1d</sub> | 909.30 | 0.0% | +76.7% | 5d | SMA-OK | RS-OK | +1.12% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>✓ SAFE . ↗786Cr · 474Cr . ↑CMF7d</sub> | 1139.35 | -2.6% | +216.9% | 5d | SMA-OK | RS-OK | +1.36% |
| [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO)<br><sub>✓ SAFE . ↗158Cr · 141Cr . ↑CMF6d</sub> | 84.23 | 0.0% | +172.0% | 5d | SMA-OK | RS-OK | +1.42% |
| [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK)<br><sub>✓ SAFE . ↗213Cr · 132Cr . ↑CMF22d</sub> | 412.55 | -1.4% | +56.0% | 5d | SMA-OK | RS-OK | +0.43% |
| [NOVARTIND](https://in.tradingview.com/chart/?symbol=NSE:NOVARTIND)<br><sub>✓ SAFE . ↗102Cr · 109Cr . ↑CMF3d</sub> | 2391.30 | -1.5% | +349.7% | 5d | SMA-OK | RS-OK | -1.52% |
| [RAIN](https://in.tradingview.com/chart/?symbol=NSE:RAIN)<br><sub>✓ SAFE . ↗111Cr · 94Cr . ↓CMF25d</sub> | 215.97 | -11.1% | +112.8% | 5d | SMA-OK | RS-OK | -0.60% |
| [VENUSPIPES](https://in.tradingview.com/chart/?symbol=NSE:VENUSPIPES)<br><sub>✓ SAFE . ↗58Cr · 61Cr . ↑CMF4d</sub> | 2020.10 | 0.0% | +126.0% | 5d | SMA-OK | RS-OK | +3.64% |
| [HONASA](https://in.tradingview.com/chart/?symbol=NSE:HONASA)<br><sub>✓ SAFE . ↘41Cr · 32Cr . ↓CMF0d</sub> | 471.15 | -6.3% | +83.8% | 5d | SMA-OK | RS-OK | -0.95% |
| [NIACL](https://in.tradingview.com/chart/?symbol=NSE:NIACL)<br><sub>✓ SAFE . ↗432Cr · 139Cr . ↑CMF7d</sub> | 198.39 | -14.2% | +68.4% | 6d | SMA-OK | RS-OK | +0.53% |
| [TEJASNET](https://in.tradingview.com/chart/?symbol=NSE:TEJASNET)<br><sub>✓ SAFE . →331Cr · 136Cr . ↓CMF4d</sub> | 552.65 | -12.6% | +86.6% | 6d | SMA-OK | RS-OK | +0.52% |
| [JINDWORLD](https://in.tradingview.com/chart/?symbol=NSE:JINDWORLD)<br><sub>✓ SAFE . ↗355Cr · 77Cr . ↑CMF8d</sub> | 52.88 | -9.6% | +192.2% | 6d | SMA-OK | RS-OK | -4.96% |
| [MAHSEAMLES](https://in.tradingview.com/chart/?symbol=NSE:MAHSEAMLES)<br><sub>✓ SAFE . ↗46Cr · 76Cr . ↑CMF1d</sub> | 728.90 | 0.0% | +43.9% | 6d | SMA-OK | RS-OK | +1.38% |
| [WOCKPHARMA](https://in.tradingview.com/chart/?symbol=NSE:WOCKPHARMA)<br><sub>✓ SAFE . ↗338Cr · 242Cr . ↑CMF4d</sub> | 2179.40 | -3.1% | +98.1% | 7d | SMA-OK | RS-OK | -1.86% |
| [EDELWEISS](https://in.tradingview.com/chart/?symbol=NSE:EDELWEISS)<br><sub>✓ SAFE . ↗167Cr · 129Cr . ↑CMF3d</sub> | 132.43 | -4.6% | +32.9% | 7d | SMA-OK | RS-OK | -3.15% |
| [SKIPPER](https://in.tradingview.com/chart/?symbol=NSE:SKIPPER)<br><sub>✓ SAFE . ↗127Cr · 119Cr . ↑CMF17d</sub> | 551.55 | -8.8% | +66.9% | 7d | SMA-OK | RS-OK | -5.39% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>✓ SAFE . →330Cr · 361Cr . ↑CMF18d</sub> | 433.35 | -2.1% | +105.3% | 8d | SMA-OK | RS-OK | +2.65% |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>⚠ CAUTION . →341Cr · 271Cr . ↑CMF23d</sub> | 3295.00 | -2.5% | +30.2% | 8d | SMA-OK | RS-OK | -0.36% |
| [MAHABANK](https://in.tradingview.com/chart/?symbol=NSE:MAHABANK)<br><sub>✓ SAFE . →151Cr · 183Cr . ↓CMF3d</sub> | 84.20 | -10.3% | +56.0% | 9d | SMA-OK | RS-OK | -0.18% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . →84Cr · 64Cr . ↑CMF5d</sub> | 691.75 | -3.0% | +209.6% | 10d | SMA-OK | RS-OK | -2.99% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . ↘90Cr · 62Cr . ↑CMF1d</sub> | 3825.50 | -1.9% | +204.9% | 10d | SMA-OK | RS-OK | -0.09% |
| [CGCL](https://in.tradingview.com/chart/?symbol=NSE:CGCL)<br><sub>✓ SAFE . ↘141Cr · 52Cr . ↑CMF13d</sub> | 266.00 | -5.0% | +75.0% | 10d | SMA-OK | RS-OK | -2.30% |
| [CONFIPET](https://in.tradingview.com/chart/?symbol=NSE:CONFIPET)<br><sub>✓ SAFE . ↗45Cr · 42Cr . ↑CMF2d</sub> | 89.22 | -1.6% | +209.7% | 10d | SMA-OK | RS-OK | +1.57% |
| [BALAMINES](https://in.tradingview.com/chart/?symbol=NSE:BALAMINES)<br><sub>✓ SAFE . →65Cr · 40Cr . ↑CMF12d</sub> | 2276.50 | -11.3% | +133.0% | 10d | SMA-OK | RS-OK | -2.82% |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE)<br><sub>✓ SAFE . ↘33Cr · 34Cr . ↑CMF27d</sub> | 1129.00 | -4.7% | +50.7% | 10d | SMA-OK | RS-OK | +0.70% |
| [EXICOM](https://in.tradingview.com/chart/?symbol=NSE:EXICOM)<br><sub>✓ SAFE . ↗40Cr · 31Cr . ↑CMF5d</sub> | 182.28 | -1.1% | +139.0% | 11d | SMA-OK | RS-OK | +3.14% |
| [WHEELS](https://in.tradingview.com/chart/?symbol=NSE:WHEELS)<br><sub>✓ SAFE . ↗332Cr · 86Cr . ↑CMF11d</sub> | 2230.10 | -7.1% | +212.3% | 12d | SMA-OK | RS-OK | -3.58% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>✓ SAFE . ↘84Cr · 55Cr . ↑CMF12d</sub> | 2246.60 | -2.1% | +109.3% | 12d | SMA-OK | RS-OK | -2.14% |
| [RPEL](https://in.tradingview.com/chart/?symbol=NSE:RPEL)<br><sub>✓ SAFE . →28Cr · 32Cr . ↑CMF21d</sub> | 1845.20 | -2.1% | +225.8% | 12d | SMA-OK | RS-OK | +5.83% |
| [QUADFUTURE](https://in.tradingview.com/chart/?symbol=NSE:QUADFUTURE)<br><sub>✓ SAFE . ↘71Cr · 496Cr . ↑CMF15d</sub> | 478.50 | 0.0% | +89.4% | 14d | SMA-OK | RS-OK | +9.80% |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>✓ SAFE . ↘45Cr · 137Cr . ↑CMF22d</sub> | 633.25 | -6.6% | +42.2% | 15d | SMA-OK | RS-OK | -3.20% |
| [BODALCHEM](https://in.tradingview.com/chart/?symbol=NSE:BODALCHEM)<br><sub>✓ SAFE . ↗149Cr · 129Cr . ↑CMF17d</sub> | 172.40 | -6.3% | +296.8% | 15d | SMA-OK | RS-OK | +3.79% |
| [BLUESTONE](https://in.tradingview.com/chart/?symbol=NSE:BLUESTONE)<br><sub>✓ SAFE . →73Cr · 116Cr . ↑CMF0d</sub> | 890.35 | -0.5% | +120.7% | 15d | SMA-OK | RS-OK | +4.12% |
| [NEULANDLAB](https://in.tradingview.com/chart/?symbol=NSE:NEULANDLAB)<br><sub>✓ SAFE . →100Cr · 103Cr . ↑CMF4d</sub> | 23535.00 | -1.9% | +103.7% | 15d | SMA-OK | RS-OK | -1.11% |
| [GLENMARK](https://in.tradingview.com/chart/?symbol=NSE:GLENMARK)<br><sub>✓ SAFE . →115Cr · 84Cr . ↑CMF16d</sub> | 2419.20 | -3.8% | +33.6% | 15d | SMA-OK | RS-OK | +0.17% |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>✓ SAFE . ↘37Cr · 35Cr . ↑CMF1d</sub> | 1968.50 | -1.0% | +55.2% | 15d | SMA-OK | RS-OK | -0.12% |
| [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX)<br><sub>✓ SAFE . ↗45Cr · 340Cr . ↑CMF30d</sub> | 87.41 | 0.0% | +136.9% | 16d | SMA-OK | RS-OK | +14.64% |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN)<br><sub>✓ SAFE . ↗250Cr · 44Cr . ↑CMF27d</sub> | 268.95 | -4.6% | +63.4% | 16d | SMA-OK | RS-OK | -1.14% |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL)<br><sub>✓ SAFE . ↗48Cr · 44Cr . ↑CMF1d</sub> | 188.38 | -2.7% | +120.1% | 16d | SMA-OK | RS-OK | -1.79% |
| [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS)<br><sub>✓ SAFE . ↗32Cr · 51Cr . ↑CMF2d</sub> | 239.07 | 0.0% | +51.0% | 17d | SMA-OK | RS-OK | +3.25% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [DEEPINDS](https://in.tradingview.com/chart/?symbol=NSE:DEEPINDS)<br><sub>✓ SAFE . ↗55Cr · 40Cr . ↑CMF30d</sub> | 774.40 | -5.4% | +133.6% | 18d | SMA-OK | RS-OK | -1.07% |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>✓ SAFE . ↘78Cr · 50Cr . ↑CMF18d</sub> | 402.30 | -3.8% | +102.2% | 19d | SMA-OK | RS-OK | +1.27% |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH)<br><sub>✓ SAFE . ↗35Cr · 33Cr . ↑CMF0d</sub> | 1993.70 | -4.1% | +86.0% | 19d | SMA-OK | RS-OK | +2.63% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↗632Cr · 1629Cr . ↑CMF23d</sub> | 1002.80 | 0.0% | +211.6% | 20d | SMA-OK | RS-OK | +17.44% |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . ↘660Cr · 552Cr . ↑CMF22d</sub> | 3276.00 | -4.8% | +116.4% | 20d | SMA-OK | RS-OK | -0.73% |
| [FINCABLES](https://in.tradingview.com/chart/?symbol=NSE:FINCABLES)<br><sub>✓ SAFE . ↗240Cr · 478Cr . ↑CMF2d</sub> | 1424.00 | 0.0% | +100.3% | 20d | SMA-OK | RS-OK | +0.39% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>✓ SAFE . ↗163Cr · 392Cr . ↑CMF11d</sub> | 866.10 | -1.2% | +178.9% | 20d | SMA-OK | RS-OK | -1.18% |
| [DATAPATTNS](https://in.tradingview.com/chart/?symbol=NSE:DATAPATTNS)<br><sub>✓ SAFE . ↘336Cr · 271Cr . ↑CMF3d</sub> | 4829.20 | -2.1% | +121.3% | 20d | SMA-OK | RS-OK | +1.09% |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>✓ SAFE . ↘41Cr · 97Cr . ↓CMF30d</sub> | 2373.00 | -0.7% | +142.2% | 20d | SMA-OK | RS-OK | -0.67% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>✓ SAFE . ↘73Cr · 59Cr . ↑CMF22d</sub> | 563.95 | -1.7% | +255.1% | 20d | SMA-OK | RS-OK | -0.04% |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER)<br><sub>✓ SAFE . →47Cr · 52Cr . ↑CMF24d</sub> | 1426.50 | -6.1% | +139.7% | 20d | SMA-OK | RS-OK | -2.17% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>✓ SAFE . ↗84Cr · 46Cr . ↑CMF13d</sub> | 904.40 | -7.4% | +232.1% | 20d | SMA-OK | RS-OK | -2.05% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>✓ SAFE . ↗73Cr · 35Cr . ↑CMF23d</sub> | 679.65 | 0.0% | +180.2% | 20d | SMA-OK | RS-OK | +0.25% |
| [KRN](https://in.tradingview.com/chart/?symbol=NSE:KRN)<br><sub>✓ SAFE . ↘38Cr · 30Cr . ↑CMF27d</sub> | 1593.60 | -4.0% | +166.4% | 20d | SMA-OK | RS-OK | +0.57% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↘93Cr · 55Cr . ↑CMF0d</sub> | 207.68 | -2.0% | +91.7% | 21d | SMA-OK | RS-OK | -1.34% |
| [TBZ](https://in.tradingview.com/chart/?symbol=NSE:TBZ)<br><sub>✓ SAFE . ↗338Cr · 144Cr . ↑CMF12d</sub> | 526.30 | -5.2% | +372.0% | 22d | SMA-OK | RS-OK | +5.00% |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE)<br><sub>↗47Cr · 32Cr . ↑CMF29d</sub> | 419.15 | -3.1% | +176.3% | 22d | SMA-OK | RS-OK | +2.52% |
| [HEG](https://in.tradingview.com/chart/?symbol=NSE:HEG)<br><sub>✓ SAFE . →118Cr · 187Cr . ↑CMF15d</sub> | 728.25 | -1.5% | +52.6% | 22d | SMA-OK | RS-OK | +2.94% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>✓ SAFE . →183Cr · 132Cr . ↑CMF25d</sub> | 48870.00 | -2.3% | +70.0% | 24d | SMA-OK | RS-OK | +0.17% |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY)<br><sub>✓ SAFE . ↗51Cr · 63Cr . ↑CMF2d</sub> | 3279.50 | -5.2% | +80.0% | 24d | SMA-OK | RS-OK | -3.07% |
| [RACLGEAR](https://in.tradingview.com/chart/?symbol=NSE:RACLGEAR)<br><sub>✓ SAFE . ↗27Cr · 201Cr . ↑CMF0d</sub> | 1756.70 | 0.0% | +95.0% | 25d | SMA-OK | RS-OK | +10.61% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>✓ SAFE . →100Cr · 136Cr . ↑CMF30d</sub> | 1178.90 | -0.5% | +57.0% | 25d | SMA-OK | RS-OK | -0.01% |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH)<br><sub>✓ SAFE . →22Cr · 75Cr . ↑CMF0d</sub> | 12097.00 | -3.5% | +81.1% | 25d | SMA-OK | RS-OK | +4.80% |
| [JINDALSAW](https://in.tradingview.com/chart/?symbol=NSE:JINDALSAW)<br><sub>✓ SAFE . ↘72Cr · 59Cr . ↑CMF30d</sub> | 311.95 | -1.7% | +101.7% | 25d | SMA-OK | RS-OK | -1.75% |
| [KENNAMET](https://in.tradingview.com/chart/?symbol=NSE:KENNAMET)<br><sub>✓ SAFE . ↘20Cr · 33Cr . ↑CMF25d</sub> | 4682.40 | -6.9% | +126.9% | 25d | SMA-OK | RS-OK | -6.87% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>✓ SAFE . ↗92Cr · 79Cr . ↓CMF5d</sub> | 940.90 | -1.8% | +60.1% | 26d | SMA-OK | RS-OK | -0.15% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>✓ SAFE . →68Cr · 137Cr . ↑CMF23d</sub> | 468.15 | 0.0% | +343.1% | 27d | SMA-OK | RS-OK | +4.99% |
| [FCL](https://in.tradingview.com/chart/?symbol=NSE:FCL)<br><sub>✓ SAFE . ↗164Cr · 135Cr . ↑CMF15d</sub> | 57.72 | -1.7% | +200.0% | 27d | SMA-OK | RS-OK | -1.69% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . →268Cr · 177Cr . ↑CMF28d</sub> | 115.78 | -2.6% | +243.8% | 28d | SMA-OK | RS-OK | +0.43% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>⚠ CAUTION . ↗41Cr · 43Cr . ↑CMF2d</sub> | 1909.00 | -3.0% | +46.0% | 28d | SMA-OK | RS-OK | -0.40% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . ↗503Cr · 354Cr . ↑CMF30d</sub> | 9443.00 | -1.4% | +66.0% | 29d | SMA-OK | RS-OK | -1.38% |
| [SOLARINDS](https://in.tradingview.com/chart/?symbol=NSE:SOLARINDS)<br><sub>✓ SAFE . →401Cr · 204Cr . ↑CMF30d</sub> | 22330.00 | -0.6% | +89.7% | 29d | SMA-OK | RS-OK | -0.56% |
| [SMLMAH](https://in.tradingview.com/chart/?symbol=NSE:SMLMAH)<br><sub>✓ SAFE . ↗113Cr · 72Cr . ↑CMF5d</sub> | 6583.00 | 0.0% | +138.1% | 29d | SMA-OK | RS-OK | +4.86% |
| [SIEMENS](https://in.tradingview.com/chart/?symbol=NSE:SIEMENS)<br><sub>✓ SAFE . ↘119Cr · 146Cr . ↓CMF1d</sub> | 3947.70 | -3.7% | +38.6% | 29d | SMA-OK | RS-OK | -0.09% |
| [NETWEB](https://in.tradingview.com/chart/?symbol=NSE:NETWEB)<br><sub>✓ SAFE . ↘695Cr · 437Cr . ↓CMF5d</sub> | 5027.00 | -10.2% | +76.9% | 30d | SMA-OK | RS-OK | +0.27% |
| [APARINDS](https://in.tradingview.com/chart/?symbol=NSE:APARINDS)<br><sub>✓ SAFE . ↘201Cr · 296Cr . ↑CMF1d</sub> | 17500.00 | -2.8% | +151.2% | 30d | SMA-OK | RS-OK | +0.91% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>✓ SAFE . ↗358Cr · 102Cr . ↑CMF6d</sub> | 1589.30 | -3.0% | +148.3% | 30d | SMA-OK | RS-OK | -0.59% |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS)<br><sub>✓ SAFE . →90Cr · 54Cr . ↓CMF0d</sub> | 329.40 | -1.9% | +110.0% | 30d | SMA-OK | RS-OK | -0.30% |
| [NRBBEARING](https://in.tradingview.com/chart/?symbol=NSE:NRBBEARING)<br><sub>✓ SAFE . ↗25Cr · 36Cr . ↑CMF25d</sub> | 514.65 | -0.3% | +138.0% | 30d | SMA-OK | RS-OK | -0.25% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . ↗122Cr · 74Cr . ↑CMF5d</sub> | 8543.50 | -2.6% | +87.7% | 31d | SMA-OK | RS-OK | -1.80% |
| [BIRLACABLE](https://in.tradingview.com/chart/?symbol=NSE:BIRLACABLE)<br><sub>✓ SAFE . ↗21Cr · 39Cr . ↑CMF30d</sub> | 392.35 | 0.0% | +276.2% | 31d | SMA-OK | RS-OK | +4.72% |
| [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON)<br><sub>⚠ CAUTION . →198Cr · 93Cr . ↓CMF3d</sub> | 164.17 | -3.8% | +74.1% | 33d | SMA-OK | RS-OK | +0.20% |
| [AVALON](https://in.tradingview.com/chart/?symbol=NSE:AVALON)<br><sub>✓ SAFE . →124Cr · 76Cr . ↑CMF27d</sub> | 2264.50 | -4.6% | +185.3% | 33d | SMA-OK | RS-OK | +1.68% |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>✓ SAFE . →78Cr · 62Cr . ↓CMF19d</sub> | 4773.20 | -0.3% | +60.7% | 33d | SMA-OK | RS-OK | -0.27% |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH)<br><sub>✓ SAFE . ↗45Cr · 48Cr . ↑CMF3d</sub> | 1610.00 | -1.2% | +127.9% | 34d | SMA-OK | RS-OK | +2.67% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>⚠ CAUTION . →148Cr · 83Cr . ↑CMF28d</sub> | 1679.80 | -2.2% | +59.9% | 35d | SMA-OK | RS-OK | +0.68% |
| [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN)<br><sub>✓ SAFE . ↗82Cr · 62Cr . ↑CMF30d</sub> | 11669.00 | -1.5% | +81.6% | 35d | SMA-OK | RS-OK | -1.54% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>✓ SAFE . →55Cr · 41Cr . ↓CMF9d</sub> | 711.20 | -5.8% | +53.7% | 35d | SMA-OK | RS-OK | -2.18% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . ↘118Cr · 126Cr . ↑CMF30d</sub> | 288.30 | -7.2% | +119.6% | 37d | SMA-OK | RS-OK | -7.18% |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS)<br><sub>✓ SAFE . ↗363Cr · 101Cr . ↑CMF9d</sub> | 322.85 | -4.3% | +173.7% | 37d | SMA-OK | RS-OK | -0.35% |
| [KABRAEXTRU](https://in.tradingview.com/chart/?symbol=NSE:KABRAEXTRU)<br><sub>✓ SAFE . →27Cr · 35Cr . ↑CMF30d</sub> | 723.15 | 0.0% | +296.1% | 37d | SMA-OK | RS-OK | +2.20% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↗158Cr · 45Cr . ↑CMF8d</sub> | 370.65 | -0.8% | +117.5% | 39d | SMA-OK | RS-OK | -0.79% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . ↘108Cr · 86Cr . ↑CMF30d</sub> | 141.49 | -3.6% | +156.1% | 40d | SMA-OK | RS-OK | -1.17% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>✓ SAFE . ↘33Cr · 72Cr . ↑CMF0d</sub> | 763.65 | 0.0% | +710.9% | 40d | SMA-OK | RS-OK | +5.00% |
| [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP)<br><sub>✓ SAFE . →96Cr · 100Cr . ↑CMF12d</sub> | 194.31 | -8.8% | +184.9% | 43d | SMA-OK | RS-OK | -8.10% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>✓ SAFE . ↘71Cr · 69Cr . ↑CMF30d</sub> | 325.35 | -4.3% | +90.5% | 45d | SMA-OK | RS-OK | -2.17% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>⚠ CAUTION . ↘45Cr · 33Cr . ↓CMF18d</sub> | 333.80 | -5.8% | +62.3% | 45d | SMA-OK | RS-OK | -0.45% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↗246Cr · 114Cr . ↑CMF26d</sub> | 2922.30 | -3.4% | +83.0% | 46d | SMA-OK | RS-OK | -0.83% |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>✓ SAFE . →503Cr · 90Cr . ↑CMF29d</sub> | 691.40 | -9.9% | +73.8% | 47d | SMA-OK | RS-OK | -1.95% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . →61Cr · 43Cr . ↑CMF30d</sub> | 370.30 | -1.2% | +70.1% | 47d | SMA-OK | RS-OK | -1.16% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↗386Cr · 459Cr . ↑CMF2d</sub> | 1572.90 | -3.3% | +117.4% | 48d | SMA-OK | RS-OK | -3.29% |
| [TITAN](https://in.tradingview.com/chart/?symbol=NSE:TITAN)<br><sub>⚠ CAUTION . ↗289Cr · 235Cr . ↑CMF30d</sub> | 4985.50 | -3.6% | +49.8% | 48d | SMA-OK | RS-OK | -0.03% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>✓ SAFE . ↘103Cr · 129Cr . ↓CMF1d</sub> | 2849.10 | -1.8% | +108.5% | 50d | SMA-OK | RS-OK | +2.73% |
| [SOTL](https://in.tradingview.com/chart/?symbol=NSE:SOTL)<br><sub>✓ SAFE . ↗157Cr · 33Cr . ↑CMF8d</sub> | 716.25 | -8.4% | +148.6% | 51d | SMA-OK | RS-OK | +2.75% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . ↗1096Cr · 808Cr . ↑CMF30d</sub> | 1656.00 | -4.0% | +206.7% | 55d | SMA-OK | RS-OK | -0.14% |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>✓ SAFE . →129Cr · 141Cr . ↑CMF6d</sub> | 961.15 | -0.3% | +260.0% | 55d | SMA-OK | RS-OK | +2.26% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>✓ SAFE . →37Cr · 59Cr . ↑CMF1d</sub> | 1674.70 | -1.3% | +129.2% | 55d | SMA-OK | RS-OK | +2.10% |
| [YASHO](https://in.tradingview.com/chart/?symbol=NSE:YASHO)<br><sub>✓ SAFE . ↘15Cr · 40Cr . ↑CMF0d</sub> | 4187.50 | -14.8% | +259.2% | 55d | SMA-OK | RS-OK | +5.74% |
| [MTARTECH](https://in.tradingview.com/chart/?symbol=NSE:MTARTECH)<br><sub>✓ SAFE . ↗2251Cr · 944Cr . ↑CMF8d</sub> | 7777.00 | -7.1% | +457.1% | 58d | SMA-OK | RS-OK | -4.25% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . →158Cr · 137Cr . ↑CMF21d</sub> | 344.50 | -1.4% | +49.4% | 65d | SMA-OK | RS-OK | +0.75% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>✓ SAFE . →28Cr · 31Cr . ↓CMF9d</sub> | 776.35 | -0.5% | +87.5% | 70d | SMA-OK | RS-OK | +3.56% |
| [PARAS](https://in.tradingview.com/chart/?symbol=NSE:PARAS)<br><sub>✓ SAFE . ↘161Cr · 101Cr . ↑CMF27d</sub> | 1435.60 | -6.0% | +145.6% | 79d | SMA-OK | RS-OK | -1.22% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↗88Cr · 53Cr . ↑CMF22d</sub> | 4129.90 | -0.1% | +201.0% | 80d | SMA-OK | RS-OK | +0.54% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . ↗1042Cr · 216Cr . ↑CMF30d</sub> | 1876.70 | -3.2% | +125.5% | 84d | SMA-OK | RS-OK | +0.98% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↘109Cr · 66Cr . ↑CMF4d</sub> | 788.00 | -4.4% | +94.4% | 85d | SMA-OK | RS-OK | -1.93% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>✓ SAFE . ↘572Cr · 327Cr . ↑CMF30d</sub> | 2676.60 | -3.6% | +270.8% | 87d | SMA-OK | RS-OK | -3.61% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . ↗219Cr · 185Cr . ↑CMF8d</sub> | 1585.00 | -5.4% | +99.4% | 99d | SMA-OK | RS-OK | -0.38% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . ↗81Cr · 36Cr . ↑CMF1d</sub> | 827.40 | -2.4% | +214.3% | 104d | SMA-OK | RS-OK | -0.35% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↘314Cr · 299Cr . ↑CMF30d</sub> | 280.00 | -5.0% | +606.2% | 117d | SMA-OK | RS-OK | +0.92% |

### By Trend Age

**<2 WEEKS** (51)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABSLAMC,NSE:ACE,NSE:ACUTAAS,NSE:ADANIENT,NSE:ADANIPORTS,NSE:ADANIPOWER,NSE:AEGISLOG,NSE:ANTELOPUS,NSE:APOLLO,NSE:APOLLOHOSP,NSE:BALAMINES,NSE:BHEL,NSE:CGCL,NSE:CGPOWER,NSE:CONFIPET,NSE:CPPLUS,NSE:EDELWEISS,NSE:GRANULES,NSE:GRAPHITE,NSE:GRASIM,NSE:GVT&D,NSE:HINDALCO,NSE:HONASA,NSE:INDNIPPON,NSE:IONEXCHANG,NSE:JAMNAAUTO,NSE:JINDWORLD,NSE:JSWINFRA,NSE:KIRLOSIND,NSE:MAHABANK,NSE:MAHSEAMLES,NSE:MIDHANI,NSE:MOTILALOFS,NSE:NIACL,NSE:NOVARTIND,NSE:PAISALO,NSE:PPLPHARMA,NSE:PRICOLLTD,NSE:PRIVISCL,NSE:PVRINOX,NSE:RAIN,NSE:RBLBANK,NSE:SHREEJISPG,NSE:SKIPPER,NSE:SUDARSCHEM,NSE:TEJASNET,NSE:UNIONBANK,NSE:VARROC,NSE:VENUSPIPES,NSE:WABAG,NSE:WOCKPHARMA
```

**2-4 WEEKS** (31)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ACMESOLAR,NSE:AEROFLEX,NSE:BLUESTONE,NSE:BODALCHEM,NSE:CYIENTDLM,NSE:DATAPATTNS,NSE:DEEPINDS,NSE:EBGNG,NSE:EMIL,NSE:ENGINERSIN,NSE:EXICOM,NSE:FILATEX,NSE:FINCABLES,NSE:GLENMARK,NSE:HFCL,NSE:INOXINDIA,NSE:IPCALAB,NSE:JINDRILL,NSE:KRN,NSE:KROSS,NSE:LUMAXTECH,NSE:MANINDS,NSE:MCX,NSE:NEOGEN,NSE:NEULANDLAB,NSE:QPOWER,NSE:QUADFUTURE,NSE:RAYMOND,NSE:RPEL,NSE:WELSPUNLIV,NSE:WHEELS
```

**1-2 MONTHS** (40)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ANTHEM,NSE:APARINDS,NSE:AUROPHARMA,NSE:AVALON,NSE:BIRLACABLE,NSE:BOSCHLTD,NSE:CRAFTSMAN,NSE:DIACABS,NSE:DIVISLAB,NSE:DYNAMATECH,NSE:FCL,NSE:FLUOROCHEM,NSE:HEG,NSE:JINDALSAW,NSE:KABRAEXTRU,NSE:KENNAMET,NSE:LALPATHLAB,NSE:MARINE,NSE:MARKSANS,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:NAVINFLUOR,NSE:NETWEB,NSE:NRBBEARING,NSE:PNBHOUSING,NSE:RACLGEAR,NSE:RATNAVEER,NSE:RKFORGE,NSE:SETL,NSE:SHAILY,NSE:SIEMENS,NSE:SIGMAADV,NSE:SMLMAH,NSE:SOLARINDS,NSE:SSWL,NSE:STLTECH,NSE:SYRMA,NSE:TBZ,NSE:TFCILTD,NSE:UNIMECH
```

**2-3 MONTHS** (15)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AETHER,NSE:ATHERENERG,NSE:AZAD,NSE:BALRAMCHIN,NSE:CHENNPETRO,NSE:GLAND,NSE:IOLCP,NSE:KARURVYSYA,NSE:KTKBANK,NSE:MTARTECH,NSE:NAZARA,NSE:SHILPAMED,NSE:SOTL,NSE:TITAN,NSE:YASHO
```

**3-6 MONTHS** (10)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AKUMS,NSE:CUPID,NSE:LAURUSLABS,NSE:NYKAA,NSE:PARAS,NSE:SAILIFE,NSE:SANSERA,NSE:SKYGOLD,NSE:SONACOMS,NSE:WELCORP
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
