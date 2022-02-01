from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.setposition(x_position, 0)
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)

    def go_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 50)
    
    
    def go_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 50)