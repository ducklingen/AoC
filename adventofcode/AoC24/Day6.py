import logging
from copy import deepcopy
from pathlib import Path

from adventofcode.helpers.AoCHelper import (
    read_input_lines,
    turn_right,
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

INPUT_FOLDER_PATH = Path("AoC24") / "Inputs" / "Day6"


class LoopDetected(Exception):
    """Raised when a loop is detected in the patrol path."""


def next_step_out_of_bounds(
    grid: list[list[str]],
    guard_pos: tuple[int, int],
    guard_dir: tuple[int, int],
) -> bool:
    return (
        guard_pos[0] + guard_dir[0] < 0
        or guard_pos[1] + guard_dir[1] < 0
        or guard_pos[0] + guard_dir[0] >= len(grid)
        or guard_pos[1] + guard_dir[1] >= len(grid[0])
    )


def get_guard_position_and_direction(
    grid: list[list[str]],
) -> tuple[tuple[int, int], tuple[int, int]]:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                guard_pos = (i, j)
                guard_dir = (-1, 0)
            elif grid[i][j] == "v":
                guard_pos = (i, j)
                guard_dir = (1, 0)
            elif grid[i][j] == ">":
                guard_pos = (i, j)
                guard_dir = (0, 1)
            elif grid[i][j] == "<":
                guard_pos = (i, j)
                guard_dir = (0, -1)

    return guard_pos, guard_dir


def patrol(
    grid: list[list[str]],
    guard_pos: tuple[int, int],
    guard_dir: tuple[int, int],
) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    inside_grid = True

    path = [(guard_pos, guard_dir)]

    while inside_grid:
        if next_step_out_of_bounds(grid, guard_pos, guard_dir):
            inside_grid = False

        elif grid[guard_pos[0] + guard_dir[0]][guard_pos[1] + guard_dir[1]] in [
            ".",
            ">",
            "<",
            "^",
            "v",
        ]:
            guard_pos = (
                guard_pos[0] + guard_dir[0],
                guard_pos[1] + guard_dir[1],
            )
            if (guard_pos, guard_dir) in path:
                raise LoopDetected("Loop detected in patrol path.")

            path.append((guard_pos, guard_dir))

        else:
            guard_dir = turn_right(guard_dir, 90)

    return path


def solve_one(input_file: str) -> int:
    input_lines = read_input_lines(INPUT_FOLDER_PATH / input_file)
    grid = [list(line) for line in input_lines]

    guard_pos, guard_dir = get_guard_position_and_direction(grid)

    path = patrol(grid, guard_pos, guard_dir)

    res = len(set([pos for pos, _ in path]))

    return res


def solve_two(input_file: str) -> int:
    input_lines = read_input_lines(INPUT_FOLDER_PATH / input_file)
    grid = [list(line) for line in input_lines]

    guard_pos, guard_dir = get_guard_position_and_direction(grid)

    res = 0

    path = patrol(grid, guard_pos, guard_dir)
    unique_positions = set([pos for pos, _ in path])

    positions_checked = 0

    for pos in unique_positions:
        modified_grid = deepcopy(grid)

        modified_grid[pos[0]][pos[1]] = "O"

        try:
            patrol(modified_grid, guard_pos, guard_dir)
        except LoopDetected:
            res += 1
        finally:
            positions_checked += 1

    return res


if __name__ == "__main__":
    res = solve_one("input.txt")
    assert res == 5080, f"Test failed: got {res}"
    logger.info(f"Part 1: {res}")

    res = solve_two("input.txt")
    assert res == 1919, f"Test failed: got {res}"
    logger.info(f"Part 2: {res}")
