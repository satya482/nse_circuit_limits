"""Slot capacity state machine (Sec 9). Slots are a plain list[dict] the
caller owns and passes in/out -- no persistence (matches the Phase 1+2 design
decision to cut signals.db; the same reasoning applies here, see the Phase 3
plan's Global Constraints). Every function returns a new list; none mutate
their input in place, so callers can't be surprised by aliasing."""

import copy

MAX_ARMED = 2


def init_slots(n: int) -> list[dict]:
    return [{"status": "FREE", "symbol": None} for _ in range(n)]


def _find(slots: list[dict], status: str) -> int | None:
    for i, slot in enumerate(slots):
        if slot["status"] == status:
            return i
    return None


def assign_slot(slots: list[dict], symbol: str) -> list[dict]:
    slots = copy.deepcopy(slots)
    idx = _find(slots, "FREE")
    if idx is None:
        raise ValueError(f"no free slot for {symbol}")
    slots[idx] = {"status": "DEPLOYED", "symbol": symbol}
    return slots


def arm_slot(slots: list[dict], symbol: str) -> list[dict]:
    slots = copy.deepcopy(slots)
    if count_status(slots, "ARMED") >= MAX_ARMED:
        raise ValueError(f"max {MAX_ARMED} armed slots already reserved")
    idx = _find(slots, "FREE")
    if idx is None:
        raise ValueError(f"no free slot to arm for {symbol}")
    slots[idx] = {"status": "ARMED", "symbol": symbol}
    return slots


def free_slot(slots: list[dict], symbol: str) -> list[dict]:
    slots = copy.deepcopy(slots)
    for slot in slots:
        if slot["symbol"] == symbol:
            slot["status"] = "FREE"
            slot["symbol"] = None
            return slots
    raise ValueError(f"{symbol} not found in any slot")


def count_status(slots: list[dict], status: str) -> int:
    return sum(1 for slot in slots if slot["status"] == status)


def rotate_to_top_hot(slots: list[dict], exiting_symbol: str, hot_candidates: list[str]) -> list[dict]:
    """Sec 9: 'Time-stop exit frees slot immediately; rotate to top HOT
    candidate.' hot_candidates is caller-ranked (best first); takes the first
    one not already occupying a slot."""
    slots = free_slot(slots, exiting_symbol)
    occupied = {slot["symbol"] for slot in slots if slot["symbol"]}
    for candidate in hot_candidates:
        if candidate not in occupied:
            return assign_slot(slots, candidate)
    return slots
