
# useful shortcut Ctrl + / = comment the code

fruit = ["item1", "item2"]

print(fruit[-1]) # it will print the first element at the end

fruit[0] = "apple" # rewriting the first element

fruit.append("cherry") # appends element at the end of the list

fruit.extend(["orange", "pear"])

fruit = ["cherry, grapes"]
vegetables = ["spinach", "tomatoes"]

dirty_dozen = [fruit, vegetables] # mested list
print(dirty_dozen)
