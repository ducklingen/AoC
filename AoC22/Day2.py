from helpers import AoCHelper

input = AoCHelper.read_input_lines("day2/input1.txt")

total_score = 0

scores = {'X': 1, 'Y': 2, 'Z': 3}
wins = {'X': 'C', 'Y': 'A', 'Z': 'B'}
losses = {'X': 'B', 'Y': 'C', 'Z': 'A'}
sames = {'X': 'A', 'Y': 'B', 'Z': 'C'}

for i in input:
    opp, me = i.split()
    total_score += scores[me]

    if opp == wins[me]:
        total_score += 6
    elif opp != losses[me]:
        total_score += 3

assert total_score == 12276
print(f"Part 1: {total_score}")


total_score = 0

for i in input:
    opp, res = i.split()

    if res == 'X':
        total_score += scores[list(losses)[list(losses.values()).index(opp)]]

    if res == 'Y':
        total_score += 3 + scores[list(sames)[list(sames.values()).index(opp)]]

    if res == 'Z':
        total_score += 6 + scores[list(wins)[list(wins.values()).index(opp)]]

assert total_score == 9975
print(f"Part 2: {total_score}")