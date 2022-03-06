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
car = CarManager()
score = Scoreboard()

screen.onkey(player.move, "Up") 

game_is_on = True
 
loop_time = 0

while game_is_on: 
     
    time.sleep(0.1)
    screen.update()
    loop_time += 1
    if loop_time % 6 == 0:
        car.make_car()
    car.move()   
  
    
    if player.ycor() > 300:
        score.score_cal()
        player.restart()
        car.increase_speed()

    
    for the_car in car.car_list:
        if the_car.distance(player) < 25:
            game_is_on = False
            score.game_over()
            player.game_is_on = False
            

    



screen.exitonclick()