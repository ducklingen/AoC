from helpers import AoCHelper

input = AoCHelper.read_input_lines("day1/input1.txt")
numbers = list(map(int, input))


def simpleIncreases(input_numbers):
    return sum(
        [
            input_numbers[i] < input_numbers[i + 1]
            for i in range(len(input_numbers) - 1)
        ]
    )


def rollingSumIncreases(input_numbers):
    return sum(
        [
            input_numbers[i] < input_numbers[i + 3]
            for i in range(len(input_numbers) - 3)
        ]
    )


simpleIncreases = simpleIncreases(numbers)
assert simpleIncreases == 1162
print(f"Part 1: {simpleIncreases}")

rollingSumIncreases = rollingSumIncreases(numbers)
assert rollingSumIncreases == 1190
print(f"Part 2: {rollingSumIncreases}")
