from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        file = open("data.txt", mode="r")
        self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High score : {self.highscore}", align="center",
                   font=("Arial", 8, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            file = open("data.txt", mode="w")
            file.write(str(self.highscore))
            self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game Over", align="center", font=("Arial", 12, "normal"))
