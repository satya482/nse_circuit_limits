> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-10-28
*Generated 2026-10-28 15:46 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS) | [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR) |
| [AARTIDRUGS](https://in.tradingview.com/chart/?symbol=NSE:AARTIDRUGS) | [ARIS](https://in.tradingview.com/chart/?symbol=NSE:ARIS) |
| [ALIVUS](https://in.tradingview.com/chart/?symbol=NSE:ALIVUS) | [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML) |
| [AXISCADES](https://in.tradingview.com/chart/?symbol=NSE:AXISCADES) | [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR) |
| [CEMPRO](https://in.tradingview.com/chart/?symbol=NSE:CEMPRO) | [GCSL](https://in.tradingview.com/chart/?symbol=NSE:GCSL) |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB) | [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA) |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB) | [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH) |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH) | [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB) |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR) | [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE) |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA) | [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS) |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA) | [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA) |
| [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA) | [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD) |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL) |  |
| [SMSPHARMA](https://in.tradingview.com/chart/?symbol=NSE:SMSPHARMA) |  |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA) |  |

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

**Qualifying: 62**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:63MOONS,NSE:AARTIDRUGS,NSE:AARTIPHARM,NSE:ACUTAAS,NSE:ALIVUS,NSE:ANTELOPUS,NSE:APOLLO,NSE:ATHERENERG,NSE:CEMPRO,NSE:CHENNPETRO,NSE:COFORGE,NSE:CRAFTSMAN,NSE:FEDERALBNK,NSE:GABRIEL,NSE:GESHIP,NSE:GLAND,NSE:INDGN,NSE:INDHOTEL,NSE:INDSWFTLAB,NSE:KARURVYSYA,NSE:LALPATHLAB,NSE:LUMAXTECH,NSE:MAHLOG,NSE:NAVINFLUOR,NSE:NUVAMA,NSE:NYKAA,NSE:PARACABLES,NSE:PPLPHARMA,NSE:PRIVISCL,NSE:SANSERA,NSE:SAREGAMA,NSE:SETL,NSE:SGMART,NSE:SMSPHARMA,NSE:SONACOMS,NSE:UNIMECH,NSE:WELSPUNLIV,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AXISCADES,NSE:HFCL,NSE:KROSS,NSE:PVRINOX,NSE:SOUTHBANK,NSE:TIPSMUSIC,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABDL,NSE:CPPLUS,NSE:CUPID,NSE:PTCIL,NSE:SIGMAADV,NSE:STLTECH,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:MOREPENLAB,NSE:RAYMOND,NSE:SAMBHV,NSE:SBC,NSE:SHANTIGOLD,NSE:SHREEJISPG,NSE:THELEELA,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:KMEW,NSE:LAURUSLABS,NSE:NAZARA,NSE:RATNAVEER,NSE:SSWL,NSE:TFCILTD
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [AARTIDRUGS](https://in.tradingview.com/chart/?symbol=NSE:AARTIDRUGS)<br><sub>✓ SAFE . ↗57Cr · 518Cr . ↑CMF0d</sub> | 447.90 | -13.9% | +40.1% | 0d | SMA-OK | RS-OK | +11.35% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>✓ SAFE . →25Cr · 58Cr . ↓CMF13d . DEL100%(T-1)</sub> | 386.65 | -17.4% | +266.0% | 0d | SMA-OK | RS-OK | +4.95% |
| [MAHLOG](https://in.tradingview.com/chart/?symbol=NSE:MAHLOG)<br><sub>✓ SAFE . ↗70Cr · 29Cr . ↑CMF1d</sub> | 431.35 | -2.6% | +54.3% | 0d | SMA-OK | RS-OK | -0.66% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>✓ SAFE . ↗319Cr · 2749Cr . ↑CMF0d</sub> | 232.80 | 0.0% | +74.7% | 1d | SMA-OK | RS-OK | +17.15% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . ↗119Cr · 283Cr . ↑CMF1d</sub> | 8501.00 | -3.1% | +70.8% | 1d | SMA-OK | RS-OK | +2.99% |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH)<br><sub>✓ SAFE . →37Cr · 113Cr . ↑CMF2d</sub> | 2043.10 | -3.5% | +81.2% | 1d | SMA-OK | RS-OK | +6.95% |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA)<br><sub>✓ SAFE . ↘40Cr · 48Cr . ↑CMF17d</sub> | 1744.70 | -11.9% | +57.1% | 1d | SMA-OK | RS-OK | +3.19% |
| [CEMPRO](https://in.tradingview.com/chart/?symbol=NSE:CEMPRO)<br><sub>✓ SAFE . ↗71Cr · 27Cr . ↓CMF25d</sub> | 1230.20 | -25.0% | +141.4% | 1d | SMA-OK | RS-OK | +2.19% |
| [ALIVUS](https://in.tradingview.com/chart/?symbol=NSE:ALIVUS)<br><sub>⚠ CAUTION . →11Cr · 26Cr . ↑CMF18d</sub> | 1399.40 | -3.1% | +62.7% | 1d | SMA-OK | RS-OK | +4.15% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>✓ SAFE . →44Cr · 24Cr . ↑CMF10d</sub> | 1922.30 | -4.1% | +47.0% | 1d | SMA-OK | RS-OK | +1.08% |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB)<br><sub>✓ SAFE . →16Cr · 22Cr . ↓CMF10d</sub> | 378.95 | -8.3% | +329.9% | 1d | SMA-OK | RS-OK | +2.75% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↗339Cr · 550Cr . ↑CMF2d</sub> | 879.45 | 0.0% | +97.9% | 2d | SMA-OK | RS-OK | +3.24% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>✓ SAFE . ↗484Cr · 894Cr . ↑CMF1d</sub> | 777.00 | -0.7% | +36.1% | 2d | SMA-OK | RS-OK | -0.68% |
| [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN)<br><sub>✓ SAFE . ↗62Cr · 220Cr . ↑CMF10d</sub> | 11014.00 | -7.1% | +70.2% | 2d | SMA-OK | RS-OK | +0.03% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . ↘119Cr · 172Cr . ↑CMF11d</sub> | 342.50 | -2.0% | +45.9% | 2d | SMA-OK | RS-OK | +0.91% |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH)<br><sub>✓ SAFE . ↗38Cr · 131Cr . ↑CMF6d</sub> | 1638.10 | -12.5% | +131.9% | 2d | SMA-OK | RS-OK | -3.16% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . →110Cr · 86Cr . ↑CMF30d</sub> | 3049.00 | -3.2% | +90.9% | 2d | SMA-OK | RS-OK | +3.00% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>✓ SAFE . ↗229Cr · 78Cr . ↓CMF0d</sub> | 350.20 | -5.4% | +45.2% | 2d | SMA-OK | RS-OK | -0.11% |
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP)<br><sub>✓ SAFE . →98Cr · 70Cr . ↑CMF1d</sub> | 1559.90 | -9.3% | +48.6% | 2d | SMA-OK | RS-OK | +0.58% |
| [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA)<br><sub>✓ SAFE . ↗17Cr · 51Cr . ↑CMF15d</sub> | 523.95 | -6.0% | +68.4% | 2d | SMA-OK | RS-OK | +2.84% |
| [AARTIPHARM](https://in.tradingview.com/chart/?symbol=NSE:AARTIPHARM)<br><sub>✓ SAFE . ↘36Cr · 41Cr . ↓CMF7d</sub> | 881.95 | -9.5% | +49.0% | 2d | SMA-OK | RS-OK | -0.45% |
| [SMSPHARMA](https://in.tradingview.com/chart/?symbol=NSE:SMSPHARMA)<br><sub>✓ SAFE . →17Cr · 37Cr . ↓CMF7d</sub> | 475.45 | -1.6% | +75.1% | 2d | SMA-OK | RS-OK | +7.37% |
| [PARACABLES](https://in.tradingview.com/chart/?symbol=NSE:PARACABLES)<br><sub>✓ SAFE . ↗67Cr · 33Cr . ↑CMF8d</sub> | 63.75 | -14.0% | +123.2% | 2d | SMA-OK | RS-OK | -2.75% |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL)<br><sub>✓ SAFE . ↘27Cr · 30Cr . ↑CMF1d</sub> | 3475.90 | -7.3% | +32.9% | 2d | SMA-OK | RS-OK | -1.55% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↘48Cr · 22Cr . ↓CMF8d</sub> | 215.51 | -9.9% | +99.0% | 2d | SMA-OK | RS-OK | +0.22% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>✓ SAFE . ↗389Cr · 843Cr . ↑CMF2d</sub> | 3710.00 | -2.2% | +131.5% | 3d | SMA-OK | RS-OK | -2.20% |
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO)<br><sub>✓ SAFE . ↗645Cr · 503Cr . ↓CMF5d</sub> | 414.90 | -7.8% | +127.8% | 3d | SMA-OK | RS-OK | -2.47% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . →603Cr · 436Cr . ↑CMF2d</sub> | 1650.00 | -4.4% | +174.4% | 3d | SMA-OK | RS-OK | -1.43% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . →81Cr · 51Cr . ↓CMF0d</sub> | 4310.00 | -7.6% | +185.0% | 3d | SMA-OK | RS-OK | +0.45% |
| [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN)<br><sub>✓ SAFE . ↗20Cr · 22Cr . ↑CMF1d</sub> | 598.95 | -2.3% | +41.4% | 3d | SMA-OK | RS-OK | -0.17% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>✓ SAFE . ↗61Cr · 21Cr . ↓CMF6d</sub> | 1449.00 | -8.7% | +76.0% | 3d | SMA-OK | RS-OK | -0.05% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>✓ SAFE . ↗64Cr · 21Cr . ↑CMF30d</sub> | 1055.30 | -16.4% | +193.5% | 3d | SMA-OK | RS-OK | -3.29% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>✓ SAFE . ↗50Cr · 125Cr . ↑CMF2d</sub> | 802.95 | -4.7% | +151.4% | 4d | SMA-OK | RS-OK | +0.44% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↘401Cr · 233Cr . ↑CMF15d</sub> | 1521.40 | -6.5% | +94.4% | 8d | SMA-OK | RS-OK | -3.33% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>✓ SAFE . ↗383Cr · 205Cr . ↑CMF7d</sub> | 346.00 | -6.9% | +47.4% | 8d | SMA-OK | RS-OK | +1.29% |
| [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS)<br><sub>✓ SAFE . →43Cr · 46Cr . ↑CMF0d</sub> | 932.50 | 0.0% | +98.3% | 8d | SMA-OK | RS-OK | +2.47% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>✓ SAFE . →508Cr · 432Cr . ↑CMF1d</sub> | 1961.90 | -2.6% | +82.7% | 9d | SMA-OK | RS-OK | -1.76% |
| [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS)<br><sub>✓ SAFE . ↗129Cr · 55Cr . ↑CMF3d</sub> | 294.70 | -3.9% | +86.2% | 12d | SMA-OK | RS-OK | +0.67% |
| [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC)<br><sub>✓ SAFE . ↗109Cr · 131Cr . ↑CMF12d</sub> | 793.90 | 0.0% | +63.9% | 13d | SMA-OK | RS-OK | +7.05% |
| [SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK)<br><sub>✓ SAFE . ↗166Cr · 68Cr . ↑CMF25d</sub> | 54.64 | -2.0% | +62.6% | 14d | SMA-OK | RS-OK | +0.61% |
| [AXISCADES](https://in.tradingview.com/chart/?symbol=NSE:AXISCADES)<br><sub>✓ SAFE . ↘27Cr · 23Cr . ↓CMF0d</sub> | 2014.60 | -12.7% | +82.9% | 17d | SMA-OK | RS-OK | +2.62% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . ↘111Cr · 375Cr . ↑CMF30d</sub> | 1445.30 | -1.3% | +57.3% | 21d | SMA-OK | RS-OK | -1.28% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↘467Cr · 338Cr . ↑CMF25d</sub> | 314.55 | -14.1% | +573.6% | 22d | SMA-OK | RS-OK | -0.65% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>✓ SAFE . ↘38Cr · 75Cr . ↓CMF4d</sub> | 702.20 | -6.2% | +82.8% | 23d | SMA-OK | RS-OK | +1.31% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . ↘99Cr · 39Cr . ↓CMF6d</sub> | 3979.00 | -10.4% | +202.8% | 23d | SMA-OK | RS-OK | +0.27% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>✓ SAFE . ↘52Cr · 21Cr . ↑CMF15d</sub> | 24005.00 | -6.6% | +63.0% | 30d | SMA-OK | RS-OK | -0.21% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>✓ SAFE . ↘33Cr · 72Cr . ↑CMF0d</sub> | 763.65 | 0.0% | +710.9% | 40d | SMA-OK | RS-OK | +5.00% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . ↗110Cr · 145Cr . ↑CMF30d</sub> | 840.30 | 0.0% | +243.4% | 43d | SMA-OK | RS-OK | +0.16% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . ↘79Cr · 71Cr . ↓CMF0d</sub> | 65.48 | -1.0% | +178.0% | 43d | SMA-OK | RS-OK | -1.04% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↗253Cr · 230Cr . ↑CMF30d</sub> | 129.55 | -11.9% | +284.6% | 48d | SMA-OK | RS-OK | -5.13% |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA)<br><sub>✓ SAFE . ↗51Cr · 61Cr . ↓CMF9d</sub> | 605.20 | -2.8% | +55.3% | 52d | SMA-OK | RS-OK | +2.01% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↘80Cr · 213Cr . ↓CMF0d</sub> | 1060.10 | -18.5% | +229.4% | 53d | SMA-OK | RS-OK | -1.95% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>✓ SAFE . →36Cr · 29Cr . ↑CMF28d</sub> | 165.43 | -4.1% | +101.0% | 53d | SMA-OK | RS-OK | -1.86% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>✓ SAFE . ↘87Cr · 79Cr . ↑CMF25d</sub> | 321.15 | -24.1% | +105.0% | 55d | SMA-OK | RS-OK | -5.29% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . ↘116Cr · 84Cr . ↑CMF0d</sub> | 345.10 | -1.5% | +162.8% | 70d | SMA-OK | RS-OK | -0.62% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↗365Cr · 75Cr . ↑CMF17d</sub> | 526.60 | -1.1% | +209.0% | 72d | SMA-OK | RS-OK | -0.43% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . →174Cr · 104Cr . ↑CMF1d</sub> | 156.94 | -2.4% | +184.1% | 73d | SMA-OK | RS-OK | +1.23% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . →68Cr · 36Cr . ↑CMF3d</sub> | 400.00 | -4.3% | +83.8% | 80d | SMA-OK | RS-OK | -0.32% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>✓ SAFE . ↘34Cr · 27Cr . ↑CMF22d</sub> | 3166.10 | -5.4% | +173.0% | 98d | SMA-OK | RS-OK | -1.98% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . →262Cr · 361Cr . ↓CMF0d</sub> | 1955.00 | -5.5% | +112.3% | 117d | SMA-OK | RS-OK | -2.37% |

### By Trend Age

**<2 WEEKS** (37)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:63MOONS,NSE:AARTIDRUGS,NSE:AARTIPHARM,NSE:ACUTAAS,NSE:ALIVUS,NSE:ANTELOPUS,NSE:APOLLO,NSE:ATHERENERG,NSE:CEMPRO,NSE:CHENNPETRO,NSE:COFORGE,NSE:CRAFTSMAN,NSE:FEDERALBNK,NSE:GABRIEL,NSE:GESHIP,NSE:GLAND,NSE:INDGN,NSE:INDHOTEL,NSE:INDSWFTLAB,NSE:KARURVYSYA,NSE:LALPATHLAB,NSE:LUMAXTECH,NSE:MAHLOG,NSE:NAVINFLUOR,NSE:NUVAMA,NSE:NYKAA,NSE:PARACABLES,NSE:PPLPHARMA,NSE:PRIVISCL,NSE:SANSERA,NSE:SAREGAMA,NSE:SETL,NSE:SGMART,NSE:SMSPHARMA,NSE:SONACOMS,NSE:UNIMECH,NSE:WELSPUNLIV
```

**2-4 WEEKS** (6)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AXISCADES,NSE:HFCL,NSE:KROSS,NSE:PVRINOX,NSE:SOUTHBANK,NSE:TIPSMUSIC
```

**1-2 MONTHS** (6)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:CPPLUS,NSE:CUPID,NSE:PTCIL,NSE:SIGMAADV,NSE:STLTECH
```

**2-3 MONTHS** (7)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MOREPENLAB,NSE:RAYMOND,NSE:SAMBHV,NSE:SBC,NSE:SHANTIGOLD,NSE:SHREEJISPG,NSE:THELEELA
```

**3-6 MONTHS** (6)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:KMEW,NSE:LAURUSLABS,NSE:NAZARA,NSE:RATNAVEER,NSE:SSWL,NSE:TFCILTD
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
