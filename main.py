from Classes.Deck import Deck
from Classes.Person import Person
import os


# Function to clear the historical output
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to stop the game
def stop_game():
    global player, dealer

    # Check if the player is out of chips
    if player.chips.total == 0:
        print(f'\n{player.name} is out of chips. {dealer.name} won the game')
        return False

    # Check if the dealer is out of chips
    elif dealer.chips.total <= 0:
        print(f'\n{dealer.name} is out of chips. {player.name} won the game')
        return False

    # Check if the player want to stop the game
    choice = 'wrong'
    while choice not in ['Y', 'y', 'n', 'N']:
        choice = input("\nWould you like to play another round? Y or N ")

        # Checks if the input is valid
        if choice not in ['Y', 'y', 'n', 'N']:
            print("Sorry, I didn't understand.")

    if choice in ['Y', 'y']:
        return True
    else:
        return False


#  Function that sets the hit or stand for the person
def hit_or_stand():
    choice = 'wrong'

    # Check if the player wants to hit or stand
    while choice not in ['Y', 'y', 'n', 'N']:
        choice = input("Yould you like to hit? Y or N ")
        
        # Checks if the input is valid
        if choice not in ['Y', 'y', 'n', 'N']:
            print("Sorry I didn't understand.")
    
    if choice in ['Y', 'y']:
        return 'HIT'
    else:
        return 'STAND'


# Print information about the round
def information(dealer, player):
    clear()
    # Shows all the cards and the cards value
    player.print()
    dealer.print()

    # Both the player and the dealer got busted
    if dealer.get_value() > 21 and player.get_value() > 21:
        print(f'Both {dealer.name} and {player.name} got busted.')

        # Set the score and resets the bet
        dealer.chips.tie_bet()
        player.chips.tie_bet()

    # It's a tie between the dealer and the player
    elif dealer.get_value() == player.get_value():
        print(f'{dealer.name} and {player.name} have the same total. It is a tie!')

        # Set the score and resets the bet
        dealer.chips.tie_bet()
        player.chips.tie_bet()

    # The dealer got busted
    elif dealer.get_value() > 21:
        print(f'{dealer.name} got busted. {player.name} won the round.')

        # Set the score and resets the bet
        dealer.chips.lose_bet()
        player.chips.win_bet()

    # The player got busted
    elif player.get_value() > 21:
        print(f'{player.name} got busted. {dealer.name} won the round.')

        # Set the score and resets the bet
        dealer.chips.win_bet()
        player.chips.lose_bet()

    # The dealer won the round
    elif dealer.get_value() > player.get_value():
        print(f'{dealer.name} has a bigger score and won the round.')

        # Set the score and resets the bet
        dealer.chips.win_bet()
        player.chips.lose_bet()

    # The player won the round
    else:
        print(f'{player.name} has a bigger score and won the round.')

        # Set the score and resets the bet
        dealer.chips.lose_bet()
        player.chips.win_bet()

    # Print the number of chips of the players
    print('\n')
    print(f'{dealer.name} has a total of {dealer.chips.total} chips')
    print(f'{player.name} has a total of {player.chips.total} chips')


# The actual game
def blackjack(dealer, player):
    clear()

    # Creates the card deck then shuffles it
    deck = Deck()
    deck.shuffle()

    # Deals 2 cards to the player and the dealer
    for _ in range(2):
        dealer.add_card(deck.deal_one())
        player.add_card(deck.deal_one())

    # Shows player cards and one of the dealer card
    player.print()
    print(f'{dealer.name} visible card is {dealer.hand.cards[0]}\n')

    # As long as the player wants/isn't busted pull a card
    choice = hit_or_stand()
    while choice == "HIT":
        player.add_card(deck.deal_one())
        if player.get_value() < 21:
            clear()
            player.print()
            print(f'{dealer.name} visible card is {dealer.hand.cards[0]}\n')

            choice = hit_or_stand()
        else:
            choice = "STAND"

    # As long as the dealer has a value < 17 he will pull
    while dealer.get_value() < 17:
        dealer.add_card(deck.deal_one())

    # Print final information
    information(dealer, player)


clear()
# Create the player and the dealer and sets the total of chips
player = Person(input("Player name: "))
player.set_total()
dealer = Person("The dealer", player.chips.total)


game_on = True
while game_on:
    clear()

    # Set the bet
    player.set_bet()
    dealer.chips.bet = player.chips.bet

    # Play a blackjack round
    blackjack(dealer, player)

    # Clears the hand
    dealer.clear_hand()
    player.clear_hand()

    # Check if the player want's to continue playing the game
    game_on = stop_game()

clear()
