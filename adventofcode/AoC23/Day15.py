from adventofcode.helpers.AoCHelper import read_input_lines

input = read_input_lines("AoC23/Inputs/Day15/inputs.txt")[0]

result = 0
init_sequence = input.split(",")


def compute_hash(string: str) -> int:
    hash = 0
    for c in string:
        hash += ord(c)
        hash = hash * 17
        hash = hash % 256

    return hash


for init in init_sequence:
    result += compute_hash(init)

print(result)
