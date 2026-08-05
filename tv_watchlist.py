"""Shared TradingView benchmarks prepended to every scanner watchlist copy-block."""

INDEX_WATCHLIST_SYMBOLS = ["NSE:NIFTYSMLCAP250", "NSE:NIFTYMIDSML400"]
COMMODITY_WATCHLIST_SYMBOLS = ["MCX:GOLDM1!", "MCX:SILVERM1!", "MCX:COPPER1!"]


def tv_csv(symbols):
    """Join NSE:-prefixed symbols into a copy-paste CSV, benchmarks first."""
    return ",".join(INDEX_WATCHLIST_SYMBOLS + COMMODITY_WATCHLIST_SYMBOLS + list(symbols))


def tv_top_sections():
    """###INDICES / ###COMMODITIES section headers for a top combined multi-bucket block."""
    return [
        "###INDICES," + ",".join(INDEX_WATCHLIST_SYMBOLS),
        "###COMMODITIES," + ",".join(COMMODITY_WATCHLIST_SYMBOLS),
    ]
