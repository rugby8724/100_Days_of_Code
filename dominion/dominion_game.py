from player_cards import PlayerCards

playerOneCards = PlayerCards()
playerTwoCards = PlayerCards()

playerOneCards.create_starting_pile()
playerTwoCards.create_starting_pile()

print(playerOneCards.playercardpile)
print(playerTwoCards.playercardpile)

playerOneCards.draw_hand()
playerTwoCards.draw_hand()

print(playerOneCards.playerhand)
print(playerTwoCards.playerhand)
