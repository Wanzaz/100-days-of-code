# one way to open file
file = open("my_file.txt")
contents = file.read()
#print(contents)
file.close()


# second way to open file
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)


# writing in file
with open("my_file.txt", mode="a") as file: # modes: w (write), a (append), r (read-only)
    file.write("\nNew words")


# creating and writing into new file
with open("new_file.txt", mode="w") as file: # if the file doesn't exist it will be created
    file.write("\nNew words")
