
# Normal Function
def add_(n1, n2):
    return n1 + n2

# Function with *args
def add(*args):
    print(args[0])

    for n in args:
        print(n)

# unlimited arguments = unlimited positional arguments
add(1, 2, 3, 4, 5) 


def add_t(*args): # type(*args) = tuple
    total = 0
    for n in args:
        total += n
    return total

print(f"Total of numbers: {add_t(1, 2, 3, 4, 5)}")

