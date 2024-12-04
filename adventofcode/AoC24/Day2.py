from pathlib import Path

from adventofcode.helpers.AoCHelper import (
    extract_numbers_from_line,
    read_input_lines,
)

path = Path("AoC24")

cwd = Path.cwd()
print(cwd)

input_lines = read_input_lines(path / "Inputs" / "Day2" / "input.txt")

safe = 0


def safe_report(report: list[int]) -> bool:
    asc_report = report.copy()
    asc_report.sort()

    desc_report = report.copy()
    desc_report.sort(reverse=True)

    if report not in (asc_report, desc_report):
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


for i in input_lines:
    report = extract_numbers_from_line(i)
    safe += safe_report_two(report)


print(safe)
