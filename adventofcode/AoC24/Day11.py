from adventofcode.helpers.AoCHelper import extract_numbers_from_line
from functools import lru_cache


TEST = "125 17"
INPUT = "3 386358 86195 85 1267 3752457 0 741"

input = extract_numbers_from_line(INPUT)


@lru_cache
def process_number(number: int) -> list[int]:
    if number == 0:
        return [1]
    if len(str(number)) % 2 == 0:
        length = len(str(number))
        return [
            int(str(number)[: length // 2]),
            int(str(number)[length // 2 :]),
        ]
    else:
        return [number * 2024]


for i in range(25):
    new_list = []
    for j in input:
        new_list.extend(process_number(j))
    input = new_list

    print(f"Blinked {i + 1} times")

print(len(input))
