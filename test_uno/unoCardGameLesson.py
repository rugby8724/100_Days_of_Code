import random

def buildDeck():
    """
    Generate the UNO deck of 108 cards
    Parameters: None
    Return values: deck->list
    """
    deck = []
    colors = ['Red', 'Green', 'Yellow', 'Blue']
    values = [0,1,2,3,4,5,6,7,8,9, 'Draw Two', 'Skip', 'Reverse']
    wilds = ['Wild', 'Wild Draw Four']
    for color in colors:
        for value in values:
            cardVal = f'{color} {value}'
            deck.append(cardVal)
            if value != 0:
                deck.append(cardVal)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    return deck

def shuffleDeck(deck):
    '''
    Shuffles a list of items passsed into it
    Parameters: deck->list
    :return: deck-> list
    '''
    for cardPos in range(len(deck)):
        randPos = random.randint(0,107)
        deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
    return deck


unoDeck = buildDeck()
unoDeck = shuffleDeck(unoDeck)
print(unoDeck)