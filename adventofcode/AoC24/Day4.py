import re
from pathlib import Path

from adventofcode.helpers.AoCHelper import (
    read_input_lines,
)

INPUT_FOLDER_PATH = Path("AoC24") / "Inputs" / "Day4"

input_lines = read_input_lines(INPUT_FOLDER_PATH / "input.txt")

print(f"Found {len(input_lines)} input lines of length {len(input_lines[0])}")

PATTERN = r"XMAS"


def rotate_matrix(matrix: list[list[str]]) -> list[list[str]]:
    return [list(row) for row in zip(*matrix[::-1])]


def get_diagonal(matrix: list[list[str]], index: int) -> list[str]:
    if index == 0:
        return [matrix[i][i] for i in range(len(matrix))]
    if index > 0:
        return [matrix[i][i + index] for i in range(len(matrix) - index)]
    if index < 0:
        return [matrix[i - index][i] for i in range(len(matrix) + index)]


test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(test_matrix)
print(rotate_matrix(test_matrix))

for i in range(-2, 3):
    print(get_diagonal(test_matrix, i))

res = 0

for _ in range(4):
    print("Searching horizontally")
    for idx, line in enumerate(input_lines):
        matches = re.findall(PATTERN, "".join(line))
        res += len(matches)
        if matches:
            print(f"Found {len(matches)} matches in line {idx + 1}")
    print("Searching diagonally")
    for i in range(-len(input_lines) + 1, len(input_lines)):
        matches = re.findall(PATTERN, "".join(get_diagonal(input_lines, i)))
        res += len(matches)
        if matches:
            print(f"Found {len(matches)} matches in diagonal {i}")
    print("Rotating matrix")
    input_lines = rotate_matrix(input_lines)

print(f"Found {res} matches in total")


res = 0
for i in range(len(input_lines)):
    for j in range(len(input_lines[i])):
        if input_lines[i][j] == "A":
            try:
                up_left = input_lines[i - 1][j - 1]
                up_right = input_lines[i - 1][j + 1]
                down_left = input_lines[i + 1][j - 1]
                down_right = input_lines[i + 1][j + 1]

                if (f"{up_left}A{down_right}" in ["SAM", "MAS"]) and (
                    f"{up_right}A{down_left}" in ["SAM", "MAS"]
                ):
                    print(f"Found X-MAS at ({i}, {j}).")
                    res += 1
            except IndexError:
                print(f"({i}, {j}) on border - skipping.")


print(f"Found {res} matches in total")
