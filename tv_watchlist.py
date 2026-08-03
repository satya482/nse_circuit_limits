"""Shared TradingView benchmark indices prepended to every scanner watchlist copy-block."""

INDEX_WATCHLIST_SYMBOLS = ["NSE:NIFTYSMLCAP250", "NSE:NIFTYMIDSML400"]


def tv_csv(symbols):
    """Join NSE:-prefixed symbols into a copy-paste CSV, benchmark indices first."""
    return ",".join(INDEX_WATCHLIST_SYMBOLS + list(symbols))
