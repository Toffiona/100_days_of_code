from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        y_position = random.randint(-250, 250)
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.setheading(180)
        self.goto(360, y_position)
        self.color(random.choice(COLORS))
        self.speed_level = STARTING_MOVE_DISTANCE
        

    def move(self):
        self.forward(self.speed_level)

    def up_speed(self):
        self.speed_level += MOVE_INCREMENT
