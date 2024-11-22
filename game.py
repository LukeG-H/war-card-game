from game_setup import *


def isGameWon(player1_hand, player2_hand):
    game_won = False
    winner = 'Nobody'

    if len(player1_hand) == 0:
        game_won = True
        winner = "Player 2"
    elif len(player1_hand) == 52:
        game_won = True
        winner = "Player 1"
    elif len(player2_hand) == 0:
        game_won = True
        winner = "Player 1"
    elif len(player2_hand) == 52:
        game_won = True
        winner = "Player 2"
    return game_won, winner


def playGame(player1, player2):
    player1_hand = player1
    player2_hand = player2
    game_won = False
    game_draw = False
    count_rounds = 0
    rounds_won = {}
    
    # print(f"P1 BEFORE:\n{player1_hand}\n\nP2 BEFORE:\n{player2_hand}\n")
    while not game_won and not game_draw:
        game_won, winner = isGameWon(player1_hand, player2_hand)
        
        if game_won:
            break
        round_winner = playRounds(player1_hand,player2_hand)
    
        if round_winner not in rounds_won:
            rounds_won[round_winner] = 0
        rounds_won[round_winner] += 1
        count_rounds += 1
        
        print(f"ROUND WINNER: {round_winner}\n")

# comment this out for actual game -> set to True to play 1 round of game (for test purposes)     
        # game_won = True
        if count_rounds >= 1500:
            game_draw = True
            print(f"Reached {count_rounds} Rounds... Call it a draw!")
# TODO if draw -> player with highest number of cards wins, or if the same player that won highest number of rounds, or nobody

    # print(f"Player 1's Hand AFTER:\n{player1_hand}\n\nPlayer 2's Hand AFTER:\n{player2_hand}\n")
    print(f"Player 1 has: {len(player1_hand)} cards and Player 2 has: {len(player2_hand)} cards\n")
    print(f"After {count_rounds} rounds, the number of rounds won by each player was: {rounds_won}")      
    return winner


def playRounds(player1_hand, player2_hand):
    player1_flipped_card = player1_hand.pop(0)
    print(f"Player 1 Card: {player1_flipped_card}")

    player2_flipped_card = player2_hand.pop(0)
    print(f"Player 2 Card: {player2_flipped_card}")

    round_winner, winnings = decideWhoWon(player1_flipped_card, player2_flipped_card, player1_hand, player2_hand)
    
    if round_winner == "Player 1":
        player1_hand.extend(winnings)
    elif round_winner == "Player 2":
        player2_hand.extend(winnings) 
    return round_winner


def decideWhoWon(player1_flipped_card, player2_flipped_card, player1_hand, player2_hand):
# split player card string into list of elements and get the first index
        p1_str = player1_flipped_card.split(" ")[0]
        p2_str = player2_flipped_card.split(" ")[0]
        winnings = [player1_flipped_card, player2_flipped_card]

# set the card letters to their equivalent values, as strings
# TODO abstract this out or make it better. this looks hideous
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
        print(f"{p1_value} vs {p2_value}\n")

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
# DONE: need to check if either player has 0 cards during the 'war' otherwise 'pop from empty list error' -> probably best to make a function
    war_cards_pot = []
    print("# WAR ROUND #")

    for _ in range(0,3):
        game_won, winner = isGameWon(player1_hand, player2_hand)
        
        if game_won:
            return winner, war_cards_pot
        player1_carddown = player1_hand.pop(0)
        war_cards_pot.append(player1_carddown)
        player2_carddown = player2_hand.pop(0)
        war_cards_pot.append(player2_carddown)
    # prints to check the correct cards are winning and being added to other players hand
    # print(f"WAR CARDS POT: {war_cards_pot}")
    # print(f"P1 Hand: {player1_hand}\nP2 Hand: {player2_hand}")
    game_won, winner = isGameWon(player1_hand, player2_hand)

    if game_won:
        return winner, war_cards_pot
    player1_war_card = player1_hand.pop(0)
    print(f"Player 1 War card: {player1_war_card}")

    player2_war_card = player2_hand.pop(0)
    print(f"Player 2 War card: {player2_war_card}")

    war_winner, winning_cards = decideWhoWon(player1_war_card,player2_war_card,player1_hand,player2_hand)
    print(f"WAR WINNER: {war_winner}")

    war_cards_pot.extend(winning_cards)
    return war_winner, war_cards_pot


def main():
    deck = setUpDeck()
    player1_hand, player2_hand = setUpGame(deck)
    winner = playGame(player1_hand,player2_hand)
    print(f"THE WINNER IS: {winner}")

if __name__ == '__main__':
    main()