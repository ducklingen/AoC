import copy
import sys

from helpers.AoCHelper import *
from helpers.GlobalVariables import *

sys.setrecursionlimit(5000)

input_lines = [list(i) for i in read_input_lines("day11/day11input1.txt")]


def process_seats(seats, neighbour_limit, immediate_neighbour):
    new_configuration = copy.deepcopy(seats)

    for i in range(len(seats)):
        for j in range(len(seats[0])):
            seat_status = new_configuration[i][j]

            if new_configuration == ".":
                new_configuration[i][j] = seat_status
                continue

            adjacent_people = list(
                filter(
                    lambda x: x == "#",
                    get_neighbours(
                        i, j, seats, all_directions, immediate_neighbour, ["."]
                    ),
                )
            )

            if seat_status == "L" and len(adjacent_people) == 0:
                new_configuration[i][j] = "#"
            elif seat_status == "#" and len(adjacent_people) >= neighbour_limit:
                new_configuration[i][j] = "L"
            else:
                new_configuration[i][j] = seat_status

    return new_configuration


def find_stable_configuration(
    initial_configuration, neighbour_limit, immediate_neighbour
):
    initial_seats = initial_configuration
    updated_seats = process_seats(
        initial_configuration, neighbour_limit, immediate_neighbour
    )

    while not min([i == j for i, j in zip(initial_seats, updated_seats)]):
        initial_seats = updated_seats
        updated_seats = process_seats(
            initial_seats, neighbour_limit, immediate_neighbour
        )

    return updated_seats


# Part 1
taken_seats = sum(
    [
        seat_row.count("#")
        for seat_row in find_stable_configuration(input_lines, 4, True)
    ]
)
assert taken_seats == 2263
print("Part 1: " + str(taken_seats))

# Part 2
taken_seats = sum(
    [
        seat_row.count("#")
        for seat_row in find_stable_configuration(input_lines, 5, False)
    ]
)
assert taken_seats == 2002
print("Part 2: " + str(taken_seats))
