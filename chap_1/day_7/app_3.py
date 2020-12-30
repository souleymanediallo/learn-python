import random

my_list = ["Marseille", "Bordeaux", "Nice"]
choice_my_list = random.choice(my_list)
print(choice_my_list)

display = []
for _ in choice_my_list:
    display += "_"

print(display)

my_choice = input("Guess a letter ")

for position in range(len(choice_my_list)):
    letter = choice_my_list[position]
    if letter == my_choice:
        display[position] = letter

print(display)
