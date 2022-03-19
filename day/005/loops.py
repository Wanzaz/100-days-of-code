fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")


for number in range(1, 11, 3): # the 3 describes how big the should be the step
    print(number)

    
# calculates the sum of all the even numbers form 1 to 1000
sum = 0
for num in range(2, 101, 2):
    sum += num

print(sum)


# fizz buz game
num = 1
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
