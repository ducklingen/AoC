routes = read_input_lines('day3/input1.txt')


class Santa:
    x = 0
    y = 0

    def __init__(self):
        self.x = 0
        self.y = 0

    def nextHouse(self, direction):
        if direction == '<':
            self.x -= 1
        elif direction == '>':
            self.x += 1
        elif direction == '^':
            self.y += 1
        else:
            self.y -= 1

        return self.x, self.y

    def reset(self):
        self.x = 0
        self.y = 0


houses = ["x0y0"]

santa = Santa()

x = 0
y = 0
for d in routes[0]:
    (x,y) = santa.nextHouse(d)

    houses.append("x" + str(x) + "y" + str(y))

part_one = len(set(houses))
assert part_one == 2572
print(f"Part 1: {part_one}")

houses = ["x0y0"]

santa = Santa()
roboSanta = Santa()

x = 0
y = 0
for idx, d in enumerate(routes[0]):
    if idx % 2 == 0:
        (x, y) = santa.nextHouse(d)
    else:
        (x, y) = roboSanta.nextHouse(d)

    houses.append("x" + str(x) + "y" + str(y))

part_two = len(set(houses))
assert part_two == 2631
prints(f"Part 2: {part_two}")