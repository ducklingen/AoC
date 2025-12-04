import logging
from pathlib import Path

from adventofcode.helpers.AoCHelper import read_input_lines

path = Path("AoC25") / "Inputs" / "Day1"

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def solve_one(input_file: str) -> int:
    input_lines = read_input_lines(path / input_file)

    res = 0
    pos = 50

    for line in input_lines:
        dir = line[0]
        length = int(line[1:])

        if dir == "L":
            pos -= length
            pos = pos % 100
        else:
            pos += length
            pos = pos % 100

        if pos == 0:
            res += 1

    return res


def solve_two(input_file: str) -> int:
    input_lines = read_input_lines(path / input_file)

    res = 0
    pos = 50

    for line in input_lines:
        dir = line[0]
        length = int(line[1:])

        res += length // 100
        length = length % 100

        if dir == "L":
            if length > pos and pos != 0:
                res += 1
            pos -= length
            pos = pos % 100
        else:
            if length > 100 - pos and pos != 0:
                res += 1
            pos += length
            pos = pos % 100

        if pos == 0:
            res += 1

    return res


if __name__ == "__main__":
    res = solve_one("input.txt")
    assert res == 989, "Part 1 result does not match expected value"
    logger.info(f"Part 1: {res}")

    res = solve_two("input.txt")
    assert res == 5941, "Part 2 result does not match expected value"
    logger.info(f"Part 2: {res}")
