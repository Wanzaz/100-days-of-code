import os


bidder_dictonary = {}

user_name = input("What is your name?: ")
user_bid = int(input("What's you bid? $"))
other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
os.system('clear')

bidder_dictonary[user_name] = user_bid

while other_bidders == 'yes':
	# If you are running Windows use: os.system('cls') instead of os.system('clear')
	os.system('clear')
	user_name = input("What is your name?: ")
	user_bid = int(input("What's you bid? $"))
	other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
	bidder_dictonary[user_name] = user_bid

biggest_bid = bidder_dictonary[user_name]
winner_name = user_name
for key, value in bidder_dictonary.items():
	if biggest_bid < value:
		biggest_bid = value
		winner_name = key

print(f"\nThe winner is {winner_name} a bid of ${biggest_bid}.")

