import tkinter as tk
import random
from tkinter import messagebox
import time

# Create the main game window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Variables
player_choice = ""
computer_choice = ""
choices = ["Rock", "Paper", "Scissors"]

# Function to handle the player's choice
def make_choice(choice):
    global player_choice, computer_choice
    player_choice = choice
    computer_choice = random.choice(choices)
    
    # Display the loading label
    loading_label.config(text="Loading...")
    
    # Disable buttons to prevent multiple clicks during loading
    rock_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissors_button.config(state="disabled")
    
    # After 2 seconds, display the result
    root.after(900, display_result)

# Function to display the result after loading
def display_result():
    result = check_winner(player_choice, computer_choice)
    
    # Update the loading label to show the result
    loading_label.config(text=result)
    
    # Enable buttons again
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")

# Function to check the winner
def check_winner(player, computer):
    if player == computer:
        return f"Both chose {player}. It's a tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return f"You chose {player}, Computer \n chose {computer}. You win!"
    else:
        return f"You chose {player}, Computer \n chose {computer}. You lose!"

# UI Elements
label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("consolas", 20))
label.pack(pady=20)

# Loading label (initially empty)
loading_label = tk.Label(root, text="", font=("consolas", 20))
loading_label.pack(pady=20)

# Buttons for Rock, Paper, and Scissors
rock_button = tk.Button(root, text="Rock", font=("consolas", 20), command=lambda: make_choice("Rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", font=("consolas", 20), command=lambda: make_choice("Paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", font=("consolas", 20), command=lambda: make_choice("Scissors"))
scissors_button.pack(pady=10)

# Start the game loop
root.mainloop()
