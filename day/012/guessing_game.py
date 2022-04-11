#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode)

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

answer = randint(1, 100)

def set_difficulty():
    """Lets the player choose between hard and easy level"""

    user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if user_choice == "easy":
         return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS



print(logo)

print(f"""{'-'*40}
Welcome to the Number Guessing Game!\n
I'am thinking of a number between 1 and 100\n
Pssst, the correct answer is {answer}

{'-'*40}\n""")

chosen_level = set_difficulty()

def checking_answer():
    global chosen_level
    """checks answer against guess. Returns the number of turns remaining."""
    for i in range(0, chosen_level):
        print(f"You have {chosen_level} attempts remaining to guess the number.")
        chosen_level -= 1

        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"You got it! The answer was {answer}.")
            exit()
        elif guess > answer:
            print("Too high.")
        elif guess < answer:
            print("Too low.")

checking_answer()


# End of program that won't' accessed if the player guesses the right answer
print("You have run out of guesses, you lose.")

