from turtle import Turtle
import random


# everytime an object for food is created a turtle is created as we have inherited turtle
class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        # how the turtle looks is written here
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("blue")
        self.speed("fastest")

    def refresh(self):
        # refreshing meaning everytime going to a new location
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
