from helpers import AoCHelper

input = AoCHelper.read_input_lines("day5/input1.txt")
lines = AoCHelper.extract_numbers(input)
grid_size = max(AoCHelper.combine_lists(lines))

print(f"Grid size: {grid_size}")


def draw_lines(lines, grid_size, include_diagonals):
    grid = [[0 for j in range(grid_size + 1)] for i in range(grid_size + 1)]

    for line in lines:
        x1, y1, x2, y2 = line

        if x1 == x2:
            for k in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1][k] = grid[x1][k] + 1

        if y1 == y2:
            for k in range(min(x1, x2), max(x1, x2) + 1):
                grid[k][y1] = grid[k][y1] + 1

        if abs(y2 - y1) == abs(x2 - x1) and include_diagonals:
            line_lenght = abs(y2 - y1) + 1

            if x1 < x2 and y1 < y2:
                for i in range(line_lenght):
                    grid[x1 + i][y1 + i] = grid[x1 + i][y1 + i] + 1
            if x1 < x2 and y1 > y2:
                for i in range(line_lenght):
                    grid[x1 + i][y1 - i] = grid[x1 + i][y1 - i] + 1
            if x1 > x2 and y1 < y2:
                for i in range(line_lenght):
                    grid[x1 - i][y1 + i] = grid[x1 - i][y1 + i] + 1
            if x1 > x2 and y1 > y2:
                for i in range(line_lenght):
                    grid[x1 - i][y1 - i] = grid[x1 - i][y1 - i] + 1

    return grid


# Part 1
grid = draw_lines(lines, grid_size, False)
res = sum([i > 1 for i in AoCHelper.combine_lists(grid)])
assert res == 5092
print(f"Part 1: {res}")

# Part 2
grid = draw_lines(lines, grid_size, True)
res = sum([i > 1 for i in AoCHelper.combine_lists(grid)])
assert res == 20484
print(f"Part 2: {res}")
