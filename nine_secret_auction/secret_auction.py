import os
from art import logo


print(logo)

bids = {}

def highest_bidder(bids):
    bidder = ''
    bid = 0
    for k, v in bids.items():
        if v > bid:
            bidder = k
            bid = v
    print(f'The winning bidder is {bidder} with a bid of ${bid}')


new_bid = True
while new_bid == True:
    name = input('What is your name?  ')
    bid = int(input('What\'s your bid?  '))

    bids[name] = bid

    new_bidder = input('Are there any other bidders? Type "y" or "n"  ').lower()
    if new_bidder == 'n':
        new_bid = False
        os.system('clear')
        highest_bidder(bids)
    else:
        os.system('clear')
        continue
