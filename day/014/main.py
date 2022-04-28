import os
import random
from art import logo, vs
from game_data import data

def random_person(data):
    """Pick random data and address it to person."""
    person = random.choice(data)
    return person

def game_over(score):
    """Print the final score and end the game."""
    os.system("clear")
    print(f"{logo} \n Sorry, that's wrong. Final score: {score}'")

def higher_or_lower(data):
    """Game that let you decide if the person is more famous or not."""
    should_continue = True
    person = random_person(data) 
    person2 = random_person(data) 
    if person == person2:
        person2 = random_person(data)
    score = 0

    while should_continue:
        # Generate random person B
        person2 = random_person(data) 

        # Interaction with player
        os.system("clear")
        print(f"{logo}\n  Compare A: {person['name']}, a {person['description']}, from {person['description']}\n  {vs}\n  Against B: {person2['name']}, a {person2['description']}, from {person2['country']}")
        print(f"Your score is {score}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower() # for higher user tolerance

        # Check if the user guessed right
        if guess == 'a' and person['follower_count'] > person2['follower_count']:
                score +=1
        elif guess == 'b' and person2['follower_count'] > person['follower_count']:
                score +=1
        else:
            game_over(score)
            should_continue = False

        # To save B person to A
        person = person2

higher_or_lower(data)


