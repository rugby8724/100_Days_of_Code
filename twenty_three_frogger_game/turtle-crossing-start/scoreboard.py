from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 0
        self.penup()
        self.setposition(-240, 260)
        self.hideturtle()
        self.level()

    def level(self):
        self.current_level += 1
        self.clear()
        self.write(f'Level: {self.current_level}', align=ALIGNMENT, font=FONT )

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f'GAMEOVER, Level: {self.current_level}', align=ALIGNMENT, font=FONT)

