from helpers.AoCHelper import *

inputlines = read_input_lines("day7/day7input1.txt")

specialbag = "shiny gold bag"

bags = {}

for i in inputlines:
    i = i.replace("bags", "bag").replace(".", "")
    container, indhold = i.split(" contain ")
    indholdsliste = []
    for j in indhold.split(", "):
        if j == "no other bag":
            break

        list = j.split(" ")
        indholdsliste.append((list[0], list_to_string(list[1:], " ").strip()))

    bags[container] = indholdsliste


def containsShinyGold(baglist, bags):
    contains = False
    for bag in baglist:
        if bag[1] == specialbag:
            contains = True
            break

    if not contains and baglist != []:
        contains = max(
            [containsShinyGold(bags[bag[1]], bags) for bag in baglist]
        )

    return contains


def containsNumberOfBags(baglist, bags):
    return sum(
        [
            int(bag[0]) + int(bag[0]) * containsNumberOfBags(bags[bag[1]], bags)
            for bag in baglist
        ]
    )


assert sum([containsShinyGold(bags[bag], bags) for bag in bags]) == 192
print(
    "Part 1: " + str(sum([containsShinyGold(bags[bag], bags) for bag in bags]))
)
assert containsNumberOfBags(bags[specialbag], bags) == 12128
print("Part 2: " + str(containsNumberOfBags(bags[specialbag], bags)))
