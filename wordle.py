import os
import random

def clear_screen():
    os.system("clear")

GREEN = "\u001b[32m"
YELLOW = "\u001b[33m"
RESET = "\u001b[0m"

print("Wordle Time")

# Define a function to select a random word from the file
def random_word():
    with open("rand.txt") as f:
        file_content = f.read().splitlines()  # Split lines to get a list of words
        return random.choice(file_content)

right = random_word()  # Call the function to get a random word

for _ in range(6):
    guess = input("Please guess a 5 letter wordle => ").upper()

    if len(guess) != 5:
        print("Word not allowed, it has to be 5 letters")
        continue

    for i in range(5):
        if guess[i] == right[i]:
            print(f"{GREEN}{guess[i]}{RESET}", end="")
        elif guess[i] in right:
            print(f"{YELLOW}{guess[i]}{RESET}", end="")
        else:
            print(guess[i], end="")

    print()

    if guess == right:
        print("You Win!!")
        break
else:
    print(f"Sorry, the right word is {right}")
