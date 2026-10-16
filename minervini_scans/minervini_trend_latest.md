> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-10-16
*Generated 2026-10-16 15:48 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [AARTIPHARM](https://in.tradingview.com/chart/?symbol=NSE:AARTIPHARM) | [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL) |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX) | [ARFIN](https://in.tradingview.com/chart/?symbol=NSE:ARFIN) |
| [AXISCADES](https://in.tradingview.com/chart/?symbol=NSE:AXISCADES) | [ARIS](https://in.tradingview.com/chart/?symbol=NSE:ARIS) |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE) | [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA) |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE) | [BLUSPRING](https://in.tradingview.com/chart/?symbol=NSE:BLUSPRING) |
| [DELTACORP](https://in.tradingview.com/chart/?symbol=NSE:DELTACORP) | [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO) |
| [FEDFINA](https://in.tradingview.com/chart/?symbol=NSE:FEDFINA) | [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN) |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE) | [ENRIN](https://in.tradingview.com/chart/?symbol=NSE:ENRIN) |
| [JTLIND](https://in.tradingview.com/chart/?symbol=NSE:JTLIND) | [JGCHEM](https://in.tradingview.com/chart/?symbol=NSE:JGCHEM) |
| [NITINSPIN](https://in.tradingview.com/chart/?symbol=NSE:NITINSPIN) | [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX) |
| [OCCLLTD](https://in.tradingview.com/chart/?symbol=NSE:OCCLLTD) | [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT) |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER) | [PHOENIXLTD](https://in.tradingview.com/chart/?symbol=NSE:PHOENIXLTD) |
| [RPEL](https://in.tradingview.com/chart/?symbol=NSE:RPEL) | [PREMEXPLN](https://in.tradingview.com/chart/?symbol=NSE:PREMEXPLN) |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA) | [UTTAMSUGAR](https://in.tradingview.com/chart/?symbol=NSE:UTTAMSUGAR) |
| [SGFIN](https://in.tradingview.com/chart/?symbol=NSE:SGFIN) |  |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART) |  |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON) |  |
| [SMSPHARMA](https://in.tradingview.com/chart/?symbol=NSE:SMSPHARMA) |  |
| [SOLARA](https://in.tradingview.com/chart/?symbol=NSE:SOLARA) |  |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL) |  |
| [TBZ](https://in.tradingview.com/chart/?symbol=NSE:TBZ) |  |
| [YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH) |  |

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

**Qualifying: 92**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:63MOONS,NSE:AARTIIND,NSE:AARTIPHARM,NSE:ADANIGREEN,NSE:AEROFLEX,NSE:APOLLO,NSE:AURUM,NSE:AXISCADES,NSE:BALRAMCHIN,NSE:BBOX,NSE:BHEL,NSE:CARTRADE,NSE:COFORGE,NSE:CRAFTSMAN,NSE:DELTACORP,NSE:EDELWEISS,NSE:FEDFINA,NSE:GRAPHITE,NSE:HAL,NSE:JAYNECOIND,NSE:JINDALSAW,NSE:JTLIND,NSE:KARURVYSYA,NSE:KROSS,NSE:KTKBANK,NSE:NITINSPIN,NSE:NYKAA,NSE:PAYTM,NSE:PNBHOUSING,NSE:QPOWER,NSE:RAIN,NSE:SANSERA,NSE:SGFIN,NSE:SGMART,NSE:SHRIPISTON,NSE:SHYAMMETL,NSE:SOLARA,NSE:SOLARINDS,NSE:SOUTHBANK,NSE:STYLEBAAZA,NSE:TIPSMUSIC,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ADANIPORTS,NSE:AEGISLOG,NSE:CPPLUS,NSE:CUPID,NSE:HFCL,NSE:LLOYDSENGG,NSE:OCCLLTD,NSE:OPTIEMUS,NSE:PVRINOX,NSE:RAYMONDREL,NSE:REDINGTON,NSE:SMSPHARMA,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:DIACABS,NSE:MOTILALOFS,NSE:OAL,NSE:ORIENTHOT,NSE:PAISALO,NSE:PTCIL,NSE:RPEL,NSE:SBC,NSE:SHREEJISPG,NSE:STLTECH,NSE:TBZ,NSE:YATHARTH,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:CYIENTDLM,NSE:DYNAMATECH,NSE:EBGNG,NSE:FCL,NSE:FINCABLES,NSE:MANINDS,NSE:MARINE,NSE:MOREPENLAB,NSE:MTARTECH,NSE:NEOGEN,NSE:RATNAVEER,NSE:RAYMOND,NSE:SAMBHV,NSE:SHANTIGOLD,NSE:SYRMA,NSE:THELEELA,NSE:WELSPUNLIV,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:GLAND,NSE:IOLCP,NSE:KMEW,NSE:LAURUSLABS,NSE:NAZARA,NSE:SSWL,NSE:TFCILTD,NSE:WELCORP,NSE:WSTCSTPAPR,###6+ MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:SKYGOLD
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [ADANIGREEN](https://in.tradingview.com/chart/?symbol=NSE:ADANIGREEN)<br><sub>✓ SAFE . ↗421Cr · 123Cr . ↓CMF9d</sub> | 1303.00 | -18.8% | +68.6% | 0d | SMA-OK | RS-OK | -1.17% |
| [JINDALSAW](https://in.tradingview.com/chart/?symbol=NSE:JINDALSAW)<br><sub>✓ SAFE . ↗52Cr · 108Cr . ↑CMF3d</sub> | 301.55 | -5.0% | +95.0% | 0d | SMA-OK | RS-OK | +0.84% |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON)<br><sub>✓ SAFE . ↘31Cr · 78Cr . ↓CMF10d</sub> | 4629.90 | -2.5% | +78.4% | 0d | SMA-OK | RS-OK | +6.68% |
| [AARTIIND](https://in.tradingview.com/chart/?symbol=NSE:AARTIIND)<br><sub>⚠ CAUTION . ↗42Cr · 67Cr . ↑CMF3d . DEL67%(T-1)</sub> | 503.00 | -7.4% | +47.9% | 0d | SMA-OK | RS-OK | -0.63% |
| [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS)<br><sub>✓ SAFE . ↗64Cr · 47Cr . ↓CMF15d</sub> | 919.60 | -1.3% | +95.5% | 0d | SMA-OK | RS-OK | +0.94% |
| [FEDFINA](https://in.tradingview.com/chart/?symbol=NSE:FEDFINA)<br><sub>✓ SAFE . ↗24Cr · 28Cr . ↑CMF4d</sub> | 161.86 | -8.2% | +34.0% | 0d | SMA-OK | RS-OK | +3.17% |
| [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN)<br><sub>✓ SAFE . →51Cr · 25Cr . ↑CMF2d</sub> | 10960.00 | -7.5% | +70.0% | 0d | SMA-OK | RS-OK | +0.04% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>✓ SAFE . ↗454Cr · 404Cr . ↓CMF1d</sub> | 1951.90 | -3.1% | +81.8% | 1d | SMA-OK | RS-OK | +0.87% |
| [SOLARA](https://in.tradingview.com/chart/?symbol=NSE:SOLARA)<br><sub>✓ SAFE . ↗53Cr · 397Cr . ↓CMF9d</sub> | 696.70 | -7.5% | +63.7% | 1d | SMA-OK | RS-OK | +7.52% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>✓ SAFE . ↗203Cr · 147Cr . ↓CMF2d</sub> | 525.80 | -8.3% | +231.1% | 1d | SMA-OK | RS-OK | +3.71% |
| [JTLIND](https://in.tradingview.com/chart/?symbol=NSE:JTLIND)<br><sub>✓ SAFE . ↗38Cr · 142Cr . ↓CMF6d . DEL54%(T-1)</sub> | 87.33 | -5.5% | +114.0% | 1d | SMA-OK | RS-OK | +4.69% |
| [CARTRADE](https://in.tradingview.com/chart/?symbol=NSE:CARTRADE)<br><sub>✓ SAFE . ↗109Cr · 102Cr . ↑CMF0d</sub> | 3011.40 | -7.9% | +85.5% | 1d | SMA-OK | RS-OK | +1.94% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↘80Cr · 78Cr . ↑CMF30d</sub> | 4120.70 | -11.6% | +187.7% | 1d | SMA-OK | RS-OK | +1.75% |
| [DELTACORP](https://in.tradingview.com/chart/?symbol=NSE:DELTACORP)<br><sub>✓ SAFE . →185Cr · 39Cr . ↑CMF9d</sub> | 81.04 | -5.1% | +64.2% | 1d | SMA-OK | RS-OK | +2.26% |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE)<br><sub>✓ SAFE . ↘80Cr · 34Cr . ↓CMF2d</sub> | 770.25 | -9.5% | +46.4% | 1d | SMA-OK | RS-OK | +1.08% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>✓ SAFE . ↗21Cr · 31Cr . ↓CMF27d</sub> | 798.20 | -5.2% | +149.9% | 1d | SMA-OK | RS-OK | +5.58% |
| [AARTIPHARM](https://in.tradingview.com/chart/?symbol=NSE:AARTIPHARM)<br><sub>✓ SAFE . ↘47Cr · 27Cr . ↑CMF0d</sub> | 873.65 | -10.4% | +47.6% | 1d | SMA-OK | RS-OK | +0.77% |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER)<br><sub>✓ SAFE . →45Cr · 27Cr . ↓CMF1d</sub> | 1454.30 | -11.8% | +144.4% | 1d | SMA-OK | RS-OK | +1.34% |
| [HAL](https://in.tradingview.com/chart/?symbol=NSE:HAL)<br><sub>✓ SAFE . →310Cr · 386Cr . ↓CMF28d</sub> | 4908.00 | -3.7% | +40.7% | 3d | SMA-OK | RS-OK | -0.51% |
| [STYLEBAAZA](https://in.tradingview.com/chart/?symbol=NSE:STYLEBAAZA)<br><sub>✓ SAFE . ↘45Cr · 155Cr . ↓CMF1d</sub> | 399.50 | -9.1% | +68.5% | 3d | SMA-OK | RS-OK | +3.52% |
| [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM)<br><sub>✓ SAFE . ↗877Cr · 454Cr . ↑CMF30d</sub> | 1706.40 | -7.8% | +77.9% | 4d | SMA-OK | RS-OK | -0.35% |
| [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS)<br><sub>✓ SAFE . →51Cr · 45Cr . ↑CMF27d</sub> | 272.00 | -2.4% | +71.8% | 4d | SMA-OK | RS-OK | +0.74% |
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO)<br><sub>✓ SAFE . →306Cr · 606Cr . ↑CMF2d</sub> | 429.00 | -4.7% | +135.5% | 5d | SMA-OK | RS-OK | +2.79% |
| [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC)<br><sub>✓ SAFE . ↗77Cr · 334Cr . ↑CMF4d</sub> | 746.90 | 0.0% | +54.2% | 5d | SMA-OK | RS-OK | +8.80% |
| [SOLARINDS](https://in.tradingview.com/chart/?symbol=NSE:SOLARINDS)<br><sub>✓ SAFE . ↘314Cr · 262Cr . ↓CMF18d</sub> | 19996.00 | -11.0% | +69.9% | 5d | SMA-OK | RS-OK | -0.86% |
| [JAYNECOIND](https://in.tradingview.com/chart/?symbol=NSE:JAYNECOIND)<br><sub>✓ SAFE . ↗48Cr · 174Cr . ↑CMF3d</sub> | 100.62 | -12.7% | +51.8% | 5d | SMA-OK | RS-OK | +4.05% |
| [EDELWEISS](https://in.tradingview.com/chart/?symbol=NSE:EDELWEISS)<br><sub>✓ SAFE . ↘44Cr · 37Cr . ↓CMF8d</sub> | 134.84 | -5.5% | +35.3% | 5d | SMA-OK | RS-OK | +0.45% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>✓ SAFE . ↗158Cr · 638Cr . ↑CMF1d</sub> | 355.65 | 0.0% | +57.0% | 6d | SMA-OK | RS-OK | +2.49% |
| [SGFIN](https://in.tradingview.com/chart/?symbol=NSE:SGFIN)<br><sub>✓ SAFE . ↗73Cr · 278Cr . ↑CMF11d</sub> | 676.70 | -4.7% | +103.7% | 6d | SMA-OK | RS-OK | -2.21% |
| [SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK)<br><sub>✓ SAFE . ↗111Cr · 189Cr . ↑CMF17d</sub> | 51.45 | -0.1% | +57.6% | 6d | SMA-OK | RS-OK | -0.10% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . ↗190Cr · 92Cr . ↑CMF3d</sub> | 345.00 | -1.3% | +47.0% | 6d | SMA-OK | RS-OK | +2.37% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>✓ SAFE . →58Cr · 78Cr . ↑CMF5d</sub> | 329.85 | -3.8% | +91.9% | 6d | SMA-OK | RS-OK | -1.60% |
| [RAIN](https://in.tradingview.com/chart/?symbol=NSE:RAIN)<br><sub>✓ SAFE . ↗106Cr · 72Cr . ↑CMF7d</sub> | 228.55 | -5.9% | +125.2% | 6d | SMA-OK | RS-OK | +1.62% |
| [NITINSPIN](https://in.tradingview.com/chart/?symbol=NSE:NITINSPIN)<br><sub>✓ SAFE . ↗9Cr · 36Cr . ↑CMF0d</sub> | 653.85 | -0.2% | +114.1% | 6d | SMA-OK | RS-OK | +5.38% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>✓ SAFE . ↗111Cr · 55Cr . ↑CMF3d</sub> | 1167.70 | -4.7% | +55.5% | 7d | SMA-OK | RS-OK | -1.16% |
| [AURUM](https://in.tradingview.com/chart/?symbol=NSE:AURUM)<br><sub>✓ SAFE . ↗37Cr · 216Cr . ↓CMF3d</sub> | 232.37 | -7.4% | +50.0% | 9d | SMA-OK | RS-OK | -2.37% |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL)<br><sub>✓ SAFE . ↘53Cr · 115Cr . ↑CMF3d</sub> | 1198.50 | 0.0% | +57.4% | 9d | SMA-OK | RS-OK | +3.51% |
| [AXISCADES](https://in.tradingview.com/chart/?symbol=NSE:AXISCADES)<br><sub>✓ SAFE . ↘38Cr · 44Cr . ↑CMF30d</sub> | 2116.00 | -8.3% | +92.2% | 9d | SMA-OK | RS-OK | +4.84% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>✓ SAFE . ↗724Cr · 1018Cr . ↑CMF30d</sub> | 433.10 | -6.7% | +87.5% | 10d | SMA-OK | RS-OK | -6.66% |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>✓ SAFE . →100Cr · 98Cr . ↓CMF0d . DEL45%(T-1)</sub> | 721.15 | -6.0% | +81.3% | 10d | SMA-OK | RS-OK | +0.15% |
| [BBOX](https://in.tradingview.com/chart/?symbol=NSE:BBOX)<br><sub>✓ SAFE . ↗158Cr · 74Cr . ↓CMF1d</sub> | 907.25 | -15.9% | +102.9% | 10d | SMA-OK | RS-OK | +4.04% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>✓ SAFE . ↗172Cr · 112Cr . ↑CMF29d</sub> | 1366.70 | -8.2% | +132.5% | 13d | SMA-OK | RS-OK | -2.93% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . ↗145Cr · 91Cr . ↑CMF22d</sub> | 1401.00 | -0.2% | +52.5% | 13d | SMA-OK | RS-OK | +1.10% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↘775Cr · 544Cr . ↑CMF17d</sub> | 353.70 | -3.4% | +657.4% | 14d | SMA-OK | RS-OK | +0.67% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>✓ SAFE . ↘129Cr · 294Cr . ↑CMF15d</sub> | 96.37 | -5.7% | +155.4% | 15d | SMA-OK | RS-OK | +5.21% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . ↗194Cr · 113Cr . ↑CMF3d</sub> | 4063.60 | -8.5% | +209.3% | 15d | SMA-OK | RS-OK | -0.26% |
| [SMSPHARMA](https://in.tradingview.com/chart/?symbol=NSE:SMSPHARMA)<br><sub>✓ SAFE . ↘18Cr · 33Cr . ↑CMF3d</sub> | 450.50 | -6.8% | +65.9% | 15d | SMA-OK | RS-OK | +5.75% |
| [RAYMONDREL](https://in.tradingview.com/chart/?symbol=NSE:RAYMONDREL)<br><sub>✓ SAFE . ↘73Cr · 32Cr . ↑CMF17d . DEL43%(T-1)</sub> | 652.55 | -9.7% | +82.6% | 15d | SMA-OK | RS-OK | +0.91% |
| [OCCLLTD](https://in.tradingview.com/chart/?symbol=NSE:OCCLLTD)<br><sub>↗8Cr · 29Cr . ↑CMF14d</sub> | 195.03 | -16.3% | +150.7% | 16d | SMA-OK | RS-OK | -14.46% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>✓ SAFE . ↗729Cr · 383Cr . ↑CMF22d</sub> | 1746.60 | -7.3% | +34.0% | 17d | SMA-OK | RS-OK | -0.12% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [REDINGTON](https://in.tradingview.com/chart/?symbol=NSE:REDINGTON)<br><sub>✓ SAFE . →152Cr · 193Cr . ↓CMF2d</sub> | 383.50 | -7.1% | +91.8% | 20d | SMA-OK | RS-OK | -2.17% |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS)<br><sub>✓ SAFE . ↘129Cr · 48Cr . ↑CMF30d</sub> | 788.65 | -11.4% | +169.4% | 20d | SMA-OK | RS-OK | +3.93% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>✓ SAFE . ↗91Cr · 31Cr . ↑CMF7d</sub> | 24680.00 | -4.0% | +67.6% | 22d | SMA-OK | RS-OK | -1.83% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [MOTILALOFS](https://in.tradingview.com/chart/?symbol=NSE:MOTILALOFS)<br><sub>✓ SAFE . →95Cr · 64Cr . ↑CMF8d</sub> | 1057.60 | -3.1% | +68.4% | 28d | SMA-OK | RS-OK | -0.43% |
| [TBZ](https://in.tradingview.com/chart/?symbol=NSE:TBZ)<br><sub>✓ SAFE . ↘113Cr · 59Cr . ↑CMF19d</sub> | 665.35 | 0.0% | +496.7% | 29d | SMA-OK | RS-OK | +4.99% |
| [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO)<br><sub>✓ SAFE . ↘81Cr · 67Cr . ↑CMF0d</sub> | 81.50 | -12.8% | +163.2% | 30d | SMA-OK | RS-OK | +0.75% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . ↗127Cr · 83Cr . ↓CMF0d</sub> | 63.33 | -1.4% | +174.3% | 35d | SMA-OK | RS-OK | -1.43% |
| [OAL](https://in.tradingview.com/chart/?symbol=NSE:OAL)<br><sub>✓ SAFE . ↗28Cr · 69Cr . ↑CMF3d</sub> | 629.55 | 0.0% | +167.4% | 35d | SMA-OK | RS-OK | +7.52% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . ↗83Cr · 65Cr . ↑CMF30d</sub> | 840.00 | 0.0% | +260.2% | 35d | SMA-OK | RS-OK | +0.60% |
| [ORIENTHOT](https://in.tradingview.com/chart/?symbol=NSE:ORIENTHOT)<br><sub>✓ SAFE . ↗13Cr · 55Cr . ↑CMF3d</sub> | 151.80 | 0.0% | +85.1% | 35d | SMA-OK | RS-OK | +3.97% |
| [YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH)<br><sub>✓ SAFE . ↘36Cr · 25Cr . ↓CMF0d</sub> | 992.10 | -14.6% | +80.1% | 35d | SMA-OK | RS-OK | +0.73% |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS)<br><sub>✓ SAFE . ↗363Cr · 101Cr . ↑CMF9d</sub> | 322.85 | -4.3% | +173.7% | 37d | SMA-OK | RS-OK | -0.35% |
| [RPEL](https://in.tradingview.com/chart/?symbol=NSE:RPEL)<br><sub>✓ SAFE . ↗20Cr · 27Cr . ↑CMF0d</sub> | 1811.50 | -3.9% | +219.8% | 37d | SMA-OK | RS-OK | +2.67% |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA)<br><sub>✓ SAFE . ↗51Cr · 48Cr . ↓CMF1d</sub> | 616.30 | 0.0% | +58.2% | 44d | SMA-OK | RS-OK | +4.65% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>✓ SAFE . ↗84Cr · 343Cr . ↑CMF7d</sub> | 897.25 | -13.6% | +229.5% | 45d | SMA-OK | RS-OK | -13.03% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>✓ SAFE . ↘52Cr · 122Cr . ↑CMF20d</sub> | 172.47 | 0.0% | +109.6% | 45d | SMA-OK | RS-OK | +5.23% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↘139Cr · 58Cr . ↑CMF3d . DEL23%(T-1)</sub> | 1133.90 | -12.8% | +252.3% | 45d | SMA-OK | RS-OK | +0.75% |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>✓ SAFE . ↗57Cr · 45Cr . ↓CMF0d</sub> | 2484.80 | -7.6% | +153.6% | 45d | SMA-OK | RS-OK | -0.96% |
| [FINCABLES](https://in.tradingview.com/chart/?symbol=NSE:FINCABLES)<br><sub>✓ SAFE . ↘58Cr · 37Cr . ↑CMF27d</sub> | 1367.70 | -7.8% | +92.4% | 45d | SMA-OK | RS-OK | -1.26% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>✓ SAFE . →45Cr · 29Cr . ↓CMF0d</sub> | 708.05 | -3.2% | +191.9% | 45d | SMA-OK | RS-OK | +1.73% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>✓ SAFE . ↘34Cr · 26Cr . ↑CMF30d</sub> | 865.35 | -15.2% | +178.7% | 45d | SMA-OK | RS-OK | +2.40% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↘73Cr · 87Cr . ↓CMF0d</sub> | 219.30 | -8.3% | +102.5% | 46d | SMA-OK | RS-OK | +0.64% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>✓ SAFE . ↘187Cr · 249Cr . ↑CMF17d</sub> | 423.30 | 0.0% | +170.3% | 47d | SMA-OK | RS-OK | +9.38% |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE)<br><sub>↘72Cr · 35Cr . ↑CMF30d</sub> | 429.00 | -10.4% | +182.8% | 47d | SMA-OK | RS-OK | -3.13% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↗253Cr · 230Cr . ↑CMF30d</sub> | 129.55 | -11.9% | +284.6% | 48d | SMA-OK | RS-OK | -5.13% |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH)<br><sub>✓ SAFE . ↘35Cr · 27Cr . ↑CMF25d</sub> | 13774.00 | -4.5% | +79.4% | 50d | SMA-OK | RS-OK | +0.17% |
| [FCL](https://in.tradingview.com/chart/?symbol=NSE:FCL)<br><sub>✓ SAFE . ↗150Cr · 100Cr . ↓CMF0d</sub> | 57.25 | -5.3% | +197.6% | 52d | SMA-OK | RS-OK | -1.24% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>✓ SAFE . ↘155Cr · 157Cr . ↓CMF0d . DEL42%(T-1)</sub> | 1604.60 | -10.0% | +150.7% | 55d | SMA-OK | RS-OK | -5.00% |
| [MTARTECH](https://in.tradingview.com/chart/?symbol=NSE:MTARTECH)<br><sub>✓ SAFE . ↗2251Cr · 944Cr . ↑CMF8d</sub> | 7777.00 | -7.1% | +457.1% | 58d | SMA-OK | RS-OK | -4.25% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . ↘148Cr · 164Cr . ↑CMF0d</sub> | 342.90 | -0.7% | +161.2% | 62d | SMA-OK | RS-OK | +3.94% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↘42Cr · 26Cr . ↑CMF9d</sub> | 418.10 | -1.6% | +145.3% | 64d | SMA-OK | RS-OK | +2.74% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . →207Cr · 102Cr . ↓CMF21d</sub> | 155.69 | -3.2% | +181.8% | 65d | SMA-OK | RS-OK | -1.37% |
| [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP)<br><sub>✓ SAFE . →58Cr · 36Cr . ↓CMF1d</sub> | 194.69 | -11.6% | +185.4% | 68d | SMA-OK | RS-OK | -0.13% |
| [WSTCSTPAPR](https://in.tradingview.com/chart/?symbol=NSE:WSTCSTPAPR)<br><sub>✓ SAFE . ↗146Cr · 221Cr . ↑CMF26d</sub> | 840.00 | -10.7% | +120.3% | 70d | SMA-OK | RS-OK | +1.82% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . →108Cr · 50Cr . ↑CMF30d</sub> | 3043.40 | -3.4% | +90.6% | 71d | SMA-OK | RS-OK | -0.93% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . ↗80Cr · 75Cr . ↑CMF0d</sub> | 418.15 | 0.0% | +92.1% | 72d | SMA-OK | RS-OK | +3.25% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>✓ SAFE . →47Cr · 34Cr . ↑CMF14d</sub> | 3327.70 | -0.5% | +202.7% | 90d | SMA-OK | RS-OK | +3.00% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>✓ SAFE . ↘372Cr · 438Cr . ↑CMF30d</sub> | 2571.50 | -9.5% | +256.2% | 112d | SMA-OK | RS-OK | +3.61% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . →281Cr · 165Cr . ↑CMF1d</sub> | 2020.00 | -2.4% | +131.4% | 112d | SMA-OK | RS-OK | -0.83% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . ↗250Cr · 268Cr . ↑CMF6d</sub> | 1060.60 | 0.0% | +251.8% | 129d | SMA-OK | RS-OK | +5.18% |

### By Trend Age

**<2 WEEKS** (41)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:63MOONS,NSE:AARTIIND,NSE:AARTIPHARM,NSE:ADANIGREEN,NSE:AEROFLEX,NSE:APOLLO,NSE:AURUM,NSE:AXISCADES,NSE:BALRAMCHIN,NSE:BBOX,NSE:BHEL,NSE:CARTRADE,NSE:COFORGE,NSE:CRAFTSMAN,NSE:DELTACORP,NSE:EDELWEISS,NSE:FEDFINA,NSE:GRAPHITE,NSE:HAL,NSE:JAYNECOIND,NSE:JINDALSAW,NSE:JTLIND,NSE:KARURVYSYA,NSE:KROSS,NSE:KTKBANK,NSE:NITINSPIN,NSE:NYKAA,NSE:PAYTM,NSE:PNBHOUSING,NSE:QPOWER,NSE:RAIN,NSE:SANSERA,NSE:SGFIN,NSE:SGMART,NSE:SHRIPISTON,NSE:SHYAMMETL,NSE:SOLARA,NSE:SOLARINDS,NSE:SOUTHBANK,NSE:STYLEBAAZA,NSE:TIPSMUSIC
```

**2-4 WEEKS** (12)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ADANIPORTS,NSE:AEGISLOG,NSE:CPPLUS,NSE:CUPID,NSE:HFCL,NSE:LLOYDSENGG,NSE:OCCLLTD,NSE:OPTIEMUS,NSE:PVRINOX,NSE:RAYMONDREL,NSE:REDINGTON,NSE:SMSPHARMA
```

**1-2 MONTHS** (12)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:DIACABS,NSE:MOTILALOFS,NSE:OAL,NSE:ORIENTHOT,NSE:PAISALO,NSE:PTCIL,NSE:RPEL,NSE:SBC,NSE:SHREEJISPG,NSE:STLTECH,NSE:TBZ,NSE:YATHARTH
```

**2-3 MONTHS** (17)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CYIENTDLM,NSE:DYNAMATECH,NSE:EBGNG,NSE:FCL,NSE:FINCABLES,NSE:MANINDS,NSE:MARINE,NSE:MOREPENLAB,NSE:MTARTECH,NSE:NEOGEN,NSE:RATNAVEER,NSE:RAYMOND,NSE:SAMBHV,NSE:SHANTIGOLD,NSE:SYRMA,NSE:THELEELA,NSE:WELSPUNLIV
```

**3-6 MONTHS** (9)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:GLAND,NSE:IOLCP,NSE:KMEW,NSE:LAURUSLABS,NSE:NAZARA,NSE:SSWL,NSE:TFCILTD,NSE:WELCORP,NSE:WSTCSTPAPR
```

**6+ MONTHS** (1)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:SKYGOLD
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
