from collections import Counter

from helpers import AoCHelper
import time

start_time = time.time()

input_lines = AoCHelper.read_input_lines("day14/input1.txt")

template = input_lines[0]
instructions = {}

for i in range(2, len(input_lines)):
    pos, val = input_lines[i].split(" -> ")
    instructions[pos] = val


def run_game(game_lenght, instructions, template):
    changes = {
        pos: [pos[0] + value, value + pos[1]]
        for pos, value in instructions.items()
    }
    pair_counter = Counter({ins: template.count(ins) for ins in instructions})
    letter_counter = Counter(template)

    for n in range(game_lenght):
        letter_counter += {
            k: sum(
                value
                for ins, value in pair_counter.items()
                if instructions[ins] == k
            )
            for k in instructions.values()
        }

        pair_counter = Counter(
            {
                ins: sum(
                    pair_counter[change]
                    for change in changes
                    if ins in changes[change]
                )
                for ins in instructions
            }
        )

    return max(letter_counter.values()) - min(letter_counter.values())


part_one_res = run_game(10, instructions, template)
assert part_one_res == 2068
print(f"Part 1: {part_one_res}")

part_two_res = run_game(40, instructions, template)
assert part_two_res == 2158894777814
print(f"Part 2: {part_two_res}")

print("--- %s seconds ---" % (time.time() - start_time))
