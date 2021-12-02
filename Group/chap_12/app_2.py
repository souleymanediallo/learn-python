from turtle import Turtle, Screen
import random

tomy = Turtle()
tomy.pencolor("#33cc8c")


colors = ["red", "green", "pink", "blue", "red", "green", "pink", "blue"]
angle_turtle = [0, 90, 180, 270]


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tomy.pensize(10)
tomy.speed("fastest")

for _ in range(200):
    tomy.color(random_colors())
    tomy.forward(30)
    tomy.setheading(random.choice(angle_turtle))


screen = Screen()
screen.exitonclick()

