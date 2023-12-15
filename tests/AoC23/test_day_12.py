import pytest

from adventofcode.AoC23.Day12 import compute_one


@pytest.mark.parametrize(
    ("filename", "expected"), [("test1", 21), ("inputs", 7622)]
)
def test_compute_one(filename, expected):
    assert compute_one(filename) == expected
