import random

# Helpful variables to create the deck
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2,
          'Three': 3,
          'Four': 4,
          'Five': 5,
          'Six': 6,
          'Seven': 7,
          'Eight': 8,
          'Nine': 9,
          'Ten': 10,
          'Jack': 10,
          'Queen': 10,
          'King': 10,
          'Ace': 11}


class Card:
    # Constructor
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    # Print function
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    # Constructor
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    # Function that returns the length of the deck
    def __len__(self):
        return len(self.all_cards)

    # Function that shuffle the deck
    def shuffle(self):
        random.shuffle(self.all_cards)

    # Function that extracts a card from the deck
    def deal_one(self):
        try:
            return self.all_cards.pop()
        except IndexError:
            print("There aren't any cards in the deck")

    # Destructor
    def __del__(self):
        pass
