import random
import os

from game_data import data
from art import logo, vs


def new_insta(insta1=''):
    insta2 = random.choice(list(data))
    if insta2['name'] == insta1:
        new_insta(insta1)
    else:
        return insta2


def insta_compare(insta1, insta2, pick):
    pick_1 = insta1['follower_count']
    pick_2 = insta2['follower_count']
    if pick_1 > pick_2:
        return pick == '1'
    else:
        return pick == '2'


def play_game():

    insta_2 = new_insta()
    count = -1
    correct = True
    while correct == True:
        print(logo)
        count += 1
        if count >= 1:
            print(f'You\'re right Current score: {count}')
        insta_1 = insta_2
        insta_2 = new_insta(insta_1['name'])
        print(f'1: {insta_1["name"]}, {insta_1["description"]}, from: {insta_1["country"]}')
        print(vs)
        print(f'2: {insta_2["name"]}, {insta_2["description"]}, from: {insta_2["country"]}')


        player_choice = input('Who has more followers? Press 1 or 2 ')
        compare_insta = insta_compare(insta_1, insta_2, player_choice)
        correct = compare_insta
        os.system('clear')
    print(f'Sorry you\'re wrong, you got {count} correct')


play_game()
