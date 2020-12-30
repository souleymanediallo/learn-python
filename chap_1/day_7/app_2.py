import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"The solution is {chosen_word}.")

display = []

for _ in range(len(chosen_word)):
    display += "_"

print(display)
guess = input("Guess a letter : ").lower()

end_of_game = False
while not end_of_game:
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
    print("You win.")


