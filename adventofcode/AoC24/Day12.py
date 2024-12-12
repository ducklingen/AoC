import logging
from dataclasses import dataclass
from pathlib import Path

from adventofcode.helpers.AoCHelper import (
    read_input_lines,
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

INPUT_FOLDER_PATH = Path("AoC24") / "Inputs" / "Day12"

N = (0, -1)
E = (1, 0)
S = (0, 1)
W = (-1, 0)


def safe_get(
    grid: list[list[str]],
    pos: tuple[int, int],
    default: str = None,
) -> str:
    try:
        if pos[0] < 0 or pos[1] < 0:
            return default
        return grid[pos[0]][pos[1]]
    except IndexError:
        return default


@dataclass
class Garden:
    """Model representing a garden.

    Holds information about which positions are in the garden
    and what type of flower is planted in the garden.

    The `perimeter_lenght` method calculates the perimeter of the garden.
    """

    area: set[tuple[int, int]]
    flower_type: str

    def perimeter_lenght(self) -> int:
        perimeter_lenght = 0
        for pos in self.area:
            if (pos[0] - 1, pos[1]) not in self.area:
                perimeter_lenght += 1
            if (pos[0], pos[1] + 1) not in self.area:
                perimeter_lenght += 1
            if (pos[0] + 1, pos[1]) not in self.area:
                perimeter_lenght += 1
            if (pos[0], pos[1] - 1) not in self.area:
                perimeter_lenght += 1

        return perimeter_lenght


def get_garden(gardens: list[Garden], pos: tuple[int, int]) -> Garden:
    for garden in gardens:
        if pos in garden.area:
            return garden

    return None


def solve_one(input_file: str) -> int:
    input_lines = read_input_lines(INPUT_FOLDER_PATH / input_file)

    gardens: list[Garden] = []

    for i in range(len(input_lines)):
        for j in range(len(input_lines[i])):
            flower_type = input_lines[i][j]

            north = safe_get(input_lines, (i - 1, j))
            west = safe_get(input_lines, (i, j - 1))

            if north == flower_type:
                garden = get_garden(gardens, (i - 1, j))
                garden.area.add((i, j))

                # Handles the case where a garden is not connected
                # above in the outerleft corner and thus have been
                # created as a separate garden, e.g. the X's below
                #
                # AAXA
                # AXXA
                # BBBB
                #
                if west == flower_type:
                    additonal_garden = get_garden(gardens, (i, j - 1))

                    if garden != additonal_garden:
                        garden.area.update(additonal_garden.area)
                        gardens.remove(additonal_garden)
            elif west == flower_type:
                garden = get_garden(gardens, (i, j - 1))
                garden.area.add((i, j))
            else:
                gardens.append(Garden({(i, j)}, flower_type))

    for garden in gardens:
        logging.debug(
            f"Garden {garden.area} of size {len(garden.area)} with flowers "
            f"{garden.flower_type} and perimeter {garden.perimeter_lenght()}"
        )

    res = sum(
        garden.perimeter_lenght() * len(garden.area) for garden in gardens
    )
    logging.info(res)
    return res


if __name__ == "__main__":
    assert solve_one("test1.txt") == 140
    assert solve_one("test2.txt") == 772
    assert solve_one("test3.txt") == 1930
    assert solve_one("input.txt") == 1465112
