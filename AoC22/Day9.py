from helpers import AoCHelper

input = AoCHelper.read_input_lines("day9/input1.txt")


def update_head(i, head_pos):
    if i == 'R':
        head_pos = (head_pos[0] + 1, head_pos[1])
    if i == 'L':
        head_pos = (head_pos[0] - 1, head_pos[1])
    if i == 'D':
        head_pos = (head_pos[0], head_pos[1] - 1)
    if i == 'U':
        head_pos = (head_pos[0], head_pos[1] + 1)

    return head_pos


def update_tail(head_pos, tail_pos):
    if abs(head_pos[0] - tail_pos[0]) > 1 or abs(head_pos[1] - tail_pos[1]) > 1:
        if head_pos[0] == tail_pos[0]:
            if head_pos[1] > tail_pos[1] + 1:
                tail_pos = (tail_pos[0], tail_pos[1] + 1)
            else:
                tail_pos = (tail_pos[0], tail_pos[1] - 1)
        elif head_pos[1] == tail_pos[1]:
            if head_pos[0] > tail_pos[0] + 1:
                tail_pos = (tail_pos[0] + 1, tail_pos[1])
            else:
                tail_pos = (tail_pos[0] - 1, tail_pos[1])
        elif head_pos[1] > tail_pos[1]:
            if head_pos[0] > tail_pos[0]:
                tail_pos = (tail_pos[0] + 1, tail_pos[1] + 1)
            else:
                tail_pos = (tail_pos[0] - 1, tail_pos[1] + 1)
        elif head_pos[1] < tail_pos[1]:
            if head_pos[0] > tail_pos[0]:
                tail_pos = (tail_pos[0] + 1, tail_pos[1] - 1)
            else:
                tail_pos = (tail_pos[0] - 1, tail_pos[1] - 1)

    return tail_pos


instructions = []

for i in input:
    d, v = i.split(' ')
    instructions += d * int(v)

head_pos = (0, 0)
tail_pos = (0, 0)
tail_pos_history = [tail_pos]

for i in instructions:
    head_pos = update_head(i, head_pos)

    tail_pos = update_tail(head_pos, tail_pos)
    tail_pos_history.append(tail_pos)

res = len(set(tail_pos_history))
assert res == 6209
print(f"Part 1: {res}")

snake = [(0, 0) for _ in range(10)]
tail_pos_history = [(0, 0)]

for i in instructions:
    snake[0] = update_head(i, snake[0])
    init_tail_pos = snake[9]

    for j in range(9):
        snake[j + 1] = update_tail(snake[j], snake[j + 1])

    if init_tail_pos != snake[9]:
        tail_pos_history.append(snake[9])

res = len(set(tail_pos_history))
assert res == 2460
print(f"Part 2: {res}")