import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
print(game_images[users_choice])

computer_choice = random.randint(0, 2)
print(game_images[computer_choice])

rock = 0
paper = 1
scissors = 2

if users_choice == computer_choice:
    print("It is draw")
elif users_choice==rock and computer_choice==paper:
    print("Computer won")
elif users_choice==paper and computer_choice==scissors:
    print("Computer won")
elif users_choice==scissors and computer_choice==rock:
    print("Computer won")
elif users_choice==paper and computer_choice==rock:
    print("You won")
elif users_choice==scissors and computer_choice==paper:
    print("You won")
elif users_choice==rock and computer_choice==scissors:
    print("You won")
else:
    print("Follow instructions!")
