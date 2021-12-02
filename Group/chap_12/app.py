from turtle import Turtle, Screen
import random

toby = Turtle()
colors = ["red", "green", "pink", "blue", "red", "green", "pink", "blue"]
size = 100


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        toby.forward(size)
        toby.right(angle)


for shape_side_n in range(3, 11):
    toby.color(random.choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()