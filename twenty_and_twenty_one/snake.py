from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP =90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        seg = Turtle(shape='square')
        seg.penup()
        seg.color('white')
        seg.setposition(position)
        self.snake_body.append(seg)


    def extend(self):
        #add a new segment to the snake.
        self.add_segment(self.snake_body[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_position = self.snake_body[seg_num - 1].position()
            self.snake_body[seg_num].goto(new_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)






