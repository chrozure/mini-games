"""
paddle.py
Contains implementation for the Paddle class

Paddles can be moved up and down on the screen
using different buttons (explained in main.py)
"""
from turtle import Turtle

SPEED = 20


class Paddle(Turtle):

    def __init__(self, coord):
        super().__init__("square")
        self.penup()
        self.speed('fastest')
        self.shapesize(1, 5)
        self.goto(coord)

        # set direction as upwards
        self.setheading(90)
        self.color('white')

    def up(self):
        if self.ycor() < 250:
            self.forward(SPEED)

    def down(self):
        if self.ycor() > -250:
            self.backward(SPEED)
