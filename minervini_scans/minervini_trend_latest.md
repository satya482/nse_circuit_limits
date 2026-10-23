> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-10-23
*Generated 2026-10-23 15:47 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS) | [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS) |
| [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR) | [BBOX](https://in.tradingview.com/chart/?symbol=NSE:BBOX) |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH) | [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN) |
| [IIFLCAPS](https://in.tradingview.com/chart/?symbol=NSE:IIFLCAPS) | [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH) |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB) | [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN) |
| [KOLTEPATIL](https://in.tradingview.com/chart/?symbol=NSE:KOLTEPATIL) | [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA) |
| [PREMEXPLN](https://in.tradingview.com/chart/?symbol=NSE:PREMEXPLN) | [ORIENTHOT](https://in.tradingview.com/chart/?symbol=NSE:ORIENTHOT) |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH) | [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO) |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV) | [TBZ](https://in.tradingview.com/chart/?symbol=NSE:TBZ) |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART) | [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA) |
|  | [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC) |
|  | [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV) |
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

**Qualifying: 48**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ADANIGREEN,NSE:ANTELOPUS,NSE:BHEL,NSE:CHENNPETRO,NSE:COFORGE,NSE:DELTACORP,NSE:FEDERALBNK,NSE:GRWRHITECH,NSE:HAL,NSE:IIFLCAPS,NSE:IPCALAB,NSE:KOLTEPATIL,NSE:KROSS,NSE:PAYTM,NSE:SGMART,NSE:SOLARINDS,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABDL,NSE:ADANIPORTS,NSE:AXISCADES,NSE:CPPLUS,NSE:CUPID,NSE:HFCL,NSE:PVRINOX,NSE:SHYAMMETL,NSE:SOUTHBANK,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:DIACABS,NSE:GCSL,NSE:OPTIEMUS,NSE:PREMEXPLN,NSE:PTCIL,NSE:SBC,NSE:SHREEJISPG,NSE:STLTECH,NSE:WHEELS,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:EBGNG,NSE:MOREPENLAB,NSE:RAYMOND,NSE:ROSSTECH,NSE:SAMBHV,NSE:SHANTIGOLD,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:GANDHAR,NSE:KMEW,NSE:LAURUSLABS,NSE:NAZARA,NSE:RATNAVEER,NSE:SSWL,NSE:TFCILTD,###6+ MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:SKYGOLD
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>✓ SAFE . →53Cr · 362Cr . ↑CMF30d</sub> | 1136.40 | -9.9% | +216.1% | 0d | SMA-OK | RS-OK | +13.00% |
| [ADANIGREEN](https://in.tradingview.com/chart/?symbol=NSE:ADANIGREEN)<br><sub>✓ SAFE . ↗421Cr · 123Cr . ↓CMF9d</sub> | 1303.00 | -18.8% | +68.6% | 0d | SMA-OK | RS-OK | -1.17% |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>⚠ CAUTION . →47Cr · 62Cr . ↓CMF29d</sub> | 1953.30 | -2.8% | +54.0% | 0d | SMA-OK | RS-OK | +2.62% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>✓ SAFE . ↗76Cr · 173Cr . ↑CMF22d</sub> | 7034.00 | -5.1% | +160.1% | 1d | SMA-OK | RS-OK | +5.62% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>✓ SAFE . ↗28Cr · 62Cr . ↓CMF30d</sub> | 796.80 | -5.4% | +149.5% | 1d | SMA-OK | RS-OK | +5.30% |
| [KOLTEPATIL](https://in.tradingview.com/chart/?symbol=NSE:KOLTEPATIL)<br><sub>✓ SAFE . ↘9Cr · 41Cr . ↓CMF10d</sub> | 458.30 | -11.3% | +54.9% | 1d | SMA-OK | RS-OK | +6.24% |
| [HAL](https://in.tradingview.com/chart/?symbol=NSE:HAL)<br><sub>✓ SAFE . →310Cr · 386Cr . ↓CMF28d</sub> | 4908.00 | -3.7% | +40.7% | 3d | SMA-OK | RS-OK | -0.51% |
| [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM)<br><sub>✓ SAFE . ↗877Cr · 454Cr . ↑CMF30d</sub> | 1706.40 | -7.8% | +77.9% | 4d | SMA-OK | RS-OK | -0.35% |
| [IIFLCAPS](https://in.tradingview.com/chart/?symbol=NSE:IIFLCAPS)<br><sub>✓ SAFE . →16Cr · 32Cr . ↓CMF5d</sub> | 342.10 | -13.5% | +40.1% | 4d | SMA-OK | RS-OK | -0.71% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↘388Cr · 946Cr . ↑CMF12d</sub> | 1475.60 | -9.3% | +91.7% | 5d | SMA-OK | RS-OK | +1.51% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>✓ SAFE . ↗350Cr · 365Cr . ↑CMF4d</sub> | 340.90 | -8.3% | +49.9% | 5d | SMA-OK | RS-OK | -1.98% |
| [SOLARINDS](https://in.tradingview.com/chart/?symbol=NSE:SOLARINDS)<br><sub>✓ SAFE . ↘314Cr · 262Cr . ↓CMF18d</sub> | 19996.00 | -11.0% | +69.9% | 5d | SMA-OK | RS-OK | -0.86% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>✓ SAFE . →435Cr · 673Cr . ↓CMF6d</sub> | 1900.50 | -5.7% | +77.0% | 6d | SMA-OK | RS-OK | -0.43% |
| [DELTACORP](https://in.tradingview.com/chart/?symbol=NSE:DELTACORP)<br><sub>✓ SAFE . ↘37Cr · 33Cr . ↓CMF1d</sub> | 73.01 | -14.5% | +48.0% | 6d | SMA-OK | RS-OK | -4.25% |
| [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS)<br><sub>✓ SAFE . ↗151Cr · 259Cr . ↑CMF0d</sub> | 306.55 | 0.0% | +93.7% | 9d | SMA-OK | RS-OK | +4.07% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>✓ SAFE . ↗724Cr · 1018Cr . ↑CMF30d</sub> | 433.10 | -6.7% | +87.5% | 10d | SMA-OK | RS-OK | -6.66% |
| [SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK)<br><sub>✓ SAFE . ↗157Cr · 145Cr . ↑CMF22d</sub> | 52.57 | -5.7% | +56.5% | 11d | SMA-OK | RS-OK | -5.70% |
| [AXISCADES](https://in.tradingview.com/chart/?symbol=NSE:AXISCADES)<br><sub>✓ SAFE . ↘28Cr · 38Cr . ↑CMF30d</sub> | 1917.40 | -16.9% | +74.1% | 14d | SMA-OK | RS-OK | -2.24% |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL)<br><sub>✓ SAFE . ↗56Cr · 32Cr . ↑CMF8d</sub> | 1131.30 | -7.8% | +48.6% | 14d | SMA-OK | RS-OK | -5.73% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>✓ SAFE . ↗729Cr · 383Cr . ↑CMF22d</sub> | 1746.60 | -7.3% | +34.0% | 17d | SMA-OK | RS-OK | -0.12% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . ↘85Cr · 56Cr . ↑CMF27d</sub> | 1395.70 | -1.7% | +51.9% | 18d | SMA-OK | RS-OK | -1.70% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↘484Cr · 590Cr . ↑CMF22d</sub> | 306.45 | -16.3% | +556.2% | 19d | SMA-OK | RS-OK | -4.25% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . ↗145Cr · 103Cr . ↓CMF3d</sub> | 3798.00 | -14.5% | +189.0% | 20d | SMA-OK | RS-OK | -2.73% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>✓ SAFE . →46Cr · 65Cr . ↓CMF1d</sub> | 672.65 | -10.2% | +75.1% | 20d | SMA-OK | RS-OK | -3.76% |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS)<br><sub>✓ SAFE . ↘28Cr · 32Cr . ↑CMF30d</sub> | 673.70 | -24.3% | +130.1% | 25d | SMA-OK | RS-OK | -7.07% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>✓ SAFE . →68Cr · 82Cr . ↑CMF12d</sub> | 23455.00 | -8.8% | +59.3% | 27d | SMA-OK | RS-OK | -5.21% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [PREMEXPLN](https://in.tradingview.com/chart/?symbol=NSE:PREMEXPLN)<br><sub>✓ SAFE . ↗20Cr · 45Cr . ↑CMF12d</sub> | 687.40 | -15.0% | +80.2% | 30d | SMA-OK | RS-OK | -0.74% |
| [GCSL](https://in.tradingview.com/chart/?symbol=NSE:GCSL)<br><sub>✓ SAFE . ↗28Cr · 40Cr . ↑CMF30d</sub> | 726.20 | -1.9% | +225.6% | 32d | SMA-OK | RS-OK | +0.33% |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS)<br><sub>✓ SAFE . ↗363Cr · 101Cr . ↑CMF9d</sub> | 322.85 | -4.3% | +173.7% | 37d | SMA-OK | RS-OK | -0.35% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . →80Cr · 104Cr . ↑CMF30d</sub> | 776.60 | -7.5% | +226.8% | 40d | SMA-OK | RS-OK | -1.55% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . ↘89Cr · 78Cr . ↓CMF0d</sub> | 61.05 | -5.3% | +161.1% | 40d | SMA-OK | RS-OK | -1.72% |
| [WHEELS](https://in.tradingview.com/chart/?symbol=NSE:WHEELS)<br><sub>✓ SAFE . →27Cr · 48Cr . ↑CMF7d</sub> | 2157.80 | -12.0% | +202.2% | 42d | SMA-OK | RS-OK | +2.33% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↗253Cr · 230Cr . ↑CMF30d</sub> | 129.55 | -11.9% | +284.6% | 48d | SMA-OK | RS-OK | -5.13% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↘72Cr · 82Cr . ↓CMF1d</sub> | 1063.40 | -18.2% | +230.4% | 50d | SMA-OK | RS-OK | -2.05% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>✓ SAFE . ↘38Cr · 42Cr . ↑CMF25d</sub> | 157.23 | -8.8% | +91.0% | 50d | SMA-OK | RS-OK | -1.77% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>✓ SAFE . →53Cr · 41Cr . ↓CMF5d</sub> | 682.50 | -6.7% | +181.4% | 50d | SMA-OK | RS-OK | +1.30% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>✓ SAFE . ↘106Cr · 131Cr . ↑CMF22d</sub> | 368.50 | -12.9% | +135.3% | 52d | SMA-OK | RS-OK | -6.54% |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH)<br><sub>✓ SAFE . ↘19Cr · 50Cr . ↑CMF28d</sub> | 1402.60 | -13.5% | +144.4% | 55d | SMA-OK | RS-OK | +3.23% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . →134Cr · 232Cr . ↓CMF4d</sub> | 330.70 | -5.6% | +151.9% | 67d | SMA-OK | RS-OK | +1.35% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↗120Cr · 933Cr . ↑CMF14d</sub> | 468.75 | 0.0% | +175.0% | 69d | SMA-OK | RS-OK | +19.99% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . ↘164Cr · 145Cr . ↓CMF26d</sub> | 147.57 | -8.2% | +167.1% | 70d | SMA-OK | RS-OK | -2.06% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . →72Cr · 133Cr . ↑CMF0d</sub> | 402.15 | -3.8% | +84.8% | 77d | SMA-OK | RS-OK | +3.66% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>✓ SAFE . ↘33Cr · 46Cr . ↑CMF19d</sub> | 3149.70 | -5.9% | +177.2% | 95d | SMA-OK | RS-OK | +0.66% |
| [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR)<br><sub>✓ SAFE . →22Cr · 36Cr . ↑CMF25d</sub> | 293.00 | -5.8% | +150.9% | 96d | SMA-OK | RS-OK | -0.68% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . →281Cr · 165Cr . ↑CMF1d</sub> | 2020.00 | -2.4% | +131.4% | 112d | SMA-OK | RS-OK | -0.83% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . →194Cr · 200Cr . ↑CMF11d</sub> | 1046.85 | -1.3% | +247.2% | 134d | SMA-OK | RS-OK | +0.36% |

### By Trend Age

**<2 WEEKS** (16)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ADANIGREEN,NSE:ANTELOPUS,NSE:BHEL,NSE:CHENNPETRO,NSE:COFORGE,NSE:DELTACORP,NSE:FEDERALBNK,NSE:GRWRHITECH,NSE:HAL,NSE:IIFLCAPS,NSE:IPCALAB,NSE:KOLTEPATIL,NSE:KROSS,NSE:PAYTM,NSE:SGMART,NSE:SOLARINDS
```

**2-4 WEEKS** (9)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:ADANIPORTS,NSE:AXISCADES,NSE:CPPLUS,NSE:CUPID,NSE:HFCL,NSE:PVRINOX,NSE:SHYAMMETL,NSE:SOUTHBANK
```

**1-2 MONTHS** (9)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:DIACABS,NSE:GCSL,NSE:OPTIEMUS,NSE:PREMEXPLN,NSE:PTCIL,NSE:SBC,NSE:SHREEJISPG,NSE:STLTECH,NSE:WHEELS
```

**2-3 MONTHS** (6)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:EBGNG,NSE:MOREPENLAB,NSE:RAYMOND,NSE:ROSSTECH,NSE:SAMBHV,NSE:SHANTIGOLD
```

**3-6 MONTHS** (7)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GANDHAR,NSE:KMEW,NSE:LAURUSLABS,NSE:NAZARA,NSE:RATNAVEER,NSE:SSWL,NSE:TFCILTD
```

**6+ MONTHS** (1)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SKYGOLD
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
