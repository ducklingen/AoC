from itertools import combinations

from adventofcode.helpers.AoCHelper import read_input_lines

inputlines = list(map(int, read_input_lines("day9/day9input1.txt")))
preambleLength = 25


def find_invalid_number(lines):
    for i in range(preambleLength, len(lines)):
        valid = False

        for j, k in combinations(lines[i - preambleLength : i], 2):
            if j + k == lines[i]:
                valid = True
                break

        if not valid:
            return lines[i]


special_number = find_invalid_number(inputlines)
assert special_number == 10884537
print("Part 1:", str(special_number))


def find_contiguous_set(lines, target_number):
    for i in range(len(lines)):
        j = i + 1
        i_value = lines[i]

        while i_value < target_number:
            i_value += lines[j]
            j += 1

            if i_value == target_number:
                return i, j


range_start, range_end = find_contiguous_set(inputlines, special_number)
p2 = max(inputlines[range_start:range_end]) + min(
    inputlines[range_start:range_end]
)

assert p2 == 1261309
print("Part 2: " + str(p2))
