> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-08-27
*Generated 2026-08-27 15:51 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER) | [CONFIPET](https://in.tradingview.com/chart/?symbol=NSE:CONFIPET) |
| [BEPL](https://in.tradingview.com/chart/?symbol=NSE:BEPL) | [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS) |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS) | [DWARKESH](https://in.tradingview.com/chart/?symbol=NSE:DWARKESH) |
| [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN) | [DYCL](https://in.tradingview.com/chart/?symbol=NSE:DYCL) |
| [GNFC](https://in.tradingview.com/chart/?symbol=NSE:GNFC) | [ENRIN](https://in.tradingview.com/chart/?symbol=NSE:ENRIN) |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA) | [EPL](https://in.tradingview.com/chart/?symbol=NSE:EPL) |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL) | [FCL](https://in.tradingview.com/chart/?symbol=NSE:FCL) |
| [JTLIND](https://in.tradingview.com/chart/?symbol=NSE:JTLIND) | [GOKULAGRO](https://in.tradingview.com/chart/?symbol=NSE:GOKULAGRO) |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW) | [HAPPYFORGE](https://in.tradingview.com/chart/?symbol=NSE:HAPPYFORGE) |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA) | [ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL) |
| [OBEROIRLTY](https://in.tradingview.com/chart/?symbol=NSE:OBEROIRLTY) | [INDOBORAX](https://in.tradingview.com/chart/?symbol=NSE:INDOBORAX) |
| [QUADFUTURE](https://in.tradingview.com/chart/?symbol=NSE:QUADFUTURE) | [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB) |
| [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK) | [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB) |
| [SENORES](https://in.tradingview.com/chart/?symbol=NSE:SENORES) | [JAYNECOIND](https://in.tradingview.com/chart/?symbol=NSE:JAYNECOIND) |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY) | [JSFB](https://in.tradingview.com/chart/?symbol=NSE:JSFB) |
| [VINDHYATEL](https://in.tradingview.com/chart/?symbol=NSE:VINDHYATEL) | [LTFOODS](https://in.tradingview.com/chart/?symbol=NSE:LTFOODS) |
| [VOLTAMP](https://in.tradingview.com/chart/?symbol=NSE:VOLTAMP) | [MANAPPURAM](https://in.tradingview.com/chart/?symbol=NSE:MANAPPURAM) |
| [WOCKPHARMA](https://in.tradingview.com/chart/?symbol=NSE:WOCKPHARMA) | [MANORAMA](https://in.tradingview.com/chart/?symbol=NSE:MANORAMA) |
| [WSTCSTPAPR](https://in.tradingview.com/chart/?symbol=NSE:WSTCSTPAPR) | [MSTCLTD](https://in.tradingview.com/chart/?symbol=NSE:MSTCLTD) |
|  | [NMDC](https://in.tradingview.com/chart/?symbol=NSE:NMDC) |
|  | [PITTIENG](https://in.tradingview.com/chart/?symbol=NSE:PITTIENG) |
|  | [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA) |
|  | [PRECWIRE](https://in.tradingview.com/chart/?symbol=NSE:PRECWIRE) |
|  | [QUESS](https://in.tradingview.com/chart/?symbol=NSE:QUESS) |
|  | [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND) |
|  | [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS) |
|  | [SENCO](https://in.tradingview.com/chart/?symbol=NSE:SENCO) |
|  | [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL) |
|  | [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS) |
|  | [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH) |
|  | [WELENT](https://in.tradingview.com/chart/?symbol=NSE:WELENT) |
|  | [ZENTEC](https://in.tradingview.com/chart/?symbol=NSE:ZENTEC) |

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

**Qualifying: 116**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABB,NSE:ABCAPITAL,NSE:ACMESOLAR,NSE:AEROFLEX,NSE:ASIANENE,NSE:BALAMINES,NSE:CGCL,NSE:CPPLUS,NSE:CYIENTDLM,NSE:DATAPATTNS,NSE:DCBBANK,NSE:ENGINERSIN,NSE:FILATEX,NSE:FINCABLES,NSE:GLENMARK,NSE:GNFC,NSE:GRASIM,NSE:IFCI,NSE:INOXINDIA,NSE:JINDRILL,NSE:JTLIND,NSE:MAHABANK,NSE:MANINDS,NSE:MCX,NSE:MEDANTA,NSE:NEOGEN,NSE:NEULANDLAB,NSE:OBEROIRLTY,NSE:OMAXE,NSE:QUADFUTURE,NSE:SHYAMMETL,NSE:SKIPPER,NSE:THELEELA,NSE:VOLTAMP,NSE:WABAG,NSE:WELSPUNLIV,NSE:WOCKPHARMA,NSE:YATHARTH,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ANTHEM,NSE:APARINDS,NSE:AUBANK,NSE:BEPL,NSE:BOSCHLTD,NSE:DIVISLAB,NSE:ENTERO,NSE:HEG,NSE:HFCL,NSE:HINDALCO,NSE:JINDALSAW,NSE:JSWINFRA,NSE:KEI,NSE:KENNAMET,NSE:MARKSANS,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:NAVINFLUOR,NSE:NETWEB,NSE:PNBHOUSING,NSE:RBA,NSE:RBLBANK,NSE:ROSSTECH,NSE:SBCL,NSE:SENORES,NSE:SHAILY,NSE:SHANTIGOLD,NSE:SHRIRAMFIN,NSE:SIEMENS,NSE:SOLARINDS,NSE:SYRMA,NSE:TBZ,NSE:TVSMOTOR,NSE:VINDHYATEL,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AARTIIND,NSE:AEGISLOG,NSE:AUROPHARMA,NSE:AVALON,NSE:AZAD,NSE:BALRAMCHIN,NSE:CHENNPETRO,NSE:CRAFTSMAN,NSE:EICHERMOT,NSE:FLUOROCHEM,NSE:GLAND,NSE:IOLCP,NSE:KARURVYSYA,NSE:KTKBANK,NSE:NAZARA,NSE:OFSS,NSE:RAMRAT,NSE:RATNAVEER,NSE:RKFORGE,NSE:SIGMAADV,NSE:STLTECH,NSE:TFCILTD,NSE:TITAN,NSE:WSTCSTPAPR,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AETHER,NSE:AKUMS,NSE:ATHERENERG,NSE:KMEW,NSE:MTARTECH,NSE:NYKAA,NSE:SHILPAMED,NSE:SHRIPISTON,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:CUPID,NSE:GRWRHITECH,NSE:HONASA,NSE:LAURUSLABS,NSE:PARAS,NSE:RADICO,NSE:RRKABEL,NSE:SAILIFE,NSE:SANSERA,NSE:SKYGOLD,NSE:SONACOMS,NSE:WELCORP
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [WOCKPHARMA](https://in.tradingview.com/chart/?symbol=NSE:WOCKPHARMA)<br><sub>✓ SAFE . ↘92Cr · 237Cr . ↓CMF9d</sub> | 1962.00 | -8.9% | +78.3% | 0d | SMA-OK | RS-OK | +4.25% |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL)<br><sub>✓ SAFE . →49Cr · 216Cr . ↓CMF13d . DEL60%(T-1)</sub> | 1042.40 | -1.9% | +36.9% | 0d | SMA-OK | RS-OK | +0.18% |
| [ABB](https://in.tradingview.com/chart/?symbol=NSE:ABB)<br><sub>✓ SAFE . ↘111Cr · 87Cr . ↑CMF2d . DEL61%(T-1)</sub> | 7520.00 | -2.8% | +60.3% | 0d | SMA-OK | RS-OK | +1.29% |
| [MAHABANK](https://in.tradingview.com/chart/?symbol=NSE:MAHABANK)<br><sub>✓ SAFE . ↗129Cr · 137Cr . ↑CMF1d</sub> | 84.69 | -9.8% | +63.0% | 0d | SMA-OK | RS-OK | -1.06% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . →104Cr · 108Cr . ↓CMF29d</sub> | 3629.70 | -6.9% | +190.8% | 0d | SMA-OK | RS-OK | +2.82% |
| [CGCL](https://in.tradingview.com/chart/?symbol=NSE:CGCL)<br><sub>✓ SAFE . ↗182Cr · 99Cr . ↑CMF2d</sub> | 244.80 | -5.4% | +61.1% | 0d | SMA-OK | RS-OK | -4.51% |
| [YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH)<br><sub>✓ SAFE . →45Cr · 67Cr . ↑CMF3d</sub> | 973.05 | 0.0% | +76.7% | 0d | SMA-OK | RS-OK | +0.80% |
| [BALAMINES](https://in.tradingview.com/chart/?symbol=NSE:BALAMINES)<br><sub>✓ SAFE . ↗58Cr · 57Cr . ↑CMF1d</sub> | 2425.80 | -0.5% | +148.2% | 0d | SMA-OK | RS-OK | -0.47% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>✓ SAFE . ↗119Cr · 977Cr . ↑CMF1d</sub> | 2177.90 | 0.0% | +102.9% | 1d | SMA-OK | RS-OK | +13.04% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>✓ SAFE . ↘131Cr · 86Cr . ↑CMF20d</sub> | 413.00 | -2.8% | +50.3% | 1d | SMA-OK | RS-OK | +0.00% |
| [OBEROIRLTY](https://in.tradingview.com/chart/?symbol=NSE:OBEROIRLTY)<br><sub>✓ SAFE . ↗115Cr · 51Cr . ↑CMF0d</sub> | 1872.90 | -4.1% | +32.7% | 1d | SMA-OK | RS-OK | +0.16% |
| [GNFC](https://in.tradingview.com/chart/?symbol=NSE:GNFC)<br><sub>✓ SAFE . ↗43Cr · 28Cr . ↓CMF2d</sub> | 577.00 | -5.4% | +57.5% | 1d | SMA-OK | RS-OK | -1.24% |
| [WABAG](https://in.tradingview.com/chart/?symbol=NSE:WABAG)<br><sub>✓ SAFE . ↗172Cr · 249Cr . ↑CMF3d</sub> | 2133.90 | -3.9% | +103.4% | 3d | SMA-OK | RS-OK | -0.99% |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>⚠ CAUTION . ↗416Cr · 526Cr . ↑CMF11d</sub> | 3300.00 | -2.4% | +30.4% | 3d | SMA-OK | RS-OK | -0.24% |
| [QUADFUTURE](https://in.tradingview.com/chart/?symbol=NSE:QUADFUTURE)<br><sub>✓ SAFE . ↗172Cr · 76Cr . ↑CMF4d</sub> | 432.55 | -10.5% | +71.2% | 3d | SMA-OK | RS-OK | +5.00% |
| [DCBBANK](https://in.tradingview.com/chart/?symbol=NSE:DCBBANK)<br><sub>✓ SAFE . ↗100Cr · 211Cr . ↑CMF3d</sub> | 217.51 | 0.0% | +80.9% | 4d | SMA-OK | RS-OK | +1.72% |
| [GLENMARK](https://in.tradingview.com/chart/?symbol=NSE:GLENMARK)<br><sub>✓ SAFE . →129Cr · 110Cr . ↑CMF5d</sub> | 2460.00 | 0.0% | +35.9% | 4d | SMA-OK | RS-OK | +0.89% |
| [SKIPPER](https://in.tradingview.com/chart/?symbol=NSE:SKIPPER)<br><sub>✓ SAFE . ↗59Cr · 93Cr . ↑CMF6d</sub> | 558.10 | -2.9% | +68.9% | 4d | SMA-OK | RS-OK | +1.98% |
| [NEULANDLAB](https://in.tradingview.com/chart/?symbol=NSE:NEULANDLAB)<br><sub>✓ SAFE . ↘117Cr · 89Cr . ↓CMF15d</sub> | 23496.00 | -0.7% | +103.3% | 4d | SMA-OK | RS-OK | -0.21% |
| [JTLIND](https://in.tradingview.com/chart/?symbol=NSE:JTLIND)<br><sub>✓ SAFE . →21Cr · 55Cr . ↑CMF5d</sub> | 82.57 | -0.6% | +102.4% | 4d | SMA-OK | RS-OK | +1.93% |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>✓ SAFE . ↗148Cr · 34Cr . ↑CMF11d</sub> | 630.55 | -5.9% | +41.6% | 4d | SMA-OK | RS-OK | -0.30% |
| [ASIANENE](https://in.tradingview.com/chart/?symbol=NSE:ASIANENE)<br><sub>✓ SAFE . ↗54Cr · 27Cr . ↑CMF21d</sub> | 492.70 | 0.0% | +110.6% | 4d | SMA-OK | RS-OK | +2.96% |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN)<br><sub>✓ SAFE . →68Cr · 37Cr . ↑CMF16d</sub> | 246.96 | -5.9% | +50.1% | 5d | SMA-OK | RS-OK | -1.36% |
| [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX)<br><sub>✓ SAFE . ↘25Cr · 36Cr . ↑CMF30d</sub> | 78.31 | -9.7% | +112.2% | 5d | SMA-OK | RS-OK | +4.15% |
| [MEDANTA](https://in.tradingview.com/chart/?symbol=NSE:MEDANTA)<br><sub>✓ SAFE . →43Cr · 167Cr . ↑CMF24d</sub> | 1508.90 | 0.0% | +57.0% | 7d | SMA-OK | RS-OK | +3.43% |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA)<br><sub>✓ SAFE . →44Cr · 63Cr . ↑CMF5d</sub> | 553.80 | -1.4% | +42.1% | 8d | SMA-OK | RS-OK | +0.18% |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>✓ SAFE . ↗96Cr · 61Cr . ↑CMF7d</sub> | 386.30 | -5.6% | +94.2% | 8d | SMA-OK | RS-OK | -2.44% |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . →863Cr · 683Cr . ↑CMF11d</sub> | 3273.00 | -4.9% | +121.4% | 9d | SMA-OK | RS-OK | -2.30% |
| [IFCI](https://in.tradingview.com/chart/?symbol=NSE:IFCI)<br><sub>✓ SAFE . ↗313Cr · 376Cr . ↓CMF0d</sub> | 84.27 | -6.4% | +80.0% | 9d | SMA-OK | RS-OK | -1.37% |
| [DATAPATTNS](https://in.tradingview.com/chart/?symbol=NSE:DATAPATTNS)<br><sub>✓ SAFE . ↗495Cr · 207Cr . ↑CMF26d</sub> | 4666.70 | -4.1% | +113.8% | 9d | SMA-OK | RS-OK | -2.36% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>✓ SAFE . →90Cr · 174Cr . ↑CMF0d</sub> | 767.45 | 0.0% | +147.1% | 9d | SMA-OK | RS-OK | +9.15% |
| [FINCABLES](https://in.tradingview.com/chart/?symbol=NSE:FINCABLES)<br><sub>✓ SAFE . ↘110Cr · 88Cr . ↑CMF8d</sub> | 1291.15 | -2.9% | +81.6% | 9d | SMA-OK | RS-OK | +0.37% |
| [VOLTAMP](https://in.tradingview.com/chart/?symbol=NSE:VOLTAMP)<br><sub>✓ SAFE . ↘58Cr · 63Cr . ↑CMF0d</sub> | 11228.50 | -10.3% | +65.6% | 9d | SMA-OK | RS-OK | +2.28% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>✓ SAFE . ↗87Cr · 58Cr . ↑CMF11d</sub> | 522.10 | -2.7% | +228.8% | 9d | SMA-OK | RS-OK | -2.66% |
| [OMAXE](https://in.tradingview.com/chart/?symbol=NSE:OMAXE)<br><sub>✓ SAFE . ↗56Cr · 56Cr . ↑CMF10d</sub> | 113.38 | 0.0% | +76.9% | 9d | SMA-OK | RS-OK | +3.67% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>✓ SAFE . →53Cr · 51Cr . ↑CMF2d</sub> | 810.40 | 0.0% | +197.6% | 9d | SMA-OK | RS-OK | +1.57% |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>✓ SAFE . ↗65Cr · 29Cr . ↓CMF22d</sub> | 2230.20 | -4.2% | +127.6% | 9d | SMA-OK | RS-OK | +2.15% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↗363Cr · 49Cr . ↓CMF21d</sub> | 192.29 | 0.0% | +77.5% | 10d | SMA-OK | RS-OK | +0.87% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>✓ SAFE . ↘427Cr · 414Cr . ↑CMF11d</sub> | 1053.50 | -8.4% | +50.3% | 11d | SMA-OK | RS-OK | +1.89% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>✓ SAFE . ↗104Cr · 209Cr . ↑CMF9d</sub> | 246.05 | -9.0% | +57.1% | 11d | SMA-OK | RS-OK | -7.52% |
| [TBZ](https://in.tradingview.com/chart/?symbol=NSE:TBZ)<br><sub>✓ SAFE . →54Cr · 56Cr . ↑CMF1d</sub> | 306.10 | 0.0% | +174.5% | 11d | SMA-OK | RS-OK | +0.10% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>✓ SAFE . ↗293Cr · 133Cr . ↑CMF13d</sub> | 47965.00 | -1.6% | +66.9% | 12d | SMA-OK | RS-OK | -0.49% |
| [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA)<br><sub>✓ SAFE . ↘82Cr · 43Cr . ↑CMF17d</sub> | 100.62 | -5.5% | +75.7% | 12d | SMA-OK | RS-OK | -1.70% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>✓ SAFE . ↘277Cr · 226Cr . ↑CMF20d</sub> | 4364.50 | -2.3% | +35.6% | 13d | SMA-OK | RS-OK | -0.58% |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY)<br><sub>✓ SAFE . ↘30Cr · 38Cr . ↑CMF24d</sub> | 3289.00 | -4.9% | +80.6% | 13d | SMA-OK | RS-OK | +1.57% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘430Cr · 476Cr . ↑CMF16d</sub> | 245.84 | 0.0% | +303.3% | 14d | SMA-OK | RS-OK | +4.22% |
| [JINDALSAW](https://in.tradingview.com/chart/?symbol=NSE:JINDALSAW)<br><sub>✓ SAFE . ↗135Cr · 266Cr . ↑CMF30d</sub> | 310.25 | 0.0% | +100.6% | 14d | SMA-OK | RS-OK | +2.58% |
| [KEI](https://in.tradingview.com/chart/?symbol=NSE:KEI)<br><sub>✓ SAFE . ↘158Cr · 118Cr . ↑CMF17d</sub> | 5536.00 | -5.7% | +45.5% | 14d | SMA-OK | RS-OK | -0.07% |
| [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA)<br><sub>✓ SAFE . ↘66Cr · 96Cr . ↑CMF30d</sub> | 337.95 | -3.8% | +44.2% | 14d | SMA-OK | RS-OK | -2.03% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>✓ SAFE . ↘92Cr · 46Cr . ↑CMF30d</sub> | 1178.00 | -0.6% | +56.9% | 14d | SMA-OK | RS-OK | -0.59% |
| [KENNAMET](https://in.tradingview.com/chart/?symbol=NSE:KENNAMET)<br><sub>✓ SAFE . ↗41Cr · 29Cr . ↑CMF14d</sub> | 4515.10 | 0.0% | +124.9% | 14d | SMA-OK | RS-OK | +4.38% |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH)<br><sub>✓ SAFE . →32Cr · 28Cr . ↓CMF1d . DEL65%(T-1)</sub> | 1103.40 | -0.5% | +92.3% | 14d | SMA-OK | RS-OK | +0.31% |
| [SENORES](https://in.tradingview.com/chart/?symbol=NSE:SENORES)<br><sub>✓ SAFE . ↘30Cr · 25Cr . ↑CMF2d</sub> | 1474.60 | -4.9% | +118.9% | 14d | SMA-OK | RS-OK | -1.34% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>✓ SAFE . →65Cr · 112Cr . ↑CMF26d</sub> | 924.60 | 0.0% | +57.3% | 15d | SMA-OK | RS-OK | +0.17% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>✓ SAFE . ↘324Cr · 334Cr . ↑CMF14d</sub> | 1115.60 | -2.1% | +95.2% | 16d | SMA-OK | RS-OK | -1.27% |
| [HEG](https://in.tradingview.com/chart/?symbol=NSE:HEG)<br><sub>✓ SAFE . ↗136Cr · 42Cr . ↑CMF9d</sub> | 710.20 | -3.9% | +53.7% | 16d | SMA-OK | RS-OK | -0.47% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . ↘280Cr · 207Cr . ↑CMF23d</sub> | 8500.00 | -1.2% | +49.4% | 17d | SMA-OK | RS-OK | -1.13% |
| [SOLARINDS](https://in.tradingview.com/chart/?symbol=NSE:SOLARINDS)<br><sub>✓ SAFE . ↗426Cr · 132Cr . ↑CMF30d</sub> | 19924.00 | -2.0% | +69.2% | 17d | SMA-OK | RS-OK | +0.12% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>✓ SAFE . ↗96Cr · 224Cr . ↑CMF2d</sub> | 1753.50 | 0.0% | +84.7% | 17d | SMA-OK | RS-OK | +6.40% |
| [SIEMENS](https://in.tradingview.com/chart/?symbol=NSE:SIEMENS)<br><sub>✓ SAFE . →199Cr · 536Cr . ↑CMF20d . DEL55%(T-1)</sub> | 4098.00 | 0.0% | +43.9% | 17d | SMA-OK | RS-OK | +4.54% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↘247Cr · 141Cr . ↑CMF17d</sub> | 96.70 | -0.3% | +187.1% | 17d | SMA-OK | RS-OK | -0.29% |
| [BEPL](https://in.tradingview.com/chart/?symbol=NSE:BEPL)<br><sub>✓ SAFE . →20Cr · 34Cr . ↑CMF3d</sub> | 121.43 | -6.3% | +57.1% | 18d | SMA-OK | RS-OK | -5.39% |
| [NETWEB](https://in.tradingview.com/chart/?symbol=NSE:NETWEB)<br><sub>✓ SAFE . ↗1344Cr · 1095Cr . ↑CMF16d</sub> | 5272.20 | -5.9% | +138.8% | 19d | SMA-OK | RS-OK | +0.01% |
| [APARINDS](https://in.tradingview.com/chart/?symbol=NSE:APARINDS)<br><sub>✓ SAFE . ↘280Cr · 385Cr . ↑CMF18d</sub> | 17900.00 | -0.6% | +157.0% | 19d | SMA-OK | RS-OK | +4.91% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>✓ SAFE . ↘148Cr · 143Cr . ↓CMF20d</sub> | 1493.50 | -1.5% | +133.3% | 19d | SMA-OK | RS-OK | +1.32% |
| [AUBANK](https://in.tradingview.com/chart/?symbol=NSE:AUBANK)<br><sub>✓ SAFE . →197Cr · 98Cr . ↑CMF17d</sub> | 1091.00 | -3.3% | +57.1% | 19d | SMA-OK | RS-OK | -2.02% |
| [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK)<br><sub>✓ SAFE . ↘71Cr · 62Cr . ↑CMF11d</sub> | 385.40 | -1.8% | +53.6% | 19d | SMA-OK | RS-OK | +0.76% |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS)<br><sub>✓ SAFE . ↘165Cr · 46Cr . ↑CMF11d</sub> | 326.15 | -2.1% | +107.9% | 19d | SMA-OK | RS-OK | -1.48% |
| [VINDHYATEL](https://in.tradingview.com/chart/?symbol=NSE:VINDHYATEL)<br><sub>✓ SAFE . ↘15Cr · 38Cr . ↑CMF18d</sub> | 2530.50 | -2.0% | +159.5% | 19d | SMA-OK | RS-OK | +5.58% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . ↘98Cr · 138Cr . ↑CMF15d</sub> | 8567.50 | -1.0% | +88.2% | 20d | SMA-OK | RS-OK | +0.17% |
| [SBCL](https://in.tradingview.com/chart/?symbol=NSE:SBCL)<br><sub>✓ SAFE . ↘29Cr · 36Cr . ↑CMF17d</sub> | 1044.20 | -5.5% | +178.3% | 20d | SMA-OK | RS-OK | -0.85% |
| [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON)<br><sub>✓ SAFE . ↘192Cr · 84Cr . ↑CMF17d</sub> | 167.50 | -1.7% | +81.8% | 21d | SMA-OK | RS-OK | -1.11% |
| [AVALON](https://in.tradingview.com/chart/?symbol=NSE:AVALON)<br><sub>✓ SAFE . →133Cr · 63Cr . ↑CMF16d</sub> | 2256.60 | 0.0% | +184.3% | 22d | SMA-OK | RS-OK | +1.36% |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>✓ SAFE . ↘83Cr · 29Cr . ↓CMF8d</sub> | 4672.10 | -1.4% | +57.3% | 22d | SMA-OK | RS-OK | -1.27% |
| [RAMRAT](https://in.tradingview.com/chart/?symbol=NSE:RAMRAT)<br><sub>✓ SAFE . ↗33Cr · 216Cr . ↑CMF22d</sub> | 569.60 | 0.0% | +104.7% | 24d | SMA-OK | RS-OK | +8.76% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>✓ SAFE . ↘125Cr · 117Cr . ↑CMF17d</sub> | 1637.00 | -1.8% | +60.1% | 24d | SMA-OK | RS-OK | +0.86% |
| [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN)<br><sub>⚠ CAUTION . ↘34Cr · 51Cr . ↑CMF28d</sub> | 10898.00 | 0.0% | +69.6% | 24d | SMA-OK | RS-OK | +3.41% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>✓ SAFE . ↘51Cr · 41Cr . ↑CMF30d</sub> | 716.65 | -5.1% | +54.9% | 24d | SMA-OK | RS-OK | -2.10% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>✓ SAFE . ↘205Cr · 171Cr . ↑CMF20d</sub> | 11501.00 | -3.3% | +82.5% | 25d | SMA-OK | RS-OK | -1.90% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>✓ SAFE . ↘263Cr · 161Cr . ↑CMF20d</sub> | 8012.50 | -2.2% | +35.5% | 26d | SMA-OK | RS-OK | +0.03% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . →316Cr · 209Cr . ↑CMF23d</sub> | 294.89 | 0.0% | +124.6% | 26d | SMA-OK | RS-OK | +5.59% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . →256Cr · 149Cr . ↑CMF24d</sub> | 141.84 | 0.0% | +156.8% | 29d | SMA-OK | RS-OK | +0.60% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>✓ SAFE . ↘118Cr · 53Cr . ↑CMF7d</sub> | 1298.00 | -8.5% | +120.8% | 29d | SMA-OK | RS-OK | -2.53% |
| [AARTIIND](https://in.tradingview.com/chart/?symbol=NSE:AARTIIND)<br><sub>✓ SAFE . ↘64Cr · 29Cr . ↑CMF3d</sub> | 538.90 | -0.8% | +58.5% | 29d | SMA-OK | RS-OK | -0.75% |
| [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP)<br><sub>✓ SAFE . ↗96Cr · 200Cr . ↑CMF1d</sub> | 193.07 | 0.0% | +183.1% | 32d | SMA-OK | RS-OK | +3.80% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>⚠ CAUTION . →60Cr · 62Cr . ↓CMF7d</sub> | 346.30 | -2.3% | +70.6% | 34d | SMA-OK | RS-OK | -2.27% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>✓ SAFE . →110Cr · 48Cr . ↑CMF25d</sub> | 327.15 | -3.1% | +97.7% | 34d | SMA-OK | RS-OK | -3.12% |
| [WSTCSTPAPR](https://in.tradingview.com/chart/?symbol=NSE:WSTCSTPAPR)<br><sub>✓ SAFE . ↘13Cr · 27Cr . ↑CMF16d</sub> | 606.85 | -4.8% | +59.2% | 34d | SMA-OK | RS-OK | -0.16% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↘111Cr · 37Cr . ↑CMF15d</sub> | 2873.50 | -3.3% | +80.0% | 35d | SMA-OK | RS-OK | -1.02% |
| [TITAN](https://in.tradingview.com/chart/?symbol=NSE:TITAN)<br><sub>⚠ CAUTION . ↘324Cr · 120Cr . ↑CMF24d</sub> | 5061.50 | -1.3% | +52.1% | 36d | SMA-OK | RS-OK | -0.48% |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>✓ SAFE . ↗530Cr · 122Cr . ↑CMF18d</sub> | 649.95 | -15.3% | +63.4% | 36d | SMA-OK | RS-OK | -3.62% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . ↘44Cr · 29Cr . ↑CMF19d</sub> | 354.50 | -1.0% | +62.9% | 36d | SMA-OK | RS-OK | -0.52% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↘254Cr · 78Cr . ↑CMF30d</sub> | 1352.40 | -6.1% | +109.6% | 37d | SMA-OK | RS-OK | -1.64% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>✓ SAFE . →193Cr · 57Cr . ↑CMF10d</sub> | 2802.40 | -3.4% | +105.1% | 39d | SMA-OK | RS-OK | -0.82% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>✓ SAFE . ↘33Cr · 72Cr . ↑CMF0d</sub> | 763.65 | 0.0% | +710.9% | 40d | SMA-OK | RS-OK | +5.00% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . ↘339Cr · 412Cr . ↑CMF30d</sub> | 1495.30 | -4.7% | +258.0% | 44d | SMA-OK | RS-OK | +0.05% |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>✓ SAFE . ↘110Cr · 205Cr . ↑CMF3d</sub> | 901.85 | 0.0% | +237.8% | 44d | SMA-OK | RS-OK | +4.77% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>✓ SAFE . ↘36Cr · 34Cr . ↓CMF11d</sub> | 1677.30 | 0.0% | +129.5% | 44d | SMA-OK | RS-OK | +1.35% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>✓ SAFE . ↗47Cr · 90Cr . ↓CMF4d</sub> | 2969.00 | 0.0% | +242.5% | 54d | SMA-OK | RS-OK | +6.88% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . ↘136Cr · 52Cr . ↑CMF10d</sub> | 338.00 | -2.0% | +47.3% | 54d | SMA-OK | RS-OK | -0.59% |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON)<br><sub>✓ SAFE . ↗40Cr · 33Cr . ↑CMF30d</sub> | 4498.40 | -5.2% | +79.0% | 54d | SMA-OK | RS-OK | -2.42% |
| [MTARTECH](https://in.tradingview.com/chart/?symbol=NSE:MTARTECH)<br><sub>✓ SAFE . ↗2251Cr · 944Cr . ↑CMF8d</sub> | 7777.00 | -7.1% | +457.1% | 58d | SMA-OK | RS-OK | -4.25% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>✓ SAFE . ↘26Cr · 27Cr . ↓CMF2d</sub> | 761.20 | -1.2% | +83.8% | 59d | SMA-OK | RS-OK | -0.64% |
| [PARAS](https://in.tradingview.com/chart/?symbol=NSE:PARAS)<br><sub>✓ SAFE . ↗329Cr · 89Cr . ↑CMF16d</sub> | 1454.80 | -4.7% | +148.9% | 68d | SMA-OK | RS-OK | -2.54% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↘70Cr · 31Cr . ↑CMF11d</sub> | 3842.80 | -4.0% | +206.8% | 69d | SMA-OK | RS-OK | +0.16% |
| [RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO)<br><sub>✓ SAFE . ↘124Cr · 98Cr . ↑CMF16d</sub> | 4606.00 | -2.7% | +81.3% | 71d | SMA-OK | RS-OK | -0.17% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . ↘336Cr · 663Cr . ↑CMF30d</sub> | 1866.20 | 0.0% | +124.2% | 74d | SMA-OK | RS-OK | +3.62% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↘152Cr · 157Cr . ↑CMF30d</sub> | 819.00 | -0.6% | +102.1% | 74d | SMA-OK | RS-OK | +3.02% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>✓ SAFE . ↗1006Cr · 981Cr . ↑CMF30d</sub> | 2405.80 | -0.1% | +233.3% | 76d | SMA-OK | RS-OK | +4.30% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>✓ SAFE . ↘43Cr · 202Cr . ↓CMF15d</sub> | 7060.50 | -4.7% | +161.8% | 82d | SMA-OK | RS-OK | -0.77% |
| [RRKABEL](https://in.tradingview.com/chart/?symbol=NSE:RRKABEL)<br><sub>✓ SAFE . →114Cr · 219Cr . ↓CMF13d</sub> | 2830.10 | -3.1% | +142.4% | 84d | SMA-OK | RS-OK | +0.69% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . ↘45Cr · 64Cr . ↑CMF30d</sub> | 1488.20 | 0.0% | +87.2% | 88d | SMA-OK | RS-OK | +1.86% |
| [HONASA](https://in.tradingview.com/chart/?symbol=NSE:HONASA)<br><sub>✓ SAFE . ↗157Cr · 57Cr . ↑CMF9d</sub> | 484.85 | -3.6% | +89.2% | 92d | SMA-OK | RS-OK | +1.97% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . ↘66Cr · 38Cr . ↓CMF17d</sub> | 843.05 | -0.6% | +220.2% | 93d | SMA-OK | RS-OK | -0.60% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . →795Cr · 549Cr . ↑CMF30d</sub> | 276.65 | -6.2% | +713.7% | 106d | SMA-OK | RS-OK | -2.58% |

### By Trend Age

**<2 WEEKS** (38)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABB,NSE:ABCAPITAL,NSE:ACMESOLAR,NSE:AEROFLEX,NSE:ASIANENE,NSE:BALAMINES,NSE:CGCL,NSE:CPPLUS,NSE:CYIENTDLM,NSE:DATAPATTNS,NSE:DCBBANK,NSE:ENGINERSIN,NSE:FILATEX,NSE:FINCABLES,NSE:GLENMARK,NSE:GNFC,NSE:GRASIM,NSE:IFCI,NSE:INOXINDIA,NSE:JINDRILL,NSE:JTLIND,NSE:MAHABANK,NSE:MANINDS,NSE:MCX,NSE:MEDANTA,NSE:NEOGEN,NSE:NEULANDLAB,NSE:OBEROIRLTY,NSE:OMAXE,NSE:QUADFUTURE,NSE:SHYAMMETL,NSE:SKIPPER,NSE:THELEELA,NSE:VOLTAMP,NSE:WABAG,NSE:WELSPUNLIV,NSE:WOCKPHARMA,NSE:YATHARTH
```

**2-4 WEEKS** (34)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ANTHEM,NSE:APARINDS,NSE:AUBANK,NSE:BEPL,NSE:BOSCHLTD,NSE:DIVISLAB,NSE:ENTERO,NSE:HEG,NSE:HFCL,NSE:HINDALCO,NSE:JINDALSAW,NSE:JSWINFRA,NSE:KEI,NSE:KENNAMET,NSE:MARKSANS,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:NAVINFLUOR,NSE:NETWEB,NSE:PNBHOUSING,NSE:RBA,NSE:RBLBANK,NSE:ROSSTECH,NSE:SBCL,NSE:SENORES,NSE:SHAILY,NSE:SHANTIGOLD,NSE:SHRIRAMFIN,NSE:SIEMENS,NSE:SOLARINDS,NSE:SYRMA,NSE:TBZ,NSE:TVSMOTOR,NSE:VINDHYATEL
```

**1-2 MONTHS** (24)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AARTIIND,NSE:AEGISLOG,NSE:AUROPHARMA,NSE:AVALON,NSE:AZAD,NSE:BALRAMCHIN,NSE:CHENNPETRO,NSE:CRAFTSMAN,NSE:EICHERMOT,NSE:FLUOROCHEM,NSE:GLAND,NSE:IOLCP,NSE:KARURVYSYA,NSE:KTKBANK,NSE:NAZARA,NSE:OFSS,NSE:RAMRAT,NSE:RATNAVEER,NSE:RKFORGE,NSE:SIGMAADV,NSE:STLTECH,NSE:TFCILTD,NSE:TITAN,NSE:WSTCSTPAPR
```

**2-3 MONTHS** (8)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AETHER,NSE:AKUMS,NSE:ATHERENERG,NSE:KMEW,NSE:MTARTECH,NSE:NYKAA,NSE:SHILPAMED,NSE:SHRIPISTON
```

**3-6 MONTHS** (12)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CUPID,NSE:GRWRHITECH,NSE:HONASA,NSE:LAURUSLABS,NSE:PARAS,NSE:RADICO,NSE:RRKABEL,NSE:SAILIFE,NSE:SANSERA,NSE:SKYGOLD,NSE:SONACOMS,NSE:WELCORP
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
