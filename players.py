__author__ = 'luke'

class Player():
    def __init__(self, name):
        self.name = name
        self.deck = []


    def recive_card(self,card):
        self.deck.append(card)

    def top_card(self):
        return self.deck[0]

    def give_top_card(self):
        return self.deck.pop(0)

