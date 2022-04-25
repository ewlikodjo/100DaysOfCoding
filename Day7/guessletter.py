# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
count = 0


guess = input(str("Guess letter: "))

if guess not in chosen_word:
    print("game over")

else:
    print("whoo it mused!")

print(guess.upper())
print(chosen_word.upper())
