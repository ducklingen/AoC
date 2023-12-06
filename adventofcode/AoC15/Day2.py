from itertools import combinations

from adventofcode.helpers.AoCHelper import (
    extract_numbers_from_line,
    read_input_lines,
)

input = [
    extract_numbers_from_line(line)
    for line in read_input_lines("AoC15/Inputs/day2/day2input1.txt")
]

paperNeed = 0
ribbonNeed = 0

for line, w, h in input:
    s1 = line * w
    s2 = w * h
    s3 = h * line

    paperNeed += 2 * (s1 + s2 + s3) + min([s1, s2, s3])
    ribbonNeed += line * w * h + 2 * min(
        a + b for a, b in combinations([line, w, h], 2)
    )

assert paperNeed == 1588178
print(f"Part 1: {paperNeed}")

assert ribbonNeed == 3783758
print(f"Part 2: {ribbonNeed}")
