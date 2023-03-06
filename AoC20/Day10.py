from itertools import combinations
import sys
from helpers.AoCHelper import *

sys.setrecursionlimit(5000)

## Part 1
inputlines = list(map(int, read_input_lines('day10/day10input1.txt')))
inputlines.append(0)
inputlines.sort()

output_joltage = 0
initial_output_joltage = -1
one_jolt_differences = 0
three_jolt_differences = 0

while initial_output_joltage != output_joltage:
    initial_output_joltage = output_joltage
    for i in inputlines:
        if i == output_joltage + 1:
            output_joltage = i
            one_jolt_differences += 1
        elif i == output_joltage + 2:
            output_joltage = i
        elif i == output_joltage + 3:
            output_joltage = i
            three_jolt_differences += 1


assert one_jolt_differences * (three_jolt_differences + 1) == 1690
print("Part 1: " + str(one_jolt_differences * (three_jolt_differences + 1)))

## Part 2
input_lines_reversed = list(map(int, read_input_lines('day10/day10input1.txt')))
input_lines_reversed.append(0)
input_lines_reversed.sort(reverse=True)
branch_numbers = {}


for i in input_lines_reversed:
    continuations = list(filter(lambda x: i < x <= i+3, inputlines))

    if len(continuations) > 0:
        branch_numbers[i] = sum([branch_numbers[j] for j in continuations])
    else:
        branch_numbers[i] = 1

assert branch_numbers[0] == 5289227976704
print("Part 2: " + str(branch_numbers[0]))
