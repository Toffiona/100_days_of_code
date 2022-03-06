from turtle import Turtle, Screen
import random
import time
screen = Screen
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.speed_level = 0
        

    def make_car(self):
    
        new_car = Turtle()
        y_position = random.randint(-250, 250)
        new_car.penup()
        new_car.speed(0)
        new_car.shape("square")
        new_car.shapesize(1, 2)
        new_car.setheading(180)
        new_car.goto(360, y_position)
        new_car.color(random.choice(COLORS))
        self.car_list.append(new_car)            
        

        
    def move(self):
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE + self.speed_level)

    def increase_speed(self):
        self.speed_level += MOVE_INCREMENT


    
