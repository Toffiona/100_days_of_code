FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score_cal()

    def score_cal(self):
        self.clear()
        self.setposition(0,250)
        self.write(f"Level = {self.score}", True, align = "center", font =FONT)
        self.score += 1
        
    def game_over(self): 
        self.goto(0,0)   
        self.write("GAME OVER", True, align = "center", font =FONT)   
