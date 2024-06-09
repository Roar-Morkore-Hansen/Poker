import pygame
import random
import os

from cards import *
from potOdds import *

# Initialize Pygame
pygame.init()
pygame.font.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (53,101,77)

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the width and height of the cards
CARD_WIDTH = 100
CARD_HEIGHT = 145
CARD_GAP = 20

# Define card path
CARDPATH = "PNG-cards-1.3"

# Set the title of the window
pygame.display.set_caption("Playing Card Game")



# Function to display text
def display_text(string, x, y):
    # Define a font and size
    font = pygame.font.SysFont(None, 30)
    # Render the text
    text_surface = font.render(string, False, WHITE)
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
    screen.blit(text_surface, [x - text_width/2, y - text_height/2])

# Function to display a card
def display_card(card, x, y):
    image = card.image
    scaledImage = pygame.transform.scale(image, (CARD_WIDTH, CARD_HEIGHT))
    screen.blit(scaledImage, [x, y])

# Defining Player clas
class Player:
    def __init__(self):
        self.hand = None

class Pot:
    def __init__(self):
        self.value = None
    def set(self, pot):
        self.value = pot
    def add(self, int):
        self.value += int

class Bet:
    def __init__(self):
        self.value = None
    def set(self, pot):
        self.value = pot

class Community_Cards:
    def __init__(self):
        self.flop = None
        self.turn = None
        self.river = None


# Board Display
class Board_Display:
    def __init__(self, player, community_cards, bet, pot):
        self.player = player
        self.community_cards = community_cards
        self.pot = pot
        self.bet = bet
        # Screen
        self.width, self.hight = pygame.display.get_surface().get_size()
        # Community Card positions
        self.community_card_y = self.hight / 10 * 2
        self.community_card_x = (self.width / 2) - CARD_WIDTH / 2 - (2 * (CARD_WIDTH + CARD_GAP))
        # Player Card positions
        self.player_card_y = (self.hight / 10) * 5
        self.player_card_x = (self.width / 2) - (CARD_WIDTH / 2) - ((CARD_GAP + CARD_WIDTH) / 2)
        # Pot position
        self.pot_x = self.width / 2
        self.pot_y = self.hight/10 * 1
        # Bet position
        self.bet_x = self.width / 2
        self.bet_y = self.hight / 10 * 9
        # Potodds position
        self.potOdds_x =  self.width / 10 * 8
        self.potOdds_y =  self.hight / 10 * 8
    def display_flop(self):
        if not self.community_cards.flop == None:
            display_card(self.community_cards.flop[0], 
                         self.community_card_x, 
                         self.community_card_y) 
            display_card(self.community_cards.flop[1], 
                         self.community_card_x + (CARD_WIDTH + CARD_GAP), 
                         self.community_card_y) 
            display_card(self.community_cards.flop[2], 
                         self.community_card_x + 2 * (CARD_WIDTH + CARD_GAP),
                         self.community_card_y) 
    def display_turn(self):
        if not self.community_cards.turn == None:
            display_card(self.community_cards.turn, 
                         self.community_card_x + 3 * (CARD_WIDTH + CARD_GAP),
                         self.community_card_y) 
    def display_river(self):
        if not self.community_cards.river == None:
            display_card(self.community_cards.river, 
                         self.community_card_x + 4 * (CARD_WIDTH + CARD_GAP),
                         self.community_card_y) 
    def display_hand(self):
        if not self.player.hand == None:
            display_card(self.player.hand[0],
                         self.player_card_x,
                         self.player_card_y) 
            display_card(self.player.hand[1],
                         self.player_card_x + (CARD_WIDTH + CARD_GAP),
                         self.player_card_y) 
    def display_pot(self):
        if not self.pot.value == None:
            string = "Pot: " + str(self.pot.value)
            display_text(string, self.pot_x, self.pot_y)
    def display_bet(self):
        if not self.bet.value == None:
            string = "bet: " + str(self.bet.value)
            display_text(string, self.bet_x, self.bet_y)
    def display_potOdds(self):
        if not self.bet.value == None:
            string = "potodds: " + "1:" + str(odds_ration(self.bet.value, self.pot.value)) + "    -     %: " + str(betting_percent(self.bet.value, self.pot.value))
            display_text(string, self.potOdds_x, self.potOdds_y)
    def display(self):
        self.display_pot()
        self.display_bet()
        self.display_potOdds()
        self.display_flop()
        self.display_turn()
        self.display_river()
        self.display_hand()




# Define Board Class
class Board:
    def __init__(self, deck, bet, pot):
        self.deck = deck
        self.player = Player()
        self.community_cards = Community_Cards()
        self.stage = Stage(self)
        self.bet = bet
        self.pot = pot
        self.board_display = Board_Display(self.player, self.community_cards, self.bet, self.pot)
    def deal_hand(self):
        hand = []
        for i in range(2):
            hand.append(self.deck.draw_card())
        self.player.hand = hand
    def deal_flop(self):
        flop = []
        for i in range(3):
            flop.append(self.deck.draw_card())
        self.community_cards.flop = flop
    def deal_turn(self):
        self.community_cards.turn = self.deck.draw_card()
    def deal_river(self):
        self.community_cards.river = self.deck.draw_card()
    def display(self):
        self.board_display.display()


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
    deck = Deck()
    deck.shuffle()
    board = Board(deck, Bet(), Pot())

    # Main loop
    done = False
    clock = pygame.time.Clock()

    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONUP:
                board.pot.set(random.randint(1, 10) * 100)
                board.bet.set(random.randint(1, 10) * 10)
                if board.stage.stageNum >= 4:
                    deck.new_deck()
                    deck.shuffle()
                    board = Board(deck, Bet(), Pot())
                else:
                    board.stage.advance()



        # --- Game logic should go here

        # --- Drawing code should go here
        screen.fill(GREEN)
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

