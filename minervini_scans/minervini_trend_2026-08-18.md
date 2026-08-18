> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-08-18
*Generated 2026-08-18 15:45 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS) | [APEX](https://in.tradingview.com/chart/?symbol=NSE:APEX) |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER) | [APOLLOPIPE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOPIPE) |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS) | [ARVIND](https://in.tradingview.com/chart/?symbol=NSE:ARVIND) |
| [ASTRAMICRO](https://in.tradingview.com/chart/?symbol=NSE:ASTRAMICRO) | [AVADHSUGAR](https://in.tradingview.com/chart/?symbol=NSE:AVADHSUGAR) |
| [BLISSGVS](https://in.tradingview.com/chart/?symbol=NSE:BLISSGVS) | [DALMIASUG](https://in.tradingview.com/chart/?symbol=NSE:DALMIASUG) |
| [CARBORUNIV](https://in.tradingview.com/chart/?symbol=NSE:CARBORUNIV) | [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG) |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH) | [EDELWEISS](https://in.tradingview.com/chart/?symbol=NSE:EDELWEISS) |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN) | [EPL](https://in.tradingview.com/chart/?symbol=NSE:EPL) |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL) | [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH) |
| [GAEL](https://in.tradingview.com/chart/?symbol=NSE:GAEL) | [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP) |
| [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR) | [KINGFA](https://in.tradingview.com/chart/?symbol=NSE:KINGFA) |
| [ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL) | [KPIL](https://in.tradingview.com/chart/?symbol=NSE:KPIL) |
| [INDUSINDBK](https://in.tradingview.com/chart/?symbol=NSE:INDUSINDBK) | [NRBBEARING](https://in.tradingview.com/chart/?symbol=NSE:NRBBEARING) |
| [JGCHEM](https://in.tradingview.com/chart/?symbol=NSE:JGCHEM) | [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA) |
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL) | [OMAXE](https://in.tradingview.com/chart/?symbol=NSE:OMAXE) |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB) | [PICCADIL](https://in.tradingview.com/chart/?symbol=NSE:PICCADIL) |
| [LLOYDSENT](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENT) | [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA) |
| [MACPOWER](https://in.tradingview.com/chart/?symbol=NSE:MACPOWER) | [SEAMECLTD](https://in.tradingview.com/chart/?symbol=NSE:SEAMECLTD) |
| [MMFL](https://in.tradingview.com/chart/?symbol=NSE:MMFL) | [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL) |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA) | [SUVEN](https://in.tradingview.com/chart/?symbol=NSE:SUVEN) |
| [NITINSPIN](https://in.tradingview.com/chart/?symbol=NSE:NITINSPIN) | [UNIVCABLES](https://in.tradingview.com/chart/?symbol=NSE:UNIVCABLES) |
| [QUESS](https://in.tradingview.com/chart/?symbol=NSE:QUESS) | [VADILALIND](https://in.tradingview.com/chart/?symbol=NSE:VADILALIND) |
| [RATEGAIN](https://in.tradingview.com/chart/?symbol=NSE:RATEGAIN) |  |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD) |  |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON) |  |
| [STYLAMIND](https://in.tradingview.com/chart/?symbol=NSE:STYLAMIND) |  |
| [VISHNU](https://in.tradingview.com/chart/?symbol=NSE:VISHNU) |  |
| [WABAG](https://in.tradingview.com/chart/?symbol=NSE:WABAG) |  |
| [YASHO](https://in.tradingview.com/chart/?symbol=NSE:YASHO) |  |

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

**Qualifying: 136**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ACUTAAS,NSE:AEROFLEX,NSE:ANTELOPUS,NSE:ANTHEM,NSE:ASIANENE,NSE:ASTRAMICRO,NSE:BHEL,NSE:BOSCHLTD,NSE:CARBORUNIV,NSE:CYIENTDLM,NSE:DATAPATTNS,NSE:DYNAMATECH,NSE:ELGIEQUIP,NSE:ENGINERSIN,NSE:FINCABLES,NSE:GABRIEL,NSE:GRANULES,NSE:HEG,NSE:HFCL,NSE:HINDALCO,NSE:ICIL,NSE:IDEAFORGE,NSE:IFCI,NSE:IPCALAB,NSE:JGCHEM,NSE:JINDRILL,NSE:JSWENERGY,NSE:JSWINFRA,NSE:KEI,NSE:KRN,NSE:LALPATHLAB,NSE:LLOYDSENT,NSE:MANINDS,NSE:MARINE,NSE:MCX,NSE:MIDHANI,NSE:MINDACORP,NSE:MOREPENLAB,NSE:MSTCLTD,NSE:MUNJALAU,NSE:NEOGEN,NSE:NITINSPIN,NSE:PIDILITIND,NSE:PNBHOUSING,NSE:POWERINDIA,NSE:RATEGAIN,NSE:RAYMOND,NSE:RBA,NSE:ROLEXRINGS,NSE:ROSSTECH,NSE:SENORES,NSE:SHANTIGOLD,NSE:SHRIRAMFIN,NSE:TDPOWERSYS,NSE:TVSMOTOR,NSE:VISHNU,NSE:WABAG,NSE:WELSPUNLIV,NSE:ZENTEC,NSE:ZYDUSLIFE,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABB,NSE:APARINDS,NSE:AUBANK,NSE:AUROPHARMA,NSE:AVALON,NSE:CRAFTSMAN,NSE:DIVISLAB,NSE:EICHERMOT,NSE:FLUOROCHEM,NSE:GAEL,NSE:MARKSANS,NSE:MOTHERSON,NSE:NAVINFLUOR,NSE:NESTLEIND,NSE:NETWEB,NSE:OFSS,NSE:QUESS,NSE:RATNAVEER,NSE:RBLBANK,NSE:RKFORGE,NSE:SIEMENS,NSE:SMLMAH,NSE:SOLARINDS,NSE:SYRMA,NSE:TIIL,NSE:UJJIVANSFB,NSE:UNIMECH,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AARTIIND,NSE:AEGISLOG,NSE:AETHER,NSE:AJANTPHARM,NSE:ATHERENERG,NSE:AZAD,NSE:BALRAMCHIN,NSE:CHENNPETRO,NSE:DIACABS,NSE:GLAND,NSE:GNA,NSE:HAPPYFORGE,NSE:HSCL,NSE:INDUSINDBK,NSE:KARURVYSYA,NSE:KTKBANK,NSE:LLOYDSENGG,NSE:MACPOWER,NSE:MANORAMA,NSE:MMFL,NSE:NAZARA,NSE:SHILPAMED,NSE:STLTECH,NSE:TFCILTD,NSE:TITAN,NSE:YASHO,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:DIVGIITTS,NSE:FEDERALBNK,NSE:GANDHAR,NSE:INDSWFTLAB,NSE:KMEW,NSE:MTARTECH,NSE:PANAMAPET,NSE:PARAS,NSE:SANSERA,NSE:SHRIPISTON,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:BLISSGVS,NSE:CUPID,NSE:HONASA,NSE:LAURUSLABS,NSE:RADICO,NSE:RISHABH,NSE:RRKABEL,NSE:SAILIFE,NSE:SJS,NSE:SKYGOLD,NSE:SONACOMS,NSE:STYLAMIND,NSE:WELCORP
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [JINDRILL](https://in.tradingview.com/chart/?symbol=NSE:JINDRILL)<br><sub>✓ SAFE . ↗127Cr · 1165Cr . ↑CMF4d</sub> | 651.15 | -2.8% | +46.2% | 0d | SMA-OK | RS-OK | +11.08% |
| [ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL)<br><sub>✓ SAFE . ↗136Cr · 1104Cr . ↑CMF0d</sub> | 437.70 | -0.9% | +95.8% | 0d | SMA-OK | RS-OK | +12.61% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>✓ SAFE . →344Cr · 476Cr . ↑CMF0d</sub> | 423.35 | -2.8% | +103.5% | 0d | SMA-OK | RS-OK | +0.80% |
| [NITINSPIN](https://in.tradingview.com/chart/?symbol=NSE:NITINSPIN)<br><sub>✓ SAFE . ↗31Cr · 225Cr . ↑CMF0d</sub> | 606.90 | 0.0% | +98.8% | 0d | SMA-OK | RS-OK | +9.60% |
| [ASIANENE](https://in.tradingview.com/chart/?symbol=NSE:ASIANENE)<br><sub>✓ SAFE . ↗40Cr · 169Cr . ↑CMF14d</sub> | 463.05 | 0.0% | +97.9% | 0d | SMA-OK | RS-OK | +8.89% |
| [POWERINDIA](https://in.tradingview.com/chart/?symbol=NSE:POWERINDIA)<br><sub>✓ SAFE . ↗599Cr · 2404Cr . ↑CMF0d</sub> | 36150.00 | -6.0% | +123.0% | 0d | SMA-OK | RS-OK | +10.89% |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>✓ SAFE . ↗210Cr · 151Cr . ↓CMF6d</sub> | 1882.10 | -1.0% | +48.3% | 0d | SMA-OK | RS-OK | -0.13% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>✓ SAFE . ↘77Cr · 144Cr . ↓CMF16d</sub> | 3391.40 | -8.2% | +160.9% | 0d | SMA-OK | RS-OK | +6.04% |
| [WABAG](https://in.tradingview.com/chart/?symbol=NSE:WABAG)<br><sub>✓ SAFE . ↘81Cr · 129Cr . ↓CMF20d</sub> | 1980.60 | -10.8% | +88.8% | 0d | SMA-OK | RS-OK | +4.37% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>✓ SAFE . ↗237Cr · 90Cr . ↑CMF3d</sub> | 1136.80 | -5.7% | +32.1% | 0d | SMA-OK | RS-OK | -2.61% |
| [MIDHANI](https://in.tradingview.com/chart/?symbol=NSE:MIDHANI)<br><sub>✓ SAFE . ↗140Cr · 68Cr . ↑CMF3d</sub> | 437.50 | -2.9% | +61.8% | 0d | SMA-OK | RS-OK | +2.08% |
| [JSWENERGY](https://in.tradingview.com/chart/?symbol=NSE:JSWENERGY)<br><sub>✓ SAFE . ↘94Cr · 110Cr . ↑CMF5d</sub> | 577.50 | -4.1% | +31.2% | 0d | SMA-OK | RS-OK | +2.32% |
| [ASTRAMICRO](https://in.tradingview.com/chart/?symbol=NSE:ASTRAMICRO)<br><sub>✓ SAFE . ↘84Cr · 55Cr . ↓CMF13d</sub> | 1767.40 | -5.1% | +106.5% | 0d | SMA-OK | RS-OK | +3.53% |
| [LLOYDSENT](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENT)<br><sub>✓ SAFE . ↗38Cr · 54Cr . ↓CMF4d</sub> | 79.03 | -5.4% | +91.0% | 0d | SMA-OK | RS-OK | +4.47% |
| [VISHNU](https://in.tradingview.com/chart/?symbol=NSE:VISHNU)<br><sub>✓ SAFE . →8Cr · 37Cr . ↓CMF21d</sub> | 637.50 | -0.5% | +40.8% | 0d | SMA-OK | RS-OK | +3.11% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>✓ SAFE . ↘14Cr · 33Cr . ↓CMF16d</sub> | 856.55 | -6.4% | +138.3% | 0d | SMA-OK | RS-OK | +6.95% |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . ↗995Cr · 969Cr . ↑CMF4d</sub> | 3040.00 | -11.7% | +105.7% | 2d | SMA-OK | RS-OK | +3.64% |
| [DATAPATTNS](https://in.tradingview.com/chart/?symbol=NSE:DATAPATTNS)<br><sub>✓ SAFE . ↘297Cr · 656Cr . ↑CMF19d</sub> | 4737.20 | -2.7% | +117.1% | 2d | SMA-OK | RS-OK | +4.60% |
| [ZENTEC](https://in.tradingview.com/chart/?symbol=NSE:ZENTEC)<br><sub>✓ SAFE . ↗128Cr · 544Cr . ↑CMF9d</sub> | 1982.40 | -0.7% | +61.4% | 2d | SMA-OK | RS-OK | +6.32% |
| [IFCI](https://in.tradingview.com/chart/?symbol=NSE:IFCI)<br><sub>✓ SAFE . →165Cr · 406Cr . ↑CMF5d</sub> | 81.36 | -9.7% | +73.8% | 2d | SMA-OK | RS-OK | +3.08% |
| [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN)<br><sub>✓ SAFE . ↗70Cr · 329Cr . ↓CMF15d</sub> | 2328.50 | 0.0% | +137.7% | 2d | SMA-OK | RS-OK | +2.57% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>✓ SAFE . ↘64Cr · 156Cr . ↑CMF4d</sub> | 485.85 | -4.9% | +206.0% | 2d | SMA-OK | RS-OK | +6.58% |
| [FINCABLES](https://in.tradingview.com/chart/?symbol=NSE:FINCABLES)<br><sub>✓ SAFE . ↗488Cr · 118Cr . ↑CMF1d</sub> | 1329.35 | 0.0% | +87.0% | 2d | SMA-OK | RS-OK | +0.64% |
| [MSTCLTD](https://in.tradingview.com/chart/?symbol=NSE:MSTCLTD)<br><sub>✓ SAFE . ↗28Cr · 89Cr . ↑CMF2d</sub> | 701.55 | -3.5% | +91.8% | 2d | SMA-OK | RS-OK | +7.40% |
| [IDEAFORGE](https://in.tradingview.com/chart/?symbol=NSE:IDEAFORGE)<br><sub>✓ SAFE . ↘131Cr · 72Cr . ↑CMF22d . DEL54%(T-1)</sub> | 834.85 | -2.1% | +124.6% | 2d | SMA-OK | RS-OK | +5.00% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>✓ SAFE . ↘51Cr · 69Cr . ↑CMF30d</sub> | 736.10 | -0.2% | +170.3% | 2d | SMA-OK | RS-OK | -0.18% |
| [KRN](https://in.tradingview.com/chart/?symbol=NSE:KRN)<br><sub>✓ SAFE . ↘88Cr · 65Cr . ↓CMF6d . DEL60%(T-1)</sub> | 1522.10 | -1.1% | +154.5% | 2d | SMA-OK | RS-OK | -1.14% |
| [CARBORUNIV](https://in.tradingview.com/chart/?symbol=NSE:CARBORUNIV)<br><sub>⚠ CAUTION . ↗32Cr · 59Cr . ↓CMF1d</sub> | 1126.00 | -9.3% | +50.5% | 2d | SMA-OK | RS-OK | +0.29% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>✓ SAFE . ↗103Cr · 50Cr . ↓CMF30d</sub> | 645.15 | 0.0% | +107.7% | 2d | SMA-OK | RS-OK | +2.35% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↗42Cr · 46Cr . ↑CMF5d</sub> | 625.00 | -4.5% | +94.2% | 2d | SMA-OK | RS-OK | -3.53% |
| [ELGIEQUIP](https://in.tradingview.com/chart/?symbol=NSE:ELGIEQUIP)<br><sub>✓ SAFE . ↗63Cr · 37Cr . ↑CMF14d</sub> | 614.20 | -1.6% | +47.8% | 2d | SMA-OK | RS-OK | -1.60% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↗271Cr · 955Cr . ↓CMF14d</sub> | 177.79 | 0.0% | +64.1% | 3d | SMA-OK | RS-OK | +5.73% |
| [GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL)<br><sub>✓ SAFE . ↘43Cr · 30Cr . ↑CMF30d</sub> | 1467.60 | -7.6% | +78.3% | 3d | SMA-OK | RS-OK | +1.74% |
| [RATEGAIN](https://in.tradingview.com/chart/?symbol=NSE:RATEGAIN)<br><sub>✓ SAFE . ↗86Cr · 29Cr . ↓CMF8d</sub> | 935.95 | -4.3% | +113.6% | 3d | SMA-OK | RS-OK | -1.43% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>✓ SAFE . ↗62Cr · 66Cr . ↑CMF2d</sub> | 253.85 | -4.9% | +62.1% | 4d | SMA-OK | RS-OK | -4.87% |
| [MUNJALAU](https://in.tradingview.com/chart/?symbol=NSE:MUNJALAU)<br><sub>✓ SAFE . ↗94Cr · 35Cr . ↑CMF3d</sub> | 118.39 | -1.8% | +74.7% | 4d | SMA-OK | RS-OK | -1.11% |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE)<br><sub>↗63Cr · 31Cr . ↑CMF11d</sub> | 376.80 | 0.0% | +148.4% | 4d | SMA-OK | RS-OK | +2.64% |
| [HINDALCO](https://in.tradingview.com/chart/?symbol=NSE:HINDALCO)<br><sub>✓ SAFE . ↗650Cr · 340Cr . ↑CMF5d</sub> | 1036.05 | -9.9% | +55.3% | 5d | SMA-OK | RS-OK | -0.97% |
| [RBA](https://in.tradingview.com/chart/?symbol=NSE:RBA)<br><sub>✓ SAFE . ↗323Cr · 182Cr . ↑CMF10d</sub> | 106.34 | 0.0% | +85.7% | 5d | SMA-OK | RS-OK | +6.78% |
| [PIDILITIND](https://in.tradingview.com/chart/?symbol=NSE:PIDILITIND)<br><sub>✓ SAFE . →224Cr · 112Cr . ↑CMF14d</sub> | 1699.10 | -0.1% | +33.4% | 5d | SMA-OK | RS-OK | +0.18% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>✓ SAFE . ↗271Cr · 157Cr . ↑CMF7d</sub> | 47250.00 | 0.0% | +64.4% | 6d | SMA-OK | RS-OK | +1.07% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘516Cr · 822Cr . ↑CMF9d</sub> | 230.03 | 0.0% | +277.4% | 7d | SMA-OK | RS-OK | +4.80% |
| [TDPOWERSYS](https://in.tradingview.com/chart/?symbol=NSE:TDPOWERSYS)<br><sub>✓ SAFE . ↗396Cr · 285Cr . ↑CMF13d</sub> | 1586.60 | 0.0% | +218.0% | 7d | SMA-OK | RS-OK | +2.44% |
| [TVSMOTOR](https://in.tradingview.com/chart/?symbol=NSE:TVSMOTOR)<br><sub>✓ SAFE . ↘431Cr · 236Cr . ↑CMF14d</sub> | 4314.50 | -3.4% | +45.6% | 7d | SMA-OK | RS-OK | -0.64% |
| [KEI](https://in.tradingview.com/chart/?symbol=NSE:KEI)<br><sub>✓ SAFE . ↘244Cr · 180Cr . ↑CMF10d</sub> | 5790.00 | -1.4% | +52.2% | 7d | SMA-OK | RS-OK | -1.41% |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH)<br><sub>✓ SAFE . ↘35Cr · 99Cr . ↓CMF0d</sub> | 1103.55 | -0.5% | +92.3% | 7d | SMA-OK | RS-OK | -0.48% |
| [PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING)<br><sub>✓ SAFE . ↗146Cr · 85Cr . ↑CMF30d</sub> | 1145.80 | -1.6% | +52.6% | 7d | SMA-OK | RS-OK | -0.43% |
| [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA)<br><sub>✓ SAFE . →96Cr · 61Cr . ↑CMF30d</sub> | 328.65 | -6.4% | +40.3% | 7d | SMA-OK | RS-OK | -2.01% |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN)<br><sub>✓ SAFE . ↗82Cr · 60Cr . ↑CMF9d</sub> | 244.78 | -6.7% | +48.7% | 7d | SMA-OK | RS-OK | +1.92% |
| [JGCHEM](https://in.tradingview.com/chart/?symbol=NSE:JGCHEM)<br><sub>✓ SAFE . ↗116Cr · 56Cr . ↑CMF17d</sub> | 645.85 | 0.0% | +111.6% | 7d | SMA-OK | RS-OK | +7.50% |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH)<br><sub>✓ SAFE . ↗34Cr · 39Cr . ↓CMF30d</sub> | 11770.00 | -6.1% | +83.4% | 7d | SMA-OK | RS-OK | +5.82% |
| [SENORES](https://in.tradingview.com/chart/?symbol=NSE:SENORES)<br><sub>✓ SAFE . →43Cr · 37Cr . ↑CMF1d</sub> | 1537.50 | -0.5% | +128.3% | 7d | SMA-OK | RS-OK | -0.53% |
| [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS)<br><sub>✓ SAFE . ↗240Cr · 36Cr . ↑CMF5d</sub> | 177.06 | -1.3% | +76.3% | 7d | SMA-OK | RS-OK | -1.34% |
| [GRANULES](https://in.tradingview.com/chart/?symbol=NSE:GRANULES)<br><sub>✓ SAFE . ↘46Cr · 35Cr . ↓CMF16d</sub> | 851.20 | -5.8% | +85.8% | 7d | SMA-OK | RS-OK | -1.20% |
| [ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM)<br><sub>✓ SAFE . ↘61Cr · 43Cr . ↑CMF19d</sub> | 891.05 | -0.8% | +51.6% | 8d | SMA-OK | RS-OK | -0.77% |
| [HEG](https://in.tradingview.com/chart/?symbol=NSE:HEG)<br><sub>✓ SAFE . ↘139Cr · 401Cr . ↑CMF2d</sub> | 739.25 | 0.0% | +60.0% | 9d | SMA-OK | RS-OK | +5.86% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↗412Cr · 304Cr . ↑CMF10d</sub> | 88.44 | -1.5% | +162.6% | 10d | SMA-OK | RS-OK | -1.54% |
| [SHRIRAMFIN](https://in.tradingview.com/chart/?symbol=NSE:SHRIRAMFIN)<br><sub>✓ SAFE . ↘562Cr · 268Cr . ↑CMF8d</sub> | 1124.90 | -1.2% | +96.8% | 10d | SMA-OK | RS-OK | -0.65% |
| [MINDACORP](https://in.tradingview.com/chart/?symbol=NSE:MINDACORP)<br><sub>✓ SAFE . ↗89Cr · 122Cr . ↓CMF3d</sub> | 745.25 | 0.0% | +55.0% | 10d | SMA-OK | RS-OK | +2.77% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>✓ SAFE . ↘48Cr · 40Cr . ↑CMF25d</sub> | 1901.40 | -3.4% | +45.4% | 10d | SMA-OK | RS-OK | +1.28% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . →498Cr · 283Cr . ↑CMF17d</sub> | 8475.00 | -1.5% | +49.0% | 11d | SMA-OK | RS-OK | -0.29% |
| [SOLARINDS](https://in.tradingview.com/chart/?symbol=NSE:SOLARINDS)<br><sub>✓ SAFE . ↗338Cr · 965Cr . ↑CMF30d</sub> | 19970.00 | -1.7% | +69.6% | 11d | SMA-OK | RS-OK | -1.74% |
| [SMLMAH](https://in.tradingview.com/chart/?symbol=NSE:SMLMAH)<br><sub>✓ SAFE . ↘105Cr · 48Cr . ↑CMF14d</sub> | 5309.50 | -10.3% | +92.0% | 11d | SMA-OK | RS-OK | -0.22% |
| [SIEMENS](https://in.tradingview.com/chart/?symbol=NSE:SIEMENS)<br><sub>✓ SAFE . ↗208Cr · 117Cr . ↑CMF14d</sub> | 3936.00 | -2.1% | +38.2% | 11d | SMA-OK | RS-OK | -1.28% |
| [NETWEB](https://in.tradingview.com/chart/?symbol=NSE:NETWEB)<br><sub>✓ SAFE . →848Cr · 1282Cr . ↑CMF9d</sub> | 5354.50 | 0.0% | +161.4% | 12d | SMA-OK | RS-OK | +2.73% |
| [APARINDS](https://in.tradingview.com/chart/?symbol=NSE:APARINDS)<br><sub>✓ SAFE . →357Cr · 583Cr . ↑CMF11d</sub> | 17214.00 | -4.4% | +147.1% | 12d | SMA-OK | RS-OK | +4.18% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>✓ SAFE . ↘208Cr · 349Cr . ↓CMF13d</sub> | 1500.10 | -1.1% | +134.3% | 12d | SMA-OK | RS-OK | +2.19% |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS)<br><sub>✓ SAFE . ↗328Cr · 108Cr . ↑CMF4d</sub> | 326.50 | -2.0% | +108.1% | 12d | SMA-OK | RS-OK | -1.49% |
| [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK)<br><sub>✓ SAFE . ↘91Cr · 89Cr . ↑CMF4d</sub> | 383.00 | -2.3% | +52.7% | 12d | SMA-OK | RS-OK | +0.39% |
| [AUBANK](https://in.tradingview.com/chart/?symbol=NSE:AUBANK)<br><sub>✓ SAFE . ↘159Cr · 48Cr . ↑CMF10d</sub> | 1075.70 | -2.0% | +54.9% | 12d | SMA-OK | RS-OK | +0.33% |
| [GAEL](https://in.tradingview.com/chart/?symbol=NSE:GAEL)<br><sub>✓ SAFE . ↘21Cr · 34Cr . ↑CMF17d</sub> | 177.76 | -1.6% | +74.7% | 12d | SMA-OK | RS-OK | +2.90% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . ↗473Cr · 89Cr . ↑CMF8d</sub> | 8255.00 | -4.6% | +81.3% | 13d | SMA-OK | RS-OK | +1.28% |
| [NESTLEIND](https://in.tradingview.com/chart/?symbol=NSE:NESTLEIND)<br><sub>✓ SAFE . ↘297Cr · 218Cr . ↑CMF11d</sub> | 1500.20 | -2.6% | +37.7% | 15d | SMA-OK | RS-OK | -0.44% |
| [AVALON](https://in.tradingview.com/chart/?symbol=NSE:AVALON)<br><sub>✓ SAFE . ↗150Cr · 250Cr . ↑CMF9d</sub> | 2197.30 | 0.0% | +176.8% | 15d | SMA-OK | RS-OK | +6.70% |
| [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON)<br><sub>✓ SAFE . ↗514Cr · 174Cr . ↑CMF11d</sub> | 168.60 | -0.5% | +86.8% | 15d | SMA-OK | RS-OK | +0.72% |
| [FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM)<br><sub>✓ SAFE . ↗164Cr · 58Cr . ↓CMF1d</sub> | 4674.80 | -1.3% | +57.4% | 15d | SMA-OK | RS-OK | -0.69% |
| [QUESS](https://in.tradingview.com/chart/?symbol=NSE:QUESS)<br><sub>✓ SAFE . ↘17Cr · 32Cr . ↑CMF30d</sub> | 336.90 | -2.4% | +98.5% | 16d | SMA-OK | RS-OK | -2.04% |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH)<br><sub>✓ SAFE . ↗47Cr · 29Cr . ↑CMF2d</sub> | 1517.40 | -0.3% | +114.8% | 16d | SMA-OK | RS-OK | +0.40% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>✓ SAFE . →171Cr · 94Cr . ↑CMF10d</sub> | 1645.00 | -1.3% | +60.9% | 17d | SMA-OK | RS-OK | +1.09% |
| [RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE)<br><sub>✓ SAFE . ↘104Cr · 65Cr . ↑CMF23d</sub> | 754.35 | -0.1% | +63.0% | 17d | SMA-OK | RS-OK | -0.09% |
| [CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN)<br><sub>✓ SAFE . ↘41Cr · 63Cr . ↑CMF21d</sub> | 10890.50 | 0.0% | +69.5% | 17d | SMA-OK | RS-OK | +3.92% |
| [TIIL](https://in.tradingview.com/chart/?symbol=NSE:TIIL)<br><sub>✓ SAFE . ↗45Cr · 62Cr . ↓CMF2d</sub> | 3280.20 | 0.0% | +72.0% | 17d | SMA-OK | RS-OK | +5.91% |
| [OFSS](https://in.tradingview.com/chart/?symbol=NSE:OFSS)<br><sub>✓ SAFE . ↘264Cr · 306Cr . ↑CMF13d</sub> | 11828.00 | -0.6% | +87.7% | 18d | SMA-OK | RS-OK | +2.05% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . ↘237Cr · 294Cr . ↑CMF16d</sub> | 252.19 | 0.0% | +92.1% | 19d | SMA-OK | RS-OK | +2.99% |
| [UJJIVANSFB](https://in.tradingview.com/chart/?symbol=NSE:UJJIVANSFB)<br><sub>✓ SAFE . ↘84Cr · 82Cr . ↑CMF5d</sub> | 72.33 | -0.2% | +73.6% | 19d | SMA-OK | RS-OK | +0.17% |
| [EICHERMOT](https://in.tradingview.com/chart/?symbol=NSE:EICHERMOT)<br><sub>✓ SAFE . →369Cr · 232Cr . ↑CMF14d</sub> | 8101.00 | -1.1% | +43.2% | 20d | SMA-OK | RS-OK | +0.01% |
| [ABB](https://in.tradingview.com/chart/?symbol=NSE:ABB)<br><sub>✓ SAFE . →260Cr · 124Cr . ↓CMF1d</sub> | 7650.00 | -1.1% | +63.1% | 20d | SMA-OK | RS-OK | -0.78% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>✓ SAFE . ↗188Cr · 424Cr . ↑CMF0d</sub> | 1367.70 | -2.9% | +132.6% | 22d | SMA-OK | RS-OK | +6.25% |
| [HSCL](https://in.tradingview.com/chart/?symbol=NSE:HSCL)<br><sub>✓ SAFE . ↘272Cr · 258Cr . ↓CMF1d . DEL53%(T-1)</sub> | 781.80 | -2.4% | +85.3% | 22d | SMA-OK | RS-OK | -0.71% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . ↘216Cr · 213Cr . ↑CMF17d</sub> | 123.70 | 0.0% | +123.9% | 22d | SMA-OK | RS-OK | +2.84% |
| [AARTIIND](https://in.tradingview.com/chart/?symbol=NSE:AARTIIND)<br><sub>✓ SAFE . →100Cr · 44Cr . ↓CMF12d</sub> | 530.10 | -1.5% | +55.9% | 22d | SMA-OK | RS-OK | +0.65% |
| [MANORAMA](https://in.tradingview.com/chart/?symbol=NSE:MANORAMA)<br><sub>✓ SAFE . ↗327Cr · 289Cr . ↓CMF30d</sub> | 1901.00 | -2.2% | +76.7% | 27d | SMA-OK | RS-OK | -2.18% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>✓ SAFE . ↗161Cr · 101Cr . ↑CMF10d</sub> | 93.66 | -3.3% | +148.2% | 27d | SMA-OK | RS-OK | +2.69% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>✓ SAFE . ↘96Cr · 71Cr . ↑CMF18d</sub> | 310.75 | -0.9% | +88.1% | 27d | SMA-OK | RS-OK | +1.39% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>⚠ CAUTION . ↘44Cr · 35Cr . ↓CMF0d</sub> | 333.90 | -4.1% | +64.5% | 27d | SMA-OK | RS-OK | -0.03% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↗394Cr · 140Cr . ↑CMF8d</sub> | 2858.60 | -3.8% | +79.0% | 28d | SMA-OK | RS-OK | -1.77% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN)<br><sub>✓ SAFE . →48Cr · 73Cr . ↑CMF11d</sub> | 653.25 | -0.8% | +64.2% | 29d | SMA-OK | RS-OK | -0.38% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . ↘72Cr · 46Cr . ↑CMF12d</sub> | 355.55 | -0.1% | +63.4% | 29d | SMA-OK | RS-OK | +1.56% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↗475Cr · 503Cr . ↑CMF23d</sub> | 1404.00 | -1.5% | +123.9% | 30d | SMA-OK | RS-OK | +1.56% |
| [TITAN](https://in.tradingview.com/chart/?symbol=NSE:TITAN)<br><sub>⚠ CAUTION . ↗618Cr · 285Cr . ↑CMF18d</sub> | 5068.40 | -1.2% | +52.3% | 30d | SMA-OK | RS-OK | +0.09% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>✓ SAFE . ↗260Cr · 221Cr . ↑CMF3d</sub> | 2858.90 | -1.4% | +109.2% | 32d | SMA-OK | RS-OK | -1.41% |
| [MMFL](https://in.tradingview.com/chart/?symbol=NSE:MMFL)<br><sub>✓ SAFE . ↗25Cr · 64Cr . ↑CMF21d</sub> | 680.20 | 0.0% | +128.2% | 32d | SMA-OK | RS-OK | +7.58% |
| [INDUSINDBK](https://in.tradingview.com/chart/?symbol=NSE:INDUSINDBK)<br><sub>⚠ CAUTION . ↘107Cr · 55Cr . ↑CMF30d</sub> | 1015.00 | -5.1% | +42.4% | 32d | SMA-OK | RS-OK | +0.44% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . →605Cr · 405Cr . ↑CMF30d</sub> | 1465.80 | -6.6% | +255.5% | 37d | SMA-OK | RS-OK | -1.31% |
| [YASHO](https://in.tradingview.com/chart/?symbol=NSE:YASHO)<br><sub>✓ SAFE . ↘36Cr · 118Cr . ↑CMF12d</sub> | 4915.80 | 0.0% | +321.7% | 37d | SMA-OK | RS-OK | +12.69% |
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM)<br><sub>⚠ CAUTION . ↘34Cr · 54Cr . ↓CMF0d</sub> | 3706.40 | -0.3% | +55.2% | 37d | SMA-OK | RS-OK | -0.32% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>✓ SAFE . ↘34Cr · 50Cr . ↓CMF4d</sub> | 1633.60 | -0.0% | +123.5% | 37d | SMA-OK | RS-OK | +1.74% |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>✓ SAFE . ↗463Cr · 49Cr . ↓CMF0d</sub> | 809.80 | -1.5% | +203.3% | 37d | SMA-OK | RS-OK | +0.06% |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS)<br><sub>✓ SAFE . ↗363Cr · 101Cr . ↑CMF9d</sub> | 322.85 | -4.3% | +173.7% | 37d | SMA-OK | RS-OK | -0.35% |
| [GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA)<br><sub>✓ SAFE . ↗36Cr · 40Cr . ↓CMF6d</sub> | 581.50 | -1.8% | +95.1% | 42d | SMA-OK | RS-OK | +3.55% |
| [HAPPYFORGE](https://in.tradingview.com/chart/?symbol=NSE:HAPPYFORGE)<br><sub>✓ SAFE . ↗41Cr · 40Cr . ↑CMF30d</sub> | 2260.60 | 0.0% | +157.5% | 42d | SMA-OK | RS-OK | +2.84% |
| [MACPOWER](https://in.tradingview.com/chart/?symbol=NSE:MACPOWER)<br><sub>✓ SAFE . →14Cr · 38Cr . ↑CMF14d</sub> | 1983.60 | 0.0% | +154.9% | 42d | SMA-OK | RS-OK | +11.35% |
| [PANAMAPET](https://in.tradingview.com/chart/?symbol=NSE:PANAMAPET)<br><sub>✓ SAFE . ↗111Cr · 43Cr . ↓CMF4d</sub> | 502.65 | -7.9% | +116.6% | 46d | SMA-OK | RS-OK | +3.19% |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON)<br><sub>✓ SAFE . ↗31Cr · 59Cr . ↑CMF30d</sub> | 4509.10 | -0.3% | +84.4% | 47d | SMA-OK | RS-OK | +1.63% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>✓ SAFE . →35Cr · 44Cr . ↑CMF0d</sub> | 2706.20 | -1.8% | +224.3% | 47d | SMA-OK | RS-OK | -1.82% |
| [GANDHAR](https://in.tradingview.com/chart/?symbol=NSE:GANDHAR)<br><sub>✓ SAFE . ↘49Cr · 57Cr . ↓CMF16d</sub> | 255.10 | -9.7% | +118.4% | 48d | SMA-OK | RS-OK | +3.41% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>⚠ CAUTION . ↘130Cr · 101Cr . ↑CMF30d</sub> | 357.80 | -3.7% | +88.4% | 52d | SMA-OK | RS-OK | +1.04% |
| [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB)<br><sub>✓ SAFE . ↗103Cr · 176Cr . ↑CMF5d</sub> | 346.87 | 0.0% | +293.5% | 57d | SMA-OK | RS-OK | +10.81% |
| [DIVGIITTS](https://in.tradingview.com/chart/?symbol=NSE:DIVGIITTS)<br><sub>✓ SAFE . ↗62Cr · 39Cr . ↑CMF6d</sub> | 1259.00 | -3.2% | +116.4% | 57d | SMA-OK | RS-OK | -1.98% |
| [MTARTECH](https://in.tradingview.com/chart/?symbol=NSE:MTARTECH)<br><sub>✓ SAFE . ↗2251Cr · 944Cr . ↑CMF8d</sub> | 7777.00 | -7.1% | +457.1% | 58d | SMA-OK | RS-OK | -4.25% |
| [PARAS](https://in.tradingview.com/chart/?symbol=NSE:PARAS)<br><sub>✓ SAFE . ↗247Cr · 826Cr . ↑CMF9d</sub> | 1527.30 | 0.0% | +161.3% | 61d | SMA-OK | RS-OK | +10.00% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↗155Cr · 69Cr . ↑CMF4d</sub> | 4003.20 | 0.0% | +219.6% | 62d | SMA-OK | RS-OK | +0.03% |
| [RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO)<br><sub>✓ SAFE . ↘168Cr · 195Cr . ↑CMF9d</sub> | 4732.90 | 0.0% | +86.2% | 64d | SMA-OK | RS-OK | +0.84% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↘194Cr · 236Cr . ↑CMF30d</sub> | 824.00 | 0.0% | +103.3% | 67d | SMA-OK | RS-OK | +2.35% |
| [BLISSGVS](https://in.tradingview.com/chart/?symbol=NSE:BLISSGVS)<br><sub>✓ SAFE . →52Cr · 21Cr . ↑CMF30d</sub> | 527.10 | -2.7% | +312.1% | 68d | SMA-OK | RS-OK | +0.68% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . ↘315Cr · 234Cr . ↑CMF30d</sub> | 1814.00 | -2.0% | +120.7% | 69d | SMA-OK | RS-OK | +0.24% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>✓ SAFE . →140Cr · 137Cr . ↑CMF30d</sub> | 1917.10 | 0.0% | +165.6% | 69d | SMA-OK | RS-OK | +1.87% |
| [STYLAMIND](https://in.tradingview.com/chart/?symbol=NSE:STYLAMIND)<br><sub>✓ SAFE . ↘18Cr · 36Cr . ↓CMF19d</sub> | 3736.40 | 0.0% | +133.7% | 72d | SMA-OK | RS-OK | +4.30% |
| [RRKABEL](https://in.tradingview.com/chart/?symbol=NSE:RRKABEL)<br><sub>✓ SAFE . ↘114Cr · 194Cr . ↓CMF6d</sub> | 2784.90 | -1.7% | +138.5% | 77d | SMA-OK | RS-OK | +1.32% |
| [SJS](https://in.tradingview.com/chart/?symbol=NSE:SJS)<br><sub>✓ SAFE . ↗64Cr · 56Cr . ↑CMF0d</sub> | 2500.20 | -1.4% | +112.5% | 77d | SMA-OK | RS-OK | -1.35% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . ↗111Cr · 65Cr . ↑CMF28d</sub> | 1440.10 | -1.6% | +81.1% | 81d | SMA-OK | RS-OK | +1.67% |
| [HONASA](https://in.tradingview.com/chart/?symbol=NSE:HONASA)<br><sub>✓ SAFE . ↗162Cr · 91Cr . ↑CMF2d</sub> | 474.60 | -5.6% | +85.2% | 85d | SMA-OK | RS-OK | -1.46% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . ↗156Cr · 56Cr . ↓CMF10d</sub> | 795.05 | -4.6% | +202.0% | 86d | SMA-OK | RS-OK | +2.40% |
| [RISHABH](https://in.tradingview.com/chart/?symbol=NSE:RISHABH)<br><sub>✓ SAFE . ↗25Cr · 47Cr . ↑CMF1d</sub> | 665.75 | -4.2% | +123.3% | 93d | SMA-OK | RS-OK | -4.15% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↗1260Cr · 1957Cr . ↑CMF30d</sub> | 284.03 | -3.7% | +751.7% | 99d | SMA-OK | RS-OK | +6.25% |

### By Trend Age

**<2 WEEKS** (60)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ACUTAAS,NSE:AEROFLEX,NSE:ANTELOPUS,NSE:ANTHEM,NSE:ASIANENE,NSE:ASTRAMICRO,NSE:BHEL,NSE:BOSCHLTD,NSE:CARBORUNIV,NSE:CYIENTDLM,NSE:DATAPATTNS,NSE:DYNAMATECH,NSE:ELGIEQUIP,NSE:ENGINERSIN,NSE:FINCABLES,NSE:GABRIEL,NSE:GRANULES,NSE:HEG,NSE:HFCL,NSE:HINDALCO,NSE:ICIL,NSE:IDEAFORGE,NSE:IFCI,NSE:IPCALAB,NSE:JGCHEM,NSE:JINDRILL,NSE:JSWENERGY,NSE:JSWINFRA,NSE:KEI,NSE:KRN,NSE:LALPATHLAB,NSE:LLOYDSENT,NSE:MANINDS,NSE:MARINE,NSE:MCX,NSE:MIDHANI,NSE:MINDACORP,NSE:MOREPENLAB,NSE:MSTCLTD,NSE:MUNJALAU,NSE:NEOGEN,NSE:NITINSPIN,NSE:PIDILITIND,NSE:PNBHOUSING,NSE:POWERINDIA,NSE:RATEGAIN,NSE:RAYMOND,NSE:RBA,NSE:ROLEXRINGS,NSE:ROSSTECH,NSE:SENORES,NSE:SHANTIGOLD,NSE:SHRIRAMFIN,NSE:TDPOWERSYS,NSE:TVSMOTOR,NSE:VISHNU,NSE:WABAG,NSE:WELSPUNLIV,NSE:ZENTEC,NSE:ZYDUSLIFE
```

**2-4 WEEKS** (27)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABB,NSE:APARINDS,NSE:AUBANK,NSE:AUROPHARMA,NSE:AVALON,NSE:CRAFTSMAN,NSE:DIVISLAB,NSE:EICHERMOT,NSE:FLUOROCHEM,NSE:GAEL,NSE:MARKSANS,NSE:MOTHERSON,NSE:NAVINFLUOR,NSE:NESTLEIND,NSE:NETWEB,NSE:OFSS,NSE:QUESS,NSE:RATNAVEER,NSE:RBLBANK,NSE:RKFORGE,NSE:SIEMENS,NSE:SMLMAH,NSE:SOLARINDS,NSE:SYRMA,NSE:TIIL,NSE:UJJIVANSFB,NSE:UNIMECH
```

**1-2 MONTHS** (26)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AARTIIND,NSE:AEGISLOG,NSE:AETHER,NSE:AJANTPHARM,NSE:ATHERENERG,NSE:AZAD,NSE:BALRAMCHIN,NSE:CHENNPETRO,NSE:DIACABS,NSE:GLAND,NSE:GNA,NSE:HAPPYFORGE,NSE:HSCL,NSE:INDUSINDBK,NSE:KARURVYSYA,NSE:KTKBANK,NSE:LLOYDSENGG,NSE:MACPOWER,NSE:MANORAMA,NSE:MMFL,NSE:NAZARA,NSE:SHILPAMED,NSE:STLTECH,NSE:TFCILTD,NSE:TITAN,NSE:YASHO
```

**2-3 MONTHS** (10)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:DIVGIITTS,NSE:FEDERALBNK,NSE:GANDHAR,NSE:INDSWFTLAB,NSE:KMEW,NSE:MTARTECH,NSE:PANAMAPET,NSE:PARAS,NSE:SANSERA,NSE:SHRIPISTON
```

**3-6 MONTHS** (13)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:BLISSGVS,NSE:CUPID,NSE:HONASA,NSE:LAURUSLABS,NSE:RADICO,NSE:RISHABH,NSE:RRKABEL,NSE:SAILIFE,NSE:SJS,NSE:SKYGOLD,NSE:SONACOMS,NSE:STYLAMIND,NSE:WELCORP
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
