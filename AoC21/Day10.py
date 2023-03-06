from helpers import AoCHelper

input_lines = AoCHelper.read_input_lines("day10/input1.txt")

brackets = {')': '(', ']': '[', '}': '{', '>': '<'}
bracket_scores = {'(': 1, '[': 2, '{': 3, '<': 4, ')': 3, ']': 57, '}': 1197, '>': 25137}

incomplete_scores = []
score = 0

for i in input_lines:
    open_start_brackets = []
    corrupt = False

    for c in i:
        if c in brackets.values():
            open_start_brackets.append(c)
        else:
            if open_start_brackets[-1] != brackets[c]:
                score += bracket_scores[c]
                corrupt = True
                break
            else:
                open_start_brackets = open_start_brackets[:-1]

    if not corrupt:
        line_score = 0
        open_start_brackets.reverse()

        for b in open_start_brackets:
            line_score = 5 * line_score + bracket_scores[b]

        incomplete_scores.append(line_score)

assert score == 240123
print(f"Part 1: {score}")

incomplete_scores.sort()
part_two_score = incomplete_scores[len(incomplete_scores) // 2]
assert part_two_score == 3260812321
print(f"Part 2: {part_two_score}")