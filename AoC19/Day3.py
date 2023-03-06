import math
import sys

from helpers import AoCHelper

def getPointsFromWire(wire):
    points = []

    x = 0
    y = 0

    for destination in wire:
        direction = destination[0:1]
        length = destination[1:]

        if direction == 'R':
            for j in range(int(length)):
                points.append((x, y))
                x = x + 1

        if direction == 'U':
            for j in range(int(length)):
                points.append((x, y))
                y = y + 1

        if direction == 'L':
            for j in range(int(length)):
                points.append((x, y))
                x = x - 1

        if direction == 'D':
            for j in range(int(length)):
                points.append((x, y))
                y = y - 1

    return points


# wires = AoCHelper.readInputCommaLines("Testdata/Day3Test0.txt")
# wires = AoCHelper.readInputCommaLines("Testdata/Day3Test1.txt")
# wires = AoCHelper.readInputCommaLines("Testdata/Day3Test2.txt")

wires = AoCHelper.read_input_comma_lines("Day3Input.txt")

wire1 = wires[0]
wire2 = wires[1]

points1 = getPointsFromWire(wire1)
points2 = getPointsFromWire(wire2)
intersections = set(points1).intersection(points2)

intersections.remove((0, 0))

stepsTotal = sys.maxsize

for i in intersections:

    steps1 = points1.index(i)
    steps2 = points2.index(i)

    steps = steps1 + steps2

    if steps < stepsTotal:
        stepsTotal = steps

print(stepsTotal)
