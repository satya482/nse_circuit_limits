> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-10-27
*Generated 2026-10-27 15:46 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [AARTIPHARM](https://in.tradingview.com/chart/?symbol=NSE:AARTIPHARM) | [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS) |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR) | [DELTACORP](https://in.tradingview.com/chart/?symbol=NSE:DELTACORP) |
| [ARIS](https://in.tradingview.com/chart/?symbol=NSE:ARIS) | [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS) |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML) | [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG) |
| [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN) | [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL) |
| [GCSL](https://in.tradingview.com/chart/?symbol=NSE:GCSL) | [SMCGLOBAL](https://in.tradingview.com/chart/?symbol=NSE:SMCGLOBAL) |
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP) | [UTTAMSUGAR](https://in.tradingview.com/chart/?symbol=NSE:UTTAMSUGAR) |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND) | [WESTLIFE](https://in.tradingview.com/chart/?symbol=NSE:WESTLIFE) |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA) | [WSTCSTPAPR](https://in.tradingview.com/chart/?symbol=NSE:WSTCSTPAPR) |
| [MAHLOG](https://in.tradingview.com/chart/?symbol=NSE:MAHLOG) |  |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE) |  |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA) |  |
| [PARACABLES](https://in.tradingview.com/chart/?symbol=NSE:PARACABLES) |  |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL) |  |
| [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA) |  |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV) |  |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS) |  |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH) |  |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV) |  |

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

**Qualifying: 59**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AARTIPHARM,NSE:ACMESOLAR,NSE:ACUTAAS,NSE:ANTELOPUS,NSE:APOLLO,NSE:ARIS,NSE:ATHERENERG,NSE:BEML,NSE:CHENNPETRO,NSE:COFORGE,NSE:CRAFTSMAN,NSE:FEDERALBNK,NSE:GABRIEL,NSE:GESHIP,NSE:GLAND,NSE:GNA,NSE:GRWRHITECH,NSE:INDGN,NSE:INDHOTEL,NSE:IPCALAB,NSE:KARURVYSYA,NSE:MAHLOG,NSE:MARINE,NSE:NYKAA,NSE:PARACABLES,NSE:PRIVISCL,NSE:RBA,NSE:SANSERA,NSE:SGMART,NSE:SONACOMS,NSE:UNIMECH,NSE:WELSPUNLIV,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:CUPID,NSE:HFCL,NSE:KROSS,NSE:PVRINOX,NSE:SOUTHBANK,NSE:TIPSMUSIC,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABDL,NSE:CPPLUS,NSE:GCSL,NSE:OPTIEMUS,NSE:PTCIL,NSE:SBC,NSE:SHREEJISPG,NSE:SIGMAADV,NSE:STLTECH,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:MOREPENLAB,NSE:RAYMOND,NSE:SAMBHV,NSE:SHANTIGOLD,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:GANDHAR,NSE:KMEW,NSE:LAURUSLABS,NSE:NAZARA,NSE:RATNAVEER,NSE:SSWL,NSE:TFCILTD,###6+ MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:SKYGOLD
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [MAHLOG](https://in.tradingview.com/chart/?symbol=NSE:MAHLOG)<br><sub>✓ SAFE . ↗69Cr · 206Cr . ↑CMF0d</sub> | 434.20 | -1.9% | +55.3% | 0d | SMA-OK | RS-OK | +11.29% |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>✓ SAFE . ↗39Cr · 96Cr . ↓CMF7d</sub> | 416.05 | -9.3% | +109.1% | 0d | SMA-OK | RS-OK | +8.87% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↗303Cr · 1625Cr . ↑CMF1d</sub> | 851.85 | 0.0% | +91.7% | 1d | SMA-OK | RS-OK | +8.95% |
| [PARACABLES](https://in.tradingview.com/chart/?symbol=NSE:PARACABLES)<br><sub>✓ SAFE . ↗66Cr · 270Cr . ↑CMF7d</sub> | 65.55 | -11.6% | +129.5% | 1d | SMA-OK | RS-OK | +9.91% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . ↘111Cr · 176Cr . ↑CMF10d</sub> | 339.40 | -2.9% | +44.6% | 1d | SMA-OK | RS-OK | +2.90% |
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP)<br><sub>✓ SAFE . →101Cr · 169Cr . ↑CMF0d</sub> | 1550.90 | -9.8% | +47.8% | 1d | SMA-OK | RS-OK | +1.21% |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML)<br><sub>✓ SAFE . ↗43Cr · 134Cr . ↑CMF2d</sub> | 1998.60 | -9.9% | +45.9% | 1d | SMA-OK | RS-OK | +8.35% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . →104Cr · 118Cr . ↑CMF30d</sub> | 2960.30 | -6.0% | +85.4% | 1d | SMA-OK | RS-OK | +4.09% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>✓ SAFE . ↗230Cr · 88Cr . ↑CMF0d</sub> | 350.60 | -5.3% | +45.4% | 1d | SMA-OK | RS-OK | +3.82% |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE)<br><sub>↘44Cr · 86Cr . ↑CMF30d</sub> | 425.25 | -11.2% | +180.3% | 1d | SMA-OK | RS-OK | +9.57% |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL)<br><sub>✓ SAFE . ↘26Cr · 61Cr . ↑CMF0d</sub> | 3530.50 | -5.9% | +35.0% | 1d | SMA-OK | RS-OK | +5.20% |
| [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN)<br><sub>✓ SAFE . →46Cr · 54Cr . ↑CMF9d</sub> | 11011.00 | -7.1% | +70.8% | 1d | SMA-OK | RS-OK | +2.66% |
| [AARTIPHARM](https://in.tradingview.com/chart/?symbol=NSE:AARTIPHARM)<br><sub>✓ SAFE . ↘37Cr · 49Cr . ↓CMF6d</sub> | 885.90 | -9.1% | +49.7% | 1d | SMA-OK | RS-OK | +7.63% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↘52Cr · 49Cr . ↓CMF7d</sub> | 215.03 | -10.1% | +98.5% | 1d | SMA-OK | RS-OK | +2.90% |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH)<br><sub>✓ SAFE . ↘28Cr · 48Cr . ↑CMF5d</sub> | 1691.50 | -9.7% | +139.5% | 1d | SMA-OK | RS-OK | +4.68% |
| [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA)<br><sub>✓ SAFE . →25Cr · 32Cr . ↑CMF3d</sub> | 95.92 | -9.9% | +67.5% | 1d | SMA-OK | RS-OK | +4.37% |
| [ARIS](https://in.tradingview.com/chart/?symbol=NSE:ARIS)<br><sub>✓ SAFE . ↘17Cr · 30Cr . ↑CMF19d</sub> | 140.91 | -16.9% | +67.4% | 1d | SMA-OK | RS-OK | +4.52% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . →605Cr · 2179Cr . ↑CMF1d</sub> | 1674.00 | -3.0% | +178.4% | 2d | SMA-OK | RS-OK | +6.29% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>✓ SAFE . ↗324Cr · 1800Cr . ↑CMF1d</sub> | 3793.30 | 0.0% | +136.7% | 2d | SMA-OK | RS-OK | +13.27% |
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO)<br><sub>✓ SAFE . ↗648Cr · 1666Cr . ↓CMF4d</sub> | 425.40 | -5.5% | +133.5% | 2d | SMA-OK | RS-OK | +3.53% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>✓ SAFE . ↗484Cr · 894Cr . ↑CMF1d</sub> | 777.00 | -0.7% | +36.1% | 2d | SMA-OK | RS-OK | -0.68% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>✓ SAFE . ↗66Cr · 89Cr . ↑CMF30d</sub> | 1091.20 | -13.5% | +203.5% | 2d | SMA-OK | RS-OK | -8.21% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . →81Cr · 81Cr . ↑CMF1d</sub> | 4290.60 | -8.0% | +191.4% | 2d | SMA-OK | RS-OK | +3.45% |
| [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN)<br><sub>✓ SAFE . →20Cr · 47Cr . ↑CMF0d</sub> | 599.95 | -2.2% | +41.7% | 2d | SMA-OK | RS-OK | -0.30% |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>⚠ CAUTION . →48Cr · 37Cr . ↓CMF30d</sub> | 1980.80 | -1.4% | +55.8% | 2d | SMA-OK | RS-OK | +2.18% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>✓ SAFE . ↗61Cr · 29Cr . ↓CMF5d</sub> | 1449.70 | -8.7% | +76.1% | 2d | SMA-OK | RS-OK | +3.97% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>✓ SAFE . →28Cr · 28Cr . ↑CMF1d</sub> | 579.65 | -6.6% | +94.4% | 2d | SMA-OK | RS-OK | +3.64% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>✓ SAFE . ↗82Cr · 33Cr . ↑CMF24d</sub> | 7160.00 | -3.4% | +164.7% | 3d | SMA-OK | RS-OK | +2.62% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>✓ SAFE . ↗38Cr · 32Cr . ↑CMF1d</sub> | 799.40 | -5.1% | +150.3% | 3d | SMA-OK | RS-OK | -0.04% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↘466Cr · 340Cr . ↑CMF14d</sub> | 1573.80 | -3.2% | +101.1% | 7d | SMA-OK | RS-OK | +3.44% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>✓ SAFE . ↗381Cr · 332Cr . ↑CMF6d</sub> | 341.60 | -8.1% | +45.5% | 7d | SMA-OK | RS-OK | -0.81% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>✓ SAFE . →528Cr · 758Cr . ↑CMF0d</sub> | 1997.00 | -0.9% | +86.0% | 8d | SMA-OK | RS-OK | +0.20% |
| [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS)<br><sub>✓ SAFE . ↗153Cr · 53Cr . ↑CMF2d</sub> | 292.75 | -4.5% | +85.0% | 11d | SMA-OK | RS-OK | +1.40% |
| [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC)<br><sub>✓ SAFE . ↗94Cr · 39Cr . ↑CMF11d</sub> | 741.60 | -3.9% | +53.1% | 12d | SMA-OK | RS-OK | +3.45% |
| [SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK)<br><sub>✓ SAFE . ↗165Cr · 60Cr . ↑CMF24d</sub> | 54.31 | -2.6% | +61.6% | 13d | SMA-OK | RS-OK | +3.06% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . ↘81Cr · 157Cr . ↑CMF29d</sub> | 1464.00 | 0.0% | +59.4% | 20d | SMA-OK | RS-OK | +4.22% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↘471Cr · 401Cr . ↑CMF24d</sub> | 316.60 | -13.5% | +577.9% | 21d | SMA-OK | RS-OK | +0.81% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . →123Cr · 57Cr . ↓CMF5d</sub> | 3968.20 | -10.6% | +202.0% | 22d | SMA-OK | RS-OK | +2.61% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>✓ SAFE . ↘36Cr · 25Cr . ↓CMF3d</sub> | 693.15 | -7.4% | +80.4% | 22d | SMA-OK | RS-OK | +3.29% |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS)<br><sub>✓ SAFE . ↘27Cr · 29Cr . ↑CMF30d</sub> | 734.10 | -17.5% | +150.8% | 27d | SMA-OK | RS-OK | +5.66% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>✓ SAFE . ↘55Cr · 35Cr . ↑CMF14d</sub> | 24055.00 | -6.5% | +63.4% | 29d | SMA-OK | RS-OK | +3.73% |
| [GCSL](https://in.tradingview.com/chart/?symbol=NSE:GCSL)<br><sub>✓ SAFE . →28Cr · 40Cr . ↑CMF30d</sub> | 747.70 | 0.0% | +235.2% | 34d | SMA-OK | RS-OK | +2.01% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>✓ SAFE . ↘33Cr · 72Cr . ↑CMF0d</sub> | 763.65 | 0.0% | +710.9% | 40d | SMA-OK | RS-OK | +5.00% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . ↗99Cr · 105Cr . ↑CMF30d</sub> | 838.95 | -0.1% | +247.8% | 42d | SMA-OK | RS-OK | +3.38% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . ↘84Cr · 97Cr . ↑CMF0d</sub> | 66.17 | 0.0% | +182.2% | 42d | SMA-OK | RS-OK | +3.86% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↗253Cr · 230Cr . ↑CMF30d</sub> | 129.55 | -11.9% | +284.6% | 48d | SMA-OK | RS-OK | -5.13% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↘70Cr · 52Cr . ↑CMF1d</sub> | 1081.20 | -16.9% | +235.9% | 52d | SMA-OK | RS-OK | +2.45% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>✓ SAFE . ↘36Cr · 35Cr . ↑CMF27d</sub> | 168.57 | -2.3% | +104.8% | 52d | SMA-OK | RS-OK | +6.83% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>✓ SAFE . ↘91Cr · 54Cr . ↑CMF24d</sub> | 339.10 | -19.9% | +116.5% | 54d | SMA-OK | RS-OK | +3.51% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . →128Cr · 92Cr . ↓CMF6d</sub> | 347.25 | -0.9% | +164.5% | 69d | SMA-OK | RS-OK | +4.40% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↗362Cr · 390Cr . ↑CMF16d</sub> | 528.90 | -0.6% | +210.3% | 71d | SMA-OK | RS-OK | -0.63% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . →184Cr · 141Cr . ↑CMF0d</sub> | 155.04 | -3.6% | +180.7% | 72d | SMA-OK | RS-OK | +0.47% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . →71Cr · 158Cr . ↑CMF2d</sub> | 401.30 | -4.0% | +84.4% | 79d | SMA-OK | RS-OK | +0.26% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>✓ SAFE . ↘34Cr · 51Cr . ↑CMF21d</sub> | 3230.20 | -3.5% | +178.5% | 97d | SMA-OK | RS-OK | -1.59% |
| [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR)<br><sub>✓ SAFE . →28Cr · 81Cr . ↑CMF27d</sub> | 314.90 | 0.0% | +169.6% | 98d | SMA-OK | RS-OK | +4.88% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . →262Cr · 361Cr . ↓CMF0d</sub> | 1955.00 | -5.5% | +112.3% | 117d | SMA-OK | RS-OK | -2.37% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . →206Cr · 521Cr . ↑CMF13d</sub> | 935.15 | -11.8% | +210.2% | 136d | SMA-OK | RS-OK | -0.36% |

### By Trend Age

**<2 WEEKS** (32)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AARTIPHARM,NSE:ACMESOLAR,NSE:ACUTAAS,NSE:ANTELOPUS,NSE:APOLLO,NSE:ARIS,NSE:ATHERENERG,NSE:BEML,NSE:CHENNPETRO,NSE:COFORGE,NSE:CRAFTSMAN,NSE:FEDERALBNK,NSE:GABRIEL,NSE:GESHIP,NSE:GLAND,NSE:GNA,NSE:GRWRHITECH,NSE:INDGN,NSE:INDHOTEL,NSE:IPCALAB,NSE:KARURVYSYA,NSE:MAHLOG,NSE:MARINE,NSE:NYKAA,NSE:PARACABLES,NSE:PRIVISCL,NSE:RBA,NSE:SANSERA,NSE:SGMART,NSE:SONACOMS,NSE:UNIMECH,NSE:WELSPUNLIV
```

**2-4 WEEKS** (6)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CUPID,NSE:HFCL,NSE:KROSS,NSE:PVRINOX,NSE:SOUTHBANK,NSE:TIPSMUSIC
```

**1-2 MONTHS** (9)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:CPPLUS,NSE:GCSL,NSE:OPTIEMUS,NSE:PTCIL,NSE:SBC,NSE:SHREEJISPG,NSE:SIGMAADV,NSE:STLTECH
```

**2-3 MONTHS** (4)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MOREPENLAB,NSE:RAYMOND,NSE:SAMBHV,NSE:SHANTIGOLD
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
