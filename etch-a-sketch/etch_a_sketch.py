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

FONT = ("Helvetica", 16, "normal")
COLOURS = [('black', 'b'), ('blue', 'l'), ('green', 'g'), ('purple', 'p'), ('red', 'r'), ('yellow', 'y')]

screen = Screen()
FAR_RIGHT = screen.window_width() // 2
BOTTOM = -screen.window_height() // 2
screen.title("Etch-A-Sketch")

t = Turtle()
speed = 10


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

    guide.forward(60)
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


# Turtle functionality
def move_forward():
    t.forward(speed)


def move_backward():
    t.backward(speed)


def turn_counter_clockwise():
    t.left(10)


def turn_clockwise():
    t.right(10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.setheading(0)
    t.pendown()


def make_pen_thick():
    t.turtlesize(2, 2)
    t.pensize(10)


def make_pen_thin():
    t.turtlesize(1, 1)
    t.pensize(1)


def teleport():
    x = screen.numinput("Teleport", f"x co-ordinate ({-FAR_RIGHT} to {FAR_RIGHT}): ")
    if x:
        y = screen.numinput("Teleport", f"y co-ordinate ({BOTTOM} to {BOTTOM}):")
        t.penup()
        t.goto(x, y)
        t.pendown()
    screen.listen()


def black():
    t.color('black')


def blue():
    t.color('blue')


def green():
    t.color('green')


def red():
    t.color('red')


def purple():
    t.color('purple')


def yellow():
    t.color('yellow')


show_controls()
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='Up', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key='a', fun=turn_counter_clockwise)
screen.onkey(key="Left", fun=turn_counter_clockwise)
screen.onkey(key='d', fun=turn_clockwise)
screen.onkey(key="Right", fun=turn_clockwise)
screen.onkey(key='c', fun=clear)
screen.onkey(key='q', fun=make_pen_thin)
screen.onkey(key='e', fun=make_pen_thick)
screen.onkey(key='t', fun=teleport)
screen.onkey(key='b', fun=black)
screen.onkey(key='l', fun=blue)
screen.onkey(key='r', fun=red)
screen.onkey(key='p', fun=purple)
screen.onkey(key='y', fun=yellow)

screen.exitonclick()
