> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-08-13
*Generated 2026-08-13 15:46 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER) | [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN) |
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM) | [CARBORUNIV](https://in.tradingview.com/chart/?symbol=NSE:CARBORUNIV) |
| [ARMANFIN](https://in.tradingview.com/chart/?symbol=NSE:ARMANFIN) | [CNL](https://in.tradingview.com/chart/?symbol=NSE:CNL) |
| [ARVIND](https://in.tradingview.com/chart/?symbol=NSE:ARVIND) | [CREDITACC](https://in.tradingview.com/chart/?symbol=NSE:CREDITACC) |
| [BHARATSE](https://in.tradingview.com/chart/?symbol=NSE:BHARATSE) | [EMCURE](https://in.tradingview.com/chart/?symbol=NSE:EMCURE) |
| [BLISSGVS](https://in.tradingview.com/chart/?symbol=NSE:BLISSGVS) | [FINEORG](https://in.tradingview.com/chart/?symbol=NSE:FINEORG) |
| [DALMIASUG](https://in.tradingview.com/chart/?symbol=NSE:DALMIASUG) | [HAPPYFORGE](https://in.tradingview.com/chart/?symbol=NSE:HAPPYFORGE) |
| [EDELWEISS](https://in.tradingview.com/chart/?symbol=NSE:EDELWEISS) | [ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL) |
| [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR) | [INNOVACAP](https://in.tradingview.com/chart/?symbol=NSE:INNOVACAP) |
| [GRANULES](https://in.tradingview.com/chart/?symbol=NSE:GRANULES) | [JGCHEM](https://in.tradingview.com/chart/?symbol=NSE:JGCHEM) |
| [IFCI](https://in.tradingview.com/chart/?symbol=NSE:IFCI) | [KINGFA](https://in.tradingview.com/chart/?symbol=NSE:KINGFA) |
| [INGERRAND](https://in.tradingview.com/chart/?symbol=NSE:INGERRAND) | [KPIL](https://in.tradingview.com/chart/?symbol=NSE:KPIL) |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB) | [KRN](https://in.tradingview.com/chart/?symbol=NSE:KRN) |
| [KERNEX](https://in.tradingview.com/chart/?symbol=NSE:KERNEX) | [MANAPPURAM](https://in.tradingview.com/chart/?symbol=NSE:MANAPPURAM) |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE) | [MUFIN](https://in.tradingview.com/chart/?symbol=NSE:MUFIN) |
| [MIDHANI](https://in.tradingview.com/chart/?symbol=NSE:MIDHANI) | [POLYPLEX](https://in.tradingview.com/chart/?symbol=NSE:POLYPLEX) |
| [MUNJALAU](https://in.tradingview.com/chart/?symbol=NSE:MUNJALAU) | [RAMRAT](https://in.tradingview.com/chart/?symbol=NSE:RAMRAT) |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA) | [RATEGAIN](https://in.tradingview.com/chart/?symbol=NSE:RATEGAIN) |
| [OMAXE](https://in.tradingview.com/chart/?symbol=NSE:OMAXE) | [SENORES](https://in.tradingview.com/chart/?symbol=NSE:SENORES) |
| [PRECWIRE](https://in.tradingview.com/chart/?symbol=NSE:PRECWIRE) | [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL) |
| [PRUDENT](https://in.tradingview.com/chart/?symbol=NSE:PRUDENT) | [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON) |
| [RAIN](https://in.tradingview.com/chart/?symbol=NSE:RAIN) | [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS) |
| [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA) | [VINDHYATEL](https://in.tradingview.com/chart/?symbol=NSE:VINDHYATEL) |
| [SOMANYCERA](https://in.tradingview.com/chart/?symbol=NSE:SOMANYCERA) | [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV) |
| [TBZ](https://in.tradingview.com/chart/?symbol=NSE:TBZ) | [YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH) |
| [VADILALIND](https://in.tradingview.com/chart/?symbol=NSE:VADILALIND) |  |

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

**Qualifying: 124**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AEROFLEX,NSE:ANTHEM,NSE:APARINDS,NSE:ARVIND,NSE:AUBANK,NSE:BHARATSE,NSE:DALMIASUG,NSE:DATAPATTNS,NSE:DIVISLAB,NSE:EDELWEISS,NSE:ENTERO,NSE:EPL,NSE:FINCABLES,NSE:GRANULES,NSE:HEG,NSE:HFCL,NSE:HINDALCO,NSE:IFCI,NSE:INGERRAND,NSE:IPCALAB,NSE:JSWENERGY,NSE:JSWINFRA,NSE:KEI,NSE:KENNAMET,NSE:LALPATHLAB,NSE:MANINDS,NSE:MARINE,NSE:MARKSANS,NSE:MCX,NSE:MIDHANI,NSE:MINDACORP,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:MUNJALAU,NSE:NAVINFLUOR,NSE:NESTLEIND,NSE:NETWEB,NSE:OMAXE,NSE:PNBHOUSING,NSE:POWERINDIA,NSE:PRECWIRE,NSE:PRUDENT,NSE:QPOWER,NSE:RAIN,NSE:RBA,NSE:RBLBANK,NSE:ROLEXRINGS,NSE:SAREGAMA,NSE:SBCL,NSE:SCHNEIDER,NSE:SEAMECLTD,NSE:SHAILY,NSE:SHRIRAMFIN,NSE:SIEMENS,NSE:SMLMAH,NSE:SOLARINDS,NSE:SOMANYCERA,NSE:SYRMA,NSE:TBZ,NSE:TDPOWERSYS,NSE:TVSMOTOR,NSE:VADILALIND,NSE:VIJAYA,NSE:ZENTEC,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AARTIIND,NSE:ABB,NSE:AEGISLOG,NSE:ARMANFIN,NSE:AUROPHARMA,NSE:AVALON,NSE:BELRISE,NSE:CRAFTSMAN,NSE:EICHERMOT,NSE:FLUOROCHEM,NSE:HSCL,NSE:LLOYDSME,NSE:OFSS,NSE:RATNAVEER,NSE:RKFORGE,NSE:TFCILTD,NSE:THYROCARE,NSE:TIIL,NSE:UJJIVANSFB,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABCAPITAL,NSE:AETHER,NSE:AJANTPHARM,NSE:ATHERENERG,NSE:AZAD,NSE:CHENNPETRO,NSE:DIACABS,NSE:GLAND,NSE:INDUSINDBK,NSE:IOLCP,NSE:KARURVYSYA,NSE:KTKBANK,NSE:LLOYDSENGG,NSE:NAZARA,NSE:SHILPAMED,NSE:STLTECH,NSE:TITAN,NSE:TORNTPHARM,NSE:WSTCSTPAPR,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:DIVGIITTS,NSE:FEDERALBNK,NSE:GANDHAR,NSE:INDSWFTLAB,NSE:KERNEX,NSE:MTARTECH,NSE:NYKAA,NSE:PANAMAPET,NSE:PARAS,NSE:RADICO,NSE:SANSERA,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:BLISSGVS,NSE:CUPID,NSE:GRWRHITECH,NSE:HONASA,NSE:LAURUSLABS,NSE:PAISALO,NSE:RRKABEL,NSE:SAILIFE,NSE:SKYGOLD,NSE:SONACOMS,NSE:WELCORP
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . ↗935Cr · 848Cr . ↑CMF1d</sub> | 2970.00 | -13.7% | +100.9% | 0d | SMA-OK | RS-OK | -0.00% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>✓ SAFE . →488Cr · 631Cr . ↓CMF30d</sub> | 1025.35 | -10.8% | +53.7% | 0d | SMA-OK | RS-OK | -1.41% |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>⚠ CAUTION . ↗63Cr · 330Cr . ↓CMF3d</sub> | 1796.30 | -5.5% | +41.6% | 0d | SMA-OK | RS-OK | +1.68% |
| [IFCI](https://in.tradingview.com/chart/?symbol=NSE:IFCI)<br><sub>✓ SAFE . ↗143Cr · 312Cr . ↑CMF2d</sub> | 76.66 | -14.9% | +63.8% | 0d | SMA-OK | RS-OK | +4.29% |
| [DATAPATTNS](https://in.tradingview.com/chart/?symbol=NSE:DATAPATTNS)<br><sub>✓ SAFE . ↘376Cr · 269Cr . ↑CMF16d</sub> | 4529.30 | -6.9% | +107.5% | 0d | SMA-OK | RS-OK | +0.85% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>✓ SAFE . ↗599Cr · 2404Cr . ↑CMF0d</sub> | 36150.00 | -6.0% | +123.0% | 0d | SMA-OK | RS-OK | +10.89% |
| [FINCABLES](https://in.tradingview.com/chart/?symbol=NSE:FINCABLES)<br><sub>✓ SAFE . ↗410Cr · 205Cr . ↓CMF0d</sub> | 1249.30 | -2.4% | +75.8% | 0d | SMA-OK | RS-OK | -2.40% |
| [OMAXE](https://in.tradingview.com/chart/?symbol=NSE:OMAXE)<br><sub>✓ SAFE . ↗22Cr · 191Cr . ↑CMF0d . DEL65%(T-1)</sub> | 98.37 | 0.0% | +53.5% | 0d | SMA-OK | RS-OK | +19.99% |
| [EDELWEISS](https://in.tradingview.com/chart/?symbol=NSE:EDELWEISS)<br><sub>✓ SAFE . ↗52Cr · 126Cr . ↑CMF0d</sub> | 124.88 | -4.1% | +33.5% | 0d | SMA-OK | RS-OK | +5.03% |
| [SOMANYCERA](https://in.tradingview.com/chart/?symbol=NSE:SOMANYCERA)<br><sub>✓ SAFE . ↗19Cr · 106Cr . ↓CMF30d</sub> | 519.15 | -3.7% | +53.4% | 0d | SMA-OK | RS-OK | +2.18% |
| [JSWENERGY](https://in.tradingview.com/chart/?symbol=NSE:JSWENERGY)<br><sub>✓ SAFE . ↘94Cr · 110Cr . ↑CMF5d</sub> | 577.50 | -4.1% | +31.2% | 0d | SMA-OK | RS-OK | +2.32% |
| [INGERRAND](https://in.tradingview.com/chart/?symbol=NSE:INGERRAND)<br><sub>⚠ CAUTION . ↗14Cr · 75Cr . ↑CMF0d</sub> | 4606.40 | -2.3% | +47.4% | 0d | SMA-OK | RS-OK | +7.32% |
| [EPL](https://in.tradingview.com/chart/?symbol=NSE:EPL)<br><sub>✓ SAFE . ↗51Cr · 65Cr . ↓CMF1d</sub> | 247.24 | 0.0% | +37.3% | 0d | SMA-OK | RS-OK | +1.48% |
| [ZENTEC](https://in.tradingview.com/chart/?symbol=NSE:ZENTEC)<br><sub>✓ SAFE . →74Cr · 53Cr . ↑CMF6d</sub> | 1831.80 | -8.3% | +49.2% | 0d | SMA-OK | RS-OK | +0.41% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>✓ SAFE . ↘53Cr · 46Cr . ↑CMF1d</sub> | 448.25 | -12.3% | +182.3% | 0d | SMA-OK | RS-OK | +0.38% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>✓ SAFE . ↗79Cr · 44Cr . ↓CMF29d</sub> | 576.15 | -4.2% | +85.5% | 0d | SMA-OK | RS-OK | -3.76% |
| [VIJAYA](https://in.tradingview.com/chart/?symbol=NSE:VIJAYA)<br><sub>✓ SAFE . ↗55Cr · 41Cr . ↑CMF1d</sub> | 1486.50 | -1.6% | +72.6% | 0d | SMA-OK | RS-OK | -1.60% |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER)<br><sub>✓ SAFE . ↘111Cr · 41Cr . ↓CMF2d . DEL61%(T-1)</sub> | 1278.10 | -8.6% | +253.5% | 0d | SMA-OK | RS-OK | -1.27% |
| [SCHNEIDER](https://in.tradingview.com/chart/?symbol=NSE:SCHNEIDER)<br><sub>✓ SAFE . ↗50Cr · 38Cr . ↑CMF3d</sub> | 1379.10 | -8.1% | +138.1% | 0d | SMA-OK | RS-OK | -3.69% |
| [MIDHANI](https://in.tradingview.com/chart/?symbol=NSE:MIDHANI)<br><sub>✓ SAFE . ↗110Cr · 721Cr . ↑CMF0d</sub> | 444.85 | -1.2% | +64.5% | 1d | SMA-OK | RS-OK | +8.91% |
| [MUNJALAU](https://in.tradingview.com/chart/?symbol=NSE:MUNJALAU)<br><sub>✓ SAFE . ↗52Cr · 495Cr . ↑CMF0d</sub> | 119.37 | 0.0% | +76.1% | 1d | SMA-OK | RS-OK | +19.57% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>✓ SAFE . ↗755Cr · 485Cr . ↑CMF8d</sub> | 4399.30 | -1.3% | +57.5% | 1d | SMA-OK | RS-OK | -1.25% |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE)<br><sub>↗69Cr · 58Cr . ↑CMF8d</sub> | 371.20 | 0.0% | +144.7% | 1d | SMA-OK | RS-OK | +6.97% |
| [TBZ](https://in.tradingview.com/chart/?symbol=NSE:TBZ)<br><sub>✓ SAFE . ↘41Cr · 43Cr . ↓CMF2d</sub> | 247.45 | -15.0% | +121.9% | 1d | SMA-OK | RS-OK | +4.45% |
| [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA)<br><sub>✓ SAFE . ↗384Cr · 284Cr . ↑CMF7d</sub> | 98.35 | 0.0% | +71.8% | 2d | SMA-OK | RS-OK | +4.83% |
| [RAIN](https://in.tradingview.com/chart/?symbol=NSE:RAIN)<br><sub>✓ SAFE . ↗188Cr · 108Cr . ↓CMF4d</sub> | 213.99 | -11.9% | +110.9% | 2d | SMA-OK | RS-OK | +2.20% |
| [VADILALIND](https://in.tradingview.com/chart/?symbol=NSE:VADILALIND)<br><sub>✓ SAFE . ↗41Cr · 278Cr . ↓CMF0d</sub> | 7781.00 | 0.0% | +92.7% | 3d | SMA-OK | RS-OK | +7.38% |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY)<br><sub>✓ SAFE . ↗101Cr · 32Cr . ↑CMF14d</sub> | 3406.90 | -1.5% | +112.9% | 3d | SMA-OK | RS-OK | -0.79% |
| [BHARATSE](https://in.tradingview.com/chart/?symbol=NSE:BHARATSE)<br><sub>✓ SAFE . ↗17Cr · 31Cr . ↑CMF0d</sub> | 245.25 | -3.7% | +130.5% | 3d | SMA-OK | RS-OK | +4.23% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . →576Cr · 534Cr . ↑CMF6d</sub> | 227.36 | 0.0% | +273.0% | 4d | SMA-OK | RS-OK | +2.64% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>✓ SAFE . ↗842Cr · 1414Cr . ↑CMF2d</sub> | 1139.00 | 0.0% | +99.2% | 4d | SMA-OK | RS-OK | +1.48% |
| [TDPOWERSYS](https://in.tradingview.com/chart/?symbol=NSE:TDPOWERSYS)<br><sub>✓ SAFE . ↗350Cr · 329Cr . ↑CMF10d</sub> | 1481.60 | 0.0% | +213.3% | 4d | SMA-OK | RS-OK | +0.10% |
| [PRECWIRE](https://in.tradingview.com/chart/?symbol=NSE:PRECWIRE)<br><sub>✓ SAFE . ↗60Cr · 321Cr . ↑CMF1d</sub> | 468.65 | 0.0% | +174.7% | 4d | SMA-OK | RS-OK | +10.98% |
| [KEI](https://in.tradingview.com/chart/?symbol=NSE:KEI)<br><sub>✓ SAFE . ↗454Cr · 248Cr . ↑CMF7d</sub> | 5789.00 | 0.0% | +53.8% | 4d | SMA-OK | RS-OK | +0.61% |
| [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS)<br><sub>✓ SAFE . ↗231Cr · 144Cr . ↑CMF2d</sub> | 178.26 | 0.0% | +77.5% | 4d | SMA-OK | RS-OK | +3.03% |
| [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA)<br><sub>✓ SAFE . →122Cr · 83Cr . ↑CMF30d</sub> | 341.35 | -2.8% | +45.7% | 4d | SMA-OK | RS-OK | -1.51% |
| [GRANULES](https://in.tradingview.com/chart/?symbol=NSE:GRANULES)<br><sub>✓ SAFE . ↘58Cr · 64Cr . ↓CMF13d</sub> | 857.55 | -5.1% | +95.1% | 4d | SMA-OK | RS-OK | -0.84% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>✓ SAFE . ↗177Cr · 64Cr . ↑CMF27d</sub> | 1164.80 | 0.0% | +55.2% | 4d | SMA-OK | RS-OK | +0.62% |
| [ARVIND](https://in.tradingview.com/chart/?symbol=NSE:ARVIND)<br><sub>✓ SAFE . ↗44Cr · 61Cr . ↑CMF0d</sub> | 555.65 | -5.3% | +98.7% | 4d | SMA-OK | RS-OK | -1.98% |
| [DALMIASUG](https://in.tradingview.com/chart/?symbol=NSE:DALMIASUG)<br><sub>✓ SAFE . ↗77Cr · 46Cr . ↑CMF28d</sub> | 427.35 | 0.0% | +61.6% | 4d | SMA-OK | RS-OK | +4.21% |
| [SEAMECLTD](https://in.tradingview.com/chart/?symbol=NSE:SEAMECLTD)<br><sub>✓ SAFE . ↗19Cr · 39Cr . ↓CMF16d</sub> | 1532.30 | -6.8% | +93.8% | 4d | SMA-OK | RS-OK | +0.69% |
| [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA)<br><sub>✓ SAFE . ↗67Cr · 34Cr . ↑CMF28d</sub> | 531.65 | -4.6% | +70.9% | 4d | SMA-OK | RS-OK | +3.02% |
| [KENNAMET](https://in.tradingview.com/chart/?symbol=NSE:KENNAMET)<br><sub>✓ SAFE . ↗16Cr · 29Cr . ↑CMF4d</sub> | 3674.10 | 0.0% | +83.6% | 4d | SMA-OK | RS-OK | +2.85% |
| [SOLARINDS](https://in.tradingview.com/chart/?symbol=NSE:SOLARINDS)<br><sub>✓ SAFE . ↘135Cr · 114Cr . ↑CMF24d</sub> | 18535.00 | -3.0% | +57.4% | 5d | SMA-OK | RS-OK | +0.73% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . ↗604Cr · 264Cr . ↑CMF11d</sub> | 8282.50 | -3.5% | +45.6% | 5d | SMA-OK | RS-OK | -1.26% |
| [SIEMENS](https://in.tradingview.com/chart/?symbol=NSE:SIEMENS)<br><sub>✓ SAFE . →164Cr · 83Cr . ↑CMF8d</sub> | 3955.00 | -1.1% | +38.8% | 5d | SMA-OK | RS-OK | -0.63% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>✓ SAFE . ↘71Cr · 39Cr . ↑CMF16d</sub> | 874.90 | -1.9% | +48.8% | 5d | SMA-OK | RS-OK | -0.40% |
| [HEG](https://in.tradingview.com/chart/?symbol=NSE:HEG)<br><sub>✓ SAFE . ↘85Cr · 83Cr . ↓CMF0d</sub> | 687.00 | 0.0% | +48.7% | 6d | SMA-OK | RS-OK | +1.88% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↗341Cr · 419Cr . ↑CMF7d</sub> | 80.89 | 0.0% | +140.2% | 7d | SMA-OK | RS-OK | +10.11% |
| [MINDACORP](https://in.tradingview.com/chart/?symbol=NSE:MINDACORP)<br><sub>✓ SAFE . ↗45Cr · 203Cr . ↓CMF0d</sub> | 712.05 | -3.3% | +55.2% | 7d | SMA-OK | RS-OK | -3.29% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>✓ SAFE . ↘69Cr · 40Cr . ↑CMF22d</sub> | 1968.40 | 0.0% | +50.5% | 7d | SMA-OK | RS-OK | +0.77% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>✓ SAFE . ↗45Cr · 33Cr . ↓CMF5d</sub> | 1448.00 | 0.0% | +52.5% | 7d | SMA-OK | RS-OK | +1.95% |
| [SMLMAH](https://in.tradingview.com/chart/?symbol=NSE:SMLMAH)<br><sub>✓ SAFE . ↗182Cr · 57Cr . ↑CMF11d</sub> | 5172.00 | -12.6% | +87.0% | 8d | SMA-OK | RS-OK | +0.00% |
| [NETWEB](https://in.tradingview.com/chart/?symbol=NSE:NETWEB)<br><sub>✓ SAFE . ↗987Cr · 1791Cr . ↑CMF6d</sub> | 5181.00 | 0.0% | +152.9% | 9d | SMA-OK | RS-OK | +7.10% |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS)<br><sub>✓ SAFE . ↗202Cr · 325Cr . ↑CMF1d</sub> | 303.40 | -2.9% | +93.4% | 9d | SMA-OK | RS-OK | -2.94% |
| [APARINDS](https://in.tradingview.com/chart/?symbol=NSE:APARINDS)<br><sub>✓ SAFE . ↗365Cr · 306Cr . ↑CMF8d</sub> | 17225.00 | -4.3% | +147.3% | 9d | SMA-OK | RS-OK | -4.31% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>✓ SAFE . ↗446Cr · 234Cr . ↑CMF5d</sub> | 1520.00 | -0.7% | +39.5% | 9d | SMA-OK | RS-OK | +0.00% |
| [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON)<br><sub>✓ SAFE . ↗289Cr · 602Cr . ↑CMF5d</sub> | 154.00 | -0.7% | +70.6% | 9d | SMA-OK | RS-OK | -0.23% |
| [AUBANK](https://in.tradingview.com/chart/?symbol=NSE:AUBANK)<br><sub>✓ SAFE . →184Cr · 180Cr . ↑CMF7d</sub> | 1098.00 | 0.0% | +58.1% | 9d | SMA-OK | RS-OK | +0.60% |
| [PRUDENT](https://in.tradingview.com/chart/?symbol=NSE:PRUDENT)<br><sub>✓ SAFE . ↗24Cr · 143Cr . ↑CMF10d</sub> | 3325.00 | -2.2% | +53.8% | 9d | SMA-OK | RS-OK | -1.17% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>✓ SAFE . →212Cr · 109Cr . ↓CMF10d</sub> | 1467.70 | -3.2% | +129.3% | 9d | SMA-OK | RS-OK | -0.38% |
| [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK)<br><sub>✓ SAFE . ↘116Cr · 43Cr . ↑CMF1d</sub> | 387.25 | -1.2% | +54.4% | 9d | SMA-OK | RS-OK | -0.65% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . ↗491Cr · 108Cr . ↑CMF5d</sub> | 8294.00 | -4.1% | +82.2% | 10d | SMA-OK | RS-OK | -0.75% |
| [SBCL](https://in.tradingview.com/chart/?symbol=NSE:SBCL)<br><sub>✓ SAFE . ↗214Cr · 28Cr . ↑CMF7d</sub> | 1008.65 | -8.7% | +168.8% | 10d | SMA-OK | RS-OK | -1.75% |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>✓ SAFE . ↗138Cr · 573Cr . ↑CMF30d</sub> | 4714.70 | 0.0% | +58.7% | 12d | SMA-OK | RS-OK | +3.26% |
| [BELRISE](https://in.tradingview.com/chart/?symbol=NSE:BELRISE)<br><sub>✓ SAFE . ↗137Cr · 111Cr . ↑CMF5d</sub> | 254.42 | -2.7% | +90.8% | 12d | SMA-OK | RS-OK | -2.65% |
| [AVALON](https://in.tradingview.com/chart/?symbol=NSE:AVALON)<br><sub>✓ SAFE . ↗116Cr · 35Cr . ↑CMF6d</sub> | 1930.40 | -1.8% | +143.2% | 12d | SMA-OK | RS-OK | -1.71% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>✓ SAFE . ↗505Cr · 290Cr . ↑CMF8d</sub> | 7935.00 | -3.1% | +45.1% | 14d | SMA-OK | RS-OK | -0.64% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>✓ SAFE . ↗203Cr · 160Cr . ↑CMF7d</sub> | 1663.40 | -0.2% | +62.7% | 14d | SMA-OK | RS-OK | -0.22% |
| [ABB](https://in.tradingview.com/chart/?symbol=NSE:ABB)<br><sub>✓ SAFE . →350Cr · 120Cr . ↑CMF20d</sub> | 7735.00 | 0.0% | +64.9% | 14d | SMA-OK | RS-OK | +0.58% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>✓ SAFE . ↘147Cr · 41Cr . ↑CMF20d</sub> | 733.30 | -2.4% | +58.5% | 14d | SMA-OK | RS-OK | -1.35% |
| [TIIL](https://in.tradingview.com/chart/?symbol=NSE:TIIL)<br><sub>✓ SAFE . ↗11Cr · 32Cr . ↑CMF1d</sub> | 2887.60 | -3.2% | +51.4% | 14d | SMA-OK | RS-OK | +0.32% |
| [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN)<br><sub>✓ SAFE . ↘48Cr · 29Cr . ↑CMF18d</sub> | 10380.00 | -1.7% | +61.6% | 14d | SMA-OK | RS-OK | -1.25% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . →224Cr · 221Cr . ↑CMF13d</sub> | 220.00 | 0.0% | +67.6% | 16d | SMA-OK | RS-OK | +4.76% |
| [ARMANFIN](https://in.tradingview.com/chart/?symbol=NSE:ARMANFIN)<br><sub>✓ SAFE . ↗16Cr · 62Cr . ↓CMF22d</sub> | 2013.40 | -1.8% | +50.3% | 16d | SMA-OK | RS-OK | +0.12% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>✓ SAFE . ↘94Cr · 55Cr . ↑CMF2d</sub> | 71.19 | -1.6% | +70.8% | 16d | SMA-OK | RS-OK | -1.64% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>✓ SAFE . ↘254Cr · 279Cr . ↑CMF12d</sub> | 11590.00 | -2.6% | +83.9% | 17d | SMA-OK | RS-OK | -2.57% |
| [THYROCARE](https://in.tradingview.com/chart/?symbol=NSE:THYROCARE)<br><sub>✓ SAFE . ↘71Cr · 401Cr . ↓CMF14d</sub> | 606.00 | -6.7% | +73.4% | 19d | SMA-OK | RS-OK | -5.75% |
| [HSCL](https://in.tradingview.com/chart/?symbol=NSE:HSCL)<br><sub>✓ SAFE . ↘274Cr · 278Cr . ↑CMF19d . DEL51%(T-1)</sub> | 778.15 | -2.8% | +84.4% | 19d | SMA-OK | RS-OK | +2.07% |
| [LLOYDSME](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSME)<br><sub>✓ SAFE . ↗139Cr · 74Cr . ↑CMF15d</sub> | 2081.30 | 0.0% | +93.9% | 19d | SMA-OK | RS-OK | +1.38% |
| [AARTIIND](https://in.tradingview.com/chart/?symbol=NSE:AARTIIND)<br><sub>✓ SAFE . ↗146Cr · 153Cr . ↓CMF9d</sub> | 538.20 | 0.0% | +58.3% | 19d | SMA-OK | RS-OK | +1.38% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . ↘171Cr · 124Cr . ↑CMF14d . DEL70%(T-1)</sub> | 115.31 | -1.8% | +108.7% | 19d | SMA-OK | RS-OK | +0.16% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>✓ SAFE . →168Cr · 83Cr . ↓CMF1d . DEL46%(T-1)</sub> | 1247.00 | -11.5% | +112.1% | 19d | SMA-OK | RS-OK | -1.38% |
| [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP)<br><sub>✓ SAFE . ↗66Cr · 53Cr . ↓CMF7d</sub> | 166.02 | -4.5% | +143.4% | 22d | SMA-OK | RS-OK | +4.80% |
| [TITAN](https://in.tradingview.com/chart/?symbol=NSE:TITAN)<br><sub>⚠ CAUTION . ↗422Cr · 629Cr . ↑CMF12d</sub> | 4992.00 | -0.2% | +50.5% | 24d | SMA-OK | RS-OK | +1.62% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>✓ SAFE . ↘337Cr · 345Cr . ↑CMF24d</sub> | 4967.50 | -3.0% | +41.3% | 24d | SMA-OK | RS-OK | -0.65% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>✓ SAFE . ↗162Cr · 44Cr . ↑CMF7d</sub> | 91.15 | -5.9% | +141.6% | 24d | SMA-OK | RS-OK | -1.36% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>✓ SAFE . ↘58Cr · 39Cr . ↑CMF30d</sub> | 335.95 | -3.5% | +65.5% | 24d | SMA-OK | RS-OK | -0.84% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>✓ SAFE . →110Cr · 36Cr . ↑CMF15d</sub> | 312.75 | -0.3% | +89.3% | 24d | SMA-OK | RS-OK | -0.30% |
| [WSTCSTPAPR](https://in.tradingview.com/chart/?symbol=NSE:WSTCSTPAPR)<br><sub>✓ SAFE . ↗28Cr · 30Cr . ↑CMF6d</sub> | 606.10 | -3.0% | +59.0% | 24d | SMA-OK | RS-OK | -2.95% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↗405Cr · 235Cr . ↑CMF5d</sub> | 2967.60 | 0.0% | +85.8% | 25d | SMA-OK | RS-OK | +2.64% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . ↗170Cr · 42Cr . ↑CMF9d</sub> | 355.20 | -0.1% | +63.2% | 26d | SMA-OK | RS-OK | +0.85% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↗454Cr · 248Cr . ↑CMF20d</sub> | 1341.80 | -5.9% | +114.0% | 27d | SMA-OK | RS-OK | -2.73% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>✓ SAFE . →162Cr · 487Cr . ↑CMF0d</sub> | 2665.10 | 0.0% | +95.0% | 29d | SMA-OK | RS-OK | +7.49% |
| [INDUSINDBK](https://in.tradingview.com/chart/?symbol=NSE:INDUSINDBK)<br><sub>✓ SAFE . ↘127Cr · 69Cr . ↑CMF30d</sub> | 1024.70 | -4.2% | +43.8% | 29d | SMA-OK | RS-OK | +0.71% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . ↗989Cr · 612Cr . ↑CMF30d</sub> | 1526.50 | -2.7% | +280.6% | 34d | SMA-OK | RS-OK | -2.73% |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>✓ SAFE . ↗462Cr · 112Cr . ↓CMF5d</sub> | 807.05 | -1.5% | +202.3% | 34d | SMA-OK | RS-OK | +0.23% |
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM)<br><sub>⚠ CAUTION . ↘35Cr · 49Cr . ↑CMF30d</sub> | 3614.60 | 0.0% | +51.3% | 34d | SMA-OK | RS-OK | +2.08% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>✓ SAFE . ↗86Cr · 34Cr . ↓CMF1d</sub> | 1580.10 | -3.3% | +116.2% | 34d | SMA-OK | RS-OK | -2.02% |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS)<br><sub>✓ SAFE . ↗363Cr · 101Cr . ↑CMF9d</sub> | 322.85 | -4.3% | +173.7% | 37d | SMA-OK | RS-OK | -0.35% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>✓ SAFE . ↗192Cr · 89Cr . ↑CMF8d</sub> | 423.00 | -0.4% | +68.2% | 39d | SMA-OK | RS-OK | -0.40% |
| [PANAMAPET](https://in.tradingview.com/chart/?symbol=NSE:PANAMAPET)<br><sub>✓ SAFE . ↗96Cr · 273Cr . ↓CMF1d</sub> | 488.20 | -10.5% | +110.3% | 43d | SMA-OK | RS-OK | +1.59% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . ↗296Cr · 241Cr . ↑CMF0d</sub> | 331.15 | -4.0% | +63.8% | 44d | SMA-OK | RS-OK | +0.94% |
| [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR)<br><sub>✓ SAFE . ↘70Cr · 39Cr . ↓CMF13d . DEL48%(T-1)</sub> | 244.75 | -13.4% | +109.6% | 45d | SMA-OK | RS-OK | +3.58% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>✓ SAFE . ↘145Cr · 95Cr . ↑CMF30d</sub> | 352.45 | -5.2% | +85.6% | 49d | SMA-OK | RS-OK | -1.23% |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB)<br><sub>✓ SAFE . ↗66Cr · 53Cr . ↑CMF2d</sub> | 296.63 | -1.1% | +236.5% | 54d | SMA-OK | RS-OK | -1.12% |
| [DIVGIITTS](https://in.tradingview.com/chart/?symbol=NSE:DIVGIITTS)<br><sub>✓ SAFE . ↗46Cr · 49Cr . ↑CMF3d</sub> | 1219.75 | -1.0% | +109.7% | 54d | SMA-OK | RS-OK | -0.99% |
| [KERNEX](https://in.tradingview.com/chart/?symbol=NSE:KERNEX)<br><sub>✓ SAFE . ↗105Cr · 506Cr . ↓CMF1d</sub> | 2242.70 | -12.0% | +161.7% | 58d | SMA-OK | RS-OK | +3.33% |
| [PARAS](https://in.tradingview.com/chart/?symbol=NSE:PARAS)<br><sub>✓ SAFE . ↗150Cr · 221Cr . ↑CMF6d</sub> | 1342.20 | -4.7% | +129.6% | 58d | SMA-OK | RS-OK | +4.80% |
| [MTARTECH](https://in.tradingview.com/chart/?symbol=NSE:MTARTECH)<br><sub>✓ SAFE . ↗2251Cr · 944Cr . ↑CMF8d</sub> | 7777.00 | -7.1% | +457.1% | 58d | SMA-OK | RS-OK | -4.25% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↗131Cr · 368Cr . ↑CMF1d</sub> | 3786.00 | -2.4% | +206.1% | 59d | SMA-OK | RS-OK | -2.38% |
| [RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO)<br><sub>✓ SAFE . ↘171Cr · 187Cr . ↑CMF6d</sub> | 4675.20 | 0.0% | +84.0% | 61d | SMA-OK | RS-OK | +3.14% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↘199Cr · 139Cr . ↑CMF30d</sub> | 799.90 | -2.2% | +97.4% | 64d | SMA-OK | RS-OK | -0.57% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . →420Cr · 249Cr . ↑CMF30d</sub> | 1851.70 | 0.0% | +125.3% | 66d | SMA-OK | RS-OK | +0.40% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>✓ SAFE . →141Cr · 91Cr . ↑CMF30d</sub> | 1883.90 | 0.0% | +161.0% | 66d | SMA-OK | RS-OK | +0.87% |
| [BLISSGVS](https://in.tradingview.com/chart/?symbol=NSE:BLISSGVS)<br><sub>✓ SAFE . →52Cr · 21Cr . ↑CMF30d</sub> | 527.10 | -2.7% | +312.1% | 68d | SMA-OK | RS-OK | +0.68% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>✓ SAFE . ↗89Cr · 57Cr . ↓CMF5d</sub> | 7230.00 | -2.4% | +168.0% | 72d | SMA-OK | RS-OK | +1.37% |
| [RRKABEL](https://in.tradingview.com/chart/?symbol=NSE:RRKABEL)<br><sub>✓ SAFE . ↘118Cr · 49Cr . ↓CMF3d</sub> | 2834.20 | 0.0% | +142.8% | 74d | SMA-OK | RS-OK | +1.60% |
| [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO)<br><sub>✓ SAFE . ↘80Cr · 73Cr . ↓CMF6d</sub> | 69.94 | -5.2% | +132.4% | 78d | SMA-OK | RS-OK | +1.73% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . ↗113Cr · 69Cr . ↑CMF25d</sub> | 1451.20 | -0.8% | +82.5% | 78d | SMA-OK | RS-OK | -0.85% |
| [HONASA](https://in.tradingview.com/chart/?symbol=NSE:HONASA)<br><sub>✓ SAFE . ↗47Cr · 121Cr . ↓CMF13d</sub> | 479.45 | 0.0% | +87.1% | 82d | SMA-OK | RS-OK | +2.58% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . ↗149Cr · 158Cr . ↓CMF7d</sub> | 773.95 | -7.1% | +194.0% | 83d | SMA-OK | RS-OK | -7.10% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . →1010Cr · 1353Cr . ↑CMF30d</sub> | 294.86 | 0.0% | +792.2% | 96d | SMA-OK | RS-OK | +1.72% |

### By Trend Age

**<2 WEEKS** (64)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AEROFLEX,NSE:ANTHEM,NSE:APARINDS,NSE:ARVIND,NSE:AUBANK,NSE:BHARATSE,NSE:DALMIASUG,NSE:DATAPATTNS,NSE:DIVISLAB,NSE:EDELWEISS,NSE:ENTERO,NSE:EPL,NSE:FINCABLES,NSE:GRANULES,NSE:HEG,NSE:HFCL,NSE:HINDALCO,NSE:IFCI,NSE:INGERRAND,NSE:IPCALAB,NSE:JSWENERGY,NSE:JSWINFRA,NSE:KEI,NSE:KENNAMET,NSE:LALPATHLAB,NSE:MANINDS,NSE:MARINE,NSE:MARKSANS,NSE:MCX,NSE:MIDHANI,NSE:MINDACORP,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:MUNJALAU,NSE:NAVINFLUOR,NSE:NESTLEIND,NSE:NETWEB,NSE:OMAXE,NSE:PNBHOUSING,NSE:POWERINDIA,NSE:PRECWIRE,NSE:PRUDENT,NSE:QPOWER,NSE:RAIN,NSE:RBA,NSE:RBLBANK,NSE:ROLEXRINGS,NSE:SAREGAMA,NSE:SBCL,NSE:SCHNEIDER,NSE:SEAMECLTD,NSE:SHAILY,NSE:SHRIRAMFIN,NSE:SIEMENS,NSE:SMLMAH,NSE:SOLARINDS,NSE:SOMANYCERA,NSE:SYRMA,NSE:TBZ,NSE:TDPOWERSYS,NSE:TVSMOTOR,NSE:VADILALIND,NSE:VIJAYA,NSE:ZENTEC
```

**2-4 WEEKS** (19)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AARTIIND,NSE:ABB,NSE:AEGISLOG,NSE:ARMANFIN,NSE:AUROPHARMA,NSE:AVALON,NSE:BELRISE,NSE:CRAFTSMAN,NSE:EICHERMOT,NSE:FLUOROCHEM,NSE:HSCL,NSE:LLOYDSME,NSE:OFSS,NSE:RATNAVEER,NSE:RKFORGE,NSE:TFCILTD,NSE:THYROCARE,NSE:TIIL,NSE:UJJIVANSFB
```

**1-2 MONTHS** (19)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABCAPITAL,NSE:AETHER,NSE:AJANTPHARM,NSE:ATHERENERG,NSE:AZAD,NSE:CHENNPETRO,NSE:DIACABS,NSE:GLAND,NSE:INDUSINDBK,NSE:IOLCP,NSE:KARURVYSYA,NSE:KTKBANK,NSE:LLOYDSENGG,NSE:NAZARA,NSE:SHILPAMED,NSE:STLTECH,NSE:TITAN,NSE:TORNTPHARM,NSE:WSTCSTPAPR
```

**2-3 MONTHS** (11)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:DIVGIITTS,NSE:FEDERALBNK,NSE:GANDHAR,NSE:INDSWFTLAB,NSE:KERNEX,NSE:MTARTECH,NSE:NYKAA,NSE:PANAMAPET,NSE:PARAS,NSE:RADICO,NSE:SANSERA
```

**3-6 MONTHS** (11)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:BLISSGVS,NSE:CUPID,NSE:GRWRHITECH,NSE:HONASA,NSE:LAURUSLABS,NSE:PAISALO,NSE:RRKABEL,NSE:SAILIFE,NSE:SKYGOLD,NSE:SONACOMS,NSE:WELCORP
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
