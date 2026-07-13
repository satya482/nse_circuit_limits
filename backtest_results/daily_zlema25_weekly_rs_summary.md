> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Daily ZLEMA25 + Weekly RS EMA9 Backtest

**Period:** 2021-08-20 to 2026-07-13
**Symbols:** TRIVENI, CARTRADE, KIRLOSENG

## Method

Enter at the close on a daily ZLEMA25 turn-up when daily RS is above its no-look-ahead weekly EMA9 and that EMA9 is rising. Exit at the close on the first ZLEMA25 downturn or when the weekly RS EMA9 is no longer rising. Open trades are excluded from completed-trade statistics.

## Summary

| symbol | trades | wins | losses | zeros | win_rate_pct | average_return_pct | median_return_pct | compounded_return_pct | best_return_pct | worst_return_pct | average_holding_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRIVENI | 48 | 13 | 35 | 0 | 27.08 | -0.27 | -1.45 | -18.37 | 26.68 | -8.23 | 6.40 |
| CARTRADE | 40 | 10 | 30 | 0 | 25.00 | 1.03 | -1.13 | 22.49 | 61.97 | -12.80 | 6.03 |
| KIRLOSENG | 57 | 21 | 36 | 0 | 36.84 | 3.10 | -0.91 | 350.56 | 43.10 | -5.86 | 8.19 |
| COMBINED | 145 | 44 | 101 | 0 | 30.34 | 1.41 | -1.08 | 350.47 | 61.97 | -12.80 | 7.00 |

## Skipped Symbols

None.

## Completed Trades

| symbol | entry_date | entry_close | exit_date | exit_close | return_pct | holding_trading_days | holding_calendar_days | exit_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRIVENI | 2021-10-26 | 203.85 | 2021-10-28 | 187.85 | -7.85 | 2 | 2 | ZLEMA_AND_RS |
| TRIVENI | 2021-11-02 | 204.05 | 2021-11-16 | 198.05 | -2.94 | 9 | 14 | ZLEMA_AND_RS |
| TRIVENI | 2021-11-17 | 205.75 | 2021-11-18 | 199.70 | -2.94 | 1 | 1 | ZLEMA_DOWN |
| TRIVENI | 2021-11-24 | 216.40 | 2021-11-29 | 201.20 | -7.02 | 3 | 5 | ZLEMA_DOWN |
| TRIVENI | 2021-12-02 | 209.10 | 2021-12-20 | 208.65 | -0.22 | 12 | 18 | ZLEMA_DOWN |
| TRIVENI | 2021-12-23 | 216.90 | 2021-12-24 | 216.00 | -0.41 | 1 | 1 | ZLEMA_DOWN |
| TRIVENI | 2021-12-27 | 217.05 | 2022-01-24 | 231.15 | 6.50 | 20 | 28 | ZLEMA_DOWN |
| TRIVENI | 2022-01-27 | 265.15 | 2022-02-14 | 255.35 | -3.70 | 12 | 18 | ZLEMA_DOWN |
| TRIVENI | 2022-02-15 | 272.35 | 2022-02-17 | 272.10 | -0.09 | 2 | 2 | ZLEMA_DOWN |
| TRIVENI | 2022-03-03 | 266.15 | 2022-04-25 | 337.15 | 26.68 | 34 | 53 | ZLEMA_DOWN |
| TRIVENI | 2022-05-18 | 317.10 | 2022-05-23 | 297.35 | -6.23 | 3 | 5 | ZLEMA_DOWN |
| TRIVENI | 2022-09-30 | 254.20 | 2022-10-25 | 269.60 | 6.06 | 16 | 25 | ZLEMA_DOWN |
| TRIVENI | 2022-11-04 | 270.85 | 2022-11-22 | 273.55 | 1.00 | 11 | 18 | ZLEMA_DOWN |
| TRIVENI | 2022-11-24 | 278.45 | 2022-12-08 | 282.05 | 1.29 | 10 | 14 | ZLEMA_AND_RS |
| TRIVENI | 2022-12-16 | 289.00 | 2022-12-22 | 276.70 | -4.26 | 4 | 6 | ZLEMA_DOWN |
| TRIVENI | 2022-12-27 | 290.20 | 2022-12-29 | 283.15 | -2.43 | 2 | 2 | ZLEMA_DOWN |
| TRIVENI | 2023-01-06 | 285.10 | 2023-01-09 | 282.60 | -0.88 | 1 | 3 | ZLEMA_DOWN |
| TRIVENI | 2023-01-16 | 283.25 | 2023-01-17 | 281.85 | -0.49 | 1 | 1 | ZLEMA_DOWN |
| TRIVENI | 2023-01-18 | 285.65 | 2023-01-19 | 282.60 | -1.07 | 1 | 1 | ZLEMA_DOWN |
| TRIVENI | 2023-01-31 | 285.70 | 2023-02-01 | 270.20 | -5.43 | 1 | 1 | ZLEMA_AND_RS |
| TRIVENI | 2023-02-10 | 279.40 | 2023-02-21 | 275.85 | -1.27 | 7 | 11 | ZLEMA_DOWN |
| TRIVENI | 2023-03-02 | 279.05 | 2023-03-15 | 270.95 | -2.90 | 8 | 13 | ZLEMA_AND_RS |
| TRIVENI | 2023-03-23 | 277.80 | 2023-03-24 | 266.45 | -4.09 | 1 | 1 | ZLEMA_AND_RS |
| TRIVENI | 2023-08-21 | 303.90 | 2023-08-22 | 303.45 | -0.15 | 1 | 1 | RS_NOT_RISING |
| TRIVENI | 2023-10-10 | 386.45 | 2023-10-23 | 354.65 | -8.23 | 9 | 13 | ZLEMA_AND_RS |
| TRIVENI | 2024-03-04 | 353.85 | 2024-03-05 | 345.60 | -2.33 | 1 | 1 | RS_NOT_RISING |
| TRIVENI | 2024-04-22 | 359.90 | 2024-05-06 | 348.25 | -3.24 | 9 | 14 | ZLEMA_AND_RS |
| TRIVENI | 2024-05-08 | 354.90 | 2024-05-09 | 347.85 | -1.99 | 1 | 1 | ZLEMA_DOWN |
| TRIVENI | 2024-05-14 | 355.90 | 2024-05-16 | 350.10 | -1.63 | 2 | 2 | ZLEMA_AND_RS |
| TRIVENI | 2024-05-17 | 365.10 | 2024-05-21 | 351.75 | -3.66 | 2 | 4 | ZLEMA_AND_RS |
| TRIVENI | 2024-07-24 | 413.60 | 2024-08-02 | 397.90 | -3.80 | 7 | 9 | ZLEMA_AND_RS |
| TRIVENI | 2024-08-13 | 412.15 | 2024-09-26 | 472.10 | 14.55 | 31 | 44 | ZLEMA_DOWN |
| TRIVENI | 2024-10-01 | 478.65 | 2024-10-03 | 473.20 | -1.14 | 1 | 2 | ZLEMA_DOWN |
| TRIVENI | 2025-01-01 | 462.80 | 2025-01-02 | 454.95 | -1.70 | 1 | 1 | ZLEMA_DOWN |
| TRIVENI | 2025-02-21 | 377.85 | 2025-02-25 | 363.95 | -3.68 | 2 | 4 | ZLEMA_AND_RS |
| TRIVENI | 2025-03-06 | 366.15 | 2025-03-13 | 365.25 | -0.25 | 5 | 7 | ZLEMA_DOWN |
| TRIVENI | 2025-03-17 | 366.85 | 2025-03-26 | 385.00 | 4.95 | 7 | 9 | RS_NOT_RISING |
| TRIVENI | 2025-04-11 | 379.90 | 2025-04-21 | 399.60 | 5.19 | 4 | 10 | RS_NOT_RISING |
| TRIVENI | 2025-05-07 | 418.40 | 2025-05-08 | 409.40 | -2.15 | 1 | 1 | ZLEMA_DOWN |
| TRIVENI | 2025-05-12 | 419.30 | 2025-05-16 | 430.10 | 2.58 | 4 | 4 | RS_NOT_RISING |
| TRIVENI | 2025-08-28 | 351.75 | 2025-09-01 | 349.70 | -0.58 | 2 | 4 | RS_NOT_RISING |
| TRIVENI | 2025-11-27 | 363.15 | 2025-11-28 | 355.85 | -2.01 | 1 | 1 | ZLEMA_AND_RS |
| TRIVENI | 2025-12-09 | 365.05 | 2025-12-10 | 347.65 | -4.77 | 1 | 1 | ZLEMA_AND_RS |
| TRIVENI | 2025-12-12 | 357.85 | 2026-01-05 | 380.05 | 6.20 | 15 | 24 | ZLEMA_DOWN |
| TRIVENI | 2026-01-28 | 358.55 | 2026-02-24 | 380.00 | 5.98 | 20 | 27 | ZLEMA_DOWN |
| TRIVENI | 2026-02-25 | 385.10 | 2026-03-09 | 374.65 | -2.71 | 7 | 12 | ZLEMA_DOWN |
| TRIVENI | 2026-03-24 | 370.30 | 2026-04-10 | 383.00 | 3.43 | 10 | 17 | RS_NOT_RISING |
| TRIVENI | 2026-06-11 | 382.60 | 2026-06-12 | 385.95 | 0.88 | 1 | 1 | RS_NOT_RISING |
| CARTRADE | 2022-04-26 | 638.35 | 2022-05-09 | 616.85 | -3.37 | 8 | 13 | ZLEMA_DOWN |
| CARTRADE | 2022-05-24 | 609.15 | 2022-05-25 | 579.35 | -4.89 | 1 | 1 | ZLEMA_DOWN |
| CARTRADE | 2022-05-27 | 618.50 | 2022-06-14 | 630.70 | 1.97 | 12 | 18 | ZLEMA_DOWN |
| CARTRADE | 2023-07-03 | 491.90 | 2023-07-10 | 487.35 | -0.92 | 5 | 7 | ZLEMA_AND_RS |
| CARTRADE | 2023-07-11 | 555.95 | 2023-07-18 | 508.65 | -8.51 | 5 | 7 | ZLEMA_DOWN |
| CARTRADE | 2023-07-19 | 512.10 | 2023-07-21 | 509.60 | -0.49 | 2 | 2 | ZLEMA_DOWN |
| CARTRADE | 2023-09-13 | 567.45 | 2023-09-20 | 565.20 | -0.40 | 4 | 7 | ZLEMA_AND_RS |
| CARTRADE | 2023-10-03 | 584.80 | 2023-10-23 | 616.15 | 5.36 | 14 | 20 | ZLEMA_DOWN |
| CARTRADE | 2023-10-25 | 643.40 | 2023-11-22 | 779.20 | 21.11 | 20 | 28 | ZLEMA_DOWN |
| CARTRADE | 2023-11-24 | 841.50 | 2023-11-29 | 782.15 | -7.05 | 2 | 5 | ZLEMA_DOWN |
| CARTRADE | 2024-02-26 | 760.30 | 2024-03-06 | 725.30 | -4.60 | 8 | 9 | ZLEMA_AND_RS |
| CARTRADE | 2024-04-01 | 707.10 | 2024-04-05 | 716.55 | 1.34 | 4 | 4 | RS_NOT_RISING |
| CARTRADE | 2024-05-30 | 893.60 | 2024-05-31 | 869.65 | -2.68 | 1 | 1 | ZLEMA_DOWN |
| CARTRADE | 2024-08-16 | 878.85 | 2024-08-26 | 875.05 | -0.43 | 6 | 10 | ZLEMA_AND_RS |
| CARTRADE | 2024-09-10 | 917.80 | 2024-09-30 | 964.45 | 5.08 | 14 | 20 | ZLEMA_DOWN |
| CARTRADE | 2024-10-01 | 990.85 | 2024-10-03 | 933.00 | -5.84 | 1 | 2 | ZLEMA_AND_RS |
| CARTRADE | 2024-10-11 | 939.00 | 2024-12-30 | 1520.90 | 61.97 | 53 | 80 | ZLEMA_DOWN |
| CARTRADE | 2025-01-02 | 1597.45 | 2025-01-07 | 1557.10 | -2.53 | 3 | 5 | ZLEMA_DOWN |
| CARTRADE | 2025-01-09 | 1619.95 | 2025-01-10 | 1549.20 | -4.37 | 1 | 1 | ZLEMA_DOWN |
| CARTRADE | 2025-01-29 | 1541.20 | 2025-02-10 | 1608.40 | 4.36 | 9 | 12 | ZLEMA_DOWN |
| CARTRADE | 2025-03-04 | 1548.55 | 2025-03-06 | 1541.50 | -0.46 | 2 | 2 | ZLEMA_DOWN |
| CARTRADE | 2025-03-07 | 1548.80 | 2025-03-12 | 1532.55 | -1.05 | 3 | 5 | ZLEMA_DOWN |
| CARTRADE | 2025-03-13 | 1559.00 | 2025-03-28 | 1644.95 | 5.51 | 10 | 15 | ZLEMA_DOWN |
| CARTRADE | 2025-04-03 | 1679.10 | 2025-04-07 | 1464.20 | -12.80 | 2 | 4 | ZLEMA_AND_RS |
| CARTRADE | 2025-08-29 | 2398.00 | 2025-09-10 | 2453.70 | 2.32 | 8 | 12 | ZLEMA_DOWN |
| CARTRADE | 2025-09-19 | 2540.60 | 2025-09-22 | 2389.20 | -5.96 | 1 | 3 | ZLEMA_DOWN |
| CARTRADE | 2025-09-24 | 2493.00 | 2025-09-25 | 2454.30 | -1.55 | 1 | 1 | ZLEMA_DOWN |
| CARTRADE | 2025-09-29 | 2500.40 | 2025-09-30 | 2450.10 | -2.01 | 1 | 1 | ZLEMA_DOWN |
| CARTRADE | 2025-10-03 | 2497.80 | 2025-10-07 | 2462.80 | -1.40 | 2 | 4 | ZLEMA_DOWN |
| CARTRADE | 2025-10-08 | 2492.00 | 2025-10-09 | 2475.00 | -0.68 | 1 | 1 | ZLEMA_DOWN |
| CARTRADE | 2025-10-13 | 2498.50 | 2025-10-14 | 2466.80 | -1.27 | 1 | 1 | ZLEMA_DOWN |
| CARTRADE | 2025-10-15 | 2487.80 | 2025-10-17 | 2457.60 | -1.21 | 2 | 2 | ZLEMA_DOWN |
| CARTRADE | 2025-10-21 | 2514.10 | 2025-11-21 | 3024.80 | 20.31 | 21 | 31 | ZLEMA_DOWN |
| CARTRADE | 2025-11-24 | 3063.60 | 2025-11-27 | 3055.50 | -0.26 | 3 | 3 | ZLEMA_DOWN |
| CARTRADE | 2025-11-28 | 3087.70 | 2025-12-01 | 3063.60 | -0.78 | 1 | 3 | ZLEMA_DOWN |
| CARTRADE | 2025-12-03 | 3095.20 | 2025-12-04 | 3008.30 | -2.81 | 1 | 1 | ZLEMA_DOWN |
| CARTRADE | 2025-12-22 | 2902.40 | 2025-12-23 | 2792.90 | -3.77 | 1 | 1 | ZLEMA_AND_RS |
| CARTRADE | 2025-12-31 | 2826.20 | 2026-01-07 | 2812.80 | -0.47 | 5 | 7 | ZLEMA_AND_RS |
| CARTRADE | 2026-01-13 | 2800.50 | 2026-01-14 | 2706.60 | -3.35 | 1 | 1 | ZLEMA_AND_RS |
| CARTRADE | 2026-01-30 | 2649.30 | 2026-02-01 | 2585.40 | -2.41 | 1 | 2 | ZLEMA_DOWN |
| KIRLOSENG | 2022-05-17 | 146.55 | 2022-05-19 | 141.45 | -3.48 | 2 | 2 | ZLEMA_DOWN |
| KIRLOSENG | 2022-05-20 | 153.15 | 2022-05-25 | 147.85 | -3.46 | 3 | 5 | ZLEMA_DOWN |
| KIRLOSENG | 2022-05-26 | 152.60 | 2022-06-07 | 152.85 | 0.16 | 8 | 12 | ZLEMA_DOWN |
| KIRLOSENG | 2022-08-11 | 165.65 | 2022-09-20 | 237.05 | 43.10 | 26 | 40 | ZLEMA_DOWN |
| KIRLOSENG | 2022-09-22 | 239.85 | 2022-09-23 | 237.00 | -1.19 | 1 | 1 | ZLEMA_DOWN |
| KIRLOSENG | 2022-09-30 | 243.05 | 2022-10-03 | 229.55 | -5.55 | 1 | 3 | ZLEMA_DOWN |
| KIRLOSENG | 2022-10-06 | 240.25 | 2022-10-21 | 255.65 | 6.41 | 11 | 15 | ZLEMA_DOWN |
| KIRLOSENG | 2022-10-24 | 265.00 | 2022-10-25 | 263.55 | -0.55 | 1 | 1 | ZLEMA_DOWN |
| KIRLOSENG | 2022-11-04 | 277.00 | 2022-11-25 | 312.90 | 12.96 | 14 | 21 | ZLEMA_DOWN |
| KIRLOSENG | 2022-11-28 | 327.45 | 2022-12-14 | 334.05 | 2.02 | 12 | 16 | ZLEMA_DOWN |
| KIRLOSENG | 2022-12-15 | 337.95 | 2022-12-16 | 318.70 | -5.70 | 1 | 1 | ZLEMA_DOWN |
| KIRLOSENG | 2022-12-30 | 322.60 | 2023-01-02 | 314.85 | -2.40 | 1 | 3 | ZLEMA_DOWN |
| KIRLOSENG | 2023-01-16 | 317.85 | 2023-01-17 | 315.30 | -0.80 | 1 | 1 | ZLEMA_DOWN |
| KIRLOSENG | 2023-01-18 | 323.85 | 2023-01-24 | 314.20 | -2.98 | 4 | 6 | ZLEMA_DOWN |
| KIRLOSENG | 2023-01-31 | 313.40 | 2023-02-01 | 305.30 | -2.58 | 1 | 1 | ZLEMA_DOWN |
| KIRLOSENG | 2023-02-06 | 311.25 | 2023-02-07 | 305.35 | -1.90 | 1 | 1 | ZLEMA_AND_RS |
| KIRLOSENG | 2023-02-09 | 327.00 | 2023-02-24 | 314.65 | -3.78 | 11 | 15 | ZLEMA_DOWN |
| KIRLOSENG | 2023-02-28 | 315.15 | 2023-03-01 | 310.35 | -1.52 | 1 | 1 | ZLEMA_DOWN |
| KIRLOSENG | 2023-03-03 | 319.75 | 2023-04-10 | 378.05 | 18.23 | 22 | 38 | ZLEMA_DOWN |
| KIRLOSENG | 2023-04-11 | 391.60 | 2023-04-27 | 396.20 | 1.17 | 11 | 16 | ZLEMA_DOWN |
| KIRLOSENG | 2023-05-11 | 410.90 | 2023-05-23 | 401.90 | -2.19 | 8 | 12 | ZLEMA_AND_RS |
| KIRLOSENG | 2023-08-31 | 483.90 | 2023-09-12 | 497.90 | 2.89 | 8 | 12 | ZLEMA_DOWN |
| KIRLOSENG | 2023-09-26 | 510.65 | 2023-10-23 | 533.85 | 4.54 | 18 | 27 | ZLEMA_DOWN |
| KIRLOSENG | 2023-10-31 | 543.70 | 2023-11-03 | 533.45 | -1.89 | 3 | 3 | ZLEMA_DOWN |
| KIRLOSENG | 2023-11-06 | 544.95 | 2023-11-08 | 543.30 | -0.30 | 2 | 2 | ZLEMA_DOWN |
| KIRLOSENG | 2023-11-09 | 547.35 | 2023-11-16 | 540.85 | -1.19 | 5 | 7 | ZLEMA_AND_RS |
| KIRLOSENG | 2023-11-28 | 561.20 | 2024-01-23 | 680.50 | 21.26 | 39 | 56 | ZLEMA_DOWN |
| KIRLOSENG | 2024-01-25 | 689.15 | 2024-03-05 | 881.30 | 27.88 | 28 | 40 | ZLEMA_DOWN |
| KIRLOSENG | 2024-03-15 | 854.10 | 2024-03-18 | 841.90 | -1.43 | 1 | 3 | ZLEMA_DOWN |
| KIRLOSENG | 2024-03-21 | 855.35 | 2024-04-15 | 867.35 | 1.40 | 14 | 25 | ZLEMA_AND_RS |
| KIRLOSENG | 2024-04-16 | 894.85 | 2024-04-19 | 885.20 | -1.08 | 2 | 3 | ZLEMA_DOWN |
| KIRLOSENG | 2024-04-22 | 935.50 | 2024-05-29 | 1209.95 | 29.34 | 26 | 37 | ZLEMA_DOWN |
| KIRLOSENG | 2024-05-31 | 1246.10 | 2024-06-04 | 1210.80 | -2.83 | 2 | 4 | ZLEMA_DOWN |
| KIRLOSENG | 2024-06-07 | 1241.45 | 2024-06-10 | 1230.20 | -0.91 | 1 | 3 | ZLEMA_DOWN |
| KIRLOSENG | 2024-06-11 | 1280.55 | 2024-07-09 | 1381.10 | 7.85 | 19 | 28 | ZLEMA_DOWN |
| KIRLOSENG | 2024-08-30 | 1334.35 | 2024-09-05 | 1324.90 | -0.71 | 4 | 6 | RS_NOT_RISING |
| KIRLOSENG | 2024-11-06 | 1192.95 | 2024-11-12 | 1137.70 | -4.63 | 4 | 6 | ZLEMA_DOWN |
| KIRLOSENG | 2024-11-14 | 1137.40 | 2024-11-18 | 1135.45 | -0.17 | 1 | 4 | ZLEMA_DOWN |
| KIRLOSENG | 2025-04-11 | 726.15 | 2025-04-15 | 732.70 | 0.90 | 1 | 4 | RS_NOT_RISING |
| KIRLOSENG | 2025-07-10 | 918.10 | 2025-07-28 | 902.65 | -1.68 | 12 | 18 | ZLEMA_DOWN |
| KIRLOSENG | 2025-07-29 | 920.80 | 2025-07-31 | 904.20 | -1.80 | 2 | 2 | ZLEMA_DOWN |
| KIRLOSENG | 2025-08-06 | 919.50 | 2025-08-08 | 904.85 | -1.59 | 2 | 2 | ZLEMA_DOWN |
| KIRLOSENG | 2025-08-11 | 912.25 | 2025-08-12 | 896.20 | -1.76 | 1 | 1 | ZLEMA_DOWN |
| KIRLOSENG | 2025-08-18 | 944.10 | 2025-08-26 | 923.60 | -2.17 | 6 | 8 | ZLEMA_DOWN |
| KIRLOSENG | 2025-09-16 | 931.20 | 2025-09-26 | 915.20 | -1.72 | 8 | 10 | ZLEMA_DOWN |
| KIRLOSENG | 2025-11-12 | 1058.65 | 2025-12-03 | 1085.20 | 2.51 | 15 | 21 | ZLEMA_DOWN |
| KIRLOSENG | 2025-12-04 | 1165.10 | 2025-12-08 | 1096.80 | -5.86 | 2 | 4 | ZLEMA_DOWN |
| KIRLOSENG | 2025-12-09 | 1123.40 | 2025-12-10 | 1112.50 | -0.97 | 1 | 1 | ZLEMA_DOWN |
| KIRLOSENG | 2025-12-12 | 1144.60 | 2025-12-29 | 1222.40 | 6.80 | 10 | 17 | ZLEMA_DOWN |
| KIRLOSENG | 2026-01-01 | 1230.50 | 2026-01-07 | 1221.50 | -0.73 | 4 | 6 | ZLEMA_DOWN |
| KIRLOSENG | 2026-01-30 | 1174.00 | 2026-02-01 | 1140.40 | -2.86 | 1 | 2 | ZLEMA_DOWN |
| KIRLOSENG | 2026-02-02 | 1152.30 | 2026-03-18 | 1435.60 | 24.59 | 31 | 44 | ZLEMA_DOWN |
| KIRLOSENG | 2026-04-06 | 1416.40 | 2026-05-11 | 1660.00 | 17.20 | 23 | 35 | ZLEMA_DOWN |
| KIRLOSENG | 2026-05-15 | 1740.20 | 2026-05-19 | 1660.30 | -4.59 | 2 | 4 | ZLEMA_DOWN |
| KIRLOSENG | 2026-05-21 | 1674.70 | 2026-05-22 | 1671.00 | -0.22 | 1 | 1 | ZLEMA_DOWN |
| KIRLOSENG | 2026-05-25 | 1702.80 | 2026-06-10 | 1817.80 | 6.75 | 12 | 16 | ZLEMA_DOWN |
| KIRLOSENG | 2026-06-12 | 1890.50 | 2026-07-03 | 2230.80 | 18.00 | 15 | 21 | ZLEMA_DOWN |

## Open Trades

| symbol | entry_date | entry_close | last_date | last_close | unrealized_return_pct | holding_trading_days | holding_calendar_days |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KIRLOSENG | 2026-07-08 | 2277.00 | 2026-07-13 | 2436.20 | 6.99 | 3 | 5 |

> The combined compounded return is a strategy-sequence diagnostic, not a realizable portfolio return, because trades in different stocks may overlap.


---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
