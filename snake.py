import tkinter as tk
import random

# Game constants
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#0000FF"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self, canvas):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        self.canvas = canvas

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self, canvas):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food, canvas, window, label):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates = [[x, y]] + snake.coordinates[:-1]

    for index, (x, y) in enumerate(snake.coordinates):
        canvas.coords(snake.squares[index], x, y, x + SPACE_SIZE, y + SPACE_SIZE)

    # Check for collisions
    if check_collisions(snake):
        game_over(window, canvas)

        
    else:
        # Check if snake eats food
        if snake.coordinates[0] == food.coordinates:
            snake.coordinates.append(snake.coordinates[-1])
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
            snake.squares.append(square)
            canvas.delete("food")
            food = Food(canvas)
            global score

            score += 1
            label.config(text="Score: {}".format(score))

        window.after(SPEED, next_turn, snake, food, canvas, window, label)

def change_direction(new_direction):
    global direction
    if new_direction == "left" and direction != "right":
        direction = "left"
    elif new_direction == "right" and direction != "left":
        direction = "right"
    elif new_direction == "up" and direction != "down":
        direction = "up"
    elif new_direction == "down" and direction != "up":
        direction = "down"

def check_collisions(snake):
    x, y = snake.coordinates[0]

    # Check if snake hits the walls
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    # Check if snake hits itself
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over(window, canvas):
    canvas.delete(tk.ALL)
    canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2, text="GAME OVER", fill="red", font=("consolas", 70))

# Initialize window
window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"

label = tk.Label(window, text="Score: {}".format(score), font=("consolas", 40))
label.pack()

canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Center the game window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create snake and food objects
snake = Snake(canvas)
food = Food(canvas)

# Bind keys for direction changes
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

# Start the game
next_turn(snake, food, canvas, window, label)

# Run the window loop
window.mainloop()
