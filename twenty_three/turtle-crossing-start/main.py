import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turbo = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turbo.move_turtle, 'Up')

game_is_on = True
new_cars = 1
car_speed = 0.3
while game_is_on:
    time.sleep(car_speed)
    screen.update()
    if new_cars % 5 == 0:
        cars.add_car()
    cars.move_car()
    # Detect Turbo collision with car
    for car in cars.cars:
        if turbo.distance(car) < 25:
            score.game_over()
            time.sleep(4)
            game_is_on = False
    # Add New Level
    if turbo.ycor() > 300:
        score.level()
        turbo.goto(0, -280)
        car_speed *= 0.9

    new_cars += 1
