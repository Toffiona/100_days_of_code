import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer()
screen.listen()

player = Player()

screen.onkey(player.move, "Up")

game_is_on = True


car = CarManager()
game_loop = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car = CarManager()
    car.move()
    
    
    
    if player.ycor() > 300:
        player.restart()
        car.up_speed()












screen.exitonclick()