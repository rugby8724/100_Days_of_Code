import random


class PlayerCards:
    def __init__(self):
        self.playercardpile = []
        self.playerhand = []


    def pile_shuffle(self, cardpile):
        random.shuffle(cardpile)

    def create_starting_hand(self):
        for i in range(4):
            self.playercardpile.append('copper')
        for i in range(3):
            self.playercardpile.append('estate')
        self.pile_shuffle(self.playercardpile)


    def deal_cards(self,):
        for i in range(3):
            self.playerhand.append(self.playercardpile.pop(0))






