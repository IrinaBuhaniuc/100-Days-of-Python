import turtle
import pandas
from state_name import State


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    states = data.state.to_list()
    if answer_state == "Exit":
        break

    for name in states:
        if name == answer_state:
            coordonate = data[data.state == answer_state]
            x = coordonate["x"].to_list()
            y = coordonate["y"].to_list()
            state = State(x[0], y[0], name)
            guessed_states.append(answer_state)


for guess in guessed_states:
    if guess in states:
        states.remove(guess)
print(states)
dataframe = pandas.DataFrame(states)
dataframe.to_csv('states_to_lern.cvs')
