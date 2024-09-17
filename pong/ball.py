"""
ball.py
Contains the implementation of the Ball class.

The ball bounces when it reaches the wall or a paddle,
and refreshes if it goes past a paddle.
It will slowly get faster as a rally goes on.
"""

from turtle import Turtle
import random

START_MOVE_SPEED = 0.05


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color('white')
        self.penup()
        self.dx = 10
        self.dy = 10
        self.move_speed = START_MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.dy *= -1

    def left_paddle_bounce(self):
        self.move_speed *= 0.95
        self.dx = 10 + random.randint(-3, 3)

    def right_paddle_bounce(self):
        self.move_speed *= 0.95
        self.dx = -10 + random.randint(-5, 5)

    def refresh(self):
        self.goto(0, 0)
        self.move_speed = START_MOVE_SPEED
        self.dx *= -1

