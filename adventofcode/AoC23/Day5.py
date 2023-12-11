import logging
import sys
from math import ceil

from adventofcode.helpers.AoCHelper import (
    extract_numbers_from_line,
    group_lines,
    read_input_lines,
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

input = read_input_lines("AoC23/Inputs/Day5/test1.txt")
initial_seeds = extract_numbers_from_line(input[0])
logging.info(initial_seeds)

groups = group_lines(input[2:])


def transform_positions_min(initial_positions, groups):
    min = sys.maxsize * 2 + 1
    for s in initial_positions:
        for g in groups:
            new_pos = s
            for t in g[1:]:
                dest, src, rng = extract_numbers_from_line(t)

                if src <= s <= src + rng - 1:
                    new_pos = s + (dest - src)

            s = new_pos

        if s < min:
            min = s

    return min


# result = transform_positions_min(initial_seeds, groups)
# assert result == 650599855
# logging.info(f"Part 1: {result}")

initial_ranges = [
    (initial_seeds[i * 2], initial_seeds[i * 2] + initial_seeds[i * 2 + 1])
    for i in range(ceil(len(initial_seeds) / 2))
]

print(initial_ranges)

for g in groups:
    for t in g[1:]:
        dest, src, rng = extract_numbers_from_line(t)
        print(f"Moving ({src}, {src+rng}) to ({dest}, {dest+rng})")
        translation = dest - src
        new_ranges = []
        for start, end in initial_ranges:
            print(f"--- Transforming ({start}, {end}) ---")
            # INTERIOR
            if start > src and end < src + rng:
                nr = (start + translation, end + translation)
                print(f"Interior: Adding {nr}")
                new_ranges.append(nr)
                start = end = -1
            # LOWER
            elif start < src and src <= end < src + rng:
                nr = (dest, dest + (end - src))
                rm = (start, src)
                print(f"Lower: Adding {nr}, {rm}")
                new_ranges.append(nr)
                new_ranges.append(rm)
            # UPPER
            elif src <= start < src + rng and end >= src + rng:
                nr = (start + translation, dest + rng)
                rm = (src + rng, end)
                print(f"Upper: Adding {nr}, {rm}")
                new_ranges.append(nr)
                new_ranges.append(rm)
            # EXTERIOR
            elif start <= src and end >= src + rng:
                nr = (dest, dest + rng)
                rm1 = (start, src)
                rm2 = (src + rng, end)
                print(f"Exterior: Adding {nr}, {rm1}, {rm2}")
                new_ranges.append(nr)
                new_ranges.append(rm1)
                new_ranges.append(rm2)
            else:
                print(f"Unchanged: Adding ({start},{end})")
                new_ranges.append((start, end))

        print(f"New ranges: {new_ranges}")
        initial_ranges = new_ranges
# logging.info(f"Part 2: {result}")

print(min([x[0] for x in initial_ranges]))
