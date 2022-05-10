import random
from turtle import Turtle, Screen

tim = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# 1. Challenge
def draw_a_square(turtle_name):
    for i in range(4):
        tim.forward(100)
        tim.left(90)

# 2. Challenge
def draw_a_dashed_line(turtle_name):
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

for shape_side_n in range(3, 10):
tim.color(random.choice(colours))
draw_shape(shape_side_n)


tim.shape("turtle")
tim.color("red")

# Calling all functions
# draw_a_square(tim)
# draw_a_dashed_line(tim)


screen = Screen()
screen.exitonclick()
