import logging

import pytest

from adventofcode.AoC23.Day6 import compute_part_one, compute_part_two


@pytest.mark.parametrize(
    ("file", "expected"),
    [
        ("test1", 288),
        ("inputs", 1083852),
    ],
)
def test_part_one(file, expected):
    result = compute_part_one(file)
    assert result == expected
    logging.info(f"Day 6, 2023 Part 1: {result}")


@pytest.mark.parametrize(
    ("file", "expected"),
    [
        ("test1", 71503),
        ("inputs", 23501589),
    ],
)
def test_part_two(file, expected):
    result = compute_part_two(file)
    assert result == expected
    logging.info(f"Day 6, 2023 Part 2: {result}")
