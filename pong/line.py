"""
line.py

Contains the implementation of the Line class
Simply draws a vertical line in the middle of the screen
"""

from turtle import Screen, Turtle


class Line(Turtle):
    def __init__(self):
        screen = Screen()
        height = screen.window_height() / 2

        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.pensize(3)

        self.goto(0, height)
        self.pendown()
        self.pencolor('white')

        self.setheading(270)

        while self.ycor() > -height:
            self.forward(20)
            self.penup()
            self.forward(10)
            self.pendown()

