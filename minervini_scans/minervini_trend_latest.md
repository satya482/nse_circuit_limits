> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-10-29
*Generated 2026-10-29 15:57 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX) | [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS) |
| [BLISSGVS](https://in.tradingview.com/chart/?symbol=NSE:BLISSGVS) | [AXISCADES](https://in.tradingview.com/chart/?symbol=NSE:AXISCADES) |
| [CNL](https://in.tradingview.com/chart/?symbol=NSE:CNL) | [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN) |
| [DELTACORP](https://in.tradingview.com/chart/?symbol=NSE:DELTACORP) | [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL) |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS) | [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN) |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG) | [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB) |
| [GRINDWELL](https://in.tradingview.com/chart/?symbol=NSE:GRINDWELL) | [MAHLOG](https://in.tradingview.com/chart/?symbol=NSE:MAHLOG) |
| [NILKAMAL](https://in.tradingview.com/chart/?symbol=NSE:NILKAMAL) | [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB) |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS) | [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR) |
| [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO) | [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL) |
| [PHOENIXLTD](https://in.tradingview.com/chart/?symbol=NSE:PHOENIXLTD) | [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV) |
| [RPGLIFE](https://in.tradingview.com/chart/?symbol=NSE:RPGLIFE) |  |
| [SATIN](https://in.tradingview.com/chart/?symbol=NSE:SATIN) |  |
| [SGFIN](https://in.tradingview.com/chart/?symbol=NSE:SGFIN) |  |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL) |  |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD) |  |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA) |  |
| [UTTAMSUGAR](https://in.tradingview.com/chart/?symbol=NSE:UTTAMSUGAR) |  |
| [WHEELS](https://in.tradingview.com/chart/?symbol=NSE:WHEELS) |  |
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

**Qualifying: 71**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:63MOONS,NSE:AARTIDRUGS,NSE:AARTIPHARM,NSE:ACUTAAS,NSE:AEROFLEX,NSE:ALIVUS,NSE:APOLLO,NSE:ATHERENERG,NSE:CEMPRO,NSE:CHENNPETRO,NSE:CNL,NSE:COFORGE,NSE:DELTACORP,NSE:FEDERALBNK,NSE:GESHIP,NSE:GLAND,NSE:GRINDWELL,NSE:INDHOTEL,NSE:INDSWFTLAB,NSE:KARURVYSYA,NSE:LUMAXTECH,NSE:NILKAMAL,NSE:NUVAMA,NSE:NYKAA,NSE:PAISALO,NSE:PARACABLES,NSE:PHOENIXLTD,NSE:PPLPHARMA,NSE:RPGLIFE,NSE:SANSERA,NSE:SAREGAMA,NSE:SATIN,NSE:SETL,NSE:SGFIN,NSE:SGMART,NSE:SKYGOLD,NSE:SMSPHARMA,NSE:SONACOMS,NSE:SYRMA,NSE:UNIMECH,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:HFCL,NSE:KROSS,NSE:SHYAMMETL,NSE:SOUTHBANK,NSE:TIPSMUSIC,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABDL,NSE:CPPLUS,NSE:CUPID,NSE:DIACABS,NSE:OPTIEMUS,NSE:PTCIL,NSE:PVRINOX,NSE:SIGMAADV,NSE:STLTECH,NSE:UTTAMSUGAR,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:EBGNG,NSE:RAYMOND,NSE:SAMBHV,NSE:SBC,NSE:SHANTIGOLD,NSE:SHREEJISPG,NSE:THELEELA,NSE:WHEELS,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:BLISSGVS,NSE:KMEW,NSE:LAURUSLABS,NSE:NAZARA,NSE:RATNAVEER,NSE:SSWL,NSE:TFCILTD,NSE:WSTCSTPAPR
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>✓ SAFE . ↗308Cr · 1936Cr . ↓CMF11d</sub> | 538.35 | -6.1% | +239.0% | 0d | SMA-OK | RS-OK | +9.37% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>✓ SAFE . ↗213Cr · 491Cr . ↑CMF0d</sub> | 1669.00 | -6.4% | +160.7% | 0d | SMA-OK | RS-OK | +6.78% |
| [NILKAMAL](https://in.tradingview.com/chart/?symbol=NSE:NILKAMAL)<br><sub>✓ SAFE . ↗15Cr · 118Cr . ↑CMF0d</sub> | 2003.90 | -5.3% | +87.9% | 0d | SMA-OK | RS-OK | +13.63% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>✓ SAFE . →27Cr · 50Cr . ↑CMF0d</sub> | 405.35 | -13.4% | +283.7% | 0d | SMA-OK | RS-OK | +4.84% |
| [AARTIDRUGS](https://in.tradingview.com/chart/?symbol=NSE:AARTIDRUGS)<br><sub>✓ SAFE . ↗61Cr · 43Cr . ↑CMF1d</sub> | 449.00 | -13.7% | +40.4% | 0d | SMA-OK | RS-OK | +0.25% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . ↗239Cr · 164Cr . ↑CMF15d</sub> | 876.45 | -17.4% | +190.7% | 1d | SMA-OK | RS-OK | +2.11% |
| [SGFIN](https://in.tradingview.com/chart/?symbol=NSE:SGFIN)<br><sub>✓ SAFE . →60Cr · 158Cr . ↑CMF20d</sub> | 734.95 | 0.0% | +121.2% | 1d | SMA-OK | RS-OK | +12.83% |
| [PHOENIXLTD](https://in.tradingview.com/chart/?symbol=NSE:PHOENIXLTD)<br><sub>⚠ CAUTION . ↘76Cr · 64Cr . ↓CMF22d</sub> | 1969.90 | -8.5% | +33.3% | 1d | SMA-OK | RS-OK | +3.72% |
| [GRINDWELL](https://in.tradingview.com/chart/?symbol=NSE:GRINDWELL)<br><sub>⚠ CAUTION . →9Cr · 50Cr . ↑CMF0d</sub> | 1955.20 | -17.9% | +44.5% | 1d | SMA-OK | RS-OK | +5.62% |
| [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO)<br><sub>✓ SAFE . ↘56Cr · 47Cr . ↑CMF3d</sub> | 79.40 | -15.0% | +156.4% | 1d | SMA-OK | RS-OK | +0.54% |
| [CNL](https://in.tradingview.com/chart/?symbol=NSE:CNL)<br><sub>✓ SAFE . ↗5Cr · 29Cr . ↑CMF0d</sub> | 1202.40 | -6.0% | +127.7% | 1d | SMA-OK | RS-OK | +11.15% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>✓ SAFE . ↗371Cr · 608Cr . ↑CMF1d</sub> | 230.78 | -0.9% | +73.2% | 2d | SMA-OK | RS-OK | -0.87% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>✓ SAFE . ↗484Cr · 894Cr . ↑CMF1d</sub> | 777.00 | -0.7% | +36.1% | 2d | SMA-OK | RS-OK | -0.68% |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB)<br><sub>✓ SAFE . ↗31Cr · 145Cr . ↑CMF0d</sub> | 409.80 | -0.8% | +364.9% | 2d | SMA-OK | RS-OK | +8.14% |
| [CEMPRO](https://in.tradingview.com/chart/?symbol=NSE:CEMPRO)<br><sub>✓ SAFE . →58Cr · 97Cr . ↓CMF26d</sub> | 1287.40 | -21.5% | +152.6% | 2d | SMA-OK | RS-OK | +4.65% |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH)<br><sub>✓ SAFE . ↗43Cr · 79Cr . ↑CMF3d</sub> | 2058.50 | -2.7% | +82.5% | 2d | SMA-OK | RS-OK | +0.75% |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA)<br><sub>✓ SAFE . ↘43Cr · 44Cr . ↑CMF18d</sub> | 1783.90 | -9.9% | +60.6% | 2d | SMA-OK | RS-OK | +2.25% |
| [ALIVUS](https://in.tradingview.com/chart/?symbol=NSE:ALIVUS)<br><sub>⚠ CAUTION . ↗14Cr · 37Cr . ↑CMF19d</sub> | 1397.40 | -3.2% | +62.5% | 2d | SMA-OK | RS-OK | -0.14% |
| [AARTIPHARM](https://in.tradingview.com/chart/?symbol=NSE:AARTIPHARM)<br><sub>✓ SAFE . ↗68Cr · 323Cr . ↓CMF8d</sub> | 927.65 | -4.9% | +56.7% | 3d | SMA-OK | RS-OK | +5.18% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . ↘143Cr · 266Cr . ↑CMF12d</sub> | 352.90 | 0.0% | +50.4% | 3d | SMA-OK | RS-OK | +3.04% |
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP)<br><sub>✓ SAFE . →106Cr · 216Cr . ↑CMF2d</sub> | 1618.80 | -5.9% | +54.2% | 3d | SMA-OK | RS-OK | +3.78% |
| [SATIN](https://in.tradingview.com/chart/?symbol=NSE:SATIN)<br><sub>✓ SAFE . →24Cr · 205Cr . ↑CMF17d</sub> | 251.18 | -6.6% | +83.0% | 3d | SMA-OK | RS-OK | +10.12% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↗344Cr · 203Cr . ↑CMF3d</sub> | 873.60 | -0.7% | +96.6% | 3d | SMA-OK | RS-OK | -0.67% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . →118Cr · 119Cr . ↑CMF30d</sub> | 3074.50 | -2.4% | +92.5% | 3d | SMA-OK | RS-OK | +0.84% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>✓ SAFE . ↗220Cr · 80Cr . ↓CMF1d</sub> | 354.50 | -4.2% | +47.0% | 3d | SMA-OK | RS-OK | +1.23% |
| [RPGLIFE](https://in.tradingview.com/chart/?symbol=NSE:RPGLIFE)<br><sub>✓ SAFE . ↗8Cr · 41Cr . ↑CMF26d</sub> | 3003.80 | -2.8% | +72.2% | 3d | SMA-OK | RS-OK | +5.62% |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH)<br><sub>✓ SAFE . ↗41Cr · 41Cr . ↑CMF7d</sub> | 1658.00 | -11.5% | +134.7% | 3d | SMA-OK | RS-OK | +1.21% |
| [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA)<br><sub>✓ SAFE . ↗20Cr · 32Cr . ↑CMF16d</sub> | 536.00 | -3.8% | +72.3% | 3d | SMA-OK | RS-OK | +2.30% |
| [PARACABLES](https://in.tradingview.com/chart/?symbol=NSE:PARACABLES)<br><sub>✓ SAFE . ↗72Cr · 29Cr . ↑CMF9d</sub> | 66.03 | -10.9% | +131.2% | 3d | SMA-OK | RS-OK | +3.58% |
| [SMSPHARMA](https://in.tradingview.com/chart/?symbol=NSE:SMSPHARMA)<br><sub>✓ SAFE . →19Cr · 26Cr . ↓CMF8d</sub> | 485.80 | 0.0% | +78.9% | 3d | SMA-OK | RS-OK | +2.18% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>✓ SAFE . ↗525Cr · 1168Cr . ↑CMF3d</sub> | 3976.70 | 0.0% | +148.2% | 4d | SMA-OK | RS-OK | +7.19% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . ↗613Cr · 280Cr . ↑CMF3d</sub> | 1663.00 | -3.6% | +176.5% | 4d | SMA-OK | RS-OK | +0.79% |
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO)<br><sub>✓ SAFE . ↗646Cr · 245Cr . ↓CMF6d</sub> | 421.55 | -6.3% | +131.4% | 4d | SMA-OK | RS-OK | +1.60% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . →74Cr · 31Cr . ↑CMF0d</sub> | 4270.30 | -8.4% | +182.4% | 4d | SMA-OK | RS-OK | -0.92% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>✓ SAFE . ↗117Cr · 643Cr . ↑CMF3d</sub> | 864.55 | 0.0% | +170.7% | 5d | SMA-OK | RS-OK | +7.67% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↘377Cr · 170Cr . ↑CMF16d</sub> | 1511.80 | -7.0% | +93.2% | 9d | SMA-OK | RS-OK | -0.63% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>✓ SAFE . ↗388Cr · 168Cr . ↑CMF8d</sub> | 347.75 | -6.4% | +48.1% | 9d | SMA-OK | RS-OK | +0.51% |
| [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS)<br><sub>✓ SAFE . ↘39Cr · 53Cr . ↓CMF0d</sub> | 936.30 | 0.0% | +99.1% | 9d | SMA-OK | RS-OK | +0.41% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>✓ SAFE . →488Cr · 307Cr . ↑CMF2d</sub> | 1962.00 | -2.6% | +82.7% | 10d | SMA-OK | RS-OK | +0.01% |
| [DELTACORP](https://in.tradingview.com/chart/?symbol=NSE:DELTACORP)<br><sub>✓ SAFE . ↘31Cr · 36Cr . ↑CMF1d</sub> | 75.88 | -11.2% | +53.8% | 10d | SMA-OK | RS-OK | +7.68% |
| [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS)<br><sub>✓ SAFE . ↗133Cr · 59Cr . ↑CMF4d</sub> | 300.85 | -1.9% | +90.1% | 13d | SMA-OK | RS-OK | +2.09% |
| [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC)<br><sub>✓ SAFE . ↗100Cr · 74Cr . ↑CMF13d</sub> | 791.35 | -0.3% | +63.4% | 14d | SMA-OK | RS-OK | -0.32% |
| [SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK)<br><sub>✓ SAFE . ↗143Cr · 144Cr . ↑CMF26d</sub> | 56.57 | 0.0% | +68.4% | 15d | SMA-OK | RS-OK | +3.53% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL)<br><sub>✓ SAFE . →46Cr · 26Cr . ↑CMF12d</sub> | 1141.60 | -6.9% | +49.9% | 18d | SMA-OK | RS-OK | -0.27% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . →135Cr · 248Cr . ↑CMF30d</sub> | 1490.30 | 0.0% | +62.2% | 22d | SMA-OK | RS-OK | +3.11% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↘467Cr · 291Cr . ↑CMF26d</sub> | 320.15 | -12.6% | +585.5% | 23d | SMA-OK | RS-OK | +1.78% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . ↘84Cr · 103Cr . ↓CMF7d</sub> | 3951.70 | -11.0% | +200.7% | 24d | SMA-OK | RS-OK | -0.69% |
| [UTTAMSUGAR](https://in.tradingview.com/chart/?symbol=NSE:UTTAMSUGAR)<br><sub>✓ SAFE . ↘20Cr · 28Cr . ↑CMF24d</sub> | 360.70 | -7.2% | +92.5% | 24d | SMA-OK | RS-OK | +14.24% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>✓ SAFE . ↘33Cr · 28Cr . ↑CMF0d</sub> | 710.20 | -5.1% | +84.9% | 24d | SMA-OK | RS-OK | +1.14% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS)<br><sub>✓ SAFE . ↘35Cr · 80Cr . ↑CMF30d</sub> | 821.70 | -7.7% | +180.7% | 29d | SMA-OK | RS-OK | +11.70% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>✓ SAFE . ↘53Cr · 59Cr . ↑CMF16d</sub> | 24700.00 | -3.9% | +67.7% | 31d | SMA-OK | RS-OK | +2.90% |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS)<br><sub>✓ SAFE . ↗363Cr · 101Cr . ↑CMF9d</sub> | 322.85 | -4.3% | +173.7% | 37d | SMA-OK | RS-OK | -0.35% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>✓ SAFE . ↘33Cr · 72Cr . ↑CMF0d</sub> | 763.65 | 0.0% | +710.9% | 40d | SMA-OK | RS-OK | +5.00% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . ↘76Cr · 84Cr . ↓CMF1d</sub> | 66.52 | 0.0% | +179.4% | 44d | SMA-OK | RS-OK | +1.59% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . ↗104Cr · 28Cr . ↑CMF30d</sub> | 832.60 | -0.9% | +233.1% | 44d | SMA-OK | RS-OK | -0.92% |
| [WHEELS](https://in.tradingview.com/chart/?symbol=NSE:WHEELS)<br><sub>✓ SAFE . ↗32Cr · 109Cr . ↓CMF0d</sub> | 2196.80 | -10.4% | +207.7% | 46d | SMA-OK | RS-OK | -2.61% |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA)<br><sub>✓ SAFE . →41Cr · 88Cr . ↓CMF10d . DEL76%(T-1)</sub> | 639.90 | 0.0% | +64.2% | 53d | SMA-OK | RS-OK | +5.73% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↘90Cr · 124Cr . ↓CMF1d</sub> | 1101.90 | -15.3% | +242.4% | 54d | SMA-OK | RS-OK | +3.94% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>✓ SAFE . →42Cr · 99Cr . ↓CMF0d</sub> | 159.33 | -7.6% | +93.6% | 54d | SMA-OK | RS-OK | -3.69% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>✓ SAFE . ↗53Cr · 39Cr . ↓CMF9d</sub> | 690.10 | -5.6% | +184.5% | 54d | SMA-OK | RS-OK | -4.58% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>✓ SAFE . ↘89Cr · 52Cr . ↑CMF26d</sub> | 331.85 | -21.6% | +111.9% | 56d | SMA-OK | RS-OK | +3.33% |
| [BLISSGVS](https://in.tradingview.com/chart/?symbol=NSE:BLISSGVS)<br><sub>✓ SAFE . →52Cr · 21Cr . ↑CMF30d</sub> | 527.10 | -2.7% | +312.1% | 68d | SMA-OK | RS-OK | +0.68% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . ↘105Cr · 64Cr . ↓CMF0d</sub> | 352.85 | 0.0% | +168.7% | 71d | SMA-OK | RS-OK | +2.25% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↗368Cr · 66Cr . ↑CMF18d</sub> | 525.80 | -1.2% | +208.5% | 73d | SMA-OK | RS-OK | -0.15% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . →170Cr · 216Cr . ↑CMF2d</sub> | 159.66 | -0.7% | +189.0% | 74d | SMA-OK | RS-OK | +1.73% |
| [WSTCSTPAPR](https://in.tradingview.com/chart/?symbol=NSE:WSTCSTPAPR)<br><sub>✓ SAFE . ↘57Cr · 61Cr . ↑CMF30d</sub> | 839.85 | -10.7% | +120.3% | 79d | SMA-OK | RS-OK | +2.92% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . →72Cr · 83Cr . ↑CMF4d</sub> | 405.40 | -3.0% | +86.3% | 81d | SMA-OK | RS-OK | +1.35% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>✓ SAFE . ↘33Cr · 27Cr . ↑CMF23d</sub> | 3089.20 | -7.7% | +159.5% | 99d | SMA-OK | RS-OK | -2.43% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . →262Cr · 361Cr . ↓CMF0d</sub> | 1955.00 | -5.5% | +112.3% | 117d | SMA-OK | RS-OK | -2.37% |

### By Trend Age

**<2 WEEKS** (40)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:63MOONS,NSE:AARTIDRUGS,NSE:AARTIPHARM,NSE:ACUTAAS,NSE:AEROFLEX,NSE:ALIVUS,NSE:APOLLO,NSE:ATHERENERG,NSE:CEMPRO,NSE:CHENNPETRO,NSE:CNL,NSE:COFORGE,NSE:DELTACORP,NSE:FEDERALBNK,NSE:GESHIP,NSE:GLAND,NSE:GRINDWELL,NSE:INDHOTEL,NSE:INDSWFTLAB,NSE:KARURVYSYA,NSE:LUMAXTECH,NSE:NILKAMAL,NSE:NUVAMA,NSE:NYKAA,NSE:PAISALO,NSE:PARACABLES,NSE:PHOENIXLTD,NSE:PPLPHARMA,NSE:RPGLIFE,NSE:SANSERA,NSE:SAREGAMA,NSE:SATIN,NSE:SETL,NSE:SGFIN,NSE:SGMART,NSE:SKYGOLD,NSE:SMSPHARMA,NSE:SONACOMS,NSE:SYRMA,NSE:UNIMECH
```

**2-4 WEEKS** (5)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:HFCL,NSE:KROSS,NSE:SHYAMMETL,NSE:SOUTHBANK,NSE:TIPSMUSIC
```

**1-2 MONTHS** (10)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:CPPLUS,NSE:CUPID,NSE:DIACABS,NSE:OPTIEMUS,NSE:PTCIL,NSE:PVRINOX,NSE:SIGMAADV,NSE:STLTECH,NSE:UTTAMSUGAR
```

**2-3 MONTHS** (8)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:EBGNG,NSE:RAYMOND,NSE:SAMBHV,NSE:SBC,NSE:SHANTIGOLD,NSE:SHREEJISPG,NSE:THELEELA,NSE:WHEELS
```

**3-6 MONTHS** (8)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:BLISSGVS,NSE:KMEW,NSE:LAURUSLABS,NSE:NAZARA,NSE:RATNAVEER,NSE:SSWL,NSE:TFCILTD,NSE:WSTCSTPAPR
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
