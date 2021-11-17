from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Application SD", prompt="A quel joueur va gagner ?")
# E = 0, N = 90, W=180, S = 270

colors_turtle = ["green", "red", "yellow", "pink", "blue", "black"]
y_positions = [-90, -40, 0, 40, 70, 120]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors_turtle[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()