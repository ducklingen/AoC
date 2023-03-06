import math
import re
from itertools import product
from math import radians, sin, cos, ceil

from helpers.GlobalVariables import all_directions


def read_input_lines(filename, linebreaks=False):
    if linebreaks:
        return [line for line in open("Inputs/" + filename)]
    else:
        return [line.rstrip('\n') for line in open("Inputs/" + filename)]


def read_input_comma_line(filename):
    lines = read_input_lines(filename)
    return lines[0].split(',')


def read_input_comma_lines(filename):
    lines = read_input_lines(filename)

    lists = []

    for i in lines:
        lists.append(i.split(','))

    return lists


def prints(i):
    print(str(i))


def prod(ints):
    p = 1
    for i in ints:
        p *= int(i)
    return p


def list_to_string(listofstrings, separator=''):
    string = ''
    for l in listofstrings:
        string += (str(l) + separator)
    return string


def group_lines(inputlines):
    groups = []
    group = []

    for i in inputlines:
        if i == '':
            groups.append(group)
            group = []
        else:
            group.append(i)

    groups.append(group)

    return groups


def extract_numbers_from_line(line):
    pattern = r'((?<!\d)[+-]?)(\d+)'
    return [int(match.group()) for match in re.finditer(pattern, line)]


def extract_numbers(lines):
    return [extract_numbers_from_line(line) for line in lines]


def get_neighbours(i, j, grid, directions=all_directions, immediate_neighbour=True, characters_to_skip=[]):
    neighbours = []

    for x, y in directions:
        if immediate_neighbour and 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]):
            neighbours.append(grid[i + x][j + y])
        else:
            neighbours.append(get_first_in_direction(i, j, grid, x, y, characters_to_skip))

    return neighbours


def get_first_in_direction(i, j, grid, i_increment, j_increment, characters_to_skip):
    while 0 <= i + i_increment < len(grid) and 0 <= j + j_increment < len(grid[0]):
        if grid[i + i_increment][j + j_increment] not in characters_to_skip:
            return grid[i + i_increment][j + j_increment]
        else:
            i += i_increment
            j += j_increment

    return '.'


def turn_right(coordinates, degrees):
    for turn in range(ceil(degrees/90)):
        coordinates = (coordinates[1], -coordinates[0])

    return coordinates


# Credit til Patrick
def rotate(coordinates, angle):
    angle_in_radians = radians(angle)
    px, py = coordinates

    qx = cos(angle_in_radians) * px - sin(angle_in_radians) * py
    qy = sin(angle_in_radians) * px + cos(angle_in_radians) * py

    return round(qx), round(qy)


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


def get_all_combinations(list_of_values, size_of_tuples):
    return [list(x) for x in product(list_of_values, repeat=size_of_tuples)]


def split_lines_into_chunks(lines, delimiters):
    chuncks = []
    chunk = []

    for l in lines:
        if l in delimiters:
            chuncks.append(chunk)
            chunk = []
        else:
            chunk.append(l)

    chuncks.append(chunk)

    return chuncks