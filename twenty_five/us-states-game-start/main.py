import turtle
import pandas


screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

state_data = pandas.read_csv('50_states.csv')

correct_list = []
while len(correct_list) < 50:

    answer_state = screen.textinput(title=f'{len(correct_list)}/50 Guess the State ', prompt='Guess a state').title()
    if answer_state == 'Exit':
        break
    if answer_state in state_data.state.values and answer_state not in correct_list:
        correct_list.append(answer_state)
        tad = turtle.Turtle()
        tad.penup()
        state = state_data[state_data.state == answer_state]
        tad.goto(int(state.x), int(state.y))
        tad.hideturtle()
        tad.write(f'{answer_state}')





screen.exitonclick()


