import turtle as t
import random

from hirst import final_colors

t.colormode(255)
tad = t.Turtle()
tad.penup()
tad.setpos(-200, -200)
for i in range(11):
    if i != 0:
        tad.penup()
        tad.setheading(90)
        tad.forward(50)
        if i % 2 == 0:
            tad.setheading(0)
        else:
            tad.setheading(180)
    for x in range(11):
        tad.pendown()
        tad.dot(20, random.choice(final_colors))
        tad.penup()
        if x < 10:
            tad.forward(50)

screen = t.Screen()
screen.exitonclick()

