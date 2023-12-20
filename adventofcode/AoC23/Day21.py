import logging

from adventofcode.helpers.AoCHelper import (
    get_neighbour_coordinates,
    read_input_lines,
)
from adventofcode.helpers.GlobalVariables import cardinal_directions


def locate_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                return (i, j)


def compute_one(filename: str, steps: int) -> int:
    grid = read_input_lines(f"AoC23/Inputs/Day21/{filename}.txt")
    x, y = locate_start(grid)

    logging.debug(f"Start: ({x},{y})")
    possible_locations = {(x, y)}
    for _ in range(steps):
        new_locations = set([])

        for i, j in possible_locations:
            neighbours = get_neighbour_coordinates(
                i, j, grid, cardinal_directions
            )

            for n in neighbours:
                x = int(n[0])
                y = int(n[1])
                if grid[x][y] != "#":
                    new_locations.add((x, y))

        possible_locations = new_locations

    return len(possible_locations)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    res = compute_one("inputs", 64)
    logging.info(f"Part 1: {res}")
