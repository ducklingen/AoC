from helpers.AoCHelper import *

inputlines = read_input_lines('day8/day8input1.txt')


def alter_program(index, program):
    new_program = [x for x in program]
    operation = program[index]

    if operation[0:3] == 'jmp':
        new_program[index] = operation.replace('jmp', 'nop')
    elif operation[0:3] == 'nop':
        new_program[index] = operation.replace('nop', 'jmp')

    return new_program


def execute_operation(index, operation, accumulator):
    if operation[0:3] == 'acc':
        accumulator += extract_numbers_from_line(operation)[0]
        index += 1
    elif operation[0:3] == 'jmp':
        index += extract_numbers_from_line(operation)[0]
    else:
        index += 1

    return accumulator, index


def run_program(program):
    current_line, accumulator, visited_lines, terminated = [0, 0, set(), False]

    while current_line not in visited_lines and current_line < len(program):
        visited_lines.add(current_line)
        accumulator, current_line = execute_operation(current_line, program[current_line], accumulator)

    if current_line >= len(program):
        terminated = True

    return accumulator, terminated


# Part 1
assert run_program(inputlines)[0] == 1744
print("Part 1: " + str(run_program(inputlines)[0]))

# Part 2
for i in range(len(inputlines)):
    accumulator, terminated = run_program(alter_program(i, read_input_lines('day8/day8input1.txt')))

    if terminated:
        assert accumulator == 1174
        print("Part 2: " + str(accumulator))
        break
