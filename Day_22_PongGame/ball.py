from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.penup()
        new_x = self.xcor() + self.x_move
        new_y= self.ycor() + self.y_move
        return self.goto(new_x, new_y)
        
    def wall_bounce(self):
        self.y_move *= -1
        # self.goto(new_x, new_y)

    def bounce(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0,0)
        self.x_move *= -1
        
        
                    

            
            