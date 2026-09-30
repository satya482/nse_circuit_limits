> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Darvas chart overlay implementation plan

Goal: fixed length 5 Darvas top/bottom lines on charts.html, one default-on toggle.
Architecture: compute from embedded OHLC bars in the shared JavaScript renderer; opt in only from tradingview_watchlist_dashboard.py. Preserve Pine strict comparisons and ordinary line plots, with whitespace until first confirmation.

- [x] Add Node-executed tests for confirmation after three bars, frozen levels, equal highs, restart timing, and empty data.
- [x] Add darvasLineData(bars), rebuildDarvas(entry), chart initialization, and guarded toggle listener in union_chart_dashboard.py.
- [x] Add darvas_enabled=False to build_html; enable it in tradingview_watchlist_dashboard.py.
- [x] Verify toggle off/on and run dashboard tests.
- [x] Regenerate dashboard/charts.html from its existing embedded records, preserving its date and data; update HANDOFF.md.

Validation: python -m pytest tests/test_darvas_chart.py tests/test_union_chart_dashboard.py tests/test_near_52w_high_chart_dashboard.py tests/test_us_near_52w_high_chart_dashboard.py -q -p no:cacheprovider

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
