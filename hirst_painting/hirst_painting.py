"""
hirst_painting.py
A program which randomly generates a piece of art inspired by Damien Hirst's spot paintings
https://www.artsy.net/artist-series/damien-hirst-spots

Once the painting is complete, click on the screen to exit.

Inspired by 100 Days of Code day 18
"""

from turtle import Turtle, Screen, colormode
import random

colormode(255)

t = Turtle()
screen = Screen()

t.penup()
t.hideturtle()
t.speed('fast')
t.goto(-225, -225)
for i in range(10):
    for j in range(10):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        t.dot(20, (r, g, b))
        t.forward(50)

    # Move to next line
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)

screen.exitonclick()
