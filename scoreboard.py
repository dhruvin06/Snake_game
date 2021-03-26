from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.write(arg=f"Score = {self.score - 1}", align="center", font=("Arial", 8, "normal"))

    def update(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=("Arial", 12, "normal"))
