import logging
from pathlib import Path

from adventofcode.helpers.AoCHelper import read_input_lines

path = Path("AoC25") / "Inputs" / "Day2"

logger = logging.getLogger(__name__)


def is_invalid_one(id: str) -> bool:
    if len(id) % 2 == 0:
        half = len(id) // 2
        if id[:half] == id[half:]:
            logger.debug(f"Found invalid ID: {id}")
            return True

    return False


def is_invalid_two(id: str, divisors: list[int] | None = None) -> bool:
    id_length = len(id)

    divisors = [i for i in range(1, id_length + 1) if id_length % i == 0]

    for d in divisors:
        split = [id[d * i : d * (i + 1)] for i in range(id_length // d)]
        if len(set(split)) == 1 and len(split) > 1:
            logger.debug(f"{id} is split of {split}")
            return True

    return False


def solve_one(input_file: str) -> int:
    input = read_input_lines(path / input_file)[0]

    ranges = input.split(",")
    ranges = [r for r in ranges if r]

    res = 0

    for r in ranges:
        logger.debug(f"Processing range {r}")
        start, end = map(int, r.split("-"))

        for i in range(start, end + 1):
            i_as_string = str(i)
            if is_invalid_one(i_as_string):
                res += i

    return res


def solve_two(input_file: str) -> int:
    input = read_input_lines(path / input_file)[0]

    ranges = input.split(",")
    ranges = [r for r in ranges if r]

    res = 0

    for r in ranges:
        logger.debug(f"Processing range {r}")
        start, end = map(int, r.split("-"))

        for i in range(start, end + 1):
            i_as_string = str(i)
            if is_invalid_two(i_as_string):
                res += i

    return res


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    res = solve_one("input.txt")
    assert res == 32976912643, "Part 1 result does not match expected value"
    logger.info(f"Part 1: {res}")

    res = solve_two("input.txt")
    assert res == 54446379122, "Part 2 result does not match expected value"
    logger.info(f"Part 2: {res}")
