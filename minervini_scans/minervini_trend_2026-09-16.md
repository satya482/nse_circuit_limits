> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-09-16
*Generated 2026-09-16 15:46 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS) | [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX) |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML) | [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER) |
| [CENTUM](https://in.tradingview.com/chart/?symbol=NSE:CENTUM) | [ASKAUTOLTD](https://in.tradingview.com/chart/?symbol=NSE:ASKAUTOLTD) |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH) | [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD) |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL) | [BIRLACABLE](https://in.tradingview.com/chart/?symbol=NSE:BIRLACABLE) |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO) | [CONFIPET](https://in.tradingview.com/chart/?symbol=NSE:CONFIPET) |
| [FOSECOIND](https://in.tradingview.com/chart/?symbol=NSE:FOSECOIND) | [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS) |
| [HAPPYFORGE](https://in.tradingview.com/chart/?symbol=NSE:HAPPYFORGE) | [ELGIEQUIP](https://in.tradingview.com/chart/?symbol=NSE:ELGIEQUIP) |
| [HONASA](https://in.tradingview.com/chart/?symbol=NSE:HONASA) | [GRANULES](https://in.tradingview.com/chart/?symbol=NSE:GRANULES) |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB) | [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH) |
| [JKPAPER](https://in.tradingview.com/chart/?symbol=NSE:JKPAPER) | [NOVARTIND](https://in.tradingview.com/chart/?symbol=NSE:NOVARTIND) |
| [JTLIND](https://in.tradingview.com/chart/?symbol=NSE:JTLIND) | [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA) |
| [KABRAEXTRU](https://in.tradingview.com/chart/?symbol=NSE:KABRAEXTRU) | [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT) |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA) | [PARAS](https://in.tradingview.com/chart/?symbol=NSE:PARAS) |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW) | [PRICOLLTD](https://in.tradingview.com/chart/?symbol=NSE:PRICOLLTD) |
| [RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO) | [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY) |
| [SMLMAH](https://in.tradingview.com/chart/?symbol=NSE:SMLMAH) | [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS) |
| [SUNDRMFAST](https://in.tradingview.com/chart/?symbol=NSE:SUNDRMFAST) | [YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH) |
| [VARROC](https://in.tradingview.com/chart/?symbol=NSE:VARROC) |  |
| [VOLTAMP](https://in.tradingview.com/chart/?symbol=NSE:VOLTAMP) |  |

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

**Qualifying: 125**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ACUTAAS,NSE:ADANIENT,NSE:ADANIPORTS,NSE:ADANIPOWER,NSE:AEGISLOG,NSE:ANTELOPUS,NSE:APOLLOHOSP,NSE:ARVIND,NSE:BEML,NSE:BHEL,NSE:CENTUM,NSE:CGPOWER,NSE:EMCURE,NSE:GRAPHITE,NSE:GRASIM,NSE:GVT&D,NSE:HINDALCO,NSE:HONASA,NSE:INDORAMA,NSE:JKPAPER,NSE:KARURVYSYA,NSE:MOTILALOFS,NSE:PAISALO,NSE:PFOCUS,NSE:PPLPHARMA,NSE:PVRINOX,NSE:RADICO,NSE:RBLBANK,NSE:STAR,NSE:SUNDRMFAST,NSE:UNIONBANK,NSE:VARROC,NSE:VENUSPIPES,NSE:WABAG,NSE:WOCKPHARMA,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ACE,NSE:ASIANENE,NSE:BLUESTONE,NSE:BODALCHEM,NSE:CGCL,NSE:DEEPINDS,NSE:EMIL,NSE:ENGINERSIN,NSE:FILATEX,NSE:FOSECOIND,NSE:GLENMARK,NSE:HFCL,NSE:IPCALAB,NSE:JTLIND,NSE:KOPRAN,NSE:NEULANDLAB,NSE:QUADFUTURE,NSE:RPEL,NSE:SHREEJISPG,NSE:TI,NSE:WELENT,NSE:WHEELS,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ACMESOLAR,NSE:ANTHEM,NSE:APARINDS,NSE:AUROPHARMA,NSE:AVALON,NSE:BOSCHLTD,NSE:CRAFTSMAN,NSE:CYIENTDLM,NSE:DIACABS,NSE:DIVISLAB,NSE:DYNAMATECH,NSE:EBGNG,NSE:ENTERO,NSE:FCL,NSE:FINCABLES,NSE:FLUOROCHEM,NSE:HEG,NSE:JINDALSAW,NSE:KABRAEXTRU,NSE:KRN,NSE:LALPATHLAB,NSE:MANINDS,NSE:MARINE,NSE:MARKSANS,NSE:MCX,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:NAVINFLUOR,NSE:NEOGEN,NSE:PNBHOUSING,NSE:QPOWER,NSE:RACLGEAR,NSE:RATNAVEER,NSE:RAYMOND,NSE:RKFORGE,NSE:ROSSTECH,NSE:SBCL,NSE:SIEMENS,NSE:SMLMAH,NSE:SOLARINDS,NSE:SSWL,NSE:STLTECH,NSE:SYRMA,NSE:TBZ,NSE:UNIMECH,NSE:VOLTAMP,NSE:WELSPUNLIV,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ATHERENERG,NSE:BALRAMCHIN,NSE:CHENNPETRO,NSE:GLAND,NSE:HAPPYFORGE,NSE:IOLCP,NSE:KTKBANK,NSE:MANORAMA,NSE:MTARTECH,NSE:NAZARA,NSE:SHILPAMED,NSE:TFCILTD,NSE:TITAN,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:CUPID,NSE:INDSWFTLAB,NSE:KMEW,NSE:LAURUSLABS,NSE:SAILIFE,NSE:SANSERA,NSE:SKYGOLD,NSE:WELCORP
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>⚠ CAUTION . →294Cr · 318Cr . ↓CMF0d</sub> | 1020.80 | -11.2% | +38.2% | 0d | SMA-OK | RS-OK | +1.17% |
| [GVT&D](https://in.tradingview.com/chart/?symbol=NSE:GVT&D)<br><sub>✓ SAFE . ↗550Cr · 503Cr . ↑CMF1d</sub> | 4656.00 | -15.9% | +82.0% | 0d | SMA-OK | RS-OK | -1.98% |
| [ADANIPOWER](https://in.tradingview.com/chart/?symbol=NSE:ADANIPOWER)<br><sub>✓ SAFE . ↗602Cr · 703Cr . ↓CMF30d</sub> | 214.00 | -14.0% | +75.8% | 0d | SMA-OK | RS-OK | +2.69% |
| [ADANIENT](https://in.tradingview.com/chart/?symbol=NSE:ADANIENT)<br><sub>✓ SAFE . ↗921Cr · 1631Cr . ↓CMF7d</sub> | 3104.10 | -3.3% | +76.5% | 0d | SMA-OK | RS-OK | +5.11% |
| [APOLLOHOSP](https://in.tradingview.com/chart/?symbol=NSE:APOLLOHOSP)<br><sub>✓ SAFE . ↘252Cr · 323Cr . ↑CMF1d</sub> | 8935.00 | -1.3% | +31.5% | 0d | SMA-OK | RS-OK | +1.10% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>✓ SAFE . ↗589Cr · 962Cr . ↑CMF1d</sub> | 1765.20 | -6.3% | +35.4% | 0d | SMA-OK | RS-OK | +3.23% |
| [RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO)<br><sub>⚠ CAUTION . ↘73Cr · 124Cr . ↓CMF1d</sub> | 4466.00 | -5.6% | +75.7% | 1d | SMA-OK | RS-OK | +2.43% |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML)<br><sub>✓ SAFE . ↗103Cr · 84Cr . ↓CMF6d</sub> | 1991.90 | -10.9% | +45.5% | 1d | SMA-OK | RS-OK | +2.71% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>✓ SAFE . →93Cr · 81Cr . ↓CMF1d</sub> | 3344.70 | -9.5% | +153.8% | 1d | SMA-OK | RS-OK | +2.40% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>⚠ CAUTION . ↘45Cr · 78Cr . ↓CMF21d</sub> | 334.80 | -5.5% | +62.8% | 1d | SMA-OK | RS-OK | +3.19% |
| [HONASA](https://in.tradingview.com/chart/?symbol=NSE:HONASA)<br><sub>✓ SAFE . ↘32Cr · 35Cr . ↓CMF3d</sub> | 469.30 | -6.7% | +83.1% | 1d | SMA-OK | RS-OK | +2.64% |
| [SUNDRMFAST](https://in.tradingview.com/chart/?symbol=NSE:SUNDRMFAST)<br><sub>⚠ CAUTION . ↗43Cr · 65Cr . ↓CMF6d</sub> | 1219.90 | -3.9% | +62.9% | 2d | SMA-OK | RS-OK | -1.41% |
| [INDORAMA](https://in.tradingview.com/chart/?symbol=NSE:INDORAMA)<br><sub>✓ SAFE . ↗23Cr · 31Cr . ↑CMF5d</sub> | 85.60 | -1.0% | +184.5% | 2d | SMA-OK | RS-OK | +3.37% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>✓ SAFE . ↗128Cr · 270Cr . ↑CMF7d</sub> | 1381.20 | -2.6% | +134.9% | 3d | SMA-OK | RS-OK | +4.36% |
| [UNIONBANK](https://in.tradingview.com/chart/?symbol=NSE:UNIONBANK)<br><sub>✓ SAFE . →151Cr · 125Cr . ↓CMF0d</sub> | 182.67 | -9.7% | +44.0% | 3d | SMA-OK | RS-OK | -0.30% |
| [CGPOWER](https://in.tradingview.com/chart/?symbol=NSE:CGPOWER)<br><sub>✓ SAFE . ↗281Cr · 312Cr . ↑CMF25d</sub> | 925.30 | -5.2% | +74.4% | 3d | SMA-OK | RS-OK | +1.60% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . ↗110Cr · 57Cr . ↑CMF0d</sub> | 1254.60 | -0.1% | +36.6% | 5d | SMA-OK | RS-OK | +2.75% |
| [WABAG](https://in.tradingview.com/chart/?symbol=NSE:WABAG)<br><sub>✓ SAFE . →187Cr · 180Cr . ↑CMF6d</sub> | 2055.80 | -9.8% | +96.0% | 6d | SMA-OK | RS-OK | -2.26% |
| [MOTILALOFS](https://in.tradingview.com/chart/?symbol=NSE:MOTILALOFS)<br><sub>✓ SAFE . ↘64Cr · 75Cr . ↑CMF18d</sub> | 976.50 | -10.5% | +55.4% | 6d | SMA-OK | RS-OK | -1.44% |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE)<br><sub>✓ SAFE . ↗486Cr · 243Cr . ↑CMF5d</sub> | 805.05 | -4.7% | +53.0% | 7d | SMA-OK | RS-OK | +3.01% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>✓ SAFE . ↗99Cr · 60Cr . ↓CMF1d</sub> | 202.37 | -10.7% | +51.8% | 7d | SMA-OK | RS-OK | -0.54% |
| [VARROC](https://in.tradingview.com/chart/?symbol=NSE:VARROC)<br><sub>✓ SAFE . →32Cr · 37Cr . ↑CMF4d</sub> | 851.15 | -3.8% | +82.1% | 7d | SMA-OK | RS-OK | +1.81% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>✓ SAFE . ↗725Cr · 506Cr . ↑CMF10d</sub> | 1170.95 | 0.0% | +225.7% | 8d | SMA-OK | RS-OK | +10.70% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>✓ SAFE . →330Cr · 361Cr . ↑CMF18d</sub> | 433.35 | -2.1% | +105.3% | 8d | SMA-OK | RS-OK | +2.65% |
| [GRASIM](https://in.tradingview.com/chart/?symbol=NSE:GRASIM)<br><sub>⚠ CAUTION . →341Cr · 271Cr . ↑CMF23d</sub> | 3295.00 | -2.5% | +30.2% | 8d | SMA-OK | RS-OK | -0.36% |
| [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO)<br><sub>✓ SAFE . ↗167Cr · 178Cr . ↑CMF9d</sub> | 84.59 | 0.0% | +173.1% | 8d | SMA-OK | RS-OK | +0.14% |
| [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK)<br><sub>✓ SAFE . ↗189Cr · 105Cr . ↑CMF25d</sub> | 404.00 | -3.5% | +52.8% | 8d | SMA-OK | RS-OK | +0.10% |
| [ARVIND](https://in.tradingview.com/chart/?symbol=NSE:ARVIND)<br><sub>✓ SAFE . →40Cr · 54Cr . ↑CMF24d</sub> | 548.05 | -6.6% | +96.0% | 8d | SMA-OK | RS-OK | -0.46% |
| [EMCURE](https://in.tradingview.com/chart/?symbol=NSE:EMCURE)<br><sub>✓ SAFE . ↗29Cr · 48Cr . ↓CMF23d</sub> | 1931.90 | -3.9% | +51.9% | 8d | SMA-OK | RS-OK | -3.07% |
| [STAR](https://in.tradingview.com/chart/?symbol=NSE:STAR)<br><sub>✓ SAFE . ↘61Cr · 47Cr . ↑CMF7d</sub> | 1183.90 | -2.7% | +49.2% | 8d | SMA-OK | RS-OK | +2.89% |
| [VENUSPIPES](https://in.tradingview.com/chart/?symbol=NSE:VENUSPIPES)<br><sub>✓ SAFE . ↗59Cr · 42Cr . ↑CMF7d</sub> | 1938.10 | -4.1% | +116.8% | 8d | SMA-OK | RS-OK | -0.18% |
| [CENTUM](https://in.tradingview.com/chart/?symbol=NSE:CENTUM)<br><sub>✓ SAFE . ↗59Cr · 39Cr . ↑CMF7d</sub> | 4276.10 | -2.3% | +104.3% | 8d | SMA-OK | RS-OK | +6.62% |
| [JKPAPER](https://in.tradingview.com/chart/?symbol=NSE:JKPAPER)<br><sub>✓ SAFE . ↗32Cr · 30Cr . ↑CMF0d</sub> | 417.35 | -2.1% | +36.2% | 9d | SMA-OK | RS-OK | +3.79% |
| [WOCKPHARMA](https://in.tradingview.com/chart/?symbol=NSE:WOCKPHARMA)<br><sub>✓ SAFE . ↗315Cr · 255Cr . ↑CMF7d</sub> | 2021.50 | -10.1% | +83.7% | 10d | SMA-OK | RS-OK | -2.06% |
| [PFOCUS](https://in.tradingview.com/chart/?symbol=NSE:PFOCUS)<br><sub>✓ SAFE . →39Cr · 75Cr . ↑CMF8d</sub> | 320.45 | -8.3% | +96.9% | 10d | SMA-OK | RS-OK | +0.45% |
| [FOSECOIND](https://in.tradingview.com/chart/?symbol=NSE:FOSECOIND)<br><sub>✓ SAFE . →17Cr · 122Cr . ↑CMF16d</sub> | 6846.50 | 0.0% | +57.5% | 12d | SMA-OK | RS-OK | +10.01% |
| [CGCL](https://in.tradingview.com/chart/?symbol=NSE:CGCL)<br><sub>✓ SAFE . ↘137Cr · 196Cr . ↑CMF16d</sub> | 256.65 | -8.3% | +68.9% | 13d | SMA-OK | RS-OK | +0.61% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . ↗94Cr · 53Cr . ↑CMF8d</sub> | 690.20 | -3.2% | +208.9% | 13d | SMA-OK | RS-OK | +0.91% |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE)<br><sub>✓ SAFE . ↗35Cr · 49Cr . ↓CMF1d</sub> | 1149.70 | -3.0% | +53.5% | 13d | SMA-OK | RS-OK | +1.55% |
| [TI](https://in.tradingview.com/chart/?symbol=NSE:TI)<br><sub>✓ SAFE . ↘22Cr · 30Cr . ↓CMF4d</sub> | 526.55 | -9.7% | +35.4% | 13d | SMA-OK | RS-OK | +3.09% |
| [KOPRAN](https://in.tradingview.com/chart/?symbol=NSE:KOPRAN)<br><sub>✓ SAFE . ↗91Cr · 371Cr . ↑CMF0d</sub> | 260.86 | 0.0% | +141.4% | 14d | SMA-OK | RS-OK | +4.39% |
| [WHEELS](https://in.tradingview.com/chart/?symbol=NSE:WHEELS)<br><sub>✓ SAFE . ↗321Cr · 51Cr . ↑CMF14d</sub> | 2110.50 | -12.1% | +195.6% | 15d | SMA-OK | RS-OK | -0.87% |
| [RPEL](https://in.tradingview.com/chart/?symbol=NSE:RPEL)<br><sub>✓ SAFE . ↗27Cr · 38Cr . ↓CMF0d</sub> | 1547.00 | -17.9% | +173.1% | 15d | SMA-OK | RS-OK | -4.65% |
| [QUADFUTURE](https://in.tradingview.com/chart/?symbol=NSE:QUADFUTURE)<br><sub>✓ SAFE . ↘94Cr · 55Cr . ↑CMF18d</sub> | 491.95 | 0.0% | +94.7% | 17d | SMA-OK | RS-OK | +1.52% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [GLENMARK](https://in.tradingview.com/chart/?symbol=NSE:GLENMARK)<br><sub>✓ SAFE . ↘87Cr · 163Cr . ↑CMF19d</sub> | 2410.00 | -4.2% | +33.1% | 18d | SMA-OK | RS-OK | +1.61% |
| [NEULANDLAB](https://in.tradingview.com/chart/?symbol=NSE:NEULANDLAB)<br><sub>✓ SAFE . →95Cr · 115Cr . ↓CMF2d</sub> | 22625.00 | -5.7% | +95.8% | 18d | SMA-OK | RS-OK | +0.13% |
| [BLUESTONE](https://in.tradingview.com/chart/?symbol=NSE:BLUESTONE)<br><sub>✓ SAFE . ↗66Cr · 69Cr . ↑CMF3d</sub> | 856.00 | -4.3% | +112.2% | 18d | SMA-OK | RS-OK | +3.31% |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>⚠ CAUTION . ↘34Cr · 66Cr . ↓CMF2d</sub> | 1950.70 | -1.9% | +53.8% | 18d | SMA-OK | RS-OK | +0.95% |
| [WELENT](https://in.tradingview.com/chart/?symbol=NSE:WELENT)<br><sub>✓ SAFE . →81Cr · 45Cr . ↑CMF18d</sub> | 768.00 | -5.6% | +84.7% | 18d | SMA-OK | RS-OK | +4.12% |
| [ASIANENE](https://in.tradingview.com/chart/?symbol=NSE:ASIANENE)<br><sub>✓ SAFE . →30Cr · 36Cr . ↑CMF30d</sub> | 494.10 | -10.7% | +111.2% | 18d | SMA-OK | RS-OK | +1.82% |
| [JTLIND](https://in.tradingview.com/chart/?symbol=NSE:JTLIND)<br><sub>✓ SAFE . ↘25Cr · 32Cr . ↑CMF19d</sub> | 84.60 | -8.4% | +107.4% | 18d | SMA-OK | RS-OK | +2.58% |
| [BODALCHEM](https://in.tradingview.com/chart/?symbol=NSE:BODALCHEM)<br><sub>✓ SAFE . ↘74Cr · 32Cr . ↑CMF20d</sub> | 173.46 | -5.8% | +299.2% | 18d | SMA-OK | RS-OK | -1.81% |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN)<br><sub>✓ SAFE . ↘71Cr · 58Cr . ↑CMF30d</sub> | 260.65 | -7.6% | +58.4% | 19d | SMA-OK | RS-OK | -0.69% |
| [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX)<br><sub>✓ SAFE . ↗51Cr · 43Cr . ↑CMF30d</sub> | 87.22 | -0.2% | +136.4% | 19d | SMA-OK | RS-OK | +5.84% |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL)<br><sub>✓ SAFE . ↗47Cr · 38Cr . ↑CMF4d</sub> | 180.93 | -6.5% | +111.4% | 19d | SMA-OK | RS-OK | -2.23% |
| [DEEPINDS](https://in.tradingview.com/chart/?symbol=NSE:DEEPINDS)<br><sub>✓ SAFE . ↗53Cr · 52Cr . ↑CMF30d</sub> | 735.15 | -10.2% | +121.7% | 21d | SMA-OK | RS-OK | +0.65% |
| [HEG](https://in.tradingview.com/chart/?symbol=NSE:HEG)<br><sub>✓ SAFE . →118Cr · 187Cr . ↑CMF15d</sub> | 728.25 | -1.5% | +52.6% | 22d | SMA-OK | RS-OK | +2.94% |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>✓ SAFE . ↘80Cr · 56Cr . ↑CMF21d</sub> | 418.00 | -0.6% | +110.1% | 22d | SMA-OK | RS-OK | -0.57% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↗950Cr · 1258Cr . ↑CMF26d</sub> | 993.90 | -0.9% | +208.8% | 23d | SMA-OK | RS-OK | -0.21% |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . ↘549Cr · 633Cr . ↑CMF25d</sub> | 3211.20 | -6.7% | +110.0% | 23d | SMA-OK | RS-OK | +1.19% |
| [FINCABLES](https://in.tradingview.com/chart/?symbol=NSE:FINCABLES)<br><sub>✓ SAFE . ↗231Cr · 172Cr . ↑CMF5d</sub> | 1362.60 | -4.3% | +91.7% | 23d | SMA-OK | RS-OK | +1.69% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>✓ SAFE . ↗160Cr · 164Cr . ↑CMF14d</sub> | 790.30 | -9.8% | +154.5% | 23d | SMA-OK | RS-OK | -2.21% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>✓ SAFE . →69Cr · 74Cr . ↑CMF16d</sub> | 867.40 | -11.1% | +218.5% | 23d | SMA-OK | RS-OK | -1.73% |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER)<br><sub>✓ SAFE . →44Cr · 70Cr . ↓CMF2d</sub> | 1422.90 | -6.4% | +139.1% | 23d | SMA-OK | RS-OK | +5.00% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>✓ SAFE . →61Cr · 66Cr . ↓CMF0d</sub> | 645.55 | -5.0% | +166.2% | 23d | SMA-OK | RS-OK | -3.86% |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>✓ SAFE . ↗46Cr · 55Cr . ↑CMF1d</sub> | 2302.40 | -3.6% | +135.0% | 23d | SMA-OK | RS-OK | -0.34% |
| [KRN](https://in.tradingview.com/chart/?symbol=NSE:KRN)<br><sub>✓ SAFE . →29Cr · 40Cr . ↓CMF1d</sub> | 1438.30 | -13.4% | +140.5% | 23d | SMA-OK | RS-OK | -5.00% |
| [VOLTAMP](https://in.tradingview.com/chart/?symbol=NSE:VOLTAMP)<br><sub>✓ SAFE . ↘28Cr · 30Cr . ↑CMF14d</sub> | 10513.00 | -16.0% | +55.1% | 23d | SMA-OK | RS-OK | -0.78% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>✓ SAFE . →183Cr · 132Cr . ↑CMF25d</sub> | 48870.00 | -2.3% | +70.0% | 24d | SMA-OK | RS-OK | +0.17% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↘82Cr · 63Cr . ↑CMF3d</sub> | 202.82 | -4.3% | +87.2% | 24d | SMA-OK | RS-OK | +0.59% |
| [TBZ](https://in.tradingview.com/chart/?symbol=NSE:TBZ)<br><sub>✓ SAFE . ↘134Cr · 86Cr . ↑CMF15d</sub> | 547.50 | -1.4% | +391.0% | 25d | SMA-OK | RS-OK | +4.40% |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE)<br><sub>↘26Cr · 46Cr . ↑CMF30d</sub> | 373.30 | -13.7% | +146.1% | 25d | SMA-OK | RS-OK | -0.92% |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH)<br><sub>✓ SAFE . ↗77Cr · 457Cr . ↑CMF1d</sub> | 1349.90 | 0.0% | +135.2% | 28d | SMA-OK | RS-OK | +6.68% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>✓ SAFE . ↘73Cr · 112Cr . ↓CMF0d</sub> | 1134.00 | -4.3% | +51.0% | 28d | SMA-OK | RS-OK | -0.96% |
| [JINDALSAW](https://in.tradingview.com/chart/?symbol=NSE:JINDALSAW)<br><sub>✓ SAFE . ↘55Cr · 68Cr . ↑CMF30d</sub> | 281.25 | -11.4% | +81.9% | 28d | SMA-OK | RS-OK | -2.68% |
| [RACLGEAR](https://in.tradingview.com/chart/?symbol=NSE:RACLGEAR)<br><sub>✓ SAFE . ↗35Cr · 48Cr . ↑CMF3d</sub> | 1852.40 | 0.0% | +104.0% | 28d | SMA-OK | RS-OK | +5.54% |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH)<br><sub>✓ SAFE . ↗23Cr · 35Cr . ↑CMF3d</sub> | 12077.00 | -3.6% | +78.7% | 28d | SMA-OK | RS-OK | +0.05% |
| [SOLARINDS](https://in.tradingview.com/chart/?symbol=NSE:SOLARINDS)<br><sub>✓ SAFE . →401Cr · 204Cr . ↑CMF30d</sub> | 22330.00 | -0.6% | +89.7% | 29d | SMA-OK | RS-OK | -0.56% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . ↗503Cr · 354Cr . ↑CMF30d</sub> | 9443.00 | -1.4% | +66.0% | 29d | SMA-OK | RS-OK | -1.38% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>✓ SAFE . ↘67Cr · 93Cr . ↓CMF8d</sub> | 908.45 | -5.2% | +54.5% | 29d | SMA-OK | RS-OK | -3.65% |
| [SIEMENS](https://in.tradingview.com/chart/?symbol=NSE:SIEMENS)<br><sub>✓ SAFE . ↘119Cr · 146Cr . ↓CMF1d</sub> | 3947.70 | -3.7% | +38.6% | 29d | SMA-OK | RS-OK | -0.09% |
| [FCL](https://in.tradingview.com/chart/?symbol=NSE:FCL)<br><sub>✓ SAFE . ↗162Cr · 156Cr . ↑CMF18d</sub> | 53.07 | -9.6% | +175.8% | 30d | SMA-OK | RS-OK | -1.50% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↘215Cr · 452Cr . ↑CMF30d</sub> | 114.73 | -3.5% | +240.6% | 31d | SMA-OK | RS-OK | +8.01% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>✓ SAFE . ↗58Cr · 296Cr . ↓CMF0d</sub> | 1895.70 | -3.7% | +45.0% | 31d | SMA-OK | RS-OK | -0.56% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>✓ SAFE . ↘25Cr · 41Cr . ↑CMF16d</sub> | 1731.80 | -8.8% | +82.4% | 31d | SMA-OK | RS-OK | -3.90% |
| [SMLMAH](https://in.tradingview.com/chart/?symbol=NSE:SMLMAH)<br><sub>✓ SAFE . ↗84Cr · 50Cr . ↑CMF8d</sub> | 5971.50 | -9.3% | +115.9% | 32d | SMA-OK | RS-OK | -4.52% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>✓ SAFE . ↗338Cr · 254Cr . ↑CMF9d</sub> | 1511.20 | -7.8% | +136.1% | 33d | SMA-OK | RS-OK | +0.23% |
| [APARINDS](https://in.tradingview.com/chart/?symbol=NSE:APARINDS)<br><sub>✓ SAFE . →186Cr · 185Cr . ↑CMF4d</sub> | 17075.00 | -5.1% | +145.1% | 33d | SMA-OK | RS-OK | +3.17% |
| [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON)<br><sub>⚠ CAUTION . →198Cr · 93Cr . ↓CMF3d</sub> | 164.17 | -3.8% | +74.1% | 33d | SMA-OK | RS-OK | +0.20% |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS)<br><sub>✓ SAFE . →68Cr · 72Cr . ↓CMF3d</sub> | 316.45 | -5.8% | +101.7% | 33d | SMA-OK | RS-OK | +1.15% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . →92Cr · 81Cr . ↑CMF8d</sub> | 8160.50 | -7.0% | +79.3% | 34d | SMA-OK | RS-OK | -0.82% |
| [SBCL](https://in.tradingview.com/chart/?symbol=NSE:SBCL)<br><sub>✓ SAFE . →41Cr · 56Cr . ↓CMF7d</sub> | 1057.00 | -8.6% | +181.7% | 34d | SMA-OK | RS-OK | +3.61% |
| [AVALON](https://in.tradingview.com/chart/?symbol=NSE:AVALON)<br><sub>✓ SAFE . →117Cr · 207Cr . ↓CMF1d</sub> | 2216.10 | -6.6% | +179.2% | 36d | SMA-OK | RS-OK | +2.56% |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>✓ SAFE . →67Cr · 47Cr . ↓CMF22d</sub> | 4533.60 | -5.3% | +52.6% | 36d | SMA-OK | RS-OK | -1.47% |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH)<br><sub>✓ SAFE . ↗45Cr · 70Cr . ↑CMF6d</sub> | 1515.80 | -7.0% | +114.6% | 37d | SMA-OK | RS-OK | -1.48% |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS)<br><sub>✓ SAFE . ↗363Cr · 101Cr . ↑CMF9d</sub> | 322.85 | -4.3% | +173.7% | 37d | SMA-OK | RS-OK | -0.35% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>⚠ CAUTION . ↘98Cr · 86Cr . ↑CMF30d</sub> | 1643.00 | -4.3% | +53.4% | 38d | SMA-OK | RS-OK | -1.02% |
| [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN)<br><sub>✓ SAFE . ↘47Cr · 63Cr . ↑CMF30d</sub> | 11040.00 | -6.8% | +71.9% | 38d | SMA-OK | RS-OK | -0.53% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>✓ SAFE . ↘42Cr · 35Cr . ↓CMF12d</sub> | 688.80 | -8.8% | +48.9% | 38d | SMA-OK | RS-OK | +0.09% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . ↘121Cr · 341Cr . ↑CMF30d . DEL56%(T-1)</sub> | 286.75 | -7.7% | +118.4% | 40d | SMA-OK | RS-OK | -0.98% |
| [KABRAEXTRU](https://in.tradingview.com/chart/?symbol=NSE:KABRAEXTRU)<br><sub>✓ SAFE . →25Cr · 41Cr . ↑CMF30d</sub> | 628.10 | -13.1% | +244.0% | 40d | SMA-OK | RS-OK | -3.50% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↘45Cr · 62Cr . ↑CMF11d</sub> | 350.05 | -6.3% | +105.4% | 42d | SMA-OK | RS-OK | +3.26% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . ↘97Cr · 163Cr . ↑CMF30d</sub> | 138.81 | -5.4% | +151.3% | 43d | SMA-OK | RS-OK | +0.46% |
| [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP)<br><sub>✓ SAFE . →106Cr · 168Cr . ↑CMF15d</sub> | 194.57 | -8.7% | +185.3% | 46d | SMA-OK | RS-OK | +8.38% |
| [TITAN](https://in.tradingview.com/chart/?symbol=NSE:TITAN)<br><sub>⚠ CAUTION . ↗289Cr · 235Cr . ↑CMF30d</sub> | 4985.50 | -3.6% | +49.8% | 48d | SMA-OK | RS-OK | -0.03% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>✓ SAFE . ↘61Cr · 66Cr . ↑CMF30d</sub> | 318.20 | -6.4% | +86.3% | 48d | SMA-OK | RS-OK | +0.71% |
| [MANORAMA](https://in.tradingview.com/chart/?symbol=NSE:MANORAMA)<br><sub>✓ SAFE . ↗61Cr · 51Cr . ↑CMF1d</sub> | 1916.40 | -10.2% | +78.1% | 48d | SMA-OK | RS-OK | -3.56% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↗239Cr · 212Cr . ↑CMF29d</sub> | 2826.60 | -6.6% | +77.0% | 49d | SMA-OK | RS-OK | -2.38% |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>✓ SAFE . ↘175Cr · 64Cr . ↑CMF30d</sub> | 682.60 | -11.0% | +71.6% | 50d | SMA-OK | RS-OK | +0.81% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . ↘34Cr · 38Cr . ↑CMF30d</sub> | 351.15 | -6.3% | +61.3% | 50d | SMA-OK | RS-OK | -1.75% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↗334Cr · 198Cr . ↑CMF0d</sub> | 1456.00 | -10.5% | +101.2% | 51d | SMA-OK | RS-OK | -1.07% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . ↘594Cr · 561Cr . ↑CMF30d</sub> | 1567.50 | -9.2% | +190.3% | 58d | SMA-OK | RS-OK | -0.06% |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>✓ SAFE . ↘84Cr · 110Cr . ↑CMF9d</sub> | 928.05 | -3.7% | +247.6% | 58d | SMA-OK | RS-OK | +1.77% |
| [MTARTECH](https://in.tradingview.com/chart/?symbol=NSE:MTARTECH)<br><sub>✓ SAFE . ↗2251Cr · 944Cr . ↑CMF8d</sub> | 7777.00 | -7.1% | +457.1% | 58d | SMA-OK | RS-OK | -4.25% |
| [HAPPYFORGE](https://in.tradingview.com/chart/?symbol=NSE:HAPPYFORGE)<br><sub>✓ SAFE . ↘14Cr · 36Cr . ↑CMF30d</sub> | 2155.90 | -10.9% | +139.1% | 63d | SMA-OK | RS-OK | +3.93% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>✓ SAFE . →24Cr · 65Cr . ↑CMF2d</sub> | 2708.70 | -14.0% | +146.4% | 68d | SMA-OK | RS-OK | -0.80% |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB)<br><sub>✓ SAFE . ↘28Cr · 60Cr . ↑CMF26d</sub> | 363.90 | -6.3% | +312.8% | 78d | SMA-OK | RS-OK | -3.92% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↗79Cr · 91Cr . ↑CMF25d</sub> | 3971.20 | -4.0% | +189.4% | 83d | SMA-OK | RS-OK | +2.57% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>✓ SAFE . ↘497Cr · 711Cr . ↑CMF30d</sub> | 2424.50 | -12.7% | +235.9% | 90d | SMA-OK | RS-OK | +0.46% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . ↘350Cr · 286Cr . ↑CMF30d</sub> | 1920.60 | -2.5% | +130.8% | 91d | SMA-OK | RS-OK | -2.46% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . →138Cr · 123Cr . ↑CMF11d</sub> | 1539.10 | -8.1% | +93.6% | 102d | SMA-OK | RS-OK | -0.16% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . →63Cr · 56Cr . ↓CMF1d</sub> | 792.60 | -6.5% | +201.1% | 107d | SMA-OK | RS-OK | +0.41% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↘267Cr · 243Cr . ↑CMF30d</sub> | 280.00 | -5.0% | +583.8% | 120d | SMA-OK | RS-OK | -1.55% |

### By Trend Age

**<2 WEEKS** (35)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ACUTAAS,NSE:ADANIENT,NSE:ADANIPORTS,NSE:ADANIPOWER,NSE:AEGISLOG,NSE:ANTELOPUS,NSE:APOLLOHOSP,NSE:ARVIND,NSE:BEML,NSE:BHEL,NSE:CENTUM,NSE:CGPOWER,NSE:EMCURE,NSE:GRAPHITE,NSE:GRASIM,NSE:GVT&D,NSE:HINDALCO,NSE:HONASA,NSE:INDORAMA,NSE:JKPAPER,NSE:KARURVYSYA,NSE:MOTILALOFS,NSE:PAISALO,NSE:PFOCUS,NSE:PPLPHARMA,NSE:PVRINOX,NSE:RADICO,NSE:RBLBANK,NSE:STAR,NSE:SUNDRMFAST,NSE:UNIONBANK,NSE:VARROC,NSE:VENUSPIPES,NSE:WABAG,NSE:WOCKPHARMA
```

**2-4 WEEKS** (22)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ACE,NSE:ASIANENE,NSE:BLUESTONE,NSE:BODALCHEM,NSE:CGCL,NSE:DEEPINDS,NSE:EMIL,NSE:ENGINERSIN,NSE:FILATEX,NSE:FOSECOIND,NSE:GLENMARK,NSE:HFCL,NSE:IPCALAB,NSE:JTLIND,NSE:KOPRAN,NSE:NEULANDLAB,NSE:QUADFUTURE,NSE:RPEL,NSE:SHREEJISPG,NSE:TI,NSE:WELENT,NSE:WHEELS
```

**1-2 MONTHS** (47)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ACMESOLAR,NSE:ANTHEM,NSE:APARINDS,NSE:AUROPHARMA,NSE:AVALON,NSE:BOSCHLTD,NSE:CRAFTSMAN,NSE:CYIENTDLM,NSE:DIACABS,NSE:DIVISLAB,NSE:DYNAMATECH,NSE:EBGNG,NSE:ENTERO,NSE:FCL,NSE:FINCABLES,NSE:FLUOROCHEM,NSE:HEG,NSE:JINDALSAW,NSE:KABRAEXTRU,NSE:KRN,NSE:LALPATHLAB,NSE:MANINDS,NSE:MARINE,NSE:MARKSANS,NSE:MCX,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:NAVINFLUOR,NSE:NEOGEN,NSE:PNBHOUSING,NSE:QPOWER,NSE:RACLGEAR,NSE:RATNAVEER,NSE:RAYMOND,NSE:RKFORGE,NSE:ROSSTECH,NSE:SBCL,NSE:SIEMENS,NSE:SMLMAH,NSE:SOLARINDS,NSE:SSWL,NSE:STLTECH,NSE:SYRMA,NSE:TBZ,NSE:UNIMECH,NSE:VOLTAMP,NSE:WELSPUNLIV
```

**2-3 MONTHS** (13)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ATHERENERG,NSE:BALRAMCHIN,NSE:CHENNPETRO,NSE:GLAND,NSE:HAPPYFORGE,NSE:IOLCP,NSE:KTKBANK,NSE:MANORAMA,NSE:MTARTECH,NSE:NAZARA,NSE:SHILPAMED,NSE:TFCILTD,NSE:TITAN
```

**3-6 MONTHS** (8)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CUPID,NSE:INDSWFTLAB,NSE:KMEW,NSE:LAURUSLABS,NSE:SAILIFE,NSE:SANSERA,NSE:SKYGOLD,NSE:WELCORP
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
