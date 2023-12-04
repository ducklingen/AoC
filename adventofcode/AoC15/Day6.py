instructions = read_input_lines('day6/input1.txt')

grid = [[0 for i in range(1000)] for j in range(1000)]


def numberOfLitLights(grid):
    litLights = 0
    for column in grid:
        for row in column:
            litLights += row
    return litLights


def turnOnLights(a, b, x, y):
    for i in range(a, x+1):
        for j in range(b, y+1):
            grid[i][j] += 1


def toggleLights(a, b, x, y):
    for i in range(a,x+1):
        for j in range(b, y+1):
            grid[i][j] += 2


def turnOffLights(a, b, x, y):
    for i in range(a,x+1):
        for j in range(b, y+1):
            if grid[i][j] > 0:
                grid[i][j] -= 1
            else:
                grid[i][j] = 0

for inst in instructions:
    a, b, x, y = extract_numbers_from_line(inst)

    if re.search('turn on', inst):
        turnOnLights(a, b, x, y)
    elif re.search('turn off', inst):
        turnOffLights(a, b, x, y)
    elif re.search('toggle', inst):
        toggleLights(a, b, x, y)

    print(inst)
    print(str(numberOfLitLights(grid)))

print(str(numberOfLitLights(grid)))

