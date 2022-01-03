from turtle import Turtle, Screen, colormode, pencolor
from random import randint

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

def change_color():
    colormode(255)
    R = randint(0, 255)
    G = randint(0, 255) 
    B = randint(0, 255)
    timmy.pencolor(R, G, B)

for _ in range(4):
    timmy.forward(100)
    timmy.right(120)

timmy.left(120)

change_color()
for _ in range(4):
    timmy.right(90)
    timmy.forward(100)


def draw_polygon(angle, turn):
    change_color()
    for _ in range(turn):
        timmy.right(angle)
        timmy.forward(100)
    

draw_polygon(72,5)

draw_polygon(60,6)

draw_polygon(51.43,7)

draw_polygon(45,8)
         


screen = Screen()
screen.exitonclick()