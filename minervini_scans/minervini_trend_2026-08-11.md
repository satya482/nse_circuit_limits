> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-08-11
*Generated 2026-08-11 15:45 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [AARTIIND](https://in.tradingview.com/chart/?symbol=NSE:AARTIIND) | [ALIVUS](https://in.tradingview.com/chart/?symbol=NSE:ALIVUS) |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER) | [ANDHRSUGAR](https://in.tradingview.com/chart/?symbol=NSE:ANDHRSUGAR) |
| [CGCL](https://in.tradingview.com/chart/?symbol=NSE:CGCL) | [BEPL](https://in.tradingview.com/chart/?symbol=NSE:BEPL) |
| [COMSYN](https://in.tradingview.com/chart/?symbol=NSE:COMSYN) | [CAPLIPOINT](https://in.tradingview.com/chart/?symbol=NSE:CAPLIPOINT) |
| [FINCABLES](https://in.tradingview.com/chart/?symbol=NSE:FINCABLES) | [CARYSIL](https://in.tradingview.com/chart/?symbol=NSE:CARYSIL) |
| [FINEORG](https://in.tradingview.com/chart/?symbol=NSE:FINEORG) | [DALMIASUG](https://in.tradingview.com/chart/?symbol=NSE:DALMIASUG) |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM) | [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH) |
| [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR) | [EMCURE](https://in.tradingview.com/chart/?symbol=NSE:EMCURE) |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB) | [INDOBORAX](https://in.tradingview.com/chart/?symbol=NSE:INDOBORAX) |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA) | [INDUSINDBK](https://in.tradingview.com/chart/?symbol=NSE:INDUSINDBK) |
| [JSWENERGY](https://in.tradingview.com/chart/?symbol=NSE:JSWENERGY) | [IRISDOREME](https://in.tradingview.com/chart/?symbol=NSE:IRISDOREME) |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS) | [JINDALSAW](https://in.tradingview.com/chart/?symbol=NSE:JINDALSAW) |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX) | [KABRAEXTRU](https://in.tradingview.com/chart/?symbol=NSE:KABRAEXTRU) |
| [POLYPLEX](https://in.tradingview.com/chart/?symbol=NSE:POLYPLEX) | [KIMS](https://in.tradingview.com/chart/?symbol=NSE:KIMS) |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA) | [MINDACORP](https://in.tradingview.com/chart/?symbol=NSE:MINDACORP) |
| [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS) | [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA) |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL) | [NITINSPIN](https://in.tradingview.com/chart/?symbol=NSE:NITINSPIN) |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY) | [NRBBEARING](https://in.tradingview.com/chart/?symbol=NSE:NRBBEARING) |
| [THYROCARE](https://in.tradingview.com/chart/?symbol=NSE:THYROCARE) | [PGIL](https://in.tradingview.com/chart/?symbol=NSE:PGIL) |
| [VENKEYS](https://in.tradingview.com/chart/?symbol=NSE:VENKEYS) | [RICOAUTO](https://in.tradingview.com/chart/?symbol=NSE:RICOAUTO) |
| [ZENTEC](https://in.tradingview.com/chart/?symbol=NSE:ZENTEC) | [SOTL](https://in.tradingview.com/chart/?symbol=NSE:SOTL) |
|  | [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL) |
|  | [SUVEN](https://in.tradingview.com/chart/?symbol=NSE:SUVEN) |
|  | [TALBROAUTO](https://in.tradingview.com/chart/?symbol=NSE:TALBROAUTO) |
|  | [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH) |
|  | [VIJAYA](https://in.tradingview.com/chart/?symbol=NSE:VIJAYA) |
|  | [VINDHYATEL](https://in.tradingview.com/chart/?symbol=NSE:VINDHYATEL) |
|  | [VIYASH](https://in.tradingview.com/chart/?symbol=NSE:VIYASH) |
|  | [VOLTAMP](https://in.tradingview.com/chart/?symbol=NSE:VOLTAMP) |

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

**Qualifying: 115**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ANTHEM,NSE:APARINDS,NSE:ARVIND,NSE:AUBANK,NSE:AVALON,NSE:BELRISE,NSE:CARBORUNIV,NSE:CGCL,NSE:CREDITACC,NSE:DIVISLAB,NSE:ENGINERSIN,NSE:ENTERO,NSE:FINCABLES,NSE:FINEORG,NSE:FLUOROCHEM,NSE:GRANULES,NSE:HEG,NSE:HFCL,NSE:HINDALCO,NSE:JGCHEM,NSE:JSWENERGY,NSE:JSWINFRA,NSE:KEI,NSE:LALPATHLAB,NSE:MARKSANS,NSE:MCX,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:NAVINFLUOR,NSE:NEOGEN,NSE:NESTLEIND,NSE:NETWEB,NSE:OFSS,NSE:PIXTRANS,NSE:PNBHOUSING,NSE:POLYPLEX,NSE:POWERINDIA,NSE:PRECWIRE,NSE:RATEGAIN,NSE:RBLBANK,NSE:ROLEXRINGS,NSE:SBCL,NSE:SCHNEIDER,NSE:SENORES,NSE:SETL,NSE:SHAILY,NSE:SHRIRAMFIN,NSE:SIEMENS,NSE:SMLMAH,NSE:SOLARINDS,NSE:SYRMA,NSE:TDPOWERSYS,NSE:TVSMOTOR,NSE:VENKEYS,NSE:YATHARTH,NSE:ZENTEC,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AARTIIND,NSE:ABB,NSE:AEGISLOG,NSE:AUROPHARMA,NSE:EICHERMOT,NSE:HSCL,NSE:IOLCP,NSE:LLOYDSENT,NSE:LLOYDSME,NSE:RATNAVEER,NSE:RKFORGE,NSE:SENCO,NSE:TFCILTD,NSE:THYROCARE,NSE:UJJIVANSFB,NSE:UNIVCABLES,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABCAPITAL,NSE:AETHER,NSE:ASTERDM,NSE:ATHERENERG,NSE:AZAD,NSE:BALRAMCHIN,NSE:CHENNPETRO,NSE:COMSYN,NSE:CONFIPET,NSE:DIACABS,NSE:GLAND,NSE:GNA,NSE:KARURVYSYA,NSE:KTKBANK,NSE:LLOYDSENGG,NSE:MANAPPURAM,NSE:NYKAA,NSE:SHILPAMED,NSE:STLTECH,NSE:TITAN,NSE:TORNTPHARM,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AKUMS,NSE:BHARATFORG,NSE:FEDERALBNK,NSE:GANDHAR,NSE:INDSWFTLAB,NSE:KERNEX,NSE:MTARTECH,NSE:PARAS,NSE:RADICO,NSE:SANSERA,NSE:SONACOMS,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:CUPID,NSE:GRWRHITECH,NSE:HONASA,NSE:INOXINDIA,NSE:LAURUSLABS,NSE:PAISALO,NSE:RRKABEL,NSE:SAILIFE,NSE:SJS,NSE:SKYGOLD,NSE:WELCORP
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . ↗720Cr · 1212Cr . ↓CMF17d</sub> | 2895.00 | -15.9% | +95.9% | 0d | SMA-OK | RS-OK | +4.92% |
| [FINCABLES](https://in.tradingview.com/chart/?symbol=NSE:FINCABLES)<br><sub>✓ SAFE . ↗136Cr · 1067Cr . ↑CMF1d</sub> | 1207.85 | 0.0% | +69.9% | 0d | SMA-OK | RS-OK | +14.16% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>✓ SAFE . ↗599Cr · 2404Cr . ↑CMF0d</sub> | 36150.00 | -6.0% | +123.0% | 0d | SMA-OK | RS-OK | +10.89% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>✓ SAFE . →488Cr · 631Cr . ↓CMF30d</sub> | 1025.35 | -10.8% | +53.7% | 0d | SMA-OK | RS-OK | -1.41% |
| [ZENTEC](https://in.tradingview.com/chart/?symbol=NSE:ZENTEC)<br><sub>✓ SAFE . →70Cr · 156Cr . ↑CMF4d</sub> | 1819.80 | -8.9% | +48.2% | 0d | SMA-OK | RS-OK | +5.80% |
| [JSWENERGY](https://in.tradingview.com/chart/?symbol=NSE:JSWENERGY)<br><sub>✓ SAFE . ↘94Cr · 110Cr . ↑CMF5d</sub> | 577.50 | -4.1% | +31.2% | 0d | SMA-OK | RS-OK | +2.32% |
| [CGCL](https://in.tradingview.com/chart/?symbol=NSE:CGCL)<br><sub>✓ SAFE . →86Cr · 59Cr . ↓CMF14d</sub> | 235.46 | -9.1% | +54.9% | 0d | SMA-OK | RS-OK | +1.32% |
| [PIXTRANS](https://in.tradingview.com/chart/?symbol=NSE:PIXTRANS)<br><sub>✓ SAFE . ↗33Cr · 51Cr . ↑CMF9d</sub> | 1983.00 | -0.2% | +56.7% | 0d | SMA-OK | RS-OK | -0.18% |
| [CARBORUNIV](https://in.tradingview.com/chart/?symbol=NSE:CARBORUNIV)<br><sub>⚠ CAUTION . ↗24Cr · 42Cr . ↑CMF1d</sub> | 1173.80 | -5.5% | +56.9% | 0d | SMA-OK | RS-OK | +4.71% |
| [SCHNEIDER](https://in.tradingview.com/chart/?symbol=NSE:SCHNEIDER)<br><sub>✓ SAFE . ↗50Cr · 41Cr . ↑CMF1d</sub> | 1403.30 | -6.5% | +142.3% | 0d | SMA-OK | RS-OK | -1.52% |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>✓ SAFE . →34Cr · 39Cr . ↓CMF10d</sub> | 2092.70 | -9.9% | +113.6% | 0d | SMA-OK | RS-OK | -4.13% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>✓ SAFE . ↗755Cr · 485Cr . ↑CMF8d</sub> | 4399.30 | -1.3% | +57.5% | 1d | SMA-OK | RS-OK | -1.25% |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY)<br><sub>✓ SAFE . ↗102Cr · 246Cr . ↑CMF12d</sub> | 3457.90 | 0.0% | +118.1% | 1d | SMA-OK | RS-OK | +2.69% |
| [FINEORG](https://in.tradingview.com/chart/?symbol=NSE:FINEORG)<br><sub>✓ SAFE . ↗23Cr · 119Cr . ↑CMF2d</sub> | 5120.70 | -4.8% | +31.7% | 1d | SMA-OK | RS-OK | +1.85% |
| [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS)<br><sub>✓ SAFE . ↗192Cr · 993Cr . ↑CMF0d</sub> | 177.29 | 0.0% | +76.5% | 2d | SMA-OK | RS-OK | +14.19% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . →563Cr · 321Cr . ↑CMF4d</sub> | 214.24 | -5.2% | +251.5% | 2d | SMA-OK | RS-OK | +0.60% |
| [KEI](https://in.tradingview.com/chart/?symbol=NSE:KEI)<br><sub>✓ SAFE . ↗424Cr · 235Cr . ↑CMF5d</sub> | 5645.00 | -0.3% | +49.9% | 2d | SMA-OK | RS-OK | -0.26% |
| [TDPOWERSYS](https://in.tradingview.com/chart/?symbol=NSE:TDPOWERSYS)<br><sub>✓ SAFE . ↗222Cr · 160Cr . ↑CMF8d</sub> | 1275.60 | -6.7% | +169.8% | 2d | SMA-OK | RS-OK | +3.17% |
| [VENKEYS](https://in.tradingview.com/chart/?symbol=NSE:VENKEYS)<br><sub>✓ SAFE . ↗21Cr · 150Cr . ↓CMF20d</sub> | 1537.80 | -10.0% | +31.3% | 2d | SMA-OK | RS-OK | -1.74% |
| [JGCHEM](https://in.tradingview.com/chart/?symbol=NSE:JGCHEM)<br><sub>✓ SAFE . ↗100Cr · 134Cr . ↑CMF12d</sub> | 622.35 | 0.0% | +103.9% | 2d | SMA-OK | RS-OK | +0.02% |
| [YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH)<br><sub>✓ SAFE . ↗31Cr · 92Cr . ↓CMF0d</sub> | 865.70 | -3.7% | +57.2% | 2d | SMA-OK | RS-OK | -3.68% |
| [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA)<br><sub>✓ SAFE . →114Cr · 84Cr . ↑CMF30d</sub> | 341.85 | -2.7% | +45.9% | 2d | SMA-OK | RS-OK | -0.04% |
| [SENORES](https://in.tradingview.com/chart/?symbol=NSE:SENORES)<br><sub>✓ SAFE . ↘38Cr · 62Cr . ↓CMF10d</sub> | 1475.70 | -0.4% | +128.0% | 2d | SMA-OK | RS-OK | +3.76% |
| [ARVIND](https://in.tradingview.com/chart/?symbol=NSE:ARVIND)<br><sub>✓ SAFE . ↗40Cr · 59Cr . ↓CMF14d</sub> | 567.65 | -3.2% | +103.0% | 2d | SMA-OK | RS-OK | +3.09% |
| [PRECWIRE](https://in.tradingview.com/chart/?symbol=NSE:PRECWIRE)<br><sub>✓ SAFE . ↗23Cr · 53Cr . ↓CMF0d</sub> | 414.20 | -9.4% | +142.8% | 2d | SMA-OK | RS-OK | -4.41% |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN)<br><sub>✓ SAFE . ↗59Cr · 47Cr . ↑CMF4d</sub> | 242.99 | -7.4% | +47.7% | 2d | SMA-OK | RS-OK | -2.00% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>✓ SAFE . ↗174Cr · 44Cr . ↑CMF25d</sub> | 1142.10 | -0.7% | +52.1% | 2d | SMA-OK | RS-OK | -0.63% |
| [GRANULES](https://in.tradingview.com/chart/?symbol=NSE:GRANULES)<br><sub>✓ SAFE . ↘64Cr · 32Cr . ↓CMF11d</sub> | 861.00 | -4.7% | +96.0% | 2d | SMA-OK | RS-OK | +0.68% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>✓ SAFE . ↘70Cr · 143Cr . ↑CMF14d</sub> | 891.65 | 0.0% | +51.7% | 3d | SMA-OK | RS-OK | +4.53% |
| [CREDITACC](https://in.tradingview.com/chart/?symbol=NSE:CREDITACC)<br><sub>✓ SAFE . ↘47Cr · 34Cr . ↑CMF30d</sub> | 1540.30 | -4.6% | +35.7% | 3d | SMA-OK | RS-OK | +0.64% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>✓ SAFE . ↗842Cr · 1414Cr . ↑CMF2d</sub> | 1139.00 | 0.0% | +99.2% | 4d | SMA-OK | RS-OK | +1.48% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>✓ SAFE . →18Cr · 65Cr . ↑CMF0d</sub> | 297.30 | 0.0% | +181.4% | 4d | SMA-OK | RS-OK | +4.78% |
| [HEG](https://in.tradingview.com/chart/?symbol=NSE:HEG)<br><sub>✓ SAFE . ↘101Cr · 52Cr . ↑CMF12d</sub> | 678.25 | -1.2% | +46.8% | 4d | SMA-OK | RS-OK | -0.78% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . ↗604Cr · 264Cr . ↑CMF11d</sub> | 8282.50 | -3.5% | +45.6% | 5d | SMA-OK | RS-OK | -1.26% |
| [SIEMENS](https://in.tradingview.com/chart/?symbol=NSE:SIEMENS)<br><sub>✓ SAFE . →164Cr · 83Cr . ↑CMF8d</sub> | 3955.00 | -1.1% | +38.8% | 5d | SMA-OK | RS-OK | -0.63% |
| [SOLARINDS](https://in.tradingview.com/chart/?symbol=NSE:SOLARINDS)<br><sub>✓ SAFE . ↘135Cr · 114Cr . ↑CMF24d</sub> | 18535.00 | -3.0% | +57.4% | 5d | SMA-OK | RS-OK | +0.73% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>✓ SAFE . ↗39Cr · 88Cr . ↓CMF3d</sub> | 1427.20 | 0.0% | +50.4% | 5d | SMA-OK | RS-OK | +8.52% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↗281Cr · 72Cr . ↑CMF5d</sub> | 76.89 | -4.2% | +128.3% | 5d | SMA-OK | RS-OK | -2.87% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>✓ SAFE . →90Cr · 39Cr . ↑CMF20d</sub> | 1949.90 | -0.2% | +49.1% | 5d | SMA-OK | RS-OK | -0.21% |
| [SMLMAH](https://in.tradingview.com/chart/?symbol=NSE:SMLMAH)<br><sub>✓ SAFE . ↗277Cr · 114Cr . ↑CMF9d</sub> | 5208.50 | -12.0% | +88.4% | 6d | SMA-OK | RS-OK | -0.35% |
| [NETWEB](https://in.tradingview.com/chart/?symbol=NSE:NETWEB)<br><sub>✓ SAFE . ↗838Cr · 332Cr . ↑CMF4d</sub> | 4859.80 | -4.9% | +137.2% | 7d | SMA-OK | RS-OK | -0.88% |
| [APARINDS](https://in.tradingview.com/chart/?symbol=NSE:APARINDS)<br><sub>✓ SAFE . ↗316Cr · 282Cr . ↑CMF6d</sub> | 16748.00 | 0.0% | +140.4% | 7d | SMA-OK | RS-OK | +1.82% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>✓ SAFE . ↗362Cr · 225Cr . ↓CMF8d</sub> | 1494.80 | -1.4% | +133.5% | 7d | SMA-OK | RS-OK | -1.42% |
| [AUBANK](https://in.tradingview.com/chart/?symbol=NSE:AUBANK)<br><sub>✓ SAFE . →173Cr · 201Cr . ↑CMF5d</sub> | 1070.90 | -1.5% | +54.2% | 7d | SMA-OK | RS-OK | +0.27% |
| [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK)<br><sub>✓ SAFE . ↘177Cr · 55Cr . ↓CMF2d</sub> | 389.70 | -0.6% | +55.4% | 7d | SMA-OK | RS-OK | -0.33% |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS)<br><sub>✓ SAFE . ↘26Cr · 40Cr . ↓CMF30d</sub> | 278.95 | 0.0% | +77.8% | 7d | SMA-OK | RS-OK | +2.76% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . ↗470Cr · 194Cr . ↑CMF3d</sub> | 8156.00 | -5.7% | +79.2% | 8d | SMA-OK | RS-OK | -0.49% |
| [SBCL](https://in.tradingview.com/chart/?symbol=NSE:SBCL)<br><sub>✓ SAFE . ↗215Cr · 190Cr . ↑CMF5d</sub> | 1039.20 | -6.0% | +176.9% | 8d | SMA-OK | RS-OK | -5.96% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>✓ SAFE . ↗446Cr · 234Cr . ↑CMF5d</sub> | 1520.00 | -0.7% | +39.5% | 9d | SMA-OK | RS-OK | +0.00% |
| [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON)<br><sub>✓ SAFE . ↗289Cr · 602Cr . ↑CMF5d</sub> | 154.00 | -0.7% | +70.6% | 9d | SMA-OK | RS-OK | -0.23% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>✓ SAFE . ↗749Cr · 298Cr . ↑CMF27d</sub> | 11600.00 | -1.5% | +84.1% | 9d | SMA-OK | RS-OK | +2.36% |
| [RATEGAIN](https://in.tradingview.com/chart/?symbol=NSE:RATEGAIN)<br><sub>✓ SAFE . ↗83Cr · 47Cr . ↓CMF3d</sub> | 908.85 | -7.1% | +112.7% | 9d | SMA-OK | RS-OK | -2.54% |
| [BELRISE](https://in.tradingview.com/chart/?symbol=NSE:BELRISE)<br><sub>✓ SAFE . →115Cr · 75Cr . ↑CMF3d</sub> | 253.97 | 0.0% | +90.5% | 10d | SMA-OK | RS-OK | +0.47% |
| [POLYPLEX](https://in.tradingview.com/chart/?symbol=NSE:POLYPLEX)<br><sub>✓ SAFE . →13Cr · 56Cr . ↑CMF15d</sub> | 1229.60 | 0.0% | +64.4% | 10d | SMA-OK | RS-OK | +4.23% |
| [AVALON](https://in.tradingview.com/chart/?symbol=NSE:AVALON)<br><sub>✓ SAFE . ↗124Cr · 41Cr . ↑CMF4d</sub> | 1938.30 | -1.4% | +144.2% | 10d | SMA-OK | RS-OK | +0.76% |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>✓ SAFE . ↘40Cr · 32Cr . ↑CMF30d</sub> | 4416.20 | -4.3% | +48.7% | 10d | SMA-OK | RS-OK | -1.51% |
| [SENCO](https://in.tradingview.com/chart/?symbol=NSE:SENCO)<br><sub>✓ SAFE . ↘57Cr · 51Cr . ↑CMF15d</sub> | 401.25 | -4.2% | +43.9% | 11d | SMA-OK | RS-OK | +0.60% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>✓ SAFE . ↘159Cr · 124Cr . ↑CMF18d</sub> | 751.35 | 0.0% | +62.4% | 12d | SMA-OK | RS-OK | +2.06% |
| [LLOYDSENT](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENT)<br><sub>✓ SAFE . ↘37Cr · 84Cr . ↑CMF16d</sub> | 80.48 | -3.6% | +94.5% | 12d | SMA-OK | RS-OK | -2.51% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>✓ SAFE . ↗202Cr · 70Cr . ↑CMF5d</sub> | 1658.00 | 0.0% | +62.2% | 12d | SMA-OK | RS-OK | +0.61% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>✓ SAFE . ↗505Cr · 290Cr . ↑CMF8d</sub> | 7935.00 | -3.1% | +45.1% | 14d | SMA-OK | RS-OK | -0.64% |
| [ABB](https://in.tradingview.com/chart/?symbol=NSE:ABB)<br><sub>✓ SAFE . →350Cr · 120Cr . ↑CMF20d</sub> | 7735.00 | 0.0% | +64.9% | 14d | SMA-OK | RS-OK | +0.58% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>✓ SAFE . ↘91Cr · 69Cr . ↑CMF0d</sub> | 70.14 | -2.7% | +68.3% | 14d | SMA-OK | RS-OK | +0.54% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . →203Cr · 38Cr . ↑CMF11d</sub> | 206.16 | -1.5% | +57.0% | 14d | SMA-OK | RS-OK | -0.83% |
| [HSCL](https://in.tradingview.com/chart/?symbol=NSE:HSCL)<br><sub>✓ SAFE . ↘291Cr · 514Cr . ↑CMF17d</sub> | 755.50 | -5.7% | +79.0% | 17d | SMA-OK | RS-OK | -2.14% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . →208Cr · 134Cr . ↑CMF12d</sub> | 115.60 | -1.6% | +109.3% | 17d | SMA-OK | RS-OK | +0.33% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>✓ SAFE . ↘167Cr · 107Cr . ↑CMF30d</sub> | 1297.60 | -7.9% | +120.7% | 17d | SMA-OK | RS-OK | -2.71% |
| [UNIVCABLES](https://in.tradingview.com/chart/?symbol=NSE:UNIVCABLES)<br><sub>✓ SAFE . ↗63Cr · 100Cr . ↑CMF13d</sub> | 1669.40 | -1.4% | +185.6% | 17d | SMA-OK | RS-OK | -1.42% |
| [AARTIIND](https://in.tradingview.com/chart/?symbol=NSE:AARTIIND)<br><sub>✓ SAFE . ↗99Cr · 66Cr . ↓CMF7d</sub> | 505.30 | -1.5% | +48.6% | 17d | SMA-OK | RS-OK | +0.95% |
| [THYROCARE](https://in.tradingview.com/chart/?symbol=NSE:THYROCARE)<br><sub>✓ SAFE . ↘32Cr · 40Cr . ↓CMF12d</sub> | 649.35 | 0.0% | +85.8% | 17d | SMA-OK | RS-OK | +4.38% |
| [LLOYDSME](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSME)<br><sub>✓ SAFE . ↗139Cr · 74Cr . ↑CMF15d</sub> | 2081.30 | 0.0% | +93.9% | 19d | SMA-OK | RS-OK | +1.38% |
| [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP)<br><sub>✓ SAFE . →60Cr · 73Cr . ↓CMF5d</sub> | 164.14 | -5.5% | +140.6% | 20d | SMA-OK | RS-OK | -0.32% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>✓ SAFE . ↗165Cr · 104Cr . ↑CMF5d</sub> | 93.04 | -4.0% | +146.6% | 22d | SMA-OK | RS-OK | -2.40% |
| [ASTERDM](https://in.tradingview.com/chart/?symbol=NSE:ASTERDM)<br><sub>⚠ CAUTION . ↗83Cr · 86Cr . ↓CMF0d</sub> | 854.90 | -1.7% | +58.9% | 22d | SMA-OK | RS-OK | -1.41% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>✓ SAFE . ↗132Cr · 83Cr . ↑CMF13d</sub> | 302.85 | -2.3% | +83.3% | 22d | SMA-OK | RS-OK | -0.79% |
| [COMSYN](https://in.tradingview.com/chart/?symbol=NSE:COMSYN)<br><sub>✓ SAFE . ↗57Cr · 65Cr . ↑CMF1d</sub> | 267.55 | -0.6% | +103.7% | 22d | SMA-OK | RS-OK | -0.55% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>✓ SAFE . ↘60Cr · 38Cr . ↑CMF30d</sub> | 334.20 | -4.0% | +64.7% | 22d | SMA-OK | RS-OK | +0.91% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↗401Cr · 2562Cr . ↑CMF3d</sub> | 2924.40 | 0.0% | +83.1% | 23d | SMA-OK | RS-OK | +9.64% |
| [TITAN](https://in.tradingview.com/chart/?symbol=NSE:TITAN)<br><sub>⚠ CAUTION . ↗422Cr · 629Cr . ↑CMF12d</sub> | 4992.00 | -0.2% | +50.5% | 24d | SMA-OK | RS-OK | +1.62% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>✓ SAFE . ↘337Cr · 345Cr . ↑CMF24d</sub> | 4967.50 | -3.0% | +41.3% | 24d | SMA-OK | RS-OK | -0.65% |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>✓ SAFE . ↗55Cr · 40Cr . ↑CMF6d</sub> | 627.80 | -4.7% | +57.8% | 24d | SMA-OK | RS-OK | -4.19% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . →472Cr · 2458Cr . ↑CMF18d</sub> | 1426.10 | 0.0% | +127.4% | 25d | SMA-OK | RS-OK | +15.00% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>✓ SAFE . →127Cr · 91Cr . ↓CMF3d</sub> | 2472.10 | -3.0% | +80.9% | 27d | SMA-OK | RS-OK | -3.04% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [MANAPPURAM](https://in.tradingview.com/chart/?symbol=NSE:MANAPPURAM)<br><sub>✓ SAFE . ↗266Cr · 219Cr . ↑CMF30d</sub> | 360.00 | -3.2% | +43.4% | 29d | SMA-OK | RS-OK | -2.52% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . →946Cr · 742Cr . ↑CMF30d</sub> | 1525.40 | 0.0% | +295.7% | 32d | SMA-OK | RS-OK | +4.04% |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>✓ SAFE . ↗455Cr · 198Cr . ↓CMF3d</sub> | 819.70 | 0.0% | +207.0% | 32d | SMA-OK | RS-OK | +1.50% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>✓ SAFE . ↗96Cr · 35Cr . ↑CMF0d</sub> | 1634.20 | 0.0% | +123.6% | 32d | SMA-OK | RS-OK | +2.30% |
| [CONFIPET](https://in.tradingview.com/chart/?symbol=NSE:CONFIPET)<br><sub>✓ SAFE . ↗31Cr · 119Cr . ↓CMF0d</sub> | 78.42 | -6.4% | +172.2% | 36d | SMA-OK | RS-OK | -5.22% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>✓ SAFE . ↘32Cr · 49Cr . ↓CMF1d</sub> | 537.35 | -9.2% | +80.3% | 37d | SMA-OK | RS-OK | -0.25% |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS)<br><sub>✓ SAFE . ↗363Cr · 101Cr . ↑CMF9d</sub> | 322.85 | -4.3% | +173.7% | 37d | SMA-OK | RS-OK | -0.35% |
| [ABCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:ABCAPITAL)<br><sub>✓ SAFE . ↗192Cr · 89Cr . ↑CMF8d</sub> | 423.00 | -0.4% | +68.2% | 39d | SMA-OK | RS-OK | -0.40% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . ↗292Cr · 256Cr . ↓CMF2d</sub> | 325.00 | -5.8% | +60.8% | 42d | SMA-OK | RS-OK | +0.40% |
| [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR)<br><sub>✓ SAFE . ↘83Cr · 46Cr . ↓CMF11d</sub> | 243.41 | -13.8% | +108.4% | 43d | SMA-OK | RS-OK | +2.78% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>✓ SAFE . ↘167Cr · 172Cr . ↑CMF30d</sub> | 354.55 | -4.6% | +86.7% | 47d | SMA-OK | RS-OK | -1.06% |
| [AKUMS](https://in.tradingview.com/chart/?symbol=NSE:AKUMS)<br><sub>✓ SAFE . ↗36Cr · 87Cr . ↑CMF15d</sub> | 760.95 | 0.0% | +83.8% | 47d | SMA-OK | RS-OK | +4.23% |
| [BHARATFORG](https://in.tradingview.com/chart/?symbol=NSE:BHARATFORG)<br><sub>✓ SAFE . →154Cr · 194Cr . ↑CMF30d</sub> | 2210.00 | -0.0% | +99.7% | 48d | SMA-OK | RS-OK | +0.59% |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB)<br><sub>✓ SAFE . ↗37Cr · 260Cr . ↑CMF0d</sub> | 284.68 | 0.0% | +222.9% | 52d | SMA-OK | RS-OK | +20.00% |
| [PARAS](https://in.tradingview.com/chart/?symbol=NSE:PARAS)<br><sub>✓ SAFE . ↗133Cr · 69Cr . ↑CMF4d</sub> | 1284.00 | -8.8% | +119.6% | 56d | SMA-OK | RS-OK | +1.30% |
| [KERNEX](https://in.tradingview.com/chart/?symbol=NSE:KERNEX)<br><sub>✓ SAFE . ↗52Cr · 54Cr . ↑CMF0d</sub> | 2387.30 | -6.4% | +178.6% | 56d | SMA-OK | RS-OK | +3.34% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . →89Cr · 125Cr . ↓CMF16d</sub> | 3685.10 | -4.6% | +197.9% | 57d | SMA-OK | RS-OK | -3.34% |
| [MTARTECH](https://in.tradingview.com/chart/?symbol=NSE:MTARTECH)<br><sub>✓ SAFE . ↗2251Cr · 944Cr . ↑CMF8d</sub> | 7777.00 | -7.1% | +457.1% | 58d | SMA-OK | RS-OK | -4.25% |
| [RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO)<br><sub>✓ SAFE . →235Cr · 96Cr . ↑CMF4d</sub> | 4545.00 | -0.1% | +78.9% | 59d | SMA-OK | RS-OK | -0.11% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . →247Cr · 110Cr . ↑CMF28d</sub> | 800.00 | -2.2% | +97.4% | 62d | SMA-OK | RS-OK | -1.54% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>✓ SAFE . →144Cr · 141Cr . ↑CMF30d</sub> | 1836.90 | -0.6% | +154.5% | 64d | SMA-OK | RS-OK | -0.63% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . ↗540Cr · 286Cr . ↑CMF30d</sub> | 1844.30 | -0.3% | +124.4% | 65d | SMA-OK | RS-OK | +0.78% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>✓ SAFE . ↗84Cr · 32Cr . ↓CMF3d</sub> | 7020.50 | -5.3% | +160.3% | 70d | SMA-OK | RS-OK | +0.28% |
| [RRKABEL](https://in.tradingview.com/chart/?symbol=NSE:RRKABEL)<br><sub>✓ SAFE . ↘143Cr · 88Cr . ↓CMF1d</sub> | 2812.80 | 0.0% | +140.9% | 72d | SMA-OK | RS-OK | +2.03% |
| [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS)<br><sub>✓ SAFE . ↗48Cr · 71Cr . ↑CMF7d</sub> | 2402.80 | -4.3% | +108.6% | 72d | SMA-OK | RS-OK | +1.30% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . ↗109Cr · 104Cr . ↑CMF23d</sub> | 1444.40 | 0.0% | +82.5% | 76d | SMA-OK | RS-OK | +1.28% |
| [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO)<br><sub>✓ SAFE . ↘79Cr · 42Cr . ↓CMF4d</sub> | 69.31 | -6.1% | +130.3% | 76d | SMA-OK | RS-OK | -0.90% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>✓ SAFE . ↘38Cr · 54Cr . ↑CMF1d</sub> | 1938.00 | -7.4% | +80.8% | 79d | SMA-OK | RS-OK | -2.32% |
| [HONASA](https://in.tradingview.com/chart/?symbol=NSE:HONASA)<br><sub>✓ SAFE . →37Cr · 39Cr . ↓CMF11d</sub> | 467.30 | -2.2% | +82.3% | 80d | SMA-OK | RS-OK | -2.05% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . ↗137Cr · 123Cr . ↓CMF5d</sub> | 790.05 | 0.0% | +200.1% | 81d | SMA-OK | RS-OK | +1.34% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . →844Cr · 1048Cr . ↑CMF30d</sub> | 276.65 | 0.0% | +737.1% | 94d | SMA-OK | RS-OK | +5.31% |

### By Trend Age

**<2 WEEKS** (56)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ANTHEM,NSE:APARINDS,NSE:ARVIND,NSE:AUBANK,NSE:AVALON,NSE:BELRISE,NSE:CARBORUNIV,NSE:CGCL,NSE:CREDITACC,NSE:DIVISLAB,NSE:ENGINERSIN,NSE:ENTERO,NSE:FINCABLES,NSE:FINEORG,NSE:FLUOROCHEM,NSE:GRANULES,NSE:HEG,NSE:HFCL,NSE:HINDALCO,NSE:JGCHEM,NSE:JSWENERGY,NSE:JSWINFRA,NSE:KEI,NSE:LALPATHLAB,NSE:MARKSANS,NSE:MCX,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:NAVINFLUOR,NSE:NEOGEN,NSE:NESTLEIND,NSE:NETWEB,NSE:OFSS,NSE:PIXTRANS,NSE:PNBHOUSING,NSE:POLYPLEX,NSE:POWERINDIA,NSE:PRECWIRE,NSE:RATEGAIN,NSE:RBLBANK,NSE:ROLEXRINGS,NSE:SBCL,NSE:SCHNEIDER,NSE:SENORES,NSE:SETL,NSE:SHAILY,NSE:SHRIRAMFIN,NSE:SIEMENS,NSE:SMLMAH,NSE:SOLARINDS,NSE:SYRMA,NSE:TDPOWERSYS,NSE:TVSMOTOR,NSE:VENKEYS,NSE:YATHARTH,NSE:ZENTEC
```

**2-4 WEEKS** (16)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AARTIIND,NSE:ABB,NSE:AEGISLOG,NSE:AUROPHARMA,NSE:EICHERMOT,NSE:HSCL,NSE:IOLCP,NSE:LLOYDSENT,NSE:LLOYDSME,NSE:RATNAVEER,NSE:RKFORGE,NSE:SENCO,NSE:TFCILTD,NSE:THYROCARE,NSE:UJJIVANSFB,NSE:UNIVCABLES
```

**1-2 MONTHS** (21)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABCAPITAL,NSE:AETHER,NSE:ASTERDM,NSE:ATHERENERG,NSE:AZAD,NSE:BALRAMCHIN,NSE:CHENNPETRO,NSE:COMSYN,NSE:CONFIPET,NSE:DIACABS,NSE:GLAND,NSE:GNA,NSE:KARURVYSYA,NSE:KTKBANK,NSE:LLOYDSENGG,NSE:MANAPPURAM,NSE:NYKAA,NSE:SHILPAMED,NSE:STLTECH,NSE:TITAN,NSE:TORNTPHARM
```

**2-3 MONTHS** (11)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AKUMS,NSE:BHARATFORG,NSE:FEDERALBNK,NSE:GANDHAR,NSE:INDSWFTLAB,NSE:KERNEX,NSE:MTARTECH,NSE:PARAS,NSE:RADICO,NSE:SANSERA,NSE:SONACOMS
```

**3-6 MONTHS** (11)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CUPID,NSE:GRWRHITECH,NSE:HONASA,NSE:INOXINDIA,NSE:LAURUSLABS,NSE:PAISALO,NSE:RRKABEL,NSE:SAILIFE,NSE:SJS,NSE:SKYGOLD,NSE:WELCORP
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
