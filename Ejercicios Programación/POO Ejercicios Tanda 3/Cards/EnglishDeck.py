from Deck import Deck
from Card import Card


class EnglishDeck(Deck):

    def __init__(self):
        numbers = "1 2 3 4 5 6 7 8 9 10 J Q K".split()
        suits = "♠ ♡ ♢ ♣".split()
        cards = [Card(n, s) for s in suits for n in numbers]
        super().__init__(cards)