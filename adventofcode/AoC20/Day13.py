import copy
import sys
import math
from helpers.AoCHelper import *
from helpers.GlobalVariables import *

sys.setrecursionlimit(5000)

# Part 1
input_lines = read_input_lines("day13/day13input1.txt")
earliest_departure = int(input_lines[0])
busses = extract_numbers_from_line(input_lines[1])
departure = sys.maxsize
p1 = 0

for b in busses:
    first_valid_depature = math.ceil(earliest_departure / b) * b

    if first_valid_depature < departure:
        departure = first_valid_depature
        p1 = b * (departure - earliest_departure)

assert p1 == 333
print("Part 1: " + str(p1))

# Part 2


def get_next_departure(min_departure, bus_id):
    return math.ceil(min_departure / bus_id) * bus_id


def run_part_two(file_name):
    input_line = read_input_lines("day13/" + file_name + ".txt")[1].split(",")
    bus_ids = extract_numbers_from_line(
        read_input_lines("day13/" + file_name + ".txt")[1]
    )
    first_id = bus_ids[0]
    departure_gaps = {}
    gap = 0

    for i in input_line:
        gap += 1

        if i != "x":
            currentId = i
            departure_gaps[int(currentId)] = gap - 1

    possible_departure = 0
    current_idx = 0
    step = first_id

    while True:
        current_bus = bus_ids[current_idx]
        next_bus = bus_ids[current_idx + 1]

        valid_departure = True

        for g in departure_gaps:
            if (departure_gaps[g] + possible_departure) % g != 0:
                valid_departure = False

        if valid_departure:
            break
        else:
            if min(
                [
                    (departure_gaps[bus] + possible_departure) % bus == 0
                    for bus in [current_bus, next_bus]
                ]
            ):
                if lcm(step, bus_ids[current_idx]) > step:
                    step = lcm(step, bus_ids[current_idx])
                current_idx += 1

            possible_departure += int(step)

    return possible_departure


t0 = run_part_two("day13test0")
assert t0 == 1068781
# print(t0)
t1 = run_part_two("day13test1")
assert t1 == 3417
# print(t1)
t2 = run_part_two("day13test2")
assert t2 == 754018
# print(t2)
t3 = run_part_two("day13test3")
assert t3 == 779210
# print(t3)
t4 = run_part_two("day13test4")
assert t4 == 1261476
# print(t4)
t5 = run_part_two("day13test5")
assert t5 == 1202161486
# print(t5)


p2 = run_part_two("day13input1")
assert p2 == 690123192779524
print("Part 2: " + str(p2))
