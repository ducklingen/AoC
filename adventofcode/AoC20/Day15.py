import sys

from adventofcode.helpers.AoCHelper import extract_numbers_from_line

sys.setrecursionlimit(5000)

# tic = time.perf_counter()


def play_n_turns(n):
    input_numbers = extract_numbers_from_line("14,8,16,0,1,17")

    dict = {}
    turn_number = 0

    for idx, i in enumerate(input_numbers[:-1]):
        dict[i] = idx
        turn_number += 1

    previous_turn = input_numbers[len(input_numbers) - 1]

    for i in range(len(input_numbers), n + 2):
        if previous_turn in dict.keys():
            last_spoken = dict[previous_turn] + 1
            dict[previous_turn] = i - 1
            previous_turn = i - last_spoken

        else:
            dict[previous_turn] = i - 1
            previous_turn = 0
        if i + 1 == n:
            return previous_turn


# toc = time.perf_counter()
# print(f"Performed task in {toc - tic:0.4f} seconds")


p1 = play_n_turns(2020)
p2 = play_n_turns(30000000)
assert p1 == 240
assert p2 == 505
print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
