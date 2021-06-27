from player_cards import PlayerCards

playerOneCards = PlayerCards()
playerTwoCards = PlayerCards()

playerOneCards.create_starting_hand()
playerTwoCards.create_starting_hand()

print(playerOneCards.playercardpile)
print(playerTwoCards.playercardpile)

playerOneCards.deal_cards()
playerTwoCards.deal_cards()

print(playerOneCards.playerhand)
print(playerTwoCards.playerhand)
