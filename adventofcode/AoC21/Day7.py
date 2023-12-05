from helpers import AoCHelper

input = AoCHelper.read_input_lines("day7/input1.txt")
numbers = AoCHelper.extract_numbers_from_line(input)

min_sum_easy = min(
    sum(abs(n - k) for k in numbers) for n in range(max(numbers) + 1)
)
assert min_sum_easy == 336701
print(f"Part 1: {min_sum_easy}")

min_sum_hard = min(
    sum(abs(n - k) * (abs(n - k) + 1) / 2 for k in numbers)
    for n in range(max(numbers) + 1)
)
assert min_sum_hard == 95167302
print(f"Part 2: {min_sum_hard}")
