import logging
from collections import Counter
from functools import cmp_to_key
from typing import Dict

from adventofcode.helpers.AoCHelper import read_input_lines

cards_ranking = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def parse_hands(filename: str) -> Dict[str, str]:
    lines = read_input_lines(f"AoC23/Inputs/Day7/{filename}.txt")
    players = {hand: bet for hand, bet in map(lambda x: x.split(), lines)}

    return players


def classify_hand(hand: str, part_two: bool = False) -> int:
    c = Counter(list(hand))
    jokers = c["J"] * int(part_two)
    if part_two:
        del c["J"]

    if jokers == 5 or max(c.values()) + jokers == 5:
        return 7
    if max(c.values()) + jokers == 4:
        return 6
    if max(c.values()) + jokers == 3:
        if (
            jokers == 1
            and len([x for x in c.values() if x == 2]) == 2
            or jokers == 0
            and 2 in c.values()
        ):
            return 5
        else:
            return 4
    if max(c.values()) + jokers == 2:
        if len([x for x in c.values() if x == 2]) == 2:
            return 3
        else:
            return 2
    return 1


def compare(hand1: str, hand2: str, part_two: bool = False) -> int:
    rank1 = classify_hand(hand1, part_two)
    rank2 = classify_hand(hand2, part_two)

    if part_two:
        cards_ranking["J"] = 1

    if rank1 < rank2:
        return -1
    if rank1 > rank2:
        return 1

    for i in range(5):
        if cards_ranking[hand1[i]] < cards_ranking[hand2[i]]:
            return -1
        if cards_ranking[hand1[i]] > cards_ranking[hand2[i]]:
            return 1
    return 0


def compare_one(hand1: str, hand2: str) -> int:
    return compare(hand1, hand2)


def compare_two(hand1: str, hand2: str) -> int:
    return compare(hand1, hand2, True)


def compute(filename, compare_function):
    players = parse_hands(filename)
    hands = list(players.keys())
    hands.sort(key=cmp_to_key(compare_function))
    return sum(
        [(idx + 1) * int(players[hand]) for idx, hand in enumerate(hands)]
    )


def compute_one(filename):
    return compute(filename, compare_one)


def compute_two(filename):
    return compute(filename, compare_two)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    winnings = compute_one("inputs")
    assert winnings == 253313241
    logging.info(winnings)

    winnings = compute_two("inputs")
    assert winnings == 253362743
    logging.info(winnings)
