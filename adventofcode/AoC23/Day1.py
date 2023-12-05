from adventofcode.helpers import AoCHelper
import regex as re

lines = AoCHelper.read_input_lines("Day1/inputs1.txt")

digit_words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

result1 = 0
for l in lines:
    numbers = [int(d) for d in re.findall(r"\d", l)]
    result1 += 10 * numbers[0] + numbers[-1]

assert result1 == 55607
print(f"Part 1: {result1}")

result2 = 0
for l in lines:
    digits = re.findall(
        r"\d|one|two|three|four|five|six|seven|eight|nine", l, overlapped=True
    )
    real_digits = [int(d) if d.isdigit() else digit_words[d] for d in digits]

    result2 += 10 * real_digits[0] + real_digits[-1]

assert result2 == 55291
print(f"Part 2: {result2}")
