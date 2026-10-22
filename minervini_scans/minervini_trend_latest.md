> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-10-22
*Generated 2026-10-22 15:46 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN) | [ARFIN](https://in.tradingview.com/chart/?symbol=NSE:ARFIN) |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS) | [CCAVENUE](https://in.tradingview.com/chart/?symbol=NSE:CCAVENUE) |
| [ORIENTHOT](https://in.tradingview.com/chart/?symbol=NSE:ORIENTHOT) | [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX) |
| [TBZ](https://in.tradingview.com/chart/?symbol=NSE:TBZ) | [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL) |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA) | [IIFLCAPS](https://in.tradingview.com/chart/?symbol=NSE:IIFLCAPS) |
|  | [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG) |
|  | [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS) |
|  | [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE) |
|  | [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN) |
|  | [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT) |
|  | [PARACABLES](https://in.tradingview.com/chart/?symbol=NSE:PARACABLES) |
|  | [PREMEXPLN](https://in.tradingview.com/chart/?symbol=NSE:PREMEXPLN) |
|  | [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV) |
|  | [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV) |
|  | [TATVA](https://in.tradingview.com/chart/?symbol=NSE:TATVA) |
|  | [UTTAMSUGAR](https://in.tradingview.com/chart/?symbol=NSE:UTTAMSUGAR) |
|  | [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP) |

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

**Qualifying: 51**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:63MOONS,NSE:ADANIGREEN,NSE:BHEL,NSE:CHENNPETRO,NSE:COFORGE,NSE:CRAFTSMAN,NSE:DELTACORP,NSE:FEDERALBNK,NSE:HAL,NSE:INDGN,NSE:KARURVYSYA,NSE:KROSS,NSE:PAYTM,NSE:SOLARINDS,NSE:SOUTHBANK,NSE:TIPSMUSIC,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABDL,NSE:ADANIPORTS,NSE:AXISCADES,NSE:BBOX,NSE:CPPLUS,NSE:CUPID,NSE:HFCL,NSE:PVRINOX,NSE:SHYAMMETL,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:DIACABS,NSE:GCSL,NSE:OPTIEMUS,NSE:ORIENTHOT,NSE:PAISALO,NSE:PTCIL,NSE:SBC,NSE:SHREEJISPG,NSE:STLTECH,NSE:TBZ,NSE:WHEELS,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:DYNAMATECH,NSE:EBGNG,NSE:MOREPENLAB,NSE:RAYMOND,NSE:SHANTIGOLD,NSE:THELEELA,NSE:WELSPUNLIV,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:KMEW,NSE:LAURUSLABS,NSE:NAZARA,NSE:RATNAVEER,NSE:SSWL,NSE:TFCILTD,NSE:WSTCSTPAPR,###6+ MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:SKYGOLD
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [ADANIGREEN](https://in.tradingview.com/chart/?symbol=NSE:ADANIGREEN)<br><sub>✓ SAFE . ↗421Cr · 123Cr . ↓CMF9d</sub> | 1303.00 | -18.8% | +68.6% | 0d | SMA-OK | RS-OK | -1.17% |
| [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN)<br><sub>✓ SAFE . ↘13Cr · 23Cr . ↓CMF18d</sub> | 588.10 | -4.1% | +38.9% | 1d | SMA-OK | RS-OK | +1.31% |
| [HAL](https://in.tradingview.com/chart/?symbol=NSE:HAL)<br><sub>✓ SAFE . →310Cr · 386Cr . ↓CMF28d</sub> | 4908.00 | -3.7% | +40.7% | 3d | SMA-OK | RS-OK | -0.51% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↘314Cr · 706Cr . ↑CMF11d</sub> | 1453.70 | -10.6% | +94.7% | 4d | SMA-OK | RS-OK | +1.06% |
| [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM)<br><sub>✓ SAFE . ↗877Cr · 454Cr . ↑CMF30d</sub> | 1706.40 | -7.8% | +77.9% | 4d | SMA-OK | RS-OK | -0.35% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>✓ SAFE . ↗338Cr · 277Cr . ↑CMF3d</sub> | 347.80 | -6.4% | +52.9% | 4d | SMA-OK | RS-OK | +1.10% |
| [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN)<br><sub>⚠ CAUTION . →47Cr · 56Cr . ↑CMF6d</sub> | 10998.00 | -7.2% | +70.6% | 4d | SMA-OK | RS-OK | +0.08% |
| [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS)<br><sub>✓ SAFE . ↗66Cr · 30Cr . ↓CMF19d</sub> | 867.25 | -6.9% | +84.4% | 4d | SMA-OK | RS-OK | -0.96% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>✓ SAFE . →413Cr · 671Cr . ↓CMF5d</sub> | 1908.80 | -5.3% | +77.7% | 5d | SMA-OK | RS-OK | -2.16% |
| [SOLARINDS](https://in.tradingview.com/chart/?symbol=NSE:SOLARINDS)<br><sub>✓ SAFE . ↘314Cr · 262Cr . ↓CMF18d</sub> | 19996.00 | -11.0% | +69.9% | 5d | SMA-OK | RS-OK | -0.86% |
| [DELTACORP](https://in.tradingview.com/chart/?symbol=NSE:DELTACORP)<br><sub>✓ SAFE . ↘44Cr · 54Cr . ↓CMF0d</sub> | 76.25 | -10.7% | +54.5% | 5d | SMA-OK | RS-OK | +3.70% |
| [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS)<br><sub>✓ SAFE . ↗124Cr · 201Cr . ↓CMF3d</sub> | 294.55 | -1.0% | +86.1% | 8d | SMA-OK | RS-OK | +5.84% |
| [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC)<br><sub>✓ SAFE . ↗99Cr · 50Cr . ↑CMF8d</sub> | 723.25 | -6.3% | +49.3% | 9d | SMA-OK | RS-OK | -3.31% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>✓ SAFE . ↗724Cr · 1018Cr . ↑CMF30d</sub> | 433.10 | -6.7% | +87.5% | 10d | SMA-OK | RS-OK | -6.66% |
| [SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK)<br><sub>✓ SAFE . ↗158Cr · 144Cr . ↑CMF21d</sub> | 55.75 | 0.0% | +65.9% | 10d | SMA-OK | RS-OK | +1.42% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>✓ SAFE . ↗233Cr · 119Cr . ↑CMF5d</sub> | 356.05 | -3.8% | +47.7% | 10d | SMA-OK | RS-OK | -1.00% |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL)<br><sub>✓ SAFE . ↗58Cr · 44Cr . ↑CMF7d</sub> | 1200.00 | -2.2% | +57.6% | 13d | SMA-OK | RS-OK | +0.37% |
| [AXISCADES](https://in.tradingview.com/chart/?symbol=NSE:AXISCADES)<br><sub>✓ SAFE . ↘28Cr · 30Cr . ↑CMF30d</sub> | 1961.30 | -15.0% | +78.1% | 13d | SMA-OK | RS-OK | -0.48% |
| [BBOX](https://in.tradingview.com/chart/?symbol=NSE:BBOX)<br><sub>✓ SAFE . ↗127Cr · 102Cr . ↓CMF5d</sub> | 885.00 | -17.9% | +97.9% | 14d | SMA-OK | RS-OK | -1.32% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>✓ SAFE . ↗729Cr · 383Cr . ↑CMF22d</sub> | 1746.60 | -7.3% | +34.0% | 17d | SMA-OK | RS-OK | -0.12% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . ↘90Cr · 127Cr . ↑CMF26d</sub> | 1419.90 | 0.0% | +54.6% | 17d | SMA-OK | RS-OK | +0.14% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↘552Cr · 672Cr . ↑CMF21d</sub> | 320.05 | -12.6% | +585.3% | 18d | SMA-OK | RS-OK | -6.07% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . ↗173Cr · 79Cr . ↓CMF2d</sub> | 3904.60 | -12.1% | +197.2% | 19d | SMA-OK | RS-OK | +0.01% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>✓ SAFE . ↘49Cr · 26Cr . ↓CMF0d</sub> | 698.90 | -6.6% | +81.9% | 19d | SMA-OK | RS-OK | +0.59% |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS)<br><sub>✓ SAFE . ↘31Cr · 29Cr . ↑CMF30d</sub> | 724.95 | -18.5% | +147.6% | 24d | SMA-OK | RS-OK | -1.00% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>✓ SAFE . →71Cr · 51Cr . ↑CMF11d</sub> | 24745.00 | -3.8% | +68.0% | 26d | SMA-OK | RS-OK | -1.47% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [TBZ](https://in.tradingview.com/chart/?symbol=NSE:TBZ)<br><sub>✓ SAFE . ↘113Cr · 59Cr . ↑CMF19d</sub> | 665.35 | 0.0% | +496.7% | 29d | SMA-OK | RS-OK | +4.99% |
| [GCSL](https://in.tradingview.com/chart/?symbol=NSE:GCSL)<br><sub>✓ SAFE . →27Cr · 22Cr . ↑CMF30d</sub> | 723.80 | -2.2% | +228.3% | 31d | SMA-OK | RS-OK | +1.74% |
| [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO)<br><sub>✓ SAFE . ↘63Cr · 48Cr . ↓CMF3d</sub> | 79.34 | -15.1% | +156.2% | 34d | SMA-OK | RS-OK | -0.45% |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS)<br><sub>✓ SAFE . ↗363Cr · 101Cr . ↑CMF9d</sub> | 322.85 | -4.3% | +173.7% | 37d | SMA-OK | RS-OK | -0.35% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . →81Cr · 100Cr . ↑CMF30d</sub> | 788.85 | -6.1% | +232.0% | 39d | SMA-OK | RS-OK | +1.22% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . ↘94Cr · 75Cr . ↑CMF2d</sub> | 62.12 | -3.7% | +165.7% | 39d | SMA-OK | RS-OK | -1.30% |
| [ORIENTHOT](https://in.tradingview.com/chart/?symbol=NSE:ORIENTHOT)<br><sub>✓ SAFE . ↗20Cr · 60Cr . ↑CMF7d</sub> | 154.30 | 0.0% | +88.1% | 39d | SMA-OK | RS-OK | +4.70% |
| [WHEELS](https://in.tradingview.com/chart/?symbol=NSE:WHEELS)<br><sub>✓ SAFE . ↘23Cr · 23Cr . ↑CMF6d</sub> | 2108.70 | -14.0% | +195.3% | 41d | SMA-OK | RS-OK | -3.95% |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA)<br><sub>✓ SAFE . ↗52Cr · 55Cr . ↓CMF5d</sub> | 595.65 | -4.4% | +52.9% | 48d | SMA-OK | RS-OK | +1.73% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↗253Cr · 230Cr . ↑CMF30d</sub> | 129.55 | -11.9% | +284.6% | 48d | SMA-OK | RS-OK | -5.13% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>✓ SAFE . →51Cr · 227Cr . ↓CMF4d</sub> | 673.75 | -7.9% | +177.8% | 49d | SMA-OK | RS-OK | +0.50% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↘78Cr · 91Cr . ↓CMF0d . DEL32%(T-1)</sub> | 1085.70 | -16.5% | +237.3% | 49d | SMA-OK | RS-OK | -0.29% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↘51Cr · 52Cr . ↓CMF4d</sub> | 213.94 | -10.5% | +97.5% | 50d | SMA-OK | RS-OK | +0.90% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>✓ SAFE . ↘140Cr · 76Cr . ↑CMF21d</sub> | 394.30 | -6.9% | +151.7% | 51d | SMA-OK | RS-OK | -1.23% |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH)<br><sub>✓ SAFE . ↘25Cr · 30Cr . ↑CMF29d</sub> | 12591.00 | -12.7% | +64.0% | 54d | SMA-OK | RS-OK | -1.53% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . ↘125Cr · 37Cr . ↓CMF3d</sub> | 326.30 | -6.9% | +148.5% | 66d | SMA-OK | RS-OK | -2.63% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↘25Cr · 32Cr . ↑CMF13d . DEL57%(T-1)</sub> | 390.65 | -8.0% | +129.2% | 68d | SMA-OK | RS-OK | -0.24% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . →194Cr · 211Cr . ↓CMF25d</sub> | 150.67 | -6.3% | +172.8% | 69d | SMA-OK | RS-OK | +0.31% |
| [WSTCSTPAPR](https://in.tradingview.com/chart/?symbol=NSE:WSTCSTPAPR)<br><sub>✓ SAFE . ↗157Cr · 145Cr . ↑CMF30d</sub> | 824.65 | -12.3% | +116.3% | 74d | SMA-OK | RS-OK | +6.41% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . →62Cr · 71Cr . ↓CMF0d</sub> | 387.95 | -7.2% | +78.2% | 76d | SMA-OK | RS-OK | -2.75% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>✓ SAFE . ↘36Cr · 37Cr . ↑CMF18d</sub> | 3129.10 | -6.5% | +184.0% | 94d | SMA-OK | RS-OK | +0.29% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . →281Cr · 165Cr . ↑CMF1d</sub> | 2020.00 | -2.4% | +131.4% | 112d | SMA-OK | RS-OK | -0.83% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . ↗197Cr · 111Cr . ↑CMF10d</sub> | 1043.05 | -1.7% | +246.0% | 133d | SMA-OK | RS-OK | -0.24% |

### By Trend Age

**<2 WEEKS** (16)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:63MOONS,NSE:ADANIGREEN,NSE:BHEL,NSE:CHENNPETRO,NSE:COFORGE,NSE:CRAFTSMAN,NSE:DELTACORP,NSE:FEDERALBNK,NSE:HAL,NSE:INDGN,NSE:KARURVYSYA,NSE:KROSS,NSE:PAYTM,NSE:SOLARINDS,NSE:SOUTHBANK,NSE:TIPSMUSIC
```

**2-4 WEEKS** (9)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:ADANIPORTS,NSE:AXISCADES,NSE:BBOX,NSE:CPPLUS,NSE:CUPID,NSE:HFCL,NSE:PVRINOX,NSE:SHYAMMETL
```

**1-2 MONTHS** (11)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:DIACABS,NSE:GCSL,NSE:OPTIEMUS,NSE:ORIENTHOT,NSE:PAISALO,NSE:PTCIL,NSE:SBC,NSE:SHREEJISPG,NSE:STLTECH,NSE:TBZ,NSE:WHEELS
```

**2-3 MONTHS** (7)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:DYNAMATECH,NSE:EBGNG,NSE:MOREPENLAB,NSE:RAYMOND,NSE:SHANTIGOLD,NSE:THELEELA,NSE:WELSPUNLIV
```

**3-6 MONTHS** (7)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:KMEW,NSE:LAURUSLABS,NSE:NAZARA,NSE:RATNAVEER,NSE:SSWL,NSE:TFCILTD,NSE:WSTCSTPAPR
```

**6+ MONTHS** (1)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SKYGOLD
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
