from helpers.AoCHelper import *
from codecs import encode, decode
import re

inputlines = read_input_lines('day8/test1.txt')

byteDiff = 0


def escapes(streng):
    return streng.replace('"', '\\"')


for i in inputlines:
    escapedString = '\"' + escapes(re.escape(i)) + '\"'
    print(str(len(escapedString) - len(i)) + ": " + i + " -> " + escapedString)
    byteDiff += len(escapedString) - len(i)

print(byteDiff)