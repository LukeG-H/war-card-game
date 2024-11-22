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
    
    def createDeck(self):
        for value in VALUES:
            for suit in SUITS:
                cards = str(Card(value, suit))
                self.deck.append(cards)
    
    def shuffleDeck(self):
        random.shuffle(self.deck)

    def dealCardFromDeck(self):
        card = self.deck.pop(0)
        return card
    
    def splitDeckInTwo(self):
        first_half = []
        second_half = []
        
        for _ in range(0,26):
            first_half.append(self.deck.pop(0))

        second_half = (self.deck)
        return first_half, second_half


def setUpDeck():
    deck = Deck()
    deck.createDeck()
    return deck


def setUpGame(deck):
    deck.shuffleDeck()
    player1_hand, player2_hand = deck.splitDeckInTwo()
    return player1_hand, player2_hand


def playGame(player1, player2):
    player1_hand = player1
    player2_hand = player2
    
    game_won = False
    count_rounds = 0
    rounds_won = {}
    winner = ""
    
    print(f"P1 BEFORE:\n{player1_hand}\n\nP2 BEFORE:\n{player2_hand}\n")
    
    while not game_won:
        # print(count_rounds)

        if len(player1_hand) == 0:
            winner = "Player 2"
            game_won = True

        elif len(player2_hand) == 0:
            winner = "Player 1"
            game_won = True
        
        else:
            round_winner = playRounds(player1_hand,player2_hand)
        
            if round_winner not in rounds_won:
                rounds_won[round_winner] = 0
            rounds_won[round_winner] += 1
            
            count_rounds += 1
    # comment this out for actual game -> set to True to play 1 round of game (for test purposes)     
            game_won = True
            print(f"ROUND WINNER: {round_winner}\n")

    print(f"P1 AFTER:\n{player1_hand}\n\nP2 AFTER:\n{player2_hand}\n")
    # print(f"P1 Turns: {player1_turns}, P2 Turns: {player2_turns}, Rounds: {count_rounds}, Game Won: {game_won}")
    print(f"After {count_rounds} rounds, the number of rounds won by each player was: {rounds_won}")
            
    return winner

def playRounds(player1_hand, player2_hand):
    player1_flipped_card = player1_hand.pop(0)
    print(f"Player 1 Card: {player1_flipped_card}")

    player2_flipped_card = player2_hand.pop(0)
    print(f"Player 2 Card: {player2_flipped_card}")

    round_winner, winnings = decideWhoWon(player1_flipped_card, player2_flipped_card, player1_hand, player2_hand)
    
    if round_winner == "Player 1":
        # player1_hand.append(player2_flipped_card)
        # player1_hand.append(player1_flipped_card)
        player1_hand.extend(winnings)
    
    if round_winner == "Player 2":
        # player2_hand.append(player1_flipped_card)
        # player2_hand.append(player2_flipped_card)
        player2_hand.extend(winnings)
        
    return round_winner
    
def decideWhoWon(player1_flipped_card, player2_flipped_card, player1_hand, player2_hand):
# split player card string into list of elements and get the first index
        p1_str = player1_flipped_card.split(" ")[0]
        p2_str = player2_flipped_card.split(" ")[0]
        winnings = [player1_flipped_card, player2_flipped_card]
# set the card letters to their equivalent values, as strings
        if p1_str or p2_str in ('A','K','Q','J'):
            if p1_str == 'A':
                p1_str = '14'
            if p2_str == 'A':
                p2_str = '14'
            
            if p1_str == 'K':
                p1_str = '13'
            if p2_str == 'K':
                p2_str = '13'

            if p1_str == 'Q':
                p1_str = '12'
            if p2_str == 'Q':
                p2_str = '12'

            if p1_str == 'J':
                p1_str = '11'
            if p2_str == 'J':
                p2_str = '11'
# convert the string values of each card into ints
        p1_value = int(p1_str)
        p2_value = int(p2_str)
        print(f"{p1_value} vs {p2_value}")
        # print(type(p1_value), type(p2_value))
        # print(p1_value + 1, p2_value + 1)
 # determine which card is 'higher' in value and set the winner, if cards are equal then go to war       
        if p1_value > p2_value:
            winner = "Player 1"
        elif p1_value < p2_value:
            winner = "Player 2"
        else:
            winner, war_winnings = goToWar(player1_hand,player2_hand)
            winnings.extend(war_winnings)
        return winner, winnings


def goToWar(player1_hand, player2_hand):
# TODO need to check if either player has 0 cards during the 'war' otherwise 'pop from empty list error'
    war_cards_pot = []
    for _ in range(0,3):
        player1_carddown = player1_hand.pop(0)
        war_cards_pot.append(player1_carddown)
        player2_carddown = player2_hand.pop(0)
        war_cards_pot.append(player2_carddown)
    
    print(f"WAR CARDS POT: {war_cards_pot}")
    print(f"P1 Hand: {player1_hand}\nP2 Hand: {player2_hand}")

    player1_war_card = player1_hand.pop(0)
    print(f"P1 War card: {player1_war_card}")

    player2_war_card = player2_hand.pop(0)
    print(f"P2 War card: {player2_war_card}")

    war_winner, winning_cards = decideWhoWon(player1_war_card,player2_war_card,player1_hand,player2_hand)
    print(f"WAR WINNER: {war_winner}")
    war_cards_pot.extend(winning_cards)
    # winner = "DRAW"
    return war_winner, war_cards_pot


def main():
    deck = setUpDeck()
    player1_hand, player2_hand = setUpGame(deck)
    winner = playGame(player1_hand,player2_hand)
    print(f"The Winner is: {winner}")
    #  top_card_P1 = player1_hand[0]

if __name__ == '__main__':
    main()