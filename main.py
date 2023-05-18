from turtle import Turtle, Screen
import pandas

data = pandas.read_csv('50_states.csv')
states = data.state.to_list()
states_guessed = []
missing_states = []

pen = Turtle()
answer = Turtle()
answer.hideturtle()
screen = Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
pen.shape(image)


while len(states_guessed) < 50:
    answer_state = screen.textinput(title=f"{len(states_guessed)}/50 States Guessed",
                                    prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        missing_states = [state for state in states if state not in states_guessed]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in states:
        state_data = data[data.state == answer_state]
        x_pos = int(state_data.x)
        y_pos = int(state_data.y)
        answer.penup()
        answer.goto(x_pos, y_pos)
        answer.write(arg=f"{state_data.state.item()}", align='center', font=('Courier', 8, "normal"))
        if answer_state not in states_guessed:
            states_guessed.append(answer_state)
