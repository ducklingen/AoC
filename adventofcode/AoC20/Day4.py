import re
from helpers import AoCHelper
from helpers.AoCHelper import group_lines, list_to_string

input = AoCHelper.read_input_lines("day4/day4input1.txt")
passports = [list_to_string(l, " ") for l in group_lines(input)]

requiredKeys = {"byr", "iyr", "eyr", "hgt", "ecl", "hcl", "pid"}

validPassports = 0
passportsWithRequiredKeys = 0


def hasRequiredKeys(keys):
    return requiredKeys.intersection(set(keys)) == requiredKeys


def validateFields(fields):
    validPassport = True
    for f in fields:
        key, value = f.split(":")

        if validPassport:
            validPassport = passportFieldValidator(key, value)
        else:
            return False
    return validPassport


def passportFieldValidator(key, value):
    if key == "byr":
        return 1920 <= int(value) <= 2002
    elif key == "iyr":
        return 2010 <= int(value) <= 2020
    elif key == "eyr":
        return 2020 <= int(value) <= 2030
    elif key == "hgt":
        return (
            re.search("^\d*cm$", value)
            and 150 <= int(value.replace("cm", "")) <= 193
        ) or (
            re.search("^\d*in$", value)
            and 59 <= int(value.replace("in", "")) <= 76
        )
    elif key == "hcl":
        return re.search("^#[0-9a-f]{6}", value)
    elif key == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif key == "pid":
        return re.search("^\d{9}$", value)
    else:
        return True


for p in passports:
    validPassport = True
    fields = [field for field in p.split(" ") if field.strip()]
    fieldKeys = [f.split(":")[0] for f in fields]

    if hasRequiredKeys(fieldKeys):
        passportsWithRequiredKeys += 1
        validPassports += bool(validateFields(fields))
    else:
        continue

assert passportsWithRequiredKeys == 192
print("Part 1: " + str(passportsWithRequiredKeys))
assert validPassports == 101
print("Part 2: " + str(validPassports))
