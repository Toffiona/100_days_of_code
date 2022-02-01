from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self,x, y):
        super().__init__()
        self.penup()
        self.goto(x,y)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.score_cal()

    def score_cal(self):
        self.clear()
        self.write(f"Score: {self.score}",False,align = "center", font = ("Arial", 20, "normal"))
        self.score += 1