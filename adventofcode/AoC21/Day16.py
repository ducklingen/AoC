from helpers import AoCHelper
from sys import maxsize
import time

start_time = time.time()

input_lines = AoCHelper.read_input_lines("day16/input1.txt")
input = input_lines[0]

ins = bin(int(input, 16))[2:].zfill(len(input) * 4)


class Package:
    version = 0
    type = 0
    lit_val = 0
    subpackages = []

    def __init__(self, version, type):
        self.version = version
        self.type = type


def extract_number(input, index, size):
    return int(input[index : index + size], 2), index + size


def unpack(input, index, number_of_packages, end_of_package):
    packages = []

    while len(packages) < number_of_packages and index < end_of_package:
        version, index = extract_number(input, index, 3)
        type, index = extract_number(input, index, 3)

        package = Package(version, type)

        if type == 4:
            lit_val_string = ""
            last_pack = False

            while not last_pack:
                if input[index] == "0":
                    last_pack = True

                lit_val_string += input[index + 1 : index + 5]
                index += 5

            package.lit_val = int(lit_val_string, 2)

        else:
            lenght_type, index = extract_number(input, index, 1)

            if lenght_type == 0:
                lenght, index = extract_number(input, index, 15)
                subpackages, index = unpack(
                    input, index, maxsize, index + lenght
                )
                package.subpackages = subpackages
            else:
                number_of_sub_packages, index = extract_number(input, index, 11)
                subpackages, index = unpack(
                    input, index, number_of_sub_packages, maxsize
                )
                package.subpackages = subpackages

        packages.append(package)

    return packages, index


def sum_version(package: Package):
    res = package.version

    if len(package.subpackages) > 0:
        res += sum(sum_version(p) for p in package.subpackages)

    return res


def calculate_value(package: Package):
    res = 0

    if package.type == 0:
        res = sum(calculate_value(p) for p in package.subpackages)
    elif package.type == 1:
        res = AoCHelper.prod(calculate_value(p) for p in package.subpackages)
    elif package.type == 2:
        res = min(calculate_value(p) for p in package.subpackages)
    elif package.type == 3:
        res = max(calculate_value(p) for p in package.subpackages)
    elif package.type == 4:
        res = package.lit_val
    elif package.type == 5:
        a = calculate_value(package.subpackages[0])
        b = calculate_value(package.subpackages[1])
        res = int(a > b)
    elif package.type == 6:
        a = calculate_value(package.subpackages[0])
        b = calculate_value(package.subpackages[1])
        res = int(a < b)
    elif package.type == 7:
        a = calculate_value(package.subpackages[0])
        b = calculate_value(package.subpackages[1])
        res = int(a == b)

    return res


packages = unpack(ins, 0, 1, len(ins))[0]

part_one_res = sum_version(packages[0])
assert part_one_res == 949
print(f"Part 1: {part_one_res}")

part_two_res = calculate_value(packages[0])
assert part_two_res == 1114600142730
print(f"Part 2: {part_two_res}")

print("--- %s seconds ---" % (time.time() - start_time))
