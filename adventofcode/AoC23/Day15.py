import re

from adventofcode.helpers.AoCHelper import read_input_lines


def compute_hash(string: str) -> int:
    hash = 0
    for c in string:
        hash += ord(c)
        hash = hash * 17
        hash = hash % 256

    return hash


def populate_boxes(init_sequence):
    boxes = [{} for _ in range(256)]
    for init in init_sequence:
        op_idx = re.search(r"=|-", init).start()
        label = init[:op_idx]
        operation = init[op_idx]

        label_hash = compute_hash(label)

        if operation == "-":
            if label in boxes[label_hash].keys():
                del boxes[label_hash][label]
        else:
            focal_lenght = init[op_idx + 1]
            boxes[label_hash][label] = focal_lenght

    return boxes


if __name__ == "__main__":
    input = read_input_lines("AoC23/Inputs/Day15/inputs.txt")[0]
    init_sequence = input.split(",")

    result = sum(compute_hash(init) for init in init_sequence)
    assert result == 513214
    print(f"Part 1: {result}")

    result2 = 0
    for idx, box in enumerate(populate_boxes(init_sequence)):
        for idy, label in enumerate(box.keys()):
            result2 += (idx + 1) * (idy + 1) * int(box[label])
    assert result2 == 258826
    print(f"Part 2: {result2}")
