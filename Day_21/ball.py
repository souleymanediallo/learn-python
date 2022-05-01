from turtle import Turtle


class Ball(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(x_pos, y_pos)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        return self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

