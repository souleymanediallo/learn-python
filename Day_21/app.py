from turtle import Screen
import time
from Day_21.ball import Ball
from Day_21.paddle import Paddle
from Day_21.scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle(350, 0)
r_paddle = Paddle(-350, 0)
ball = Ball(0, 0)
scoreboard = Scoreboard()


screen.listen()
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")
screen.onkey(r_paddle.up, "t")
screen.onkey(r_paddle.down, "d")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.tracer(1)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
