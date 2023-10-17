from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_paddle_score = 0
        self.right_paddle_score = 0
        self.goto(-100, 180)
        self.write(self.left_paddle_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 180)
        self.write(self.right_paddle_score, align="center", font=("Courier", 80, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.left_paddle_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 180)
        self.write(self.right_paddle_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """Increases score of left paddle"""
        self.left_paddle_score += 1
        self.update_scoreboard()
    def r_point(self):
        """Increses score of right paddle"""
        self.right_paddle_score += 1
        self.update_scoreboard()