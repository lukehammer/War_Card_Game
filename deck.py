__author__ = 'luke'

import random

from cards import Card

class Deck():
    def build(self):
        cards = []
        for suit in ["h","s","c","d"]:
            for i in range(1,14):
                cards.append(suit + str(i))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards


    def __init__(self):
        self.cards = self.build()
        self.shuffle()

    def deal_one(self):
        if not len(self.cards) == 0:
            return self.cards.pop()
        else:
            print("you are out of cards to deal")
