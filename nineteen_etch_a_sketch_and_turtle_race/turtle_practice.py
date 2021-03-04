from turtle import Turtle, Screen

tad = Turtle()
screen = Screen()

def move_forwards():
    tad.forward(10)


screen.listen()
screen.onkey(key='space', fun=move_forwards)
screen.exitonclick()
