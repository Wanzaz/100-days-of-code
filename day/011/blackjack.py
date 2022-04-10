import os
import random
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(card_list, cards):
    card_list.append(random.choice(cards)) 

user_cards = []
computer_cards = []
deal_card(user_cards, cards)
deal_card(user_cards, cards)
deal_card(computer_cards, cards) 
deal_card(computer_cards, cards)

def calculate_score(c_list):
    list_sum = sum(c_list)
    if list_sum == 21:
        return 0
    elif list_sum > 21:
        for card in c_list:
            if card == 11:
                c_list.remove(card) 
                c_list.append(1)
                print("Ace")
    return list_sum

def compare(user, computer):
    user_sum = sum(user)
    computer_sum = sum(computer)
    if computer_sum == user_sum:
        print("Draw")
    elif computer_sum == 21:
        print("Lose, computer has blackjack")
    elif user_sum == 21:
        print("Win, you have blackjack")
    elif user_sum > 21:
        print("Lose, you went over")
    elif computer_sum > 21:
        print("Win, computer went over")
    elif computer_sum > user_sum:
        print("Lose, computer has bigger cards")
    else:
        print("Win, you have bigger cards")

def blackjack():
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's firs card: {user_cards[0]}")

    if calculate_score(user_cards) > 21 or calculate_score(computer_cards) == 0:
        print("Lose, you went over or computer has blackjack")
        exit()
    if calculate_score(user_cards) == 0:
        print("Win, you have blackjack")
        exit()

    should_continue = True
    while should_continue == True:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == 'y':
            deal_card(user_cards, cards)
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
            print(f"Computer's firs card: {user_cards[0]}")
            if calculate_score(user_cards) == 0:
                print("Win, you have blackjack")
                exit()
            if calculate_score(user_cards) > 21:
                print("Lose, you went over")
                exit()
        else:
            should_continue = False 

    if sum(computer_cards) < 17:
        while calculate_score(computer_cards) < 17:
            deal_card(computer_cards, cards)
            calculate_score(computer_cards)

    compare(user_cards, computer_cards)


s_continue = True
while s_continue == True:
    another_game = input("Do you want to play a game of Blackjack? 'y' or 'n': ")
    if s_continue == True:
        os.system('clear')
        print(logo)
        blackjack()
    else:
        s_continue = False
