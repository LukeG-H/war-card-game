import random

VALUES = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
SUITS = ["CLUBS","SPADES","HEARTS","DIAMONDS"]


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.deck = []
    
    def __str__(self):
        return f"{self.deck}"
    
    def create_deck(self):
        for value in VALUES:
            for suit in SUITS:
                cards = str(Card(value, suit))
                self.deck.append(cards)
    
    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_card_from_deck(self):
        card = self.deck.pop(0)
        return card
    
    def split_deck_in_two(self):
        first_half = []
        second_half = []
        
        for _ in range(0,26):
            first_half.append(self.deck.pop(0))

        second_half = (self.deck)
        return first_half, second_half