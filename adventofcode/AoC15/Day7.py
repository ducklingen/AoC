import re

operations = read_input_lines("day7/input1.txt")

wires = {}


def calculateInput(input, dict):
    if re.search("AND", input):
        a, b = input.split(" AND ")
        if not a.isdigit():
            a = int(dict[a])
        if not b.isdigit():
            b = int(dict[b])
        return int(a) & int(b)
    elif re.search("OR", input):
        a, b = input.split(" OR ")
        if not a.isdigit():
            a = int(dict[a])
        if not b.isdigit():
            b = int(dict[b])
        return int(a) | int(b)
    elif re.search("LSHIFT", input):
        a, b = input.split(" LSHIFT ")
        if not a.isdigit():
            a = int(dict[a])
        return int(a) << int(b)
    elif re.search("RSHIFT", input):
        a, b = input.split(" RSHIFT ")
        if not a.isdigit():
            a = int(dict[a])
        return int(a) >> int(b)
    elif re.search("NOT", input):
        a = input[4:]
        if not a.isdigit():
            a = int(dict[a])
        return 65535 - int(a)
    else:
        if not input.isdigit():
            input = int(dict[input])
        return int(input)


def runCircuit(wires, operations):
    while "a" not in wires.keys():
        for operation in operations:
            input, wire = operation.split(" -> ")

            try:
                if wire in wires.keys():
                    continue
                wires[wire] = calculateInput(input, wires)
                # print("Completed operation: " + operation)
            except:
                something = 0
                # print("Skipping operation: " + operation)

    return wires


wires = runCircuit(wires, operations)

print(str(wires["a"]))

newWires = {"b": wires["a"]}

newWires = runCircuit(newWires, operations)

print(str(newWires["a"]))
