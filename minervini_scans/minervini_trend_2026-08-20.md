> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-08-20
*Generated 2026-08-20 15:47 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [BLSE](https://in.tradingview.com/chart/?symbol=NSE:BLSE) | [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM) |
| [CARBORUNIV](https://in.tradingview.com/chart/?symbol=NSE:CARBORUNIV) | [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM) |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM) | [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN) |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG) | [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS) |
| [EQUITASBNK](https://in.tradingview.com/chart/?symbol=NSE:EQUITASBNK) | [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH) |
| [GAEL](https://in.tradingview.com/chart/?symbol=NSE:GAEL) | [HAPPYFORGE](https://in.tradingview.com/chart/?symbol=NSE:HAPPYFORGE) |
| [GOKULAGRO](https://in.tradingview.com/chart/?symbol=NSE:GOKULAGRO) | [HSCL](https://in.tradingview.com/chart/?symbol=NSE:HSCL) |
| [INDOBORAX](https://in.tradingview.com/chart/?symbol=NSE:INDOBORAX) | [IDEAFORGE](https://in.tradingview.com/chart/?symbol=NSE:IDEAFORGE) |
| [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP) | [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB) |
| [JAYNECOIND](https://in.tradingview.com/chart/?symbol=NSE:JAYNECOIND) | [INDUSINDBK](https://in.tradingview.com/chart/?symbol=NSE:INDUSINDBK) |
| [LLOYDSENT](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENT) | [JINDALSAW](https://in.tradingview.com/chart/?symbol=NSE:JINDALSAW) |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH) | [KRN](https://in.tradingview.com/chart/?symbol=NSE:KRN) |
| [MANGLMCEM](https://in.tradingview.com/chart/?symbol=NSE:MANGLMCEM) | [MSTCLTD](https://in.tradingview.com/chart/?symbol=NSE:MSTCLTD) |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE) | [NRBBEARING](https://in.tradingview.com/chart/?symbol=NSE:NRBBEARING) |
| [MINDACORP](https://in.tradingview.com/chart/?symbol=NSE:MINDACORP) | [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO) |
| [MUFIN](https://in.tradingview.com/chart/?symbol=NSE:MUFIN) | [PITTIENG](https://in.tradingview.com/chart/?symbol=NSE:PITTIENG) |
| [RATEGAIN](https://in.tradingview.com/chart/?symbol=NSE:RATEGAIN) | [PRECWIRE](https://in.tradingview.com/chart/?symbol=NSE:PRECWIRE) |
| [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS) | [RACLGEAR](https://in.tradingview.com/chart/?symbol=NSE:RACLGEAR) |
| [RPTECH](https://in.tradingview.com/chart/?symbol=NSE:RPTECH) | [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY) |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE) | [SMLMAH](https://in.tradingview.com/chart/?symbol=NSE:SMLMAH) |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV) | [THYROCARE](https://in.tradingview.com/chart/?symbol=NSE:THYROCARE) |
| [SBCL](https://in.tradingview.com/chart/?symbol=NSE:SBCL) | [UNIVCABLES](https://in.tradingview.com/chart/?symbol=NSE:UNIVCABLES) |
| [SEAMECLTD](https://in.tradingview.com/chart/?symbol=NSE:SEAMECLTD) | [VIYASH](https://in.tradingview.com/chart/?symbol=NSE:VIYASH) |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON) |  |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV) |  |
| [SKIPPER](https://in.tradingview.com/chart/?symbol=NSE:SKIPPER) |  |
| [SUVEN](https://in.tradingview.com/chart/?symbol=NSE:SUVEN) |  |
| [VOLTAMP](https://in.tradingview.com/chart/?symbol=NSE:VOLTAMP) |  |
| [WABAG](https://in.tradingview.com/chart/?symbol=NSE:WABAG) |  |

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

**Qualifying: 128**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ACMESOLAR,NSE:AEROFLEX,NSE:APOLLOPIPE,NSE:ASIANENE,NSE:AVADHSUGAR,NSE:BHEL,NSE:BLSE,NSE:BOSCHLTD,NSE:CARBORUNIV,NSE:CYIENTDLM,NSE:DALMIASUG,NSE:DATAPATTNS,NSE:DEEPINDS,NSE:DHAMPURSUG,NSE:DREDGECORP,NSE:EBGNG,NSE:EDELWEISS,NSE:ELGIEQUIP,NSE:ENRIN,NSE:EPL,NSE:EQUITASBNK,NSE:FINCABLES,NSE:HFCL,NSE:HINDALCO,NSE:ICIL,NSE:IFCI,NSE:INDOBORAX,NSE:IPCALAB,NSE:JAYNECOIND,NSE:JINDRILL,NSE:JSWINFRA,NSE:KEI,NSE:KENNAMET,NSE:LLOYDSENT,NSE:LUMAXTECH,NSE:MANGLMCEM,NSE:MANINDS,NSE:MARINE,NSE:MCX,NSE:NEOGEN,NSE:PIDILITIND,NSE:PNBHOUSING,NSE:POWERINDIA,NSE:RATEGAIN,NSE:RAYMOND,NSE:RBA,NSE:ROLEXRINGS,NSE:SAMBHV,NSE:SEAMECLTD,NSE:SHANTIGOLD,NSE:SHRIRAMFIN,NSE:SKIPPER,NSE:TDPOWERSYS,NSE:THELEELA,NSE:TVSMOTOR,NSE:VOLTAMP,NSE:WABAG,NSE:WELSPUNLIV,NSE:ZENTEC,NSE:ZYDUSLIFE,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABB,NSE:APARINDS,NSE:AUBANK,NSE:AUROPHARMA,NSE:AVALON,NSE:DIVISLAB,NSE:EICHERMOT,NSE:FLUOROCHEM,NSE:GAEL,NSE:GOKULAGRO,NSE:HEG,NSE:LALPATHLAB,NSE:MARKSANS,NSE:MINDACORP,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:MUFIN,NSE:NAVINFLUOR,NSE:NESTLEIND,NSE:NETWEB,NSE:OFSS,NSE:RATNAVEER,NSE:RBLBANK,NSE:RKFORGE,NSE:SBCL,NSE:SIEMENS,NSE:SOLARINDS,NSE:SYRMA,NSE:UJJIVANSFB,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AARTIIND,NSE:AEGISLOG,NSE:ATHERENERG,NSE:AZAD,NSE:BALRAMCHIN,NSE:CHENNPETRO,NSE:GLAND,NSE:IOLCP,NSE:KARURVYSYA,NSE:KTKBANK,NSE:LLOYDSENGG,NSE:MANORAMA,NSE:NAZARA,NSE:SHILPAMED,NSE:SIGMAADV,NSE:STLTECH,NSE:SUVEN,NSE:TFCILTD,NSE:TITAN,NSE:YASHO,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AKUMS,NSE:FEDERALBNK,NSE:MTARTECH,NSE:NYKAA,NSE:PARAS,NSE:SHRIPISTON,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:BLISSGVS,NSE:CUPID,NSE:HONASA,NSE:LAURUSLABS,NSE:RADICO,NSE:RISHABH,NSE:RPTECH,NSE:RRKABEL,NSE:SAILIFE,NSE:SANSERA,NSE:SKYGOLD,NSE:SONACOMS,NSE:WELCORP
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [WABAG](https://in.tradingview.com/chart/?symbol=NSE:WABAG)<br><sub>✓ SAFE . →110Cr · 288Cr . ↑CMF0d</sub> | 2057.90 | -7.4% | +96.2% | 0d | SMA-OK | RS-OK | +4.08% |
| [MANGLMCEM](https://in.tradingview.com/chart/?symbol=NSE:MANGLMCEM)<br><sub>✓ SAFE . ↗30Cr · 268Cr . ↑CMF0d</sub> | 981.85 | -0.5% | +43.3% | 0d | SMA-OK | RS-OK | +9.73% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>✓ SAFE . →344Cr · 476Cr . ↑CMF0d</sub> | 423.35 | -2.8% | +103.5% | 0d | SMA-OK | RS-OK | +0.80% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>✓ SAFE . ↗237Cr · 90Cr . ↑CMF3d</sub> | 1136.80 | -5.7% | +32.1% | 0d | SMA-OK | RS-OK | -2.61% |
| [JAYNECOIND](https://in.tradingview.com/chart/?symbol=NSE:JAYNECOIND)<br><sub>✓ SAFE . →32Cr · 71Cr . ↑CMF1d</sub> | 93.68 | -18.7% | +62.8% | 0d | SMA-OK | RS-OK | +2.70% |
| [APOLLOPIPE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOPIPE)<br><sub>✓ SAFE . ↗34Cr · 55Cr . ↓CMF10d</sub> | 603.25 | 0.0% | +137.1% | 0d | SMA-OK | RS-OK | +4.65% |
| [ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL)<br><sub>✓ SAFE . ↗148Cr · 45Cr . ↑CMF2d</sub> | 435.10 | -2.0% | +94.6% | 0d | SMA-OK | RS-OK | -1.96% |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>✓ SAFE . ↗222Cr · 45Cr . ↓CMF8d</sub> | 1900.10 | -0.2% | +49.8% | 0d | SMA-OK | RS-OK | -0.19% |
| [SKIPPER](https://in.tradingview.com/chart/?symbol=NSE:SKIPPER)<br><sub>✓ SAFE . ↗40Cr · 44Cr . ↑CMF1d</sub> | 555.45 | -3.4% | +68.1% | 0d | SMA-OK | RS-OK | +0.84% |
| [ASIANENE](https://in.tradingview.com/chart/?symbol=NSE:ASIANENE)<br><sub>✓ SAFE . ↗50Cr · 42Cr . ↑CMF16d</sub> | 484.90 | 0.0% | +107.3% | 0d | SMA-OK | RS-OK | +1.28% |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>✓ SAFE . ↗142Cr · 33Cr . ↑CMF6d</sub> | 628.70 | -6.1% | +41.2% | 0d | SMA-OK | RS-OK | -1.01% |
| [LLOYDSENT](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENT)<br><sub>✓ SAFE . ↗38Cr · 30Cr . ↓CMF6d</sub> | 78.55 | -5.9% | +89.8% | 0d | SMA-OK | RS-OK | -0.03% |
| [EQUITASBNK](https://in.tradingview.com/chart/?symbol=NSE:EQUITASBNK)<br><sub>✓ SAFE . ↘16Cr · 28Cr . ↓CMF0d</sub> | 76.99 | -7.3% | +53.2% | 0d | SMA-OK | RS-OK | +3.08% |
| [BLSE](https://in.tradingview.com/chart/?symbol=NSE:BLSE)<br><sub>✓ SAFE . ↘17Cr · 48Cr . ↑CMF30d</sub> | 321.10 | 0.0% | +149.7% | 1d | SMA-OK | RS-OK | +2.23% |
| [CARBORUNIV](https://in.tradingview.com/chart/?symbol=NSE:CARBORUNIV)<br><sub>⚠ CAUTION . ↗35Cr · 30Cr . ↑CMF0d</sub> | 1137.60 | -8.4% | +52.0% | 1d | SMA-OK | RS-OK | +4.64% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>✓ SAFE . ↗550Cr · 163Cr . ↑CMF6d</sub> | 35265.00 | -8.3% | +117.5% | 2d | SMA-OK | RS-OK | -0.52% |
| [EDELWEISS](https://in.tradingview.com/chart/?symbol=NSE:EDELWEISS)<br><sub>✓ SAFE . ↗53Cr · 150Cr . ↑CMF2d</sub> | 126.62 | -2.8% | +34.9% | 2d | SMA-OK | RS-OK | +3.56% |
| [DEEPINDS](https://in.tradingview.com/chart/?symbol=NSE:DEEPINDS)<br><sub>✓ SAFE . ↘34Cr · 34Cr . ↑CMF14d . DEL59%(T-1)</sub> | 658.45 | -8.3% | +98.6% | 2d | SMA-OK | RS-OK | -1.33% |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>✓ SAFE . ↘69Cr · 376Cr . ↑CMF2d</sub> | 397.40 | 0.0% | +99.7% | 3d | SMA-OK | RS-OK | +4.47% |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA)<br><sub>✓ SAFE . ↘32Cr · 76Cr . ↑CMF0d</sub> | 539.70 | 0.0% | +38.5% | 3d | SMA-OK | RS-OK | +1.30% |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH)<br><sub>✓ SAFE . ↗165Cr · 29Cr . ↑CMF15d</sub> | 2043.70 | -1.6% | +95.0% | 3d | SMA-OK | RS-OK | +2.85% |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . ↗1008Cr · 1226Cr . ↑CMF6d</sub> | 3126.00 | -9.2% | +111.5% | 4d | SMA-OK | RS-OK | +5.15% |
| [DATAPATTNS](https://in.tradingview.com/chart/?symbol=NSE:DATAPATTNS)<br><sub>✓ SAFE . ↘322Cr · 598Cr . ↑CMF21d</sub> | 4700.20 | -3.4% | +115.4% | 4d | SMA-OK | RS-OK | -1.55% |
| [INDOBORAX](https://in.tradingview.com/chart/?symbol=NSE:INDOBORAX)<br><sub>✓ SAFE . ↘47Cr · 304Cr . ↑CMF22d</sub> | 498.15 | 0.0% | +118.6% | 4d | SMA-OK | RS-OK | +14.82% |
| [IFCI](https://in.tradingview.com/chart/?symbol=NSE:IFCI)<br><sub>✓ SAFE . ↗223Cr · 190Cr . ↑CMF7d</sub> | 81.76 | -9.2% | +74.7% | 4d | SMA-OK | RS-OK | +0.10% |
| [EPL](https://in.tradingview.com/chart/?symbol=NSE:EPL)<br><sub>✓ SAFE . ↗97Cr · 175Cr . ↓CMF6d</sub> | 270.10 | 0.0% | +50.0% | 4d | SMA-OK | RS-OK | +7.70% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>✓ SAFE . ↗120Cr · 124Cr . ↓CMF30d</sub> | 676.90 | 0.0% | +118.0% | 4d | SMA-OK | RS-OK | +5.26% |
| [ZENTEC](https://in.tradingview.com/chart/?symbol=NSE:ZENTEC)<br><sub>✓ SAFE . ↗135Cr · 93Cr . ↑CMF11d</sub> | 1909.10 | -4.4% | +55.5% | 4d | SMA-OK | RS-OK | -1.22% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>✓ SAFE . ↘36Cr · 90Cr . ↑CMF7d</sub> | 624.75 | -7.4% | +157.6% | 4d | SMA-OK | RS-OK | +6.18% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>✓ SAFE . ↘22Cr · 70Cr . ↓CMF16d</sub> | 131.38 | 0.0% | +59.6% | 4d | SMA-OK | RS-OK | +6.89% |
| [FINCABLES](https://in.tradingview.com/chart/?symbol=NSE:FINCABLES)<br><sub>✓ SAFE . ↗480Cr · 66Cr . ↑CMF3d</sub> | 1291.20 | -2.9% | +81.7% | 4d | SMA-OK | RS-OK | -1.71% |
| [VOLTAMP](https://in.tradingview.com/chart/?symbol=NSE:VOLTAMP)<br><sub>✓ SAFE . ↘25Cr · 59Cr . ↓CMF30d</sub> | 10313.50 | -17.6% | +52.2% | 4d | SMA-OK | RS-OK | +3.14% |
| [ELGIEQUIP](https://in.tradingview.com/chart/?symbol=NSE:ELGIEQUIP)<br><sub>✓ SAFE . ↗78Cr · 51Cr . ↑CMF16d</sub> | 632.45 | -0.8% | +52.2% | 4d | SMA-OK | RS-OK | -0.84% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↗43Cr · 48Cr . ↑CMF7d</sub> | 656.65 | 0.0% | +104.0% | 4d | SMA-OK | RS-OK | +4.15% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>✓ SAFE . ↗51Cr · 38Cr . ↓CMF1d</sub> | 730.25 | -1.0% | +168.2% | 4d | SMA-OK | RS-OK | +2.05% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>✓ SAFE . ↘62Cr · 33Cr . ↑CMF6d</sub> | 475.30 | -7.0% | +199.3% | 4d | SMA-OK | RS-OK | +0.24% |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>✓ SAFE . ↗72Cr · 31Cr . ↓CMF17d</sub> | 2259.10 | -3.0% | +130.6% | 4d | SMA-OK | RS-OK | -2.99% |
| [DREDGECORP](https://in.tradingview.com/chart/?symbol=NSE:DREDGECORP)<br><sub>✓ SAFE . ↗32Cr · 28Cr . ↑CMF16d</sub> | 1118.30 | -9.3% | +90.0% | 4d | SMA-OK | RS-OK | -5.96% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>✓ SAFE . ↗650Cr · 340Cr . ↑CMF5d</sub> | 1036.05 | -9.9% | +55.3% | 5d | SMA-OK | RS-OK | -0.97% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↗348Cr · 411Cr . ↓CMF16d</sub> | 188.69 | 0.0% | +74.2% | 5d | SMA-OK | RS-OK | +4.11% |
| [ENRIN](https://in.tradingview.com/chart/?symbol=NSE:ENRIN)<br><sub>✓ SAFE . ↗414Cr · 65Cr . ↑CMF7d</sub> | 3584.00 | -7.4% | +68.6% | 5d | SMA-OK | RS-OK | -0.60% |
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>✓ SAFE . →224Cr · 112Cr . ↑CMF14d</sub> | 1699.10 | -0.1% | +33.4% | 5d | SMA-OK | RS-OK | +0.18% |
| [RATEGAIN](https://in.tradingview.com/chart/?symbol=NSE:RATEGAIN)<br><sub>✓ SAFE . ↘46Cr · 32Cr . ↓CMF10d</sub> | 943.75 | -3.5% | +115.4% | 5d | SMA-OK | RS-OK | +1.41% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>✓ SAFE . ↗271Cr · 157Cr . ↑CMF7d</sub> | 47250.00 | 0.0% | +64.4% | 6d | SMA-OK | RS-OK | +1.07% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>✓ SAFE . ↗73Cr · 61Cr . ↑CMF4d</sub> | 254.06 | -4.8% | +62.2% | 6d | SMA-OK | RS-OK | +5.09% |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE)<br><sub>→55Cr · 43Cr . ↑CMF13d</sub> | 373.25 | -0.9% | +146.0% | 6d | SMA-OK | RS-OK | +0.48% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>✓ SAFE . ↘431Cr · 236Cr . ↑CMF14d</sub> | 4314.50 | -3.4% | +45.6% | 7d | SMA-OK | RS-OK | -0.64% |
| [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA)<br><sub>✓ SAFE . ↘153Cr · 66Cr . ↑CMF12d</sub> | 105.21 | -1.1% | +83.7% | 7d | SMA-OK | RS-OK | +4.11% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>✓ SAFE . ↘108Cr · 266Cr . ↑CMF30d</sub> | 1175.50 | 0.0% | +56.6% | 9d | SMA-OK | RS-OK | +0.13% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘431Cr · 225Cr . ↑CMF11d</sub> | 223.90 | -2.7% | +267.4% | 9d | SMA-OK | RS-OK | -1.16% |
| [KEI](https://in.tradingview.com/chart/?symbol=NSE:KEI)<br><sub>✓ SAFE . ↘193Cr · 180Cr . ↑CMF12d</sub> | 5675.00 | -3.4% | +49.1% | 9d | SMA-OK | RS-OK | -0.11% |
| [AVADHSUGAR](https://in.tradingview.com/chart/?symbol=NSE:AVADHSUGAR)<br><sub>✓ SAFE . ↘39Cr · 169Cr . ↑CMF30d</sub> | 814.70 | 0.0% | +161.8% | 9d | SMA-OK | RS-OK | +9.52% |
| [TDPOWERSYS](https://in.tradingview.com/chart/?symbol=NSE:TDPOWERSYS)<br><sub>✓ SAFE . ↗368Cr · 167Cr . ↑CMF15d</sub> | 1507.50 | -5.0% | +202.2% | 9d | SMA-OK | RS-OK | -2.47% |
| [DHAMPURSUG](https://in.tradingview.com/chart/?symbol=NSE:DHAMPURSUG)<br><sub>✓ SAFE . ↗31Cr · 125Cr . ↑CMF1d</sub> | 189.76 | 0.0% | +71.8% | 9d | SMA-OK | RS-OK | +7.71% |
| [DALMIASUG](https://in.tradingview.com/chart/?symbol=NSE:DALMIASUG)<br><sub>✓ SAFE . ↘44Cr · 115Cr . ↑CMF30d</sub> | 508.10 | 0.0% | +92.1% | 9d | SMA-OK | RS-OK | +6.84% |
| [SEAMECLTD](https://in.tradingview.com/chart/?symbol=NSE:SEAMECLTD)<br><sub>✓ SAFE . ↗36Cr · 108Cr . ↑CMF4d</sub> | 1699.00 | 0.0% | +114.9% | 9d | SMA-OK | RS-OK | +3.87% |
| [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS)<br><sub>✓ SAFE . ↗189Cr · 81Cr . ↑CMF7d</sub> | 185.82 | 0.0% | +85.0% | 9d | SMA-OK | RS-OK | +6.37% |
| [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA)<br><sub>✓ SAFE . →97Cr · 48Cr . ↑CMF30d</sub> | 329.85 | -6.1% | +40.8% | 9d | SMA-OK | RS-OK | -0.02% |
| [KENNAMET](https://in.tradingview.com/chart/?symbol=NSE:KENNAMET)<br><sub>✓ SAFE . ↗30Cr · 28Cr . ↑CMF9d</sub> | 3719.60 | 0.0% | +85.9% | 9d | SMA-OK | RS-OK | +2.86% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>↘562Cr · 268Cr . ↑CMF8d</sub> | 1124.90 | -1.2% | +96.8% | 10d | SMA-OK | RS-OK | -0.65% |
| [SOLARINDS](https://in.tradingview.com/chart/?symbol=NSE:SOLARINDS)<br><sub>✓ SAFE . ↗338Cr · 965Cr . ↑CMF30d</sub> | 19970.00 | -1.7% | +69.6% | 11d | SMA-OK | RS-OK | -1.74% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . →498Cr · 283Cr . ↑CMF17d</sub> | 8475.00 | -1.5% | +49.0% | 11d | SMA-OK | RS-OK | -0.29% |
| [HEG](https://in.tradingview.com/chart/?symbol=NSE:HEG)<br><sub>✓ SAFE . ↘134Cr · 100Cr . ↑CMF4d</sub> | 711.95 | -3.7% | +54.1% | 11d | SMA-OK | RS-OK | +0.55% |
| [SIEMENS](https://in.tradingview.com/chart/?symbol=NSE:SIEMENS)<br><sub>✓ SAFE . ↗208Cr · 117Cr . ↑CMF14d</sub> | 3936.00 | -2.1% | +38.2% | 11d | SMA-OK | RS-OK | -1.28% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . →294Cr · 459Cr . ↑CMF12d</sub> | 96.47 | 0.0% | +186.4% | 12d | SMA-OK | RS-OK | +9.10% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>✓ SAFE . ↘42Cr · 58Cr . ↑CMF27d</sub> | 1889.40 | -4.0% | +44.5% | 12d | SMA-OK | RS-OK | +0.12% |
| [MINDACORP](https://in.tradingview.com/chart/?symbol=NSE:MINDACORP)<br><sub>✓ SAFE . ↗93Cr · 41Cr . ↓CMF5d</sub> | 743.30 | -0.3% | +54.6% | 12d | SMA-OK | RS-OK | +0.60% |
| [NETWEB](https://in.tradingview.com/chart/?symbol=NSE:NETWEB)<br><sub>✓ SAFE . →1039Cr · 2416Cr . ↑CMF11d</sub> | 5419.80 | 0.0% | +164.6% | 14d | SMA-OK | RS-OK | +7.00% |
| [AUBANK](https://in.tradingview.com/chart/?symbol=NSE:AUBANK)<br><sub>✓ SAFE . ↘150Cr · 400Cr . ↑CMF12d</sub> | 1088.00 | -0.9% | +56.7% | 14d | SMA-OK | RS-OK | +1.21% |
| [APARINDS](https://in.tradingview.com/chart/?symbol=NSE:APARINDS)<br><sub>✓ SAFE . →339Cr · 205Cr . ↑CMF13d</sub> | 16784.00 | -6.8% | +140.9% | 14d | SMA-OK | RS-OK | +1.02% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>✓ SAFE . ↘198Cr · 194Cr . ↓CMF15d</sub> | 1443.70 | -4.8% | +125.5% | 14d | SMA-OK | RS-OK | -3.42% |
| [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK)<br><sub>✓ SAFE . ↘68Cr · 107Cr . ↑CMF6d</sub> | 392.30 | 0.0% | +56.4% | 14d | SMA-OK | RS-OK | +2.83% |
| [GOKULAGRO](https://in.tradingview.com/chart/?symbol=NSE:GOKULAGRO)<br><sub>✓ SAFE . →19Cr · 100Cr . ↓CMF30d</sub> | 243.69 | 0.0% | +59.6% | 14d | SMA-OK | RS-OK | +0.28% |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS)<br><sub>✓ SAFE . ↗330Cr · 63Cr . ↑CMF6d</sub> | 320.85 | -3.6% | +104.5% | 14d | SMA-OK | RS-OK | -1.88% |
| [GAEL](https://in.tradingview.com/chart/?symbol=NSE:GAEL)<br><sub>✓ SAFE . ↘21Cr · 41Cr . ↑CMF19d</sub> | 183.36 | 0.0% | +80.2% | 14d | SMA-OK | RS-OK | +5.48% |
| [MUFIN](https://in.tradingview.com/chart/?symbol=NSE:MUFIN)<br><sub>✓ SAFE . →18Cr · 29Cr . ↑CMF0d</sub> | 139.51 | 0.0% | +66.6% | 14d | SMA-OK | RS-OK | +3.26% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>✓ SAFE . ↘297Cr · 218Cr . ↑CMF11d</sub> | 1500.20 | -2.6% | +37.7% | 15d | SMA-OK | RS-OK | -0.44% |
| [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON)<br><sub>✓ SAFE . ↗514Cr · 174Cr . ↑CMF11d</sub> | 168.60 | -0.5% | +86.8% | 15d | SMA-OK | RS-OK | +0.72% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . ↘159Cr · 49Cr . ↑CMF10d</sub> | 8256.00 | -4.6% | +81.4% | 15d | SMA-OK | RS-OK | -0.26% |
| [SBCL](https://in.tradingview.com/chart/?symbol=NSE:SBCL)<br><sub>✓ SAFE . ↗213Cr · 35Cr . ↑CMF12d</sub> | 1025.35 | -7.2% | +173.2% | 15d | SMA-OK | RS-OK | -0.02% |
| [AVALON](https://in.tradingview.com/chart/?symbol=NSE:AVALON)<br><sub>✓ SAFE . ↗163Cr · 174Cr . ↑CMF11d</sub> | 2245.50 | -0.0% | +182.9% | 17d | SMA-OK | RS-OK | -0.00% |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>✓ SAFE . ↗177Cr · 123Cr . ↓CMF3d</sub> | 4682.70 | -1.2% | +57.7% | 17d | SMA-OK | RS-OK | -0.14% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>✓ SAFE . ↘264Cr · 306Cr . ↑CMF13d</sub> | 11828.00 | -0.6% | +87.7% | 18d | SMA-OK | RS-OK | +2.05% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>✓ SAFE . →150Cr · 130Cr . ↑CMF12d</sub> | 1608.00 | -3.5% | +57.3% | 19d | SMA-OK | RS-OK | -1.02% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>✓ SAFE . ↘91Cr · 37Cr . ↑CMF25d</sub> | 745.40 | -1.3% | +61.1% | 19d | SMA-OK | RS-OK | -0.51% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>✓ SAFE . →369Cr · 232Cr . ↑CMF14d</sub> | 8101.00 | -1.1% | +43.2% | 20d | SMA-OK | RS-OK | +0.01% |
| [ABB](https://in.tradingview.com/chart/?symbol=NSE:ABB)<br><sub>✓ SAFE . →260Cr · 124Cr . ↓CMF1d</sub> | 7650.00 | -1.1% | +63.1% | 20d | SMA-OK | RS-OK | -0.78% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . ↘258Cr · 304Cr . ↑CMF18d</sub> | 269.24 | 0.0% | +105.1% | 21d | SMA-OK | RS-OK | +7.52% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>✓ SAFE . ↘89Cr · 171Cr . ↓CMF0d</sub> | 71.93 | -0.7% | +69.5% | 21d | SMA-OK | RS-OK | +0.18% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . →251Cr · 369Cr . ↑CMF19d</sub> | 132.76 | 0.0% | +140.3% | 24d | SMA-OK | RS-OK | +1.03% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>✓ SAFE . →137Cr · 41Cr . ↑CMF2d</sub> | 1336.20 | -5.2% | +127.3% | 24d | SMA-OK | RS-OK | -2.04% |
| [AARTIIND](https://in.tradingview.com/chart/?symbol=NSE:AARTIIND)<br><sub>✓ SAFE . →93Cr · 39Cr . ↓CMF14d . DEL65%(T-1)</sub> | 520.05 | -3.4% | +53.0% | 24d | SMA-OK | RS-OK | -1.33% |
| [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP)<br><sub>✓ SAFE . ↗63Cr · 34Cr . ↓CMF12d</sub> | 163.75 | -5.8% | +140.1% | 27d | SMA-OK | RS-OK | +4.35% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>✓ SAFE . ↘113Cr · 207Cr . ↑CMF20d</sub> | 335.05 | 0.0% | +102.4% | 29d | SMA-OK | RS-OK | +3.39% |
| [MANORAMA](https://in.tradingview.com/chart/?symbol=NSE:MANORAMA)<br><sub>✓ SAFE . ↗361Cr · 85Cr . ↓CMF30d</sub> | 1958.70 | 0.0% | +82.1% | 29d | SMA-OK | RS-OK | +1.22% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>⚠ CAUTION . ↘44Cr · 78Cr . ↓CMF2d</sub> | 334.10 | -4.0% | +64.6% | 29d | SMA-OK | RS-OK | +0.92% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>✓ SAFE . ↗131Cr · 42Cr . ↑CMF12d</sub> | 92.25 | -4.8% | +144.5% | 29d | SMA-OK | RS-OK | -0.70% |
| [TITAN](https://in.tradingview.com/chart/?symbol=NSE:TITAN)<br><sub>⚠ CAUTION . ↗618Cr · 285Cr . ↑CMF18d</sub> | 5068.40 | -1.2% | +52.3% | 30d | SMA-OK | RS-OK | +0.09% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↗389Cr · 159Cr . ↑CMF10d</sub> | 2820.00 | -5.1% | +76.6% | 30d | SMA-OK | RS-OK | -0.75% |
| [SUVEN](https://in.tradingview.com/chart/?symbol=NSE:SUVEN)<br><sub>✓ SAFE . ↗35Cr · 122Cr . ↑CMF0d</sub> | 373.60 | 0.0% | +195.0% | 30d | SMA-OK | RS-OK | +12.34% |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>✓ SAFE . ↗317Cr · 2571Cr . ↑CMF13d</sub> | 767.10 | 0.0% | +92.8% | 31d | SMA-OK | RS-OK | +17.87% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . ↘55Cr · 63Cr . ↑CMF14d</sub> | 357.50 | 0.0% | +64.3% | 31d | SMA-OK | RS-OK | +0.04% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↗537Cr · 310Cr . ↑CMF25d</sub> | 1390.50 | -3.5% | +121.8% | 32d | SMA-OK | RS-OK | -3.46% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>✓ SAFE . ↗252Cr · 106Cr . ↑CMF5d</sub> | 2766.60 | -4.6% | +102.5% | 34d | SMA-OK | RS-OK | -2.18% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>✓ SAFE . ↘29Cr · 47Cr . ↑CMF30d . DEL100%(T-1)</sub> | 664.45 | -3.9% | +677.8% | 35d | SMA-OK | RS-OK | -3.89% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . ↘477Cr · 249Cr . ↑CMF30d</sub> | 1449.60 | -7.6% | +249.8% | 39d | SMA-OK | RS-OK | +0.79% |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>✓ SAFE . ↘179Cr · 107Cr . ↑CMF0d</sub> | 820.95 | -0.1% | +207.5% | 39d | SMA-OK | RS-OK | +1.63% |
| [YASHO](https://in.tradingview.com/chart/?symbol=NSE:YASHO)<br><sub>✓ SAFE . ↘34Cr · 53Cr . ↑CMF14d</sub> | 4284.20 | -12.8% | +267.5% | 39d | SMA-OK | RS-OK | -4.17% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . ↘165Cr · 219Cr . ↑CMF5d</sub> | 330.35 | -4.2% | +50.7% | 49d | SMA-OK | RS-OK | +0.92% |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON)<br><sub>✓ SAFE . →28Cr · 32Cr . ↑CMF30d</sub> | 4513.80 | -0.2% | +81.4% | 49d | SMA-OK | RS-OK | +1.34% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>⚠ CAUTION . ↘121Cr · 154Cr . ↑CMF30d</sub> | 355.30 | -4.4% | +87.1% | 54d | SMA-OK | RS-OK | -0.98% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>✓ SAFE . ↗48Cr · 32Cr . ↓CMF0d</sub> | 752.90 | -1.1% | +81.8% | 54d | SMA-OK | RS-OK | -0.05% |
| [MTARTECH](https://in.tradingview.com/chart/?symbol=NSE:MTARTECH)<br><sub>✓ SAFE . ↗2251Cr · 944Cr . ↑CMF8d</sub> | 7777.00 | -7.1% | +457.1% | 58d | SMA-OK | RS-OK | -4.25% |
| [PARAS](https://in.tradingview.com/chart/?symbol=NSE:PARAS)<br><sub>✓ SAFE . ↗278Cr · 182Cr . ↑CMF11d</sub> | 1502.00 | -1.7% | +156.9% | 63d | SMA-OK | RS-OK | +0.37% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↗129Cr · 36Cr . ↑CMF6d</sub> | 3900.20 | -2.6% | +211.4% | 64d | SMA-OK | RS-OK | +0.15% |
| [RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO)<br><sub>✓ SAFE . ↘148Cr · 196Cr . ↑CMF11d</sub> | 4696.00 | -0.8% | +84.8% | 66d | SMA-OK | RS-OK | +0.00% |
| [BLISSGVS](https://in.tradingview.com/chart/?symbol=NSE:BLISSGVS)<br><sub>✓ SAFE . →52Cr · 21Cr . ↑CMF30d</sub> | 527.10 | -2.7% | +312.1% | 68d | SMA-OK | RS-OK | +0.68% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↘179Cr · 232Cr . ↑CMF30d</sub> | 821.90 | -0.3% | +102.8% | 69d | SMA-OK | RS-OK | -0.19% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . ↘286Cr · 240Cr . ↑CMF30d</sub> | 1825.00 | -1.4% | +119.6% | 71d | SMA-OK | RS-OK | +1.29% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>✓ SAFE . ↘129Cr · 150Cr . ↑CMF30d</sub> | 2005.20 | 0.0% | +177.8% | 71d | SMA-OK | RS-OK | +1.59% |
| [RRKABEL](https://in.tradingview.com/chart/?symbol=NSE:RRKABEL)<br><sub>✓ SAFE . ↘96Cr · 72Cr . ↓CMF8d</sub> | 2894.20 | -0.2% | +147.9% | 79d | SMA-OK | RS-OK | -0.16% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . ↗99Cr · 76Cr . ↑CMF30d</sub> | 1471.60 | 0.0% | +85.1% | 83d | SMA-OK | RS-OK | +3.47% |
| [HONASA](https://in.tradingview.com/chart/?symbol=NSE:HONASA)<br><sub>✓ SAFE . ↗167Cr · 41Cr . ↑CMF4d</sub> | 483.80 | -3.8% | +88.8% | 87d | SMA-OK | RS-OK | +1.51% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . ↗150Cr · 40Cr . ↓CMF12d</sub> | 778.55 | -6.5% | +195.7% | 88d | SMA-OK | RS-OK | +0.10% |
| [RISHABH](https://in.tradingview.com/chart/?symbol=NSE:RISHABH)<br><sub>✓ SAFE . ↗40Cr · 116Cr . ↑CMF3d</sub> | 684.20 | -1.6% | +113.9% | 95d | SMA-OK | RS-OK | -1.55% |
| [RPTECH](https://in.tradingview.com/chart/?symbol=NSE:RPTECH)<br><sub>✓ SAFE . ↘25Cr · 30Cr . ↓CMF1d</sub> | 856.15 | -5.2% | +207.0% | 98d | SMA-OK | RS-OK | +2.14% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↗1175Cr · 733Cr . ↑CMF30d</sub> | 282.43 | -4.2% | +746.9% | 101d | SMA-OK | RS-OK | -0.75% |

### By Trend Age

**<2 WEEKS** (60)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ACMESOLAR,NSE:AEROFLEX,NSE:APOLLOPIPE,NSE:ASIANENE,NSE:AVADHSUGAR,NSE:BHEL,NSE:BLSE,NSE:BOSCHLTD,NSE:CARBORUNIV,NSE:CYIENTDLM,NSE:DALMIASUG,NSE:DATAPATTNS,NSE:DEEPINDS,NSE:DHAMPURSUG,NSE:DREDGECORP,NSE:EBGNG,NSE:EDELWEISS,NSE:ELGIEQUIP,NSE:ENRIN,NSE:EPL,NSE:EQUITASBNK,NSE:FINCABLES,NSE:HFCL,NSE:HINDALCO,NSE:ICIL,NSE:IFCI,NSE:INDOBORAX,NSE:IPCALAB,NSE:JAYNECOIND,NSE:JINDRILL,NSE:JSWINFRA,NSE:KEI,NSE:KENNAMET,NSE:LLOYDSENT,NSE:LUMAXTECH,NSE:MANGLMCEM,NSE:MANINDS,NSE:MARINE,NSE:MCX,NSE:NEOGEN,NSE:PIDILITIND,NSE:PNBHOUSING,NSE:POWERINDIA,NSE:RATEGAIN,NSE:RAYMOND,NSE:RBA,NSE:ROLEXRINGS,NSE:SAMBHV,NSE:SEAMECLTD,NSE:SHANTIGOLD,NSE:SHRIRAMFIN,NSE:SKIPPER,NSE:TDPOWERSYS,NSE:THELEELA,NSE:TVSMOTOR,NSE:VOLTAMP,NSE:WABAG,NSE:WELSPUNLIV,NSE:ZENTEC,NSE:ZYDUSLIFE
```

**2-4 WEEKS** (29)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABB,NSE:APARINDS,NSE:AUBANK,NSE:AUROPHARMA,NSE:AVALON,NSE:DIVISLAB,NSE:EICHERMOT,NSE:FLUOROCHEM,NSE:GAEL,NSE:GOKULAGRO,NSE:HEG,NSE:LALPATHLAB,NSE:MARKSANS,NSE:MINDACORP,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:MUFIN,NSE:NAVINFLUOR,NSE:NESTLEIND,NSE:NETWEB,NSE:OFSS,NSE:RATNAVEER,NSE:RBLBANK,NSE:RKFORGE,NSE:SBCL,NSE:SIEMENS,NSE:SOLARINDS,NSE:SYRMA,NSE:UJJIVANSFB
```

**1-2 MONTHS** (20)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AARTIIND,NSE:AEGISLOG,NSE:ATHERENERG,NSE:AZAD,NSE:BALRAMCHIN,NSE:CHENNPETRO,NSE:GLAND,NSE:IOLCP,NSE:KARURVYSYA,NSE:KTKBANK,NSE:LLOYDSENGG,NSE:MANORAMA,NSE:NAZARA,NSE:SHILPAMED,NSE:SIGMAADV,NSE:STLTECH,NSE:SUVEN,NSE:TFCILTD,NSE:TITAN,NSE:YASHO
```

**2-3 MONTHS** (6)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AKUMS,NSE:FEDERALBNK,NSE:MTARTECH,NSE:NYKAA,NSE:PARAS,NSE:SHRIPISTON
```

**3-6 MONTHS** (13)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:BLISSGVS,NSE:CUPID,NSE:HONASA,NSE:LAURUSLABS,NSE:RADICO,NSE:RISHABH,NSE:RPTECH,NSE:RRKABEL,NSE:SAILIFE,NSE:SANSERA,NSE:SKYGOLD,NSE:SONACOMS,NSE:WELCORP
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
