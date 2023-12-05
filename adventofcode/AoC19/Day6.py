import sys

from adventofcode.helpers import AoCHelper

inputLines = AoCHelper.read_input_lines("day6input.txt")

orbitPairs = {}

for input in inputLines:
    nodes = input.split(")")

    center = nodes[0]
    satellite = nodes[1]

    orbitPairs[satellite] = center

# orbits = {}


def getOrbitPath(satellite, orbitPairs):
    planetOrbits = []

    loopVar = satellite

    while loopVar in orbitPairs:
        planetOrbits.append(orbitPairs[loopVar])

        loopVar = orbitPairs[loopVar]

    return planetOrbits


# for satellite in orbitPairs:
#     orbits[satellite] = getOrbitPath(satellite, orbitPairs)
#
# numberOfTotalOrbits = 0
#
# for x in orbits:
#     numberOfTotalOrbits = numberOfTotalOrbits + len(orbits[x])

orbitPathOfYou = getOrbitPath("YOU", orbitPairs)
orbitPathOfSan = getOrbitPath("SAN", orbitPairs)

intersections = set(orbitPathOfSan).intersection(orbitPathOfYou)

distanceToCommonPoint = sys.maxsize
closestIntersection = ""

for i in intersections:
    if (
        orbitPathOfYou.index(i) + orbitPathOfSan.index(i)
        < distanceToCommonPoint
    ):
        distanceToCommonPoint = orbitPathOfYou.index(i) + orbitPathOfSan.index(
            i
        )
        closestIntersection = i

print("Hej")
