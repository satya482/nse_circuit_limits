> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-11-06
*Generated 2026-11-06 15:51 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS) | [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX) |
| [AARTIPHARM](https://in.tradingview.com/chart/?symbol=NSE:AARTIPHARM) | [ASKAUTOLTD](https://in.tradingview.com/chart/?symbol=NSE:ASKAUTOLTD) |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE) | [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN) |
| [ALIVUS](https://in.tradingview.com/chart/?symbol=NSE:ALIVUS) | [CEIGALL](https://in.tradingview.com/chart/?symbol=NSE:CEIGALL) |
| [BLUEJET](https://in.tradingview.com/chart/?symbol=NSE:BLUEJET) | [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG) |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH) | [GHCLTEXTIL](https://in.tradingview.com/chart/?symbol=NSE:GHCLTEXTIL) |
| [IKIO](https://in.tradingview.com/chart/?symbol=NSE:IKIO) | [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL) |
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL) | [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB) |
| [MMFL](https://in.tradingview.com/chart/?symbol=NSE:MMFL) | [JASH](https://in.tradingview.com/chart/?symbol=NSE:JASH) |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA) | [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA) |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA) | [KAJARIACER](https://in.tradingview.com/chart/?symbol=NSE:KAJARIACER) |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS) | [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW) |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL) | [LOTUSDEV](https://in.tradingview.com/chart/?symbol=NSE:LOTUSDEV) |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART) | [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE) |
| [STYLEBAAZA](https://in.tradingview.com/chart/?symbol=NSE:STYLEBAAZA) | [PARACABLES](https://in.tradingview.com/chart/?symbol=NSE:PARACABLES) |
| [WABAG](https://in.tradingview.com/chart/?symbol=NSE:WABAG) | [PRICOLLTD](https://in.tradingview.com/chart/?symbol=NSE:PRICOLLTD) |
|  | [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA) |
|  | [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE) |
|  | [RPTECH](https://in.tradingview.com/chart/?symbol=NSE:RPTECH) |
|  | [SMSPHARMA](https://in.tradingview.com/chart/?symbol=NSE:SMSPHARMA) |
|  | [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA) |
|  | [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH) |

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

**Qualifying: 79**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AARTIPHARM,NSE:ACE,NSE:ACUTAAS,NSE:ADANIPORTS,NSE:ALIVUS,NSE:ANTHEM,NSE:APOLLO,NSE:ATHERENERG,NSE:AUROPHARMA,NSE:BLUEJET,NSE:BOSCHLTD,NSE:CEMPRO,NSE:CPPLUS,NSE:DIACABS,NSE:DIVISLAB,NSE:DYNAMATECH,NSE:EMCURE,NSE:ENGINERSIN,NSE:ENTERO,NSE:ETERNAL,NSE:FLUOROCHEM,NSE:GAIL,NSE:GLAND,NSE:GLENMARK,NSE:HAL,NSE:HONASA,NSE:ICIL,NSE:IKIO,NSE:INDHOTEL,NSE:JYOTICNC,NSE:KALYANKJIL,NSE:KARURVYSYA,NSE:LALPATHLAB,NSE:LUMAXTECH,NSE:MAHABANK,NSE:MCX,NSE:MMFL,NSE:MOTILALOFS,NSE:MUFIN,NSE:NAVINFLUOR,NSE:NEOGEN,NSE:NUVAMA,NSE:NYKAA,NSE:PHOENIXLTD,NSE:PPLPHARMA,NSE:RADICO,NSE:ROLEXRINGS,NSE:RUBICON,NSE:SAILIFE,NSE:SANSERA,NSE:SAREGAMA,NSE:SHRINGARMS,NSE:SKYGOLD,NSE:SONACOMS,NSE:STYLEBAAZA,NSE:TECHM,NSE:WABAG,NSE:WELSPUNLIV,NSE:ZYDUSLIFE,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:63MOONS,NSE:COFORGE,NSE:GRWRHITECH,NSE:SGMART,NSE:SOUTHBANK,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:CUPID,NSE:OPTIEMUS,NSE:PTCIL,NSE:PVRINOX,NSE:SHYAMMETL,NSE:STLTECH,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:MOREPENLAB,NSE:RAYMOND,NSE:SAMBHV,NSE:SBC,NSE:SHREEJISPG,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:LAURUSLABS,NSE:NAZARA,NSE:RATNAVEER,NSE:TFCILTD
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL)<br><sub>✓ SAFE . ↗375Cr · 1475Cr . ↑CMF0d</sub> | 590.75 | -6.9% | +78.6% | 0d | SMA-OK | RS-OK | +5.49% |
| [IKIO](https://in.tradingview.com/chart/?symbol=NSE:IKIO)<br><sub>✓ SAFE . ↗39Cr · 375Cr . ↑CMF0d</sub> | 196.69 | -15.1% | +83.3% | 0d | SMA-OK | RS-OK | +13.11% |
| [WABAG](https://in.tradingview.com/chart/?symbol=NSE:WABAG)<br><sub>✓ SAFE . ↗116Cr · 317Cr . ↑CMF0d</sub> | 1988.20 | -12.7% | +89.5% | 0d | SMA-OK | RS-OK | +6.57% |
| [MMFL](https://in.tradingview.com/chart/?symbol=NSE:MMFL)<br><sub>✓ SAFE . ↗39Cr · 314Cr . ↑CMF0d</sub> | 629.40 | -7.5% | +111.1% | 0d | SMA-OK | RS-OK | +19.95% |
| [MOTILALOFS](https://in.tradingview.com/chart/?symbol=NSE:MOTILALOFS)<br><sub>✓ SAFE . ↗160Cr · 213Cr . ↑CMF1d</sub> | 1102.00 | 0.0% | +75.4% | 0d | SMA-OK | RS-OK | +0.64% |
| [RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO)<br><sub>✓ SAFE . ↗297Cr · 100Cr . ↑CMF6d</sub> | 4515.20 | -4.6% | +77.7% | 0d | SMA-OK | RS-OK | -0.22% |
| [STYLEBAAZA](https://in.tradingview.com/chart/?symbol=NSE:STYLEBAAZA)<br><sub>✓ SAFE . ↘28Cr · 82Cr . ↓CMF9d</sub> | 390.75 | -11.1% | +64.8% | 0d | SMA-OK | RS-OK | +4.84% |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE)<br><sub>✓ SAFE . ↗38Cr · 78Cr . ↑CMF0d</sub> | 1167.70 | -6.9% | +55.9% | 0d | SMA-OK | RS-OK | +3.55% |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN)<br><sub>✓ SAFE . ↗203Cr · 75Cr . ↑CMF4d</sub> | 292.70 | -7.3% | +77.9% | 0d | SMA-OK | RS-OK | -1.94% |
| [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS)<br><sub>✓ SAFE . ↗88Cr · 66Cr . ↑CMF2d</sub> | 201.17 | -2.2% | +100.3% | 0d | SMA-OK | RS-OK | -2.19% |
| [BLUEJET](https://in.tradingview.com/chart/?symbol=NSE:BLUEJET)<br><sub>✓ SAFE . ↗77Cr · 62Cr . ↑CMF1d</sub> | 553.80 | -11.6% | +69.2% | 0d | SMA-OK | RS-OK | -3.91% |
| [JYOTICNC](https://in.tradingview.com/chart/?symbol=NSE:JYOTICNC)<br><sub>✓ SAFE . ↗144Cr · 59Cr . ↑CMF2d</sub> | 1019.90 | -8.4% | +74.2% | 0d | SMA-OK | RS-OK | -0.23% |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>✓ SAFE . ↘42Cr · 56Cr . ↑CMF0d</sub> | 2548.60 | -5.2% | +160.1% | 0d | SMA-OK | RS-OK | +5.84% |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH)<br><sub>✓ SAFE . →23Cr · 45Cr . ↑CMF2d</sub> | 12822.00 | -11.1% | +62.3% | 0d | SMA-OK | RS-OK | -0.83% |
| [TECHM](https://in.tradingview.com/chart/?symbol=NSE:TECHM)<br><sub>✓ SAFE . ↘599Cr · 383Cr . ↑CMF11d</sub> | 1780.10 | -3.0% | +34.1% | 1d | SMA-OK | RS-OK | -0.60% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>⚠ CAUTION . →130Cr · 230Cr . ↓CMF21d</sub> | 176.19 | -2.9% | +30.1% | 1d | SMA-OK | RS-OK | +4.93% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>✓ SAFE . ↗67Cr · 229Cr . ↑CMF0d</sub> | 1900.40 | 0.0% | +100.2% | 2d | SMA-OK | RS-OK | +8.34% |
| [MAHABANK](https://in.tradingview.com/chart/?symbol=NSE:MAHABANK)<br><sub>✓ SAFE . ↗158Cr · 208Cr . ↑CMF8d</sub> | 86.91 | -7.4% | +54.6% | 2d | SMA-OK | RS-OK | +2.13% |
| [HONASA](https://in.tradingview.com/chart/?symbol=NSE:HONASA)<br><sub>✓ SAFE . ↗43Cr · 171Cr . ↓CMF0d</sub> | 466.40 | -7.2% | +82.0% | 3d | SMA-OK | RS-OK | -3.19% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . ↘143Cr · 266Cr . ↑CMF12d</sub> | 352.90 | 0.0% | +50.4% | 3d | SMA-OK | RS-OK | +3.04% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>✓ SAFE . ↘105Cr · 133Cr . ↓CMF7d</sub> | 370.05 | 0.0% | +53.5% | 3d | SMA-OK | RS-OK | +2.65% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>✓ SAFE . →33Cr · 46Cr . ↑CMF10d</sub> | 915.55 | -4.4% | +55.7% | 3d | SMA-OK | RS-OK | +0.22% |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>⚠ CAUTION . ↗49Cr · 38Cr . ↑CMF2d</sub> | 4665.50 | -2.5% | +57.1% | 3d | SMA-OK | RS-OK | -0.94% |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . ↗979Cr · 1459Cr . ↑CMF8d</sub> | 3528.00 | 0.0% | +87.1% | 4d | SMA-OK | RS-OK | +4.81% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>⚠ CAUTION . →93Cr · 96Cr . ↑CMF3d</sub> | 47970.00 | -4.1% | +66.9% | 4d | SMA-OK | RS-OK | +1.63% |
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO)<br><sub>✓ SAFE . ↗676Cr · 289Cr . ↓CMF12d</sub> | 413.65 | -8.1% | +127.1% | 4d | SMA-OK | RS-OK | -4.83% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>✓ SAFE . ↗71Cr · 112Cr . ↑CMF4d</sub> | 1970.00 | -2.9% | +50.7% | 4d | SMA-OK | RS-OK | +0.16% |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS)<br><sub>✓ SAFE . ↗60Cr · 58Cr . ↑CMF9d</sub> | 370.65 | -6.1% | +214.3% | 4d | SMA-OK | RS-OK | -4.58% |
| [EMCURE](https://in.tradingview.com/chart/?symbol=NSE:EMCURE)<br><sub>✓ SAFE . ↗78Cr · 51Cr . ↑CMF10d</sub> | 2212.80 | -1.4% | +65.5% | 4d | SMA-OK | RS-OK | -1.43% |
| [GLENMARK](https://in.tradingview.com/chart/?symbol=NSE:GLENMARK)<br><sub>✓ SAFE . ↗303Cr · 1304Cr . ↑CMF4d</sub> | 2590.00 | 0.0% | +42.5% | 5d | SMA-OK | RS-OK | +4.36% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . ↗717Cr · 890Cr . ↑CMF4d</sub> | 9927.00 | 0.0% | +70.5% | 5d | SMA-OK | RS-OK | +1.50% |
| [HAL](https://in.tradingview.com/chart/?symbol=NSE:HAL)<br><sub>✓ SAFE . →341Cr · 275Cr . ↑CMF8d</sub> | 4837.80 | -5.1% | +38.7% | 5d | SMA-OK | RS-OK | -0.33% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . →147Cr · 488Cr . ↓CMF0d</sub> | 4131.40 | -7.0% | +201.3% | 5d | SMA-OK | RS-OK | -0.94% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↗90Cr · 211Cr . ↓CMF0d</sub> | 4322.70 | -7.3% | +182.7% | 5d | SMA-OK | RS-OK | -2.46% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>✓ SAFE . →38Cr · 114Cr . ↑CMF10d</sub> | 1659.30 | -10.8% | +169.7% | 5d | SMA-OK | RS-OK | -4.67% |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA)<br><sub>✓ SAFE . →52Cr · 87Cr . ↑CMF24d</sub> | 1848.10 | -6.7% | +66.4% | 5d | SMA-OK | RS-OK | -1.35% |
| [MUFIN](https://in.tradingview.com/chart/?symbol=NSE:MUFIN)<br><sub>✓ SAFE . ↗25Cr · 34Cr . ↑CMF6d</sub> | 141.46 | -1.4% | +48.3% | 5d | SMA-OK | RS-OK | -1.35% |
| [ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL)<br><sub>✓ SAFE . ↗77Cr · 34Cr . ↑CMF6d</sub> | 489.85 | -6.8% | +118.2% | 5d | SMA-OK | RS-OK | -2.25% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . ↗314Cr · 2361Cr . ↑CMF5d</sub> | 1785.10 | 0.0% | +124.5% | 6d | SMA-OK | RS-OK | +11.95% |
| [ETERNAL](https://in.tradingview.com/chart/?symbol=NSE:ETERNAL)<br><sub>✓ SAFE . ↗1228Cr · 616Cr . ↑CMF2d</sub> | 344.20 | 0.0% | +59.6% | 6d | SMA-OK | RS-OK | +0.16% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>✓ SAFE . ↘537Cr · 253Cr . ↑CMF30d</sub> | 1846.00 | -2.0% | +41.6% | 6d | SMA-OK | RS-OK | -0.22% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>✓ SAFE . ↗219Cr · 233Cr . ↑CMF9d</sub> | 1800.00 | 0.0% | +60.5% | 6d | SMA-OK | RS-OK | +0.84% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>✓ SAFE . →170Cr · 139Cr . ↑CMF2d</sub> | 1238.60 | -0.6% | +43.9% | 6d | SMA-OK | RS-OK | -0.55% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . ↗234Cr · 198Cr . ↑CMF8d</sub> | 9010.00 | 0.0% | +62.0% | 6d | SMA-OK | RS-OK | +1.87% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↗434Cr · 108Cr . ↑CMF4d</sub> | 241.30 | -8.8% | +122.8% | 6d | SMA-OK | RS-OK | -4.75% |
| [SHRINGARMS](https://in.tradingview.com/chart/?symbol=NSE:SHRINGARMS)<br><sub>✓ SAFE . ↘40Cr · 49Cr . ↑CMF19d</sub> | 309.45 | -3.1% | +85.4% | 6d | SMA-OK | RS-OK | -0.83% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . ↗241Cr · 95Cr . ↑CMF21d</sub> | 951.95 | -10.2% | +215.7% | 7d | SMA-OK | RS-OK | +0.31% |
| [PHOENIXLTD](https://in.tradingview.com/chart/?symbol=NSE:PHOENIXLTD)<br><sub>⚠ CAUTION . ↘87Cr · 66Cr . ↑CMF1d</sub> | 2154.90 | 0.0% | +45.9% | 7d | SMA-OK | RS-OK | +1.36% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>✓ SAFE . ↗629Cr · 442Cr . ↑CMF7d</sub> | 822.90 | 0.0% | +44.1% | 8d | SMA-OK | RS-OK | +1.39% |
| [ALIVUS](https://in.tradingview.com/chart/?symbol=NSE:ALIVUS)<br><sub>✓ SAFE . ↗76Cr · 234Cr . ↑CMF0d</sub> | 1480.60 | -2.6% | +72.2% | 8d | SMA-OK | RS-OK | -1.11% |
| [CEMPRO](https://in.tradingview.com/chart/?symbol=NSE:CEMPRO)<br><sub>✓ SAFE . ↘70Cr · 114Cr . ↓CMF1d</sub> | 1323.30 | -19.3% | +159.6% | 8d | SMA-OK | RS-OK | +2.79% |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH)<br><sub>✓ SAFE . ↗70Cr · 99Cr . ↑CMF9d</sub> | 2327.40 | 0.0% | +80.8% | 8d | SMA-OK | RS-OK | +3.17% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>✓ SAFE . ↗487Cr · 68Cr . ↑CMF7d</sub> | 239.32 | -0.3% | +79.6% | 8d | SMA-OK | RS-OK | +0.29% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↗440Cr · 121Cr . ↑CMF9d</sub> | 900.00 | -1.7% | +102.5% | 9d | SMA-OK | RS-OK | -1.67% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↗123Cr · 112Cr . ↑CMF30d</sub> | 3169.30 | 0.0% | +98.5% | 9d | SMA-OK | RS-OK | +0.77% |
| [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA)<br><sub>✓ SAFE . ↗240Cr · 75Cr . ↑CMF22d</sub> | 619.65 | -2.7% | +99.2% | 9d | SMA-OK | RS-OK | -1.96% |
| [AARTIPHARM](https://in.tradingview.com/chart/?symbol=NSE:AARTIPHARM)<br><sub>✓ SAFE . ↗72Cr · 40Cr . ↑CMF4d</sub> | 929.10 | -4.7% | +57.0% | 9d | SMA-OK | RS-OK | +0.09% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . ↗922Cr · 428Cr . ↑CMF9d</sub> | 1821.70 | -1.0% | +202.9% | 10d | SMA-OK | RS-OK | +2.42% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>✓ SAFE . ↗542Cr · 104Cr . ↑CMF9d</sub> | 3786.60 | -5.4% | +136.3% | 10d | SMA-OK | RS-OK | +0.42% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>✓ SAFE . ↘47Cr · 45Cr . ↑CMF30d</sub> | 7653.50 | 0.0% | +183.0% | 11d | SMA-OK | RS-OK | +0.30% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>✓ SAFE . ↗116Cr · 40Cr . ↑CMF9d</sub> | 859.15 | -4.9% | +169.0% | 11d | SMA-OK | RS-OK | -4.33% |
| [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS)<br><sub>✓ SAFE . ↘41Cr · 36Cr . ↑CMF4d</sub> | 896.00 | -6.8% | +90.5% | 15d | SMA-OK | RS-OK | -5.87% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>✓ SAFE . ↗622Cr · 505Cr . ↑CMF8d</sub> | 2076.00 | -1.1% | +93.3% | 16d | SMA-OK | RS-OK | -0.14% |
| [SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK)<br><sub>✓ SAFE . ↘85Cr · 89Cr . ↑CMF30d</sub> | 57.75 | 0.0% | +71.9% | 21d | SMA-OK | RS-OK | +2.54% |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL)<br><sub>✓ SAFE . →63Cr · 150Cr . ↑CMF18d</sub> | 1300.60 | 0.0% | +70.8% | 24d | SMA-OK | RS-OK | +2.41% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . ↗181Cr · 108Cr . ↑CMF30d</sub> | 1565.60 | -1.0% | +70.4% | 28d | SMA-OK | RS-OK | -1.00% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↘349Cr · 122Cr . ↓CMF1d</sub> | 338.90 | -7.4% | +569.1% | 29d | SMA-OK | RS-OK | -0.69% |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS)<br><sub>✓ SAFE . →34Cr · 42Cr . ↑CMF1d</sub> | 746.75 | -16.1% | +155.1% | 35d | SMA-OK | RS-OK | -10.14% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>✓ SAFE . ↘38Cr · 50Cr . ↑CMF0d</sub> | 24335.00 | -5.4% | +65.3% | 37d | SMA-OK | RS-OK | +0.04% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↗253Cr · 230Cr . ↑CMF30d</sub> | 129.55 | -11.9% | +284.6% | 48d | SMA-OK | RS-OK | -5.13% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . →88Cr · 84Cr . ↓CMF7d</sub> | 68.70 | 0.0% | +179.3% | 50d | SMA-OK | RS-OK | +2.86% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . →102Cr · 56Cr . ↑CMF30d</sub> | 884.55 | 0.0% | +228.0% | 50d | SMA-OK | RS-OK | +2.40% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . →85Cr · 47Cr . ↑CMF2d</sub> | 1082.00 | -16.8% | +236.2% | 60d | SMA-OK | RS-OK | -4.31% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>✓ SAFE . →45Cr · 31Cr . ↓CMF1d</sub> | 163.39 | -5.3% | +98.5% | 60d | SMA-OK | RS-OK | -3.02% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . →153Cr · 114Cr . ↑CMF5d</sub> | 365.75 | -3.9% | +178.6% | 77d | SMA-OK | RS-OK | -1.98% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . ↗231Cr · 209Cr . ↑CMF8d</sub> | 160.50 | -0.9% | +190.6% | 80d | SMA-OK | RS-OK | -0.47% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . ↘59Cr · 33Cr . ↑CMF10d</sub> | 412.10 | -2.1% | +89.3% | 87d | SMA-OK | RS-OK | -1.32% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . ↗629Cr · 700Cr . ↑CMF5d</sub> | 2350.00 | -2.3% | +152.6% | 123d | SMA-OK | RS-OK | -2.31% |

### By Trend Age

**<2 WEEKS** (59)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AARTIPHARM,NSE:ACE,NSE:ACUTAAS,NSE:ADANIPORTS,NSE:ALIVUS,NSE:ANTHEM,NSE:APOLLO,NSE:ATHERENERG,NSE:AUROPHARMA,NSE:BLUEJET,NSE:BOSCHLTD,NSE:CEMPRO,NSE:CPPLUS,NSE:DIACABS,NSE:DIVISLAB,NSE:DYNAMATECH,NSE:EMCURE,NSE:ENGINERSIN,NSE:ENTERO,NSE:ETERNAL,NSE:FLUOROCHEM,NSE:GAIL,NSE:GLAND,NSE:GLENMARK,NSE:HAL,NSE:HONASA,NSE:ICIL,NSE:IKIO,NSE:INDHOTEL,NSE:JYOTICNC,NSE:KALYANKJIL,NSE:KARURVYSYA,NSE:LALPATHLAB,NSE:LUMAXTECH,NSE:MAHABANK,NSE:MCX,NSE:MMFL,NSE:MOTILALOFS,NSE:MUFIN,NSE:NAVINFLUOR,NSE:NEOGEN,NSE:NUVAMA,NSE:NYKAA,NSE:PHOENIXLTD,NSE:PPLPHARMA,NSE:RADICO,NSE:ROLEXRINGS,NSE:RUBICON,NSE:SAILIFE,NSE:SANSERA,NSE:SAREGAMA,NSE:SHRINGARMS,NSE:SKYGOLD,NSE:SONACOMS,NSE:STYLEBAAZA,NSE:TECHM,NSE:WABAG,NSE:WELSPUNLIV,NSE:ZYDUSLIFE
```

**2-4 WEEKS** (5)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:63MOONS,NSE:COFORGE,NSE:GRWRHITECH,NSE:SGMART,NSE:SOUTHBANK
```

**1-2 MONTHS** (6)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CUPID,NSE:OPTIEMUS,NSE:PTCIL,NSE:PVRINOX,NSE:SHYAMMETL,NSE:STLTECH
```

**2-3 MONTHS** (5)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:MOREPENLAB,NSE:RAYMOND,NSE:SAMBHV,NSE:SBC,NSE:SHREEJISPG
```

**3-6 MONTHS** (4)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LAURUSLABS,NSE:NAZARA,NSE:RATNAVEER,NSE:TFCILTD
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
