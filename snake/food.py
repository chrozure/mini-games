"""
food.py
Contains the implementation of the Food class

The food gets randomly generated onto a spot on the screen.
"""

from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, snake):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=-0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh(snake)

    def refresh(self, snake):
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 260)
        # Ensure that new food doesn't touch snake
        while snake.touches(random_x, random_y):
            random_x = random.randint(-275, 275)
            random_y = random.randint(-275, 260)
        self.goto(random_x, random_y)
