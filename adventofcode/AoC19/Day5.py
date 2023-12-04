from adventofcode.helpers import AoCHelper

programToRun = AoCHelper.read_input_comma_line("day5input.txt")


def getNextInstruction(instructionParam):
    return int(instructionParam) % 10


def getParameter(io, paramPos, instructionPos, programToRun):
    iofields = list(io)
    iofields.reverse()
    iofields = iofields + ['0', '0', '0', '0', '0']

    intermediate = int(iofields[paramPos + 1])

    if intermediate == 0:
        return int(programToRun[instructionPos + paramPos])
    elif intermediate == 1:
        return instructionPos + paramPos


def runProgram(programToRun, input):
    instructionPosition = 0

    instruction = getNextInstruction(int(programToRun[instructionPosition]))

    while instruction in (1, 2, 3, 4, 5, 6, 7, 8):

        instructionObject = str(programToRun[instructionPosition])

        if len(instructionObject) > 2:
            firstInput = getParameter(instructionObject, 1, instructionPosition, programToRun)
            secondInput = getParameter(instructionObject, 2, instructionPosition, programToRun)
            output = getParameter(instructionObject, 3, instructionPosition, programToRun)
        else:
            firstInput = int(programToRun[instructionPosition + 1])
            secondInput = int(programToRun[instructionPosition + 2])
            try:
                output = int(programToRun[instructionPosition + 3])
            except IndexError:
                output = 0

        if instruction == 1:
            programToRun[output] = int(programToRun[firstInput]) + int(programToRun[secondInput])
            nextStep = instructionPosition + 4
        if instruction == 2:
            programToRun[output] = int(programToRun[firstInput]) * int(programToRun[secondInput])
            nextStep = instructionPosition + 4
        if instruction == 3:
            programToRun[firstInput] = input
            nextStep = instructionPosition + 2
        if instruction == 4:
            print("Output is " + str(programToRun[firstInput]))
            nextStep = instructionPosition + 2
        if instruction == 5:
            if int(programToRun[firstInput]) != 0:
                nextStep = int(programToRun[secondInput])
            else:
                nextStep = instructionPosition + 3
        if instruction == 6:
            if int(programToRun[firstInput]) == 0:
                nextStep = int(programToRun[secondInput])
            else:
                nextStep = instructionPosition + 3
        if instruction == 7:
            if int(programToRun[firstInput]) < int(programToRun[secondInput]):
                programToRun[output] = 1
            else:
                programToRun[output] = 0
            nextStep = instructionPosition + 4

        if instruction == 8:
            if int(programToRun[firstInput]) == int(programToRun[secondInput]):
                programToRun[output] = 1
            else:
                programToRun[output] = 0
            nextStep = instructionPosition + 4

        instruction = getNextInstruction(programToRun[nextStep])
        instructionPosition = nextStep

    return programToRun


runProgram(programToRun, 5)