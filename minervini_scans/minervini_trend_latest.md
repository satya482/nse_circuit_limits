> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-11-27
*Generated 2026-11-27 15:49 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR) | [ARIS](https://in.tradingview.com/chart/?symbol=NSE:ARIS) |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG) | [AVADHSUGAR](https://in.tradingview.com/chart/?symbol=NSE:AVADHSUGAR) |
| [AGARWALEYE](https://in.tradingview.com/chart/?symbol=NSE:AGARWALEYE) | [DCBBANK](https://in.tradingview.com/chart/?symbol=NSE:DCBBANK) |
| [ASTRAMICRO](https://in.tradingview.com/chart/?symbol=NSE:ASTRAMICRO) | [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM) |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN) | [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH) |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE) | [ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL) |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH) | [KAJARIACER](https://in.tradingview.com/chart/?symbol=NSE:KAJARIACER) |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO) | [KOPRAN](https://in.tradingview.com/chart/?symbol=NSE:KOPRAN) |
| [HAL](https://in.tradingview.com/chart/?symbol=NSE:HAL) | [LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS) |
| [LENSKART](https://in.tradingview.com/chart/?symbol=NSE:LENSKART) | [METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS) |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE) | [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON) |
| [MEDANTA](https://in.tradingview.com/chart/?symbol=NSE:MEDANTA) | [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA) |
| [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT) | [PROTEAN](https://in.tradingview.com/chart/?symbol=NSE:PROTEAN) |
| [PARAS](https://in.tradingview.com/chart/?symbol=NSE:PARAS) | [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA) |
| [PRESTIGE](https://in.tradingview.com/chart/?symbol=NSE:PRESTIGE) | [TANLA](https://in.tradingview.com/chart/?symbol=NSE:TANLA) |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER) | [VIJAYA](https://in.tradingview.com/chart/?symbol=NSE:VIJAYA) |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV) | [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE) |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART) |  |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL) |  |
| [SPORTKING](https://in.tradingview.com/chart/?symbol=NSE:SPORTKING) |  |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM) |  |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH) |  |

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

**Qualifying: 119**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ACMESOLAR,NSE:AEGISLOG,NSE:AETHER,NSE:ASTRAMICRO,NSE:BAJAJHLDNG,NSE:BALRAMCHIN,NSE:BEML,NSE:COHANCE,NSE:CPPLUS,NSE:CRAFTSMAN,NSE:DALMIASUG,NSE:DHAMPURSUG,NSE:ENGINERSIN,NSE:FEDERALBNK,NSE:FILATEX,NSE:GABRIEL,NSE:GESHIP,NSE:GLAXO,NSE:GRAPHITE,NSE:GREAVESCOT,NSE:HAL,NSE:IGIL,NSE:IIFLCAPS,NSE:INDIGO,NSE:INOXINDIA,NSE:JSWINFRA,NSE:LENSKART,NSE:LGEINDIA,NSE:MANKIND,NSE:MARINE,NSE:NEULANDLAB,NSE:NUVAMA,NSE:ONEPOINT,NSE:PARAS,NSE:PNBHOUSING,NSE:PRESTIGE,NSE:PTCIL,NSE:QPOWER,NSE:RAYMONDREL,NSE:SAMBHV,NSE:SHAILY,NSE:SPORTKING,NSE:TECHM,NSE:TORNTPHARM,NSE:UNIMECH,NSE:UNOMINDA,NSE:WOCKPHARMA,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABCAPITAL,NSE:ACE,NSE:AGARWALEYE,NSE:ANTHEM,NSE:APLLTD,NSE:APOLLO,NSE:AUROPHARMA,NSE:BALUFORGE,NSE:BOSCHLTD,NSE:DLF,NSE:DYNAMATECH,NSE:ENTERO,NSE:GAIL,NSE:GLENMARK,NSE:HFCL,NSE:HONASA,NSE:INDGN,NSE:JYOTICNC,NSE:KALYANKJIL,NSE:KARURVYSYA,NSE:KPRMILL,NSE:KTKBANK,NSE:LALPATHLAB,NSE:LODHA,NSE:MAHABANK,NSE:MANAKCOAT,NSE:MCX,NSE:MEDANTA,NSE:MOTILALOFS,NSE:NAVINFLUOR,NSE:PARAGMILK,NSE:PETRONET,NSE:POONAWALLA,NSE:RADICO,NSE:RKFORGE,NSE:RUBICON,NSE:SAILIFE,NSE:SANSERA,NSE:STYLEBAAZA,NSE:TVSMOTOR,NSE:URBANCO,NSE:WELSPUNLIV,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AARTIPHARM,NSE:ACUTAAS,NSE:ADANIPORTS,NSE:ATHERENERG,NSE:CCAVENUE,NSE:COFORGE,NSE:DIVISLAB,NSE:ETERNAL,NSE:GLAND,NSE:INDHOTEL,NSE:PHOENIXLTD,NSE:PPLPHARMA,NSE:SGMART,NSE:SHYAMMETL,NSE:SONACOMS,NSE:SOUTHBANK,NSE:STLTECH,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABDL,NSE:CUPID,NSE:GCSL,NSE:MOREPENLAB,NSE:PVRINOX,NSE:UTTAMSUGAR,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:RATNAVEER,NSE:RAYMOND,NSE:SBC,NSE:SHREEJISPG,NSE:TFCILTD,NSE:THELEELA,###6+ MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:LAURUSLABS
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [HAL](https://in.tradingview.com/chart/?symbol=NSE:HAL)<br><sub>✓ SAFE . ↗483Cr · 1224Cr . ↑CMF25d</sub> | 5074.00 | -0.5% | +45.5% | 0d | SMA-OK | RS-OK | +3.35% |
| [TECHM](https://in.tradingview.com/chart/?symbol=NSE:TECHM)<br><sub>✓ SAFE . →366Cr · 361Cr . ↓CMF5d</sub> | 1813.90 | -2.2% | +36.6% | 0d | SMA-OK | RS-OK | -2.20% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>⚠ CAUTION . ↗234Cr · 359Cr . ↑CMF20d</sub> | 5034.00 | -1.7% | +36.6% | 0d | SMA-OK | RS-OK | +0.30% |
| [DHAMPURSUG](https://in.tradingview.com/chart/?symbol=NSE:DHAMPURSUG)<br><sub>✓ SAFE . ↗117Cr · 313Cr . ↑CMF1d</sub> | 195.46 | -5.9% | +76.9% | 0d | SMA-OK | RS-OK | +8.58% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>✓ SAFE . ↘80Cr · 214Cr . ↑CMF30d</sub> | 1297.90 | -12.8% | +120.8% | 0d | SMA-OK | RS-OK | +7.16% |
| [PARAS](https://in.tradingview.com/chart/?symbol=NSE:PARAS)<br><sub>✓ SAFE . ↘48Cr · 173Cr . ↓CMF4d</sub> | 1302.60 | -14.7% | +122.8% | 0d | SMA-OK | RS-OK | +5.04% |
| [LGEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LGEINDIA)<br><sub>✓ SAFE . ↗430Cr · 156Cr . ↓CMF10d</sub> | 1770.90 | -1.3% | +34.3% | 0d | SMA-OK | RS-OK | +0.73% |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY)<br><sub>✓ SAFE . ↗110Cr · 136Cr . ↑CMF1d</sub> | 3350.50 | -3.1% | +83.9% | 0d | SMA-OK | RS-OK | -0.86% |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>✓ SAFE . ↘54Cr · 123Cr . ↑CMF18d</sub> | 675.45 | -11.9% | +69.8% | 0d | SMA-OK | RS-OK | +3.93% |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>✓ SAFE . ↗38Cr · 102Cr . ↑CMF0d</sub> | 426.35 | -7.0% | +114.3% | 0d | SMA-OK | RS-OK | +2.54% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>✓ SAFE . →46Cr · 80Cr . ↑CMF7d</sub> | 1761.40 | -2.1% | +115.9% | 0d | SMA-OK | RS-OK | +3.56% |
| [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA)<br><sub>⚠ CAUTION . ↗77Cr · 72Cr . ↑CMF17d</sub> | 355.50 | -3.3% | +51.7% | 0d | SMA-OK | RS-OK | -2.78% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>⚠ CAUTION . ↗47Cr · 68Cr . ↑CMF4d</sub> | 25460.00 | -1.0% | +72.9% | 0d | SMA-OK | RS-OK | +2.35% |
| [NEULANDLAB](https://in.tradingview.com/chart/?symbol=NSE:NEULANDLAB)<br><sub>✓ SAFE . ↘79Cr · 62Cr . ↑CMF17d</sub> | 21435.00 | -10.7% | +85.5% | 0d | SMA-OK | RS-OK | +1.50% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . ↘62Cr · 54Cr . ↓CMF15d</sub> | 4307.20 | -3.0% | +214.1% | 0d | SMA-OK | RS-OK | +1.70% |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE)<br><sub>↘34Cr · 52Cr . ↓CMF19d</sub> | 439.45 | -8.2% | +189.7% | 0d | SMA-OK | RS-OK | +4.84% |
| [ASTRAMICRO](https://in.tradingview.com/chart/?symbol=NSE:ASTRAMICRO)<br><sub>✓ SAFE . ↘37Cr · 49Cr . ↑CMF0d</sub> | 1666.90 | -10.5% | +94.8% | 0d | SMA-OK | RS-OK | +2.86% |
| [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT)<br><sub>✓ SAFE . ↗20Cr · 38Cr . ↑CMF12d</sub> | 74.60 | -12.4% | +80.2% | 0d | SMA-OK | RS-OK | +8.48% |
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP)<br><sub>✓ SAFE . ↘61Cr · 37Cr . ↓CMF6d</sub> | 1550.60 | -9.8% | +44.7% | 0d | SMA-OK | RS-OK | +1.27% |
| [IIFLCAPS](https://in.tradingview.com/chart/?symbol=NSE:IIFLCAPS)<br><sub>✓ SAFE . →95Cr · 34Cr . ↓CMF10d</sub> | 346.80 | -12.3% | +42.0% | 0d | SMA-OK | RS-OK | +0.19% |
| [DALMIASUG](https://in.tradingview.com/chart/?symbol=NSE:DALMIASUG)<br><sub>✓ SAFE . ↘10Cr · 29Cr . ↑CMF30d</sub> | 486.05 | -4.3% | +83.8% | 0d | SMA-OK | RS-OK | +7.74% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>✓ SAFE . ↗61Cr · 27Cr . ↑CMF4d</sub> | 177.30 | 0.0% | +115.4% | 0d | SMA-OK | RS-OK | +1.87% |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE)<br><sub>✓ SAFE . ↘36Cr · 21Cr . ↑CMF17d</sub> | 792.00 | -7.0% | +50.5% | 0d | SMA-OK | RS-OK | +0.03% |
| [PRESTIGE](https://in.tradingview.com/chart/?symbol=NSE:PRESTIGE)<br><sub>✓ SAFE . ↗237Cr · 258Cr . ↑CMF19d</sub> | 1796.70 | -1.9% | +59.5% | 1d | SMA-OK | RS-OK | -1.93% |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER)<br><sub>✓ SAFE . →49Cr · 43Cr . ↓CMF30d</sub> | 1496.80 | -9.2% | +151.5% | 1d | SMA-OK | RS-OK | +1.66% |
| [RAYMONDREL](https://in.tradingview.com/chart/?symbol=NSE:RAYMONDREL)<br><sub>✓ SAFE . ↗37Cr · 64Cr . ↑CMF6d</sub> | 651.60 | -9.8% | +82.3% | 2d | SMA-OK | RS-OK | +5.26% |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN)<br><sub>✓ SAFE . ↘61Cr · 55Cr . ↑CMF19d</sub> | 300.75 | -4.7% | +82.8% | 2d | SMA-OK | RS-OK | +3.30% |
| [GLAXO](https://in.tradingview.com/chart/?symbol=NSE:GLAXO)<br><sub>⚠ CAUTION . ↘23Cr · 35Cr . ↑CMF13d</sub> | 2770.40 | -10.8% | +31.7% | 2d | SMA-OK | RS-OK | -0.34% |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH)<br><sub>✓ SAFE . ↘23Cr · 34Cr . ↑CMF17d</sub> | 1848.90 | -6.6% | +161.8% | 2d | SMA-OK | RS-OK | +5.09% |
| [BAJAJHLDNG](https://in.tradingview.com/chart/?symbol=NSE:BAJAJHLDNG)<br><sub>⚠ CAUTION . →37Cr · 35Cr . ↑CMF3d</sub> | 11703.00 | -1.9% | +33.8% | 3d | SMA-OK | RS-OK | -1.93% |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA)<br><sub>✓ SAFE . ↘37Cr · 33Cr . ↓CMF7d</sub> | 1835.00 | -7.3% | +65.2% | 3d | SMA-OK | RS-OK | -1.07% |
| [WOCKPHARMA](https://in.tradingview.com/chart/?symbol=NSE:WOCKPHARMA)<br><sub>✓ SAFE . ↗201Cr · 190Cr . ↑CMF16d</sub> | 2244.40 | -3.7% | +104.0% | 5d | SMA-OK | RS-OK | +0.48% |
| [COHANCE](https://in.tradingview.com/chart/?symbol=NSE:COHANCE)<br><sub>✓ SAFE . ↗96Cr · 80Cr . ↓CMF2d</sub> | 497.55 | -10.0% | +77.8% | 5d | SMA-OK | RS-OK | -1.00% |
| [SPORTKING](https://in.tradingview.com/chart/?symbol=NSE:SPORTKING)<br><sub>✓ SAFE . ↗24Cr · 62Cr . ↑CMF0d</sub> | 249.03 | 0.0% | +212.5% | 5d | SMA-OK | RS-OK | +7.91% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>⚠ CAUTION . →61Cr · 47Cr . ↑CMF0d</sub> | 1162.00 | -5.1% | +54.8% | 5d | SMA-OK | RS-OK | -0.77% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>✓ SAFE . ↗128Cr · 29Cr . ↑CMF7d</sub> | 2139.30 | -6.8% | +99.3% | 5d | SMA-OK | RS-OK | -1.09% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>✓ SAFE . ↘95Cr · 107Cr . ↓CMF1d</sub> | 2689.40 | 0.0% | +39.5% | 8d | SMA-OK | RS-OK | +0.16% |
| [LENSKART](https://in.tradingview.com/chart/?symbol=NSE:LENSKART)<br><sub>✓ SAFE . ↘290Cr · 150Cr . ↓CMF2d</sub> | 718.35 | -3.5% | +77.7% | 9d | SMA-OK | RS-OK | +0.22% |
| [IGIL](https://in.tradingview.com/chart/?symbol=NSE:IGIL)<br><sub>✓ SAFE . ↘37Cr · 104Cr . ↓CMF5d</sub> | 429.65 | -4.6% | +47.6% | 9d | SMA-OK | RS-OK | +1.52% |
| [UNOMINDA](https://in.tradingview.com/chart/?symbol=NSE:UNOMINDA)<br><sub>✓ SAFE . ↘118Cr · 89Cr . ↑CMF21d</sub> | 1354.00 | -2.6% | +33.6% | 9d | SMA-OK | RS-OK | -2.59% |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML)<br><sub>✓ SAFE . ↗267Cr · 2352Cr . ↑CMF0d</sub> | 2346.10 | 0.0% | +71.3% | 10d | SMA-OK | RS-OK | +14.99% |
| [INDIGO](https://in.tradingview.com/chart/?symbol=NSE:INDIGO)<br><sub>✓ SAFE . ↘437Cr · 489Cr . ↑CMF13d</sub> | 5659.60 | -4.4% | +43.5% | 10d | SMA-OK | RS-OK | +0.62% |
| [GREAVESCOT](https://in.tradingview.com/chart/?symbol=NSE:GREAVESCOT)<br><sub>✓ SAFE . ↗531Cr · 425Cr . ↑CMF19d</sub> | 322.69 | -1.0% | +167.5% | 10d | SMA-OK | RS-OK | -0.95% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>⚠ CAUTION . →234Cr · 139Cr . ↑CMF29d</sub> | 360.00 | -3.6% | +45.8% | 10d | SMA-OK | RS-OK | +0.88% |
| [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN)<br><sub>⚠ CAUTION . →48Cr · 40Cr . ↑CMF30d</sub> | 12005.00 | 0.0% | +83.4% | 10d | SMA-OK | RS-OK | +1.22% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>✓ SAFE . ↘53Cr · 33Cr . ↑CMF11d</sub> | 1546.80 | -5.8% | +87.9% | 10d | SMA-OK | RS-OK | +0.62% |
| [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX)<br><sub>✓ SAFE . ↗49Cr · 28Cr . ↓CMF8d . DEL68%(T-1)</sub> | 112.57 | 0.0% | +205.1% | 10d | SMA-OK | RS-OK | +2.29% |
| [LODHA](https://in.tradingview.com/chart/?symbol=NSE:LODHA)<br><sub>✓ SAFE . →190Cr · 439Cr . ↑CMF15d</sub> | 1251.80 | -4.9% | +84.9% | 11d | SMA-OK | RS-OK | -0.75% |
| [POONAWALLA](https://in.tradingview.com/chart/?symbol=NSE:POONAWALLA)<br><sub>✓ SAFE . →100Cr · 71Cr . ↑CMF20d</sub> | 494.90 | -4.5% | +34.3% | 11d | SMA-OK | RS-OK | -2.69% |
| [PETRONET](https://in.tradingview.com/chart/?symbol=NSE:PETRONET)<br><sub>✓ SAFE . ↘67Cr · 52Cr . ↑CMF24d</sub> | 322.35 | -3.8% | +35.4% | 11d | SMA-OK | RS-OK | -1.26% |
| [PARAGMILK](https://in.tradingview.com/chart/?symbol=NSE:PARAGMILK)<br><sub>✓ SAFE . ↘49Cr · 44Cr . ↑CMF17d</sub> | 321.63 | -6.5% | +78.8% | 11d | SMA-OK | RS-OK | +1.96% |
| [BALUFORGE](https://in.tradingview.com/chart/?symbol=NSE:BALUFORGE)<br><sub>✓ SAFE . →45Cr · 24Cr . ↑CMF16d</sub> | 529.95 | -18.9% | +48.7% | 12d | SMA-OK | RS-OK | +0.20% |
| [DLF](https://in.tradingview.com/chart/?symbol=NSE:DLF)<br><sub>✓ SAFE . →247Cr · 248Cr . ↑CMF16d</sub> | 805.45 | -0.3% | +59.8% | 13d | SMA-OK | RS-OK | -0.29% |
| [URBANCO](https://in.tradingview.com/chart/?symbol=NSE:URBANCO)<br><sub>✓ SAFE . ↗287Cr · 224Cr . ↑CMF12d</sub> | 174.92 | -3.4% | +69.8% | 13d | SMA-OK | RS-OK | +2.46% |
| [AGARWALEYE](https://in.tradingview.com/chart/?symbol=NSE:AGARWALEYE)<br><sub>⚠ CAUTION . ↘11Cr · 28Cr . ↑CMF30d</sub> | 581.35 | 0.0% | +43.0% | 13d | SMA-OK | RS-OK | +1.53% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>✓ SAFE . ↘64Cr · 48Cr . ↑CMF12d</sub> | 335.25 | -9.1% | +87.5% | 14d | SMA-OK | RS-OK | -1.31% |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>✓ SAFE . ↘859Cr · 691Cr . ↑CMF15d</sub> | 659.50 | -7.2% | +99.4% | 15d | SMA-OK | RS-OK | +3.08% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>✓ SAFE . →134Cr · 249Cr . ↑CMF14d</sub> | 410.30 | -3.4% | +40.4% | 15d | SMA-OK | RS-OK | -0.77% |
| [MOTILALOFS](https://in.tradingview.com/chart/?symbol=NSE:MOTILALOFS)<br><sub>✓ SAFE . ↘164Cr · 226Cr . ↑CMF16d</sub> | 1222.15 | -1.5% | +94.5% | 15d | SMA-OK | RS-OK | +0.57% |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE)<br><sub>✓ SAFE . ↗77Cr · 122Cr . ↑CMF1d</sub> | 1325.70 | 0.0% | +77.0% | 15d | SMA-OK | RS-OK | +2.37% |
| [RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO)<br><sub>✓ SAFE . ↘132Cr · 104Cr . ↑CMF21d</sub> | 4646.60 | -1.8% | +82.9% | 15d | SMA-OK | RS-OK | -0.52% |
| [STYLEBAAZA](https://in.tradingview.com/chart/?symbol=NSE:STYLEBAAZA)<br><sub>✓ SAFE . ↗139Cr · 53Cr . ↑CMF14d</sub> | 511.70 | -5.1% | +115.8% | 15d | SMA-OK | RS-OK | -0.60% |
| [JYOTICNC](https://in.tradingview.com/chart/?symbol=NSE:JYOTICNC)<br><sub>✓ SAFE . ↘34Cr · 36Cr . ↑CMF17d</sub> | 1058.65 | -5.0% | +80.8% | 15d | SMA-OK | RS-OK | +0.79% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>✓ SAFE . ↘48Cr · 33Cr . ↑CMF22d</sub> | 781.25 | -1.3% | +68.8% | 15d | SMA-OK | RS-OK | -0.84% |
| [MEDANTA](https://in.tradingview.com/chart/?symbol=NSE:MEDANTA)<br><sub>✓ SAFE . ↘28Cr · 28Cr . ↑CMF18d</sub> | 1473.70 | -3.6% | +53.3% | 15d | SMA-OK | RS-OK | -2.50% |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH)<br><sub>✓ SAFE . ↘16Cr · 25Cr . ↑CMF11d</sub> | 13877.00 | -3.8% | +75.7% | 15d | SMA-OK | RS-OK | +4.94% |
| [APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD)<br><sub>✓ SAFE . ↘26Cr · 21Cr . ↓CMF1d</sub> | 1013.40 | -4.1% | +56.7% | 15d | SMA-OK | RS-OK | -0.53% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>✓ SAFE . →391Cr · 262Cr . ↑CMF24d</sub> | 4526.50 | -1.6% | +37.9% | 17d | SMA-OK | RS-OK | -0.52% |
| [MAHABANK](https://in.tradingview.com/chart/?symbol=NSE:MAHABANK)<br><sub>✓ SAFE . →205Cr · 172Cr . ↑CMF23d</sub> | 95.73 | -3.7% | +70.3% | 17d | SMA-OK | RS-OK | +1.62% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>✓ SAFE . ↘24Cr · 36Cr . ↑CMF15d</sub> | 1823.40 | -13.8% | +92.1% | 17d | SMA-OK | RS-OK | -0.47% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>✓ SAFE . ↘162Cr · 154Cr . ↑CMF16d</sub> | 185.00 | -3.7% | +36.6% | 18d | SMA-OK | RS-OK | -1.60% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>✓ SAFE . ↗133Cr · 108Cr . ↑CMF7d</sub> | 371.10 | -5.7% | +53.9% | 18d | SMA-OK | RS-OK | +0.30% |
| [MANAKCOAT](https://in.tradingview.com/chart/?symbol=NSE:MANAKCOAT)<br><sub>✓ SAFE . ↘24Cr · 63Cr . ↓CMF5d</sub> | 165.68 | -6.2% | +71.3% | 18d | SMA-OK | RS-OK | +3.25% |
| [HONASA](https://in.tradingview.com/chart/?symbol=NSE:HONASA)<br><sub>✓ SAFE . →84Cr · 52Cr . ↑CMF12d</sub> | 512.55 | -5.0% | +100.0% | 18d | SMA-OK | RS-OK | -3.88% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>✓ SAFE . ↘33Cr · 40Cr . ↑CMF25d</sub> | 984.15 | 0.0% | +67.4% | 18d | SMA-OK | RS-OK | +0.89% |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . ↘913Cr · 1175Cr . ↑CMF23d</sub> | 3900.00 | 0.0% | +97.7% | 19d | SMA-OK | RS-OK | +1.69% |
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO)<br><sub>✓ SAFE . ↘336Cr · 305Cr . ↑CMF3d</sub> | 435.50 | -8.4% | +139.1% | 19d | SMA-OK | RS-OK | +1.56% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>✓ SAFE . ↘217Cr · 214Cr . ↑CMF22d</sub> | 1791.80 | -3.4% | +59.7% | 19d | SMA-OK | RS-OK | -1.06% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>✓ SAFE . ↘42Cr · 26Cr . ↓CMF4d</sub> | 1983.30 | -2.8% | +51.7% | 19d | SMA-OK | RS-OK | -2.68% |
| [GLENMARK](https://in.tradingview.com/chart/?symbol=NSE:GLENMARK)<br><sub>✓ SAFE . ↘152Cr · 259Cr . ↑CMF19d</sub> | 2834.90 | 0.0% | +47.6% | 20d | SMA-OK | RS-OK | +3.46% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↘64Cr · 45Cr . ↑CMF13d</sub> | 4742.20 | -1.2% | +191.0% | 20d | SMA-OK | RS-OK | +1.20% |
| [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN)<br><sub>✓ SAFE . ↘33Cr · 44Cr . ↓CMF19d</sub> | 670.60 | 0.0% | +58.3% | 20d | SMA-OK | RS-OK | +1.98% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>✓ SAFE . ↘34Cr · 44Cr . ↑CMF25d</sub> | 1869.30 | 0.0% | +203.9% | 20d | SMA-OK | RS-OK | +0.95% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . ↘219Cr · 247Cr . ↑CMF23d</sub> | 10456.50 | 0.0% | +88.0% | 21d | SMA-OK | RS-OK | +1.82% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↘210Cr · 140Cr . ↑CMF19d</sub> | 285.52 | 0.0% | +163.6% | 21d | SMA-OK | RS-OK | +1.84% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>✓ SAFE . ↘116Cr · 113Cr . ↑CMF20d</sub> | 49170.00 | -6.3% | +71.1% | 21d | SMA-OK | RS-OK | +0.70% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . ↘121Cr · 48Cr . ↑CMF20d</sub> | 1806.10 | -6.4% | +127.2% | 21d | SMA-OK | RS-OK | -0.36% |
| [KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL)<br><sub>✓ SAFE . ↗69Cr · 44Cr . ↓CMF2d . DEL80%(T-1)</sub> | 1217.30 | -0.1% | +50.1% | 21d | SMA-OK | RS-OK | +2.25% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . ↘755Cr · 436Cr . ↑CMF21d</sub> | 11560.00 | -0.6% | +98.6% | 22d | SMA-OK | RS-OK | -0.61% |
| [PHOENIXLTD](https://in.tradingview.com/chart/?symbol=NSE:PHOENIXLTD)<br><sub>⚠ CAUTION . ↗135Cr · 124Cr . ↑CMF16d</sub> | 2229.70 | -2.7% | +50.9% | 22d | SMA-OK | RS-OK | -2.68% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>✓ SAFE . ↘404Cr · 1269Cr . ↑CMF30d</sub> | 1880.00 | -3.6% | +44.2% | 23d | SMA-OK | RS-OK | -1.64% |
| [ETERNAL](https://in.tradingview.com/chart/?symbol=NSE:ETERNAL)<br><sub>⚠ CAUTION . →743Cr · 688Cr . ↑CMF19d</sub> | 363.00 | -3.2% | +68.3% | 23d | SMA-OK | RS-OK | -1.28% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>✓ SAFE . ↗148Cr · 113Cr . ↑CMF22d</sub> | 231.00 | -6.2% | +73.3% | 23d | SMA-OK | RS-OK | -1.95% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . →156Cr · 160Cr . ↑CMF24d</sub> | 879.00 | -5.1% | +97.8% | 24d | SMA-OK | RS-OK | -0.28% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↘74Cr · 93Cr . ↑CMF30d</sub> | 3362.00 | -0.7% | +110.5% | 24d | SMA-OK | RS-OK | -0.26% |
| [AARTIPHARM](https://in.tradingview.com/chart/?symbol=NSE:AARTIPHARM)<br><sub>✓ SAFE . →52Cr · 39Cr . ↑CMF19d</sub> | 1015.15 | -1.0% | +71.5% | 24d | SMA-OK | RS-OK | -0.68% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>✓ SAFE . ↘328Cr · 264Cr . ↑CMF24d</sub> | 884.80 | -3.0% | +55.0% | 25d | SMA-OK | RS-OK | -0.21% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . ↘357Cr · 206Cr . ↑CMF24d</sub> | 1888.40 | -4.6% | +214.0% | 25d | SMA-OK | RS-OK | -0.92% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>✓ SAFE . ↘144Cr · 189Cr . ↓CMF0d</sub> | 4075.00 | -0.1% | +154.3% | 25d | SMA-OK | RS-OK | -0.12% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>✓ SAFE . ↗467Cr · 1006Cr . ↑CMF1d</sub> | 913.15 | -16.8% | +185.9% | 26d | SMA-OK | RS-OK | +3.64% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [CCAVENUE](https://in.tradingview.com/chart/?symbol=NSE:CCAVENUE)<br><sub>✓ SAFE . →17Cr · 46Cr . ↑CMF0d</sub> | 119.09 | -13.9% | +805.6% | 30d | SMA-OK | RS-OK | +3.53% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>✓ SAFE . ↗816Cr · 989Cr . ↓CMF0d</sub> | 2071.00 | -3.3% | +92.8% | 31d | SMA-OK | RS-OK | +3.55% |
| [SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK)<br><sub>✓ SAFE . →76Cr · 46Cr . ↓CMF1d</sub> | 58.12 | -6.0% | +73.0% | 36d | SMA-OK | RS-OK | +0.92% |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL)<br><sub>✓ SAFE . ↘30Cr · 23Cr . ↓CMF0d</sub> | 1305.40 | -2.9% | +71.4% | 39d | SMA-OK | RS-OK | +0.96% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . ↘112Cr · 85Cr . ↑CMF2d</sub> | 1679.10 | -2.1% | +82.8% | 43d | SMA-OK | RS-OK | +2.50% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↘345Cr · 768Cr . ↑CMF11d</sub> | 389.50 | 0.0% | +458.0% | 44d | SMA-OK | RS-OK | +4.96% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>✓ SAFE . ↗68Cr · 51Cr . ↑CMF7d</sub> | 838.00 | 0.0% | +118.1% | 45d | SMA-OK | RS-OK | +2.16% |
| [UTTAMSUGAR](https://in.tradingview.com/chart/?symbol=NSE:UTTAMSUGAR)<br><sub>✓ SAFE . ↗17Cr · 25Cr . ↑CMF4d</sub> | 390.65 | 0.0% | +108.5% | 45d | SMA-OK | RS-OK | +2.32% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↗253Cr · 230Cr . ↑CMF30d</sub> | 129.55 | -11.9% | +284.6% | 48d | SMA-OK | RS-OK | -5.13% |
| [GCSL](https://in.tradingview.com/chart/?symbol=NSE:GCSL)<br><sub>✓ SAFE . →22Cr · 23Cr . ↓CMF0d</sub> | 851.55 | -0.1% | +202.3% | 57d | SMA-OK | RS-OK | +0.12% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . ↘55Cr · 73Cr . ↑CMF30d</sub> | 923.70 | 0.0% | +201.5% | 65d | SMA-OK | RS-OK | +1.43% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . →72Cr · 66Cr . ↓CMF22d</sub> | 68.10 | -3.2% | +155.8% | 65d | SMA-OK | RS-OK | -0.37% |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA)<br><sub>✓ SAFE . ↘28Cr · 28Cr . ↑CMF11d</sub> | 690.00 | -1.2% | +77.1% | 74d | SMA-OK | RS-OK | +0.61% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . →72Cr · 189Cr . ↑CMF11d</sub> | 1278.60 | -1.7% | +297.3% | 75d | SMA-OK | RS-OK | +8.06% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . →143Cr · 416Cr . ↓CMF0d</sub> | 398.30 | -1.7% | +203.4% | 92d | SMA-OK | RS-OK | -1.65% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . ↘110Cr · 209Cr . ↑CMF23d</sub> | 173.97 | -0.6% | +214.9% | 95d | SMA-OK | RS-OK | -0.55% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . →688Cr · 549Cr . ↑CMF22d</sub> | 2504.40 | -0.0% | +169.2% | 140d | SMA-OK | RS-OK | -0.02% |

### By Trend Age

**<2 WEEKS** (47)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ACMESOLAR,NSE:AEGISLOG,NSE:AETHER,NSE:ASTRAMICRO,NSE:BAJAJHLDNG,NSE:BALRAMCHIN,NSE:BEML,NSE:COHANCE,NSE:CPPLUS,NSE:CRAFTSMAN,NSE:DALMIASUG,NSE:DHAMPURSUG,NSE:ENGINERSIN,NSE:FEDERALBNK,NSE:FILATEX,NSE:GABRIEL,NSE:GESHIP,NSE:GLAXO,NSE:GRAPHITE,NSE:GREAVESCOT,NSE:HAL,NSE:IGIL,NSE:IIFLCAPS,NSE:INDIGO,NSE:INOXINDIA,NSE:JSWINFRA,NSE:LENSKART,NSE:LGEINDIA,NSE:MANKIND,NSE:MARINE,NSE:NEULANDLAB,NSE:NUVAMA,NSE:ONEPOINT,NSE:PARAS,NSE:PNBHOUSING,NSE:PRESTIGE,NSE:PTCIL,NSE:QPOWER,NSE:RAYMONDREL,NSE:SAMBHV,NSE:SHAILY,NSE:SPORTKING,NSE:TECHM,NSE:TORNTPHARM,NSE:UNIMECH,NSE:UNOMINDA,NSE:WOCKPHARMA
```

**2-4 WEEKS** (42)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABCAPITAL,NSE:ACE,NSE:AGARWALEYE,NSE:ANTHEM,NSE:APLLTD,NSE:APOLLO,NSE:AUROPHARMA,NSE:BALUFORGE,NSE:BOSCHLTD,NSE:DLF,NSE:DYNAMATECH,NSE:ENTERO,NSE:GAIL,NSE:GLENMARK,NSE:HFCL,NSE:HONASA,NSE:INDGN,NSE:JYOTICNC,NSE:KALYANKJIL,NSE:KARURVYSYA,NSE:KPRMILL,NSE:KTKBANK,NSE:LALPATHLAB,NSE:LODHA,NSE:MAHABANK,NSE:MANAKCOAT,NSE:MCX,NSE:MEDANTA,NSE:MOTILALOFS,NSE:NAVINFLUOR,NSE:PARAGMILK,NSE:PETRONET,NSE:POONAWALLA,NSE:RADICO,NSE:RKFORGE,NSE:RUBICON,NSE:SAILIFE,NSE:SANSERA,NSE:STYLEBAAZA,NSE:TVSMOTOR,NSE:URBANCO,NSE:WELSPUNLIV
```

**1-2 MONTHS** (17)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AARTIPHARM,NSE:ACUTAAS,NSE:ADANIPORTS,NSE:ATHERENERG,NSE:CCAVENUE,NSE:COFORGE,NSE:DIVISLAB,NSE:ETERNAL,NSE:GLAND,NSE:INDHOTEL,NSE:PHOENIXLTD,NSE:PPLPHARMA,NSE:SGMART,NSE:SHYAMMETL,NSE:SONACOMS,NSE:SOUTHBANK,NSE:STLTECH
```

**2-3 MONTHS** (6)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:CUPID,NSE:GCSL,NSE:MOREPENLAB,NSE:PVRINOX,NSE:UTTAMSUGAR
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
