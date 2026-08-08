"""Shared TradingView benchmarks prepended to every scanner watchlist copy-block."""

INDEX_WATCHLIST_SYMBOLS = ["NSE:NIFTYSMLCAP250", "NSE:NIFTYMIDSML400"]
COMMODITY_WATCHLIST_SYMBOLS = ["MCX:GOLDM1!", "MCX:SILVERM1!", "MCX:COPPER1!", "MCX:ALUMINIUM1!"]


def tv_top_sections():
    """###INDICES / ###COMMODITIES section headers for a top combined multi-bucket block."""
    return [
        "###INDICES," + ",".join(INDEX_WATCHLIST_SYMBOLS),
        "###COMMODITIES," + ",".join(COMMODITY_WATCHLIST_SYMBOLS),
    ]


def tv_csv_flat(symbols):
    """Flat benchmarks + symbols CSV, no section markers of its own — for use inside
    a block that already carries its own external ###LABEL, prefix."""
    return ",".join(INDEX_WATCHLIST_SYMBOLS + COMMODITY_WATCHLIST_SYMBOLS + list(symbols))


def tv_csv(symbols, label="WATCHLIST"):
    """Self-contained TV-import copy block: ###INDICES / ###COMMODITIES / ###<label> sections."""
    return ",".join(tv_top_sections() + [f"###{label}," + ",".join(symbols)])
