import logging
from pathlib import Path

from adventofcode.helpers.AoCHelper import prod, read_input_lines

path = Path("AoC25") / "Inputs" / "Day6"

logger = logging.getLogger(__name__)


def get_digit_from_the_left(number: int, position: int) -> str | None:
    if len(str(number)) > position:
        return str(number)[position]
    else:
        return None


def combine_digits(digits: list[str | None]) -> int:
    digits_cleaned = [d for d in digits if d]

    for d in digits_cleaned:
        try:
            int(d)
        except Exception as e:
            logger.exception(f"{d} not a digit")

    return int("".join(digits_cleaned))


def solve_one(input_file: str) -> int:
    input = read_input_lines(path / input_file)
    res = 0

    rows = []
    for i in input:
        rows.append([s for s in i.split(" ") if s])

    number_of_calculations = len(rows[0])

    for i in range(number_of_calculations):
        numbers = [int(r[i]) for r in rows[:-1]]
        operation = rows[-1][i]

        if operation == "+":
            res += sum(numbers)
        if operation == "*":
            res += prod(numbers)

    return res


def solve_two(input_file: str) -> int:
    input = read_input_lines(path / input_file)
    res = 0

    rows = []
    for i in input:
        rows.append([s for s in i.split(" ") if s])

    number_of_calculations = len(rows[0])

    for i in range(number_of_calculations):
        normal_numbers = [int(r[i]) for r in rows[:-1]]
        operation = rows[-1][i]

        max_number_magnitude = max(len(str(n)) for n in normal_numbers)
        numbers = []

        for j in range(max_number_magnitude):
            numbers.append(
                combine_digits(
                    get_digit_from_the_left(n, j) for n in normal_numbers
                )
            )

        if operation == "+":
            logger.debug(f"Adding up {numbers}")
            res += sum(numbers)
        if operation == "*":
            logger.debug(f"Multiplying {numbers}")
            res += prod(numbers)

    return res


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    res = solve_one("input.txt")
    logger.info(f"Part 1: {res}")

    res = solve_two("test.txt")
    logger.info(f"Part 2: {res}")
