from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 16, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_highscore()
        self.setposition(0, 280)
        self.color('white')
        self.hideturtle()
        self.update_score()

    def get_highscore(self):
        with open('data.txt') as saved_score:
            self.high_score = int(saved_score.read())

    def update_score(self):
        self.clear()
        self.write(f'Score = {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)
        self.score += 1

    def reset(self):
        if self.score - 1 > self.high_score:
            with open('data.txt', mode='w') as saved_score:
                new_high = self.score -1
                saved_score.write(str(new_high))
            self.get_highscore()
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.setposition(0,0)
    #     self.write('GAME OVER', align=ALIGNMENT, font=FONT)
