import math
# math.ceil(4.2) - round up the number so the result of this will be 5
# round(4.2) - round down the number so the result of this will be 4

def paint_calc(height, width, cover):
    num_of_cans = int(math.ceil((height * width) / cover))
    print(f"You'll need {num_of_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)
