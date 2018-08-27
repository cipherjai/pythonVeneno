# for random card shuffle
import random

# declaring the constant values for the whole game

#Boolean used to know which hand is playing
playing = False

chip_pool = 100000
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

    def calc_val(self):
        """Calculate the value of the hand, make aces an 11 if thet don't bust the hand"""
        if(self.ace == True and self.value <12):
            return self.value + 10
        else:
            return self.value

    def draw(self, hidden):
        if hidden == True and playing == True:
            # Don't show first hidden card
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()


class Deck:

    def __init__(self):
        '''Creating a deck in order'''
        self.deck = []
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        """ Shuffle the deck """
        random.shuffle(self.deck)

    def deal(self):
        '''Grab first item in deck'''
        single_card = self.deck.pop()
        return single_card

    def __str__(self):
        deck_comp = ""
        for card in self.cards:
            deck_comp += " " + deck_comp.__str__()

        return "The deck has" + deck_comp


def make_bet():
    ''''Ask the player for the bet amount and '''
    global bet
    bet = 0

    print("What amount of chips you want to enter? Enter whole number please ! ")

    while bet == 0:
        bet_comp = input("> ") # for checking the amount to bet
        bet_comp = int(bet_comp)

        # checking for the amount of chips left and bet applied
        if bet_comp >= 1 and bet_comp <= chip_pool:
            bet = bet_comp
        else:
            print("Invalid bet, you only have %s chips left !" % str(chip_pool))

def deal_cards():
    """Deals up cards and sets up rounds"""

    # set up all global variable
    global result, playing, deck, player_hand, dealer_hand, chip_pool, bet

    # create a deck
    deck = Deck()

    # shuffle it
    make_bet()

    # Set up both player and dealer's hand
    player_hand = Hand()
    dealer_hand = Hand()

    # dealing out initial cards
    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())

    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    result = "Hit or Stand? Press either h or s > "

    if playing == True:
        print('Fold, Sorry')
        chip_pool -= bet

    # Set up to know currently playing Hand
    playing = True
    game_step()


def hit():

    """Ïmplement Hit"""
    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

    # If hand is in play, add card
    if playing:
        if player_hand.calc_val() <= 21:
            player_hand.card_add(deck.deal())

        print("Player Hand is %s" %player_hand)

        if player_hand.calc_val() <= 21:
            result = 'Busted!' + phrase_to_shuffle

            chip_pool -= bet
            playing = False

    else:
        result = "Sorry, can't hit" + phrase_to_shuffle

    game_step()


def stand():
    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet
    ''' This function will now play the dealers hand, since stand was chosen '''

    if playing == False:
        if player_hand.calc_val() > 0:
            result = "Sorry, you can't stand !"

    # Now go through all other possible options
    else:

        # Soft 17 Rule
        while dealer_hand.calc_val() < 17:
            dealer_hand.card_add(deck.deal())

        # Dealer Busts
        if dealer_hand.calc_val() > 21:
            result = 'Dealer busts! You win!' + phrase_to_shuffle
            chip_pool += bet
            playing =  False

            # If player has better hand than dealer
        elif dealer_hand.calc_val() < player_hand.calc_val():
            result = 'You beat the dealer, you Won!!' + phrase_to_shuffle
            chip_pool += bet
            playing = False

        # Push
        elif dealer_hand.calc_val() == player_hand.calc_val():
            result = 'Tied up, Push!' +phrase_to_shuffle
            playing = False

        # Dealer beats player
        else:
            result = 'Dealer Wins!' + phrase_to_shuffle
            chip_pool -= bet
            playing = False
    game_step()

def game_step():

    # Function to print game step/status on output

    # Display Player hand
    print (" ")
    print('Player Hand is: ' , player_hand.draw(hidden=False))

    print("Player total hand is: " + str(player_hand.calc_val()))

    #Display Dealer Hand
    print('Dealer Hand is: ', dealer_hand.draw(hidden=True))

    # If game round is over
    if playing == False:
        print("--- for a total of " + str(dealer_hand.calc_val()))
        print("Chip total: " + str(chip_pool))

    # Otherwise, don't know the second card yet
    else:
        print("With another card hidden upside down")

    # Print Result of hit or stand
    print(result)
    player_input()


def game_exit():
    print("Thanks for Playing!")
    exit()

def player_input():
    # Read the user input, Lowercase it

    plin = input("> ").lower()

    if plin == 'h':
        hit()

    elif plin == 's':
        stand()

    elif plin == 'd':
        deal_cards()

    elif plin == 'q':
        game_exit()

    else:
        print("Invalid Input... Enter h, s, d or q")
        player_input()


def intro():
    statement = '''Welcome to BlackJack! Get as close to 21 as you can without going over!
    Dealer hits until she reaches 17. Aces count as 1 or 11.
    Card output goes a letter followed by a number of face notation'''
    print(statement)

# Create a Deck
deck = Deck()
#Shuffle it
deck.shuffle()
# Create player and dealer hands
player_hand = Hand()
dealer_hand = Hand()
#Print the intro
intro()
# Deal out the cards and start the game!
deal_cards()
