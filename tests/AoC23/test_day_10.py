import pytest

from adventofcode.AoC23.Day10 import compute_one, compute_two


@pytest.mark.parametrize(
    ("filename", "start_pipe", "expected"),
    [("test1", "F", 4), ("test2", "F", 8), ("inputs", "L", 6812)],
)
def test_part_one(filename, start_pipe, expected):
    assert compute_one(filename, start_pipe) == expected


@pytest.mark.skip()
@pytest.mark.parametrize(
    ("filename", "start_pipe", "expected"),
    [("test3", "F", 4), ("test4", "F", 8), ("inputs", "L", 400)],
)
def test_part_two(filename, start_pipe, expected):
    assert compute_two(filename, start_pipe) == expected
