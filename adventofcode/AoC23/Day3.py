from adventofcode.helpers import AoCHelper, GlobalVariables
import re
import logging


def has_adjacent_symbols(x: int, y: int, len: int, engine) -> bool:
    digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

    directions = GlobalVariables.all_directions.copy()

    if len > 1:
        directions.remove((0, 1))
        neighbours = AoCHelper.get_neighbours(x, y, engine, directions)

        directions.remove((0, -1))
        for i in range(len - 1):
            neighbours += AoCHelper.get_neighbours(x, y + i, engine, directions)

        directions.append((0, 1))
        neighbours += AoCHelper.get_neighbours(
            x, y + len - 1, engine, directions
        )

        if set(neighbours) - digits != {"."}:
            return True
    else:
        neighbours = AoCHelper.get_neighbours(x, y, engine, directions)

    return set(neighbours) - digits != {"."}


def compute_part_one(filename):
    engine = AoCHelper.read_input_lines(f"AoC23/Inputs/Day3/{filename}.txt")
    result = 0
    for row_id, row in enumerate(engine):
        pattern = r"([1-9]\d*)"

        numbers = [
            (int(match.group()), match.start())
            for match in re.finditer(pattern, row)
        ]

        for n, idx in numbers:
            logging.info(f"Checking number {n}")
            if has_adjacent_symbols(row_id, idx, len(str(n)), engine):
                result += n

    return result


def adjecent_number(gp: int, idx: int, x: str) -> bool:
    return gp <= idx <= gp + 1 or gp <= idx + len(x) <= gp + len(x)


def compute_part_two(filename):
    engine = AoCHelper.read_input_lines(f"AoC23/Inputs/Day3/{filename}.txt")
    result = 0

    for row_id, row in enumerate(engine):
        gear_pattern = r"(\*)"
        gear_positions = [
            match.start() for match in re.finditer(gear_pattern, row)
        ]

        number_pattern = r"([1-9]\d*)"
        adjecent_numbers = []

        logging.info(
            f"Found gear in row {row_id} at positions {gear_positions}"
        )
        for gp in gear_positions:
            numbers = []
            # Finding number above
            if row_id > 0:
                numbers += [
                    (match.group(), match.start())
                    for match in re.finditer(number_pattern, engine[row_id - 1])
                ]

            # Finding numbers to the side
            numbers += [
                (match.group(), match.start())
                for match in re.finditer(number_pattern, engine[row_id])
            ]

            # Finding numbers below
            if row_id + 1 < len(engine):
                numbers += [
                    (match.group(), match.start())
                    for match in re.finditer(number_pattern, engine[row_id + 1])
                ]

            adjecent_numbers = [
                int(x) for x, idx in numbers if adjecent_number(gp, idx, x)
            ]

            logging.info(
                f"Gear at position ({row_id}, {gp}) has adjecent numbers: {adjecent_numbers}"
            )
            if len(adjecent_numbers) == 2:
                result += AoCHelper.prod(adjecent_numbers)

    return result


if __name__ == "__main__":
    result1 = compute_part_one("inputs1")
    assert result1 == 546312
    print(f"Part 1: {result1}")

    result2 = compute_part_two("inputs1")
    assert result2 == 87449461
    print(f"Part 2: {result2}")
