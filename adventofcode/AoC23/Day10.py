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


def compute_two(filename, start_pipe):
    grid = read_input_lines(f"AoC23/Inputs/Day10/{filename}.txt")

    x, y = locate_start(grid)

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

    filtered_grid = [
        ["." for _ in range(len(grid[0]))] for _ in range(len(grid))
    ]
    print("Dummy grid")

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in [(x, y) for (_, x, y) in pipe]:
                filtered_grid[i][j] = grid[i][j]
            else:
                filtered_grid[i][j] = "."

    print(filtered_grid)
    enclosed_area = 0
    pattern = r"^(L[-]*7)|^(F[-]*J)"
    for line in filtered_grid:
        line = "".join(line)
        print(line)
        enclosed = False
        for idx, char in enumerate(line):
            if char == "." and enclosed:
                print(f"Adding area at position {idx}")
                enclosed_area += 1
            if char == "|" or re.match(pattern, line[idx:]):
                print(
                    f"Moving inside/outside at position {idx} with value {char}"
                )
                enclosed = not enclosed

    return enclosed_area


if __name__ == "__main__":
    area = compute_two("inputs", "L")
    print(area)
