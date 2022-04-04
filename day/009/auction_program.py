import os

bidder_dictonary = {}
should_continue = True

while should_continue:
	# If you are running Windows use: os.system('cls') instead of os.system('clear')
	os.system('clear')
	user_name = input("What is your name?: ")
	user_bid = int(input("What's you bid? $"))
	other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
	bidder_dictonary[user_name] = user_bid
	if other_bidders == 'no':
		should_continue = False

def find_highest_bid(bid_record):
	biggest_bid = bidder_dictonary[user_name]
	winner_name = user_name
	for key, value in bidder_dictonary.items():
		if biggest_bid < value:
			biggest_bid = value
			winner_name = key

	print(f"\nThe winner is {winner_name} a bid of ${biggest_bid}.")

find_highest_bid(bidder_dictonary)
