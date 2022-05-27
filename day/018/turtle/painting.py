import random
import turtle
from turtle import Turtle, Screen
import colorgram as cg

image = "image_painting.jpg"
tim = Turtle()
turtle.colormode(255)
tim.speed(0) # fastest
"""""
colors = [(250, 251, 247), (199, 168, 94), (227, 239, 232), (129, 179, 191), 
(163, 58, 78), (234, 221, 121), (49, 113, 167), (241, 217, 222), (104, 87, 83), 
(143, 187, 119), (239, 245, 249), (216, 151, 171), (67, 125, 76), (94, 124, 180), 
(85, 165, 94), (190, 71, 90), (161, 34, 49), (142, 119, 116), (221, 173, 182), (175, 205, 174), 
(163, 202, 211), (204, 116, 48), (75, 60, 56), (67, 56, 52), (176, 190, 213)]
"""

def extracting_colors(image_name):
    """Extract the colors from the image and return them in list (rgb format)"""
    color_list = cg.extract(image_name, 25)
    color_palette = []

    for color in color_list:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        color_palette.append(new_color)

    return color_palette

def hirst_painting(color_list):
    """Paint 10X10 dots square with random colors"""
    number_of_dots = 100
    tim.penup()
    tim.hideturtle()

    # set starting position
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)

    # algorithm to paint 10X10 square
    for dot_count in range(1, number_of_dots + 1):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


colors = extracting_colors(image)

hirst_painting(colors)

screen = Screen()
screen.exitonclick()
