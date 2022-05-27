from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
# Higher Order Function
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
