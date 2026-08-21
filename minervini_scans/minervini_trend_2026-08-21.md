> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-08-21
*Generated 2026-08-21 15:45 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [AEROENTER](https://in.tradingview.com/chart/?symbol=NSE:AEROENTER) | [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS) |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER) | [APOLLOPIPE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOPIPE) |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM) | [ASIANENE](https://in.tradingview.com/chart/?symbol=NSE:ASIANENE) |
| [BEPL](https://in.tradingview.com/chart/?symbol=NSE:BEPL) | [BLISSGVS](https://in.tradingview.com/chart/?symbol=NSE:BLISSGVS) |
| [BLUSPRING](https://in.tradingview.com/chart/?symbol=NSE:BLUSPRING) | [BLSE](https://in.tradingview.com/chart/?symbol=NSE:BLSE) |
| [DCBBANK](https://in.tradingview.com/chart/?symbol=NSE:DCBBANK) | [DREDGECORP](https://in.tradingview.com/chart/?symbol=NSE:DREDGECORP) |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL) | [EQUITASBNK](https://in.tradingview.com/chart/?symbol=NSE:EQUITASBNK) |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN) | [GOKULAGRO](https://in.tradingview.com/chart/?symbol=NSE:GOKULAGRO) |
| [EXIDEIND](https://in.tradingview.com/chart/?symbol=NSE:EXIDEIND) | [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA) |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL) | [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB) |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA) | [LLOYDSENT](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENT) |
| [GRANULES](https://in.tradingview.com/chart/?symbol=NSE:GRANULES) | [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH) |
| [IDEAFORGE](https://in.tradingview.com/chart/?symbol=NSE:IDEAFORGE) | [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE) |
| [JINDALSAW](https://in.tradingview.com/chart/?symbol=NSE:JINDALSAW) | [MINDACORP](https://in.tradingview.com/chart/?symbol=NSE:MINDACORP) |
| [JSFB](https://in.tradingview.com/chart/?symbol=NSE:JSFB) | [MUFIN](https://in.tradingview.com/chart/?symbol=NSE:MUFIN) |
| [JTLIND](https://in.tradingview.com/chart/?symbol=NSE:JTLIND) | [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA) |
| [KABRAEXTRU](https://in.tradingview.com/chart/?symbol=NSE:KABRAEXTRU) | [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND) |
| [KDDL](https://in.tradingview.com/chart/?symbol=NSE:KDDL) | [RPTECH](https://in.tradingview.com/chart/?symbol=NSE:RPTECH) |
| [MANAPPURAM](https://in.tradingview.com/chart/?symbol=NSE:MANAPPURAM) | [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV) |
| [MIDHANI](https://in.tradingview.com/chart/?symbol=NSE:MIDHANI) | [SEAMECLTD](https://in.tradingview.com/chart/?symbol=NSE:SEAMECLTD) |
| [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO) | [WABAG](https://in.tradingview.com/chart/?symbol=NSE:WABAG) |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY) |  |
| [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS) |  |
| [SMLMAH](https://in.tradingview.com/chart/?symbol=NSE:SMLMAH) |  |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL) |  |
| [STYLAMIND](https://in.tradingview.com/chart/?symbol=NSE:STYLAMIND) |  |
| [TATATECH](https://in.tradingview.com/chart/?symbol=NSE:TATATECH) |  |
| [TBZ](https://in.tradingview.com/chart/?symbol=NSE:TBZ) |  |
| [VADILALIND](https://in.tradingview.com/chart/?symbol=NSE:VADILALIND) |  |
| [VIYASH](https://in.tradingview.com/chart/?symbol=NSE:VIYASH) |  |
| [WELENT](https://in.tradingview.com/chart/?symbol=NSE:WELENT) |  |

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

**Qualifying: 138**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ACMESOLAR,NSE:AEROENTER,NSE:AEROFLEX,NSE:AVADHSUGAR,NSE:BHEL,NSE:BLUSPRING,NSE:BOSCHLTD,NSE:CARBORUNIV,NSE:CYIENTDLM,NSE:DALMIASUG,NSE:DATAPATTNS,NSE:DCBBANK,NSE:DEEPINDS,NSE:DHAMPURSUG,NSE:EBGNG,NSE:EDELWEISS,NSE:ELGIEQUIP,NSE:EMIL,NSE:ENGINERSIN,NSE:ENRIN,NSE:EPL,NSE:EXIDEIND,NSE:FINCABLES,NSE:GABRIEL,NSE:GRANULES,NSE:HFCL,NSE:HINDALCO,NSE:ICIL,NSE:IDEAFORGE,NSE:IFCI,NSE:INDOBORAX,NSE:IPCALAB,NSE:JAYNECOIND,NSE:JINDALSAW,NSE:JINDRILL,NSE:JSFB,NSE:JSWINFRA,NSE:JTLIND,NSE:KEI,NSE:KENNAMET,NSE:MANAPPURAM,NSE:MANGLMCEM,NSE:MANINDS,NSE:MCX,NSE:MIDHANI,NSE:NEOGEN,NSE:PIDILITIND,NSE:PNBHOUSING,NSE:POWERINDIA,NSE:RATEGAIN,NSE:RBA,NSE:ROLEXRINGS,NSE:SHAILY,NSE:SHANTIGOLD,NSE:SHRIRAMFIN,NSE:SKIPPER,NSE:TATATECH,NSE:TBZ,NSE:TDPOWERSYS,NSE:THELEELA,NSE:TVSMOTOR,NSE:VADILALIND,NSE:VIYASH,NSE:VOLTAMP,NSE:WELENT,NSE:WELSPUNLIV,NSE:ZENTEC,NSE:ZYDUSLIFE,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABB,NSE:ANTHEM,NSE:APARINDS,NSE:AUBANK,NSE:AUROPHARMA,NSE:AVALON,NSE:BEPL,NSE:DIVISLAB,NSE:EICHERMOT,NSE:FLUOROCHEM,NSE:GAEL,NSE:HEG,NSE:MARKSANS,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:NAVINFLUOR,NSE:NESTLEIND,NSE:NETWEB,NSE:OFSS,NSE:RBLBANK,NSE:RKFORGE,NSE:SBCL,NSE:SIEMENS,NSE:SMLMAH,NSE:SOLARINDS,NSE:SYRMA,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AARTIIND,NSE:AEGISLOG,NSE:AETHER,NSE:ATHERENERG,NSE:AZAD,NSE:BALRAMCHIN,NSE:CHENNPETRO,NSE:GLAND,NSE:IOLCP,NSE:KABRAEXTRU,NSE:KDDL,NSE:KTKBANK,NSE:LLOYDSENGG,NSE:MANORAMA,NSE:RATNAVEER,NSE:SHILPAMED,NSE:SIGMAADV,NSE:SSWL,NSE:STLTECH,NSE:SUVEN,NSE:TFCILTD,NSE:TITAN,NSE:UJJIVANSFB,NSE:YASHO,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:FEDERALBNK,NSE:GNA,NSE:MTARTECH,NSE:NYKAA,NSE:SHRIPISTON,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:CUPID,NSE:HONASA,NSE:LAURUSLABS,NSE:PAISALO,NSE:PARAS,NSE:RADICO,NSE:RISHABH,NSE:RRKABEL,NSE:SAILIFE,NSE:SANSERA,NSE:SJS,NSE:SKYGOLD,NSE:SONACOMS,NSE:STYLAMIND,NSE:WELCORP
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [WELENT](https://in.tradingview.com/chart/?symbol=NSE:WELENT)<br><sub>✓ SAFE . ↗51Cr · 357Cr . ↑CMF0d</sub> | 631.45 | 0.0% | +51.9% | 0d | SMA-OK | RS-OK | +8.00% |
| [MANAPPURAM](https://in.tradingview.com/chart/?symbol=NSE:MANAPPURAM)<br><sub>✓ SAFE . →282Cr · 353Cr . ↓CMF7d</sub> | 357.50 | -3.9% | +42.4% | 0d | SMA-OK | RS-OK | +2.36% |
| [DCBBANK](https://in.tradingview.com/chart/?symbol=NSE:DCBBANK)<br><sub>✓ SAFE . →41Cr · 207Cr . ↓CMF20d</sub> | 203.59 | 0.0% | +69.4% | 0d | SMA-OK | RS-OK | +7.94% |
| [JAYNECOIND](https://in.tradingview.com/chart/?symbol=NSE:JAYNECOIND)<br><sub>✓ SAFE . ↗47Cr · 170Cr . ↑CMF2d</sub> | 99.89 | -13.3% | +73.5% | 0d | SMA-OK | RS-OK | +6.63% |
| [VIYASH](https://in.tradingview.com/chart/?symbol=NSE:VIYASH)<br><sub>✓ SAFE . ↗98Cr · 169Cr . ↑CMF2d</sub> | 275.95 | -6.2% | +62.9% | 0d | SMA-OK | RS-OK | +3.80% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>✓ SAFE . →344Cr · 476Cr . ↑CMF0d</sub> | 423.35 | -2.8% | +103.5% | 0d | SMA-OK | RS-OK | +0.80% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>✓ SAFE . ↗237Cr · 90Cr . ↑CMF3d</sub> | 1136.80 | -5.7% | +32.1% | 0d | SMA-OK | RS-OK | -2.61% |
| [MANGLMCEM](https://in.tradingview.com/chart/?symbol=NSE:MANGLMCEM)<br><sub>✓ SAFE . ↗37Cr · 64Cr . ↑CMF1d</sub> | 1027.95 | 0.0% | +50.1% | 0d | SMA-OK | RS-OK | +4.70% |
| [JTLIND](https://in.tradingview.com/chart/?symbol=NSE:JTLIND)<br><sub>✓ SAFE . ↘15Cr · 53Cr . ↑CMF1d</sub> | 79.52 | -4.3% | +94.9% | 0d | SMA-OK | RS-OK | +6.58% |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>✓ SAFE . ↗148Cr · 51Cr . ↑CMF7d</sub> | 642.75 | -4.0% | +44.3% | 0d | SMA-OK | RS-OK | +2.23% |
| [SKIPPER](https://in.tradingview.com/chart/?symbol=NSE:SKIPPER)<br><sub>✓ SAFE . ↗42Cr · 38Cr . ↑CMF2d</sub> | 554.00 | -3.6% | +67.7% | 0d | SMA-OK | RS-OK | -0.26% |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>✓ SAFE . ↗226Cr · 37Cr . ↓CMF9d</sub> | 1911.20 | 0.0% | +50.6% | 0d | SMA-OK | RS-OK | +0.58% |
| [ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL)<br><sub>✓ SAFE . ↗153Cr · 35Cr . ↑CMF3d</sub> | 443.55 | -0.1% | +98.4% | 0d | SMA-OK | RS-OK | +1.94% |
| [MIDHANI](https://in.tradingview.com/chart/?symbol=NSE:MIDHANI)<br><sub>✓ SAFE . ↗126Cr · 30Cr . ↑CMF6d</sub> | 423.95 | -5.9% | +56.8% | 0d | SMA-OK | RS-OK | +0.82% |
| [EXIDEIND](https://in.tradingview.com/chart/?symbol=NSE:EXIDEIND)<br><sub>✓ SAFE . ↘123Cr · 111Cr . ↑CMF30d</sub> | 459.60 | -6.3% | +59.6% | 1d | SMA-OK | RS-OK | -0.97% |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN)<br><sub>✓ SAFE . →61Cr · 62Cr . ↑CMF12d</sub> | 244.91 | -6.6% | +48.8% | 1d | SMA-OK | RS-OK | +3.25% |
| [TATATECH](https://in.tradingview.com/chart/?symbol=NSE:TATATECH)<br><sub>✓ SAFE . ↘122Cr · 50Cr . ↑CMF11d</sub> | 820.75 | -6.6% | +61.2% | 1d | SMA-OK | RS-OK | -0.39% |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL)<br><sub>✓ SAFE . ↗376Cr · 41Cr . ↑CMF10d</sub> | 186.71 | -3.6% | +118.2% | 1d | SMA-OK | RS-OK | -2.28% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>✓ SAFE . ↗550Cr · 163Cr . ↑CMF6d</sub> | 35265.00 | -8.3% | +117.5% | 2d | SMA-OK | RS-OK | -0.52% |
| [CARBORUNIV](https://in.tradingview.com/chart/?symbol=NSE:CARBORUNIV)<br><sub>⚠ CAUTION . ↗39Cr · 88Cr . ↑CMF1d</sub> | 1169.80 | -5.8% | +56.3% | 2d | SMA-OK | RS-OK | +2.83% |
| [JSFB](https://in.tradingview.com/chart/?symbol=NSE:JSFB)<br><sub>✓ SAFE . ↗59Cr · 310Cr . ↑CMF6d</sub> | 582.35 | -0.4% | +70.4% | 3d | SMA-OK | RS-OK | +3.46% |
| [EDELWEISS](https://in.tradingview.com/chart/?symbol=NSE:EDELWEISS)<br><sub>✓ SAFE . ↗63Cr · 142Cr . ↑CMF3d</sub> | 128.68 | -1.2% | +37.1% | 3d | SMA-OK | RS-OK | +1.63% |
| [DEEPINDS](https://in.tradingview.com/chart/?symbol=NSE:DEEPINDS)<br><sub>✓ SAFE . ↘36Cr · 40Cr . ↑CMF15d</sub> | 688.05 | -4.2% | +107.5% | 3d | SMA-OK | RS-OK | +4.50% |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>✓ SAFE . →83Cr · 182Cr . ↑CMF3d</sub> | 401.60 | 0.0% | +101.8% | 4d | SMA-OK | RS-OK | +1.06% |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA)<br><sub>✓ SAFE . →37Cr · 59Cr . ↑CMF1d</sub> | 561.70 | 0.0% | +44.2% | 4d | SMA-OK | RS-OK | +4.08% |
| [BLUSPRING](https://in.tradingview.com/chart/?symbol=NSE:BLUSPRING)<br><sub>✓ SAFE . ↗9Cr · 33Cr . ↑CMF2d</sub> | 128.98 | 0.0% | +188.4% | 4d | SMA-OK | RS-OK | +9.34% |
| [DATAPATTNS](https://in.tradingview.com/chart/?symbol=NSE:DATAPATTNS)<br><sub>✓ SAFE . →426Cr · 1118Cr . ↑CMF22d</sub> | 4829.90 | -0.7% | +121.3% | 5d | SMA-OK | RS-OK | +2.76% |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . ↗1092Cr · 1106Cr . ↑CMF7d</sub> | 3185.00 | -7.5% | +115.5% | 5d | SMA-OK | RS-OK | +1.89% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>✓ SAFE . ↗650Cr · 340Cr . ↑CMF5d</sub> | 1036.05 | -9.9% | +55.3% | 5d | SMA-OK | RS-OK | -0.97% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>✓ SAFE . ↗144Cr · 199Cr . ↓CMF30d</sub> | 715.40 | 0.0% | +130.4% | 5d | SMA-OK | RS-OK | +5.69% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>✓ SAFE . →75Cr · 154Cr . ↑CMF7d</sub> | 503.00 | -1.5% | +216.8% | 5d | SMA-OK | RS-OK | +5.83% |
| [VOLTAMP](https://in.tradingview.com/chart/?symbol=NSE:VOLTAMP)<br><sub>✓ SAFE . ↘37Cr · 135Cr . ↑CMF0d</sub> | 10869.50 | -13.2% | +60.4% | 5d | SMA-OK | RS-OK | +5.39% |
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>✓ SAFE . →224Cr · 112Cr . ↑CMF14d</sub> | 1699.10 | -0.1% | +33.4% | 5d | SMA-OK | RS-OK | +0.18% |
| [ZENTEC](https://in.tradingview.com/chart/?symbol=NSE:ZENTEC)<br><sub>✓ SAFE . ↗143Cr · 112Cr . ↑CMF12d</sub> | 1926.30 | -3.5% | +56.9% | 5d | SMA-OK | RS-OK | +0.90% |
| [EPL](https://in.tradingview.com/chart/?symbol=NSE:EPL)<br><sub>✓ SAFE . ↗104Cr · 105Cr . ↓CMF7d</sub> | 265.61 | -1.7% | +47.5% | 5d | SMA-OK | RS-OK | -1.66% |
| [IFCI](https://in.tradingview.com/chart/?symbol=NSE:IFCI)<br><sub>✓ SAFE . ↗227Cr · 104Cr . ↑CMF8d</sub> | 80.91 | -10.2% | +72.8% | 5d | SMA-OK | RS-OK | -1.04% |
| [INDOBORAX](https://in.tradingview.com/chart/?symbol=NSE:INDOBORAX)<br><sub>✓ SAFE . ↗58Cr · 104Cr . ↑CMF23d</sub> | 511.85 | 0.0% | +124.6% | 5d | SMA-OK | RS-OK | +2.75% |
| [ENRIN](https://in.tradingview.com/chart/?symbol=NSE:ENRIN)<br><sub>✓ SAFE . ↗414Cr · 65Cr . ↑CMF7d</sub> | 3584.00 | -7.4% | +68.6% | 5d | SMA-OK | RS-OK | -0.60% |
| [FINCABLES](https://in.tradingview.com/chart/?symbol=NSE:FINCABLES)<br><sub>✓ SAFE . ↗473Cr · 69Cr . ↑CMF4d</sub> | 1260.50 | -5.2% | +77.3% | 5d | SMA-OK | RS-OK | -2.38% |
| [IDEAFORGE](https://in.tradingview.com/chart/?symbol=NSE:IDEAFORGE)<br><sub>✓ SAFE . ↘73Cr · 67Cr . ↑CMF25d</sub> | 812.50 | -4.7% | +118.6% | 5d | SMA-OK | RS-OK | +0.73% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>✓ SAFE . ↗49Cr · 45Cr . ↓CMF2d</sub> | 721.15 | -2.2% | +164.8% | 5d | SMA-OK | RS-OK | -1.25% |
| [ELGIEQUIP](https://in.tradingview.com/chart/?symbol=NSE:ELGIEQUIP)<br><sub>✓ SAFE . ↗81Cr · 45Cr . ↑CMF17d</sub> | 634.35 | -0.5% | +52.7% | 5d | SMA-OK | RS-OK | +0.30% |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>✓ SAFE . ↗74Cr · 36Cr . ↓CMF18d</sub> | 2230.10 | -4.2% | +127.6% | 5d | SMA-OK | RS-OK | -1.28% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>✓ SAFE . ↘36Cr · 33Cr . ↑CMF8d</sub> | 606.20 | -10.2% | +149.9% | 5d | SMA-OK | RS-OK | -2.97% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>✓ SAFE . ↗271Cr · 157Cr . ↑CMF7d</sub> | 47250.00 | 0.0% | +64.4% | 6d | SMA-OK | RS-OK | +1.07% |
| [RATEGAIN](https://in.tradingview.com/chart/?symbol=NSE:RATEGAIN)<br><sub>✓ SAFE . ↘49Cr · 95Cr . ↓CMF11d</sub> | 990.05 | 0.0% | +126.0% | 6d | SMA-OK | RS-OK | +4.91% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↗347Cr · 94Cr . ↓CMF17d</sub> | 189.22 | 0.0% | +74.7% | 6d | SMA-OK | RS-OK | +0.28% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>✓ SAFE . ↘26Cr · 29Cr . ↑CMF1d</sub> | 1420.60 | -10.5% | +72.6% | 6d | SMA-OK | RS-OK | -1.13% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>✓ SAFE . ↘431Cr · 236Cr . ↑CMF14d</sub> | 4314.50 | -3.4% | +45.6% | 7d | SMA-OK | RS-OK | -0.64% |
| [TBZ](https://in.tradingview.com/chart/?symbol=NSE:TBZ)<br><sub>✓ SAFE . →53Cr · 199Cr . ↑CMF0d . DEL67%(T-1)</sub> | 279.50 | -4.0% | +150.7% | 7d | SMA-OK | RS-OK | +12.32% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>✓ SAFE . ↗86Cr · 124Cr . ↑CMF5d</sub> | 269.58 | 0.0% | +72.1% | 7d | SMA-OK | RS-OK | +6.11% |
| [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA)<br><sub>✓ SAFE . ↘126Cr · 59Cr . ↑CMF13d</sub> | 104.24 | -2.0% | +82.0% | 8d | SMA-OK | RS-OK | -0.92% |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY)<br><sub>✓ SAFE . →62Cr · 36Cr . ↑CMF20d</sub> | 3321.00 | -4.0% | +82.3% | 9d | SMA-OK | RS-OK | -0.87% |
| [VADILALIND](https://in.tradingview.com/chart/?symbol=NSE:VADILALIND)<br><sub>✓ SAFE . ↗46Cr · 28Cr . ↓CMF6d</sub> | 7417.50 | -4.7% | +83.7% | 9d | SMA-OK | RS-OK | +0.21% |
| [JINDALSAW](https://in.tradingview.com/chart/?symbol=NSE:JINDALSAW)<br><sub>✓ SAFE . ↗74Cr · 490Cr . ↑CMF30d</sub> | 291.65 | 0.0% | +88.6% | 10d | SMA-OK | RS-OK | +8.12% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘423Cr · 284Cr . ↑CMF12d</sub> | 228.01 | -0.9% | +274.1% | 10d | SMA-OK | RS-OK | +1.84% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>↘562Cr · 268Cr . ↑CMF8d</sub> | 1124.90 | -1.2% | +96.8% | 10d | SMA-OK | RS-OK | -0.65% |
| [TDPOWERSYS](https://in.tradingview.com/chart/?symbol=NSE:TDPOWERSYS)<br><sub>✓ SAFE . ↗377Cr · 211Cr . ↑CMF16d</sub> | 1534.80 | -3.3% | +207.6% | 10d | SMA-OK | RS-OK | +1.81% |
| [KEI](https://in.tradingview.com/chart/?symbol=NSE:KEI)<br><sub>✓ SAFE . ↘189Cr · 160Cr . ↑CMF13d</sub> | 5527.60 | -5.9% | +45.3% | 10d | SMA-OK | RS-OK | -2.60% |
| [AVADHSUGAR](https://in.tradingview.com/chart/?symbol=NSE:AVADHSUGAR)<br><sub>✓ SAFE . →50Cr · 110Cr . ↑CMF30d</sub> | 834.80 | 0.0% | +168.2% | 10d | SMA-OK | RS-OK | +2.47% |
| [KENNAMET](https://in.tradingview.com/chart/?symbol=NSE:KENNAMET)<br><sub>✓ SAFE . ↗40Cr · 88Cr . ↑CMF10d</sub> | 4044.70 | 0.0% | +102.1% | 10d | SMA-OK | RS-OK | +8.74% |
| [DALMIASUG](https://in.tradingview.com/chart/?symbol=NSE:DALMIASUG)<br><sub>✓ SAFE . ↘50Cr · 79Cr . ↑CMF30d</sub> | 497.95 | -2.0% | +88.3% | 10d | SMA-OK | RS-OK | -2.00% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>✓ SAFE . ↘98Cr · 74Cr . ↑CMF30d</sub> | 1170.30 | -0.4% | +55.9% | 10d | SMA-OK | RS-OK | -0.44% |
| [DHAMPURSUG](https://in.tradingview.com/chart/?symbol=NSE:DHAMPURSUG)<br><sub>✓ SAFE . ↗37Cr · 65Cr . ↑CMF2d</sub> | 185.23 | -2.4% | +67.7% | 10d | SMA-OK | RS-OK | -2.39% |
| [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA)<br><sub>✓ SAFE . →95Cr · 49Cr . ↑CMF30d</sub> | 335.70 | -4.4% | +43.3% | 10d | SMA-OK | RS-OK | +1.77% |
| [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS)<br><sub>✓ SAFE . ↗179Cr · 48Cr . ↑CMF8d</sub> | 183.37 | -1.3% | +82.6% | 10d | SMA-OK | RS-OK | -1.32% |
| [AEROENTER](https://in.tradingview.com/chart/?symbol=NSE:AEROENTER)<br><sub>✓ SAFE . ↗11Cr · 38Cr . ↑CMF3d</sub> | 140.07 | -3.4% | +115.7% | 10d | SMA-OK | RS-OK | +7.21% |
| [GRANULES](https://in.tradingview.com/chart/?symbol=NSE:GRANULES)<br><sub>✓ SAFE . ↘38Cr · 35Cr . ↓CMF19d</sub> | 858.15 | -5.0% | +87.3% | 10d | SMA-OK | RS-OK | +1.97% |
| [SOLARINDS](https://in.tradingview.com/chart/?symbol=NSE:SOLARINDS)<br><sub>✓ SAFE . ↗338Cr · 965Cr . ↑CMF30d</sub> | 19970.00 | -1.7% | +69.6% | 11d | SMA-OK | RS-OK | -1.74% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . →498Cr · 283Cr . ↑CMF17d</sub> | 8475.00 | -1.5% | +49.0% | 11d | SMA-OK | RS-OK | -0.29% |
| [SIEMENS](https://in.tradingview.com/chart/?symbol=NSE:SIEMENS)<br><sub>✓ SAFE . ↗208Cr · 117Cr . ↑CMF14d</sub> | 3936.00 | -2.1% | +38.2% | 11d | SMA-OK | RS-OK | -1.28% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>✓ SAFE . →58Cr · 68Cr . ↑CMF22d</sub> | 871.45 | -3.0% | +48.2% | 11d | SMA-OK | RS-OK | -0.35% |
| [HEG](https://in.tradingview.com/chart/?symbol=NSE:HEG)<br><sub>✓ SAFE . →136Cr · 66Cr . ↑CMF5d</sub> | 710.75 | -3.9% | +53.8% | 12d | SMA-OK | RS-OK | -0.17% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . →282Cr · 245Cr . ↑CMF13d</sub> | 96.01 | -0.5% | +185.1% | 13d | SMA-OK | RS-OK | -0.48% |
| [SMLMAH](https://in.tradingview.com/chart/?symbol=NSE:SMLMAH)<br><sub>✓ SAFE . ↘73Cr · 44Cr . ↑CMF17d</sub> | 5324.00 | -10.0% | +92.5% | 14d | SMA-OK | RS-OK | +3.19% |
| [BEPL](https://in.tradingview.com/chart/?symbol=NSE:BEPL)<br><sub>✓ SAFE . ↘15Cr · 35Cr . ↓CMF0d</sub> | 125.82 | -1.5% | +62.8% | 14d | SMA-OK | RS-OK | +2.10% |
| [NETWEB](https://in.tradingview.com/chart/?symbol=NSE:NETWEB)<br><sub>✓ SAFE . ↗1240Cr · 2390Cr . ↑CMF12d</sub> | 5601.00 | 0.0% | +173.4% | 15d | SMA-OK | RS-OK | +3.34% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>✓ SAFE . ↘297Cr · 218Cr . ↑CMF11d</sub> | 1500.20 | -2.6% | +37.7% | 15d | SMA-OK | RS-OK | -0.44% |
| [AUBANK](https://in.tradingview.com/chart/?symbol=NSE:AUBANK)<br><sub>✓ SAFE . ↘167Cr · 234Cr . ↑CMF13d</sub> | 1108.20 | 0.0% | +59.6% | 15d | SMA-OK | RS-OK | +1.86% |
| [APARINDS](https://in.tradingview.com/chart/?symbol=NSE:APARINDS)<br><sub>✓ SAFE . →327Cr · 157Cr . ↑CMF14d</sub> | 16856.00 | -6.4% | +142.0% | 15d | SMA-OK | RS-OK | +0.43% |
| [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON)<br><sub>✓ SAFE . ↗514Cr · 174Cr . ↑CMF11d</sub> | 168.60 | -0.5% | +86.8% | 15d | SMA-OK | RS-OK | +0.72% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>✓ SAFE . ↘199Cr · 87Cr . ↓CMF16d</sub> | 1439.30 | -5.1% | +124.8% | 15d | SMA-OK | RS-OK | -0.30% |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS)<br><sub>✓ SAFE . ↗335Cr · 83Cr . ↑CMF7d</sub> | 321.30 | -3.5% | +104.8% | 15d | SMA-OK | RS-OK | +0.14% |
| [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK)<br><sub>✓ SAFE . ↘70Cr · 78Cr . ↑CMF7d</sub> | 392.50 | 0.0% | +56.5% | 15d | SMA-OK | RS-OK | +0.05% |
| [GAEL](https://in.tradingview.com/chart/?symbol=NSE:GAEL)<br><sub>✓ SAFE . ↘20Cr · 27Cr . ↑CMF20d</sub> | 177.46 | -3.2% | +74.4% | 15d | SMA-OK | RS-OK | -3.22% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . ↘120Cr · 111Cr . ↑CMF11d</sub> | 8206.50 | -5.1% | +80.3% | 16d | SMA-OK | RS-OK | -0.60% |
| [SBCL](https://in.tradingview.com/chart/?symbol=NSE:SBCL)<br><sub>✓ SAFE . ↗150Cr · 31Cr . ↑CMF13d</sub> | 993.25 | -10.1% | +164.7% | 16d | SMA-OK | RS-OK | -3.13% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>✓ SAFE . ↘264Cr · 306Cr . ↑CMF13d</sub> | 11828.00 | -0.6% | +87.7% | 18d | SMA-OK | RS-OK | +2.05% |
| [AVALON](https://in.tradingview.com/chart/?symbol=NSE:AVALON)<br><sub>✓ SAFE . →127Cr · 97Cr . ↑CMF12d</sub> | 2183.80 | -2.8% | +175.1% | 18d | SMA-OK | RS-OK | -2.75% |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>✓ SAFE . ↗172Cr · 40Cr . ↓CMF4d</sub> | 4621.90 | -2.4% | +55.6% | 18d | SMA-OK | RS-OK | -1.30% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>✓ SAFE . →369Cr · 232Cr . ↑CMF14d</sub> | 8101.00 | -1.1% | +43.2% | 20d | SMA-OK | RS-OK | +0.01% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>✓ SAFE . ↘130Cr · 122Cr . ↑CMF13d</sub> | 1621.30 | -2.7% | +58.6% | 20d | SMA-OK | RS-OK | +0.83% |
| [ABB](https://in.tradingview.com/chart/?symbol=NSE:ABB)<br><sub>✓ SAFE . →260Cr · 124Cr . ↓CMF1d</sub> | 7650.00 | -1.1% | +63.1% | 20d | SMA-OK | RS-OK | -0.78% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>✓ SAFE . ↘81Cr · 37Cr . ↑CMF26d</sub> | 737.05 | -2.4% | +59.3% | 20d | SMA-OK | RS-OK | -1.12% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . ↘268Cr · 296Cr . ↑CMF19d</sub> | 267.04 | -0.8% | +103.4% | 22d | SMA-OK | RS-OK | -0.82% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>✓ SAFE . ↘89Cr · 56Cr . ↓CMF1d</sub> | 72.07 | -0.6% | +69.9% | 22d | SMA-OK | RS-OK | +0.19% |
| [KABRAEXTRU](https://in.tradingview.com/chart/?symbol=NSE:KABRAEXTRU)<br><sub>✓ SAFE . →27Cr · 32Cr . ↑CMF30d</sub> | 566.20 | 0.0% | +210.1% | 22d | SMA-OK | RS-OK | +7.01% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↘15Cr · 28Cr . ↓CMF1d</sub> | 295.00 | -8.3% | +73.1% | 24d | SMA-OK | RS-OK | -3.22% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>✓ SAFE . ↘142Cr · 203Cr . ↑CMF3d</sub> | 1417.90 | 0.0% | +141.2% | 25d | SMA-OK | RS-OK | +6.11% |
| [KDDL](https://in.tradingview.com/chart/?symbol=NSE:KDDL)<br><sub>✓ SAFE . ↘25Cr · 141Cr . ↓CMF12d</sub> | 4005.40 | -2.2% | +97.7% | 25d | SMA-OK | RS-OK | +1.59% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . ↘228Cr · 117Cr . ↑CMF20d</sub> | 130.99 | -1.3% | +137.1% | 25d | SMA-OK | RS-OK | -1.33% |
| [AARTIIND](https://in.tradingview.com/chart/?symbol=NSE:AARTIIND)<br><sub>✓ SAFE . →92Cr · 52Cr . ↓CMF15d</sub> | 527.20 | -2.0% | +55.1% | 25d | SMA-OK | RS-OK | +1.37% |
| [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP)<br><sub>✓ SAFE . ↗69Cr · 124Cr . ↓CMF13d</sub> | 169.52 | -2.5% | +148.5% | 28d | SMA-OK | RS-OK | +3.52% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [TITAN](https://in.tradingview.com/chart/?symbol=NSE:TITAN)<br><sub>⚠ CAUTION . ↗618Cr · 285Cr . ↑CMF18d</sub> | 5068.40 | -1.2% | +52.3% | 30d | SMA-OK | RS-OK | +0.09% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>✓ SAFE . ↘105Cr · 113Cr . ↑CMF21d</sub> | 328.30 | -2.0% | +98.4% | 30d | SMA-OK | RS-OK | -2.01% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>✓ SAFE . ↘76Cr · 67Cr . ↑CMF13d</sub> | 90.05 | -7.0% | +138.7% | 30d | SMA-OK | RS-OK | -2.38% |
| [MANORAMA](https://in.tradingview.com/chart/?symbol=NSE:MANORAMA)<br><sub>✓ SAFE . ↗350Cr · 41Cr . ↓CMF30d</sub> | 1927.30 | -1.6% | +79.2% | 30d | SMA-OK | RS-OK | -1.60% |
| [SUVEN](https://in.tradingview.com/chart/?symbol=NSE:SUVEN)<br><sub>✓ SAFE . ↗40Cr · 69Cr . ↑CMF1d</sub> | 373.15 | -0.1% | +194.6% | 31d | SMA-OK | RS-OK | -0.12% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↗387Cr · 69Cr . ↑CMF11d</sub> | 2819.30 | -5.1% | +76.6% | 31d | SMA-OK | RS-OK | -0.02% |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>✓ SAFE . ↗445Cr · 1458Cr . ↑CMF14d</sub> | 729.35 | -4.9% | +83.3% | 32d | SMA-OK | RS-OK | -4.92% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↗530Cr · 123Cr . ↑CMF26d</sub> | 1393.50 | -3.2% | +116.0% | 33d | SMA-OK | RS-OK | +0.22% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>✓ SAFE . ↗256Cr · 131Cr . ↑CMF6d</sub> | 2837.80 | -2.1% | +107.7% | 35d | SMA-OK | RS-OK | +2.57% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>✓ SAFE . ↘34Cr · 47Cr . ↑CMF30d</sub> | 688.20 | -0.5% | +705.6% | 36d | SMA-OK | RS-OK | +3.57% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . ↘436Cr · 228Cr . ↑CMF30d</sub> | 1462.00 | -6.8% | +251.4% | 40d | SMA-OK | RS-OK | +0.86% |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>✓ SAFE . ↘132Cr · 58Cr . ↓CMF0d</sub> | 814.95 | -0.9% | +205.2% | 40d | SMA-OK | RS-OK | -0.73% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>✓ SAFE . ↘31Cr · 54Cr . ↓CMF7d</sub> | 1626.60 | -0.8% | +122.6% | 40d | SMA-OK | RS-OK | -0.48% |
| [YASHO](https://in.tradingview.com/chart/?symbol=NSE:YASHO)<br><sub>✓ SAFE . ↘37Cr · 36Cr . ↑CMF15d</sub> | 4400.00 | -10.5% | +277.5% | 40d | SMA-OK | RS-OK | +2.70% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>✓ SAFE . ↗31Cr · 28Cr . ↓CMF9d</sub> | 562.85 | -4.9% | +88.8% | 45d | SMA-OK | RS-OK | -0.58% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . ↘173Cr · 216Cr . ↑CMF6d</sub> | 334.00 | -3.2% | +48.5% | 50d | SMA-OK | RS-OK | +1.10% |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON)<br><sub>✓ SAFE . →30Cr · 40Cr . ↑CMF30d</sub> | 4600.10 | 0.0% | +83.1% | 50d | SMA-OK | RS-OK | +1.91% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>⚠ CAUTION . ↘121Cr · 159Cr . ↑CMF30d</sub> | 361.00 | -2.9% | +90.1% | 55d | SMA-OK | RS-OK | +1.60% |
| [MTARTECH](https://in.tradingview.com/chart/?symbol=NSE:MTARTECH)<br><sub>✓ SAFE . ↗2251Cr · 944Cr . ↑CMF8d</sub> | 7777.00 | -7.1% | +457.1% | 58d | SMA-OK | RS-OK | -4.25% |
| [PARAS](https://in.tradingview.com/chart/?symbol=NSE:PARAS)<br><sub>✓ SAFE . ↗294Cr · 351Cr . ↑CMF12d</sub> | 1499.60 | -1.8% | +156.5% | 64d | SMA-OK | RS-OK | -0.16% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↗125Cr · 36Cr . ↑CMF7d</sub> | 3876.90 | -3.2% | +209.5% | 65d | SMA-OK | RS-OK | -0.60% |
| [RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO)<br><sub>✓ SAFE . ↘140Cr · 81Cr . ↑CMF12d</sub> | 4639.80 | -2.0% | +82.6% | 67d | SMA-OK | RS-OK | -1.20% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↘164Cr · 161Cr . ↑CMF30d</sub> | 817.60 | -0.8% | +101.8% | 70d | SMA-OK | RS-OK | -0.52% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>✓ SAFE . ↗594Cr · 4615Cr . ↑CMF30d</sub> | 2311.90 | 0.0% | +220.3% | 72d | SMA-OK | RS-OK | +15.30% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . ↘282Cr · 253Cr . ↑CMF30d</sub> | 1802.00 | -2.7% | +116.5% | 72d | SMA-OK | RS-OK | -1.26% |
| [STYLAMIND](https://in.tradingview.com/chart/?symbol=NSE:STYLAMIND)<br><sub>✓ SAFE . →20Cr · 46Cr . ↓CMF22d</sub> | 3601.70 | -3.6% | +125.2% | 75d | SMA-OK | RS-OK | -0.43% |
| [RRKABEL](https://in.tradingview.com/chart/?symbol=NSE:RRKABEL)<br><sub>✓ SAFE . ↘97Cr · 79Cr . ↓CMF9d</sub> | 2919.30 | 0.0% | +150.0% | 80d | SMA-OK | RS-OK | +0.87% |
| [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS)<br><sub>✓ SAFE . →51Cr · 40Cr . ↓CMF0d</sub> | 2497.40 | -1.5% | +92.8% | 80d | SMA-OK | RS-OK | -0.02% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . →89Cr · 47Cr . ↑CMF30d</sub> | 1457.40 | -1.0% | +83.3% | 84d | SMA-OK | RS-OK | -0.96% |
| [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO)<br><sub>✓ SAFE . ↘49Cr · 36Cr . ↓CMF12d</sub> | 69.79 | -5.4% | +131.9% | 84d | SMA-OK | RS-OK | -0.23% |
| [HONASA](https://in.tradingview.com/chart/?symbol=NSE:HONASA)<br><sub>✓ SAFE . ↗167Cr · 54Cr . ↑CMF5d</sub> | 481.90 | -4.2% | +88.0% | 88d | SMA-OK | RS-OK | -0.39% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . ↗145Cr · 62Cr . ↓CMF13d</sub> | 803.50 | -3.6% | +205.2% | 89d | SMA-OK | RS-OK | +3.20% |
| [RISHABH](https://in.tradingview.com/chart/?symbol=NSE:RISHABH)<br><sub>✓ SAFE . ↗41Cr · 28Cr . ↓CMF0d</sub> | 669.30 | -3.7% | +109.3% | 96d | SMA-OK | RS-OK | -2.18% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↗1100Cr · 474Cr . ↑CMF30d</sub> | 284.58 | -3.5% | +753.3% | 102d | SMA-OK | RS-OK | +0.76% |

### By Trend Age

**<2 WEEKS** (68)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ACMESOLAR,NSE:AEROENTER,NSE:AEROFLEX,NSE:AVADHSUGAR,NSE:BHEL,NSE:BLUSPRING,NSE:BOSCHLTD,NSE:CARBORUNIV,NSE:CYIENTDLM,NSE:DALMIASUG,NSE:DATAPATTNS,NSE:DCBBANK,NSE:DEEPINDS,NSE:DHAMPURSUG,NSE:EBGNG,NSE:EDELWEISS,NSE:ELGIEQUIP,NSE:EMIL,NSE:ENGINERSIN,NSE:ENRIN,NSE:EPL,NSE:EXIDEIND,NSE:FINCABLES,NSE:GABRIEL,NSE:GRANULES,NSE:HFCL,NSE:HINDALCO,NSE:ICIL,NSE:IDEAFORGE,NSE:IFCI,NSE:INDOBORAX,NSE:IPCALAB,NSE:JAYNECOIND,NSE:JINDALSAW,NSE:JINDRILL,NSE:JSFB,NSE:JSWINFRA,NSE:JTLIND,NSE:KEI,NSE:KENNAMET,NSE:MANAPPURAM,NSE:MANGLMCEM,NSE:MANINDS,NSE:MCX,NSE:MIDHANI,NSE:NEOGEN,NSE:PIDILITIND,NSE:PNBHOUSING,NSE:POWERINDIA,NSE:RATEGAIN,NSE:RBA,NSE:ROLEXRINGS,NSE:SHAILY,NSE:SHANTIGOLD,NSE:SHRIRAMFIN,NSE:SKIPPER,NSE:TATATECH,NSE:TBZ,NSE:TDPOWERSYS,NSE:THELEELA,NSE:TVSMOTOR,NSE:VADILALIND,NSE:VIYASH,NSE:VOLTAMP,NSE:WELENT,NSE:WELSPUNLIV,NSE:ZENTEC,NSE:ZYDUSLIFE
```

**2-4 WEEKS** (26)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABB,NSE:ANTHEM,NSE:APARINDS,NSE:AUBANK,NSE:AUROPHARMA,NSE:AVALON,NSE:BEPL,NSE:DIVISLAB,NSE:EICHERMOT,NSE:FLUOROCHEM,NSE:GAEL,NSE:HEG,NSE:MARKSANS,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:NAVINFLUOR,NSE:NESTLEIND,NSE:NETWEB,NSE:OFSS,NSE:RBLBANK,NSE:RKFORGE,NSE:SBCL,NSE:SIEMENS,NSE:SMLMAH,NSE:SOLARINDS,NSE:SYRMA
```

**1-2 MONTHS** (24)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AARTIIND,NSE:AEGISLOG,NSE:AETHER,NSE:ATHERENERG,NSE:AZAD,NSE:BALRAMCHIN,NSE:CHENNPETRO,NSE:GLAND,NSE:IOLCP,NSE:KABRAEXTRU,NSE:KDDL,NSE:KTKBANK,NSE:LLOYDSENGG,NSE:MANORAMA,NSE:RATNAVEER,NSE:SHILPAMED,NSE:SIGMAADV,NSE:SSWL,NSE:STLTECH,NSE:SUVEN,NSE:TFCILTD,NSE:TITAN,NSE:UJJIVANSFB,NSE:YASHO
```

**2-3 MONTHS** (5)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:FEDERALBNK,NSE:GNA,NSE:MTARTECH,NSE:NYKAA,NSE:SHRIPISTON
```

**3-6 MONTHS** (15)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CUPID,NSE:HONASA,NSE:LAURUSLABS,NSE:PAISALO,NSE:PARAS,NSE:RADICO,NSE:RISHABH,NSE:RRKABEL,NSE:SAILIFE,NSE:SANSERA,NSE:SJS,NSE:SKYGOLD,NSE:SONACOMS,NSE:STYLAMIND,NSE:WELCORP
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
