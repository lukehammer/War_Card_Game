__author__ = 'luke'
import random

from deck import Deck
from hand import Hand
from cards import Card
from players import Player

# get shuffeled deck
deck = Deck()

# get Players
luke = Player("luke")
toni = Player("toni")

# deal cards
while len(deck.cards) > 0:
    luke.recive_card(deck.deal_one())
    toni.recive_card(deck.deal_one())

print("lukes cards" + str(luke.deck))
print("deck" + str(deck.cards))

# start playing hands
count = 0
luke_max_cards = 0
pile = []
while (len(toni.deck) > 0) and (count < 2000000) and (len(luke.deck) > 0):
    lukes_card = Card(luke.top_card())
    tonis_card = Card(toni.top_card())
    print(lukes_card.name + " vs " + tonis_card.name)
    pile.append(luke.give_top_card())
    pile.append(toni.give_top_card())
    if lukes_card.rank > tonis_card.rank:
        luke.deck.extend(pile)
        pile = []
        print("luke wins")
    elif tonis_card.rank > lukes_card.rank:
        toni.deck.extend(pile)
        pile = []
        print("toni wins")
    else:
        print("WARWARWARWARWARWARWARWARWARWARWARWARWARWARWARWARWARWARWARWARWARWARWARWARWARWARWARWARWARWARWARWAR")
        pile.append(luke.give_top_card())
        pile.append(toni.give_top_card())
        pile.append(luke.give_top_card())
        pile.append(toni.give_top_card())
        pile.append(luke.give_top_card())
        pile.append(toni.give_top_card())

    count = count + 1
    print("{} is the number of hand played".format(str(count)))
    # print("lukes max cards " + str(luke_max_cards))
    print("toni has :{} cards and Luke has :{} cards and there a {} in the pile".format(len(toni.deck), len(luke.deck),
          len(pile)))

    number = len(luke.deck) + len(toni.deck) + len(pile)
    if luke_max_cards < len(luke.deck):
        luke_max_cards = len(luke.deck)

    print("number of cards in decks " + str(number))
    print("tonis cards" + str(toni.deck))
    print("lukes cards" + str(luke.deck))



print(luke_max_cards)
print("tonis cards" + str(toni.deck))
print("lukes cards" + str(luke.deck))



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
