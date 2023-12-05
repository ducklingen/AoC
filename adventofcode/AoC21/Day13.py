from helpers import AoCHelper
import time

start_time = time.time()

input_lines = AoCHelper.read_input_lines("day13/input1.txt")
instructions = []
dots = set([])

# Initialization
for i in input_lines:
    if i[:4] == "fold":
        a, b, c = i.split()
        d, n = c.split("=")
        instructions.append((d, int(n)))
    elif i != "":
        x, y = i.split(",")
        dots.add((int(x), int(y)))


def fold(dots, d, n):
    new_dots = set([])

    if d == "x":
        for x, y in dots:
            if x > n:
                new_dots.add((2 * n - x, y))
            else:
                new_dots.add((x, y))

    if d == "y":
        for x, y in dots:
            if y > n:
                new_dots.add((x, 2 * n - y))
            else:
                new_dots.add((x, y))

    return new_dots


easy_dots = fold(dots, instructions[0][0], instructions[0][1])
assert len(easy_dots) == 770
print(f"Part 1: {len(easy_dots)}")


hard_dots = dots.copy()
for d, n in instructions:
    hard_dots = fold(hard_dots, d, n)

for i in range(7):
    line = ""
    for j in range(41):
        if (j, i) in hard_dots:
            line += "#"
        else:
            line += " "

    print(line)


print("--- %s seconds ---" % (time.time() - start_time))
