from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POSITION_Y = [-200, -150, -50, 0, 50, 100, 200]


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.create_car()

    def create_car(self):
        for car in range(6):
            self.shape("square")
            self.penup()
            self.shapesize(1, 3)
            self.goto(280, POSITION_Y[car])
            self.color(COLORS[car])





