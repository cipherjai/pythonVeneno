# for random card shuffle
import random

# declaring the constant values for the whole game

#Boolean used to know which hand is playing
playing = False

pool_of_chips = 100000
bet = 1
phrase_to_shuffle = "Press 'd' to deal the cards again, or 'q' to quit"

# defining card flavors
# Hearts, Diamonds, Clubs, Spades

# Tuple is used just to make sure the order is maintained and referenced to same and cannot be changed.
suits = ('H', 'D', 'C', 'S')

#Possible card ranks
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

# Point values dict (Note: Aces can also be 11, check self.ace for details)
card_val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}


# Card class

class Card:
    """docstring for Card."""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + " " + self.rank

    def grab_suit(self):
        return self.suit

    def grab_rank(self):
        return self.rank

    def draw(self):
        print(self.suit + self.rank)

class Hand:
    """ doctstring for Hand Class """

    def __init__(self):
        self.cards = []
        self.value = 0
        # Aces can be 1 or 11
        self.ace = False

    def __str__(self):
        # return string of current hand composition
        hand_comp = ""

        # List Comprehension
        for card in self.cards:
            card_name = card.__str__()
            hand_comp += " " + card_name

        return 'The hand has %s' %hand_comp

    def card_add(self, card):
        ''' Add another card to hand '''
        self.cards.append(card)

        #check for aces in variable:
        if (card.rank == 'A'):
            self.ace = True
        self.value += card_val[card.rank]

    def card_val(self):
        """Calculate the value of the hand, make aces an 11 if thet don't bust the hand"""
        if(self.ace == True and self.value <12):
            return self.value + 10
        else:
            return self.value

    def draw(self, hidden):
        self.card = null
        
