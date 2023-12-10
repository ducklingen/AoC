import pytest

from adventofcode.AoC23.Day10 import compute_one


@pytest.mark.parametrize(
    ("filename", "start_pipe", "expected"),
    [("test1", "F", 4), ("test2", "F", 8), ("inputs", "L", 6812)],
)
def test_part_one(filename, start_pipe, expected):
    assert compute_one(filename, start_pipe) == expected
