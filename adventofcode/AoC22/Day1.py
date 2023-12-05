from adventofcode.helpers import AoCHelper

input = AoCHelper.read_input_lines("day1/input1.txt")
groups = AoCHelper.group_lines(input)


def get_top_n(items, n):
    items.sort(reverse=True)
    return items[:n]


# Part 1
res = max([sum(map(int, g)) for g in groups])
assert res == 67450
print(f"Part 1: {res}")

# Part 2
res = sum(get_top_n([sum(map(int, g)) for g in groups], 3))
assert res == 199357
print(f"Part 2: {res}")
