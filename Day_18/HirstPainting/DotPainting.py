import random
color_list = [(199, 168, 94), (227, 239, 232), (129, 179, 191), (163, 58, 78), (234, 221, 121), (49, 113, 167), (241, 217, 222), (104, 87, 83), (143, 187, 119), (239, 245, 249), (216, 151, 171), (67, 125, 76), (94, 124, 180), (85, 165, 94), (190, 71, 90), (161, 34, 49), (142, 119, 116), (221, 173, 182), (175, 205, 174), (163, 202, 211), (204, 116, 48), (75, 60, 56), (67, 56, 52), (176, 190, 213)]

from turtle import Turtle, Screen, colormode
colormode(255)
tim = Turtle()
tim.speed(0)
tim.hideturtle()


def draw_dots(num_of_dots):
    for _ in range(num_of_dots):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.forward(50)
        
def positioning(num_of_row, num_of_dots):
    y_distance = -200
    for _ in range(num_of_row):
        tim.penup()
        tim.setpos(-200, y_distance)
        draw_dots(num_of_dots)
        y_distance += 50

positioning(10, 10)


screen = Screen()
screen.exitonclick()