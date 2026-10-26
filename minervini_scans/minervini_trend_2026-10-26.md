> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-10-26
*Generated 2026-10-26 15:45 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS) | [ADANIGREEN](https://in.tradingview.com/chart/?symbol=NSE:ADANIGREEN) |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS) | [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS) |
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO) | [AXISCADES](https://in.tradingview.com/chart/?symbol=NSE:AXISCADES) |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG) | [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL) |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL) | [GCSL](https://in.tradingview.com/chart/?symbol=NSE:GCSL) |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA) | [HAL](https://in.tradingview.com/chart/?symbol=NSE:HAL) |
| [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN) | [IIFLCAPS](https://in.tradingview.com/chart/?symbol=NSE:IIFLCAPS) |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL) | [KOLTEPATIL](https://in.tradingview.com/chart/?symbol=NSE:KOLTEPATIL) |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA) | [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM) |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV) | [PREMEXPLN](https://in.tradingview.com/chart/?symbol=NSE:PREMEXPLN) |
| [SMCGLOBAL](https://in.tradingview.com/chart/?symbol=NSE:SMCGLOBAL) | [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH) |
| [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC) | [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV) |
| [UTTAMSUGAR](https://in.tradingview.com/chart/?symbol=NSE:UTTAMSUGAR) | [SOLARINDS](https://in.tradingview.com/chart/?symbol=NSE:SOLARINDS) |
| [WESTLIFE](https://in.tradingview.com/chart/?symbol=NSE:WESTLIFE) | [WHEELS](https://in.tradingview.com/chart/?symbol=NSE:WHEELS) |
| [WSTCSTPAPR](https://in.tradingview.com/chart/?symbol=NSE:WSTCSTPAPR) |  |

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

**Qualifying: 49**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:63MOONS,NSE:ACUTAAS,NSE:ANTELOPUS,NSE:APOLLO,NSE:ATHERENERG,NSE:CHENNPETRO,NSE:COFORGE,NSE:DELTACORP,NSE:FEDERALBNK,NSE:GABRIEL,NSE:GNA,NSE:GRWRHITECH,NSE:INDGN,NSE:INDHOTEL,NSE:IPCALAB,NSE:KROSS,NSE:SANSERA,NSE:SGMART,NSE:SMCGLOBAL,NSE:WESTLIFE,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABDL,NSE:CPPLUS,NSE:CUPID,NSE:HFCL,NSE:PVRINOX,NSE:SHYAMMETL,NSE:SOUTHBANK,NSE:TIPSMUSIC,NSE:UTTAMSUGAR,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:DIACABS,NSE:OPTIEMUS,NSE:PTCIL,NSE:SBC,NSE:SHREEJISPG,NSE:SIGMAADV,NSE:STLTECH,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:EBGNG,NSE:MOREPENLAB,NSE:RAYMOND,NSE:SHANTIGOLD,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:GANDHAR,NSE:KMEW,NSE:LAURUSLABS,NSE:NAZARA,NSE:RATNAVEER,NSE:SSWL,NSE:TFCILTD,NSE:WSTCSTPAPR,###6+ MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:SKYGOLD
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO)<br><sub>✓ SAFE . ↗487Cr · 2161Cr . ↓CMF3d</sub> | 410.90 | -8.7% | +125.6% | 1d | SMA-OK | RS-OK | +9.65% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . ↘399Cr · 1437Cr . ↑CMF0d</sub> | 1575.00 | -8.7% | +161.9% | 1d | SMA-OK | RS-OK | +14.13% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>✓ SAFE . →136Cr · 417Cr . ↑CMF0d</sub> | 3348.80 | -9.4% | +109.0% | 1d | SMA-OK | RS-OK | +6.73% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>✓ SAFE . ↗65Cr · 125Cr . ↑CMF30d</sub> | 1188.80 | -5.8% | +230.7% | 1d | SMA-OK | RS-OK | +4.61% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↘74Cr · 109Cr . ↑CMF0d</sub> | 4147.70 | -11.0% | +181.7% | 1d | SMA-OK | RS-OK | +4.27% |
| [WESTLIFE](https://in.tradingview.com/chart/?symbol=NSE:WESTLIFE)<br><sub>✓ SAFE . ↗64Cr · 89Cr . ↓CMF3d</sub> | 587.60 | -2.2% | +41.0% | 1d | SMA-OK | RS-OK | +3.47% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>✓ SAFE . →26Cr · 77Cr . ↑CMF0d</sub> | 559.30 | -9.9% | +87.6% | 1d | SMA-OK | RS-OK | +8.06% |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>⚠ CAUTION . ↗50Cr · 64Cr . ↓CMF30d</sub> | 1938.60 | -3.5% | +52.5% | 1d | SMA-OK | RS-OK | -0.75% |
| [SMCGLOBAL](https://in.tradingview.com/chart/?symbol=NSE:SMCGLOBAL)<br><sub>✓ SAFE . ↘36Cr · 40Cr . ↑CMF15d</sub> | 94.26 | -19.7% | +69.6% | 1d | SMA-OK | RS-OK | -1.42% |
| [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN)<br><sub>✓ SAFE . ↘17Cr · 32Cr . ↓CMF20d</sub> | 601.75 | -1.9% | +42.1% | 1d | SMA-OK | RS-OK | +5.22% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>✓ SAFE . ↗58Cr · 24Cr . ↓CMF4d</sub> | 1394.30 | -12.2% | +69.4% | 1d | SMA-OK | RS-OK | +1.72% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>✓ SAFE . ↗484Cr · 894Cr . ↑CMF1d</sub> | 777.00 | -0.7% | +36.1% | 2d | SMA-OK | RS-OK | -0.68% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>✓ SAFE . ↗37Cr · 112Cr . ↑CMF0d</sub> | 799.70 | -5.1% | +150.4% | 2d | SMA-OK | RS-OK | +0.36% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>✓ SAFE . ↗80Cr · 85Cr . ↑CMF23d</sub> | 6977.00 | -5.8% | +158.0% | 2d | SMA-OK | RS-OK | -0.81% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↘440Cr · 603Cr . ↑CMF13d</sub> | 1521.40 | -6.5% | +97.6% | 6d | SMA-OK | RS-OK | +3.10% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>✓ SAFE . ↗360Cr · 243Cr . ↑CMF5d</sub> | 344.40 | -7.3% | +47.2% | 6d | SMA-OK | RS-OK | +1.03% |
| [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS)<br><sub>✓ SAFE . ↗58Cr · 76Cr . ↓CMF21d</sub> | 906.50 | -2.7% | +92.7% | 6d | SMA-OK | RS-OK | +5.41% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>✓ SAFE . ↗527Cr · 961Cr . ↓CMF7d</sub> | 1993.00 | -1.1% | +85.6% | 7d | SMA-OK | RS-OK | +4.87% |
| [DELTACORP](https://in.tradingview.com/chart/?symbol=NSE:DELTACORP)<br><sub>✓ SAFE . ↘34Cr · 24Cr . ↓CMF2d</sub> | 73.29 | -14.2% | +48.5% | 7d | SMA-OK | RS-OK | +0.38% |
| [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS)<br><sub>✓ SAFE . ↗147Cr · 51Cr . ↑CMF1d</sub> | 288.70 | -5.8% | +82.4% | 10d | SMA-OK | RS-OK | -5.82% |
| [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC)<br><sub>✓ SAFE . ↗92Cr · 24Cr . ↑CMF10d</sub> | 716.90 | -7.1% | +48.0% | 11d | SMA-OK | RS-OK | -0.02% |
| [SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK)<br><sub>✓ SAFE . ↗160Cr · 95Cr . ↑CMF23d</sub> | 52.70 | -5.5% | +56.8% | 12d | SMA-OK | RS-OK | +0.25% |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL)<br><sub>✓ SAFE . ↗55Cr · 27Cr . ↑CMF9d</sub> | 1126.20 | -8.2% | +47.9% | 15d | SMA-OK | RS-OK | -0.45% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . ↘75Cr · 56Cr . ↑CMF28d</sub> | 1404.70 | -1.1% | +52.9% | 19d | SMA-OK | RS-OK | +0.64% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↘483Cr · 477Cr . ↑CMF23d</sub> | 314.05 | -14.2% | +572.5% | 20d | SMA-OK | RS-OK | +2.48% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . →132Cr · 95Cr . ↓CMF4d</sub> | 3867.40 | -12.9% | +194.3% | 21d | SMA-OK | RS-OK | +1.83% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>✓ SAFE . →43Cr · 24Cr . ↓CMF2d</sub> | 671.05 | -10.4% | +74.7% | 21d | SMA-OK | RS-OK | -0.24% |
| [UTTAMSUGAR](https://in.tradingview.com/chart/?symbol=NSE:UTTAMSUGAR)<br><sub>✓ SAFE . ↗36Cr · 24Cr . ↑CMF21d</sub> | 309.20 | -20.5% | +65.0% | 21d | SMA-OK | RS-OK | -12.26% |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS)<br><sub>✓ SAFE . ↘29Cr · 31Cr . ↑CMF30d</sub> | 694.80 | -21.9% | +137.3% | 26d | SMA-OK | RS-OK | +3.13% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>✓ SAFE . ↘59Cr · 40Cr . ↑CMF13d</sub> | 23190.00 | -9.8% | +57.5% | 28d | SMA-OK | RS-OK | -1.13% |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS)<br><sub>✓ SAFE . ↗363Cr · 101Cr . ↑CMF9d</sub> | 322.85 | -4.3% | +173.7% | 37d | SMA-OK | RS-OK | -0.35% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>✓ SAFE . ↘33Cr · 72Cr . ↑CMF0d</sub> | 763.65 | 0.0% | +710.9% | 40d | SMA-OK | RS-OK | +5.00% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . ↗92Cr · 129Cr . ↑CMF30d</sub> | 811.50 | -3.4% | +237.7% | 41d | SMA-OK | RS-OK | +4.49% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . ↘84Cr · 66Cr . ↓CMF1d</sub> | 63.71 | -1.2% | +171.7% | 41d | SMA-OK | RS-OK | +4.36% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↗253Cr · 230Cr . ↑CMF30d</sub> | 129.55 | -11.9% | +284.6% | 48d | SMA-OK | RS-OK | -5.13% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↘72Cr · 75Cr . ↑CMF0d</sub> | 1055.30 | -18.9% | +227.9% | 51d | SMA-OK | RS-OK | -0.76% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>✓ SAFE . ↗59Cr · 68Cr . ↓CMF6d</sub> | 708.60 | -3.1% | +192.1% | 51d | SMA-OK | RS-OK | +3.82% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>✓ SAFE . ↘91Cr · 126Cr . ↑CMF23d</sub> | 327.60 | -22.6% | +109.2% | 53d | SMA-OK | RS-OK | -11.10% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . →128Cr · 70Cr . ↓CMF5d</sub> | 332.60 | -5.1% | +153.3% | 68d | SMA-OK | RS-OK | +0.57% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↗329Cr · 1949Cr . ↑CMF15d</sub> | 532.25 | 0.0% | +212.3% | 70d | SMA-OK | RS-OK | +13.55% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . →190Cr · 274Cr . ↓CMF27d</sub> | 154.31 | -4.0% | +179.3% | 71d | SMA-OK | RS-OK | +4.57% |
| [WSTCSTPAPR](https://in.tradingview.com/chart/?symbol=NSE:WSTCSTPAPR)<br><sub>✓ SAFE . ↗117Cr · 24Cr . ↑CMF30d</sub> | 787.80 | -16.2% | +106.6% | 76d | SMA-OK | RS-OK | -1.21% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . ↘61Cr · 71Cr . ↑CMF1d</sub> | 400.25 | -4.3% | +83.9% | 78d | SMA-OK | RS-OK | -0.47% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>✓ SAFE . ↘33Cr · 35Cr . ↑CMF20d</sub> | 3282.50 | -1.9% | +183.0% | 96d | SMA-OK | RS-OK | +4.22% |
| [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR)<br><sub>✓ SAFE . ↘21Cr · 36Cr . ↑CMF26d</sub> | 300.25 | -3.4% | +157.1% | 97d | SMA-OK | RS-OK | +2.47% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . →262Cr · 361Cr . ↓CMF0d</sub> | 1955.00 | -5.5% | +112.3% | 117d | SMA-OK | RS-OK | -2.37% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . →174Cr · 297Cr . ↑CMF12d</sub> | 938.50 | -11.5% | +211.3% | 135d | SMA-OK | RS-OK | -10.35% |

### By Trend Age

**<2 WEEKS** (20)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:63MOONS,NSE:ACUTAAS,NSE:ANTELOPUS,NSE:APOLLO,NSE:ATHERENERG,NSE:CHENNPETRO,NSE:COFORGE,NSE:DELTACORP,NSE:FEDERALBNK,NSE:GABRIEL,NSE:GNA,NSE:GRWRHITECH,NSE:INDGN,NSE:INDHOTEL,NSE:IPCALAB,NSE:KROSS,NSE:SANSERA,NSE:SGMART,NSE:SMCGLOBAL,NSE:WESTLIFE
```

**2-4 WEEKS** (9)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:CPPLUS,NSE:CUPID,NSE:HFCL,NSE:PVRINOX,NSE:SHYAMMETL,NSE:SOUTHBANK,NSE:TIPSMUSIC,NSE:UTTAMSUGAR
```

**1-2 MONTHS** (7)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:DIACABS,NSE:OPTIEMUS,NSE:PTCIL,NSE:SBC,NSE:SHREEJISPG,NSE:SIGMAADV,NSE:STLTECH
```

**2-3 MONTHS** (4)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:EBGNG,NSE:MOREPENLAB,NSE:RAYMOND,NSE:SHANTIGOLD
```

**3-6 MONTHS** (8)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GANDHAR,NSE:KMEW,NSE:LAURUSLABS,NSE:NAZARA,NSE:RATNAVEER,NSE:SSWL,NSE:TFCILTD,NSE:WSTCSTPAPR
```

**6+ MONTHS** (1)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SKYGOLD
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
