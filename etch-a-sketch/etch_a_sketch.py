"""
etch_a_sketch.py

A program that lets your artistic creativity shine!
You can control the cursor using WASD or the arrow keys
Other controls are:
    - c: clear
    - q: make pen thin
    - e: make pen thick
    - t: teleport
    - b: set colour to black
    - l: set colour to blue
    - g: set colour to green
    - r: set colour to red
    - p: set colour to pink
    - y: set colour to yellow

To exit the program, simply click anywhere on the screen.

Inspired from day 19 of 100 days of code
"""

from turtle import Turtle, Screen
from commands import *

FONT = ("Helvetica", 16, "normal")
COLOURS = [('black', 'b'), ('blue', 'l'), ('green', 'g'), ('purple', 'p'), ('red', 'r'), ('yellow', 'y')]

screen = Screen()
screen.setup(width=960, height=675)
FAR_RIGHT = screen.window_width() // 2
BOTTOM = -screen.window_height() // 2
screen.title("Etch-A-Sketch")

t = Turtle()


def show_controls():
    guide = Turtle()
    guide.hideturtle()
    guide.speed('fastest')
    guide.penup()

    # make box at bottom right of screen
    guide.goto(FAR_RIGHT, BOTTOM + 180)
    guide.pendown()
    guide.backward(150)
    guide.goto(FAR_RIGHT - 150, BOTTOM)
    guide.penup()

    # write out controls
    guide.goto(FAR_RIGHT - 130, BOTTOM + 150)
    commands = ["clear - c", "thin - q", "thick - e", "teleport - t"]
    for command in commands:
        guide.write(command, align='left', font=FONT)
        guide.right(90)
        guide.forward(20)
        guide.left(90)

    guide.forward(5)

    # first column of colours
    num_colours = len(COLOURS)
    for color, command in COLOURS[:num_colours // 2]:
        guide.dot(16, color)
        guide.forward(15)
        guide.right(90)
        guide.forward(10)
        guide.write(f'- {command}', align="left", font=FONT)
        guide.forward(10)
        guide.left(90)
        guide.backward(15)

    guide.forward(65)
    guide.left(90)
    guide.forward(10 * num_colours)
    guide.right(90)

    # second column of colours
    for color, command in COLOURS[num_colours // 2:]:
        guide.dot(16, color)
        guide.forward(15)
        guide.right(90)
        guide.forward(10)
        guide.write(f'- {command}', align="left", font=FONT)
        guide.forward(10)
        guide.left(90)
        guide.backward(15)


show_controls()
screen.listen()
screen.onkey(key='w', fun=lambda: move_forward(t))
screen.onkey(key='Up', fun=lambda: move_forward(t))
screen.onkey(key='s', fun=lambda: move_backward(t))
screen.onkey(key="Down", fun=lambda: move_backward(t))
screen.onkey(key='a', fun=lambda: turn_counter_clockwise(t))
screen.onkey(key="Left", fun=lambda: turn_counter_clockwise(t))
screen.onkey(key='d', fun=lambda: turn_clockwise(t))
screen.onkey(key="Right", fun=lambda: turn_clockwise(t))
screen.onkey(key='c', fun=lambda: clear(t))
screen.onkey(key='q', fun=lambda: make_pen_thin(t))
screen.onkey(key='e', fun=lambda: make_pen_thick(t))
screen.onkey(key='t', fun=lambda: teleport(t, screen))
screen.onkey(key='b', fun=lambda: black(t))
screen.onkey(key='l', fun=lambda: blue(t))
screen.onkey(key='g', fun=lambda: green(t))
screen.onkey(key='p', fun=lambda: purple(t))
screen.onkey(key='r', fun=lambda: red(t))
screen.onkey(key='y', fun=lambda: yellow(t))

screen.exitonclick()
