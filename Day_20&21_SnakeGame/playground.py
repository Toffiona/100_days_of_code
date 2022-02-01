from turtle import Turtle, Screen
screen = Screen()

joe = Turtle()
joe.shape("circle")
joe.shapesize(5,2)
joe.forward(30)

hen = Turtle()
hen.shape("turtle")
hen.shapesize(2,4)
hen.goto(100,100)

print(joe.distance(hen))


screen.exitonclick()