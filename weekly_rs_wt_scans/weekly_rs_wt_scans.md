> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Weekly RS EMA21 + WT1 Uptrend — 2026-11-18

Price data: 2026-11-18. Current developing week included; signals can change before the week closes. NSE common equities; price > Rs50; market cap Rs1,000 crore to Rs5 lakh crore. Weekly RS = stock close / NIFTY MIDSML 400 close x 1000; EMA21 uses adjust=False. Weekly WT1 uses HLC3, EMA10 channel and EMA21 smoothing, matching the existing WaveTrend calculator. Both latest weekly values must be strictly greater than their previous weekly values. Minimum 22 weekly bars; all available history up to 1500 daily bars. Flat slopes do not qualify. No daily EMA200, 52-week-high, float, liquidity, WT1 zero-line or WT2 gate. No manual-list bypass. All qualifiers are shown.

Universe: 1453 | Evaluated: 998 | Qualified: 283 | Excluded: 455

[Weekly chart dashboard](../dashboard/weekly_rs_wt.html)

## TradingView watchlist

```text
###INDICES,NSE:NIFTYSMLCAP250,NSE:NIFTYMIDSML400,###COMMODITIES,MCX:GOLDM1!,MCX:SILVERM1!,MCX:COPPER1!,MCX:ALUMINIUM1!,###WEEKLY RS21 WT1 UP,NSE:360ONE,NSE:5PAISA,NSE:63MOONS,NSE:AARTIDRUGS,NSE:ABDL,NSE:ABREL,NSE:ACE,NSE:ACUTAAS,NSE:AEGISVOPAK,NSE:AEROENTER,NSE:AETHER,NSE:AFFLE,NSE:AGARWALEYE,NSE:AGIIL,NSE:AIIL,NSE:AJAXENGG,NSE:AJMERA,NSE:ALEMBICLTD,NSE:ALICON,NSE:ALLDIGI,NSE:ANANDRATHI,NSE:ANGELONE,NSE:ANTHEM,NSE:ANUP,NSE:ANURAS,NSE:APLAPOLLO,NSE:APLLTD,NSE:APOLLO,NSE:APOLLOPIPE,NSE:ARIS,NSE:ARTEMISMED,NSE:ARVSMART,NSE:ASAHIINDIA,NSE:ASHOKA,NSE:ASHOKLEY,NSE:ASKAUTOLTD,NSE:ASTRAMICRO,NSE:ATHERENERG,NSE:AUTOAXLES,NSE:AVANTEL,NSE:AVTNPL,NSE:AWFIS,NSE:AYMSYNTEX,NSE:BALAJITELE,NSE:BALKRISIND,NSE:BALUFORGE,NSE:BANCOINDIA,NSE:BBL,NSE:BBOX,NSE:BECTORFOOD,NSE:BELRISE,NSE:BEML,NSE:BFINVEST,NSE:BHARTIHEXA,NSE:BLUESTARCO,NSE:BOROLTD,NSE:CANTABIL,NSE:CAPITALSFB,NSE:CDSL,NSE:CEATLTD,NSE:CEIGALL,NSE:CEMPRO,NSE:CENTUM,NSE:CHEMPLASTS,NSE:CNL,NSE:COHANCE,NSE:COROMANDEL,NSE:COSMOFIRST,NSE:CRAFTSMAN,NSE:CSBBANK,NSE:CUB,NSE:DALMIASUG,NSE:DAMCAPITAL,NSE:DCBBANK,NSE:DEEPAKFERT,NSE:DELHIVERY,NSE:DELTACORP,NSE:DIFFNKG,NSE:DSSL,NSE:DVL,NSE:DYNAMATECH,NSE:EDELWEISS,NSE:EIHOTEL,NSE:EIMCOELECO,NSE:EMAMILTD,NSE:EMCURE,NSE:ENGINERSIN,NSE:ENTERO,NSE:ERIS,NSE:ETHOSLTD,NSE:EUREKAFORB,NSE:EXCELINDUS,NSE:FAZE3Q,NSE:FDC,NSE:FEDERALBNK,NSE:FIEMIND,NSE:FILATEX,NSE:FINEORG,NSE:FLUOROCHEM,NSE:GABRIEL,NSE:GALAPREC,NSE:GESHIP,NSE:GHCL,NSE:GHCLTEXTIL,NSE:GLAND,NSE:GLENMARK,NSE:GODREJIND,NSE:GODREJPROP,NSE:GPPL,NSE:GRAPHITE,NSE:GREAVESCOT,NSE:GRWRHITECH,NSE:GULFOILLUB,NSE:HARIOMPIPE,NSE:HBLENGINE,NSE:HESTERBIO,NSE:HIKAL,NSE:HINDOILEXP,NSE:HINDPETRO,NSE:HLEGLAS,NSE:HONASA,NSE:ICIL,NSE:IDFCFIRSTB,NSE:IGIL,NSE:IIFL,NSE:IKIO,NSE:INDGN,NSE:INDIQUBE,NSE:INDOCO,NSE:INDRAMEDCO,NSE:INOXINDIA,NSE:IREDA,NSE:ISGEC,NSE:ITCHOTELS,NSE:ITDC,NSE:IXIGO,NSE:J&KBANK,NSE:JAMNAAUTO,NSE:JASH,NSE:JINDALPHOT,NSE:JSL,NSE:JYOTICNC,NSE:KALAMANDIR,NSE:KALYANKJIL,NSE:KANSAINER,NSE:KARURVYSYA,NSE:KDDL,NSE:KFINTECH,NSE:KIMS,NSE:KOLTEPATIL,NSE:KPRMILL,NSE:KRBL,NSE:KTKBANK,NSE:LALPATHLAB,NSE:LEMONTREE,NSE:LICHSGFIN,NSE:LINDEINDIA,NSE:LMW,NSE:LTFOODS,NSE:LTTS,NSE:LUMAXIND,NSE:LUMAXTECH,NSE:MAHABANK,NSE:MANAKCOAT,NSE:MARATHON,NSE:MAXESTATES,NSE:MCX,NSE:METROPOLIS,NSE:MGL,NSE:MINDACORP,NSE:MMFL,NSE:MOBIKWIK,NSE:MOTILALOFS,NSE:MRF,NSE:MRPL,NSE:MSTCLTD,NSE:MUFIN,NSE:NAVINFLUOR,NSE:NAZARA,NSE:NELCAST,NSE:NEOGEN,NSE:NEULANDLAB,NSE:NGLFINE,NSE:NH,NSE:NILKAMAL,NSE:NITINSPIN,NSE:NUVAMA,NSE:NUVOCO,NSE:OBEROIRLTY,NSE:ONESOURCE,NSE:OPTIEMUS,NSE:ORCHPHARMA,NSE:ORIENTELEC,NSE:ORIENTHOT,NSE:PARACABLES,NSE:PARAGMILK,NSE:PATANJALI,NSE:PDSL,NSE:PETRONET,NSE:PHOENIXLTD,NSE:PNBGILTS,NSE:PNBHOUSING,NSE:POLYMED,NSE:POONAWALLA,NSE:PPLPHARMA,NSE:PRESTIGE,NSE:PRIMESECU,NSE:PRINCEPIPE,NSE:PRIVISCL,NSE:PROTEAN,NSE:PVRINOX,NSE:QUESS,NSE:RACLGEAR,NSE:RADICO,NSE:RAMKY,NSE:RAYMONDREL,NSE:REPCOHOME,NSE:RKFORGE,NSE:ROLEXRINGS,NSE:ROSSTECH,NSE:RPEL,NSE:RPSGVENT,NSE:SAILIFE,NSE:SANATHAN,NSE:SANGAMIND,NSE:SANOFI,NSE:SANSERA,NSE:SAREGAMA,NSE:SASKEN,NSE:SATIN,NSE:SDBL,NSE:SHARDAMOTR,NSE:SHREECEM,NSE:SHYAMMETL,NSE:SIGNATURE,NSE:SIMPLEXINF,NSE:SMARTWORKS,NSE:SONACOMS,NSE:SOUTHBANK,NSE:SPAL,NSE:SPORTKING,NSE:STEL,NSE:STYLAMIND,NSE:SUDARSCHEM,NSE:SUNTECK,NSE:SUNTV,NSE:SURAKSHA,NSE:SURYODAY,NSE:SYNGENE,NSE:TALBROAUTO,NSE:TANLA,NSE:TASTYBITE,NSE:TATACOMM,NSE:TCPLPACK,NSE:THELEELA,NSE:THOMASCOOK,NSE:TI,NSE:TIIL,NSE:TIMETECHNO,NSE:TIPSMUSIC,NSE:TMB,NSE:TSFINV,NSE:TTKHLTCARE,NSE:TVSSCS,NSE:TVSSRICHAK,NSE:UDS,NSE:UFLEX,NSE:UNIMECH,NSE:UNOMINDA,NSE:VARROC,NSE:VIJAYA,NSE:VMART,NSE:VRLLOG,NSE:VSSL,NSE:WELSPUNLIV,NSE:WESTLIFE,NSE:WINDMACHIN,NSE:WOCKPHARMA,NSE:XPROINDIA,NSE:YATHARTH,NSE:ZENSARTECH,NSE:ZENTEC,NSE:ZOTA
```

## All qualifying stocks

| Symbol | Close | Week % | RS EMA21 | Previous | RS slope | WT1 | Previous WT1 | WT1 slope | Weeks |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [NSE:360ONE](https://in.tradingview.com/chart/?symbol=NSE:360ONE&interval=W) | 1211.05 | +2.91 | 53.7272 | 53.2426 | +0.4846 | 5.1181 | -5.0104 | +10.1285 | 315 |
| [NSE:5PAISA](https://in.tradingview.com/chart/?symbol=NSE:5PAISA&interval=W) | 343.30 | +1.24 | 16.4338 | 16.4167 | +0.0170 | -1.3487 | -4.8185 | +3.4698 | 315 |
| [NSE:63MOONS](https://in.tradingview.com/chart/?symbol=NSE:63MOONS&interval=W) | 927.00 | +0.38 | 40.7331 | 40.3230 | +0.4102 | 51.1039 | 50.0397 | +1.0643 | 315 |
| [NSE:AARTIDRUGS](https://in.tradingview.com/chart/?symbol=NSE:AARTIDRUGS&interval=W) | 505.75 | -0.32 | 20.8299 | 20.4668 | +0.3631 | 48.7322 | 41.2143 | +7.5179 | 315 |
| [NSE:ABDL](https://in.tradingview.com/chart/?symbol=NSE:ABDL&interval=W) | 798.05 | +5.33 | 32.7625 | 32.1790 | +0.5836 | 64.9874 | 57.9332 | +7.0542 | 125 |
| [NSE:ABREL](https://in.tradingview.com/chart/?symbol=NSE:ABREL&interval=W) | 1243.00 | +3.33 | 59.4187 | 59.3488 | +0.0700 | -34.4747 | -42.8662 | +8.3915 | 315 |
| [NSE:ACE](https://in.tradingview.com/chart/?symbol=NSE:ACE&interval=W) | 1189.20 | +0.78 | 53.5087 | 53.1079 | +0.4008 | 33.2438 | 31.4358 | +1.8080 | 315 |
| [NSE:ACUTAAS](https://in.tradingview.com/chart/?symbol=NSE:ACUTAAS&interval=W) | 3991.30 | -1.18 | 165.7455 | 163.0159 | +2.7296 | 53.3675 | 49.1029 | +4.2646 | 271 |
| [NSE:AEGISVOPAK](https://in.tradingview.com/chart/?symbol=NSE:AEGISVOPAK&interval=W) | 280.22 | -2.00 | 12.9206 | 12.8574 | +0.0632 | 9.8691 | 5.9719 | +3.8972 | 77 |
| [NSE:AEROENTER](https://in.tradingview.com/chart/?symbol=NSE:AEROENTER&interval=W) | 135.77 | +3.09 | 6.0545 | 6.0033 | +0.0512 | 19.1673 | 12.9382 | +6.2291 | 209 |
| [NSE:AETHER](https://in.tradingview.com/chart/?symbol=NSE:AETHER&interval=W) | 1647.20 | -1.79 | 75.1096 | 74.6538 | +0.4558 | 35.6940 | 34.4745 | +1.2195 | 234 |
| [NSE:AFFLE](https://in.tradingview.com/chart/?symbol=NSE:AFFLE&interval=W) | 1585.10 | -1.44 | 73.8541 | 73.5731 | +0.2810 | -3.0589 | -8.7231 | +5.6642 | 315 |
| [NSE:AGARWALEYE](https://in.tradingview.com/chart/?symbol=NSE:AGARWALEYE&interval=W) | 549.50 | -0.24 | 24.3228 | 24.0974 | +0.2254 | 31.9402 | 24.2269 | +7.7133 | 94 |
| [NSE:AGIIL](https://in.tradingview.com/chart/?symbol=NSE:AGIIL&interval=W) | 310.76 | -1.85 | 14.0769 | 13.9816 | +0.0953 | -22.5260 | -32.3214 | +9.7954 | 123 |
| [NSE:AIIL](https://in.tradingview.com/chart/?symbol=NSE:AIIL&interval=W) | 554.80 | -3.81 | 26.3797 | 26.3344 | +0.0453 | 17.6563 | 15.4698 | +2.1865 | 135 |
| [NSE:AJAXENGG](https://in.tradingview.com/chart/?symbol=NSE:AJAXENGG&interval=W) | 623.90 | +7.78 | 27.7142 | 27.4681 | +0.2461 | 12.5757 | -0.3281 | +12.9037 | 92 |
| [NSE:AJMERA](https://in.tradingview.com/chart/?symbol=NSE:AJMERA&interval=W) | 133.66 | +0.29 | 6.1692 | 6.1397 | +0.0295 | 19.2150 | 12.4369 | +6.7781 | 315 |
| [NSE:ALEMBICLTD](https://in.tradingview.com/chart/?symbol=NSE:ALEMBICLTD&interval=W) | 112.41 | -0.93 | 4.7829 | 4.7175 | +0.0654 | 26.3368 | 17.8091 | +8.5278 | 315 |
| [NSE:ALICON](https://in.tradingview.com/chart/?symbol=NSE:ALICON&interval=W) | 997.00 | +2.14 | 39.0676 | 38.1523 | +0.9153 | 59.3500 | 53.6813 | +5.6687 | 315 |
| [NSE:ALLDIGI](https://in.tradingview.com/chart/?symbol=NSE:ALLDIGI&interval=W) | 831.90 | -0.30 | 39.4218 | 39.3404 | +0.0813 | -3.4685 | -10.2741 | +6.8056 | 315 |
| [NSE:ANANDRATHI](https://in.tradingview.com/chart/?symbol=NSE:ANANDRATHI&interval=W) | 2375.10 | -0.26 | 112.0582 | 111.7768 | +0.2815 | 15.9529 | 10.1627 | +5.7902 | 258 |
| [NSE:ANGELONE](https://in.tradingview.com/chart/?symbol=NSE:ANGELONE&interval=W) | 338.30 | -3.07 | 14.9192 | 14.7749 | +0.1443 | 15.1662 | 4.7264 | +10.4398 | 315 |
| [NSE:ANTHEM](https://in.tradingview.com/chart/?symbol=NSE:ANTHEM&interval=W) | 914.35 | -2.41 | 41.6675 | 41.4120 | +0.2555 | 37.5126 | 35.5168 | +1.9959 | 70 |
| [NSE:ANUP](https://in.tradingview.com/chart/?symbol=NSE:ANUP&interval=W) | 1789.70 | +3.75 | 82.7777 | 82.3995 | +0.3782 | -35.8099 | -45.9134 | +10.1035 | 315 |
| [NSE:ANURAS](https://in.tradingview.com/chart/?symbol=NSE:ANURAS&interval=W) | 1321.10 | +1.58 | 59.5041 | 59.0649 | +0.4392 | -19.8694 | -35.4199 | +15.5505 | 296 |
| [NSE:APLAPOLLO](https://in.tradingview.com/chart/?symbol=NSE:APLAPOLLO&interval=W) | 2161.20 | -4.01 | 102.2577 | 102.0307 | +0.2270 | 36.0766 | 34.1323 | +1.9443 | 315 |
| [NSE:APLLTD](https://in.tradingview.com/chart/?symbol=NSE:APLLTD&interval=W) | 1044.35 | +1.38 | 41.7247 | 40.8461 | +0.8786 | 41.7443 | 33.1276 | +8.6166 | 315 |
| [NSE:APOLLO](https://in.tradingview.com/chart/?symbol=NSE:APOLLO&interval=W) | 447.50 | -5.91 | 19.4013 | 19.1771 | +0.2242 | 52.5283 | 46.0420 | +6.4864 | 315 |
| [NSE:APOLLOPIPE](https://in.tradingview.com/chart/?symbol=NSE:APOLLOPIPE&interval=W) | 547.35 | +9.51 | 24.9673 | 24.8168 | +0.1506 | 4.4826 | 0.6330 | +3.8496 | 315 |
| [NSE:ARIS](https://in.tradingview.com/chart/?symbol=NSE:ARIS&interval=W) | 146.12 | -0.50 | 6.6175 | 6.5725 | +0.0450 | 43.7629 | 40.3595 | +3.4034 | 74 |
| [NSE:ARTEMISMED](https://in.tradingview.com/chart/?symbol=NSE:ARTEMISMED&interval=W) | 343.40 | +6.71 | 15.0027 | 14.8421 | +0.1606 | 28.4930 | 23.3780 | +5.1149 | 315 |
| [NSE:ARVSMART](https://in.tradingview.com/chart/?symbol=NSE:ARVSMART&interval=W) | 633.55 | +2.10 | 29.4631 | 29.3453 | +0.1179 | 2.2116 | -6.2426 | +8.4543 | 315 |
| [NSE:ASAHIINDIA](https://in.tradingview.com/chart/?symbol=NSE:ASAHIINDIA&interval=W) | 1157.30 | +4.24 | 46.9960 | 46.0982 | +0.8977 | 50.5708 | 40.2782 | +10.2926 | 315 |
| [NSE:ASHOKA](https://in.tradingview.com/chart/?symbol=NSE:ASHOKA&interval=W) | 115.20 | +3.02 | 5.5000 | 5.4928 | +0.0072 | -42.2647 | -52.3499 | +10.0852 | 315 |
| [NSE:ASHOKLEY](https://in.tradingview.com/chart/?symbol=NSE:ASHOKLEY&interval=W) | 162.45 | -3.99 | 7.8229 | 7.8195 | +0.0034 | -8.2431 | -12.0282 | +3.7851 | 315 |
| [NSE:ASKAUTOLTD](https://in.tradingview.com/chart/?symbol=NSE:ASKAUTOLTD&interval=W) | 630.25 | -1.94 | 28.2704 | 28.0492 | +0.2212 | 36.6657 | 34.8192 | +1.8465 | 158 |
| [NSE:ASTRAMICRO](https://in.tradingview.com/chart/?symbol=NSE:ASTRAMICRO&interval=W) | 1660.80 | -2.51 | 77.5068 | 77.2249 | +0.2819 | 5.6641 | 1.8377 | +3.8264 | 315 |
| [NSE:ATHERENERG](https://in.tradingview.com/chart/?symbol=NSE:ATHERENERG&interval=W) | 1901.10 | -2.26 | 73.1550 | 71.2758 | +1.8793 | 67.6675 | 64.2810 | +3.3865 | 81 |
| [NSE:AUTOAXLES](https://in.tradingview.com/chart/?symbol=NSE:AUTOAXLES&interval=W) | 1812.10 | -0.18 | 83.2556 | 82.8169 | +0.4387 | -23.0906 | -35.7954 | +12.7048 | 315 |
| [NSE:AVANTEL](https://in.tradingview.com/chart/?symbol=NSE:AVANTEL&interval=W) | 156.91 | -4.76 | 7.4624 | 7.4497 | +0.0127 | -25.7506 | -34.9611 | +9.2104 | 121 |
| [NSE:AVTNPL](https://in.tradingview.com/chart/?symbol=NSE:AVTNPL&interval=W) | 103.43 | +7.05 | 4.2615 | 4.1874 | +0.0741 | 63.3202 | 60.7077 | +2.6125 | 315 |
| [NSE:AWFIS](https://in.tradingview.com/chart/?symbol=NSE:AWFIS&interval=W) | 285.40 | -2.12 | 13.4177 | 13.3791 | +0.0386 | -25.8015 | -35.8420 | +10.0405 | 130 |
| [NSE:AYMSYNTEX](https://in.tradingview.com/chart/?symbol=NSE:AYMSYNTEX&interval=W) | 275.08 | +4.78 | 12.5033 | 12.4231 | +0.0801 | 27.7163 | 26.1855 | +1.5307 | 315 |
| [NSE:BALAJITELE](https://in.tradingview.com/chart/?symbol=NSE:BALAJITELE&interval=W) | 95.42 | -7.17 | 4.4900 | 4.4775 | +0.0125 | 0.2299 | -7.5368 | +7.7667 | 315 |
| [NSE:BALKRISIND](https://in.tradingview.com/chart/?symbol=NSE:BALKRISIND&interval=W) | 2286.40 | +0.66 | 107.8266 | 107.5509 | +0.2756 | -4.8227 | -11.3429 | +6.5202 | 315 |
| [NSE:BALUFORGE](https://in.tradingview.com/chart/?symbol=NSE:BALUFORGE&interval=W) | 535.65 | -2.66 | 24.2825 | 24.1200 | +0.1624 | 1.9316 | -4.2058 | +6.1373 | 134 |
| [NSE:BANCOINDIA](https://in.tradingview.com/chart/?symbol=NSE:BANCOINDIA&interval=W) | 711.35 | +4.53 | 30.7307 | 30.3633 | +0.3674 | -2.1683 | -14.1321 | +11.9638 | 315 |
| [NSE:BBL](https://in.tradingview.com/chart/?symbol=NSE:BBL&interval=W) | 2578.80 | -5.29 | 119.0850 | 118.5210 | +0.5640 | -1.9727 | -9.9214 | +7.9487 | 315 |
| [NSE:BBOX](https://in.tradingview.com/chart/?symbol=NSE:BBOX&interval=W) | 880.00 | -2.30 | 39.9811 | 39.7231 | +0.2581 | 24.8065 | 19.5154 | +5.2911 | 315 |
| [NSE:BECTORFOOD](https://in.tradingview.com/chart/?symbol=NSE:BECTORFOOD&interval=W) | 216.89 | +2.46 | 10.1692 | 10.1372 | +0.0321 | -4.3097 | -10.3888 | +6.0791 | 309 |
| [NSE:BELRISE](https://in.tradingview.com/chart/?symbol=NSE:BELRISE&interval=W) | 234.48 | +8.96 | 10.9646 | 10.9270 | +0.0376 | -5.6871 | -11.4970 | +5.8098 | 78 |
| [NSE:BEML](https://in.tradingview.com/chart/?symbol=NSE:BEML&interval=W) | 2020.20 | -3.72 | 94.3226 | 93.9840 | +0.3385 | 39.7885 | 38.2001 | +1.5884 | 315 |
| [NSE:BFINVEST](https://in.tradingview.com/chart/?symbol=NSE:BFINVEST&interval=W) | 492.15 | +10.31 | 21.2114 | 20.9522 | +0.2592 | -17.8216 | -32.5782 | +14.7566 | 315 |
| [NSE:BHARTIHEXA](https://in.tradingview.com/chart/?symbol=NSE:BHARTIHEXA&interval=W) | 1666.30 | +0.05 | 77.3631 | 77.0403 | +0.3228 | 17.6923 | 13.0414 | +4.6509 | 137 |
| [NSE:BLUESTARCO](https://in.tradingview.com/chart/?symbol=NSE:BLUESTARCO&interval=W) | 1621.80 | +2.18 | 77.1890 | 77.0640 | +0.1250 | -1.0142 | -9.3659 | +8.3517 | 315 |
| [NSE:BOROLTD](https://in.tradingview.com/chart/?symbol=NSE:BOROLTD&interval=W) | 324.75 | +4.25 | 13.1841 | 12.9319 | +0.2523 | 61.7994 | 56.0667 | +5.7327 | 315 |
| [NSE:CANTABIL](https://in.tradingview.com/chart/?symbol=NSE:CANTABIL&interval=W) | 257.85 | -1.04 | 11.9978 | 11.9505 | +0.0473 | 28.4542 | 24.7985 | +3.6557 | 315 |
| [NSE:CAPITALSFB](https://in.tradingview.com/chart/?symbol=NSE:CAPITALSFB&interval=W) | 290.30 | +3.40 | 13.5216 | 13.4697 | +0.0519 | -13.0106 | -24.8598 | +11.8492 | 145 |
| [NSE:CDSL](https://in.tradingview.com/chart/?symbol=NSE:CDSL&interval=W) | 1416.60 | -2.10 | 64.7991 | 64.4275 | +0.3715 | 2.5415 | -7.6366 | +10.1780 | 315 |
| [NSE:CEATLTD](https://in.tradingview.com/chart/?symbol=NSE:CEATLTD&interval=W) | 3498.90 | -1.17 | 165.6584 | 165.3017 | +0.3568 | -15.2871 | -23.5733 | +8.2861 | 315 |
| [NSE:CEIGALL](https://in.tradingview.com/chart/?symbol=NSE:CEIGALL&interval=W) | 387.15 | -2.41 | 17.8530 | 17.7659 | +0.0872 | 42.7784 | 41.9069 | +0.8714 | 120 |
| [NSE:CEMPRO](https://in.tradingview.com/chart/?symbol=NSE:CEMPRO&interval=W) | 1354.40 | +3.01 | 59.5153 | 58.9162 | +0.5991 | 14.6490 | 8.3048 | +6.3442 | 315 |
| [NSE:CENTUM](https://in.tradingview.com/chart/?symbol=NSE:CENTUM&interval=W) | 4492.80 | +0.26 | 193.0868 | 190.6658 | +2.4210 | 47.3447 | 44.5892 | +2.7555 | 315 |
| [NSE:CHEMPLASTS](https://in.tradingview.com/chart/?symbol=NSE:CHEMPLASTS&interval=W) | 248.40 | +4.87 | 10.1552 | 9.9693 | +0.1859 | 13.6952 | 1.8816 | +11.8135 | 274 |
| [NSE:CNL](https://in.tradingview.com/chart/?symbol=NSE:CNL&interval=W) | 1382.30 | -5.22 | 54.1904 | 52.9239 | +1.2665 | 60.5702 | 56.8337 | +3.7365 | 315 |
| [NSE:COHANCE](https://in.tradingview.com/chart/?symbol=NSE:COHANCE&interval=W) | 456.40 | -0.48 | 21.7476 | 21.7150 | +0.0326 | 21.2283 | 19.1900 | +2.0383 | 315 |
| [NSE:COROMANDEL](https://in.tradingview.com/chart/?symbol=NSE:COROMANDEL&interval=W) | 1959.00 | +0.20 | 92.3634 | 92.1249 | +0.2385 | -25.5673 | -35.2749 | +9.7076 | 315 |
| [NSE:COSMOFIRST](https://in.tradingview.com/chart/?symbol=NSE:COSMOFIRST&interval=W) | 824.90 | -0.83 | 39.7646 | 39.7514 | +0.0132 | -5.2435 | -8.4009 | +3.1575 | 315 |
| [NSE:CRAFTSMAN](https://in.tradingview.com/chart/?symbol=NSE:CRAFTSMAN&interval=W) | 11345.00 | +2.42 | 502.4180 | 497.7891 | +4.6288 | 42.9989 | 37.0423 | +5.9566 | 296 |
| [NSE:CSBBANK](https://in.tradingview.com/chart/?symbol=NSE:CSBBANK&interval=W) | 333.55 | +9.81 | 15.8419 | 15.8128 | +0.0290 | -43.7011 | -54.1933 | +10.4923 | 315 |
| [NSE:CUB](https://in.tradingview.com/chart/?symbol=NSE:CUB&interval=W) | 232.20 | -0.09 | 11.0558 | 11.0384 | +0.0175 | -2.5668 | -11.8431 | +9.2763 | 315 |
| [NSE:DALMIASUG](https://in.tradingview.com/chart/?symbol=NSE:DALMIASUG&interval=W) | 458.35 | -6.18 | 20.5109 | 20.3452 | +0.1657 | 44.7652 | 43.0544 | +1.7108 | 315 |
| [NSE:DAMCAPITAL](https://in.tradingview.com/chart/?symbol=NSE:DAMCAPITAL&interval=W) | 149.26 | +3.44 | 7.0756 | 7.0613 | +0.0143 | -30.2779 | -40.2809 | +10.0030 | 100 |
| [NSE:DCBBANK](https://in.tradingview.com/chart/?symbol=NSE:DCBBANK&interval=W) | 227.65 | -2.30 | 9.9738 | 9.8702 | +0.1037 | 40.6955 | 33.0365 | +7.6590 | 315 |
| [NSE:DEEPAKFERT](https://in.tradingview.com/chart/?symbol=NSE:DEEPAKFERT&interval=W) | 1480.50 | +17.33 | 64.8579 | 64.1832 | +0.6747 | -28.2004 | -38.9809 | +10.7805 | 315 |
| [NSE:DELHIVERY](https://in.tradingview.com/chart/?symbol=NSE:DELHIVERY&interval=W) | 449.50 | +3.03 | 21.0341 | 20.9635 | +0.0706 | -23.6921 | -33.5859 | +9.8938 | 235 |
| [NSE:DELTACORP](https://in.tradingview.com/chart/?symbol=NSE:DELTACORP&interval=W) | 81.62 | -3.25 | 3.4924 | 3.4469 | +0.0455 | 22.8767 | 17.6197 | +5.2570 | 315 |
| [NSE:DIFFNKG](https://in.tradingview.com/chart/?symbol=NSE:DIFFNKG&interval=W) | 448.75 | +0.18 | 20.0029 | 19.8328 | +0.1701 | 30.9688 | 28.0140 | +2.9548 | 112 |
| [NSE:DSSL](https://in.tradingview.com/chart/?symbol=NSE:DSSL&interval=W) | 1086.95 | +3.18 | 52.4294 | 52.4152 | +0.0142 | -23.8008 | -34.6152 | +10.8144 | 315 |
| [NSE:DVL](https://in.tradingview.com/chart/?symbol=NSE:DVL&interval=W) | 315.90 | +2.60 | 13.5063 | 13.3291 | +0.1772 | 46.4368 | 39.0899 | +7.3469 | 315 |
| [NSE:DYNAMATECH](https://in.tradingview.com/chart/?symbol=NSE:DYNAMATECH&interval=W) | 13388.00 | +1.90 | 592.6474 | 587.1604 | +5.4870 | 49.8289 | 48.9908 | +0.8381 | 315 |
| [NSE:EDELWEISS](https://in.tradingview.com/chart/?symbol=NSE:EDELWEISS&interval=W) | 130.94 | -3.85 | 6.1780 | 6.1625 | +0.0155 | 29.9311 | 28.5538 | +1.3773 | 315 |
| [NSE:EIHOTEL](https://in.tradingview.com/chart/?symbol=NSE:EIHOTEL&interval=W) | 313.45 | -0.98 | 14.9189 | 14.8947 | +0.0241 | -9.4957 | -17.8374 | +8.3417 | 315 |
| [NSE:EIMCOELECO](https://in.tradingview.com/chart/?symbol=NSE:EIMCOELECO&interval=W) | 2528.10 | -6.87 | 106.3883 | 104.7998 | +1.5885 | 61.2646 | 58.1630 | +3.1016 | 315 |
| [NSE:EMAMILTD](https://in.tradingview.com/chart/?symbol=NSE:EMAMILTD&interval=W) | 412.80 | +1.15 | 19.1745 | 19.0954 | +0.0791 | -22.8448 | -36.3112 | +13.4664 | 315 |
| [NSE:EMCURE](https://in.tradingview.com/chart/?symbol=NSE:EMCURE&interval=W) | 2334.80 | -1.14 | 95.4353 | 93.6865 | +1.7488 | 50.8322 | 44.0982 | +6.7340 | 124 |
| [NSE:ENGINERSIN](https://in.tradingview.com/chart/?symbol=NSE:ENGINERSIN&interval=W) | 304.70 | -2.48 | 13.1035 | 12.9402 | +0.1633 | 46.8560 | 43.6625 | +3.1935 | 315 |
| [NSE:ENTERO](https://in.tradingview.com/chart/?symbol=NSE:ENTERO&interval=W) | 1986.00 | +0.88 | 78.9116 | 77.1973 | +1.7142 | 56.3329 | 53.7388 | +2.5941 | 145 |
| [NSE:ERIS](https://in.tradingview.com/chart/?symbol=NSE:ERIS&interval=W) | 1337.10 | +2.29 | 62.5740 | 62.3645 | +0.2095 | -33.6618 | -45.2123 | +11.5505 | 315 |
| [NSE:ETHOSLTD](https://in.tradingview.com/chart/?symbol=NSE:ETHOSLTD&interval=W) | 2819.20 | +1.40 | 127.8998 | 127.0546 | +0.8452 | 16.5333 | 11.1527 | +5.3805 | 234 |
| [NSE:EUREKAFORB](https://in.tradingview.com/chart/?symbol=NSE:EUREKAFORB&interval=W) | 400.45 | +7.73 | 19.1665 | 19.1463 | +0.0201 | -50.8821 | -61.3100 | +10.4279 | 115 |
| [NSE:EXCELINDUS](https://in.tradingview.com/chart/?symbol=NSE:EXCELINDUS&interval=W) | 1012.30 | +1.93 | 46.3982 | 46.1420 | +0.2562 | -3.8976 | -12.2179 | +8.3203 | 315 |
| [NSE:FAZE3Q](https://in.tradingview.com/chart/?symbol=NSE:FAZE3Q&interval=W) | 612.05 | +10.42 | 24.0855 | 23.5339 | +0.5517 | -1.6656 | -14.2827 | +12.6171 | 210 |
| [NSE:FDC](https://in.tradingview.com/chart/?symbol=NSE:FDC&interval=W) | 373.90 | +0.48 | 17.8373 | 17.8127 | +0.0247 | 1.1824 | -2.6206 | +3.8030 | 315 |
| [NSE:FEDERALBNK](https://in.tradingview.com/chart/?symbol=NSE:FEDERALBNK&interval=W) | 360.35 | -0.17 | 16.3440 | 16.2356 | +0.1084 | 36.2440 | 27.3993 | +8.8448 | 315 |
| [NSE:FIEMIND](https://in.tradingview.com/chart/?symbol=NSE:FIEMIND&interval=W) | 2110.40 | -1.07 | 98.6368 | 98.2934 | +0.3434 | -17.0098 | -26.8365 | +9.8267 | 315 |
| [NSE:FILATEX](https://in.tradingview.com/chart/?symbol=NSE:FILATEX&interval=W) | 110.41 | +9.65 | 4.2729 | 4.1662 | +0.1067 | 55.1121 | 51.1267 | +3.9854 | 315 |
| [NSE:FINEORG](https://in.tradingview.com/chart/?symbol=NSE:FINEORG&interval=W) | 5519.00 | +4.14 | 250.2282 | 248.5581 | +1.6701 | 42.0631 | 34.8974 | +7.1657 | 315 |
| [NSE:FLUOROCHEM](https://in.tradingview.com/chart/?symbol=NSE:FLUOROCHEM&interval=W) | 4820.40 | +2.30 | 213.1972 | 211.2028 | +1.9944 | 34.1784 | 28.3610 | +5.8175 | 315 |
| [NSE:GABRIEL](https://in.tradingview.com/chart/?symbol=NSE:GABRIEL&interval=W) | 1491.20 | -3.96 | 66.1540 | 65.5572 | +0.5969 | 51.2484 | 47.8790 | +3.3694 | 315 |
| [NSE:GALAPREC](https://in.tradingview.com/chart/?symbol=NSE:GALAPREC&interval=W) | 1224.60 | -1.25 | 52.4738 | 51.7983 | +0.6755 | 40.0024 | 33.2961 | +6.7062 | 115 |
| [NSE:GESHIP](https://in.tradingview.com/chart/?symbol=NSE:GESHIP&interval=W) | 1530.60 | +0.83 | 71.2999 | 71.0271 | +0.2728 | 29.0523 | 26.5888 | +2.4636 | 315 |
| [NSE:GHCL](https://in.tradingview.com/chart/?symbol=NSE:GHCL&interval=W) | 454.05 | +1.94 | 20.7630 | 20.6432 | +0.1197 | -30.3945 | -43.3209 | +12.9264 | 315 |
| [NSE:GHCLTEXTIL](https://in.tradingview.com/chart/?symbol=NSE:GHCLTEXTIL&interval=W) | 136.90 | +5.26 | 5.8866 | 5.8131 | +0.0735 | 41.8470 | 37.1265 | +4.7204 | 180 |
| [NSE:GLAND](https://in.tradingview.com/chart/?symbol=NSE:GLAND&interval=W) | 3230.50 | -3.11 | 138.3768 | 136.5900 | +1.7868 | 63.4218 | 61.4075 | +2.0142 | 314 |
| [NSE:GLENMARK](https://in.tradingview.com/chart/?symbol=NSE:GLENMARK&interval=W) | 2646.10 | +0.23 | 115.3768 | 114.1165 | +1.2603 | 38.3514 | 31.9048 | +6.4465 | 315 |
| [NSE:GODREJIND](https://in.tradingview.com/chart/?symbol=NSE:GODREJIND&interval=W) | 1101.50 | -1.40 | 52.5245 | 52.4495 | +0.0750 | -22.6878 | -29.4190 | +6.7312 | 315 |
| [NSE:GODREJPROP](https://in.tradingview.com/chart/?symbol=NSE:GODREJPROP&interval=W) | 1877.60 | +1.22 | 86.4634 | 86.0286 | +0.4348 | -11.8077 | -19.4924 | +7.6846 | 315 |
| [NSE:GPPL](https://in.tradingview.com/chart/?symbol=NSE:GPPL&interval=W) | 174.72 | +0.65 | 7.9472 | 7.8969 | +0.0503 | 36.4580 | 29.7657 | +6.6923 | 315 |
| [NSE:GRAPHITE](https://in.tradingview.com/chart/?symbol=NSE:GRAPHITE&interval=W) | 782.50 | -2.18 | 36.0145 | 35.8313 | +0.1832 | 28.3926 | 25.5496 | +2.8431 | 315 |
| [NSE:GREAVESCOT](https://in.tradingview.com/chart/?symbol=NSE:GREAVESCOT&interval=W) | 266.63 | +17.99 | 10.2228 | 9.9555 | +0.2673 | 21.0313 | 7.1387 | +13.8926 | 315 |
| [NSE:GRWRHITECH](https://in.tradingview.com/chart/?symbol=NSE:GRWRHITECH&interval=W) | 7842.00 | +4.25 | 334.9979 | 330.5694 | +4.4284 | 47.8818 | 43.6149 | +4.2668 | 251 |
| [NSE:GULFOILLUB](https://in.tradingview.com/chart/?symbol=NSE:GULFOILLUB&interval=W) | 1150.00 | +1.83 | 52.6117 | 52.3108 | +0.3009 | 17.9424 | 8.5026 | +9.4398 | 315 |
| [NSE:HARIOMPIPE](https://in.tradingview.com/chart/?symbol=NSE:HARIOMPIPE&interval=W) | 355.15 | -3.40 | 17.1627 | 17.1612 | +0.0014 | -21.2029 | -27.5716 | +6.3687 | 241 |
| [NSE:HBLENGINE](https://in.tradingview.com/chart/?symbol=NSE:HBLENGINE&interval=W) | 788.05 | -1.44 | 37.4499 | 37.3835 | +0.0664 | 24.2407 | 24.0447 | +0.1959 | 315 |
| [NSE:HESTERBIO](https://in.tradingview.com/chart/?symbol=NSE:HESTERBIO&interval=W) | 2348.00 | +1.05 | 107.0397 | 106.3874 | +0.6522 | 18.9230 | 15.9430 | +2.9800 | 315 |
| [NSE:HIKAL](https://in.tradingview.com/chart/?symbol=NSE:HIKAL&interval=W) | 223.15 | +0.31 | 10.4699 | 10.4377 | +0.0323 | 6.1473 | 3.3358 | +2.8115 | 315 |
| [NSE:HINDOILEXP](https://in.tradingview.com/chart/?symbol=NSE:HINDOILEXP&interval=W) | 227.84 | +18.42 | 8.3506 | 8.0837 | +0.2669 | 22.0677 | 4.4005 | +17.6672 | 315 |
| [NSE:HINDPETRO](https://in.tradingview.com/chart/?symbol=NSE:HINDPETRO&interval=W) | 386.45 | +1.30 | 17.8896 | 17.8095 | +0.0801 | -15.5905 | -25.2304 | +9.6400 | 315 |
| [NSE:HLEGLAS](https://in.tradingview.com/chart/?symbol=NSE:HLEGLAS&interval=W) | 420.20 | -4.20 | 19.5146 | 19.4338 | +0.0809 | 25.9167 | 24.8670 | +1.0497 | 300 |
| [NSE:HONASA](https://in.tradingview.com/chart/?symbol=NSE:HONASA&interval=W) | 524.50 | +4.49 | 22.1323 | 21.8088 | +0.3235 | 35.1187 | 25.6608 | +9.4579 | 159 |
| [NSE:ICIL](https://in.tradingview.com/chart/?symbol=NSE:ICIL&interval=W) | 576.55 | +5.33 | 21.4924 | 20.8532 | +0.6393 | 61.3025 | 53.9528 | +7.3497 | 315 |
| [NSE:IDFCFIRSTB](https://in.tradingview.com/chart/?symbol=NSE:IDFCFIRSTB&interval=W) | 82.45 | +3.66 | 3.8555 | 3.8423 | +0.0132 | -1.7046 | -7.2689 | +5.5643 | 315 |
| [NSE:IGIL](https://in.tradingview.com/chart/?symbol=NSE:IGIL&interval=W) | 444.10 | +1.18 | 17.8934 | 17.5348 | +0.3586 | 22.9454 | 15.5648 | +7.3805 | 101 |
| [NSE:IIFL](https://in.tradingview.com/chart/?symbol=NSE:IIFL&interval=W) | 661.95 | +3.25 | 28.7378 | 28.4100 | +0.3278 | 25.2080 | 18.0554 | +7.1526 | 315 |
| [NSE:IKIO](https://in.tradingview.com/chart/?symbol=NSE:IKIO&interval=W) | 203.56 | +5.75 | 9.1975 | 9.1327 | +0.0648 | 5.5375 | 1.0673 | +4.4702 | 180 |
| [NSE:INDGN](https://in.tradingview.com/chart/?symbol=NSE:INDGN&interval=W) | 654.95 | -1.69 | 28.4152 | 28.0890 | +0.3262 | 62.2518 | 57.3908 | +4.8610 | 132 |
| [NSE:INDIQUBE](https://in.tradingview.com/chart/?symbol=NSE:INDIQUBE&interval=W) | 183.19 | -2.16 | 8.8519 | 8.8510 | +0.0008 | 13.2135 | 13.0539 | +0.1596 | 69 |
| [NSE:INDOCO](https://in.tradingview.com/chart/?symbol=NSE:INDOCO&interval=W) | 242.01 | +5.84 | 11.3748 | 11.3418 | +0.0330 | -4.4027 | -8.6531 | +4.2504 | 315 |
| [NSE:INDRAMEDCO](https://in.tradingview.com/chart/?symbol=NSE:INDRAMEDCO&interval=W) | 358.00 | +8.44 | 17.0792 | 17.0556 | +0.0236 | -52.9551 | -63.5364 | +10.5812 | 315 |
| [NSE:INOXINDIA](https://in.tradingview.com/chart/?symbol=NSE:INOXINDIA&interval=W) | 2123.20 | +8.22 | 94.5265 | 93.7102 | +0.8163 | 16.9612 | 13.6040 | +3.3572 | 153 |
| [NSE:IREDA](https://in.tradingview.com/chart/?symbol=NSE:IREDA&interval=W) | 119.80 | +1.27 | 5.5838 | 5.5627 | +0.0210 | -35.7482 | -47.4942 | +11.7459 | 156 |
| [NSE:ISGEC](https://in.tradingview.com/chart/?symbol=NSE:ISGEC&interval=W) | 990.10 | +0.44 | 43.9623 | 43.5698 | +0.3924 | 24.3723 | 19.0429 | +5.3294 | 290 |
| [NSE:ITCHOTELS](https://in.tradingview.com/chart/?symbol=NSE:ITCHOTELS&interval=W) | 177.16 | +2.05 | 8.0891 | 8.0412 | +0.0479 | 14.6668 | 6.2777 | +8.3891 | 95 |
| [NSE:ITDC](https://in.tradingview.com/chart/?symbol=NSE:ITDC&interval=W) | 662.80 | -0.76 | 31.3836 | 31.3163 | +0.0673 | -8.2612 | -12.5667 | +4.3055 | 315 |
| [NSE:IXIGO](https://in.tradingview.com/chart/?symbol=NSE:IXIGO&interval=W) | 177.03 | +8.48 | 8.1169 | 8.0724 | +0.0445 | -23.5451 | -33.7221 | +10.1770 | 127 |
| [NSE:J&KBANK](https://in.tradingview.com/chart/?symbol=NSE:J&KBANK&interval=W) | 140.83 | +2.59 | 6.7624 | 6.7575 | +0.0049 | -24.1160 | -29.6986 | +5.5826 | 315 |
| [NSE:JAMNAAUTO](https://in.tradingview.com/chart/?symbol=NSE:JAMNAAUTO&interval=W) | 136.30 | -8.48 | 6.4297 | 6.4134 | +0.0163 | 27.3432 | 22.9011 | +4.4421 | 315 |
| [NSE:JASH](https://in.tradingview.com/chart/?symbol=NSE:JASH&interval=W) | 535.90 | -2.52 | 25.0204 | 24.9305 | +0.0899 | 31.3340 | 30.5916 | +0.7425 | 315 |
| [NSE:JINDALPHOT](https://in.tradingview.com/chart/?symbol=NSE:JINDALPHOT&interval=W) | 1115.90 | -0.91 | 52.9718 | 52.8719 | +0.0999 | 5.9374 | 0.2008 | +5.7366 | 315 |
| [NSE:JSL](https://in.tradingview.com/chart/?symbol=NSE:JSL&interval=W) | 731.45 | +2.65 | 35.0894 | 35.0606 | +0.0288 | -17.4029 | -23.6160 | +6.2130 | 315 |
| [NSE:JYOTICNC](https://in.tradingview.com/chart/?symbol=NSE:JYOTICNC&interval=W) | 1050.00 | -2.15 | 46.0816 | 45.6114 | +0.4702 | 36.8204 | 34.7467 | +2.0738 | 149 |
| [NSE:KALAMANDIR](https://in.tradingview.com/chart/?symbol=NSE:KALAMANDIR&interval=W) | 87.27 | -3.17 | 4.1795 | 4.1754 | +0.0041 | -33.2401 | -42.4337 | +9.1936 | 165 |
| [NSE:KALYANKJIL](https://in.tradingview.com/chart/?symbol=NSE:KALYANKJIL&interval=W) | 650.00 | -6.74 | 27.0710 | 26.6343 | +0.4367 | 29.5360 | 21.0330 | +8.5030 | 296 |
| [NSE:KANSAINER](https://in.tradingview.com/chart/?symbol=NSE:KANSAINER&interval=W) | 198.96 | -1.06 | 9.4322 | 9.4131 | +0.0191 | -19.5924 | -28.1941 | +8.6017 | 315 |
| [NSE:KARURVYSYA](https://in.tradingview.com/chart/?symbol=NSE:KARURVYSYA&interval=W) | 387.00 | +1.43 | 16.6103 | 16.3996 | +0.2107 | 64.7738 | 59.8311 | +4.9427 | 315 |
| [NSE:KDDL](https://in.tradingview.com/chart/?symbol=NSE:KDDL&interval=W) | 4876.80 | +17.14 | 182.8420 | 177.5393 | +5.3027 | 56.5982 | 46.5015 | +10.0967 | 315 |
| [NSE:KFINTECH](https://in.tradingview.com/chart/?symbol=NSE:KFINTECH&interval=W) | 932.75 | -1.91 | 43.7821 | 43.6490 | +0.1331 | -3.0536 | -12.2105 | +9.1568 | 204 |
| [NSE:KIMS](https://in.tradingview.com/chart/?symbol=NSE:KIMS&interval=W) | 759.00 | +4.02 | 36.1211 | 36.0622 | +0.0588 | -18.5783 | -25.6678 | +7.0895 | 282 |
| [NSE:KOLTEPATIL](https://in.tradingview.com/chart/?symbol=NSE:KOLTEPATIL&interval=W) | 460.05 | +0.69 | 20.9321 | 20.8002 | +0.1318 | 44.7843 | 44.3575 | +0.4268 | 315 |
| [NSE:KPRMILL](https://in.tradingview.com/chart/?symbol=NSE:KPRMILL&interval=W) | 1207.50 | +4.24 | 53.7246 | 53.2569 | +0.4677 | 27.7875 | 19.0375 | +8.7501 | 315 |
| [NSE:KRBL](https://in.tradingview.com/chart/?symbol=NSE:KRBL&interval=W) | 408.70 | -5.40 | 18.8318 | 18.7383 | +0.0935 | 18.1736 | 13.0382 | +5.1354 | 315 |
| [NSE:KTKBANK](https://in.tradingview.com/chart/?symbol=NSE:KTKBANK&interval=W) | 342.35 | -5.42 | 15.1368 | 14.9947 | +0.1421 | 49.6705 | 44.7173 | +4.9532 | 315 |
| [NSE:LALPATHLAB](https://in.tradingview.com/chart/?symbol=NSE:LALPATHLAB&interval=W) | 1965.40 | -1.38 | 90.6005 | 90.1548 | +0.4457 | 45.5946 | 45.1341 | +0.4605 | 315 |
| [NSE:LEMONTREE](https://in.tradingview.com/chart/?symbol=NSE:LEMONTREE&interval=W) | 123.59 | +1.34 | 5.5285 | 5.4836 | +0.0449 | 20.0516 | 8.9443 | +11.1073 | 315 |
| [NSE:LICHSGFIN](https://in.tradingview.com/chart/?symbol=NSE:LICHSGFIN&interval=W) | 610.00 | +4.26 | 26.3657 | 26.0520 | +0.3137 | 6.5034 | -7.9538 | +14.4572 | 315 |
| [NSE:LINDEINDIA](https://in.tradingview.com/chart/?symbol=NSE:LINDEINDIA&interval=W) | 6865.00 | +0.21 | 316.5237 | 314.9731 | +1.5505 | -25.1612 | -35.7496 | +10.5884 | 315 |
| [NSE:LMW](https://in.tradingview.com/chart/?symbol=NSE:LMW&interval=W) | 17705.00 | +1.22 | 815.7934 | 811.7416 | +4.0518 | 12.8046 | 8.6328 | +4.1719 | 315 |
| [NSE:LTFOODS](https://in.tradingview.com/chart/?symbol=NSE:LTFOODS&interval=W) | 419.25 | -1.28 | 19.9649 | 19.9337 | +0.0312 | 2.3472 | -1.6486 | +3.9957 | 315 |
| [NSE:LTTS](https://in.tradingview.com/chart/?symbol=NSE:LTTS&interval=W) | 4095.70 | -3.57 | 181.1764 | 179.4850 | +1.6914 | 32.3602 | 29.5999 | +2.7603 | 315 |
| [NSE:LUMAXIND](https://in.tradingview.com/chart/?symbol=NSE:LUMAXIND&interval=W) | 5657.20 | -0.62 | 268.8500 | 268.3737 | +0.4763 | -0.7416 | -7.7390 | +6.9974 | 315 |
| [NSE:LUMAXTECH](https://in.tradingview.com/chart/?symbol=NSE:LUMAXTECH&interval=W) | 2316.10 | +1.62 | 95.2159 | 93.5356 | +1.6803 | 48.5520 | 43.1566 | +5.3954 | 315 |
| [NSE:MAHABANK](https://in.tradingview.com/chart/?symbol=NSE:MAHABANK&interval=W) | 96.00 | +4.69 | 4.0498 | 3.9904 | +0.0593 | 27.4688 | 15.0188 | +12.4500 | 315 |
| [NSE:MANAKCOAT](https://in.tradingview.com/chart/?symbol=NSE:MANAKCOAT&interval=W) | 161.82 | -5.79 | 6.5312 | 6.4016 | +0.1295 | 69.0716 | 66.1202 | +2.9514 | 315 |
| [NSE:MARATHON](https://in.tradingview.com/chart/?symbol=NSE:MARATHON&interval=W) | 435.95 | +0.01 | 19.8321 | 19.7068 | +0.1253 | -8.1206 | -18.6159 | +10.4953 | 315 |
| [NSE:MAXESTATES](https://in.tradingview.com/chart/?symbol=NSE:MAXESTATES&interval=W) | 574.95 | -0.82 | 24.7727 | 24.4692 | +0.3035 | 34.7451 | 29.5046 | +5.2406 | 160 |
| [NSE:MCX](https://in.tradingview.com/chart/?symbol=NSE:MCX&interval=W) | 3619.00 | -2.72 | 155.3788 | 153.4132 | +1.9656 | 51.8309 | 46.9200 | +4.9109 | 315 |
| [NSE:METROPOLIS](https://in.tradingview.com/chart/?symbol=NSE:METROPOLIS&interval=W) | 564.30 | +0.02 | 26.8481 | 26.8037 | +0.0445 | 13.7984 | 11.9393 | +1.8591 | 315 |
| [NSE:MGL](https://in.tradingview.com/chart/?symbol=NSE:MGL&interval=W) | 1115.50 | -3.72 | 53.2425 | 53.1716 | +0.0709 | -12.1693 | -19.6669 | +7.4976 | 315 |
| [NSE:MINDACORP](https://in.tradingview.com/chart/?symbol=NSE:MINDACORP&interval=W) | 714.20 | -2.98 | 32.5745 | 32.3776 | +0.1968 | 10.2461 | 3.9872 | +6.2589 | 315 |
| [NSE:MMFL](https://in.tradingview.com/chart/?symbol=NSE:MMFL&interval=W) | 659.05 | -3.77 | 27.8674 | 27.4666 | +0.4008 | 29.7929 | 24.0656 | +5.7273 | 315 |
| [NSE:MOBIKWIK](https://in.tradingview.com/chart/?symbol=NSE:MOBIKWIK&interval=W) | 226.72 | -0.04 | 10.4150 | 10.3600 | +0.0550 | 30.9935 | 29.0126 | +1.9809 | 101 |
| [NSE:MOTILALOFS](https://in.tradingview.com/chart/?symbol=NSE:MOTILALOFS&interval=W) | 1228.95 | +0.73 | 49.4292 | 48.4283 | +1.0010 | 53.5869 | 46.5240 | +7.0629 | 315 |
| [NSE:MRF](https://in.tradingview.com/chart/?symbol=NSE:MRF&interval=W) | 128845.00 | +0.70 | 6183.2872 | 6178.4508 | +4.8364 | -29.8977 | -39.5677 | +9.6700 | 315 |
| [NSE:MRPL](https://in.tradingview.com/chart/?symbol=NSE:MRPL&interval=W) | 175.97 | -1.52 | 8.2891 | 8.2669 | +0.0222 | 27.5191 | 27.0230 | +0.4961 | 315 |
| [NSE:MSTCLTD](https://in.tradingview.com/chart/?symbol=NSE:MSTCLTD&interval=W) | 693.10 | -11.52 | 31.2828 | 31.0589 | +0.2239 | 15.9666 | 10.5296 | +5.4370 | 315 |
| [NSE:MUFIN](https://in.tradingview.com/chart/?symbol=NSE:MUFIN&interval=W) | 137.65 | -0.64 | 6.4478 | 6.4268 | +0.0210 | 41.5343 | 39.9816 | +1.5527 | 159 |
| [NSE:NAVINFLUOR](https://in.tradingview.com/chart/?symbol=NSE:NAVINFLUOR&interval=W) | 10278.00 | +2.76 | 409.4400 | 400.6740 | +8.7660 | 64.4571 | 56.7465 | +7.7106 | 315 |
| [NSE:NAZARA](https://in.tradingview.com/chart/?symbol=NSE:NAZARA&interval=W) | 415.60 | -2.30 | 18.0480 | 17.8427 | +0.2053 | 65.2251 | 65.1662 | +0.0589 | 295 |
| [NSE:NELCAST](https://in.tradingview.com/chart/?symbol=NSE:NELCAST&interval=W) | 143.62 | -6.43 | 6.4676 | 6.4197 | +0.0479 | 21.6716 | 18.4362 | +3.2354 | 315 |
| [NSE:NEOGEN](https://in.tradingview.com/chart/?symbol=NSE:NEOGEN&interval=W) | 2780.20 | -1.02 | 111.7393 | 109.4667 | +2.2726 | 59.6473 | 55.5248 | +4.1225 | 315 |
| [NSE:NEULANDLAB](https://in.tradingview.com/chart/?symbol=NSE:NEULANDLAB&interval=W) | 21455.00 | +1.79 | 983.8966 | 978.5181 | +5.3785 | 11.4163 | 8.1425 | +3.2738 | 315 |
| [NSE:NGLFINE](https://in.tradingview.com/chart/?symbol=NSE:NGLFINE&interval=W) | 2848.50 | -6.34 | 137.5165 | 137.4912 | +0.0253 | 4.0526 | 1.1775 | +2.8751 | 229 |
| [NSE:NH](https://in.tradingview.com/chart/?symbol=NSE:NH&interval=W) | 1891.30 | +1.66 | 89.3180 | 89.1025 | +0.2156 | -14.5434 | -21.9073 | +7.3639 | 315 |
| [NSE:NILKAMAL](https://in.tradingview.com/chart/?symbol=NSE:NILKAMAL&interval=W) | 2200.10 | -1.34 | 89.5594 | 87.8744 | +1.6850 | 46.8644 | 41.3626 | +5.5019 | 315 |
| [NSE:NITINSPIN](https://in.tradingview.com/chart/?symbol=NSE:NITINSPIN&interval=W) | 680.30 | +1.42 | 29.4043 | 29.0544 | +0.3499 | 62.7652 | 60.1480 | +2.6172 | 315 |
| [NSE:NUVAMA](https://in.tradingview.com/chart/?symbol=NSE:NUVAMA&interval=W) | 1871.20 | +1.27 | 84.4780 | 83.8756 | +0.6024 | 28.2036 | 22.8383 | +5.3653 | 165 |
| [NSE:NUVOCO](https://in.tradingview.com/chart/?symbol=NSE:NUVOCO&interval=W) | 349.95 | +2.50 | 16.2233 | 16.1531 | +0.0702 | 22.3283 | 14.9780 | +7.3503 | 274 |
| [NSE:OBEROIRLTY](https://in.tradingview.com/chart/?symbol=NSE:OBEROIRLTY&interval=W) | 1800.00 | +0.13 | 85.1481 | 84.9572 | +0.1910 | -4.9755 | -11.2758 | +6.3004 | 315 |
| [NSE:ONESOURCE](https://in.tradingview.com/chart/?symbol=NSE:ONESOURCE&interval=W) | 1586.20 | -1.48 | 75.9775 | 75.9035 | +0.0740 | -15.5133 | -22.0008 | +6.4875 | 96 |
| [NSE:OPTIEMUS](https://in.tradingview.com/chart/?symbol=NSE:OPTIEMUS&interval=W) | 829.85 | +2.00 | 32.8972 | 32.1733 | +0.7239 | 63.4239 | 62.5197 | +0.9042 | 315 |
| [NSE:ORCHPHARMA](https://in.tradingview.com/chart/?symbol=NSE:ORCHPHARMA&interval=W) | 955.95 | +8.09 | 44.4925 | 44.3182 | +0.1743 | -7.1990 | -10.8997 | +3.7007 | 315 |
| [NSE:ORIENTELEC](https://in.tradingview.com/chart/?symbol=NSE:ORIENTELEC&interval=W) | 198.51 | -0.22 | 8.9019 | 8.8320 | +0.0699 | 12.7351 | 6.8958 | +5.8392 | 315 |
| [NSE:ORIENTHOT](https://in.tradingview.com/chart/?symbol=NSE:ORIENTHOT&interval=W) | 173.96 | -0.84 | 7.1061 | 6.9754 | +0.1308 | 71.0735 | 69.3876 | +1.6859 | 315 |
| [NSE:PARACABLES](https://in.tradingview.com/chart/?symbol=NSE:PARACABLES&interval=W) | 61.48 | -7.92 | 2.9591 | 2.9576 | +0.0014 | 12.9404 | 12.8894 | +0.0510 | 315 |
| [NSE:PARAGMILK](https://in.tradingview.com/chart/?symbol=NSE:PARAGMILK&interval=W) | 329.97 | -0.38 | 13.0100 | 12.7151 | +0.2949 | 52.5660 | 47.5872 | +4.9788 | 315 |
| [NSE:PATANJALI](https://in.tradingview.com/chart/?symbol=NSE:PATANJALI&interval=W) | 401.00 | -4.75 | 18.9188 | 18.8712 | +0.0476 | 1.7438 | -5.8695 | +7.6133 | 315 |
| [NSE:PDSL](https://in.tradingview.com/chart/?symbol=NSE:PDSL&interval=W) | 405.10 | -1.73 | 17.4933 | 17.2834 | +0.2100 | 28.1064 | 20.6458 | +7.4607 | 315 |
| [NSE:PETRONET](https://in.tradingview.com/chart/?symbol=NSE:PETRONET&interval=W) | 325.50 | +0.45 | 14.3278 | 14.1863 | +0.1415 | 73.2080 | 67.3002 | +5.9078 | 315 |
| [NSE:PHOENIXLTD](https://in.tradingview.com/chart/?symbol=NSE:PHOENIXLTD&interval=W) | 2204.60 | -2.24 | 95.7452 | 94.6570 | +1.0881 | 42.4798 | 34.3742 | +8.1057 | 315 |
| [NSE:PNBGILTS](https://in.tradingview.com/chart/?symbol=NSE:PNBGILTS&interval=W) | 80.34 | +3.79 | 3.8044 | 3.7962 | +0.0081 | -18.1846 | -25.1599 | +6.9753 | 315 |
| [NSE:PNBHOUSING](https://in.tradingview.com/chart/?symbol=NSE:PNBHOUSING&interval=W) | 1125.30 | +0.72 | 53.4214 | 53.3210 | +0.1004 | 16.4909 | 15.9148 | +0.5761 | 315 |
| [NSE:POLYMED](https://in.tradingview.com/chart/?symbol=NSE:POLYMED&interval=W) | 1654.50 | -1.59 | 78.7046 | 78.5729 | +0.1316 | -6.9012 | -12.2436 | +5.3424 | 315 |
| [NSE:POONAWALLA](https://in.tradingview.com/chart/?symbol=NSE:POONAWALLA&interval=W) | 501.35 | +3.41 | 22.3525 | 22.1629 | +0.1896 | 14.2293 | 4.8368 | +9.3926 | 315 |
| [NSE:PPLPHARMA](https://in.tradingview.com/chart/?symbol=NSE:PPLPHARMA&interval=W) | 238.95 | -2.29 | 10.1696 | 10.0308 | +0.1387 | 52.2097 | 49.2301 | +2.9797 | 214 |
| [NSE:PRESTIGE](https://in.tradingview.com/chart/?symbol=NSE:PRESTIGE&interval=W) | 1657.40 | +0.45 | 74.4136 | 73.8389 | +0.5747 | 6.4344 | -2.5906 | +9.0250 | 315 |
| [NSE:PRIMESECU](https://in.tradingview.com/chart/?symbol=NSE:PRIMESECU&interval=W) | 308.70 | +1.25 | 14.2169 | 14.1455 | +0.0714 | 30.2708 | 24.1437 | +6.1271 | 315 |
| [NSE:PRINCEPIPE](https://in.tradingview.com/chart/?symbol=NSE:PRINCEPIPE&interval=W) | 292.95 | -7.19 | 13.4242 | 13.3498 | +0.0744 | 18.9400 | 13.9625 | +4.9775 | 315 |
| [NSE:PRIVISCL](https://in.tradingview.com/chart/?symbol=NSE:PRIVISCL&interval=W) | 3438.30 | +1.77 | 165.6626 | 165.5993 | +0.0633 | -9.1587 | -9.7767 | +0.6180 | 315 |
| [NSE:PROTEAN](https://in.tradingview.com/chart/?symbol=NSE:PROTEAN&interval=W) | 671.80 | -6.00 | 30.0461 | 29.8015 | +0.2446 | 20.4219 | 16.0672 | +4.3547 | 94 |
| [NSE:PVRINOX](https://in.tradingview.com/chart/?symbol=NSE:PVRINOX&interval=W) | 1714.40 | +4.46 | 64.8818 | 63.0782 | +1.8036 | 75.2854 | 73.0197 | +2.2656 | 315 |
| [NSE:QUESS](https://in.tradingview.com/chart/?symbol=NSE:QUESS&interval=W) | 327.35 | -4.45 | 15.2108 | 15.1487 | +0.0622 | 26.3617 | 25.5231 | +0.8385 | 315 |
| [NSE:RACLGEAR](https://in.tradingview.com/chart/?symbol=NSE:RACLGEAR&interval=W) | 1578.30 | +2.40 | 71.4215 | 70.9301 | +0.4914 | 24.3619 | 21.4198 | +2.9421 | 104 |
| [NSE:RADICO](https://in.tradingview.com/chart/?symbol=NSE:RADICO&interval=W) | 4665.00 | +1.30 | 207.8575 | 206.0807 | +1.7768 | 34.3204 | 28.3136 | +6.0068 | 315 |
| [NSE:RAMKY](https://in.tradingview.com/chart/?symbol=NSE:RAMKY&interval=W) | 387.05 | +0.58 | 17.3982 | 17.2661 | +0.1322 | -31.0395 | -40.7523 | +9.7128 | 315 |
| [NSE:RAYMONDREL](https://in.tradingview.com/chart/?symbol=NSE:RAYMONDREL&interval=W) | 634.00 | +8.62 | 29.1536 | 29.0026 | +0.1510 | -1.1826 | -2.7316 | +1.5489 | 73 |
| [NSE:REPCOHOME](https://in.tradingview.com/chart/?symbol=NSE:REPCOHOME&interval=W) | 381.40 | +0.22 | 17.4927 | 17.3974 | +0.0954 | -27.0365 | -38.4766 | +11.4402 | 315 |
| [NSE:RKFORGE](https://in.tradingview.com/chart/?symbol=NSE:RKFORGE&interval=W) | 758.65 | -3.32 | 33.0241 | 32.6573 | +0.3668 | 39.3134 | 33.0251 | +6.2883 | 315 |
| [NSE:ROLEXRINGS](https://in.tradingview.com/chart/?symbol=NSE:ROLEXRINGS&interval=W) | 203.07 | -4.81 | 8.4987 | 8.3665 | +0.1323 | 50.5234 | 47.1871 | +3.3363 | 276 |
| [NSE:ROSSTECH](https://in.tradingview.com/chart/?symbol=NSE:ROSSTECH&interval=W) | 1531.60 | -0.76 | 62.9947 | 61.8865 | +1.1082 | 67.0633 | 66.3597 | +0.7037 | 102 |
| [NSE:RPEL](https://in.tradingview.com/chart/?symbol=NSE:RPEL&interval=W) | 1912.90 | -1.71 | 77.9422 | 76.4846 | +1.4576 | 57.8382 | 54.7975 | +3.0406 | 120 |
| [NSE:RPSGVENT](https://in.tradingview.com/chart/?symbol=NSE:RPSGVENT&interval=W) | 867.60 | +2.72 | 41.6358 | 41.6032 | +0.0326 | -10.7180 | -19.4773 | +8.7593 | 315 |
| [NSE:SAILIFE](https://in.tradingview.com/chart/?symbol=NSE:SAILIFE&interval=W) | 1788.10 | -7.29 | 73.0710 | 71.7299 | +1.3411 | 63.7201 | 60.6082 | +3.1119 | 101 |
| [NSE:SANATHAN](https://in.tradingview.com/chart/?symbol=NSE:SANATHAN&interval=W) | 589.70 | -0.25 | 24.5396 | 24.1414 | +0.3982 | 66.5148 | 61.9934 | +4.5213 | 100 |
| [NSE:SANGAMIND](https://in.tradingview.com/chart/?symbol=NSE:SANGAMIND&interval=W) | 682.20 | +6.87 | 29.0706 | 28.6782 | +0.3924 | 55.2363 | 44.4653 | +10.7709 | 315 |
| [NSE:SANOFI](https://in.tradingview.com/chart/?symbol=NSE:SANOFI&interval=W) | 3231.80 | -2.11 | 156.2197 | 156.2109 | +0.0088 | -25.3297 | -31.6575 | +6.3278 | 315 |
| [NSE:SANSERA](https://in.tradingview.com/chart/?symbol=NSE:SANSERA&interval=W) | 4500.00 | -4.43 | 190.9828 | 188.3166 | +2.6662 | 64.2000 | 62.9734 | +1.2266 | 270 |
| [NSE:SAREGAMA](https://in.tradingview.com/chart/?symbol=NSE:SAREGAMA&interval=W) | 677.35 | +3.66 | 25.6625 | 24.9528 | +0.7098 | 70.9014 | 64.2023 | +6.6991 | 315 |
| [NSE:SASKEN](https://in.tradingview.com/chart/?symbol=NSE:SASKEN&interval=W) | 1864.40 | +7.78 | 86.0768 | 85.6672 | +0.4096 | -17.5107 | -24.5033 | +6.9925 | 315 |
| [NSE:SATIN](https://in.tradingview.com/chart/?symbol=NSE:SATIN&interval=W) | 255.71 | -2.66 | 11.3185 | 11.2136 | +0.1049 | 36.4575 | 32.3029 | +4.1546 | 315 |
| [NSE:SDBL](https://in.tradingview.com/chart/?symbol=NSE:SDBL&interval=W) | 75.58 | -1.74 | 3.6328 | 3.6305 | +0.0023 | 0.6195 | -5.5088 | +6.1284 | 315 |
| [NSE:SHARDAMOTR](https://in.tradingview.com/chart/?symbol=NSE:SHARDAMOTR&interval=W) | 935.05 | -3.08 | 43.3608 | 43.1745 | +0.1863 | 15.4757 | 8.0929 | +7.3828 | 315 |
| [NSE:SHREECEM](https://in.tradingview.com/chart/?symbol=NSE:SHREECEM&interval=W) | 24835.00 | +0.73 | 1169.8854 | 1166.7582 | +3.1272 | -7.5519 | -15.1256 | +7.5737 | 315 |
| [NSE:SHYAMMETL](https://in.tradingview.com/chart/?symbol=NSE:SHYAMMETL&interval=W) | 1317.10 | +0.09 | 54.4256 | 53.4979 | +0.9277 | 78.1422 | 76.2436 | +1.8986 | 283 |
| [NSE:SIGNATURE](https://in.tradingview.com/chart/?symbol=NSE:SIGNATURE&interval=W) | 843.05 | +9.97 | 37.8490 | 37.5565 | +0.2926 | -33.1165 | -50.1345 | +17.0180 | 165 |
| [NSE:SIMPLEXINF](https://in.tradingview.com/chart/?symbol=NSE:SIMPLEXINF&interval=W) | 298.65 | -0.25 | 12.7047 | 12.5307 | +0.1740 | 43.7617 | 36.5033 | +7.2584 | 315 |
| [NSE:SMARTWORKS](https://in.tradingview.com/chart/?symbol=NSE:SMARTWORKS&interval=W) | 509.10 | -0.42 | 23.9149 | 23.8441 | +0.0708 | 18.5722 | 16.6116 | +1.9606 | 71 |
| [NSE:SONACOMS](https://in.tradingview.com/chart/?symbol=NSE:SONACOMS&interval=W) | 889.00 | -3.26 | 38.4661 | 38.0130 | +0.4531 | 64.1521 | 63.7890 | +0.3631 | 283 |
| [NSE:SOUTHBANK](https://in.tradingview.com/chart/?symbol=NSE:SOUTHBANK&interval=W) | 61.02 | -1.36 | 2.4671 | 2.4187 | +0.0484 | 83.1447 | 81.3094 | +1.8353 | 315 |
| [NSE:SPAL](https://in.tradingview.com/chart/?symbol=NSE:SPAL&interval=W) | 933.35 | +4.26 | 44.6281 | 44.5767 | +0.0514 | -15.4861 | -18.5136 | +3.0275 | 315 |
| [NSE:SPORTKING](https://in.tradingview.com/chart/?symbol=NSE:SPORTKING&interval=W) | 217.57 | +7.45 | 9.6519 | 9.5648 | +0.0871 | 20.5829 | 15.6153 | +4.9676 | 222 |
| [NSE:STEL](https://in.tradingview.com/chart/?symbol=NSE:STEL&interval=W) | 616.05 | -7.23 | 27.5036 | 27.2744 | +0.2292 | 15.6345 | 8.4504 | +7.1841 | 315 |
| [NSE:STYLAMIND](https://in.tradingview.com/chart/?symbol=NSE:STYLAMIND&interval=W) | 3282.90 | +1.48 | 154.2313 | 153.7766 | +0.4548 | -1.9291 | -4.7892 | +2.8601 | 277 |
| [NSE:SUDARSCHEM](https://in.tradingview.com/chart/?symbol=NSE:SUDARSCHEM&interval=W) | 1138.75 | -1.63 | 53.4926 | 53.3343 | +0.1584 | 15.6508 | 14.5630 | +1.0878 | 315 |
| [NSE:SUNTECK](https://in.tradingview.com/chart/?symbol=NSE:SUNTECK&interval=W) | 311.35 | +0.21 | 14.5572 | 14.5070 | +0.0501 | -21.4895 | -32.2977 | +10.8082 | 315 |
| [NSE:SUNTV](https://in.tradingview.com/chart/?symbol=NSE:SUNTV&interval=W) | 696.35 | +7.68 | 27.8674 | 27.2862 | +0.5812 | 29.2269 | 22.0954 | +7.1315 | 315 |
| [NSE:SURAKSHA](https://in.tradingview.com/chart/?symbol=NSE:SURAKSHA&interval=W) | 348.05 | +1.86 | 15.3498 | 15.2014 | +0.1484 | 28.9439 | 25.6222 | +3.3217 | 103 |
| [NSE:SURYODAY](https://in.tradingview.com/chart/?symbol=NSE:SURYODAY&interval=W) | 153.35 | -1.86 | 7.3662 | 7.3612 | +0.0051 | -16.3179 | -22.3839 | +6.0660 | 296 |
| [NSE:SYNGENE](https://in.tradingview.com/chart/?symbol=NSE:SYNGENE&interval=W) | 434.80 | -2.14 | 19.9284 | 19.8184 | +0.1101 | -7.2805 | -16.5511 | +9.2706 | 315 |
| [NSE:TALBROAUTO](https://in.tradingview.com/chart/?symbol=NSE:TALBROAUTO&interval=W) | 406.95 | -0.12 | 18.9483 | 18.8749 | +0.0734 | 9.5438 | 7.1704 | +2.3733 | 315 |
| [NSE:TANLA](https://in.tradingview.com/chart/?symbol=NSE:TANLA&interval=W) | 698.05 | -4.76 | 28.1264 | 27.5629 | +0.5635 | 37.9303 | 31.7771 | +6.1533 | 315 |
| [NSE:TASTYBITE](https://in.tradingview.com/chart/?symbol=NSE:TASTYBITE&interval=W) | 11110.00 | -2.89 | 467.7275 | 460.7662 | +6.9613 | 45.4143 | 38.6076 | +6.8068 | 315 |
| [NSE:TATACOMM](https://in.tradingview.com/chart/?symbol=NSE:TATACOMM&interval=W) | 1767.30 | -0.32 | 84.2181 | 84.0922 | +0.1258 | -3.1944 | -13.5050 | +10.3106 | 315 |
| [NSE:TCPLPACK](https://in.tradingview.com/chart/?symbol=NSE:TCPLPACK&interval=W) | 4517.80 | +0.81 | 189.8144 | 186.9453 | +2.8691 | 59.4711 | 58.2040 | +1.2671 | 315 |
| [NSE:THELEELA](https://in.tradingview.com/chart/?symbol=NSE:THELEELA&interval=W) | 689.35 | +3.45 | 27.9366 | 27.3962 | +0.5404 | 73.4318 | 72.4930 | +0.9389 | 77 |
| [NSE:THOMASCOOK](https://in.tradingview.com/chart/?symbol=NSE:THOMASCOOK&interval=W) | 110.71 | +0.76 | 5.0170 | 4.9833 | +0.0338 | -11.0461 | -22.6366 | +11.5906 | 315 |
| [NSE:TI](https://in.tradingview.com/chart/?symbol=NSE:TI&interval=W) | 533.85 | +2.99 | 24.7917 | 24.6889 | +0.1028 | 15.7088 | 14.0371 | +1.6718 | 315 |
| [NSE:TIIL](https://in.tradingview.com/chart/?symbol=NSE:TIIL&interval=W) | 2809.60 | -2.70 | 134.5241 | 134.3878 | +0.1364 | 13.7305 | 11.3303 | +2.4002 | 315 |
| [NSE:TIMETECHNO](https://in.tradingview.com/chart/?symbol=NSE:TIMETECHNO&interval=W) | 189.87 | +0.09 | 8.8253 | 8.7895 | +0.0358 | -14.3893 | -23.6517 | +9.2623 | 315 |
| [NSE:TIPSMUSIC](https://in.tradingview.com/chart/?symbol=NSE:TIPSMUSIC&interval=W) | 811.25 | -0.64 | 34.3930 | 33.9086 | +0.4844 | 54.0436 | 50.3842 | +3.6594 | 315 |
| [NSE:TMB](https://in.tradingview.com/chart/?symbol=NSE:TMB&interval=W) | 892.25 | +0.25 | 40.5840 | 40.3269 | +0.2570 | 24.5809 | 19.6928 | +4.8881 | 219 |
| [NSE:TSFINV](https://in.tradingview.com/chart/?symbol=NSE:TSFINV&interval=W) | 419.30 | +1.08 | 20.2790 | 20.2789 | +0.0001 | -9.7331 | -11.8008 | +2.0677 | 315 |
| [NSE:TTKHLTCARE](https://in.tradingview.com/chart/?symbol=NSE:TTKHLTCARE&interval=W) | 1047.10 | +11.58 | 48.5425 | 48.3324 | +0.2101 | -6.6588 | -10.7878 | +4.1289 | 315 |
| [NSE:TVSSCS](https://in.tradingview.com/chart/?symbol=NSE:TVSSCS&interval=W) | 134.52 | +10.04 | 6.0376 | 5.9907 | +0.0469 | -15.1885 | -30.1344 | +14.9460 | 170 |
| [NSE:TVSSRICHAK](https://in.tradingview.com/chart/?symbol=NSE:TVSSRICHAK&interval=W) | 4485.40 | +3.45 | 211.9392 | 211.4393 | +0.4999 | 9.5624 | 4.3050 | +5.2574 | 315 |
| [NSE:UDS](https://in.tradingview.com/chart/?symbol=NSE:UDS&interval=W) | 219.20 | +0.93 | 9.9128 | 9.8440 | +0.0689 | 32.6074 | 26.5137 | +6.0937 | 164 |
| [NSE:UFLEX](https://in.tradingview.com/chart/?symbol=NSE:UFLEX&interval=W) | 626.70 | +1.36 | 27.9200 | 27.6809 | +0.2391 | 35.5210 | 33.5686 | +1.9524 | 315 |
| [NSE:UNIMECH](https://in.tradingview.com/chart/?symbol=NSE:UNIMECH&interval=W) | 1796.40 | -7.30 | 75.8488 | 74.7453 | +1.1035 | 60.8514 | 60.4318 | +0.4197 | 99 |
| [NSE:UNOMINDA](https://in.tradingview.com/chart/?symbol=NSE:UNOMINDA&interval=W) | 1370.00 | -1.30 | 58.6306 | 57.8676 | +0.7630 | 19.3262 | 11.1145 | +8.2118 | 315 |
| [NSE:VARROC](https://in.tradingview.com/chart/?symbol=NSE:VARROC&interval=W) | 821.80 | -2.02 | 37.3331 | 37.0918 | +0.2414 | 35.2887 | 33.1461 | +2.1426 | 315 |
| [NSE:VIJAYA](https://in.tradingview.com/chart/?symbol=NSE:VIJAYA&interval=W) | 1533.60 | +8.76 | 68.5411 | 67.9778 | +0.5632 | 26.6567 | 20.4437 | +6.2130 | 271 |
| [NSE:VMART](https://in.tradingview.com/chart/?symbol=NSE:VMART&interval=W) | 783.80 | +1.46 | 37.2310 | 37.1632 | +0.0678 | 3.9247 | 2.3337 | +1.5910 | 315 |
| [NSE:VRLLOG](https://in.tradingview.com/chart/?symbol=NSE:VRLLOG&interval=W) | 338.70 | -0.41 | 13.9473 | 13.7039 | +0.2434 | 36.6821 | 28.6247 | +8.0574 | 315 |
| [NSE:VSSL](https://in.tradingview.com/chart/?symbol=NSE:VSSL&interval=W) | 380.35 | +0.69 | 16.9667 | 16.8238 | +0.1429 | 36.9291 | 35.2952 | +1.6339 | 315 |
| [NSE:WELSPUNLIV](https://in.tradingview.com/chart/?symbol=NSE:WELSPUNLIV&interval=W) | 255.97 | +2.33 | 10.1082 | 9.8810 | +0.2272 | 69.7609 | 68.6363 | +1.1246 | 315 |
| [NSE:WESTLIFE](https://in.tradingview.com/chart/?symbol=NSE:WESTLIFE&interval=W) | 675.00 | +2.42 | 28.1557 | 27.7066 | +0.4491 | 62.5864 | 59.1520 | +3.4343 | 315 |
| [NSE:WINDMACHIN](https://in.tradingview.com/chart/?symbol=NSE:WINDMACHIN&interval=W) | 297.55 | +0.83 | 14.2593 | 14.2461 | +0.0132 | -16.0413 | -21.5091 | +5.4678 | 315 |
| [NSE:WOCKPHARMA](https://in.tradingview.com/chart/?symbol=NSE:WOCKPHARMA&interval=W) | 2026.60 | -0.03 | 94.5577 | 94.2117 | +0.3460 | 18.6218 | 17.4633 | +1.1585 | 315 |
| [NSE:XPROINDIA](https://in.tradingview.com/chart/?symbol=NSE:XPROINDIA&interval=W) | 1262.00 | +6.04 | 56.3474 | 55.8784 | +0.4690 | -9.6703 | -19.1440 | +9.4737 | 315 |
| [NSE:YATHARTH](https://in.tradingview.com/chart/?symbol=NSE:YATHARTH&interval=W) | 1091.10 | +2.85 | 46.8634 | 46.2725 | +0.5908 | 51.0881 | 47.1146 | +3.9735 | 172 |
| [NSE:ZENSARTECH](https://in.tradingview.com/chart/?symbol=NSE:ZENSARTECH&interval=W) | 527.35 | -4.04 | 24.5692 | 24.4755 | +0.0936 | 8.1684 | 4.4725 | +3.6959 | 315 |
| [NSE:ZENTEC](https://in.tradingview.com/chart/?symbol=NSE:ZENTEC&interval=W) | 1724.00 | -1.13 | 81.5776 | 81.3972 | +0.1804 | -2.6914 | -6.9809 | +4.2896 | 315 |
| [NSE:ZOTA](https://in.tradingview.com/chart/?symbol=NSE:ZOTA&interval=W) | 1314.50 | +1.34 | 61.7505 | 61.5679 | +0.1826 | 9.8859 | 6.7481 | +3.1378 | 315 |

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
- DRAGARWQ: missing latest benchmark session
- DRREDDY: missing latest benchmark session
- E2E: missing sessions or benchmark history mismatch
- EDELALTS: insufficient history: need 22 weekly bars
- EFCIL: missing sessions or benchmark history mismatch
- EICHERMOT: missing latest benchmark session
- ELANTAS: missing sessions or benchmark history mismatch
- ELEVATE: missing sessions or benchmark history mismatch
- ELPROINTL: missing latest benchmark session
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
- MAXHEALTH: missing latest benchmark session
- MAZDOCK: missing sessions or benchmark history mismatch
- MBAPL: missing sessions or benchmark history mismatch
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
- NSIL: missing sessions or benchmark history mismatch
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
- PILANIINVS: missing sessions or benchmark history mismatch
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
- SEJALLTD: missing sessions or benchmark history mismatch
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
- WEL: missing sessions or benchmark history mismatch
- WEWORK: missing sessions or benchmark history mismatch
- WIPRO: missing latest benchmark session
- WPIL: missing sessions or benchmark history mismatch
- XTRANET: missing sessions or benchmark history mismatch
- ZETWERK: insufficient history: need 22 weekly bars
- ZSARACOM: missing sessions or benchmark history mismatch
- ZYDUSLIFE: missing latest benchmark session


---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
