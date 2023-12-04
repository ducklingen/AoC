import time


def move_pawn(pos, dice_sum):
    pos = (pos + dice_sum) % 10 if pos + dice_sum > 10 else pos + dice_sum
    if pos == 0:
        pos = 10

    return pos


def play_easy(player_one_pos, player_two_pos):
    dice_val = 1
    player_one_score = player_two_score = 0
    dice_rolls = 0

    while player_one_score < 1000 and player_two_score < 1000:
        dice_sum = 0

        for i in range(3):
            dice_sum += dice_val
            dice_val = dice_val + 1 if dice_val < 100 else 1

        player_one_pos = move_pawn(player_one_pos, dice_sum)
        player_one_score += player_one_pos
        dice_rolls += 3

        if player_one_score < 1000:
            dice_sum = 0

            for j in range(3):
                dice_sum += dice_val
                dice_val = dice_val + 1 if dice_val < 100 else 1

            player_two_pos = move_pawn(player_two_pos, dice_sum)
            player_two_score += player_two_pos
            dice_rolls += 3

    return dice_rolls * player_two_score if player_one_score >= 1000 else dice_rolls * player_one_score


start_time = time.time()

# player_one_start_pos = 4
# player_two_start_pos = 8
player_one_start_pos = 7
player_two_start_pos = 9

part_one_res = play_easy(player_one_start_pos, player_two_start_pos)
assert part_one_res == 679329
print(f"Part 1: {part_one_res}")

print("--- %s seconds ---" % (time.time() - start_time))
