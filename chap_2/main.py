from turtle import Screen
from chap_2.paddle import Paddle
from chap_2.ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))

ball = Ball()

game_is_on = True


screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")

screen.onkey(r_paddle.go_up, "t")
screen.onkey(r_paddle.go_down, "b")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()