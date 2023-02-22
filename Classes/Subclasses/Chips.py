class Chips:
    # Constructor
    def __init__(self, total=100):
        # This value can be set to a default value or supplied by a user input
        self.total = total
        self.bet = 0

    # Print function
    def __str__(self):
        return str(self.total)

    # Function if the bet is won
    def win_bet(self):
        self.total += self.bet
        self.bet = 0

    # Function if the bet is lost
    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0

    # Function if it's a tie
    def tie_bet(self):
        self.bet = 0
