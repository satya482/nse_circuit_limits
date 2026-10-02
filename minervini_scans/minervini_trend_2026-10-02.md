> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-10-02
*Generated 2026-10-02 15:48 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| *(none)* | *(none)* |

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
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ABDL,NSE:ADANIPORTS,NSE:AEGISLOG,NSE:AEGISVOPAK,NSE:APOLLO,NSE:APOLLOHOSP,NSE:BELRISE,NSE:BHEL,NSE:CARBORUNIV,NSE:CGCL,NSE:CGPOWER,NSE:CPPLUS,NSE:CUPID,NSE:GALAXYSURF,NSE:GREAVESCOT,NSE:KAJARIACER,NSE:KIRLOSENG,NSE:LLOYDSENGG,NSE:MANKIND,NSE:MIDHANI,NSE:ONEPOINT,NSE:OPTIEMUS,NSE:PAYTM,NSE:PHOENIXLTD,NSE:PIXTRANS,NSE:PRIVISCL,NSE:PVRINOX,NSE:RAYMONDREL,NSE:REDINGTON,NSE:RPTECH,NSE:SCHNEIDER,NSE:TORNTPHARM,NSE:ZYDUSLIFE,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ANTELOPUS,NSE:AZAD,NSE:BEML,NSE:CENTUM,NSE:EDELWEISS,NSE:GNFC,NSE:GRAPHITE,NSE:HFCL,NSE:INOXINDIA,NSE:JSWINFRA,NSE:MOTILALOFS,NSE:PAISALO,NSE:RBLBANK,NSE:SHRIPISTON,NSE:SONACOMS,NSE:STAR,NSE:SUDARSCHEM,NSE:VENUSPIPES,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:ACE,NSE:ACMESOLAR,NSE:AEROFLEX,NSE:BOSCHLTD,NSE:CYIENTDLM,NSE:DIVISLAB,NSE:DYNAMATECH,NSE:EBGNG,NSE:EMIL,NSE:ENGINERSIN,NSE:FCL,NSE:FILATEX,NSE:FINCABLES,NSE:IPCALAB,NSE:JGCHEM,NSE:LUMAXTECH,NSE:MANINDS,NSE:MARINE,NSE:MCX,NSE:PRECWIRE,NSE:QPOWER,NSE:RAYMOND,NSE:ROLEXRINGS,NSE:ROSSTECH,NSE:SAMBHV,NSE:SBC,NSE:SHANTIGOLD,NSE:SHREEJISPG,NSE:SHYAMMETL,NSE:SIGMAADV,NSE:STLTECH,NSE:STYLEBAAZA,NSE:WELSPUNLIV,NSE:WHEELS,NSE:WOCKPHARMA,NSE:YATHARTH,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:APARINDS,NSE:AUROPHARMA,NSE:AVALON,NSE:ENTERO,NSE:GLAND,NSE:IOLCP,NSE:KTKBANK,NSE:LALPATHLAB,NSE:MANORAMA,NSE:MARKSANS,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:MTARTECH,NSE:NAZARA,NSE:NRBBEARING,NSE:RAMRAT,NSE:RATNAVEER,NSE:SMLMAH,NSE:SSWL,NSE:SYRMA,NSE:TFCILTD,NSE:UNIMECH,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:AETHER,NSE:KMEW,NSE:LAURUSLABS,NSE:SAILIFE,NSE:SANSERA,NSE:SHILPAMED,NSE:SKYGOLD,NSE:WELCORP
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [SCHNEIDER](https://in.tradingview.com/chart/?symbol=NSE:SCHNEIDER)<br><sub>✓ SAFE . ↗38Cr · 0.0Cr . ↑CMF11d</sub> | 1275.40 | -15.0% | +120.2% | 0d | SMA-OK | RS-OK | +0.00% |
| [TORNTPHARM](https://in.tradingview.com/chart/?symbol=NSE:TORNTPHARM)<br><sub>⚠ CAUTION . ↗186Cr · 190Cr . ↑CMF22d</sub> | 4971.00 | -3.0% | +41.4% | 0d | SMA-OK | RS-OK | +0.86% |
| [MIDHANI](https://in.tradingview.com/chart/?symbol=NSE:MIDHANI)<br><sub>✓ SAFE . ↘35Cr · 0.0Cr . ↑CMF30d</sub> | 433.60 | -9.1% | +60.3% | 0d | SMA-OK | RS-OK | +0.00% |
| [BHEL](https://in.tradingview.com/chart/?symbol=NSE:BHEL)<br><sub>✓ SAFE . →273Cr · 285Cr . ↑CMF29d</sub> | 422.85 | -4.5% | +83.1% | 1d | SMA-OK | RS-OK | +1.81% |
| [MANKIND](https://in.tradingview.com/chart/?symbol=NSE:MANKIND)<br><sub>✓ SAFE . ↗181Cr · 497Cr . ↑CMF12d</sub> | 2550.20 | -2.6% | +32.3% | 1d | SMA-OK | RS-OK | +4.71% |
| [PIXTRANS](https://in.tradingview.com/chart/?symbol=NSE:PIXTRANS)<br><sub>✓ SAFE . ↗28Cr · 0.0Cr . ↓CMF19d</sub> | 1809.30 | -8.9% | +42.6% | 2d | SMA-OK | RS-OK | +0.00% |
| [AEGISLOG](https://in.tradingview.com/chart/?symbol=NSE:AEGISLOG)<br><sub>✓ SAFE . →117Cr · 0.0Cr . ↑CMF19d</sub> | 1401.10 | -5.7% | +138.3% | 3d | SMA-OK | RS-OK | +0.00% |
| [KAJARIACER](https://in.tradingview.com/chart/?symbol=NSE:KAJARIACER)<br><sub>✓ SAFE . ↗92Cr · 0.0Cr . ↓CMF3d</sub> | 1225.10 | -2.9% | +38.6% | 3d | SMA-OK | RS-OK | +0.00% |
| [CGCL](https://in.tradingview.com/chart/?symbol=NSE:CGCL)<br><sub>✓ SAFE . ↘46Cr · 0.0Cr . ↓CMF2d</sub> | 249.23 | -11.0% | +64.0% | 3d | SMA-OK | RS-OK | +0.00% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . ↘56Cr · 0.0Cr . ↑CMF12d</sub> | 1215.30 | -9.9% | +32.3% | 3d | SMA-OK | RS-OK | +0.00% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↗1039Cr · 0.0Cr . ↑CMF7d</sub> | 312.50 | 0.0% | +627.6% | 4d | SMA-OK | RS-OK | +0.00% |
| [KIRLOSENG](https://in.tradingview.com/chart/?symbol=NSE:KIRLOSENG)<br><sub>✓ SAFE . ↗216Cr · 0.0Cr . ↑CMF30d</sub> | 2242.70 | -12.5% | +157.9% | 4d | SMA-OK | RS-OK | +0.00% |
| [PAYTM](https://in.tradingview.com/chart/?symbol=NSE:PAYTM)<br><sub>✓ SAFE . ↗833Cr · 648Cr . ↑CMF30d</sub> | 1687.90 | -8.8% | +76.0% | 5d | SMA-OK | RS-OK | +3.18% |
| [ZYDUSLIFE](https://in.tradingview.com/chart/?symbol=NSE:ZYDUSLIFE)<br><sub>✓ SAFE . →159Cr · 238Cr . ↓CMF0d</sub> | 1202.90 | -0.2% | +39.8% | 5d | SMA-OK | RS-OK | +1.91% |
| [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO)<br><sub>✓ SAFE . ↘260Cr · 0.0Cr . ↓CMF2d</sub> | 394.00 | -12.5% | +116.3% | 5d | SMA-OK | RS-OK | +0.00% |
| [LLOYDSENGG](https://in.tradingview.com/chart/?symbol=NSE:LLOYDSENGG)<br><sub>✓ SAFE . ↗199Cr · 0.0Cr . ↑CMF5d</sub> | 98.31 | -3.8% | +160.6% | 5d | SMA-OK | RS-OK | +0.00% |
| [PHOENIXLTD](https://in.tradingview.com/chart/?symbol=NSE:PHOENIXLTD)<br><sub>⚠ CAUTION . →76Cr · 0.0Cr . ↓CMF3d</sub> | 1930.00 | -10.4% | +30.6% | 5d | SMA-OK | RS-OK | +0.00% |
| [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL)<br><sub>✓ SAFE . ↗122Cr · 0.0Cr . ↑CMF30d</sub> | 679.45 | -6.1% | +76.9% | 5d | SMA-OK | RS-OK | +0.00% |
| [RAYMONDREL](https://in.tradingview.com/chart/?symbol=NSE:RAYMONDREL)<br><sub>✓ SAFE . ↗292Cr · 0.0Cr . ↑CMF7d</sub> | 648.45 | -10.3% | +81.5% | 5d | SMA-OK | RS-OK | +0.00% |
| [PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL)<br><sub>✓ SAFE . ↗48Cr · 0.0Cr . ↑CMF15d</sub> | 3573.00 | -4.7% | +51.4% | 5d | SMA-OK | RS-OK | +0.00% |
| [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS)<br><sub>✓ SAFE . ↘81Cr · 0.0Cr . ↓CMF4d</sub> | 3799.60 | -2.6% | +189.2% | 5d | SMA-OK | RS-OK | +0.00% |
| [GREAVESCOT](https://in.tradingview.com/chart/?symbol=NSE:GREAVESCOT)<br><sub>✓ SAFE . ↗93Cr · 0.0Cr . ↑CMF11d</sub> | 225.98 | -14.3% | +87.4% | 5d | SMA-OK | RS-OK | +0.00% |
| [RPTECH](https://in.tradingview.com/chart/?symbol=NSE:RPTECH)<br><sub>✓ SAFE . ↗43Cr · 0.0Cr . ↑CMF8d</sub> | 953.15 | -0.0% | +202.4% | 5d | SMA-OK | RS-OK | +0.00% |
| [APOLLOHOSP](https://in.tradingview.com/chart/?symbol=NSE:APOLLOHOSP)<br><sub>⚠ CAUTION . →268Cr · 386Cr . ↓CMF1d</sub> | 8890.00 | -2.0% | +30.9% | 6d | SMA-OK | RS-OK | +0.02% |
| [CGPOWER](https://in.tradingview.com/chart/?symbol=NSE:CGPOWER)<br><sub>✓ SAFE . ↘194Cr · 84Cr . ↓CMF0d</sub> | 886.10 | -9.3% | +67.0% | 6d | SMA-OK | RS-OK | -0.07% |
| [ADANIPORTS](https://in.tradingview.com/chart/?symbol=NSE:ADANIPORTS)<br><sub>✓ SAFE . ↘288Cr · 157Cr . ↑CMF12d</sub> | 1788.90 | -5.0% | +37.2% | 7d | SMA-OK | RS-OK | +0.20% |
| [GALAXYSURF](https://in.tradingview.com/chart/?symbol=NSE:GALAXYSURF)<br><sub>✓ SAFE . ↗13Cr · 0.0Cr . ↓CMF2d</sub> | 2376.90 | -5.2% | +56.9% | 9d | SMA-OK | RS-OK | +0.00% |
| [AEGISVOPAK](https://in.tradingview.com/chart/?symbol=NSE:AEGISVOPAK)<br><sub>✓ SAFE . ↘45Cr · 0.0Cr . ↑CMF22d</sub> | 290.75 | -8.7% | +79.9% | 9d | SMA-OK | RS-OK | +0.00% |
| [REDINGTON](https://in.tradingview.com/chart/?symbol=NSE:REDINGTON)<br><sub>✓ SAFE . ↘136Cr · 0.0Cr . ↑CMF8d</sub> | 397.95 | -3.0% | +99.0% | 10d | SMA-OK | RS-OK | +0.00% |
| [BELRISE](https://in.tradingview.com/chart/?symbol=NSE:BELRISE)<br><sub>✓ SAFE . →65Cr · 0.0Cr . ↓CMF2d</sub> | 237.50 | -9.1% | +63.7% | 10d | SMA-OK | RS-OK | +0.00% |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS)<br><sub>✓ SAFE . ↗210Cr · 0.0Cr . ↑CMF22d</sub> | 803.70 | -3.0% | +174.5% | 10d | SMA-OK | RS-OK | +0.00% |
| [CARBORUNIV](https://in.tradingview.com/chart/?symbol=NSE:CARBORUNIV)<br><sub>✓ SAFE . ↗131Cr · 0.0Cr . ↓CMF29d</sub> | 1239.70 | -4.4% | +65.7% | 10d | SMA-OK | RS-OK | +0.00% |
| [ONEPOINT](https://in.tradingview.com/chart/?symbol=NSE:ONEPOINT)<br><sub>✓ SAFE . ↗49Cr · 0.0Cr . ↑CMF3d</sub> | 74.37 | 0.0% | +79.7% | 10d | SMA-OK | RS-OK | +0.00% |
| [INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA)<br><sub>✓ SAFE . ↘57Cr · 0.0Cr . ↓CMF6d</sub> | 2168.30 | -5.6% | +102.0% | 11d | SMA-OK | RS-OK | +0.00% |
| [JSWINFRA](https://in.tradingview.com/chart/?symbol=NSE:JSWINFRA)<br><sub>✓ SAFE . →158Cr · 0.0Cr . ↑CMF11d</sub> | 357.45 | -2.8% | +52.6% | 11d | SMA-OK | RS-OK | +0.00% |
| [EDELWEISS](https://in.tradingview.com/chart/?symbol=NSE:EDELWEISS)<br><sub>✓ SAFE . ↘110Cr · 0.0Cr . ↑CMF18d</sub> | 137.90 | -3.4% | +38.4% | 11d | SMA-OK | RS-OK | +0.00% |
| [SHRIPISTON](https://in.tradingview.com/chart/?symbol=NSE:SHRIPISTON)<br><sub>✓ SAFE . ↗46Cr · 0.0Cr . ↓CMF0d</sub> | 4490.50 | -5.4% | +73.0% | 11d | SMA-OK | RS-OK | +0.00% |
| [AZAD](https://in.tradingview.com/chart/?symbol=NSE:AZAD)<br><sub>✓ SAFE . ↗405Cr · 0.0Cr . ↓CMF2d</sub> | 2860.90 | -3.5% | +109.4% | 12d | SMA-OK | RS-OK | +0.00% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↗215Cr · 0.0Cr . ↑CMF3d</sub> | 805.00 | -3.4% | +98.6% | 12d | SMA-OK | RS-OK | +0.00% |
| [GNFC](https://in.tradingview.com/chart/?symbol=NSE:GNFC)<br><sub>✓ SAFE . ↘60Cr · 0.0Cr . ↑CMF11d</sub> | 589.15 | -6.5% | +60.8% | 12d | SMA-OK | RS-OK | +0.00% |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML)<br><sub>✓ SAFE . ↘36Cr · 0.0Cr . ↓CMF5d</sub> | 1962.30 | -12.2% | +43.3% | 13d | SMA-OK | RS-OK | +0.00% |
| [SUDARSCHEM](https://in.tradingview.com/chart/?symbol=NSE:SUDARSCHEM)<br><sub>✓ SAFE . ↘20Cr · 0.0Cr . ↑CMF0d</sub> | 1241.50 | -7.8% | +66.1% | 17d | SMA-OK | RS-OK | +0.00% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [MOTILALOFS](https://in.tradingview.com/chart/?symbol=NSE:MOTILALOFS)<br><sub>✓ SAFE . ↗88Cr · 0.0Cr . ↑CMF1d</sub> | 989.90 | -9.3% | +57.6% | 18d | SMA-OK | RS-OK | +0.00% |
| [GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE)<br><sub>✓ SAFE . ↘104Cr · 0.0Cr . ↑CMF17d</sub> | 786.15 | -6.9% | +49.4% | 19d | SMA-OK | RS-OK | +0.00% |
| [RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK)<br><sub>✓ SAFE . ↗162Cr · 0.0Cr . ↑CMF30d</sub> | 411.40 | -3.9% | +50.4% | 20d | SMA-OK | RS-OK | +0.00% |
| [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO)<br><sub>✓ SAFE . ↘126Cr · 0.0Cr . ↑CMF21d</sub> | 79.90 | -14.5% | +158.0% | 20d | SMA-OK | RS-OK | +0.00% |
| [ANTELOPUS](https://in.tradingview.com/chart/?symbol=NSE:ANTELOPUS)<br><sub>✓ SAFE . ↘159Cr · 0.0Cr . ↑CMF22d . DEL21%(T-1)</sub> | 1106.50 | -12.3% | +207.8% | 20d | SMA-OK | RS-OK | +0.00% |
| [CENTUM](https://in.tradingview.com/chart/?symbol=NSE:CENTUM)<br><sub>✓ SAFE . →69Cr · 0.0Cr . ↑CMF19d</sub> | 4701.70 | -4.5% | +124.7% | 20d | SMA-OK | RS-OK | +0.00% |
| [STAR](https://in.tradingview.com/chart/?symbol=NSE:STAR)<br><sub>✓ SAFE . ↘25Cr · 0.0Cr . ↑CMF19d</sub> | 1084.80 | -12.2% | +36.7% | 20d | SMA-OK | RS-OK | +0.00% |
| [VENUSPIPES](https://in.tradingview.com/chart/?symbol=NSE:VENUSPIPES)<br><sub>✓ SAFE . ↘39Cr · 0.0Cr . ↑CMF19d</sub> | 2204.90 | -3.4% | +146.6% | 20d | SMA-OK | RS-OK | +0.00% |
| [WOCKPHARMA](https://in.tradingview.com/chart/?symbol=NSE:WOCKPHARMA)<br><sub>✓ SAFE . →243Cr · 0.0Cr . ↑CMF19d</sub> | 2083.90 | -10.6% | +89.4% | 22d | SMA-OK | RS-OK | +0.00% |
| [STYLEBAAZA](https://in.tradingview.com/chart/?symbol=NSE:STYLEBAAZA)<br><sub>✓ SAFE . ↗66Cr · 0.0Cr . ↓CMF1d</sub> | 368.35 | -16.2% | +55.3% | 22d | SMA-OK | RS-OK | +0.00% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . ↗95Cr · 0.0Cr . ↑CMF2d</sub> | 58.54 | 0.0% | +164.3% | 25d | SMA-OK | RS-OK | +0.00% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . ↘56Cr · 0.0Cr . ↑CMF20d</sub> | 775.35 | 0.0% | +247.0% | 25d | SMA-OK | RS-OK | +0.00% |
| [ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE)<br><sub>✓ SAFE . ↘34Cr · 0.0Cr . ↑CMF6d</sub> | 1212.30 | -3.3% | +61.9% | 25d | SMA-OK | RS-OK | +0.00% |
| [YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH)<br><sub>✓ SAFE . ↘47Cr · 0.0Cr . ↑CMF18d</sub> | 1033.70 | -11.1% | +87.7% | 25d | SMA-OK | RS-OK | +0.00% |
| [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL)<br><sub>✓ SAFE . ↗73Cr · 0.0Cr . ↓CMF5d</sub> | 1047.80 | -5.2% | +37.6% | 25d | SMA-OK | RS-OK | +0.00% |
| [WHEELS](https://in.tradingview.com/chart/?symbol=NSE:WHEELS)<br><sub>✓ SAFE . ↘54Cr · 0.0Cr . ↑CMF26d</sub> | 2241.30 | -6.6% | +213.9% | 27d | SMA-OK | RS-OK | +0.00% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [IPCALAB](https://in.tradingview.com/chart/?symbol=NSE:IPCALAB)<br><sub>⚠ CAUTION . →40Cr · 0.0Cr . ↓CMF14d</sub> | 1943.20 | -3.3% | +53.2% | 30d | SMA-OK | RS-OK | +0.00% |
| [ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN)<br><sub>✓ SAFE . ↗299Cr · 0.0Cr . ↑CMF30d</sub> | 312.75 | -0.9% | +90.1% | 31d | SMA-OK | RS-OK | +0.00% |
| [EMIL](https://in.tradingview.com/chart/?symbol=NSE:EMIL)<br><sub>✓ SAFE . →90Cr · 0.0Cr . ↑CMF16d</sub> | 204.05 | -0.6% | +138.4% | 31d | SMA-OK | RS-OK | +0.00% |
| [FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX)<br><sub>✓ SAFE . →72Cr · 0.0Cr . ↑CMF30d</sub> | 106.10 | -5.3% | +187.5% | 31d | SMA-OK | RS-OK | +0.00% |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH)<br><sub>✓ SAFE . →24Cr · 0.0Cr . ↑CMF0d</sub> | 1978.90 | -6.5% | +75.5% | 34d | SMA-OK | RS-OK | +0.00% |
| [ACMESOLAR](https://in.tradingview.com/chart/?symbol=NSE:ACMESOLAR)<br><sub>✓ SAFE . →100Cr · 0.0Cr . ↑CMF30d</sub> | 432.55 | -5.7% | +117.4% | 34d | SMA-OK | RS-OK | +0.00% |
| [MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX)<br><sub>✓ SAFE . →588Cr · 0.0Cr . ↓CMF4d</sub> | 3204.00 | -6.9% | +100.2% | 35d | SMA-OK | RS-OK | +0.00% |
| [BOSCHLTD](https://in.tradingview.com/chart/?symbol=NSE:BOSCHLTD)<br><sub>✓ SAFE . ↘100Cr · 89Cr . ↑CMF30d</sub> | 48000.00 | -4.0% | +67.0% | 35d | SMA-OK | RS-OK | +0.52% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↘428Cr · 0.0Cr . ↑CMF30d</sub> | 1197.20 | -1.3% | +272.0% | 35d | SMA-OK | RS-OK | +0.00% |
| [MANINDS](https://in.tradingview.com/chart/?symbol=NSE:MANINDS)<br><sub>✓ SAFE . →181Cr · 0.0Cr . ↑CMF26d</sub> | 921.55 | -9.7% | +196.7% | 35d | SMA-OK | RS-OK | +0.00% |
| [FINCABLES](https://in.tradingview.com/chart/?symbol=NSE:FINCABLES)<br><sub>✓ SAFE . ↘91Cr · 0.0Cr . ↑CMF17d</sub> | 1458.80 | -1.4% | +105.2% | 35d | SMA-OK | RS-OK | +0.00% |
| [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG)<br><sub>✓ SAFE . ↘48Cr · 0.0Cr . ↑CMF0d</sub> | 704.70 | -1.5% | +190.5% | 35d | SMA-OK | RS-OK | +0.00% |
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>✓ SAFE . ↘45Cr · 0.0Cr . ↑CMF30d</sub> | 521.35 | -9.1% | +228.3% | 35d | SMA-OK | RS-OK | +0.00% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>✓ SAFE . ↗164Cr · 0.0Cr . ↑CMF10d</sub> | 161.45 | -2.1% | +96.2% | 35d | SMA-OK | RS-OK | +0.00% |
| [QPOWER](https://in.tradingview.com/chart/?symbol=NSE:QPOWER)<br><sub>✓ SAFE . ↘45Cr · 0.0Cr . ↑CMF4d</sub> | 1564.60 | -3.1% | +162.9% | 35d | SMA-OK | RS-OK | +0.00% |
| [CYIENTDLM](https://in.tradingview.com/chart/?symbol=NSE:CYIENTDLM)<br><sub>✓ SAFE . ↘28Cr · 0.0Cr . ↑CMF28d</sub> | 893.90 | -8.4% | +228.3% | 35d | SMA-OK | RS-OK | +0.00% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↗141Cr · 0.0Cr . ↑CMF15d</sub> | 239.17 | 0.0% | +120.8% | 36d | SMA-OK | RS-OK | +0.00% |
| [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD)<br><sub>✓ SAFE . ↗218Cr · 0.0Cr . ↑CMF7d</sub> | 303.55 | -6.8% | +93.8% | 37d | SMA-OK | RS-OK | +0.00% |
| [MARINE](https://in.tradingview.com/chart/?symbol=NSE:MARINE)<br><sub>↗142Cr · 0.0Cr . ↑CMF30d</sub> | 436.55 | -0.4% | +187.8% | 37d | SMA-OK | RS-OK | +0.00% |
| [DIVISLAB](https://in.tradingview.com/chart/?symbol=NSE:DIVISLAB)<br><sub>✓ SAFE . →495Cr · 369Cr . ↑CMF30d</sub> | 9575.50 | -0.5% | +68.3% | 40d | SMA-OK | RS-OK | -0.28% |
| [ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS)<br><sub>✓ SAFE . ↗57Cr · 0.0Cr . ↑CMF5d</sub> | 196.36 | 0.0% | +95.5% | 40d | SMA-OK | RS-OK | +0.00% |
| [DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH)<br><sub>✓ SAFE . ↗44Cr · 0.0Cr . ↑CMF15d</sub> | 13756.00 | 0.0% | +101.1% | 40d | SMA-OK | RS-OK | +0.00% |
| [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV)<br><sub>✓ SAFE . ↘33Cr · 72Cr . ↑CMF0d</sub> | 763.65 | 0.0% | +710.9% | 40d | SMA-OK | RS-OK | +5.00% |
| [JGCHEM](https://in.tradingview.com/chart/?symbol=NSE:JGCHEM)<br><sub>✓ SAFE . ↗36Cr · 0.0Cr . ↑CMF3d</sub> | 610.30 | -7.3% | +100.0% | 40d | SMA-OK | RS-OK | +0.00% |
| [ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH)<br><sub>✓ SAFE . ↘43Cr · 0.0Cr . ↑CMF13d</sub> | 1522.30 | 0.0% | +165.3% | 40d | SMA-OK | RS-OK | +0.00% |
| [PRECWIRE](https://in.tradingview.com/chart/?symbol=NSE:PRECWIRE)<br><sub>✓ SAFE . →30Cr · 0.0Cr . ↑CMF30d</sub> | 501.40 | -1.2% | +162.0% | 40d | SMA-OK | RS-OK | +0.00% |
| [FCL](https://in.tradingview.com/chart/?symbol=NSE:FCL)<br><sub>✓ SAFE . ↘118Cr · 0.0Cr . ↓CMF1d</sub> | 55.72 | -7.9% | +189.6% | 42d | SMA-OK | RS-OK | +0.00% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . →205Cr · 0.0Cr . ↑CMF30d</sub> | 133.72 | 0.0% | +297.0% | 43d | SMA-OK | RS-OK | +0.00% |
| [LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB)<br><sub>✓ SAFE . →64Cr · 0.0Cr . ↑CMF0d</sub> | 2005.10 | 0.0% | +53.3% | 43d | SMA-OK | RS-OK | +0.00% |
| [ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO)<br><sub>✓ SAFE . ↘28Cr · 0.0Cr . ↑CMF28d</sub> | 1680.80 | -11.5% | +77.1% | 43d | SMA-OK | RS-OK | +0.00% |
| [MOTHERSON](https://in.tradingview.com/chart/?symbol=NSE:MOTHERSON)<br><sub>⚠ CAUTION . →199Cr · 229Cr . ↓CMF8d</sub> | 165.50 | -3.0% | +62.8% | 44d | SMA-OK | RS-OK | +1.85% |
| [SMLMAH](https://in.tradingview.com/chart/?symbol=NSE:SMLMAH)<br><sub>✓ SAFE . ↘31Cr · 0.0Cr . ↑CMF20d</sub> | 6251.00 | -8.4% | +126.1% | 44d | SMA-OK | RS-OK | +0.00% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>✓ SAFE . ↘305Cr · 0.0Cr . ↑CMF21d</sub> | 1717.90 | -3.6% | +168.4% | 45d | SMA-OK | RS-OK | +0.00% |
| [APARINDS](https://in.tradingview.com/chart/?symbol=NSE:APARINDS)<br><sub>✓ SAFE . →213Cr · 0.0Cr . ↑CMF16d</sub> | 17648.00 | -6.8% | +153.3% | 45d | SMA-OK | RS-OK | +0.00% |
| [MARKSANS](https://in.tradingview.com/chart/?symbol=NSE:MARKSANS)<br><sub>✓ SAFE . ↗80Cr · 0.0Cr . ↓CMF2d</sub> | 325.60 | -6.3% | +107.5% | 45d | SMA-OK | RS-OK | +0.00% |
| [NRBBEARING](https://in.tradingview.com/chart/?symbol=NSE:NRBBEARING)<br><sub>✓ SAFE . ↘37Cr · 0.0Cr . ↑CMF30d</sub> | 542.60 | 0.0% | +151.0% | 45d | SMA-OK | RS-OK | +0.00% |
| [AVALON](https://in.tradingview.com/chart/?symbol=NSE:AVALON)<br><sub>✓ SAFE . ↘118Cr · 0.0Cr . ↑CMF10d</sub> | 2280.20 | -10.1% | +187.2% | 48d | SMA-OK | RS-OK | +0.00% |
| [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH)<br><sub>✓ SAFE . →64Cr · 0.0Cr . ↑CMF18d</sub> | 1773.00 | 0.0% | +151.0% | 49d | SMA-OK | RS-OK | +0.00% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>⚠ CAUTION . ↗137Cr · 0.0Cr . ↑CMF30d</sub> | 1676.80 | -3.3% | +56.6% | 50d | SMA-OK | RS-OK | +0.00% |
| [RAMRAT](https://in.tradingview.com/chart/?symbol=NSE:RAMRAT)<br><sub>✓ SAFE . ↗20Cr · 0.0Cr . ↑CMF2d</sub> | 616.55 | 0.0% | +121.6% | 50d | SMA-OK | RS-OK | +0.00% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . →245Cr · 0.0Cr . ↑CMF30d</sub> | 345.45 | 0.0% | +163.1% | 52d | SMA-OK | RS-OK | +0.00% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↗61Cr · 0.0Cr . ↓CMF1d</sub> | 390.80 | -4.2% | +129.3% | 54d | SMA-OK | RS-OK | +0.00% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . ↗214Cr · 0.0Cr . ↓CMF11d</sub> | 138.79 | -5.4% | +151.2% | 55d | SMA-OK | RS-OK | +0.00% |
| [MTARTECH](https://in.tradingview.com/chart/?symbol=NSE:MTARTECH)<br><sub>✓ SAFE . ↗2251Cr · 944Cr . ↑CMF8d</sub> | 7777.00 | -7.1% | +457.1% | 58d | SMA-OK | RS-OK | -4.25% |
| [IOLCP](https://in.tradingview.com/chart/?symbol=NSE:IOLCP)<br><sub>✓ SAFE . ↘52Cr · 0.0Cr . ↑CMF3d</sub> | 209.39 | -1.7% | +207.0% | 58d | SMA-OK | RS-OK | +0.00% |
| [KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK)<br><sub>✓ SAFE . →56Cr · 0.0Cr . ↓CMF1d</sub> | 321.60 | -6.3% | +88.0% | 60d | SMA-OK | RS-OK | +0.00% |
| [MANORAMA](https://in.tradingview.com/chart/?symbol=NSE:MANORAMA)<br><sub>✓ SAFE . ↘28Cr · 0.0Cr . ↓CMF0d</sub> | 1880.30 | -11.8% | +74.8% | 60d | SMA-OK | RS-OK | +0.00% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . ↘85Cr · 0.0Cr . ↑CMF30d</sub> | 2874.40 | -5.0% | +80.0% | 61d | SMA-OK | RS-OK | +0.00% |
| [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA)<br><sub>✓ SAFE . →57Cr · 0.0Cr . ↑CMF30d</sub> | 384.70 | -2.1% | +76.8% | 62d | SMA-OK | RS-OK | +0.00% |
| [SHILPAMED](https://in.tradingview.com/chart/?symbol=NSE:SHILPAMED)<br><sub>✓ SAFE . →82Cr · 0.0Cr . ↑CMF21d</sub> | 1064.10 | -0.6% | +298.5% | 70d | SMA-OK | RS-OK | +0.00% |
| [AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER)<br><sub>✓ SAFE . ↗62Cr · 0.0Cr . ↑CMF16d</sub> | 1670.00 | -5.5% | +128.0% | 70d | SMA-OK | RS-OK | +0.00% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>✓ SAFE . ↗47Cr · 0.0Cr . ↑CMF4d . DEL59%(T-1)</sub> | 2950.10 | -6.4% | +168.3% | 80d | SMA-OK | RS-OK | +0.00% |
| [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA)<br><sub>✓ SAFE . ↗183Cr · 0.0Cr . ↑CMF30d</sub> | 4276.60 | -8.3% | +205.8% | 95d | SMA-OK | RS-OK | +0.00% |
| [WELCORP](https://in.tradingview.com/chart/?symbol=NSE:WELCORP)<br><sub>✓ SAFE . →468Cr · 0.0Cr . ↑CMF30d</sub> | 2605.80 | -8.3% | +261.0% | 102d | SMA-OK | RS-OK | +0.00% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . →329Cr · 281Cr . ↑CMF30d</sub> | 1977.20 | -2.6% | +135.1% | 103d | SMA-OK | RS-OK | -0.14% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . ↘53Cr · 0.0Cr . ↓CMF2d</sub> | 1541.20 | -8.0% | +93.9% | 114d | SMA-OK | RS-OK | +0.00% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . →62Cr · 0.0Cr . ↑CMF1d</sub> | 810.65 | -4.4% | +193.0% | 119d | SMA-OK | RS-OK | +0.00% |

### By Trend Age

**<2 WEEKS** (33)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ABDL,NSE:ADANIPORTS,NSE:AEGISLOG,NSE:AEGISVOPAK,NSE:APOLLO,NSE:APOLLOHOSP,NSE:BELRISE,NSE:BHEL,NSE:CARBORUNIV,NSE:CGCL,NSE:CGPOWER,NSE:CPPLUS,NSE:CUPID,NSE:GALAXYSURF,NSE:GREAVESCOT,NSE:KAJARIACER,NSE:KIRLOSENG,NSE:LLOYDSENGG,NSE:MANKIND,NSE:MIDHANI,NSE:ONEPOINT,NSE:OPTIEMUS,NSE:PAYTM,NSE:PHOENIXLTD,NSE:PIXTRANS,NSE:PRIVISCL,NSE:PVRINOX,NSE:RAYMONDREL,NSE:REDINGTON,NSE:RPTECH,NSE:SCHNEIDER,NSE:TORNTPHARM,NSE:ZYDUSLIFE
```

**2-4 WEEKS** (18)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ANTELOPUS,NSE:AZAD,NSE:BEML,NSE:CENTUM,NSE:EDELWEISS,NSE:GNFC,NSE:GRAPHITE,NSE:HFCL,NSE:INOXINDIA,NSE:JSWINFRA,NSE:MOTILALOFS,NSE:PAISALO,NSE:RBLBANK,NSE:SHRIPISTON,NSE:SONACOMS,NSE:STAR,NSE:SUDARSCHEM,NSE:VENUSPIPES
```

**1-2 MONTHS** (36)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:ACE,NSE:ACMESOLAR,NSE:AEROFLEX,NSE:BOSCHLTD,NSE:CYIENTDLM,NSE:DIVISLAB,NSE:DYNAMATECH,NSE:EBGNG,NSE:EMIL,NSE:ENGINERSIN,NSE:FCL,NSE:FILATEX,NSE:FINCABLES,NSE:IPCALAB,NSE:JGCHEM,NSE:LUMAXTECH,NSE:MANINDS,NSE:MARINE,NSE:MCX,NSE:PRECWIRE,NSE:QPOWER,NSE:RAYMOND,NSE:ROLEXRINGS,NSE:ROSSTECH,NSE:SAMBHV,NSE:SBC,NSE:SHANTIGOLD,NSE:SHREEJISPG,NSE:SHYAMMETL,NSE:SIGMAADV,NSE:STLTECH,NSE:STYLEBAAZA,NSE:WELSPUNLIV,NSE:WHEELS,NSE:WOCKPHARMA,NSE:YATHARTH
```

**2-3 MONTHS** (22)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:APARINDS,NSE:AUROPHARMA,NSE:AVALON,NSE:ENTERO,NSE:GLAND,NSE:IOLCP,NSE:KTKBANK,NSE:LALPATHLAB,NSE:MANORAMA,NSE:MARKSANS,NSE:MOREPENLAB,NSE:MOTHERSON,NSE:MTARTECH,NSE:NAZARA,NSE:NRBBEARING,NSE:RAMRAT,NSE:RATNAVEER,NSE:SMLMAH,NSE:SSWL,NSE:SYRMA,NSE:TFCILTD,NSE:UNIMECH
```

**3-6 MONTHS** (8)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:AETHER,NSE:KMEW,NSE:LAURUSLABS,NSE:SAILIFE,NSE:SANSERA,NSE:SHILPAMED,NSE:SKYGOLD,NSE:WELCORP
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
