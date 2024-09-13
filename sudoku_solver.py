def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def is_valid(board, num, pos):
    row, col = pos

    # Check the row
    for i in range(9):
        if board[row][i] == num and col != i:
            return False

    # Check the column
    for i in range(9):
        if board[i][col] == num and row != i:
            return False

    # Check the 3x3 grid
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # Row, Col of empty cell
    return None

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True  # Solved
    else:
        row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Backtrack

    return False

# Example unsolved Sudoku board (0 represents an empty cell)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Original Board:")
print_board(board)

if solve_sudoku(board):
    print("\nSolved Sudoku Board:")
    print_board(board)
else:
    print("No solution exists.")
