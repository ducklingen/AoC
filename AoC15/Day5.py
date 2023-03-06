from helpers.AoCHelper import *
import re

input = read_input_lines('day5/input1.txt')
niceStrings = 0
niceStrings2 = 0


def hasThreeVowels(string):
    return sum([string.count(v) for v in ['a', 'e', 'i', 'o', 'u']]) >= 3


def hasConsecutiveLetters(string):
    consecutiveLetters = False
    for i in range(len(string[:-1])):
        if string[i] == string[i+1]:
            consecutiveLetters = True
            break
    return consecutiveLetters


def noNaugthyStrings(string):
    return not (re.search('ab', string) or re.search('cd', string) or re.search('pq', string) or re.search('xy', string))


def hasAlmostNeighboursLetters(string):
    almostNeighbours = False
    for i in range(len(string[:-2])):
        if string[i] == string[i+2]:
            almostNeighbours = True
            break
    return almostNeighbours

def hasDoubleRepeats(string):
    doubleDoubles = False
    for i in range(len(string[:-2])):
        if re.search(string[i:i+2], string[i+2:]):
            print(string[i:i+2] + " found in " + string[i+2:])
            return True
    return doubleDoubles


for i in input:
    niceStrings += hasThreeVowels(i) and hasConsecutiveLetters(i) and noNaugthyStrings(i)
    niceStrings2 += hasAlmostNeighboursLetters(i) and hasDoubleRepeats(i)

print(str(niceStrings))
print(str(niceStrings2))