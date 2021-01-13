import os
from art import logo as logo




print(logo)

bids = {}

new_bid = True

while new_bid == True:
    name = input('What is your name?  ')
    bid = int(input('What\'s your bid?  '))

    bids[name] = bid

    new_bidder = input('Are there any other bidders? Type "y" or "n"  ').lower()
    if new_bidder == 'n':
        new_bid = False
    else:
        os.system('clear')
        continue
os.system('clear')
bidder = ''
bid = 0
for k, v in bids.items():
    if v > bid:
        bidder = k
        bid = v
print(f'The winning bidder is {bidder} with a bid of {bid}')
