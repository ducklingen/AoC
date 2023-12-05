from math import ceil, floor, sqrt
from typing import Tuple

from adventofcode.helpers import AoCHelper


def compute_borders(time, record) -> Tuple[int, int]:
    disc = time * time - 4 * (record + 1)
    lower = max(0, ceil((time - sqrt(disc)) / 2))
    upper = min(time, floor((time + sqrt(disc)) / 2))

    return (lower, upper)


def compute_part_one(filename):
    input = AoCHelper.read_input_lines(f"AoC23/Inputs/Day6/{filename}.txt")
    times = AoCHelper.extract_numbers_from_line(input[0])
    records = AoCHelper.extract_numbers_from_line(input[1])
    games = list(zip(times, records))

    result = 1

    for g in games:
        time, record = g
        lower, upper = compute_borders(time, record)

        result *= upper - lower + 1

    return result


def compute_part_two(filename):
    input = AoCHelper.read_input_lines(f"AoC23/Inputs/Day6/{filename}.txt")
    full_time = int(
        "".join([str(t) for t in AoCHelper.extract_numbers_from_line(input[0])])
    )
    full_record = int(
        "".join([str(r) for r in AoCHelper.extract_numbers_from_line(input[1])])
    )

    lower, upper = compute_borders(full_time, full_record)

    return upper - lower + 1


if __name__ == "__main__":
    result1 = compute_part_one("inputs")
    assert result1 == 1083852
    print(f"Part 1: {result1}")

    result2 = compute_part_two("inputs")
    assert result2 == 23501589
    print(f"Part 2: {result2}")
