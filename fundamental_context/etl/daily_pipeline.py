"""
Daily Knowledge Graph Pipeline

Runs three steps in sequence after market close (~5:00 PM IST):
  1. NSE RSS parser  -> create Catalyst nodes
  2. Score recompute -> update conviction_score on all companies
  3. EP flag check   -> write ep_watchlist_YYYYMMDD.csv

Usage:
  python daily_pipeline.py --mode full      # all three steps
  python daily_pipeline.py --mode rss       # only NSE RSS
  python daily_pipeline.py --mode scores    # only score recompute
  python daily_pipeline.py --mode ep        # only EP flag check
"""
from __future__ import annotations

import argparse
import logging
import sys
from datetime import date
from pathlib import Path

# ── Logging ───────────────────────────────────────────────────────────────────
_HERE    = Path(__file__).parent
_LOG_DIR = _HERE.parent / "logs"
_LOG_DIR.mkdir(exist_ok=True)

_LOG_FILE = _LOG_DIR / f"pipeline_{date.today().isoformat()}.log"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)-5s | %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.FileHandler(_LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger(__name__)


# ── Steps ─────────────────────────────────────────────────────────────────────
def step_rss() -> None:
    log.info("=== Step 1: NSE RSS Parser ===")
    from nse_rss_parser import main as rss_main  # type: ignore[import]
    rss_main()
    log.info("=== Step 1 Done ===")


def step_scores() -> None:
    log.info("=== Step 2: Score Recompute ===")
    from recompute_scores import run as scores_run  # type: ignore[import]
    updated = scores_run()
    log.info(f"=== Step 2 Done | {updated} companies updated ===")


def step_ep() -> None:
    log.info("=== Step 3: EP Flag Check ===")
    from flag_ep_candidates import run as ep_run  # type: ignore[import]
    ep_run()
    log.info("=== Step 3 Done ===")


STEPS = {
    "rss":    step_rss,
    "scores": step_scores,
    "ep":     step_ep,
}


def main() -> None:
    parser = argparse.ArgumentParser(description="NSE Knowledge Graph daily pipeline")
    parser.add_argument(
        "--mode",
        choices=["full", "rss", "scores", "ep"],
        default="full",
        help="Which pipeline step(s) to run",
    )
    args = parser.parse_args()

    log.info(f"=== Pipeline START | mode={args.mode} | {date.today()} ===")

    if args.mode == "full":
        for step in ["rss", "scores", "ep"]:
            STEPS[step]()
    else:
        STEPS[args.mode]()

    log.info(f"=== Pipeline DONE | log -> {_LOG_FILE} ===")


if __name__ == "__main__":
    main()
