rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

rps=[rock, paper, scissors]
str_rps=['rock', 'paper', 'scissors']
ai = random.randint(0,2)
player = int(input('press 0 for rock, 1 for paper, 2 for scissors  '))

if player > 2:
  print('Invalid # please enter a 0, 1, or 2')
  player = int(input('press 0 for rock, 1 for paper, 2 for scissors  '))


print(f'You Choose! {str_rps[player]}\n')

print(rps[player])
print(f'\n The Computer throws {str_rps[ai]}\n')
print(rps[ai])

if ai == player:
  print('You\'re as smart as a bot...you both tied')
elif (player == 0 and ai == 2 ) or (player == 1 and ai == 0) or (player == 2 and ai == 1):
  print('You win, You\'re better than a computer')
else:
  print('Sorry you lose, The bots look well on their way to taking over the world')
