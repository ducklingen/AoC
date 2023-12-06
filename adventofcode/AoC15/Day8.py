import re

from adventofcode.helpers.AoCHelper import read_input_lines

inputlines = read_input_lines("AoC15/Inputs/day8/test1.txt")

byteDiff = 0


def escapes(streng):
    return streng.replace('"', '\\"')


for i in inputlines:
    escapedString = '"' + escapes(re.escape(i)) + '"'
    print(str(len(escapedString) - len(i)) + ": " + i + " -> " + escapedString)
    byteDiff += len(escapedString) - len(i)

print(byteDiff)
