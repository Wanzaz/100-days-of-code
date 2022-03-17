import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# or you can use the choice() function
# print(random.choice(names))
quantity = len(names)
paying = random.randint(1, quantity-1) # the -1 is there because we are starting at 0

print(f"{names[paying]} is going to buy the meal today!") 
