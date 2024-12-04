import pytest

from adventofcode.helpers import AoCHelper


@pytest.mark.parametrize(
    ("lists", "expected"),
    [([[1]], [1]), ([[1], [2, 3]], [1, 2, 3])],
)
def test_combine_lists(lists, expected):
    assert AoCHelper.combine_lists(lists) == expected


def test_rotate_matrix():
    input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    assert AoCHelper.rotate_matrix(input_matrix) == expected_matrix


@pytest.mark.parametrize(
    ("index", "expected"),
    [(0, [1, 5, 9]), (1, [2, 6]), (-1, [4, 8]), (2, [3]), (-2, [7])],
)
def test_get_diagonal(index, expected):
    input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    assert AoCHelper.get_diagonal(input_matrix, index) == expected


def test_extract_numbers_from_line():
    input_string = "hre-1gregaw23hjtshjr3,4"
    assert AoCHelper.extract_numbers_from_line(input_string) == [-1, 23, 3, 4]
