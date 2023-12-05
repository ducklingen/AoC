from adventofcode.helpers import AoCHelper


def runProgram(programToRun):
    start = 0

    while int(programToRun[start]) in (1, 2):
        operation = int(programToRun[start])

        firstInput = int(programToRun[start + 1])
        secondInput = int(programToRun[start + 2])

        if operation == 1:
            programToRun[int(programToRun[start + 3])] = int(
                programToRun[firstInput]
            ) + int(programToRun[secondInput])
        if operation == 2:
            programToRun[int(programToRun[start + 3])] = int(
                programToRun[firstInput]
            ) * int(programToRun[secondInput])

        start = start + 4

    return programToRun


def printProcessedInput(programToRun):
    processedInput = runProgram(programToRun)

    outputOfProgram = ",".join(map(str, processedInput))

    print(outputOfProgram)


def getOutputOfProces(programToRun):
    return runProgram(programToRun)[0]


# printProcessedInput([1,0,0,0,99])
# printProcessedInput([2,3,0,3,99])
# printProcessedInput([2,4,4,5,99,0])
# printProcessedInput([1,1,1,4,99,5,6,0,99])

for i in range(99):
    for j in range(99):
        program = AoCHelper.read_input_comma_line("Day2Input.txt")

        program[1] = i
        program[2] = j

        output = getOutputOfProces(program)

        if output == 19690720:
            print(100 * i + j)
