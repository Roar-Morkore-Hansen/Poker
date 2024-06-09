import pygame
import random
import os



# Define the Card class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        CARDPATH = "PNG-cards-1.3"
        self.image = pygame.image.load(os.path.join(CARDPATH, f"{self.value}_of_{self.suit}.png"))

# Class for deck of cards
class Deck():
    def __init__(self):
        self.deck = self.create()
    def new_deck(self):
        self.deck = self.create()
    def shuffle(self):
        random.shuffle(self.deck)
    def create(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        deck = [Card(suit, value) for suit in suits for value in values]
        return deck
    def draw_card(self):
        return self.deck.pop(0)
