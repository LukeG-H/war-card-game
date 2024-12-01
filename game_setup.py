from card_deck_classes import *

def set_up_deck():
    deck = Deck()
    deck.create_deck()
    return deck


def set_up_game(deck):
    deck.shuffle_deck()
    player1_hand, player2_hand = deck.split_deck_in_two()
    return player1_hand, player2_hand