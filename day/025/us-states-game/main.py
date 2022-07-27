import turtle
import pandas

FONT = ("Arial", 10, "normal")
ALIGNMENT = "center"

t = turtle.Turtle()
t.hideturtle()
t.penup()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?r").title()
    if answer_state == "Exit":
        break
    state_data = data[data.state == answer_state]

    # all_states = list of states and value of boolean value (examples Ohio: True)
    all_states = data.state.str.match(answer_state)
    for state in all_states:
        if state:
            guessed_states.append(answer_state)
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state, align=ALIGNMENT, font=FONT)

