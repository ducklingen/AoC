from adventofcode.helpers.AoCHelper import lcm, read_input_lines


def steps_before_end(start, connections, directions):
    loc = start
    steps = 0

    while loc[2] != "Z":
        for d in list(directions):
            if d == "R":
                loc = connections[loc][1]
            else:
                loc = connections[loc][0]

            steps += 1

            if loc[2] == "Z":
                break

    return steps, loc


def compute_one(filename):
    input = read_input_lines(f"AoC23/Inputs/Day8/{filename}.txt")
    directions = input[0]
    connections = {i[0:3]: (i[7:10], i[12:15]) for i in input[2:]}

    steps = 0
    location = "AAA"

    while location != "ZZZ":
        for d in list(directions):
            if d == "R":
                location = connections[location][1]
            else:
                location = connections[location][0]

            steps += 1

            if location == "ZZZ":
                break

    return steps


def compute_two(filename):
    input = read_input_lines(f"AoC23/Inputs/Day8/{filename}.txt")
    directions = input[0]
    connections = {i[0:3]: (i[7:10], i[12:15]) for i in input[2:]}

    locations = [key for key in connections.keys() if key[2] == "A"]
    steps = {
        loc: steps_before_end(loc, connections, directions) for loc in locations
    }
    values = [steps[i][0] for i in steps.keys()]
    result = values[0]
    for i in range(len(values) - 1):
        result = lcm(result, values[i + 1])

    return result


if __name__ == "__main__":
    result = compute_one("inputs")
    assert result == 19241
    print(f"Part 1: {result}")

    result = compute_two("inputs")
    assert result == 9606140307013
    print(f"Part 2: {result}")
