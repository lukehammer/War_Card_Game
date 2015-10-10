__author__ = 'luke'
import random

class Deck():
    def build(self):
        cards = []
        for suit in ["h","s","c","d"]:
            for i in range(1,14):
                cards.append(i)
        return cards
    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards


    def __init__(self):
        self.cards = self.build()
        self.shuffle(self.cards)


game = Deck()
print game.cards
game.shuffle()


#
#     deck = []
#     player1_deck = []
#     player2_deck = []
#     player1_discard = []
#     player2_discard = []
#     player1_hand = []
#     player2_hand = []
#
#
#
#     def deal_all_cards(self):
#         has_player_one_been_delt = 0
#         deal_from = deck
#         for card in deal_from:
#             if not has_player_one_been_delt:
#                 player1_deck.append(card)
#                 has_player_one_been_delt = 1
#                 print "player 1" + str(player1_deck)
#             else:
#                 player2_deck.append(card)
#                 has_player_one_been_delt = 0
#                 print "player 2" + str(player2_deck)
#
# def shuffle_deck(deck):
#     random.shuffle(deck)
#     print deck
#     return deck
#
#
#
# game = game()
#
#
#
# def playhand(game_state):
#     player1_deck = game_state[0]
#     player2_deck = game_state[1]
#     player1_card = player1_deck.pop()
#     player2_card = player2_deck.pop()
#     if player2_card > player1_card:
#         player2_deck.insert(0,player1_card)
#         player2_deck.insert(0,player2_card)
#     elif player2_card < player1_card:
#         player1_deck.insert(0,player1_card)
#         player1_deck.insert(0,player2_card)
#     else:
#         print "WAR WAR "+ str(player1_card)+ " VS " + str(player2_card)
#
#
#     print "+++++++++++++++++++++++++++++++++++"
#     print "player 1 deck "+ str(player1_deck)
#     print "player 2 deck "+ str(player2_deck)
#     return [player1_deck,player2_deck]
#
