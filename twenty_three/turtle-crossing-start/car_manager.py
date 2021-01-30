from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_WIDTH = 1
CAR_LENGTH = 2


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.starting_cars()

    def new_car(self, x, y):
        turbo = Turtle('square')
        turbo.penup()
        turbo.color(random.choice(COLORS))
        turbo.shapesize(stretch_wid=CAR_WIDTH, stretch_len=CAR_LENGTH)
        turbo.goto(x, y)
        turbo.setheading(180)
        self.cars.append(turbo)

    def starting_cars(self):
        for x in range(-280, 300, 50):
            for y in range(-240, 270, 30):
                car = random.randint(1, 7)
                if car == 7:
                    self.new_car(x, y)

    def add_car(self):
        for i in range(-240, 200, 30):
            car = random.randint(1, 7)
            if car == 7:
                self.new_car(300, i)

    def move_car(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)



