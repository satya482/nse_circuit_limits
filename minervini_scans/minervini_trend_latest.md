> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-11-16
*Generated 2026-11-16 16:24 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP) | [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER) |
| [LOTUSDEV](https://in.tradingview.com/chart/?symbol=NSE:LOTUSDEV) | [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS) |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING) | [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM) |
| [TIIL](https://in.tradingview.com/chart/?symbol=NSE:TIIL) | [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP) |
| [TITAN](https://in.tradingview.com/chart/?symbol=NSE:TITAN) | [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED) |
|  | [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE) |

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
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABCAPITAL,NSE:ACE,NSE:ALICON,NSE:APLLTD,NSE:APOLLO,NSE:ASAHIINDIA,NSE:ASTRAMICRO,NSE:BALUFORGE,NSE:BHEL,NSE:BOROLTD,NSE:CENTUM,NSE:DIACABS,NSE:DLF,NSE:ENGINERSIN,NSE:FEDERALBNK,NSE:FILATEX,NSE:FLUOROCHEM,NSE:GABRIEL,NSE:GESHIP,NSE:GRAPHITE,NSE:GREAVESCOT,NSE:HINDOILEXP,NSE:HONASA,NSE:INDIGO,NSE:ITDC,NSE:JAMNAAUTO,NSE:JYOTICNC,NSE:KALYANKJIL,NSE:KARURVYSYA,NSE:KOTAKBANK,NSE:KTKBANK,NSE:LALPATHLAB,NSE:LODHA,NSE:LOTUSDEV,NSE:LTTS,NSE:MAHABANK,NSE:MANAKCOAT,NSE:MANKIND,NSE:MCX,NSE:MOTHERSON,NSE:MOTILALOFS,NSE:MSTCLTD,NSE:NEULANDLAB,NSE:PARAGMILK,NSE:PAYTM,NSE:PETRONET,NSE:PNBHOUSING,NSE:POONAWALLA,NSE:QPOWER,NSE:RADICO,NSE:RKFORGE,NSE:ROLEXRINGS,NSE:ROSSTECH,NSE:RPEL,NSE:STYLEBAAZA,NSE:TANLA,NSE:TIIL,NSE:TITAN,NSE:TVSMOTOR,NSE:TVSSRICHAK,NSE:UFLEX,NSE:UNIMECH,NSE:URBANCO,NSE:VIJAYA,NSE:VRLLOG,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AARTIDRUGS,NSE:AARTIPHARM,NSE:ACUTAAS,NSE:ADANIPORTS,NSE:ALIVUS,NSE:ATHERENERG,NSE:AUROPHARMA,NSE:BOSCHLTD,NSE:DIVISLAB,NSE:ETERNAL,NSE:GAIL,NSE:GLAND,NSE:GLENMARK,NSE:GRWRHITECH,NSE:HFCL,NSE:INDGN,NSE:INDHOTEL,NSE:KPRMILL,NSE:NAVINFLUOR,NSE:NUVAMA,NSE:NYKAA,NSE:PHOENIXLTD,NSE:PPLPHARMA,NSE:SAILIFE,NSE:SANSERA,NSE:SAREGAMA,NSE:SGFIN,NSE:SGMART,NSE:SKYGOLD,NSE:SONACOMS,NSE:TECHM,NSE:WELSPUNLIV,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABDL,NSE:COFORGE,NSE:CUPID,NSE:KROSS,NSE:PVRINOX,NSE:SIGMAADV,NSE:SOUTHBANK,NSE:STLTECH,NSE:TIPSMUSIC,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:GCSL,NSE:MOREPENLAB,NSE:SBC,NSE:SHREEJISPG,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:NAZARA,NSE:RATNAVEER,NSE:RAYMOND,NSE:SAMBHV,NSE:TFCILTD,###6+ MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:LAURUSLABS
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [TVSSRICHAK](https://in.tradingview.com/chart/?symbol=NSE:TVSSRICHAK)<br><sub>✓ SAFE . ↗18Cr · 159Cr . ↓CMF30d</sub> | 4647.30 | -15.9% | +44.7% | 0d | SMA-OK | RS-OK | +7.19% |
| [VIJAYA](https://in.tradingview.com/chart/?symbol=NSE:VIJAYA)<br><sub>⚠ CAUTION . ↗32Cr · 123Cr . ↑CMF16d</sub> | 1487.50 | -5.3% | +72.7% | 0d | SMA-OK | RS-OK | +5.49% |
| [NEULANDLAB](https://in.tradingview.com/chart/?symbol=NSE:NEULANDLAB)<br><sub>✓ SAFE . ↗153Cr · 123Cr . ↑CMF8d</sub> | 21640.00 | -9.8% | +87.3% | 0d | SMA-OK | RS-OK | +2.67% |
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP)<br><sub>✓ SAFE . ↗150Cr · 118Cr . ↑CMF1d</sub> | 1532.90 | -10.9% | +44.1% | 0d | SMA-OK | RS-OK | +0.98% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>✓ SAFE . ↘67Cr · 41Cr . ↓CMF12d</sub> | 1135.90 | -7.3% | +51.3% | 0d | SMA-OK | RS-OK | +1.66% |
| [LOTUSDEV](https://in.tradingview.com/chart/?symbol=NSE:LOTUSDEV)<br><sub>✓ SAFE . ↘31Cr · 41Cr . ↑CMF30d</sub> | 231.77 | -6.6% | +125.4% | 0d | SMA-OK | RS-OK | +1.68% |
| [TITAN](https://in.tradingview.com/chart/?symbol=NSE:TITAN)<br><sub>⚠ CAUTION . ↗613Cr · 448Cr . ↑CMF9d</sub> | 4910.00 | -5.0% | +30.3% | 1d | SMA-OK | RS-OK | +1.34% |
| [HINDOILEXP](https://in.tradingview.com/chart/?symbol=NSE:HINDOILEXP)<br><sub>✓ SAFE . ↗69Cr · 424Cr . ↑CMF3d</sub> | 212.66 | 0.0% | +79.7% | 1d | SMA-OK | RS-OK | +10.53% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>✓ SAFE . →409Cr · 316Cr . ↑CMF1d</sub> | 430.10 | -7.3% | +77.4% | 1d | SMA-OK | RS-OK | -1.42% |
| [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON)<br><sub>✓ SAFE . ↗392Cr · 270Cr . ↑CMF10d</sub> | 162.98 | -4.5% | +55.1% | 1d | SMA-OK | RS-OK | -1.10% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>⚠ CAUTION . →237Cr · 215Cr . ↑CMF20d</sub> | 362.00 | -2.6% | +48.1% | 1d | SMA-OK | RS-OK | +0.29% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>✓ SAFE . ↘155Cr · 112Cr . ↑CMF6d</sub> | 2626.60 | -1.6% | +36.3% | 1d | SMA-OK | RS-OK | -0.51% |
| [MSTCLTD](https://in.tradingview.com/chart/?symbol=NSE:MSTCLTD)<br><sub>✓ SAFE . ↗74Cr · 81Cr . ↑CMF1d</sub> | 756.50 | -3.7% | +106.8% | 1d | SMA-OK | RS-OK | -3.43% |
| [ASTRAMICRO](https://in.tradingview.com/chart/?symbol=NSE:ASTRAMICRO)<br><sub>✓ SAFE . ↗95Cr · 69Cr . ↑CMF0d</sub> | 1697.20 | -8.8% | +98.3% | 1d | SMA-OK | RS-OK | -0.37% |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE)<br><sub>✓ SAFE . ↗69Cr · 61Cr . ↑CMF8d</sub> | 797.95 | -6.3% | +51.7% | 1d | SMA-OK | RS-OK | -0.25% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>✓ SAFE . ↗157Cr · 46Cr . ↑CMF2d</sub> | 1492.20 | -9.1% | +81.3% | 1d | SMA-OK | RS-OK | -3.90% |
| [UFLEX](https://in.tradingview.com/chart/?symbol=NSE:UFLEX)<br><sub>✓ SAFE . ↗17Cr · 46Cr . ↓CMF30d</sub> | 630.55 | -10.2% | +88.6% | 1d | SMA-OK | RS-OK | +1.98% |
| [ITDC](https://in.tradingview.com/chart/?symbol=NSE:ITDC)<br><sub>✓ SAFE . ↗25Cr · 30Cr . ↓CMF19d</sub> | 674.80 | -15.0% | +82.1% | 1d | SMA-OK | RS-OK | +1.03% |
| [GREAVESCOT](https://in.tradingview.com/chart/?symbol=NSE:GREAVESCOT)<br><sub>✓ SAFE . ↘35Cr · 29Cr . ↑CMF10d</sub> | 228.12 | -13.5% | +89.1% | 1d | SMA-OK | RS-OK | +0.95% |
| [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX)<br><sub>✓ SAFE . →15Cr · 28Cr . ↑CMF0d</sub> | 103.47 | -7.6% | +180.4% | 1d | SMA-OK | RS-OK | +2.76% |
| [PARAGMILK](https://in.tradingview.com/chart/?symbol=NSE:PARAGMILK)<br><sub>✓ SAFE . ↗183Cr · 105Cr . ↑CMF8d</sub> | 344.14 | -4.2% | +91.3% | 2d | SMA-OK | RS-OK | +3.90% |
| [PETRONET](https://in.tradingview.com/chart/?symbol=NSE:PETRONET)<br><sub>✓ SAFE . ↗136Cr · 66Cr . ↑CMF15d</sub> | 326.00 | -2.7% | +36.9% | 2d | SMA-OK | RS-OK | +0.60% |
| [POONAWALLA](https://in.tradingview.com/chart/?symbol=NSE:POONAWALLA)<br><sub>✓ SAFE . ↘76Cr · 49Cr . ↑CMF11d</sub> | 490.50 | -2.4% | +33.1% | 2d | SMA-OK | RS-OK | +1.18% |
| [CENTUM](https://in.tradingview.com/chart/?symbol=NSE:CENTUM)<br><sub>✓ SAFE . ↗29Cr · 30Cr . ↓CMF14d</sub> | 4336.50 | -11.9% | +107.2% | 2d | SMA-OK | RS-OK | -3.23% |
| [VRLLOG](https://in.tradingview.com/chart/?symbol=NSE:VRLLOG)<br><sub>✓ SAFE . ↗131Cr · 28Cr . ↓CMF30d</sub> | 340.30 | 0.0% | +48.2% | 2d | SMA-OK | RS-OK | +0.06% |
| [LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS)<br><sub>✓ SAFE . ↘42Cr · 27Cr . ↑CMF24d</sub> | 4226.00 | -10.0% | +38.7% | 2d | SMA-OK | RS-OK | -0.50% |
| [INDIGO](https://in.tradingview.com/chart/?symbol=NSE:INDIGO)<br><sub>✓ SAFE . ↗588Cr · 347Cr . ↑CMF6d</sub> | 5544.00 | -6.3% | +40.6% | 3d | SMA-OK | RS-OK | -0.77% |
| [BALUFORGE](https://in.tradingview.com/chart/?symbol=NSE:BALUFORGE)<br><sub>✓ SAFE . ↗56Cr · 97Cr . ↑CMF7d</sub> | 520.40 | -20.4% | +46.1% | 3d | SMA-OK | RS-OK | -5.43% |
| [ASAHIINDIA](https://in.tradingview.com/chart/?symbol=NSE:ASAHIINDIA)<br><sub>⚠ CAUTION . ↗47Cr · 65Cr . ↑CMF13d</sub> | 1165.05 | 0.0% | +48.5% | 3d | SMA-OK | RS-OK | +4.94% |
| [TANLA](https://in.tradingview.com/chart/?symbol=NSE:TANLA)<br><sub>✓ SAFE . →101Cr · 46Cr . ↑CMF3d</sub> | 701.20 | -4.3% | +85.8% | 3d | SMA-OK | RS-OK | -4.33% |
| [TIIL](https://in.tradingview.com/chart/?symbol=NSE:TIIL)<br><sub>✓ SAFE . →10Cr · 46Cr . ↑CMF11d</sub> | 2939.20 | -14.9% | +54.1% | 3d | SMA-OK | RS-OK | +1.79% |
| [JAMNAAUTO](https://in.tradingview.com/chart/?symbol=NSE:JAMNAAUTO)<br><sub>✓ SAFE . ↗41Cr · 119Cr . ↓CMF0d</sub> | 144.07 | -5.1% | +38.5% | 4d | SMA-OK | RS-OK | -3.26% |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>✓ SAFE . →176Cr · 107Cr . ↑CMF8d</sub> | 1192.80 | -9.4% | +76.2% | 4d | SMA-OK | RS-OK | -2.23% |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER)<br><sub>✓ SAFE . ↘45Cr · 56Cr . ↓CMF22d</sub> | 1525.90 | -7.5% | +156.4% | 4d | SMA-OK | RS-OK | +3.02% |
| [URBANCO](https://in.tradingview.com/chart/?symbol=NSE:URBANCO)<br><sub>✓ SAFE . ↘61Cr · 50Cr . ↑CMF3d</sub> | 171.70 | -5.2% | +66.7% | 4d | SMA-OK | RS-OK | +1.71% |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH)<br><sub>✓ SAFE . ↗25Cr · 36Cr . ↓CMF14d</sub> | 1574.30 | -3.0% | +174.3% | 4d | SMA-OK | RS-OK | +2.00% |
| [KOTAKBANK](https://in.tradingview.com/chart/?symbol=NSE:KOTAKBANK)<br><sub>⚠ CAUTION . →923Cr · 659Cr . ↑CMF10d</sub> | 494.20 | 0.0% | +39.8% | 5d | SMA-OK | RS-OK | +1.16% |
| [BOROLTD](https://in.tradingview.com/chart/?symbol=NSE:BOROLTD)<br><sub>✓ SAFE . ↘27Cr · 163Cr . ↑CMF11d</sub> | 341.10 | 0.0% | +58.2% | 5d | SMA-OK | RS-OK | +9.50% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>✓ SAFE . →93Cr · 119Cr . ↑CMF3d</sub> | 363.40 | -0.7% | +108.0% | 5d | SMA-OK | RS-OK | +0.40% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>✓ SAFE . ↗1519Cr · 1467Cr . ↑CMF6d</sub> | 708.15 | -0.4% | +114.1% | 6d | SMA-OK | RS-OK | +1.60% |
| [STYLEBAAZA](https://in.tradingview.com/chart/?symbol=NSE:STYLEBAAZA)<br><sub>✓ SAFE . ↗133Cr · 410Cr . ↑CMF5d</sub> | 511.70 | 0.0% | +115.8% | 6d | SMA-OK | RS-OK | +9.16% |
| [RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO)<br><sub>✓ SAFE . ↘195Cr · 154Cr . ↑CMF12d</sub> | 4665.00 | -1.4% | +83.6% | 6d | SMA-OK | RS-OK | +1.30% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>✓ SAFE . ↗257Cr · 116Cr . ↑CMF9d</sub> | 754.75 | -1.9% | +49.7% | 6d | SMA-OK | RS-OK | -0.53% |
| [MOTILALOFS](https://in.tradingview.com/chart/?symbol=NSE:MOTILALOFS)<br><sub>✓ SAFE . ↗257Cr · 103Cr . ↑CMF7d</sub> | 1217.00 | -0.2% | +93.7% | 6d | SMA-OK | RS-OK | -0.25% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>✓ SAFE . →103Cr · 76Cr . ↑CMF13d</sub> | 791.85 | 0.0% | +71.1% | 6d | SMA-OK | RS-OK | +0.91% |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN)<br><sub>✓ SAFE . ↘131Cr · 65Cr . ↑CMF10d</sub> | 312.05 | -1.1% | +89.6% | 6d | SMA-OK | RS-OK | -0.13% |
| [APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD)<br><sub>✓ SAFE . ↗123Cr · 48Cr . ↑CMF13d</sub> | 1057.10 | 0.0% | +63.5% | 6d | SMA-OK | RS-OK | +2.62% |
| [JYOTICNC](https://in.tradingview.com/chart/?symbol=NSE:JYOTICNC)<br><sub>✓ SAFE . ↗148Cr · 40Cr . ↑CMF8d</sub> | 1072.40 | -3.7% | +83.2% | 6d | SMA-OK | RS-OK | -0.07% |
| [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS)<br><sub>✓ SAFE . ↗107Cr · 31Cr . ↑CMF8d</sub> | 209.36 | -4.1% | +108.4% | 6d | SMA-OK | RS-OK | -1.87% |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE)<br><sub>✓ SAFE . ↗49Cr · 28Cr . ↓CMF3d</sub> | 1176.30 | -6.2% | +57.1% | 6d | SMA-OK | RS-OK | -0.31% |
| [MAHABANK](https://in.tradingview.com/chart/?symbol=NSE:MAHABANK)<br><sub>✓ SAFE . ↗172Cr · 108Cr . ↑CMF14d</sub> | 92.00 | -2.0% | +63.6% | 8d | SMA-OK | RS-OK | +0.33% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>✓ SAFE . →126Cr · 56Cr . ↑CMF7d</sub> | 408.50 | -3.8% | +39.8% | 8d | SMA-OK | RS-OK | +0.12% |
| [ALICON](https://in.tradingview.com/chart/?symbol=NSE:ALICON)<br><sub>✓ SAFE . ↗36Cr · 27Cr . ↑CMF30d</sub> | 966.05 | -1.0% | +64.8% | 8d | SMA-OK | RS-OK | -1.03% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>✓ SAFE . ↘105Cr · 170Cr . ↓CMF0d</sub> | 390.25 | 0.0% | +61.8% | 9d | SMA-OK | RS-OK | +2.28% |
| [HONASA](https://in.tradingview.com/chart/?symbol=NSE:HONASA)<br><sub>✓ SAFE . ↗100Cr · 69Cr . ↑CMF3d</sub> | 501.25 | -0.3% | +95.6% | 9d | SMA-OK | RS-OK | -0.14% |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>⚠ CAUTION . ↗63Cr · 64Cr . ↑CMF8d</sub> | 4824.10 | -0.0% | +62.4% | 9d | SMA-OK | RS-OK | +2.38% |
| [MANAKCOAT](https://in.tradingview.com/chart/?symbol=NSE:MANAKCOAT)<br><sub>✓ SAFE . ↗40Cr · 45Cr . ↑CMF15d</sub> | 170.95 | -3.2% | +76.7% | 9d | SMA-OK | RS-OK | -0.47% |
| [RPEL](https://in.tradingview.com/chart/?symbol=NSE:RPEL)<br><sub>✓ SAFE . ↗27Cr · 29Cr . ↑CMF21d . DEL72%(T-1)</sub> | 1977.20 | 0.0% | +249.1% | 9d | SMA-OK | RS-OK | +1.59% |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH)<br><sub>✓ SAFE . →43Cr · 27Cr . ↑CMF8d</sub> | 1872.00 | -5.5% | +165.0% | 9d | SMA-OK | RS-OK | -3.40% |
| [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM)<br><sub>✓ SAFE . →622Cr · 886Cr . ↑CMF30d</sub> | 1890.80 | -2.5% | +97.2% | 10d | SMA-OK | RS-OK | -2.53% |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . ↗1176Cr · 566Cr . ↑CMF14d</sub> | 3729.60 | 0.0% | +92.9% | 10d | SMA-OK | RS-OK | +0.26% |
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO)<br><sub>✓ SAFE . →621Cr · 495Cr . ↑CMF1d</sub> | 470.60 | -1.1% | +158.3% | 10d | SMA-OK | RS-OK | -1.05% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>✓ SAFE . →301Cr · 263Cr . ↑CMF17d</sub> | 4453.00 | -2.3% | +35.6% | 10d | SMA-OK | RS-OK | -0.93% |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS)<br><sub>✓ SAFE . ↗57Cr · 79Cr . ↑CMF15d</sub> | 368.10 | -6.8% | +212.1% | 10d | SMA-OK | RS-OK | -2.66% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>✓ SAFE . ↗72Cr · 43Cr . ↑CMF10d</sub> | 2000.70 | -1.4% | +53.0% | 10d | SMA-OK | RS-OK | +0.39% |
| [TECHM](https://in.tradingview.com/chart/?symbol=NSE:TECHM)<br><sub>✓ SAFE . ↘341Cr · 273Cr . ↑CMF21d</sub> | 1776.40 | -3.2% | +33.8% | 11d | SMA-OK | RS-OK | +0.70% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>✓ SAFE . ↗309Cr · 213Cr . ↑CMF14d</sub> | 1823.20 | -1.7% | +62.5% | 11d | SMA-OK | RS-OK | +0.89% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>✓ SAFE . ↗194Cr · 135Cr . ↑CMF9d</sub> | 187.00 | -1.5% | +38.1% | 11d | SMA-OK | RS-OK | -0.53% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↗125Cr · 98Cr . ↑CMF4d</sub> | 4763.60 | 0.0% | +207.9% | 11d | SMA-OK | RS-OK | +1.17% |
| [GLENMARK](https://in.tradingview.com/chart/?symbol=NSE:GLENMARK)<br><sub>✓ SAFE . ↗312Cr · 93Cr . ↑CMF10d</sub> | 2632.90 | -1.7% | +43.0% | 11d | SMA-OK | RS-OK | -0.27% |
| [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN)<br><sub>✓ SAFE . ↗53Cr · 51Cr . ↓CMF10d</sub> | 662.40 | -0.6% | +56.4% | 11d | SMA-OK | RS-OK | -0.57% |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA)<br><sub>✓ SAFE . ↗63Cr · 39Cr . ↑CMF30d</sub> | 1860.40 | -6.0% | +67.5% | 11d | SMA-OK | RS-OK | +0.68% |
| [AARTIDRUGS](https://in.tradingview.com/chart/?symbol=NSE:AARTIDRUGS)<br><sub>✓ SAFE . ↗169Cr · 27Cr . ↑CMF13d</sub> | 501.25 | -1.5% | +56.8% | 11d | SMA-OK | RS-OK | -1.20% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . ↗580Cr · 229Cr . ↑CMF11d</sub> | 1800.20 | -6.7% | +126.4% | 12d | SMA-OK | RS-OK | -6.67% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . →247Cr · 226Cr . ↑CMF14d</sub> | 9890.00 | -1.1% | +77.8% | 12d | SMA-OK | RS-OK | -1.12% |
| [KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL)<br><sub>⚠ CAUTION . ↘34Cr · 69Cr . ↑CMF17d</sub> | 1211.00 | -0.6% | +49.3% | 12d | SMA-OK | RS-OK | +4.54% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . →259Cr · 39Cr . ↑CMF10d</sub> | 246.13 | -7.0% | +127.2% | 12d | SMA-OK | RS-OK | -1.60% |
| [SGFIN](https://in.tradingview.com/chart/?symbol=NSE:SGFIN)<br><sub>✓ SAFE . →27Cr · 132Cr . ↑CMF30d</sub> | 740.25 | 0.0% | +122.8% | 13d | SMA-OK | RS-OK | +6.01% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . ↘113Cr · 107Cr . ↑CMF27d</sub> | 969.60 | -8.6% | +221.6% | 13d | SMA-OK | RS-OK | -5.14% |
| [PHOENIXLTD](https://in.tradingview.com/chart/?symbol=NSE:PHOENIXLTD)<br><sub>⚠ CAUTION . →91Cr · 103Cr . ↑CMF7d</sub> | 2202.00 | -3.9% | +49.0% | 13d | SMA-OK | RS-OK | -2.35% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>✓ SAFE . ↘117Cr · 261Cr . ↑CMF13d</sub> | 244.93 | -0.6% | +83.8% | 14d | SMA-OK | RS-OK | +0.16% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>✓ SAFE . ↗210Cr · 150Cr . ↑CMF13d</sub> | 48795.00 | -7.0% | +69.8% | 14d | SMA-OK | RS-OK | -1.20% |
| [ALIVUS](https://in.tradingview.com/chart/?symbol=NSE:ALIVUS)<br><sub>✓ SAFE . ↗95Cr · 59Cr . ↓CMF4d</sub> | 1448.60 | -7.1% | +68.4% | 14d | SMA-OK | RS-OK | -0.82% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . ↗1095Cr · 1001Cr . ↑CMF14d</sub> | 11080.00 | -4.2% | +90.3% | 15d | SMA-OK | RS-OK | -3.16% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↘177Cr · 172Cr . ↑CMF15d</sub> | 899.00 | -2.9% | +102.3% | 15d | SMA-OK | RS-OK | -2.18% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↗194Cr · 142Cr . ↑CMF30d</sub> | 3385.90 | 0.0% | +112.0% | 15d | SMA-OK | RS-OK | +1.55% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . ↗241Cr · 120Cr . ↑CMF24d</sub> | 360.85 | -1.2% | +53.7% | 15d | SMA-OK | RS-OK | -1.19% |
| [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA)<br><sub>✓ SAFE . ↗268Cr · 102Cr . ↑CMF28d</sub> | 670.00 | 0.0% | +115.4% | 15d | SMA-OK | RS-OK | +2.53% |
| [AARTIPHARM](https://in.tradingview.com/chart/?symbol=NSE:AARTIPHARM)<br><sub>✓ SAFE . ↘59Cr · 84Cr . ↑CMF10d</sub> | 986.75 | -2.4% | +66.7% | 15d | SMA-OK | RS-OK | -1.12% |
| [ETERNAL](https://in.tradingview.com/chart/?symbol=NSE:ETERNAL)<br><sub>✓ SAFE . ↘756Cr · 878Cr . ↑CMF12d</sub> | 371.10 | 0.0% | +72.1% | 16d | SMA-OK | RS-OK | +2.05% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . ↘510Cr · 857Cr . ↑CMF15d</sub> | 1939.60 | -0.3% | +222.5% | 16d | SMA-OK | RS-OK | -0.28% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>✓ SAFE . →491Cr · 256Cr . ↑CMF30d</sub> | 1893.00 | -2.9% | +45.2% | 16d | SMA-OK | RS-OK | -0.54% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>✓ SAFE . ↘177Cr · 152Cr . ↑CMF15d</sub> | 3947.30 | -2.3% | +146.3% | 16d | SMA-OK | RS-OK | -2.27% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>✓ SAFE . ↘48Cr · 138Cr . ↑CMF15d</sub> | 983.40 | 0.0% | +207.9% | 17d | SMA-OK | RS-OK | +4.46% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>✓ SAFE . ↘48Cr · 45Cr . ↑CMF30d</sub> | 7647.50 | -3.2% | +182.8% | 17d | SMA-OK | RS-OK | +1.66% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>✓ SAFE . ↘436Cr · 196Cr . ↑CMF17d</sub> | 886.00 | -0.6% | +55.2% | 18d | SMA-OK | RS-OK | -0.48% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>✓ SAFE . ↘323Cr · 306Cr . ↑CMF14d</sub> | 2010.00 | -4.2% | +87.2% | 22d | SMA-OK | RS-OK | -0.89% |
| [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS)<br><sub>✓ SAFE . ↘44Cr · 50Cr . ↑CMF0d</sub> | 283.20 | -7.6% | +78.9% | 25d | SMA-OK | RS-OK | -7.42% |
| [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC)<br><sub>✓ SAFE . ↘37Cr · 48Cr . ↑CMF25d</sub> | 807.15 | -1.1% | +64.7% | 26d | SMA-OK | RS-OK | -1.14% |
| [SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK)<br><sub>✓ SAFE . ↘83Cr · 51Cr . ↑CMF30d</sub> | 61.85 | -0.0% | +84.1% | 27d | SMA-OK | RS-OK | -0.02% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . →138Cr · 81Cr . ↑CMF2d</sub> | 1639.40 | -0.8% | +78.5% | 34d | SMA-OK | RS-OK | -0.11% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . →512Cr · 599Cr . ↑CMF2d</sub> | 361.90 | -6.0% | +476.7% | 35d | SMA-OK | RS-OK | -4.21% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>✓ SAFE . →33Cr · 67Cr . ↑CMF12d</sub> | 784.25 | 0.0% | +104.2% | 36d | SMA-OK | RS-OK | +3.50% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>✓ SAFE . ↘33Cr · 72Cr . ↑CMF0d</sub> | 763.65 | 0.0% | +710.9% | 40d | SMA-OK | RS-OK | +5.00% |
| [GCSL](https://in.tradingview.com/chart/?symbol=NSE:GCSL)<br><sub>✓ SAFE . →26Cr · 44Cr . ↑CMF30d</sub> | 823.50 | 0.0% | +192.4% | 48d | SMA-OK | RS-OK | +0.07% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↗253Cr · 230Cr . ↑CMF30d</sub> | 129.55 | -11.9% | +284.6% | 48d | SMA-OK | RS-OK | -5.13% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . →86Cr · 94Cr . ↓CMF13d</sub> | 70.37 | 0.0% | +174.7% | 56d | SMA-OK | RS-OK | +0.10% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . ↘65Cr · 49Cr . ↑CMF30d</sub> | 914.90 | 0.0% | +208.5% | 56d | SMA-OK | RS-OK | +0.45% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↘59Cr · 85Cr . ↑CMF2d</sub> | 1185.80 | -8.8% | +268.4% | 66d | SMA-OK | RS-OK | +3.20% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>✓ SAFE . →31Cr · 29Cr . ↓CMF7d</sub> | 161.69 | -6.3% | +96.5% | 66d | SMA-OK | RS-OK | -1.69% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . ↘94Cr · 61Cr . ↑CMF11d</sub> | 362.30 | -4.8% | +175.9% | 83d | SMA-OK | RS-OK | -0.56% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . →211Cr · 130Cr . ↑CMF14d</sub> | 165.81 | -1.5% | +200.2% | 86d | SMA-OK | RS-OK | +1.13% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . ↘47Cr · 59Cr . ↑CMF16d</sub> | 430.40 | 0.0% | +97.7% | 93d | SMA-OK | RS-OK | +1.18% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . →657Cr · 1519Cr . ↑CMF15d</sub> | 2220.00 | -9.5% | +138.7% | 133d | SMA-OK | RS-OK | -8.42% |

### By Trend Age

**<2 WEEKS** (65)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABCAPITAL,NSE:ACE,NSE:ALICON,NSE:APLLTD,NSE:APOLLO,NSE:ASAHIINDIA,NSE:ASTRAMICRO,NSE:BALUFORGE,NSE:BHEL,NSE:BOROLTD,NSE:CENTUM,NSE:DIACABS,NSE:DLF,NSE:ENGINERSIN,NSE:FEDERALBNK,NSE:FILATEX,NSE:FLUOROCHEM,NSE:GABRIEL,NSE:GESHIP,NSE:GRAPHITE,NSE:GREAVESCOT,NSE:HINDOILEXP,NSE:HONASA,NSE:INDIGO,NSE:ITDC,NSE:JAMNAAUTO,NSE:JYOTICNC,NSE:KALYANKJIL,NSE:KARURVYSYA,NSE:KOTAKBANK,NSE:KTKBANK,NSE:LALPATHLAB,NSE:LODHA,NSE:LOTUSDEV,NSE:LTTS,NSE:MAHABANK,NSE:MANAKCOAT,NSE:MANKIND,NSE:MCX,NSE:MOTHERSON,NSE:MOTILALOFS,NSE:MSTCLTD,NSE:NEULANDLAB,NSE:PARAGMILK,NSE:PAYTM,NSE:PETRONET,NSE:PNBHOUSING,NSE:POONAWALLA,NSE:QPOWER,NSE:RADICO,NSE:RKFORGE,NSE:ROLEXRINGS,NSE:ROSSTECH,NSE:RPEL,NSE:STYLEBAAZA,NSE:TANLA,NSE:TIIL,NSE:TITAN,NSE:TVSMOTOR,NSE:TVSSRICHAK,NSE:UFLEX,NSE:UNIMECH,NSE:URBANCO,NSE:VIJAYA,NSE:VRLLOG
```

**2-4 WEEKS** (32)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AARTIDRUGS,NSE:AARTIPHARM,NSE:ACUTAAS,NSE:ADANIPORTS,NSE:ALIVUS,NSE:ATHERENERG,NSE:AUROPHARMA,NSE:BOSCHLTD,NSE:DIVISLAB,NSE:ETERNAL,NSE:GAIL,NSE:GLAND,NSE:GLENMARK,NSE:GRWRHITECH,NSE:HFCL,NSE:INDGN,NSE:INDHOTEL,NSE:KPRMILL,NSE:NAVINFLUOR,NSE:NUVAMA,NSE:NYKAA,NSE:PHOENIXLTD,NSE:PPLPHARMA,NSE:SAILIFE,NSE:SANSERA,NSE:SAREGAMA,NSE:SGFIN,NSE:SGMART,NSE:SKYGOLD,NSE:SONACOMS,NSE:TECHM,NSE:WELSPUNLIV
```

**1-2 MONTHS** (9)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:COFORGE,NSE:CUPID,NSE:KROSS,NSE:PVRINOX,NSE:SIGMAADV,NSE:SOUTHBANK,NSE:STLTECH,NSE:TIPSMUSIC
```

**2-3 MONTHS** (4)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GCSL,NSE:MOREPENLAB,NSE:SBC,NSE:SHREEJISPG
```

**3-6 MONTHS** (5)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:NAZARA,NSE:RATNAVEER,NSE:RAYMOND,NSE:SAMBHV,NSE:TFCILTD
```

**6+ MONTHS** (1)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LAURUSLABS
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
