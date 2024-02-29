from Deck import Deck
from Player import Player
from Table import Table
from Game import Game

def main():
    game = Game()

    print("\nWelcome to Blackjack!")
    if game.gameOn():
        print("Player wins! Leave Las Vegas while you still can!")
    else:
        print("Dealer wins! Remember - gamblers win big 95 percent of the games after they quit!")

if __name__=="__main__":
    main()