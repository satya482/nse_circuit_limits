> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-11-02
*Generated 2026-11-02 15:49 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [AARTIDRUGS](https://in.tradingview.com/chart/?symbol=NSE:AARTIDRUGS) | [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX) |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL) | [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM) |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR) | [BHAGERIA](https://in.tradingview.com/chart/?symbol=NSE:BHAGERIA) |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS) | [BLISSGVS](https://in.tradingview.com/chart/?symbol=NSE:BLISSGVS) |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN) | [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS) |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL) | [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH) |
| [GLENMARK](https://in.tradingview.com/chart/?symbol=NSE:GLENMARK) | [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW) |
| [GREAVESCOT](https://in.tradingview.com/chart/?symbol=NSE:GREAVESCOT) | [KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL) |
| [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN) | [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB) |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB) | [NILKAMAL](https://in.tradingview.com/chart/?symbol=NSE:NILKAMAL) |
| [MENONBE](https://in.tradingview.com/chart/?symbol=NSE:MENONBE) | [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS) |
| [MUFIN](https://in.tradingview.com/chart/?symbol=NSE:MUFIN) | [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA) |
| [NITINSPIN](https://in.tradingview.com/chart/?symbol=NSE:NITINSPIN) | [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL) |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA) | [SGFIN](https://in.tradingview.com/chart/?symbol=NSE:SGFIN) |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON) | [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY) |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA) | [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD) |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL) | [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA) |
| [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC) |  |

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
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AARTIDRUGS,NSE:AARTIPHARM,NSE:ACMESOLAR,NSE:ACUTAAS,NSE:ALIVUS,NSE:ATHERENERG,NSE:AUROPHARMA,NSE:BEML,NSE:CEMPRO,NSE:CPPLUS,NSE:ENGINERSIN,NSE:GABRIEL,NSE:GESHIP,NSE:GLAND,NSE:GLENMARK,NSE:GREAVESCOT,NSE:INDGN,NSE:INDHOTEL,NSE:IPCALAB,NSE:KARURVYSYA,NSE:LUMAXTECH,NSE:MENONBE,NSE:MUFIN,NSE:NAVINFLUOR,NSE:NITINSPIN,NSE:NUVAMA,NSE:NYKAA,NSE:PHOENIXLTD,NSE:PPLPHARMA,NSE:RUBICON,NSE:SAILIFE,NSE:SANSERA,NSE:SGMART,NSE:SMSPHARMA,NSE:SONACOMS,NSE:WELSPUNLIV,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:63MOONS,NSE:CHENNPETRO,NSE:COFORGE,NSE:FEDERALBNK,NSE:HFCL,NSE:KROSS,NSE:SHYAMMETL,NSE:SOUTHBANK,NSE:TIPSMUSIC,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABDL,NSE:CUPID,NSE:PTCIL,NSE:PVRINOX,NSE:STLTECH,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:RAYMOND,NSE:SAMBHV,NSE:SBC,NSE:SHREEJISPG,NSE:THELEELA,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:LAURUSLABS,NSE:RATNAVEER,NSE:SSWL,NSE:TFCILTD
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN)<br><sub>✓ SAFE . ↗173Cr · 1039Cr . ↑CMF0d</sub> | 289.65 | -8.2% | +76.0% | 0d | SMA-OK | RS-OK | +15.01% |
| [GLENMARK](https://in.tradingview.com/chart/?symbol=NSE:GLENMARK)<br><sub>✓ SAFE . ↗147Cr · 369Cr . ↑CMF0d</sub> | 2382.00 | -5.3% | +31.6% | 1d | SMA-OK | RS-OK | +3.62% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . ↘84Cr · 147Cr . ↓CMF9d</sub> | 3849.30 | -13.3% | +192.9% | 1d | SMA-OK | RS-OK | +0.99% |
| [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN)<br><sub>✓ SAFE . ↗35Cr · 120Cr . ↓CMF0d</sub> | 619.40 | 0.0% | +46.3% | 1d | SMA-OK | RS-OK | +5.56% |
| [MENONBE](https://in.tradingview.com/chart/?symbol=NSE:MENONBE)<br><sub>✓ SAFE . ↗29Cr · 113Cr . ↑CMF1d</sub> | 311.10 | -3.2% | +203.1% | 1d | SMA-OK | RS-OK | +12.64% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . →74Cr · 65Cr . ↓CMF1d</sub> | 4157.40 | -10.8% | +174.5% | 1d | SMA-OK | RS-OK | +1.11% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>✓ SAFE . ↗33Cr · 62Cr . ↑CMF6d</sub> | 1667.40 | -10.4% | +173.4% | 1d | SMA-OK | RS-OK | +3.53% |
| [GREAVESCOT](https://in.tradingview.com/chart/?symbol=NSE:GREAVESCOT)<br><sub>✓ SAFE . ↗77Cr · 47Cr . ↑CMF0d</sub> | 206.25 | -21.8% | +71.0% | 1d | SMA-OK | RS-OK | +3.44% |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA)<br><sub>✓ SAFE . ↘47Cr · 47Cr . ↑CMF20d</sub> | 1805.10 | -8.8% | +62.5% | 1d | SMA-OK | RS-OK | +3.98% |
| [MUFIN](https://in.tradingview.com/chart/?symbol=NSE:MUFIN)<br><sub>✓ SAFE . →21Cr · 45Cr . ↑CMF2d</sub> | 136.07 | -4.1% | +42.7% | 1d | SMA-OK | RS-OK | +2.47% |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>⚠ CAUTION . →49Cr · 42Cr . ↓CMF30d</sub> | 1949.90 | -3.0% | +50.6% | 1d | SMA-OK | RS-OK | +1.15% |
| [AARTIDRUGS](https://in.tradingview.com/chart/?symbol=NSE:AARTIDRUGS)<br><sub>✓ SAFE . ↗65Cr · 34Cr . ↑CMF3d</sub> | 453.80 | -12.8% | +41.9% | 1d | SMA-OK | RS-OK | +4.27% |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>✓ SAFE . ↗48Cr · 28Cr . ↓CMF11d</sub> | 418.75 | -8.7% | +110.5% | 1d | SMA-OK | RS-OK | +3.45% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↗244Cr · 1421Cr . ↑CMF0d</sub> | 242.34 | 0.0% | +123.7% | 2d | SMA-OK | RS-OK | +10.62% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>✓ SAFE . ↗484Cr · 894Cr . ↑CMF1d</sub> | 777.00 | -0.7% | +36.1% | 2d | SMA-OK | RS-OK | -0.68% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . ↗174Cr · 301Cr . ↑CMF4d</sub> | 8406.00 | -4.2% | +51.1% | 2d | SMA-OK | RS-OK | -3.16% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>⚠ CAUTION . →123Cr · 124Cr . ↑CMF5d</sub> | 1683.80 | -2.9% | +50.1% | 2d | SMA-OK | RS-OK | +0.14% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . →67Cr · 97Cr . ↑CMF1d</sub> | 1542.30 | -7.9% | +94.0% | 2d | SMA-OK | RS-OK | -0.98% |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML)<br><sub>✓ SAFE . →43Cr · 61Cr . ↑CMF6d</sub> | 2030.90 | -7.1% | +48.3% | 2d | SMA-OK | RS-OK | +2.13% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . ↘143Cr · 266Cr . ↑CMF12d</sub> | 352.90 | 0.0% | +50.4% | 3d | SMA-OK | RS-OK | +3.04% |
| [PHOENIXLTD](https://in.tradingview.com/chart/?symbol=NSE:PHOENIXLTD)<br><sub>⚠ CAUTION . ↘85Cr · 137Cr . ↓CMF24d</sub> | 2016.60 | -6.4% | +36.5% | 3d | SMA-OK | RS-OK | +3.03% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>✓ SAFE . ↗463Cr · 216Cr . ↑CMF3d</sub> | 239.92 | 0.0% | +80.0% | 4d | SMA-OK | RS-OK | +0.42% |
| [ALIVUS](https://in.tradingview.com/chart/?symbol=NSE:ALIVUS)<br><sub>✓ SAFE . ↗38Cr · 90Cr . ↓CMF1d</sub> | 1447.60 | 0.0% | +68.3% | 4d | SMA-OK | RS-OK | +2.28% |
| [NITINSPIN](https://in.tradingview.com/chart/?symbol=NSE:NITINSPIN)<br><sub>✓ SAFE . →10Cr · 42Cr . ↑CMF11d</sub> | 664.30 | 0.0% | +117.6% | 4d | SMA-OK | RS-OK | +2.01% |
| [CEMPRO](https://in.tradingview.com/chart/?symbol=NSE:CEMPRO)<br><sub>✓ SAFE . ↘52Cr · 30Cr . ↓CMF28d</sub> | 1289.60 | -21.3% | +153.0% | 4d | SMA-OK | RS-OK | +1.94% |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH)<br><sub>✓ SAFE . →43Cr · 29Cr . ↑CMF5d</sub> | 2014.40 | -4.8% | +74.4% | 4d | SMA-OK | RS-OK | -0.41% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↗387Cr · 252Cr . ↑CMF5d</sub> | 905.95 | 0.0% | +103.8% | 5d | SMA-OK | RS-OK | +1.73% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>✓ SAFE . ↘126Cr · 110Cr . ↓CMF3d</sub> | 344.50 | -6.9% | +42.9% | 5d | SMA-OK | RS-OK | -3.26% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . →124Cr · 67Cr . ↑CMF30d</sub> | 3066.60 | -2.7% | +92.0% | 5d | SMA-OK | RS-OK | -0.95% |
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP)<br><sub>✓ SAFE . →99Cr · 50Cr . ↑CMF4d</sub> | 1600.40 | -6.9% | +52.5% | 5d | SMA-OK | RS-OK | +0.43% |
| [SMSPHARMA](https://in.tradingview.com/chart/?symbol=NSE:SMSPHARMA)<br><sub>✓ SAFE . ↗41Cr · 42Cr . ↑CMF1d</sub> | 504.15 | -1.4% | +85.7% | 5d | SMA-OK | RS-OK | -1.41% |
| [AARTIPHARM](https://in.tradingview.com/chart/?symbol=NSE:AARTIPHARM)<br><sub>✓ SAFE . ↗68Cr · 41Cr . ↑CMF0d</sub> | 888.80 | -8.8% | +50.1% | 5d | SMA-OK | RS-OK | +1.84% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . ↗793Cr · 578Cr . ↑CMF5d</sub> | 1774.60 | 0.0% | +195.1% | 6d | SMA-OK | RS-OK | +1.06% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>✓ SAFE . ↗536Cr · 180Cr . ↑CMF5d</sub> | 3892.60 | -2.8% | +142.9% | 6d | SMA-OK | RS-OK | -2.77% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>✓ SAFE . ↘25Cr · 28Cr . ↓CMF9d</sub> | 1443.80 | -9.1% | +75.4% | 6d | SMA-OK | RS-OK | +1.32% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>✓ SAFE . ↗117Cr · 55Cr . ↑CMF5d</sub> | 878.90 | 0.0% | +175.2% | 7d | SMA-OK | RS-OK | +2.63% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↘376Cr · 282Cr . ↑CMF18d</sub> | 1546.00 | -4.9% | +97.5% | 11d | SMA-OK | RS-OK | +2.28% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>✓ SAFE . ↘203Cr · 129Cr . ↑CMF10d</sub> | 337.50 | -9.2% | +43.1% | 11d | SMA-OK | RS-OK | -0.65% |
| [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS)<br><sub>✓ SAFE . ↘43Cr · 61Cr . ↑CMF0d</sub> | 961.50 | 0.0% | +104.4% | 11d | SMA-OK | RS-OK | +1.33% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>✓ SAFE . ↗655Cr · 758Cr . ↑CMF4d</sub> | 2099.00 | 0.0% | +95.5% | 12d | SMA-OK | RS-OK | +2.64% |
| [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS)<br><sub>✓ SAFE . →78Cr · 39Cr . ↓CMF0d</sub> | 267.65 | -12.7% | +69.1% | 15d | SMA-OK | RS-OK | -4.55% |
| [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC)<br><sub>✓ SAFE . ↘46Cr · 27Cr . ↑CMF15d</sub> | 784.95 | -1.1% | +62.0% | 16d | SMA-OK | RS-OK | +0.37% |
| [SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK)<br><sub>✓ SAFE . ↘101Cr · 61Cr . ↑CMF28d</sub> | 54.51 | -3.6% | +62.2% | 17d | SMA-OK | RS-OK | -1.77% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL)<br><sub>✓ SAFE . ↘44Cr · 143Cr . ↑CMF14d</sub> | 1191.00 | -2.9% | +56.4% | 20d | SMA-OK | RS-OK | +2.42% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . →139Cr · 99Cr . ↑CMF30d</sub> | 1512.70 | 0.0% | +64.7% | 24d | SMA-OK | RS-OK | +1.18% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↘447Cr · 585Cr . ↑CMF28d</sub> | 340.50 | -7.0% | +606.4% | 25d | SMA-OK | RS-OK | +4.91% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>✓ SAFE . ↘35Cr · 34Cr . ↑CMF2d</sub> | 708.25 | -5.4% | +84.4% | 26d | SMA-OK | RS-OK | +1.43% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>✓ SAFE . ↘52Cr · 36Cr . ↑CMF18d</sub> | 24385.00 | -5.2% | +65.6% | 33d | SMA-OK | RS-OK | +1.84% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . ↘77Cr · 118Cr . ↓CMF3d</sub> | 65.34 | -1.8% | +171.7% | 46d | SMA-OK | RS-OK | -1.22% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . ↗111Cr · 79Cr . ↑CMF30d</sub> | 873.65 | 0.0% | +227.9% | 46d | SMA-OK | RS-OK | +3.60% |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA)<br><sub>✓ SAFE . →51Cr · 158Cr . ↓CMF12d</sub> | 671.05 | 0.0% | +72.2% | 55d | SMA-OK | RS-OK | +5.80% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↘94Cr · 87Cr . ↓CMF3d</sub> | 1125.00 | -13.5% | +249.5% | 56d | SMA-OK | RS-OK | +2.25% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>✓ SAFE . →37Cr · 52Cr . ↑CMF0d</sub> | 165.01 | -4.3% | +100.5% | 56d | SMA-OK | RS-OK | +8.37% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . ↘128Cr · 318Cr . ↑CMF1d</sub> | 379.20 | 0.0% | +188.8% | 73d | SMA-OK | RS-OK | +5.26% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↗348Cr · 82Cr . ↑CMF20d</sub> | 486.95 | -8.5% | +185.7% | 75d | SMA-OK | RS-OK | -1.36% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . →174Cr · 212Cr . ↑CMF4d</sub> | 157.96 | -1.8% | +186.0% | 76d | SMA-OK | RS-OK | +0.03% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . →262Cr · 361Cr . ↓CMF0d</sub> | 1955.00 | -5.5% | +112.3% | 117d | SMA-OK | RS-OK | -2.37% |

### By Trend Age

**<2 WEEKS** (36)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AARTIDRUGS,NSE:AARTIPHARM,NSE:ACMESOLAR,NSE:ACUTAAS,NSE:ALIVUS,NSE:ATHERENERG,NSE:AUROPHARMA,NSE:BEML,NSE:CEMPRO,NSE:CPPLUS,NSE:ENGINERSIN,NSE:GABRIEL,NSE:GESHIP,NSE:GLAND,NSE:GLENMARK,NSE:GREAVESCOT,NSE:INDGN,NSE:INDHOTEL,NSE:IPCALAB,NSE:KARURVYSYA,NSE:LUMAXTECH,NSE:MENONBE,NSE:MUFIN,NSE:NAVINFLUOR,NSE:NITINSPIN,NSE:NUVAMA,NSE:NYKAA,NSE:PHOENIXLTD,NSE:PPLPHARMA,NSE:RUBICON,NSE:SAILIFE,NSE:SANSERA,NSE:SGMART,NSE:SMSPHARMA,NSE:SONACOMS,NSE:WELSPUNLIV
```

**2-4 WEEKS** (9)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:63MOONS,NSE:CHENNPETRO,NSE:COFORGE,NSE:FEDERALBNK,NSE:HFCL,NSE:KROSS,NSE:SHYAMMETL,NSE:SOUTHBANK,NSE:TIPSMUSIC
```

**1-2 MONTHS** (5)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:CUPID,NSE:PTCIL,NSE:PVRINOX,NSE:STLTECH
```

**2-3 MONTHS** (5)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:RAYMOND,NSE:SAMBHV,NSE:SBC,NSE:SHREEJISPG,NSE:THELEELA
```

**3-6 MONTHS** (4)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LAURUSLABS,NSE:RATNAVEER,NSE:SSWL,NSE:TFCILTD
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
