import random


class PlayerCards:
    def __init__(self):
        self.playercardpile = []
        self.playerhand = []


    def pile_shuffle(self, cardpile):
        random.shuffle(cardpile)

    def create_starting_pile(self):
        for i in range(4):
            self.playercardpile.append('copper')
        for i in range(3):
            self.playercardpile.append('estate')
        self.pile_shuffle(self.playercardpile)

    def draw_extra_card(self):
        self.playerhand.append(self.playercardpile.pop())


    def draw_hand(self, ):
        for i in range(3):
            self.draw_extra_card()






