################### Scope ####################

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength) it will raise NameError because it is in local score and we want to use it in global scope


# Global  Scope
# It is available anywhere in our file
player_health = 10

def player():
    print(player_health)

player()


# There is no Block Scope

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

# If you create a variable within function you can use it only within the function
# If you create a variable in for, while loop you can use it also outside the loop


# Modifying Global Scope

enemies = 1

def increase_enemies():
    global enemies # allows you to modify a global variable in function
    enemies = 2
    print(f"enemies inside function: {enemies}")
    return enemies + 1 # a way to be able to use the global variable without changing it

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


# Global Constants
# Are usually written with uppercase

PI = 3.14159
URL = "https://www.google.com"


