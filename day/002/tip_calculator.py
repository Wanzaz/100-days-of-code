#my solution

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
amount_of_people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
payment = float((tip * total_bill/100 + total_bill)/amount_of_people)
payment = round(payment, 2)
payment = "{:.2f}".format(payment)
print(f"Each person should pay: ${payment}")
