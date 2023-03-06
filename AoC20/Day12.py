import copy
import sys
import math
from helpers.AoCHelper import *
from helpers.GlobalVariables import *

sys.setrecursionlimit(5000)

input_lines = read_input_lines('day12/day12input1.txt')

position = (0, 0)
direction = (1, 0)

for i in input_lines:
    operation = i[0:1]
    value = int(i[1:])

    if cardinal_directions_dict.get(operation, ''):
        position = (position[0] + cardinal_directions_dict[operation][0] * value, position[1] + cardinal_directions_dict[operation][1] * value)
    if operation == 'F':
        position = (position[0] + value * direction[0], position[1] + value * direction[1])
    if operation == 'R':
        direction = rotate(direction, 360 - value)
    if operation == 'L':
        direction = rotate(direction, value)


manhattan_distance = abs(position[0]) + abs(position[1])
assert manhattan_distance == 1148
print("Part 1: " + str(manhattan_distance))

position = (0, 0)
waypoint = (10, 1)

for i in input_lines:
    operation = i[0:1]
    value = int(i[1:])

    if cardinal_directions_dict.get(operation, ''):
        waypoint = (waypoint[0] + cardinal_directions_dict[operation][0] * value,
                    waypoint[1] + cardinal_directions_dict[operation][1] * value)
    if operation == 'F':
        position = (position[0] + value * waypoint[0], position[1] + value * waypoint[1])
    if operation == 'R':
        waypoint = rotate(waypoint, 360 - value)
    if operation == 'L':
        waypoint = rotate(waypoint, value)


manhattan_distance = abs(position[0]) + abs(position[1])
assert manhattan_distance == 52203
print("Part 2: " + str(manhattan_distance))