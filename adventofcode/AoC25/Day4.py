import logging
import sys
from pathlib import Path

from adventofcode.helpers.AoCHelper import get_neighbours, read_input_lines

path = Path("AoC25") / "Inputs" / "Day4"

logger = logging.getLogger(__name__)


def can_pick_up_roll(entry: str, grid: list[list[str]], i: int, j: int) -> bool:
    if entry == "@":
        neighbours = get_neighbours(i, j, grid)
        roll_neighbours = [n for n in neighbours if n == "@"]

        if len(roll_neighbours) < 4:
            logger.debug(f"Found roll at index ({i},{j}) to pick up")
            return True
        else:
            return False
    return False


def solve_one(input_file: str) -> int:
    input = read_input_lines(path / input_file)
    grid = [list(i) for i in input]

    res = 0

    for i, row in enumerate(grid):
        for j, entry in enumerate(row):
            if can_pick_up_roll(entry, grid, i, j):
                res += 1

    return res


def solve_two(input_file: str) -> int:
    input = read_input_lines(path / input_file)
    grid = [list(i) for i in input]

    res = 0
    rolls_removed = sys.maxsize

    while rolls_removed > 0:
        rolls_removed = 0
        new_grid = []
        for i, row in enumerate(grid):
            new_row = []
            for j, entry in enumerate(row):
                if can_pick_up_roll(entry, grid, i, j):
                    rolls_removed += 1
                    new_row.append(".")
                else:
                    new_row.append(entry)
            new_grid.append(new_row)

        res += rolls_removed
        grid = new_grid

    return res


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    res = solve_one("input.txt")
    assert res == 1502, "Part 1 result does not match expected value"
    logger.info(f"Part 1: {res}")

    res = solve_two("input.txt")
    assert res == 9083, "Part 2 result does not match expected value"
    logger.info(f"Part 2: {res}")
