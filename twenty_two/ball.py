from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.bounces = 1
        self.move_speed = 0.05

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.bounces += 1
        if self.bounces % 2 == 0:
            self.move_speed *= 0.9



    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.05






