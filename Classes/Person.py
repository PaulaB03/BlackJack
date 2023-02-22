from Classes.Subclasses.Chips import Chips
from Classes.Subclasses.Hand import Hand


class Person:
    # Constructor
    def __init__(self, name, total=100):
        self.name = name
        self.hand = Hand()
        self.chips = Chips(total)

    # Function that adds new card in the hand
    def add_card(self, new_card):
        self.hand.add_card(new_card)

    # Print function
    def print(self):
        print(f'{self.name} cards have a value of {self.hand.get_value()}')
        print("The cards:")
        self.hand.print_hand()
        print("\n")

    # Function that sets the total of chips
    def set_total(self):
        result = 'wrong'
        # Loop for imputing a numeral value
        while True:
            try:
                result = int(input("Please provide the number of chips: "))
            except ValueError:
                print("That is not a number")
                continue
            else:
                break

        self.chips.total = result

    # Function that sets the bet
    def set_bet(self):
        result = 'wrong'
        # Loop for imputing a numerical value
        while True:
            try:
                result = int(input("Please provide this round bet: "))
            except ValueError:
                print("That's not a number")
                continue
            else:
                if result > self.chips.total:
                    print("You don't have that many chips")
                    continue
                elif result <= 0:
                    print("You can't input this value")
                else:
                    break

        self.chips.bet = result

    # Function that clears the hand
    def clear_hand(self):
        self.hand.clear_hand()

    # Function that gets the value of the hand
    def get_value(self):
        return self.hand.get_value()
