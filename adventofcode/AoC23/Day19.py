import re

from adventofcode.helpers.AoCHelper import group_lines, read_input_lines


def process_rules(rules, vars) -> str:
    for r in rules:
        if "<" in r:
            var, limit, res = re.split(r"<|:", r)
            if vars[var] < int(limit):
                return res
        if ">" in r:
            var, limit, res = re.split(r">|:", r)
            if vars[var] > int(limit):
                return res
        if "<" not in r and ">" not in r:
            return r


def create_flow_dict(flows: list[str]) -> dict[str, list[str]]:
    flow_dict = {}
    for f in flows:
        f = f[:-1]
        start, rules_string = f.split("{")
        flow_dict[start] = rules_string.split(",")

    return flow_dict


def create_ratings_dict(ratings: str) -> dict[str, int]:
    ratings_dict = {}

    ratings = ratings[1:-1]
    vars = ratings.split(",")
    for v in vars:
        var, value = v.split("=")
        ratings_dict[var] = int(value)

    return ratings_dict


def compute_one(filename: str) -> int:
    input = read_input_lines(f"AoC23/Inputs/Day19/{filename}.txt")
    flows, ratings = group_lines(input)
    flow_dict = create_flow_dict(flows)
    res = 0
    for r in ratings:
        ratings_dict = create_ratings_dict(r)

        state = "in"
        while state not in ("A", "R"):
            state = process_rules(flow_dict[state], ratings_dict)

        if state == "A":
            res += sum(ratings_dict.values())

    return res


if __name__ == "__main__":
    res = compute_one("inputs")
    assert res == 397134
    print(f"Part 1: {res}")
