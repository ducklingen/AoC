from helpers import AoCHelper
from itertools import product
from sys import maxsize
from queue import PriorityQueue
import time

start_time = time.time()

input_lines = AoCHelper.read_input_lines("day15/input1.txt")

easy_grid = [list(map(int, l)) for l in input_lines]

hard_grid = []

for i in range(len(input_lines) * 5):
    h_line = []
    for j in range(5):
        h_line += [int(n) + j + (i // len(input_lines)) if int(n) + j + (i // len(input_lines)) <= 9 else int(n) + j + (i // len(input_lines)) - 9 for n in input_lines[i % len(input_lines)]]

    hard_grid.append(h_line)


def find_shortest(grid):

    distance = {node: 0 if node == (0,0) else maxsize for node in product(range(len(grid)), range(len(grid[0])))}
    tentative_nodes = PriorityQueue()
    x = y = 0

    while not (x == len(grid) - 1 and y == len(grid[0]) - 1):
        for n, m in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if 0 <= x + n < len(grid) and 0 <= y + m < len(grid[0]):
                if distance[(x, y)] + grid[x + n][y + m] < distance[(x + n, y + m)]:
                    distance[(x + n, y + m)] = distance[(x, y)] + grid[x + n][y + m]
                    tentative_nodes.put((distance[(x + n, y + m)], (x + n, y + m)))

        if not tentative_nodes.empty():
            new_element = tentative_nodes.get()
            x, y = new_element[1]
        else:
            break

    return distance[(len(grid) - 1, len(grid[0]) - 1)]


part_one_res = find_shortest(easy_grid)
assert part_one_res == 592
print(f"Part 1: {part_one_res}")

part_two_res = find_shortest(hard_grid)
assert part_two_res == 2897
print(f"Part 2: {part_two_res}")

print("--- %s seconds ---" % (time.time() - start_time))