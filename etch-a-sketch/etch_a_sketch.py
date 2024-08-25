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


def teleport():
    x = screen.numinput("Teleport", "x co-ordinate: ")
    y = screen.numinput("Teleport", "y co-ordinate: ")
    t.penup()
    t.goto(x, y)
    t.pendown()
    screen.listen()


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
screen.onkey(key='t', fun=teleport)


screen.exitonclick()
