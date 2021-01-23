import turtle as t
import random as ran

tim = t.Turtle()
tim.shape('turtle')
# tim.color('green')

# colors = ["red","green","blue","orange","purple","pink","yellow", 'cyan', 'aquamarine']
# sides = 3
# while sides < 9:
#     tim.color(colors[0])
#     colors.pop(0)
#     for i in range(sides):
#         tim.forward(100)
#         tim.right(360/sides)
#     sides += 1


t.colormode(255)






def random_color():
    r = ran.randint(0, 255)
    g = ran.randint(0, 255)
    b = ran.randint(0, 255)
    color = (r, g, b)
    return color

def random_walk():
    tad = t.Turtle()
    tad.speed(10)
    tad.shape('turtle')
    tad.pensize(10)

    for i in range(70):
        tad.color(random_color())
        turn = ran.randint(0,3)
        tad.setheading(90 * turn)
        tad.forward(35)


def spirograph_turtle():
    tad = t.Turtle()
    tad.speed(0)
    tad.shape('turtle')
    for i in range(36):
        tad.color(random_color())
        tad.circle(100)
        tad.setheading(tad.heading() + 10)


spirograph_turtle()




screen = t.Screen()
screen.exitonclick()