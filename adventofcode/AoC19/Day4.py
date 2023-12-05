def isSixDigits(number):
    return 100000 <= number <= 999999


def hasTwoAdjecentPairOfDigits(number):
    result = False

    digits = list(map(int, str(number)))

    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1]:
            return True

    return result


def hasNondecreasingDigits(number):
    result = True

    digits = list(map(int, str(number)))

    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return False

    return result


def hasTwoAdjecentPairButOnlyPairOfDigits(number):
    result = False

    for i in "1234567890":
        if i + i in str(number) and i + i + i not in str(number):
            return True

    return result


def isValidPassword(number):
    return (
        isSixDigits(number)
        and hasTwoAdjecentPairButOnlyPairOfDigits(number)
        and hasNondecreasingDigits(number)
    )


numberOfValidPasswords = 0

for password in range(254032, 789860):
    if isValidPassword(password):
        numberOfValidPasswords = numberOfValidPasswords + 1

print(numberOfValidPasswords)

# print(hasTwoAdjecentPairOfDigits(111111))
# print(hasTwoAdjecentPairOfDigits(223450))
# print(hasTwoAdjecentPairOfDigits(123789))

# print(hasTwoAdjecentPairButOnlyPairOfDigits(112233))
# print(hasTwoAdjecentPairButOnlyPairOfDigits(123444))
# print(hasTwoAdjecentPairButOnlyPairOfDigits(111122))
# print(hasTwoAdjecentPairButOnlyPairOfDigits(111111))
# print(hasTwoAdjecentPairButOnlyPairOfDigits(223450))
# print(hasTwoAdjecentPairButOnlyPairOfDigits(123789))
# print(hasTwoAdjecentPairButOnlyPairOfDigits(122122))
# print(hasTwoAdjecentPairButOnlyPairOfDigits(111222))

# print(hasNondecreasingDigits(111111))
# print(hasNondecreasingDigits(223450))
# print(hasNondecreasingDigits(123789))

# print(isValidPassword(111111))
# print(isValidPassword(223450))
# print(isValidPassword(123789))
