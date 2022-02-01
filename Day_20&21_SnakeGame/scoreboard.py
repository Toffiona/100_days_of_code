from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(0, 280)
        self.hideturtle()
        self.color("white")
        self.score = -1
        self.score_cal()

    def score_cal(self):
        self.clear()
        self.score +=1
        self.write("Score: " + str(self.score), False, align="center", font=('Arial', 12, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font=('Arial', 20, "normal"))

        