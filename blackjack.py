# Welcome to day 11 of the 100 days of code challenge. This project has been my
# hardest project to date. It consists of a blackjack game where the user, plays
# against the computer to be the closest to 21. While this project has taken me
# multiple days to complete, I have still heldfast to the 100 days of code,
# coding a little each day no mater what. Poke around a bit and enjoy playing
# some blackjack!

#import random and logo modules for later use
import random
from logos import logo

############### Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# Prints the logos and welcome statement
print(logo)
print("Welcome to blackJack!")

# List of cards to choose from
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Empty lists to eventually hold the compuer and users cards
hand_user = []
hand_computer = []

# Function Section: Here are all the functions used to run the game.
def draw():
    """Draw fuction, takes a random card from the cards list and adds it to
    the users hand of cards"""

    next_card = random.choice(cards)
    hand_user.append(next_card)
    print(f"Your cards: {hand_user} Current total: {sum(hand_user)}")

def computer_play():
    """Computer play function, this function contains all the logic of the
    computers turn. The computer stops adding cars to its hand when it reaches
    a sum of 16 points"""

    while sum(hand_computer) < 16:
        comp_next_card = random.choice(cards)
        hand_computer.append(comp_next_card)
        sum(hand_computer)

def ace_change():
    """Ace change function, this function takes any aces in the deck and
    changes their value from 11 to 1"""
    # For loop using enumerate to look for all values of 11 to change them to 1
    for index, num in enumerate(hand_user):
        if num == 11:
            hand_user[index] = 1
    print(f"You have an ace! Your new cards are: {hand_user} Current total: {sum(hand_user)}")


def evaluate():
    """Evaluate function, contains all of the logic to determine if the
    computer or the user is the winner"""

    # Computer automactially wins it gets 21 no matter if the user has one, this is why it comes first
    if sum(hand_computer) == 21:
        print(f"Dealer has {hand_computer}. Dealer Wins!")

    # If the user gets 21 they win, only if the computer does not have 21
    elif sum(hand_user) == 21:
        print(f"You have {hand_user}. You win!")

    # If the computer goes over 21 the user wins
    elif sum(hand_computer) > 21:
        print(f"Dealer has {hand_computer}. Total: {sum(hand_computer)}")
        print(f"You have {hand_user}. Total: {sum(hand_user)} You win!")

    # If the user and computer share the same total value its a draw
    elif sum(hand_user) == sum(hand_computer):
        print(f"Draw! Dealer has {hand_computer} you have {hand_user}.")

    # If the users hand is bigger than the computers they win.
    elif sum(hand_user) > sum(hand_computer):
        print(f"Dealer has {hand_computer}. Total: {sum(hand_computer)}")
        print(f"You have {hand_user}. Total: {sum(hand_user)} You win!")

    # If the users hand is smaller than the computer they lose.
    elif sum(hand_user) < sum(hand_computer):
        print(f"You have {hand_user}. Total: {sum(hand_user)}")
        print(f"Dealer has {hand_computer}. Total: {sum(hand_computer)} Dealer wins!")

def game_start():
    """Game Start is the main game logic function. It contains all of the code
    to run the game"""
    # Initalizing game state
    playing = True

    # Starting hand for the user by adding two card to the empty list
    hand_user.append(random.choice(cards))
    hand_user.append(random.choice(cards))

    # Showing the users cars and total sum using f strings
    print(f"Your cards: {hand_user} Current total: {sum(hand_user)}")

    # Starting hand for the computer by adding two cards to the empty list
    hand_computer.append(random.choice(cards))
    hand_computer.append(random.choice(cards))

    # Showing the computers first card to the user using f strings
    print(f"The dealers first card is {hand_computer[0]}")


    # Main Game Loop
    while playing:
        # If the user has less than a sume of 22 they can draw another card
        if sum(hand_user)< 22:
            draw_again = input('Would you like to draw again? "Yes" or "No"\n').lower()
            if draw_again == "yes":
                draw()
            # If the user goes over 21 the computer plays and winner is evaluated
            else:
                playing = False
                computer_play()
                evaluate()
        # If the user has an ace in hand and goes over 21 aces change and score revaluated
        elif sum(hand_user) >= 22 and 11 in hand_user:
            ace_change()
            draw_again = input('Would you like to draw again? "Yes" or "No"\n').lower()
            if draw_again == "yes":
                draw()
            else:
                playing = False
                computer_play()
                evaluate()
        # If the user goes over 21 they lose.
        else:
            print(f"Your cards: {hand_user} Total: {sum(hand_user)}. You went over 21 You Lose")
            computer_play()
            playing = False

# Calling the Game start function to start the game.
game_start()

# Here a while loop is placed to ask the user if they wish to continue playing
# This is something that was not asked of the project but convient to the user
while True:
    # Ask the user if they want to play again
    new_game = input('Would you like to play again? "Yes" or "No"\n').lower()

    # If yes clear the previous game's hand and call game_start to start again
    if new_game == "yes":
        hand_user = []
        hand_computer = []
        game_start()
    else:
        break
