from adventofcode.helpers import IntcodeComputer
from adventofcode.helpers.AoCHelper import read_input_lines

inputProgramString = read_input_lines("AoC19/Inputs/Day11Input.txt")[0]

inputProgram = inputProgramString.split(",")

computer = IntcodeComputer(inputProgram)

computer.runProgram(0, 0)
