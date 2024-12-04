from collections import Counter
from pathlib import Path

from adventofcode.helpers.AoCHelper import read_input_lines

path = Path("AoC24")

cwd = Path.cwd()
print(cwd)

input_lines = read_input_lines(path / "Inputs" / "Day1" / "input.txt")

left = []
right = []

for i in input_lines:
    l, r = i.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

res = 0

for l, r in zip(left, right):
    res += abs(r - l)

print(res)

c = Counter(right)

res = 0
for i in left:
    res += i * c[i]

print(res)
