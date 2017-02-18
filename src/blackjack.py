import random

playing = False
chip_pool = 100
bet = 1
restart_phrase = "press 'd' to deal the cards again or press 'q' to quit "

suits = ('H', 'D', 'C', 'S')

ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

card_val = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def draw(self):
        print self.suit + self.rank


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False

    def __str__(self):
        hand_comp = ""

        # Better way to do this? List comprehension?
        for card in self.cards:
            card_name = card.__str__()
            hand_comp += " " + card_name

        return 'The hand has %s' % hand_comp

    def add_card(self, card):
        self.cards.append(card)

        if card.rank == 'A':
            self.ace = True
        self.value += card_val[card.rank]

    def card_value(self):
        if self.ace is True and self.value < 12:
            return self.value + 10
        else:
            return self.value

    def draw(self, hidden):
        if hidden is True and playing is True:
            # Don't show first hidden card
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()


