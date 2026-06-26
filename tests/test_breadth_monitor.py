import pandas as pd

# Insert project root into path so imports work from tests/
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.refresh_breadth_universe import filter_instruments


def test_filter_keeps_nse_eq_no_dash():
    raw = pd.DataFrame(
        [
            {
                "exchange": "NSE",
                "segment": "NSE",
                "instrument_type": "EQ",
                "tradingsymbol": "SBIN",
                "instrument_token": 1,
                "name": "State Bank",
            },
            {
                "exchange": "NSE",
                "segment": "NSE",
                "instrument_type": "EQ",
                "tradingsymbol": "SBIN-BE",
                "instrument_token": 2,
                "name": "SBI BE",
            },
            {
                "exchange": "NSE",
                "segment": "INDICES",
                "instrument_type": "INDICES",
                "tradingsymbol": "NIFTY 50",
                "instrument_token": 3,
                "name": "Nifty",
            },
            {
                "exchange": "BSE",
                "segment": "BSE",
                "instrument_type": "EQ",
                "tradingsymbol": "SBIN",
                "instrument_token": 4,
                "name": "SBI BSE",
            },
            {
                "exchange": "NSE",
                "segment": "NSE",
                "instrument_type": "EQ",
                "tradingsymbol": "XYZ-SM",
                "instrument_token": 5,
                "name": "SME stock",
            },
        ]
    )
    result = filter_instruments(raw)
    assert list(result["symbol"]) == ["SBIN"]
    assert "instrument_token" in result.columns
    assert "generated_date" in result.columns
