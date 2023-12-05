from itertools import combinations_with_replacement, permutations

combination_set = set()

for i in combinations_with_replacement([0, 1], 10):
    for j in permutations(i):
        combination_set.add(j)

for c in combination_set:
    print(c)
