from turtle import Turtle, Screen
import random
import turtle as t

t.colormode(255)

tomy = Turtle()

colors = ["red", "green", "orange", "purple", "blue", "brown"]
directions = [0, 90, 180, 270]


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_colors = (r, g, b)
    return r_colors


tomy.speed("fastest")


def draw_circle(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tomy.color(random_colors())
        tomy.circle(100)
        tomy.setheading(tomy.heading() + size_of_gap)


draw_circle(6)

screen = Screen()
screen.exitonclick()