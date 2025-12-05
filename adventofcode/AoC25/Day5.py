import logging
from pathlib import Path

from adventofcode.helpers.AoCHelper import group_lines, read_input_lines

path = Path("AoC25") / "Inputs" / "Day5"

logger = logging.getLogger(__name__)


def solve_one(input_file: str) -> int:
    input = read_input_lines(path / input_file)
    ranges, ids = group_lines(input)

    res = 0

    for id in ids:
        for r in ranges:
            start, end = map(int, r.split("-"))
            if start <= int(id) <= end:
                logger.debug(f"ID {id} is valid for range {r}")
                res += 1
                break

    return res


def solve_two(input_file: str) -> int:
    input = read_input_lines(path / input_file)
    ranges_as_string, _ = group_lines(input)
    ranges = sorted(
        [tuple(map(int, r.split("-"))) for r in ranges_as_string],
        key=lambda x: x[0],
    )

    aggregated_ranges: list[tuple[int, int]] = []

    for start, end in ranges:
        new_aggregated_ranges = aggregated_ranges.copy()

        overlap = False

        for aggregate_range in aggregated_ranges:
            agg_start, agg_end = aggregate_range

            if agg_start <= start <= agg_end:
                new_aggregated_ranges.remove((agg_start, agg_end))
                new_aggregated_ranges.append((agg_start, max(agg_end, end)))
                overlap = True
                break

        if not overlap:
            new_aggregated_ranges.append((start, end))

        aggregated_ranges = new_aggregated_ranges

    return sum(end - start + 1 for start, end in aggregated_ranges)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    res = solve_one("input.txt")
    assert res == 726, "Part 1 result does not match expected value"
    logger.info(f"Part 1: {res}")

    res = solve_two("input.txt")
    assert res == 354226555270043, "Part 2 result does not match expected value"
    logger.info(f"Part 2: {res}")
