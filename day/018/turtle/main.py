from turtle import Turtle, Screen

tim= Turtle()

def draw_a_square(turtle_name):
    for i in range(4):
        tim.forward(100)
        tim.left(90)

tim.shape("turtle")
tim.color("red")

draw_a_square(tim)



screen = Screen()
screen.exitonclick()
