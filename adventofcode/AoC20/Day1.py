from itertools import combinations

from helpers import AoCHelper
from helpers.AoCHelper import prod

input = AoCHelper.read_input_lines("day1/day1input1.txt")


for ints in combinations(map(int, input), 2):
    if sum(ints) == 2020:
        assert prod(ints) == 539851
        print("Part 1: " + str(prod(ints)))
        break

for ints in combinations(map(int, input), 3):
    if sum(ints) == 2020:
        assert prod(ints) == 212481360
        print("Part 2: " + str(prod(ints)))
        break
