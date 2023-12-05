import math
import re
from itertools import product
from math import radians, sin, cos, ceil
from functools import wraps

from adventofcode.helpers.GlobalVariables import all_directions


def read_input_lines(filename, linebreaks=False):
    if linebreaks:
        return [line for line in open("adventofcode/" + filename)]
    else:
        return [line.rstrip("\n") for line in open("adventofcode/" + filename)]


def read_input_comma_line(filename):
    lines = read_input_lines(filename)
    return lines[0].split(",")


def read_input_comma_lines(filename):
    lines = read_input_lines(filename)

    lists = []

    for i in lines:
        lists.append(i.split(","))

    return lists


def prints(i):
    print(str(i))


def prod(ints):
    p = 1
    for i in ints:
        p *= int(i)
    return p


def list_to_string(listofstrings, separator=""):
    string = ""
    for l in listofstrings:
        string += str(l) + separator
    return string


def group_lines(inputlines):
    groups = []
    group = []

    for i in inputlines:
        if i == "":
            groups.append(group)
            group = []
        else:
            group.append(i)

    groups.append(group)

    return groups


def extract_numbers_from_line(line):
    pattern = r"((?<!\d)[+-]?)(\d+)"

    if isinstance(line, str):
        return [int(match.group()) for match in re.finditer(pattern, line)]
    else:
        return [int(match.group()) for match in re.finditer(pattern, line[0])]


def extract_numbers(lines):
    return [extract_numbers_from_line(line) for line in lines]


def get_neighbours(
    i,
    j,
    grid,
    directions=all_directions,
    immediate_neighbour=True,
    characters_to_skip=[],
):
    neighbours = []

    for x, y in directions:
        if (
            immediate_neighbour
            and 0 <= i + x < len(grid)
            and 0 <= j + y < len(grid[0])
        ):
            neighbours.append(grid[i + x][j + y])
        else:
            neighbours.append(
                get_first_in_direction(i, j, grid, x, y, characters_to_skip)
            )

    return neighbours


def get_first_in_direction(
    i, j, grid, i_increment, j_increment, characters_to_skip
):
    while 0 <= i + i_increment < len(grid) and 0 <= j + j_increment < len(
        grid[0]
    ):
        if grid[i + i_increment][j + j_increment] not in characters_to_skip:
            return grid[i + i_increment][j + j_increment]
        else:
            i += i_increment
            j += j_increment

    return "."


def turn_right(coordinates, degrees):
    for turn in range(ceil(degrees / 90)):
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
    return abs(a * b) // math.gcd(a, b)


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


def combine_lists(lists):
    res = []

    for l in lists:
        res += l

    return res


def is_integer(b):
    try:
        int(b)
        return True
    except ValueError:
        return False
    except TypeError:
        return False


def to_hashable(*args, **kwargs):
    if len(kwargs) > 0:
        return to_hashable(*args, *kwargs.items())
    assert len(args) > 0
    if len(args) == 1:
        arg = args[0]
        if isinstance(arg, list):
            return (tuple(to_hashable(a) for a in arg),)
        elif isinstance(arg, set):
            return (tuple(a for a in sorted(arg, key=hash)),)
        elif isinstance(arg, dict):
            return (to_hashable(*arg.items()),)
        elif isinstance(arg, tuple):
            return (arg,)
        return arg
    return tuple(to_hashable(arg) for arg in args)


def memoize(f):
    mem = {}

    @wraps(f)
    def inner(*args, **kwargs):
        key = to_hashable(*args, **kwargs)
        if key in mem:
            return mem[key]
        result = f(*args, **kwargs)
        mem[key] = result
        return mem[key]

    return inner


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
