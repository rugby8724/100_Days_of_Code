from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 16, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setposition(0, 280)
        self.color('white')
        self.hideturtle()
        self.add_point()

    def add_point(self):
        self.clear()
        self.write(f'Score = {self.score}', align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.setposition(0,0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
