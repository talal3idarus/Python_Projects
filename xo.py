import tkinter as tk
from tkinter import messagebox

# Create the main game window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Variables
current_player = "X"
game_board = [" " for _ in range(9)]
buttons = []

# Function to check if there's a winner
def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if game_board[combo[0]] == game_board[combo[1]] == game_board[combo[2]] and game_board[combo[0]] != " ":
            return game_board[combo[0]]
    return None

# Function to handle the player's move
def handle_click(index):
    global current_player

    if game_board[index] == " ":
        game_board[index] = current_player
        buttons[index].config(text=current_player)

        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif " " not in game_board:
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            # Switch the player
            current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global game_board, current_player
    game_board = [" " for _ in range(9)]
    current_player = "X"
    for button in buttons:
        button.config(text=" ")

# Create the Tic-Tac-Toe board with buttons
for i in range(9):
    button = tk.Button(root, text=" ", font=('consolas', 40), width=5, height=2, 
                       command=lambda i=i: handle_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Start the game loop
root.mainloop()
