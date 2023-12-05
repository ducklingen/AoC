from math import ceil

from adventofcode.helpers import AoCHelper

# lines = AoCHelper.readInputLines("Testdata/Day14Test3.txt")
lines = AoCHelper.readInputLines("day14input.txt")

recipes = {}


def parseRecipe(line):
    inputOutput = line.split("=>")

    outputSplit = inputOutput[1].strip().split(" ")
    outputType = outputSplit[1]
    outputAmount = outputSplit[0]

    reagents = []
    reagentLines = inputOutput[0].split(",")

    for reagentLine in reagentLines:
        reagentSplit = reagentLine.strip().split(" ")

        reagents.append((reagentSplit[0], reagentSplit[1]))

    recipes[outputType] = [outputAmount, reagents]


for line in lines:
    parseRecipe(line)

amountsOfOre = 0

leftovers = {}


def oreNeededFor(type, amount):
    if type == "ORE":
        return int(amount)
    else:
        recipeOutput = recipes[type][0]
        recipeMultiple = ceil(
            (int(amount) - int(leftovers.setdefault(type, 0)))
            / int(recipeOutput)
        )

        leftovers[type] = recipeMultiple * int(recipeOutput) - (
            int(amount) - int(leftovers.setdefault(type, 0))
        )

        oreNeeded = 0

        for reagent in recipes[type][1]:
            # print("Use " + str(recipeMultiple*int(reagent[0])) + " batches of " + reagent[1] + " for " + str(amount) + " batches of " + type)
            oreNeeded = oreNeeded + oreNeededFor(
                reagent[1], recipeMultiple * int(reagent[0])
            )

        return oreNeeded


# print(oreNeededFor("FUEL", 1))
oreStorage = 1000000000000
fuel = 1630000

while True:
    leftovers = {}

    if oreNeededFor("FUEL", fuel) >= oreStorage:
        print("Cannot produce " + str(fuel) + " stacks of fuel")
        break

    if fuel % 1000 == 0:
        print("Can produce " + str(fuel) + " stacks of fuel")

    fuel = fuel + 1

# print(oreNeededFor("FUEL", 1639376))
