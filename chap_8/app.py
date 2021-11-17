from turtle import Turtle, Screen

# https://realpython.com/beginners-guide-python-turtle/

toby = Turtle()
screen = Screen()
screen.setup(width=500, height=500)
screen.title("Application Souleymane")


def move_forwards():
    toby.forward(20)


def move_backwards():
    toby.backward(20)


def turn_right():
    toby.right(90)


def clear():
    toby.clear()
    toby.penup()
    toby.home()
    toby.pendown()


def turn_left():
    toby.left(90)


screen.listen()
screen.onkey(move_forwards, "f")
screen.onkey(move_backwards, "b")
screen.onkey(turn_left, "l")
screen.onkey(turn_right, "r")
screen.onkey(clear, "c")
screen.bgcolor("orange")
result = screen.textinput("NIM", "Name of first player:")
print(result)

screen.exitonclick()
