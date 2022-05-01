from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.speed(1)
        self.goto(x_pos, y_pos)

    def up(self):
        new_pos_y = self.ycor() + 10
        return self.goto(self.xcor(), new_pos_y)

    def down(self):
        new_pos_y = self.ycor() - 10
        return self.goto(self.xcor(), new_pos_y)





