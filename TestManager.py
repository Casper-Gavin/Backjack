import unittest

from Deck import Deck
from Player import Player
from Table import Table
from Game import Game
from Card import Card


class CardTests(unittest.TestCase):
    def testSetUpRank(self):
        self.card = Card('2', 'Hearts')
        self.assertEqual(self.card.rank, '2')

    def testSetUpSuit(self):
        self.card = Card('2', 'Hearts')
        self.assertEqual(self.card.suit, 'Hearts')


class PlayerTests(unittest.TestCase):
    def testSetUpPlayer(self):
        self.player = Player()
        self.assertEqual(self.player.aces, 0)

    # integration tests
        
    def testAddCardValue(self):
        self.player = Player()
        self.card = Card('2', 'Hearts')
        self.player.addCard(self.card)
        self.assertEqual(self.player.value, 2)

    def testAddCardAces(self):
        self.player = Player()
        self.card = Card('A', 'Hearts')
        self.player.addCard(self.card)
        self.assertEqual(self.player.aces, 1)

    def testAceAdjustAces(self):
        self.player = Player()
        self.card1 = Card('A', 'Hearts')
        self.card2 = Card('K', 'Spades')
        self.card3 = Card('5', 'Clubs')
        self.player.addCard(self.card1)
        self.player.addCard(self.card2)
        self.player.addCard(self.card3)
        self.player.aceAdjust()
        self.assertEqual(self.player.aces, 0)

    def testAceAdjustValue(self):
        self.player = Player()
        self.card1 = Card('A', 'Hearts')
        self.card2 = Card('K', 'Spades')
        self.card3 = Card('5', 'Clubs')
        self.player.addCard(self.card1)
        self.player.addCard(self.card2)
        self.player.addCard(self.card3)
        self.player.aceAdjust()
        self.assertEqual(self.player.value, 16)


class DeckTests(unittest.TestCase):
    # can't fully test the deck because where the cards' order is random
    def testSetUp(self):
        self.deck = Deck()
        self.assertEqual(len(self.deck.cards), 52)

    def testGiveCard(self):
        self.deck = Deck()
        self.assertIsInstance(self.deck.giveCard(), Card, "Output should be of type Card")

class GameTests(unittest.TestCase):
    def testCheckPlayerWinTrue(self):
        self.game = Game()
        self.assertEqual(self.game.checkPlayerWin(22), True)

    def testCheckPlayerWinFalse(self):
        self.game = Game()
        self.assertEqual(self.game.checkPlayerWin(21), False)

    def testCheckDealerWinLoseOutright(self):
        self.game = Game()
        self.assertEqual(self.game.checkDealerWin(22, 19), False)

    def testCheckDealerWinPlayerWins(self):
        self.game = Game()
        self.assertEqual(self.game.checkDealerWin(15, 21), True)

    def testCheckDealerWinDealerWins(self):
        self.game = Game()
        self.assertEqual(self.game.checkDealerWin(20, 19), False)

    def testCheckDealerWinTie(self):
        self.game = Game()
        self.assertEqual(self.game.checkDealerWin(20, 20), True)



if __name__ == '__main__': 
    unittest.main()