from adventofcode.helpers.AoCHelper import read_input_lines


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


# def compute_two(filename):
#     input = read_input_lines(f"AoC23/Inputs/Day8/{filename}.txt")
#     directions = input[0]
#     connections = {i[0:3]: (i[7:10], i[12:15]) for i in input[2:]}

#     def steps_before_end(start, connections, directions):
#         loc = start
#         steps = 0

#         while loc[2] != "Z":
#             for d in list(directions):
#                 if d == "R":
#                     loc = connections[loc][1]
#                 else:
#                     loc = connections[loc][0]

#                 steps += 1

#                 if loc[2] == "Z":
#                     break

#         return steps

#     locations = [key for key in connections.keys() if key[2] == "A"]
#     steps = {
#         loc: steps_before_end(loc, connections, directions) for loc in locations
#     }
#     print(steps)

#     steps = 0
#     while any(loc[2] != "Z" for loc in locations):
#         if steps % 100000 == 0:
#             print(f"Checked {steps} steps")

#         for d in list(directions):
#             new_locations = []
#             for loc in locations:
#                 if d == "R":
#                     new_locations.append(connections[loc][1])
#                 else:
#                     new_locations.append(connections[loc][0])

#             steps += 1
#             locations = new_locations

#             if all(loc[2] == "Z" for loc in locations):
#                 print(locations)
#                 break

#     print(steps)


if __name__ == "__main__":
    result = compute_one("inputs")
    assert result == 19241
    print(f"Part 1: {result}")
