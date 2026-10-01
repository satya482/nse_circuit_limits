> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-10-01
*Generated 2026-10-01 15:47 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL) | [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS) |
| [AEGISVOPAK](https://in.tradingview.com/chart/?symbol=NSE:AEGISVOPAK) | [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM) |
| [BELRISE](https://in.tradingview.com/chart/?symbol=NSE:BELRISE) | [ARTEMISMED](https://in.tradingview.com/chart/?symbol=NSE:ARTEMISMED) |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM) | [BALRAMCHIN](https://in.tradingview.com/chart/?symbol=NSE:BALRAMCHIN) |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO) | [CAPLIPOINT](https://in.tradingview.com/chart/?symbol=NSE:CAPLIPOINT) |
| [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX) | [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO) |
| [GALAXYSURF](https://in.tradingview.com/chart/?symbol=NSE:GALAXYSURF) | [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH) |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH) | [ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL) |
| [MANORAMA](https://in.tradingview.com/chart/?symbol=NSE:MANORAMA) | [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB) |
| [NRBBEARING](https://in.tradingview.com/chart/?symbol=NSE:NRBBEARING) | [INNOVACAP](https://in.tradingview.com/chart/?symbol=NSE:INNOVACAP) |
| [PIXTRANS](https://in.tradingview.com/chart/?symbol=NSE:PIXTRANS) | [ITDC](https://in.tradingview.com/chart/?symbol=NSE:ITDC) |
| [PRECWIRE](https://in.tradingview.com/chart/?symbol=NSE:PRECWIRE) | [JASH](https://in.tradingview.com/chart/?symbol=NSE:JASH) |
| [RAMRAT](https://in.tradingview.com/chart/?symbol=NSE:RAMRAT) | [JAYNECOIND](https://in.tradingview.com/chart/?symbol=NSE:JAYNECOIND) |
| [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS) | [KENNAMET](https://in.tradingview.com/chart/?symbol=NSE:KENNAMET) |
| [SCHNEIDER](https://in.tradingview.com/chart/?symbol=NSE:SCHNEIDER) | [LLOYDSENT](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENT) |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG) | [MAHSEAMLES](https://in.tradingview.com/chart/?symbol=NSE:MAHSEAMLES) |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL) | [MUNJALAU](https://in.tradingview.com/chart/?symbol=NSE:MUNJALAU) |
| [VENUSPIPES](https://in.tradingview.com/chart/?symbol=NSE:VENUSPIPES) | [NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN) |
| [WHEELS](https://in.tradingview.com/chart/?symbol=NSE:WHEELS) | [PCBL](https://in.tradingview.com/chart/?symbol=NSE:PCBL) |
|  | [PFOCUS](https://in.tradingview.com/chart/?symbol=NSE:PFOCUS) |
|  | [POWERMECH](https://in.tradingview.com/chart/?symbol=NSE:POWERMECH) |
|  | [PREMEXPLN](https://in.tradingview.com/chart/?symbol=NSE:PREMEXPLN) |
|  | [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL) |
|  | [QUADFUTURE](https://in.tradingview.com/chart/?symbol=NSE:QUADFUTURE) |
|  | [RAIN](https://in.tradingview.com/chart/?symbol=NSE:RAIN) |
|  | [SAIL](https://in.tradingview.com/chart/?symbol=NSE:SAIL) |
|  | [SOTL](https://in.tradingview.com/chart/?symbol=NSE:SOTL) |
|  | [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA) |
|  | [TI](https://in.tradingview.com/chart/?symbol=NSE:TI) |
|  | [WABAG](https://in.tradingview.com/chart/?symbol=NSE:WABAG) |

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

**Qualifying: 117**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABDL,NSE:ADANIPORTS,NSE:AEGISLOG,NSE:AEGISVOPAK,NSE:APOLLO,NSE:APOLLOHOSP,NSE:BELRISE,NSE:BHEL,NSE:CARBORUNIV,NSE:CGCL,NSE:CGPOWER,NSE:CPPLUS,NSE:CUPID,NSE:EDELWEISS,NSE:GALAXYSURF,NSE:GREAVESCOT,NSE:INOXINDIA,NSE:JSWINFRA,NSE:KAJARIACER,NSE:KIRLOSENG,NSE:LLOYDSENGG,NSE:MANKIND,NSE:MIDHANI,NSE:ONEPOINT,NSE:OPTIEMUS,NSE:PAYTM,NSE:PHOENIXLTD,NSE:PIXTRANS,NSE:PRIVISCL,NSE:PVRINOX,NSE:RAYMONDREL,NSE:REDINGTON,NSE:RPTECH,NSE:SCHNEIDER,NSE:SHRIPISTON,NSE:TORNTPHARM,NSE:ZYDUSLIFE,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ANTELOPUS,NSE:AZAD,NSE:BEML,NSE:CENTUM,NSE:GNFC,NSE:GRAPHITE,NSE:HFCL,NSE:MOTILALOFS,NSE:PAISALO,NSE:RBLBANK,NSE:SONACOMS,NSE:STAR,NSE:STYLEBAAZA,NSE:SUDARSCHEM,NSE:VENUSPIPES,NSE:WOCKPHARMA,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ACE,NSE:ACMESOLAR,NSE:AEROFLEX,NSE:BOSCHLTD,NSE:CYIENTDLM,NSE:DIVISLAB,NSE:DYNAMATECH,NSE:EBGNG,NSE:EMIL,NSE:ENGINERSIN,NSE:ENTERO,NSE:FCL,NSE:FILATEX,NSE:FINCABLES,NSE:IPCALAB,NSE:JGCHEM,NSE:LALPATHLAB,NSE:LUMAXTECH,NSE:MANINDS,NSE:MARINE,NSE:MCX,NSE:MOREPENLAB,NSE:PRECWIRE,NSE:QPOWER,NSE:RAYMOND,NSE:ROLEXRINGS,NSE:ROSSTECH,NSE:SAMBHV,NSE:SBC,NSE:SHANTIGOLD,NSE:SHREEJISPG,NSE:SHYAMMETL,NSE:SIGMAADV,NSE:STLTECH,NSE:WELSPUNLIV,NSE:WHEELS,NSE:YATHARTH,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:APARINDS,NSE:AUROPHARMA,NSE:AVALON,NSE:GLAND,NSE:IOLCP,NSE:KTKBANK,NSE:MANORAMA,NSE:MARKSANS,NSE:MOTHERSON,NSE:MTARTECH,NSE:NAZARA,NSE:NRBBEARING,NSE:RAMRAT,NSE:RATNAVEER,NSE:SMLMAH,NSE:SSWL,NSE:SYRMA,NSE:TFCILTD,NSE:UNIMECH,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AETHER,NSE:KMEW,NSE:LAURUSLABS,NSE:SAILIFE,NSE:SANSERA,NSE:SHILPAMED,NSE:SKYGOLD,NSE:WELCORP
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [SCHNEIDER](https://in.tradingview.com/chart/?symbol=NSE:SCHNEIDER)<br><sub>✓ SAFE . ↗42Cr · 184Cr . ↑CMF10d</sub> | 1275.40 | -15.0% | +120.2% | 0d | SMA-OK | RS-OK | +5.98% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>⚠ CAUTION . ↗186Cr · 190Cr . ↑CMF22d</sub> | 4971.00 | -3.0% | +41.4% | 0d | SMA-OK | RS-OK | +0.86% |
| [MIDHANI](https://in.tradingview.com/chart/?symbol=NSE:MIDHANI)<br><sub>✓ SAFE . ↘41Cr · 36Cr . ↑CMF30d</sub> | 433.60 | -9.1% | +60.3% | 0d | SMA-OK | RS-OK | -0.93% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>✓ SAFE . →273Cr · 285Cr . ↑CMF29d</sub> | 422.85 | -4.5% | +83.1% | 1d | SMA-OK | RS-OK | +1.81% |
| [PIXTRANS](https://in.tradingview.com/chart/?symbol=NSE:PIXTRANS)<br><sub>✓ SAFE . ↗28Cr · 263Cr . ↓CMF18d</sub> | 1809.30 | -8.9% | +42.6% | 1d | SMA-OK | RS-OK | +4.77% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>✓ SAFE . ↗181Cr · 497Cr . ↑CMF12d</sub> | 2550.20 | -2.6% | +32.3% | 1d | SMA-OK | RS-OK | +4.71% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>✓ SAFE . →136Cr · 149Cr . ↑CMF18d</sub> | 1401.10 | -5.7% | +138.3% | 2d | SMA-OK | RS-OK | +1.52% |
| [KAJARIACER](https://in.tradingview.com/chart/?symbol=NSE:KAJARIACER)<br><sub>✓ SAFE . ↗94Cr · 78Cr . ↓CMF2d</sub> | 1225.10 | -2.9% | +38.6% | 2d | SMA-OK | RS-OK | -0.81% |
| [CGCL](https://in.tradingview.com/chart/?symbol=NSE:CGCL)<br><sub>✓ SAFE . ↘62Cr · 70Cr . ↓CMF1d</sub> | 249.23 | -11.0% | +64.0% | 2d | SMA-OK | RS-OK | +0.72% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . ↘69Cr · 39Cr . ↑CMF11d</sub> | 1215.30 | -9.9% | +32.3% | 2d | SMA-OK | RS-OK | -2.20% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↗1124Cr · 791Cr . ↑CMF6d</sub> | 312.50 | 0.0% | +627.6% | 3d | SMA-OK | RS-OK | +0.27% |
| [KIRLOSENG](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSENG)<br><sub>✓ SAFE . ↗227Cr · 161Cr . ↑CMF30d</sub> | 2242.70 | -12.5% | +157.9% | 3d | SMA-OK | RS-OK | -2.67% |
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO)<br><sub>✓ SAFE . →296Cr · 161Cr . ↓CMF1d</sub> | 394.00 | -12.5% | +116.3% | 4d | SMA-OK | RS-OK | -2.34% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>✓ SAFE . ↗201Cr · 151Cr . ↑CMF4d</sub> | 98.31 | -3.8% | +160.6% | 4d | SMA-OK | RS-OK | -0.33% |
| [PHOENIXLTD](https://in.tradingview.com/chart/?symbol=NSE:PHOENIXLTD)<br><sub>⚠ CAUTION . ↗84Cr · 107Cr . ↓CMF2d</sub> | 1930.00 | -10.4% | +30.6% | 4d | SMA-OK | RS-OK | -0.26% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>✓ SAFE . ↗125Cr · 72Cr . ↑CMF30d</sub> | 679.45 | -6.1% | +76.9% | 4d | SMA-OK | RS-OK | -5.49% |
| [RAYMONDREL](https://in.tradingview.com/chart/?symbol=NSE:RAYMONDREL)<br><sub>✓ SAFE . ↗295Cr · 55Cr . ↑CMF6d</sub> | 648.45 | -10.3% | +81.5% | 4d | SMA-OK | RS-OK | -3.21% |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL)<br><sub>✓ SAFE . ↗49Cr · 48Cr . ↑CMF14d</sub> | 3573.00 | -4.7% | +51.4% | 4d | SMA-OK | RS-OK | -0.38% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . ↗115Cr · 45Cr . ↓CMF3d</sub> | 3799.60 | -2.6% | +197.8% | 4d | SMA-OK | RS-OK | -1.22% |
| [GREAVESCOT](https://in.tradingview.com/chart/?symbol=NSE:GREAVESCOT)<br><sub>✓ SAFE . ↗96Cr · 40Cr . ↑CMF10d</sub> | 225.98 | -14.3% | +87.4% | 4d | SMA-OK | RS-OK | -1.87% |
| [RPTECH](https://in.tradingview.com/chart/?symbol=NSE:RPTECH)<br><sub>✓ SAFE . ↗45Cr · 36Cr . ↑CMF7d</sub> | 953.15 | -0.0% | +202.4% | 4d | SMA-OK | RS-OK | -0.04% |
| [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM)<br><sub>✓ SAFE . ↗833Cr · 648Cr . ↑CMF30d</sub> | 1687.90 | -8.8% | +76.0% | 5d | SMA-OK | RS-OK | +3.18% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>✓ SAFE . →159Cr · 238Cr . ↓CMF0d</sub> | 1202.90 | -0.2% | +39.8% | 5d | SMA-OK | RS-OK | +1.91% |
| [APOLLOHOSP](https://in.tradingview.com/chart/?symbol=NSE:APOLLOHOSP)<br><sub>⚠ CAUTION . →268Cr · 386Cr . ↓CMF1d</sub> | 8890.00 | -2.0% | +30.9% | 6d | SMA-OK | RS-OK | +0.02% |
| [CGPOWER](https://in.tradingview.com/chart/?symbol=NSE:CGPOWER)<br><sub>✓ SAFE . ↘194Cr · 84Cr . ↓CMF0d</sub> | 886.10 | -9.3% | +67.0% | 6d | SMA-OK | RS-OK | -0.07% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>✓ SAFE . ↘288Cr · 157Cr . ↑CMF12d</sub> | 1788.90 | -5.0% | +37.2% | 7d | SMA-OK | RS-OK | +0.20% |
| [GALAXYSURF](https://in.tradingview.com/chart/?symbol=NSE:GALAXYSURF)<br><sub>✓ SAFE . ↗13Cr · 51Cr . ↓CMF1d</sub> | 2376.90 | -5.2% | +56.9% | 8d | SMA-OK | RS-OK | +1.89% |
| [AEGISVOPAK](https://in.tradingview.com/chart/?symbol=NSE:AEGISVOPAK)<br><sub>✓ SAFE . →52Cr · 51Cr . ↑CMF21d</sub> | 290.75 | -8.7% | +79.9% | 8d | SMA-OK | RS-OK | -2.04% |
| [REDINGTON](https://in.tradingview.com/chart/?symbol=NSE:REDINGTON)<br><sub>✓ SAFE . ↘179Cr · 111Cr . ↑CMF7d</sub> | 397.95 | -3.0% | +99.0% | 9d | SMA-OK | RS-OK | -2.22% |
| [BELRISE](https://in.tradingview.com/chart/?symbol=NSE:BELRISE)<br><sub>✓ SAFE . ↗90Cr · 89Cr . ↓CMF1d</sub> | 237.50 | -9.1% | +63.7% | 9d | SMA-OK | RS-OK | -1.19% |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS)<br><sub>✓ SAFE . ↗211Cr · 53Cr . ↑CMF21d</sub> | 803.70 | -3.0% | +174.5% | 9d | SMA-OK | RS-OK | +4.68% |
| [CARBORUNIV](https://in.tradingview.com/chart/?symbol=NSE:CARBORUNIV)<br><sub>✓ SAFE . ↗138Cr · 48Cr . ↓CMF28d</sub> | 1239.70 | -4.4% | +65.7% | 9d | SMA-OK | RS-OK | -1.02% |
| [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT)<br><sub>✓ SAFE . ↗49Cr · 46Cr . ↑CMF2d</sub> | 74.37 | 0.0% | +79.7% | 9d | SMA-OK | RS-OK | +1.34% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>✓ SAFE . ↘62Cr · 137Cr . ↓CMF5d</sub> | 2168.30 | -5.6% | +102.0% | 10d | SMA-OK | RS-OK | +5.64% |
| [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA)<br><sub>✓ SAFE . ↗249Cr · 123Cr . ↑CMF10d</sub> | 357.45 | -2.8% | +52.6% | 10d | SMA-OK | RS-OK | +0.24% |
| [EDELWEISS](https://in.tradingview.com/chart/?symbol=NSE:EDELWEISS)<br><sub>✓ SAFE . ↘122Cr · 85Cr . ↑CMF17d</sub> | 137.90 | -3.4% | +38.4% | 10d | SMA-OK | RS-OK | -3.38% |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON)<br><sub>✓ SAFE . ↗53Cr · 84Cr . ↑CMF30d</sub> | 4490.50 | -5.4% | +73.0% | 10d | SMA-OK | RS-OK | -3.51% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>✓ SAFE . ↗425Cr · 382Cr . ↓CMF1d</sub> | 2860.90 | -3.5% | +109.4% | 11d | SMA-OK | RS-OK | -3.45% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↗249Cr · 282Cr . ↑CMF2d</sub> | 805.00 | -3.4% | +98.6% | 11d | SMA-OK | RS-OK | -3.01% |
| [GNFC](https://in.tradingview.com/chart/?symbol=NSE:GNFC)<br><sub>✓ SAFE . →68Cr · 37Cr . ↑CMF10d</sub> | 589.15 | -6.5% | +60.8% | 11d | SMA-OK | RS-OK | -2.52% |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML)<br><sub>✓ SAFE . ↘63Cr · 39Cr . ↓CMF4d</sub> | 1962.30 | -12.2% | +43.3% | 12d | SMA-OK | RS-OK | -1.51% |
| [SUDARSCHEM](https://in.tradingview.com/chart/?symbol=NSE:SUDARSCHEM)<br><sub>✓ SAFE . →24Cr · 53Cr . ↓CMF1d . DEL71%(T-1)</sub> | 1241.50 | -7.8% | +66.1% | 16d | SMA-OK | RS-OK | +3.12% |
| [MOTILALOFS](https://in.tradingview.com/chart/?symbol=NSE:MOTILALOFS)<br><sub>✓ SAFE . ↗95Cr · 159Cr . ↑CMF0d</sub> | 989.90 | -9.3% | +57.6% | 17d | SMA-OK | RS-OK | -0.41% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE)<br><sub>✓ SAFE . ↘122Cr · 125Cr . ↑CMF16d</sub> | 786.15 | -6.9% | +49.4% | 18d | SMA-OK | RS-OK | +2.79% |
| [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK)<br><sub>✓ SAFE . ↗178Cr · 222Cr . ↑CMF30d</sub> | 411.40 | -3.9% | +50.4% | 19d | SMA-OK | RS-OK | +2.00% |
| [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO)<br><sub>✓ SAFE . →146Cr · 124Cr . ↑CMF20d</sub> | 79.90 | -14.5% | +158.0% | 19d | SMA-OK | RS-OK | +4.57% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>✓ SAFE . ↘165Cr · 55Cr . ↑CMF21d . DEL36%(T-1)</sub> | 1106.50 | -12.3% | +207.8% | 19d | SMA-OK | RS-OK | -1.72% |
| [CENTUM](https://in.tradingview.com/chart/?symbol=NSE:CENTUM)<br><sub>✓ SAFE . →71Cr · 37Cr . ↑CMF18d</sub> | 4701.70 | -4.5% | +124.7% | 19d | SMA-OK | RS-OK | -2.01% |
| [STAR](https://in.tradingview.com/chart/?symbol=NSE:STAR)<br><sub>✓ SAFE . ↘28Cr · 37Cr . ↑CMF18d</sub> | 1084.80 | -12.2% | +36.7% | 19d | SMA-OK | RS-OK | -3.14% |
| [VENUSPIPES](https://in.tradingview.com/chart/?symbol=NSE:VENUSPIPES)<br><sub>✓ SAFE . ↘67Cr · 36Cr . ↑CMF18d</sub> | 2204.90 | -3.4% | +146.6% | 19d | SMA-OK | RS-OK | +2.69% |
| [WOCKPHARMA](https://in.tradingview.com/chart/?symbol=NSE:WOCKPHARMA)<br><sub>✓ SAFE . ↘254Cr · 163Cr . ↑CMF18d</sub> | 2083.90 | -10.6% | +89.4% | 21d | SMA-OK | RS-OK | -1.53% |
| [STYLEBAAZA](https://in.tradingview.com/chart/?symbol=NSE:STYLEBAAZA)<br><sub>✓ SAFE . ↗68Cr · 60Cr . ↓CMF0d</sub> | 368.35 | -16.2% | +55.3% | 21d | SMA-OK | RS-OK | -4.26% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . ↗104Cr · 184Cr . ↑CMF1d</sub> | 58.54 | 0.0% | +172.5% | 24d | SMA-OK | RS-OK | +0.43% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . ↘62Cr · 79Cr . ↑CMF19d</sub> | 775.35 | 0.0% | +247.0% | 24d | SMA-OK | RS-OK | +0.64% |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE)<br><sub>✓ SAFE . →45Cr · 56Cr . ↑CMF5d</sub> | 1212.30 | -3.3% | +61.9% | 24d | SMA-OK | RS-OK | -1.60% |
| [YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH)<br><sub>✓ SAFE . ↗114Cr · 53Cr . ↑CMF17d</sub> | 1033.70 | -11.1% | +87.7% | 24d | SMA-OK | RS-OK | +0.12% |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL)<br><sub>✓ SAFE . ↗86Cr · 50Cr . ↓CMF4d</sub> | 1047.80 | -5.2% | +37.6% | 24d | SMA-OK | RS-OK | -1.62% |
| [WHEELS](https://in.tradingview.com/chart/?symbol=NSE:WHEELS)<br><sub>✓ SAFE . ↘61Cr · 41Cr . ↑CMF25d</sub> | 2241.30 | -6.6% | +213.9% | 26d | SMA-OK | RS-OK | +0.91% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>⚠ CAUTION . ↗50Cr · 63Cr . ↓CMF13d</sub> | 1943.20 | -3.3% | +53.2% | 29d | SMA-OK | RS-OK | +0.84% |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN)<br><sub>✓ SAFE . ↗304Cr · 247Cr . ↑CMF30d</sub> | 312.75 | -0.9% | +90.1% | 30d | SMA-OK | RS-OK | +1.02% |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL)<br><sub>✓ SAFE . ↗122Cr · 82Cr . ↑CMF15d</sub> | 204.05 | -0.6% | +138.4% | 30d | SMA-OK | RS-OK | -0.64% |
| [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX)<br><sub>✓ SAFE . →79Cr · 37Cr . ↑CMF30d</sub> | 106.10 | -5.3% | +187.5% | 30d | SMA-OK | RS-OK | -1.54% |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH)<br><sub>✓ SAFE . →28Cr · 47Cr . ↓CMF0d</sub> | 1978.90 | -6.5% | +75.5% | 33d | SMA-OK | RS-OK | -4.71% |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>✓ SAFE . ↗152Cr · 47Cr . ↑CMF30d</sub> | 432.55 | -5.7% | +117.4% | 33d | SMA-OK | RS-OK | -1.47% |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . ↗659Cr · 642Cr . ↓CMF3d</sub> | 3204.00 | -6.9% | +105.5% | 34d | SMA-OK | RS-OK | -2.92% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↘453Cr · 143Cr . ↑CMF30d</sub> | 1197.20 | -1.3% | +272.0% | 34d | SMA-OK | RS-OK | -1.31% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>✓ SAFE . →191Cr · 92Cr . ↑CMF25d</sub> | 921.55 | -9.7% | +196.7% | 34d | SMA-OK | RS-OK | +1.56% |
| [FINCABLES](https://in.tradingview.com/chart/?symbol=NSE:FINCABLES)<br><sub>✓ SAFE . ↘106Cr · 87Cr . ↑CMF16d . DEL51%(T-1)</sub> | 1458.80 | -1.4% | +105.2% | 34d | SMA-OK | RS-OK | +0.59% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>✓ SAFE . →56Cr · 63Cr . ↓CMF4d</sub> | 704.70 | -1.5% | +190.5% | 34d | SMA-OK | RS-OK | +2.61% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>✓ SAFE . ↘50Cr · 62Cr . ↑CMF30d</sub> | 521.35 | -9.1% | +228.3% | 34d | SMA-OK | RS-OK | -2.84% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>✓ SAFE . ↗210Cr · 58Cr . ↑CMF9d</sub> | 161.45 | -2.1% | +96.2% | 34d | SMA-OK | RS-OK | -2.09% |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER)<br><sub>✓ SAFE . →49Cr · 50Cr . ↑CMF3d</sub> | 1564.60 | -3.1% | +162.9% | 34d | SMA-OK | RS-OK | -1.27% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>✓ SAFE . ↘32Cr · 35Cr . ↑CMF27d</sub> | 893.90 | -8.4% | +228.3% | 34d | SMA-OK | RS-OK | -2.21% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↗150Cr · 539Cr . ↑CMF14d</sub> | 239.17 | 0.0% | +120.8% | 35d | SMA-OK | RS-OK | +5.21% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>✓ SAFE . ↘100Cr · 89Cr . ↑CMF30d</sub> | 48000.00 | -4.0% | +67.0% | 35d | SMA-OK | RS-OK | +0.52% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>✓ SAFE . ↗227Cr · 68Cr . ↑CMF6d</sub> | 303.55 | -6.8% | +93.8% | 36d | SMA-OK | RS-OK | -1.64% |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE)<br><sub>↗144Cr · 65Cr . ↑CMF30d</sub> | 436.55 | -0.4% | +187.8% | 36d | SMA-OK | RS-OK | +1.63% |
| [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS)<br><sub>✓ SAFE . ↗58Cr · 103Cr . ↑CMF4d</sub> | 196.36 | 0.0% | +95.5% | 39d | SMA-OK | RS-OK | +3.30% |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH)<br><sub>✓ SAFE . ↗45Cr · 59Cr . ↑CMF14d . DEL60%(T-1)</sub> | 13756.00 | 0.0% | +101.1% | 39d | SMA-OK | RS-OK | +1.07% |
| [JGCHEM](https://in.tradingview.com/chart/?symbol=NSE:JGCHEM)<br><sub>✓ SAFE . ↗38Cr · 48Cr . ↑CMF2d</sub> | 610.30 | -7.3% | +100.0% | 39d | SMA-OK | RS-OK | -5.39% |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH)<br><sub>✓ SAFE . ↘57Cr · 38Cr . ↑CMF12d</sub> | 1522.30 | 0.0% | +165.3% | 39d | SMA-OK | RS-OK | +1.27% |
| [PRECWIRE](https://in.tradingview.com/chart/?symbol=NSE:PRECWIRE)<br><sub>✓ SAFE . ↗40Cr · 35Cr . ↑CMF30d</sub> | 501.40 | -1.2% | +173.2% | 39d | SMA-OK | RS-OK | +1.82% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . →495Cr · 369Cr . ↑CMF30d</sub> | 9575.50 | -0.5% | +68.3% | 40d | SMA-OK | RS-OK | -0.28% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>✓ SAFE . ↘33Cr · 72Cr . ↑CMF0d</sub> | 763.65 | 0.0% | +710.9% | 40d | SMA-OK | RS-OK | +5.00% |
| [FCL](https://in.tradingview.com/chart/?symbol=NSE:FCL)<br><sub>✓ SAFE . ↘132Cr · 185Cr . ↓CMF0d</sub> | 55.72 | -7.9% | +189.6% | 41d | SMA-OK | RS-OK | -3.01% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . →228Cr · 507Cr . ↑CMF30d</sub> | 133.72 | 0.0% | +297.0% | 42d | SMA-OK | RS-OK | +6.14% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>✓ SAFE . →74Cr · 109Cr . ↓CMF11d</sub> | 2005.10 | 0.0% | +53.3% | 42d | SMA-OK | RS-OK | +0.91% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>✓ SAFE . ↘32Cr · 34Cr . ↑CMF27d</sub> | 1680.80 | -11.5% | +77.1% | 42d | SMA-OK | RS-OK | -1.64% |
| [SMLMAH](https://in.tradingview.com/chart/?symbol=NSE:SMLMAH)<br><sub>✓ SAFE . ↘34Cr · 45Cr . ↑CMF19d</sub> | 6251.00 | -8.4% | +126.1% | 43d | SMA-OK | RS-OK | -4.97% |
| [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON)<br><sub>⚠ CAUTION . →199Cr · 229Cr . ↓CMF8d</sub> | 165.50 | -3.0% | +62.8% | 44d | SMA-OK | RS-OK | +1.85% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>✓ SAFE . →485Cr · 322Cr . ↑CMF20d</sub> | 1717.90 | -3.6% | +168.4% | 44d | SMA-OK | RS-OK | -3.65% |
| [APARINDS](https://in.tradingview.com/chart/?symbol=NSE:APARINDS)<br><sub>✓ SAFE . ↗261Cr · 244Cr . ↑CMF15d</sub> | 17648.00 | -6.8% | +153.3% | 44d | SMA-OK | RS-OK | +1.52% |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS)<br><sub>✓ SAFE . ↗83Cr · 80Cr . ↓CMF1d</sub> | 325.60 | -6.3% | +107.5% | 44d | SMA-OK | RS-OK | +1.02% |
| [NRBBEARING](https://in.tradingview.com/chart/?symbol=NSE:NRBBEARING)<br><sub>✓ SAFE . ↗89Cr · 37Cr . ↑CMF30d</sub> | 542.60 | 0.0% | +151.0% | 44d | SMA-OK | RS-OK | +1.60% |
| [AVALON](https://in.tradingview.com/chart/?symbol=NSE:AVALON)<br><sub>✓ SAFE . ↗217Cr · 73Cr . ↑CMF9d</sub> | 2280.20 | -10.1% | +187.2% | 47d | SMA-OK | RS-OK | -0.72% |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH)<br><sub>✓ SAFE . →67Cr · 72Cr . ↑CMF17d</sub> | 1773.00 | 0.0% | +151.0% | 48d | SMA-OK | RS-OK | +2.84% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>⚠ CAUTION . ↗158Cr · 180Cr . ↑CMF30d</sub> | 1676.80 | -3.3% | +56.6% | 49d | SMA-OK | RS-OK | +0.29% |
| [RAMRAT](https://in.tradingview.com/chart/?symbol=NSE:RAMRAT)<br><sub>✓ SAFE . ↗21Cr · 62Cr . ↑CMF1d</sub> | 616.55 | 0.0% | +121.6% | 49d | SMA-OK | RS-OK | +5.86% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . ↗279Cr · 399Cr . ↑CMF30d</sub> | 345.45 | 0.0% | +163.1% | 51d | SMA-OK | RS-OK | +4.44% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↗68Cr · 128Cr . ↓CMF0d</sub> | 390.80 | -4.2% | +129.3% | 53d | SMA-OK | RS-OK | -4.24% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . ↗229Cr · 84Cr . ↓CMF10d</sub> | 138.79 | -5.4% | +151.2% | 54d | SMA-OK | RS-OK | -2.20% |
| [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP)<br><sub>✓ SAFE . ↘62Cr · 85Cr . ↑CMF2d</sub> | 209.39 | -1.7% | +207.0% | 57d | SMA-OK | RS-OK | +1.12% |
| [MTARTECH](https://in.tradingview.com/chart/?symbol=NSE:MTARTECH)<br><sub>✓ SAFE . ↗2251Cr · 944Cr . ↑CMF8d</sub> | 7777.00 | -7.1% | +457.1% | 58d | SMA-OK | RS-OK | -4.25% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>✓ SAFE . →62Cr · 106Cr . ↓CMF0d</sub> | 321.60 | -6.3% | +88.0% | 59d | SMA-OK | RS-OK | -2.25% |
| [MANORAMA](https://in.tradingview.com/chart/?symbol=NSE:MANORAMA)<br><sub>✓ SAFE . ↘30Cr · 91Cr . ↑CMF12d</sub> | 1880.30 | -11.8% | +74.8% | 59d | SMA-OK | RS-OK | +1.48% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↘100Cr · 94Cr . ↑CMF30d</sub> | 2874.40 | -5.0% | +80.0% | 60d | SMA-OK | RS-OK | -0.86% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . ↗68Cr · 51Cr . ↑CMF30d</sub> | 384.70 | -2.1% | +76.8% | 61d | SMA-OK | RS-OK | -2.07% |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>✓ SAFE . →101Cr · 180Cr . ↑CMF20d</sub> | 1064.10 | -0.6% | +298.5% | 69d | SMA-OK | RS-OK | +1.61% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>✓ SAFE . ↗63Cr · 62Cr . ↑CMF15d</sub> | 1670.00 | -5.5% | +128.0% | 69d | SMA-OK | RS-OK | -1.72% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>✓ SAFE . ↗49Cr · 41Cr . ↑CMF3d</sub> | 2950.10 | -6.4% | +168.3% | 79d | SMA-OK | RS-OK | -3.01% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↗196Cr · 194Cr . ↑CMF30d</sub> | 4276.60 | -8.3% | +211.7% | 94d | SMA-OK | RS-OK | -5.75% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . ↘382Cr · 266Cr . ↑CMF30d</sub> | 2031.00 | 0.0% | +144.0% | 97d | SMA-OK | RS-OK | +1.22% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>✓ SAFE . ↗589Cr · 602Cr . ↑CMF30d</sub> | 2605.80 | -8.3% | +261.0% | 101d | SMA-OK | RS-OK | -4.09% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . ↘66Cr · 90Cr . ↓CMF1d</sub> | 1541.20 | -8.0% | +93.9% | 113d | SMA-OK | RS-OK | +1.10% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . →66Cr · 92Cr . ↑CMF0d</sub> | 810.65 | -4.4% | +207.9% | 118d | SMA-OK | RS-OK | -0.01% |

### By Trend Age

**<2 WEEKS** (37)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:ADANIPORTS,NSE:AEGISLOG,NSE:AEGISVOPAK,NSE:APOLLO,NSE:APOLLOHOSP,NSE:BELRISE,NSE:BHEL,NSE:CARBORUNIV,NSE:CGCL,NSE:CGPOWER,NSE:CPPLUS,NSE:CUPID,NSE:EDELWEISS,NSE:GALAXYSURF,NSE:GREAVESCOT,NSE:INOXINDIA,NSE:JSWINFRA,NSE:KAJARIACER,NSE:KIRLOSENG,NSE:LLOYDSENGG,NSE:MANKIND,NSE:MIDHANI,NSE:ONEPOINT,NSE:OPTIEMUS,NSE:PAYTM,NSE:PHOENIXLTD,NSE:PIXTRANS,NSE:PRIVISCL,NSE:PVRINOX,NSE:RAYMONDREL,NSE:REDINGTON,NSE:RPTECH,NSE:SCHNEIDER,NSE:SHRIPISTON,NSE:TORNTPHARM,NSE:ZYDUSLIFE
```

**2-4 WEEKS** (16)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ANTELOPUS,NSE:AZAD,NSE:BEML,NSE:CENTUM,NSE:GNFC,NSE:GRAPHITE,NSE:HFCL,NSE:MOTILALOFS,NSE:PAISALO,NSE:RBLBANK,NSE:SONACOMS,NSE:STAR,NSE:STYLEBAAZA,NSE:SUDARSCHEM,NSE:VENUSPIPES,NSE:WOCKPHARMA
```

**1-2 MONTHS** (37)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ACE,NSE:ACMESOLAR,NSE:AEROFLEX,NSE:BOSCHLTD,NSE:CYIENTDLM,NSE:DIVISLAB,NSE:DYNAMATECH,NSE:EBGNG,NSE:EMIL,NSE:ENGINERSIN,NSE:ENTERO,NSE:FCL,NSE:FILATEX,NSE:FINCABLES,NSE:IPCALAB,NSE:JGCHEM,NSE:LALPATHLAB,NSE:LUMAXTECH,NSE:MANINDS,NSE:MARINE,NSE:MCX,NSE:MOREPENLAB,NSE:PRECWIRE,NSE:QPOWER,NSE:RAYMOND,NSE:ROLEXRINGS,NSE:ROSSTECH,NSE:SAMBHV,NSE:SBC,NSE:SHANTIGOLD,NSE:SHREEJISPG,NSE:SHYAMMETL,NSE:SIGMAADV,NSE:STLTECH,NSE:WELSPUNLIV,NSE:WHEELS,NSE:YATHARTH
```

**2-3 MONTHS** (19)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:APARINDS,NSE:AUROPHARMA,NSE:AVALON,NSE:GLAND,NSE:IOLCP,NSE:KTKBANK,NSE:MANORAMA,NSE:MARKSANS,NSE:MOTHERSON,NSE:MTARTECH,NSE:NAZARA,NSE:NRBBEARING,NSE:RAMRAT,NSE:RATNAVEER,NSE:SMLMAH,NSE:SSWL,NSE:SYRMA,NSE:TFCILTD,NSE:UNIMECH
```

**3-6 MONTHS** (8)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AETHER,NSE:KMEW,NSE:LAURUSLABS,NSE:SAILIFE,NSE:SANSERA,NSE:SHILPAMED,NSE:SKYGOLD,NSE:WELCORP
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
