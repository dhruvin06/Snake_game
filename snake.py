from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]

    def create_snake(self):
        for x in POSITIONS:
            self.add_segment(x)

    def add_segment(self, x):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(x)
        self.turtle_list.append(turtle)

    def extend(self):
        self.add_segment(self.turtle_list[-1].position())

    def move(self):
        for x in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[x - 1].xcor()
            new_y = self.turtle_list[x - 1].ycor()
            self.turtle_list[x].goto(x=new_x, y=new_y)
        self.turtle_list[0].forward(10)

    def snake_reset(self):
        for x in self.turtle_list:
            x.goto(1000, 1000)
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
