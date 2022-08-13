# Handling Exceptions
    # try: - something that might cause an exception
    # except: - do this if there was an exception
    # else: - do this if there were no exceptions
    # finally: do this no matter what happens
    # raise - raise our own exceptions


# FileNotFound
# with open("a_file.txt") as data:
    # file.read()

try:
    file = open("a_file.txt")
    a_dictonary = {"key": "value"}
    print(a_dictonary["key"])

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print("That key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    # raise KeyError("This is an error that I made up.")
    file.close()
    print("File was closed.")

# KeyError
# a_dictonary = {"key": "value"}
# value = a_dictonary["non_existing_key"]

# IndexError
# fruit_list = {"Apple", "Banana", "Pear"}
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters")


bmi = weight / height ** 2
print(bmi)
