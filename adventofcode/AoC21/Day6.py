from helpers import AoCHelper

input = AoCHelper.read_input_lines("day6/input1.txt")


def init_dictionary(input_line):
    fishes = AoCHelper.extract_numbers(input_line)[0]
    return {n: len([fish for fish in fishes if fish == n]) for n in range(9)}


def run_simulation(length, fish_dict):
    for i in range(length):
        new_fish_dict = {8: fish_dict[0], 6: fish_dict[0] + fish_dict[7]}

        for key in fish_dict:
            if key > 0 and key != 7:
                new_fish_dict[key - 1] = fish_dict[key]

        fish_dict = new_fish_dict

    return fish_dict


fish_dict = init_dictionary(input)

part_one_dict = run_simulation(80, fish_dict)
part_one_res = sum(part_one_dict.values())
assert part_one_res == 360268
print(f"Part one: {part_one_res}")

part_two_dict = run_simulation(256, fish_dict)
part_two_res = sum(part_two_dict.values())
assert part_two_res == 1632146183902
print(f"Part two: {part_two_res}")
