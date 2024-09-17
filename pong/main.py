"""
main.py
Driver code for the pong game

Use W and S to control the left paddle, and Up and Down for the right paddle
Every time the ball goes past a paddle, the other player gains a point!
The game doesn't end - the score currently goes up to infinity

You can quit the game by closing the window.

Inspired by day 22 of 100 days of code
"""
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# set up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

# create objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.update()

# set up event listeners
screen.listen()
screen.onkeypress(key='w', fun=l_paddle.up)
screen.onkeypress(key='s', fun=l_paddle.down)
screen.onkeypress(key='Up', fun=r_paddle.up)
screen.onkeypress(key='Down', fun=r_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    # check collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.wall_bounce()

    # check collision with left paddle
    if ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.left_paddle_bounce()

    # check collision with right paddle
    elif ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.right_paddle_bounce()

    # check if right paddle missed ball
    elif ball.xcor() > 380:
        scoreboard.l_point()
        ball.refresh()

    # check if left paddle missed ball
    elif ball.xcor() < -380:
        scoreboard.r_point()
        ball.refresh()

    screen.update()

screen.exitonclick()
