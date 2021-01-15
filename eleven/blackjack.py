import os
import random

from art import logo



# play = input('Do you want to play a game of Blackjack? Type "y" or "n" ')


def blackjack():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print(logo)

    player_cards = [random.choice(cards), random.choice(cards)]
    player_score = sum(player_cards)
    dealer_cards = [random.choice(cards), random.choice(cards)]
    dealer_score = sum(dealer_cards)

    if player_score == 21:
        return 'Congrats you have a blackjack and Win!!!'
    playing = True
    while playing == True:
        if 11 not in player_cards:
            print(f'Your cards: {player_cards}, current score: {player_score}')
        elif player_score <= 21:
            print(f'Your cards: {player_cards}, current score: {player_score} or {player_score - 10}')
        else:
            sub = player_cards.index(11)
            player_cards[sub] -= 10
            player_score = sum(player_cards)
            continue

        print(f'Dealer\'s first card: {dealer_cards[0]}')
        if player_score <= 21:
            if input('Type "y" to get another card, type "s" to stand  ') == 'y':
                player_cards.append(random.choice(cards))
                player_score = sum(player_cards)
                os.system('clear')
            else:
                playing = False
        else:
            return (f'Sorry you busted with {player_score}. The Dealer Wins :( ')

    while dealer_score < 17:
        dealer_cards.append(random.choice(cards))
        dealer_score = sum(dealer_cards)
        if 11 in dealer_cards and dealer_score > 21:
            sub = dealer_cards.index(11)
            dealer_cards[sub] -= 10
            dealer_score = sum(dealer_cards)


    player_final = f'Your final hand: {player_cards}, final_score: {player_score}'
    dealer_final = f'Dealer\'s final hand: {dealer_cards}, final_score: {dealer_score}'

    if dealer_score > 21:
        return (f'The Dealer {dealer_cards} busted with {dealer_score}. You Win!!!')
    elif player_score == dealer_score:
        return(f'Looks like there is a tie Dealer: {dealer_score} Player: {player_score}')
    elif player_score > dealer_score:
        return player_final + str('\n') + dealer_final + str('\n You Win!!!')
    else:
        return player_final + str('\n') + dealer_final + str('\n Dealer Wins')

new_game = True
while new_game == True:
    play = blackjack()
    print(play)
    if input('Press y to play another game or press e to exit ') == 'y':
        os.system('clear')
    else:
        new_game = False
        os.system('clear')
