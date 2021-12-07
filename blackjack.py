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

hand_user = []
hand_computer = []

def draw():
    next_card = random.choice(cards)
    hand_user.append(next_card)
    print(f"Your cards: {hand_user} Current total: {sum(hand_user)}")

def computer_play():
    while sum(hand_computer) < 16:
        comp_next_card = random.choice(cards)
        hand_computer.append(comp_next_card)
        sum(hand_computer)
    print(f"The dealers final hand is {hand_computer} Total: {sum(hand_computer)}")

def evaluate():
    if sum(hand_computer) == 21:
        print(f"Dealer has {hand_computer}. Dealer Wins!")
    elif sum(hand_user) == 21:
        print(f"You have {hand_user}. You win!")
    elif sum(hand_computer) > 21:
        print(f"Dealer has {hand_computer}. Total: {sum(hand_computer)}")
        print(f"You have {hand_user}. Total: {sum(hand_user)} You win!")
    elif sum(hand_user) == sum(hand_computer):
        print(f"Draw! Dealer has {hand_computer} you have {hand_user}.")
    elif sum(hand_user) > sum(hand_computer):
        print(f"Dealer has {hand_computer}. Total: {sum(hand_computer)}")
        print(f"You have {hand_user}. Total: {sum(hand_user)} You win!")
    elif sum(hand_user) < sum(hand_computer):
        print(f"You have {hand_user}. Total: {sum(hand_user)}")
        print(f"Dealer has {hand_computer}. Total: {sum(hand_computer)} Dealer wins!")



hand_user.append(random.choice(cards))
hand_user.append(random.choice(cards))
print(f"Your cards: {hand_user} Current total: {sum(hand_user)}")

hand_computer.append(random.choice(cards))
hand_computer.append(random.choice(cards))
print(f"The dealers first card is {hand_computer[0]}")

#game_start()
playing = True
while playing:
    if sum(hand_user)< 22:
        draw_again = input('Would you like to draw again? "Yes" or "No"\n').lower()
        if draw_again == "yes":
            draw()
        else:
            playing = False
            computer_play()
            evaluate()
    else:
        print(f"Your cards: {hand_user} Total: {sum(hand_user)}. You went over 21 You Lose")
        computer_play()
        playing = False

# Remaining Tasks
    # Show different values for the Ace depending on score
    # Create statements to show final card set of both players to the user
    # Refractor code
