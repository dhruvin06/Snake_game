from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

score = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    # gives time between update and tracer else as soon as a set gets updated tracer switches off the animation
    # and you cannot se the update and will directly see the end update
    time.sleep(0.05)
    snake.move()
    # detecting the collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update()

    # detecting collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    #detecting collision with tail
    for x in snake.turtle_list:
        if x == snake.head:
            pass
        elif snake.head.distance(x)<10:
            game_is_on=False
            score.game_over()

screen.exitonclick()
