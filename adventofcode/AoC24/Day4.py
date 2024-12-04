import logging
import re
from pathlib import Path

from adventofcode.helpers.AoCHelper import (
    read_input_lines,
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

INPUT_FOLDER_PATH = Path("AoC24") / "Inputs" / "Day4"


def rotate_matrix(matrix: list[list[str]]) -> list[list[str]]:
    """Rotate a matrix by 90 degrees clockwise.

    Parameters
    ----------
    matrix : list[list[str]]
        The matrix to rotate.

    Returns
    -------
    list[list[str]]
        The rotated matrix.

    """
    return [list(row) for row in zip(*matrix[::-1])]


def get_diagonal(matrix: list[list[str]], index: int) -> list[str]:
    """Get elements in diagonal row of a matrix.

    Parameters
    ----------
    matrix : list[list[str]]
        The matrix to get the diagonal from.
    index : int
        The index of the diagonal. 0 is the main diagonal, positive numbers are
        above the main diagonal, negative numbers are below the main diagonal.

    Returns
    -------
    list[str]
        The elements in the diagonal row.

    """
    if index == 0:
        return [matrix[i][i] for i in range(len(matrix))]
    if index > 0:
        return [matrix[i][i + index] for i in range(len(matrix) - index)]
    if index < 0:
        return [matrix[i - index][i] for i in range(len(matrix) + index)]


def solve_one(input_file: str) -> int:
    input_lines = read_input_lines(INPUT_FOLDER_PATH / input_file)
    pattern = r"XMAS"

    occurences_found = 0

    for _ in range(4):
        for line in input_lines:
            matches = re.findall(pattern, "".join(line))
            occurences_found += len(matches)

        for i in range(-len(input_lines) + 1, len(input_lines)):
            matches = re.findall(pattern, "".join(get_diagonal(input_lines, i)))
            occurences_found += len(matches)

        input_lines = rotate_matrix(input_lines)

    return occurences_found


def solve_two(input_file: str) -> int:
    input_lines = read_input_lines(INPUT_FOLDER_PATH / input_file)

    occurences_found = 0
    for i in range(1, len(input_lines) - 1):
        for j in range(1, len(input_lines[i]) - 1):
            if input_lines[i][j] == "A":
                up_left = input_lines[i - 1][j - 1]
                up_right = input_lines[i - 1][j + 1]
                down_left = input_lines[i + 1][j - 1]
                down_right = input_lines[i + 1][j + 1]

                if (f"{up_left}A{down_right}" in ["SAM", "MAS"]) and (
                    f"{up_right}A{down_left}" in ["SAM", "MAS"]
                ):
                    occurences_found += 1
    return occurences_found


if __name__ == "__main__":
    res = solve_one("input.txt")
    assert res == 2591, f"Test failed: got {res}"
    logger.info(f"Part 1: {res}")

    res = solve_two("input.txt")
    assert res == 1880, f"Test failed: got {res}"
    logger.info(f"Part 2: {res}")
