from turtle import Screen
import time

from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard

#Setup pong screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('Pong')

pong = Paddles()
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(pong.up_pad1, 'a')
screen.onkey(pong.down_pad1, 'z')
screen.onkey(pong.up_pad2, 'Up')
screen.onkey(pong.down_pad2, 'Down')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(pong.paddles[1]) < 50 and ball.xcor() > 320 or ball.distance(pong.paddles[0]) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when paddle misses
    if ball.xcor() > 420:
        score.l_point()
        ball.reset_position()

    if ball.xcor() < -420:
        score.r_point()
        ball.reset_position()

    game_is_on = score.game_over()






screen.exitonclick()
