> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-11-25
*Generated 2026-11-25 15:48 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER) | [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS) |
| [ARFIN](https://in.tradingview.com/chart/?symbol=NSE:ARFIN) | [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO) |
| [ARIS](https://in.tradingview.com/chart/?symbol=NSE:ARIS) | [ARVIND](https://in.tradingview.com/chart/?symbol=NSE:ARVIND) |
| [BAJAJHLDNG](https://in.tradingview.com/chart/?symbol=NSE:BAJAJHLDNG) | [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL) |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML) | [BLISSGVS](https://in.tradingview.com/chart/?symbol=NSE:BLISSGVS) |
| [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX) | [COMSYN](https://in.tradingview.com/chart/?symbol=NSE:COMSYN) |
| [IGIL](https://in.tradingview.com/chart/?symbol=NSE:IGIL) | [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS) |
| [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN) | [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN) |
| [KOPRAN](https://in.tradingview.com/chart/?symbol=NSE:KOPRAN) | [HINDOILEXP](https://in.tradingview.com/chart/?symbol=NSE:HINDOILEXP) |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH) | [ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL) |
| [MAXESTATES](https://in.tradingview.com/chart/?symbol=NSE:MAXESTATES) | [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA) |
| [NEULANDLAB](https://in.tradingview.com/chart/?symbol=NSE:NEULANDLAB) | [LICHSGFIN](https://in.tradingview.com/chart/?symbol=NSE:LICHSGFIN) |
| [PDSL](https://in.tradingview.com/chart/?symbol=NSE:PDSL) | [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB) |
| [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS) | [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN) |
| [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC) | [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM) |
| [YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH) | [PROTEAN](https://in.tradingview.com/chart/?symbol=NSE:PROTEAN) |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE) | [SGFIN](https://in.tradingview.com/chart/?symbol=NSE:SGFIN) |
|  | [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART) |
|  | [SPORTKING](https://in.tradingview.com/chart/?symbol=NSE:SPORTKING) |
|  | [TITAN](https://in.tradingview.com/chart/?symbol=NSE:TITAN) |
|  | [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH) |
|  | [WESTLIFE](https://in.tradingview.com/chart/?symbol=NSE:WESTLIFE) |

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

**Qualifying: 112**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AETHER,NSE:ARFIN,NSE:BAJAJHLDNG,NSE:BEML,NSE:COHANCE,NSE:CPPLUS,NSE:CRAFTSMAN,NSE:FEDERALBNK,NSE:FILATEX,NSE:GABRIEL,NSE:GESHIP,NSE:GRANULES,NSE:GRAPHITE,NSE:GREAVESCOT,NSE:IGIL,NSE:IIFL,NSE:INDIGO,NSE:JSWINFRA,NSE:KOPRAN,NSE:LGEINDIA,NSE:LODHA,NSE:LTTS,NSE:MANKIND,NSE:MAXESTATES,NSE:MOTHERSON,NSE:NEULANDLAB,NSE:PARAGMILK,NSE:PETRONET,NSE:PNBHOUSING,NSE:POONAWALLA,NSE:PTCIL,NSE:RBLBANK,NSE:SAMBHV,NSE:TANLA,NSE:TECHM,NSE:TI,NSE:UNOMINDA,NSE:VIJAYA,NSE:WOCKPHARMA,NSE:ZYDUSLIFE,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABCAPITAL,NSE:ACE,NSE:ADANIPORTS,NSE:ANTHEM,NSE:APLLTD,NSE:AUROPHARMA,NSE:BOSCHLTD,NSE:CEMPRO,NSE:DCBBANK,NSE:DIVISLAB,NSE:DLF,NSE:EMCURE,NSE:ENTERO,NSE:ETERNAL,NSE:FLUOROCHEM,NSE:GAIL,NSE:GLENMARK,NSE:HFCL,NSE:HONASA,NSE:INDGN,NSE:JYOTICNC,NSE:KALYANKJIL,NSE:KARURVYSYA,NSE:KDDL,NSE:KPRMILL,NSE:KTKBANK,NSE:LALPATHLAB,NSE:LUMAXTECH,NSE:MAHABANK,NSE:MCX,NSE:MEDANTA,NSE:MOTILALOFS,NSE:NAVINFLUOR,NSE:NYKAA,NSE:PDSL,NSE:PHOENIXLTD,NSE:PPLPHARMA,NSE:RADICO,NSE:RKFORGE,NSE:ROLEXRINGS,NSE:RUBICON,NSE:SAILIFE,NSE:SANSERA,NSE:STYLEBAAZA,NSE:TVSMOTOR,NSE:URBANCO,NSE:WELSPUNLIV,NSE:YATHARTH,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AARTIPHARM,NSE:ACUTAAS,NSE:ARIS,NSE:ATHERENERG,NSE:COFORGE,NSE:CUPID,NSE:GLAND,NSE:GRWRHITECH,NSE:INDHOTEL,NSE:PVRINOX,NSE:SAREGAMA,NSE:SONACOMS,NSE:SOUTHBANK,NSE:STLTECH,NSE:TIPSMUSIC,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABDL,NSE:SBC,NSE:SHREEJISPG,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:RATNAVEER,NSE:RAYMOND,NSE:SSWL,NSE:TFCILTD,NSE:THELEELA,###6+ MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:LAURUSLABS
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [KOPRAN](https://in.tradingview.com/chart/?symbol=NSE:KOPRAN)<br><sub>✓ SAFE . ↗51Cr · 377Cr . ↑CMF9d</sub> | 289.52 | -0.5% | +168.0% | 0d | SMA-OK | RS-OK | +9.11% |
| [IIFL](https://in.tradingview.com/chart/?symbol=NSE:IIFL)<br><sub>✓ SAFE . ↗551Cr · 347Cr . ↓CMF5d</sub> | 610.50 | -12.3% | +45.6% | 0d | SMA-OK | RS-OK | -0.73% |
| [LGEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LGEINDIA)<br><sub>✓ SAFE . ↗141Cr · 301Cr . ↓CMF8d</sub> | 1775.00 | -1.0% | +34.6% | 0d | SMA-OK | RS-OK | +1.97% |
| [TECHM](https://in.tradingview.com/chart/?symbol=NSE:TECHM)<br><sub>✓ SAFE . →377Cr · 565Cr . ↓CMF3d</sub> | 1777.50 | -3.1% | +33.9% | 0d | SMA-OK | RS-OK | +1.79% |
| [GRANULES](https://in.tradingview.com/chart/?symbol=NSE:GRANULES)<br><sub>✓ SAFE . →156Cr · 195Cr . ↑CMF13d</sub> | 840.80 | -7.5% | +56.4% | 0d | SMA-OK | RS-OK | +0.36% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>✓ SAFE . ↘138Cr · 83Cr . ↑CMF17d</sub> | 1199.50 | -3.7% | +39.4% | 0d | SMA-OK | RS-OK | -0.04% |
| [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA)<br><sub>⚠ CAUTION . →71Cr · 147Cr . ↑CMF15d</sub> | 357.65 | -2.7% | +52.6% | 0d | SMA-OK | RS-OK | +1.16% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . ↘62Cr · 82Cr . ↓CMF13d</sub> | 4204.70 | -5.3% | +206.7% | 0d | SMA-OK | RS-OK | +3.21% |
| [NEULANDLAB](https://in.tradingview.com/chart/?symbol=NSE:NEULANDLAB)<br><sub>✓ SAFE . ↘88Cr · 62Cr . ↑CMF15d</sub> | 20968.00 | -12.6% | +81.5% | 0d | SMA-OK | RS-OK | +2.03% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>✓ SAFE . ↘35Cr · 55Cr . ↑CMF5d</sub> | 1676.50 | -6.9% | +105.5% | 0d | SMA-OK | RS-OK | +4.98% |
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP)<br><sub>✓ SAFE . ↘85Cr · 55Cr . ↓CMF4d</sub> | 1548.00 | -10.0% | +44.5% | 0d | SMA-OK | RS-OK | +0.63% |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE)<br><sub>✓ SAFE . ↘45Cr · 53Cr . ↑CMF15d</sub> | 794.45 | -6.7% | +51.0% | 0d | SMA-OK | RS-OK | +0.58% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>✓ SAFE . ↗59Cr · 53Cr . ↑CMF2d</sub> | 171.66 | -3.0% | +108.6% | 0d | SMA-OK | RS-OK | -2.96% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>✓ SAFE . →40Cr · 46Cr . ↑CMF2d</sub> | 24380.00 | -5.2% | +65.6% | 0d | SMA-OK | RS-OK | -0.18% |
| [ARFIN](https://in.tradingview.com/chart/?symbol=NSE:ARFIN)<br><sub>✓ SAFE . ↘14Cr · 34Cr . ↑CMF4d</sub> | 94.93 | -12.3% | +64.3% | 0d | SMA-OK | RS-OK | +3.96% |
| [BAJAJHLDNG](https://in.tradingview.com/chart/?symbol=NSE:BAJAJHLDNG)<br><sub>⚠ CAUTION . ↘32Cr · 32Cr . ↑CMF1d</sub> | 11541.00 | -2.8% | +32.0% | 1d | SMA-OK | RS-OK | -1.10% |
| [COHANCE](https://in.tradingview.com/chart/?symbol=NSE:COHANCE)<br><sub>✓ SAFE . ↗82Cr · 660Cr . ↓CMF0d</sub> | 489.55 | -14.8% | +74.9% | 3d | SMA-OK | RS-OK | +3.11% |
| [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON)<br><sub>✓ SAFE . →278Cr · 171Cr . ↑CMF15d</sub> | 165.76 | -2.9% | +57.7% | 3d | SMA-OK | RS-OK | -0.46% |
| [WOCKPHARMA](https://in.tradingview.com/chart/?symbol=NSE:WOCKPHARMA)<br><sub>✓ SAFE . →147Cr · 179Cr . ↑CMF14d</sub> | 2078.00 | -10.8% | +88.9% | 3d | SMA-OK | RS-OK | -3.45% |
| [VIJAYA](https://in.tradingview.com/chart/?symbol=NSE:VIJAYA)<br><sub>✓ SAFE . ↗59Cr · 139Cr . ↑CMF23d</sub> | 1627.70 | 0.0% | +89.0% | 3d | SMA-OK | RS-OK | +3.50% |
| [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK)<br><sub>✓ SAFE . ↘112Cr · 136Cr . ↑CMF9d</sub> | 390.45 | -8.8% | +35.3% | 3d | SMA-OK | RS-OK | -0.78% |
| [TI](https://in.tradingview.com/chart/?symbol=NSE:TI)<br><sub>✓ SAFE . ↗51Cr · 105Cr . ↑CMF16d</sub> | 558.30 | -7.2% | +43.6% | 3d | SMA-OK | RS-OK | +1.34% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>✓ SAFE . ↘68Cr · 95Cr . ↓CMF19d</sub> | 1183.30 | -3.4% | +57.6% | 3d | SMA-OK | RS-OK | +0.26% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>✓ SAFE . ↘136Cr · 47Cr . ↑CMF11d</sub> | 2615.10 | -2.0% | +35.7% | 6d | SMA-OK | RS-OK | -1.87% |
| [UNOMINDA](https://in.tradingview.com/chart/?symbol=NSE:UNOMINDA)<br><sub>✓ SAFE . ↘139Cr · 106Cr . ↑CMF19d</sub> | 1375.00 | -0.9% | +35.7% | 7d | SMA-OK | RS-OK | +1.33% |
| [IGIL](https://in.tradingview.com/chart/?symbol=NSE:IGIL)<br><sub>✓ SAFE . ↘34Cr · 42Cr . ↓CMF3d</sub> | 432.50 | -4.0% | +48.6% | 7d | SMA-OK | RS-OK | +0.32% |
| [GREAVESCOT](https://in.tradingview.com/chart/?symbol=NSE:GREAVESCOT)<br><sub>✓ SAFE . ↗379Cr · 1268Cr . ↑CMF17d</sub> | 309.44 | 0.0% | +156.6% | 8d | SMA-OK | RS-OK | +14.98% |
| [INDIGO](https://in.tradingview.com/chart/?symbol=NSE:INDIGO)<br><sub>✓ SAFE . →499Cr · 262Cr . ↑CMF11d</sub> | 5523.00 | -6.7% | +40.1% | 8d | SMA-OK | RS-OK | -1.16% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>⚠ CAUTION . →238Cr · 285Cr . ↑CMF27d</sub> | 356.20 | -4.6% | +44.3% | 8d | SMA-OK | RS-OK | -1.00% |
| [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN)<br><sub>✓ SAFE . ↘42Cr · 53Cr . ↑CMF30d</sub> | 11769.00 | -1.3% | +79.8% | 8d | SMA-OK | RS-OK | +1.03% |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML)<br><sub>✓ SAFE . ↘38Cr · 52Cr . ↓CMF1d</sub> | 2041.20 | -4.4% | +49.1% | 8d | SMA-OK | RS-OK | +1.65% |
| [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX)<br><sub>✓ SAFE . ↗44Cr · 33Cr . ↓CMF6d</sub> | 111.88 | -0.1% | +203.2% | 8d | SMA-OK | RS-OK | +3.58% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>✓ SAFE . ↗185Cr · 32Cr . ↑CMF9d</sub> | 1501.80 | -8.5% | +82.5% | 8d | SMA-OK | RS-OK | -0.40% |
| [MAXESTATES](https://in.tradingview.com/chart/?symbol=NSE:MAXESTATES)<br><sub>⚠ CAUTION . ↗10Cr · 27Cr . ↑CMF9d</sub> | 614.35 | -0.4% | +99.0% | 8d | SMA-OK | RS-OK | +2.79% |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>✓ SAFE . ↘141Cr · 128Cr . ↑CMF13d</sub> | 1219.00 | -7.4% | +80.1% | 9d | SMA-OK | RS-OK | +0.02% |
| [POONAWALLA](https://in.tradingview.com/chart/?symbol=NSE:POONAWALLA)<br><sub>✓ SAFE . ↘105Cr · 104Cr . ↑CMF18d</sub> | 513.45 | -1.0% | +39.4% | 9d | SMA-OK | RS-OK | -0.76% |
| [PETRONET](https://in.tradingview.com/chart/?symbol=NSE:PETRONET)<br><sub>✓ SAFE . →101Cr · 62Cr . ↑CMF22d</sub> | 327.00 | -2.4% | +37.4% | 9d | SMA-OK | RS-OK | +0.29% |
| [LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS)<br><sub>✓ SAFE . ↘38Cr · 44Cr . ↑CMF30d</sub> | 4178.00 | -11.0% | +37.1% | 9d | SMA-OK | RS-OK | -1.06% |
| [PARAGMILK](https://in.tradingview.com/chart/?symbol=NSE:PARAGMILK)<br><sub>✓ SAFE . ↘48Cr · 34Cr . ↑CMF15d</sub> | 338.40 | -1.7% | +88.1% | 9d | SMA-OK | RS-OK | -1.50% |
| [TANLA](https://in.tradingview.com/chart/?symbol=NSE:TANLA)<br><sub>✓ SAFE . ↘53Cr · 39Cr . ↑CMF10d</sub> | 649.50 | -11.4% | +72.1% | 10d | SMA-OK | RS-OK | -4.56% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>✓ SAFE . →238Cr · 250Cr . ↑CMF14d</sub> | 794.10 | 0.0% | +57.5% | 11d | SMA-OK | RS-OK | +1.16% |
| [URBANCO](https://in.tradingview.com/chart/?symbol=NSE:URBANCO)<br><sub>✓ SAFE . ↗244Cr · 174Cr . ↑CMF10d</sub> | 164.85 | -9.0% | +60.0% | 11d | SMA-OK | RS-OK | -2.27% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>✓ SAFE . →79Cr · 50Cr . ↑CMF10d</sub> | 339.80 | -7.9% | +90.1% | 12d | SMA-OK | RS-OK | -0.42% |
| [DCBBANK](https://in.tradingview.com/chart/?symbol=NSE:DCBBANK)<br><sub>✓ SAFE . ↗35Cr · 49Cr . ↑CMF3d</sub> | 241.64 | 0.0% | +52.6% | 12d | SMA-OK | RS-OK | +1.56% |
| [PDSL](https://in.tradingview.com/chart/?symbol=NSE:PDSL)<br><sub>✓ SAFE . ↘11Cr · 29Cr . ↑CMF17d</sub> | 418.95 | 0.0% | +65.0% | 12d | SMA-OK | RS-OK | +1.38% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>✓ SAFE . ↗1169Cr · 527Cr . ↑CMF13d</sub> | 636.35 | -10.5% | +92.4% | 13d | SMA-OK | RS-OK | -2.53% |
| [RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO)<br><sub>✓ SAFE . ↘157Cr · 182Cr . ↑CMF19d</sub> | 4699.00 | -0.7% | +84.9% | 13d | SMA-OK | RS-OK | +1.35% |
| [MOTILALOFS](https://in.tradingview.com/chart/?symbol=NSE:MOTILALOFS)<br><sub>✓ SAFE . →208Cr · 140Cr . ↑CMF14d</sub> | 1230.10 | -0.8% | +95.8% | 13d | SMA-OK | RS-OK | -0.40% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>✓ SAFE . ↘120Cr · 100Cr . ↑CMF12d</sub> | 415.80 | -2.1% | +42.3% | 13d | SMA-OK | RS-OK | -1.70% |
| [STYLEBAAZA](https://in.tradingview.com/chart/?symbol=NSE:STYLEBAAZA)<br><sub>✓ SAFE . ↗173Cr · 64Cr . ↑CMF12d</sub> | 515.50 | -4.4% | +117.4% | 13d | SMA-OK | RS-OK | +2.41% |
| [YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH)<br><sub>✓ SAFE . ↘24Cr · 46Cr . ↑CMF16d</sub> | 1080.80 | -7.0% | +96.2% | 13d | SMA-OK | RS-OK | -0.39% |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE)<br><sub>✓ SAFE . →40Cr · 42Cr . ↓CMF10d</sub> | 1190.35 | -5.1% | +58.9% | 13d | SMA-OK | RS-OK | +0.24% |
| [JYOTICNC](https://in.tradingview.com/chart/?symbol=NSE:JYOTICNC)<br><sub>✓ SAFE . ↘36Cr · 41Cr . ↑CMF15d</sub> | 1019.20 | -8.5% | +74.1% | 13d | SMA-OK | RS-OK | -2.28% |
| [APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD)<br><sub>✓ SAFE . ↘30Cr · 34Cr . ↑CMF20d</sub> | 1030.45 | -2.5% | +59.4% | 13d | SMA-OK | RS-OK | +1.34% |
| [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS)<br><sub>✓ SAFE . ↘28Cr · 32Cr . ↑CMF15d</sub> | 192.02 | -12.0% | +88.3% | 13d | SMA-OK | RS-OK | -0.77% |
| [MEDANTA](https://in.tradingview.com/chart/?symbol=NSE:MEDANTA)<br><sub>✓ SAFE . ↘29Cr · 31Cr . ↑CMF16d</sub> | 1528.50 | 0.0% | +59.0% | 13d | SMA-OK | RS-OK | +1.89% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>✓ SAFE . ↘58Cr · 29Cr . ↑CMF20d</sub> | 745.75 | -5.8% | +61.2% | 13d | SMA-OK | RS-OK | -0.48% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>✓ SAFE . →432Cr · 304Cr . ↑CMF22d</sub> | 4528.20 | -1.6% | +37.9% | 15d | SMA-OK | RS-OK | -1.35% |
| [MAHABANK](https://in.tradingview.com/chart/?symbol=NSE:MAHABANK)<br><sub>✓ SAFE . ↗212Cr · 200Cr . ↑CMF21d</sub> | 98.71 | -0.7% | +75.6% | 15d | SMA-OK | RS-OK | +1.18% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>✓ SAFE . ↘24Cr · 73Cr . ↑CMF13d</sub> | 1898.00 | -10.3% | +100.0% | 15d | SMA-OK | RS-OK | +0.76% |
| [KDDL](https://in.tradingview.com/chart/?symbol=NSE:KDDL)<br><sub>✓ SAFE . ↗109Cr · 32Cr . ↑CMF14d</sub> | 4531.20 | -7.1% | +123.7% | 15d | SMA-OK | RS-OK | -1.58% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>✓ SAFE . ↗130Cr · 242Cr . ↑CMF5d</sub> | 378.75 | -3.7% | +57.1% | 16d | SMA-OK | RS-OK | -1.39% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>✓ SAFE . →175Cr · 75Cr . ↑CMF14d</sub> | 185.60 | -3.4% | +37.1% | 16d | SMA-OK | RS-OK | -3.05% |
| [HONASA](https://in.tradingview.com/chart/?symbol=NSE:HONASA)<br><sub>✓ SAFE . ↗104Cr · 87Cr . ↑CMF10d</sub> | 536.45 | -0.6% | +109.3% | 16d | SMA-OK | RS-OK | -0.61% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>✓ SAFE . ↘31Cr · 43Cr . ↑CMF23d</sub> | 968.20 | 0.0% | +64.7% | 16d | SMA-OK | RS-OK | +1.13% |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>✓ SAFE . →57Cr · 43Cr . ↑CMF15d</sub> | 4731.80 | -5.0% | +59.3% | 16d | SMA-OK | RS-OK | -3.33% |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . ↘724Cr · 843Cr . ↑CMF21d</sub> | 3565.00 | -4.4% | +80.7% | 17d | SMA-OK | RS-OK | -0.46% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>✓ SAFE . ↗265Cr · 218Cr . ↑CMF20d</sub> | 1798.00 | -3.1% | +60.3% | 17d | SMA-OK | RS-OK | -0.06% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>✓ SAFE . ↘45Cr · 59Cr . ↓CMF2d</sub> | 2028.30 | -0.6% | +55.1% | 17d | SMA-OK | RS-OK | -0.60% |
| [EMCURE](https://in.tradingview.com/chart/?symbol=NSE:EMCURE)<br><sub>✓ SAFE . ↘52Cr · 28Cr . ↑CMF23d</sub> | 2313.50 | -2.0% | +69.5% | 17d | SMA-OK | RS-OK | +0.16% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [GLENMARK](https://in.tradingview.com/chart/?symbol=NSE:GLENMARK)<br><sub>✓ SAFE . ↘146Cr · 229Cr . ↑CMF17d</sub> | 2719.00 | 0.0% | +41.6% | 18d | SMA-OK | RS-OK | +2.33% |
| [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN)<br><sub>✓ SAFE . ↗51Cr · 78Cr . ↓CMF17d</sub> | 653.55 | -1.9% | +54.3% | 18d | SMA-OK | RS-OK | +0.27% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↘70Cr · 72Cr . ↑CMF11d</sub> | 4708.50 | -1.9% | +189.0% | 18d | SMA-OK | RS-OK | +1.93% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>✓ SAFE . ↘21Cr · 29Cr . ↑CMF23d</sub> | 1711.60 | -8.0% | +178.2% | 18d | SMA-OK | RS-OK | +2.14% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . →225Cr · 203Cr . ↑CMF21d</sub> | 9956.00 | -3.1% | +79.0% | 19d | SMA-OK | RS-OK | -1.95% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↘186Cr · 179Cr . ↑CMF17d</sub> | 276.57 | 0.0% | +155.3% | 19d | SMA-OK | RS-OK | +2.15% |
| [KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL)<br><sub>✓ SAFE . ↗64Cr · 178Cr . ↓CMF0d . DEL79%(T-1)</sub> | 1173.00 | -3.7% | +44.7% | 19d | SMA-OK | RS-OK | -2.81% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>✓ SAFE . ↘139Cr · 111Cr . ↑CMF18d</sub> | 48800.00 | -7.0% | +69.8% | 19d | SMA-OK | RS-OK | -1.13% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . ↘156Cr · 69Cr . ↑CMF18d</sub> | 1799.30 | -6.7% | +126.3% | 19d | SMA-OK | RS-OK | -0.54% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . ↗1100Cr · 1390Cr . ↑CMF19d</sub> | 11203.00 | -3.1% | +92.5% | 20d | SMA-OK | RS-OK | +0.20% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . ↘144Cr · 144Cr . ↑CMF29d</sub> | 357.00 | -2.2% | +52.1% | 20d | SMA-OK | RS-OK | -1.92% |
| [PHOENIXLTD](https://in.tradingview.com/chart/?symbol=NSE:PHOENIXLTD)<br><sub>⚠ CAUTION . ↗136Cr · 158Cr . ↑CMF14d</sub> | 2285.50 | -0.3% | +54.7% | 20d | SMA-OK | RS-OK | +0.41% |
| [ETERNAL](https://in.tradingview.com/chart/?symbol=NSE:ETERNAL)<br><sub>⚠ CAUTION . →730Cr · 535Cr . ↑CMF17d</sub> | 362.10 | -3.5% | +67.9% | 21d | SMA-OK | RS-OK | -0.52% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>✓ SAFE . ↘374Cr · 376Cr . ↑CMF30d</sub> | 1919.00 | -1.6% | +47.2% | 21d | SMA-OK | RS-OK | +0.10% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>✓ SAFE . ↘137Cr · 633Cr . ↑CMF20d</sub> | 232.54 | -5.6% | +74.5% | 21d | SMA-OK | RS-OK | -1.84% |
| [CEMPRO](https://in.tradingview.com/chart/?symbol=NSE:CEMPRO)<br><sub>✓ SAFE . ↘50Cr · 34Cr . ↑CMF7d</sub> | 1414.70 | -13.7% | +177.6% | 21d | SMA-OK | RS-OK | -1.68% |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH)<br><sub>✓ SAFE . ↘29Cr · 26Cr . ↓CMF0d</sub> | 2386.40 | -0.7% | +85.4% | 21d | SMA-OK | RS-OK | +2.58% |
| [ARIS](https://in.tradingview.com/chart/?symbol=NSE:ARIS)<br><sub>✓ SAFE . ↗82Cr · 302Cr . ↑CMF30d</sub> | 190.30 | 0.0% | +126.1% | 22d | SMA-OK | RS-OK | +14.09% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↘132Cr · 168Cr . ↑CMF22d</sub> | 883.15 | -4.6% | +98.7% | 22d | SMA-OK | RS-OK | -0.32% |
| [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA)<br><sub>✓ SAFE . ↘44Cr · 90Cr . ↑CMF30d</sub> | 620.55 | -8.4% | +99.5% | 22d | SMA-OK | RS-OK | -5.63% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↘72Cr · 69Cr . ↑CMF30d</sub> | 3348.40 | -1.1% | +109.7% | 22d | SMA-OK | RS-OK | +1.55% |
| [AARTIPHARM](https://in.tradingview.com/chart/?symbol=NSE:AARTIPHARM)<br><sub>✓ SAFE . →70Cr · 46Cr . ↑CMF17d</sub> | 1025.45 | 0.0% | +73.2% | 22d | SMA-OK | RS-OK | +0.47% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . ↘389Cr · 539Cr . ↑CMF22d</sub> | 1871.90 | -5.4% | +211.3% | 23d | SMA-OK | RS-OK | -5.42% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>✓ SAFE . →400Cr · 326Cr . ↑CMF22d</sub> | 906.00 | -0.7% | +58.7% | 23d | SMA-OK | RS-OK | -0.66% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>✓ SAFE . ↘160Cr · 161Cr . ↑CMF22d</sub> | 3993.00 | -1.1% | +149.2% | 23d | SMA-OK | RS-OK | +3.05% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>✓ SAFE . ↘31Cr · 61Cr . ↑CMF30d</sub> | 7628.00 | -4.3% | +182.0% | 24d | SMA-OK | RS-OK | -3.38% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>✓ SAFE . ↗639Cr · 808Cr . ↑CMF21d</sub> | 2060.00 | -3.8% | +91.8% | 29d | SMA-OK | RS-OK | -3.84% |
| [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC)<br><sub>✓ SAFE . →31Cr · 39Cr . ↓CMF0d</sub> | 764.95 | -8.2% | +55.8% | 33d | SMA-OK | RS-OK | -5.00% |
| [SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK)<br><sub>✓ SAFE . →87Cr · 98Cr . ↑CMF30d</sub> | 58.77 | -5.0% | +74.9% | 34d | SMA-OK | RS-OK | -0.17% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . ↘125Cr · 111Cr . ↑CMF0d</sub> | 1709.30 | -0.3% | +86.1% | 41d | SMA-OK | RS-OK | +0.56% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↗512Cr · 250Cr . ↑CMF9d</sub> | 366.35 | -4.8% | +457.2% | 42d | SMA-OK | RS-OK | +1.16% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>✓ SAFE . ↗65Cr · 40Cr . ↑CMF5d</sub> | 807.20 | -0.1% | +110.1% | 43d | SMA-OK | RS-OK | +0.54% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . →78Cr · 64Cr . ↓CMF20d</sub> | 68.27 | -3.0% | +164.8% | 63d | SMA-OK | RS-OK | +0.29% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . ↘51Cr · 60Cr . ↑CMF30d</sub> | 908.15 | -0.7% | +196.4% | 63d | SMA-OK | RS-OK | -0.20% |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA)<br><sub>✓ SAFE . ↘25Cr · 48Cr . ↑CMF9d</sub> | 680.55 | -2.5% | +74.7% | 72d | SMA-OK | RS-OK | -0.85% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . →60Cr · 42Cr . ↑CMF9d</sub> | 1189.90 | -8.5% | +269.7% | 73d | SMA-OK | RS-OK | -1.27% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . ↘98Cr · 130Cr . ↑CMF2d</sub> | 404.55 | 0.0% | +208.1% | 90d | SMA-OK | RS-OK | +0.31% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↘32Cr · 27Cr . ↑CMF30d</sub> | 494.20 | -13.7% | +190.0% | 92d | SMA-OK | RS-OK | +0.76% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . ↘109Cr · 186Cr . ↑CMF21d</sub> | 173.66 | 0.0% | +214.4% | 93d | SMA-OK | RS-OK | +0.09% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . →717Cr · 457Cr . ↑CMF20d</sub> | 2370.70 | -3.4% | +154.9% | 138d | SMA-OK | RS-OK | +3.32% |

### By Trend Age

**<2 WEEKS** (40)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AETHER,NSE:ARFIN,NSE:BAJAJHLDNG,NSE:BEML,NSE:COHANCE,NSE:CPPLUS,NSE:CRAFTSMAN,NSE:FEDERALBNK,NSE:FILATEX,NSE:GABRIEL,NSE:GESHIP,NSE:GRANULES,NSE:GRAPHITE,NSE:GREAVESCOT,NSE:IGIL,NSE:IIFL,NSE:INDIGO,NSE:JSWINFRA,NSE:KOPRAN,NSE:LGEINDIA,NSE:LODHA,NSE:LTTS,NSE:MANKIND,NSE:MAXESTATES,NSE:MOTHERSON,NSE:NEULANDLAB,NSE:PARAGMILK,NSE:PETRONET,NSE:PNBHOUSING,NSE:POONAWALLA,NSE:PTCIL,NSE:RBLBANK,NSE:SAMBHV,NSE:TANLA,NSE:TECHM,NSE:TI,NSE:UNOMINDA,NSE:VIJAYA,NSE:WOCKPHARMA,NSE:ZYDUSLIFE
```

**2-4 WEEKS** (48)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABCAPITAL,NSE:ACE,NSE:ADANIPORTS,NSE:ANTHEM,NSE:APLLTD,NSE:AUROPHARMA,NSE:BOSCHLTD,NSE:CEMPRO,NSE:DCBBANK,NSE:DIVISLAB,NSE:DLF,NSE:EMCURE,NSE:ENTERO,NSE:ETERNAL,NSE:FLUOROCHEM,NSE:GAIL,NSE:GLENMARK,NSE:HFCL,NSE:HONASA,NSE:INDGN,NSE:JYOTICNC,NSE:KALYANKJIL,NSE:KARURVYSYA,NSE:KDDL,NSE:KPRMILL,NSE:KTKBANK,NSE:LALPATHLAB,NSE:LUMAXTECH,NSE:MAHABANK,NSE:MCX,NSE:MEDANTA,NSE:MOTILALOFS,NSE:NAVINFLUOR,NSE:NYKAA,NSE:PDSL,NSE:PHOENIXLTD,NSE:PPLPHARMA,NSE:RADICO,NSE:RKFORGE,NSE:ROLEXRINGS,NSE:RUBICON,NSE:SAILIFE,NSE:SANSERA,NSE:STYLEBAAZA,NSE:TVSMOTOR,NSE:URBANCO,NSE:WELSPUNLIV,NSE:YATHARTH
```

**1-2 MONTHS** (15)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AARTIPHARM,NSE:ACUTAAS,NSE:ARIS,NSE:ATHERENERG,NSE:COFORGE,NSE:CUPID,NSE:GLAND,NSE:GRWRHITECH,NSE:INDHOTEL,NSE:PVRINOX,NSE:SAREGAMA,NSE:SONACOMS,NSE:SOUTHBANK,NSE:STLTECH,NSE:TIPSMUSIC
```

**2-3 MONTHS** (3)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:SBC,NSE:SHREEJISPG
```

**3-6 MONTHS** (5)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:RATNAVEER,NSE:RAYMOND,NSE:SSWL,NSE:TFCILTD,NSE:THELEELA
```

**6+ MONTHS** (1)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LAURUSLABS
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
