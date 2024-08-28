"""
commands.py

Contains all the functions that allows the cursor to move
in the etch-a-sketch program
"""

speed = 10


def move_forward(t):
    t.forward(speed)


def move_backward(t):
    t.backward(speed)


def turn_counter_clockwise(t):
    t.left(10)


def turn_clockwise(t):
    t.right(10)


def clear(t):
    t.clear()
    t.penup()
    t.home()
    t.setheading(0)
    t.pendown()


def make_pen_thick(t):
    t.turtlesize(2, 2)
    t.pensize(10)


def make_pen_thin(t):
    t.turtlesize(1, 1)
    t.pensize(1)


def teleport(t, screen):
    far_right = screen.window_width() // 2
    bottom = -screen.window_height() // 2
    x = screen.numinput("Teleport", f"x co-ordinate ({-far_right} to {far_right}): ")
    if x:
        y = screen.numinput("Teleport", f"y co-ordinate ({bottom} to {bottom}):")
        if y:
            t.penup()
            t.goto(x, y)
            t.pendown()
    screen.listen()


def black(t):
    t.color('black')


def blue(t):
    t.color('blue')


def green(t):
    t.color('green')


def purple(t):
    t.color('purple')


def red(t):
    t.color('red')


def yellow(t):
    t.color('yellow')
