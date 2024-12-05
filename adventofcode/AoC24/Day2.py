from pathlib import Path

from adventofcode.helpers.AoCHelper import (
    extract_numbers_from_line,
    is_list_sorted,
    read_input_lines,
)

INPUT_FILE_PATH = Path("AoC24") / "Inputs" / "Day2"


input_lines = read_input_lines(INPUT_FILE_PATH / "input.txt")

safe = 0


def safe_report(report: list[int]) -> bool:
    if not is_list_sorted(report):
        return False

    for j in range(len(report) - 1):
        if not (0 < abs(report[j] - report[j + 1]) < 4):
            return False

    return True


def safe_report_two(report: list[int]) -> bool:
    for i in range(len(report)):
        dampened_report = report.copy()
        del dampened_report[i]
        if safe_report(dampened_report):
            return True

    return False


def solve_one(input_file: str) -> int:
    read_input_lines(INPUT_FILE_PATH / input_file)

    return sum(safe_report(extract_numbers_from_line(i)) for i in input_lines)


def solve_two(input_file: str) -> int:
    read_input_lines(INPUT_FILE_PATH / input_file)

    return sum(
        safe_report_two(extract_numbers_from_line(i)) for i in input_lines
    )


if __name__ == "__main__":
    res = solve_one("input.txt")
    assert res == 371, f"Test failed: got {res}"
    print(f"Part one: {res}")

    res = solve_two("input.txt")
    assert res == 426, f"Test failed: got {res}"
    print(f"Part two: {res}")
