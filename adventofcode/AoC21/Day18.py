import sys
import time

from helpers.AoCHelper import *

start_time = time.time()
input_lines = read_input_lines("day18/test2.txt")


def valid_line(line):
    if max(extract_numbers_from_line(line)) > 9:
        return False

    level = 0
    for c in line:
        if c == "[":
            level += 1
        if c == "]":
            level -= 1

        if level > 4:
            return False

    return True


def split_line(res):
    while max(extract_numbers_from_line(res)) > 9:
        max_val = max(extract_numbers_from_line(res))
        res = res.replace(
            str(max_val), f"[{max_val // 2},{math.ceil(max_val / 2)}]"
        )
        print(f"Split line into {res}")

    return res


def explode_line(res):
    level = 0
    left_idx = -1
    right_idx = sys.maxsize
    pair_idx = sys.maxsize

    for idx, c in enumerate(res):
        if c == "[":
            level += 1
        elif c == "]":
            level -= 1
        elif is_integer(c) and idx > pair_idx + 4:
            right_idx = idx
            break
        elif (
            is_integer(c)
            and level > 4
            and re.search(r",\d]", res[idx + 1 : idx + 4])
        ):
            pair_idx = idx
        elif is_integer(c) and idx < pair_idx:
            left_idx = idx

    if pair_idx < sys.maxsize:
        if right_idx < sys.maxsize:
            res = (
                res[:right_idx]
                + str(int(res[right_idx]) + int(res[pair_idx + 2]))
                + res[right_idx + 1 :]
            )

        extra_digit = 0
        if left_idx > 0:
            extra_digit = int(int(res[left_idx]) + int(res[pair_idx]) > 9)
            res = (
                res[:left_idx]
                + str(int(res[left_idx]) + int(res[pair_idx]))
                + res[left_idx + 1 :]
            )

        res = (
            res[: pair_idx - 1 + extra_digit]
            + "0"
            + res[pair_idx + 4 + extra_digit :]
        )
        print(f"Exploxed line into {res}")

    return res


def process_result(line):
    res = str(line)

    while not valid_line(res):
        res = split_line(res)
        res = explode_line(res)

    return res


# final_sum = ''
# #
# # for i in input_lines:
# #     final_sum = f'[{final_sum},{i}]' if final_sum != '' else i
# #     print(f"New initial sum {final_sum}")
# #     final_sum = process_result(final_sum)
# #     print(f"New reduced sum {final_sum}")
# #
# # print(final_sum)

# res = explode_line('[[[[4,0],[5,4]],[[7,7],[6,0]]],[[7,[5,5]],[[5,7],[[0,[5,6]],[8,8]]]]]')

res = process_result(
    "[[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]"
)
print("--- %s seconds ---" % (time.time() - start_time))
