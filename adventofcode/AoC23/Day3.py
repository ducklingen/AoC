from adventofcode.helpers import AoCHelper, GlobalVariables
import re

engine = AoCHelper.read_input_lines("Day3/inputs1.txt")
digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
different_neighbours = set()

def has_adjacent_symbols(x: int, y: int, len: int, engine, number: int) -> bool:
    directions = GlobalVariables.all_directions.copy()
    directions.remove((0, 1))
    neighbours = AoCHelper.get_neighbours(x, y, engine, directions)
    if set(neighbours) - digits != {'.'}:
        print(f"{number} has non-trivial neighbours {set(neighbours) - {'.'}}")
        different_neighbours.update(neighbours)
        return True

    if len > 1:
        directions.remove((0, -1))
        for i in range(len - 1):
            neighbours = AoCHelper.get_neighbours(x, y + i, engine, directions)
            if set(neighbours) - digits != {'.'}:
                print(f"{number} has non-trivial neighbours {set(neighbours) - {'.'}}")
                different_neighbours.update(neighbours)
                return True

        directions.append((0,1))
        neighbours = AoCHelper.get_neighbours(x, y + len - 1, engine, directions)
        if set(neighbours) - digits != {'.'}:
            print(f"{number} has non-trivial neighbours {set(neighbours) - {'.'}}")
            different_neighbours.update(neighbours)
            return True

    return False

result = 0
real_numbers = []
for row_id, row in enumerate(engine):
    pattern = r'([-]?[1-9]\d*)'

    numbers = [(int(match.group()), match.start()) for match in re.finditer(pattern, row)]

    for n, idx in numbers:
        print(f"Checking number {n}")
        if has_adjacent_symbols(row_id, idx, len(str(n)), engine, n):
            real_numbers.append(n)
            result += n


print(different_neighbours)
print(result)