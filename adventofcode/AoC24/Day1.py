from collections import Counter
from pathlib import Path

from adventofcode.helpers.AoCHelper import read_input_lines

path = Path("AoC24") / "Inputs" / "Day1"


def parse_input(lines: list[str]) -> tuple[list[int], list[int]]:
    left = []
    right = []

    for i in lines:
        l, r = i.split()  # noqa: E741
        left.append(int(l))
        right.append(int(r))

    return left, right


def solve_one(input_file: str) -> int:
    input_lines = read_input_lines(path / input_file)
    left, right = parse_input(input_lines)

    left.sort()
    right.sort()

    return sum(abs(l - r) for l, r in zip(left, right, strict=True))  # noqa: E741


def solve_two(input_file: str) -> int:
    input_lines = read_input_lines(path / input_file)
    left, right = parse_input(input_lines)

    c = Counter(right)

    return sum(i * c[i] for i in left)


if __name__ == "__main__":
    res = solve_one("input.txt")
    assert res == 2742123, f"Test failed: got {res}"
    print(f"Part 1: {res}")

    res = solve_two("input.txt")
    assert res == 21328497, f"Test failed: got {res}"
    print(f"Part 2: {res}")
