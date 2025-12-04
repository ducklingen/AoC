import logging
from pathlib import Path

from adventofcode.helpers.AoCHelper import read_input_lines

path = Path("AoC25") / "Inputs" / "Day3"

logger = logging.getLogger(__name__)


def solve_one(input_file: str) -> int:
    input = read_input_lines(path / input_file)

    res = 0

    for battery in input:
        leading_digit = max(int(i) for i in battery[:-1])
        logger.debug(f"Found leading digit {leading_digit}")

        leading_digit_pos = battery.index(str(leading_digit))
        second_digit = max(int(i) for i in battery[leading_digit_pos + 1 :])

        logger.debug(f"Max voltage {leading_digit}{second_digit}")

        res += leading_digit * 10 + second_digit

    return res


def solve_two(input_file: str) -> int:
    input = read_input_lines(path / input_file)

    res = 0

    for battery in input:
        digits = []

        for j in range(12 - 1):
            leading_digit = max(int(i) for i in battery[: -(12 - j - 1)])

            digits.append(str(leading_digit))

            leading_digit_pos = battery.index(str(leading_digit))
            battery = battery[leading_digit_pos + 1 :]

            logger.debug(
                f"Found digit {leading_digit}, with remaining battery {battery}"
            )

        digits.append(str(max(int(i) for i in battery)))

        logger.debug(f"Max voltage {''.join(digits)}")
        res += int("".join(digits))

    return res


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    res = solve_one("input.txt")
    logger.info(f"Part 1: {res}")

    res = solve_two("input.txt")
    logger.info(f"Part 2: {res}")
