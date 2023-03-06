from helpers import AoCHelper

input = AoCHelper.read_input_lines("day8/input1.txt")

visible_trees = set([])
tree_map = [list(map(int, i)) for i in input]

for i in range(len(tree_map)):
    a = b = c = d = -1

    for j in range(len(tree_map[i])):
        if tree_map[i][j] > a:
            visible_trees.add((i,j))
            a = tree_map[i][j]

        if tree_map[i][len(input[i]) - j - 1] > b:
            visible_trees.add((i, len(input[i]) - j - 1))
            b = tree_map[i][len(input[i]) - j - 1]

        if tree_map[j][i] > c:
            visible_trees.add((j, i))
            c = tree_map[j][i]

        if tree_map[len(input[i]) - j - 1][i] > d:
            visible_trees.add((len(input[i]) - j - 1, i))
            d = tree_map[len(input[i]) - j - 1][i]

res = len(visible_trees)
print(f"Part 1: {res}")


def scenic_score(map, i, j):
    own_val = tree_map[i][j]

    step = 1
    visible_trees_s = 0
    while i + step < len(map):
        visible_trees_s += 1
        if tree_map[i + step][j] < own_val:
            step += 1
        else:
            break

    step = 1
    visible_trees_n = 0
    while i - step >= 0:
        visible_trees_n += 1
        if tree_map[i - step][j] < own_val:
            step += 1
        else:
            break

    step = 1
    visible_trees_e = 0
    while j + step < len(map):
        visible_trees_e += 1
        if tree_map[i][j + step] < own_val:
            step += 1
        else:
            break

    step = 1
    visible_trees_w = 0
    while j - step >= 0:
        visible_trees_w += 1
        if tree_map[i][j - step] < own_val:
            step += 1
        else:
            break

    return visible_trees_e * visible_trees_n * visible_trees_s * visible_trees_w


scenic_scores = [[scenic_score(tree_map, i, j) for j in range(len(tree_map))] for i in range(len(tree_map))]
res = max([max(s) for s in scenic_scores])
assert res == 211680
print(f"Part 2: {res}")