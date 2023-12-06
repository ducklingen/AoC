import sys

from adventofcode.helpers.AoCHelper import (
    extract_numbers_from_line,
    read_input_lines,
    split_lines_into_chunks,
)

sys.setrecursionlimit(5000)

# tic = time.perf_counter()


# input_lines = read_input_lines('day16/day16input1.txt')
# rules, my, nearby = split_lines_into_chunks(input_lines, [''])
# ranges = []
#
# for r in rules:
#     a, b, c, d = extract_numbers_from_line(r)
#     ranges.append((a, b))
#     ranges.append((c, d))
#
# values = []
# for n in nearby[1:]:
#     values += extract_numbers_from_line(n)
#
#
def is_valid(value, ranges):
    valid = False

    for r in ranges:
        if r[0] <= value <= r[1]:
            valid = True
            break

    return valid


# errors = list(filter(lambda x: not is_valid(x, ranges), values))
# p1 = sum(errors)
# assert p1 == 26869
# print(p1)

input_lines = read_input_lines("day16/day16input1.txt")

rules, my, nearby = split_lines_into_chunks(input_lines, [""])
nearby_numbers = [extract_numbers_from_line(n) for n in nearby]
my_ticket = extract_numbers_from_line(my[1])
position_lists = []
ranges = []

for r in rules:
    a, b, c, d = extract_numbers_from_line(r)
    ranges.append((a, b))
    ranges.append((c, d))

valid_tickets = []
for n in nearby_numbers[1:]:
    if min([is_valid(x, ranges) for x in n]) == 1:
        valid_tickets.append(n)


for i in range(len(nearby_numbers[1])):
    position_list = []
    for n in valid_tickets:
        position_list.append(n[i])

    position_lists.append(position_list)

matching_rules_dict = {}

for idx, p in enumerate(position_lists):
    matching_rules = []

    for r in rules:
        a, b, c, d = extract_numbers_from_line(r)
        rule_name = r.split(":")[0]
        if (
            rule_name in matching_rules_dict.keys()
            or idx in matching_rules_dict.values()
        ):
            continue

        # print([a <= x <= b or c <= x <= d for x in p])

        if min([a <= x <= b or c <= x <= d for x in p]) == 1:
            matching_rules.append(rule_name)

    matching_rules_dict[idx] = matching_rules

    if (
        idx not in matching_rules_dict.keys()
        or len(matching_rules_dict[idx]) == 0
    ):
        print(
            "No remaining rules found matching values at position " + str(idx)
        )

p2 = 1

rule_fields = {}

while len(rule_fields.keys()) < len(rules):
    for i in matching_rules_dict:
        if len(matching_rules_dict[i]) == 1:
            rule = matching_rules_dict[i][0]
            print("Matching rule " + rule + " with column " + str(i))
            rule_fields[i] = rule

            for j in matching_rules_dict:
                if i != j and rule in matching_rules_dict[j]:
                    matching_rules_dict[j].remove(rule)

for rf in rule_fields:
    print(rf)
    print(rule_fields[rf])

    if rule_fields[rf][:9] == "departure":
        p2 *= int(my_ticket[rf])

print(p2)
