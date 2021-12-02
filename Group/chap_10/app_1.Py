from turtle import Turtle, Screen
import random
import time

is_race_on = False

screen = Screen()
screen.title("Application Game")
screen.setup(width=600, height=600)
screen.bgcolor("red")
user_bet = screen.textinput(title="Choisir un joueur", prompt="Quel choisir va gagner")

position_x = [(-300, 0), (-300, 40), (-300, 80)]
all_colors = ["green", "white", "black"]

all_turtles = []

for turtle in range(0, 3):
    toby = Turtle(shape="turtle")
    toby.color(all_colors[turtle])
    toby.penup()
    toby.goto(position_x[turtle])
    all_turtles.append(toby)

if user_bet:
    is_race_on = True


while is_race_on:
    random_game = random.randint(0, 20)
    for new_turtle in all_turtles:
        new_turtle.forward(random_game)


screen.exitonclick()