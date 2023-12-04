import math
from helpers import AoCHelper
from helpers.AoCHelper import prod

input = AoCHelper.read_input_lines("day3/day3input1.txt")

def treesInSlope(x,y):
    return sum([(input[x*k][y*k % len(input[0])] == '#') for k in range(math.ceil(len(input)/x))])


assert treesInSlope(1, 3) == 181
print("Part 1: " + str(treesInSlope(1, 3)))

numberOfTrees = prod([treesInSlope(x, y) for x, y in [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]])

assert numberOfTrees == 1260601650
print("Part 2: " + str(numberOfTrees))
