from math import ceil

from adventofcode.helpers import AoCHelper

input = AoCHelper.read_input_lines("day3/input1.txt")


def letter_value(char):
    if 65 <= ord(char) < 97:
        return ord(char) - 38
    else:
        return ord(char) - 96


res = 0
for i in input:
    left, right = list(i)[: ceil(len(i) / 2)], list(i)[ceil(len(i) / 2) :]
    common_element = AoCHelper.intersection(left, right)[0]
    res += letter_value(common_element)

assert res == 7908
print(f"Part 1: {res}")


res = 0
for i in range(ceil(len(input) / 3)):
    a, b, c = input[i * 3 : i * 3 + 3]
    common_element = list(set(a) & set(b) & set(c))[0]
    res += letter_value(common_element)

assert res == 2838
print(f"Part 2: {res}")
