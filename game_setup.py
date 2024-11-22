from card_deck_classes import *

def setUpDeck():
    deck = Deck()
    deck.createDeck()
    return deck


def setUpGame(deck):
    deck.shuffleDeck()
    player1_hand, player2_hand = deck.splitDeckInTwo()
    return player1_hand, player2_hand