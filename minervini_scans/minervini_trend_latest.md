> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.
# Minervini Trend Template Scan - 2026-10-30
*Generated 2026-10-30 15:51 IST*

### Additions / Deletions vs previous run
| Additions | Deletions |
|-----------|-----------|
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM) | [AARTIDRUGS](https://in.tradingview.com/chart/?symbol=NSE:AARTIDRUGS) |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA) | [ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL) |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML) | [APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO) |
| [BHAGERIA](https://in.tradingview.com/chart/?symbol=NSE:BHAGERIA) | [CNL](https://in.tradingview.com/chart/?symbol=NSE:CNL) |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH) | [CPPLUS](https://in.tradingview.com/chart/?symbol=NSE:CPPLUS) |
| [KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL) | [DELTACORP](https://in.tradingview.com/chart/?symbol=NSE:DELTACORP) |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB) | [EBGNG](https://in.tradingview.com/chart/?symbol=NSE:EBGNG) |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR) | [GRINDWELL](https://in.tradingview.com/chart/?symbol=NSE:GRINDWELL) |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE) | [INDSWFTLAB](https://in.tradingview.com/chart/?symbol=NSE:INDSWFTLAB) |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY) | [NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA) |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV) | [NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA) |
|  | [PAISALO](https://in.tradingview.com/chart/?symbol=NSE:PAISALO) |
|  | [PARACABLES](https://in.tradingview.com/chart/?symbol=NSE:PARACABLES) |
|  | [RPGLIFE](https://in.tradingview.com/chart/?symbol=NSE:RPGLIFE) |
|  | [SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA) |
|  | [SATIN](https://in.tradingview.com/chart/?symbol=NSE:SATIN) |
|  | [SHANTIGOLD](https://in.tradingview.com/chart/?symbol=NSE:SHANTIGOLD) |
|  | [SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL) |
|  | [SIGMAADV](https://in.tradingview.com/chart/?symbol=NSE:SIGMAADV) |
|  | [TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC) |
|  | [UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH) |
|  | [UTTAMSUGAR](https://in.tradingview.com/chart/?symbol=NSE:UTTAMSUGAR) |
|  | [WHEELS](https://in.tradingview.com/chart/?symbol=NSE:WHEELS) |
|  | [WSTCSTPAPR](https://in.tradingview.com/chart/?symbol=NSE:WSTCSTPAPR) |

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

**Qualifying: 58**

### Trend Template Qualifiers

**TradingView watchlist** *(sectioned by trend age — paste into TV import)*
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###<2 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:63MOONS,NSE:AARTIPHARM,NSE:ACUTAAS,NSE:AEROFLEX,NSE:AJANTPHARM,NSE:ALIVUS,NSE:ATHERENERG,NSE:AUROPHARMA,NSE:BEML,NSE:CEMPRO,NSE:CHENNPETRO,NSE:FEDERALBNK,NSE:GESHIP,NSE:GLAND,NSE:GRWRHITECH,NSE:INDHOTEL,NSE:KARURVYSYA,NSE:KPRMILL,NSE:LUMAXTECH,NSE:NAVINFLUOR,NSE:NILKAMAL,NSE:NYKAA,NSE:PHOENIXLTD,NSE:PPLPHARMA,NSE:SAILIFE,NSE:SAREGAMA,NSE:SETL,NSE:SGFIN,NSE:SGMART,NSE:SHAILY,NSE:SKYGOLD,NSE:SMSPHARMA,NSE:SONACOMS,NSE:SYRMA,NSE:WELSPUNLIV,###2-4 WEEKS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:COFORGE,NSE:HFCL,NSE:KROSS,NSE:SOUTHBANK,###1-2 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:CUPID,NSE:DIACABS,NSE:OPTIEMUS,NSE:PTCIL,NSE:PVRINOX,NSE:STLTECH,###2-3 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:BHAGERIA,NSE:MOREPENLAB,NSE:RAYMOND,NSE:SAMBHV,NSE:SBC,NSE:SHREEJISPG,NSE:THELEELA,###3-6 MONTHS,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,NSE:BLISSGVS,NSE:KMEW,NSE:LAURUSLABS,NSE:RATNAVEER,NSE:SSWL,NSE:TFCILTD
```

| Symbol | Close | %off 52wk-high | %above 52wk-low | Age | SMA stack | RS gate | Day chg% |
|--------|------:|----------------:|------------------:|----:|:---------:|:-------:|--------:|
| [AEROFLEX](https://in.tradingview.com/chart/?symbol=NSE:AEROFLEX)<br><sub>✓ SAFE . ↗366Cr · 740Cr . ↓CMF12d</sub> | 536.40 | -6.5% | +237.8% | 0d | SMA-OK | RS-OK | -0.36% |
| [SYRMA](https://in.tradingview.com/chart/?symbol=NSE:SYRMA)<br><sub>✓ SAFE . ↗216Cr · 245Cr . ↓CMF0d</sub> | 1625.30 | -8.8% | +153.9% | 0d | SMA-OK | RS-OK | -2.62% |
| [SETL](https://in.tradingview.com/chart/?symbol=NSE:SETL)<br><sub>✓ SAFE . →29Cr · 48Cr . ↑CMF1d</sub> | 395.85 | -15.4% | +274.7% | 0d | SMA-OK | RS-OK | -2.34% |
| [NILKAMAL](https://in.tradingview.com/chart/?symbol=NSE:NILKAMAL)<br><sub>✓ SAFE . ↗17Cr · 27Cr . ↑CMF1d</sub> | 1948.70 | -7.9% | +82.7% | 0d | SMA-OK | RS-OK | -2.75% |
| [WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV)<br><sub>✓ SAFE . ↗99Cr · 613Cr . ↓CMF10d</sub> | 219.08 | -8.4% | +102.3% | 1d | SMA-OK | RS-OK | +3.26% |
| [NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR)<br><sub>✓ SAFE . ↗152Cr · 338Cr . ↑CMF3d</sub> | 8680.00 | -1.1% | +56.0% | 1d | SMA-OK | RS-OK | +5.08% |
| [AJANTPHARM](https://in.tradingview.com/chart/?symbol=NSE:AJANTPHARM)<br><sub>⚠ CAUTION . ↗57Cr · 334Cr . ↓CMF22d</sub> | 3508.80 | -5.6% | +42.7% | 1d | SMA-OK | RS-OK | +1.42% |
| [SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE)<br><sub>✓ SAFE . ↘62Cr · 197Cr . ↑CMF0d</sub> | 1557.50 | -7.0% | +95.9% | 1d | SMA-OK | RS-OK | +4.13% |
| [AUROPHARMA](https://in.tradingview.com/chart/?symbol=NSE:AUROPHARMA)<br><sub>⚠ CAUTION . →122Cr · 160Cr . ↑CMF4d</sub> | 1681.40 | -3.0% | +49.9% | 1d | SMA-OK | RS-OK | +1.30% |
| [SHAILY](https://in.tradingview.com/chart/?symbol=NSE:SHAILY)<br><sub>✓ SAFE . ↗47Cr · 113Cr . ↑CMF4d</sub> | 3169.80 | -8.3% | +74.0% | 1d | SMA-OK | RS-OK | +3.71% |
| [KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL)<br><sub>⚠ CAUTION . ↗43Cr · 112Cr . ↑CMF6d</sub> | 1114.60 | -8.5% | +37.5% | 1d | SMA-OK | RS-OK | +2.95% |
| [BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML)<br><sub>✓ SAFE . →40Cr · 32Cr . ↑CMF5d</sub> | 1988.60 | -9.6% | +45.2% | 1d | SMA-OK | RS-OK | +0.64% |
| [INDHOTEL](https://in.tradingview.com/chart/?symbol=NSE:INDHOTEL)<br><sub>✓ SAFE . ↗484Cr · 894Cr . ↑CMF1d</sub> | 777.00 | -0.7% | +36.1% | 2d | SMA-OK | RS-OK | -0.68% |
| [SKYGOLD](https://in.tradingview.com/chart/?symbol=NSE:SKYGOLD)<br><sub>✓ SAFE . →230Cr · 113Cr . ↑CMF16d</sub> | 883.20 | -16.7% | +192.9% | 2d | SMA-OK | RS-OK | +0.77% |
| [PHOENIXLTD](https://in.tradingview.com/chart/?symbol=NSE:PHOENIXLTD)<br><sub>⚠ CAUTION . ↘78Cr · 89Cr . ↓CMF23d</sub> | 1957.20 | -9.1% | +32.5% | 2d | SMA-OK | RS-OK | -0.64% |
| [SGFIN](https://in.tradingview.com/chart/?symbol=NSE:SGFIN)<br><sub>✓ SAFE . ↘31Cr · 31Cr . ↑CMF21d</sub> | 689.00 | -6.3% | +107.4% | 2d | SMA-OK | RS-OK | -6.25% |
| [PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA)<br><sub>✓ SAFE . ↗443Cr · 641Cr . ↑CMF2d</sub> | 238.91 | 0.0% | +79.3% | 3d | SMA-OK | RS-OK | +3.52% |
| [ALIVUS](https://in.tradingview.com/chart/?symbol=NSE:ALIVUS)<br><sub>✓ SAFE . ↗30Cr · 162Cr . ↓CMF0d</sub> | 1415.30 | -2.0% | +64.6% | 3d | SMA-OK | RS-OK | +1.28% |
| [NYKAA](https://in.tradingview.com/chart/?symbol=NSE:NYKAA)<br><sub>✓ SAFE . ↘143Cr · 266Cr . ↑CMF12d</sub> | 352.90 | 0.0% | +50.4% | 3d | SMA-OK | RS-OK | +3.04% |
| [CEMPRO](https://in.tradingview.com/chart/?symbol=NSE:CEMPRO)<br><sub>✓ SAFE . ↘53Cr · 38Cr . ↓CMF27d</sub> | 1265.00 | -22.8% | +148.2% | 3d | SMA-OK | RS-OK | -1.74% |
| [LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH)<br><sub>✓ SAFE . →42Cr · 26Cr . ↑CMF4d</sub> | 2022.70 | -4.4% | +79.4% | 3d | SMA-OK | RS-OK | -1.74% |
| [SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS)<br><sub>✓ SAFE . ↗369Cr · 306Cr . ↑CMF4d</sub> | 890.50 | 0.0% | +100.4% | 4d | SMA-OK | RS-OK | +1.93% |
| [SMSPHARMA](https://in.tradingview.com/chart/?symbol=NSE:SMSPHARMA)<br><sub>✓ SAFE . ↗38Cr · 220Cr . ↑CMF0d</sub> | 511.35 | 0.0% | +88.3% | 4d | SMA-OK | RS-OK | +5.26% |
| [KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA)<br><sub>✓ SAFE . →168Cr · 105Cr . ↓CMF2d</sub> | 356.10 | -3.8% | +47.7% | 4d | SMA-OK | RS-OK | +0.45% |
| [GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND)<br><sub>✓ SAFE . →123Cr · 93Cr . ↑CMF30d</sub> | 3095.90 | -1.7% | +93.9% | 4d | SMA-OK | RS-OK | +0.70% |
| [GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP)<br><sub>✓ SAFE . →101Cr · 91Cr . ↑CMF3d</sub> | 1593.60 | -7.3% | +51.8% | 4d | SMA-OK | RS-OK | -1.56% |
| [AARTIPHARM](https://in.tradingview.com/chart/?symbol=NSE:AARTIPHARM)<br><sub>✓ SAFE . ↗67Cr · 56Cr . ↓CMF9d</sub> | 872.70 | -10.5% | +47.4% | 4d | SMA-OK | RS-OK | -5.92% |
| [SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA)<br><sub>✓ SAFE . ↗24Cr · 43Cr . ↑CMF17d</sub> | 548.65 | -1.5% | +76.4% | 4d | SMA-OK | RS-OK | +2.36% |
| [ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG)<br><sub>✓ SAFE . ↗762Cr · 1391Cr . ↑CMF4d</sub> | 1756.00 | 0.0% | +192.0% | 5d | SMA-OK | RS-OK | +5.59% |
| [ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS)<br><sub>✓ SAFE . ↗555Cr · 459Cr . ↑CMF4d</sub> | 4003.60 | 0.0% | +149.8% | 5d | SMA-OK | RS-OK | +0.68% |
| [SGMART](https://in.tradingview.com/chart/?symbol=NSE:SGMART)<br><sub>✓ SAFE . ↗116Cr · 37Cr . ↑CMF4d</sub> | 856.35 | -0.9% | +168.2% | 6d | SMA-OK | RS-OK | -0.95% |
| [GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH)<br><sub>✓ SAFE . ↗81Cr · 35Cr . ↑CMF27d</sub> | 6974.50 | -5.9% | +157.9% | 6d | SMA-OK | RS-OK | -0.61% |
| [CHENNPETRO](https://in.tradingview.com/chart/?symbol=NSE:CHENNPETRO)<br><sub>✓ SAFE . ↘372Cr · 173Cr . ↑CMF17d</sub> | 1511.50 | -7.1% | +93.1% | 10d | SMA-OK | RS-OK | -0.02% |
| [FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK)<br><sub>✓ SAFE . →297Cr · 143Cr . ↑CMF9d</sub> | 339.70 | -8.6% | +44.1% | 10d | SMA-OK | RS-OK | -2.31% |
| [63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS)<br><sub>✓ SAFE . ↘40Cr · 48Cr . ↓CMF1d</sub> | 948.85 | 0.0% | +101.8% | 10d | SMA-OK | RS-OK | +1.34% |
| [COFORGE](https://in.tradingview.com/chart/?symbol=NSE:COFORGE)<br><sub>✓ SAFE . ↗591Cr · 1252Cr . ↑CMF3d</sub> | 2045.00 | 0.0% | +90.4% | 11d | SMA-OK | RS-OK | +4.23% |
| [KROSS](https://in.tradingview.com/chart/?symbol=NSE:KROSS)<br><sub>✓ SAFE . ↗124Cr · 52Cr . ↑CMF5d</sub> | 280.40 | -8.5% | +77.2% | 14d | SMA-OK | RS-OK | -6.80% |
| [SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK)<br><sub>✓ SAFE . →129Cr · 97Cr . ↑CMF27d</sub> | 55.49 | -1.9% | +65.1% | 16d | SMA-OK | RS-OK | -1.91% |
| [HFCL](https://in.tradingview.com/chart/?symbol=NSE:HFCL)<br><sub>✓ SAFE . ↘364Cr · 386Cr . ↑CMF20d</sub> | 226.27 | -10.0% | +271.2% | 18d | SMA-OK | RS-OK | -4.38% |
| [PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX)<br><sub>✓ SAFE . →136Cr · 99Cr . ↑CMF30d</sub> | 1495.10 | 0.0% | +62.8% | 23d | SMA-OK | RS-OK | +0.32% |
| [CUPID](https://in.tradingview.com/chart/?symbol=NSE:CUPID)<br><sub>✓ SAFE . ↘443Cr · 199Cr . ↑CMF27d</sub> | 324.55 | -11.3% | +595.0% | 24d | SMA-OK | RS-OK | +1.37% |
| [STLTECH](https://in.tradingview.com/chart/?symbol=NSE:STLTECH)<br><sub>✓ SAFE . →292Cr · 255Cr . ↑CMF30d</sub> | 405.15 | 0.0% | +560.0% | 28d | SMA-OK | RS-OK | +1.72% |
| [OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS)<br><sub>✓ SAFE . ↘31Cr · 28Cr . ↑CMF30d</sub> | 789.45 | -11.3% | +169.7% | 30d | SMA-OK | RS-OK | -3.92% |
| [PTCIL](https://in.tradingview.com/chart/?symbol=NSE:PTCIL)<br><sub>✓ SAFE . ↘55Cr · 58Cr . ↑CMF17d</sub> | 23945.00 | -6.9% | +62.6% | 32d | SMA-OK | RS-OK | -3.06% |
| [DIACABS](https://in.tradingview.com/chart/?symbol=NSE:DIACABS)<br><sub>✓ SAFE . ↗363Cr · 101Cr . ↑CMF9d</sub> | 322.85 | -4.3% | +173.7% | 37d | SMA-OK | RS-OK | -0.35% |
| [BHAGERIA](https://in.tradingview.com/chart/?symbol=NSE:BHAGERIA)<br><sub>✓ SAFE . ↗11Cr · 33Cr . ↓CMF0d</sub> | 362.45 | -10.8% | +182.0% | 43d | SMA-OK | RS-OK | -2.24% |
| [SHREEJISPG](https://in.tradingview.com/chart/?symbol=NSE:SHREEJISPG)<br><sub>✓ SAFE . ↗110Cr · 113Cr . ↑CMF30d</sub> | 843.30 | 0.0% | +218.1% | 45d | SMA-OK | RS-OK | +1.29% |
| [SBC](https://in.tradingview.com/chart/?symbol=NSE:SBC)<br><sub>✓ SAFE . ↘75Cr · 74Cr . ↓CMF2d</sub> | 66.15 | -0.6% | +176.5% | 45d | SMA-OK | RS-OK | -0.56% |
| [MOREPENLAB](https://in.tradingview.com/chart/?symbol=NSE:MOREPENLAB)<br><sub>✓ SAFE . ↗253Cr · 230Cr . ↑CMF30d</sub> | 129.55 | -11.9% | +284.6% | 48d | SMA-OK | RS-OK | -5.13% |
| [THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA)<br><sub>✓ SAFE . ↘39Cr · 32Cr . ↓CMF11d</sub> | 634.25 | -0.9% | +62.8% | 54d | SMA-OK | RS-OK | -0.88% |
| [RAYMOND](https://in.tradingview.com/chart/?symbol=NSE:RAYMOND)<br><sub>✓ SAFE . ↘90Cr · 62Cr . ↓CMF2d</sub> | 1100.20 | -15.4% | +241.8% | 55d | SMA-OK | RS-OK | -0.15% |
| [SAMBHV](https://in.tradingview.com/chart/?symbol=NSE:SAMBHV)<br><sub>✓ SAFE . ↘33Cr · 35Cr . ↓CMF1d</sub> | 152.26 | -11.7% | +85.0% | 55d | SMA-OK | RS-OK | -4.44% |
| [BLISSGVS](https://in.tradingview.com/chart/?symbol=NSE:BLISSGVS)<br><sub>✓ SAFE . →52Cr · 21Cr . ↑CMF30d</sub> | 527.10 | -2.7% | +312.1% | 68d | SMA-OK | RS-OK | +0.68% |
| [RATNAVEER](https://in.tradingview.com/chart/?symbol=NSE:RATNAVEER)<br><sub>✓ SAFE . ↘111Cr · 213Cr . ↑CMF0d</sub> | 360.25 | 0.0% | +174.4% | 72d | SMA-OK | RS-OK | +2.10% |
| [SSWL](https://in.tradingview.com/chart/?symbol=NSE:SSWL)<br><sub>✓ SAFE . ↗348Cr · 60Cr . ↑CMF19d</sub> | 493.65 | -7.3% | +189.6% | 74d | SMA-OK | RS-OK | -6.11% |
| [TFCILTD](https://in.tradingview.com/chart/?symbol=NSE:TFCILTD)<br><sub>✓ SAFE . →175Cr · 170Cr . ↑CMF3d</sub> | 157.92 | -1.8% | +185.9% | 75d | SMA-OK | RS-OK | -1.09% |
| [KMEW](https://in.tradingview.com/chart/?symbol=NSE:KMEW)<br><sub>✓ SAFE . ↘35Cr · 53Cr . ↑CMF24d</sub> | 3094.80 | -7.5% | +155.9% | 100d | SMA-OK | RS-OK | +0.18% |
| [LAURUSLABS](https://in.tradingview.com/chart/?symbol=NSE:LAURUSLABS)<br><sub>✓ SAFE . →262Cr · 361Cr . ↓CMF0d</sub> | 1955.00 | -5.5% | +112.3% | 117d | SMA-OK | RS-OK | -2.37% |

### By Trend Age

**<2 WEEKS** (35)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:63MOONS,NSE:AARTIPHARM,NSE:ACUTAAS,NSE:AEROFLEX,NSE:AJANTPHARM,NSE:ALIVUS,NSE:ATHERENERG,NSE:AUROPHARMA,NSE:BEML,NSE:CEMPRO,NSE:CHENNPETRO,NSE:FEDERALBNK,NSE:GESHIP,NSE:GLAND,NSE:GRWRHITECH,NSE:INDHOTEL,NSE:KARURVYSYA,NSE:KPRMILL,NSE:LUMAXTECH,NSE:NAVINFLUOR,NSE:NILKAMAL,NSE:NYKAA,NSE:PHOENIXLTD,NSE:PPLPHARMA,NSE:SAILIFE,NSE:SAREGAMA,NSE:SETL,NSE:SGFIN,NSE:SGMART,NSE:SHAILY,NSE:SKYGOLD,NSE:SMSPHARMA,NSE:SONACOMS,NSE:SYRMA,NSE:WELSPUNLIV
```

**2-4 WEEKS** (4)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:COFORGE,NSE:HFCL,NSE:KROSS,NSE:SOUTHBANK
```

**1-2 MONTHS** (6)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:CUPID,NSE:DIACABS,NSE:OPTIEMUS,NSE:PTCIL,NSE:PVRINOX,NSE:STLTECH
```

**2-3 MONTHS** (7)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:BHAGERIA,NSE:MOREPENLAB,NSE:RAYMOND,NSE:SAMBHV,NSE:SBC,NSE:SHREEJISPG,NSE:THELEELA
```

**3-6 MONTHS** (6)
```
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WATCHLIST,NSE:BLISSGVS,NSE:KMEW,NSE:LAURUSLABS,NSE:RATNAVEER,NSE:SSWL,NSE:TFCILTD
```
---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
