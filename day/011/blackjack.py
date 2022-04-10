import os
import random
from art import logo


def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(card_list):
    """Take a list of cards and return the score calculated from the cards"""
    card_sum = sum(card_list)
    if card_sum == 21 and len(card_list) == 2:
        return 0

    if 11 in card_list and card_sum > 21:
        card_list.remove(11) 
        card_list.append(1)

    return card_sum

def compare(user_score, computer_score):
    """Compares the the user and computer score and makes decision who wins"""
    if user_score > 21 and computer_score > 21:
            return "You went over. You lose """
    if computer_score == user_score:
        return "Draw"
    elif computer_score == 21:
        return "Lose, opponent has blackjack"
    elif user_score == 21:
        return "Win, you have blackjack"
    elif user_score > 21:
        return "Lose, you went over"
    elif computer_score > 21:
        return "Win, opponent went over"
    elif computer_score < user_score:
        return "Win"

    return "Lose"

def play_game():
    os.system("clear")
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        # to use the += we would have to have a list not only one element 
        # append adds one item to the list
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"    Computer's firs card: {user_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    computer_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(compare(user_score, computer_score))
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()
