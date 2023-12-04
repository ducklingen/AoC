from adventofcode.helpers import AoCHelper

input = AoCHelper.read_input_lines("day10/input1.txt")

cycle_register_values = []
register_value = 1

for i in input:
    cycle_register_values.append(register_value)

    if i != 'noop':
        a, v = i.split()
        val = int(v)

        cycle_register_values.append(register_value)
        register_value += val

sample_idx = [20, 60, 100, 140, 180, 220]
res = sum([i * cycle_register_values[i - 1] for i in sample_idx])
assert res == 16880
print(f"Part 1: {res}")

crt = ['', '', '', '', '', '']
for j in range(240):
    char_to_print = ' '

    if abs(j % 40  - cycle_register_values[j]) <= 1:
        char_to_print = '#'

    crt[j // 40] += char_to_print

for c in crt:
    print(c)