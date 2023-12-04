from adventofcode.helpers import AoCHelper
from itertools import permutations


def runDay7Program(input1, input2):
    programDefinition = AoCHelper.readInputCommaLine("day7input.txt")

    return IntcodeComputer.runProgram(programDefinition, [input1, input2])


combinations = permutations([0, 1, 2, 3, 4])

maxThrust = 0

for c in combinations:
    outputA = runDay7Program(c[0], 0)[0]
    outputB = runDay7Program(c[1], outputA)[0]
    outputC = runDay7Program(c[2], outputB)[0]
    outputD = runDay7Program(c[3], outputC)[0]
    outputE = runDay7Program(c[4], outputD)[0]

    if outputE > maxThrust:
        maxThrust = outputE

print(maxThrust)
