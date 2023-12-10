from adventofcode.helpers.AoCHelper import get_neighbours, read_input_lines

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


def compute_one(filename, start_pipe):
    grid = read_input_lines(f"AoC23/Inputs/Day10/{filename}.txt")

    x, y = locate_start(grid)

    pipe = [start_pipe]
    next_piece = ""
    exit = pipes[start_pipe][0]

    while next_piece != "S":
        x = x + exit[0]
        y = y + exit[1]
        next_piece = grid[x][y]

        if next_piece == "S":
            break
        pipe.append(next_piece)
        entry = (exit[0] * -1, exit[1] * -1)
        exits = pipes[next_piece].copy()
        exits.remove(entry)
        exit = exits[0]

    print(pipe)

    return len(pipe) / 2
