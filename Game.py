from Deck import Deck
from Player import Player
from Table import Table

class Game:
    deck = Deck()
    playerHand = Player()
    dealerHand = Player()

    def __init__(self) -> None:
        pass

    def checkPlayerWin(self, value):
        if value > 21:
            return True
        return False
        
    def checkDealerWin(self, dealerValue, playerValue):
        if dealerValue > 21:
            Table.dealerLoses()
            return False
        elif playerValue > dealerValue:
            Table.playerWins()
            return True
        elif playerValue < dealerValue:
            Table.dealerWins()
            return False
        else:
            # tie goes to player
            Table.tie()
            return True

    # like a main function - hard to test
    def gameOn(self):
        # Deal initial cards
        self.playerHand.addCard(self.deck.giveCard())
        self.dealerHand.addCard(self.deck.giveCard())
        self.playerHand.addCard(self.deck.giveCard())
        self.dealerHand.addCard(self.deck.giveCard())

        # Show cards
        Table.showHidden(self.playerHand, self.dealerHand)

        while True:
            # player's turn
            while True:
                playerInput = input("\nWould you like to Hit (continue) or Stand (stop)? Enter 'hit' or 'stand': ")

                if playerInput.lower() == 'hit':
                    self.playerHand.addCard(self.deck.giveCard())
                    Table.showHidden(self.playerHand, self.dealerHand)

                    if self.checkPlayerWin(self.playerHand.value):
                        self.playerHand.aceAdjust()
                        if self.checkPlayerWin(self.playerHand.value):
                            Table.playerLoses()
                            return False

                # elif is for multiple conditions in a if else chain
                elif playerInput.lower() == 'stand':
                    break
                else:
                    print("Invalid input - enter 'hit' or 'stand'")

            # dealer's turn - dealer rule uses 17 instead of 21
            while self.dealerHand.value < 17:
                self.dealerHand.addCard(self.deck.giveCard())

            # Show all cards
            Table.showAll(self.playerHand, self.dealerHand)

            # Check winning conditions - tie goes to player
            if self.checkDealerWin(self.dealerHand.value, self.playerHand.value):
                return True
            else:
                return False