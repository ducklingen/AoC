from helpers import AoCHelper

input = AoCHelper.read_input_lines("day4/input1.txt")

res1 = res2 = 0
for i in input:
    n1, n2 = i.split(',')

    a, b = map(int, n1.split('-'))
    c, d = map(int, n2.split('-'))

    res1 += a <= c <= d <= b or c <= a <= b <= d
    res2 += not(b < c or d < a)


assert res1 == 542
print(f"Part 1: {res1}")

assert res2 == 900
print(f"Part 2: {res2}")