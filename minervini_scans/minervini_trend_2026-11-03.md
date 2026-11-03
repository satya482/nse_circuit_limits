> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-11-03
*Generated 2026-11-03 15:49 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS) | [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS) |
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO) | [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL) |
| [ARFIN](https://in.tradingview.com/chart/?symbol=NSE:ARFIN) | [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR) |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD) | [CEMPRO](https://in.tradingview.com/chart/?symbol=NSE:CEMPRO) |
| [CCAVENUE](https://in.tradingview.com/chart/?symbol=NSE:CCAVENUE) | [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK) |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS) | [GREAVESCOT](https://in.tradingview.com/chart/?symbol=NSE:GREAVESCOT) |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB) | [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA) |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG) | [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS) |
| [EMCURE](https://in.tradingview.com/chart/?symbol=NSE:EMCURE) | [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH) |
| [ETERNAL](https://in.tradingview.com/chart/?symbol=NSE:ETERNAL) | [MENONBE](https://in.tradingview.com/chart/?symbol=NSE:MENONBE) |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL) | [MUFIN](https://in.tradingview.com/chart/?symbol=NSE:MUFIN) |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH) | [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL) |
| [HAL](https://in.tradingview.com/chart/?symbol=NSE:HAL) | [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV) |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB) |  |
| [LOTUSDEV](https://in.tradingview.com/chart/?symbol=NSE:LOTUSDEV) |  |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX) |  |
| [MINDACORP](https://in.tradingview.com/chart/?symbol=NSE:MINDACORP) |  |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA) |  |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS) |  |
| [PRINCEPIPE](https://in.tradingview.com/chart/?symbol=NSE:PRINCEPIPE) |  |
| [RML](https://in.tradingview.com/chart/?symbol=NSE:RML) |  |
| [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA) |  |
| [SHREEPUSHK](https://in.tradingview.com/chart/?symbol=NSE:SHREEPUSHK) |  |
| [TECHM](https://in.tradingview.com/chart/?symbol=NSE:TECHM) |  |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE) |  |

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
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AARTIDRUGS,NSE:AARTIPHARM,NSE:ACUTAAS,NSE:ADANIPORTS,NSE:ALIVUS,NSE:APOLLO,NSE:ARFIN,NSE:ATHERENERG,NSE:AUROPHARMA,NSE:BEML,NSE:BOSCHLTD,NSE:CCAVENUE,NSE:CPPLUS,NSE:DIACABS,NSE:DIVISLAB,NSE:EBGNG,NSE:EMCURE,NSE:ENGINERSIN,NSE:ETERNAL,NSE:GABRIEL,NSE:GAIL,NSE:GESHIP,NSE:GLAND,NSE:GLENMARK,NSE:GRWRHITECH,NSE:HAL,NSE:INDGN,NSE:INDHOTEL,NSE:IPCALAB,NSE:LALPATHLAB,NSE:MCX,NSE:MINDACORP,NSE:NAVINFLUOR,NSE:NITINSPIN,NSE:NUVAMA,NSE:NYKAA,NSE:PHOENIXLTD,NSE:PPLPHARMA,NSE:PRINCEPIPE,NSE:RML,NSE:RUBICON,NSE:SAILIFE,NSE:SANSERA,NSE:SAREGAMA,NSE:SGMART,NSE:SHREEPUSHK,NSE:SMSPHARMA,NSE:SONACOMS,NSE:TECHM,NSE:WELSPUNLIV,NSE:ZYDUSLIFE,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:CHENNPETRO,NSE:COFORGE,NSE:HFCL,NSE:SHYAMMETL,NSE:SOUTHBANK,NSE:TIPSMUSIC,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:CUPID,NSE:LOTUSDEV,NSE:OPTIEMUS,NSE:PVRINOX,NSE:STLTECH,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:RAYMOND,NSE:SBC,NSE:SHREEJISPG,NSE:THELEELA,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:LAURUSLABS,NSE:NAZARA,NSE:RATNAVEER,NSE:SSWL,NSE:TFCILTD
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN)<br><sub>✓ SAFE . ↗196Cr · 238Cr . ↑CMF1d</sub> | 289.25 | -8.4% | +75.8% | 0d | SMA-OK | RS-OK | -0.14% |
| [RML](https://in.tradingview.com/chart/?symbol=NSE:RML)<br><sub>⚠ CAUTION . ↗6Cr · 31Cr . ↓CMF21d</sub> | 1316.30 | -6.6% | +112.3% | 0d | SMA-OK | RS-OK | +6.91% |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . →562Cr · 1657Cr . ↑CMF5d</sub> | 3490.10 | 0.0% | +88.7% | 1d | SMA-OK | RS-OK | +7.42% |
| [TECHM](https://in.tradingview.com/chart/?symbol=NSE:TECHM)<br><sub>✓ SAFE . ↘599Cr · 383Cr . ↑CMF11d</sub> | 1780.10 | -3.0% | +34.1% | 1d | SMA-OK | RS-OK | -0.60% |
| [GAIL](https://in.tradingview.com/chart/?symbol=NSE:GAIL)<br><sub>⚠ CAUTION . →130Cr · 230Cr . ↓CMF21d</sub> | 176.19 | -2.9% | +30.1% | 1d | SMA-OK | RS-OK | +4.93% |
| [EMCURE](https://in.tradingview.com/chart/?symbol=NSE:EMCURE)<br><sub>✓ SAFE . ↗38Cr · 199Cr . ↑CMF7d</sub> | 1976.60 | -1.6% | +49.2% | 1d | SMA-OK | RS-OK | +4.94% |
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO)<br><sub>✓ SAFE . ↗594Cr · 188Cr . ↓CMF9d</sub> | 401.20 | -10.9% | +120.2% | 1d | SMA-OK | RS-OK | +0.85% |
| [MINDACORP](https://in.tradingview.com/chart/?symbol=NSE:MINDACORP)<br><sub>✓ SAFE . ↗30Cr · 120Cr . ↑CMF3d</sub> | 684.60 | -8.1% | +42.4% | 1d | SMA-OK | RS-OK | +3.90% |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS)<br><sub>✓ SAFE . ↗47Cr · 106Cr . ↑CMF6d</sub> | 367.50 | -6.9% | +211.6% | 1d | SMA-OK | RS-OK | +5.00% |
| [ARFIN](https://in.tradingview.com/chart/?symbol=NSE:ARFIN)<br><sub>✓ SAFE . ↘21Cr · 63Cr . ↓CMF0d</sub> | 95.77 | -11.5% | +76.2% | 1d | SMA-OK | RS-OK | +4.95% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>⚠ CAUTION . ↗48Cr · 45Cr . ↑CMF1d</sub> | 1925.70 | -4.0% | +47.3% | 1d | SMA-OK | RS-OK | +2.04% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>✓ SAFE . ↗63Cr · 43Cr . ↓CMF12d</sub> | 687.20 | -6.0% | +183.3% | 1d | SMA-OK | RS-OK | +4.18% |
| [GLENMARK](https://in.tradingview.com/chart/?symbol=NSE:GLENMARK)<br><sub>✓ SAFE . ↗171Cr · 224Cr . ↑CMF1d</sub> | 2408.00 | -4.3% | +33.0% | 2d | SMA-OK | RS-OK | +1.09% |
| [PRINCEPIPE](https://in.tradingview.com/chart/?symbol=NSE:PRINCEPIPE)<br><sub>✓ SAFE . ↗18Cr · 134Cr . ↑CMF16d</sub> | 275.90 | -14.8% | +33.9% | 2d | SMA-OK | RS-OK | +2.58% |
| [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA)<br><sub>✓ SAFE . →56Cr · 73Cr . ↑CMF21d</sub> | 1866.20 | -5.8% | +68.0% | 2d | SMA-OK | RS-OK | +3.38% |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>⚠ CAUTION . ↗56Cr · 71Cr . ↓CMF30d</sub> | 1950.10 | -3.0% | +50.6% | 2d | SMA-OK | RS-OK | +0.01% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↗82Cr · 68Cr . ↓CMF2d</sub> | 4225.20 | -9.4% | +178.9% | 2d | SMA-OK | RS-OK | +1.63% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . ↘91Cr · 58Cr . ↓CMF10d</sub> | 3881.10 | -12.6% | +193.6% | 2d | SMA-OK | RS-OK | +0.83% |
| [INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN)<br><sub>✓ SAFE . ↗40Cr · 49Cr . ↓CMF1d</sub> | 612.80 | -1.1% | +44.7% | 2d | SMA-OK | RS-OK | -1.07% |
| [RUBICON](https://in.tradingview.com/chart/?symbol=NSE:RUBICON)<br><sub>✓ SAFE . ↗38Cr · 33Cr . ↑CMF7d</sub> | 1718.00 | -7.7% | +179.3% | 2d | SMA-OK | RS-OK | +3.03% |
| [AARTIDRUGS](https://in.tradingview.com/chart/?symbol=NSE:AARTIDRUGS)<br><sub>✓ SAFE . ↗70Cr · 32Cr . ↑CMF4d</sub> | 466.30 | -10.4% | +45.8% | 2d | SMA-OK | RS-OK | +2.75% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↗360Cr · 1059Cr . ↑CMF1d</sub> | 253.09 | 0.0% | +133.7% | 3d | SMA-OK | RS-OK | +4.44% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>⚠ CAUTION . ↗146Cr · 224Cr . ↑CMF6d</sub> | 1694.50 | -2.3% | +51.1% | 3d | SMA-OK | RS-OK | +0.64% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . ↘143Cr · 266Cr . ↑CMF12d</sub> | 352.90 | 0.0% | +50.4% | 3d | SMA-OK | RS-OK | +3.04% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . ↗191Cr · 148Cr . ↑CMF5d</sub> | 8530.00 | -2.8% | +53.3% | 3d | SMA-OK | RS-OK | +1.48% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . →74Cr · 62Cr . ↑CMF2d</sub> | 1558.20 | -7.0% | +96.0% | 3d | SMA-OK | RS-OK | +1.03% |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML)<br><sub>✓ SAFE . ↗46Cr · 30Cr . ↑CMF7d</sub> | 2051.70 | -4.6% | +49.8% | 3d | SMA-OK | RS-OK | +1.02% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>⚠ CAUTION . →93Cr · 96Cr . ↑CMF3d</sub> | 47970.00 | -4.1% | +66.9% | 4d | SMA-OK | RS-OK | +1.63% |
| [PHOENIXLTD](https://in.tradingview.com/chart/?symbol=NSE:PHOENIXLTD)<br><sub>⚠ CAUTION . →96Cr · 98Cr . ↓CMF25d</sub> | 2048.70 | -4.9% | +38.7% | 4d | SMA-OK | RS-OK | +1.59% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . ↗717Cr · 890Cr . ↑CMF4d</sub> | 9927.00 | 0.0% | +70.5% | 5d | SMA-OK | RS-OK | +1.50% |
| [HAL](https://in.tradingview.com/chart/?symbol=NSE:HAL)<br><sub>✓ SAFE . →341Cr · 275Cr . ↑CMF8d</sub> | 4837.80 | -5.1% | +38.7% | 5d | SMA-OK | RS-OK | -0.33% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>✓ SAFE . ↗469Cr · 175Cr . ↑CMF4d</sub> | 233.69 | -2.6% | +75.4% | 5d | SMA-OK | RS-OK | -2.60% |
| [ALIVUS](https://in.tradingview.com/chart/?symbol=NSE:ALIVUS)<br><sub>✓ SAFE . ↗46Cr · 78Cr . ↓CMF2d</sub> | 1481.30 | 0.0% | +72.2% | 5d | SMA-OK | RS-OK | +2.33% |
| [NITINSPIN](https://in.tradingview.com/chart/?symbol=NSE:NITINSPIN)<br><sub>✓ SAFE . ↗14Cr · 34Cr . ↑CMF12d</sub> | 658.80 | -0.8% | +115.8% | 5d | SMA-OK | RS-OK | -0.83% |
| [ETERNAL](https://in.tradingview.com/chart/?symbol=NSE:ETERNAL)<br><sub>✓ SAFE . ↗1228Cr · 616Cr . ↑CMF2d</sub> | 344.20 | 0.0% | +59.6% | 6d | SMA-OK | RS-OK | +0.16% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>✓ SAFE . ↘537Cr · 253Cr . ↑CMF30d</sub> | 1846.00 | -2.0% | +41.6% | 6d | SMA-OK | RS-OK | -0.22% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>✓ SAFE . →170Cr · 139Cr . ↑CMF2d</sub> | 1238.60 | -0.6% | +43.9% | 6d | SMA-OK | RS-OK | -0.55% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↗407Cr · 218Cr . ↑CMF6d</sub> | 900.00 | -0.7% | +102.5% | 6d | SMA-OK | RS-OK | -0.66% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↗145Cr · 178Cr . ↑CMF30d</sub> | 3158.90 | 0.0% | +97.8% | 6d | SMA-OK | RS-OK | +3.01% |
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP)<br><sub>✓ SAFE . →107Cr · 116Cr . ↑CMF5d</sub> | 1536.50 | -10.6% | +46.4% | 6d | SMA-OK | RS-OK | -3.99% |
| [AARTIPHARM](https://in.tradingview.com/chart/?symbol=NSE:AARTIPHARM)<br><sub>✓ SAFE . ↗77Cr · 62Cr . ↑CMF1d</sub> | 919.95 | -5.6% | +55.4% | 6d | SMA-OK | RS-OK | +3.50% |
| [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA)<br><sub>✓ SAFE . ↗29Cr · 43Cr . ↑CMF19d</sub> | 562.20 | 0.0% | +80.7% | 6d | SMA-OK | RS-OK | +2.99% |
| [SMSPHARMA](https://in.tradingview.com/chart/?symbol=NSE:SMSPHARMA)<br><sub>✓ SAFE . ↗45Cr · 34Cr . ↑CMF2d</sub> | 514.15 | 0.0% | +89.3% | 6d | SMA-OK | RS-OK | +1.98% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . ↗844Cr · 419Cr . ↑CMF6d</sub> | 1795.00 | 0.0% | +198.5% | 7d | SMA-OK | RS-OK | +1.15% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>✓ SAFE . ↗555Cr · 170Cr . ↑CMF6d</sub> | 3904.00 | -2.5% | +143.6% | 7d | SMA-OK | RS-OK | +0.29% |
| [SHREEPUSHK](https://in.tradingview.com/chart/?symbol=NSE:SHREEPUSHK)<br><sub>✓ SAFE . ↗15Cr · 69Cr . ↑CMF7d</sub> | 623.10 | 0.0% | +126.0% | 7d | SMA-OK | RS-OK | +9.33% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>✓ SAFE . ↘28Cr · 32Cr . ↓CMF10d</sub> | 1401.10 | -11.8% | +70.2% | 7d | SMA-OK | RS-OK | -2.96% |
| [CCAVENUE](https://in.tradingview.com/chart/?symbol=NSE:CCAVENUE)<br><sub>✓ SAFE . ↘19Cr · 30Cr . ↓CMF30d</sub> | 126.30 | -2.9% | +860.5% | 7d | SMA-OK | RS-OK | +1.62% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>✓ SAFE . ↗629Cr · 442Cr . ↑CMF7d</sub> | 822.90 | 0.0% | +44.1% | 8d | SMA-OK | RS-OK | +1.39% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>✓ SAFE . ↗93Cr · 75Cr . ↑CMF29d</sub> | 7395.50 | -0.2% | +173.5% | 8d | SMA-OK | RS-OK | +6.21% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>✓ SAFE . ↗122Cr · 45Cr . ↑CMF6d</sub> | 886.30 | 0.0% | +177.5% | 8d | SMA-OK | RS-OK | +0.84% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↘396Cr · 216Cr . ↑CMF19d</sub> | 1540.60 | -5.3% | +96.8% | 12d | SMA-OK | RS-OK | -0.35% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>✓ SAFE . ↗674Cr · 307Cr . ↑CMF5d</sub> | 2060.80 | -1.8% | +91.9% | 13d | SMA-OK | RS-OK | -1.82% |
| [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC)<br><sub>✓ SAFE . ↘49Cr · 36Cr . ↑CMF16d</sub> | 787.25 | -0.8% | +62.5% | 17d | SMA-OK | RS-OK | +0.29% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK)<br><sub>✓ SAFE . ↘105Cr · 49Cr . ↑CMF29d</sub> | 53.96 | -4.6% | +60.6% | 18d | SMA-OK | RS-OK | -1.01% |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL)<br><sub>✓ SAFE . →51Cr · 69Cr . ↑CMF15d</sub> | 1219.50 | -0.6% | +60.2% | 21d | SMA-OK | RS-OK | +2.39% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . →158Cr · 175Cr . ↑CMF30d</sub> | 1524.00 | 0.0% | +65.9% | 25d | SMA-OK | RS-OK | +0.75% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↘489Cr · 441Cr . ↑CMF29d</sub> | 338.50 | -7.5% | +602.3% | 26d | SMA-OK | RS-OK | -0.59% |
| [LOTUSDEV](https://in.tradingview.com/chart/?symbol=NSE:LOTUSDEV)<br><sub>✓ SAFE . ↗75Cr · 62Cr . ↑CMF30d</sub> | 240.70 | -3.0% | +134.1% | 26d | SMA-OK | RS-OK | -2.96% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS)<br><sub>✓ SAFE . →36Cr · 51Cr . ↓CMF0d</sub> | 800.00 | -10.1% | +173.3% | 32d | SMA-OK | RS-OK | +2.52% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . ↗119Cr · 106Cr . ↑CMF30d</sub> | 851.00 | -2.6% | +216.9% | 47d | SMA-OK | RS-OK | -2.59% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . →87Cr · 82Cr . ↓CMF4d</sub> | 66.71 | 0.0% | +175.7% | 47d | SMA-OK | RS-OK | +2.10% |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA)<br><sub>✓ SAFE . →53Cr · 36Cr . ↓CMF13d</sub> | 652.85 | -2.7% | +67.5% | 56d | SMA-OK | RS-OK | -2.71% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . →107Cr · 92Cr . ↓CMF4d . DEL33%(T-1)</sub> | 1172.30 | -9.9% | +264.2% | 57d | SMA-OK | RS-OK | +4.20% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . →152Cr · 235Cr . ↑CMF2d</sub> | 379.40 | 0.0% | +189.0% | 74d | SMA-OK | RS-OK | +0.05% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↗374Cr · 73Cr . ↑CMF21d</sub> | 512.55 | -3.7% | +200.7% | 76d | SMA-OK | RS-OK | +5.26% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . →212Cr · 333Cr . ↑CMF5d</sub> | 161.89 | 0.0% | +193.1% | 77d | SMA-OK | RS-OK | +2.49% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . →68Cr · 29Cr . ↑CMF7d</sub> | 399.20 | -4.5% | +83.4% | 84d | SMA-OK | RS-OK | -0.61% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . ↗629Cr · 700Cr . ↑CMF5d</sub> | 2350.00 | -2.3% | +152.6% | 123d | SMA-OK | RS-OK | -2.31% |

### By Trend Age

**<2 WEEKS** (51)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AARTIDRUGS,NSE:AARTIPHARM,NSE:ACUTAAS,NSE:ADANIPORTS,NSE:ALIVUS,NSE:APOLLO,NSE:ARFIN,NSE:ATHERENERG,NSE:AUROPHARMA,NSE:BEML,NSE:BOSCHLTD,NSE:CCAVENUE,NSE:CPPLUS,NSE:DIACABS,NSE:DIVISLAB,NSE:EBGNG,NSE:EMCURE,NSE:ENGINERSIN,NSE:ETERNAL,NSE:GABRIEL,NSE:GAIL,NSE:GESHIP,NSE:GLAND,NSE:GLENMARK,NSE:GRWRHITECH,NSE:HAL,NSE:INDGN,NSE:INDHOTEL,NSE:IPCALAB,NSE:LALPATHLAB,NSE:MCX,NSE:MINDACORP,NSE:NAVINFLUOR,NSE:NITINSPIN,NSE:NUVAMA,NSE:NYKAA,NSE:PHOENIXLTD,NSE:PPLPHARMA,NSE:PRINCEPIPE,NSE:RML,NSE:RUBICON,NSE:SAILIFE,NSE:SANSERA,NSE:SAREGAMA,NSE:SGMART,NSE:SHREEPUSHK,NSE:SMSPHARMA,NSE:SONACOMS,NSE:TECHM,NSE:WELSPUNLIV,NSE:ZYDUSLIFE
```

**2-4 WEEKS** (6)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CHENNPETRO,NSE:COFORGE,NSE:HFCL,NSE:SHYAMMETL,NSE:SOUTHBANK,NSE:TIPSMUSIC
```

**1-2 MONTHS** (5)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CUPID,NSE:LOTUSDEV,NSE:OPTIEMUS,NSE:PVRINOX,NSE:STLTECH
```

**2-3 MONTHS** (4)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:RAYMOND,NSE:SBC,NSE:SHREEJISPG,NSE:THELEELA
```

**3-6 MONTHS** (5)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:LAURUSLABS,NSE:NAZARA,NSE:RATNAVEER,NSE:SSWL,NSE:TFCILTD
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
