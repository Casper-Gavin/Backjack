from Card import Card

class Player:
    cards = []
    value = 0
    aces = 0 

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def addCard(self, card):
        self.cards.append(card)
        self.value += Card.values[card.rank]
        if card.rank == 'A':
            self.aces += 1

    def aceAdjust(self):
        # if above 21 and has an ace
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1