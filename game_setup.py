# THIS FILE IS NOT NEEDED AS THE CLASSES AND METHODS ARE NOW CALLED DIRECTLY WITHIN 'game.py' #
# KEEPING FOR HISTORY AND FOR FUTURE ABSTRACTION IF NEEDED # 

from card_deck_classes import *

def set_up_deck():
    deck = Deck()
    return deck


def deal_player_hands(deck):
    player1_hand, player2_hand = deck.split_deck_in_two()
    return player1_hand, player2_hand