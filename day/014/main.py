import os
import random
from art import logo, vs
from game_data import data

def random_person(data):
    person = random.choice(data)
    return person

def game_over(score):
    os.system("clear")
    print(f"{logo} \n Sorry, that's wrong. Final score: {score}'")

def higher_or_lower():
    should_continue = True
    person = random_person(data) 
    person2 = random_person(data) 
    score = 0


    while should_continue:
        person2 = random_person(data) 
        os.system("clear")
        print(f"{logo}\n  Compare A: {person['name']}, a {person['description']}, from {person['description']}\n  {vs}\n  Against B: {person2['name']}, a {person2['description']}, from {person2['country']}")
        print(f"You score is {score}")
        tip = input("Who has more followers? Type 'A' or 'B': ")

        if tip == 'A':
            if person['follower_count'] > person2['follower_count']:
                score +=1
            else:
                game_over(score)
                should_continue = False
        elif tip == 'B':
            if person2['follower_count'] > person['follower_count']:
                score +=1
            else:
                game_over(score)
                should_continue = False

        person = person2

higher_or_lower()


