from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    return tim.forward(100)

# get hold of the screen object to ask it to start listening
screen.listen()
# once the screen start listening, we have to buy a function that will be triggered
# when a key is pressed on keyboard. example of key : "a", "space"
# use even listener ex. onkeymethod
screen.onkey(key = "space", fun = move_forward)
#note: no parenthesis when passing a function as an argument in another function

screen.exitonclick()