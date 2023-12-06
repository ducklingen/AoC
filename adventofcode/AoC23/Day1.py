import regex as re

from adventofcode.helpers.AoCHelper import read_input_lines


def combine_ends(numbers: list[int]) -> int:
    return 10 * numbers[0] + numbers[-1]


def compute_part_one(filename):
    lines = read_input_lines(f"AoC23/Inputs/Day1/{filename}.txt")

    result = 0
    for line in lines:
        numbers = [int(d) for d in re.findall(r"\d", line)]
        result += combine_ends(numbers)

    return result


def compute_part_two(filename):
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

    lines = read_input_lines(f"AoC23/Inputs/Day1/{filename}.txt")

    result = 0
    for line in lines:
        digits = re.findall(
            r"\d|one|two|three|four|five|six|seven|eight|nine",
            line,
            overlapped=True,
        )
        real_digits = [
            int(d) if d.isdigit() else digit_words[d] for d in digits
        ]

        result += combine_ends(real_digits)

    return result


if __name__ == "__main__":
    result1 = compute_part_one("inputs1")
    assert result1 == 55607
    print(f"Part 1: {result1}")

    result2 = compute_part_two("inputs1")
    assert result2 == 55291
    print(f"Part 2: {result2}")
