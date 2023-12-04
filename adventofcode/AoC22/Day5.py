from adventofcode.helpers import AoCHelper

input = AoCHelper.read_input_lines("day5/input1.txt")
setup, instructions = AoCHelper.group_lines(input)


def init(setup):
    number_of_stacks = len(setup[-1:][0].split())
    stacks = [[] for _ in range(number_of_stacks)]

    for s in setup[:len(setup)-1]:
        for i in range(number_of_stacks):
            if (x := s[1 + i*4]) != ' ':
                stacks[i].append(x)

    for s in stacks:
        s.reverse()

    return stacks


def top_crates(stacks):
    res = ''
    for s in stacks:
        res += s.pop()

    return res


stacks = init(setup)
for i in instructions:
    a, f, t = AoCHelper.extract_numbers_from_line(i)

    for j in range(a):
        e = stacks[f-1].pop()
        stacks[t-1].append(e)

res = top_crates(stacks)
assert res == 'HNSNMTLHQ'
print(f"Part 1: {res}")

stacks = init(setup)
for i in instructions:
    a, f, t = AoCHelper.extract_numbers_from_line(i)

    m, r = stacks[f-1][-a:], stacks[f-1][:-a]
    stacks[f-1] = r
    stacks[t-1] = stacks[t-1] + m

res = top_crates(stacks)
assert res == 'RNLFDJMCT'
print(f"Part 2: {res}")


