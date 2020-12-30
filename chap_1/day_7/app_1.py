import random

word_list = ["Marseille", "Paris", "Toulouse"]

chosen_word = random.choice(word_list)

guess_letter = input("Guess a letter please ? ").lower()

for letter in chosen_word:
    if letter == guess_letter:
        print("Right")
    else:
        print("Wrong")



