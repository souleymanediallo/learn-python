from turtle import Turtle, Screen
import random

colors = ["red", "green", "pink", "blue", "red", "green", "pink", "blue"]
angle_turtle = [0, 90, 180, 270]

tomy = Turtle()
tomy.pensize(10)
tomy.speed("fastest")

for _ in range(200):
    tomy.color(random.choice(colors))
    tomy.forward(30)
    tomy.setheading(random.choice(angle_turtle))


screen = Screen()
screen.exitonclick()

