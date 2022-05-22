import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
turtle.colormode(255)
directions = [0, 90, 180, 270]
tim.speed(0) # fastest
tim.shape("turtle")
tim.color("red")


# 1. Challenge
def draw_a_square():
    for i in range(4):
        tim.forward(100)
        tim.left(90)


# 2. Challenge
def draw_a_dashed_line():
    for _ in range(15):
        tim.penup()
        tim.forward(10)
        tim.pendown()
        tim.forward(10)


# 3. Challenge
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


"""for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n) """


# 4. Challenge
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def random_walk():
    for _ in range(200):
        tim.width(10)
        tim.setheading(random.choice(directions))
        tim.color(random_color())
        tim.forward(30)


# 5. Challenge
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100, 360)
        tim.setheading(tim.heading() + size_of_gap)


# Calling all functions
# draw_a_square()
# draw_a_dashed_line()
# random_walk()
draw_spirograph(5)

screen = Screen()
screen.exitonclick()
