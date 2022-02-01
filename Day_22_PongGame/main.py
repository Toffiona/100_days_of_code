from turtle import Turtle, Screen, exitonclick
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

paddle_r = Paddle(350)
paddle_l = Paddle(-350)
ball = Ball()
score_r = Scoreboard(200, 260)
score_l = Scoreboard(-200, 260)

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

sleep_time = 0.1
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        # while ball.xcor() < 380:            
            # screen.update()
            # time.sleep(0.02)  
            ball.wall_bounce()

    if ball.distance(paddle_r) < 60 and ball.xcor() == 330 or ball.distance(paddle_l) < 60 and ball.xcor() == -330:
        ball.bounce()
        if sleep_time > 0.05:
            sleep_time -= 0.01
        
        

    if ball.xcor() > 400:
        ball.reset()
        score_l.score_cal()

    if ball.xcor() < -400:
        ball.reset()
        sleep_time = 0.1
        score_r.score_cal()
        



screen.exitonclick()