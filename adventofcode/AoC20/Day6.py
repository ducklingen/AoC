from string import ascii_lowercase

from adventofcode.helpers.AoCHelper import (
    group_lines,
    list_to_string,
    read_input_lines,
)

input = read_input_lines("AoC20/Inputs/day6/day6input1.txt")
groups = group_lines(input)

numberOfYeses = sum([len(set(list_to_string(g))) for g in groups])

assert numberOfYeses == 6625
print("Part 1: " + str(numberOfYeses))
numberOfYeses = 0

for c in ascii_lowercase:
    for g in groups:
        allYes = True
        for i in g:
            if c not in i:
                allYes = False
                break

        numberOfYeses += allYes

assert numberOfYeses == 3360
print(f"Part 2: {numberOfYeses}")
