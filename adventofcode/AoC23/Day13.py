from adventofcode.helpers.AoCHelper import group_lines, read_input_lines

input = read_input_lines("AoC23/Inputs/Day13/inputs.txt")
grids = group_lines(input)

result = 0
for grid in grids:
    grid_result = -1
    for i in range(len(grid)):
        closest_border = min(i, len(grid) - i - 2) + 1

        if closest_border == 0:
            continue

        if (
            min([grid[i - j] == grid[i + j + 1] for j in range(closest_border)])
            == 1
        ):
            grid_result = (i + 1) * 100
            break

    if grid_result <= 0:
        width = len(grid[0])
        for k in range(width):
            closest_border = min(k, width - k - 2) + 1
            if closest_border == 0:
                continue

            if (
                min(
                    [
                        [r[k - j] for r in grid] == [r[k + j + 1] for r in grid]
                        for j in range(closest_border)
                    ]
                )
                == 1
            ):
                grid_result = k + 1
                break

    result += grid_result

print(result)
