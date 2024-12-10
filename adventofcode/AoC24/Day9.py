import logging
from itertools import combinations
from pathlib import Path
from copy import deepcopy
import time
import numpy as np

from adventofcode.helpers.AoCHelper import (
    read_input_lines,
)
import math

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

INPUT_FOLDER_PATH = Path("AoC24") / "Inputs" / "Day9"

input = read_input_lines(INPUT_FOLDER_PATH / "input.txt")[0]


data: list[list[int]] = []
id = 0
for i in range(len(input)):
    if int(i) % 2 == 0:
        data.extend([id for _ in range(int(input[int(i)]))])
        id += 1


result_list = []
try:
    for i in range(len(input)):
        if int(i) % 2 == 0:
            for _ in range(int(input[int(i)])):
                result_list.append(data.pop(0))
        else:
            for _ in range(int(input[int(i)])):
                result_list.append(data.pop())
except IndexError:
    print("Finished processing list")

result = sum(idx * i for idx, i in enumerate(result_list))
print(result)

start = time.time()

data: list[list[int]] = []
id = 0
for i in range(len(input)):
    if int(i) % 2 == 0:
        data.append([id for _ in range(int(input[int(i)]))])
        id += 1
    else:
        data.append(["." for _ in range(int(input[int(i)]))])


start_list = data.pop(0)
result_list = deepcopy(start_list)
for i in range(len(data) - 1):
    if i % 2 == 0:
        file = data[len(data) - i - 1]

        for j in range(len(data) - i - 2):
            if j % 2 == 0:
                filled = [d for d in data[j] if d != "."]
                spaces = [d for d in data[j] if d == "."]

                if len(file) <= len(spaces):
                    if i < 40:
                        print(
                            f"Moving {file} from index {len(data) - i - 1} to "
                            f"{data[j]} at index {j}"
                        )
                    data[j] = filled + file + spaces[len(file) :]
                    if i < 40:
                        print(f"Result: {data[j]}")
                    data[len(data) - i - 1] = ["."] * len(file)
                    break


for d in data:
    result_list.extend(d)

print(len(data))
print("00...111...2...333.44.5555.6666.777.888899")
# print("".join(map(str, result_list)))
print("00992111777.44.333....5555.6666.....8888..")
result = sum(idx * int(i) for idx, i in enumerate(result_list) if i != ".")
print(result)
print(f"Part 2 ran in {time.time() - start:2f} seconds")

print(0, start_list, len(start_list))
for i in range(min(20, len(data) // 2)):
    print(i + 1, data[i], len(data[i]))

for _ in range(3):
    print(".")

for i in range(min(20, len(data) // 2)):
    print(
        math.ceil((len(data) - min(20, len(data) // 2) + i + 1) // 2),
        data[len(data) - min(20, len(data) // 2) + i],
        len(data[len(data) - min(20, len(data) // 2) + i]),
    )
