from helpers import AoCHelper
import re

input = AoCHelper.read_input_lines("Day2/inputs1.txt")


def parse_input(input):
    games = []
    for i in input:
        color_dict = {"green": [], "blue": [], "red": []}
        game, rounds = i.split(":")
        _, game_id = game.split()

        color_rounds = re.split(';|,', rounds)
        for cr in color_rounds:
            amount, color = cr.strip().split()
            color_dict[color].append(int(amount))

        games.append((game_id, color_dict))

    return games


games = parse_input(input)
result = result2 = 0
for id, dict in games:
    if max(dict["red"]) <= 12 and max(dict["green"]) <= 13 and max(dict["blue"]) <= 14:
        result += int(id)

    result2 += max(dict["red"]) * max(dict["green"]) * max(dict["blue"])

assert result == 2716
print(f"Part 1: {result}")
assert result2 == 72227
print(f"Part 2: {result2}")
