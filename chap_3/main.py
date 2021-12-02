from turtle import Screen
import time

from chap_13.ball import Ball
from chap_3.paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# paddle
paddle = Paddle((0, -260))
ball = Ball()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.xcor() > 280 or ball.ycor() < 280:
        print("hello")

screen.exitonclick()