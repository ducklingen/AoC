from math import gcd

europa = [[-17, -9, -4], [0, 0, 0]]
io = [[-2, 2, 13], [0, 0, 0]]
ganymede = [[1, 5, 1], [0, 0, 0]]
callisto = [[-4, 7, 7], [0, 0, 0]]

# europa = [[4, 12, 13], [0, 0, 0]]
# io = [[-9, 14, -3], [0, 0, 0]]
# ganymede = [[-7, -1, 2], [0, 0, 0]]
# callisto = [[-11, 17, -1], [0, 0, 0]]

# europa = [[-1, 0, 2], [0, 0, 0]]
# io = [[2, -10, -7], [0, 0, 0]]
# ganymede = [[4, -8, 8], [0, 0, 0]]
# callisto = [[3, 5, -1], [0, 0, 0]]

moons = [europa, io, ganymede, callisto]


def performStep(moons):
    for i in range(4):
        for j in range(4):
            if j > i:
                for k in range(3):
                    if moons[i][0][k] > moons[j][0][k]:
                        moons[i][1][k] = moons[i][1][k] - 1
                        moons[j][1][k] = moons[j][1][k] + 1
                    elif moons[i][0][k] < moons[j][0][k]:
                        moons[i][1][k] = moons[i][1][k] + 1
                        moons[j][1][k] = moons[j][1][k] - 1

    for moon in moons:
        for k in range(3):
            moon[0][k] = moon[0][k] + moon[1][k]

    return moons


def performStepDirection(moons, k):
    for i in range(4):
        for j in range(4):
            if j > i:
                if moons[i][0][k] > moons[j][0][k]:
                    moons[i][1][k] = moons[i][1][k] - 1
                    moons[j][1][k] = moons[j][1][k] + 1
                elif moons[i][0][k] < moons[j][0][k]:
                    moons[i][1][k] = moons[i][1][k] + 1
                    moons[j][1][k] = moons[j][1][k] - 1

    for moon in moons:
        moon[0][k] = moon[0][k] + moon[1][k]

    return moons


def moonsDirectionAsString(moons, k):
    moonsAsString = ""

    for i in range(4):
        for j in range(2):
            moonsAsString = moonsAsString + str(moons[i][j][k]) + "$"

    return moonsAsString


def lcm(a, b):
    return int(a * b / gcd(a, b))


periods = []

# while True:
for k in range(3):
    steps = 0

    statesAsSet = set([])

    moonsAsString = ""

    while steps == 0 or moonsAsString not in statesAsSet:
        steps = steps + 1
        statesAsSet.add(moonsAsString)
        moons = performStepDirection(moons, k)
        moonsAsString = moonsDirectionAsString(moons, k)

        # if steps % 1000 == 0:
        #     print(steps)

    print(moonsAsString)
    print(steps - 1)
    periods.append(steps - 1)

print(lcm(lcm(periods[0], periods[1]), periods[2]))

# def calculateEnergiOfMoon(moon):
#     return (abs(moon[0][0])+abs(moon[0][1])+
#           abs(moon[0][2]))*(abs(moon[1][0])+abs(moon[1][1])+abs(moon[1][2]))
#
# for i in range(1000):
#     moons = performStep(moons)
#     print(i)
#     print(moons)
#
# totalEnergi = 0
#
# for moon in moons:
#     totalEnergi = totalEnergi + calculateEnergiOfMoon(moon)
#
# print(totalEnergi)
