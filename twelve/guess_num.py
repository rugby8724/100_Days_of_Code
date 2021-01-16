import os
import random

from art import logo

def guess_game():
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print('I\'m guessing of a number between 1 and 100' )
    if input('Difficulty: press h for hard or e for easy ') == 'h':
        chances = 5
    else:
        chances = 7
    num = random.randint(1, 101)

    while chances >= 1:
        print(f'You have {chances} attempts remaining to guess the number')
        guess = int(input('Make a guess: '))
        chances -= 1
        if guess == num:
            print(f'Congrats your guess of {guess} is correct!!!')
            break
        elif guess > num and chances >= 1:
            print('Too high guess again')
        elif guess < num and chances >= 1:
            print('Too low guess again')
        else:
            print(f'Sorry you lost, the number was {num}')
    if input('Would you like to play again press y for yes or n to exit ') == 'y':
        os.system('clear')
        guess_game()
    else:
        os.system('clear')
        exit()

guess_game()
