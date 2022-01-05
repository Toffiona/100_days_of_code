from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
colormode(255)
########### Challenge 4 - Random Walk ########
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return tim.color(r , g, b)

tim.pensize(10)
# tim.speed(10)


def go_right():
    tim.setheading(0)
    tim.forward(20)
def go_left():
    tim.setheading(180)
    tim.forward(20)
def go_straight():
    tim.setheading(90)
    tim.forward(20)
def go_back():
    tim.setheading(270)
    tim.forward(20)

movement = [go_left, go_right, go_back, go_straight]

for _ in range(100):
    #tim.pencolor(random.choice(colours))
    random_colour()
    move = random.choice(movement)
    move()







screen = Screen()
screen.exitonclick()