import logging
from pathlib import Path

from adventofcode.helpers.AoCHelper import read_input_lines, get_neighbours

path = Path("AoC25") / "Inputs" / "Day4"

logger = logging.getLogger(__name__)


def solve_one(input_file: str) -> int:
    input = read_input_lines(path / input_file)
    grid = [list(i) for i in input]

    res = 0

    for i, row in enumerate(grid):
        for j, entry in enumerate(row):
            if entry == "@":
                neighbours = get_neighbours(i, j, grid)
                roll_neighbours = [n for n in neighbours if n == "@"]

                if len(roll_neighbours) < 4:
                    logger.debug(f"Found roll at index ({i},{j}) to pick up")
                    res += 1


    return res

def solve_two(input_file: str) -> int:
    input = read_input_lines(path / input_file)

    res = 0

    return res



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    res = solve_one("input.txt")
    logger.info(f"Part 1: {res}")

    res = solve_two("input.txt")
    logger.info(f"Part 2: {res}")
