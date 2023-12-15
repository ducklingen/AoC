from itertools import combinations

from adventofcode.helpers.AoCHelper import (
    extract_numbers_from_line,
    read_input_lines,
)


def compute_one(filename):
    input = read_input_lines(f"AoC23/Inputs/Day12/{filename}.txt")

    result = 0
    for i in input:
        req = extract_numbers_from_line(i)

        lava, _ = i.split()

        req_sum = sum(req)
        known_spaces = sum(c == "#" for c in lava)

        unknown_positions = [idx for idx, c in enumerate(lava) if c == "?"]

        for comb in combinations(unknown_positions, req_sum - known_spaces):
            cand_as_string = "".join(
                [
                    "#" if idx in comb or lava[idx] == "#" else "."
                    for idx in range(len(lava))
                ]
            )

            groups = list(filter(str.strip, cand_as_string.split(".")))

            if len(groups) == len(req) and all(
                len(g) == r for r, g in zip(req, groups)
            ):
                result += 1

    return result


if __name__ == "__main__":
    result = compute_one("inputs")
    assert result == 7622
    print(f"Part 1: {result}")
