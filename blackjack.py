import random
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

print("Welcome to blackJack!")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

first_hand_user = []
first_hand_computer = []

first_hand_user.append(random.choice(cards))
first_hand_user.append(random.choice(cards))
print(f"You currently have {sum(first_hand_user)}")

first_hand_computer.append(random.choice(cards))
first_hand_computer.append(random.choice(cards))
print(f"The dealer currently has {first_hand_computer[0]}")

draw_again = input('Would you like to draw again? "Yes" or "No"\n').lower()

if draw_again == "yes":
    next_card = random.choice(cards)
    first_hand_user.append(next_card)
    print(first_hand_user)
else:
    while sum(first_hand_computer) < 16:
        com_next_card = random.choice(cards)
        first_hand_computer.append(com_next_card)
        sum(first_hand_computer)
    print(first_hand_computer)


    # Todo create game loop for play again
    # Todo make function for gameplay
    # Show different values for the Ace depending on score
    # Create if logic to determine winner
    # Create statements to show final card set of both players to the user
    # Create inputs for better UI
    # Refractor code
