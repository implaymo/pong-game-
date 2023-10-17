import turtle
from turtle import Turtle


DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(position)

    # # # Change Paddles direction
    def up(self):
        y = self.ycor()
        y += DISTANCE
        self.sety(y)

    def down(self):
        y = self.ycor()
        y -= DISTANCE
        self.sety(y)

