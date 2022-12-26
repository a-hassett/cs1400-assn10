# Alexandra Hassett, CS 1400

import random
import time


class Card:
    def __init__(self, num=1, suit="S"):
        # If the entered values are not within the range, the default is ace of spades
        if not(num > 0 or num < 14):
            num = 1
        if not(suit == "C" or suit == "D" or suit == "H" or suit == "S"):
            suit = "S"
        self.num = num
        self.suit = suit

    # If the self card is less than the other card, return true. Suits are more important and are in ABC order
    def __lt__(self, other):
        if self.suit != other.suit:
            if ord(self.suit) < ord(other.suit):
                return True
            else:
                return False
        else:
            if self.num < other.num:
                return True
            else:
                return False

    def print(self):
        # Set the printed string using the values of the card's suit and number
        if self.suit == "C":
            printedSuit = "\u2663"
        elif self.suit == "D":
            printedSuit = "\u2662"
        elif self.suit == "H":
            printedSuit = "\u2661"
        else:
            printedSuit = "\u2660"
        if self.num == 1:
            printedNum = "A"
        elif self.num == 11:
            printedNum = "J"
        elif self.num == 12:
            printedNum = "Q"
        elif self.num == 13:
            printedNum = "K"
        else:
            printedNum = str(self.num)
        print(format(printedNum + printedSuit, ">3s"), end="\t")

    def blackJackValue(self):
        # Aces are worth 11; Jack, Queen, King are worth 10; everything else is worth its face value
        if self.num == 1:
            return 11
        elif self.num == 11 or self.num == 12 or self.num == 13:
            return 10
        else:
            return self.num


class Deck:
    def __init__(self):
        self.__deck = []
        self.__fullArrangedDeck = []  # Have a list that has all cards in order
        # We'll need these non-private variables for the deal function
        self.num = 1
        self.suit = "S"
        # Set two lists with all the cards in order
        for i in range(4):
            suits = "CDHS"
            if suits[i] == "C":
                self.__suit = "\u2663"
            if suits[i] == "D":
                self.__suit = "\u2662"
            if suits[i] == "H":
                self.__suit = "\u2661"
            if suits[i] == "S":
                self.__suit = "\u2660"
            for j in range(13):
                if j == 0:
                    self.__deck.append("A" + self.__suit)
                    self.__fullArrangedDeck.append("A" + self.__suit)
                elif j == 10:
                    self.__deck.append("J" + self.__suit)
                    self.__fullArrangedDeck.append("J" + self.__suit)
                elif j == 11:
                    self.__deck.append("Q" + self.__suit)
                    self.__fullArrangedDeck.append("Q" + self.__suit)
                elif j == 12:
                    self.__deck.append("K" + self.__suit)
                    self.__fullArrangedDeck.append("K" + self.__suit)
                else:
                    self.__deck.append(str(j + 1) + self.__suit)
                    self.__fullArrangedDeck.append(str(j + 1) + self.__suit)

    # Print the entire deck in the order it's currently in with each card on a new line
    def print(self):
        for i in range(len(self.__deck)):
            print(format(self.__deck[i], ">3s"))

    def shuffle(self):
        random.shuffle(self.__deck)

    # Put all the cards currently in the deck back in order
    def arrange(self):
        arrangedDeck = self.__fullArrangedDeck
        missingCards = []
        for i in range(len(arrangedDeck)):
            if arrangedDeck[i] not in self.__deck:
                missingCards.append(arrangedDeck[i])
        for i in range(len(missingCards)):
            arrangedDeck.remove(missingCards[i])
        self.__deck = arrangedDeck

    # Reset the deck to being full and in order
    def restore(self):
        self.__deck = []
        self.__fullArrangedDeck = []
        for i in range(4):
            suits = "CDHS"
            if suits[i] == "C":
                self.__suit = "\u2663"
            if suits[i] == "D":
                self.__suit = "\u2662"
            if suits[i] == "H":
                self.__suit = "\u2661"
            if suits[i] == "S":
                self.__suit = "\u2660"
            for j in range(13):
                if j == 0:
                    self.__deck.append("A" + self.__suit)
                elif j == 10:
                    self.__deck.append("J" + self.__suit)
                elif j == 11:
                    self.__deck.append("Q" + self.__suit)
                elif j == 12:
                    self.__deck.append("K" + self.__suit)
                else:
                    self.__deck.append(str(j + 1) + self.__suit)
        self.__fullArrangedDeck = self.__deck

    def deal(self):
        c = Card()  # The card that gets pulled out needs to have attributes of a card, not a deck
        drawn = self.__deck.pop(0)  # Remove the card that gets pulled out from the deck
        num = drawn[0:len(drawn) - 1]
        suit = drawn[len(drawn) - 1]
        # Reformat the values so it can be printed
        if num == "A":
            c.num = 1
        elif num == "J":
            c.num = 11
        elif num == "Q":
            c.num = 12
        elif num == "K":
            c.num = 13
        else:
            c.num = int(num)
        if suit == "\u2663":
            c.suit = "C"
        elif suit == "\u2662":
            c.suit = "D"
        elif suit == "\u2661":
            c.suit = "H"
        else:
            c.suit = "S"
        return c

    def numCards(self):
        return len(self.__deck)


class Hand:
    def __init__(self):
        self.__hand = []

    def addCard(self, card):
        # Reformat so it will work in the card class
        if card.suit == "C":
            suit = "\u2663"
        elif card.suit == "D":
            suit = "\u2662"
        elif card.suit == "H":
            suit = "\u2661"
        else:
            suit = "\u2660"
        if card.num == 1:
            cardString = "A" + suit
        elif card.num == 11:
            cardString = "J" + suit
        elif card.num == 12:
            cardString = "Q" + suit
        elif card.num == 13:
            cardString = "K" + suit
        else:
            cardString = str(card.num) + suit
        self.__hand.append(cardString)

    def numCards(self):
        return len(self.__hand)

    def print(self):
        for i in range(len(self.__hand)):
            print(format(self.__hand[i], ">3s"), end=" ")

    def printBlackJackDealer(self):
        for i in range(len(self.__hand)):
            if i != 0:
                print(format(self.__hand[i], ">3s"), end=" ")
            else:
                print(format("??", ">3s"), end=" ")

    def blackJackValue(self):
        hand = []
        total = 0
        # Collect the numbers of the cards in hand
        for i in range(len(self.__hand)):
            card = self.__hand[i]
            hand.append(card[0:len(card) - 1])
        # Set Ace, Jack, Queen, and King to their blackjack values
        for i in range(len(hand)):
            if hand[i] == "A":
                hand[i] = 11
            elif hand[i] == "J" or hand[i] == "Q" or hand[i] == "K":
                hand[i] = 10
            else:
                hand[i] = int(hand[i])
        # If having Ace = 11 means we bust, set Ace to 1 instead. If there are multiple, set more than one to equal 1
        minimizedAce = False
        for i in range(len(hand)):
            total += hand[i]
            if 11 in hand and total > 21 and not minimizedAce:
                minimizedAce = True
                total -= 10

        return total

# Everything below this line is preset. Do not change.

class BlackJackGame:
    def __init__(self):
        self.__d = Deck()
        self.__d.shuffle()

    def displayLine(self, who, hand):
        print(who + ": ", end="")
        print(" (" + str(hand.blackJackValue()) + ")\t", end="")
        hand.print()
        if hand.numCards() <= 5:
            print("\t", end="")
        if hand.numCards() <= 3:
            print("\t", end="")

    def pickWinner(self, n, dn, b, db, pf, df):
        print()
        if n and not dn:
            print("\t\tyou win!")
        elif n and dn:
            print("\t\t(push)")
        elif not n and dn:
            print("\t\tdealer wins.")
        elif b and not db:
            print("\t\tdealer wins.")
        elif not b and db:
            print("\t\tyou win!")
        elif pf == df:
            print("\t\t(push)")
        elif pf > df:
            print("\t\tyou win!")
        else:
            print("\t\tdealer wins.")
        print()

    def play(self):
        print()
        print("\t\tWelcome to Simple Blackjack")
        print()

        while True:
            if self.__d.numCards() < 14:
                print("\t\t\t\t\tDealer shuffles the deck")
                self.__d.restore()
                self.__d.shuffle()

            dealer = Hand()
            player = Hand()

            natural = False
            dnatural = False
            busted = False
            dbusted = False
            playerfinal = 0
            dealerfinal = 0

            dealer.addCard(self.__d.deal())
            dealer.addCard(self.__d.deal())

            print("dealer" + ": ", end="")
            print(" (??)\t", end="")
            dealer.printBlackJackDealer()
            print()

            player.addCard(self.__d.deal())
            player.addCard(self.__d.deal())

            if player.blackJackValue() == 21:
                self.displayLine("player", player)
                print("natural blackjack!")
                natural = True

            while player.blackJackValue() < 21:
                self.displayLine("player", player)
                response = input("hit? [y/n] ")
                if response == "n":
                    break
                player.addCard(self.__d.deal())

            self.displayLine("player", player)
            playerfinal = player.blackJackValue()
            if playerfinal == 21 and not natural:
                print("blackjack!")
            elif playerfinal > 21:
                print("you busted.")
                busted = True
            else:
                print("you hold.")

            time.sleep(1)

            if dealer.blackJackValue() == 21:
                self.displayLine("dealer", dealer)
                print("dealer blackjack!")
                dnatural = True

            if busted:
                self.displayLine("dealer", dealer)
                print()

            if not natural and not busted:
                while dealer.blackJackValue() <= 15 and not busted:
                    self.displayLine("dealer", dealer)
                    print("dealer hits.")
                    time.sleep(1)

                    dealer.addCard(self.__d.deal())

                self.displayLine("dealer", dealer)
                dealerfinal = dealer.blackJackValue()
                if dealerfinal == 21 and not dnatural:
                    print("dealer blackjack!")
                elif dealerfinal > 21:
                    print("dealer busted.")
                    dbusted = True
                else:
                    print("dealer holds.")

            time.sleep(1)

            self.pickWinner(natural, dnatural, busted, dbusted, playerfinal, dealerfinal)

            response = input("\t\t\t\t\tplay again? [y/n] ")
            if response == "n":
                break

        print("\t\t\t\t\tso long!")
        print()


def cardTest():
    print()
    print("Card Test")
    print()
    c1 = Card()
    c2 = Card(13, "H")
    c3 = Card(3, "C")
    c4 = Card(3, "D")

    c1.print()
    c2.print()
    c3.print()
    c4.print()
    print()
    print(format(c1.blackJackValue(), "3.0f"), end=" ")
    print(format(c2.blackJackValue(), "3.0f"), end=" ")
    print(format(c3.blackJackValue(), "3.0f"), end=" ")
    print(format(c4.blackJackValue(), "3.0f"), end=" ")
    print()
    print()

    c0 = Card(13, "C")
    c1 = Card(1, "D")
    c2 = Card(2, "D")
    c3 = Card(3, "D")
    c4 = Card(10, "D")
    c5 = Card(11, "D")
    c6 = Card(12, "D")
    c7 = Card(13, "D")
    c8 = Card(1, "H")
    c9 = Card(1, "S")
    c0.print()
    c1.print()
    c2.print()
    c3.print()
    c4.print()
    c5.print()
    c6.print()
    c7.print()
    c8.print()
    c9.print()
    print()
    print(c0 < c1)
    print(c1 < c2)
    print(c2 < c3)
    print(c3 < c4)
    print(c4 < c5)
    print(c5 < c6)
    print(c6 < c7)
    print(c7 < c8)
    print(c8 < c9)
    print(c9 < c0)


def deckTest():
    print()
    print("Deck Test")
    print()
    d = Deck()
    d.print()
    print()
    d.shuffle()
    d.print()
    print()
    d.arrange()
    d.print()
    print()
    c0 = d.deal()
    c1 = d.deal()
    c0.print()
    c1.print()
    print()
    print()
    d.print()
    print()
    print(d.numCards())
    d.restore()
    print(d.numCards())
    print()
    d.print()
    print()


def handTest():
    print()
    print("Hand Test")
    print()
    c1 = Card(1, "S")
    c2 = Card(13, "H")
    c3 = Card(3, "C")
    h = Hand()
    h.addCard(c1)
    h.addCard(c2)
    h.print()
    print()
    print(h.numCards())
    h.addCard(c3)
    h.print()
    print()
    print(h.numCards())
    print()

    h2 = Hand()
    h2.addCard(c1)
    h2.addCard(c2)
    h2.printBlackJackDealer()
    print()
    h2.print()
    print("=", h2.blackJackValue())
    print()
    h2.addCard(c3)
    h2.print()
    print("=", h2.blackJackValue())
    print()


def test():
    cardTest()
    deckTest()
    handTest()


def main():
    game = BlackJackGame()
    game.play()

    # test()


main()
