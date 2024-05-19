import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (53,101,77)

# Define a font and size
font = pygame.font.Font(None, 36)

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define card path
CARDPATH = "PNG-cards-1.3"

# Set the title of the window
pygame.display.set_caption("Potodds Game")

def display_text(string, x, y):
    # Render the text
    text = font.render(string, True, (255, 255, 255))  # White text
    text_rect = text.get_rect(center=(320, 240))  # Center the text
    screen.blit(text_rect, [x, y])

class Pot:
    def __init__(self):
        self.pot = None
    def set_pot(self, pot):
        self.pot = pot
    def add(self, int):
        self.pot += int
    def display_pot(self):
        if not self.pot == None:
            display_text(str(self.pot), 300, 300) 
    def display(self):
        self.display_pot()

class Bet:
    def __init__(self):
        self.bet = None
    def set_bet(self, pot):
        self.bet = pot
    def display_bet(self):
        if not self.bet == None:
            display_text(str(self.bet), 200, 300) 
    def display(self):
        self.display_bet()


# Define Board Class
class Board:
    def __init__(self, bet, pot):
        self.bet = bet
        self.pot = pot
        self.pot_odds = Pot_Odds(bet, pot)
    def display(self):
        self.bet.display()
        self.pot.display()


class Stage:
    def __init__(self, board):
        self.board = board
        self.stageNum = 0
    def advance(self):
        self.stageNum += 1
        if self.stageNum == 1:
            print(self.stageNum, "SHOW POT AND BET")
        elif self.stageNum == 2:
            print(self.stageNum, "SHOW ODDS")


class Pot_Odds:
    def __init__(self, bet, pot):
        self.bet = bet
        self.pot = pot
        self.numerator = 0
        self.denominator = 0
    def get_betting_percent(self):
        betting_percent =  self.bet / (self.pot + self.bet) * 100
        print(betting_percent)
    def get_pot_odds_ratio(self):
        risk = 1
        value = self.pot/self.bet
        print(f'{value}:{risk}')
    def get_pot_odds_value(self):
        risk = self.bet
        value = self.pot
        print(f'{value}:{risk}')
        

# Main function
def main():
    # Create the deck of cards
    board = Board(Bet(), Pot())

    # Main loop
    done = False
    clock = pygame.time.Clock()

    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONUP:
                pot = random.randint(1, 10) * 100
                bet = random.randint(1, 10) * 10
                Board(bet, pot).pot_odds.get_pot_odds_ratio()
                Board(bet, pot).pot_odds.get_pot_odds_value()
                Board(bet, pot).pot_odds.get_betting_percent()
                print("============")



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

