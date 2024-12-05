import logging
from functools import cmp_to_key
from pathlib import Path
from typing import Callable

from adventofcode.helpers.AoCHelper import (
    extract_numbers_from_line,
    group_lines,
    read_input_lines,
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

INPUT_FOLDER_PATH = Path("AoC24") / "Inputs" / "Day5"


def verify_updates(updates: list[int], rules: list[tuple[int, int]]) -> bool:
    for a, b in rules:
        if a in updates and b in updates:
            if updates.index(a) >= updates.index(b):
                return False

    return True


def compare_function(rules: list[tuple[int, int]]) -> Callable[[int, int], int]:

    rules_as_dict: dict[int, list[int]] = {}

    for a, b in rules:
        if a in rules_as_dict.keys():
            rules_as_dict[a].append(b)
        else:
            rules_as_dict[a] = [b]

    def _compare(a: int, b: int) -> int:
        if a in rules_as_dict.keys() and b in rules_as_dict[a]:
            return -1
        elif b in rules_as_dict.keys() and a in rules_as_dict[b]:
            return 1
        else:
            return 0

    return _compare


def solve_one(input_file: str) -> int:

    input_lines = read_input_lines(INPUT_FOLDER_PATH / input_file)
    rules, updates = group_lines(input_lines)

    rule_pairs = [extract_numbers_from_line(rule) for rule in rules]
    res = 0
    for update in updates:
        update_as_list = extract_numbers_from_line(update)

        if verify_updates(update_as_list, rule_pairs):
            res += update_as_list[len(update_as_list) // 2]

    return res


def solve_two(input_file: str) -> int:

    input_lines = read_input_lines(INPUT_FOLDER_PATH / input_file)
    rules, updates = group_lines(input_lines)

    rule_pairs = [extract_numbers_from_line(rule) for rule in rules]
    res = 0
    for update in updates:
        update_as_list = extract_numbers_from_line(update)
        key = cmp_to_key(compare_function(rule_pairs))

        if not verify_updates(update_as_list, rule_pairs):
            update_as_list.sort(key=key)
            res += update_as_list[len(update_as_list) // 2]

    return res


if __name__ == "__main__":
    res = solve_one("input.txt")
    assert res == 4281, f"Test failed: got {res}"
    logger.info(f"Part 1: {res}")

    res = solve_two("input.txt")
    assert res == 5466, f"Test failed: got {res}"
    logger.info(f"Part 2: {res}")
