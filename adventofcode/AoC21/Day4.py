from helpers import AoCHelper

input = AoCHelper.read_input_lines("day4/input1.txt")
numbers = AoCHelper.extract_numbers_from_line(input[0])


class BingoSheet:

    """Class representing af bingo sheet."""

    status = []
    sheet = []
    sheet_number = 0

    def __init__(self, sheet_numbers, sheet_index):
        self.sheet = sheet_numbers
        self.status = [0 for i in range(25)]
        self.sheet_number = sheet_index

    def update_status(self, number_picked):
        if number_picked in self.sheet:
            self.status[self.sheet.index(number_picked)] = 1

    def check_for_bingo(self):
        for j in range(5):
            if sum(self.status[j * 5 : j * 5 + 5]) == 5:
                return True

            if sum([self.status[k] for k in range(25) if k % 5 == j]) == 5:
                return True

        return False

    def get_score(self):
        return sum([k * (1 - n) for k, n in zip(self.sheet, self.status)])


def initialize_bingo(input_lines):
    sheet_objects = []
    sheets = AoCHelper.group_lines(input_lines[2:])

    for idx, sheet in enumerate(sheets):
        sheet_as_string = " ".join(sheet)
        sheet_as_number_list = AoCHelper.extract_numbers_from_line(
            sheet_as_string
        )
        sheet_objects.append(BingoSheet(sheet_as_number_list, idx))

    return sheet_objects


def run_game_easy(sheet_objects, numbers_picked):
    for k in numbers_picked:
        for sheet in sheet_objects:
            sheet.update_status(k)
            if sheet.check_for_bingo():
                return k * sheet.get_score()


def run_game_hard(sheet_objects, numbers_picked):
    sheets_left = sheet_objects

    for k in numbers_picked:
        survivor_list = []

        for sheet in sheets_left:
            sheet.update_status(k)
            if sheet.check_for_bingo():
                if len(sheets_left) == 1:
                    return k * sheets_left[0].get_score()
            else:
                survivor_list.append(sheet)

        sheets_left = survivor_list


# Part 1
game_sheets_easy = initialize_bingo(input)
score = run_game_easy(game_sheets_easy, numbers)
assert score == 89001
print(f"Part 1: {score}")

# Part 2
game_sheets_hard = initialize_bingo(input)
score = run_game_hard(game_sheets_hard, numbers)
assert score == 7296
print(f"Part 2: {score}")
