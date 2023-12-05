import sys

from helpers.AoCHelper import *
from helpers.GlobalVariables import *

sys.setrecursionlimit(5000)


def decimal_to_binary(n, expand=False):
    if expand:
        binary = bin(n).replace("0b", "")
        leading_zeros = 36 - len(binary)
        return "0" * leading_zeros + binary
    else:
        return bin(n).replace("0b", "")


def write_to_adresses(value, position, mask):
    position_as_binary = decimal_to_binary(position, True)
    masked_position = mask_value(position_as_binary, mask, "0")

    for comb in get_all_combinations([0, 1], masked_position.count("X")):
        idx = 0
        new_position = ""
        for i in range(len(mask)):
            if masked_position[i] == "X":
                new_position += str(comb[idx])
                idx += 1
            else:
                new_position += masked_position[i]

        memory[new_position] = value


def mask_value(value_to_mask, mask, char_to_ignore):
    new_value = ""
    for i in range(len(mask)):
        if mask[i] != char_to_ignore:
            new_value += mask[i]
        else:
            new_value += value_to_mask[i]

    return new_value


# Part 1
input_lines = read_input_lines("day14/day14input1.txt")
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
memory = {}

for i in input_lines:
    if i[:3] == "mem":
        position, value = extract_numbers_from_line(i)
        value_as_binary = decimal_to_binary(value, True)
        masked_value = int(mask_value(value_as_binary, mask, "X"), 2)
        memory[position] = masked_value

    else:
        mask = i[7:]

p1 = sum(memory.values())
assert p1 == 11612740949946
print("Part 1: " + str(p1))

# Part 2
input_lines = read_input_lines("day14/day14input1.txt")
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
memory = {}

for i in input_lines:
    if i[:3] == "mem":
        position, value = extract_numbers_from_line(i)
        value_as_binary = decimal_to_binary(value, True)
        write_to_adresses(value, position, mask)
    else:
        mask = i[7:]

p2 = sum(memory.values())
assert p2 == 3394509207186
print("Part 2: " + str(p2))
