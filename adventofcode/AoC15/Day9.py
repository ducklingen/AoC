from itertools import permutations

from adventofcode.helpers.AoCHelper import read_input_lines

inputlines = read_input_lines("AoC15/Inputs/day9/input1.txt")

cities = set([])
routes = {}

for i in inputlines:
    route, length = i.split(" = ")
    f, t = route.split(" to ")
    cities.add(f)
    cities.add(t)

    routes[(f, t)] = length
    routes[(t, f)] = length


def routeLength(perm):
    return sum(
        [int(routes[(perm[i], perm[i + 1])]) for i in range(len(perm) - 1)]
    )


minRoute = min(
    [routeLength(perm) for perm in permutations(list(cities), len(cities))]
)
maxRoute = max(
    [routeLength(perm) for perm in permutations(list(cities), len(cities))]
)

print(str(minRoute))
print(str(maxRoute))
