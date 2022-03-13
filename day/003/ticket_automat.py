print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bil = 0

# Nested condition
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a ride on us!")
    else:
        bill = 12

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")
    
else:
    print("Sorry, you can't ride the rollercoaster for now!")
