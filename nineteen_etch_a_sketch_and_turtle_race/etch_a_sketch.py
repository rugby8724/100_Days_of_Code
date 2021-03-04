from turtle import Turtle, Screen

tad = Turtle()
screen = Screen()


def move_forwards():
    tad.forward(10)


def move_backwards():
    tad.backward(10)

def move_left():
    tad.setheading(tad.heading() + 10)


def move_right():
    tad.setheading(tad.heading() - 10)

def clean_screen():
    tad.clear()
    tad.reset()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='x', fun=clean_screen)
screen.exitonclick()