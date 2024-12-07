from pathlib import Path
from adventofcode.helpers.AoCHelper import (
    read_input_lines,
    extract_numbers_from_line,
    get_all_combinations,
)
import time

INPUT_FOLDER_PATH = Path("AoC24") / "Inputs" / "Day7"


def plus(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


start_time = time.time()


input_lines = read_input_lines(INPUT_FOLDER_PATH / "input.txt")

result = 0


for i in input_lines:
    expected, *inputs = extract_numbers_from_line(i)

    operations = get_all_combinations(["+", "*", "||"], len(inputs) - 1)

    for op in operations:
        temp_res = inputs[0]
        for idx, o in enumerate(op):
            if o == "+":
                temp_res = plus(temp_res, inputs[idx + 1])
            elif o == "*":
                temp_res = multiply(temp_res, inputs[idx + 1])
            elif o == "||":
                temp_res = concat(temp_res, inputs[idx + 1])

        if temp_res == expected:
            print("Match found with operations:", op)
            result += expected
            break

print(result)
end_time = time.time()

print(f"Duration: {end_time - start_time}")
