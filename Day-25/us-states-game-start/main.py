import pandas

import turtle

from charset_normalizer.utils import any_specified_encoding

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()




guessed_state = []

while len(guessed_state) < 50:
    state_answer = screen.textinput(title=f"{len(guessed_state)}"
                                          f"/50 State Correct", prompt="What's another States's name").title()

    if state_answer == 'Exit':
        missed_states = []
        for state in all_states:
            if state not in guessed_state:
                missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        print(new_data)
        new_data.to_csv('states_to_learn.csv')
        break

    if state_answer in all_states:
        guessed_state.append(state_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[state_answer == data.state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_answer)




turtle.exitonclick()
