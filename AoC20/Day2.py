import math
from helpers import AoCHelper
from helpers.AoCHelper import prints

input = AoCHelper.read_input_lines("day2/day2input1.txt")


def validPassword1(input):
    range, char, password = input.split( )
    min, max = map(int, range.split('-'))
    character = char.replace(':', '')

    return min <= password.count(character) <= max


def validPassword2(input):
    range, char, password = input.split( )
    first, second = map(int, range.split('-'))
    character = char.replace(':', '')

    return (list(password)[first-1] == character) ^ (list(password)[second-1] == character)


validPasswords1 = sum([validPassword1(i) for i in input])
validPasswords2 = sum([validPassword2(i) for i in input])

assert validPasswords1 == 538
print("Part 1: " + str(validPasswords1))
assert validPasswords2 == 489
print("Part 2: " + str(validPasswords2))
