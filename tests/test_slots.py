# tests/test_slots.py
import pytest

from capital import slots


def test_init_slots_all_free():
    s = slots.init_slots(5)
    assert len(s) == 5
    assert all(slot["status"] == "FREE" and slot["symbol"] is None for slot in s)


def test_assign_slot_fills_first_free():
    s = slots.init_slots(3)
    s = slots.assign_slot(s, "TCS")
    assert s[0] == {"status": "DEPLOYED", "symbol": "TCS"}
    assert s[1]["status"] == "FREE"


def test_assign_slot_raises_when_full():
    s = [{"status": "DEPLOYED", "symbol": "TCS"}]
    with pytest.raises(ValueError, match="no free slot"):
        slots.assign_slot(s, "INFY")


def test_arm_slot_reserves_up_to_two():
    s = slots.init_slots(3)
    s = slots.arm_slot(s, "TCS")
    s = slots.arm_slot(s, "INFY")
    assert slots.count_status(s, "ARMED") == 2


def test_arm_slot_raises_when_two_already_armed():
    s = slots.init_slots(3)
    s = slots.arm_slot(s, "TCS")
    s = slots.arm_slot(s, "INFY")
    with pytest.raises(ValueError, match="max 2 armed"):
        slots.arm_slot(s, "WIPRO")


def test_free_slot_by_symbol():
    s = [{"status": "DEPLOYED", "symbol": "TCS"}, {"status": "FREE", "symbol": None}]
    s = slots.free_slot(s, "TCS")
    assert s[0] == {"status": "FREE", "symbol": None}


def test_free_slot_raises_when_symbol_not_found():
    s = [{"status": "FREE", "symbol": None}]
    with pytest.raises(ValueError, match="not found"):
        slots.free_slot(s, "TCS")


def test_count_status():
    s = [
        {"status": "DEPLOYED", "symbol": "TCS"},
        {"status": "ARMED", "symbol": "INFY"},
        {"status": "FREE", "symbol": None},
    ]
    assert slots.count_status(s, "DEPLOYED") == 1
    assert slots.count_status(s, "FREE") == 1


def test_rotate_to_top_hot_frees_then_assigns():
    s = [{"status": "DEPLOYED", "symbol": "TCS"}, {"status": "FREE", "symbol": None}]
    s = slots.rotate_to_top_hot(s, exiting_symbol="TCS", hot_candidates=["INFY", "WIPRO"])
    assert slots.count_status(s, "DEPLOYED") == 1
    symbols = {slot["symbol"] for slot in s if slot["status"] == "DEPLOYED"}
    assert symbols == {"INFY"}


def test_rotate_to_top_hot_no_candidates_just_frees():
    s = [{"status": "DEPLOYED", "symbol": "TCS"}]
    s = slots.rotate_to_top_hot(s, exiting_symbol="TCS", hot_candidates=[])
    assert s[0] == {"status": "FREE", "symbol": None}
