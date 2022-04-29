import turtle as turtle_module
import random

colors_list = [(254, 253, 253), (101, 190, 171), (100, 164, 209), (207, 137, 182), (213, 230, 240), (56, 179, 154), (49, 124, 170), (187, 222, 211), (25, 26, 26), (217, 163, 85), (239, 212, 97), (189, 89, 132), (124, 73, 114), (160, 209, 185), (89, 126, 186), (237, 160, 182), (242, 206, 217), (51, 154, 194), (46, 134, 112), (64, 30, 45), (136, 83, 61), (90, 49, 60), (143, 207, 229), (175, 185, 215), (185, 134, 58), (224, 175, 169), (213, 73, 61), (29, 32, 50), (98, 48, 45), (45, 57, 96)]

turtle_module.colormode(255)

tomy = turtle_module.Turtle()
tomy.up()
tomy.setheading(225)
tomy.forward(300)
tomy.setheading(0)

for _ in range(10):
    tomy.dot(20, random.choice(colors_list))
    tomy.forward(50)

screen = turtle_module.Screen()
screen.exitonclick()

