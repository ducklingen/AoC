import logging
import time
from pathlib import Path

from adventofcode.helpers.AoCHelper import (
    extract_numbers_from_line,
    get_all_combinations,
    read_input_lines,
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

INPUT_FOLDER_PATH = Path("AoC24") / "Inputs" / "Day7"


def plus(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


def solve(input_file: str, available_operations: list[str]) -> int:

    input_lines = read_input_lines(INPUT_FOLDER_PATH / input_file)

    result = 0

    for i in input_lines:
        expected, *inputs = extract_numbers_from_line(i)

        operations = get_all_combinations(available_operations, len(inputs) - 1)

        for op in operations:
            temp_res = inputs[0]
            for idx, o in enumerate(op):
                temp_res = o(temp_res, inputs[idx + 1])

                if temp_res > expected:
                    break

            if temp_res == expected:
                result += expected
                break

    return result


if __name__ == "__main__":
    start_time = time.time()
    res = solve("input.txt", [multiply, plus])
    assert res == 1298300076754, f"Test failed: got {res}"
    logger.info(f"Part 1: {res}")
    time_one = time.time()
    logger.info(f"Solved part 1 in {time_one - start_time:.3f} seconds.")

    res = solve("input.txt", [concat, multiply, plus])
    assert res == 248427118972289, f"Test failed: got {res}"
    logger.info(f"Part 2: {res}")
    logger.info(f"Solved part 2 in {time.time() - time_one:.3f} seconds.")
