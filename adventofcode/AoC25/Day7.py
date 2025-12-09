import logging
from pathlib import Path

from adventofcode.helpers.AoCHelper import prod, read_input_lines

path = Path("AoC25") / "Inputs" / "Day7"

logger = logging.getLogger(__name__)


def solve_one(input_file: str) -> int:
    input = read_input_lines(path / input_file)
    res = 0

    for i in range(len(input) - 1):
        logger.debug(f"{input[i]}")

        next_row = list(input[i + 1])
        for j in range(len(input[0])):
            if input[i][j] in ("|", "S"):
                if input[i + 1][j] == ".":
                    next_row[j] = "|"
                else:
                    res += 1
                    next_row[j - 1] = "|"
                    next_row[j + 1] = "|"

        logger.debug(f"{next_row}")
        input[i + 1] = next_row

    return res


def solve_two(input_file: str) -> int:
    input = read_input_lines(path / input_file)
    res = 0

    return res


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    res = solve_one("input.txt")
    logger.info(f"Part 1: {res}")

    res = solve_two("test.txt")
    logger.info(f"Part 2: {res}")
