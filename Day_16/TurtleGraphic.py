
#TODO1 Construct an object

#import turle module
from turtle import Turtle, Screen, forward

# create new object from Turle class and save it in to an object called timmy
timmy = Turtle()
#change the objeact shape to turtle
timmy.shape("turtle")
timmy.color("blue")
# print the object
print(timmy)


def move_forward(turtle, space):
    return (turtle.forward(space))

move_forward(timmy,100)

#Object's attributes
#object.attributes

my_screen = Screen()
print(my_screen)
print(my_screen.canvheight)

# METHOD: call a function associated with the object
my_screen.exitonclick()






