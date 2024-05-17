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

