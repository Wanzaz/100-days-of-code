# For Loop
numbers = [1, 2, 3]
new_list []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)


# List Comprehension
# new_list = [new_item for item in list]
# short_names = [new_item for item in list if test]


# Adding to numbers-list numbers + 1
numbers = [1, 2, 3]
new_numbers = [num + 1 for num in numbers]


# Going through list and seeing results what is happening
name = 'Angela'
new_list = [letter for letter in name]


# Create a new list from a range, where the list items are double the values in the range.
doubled_values = [num * 2 for num in range(1, 5)]


# Create a new list with names that have less than 5 letters
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]


# Create a new list with names that have more than 5 letters and turn them into upper letters
long_names = [name.upper() for name in names if len(name) > 5]



