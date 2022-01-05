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

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(120)

# timmy.left(120)

# for _ in range(4):
#     timmy.right(90)
#     timmy.forward(100)


def draw_polygon(side):
    change_color()
    angle = 360 / side
    for _ in range(side):
        timmy.right(angle)
        timmy.forward(100)
        
for draw in range(3, 9):
    draw_polygon(draw)

screen = Screen()
screen.exitonclick()