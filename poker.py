import random

suits = ["H", "D", "C", "S"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def deck():
    cardDeck = []
    for suit in suits:
        for value in values:
            cardDeck.append(value + suit)
    return cardDeck

def draw(deck):
    deckSize = len(deck) - 1
    randNum = random.randint(0, deckSize)
    return deck.pop(randNum)

def drawNum(num, deck):
    cards = []
    for i in range(num):
        cards.append(draw(deck))
    return cards

def dealHand(deck):
    return drawNum(2, deck)

def dealFlop(deck):
    return drawNum(3, deck)

def dealTurn(deck):
    return drawNum(1, deck)

def dealRiver(deck):
    return drawNum(1, deck)


def deal(deck):
    communityCards = []

    print(*dealHand(deck))
    input("FLOP: ")
    communityCards += dealFlop(deck)
    print(*communityCards)
    input("TURN: ")
    communityCards += dealTurn(deck)
    print(*communityCards)
    input("RIVER: ")
    communityCards += dealRiver(deck)
    print(*communityCards)

def main():
    print("press any button to see show next cards")
    
    cardDeck = deck()
    loop = True

    while loop:
        print("=" * 5 + "POKER" + "=" * 5)
        deal(cardDeck)

        print("=" * 15)
        x = input("press q to quit, any other to play again: ")
        if x == "q" or x == "Q":
            loop = False


main()


