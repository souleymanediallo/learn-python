import turtle
position = [-100, -40, 0, 40, 120]
colors = ["red", "green", "yellow", "orange", "brown"]
is_race_on = False

screen = turtle.Screen()
screen.setup(500, 400)
user_belt = screen.textinput(title="Pariez maintenan", prompt="Indiquer votre couleurs ")

all_turtles = []
for turtle_position in range(0, 5):
    tomy = turtle.Turtle(shape="turtle")
    tomy.color(colors[turtle_position])
    tomy.up()
    tomy.goto(-200, position[turtle_position])
    all_turtles.append(tomy)

if user_belt:
    is_race_on = True

while is_race_on:
    for t in all_turtles:
        if t.xcor() > 200:
            is_race_on = False
            wining_color = t.pencolor()
            if wining_color == user_belt:
                print(f"Vous avez gagné {wining_color}")
            else:
                print(f"Vous avez perdu, la couleur {wining_color} a gagné !")

        t.forward(10)

screen.exitonclick()