from turtle import Turtle
DISTANCE = 20
class Snake:
    def __init__(self):
        start_position = [(0,0), (-20,0), (-40,0)]
        self.segments = []
        for position in start_position:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.segments.append(snake)
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        
      

    def move(self):
        
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        return self.head.forward(DISTANCE)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        
    def add_segment(self):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        new_x = self.segments[len(self.segments) - 1].xcor()
        new_y = self.segments[len(self.segments) - 1].ycor()
        snake.goto(new_x, new_y)
        self.segments.append(snake)

    
    def hit(self):
        for segment in range(1, len(self.segments)):
            if self.head.distance(self.segments[segment]) < 1:
                return True


