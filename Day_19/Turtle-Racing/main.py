from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?, enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
def turtle(name, color, y_num):

    name = Turtle(shape="turtle")
    #tim.shape("turtle")
    name.penup()
    name.color(colors[color])
    name.goto(-230, y_num)
    turtle_list.append(name)


turtle("tim", 0, -20)
turtle("tom", 1, 20)
turtle("jerry", 2, -60)
turtle("toffee", 3, 60)
turtle("fioka", 4, -100)
turtle("rosie", 5, 100)

print(turtle_list)

if user_bet:
    race_is_on = True

while race_is_on:    
    for turtle in turtle_list:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            race_is_on = False
            if user_bet == winning_color:
                print(f"You have won!. The winning turtle is {winning_color}")
            else:
                print(f"You have lost!. The winning turtle is {winning_color}") 


screen.exitonclick()