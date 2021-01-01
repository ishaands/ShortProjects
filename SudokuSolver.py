# Sudoku Solving Algorithm

# Sudoku Board
board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

# Print Board
def printBoard(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
        print('\n')

# Checks Input Validity (i is row, j is column)
def validInput(board, n, i, j):
    # check row
    if n in board[i]:
        return False

    # check column
    for k in range(9):
        if board[k][j] == n:
            return False

    # check box
    for k in range(3 * (i // 3), 3 * (i // 3) + 3):
        for l in range(3 * (j // 3), 3 * (j // 3) + 3):
            if board[k][l] == n:
                return False

    # check diagonal (only used in X-Sudoku)
    # if i == j:
    #     for k in range(9):
    #         if board[k][k] == n:
    #             return False
    # if 8-i == j:
    #     for k in range(9):
    #         if board[8-k][k] == n:
    #             return False

    return True

# Empty-Box Finder
def findEmptyBox(board, currentBox):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                currentBox[0] = i
                currentBox[1] = j
                return True
    return False

# Recursive Top Function
def sudokuSolver(board):
    currentBox = [0, 0]
    if not findEmptyBox(board, currentBox):
        return True
    currentRow = currentBox[0]
    currentCol = currentBox[1]

    for i in range(1, 10):
        if validInput(board, i, currentRow, currentCol):
            board[currentRow][currentCol] = i
            if sudokuSolver(board):
                return True
            else:
                board[currentRow][currentCol] = 0

# Driver Code
if sudokuSolver(board):
    print(printBoard(board))
else:
    print('No solutions exist :(')

# Time Complexity: O(9^(n^2)), but early pruning will improve average-case performance
# Space Complexity: O(n^2)

