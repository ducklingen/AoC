import math
from helpers import AoCHelper


def calculate_mass(mass):
    return math.floor((mass / 3)) - 2


def calculate_fuel_need_v2(mass):
    if mass <= 0:
        return 0
    else:
        firstBatch = max(calculate_mass(mass), 0)
        return firstBatch + calculate_fuel_need_v2(firstBatch)


massList = AoCHelper.read_input_lines("Day1Input.txt")

fuelSum = 0

for i in massList:
    fuelSum = fuelSum + calculate_fuel_need_v2(int(i))
#
print(fuelSum)

print(calculate_fuel_need_v2(14))
print(calculate_fuel_need_v2(1969))
print(calculate_fuel_need_v2(100756))
