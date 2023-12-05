import pytest

from adventofcode.helpers import AoCHelper


@pytest.mark.parametrize(
    ("lists", "expected"),
    [([[1]], [1]), ([[1], [2, 3]], [1, 2, 3])],
)
def test_combine_lists(lists, expected):
    assert AoCHelper.combine_lists(lists) == expected
