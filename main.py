import turtle
import os
import winsound

wn = turtle.Screen()
wn.bgpic("milkyway.png")
wn.title("Pong by KevinT")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("PlayerA: 0 PlayerB: 0", align="center", font=("Courier", 24, "normal"))

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # speed of animation, max speed
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # speed of animation, max speed
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

# Center Line
for yCoordinate in range(10,300,30):
    center_line = turtle.Turtle()
    center_line.shape("square")
    center_line.penup()
    center_line.shapesize(stretch_wid=1,stretch_len=0.3)
    center_line.color("white")
    center_line.goto(0, yCoordinate)
    center_line_below = turtle.Turtle()
    center_line_below.shape("square")
    center_line_below.penup()
    center_line_below.shapesize(stretch_wid=1,stretch_len=0.3)
    center_line_below.color("white")
    center_line_below.goto(0, -yCoordinate)

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()  # listen for keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Code For Hitting the Ceiling
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    # Code For Hitting the Floor
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    # Code for Hitting the Right Outside
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        scoreboard.clear()
        scoreboard.write("PlayerA: {}  PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    # Code for Hitting the Left Outside
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        scoreboard.clear()
        scoreboard.write("PlayerA: {}  PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    # Code for ball being between yCoordinates of paddle, and halfway through the paddle width
    if 340 < ball.xcor() < 350 and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    # Code for ball being between yCoordinates of paddle, and halfway through the paddle width
    if -350 < ball.xcor() < -340 and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

