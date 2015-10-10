__author__ = 'luke'


class Card():
    def __init__(self, card_code):
        suits = \
            {'s': 'Spades',
             'd': 'Diamonds',
             'c': 'Clubs',
             'h': 'Hearts'}

        # just getting the first letter of the string to find suit

        suit_letter = card_code[0]
        self.suit = suits[suit_letter]

        # this section tests and assigns values to cards
        # first remove the first char from the Card_code

        l = list(card_code)
        l[0] = ""
        card_code = "".join(l)
        card_code = int(card_code)
        # this first section works with numbers 2 to 10
        if (card_code > 1) and (card_code < 11):
            self.value = card_code
        elif card_code == 13:
            self.value = "King"
        elif card_code == 12:
            self.value = "Queen"
        elif card_code == 11:
            self.value = "Jack"
        elif card_code == 1:
            self.value = "Ace"
        else:
            print("card does not have a valid value self.value not set")
        self.rank = card_code

        self.name = "{} of {}".format(self.value, self.suit)
