from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.color("white")
        self.game_is_on = True
        

    def move(self):
        if self.game_is_on:
            self.forward(MOVE_DISTANCE)

    def restart(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()

    

