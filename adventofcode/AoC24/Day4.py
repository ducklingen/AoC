import logging
import re
from pathlib import Path

from adventofcode.helpers.AoCHelper import (
    get_diagonal,
    read_input_lines,
    rotate_matrix,
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

INPUT_FOLDER_PATH = Path("AoC24") / "Inputs" / "Day4"


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
