from adventofcode.helpers.AoCHelper import (
    extract_numbers_from_line,
    read_input_lines,
)

input = read_input_lines("AoC23/Inputs/Day9/inputs.txt")

result = 0
for line in input:
    start = extract_numbers_from_line(line)
    breakdowns = [start]
    while set(breakdowns[-1]) != {0}:
        numbers = breakdowns[-1]

        diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
        breakdowns.append(diffs)

    add_value = 0
    number_of_breakdowns = len(breakdowns)
    for i in range(number_of_breakdowns - 1):
        new_value = add_value + breakdowns[number_of_breakdowns - i - 2][-1]
        add_value = new_value

    result += add_value

print(result)


result = 0
for line in input:
    start = extract_numbers_from_line(line)
    breakdowns = [start]
    while set(breakdowns[-1]) != {0}:
        numbers = breakdowns[-1]

        diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
        breakdowns.append(diffs)

    subtract_value = 0
    number_of_breakdowns = len(breakdowns)
    for i in range(number_of_breakdowns - 1):
        new_value = breakdowns[number_of_breakdowns - i - 2][0] - subtract_value
        subtract_value = new_value

    result += subtract_value

print(result)
