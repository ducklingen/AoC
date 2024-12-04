from adventofcode.helpers.AoCHelper import read_input_lines, extract_numbers_from_line, prod
from pathlib import Path
from collections import Counter
import re
path = Path("AoC24")
cwd = Path.cwd()
print(cwd)

input_lines = read_input_lines(path / "Inputs" / "Day3" / "inputs.txt")

print(input_lines)

pattern = r"(mul\(\-?\d{1,3},\-?\d{1,3}\))"

cleaned_data = []
for input_line in input_lines:
    cleaned_data.extend([match.group() for match in re.finditer(pattern, input_line)])

res = 0
for d in cleaned_data:
    print(d)
    numbers = extract_numbers_from_line(d)

    assert len(numbers) == 2
    assert all(-1000 < x < 1000 for x in numbers)

    res += numbers[0] * numbers[1]

print(res)

input_line = read_input_lines(path / "Inputs" / "Day3" / "inputs.txt")[0]

cleaned_data = []
dos = input_line.split("do()")
for d in dos:
    print(d)
    if "don't()" in d:
        do, *_ = d.split("don't()")
    else:
        do = d
    cleaned_data.extend([match.group() for match in re.finditer(pattern, do)])

res = 0
for d in cleaned_data:
    print(d)
    numbers = extract_numbers_from_line(d)

    assert len(numbers) == 2
    assert all(-1000 < x < 1000 for x in numbers)

    res += numbers[0] * numbers[1]

print(res)