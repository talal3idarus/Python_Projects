import turtle as t

# Initialize player scores
playerAscore = 0
playerBscore = 0

# Create a window
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

# Create the left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# Create the right paddle (correct initial position)
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# Create the ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ballxdirection = 0.2
ballydirection = 0.2

# Create the pen for scorecard updates
pen = t.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=('Arial', 24, 'normal'))

# Moving the left paddle up
def leftpaddleup():
    y = leftpaddle.ycor()
    if y < 250:  # Limit paddle movement within window
        y += 20
    leftpaddle.sety(y)

# Moving the left paddle down
def leftpaddledown():
    y = leftpaddle.ycor()
    if y > -240:
        y -= 20
    leftpaddle.sety(y)

# Moving the right paddle up
def rightpaddleup():
    y = rightpaddle.ycor()
    if y < 250:
        y += 20
    rightpaddle.sety(y)

# Moving the right paddle down
def rightpaddledown():
    y = rightpaddle.ycor()
    if y > -240:
        y -= 20
    rightpaddle.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    # Border collision (top and bottom)
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection *= -1

    # Right paddle border (ball goes out of bounds)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection *= -1
        playerAscore += 1
        pen.clear()
        pen.write(f"Player A: {playerAscore}  Player B: {playerBscore}", align="center", font=('Arial', 24, 'normal'))

    # Left paddle border (ball goes out of bounds)
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdirection *= -1
        playerBscore += 1
        pen.clear()
        pen.write(f"Player A: {playerAscore}  Player B: {playerBscore}", align="center", font=('Arial', 24, 'normal'))

    # Ball collision with right paddle
    if (340 < ball.xcor() < 350) and (rightpaddle.ycor() - 50 < ball.ycor() < rightpaddle.ycor() + 50):
        ball.setx(340)
        ballxdirection *= -1

    # Ball collision with left paddle
    if (-350 < ball.xcor() < -340) and (leftpaddle.ycor() - 50 < ball.ycor() < leftpaddle.ycor() + 50):
        ball.setx(-340)
        ballxdirection *= -1
