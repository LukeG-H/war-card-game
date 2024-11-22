###################
#       WAR       #
###################

The goal of this project was to create a simple implementation of the card game "WAR", in python. 
This was the result of a work discussion that led to a challenge between a colleague and I.
The aim being to challenge our programming abilities and to see how we approach the problem differently.

No AI generated code was used for this implementation.
Google and Youtube were the only references that I allowed myself to use.
My initial goal was to get something working as quickly as possible, with the 'promise to myself' that I would tidy-up and improve my solution over time.


# RULES #
    -> 2 Players split a deck of (shuffled) cards
    -> the players take turns to flip thier top card face-up
    -> the highest of the 2 cards wins that round, the winner of the round collects both cards
    -> if both cards are of equal value, then the players 'go to war'
        -> each player deals 3 of their cards face down and flips the 4th card
        -> the highest of these 2 cards 'wins the war' and collects all the cards dealt in that round (8 total)
    -> this continues until 1 player holds all the cards, leaving the other player with 0 cards

# RULES CONT. #
    -> Ace is the highest card (with a value = 14)
    -> 2 is the lowest card
    -> K > Q > J (where K = 13, Q = 12, J = 11)


