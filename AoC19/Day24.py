from helpers import AoCHelper

def convertInputToBoard(lines):
    board = []

    for line in lines:
        row = []

        for i in range(len(line)):
            if line[i] == "#":
                row.append(1)
            elif line[i] == ".":
                row.append(0)

        board.append(row)

    return board
def printBoard(board):
    for row in board:
        rowAsString = ""

        for i in range(len(row)):
            if row[i] == 1:
                rowAsString += "#"
            else:
                rowAsString += "."

        print(rowAsString)
def amountOfNeighbouringBugs(board, x, y):
    neighbouringBugs = 0

    if x > 0:
        neighbouringBugs += board[x - 1][y]
    if y > 0:
        neighbouringBugs += board[x][y - 1]
    if x < 4:
        neighbouringBugs += board[x + 1][y]
    if y < 4:
        neighbouringBugs += board[x][y + 1]

    return neighbouringBugs
def calculateNextStateOfPoint(board, x, y):
    if board[x][y] == 1:
        result = 1 if amountOfNeighbouringBugs(board, x, y) == 1 else 0
    elif board[x][y] == 0:
        result = 1 if amountOfNeighbouringBugs(board, x, y) in (1, 2) else 0

    return result
def passTime(board):
    newBoard = [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]

    for i in range(5):
        for j in range(5):
            newBoard[i][j] = calculateNextStateOfPoint(board, i, j)

    return newBoard

lines = AoCHelper.readInputLines("day24input.txt")

board = convertInputToBoard(lines)

def boardAsString(board):
    boardAsString = ""

    for x in range(5):
        for y in range(5):
            boardAsString += str(board[x][y])

    return boardAsString


# for i in range(5):
#     print(boardAsString(board))
#     board = passTime(board)
#     print("-----------------")

steps = 0
boardsAsSet = set([])

boardString = ""

while steps == 0 or boardString not in boardsAsSet:
    steps = steps + 1
    boardsAsSet.add(boardString)
    board = passTime(board)
    boardString = boardAsString(board)

    # if steps % 1000 == 0:
    #     print(steps)

printBoard(board)
print(boardString)
print(steps - 1)

result = 0

for i in range(len(boardString)):
    if int(boardString[i]) == 1:
        result += 2 ** i

print(result)
