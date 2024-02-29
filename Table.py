# this class is all output so will not be fully tested
class Table:
    def showHidden(player, dealer):
        print("\nDealer's Hand: ")
        print(" <card hidden> ")
        print('', dealer.cards[1])
        print("\nPlayer's Hand: ", *player.cards)

    def showAll(player, dealer):
        print("\nDealer's Hand: ", *dealer.cards)
        print("Dealer's Hand = ", dealer.value)
        print("\nPlayer's Hand: ", *player.cards)
        print("Player's Hand = ", player.value)

    def playerLoses():
        print("Player loses")

    def playerWins():
        print("Player wins")

    def dealerLoses():
        print("Dealer loses! Player wins!")

    def dealerWins():
        print("Dealer wins!")

    def tie():
        print("It's a push. Tie game")