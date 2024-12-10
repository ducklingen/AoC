import logging
from itertools import combinations
from pathlib import Path
import numpy as np

from adventofcode.helpers.AoCHelper import (
    read_input_lines,
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

INPUT_FOLDER_PATH = Path("AoC24") / "Inputs" / "Day8"


def in_grid(position: tuple[int, int], grid: list[list]) -> bool:
    return 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0])


def parse_data(input_lines: list[str]) -> dict[str, list[tuple[int, int]]]:
    data: dict[str, list[tuple[int, int]]] = {}

    for i in range(len(input_lines)):
        for j in range(len(input_lines[0])):
            if input_lines[i][j] != ".":
                char = input_lines[i][j]
                if char not in data:
                    data[char] = [(i, j)]
                else:
                    data[char].append((i, j))

    return data


input_lines = read_input_lines(INPUT_FOLDER_PATH / "input.txt")

data = parse_data(input_lines)


def solve(input_file: str, second_part: bool) -> int:
    input_lines = read_input_lines(INPUT_FOLDER_PATH / input_file)

    data = parse_data(input_lines)
    antinodes: list[tuple[int, int]] = []
    for _, v in data.items():

        if second_part:
            antinodes.extend(v)

        pairs = list(combinations(v, 2))

        for x, y in pairs:
            x = np.array(x)
            y = np.array(y)
            vector = y - x

            antinode_one = x - vector
            antinode_two = y + vector

            while in_grid(antinode_one, input_lines):

                antinodes.append(tuple(antinode_one))
                if second_part:
                    antinode_one = antinode_one - vector
                else:
                    break

            while in_grid(antinode_two, input_lines):

                antinodes.append(tuple(antinode_two))
                if second_part:
                    antinode_two = antinode_two + vector
                else:
                    break

    return len(set(antinodes))


def solve_one(input_file: str) -> int:
    return solve(input_file, False)


def solve_two(input_file: str) -> int:
    return solve(input_file, True)


if __name__ == "__main__":
    res = solve_one("input.txt")
    assert res == 361, f"Test failed: got {res}"
    logging.info(f"Part 1: {res}")

    res = solve_two("input.txt")
    assert res == 1249, f"Test failed: got {res}"
    logging.info(f"Part 2: {res}")
