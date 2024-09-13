import tkinter as tk
from tkinter import messagebox
import random

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.board = self.generate_board()
        self.create_board()

    def create_board(self):
        for row in range(9):
            for col in range(9):
                cell_value = self.board[row][col]
                if cell_value != 0:
                    # Prefilled cells
                    label = tk.Label(self.root, text=str(cell_value), font=("Arial", 18), width=2, height=1)
                    label.grid(row=row, column=col, padx=5, pady=5)
                    self.cells[row][col] = label
                else:
                    # Empty cells (where player can enter values)
                    entry = tk.Entry(self.root, font=("Arial", 18), width=2, justify='center')
                    entry.grid(row=row, column=col, padx=5, pady=5)
                    self.cells[row][col] = entry

        # Add a button to check the solution
        check_button = tk.Button(self.root, text="Check Solution", command=self.check_solution)
        check_button.grid(row=9, column=0, columnspan=9)

    def check_solution(self):
        for row in range(9):
            for col in range(9):
                if isinstance(self.cells[row][col], tk.Entry):
                    try:
                        # Get user input from each Entry cell
                        value = int(self.cells[row][col].get())
                    except ValueError:
                        # If not a valid number, show an error message
                        messagebox.showerror("Invalid input", "Please enter numbers between 1 and 9.")
                        return

                    # Check if the value is correct according to the Sudoku rules
                    if not self.is_valid_move(value, row, col):
                        messagebox.showerror("Incorrect", f"Incorrect value at row {row+1}, column {col+1}")
                        return

        messagebox.showinfo("Success", "Congratulations! You solved the Sudoku puzzle!")

    def is_valid_move(self, value, row, col):
        # Check if the value already exists in the row, column, or 3x3 grid
        for i in range(9):
            if value == self.board[row][i] or value == self.board[i][col]:
                return False

        # Check the 3x3 grid
        box_row_start = (row // 3) * 3
        box_col_start = (col // 3) * 3
        for i in range(box_row_start, box_row_start + 3):
            for j in range(box_col_start, box_col_start + 3):
                if value == self.board[i][j]:
                    return False

        return True

    def generate_board(self):
        # Generate a valid Sudoku board using a simple backtracking algorithm
        board = [[0 for _ in range(9)] for _ in range(9)]
        self.fill_board(board)
        self.remove_numbers(board)
        return board

    def fill_board(self, board):
        # Simple backtracking to fill the board
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)
                    for number in numbers:
                        if self.is_valid_move_in_board(board, number, i, j):
                            board[i][j] = number
                            if self.fill_board(board):
                                return True
                            board[i][j] = 0
                    return False
        return True

    def is_valid_move_in_board(self, board, number, row, col):
        # Check if the number is valid in the current position in the board
        for i in range(9):
            if board[row][i] == number or board[i][col] == number:
                return False

        box_row_start = (row // 3) * 3
        box_col_start = (col // 3) * 3
        for i in range(box_row_start, box_row_start + 3):
            for j in range(box_col_start, box_col_start + 3):
                if board[i][j] == number:
                    return False

        return True

    def remove_numbers(self, board):
        # Remove some numbers to create the puzzle
        # Higher number means more removed cells
        removal_count = random.randint(40, 55)
        while removal_count > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if board[row][col] != 0:
                board[row][col] = 0
                removal_count -= 1

if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()
