"""
this application should be able to function as a blackjack game

things it will keep track of is 
a deck, hands, and it will declare winners

key feature: we will not need to build a cli / api in order
to validate that it works

goal: use testing to build out this blackjack service
"""
import random

# What is a card
# suit + value / type

# What is a deck
# a collection of unique cards

# Turns / Draws
# Hitting and Standing

# Busting

# A hand
# value of hand
# how to compare hands for winners

# Player count

# There is a pre-step (setup) where a deck is shuffled
# There is a round where some number of players participate
# There is initial base hand drawing 
# There are turns where players try to improve hands
# There is mandated actions on dealer hand
# There is declaration of win / loss

# Player, get a hand [(k, hearts), ]
# Blackjack(Players: [Player(Name), ...])
# Blackjack.dealerHand ? do we need this?


# Contains Cards, when you create it they are in order
# You can shuffle
# you can Deal
# you can reset

cardValues = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "Kind": 10,
    "Ace": (1, 11),
}

class Deck:
    def __init__(self):
        numbersStrList = [str(x) for x in range(2, 11)]
        cardTypes = ["Jack", "Queen", "King", "Ace", *numbersStrList]
        suits = ["Diamond", "Heart", "Spade", "Club"]

        self._starting_deck = [(value, suit) for suit in suits for value in cardTypes]
        self._deck = self._starting_deck.copy()

    def shuffle(self):
        random.shuffle(self._deck)
    
    def deal(self):
        return self._deck.pop()

    def reset(self):
        self._deck = self._starting_deck.copy()

class Blackjack:
    def __init__(self, players):
        # Ready, Player Turn, Dealer Turn, Payout
        self.status = "Ready"
        self.dealer = Player("Dealer")
        self.players = players
        self.yetToPlay = players.copy()
        self.deck = Deck()
        self.deck.shuffle()
    
    def initialDeal(self):
        self.dealCardToAll()
        self.dealCardToAll()
        self.status = "Player Turn"

    def dealCardToAll(self):
        for p in self.players:
            p.addToHand(self.deck.deal())
        self.dealer.addToHand(self.deck.deal())

    def getGameStatus(self):
        return self.status

    def getCurrentPlayer(self):
        hasNext = len(self.yetToPlay) > 0 
        if hasNext: 
            return self.yetToPlay[0]
        else:
            return None

    def takePlayerTurn(self, choice):
        match choice:
            case "Hit": 
                p = self.getCurrentPlayer()
                p.addToHand(self.deck.pop())
                if self.hasBusted(p):
                    self.yetToPlay.pop()

            case "Stand": 
                self.yetToPlay.pop()
            
        if len(self.yetToPlay) == 0:
            self.status == "Concluded"

    def hasBusted(self, player):
        total = 0
        for c in player.hand:
            cardValue = c[0]
            # If you have an ace default to lowest else get the value
            v = 1 if cardValue == "Ace" else cardValues[cardValue]
            total += v

        return total > 21


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def addToHand(self, card):
        self.hand.append(card)

    def resetHand(self):
        self.hand.clear()
