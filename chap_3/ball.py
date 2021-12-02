from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("white")
        self.x_position = 10
        self.y_position = 10

    def moove(self):
        new_x = self.xcor() - self.x_position
        new_y = self.ycor() - self.y_position
        return self.goto(new_x, new_y)

    def bounce(self):
        pass