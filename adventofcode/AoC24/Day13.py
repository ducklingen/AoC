import logging
from pathlib import Path

from adventofcode.helpers.AoCHelper import (
    extract_numbers_from_line,
    group_lines,
    read_input_lines,
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

INPUT_FOLDER_PATH = Path("AoC24") / "Inputs" / "Day13"
ADD = 10_000_000_000_000


def parse_game(
    game: list[str],
) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    if len(game) != 3:
        raise ValueError(f"Invalid game: {game}. Expected 3 lines")

    a, d = extract_numbers_from_line(game[0])
    b, e = extract_numbers_from_line(game[1])
    c, f = extract_numbers_from_line(game[2])

    return (a, b, c), (d, e, f)


def solve_equations(
    a: int, b: int, c: int, d: int, e: int, f: int
) -> tuple[int, int]:
    if b != 0 and (b * d - a * e) != 0:
        x = (f - (e * c) / b) * (b / (b * d - a * e))
        y = (c - a * x) / b

        x, y = clean_solution(x, y)
        return x, y

    else:
        raise ValueError(
            f"Can not solve the equation: {a}x + {b}y = {c}, {d}x + {e}y = {f}"
        )


def clean_solution(x: float, y: float) -> tuple[int, int]:
    if abs(x - round(x)) < 1e-3:
        x = float(round(x))
    if abs(y - round(y)) < 1e-3:
        y = float(round(y))

    if x >= 0 and y >= 0 and x.is_integer() and y.is_integer():
        return int(x), int(y)
    else:
        raise ValueError(f"({x}, {y}) is not a valid solution")


def solve(input_file: str, part_two: bool):
    input_data = read_input_lines(INPUT_FOLDER_PATH / input_file)
    games = group_lines(input_data)

    res = 0
    for g in games:
        (a, b, c), (d, e, f) = parse_game(g)

        if part_two:
            c = c + ADD
            f = f + ADD

        try:
            x, y = solve_equations(a, b, c, d, e, f)
            res += 3 * x + y
        except ValueError as e:
            logger.debug(e)

    return res


if __name__ == "__main__":
    res = solve("input.txt", part_two=False)
    assert res == 37_297, f"Test failed: got {res}"
    logger.info(f"Part 1: {res}")

    res = solve("input.txt", part_two=True)
    assert res == 83_197_086_729_371, f"Test failed: got {res}"
    logger.info(f"Part 2: {res}")
