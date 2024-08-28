"""
etch_a_sketch.py

A program that lets your artistic creativity shine!
You can control the cursor using WASD or the arrow keys
Other controls are:
    - c: clear
    - q: quit
    - t: teleport
    - b: set colour to black
    - l: set colour to blue
    - r: set colour to red
    - p: set colour to pink
    - y: set colour to yellow

Inspired from day 19 of 100 days of code
"""
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.title("Etch-A-Sketch")
speed = 10


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


def quit_game():
    screen.bye()


def teleport():
    x = screen.numinput("Teleport", "x co-ordinate: ")
    y = screen.numinput("Teleport", "y co-ordinate: ")
    t.penup()
    t.goto(x, y)
    t.pendown()
    screen.listen()


def black():
    t.color('black')


def blue():
    t.color('blue')


def red():
    t.color('red')


def pink():
    t.color('pink')


def yellow():
    t.color('yellow')


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
screen.onkey(key='q', fun=quit_game)
screen.onkey(key='t', fun=teleport)
screen.onkey(key='b', fun=black)
screen.onkey(key='l', fun=blue)
screen.onkey(key='r', fun=red)
screen.onkey(key='p', fun=pink)
screen.onkey(key='y', fun=yellow)

screen.exitonclick()
