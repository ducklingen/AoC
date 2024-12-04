import re
from pathlib import Path

from adventofcode.helpers.AoCHelper import (
    extract_numbers_from_line,
    read_input_lines,
)

INPUT_FOLDER_PATH = Path("AoC24") / "Inputs" / "Day3"


def extract_operations_from_line(line: str) -> list[str]:
    pattern = r"(mul\(\-?\d{1,3},\-?\d{1,3}\))"
    return [match.group() for match in re.finditer(pattern, line)]


def perform_operation(operation: str) -> int:
    numbers = extract_numbers_from_line(operation)
    return numbers[0] * numbers[1]


def solve_one(input_file: str) -> int:
    input_line = read_input_lines(input_file)[0]

    cleaned_data = extract_operations_from_line(input_line)
    return sum(perform_operation(op) for op in cleaned_data)


def solve_two(input_file: str) -> int:
    input_line = read_input_lines(input_file)[0]

    cleaned_data = []
    dos = input_line.split("do()")
    for d in dos:
        do = d.split("don't()")[0]
        cleaned_data.extend(extract_operations_from_line(do))

    return sum(perform_operation(op) for op in cleaned_data)


if __name__ == "__main__":
    res = solve_one(INPUT_FOLDER_PATH / "inputs.txt")
    assert res == 183669043, f"Test failed: got {res}"
    print(f"Part 1: {res}")

    res = solve_two(INPUT_FOLDER_PATH / "inputs.txt")
    assert res == 59097164, f"Test failed: got {res}"
    print(f"Part 2: {res}")
