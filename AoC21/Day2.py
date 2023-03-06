from helpers import AoCHelper

input = AoCHelper.read_input_lines("day2/input1.txt")


def calculate_naive_position(input_lines):
    h_pos, v_pos = 0, 0

    for i in input_lines:
        direction, distance = i.split(' ')

        if direction == 'forward':
            h_pos += int(distance)
        if direction == 'up':
            v_pos -= int(distance)
        if direction == 'down':
            v_pos += int(distance)

    return h_pos*v_pos


def calculate_position_with_aim(input_lines):
    h_pos, v_pos, aim = 0, 0, 0

    for i in input_lines:
        direction, distance = i.split(' ')

        if direction == 'forward':
            h_pos += int(distance)
            v_pos += (aim * int(distance))
        if direction == 'up':
            aim -= int(distance)
        if direction == 'down':
            aim += int(distance)

    return h_pos*v_pos


naive_position = calculate_naive_position(input)
assert naive_position == 1690020
print (f"Part 1: {naive_position}")


position_with_aim = calculate_position_with_aim(input)
assert position_with_aim == 1408487760
print(f"Part 2: {position_with_aim}")


