from turtle import Turtle

WIDTH = 5
HEIGHT = 1
X_POS = 350
Y_POS = 0
UP = 90
DOWN = 270
MOVE = 40


class Paddles:
    def __init__(self):
        super().__init__()
        self.paddles = []
        self.create_paddles()

    def create_paddles(self):
        for i in range(2):
            pad = Turtle(shape='square')
            pad.penup()
            pad.color('white')
            pad.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
            pad.shearfactor(0)
            print(i)
            if i != 1:
                pad.setposition(X_POS * - 1, Y_POS)
                self.paddles.append(pad)
            else:
                pad.setposition(X_POS, Y_POS)
                self.paddles.append(pad)

    def up_pad1(self):
        new_y = self.paddles[0].ycor() + 20
        self.paddles[0].goto(self.paddles[0].xcor(), new_y)

    def down_pad1(self):
        new_y = self.paddles[0].ycor() - 20
        self.paddles[0].goto(self.paddles[0].xcor(), new_y)

    def up_pad2(self):
        new_y = self.paddles[1].ycor() + 20
        self.paddles[1].goto(self.paddles[1].xcor(), new_y)

    def down_pad2(self):
        new_y = self.paddles[1].ycor() - 20
        self.paddles[1].goto(self.paddles[1].xcor(), new_y)





