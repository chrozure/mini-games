"""
scoreboard.py
Keeps track of the player's score and displays it at the top of the screen
"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")
SMALL_FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 260)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -30)
        self.write("Click to exit", align=ALIGNMENT, font=SMALL_FONT)