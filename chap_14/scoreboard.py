from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 260)
        self.score = 0
        self.write("Votre score est : ", self.score, font=FONT)

