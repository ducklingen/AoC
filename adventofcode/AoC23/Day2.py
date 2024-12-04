import re

from adventofcode.helpers.AoCHelper import read_input_lines

input = read_input_lines("Day2/inputs1.txt")


def parse_input(input: list[str]) -> list[tuple[int, dict[str, list[int]]]]:
    games: list[tuple[int, dict[str, list[int]]]] = []
    for i in input:
        color_dict = {"green": [], "blue": [], "red": []}
        game, rounds = i.split(":")
        _, game_id = game.split()

        color_rounds = re.split(";|,", rounds)
        for cr in color_rounds:
            amount, color = cr.strip().split()
            color_dict[color].append(int(amount))

        games.append((int(game_id), color_dict))

    return games


games = parse_input(input)
result = result2 = 0
for id, game in games:
    if (
        max(game["red"]) <= 12
        and max(game["green"]) <= 13
        and max(game["blue"]) <= 14
    ):
        result += id

    result2 += max(game["red"]) * max(game["green"]) * max(game["blue"])

assert result == 2716
print(f"Part 1: {result}")
assert result2 == 72227
print(f"Part 2: {result2}")
