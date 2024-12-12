from functools import lru_cache
import time
from adventofcode.helpers.AoCHelper import combine_lists

TEST = [125, 17]
INPUT = [3, 386358, 86195, 85, 1267, 3752457, 0, 741]


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


@lru_cache
def process_list(input: tuple[int], step: int) -> list[int]:
    new_list = []
    for _ in range(step):
        new_list = tuple(combine_lists([process_number(j) for j in input]))
        input = new_list
    return input


def process(input: list[int], n: int, max: int, step: int = 1) -> int:
    if n == max:
        return len(input)

    new_list = process_list(tuple(input), step)

    if len(new_list) >= 50:
        return process(new_list[:25], n + step, max) + process(
            new_list[25:], n + step, max
        )

    return process(new_list, n + step, max)


# print(process(INPUT, 0, 50, 5))
for i in range(6):
    start = time.time()
    print(process(INPUT, 0, i * 5, 5))
    print(f"Blinked {i * 5} times in {time.time() - start: 2f} seconds")
