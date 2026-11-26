> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-11-26
*Generated 2026-11-26 15:51 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO) | [ARFIN](https://in.tradingview.com/chart/?symbol=NSE:ARFIN) |
| [AVADHSUGAR](https://in.tradingview.com/chart/?symbol=NSE:AVADHSUGAR) | [CEMPRO](https://in.tradingview.com/chart/?symbol=NSE:CEMPRO) |
| [BALUFORGE](https://in.tradingview.com/chart/?symbol=NSE:BALUFORGE) | [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE) |
| [CCAVENUE](https://in.tradingview.com/chart/?symbol=NSE:CCAVENUE) | [EMCURE](https://in.tradingview.com/chart/?symbol=NSE:EMCURE) |
| [DALMIASUG](https://in.tradingview.com/chart/?symbol=NSE:DALMIASUG) | [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO) |
| [DHAMPURSUG](https://in.tradingview.com/chart/?symbol=NSE:DHAMPURSUG) | [GRANULES](https://in.tradingview.com/chart/?symbol=NSE:GRANULES) |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN) | [IIFL](https://in.tradingview.com/chart/?symbol=NSE:IIFL) |
| [GCSL](https://in.tradingview.com/chart/?symbol=NSE:GCSL) | [KDDL](https://in.tradingview.com/chart/?symbol=NSE:KDDL) |
| [GLAXO](https://in.tradingview.com/chart/?symbol=NSE:GLAXO) | [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH) |
| [ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL) | [MAXESTATES](https://in.tradingview.com/chart/?symbol=NSE:MAXESTATES) |
| [IIFLCAPS](https://in.tradingview.com/chart/?symbol=NSE:IIFLCAPS) | [MEDANTA](https://in.tradingview.com/chart/?symbol=NSE:MEDANTA) |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA) | [PDSL](https://in.tradingview.com/chart/?symbol=NSE:PDSL) |
| [KAJARIACER](https://in.tradingview.com/chart/?symbol=NSE:KAJARIACER) | [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK) |
| [MANAKCOAT](https://in.tradingview.com/chart/?symbol=NSE:MANAKCOAT) | [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS) |
| [METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS) | [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV) |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB) | [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL) |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA) | [TI](https://in.tradingview.com/chart/?symbol=NSE:TI) |
| [PROTEAN](https://in.tradingview.com/chart/?symbol=NSE:PROTEAN) | [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC) |
| [RAYMONDREL](https://in.tradingview.com/chart/?symbol=NSE:RAYMONDREL) | [YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH) |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY) |  |
| [UTTAMSUGAR](https://in.tradingview.com/chart/?symbol=NSE:UTTAMSUGAR) |  |

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

**Qualifying: 114**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AETHER,NSE:AVADHSUGAR,NSE:BAJAJHLDNG,NSE:BEML,NSE:COHANCE,NSE:CPPLUS,NSE:CRAFTSMAN,NSE:DALMIASUG,NSE:DHAMPURSUG,NSE:ENGINERSIN,NSE:FEDERALBNK,NSE:FILATEX,NSE:GABRIEL,NSE:GESHIP,NSE:GLAXO,NSE:GRAPHITE,NSE:GREAVESCOT,NSE:IGIL,NSE:IIFLCAPS,NSE:INDIGO,NSE:INOXINDIA,NSE:JSWINFRA,NSE:KAJARIACER,NSE:KOPRAN,NSE:LGEINDIA,NSE:LODHA,NSE:LTTS,NSE:MANKIND,NSE:METROPOLIS,NSE:MOTHERSON,NSE:NEULANDLAB,NSE:NUVAMA,NSE:PARAGMILK,NSE:PETRONET,NSE:PNBHOUSING,NSE:POONAWALLA,NSE:PROTEAN,NSE:PTCIL,NSE:RAYMONDREL,NSE:SHAILY,NSE:TECHM,NSE:UNOMINDA,NSE:VIJAYA,NSE:WOCKPHARMA,NSE:ZYDUSLIFE,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABCAPITAL,NSE:ACE,NSE:ADANIPORTS,NSE:ANTHEM,NSE:APLLTD,NSE:APOLLO,NSE:AUROPHARMA,NSE:BALUFORGE,NSE:BOSCHLTD,NSE:DCBBANK,NSE:DIVISLAB,NSE:DLF,NSE:ETERNAL,NSE:FLUOROCHEM,NSE:GAIL,NSE:GLENMARK,NSE:HFCL,NSE:HONASA,NSE:ICIL,NSE:INDGN,NSE:JYOTICNC,NSE:KALYANKJIL,NSE:KARURVYSYA,NSE:KPRMILL,NSE:KTKBANK,NSE:LALPATHLAB,NSE:MAHABANK,NSE:MANAKCOAT,NSE:MCX,NSE:MOTILALOFS,NSE:NAVINFLUOR,NSE:NYKAA,NSE:PHOENIXLTD,NSE:RADICO,NSE:RKFORGE,NSE:RUBICON,NSE:SAILIFE,NSE:SANSERA,NSE:STYLEBAAZA,NSE:TANLA,NSE:TVSMOTOR,NSE:URBANCO,NSE:WELSPUNLIV,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AARTIPHARM,NSE:ACUTAAS,NSE:ARIS,NSE:ATHERENERG,NSE:CCAVENUE,NSE:GLAND,NSE:GRWRHITECH,NSE:INDHOTEL,NSE:PPLPHARMA,NSE:PVRINOX,NSE:SAREGAMA,NSE:SONACOMS,NSE:SOUTHBANK,NSE:STLTECH,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABDL,NSE:CUPID,NSE:GCSL,NSE:MOREPENLAB,NSE:UTTAMSUGAR,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:RATNAVEER,NSE:RAYMOND,NSE:SBC,NSE:SHREEJISPG,NSE:TFCILTD,NSE:THELEELA,###6+ MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:LAURUSLABS
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [LGEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LGEINDIA)<br><sub>✓ SAFE . ↗141Cr · 301Cr . ↓CMF8d</sub> | 1775.00 | -1.0% | +34.6% | 0d | SMA-OK | RS-OK | +1.97% |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY)<br><sub>✓ SAFE . ↗99Cr · 780Cr . ↑CMF0d</sub> | 3379.60 | -2.3% | +85.5% | 0d | SMA-OK | RS-OK | +16.33% |
| [DHAMPURSUG](https://in.tradingview.com/chart/?symbol=NSE:DHAMPURSUG)<br><sub>✓ SAFE . ↗82Cr · 735Cr . ↑CMF0d</sub> | 180.01 | -13.3% | +62.9% | 0d | SMA-OK | RS-OK | +13.21% |
| [TECHM](https://in.tradingview.com/chart/?symbol=NSE:TECHM)<br><sub>✓ SAFE . →377Cr · 565Cr . ↓CMF3d</sub> | 1777.50 | -3.1% | +33.9% | 0d | SMA-OK | RS-OK | +1.79% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>✓ SAFE . ↘138Cr · 83Cr . ↑CMF17d</sub> | 1199.50 | -3.7% | +39.4% | 0d | SMA-OK | RS-OK | -0.04% |
| [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA)<br><sub>⚠ CAUTION . ↗77Cr · 109Cr . ↑CMF16d</sub> | 365.65 | -0.5% | +56.1% | 0d | SMA-OK | RS-OK | +2.24% |
| [METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS)<br><sub>⚠ CAUTION . →16Cr · 64Cr . ↓CMF0d</sub> | 580.30 | -3.6% | +37.6% | 0d | SMA-OK | RS-OK | +2.38% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>⚠ CAUTION . ↗44Cr · 60Cr . ↑CMF3d</sub> | 24875.00 | -3.3% | +68.9% | 0d | SMA-OK | RS-OK | +2.03% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>✓ SAFE . ↘38Cr · 60Cr . ↑CMF6d</sub> | 1700.80 | -5.5% | +108.5% | 0d | SMA-OK | RS-OK | +1.45% |
| [IIFLCAPS](https://in.tradingview.com/chart/?symbol=NSE:IIFLCAPS)<br><sub>✓ SAFE . ↗139Cr · 60Cr . ↓CMF9d</sub> | 346.15 | -12.5% | +41.8% | 0d | SMA-OK | RS-OK | +3.53% |
| [NEULANDLAB](https://in.tradingview.com/chart/?symbol=NSE:NEULANDLAB)<br><sub>✓ SAFE . ↘86Cr · 59Cr . ↑CMF16d</sub> | 21119.00 | -12.0% | +82.8% | 0d | SMA-OK | RS-OK | +0.72% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . ↘61Cr · 56Cr . ↓CMF14d</sub> | 4235.00 | -4.6% | +208.9% | 0d | SMA-OK | RS-OK | +0.72% |
| [KAJARIACER](https://in.tradingview.com/chart/?symbol=NSE:KAJARIACER)<br><sub>✓ SAFE . ↘33Cr · 41Cr . ↓CMF30d</sub> | 1223.40 | -3.0% | +38.4% | 0d | SMA-OK | RS-OK | +1.44% |
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP)<br><sub>✓ SAFE . ↘80Cr · 40Cr . ↓CMF5d</sub> | 1531.20 | -11.0% | +42.9% | 0d | SMA-OK | RS-OK | -1.09% |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE)<br><sub>✓ SAFE . ↘40Cr · 39Cr . ↑CMF16d</sub> | 791.75 | -7.0% | +50.5% | 0d | SMA-OK | RS-OK | -0.34% |
| [DALMIASUG](https://in.tradingview.com/chart/?symbol=NSE:DALMIASUG)<br><sub>✓ SAFE . ↘8Cr · 37Cr . ↑CMF30d</sub> | 451.15 | -11.2% | +70.6% | 0d | SMA-OK | RS-OK | +2.13% |
| [KOPRAN](https://in.tradingview.com/chart/?symbol=NSE:KOPRAN)<br><sub>✓ SAFE . ↗47Cr · 32Cr . ↑CMF10d</sub> | 281.16 | -3.3% | +160.2% | 0d | SMA-OK | RS-OK | -2.89% |
| [AVADHSUGAR](https://in.tradingview.com/chart/?symbol=NSE:AVADHSUGAR)<br><sub>✓ SAFE . ↘7Cr · 27Cr . ↑CMF0d</sub> | 869.95 | -12.8% | +179.5% | 0d | SMA-OK | RS-OK | +5.92% |
| [BAJAJHLDNG](https://in.tradingview.com/chart/?symbol=NSE:BAJAJHLDNG)<br><sub>⚠ CAUTION . ↘32Cr · 32Cr . ↑CMF1d</sub> | 11541.00 | -2.8% | +32.0% | 1d | SMA-OK | RS-OK | -1.10% |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN)<br><sub>✓ SAFE . ↘62Cr · 31Cr . ↑CMF18d</sub> | 291.15 | -7.8% | +76.9% | 1d | SMA-OK | RS-OK | +0.94% |
| [GLAXO](https://in.tradingview.com/chart/?symbol=NSE:GLAXO)<br><sub>⚠ CAUTION . ↘22Cr · 28Cr . ↑CMF12d</sub> | 2779.80 | -10.5% | +32.2% | 1d | SMA-OK | RS-OK | +2.42% |
| [RAYMONDREL](https://in.tradingview.com/chart/?symbol=NSE:RAYMONDREL)<br><sub>✓ SAFE . ↗32Cr · 23Cr . ↑CMF5d</sub> | 619.05 | -14.3% | +73.2% | 1d | SMA-OK | RS-OK | +2.03% |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA)<br><sub>✓ SAFE . ↘39Cr · 54Cr . ↓CMF6d</sub> | 1854.80 | -6.3% | +67.0% | 2d | SMA-OK | RS-OK | +3.31% |
| [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON)<br><sub>✓ SAFE . →278Cr · 171Cr . ↑CMF15d</sub> | 165.76 | -2.9% | +57.7% | 3d | SMA-OK | RS-OK | -0.46% |
| [WOCKPHARMA](https://in.tradingview.com/chart/?symbol=NSE:WOCKPHARMA)<br><sub>✓ SAFE . ↗190Cr · 394Cr . ↑CMF15d</sub> | 2233.70 | -4.1% | +103.0% | 4d | SMA-OK | RS-OK | +7.49% |
| [COHANCE](https://in.tradingview.com/chart/?symbol=NSE:COHANCE)<br><sub>✓ SAFE . ↗92Cr · 102Cr . ↓CMF1d</sub> | 502.60 | -10.9% | +79.6% | 4d | SMA-OK | RS-OK | +2.67% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>✓ SAFE . ↘59Cr · 42Cr . ↓CMF20d</sub> | 1171.00 | -4.4% | +56.0% | 4d | SMA-OK | RS-OK | -1.04% |
| [VIJAYA](https://in.tradingview.com/chart/?symbol=NSE:VIJAYA)<br><sub>✓ SAFE . ↗58Cr · 27Cr . ↑CMF24d</sub> | 1587.10 | -2.5% | +84.2% | 4d | SMA-OK | RS-OK | -2.49% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>✓ SAFE . ↗129Cr · 25Cr . ↑CMF6d</sub> | 2162.80 | -5.8% | +101.5% | 4d | SMA-OK | RS-OK | +1.19% |
| [PROTEAN](https://in.tradingview.com/chart/?symbol=NSE:PROTEAN)<br><sub>✓ SAFE . ↘24Cr · 23Cr . ↓CMF0d</sub> | 693.25 | -15.2% | +55.3% | 5d | SMA-OK | RS-OK | +1.71% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>✓ SAFE . ↘136Cr · 47Cr . ↑CMF11d</sub> | 2615.10 | -2.0% | +35.7% | 6d | SMA-OK | RS-OK | -1.87% |
| [INDIGO](https://in.tradingview.com/chart/?symbol=NSE:INDIGO)<br><sub>✓ SAFE . →499Cr · 262Cr . ↑CMF11d</sub> | 5523.00 | -6.7% | +40.1% | 8d | SMA-OK | RS-OK | -1.16% |
| [UNOMINDA](https://in.tradingview.com/chart/?symbol=NSE:UNOMINDA)<br><sub>✓ SAFE . ↘140Cr · 103Cr . ↑CMF20d</sub> | 1390.00 | 0.0% | +37.2% | 8d | SMA-OK | RS-OK | +1.09% |
| [IGIL](https://in.tradingview.com/chart/?symbol=NSE:IGIL)<br><sub>✓ SAFE . ↘32Cr · 33Cr . ↓CMF4d</sub> | 423.20 | -6.1% | +45.4% | 8d | SMA-OK | RS-OK | -2.15% |
| [GREAVESCOT](https://in.tradingview.com/chart/?symbol=NSE:GREAVESCOT)<br><sub>✓ SAFE . ↗502Cr · 1082Cr . ↑CMF18d</sub> | 325.79 | 0.0% | +170.1% | 9d | SMA-OK | RS-OK | +5.28% |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>✓ SAFE . ↘141Cr · 128Cr . ↑CMF13d</sub> | 1219.00 | -7.4% | +80.1% | 9d | SMA-OK | RS-OK | +0.02% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>⚠ CAUTION . →232Cr · 299Cr . ↑CMF28d</sub> | 356.85 | -4.5% | +44.6% | 9d | SMA-OK | RS-OK | +0.18% |
| [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN)<br><sub>⚠ CAUTION . →45Cr · 93Cr . ↑CMF30d</sub> | 11860.00 | -0.6% | +81.2% | 9d | SMA-OK | RS-OK | +0.77% |
| [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX)<br><sub>✓ SAFE . ↗47Cr · 50Cr . ↓CMF7d</sub> | 110.05 | -1.7% | +198.2% | 9d | SMA-OK | RS-OK | -1.64% |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML)<br><sub>✓ SAFE . ↘32Cr · 33Cr . ↓CMF2d</sub> | 2040.20 | -4.4% | +49.0% | 9d | SMA-OK | RS-OK | -0.05% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>✓ SAFE . ↘69Cr · 31Cr . ↑CMF10d</sub> | 1537.30 | -6.3% | +86.8% | 9d | SMA-OK | RS-OK | +2.36% |
| [POONAWALLA](https://in.tradingview.com/chart/?symbol=NSE:POONAWALLA)<br><sub>✓ SAFE . ↘99Cr · 75Cr . ↑CMF19d</sub> | 508.60 | -1.9% | +38.1% | 10d | SMA-OK | RS-OK | -0.94% |
| [PETRONET](https://in.tradingview.com/chart/?symbol=NSE:PETRONET)<br><sub>✓ SAFE . ↘90Cr · 73Cr . ↑CMF23d</sub> | 326.45 | -2.6% | +37.1% | 10d | SMA-OK | RS-OK | -0.17% |
| [PARAGMILK](https://in.tradingview.com/chart/?symbol=NSE:PARAGMILK)<br><sub>✓ SAFE . ↘48Cr · 57Cr . ↑CMF16d</sub> | 315.44 | -8.3% | +75.4% | 10d | SMA-OK | RS-OK | -6.78% |
| [LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS)<br><sub>✓ SAFE . ↘39Cr · 48Cr . ↓CMF0d</sub> | 4245.20 | -9.6% | +39.3% | 10d | SMA-OK | RS-OK | +1.61% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>✓ SAFE . →238Cr · 250Cr . ↑CMF14d</sub> | 794.10 | 0.0% | +57.5% | 11d | SMA-OK | RS-OK | +1.16% |
| [TANLA](https://in.tradingview.com/chart/?symbol=NSE:TANLA)<br><sub>✓ SAFE . ↘38Cr · 55Cr . ↑CMF11d</sub> | 624.70 | -14.8% | +65.5% | 11d | SMA-OK | RS-OK | -3.82% |
| [BALUFORGE](https://in.tradingview.com/chart/?symbol=NSE:BALUFORGE)<br><sub>✓ SAFE . →48Cr · 38Cr . ↑CMF15d</sub> | 528.90 | -19.1% | +48.4% | 11d | SMA-OK | RS-OK | +4.49% |
| [URBANCO](https://in.tradingview.com/chart/?symbol=NSE:URBANCO)<br><sub>✓ SAFE . ↗267Cr · 222Cr . ↑CMF11d . DEL68%(T-1)</sub> | 170.72 | -5.7% | +65.7% | 12d | SMA-OK | RS-OK | +3.56% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>✓ SAFE . ↘120Cr · 100Cr . ↑CMF12d</sub> | 415.80 | -2.1% | +42.3% | 13d | SMA-OK | RS-OK | -1.70% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>✓ SAFE . →68Cr · 40Cr . ↑CMF11d</sub> | 339.70 | -7.9% | +90.0% | 13d | SMA-OK | RS-OK | -0.03% |
| [DCBBANK](https://in.tradingview.com/chart/?symbol=NSE:DCBBANK)<br><sub>✓ SAFE . →29Cr · 40Cr . ↑CMF4d</sub> | 227.17 | -6.0% | +43.5% | 13d | SMA-OK | RS-OK | -5.99% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>✓ SAFE . ↘900Cr · 524Cr . ↑CMF14d</sub> | 639.80 | -10.0% | +93.4% | 14d | SMA-OK | RS-OK | +0.54% |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE)<br><sub>✓ SAFE . ↗82Cr · 424Cr . ↑CMF0d</sub> | 1295.00 | 0.0% | +72.9% | 14d | SMA-OK | RS-OK | +8.79% |
| [RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO)<br><sub>✓ SAFE . ↘139Cr · 144Cr . ↑CMF20d</sub> | 4671.00 | -1.3% | +83.8% | 14d | SMA-OK | RS-OK | -0.60% |
| [MOTILALOFS](https://in.tradingview.com/chart/?symbol=NSE:MOTILALOFS)<br><sub>✓ SAFE . ↘158Cr · 123Cr . ↑CMF15d</sub> | 1215.25 | -2.0% | +93.4% | 14d | SMA-OK | RS-OK | -1.21% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>✓ SAFE . ↘57Cr · 116Cr . ↑CMF21d</sub> | 787.85 | -0.5% | +70.3% | 14d | SMA-OK | RS-OK | +5.65% |
| [STYLEBAAZA](https://in.tradingview.com/chart/?symbol=NSE:STYLEBAAZA)<br><sub>✓ SAFE . ↗164Cr · 52Cr . ↑CMF13d</sub> | 514.80 | -4.6% | +117.1% | 14d | SMA-OK | RS-OK | -0.14% |
| [JYOTICNC](https://in.tradingview.com/chart/?symbol=NSE:JYOTICNC)<br><sub>✓ SAFE . ↘36Cr · 48Cr . ↑CMF16d</sub> | 1050.35 | -5.7% | +79.4% | 14d | SMA-OK | RS-OK | +3.06% |
| [APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD)<br><sub>✓ SAFE . ↘29Cr · 38Cr . ↓CMF0d</sub> | 1018.80 | -3.6% | +57.6% | 14d | SMA-OK | RS-OK | -1.13% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>✓ SAFE . →432Cr · 304Cr . ↑CMF22d</sub> | 4528.20 | -1.6% | +37.9% | 15d | SMA-OK | RS-OK | -1.35% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>✓ SAFE . →175Cr · 75Cr . ↑CMF14d</sub> | 185.60 | -3.4% | +37.1% | 16d | SMA-OK | RS-OK | -3.05% |
| [MAHABANK](https://in.tradingview.com/chart/?symbol=NSE:MAHABANK)<br><sub>✓ SAFE . →201Cr · 155Cr . ↑CMF22d</sub> | 94.20 | -5.3% | +67.6% | 16d | SMA-OK | RS-OK | -4.57% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>✓ SAFE . ↗265Cr · 218Cr . ↑CMF20d</sub> | 1798.00 | -3.1% | +60.3% | 17d | SMA-OK | RS-OK | -0.06% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>✓ SAFE . ↗126Cr · 98Cr . ↑CMF6d</sub> | 370.00 | -6.0% | +53.5% | 17d | SMA-OK | RS-OK | -2.31% |
| [MANAKCOAT](https://in.tradingview.com/chart/?symbol=NSE:MANAKCOAT)<br><sub>✓ SAFE . →24Cr · 47Cr . ↓CMF4d</sub> | 160.46 | -9.1% | +65.9% | 17d | SMA-OK | RS-OK | +4.60% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>✓ SAFE . ↘32Cr · 40Cr . ↑CMF24d</sub> | 975.50 | 0.0% | +65.9% | 17d | SMA-OK | RS-OK | +0.75% |
| [HONASA](https://in.tradingview.com/chart/?symbol=NSE:HONASA)<br><sub>✓ SAFE . →98Cr · 35Cr . ↑CMF11d</sub> | 533.25 | -1.2% | +108.1% | 17d | SMA-OK | RS-OK | -0.60% |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>✓ SAFE . →53Cr · 25Cr . ↑CMF16d</sub> | 4781.20 | -4.0% | +61.0% | 17d | SMA-OK | RS-OK | +1.04% |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . ↘907Cr · 1861Cr . ↑CMF22d</sub> | 3835.00 | 0.0% | +94.4% | 18d | SMA-OK | RS-OK | +7.57% |
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO)<br><sub>✓ SAFE . →424Cr · 286Cr . ↑CMF2d</sub> | 428.80 | -9.8% | +135.4% | 18d | SMA-OK | RS-OK | +2.12% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>✓ SAFE . ↘44Cr · 34Cr . ↓CMF3d</sub> | 2037.90 | -0.1% | +55.9% | 18d | SMA-OK | RS-OK | +0.47% |
| [GLENMARK](https://in.tradingview.com/chart/?symbol=NSE:GLENMARK)<br><sub>✓ SAFE . ↘134Cr · 118Cr . ↑CMF18d</sub> | 2740.20 | 0.0% | +42.7% | 19d | SMA-OK | RS-OK | +0.78% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>✓ SAFE . ↘31Cr · 91Cr . ↑CMF24d</sub> | 1851.70 | -0.5% | +201.0% | 19d | SMA-OK | RS-OK | +8.19% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>✓ SAFE . ↘139Cr · 111Cr . ↑CMF18d</sub> | 48800.00 | -7.0% | +69.8% | 19d | SMA-OK | RS-OK | -1.13% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↘63Cr · 38Cr . ↑CMF12d</sub> | 4685.80 | -2.3% | +187.6% | 19d | SMA-OK | RS-OK | -0.48% |
| [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN)<br><sub>✓ SAFE . ↘36Cr · 37Cr . ↓CMF18d</sub> | 657.60 | -1.3% | +55.3% | 19d | SMA-OK | RS-OK | +0.62% |
| [ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL)<br><sub>✓ SAFE . ↘34Cr · 22Cr . ↑CMF20d</sub> | 590.05 | -0.5% | +162.8% | 19d | SMA-OK | RS-OK | +1.61% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . ↗1100Cr · 1390Cr . ↑CMF19d</sub> | 11203.00 | -3.1% | +92.5% | 20d | SMA-OK | RS-OK | +0.20% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . ↘221Cr · 317Cr . ↑CMF22d</sub> | 10270.00 | -0.1% | +84.6% | 20d | SMA-OK | RS-OK | +3.15% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↘201Cr · 231Cr . ↑CMF18d</sub> | 280.35 | 0.0% | +158.8% | 20d | SMA-OK | RS-OK | +1.37% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . ↘144Cr · 144Cr . ↑CMF29d</sub> | 357.00 | -2.2% | +52.1% | 20d | SMA-OK | RS-OK | -1.92% |
| [KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL)<br><sub>✓ SAFE . ↗67Cr · 66Cr . ↓CMF1d . DEL74%(T-1)</sub> | 1190.50 | -2.3% | +46.8% | 20d | SMA-OK | RS-OK | +1.49% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . ↘143Cr · 51Cr . ↑CMF19d</sub> | 1812.60 | -6.0% | +128.0% | 20d | SMA-OK | RS-OK | +0.74% |
| [ETERNAL](https://in.tradingview.com/chart/?symbol=NSE:ETERNAL)<br><sub>⚠ CAUTION . →730Cr · 535Cr . ↑CMF17d</sub> | 362.10 | -3.5% | +67.9% | 21d | SMA-OK | RS-OK | -0.52% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>✓ SAFE . ↘374Cr · 376Cr . ↑CMF30d</sub> | 1919.00 | -1.6% | +47.2% | 21d | SMA-OK | RS-OK | +0.10% |
| [PHOENIXLTD](https://in.tradingview.com/chart/?symbol=NSE:PHOENIXLTD)<br><sub>⚠ CAUTION . ↗137Cr · 174Cr . ↑CMF15d</sub> | 2291.00 | -0.0% | +55.1% | 21d | SMA-OK | RS-OK | +0.24% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>✓ SAFE . →146Cr · 164Cr . ↑CMF21d</sub> | 235.60 | -4.4% | +76.8% | 22d | SMA-OK | RS-OK | +1.32% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↘153Cr · 311Cr . ↑CMF23d</sub> | 881.50 | -4.8% | +98.3% | 23d | SMA-OK | RS-OK | -0.19% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>✓ SAFE . →400Cr · 326Cr . ↑CMF22d</sub> | 906.00 | -0.7% | +58.7% | 23d | SMA-OK | RS-OK | -0.66% |
| [ARIS](https://in.tradingview.com/chart/?symbol=NSE:ARIS)<br><sub>✓ SAFE . ↗82Cr · 85Cr . ↑CMF30d</sub> | 185.94 | -2.3% | +120.9% | 23d | SMA-OK | RS-OK | -2.29% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↘72Cr · 65Cr . ↑CMF30d</sub> | 3370.80 | -0.4% | +111.1% | 23d | SMA-OK | RS-OK | +0.67% |
| [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA)<br><sub>✓ SAFE . ↘44Cr · 43Cr . ↑CMF30d</sub> | 620.95 | -8.3% | +99.6% | 23d | SMA-OK | RS-OK | +0.06% |
| [AARTIPHARM](https://in.tradingview.com/chart/?symbol=NSE:AARTIPHARM)<br><sub>✓ SAFE . →55Cr · 30Cr . ↑CMF18d</sub> | 1022.15 | -0.3% | +72.7% | 23d | SMA-OK | RS-OK | -0.32% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . ↘382Cr · 285Cr . ↑CMF23d</sub> | 1906.00 | -3.7% | +217.0% | 24d | SMA-OK | RS-OK | +1.82% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>✓ SAFE . ↘150Cr · 222Cr . ↑CMF23d</sub> | 4079.90 | 0.0% | +154.6% | 24d | SMA-OK | RS-OK | +2.18% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>✓ SAFE . ↘33Cr · 44Cr . ↑CMF30d</sub> | 7447.50 | -6.5% | +175.4% | 25d | SMA-OK | RS-OK | -2.37% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [CCAVENUE](https://in.tradingview.com/chart/?symbol=NSE:CCAVENUE)<br><sub>✓ SAFE . →14Cr · 38Cr . ↓CMF3d</sub> | 115.03 | -16.8% | +774.8% | 29d | SMA-OK | RS-OK | +5.72% |
| [SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK)<br><sub>✓ SAFE . →82Cr · 44Cr . ↓CMF0d</sub> | 57.59 | -6.9% | +71.4% | 35d | SMA-OK | RS-OK | -2.01% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . ↘111Cr · 63Cr . ↑CMF1d</sub> | 1638.20 | -4.4% | +78.3% | 42d | SMA-OK | RS-OK | -4.16% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↘359Cr · 287Cr . ↑CMF10d</sub> | 371.10 | -3.6% | +463.6% | 43d | SMA-OK | RS-OK | +1.30% |
| [UTTAMSUGAR](https://in.tradingview.com/chart/?symbol=NSE:UTTAMSUGAR)<br><sub>✓ SAFE . ↗16Cr · 105Cr . ↑CMF3d</sub> | 381.80 | -1.8% | +103.8% | 44d | SMA-OK | RS-OK | +10.30% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>✓ SAFE . ↗67Cr · 68Cr . ↑CMF6d</sub> | 820.30 | 0.0% | +113.5% | 44d | SMA-OK | RS-OK | +1.62% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↗253Cr · 230Cr . ↑CMF30d</sub> | 129.55 | -11.9% | +284.6% | 48d | SMA-OK | RS-OK | -5.13% |
| [GCSL](https://in.tradingview.com/chart/?symbol=NSE:GCSL)<br><sub>✓ SAFE . ↗26Cr · 33Cr . ↑CMF30d</sub> | 850.55 | -0.2% | +202.0% | 56d | SMA-OK | RS-OK | -0.22% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . →74Cr · 70Cr . ↓CMF21d</sub> | 68.35 | -2.9% | +158.2% | 64d | SMA-OK | RS-OK | +0.12% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . ↘53Cr · 61Cr . ↑CMF30d</sub> | 910.65 | -0.5% | +197.3% | 64d | SMA-OK | RS-OK | +0.28% |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA)<br><sub>✓ SAFE . ↘26Cr · 23Cr . ↑CMF10d</sub> | 685.85 | -1.8% | +76.0% | 73d | SMA-OK | RS-OK | +0.78% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . →55Cr · 34Cr . ↑CMF10d</sub> | 1183.20 | -9.0% | +267.6% | 74d | SMA-OK | RS-OK | -0.56% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . ↘110Cr · 155Cr . ↑CMF3d</sub> | 405.00 | 0.0% | +208.5% | 91d | SMA-OK | RS-OK | +0.11% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . ↘105Cr · 154Cr . ↑CMF22d</sub> | 174.94 | 0.0% | +216.7% | 94d | SMA-OK | RS-OK | +0.74% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . →717Cr · 457Cr . ↑CMF20d</sub> | 2370.70 | -3.4% | +154.9% | 138d | SMA-OK | RS-OK | +3.32% |

### By Trend Age

**<2 WEEKS** (45)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AETHER,NSE:AVADHSUGAR,NSE:BAJAJHLDNG,NSE:BEML,NSE:COHANCE,NSE:CPPLUS,NSE:CRAFTSMAN,NSE:DALMIASUG,NSE:DHAMPURSUG,NSE:ENGINERSIN,NSE:FEDERALBNK,NSE:FILATEX,NSE:GABRIEL,NSE:GESHIP,NSE:GLAXO,NSE:GRAPHITE,NSE:GREAVESCOT,NSE:IGIL,NSE:IIFLCAPS,NSE:INDIGO,NSE:INOXINDIA,NSE:JSWINFRA,NSE:KAJARIACER,NSE:KOPRAN,NSE:LGEINDIA,NSE:LODHA,NSE:LTTS,NSE:MANKIND,NSE:METROPOLIS,NSE:MOTHERSON,NSE:NEULANDLAB,NSE:NUVAMA,NSE:PARAGMILK,NSE:PETRONET,NSE:PNBHOUSING,NSE:POONAWALLA,NSE:PROTEAN,NSE:PTCIL,NSE:RAYMONDREL,NSE:SHAILY,NSE:TECHM,NSE:UNOMINDA,NSE:VIJAYA,NSE:WOCKPHARMA,NSE:ZYDUSLIFE
```

**2-4 WEEKS** (43)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABCAPITAL,NSE:ACE,NSE:ADANIPORTS,NSE:ANTHEM,NSE:APLLTD,NSE:APOLLO,NSE:AUROPHARMA,NSE:BALUFORGE,NSE:BOSCHLTD,NSE:DCBBANK,NSE:DIVISLAB,NSE:DLF,NSE:ETERNAL,NSE:FLUOROCHEM,NSE:GAIL,NSE:GLENMARK,NSE:HFCL,NSE:HONASA,NSE:ICIL,NSE:INDGN,NSE:JYOTICNC,NSE:KALYANKJIL,NSE:KARURVYSYA,NSE:KPRMILL,NSE:KTKBANK,NSE:LALPATHLAB,NSE:MAHABANK,NSE:MANAKCOAT,NSE:MCX,NSE:MOTILALOFS,NSE:NAVINFLUOR,NSE:NYKAA,NSE:PHOENIXLTD,NSE:RADICO,NSE:RKFORGE,NSE:RUBICON,NSE:SAILIFE,NSE:SANSERA,NSE:STYLEBAAZA,NSE:TANLA,NSE:TVSMOTOR,NSE:URBANCO,NSE:WELSPUNLIV
```

**1-2 MONTHS** (14)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AARTIPHARM,NSE:ACUTAAS,NSE:ARIS,NSE:ATHERENERG,NSE:CCAVENUE,NSE:GLAND,NSE:GRWRHITECH,NSE:INDHOTEL,NSE:PPLPHARMA,NSE:PVRINOX,NSE:SAREGAMA,NSE:SONACOMS,NSE:SOUTHBANK,NSE:STLTECH
```

**2-3 MONTHS** (5)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:CUPID,NSE:GCSL,NSE:MOREPENLAB,NSE:UTTAMSUGAR
```

**3-6 MONTHS** (6)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:RATNAVEER,NSE:RAYMOND,NSE:SBC,NSE:SHREEJISPG,NSE:TFCILTD,NSE:THELEELA
```

**6+ MONTHS** (1)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LAURUSLABS
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
