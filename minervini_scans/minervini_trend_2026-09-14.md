> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-09-14
*Generated 2026-09-14 15:45 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [ANGELONE](https://in.tradingview.com/chart/?symbol=NSE:ANGELONE) |  |

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

**Qualifying: 148**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABSLAMC,NSE:ACUTAAS,NSE:ADANIENT,NSE:ADANIPORTS,NSE:ADANIPOWER,NSE:AEGISLOG,NSE:ANGELONE,NSE:ANTELOPUS,NSE:APOLLO,NSE:APOLLOHOSP,NSE:BHEL,NSE:CGPOWER,NSE:EDELWEISS,NSE:GRANULES,NSE:GRAPHITE,NSE:GRASIM,NSE:GVT&D,NSE:HINDALCO,NSE:HONASA,NSE:INDNIPPON,NSE:IONEXCHANG,NSE:JAMNAAUTO,NSE:JINDWORLD,NSE:JSWINFRA,NSE:KIRLOSIND,NSE:MAHABANK,NSE:MAHSEAMLES,NSE:MIDHANI,NSE:MOTILALOFS,NSE:NIACL,NSE:NOVARTIND,NSE:PAISALO,NSE:PPLPHARMA,NSE:PRICOLLTD,NSE:PRIVISCL,NSE:PVRINOX,NSE:RAIN,NSE:RBLBANK,NSE:SKIPPER,NSE:SUDARSCHEM,NSE:TEJASNET,NSE:UNIONBANK,NSE:VARROC,NSE:VENUSPIPES,NSE:WABAG,NSE:WOCKPHARMA,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ACE,NSE:ACMESOLAR,NSE:AEROFLEX,NSE:BALAMINES,NSE:BLUESTONE,NSE:BODALCHEM,NSE:CGCL,NSE:CONFIPET,NSE:CPPLUS,NSE:CYIENTDLM,NSE:DATAPATTNS,NSE:DEEPINDS,NSE:EBGNG,NSE:EMIL,NSE:ENGINERSIN,NSE:EXICOM,NSE:FILATEX,NSE:FINCABLES,NSE:GLENMARK,NSE:HFCL,NSE:INOXINDIA,NSE:IPCALAB,NSE:JINDRILL,NSE:KRN,NSE:KROSS,NSE:LUMAXTECH,NSE:MANINDS,NSE:MCX,NSE:NEOGEN,NSE:NEULANDLAB,NSE:QPOWER,NSE:QUADFUTURE,NSE:RAYMOND,NSE:RPEL,NSE:SHREEJISPG,NSE:WHEELS,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ANTHEM,NSE:APARINDS,NSE:AUROPHARMA,NSE:AVALON,NSE:BIRLACABLE,NSE:BOSCHLTD,NSE:CRAFTSMAN,NSE:DIACABS,NSE:DIVISLAB,NSE:DYNAMATECH,NSE:FCL,NSE:FLUOROCHEM,NSE:HEG,NSE:JINDALSAW,NSE:KABRAEXTRU,NSE:KENNAMET,NSE:LALPATHLAB,NSE:MARINE,NSE:MARKSANS,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:NAVINFLUOR,NSE:NETWEB,NSE:NRBBEARING,NSE:PNBHOUSING,NSE:RACLGEAR,NSE:RATNAVEER,NSE:RKFORGE,NSE:SETL,NSE:SHAILY,NSE:SIEMENS,NSE:SIGMAADV,NSE:SMLMAH,NSE:SOLARINDS,NSE:SSWL,NSE:STLTECH,NSE:SYRMA,NSE:TBZ,NSE:TFCILTD,NSE:UNIMECH,NSE:WELSPUNLIV,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AETHER,NSE:ATHERENERG,NSE:AZAD,NSE:BALRAMCHIN,NSE:CHENNPETRO,NSE:GLAND,NSE:IOLCP,NSE:KARURVYSYA,NSE:KTKBANK,NSE:MTARTECH,NSE:NAZARA,NSE:SHILPAMED,NSE:SOTL,NSE:TITAN,NSE:YASHO,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AKUMS,NSE:CUPID,NSE:LAURUSLABS,NSE:NYKAA,NSE:PARAS,NSE:SAILIFE,NSE:SANSERA,NSE:SKYGOLD,NSE:SONACOMS,NSE:WELCORP
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>✓ SAFE . ↗921Cr · 1631Cr . ↓CMF7d</sub> | 3104.10 | -3.3% | +76.5% | 0d | SMA-OK | RS-OK | +5.11% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>⚠ CAUTION . →294Cr · 318Cr . ↓CMF0d</sub> | 1020.80 | -11.2% | +38.2% | 0d | SMA-OK | RS-OK | +1.17% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>✓ SAFE . ↗589Cr · 962Cr . ↑CMF1d</sub> | 1765.20 | -6.3% | +35.4% | 0d | SMA-OK | RS-OK | +3.23% |
| [GVT&D](https://in.tradingview.com/chart/?symbol=NSE:GVT&D)<br><sub>✓ SAFE . ↗550Cr · 503Cr . ↑CMF1d</sub> | 4656.00 | -15.9% | +82.0% | 0d | SMA-OK | RS-OK | -1.98% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>✓ SAFE . ↗602Cr · 703Cr . ↓CMF30d</sub> | 214.00 | -14.0% | +75.8% | 0d | SMA-OK | RS-OK | +2.69% |
| [APOLLOHOSP](https://in.tradingview.com/chart/?symbol=NSE:APOLLOHOSP)<br><sub>✓ SAFE . ↘252Cr · 323Cr . ↑CMF1d</sub> | 8935.00 | -1.3% | +31.5% | 0d | SMA-OK | RS-OK | +1.10% |
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO)<br><sub>✓ SAFE . ↗288Cr · 0.0Cr . ↑CMF0d</sub> | 422.25 | -6.2% | +131.8% | 1d | SMA-OK | RS-OK | +0.00% |
| [KIRLOSIND](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSIND)<br><sub>✓ SAFE . ↗26Cr · 0.0Cr . ↑CMF1d</sub> | 3828.30 | -11.2% | +54.8% | 1d | SMA-OK | RS-OK | +0.00% |
| [ANGELONE](https://in.tradingview.com/chart/?symbol=NSE:ANGELONE)<br><sub>✓ SAFE . →207Cr · 0.0Cr . ↓CMF6d</sub> | 305.00 | -14.0% | +43.5% | 1d | SMA-OK | RS-OK | +0.00% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>✓ SAFE . →117Cr · 0.0Cr . ↑CMF5d</sub> | 1353.60 | -4.5% | +130.2% | 1d | SMA-OK | RS-OK | +0.00% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>✓ SAFE . →95Cr · 0.0Cr . ↑CMF0d</sub> | 3383.70 | -8.4% | +156.8% | 1d | SMA-OK | RS-OK | +0.00% |
| [MIDHANI](https://in.tradingview.com/chart/?symbol=NSE:MIDHANI)<br><sub>✓ SAFE . ↗222Cr · 0.0Cr . ↑CMF22d</sub> | 447.40 | -6.2% | +65.4% | 1d | SMA-OK | RS-OK | +0.00% |
| [JAMNAAUTO](https://in.tradingview.com/chart/?symbol=NSE:JAMNAAUTO)<br><sub>✓ SAFE . ↗29Cr · 0.0Cr . ↑CMF4d</sub> | 135.46 | -8.6% | +48.5% | 1d | SMA-OK | RS-OK | +0.00% |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL)<br><sub>✓ SAFE . ↗28Cr · 0.0Cr . ↑CMF1d</sub> | 3556.10 | -5.2% | +52.5% | 1d | SMA-OK | RS-OK | +0.00% |
| [CGPOWER](https://in.tradingview.com/chart/?symbol=NSE:CGPOWER)<br><sub>✓ SAFE . ↗281Cr · 312Cr . ↑CMF25d</sub> | 925.30 | -5.2% | +74.4% | 3d | SMA-OK | RS-OK | +1.60% |
| [UNIONBANK](https://in.tradingview.com/chart/?symbol=NSE:UNIONBANK)<br><sub>✓ SAFE . →151Cr · 125Cr . ↓CMF0d</sub> | 182.67 | -9.7% | +44.0% | 3d | SMA-OK | RS-OK | -0.30% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . ↗113Cr · 0.0Cr . ↓CMF15d</sub> | 1237.10 | -1.4% | +34.7% | 3d | SMA-OK | RS-OK | +0.00% |
| [SUDARSCHEM](https://in.tradingview.com/chart/?symbol=NSE:SUDARSCHEM)<br><sub>✓ SAFE . ↘49Cr · 0.0Cr . ↑CMF21d</sub> | 1248.20 | -18.1% | +67.0% | 3d | SMA-OK | RS-OK | +0.00% |
| [WABAG](https://in.tradingview.com/chart/?symbol=NSE:WABAG)<br><sub>✓ SAFE . →183Cr · 0.0Cr . ↑CMF4d</sub> | 2277.90 | 0.0% | +117.1% | 4d | SMA-OK | RS-OK | +0.00% |
| [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA)<br><sub>✓ SAFE . ↗83Cr · 0.0Cr . ↑CMF1d</sub> | 343.15 | -2.3% | +46.5% | 4d | SMA-OK | RS-OK | +0.00% |
| [ABSLAMC](https://in.tradingview.com/chart/?symbol=NSE:ABSLAMC)<br><sub>⚠ CAUTION . ↗28Cr · 0.0Cr . ↑CMF15d</sub> | 1109.90 | -7.4% | +54.8% | 4d | SMA-OK | RS-OK | +0.00% |
| [MOTILALOFS](https://in.tradingview.com/chart/?symbol=NSE:MOTILALOFS)<br><sub>✓ SAFE . ↘69Cr · 0.0Cr . ↑CMF16d</sub> | 1026.50 | -5.9% | +63.4% | 4d | SMA-OK | RS-OK | +0.00% |
| [IONEXCHANG](https://in.tradingview.com/chart/?symbol=NSE:IONEXCHANG)<br><sub>✓ SAFE . ↗46Cr · 0.0Cr . ↑CMF6d</sub> | 445.70 | -4.8% | +40.5% | 4d | SMA-OK | RS-OK | +0.00% |
| [PRICOLLTD](https://in.tradingview.com/chart/?symbol=NSE:PRICOLLTD)<br><sub>✓ SAFE . →24Cr · 0.0Cr . ↓CMF1d</sub> | 761.40 | -5.6% | +50.2% | 4d | SMA-OK | RS-OK | +0.00% |
| [INDNIPPON](https://in.tradingview.com/chart/?symbol=NSE:INDNIPPON)<br><sub>✓ SAFE . ↗67Cr · 0.0Cr . ↓CMF2d</sub> | 1358.90 | -0.7% | +100.1% | 4d | SMA-OK | RS-OK | +0.00% |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE)<br><sub>✓ SAFE . ↗517Cr · 0.0Cr . ↑CMF3d</sub> | 825.80 | -2.2% | +58.2% | 5d | SMA-OK | RS-OK | +0.00% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>✓ SAFE . ↗103Cr · 0.0Cr . ↑CMF1d</sub> | 211.35 | -6.7% | +58.6% | 5d | SMA-OK | RS-OK | +0.00% |
| [VARROC](https://in.tradingview.com/chart/?symbol=NSE:VARROC)<br><sub>✓ SAFE . ↗39Cr · 0.0Cr . ↑CMF2d</sub> | 872.00 | -1.4% | +86.6% | 5d | SMA-OK | RS-OK | +0.00% |
| [GRANULES](https://in.tradingview.com/chart/?symbol=NSE:GRANULES)<br><sub>✓ SAFE . ↗174Cr · 0.0Cr . ↑CMF2d</sub> | 909.30 | 0.0% | +76.7% | 6d | SMA-OK | RS-OK | +0.00% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>✓ SAFE . ↗786Cr · 0.0Cr . ↑CMF8d</sub> | 1139.35 | -2.6% | +216.9% | 6d | SMA-OK | RS-OK | +0.00% |
| [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO)<br><sub>✓ SAFE . ↗153Cr · 0.0Cr . ↑CMF7d</sub> | 84.23 | 0.0% | +172.0% | 6d | SMA-OK | RS-OK | +0.00% |
| [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK)<br><sub>✓ SAFE . ↗205Cr · 0.0Cr . ↑CMF23d</sub> | 412.55 | -1.4% | +56.0% | 6d | SMA-OK | RS-OK | +0.00% |
| [NOVARTIND](https://in.tradingview.com/chart/?symbol=NSE:NOVARTIND)<br><sub>✓ SAFE . ↗101Cr · 0.0Cr . ↑CMF4d</sub> | 2391.30 | -1.5% | +349.7% | 6d | SMA-OK | RS-OK | +0.00% |
| [RAIN](https://in.tradingview.com/chart/?symbol=NSE:RAIN)<br><sub>✓ SAFE . ↗105Cr · 0.0Cr . ↓CMF26d</sub> | 215.97 | -11.1% | +112.8% | 6d | SMA-OK | RS-OK | +0.00% |
| [VENUSPIPES](https://in.tradingview.com/chart/?symbol=NSE:VENUSPIPES)<br><sub>✓ SAFE . ↗56Cr · 0.0Cr . ↑CMF5d</sub> | 2020.10 | 0.0% | +126.0% | 6d | SMA-OK | RS-OK | +0.00% |
| [HONASA](https://in.tradingview.com/chart/?symbol=NSE:HONASA)<br><sub>✓ SAFE . ↘34Cr · 0.0Cr . ↓CMF1d</sub> | 471.15 | -6.3% | +83.8% | 6d | SMA-OK | RS-OK | +0.00% |
| [NIACL](https://in.tradingview.com/chart/?symbol=NSE:NIACL)<br><sub>✓ SAFE . ↗380Cr · 0.0Cr . ↑CMF8d</sub> | 198.39 | -14.2% | +68.4% | 7d | SMA-OK | RS-OK | +0.00% |
| [TEJASNET](https://in.tradingview.com/chart/?symbol=NSE:TEJASNET)<br><sub>✓ SAFE . →294Cr · 0.0Cr . ↓CMF5d</sub> | 552.65 | -12.6% | +86.6% | 7d | SMA-OK | RS-OK | +0.00% |
| [JINDWORLD](https://in.tradingview.com/chart/?symbol=NSE:JINDWORLD)<br><sub>✓ SAFE . ↗352Cr · 0.0Cr . ↑CMF9d</sub> | 52.88 | -9.6% | +192.2% | 7d | SMA-OK | RS-OK | +0.00% |
| [MAHSEAMLES](https://in.tradingview.com/chart/?symbol=NSE:MAHSEAMLES)<br><sub>✓ SAFE . ↗44Cr · 0.0Cr . ↑CMF2d</sub> | 728.90 | 0.0% | +43.9% | 7d | SMA-OK | RS-OK | +0.00% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>✓ SAFE . →330Cr · 361Cr . ↑CMF18d</sub> | 433.35 | -2.1% | +105.3% | 8d | SMA-OK | RS-OK | +2.65% |
| [WOCKPHARMA](https://in.tradingview.com/chart/?symbol=NSE:WOCKPHARMA)<br><sub>✓ SAFE . ↗319Cr · 0.0Cr . ↑CMF5d</sub> | 2179.40 | -3.1% | +98.1% | 8d | SMA-OK | RS-OK | +0.00% |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>⚠ CAUTION . →341Cr · 271Cr . ↑CMF23d</sub> | 3295.00 | -2.5% | +30.2% | 8d | SMA-OK | RS-OK | -0.36% |
| [EDELWEISS](https://in.tradingview.com/chart/?symbol=NSE:EDELWEISS)<br><sub>✓ SAFE . ↗160Cr · 0.0Cr . ↑CMF4d</sub> | 132.43 | -4.6% | +32.9% | 8d | SMA-OK | RS-OK | +0.00% |
| [SKIPPER](https://in.tradingview.com/chart/?symbol=NSE:SKIPPER)<br><sub>✓ SAFE . ↗121Cr · 0.0Cr . ↑CMF18d</sub> | 551.55 | -8.8% | +66.9% | 8d | SMA-OK | RS-OK | +0.00% |
| [MAHABANK](https://in.tradingview.com/chart/?symbol=NSE:MAHABANK)<br><sub>✓ SAFE . →139Cr · 0.0Cr . ↓CMF4d</sub> | 84.20 | -10.3% | +56.0% | 10d | SMA-OK | RS-OK | +0.00% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . →75Cr · 0.0Cr . ↑CMF6d</sub> | 691.75 | -3.0% | +209.6% | 11d | SMA-OK | RS-OK | +0.00% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . ↘76Cr · 0.0Cr . ↑CMF2d</sub> | 3825.50 | -1.9% | +204.9% | 11d | SMA-OK | RS-OK | +0.00% |
| [CGCL](https://in.tradingview.com/chart/?symbol=NSE:CGCL)<br><sub>✓ SAFE . ↘131Cr · 0.0Cr . ↑CMF14d</sub> | 266.00 | -5.0% | +75.0% | 11d | SMA-OK | RS-OK | +0.00% |
| [CONFIPET](https://in.tradingview.com/chart/?symbol=NSE:CONFIPET)<br><sub>✓ SAFE . ↗41Cr · 0.0Cr . ↑CMF3d</sub> | 89.22 | -1.6% | +209.7% | 11d | SMA-OK | RS-OK | +0.00% |
| [BALAMINES](https://in.tradingview.com/chart/?symbol=NSE:BALAMINES)<br><sub>✓ SAFE . →62Cr · 0.0Cr . ↑CMF13d</sub> | 2276.50 | -11.3% | +133.0% | 11d | SMA-OK | RS-OK | +0.00% |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE)<br><sub>✓ SAFE . ↘30Cr · 0.0Cr . ↑CMF28d</sub> | 1129.00 | -4.7% | +50.7% | 11d | SMA-OK | RS-OK | +0.00% |
| [EXICOM](https://in.tradingview.com/chart/?symbol=NSE:EXICOM)<br><sub>✓ SAFE . ↗38Cr · 0.0Cr . ↑CMF6d</sub> | 182.28 | -1.1% | +139.0% | 12d | SMA-OK | RS-OK | +0.00% |
| [WHEELS](https://in.tradingview.com/chart/?symbol=NSE:WHEELS)<br><sub>✓ SAFE . ↗329Cr · 0.0Cr . ↑CMF12d</sub> | 2230.10 | -7.1% | +212.3% | 13d | SMA-OK | RS-OK | +0.00% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>✓ SAFE . ↘77Cr · 0.0Cr . ↑CMF13d</sub> | 2246.60 | -2.1% | +109.3% | 13d | SMA-OK | RS-OK | +0.00% |
| [RPEL](https://in.tradingview.com/chart/?symbol=NSE:RPEL)<br><sub>✓ SAFE . →25Cr · 0.0Cr . ↑CMF22d</sub> | 1845.20 | -2.1% | +225.8% | 13d | SMA-OK | RS-OK | +0.00% |
| [QUADFUTURE](https://in.tradingview.com/chart/?symbol=NSE:QUADFUTURE)<br><sub>✓ SAFE . ↘70Cr · 0.0Cr . ↑CMF16d</sub> | 478.50 | 0.0% | +89.4% | 15d | SMA-OK | RS-OK | +0.00% |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>✓ SAFE . ↘44Cr · 0.0Cr . ↑CMF23d</sub> | 633.25 | -6.6% | +42.2% | 16d | SMA-OK | RS-OK | +0.00% |
| [BODALCHEM](https://in.tradingview.com/chart/?symbol=NSE:BODALCHEM)<br><sub>✓ SAFE . ↗136Cr · 0.0Cr . ↑CMF18d</sub> | 172.40 | -6.3% | +296.8% | 16d | SMA-OK | RS-OK | +0.00% |
| [BLUESTONE](https://in.tradingview.com/chart/?symbol=NSE:BLUESTONE)<br><sub>✓ SAFE . →61Cr · 0.0Cr . ↑CMF1d</sub> | 890.35 | -0.5% | +120.7% | 16d | SMA-OK | RS-OK | +0.00% |
| [NEULANDLAB](https://in.tradingview.com/chart/?symbol=NSE:NEULANDLAB)<br><sub>✓ SAFE . →91Cr · 0.0Cr . ↓CMF0d</sub> | 23535.00 | -1.9% | +103.7% | 16d | SMA-OK | RS-OK | +0.00% |
| [GLENMARK](https://in.tradingview.com/chart/?symbol=NSE:GLENMARK)<br><sub>✓ SAFE . ↘93Cr · 0.0Cr . ↑CMF17d</sub> | 2419.20 | -3.8% | +33.6% | 16d | SMA-OK | RS-OK | +0.00% |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>⚠ CAUTION . ↘30Cr · 0.0Cr . ↓CMF0d</sub> | 1968.50 | -1.0% | +55.2% | 16d | SMA-OK | RS-OK | +0.00% |
| [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX)<br><sub>✓ SAFE . ↗42Cr · 0.0Cr . ↑CMF30d</sub> | 87.41 | 0.0% | +136.9% | 17d | SMA-OK | RS-OK | +0.00% |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN)<br><sub>✓ SAFE . ↗234Cr · 0.0Cr . ↑CMF28d</sub> | 268.95 | -4.6% | +63.4% | 17d | SMA-OK | RS-OK | +0.00% |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL)<br><sub>✓ SAFE . ↗46Cr · 0.0Cr . ↑CMF2d</sub> | 188.38 | -2.7% | +120.1% | 17d | SMA-OK | RS-OK | +0.00% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS)<br><sub>✓ SAFE . ↗31Cr · 0.0Cr . ↑CMF3d</sub> | 239.07 | 0.0% | +51.0% | 18d | SMA-OK | RS-OK | +0.00% |
| [DEEPINDS](https://in.tradingview.com/chart/?symbol=NSE:DEEPINDS)<br><sub>✓ SAFE . ↗52Cr · 0.0Cr . ↑CMF30d</sub> | 774.40 | -5.4% | +133.6% | 19d | SMA-OK | RS-OK | +0.00% |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>✓ SAFE . ↘66Cr · 0.0Cr . ↑CMF19d</sub> | 402.30 | -3.8% | +102.2% | 20d | SMA-OK | RS-OK | +0.00% |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH)<br><sub>✓ SAFE . →26Cr · 0.0Cr . ↑CMF1d</sub> | 1993.70 | -4.1% | +86.0% | 20d | SMA-OK | RS-OK | +0.00% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↗628Cr · 0.0Cr . ↑CMF24d</sub> | 1002.80 | 0.0% | +211.6% | 21d | SMA-OK | RS-OK | +0.00% |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . ↘568Cr · 0.0Cr . ↑CMF23d</sub> | 3276.00 | -4.8% | +116.4% | 21d | SMA-OK | RS-OK | +0.00% |
| [FINCABLES](https://in.tradingview.com/chart/?symbol=NSE:FINCABLES)<br><sub>✓ SAFE . ↗224Cr · 0.0Cr . ↑CMF3d</sub> | 1424.00 | 0.0% | +100.3% | 21d | SMA-OK | RS-OK | +0.00% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>✓ SAFE . ↗158Cr · 0.0Cr . ↑CMF12d</sub> | 866.10 | -1.2% | +178.9% | 21d | SMA-OK | RS-OK | +0.00% |
| [DATAPATTNS](https://in.tradingview.com/chart/?symbol=NSE:DATAPATTNS)<br><sub>✓ SAFE . ↘316Cr · 0.0Cr . ↑CMF4d</sub> | 4829.20 | -2.1% | +121.3% | 21d | SMA-OK | RS-OK | +0.00% |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>✓ SAFE . ↘39Cr · 0.0Cr . ↓CMF30d</sub> | 2373.00 | -0.7% | +142.2% | 21d | SMA-OK | RS-OK | +0.00% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>✓ SAFE . ↘68Cr · 0.0Cr . ↑CMF23d</sub> | 563.95 | -1.7% | +255.1% | 21d | SMA-OK | RS-OK | +0.00% |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER)<br><sub>✓ SAFE . →38Cr · 0.0Cr . ↓CMF0d</sub> | 1426.50 | -6.1% | +139.7% | 21d | SMA-OK | RS-OK | +0.00% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>✓ SAFE . →78Cr · 0.0Cr . ↑CMF14d</sub> | 904.40 | -7.4% | +232.1% | 21d | SMA-OK | RS-OK | +0.00% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>✓ SAFE . ↗70Cr · 0.0Cr . ↑CMF24d</sub> | 679.65 | 0.0% | +180.2% | 21d | SMA-OK | RS-OK | +0.00% |
| [KRN](https://in.tradingview.com/chart/?symbol=NSE:KRN)<br><sub>✓ SAFE . ↘31Cr · 0.0Cr . ↑CMF28d</sub> | 1593.60 | -4.0% | +166.4% | 21d | SMA-OK | RS-OK | +0.00% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↘85Cr · 0.0Cr . ↑CMF1d</sub> | 207.68 | -2.0% | +91.7% | 22d | SMA-OK | RS-OK | +0.00% |
| [HEG](https://in.tradingview.com/chart/?symbol=NSE:HEG)<br><sub>✓ SAFE . →118Cr · 187Cr . ↑CMF15d</sub> | 728.25 | -1.5% | +52.6% | 22d | SMA-OK | RS-OK | +2.94% |
| [TBZ](https://in.tradingview.com/chart/?symbol=NSE:TBZ)<br><sub>✓ SAFE . ↗332Cr · 0.0Cr . ↑CMF13d</sub> | 526.30 | -5.2% | +372.0% | 23d | SMA-OK | RS-OK | +0.00% |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE)<br><sub>→40Cr · 0.0Cr . ↑CMF30d</sub> | 419.15 | -3.1% | +176.3% | 23d | SMA-OK | RS-OK | +0.00% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>✓ SAFE . →183Cr · 132Cr . ↑CMF25d</sub> | 48870.00 | -2.3% | +70.0% | 24d | SMA-OK | RS-OK | +0.17% |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY)<br><sub>✓ SAFE . ↗44Cr · 0.0Cr . ↑CMF3d</sub> | 3279.50 | -5.2% | +80.0% | 25d | SMA-OK | RS-OK | +0.00% |
| [RACLGEAR](https://in.tradingview.com/chart/?symbol=NSE:RACLGEAR)<br><sub>✓ SAFE . ↗26Cr · 0.0Cr . ↑CMF1d</sub> | 1756.70 | 0.0% | +93.5% | 26d | SMA-OK | RS-OK | +0.00% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>✓ SAFE . →92Cr · 0.0Cr . ↑CMF30d</sub> | 1178.90 | -0.5% | +57.0% | 26d | SMA-OK | RS-OK | +0.00% |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH)<br><sub>✓ SAFE . →19Cr · 0.0Cr . ↑CMF1d</sub> | 12097.00 | -3.5% | +81.1% | 26d | SMA-OK | RS-OK | +0.00% |
| [JINDALSAW](https://in.tradingview.com/chart/?symbol=NSE:JINDALSAW)<br><sub>✓ SAFE . ↘64Cr · 0.0Cr . ↑CMF30d</sub> | 311.95 | -1.7% | +101.7% | 26d | SMA-OK | RS-OK | +0.00% |
| [KENNAMET](https://in.tradingview.com/chart/?symbol=NSE:KENNAMET)<br><sub>✓ SAFE . ↘18Cr · 0.0Cr . ↑CMF26d</sub> | 4682.40 | -6.9% | +126.9% | 26d | SMA-OK | RS-OK | +0.00% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>✓ SAFE . →81Cr · 0.0Cr . ↓CMF6d</sub> | 940.90 | -1.8% | +60.1% | 27d | SMA-OK | RS-OK | +0.00% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>✓ SAFE . ↘56Cr · 0.0Cr . ↑CMF24d</sub> | 468.15 | 0.0% | +343.1% | 28d | SMA-OK | RS-OK | +0.00% |
| [FCL](https://in.tradingview.com/chart/?symbol=NSE:FCL)<br><sub>✓ SAFE . ↗155Cr · 0.0Cr . ↑CMF16d</sub> | 57.72 | -1.7% | +200.0% | 28d | SMA-OK | RS-OK | +0.00% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . ↗503Cr · 354Cr . ↑CMF30d</sub> | 9443.00 | -1.4% | +66.0% | 29d | SMA-OK | RS-OK | -1.38% |
| [SOLARINDS](https://in.tradingview.com/chart/?symbol=NSE:SOLARINDS)<br><sub>✓ SAFE . →401Cr · 204Cr . ↑CMF30d</sub> | 22330.00 | -0.6% | +89.7% | 29d | SMA-OK | RS-OK | -0.56% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↘220Cr · 0.0Cr . ↑CMF29d</sub> | 115.78 | -2.6% | +243.8% | 29d | SMA-OK | RS-OK | +0.00% |
| [SIEMENS](https://in.tradingview.com/chart/?symbol=NSE:SIEMENS)<br><sub>✓ SAFE . ↘119Cr · 146Cr . ↓CMF1d</sub> | 3947.70 | -3.7% | +38.6% | 29d | SMA-OK | RS-OK | -0.09% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>⚠ CAUTION . ↗38Cr · 0.0Cr . ↑CMF3d</sub> | 1909.00 | -3.0% | +46.0% | 29d | SMA-OK | RS-OK | +0.00% |
| [SMLMAH](https://in.tradingview.com/chart/?symbol=NSE:SMLMAH)<br><sub>✓ SAFE . ↗111Cr · 0.0Cr . ↑CMF6d</sub> | 6583.00 | 0.0% | +138.1% | 30d | SMA-OK | RS-OK | +0.00% |
| [NETWEB](https://in.tradingview.com/chart/?symbol=NSE:NETWEB)<br><sub>✓ SAFE . ↘641Cr · 0.0Cr . ↓CMF6d</sub> | 5027.00 | -10.2% | +76.9% | 31d | SMA-OK | RS-OK | +0.00% |
| [APARINDS](https://in.tradingview.com/chart/?symbol=NSE:APARINDS)<br><sub>✓ SAFE . ↘186Cr · 0.0Cr . ↑CMF2d</sub> | 17500.00 | -2.8% | +151.2% | 31d | SMA-OK | RS-OK | +0.00% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>✓ SAFE . ↗332Cr · 0.0Cr . ↑CMF7d</sub> | 1589.30 | -3.0% | +148.3% | 31d | SMA-OK | RS-OK | +0.00% |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS)<br><sub>✓ SAFE . →82Cr · 0.0Cr . ↓CMF1d</sub> | 329.40 | -1.9% | +110.0% | 31d | SMA-OK | RS-OK | +0.00% |
| [NRBBEARING](https://in.tradingview.com/chart/?symbol=NSE:NRBBEARING)<br><sub>✓ SAFE . ↗24Cr · 0.0Cr . ↑CMF26d</sub> | 514.65 | -0.3% | +138.0% | 31d | SMA-OK | RS-OK | +0.00% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . →103Cr · 0.0Cr . ↑CMF6d</sub> | 8543.50 | -2.6% | +87.7% | 32d | SMA-OK | RS-OK | +0.00% |
| [BIRLACABLE](https://in.tradingview.com/chart/?symbol=NSE:BIRLACABLE)<br><sub>✓ SAFE . ↗19Cr · 0.0Cr . ↑CMF30d</sub> | 392.35 | 0.0% | +276.2% | 32d | SMA-OK | RS-OK | +0.00% |
| [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON)<br><sub>⚠ CAUTION . →198Cr · 93Cr . ↓CMF3d</sub> | 164.17 | -3.8% | +74.1% | 33d | SMA-OK | RS-OK | +0.20% |
| [AVALON](https://in.tradingview.com/chart/?symbol=NSE:AVALON)<br><sub>✓ SAFE . →112Cr · 0.0Cr . ↑CMF28d</sub> | 2264.50 | -4.6% | +185.3% | 34d | SMA-OK | RS-OK | +0.00% |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>✓ SAFE . →69Cr · 0.0Cr . ↓CMF20d</sub> | 4773.20 | -0.3% | +60.7% | 34d | SMA-OK | RS-OK | +0.00% |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH)<br><sub>✓ SAFE . ↗40Cr · 0.0Cr . ↑CMF4d</sub> | 1610.00 | -1.2% | +127.9% | 35d | SMA-OK | RS-OK | +0.00% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>⚠ CAUTION . ↘108Cr · 0.0Cr . ↑CMF29d</sub> | 1679.80 | -2.2% | +56.9% | 36d | SMA-OK | RS-OK | +0.00% |
| [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN)<br><sub>✓ SAFE . →56Cr · 0.0Cr . ↑CMF30d</sub> | 11669.00 | -1.5% | +81.6% | 36d | SMA-OK | RS-OK | +0.00% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>✓ SAFE . ↘48Cr · 0.0Cr . ↓CMF10d</sub> | 711.20 | -5.8% | +53.7% | 36d | SMA-OK | RS-OK | +0.00% |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS)<br><sub>✓ SAFE . ↗363Cr · 101Cr . ↑CMF9d</sub> | 322.85 | -4.3% | +173.7% | 37d | SMA-OK | RS-OK | -0.35% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . ↘92Cr · 0.0Cr . ↑CMF30d . DEL56%(T-1)</sub> | 288.30 | -7.2% | +119.6% | 38d | SMA-OK | RS-OK | +0.00% |
| [KABRAEXTRU](https://in.tradingview.com/chart/?symbol=NSE:KABRAEXTRU)<br><sub>✓ SAFE . →26Cr · 0.0Cr . ↑CMF30d</sub> | 723.15 | 0.0% | +296.1% | 38d | SMA-OK | RS-OK | +0.00% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↗156Cr · 0.0Cr . ↑CMF9d</sub> | 370.65 | -0.8% | +117.5% | 40d | SMA-OK | RS-OK | +0.00% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>✓ SAFE . ↘33Cr · 72Cr . ↑CMF0d</sub> | 763.65 | 0.0% | +710.9% | 40d | SMA-OK | RS-OK | +5.00% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . ↘102Cr · 0.0Cr . ↑CMF30d</sub> | 141.49 | -3.6% | +156.1% | 41d | SMA-OK | RS-OK | +0.00% |
| [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP)<br><sub>✓ SAFE . →90Cr · 0.0Cr . ↑CMF13d</sub> | 194.31 | -8.8% | +184.9% | 44d | SMA-OK | RS-OK | +0.00% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>✓ SAFE . ↘56Cr · 0.0Cr . ↑CMF30d</sub> | 325.35 | -4.3% | +90.5% | 46d | SMA-OK | RS-OK | +0.00% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>⚠ CAUTION . ↘39Cr · 0.0Cr . ↓CMF19d</sub> | 333.80 | -5.8% | +62.3% | 46d | SMA-OK | RS-OK | +0.00% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↗235Cr · 0.0Cr . ↑CMF27d</sub> | 2922.30 | -3.4% | +83.0% | 47d | SMA-OK | RS-OK | +0.00% |
| [TITAN](https://in.tradingview.com/chart/?symbol=NSE:TITAN)<br><sub>⚠ CAUTION . ↗289Cr · 235Cr . ↑CMF30d</sub> | 4985.50 | -3.6% | +49.8% | 48d | SMA-OK | RS-OK | -0.03% |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>✓ SAFE . ↘230Cr · 0.0Cr . ↑CMF30d</sub> | 691.40 | -9.9% | +73.8% | 48d | SMA-OK | RS-OK | +0.00% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . ↘41Cr · 0.0Cr . ↑CMF30d</sub> | 370.30 | -1.2% | +70.1% | 48d | SMA-OK | RS-OK | +0.00% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↗368Cr · 0.0Cr . ↓CMF0d</sub> | 1572.90 | -3.3% | +117.4% | 49d | SMA-OK | RS-OK | +0.00% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>✓ SAFE . ↘80Cr · 0.0Cr . ↓CMF2d</sub> | 2849.10 | -1.8% | +108.5% | 51d | SMA-OK | RS-OK | +0.00% |
| [SOTL](https://in.tradingview.com/chart/?symbol=NSE:SOTL)<br><sub>✓ SAFE . ↗155Cr · 0.0Cr . ↑CMF9d</sub> | 716.25 | -8.4% | +148.6% | 52d | SMA-OK | RS-OK | +0.00% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . →769Cr · 0.0Cr . ↑CMF30d</sub> | 1656.00 | -4.0% | +206.7% | 56d | SMA-OK | RS-OK | +0.00% |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>✓ SAFE . ↘104Cr · 0.0Cr . ↑CMF7d</sub> | 961.15 | -0.3% | +260.0% | 56d | SMA-OK | RS-OK | +0.00% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>✓ SAFE . ↘31Cr · 0.0Cr . ↑CMF2d</sub> | 1674.70 | -1.3% | +129.2% | 56d | SMA-OK | RS-OK | +0.00% |
| [YASHO](https://in.tradingview.com/chart/?symbol=NSE:YASHO)<br><sub>✓ SAFE . ↘14Cr · 0.0Cr . ↓CMF0d</sub> | 4187.50 | -14.8% | +259.2% | 56d | SMA-OK | RS-OK | +0.00% |
| [MTARTECH](https://in.tradingview.com/chart/?symbol=NSE:MTARTECH)<br><sub>✓ SAFE . ↗2251Cr · 944Cr . ↑CMF8d</sub> | 7777.00 | -7.1% | +457.1% | 58d | SMA-OK | RS-OK | -4.25% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . →130Cr · 0.0Cr . ↑CMF22d</sub> | 344.50 | -1.4% | +49.4% | 66d | SMA-OK | RS-OK | +0.00% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>✓ SAFE . →26Cr · 0.0Cr . ↓CMF10d</sub> | 776.35 | -0.5% | +87.5% | 71d | SMA-OK | RS-OK | +0.00% |
| [PARAS](https://in.tradingview.com/chart/?symbol=NSE:PARAS)<br><sub>✓ SAFE . ↘150Cr · 0.0Cr . ↓CMF0d</sub> | 1435.60 | -6.0% | +145.6% | 80d | SMA-OK | RS-OK | +0.00% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↗76Cr · 0.0Cr . ↑CMF23d</sub> | 4129.90 | -0.1% | +201.0% | 81d | SMA-OK | RS-OK | +0.00% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . ↗1042Cr · 216Cr . ↑CMF30d</sub> | 1876.70 | -3.2% | +125.5% | 84d | SMA-OK | RS-OK | +0.98% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↘96Cr · 0.0Cr . ↑CMF5d</sub> | 788.00 | -4.4% | +94.4% | 86d | SMA-OK | RS-OK | +0.00% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>✓ SAFE . ↘538Cr · 0.0Cr . ↑CMF30d</sub> | 2676.60 | -3.6% | +270.8% | 88d | SMA-OK | RS-OK | +0.00% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . ↗208Cr · 0.0Cr . ↑CMF9d</sub> | 1585.00 | -5.4% | +99.4% | 100d | SMA-OK | RS-OK | +0.00% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . →74Cr · 0.0Cr . ↑CMF2d</sub> | 827.40 | -2.4% | +214.3% | 105d | SMA-OK | RS-OK | +0.00% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↘286Cr · 0.0Cr . ↑CMF30d</sub> | 280.00 | -5.0% | +606.2% | 118d | SMA-OK | RS-OK | +0.00% |

### By Trend Age

**<2 WEEKS** (46)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABSLAMC,NSE:ACUTAAS,NSE:ADANIENT,NSE:ADANIPORTS,NSE:ADANIPOWER,NSE:AEGISLOG,NSE:ANGELONE,NSE:ANTELOPUS,NSE:APOLLO,NSE:APOLLOHOSP,NSE:BHEL,NSE:CGPOWER,NSE:EDELWEISS,NSE:GRANULES,NSE:GRAPHITE,NSE:GRASIM,NSE:GVT&D,NSE:HINDALCO,NSE:HONASA,NSE:INDNIPPON,NSE:IONEXCHANG,NSE:JAMNAAUTO,NSE:JINDWORLD,NSE:JSWINFRA,NSE:KIRLOSIND,NSE:MAHABANK,NSE:MAHSEAMLES,NSE:MIDHANI,NSE:MOTILALOFS,NSE:NIACL,NSE:NOVARTIND,NSE:PAISALO,NSE:PPLPHARMA,NSE:PRICOLLTD,NSE:PRIVISCL,NSE:PVRINOX,NSE:RAIN,NSE:RBLBANK,NSE:SKIPPER,NSE:SUDARSCHEM,NSE:TEJASNET,NSE:UNIONBANK,NSE:VARROC,NSE:VENUSPIPES,NSE:WABAG,NSE:WOCKPHARMA
```

**2-4 WEEKS** (36)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ACE,NSE:ACMESOLAR,NSE:AEROFLEX,NSE:BALAMINES,NSE:BLUESTONE,NSE:BODALCHEM,NSE:CGCL,NSE:CONFIPET,NSE:CPPLUS,NSE:CYIENTDLM,NSE:DATAPATTNS,NSE:DEEPINDS,NSE:EBGNG,NSE:EMIL,NSE:ENGINERSIN,NSE:EXICOM,NSE:FILATEX,NSE:FINCABLES,NSE:GLENMARK,NSE:HFCL,NSE:INOXINDIA,NSE:IPCALAB,NSE:JINDRILL,NSE:KRN,NSE:KROSS,NSE:LUMAXTECH,NSE:MANINDS,NSE:MCX,NSE:NEOGEN,NSE:NEULANDLAB,NSE:QPOWER,NSE:QUADFUTURE,NSE:RAYMOND,NSE:RPEL,NSE:SHREEJISPG,NSE:WHEELS
```

**1-2 MONTHS** (41)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ANTHEM,NSE:APARINDS,NSE:AUROPHARMA,NSE:AVALON,NSE:BIRLACABLE,NSE:BOSCHLTD,NSE:CRAFTSMAN,NSE:DIACABS,NSE:DIVISLAB,NSE:DYNAMATECH,NSE:FCL,NSE:FLUOROCHEM,NSE:HEG,NSE:JINDALSAW,NSE:KABRAEXTRU,NSE:KENNAMET,NSE:LALPATHLAB,NSE:MARINE,NSE:MARKSANS,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:NAVINFLUOR,NSE:NETWEB,NSE:NRBBEARING,NSE:PNBHOUSING,NSE:RACLGEAR,NSE:RATNAVEER,NSE:RKFORGE,NSE:SETL,NSE:SHAILY,NSE:SIEMENS,NSE:SIGMAADV,NSE:SMLMAH,NSE:SOLARINDS,NSE:SSWL,NSE:STLTECH,NSE:SYRMA,NSE:TBZ,NSE:TFCILTD,NSE:UNIMECH,NSE:WELSPUNLIV
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
