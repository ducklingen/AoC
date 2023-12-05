from adventofcode.helpers import AoCHelper
from collections import Counter

input = AoCHelper.read_input_lines("Day4/inputs1.txt")

cards = [i[8:] for i in input]

result = 0
counter = Counter({i: 1 for i in range(len(input))})
for idx, c in enumerate(cards):
    winners, mine = c.split("|")
    winning_numbers = AoCHelper.extract_numbers_from_line(winners)
    my_numbers = AoCHelper.extract_numbers_from_line(mine)

    matches = len(set(winning_numbers).intersection(my_numbers))
    if matches > 0:
        result += 2 ** (matches - 1)

    for i in range(matches):
        counter[idx + i + 1] += counter[idx]

print(result)
print(sum(counter.values()))
