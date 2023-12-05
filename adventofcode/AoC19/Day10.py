import math
import sys
from fractions import gcd

from adventofcode.helpers import AoCHelper

inputLines = AoCHelper.readInputLines("day10input.txt")

asteroids = []


def goThroughListOfSlopes(
    slopesToProcess, rotationNumber, reversed, slopes, asteroidsShot
):
    distinctSlopes = {float(s[1]) for s in slopesToProcess}
    distinctSlopesList = list(distinctSlopes)
    distinctSlopesList.sort(reverse=reversed)

    for slope in distinctSlopesList:
        slopesWithMax = list(filter(lambda x: x[1] == slope, slopesToProcess))

        distancesToCenter = [
            math.sqrt(
                ((p[0][0] - asteroid[0]) ** 2) + ((p[0][1] - asteroid[1]) ** 2)
            )
            for p in slopesWithMax
        ]

        minIndex = distancesToCenter.index(min(distancesToCenter))

        closestAsteroid = slopesWithMax[minIndex][0]

        asteroidsShot = asteroidsShot + 1
        print(
            str(closestAsteroid)
            + " was shot as number "
            + str(asteroidsShot)
            + " at rotation number "
            + str(rotationNumber)
            + " with gun pointed in direction "
            + str(slope)
        )

        slopes.remove((closestAsteroid, slope))

    return asteroidsShot


def calculateSlope(asteroidA, asteroidB):
    distanceY = asteroidA[0] - asteroidB[0]
    distanceX = asteroidB[1] - asteroidA[1]

    if distanceX == 0 and distanceY > 0:
        return sys.maxsize
    elif distanceX == 0 and distanceY < 0:
        return -sys.maxsize
    else:
        return distanceY / distanceX


def shootAsteroids(asteroid, asteroids):
    asteroidsShot = 0
    asteroids.remove(asteroid)

    slopes = [(a, calculateSlope(asteroid, a)) for a in asteroids]

    rotationNumber = 1

    while len(slopes) > 0:
        slopesToRight = list(filter(lambda x: x[0][1] >= asteroid[1], slopes))
        slopesToLeft = list(filter(lambda x: x[0][1] < asteroid[1], slopes))

        asteroidsShot = goThroughListOfSlopes(
            slopesToRight, rotationNumber, True, slopes, asteroidsShot
        )
        asteroidsShot = goThroughListOfSlopes(
            slopesToLeft, rotationNumber, True, slopes, asteroidsShot
        )

        rotationNumber = rotationNumber + 1


def countNumberOfVisibleItemsFromAsteroid(asteroid, asteroids):
    result = 0

    for i in range(-25, 25):
        for j in range(-25, 25):
            if i == 0 and j == 0:
                continue

            if abs(gcd(i, j)) == 1:
                for p in range(1, 25):
                    if (
                        int(asteroid[0]) + p * i,
                        int(asteroid[1]) + p * j,
                    ) in asteroids:
                        result = result + 1

                        # print(str(asteroid) + " can see " + str((int(asteroid[0]) + p * i, int(asteroid[1]) + p * j)))
                        break

    return result


for i, inputLine in enumerate(inputLines):
    lineAsString = list(inputLine)

    for j, pos in enumerate(lineAsString):
        if pos == "#":
            asteroids.append((i, j))

numberOfDetectableItems = 0
asteroidChosen = ()

for asteroid in asteroids:
    print("Checking validity of asteroid " + str(asteroid))
    numberOfDetectableItemsFromRepo = countNumberOfVisibleItemsFromAsteroid(
        asteroid, asteroids
    )

    if numberOfDetectableItemsFromRepo >= numberOfDetectableItems:
        numberOfDetectableItems = numberOfDetectableItemsFromRepo
        asteroidChosen = asteroid

print(asteroidChosen)
print(numberOfDetectableItems)

shootAsteroids(asteroidChosen, asteroids)

# for a in asteroids:
#     print("The slope from " + str(asteroidChosen) + " to " + str(a) + " is " + str(calculateSlope(asteroidChosen, a)))
