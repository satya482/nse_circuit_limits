> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-10-09
*Generated 2026-10-09 15:46 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [ARIS](https://in.tradingview.com/chart/?symbol=NSE:ARIS) | [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR) |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA) | [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER) |
| [AVTNPL](https://in.tradingview.com/chart/?symbol=NSE:AVTNPL) | [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO) |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE) | [AVADHSUGAR](https://in.tradingview.com/chart/?symbol=NSE:AVADHSUGAR) |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH) | [CEIGALL](https://in.tradingview.com/chart/?symbol=NSE:CEIGALL) |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA) | [CONFIPET](https://in.tradingview.com/chart/?symbol=NSE:CONFIPET) |
| [KIRLOSENG](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSENG) | [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX) |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK) | [GCSL](https://in.tradingview.com/chart/?symbol=NSE:GCSL) |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB) | [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA) |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN) | [GREAVESCOT](https://in.tradingview.com/chart/?symbol=NSE:GREAVESCOT) |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA) | [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB) |
| [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT) | [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR) |
| [QUADFUTURE](https://in.tradingview.com/chart/?symbol=NSE:QUADFUTURE) | [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL) |
| [RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO) | [SMSPHARMA](https://in.tradingview.com/chart/?symbol=NSE:SMSPHARMA) |
| [RAIN](https://in.tradingview.com/chart/?symbol=NSE:RAIN) | [STAR](https://in.tradingview.com/chart/?symbol=NSE:STAR) |
| [SGFIN](https://in.tradingview.com/chart/?symbol=NSE:SGFIN) | [TI](https://in.tradingview.com/chart/?symbol=NSE:TI) |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV) | [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH) |
| [YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH) | [URBANCO](https://in.tradingview.com/chart/?symbol=NSE:URBANCO) |
|  | [WELENT](https://in.tradingview.com/chart/?symbol=NSE:WELENT) |
|  | [WHEELS](https://in.tradingview.com/chart/?symbol=NSE:WHEELS) |

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

**Qualifying: 93**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABDL,NSE:ADANIGREEN,NSE:AEGISLOG,NSE:ARIS,NSE:AUROPHARMA,NSE:AXISCADES,NSE:BALRAMCHIN,NSE:BBOX,NSE:BHEL,NSE:CARTRADE,NSE:CGPOWER,NSE:CHENNPETRO,NSE:CPPLUS,NSE:CUPID,NSE:ENRIN,NSE:GRWRHITECH,NSE:KARURVYSYA,NSE:KIRLOSENG,NSE:KTKBANK,NSE:LALPATHLAB,NSE:LLOYDSENGG,NSE:MAHABANK,NSE:NUVAMA,NSE:NYKAA,NSE:PAYTM,NSE:PNBHOUSING,NSE:PVRINOX,NSE:RADICO,NSE:RAIN,NSE:RAYMONDREL,NSE:RRKABEL,NSE:SGFIN,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ADANIPORTS,NSE:AZAD,NSE:HFCL,NSE:ONEPOINT,NSE:OPTIEMUS,NSE:PTCIL,NSE:REDINGTON,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ACE,NSE:AEROFLEX,NSE:AVTNPL,NSE:CENTUM,NSE:CYIENTDLM,NSE:DIACABS,NSE:EBGNG,NSE:EMIL,NSE:ENGINERSIN,NSE:FINCABLES,NSE:GRAPHITE,NSE:JTLIND,NSE:MANINDS,NSE:MARINE,NSE:MCX,NSE:MOTILALOFS,NSE:NEOGEN,NSE:PAISALO,NSE:QPOWER,NSE:QUADFUTURE,NSE:RAYMOND,NSE:RBLBANK,NSE:SAMBHV,NSE:SBC,NSE:SHANTIGOLD,NSE:SHREEJISPG,NSE:SIGMAADV,NSE:STLTECH,NSE:VENUSPIPES,NSE:WELSPUNLIV,NSE:YATHARTH,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:APARINDS,NSE:AVALON,NSE:DIVISLAB,NSE:FCL,NSE:IOLCP,NSE:MOREPENLAB,NSE:MTARTECH,NSE:RATNAVEER,NSE:ROSSTECH,NSE:SETL,NSE:SSWL,NSE:SYRMA,NSE:TFCILTD,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:GANDHAR,NSE:GLAND,NSE:KMEW,NSE:LAURUSLABS,NSE:MANORAMA,NSE:NAZARA,NSE:SANSERA,NSE:SHILPAMED,NSE:SKYGOLD,NSE:WELCORP
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [ADANIGREEN](https://in.tradingview.com/chart/?symbol=NSE:ADANIGREEN)<br><sub>✓ SAFE . ↗336Cr · 859Cr . ↓CMF3d</sub> | 1342.70 | -16.3% | +73.7% | 1d | SMA-OK | RS-OK | +2.26% |
| [CGPOWER](https://in.tradingview.com/chart/?symbol=NSE:CGPOWER)<br><sub>✓ SAFE . ↘188Cr · 109Cr . ↓CMF5d</sub> | 882.30 | -9.6% | +66.3% | 1d | SMA-OK | RS-OK | +0.38% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . ↗199Cr · 177Cr . ↓CMF1d</sub> | 343.00 | -1.9% | +46.1% | 1d | SMA-OK | RS-OK | +3.22% |
| [RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO)<br><sub>✓ SAFE . →146Cr · 151Cr . ↑CMF3d</sub> | 4550.00 | -3.9% | +79.0% | 1d | SMA-OK | RS-OK | +3.06% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>⚠ CAUTION . →128Cr · 118Cr . ↑CMF30d</sub> | 1693.00 | -2.4% | +56.0% | 1d | SMA-OK | RS-OK | +2.92% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>⚠ CAUTION . ↗72Cr · 99Cr . ↑CMF0d</sub> | 339.90 | -4.1% | +53.7% | 1d | SMA-OK | RS-OK | +3.25% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>✓ SAFE . ↘59Cr · 77Cr . ↓CMF15d</sub> | 2951.00 | -9.7% | +81.8% | 1d | SMA-OK | RS-OK | +3.99% |
| [KIRLOSENG](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSENG)<br><sub>✓ SAFE . ↗226Cr · 66Cr . ↑CMF30d</sub> | 2210.40 | -13.8% | +154.2% | 1d | SMA-OK | RS-OK | +2.19% |
| [SGFIN](https://in.tradingview.com/chart/?symbol=NSE:SGFIN)<br><sub>✓ SAFE . ↗46Cr · 57Cr . ↑CMF6d</sub> | 676.05 | -4.8% | +103.5% | 1d | SMA-OK | RS-OK | +4.67% |
| [RAIN](https://in.tradingview.com/chart/?symbol=NSE:RAIN)<br><sub>✓ SAFE . ↘58Cr · 49Cr . ↑CMF2d</sub> | 215.42 | -11.3% | +112.3% | 1d | SMA-OK | RS-OK | +1.81% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>✓ SAFE . ↘49Cr · 44Cr . ↑CMF0d</sub> | 328.20 | -4.3% | +91.8% | 1d | SMA-OK | RS-OK | +2.31% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>✓ SAFE . →37Cr · 34Cr . ↑CMF12d</sub> | 6997.50 | -5.6% | +158.7% | 1d | SMA-OK | RS-OK | +0.99% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>✓ SAFE . ↘56Cr · 32Cr . ↓CMF4d</sub> | 1933.60 | -3.6% | +47.9% | 1d | SMA-OK | RS-OK | +1.83% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>✓ SAFE . →302Cr · 344Cr . ↑CMF30d</sub> | 427.90 | -3.3% | +85.3% | 2d | SMA-OK | RS-OK | +1.64% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>✓ SAFE . →106Cr · 96Cr . ↓CMF17d</sub> | 1158.00 | -2.3% | +54.2% | 2d | SMA-OK | RS-OK | +0.70% |
| [MAHABANK](https://in.tradingview.com/chart/?symbol=NSE:MAHABANK)<br><sub>✓ SAFE . →109Cr · 90Cr . ↓CMF23d</sub> | 83.16 | -11.4% | +50.9% | 3d | SMA-OK | RS-OK | +1.35% |
| [ENRIN](https://in.tradingview.com/chart/?symbol=NSE:ENRIN)<br><sub>✓ SAFE . ↗178Cr · 141Cr . ↑CMF0d</sub> | 3350.90 | -13.5% | +57.7% | 4d | SMA-OK | RS-OK | +1.31% |
| [ARIS](https://in.tradingview.com/chart/?symbol=NSE:ARIS)<br><sub>✓ SAFE . →24Cr · 41Cr . ↑CMF7d</sub> | 140.31 | -20.1% | +66.7% | 4d | SMA-OK | RS-OK | +2.85% |
| [AXISCADES](https://in.tradingview.com/chart/?symbol=NSE:AXISCADES)<br><sub>✓ SAFE . ↗84Cr · 41Cr . ↑CMF30d</sub> | 2082.30 | -9.8% | +89.1% | 4d | SMA-OK | RS-OK | +0.23% |
| [BBOX](https://in.tradingview.com/chart/?symbol=NSE:BBOX)<br><sub>✓ SAFE . ↗144Cr · 596Cr . ↓CMF0d</sub> | 892.10 | -17.3% | +99.5% | 5d | SMA-OK | RS-OK | +4.15% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↗593Cr · 259Cr . ↑CMF2d</sub> | 1487.70 | -8.5% | +105.6% | 5d | SMA-OK | RS-OK | -2.83% |
| [RRKABEL](https://in.tradingview.com/chart/?symbol=NSE:RRKABEL)<br><sub>✓ SAFE . ↗97Cr · 68Cr . ↑CMF4d</sub> | 2705.60 | -7.6% | +117.2% | 5d | SMA-OK | RS-OK | +0.34% |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>✓ SAFE . →80Cr · 50Cr . ↓CMF6d</sub> | 678.15 | -11.6% | +70.5% | 5d | SMA-OK | RS-OK | -1.64% |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA)<br><sub>✓ SAFE . ↗129Cr · 45Cr . ↑CMF4d</sub> | 1764.40 | -10.9% | +58.9% | 5d | SMA-OK | RS-OK | +1.55% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>✓ SAFE . →111Cr · 83Cr . ↑CMF24d</sub> | 1388.90 | -6.5% | +136.2% | 8d | SMA-OK | RS-OK | +0.48% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . ↗122Cr · 81Cr . ↑CMF17d</sub> | 1327.20 | -1.6% | +44.5% | 8d | SMA-OK | RS-OK | +1.37% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . →1039Cr · 1234Cr . ↑CMF12d</sub> | 366.10 | 0.0% | +683.9% | 9d | SMA-OK | RS-OK | +2.65% |
| [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM)<br><sub>✓ SAFE . ↘566Cr · 864Cr . ↑CMF30d</sub> | 1732.90 | -6.3% | +80.7% | 10d | SMA-OK | RS-OK | +2.30% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . →117Cr · 371Cr . ↓CMF9d</sub> | 4185.20 | 0.0% | +218.5% | 10d | SMA-OK | RS-OK | +5.36% |
| [RAYMONDREL](https://in.tradingview.com/chart/?symbol=NSE:RAYMONDREL)<br><sub>✓ SAFE . ↘88Cr · 109Cr . ↑CMF12d</sub> | 698.20 | -3.4% | +95.4% | 10d | SMA-OK | RS-OK | +2.69% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>✓ SAFE . ↗152Cr · 93Cr . ↑CMF10d</sub> | 94.42 | -7.6% | +150.3% | 10d | SMA-OK | RS-OK | -1.83% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>✓ SAFE . ↘50Cr · 77Cr . ↑CMF30d</sub> | 711.55 | -1.6% | +85.2% | 10d | SMA-OK | RS-OK | +2.61% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>⚠ CAUTION . →361Cr · 468Cr . ↑CMF17d</sub> | 1777.60 | -5.6% | +36.4% | 12d | SMA-OK | RS-OK | +2.29% |
| [REDINGTON](https://in.tradingview.com/chart/?symbol=NSE:REDINGTON)<br><sub>✓ SAFE . ↘132Cr · 110Cr . ↓CMF0d</sub> | 380.00 | -7.9% | +90.0% | 15d | SMA-OK | RS-OK | -2.06% |
| [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT)<br><sub>✓ SAFE . →37Cr · 46Cr . ↑CMF8d</sub> | 80.36 | 0.0% | +94.2% | 15d | SMA-OK | RS-OK | +2.43% |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS)<br><sub>✓ SAFE . ↘154Cr · 42Cr . ↑CMF27d</sub> | 815.85 | -8.3% | +178.7% | 15d | SMA-OK | RS-OK | -0.12% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>✓ SAFE . ↗484Cr · 144Cr . ↓CMF1d</sub> | 2910.20 | -5.0% | +113.0% | 17d | SMA-OK | RS-OK | +0.92% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>✓ SAFE . ↗69Cr · 71Cr . ↑CMF2d</sub> | 24535.00 | -0.6% | +66.6% | 17d | SMA-OK | RS-OK | +0.27% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [MOTILALOFS](https://in.tradingview.com/chart/?symbol=NSE:MOTILALOFS)<br><sub>✓ SAFE . →97Cr · 85Cr . ↑CMF3d</sub> | 1026.00 | -6.0% | +63.3% | 23d | SMA-OK | RS-OK | +1.15% |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE)<br><sub>✓ SAFE . ↘103Cr · 72Cr . ↓CMF0d</sub> | 806.60 | -5.2% | +53.3% | 24d | SMA-OK | RS-OK | +0.55% |
| [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK)<br><sub>✓ SAFE . →126Cr · 158Cr . ↑CMF0d</sub> | 418.00 | -2.3% | +45.8% | 25d | SMA-OK | RS-OK | +4.32% |
| [VENUSPIPES](https://in.tradingview.com/chart/?symbol=NSE:VENUSPIPES)<br><sub>✓ SAFE . ↘38Cr · 56Cr . ↑CMF24d</sub> | 2041.40 | -10.6% | +128.3% | 25d | SMA-OK | RS-OK | -3.70% |
| [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO)<br><sub>✓ SAFE . ↘98Cr · 49Cr . ↑CMF26d</sub> | 80.90 | -13.4% | +161.2% | 25d | SMA-OK | RS-OK | -0.28% |
| [CENTUM](https://in.tradingview.com/chart/?symbol=NSE:CENTUM)<br><sub>✓ SAFE . →46Cr · 27Cr . ↑CMF24d</sub> | 4076.70 | -17.2% | +94.8% | 25d | SMA-OK | RS-OK | -1.58% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . →76Cr · 111Cr . ↑CMF25d</sub> | 811.80 | 0.0% | +263.3% | 30d | SMA-OK | RS-OK | +1.38% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . ↗131Cr · 110Cr . ↑CMF7d</sub> | 62.43 | -1.2% | +177.3% | 30d | SMA-OK | RS-OK | -1.23% |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE)<br><sub>✓ SAFE . ↘32Cr · 38Cr . ↑CMF11d</sub> | 1176.90 | -6.1% | +57.1% | 30d | SMA-OK | RS-OK | -0.25% |
| [YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH)<br><sub>✓ SAFE . ↘37Cr · 29Cr . ↑CMF23d</sub> | 1022.20 | -12.0% | +85.6% | 30d | SMA-OK | RS-OK | +0.79% |
| [QUADFUTURE](https://in.tradingview.com/chart/?symbol=NSE:QUADFUTURE)<br><sub>✓ SAFE . ↘27Cr · 27Cr . ↓CMF0d</sub> | 511.25 | -6.6% | +102.4% | 34d | SMA-OK | RS-OK | +1.09% |
| [AVTNPL](https://in.tradingview.com/chart/?symbol=NSE:AVTNPL)<br><sub>✓ SAFE . ↗12Cr · 97Cr . ↑CMF13d</sub> | 94.78 | -3.5% | +74.7% | 35d | SMA-OK | RS-OK | +10.92% |
| [JTLIND](https://in.tradingview.com/chart/?symbol=NSE:JTLIND)<br><sub>✓ SAFE . ↗28Cr · 35Cr . ↓CMF1d</sub> | 83.98 | -9.1% | +105.8% | 35d | SMA-OK | RS-OK | +0.20% |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN)<br><sub>✓ SAFE . ↘173Cr · 128Cr . ↑CMF30d</sub> | 293.10 | -7.1% | +78.1% | 36d | SMA-OK | RS-OK | +1.42% |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL)<br><sub>✓ SAFE . ↗108Cr · 43Cr . ↑CMF21d</sub> | 191.17 | -9.6% | +123.4% | 36d | SMA-OK | RS-OK | -1.11% |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS)<br><sub>✓ SAFE . ↗363Cr · 101Cr . ↑CMF9d</sub> | 322.85 | -4.3% | +173.7% | 37d | SMA-OK | RS-OK | -0.35% |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . →537Cr · 542Cr . ↓CMF9d</sub> | 3318.20 | -3.6% | +90.9% | 40d | SMA-OK | RS-OK | +1.92% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↘213Cr · 148Cr . ↓CMF0d</sub> | 1186.60 | -8.8% | +268.7% | 40d | SMA-OK | RS-OK | +1.67% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>✓ SAFE . →61Cr · 57Cr . ↑CMF30d</sub> | 520.50 | -9.2% | +227.8% | 40d | SMA-OK | RS-OK | -1.61% |
| [FINCABLES](https://in.tradingview.com/chart/?symbol=NSE:FINCABLES)<br><sub>✓ SAFE . ↘67Cr · 52Cr . ↑CMF22d</sub> | 1388.70 | -6.4% | +95.4% | 40d | SMA-OK | RS-OK | -0.96% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>✓ SAFE . ↘33Cr · 72Cr . ↑CMF0d</sub> | 763.65 | 0.0% | +710.9% | 40d | SMA-OK | RS-OK | +5.00% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>✓ SAFE . ↘57Cr · 42Cr . ↑CMF15d</sub> | 160.41 | -2.7% | +94.9% | 40d | SMA-OK | RS-OK | +1.97% |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER)<br><sub>✓ SAFE . →45Cr · 40Cr . ↑CMF9d</sub> | 1547.40 | -6.1% | +160.0% | 40d | SMA-OK | RS-OK | +0.99% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>✓ SAFE . →47Cr · 36Cr . ↓CMF4d</sub> | 685.50 | -6.3% | +182.6% | 40d | SMA-OK | RS-OK | -0.96% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>✓ SAFE . ↘56Cr · 33Cr . ↑CMF30d</sub> | 867.90 | -14.9% | +179.5% | 40d | SMA-OK | RS-OK | +1.17% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>✓ SAFE . →42Cr · 32Cr . ↑CMF2d</sub> | 952.35 | -3.6% | +249.7% | 40d | SMA-OK | RS-OK | -2.95% |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>✓ SAFE . ↘25Cr · 27Cr . ↑CMF18d</sub> | 2378.20 | -4.4% | +142.7% | 40d | SMA-OK | RS-OK | -0.06% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . →117Cr · 58Cr . ↑CMF20d</sub> | 223.75 | -6.4% | +106.6% | 41d | SMA-OK | RS-OK | -0.59% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>✓ SAFE . ↘165Cr · 399Cr . ↑CMF12d</sub> | 380.55 | 0.0% | +143.0% | 42d | SMA-OK | RS-OK | +8.53% |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE)<br><sub>↘86Cr · 37Cr . ↑CMF30d</sub> | 455.65 | -4.8% | +200.4% | 42d | SMA-OK | RS-OK | +0.67% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . →443Cr · 434Cr . ↓CMF0d</sub> | 9184.00 | -4.6% | +61.4% | 45d | SMA-OK | RS-OK | -0.70% |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH)<br><sub>✓ SAFE . ↘37Cr · 28Cr . ↑CMF18d</sub> | 1574.80 | -2.9% | +174.4% | 45d | SMA-OK | RS-OK | +0.30% |
| [FCL](https://in.tradingview.com/chart/?symbol=NSE:FCL)<br><sub>✓ SAFE . →130Cr · 127Cr . ↑CMF0d</sub> | 57.94 | -4.2% | +201.1% | 47d | SMA-OK | RS-OK | +3.48% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>✓ SAFE . →25Cr · 50Cr . ↓CMF0d</sub> | 387.95 | -17.1% | +267.2% | 47d | SMA-OK | RS-OK | -5.00% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↗253Cr · 230Cr . ↑CMF30d</sub> | 129.55 | -11.9% | +284.6% | 48d | SMA-OK | RS-OK | -5.13% |
| [APARINDS](https://in.tradingview.com/chart/?symbol=NSE:APARINDS)<br><sub>✓ SAFE . →195Cr · 178Cr . ↓CMF0d</sub> | 17984.00 | -5.1% | +158.2% | 50d | SMA-OK | RS-OK | +0.94% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>✓ SAFE . ↘240Cr · 169Cr . ↑CMF26d</sub> | 1719.90 | -3.5% | +168.7% | 50d | SMA-OK | RS-OK | +2.32% |
| [AVALON](https://in.tradingview.com/chart/?symbol=NSE:AVALON)<br><sub>✓ SAFE . ↘101Cr · 43Cr . ↑CMF15d</sub> | 2300.50 | -9.3% | +189.8% | 53d | SMA-OK | RS-OK | -0.07% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . ↘161Cr · 170Cr . ↓CMF2d</sub> | 343.60 | -0.5% | +161.7% | 57d | SMA-OK | RS-OK | +3.70% |
| [MTARTECH](https://in.tradingview.com/chart/?symbol=NSE:MTARTECH)<br><sub>✓ SAFE . ↗2251Cr · 944Cr . ↑CMF8d</sub> | 7777.00 | -7.1% | +457.1% | 58d | SMA-OK | RS-OK | -4.25% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↗63Cr · 25Cr . ↑CMF4d</sub> | 406.80 | -4.2% | +138.7% | 59d | SMA-OK | RS-OK | -0.90% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . ↗224Cr · 407Cr . ↓CMF16d</sub> | 147.05 | -3.4% | +166.2% | 60d | SMA-OK | RS-OK | +0.27% |
| [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP)<br><sub>✓ SAFE . →62Cr · 56Cr . ↑CMF0d</sub> | 201.15 | -8.7% | +194.9% | 63d | SMA-OK | RS-OK | -2.14% |
| [MANORAMA](https://in.tradingview.com/chart/?symbol=NSE:MANORAMA)<br><sub>✓ SAFE . ↗40Cr · 38Cr . ↓CMF3d</sub> | 2043.40 | -4.2% | +89.9% | 65d | SMA-OK | RS-OK | +2.25% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↗141Cr · 55Cr . ↑CMF30d</sub> | 3061.80 | -2.8% | +91.7% | 66d | SMA-OK | RS-OK | -0.56% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . ↗63Cr · 50Cr . ↓CMF2d</sub> | 377.65 | -3.9% | +73.5% | 67d | SMA-OK | RS-OK | +0.44% |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>✓ SAFE . ↘68Cr · 41Cr . ↑CMF26d</sub> | 1021.70 | -4.8% | +282.7% | 75d | SMA-OK | RS-OK | -0.35% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>✓ SAFE . ↗63Cr · 86Cr . ↑CMF9d</sub> | 3207.80 | -1.5% | +191.8% | 85d | SMA-OK | RS-OK | -1.50% |
| [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR)<br><sub>✓ SAFE . ↗24Cr · 38Cr . ↑CMF15d</sub> | 296.55 | -0.9% | +153.9% | 86d | SMA-OK | RS-OK | +0.03% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . →131Cr · 109Cr . ↑CMF30d</sub> | 4124.70 | -11.5% | +194.9% | 100d | SMA-OK | RS-OK | -0.11% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . →329Cr · 281Cr . ↑CMF30d</sub> | 1977.20 | -2.6% | +135.1% | 103d | SMA-OK | RS-OK | -0.14% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>✓ SAFE . ↘423Cr · 201Cr . ↑CMF30d</sub> | 2640.40 | -7.1% | +265.8% | 107d | SMA-OK | RS-OK | -0.41% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . ↗148Cr · 211Cr . ↑CMF1d</sub> | 921.00 | 0.0% | +205.5% | 124d | SMA-OK | RS-OK | +4.13% |

### By Trend Age

**<2 WEEKS** (32)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:ADANIGREEN,NSE:AEGISLOG,NSE:ARIS,NSE:AUROPHARMA,NSE:AXISCADES,NSE:BALRAMCHIN,NSE:BBOX,NSE:BHEL,NSE:CARTRADE,NSE:CGPOWER,NSE:CHENNPETRO,NSE:CPPLUS,NSE:CUPID,NSE:ENRIN,NSE:GRWRHITECH,NSE:KARURVYSYA,NSE:KIRLOSENG,NSE:KTKBANK,NSE:LALPATHLAB,NSE:LLOYDSENGG,NSE:MAHABANK,NSE:NUVAMA,NSE:NYKAA,NSE:PAYTM,NSE:PNBHOUSING,NSE:PVRINOX,NSE:RADICO,NSE:RAIN,NSE:RAYMONDREL,NSE:RRKABEL,NSE:SGFIN
```

**2-4 WEEKS** (7)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ADANIPORTS,NSE:AZAD,NSE:HFCL,NSE:ONEPOINT,NSE:OPTIEMUS,NSE:PTCIL,NSE:REDINGTON
```

**1-2 MONTHS** (31)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ACE,NSE:AEROFLEX,NSE:AVTNPL,NSE:CENTUM,NSE:CYIENTDLM,NSE:DIACABS,NSE:EBGNG,NSE:EMIL,NSE:ENGINERSIN,NSE:FINCABLES,NSE:GRAPHITE,NSE:JTLIND,NSE:MANINDS,NSE:MARINE,NSE:MCX,NSE:MOTILALOFS,NSE:NEOGEN,NSE:PAISALO,NSE:QPOWER,NSE:QUADFUTURE,NSE:RAYMOND,NSE:RBLBANK,NSE:SAMBHV,NSE:SBC,NSE:SHANTIGOLD,NSE:SHREEJISPG,NSE:SIGMAADV,NSE:STLTECH,NSE:VENUSPIPES,NSE:WELSPUNLIV,NSE:YATHARTH
```

**2-3 MONTHS** (13)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:APARINDS,NSE:AVALON,NSE:DIVISLAB,NSE:FCL,NSE:IOLCP,NSE:MOREPENLAB,NSE:MTARTECH,NSE:RATNAVEER,NSE:ROSSTECH,NSE:SETL,NSE:SSWL,NSE:SYRMA,NSE:TFCILTD
```

**3-6 MONTHS** (10)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GANDHAR,NSE:GLAND,NSE:KMEW,NSE:LAURUSLABS,NSE:MANORAMA,NSE:NAZARA,NSE:SANSERA,NSE:SHILPAMED,NSE:SKYGOLD,NSE:WELCORP
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
