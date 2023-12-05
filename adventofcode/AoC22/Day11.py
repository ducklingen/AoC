from collections import Counter
import math

from adventofcode.helpers import AoCHelper

input = AoCHelper.read_input_lines("day11/input1.txt")
monkey_descriptions = AoCHelper.group_lines(input)


def init_game(desc):
    monkeys = []
    for m in desc:
        starting_items = AoCHelper.extract_numbers_from_line(m[1])
        _, operation = m[2].split(" = ")
        divisor = AoCHelper.extract_numbers_from_line(m[3])[0]
        throw_t = AoCHelper.extract_numbers_from_line(m[4])[0]
        throw_f = AoCHelper.extract_numbers_from_line(m[5])[0]
        monkeys.append((starting_items, operation, divisor, throw_t, throw_f))

    return monkeys


def perform_operation(operation, input):
    a, op, b = operation.split(" ")

    if a == "old":
        a = input
    if b == "old":
        b = input

    if op == "+":
        return int(a) + int(b)
    else:
        return int(a) * int(b)


def monkey_turn(monkeys, idx, f, divisor):
    inspections = 0
    monkeys[idx][0].reverse()
    while len(monkeys[idx][0]) > 0:
        item = monkeys[idx][0].pop()
        inspections += 1
        result = perform_operation(monkeys[idx][1], item) // f

        if divisor > 0:
            result = result % divisor

        if result % monkeys[idx][2] == 0:
            monkeys[monkeys[idx][3]][0].append(result)
        else:
            monkeys[monkeys[idx][4]][0].append(result)

    return inspections


def get_result(counter):
    values = list(counter.values())
    values.sort(reverse=True)
    return values[0] * values[1]


# Part 1
monkeys = init_game(monkey_descriptions)
c = Counter()

for _ in range(20):
    for j in range(len(monkeys)):
        c[j] += monkey_turn(monkeys, j, 3, 0)

res = get_result(c)
assert res == 113232
print(f"Part 1: {res}")

# Part 2
monkeys = init_game(monkey_descriptions)
divisor = math.prod([m[2] for m in monkeys])
c = Counter()

for i in range(10000):
    for j in range(len(monkeys)):
        c[j] += monkey_turn(monkeys, j, 1, divisor)

res = get_result(c)
assert res == 29703395016
print(f"Part 2: {res}")
