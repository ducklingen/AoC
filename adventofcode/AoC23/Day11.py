from adventofcode.helpers.AoCHelper import read_input_lines


def compute(filename: str, multiplier: int):
    universe = read_input_lines(f"AoC23/Inputs/Day11/{filename}.txt")
    galaxies = []
    empty_rows = []
    empty_columns = []

    for i in range(len(universe)):
        for j in range(len(universe[0])):
            if universe[i][j] == "#":
                galaxies.append((i, j))

        if set(universe[i]) == {"."}:
            empty_rows.append(i)

    for j in range(len(universe[0])):
        if set([r[j] for r in universe]) == {"."}:
            empty_columns.append(j)

    sum_of_distances = 0
    for i in range(len(galaxies)):
        for j in range(len(galaxies) - i - 1):
            k = len(galaxies) - j - 1
            max_x = max(galaxies[i][0], galaxies[k][0])
            min_x = min(galaxies[i][0], galaxies[k][0])
            max_y = max(galaxies[i][1], galaxies[k][1])
            min_y = min(galaxies[i][1], galaxies[k][1])
            dist = max_x - min_x
            dist += max_y - min_y
            dist += sum([min_y < i < max_y for i in empty_columns]) * multiplier
            dist += sum([min_x < i < max_x for i in empty_rows]) * multiplier
            sum_of_distances += dist

    return sum_of_distances


if __name__ == "__main__":
    result1 = compute("inputs", 1)
    assert result1 == 10422930
    print(f"Part 1: {result1}")
    result2 = compute("inputs", 999999)
    assert result2 == 699909023130
    print(f"Part 2: {result2}")
