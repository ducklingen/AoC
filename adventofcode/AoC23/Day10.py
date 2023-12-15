import re

from adventofcode.helpers.AoCHelper import read_input_lines

pipes = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
    "7": [(0, -1), (1, 0)],
    "J": [(-1, 0), (0, -1)],
}


def locate_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                return (i, j)


def compute_pipe(grid, x, y, start_pipe):
    pipe = [(start_pipe, x, y)]
    next_piece = ""
    exit = pipes[start_pipe[0]][0]

    while next_piece != "S":
        x = x + exit[0]
        y = y + exit[1]
        next_piece = grid[x][y]

        if next_piece == "S":
            break
        pipe.append((next_piece, x, y))
        entry = (exit[0] * -1, exit[1] * -1)
        exits = pipes[next_piece].copy()
        exits.remove(entry)
        exit = exits[0]

    return pipe


def compute_one(filename, start_pipe):
    grid = read_input_lines(f"AoC23/Inputs/Day10/{filename}.txt")
    start_x, start_y = locate_start(grid)

    pipe = compute_pipe(grid, start_x, start_y, start_pipe)

    return len(pipe) / 2


def compute_two(filename, start_pipe):
    grid = read_input_lines(f"AoC23/Inputs/Day10/{filename}.txt")

    start_x, start_y = locate_start(grid)
    pipe = compute_pipe(grid, start_x, start_y, start_pipe)

    filtered_grid = [
        ["." for _ in range(len(grid[0]))] for _ in range(len(grid))
    ]
    for type, x, y in pipe:
        filtered_grid[x][y] = type
    filtered_grid[start_x][start_y] = start_pipe
    string_grid = ["".join(list) for list in filtered_grid]

    enclosed_area = 0
    pattern = r"^(L[-]*7)|^(F[-]*J)"
    for line in string_grid:
        enclosed = False
        enclosed_in_line = 0
        for idx, char in enumerate(line):
            if char == "." and enclosed:
                enclosed_in_line += 1
            if char == "|" or re.match(pattern, line[idx:]):
                enclosed = not enclosed

        enclosed_area += enclosed_in_line

    return enclosed_area


if __name__ == "__main__":
    result = compute_one("inputs", "L")
    assert result == 6812
    print(f"Part 1: {result}")
    area = compute_two("inputs", "L")
    assert area == 527
    print(f"Part 2: {area}")
