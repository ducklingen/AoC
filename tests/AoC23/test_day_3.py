from adventofcode.AoC23.Day3 import compute_part_one, compute_part_two, adjecent_number
import pytest


@pytest.mark.parametrize(
    ("file", "expected"),
    [
        ("test1", 4361),
        ("test2", 413),
        ("test3", 925),
        ("test4", 554003),
        ("inputs1", 546312),
    ],
)
def test_part_one(file, expected):
    assert compute_part_one(file) == expected


@pytest.mark.parametrize(
    ("file", "expected"),
    [
        ("test1", 467835),
        ("test2", 6756),
        ("test3", 6756),
        ("test4", 87263515),
        ("inputs1", 87449461),
    ],
)
def test_part_two(file, expected):
    assert compute_part_two(file) == expected


@pytest.mark.parametrize(
    ("gp", "idx", "x", "expected"),
    [(7, 3, "123", False), (63, 61, "123", True), (63, 62, "123", True)],
)
def test_adjacent_number(gp, idx, x, expected):
    assert adjecent_number(gp, idx, x) == expected
