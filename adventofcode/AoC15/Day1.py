from adventofcode.helpers import AoCHelper

input = AoCHelper.read_input_lines("day1/day1input1.txt")[0]

part_one = input.count("(") - input.count(")")
assert part_one == 280
print(f"Part 1: {part_one}")

part_two = 0
floor = 0
for idx, i in enumerate(input):
    if i == "(":
        floor += 1
    else:
        floor -= 1

    if floor < 0:
        part_two = idx + 1
        break

assert part_two == 1797
print(f"Part 2: {part_two}")
