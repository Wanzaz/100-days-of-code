import turtle
import pandas
from turtle import Turtle

FONT = ("Arial", 10, "normal")
ALIGNMENT = "center"

text = Turtle()
text.hideturtle()
text.penup()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
correct_guesses = []


game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?r")
    converted_guess = answer_state.title()
    state_guess = data[data.state == converted_guess]
    all_states = data.state.str.match(converted_guess)
    for state in all_states:
        if state:
            correct_guesses.append(converted_guess)
            text.goto(int(state_guess.x), int(state_guess.y))
            text.write(converted_guess, align=ALIGNMENT, font=FONT)

