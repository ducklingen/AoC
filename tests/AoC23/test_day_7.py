import pytest

from adventofcode.AoC23.Day7 import classify_hand, compute_one, compute_two

hands_ranking = {"HC": 1, "1P": 2, "2P": 3, "3K": 4, "FH": 5, "4K": 6, "5K": 7}


@pytest.mark.parametrize(
    ("hand", "value"),
    [("QJ64Q", "3K"), ("57874", "1P"), ("TTT66", "FH"), ("4K9KT", "1P")],
)
def test_classify_hand_two(hand, value):
    assert classify_hand(hand, True) == hands_ranking[value]


@pytest.mark.parametrize(
    ("filename", "expected"), [("test1", 6440), ("inputs", 253313241)]
)
def test_compute_one(filename, expected):
    assert compute_one(filename) == expected


@pytest.mark.parametrize(
    ("filename", "expected"), [("test1", 5905), ("inputs", 253362743)]
)
def test_compute_two(filename, expected):
    assert compute_two(filename) == expected
