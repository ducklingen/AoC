import logging
import time
from itertools import combinations
from pathlib import Path

from adventofcode.helpers.AoCHelper import (
    extract_numbers_from_line,
    get_all_combinations,
    read_input_lines,
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

INPUT_FOLDER_PATH = Path("AoC24") / "Inputs" / "Day8"

input_lines = read_input_lines(INPUT_FOLDER_PATH / "input.txt")

data: dict[str, list[tuple[int, int]]] = {}

for i in range(len(input_lines)):
    for j in range(len(input_lines[0])):
        if input_lines[i][j] != ".":
            char = input_lines[i][j]
            if char not in data:
                data[char] = [(i, j)]
            else:
                data[char].append((i, j))

antinodes: list[tuple[int, int]] = []
for k, v in data.items():
    print(k, v)

    pairs = list(combinations(v, 2))

    for x, y in pairs:
        print(f"Looking at pair {x} and {y}")
        vector = (y[0] - x[0], y[1] - x[1])
        print(vector)

        an_one = x[0] - vector[0], x[1] - vector[1]
        print(an_one)
        an_two = y[0] + vector[0], y[1] + vector[1]
        print(an_two)

        if 0 <= an_one[0] < len(input_lines) and 0 <= an_one[1] < len(
            input_lines[0]
        ):
            antinodes.append(an_one)
        if 0 <= an_two[0] < len(input_lines) and 0 <= an_two[1] < len(
            input_lines[0]
        ):
            antinodes.append(an_two)


print(len(set(antinodes)))
