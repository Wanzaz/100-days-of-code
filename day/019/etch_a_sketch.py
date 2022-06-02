# Etch-A-Sketch App
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.back(20)


def turn_left():
    new_heading = tim.heading() + 10  # or the tim.left(10) could be used
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.reset()
    # or tim.clear() ; tim.penup() ; tim.home() ; tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
