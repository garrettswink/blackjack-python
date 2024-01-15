from art import logo
import random
import os
import platform

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    # If statement for blackjack, represented by 0
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # If statement for blackjack, transformation Ace (11), depending on score count
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21:
        return "You + the computer went over. You lose 😤"
    
    if user_score == computer_score:
        return "It's a draw 🙃"
    elif computer_score == 0:
        return "You lose. The computer has Blackjack 😱"
    elif user_score == 0:
        return "You win with Blackjack 😎"
    elif user_score > 21:
        return "You lose 😭"
    elif computer_score > 21 and user_score <= 21:
        return "You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
    
def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    """The for loop uses an throwaway variable of _
    The range(2) function generates a sequence of two numbers, 0 and 1, for the loop to iterate over. Each iteration of the loop represents one round of dealing a card. 
    The deal_card() function is called to randomly select a card from a predefined list each time it is invoked.    Where the deal_cards function runs twice and returns two random cards in accordance with the range
    user_cards and computer_cards are lists that store the cards dealt to the user and the computer, respectively.
    """

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print (f"Your cards are: {user_cards}, current score {user_score}")
        print (f"The computer's cards are: {computer_cards}, current score{computer_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            hit = input("Type 'h' to hit. Type 's' to stay: ").lower()
            if hit == 'h':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()

# There's a typo in some of the inputs
# It does not appear the that the ace (1 / 11 is being handled correctly)
# When I hit 21, I did not get a win. I suspect the compare function logic is fucked