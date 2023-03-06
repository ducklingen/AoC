import math
from helpers import AoCHelper
from helpers.AoCHelper import prints

input = AoCHelper.read_input_lines("day5/day5input1.txt")


def beregnSeatId(inputstring):
    rows = range(127)
    for letter in inputstring[0:7]:
        if letter == 'F':
            rows = rows[0:math.ceil(len(rows)/2)-1]
        else:
            rows = rows[math.ceil(len(rows)/2):]

    columns = range(7)
    for letter in inputstring[7:]:
        if letter == 'L':
            columns = columns[0:math.ceil(len(columns)/2)-1]
        else:
            columns = columns[math.ceil(len(columns)/2):]

    return rows.start*8+columns.start


maxSeatId = 0
seatIds = []

for i in input:
    seatId = beregnSeatId(i)

    if seatId > maxSeatId:
        maxSeatId = seatId
    seatIds.append(seatId)

assert maxSeatId == 976
print("Part 1: " + str(maxSeatId))

for j in range(len(seatIds)):
    if j-1 in seatIds and j+1 in seatIds and j not in seatIds:
        assert j == 685
        print("Part 2: " + str(j))



