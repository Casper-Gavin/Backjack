from Card import Card
import random

class Deck:
    cards = []

    def __init__(self):
        # creates in order and then randomly shuffles the cards in the deck
        self.cards = [Card(rank, suit) for rank in Card.ranks for suit in Card.suits]
        random.shuffle(self.cards)

    def giveCard(self):
        return self.cards.pop()