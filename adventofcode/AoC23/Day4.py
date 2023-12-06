from collections import Counter

from adventofcode.helpers import AoCHelper


def identify_matches(card: str) -> int:
    winners, mine = card.split("|")
    winning_numbers = AoCHelper.extract_numbers_from_line(winners)
    my_numbers = AoCHelper.extract_numbers_from_line(mine)

    return len(set(winning_numbers).intersection(my_numbers))


def parse_cards(filename: str) -> list[str]:
    input = AoCHelper.read_input_lines(f"AoC23/Inputs/Day4/{filename}.txt")

    return [i[8:] for i in input]


def compute_one(filename: str) -> int:
    result = 0

    for c in parse_cards(filename):
        matches = identify_matches(c)
        if matches > 0:
            result += 2 ** (matches - 1)

    return result


def compute_two(filename: str) -> int:
    cards = parse_cards(filename)
    counter = Counter({i: 1 for i in range(len(cards))})
    for idx, c in enumerate(cards):
        matches = identify_matches(c)

        counter += {idx + i + 1: counter[idx] for i in range(matches)}

    return sum(counter.values())


if __name__ == "__main__":
    result = compute_one("inputs1")
    assert result == 23847
    print(f"Part 1: {result}")
    result2 = compute_two("inputs1")
    assert result2 == 8570000
    print(f"Part 2: {result2}")
