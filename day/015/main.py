from coffee_properties import MENU, resources

# REQUIREMENTS
# 1. Print report
# 2. Check resources sufficient?
# 3. Process coins.
# 4. Check transaction successful?
# 5. Make Coffee.


def report(resources, money):
    """Print out the current state of the coffee automat."""
    for key, values in resources.items():
        if key == 'coffee':
            print(f"{key.capitalize()}: {values}g")
        else:
            print(f"{key.capitalize()}: {values}ml")
    print(f"Money: ${money}")


def check_resources(type_of_coffee):
    """Check if there are enough resources to make a coffee"""
    if type_of_coffee != 'espresso':
        if MENU[type_of_coffee]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")
            return False
        elif MENU[type_of_coffee]["ingredients"]["milk"]  > resources["milk"]:
            print("Sorry there is not enough milk")
            return False
        elif MENU[type_of_coffee]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee")
            return False
        else:
            return True
    else:
        if MENU[type_of_coffee]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")
            return False
        elif MENU[type_of_coffee]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee")
            return False
        else:
            return True



def processing_coins():
    """Counts inserted money by customer."""
    print("Please insert coins.")
    quaters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    final_money = 0.25*quaters + 0.10*dimes + 0.05*nickles + 0.01*pennies 

    return final_money


def checking_inserted_coins(selected_drink, money):
    """Check if the user inserted enough money for selected drink."""
    if MENU[selected_drink]["cost"] > money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif MENU[selected_drink]["cost"] < money:
        print(f"Here is ${round(money - MENU[selected_drink]['cost'], 2)} dollars in change.")
        return True
    else:
        print("You inserted the exact amount of money that was needed.")
        return True


def deduct_resources(selected_drink):
    """Deduce the resources from the automat."""
    if selected_drink != 'espresso':
        resources["water"] = resources["water"] -  MENU[selected_drink]["ingredients"]["water"]
        resources["milk"] = resources["milk"] -  MENU[selected_drink]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[selected_drink]["ingredients"]["coffee"]
    else:
        resources["water"] = resources["water"] -  MENU[selected_drink]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[selected_drink]["ingredients"]["coffee"]




def coffee_automat():
    """Makes you wish come true."""
    should_continue = True
    money = 0
    while should_continue:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == 'off':
            # exit() 
            should_continue = False

        elif choice == 'report':
            # print report
            report(resources, money)

        elif choice == 'espresso':
            # check for report function and coin function
            if check_resources(choice): pass
            else: continue
            if checking_inserted_coins(choice, processing_coins()): pass
            else: continue
            money += 1.5

            # minus the resources
            deduct_resources(choice)

            # make espresso
            # wish customer good day
            print("Here is you latte. Enjoy!")

        elif choice == 'latte':
            if check_resources(choice): pass
            else: continue
            if checking_inserted_coins(choice, processing_coins()): pass
            else: continue
            money += 2.5

            # minus the resources
            deduct_resources(choice)
            print("Here is you latte. Enjoy!")

        elif choice == 'cappuccino':
            if check_resources(choice): pass
            else: continue
            if checking_inserted_coins(choice, processing_coins()): pass
            else: continue
            money += 3

            # minus the resources
            deduct_resources(choice)
            print("Here is you latte. Enjoy!")
        else:
            print("Please follow the instruction and try again!")

coffee_automat()
