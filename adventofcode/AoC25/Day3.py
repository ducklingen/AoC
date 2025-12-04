import logging
from pathlib import Path

from adventofcode.helpers.AoCHelper import read_input_lines

path = Path("AoC25") / "Inputs" / "Day3"

logger = logging.getLogger(__name__)


def get_max_voltage(battery: str, length: int) -> int:
    digits = []

    for j in range(length - 1):
        next_digit = max(int(i) for i in battery[: -(length - j - 1)])

        digits.append(next_digit)

        leading_digit_pos = battery.index(str(next_digit))
        battery = battery[leading_digit_pos + 1 :]

        logger.debug(
            f"Found digit {next_digit}, with remaining battery {battery}"
        )

    digits.append(max(int(i) for i in battery))

    logger.debug(f"Max voltage {''.join(map(str, digits))}")
    return int("".join(map(str, digits)))


def solve_one(input_file: str) -> int:
    input = read_input_lines(path / input_file)

    return sum(get_max_voltage(battery, 2) for battery in input)


def solve_two(input_file: str) -> int:
    input = read_input_lines(path / input_file)

    return sum(get_max_voltage(battery, 12) for battery in input)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    res = solve_one("input.txt")
    assert res == 17031, "Part 1 result does not match expected value"
    logger.info(f"Part 1: {res}")

    res = solve_two("input.txt")
    assert res == 168575096286051, "Part 2 result does not match expected value"
    logger.info(f"Part 2: {res}")
