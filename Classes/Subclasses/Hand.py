class Hand:
    # Constructor
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    # Add a card to the hand
    def add_card(self, card):
        self.cards.append(card)

        # Check if the card is an ace
        if card.value == 11:
            self.aces += 1

        # Adds the value of the card
        self.value += card.value

    # Function that adjust the value of the hand based on the aces
    def adjust_for_ace(self):
        while self.value > 21 and self.aces != 0:
            self.value -= 10
            self.aces -= 1

    # Function that returns the hand's value
    def get_value(self):
        self.adjust_for_ace()
        return self.value

    # Function that prints the hand
    def print_hand(self):
        for card in self.cards:
            print(card)

    # Function to clear the hand
    def clear_hand(self):
        self.cards = []
        self.value = 0
        self.aces = 0
