import math
import re
from functools import wraps
from itertools import product
from math import ceil, cos, radians, sin
from pathlib import Path
from typing import Any

from adventofcode.helpers.GlobalVariables import all_directions


def read_input_lines(
    file_path: str | Path, linebreaks: bool = False
) -> list[str]:
    """Read input lines from a file.

    Parameters
    ----------
    file_path : str | Path
        The path of the file to read from. Given relative to
        the `adventofcode`-folder.
    linebreaks : bool, optional
        Whether to include linebreaks in the output, by default False

    Returns
    -------
    list[str]
        A list of lines from the file.

    """
    path = Path("adventofcode") / file_path
    if linebreaks:
        return [line for line in path.open()]
    else:
        return [line.rstrip("\n") for line in path.open()]


def read_input_comma_line(file_path: str | Path) -> list[str]:
    """Read a single line from a file and split it by commas.

    Parameters
    ----------
    file_path : str | Path
        The path of the file to read from. Given relative to
        the `adventofcode`-folder.

    Returns
    -------
    list[str]
        A list of strings split by commas.

    """
    lines = read_input_lines(file_path)
    return lines[0].split(",")


def read_input_comma_lines(file_path: str | Path) -> list[list[str]]:
    """Read lines from a file and split them by commas.

    Parameters
    ----------
    file_path : str | Path
        The path of the file to read from. Given relative to
        the `adventofcode`-folder.

    Returns
    -------
    list[list[str]]
        A list of lists of strings split by commas.

    """
    lines = read_input_lines(file_path)

    lists = []

    for i in lines:
        lists.append(i.split(","))

    return lists


def prod(ints: list[int]) -> int:
    """Multiply all integers in a list.

    Analogous to the built-in `sum` function.

    Parameters
    ----------
    ints : list[int]
        A list of integers to multiply.

    Returns
    -------
    int
        The product of all integers in the list.

    """
    p = 1
    for i in ints:
        p *= int(i)
    return p


def list_to_string(strings: list[str], separator: str = ""):
    """Convert a list of strings to a single string.

    Wrapper around the built-in `join` function.

    Parameters
    ----------
    strings : list[str]
        A list of strings to join.
    separator : str, optional
        The separator to use when joining the strings, by default "".

    Returns
    -------
    str
        The combined string.

    """
    return separator.join(strings)


def group_lines(inputlines: list[str]) -> list[list[str]]:
    """Group lines by empty lines.

    Parameters
    ----------
    inputlines : list[str]
        A list of strings to group.

    Returns
    -------
    list[list[str]]
        A list of groups of strings.

    """
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


def extract_numbers_from_line(line: str | list[str]) -> list[int]:
    """Extract all integers from a string.

    Catches both positive and negative integers, but not floats. Any float
    appearing in the string will be converted into two integers, e.g.
    "1.5" will be converted into [1, 5].

    Parameters
    ----------
    line : str | list[str]
        The string to extract integers from. If a list of strings is given,
        the first string will be used.

    Returns
    -------
    list[int]
        A list of integers extracted from the string.

    """
    pattern = r"((?<!\d)[+-]?)(\d+)"

    if isinstance(line, str):
        return [int(match.group()) for match in re.finditer(pattern, line)]
    else:
        return [int(match.group()) for match in re.finditer(pattern, line[0])]


def extract_numbers(lines):
    return [extract_numbers_from_line(line) for line in lines]


def get_neighbours(
    i: int,
    j: int,
    grid: list[list],
    directions: list[tuple[int, int]] = all_directions,
    immediate_neighbour: bool = True,
    characters_to_skip: list[str] = None,
):
    if not immediate_neighbour and not characters_to_skip:
        raise ValueError(
            "If immediate_neighbour is False, characters_to_skip must be "
            "provided."
        )

    characters_to_skip = characters_to_skip or []
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


def get_neighbour_coordinates(
    i,
    j,
    grid,
    directions=all_directions,
    immediate_neighbour=True,
    characters_to_skip=None,
):
    characters_to_skip = characters_to_skip or []
    neighbours = []

    for x, y in directions:
        if (
            immediate_neighbour
            and 0 <= i + x < len(grid)
            and 0 <= j + y < len(grid[0])
        ):
            neighbours.append((i + x, j + y))
        else:
            neighbours.append(
                get_first_coordinate_in_direction(
                    i, j, grid, x, y, characters_to_skip
                )
            )

    return [n for n in neighbours if n is not None]


def get_first_coordinate_in_direction(
    i, j, grid, i_increment, j_increment, characters_to_skip
):
    while 0 <= i + i_increment < len(grid) and 0 <= j + j_increment < len(
        grid[0]
    ):
        if grid[i + i_increment][j + j_increment] not in characters_to_skip:
            return (i + i_increment, j + j_increment)
        else:
            i += i_increment
            j += j_increment

    return None


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


def turn_right(coordinates: tuple[int, int], degrees: int) -> tuple[int, int]:
    for _ in range(ceil(degrees / 90)):
        coordinates = (coordinates[1], -coordinates[0])

    return coordinates


# Credit til Patrick
def rotate(coordinates, angle):
    angle_in_radians = radians(angle)
    px, py = coordinates

    qx = cos(angle_in_radians) * px - sin(angle_in_radians) * py
    qy = sin(angle_in_radians) * px + cos(angle_in_radians) * py

    return round(qx), round(qy)


def lcm(a: int, b: int) -> int:
    """Calculate the least common multiple of two integers.

    Analogous to the built-in `math.gcd` function.

    Parameters
    ----------
    a : int
        The first integer.
    b : int
        The second integer.

    Returns
    -------
    int
        The least common multiple of the two integers.

    """
    return abs(a * b) // math.gcd(a, b)


def get_all_combinations(list_of_values, size_of_tuples):
    return [list(x) for x in product(list_of_values, repeat=size_of_tuples)]


def split_lines_into_chunks(lines, delimiters):
    chuncks = []
    chunk = []

    for line in lines:
        if line in delimiters:
            chuncks.append(chunk)
            chunk = []
        else:
            chunk.append(line)

    chuncks.append(chunk)

    return chuncks


def combine_lists(lists):
    """Combine a list of lists into a single list.

    Parameters
    ----------
    lists : list[list]
        A list of lists to combine.

    Returns
    -------
    list
        A single list containing all elements from the input lists.

    """
    return [x for list in lists for x in list]


def is_integer(b: Any) -> bool:
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


def memoize(f: callable) -> callable:
    mem = {}

    @wraps(f)
    def inner(*args: list, **kwargs: dict) -> Any:
        key = to_hashable(*args, **kwargs)
        if key in mem:
            return mem[key]
        result = f(*args, **kwargs)
        mem[key] = result
        return mem[key]

    return inner


def intersection(lst1: list, lst2: list) -> list:
    return list(set(lst1) & set(lst2))


def is_list_sorted(lst: list[int]) -> bool:
    """Check if a list is sorted in ascending or descending order.

    Parameters
    ----------
    lst : list[int]
        The list to check.

    Returns
    -------
    bool
        True if the list is sorted in ascending or descending order, False
        otherwise.

    """
    asc_report = lst.copy()
    asc_report.sort()

    desc_report = lst.copy()
    desc_report.sort(reverse=True)

    return lst in (asc_report, desc_report)


def rotate_matrix(matrix: list[list[str]]) -> list[list[str]]:
    """Rotate a matrix by 90 degrees clockwise.

    Parameters
    ----------
    matrix : list[list[str]]
        The matrix to rotate.

    Returns
    -------
    list[list[str]]
        The rotated matrix.

    """
    return [list(row) for row in zip(*matrix[::-1], strict=True)]


def get_diagonal(matrix: list[list[str]], index: int) -> list[str]:
    """Get elements in diagonal row of a matrix.

    Parameters
    ----------
    matrix : list[list[str]]
        The matrix to get the diagonal from.
    index : int
        The index of the diagonal. 0 is the main diagonal, positive numbers are
        above the main diagonal, negative numbers are below the main diagonal.

    Returns
    -------
    list[str]
        The elements in the diagonal row.

    """
    if index == 0:
        return [matrix[i][i] for i in range(len(matrix))]
    if index > 0:
        return [matrix[i][i + index] for i in range(len(matrix) - index)]
    if index < 0:
        return [matrix[i - index][i] for i in range(len(matrix) + index)]
