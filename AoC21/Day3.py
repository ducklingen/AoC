from helpers import AoCHelper

input = AoCHelper.read_input_lines("day3/input1.txt")
input_lenght = len(input[0])
gamma, epsilon = '', ''

for i in range(input_lenght):
    zeros, ones = 0, 0

    for binary in input:
        if binary[i] == '0':
            zeros += 1
        else:
            ones += 1

    if zeros > ones:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'


print(int(gamma, 2) * int(epsilon, 2))

oxy, co2 = '', ''
filtered_lines_oxy = input.copy()
filtered_lines_c02 = input.copy()
pos = 0
while len(filtered_lines_oxy) > 1:

    ones = sum([int(binary[pos]) for binary in filtered_lines_oxy])

    if ones >= len(filtered_lines_oxy) / 2:
        filtered_lines_oxy = list(filter(lambda binary: binary[pos] == '1', filtered_lines_oxy))
    else:
        filtered_lines_oxy = list(filter(lambda binary: binary[pos] == '0', filtered_lines_oxy))

    pos += 1

oxy = filtered_lines_oxy[0]
print(oxy)

pos = 0
while len(filtered_lines_c02) > 1:

    ones = sum([int(binary[pos]) for binary in filtered_lines_c02])

    if ones >= len(filtered_lines_c02) / 2:
        filtered_lines_c02 = list(filter(lambda binary: binary[pos] == '0', filtered_lines_c02))
    else:
        filtered_lines_c02 = list(filter(lambda binary: binary[pos] == '1', filtered_lines_c02))

    pos += 1

co2 = filtered_lines_c02[0]
print(filtered_lines_c02[0])

print(int(oxy, 2) * int(co2, 2))