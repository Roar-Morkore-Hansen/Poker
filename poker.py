import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define card path
CARDPATH = "PNG-cards-1.3"

# Set the title of the window
pygame.display.set_caption("Playing Card Game")

# Define the Card class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.image = pygame.image.load(os.path.join(CARDPATH, f"{self.value}_of_{self.suit}.png"))

# Function to create a deck of cards
def create_deck():
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    deck = [Card(suit, value) for suit in suits for value in values]
    return deck

# Function to shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)

# Function to draw a card
def draw_card(deck):
    return deck.pop(0)

# Function to display a card
def display_card(card, x, y):
    image = card.image
    scaledImage = pygame.transform.scale(image, (image.get_width() / 5, image.get_height() / 5))
    screen.blit(scaledImage, [x, y])

# Defining Player clas
class Player:
    def __init__(self):
        self.hand = None
    def display_hand(self):
        if not self.hand == None:
            display_card(self.hand[0], 300, 300) 
            display_card(self.hand[1], 420, 300) 
    def display(self):
        self.display_hand()

class Community_Cards:
    def __init__(self):
        self.flop = None
        self.turn = None
        self.river = None
    def display_flop(self):
        if not self.flop == None:
            display_card(self.flop[0], 100, 100) 
            display_card(self.flop[1], 220, 100) 
            display_card(self.flop[2], 340, 100) 
    def display_turn(self):
        if not self.turn == None:
            display_card(self.turn, 460, 100) 
    def display_river(self):
        if not self.river == None:
            display_card(self.river, 580, 100) 
    def display(self):
        self.display_flop()
        self.display_turn()
        self.display_river()


# Define Board Class
class Board:
    def __init__(self, deck):
        self.deck = deck
        self.player = Player()
        self.community_cards = Community_Cards()
        self.stage = Stage(self)
    def deal_hand(self):
        hand = []
        for i in range(2):
            hand.append(draw_card(self.deck))
        self.player.hand = hand
    def deal_flop(self):
        flop = []
        for i in range(3):
            flop.append(draw_card(self.deck))
        self.community_cards.flop = flop
    def deal_turn(self):
        self.community_cards.turn = draw_card(self.deck)
    def deal_river(self):
        self.community_cards.river = draw_card(self.deck)
    def display(self):
        self.player.display()
        self.community_cards.display()

class Stage:
    def __init__(self, board):
        self.board = board
        self.stageNum = 0
    def advance(self):
        self.stageNum += 1
        if self.stageNum == 1:
            print(self.stageNum, "DEAL HAND")
            self.board.deal_hand()
        elif self.stageNum == 2:
            print(self.stageNum, "DEAL FLOP")
            self.board.deal_flop()
        elif self.stageNum == 3:
            print(self.stageNum, "DEAL TURN")
            self.board.deal_turn()
        elif self.stageNum == 4:
            print(self.stageNum, "DEAL RIVER")
            self.board.deal_river()




# Main function
def main():
    # Create the deck of cards
    deck = create_deck()
    shuffle_deck(deck)
    board = Board(deck)

    # Main loop
    done = False
    clock = pygame.time.Clock()

    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if board.stage.stageNum >= 4:
                    deck = create_deck()
                    shuffle_deck(deck)
                    board = Board(deck)
                else:
                    board.stage.advance()



        # --- Game logic should go here

        # --- Drawing code should go here
        screen.fill(WHITE)
        board.display()

        # --- Update the screen
        pygame.display.flip()

        # --- Limit frames per second
        clock.tick(60)

    # Close the window and quit
    pygame.quit()

# Run the main function
if __name__ == "__main__":
    main()

