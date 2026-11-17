> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Weekly RS EMA21 + WT1 Uptrend — 2026-11-17

Price data: 2026-11-17. Current developing week included; signals can change before the week closes. NSE common equities; price > Rs50; market cap Rs1,000 crore to Rs5 lakh crore. Weekly RS = stock close / NIFTY MIDSML 400 close x 1000; EMA21 uses adjust=False. Weekly WT1 uses HLC3, EMA10 channel and EMA21 smoothing, matching the existing WaveTrend calculator. Both latest weekly values must be strictly greater than their previous weekly values. Minimum 22 weekly bars; all available history up to 1500 daily bars. Flat slopes do not qualify. No daily EMA200, 52-week-high, float, liquidity, WT1 zero-line or WT2 gate. No manual-list bypass. All qualifiers are shown.

Universe: 1450 | Evaluated: 996 | Qualified: 282 | Excluded: 454

[Weekly chart dashboard](../dashboard/weekly_rs_wt.html)

## TradingView watchlist

```text
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WEEKLY RS21 WT1 UP,NSE:360ONE,NSE:5PAISA,NSE:63MOONS,NSE:AARTIDRUGS,NSE:ABDL,NSE:ABREL,NSE:ACE,NSE:ACUTAAS,NSE:AEGISVOPAK,NSE:AEROENTER,NSE:AETHER,NSE:AFFLE,NSE:AGARWALEYE,NSE:AGIIL,NSE:AIIL,NSE:AJAXENGG,NSE:AJMERA,NSE:ALEMBICLTD,NSE:ALICON,NSE:ALLDIGI,NSE:ANANDRATHI,NSE:ANGELONE,NSE:ANTHEM,NSE:ANUP,NSE:ANURAS,NSE:APLAPOLLO,NSE:APLLTD,NSE:APOLLO,NSE:ARIS,NSE:ARTEMISMED,NSE:ARVSMART,NSE:ASAHIINDIA,NSE:ASKAUTOLTD,NSE:ASTRAMICRO,NSE:ATHERENERG,NSE:AUTOAXLES,NSE:AVANTEL,NSE:AVTNPL,NSE:AWFIS,NSE:AYMSYNTEX,NSE:BALKRISIND,NSE:BALUFORGE,NSE:BANCOINDIA,NSE:BBL,NSE:BBOX,NSE:BECTORFOOD,NSE:BELRISE,NSE:BEML,NSE:BFINVEST,NSE:BHARTIHEXA,NSE:BOROLTD,NSE:CAMS,NSE:CANTABIL,NSE:CAPITALSFB,NSE:CDSL,NSE:CEATLTD,NSE:CEIGALL,NSE:CEMPRO,NSE:CENTUM,NSE:CHEMPLASTS,NSE:CNL,NSE:COROMANDEL,NSE:COSMOFIRST,NSE:CRAFTSMAN,NSE:CSBBANK,NSE:CUB,NSE:DALMIASUG,NSE:DATAPATTNS,NSE:DCBBANK,NSE:DEEPAKFERT,NSE:DELHIVERY,NSE:DELTACORP,NSE:DIFFNKG,NSE:DIXON,NSE:DSSL,NSE:DVL,NSE:EDELWEISS,NSE:EIMCOELECO,NSE:ELECON,NSE:ELGIEQUIP,NSE:EMAMILTD,NSE:EMCURE,NSE:ENGINERSIN,NSE:ENTERO,NSE:EPL,NSE:ERIS,NSE:ETHOSLTD,NSE:EXCELINDUS,NSE:FAZE3Q,NSE:FDC,NSE:FEDERALBNK,NSE:FEDFINA,NSE:FIEMIND,NSE:FILATEX,NSE:FINEORG,NSE:FLUOROCHEM,NSE:GABRIEL,NSE:GALAPREC,NSE:GESHIP,NSE:GHCL,NSE:GHCLTEXTIL,NSE:GLAND,NSE:GLENMARK,NSE:GNA,NSE:GODREJIND,NSE:GODREJPROP,NSE:GOKULAGRO,NSE:GPPL,NSE:GPTINFRA,NSE:GRAPHITE,NSE:GREAVESCOT,NSE:GRWRHITECH,NSE:GULFOILLUB,NSE:HAVELLS,NSE:HBLENGINE,NSE:HERITGFOOD,NSE:HESTERBIO,NSE:HIKAL,NSE:HINDOILEXP,NSE:HINDPETRO,NSE:HLEGLAS,NSE:HONASA,NSE:ICICIGI,NSE:ICIL,NSE:IDFCFIRSTB,NSE:IGIL,NSE:IIFL,NSE:IKIO,NSE:INDGN,NSE:INDIQUBE,NSE:IREDA,NSE:ISGEC,NSE:ITCHOTELS,NSE:ITDC,NSE:IXIGO,NSE:JAMNAAUTO,NSE:JASH,NSE:JINDALPHOT,NSE:JKCEMENT,NSE:JSL,NSE:JYOTICNC,NSE:KALAMANDIR,NSE:KALYANKJIL,NSE:KANSAINER,NSE:KARURVYSYA,NSE:KDDL,NSE:KFINTECH,NSE:KIMS,NSE:KITEX,NSE:KPRMILL,NSE:KRBL,NSE:KTKBANK,NSE:LALPATHLAB,NSE:LEMONTREE,NSE:LICHSGFIN,NSE:LINDEINDIA,NSE:LMW,NSE:LTFOODS,NSE:LTTS,NSE:LUMAXIND,NSE:LUMAXTECH,NSE:MACPOWER,NSE:MAHABANK,NSE:MANAKCOAT,NSE:MARATHON,NSE:MAXESTATES,NSE:MCX,NSE:METROPOLIS,NSE:MINDACORP,NSE:MMFL,NSE:MOBIKWIK,NSE:MOTILALOFS,NSE:MSTCLTD,NSE:MUFIN,NSE:NAVINFLUOR,NSE:NAZARA,NSE:NELCAST,NSE:NEOGEN,NSE:NEULANDLAB,NSE:NH,NSE:NILKAMAL,NSE:NITINSPIN,NSE:NUVAMA,NSE:NUVOCO,NSE:OBEROIRLTY,NSE:OPTIEMUS,NSE:ORCHPHARMA,NSE:ORIENTELEC,NSE:ORIENTHOT,NSE:PARACABLES,NSE:PARAGMILK,NSE:PATANJALI,NSE:PDSL,NSE:PERSISTENT,NSE:PETRONET,NSE:PHOENIXLTD,NSE:PNBHOUSING,NSE:POLYMED,NSE:POONAWALLA,NSE:PPLPHARMA,NSE:PRESTIGE,NSE:PRIMESECU,NSE:PRINCEPIPE,NSE:PROTEAN,NSE:PRSMJOHNSN,NSE:PVRINOX,NSE:QUESS,NSE:RACLGEAR,NSE:RADICO,NSE:RAMKY,NSE:RBLBANK,NSE:REPCOHOME,NSE:RKFORGE,NSE:ROLEXRINGS,NSE:ROSSTECH,NSE:RPEL,NSE:RPSGVENT,NSE:SAILIFE,NSE:SAKAR,NSE:SAMHI,NSE:SANATHAN,NSE:SANDHAR,NSE:SANGAMIND,NSE:SANSERA,NSE:SAREGAMA,NSE:SASKEN,NSE:SATIN,NSE:SDBL,NSE:SHARDAMOTR,NSE:SHREECEM,NSE:SHYAMMETL,NSE:SIGNATURE,NSE:SIMPLEXINF,NSE:SMARTWORKS,NSE:SMSPHARMA,NSE:SOBHA,NSE:SONACOMS,NSE:SOUTHBANK,NSE:SPAL,NSE:SPORTKING,NSE:STEL,NSE:STYLAMIND,NSE:SUDARSCHEM,NSE:SUNTECK,NSE:SUNTV,NSE:SURAKSHA,NSE:SURYODAY,NSE:SYNGENE,NSE:TALBROAUTO,NSE:TANLA,NSE:TASTYBITE,NSE:TATACOMM,NSE:TCPLPACK,NSE:THELEELA,NSE:THOMASCOOK,NSE:TI,NSE:TIIL,NSE:TIMETECHNO,NSE:TIPSMUSIC,NSE:TMB,NSE:TTKHLTCARE,NSE:TVSSCS,NSE:TVSSRICHAK,NSE:UDS,NSE:UFLEX,NSE:UNIMECH,NSE:UNOMINDA,NSE:UTTAMSUGAR,NSE:VARROC,NSE:VIJAYA,NSE:VMART,NSE:VRLLOG,NSE:VSSL,NSE:WELSPUNLIV,NSE:WESTLIFE,NSE:WOCKPHARMA,NSE:WONDERLA,NSE:XPROINDIA,NSE:YATHARTH,NSE:ZENSARTECH,NSE:ZENTEC,NSE:ZOTA
```

## All qualifying stocks

| Symbol | Close | Week % | RS EMA21 | Previous | RS slope | WT1 | Previous WT1 | WT1 slope | Weeks |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [NSE:360ONE](https://in.tradingview.com/chart/?symbol=NSE:360ONE&interval=W) | 1202.85 | +2.21 | 53.6427 | 53.2426 | +0.4000 | 4.9509 | -5.0104 | +9.9613 | 316 |
| [NSE:5PAISA](https://in.tradingview.com/chart/?symbol=NSE:5PAISA&interval=W) | 350.05 | +3.23 | 16.4493 | 16.4167 | +0.0326 | -0.4753 | -4.8185 | +4.3432 | 316 |
| [NSE:63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS&interval=W) | 958.90 | +3.84 | 40.8347 | 40.3230 | +0.5118 | 51.9664 | 50.0397 | +1.9267 | 316 |
| [NSE:AARTIDRUGS](https://in.tradingview.com/chart/?symbol=NSE:AARTIDRUGS&interval=W) | 502.80 | -0.90 | 20.7967 | 20.4668 | +0.3299 | 48.6282 | 41.2143 | +7.4139 | 316 |
| [NSE:ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL&interval=W) | 791.65 | +4.48 | 32.7025 | 32.1790 | +0.5235 | 64.8331 | 57.9332 | +6.8999 | 125 |
| [NSE:ABREL](https://in.tradingview.com/chart/?symbol=NSE:ABREL&interval=W) | 1260.80 | +4.80 | 59.4462 | 59.3488 | +0.0974 | -34.1820 | -42.8662 | +8.6842 | 316 |
| [NSE:ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE&interval=W) | 1173.75 | -0.53 | 53.3934 | 53.1079 | +0.2855 | 32.9624 | 31.4358 | +1.5265 | 316 |
| [NSE:ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS&interval=W) | 3942.90 | -2.38 | 165.3737 | 163.0159 | +2.3578 | 53.1479 | 49.1029 | +4.0450 | 271 |
| [NSE:AEGISVOPAK](https://in.tradingview.com/chart/?symbol=NSE:AEGISVOPAK&interval=W) | 279.46 | -2.26 | 12.9060 | 12.8574 | +0.0486 | 9.8181 | 5.9719 | +3.8462 | 77 |
| [NSE:AEROENTER](https://in.tradingview.com/chart/?symbol=NSE:AEROENTER&interval=W) | 133.31 | +1.22 | 6.0383 | 6.0033 | +0.0350 | 18.4668 | 12.9382 | +5.5286 | 209 |
| [NSE:AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER&interval=W) | 1662.70 | -0.86 | 75.1107 | 74.6538 | +0.4569 | 36.2236 | 34.4745 | +1.7491 | 234 |
| [NSE:AFFLE](https://in.tradingview.com/chart/?symbol=NSE:AFFLE&interval=W) | 1580.80 | -1.70 | 73.7715 | 73.5731 | +0.1984 | -3.1361 | -8.7231 | +5.5869 | 316 |
| [NSE:AGARWALEYE](https://in.tradingview.com/chart/?symbol=NSE:AGARWALEYE&interval=W) | 539.95 | -1.97 | 24.2590 | 24.0974 | +0.1616 | 31.5991 | 24.2269 | +7.3722 | 94 |
| [NSE:AGIIL](https://in.tradingview.com/chart/?symbol=NSE:AGIIL&interval=W) | 321.75 | +1.62 | 14.1123 | 13.9816 | +0.1307 | -21.9398 | -32.3214 | +10.3817 | 123 |
| [NSE:AIIL](https://in.tradingview.com/chart/?symbol=NSE:AIIL&interval=W) | 568.50 | -1.43 | 26.4170 | 26.3344 | +0.0827 | 19.1545 | 15.4698 | +3.6847 | 135 |
| [NSE:AJAXENGG](https://in.tradingview.com/chart/?symbol=NSE:AJAXENGG&interval=W) | 577.25 | -0.28 | 27.4859 | 27.4681 | +0.0177 | 4.0880 | -0.3281 | +4.4160 | 92 |
| [NSE:AJMERA](https://in.tradingview.com/chart/?symbol=NSE:AJMERA&interval=W) | 135.69 | +1.81 | 6.1727 | 6.1397 | +0.0330 | 19.6574 | 12.4369 | +7.2206 | 316 |
| [NSE:ALEMBICLTD](https://in.tradingview.com/chart/?symbol=NSE:ALEMBICLTD&interval=W) | 113.83 | +0.32 | 4.7845 | 4.7175 | +0.0670 | 26.5610 | 17.8091 | +8.7519 | 316 |
| [NSE:ALICON](https://in.tradingview.com/chart/?symbol=NSE:ALICON&interval=W) | 1005.50 | +3.01 | 39.0645 | 38.1523 | +0.9121 | 59.4787 | 53.6813 | +5.7974 | 316 |
| [NSE:ALLDIGI](https://in.tradingview.com/chart/?symbol=NSE:ALLDIGI&interval=W) | 833.30 | -0.13 | 39.3943 | 39.3404 | +0.0539 | -3.3745 | -10.2741 | +6.8996 | 316 |
| [NSE:ANANDRATHI](https://in.tradingview.com/chart/?symbol=NSE:ANANDRATHI&interval=W) | 2375.30 | -0.25 | 111.9634 | 111.7768 | +0.1866 | 16.1941 | 10.1627 | +6.0313 | 258 |
| [NSE:ANGELONE](https://in.tradingview.com/chart/?symbol=NSE:ANGELONE&interval=W) | 349.80 | +0.23 | 14.9556 | 14.7749 | +0.1807 | 16.3560 | 4.7264 | +11.6296 | 316 |
| [NSE:ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM&interval=W) | 924.25 | -1.36 | 41.6738 | 41.4120 | +0.2618 | 38.2551 | 35.5168 | +2.7383 | 70 |
| [NSE:ANUP](https://in.tradingview.com/chart/?symbol=NSE:ANUP&interval=W) | 1798.40 | +4.26 | 82.7434 | 82.3995 | +0.3439 | -35.7396 | -45.9134 | +10.1738 | 316 |
| [NSE:ANURAS](https://in.tradingview.com/chart/?symbol=NSE:ANURAS&interval=W) | 1317.50 | +1.30 | 59.4351 | 59.0649 | +0.3702 | -19.9417 | -35.4199 | +15.4782 | 296 |
| [NSE:APLAPOLLO](https://in.tradingview.com/chart/?symbol=NSE:APLAPOLLO&interval=W) | 2188.50 | -2.80 | 102.2895 | 102.0307 | +0.2588 | 37.2960 | 34.1323 | +3.1637 | 316 |
| [NSE:APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD&interval=W) | 1050.65 | +1.99 | 41.7100 | 40.8461 | +0.8639 | 41.8303 | 33.1276 | +8.7027 | 316 |
| [NSE:APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO&interval=W) | 458.35 | -3.63 | 19.4305 | 19.1771 | +0.2535 | 53.7897 | 46.0420 | +7.7478 | 316 |
| [NSE:ARIS](https://in.tradingview.com/chart/?symbol=NSE:ARIS&interval=W) | 150.47 | +2.46 | 6.6306 | 6.5725 | +0.0580 | 44.6842 | 40.3595 | +4.3247 | 74 |
| [NSE:ARTEMISMED](https://in.tradingview.com/chart/?symbol=NSE:ARTEMISMED&interval=W) | 348.75 | +8.37 | 15.0122 | 14.8421 | +0.1701 | 28.9032 | 23.3780 | +5.5252 | 316 |
| [NSE:ARVSMART](https://in.tradingview.com/chart/?symbol=NSE:ARVSMART&interval=W) | 620.25 | -0.04 | 29.3797 | 29.3453 | +0.0344 | -0.6301 | -6.2426 | +5.6126 | 316 |
| [NSE:ASAHIINDIA](https://in.tradingview.com/chart/?symbol=NSE:ASAHIINDIA&interval=W) | 1166.50 | +5.07 | 46.9894 | 46.0982 | +0.8912 | 50.7083 | 40.2782 | +10.4301 | 316 |
| [NSE:ASKAUTOLTD](https://in.tradingview.com/chart/?symbol=NSE:ASKAUTOLTD&interval=W) | 639.85 | -0.44 | 28.2868 | 28.0492 | +0.2376 | 37.1044 | 34.8192 | +2.2852 | 158 |
| [NSE:ASTRAMICRO](https://in.tradingview.com/chart/?symbol=NSE:ASTRAMICRO&interval=W) | 1660.40 | -2.53 | 77.4381 | 77.2249 | +0.2132 | 6.2156 | 1.8377 | +4.3779 | 316 |
| [NSE:ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG&interval=W) | 1908.60 | -1.87 | 73.1110 | 71.2758 | +1.8353 | 67.7506 | 64.2810 | +3.4696 | 81 |
| [NSE:AUTOAXLES](https://in.tradingview.com/chart/?symbol=NSE:AUTOAXLES&interval=W) | 1791.00 | -1.34 | 83.0907 | 82.8169 | +0.2738 | -23.4027 | -35.7954 | +12.3927 | 316 |
| [NSE:AVANTEL](https://in.tradingview.com/chart/?symbol=NSE:AVANTEL&interval=W) | 160.83 | -2.39 | 7.4731 | 7.4497 | +0.0234 | -24.5522 | -34.9611 | +10.4088 | 121 |
| [NSE:AVTNPL](https://in.tradingview.com/chart/?symbol=NSE:AVTNPL&interval=W) | 101.22 | +4.76 | 4.2477 | 4.1874 | +0.0603 | 62.8521 | 60.7077 | +2.1444 | 316 |
| [NSE:AWFIS](https://in.tradingview.com/chart/?symbol=NSE:AWFIS&interval=W) | 286.72 | -1.67 | 13.4120 | 13.3791 | +0.0328 | -25.5142 | -35.8420 | +10.3278 | 130 |
| [NSE:AYMSYNTEX](https://in.tradingview.com/chart/?symbol=NSE:AYMSYNTEX&interval=W) | 273.37 | +4.13 | 12.4847 | 12.4231 | +0.0616 | 27.4728 | 26.1855 | +1.2872 | 316 |
| [NSE:BALKRISIND](https://in.tradingview.com/chart/?symbol=NSE:BALKRISIND&interval=W) | 2326.40 | +2.42 | 107.9086 | 107.5509 | +0.3577 | -4.2515 | -11.3429 | +7.0914 | 316 |
| [NSE:BALUFORGE](https://in.tradingview.com/chart/?symbol=NSE:BALUFORGE&interval=W) | 532.15 | -3.30 | 24.2456 | 24.1200 | +0.1256 | 1.7796 | -4.2058 | +5.9853 | 134 |
| [NSE:BANCOINDIA](https://in.tradingview.com/chart/?symbol=NSE:BANCOINDIA&interval=W) | 700.40 | +2.92 | 30.6543 | 30.3633 | +0.2910 | -2.5030 | -14.1321 | +11.6291 | 316 |
| [NSE:BBL](https://in.tradingview.com/chart/?symbol=NSE:BBL&interval=W) | 2628.60 | -3.46 | 119.1980 | 118.5210 | +0.6770 | -0.9924 | -9.9214 | +8.9290 | 316 |
| [NSE:BBOX](https://in.tradingview.com/chart/?symbol=NSE:BBOX&interval=W) | 889.85 | -1.20 | 39.9885 | 39.7231 | +0.2655 | 25.2636 | 19.5154 | +5.7482 | 316 |
| [NSE:BECTORFOOD](https://in.tradingview.com/chart/?symbol=NSE:BECTORFOOD&interval=W) | 228.48 | +7.93 | 10.2110 | 10.1372 | +0.0738 | -2.8538 | -10.3888 | +7.5350 | 309 |
| [NSE:BELRISE](https://in.tradingview.com/chart/?symbol=NSE:BELRISE&interval=W) | 235.66 | +9.51 | 10.9603 | 10.9270 | +0.0333 | -5.4943 | -11.4970 | +6.0027 | 78 |
| [NSE:BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML&interval=W) | 2062.50 | -1.70 | 94.4254 | 93.9840 | +0.4414 | 41.4957 | 38.2001 | +3.2956 | 316 |
| [NSE:BFINVEST](https://in.tradingview.com/chart/?symbol=NSE:BFINVEST&interval=W) | 488.00 | +9.38 | 21.1735 | 20.9522 | +0.2212 | -18.4283 | -32.5782 | +14.1499 | 316 |
| [NSE:BHARTIHEXA](https://in.tradingview.com/chart/?symbol=NSE:BHARTIHEXA&interval=W) | 1672.70 | +0.43 | 77.3238 | 77.0403 | +0.2835 | 17.8238 | 13.0414 | +4.7824 | 137 |
| [NSE:BOROLTD](https://in.tradingview.com/chart/?symbol=NSE:BOROLTD&interval=W) | 329.20 | +5.68 | 13.1904 | 12.9319 | +0.2585 | 62.0091 | 56.0667 | +5.9424 | 316 |
| [NSE:CAMS](https://in.tradingview.com/chart/?symbol=NSE:CAMS&interval=W) | 744.00 | +2.47 | 35.0501 | 34.9898 | +0.0604 | -24.2047 | -34.3116 | +10.1069 | 316 |
| [NSE:CANTABIL](https://in.tradingview.com/chart/?symbol=NSE:CANTABIL&interval=W) | 262.60 | +0.79 | 12.0081 | 11.9505 | +0.0576 | 29.1660 | 24.7985 | +4.3675 | 316 |
| [NSE:CAPITALSFB](https://in.tradingview.com/chart/?symbol=NSE:CAPITALSFB&interval=W) | 288.35 | +2.71 | 13.5014 | 13.4697 | +0.0317 | -15.4740 | -24.8598 | +9.3858 | 145 |
| [NSE:CDSL](https://in.tradingview.com/chart/?symbol=NSE:CDSL&interval=W) | 1439.80 | -0.50 | 64.8431 | 64.4275 | +0.4155 | 3.1859 | -7.6366 | +10.8225 | 316 |
| [NSE:CEATLTD](https://in.tradingview.com/chart/?symbol=NSE:CEATLTD&interval=W) | 3538.50 | -0.05 | 165.6899 | 165.3017 | +0.3882 | -14.9095 | -23.5733 | +8.6638 | 316 |
| [NSE:CEIGALL](https://in.tradingview.com/chart/?symbol=NSE:CEIGALL&interval=W) | 386.30 | -2.62 | 17.8337 | 17.7659 | +0.0679 | 42.6899 | 41.9069 | +0.7829 | 120 |
| [NSE:CEMPRO](https://in.tradingview.com/chart/?symbol=NSE:CEMPRO&interval=W) | 1352.30 | +2.85 | 59.4515 | 58.9162 | +0.5353 | 14.2562 | 8.3048 | +5.9514 | 316 |
| [NSE:CENTUM](https://in.tradingview.com/chart/?symbol=NSE:CENTUM&interval=W) | 4377.20 | -2.32 | 192.4020 | 190.6658 | +1.7362 | 46.6632 | 44.5892 | +2.0739 | 316 |
| [NSE:CHEMPLASTS](https://in.tradingview.com/chart/?symbol=NSE:CHEMPLASTS&interval=W) | 252.27 | +6.50 | 10.1620 | 9.9693 | +0.1927 | 13.5411 | 1.8816 | +11.6595 | 274 |
| [NSE:CNL](https://in.tradingview.com/chart/?symbol=NSE:CNL&interval=W) | 1394.30 | -4.40 | 54.1870 | 52.9239 | +1.2631 | 60.7285 | 56.8337 | +3.8948 | 316 |
| [NSE:COROMANDEL](https://in.tradingview.com/chart/?symbol=NSE:COROMANDEL&interval=W) | 1973.50 | +0.95 | 92.3476 | 92.1249 | +0.2226 | -25.3446 | -35.2749 | +9.9303 | 316 |
| [NSE:COSMOFIRST](https://in.tradingview.com/chart/?symbol=NSE:COSMOFIRST&interval=W) | 845.60 | +1.66 | 39.8216 | 39.7514 | +0.0701 | -4.3538 | -8.4009 | +4.0471 | 316 |
| [NSE:CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN&interval=W) | 11195.00 | +1.07 | 501.3071 | 497.7891 | +3.5180 | 42.1346 | 37.0423 | +5.0923 | 296 |
| [NSE:CSBBANK](https://in.tradingview.com/chart/?symbol=NSE:CSBBANK&interval=W) | 330.60 | +8.84 | 15.8156 | 15.8128 | +0.0027 | -44.7892 | -54.1933 | +9.4042 | 316 |
| [NSE:CUB](https://in.tradingview.com/chart/?symbol=NSE:CUB&interval=W) | 232.40 | +0.00 | 11.0473 | 11.0384 | +0.0090 | -2.0661 | -11.8431 | +9.7770 | 316 |
| [NSE:DALMIASUG](https://in.tradingview.com/chart/?symbol=NSE:DALMIASUG&interval=W) | 483.00 | -1.14 | 20.5998 | 20.3452 | +0.2546 | 47.0098 | 43.0544 | +3.9554 | 316 |
| [NSE:DATAPATTNS](https://in.tradingview.com/chart/?symbol=NSE:DATAPATTNS&interval=W) | 4215.90 | -1.22 | 201.7453 | 201.7164 | +0.0289 | -12.6307 | -16.7893 | +4.1586 | 257 |
| [NSE:DCBBANK](https://in.tradingview.com/chart/?symbol=NSE:DCBBANK&interval=W) | 228.13 | -2.09 | 9.9667 | 9.8702 | +0.0966 | 40.8403 | 33.0365 | +7.8038 | 316 |
| [NSE:DEEPAKFERT](https://in.tradingview.com/chart/?symbol=NSE:DEEPAKFERT&interval=W) | 1443.70 | +14.42 | 64.6379 | 64.1832 | +0.4547 | -29.1434 | -38.9809 | +9.8375 | 316 |
| [NSE:DELHIVERY](https://in.tradingview.com/chart/?symbol=NSE:DELHIVERY&interval=W) | 457.95 | +4.96 | 21.0528 | 20.9635 | +0.0893 | -23.2021 | -33.5859 | +10.3838 | 235 |
| [NSE:DELTACORP](https://in.tradingview.com/chart/?symbol=NSE:DELTACORP&interval=W) | 84.98 | +0.73 | 3.5037 | 3.4469 | +0.0569 | 23.5283 | 17.6197 | +5.9086 | 316 |
| [NSE:DIFFNKG](https://in.tradingview.com/chart/?symbol=NSE:DIFFNKG&interval=W) | 433.90 | -3.14 | 19.9201 | 19.8328 | +0.0873 | 29.9509 | 28.0140 | +1.9369 | 112 |
| [NSE:DIXON](https://in.tradingview.com/chart/?symbol=NSE:DIXON&interval=W) | 13081.00 | +2.21 | 617.9243 | 617.0300 | +0.8943 | -6.9467 | -11.1282 | +4.1815 | 316 |
| [NSE:DSSL](https://in.tradingview.com/chart/?symbol=NSE:DSSL&interval=W) | 1115.40 | +5.88 | 52.5095 | 52.4152 | +0.0943 | -22.6490 | -34.6152 | +11.9662 | 316 |
| [NSE:DVL](https://in.tradingview.com/chart/?symbol=NSE:DVL&interval=W) | 319.20 | +3.67 | 13.5080 | 13.3291 | +0.1789 | 46.5712 | 39.0899 | +7.4813 | 316 |
| [NSE:EDELWEISS](https://in.tradingview.com/chart/?symbol=NSE:EDELWEISS&interval=W) | 130.14 | -4.44 | 6.1692 | 6.1625 | +0.0067 | 29.6671 | 28.5538 | +1.1133 | 316 |
| [NSE:EIMCOELECO](https://in.tradingview.com/chart/?symbol=NSE:EIMCOELECO&interval=W) | 2588.00 | -4.66 | 106.5473 | 104.7998 | +1.7475 | 62.1301 | 58.1630 | +3.9672 | 316 |
| [NSE:ELECON](https://in.tradingview.com/chart/?symbol=NSE:ELECON&interval=W) | 453.90 | +2.23 | 21.7173 | 21.7138 | +0.0035 | -13.1369 | -18.2387 | +5.1018 | 316 |
| [NSE:ELGIEQUIP](https://in.tradingview.com/chart/?symbol=NSE:ELGIEQUIP&interval=W) | 582.75 | -0.40 | 27.8964 | 27.8934 | +0.0030 | -8.4026 | -13.8324 | +5.4299 | 316 |
| [NSE:EMAMILTD](https://in.tradingview.com/chart/?symbol=NSE:EMAMILTD&interval=W) | 412.60 | +1.10 | 19.1570 | 19.0954 | +0.0616 | -22.8615 | -36.3112 | +13.4497 | 316 |
| [NSE:EMCURE](https://in.tradingview.com/chart/?symbol=NSE:EMCURE&interval=W) | 2339.40 | -0.94 | 95.3612 | 93.6865 | +1.6747 | 50.8370 | 44.0982 | +6.7388 | 124 |
| [NSE:ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN&interval=W) | 312.90 | +0.14 | 13.1270 | 12.9402 | +0.1868 | 47.6076 | 43.6625 | +3.9451 | 316 |
| [NSE:ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO&interval=W) | 1966.60 | -0.11 | 78.7470 | 77.1973 | +1.5496 | 56.1168 | 53.7388 | +2.3781 | 145 |
| [NSE:EPL](https://in.tradingview.com/chart/?symbol=NSE:EPL&interval=W) | 239.10 | +0.56 | 11.2810 | 11.2633 | +0.0177 | -2.8407 | -8.5534 | +5.7127 | 316 |
| [NSE:ERIS](https://in.tradingview.com/chart/?symbol=NSE:ERIS&interval=W) | 1361.30 | +4.14 | 62.6255 | 62.3645 | +0.2611 | -33.3974 | -45.2123 | +11.8149 | 316 |
| [NSE:ETHOSLTD](https://in.tradingview.com/chart/?symbol=NSE:ETHOSLTD&interval=W) | 2708.00 | -2.60 | 127.3017 | 127.0546 | +0.2471 | 14.7078 | 11.1527 | +3.5551 | 234 |
| [NSE:EXCELINDUS](https://in.tradingview.com/chart/?symbol=NSE:EXCELINDUS&interval=W) | 987.35 | -0.58 | 46.2487 | 46.1420 | +0.1067 | -5.2627 | -12.2179 | +6.9553 | 316 |
| [NSE:FAZE3Q](https://in.tradingview.com/chart/?symbol=NSE:FAZE3Q&interval=W) | 572.10 | +3.21 | 23.8868 | 23.5339 | +0.3529 | -4.3867 | -14.2827 | +9.8960 | 210 |
| [NSE:FDC](https://in.tradingview.com/chart/?symbol=NSE:FDC&interval=W) | 375.90 | +1.02 | 17.8310 | 17.8127 | +0.0183 | 1.4112 | -2.6206 | +4.0319 | 316 |
| [NSE:FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK&interval=W) | 365.80 | +1.34 | 16.3533 | 16.2356 | +0.1177 | 36.8949 | 27.3993 | +9.4957 | 316 |
| [NSE:FEDFINA](https://in.tradingview.com/chart/?symbol=NSE:FEDFINA&interval=W) | 155.66 | -2.37 | 7.4535 | 7.4529 | +0.0006 | 11.1072 | 7.5860 | +3.5212 | 156 |
| [NSE:FIEMIND](https://in.tradingview.com/chart/?symbol=NSE:FIEMIND&interval=W) | 2166.10 | +1.54 | 98.7944 | 98.2934 | +0.5009 | -16.2884 | -26.8365 | +10.5481 | 316 |
| [NSE:FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX&interval=W) | 108.48 | +7.74 | 4.2601 | 4.1662 | +0.0938 | 54.8358 | 51.1267 | +3.7091 | 316 |
| [NSE:FINEORG](https://in.tradingview.com/chart/?symbol=NSE:FINEORG&interval=W) | 5299.00 | -0.01 | 249.0472 | 248.5581 | +0.4891 | 36.7072 | 34.8974 | +1.8098 | 316 |
| [NSE:FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM&interval=W) | 4752.00 | +0.85 | 212.7049 | 211.2028 | +1.5020 | 33.6654 | 28.3610 | +5.3045 | 316 |
| [NSE:GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL&interval=W) | 1498.90 | -3.46 | 66.1274 | 65.5572 | +0.5703 | 51.7366 | 47.8790 | +3.8577 | 316 |
| [NSE:GALAPREC](https://in.tradingview.com/chart/?symbol=NSE:GALAPREC&interval=W) | 1243.20 | +0.25 | 52.5054 | 51.7983 | +0.7071 | 40.3208 | 33.2961 | +7.0246 | 115 |
| [NSE:GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP&interval=W) | 1548.50 | +2.01 | 71.3162 | 71.0271 | +0.2891 | 28.6448 | 26.5888 | +2.0560 | 316 |
| [NSE:GHCL](https://in.tradingview.com/chart/?symbol=NSE:GHCL&interval=W) | 456.80 | +2.56 | 20.7566 | 20.6432 | +0.1134 | -30.2595 | -43.3209 | +13.0614 | 316 |
| [NSE:GHCLTEXTIL](https://in.tradingview.com/chart/?symbol=NSE:GHCLTEXTIL&interval=W) | 136.22 | +4.74 | 5.8781 | 5.8131 | +0.0650 | 41.0592 | 37.1265 | +3.9326 | 180 |
| [NSE:GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND&interval=W) | 3248.40 | -2.57 | 138.3245 | 136.5900 | +1.7345 | 63.6383 | 61.4075 | +2.2308 | 314 |
| [NSE:GLENMARK](https://in.tradingview.com/chart/?symbol=NSE:GLENMARK&interval=W) | 2615.80 | -0.92 | 115.1381 | 114.1165 | +1.0216 | 38.0354 | 31.9048 | +6.1306 | 316 |
| [NSE:GNA](https://in.tradingview.com/chart/?symbol=NSE:GNA&interval=W) | 575.30 | -0.96 | 25.8595 | 25.6885 | +0.1710 | 37.4839 | 36.1796 | +1.3043 | 316 |
| [NSE:GODREJIND](https://in.tradingview.com/chart/?symbol=NSE:GODREJIND&interval=W) | 1095.45 | -1.94 | 52.4538 | 52.4495 | +0.0042 | -22.8028 | -29.4190 | +6.6162 | 316 |
| [NSE:GODREJPROP](https://in.tradingview.com/chart/?symbol=NSE:GODREJPROP&interval=W) | 1892.40 | +2.02 | 86.4521 | 86.0286 | +0.4235 | -11.6529 | -19.4924 | +7.8395 | 316 |
| [NSE:GOKULAGRO](https://in.tradingview.com/chart/?symbol=NSE:GOKULAGRO&interval=W) | 221.89 | -1.97 | 10.6095 | 10.6071 | +0.0024 | -0.2774 | -4.9032 | +4.6258 | 316 |
| [NSE:GPPL](https://in.tradingview.com/chart/?symbol=NSE:GPPL&interval=W) | 173.11 | -0.28 | 7.9331 | 7.8969 | +0.0363 | 36.0773 | 29.7657 | +6.3116 | 316 |
| [NSE:GPTINFRA](https://in.tradingview.com/chart/?symbol=NSE:GPTINFRA&interval=W) | 118.32 | +1.87 | 5.6616 | 5.6608 | +0.0008 | -3.2506 | -6.4499 | +3.1993 | 316 |
| [NSE:GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE&interval=W) | 792.35 | -0.95 | 36.0258 | 35.8313 | +0.1945 | 28.9004 | 25.5496 | +3.3508 | 316 |
| [NSE:GREAVESCOT](https://in.tradingview.com/chart/?symbol=NSE:GREAVESCOT&interval=W) | 243.50 | +7.76 | 10.1113 | 9.9555 | +0.1558 | 18.0281 | 7.1387 | +10.8894 | 316 |
| [NSE:GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH&interval=W) | 7967.00 | +5.91 | 335.2263 | 330.5694 | +4.6568 | 48.2979 | 43.6149 | +4.6830 | 251 |
| [NSE:GULFOILLUB](https://in.tradingview.com/chart/?symbol=NSE:GULFOILLUB&interval=W) | 1135.80 | +0.58 | 52.5034 | 52.3108 | +0.1926 | 16.9876 | 8.5026 | +8.4850 | 316 |
| [NSE:HAVELLS](https://in.tradingview.com/chart/?symbol=NSE:HAVELLS&interval=W) | 1175.00 | +1.21 | 55.8249 | 55.7765 | +0.0483 | -25.5525 | -34.9841 | +9.4315 | 316 |
| [NSE:HBLENGINE](https://in.tradingview.com/chart/?symbol=NSE:HBLENGINE&interval=W) | 785.85 | -1.71 | 37.4086 | 37.3835 | +0.0251 | 24.1144 | 24.0447 | +0.0696 | 316 |
| [NSE:HERITGFOOD](https://in.tradingview.com/chart/?symbol=NSE:HERITGFOOD&interval=W) | 384.15 | -0.49 | 18.2227 | 18.2041 | +0.0187 | 21.5763 | 20.9581 | +0.6182 | 316 |
| [NSE:HESTERBIO](https://in.tradingview.com/chart/?symbol=NSE:HESTERBIO&interval=W) | 2324.60 | +0.04 | 106.8431 | 106.3874 | +0.4556 | 18.2318 | 15.9430 | +2.2888 | 316 |
| [NSE:HIKAL](https://in.tradingview.com/chart/?symbol=NSE:HIKAL&interval=W) | 217.94 | -2.04 | 10.4383 | 10.4377 | +0.0006 | 4.6132 | 3.3358 | +1.2774 | 316 |
| [NSE:HINDOILEXP](https://in.tradingview.com/chart/?symbol=NSE:HINDOILEXP&interval=W) | 222.29 | +15.54 | 8.3172 | 8.0837 | +0.2335 | 20.9270 | 4.4005 | +16.5265 | 316 |
| [NSE:HINDPETRO](https://in.tradingview.com/chart/?symbol=NSE:HINDPETRO&interval=W) | 389.55 | +2.11 | 17.8876 | 17.8095 | +0.0780 | -15.3727 | -25.2304 | +9.8578 | 316 |
| [NSE:HLEGLAS](https://in.tradingview.com/chart/?symbol=NSE:HLEGLAS&interval=W) | 426.95 | -2.66 | 19.5271 | 19.4338 | +0.0933 | 26.6946 | 24.8670 | +1.8276 | 300 |
| [NSE:HONASA](https://in.tradingview.com/chart/?symbol=NSE:HONASA&interval=W) | 517.80 | +3.16 | 22.0820 | 21.8088 | +0.2732 | 34.2519 | 25.6608 | +8.5911 | 159 |
| [NSE:ICICIGI](https://in.tradingview.com/chart/?symbol=NSE:ICICIGI&interval=W) | 1693.50 | +0.14 | 80.1784 | 80.0806 | +0.0977 | -9.2699 | -18.2366 | +8.9667 | 316 |
| [NSE:ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL&interval=W) | 550.25 | +0.52 | 21.3546 | 20.8532 | +0.5014 | 60.1564 | 53.9528 | +6.2036 | 316 |
| [NSE:IDFCFIRSTB](https://in.tradingview.com/chart/?symbol=NSE:IDFCFIRSTB&interval=W) | 83.59 | +5.09 | 3.8572 | 3.8423 | +0.0149 | -1.3165 | -7.2689 | +5.9524 | 316 |
| [NSE:IGIL](https://in.tradingview.com/chart/?symbol=NSE:IGIL&interval=W) | 450.60 | +2.67 | 17.9038 | 17.5348 | +0.3690 | 23.1488 | 15.5648 | +7.5840 | 101 |
| [NSE:IIFL](https://in.tradingview.com/chart/?symbol=NSE:IIFL&interval=W) | 636.40 | -0.73 | 28.5998 | 28.4100 | +0.1898 | 23.5633 | 18.0554 | +5.5079 | 316 |
| [NSE:IKIO](https://in.tradingview.com/chart/?symbol=NSE:IKIO&interval=W) | 201.62 | +4.74 | 9.1808 | 9.1327 | +0.0481 | 5.0035 | 1.0673 | +3.9362 | 180 |
| [NSE:INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN&interval=W) | 648.75 | -2.62 | 28.3618 | 28.0890 | +0.2728 | 62.0014 | 57.3908 | +4.6106 | 132 |
| [NSE:INDIQUBE](https://in.tradingview.com/chart/?symbol=NSE:INDIQUBE&interval=W) | 185.75 | -0.80 | 8.8556 | 8.8510 | +0.0046 | 14.6038 | 13.0539 | +1.5499 | 69 |
| [NSE:IREDA](https://in.tradingview.com/chart/?symbol=NSE:IREDA&interval=W) | 117.40 | -0.76 | 5.5685 | 5.5627 | +0.0058 | -36.3075 | -47.4942 | +11.1867 | 156 |
| [NSE:ISGEC](https://in.tradingview.com/chart/?symbol=NSE:ISGEC&interval=W) | 990.20 | +0.45 | 43.9228 | 43.5698 | +0.3530 | 24.3746 | 19.0429 | +5.3318 | 290 |
| [NSE:ITCHOTELS](https://in.tradingview.com/chart/?symbol=NSE:ITCHOTELS&interval=W) | 177.81 | +2.43 | 8.0848 | 8.0412 | +0.0436 | 14.7891 | 6.2777 | +8.5115 | 95 |
| [NSE:ITDC](https://in.tradingview.com/chart/?symbol=NSE:ITDC&interval=W) | 667.00 | -0.13 | 31.3752 | 31.3163 | +0.0589 | -7.7247 | -12.5667 | +4.8419 | 316 |
| [NSE:IXIGO](https://in.tradingview.com/chart/?symbol=NSE:IXIGO&interval=W) | 175.61 | +7.61 | 8.1036 | 8.0724 | +0.0312 | -23.7283 | -33.7221 | +9.9938 | 127 |
| [NSE:JAMNAAUTO](https://in.tradingview.com/chart/?symbol=NSE:JAMNAAUTO&interval=W) | 143.33 | -3.76 | 6.4548 | 6.4134 | +0.0414 | 29.6623 | 22.9011 | +6.7612 | 316 |
| [NSE:JASH](https://in.tradingview.com/chart/?symbol=NSE:JASH&interval=W) | 558.70 | +1.63 | 25.0981 | 24.9305 | +0.1676 | 33.2602 | 30.5916 | +2.6687 | 316 |
| [NSE:JINDALPHOT](https://in.tradingview.com/chart/?symbol=NSE:JINDALPHOT&interval=W) | 1120.60 | -0.49 | 52.9473 | 52.8719 | +0.0754 | 6.1327 | 0.2008 | +5.9319 | 316 |
| [NSE:JKCEMENT](https://in.tradingview.com/chart/?symbol=NSE:JKCEMENT&interval=W) | 5237.50 | +1.60 | 249.8159 | 249.6984 | +0.1175 | -21.5893 | -30.8958 | +9.3065 | 316 |
| [NSE:JSL](https://in.tradingview.com/chart/?symbol=NSE:JSL&interval=W) | 731.95 | +2.72 | 35.0621 | 35.0606 | +0.0014 | -17.3526 | -23.6160 | +6.2634 | 316 |
| [NSE:JYOTICNC](https://in.tradingview.com/chart/?symbol=NSE:JYOTICNC&interval=W) | 1041.25 | -2.97 | 46.0012 | 45.6114 | +0.3898 | 36.7822 | 34.7467 | +2.0355 | 149 |
| [NSE:KALAMANDIR](https://in.tradingview.com/chart/?symbol=NSE:KALAMANDIR&interval=W) | 89.41 | -0.80 | 4.1853 | 4.1754 | +0.0099 | -32.8774 | -42.4337 | +9.5563 | 165 |
| [NSE:KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL&interval=W) | 682.75 | -2.04 | 27.1874 | 26.6343 | +0.5531 | 30.9105 | 21.0330 | +9.8775 | 296 |
| [NSE:KANSAINER](https://in.tradingview.com/chart/?symbol=NSE:KANSAINER&interval=W) | 201.02 | -0.04 | 9.4331 | 9.4131 | +0.0200 | -19.2500 | -28.1941 | +8.9440 | 316 |
| [NSE:KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA&interval=W) | 393.50 | +3.13 | 16.6230 | 16.3996 | +0.2234 | 65.1745 | 59.8311 | +5.3434 | 316 |
| [NSE:KDDL](https://in.tradingview.com/chart/?symbol=NSE:KDDL&interval=W) | 4560.40 | +9.54 | 181.2670 | 177.5393 | +3.7276 | 52.9940 | 46.5015 | +6.4925 | 316 |
| [NSE:KFINTECH](https://in.tradingview.com/chart/?symbol=NSE:KFINTECH&interval=W) | 965.00 | +1.48 | 43.8850 | 43.6490 | +0.2360 | -1.9518 | -12.2105 | +10.2587 | 204 |
| [NSE:KIMS](https://in.tradingview.com/chart/?symbol=NSE:KIMS&interval=W) | 768.30 | +5.30 | 36.1310 | 36.0622 | +0.0687 | -18.0610 | -25.6678 | +7.6069 | 282 |
| [NSE:KITEX](https://in.tradingview.com/chart/?symbol=NSE:KITEX&interval=W) | 137.14 | +6.33 | 6.4498 | 6.4376 | +0.0122 | -34.3779 | -44.1440 | +9.7660 | 316 |
| [NSE:KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL&interval=W) | 1217.10 | +5.07 | 53.7177 | 53.2569 | +0.4608 | 28.0405 | 19.0375 | +9.0030 | 316 |
| [NSE:KRBL](https://in.tradingview.com/chart/?symbol=NSE:KRBL&interval=W) | 412.95 | -4.42 | 18.8339 | 18.7383 | +0.0955 | 18.8037 | 13.0382 | +5.7655 | 316 |
| [NSE:KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK&interval=W) | 368.80 | +1.89 | 15.2383 | 14.9947 | +0.2435 | 52.3120 | 44.7173 | +7.5946 | 316 |
| [NSE:LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB&interval=W) | 1980.20 | -0.64 | 90.5858 | 90.1548 | +0.4309 | 46.3266 | 45.1341 | +1.1925 | 316 |
| [NSE:LEMONTREE](https://in.tradingview.com/chart/?symbol=NSE:LEMONTREE&interval=W) | 123.31 | +1.11 | 5.5223 | 5.4836 | +0.0387 | 19.9887 | 8.9443 | +11.0444 | 316 |
| [NSE:LICHSGFIN](https://in.tradingview.com/chart/?symbol=NSE:LICHSGFIN&interval=W) | 622.50 | +6.39 | 26.3956 | 26.0520 | +0.3436 | 6.9425 | -7.9538 | +14.8963 | 316 |
| [NSE:LINDEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LINDEINDIA&interval=W) | 6886.00 | +0.52 | 316.3384 | 314.9731 | +1.3652 | -25.0059 | -35.7496 | +10.7437 | 316 |
| [NSE:LMW](https://in.tradingview.com/chart/?symbol=NSE:LMW&interval=W) | 17263.00 | -1.31 | 813.1539 | 811.7416 | +1.4123 | 11.0593 | 8.6328 | +2.4266 | 316 |
| [NSE:LTFOODS](https://in.tradingview.com/chart/?symbol=NSE:LTFOODS&interval=W) | 420.15 | -1.07 | 19.9520 | 19.9337 | +0.0182 | 2.4490 | -1.6486 | +4.0976 | 316 |
| [NSE:LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS&interval=W) | 4208.00 | -0.92 | 181.5005 | 179.4850 | +2.0155 | 33.2142 | 29.5999 | +3.6144 | 316 |
| [NSE:LUMAXIND](https://in.tradingview.com/chart/?symbol=NSE:LUMAXIND&interval=W) | 5701.10 | +0.15 | 268.8132 | 268.3737 | +0.4395 | -0.1754 | -7.7390 | +7.5636 | 316 |
| [NSE:LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH&interval=W) | 2404.00 | +5.48 | 95.5055 | 93.5356 | +1.9699 | 49.1455 | 43.1566 | +5.9889 | 316 |
| [NSE:MACPOWER](https://in.tradingview.com/chart/?symbol=NSE:MACPOWER&interval=W) | 2242.20 | -2.38 | 89.9058 | 88.1513 | +1.7545 | 60.6602 | 60.0294 | +0.6308 | 316 |
| [NSE:MAHABANK](https://in.tradingview.com/chart/?symbol=NSE:MAHABANK&interval=W) | 95.99 | +4.68 | 4.0459 | 3.9904 | +0.0554 | 27.2568 | 15.0188 | +12.2380 | 316 |
| [NSE:MANAKCOAT](https://in.tradingview.com/chart/?symbol=NSE:MANAKCOAT&interval=W) | 164.67 | -4.13 | 6.5371 | 6.4016 | +0.1354 | 69.5634 | 66.1202 | +3.4432 | 316 |
| [NSE:MARATHON](https://in.tradingview.com/chart/?symbol=NSE:MARATHON&interval=W) | 434.70 | -0.28 | 19.8091 | 19.7068 | +0.1023 | -8.2894 | -18.6159 | +10.3265 | 316 |
| [NSE:MAXESTATES](https://in.tradingview.com/chart/?symbol=NSE:MAXESTATES&interval=W) | 574.90 | -0.83 | 24.7493 | 24.4692 | +0.2801 | 34.7432 | 29.5046 | +5.2386 | 160 |
| [NSE:MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX&interval=W) | 3705.40 | -0.39 | 155.6093 | 153.4132 | +2.1961 | 52.7118 | 46.9200 | +5.7918 | 316 |
| [NSE:METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS&interval=W) | 567.00 | +0.50 | 26.8371 | 26.8037 | +0.0335 | 14.0464 | 11.9393 | +2.1071 | 316 |
| [NSE:MINDACORP](https://in.tradingview.com/chart/?symbol=NSE:MINDACORP&interval=W) | 707.75 | -3.86 | 32.5176 | 32.3776 | +0.1399 | 9.9954 | 3.9872 | +6.0082 | 316 |
| [NSE:MMFL](https://in.tradingview.com/chart/?symbol=NSE:MMFL&interval=W) | 664.45 | -2.99 | 27.8643 | 27.4666 | +0.3977 | 29.9576 | 24.0656 | +5.8920 | 316 |
| [NSE:MOBIKWIK](https://in.tradingview.com/chart/?symbol=NSE:MOBIKWIK&interval=W) | 229.55 | +1.20 | 10.4182 | 10.3600 | +0.0582 | 31.4593 | 29.0126 | +2.4468 | 101 |
| [NSE:MOTILALOFS](https://in.tradingview.com/chart/?symbol=NSE:MOTILALOFS&interval=W) | 1240.25 | +1.66 | 49.4289 | 48.4283 | +1.0006 | 53.7296 | 46.5240 | +7.2056 | 316 |
| [NSE:MSTCLTD](https://in.tradingview.com/chart/?symbol=NSE:MSTCLTD&interval=W) | 717.15 | -8.45 | 31.3596 | 31.0589 | +0.3008 | 16.7393 | 10.5296 | +6.2097 | 316 |
| [NSE:MUFIN](https://in.tradingview.com/chart/?symbol=NSE:MUFIN&interval=W) | 139.27 | +0.53 | 6.4493 | 6.4268 | +0.0225 | 42.2817 | 39.9816 | +2.3001 | 159 |
| [NSE:NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR&interval=W) | 9815.00 | -1.87 | 407.0086 | 400.6740 | +6.3346 | 63.3487 | 56.7465 | +6.6021 | 316 |
| [NSE:NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA&interval=W) | 422.00 | -0.80 | 18.0591 | 17.8427 | +0.2164 | 65.7591 | 65.1662 | +0.5929 | 295 |
| [NSE:NELCAST](https://in.tradingview.com/chart/?symbol=NSE:NELCAST&interval=W) | 147.65 | -3.80 | 6.4794 | 6.4197 | +0.0596 | 22.7706 | 18.4362 | +4.3344 | 316 |
| [NSE:NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN&interval=W) | 2778.60 | -1.08 | 111.6203 | 109.4667 | +2.1536 | 59.4091 | 55.5248 | +3.8843 | 316 |
| [NSE:NEULANDLAB](https://in.tradingview.com/chart/?symbol=NSE:NEULANDLAB&interval=W) | 21445.00 | +1.74 | 982.9880 | 978.5181 | +4.4699 | 11.4021 | 8.1425 | +3.2596 | 316 |
| [NSE:NH](https://in.tradingview.com/chart/?symbol=NSE:NH&interval=W) | 1907.60 | +2.54 | 89.3128 | 89.1025 | +0.2103 | -14.2467 | -21.9073 | +7.6606 | 316 |
| [NSE:NILKAMAL](https://in.tradingview.com/chart/?symbol=NSE:NILKAMAL&interval=W) | 2258.10 | +1.26 | 89.7233 | 87.8744 | +1.8489 | 47.2799 | 41.3626 | +5.9173 | 316 |
| [NSE:NITINSPIN](https://in.tradingview.com/chart/?symbol=NSE:NITINSPIN&interval=W) | 683.65 | +1.92 | 29.3915 | 29.0544 | +0.3370 | 62.9043 | 60.1480 | +2.7563 | 316 |
| [NSE:NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA&interval=W) | 1888.30 | +2.19 | 84.4770 | 83.8756 | +0.6014 | 28.5203 | 22.8383 | +5.6820 | 165 |
| [NSE:NUVOCO](https://in.tradingview.com/chart/?symbol=NSE:NUVOCO&interval=W) | 345.55 | +1.22 | 16.1901 | 16.1531 | +0.0369 | 21.5208 | 14.9780 | +6.5428 | 274 |
| [NSE:OBEROIRLTY](https://in.tradingview.com/chart/?symbol=NSE:OBEROIRLTY&interval=W) | 1819.70 | +1.23 | 85.1614 | 84.9572 | +0.2042 | -4.5123 | -11.2758 | +6.7635 | 316 |
| [NSE:OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS&interval=W) | 800.85 | -1.57 | 32.7374 | 32.1733 | +0.5641 | 62.8757 | 62.5197 | +0.3560 | 316 |
| [NSE:ORCHPHARMA](https://in.tradingview.com/chart/?symbol=NSE:ORCHPHARMA&interval=W) | 930.85 | +5.25 | 44.3446 | 44.3182 | +0.0264 | -8.0027 | -10.8997 | +2.8970 | 316 |
| [NSE:ORIENTELEC](https://in.tradingview.com/chart/?symbol=NSE:ORIENTELEC&interval=W) | 201.84 | +1.45 | 8.9084 | 8.8320 | +0.0764 | 13.1214 | 6.8958 | +6.2256 | 316 |
| [NSE:ORIENTHOT](https://in.tradingview.com/chart/?symbol=NSE:ORIENTHOT&interval=W) | 179.00 | +2.03 | 7.1211 | 6.9754 | +0.1457 | 71.7144 | 69.3876 | +2.3268 | 316 |
| [NSE:PARACABLES](https://in.tradingview.com/chart/?symbol=NSE:PARACABLES&interval=W) | 65.27 | -2.25 | 2.9731 | 2.9576 | +0.0155 | 16.5022 | 12.8894 | +3.6128 | 316 |
| [NSE:PARAGMILK](https://in.tradingview.com/chart/?symbol=NSE:PARAGMILK&interval=W) | 334.83 | +1.09 | 13.0179 | 12.7151 | +0.3028 | 52.7527 | 47.5872 | +5.1655 | 316 |
| [NSE:PATANJALI](https://in.tradingview.com/chart/?symbol=NSE:PATANJALI&interval=W) | 404.80 | -3.85 | 18.9192 | 18.8712 | +0.0480 | 1.9798 | -5.8695 | +7.8494 | 316 |
| [NSE:PDSL](https://in.tradingview.com/chart/?symbol=NSE:PDSL&interval=W) | 408.50 | -0.91 | 17.4918 | 17.2834 | +0.2084 | 28.6022 | 20.6458 | +7.9564 | 316 |
| [NSE:PERSISTENT](https://in.tradingview.com/chart/?symbol=NSE:PERSISTENT&interval=W) | 5911.00 | -1.53 | 273.7039 | 272.7476 | +0.9563 | 45.7037 | 45.0908 | +0.6129 | 316 |
| [NSE:PETRONET](https://in.tradingview.com/chart/?symbol=NSE:PETRONET&interval=W) | 328.10 | +1.25 | 14.3260 | 14.1863 | +0.1397 | 73.4388 | 67.3002 | +6.1387 | 316 |
| [NSE:PHOENIXLTD](https://in.tradingview.com/chart/?symbol=NSE:PHOENIXLTD&interval=W) | 2229.00 | -1.15 | 95.7626 | 94.6570 | +1.1056 | 42.7213 | 34.3742 | +8.3471 | 316 |
| [NSE:PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING&interval=W) | 1138.00 | +1.85 | 53.4314 | 53.3210 | +0.1104 | 17.3284 | 15.9148 | +1.4136 | 316 |
| [NSE:POLYMED](https://in.tradingview.com/chart/?symbol=NSE:POLYMED&interval=W) | 1649.60 | -1.88 | 78.6165 | 78.5729 | +0.0436 | -7.0054 | -12.2436 | +5.2383 | 316 |
| [NSE:POONAWALLA](https://in.tradingview.com/chart/?symbol=NSE:POONAWALLA&interval=W) | 490.65 | +1.21 | 22.2857 | 22.1629 | +0.1227 | 13.1600 | 4.8368 | +8.3232 | 316 |
| [NSE:PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA&interval=W) | 240.70 | -1.57 | 10.1675 | 10.0308 | +0.1367 | 52.4125 | 49.2301 | +3.1824 | 214 |
| [NSE:PRESTIGE](https://in.tradingview.com/chart/?symbol=NSE:PRESTIGE&interval=W) | 1691.50 | +2.52 | 74.4954 | 73.8389 | +0.6565 | 6.9475 | -2.5906 | +9.5381 | 316 |
| [NSE:PRIMESECU](https://in.tradingview.com/chart/?symbol=NSE:PRIMESECU&interval=W) | 310.20 | +1.74 | 14.2110 | 14.1455 | +0.0654 | 30.4677 | 24.1437 | +6.3241 | 316 |
| [NSE:PRINCEPIPE](https://in.tradingview.com/chart/?symbol=NSE:PRINCEPIPE&interval=W) | 304.30 | -3.60 | 13.4619 | 13.3498 | +0.1121 | 20.7224 | 13.9625 | +6.7599 | 316 |
| [NSE:PROTEAN](https://in.tradingview.com/chart/?symbol=NSE:PROTEAN&interval=W) | 671.95 | -5.97 | 30.0196 | 29.8015 | +0.2182 | 20.8261 | 16.0672 | +4.7589 | 94 |
| [NSE:PRSMJOHNSN](https://in.tradingview.com/chart/?symbol=NSE:PRSMJOHNSN&interval=W) | 111.97 | -0.51 | 5.3115 | 5.3061 | +0.0054 | -31.1888 | -40.9730 | +9.7841 | 316 |
| [NSE:PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX&interval=W) | 1677.40 | +2.21 | 64.6515 | 63.0782 | +1.5733 | 74.6011 | 73.0197 | +1.5813 | 316 |
| [NSE:QUESS](https://in.tradingview.com/chart/?symbol=NSE:QUESS&interval=W) | 337.15 | -1.59 | 15.2403 | 15.1487 | +0.0917 | 28.5241 | 25.5231 | +3.0010 | 316 |
| [NSE:RACLGEAR](https://in.tradingview.com/chart/?symbol=NSE:RACLGEAR&interval=W) | 1577.00 | +2.32 | 71.3522 | 70.9301 | +0.4221 | 24.3386 | 21.4198 | +2.9188 | 104 |
| [NSE:RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO&interval=W) | 4662.90 | +1.26 | 207.6602 | 206.0807 | +1.5795 | 34.3037 | 28.3136 | +5.9901 | 316 |
| [NSE:RAMKY](https://in.tradingview.com/chart/?symbol=NSE:RAMKY&interval=W) | 395.55 | +2.79 | 17.4197 | 17.2661 | +0.1536 | -30.6743 | -40.7523 | +10.0780 | 316 |
| [NSE:RBLBANK](https://in.tradingview.com/chart/?symbol=NSE:RBLBANK&interval=W) | 390.10 | +1.13 | 18.4028 | 18.3737 | +0.0292 | 19.2886 | 19.0692 | +0.2194 | 316 |
| [NSE:REPCOHOME](https://in.tradingview.com/chart/?symbol=NSE:REPCOHOME&interval=W) | 381.95 | +0.37 | 17.4798 | 17.3974 | +0.0824 | -27.0058 | -38.4766 | +11.4709 | 316 |
| [NSE:RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE&interval=W) | 782.20 | -0.32 | 33.0961 | 32.6573 | +0.4388 | 40.3560 | 33.0251 | +7.3310 | 316 |
| [NSE:ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS&interval=W) | 204.52 | -4.13 | 8.4969 | 8.3665 | +0.1304 | 50.8358 | 47.1871 | +3.6488 | 276 |
| [NSE:ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH&interval=W) | 1555.60 | +0.79 | 63.0375 | 61.8865 | +1.1510 | 67.4834 | 66.3597 | +1.1237 | 102 |
| [NSE:RPEL](https://in.tradingview.com/chart/?symbol=NSE:RPEL&interval=W) | 1971.50 | +1.30 | 78.1203 | 76.4846 | +1.6358 | 58.5655 | 54.7975 | +3.7680 | 120 |
| [NSE:RPSGVENT](https://in.tradingview.com/chart/?symbol=NSE:RPSGVENT&interval=W) | 868.85 | +2.87 | 41.6062 | 41.6032 | +0.0031 | -10.6338 | -19.4773 | +8.8435 | 316 |
| [NSE:SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE&interval=W) | 1751.50 | -9.19 | 72.8395 | 71.7299 | +1.1096 | 63.4039 | 60.6082 | +2.7956 | 101 |
| [NSE:SAKAR](https://in.tradingview.com/chart/?symbol=NSE:SAKAR&interval=W) | 1037.95 | -0.43 | 45.9172 | 45.5349 | +0.3823 | 38.5371 | 38.4274 | +0.1097 | 316 |
| [NSE:SAMHI](https://in.tradingview.com/chart/?symbol=NSE:SAMHI&interval=W) | 164.05 | -1.06 | 7.7973 | 7.7909 | +0.0064 | -9.3733 | -15.8415 | +6.4682 | 166 |
| [NSE:SANATHAN](https://in.tradingview.com/chart/?symbol=NSE:SANATHAN&interval=W) | 590.65 | -0.08 | 24.5199 | 24.1414 | +0.3785 | 66.5445 | 61.9934 | +4.5511 | 100 |
| [NSE:SANDHAR](https://in.tradingview.com/chart/?symbol=NSE:SANDHAR&interval=W) | 583.65 | +12.15 | 27.2445 | 27.1719 | +0.0725 | -35.6482 | -42.7410 | +7.0929 | 316 |
| [NSE:SANGAMIND](https://in.tradingview.com/chart/?symbol=NSE:SANGAMIND&interval=W) | 640.85 | +0.39 | 28.8630 | 28.6782 | +0.1848 | 50.2307 | 44.4653 | +5.7653 | 316 |
| [NSE:SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA&interval=W) | 4614.60 | -1.99 | 191.3006 | 188.3166 | +2.9840 | 65.2910 | 62.9734 | +2.3176 | 270 |
| [NSE:SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA&interval=W) | 674.90 | +3.28 | 25.6246 | 24.9528 | +0.6718 | 70.6842 | 64.2023 | +6.4819 | 316 |
| [NSE:SASKEN](https://in.tradingview.com/chart/?symbol=NSE:SASKEN&interval=W) | 1836.20 | +6.14 | 85.8788 | 85.6672 | +0.2116 | -18.4180 | -24.5033 | +6.0852 | 316 |
| [NSE:SATIN](https://in.tradingview.com/chart/?symbol=NSE:SATIN&interval=W) | 258.88 | -1.46 | 11.3220 | 11.2136 | +0.1084 | 36.9886 | 32.3029 | +4.6857 | 316 |
| [NSE:SDBL](https://in.tradingview.com/chart/?symbol=NSE:SDBL&interval=W) | 76.78 | -0.18 | 3.6350 | 3.6305 | +0.0044 | 1.4020 | -5.5088 | +6.9109 | 316 |
| [NSE:SHARDAMOTR](https://in.tradingview.com/chart/?symbol=NSE:SHARDAMOTR&interval=W) | 967.70 | +0.31 | 43.4654 | 43.1745 | +0.2909 | 16.5070 | 8.0929 | +8.4141 | 316 |
| [NSE:SHREECEM](https://in.tradingview.com/chart/?symbol=NSE:SHREECEM&interval=W) | 24900.00 | +0.99 | 1169.1672 | 1166.7582 | +2.4090 | -7.4668 | -15.1256 | +7.6587 | 316 |
| [NSE:SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL&interval=W) | 1321.10 | +0.40 | 54.3899 | 53.4979 | +0.8920 | 77.8289 | 76.2436 | +1.5853 | 283 |
| [NSE:SIGNATURE](https://in.tradingview.com/chart/?symbol=NSE:SIGNATURE&interval=W) | 835.60 | +9.00 | 37.7826 | 37.5565 | +0.2261 | -34.0776 | -50.1345 | +16.0569 | 165 |
| [NSE:SIMPLEXINF](https://in.tradingview.com/chart/?symbol=NSE:SIMPLEXINF&interval=W) | 287.65 | -3.92 | 12.6447 | 12.5307 | +0.1140 | 43.1288 | 36.5033 | +6.6256 | 316 |
| [NSE:SMARTWORKS](https://in.tradingview.com/chart/?symbol=NSE:SMARTWORKS&interval=W) | 509.70 | -0.30 | 23.8969 | 23.8441 | +0.0529 | 18.6194 | 16.6116 | +2.0078 | 71 |
| [NSE:SMSPHARMA](https://in.tradingview.com/chart/?symbol=NSE:SMSPHARMA&interval=W) | 487.25 | -4.09 | 21.4419 | 21.2511 | +0.1908 | 46.8699 | 46.6218 | +0.2481 | 316 |
| [NSE:SOBHA](https://in.tradingview.com/chart/?symbol=NSE:SOBHA&interval=W) | 1290.40 | +1.50 | 61.7194 | 61.7075 | +0.0119 | -26.1519 | -34.2090 | +8.0571 | 316 |
| [NSE:SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS&interval=W) | 899.70 | -2.10 | 38.4768 | 38.0130 | +0.4639 | 64.6231 | 63.7890 | +0.8341 | 283 |
| [NSE:SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK&interval=W) | 60.70 | -1.88 | 2.4633 | 2.4187 | +0.0446 | 83.0655 | 81.3094 | +1.7561 | 316 |
| [NSE:SPAL](https://in.tradingview.com/chart/?symbol=NSE:SPAL&interval=W) | 939.80 | +4.98 | 44.6186 | 44.5767 | +0.0419 | -15.2370 | -18.5136 | +3.2766 | 316 |
| [NSE:SPORTKING](https://in.tradingview.com/chart/?symbol=NSE:SPORTKING&interval=W) | 220.34 | +8.82 | 9.6552 | 9.5648 | +0.0904 | 21.1250 | 15.6153 | +5.5097 | 222 |
| [NSE:STEL](https://in.tradingview.com/chart/?symbol=NSE:STEL&interval=W) | 620.20 | -6.60 | 27.4969 | 27.2744 | +0.2224 | 15.9643 | 8.4504 | +7.5139 | 316 |
| [NSE:STYLAMIND](https://in.tradingview.com/chart/?symbol=NSE:STYLAMIND&interval=W) | 3229.80 | -0.16 | 153.8676 | 153.7766 | +0.0911 | -3.0255 | -4.7892 | +1.7637 | 277 |
| [NSE:SUDARSCHEM](https://in.tradingview.com/chart/?symbol=NSE:SUDARSCHEM&interval=W) | 1155.75 | -0.16 | 53.5208 | 53.3343 | +0.1865 | 16.1147 | 14.5630 | +1.5517 | 316 |
| [NSE:SUNTECK](https://in.tradingview.com/chart/?symbol=NSE:SUNTECK&interval=W) | 310.90 | +0.06 | 14.5426 | 14.5070 | +0.0356 | -21.5411 | -32.2977 | +10.7566 | 316 |
| [NSE:SUNTV](https://in.tradingview.com/chart/?symbol=NSE:SUNTV&interval=W) | 659.70 | +2.01 | 27.6797 | 27.2862 | +0.3934 | 27.5173 | 22.0954 | +5.4219 | 316 |
| [NSE:SURAKSHA](https://in.tradingview.com/chart/?symbol=NSE:SURAKSHA&interval=W) | 353.50 | +3.45 | 15.3595 | 15.2014 | +0.1581 | 29.3395 | 25.6222 | +3.7173 | 103 |
| [NSE:SURYODAY](https://in.tradingview.com/chart/?symbol=NSE:SURYODAY&interval=W) | 154.50 | -1.12 | 7.3651 | 7.3612 | +0.0039 | -16.0916 | -22.3839 | +6.2924 | 296 |
| [NSE:SYNGENE](https://in.tradingview.com/chart/?symbol=NSE:SYNGENE&interval=W) | 434.35 | -2.24 | 19.9089 | 19.8184 | +0.0906 | -7.1871 | -16.5511 | +9.3641 | 316 |
| [NSE:TALBROAUTO](https://in.tradingview.com/chart/?symbol=NSE:TALBROAUTO&interval=W) | 412.40 | +1.21 | 18.9557 | 18.8749 | +0.0807 | 10.1192 | 7.1704 | +2.9487 | 316 |
| [NSE:TANLA](https://in.tradingview.com/chart/?symbol=NSE:TANLA&interval=W) | 711.00 | -2.99 | 28.1547 | 27.5629 | +0.5918 | 38.1998 | 31.7771 | +6.4228 | 316 |
| [NSE:TASTYBITE](https://in.tradingview.com/chart/?symbol=NSE:TASTYBITE&interval=W) | 11299.50 | -1.24 | 468.1052 | 460.7662 | +7.3389 | 46.0327 | 38.6076 | +7.4251 | 316 |
| [NSE:TATACOMM](https://in.tradingview.com/chart/?symbol=NSE:TATACOMM&interval=W) | 1802.20 | +1.65 | 84.2989 | 84.0922 | +0.2066 | -1.9428 | -13.5050 | +11.5622 | 316 |
| [NSE:TCPLPACK](https://in.tradingview.com/chart/?symbol=NSE:TCPLPACK&interval=W) | 4562.80 | +1.81 | 189.8283 | 186.9453 | +2.8830 | 59.3674 | 58.2040 | +1.1634 | 316 |
| [NSE:THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA&interval=W) | 676.30 | +1.49 | 27.8519 | 27.3962 | +0.4558 | 72.9585 | 72.4930 | +0.4655 | 77 |
| [NSE:THOMASCOOK](https://in.tradingview.com/chart/?symbol=NSE:THOMASCOOK&interval=W) | 115.03 | +4.70 | 5.0314 | 4.9833 | +0.0481 | -10.2420 | -22.6366 | +12.3947 | 316 |
| [NSE:TI](https://in.tradingview.com/chart/?symbol=NSE:TI&interval=W) | 525.50 | +1.38 | 24.7338 | 24.6889 | +0.0449 | 15.1619 | 14.0371 | +1.1248 | 316 |
| [NSE:TIIL](https://in.tradingview.com/chart/?symbol=NSE:TIIL&interval=W) | 2854.60 | -1.14 | 134.6069 | 134.3878 | +0.2191 | 14.3546 | 11.3303 | +3.0244 | 316 |
| [NSE:TIMETECHNO](https://in.tradingview.com/chart/?symbol=NSE:TIMETECHNO&interval=W) | 192.73 | +1.60 | 8.8301 | 8.7895 | +0.0406 | -13.8104 | -23.6517 | +9.8413 | 316 |
| [NSE:TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC&interval=W) | 833.15 | +2.05 | 34.4557 | 33.9086 | +0.5471 | 54.5645 | 50.3842 | +4.1804 | 316 |
| [NSE:TMB](https://in.tradingview.com/chart/?symbol=NSE:TMB&interval=W) | 896.55 | +0.73 | 40.5667 | 40.3269 | +0.2398 | 24.7521 | 19.6928 | +5.0594 | 219 |
| [NSE:TTKHLTCARE](https://in.tradingview.com/chart/?symbol=NSE:TTKHLTCARE&interval=W) | 1096.75 | +16.87 | 48.7166 | 48.3324 | +0.3842 | -5.1927 | -10.7878 | +5.5951 | 316 |
| [NSE:TVSSCS](https://in.tradingview.com/chart/?symbol=NSE:TVSSCS&interval=W) | 137.01 | +12.07 | 6.0430 | 5.9907 | +0.0523 | -14.8141 | -30.1344 | +15.3203 | 170 |
| [NSE:TVSSRICHAK](https://in.tradingview.com/chart/?symbol=NSE:TVSSRICHAK&interval=W) | 4576.20 | +5.55 | 212.1539 | 211.4393 | +0.7147 | 10.6501 | 4.3050 | +6.3450 | 316 |
| [NSE:UDS](https://in.tradingview.com/chart/?symbol=NSE:UDS&interval=W) | 221.10 | +1.81 | 9.9123 | 9.8440 | +0.0683 | 32.9255 | 26.5137 | +6.4119 | 164 |
| [NSE:UFLEX](https://in.tradingview.com/chart/?symbol=NSE:UFLEX&interval=W) | 630.50 | +1.97 | 27.9113 | 27.6809 | +0.2304 | 35.6803 | 33.5686 | +2.1117 | 316 |
| [NSE:UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH&interval=W) | 1876.10 | -3.18 | 76.1236 | 74.7453 | +1.3783 | 62.1435 | 60.4318 | +1.7117 | 99 |
| [NSE:UNOMINDA](https://in.tradingview.com/chart/?symbol=NSE:UNOMINDA&interval=W) | 1388.10 | +0.01 | 58.6542 | 57.8676 | +0.7866 | 19.4740 | 11.1145 | +8.3595 | 316 |
| [NSE:UTTAMSUGAR](https://in.tradingview.com/chart/?symbol=NSE:UTTAMSUGAR&interval=W) | 365.05 | -2.58 | 14.9152 | 14.6573 | +0.2579 | 59.2997 | 58.7118 | +0.5879 | 316 |
| [NSE:VARROC](https://in.tradingview.com/chart/?symbol=NSE:VARROC&interval=W) | 835.90 | -0.33 | 37.3614 | 37.0918 | +0.2697 | 35.9026 | 33.1461 | +2.7565 | 316 |
| [NSE:VIJAYA](https://in.tradingview.com/chart/?symbol=NSE:VIJAYA&interval=W) | 1467.40 | +4.06 | 68.1908 | 67.9778 | +0.2130 | 21.5587 | 20.4437 | +1.1150 | 271 |
| [NSE:VMART](https://in.tradingview.com/chart/?symbol=NSE:VMART&interval=W) | 790.55 | +2.33 | 37.2288 | 37.1632 | +0.0656 | 4.4632 | 2.3337 | +2.1295 | 316 |
| [NSE:VRLLOG](https://in.tradingview.com/chart/?symbol=NSE:VRLLOG&interval=W) | 339.10 | -0.29 | 13.9354 | 13.7039 | +0.2315 | 36.5494 | 28.6247 | +7.9248 | 316 |
| [NSE:VSSL](https://in.tradingview.com/chart/?symbol=NSE:VSSL&interval=W) | 380.70 | +0.78 | 16.9529 | 16.8238 | +0.1291 | 36.9577 | 35.2952 | +1.6625 | 316 |
| [NSE:WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV&interval=W) | 265.62 | +6.19 | 10.1399 | 9.8810 | +0.2589 | 70.3301 | 68.6363 | +1.6937 | 316 |
| [NSE:WESTLIFE](https://in.tradingview.com/chart/?symbol=NSE:WESTLIFE&interval=W) | 671.70 | +1.92 | 28.1141 | 27.7066 | +0.4075 | 62.4833 | 59.1520 | +3.3312 | 316 |
| [NSE:WOCKPHARMA](https://in.tradingview.com/chart/?symbol=NSE:WOCKPHARMA&interval=W) | 2008.90 | -0.90 | 94.3989 | 94.2117 | +0.1872 | 18.1295 | 17.4633 | +0.6662 | 316 |
| [NSE:WONDERLA](https://in.tradingview.com/chart/?symbol=NSE:WONDERLA&interval=W) | 516.05 | -0.52 | 24.4300 | 24.4000 | +0.0300 | -5.8463 | -13.6644 | +7.8181 | 316 |
| [NSE:XPROINDIA](https://in.tradingview.com/chart/?symbol=NSE:XPROINDIA&interval=W) | 1277.10 | +7.31 | 56.3623 | 55.8784 | +0.4839 | -9.6204 | -19.1440 | +9.5235 | 316 |
| [NSE:YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH&interval=W) | 1109.55 | +4.59 | 46.8997 | 46.2725 | +0.6272 | 51.3373 | 47.1146 | +4.2227 | 172 |
| [NSE:ZENSARTECH](https://in.tradingview.com/chart/?symbol=NSE:ZENSARTECH&interval=W) | 528.00 | -3.92 | 24.5507 | 24.4755 | +0.0752 | 8.2386 | 4.4725 | +3.7661 | 316 |
| [NSE:ZENTEC](https://in.tradingview.com/chart/?symbol=NSE:ZENTEC&interval=W) | 1719.60 | -1.38 | 81.4889 | 81.3972 | +0.0918 | -2.7784 | -6.9809 | +4.2025 | 316 |
| [NSE:ZOTA](https://in.tradingview.com/chart/?symbol=NSE:ZOTA&interval=W) | 1290.60 | -0.50 | 61.5934 | 61.5679 | +0.0255 | 9.1205 | 6.7481 | +2.3724 | 316 |

## Excluded data

- 3BBLACKBIO: missing sessions or benchmark history mismatch
- AARTIPHARM: missing sessions or benchmark history mismatch
- ABB: missing latest benchmark session
- ABCAPITAL: missing latest benchmark session
- ACCENTMIC: missing OHLC history
- ACGL: missing sessions or benchmark history mismatch
- ADANIENSOL: missing latest benchmark session
- ADANIENT: missing latest benchmark session
- ADANIGREEN: missing latest benchmark session
- ADANIPORTS: missing latest benchmark session
- ADANIPOWER: missing latest benchmark session
- ADVAIT: missing sessions or benchmark history mismatch
- AEQUS: missing sessions or benchmark history mismatch
- AEROPLANE: missing sessions or benchmark history mismatch
- AIMTRON: missing OHLC history
- AKCAPIT: missing sessions or benchmark history mismatch
- ALGOQUANT: missing sessions or benchmark history mismatch
- ALIVUS: missing sessions or benchmark history mismatch
- ALLTIME: missing sessions or benchmark history mismatch
- ALPEXSOLAR: missing OHLC history
- AMAGI: missing sessions or benchmark history mismatch
- AMBUJACEM: missing sessions or benchmark history mismatch
- ANANTAM: missing OHLC history
- ANONDITA: missing OHLC history
- ANZEN: missing OHLC history
- AONESTEELS: missing sessions or benchmark history mismatch
- APOLLOHOSP: missing latest benchmark session
- ARCIL: missing sessions or benchmark history mismatch
- ARIHANTCAP: missing sessions or benchmark history mismatch
- ARROWGREEN: inconsistent OHLC prices
- ARSSBL: missing sessions or benchmark history mismatch
- ARYAMAN: missing sessions or benchmark history mismatch
- ASHIKAG: missing sessions or benchmark history mismatch
- ASIANENE: missing sessions or benchmark history mismatch
- ASIANPAINT: missing latest benchmark session
- ASTAR: missing sessions or benchmark history mismatch
- ATLANTAELE: missing sessions or benchmark history mismatch
- AUGMONT: missing sessions or benchmark history mismatch
- AUROPHARMA: missing latest benchmark session
- AVADHSUGAR: missing sessions or benchmark history mismatch
- AWL: missing sessions or benchmark history mismatch
- AXISBANK: missing latest benchmark session
- AYE: missing sessions or benchmark history mismatch
- BAFNAPH: missing OHLC history
- BAGMANE.RR: missing OHLC history
- BAJAJFINSV: missing latest benchmark session
- BAJAJHCARE: missing sessions or benchmark history mismatch
- BAJAJHLDNG: missing latest benchmark session
- BAJAJ_AUTO: missing OHLC history
- BANKBARODA: missing latest benchmark session
- BANKINDIA: inconsistent OHLC prices
- BEL: missing latest benchmark session
- BELDING: missing sessions or benchmark history mismatch
- BENARAS: missing sessions or benchmark history mismatch
- BENGALASM: missing sessions or benchmark history mismatch
- BETA: missing sessions or benchmark history mismatch
- BGRENERGY: missing OHLC history
- BHAGERIA: missing sessions or benchmark history mismatch
- BHARATFORG: missing sessions or benchmark history mismatch
- BHEL: missing latest benchmark session
- BIRET.RR: missing OHLC history
- BLEL: missing sessions or benchmark history mismatch
- BLIL: missing sessions or benchmark history mismatch
- BLISSGVS: missing latest benchmark session
- BLSPOLY: insufficient history: need 22 weekly bars
- BLUESTONE: missing sessions or benchmark history mismatch
- BODALCHEM: missing latest benchmark session
- BONDADA: insufficient history: need 22 weekly bars
- BONFIG: insufficient history: need 22 weekly bars
- BOSCHLTD: missing latest benchmark session
- BOSCH_HCIL: missing OHLC history
- BPCL: missing latest benchmark session
- BPLPHARMA: missing sessions or benchmark history mismatch
- BRITANNIA: missing latest benchmark session
- BSE: missing latest benchmark session
- BUILDPRO: missing sessions or benchmark history mismatch
- CANBK: missing latest benchmark session
- CANHLIFE: missing sessions or benchmark history mismatch
- CAPILLARY: missing sessions or benchmark history mismatch
- CAPINVIT: missing OHLC history
- CCAVENUE: missing sessions or benchmark history mismatch
- CEINSYS: missing sessions or benchmark history mismatch
- CGPOWER: missing latest benchmark session
- CHOLAFIN: missing latest benchmark session
- CIPLA: missing latest benchmark session
- CLEANMAX: missing sessions or benchmark history mismatch
- CMLL: missing sessions or benchmark history mismatch
- CMPDI: missing sessions or benchmark history mismatch
- CMRGREEN: missing sessions or benchmark history mismatch
- COALINDIA: missing latest benchmark session
- COCKERILL: missing sessions or benchmark history mismatch
- COMSYN: missing sessions or benchmark history mismatch
- CONSOFINVT: missing sessions or benchmark history mismatch
- CORDELIA: missing sessions or benchmark history mismatch
- CORONA: missing sessions or benchmark history mismatch
- CPPLUS: missing sessions or benchmark history mismatch
- CRAMC: missing sessions or benchmark history mismatch
- CUBEINVIT: missing OHLC history
- CUMMINSIND: missing latest benchmark session
- DANISH: missing OHLC history
- DBREALTY: missing sessions or benchmark history mismatch
- DECNGOLD: missing sessions or benchmark history mismatch
- DEEDEV: missing sessions or benchmark history mismatch
- DEEPA: missing sessions or benchmark history mismatch
- DHOOTTRANS: missing sessions or benchmark history mismatch
- DIACABS: missing sessions or benchmark history mismatch
- DISAQ: missing sessions or benchmark history mismatch
- DIVISLAB: missing latest benchmark session
- DLF: missing latest benchmark session
- DMART: missing latest benchmark session
- DOLPHIN: missing sessions or benchmark history mismatch
- DPABHUSHAN: missing latest benchmark session
- DPEL: missing OHLC history
- DRAGARWQ: missing sessions or benchmark history mismatch
- DRREDDY: missing latest benchmark session
- E2E: missing sessions or benchmark history mismatch
- EDELALTS: insufficient history: need 22 weekly bars
- EFCIL: missing sessions or benchmark history mismatch
- EICHERMOT: missing latest benchmark session
- ELANTAS: missing sessions or benchmark history mismatch
- ELEVATE: missing sessions or benchmark history mismatch
- ELPROINTL: missing sessions or benchmark history mismatch
- EMBASSY.RR: missing OHLC history
- EMBDL: missing sessions or benchmark history mismatch
- EMIL: missing sessions or benchmark history mismatch
- EMMVEE: missing sessions or benchmark history mismatch
- ENRIN: missing latest benchmark session
- EPACKPEB: missing sessions or benchmark history mismatch
- ESDS: missing sessions or benchmark history mismatch
- ETERNAL: missing latest benchmark session
- EUROPRATIK: missing sessions or benchmark history mismatch
- EVONILE: missing sessions or benchmark history mismatch
- FEDDERSHOL: missing sessions or benchmark history mismatch
- FERMENTA: missing sessions or benchmark history mismatch
- FLYSBS: missing OHLC history
- FORCEMOT: missing sessions or benchmark history mismatch
- FRACTAL: missing sessions or benchmark history mismatch
- FREDUN: missing sessions or benchmark history mismatch
- FRONTSP: missing sessions or benchmark history mismatch
- FUSION: missing sessions or benchmark history mismatch
- FUSIONCX: insufficient history: need 22 weekly bars
- GAIL: missing latest benchmark session
- GAJA: missing sessions or benchmark history mismatch
- GCSL: missing sessions or benchmark history mismatch
- GKENERGY: missing sessions or benchmark history mismatch
- GKSL: missing sessions or benchmark history mismatch
- GLASSWALL: missing sessions or benchmark history mismatch
- GLAXO: inconsistent OHLC prices
- GMRAIRPORT: missing latest benchmark session
- GODREJCP: missing sessions or benchmark history mismatch
- GOODYEAR: missing sessions or benchmark history mismatch
- GRASIM: missing latest benchmark session
- GRAUWEIL: missing sessions or benchmark history mismatch
- GROWW: missing latest benchmark session
- GSPCROP: missing sessions or benchmark history mismatch
- GSPLTRANS: missing sessions or benchmark history mismatch
- GUJENERGY: missing sessions or benchmark history mismatch
- GVT&D: missing latest benchmark session
- GYFTR: missing sessions or benchmark history mismatch
- HAL: missing latest benchmark session
- HAWKINCOOK: missing sessions or benchmark history mismatch
- HCLTECH: missing latest benchmark session
- HDFCAMC: missing latest benchmark session
- HDFCLIFE: missing latest benchmark session
- HDFIRE: insufficient history: need 22 weekly bars
- HEGAM: missing sessions or benchmark history mismatch
- HEROMOTOCO: missing latest benchmark session
- HEROMOTORS: missing sessions or benchmark history mismatch
- HFCL: missing latest benchmark session
- HINDALCO: missing latest benchmark session
- HINDUNILVR: missing latest benchmark session
- HINDZINC: missing latest benchmark session
- HMT: missing OHLC history
- HOMEFIRST: missing sessions or benchmark history mismatch
- HYUNDAI: missing latest benchmark session
- ICICIAMC: missing latest benchmark session
- ICICILIFE: missing sessions or benchmark history mismatch
- IDEAFORGE: missing sessions or benchmark history mismatch
- INA: missing sessions or benchmark history mismatch
- INDHOTEL: missing latest benchmark session
- INDIAGLYCO: missing sessions or benchmark history mismatch
- INDIANB: missing latest benchmark session
- INDIGO: missing latest benchmark session
- INDIGOPNTS: missing sessions or benchmark history mismatch
- INDIGRID: missing OHLC history
- INDOKEM: missing sessions or benchmark history mismatch
- INDOMIM: missing sessions or benchmark history mismatch
- INDOTECH: missing sessions or benchmark history mismatch
- INDPRUD: missing sessions or benchmark history mismatch
- INDUSINVIT: missing OHLC history
- INDUSTOWER: missing latest benchmark session
- INFY: missing latest benchmark session
- INVPRECQ: missing sessions or benchmark history mismatch
- IOC: missing latest benchmark session
- IRFC: missing latest benchmark session
- IRISDOREME: missing sessions or benchmark history mismatch
- ITC: missing latest benchmark session
- IVALUE: missing sessions or benchmark history mismatch
- JAIBALAJI: missing sessions or benchmark history mismatch
- JAINREC: missing sessions or benchmark history mismatch
- JAYKAY: missing sessions or benchmark history mismatch
- JAYKAYPP.E1: missing OHLC history
- JINDALSTEL: missing latest benchmark session
- JIOFIN: missing latest benchmark session
- JKPAPER: inconsistent OHLC prices
- JNPR: missing sessions or benchmark history mismatch
- JSLL: missing sessions or benchmark history mismatch
- JSWCEMENT: missing sessions or benchmark history mismatch
- JSWENERGY: missing sessions or benchmark history mismatch
- JSWSTEEL: missing latest benchmark session
- JYOTIRES: missing sessions or benchmark history mismatch
- KABRAEXTRU: missing latest benchmark session
- KAMAHOLD: missing sessions or benchmark history mismatch
- KANOHAR: missing sessions or benchmark history mismatch
- KAPSTON: missing sessions or benchmark history mismatch
- KARAMTARA: missing sessions or benchmark history mismatch
- KENNAMET: missing sessions or benchmark history mismatch
- KHAZANCHI: insufficient history: need 22 weekly bars
- KICL: missing latest benchmark session
- KIRLFER: missing sessions or benchmark history mismatch
- KISSHT: missing sessions or benchmark history mismatch
- KLBRENG_B: missing OHLC history
- KMCSHIL: missing sessions or benchmark history mismatch
- KNACK: missing sessions or benchmark history mismatch
- KODYTECH: missing OHLC history
- KOPRAN: missing sessions or benchmark history mismatch
- KOTAKBANK: missing latest benchmark session
- KOTIC: missing sessions or benchmark history mismatch
- KOVAI: missing sessions or benchmark history mismatch
- KPL: missing sessions or benchmark history mismatch
- KRISHNADEF: missing sessions or benchmark history mismatch
- KRN: missing sessions or benchmark history mismatch
- KRT.RR: missing OHLC history
- KSHINTL: missing sessions or benchmark history mismatch
- KUSUMGAR: missing sessions or benchmark history mismatch
- LALITHAA: missing sessions or benchmark history mismatch
- LASERPOWER: missing sessions or benchmark history mismatch
- LATENTVIEW: missing sessions or benchmark history mismatch
- LAURUSLABS: missing latest benchmark session
- LCCPROJECT: missing sessions or benchmark history mismatch
- LCL: missing sessions or benchmark history mismatch
- LEAPIND: missing sessions or benchmark history mismatch
- LENSKART: missing latest benchmark session
- LGEINDIA: missing latest benchmark session
- LGHL: missing latest benchmark session
- LLOYDSME: missing sessions or benchmark history mismatch
- LODHA: missing latest benchmark session
- LOTUSDEV: missing sessions or benchmark history mismatch
- LTM: missing latest benchmark session
- LUMINO: missing sessions or benchmark history mismatch
- LUPIN: missing sessions or benchmark history mismatch
- M&M: missing latest benchmark session
- MAHASTEEL: missing latest benchmark session
- MAHSCOOTER: missing sessions or benchmark history mismatch
- MANIPALHOS: missing sessions or benchmark history mismatch
- MANKIND: missing latest benchmark session
- MARICO: missing latest benchmark session
- MARINE: missing sessions or benchmark history mismatch
- MARSONS: missing sessions or benchmark history mismatch
- MARUTI: missing latest benchmark session
- MAXHEALTH: missing sessions or benchmark history mismatch
- MAZDOCK: missing sessions or benchmark history mismatch
- MBAPL: missing sessions or benchmark history mismatch
- MBECL: missing OHLC history
- MBEL: missing sessions or benchmark history mismatch
- MEDANTA: missing sessions or benchmark history mismatch
- MEESHO: missing latest benchmark session
- MENONBE: missing sessions or benchmark history mismatch
- MIDWESTLTD: missing latest benchmark session
- MIIL: missing sessions or benchmark history mismatch
- MILKYMIST: missing latest benchmark session
- MINDSPACE.RR: missing OHLC history
- MKJEWELS: insufficient history: need 22 weekly bars
- MMP: missing sessions or benchmark history mismatch
- MODISONLTD: missing latest benchmark session
- MOLBIO: missing sessions or benchmark history mismatch
- MONEYVIEW: missing sessions or benchmark history mismatch
- MONOLITH: missing OHLC history
- MOREPENLAB: missing latest benchmark session
- MOTHERSON: missing latest benchmark session
- MPIMANIPAL: missing sessions or benchmark history mismatch
- MTARTECH: missing sessions or benchmark history mismatch
- MUTHOOTFIN: missing latest benchmark session
- MVELECTRO: missing sessions or benchmark history mismatch
- NAM_INDIA: missing OHLC history
- NDRAUTO: missing sessions or benchmark history mismatch
- NEPHROPLUS: missing sessions or benchmark history mismatch
- NESTLEIND: missing latest benchmark session
- NHIT: missing OHLC history
- NINSYS: missing sessions or benchmark history mismatch
- NIRLON: missing sessions or benchmark history mismatch
- NITTAGELA: missing sessions or benchmark history mismatch
- NPST: missing sessions or benchmark history mismatch
- NRAIL: missing sessions or benchmark history mismatch
- NRL: missing sessions or benchmark history mismatch
- NSIL: missing latest benchmark session
- NTPC: missing latest benchmark session
- NXST.RR: missing OHLC history
- NYKAA: missing latest benchmark session
- OBSCP: missing OHLC history
- OFSS: missing sessions or benchmark history mismatch
- OMNI: missing latest benchmark session
- ONGC: missing latest benchmark session
- ORIANA: missing OHLC history
- ORIENTCABL: missing sessions or benchmark history mismatch
- ORKLAINDIA: missing sessions or benchmark history mismatch
- PACEDIGITK: missing sessions or benchmark history mismatch
- PANORAMA: missing sessions or benchmark history mismatch
- PARASHLTH: insufficient history: need 22 weekly bars
- PARKHOSPS: missing sessions or benchmark history mismatch
- PAUSHAKLTD: missing sessions or benchmark history mismatch
- PAYTM: missing latest benchmark session
- PERMAGN: missing sessions or benchmark history mismatch
- PERNIASPOP: missing sessions or benchmark history mismatch
- PFC: missing latest benchmark session
- PFOCUS: missing sessions or benchmark history mismatch
- PIDILITIND: missing latest benchmark session
- PILANIINVS: missing latest benchmark session
- PINELABS: missing sessions or benchmark history mismatch
- PIRAMALFIN: missing sessions or benchmark history mismatch
- PIXTRANS: missing sessions or benchmark history mismatch
- PNB: missing latest benchmark session
- PNGSREVA: missing sessions or benchmark history mismatch
- POCL: missing sessions or benchmark history mismatch
- POLYCAB: missing latest benchmark session
- POWERGRID: missing latest benchmark session
- POWERICA: missing sessions or benchmark history mismatch
- POWERINDIA: missing latest benchmark session
- PRADPME: missing sessions or benchmark history mismatch
- PRASOLCHEM: missing sessions or benchmark history mismatch
- PRIZOR: missing OHLC history
- PWL: missing sessions or benchmark history mismatch
- QLINE: missing OHLC history
- QPOWER: missing sessions or benchmark history mismatch
- RAINBOW: missing sessions or benchmark history mismatch
- RAJOOENG: missing sessions or benchmark history mismatch
- RAMBHAJO: missing latest benchmark session
- RELINFRA: missing OHLC history
- RENTOMOJO: missing sessions or benchmark history mismatch
- RIR: missing sessions or benchmark history mismatch
- RISHABH: inconsistent OHLC prices
- ROTO: missing sessions or benchmark history mismatch
- RSL: missing sessions or benchmark history mismatch
- RUBICON: missing sessions or benchmark history mismatch
- RUBYMILLS: missing sessions or benchmark history mismatch
- RUNWALENTR: missing sessions or benchmark history mismatch
- SAATVIKGL: missing sessions or benchmark history mismatch
- SAHANA: missing OHLC history
- SAIPARENT: missing sessions or benchmark history mismatch
- SALSTEEL: missing sessions or benchmark history mismatch
- SBIFUNDS: missing latest benchmark session
- SBILIFE: missing latest benchmark session
- SEDEMAC: missing sessions or benchmark history mismatch
- SEIL: missing sessions or benchmark history mismatch
- SEITINVIT: missing OHLC history
- SFCTECH: insufficient history: need 22 weekly bars
- SGFIN: missing sessions or benchmark history mismatch
- SGMART: missing sessions or benchmark history mismatch
- SHADOWFAX: missing sessions or benchmark history mismatch
- SHANKESH: missing sessions or benchmark history mismatch
- SHILCTECH: missing sessions or benchmark history mismatch
- SHIPROCKET: missing sessions or benchmark history mismatch
- SHREEJISPG: missing sessions or benchmark history mismatch
- SHREMINVIT: missing OHLC history
- SHRINGARMS: missing sessions or benchmark history mismatch
- SHRIPISTON: missing sessions or benchmark history mismatch
- SHRIRAMFIN: missing latest benchmark session
- SHUKRAPHAR: missing sessions or benchmark history mismatch
- SIEMENS: missing latest benchmark session
- SIGMAADV: missing latest benchmark session
- SIKA: missing sessions or benchmark history mismatch
- SILVERTUC: missing sessions or benchmark history mismatch
- SKFINDUS: missing sessions or benchmark history mismatch
- SKYWAYS: missing sessions or benchmark history mismatch
- SMT: insufficient history: need 22 weekly bars
- SOLARINDS: missing latest benchmark session
- SPECTRUM: missing sessions or benchmark history mismatch
- SPMLINFRA: missing sessions or benchmark history mismatch
- SSRETAIL: missing sessions or benchmark history mismatch
- STALLION: missing sessions or benchmark history mismatch
- STARHEALTH: missing sessions or benchmark history mismatch
- STEAMHOUSE: missing sessions or benchmark history mismatch
- STLTECH: missing latest benchmark session
- STUDDS: missing sessions or benchmark history mismatch
- STYL: missing sessions or benchmark history mismatch
- STYLEBAAZA: missing sessions or benchmark history mismatch
- SUDEEPPHRM: missing sessions or benchmark history mismatch
- SUNPHARMA: missing latest benchmark session
- SUNRAKSHAK: missing sessions or benchmark history mismatch
- SUNSHINE: missing sessions or benchmark history mismatch
- SWANDEF: missing OHLC history
- SYMBIOTEC: missing sessions or benchmark history mismatch
- SYSTMTXC: missing sessions or benchmark history mismatch
- TAALTECH: missing sessions or benchmark history mismatch
- TARC: missing sessions or benchmark history mismatch
- TATACAP: missing latest benchmark session
- TATACONSUM: missing latest benchmark session
- TATAPOWER: missing latest benchmark session
- TATASTEEL: missing latest benchmark session
- TBZ: missing latest benchmark session
- TECHM: missing latest benchmark session
- TECHNOCRAF: missing sessions or benchmark history mismatch
- TECHNVISN: missing sessions or benchmark history mismatch
- TEMBO: missing sessions or benchmark history mismatch
- TEMPSENS: missing sessions or benchmark history mismatch
- TENNIND: missing sessions or benchmark history mismatch
- TGVSL: missing sessions or benchmark history mismatch
- THEJO: missing sessions or benchmark history mismatch
- TIL: missing sessions or benchmark history mismatch
- TIMEX: missing sessions or benchmark history mismatch
- TITAN: missing latest benchmark session
- TMCV: missing latest benchmark session
- TMPV: missing sessions or benchmark history mismatch
- TONBO: insufficient history: need 22 weekly bars
- TORNTPHARM: missing latest benchmark session
- TRENT: missing latest benchmark session
- TRUALT: missing sessions or benchmark history mismatch
- TURTLEMINT: missing sessions or benchmark history mismatch
- TVSHLTD: missing sessions or benchmark history mismatch
- TVSMOTOR: missing latest benchmark session
- UEL: missing sessions or benchmark history mismatch
- UFBL: missing sessions or benchmark history mismatch
- UGROCAP: inconsistent OHLC prices
- ULTRACEMCO: missing latest benchmark session
- ULTRAMAR: missing sessions or benchmark history mismatch
- UNIONBANK: missing latest benchmark session
- UNITDSPR: missing latest benchmark session
- UNITEDPOLY: missing sessions or benchmark history mismatch
- URBANCO: missing sessions or benchmark history mismatch
- UTLSOLAR: missing sessions or benchmark history mismatch
- UTSSAV: missing OHLC history
- VAML: missing latest benchmark session
- VARMORA: missing sessions or benchmark history mismatch
- VBL: missing latest benchmark session
- VEDL: missing sessions or benchmark history mismatch
- VENUSREM: missing sessions or benchmark history mismatch
- VERTIS: missing OHLC history
- VHL: missing sessions or benchmark history mismatch
- VHLTD: missing OHLC history
- VIDYAWIRES: missing sessions or benchmark history mismatch
- VIKRAMSOLR: missing sessions or benchmark history mismatch
- VIKRAN: missing sessions or benchmark history mismatch
- VINYAS: missing OHLC history
- VMARCIND: missing OHLC history
- VOEPL: missing sessions or benchmark history mismatch
- WAKEFIT: missing sessions or benchmark history mismatch
- WALCHANNAG: missing sessions or benchmark history mismatch
- WEWORK: missing sessions or benchmark history mismatch
- WIPRO: missing latest benchmark session
- WPIL: missing sessions or benchmark history mismatch
- XTRANET: missing sessions or benchmark history mismatch
- ZETWERK: insufficient history: need 22 weekly bars
- ZSARACOM: missing sessions or benchmark history mismatch
- ZYDUSLIFE: missing latest benchmark session


---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
