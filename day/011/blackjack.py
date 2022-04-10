############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(cards):
    return random.choice(cards) 
user_cards = [deal_card(cards), deal_card(cards)]
computer_cards = [deal_card(cards), deal_card(cards)]

def calculate_score(list):
    list_sum = sum(list)
    if list_sum == 21:
        return 0
    if list_sum > 21:
        for card in list:
            if card == 11:
                card = 1
                print("Ace")
    return list_sum


print(logo)

def blackjack(): 
    s_continue = True
    while s_continue == True:
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        if sum(user_cards) == 21:
            print("Win, blackjack")
            break 
        elif sum(computer_cards) == 21:
            print("Lose, blackjack")
            break
        elif sum(user_cards) > 21:
            for card in user_cards:
                if card == 11:
                    card = 1
                    print("Ace")
        elif sum(computer_cards) > 21:
            for card in computer_cards:
                if card == 11:
                    card = 1
                    print("Ace")
        if sum(user_cards) > 21:
            print("Lose, you went over")
            break

        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == 'y':
            user_cards.append(deal_card(cards))
        else:
            s_continue = False
    while sum(computer_cards) < 17:
        computer_cards.append(deal_card(cards))
    if sum(user_cards) > 21:
        for card in user_cards:
            if card == 11:
                card = 1
                print("Ace")
    elif sum(computer_cards) > 21:
        for card in computer_cards:
            if card == 11:
                card = 1
                print("Ace")
    if sum(user_cards) > 21:
        print("Lose, you went over")
    elif sum(user_cards) > 21:
        print("Lose, you went over")
    elif sum(computer_cards) < sum(user_cards):
        print("Win")
    elif sum(computer_cards) < sum(user_cards):
        print("Lose")
    elif sum(computer_cards) == sum(computer_cards):
        print("Draw")

    
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's cards: {computer_cards}, current score: {sum(computer_cards)}")

blackjack()
should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while should_continue == 'y':
    blackjack()
    should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")



"""
should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if should_continue == 'n':
    quit()
should_continue = True

while should_continue == True:
    if sum(computer_cards) == 21:
        print(f"Computer wins")
    elif sum(user_cards) == 21:
        print(f"You win")
    elif sum(user_cards) > 21:
        print(f"You went over. You lose")

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if another_card == 'y':
        user_cards.append(random.choice(cards))
    elif another_card == 'n':
        while sum(computer_cards) < 16: 
            computer_cards.append(random.choice(cards))
        if sum(user_cards) > 21:
            print("You lose")
            print(f"Your cards: {user_cards}, final score: {sum(user_cards)}")
            print(f"Computer's first card: {computer_cards}, final score: {sum(computer_cards)}")
        elif sum(computer_cards) == sum(user_cards):
            print("Draw")
            print(f"Your cards: {user_cards}, final score: {sum(user_cards)}")
            print(f"Computer's first card: {computer_cards}, final score: {sum(computer_cards)}")
        elif sum(user_cards) > 21:
            print("You lose")
            print(f"Your cards: {user_cards}, final score: {sum(user_cards)}")
            print(f"Computer's first card: {computer_cards}, final score: {sum(computer_cards)}")
        elif sum(user_cards) > sum(computer_cards):
            print("You win")
            print(f"Your cards: {user_cards}, final score: {sum(user_cards)}")
            print(f"Computer's first card: {computer_cards}, final score: {sum(computer_cards)}")
        else:
            print("You lose")
            print(f"Your cards: {user_cards}, final score: {sum(user_cards)}")
            print(f"Computer's first card: {computer_cards}, final score: {sum(computer_cards)}")


should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
"""
