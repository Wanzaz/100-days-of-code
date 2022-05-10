from turtle import Turtle, Screen

tim= Turtle()

def geometrical_shapes(turle_name):
    # triangle | 360:120 = 3
    for _ in range(3):
        tim.right(120)
        tim.forward(100)

    # square | 360:90 = 4
    for _ in range(4):
        tim.right(90)
        tim.forward(100)

    # pentagon | 360:72 = 5
    for _ in range(5):
        tim.right(72)
        tim.forward(100)

    # hexagon | 360:60 = 6
    for _ in range(6):
        tim.right(60)
        tim.forward(100)

    # heptagon | 360: = 7
    for _ in range(7):
        tim.right(51.4286)
        tim.forward(100)

    # octagon | 360:45 = 8
    for _ in range(8):
        tim.right(45)
        tim.forward(100)

    # nonagon | 360:40 = 9
    for _ in range(9):
        tim.right(40)
        tim.forward(100)

    # octagon | 360:36 = 10
    for _ in range(10):
        tim.right(36)
        tim.forward(100)


geometrical_shapes(tim)
