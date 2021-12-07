from turtle import Screen
import time

from chap_14.car_manager import CarManager
from chap_14.player import Player
from chap_14.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("GAME")
screen.tracer(0)

car = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_forward, "Up")
screen.onkey(player.go_back, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
