from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
starting_line = [-230, -125]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')


for t in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[t])
    new_turtle.penup()
    new_turtle.goto(starting_line[0], starting_line[1])
    starting_line[1] += 50
    turtles.append(new_turtle)


def race():
    still_racing = 0
    while still_racing < 150:
        for turtle in turtles:
            turtle.forward(random.randint(1,20))
            still_racing = turtle.position()[0]
            if still_racing >= 150:
                print(turtle.pencolor())
                if user_bet == turtle.pencolor():
                    print(f'Your pick {user_bet} wins you lucky bastard!!!')
                else:
                    print(f'Even for a turtle {user_bet} is very slow')
                break


screen.listen()
screen.onkey(race, 'r')




screen.exitonclick()