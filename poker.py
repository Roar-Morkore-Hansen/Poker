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
    screen.blit(card.image, [x, y])

# Main function
def main():
    # Create the deck of cards
    deck = create_deck()
    shuffle_deck(deck)

    # Main loop
    done = False
    clock = pygame.time.Clock()

    card = draw_card(deck)

    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONUP:
                # Draw a card 
                if len(deck) > 0:
                    card = draw_card(deck)


        # --- Game logic should go here

        # --- Drawing code should go here
        screen.fill(WHITE)
        display_card(card, 100, 100) 

        # --- Update the screen
        pygame.display.flip()

        # --- Limit frames per second
        clock.tick(60)

    # Close the window and quit
    pygame.quit()

# Run the main function
if __name__ == "__main__":
    main()

