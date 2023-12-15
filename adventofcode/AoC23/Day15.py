import re

from adventofcode.helpers.AoCHelper import read_input_lines

input = read_input_lines("AoC23/Inputs/Day15/inputs.txt")[0]

result = 0
init_sequence = input.split(",")


def compute_hash(string: str) -> int:
    hash = 0
    for c in string:
        hash += ord(c)
        hash = hash * 17
        hash = hash % 256

    return hash


for init in init_sequence:
    result += compute_hash(init)

print(result)

boxes = [{} for _ in range(256)]
for init in init_sequence:
    op_match = re.search(r"=|-", init)
    op_idx = op_match.start()
    label = init[:op_idx]
    operation = init[op_idx]

    label_hash = compute_hash(label)

    if operation == "-":
        if label in boxes[label_hash].keys():
            del boxes[label_hash][label]
    else:
        focal_lenght = init[op_idx + 1]
        boxes[label_hash][label] = focal_lenght

result2 = 0
for idx, box in enumerate(boxes):
    for idy, label in enumerate(box.keys()):
        score = (idx + 1) * (idy + 1) * int(box[label])
        print(score)
        result2 += score

print(result2)
